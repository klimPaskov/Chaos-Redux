# Air Winter Decision Icon Handoff

Status: all nineteen sprites are registered and wired.

This package supplies one dedicated Air Winter response-category icon and eighteen dedicated decision icons. All nineteen sprite ids are registered in `interface/air_cleanliness_winter.gfx`, including `air_winter_designate_response_priority`.

## Exact sprite-to-DDS mapping

| Related consumer | Sprite ID | Runtime DDS | Native size |
| --- | --- | --- | --- |
| `air_winter_response_category` | `GFX_decision_air_winter_response_category` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_category.dds` | 52x40 |
| `air_winter_designate_response_priority` | `GFX_decision_air_winter_response_priority` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_priority.dds` | 32x32 |
| `air_winter_designate_reception_state` | `GFX_decision_air_winter_reception` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_reception.dds` | 32x32 |
| `air_winter_distribute_respirator_kits` | `GFX_decision_air_winter_respirators` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_respirators.dds` | 32x32 |
| `air_winter_convert_respiratory_clinics` | `GFX_decision_air_winter_clinics` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_clinics.dds` | 32x32 |
| `air_winter_station_roof_samplers` | `GFX_decision_air_winter_samplers` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_samplers.dds` | 32x32 |
| `air_winter_protect_crop_trials` | `GFX_decision_air_winter_crop_trials` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_crop_trials.dds` | 32x32 |
| `air_winter_clear_ash_routes` | `GFX_decision_air_winter_ash_clearance` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_ash_clearance.dds` | 32x32 |
| `air_winter_protect_rail_corridors` | `GFX_decision_air_winter_rail_corridors` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_rail_corridors.dds` | 32x32 |
| `air_winter_close_exposed_airfields` | `GFX_decision_air_winter_airfield_closure` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_airfield_closure.dds` | 32x32 |
| `air_winter_prepare_evacuation_ledger` | `GFX_decision_air_winter_evacuation_ledger` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_evacuation_ledger.dds` | 32x32 |
| `air_winter_enact_emergency_shelter_law` | `GFX_decision_air_winter_shelter_law` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_shelter_law.dds` | 32x32 |
| `air_winter_convert_greenhouse_refuge` | `GFX_decision_air_winter_greenhouse_refuge` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_greenhouse_refuge.dds` | 32x32 |
| `air_winter_controlled_evacuation` | `GFX_decision_air_winter_controlled_evacuation` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_controlled_evacuation.dds` | 32x32 |
| `air_winter_state_medical_triage` | `GFX_decision_air_winter_medical_triage` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_medical_triage.dds` | 32x32 |
| `air_winter_hold_abandonment_vote` | `GFX_decision_air_winter_abandonment_vote` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_abandonment_vote.dds` | 32x32 |
| `air_winter_seal_bunker_doors` | `GFX_decision_air_winter_bunker_seal` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_bunker_seal.dds` | 32x32 |
| `air_winter_final_evacuation` | `GFX_decision_air_winter_final_evacuation` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_final_evacuation.dds` | 32x32 |
| `air_winter_decontamination_gamble` | `GFX_decision_air_winter_decontamination` | `gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_decontamination.dds` | 32x32 |

## Sprite block

The response-priority entry and the remaining sprites below are registered in the existing block.

```text
spriteType = {
	name = "GFX_decision_air_winter_response_category"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_category.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_response_priority"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_response_priority.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_reception"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_reception.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_respirators"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_respirators.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_clinics"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_clinics.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_samplers"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_samplers.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_crop_trials"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_crop_trials.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_ash_clearance"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_ash_clearance.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_rail_corridors"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_rail_corridors.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_airfield_closure"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_airfield_closure.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_evacuation_ledger"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_evacuation_ledger.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_shelter_law"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_shelter_law.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_greenhouse_refuge"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_greenhouse_refuge.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_controlled_evacuation"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_controlled_evacuation.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_medical_triage"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_medical_triage.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_abandonment_vote"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_abandonment_vote.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_bunker_seal"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_bunker_seal.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_final_evacuation"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_final_evacuation.dds"
}

spriteType = {
	name = "GFX_decision_air_winter_decontamination"
	texturefile = "gfx/interface/air_cleanliness_winter/decisions/decision_air_winter_decontamination.dds"
}
```

## Individual review record

The review artifact is `contact_sheets/air_winter_decision_icons_dds_decoded_contact_sheet.png`. It was assembled only after decoding every final runtime DDS and includes both enlarged inspection tiles and the true native-size decode.

| Icon | Native-size review |
| --- | --- |
| Response category | The shield, black winter sun, icy rim, and ash/snow base remain distinct at 52x40. Its silhouette is suitably wider and heavier than the decisions. |
| Response priority | The worn abstract map board, warm central state area, and oversized muted-red pin remain distinct at 32x32. No border arrangement resembles a real country or territorial claim. |
| Reception | Open shelter and warm doorway read immediately. A bedroll and crate reinforce reception without crowding the 32x32 mark. |
| Respirators | Cloth mask and paired charcoal filters remain unambiguous and do not resemble zombie or skull imagery. |
| Clinics | Twin cylinders, hose, breathing mask, and medical cross read as a respiratory clinic package. |
| Samplers | Tripod, raised funnel, glass jar, vane, and ash specks read as measurement equipment, not a radio dish. |
| Crop trials | Living seedling inside the frosted cloche remains a clean protected-crop silhouette. |
| Ash clearance | Ochre plough blade visibly displaces black ash across road lines and reads as route clearance. |
| Rail corridors | Converging rails, sleeper rhythm, wheel, and protective arch retain a distinct transport-corridor read. |
| Airfield closure | Propeller, crossed barriers, chain, and padlock communicate deliberate closure without text. |
| Evacuation ledger | Open ruled book, pencil, and tied blank tag remain recognizable and contain no generated writing. |
| Shelter law | Gavel and reinforced shelter remain separable, giving the icon a direct legal-protection read. |
| Greenhouse refuge | Frosted greenhouse shell, warm open door, bench, and green plant retain the refuge concept. |
| Controlled evacuation | Boxy period bus, open door, and orderly bundled queue read clearly without a panic or military motif. |
| Medical triage | Three blank colour-tab tags, rolled bandage, and cross remain legible without text, injury, or gore. |
| Abandonment vote | Blank ballot entering the box and cracked-house plate communicate the settlement vote directly. |
| Bunker seal | Closed circular door, wheel, locking bars, and gasket clearly show a completed seal rather than an open bunker. |
| Final evacuation | A loaded period truck departs frozen ruins. Its direction and luggage load survive reduction. |
| Decontamination | Pump sprayer, crossed brush, and dirty-to-clean plate communicate manual decontamination without hazard motifs. |

## Technical validation

- `_tooling/process_air_winter_decision_icons.py` requires the exact nineteen expected assets and rejects missing or extra source, master, processed, decoded, or DDS files.
- The category is 52x40. All eighteen decisions are 32x32. Every DDS contains one image level in uncompressed 32-bit BGRA with masks `00FF0000`, `0000FF00`, `000000FF`, and `FF000000`.
- Every DDS decode is pixel-identical to its processed PNG. All assets have visible alpha, transparent corners, centered non-empty bounds, and no visible chroma-key residue.
- Raw sources, transparent masters, processed PNGs, and runtime DDS files are each unique across all nineteen concepts. The full decoded contact sheet SHA-256 is `162b5d6771c2cb02dff191595dba18d302301d0fec0482311d6fea1133bef146`.
- DirectXTex conversion used `C:/Users/klimp/AppData/Local/Temp/chaos_redux_tools/texconv-may2026.exe`, SHA-256 `dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06`. No fallback backend was invoked.
- Response-priority source PNG SHA-256: `cc013a230f3688db9b97928581ee0261f8a9d51d9b5e8c40280a65350e4ec7d6`. Transparent-master SHA-256: `3f8850de992ce95bc2c27d6c2d1b7b42e68f7c7470b7f5256d42103542165be1`.

| Sprite ID | Processed PNG SHA-256 | Runtime DDS SHA-256 |
| --- | --- | --- |
| `GFX_decision_air_winter_response_category` | `f093df1f51ecdb7f25295450c783e025399d16e53ba15ad5ee0649de013c8847` | `79df9304429a30b0ef6c495e70bde96cc3b4d3343b5e270d1dad06b3aa6ffc37` |
| `GFX_decision_air_winter_response_priority` | `3a210969ace16033f66176f3a36eec0af650d51c1920ccfaf6708c3d017017ef` | `b332cf066fee43e09be4b03fb33966f59aab4f5e6443f2bc947a5af7afa48470` |
| `GFX_decision_air_winter_reception` | `819c5f6d535178dfcaeab6fe6526216b5e8a3f97382d5ec0eeec8ba228da104a` | `f651aee94d04ff983e2e6c7f7f0f1d2de317d252623ecb29c4208c2df87afc0b` |
| `GFX_decision_air_winter_respirators` | `45e8ae95542dc90c45f5551353e1827d6c6633a81c31aab2260f648c66efc18c` | `c8db2c8151588ed55b096072ea7f8d6f7826d7a6e6c55ade0cfc846ec29532ea` |
| `GFX_decision_air_winter_clinics` | `51aaaf1ecd3dc989902ff5ed39fec13852f74e2a6b8723fb6d65d1ca68efef50` | `e5cccd912e6837fd4aeb80c242df043a9a4d1a54d1ff8dbbe51bde1d8a6a4293` |
| `GFX_decision_air_winter_samplers` | `98a137905a57da9e5a6384a8cb8e44aa239435345ed56aa00cd81bf967d3c2b0` | `7418e99b86f392f28c9824159e0fff4c2d0bba6f87d8f6a5e5fa3071a4f68b4c` |
| `GFX_decision_air_winter_crop_trials` | `99ec6cc1780ba317ebe4664db4223ae2bde1b5eea00192c6d612c94c5e98d856` | `5e64d1d1b3f068a47eca4eac33e80656d8ee27400718ef1ea76e8b2a3d5632ca` |
| `GFX_decision_air_winter_ash_clearance` | `9dec05f9f72a9d6e072cf5c65dd39a3dfd1a974ef6ed8cd3435789c3bf43a381` | `38623f550d634d3ec12635d0a805dfb901d165ac38e27729918b499e034d482f` |
| `GFX_decision_air_winter_rail_corridors` | `cb2ee8d2967262290e5df87ec36aa4da4e250f312287158b78884f09a0f91e09` | `f787e1d34513fc8a5c97f79f6d201dca3847613305fe1cba79890663c8ec1b1f` |
| `GFX_decision_air_winter_airfield_closure` | `8ff714a7b51ad7357958d01ccc6eb9e51ded7e4c78d736a85b4dfb75a0039891` | `bc5d8654213217cbd7784666b7cdaf0db13d27d75cc3b264053dc38aec71b5a6` |
| `GFX_decision_air_winter_evacuation_ledger` | `529831340a5aa780043ad5a69ba4a9c14d1b381f2b1cda01037a2868528b3108` | `f88e02a0933ca2738ada41214aabe1fd480e3dd5cec3fd8c3d9643013263c505` |
| `GFX_decision_air_winter_shelter_law` | `d46d7a04cbbb04494a11f36c37fd62cd482b74532205c953294bcb3636f91a95` | `4ef958a62a2dfe5863d516e4fcb68ecc5ccdc8d4e415df85394a3811c7690a13` |
| `GFX_decision_air_winter_greenhouse_refuge` | `8bd4c6f398dbade36d58336c7f826deba99a7f134e98454c0ab136512784ca43` | `c18e56cf59d4cb50452159835b94572888e08d520954dcb7e48b12d25529b6f9` |
| `GFX_decision_air_winter_controlled_evacuation` | `2ab1217c0cc832befc0305258e5fd8dbc6ee85fec0fc171c4be08a24809f17a0` | `878e518121acb4add6afa5890cc0e1f56457d60eccfc98dc6e4198aa271d0d64` |
| `GFX_decision_air_winter_medical_triage` | `84343f5aafcbdc30d853edc6771bdc9481429883cd127b4c8c27e64c762a3deb` | `23fd81d761728cab581eb71dc0d09ba77cfe034b2e17b8238272e57bc5e4d584` |
| `GFX_decision_air_winter_abandonment_vote` | `f145be0e6fe24ef4e6d6e726c174afc68ff0669e06c0dea76d9ed5a76b6c918a` | `95cc49bbe5efdc728641cba90f8495dc8d4dc6c2b4b0f083d048fdad1952e5fe` |
| `GFX_decision_air_winter_bunker_seal` | `81e63d11ce5d87ac93ad98b9b9f02073e4e0f501e596eaf5daf409432d62c2f8` | `88a0ca24375b780872a2c5384d6f0a93504479f1fa0432630dc6edeafcb906a6` |
| `GFX_decision_air_winter_final_evacuation` | `30edda6844f01f7e51c9ef6319742ef9551ddce27b153a6f7f1b040475d96bb9` | `74b46e6919c82e0adfec11d1b08997078c2e722785f811f00e1ae657a0fd9fd3` |
| `GFX_decision_air_winter_decontamination` | `c14724415ee63884f959082d4862c8614dac2425ab1c2a4a26ae960419d242ac` | `c975e6ccb9f1768294b6c264c8dd8055a1aaa1f299f630ddd5cc481b05575fc2` |

## Simplifications, omissions, and blockers

None. All nineteen package IDs have individually generated, reviewed, distinct source art, transparent editable masters, processed native-size PNGs, decoded runtime DDS proof, manifest rows, prompt provenance, and exact sprite entries. No placeholder, source reuse, silent fallback, zombie material, or unrelated edit was used.

Skills used: `chaos-redux-event-assets`, `chaos-redux-subagents`, and `imagegen`. No skill was created or updated. This package followed the existing reusable workflows without exposing an uncovered general process.
