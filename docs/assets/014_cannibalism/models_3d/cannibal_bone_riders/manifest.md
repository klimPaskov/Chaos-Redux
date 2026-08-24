# `cannibal_bone_riders` model package manifest

Package status: `blocked_adapter_reload_pending_professional_sources_selected`. Meshy 7 geometry, local geometry QA, previews, source provenance, all required sourced audio roles, and the existing bespoke counter audit are complete. Parent-approved CC0 horse actions and conditionally approved Meshy rider-action candidates now provide a source-compliant separate horse/rider route, but no runtime skeletal package exists until the repaired structured adapter surface is reloaded and verified.

The non-shipping source is Tatyana Kupriyanova / @CgSister's modern fictional *Horned Warrior on Pale Steed*, archived at `refs/source/recovery_v7/candidates/bone_tatyana_horned_steed.jpg`, SHA-256 `261B5442B11853971CA6B31265167EABA4D73E69AA7A116E78A3D3CD82F114D8`, source page `https://twoucan.com/profile/CgSister`. The page grants no public reuse license and contains no explicit NoAI/no-derivatives prohibition. The user explicitly authorized reference-only use of this exact artwork and one narrow native ImageGen adaptation.

The sole provider input is `refs/original/meshy_input.png`, SHA-256 `16C02D09E025CF3548BAF7BA390B37656448CF3A04D0A85689B350870C2D4E89`, 1136x1385 RGBA. It preserves the living pale horse, living painted rider, skull mask, clothing, palette, dynamic silhouette, and anatomy; removes both spears; adds a loaded leather sling, stone pouch, and skull/rib/long-bone barding; and contains genuine transparent alpha. The first native ImageGen output, SHA-256 `0D795DDAAFE2548C8AED805E4BCE4C3D461F7923B06CA21E56AD8E788363CD2F`, was rejected for a baked checkerboard. A targeted background-only repair produced the approved image; alpha minimum is 0 and maximum 255. The parent approved the exact final checksum on 2026-08-24. Complete prompt, comparison, lineage, and approval evidence is in `refs/original/input_manifest.json`.

Meshy 7 task `01a03404-f74d-7d5b-876d-5f426afe11f6` succeeded for 30 credits. Downloaded generation hashes are GLB `EA2E4E40B88BD67DE45AC0964305786602499902CEC584A12DE666794AD38E4E` and FBX `66A8EB69F7D1995B52141400B79D9C4F89FC97B85BFF140FED6F64ADC196C79D`. Adapter prepare request `a4ee1609baad4f6c80e3d6dd56eb6df1` created protected checkpoints. Repair welded 75,785 vertices and reduced boundary edges from 147,990 to zero. A single bounded reduction produced exactly 90,000 triangles and 44,670 vertices. Final checks found zero non-manifold edges, loose edges, degenerates, or negative scales, with UVMap intact. Dimensions are 16.0122756958 x 14.3398075104 x 20.4160480499 source units and ground contact is Z 0.0036. The geometry checkpoint SHA-256 is `0DC4A64B675735B45126CA93953CD81853E4389E564DEA808339D6A836EE3617`; report SHA-256 is `9F9428D01AEA3436B571A20D692FE433D83146340F6911324B447287CD29E990`.

Seven Blender previews pass the visual gate: one living horse, one living rider, readable sling stone and pouch, strong bone barding, complete mounted silhouette, and no forbidden weapon, modern equipment, undead anatomy, or prohibited motif. Provider PBR maps are preserved. Final HOI4 DDS packing was not performed because the skeleton change gate failed before export approval.

Installed precedents are `cavalry_horse.mesh`, `cavalry_frame.mesh`, `infantry.gfx`, `units_cavalry.asset`, and `animation.asset`. The horse measures 6.5955228806 x 20.3361954689 x 15.6460447654 source units at pdxmesh scale 0.45. The separate attached-entity scale precedent is 0.65 and was not baked a second time.

The initial rig request was rejected before billing because Meshy saw the original 1.99M-face task. Provider remesh task `01a03418-57e3-7399-bf55-2d769bedabee` succeeded at 90,000 triangles for 5 credits. Remesh hashes are GLB `D105CAC2E1D1CC0C37D420FB6E54776D0F15B68126015A3AB734F8900497C348` and FBX `90ED7511BEAC37D76A1032B2E673D27F80A224061C701F4B9B183C25EF95B743`. The second rig attempt failed prebilling with HTTP 422 pose-estimation failure. Total consumed credits are 35. All eight required roles are blocked. No local replacement motion was authored, and no `.mesh`, `.anim`, DDS model texture, export, or reimport is claimed.

Six licensed or public-domain audio sources and PCM S16LE 44100 Hz mono derivatives exist under `audio/`, including a public-domain stone-impact one-shot derived from stones tapped together. The bespoke counter package was reaudited: large 152x42, small 60x12, and texticon 60x12 all pass exact decoded roundtrip. Parent-owned runtime/entity/GFX/sound wiring and live in-game validation remain pending.

The v9 live route audit verified official Meshy MCP 0.4.0, exact `meshy-7`, balance 1320, adapter 1.10.0, Blender 5.1.2, io_pdx_mesh 0.91.0, and the listening Blender bridge. Meshy's current official rigging contract supports standard humanoid bipeds and explicitly excludes nonhumanoid assets; `meshy_animate` requires a successful Meshy rig task. A separated rider could be rigged as a biped, but Meshy exposes no quadruped horse rig or animation source, so separation cannot yield compliant mounted motion. No additional paid attempt was made against a documented unsupported input family.

Detailed evidence is in `evidence/final_v9_dependency_and_capability_report.md`, `evidence/action_manifest.md`, `audio/audio_manifest.md`, `job.yaml`, and `runtime/handoff.md`.

## Professional-source recovery

Mesh2Motion `mesh2motion-assets` commit `6bab14fa197957bf7851477cad0c372960a48824` is the approved CC0-1.0 horse motion source.
Exact source pages, LICENSE bytes, per-action Blender sources, the consolidated 15-action GLB, and hashes are archived in `provider/external_animation/mesh2motion_horse/`.
The selected horse clips are `Idle`, `Run`, `Rear`, `Kick`, `Head_But`, `Trot`, `Eating`, and `Death`; phase evidence and the 56-bone/weight audit are in `evidence/mesh2motion_horse_action_audit.md`.

The official Meshy action library, rejected combat candidates, phase evidence, and the conditionally approved eight-action rider plan are archived under `provider/meshy_rider_action_research/` and summarized in `evidence/meshy_rider_action_research.md`.
No new Meshy action call has been made; the planned rider tranche remains 24 credits against the latest verified balance of 587.

Installed vanilla `units_cavalry.asset` proves the required architecture: a frame entity, a horse entity, and a distinct rider entity attached at `Saddle_Node`.
The exact installed file and line-specific analysis are archived in `evidence/vanilla/units_cavalry.asset` and `evidence/vanilla_cavalry_entity_architecture.md`.
Bone Riders will therefore preserve separate bespoke horse and rider meshes and actions; it will not merge their skeletal actions.

Registration recovery commit `7e3af24ac` adds the required structured operation exposure but requires a fresh Codex/MCP process.
The current process remains paused, and an unrelated uncommitted adapter/lock 1.10.4 state is not authoritative.
No final rig, weights, Saddle_Node, `.mesh`, `.anim`, DDS model textures, exports, reimports, or compound synchronization previews are claimed.
