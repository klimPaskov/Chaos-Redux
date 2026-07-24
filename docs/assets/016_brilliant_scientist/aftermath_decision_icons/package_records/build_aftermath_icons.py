"""Build Event 016 qualifying-defeat aftermath decision/category icons."""
from __future__ import annotations
import csv, hashlib, json, re, struct, subprocess
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[5]
BASE = ROOT / "docs/assets/016_brilliant_scientist/aftermath_decision_icons"
SRC_D, SRC_C = BASE / "source_png/decisions", BASE / "source_png/categories"
ALPHA_D, ALPHA_C = BASE / "alpha_png/decisions", BASE / "alpha_png/categories"
PROC_D, PROC_C = BASE / "processed_png/decisions", BASE / "processed_png/categories"
DECODE_D, DECODE_C = BASE / "dds_decoded_png/decisions", BASE / "dds_decoded_png/categories"
RUNTIME_D = ROOT / "gfx/interface/decisions/016_brilliant_scientist/aftermath/decisions"
RUNTIME_C = ROOT / "gfx/interface/decisions/016_brilliant_scientist/aftermath/categories"
CONTACT, RECORDS, VALIDATION = BASE / "contact_sheets", BASE / "package_records", BASE / "validation"
REMOVE_KEY = Path(r"C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py")
CONVERTER = ROOT / ".agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py"

DECISIONS = [
    ("found_scientific_commission", "Treaty commission seal with microscope and papers"),
    ("exchange_countermeasures", "Countermeasure canisters exchanged across a shield"),
    ("codify_personhood_and_asylum", "Personhood charter and protective asylum arch"),
    ("ban_singularity_components", "Prohibited broken singularity reactor"),
    ("ratify_scientific_compact", "Scientific compact seal held by two hands"),
    ("register_recovered_facility", "Recovered laboratory facility registry tag"),
    ("inventory_project_templates", "Project blueprint inventory drawers"),
    ("secure_command_archives", "Locked command archive vault"),
    ("certify_global_dismantlement", "World ring with dismantled reactor pieces"),
    ("rebuild_laboratory_state", "Laboratory reconstruction with crane and masonry"),
    ("open_survivor_clinics", "Survivor clinic medical lamp and bandage"),
    ("build_memorial_archive", "Memorial stone with archive box"),
    ("close_reconstruction_board", "Reconstruction drafting board with closure seal"),
    ("hear_clone_communities", "Clone-community civic hearing"),
    ("audit_machine_nodes", "Robot node audit lens and console"),
    ("secure_paleogenetic_reserves", "Fossil tooth and amber egg reserve crate"),
    ("receive_xenobiological_handlers", "Handler with contained engineered organism"),
    ("map_portal_terminals", "Map with glowing portal terminal pins"),
    ("reconcile_temporal_records", "Split clock and temporal ledgers"),
    ("open_biological_archive", "Sealed biological archive with quarantine emblem"),
    ("catalogue_alien_cache", "Nonhuman artifact specimen case"),
    ("dispose_singularity_core", "Singularity core lowered into disposal crucible"),
]
CATEGORIES = [
    ("treaty", "Scientific treaty, protected exchange, personhood, and prohibition"),
    ("inspection", "Physical laboratory register, command archive, and dismantlement audit"),
    ("reconstruction", "Rail, factory, survivor clinic, memorial, and closure board"),
    ("remnants", "Evidence wreath of clone, machine, paleo, xeno, portal, temporal, biological, alien, and singularity remnants"),
]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()

def crop(source, out_dir, names, cols, bounds_x, bounds_y):
    im = Image.open(source).convert("RGB")
    for i, name in enumerate(names):
        row, col = divmod(i, cols)
        x0, x1 = bounds_x[col], bounds_x[col + 1]
        y0, y1 = bounds_y[row], bounds_y[row + 1]
        im.crop((x0 + 5, y0 + 5, x1 - 5, y1 - 5)).save(out_dir / f"{name}_source.png")

def key(source, out):
    subprocess.run(["python", str(REMOVE_KEY), "--input", str(source), "--out", str(out), "--auto-key", "border", "--soft-matte", "--transparent-threshold", "12", "--opaque-threshold", "220", "--edge-contract", "1", "--despill", "--force"], check=True)

def normalize(alpha, out, size):
    src = Image.open(alpha).convert("RGBA")
    if size[0] == size[1]:
        result = src.resize(size, Image.Resampling.LANCZOS)
    else:
        inner = src.resize((size[0] - 6, size[1] - 4), Image.Resampling.LANCZOS)
        result = Image.new("RGBA", size, (0, 0, 0, 0))
        result.alpha_composite(inner, ((size[0] - inner.width) // 2, (size[1] - inner.height) // 2))
    a = result.getchannel("A")
    maximum = a.getextrema()[1]
    if maximum and maximum < 255:
        a = a.point(lambda v: min(255, round(v * 255 / maximum)))
    for p in [(0, 0), (result.width - 1, 0), (0, result.height - 1), (result.width - 1, result.height - 1)]: a.putpixel(p, 0)
    result.putalpha(a)
    result.save(out)

def convert(processed, runtime, size):
    subprocess.run(["python", "-B", str(CONVERTER), "--input", str(processed), "--output", str(runtime), "--width", str(size[0]), "--height", str(size[1])], check=True)

def contact(paths, out, title, cols):
    cw, ch = 170, 155
    rows = (len(paths) + cols - 1) // cols
    sheet = Image.new("RGBA", (cw * cols, ch * rows + 30), (26, 28, 30, 255))
    draw = ImageDraw.Draw(sheet); draw.text((10, 7), title, fill=(240, 240, 240, 255))
    for i, (label, path) in enumerate(paths):
        im = Image.open(path).convert("RGBA"); im.thumbnail((132, 116), Image.Resampling.NEAREST)
        row, col = divmod(i, cols)
        sheet.alpha_composite(im, (col * cw + (cw - im.width) // 2, row * ch + 31 + (116 - im.height) // 2))
        draw.text((col * cw + 4, row * ch + 140), label[:25], fill=(220, 220, 220, 255))
    sheet.convert("RGB").save(out)

def main():
    for d in [SRC_D, SRC_C, ALPHA_D, ALPHA_C, PROC_D, PROC_C, DECODE_D, DECODE_C, RUNTIME_D, RUNTIME_C, CONTACT, RECORDS, VALIDATION]: d.mkdir(parents=True, exist_ok=True)
    a1 = SRC_D / "aftermath_decisions_atlas_01_source.png"; a2 = SRC_D / "aftermath_decisions_atlas_02_source.png"; ac = SRC_C / "aftermath_categories_atlas_source.png"
    crop(a1, SRC_D, [n for n, _ in DECISIONS[:12]], 6, [0, 286, 572, 858, 1144, 1430, 1717], [112, 458, 916])
    crop(a2, SRC_D, [n for n, _ in DECISIONS[12:]], 5, [0, 397, 793, 1189, 1586, 1983], [0, 397, 793])
    crop(ac, SRC_C, [n for n, _ in CATEGORIES], 4, [0, 496, 992, 1488, 1983], [0, 793])
    assets = []
    for name, rationale in DECISIONS:
        source = SRC_D / f"{name}_source.png"; alpha = ALPHA_D / f"{name}_alpha.png"; proc = PROC_D / f"{name}.png"; runtime = RUNTIME_D / f"aftermath_{name}.dds"; decoded = DECODE_D / f"{name}_decoded.png"
        key(source, alpha); normalize(alpha, proc, (32, 32)); convert(proc, runtime, (32, 32)); Image.open(runtime).convert("RGBA").save(decoded)
        assets.append({"type":"decision","name":name,"source_mode":"imagegen_atlas_crop","sprite":f"GFX_decision_brilliant_scientist_aftermath_{name}","size":"32x32","source":str(source.relative_to(ROOT)).replace('\\','/'),"alpha":str(alpha.relative_to(ROOT)).replace('\\','/'),"processed":str(proc.relative_to(ROOT)).replace('\\','/'),"runtime":str(runtime.relative_to(ROOT)).replace('\\','/'),"decoded":str(decoded.relative_to(ROOT)).replace('\\','/'),"source_sha256":sha(source),"processed_sha256":sha(proc),"runtime_sha256":sha(runtime),"rationale":rationale,"status":"complete"})
    for name, rationale in CATEGORIES:
        source = SRC_C / f"{name}_source.png"; alpha = ALPHA_C / f"{name}_alpha.png"; proc = PROC_C / f"{name}.png"; runtime = RUNTIME_C / f"aftermath_{name}.dds"; decoded = DECODE_C / f"{name}_decoded.png"
        key(source, alpha); normalize(alpha, proc, (50, 40)); convert(proc, runtime, (50, 40)); Image.open(runtime).convert("RGBA").save(decoded)
        assets.append({"type":"decision_category","name":name,"source_mode":"imagegen_atlas_crop","sprite":f"GFX_decision_category_brilliant_scientist_aftermath_{name}","size":"50x40","source":str(source.relative_to(ROOT)).replace('\\','/'),"alpha":str(alpha.relative_to(ROOT)).replace('\\','/'),"processed":str(proc.relative_to(ROOT)).replace('\\','/'),"runtime":str(runtime.relative_to(ROOT)).replace('\\','/'),"decoded":str(decoded.relative_to(ROOT)).replace('\\','/'),"source_sha256":sha(source),"processed_sha256":sha(proc),"runtime_sha256":sha(runtime),"rationale":rationale,"status":"complete"})
    with (RECORDS / "aftermath_decision_category_manifest.json").open("w", encoding="utf-8") as f: json.dump({"decision_count":22,"category_count":4,"assets":assets}, f, indent=2)
    with (RECORDS / "aftermath_assignment_ledger.tsv").open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f, delimiter='\t'); w.writerow(["decision_id_or_role","sprite_name","sprite_identifier"])
        for name,_ in DECISIONS: w.writerow([name,name,f"GFX_decision_brilliant_scientist_aftermath_{name}"])
    with (RECORDS / "aftermath_category_assignment_ledger.tsv").open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f, delimiter='\t'); w.writerow(["category_role","sprite_name","sprite_identifier"])
        for name,_ in CATEGORIES: w.writerow([name,name,f"GFX_decision_category_brilliant_scientist_aftermath_{name}"])
    contact([(n, PROC_D/f"{n}.png") for n,_ in DECISIONS], CONTACT/"aftermath_decisions_processed_contact_sheet.png", "Event 016 aftermath decisions — processed 32x32", 8)
    contact([(n, SRC_D/f"{n}_source.png") for n,_ in DECISIONS], CONTACT/"aftermath_decisions_sources_contact_sheet.png", "Event 016 aftermath decisions — source masters", 8)
    contact([(n, DECODE_D/f"{n}_decoded.png") for n,_ in DECISIONS], CONTACT/"aftermath_decisions_decoded_dds_contact_sheet.png", "Event 016 aftermath decisions — decoded DDS", 8)
    contact([(n, PROC_C/f"{n}.png") for n,_ in CATEGORIES], CONTACT/"aftermath_categories_processed_contact_sheet.png", "Event 016 aftermath categories — processed 50x40", 4)
    contact([(n, SRC_C/f"{n}_source.png") for n,_ in CATEGORIES], CONTACT/"aftermath_categories_sources_contact_sheet.png", "Event 016 aftermath categories — source masters", 4)
    contact([(n, DECODE_C/f"{n}_decoded.png") for n,_ in CATEGORIES], CONTACT/"aftermath_categories_decoded_dds_contact_sheet.png", "Event 016 aftermath categories — decoded DDS", 4)
    print({"decisions":22,"categories":4})

if __name__ == "__main__": main()
