"""Occupancy-mask-driven UV island dilation with source-pixel preservation."""

from __future__ import annotations

from array import array
from collections import deque
import hashlib
from typing import Dict, Iterable, Optional, Tuple

from PIL import Image


def load_occupancy_mask(path_or_image, size=None, *, allow_empty: bool = False) -> Image.Image:
    """Load an explicit grayscale occupancy mask; never infer it from artwork."""

    if isinstance(path_or_image, Image.Image):
        image = path_or_image.copy()
    else:
        with Image.open(path_or_image) as source:
            source.load()
            image = source.copy()
    if image.mode in {"1", "L", "I;16", "I"}:
        mask = image.convert("L")
    elif image.mode in {"RGB", "RGBA"}:
        channels = image.convert("RGB").split()
        if channels[0].tobytes() != channels[1].tobytes() or channels[0].tobytes() != channels[2].tobytes():
            raise ValueError("Occupancy mask must be grayscale; color-based occupancy inference is forbidden.")
        mask = channels[0].copy()
    else:
        raise ValueError(f"Unsupported occupancy-mask mode {image.mode!r}; use an 8-bit grayscale mask.")
    if size is not None and mask.size != tuple(size):
        mask = mask.resize(tuple(size), Image.Resampling.NEAREST)
    if not allow_empty and not any(mask.getdata()):
        raise ValueError("Occupancy mask contains no occupied texels.")
    return mask


def mask_stats(mask: Image.Image) -> Dict[str, float]:
    values = mask.convert("L").tobytes()
    occupied = sum(value > 0 for value in values)
    total = len(values)
    return {
        "width": mask.width,
        "height": mask.height,
        "occupied_pixels": occupied,
        "total_pixels": total,
        "coverage": round(occupied / total, 8),
        "pixel_bytes_sha256": hashlib.sha256(mask.convert("L").tobytes()).hexdigest(),
    }


def downsample_occupancy_mask(mask: Image.Image, size: Tuple[int, int]) -> Image.Image:
    """Downsample with coverage-preserving max semantics for mip QA/dilation."""

    source = mask.convert("L")
    if source.size == tuple(size):
        return source.copy()
    # BOX retains partial coverage, then any positive footprint remains occupied.
    resized = source.resize(tuple(size), Image.Resampling.BOX)
    return resized.point(lambda value: 255 if value > 0 else 0, mode="L")


def dilate_from_occupancy(
    image: Image.Image,
    occupancy_mask: Image.Image,
    radius: int = 12,
    *,
    channels: Iterable[int] = (0, 1, 2, 3),
    outside_fill: Optional[Tuple[int, int, int, int]] = None,
) -> Tuple[Image.Image, Dict[str, object]]:
    """Copy nearest occupied source texels into a bounded UV gutter.

    The 8-neighbour breadth-first pass never creates or blends source values.
    The mask is mandatory and all nonzero mask values are occupied. `outside_fill`
    is useful for packed normals, whose unused atlas pixels must be neutral.
    """

    if not 0 <= radius <= 16:
        raise ValueError("Dilation radius must be from 0 through 16 pixels.")
    rgba = image.convert("RGBA")
    mask = load_occupancy_mask(occupancy_mask, rgba.size)
    width, height = rgba.size
    count = width * height
    mask_bytes = mask.tobytes()
    source = rgba.tobytes()
    output = bytearray(source)
    channel_list = tuple(sorted(set(int(channel) for channel in channels)))
    if any(channel not in (0, 1, 2, 3) for channel in channel_list):
        raise ValueError("RGBA channel selection must use indices 0 through 3.")

    owners = array("i", [-1]) * count
    distances = bytearray([255]) * count
    frontier = deque()
    occupied_count = 0
    for index, value in enumerate(mask_bytes):
        if value > 0:
            owners[index] = index
            distances[index] = 0
            frontier.append(index)
            occupied_count += 1
        elif outside_fill is not None:
            start = index * 4
            output[start:start + 4] = bytes(outside_fill)

    if occupied_count == 0:
        raise ValueError("Occupancy mask contains no occupied texels.")
    if radius:
        while frontier:
            current = frontier.popleft()
            next_distance = distances[current] + 1
            if next_distance > radius:
                continue
            x = current % width
            y = current // width
            current_owner = owners[current]
            for dy in (-1, 0, 1):
                next_y = y + dy
                if next_y < 0 or next_y >= height:
                    continue
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    next_x = x + dx
                    if next_x < 0 or next_x >= width:
                        continue
                    neighbor = next_y * width + next_x
                    if owners[neighbor] != -1:
                        continue
                    owners[neighbor] = current_owner
                    distances[neighbor] = next_distance
                    frontier.append(neighbor)

    filled_count = 0
    max_used_distance = 0
    for index in range(count):
        if mask_bytes[index] > 0:
            continue
        owner = owners[index]
        if owner < 0:
            continue
        filled_count += 1
        max_used_distance = max(max_used_distance, distances[index])
        target_offset = index * 4
        source_offset = owner * 4
        for channel in channel_list:
            output[target_offset + channel] = source[source_offset + channel]

    result = Image.frombytes("RGBA", rgba.size, bytes(output))
    return result, {
        "dilation_radius_px": radius,
        "occupied_pixels": occupied_count,
        "coverage": round(occupied_count / count, 8),
        "filled_pixels": filled_count,
        "max_used_distance_px": max_used_distance,
        "channels_copied": ["RGBA"[channel] for channel in channel_list],
        "outside_fill": list(outside_fill) if outside_fill is not None else None,
        "source_pixel_values_only": True,
        "mask_sha256": hashlib.sha256(mask_bytes).hexdigest(),
    }
