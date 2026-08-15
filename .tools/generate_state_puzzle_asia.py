from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
GAME = Path(r"C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
PROVINCE_BMP = GAME / "map/provinces.bmp"
DEFINITION = GAME / "map/definition.csv"
STATE_DIR = GAME / "history/states"
MAP_REVISION = "b69b583264f11454ac4a5975145ec632c881dea0d0e078be523facd0c2854333"
MCP_STATE_ARTIFACT = "hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf95f9371f8cf9fe330ba8b43bfafb25db079a8557dce8ae1b36539d59738606/9ba7665e947625b9a48a398e577ebc3e9209af24eaab444349bb0f4846a85564/map-inspect.b69b583264f11454.json"
MCP_GEOMETRY_ARTIFACT = "hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b79686608d14e7abee87c1827dbbf9e7fe8f16964c83a3da7cc013a820a5cab/39ba544299e1c84a33924de175066dfc31d05ab9c9c51f6784894d100cb846db/map-province-geometry.b69b583264f11454.726d6d54a44766de.json"

OUT_GFX = ROOT / "gfx/interface/formables/state_puzzles"
OUT_DOCS = ROOT / "docs/formables/state_puzzles"
CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"


CATEGORIES: dict[str, dict] = {
    "form_rattanakosin_kingdom": {
        "decision_category": "form_rattanakosin_kingdom_category",
        "required": [289, 868, 869, 724, 741, 1067, 670, 1068, 1069],
        "groups": {
            "siam": [289, 868, 869, 724],
            "cambodia": [741, 1067],
            "laos": [670, 1068, 1069],
        },
    },
    "form_turkestan": {
        "decision_category": "form_turkestan_category",
        "required": [402, 404, 406, 407, 583, 586, 587, 588, 589, 590, 881, 882, 405, 585, 831, 823, 830, 732, 742, 584, 832],
        "groups": {
            "kazakhstan": [402, 404, 406, 407, 583, 586, 587, 588, 589, 590, 881, 882],
            "uzbekistan": [405, 585, 831],
            "karakalpakstan": [823],
            "bukhara": [830],
            "kyrgyzstan": [732],
            "tajikistan": [742],
            "turkmenistan": [584],
            "tashauz": [832],
        },
        "notes": "Decision source repeats 881 and 882; manifest de-duplicates them once in the Kazakhstan group.",
    },
    "form_mountainous_republic": {
        "decision_category": "form_mountainous_republic_category",
        "required": [232, 821, 828, 827, 826],
        "groups": {"core_territory": [232, 821, 828, 827, 826]},
    },
    "form_idel_uralic_republic": {
        "decision_category": "form_idel_ural_category",
        "required": [833, 256, 249, 399, 651],
        "groups": {"core_territory": [833, 256, 249, 399, 651]},
    },
    "unite_greater_mongolia": {
        "decision_category": "greater_mongolia_category",
        "required": [818, 817, 330, 820, 819, 564, 329, 654, 760, 756, 621, 746, 612, 611, 761, 563, 566, 616, 1043, 1040, 1039],
        "groups": {"core_territory": [818, 817, 330, 820, 819, 564, 329, 654, 760, 756, 621, 746, 612, 611, 761, 563, 566, 616, 1043, 1040, 1039]},
    },
    "unite_hui_states": {
        "decision_category": "greater_hui_state_category",
        "required": [756, 616, 754, 755, 604, 759, 1042, 1040, 1044],
        "groups": {"core_territory": [756, 616, 754, 755, 604, 759, 1042, 1040, 1044]},
        "notes": "Commented highlight-only states 283, 753, 287, 619, and 1045 are excluded because they are not in available.",
    },
    "GOE_form_hindustan": {
        "decision_category": "GOE_form_hindustan_category",
        "required": [441, 787, 440, 442, 445, 444, 443, 439, 433, 428, 437, 438, 436, 429, 427, 425, 423, 424, 426, 435, 431, 432, 434, 430, 323, 324, 321, 320, 986, 989, 991, 984, 983, 982, 985, 990, 987, 988, 1012],
        "groups": {
            "india": [439, 433, 428, 437, 438, 436, 429, 427, 425, 423, 424, 426, 435, 431, 432, 434, 986, 989, 991, 984, 983, 982, 985, 990],
            "pakistan": [441, 787, 440, 442, 445, 444, 443, 987, 988, 1012],
            "bangladesh": [430],
            "nepal": [323],
            "bhutan": [324],
            "goa": [321],
            "french_india": [320],
        },
    },
    "neo_assyrian_empire_decision": {
        "decision_category": "neo_assyrian_empire_category",
        "required": [676, 291, 1010, 675, 1011, 656, 680, 554, 677, 799, 553, 344, 350, 454, 455, 453, 446, 907, 447, 348, 345],
        "groups": {"core_territory": [676, 291, 1010, 675, 1011, 656, 680, 554, 677, 799, 553, 344, 350, 454, 455, 453, 446, 907, 447, 348, 345]},
    },
    "neo_mesopotamia_decision": {
        "decision_category": "neo_mesopotamia_category",
        "required": [413, 421, 1001, 676, 291, 1011, 656, 675, 1010, 680, 677, 799, 350, 344, 554, 553, 454, 453, 446, 907, 447],
        "groups": {"core_territory": [413, 421, 1001, 676, 291, 1011, 656, 675, 1010, 680, 677, 799, 350, 344, 554, 553, 454, 453, 446, 907, 447]},
        "notes": "State 183 is commented out of available and excluded despite appearing in highlight/core code.",
    },
}


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_states() -> dict[int, dict]:
    out: dict[int, dict] = {}
    for path in STATE_DIR.glob("*.txt"):
        m = re.match(r"\s*(\d+)\s*(?:-|–)\s*(.+?)\.txt$", path.name)
        if not m:
            continue
        sid = int(m.group(1))
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        ids_match = re.search(r"provinces\s*=\s*\{([^}]*)\}", text, flags=re.S)
        if not ids_match:
            continue
        province_ids = [int(v) for v in re.findall(r"\d+", ids_match.group(1))]
        name = m.group(2).strip()
        name = re.sub(r"^\s*-\s*", "", name)
        out[sid] = {"name": name, "province_ids": province_ids, "path": str(path)}
    return out


def build_province_map() -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[int, int]]:
    defs: list[tuple[int, int]] = []
    with DEFINITION.open(encoding="utf-8", errors="replace") as f:
        for row in csv.reader(f, delimiter=";"):
            if not row or row[0] == "0":
                continue
            try:
                pid, r, g, b = map(int, row[:4])
            except ValueError:
                continue
            defs.append((r << 16 | g << 8 | b, pid))
    defs.sort()
    def_codes = np.array([x[0] for x in defs], dtype=np.uint32)
    def_ids = np.array([x[1] for x in defs], dtype=np.int32)
    rgb = np.asarray(Image.open(PROVINCE_BMP).convert("RGB"), dtype=np.uint8)
    codes = (rgb[..., 0].astype(np.uint32) << 16) | (rgb[..., 1].astype(np.uint32) << 8) | rgb[..., 2].astype(np.uint32)
    pos = np.searchsorted(def_codes, codes)
    pos = np.minimum(pos, len(def_codes) - 1)
    province_ids = def_ids[pos]
    if not np.all(def_codes[pos] == codes):
        raise RuntimeError("provinces.bmp contains colors absent from definition.csv")
    return province_ids, rgb, def_ids, rgb.shape[:2]


def alpha_mask_rgba(mask: np.ndarray, color: tuple[int, int, int], alpha: int = 255) -> Image.Image:
    a = (mask.astype(np.uint8) * alpha)
    rgba = np.empty((*mask.shape, 4), dtype=np.uint8)
    rgba[..., 0:3] = color
    rgba[..., 3] = a
    return Image.fromarray(rgba, "RGBA")


def variant_from_mask(mask: np.ndarray, qualifying: bool) -> Image.Image:
    base = Image.fromarray((mask.astype(np.uint8) * 255), "L")
    # Interior-only edge preserves exact neighbouring state seams when pieces are assembled.
    eroded = base.filter(ImageFilter.MinFilter(3))
    edge = np.clip(np.asarray(base, dtype=np.int16) - np.asarray(eroded, dtype=np.int16), 0, 255).astype(np.uint8)
    if qualifying:
        rgb = (70, 148, 103)
        border = (164, 223, 172)
        im = alpha_mask_rgba(mask, rgb)
        border_layer = alpha_mask_rgba(edge > 0, border, 230)
        im.alpha_composite(border_layer)
        # dark one-pixel perimeter remains as the non-colour silhouette cue.
        outer = base.filter(ImageFilter.MaxFilter(3))
        outer_edge = np.clip(np.asarray(outer, dtype=np.int16) - np.asarray(base, dtype=np.int16), 0, 255).astype(np.uint8)
        im.alpha_composite(alpha_mask_rgba(outer_edge > 0, (25, 56, 45), 180))
        return im
    im = alpha_mask_rgba(mask, (98, 101, 108))
    outer = base.filter(ImageFilter.MaxFilter(3))
    outer_edge = np.clip(np.asarray(outer, dtype=np.int16) - np.asarray(base, dtype=np.int16), 0, 255).astype(np.uint8)
    im.alpha_composite(alpha_mask_rgba(outer_edge > 0, (28, 31, 35), 220))
    hatch = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(hatch)
    spacing = 5
    for x in range(-im.height, im.width + im.height, spacing):
        draw.line((x, im.height, x + im.height, 0), fill=(35, 38, 43, 130), width=1)
    hatch.putalpha(Image.composite(hatch.getchannel("A"), Image.new("L", im.size, 0), base))
    im.alpha_composite(hatch)
    # Thin pale inner edge keeps the mask legible for colour-blind readers.
    im.alpha_composite(alpha_mask_rgba(edge > 0, (178, 181, 188), 170))
    return im


def convert_dds(png: Path, dds: Path) -> None:
    dds.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["python", "-B", str(CONVERTER), "--input", str(png), "--output", str(dds), "--width", str(Image.open(png).width), "--height", str(Image.open(png).height)], check=True, cwd=ROOT)


def main() -> None:
    states = parse_states()
    missing = sorted({sid for cfg in CATEGORIES.values() for sid in cfg["required"] if sid not in states})
    if missing:
        raise RuntimeError(f"Missing state history files: {missing}")
    province_ids_img, _, def_ids, (height, width) = build_province_map()
    max_pid = int(def_ids.max())
    # State labels are built once from the installed history province membership.
    state_lookup = np.zeros(max_pid + 1, dtype=np.int16)
    for sid, rec in states.items():
        for pid in rec["province_ids"]:
            if pid <= max_pid:
                state_lookup[pid] = sid
    state_img = state_lookup[province_ids_img]
    source_map_hash = sha256_path(PROVINCE_BMP)
    definition_hash = sha256_path(DEFINITION)
    font = None
    try:
        font = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        pass

    for category_id, cfg in CATEGORIES.items():
        required = list(dict.fromkeys(cfg["required"]))
        docs = OUT_DOCS / category_id
        gfx = OUT_GFX / category_id / "states"
        docs.mkdir(parents=True, exist_ok=True)
        gfx.mkdir(parents=True, exist_ok=True)

        needed_mask = np.isin(state_img, np.array(required, dtype=np.int16))
        ys, xs = np.where(needed_mask)
        if not len(xs):
            raise RuntimeError(f"No map pixels for {category_id}")
        x0, x1, y0, y1 = int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())
        src_w, src_h = x1 - x0 + 1, y1 - y0 + 1
        canvas_w, canvas_h = 440, 180
        pad = 6
        scale = min((canvas_w - 2 * pad) / src_w, (canvas_h - 2 * pad) / src_h)
        scaled_w, scaled_h = max(1, round(src_w * scale)), max(1, round(src_h * scale))
        origin_x = (canvas_w - scaled_w) // 2
        origin_y = (canvas_h - scaled_h) // 2
        crop = state_img[y0:y1 + 1, x0:x1 + 1]
        projection = {"source_bbox": [x0, y0, x1, y1], "source_size": [src_w, src_h], "canvas": [canvas_w, canvas_h], "scale": scale, "origin": [origin_x, origin_y], "scaled_size": [scaled_w, scaled_h], "padding": pad}
        entries = []
        composites = {False: Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0)), True: Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))}
        for sid in required:
            local_mask = (crop == sid).astype(np.uint8) * 255
            src_mask = Image.fromarray(local_mask, "L")
            projected = np.asarray(src_mask.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS), dtype=np.uint8) >= 30
            yy, xx = np.where(projected)
            if not len(xx):
                raise RuntimeError(f"State {sid} has no projected pixels in {category_id}")
            tx0, tx1, ty0, ty1 = int(xx.min()), int(xx.max()), int(yy.min()), int(yy.max())
            # A transparent 2 px guard is retained around the exact mask, while tight_bbox remains exact.
            guard = 2
            piece = projected[ty0:ty1 + 1, tx0:tx1 + 1]
            piece_unresolved = variant_from_mask(piece, False)
            piece_qualifying = variant_from_mask(piece, True)
            stem = f"state_{sid}"
            source_png = docs / f"{stem}_mask.png"
            source_img = alpha_mask_rgba(piece, (255, 255, 255))
            source_img.save(source_png)
            # Runtime pieces are tight-bbox static variants with the same projection origin stored in the manifest.
            for qualifying, label, image in ((False, "unresolved", piece_unresolved), (True, "qualifying", piece_qualifying)):
                processed = docs / f"{stem}_{label}.png"
                image.save(processed)
                dds = gfx / f"{stem}_{label}.dds"
                convert_dds(processed, dds)
                composites[qualifying].alpha_composite(image, (origin_x + tx0, origin_y + ty0))
            manifest_entry = {
                "state_id": sid,
                "state_name": states[sid]["name"],
                "province_ids": states[sid]["province_ids"],
                "history_file": states[sid]["path"],
                "group": next((name for name, ids in cfg.get("groups", {}).items() if sid in ids), "core_territory"),
                "alternate_group": None,
                "counting_rule": "is_controlled_by = ROOT" if category_id.startswith("neo_") else "controls_state = STATE_ID",
                "projection_position": [origin_x + tx0, origin_y + ty0],
                "projected_mask_size": [int(piece.shape[1]), int(piece.shape[0])],
                "tight_bbox": [tx0, ty0, tx1, ty1],
                "canvas_position": [origin_x + tx0, origin_y + ty0],
                "sprite_names": {"unresolved": f"formable_state_puzzle_{category_id}_{stem}_unresolved", "qualifying": f"formable_state_puzzle_{category_id}_{stem}_qualifying"},
                "runtime_dds": {"unresolved": f"gfx/interface/formables/state_puzzles/{category_id}/states/{stem}_unresolved.dds", "qualifying": f"gfx/interface/formables/state_puzzles/{category_id}/states/{stem}_qualifying.dds"},
                "source_mask_sha256": sha256_path(source_png),
                "dds_sha256": {"unresolved": sha256_path(gfx / f"{stem}_unresolved.dds"), "qualifying": sha256_path(gfx / f"{stem}_qualifying.dds")},
                "geometry": {"derivation": "installed map/provinces.bmp pixels selected by state history province membership", "mask_pixel_count": int(piece.sum()), "source_map_revision": MAP_REVISION},
            }
            entries.append(manifest_entry)

        for qualifying, label in ((False, "projection_unresolved"), (True, "projection_qualifying")):
            composites[qualifying].save(docs / f"{label}.png")
        # Native-size review contact sheet: projections plus every state in both states.
        thumb_w, thumb_h = 180, 120
        cols = 4
        rows = 1 + (len(entries) + cols - 1) // cols
        sheet = Image.new("RGBA", (cols * thumb_w, rows * (thumb_h + 20)), (26, 28, 31, 255))
        draw = ImageDraw.Draw(sheet)
        for i, (img, title) in enumerate(((composites[False], "projection unresolved"), (composites[True], "projection qualifying"))):
            x = i * thumb_w
            thumb = img.copy(); thumb.thumbnail((thumb_w - 8, thumb_h - 8))
            sheet.alpha_composite(thumb, (x + (thumb_w - thumb.width) // 2, 4))
            draw.text((x + 4, thumb_h + 2), title, fill=(230, 230, 230), font=font)
        for idx, e in enumerate(entries):
            row = 1 + idx // cols; col = idx % cols
            x, y = col * thumb_w, row * (thumb_h + 20)
            im = Image.open(docs / f"state_{e['state_id']}_qualifying.png").convert("RGBA")
            im.thumbnail((thumb_w - 8, thumb_h - 8))
            sheet.alpha_composite(im, (x + (thumb_w - im.width) // 2, y + 2))
            draw.text((x + 4, y + thumb_h + 2), f"{e['state_id']} {e['state_name'][:20]}", fill=(230, 230, 230), font=font)
        sheet.save(docs / "contact_sheet.png")

        manifest = {
            "schema": "chaos-redux-formable-state-puzzle/v1",
            "formable_id": category_id,
            "decision_category": cfg["decision_category"],
            "map_revision": MAP_REVISION,
            "map_dimensions": [width, height],
            "source_files": {"provinces_bmp": str(PROVINCE_BMP), "provinces_bmp_sha256": source_map_hash, "definition_csv": str(DEFINITION), "definition_csv_sha256": definition_hash},
            "mcp_evidence": {"state_membership_artifact": MCP_STATE_ARTIFACT, "province_geometry_artifact": MCP_GEOMETRY_ARTIFACT, "geometry_note": "MCP map inspection verifies installed state membership and canonical row-run geometry; local mask extraction is reproducible from the same map revision."},
            "state_policy": {"required_state_ids": required, "required_count": len(required), "groups": cfg.get("groups", {}), "alternate_groups": [], "alternate_policy": "none; every listed available state is required", "excluded_or_commented_states": cfg.get("notes", "")},
            "projection": projection,
            "states": entries,
            "status_variants": {"unresolved": "grey fill + diagonal hatch + interior outline", "qualifying": "green fill + solid pale inner keyline + dark silhouette outline", "animation": "none"},
        }
        (docs / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Generated {len(CATEGORIES)} state-puzzle packages")


if __name__ == "__main__":
    main()
