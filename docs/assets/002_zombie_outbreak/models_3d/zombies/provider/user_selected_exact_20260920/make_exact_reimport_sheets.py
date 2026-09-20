"""Assemble unchanged PDX reimport frames into visual QA contact sheets."""

from pathlib import Path
from PIL import Image


ROOT = Path(__file__).parent / "final_reimport_review"
for role in ("idle", "move", "attack", "defend", "support_attack", "retreat", "training", "death"):
    for pair in (("front", "left"), ("back", "three_quarter")):
        files = [ROOT / role / f"{phase:03d}_{view}.png" for view in pair for phase in (0, 25, 50, 75, 100)]
        if not all(path.is_file() for path in files):
            raise FileNotFoundError(f"Missing {role} {pair} review frames")
        with Image.open(files[0]) as first:
            width, height = first.size
        sheet = Image.new("RGB", (width * 5, height * 2), (55, 55, 55))
        for index, path in enumerate(files):
            with Image.open(path) as frame:
                sheet.paste(frame.convert("RGB"), ((index % 5) * width, (index // 5) * height))
        out = ROOT / f"{role}_{pair[0]}_{pair[1]}_sheet.jpg"
        sheet.save(out, quality=94)
        print(out)
