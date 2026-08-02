"""Process generated Chaos Warfare doctrine and large-counter icon masters.

The source and alpha-master files are generated-art evidence. This processor only
normalizes transparent bounds, creates the vanilla two-state large-counter strip,
and builds checkerboard review sheets; it does not generate new artwork.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DOCTRINE = ROOT / "doctrine_style_icons_64x64"
COUNTERS = ROOT / "division_counter_icons_152x42"


def checker(size, cell=12):

    image = Image.new("RGBA", size, (230, 230, 230, 255))
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if ((x // cell) + (y // cell)) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=(190, 190, 190, 255))
    return image


def crop_with_margin(image, margin_ratio=0.035):

    alpha = image.getchannel("A")
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("generated alpha master has no visible subject")
    left, top, right, bottom = bbox
    margin = max(2, int(max(right - left, bottom - top) * margin_ratio))
    left = max(0, left - margin)
    top = max(0, top - margin)
    right = min(image.width, right + margin)
    bottom = min(image.height, bottom + margin)
    return image.crop((left, top, right, bottom))


def contain(image, size):

    image = image.copy()
    image.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", size, (0, 0, 0, 0))
    canvas.alpha_composite(image, ((size[0] - image.width) // 2, (size[1] - image.height) // 2))
    return canvas


def neutral_counter(image):

    image = image.copy()
    pixels = []
    for red, green, blue, alpha in image.getdata():
        if alpha == 0:
            pixels.append((0, 0, 0, 0))
            continue
        luminance = (red * 30 + green * 59 + blue * 11) // 100
        if luminance >= 155:
            color = (238, 235, 218)
        elif luminance >= 72:
            color = (93, 93, 87)
        else:
            color = (14, 15, 16)
        pixels.append((*color, alpha))
    image.putdata(pixels)
    return image


def save_contact_sheet(images, path, title, cell_size, columns):

    label_height = 34
    rows = (len(images) + columns - 1) // columns
    sheet = checker((columns * cell_size[0], rows * (cell_size[1] + label_height)), 10)
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, (label, image) in enumerate(images):
        column = index % columns
        row = index // columns
        x = column * cell_size[0]
        y = row * (cell_size[1] + label_height)
        sheet.alpha_composite(image, (x + (cell_size[0] - image.width) // 2, y))
        draw.text((x + 5, y + cell_size[1] + 4), label, fill=(20, 20, 20, 255), font=font)
    sheet.save(path)


def process_doctrine():

    out = DOCTRINE / "processed_png"
    out.mkdir(parents=True, exist_ok=True)
    review = []
    for source in sorted((DOCTRINE / "alpha_master").glob("*_alpha.png")):
        name = source.name.removesuffix("_alpha.png")
        image = Image.open(source).convert("RGBA")
        image = contain(crop_with_margin(image), (58, 58))
        canvas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        canvas.alpha_composite(image, (3, 3))
        destination = out / f"{name}.png"
        canvas.save(destination)
        preview = checker((256, 256), 16)
        preview.alpha_composite(canvas.resize((256, 256), Image.Resampling.NEAREST))
        review.append((name, preview))
    save_contact_sheet(review, DOCTRINE / "contact_sheets/doctrine_style_contact_sheet_checker.png", "Doctrine style", (256, 256), 2)


def process_counters():

    active_dir = COUNTERS / "processed_png/active"
    neutral_dir = COUNTERS / "processed_png/neutral"
    strip_dir = COUNTERS / "processed_png/strips"
    for directory in (active_dir, neutral_dir, strip_dir):
        directory.mkdir(parents=True, exist_ok=True)
    review = []
    for source in sorted((COUNTERS / "alpha_master").glob("*_alpha.png")):
        name = source.name.removesuffix("_alpha.png")
        image = Image.open(source).convert("RGBA")
        image = contain(crop_with_margin(image), (68, 36))
        active = Image.new("RGBA", (76, 42), (0, 0, 0, 0))
        active.alpha_composite(image, (4, 3))
        neutral = neutral_counter(active)
        strip = Image.new("RGBA", (152, 42), (0, 0, 0, 0))
        strip.alpha_composite(active, (0, 0))
        strip.alpha_composite(neutral, (76, 0))
        active.save(active_dir / f"{name}_active.png")
        neutral.save(neutral_dir / f"{name}_neutral.png")
        strip.save(strip_dir / f"{name}.png")

        preview = checker((304, 84), 10)
        preview.alpha_composite(strip.resize((304, 84), Image.Resampling.NEAREST))
        review.append((name, preview))
    save_contact_sheet(review, COUNTERS / "contact_sheets/division_counter_contact_sheet_checker.png", "Large division counters: active | neutral", (304, 84), 2)


if __name__ == "__main__":

    process_doctrine()
    process_counters()
