from pathlib import Path
import hashlib,json,subprocess
root=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def record(p,role): return {'path':str(p),'sha256':sha(p),'role':role}
coal_attempts=[
 {'id':'coal_golem_equipment_v1','prompt':str(root/'prompts/coal_golem_equipment_v1.json'),'tool_output':'C:/Users/klimp/.codex/generated_images/01a11102-7db8-7810-8c03-657dcb01189a/exec-91bd5cf1-868e-4689-86e9-841eb6068f79.png','retained_source':str(root/'source_png/coal_golem_equipment_v1.png'),'sha256':sha(root/'source_png/coal_golem_equipment_v1.png'),'status':'rejected','reason':'subject touched/cropped canvas edges'},
 {'id':'coal_golem_equipment_v2','prompt':str(root/'prompts/coal_golem_equipment_v2.json'),'tool_output':'C:/Users/klimp/.codex/generated_images/01a11102-7db8-7810-8c03-657dcb01189a/exec-614041de-dab0-469a-aed5-825382fbffce.png','retained_source':str(root/'source_png/coal_golem_equipment_v2.png'),'sha256':sha(root/'source_png/coal_golem_equipment_v2.png'),'status':'rejected','reason':'complete alpha but too narrow for the wide target'},
 {'id':'coal_golem_equipment_v3','prompt':str(root/'prompts/coal_golem_equipment_v3.json'),'tool_output':'C:/Users/klimp/.codex/generated_images/01a11102-7db8-7810-8c03-657dcb01189a/exec-8ed8ecf6-76ce-471f-a728-d05dd627f912.png','retained_source':str(root/'source_png/coal_golem_equipment_v3.png'),'sha256':sha(root/'source_png/coal_golem_equipment_v3.png'),'status':'rejected','reason':'wide bust still touches/crops canvas edges'},
 {'id':'coal_golem_equipment_v4','prompt':str(root/'prompts/coal_golem_equipment_v4.json'),'tool_output':'C:/Users/klimp/.codex/generated_images/01a11102-7db8-7810-8c03-657dcb01189a/exec-3f5132d5-0969-4619-8adc-2be1a91dfbae.png','retained_source':str(root/'source_png/coal_golem_equipment_v4.png'),'sha256':sha(root/'source_png/coal_golem_equipment_v4.png'),'status':'rejected','reason':'subject remained too close to the bottom edge'},
 {'id':'coal_golem_equipment_v5','prompt':str(root/'prompts/coal_golem_equipment_v5.json'),'tool_output':'C:/Users/klimp/.codex/generated_images/01a11102-7db8-7810-8c03-657dcb01189a/exec-18b9dc9f-e395-4cce-875e-d5f4bb294b62.png','retained_source':str(root/'source_png/coal_golem_equipment_v5.png'),'sha256':sha(root/'source_png/coal_golem_equipment_v5.png'),'status':'selected_and_parent_approved'}
]
assets=[]
inputs={
 'coal_golem_equipment':{
  'sprites':['GFX_coal_golem_equipment_medium','GFX_coal_golem_equipment_1_medium'],
  'runtime':'gfx/interface/technologies/coal_golem_equipment.dds','baseline':root/'originals/dds/coal_golem_equipment.dds',
  'source':root/'source_png/coal_golem_equipment_v5.png','prompt':root/'prompts/coal_golem_equipment_v5.json',
  'references':[
   record(root/'originals/png/coal_golem_equipment.png','existing opaque golem subject identity'),
   record('.agents/skills/chaos-redux-event-assets/assets/gfx_references/units/equipment/technology_art/support_equipment_1.png','canonical vanilla equipment painting/material style')],
  'processed':root/'processed_png/coal_golem_equipment_v5_131x52.png','staged':root/'staged_dds/coal_golem_equipment.dds'},
 'tabun_projectile':{
  'sprites':['GFX_EMI_livens_tabun_projectile'],
  'runtime':'gfx/interface/equipmentdesigner/modules/tabun_projectile.dds','baseline':root/'originals/dds/phosgene_projectile.dds',
  'source':root/'source_png/tabun_projectile_v1.png','prompt':root/'prompts/tabun_projectile_v1.json',
  'references':[
   record(root/'originals/png/phosgene_projectile.png','current phosgene capsule: module silhouette/style only'),
   record(root/'evidence/family_style/soman_projectile.png','current Livens sibling module: paint/material family only')],
  'processed':root/'processed_png/tabun_projectile_v1_56x42.png','staged':root/'staged_dds/tabun_projectile.dds','palette_reference':'parent-approved Tabun oxblood #55181E as a narrow physical band on a dark-olive body'},
 'archetype_livens_projector':{
  'sprites':['GFX_archetype_livens_projector_equipment_medium'],
  'runtime':'gfx/interface/archetypes/archetype_livens_projector_equipment.dds','baseline':root/'originals/dds/archetype_livens_projector_equipment.dds',
  'source':root/'source_png/archetype_livens_projector_v1.png','prompt':root/'prompts/archetype_livens_projector_v1.json',
  'references':[
   record(root/'evidence/vanilla_inspection/archetype_support_equipment.png','exact installed vanilla support archetype converted for inspection; beige silhouette style'),
   record(root/'evidence/vanilla_inspection/archetype_motorized_equipment.png','exact installed vanilla motorized archetype converted for inspection; compact shading/scale')],
  'processed':root/'processed_png/archetype_livens_projector_v1_58x40.png','staged':root/'staged_dds/archetype_livens_projector_equipment.dds'}
}
for name,spec in inputs.items():
 baseline=spec['baseline']
 out={k:v for k,v in spec.items() if k not in ('baseline','source','prompt','processed','staged')}
 out.update({'baseline_dds_path':str(baseline),'baseline_dds_sha256':sha(baseline),'source_path':str(spec['source']),'source_sha256':sha(spec['source']),'prompt_record':str(spec['prompt']),'processed_png_path':str(spec['processed']),'processed_png_sha256':sha(spec['processed']),'staged_dds_path':str(spec['staged']),'staged_dds_sha256':sha(spec['staged']),'runtime_sha256':sha(spec['runtime']),'status':'parent_approved_and_promoted'})
 assets.append(out)
# Exact project GFX source snapshot and current parent-owned alias hash.
gfx='interface/chaosx_equipment.gfx'
try: head=subprocess.check_output(['git','rev-parse',f'HEAD:{gfx}'],text=True,stderr=subprocess.DEVNULL).strip()
except subprocess.CalledProcessError: head=None
report={'workspace':str(root),'source_plan':'C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md','source_plan_sha256':'A7D534DCA813E1BD8E9245F80DB02FB54DA5A76A548662950FCFBBFD4A3A46C3','raw_issues_json':'C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_issues.json','raw_issues_sha256':'0E3B24B887C7A3EC1148E023A05D9FF3D059DF906B10540391CAAA4B5F4701DC','reference_contact_sheet':'.agents/skills/chaos-redux-event-assets/assets/gfx_references/units/equipment/technology_art/contact_sheet.png','reference_contact_sheet_sha256':'B8A2F2CD641BBA79B9F49D71DF3B4B3FBAB7DF05FF6C5787DA750121391EA80E','current_gfx':{'path':gfx,'sha256':sha(gfx),'head_blob':head,'ownership':'parent; worker made no GFX changes'},'accepted_assets':assets,'coal_candidate_lineage':coal_attempts,'review_sheets':[{'path':str(root/'contact_sheets/first_tranche_native.png'),'sha256':sha(root/'contact_sheets/first_tranche_native.png')},{'path':str(root/'contact_sheets/first_tranche_smooth_4x.png'),'sha256':sha(root/'contact_sheets/first_tranche_smooth_4x.png')}], 'dds_validation':str(root/'evidence/first_tranche_dds_validation.json'),'promotion_guard':str(root/'evidence/first_tranche_promotion.json')}
out=root/'evidence/first_tranche_lineage.json'
out.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'lineage_path':str(out),'lineage_sha256':sha(out),'current_gfx_sha256':report['current_gfx']['sha256'],'head_blob':head,'selected_source_hashes':[a['source_sha256'] for a in assets],'processed_hashes':[a['processed_png_sha256'] for a in assets],'dds_hashes':[a['staged_dds_sha256'] for a in assets]},indent=2))
