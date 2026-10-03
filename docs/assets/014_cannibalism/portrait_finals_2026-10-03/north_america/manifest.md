# Event 014 North America Warlord Portrait Candidates

Status: Parent source/framing and final DDS visual review approved all eight North America portraits. Their exact approved BGRA32 candidate bytes are installed at the eight existing runtime DDS paths. The 60-file install snapshot confirms only these eight runtime DDS files changed; GFX and character definitions are unchanged.

## Scope and acceptance basis

This tranche covers only CBA-CBH in the North America region of the accepted 56-portrait Event 014 matrix. The accepted Part 10 portrait criteria require seven distinct regional variants for each of eight reusable slots, with bald male-presenting feral human leader busts, blood and war-horror detail, unique faces, poses, props, clothing silhouettes, crops and backgrounds, and no prison or detention setting. The corresponding Part 12 criteria require all 56 regional portraits to remain distinct and correctly matched to their region.

The parent continuation report dated 2026-10-03 accepts original native fictional production within the already authorized 56-final scope. CBA-CBH are treated as invented Event 014 identities rather than grounded people, offices or real polities. Source mode is `fictional_high_chaos`; no real-person source archive or attribution URL applies.

The eight North America signatures are fixed as follows: CBA balances a splintered wagon-wheel spoke across one shoulder while watching sideways; CBB tosses a torn service cap between both hands with scalp uncovered; CBC wrings a blood-flecked uniform sleeve strip with a crooked grin; CBD slams a dented camp cooking pot against his palm with an open-mouthed snarl; CBE bends a rusty crowbar between dirty clenched hands as a rage gesture; CBF digs his nails into an empty cracked leather map case; CBG holds a jagged vehicle mirror beside his face and bares his teeth at his own reflection; CBH pulls apart a broken leather boot lace with his jaw tense.

## Native ImageGen and references

Each slot has one separate built-in native ImageGen call, one original prompt, no input image, and no retry. The exact prompts, tool-returned output paths, route, prompt hashes, output hashes, and copy-equality evidence are in `evidence/imagegen_call_log.json`; exact prompt text is also stored in `prompts/`.

All eight native tool outputs are opaque RGB images because `transparent_background=false`. Their original tool outputs remain under `C:/Users/klimp/.codex/generated_images/`, and their byte-identical project copies are under `source_png/`. No CLI/API generation route, Internet image, third-party raster or other portrait was used. No separate legal license claim is made for generated output.

The installed vanilla leader family was inspected at its actual 156x210 consumer size. The reference audit records the canonical leader contact sheet, three canonical shelf PNGs, the corresponding installed vanilla DDS paths, SHA-256 hashes and decoded-pixel equality. The inspected references informed painted rendering, restrained backgrounds and leader-bust framing only. The parent-approved Europe set was inspected for rendering and framing coherence only; no Europe or vanilla raster was attached to a generation call or used as identity source material. The portrait-backdrops reference family was not used.

Existing Europe, Asia, Africa and Middle East portraits, manifests and current prompts were checked for cross-region distinctness. Each North America prop/action is separate from the previously reserved Europe skull/bone/glove/cleaver/dog-tags/sack/shovel actions, Asia radio/mess-tin/bayonet/ledger/wire/spoon/bone-awl/bottle actions, Africa buckle/cup/ration-tin/harness/cartridge-cases/binoculars/pay-token/chain actions, and Middle East whistle/button/padlock/gauze/crate-lid/meat-hook/helmet/tooth/handkerchief actions. Read-only source paths and findings are in `evidence/cross_region_distinctness_review.json`.

## Candidate inventory and consumer crosswalk

| Slot | Assigned action | Native source and SHA-256 | Processed 156x210 preview and SHA-256 | Existing sprite and runtime DDS target |
| --- | --- | --- | --- | --- |
| CBA | Wagon-wheel spoke over shoulder; sideways gaze | `source_png/leader_CBA_warlord_north_america_source.png`, 1081x1455, `17047becc79ec49499a678511d8e2d2607a594d42779f15e99345361682e406b` | `processed_png/leader_CBA_warlord_north_america_156x210.png`, `5ad8d99d01f66560d12d8223dcba5dfe6d7e28b51c6515013b0b8182f93eee4d` | `GFX_portrait_CBA_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBA_warlord_north_america.dds` |
| CBB | Torn service cap mid-toss between both hands | `source_png/leader_CBB_warlord_north_america_source.png`, 1082x1454, `900e89cbc638b927eff5844f426fdf1d18b1f2fb42ea5ef247ed8eabc8b165bc` | `processed_png/leader_CBB_warlord_north_america_156x210.png`, `f9599de35183d39b037b4a3753297393afdf462a3b74477ab9f14a38791b9472` | `GFX_portrait_CBB_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBB_warlord_north_america.dds` |
| CBC | Wringing blood-flecked sleeve strip; crooked grin | `source_png/leader_CBC_warlord_north_america_source.png`, 1082x1454, `2b67e850c97eaff5a5c0e76f3f0fbfad29eda57f5d6acc4dd5c88912dd12a4fc` | `processed_png/leader_CBC_warlord_north_america_156x210.png`, `a0d336c61c4b75b63c22820b0264498675f59d8f55f126850a5838624dd4b7fd` | `GFX_portrait_CBC_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBC_warlord_north_america.dds` |
| CBD | Dented camp pot struck against palm; open snarl | `source_png/leader_CBD_warlord_north_america_source.png`, 1082x1453, `76fd9dfb825ef1eb87d63b7a735221f591c9fcb9cda3f7f351cf5445383679a0` | `processed_png/leader_CBD_warlord_north_america_156x210.png`, `accbfa3934ef07882986d8f24211d88d2a1087dbc5a6cd90fc2735a6665feb14` | `GFX_portrait_CBD_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBD_warlord_north_america.dds` |
| CBE | Already bowed crowbar gripped in both dirty hands | `source_png/leader_CBE_warlord_north_america_source.png`, 1081x1455, `966cd59a4c9d815eeda7ab75dd67d0bb24fb10577cfad42d7660a7c681ca6a6a` | `processed_png/leader_CBE_warlord_north_america_156x210.png`, `aad08857e84bfae7727195ecbbfc502971ea4e5106e8d8ad16558a50b86266c6` | `GFX_portrait_CBE_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBE_warlord_north_america.dds` |
| CBF | Pressing fingernails into empty cracked map case | `source_png/leader_CBF_warlord_north_america_source.png`, 1080x1456, `8633ac0c8a2e756c40492898230dba267bc30b98e111d11bf083e48df6179fc8` | `processed_png/leader_CBF_warlord_north_america_156x210.png`, `53ec20ff904d45bc047ec0edfe82526b98016a9e82c644e1e7bf49ec01c4700c` | `GFX_portrait_CBF_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBF_warlord_north_america.dds` |
| CBG | Bared teeth at his own reflection in a jagged vehicle mirror | `source_png/leader_CBG_warlord_north_america_source.png`, 1081x1455, `f89b21584ff4a094eb9bb1a1c2e74ec9354997257cce5a34087ab32e26ae7cb9` | `processed_png/leader_CBG_warlord_north_america_156x210.png`, `e91f1c6df1c40d030c98c1f28de46ed347a541ef5cf729c13c9abc4237e47b7e` | `GFX_portrait_CBG_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBG_warlord_north_america.dds` |
| CBH | Pulling apart a broken leather boot lace | `source_png/leader_CBH_warlord_north_america_source.png`, 1080x1456, `f47a82a839df9c9e95bd0079f80aa2eb02d8958d8311c42b6ddfddbdcbfa3c2d` | `processed_png/leader_CBH_warlord_north_america_156x210.png`, `300bdc08993f575e9800bb9ecc035661e2ca5bf9fb862aaada5b27def21eaca8` | `GFX_portrait_CBH_warlord_north_america` → `gfx/leaders/014_cannibalism/leader_CBH_warlord_north_america.dds` |

All crop bounds, crop PNG hashes, prompt hashes, native-copy checks and resize details are in `metadata/CBA_metadata.json` through `metadata/CBH_metadata.json` and `evidence/output_inventory.json`. The processing script performs only a tiny centered 26:35 aspect correction where required and a deterministic Lanczos resize to 156x210; it does not repaint, recolor, filter, remove backgrounds or add content.

## Visual review and protection state

The producer reviewed each full-size native master, all eight processed previews at 156x210, the 4x nearest-neighbour contact sheet and the native-size contact sheet. The parent reviewed the native 156x210 contact and approved source art and framing for this bounded eight-portrait set; the acceptance is within the existing 56-portrait scope and does not claim a new user-specific art decision. All eight show bald adult male human subjects with visible scalp, bloodshot asymmetric faces, scars or torn-lip war-horror details, invented rough clothing, distinct assigned actions and subdued opaque period backgrounds. The signature props remain readable at preview size. No visible text, logo, watermark, real-person likeness, Hannibal likeness, supernatural anatomy, animal body, prison/bar/detention imagery, prisoner clothing, sacred motif or ceremonial regalia appears. The parent source/framing receipt is `evidence/parent_source_framing_review.json`, and the per-slot review is in `evidence/visual_review.json`.

The preview sheets are `review/north_america_native_4x2_contact_sheet.png` (624x420) and `review/north_america_nearest4_4x2_contact_sheet.png` (2496x1680), ordered CBA-CBH as recorded in `review/contact_sheet_order.txt`. The DDS-decoded review sheets are `review/north_america_dds_decoded_native_4x2_contact_sheet.png` (624x420) and `review/north_america_dds_decoded_nearest4_4x2_contact_sheet.png` (2496x1680).

The current North America runtime files, `interface/014_cannibalism.gfx`, `common/characters/014_cannibalism_characters.txt`, the canonical ordinary and Wendigo Hannibal DDS files, and both animated Hannibal sheets were hashed before production in `evidence/runtime_preinstall_snapshot.json`. The runtime crosswalk contains exact GFX entry names, line numbers, DDS targets and baseline hashes. No GFX, character or runtime file was changed.

After parent source/framing approval, all eight processed PNGs were converted through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` into the isolated `candidate_dds/` folder. The bundled converter selected its FFmpeg BGRA writer because `texconv` and `texconv.exe` were absent at preflight. Each output is a 156x210, 131168-byte legacy BGRA32 DDS with a 128-byte header, one image level, no mip chain and an alpha range of 255-255. All eight decoded RGBA pixel buffers exactly match their processed PNGs, and all file hashes and decoded-pixel hashes are unique. Header fields, channel masks, byte counts, alpha, PNG-to-DDS pixel equality, DDS hashes and contact sheets are in `evidence/dds_roundtrip_audit.json`.

The parent reviewed and approved the decoded native-size DDS contact sheet and exact DDS candidates recorded in `docs/plans/014_cannibalism_plans/evidence/2026-10-03_north_america_portrait_parent_review.json`. The eight approved candidate files are installed byte-for-byte at their existing runtime paths. The before/after 60-file snapshots and exact hashes are recorded in `evidence/runtime_install_preinstall_all60_snapshot.json`, `evidence/runtime_install_postinstall_all60_snapshot.json` and `evidence/runtime_install_receipt.json`.

| Slot | Candidate DDS | Dimensions and bytes | DDS SHA-256 | Decoded RGBA pixel SHA-256 |
| --- | --- | --- | --- | --- |
| CBA | `candidate_dds/leader_CBA_warlord_north_america.dds` | 156x210, 131168 | `84d5825c1341120a177b8a65b75d2113aab888706976d7f2965ce7d90921f0d4` | `0e083f937371bb509fbe65dcb2cae9b88336e8549d3fde33014ac3bcc9af077a` |
| CBB | `candidate_dds/leader_CBB_warlord_north_america.dds` | 156x210, 131168 | `396d81b9ac64f5a5b9c0d35b532b24c322e6b5c9be7e2ff3f50aec8121dc3243` | `d41ca254e4343d8827d0a1353d5c841074da5a11d37f9ad948d05ebcce2145ac` |
| CBC | `candidate_dds/leader_CBC_warlord_north_america.dds` | 156x210, 131168 | `e7d60912994d0f949a77dca785d3932e4eaa154c6915de1dc6d1a0e12c890dbb` | `98ca97f64e3c4d3e3a586c5de09ab498179c356053979c51f2f8e67212e6accd` |
| CBD | `candidate_dds/leader_CBD_warlord_north_america.dds` | 156x210, 131168 | `950c13ea6ade4aa259ae74b0cc830bf5ab2b65538a529be78a9d6d404a16be70` | `3aa7074143de5ccb8668ffa802d5955a90c4b77ef01c89fc3f969538c32bd54f` |
| CBE | `candidate_dds/leader_CBE_warlord_north_america.dds` | 156x210, 131168 | `ba906c3f4dc070b92e8a08a0b25abc1a879aab0a8c49a61d18afaac58ea705b6` | `cc6e06b09be42e578412eb6567598c740c1cd9c9660816cdaf97ae3a13b172c3` |
| CBF | `candidate_dds/leader_CBF_warlord_north_america.dds` | 156x210, 131168 | `f0882bb9386f81bb2349c4f7f429cadfb32533621a8d91c32bb357c099cb83ea` | `246b792669820336eb7cecd0147ac6b3bcfbeca17c8d53ea09daaa7715d604ca` |
| CBG | `candidate_dds/leader_CBG_warlord_north_america.dds` | 156x210, 131168 | `21bedb01dee201b04f793da693727d0a18f2dc29357ec751a4d3a5cb0ed9f12b` | `b00ec88d3180c57bfb8367388ef8f3d366d4b0494ea5a78247882e3cce291485` |
| CBH | `candidate_dds/leader_CBH_warlord_north_america.dds` | 156x210, 131168 | `0592b9dc392572cbe0507c7dc9a9a7f9561c4b9058e6d9527f6d1799b3cc1413` | `f55696c3bae4013d54912b06645c2ee853caea1bac8edb7dc29f85249780eeda` |

| Slot | Existing runtime DDS | Pre-install SHA-256 | Installed SHA-256 |
| --- | --- | --- | --- |
| CBA | `gfx/leaders/014_cannibalism/leader_CBA_warlord_north_america.dds` | `eb651b2337e1254cd2ab3ca17618735f677ad279816e1d8b1ab3d9131afd5018` | `84d5825c1341120a177b8a65b75d2113aab888706976d7f2965ce7d90921f0d4` |
| CBB | `gfx/leaders/014_cannibalism/leader_CBB_warlord_north_america.dds` | `07582af60ccbf38433daa2c9393a41bc8e5c335f891e38cb1bcf253c2a00353b` | `396d81b9ac64f5a5b9c0d35b532b24c322e6b5c9be7e2ff3f50aec8121dc3243` |
| CBC | `gfx/leaders/014_cannibalism/leader_CBC_warlord_north_america.dds` | `2aaea3d0e9ff4b6046b17c603706a1af5d0f9422583778df2e4f165fe760982e` | `e7d60912994d0f949a77dca785d3932e4eaa154c6915de1dc6d1a0e12c890dbb` |
| CBD | `gfx/leaders/014_cannibalism/leader_CBD_warlord_north_america.dds` | `2fcf85c6dfa5d9f9412ec99c78126357a6f37f13572ad52a20ebd3b89ad35da7` | `950c13ea6ade4aa259ae74b0cc830bf5ab2b65538a529be78a9d6d404a16be70` |
| CBE | `gfx/leaders/014_cannibalism/leader_CBE_warlord_north_america.dds` | `19ac68a8bbe2c4575fd598cbfc13ecaae03c9cea9bff2fa8a3972e80c1e29099` | `ba906c3f4dc070b92e8a08a0b25abc1a879aab0a8c49a61d18afaac58ea705b6` |
| CBF | `gfx/leaders/014_cannibalism/leader_CBF_warlord_north_america.dds` | `374c6e948141e413ae9ae3ae5a4b01b966a86b468713c2e4fe610c361fcb8ced` | `f0882bb9386f81bb2349c4f7f429cadfb32533621a8d91c32bb357c099cb83ea` |
| CBG | `gfx/leaders/014_cannibalism/leader_CBG_warlord_north_america.dds` | `f12bd2c6f78784821b0182f69c3883e873c0d691ca642067076bbcfe6541ba1a` | `21bedb01dee201b04f793da693727d0a18f2dc29357ec751a4d3a5cb0ed9f12b` |
| CBH | `gfx/leaders/014_cannibalism/leader_CBH_warlord_north_america.dds` | `aff4159b8faf950b25404e6ed81c1040117e33f1cb309cd107e27309de6fc3f1` | `0592b9dc392572cbe0507c7dc9a9a7f9561c4b9058e6d9527f6d1799b3cc1413` |

## Event 014 matrix status

Global portrait count is parent-owned. The parent reports that all seven regions have eight portraits installed, for 56 of 56 total, as of 2026-10-03. This North America package independently receipts only CBA-CBH and the all-60 before/after installation snapshot; it makes no independent audit claim about the other six regions or global cross-region uniqueness.

No simplification, substitute identity, image-edit fallback, source raster reuse or unapproved route was used in this tranche.

## Current parent matrix checkpoint

The parent selected-art inventory is `docs/plans/014_cannibalism_plans/evidence/2026-10-03_global_portrait_review/candidate_inventory.json`.
It records 56 installed candidate matches and four protected Hannibal files, independently of this package's timestamped installation snapshots.
The global visual audit accepts all 56 distinct faces/compositions, and the parent-reviewed Asia CBD paper-only correction is installed. Live acceptance remains open.
