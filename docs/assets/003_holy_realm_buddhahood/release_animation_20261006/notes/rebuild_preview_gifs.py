"""Rebuild review GIFs from processed PNG frames at an exact 2-second cadence."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

import process_mandala_atlases as processor


BASE = Path(__file__).resolve().parents[1]
STATES = list(processor.ATLAS_BY_STATE)


def main() -> None:
    panel = Image.open(processor.PANEL_PATH).convert("RGB")
    previews = BASE / "previews"
    durations = processor.FRAME_DURATIONS_MS
    assert len(durations) == processor.FRAME_COUNT and sum(durations) == 2000
    for state in STATES:
        frame_dir = BASE / "processed_frames" / state
        frames = [Image.open(frame_dir / f"holy_realm_mandala_{state}_{i:03d}.png").convert("RGBA") for i in range(processor.FRAME_COUNT)]
        native = [processor.over_color(frame, processor.PANEL_RGB) for frame in frames]
        native_path = previews / f"holy_realm_mandala_{state}_preview_native.gif"
        native[0].save(native_path, save_all=True, append_images=native[1:], duration=durations, loop=0, disposal=2, optimize=False)
        consumer = [processor.make_panel_frame(panel, frame) for frame in frames]
        consumer_path = previews / f"holy_realm_mandala_{state}_preview_218_panel.gif"
        consumer[0].save(consumer_path, save_all=True, append_images=consumer[1:], duration=durations, loop=0, disposal=2, optimize=False)
        print(state, "frames=16", "durations_ms=120/130 alternating", "total_ms=2000")
    meta_path = BASE / "notes" / "frame_metadata.json"
    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    metadata["gif_preview_frame_durations_ms"] = durations
    metadata["gif_preview_total_ms"] = sum(durations)
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
