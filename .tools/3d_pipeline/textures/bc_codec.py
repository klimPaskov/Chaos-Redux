"""Deterministic NumPy BC1/BC3 compressor and complete-mip DDS writer.

The encoder uses luma-extreme block endpoints followed by deterministic least-
squares endpoint refinement. It writes the legacy DXT1/DXT5 FourCCs consumed by
the installed PDX model texture route. Every emitted mip is decoded again by
``textures.dds`` before a batch can become installable.
"""

from __future__ import annotations

import math
import struct
from typing import List, Tuple

try:
    import numpy as np
except ImportError as error:  # pragma: no cover - environment guard
    raise RuntimeError("NumPy is required by the native BC texture encoder.") from error

from PIL import Image

from .dds import (
    DDSCAPS_COMPLEX,
    DDSCAPS_MIPMAP,
    DDSCAPS_TEXTURE,
    DDSD_CAPS,
    DDSD_HEIGHT,
    DDSD_LINEARSIZE,
    DDSD_MIPMAPCOUNT,
    DDSD_PIXELFORMAT,
    DDSD_WIDTH,
)


ENCODER_VERSION = "chaosx-bc-blockfit-1.2.0"
_COEFFICIENTS = np.asarray(
    [[1.0, 0.0], [0.0, 1.0], [2.0 / 3.0, 1.0 / 3.0], [1.0 / 3.0, 2.0 / 3.0]],
    dtype=np.float64,
)


def _pack_565(rgb):
    values = np.clip(np.rint(rgb), 0, 255).astype(np.uint16)
    red = ((values[..., 0].astype(np.uint32) * 31 + 127) // 255) & 0x1F
    green = ((values[..., 1].astype(np.uint32) * 63 + 127) // 255) & 0x3F
    blue = ((values[..., 2].astype(np.uint32) * 31 + 127) // 255) & 0x1F
    return ((red << 11) | (green << 5) | blue).astype(np.uint32)


def _unpack_565(codes):
    codes = np.asarray(codes, dtype=np.uint32)
    red = (codes >> 11) & 0x1F
    green = (codes >> 5) & 0x3F
    blue = codes & 0x1F
    return np.stack(
        [
            ((red << 3) | (red >> 2)),
            ((green << 2) | (green >> 4)),
            ((blue << 3) | (blue >> 2)),
        ],
        axis=-1,
    ).astype(np.float64)


def _ensure_four_color_order(code0, code1):
    code0 = code0.astype(np.uint32, copy=True)
    code1 = code1.astype(np.uint32, copy=True)
    swap = code0 <= code1
    old0 = code0.copy()
    code0[swap] = code1[swap]
    code1[swap] = old0[swap]
    equal = code0 <= code1
    code0[equal] = np.minimum(code1[equal] + 1, 0xFFFF)
    still_equal = code0 <= code1
    code1[still_equal] = code0[still_equal] - 1
    return code0.astype(np.uint16), code1.astype(np.uint16)


def _palette(endpoint0, endpoint1):
    return np.stack(
        [
            endpoint0,
            endpoint1,
            (2.0 * endpoint0 + endpoint1) / 3.0,
            (endpoint0 + 2.0 * endpoint1) / 3.0,
        ],
        axis=1,
    )


def _encode_channel_balanced_small_blocks(blocks, code0, code1):
    """Search source-derived endpoint pairs for tiny, single-mip BC1 blocks.

    Four-texel-wide diffuse mip blocks can contain several unrelated atlas
    colors. A least-squares line fit may concentrate error in one color
    channel. This bounded search uses only quantized source texels plus the
    fitted endpoints, and selects the pair minimizing the largest per-channel
    MAE before total error, matching the existing equal per-channel gate.
    """

    code0 = code0.astype(np.uint16, copy=True)
    code1 = code1.astype(np.uint16, copy=True)
    selectors_out = np.zeros((blocks.shape[0], 16), dtype=np.uint32)
    for block_index, block in enumerate(blocks):
        candidate_codes = set(int(value) for value in _pack_565(block))
        candidate_codes.add(int(code0[block_index]))
        candidate_codes.add(int(code1[block_index]))
        candidates = sorted(candidate_codes)
        best_key = None
        best_pair = None
        best_selectors = None
        for first_index, first in enumerate(candidates):
            for second in candidates[first_index + 1:]:
                endpoint0_code = max(first, second)
                endpoint1_code = min(first, second)
                endpoint0 = _unpack_565(np.asarray([endpoint0_code], dtype=np.uint32))[0]
                endpoint1 = _unpack_565(np.asarray([endpoint1_code], dtype=np.uint32))[0]
                palette = _palette(endpoint0[None, :], endpoint1[None, :])[0]
                delta = block[:, None, :] - palette[None, :, :]
                selectors = np.argmin(np.sum(delta * delta, axis=2), axis=1)
                decoded = palette[selectors]
                absolute_error = np.abs(block - decoded)
                channel_mae = np.mean(absolute_error, axis=0)
                channel_mse = np.mean(np.square(block - decoded), axis=0)
                key = (
                    float(np.max(channel_mae)),
                    float(np.sum(channel_mae)),
                    float(np.sum(channel_mse)),
                    endpoint0_code,
                    endpoint1_code,
                )
                if best_key is None or key < best_key:
                    best_key = key
                    best_pair = (endpoint0_code, endpoint1_code)
                    best_selectors = selectors
        if best_pair is None:
            continue
        code0[block_index] = best_pair[0]
        code1[block_index] = best_pair[1]
        selectors_out[block_index] = best_selectors.astype(np.uint32)
    return code0, code1, selectors_out


def _encode_color_blocks(blocks, *, balance_small_channels: bool = False):
    """Encode `(block_count, 16, 3)` RGB blocks in four-color BC mode."""

    block_count = blocks.shape[0]
    if block_count == 0:
        return b""
    means = np.mean(blocks, axis=1)
    centered = blocks - means[:, None, :]
    covariance = np.einsum("bni,bnj->bij", centered, centered)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    principal = eigenvectors[:, :, -1]
    # Eigenvector signs are mathematically arbitrary. Canonicalize each axis
    # so identical input blocks generate identical endpoint ordering.
    for channel in range(3):
        unset = np.all(np.abs(principal[:, :channel]) <= 1e-12, axis=1) if channel else np.ones(block_count, dtype=bool)
        flip = unset & (principal[:, channel] < 0)
        principal[flip] *= -1.0
    projections = np.einsum("bni,bi->bn", centered, principal)
    low_index = np.argmin(projections, axis=1)
    high_index = np.argmax(projections, axis=1)
    rows = np.arange(block_count)
    endpoint0 = blocks[rows, high_index].copy()
    endpoint1 = blocks[rows, low_index].copy()
    code0, code1 = _ensure_four_color_order(_pack_565(endpoint0), _pack_565(endpoint1))

    for _ in range(4):
        endpoint0 = _unpack_565(code0)
        endpoint1 = _unpack_565(code1)
        palette = _palette(endpoint0, endpoint1)
        delta = blocks[:, :, None, :] - palette[:, None, :, :]
        selectors = np.argmin(np.sum(delta * delta, axis=3), axis=2)
        coefficients = _COEFFICIENTS[selectors]
        coefficient_a = coefficients[:, :, 0]
        coefficient_b = coefficients[:, :, 1]
        aa = np.sum(coefficient_a * coefficient_a, axis=1)
        ab = np.sum(coefficient_a * coefficient_b, axis=1)
        bb = np.sum(coefficient_b * coefficient_b, axis=1)
        rhs_a = np.einsum("bi,bic->bc", coefficient_a, blocks)
        rhs_b = np.einsum("bi,bic->bc", coefficient_b, blocks)
        determinant = aa * bb - ab * ab
        valid = determinant > 1e-10
        fitted0 = endpoint0.copy()
        fitted1 = endpoint1.copy()
        fitted0[valid] = (
            rhs_a[valid] * bb[valid, None] - rhs_b[valid] * ab[valid, None]
        ) / determinant[valid, None]
        fitted1[valid] = (
            rhs_b[valid] * aa[valid, None] - rhs_a[valid] * ab[valid, None]
        ) / determinant[valid, None]
        code0, code1 = _ensure_four_color_order(_pack_565(fitted0), _pack_565(fitted1))

    endpoint0 = _unpack_565(code0)
    endpoint1 = _unpack_565(code1)
    palette = _palette(endpoint0, endpoint1)
    delta = blocks[:, :, None, :] - palette[:, None, :, :]
    selectors = np.argmin(np.sum(delta * delta, axis=3), axis=2).astype(np.uint32)
    if balance_small_channels:
        code0, code1, selectors = _encode_channel_balanced_small_blocks(blocks, code0, code1)
    selector_bits = np.zeros(block_count, dtype=np.uint32)
    for pixel_index in range(16):
        selector_bits |= selectors[:, pixel_index] << np.uint32(2 * pixel_index)

    output = bytearray()
    for index in range(block_count):
        output.extend(struct.pack("<HHI", int(code0[index]), int(code1[index]), int(selector_bits[index])))
    return bytes(output)


def _encode_alpha_blocks(blocks):
    """Encode `(block_count, 16)` alpha blocks in the eight-alpha BC3 mode."""

    output = bytearray()
    for block in blocks:
        alpha0 = int(np.max(block))
        alpha1 = int(np.min(block))
        if alpha0 <= alpha1:
            if alpha1 == 0:
                alpha0, alpha1 = 1, 0
            else:
                alpha0, alpha1 = alpha1, alpha1 - 1
        palette = [alpha0, alpha1]
        palette.extend(((7 - step) * alpha0 + step * alpha1) // 7 for step in range(1, 7))
        values = block.astype(np.int16)
        candidates = np.asarray(palette, dtype=np.int16)
        selectors = np.argmin(np.abs(values[:, None] - candidates[None, :]), axis=1)
        bits = 0
        for pixel_index, selector in enumerate(selectors):
            bits |= int(selector) << (3 * pixel_index)
        output.extend(bytes((alpha0, alpha1)))
        output.extend(bits.to_bytes(6, "little"))
    return bytes(output)


def _block_view(image: Image.Image):
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8)
    height, width = rgba.shape[:2]
    padded_height = max(4, ((height + 3) // 4) * 4)
    padded_width = max(4, ((width + 3) // 4) * 4)
    padded = np.pad(
        rgba,
        ((0, padded_height - height), (0, padded_width - width), (0, 0)),
        mode="edge",
    )
    blocks = (
        padded.reshape(padded_height // 4, 4, padded_width // 4, 4, 4)
        .transpose(0, 2, 1, 3, 4)
        .reshape(-1, 16, 4)
    )
    return blocks, width, height


def encode_bc_level(image: Image.Image, format_name: str) -> bytes:
    """Encode one RGBA image level as `BC1_UNORM` or `BC3_UNORM`."""

    format_name = format_name.upper()
    if format_name not in {"BC1_UNORM", "BC3_UNORM"}:
        raise ValueError("format_name must be BC1_UNORM or BC3_UNORM.")
    blocks, width, height = _block_view(image)
    rgb = blocks[:, :, :3].astype(np.float64)
    color_data = _encode_color_blocks(
        rgb,
        balance_small_channels=(format_name == "BC1_UNORM" and (width, height) == (4, 4)),
    )
    if format_name == "BC1_UNORM":
        if any(alpha != 255 for alpha in image.convert("RGBA").getchannel("A").getdata()):
            raise ValueError("BC1 delivery is only allowed when diffuse alpha is unused/opaque.")
        return color_data
    alpha_data = _encode_alpha_blocks(blocks[:, :, 3])
    combined = bytearray()
    for index in range(blocks.shape[0]):
        combined.extend(alpha_data[index * 8:index * 8 + 8])
        combined.extend(color_data[index * 8:index * 8 + 8])
    return bytes(combined)


def build_mip_chain(image: Image.Image) -> List[Image.Image]:
    """Generate independent-channel mip sources through 1x1."""

    image = image.convert("RGBA")
    chain = [image]
    width, height = image.size
    while width > 1 or height > 1:
        width = max(1, width // 2)
        height = max(1, height // 2)
        resized_channels = [
            channel.resize((width, height), Image.Resampling.LANCZOS)
            for channel in chain[-1].split()
        ]
        chain.append(Image.merge("RGBA", resized_channels))
    return chain


def encode_mip_chain(image: Image.Image, format_name: str) -> Tuple[bytes, List[Image.Image]]:
    chain = build_mip_chain(image)
    return b"".join(encode_bc_level(level, format_name) for level in chain), chain


def build_dds(image: Image.Image, format_name: str) -> Tuple[bytes, List[Image.Image]]:
    """Write a strict legacy DXT1/DXT5 DDS with the complete mip chain."""

    format_name = format_name.upper()
    if format_name not in {"BC1_UNORM", "BC3_UNORM"}:
        raise ValueError("format_name must be BC1_UNORM or BC3_UNORM.")
    chain = build_mip_chain(image)
    return build_dds_from_mips(chain, format_name)


def build_dds_from_mips(mip_chain: List[Image.Image], format_name: str) -> Tuple[bytes, List[Image.Image]]:
    """Write supplied mip sources after checking a strict complete chain."""

    format_name = format_name.upper()
    if format_name not in {"BC1_UNORM", "BC3_UNORM"}:
        raise ValueError("format_name must be BC1_UNORM or BC3_UNORM.")
    if not mip_chain:
        raise ValueError("At least one mip source is required.")
    chain = [image.convert("RGBA") for image in mip_chain]
    width, height = chain[0].size
    if width != height or width < 4 or width & (width - 1):
        raise ValueError("Native model DDS output requires a square power-of-two image of at least 4px.")
    expected_count = int(math.floor(math.log2(width))) + 1
    if len(chain) != expected_count:
        raise ValueError(f"Complete mip chain requires {expected_count} images, found {len(chain)}.")
    for level, image in enumerate(chain):
        expected_size = (max(1, width >> level), max(1, height >> level))
        if image.size != expected_size:
            raise ValueError(f"Mip {level} must be {expected_size}, found {image.size}.")
    payload = b"".join(encode_bc_level(level, format_name) for level in chain)
    block_bytes = 8 if format_name == "BC1_UNORM" else 16
    top_size = max(1, (width + 3) // 4) * max(1, (height + 3) // 4) * block_bytes
    mip_count = len(chain)
    header = bytearray(128)
    header[:4] = b"DDS "
    flags = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT | DDSD_MIPMAPCOUNT | DDSD_LINEARSIZE
    struct.pack_into("<I", header, 4, 124)
    struct.pack_into("<I", header, 8, flags)
    struct.pack_into("<I", header, 12, height)
    struct.pack_into("<I", header, 16, width)
    struct.pack_into("<I", header, 20, top_size)
    struct.pack_into("<I", header, 28, mip_count)
    struct.pack_into("<I", header, 76, 32)
    struct.pack_into("<I", header, 80, 0x4)
    header[84:88] = b"DXT1" if format_name == "BC1_UNORM" else b"DXT5"
    caps = DDSCAPS_TEXTURE | DDSCAPS_COMPLEX | DDSCAPS_MIPMAP
    struct.pack_into("<I", header, 108, caps)
    return bytes(header) + payload, chain


def encode_metrics(source: Image.Image, decoded: Image.Image) -> dict:
    """Return per-channel error and image PSNR for an encoded mip."""

    source = source.convert("RGBA")
    decoded = decoded.convert("RGBA")
    if source.size != decoded.size:
        raise ValueError("Source and decoded mip dimensions do not match.")
    source_array = np.asarray(source, dtype=np.int16)
    decoded_array = np.asarray(decoded, dtype=np.int16)
    delta = np.abs(source_array - decoded_array).astype(np.float64)
    square = np.square(source_array.astype(np.float64) - decoded_array.astype(np.float64))
    channel_names = ("R", "G", "B", "A")
    channels = {}
    for index, name in enumerate(channel_names):
        channel_delta = delta[:, :, index]
        channel_square = square[:, :, index]
        mse = float(np.mean(channel_square))
        channels[name] = {
            "mae": round(float(np.mean(channel_delta)), 6),
            "p95_abs_error": round(float(np.percentile(channel_delta, 95)), 6),
            "max_abs_error": int(np.max(channel_delta)),
            "psnr_db": None if mse == 0 else round(10.0 * math.log10((255.0 * 255.0) / mse), 6),
        }
    image_mse = float(np.mean(square[:, :, :3]))
    return {
        "size": list(source.size),
        "rgb_mae": round(float(np.mean(delta[:, :, :3])), 6),
        "rgb_psnr_db": None if image_mse == 0 else round(10.0 * math.log10((255.0 * 255.0) / image_mse), 6),
        "channels": channels,
    }
