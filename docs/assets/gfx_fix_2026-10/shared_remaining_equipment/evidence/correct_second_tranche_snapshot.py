from pathlib import Path
import json
p=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/second_tranche_lineage.json')
d=json.loads(p.read_text(encoding='utf-8-sig'))
d['snapshot_disposition']='historical_pre_approval_snapshot'
d['superseded_by']='docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/final_asset_lineage.json'
d['snapshot_note']='This lineage was captured before parent approval and runtime promotion. Its projectile_slot_v1 threshold mask was rejected for internal dark gaps; the corrected v2 mask and final promotion are recorded in final_asset_lineage.json and blueprint_overlay_lineage_v2.json.'
for a in d.get('accepted_assets',[]):
    a['status']='historical_pre_approval_snapshot'
d['validation']['second_tranche_processing']={
 'livens':'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/livens_processing.json',
 'zombie':'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/zombie_processing.json',
 'blueprint_and_corrected_overlay':'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/blueprint_overlay_lineage_v2.json'
}
d['validation']['final_dds_validation']=[
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/second_tranche_dds_validation.json',
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/second_tranche_v2_dds_validation.json'
]
d['validation']['final_review_sheets']=[
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/contact_sheets/second_tranche_final_native.png',
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/contact_sheets/second_tranche_final_smooth_4x.png'
]
d['validation']['corrected_overlay_composites']=[
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/projectile_slot_overlay_on_blueprint_v2.png',
 'docs/assets/gfx_fix_2026-10/shared_remaining_equipment/evidence/projectile_slot_overlay_on_blueprint_v2_4x.png'
]
d['runtime_promotion']='None as of this pre-approval snapshot. The later parent-approved six-texture promotion is recorded in final_asset_lineage.json and second_tranche_promotion.json.'
p.write_text(json.dumps(d,indent=2),encoding='utf-8')
print(json.dumps({'updated':str(p),'snapshot_disposition':d['snapshot_disposition'],'asset_statuses':[a['status'] for a in d['accepted_assets']],'processing_records':d['validation']['second_tranche_processing']},indent=2))
