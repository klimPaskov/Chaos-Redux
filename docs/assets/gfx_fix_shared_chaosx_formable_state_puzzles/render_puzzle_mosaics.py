"""Render isolated before/after state-puzzle mosaics from manifest coordinates."""

from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "docs/assets/gfx_fix_shared_chaosx_formable_state_puzzles"
INVENTORY = json.loads((WORK / "input_inventory_v2.json").read_text(encoding="utf-8"))
CANDIDATES = json.loads((WORK / "processed_v3/puzzle_candidates_v3.json").read_text(encoding="utf-8"))
candidate_by = {(a["family"],a["state_id"],a["variant"]):a for a in CANDIDATES["assets"]}
snapshot_by_path = {a["runtime_dds"]:a for a in INVENTORY["assets"]}
ring_by_state = {(r["family"],r["state_id"]):r for r in INVENTORY["island_ring_states"]}
FAMILIES = INVENTORY["palette_families"] + ["GOE_form_hindustan","unite_maghreb","proclaim_greater_italy","unite_latin_africa"]
MOSAICS = WORK / "mosaics_v3"
SHEETS = WORK / "contact_sheets" / "mosaics_v3"
MOSAICS.mkdir(parents=True,exist_ok=True)
SHEETS.mkdir(parents=True,exist_ok=True)
FONT = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
SMALL = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 12)

def read_image(path: Path) -> Image.Image:
	return Image.open(path).convert("RGBA")

def runtime_before(family: str, state_id: int, variant: str, path_text: str) -> Image.Image:
	item=snapshot_by_path.get(path_text)
	if item:
		return read_image(ROOT/item["before_png"])
	return read_image(ROOT/path_text)

def current_or_candidate(family: str, state_id: int, variant: str, path_text: str) -> tuple[Image.Image,bool]:
	item=candidate_by.get((family,state_id,variant))
	if item:
		return read_image(ROOT/item["processed_png"]),True
	return read_image(ROOT/path_text),False

def family_spec(family: str):
	path=ROOT/"docs/formables/state_puzzles"/family/"manifest.json"
	manifest=json.loads(path.read_text(encoding="utf-8-sig"))
	canvas=manifest.get("projection",{}).get("canvas",manifest.get("canvas"))
	if not canvas:raise RuntimeError(f"missing registered projection canvas: {family}")
	entries=[]
	if manifest.get("assets"):
		for item in manifest["assets"]:
			bbox=item["bbox"]
			entries.append({"state_id":item["state_id"],"variant":item["variant"],"path":item["dds"],"position":bbox[:2],"declared_size":[bbox[2]-bbox[0],bbox[3]-bbox[1]]})
	else:
		for state in manifest.get("states",[]):
			position=state.get("position")
			if isinstance(position,dict):position=[position["x"],position["y"]]
			if position is None:position=state.get("canvas_position",state.get("projection_position"))
			for variant,path in state["runtime_dds"].items():
				entries.append({"state_id":state["state_id"],"variant":variant,"path":path,"position":position,"declared_size":state.get("projected_mask_size")})
	return manifest,tuple(canvas),entries

def compose(family: str, variant: str, *, after: bool) -> tuple[Image.Image,list]:
	manifest,canvas_size,entries=family_spec(family)
	mosaic=Image.new("RGBA",canvas_size,(0,0,0,0));positions=[]
	for entry in entries:
		if entry["variant"]!=variant:continue
		state_id=entry["state_id"];path_text=entry["path"]
		if after:
			image,changed=current_or_candidate(family,state_id,variant,path_text)
			marker=ring_by_state.get((family,state_id))
			position=marker["new_gui_position"] if changed and marker else entry["position"]
		else:
			image=runtime_before(family,state_id,variant,path_text);changed=False;position=entry["position"]
		if entry.get("declared_size") and not changed and tuple(entry["declared_size"])!=image.size:
			# Some old manifests describe projected geometry with half-open bounds;
			# the authoritative installed texture dimensions remain the rendered size.
			pass
		x,y=position
		mosaic.alpha_composite(image,dest=(x,y))
		positions.append({"state_id":state_id,"variant":variant,"position":position,"image_size":image.size,"candidate":changed})
	return mosaic,positions

records=[]
for family in FAMILIES:
	rows=[]
	manifest,canvas_size,_entries=family_spec(family)
	for variant in ("unresolved","qualifying"):
		before,before_positions=compose(family,variant,after=False)
		after,after_positions=compose(family,variant,after=True)
		before_path=MOSAICS/f"{family}_{variant}_before.png";after_path=MOSAICS/f"{family}_{variant}_candidate.png"
		before.save(before_path);after.save(after_path)
		rows.append((variant,before,after,before_path,after_path,before_positions,after_positions))
	# One row contains both status mosaics: old unresolved/new unresolved, old qualifying/new qualifying.
	w,h=canvas_size
	cell_w,cell_h=w,h
	sheet=Image.new("RGB",(4*cell_w+48,cell_h+94),(29,30,32));d=ImageDraw.Draw(sheet)
	d.text((12,10),f"{family}: full puzzle mosaics at registered coordinates",font=FONT,fill=(240,238,229))
	labels=["Before - unresolved","Candidate - unresolved","Before - qualifying","Candidate - qualifying"]
	imgs=[rows[0][1],rows[0][2],rows[1][1],rows[1][2]]
	for i,(label,image) in enumerate(zip(labels,imgs)):
		x=12+i*(cell_w+6);d.text((x,36),label,font=SMALL,fill=(220,216,205));sheet.paste(image.convert("RGB"),(x,56))
	spath=SHEETS/f"{family}_before_after_mosaics.png";sheet.save(spath)
	records.append({"family":family,"canvas":canvas_size,"before_unresolved":str(rows[0][3].relative_to(ROOT)).replace("\\","/"),"candidate_unresolved":str(rows[0][4].relative_to(ROOT)).replace("\\","/"),"before_qualifying":str(rows[1][3].relative_to(ROOT)).replace("\\","/"),"candidate_qualifying":str(rows[1][4].relative_to(ROOT)).replace("\\","/"),"review_sheet":str(spath.relative_to(ROOT)).replace("\\","/"),"unresolved_state_count":len(rows[0][5]),"qualifying_state_count":len(rows[1][5]),"ring_states":[r["state_id"] for r in INVENTORY["island_ring_states"] if r["family"]==family]})

# Detailed before/after state tiles for the eight deliberately enlarged island markers.
markers=INVENTORY["island_ring_states"]
columns=4; tile_w=210; tile_h=145; label_h=44
detail=Image.new("RGB",(columns*tile_w,len(markers)*(tile_h+label_h)),(28,30,32));draw=ImageDraw.Draw(detail)
for i,marker in enumerate(markers):
	family=marker["family"];sid=marker["state_id"];items=[("Before unresolved",family,sid,"unresolved"),("After unresolved",family,sid,"unresolved"),("Before qualifying",family,sid,"qualifying"),("After qualifying",family,sid,"qualifying")]
	draw.text((4,i*(tile_h+label_h)+2),f"{family} state {sid}",font=SMALL,fill=(240,238,229))
	for col,(label,fam,state,variant) in enumerate(items):
		x=col*tile_w;y=i*(tile_h+label_h);draw.text((x+4,y+22),label,font=SMALL,fill=(220,216,205))
		path_text=next(a["runtime_dds"] for a in INVENTORY["assets"] if a["family"]==family and a["state_id"]==state and a["variant"]==variant)
		if col in (0,2):image=runtime_before(family,state,variant,path_text)
		else:image,_=current_or_candidate(family,state,variant,path_text)
		bg=Image.new("RGBA",image.size,(40,41,39,255));bg.alpha_composite(image);scale=min(8,130//max(image.size));zoom=bg.resize((image.width*scale,image.height*scale),Image.Resampling.NEAREST);detail.paste(zoom.convert("RGB"),(x+4,y+label_h))
detail_path=SHEETS/"island_marker_state_detail_before_after.png";detail.save(detail_path)
(WORK/"mosaics_v3"/"mosaic_review_index_v3.json").write_text(json.dumps({"families":records,"island_detail_sheet":str(detail_path.relative_to(ROOT)).replace("\\","/")},indent=2)+"\n",encoding="utf-8")
for record in records:print(record["family"],record["review_sheet"])
print("island marker detail",detail_path)
