# Portal Raider runtime recovery handoff

Current disposition — superseded on 2026-09-06: fresh protected-source and actual-byte attack reimport review rejects the historical rigged candidate for severe torso/backpack folding, invalid aim and ground-contact error.
The recorded hashes and locator node are historical byte evidence, not proof of complete two-hand/stock contact or accepted role deformation.
The governing preservation-only manual repair and final selection are tracked in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_runtime_acceptance_2026-09-06.md`.


Owner: `/root/portal_runtime_resume`.

Date: 2026-09-05.

Status: the no-regeneration geometry, bind recovery, provider-action transfer, weapon locator, PDX export, and actual-byte reimport work is complete. Parent-owned runtime entity, action, particle/light, sound, counter-GFX integration, and live consumer validation remain open.

## Scope and preservation contract

The approved body-and-fused-gun geometry was preserved throughout this recovery. No replacement model, weapon, mesh regeneration, provider geometry substitution, gameplay file, entity file, sound definition, `.asset` file, or GUI file was edited by this handoff.

The deterministic job is `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider` with job id `portal_raider_meshy7_recovery`.

The protected approved source is `blender/checkpoints/accepted_static_geometry_pre_rig.blend`. The final runtime checkpoint is `blender/checkpoints/portal_raider_final_runtime_recovered.blend`, 30,801,420 bytes, SHA-256 `6E7D20F5B1999508DD015B73991392F6899925129FFEDFBF84B43FC0E0A01E9F`.

## Bind/rest-pose recovery result

The prior identity-scale mesh/armature mismatch was isolated from action content by comparing the same approved geometry and provider action across checkpoints. The old mesh world scale was 3.865936 against an identity armature and produced ribbon/stretch deformation. Scale-matched automatic bone heat removed the broad transform failure but retained a localized attack spike. The nearest-bone transfer retained a broad triangular stretch. The accepted pre-existing bone-distance transfer uses four nearest provider deform-bone segments with inverse-square distance weights and removes both failures without changing the geometry or source actions.

The accepted scene has 14,909 position-welded source vertices, 29,999 triangles, dimensions 3.911896944 m by 4.043290138 m by 7.351823807 m, zero non-manifold edges, zero degenerate faces, and zero zero-length normals. The body and fused gun remain one approved connected component.

The target has 24 bones in `Armature.001`, one `CHAOSX_RIG_TRANSFER` armature modifier, and matching mesh/armature world scale `0.03862994164228439` with the transfer data scale baked. The export coordinate conversion leaves armature object scale `[1,1,1]` and no negative-scale objects. Every deforming vertex has at most four influences and the final sanitized scene has exactly four influences per vertex, zero zero-weight vertices, and weight sums from `0.9999999553` to `1.0000000447`.

The full static/action diagnostic is `blender/reports/portal_raider_bind_rest_action_diagnostic.md`. It records the controlled transform, weight, modifier, rest-pose, and retarget comparisons and the adapter limitation that raw inverse-bind matrix dumps are not exposed.

## Provider lineage and action status

The provider source is `provider/downloads/portal_raider_attack_provider.fbx` and the downloaded provider action candidates under `provider/downloads/`. Every accepted action is retargeted from the verified Meshy action source, mechanically retimed from 30 FPS to 24 FPS, and contains no scale F-curves. No manual replacement, transform-only, static-pose alias, or procedural whole-rig motion was authored.

| Runtime action id | Meshy task | Provider role | Target range | Native action SHA-256 |
|---|---|---|---:|---|
| `portal_raider_idle` | `01a04312-c55a-77e4-8bf1-f7cbc34cf199` | `Idle` | 0–97 | `42518545473D0C1E1ED6E0C2C28A14A3CBE49BDA98FEDF33B118199E46344FF3` |
| `portal_raider_move` | `01a04313-6e62-7730-90a9-6fac50a4d676` | `walking_2_inplace` | 0–30 | `6EBC21246C992498CF5FF8EA6B03E8EC97821896490B10246C38D9FBE20E09A2` |
| `portal_raider_attack` | `01a04314-13fe-7842-9433-8290ec2849d9` | `Draw_and_Shoot_from_Back_1` | 0–189 | `79F3307834F6932AE87854877C37141107381D06D838C7CE758966CF59AA2BD7` |
| `portal_raider_defend` | `01a04315-229a-7aa2-901f-d4f433ff622d` | `Combat_Stance` | 0–41 | `DEA29B6F867A6AD8FC40918A61CE0350135AEC82B232A80AEBB56E3D783FF7C8` |
| `portal_raider_support_attack` | `01a04316-6088-756a-ab90-509d3d966f4e` | `Walk_Forward_While_Shooting` | 0–80 | `0FED5E9527263D0ADB09EC1E0623978415BE5D1AED8C00259FCAC896253B4EC2` |
| `portal_raider_retreat` | `01a04317-0bc8-75a8-b952-14f483ec2dac` | `Walk_Backward_with_Gun_inplace` | 0–25 | `7ACAFF6DD6DBEEB42C58601BEDC9BEC57B8A0A4BF3DA471664C442C5A767AD3F` |
| `portal_raider_portal_arrival` | `01a04318-32dd-7958-9e8a-72b17e6513bf` | `Jumping_Down` | 0–80 | `66A1ADA56E06F5BBD3C9D4473697452BD2C89FBBDBF06D735673BCA70A788BAF` |
| `portal_raider_wounded` | `01a04318-e8bd-7ff9-98fc-78bbdf4fb45d` | `Gunshot_Reaction` | 0–73 | `67C27179B4E6CA7DE59A50EEDE144E99C952ADF86A924D5E88BE14B432368053` |
| `portal_raider_death` | `01a04319-9f6c-7c24-992a-8036cd944145` | `Shot_and_Fall_Backward` | 0–85 | `029D71796BA84ECF46FCE9312B95F1F34281912DFB03645CA6DF81536A3D3F49` |

The individual source lineage records are `evidence/animation/*_provider_provenance_autoheat.json`. They use namespace-qualified imported action names and record `manual_or_procedural_replacement_authored:false`.

`attack` has a genuine draw, aim, discharge, recoil, and recovery sequence in phase samples 0, 40, 80, 100, 116, 136, 160, and 189. `support_attack` has a genuine moving-fire sequence with phase samples 0, 20, 40, 60, and 80. `death` has articulated collapse, impact, and settling evidence around frame 68. `defend` is a genuine provider `Combat_Stance` action and visibly supports a two-hand guard/aim state, but it has no separately verified discharge phase; it must not be described or wired as a firing action without a new accepted provider source.

## Weapon contact and muzzle locator

The registered locator is `portal_raider_muzzle_locator`, parented to `Armature.001/LeftHand` with bone parent type `BONE`. The exact vertex-ring selection, local transform, round-trip tolerance evidence, and frame error table are in `blender/reports/portal_raider_contact_locator_evidence.md`.

The locator errors are 0.015826 m at attack frame 1, 0.013172 m at attack frame 116, 0.030205 m at defend frame 20, and 0.047414 m at support-attack frame 40. The selected muzzle ring contains 72 vertices and is carried primarily by the support-hand side. The right-hand weighted region contains 1,440 vertices in the inspection volume and the nearest head-weighted right-hand sample is within 0.086 m of the right-hand area, with approximately 0.45 `RightHand` and 0.49 `RightForeArm` influence. Front and three-quarter critical previews show the fused firearm and both hands remaining in the weapon state.

The parent should use `portal_raider_muzzle_locator` for the muzzle particle/light node and synchronize `portal_raider_ray_attack` to attack frame 116 and support-attack frame 40, with recovery after those phases. The locator is not a substitute for gameplay hit detection.

## PDX export and actual-byte reimport

The mesh export is `exports/portal_raider.mesh`, 3,714,937 bytes, SHA-256 `9F66A01E6E0CE902D17A7A9E00A34DC97BBC1AD184FCE242CFFA9288D409D334`. The companion export text is `exports/portal_raider.txt`, 14,398,661 bytes, SHA-256 `86273A7F2A6E0D0A0A6EFED97EEB2EDEA152323B8F2855AE5B1FC81A849D887B`.

The nine action export hashes are recorded in `blender/reports/portal_raider_export_reimport_manifest.md`. Each `.anim` exported with no adapter warnings and each actual-byte reimport succeeded with action `io_pdx_rigAction`, mesh `output_unwrapped.001`, 41,902 seam-expanded vertices, 29,999 polygons, material retention, locator presence, animated bounds, and ground-contact samples. The position-welded topology remained 14,909 vertices and 29,999 triangles.

The attack proof was promoted through `promote_accepted_reimport` after relinking its reimported PDX images to job-contained provider PNGs. The promoted checkpoint is `blender/checkpoints/portal_raider_promoted_attack_reimport_packed2.blend`, 2,833,579 bytes, SHA-256 `2C119639E7D10F517D05160AA478C3774BB0EED77D428BCF994759CF61A975AA`. The promotion report is `blender/reports/promote_portal_raider_promoted_attack_reimport_packed2.json` and reports `status: pass`, `all_inputs_immutable:true`, `reopen_comparison.accepted:true`, and no mismatches.

The final locked adapter health probe used request `ccf0becfa8fe455a8c7da328d2e1bad0` and confirmed Blender 5.1.2, adapter 1.10.21, and loaded io_pdx_mesh. The final read-only scene inspection used request `ad3f9438efa742c2aa4f44bf2ef3f013`, confirmed the attack native action SHA above, 14,909 working vertices, 29,999 triangles, 24 bones, normalized four-influence weights, and the registered locator at attack frame 116.

## Materials, counters, and audio evidence

The final runtime retains the provider PBR maps and the accepted PDX material slot. The narrow adapter change that enabled reimport material relinking is in `.tools/3d_pipeline/adapter/blender_worker.py`: it only falls back to local image nodes/images when the reimported PDX material lacks the original shader tag, and it does not change geometry or action data. The source no longer emits the temporary generic diagnostic fields; the preserved `blender/reports/textures.json` investigation snapshot retains those fields as historical evidence.

The bespoke vanilla-green counter package is complete in the existing counter handoff `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/portal_raider_counter_art_handoff.md`. Parent-owned consumer tokens are `unit_portal_raider_icon` and `onmap_unit_portal_raider_icon`, with runtime DDS outputs `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`.

The sourced audio package and updated synchronization table are in `evidence/audio/audio_manifest.md`, with immutable licensing records in `evidence/audio/licensing/source_ledger.md`. The proposed parent-owned identifiers are `portal_raider_select`, `portal_raider_move_animation`, `portal_raider_idle_electrical`, `portal_raider_ray_attack`, `portal_raider_impact`, `portal_raider_portal_arrival`, and `portal_raider_death`, plus file stems listed in the manifest. Attack frame 116 and support-attack frame 40 are the measured firing phases. Defend has no verified discharge phase and should use the guard/aim electrical loop only unless the parent supplies an accepted provider action.

## Parent-owned runtime wiring

The proposed runtime identifiers are `portal_raider_mesh`, `portal_raider_entity`, `portal_raider_idle`, `portal_raider_move`, `portal_raider_attack`, `portal_raider_defend`, `portal_raider_support_attack`, `portal_raider_retreat`, `portal_raider_portal_arrival`, `portal_raider_wounded`, and `portal_raider_death`.

The parent must bind the final `.mesh`, nine `.anim` files, `portal_raider_muzzle_locator`, PDX material, entity scale 0.8, sourced audio identifiers, muzzle particle/light event, action events, and counter tokens in the parent-owned runtime surfaces. The parent must keep entity/action/sound/particle wiring changes outside this handoff's owned files and perform live consumer validation. This handoff does not claim in-game completion.

## Toolchain and cost evidence

The dependency lock records Blender 5.1.2 build `ec6e62d40fa9`, socket port 9876, `chaosx_blender_hoi4` adapter version `1.10.21`, and checksum-locked `io_pdx_mesh` 0.91.0 with manifest `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/blender_manifest.toml`. The pinned Meshy MCP server is `@meshy-ai/meshy-mcp-server` 0.4.0 at git `d8c77d1...`, using Meshy 7 task lineage already recorded in the provider evidence. The narrow relink/tolerance extension changed the locked worker source checksum to `DCFB0AD8AB3B1B1FDB37EA947AEA90864C4814317CBFF3EFAF2571AA653E0780`; the updated `dependencies.lock.json` SHA-256 is `57B2BF972D24850A7CCCD3DFDEA78194CDA8D6EB72EE1C1F94207555C5AB58E8`, and `python .tools/3d_pipeline/verify_environment.py` returned an empty findings list. No new provider call was made during this recovery and credits estimated/consumed for this recovery are 0/0.

## Files created or changed by this recovery

- `blender/reports/portal_raider_bind_rest_action_diagnostic.md`
- `blender/reports/portal_raider_contact_locator_evidence.md`
- `blender/reports/portal_raider_export_reimport_manifest.md`
- `evidence/audio/audio_manifest.md`
- `.tools/3d_pipeline/adapter/blender_worker.py`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/portal_raider_runtime_recovery_handoff_2026-09-05.md`

The nine provider lineage JSON files under `evidence/animation/` and the runtime checkpoints, exports, reimport proofs, previews, and validation JSON named above are preserved evidence from this recovery chain. No files were staged or committed.

## Remaining blocker and uncertainty

The model-side deformation, action, export, and actual-byte reimport gates are no longer blocked. The remaining acceptance boundary is parent-owned runtime wiring and live consumer validation. `defend` is accepted as a substantive provider combat stance with two-hand aim/guard evidence but not as a firing action. If the parent requires defend discharge specifically, the exact blocker is the absence of a verified provider discharge phase in `Combat_Stance`; a new provider action or explicit user-approved professional source is required, and no local replacement motion is permitted.
