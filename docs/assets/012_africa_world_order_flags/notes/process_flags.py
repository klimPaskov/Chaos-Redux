from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_png"
PROCESSED = ROOT / "processed_png"
MOD_ROOT = Path(__file__).resolve().parents[4]
TARGETS = {
    "normal": (82, 52),
    "medium": (41, 26),
    "small": (10, 7),
}

for source_path in sorted(SOURCE.glob("*.png")):
    with Image.open(source_path) as source:
        image = source.convert("RGBA")
        target_ratio = 82 / 52
        source_ratio = image.width / image.height
        if abs(source_ratio - target_ratio) > 0.25:
            raise ValueError(f"{source_path.name}: source ratio too far from HOI4 flag ratio, got {image.size}")
        if source_ratio < target_ratio:
            crop_height = round(image.width / target_ratio)
            top = (image.height - crop_height) // 2
            image = image.crop((0, top, image.width, top + crop_height))
        elif source_ratio > target_ratio:
            crop_width = round(image.height * target_ratio)
            left = (image.width - crop_width) // 2
            image = image.crop((left, 0, left + crop_width, image.height))
        for ladder, size in TARGETS.items():
            rendered = image.resize(size, Image.Resampling.LANCZOS)
            png_path = PROCESSED / f"{source_path.stem}_{ladder}.png"
            rendered.save(png_path, format="PNG", optimize=False)
            if ladder == "normal":
                target = MOD_ROOT / "gfx" / "flags" / f"{source_path.stem}.tga"
            else:
                target = MOD_ROOT / "gfx" / "flags" / ladder / f"{source_path.stem}.tga"
            target.parent.mkdir(parents=True, exist_ok=True)
            rendered.save(target, format="TGA", compression="raw")

# Review sheet: source master beside all three runtime ladders.
entries = sorted(SOURCE.glob("*.png"))
row_height = 190
sheet = Image.new("RGB", (1320, row_height * len(entries)), "#22252a")
draw = ImageDraw.Draw(sheet)
font = ImageFont.load_default()
for index, source_path in enumerate(entries):
    y = index * row_height
    with Image.open(source_path) as source:
        source_preview = source.convert("RGB")
        source_preview.thumbnail((260, 170), Image.Resampling.LANCZOS)
    draw.text((8, y + 12), source_path.stem, fill="#f3ead6", font=font)
    sheet.paste(source_preview, (210, y + 8))
    for column, (ladder, size) in enumerate(TARGETS.items()):
        png_path = PROCESSED / f"{source_path.stem}_{ladder}.png"
        with Image.open(png_path) as rendered:
            preview = rendered.convert("RGB").resize((240, 152), Image.Resampling.NEAREST)
        draw.text((540 + column * 250, y + 5), ladder, fill="#f3ead6", font=font)
        sheet.paste(preview, (500 + column * 250, y + 25))
    # Labels are kept in a sidecar text manifest; the pixel sheet remains clean artwork.
sheet.save(ROOT / "contact_sheets" / "flag_ladders.png", format="PNG", optimize=False)
