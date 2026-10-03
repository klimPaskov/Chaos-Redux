# Cannibal Feast Cohort 3D package manifest

> Historical package record. The former blocked adapter status is superseded by the installed runtime package in `manifest.json` and `runtime/handoff.md`; retain this file and any provider or `provider/downloads` paths for `lineage_only` evidence only.

Status: **blocked at the live-adapter reload gate; no Blender descendant is approved**.

## Approved source and one-image input

- Selected modern fictional artwork: CMON HATE *Um'Gra Youngblood*, archived under `refs/source/recovery_v5/` as non-shipping `reference_only_user_authorized` evidence.
- Source image: `refs/source/recovery_v5/selected_umgra_youngblood.jpg`, SHA-256 `80D34425CCC5F21E63FA378F6129DE4ED502020F2E59F8A09C7D69883D37AC9C`.
- Sole Meshy input: `refs/original/meshy_input.png`, 1305×1205 RGBA, SHA-256 `F2E2B8705068932E771FC04D140E70D69ECBBF5DBAD3E6CDA8C86494A5F9AC21`.
- Built-in ImageGen performed faithful cleanup only. Two native-alpha attempts returned baked checkerboards, so the recorded fallback applied one FFmpeg neutral-checkerboard key and passed black-background silhouette review.

## Meshy 7 provider lineage

- Official route: `@meshy-ai/meshy-mcp-server` 0.4.0, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, exact model `meshy-7`.
- Generation: `01a033c5-1c4c-7dd8-8c0c-ad365327dc1d`, 30 credits; selected GLB SHA-256 `41D874EDCD71C5F45F99E41AA7CC343A6CE58418BA410050F6ED3772C8A476C2`.
- Provider remesh: `01a033d0-7114-7171-9b10-4236e971a992`, 5 credits.
- Provider rig: `01a033ee-4dfe-7e18-8137-1293d3106cb8`, 5 credits; `provider/downloads/recovery_v6_rigged.glb`, SHA-256 `B0ECC0CEE9F290C14123D9C17F143ADF0EDCD042BE623C57799BC093E6101B44`.
- All eight distinct `meshy_animate` tasks succeeded and their FBX/GLB files, provider task receipts, action names, and hashes are preserved under `provider/downloads/` and `provider/tasks/`.
- Animation tasks: idle `01a033fd-23d4-7b88-902f-647db463c02c`; move `01a033fd-3438-7b8a-b04f-bba4caa41bf1`; attack `01a033fd-47b1-7a91-85b8-73c2caae75c7`; defend `01a033fd-6132-7357-8d0d-71aab9bb0bfa`; support attack `01a033fd-79d0-7247-a1e7-f873b97e6d9d`; retreat `01a033fd-91da-7bb2-84e7-c01d16ec9bc0`; training `01a033fd-a579-7bb6-8bba-f94187ab3b12`; death `01a033fd-b49b-7bbe-9dde-28020fae3287`.
- Animation spend: 24 credits. Recovery-v6 total: 64 credits.

## Calibration and failed Blender gate

- Vanilla source: `gfx/models/units/western_european_infantry.mesh`, object `polySurface106`; entity `gfx/entities/units_infantry.asset#infantry_rifle_entity`.
- Contract: source height `7.351824797689915`, entity scale `0.8`, effective runtime height `5.881459838151932`, forward `-Y`, up `+Z`, collision excluded, 30,000-triangle ceiling.
- The last live route reported adapter 1.10.3, Blender 5.1.2 build `ec6e62d40fa9`, and io_pdx_mesh 0.91.0.
- Prepare request `bd584690ac5646869c8c42745ec3a7af` failed closed after reopening `blender/checkpoints/05_pre_export.blend`: persisted height `7.343611240386963`, target `7.351824797689915`, delta `-0.008213557302951813`.
- Failed checkpoint SHA-256: `77FE30D4380571D7DB6713851609FAFFEEAA1E7601A62F5B456EEC871D7646EC`.
- Failure log: `logs/adapter/bd584690ac5646869c8c42745ec3a7af.result.json`, SHA-256 `362AD9D011C3A342D80BFE5474C9D70305BF81EBE12829EED778C91288626A7A`.
- Committed authoritative adapter 1.10.7 exists at revision `a3e0a1497`, but this task's live Blender MCP still reports 1.10.3. The parent ordered a process reload stop. No substitute route, further provider spend, retarget, export, or reimport is permitted until that gate is cleared.

## Audio and counters

- Seven sourced roles are complete: selection, idle, movement, attack, impact, training, and death. Exact source pages, creators, licenses, original hashes, mechanical transformations, derived hashes, and proposed synchronization live in `evidence/audio_sources/source_provenance.md` and `ffprobe_and_hash_receipt.json`.
- Training uses CC0 `swish-7.wav` by artisticdude. Source SHA-256 `E6DE737A34DE16AFED094D6170D7679149022F149E0A8356D2F029B0E8F4A4D7`; derived 44.1 kHz mono PCM SHA-256 `EFBE3B475E633A9F11D6C3BC97BA0432407D411EFA7E36071FB07FEDFDD4B839`.
- Bespoke vanilla-green large/on-map/texticon counters are complete and parent-wired in commit `b03c41aa3`. This worker did not recreate or edit them.

## Remaining work

- Reload the committed adapter process and prove exact version/checksum/environment state.
- Rebuild from immutable rigged geometry and action artifacts; prove height through save/reopen/export/reimport, bounded dimensions, intact spear/hook/chain, top-four normalized weights, packed PDX materials, and genuine motion for all eight roles.
- Export and reimport the final `.mesh` and eight `.anim` files, render action evidence, and finalize action/audio synchronization.
- Parent retains runtime copies, entity/asset/sound wiring, and live consumer validation.

No runtime or in-game completion is claimed.
