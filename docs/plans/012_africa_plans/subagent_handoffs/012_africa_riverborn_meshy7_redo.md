# Event 012 Riverborn Meshy 7 recovery handoff

Status: `blocked_generation_recovery_4_rejected_attachment_and_topology_insufficient_balance`.

## Outcome

The parent-authorized materially different Meshy 7 recovery was attempted and archived. Provider task `01a04331-33b4-7ea1-8bab-d855ed2d8765` succeeded, but the package candidate is rejected: the spear and shield are separate floating objects adjacent to open hands, not a spear held in a normal grip and a shield borne on the other arm. The working mesh also retains 8 loose boundary edges across 2 components after bounded repair. Blender may not attach or remodel the props, rejected geometry may not receive rig/animation spend, and no accepted model/action/export package exists.

The remaining live Meshy balance was 13 credits after download. A new textured Meshy 7 generation is estimated at 30 credits, so automatic generation recovery is blocked for insufficient balance.

## Gates and dependencies

- `MESHY_API_KEY` hard gate: passed without exposing the secret.
- Exact approved input: `docs/assets/012_africa/models_3d/riverborn/refs/original/meshy_input.png`, SHA-256 `A1FA4DAF0B7DBE72B3284D2A878524F6FD322F56B708BC5DA5937312B724DB59`; predecessor `FB44F05C9F19740802AB446B851678766B64C6D9DB8BCB9902CEC65C2ADF4521`.
- Source mode: `reference_only_user_authorized`; the official Grinding Gear Games *Kiloava Chieftain Concept Art* page/fingerprint, rights decision, ImageGen prompt, source-to-refinement comparison, alpha fallback, approval, and non-shipping status remain in `refs/source/`, `refs/briefs/`, `refs/derived/`, and `manifest.md`.
- Provider route: official `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK `1.29.0`, compatibility revision `meshy-7-v5`, exact generation identifier `meshy-7`.
- Live image schema: one exclusive image input; exact `meshy-7`; T/A pose, triangle topology, enhancement, PBR, remesh, texture, and output-format arguments; no geometry prompt. The request used only `file_path` and kept multiview thumbnails false.
- Lock hashes: dependencies `C27768297FB7AD5ACC9C555E7C83DC77856908E2C628BF16D9A420095C64266A`; schema `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config `4BC97CA0B07580F5AA04B49E7B9FBD1C07EC88DF5C4D56CD3BA8846E630117AB`.
- Blender `5.1.2`, build `ec6e62d40fa9`; adapter `chaosx_blender_hoi4` `1.10.14`; health request `c67476611214409aa2bdb138c9297314`; bridge `127.0.0.1:9876` listening.
- `io_pdx_mesh` `0.91.0`, archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; installed manifest and mesh/anim operators passed health inspection.

## Provider lineage, cost, and downloads

Recovery 4 differed materially from recovery 3: T-pose instead of A-pose, image enhancement enabled, and native high-density generation without integrated remesh or provider target-polycount reduction. It used exact `meshy-7`, standard model, triangle topology, textured PBR, lighting removal, and GLB/FBX outputs. Request and redacted response evidence is in `provider/requests/generation_recovery_4.json`, `provider/responses/`, and `provider/tasks/generation_recovery_4.json`.

- Task: `01a04331-33b4-7ea1-8bab-d855ed2d8765`; provider `SUCCEEDED`; package `rejected`.
- Estimated/reported Riverborn cost: 30/30 credits.
- Balance before: 73; after completion/download: 13; raw shared-account delta: 60; unattributed concurrent delta: 30.
- GLB: `provider/downloads/generation_recovery_4/riverborn_generation_recovery_4.glb`, 84,030,856 bytes, SHA-256 `B8FA48A94240BC35A19529142B357FEA876944F7A95470FA88960032DC510C56`.
- FBX: `provider/downloads/generation_recovery_4/riverborn_generation_recovery_4.fbx`, 87,015,548 bytes, SHA-256 `BC0FF8F4B3C0BAE093CE8671669E9967AF031A1B98983FCA27E57DADDE6F7339`.
- Texture hashes: base color `23BB7752EA0141368E0C5BDE84F50E0FF61E37AC7263579B8B72B746DBCAA30E`; metallic `6F960EEEFA07F9886973AAA32E41A0C1F761458E8A61764E966B119CEF5F6BBC`; roughness `4A8A20AEF666660F61DD9F06A2249DDC10A7F5757B9AAD80B0D5363EF51A972E`; normal `6ABDAF17EF0E9ED328ABC40DCEEC0C35750A4B4398ABF4083CD10A1678CDFA5F`.
- Full download ledger: `provider/downloads/generation_recovery_4/download_manifest.json`; signed URLs were not retained.

Earlier rejected Meshy 7 task ids remain `01a033eb-7cad-7cd5-adfc-76f4b97dbe59`, `01a03d69-fcfd-7d8d-8d8c-c267c5c2990d`, and `01a03d82-1562-72f3-99ea-68e83fc2cebf`. Legacy Meshy 6 task `019fd806-2e78-78aa-8876-fca8862d729d` and all locally authored actions remain historical non-promotable evidence.

## Blender geometry, material, and scale QA

Adapter request `390fe96601c84f40b9d3c2923796878f` protected the source, imported `refs/vanilla/asian_infantry.mesh`, measured vanilla height `7.516802847`, and calibrated the working duplicate to `9.396005630` at entity scale `1.0` with ground contact `0.0`. The locked crosswalk remains source height `7.516803`, target/effective runtime height `9.396004`, entity scale once.

The source contained 1,937,712 triangles and 1,069,614 vertices. Bounded repair welded 101,132 vertices and controlled reduction produced exactly 25,000 triangles and 12,130 vertices. Final QA reports zero degenerates, non-manifold edges, negative-scale objects, and zero-length normals, but 8 loose boundary edges across 2 closed components. The cap attempt rolled back rather than introduce non-manifold geometry.

Seven views prove the attachment failure. Rejection: `blender/reports/generation_recovery_4_rejection.md`. Prepare report: `blender/reports/chaosx_riverborn_recovery_4_prepare.json`, SHA-256 `62901E2C238E20F960AFF73E80B90C4B5A24CE484D8D4787C6E4199C46199603`. Protected source blend SHA-256 `9706012DE08B49AEBA9DFBA290D6F88D7AD7D8C4FDDBE58B7F5C0A9E47DCBFC1`; imported checkpoint `36B8305EFF9E093D55DF26B4130038CCA72F118E5BD131A615B49D4DBCEB837C`; geometry checkpoint `48692C5D6674D409B42E82548884083143386134C4650E6643567D944963237D`; pre-export checkpoint `C35707C86D3A764F2582F9212CB56DA5C642412B2BACA3AD92ECB5C62E13BD54`.

Provider PBR maps were retained only. PDX packed-material conversion was skipped because geometry failed; raw roughness was not promoted as PDX specular.

## Rig, actions, export, and firearm audit

Provider rig spend: 0. Animation spend: 0. No local final rig/actions were authored. All required 30 FPS roles are `blocked`: `chaosx_riverborn_idle`, `chaosx_riverborn_move`, `chaosx_riverborn_attack`, `chaosx_riverborn_water_transition`, and `chaosx_riverborn_death`. No FPS/frame/loop/root/deformation/contact preview, `.anim`, binding, or reimport proof exists for this candidate.

No `.mesh` or `.anim` export/reimport occurred. Existing exports are legacy and must not be synchronized. Source-to-runtime model/action hashes: none.

The unit is `non_firing`. Zero firearm firing states, muzzle/discharge effects, firearm lights, and firearm sounds are required or produced. The spear role is melee.

## Sound package

Immutable public-domain originals remain `audio/source/flowing_water.ogg` (Fg2, public domain, SHA-256 `6CAB6C85A0B9159AA9E98F30BEF16E5F8976A3154D8CEC4E00925AAC21289F0B`) and `audio/source/ducks_landing_water.ogg` (U.S. Fish and Wildlife Service, U.S. federal public domain, SHA-256 `C95C1641721CB80645D58FB05CEED871DCB74D1A62AD14E5D26F3B73F7BFA816`). URLs/terms are in `audio/evidence/source_research.md`.

Six derivatives pass signed 16-bit PCM, 44.1 kHz, mono ffprobe checks in `audio/evidence/pcm16_ffprobe.json`: select `3092641A7A0723C20EB5052F391C74FB3E5AD20E7AFC17FD79AD219F2C722E60`, idle `A3D0789057291FF1D0340C4978F5ADFF4D2A888BF69B3A7A3DCEBAD8AE21637C`, move `F78159604C6188C6C63871818C19CA497E36A7080FC3F4E1F0E1CF29ED27906C`, water impact `4354E642A3C640564F0845B6C49B8C6DA2E029F15B625F132A5F92EF083FE582`, transition `169E6122B82187B052718E115B66AFA8A71A5FD1C8A3060D36227FC7D6D4FC3A`, death `84E546C4B2E22465E8F3D9C4D08A34AEE4B66B93E71238F666D7CCB92412C086`.

Sound status is `blocked`: synchronization is provisional; water landing covers impact only, not a spear strike/air role; and the real selection/acknowledgement consumer is unproved. Formation creation or entity entry is not a selection substitute. No audio runtime copy/source-to-runtime hash was selected.

## Counter package

Status: `needs_user_review`. Existing bespoke bytes/evidence were preserved; no new 2D art was authored.

- Tokens: `unit_riverborn_icon`, `onmap_unit_riverborn_icon`; large `152x42` two `76x42` frames; map `60x12` two `30x12` frames.
- Definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, `GFX_unit_infantry_icon_medium` and `_white`, both two frames.
- Installed DDS hashes: large `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`; map `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`.
- Skill-local families: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.../units/land/map_counters/`, including named references/contact sheets.
- Palette: dominant RGB `73,106,73`, range `20,34,21` through `154,175,147`; map family uses inspected neutral grayscale.
- Outputs: `counters/dds/unit_riverborn_icon.dds` SHA-256 `CD28C94D31E7A8936F546AA1B06828CBB58A8AF2170E1A0E8FF1CDE4334E2A83`; `counters/dds/onmap_unit_riverborn_icon.dds` SHA-256 `E104BFE350AA75828CD8981E837BAAB563DDAB21ED5E8CC97AF730DA01783BAF`.
- Exact header/frame/alpha/bounds/round-trip and artist handoff: `counters/manifest.json`, `counters/contact_sheet.png`, `counters/gfx_handoff.md`. Parent must visually accept before promotion.

## Requirement status and parent work

| Requirement | Status | Evidence / blocker |
|---|---|---|
| Approved exact one-image reference/provenance | complete | exact hash and source/refinement package retained |
| Meshy 7 geometry | blocked | floating prop attachment failure and 8 loose edges |
| PDX materials | blocked | geometry rejected; maps retained only |
| Rig and weights | blocked | geometry rejected; no spend |
| Five skeletal actions | blocked | no accepted rig/action source; no aliases/local replacements |
| `.mesh`/`.anim` export/reimport | blocked | no accepted model/actions |
| Sourced audio | blocked | spear cue/real selection consumer missing; sync provisional |
| Bespoke counters | needs_user_review | exact staged package exists; parent contact-sheet review pending |
| Runtime synchronization/wiring | blocked, parent-owned | no selected source hashes; rejected/legacy outputs forbidden |
| In-game validation | blocked, parent-owned | no runtime candidate; no completion claim |

Parent work: carry the insufficient-credit blocker; decide whether/when enough balance exists for another materially different Meshy 7 attempt; keep model/entity readiness false; review counter contact sheet; source a licensed spear cue; prove a real selection/acknowledgement consumer; and perform final `.asset`/entity/GFX/gameplay/sound/localisation/runtime wiring/live validation only after a future complete package exists.

Meaningful validation performed: exact input/lock hashes; live balance/task reconciliation; bridge socket/adapter health; provider download checksums; seven-view identity review; vanilla height calibration; topology/triangle QA; all-WAV ffprobe; preservation review of counter definition/DDS/reference/roundtrip evidence.

Meaningful validation skipped: rig/weights/deformation; action semantics/contacts/root/FPS; PDX packing; export/reimport; action/audio sync; counter parent visual approval; runtime consumer and in-game validation. Each was skipped because geometry failed or belongs to the parent boundary.

Simplifications or fallbacks: no model, rig, animation, audio-source, or runtime fallback was used. The already documented `rembg 2.0.61` alpha fallback belongs to the approved reference lineage. No missing requirement is represented as complete.
