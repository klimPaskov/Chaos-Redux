# Elephant model repair handoff

Status: complete for the requested model, runtime installation and export/reimport proof.
The horse compatibility alias has been replaced by a custom elephant with rigid woven-wood howdah, installed vanilla rider, eight distinct actions and synchronized recorded audio.
The parent reviewed the final exported bytes after reimport and verified that those exact bytes are installed.
No in-game validation is claimed, and no commit was made, as instructed.

## Root cause and delivered change

The installed game provided the elephantry sprite, counters and seated rider animations, but no elephant mesh/entity.
The prior compatibility alias therefore rendered horse cavalry.
`gfx/entities/chaosx_africa_elephant.asset` defines the sole `elephantry_entity` and a wrapper cloned from installed `infantry_rider_entity`; its companion `.gfx` binds the custom mesh, materials and all eight actions.
Only the elephant alias and its explanatory comment were removed from `gfx/entities/chaosx_vanilla_entity_aliases.asset`.
`common/units/012_africa_elephant_forces.txt` retains `sprite = elephantry`; gameplay, counters and texticons are unchanged.

The accepted elephant body is a single connected closed surface with 20,000 triangles and 10,002 source vertices.
The hand-built howdah, woven wood, closed cloth, binding straps and forward rider perch add 8,788 triangles in 114 intentionally separate closed construction pieces.
All howdah pieces are rigidly weighted to the back control.
Total custom geometry is 28,788 triangles, with two materials and 39 bones for the spine, neck/head/jaw, five-part trunk, ears, tail, four jointed legs and attachment/control bones.
The body has no open boundaries, nonmanifold seams or degenerate faces; reviewed deformations retain the tusks, ear/head boundaries and leg volumes.
Earlier source defects in the tail surface, rigid cloth fit, tusk/trunk assignment, ear/head assignment, retreat hinge and foot contact were corrected and superseded before delivery.

The final mesh objects are `Mesh_0.002` and `Cube`, each stream index 0, both `PdxMeshAdvanced`.
Six full-mip DDS maps cover diffuse, packed normal and specular for body/howdah.
The body uses 1024 pixels because its 512 normal failed the retained-detail threshold (G standard deviation 14.47); final 1024 G16.5236/A17.9473 passes.
The howdah uses 512 pixels with G20.9526/A21.6634.
Specular padding and material ranges were corrected against immutable sources and decoded final maps, rather than resetting normals or gloss to hide defects.

## Provider, source and manual authoring

One Meshy 7 textured image-to-3D body task was used: `01a1546a-662e-73a7-b6f8-53716892bc13`.
Credits used: 30, reconciled from balance 40 to 10.
No remesh, rig, animation, rider, item or retexture task was submitted.
The downloaded GLB SHA-256 is `85A6640582C5C88F21D9813A4441E956CD86C14C0B329CCAA68A7865CB89AFF5`.
The approved original reference is `refs/original/meshy_input.png`, SHA-256 `78A04549F24C4C1E5E510BEEAD8932D89F402CC8E0B64A17DCCD7E8CBF9AA702`.
The parent-reviewed item-free 1380 by 1140 RGBA derivative is `refs/derived/models_1018/body_candidate_01.png`, SHA-256 `D25E2BC1345B70C2284C05C550A0E9F15CC264F79AA3020FD5D779438F6EB7E0`.
Historical reconstructed ImageGen receipts remain labelled reconstructed; no new image-generation call was needed for the retained approved derivative.

The howdah, measured anatomical rig, selected-region skin corrections and explicit role keys were authored live in the isolated Blender Lab session on port 9886.
The parent inspected the archived skeleton and role-key sessions; no template/formula motion or skeleton generator was used.
`evidence/live_authoring_sessions.zip`, its receipt ledger and the final death/delivery session archives preserve the exact live code and results.
The locked adapter accepts the compatibility enum `manual_blender_gpt6_astra`; this is a schema label, not a false model attribution: the production specialist actually ran as `gpt-6.1-sol`.
The final retained authoring checkpoint is `blender/checkpoints/65_final_authored_runtime_source.blend`, SHA-256 `69CA0F5DBE4ADE4F7FF4F04E76013D074B301FC3548CC2C2ED2383A4F727D27E`.
The production handoff at `runtime/handoff.md` records retained source/export/reimport checkpoints and workspace cleanup.

## Actions and actual-byte review

Every action is 30 FPS and in place in XY.
Idle breathes, moves the ears/trunk and shifts weight; move has a four-beat walk; retreat is a separate faster amble.
Attack winds up, commits a forward charge step and tusk/trunk strike, follows through and recovers; defend rears and stamps; support attack braces and raises the trunk while the rider fires; training performs a deliberate trunk/step drill; death collapses onto its side and settles.
Idle/move/retreat close their loops, and the combat/training clips return through their recovery before repeating their own state.
Death has no next state and remains settled.
Actual exported attack motion from frame 18 to 36 advances tusks by 0.448932, trunk by 1.821695 and chest by 1.580817 source units toward facing minus Y while Root XY remains fixed.
The final death half-frame scan is above the floor throughout (minimum 0.001961544 source), with maximum nearest-ground gap 0.007041128; sustained head/flank support begins at frame 92.5.
The earlier exported half-frame penetration was corrected by local shin/sole support transfer and re-exported, not waived or hidden by a global lift.

| Role | Samples / duration | Reviewed phase sheet |
| --- | --- | --- |
| idle | 151 / 5.033333 s | `evidence/final_actions/idle/idle_three_views.png` |
| move | 71 / 2.366667 s | `evidence/final_actions/move/move_three_views.png` |
| retreat | 55 / 1.833333 s | `evidence/final_actions/retreat/retreat_three_views.png` |
| attack | 84 / 2.800000 s | `evidence/final_actions/attack/attack_three_views.png` |
| defend | 97 / 3.233333 s | `evidence/final_actions/defend/defend_three_views.png` |
| support_attack | 121 / 4.033333 s | `evidence/final_actions/support_attack/support_attack_three_views.png` |
| training | 123 / 4.100000 s | `evidence/final_actions/training/training_three_views.png` |
| death | 127 / 4.233333 s | `evidence/final_actions/death/death_three_views.png` |

The parent looked at every panel in these final map-camera (55 degrees), front and side sheets, with at least five phases per action and extra swing/contact phases for gait and combat.
The combined reviewed sheet is `evidence/final_reimported_actions.png` (SHA-256 `BC617F99B52733690716C835FBB35863A34224EEDF8E5E4861F3E89E9493B628`).
The native assembly sheet is `evidence/final_reimported_rider_composite.png` (SHA-256 `83D9F1E71CF32DCB241AAEA4A61016277140ECE0EA62D9409AD158B89E65FCB4`).
The parent also reviewed all ten full-resolution tiles in `evidence/final_native_composite/`: idle frame 1, move frame 27, attack frame 36, support_attack frame 45 and death frame 103, each map/side.
Final native hand/stock/muzzle fit and death ground clearance pass; the rifle remains complete and clear of the howdah and elephant.
All eight `.anim` files passed `anim_signs.py` and delivery world/root checks, with closed-loop checks for the three looping actions.
`blender/reports/final_actual_byte_delivery_gates.json`, `final_reimport_review_<role>.json`, `final_actual_surface_sound_contacts.json` and `evidence/current_binary_binding_audit.json` retain the specific results.

## Rider, scale and native firing

The installed horse reference includes mesh scale 0.45 and entity scale 0.65, giving runtime dimensions 1.92919 by 5.94834 by 4.57647.
The elephant's seated assembly measures 6.59831 by 12.94037 by 11.77656 with mesh scale 1 and elephant entity scale 0.8.
The parent accepted the 55-degree scale comparison at `evidence/models_1018/production_relaunch/assembled_vanilla_map_scale.png`; the elephant is uniformly fitted, not stretched to the provisional height ceiling.
`blender/reports/final_native_support_and_scale.json` preserves the complete transform crosswalk.

The installed vanilla rider is attached at `Saddle_Node`, child of `Howdah`, mirroring the native cavalry attachment structure.
Native elephantry idle/move clips carry Hip scale 1.75, so seated roles use constant Saddle_Node scale 1/1.75 and combat roles use 1, with the native rider entity factor 0.8 unchanged.
The locked adapter's animation normalization initially reset that authored scale; only the already-authored constant Saddle_Node scale was restored after export, with preimage hashes and all other decoded records unchanged.
The restored final bytes were then sign-checked, delivery-checked, reimported and visually reviewed.
No native rider mesh, animation or texture is shipped.
During death the installed seated rider is carried with the collapsing platform; no separate custom rider action was requested or introduced.

| Elephant state | Native rider animation | Native rifle2 state / events |
| --- | --- | --- |
| attack | attack | defend; muzzle particle/flash and infantry_rifle_attack at 0 s, cartridge and infantry_rifle_cartridge at 1.2 s |
| defend | attack | defend; same installed event timing |
| support_attack | support_attack | support_attack; muzzle particle/flash and infantry_rifle_attack at 0 s, cartridge and infantry_rifle_cartridge at 1.2 s |
| idle / move / retreat / training / death | elephantry_idle or elephantry_move | idle; no custom weapon discharge |

The custom elephant body is non-firing; the complete package is `fires_in_combat` through its installed attached rifle.
Native weapon bindings were read from `gfx/entities/units_infantry.asset:919-956`; body/rider role propagation follows the installed cavalry pattern.

## Recorded audio

All originals and six staged derivatives were reverified against their recorded hashes before installation.
The derivatives are PCM16, 44.1 kHz, mono; mechanical high-pass/trim/fade/level processing is recorded in `evidence/audio/repair_2026_10_18_v2/receipt.json`.
No audio was synthesized, generated or hand-recorded.

| Source | Author | Licence | Original SHA-256 |
| --- | --- | --- | --- |
| [Dull Thud](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg) | gregoryweir | Public domain | `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3` |
| [Elephant voice - trumpeting](https://commons.wikimedia.org/wiki/File:Elephant_voice_-_trumpeting.ogg) | தகவலுழவன் | CC0 1.0 | `E5F3120E5EACA87CC080BBF57BD185C96D52FD0F63CC1DFE33228C8BFA29F3BC` |
| [Squeaky door](https://commons.wikimedia.org/wiki/File:Squeaky_door.ogg) | leonmire | Public domain | `B60B97C3F73C9754FC36B58CEA4862D50FF800F12632C9B55BC6F8132E93D9C5` |

The supplied trumpet is catalogued as Asian elephant and retained under the explicit existing-recording instruction.
The thud is recorded cardboard-box Foley; the creak is a recorded door sound used for the wooden platform.
Attack/death share one trumpet take, movement/impact share one thud at different levels, and these are not represented as different recordings.
The footfall file measures -5.9994 dBFS peak, 4.99 ms lead silence and no direct flat top.
`evidence/entity_audio_timing_plan.json` contains all 28 events with animation hashes, contact frames and waveform peak offsets.
Sole contacts were measured from the reimported evaluated surface at half-frame intervals (1/60 s), not inferred from ankle keys or nominal gait quarters.
The recorded impact peak is 0.051417234 s after cue start; death flank contact at 3.05 s therefore cues impact at 2.998582766 s.
Random start-delay fields were removed from movement/idle/attack effects; existing modest pitch variation and sound limiting remain.
Support attack has a trumpet cue without invented footfalls.

## Installed files and hashes

`runtime/installation_receipt.json` records source/destination SHA-256 for every one of the 24 runtime copies, with original WAV preimages preserved.
`runtime/installed_binding_audit.json` proves exact byte identity, all eight distinct action bindings, decoded mesh/material names, sound nodes/times, the native rider attachment and exactly one elephantry entity.
The initial copy helper hit an unsupported Python `Path.write_text(newline=...)` keyword after copying; the destinations and original preimages were inspected before finishing the two text edits with a compatible writer.
No asset or source edit was lost, and the final installed audit passed.
The table below lists every changed runtime file and its final SHA-256.
The complete retained job workspace plus changed documents/runtime files, including this handoff's own final hash, are inventoried in `evidence/final_file_sha256.json` (the inventory excludes itself to avoid a recursive hash).

| Changed runtime file | Final SHA-256 |
| --- | --- |
| `gfx/models/units/012_africa_elephant/chaosx_elephant.mesh` | `8C0D20DF143B12770688CBA46144FA5926D8F8C48C146E8FEDCEA6353C3DEAB4` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_attack.anim` | `CBFC1170A691B19020B61CE5F98CAED6F62EAD9EBBDEBDE90A7ABBE609A18B5E` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_body_diffuse.dds` | `1C4BBC74DF06D4C6E3E4E2CF38DFF85E3798B51BED865E8674F383872840388B` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_body_normal.dds` | `860C9283BF4F5B83D22DB5F3B9CBE1F8E7DA291E6C1CAA2272274BBF6597849F` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_body_specular.dds` | `E710122B4C38083558F2D71A4F910A8D3650EAA94DF3A5CBA5B8FF6B0C3EDF88` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_death.anim` | `A72BB95464E8C99EFEA9D8507BEC9BC59EF6C33BDD974416CD91C372B0FC3242` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_defend.anim` | `2641245BACF8DBF8ECA539BF4D5332195A196684FD746A37E44A156AB0F06962` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_howdah_diffuse.dds` | `644F1EB0FC556C19FB828E256A9BEFA32DE1E87E977CD6E8A99AAEAE11FDB3A7` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_howdah_normal.dds` | `DA4FE2847892D1F96EEA31E40DFE2E30E7ADA166902143553BB3EEC51C2368FD` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_howdah_specular.dds` | `2968BEB855FE717CB6D40EA0E5318F13BD8B5DB00441DA858D3424F5149AC5CA` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_idle.anim` | `5E7ADE30B4E0932A3DA6FD90A0134E650664228DFCC324D5BA82A325B55B09DC` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_move.anim` | `E16AAFCE8BA0CE231963C9849083AAD2B7809D8012258B6D27FE53F1B55F9123` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_retreat.anim` | `DFECA38EFEEE25ED3CA0E5D86ED8E1CDF87F3E1ABBD7608D8B8401A70C0D2027` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_support_attack.anim` | `8DB2B2AA5E64470D7638B6383D8E974DFFB3B7E09A3CE1571383EFECEF67041B` |
| `gfx/models/units/012_africa_elephant/chaosx_elephant_training.anim` | `2028034CEC7FBDA226963F177BA7F6DAFC6659DE2F76785BA377310A89064446` |
| `gfx/models/units/012_africa_elephant/animation_chaosx_elephant.asset` | `200F0F8F0E38129D89DFB78CB87D34FFE59153A76A8D83C0F8ADCAFAF7FA5C13` |
| `gfx/entities/chaosx_africa_elephant.asset` | `3F5663D959AC053546BA7648298A43DB419EFD51C22B27B14636A12E90EAEB85` |
| `gfx/entities/chaosx_africa_elephant.gfx` | `7913E97445F8B57FBDA4A49B627FF65A384122EEF9DEA971ABD54890B3578818` |
| `sound/012_africa/elephant/chaosx_elephant_move_contact.wav` | `43D52977BB54A9FEB871E13766FF3CF081721C1A0A7C9E2096EAD9DF35AFD2BD` |
| `sound/012_africa/elephant/chaosx_elephant_impact_contact.wav` | `0100B084C1392E30EB49461D543E2EF660431E542FA83F2E09F32B07F927D3A3` |
| `sound/012_africa/elephant/chaosx_elephant_idle_call.wav` | `839AE59BE7F39D5098649D8F333872063DF9D4ACF370C496AC558AB573F268B4` |
| `sound/012_africa/elephant/chaosx_elephant_attack_call.wav` | `49EF9406056629FDD8F0859D0AAD383AF6E949D70E872FAFD93E686BE7542CEB` |
| `sound/012_africa/elephant/chaosx_elephant_death_call.wav` | `49EF9406056629FDD8F0859D0AAD383AF6E949D70E872FAFD93E686BE7542CEB` |
| `sound/012_africa/elephant/chaosx_elephant_supply_load_creak.wav` | `D53A95B4B41CEDBE6866F6016932A3607CA3E3D7F3FE0BE515EC64C15CD6A2ED` |
| `gfx/entities/chaosx_vanilla_entity_aliases.asset` | `703D0258C6E6528C93AB814ECAB41772BCAD629D87A6F6EC39F398F37A7FB11D` |
| `sound/chaosx_elephants_sound.asset` | `7F647C806BFE562BF12ED3F1BED95A4B2BBBC5151E07541600D893B9B4FD125F` |

Updated documentation: this handoff, `docs/systems/3d_model_pipeline/chaosx_africa_elephant_model.md`, and job `manifest.md`, `job.yaml`, `runtime/handoff.md` plus the cited evidence receipts.
The historical manifest sections remain preserved and explicitly superseded by the current accepted package.

## Reference and tooling evidence

The reference tools were absent from the initial inventory and later became exposed and succeeded; receipts are `evidence/reference_integration_relaunch.json` and `evidence/reference_installed_entity_relaunch.json`.
`source_lookup` returned no indexed rider definition, so the exact installed source was read directly.
Offline Entity modding lines 25-183, revision `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`, covers mesh/action registration, attachment, state propagation and sound events.
Installed effects documentation lines 6826-6838, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents entity animation selection; concrete entity examples came from installed cavalry and infantry files.
The offline graphical-assets Object Types section is empty, so no schema coverage is claimed from that heading.
Native timing/in-place comparison is retained in `evidence/vanilla_action_timing_relaunch.json` and the source/reimport phase reviews.
The uppercase locator API rejection was resolved through the explicitly permitted attachment bone; a preview orientation rejection was corrected once from unsupported side to right.
No external tool repair or shared tooling change was made.

## Simplifications, omissions and limits

No requested elephant component or action was simplified or omitted, and no model production blocker remains.
Existing elephantry counters are retained by explicit user direction.
Per-subunit selection voices remain country-routed; entity idle audio is not claimed as selection audio, and no country voice routing was changed.
The reused native rider remains seated during collapse rather than receiving a separate custom rider death clip.
Verification is source, exported-byte, reimported geometry/material/action and rendered-composition evidence, not observed in-game behavior.
No Hearts of Iron IV process was launched or controlled, and no settings were changed.
The owned Blender PID 29232 and port 9886 listener are confirmed absent in `evidence/models_1018/production_relaunch/live_session_shutdown.json`.
Workspace-size cleanup is recorded in the production handoff and `evidence/models_1018/production_relaunch/checkpoint_cleanup.json`; provider/reference/audio sources, accepted checkpoints and final proofs are retained.
Cleanup removed 248 superseded checkpoints, previews, backups and successful console-log files, reclaiming 1,263,723,612 net bytes, while retaining 48 complete compact result receipts with original-log hash mappings.
The evidence workspace remains because this model-repair brief explicitly requests its manifest, contact sheets and source provenance; this is not completion of the whole Event 012 content goal.
Skills used: `chaos-redux-3d-model-pipeline` with its required references, `chaos-redux-event-assets`, and `chaos-redux-subagents`.
No skill was created or updated; no gameplay unit definition was edited.
