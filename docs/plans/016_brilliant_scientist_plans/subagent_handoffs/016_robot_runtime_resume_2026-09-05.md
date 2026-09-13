# Autonomous Robot Runtime Resume Handoff

Status: `blocked_capability_review` as of 2026-09-05.

This handoff supersedes the robot-specific runtime claims in `016_final_robot_runtime_recovery_2026-09-02.md` and `autonomous_robot_3d_model_handoff.md` for the current adapter and locator/export evidence.

The preserved autonomous robot body and both integrated arm-mounted belt-fed machine guns were kept intact, and no substitute model, substitute weapon, geometry regeneration, provider recovery, gameplay edit, or commit was performed in this pass.

## Scope and lineage

The deterministic job root is `docs/assets/shared_robot_system/models_3d/autonomous_robot` for job id `autonomous_robot` owned by `shared_robot_system`.

The immutable working source is `blender/checkpoints/manual_recovery_2026_08_27.blend` with SHA-256 `FEB2BB03E2DE7EAF84547C0864500C821A7DDD05A0BEE1958948C969F2BDB25D` and 1,876,184 bytes.

The approved single Meshy input is `refs/original/meshy_input.png` with SHA-256 `671E5197C04D709947A8B73B43717E74DC5F394166437BFF0CE0D3C1CB4905DC`, one provider input, and project-authorized built-in ImageGen provenance recorded in `refs/original/input_manifest.json`.

The historical provider lineage in `manifest.json` is Meshy 6 generation task `01a001f1-9a6f-73c0-a45a-88082c95421c`, remesh task `01a00422-4450-762d-8fbd-db589e6e9bf9`, rig task `01a0043b-dc34-7795-a542-7d9657a3820e`, and 63 historical credits consumed with recorded balance 156.

The current lock requires exact Meshy 7, so the historical Meshy 6 lineage is not silently promoted and no new provider call was made in this pass.

Estimated and consumed credits for this pass are both zero because only locked Blender inspection, locator recovery, export, and reimport evidence were run.

## Dependency and route evidence

The dependency lock is `.tools/3d_pipeline/config/dependencies.lock.json` with SHA-256 `B68663B74AA51CD3D191AA98C0EB0BD2E7C3612E238B87D7867C923093C1EA92`.

The Meshy schema lock is `.tools/3d_pipeline/config/meshy_tool_schema.lock.json` with SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.

The locked official route is `@meshy-ai/meshy-mcp-server` 0.4.0 at git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, using the repository wrapper and live schema revision `meshy-7-compat-live-declaration-2026-08-21`.

The schema exposes `meshy_check_balance`, `meshy_image_to_3d`, `meshy_get_task_status`, `meshy_download_model`, `meshy_remesh`, `meshy_rig`, `meshy_convert`, and `meshy_animate`, with exact generation model `meshy-7` and no multi-view provider input.

The repository-owned adapter config is `.tools/3d_pipeline/config/blender_hoi4_adapter.json` with SHA-256 `C68298F02A04084F9A0EF48196BE7AE4806EE746D9C7A290A3C27F3D202EA6FC`.

The verified adapter is `chaosx_blender_hoi4` 1.10.21 with source hashes `chaosx_blender_hoi4_mcp.py` `B72B323CC9B0C9D70597F662F951D1EC0B18F566BB9CFC3854E321D6D03849A4`, `blender_worker.py` `0C59C4E1D6A241003F59458F5DD130C05670633D304A05AB017E554410216FD6`, `normalization_convergence.py` `91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`, and `blender_client.py` `B2FE78FA84E297C6A913F4E2E17E2E3C1620F417306E33F3066B6F9162241A50`.

Blender health request `083c86b7b3c84b589d7d9b8a3890b203` verified Blender 5.1.2 build `ec6e62d40fa9`, the loaded `io_pdx_mesh` extension, adapter id and version, and worker log `logs/adapter/083c86b7b3c84b589d7d9b8a3890b203.result.json`.

The `io_pdx_mesh` lock is version 0.91.0 with locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2` and installed manifest SHA-256 `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC`.

The required Blender MCP socket probe to `127.0.0.1:9876` succeeded independently of process presence.

## Geometry, materials, rig, and scale

The preserved mesh has 29,971 triangles, 15,123 source vertices, one UV layer, 1,973 intentional open panel/component edges, zero non-manifold edges, zero degenerate faces, zero negative-scale objects, and zero zero-length normals.

The mesh dimensions are approximately `[6.4485998, 4.6615820, 7.3567042]`, with forward `-Y`, up `+Z`, and feet at `Z=0` within the recorded diagnostic tolerance.

The calibrated vanilla source `gfx/models/units/western_european_infantry.mesh` measures approximately 7.3518242835, while the preserved robot source height is 7.3518247604 before the entity scale of 0.8 and effective runtime height is approximately 5.8814598083.

The integrated twin arm-mounted guns, belts, boxes, and visible barrel ends remain part of the single `char1.003` mesh and were not separated, removed, or replaced.

The preserved material is `Material_1` with diffuse, normal, and specular PBR links, and the exported material is `PDXmat_char1.003`.

The 24-bone `autonomous_robot_rig` has four normalized influences per deforming vertex, zero zero-weight vertices, no non-bone groups, no negative scales, and no scale F-curves.

The legacy runtime texture hashes remain diffuse `48F9E5488DEB14CD2D058C907A9F00BD8C4A4D09C887731334D7CE875B117922`, normal `DA1253F4DEF8CAA054D2FC84F4478F8B77D432EFF94421C919E72D90ED72E65A`, and specular `CA4CFD87DE234B63480BA32D07C21D45D6D2A1214EA27CA84B78EBB79FAFEF1F`.

## Stable muzzle locator recovery

The source inspection request `8fbc26d540de46e8ac6b77100ae4b0b4` found the existing `muzzle` and `muzzle_left` empties parented to `RightHand` and `LeftHand`, but both were unregistered, ownerless, and could not be safely adopted.

The exact same-name probe request `cde6c3720b07442fbf47cbb9203649bd` failed before mutation with `ValueError: Locator name collision or ownership/registration mismatch.`

A job-owned export-safe locator named `muzzle_export` was authored on `RightHand` by request `b5953b30fa084ecab95281716c5033b4` with maximum bone-local matrix error `9.834766387939453e-7`, source checkpoint SHA `FEB2BB03E2DE7EAF84547C0864500C821A7DDD05A0B0EE1958948C969F2BDB25D`, and checkpoint `blender/checkpoints/manual_recovery_2026_08_27_muzzle_export_probe_2026_09_04.blend` SHA-256 `17AE8A7E357B0B78961C2AE844D8F34848E8BCC016ACA9F533BE71BDF28A1D2C`.

A second job-owned export-safe locator named `muzzle_left_export` was authored on `LeftHand` by request `fdc5477d879f416aa4254e6bb214cedd` with maximum bone-local matrix error `9.5367431640625e-7`, and the combined checkpoint `blender/checkpoints/manual_recovery_2026_08_27_muzzle_export_probe_2026_09_04_both.blend` has SHA-256 `2ECDC375C90F4C3784B2BAB215C7D60A22A26EF392479A9EE41982F70828757C` and 1,876,510 bytes.

Both locator calls verified all eight existing action names unchanged.

The original unregistered names remain untouched, and runtime wiring must use `muzzle_export` and `muzzle_left_export` or a separately verified parent-owned alias rather than claiming the old names were adopted.

## Exact mesh export and actual-byte reimport

The locked `export_mesh` request `4a35f3fcdc594900937ec433ec0c36b3` produced `export/manual_recovery_2026_08_27_locator_registered.mesh` with 2,596,286 bytes and SHA-256 `DC081A642954D203BCE7E7BA1B5F5465BB38D398D2A64C72F912A657891DCF57`.

The companion mesh text dump is `export/manual_recovery_2026_08_27_locator_registered.txt` with SHA-256 `FB27DF2CEDD208F4B786BCD911F61EAD9ABE517817D80C0A41A66F284634897C`.

The exported mesh selected `char1.003`, `muzzle_export`, and `muzzle_left_export`, retained 29,971 triangles, zero non-manifold edges, zero degenerate faces, 1,973 recorded open panel edges, and emitted no exporter warnings.

The exported checkpoint `blender/checkpoints/06_exported.blend` is 1,876,489 bytes with SHA-256 `9EC347D6DD6994DF008C87B326C95C5100AC6728A970297E0AA056091743048C`.

The eight exact exported animation files were produced through `io_pdx_mesh` at 30 FPS with no exporter warnings and the locked policy `normalize_exported_bone_scales_and_preserve_mesh_unit_translations`.

| Role | Exported `.anim` bytes and SHA-256 | FPS and range | Export request | Reimport proof and validation SHA-256 |
| --- | --- | --- | --- | --- |
| idle | 10,307; `C493E81B2240271B339C0B4DF74E1AC9A44AFE4292FCBEF6A7FAEFEC73102CA2` | 30; 0-48 | `12d3eba85c5647809c4f01530ade96f5` | `reimport_manual_recovery_2026_08_27_locator_registered_idle.blend` SHA `03670A8F4568C8BBCF46404AFA56C6FEF644315B3727E0774B02AC56728CA7B6`; validation `reimport_manual_recovery_2026_08_27_locator_registered_idle.json` SHA `F99D200928A8EC1791673C17937A9846D358EC4409D526F95EFAF1B69B4A2AD9` |
| move | 27,195; `703556A40151EF25469F7AB758B42DC49E50514B0E8C4CDAF2DF091D64DB584C` | 30; 0-48 | `5e06914471d14801afb761994fb3b902` | `reimport_manual_recovery_2026_08_27_locator_registered_move.blend` SHA `36B534851E856ED55B7BE16B95EFE187E2B44FAFC0F412900422BE21B74DD6C2`; validation `reimport_manual_recovery_2026_08_27_locator_registered_move.json` SHA `EBA1C365D6DC3987148979876F8162A75055854D7C2795C2E6AF68DEB1647D95` |
| attack | 10,307; `169E21176F3B98E8D56EA3F371E3B5643543833869C66A6B39616CF1869502C8` | 30; 0-48 | `302400f425e643fdabbe43da6e010225` | `reimport_manual_recovery_2026_08_27_locator_registered_attack.blend` SHA `C75A5F62EB80720B41EFC3470014F0BD971B4C7FBC49F2E9E653F02C261AD964`; validation `reimport_manual_recovery_2026_08_27_locator_registered_attack.json` SHA `1252C4C9A622C855398F2716D87DDFCDA782A500E59F5A951DE8CBF4CFFD4590` |
| defend | 10,307; `C493E81B2240271B339C0B4DF74E1AC9A44AFE4292FCBEF6A7FAEFEC73102CA2` | 30; 0-48 | `de830b0514a94135adb103adca8b0269` | `reimport_manual_recovery_2026_08_27_locator_registered_defend.blend` SHA `A54EDBBECF9098AF56668B916BDA715162D4D5382FD6E7AE82CEC807BE4249D3`; validation `reimport_manual_recovery_2026_08_27_locator_registered_defend.json` SHA `BB3F8ABB8CB6098701A6D39A50911CF5600E0712D842EA1356C2AC4007F18E17` |
| support_attack | 8,291; `4C0B0B04AFBE16D8E2A9CB7CE0212D8FA4B72C89807B9BED54C30577E11396DE` | 30; 0-36 | `18fa3bee4b6444e0af7ced2e8de3d522` | `reimport_loc_sa.blend` SHA `96022C8FC6E2E92447F33E370727AA1CB6488D8E4A2EF9D9DFB2AB5AEB00A9A7`; validation `reimport_loc_sa.json` SHA `34E3822946B88E25E5F04C6B0FB597747E94B06CF4DDF5A3AE6B6125F5BC0AB6` |
| retreat | 10,307; `8FB492C36BB61AD28F6B985E11CC549B3D294E8009B9B60AC4328EDA3A0B00AF` | 30; 0-48 | `17b55a748f8d43d5bba1b56766995f07` | `reimport_loc_ret.blend` SHA `38AF3D7591AF7FFB24A2CDE914E3AE140F03A8D72E2628CF7B4B0F7D8D42C342`; validation `reimport_loc_ret.json` SHA `354C9772FB380E547122E2D4D9B537ADADFBFA84B9A17FB307DD3A3C6CB9BD93` |
| training | 13,449; `920CE805C81F75BE47EC5D408C2355D0AE912D5657319D3E1506978EAEF3FB62` | 30; 0-48 | `6f4b358088e34d369d622d3b180f1d5e` | `reimport_loc_tr.blend` SHA `9C41D4A44103E657F328AA21653A1F7BF35549EDF6A543810071910612242FA5`; validation `reimport_loc_tr.json` SHA `C05D4CCAF3B89F9FD86B9A4F43532165F8F1832F53D8277C8DB62A47107F67AB` |
| death | 39,763; `4FC1CF58C3ECC7969397D0B3387626A1621A9BCD296D88D1EE0D6ACD2CEAFF13` | 30; 0-48 | `7817d171cc10418badfe8b72d6d1696f` | `reimport_loc_die.blend` SHA `5583A1CA2168E5C8F7DBE7FE707B21DF3F0492224D61EC71A79DC13A41186288`; validation `reimport_loc_die.json` SHA `0D4E6DCB5442A9DC1111A8CD2272074015877C7271DB2CA6439C27886F83D8D3` |

All eight final reimport validations contain `io_pdx_rigAction`, 29,971 polygons, 27,922 imported vertices, two bone-parented locator objects, zero non-manifold edges, zero degenerate faces, and ground contact below `2.8e-7`.

The first long-name support-attack reimport attempt `99a7f1067e7d42398e628cf66d17527a` failed only because Blender could not write the overlong preview path, and the short-name retry request `59169e1c6fad484487df77a8036348e1` produced the clean proof above without changing source geometry.

## Action acceptance evidence

The current native action inspection uses the adapter hash policy `inspect_scene_curve_slot_path_index_key_co_interpolation_v1_not_anim_file_sha256` and confirms that the source action data was not changed by the locator work.

All eight inspected actions report the unchanged action-integrity SHA-256 `1D7D349911E304FCEF35874A7CAE30AECF52CD7D078FEC8BB2E87B907601A27C`.

The inspected native action hashes are idle `59BA84E48899603CB2486D7CD65D30261FB771DD9F9F450EA0AF73D6075F8D14`, move `03C892A46DAAD5AA003AFEB95014780A122ECCA9D61F63718EBAB85DB756DA7E`, attack `D6082761EC6069BDFA494BF6973285A0FA376AC42843D6343B456535010FFE3A`, defend `59BA84E48899603CB2486D7CD65D30261FB771DD9F9F450EA0AF73D6075F8D14`, support attack `97BB2C54072F3722EEDE826129A0D9F1A773F2302CAC17E646F18F02C981E252`, retreat `A52AA4EED50285F4490257E01DEE9D705534D8792C86B83874A9F06F7ADBB4DA`, training `6D53C6B6FF315D264E13B4410E17922F2D513808732A17F020288AC941359BF7`, and death `865F8BD3B9491F50C5E0D369E901478906CF9D63CDE7B08691D6B72BB411F7D0`.

Idle, attack, defend, support attack, and retreat inspections with 145 rows have 72 Euler-channel rows and no quaternion-channel rows, and the idle/defend native hash and exported file hash are identical.

Move, training, and death inspections have 75 rows with 72 Euler-channel rows and no quaternion-channel rows.

The source action inspections were recorded by adapter worker logs `0019597c5eb84726a5396e84e6767fd0`, `a6dd8323b71d489494aedd0ac4942f61`, `eb99c47c7953402aa139106eb9c00b4d`, `746f5f0a2ebe4c9fa32896613c3fb064`, `dda4731998424379b4b760533d530e67`, `6297ca645773496eb739e9285659fd78`, `fc3d57239f05454c8f38d3fc1c473391`, and `7abe2eb3b0fc4e64a60b1e0f9c2e32e3`.

The attempted phase patch request `a257908d583744398537838a832ef30b` was rejected before mutation with `Source action has unsupported object, scale, or non-quaternion bone channels.` because the source uses `rotation_euler` and the locked adapter only accepts `.location` or `.rotation_quaternion` source curves for that operation.

No locked operation converts Euler keys to quaternion keys while preserving evaluated pose, removes unsupported object/custom-property channels, or creates a verified provider/professional action source.

| Role | Current disposition | Reason it is not a final accepted action |
| --- | --- | --- |
| idle | blocked | It is byte-identical to defend and only contains a small scanning-loop motion. |
| move | blocked | It has a distinct export and clean mechanical reimport, but no verified substantive locomotion/contact source. |
| attack | blocked | It lacks verified aim, discharge, recoil, and recovery phases, and its native source is Euler-keyed. |
| defend | blocked | It is a byte-identical alias of idle and is not a distinct defensive role. |
| support_attack | blocked | It lacks verified firing phases and its native source is Euler-keyed. |
| retreat | blocked | It is not verified as locomotion and its native source is Euler-keyed. |
| training | blocked | It has no accepted source semantics or approval. |
| death | blocked | The collapse is substantive in preview evidence, but the source is not an accepted provider/professional action and remains Euler-keyed. |

The `.anim` exports and reimports therefore prove serializer compatibility and byte identity of the exported artifacts, not semantic acceptance for runtime promotion.

## Runtime, muzzle effects, and sound boundary

The current parent-owned entity file is `gfx/entities/autonomous_robot.asset`, and the current parent-owned mesh registration is `gfx/entities/autonomous_robot.gfx`.

Those files name all eight animation roles and the existing `autonomous_robot_dual_mg_attack_sfx` event, but the current entity definition has no node, particle, or light entries for the new locators, so muzzle flash, smoke, light, and gunfire synchronization remain parent-owned pending work.

The inspected vanilla precedent is `gfx/entities/units_infantry.asset`, where the MG entity uses node `muzzle`, `mg_muzzle_particle`, `mg_muzzle_smoke_particle`, `mg_muzzle_flash`, and an `infantry_mg_attack` sound event on attack, defend, and support states.

The parent should use the exported names `muzzle_export` and `muzzle_left_export`, preserve both guns, and bind the dual-MG event to actual firing phases once an accepted attack source exists.

The current parent-owned sound wrapper is `sound/autonomous_robot_sound.asset`, with six role wrappers for selection, movement, idle, footfall/impact, dual-MG attack, and death, and it does not replace global voices.

The source plan records Door knocker audio.ogg by Mx. Granger as CC0 for selection/armored impact, Akkuschrauber – Cordless Screwdriver.ogg by Maximilian Schönherr as CC BY-SA 4.0 for movement/idle mechanical, Metal drop thump.ogg by stephan as public domain for footfall/impact, Maschinengewehr 42.ogv by U.S. Army Signal Corps as CC0 for weapon provenance, MG 42 (Solo) WW2.wav by Lubini as CC BY 4.0 for the exact weapon, and Explosion 10.ogg by tcpp as public domain for death.

The source pages and direct-download URLs are recorded in `evidence/audio/source_plan.md` and `evidence/audio/source_ledger.md`.

The filesystem currently contains only `evidence/audio/original/maschinengewehr_42.ogv` with SHA-256 `A9F0B43FBF3CF876217134A85B6F50B301322C0C0E95EC8483F8C7CFECB8478F` and `evidence/audio/original/mg42_solo_ww2_hq_preview.mp3` with SHA-256 `F95EB1B9FE8E5889D56BD68CA602472B751FA3D287E708F229DFF0827BD6F9FC`.

The ledger claims four additional original files and six derived OGGs, but those files are absent from the job root, so the existing runtime WAVs cannot be promoted as provenance-complete final audio without reconciliation.

The proposed ledger timing is movement servo frames 0-26 with impacts at 1 and 14, idle loop frames 0-97, dual-MG attack and support attack at frame 8, and death onset at frame 1 with collapse phases 37 and 55, but this timing is not validated against the current 30 FPS export or the legacy 24 FPS runtime line.

## Counter package

The bespoke vanilla-green counter outputs exist at `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds` with SHA-256 `147CF90C3D053947640F7865F1DADE6D8FFABA99942E8401ED4575D53DB61B09` and `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds` with SHA-256 `BDEB527F8A73494B918ADEC27C26AEC97C299F51AD00D2DA2946A37A278EDD4B`.

The inspected installed consumer tokens are `GFX_group_autonomous_robot_icon`, `GFX_unit_autonomous_robot_icon_medium`, and `GFX_unit_autonomous_robot_icon_medium_white` in `interface/subuniticons.gfx`.

The large strip is 152x42 with two 76x42 frames, the map strip is 60x12 with two 30x12 frames, and sampled vanilla palette anchors include `(73,106,73)`, `(81,113,81)`, `(119,144,119)`, `(151,170,151)`, `(186,199,186)`, `(198,208,198)`, `(32,44,32)`, `(9,13,9)`, and `(0,0,0)`.

Counter inspection and artist evidence are in `evidence/counter/validation/reference_inspection.md`, `evidence/counter/gfx_handoff.md`, and `evidence/counter/manifest.md`, with parent handoff `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/autonomous_robot_counter_art_handoff.md`.

Parent-owned GFX registration and live consumer validation remain pending, and no reused vanilla counter was introduced.

## Files changed and validation

The only authored source/documentation file changed in this resume is `docs/assets/shared_robot_system/models_3d/autonomous_robot/manifest.json`, which now has status `blocked_capability_review`, records the current adapter and export evidence, separates legacy runtime hashes, and has SHA-256 `74E60D0EC88DE5AA6CA5E5A2AD2EBC6CE8FDDC2F7E535B1BBE5638208B0320B3`.

The adapter-generated evidence added or refreshed in the job root includes the two locator checkpoints, `06_exported.blend`, the locator-bearing mesh and eight `.anim` files, eight actual-byte reimport proof blends, eight validation JSON files, previews, and their adapter result logs listed above.

No gameplay, focus, event, GUI, catalog, entity, sound, or unrelated package source file was edited by this resume worker.

The meaningful validation performed was locked Blender health and socket verification, source geometry/action inspection, same-name locator collision proof, job-owned locator registration, locator-bearing mesh export, eight animation exports, eight exact-byte reimports, material/geometry/weight metrics, ground-contact checks, counter output/hash verification, and manifest hash verification.

Live game validation, final runtime path promotion, particle/light behavior, gunfire timing, mechanical/death sound timing, and parent-owned entity/sound wiring were not claimed because agents must not run the game and the action/audio gates remain unresolved.

## Required parent follow-up and blockers

The primary blocker is the absence of an approved action-capable route that can retain genuine substantive motion while converting or supplying valid quaternion-keyed skeletal actions; manual transform-only or semantic-alias replacements remain forbidden.

The attack and support-attack roles specifically require verified aim, discharge, recoil, and recovery motion, while move and retreat require verified locomotion and ground contacts, defend must be distinct from idle, and death must retain accepted collapse, impact, and settling motion.

The historical Meshy 6 lineage also cannot satisfy the current Meshy 7 lock without a new provider operation, and regeneration is explicitly forbidden for this preserved-geometry task.

The audio package is blocked until the claimed licensed originals and derived files are restored or the ledger is corrected with immutable source bytes, transformations, checksums, and the exact role/sync mapping.

The parent may complete runtime wiring only after those gates are resolved by binding `muzzle_export` and `muzzle_left_export`, adding vanilla-pattern muzzle particles and light, synchronizing dual-MG fire and mechanical/death audio to accepted action phases, preserving role audio without global voice replacement, promoting the final hashes to the runtime paths, and performing user-owned live validation.

No simplification or fallback was used, and no final completion claim is made.
