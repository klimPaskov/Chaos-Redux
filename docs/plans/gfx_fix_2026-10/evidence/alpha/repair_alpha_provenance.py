"""Mechanical alpha/edge repair requested by the October graphics review."""
from pathlib import Path
import hashlib
import importlib.util
import json
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('dds', ROOT / '.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py')
dds = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dds)

def largest(mask, minimum=10):
    labels, n = ndi.label(mask)
    counts = np.bincount(labels.ravel())
    keep = counts >= minimum
    keep[0] = False
    return keep[labels]

def repair(p, family):
    raw = p.read_bytes()
    original_path = OUT / 'before' / family / (p.stem + '.png')
    original = Image.open(original_path if original_path.exists() else p).convert('RGBA')
    a = np.array(original)
    alpha = a[:, :, 3]
    rgb = a[:, :, :3].astype(float)
    if family == '015':
        purple = (rgb[:, :, 0] > rgb[:, :, 1] * 1.1 + 4) & (rgb[:, :, 2] > rgb[:, :, 1] * 1.1 + 4)
        core = (alpha >= 230) & ~purple
        distance, near = ndi.distance_transform_edt(~core, return_indices=True)
        edge = (alpha > 0) & ((alpha < 230) | purple)
        a[:, :, :3][edge] = a[near[0], near[1], :3][edge]
        # Keep every inherited thin beam, cord, and scaffold tip intact.
        # Chroma removal changes RGB only; this family's alpha is preserved.
        stray_regions = {
            'goal_utopia_auditors': (89, 35, 93, 47),
            'goal_utopia_granaries': (88, 44, 92, 55),
            'goal_utopia_measures': (61, 0, 71, 4),
        }
        if p.stem in stray_regions:
            x0, y0, x1, y1 = stray_regions[p.stem]
            labels, _ = ndi.label(alpha > 0, structure=np.ones((3, 3)))
            counts = np.bincount(labels.ravel())
            marks = [n for n in np.unique(labels[y0:y1, x0:x1]) if n and counts[n] < 80]
            assert marks, ('Reviewed detached mark not found', p)
            removed = np.isin(labels, marks)
            alpha[removed] = 0
            a[:, :, :3][removed] = 0
    else:
        silhouette = largest(alpha > 80, minimum=10)
        silhouette = ndi.binary_fill_holes(silhouette)
        interior = ndi.binary_erosion(silhouette)
        alpha[interior] = 255
        alpha[~ndi.binary_dilation(silhouette)] = 0
        # Preserve the original antialiasing only at the surviving outline.
        alpha[silhouette & (alpha == 0)] = 255
    a[:, :, 3] = alpha
    preview_path = OUT / 'processed' / family / (p.stem + '.png')
    original_path.parent.mkdir(parents=True, exist_ok=True)
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    if not original_path.exists():
        original.save(original_path)
    Image.fromarray(a).save(preview_path)
    processed = Image.fromarray(a)
    dds.write_bgra_dds(p, processed.width, processed.height, processed.tobytes('raw', 'BGRA'))
    b = p.read_bytes()
    decoded = np.array(Image.open(p).convert('RGBA'))
    assert np.array_equal(a, decoded), p
    assert len(b) == 128 + original.width * original.height * 4
    previous = OUT / 'alpha_results.json'
    prior = {r['path']: r for r in json.loads(previous.read_text())} if previous.exists() else {}
    path = p.relative_to(ROOT).as_posix()
    return {'path': path, 'before_sha256': prior.get(path, {}).get('before_sha256', hashlib.sha256(raw).hexdigest()), 'after_sha256': hashlib.sha256(b).hexdigest(), 'size': list(original.size), 'roundtrip_equal': True}

if __name__ == '__main__':
    paths = [(p, '015') for p in sorted((ROOT / 'gfx/interface/goals/015_utopia_manifesto').glob('goal_utopia_*.dds'))]
    paths += [(ROOT / 'gfx/interface/goals/019_infantry_spawn' / (n + '.dds'), '019') for n in ['infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks', 'infantry_spawn_derivative_zombie_a_realm_of_base_dead']]
    paths += [(ROOT / 'gfx/interface/decisions/019_infantry_spawn/prototype_cannibalization.dds', '019')]
    report = [repair(p, family) for p, family in paths]
    (OUT / 'alpha_results.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(len(report), 'repaired and DDS round-trip verified')
