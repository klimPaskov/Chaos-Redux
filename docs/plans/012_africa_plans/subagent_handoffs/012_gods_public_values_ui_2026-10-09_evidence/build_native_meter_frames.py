"""Compile static value states from the installed stock 181x16 subject rail.

These are data-selected frames, not an animation or replacement artwork.
Frame 1 is empty, frame 49 is 48%, and frame 101 is full.
160x14 stored frames keep the horizontal atlas below 16384 pixels.
The native icon scale restores 181x15.8375 display bounds.
"""
from pathlib import Path
from PIL import Image

GAME = Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
OUTPUT = Path(__file__).resolve().parent
fill = Image.open(GAME / "gfx/interface/autonomy/subject_progress_bar_long.dds").convert("RGBA")
rail = Image.open(GAME / "gfx/interface/autonomy/subject_progress_bar_long_bg.dds").convert("RGBA")
assert fill.size == rail.size == (181, 16)
fill = fill.resize((160, 14), Image.Resampling.LANCZOS)
rail = rail.resize((160, 14), Image.Resampling.LANCZOS)
width, height = fill.size
atlas = Image.new("RGBA", (width * 101, height))
samples = Image.new("RGBA", (width, height * 5))
for value in range(101):
	frame = rail.copy()
	filled_width = round(width * value / 100)
	if filled_width:
		frame.paste(fill.crop((0, 0, filled_width, height)), (0, 0))
	atlas.paste(frame, (width * value, 0))
	if value in (0, 38, 48, 85, 100):
		samples.paste(frame, (0, (0, 38, 48, 85, 100).index(value) * height))
atlas.save(OUTPUT / "gods_public_values_meter_101.dds")
samples.save(OUTPUT / "native_meter_frame_samples.png")
print("101 stock-derived static frames; 160x14 stored, 181x15.8375 displayed; empty/38/48/85/full samples")
