"""Strict legacy BC1/BC3 DDS parsing and pixel decoding for pipeline QA.

The runtime model-texture route uses legacy DXT1/BC1 and DXT5/BC3 DDS files.
This module validates the complete file, not just its 128-byte signature, and
decodes every mip format used by the delivery gate without relying on Blender.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import struct
from typing import Tuple


DDS_HEADER_BYTES = 128
DDSD_CAPS = 0x1
DDSD_HEIGHT = 0x2
DDSD_WIDTH = 0x4
DDSD_PITCH = 0x8
DDSD_PIXELFORMAT = 0x1000
DDSD_MIPMAPCOUNT = 0x20000
DDSD_LINEARSIZE = 0x80000
DDPF_FOURCC = 0x4
DDPF_RGB = 0x40
DDPF_ALPHAPIXELS = 0x1
DDSCAPS_COMPLEX = 0x8
DDSCAPS_TEXTURE = 0x1000
DDSCAPS_MIPMAP = 0x400000


class DdsError(ValueError):
    """The DDS header, payload, or compressed pixels are invalid."""


@dataclass(frozen=True)
class DdsHeader:
    width: int
    height: int
    mip_count: int
    fourcc: str
    flags: int
    caps: int
    payload_offset: int
    mip_sizes: Tuple[int, ...]
    pixel_layout: str
    red_mask: int = 0
    green_mask: int = 0
    blue_mask: int = 0
    alpha_mask: int = 0

    @property
    def format_name(self) -> str:
        if self.pixel_layout == "BC1":
            return "BC1_UNORM"
        if self.pixel_layout == "BC3":
            return "BC3_UNORM"
        return self.pixel_layout


def _mip_dimensions(width: int, height: int, level: int) -> Tuple[int, int]:
    return max(1, width >> level), max(1, height >> level)


def _mip_payload_size(width: int, height: int, block_bytes: int) -> int:
    return max(1, (width + 3) // 4) * max(1, (height + 3) // 4) * block_bytes


def _full_mip_count(width: int, height: int) -> int:
    return int(math.floor(math.log2(max(width, height)))) + 1


def parse_dds_header(
    data: bytes,
    file_size: int = None,
    *,
    require_full_mips: bool = True,
    min_dimension: int = 4,
    max_dimension: int = 1024,
    allow_uncompressed_bgra: bool = False,
) -> DdsHeader:
    """Parse a bounded legacy BC1/BC3 DDS and verify its payload length.

    The strict delivery mode requires square power-of-two textures and the
    complete chain through 1x1. Set a test-sized dimension range only for
    focused parser fixtures; production delivery uses 128..1024 pixels.
    """

    if len(data) < DDS_HEADER_BYTES:
        raise DdsError("DDS is shorter than the required 128-byte header.")
    if data[:4] != b"DDS ":
        raise DdsError("DDS magic is missing.")
    if file_size is None:
        file_size = len(data)
    if file_size < DDS_HEADER_BYTES:
        raise DdsError("DDS file length is shorter than its header.")

    values = struct.unpack_from("<31I", data, 4)
    header_size = values[0]
    flags = values[1]
    height = values[2]
    width = values[3]
    linear_size = values[4]
    depth = values[5]
    declared_mips = values[6]
    pixel_format_size = values[18]
    pixel_format_flags = values[19]
    fourcc_bytes = struct.pack("<I", values[20])
    rgb_bit_count = values[21]
    red_mask, green_mask, blue_mask, alpha_mask = values[22:26]
    caps = values[26]
    caps2 = values[27]

    if header_size != 124 or pixel_format_size != 32:
        raise DdsError("DDS_HEADER or DDS_PIXELFORMAT has an invalid size.")
    required_flags = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PIXELFORMAT
    if flags & required_flags != required_flags:
        raise DdsError("DDS header is missing required caps, dimensions, or pixel-format flags.")
    if caps & DDSCAPS_TEXTURE == 0:
        raise DdsError("DDSCAPS_TEXTURE is missing.")
    if depth not in (0, 1) or caps2 != 0:
        raise DdsError("Only a single 2D texture without cube, volume, or array data is supported.")
    if width != height or width < min_dimension or width > max_dimension:
        raise DdsError("Texture dimensions must be square and inside the configured budget.")
    if width & (width - 1):
        raise DdsError("Texture dimensions must be a power of two for the full mip chain.")
    pixel_layout = ""
    if pixel_format_flags & DDPF_FOURCC:
        try:
            fourcc = fourcc_bytes.decode("ascii")
        except UnicodeDecodeError as error:
            raise DdsError("DDS FourCC is not ASCII.") from error
        if fourcc not in {"DXT1", "DXT5"}:
            raise DdsError("Only legacy DXT1/BC1 and DXT5/BC3 are accepted.")
        pixel_layout = "BC1" if fourcc == "DXT1" else "BC3"
    elif (
        allow_uncompressed_bgra
        and fourcc_bytes == b"\0\0\0\0"
        and pixel_format_flags == (DDPF_RGB | DDPF_ALPHAPIXELS)
        and rgb_bit_count == 32
        and (red_mask, green_mask, blue_mask, alpha_mask)
        == (0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000)
    ):
        pixel_layout = "BGRA8"
    else:
        raise DdsError("Compressed FourCC format is required (input-only BGRA is disabled).")

    expected_mips = _full_mip_count(width, height)
    mip_count = declared_mips if flags & DDSD_MIPMAPCOUNT else 1
    if mip_count < 1:
        raise DdsError("DDS mip count must be positive.")
    if require_full_mips and mip_count != expected_mips:
        raise DdsError(
            "DDS must contain a complete mip chain: "
            f"expected {expected_mips}, found {mip_count}."
        )
    if mip_count > expected_mips:
        raise DdsError("DDS declares more mip levels than its dimensions allow.")
    if require_full_mips:
        required_caps = DDSCAPS_COMPLEX | DDSCAPS_MIPMAP
        if caps & required_caps != required_caps:
            raise DdsError("A full mip chain requires DDSCAPS_COMPLEX and DDSCAPS_MIPMAP.")
        if flags & (DDSD_MIPMAPCOUNT | DDSD_LINEARSIZE) != (DDSD_MIPMAPCOUNT | DDSD_LINEARSIZE):
            raise DdsError("Compressed mipmapped DDS must declare mip count and linear size.")

    if pixel_layout == "BGRA8" and mip_count != 1:
        raise DdsError("Only one-level uncompressed BGRA inputs are supported.")
    block_bytes = 8 if pixel_layout == "BC1" else 16
    mip_sizes = []
    for level in range(mip_count):
        mip_width, mip_height = _mip_dimensions(width, height, level)
        if pixel_layout == "BGRA8":
            mip_sizes.append(mip_width * mip_height * 4)
        else:
            mip_sizes.append(_mip_payload_size(mip_width, mip_height, block_bytes))
    if pixel_layout == "BGRA8":
        if flags & DDSD_PITCH == 0 or linear_size not in (0, width * 4):
            raise DdsError("Uncompressed BGRA row pitch does not match its width.")
    elif flags & DDSD_LINEARSIZE and linear_size != mip_sizes[0]:
        raise DdsError("DDS top-level linear size does not match the compressed dimensions.")
    expected_file_size = DDS_HEADER_BYTES + sum(mip_sizes)
    if file_size != expected_file_size:
        raise DdsError(
            f"DDS payload length mismatch: expected {expected_file_size} bytes, found {file_size}."
        )
    if len(data) < min(file_size, DDS_HEADER_BYTES + mip_sizes[0]):
        raise DdsError("Provided DDS bytes do not include the complete top-level mip.")
    return DdsHeader(
        width=width,
        height=height,
        mip_count=mip_count,
        fourcc=fourcc_bytes.decode("ascii", errors="replace").rstrip("\0"),
        flags=flags,
        caps=caps,
        payload_offset=DDS_HEADER_BYTES,
        mip_sizes=tuple(mip_sizes),
        pixel_layout=pixel_layout,
        red_mask=red_mask,
        green_mask=green_mask,
        blue_mask=blue_mask,
        alpha_mask=alpha_mask,
    )


def _color_565(value: int) -> Tuple[int, int, int]:
    red = (value >> 11) & 0x1F
    green = (value >> 5) & 0x3F
    blue = value & 0x1F
    return (
        (red << 3) | (red >> 2),
        (green << 2) | (green >> 4),
        (blue << 3) | (blue >> 2),
    )


def _bc1_colors(block: bytes, *, force_four_colors: bool = False):
    color0, color1, selectors = struct.unpack("<HHI", block)
    c0 = _color_565(color0)
    c1 = _color_565(color1)
    palette = [c0 + (255,), c1 + (255,)]
    if color0 > color1 or force_four_colors:
        palette.append(tuple((2 * a + b) // 3 for a, b in zip(c0, c1)) + (255,))
        palette.append(tuple((a + 2 * b) // 3 for a, b in zip(c0, c1)) + (255,))
    else:
        palette.append(tuple((a + b) // 2 for a, b in zip(c0, c1)) + (255,))
        palette.append((0, 0, 0, 0))
    return palette, selectors


def _bc3_alpha(block: bytes):
    alpha0 = block[0]
    alpha1 = block[1]
    bits = int.from_bytes(block[2:8], "little")
    if alpha0 > alpha1:
        palette = [alpha0, alpha1]
        palette.extend(((7 - index) * alpha0 + index * alpha1) // 7 for index in range(1, 7))
    else:
        palette = [alpha0, alpha1]
        palette.extend(((5 - index) * alpha0 + index * alpha1) // 5 for index in range(1, 5))
        palette.extend((0, 255))
    return palette, bits


def decode_mip_rgba(data: bytes, header: DdsHeader = None, level: int = 0):
    """Decode one BC1/BC3 mip into an RGBA Pillow image."""

    try:
        from PIL import Image
    except ImportError as error:  # pragma: no cover - environment guard
        raise RuntimeError("Pillow is required to decode DDS pixels.") from error

    if header is None:
        header = parse_dds_header(data)
    if level < 0 or level >= header.mip_count:
        raise DdsError("Requested DDS mip level is out of range.")
    if len(data) != DDS_HEADER_BYTES + sum(header.mip_sizes):
        raise DdsError("DDS bytes changed after header validation.")

    offset = DDS_HEADER_BYTES + sum(header.mip_sizes[:level])
    width, height = _mip_dimensions(header.width, header.height, level)
    if header.pixel_layout == "BGRA8":
        width_bytes = width * 4
        start = offset
        raw = data[start:start + width_bytes * height]
        if len(raw) != width_bytes * height:
            raise DdsError("Uncompressed BGRA pixels are truncated.")
        rgba = bytearray(len(raw))
        for index in range(0, len(raw), 4):
            blue, green, red, alpha = raw[index:index + 4]
            rgba[index:index + 4] = bytes((red, green, blue, alpha))
        return Image.frombytes("RGBA", (width, height), bytes(rgba))

    block_bytes = 8 if header.pixel_layout == "BC1" else 16
    blocks_x = max(1, (width + 3) // 4)
    blocks_y = max(1, (height + 3) // 4)
    pixels = bytearray(width * height * 4)
    for block_y in range(blocks_y):
        for block_x in range(blocks_x):
            block = data[offset:offset + block_bytes]
            if len(block) != block_bytes:
                raise DdsError("Compressed block is truncated.")
            offset += block_bytes
            if header.pixel_layout == "BC1":
                palette, color_bits = _bc1_colors(block)
                alpha_palette = None
                alpha_bits = 0
            else:
                alpha_palette, alpha_bits = _bc3_alpha(block[:8])
                palette, color_bits = _bc1_colors(block[8:16], force_four_colors=True)
            for local_y in range(4):
                pixel_y = block_y * 4 + local_y
                if pixel_y >= height:
                    continue
                for local_x in range(4):
                    pixel_x = block_x * 4 + local_x
                    if pixel_x >= width:
                        continue
                    selector_index = local_y * 4 + local_x
                    color_index = (color_bits >> (2 * selector_index)) & 0x3
                    rgba = list(palette[color_index])
                    if alpha_palette is not None:
                        alpha_index = (alpha_bits >> (3 * selector_index)) & 0x7
                        rgba[3] = alpha_palette[alpha_index]
                    pixel_offset = (pixel_y * width + pixel_x) * 4
                    pixels[pixel_offset:pixel_offset + 4] = bytes(rgba)
    if offset != DDS_HEADER_BYTES + sum(header.mip_sizes[:level + 1]):
        raise DdsError("Compressed mip decoder did not consume the declared block payload.")
    return Image.frombytes("RGBA", (width, height), bytes(pixels))
