"""Build labeled review sheets from the native-size scripted GUI reference PNGs."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
THUMB_SIZE = (520, 560)
PADDING = 16
LABEL_HEIGHT = 48


def font():
    for candidate in ("C:/Windows/Fonts/segoeui.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(candidate, 16)
        except OSError:
            continue
    return ImageFont.load_default()


def references(folder: Path) -> list[Path]:
    return sorted(
        path
        for path in folder.glob("*.png")
        if path.name != "contact_sheet.png" and not path.name.endswith("_full.png")
    )


def make_sheet(images: list[Path], destination: Path, columns: int) -> None:
    cell_width = THUMB_SIZE[0] + 2 * PADDING
    cell_height = THUMB_SIZE[1] + LABEL_HEIGHT + 2 * PADDING
    rows = (len(images) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), "#17202b")
    draw = ImageDraw.Draw(sheet)
    label_font = font()
    for index, source in enumerate(images):
        with Image.open(source) as original:
            native_size = original.size
            preview = ImageOps.contain(original.convert("RGBA"), THUMB_SIZE)
        column, row = index % columns, index // columns
        x = column * cell_width + PADDING
        y = row * cell_height + PADDING
        draw.rectangle(
            (x - 1, y - 1, x + THUMB_SIZE[0] + 1, y + THUMB_SIZE[1] + 1),
            outline="#56677a",
        )
        sheet.paste(preview, (x + (THUMB_SIZE[0] - preview.width) // 2, y), preview)
        draw.text(
            (x, y + THUMB_SIZE[1] + 8),
            f"{source.name}  {native_size[0]}×{native_size[1]}",
            font=label_font,
            fill="#f0f2f5",
        )
    sheet.save(destination, format="PNG", optimize=True)


def main() -> None:
    all_references: list[Path] = []
    for folder in sorted(path for path in ROOT.rglob("*") if path.is_dir()):
        if "source_full" in folder.parts:
            continue
        images = references(folder)
        if not images:
            continue
        make_sheet(images, folder / "contact_sheet.png", min(2, len(images)))
        all_references.extend(images)
    if all_references:
        make_sheet(all_references, ROOT / "contact_sheet.png", 3)


if __name__ == "__main__":
    main()
