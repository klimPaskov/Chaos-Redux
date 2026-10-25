#!/usr/bin/env python3
"""Bounded, review-first 2D sprite QA and mechanical alpha repair."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import struct
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import distance_transform_edt, binary_erosion, label

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.tools'))
from lib.game import game_dir  # noqa: E402
from lib.report import (  # noqa: E402
    Finding, PathFilter, add_arguments, exit_code, merge_json, print_findings, requested_paths,
    relative as report_relative,
)
CONVERTER = ROOT / '.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py'
PROFILES = {
    'focus': (94, 86, 2), 'decision': (34, 34, 2),
    'category': (52, 40, 3), 'idea': (64, 64, 2),
    'report': (210, 176, 0), 'news': (397, 153, 0),
    'counter-large': (76, 42, 1), 'counter-small': (30, 12, 0),
    'texticon': (18, 18, 1),
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    """Fail closed on LFS stubs, truncated inputs and unsupported DDS formats."""
    path = Path(path)
    with path.open('rb') as stream:
        prefix = stream.read(160)
    if prefix.startswith(b'version https://git-lfs.github.com/spec/v1\n'):
        raise ValueError(f'LFS pointer is not image data: {path}')
    with Image.open(path) as source:
        source.load()
        return source.convert('RGBA')


def strict_dds(path):
    """Canonical skill converter layout, not merely decoder acceptance."""
    raw = Path(path).read_bytes()
    if len(raw) < 128:
        raise ValueError('DDS header truncated')
    magic, *words = struct.unpack('<4s31I', raw[:128])
    h, w = words[2:4]
    expected = [124, 0x100f, h, w, w * 4, 0, 0, *([0] * 11),
                32, 65, 0, 32, 0xff0000, 0xff00, 0xff, 0xff000000,
                0x1000, 0, 0, 0, 0]
    if magic != b'DDS ' or words != expected or not w or not h:
        raise ValueError('Not canonical one-level legacy BGRA DDS')
    if len(raw) != 128 + w * h * 4:
        raise ValueError('DDS payload length mismatch')
    return Image.frombytes('RGBA', (w, h), raw[128:], 'raw', 'BGRA')


def write_dds(image, path, overwrite=False):
    """Call the single canonical writer, then strict-decode and compare pixels."""
    path = Path(path)
    if path.exists() and not overwrite:
        raise FileExistsError(path)
    image = image.convert('RGBA')
    spec = importlib.util.spec_from_file_location('chaos_dds_converter', CONVERTER)
    converter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(converter)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, scratch = tempfile.mkstemp(suffix='.dds', dir=path.parent)
    os.close(fd)
    scratch = Path(scratch)
    try:
        converter.write_bgra_dds(scratch, image.width, image.height, image.tobytes('raw', 'BGRA'))
        decoded = strict_dds(scratch)
        if decoded.tobytes() != image.tobytes() or load(scratch).tobytes() != image.tobytes():
            raise ValueError('DDS round-trip pixels differ')
        install_output(scratch, path, overwrite)
    finally:
        scratch.unlink(missing_ok=True)


def write_png(image, path, overwrite=False):
    path = Path(path)
    if path.exists() and not overwrite:
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, scratch = tempfile.mkstemp(suffix='.png', dir=path.parent)
    os.close(fd)
    scratch = Path(scratch)
    try:
        image.save(scratch)
        if load(scratch).tobytes() != image.tobytes():
            raise ValueError('PNG round-trip pixels differ')
        install_output(scratch, path, overwrite)
    finally:
        scratch.unlink(missing_ok=True)


def install_output(scratch, path, overwrite):
    if overwrite:
        os.replace(scratch, path)
    else:
        # Same-directory hard link is an atomic exclusive install, so another
        # worker creating the output between the exists check and here survives.
        # Unsupported filesystems fail closed instead of allowing clobbering.
        os.link(scratch, path)


def frames(image, count):
    if count < 1 or image.width % count:
        raise ValueError('Frame count must divide sheet width exactly')
    width = image.width // count
    return [image.crop((i * width, 0, (i + 1) * width, image.height)) for i in range(count)]


def chroma(rgb, delta=40):
    rgb = rgb.astype(np.int16)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return ((r > g + delta) & (b > g + delta)) | ((g > r + delta) & (g > b + delta))


def alpha_stats(image):
    a = np.asarray(image)[..., 3]
    subject = a[a > 0]
    bbox = image.getchannel('A').getbbox()
    return {'subject_alpha_mean': round(float(subject.mean()), 3) if subject.size else 0,
            'alpha_min': int(a.min()), 'alpha_max': int(a.max()),
            'subject_pixels': int(subject.size), 'opaque_pixels': int((a == 255).sum()),
            'visible_bounds': list(bbox) if bbox else None,
            'ghosted': not subject.size or float(subject.mean()) < 200}


def edge_stats(image):
    arr = np.asarray(image)
    a = arr[..., 3]
    # Include opaque boundary pixels as well as the antialiased rim.
    edge = (a > 0) & ((a < 255) | ~binary_erosion(a > 0, border_value=0))
    return {'edge_pixels': int(edge.sum()),
            'chroma_edge_pixels': int((edge & chroma(arr[..., :3])).sum())}


def defringe(image, erosion=1, spill_mask=None):
    """Erode alpha; extend nearest uncontaminated interior RGB into the rim.

    Intentionally does not key opaque backgrounds, unpremultiply colours or
    increase opacity. Such changes need source evidence and separate review.
    """
    arr = np.array(image)
    alpha = arr[..., 3]
    if spill_mask is None:
        spill_mask = np.zeros(alpha.shape, dtype=bool)
    else:
        spill_mask = np.asarray(spill_mask, dtype=bool)
        if spill_mask.shape != alpha.shape:
            raise ValueError('Spill mask must match the exact frame canvas')
    if alpha.max() == 0:
        raise ValueError('Empty subject')
    if alpha.min() > 0:
        raise ValueError('No transparent canvas; cannot infer a cut-out')
    core = (alpha >= 240) & ~chroma(arr[..., :3]) & ~spill_mask
    core = binary_erosion(core, iterations=1, border_value=0)
    if not core.any():
        raise ValueError('No uncontaminated opaque interior; repair needs source review')
    if erosion:
        # Pillow min filter repeats boundary pixels; explicit zero padding prevents clipping survival.
        padded = Image.new('L', (image.width + 2 * erosion, image.height + 2 * erosion))
        padded.paste(image.getchannel('A'), (erosion, erosion))
        alpha_out = np.asarray(padded.filter(ImageFilter.MinFilter(2 * erosion + 1))
                               .crop((erosion, erosion, image.width + erosion, image.height + erosion)))
    else:
        alpha_out = alpha.copy()
    if not alpha_out.any():
        raise ValueError('Erosion would erase subject')
    _, nearest = distance_transform_edt(~core, return_indices=True)
    # A vivid green field inside the painted object is not key spill.
    # Limit opaque recolouring to the two-pixel original boundary band.
    boundary = ~binary_erosion(alpha >= 240, iterations=2, border_value=0)
    rim = (alpha_out < 255) | ((alpha_out > 0) & chroma(arr[..., :3]) & boundary) | spill_mask
    arr[..., :3][rim] = arr[nearest[0][rim], nearest[1][rim], :3]
    arr[..., 3] = alpha_out
    return Image.fromarray(arr, 'RGBA')


def size_check(image, profile, count=1, margin=None, canvas=None):
    w, h, default_margin = PROFILES[profile]
    if canvas:
        w, h = canvas
    minimum = default_margin if margin is None else margin
    findings = []
    if image.size != (w * count, h):
        findings.append(f'canvas {image.size}, expected {(w * count, h)}')
    for i, frame in enumerate(frames(image, count)):
        bbox = frame.getchannel('A').point(lambda x: 255 if x >= 16 else 0).getbbox()
        if not bbox:
            findings.append(f'frame {i + 1}: empty subject')
            continue
        margins = [bbox[0], bbox[1], frame.width - bbox[2], frame.height - bbox[3]]
        if min(margins) < minimum:
            findings.append(f'frame {i + 1}: margins L/T/R/B {margins}, minimum {minimum}')
        if profile in ('focus', 'decision', 'category', 'idea'):
            fill = max((bbox[2] - bbox[0]) / frame.width, (bbox[3] - bbox[1]) / frame.height)
            if fill < .80:
                findings.append(f'frame {i + 1}: subject span {fill:.1%}; review undersized artwork')
    return findings


def counter_check(image, surface, reference):
    """Heuristic triage, always compared to the exact installed vanilla DDS."""
    findings = []
    if image.size != reference.size:
        findings.append(f'canvas {image.size}, reference {reference.size}')
    expected_count = 2
    art, alternate = frames(image, expected_count)
    ref_art, ref_alt = frames(reference, expected_count)
    def solid_pixels(frame):
        a = np.asarray(frame)
        return a[..., :3][a[..., 3] >= 200].astype(float)
    subject = solid_pixels(art)
    ref = solid_pixels(ref_art)
    if not subject.size or not ref.size:
        return findings + ['normal frame or reference lacks opaque subject']
    alpha = alpha_stats(art)
    reference_alpha = alpha_stats(ref_art)
    # Vanilla's antialiased silhouettes can themselves average below 200.
    # The dedicated alpha command retains the user's literal 200 threshold;
    # convention QA compares like-for-like against this exact reference.
    if alpha['alpha_max'] < 200 or alpha['subject_alpha_mean'] < reference_alpha['subject_alpha_mean'] - 25:
        findings.append('normal frame opacity substantially below the supplied vanilla reference')
    if surface == 'large':
        # Median palette distance catches painted/full-colour replacements without forcing one arbitrary green.
        distance = float(np.linalg.norm(np.median(subject, axis=0) - np.median(ref, axis=0)))
        if distance > 45:
            findings.append(f'normal frame palette differs from vanilla: RGB distance {distance:.1f}')
        spread = float(np.percentile(np.ptp(subject, axis=0), 80))
        reference_spread = float(np.percentile(np.ptp(ref, axis=0), 80))
        if spread > reference_spread + 30:
            findings.append('normal frame broad colour range; review flat green silhouette convention')
    else:
        grey = (np.ptp(subject, axis=1) < 25) & (subject.mean(axis=1) >= 160)
        if grey.mean() < .70:
            findings.append('small normal frame is not predominantly light grey/white')
    alt = np.asarray(alternate)
    opaque = alt[..., 3] >= 200
    white = opaque & (alt[..., :3].min(axis=2) > 170)
    black = opaque & (alt[..., :3].max(axis=2) < 85)
    if white.sum() < 8 or black.sum() < 4:
        findings.append('alternate frame lacks opaque white NATO field or black line glyph')
    def field_shape(frame):
        pixels = np.asarray(frame)
        mask = (pixels[..., 3] >= 200) & ((pixels[..., :3].min(axis=2) > 170)
                                        | (pixels[..., :3].max(axis=2) < 85))
        components, count = label(mask, np.ones((3, 3), dtype=bool))
        if not count:
            return 0, 0, 0
        areas = np.bincount(components.ravel())
        areas[0] = 0
        component = components == int(areas.argmax())
        ys, xs = np.where(component)
        width, height = int(xs.max() - xs.min() + 1), int(ys.max() - ys.min() + 1)
        return float(component.sum() / (width * height)), width / height, int(component.sum())
    density, aspect, area = field_shape(alternate)
    ref_density, ref_aspect, ref_area = field_shape(ref_alt)
    if area < ref_area * .25 or density < ref_density * .70 or abs(aspect - ref_aspect) > .60:
        findings.append('alternate frame lacks a coherent rectangular NATO field comparable to vanilla')
    if art.tobytes() == alternate.tobytes():
        findings.append('two frames are identical')
    return findings


def sprite_registry(root):
    """Bounded text registry reader for sheet/inventory tools, never a script rewrite."""
    entries = []
    for path in sorted((Path(root) / 'interface').rglob('*.gfx')):
        source = path.read_text(encoding='utf-8-sig')
        # Keep hashes inside quoted strings; comments cannot contain braces for scanning.
        source = re.sub(r'"[^"\n]*"|#[^\n]*', lambda m: m[0] if m[0].startswith('"') else '', source)
        for match in re.finditer(r'(?:spriteType|frameAnimatedSpriteType|corneredTileSpriteType)\s*=\s*\{', source, re.I):
            # Comment removal keeps every newline, so offsets still map to source lines.
            line = source.count('\n', 0, match.start()) + 1
            depth, end = 1, match.end()
            quoted = False
            while end < len(source) and depth:
                char = source[end]
                if char == '"':
                    quoted = not quoted
                if not quoted:
                    depth += (char == '{') - (char == '}')
                end += 1
            block = source[match.end():end]
            name = re.search(r'\bname\s*=\s*"?([\w.-]+)', block, re.I)
            texture = re.search(r'\btexturefile\s*=\s*"([^"]+)"', block, re.I)
            count = re.search(r'\bnoOfFrames\s*=\s*(\d+)', block, re.I)
            if name and texture:
                basename = path.stem
                group = basename[:3] if re.match(r'\d{3}_', basename) else ('shared_' + basename if basename.startswith('chaosx') else basename)
                entries.append({'group': group, 'sprite': name[1], 'texture': texture[1].replace('//', '/'),
                                'frames': int(count[1]) if count else 1, 'registry': path.relative_to(root).as_posix(),
                                'line': line})
    return entries


# ---------------------------------------------------------------------------
# Repository-wide read-only conformance checks (`sprites`, `flags`, `achievements`, `binaries`, `audit`).
# They follow the `.tools/lib/report.py` contract. Each rule cites its source:
# - GFX-FRAME-WIDTH (warning): a horizontal strip is sliced into `noOfFrames` equal frames, so an uneven
#   width shifts every later frame (vanilla `building_icon_strip.dds`: 1426 px / 31 frames = 46 px). Vanilla
#   itself ships 79 of 1798 multi-frame sprites with uneven widths, so the engine tolerates it and the
#   message gives the per-frame width for review.
# - GFX-FLAG-SIZE (error): normal, medium and small flags are 82x52, 41x26 and 10x7 (event-assets skill flag
#   rules; 2202 of 2203 vanilla files per folder).
# - GFX-FLAG-LADDER (warning): the skill requires all three sizes before a flag is complete, but vanilla
#   ships incomplete ladders (89 normal flags without a small file), so a gap is not an engine failure.
# - GFX-FLAG-ORIGIN (warning, decision D4): the skill forbids top-origin flag TGAs; vanilla ships 5.
# - GFX-ACHIEVEMENT-SIZE (error): achievement art is 64x64 (882 of 882 vanilla files;
#   `process_achievement_icons.py`). The base, `_grey` and `_not_eligible` files of every defined
#   achievement are already required by `audit_asset_wiring_static.py` (implicit achievement-art rule).
# - GFX-LFS-POINTER and GFX-TRUNCATED (error): a runtime binary must hold real data. Header parsing accepts
#   legacy, DX10, compressed and mipmapped DDS, which the game loads, rather than requiring Pillow support.
# ---------------------------------------------------------------------------

LFS_POINTER = b'version https://git-lfs.github.com/spec/v1'
FLAG_LADDER = {'': (82, 52), 'medium': (41, 26), 'small': (10, 7)}
ACHIEVEMENT_SIZE = (64, 64)
RUNTIME_BINARY_DIRS = ('gfx', 'sound', 'music')
RUNTIME_BINARY_SUFFIXES = {'.dds', '.tga', '.png', '.mesh', '.anim', '.wav', '.ogg'}
GFX_LEVELS = {
    'GFX-FRAME-WIDTH': 'warning', 'GFX-FLAG-SIZE': 'error', 'GFX-FLAG-LADDER': 'warning', 'GFX-FLAG-ORIGIN': 'warning',
    'GFX-ACHIEVEMENT-SIZE': 'error', 'GFX-LFS-POINTER': 'error', 'GFX-TRUNCATED': 'error',
}
# Bytes per 4x4 block (compressed) or per pixel (uncompressed) for DDS formats with a known payload size.
DDS_BLOCK_BYTES = {b'DXT1': 8, b'DXT2': 16, b'DXT3': 16, b'DXT4': 16, b'DXT5': 16, b'ATI1': 8, b'BC4U': 8, b'ATI2': 16, b'BC5U': 16}
DXGI_BLOCK_BYTES = {71: 8, 72: 8, 74: 16, 75: 16, 77: 16, 78: 16, 80: 8, 81: 8, 83: 16, 84: 16, 98: 16, 99: 16}
DXGI_PIXEL_BYTES = {28: 4, 29: 4, 87: 4, 91: 4}


def gfx_finding(rule, path, line, message, check='gfx'):
    return Finding(check, rule, GFX_LEVELS[rule], report_relative(path), line, message)


def header_size(path):
    """Return (width, height) from the file header without decoding pixels."""
    raw = Path(path).read_bytes()[:64]
    if raw.startswith(LFS_POINTER):
        raise ValueError('Git LFS pointer, not image data')
    if raw[:4] == b'DDS ' and len(raw) >= 20:
        height, width = struct.unpack_from('<2I', raw, 12)
        return width, height
    if raw[:8] == b'\x89PNG\r\n\x1a\n' and len(raw) >= 24:
        return struct.unpack_from('>2I', raw, 16)
    if Path(path).suffix.lower() == '.tga' and len(raw) >= 18:
        return struct.unpack_from('<2H', raw, 12)
    with Image.open(path) as image:
        return image.size


def dds_payload_bytes(header):
    """Minimum payload length for a DDS header, or None when the format's size is not known here."""
    height, width = struct.unpack_from('<2I', header, 12)
    flags, mips = struct.unpack_from('<I', header, 8)[0], struct.unpack_from('<I', header, 28)[0]
    pf_flags, fourcc, bit_count = struct.unpack_from('<I', header, 80)[0], header[84:88], struct.unpack_from('<I', header, 88)[0]
    caps2 = struct.unpack_from('<I', header, 112)[0]
    levels = mips if flags & 0x20000 and mips else 1
    block = pixel = None
    if pf_flags & 0x4 and fourcc == b'DX10':
        if len(header) < 148 or struct.unpack_from('<I', header, 140)[0] != 1:
            return None  # texture arrays are outside the runtime formats checked here
        dxgi = struct.unpack_from('<I', header, 128)[0]
        block, pixel = DXGI_BLOCK_BYTES.get(dxgi), DXGI_PIXEL_BYTES.get(dxgi)
    elif pf_flags & 0x4:
        block = DDS_BLOCK_BYTES.get(fourcc)
    elif pf_flags & 0x40 and bit_count % 8 == 0:
        pixel = bit_count // 8
    if caps2 & 0x200 or (block is None and pixel is None):
        return None  # cube maps and unlisted formats
    total = 0
    for level in range(levels):
        w, h = max(1, width >> level), max(1, height >> level)
        total += ((w + 3) // 4) * ((h + 3) // 4) * block if block else w * h * pixel
    return total


def binary_problem(path):
    """Return (rule, message) when a runtime binary is not usable data, else None."""
    path = Path(path)
    size = path.stat().st_size
    with path.open('rb') as stream:
        head = stream.read(160)
    if head.startswith(LFS_POINTER):
        return 'GFX-LFS-POINTER', 'is a Git LFS pointer, not the binary; run git lfs checkout for this path'
    suffix = path.suffix.lower()
    if suffix == '.dds':
        if head[:4] != b'DDS ' or size < 128:
            return 'GFX-TRUNCATED', 'has no complete DDS header'
        header_length = 148 if head[84:88] == b'DX10' else 128
        payload = dds_payload_bytes(head)
        if payload is not None and size < header_length + payload:
            return 'GFX-TRUNCATED', f'holds {size} bytes; its DDS header needs at least {header_length + payload}'
    elif suffix == '.tga':
        if size < 18:
            return 'GFX-TRUNCATED', 'has no complete TGA header'
        id_length, colour_map_type, image_type = head[0], head[1], head[2]
        width, height = struct.unpack_from('<2H', head, 12)
        if image_type in (2, 3) and colour_map_type == 0:
            needed = 18 + id_length + width * height * (head[16] // 8)
            if size < needed:
                return 'GFX-TRUNCATED', f'holds {size} bytes; its TGA header needs at least {needed}'
    elif suffix == '.png' and head[:8] != b'\x89PNG\r\n\x1a\n':
        return 'GFX-TRUNCATED', 'does not start with the PNG signature'
    elif suffix == '.wav' and not (head[:4] == b'RIFF' and head[8:12] == b'WAVE'):
        return 'GFX-TRUNCATED', 'does not start with a RIFF/WAVE header'
    elif suffix == '.ogg' and head[:4] != b'OggS':
        return 'GFX-TRUNCATED', 'does not start with an Ogg page header'
    return None


def check_binaries(root=ROOT, paths=None):
    selector, findings = PathFilter(paths), []
    for folder in RUNTIME_BINARY_DIRS:
        base = Path(root) / folder
        if not base.is_dir():
            continue
        for path in sorted(base.rglob('*')):
            if path.suffix.lower() not in RUNTIME_BINARY_SUFFIXES or not path.is_file():
                continue
            rel = path.relative_to(root).as_posix()
            if not selector.matches(rel):
                continue
            problem = binary_problem(path)
            if problem:
                findings.append(gfx_finding(problem[0], rel, 0, f'{rel} {problem[1]}'))
    return findings


def resolve_texture(texture, root, vanilla):
    """Find a registered texture in the mod, then vanilla; a `.tga` reference also matches a same-stem `.dds`."""
    for base in (Path(root), Path(vanilla)):
        for candidate in (texture, texture[:-4] + '.dds' if texture.lower().endswith('.tga') else None):
            if candidate and (base / candidate).is_file():
                return base / candidate
    return None


def check_sprites(root=ROOT, paths=None, vanilla=None):
    selector, findings = PathFilter(paths), []
    vanilla = vanilla or game_dir()
    for entry in sprite_registry(root):
        if entry['frames'] <= 1:
            continue
        if paths and not (selector.matches(entry['registry']) or selector.matches(entry['texture'])):
            continue
        texture = resolve_texture(entry['texture'], root, vanilla)
        if texture is None:
            continue  # a missing texture is reported by audit_asset_wiring_static.py
        try:
            width, _ = header_size(texture)
        except Exception:
            continue  # unreadable binaries are reported by the binaries check
        if width % entry['frames']:
            findings.append(gfx_finding('GFX-FRAME-WIDTH', entry['registry'], entry['line'],
                f"{entry['sprite']}: {entry['texture']} is {width} px wide, which does not divide into "
                f"noOfFrames = {entry['frames']} ({width / entry['frames']:.2f} px per frame)"))
    return findings


def check_flags(root=ROOT, paths=None):
    selector, findings, stems = PathFilter(paths), [], {}
    for folder in FLAG_LADDER:
        base = Path(root) / 'gfx' / 'flags' / folder
        stems[folder] = {p.stem: p for p in base.glob('*.tga')} if base.is_dir() else {}
    for folder, (want_w, want_h) in FLAG_LADDER.items():
        for stem, path in sorted(stems[folder].items()):
            rel = path.relative_to(root).as_posix()
            if not selector.matches(rel):
                continue
            label = folder or 'normal'
            try:
                width, height = header_size(path)
            except Exception as error:
                findings.append(gfx_finding('GFX-FLAG-SIZE', rel, 0, f'{label} flag {stem} cannot be read: {error}'))
                continue
            if (width, height) != (want_w, want_h):
                findings.append(gfx_finding('GFX-FLAG-SIZE', rel, 0, f'{label} flag {stem} is {width}x{height}, not {want_w}x{want_h}'))
            missing = [other or 'normal' for other in FLAG_LADDER if other != folder and stem not in stems[other]]
            if missing:
                findings.append(gfx_finding('GFX-FLAG-LADDER', rel, 0, f'{label} flag {stem} has no {" or ".join(missing)} size'))
            if path.read_bytes()[17:18] and path.read_bytes()[17] & 0x20:
                findings.append(gfx_finding('GFX-FLAG-ORIGIN', rel, 0, f'{label} flag {stem} is stored top-origin'))
    return findings


def check_achievements(root=ROOT, paths=None):
    selector, findings = PathFilter(paths), []
    base = Path(root) / 'gfx' / 'achievements'
    files = {p.stem: p for p in base.glob('*.dds')} if base.is_dir() else {}
    for stem, path in sorted(files.items()):
        rel = path.relative_to(root).as_posix()
        if not selector.matches(rel):
            continue
        try:
            size = header_size(path)
        except Exception:
            continue  # unreadable binaries are reported by the binaries check
        if tuple(size) != ACHIEVEMENT_SIZE:
            findings.append(gfx_finding('GFX-ACHIEVEMENT-SIZE', rel, 0, f'achievement art {stem} is {size[0]}x{size[1]}, not 64x64'))
    return findings


CONFORMANCE_CHECKS = {
    'sprites': check_sprites, 'flags': check_flags, 'achievements': check_achievements, 'binaries': check_binaries,
}


def run_conformance(command, args):
    paths = requested_paths(args)
    chosen = CONFORMANCE_CHECKS if command == 'audit' else {command: CONFORMANCE_CHECKS[command]}
    findings = sorted((f for check in chosen.values() for f in check(ROOT, paths)),
                      key=lambda f: (f.path, f.line, f.rule, f.message))
    print_findings('gfx', findings)
    if args.json:
        merge_json(Path(args.json), findings, GFX_LEVELS)
    return exit_code(findings, args.fail_on)


def sheet(entries, root, out, label='review'):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    grouped = {}
    for item in entries:
        grouped.setdefault(item['group'], []).append(item)
    artifacts = []
    for group, items in grouped.items():
        for start in range(0, len(items), 24):
            chunk = items[start:start + 24]
            cell_w, cell_h = 280, 220
            canvas = Image.new('RGB', (cell_w * 4, cell_h * math.ceil(len(chunk) / 4)), '#181818')
            draw = ImageDraw.Draw(canvas)
            for n, entry in enumerate(chunk):
                x, y = n % 4 * cell_w, n // 4 * cell_h
                try:
                    source = load(Path(root) / entry['texture'])
                    native = frames(source, entry['frames'])[0]
                    bg = Image.new('RGBA', (cell_w - 8, 170), '#5c5c5c')
                    bd = ImageDraw.Draw(bg)
                    for cy in range(0, 170, 8):
                        for cx in range(0, cell_w - 8, 8):
                            if (cx // 8 + cy // 8) % 2:
                                bd.rectangle((cx, cy, cx + 7, cy + 7), fill='#787878')
                    # Native view plus enlarged smooth preview; show every frame in separate tiles if requested by caller.
                    enlarged = native.copy()
                    enlarged.thumbnail((150, 155))
                    if native.width <= 94 and native.height <= 86:
                        enlarged = native.resize((native.width * 2, native.height * 2), Image.Resampling.BICUBIC)
                        enlarged.thumbnail((150, 155))
                    bg.alpha_composite(native, (2, max(0, (170 - native.height) // 2))) if native.width <= 110 and native.height <= 170 else None
                    bg.alpha_composite(enlarged, (116, (170 - enlarged.height) // 2))
                    canvas.paste(bg.convert('RGB'), (x + 4, y + 4))
                    stats = alpha_stats(native)
                    caption = f'{source.width}x{source.height}, {entry["frames"]}f, alpha {stats["subject_alpha_mean"]}'
                except Exception as error:
                    caption = f'ERROR: {error}'
                draw.text((x + 4, y + 178), entry['sprite'].removeprefix('GFX_')[:42], fill='white')
                draw.text((x + 4, y + 192), caption[:44], fill='#c9b890')
            path = out / f'{group}_{label}_{start // 24 + 1}.png'
            canvas.save(path)
            artifacts.append(str(path))
    return artifacts


def input_items(args):
    items = [(Path(p), args.frames or 1) for p in args.inputs]
    if args.list:
        data = json.loads(Path(args.list).read_text(encoding='utf-8-sig'))
        rows = data if isinstance(data, list) else data['assets']
        for row in rows:
            path = Path(row if isinstance(row, str) else row.get('texture', row.get('path')))
            count = args.frames if args.frames is not None else (1 if isinstance(row, str) else row.get('frames', 1))
            items.append((path, int(count)))
    if not items:
        raise ValueError('Supply explicit image paths or --list; no implicit whole-repository pass')
    unique = {}
    for path, count in items:
        key = path.resolve()
        if key in unique and unique[key][1] != count:
            raise ValueError(f'Conflicting declared frame counts for {path}')
        unique[key] = (path, count)
    return list(unique.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for command in ('alpha', 'size', 'defringe', 'dds', 'counter'):
        p = sub.add_parser(command)
        p.add_argument('inputs', nargs='*')
        p.add_argument('--list', help='JSON array of paths or objects with texture/path')
        p.add_argument('--json', help='Write full machine-readable results')
        p.add_argument('--frames', type=int, default=2 if command == 'counter' else None,
                       help='Override horizontal frame count; otherwise use manifest frames or 1 (counter: 2)')
        if command in ('defringe', 'dds'):
            p.add_argument('--out', required=True, help='Separate output directory')
            p.add_argument('--root', default='.', help='Preserve paths relative to this root under output')
            p.add_argument('--force', action='store_true', help='Replace an existing output, never authorizes input overwrite')
        if command == 'defringe':
            p.add_argument('--erosion', type=int, choices=(0, 1), default=1)
            p.add_argument('--spill-mask', help='Reviewed grayscale PNG mask: nonzero pixels explicitly select opaque key spill; exact sheet dimensions')
        if command == 'size':
            p.add_argument('--profile', required=True, choices=PROFILES)
            p.add_argument('--margin', type=int)
            p.add_argument('--canvas', nargs=2, type=int, help='Verified consumer frame canvas W H')
        if command == 'counter':
            p.add_argument('--surface', required=True, choices=('large', 'small'))
            p.add_argument('--reference', required=True, help='Exact vanilla two-frame DDS for this surface')
    p = sub.add_parser('sheet')
    p.add_argument('--root', default=str(ROOT))
    p.add_argument('--groups', nargs='+', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--label', default='review')
    for command in (*CONFORMANCE_CHECKS, 'audit'):
        p = sub.add_parser(command, help='read-only repository conformance check (see the module comments)')
        p.add_argument('--json', help='also write the findings as JSON')
        add_arguments(p)
    args = parser.parse_args()
    if args.command in CONFORMANCE_CHECKS or args.command == 'audit':
        return run_conformance(args.command, args)
    if args.command == 'counter' and args.frames != 2:
        parser.error('Counter convention checks require exactly two frames')
    if args.command == 'sheet':
        entries = [e for e in sprite_registry(Path(args.root)) if e['group'] in args.groups]
        if not entries:
            parser.error('No matching registered sprites')
        print(json.dumps(sheet(entries, args.root, args.out, args.label), indent=2))
        return 0
    items = input_items(args)
    protected = {path.resolve() for path, _ in items}
    if args.list:
        protected.add(Path(args.list).resolve())
    if getattr(args, 'spill_mask', None):
        protected.add(Path(args.spill_mask).resolve())
    if args.json:
        report_path = Path(args.json).resolve()
        outputs = set()
        if args.command in ('dds', 'defringe'):
            for path, _ in items:
                relative = path.resolve().relative_to(Path(args.root).resolve())
                outputs.add((Path(args.out) / relative).with_suffix('.dds' if args.command == 'dds' else '.png').resolve())
        if report_path in protected | outputs:
            parser.error('--json cannot overwrite an input, input list, or image output')
    rows, failed = [], False
    for path, frame_count in items:
        row = {'path': str(path)}
        try:
            row['sha256'] = digest(path)
            image = load(path)
            row['size'] = list(image.size)
            split = frames(image, frame_count)
            row['frames'] = [dict(alpha_stats(f), **edge_stats(f)) for f in split]
            if args.command == 'alpha':
                row['findings'] = [f'frame {i + 1}: subject alpha mean below 200' for i, f in enumerate(split) if alpha_stats(f)['ghosted']]
            elif args.command == 'size':
                row['findings'] = size_check(image, args.profile, frame_count, args.margin, args.canvas)
            elif args.command == 'counter':
                row['findings'] = counter_check(image, args.surface, load(args.reference))
            else:
                root = Path(args.root).resolve()
                relative = path.resolve().relative_to(root)
                out = (Path(args.out) / relative).with_suffix('.dds' if args.command == 'dds' else '.png')
                if out.resolve() == path.resolve():
                    raise ValueError('Input overwrite forbidden; use separate review output')
                if out.exists() and not args.force:
                    raise FileExistsError(out)
                if args.command == 'defringe':
                    masks = [None] * frame_count
                    if args.spill_mask:
                        mask = load(args.spill_mask)
                        if mask.size != image.size:
                            raise ValueError('Spill mask must match exact sheet canvas')
                        masks = [np.asarray(f.convert('L')) > 0 for f in frames(mask, frame_count)]
                    repaired = [defringe(f, args.erosion, m) for f, m in zip(split, masks)]
                    result = Image.new('RGBA', image.size)
                    for i, f in enumerate(repaired):
                        result.paste(f, (i * f.width, 0))
                    write_png(result, out, args.force)
                else:
                    result = image
                    write_dds(result, out, args.force)
                row['output'] = str(out)
                row['output_sha256'] = digest(out)
                row['after'] = [dict(alpha_stats(f), **edge_stats(f)) for f in frames(result, frame_count)]
                row['findings'] = []
            if row['findings']:
                failed = True
        except Exception as error:
            row['error'] = str(error)
            failed = True
        rows.append(row)
    if args.json:
        target = Path(args.json)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'checked': len(rows), 'flagged': sum(bool(r.get('findings') or r.get('error')) for r in rows), 'results': rows}, indent=2))
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
