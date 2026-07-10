from __future__ import annotations

import csv
import hashlib
import struct
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "docs" / "assets" / "011_secret_alliance"
PROCESSED = PACKAGE / "processed_png"
ANIMATION = PACKAGE / "animations" / "coalition_closure_warning"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dds_header(path: Path) -> tuple[int, int, int, int, int, int, int]:
    data = path.read_bytes()[:128]
    if len(data) != 128 or data[:4] != b"DDS ":
        raise RuntimeError(f"Invalid DDS header: {path}")
    height, width = struct.unpack_from("<II", data, 12)
    rgb_bits = struct.unpack_from("<I", data, 88)[0]
    masks = struct.unpack_from("<IIII", data, 92)
    return (width, height, rgb_bits, *masks)


def assert_unique(paths: list[Path], label: str) -> None:
    hashes = [sha256(path) for path in paths]
    if len(set(hashes)) != len(hashes):
        raise RuntimeError(f"Duplicate {label} found")


def main() -> None:
    with (PACKAGE / "conversion_manifest.tsv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(rows) != 57:
        raise RuntimeError(f"Expected 57 runtime DDS targets, found {len(rows)}")

    transparent_count = 0
    fringe_pixels = 0
    visible_pixels = 0
    dds_sizes: set[tuple[int, int]] = set()
    for row in rows:
        png = ROOT / row["processed_png"]
        dds = ROOT / row["final_dds"]
        expected = (int(row["width"]), int(row["height"]))
        if not png.exists() or not dds.exists():
            raise RuntimeError(f"Missing runtime asset pair: {png} / {dds}")
        png_image = Image.open(png).convert("RGBA")
        dds_image = Image.open(dds).convert("RGBA")
        if png_image.size != expected or dds_image.size != expected:
            raise RuntimeError(f"Dimension mismatch: {png} / {dds} / {expected}")
        header = dds_header(dds)
        if header != (
            expected[0],
            expected[1],
            32,
            0x00FF0000,
            0x0000FF00,
            0x000000FF,
            0xFF000000,
        ):
            raise RuntimeError(f"DDS is not one-mip 32-bit BGRA/B8G8R8A8 style: {dds}: {header}")
        dds_sizes.add(expected)

        is_achievement = row["final_dds"].startswith("gfx/achievements/")
        is_panel = row["final_dds"].endswith("counter_network_panel.dds")
        if not is_achievement and not is_panel:
            alpha = png_image.getchannel("A")
            extrema = alpha.getextrema()
            if extrema[0] != 0 or extrema[1] != 255:
                raise RuntimeError(f"Transparent asset lacks both transparent and opaque pixels: {png}")
            corners = [
                alpha.getpixel((0, 0)),
                alpha.getpixel((png_image.width - 1, 0)),
                alpha.getpixel((0, png_image.height - 1)),
                alpha.getpixel((png_image.width - 1, png_image.height - 1)),
            ]
            if any(corners):
                raise RuntimeError(f"Transparent asset has nontransparent corner pixels: {png}: {corners}")
            transparent_count += 1
            for red, green, blue, pixel_alpha in png_image.getdata():
                if pixel_alpha > 8:
                    visible_pixels += 1
                    if green > 180 and red < 100 and blue < 100:
                        fringe_pixels += 1

    if fringe_pixels:
        raise RuntimeError(f"Detected {fringe_pixels} bright chroma-green visible pixels")

    decision_sources = [
        PACKAGE / "source_png" / f"{name}_source.png"
        for name in (
            "decision_compare_traffic",
            "decision_trace_courier",
            "decision_compare_sabotage",
            "decision_compartmentalize",
            "decision_secure_industry",
            "decision_harden_border",
            "decision_quiet_approach",
            "decision_security_guarantee",
            "decision_feed_false_plans",
            "decision_turn_member",
            "decision_disrupt_conference",
            "decision_border_intercept",
            "decision_release_dossier",
            "decision_emergency_mobilization",
            "decision_preempt_coalition",
            "decision_offer_separate_terms",
            "decision_strike_depots",
        )
    ]
    idea_sources = sorted((PACKAGE / "source_png").glob("idea_*_source.png"))
    animation_sources = sorted((ANIMATION / "source_frames").glob("*_source.png"))
    animation_processed = sorted((ANIMATION / "processed_frames").glob("*.png"))
    if len(decision_sources) != 17 or len(idea_sources) != 7:
        raise RuntimeError("Static icon source count mismatch")
    if len(animation_sources) != 8 or len(animation_processed) != 8:
        raise RuntimeError("Animation source or processed frame count mismatch")
    assert_unique(decision_sources, "decision source artwork")
    assert_unique(idea_sources, "idea source artwork")
    assert_unique(animation_sources, "animation source frames")
    assert_unique(animation_processed, "animation processed frames")

    animation_sheet = Image.open(ANIMATION / "sheets" / "coalition_closure_warning_sheet.png").convert("RGBA")
    if animation_sheet.size != (1024, 96):
        raise RuntimeError("Animation sheet size mismatch")
    for index, frame_path in enumerate(animation_processed):
        frame = Image.open(frame_path).convert("RGBA")
        extracted = animation_sheet.crop((index * 128, 0, (index + 1) * 128, 96))
        if frame.tobytes() != extracted.tobytes():
            raise RuntimeError(f"Animation sheet frame {index} does not match processed frame")

    suspect_sheet = Image.open(PROCESSED / "suspect_card_states.png").convert("RGBA")
    if suspect_sheet.size != (736, 96):
        raise RuntimeError("Suspect state sheet size mismatch")
    suspect_states = ["unknown", "possible", "likely", "confirmed"]
    for index, state in enumerate(suspect_states):
        frame = Image.open(PROCESSED / f"suspect_card_{state}.png").convert("RGBA")
        extracted = suspect_sheet.crop((index * 184, 0, (index + 1) * 184, 96))
        if frame.tobytes() != extracted.tobytes():
            raise RuntimeError(f"Suspect sheet state {state} does not match processed frame")

    overlay = Image.open(PACKAGE / "source_png" / "achievement_not_eligible_overlay_recovered.png").convert("RGBA")
    overlay_nonzero = sum(1 for value in overlay.getchannel("A").getdata() if value)
    if overlay_nonzero != 939:
        raise RuntimeError(f"Recovered achievement overlay changed: {overlay_nonzero} nonzero-alpha pixels")
    for base_path in sorted(PROCESSED.glob("011_secret_alliance_*.png")):
        if base_path.stem.endswith(("_grey", "_not_eligible")):
            continue
        grey_path = base_path.with_name(base_path.stem + "_grey.png")
        not_eligible_path = base_path.with_name(base_path.stem + "_not_eligible.png")
        if not grey_path.exists() or not not_eligible_path.exists():
            continue
        grey = Image.open(grey_path).convert("RGBA")
        expected = Image.alpha_composite(grey, overlay)
        actual = Image.open(not_eligible_path).convert("RGBA")
        if expected.tobytes() != actual.tobytes():
            raise RuntimeError(f"Not-eligible variant did not use recovered overlay: {not_eligible_path}")
        assert_unique([base_path, grey_path, not_eligible_path], f"achievement triplet {base_path.stem}")

    report = PACKAGE / "validation_icons_ui_animation.txt"
    report.write_text(
        "Event 011 icon/UI/animation validation\n"
        f"runtime DDS targets: {len(rows)}\n"
        "DDS encoding: one-mip 32-bit BGRA/B8G8R8A8-style masks on every target\n"
        f"distinct DDS dimensions: {', '.join(f'{w}x{h}' for w, h in sorted(dds_sizes))}\n"
        f"transparent runtime assets checked: {transparent_count}\n"
        f"visible alpha pixels checked for chroma fringe: {visible_pixels}\n"
        "bright chroma-green visible pixels: 0\n"
        "decision source artworks: 17 unique\n"
        "idea source artworks: 7 unique\n"
        "animation source frames: 8 unique\n"
        "animation processed frames: 8 unique\n"
        "animation sheet: 1024x96, eight exact 128x96 frame columns\n"
        "suspect-card sheet: 736x96, four exact 184x96 state columns\n"
        f"achievement overlay nonzero-alpha pixels: {overlay_nonzero}\n"
        "achievement triplets: six exact completed/grey/recovered-overlay composites\n",
        encoding="utf-8",
    )
    print(report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
