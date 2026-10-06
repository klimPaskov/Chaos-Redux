"""Split generated Mandala animation atlases and perform mechanical QA previews.

The source atlas cells supply every motion pose. This script only crops, pads,
applies the verified edge-removal fallback, resizes, sheets, previews, and records
metadata; it does not synthesize motion or redraw any cell.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from rembg import new_session, remove


BASE = Path(__file__).resolve().parents[1]
REPO = Path.cwd()
FRAME_SIZE = 420
CELL_SIZE = 314
FRAME_COUNT = 16
FPS = 8
FRAME_DURATIONS_MS = [120, 130] * 8
PANEL_RGB = (23, 32, 42)
LIGHT_RGB = (220, 220, 220)
PANEL_PATH = REPO / "docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/gui_render_before_refuge_19360101_cropped.png"
PANEL_ICON_RECT = (126, 12, 343, 229)
ATLAS_BY_STATE = {
    "dormant": "source_atlases/dormant_atlas_v3_edge_repair.png",
    "teaching": "source_atlases/teaching_atlas_v2_framing_edge_repair.png",
    "meditation": "source_atlases/meditation_atlas_v2_framing_edge_repair.png",
    "awakened": "source_atlases/awakened_atlas_v2_framing_edge_repair.png",
    "wrathful": "source_atlases/wrathful_atlas_v2_framing_edge_repair.png",
    "final_silence": "source_atlases/final_silence_atlas_v2_framing_edge_repair.png",
    "empty": "source_atlases/empty_atlas_v2_framing_edge_repair.png",
}
MODEL_PATH = Path.home() / ".u2net" / "isnet-general-use.onnx"
MODEL_SHA256 = "60920E99C45464F2BA57BEE2AD08C919A52BBF852739E96947FBB4358C0D964A"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def cell_bounds(image: Image.Image, index: int) -> tuple[int, int, int, int]:
    row, col = divmod(index, 4)
    x0 = round(col * image.width / 4)
    x1 = round((col + 1) * image.width / 4)
    y0 = round(row * image.height / 4)
    y1 = round((row + 1) * image.height / 4)
    return x0, y0, x1, y1


def pad_cell(cell: Image.Image) -> tuple[Image.Image, tuple[int, int]]:
    canvas = Image.new("RGBA", (CELL_SIZE, CELL_SIZE), (0, 0, 0, 0))
    offset = ((CELL_SIZE - cell.width) // 2, (CELL_SIZE - cell.height) // 2)
    canvas.alpha_composite(cell.convert("RGBA"), offset)
    return canvas, offset


def alpha_stats(image: Image.Image) -> dict:
    alpha = np.asarray(image.getchannel("A"))
    return {
        "extrema": list(image.getchannel("A").getextrema()),
        "transparent_pixels": int(np.count_nonzero(alpha == 0)),
        "opaque_pixels": int(np.count_nonzero(alpha == 255)),
        "alpha_bbox": list(image.getchannel("A").getbbox() or (0, 0, 0, 0)),
        "corner_alpha": [
            int(alpha[0, 0]),
            int(alpha[0, -1]),
            int(alpha[-1, 0]),
            int(alpha[-1, -1]),
        ],
    }


def over_color(image: Image.Image, color: tuple[int, int, int]) -> Image.Image:
    background = Image.new("RGBA", image.size, (*color, 255))
    background.alpha_composite(image.convert("RGBA"))
    return background.convert("RGB")


def contact_sheet(frames: list[Image.Image], cell_size: int, color: tuple[int, int, int]) -> Image.Image:
    sheet = Image.new("RGB", (cell_size * 4, cell_size * 4), color)
    for index, frame in enumerate(frames):
        preview = frame.convert("RGBA").resize((cell_size, cell_size), Image.Resampling.LANCZOS)
        sheet.paste(over_color(preview, color), ((index % 4) * cell_size, (index // 4) * cell_size))
    return sheet


def make_panel_frame(panel: Image.Image, frame: Image.Image) -> Image.Image:
    result = panel.copy().convert("RGB")
    draw = ImageDraw.Draw(result)
    draw.rectangle(PANEL_ICON_RECT, fill=PANEL_RGB)
    overlay = frame.convert("RGBA").resize((218, 218), Image.Resampling.LANCZOS)
    rgba = result.convert("RGBA")
    rgba.alpha_composite(overlay, (126, 12))
    return rgba.convert("RGB")


def save_contact(frames: list[Image.Image], state: str) -> dict:
    contacts = BASE / "contact_sheets"
    contacts.mkdir(parents=True, exist_ok=True)
    native = contact_sheet(frames, FRAME_SIZE, PANEL_RGB)
    native_path = contacts / f"holy_realm_mandala_{state}_contact_native.png"
    native.save(native_path)
    upscale = contact_sheet(frames, FRAME_SIZE * 4, PANEL_RGB)
    upscale_path = contacts / f"holy_realm_mandala_{state}_contact_4x.png"
    upscale.save(upscale_path)
    consumer_dark = contact_sheet(frames, 218, PANEL_RGB)
    consumer_dark_path = contacts / f"holy_realm_mandala_{state}_contact_218_dark.png"
    consumer_dark.save(consumer_dark_path)
    consumer_light = contact_sheet(frames, 218, LIGHT_RGB)
    consumer_light_path = contacts / f"holy_realm_mandala_{state}_contact_218_light_gray.png"
    consumer_light.save(consumer_light_path)
    return {
        "native": str(native_path.relative_to(BASE)),
        "4x": str(upscale_path.relative_to(BASE)),
        "consumer_218_dark": str(consumer_dark_path.relative_to(BASE)),
        "consumer_218_light_gray": str(consumer_light_path.relative_to(BASE)),
    }


def main() -> None:
    assert MODEL_PATH.is_file(), f"Missing verified local rembg model: {MODEL_PATH}"
    assert sha256(MODEL_PATH).upper() == MODEL_SHA256, "Unexpected local rembg model hash"
    panel = Image.open(PANEL_PATH).convert("RGB")
    assert panel.size == (471, 484), f"Unexpected production crop size: {panel.size}"
    session = new_session("isnet-general-use")
    metadata = {
        "consumer": "holy_realm_mandala_core",
        "target_frame_size": [FRAME_SIZE, FRAME_SIZE],
        "frame_count": FRAME_COUNT,
        "fps": FPS,
        "loop_seconds": 2,
        "gif_preview_frame_durations_ms": FRAME_DURATIONS_MS,
        "gif_preview_total_ms": sum(FRAME_DURATIONS_MS),
        "looping": True,
        "frame_order": "left-to-right, top-to-bottom in source atlas; left-to-right in final sheet",
        "anchor": {"name": "center", "processed_pixel": [210, 210]},
        "alignment": "fractional 4x4 cell crops are padded to 314x314 at the cell center, then uniformly resized to 420x420; no art translation, rotation, warp, or scale animation is added",
        "edge_cleanup_fallback": {
            "tool": "rembg",
            "version": "2.0.61",
            "model": "isnet-general-use",
            "model_path": str(MODEL_PATH),
            "model_sha256": MODEL_SHA256,
            "alpha_matting": False,
            "post_process_mask": False,
            "reason": "Native ImageGen alpha contained colored fringe/stray pixels; targeted ImageGen alpha-edge edits were attempted first and did not remove all observed spill.",
        },
        "gui_dark_reference": {
            "path": str(PANEL_PATH.relative_to(REPO)),
            "size": list(panel.size),
            "sampled_background_rgb": list(PANEL_RGB),
            "sampled_background_hex": "#17202A",
            "icon_rect": list(PANEL_ICON_RECT),
            "ui_scale": 1.0,
        },
        "states": {},
    }
    for state, relative_atlas in ATLAS_BY_STATE.items():
        atlas_path = BASE / relative_atlas
        atlas = Image.open(atlas_path).convert("RGBA")
        assert atlas.size == (1254, 1254), f"Unexpected source atlas dimensions for {state}: {atlas.size}"
        source_dir = BASE / "source_frames" / state
        processed_dir = BASE / "processed_frames" / state
        source_dir.mkdir(parents=True, exist_ok=True)
        processed_dir.mkdir(parents=True, exist_ok=True)
        processed_frames = []
        frame_rows = []
        for index in range(FRAME_COUNT):
            bounds = cell_bounds(atlas, index)
            raw = atlas.crop(bounds).convert("RGBA")
            source_path = source_dir / f"holy_realm_mandala_{state}_{index:03d}_source.png"
            raw.save(source_path)
            padded, pad_offset = pad_cell(raw)
            cleaned = remove(padded, session=session, alpha_matting=False, post_process_mask=False)
            if not isinstance(cleaned, Image.Image):
                cleaned = Image.open(cleaned)
            cleaned = cleaned.convert("RGBA")
            processed = cleaned.resize((FRAME_SIZE, FRAME_SIZE), Image.Resampling.LANCZOS)
            processed_path = processed_dir / f"holy_realm_mandala_{state}_{index:03d}.png"
            processed.save(processed_path)
            assert processed.size == (FRAME_SIZE, FRAME_SIZE)
            assert processed.getchannel("A").getpixel((0, 0)) == 0
            assert processed.getchannel("A").getpixel((FRAME_SIZE - 1, 0)) == 0
            assert processed.getchannel("A").getpixel((0, FRAME_SIZE - 1)) == 0
            assert processed.getchannel("A").getpixel((FRAME_SIZE - 1, FRAME_SIZE - 1)) == 0
            processed_frames.append(processed)
            frame_rows.append({
                "index": index,
                "source": str(source_path.relative_to(BASE)),
                "source_sha256": sha256(source_path),
                "source_dimensions": list(raw.size),
                "source_crop_xyxy": list(bounds),
                "source_pad_offset": list(pad_offset),
                "processed": str(processed_path.relative_to(BASE)),
                "processed_sha256": sha256(processed_path),
                "processed_dimensions": list(processed.size),
                "alpha": alpha_stats(processed),
            })
        assert len({sha256(processed_dir / f"holy_realm_mandala_{state}_{i:03d}.png") for i in range(FRAME_COUNT)}) == FRAME_COUNT, f"Duplicate processed poses in {state}"
        static_path = BASE / "static_fallbacks" / f"holy_realm_mandala_{state}.png"
        static_path.parent.mkdir(parents=True, exist_ok=True)
        processed_frames[0].save(static_path)
        sheet = Image.new("RGBA", (FRAME_SIZE * FRAME_COUNT, FRAME_SIZE), (0, 0, 0, 0))
        for index, frame in enumerate(processed_frames):
            sheet.alpha_composite(frame, (index * FRAME_SIZE, 0))
        sheet_path = BASE / "sheets" / f"holy_realm_mandala_{state}_sheet.png"
        sheet_path.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(sheet_path)
        assert sheet.size == (6720, 420)
        preview_dir = BASE / "previews"
        preview_dir.mkdir(parents=True, exist_ok=True)
        native_preview_frames = [over_color(frame, PANEL_RGB) for frame in processed_frames]
        native_gif = preview_dir / f"holy_realm_mandala_{state}_preview_native.gif"
        native_preview_frames[0].save(native_gif, save_all=True, append_images=native_preview_frames[1:], duration=FRAME_DURATIONS_MS, loop=0, disposal=2, optimize=False)
        consumer_frames = [make_panel_frame(panel, frame) for frame in processed_frames]
        consumer_gif = preview_dir / f"holy_realm_mandala_{state}_preview_218_panel.gif"
        consumer_frames[0].save(consumer_gif, save_all=True, append_images=consumer_frames[1:], duration=FRAME_DURATIONS_MS, loop=0, disposal=2, optimize=False)
        loop_diff = ImageChops.difference(processed_frames[15], processed_frames[0]).convert("RGB")
        state_contacts = save_contact(processed_frames, state)
        metadata["states"][state] = {
            "source_atlas": str(atlas_path.relative_to(BASE)),
            "source_atlas_sha256": sha256(atlas_path),
            "static_fallback_png": str(static_path.relative_to(BASE)),
            "static_fallback_sha256": sha256(static_path),
            "sheet_png": str(sheet_path.relative_to(BASE)),
            "sheet_sha256": sha256(sheet_path),
            "sheet_dimensions": list(sheet.size),
            "preview_native_gif": str(native_gif.relative_to(BASE)),
            "preview_consumer_218_panel_gif": str(consumer_gif.relative_to(BASE)),
            "contact_sheets": state_contacts,
            "frame_pixels_distinct": len(set(sha256(processed_dir / f"holy_realm_mandala_{state}_{i:03d}.png") for i in range(FRAME_COUNT))) == FRAME_COUNT,
            "loop_last_first_difference_bbox": list(loop_diff.getbbox() or (0, 0, 0, 0)),
            "loop_last_first_mean_abs_rgb_difference": float(np.asarray(loop_diff).mean()),
            "frames": frame_rows,
        }
        print(state, "frames=16", "sheet=6720x420", "unique=16", "loop_mae=", round(metadata["states"][state]["loop_last_first_mean_abs_rgb_difference"], 3))
    out = BASE / "notes" / "frame_metadata.json"
    out.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    print("metadata", out.relative_to(BASE))


if __name__ == "__main__":
    main()
