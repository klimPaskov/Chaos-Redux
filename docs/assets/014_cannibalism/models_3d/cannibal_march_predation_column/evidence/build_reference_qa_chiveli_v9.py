"""Build source/final comparison and alpha QA for the Chiveli recovery-v9 reference."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def sha256(path: Path) -> str:
	hasher = hashlib.sha256()
	with path.open("rb") as handle:
		for block in iter(lambda: handle.read(1024 * 1024), b""):
			hasher.update(block)
	return hasher.hexdigest().upper()


def contain(image: Image.Image, size: tuple[int, int], background: tuple[int, int, int, int]) -> Image.Image:
	copy = image.copy()
	copy.thumbnail(size, Image.Resampling.LANCZOS)
	canvas = Image.new("RGBA", size, background)
	canvas.alpha_composite(copy, ((size[0] - copy.width) // 2, (size[1] - copy.height) // 2))
	return canvas


def checker(size: tuple[int, int], cell: int = 32) -> Image.Image:
	y, x = np.indices((size[1], size[0]))
	pattern = ((x // cell + y // cell) % 2).astype(np.uint8)
	values = np.where(pattern[..., None] == 0, 72, 126).astype(np.uint8)
	rgb = np.repeat(values, 3, axis=2)
	return Image.fromarray(rgb, "RGB").convert("RGBA")


def labelled_panel(image: Image.Image, title: str, width: int, height: int) -> Image.Image:
	panel = Image.new("RGBA", (width, height + 40), (24, 24, 24, 255))
	panel.alpha_composite(contain(image, (width, height), (24, 24, 24, 255)), (0, 40))
	ImageDraw.Draw(panel).text((12, 12), title, fill=(240, 240, 240, 255), font=ImageFont.load_default())
	return panel


def main() -> int:
	if len(sys.argv) != 4:
		raise SystemExit("usage: build_reference_qa_chiveli_v9.py SOURCE FINAL OUTPUT_DIR")

	source_path = Path(sys.argv[1])
	final_path = Path(sys.argv[2])
	output_dir = Path(sys.argv[3])
	output_dir.mkdir(parents=True, exist_ok=True)
	source = Image.open(source_path).convert("RGBA")
	final = Image.open(final_path).convert("RGBA")

	comparison = Image.new("RGBA", (1800, 1040), (18, 18, 18, 255))
	comparison.alpha_composite(labelled_panel(source, "REFERENCE-ONLY SOURCE - ALEXANDER CHIVELI CANNIBAL", 900, 1000), (0, 0))
	comparison.alpha_composite(labelled_panel(final, "APPROVED MESHY INPUT - BOUNDED ARCHER EDIT", 900, 1000), (900, 0))
	comparison_path = output_dir / "chiveli_source_to_final_comparison_v9.png"
	comparison.convert("RGB").save(comparison_path)

	backgrounds = {
		"black": Image.new("RGBA", final.size, (0, 0, 0, 255)),
		"white": Image.new("RGBA", final.size, (255, 255, 255, 255)),
		"checker": checker(final.size),
	}
	qa_paths: dict[str, str] = {}
	for name, background in backgrounds.items():
		background.alpha_composite(final)
		path = output_dir / f"meshy_input_alpha_{name}_v9.png"
		background.convert("RGB").save(path)
		qa_paths[name] = path.as_posix()

	alpha = np.array(final.getchannel("A"))
	visible = alpha > 0
	y_coords, x_coords = np.where(visible)
	partial = (alpha > 0) & (alpha < 255)
	metrics = {
		"schema_version": "1.0.0",
		"source": {"path": source_path.as_posix(), "sha256": sha256(source_path)},
		"final": {
			"path": final_path.as_posix(),
			"sha256": sha256(final_path),
			"width": final.width,
			"height": final.height,
			"mode": final.mode,
			"alpha_min": int(alpha.min()),
			"alpha_max": int(alpha.max()),
			"transparent_pixels": int((alpha == 0).sum()),
			"opaque_pixels": int((alpha == 255).sum()),
			"partial_alpha_pixels": int(partial.sum()),
			"visible_bounds": [int(x_coords.min()), int(y_coords.min()), int(x_coords.max()), int(y_coords.max())],
		},
		"comparison": {"path": comparison_path.as_posix(), "sha256": sha256(comparison_path)},
		"alpha_qa": {name: {"path": path, "sha256": sha256(Path(path))} for name, path in qa_paths.items()},
	}
	metrics_path = output_dir / "chiveli_reference_qa_v9.json"
	metrics_path.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
