# Battalion model repair — 18 October 2026

## Result

The requested battalion repair is installed and ready for parent review and commit.
The delivered mesh and all eight animations were exported through the locked adapter, quaternion-sign checked, natively reimported, inspected from front/side/54.57-degree map views at five phases per action, and copied with matching source/destination SHA-256 values.
No Meshy call, balance query, paid task, audio generation, HOI4 launch or Git commit was made.
New provider task IDs: none; credits used: **0**.
No in-game validation is claimed.

## Root cause and repair

The reservoir was substantially skinned to both arms and shoulders, so ordinary arm motion bent and lifted the backpack.
The lance had no credible two-hand retention, several presets did not fit their state, and the repeated attack/support endings failed to close.
The body also contained dangling triangle flaps and pinched/non-manifold regions.
The final body is one closed connected shell, with a separately closed rigid lance and a closed flexible feed hose.
The 34,782-triangle assembly retains the 24 body bones plus `spray_lance_control` under `RightHand`, fixed closed gloves, the vanilla-calibrated height and entity scale 0.8.
The reviewed reservoir region now follows the torso; the attachment band is blended to the spine, and the lance/fore-grip contacts are maintained on the assembled model.
The nozzle was measured against the actual mouth of the lance.

| Role | Shipped defect | Installed behavior | Frames at 30 FPS |
| --- | --- | --- | --- |
| idle | Wide one-handed weapon swinging and abrupt head/elbow motion. | Two-hand low-ready carry, breathing and measured weight shifts/look turns. | 1–233 |
| move | Carry_Heavy_Object_Walk produced spread arms and a laden, unsuitable carry. | Even, shorter walking strides with one measured plant per foot and a retained carry. | 1–41 |
| attack | The nozzle crossed the chest, aim was off-axis and the repeated ending did not close. | Low-ready preparation, forward aim, one finite spray, follow-through and recovery while advancing. | 1–61 |
| defend | Standing_Reload gestures did not read as braced defense. | Braced guarded stance with the lance retained; no empty-space reload or reservoir cue. | 1–51 |
| support_attack | A kneel-to-stand ending snapped when the state repeated; coat and aim failed. | Distinct low braced performance with two forward spray windows and a closed return. | 1–129 |
| retreat | An uneven short backward shuffle with equipment contact and single-frame motion defects. | Hurried low carry with higher foot clearance, soft knees and two balanced plants. | 1–39 |
| training | Kneeling_Reload manipulated empty space and swept the lance across the knee. | Kneeling dry-aim and recovery drill with both hands retained on the lance. | 1–208 |
| death | Long upright reaction, poor retained-item contact and unsupported final body groups. | Shot reaction, knee drop, articulated side collapse and grounded settle with the lance retained. | 1–141 |

The backward-gun shuffle candidate was rejected after its asymmetric plants were measured; retreat uses the distinct already-downloaded running motion with authored foot paths and soft knees.
Death received a stable support-arm solve, knee-drop timing cleanup and an articulated side settle after dense native review found a grip loss and a floor interpolation excursion.

## Runtime files and final SHA-256

Every runtime copy is listed here; its exact source path, old destination hash, final source hash and final destination hash are in the [installation receipt](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/models_1018/continuation/runtime_installation.json).

| Changed runtime file | Final SHA-256 |
| --- | --- |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion.mesh` | `3648D1E56FA3330BCF3C23A21E842C837996215F915D26FF61798347E1723CBF` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_idle.anim` | `8F44FDACF3C7A90A4CA0056614871C8ABAD513C0B3DC2176D1365B5220F142FD` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_move.anim` | `6AF103E8D1BC26B554B5DA58830ED436A8761DE718B44A69634230B01652A811` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_attack.anim` | `ECAB3FFA9E47C09265850017B784BE6A2E383BFB2B152E8D2DBFD632368EBE38` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_defend.anim` | `5721EC2A781D4495BAE0890E4FCD791E744C3A98377891ACFC6CA6B42A3A834E` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_support_attack.anim` | `BE41286EBC9B0F6CC1173A9D3C5163CB090213E7EDE6F91491D05B3E55B5F0FE` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_retreat.anim` | `DBF5D3D0CE181940FB95ED148839731823175160EEF90105B50497AD0A32B644` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_training.anim` | `67E5F2423CA84BBCB7EA01A0A2C7A18DE2B27235B50960366F04A541B263C54A` |
| `gfx/models/units/chaos_assault_battalion/chaos_assault_battalion_death.anim` | `ECF15ECC53C0D29FCF9EBA30391023F9EBB8E9D0E33A65BF8FE69BC39E89060B` |
| `gfx/entities/chaos_assault_battalion.gfx` | `D96BB90EAF2B72F5B90015E8F28522E937A8FF0940E8A0F13165D6169E635344` |
| `gfx/entities/chaos_assault_battalion.asset` | `D5025A24488DA14D3E1201263E791505EBD8E39EA3BEFDA661C25716F700B422` |
| `sound/chaos_assault_battalion_sound.asset` | `14FE4690AE02B8C105BD4745DAB030B5BD051172B4B621785C67B2D3886AF783` |

The three DDS maps, twelve WAV files and animation registration asset remain byte-identical to intake.
The GFX registrations cover the four `char1.001` streams, the `char1.002` lance stream and the `reservoir_feed_hose` stream.
All public mesh, entity, animation and state identifiers remain stable.
The complete owned-write inventory, including the final manifest, job record, checkpoints, renders, scratch transcripts and this handoff, is [final_file_hashes.json](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/models_1018/continuation/final_file_hashes.json).

## Evidence reviewed

Final combined sheet: [final_reimported_actions_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimported_actions_contact_sheet.png).
Per-action sheets below contain all five front, side and map phases.
The native review also includes discharge grip close-ups, decoded-material views and rear/top/underside rest views.

| Action | Reviewed sheet |
| --- | --- |
| idle | [idle_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/idle_contact_sheet.png) |
| move | [move_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/move_contact_sheet.png) |
| attack | [attack_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/attack_contact_sheet.png) |
| defend | [defend_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/defend_contact_sheet.png) |
| support_attack | [support_attack_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/support_attack_contact_sheet.png) |
| retreat | [retreat_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/retreat_contact_sheet.png) |
| training | [training_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/training_contact_sheet.png) |
| death | [death_contact_sheet.png](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/death_contact_sheet.png) |

The exact individual render paths, immutable input hashes, phase frames and half-frame measurements are in [review.json](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/final_reimport_shipping/review.json).
The [final export record](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/models_1018/continuation/final_export.json) binds every selected `.anim` to its native reimport and current mesh.
All eight actual-byte motion gates pass, without strike-window exceptions; repeated states close, root motion remains in place, and the serialized quaternion signs are continuous.
Both move and retreat have exactly one certain plant per foot.
The largest measured support-grip anchor deviation across the final native half-frame samples is under 0.01 source units, and all measured sole excursions remain within the 0.01-unit review tolerance.
The source/native comparison used the installed GER infantry idle, moving, standing/crouched attack, retreat, aim-exercise and death clips in `evidence/models_1018/vanilla/reference_sheet.png`.
The walk uses the same 41-frame span as the inspected vanilla walk; the other clips have timings appropriate to the retained sprayer and loaded reservoir.
These are source, exported-byte and Blender observations, not observed HOI4 behavior.

## Sound and particle synchronization

| State | Cue time(s) in seconds | Evidence |
| --- | --- | --- |
| attack | 0.4000 | Forward aim and one 0.610-second recorded spray / finite burst |
| support_attack | 0.6667, 2.1333 | Two forward braced spray windows |
| move | 0.5667, 1.2333 | Native boot-sole landings, one per foot |
| retreat | 0.5333, 1.1667 | Native boot-sole landings, one per foot |
| death | 0.1000 voice; 2.9333 impact | First sustained torso/gear ground contact, then settle |

The finite spray emitter and recorded burst have matching 0.610-second emission/audio duration; its 0.350-second particle tail finishes before the next discharge.
The move sound’s random onset delay was removed so the recordings follow the measured plants.
Footstep tails may cross an animation loop boundary but finish before the next measured footstep.
All twelve retained WAVs were probed as PCM signed 16-bit, mono, 44.1 kHz; receipts are in [runtime_audio_probe.json](../../assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/models_1018/continuation/runtime_audio_probe.json).

| Existing recording family | Source | Author / performer | License |
| --- | --- | --- | --- |
| Breath | https://opengameart.org/content/horror-breathing | primbal | CC0 1.0 |
| Spray | https://freesound.org/people/Soundkrampf/sounds/414025/ | Soundkrampf | CC0 1.0 |
| Footsteps | https://opengameart.org/content/footsteps-0 | GboxMikeFozzy | CC0 1.0 |
| Death voices | https://opengameart.org/content/death-sounds-0 | Exewin | CC0 1.0 |
| Body impact | https://bigsoundbank.com/body-fall-1-s2452.html | Joseph SARDIN; Kellian F. and Yoann B. | CC0 1.0 |
| Reservoir contact, retained recording | https://opengameart.org/content/fantasy-accessory-sfx-library | Vehicle / Jan Schupke | CC0 1.0 |

Source/member hashes and prior derivations remain in `wp5_wp6_audio_handoff.md` and the job’s existing audio receipts.
The archived spray source is lossy MP3; the reservoir library’s original archive is absent locally, while its source member and prior attribution registry are retained.
No new source provenance or auditory/in-game playback acceptance is claimed for those historical recordings.

## Reused motion provenance

These are historical task IDs for files already downloaded, not tasks submitted during this repair.
Each role has its own distinct source motion; the free walk and free run are different motions bundled with the same historical rig task.

| Role | Source motion | Historical task ID |
| --- | --- | --- |
| idle | Idle, preset 0 | `019fd5d8-f32e-79df-bbbd-be40e4c1c46d` |
| move | Free walking / walking_man | `019fd5d0-471a-76c3-962a-171f0bb253fe` |
| attack | Run_and_Shoot, preset 98 | `019fd5d8-f990-787d-84c6-58f73dd022a2` |
| defend | Combat_Stance, preset 89 | `019fd5d8-fdcc-77f8-82c7-c8ee13e644e6` |
| support_attack | Side_Shot | `01a00442-7654-7e44-bba4-fe07e5c42650` |
| retreat | Free running / running | `019fd5d0-471a-76c3-962a-171f0bb253fe` |
| training | Kneeling_Reload, preset 165 | `01a0e3e7-5104-7417-80eb-034a2335a77b` |
| death | Dead, preset 8 | `019fd5d9-0214-79e1-bfb4-752194ea9f11` |

The source hashes, inspection results and receipt-verified import calls are under `provider/reused_presets/`.

## Tool evidence, limits and completion boundary

Blender 5.2.2 LTS build `d13f752e3b9c`, Lab 1.0.3, adapter 1.11.0 and the locked io_pdx_mesh 0.91 compatibility files were verified.
The connected tool inventory exposed no HOI4 coding-reference or Blender tools, so the verified repository MCP wrappers and pertinent local reference files were used.
Reference paths, line spans and source hashes are retained in `evidence/models_1018/relaunch_references.json`; the offline entity sections and installed infantry entity/shader precedents were read.
The material helper rejected valid BC1 diffuse input, so the same verified DDS maps were bound through the authorized live Blender route; no shared tool was changed.
Missing job-profile metadata and the owned nozzle’s working-object classification were corrected before the successful export receipts.
The Blender importer can reintroduce q/-q curve signs while reconstructing native poses; equivalent-sign cleanup in the unsaved review scene is recorded separately from `anim_signs.py` on every delivered `.anim`.
Only the assigned Lab process on port 9884 was used; its closure receipt is `evidence/models_1018/continuation/session_closed.json`.

## Simplifications, omissions, and blockers

**None within the requested repair.**
Fixed closed glove grips without finger articulation or subdivision follow the explicit user instruction.
No action, equipment component, runtime registration or required review view is omitted, and no placeholder or transform-only action was shipped.
The existing counters and unit/gameplay definitions were outside this repair and remain unchanged.
The parent owns final package review and the commit; this job created no commit.
The user owns in-game validation, which is neither claimed nor requested as a completion gate.

Skills used: `chaos-redux-3d-model-pipeline` with its start-gate, Blender/export, audio/counter and rebuild references; `chaos-redux-event-assets` with its unit-material and reference-library guidance.
No unit definition was touched, no skill was created or updated, and no shared tooling was edited.
