# Event 020 free rat-animation source audit and production handoff

Date: 2026-08-24
Owner: `020_black_plague`
Asset: `rat_ground_unit_shared`
Status: **eight free professional source actions exported; direct weight transfer rejected; final rat retarget blocked**

## Outcome

The paid Fab route was abandoned after the user's correction. No purchase, login, account creation, or financial transaction occurred.

The CC0 Quaternius Ultimate Animated Animal Pack is the selected free professional quadruped source. The official source-format `Fox.fbx` and license evidence were acquired anonymously at zero cost. The fox is used only as an animation and rig donor; its geometry is not an approved runtime replacement for the one shared oversized rat.

The locked adapter structurally verified one 67-bone tail-bearing quadruped rig and thirteen distinct 30 FPS actions. Eight distinct actions cover the contract without aliasing:

| Runtime role | Approved source action | Source frames | Intended 24 FPS behavior |
|---|---|---:|---|
| idle | `AnimalArmature|AnimalArmature|Idle` | 1–101 | loop; breathing/posture/tail motion |
| move | `AnimalArmature|AnimalArmature|Walk` | 1–33 | loop; quadruped locomotion |
| attack | `AnimalArmature|AnimalArmature|Attack` | 1–41 | nonloop; wind-up/contact/recovery |
| defend | `AnimalArmature|AnimalArmature|Idle_HitReact_Left` | 1–21 | nonloop; dedicated lateral reaction/evasion |
| support_attack | `AnimalArmature|AnimalArmature|Gallop_Jump` | 1–29 | nonloop; distinct pouncing/flanking assault |
| retreat | `AnimalArmature|AnimalArmature|Gallop` | 1–18 | loop; dedicated rapid withdrawal locomotion |
| training | `AnimalArmature|AnimalArmature|Eating` | 1–77 | loop; dedicated head-low creature drill/feeding behavior |
| death | `AnimalArmature|AnimalArmature|Death` | 1–33 | nonloop; articulated collapse/settle |

The mapping is source-distinct and the source motions are structurally valid. All eight were re-imported from the immutable FBX with individual verified provenance receipts, retimed to 24 FPS without altering keyed values, and exported to job-local `.anim` evidence. These are source-rig candidates only, not installable rat animations, because the attempted Fox-weight transfer failed deformation QA.

## Immutable source and license

- Source page: `https://quaternius.com/packs/ultimateanimatedanimals.html`
- Official public folder: `https://drive.google.com/drive/folders/1uJ3N5HfB7jKTseJUNQr3N4YaN0UuEtHk`
- Official FBX file id: `18LKS424TzJB7WO8ZjhwCimov7RNnhSih`
- Local source: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/originals/quaternius_ultimate_fox.fbx`
- Source SHA-256: `24DA24DBD2800BE0B268ADE50429FB7D815423A92A9A39178A4FC460D7B832DE`; 3,498,828 bytes.
- Official license file id: `1F2uy8T2fRpdc6gZ4mnS02_C2E63WvKtn`
- Preserved license: `evidence/free_animation_sources/originals/quaternius_ultimate_license.txt`
- License SHA-256: `256BF3C521D10DD09071855B8784859B0131196D623AE3BC3239787E32A2703F`.
- License: CC0 1.0 Universal/Public Domain Dedication; modification, retargeting, and redistribution are permitted without attribution. Credit to Quaternius remains recommended in project asset credits.

Five additional OpenGameArt rat families were preserved and audited under `evidence/free_animation_sources/`. Their exact URLs, licenses, archive hashes, and inventories are recorded in `source_research.md`. They remain alternative evidence, not selected runtime motion.

## Blender evidence

- Preparation request: `9259719b2d6f40be92f035cc8e558219`.
- Adapter: `chaosx_blender_hoi4` 1.8.2 at the time of source import.
- Blender: 5.1.2, build `ec6e62d40fa9`.
- `io_pdx_mesh`: 0.91.0; archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Source checkpoint: `blender/source/free_quaternius_fox_audit_provider_source.blend`, SHA-256 `0A8328FB030A673B3030621F4996C0A1C2FE46B87EA6CCDF1A739EBDA4FEE8EF`.
- Imported audit checkpoint: `blender/checkpoints/00_imported_candidate.blend`, SHA-256 `BE3FF992B07D50E5E3B0518AEC665B3D357B8D7DE473AA0D86F44C5A3E20CCD2`.
- Preparation report: `blender/reports/free_quaternius_fox_audit_prepare.json`, SHA-256 `AF933E9A16FBD2663E046AF363C89101BB0B2D4E1A9BB42D2EAD9C1F4A4892BF`.
- Structural result: 67 bones, 46 deform vertex groups, 926 source vertices, 1,848 triangles, no zero-weight source vertices, and all thirteen source actions present.
- Audit-only scale normalization reproduced mesh height `7.3518247604`, entity scale `1.35`, and effective height `9.9249634265`. Runtime acceptance remains the prior exact crosswalk `9.9249627827` and must not be replaced by the donor-mesh measurement.
- Rig correspondence: `evidence/free_animation_sources/quaternius_fox_to_rat_rig_map.md`.
- Preview evidence: 24 selected-action phase PNGs under `blender/previews/free_quaternius_*_left.png`; all are rejected as blank.

## Locked production continuation and blocker

Adapter 1.8.4 passed `verify_environment.py --probe-meshy` with no findings. Topology-preserving dual-source request `9a3faa388d214fbb9755a0bfa1022ce3` used the immutable Fox FBX as rig/action source and `blender/checkpoints/reimport_runtime_snapshot_reimport.blend` as geometry source. It preserved exactly 32,909 vertices and 29,999 triangles, bound all three 1024×1024 runtime DDS maps from job-local evidence copies, transferred weights to 32,909 vertices, retained 13 source actions, and reproduced source height `7.3518247604` and effective height `9.9249634265`.

Eight JSON provenance receipts under `evidence/free_animation_sources/provenance/` verify the exact selected FBX action, CC0 source reference, and immutable FBX checksum. Exact-name same-rig imports and 30→24 FPS retimes succeeded for every role. Exported action ranges are idle 0–81, move 0–27, attack 0–33, defend 0–17, support attack 0–24, retreat 0–15, training 0–62, and death 0–27. The eight `.anim` files and text receipts are under `exports/`.

The direct Fox-weighted geometry is rejected. Nonblank phase previews under `blender/previews/rat_quat_*` show severe paw/limb sheet stretching in walk, forequarter/head collapse in attack, and unacceptable deformation in hit reaction, gallop, pounce, eating, and death. Representative failures are `rat_quat_walk_f9_left.png`, `rat_quat_walk_f25_left.png`, `rat_quat_attack_f21_left.png`, `rat_quat_gallop_jump_f22_left.png`, and `rat_quat_death_f33_left.png`.

Adapter 1.8.5 sanitation request `7de063bb8bb9440ca15f1009c0228a1a` is also rejected. The working mesh retained both the inherited `io_pdx_rig` and transferred Fox modifiers, so sanitation selected the old rig, removed 119,145 Fox influences, repaired all 32,909 vertices to `root`, and destroyed deformation. Its output checkpoint is evidence only.

Mesh export before sanitation failed because weighted `Tail5` was marked missing/excluded by `io_pdx_mesh` (`d6c5fdcd7b984847ad573b871315ab0a`). Idle source-rig animation export did succeed (`fedfb49a247f4b59a7a110e4e95feb04`), and the other seven exports also succeeded, but none may be wired because they target the 67-bone source skeleton rather than the installed 17-bone rat rig.

The required continuation is a bounded rest-space source-to-target retarget onto the untouched installed `io_pdx_rig`, not another surface-weight transfer. `evidence/free_animation_sources/quaternius_fox_to_rat_rig_map.md` now records exact source chains, target bones, inspected source rest axes, omitted-detail policy, and the requirement that the adapter read full parent-relative rest matrices and roll internally. No unrestricted Blender script, procedural replacement motion, alias, or runtime mutation is authorized.

Adapter 1.8.6 added the explicit `bone_chains` rest-space route and passed the dependency verifier. The first high-motion Walk request still stopped before source import because `blender/checkpoints/reimport_runtime_snapshot_reimport.blend` contains no `chaosx_working` armature: request `3cb3c15dbd3f4230b1929a7af64f5dee` reported `available_armatures: []` for requested `io_pdx_rig`. A bounded promotion/duplication step must mark exact working copies of the audited 17-bone rig and mesh while preserving the original as protected evidence; selecting an unmarked checkpoint or editing it through unrestricted Blender is not allowed.

A promotion flag was subsequently added to the local adapter sources, but the mandatory verifier then failed and no promotion call was made. Current mismatches are MCP expected `201A7204D08A4407074B5C097CDAEB7CBF97953844DE7D72076F2ADAC59CAF6F` versus actual `5EA1A6C2443220CA9A89F5D9CA6C45F197B3BFD757B728C8103DBECC5A00A527`, worker expected `475363E61D5CF8E3C1C99C18868402A44F0A3F9ECF0637DE53CF2C93614C98BE` versus actual `4E6A49DCA1FC0F4ECA4E34A62EF8F16D1F5A7E37AD9D85B881155DC9213B205A`, and client expected `6813E3619E6E08F9D93566649961C36441D395278CABB3D4533C6D4C0C7F3DB9` versus actual `54810C976CD9969B9DC5CB578480AA764CD2B5681AA4D0D8185298DEF4ED3B45`. Dependency-lock synchronization and a clean verifier are required before resuming.

The lock was then synchronized through adapter 1.8.8. Adapter 1.8.7 promotion/retarget request `241bc0fd2606471a91ecd2a162f68d53` and adapter 1.8.8 rest-basis-conjugated request `af2959ebcc034b2ab7ed6c87388b991a` both transferred Walk structurally but failed visual and contact acceptance. Version 1.8.7 previews are `blender/previews/rat_retarget_move_f*`; version 1.8.8 previews are `blender/previews/rat_retarget_v188_move_f*`. The latter still reached minimum evaluated Z `-0.9512174129`, so grounding correction is not appropriate: the underlying hierarchy/twist transfer must be fixed first. No other role was retargeted after either Walk failure.

Adapter 1.8.9 hierarchy-aware armature-space request `f23ba76a7c564e9e99152aab6a6646a8` also failed Walk acceptance. Its target motion peak was `52.5559912100` versus source peak about `7.36`; early-stop previews at `blender/previews/rat_retarget_v189_move_f1_*` and `_f17_*` retained severe limb/tail distortion and minimum Z reached `-0.9878041744`. Remaining phases and all seven other roles were deliberately skipped.

## Audio status

The user-approved audio package is complete as source and mechanical derivatives. Ten signed 16-bit PCM, 44.1 kHz mono candidates are staged under `audio/final_candidates/`; exact source URLs, creators, licenses, transformations, original/derived hashes, ffprobe receipts, stable identifiers, and provisional action sync recommendations are in `audio/final_candidates_manifest.md` and the earlier `2026-08-24_event020_rat_animation_sound_handoff.md`.

Animation-frame sync remains provisional until the eight source actions are retimed and baked at 24 FPS. No sound definition or runtime sound file was edited.

## Counter status

The counter audit remains unchanged. Existing shared and gameplay alias tokens and both installed DDS strips remain parent-owned and were not modified. Counter provenance/recovery status is recorded in the earlier core handoff. This continuation did not redraw or install counter art.

## Costs and provider status

- Meshy calls: 0.
- Meshy credits consumed: 0.
- Free source cost: 0.
- Paid acquisition or transaction: none.
- Meshy remains unsuitable for quadruped animation; no new geometry was generated.

## Files created or changed in this continuation

- `rat_ground_unit_shared_model_job.yaml`
- `history.md`
- `evidence/free_animation_sources/source_research.md`
- `evidence/free_animation_sources/originals/quaternius_ultimate_fox.fbx`
- `evidence/free_animation_sources/originals/quaternius_ultimate_license.txt`
- `evidence/free_animation_sources/quaternius_fox_to_rat_rig_map.md`
- `evidence/free_animation_sources/quadruped_retarget_tooling_gap.md`
- eight receipts under `evidence/free_animation_sources/provenance/`
- eight source-skeleton `.anim` and `.txt` exports plus `exports/source_skeleton_action_manifest.md`
- job-local audited runtime texture copies under `evidence/runtime_texture_sources/`
- adapter source/checkpoint/report and phase previews under `blender/`
- supersession note in `2026-08-24_event020_rat_professional_source_followup.md`
- this handoff
- `.tools/3d_pipeline/reports/environment_report.json` regenerated by the mandatory verifier

No gameplay, localisation, GFX, entity, `.asset`, sound definition, installed runtime mesh, installed runtime animation, installed sound, or counter file was edited. No commit was created.

## Completion state

- Free licensed professional source: complete.
- Eight distinct source-action inventory: complete, provenance-stamped, retimed, and exported on the source skeleton.
- Existing rat geometry preservation: complete; runtime bytes untouched.
- Direct Fox rig bind/weights: rejected by visual deformation QA; not a final asset.
- Eight final rat-rig `.anim` exports/reimports: blocked on bounded rest-space retarget to the untouched 17-bone rat rig.
- Audio source/derivative package: complete and unwired.
- Parent runtime wiring and in-game validation: not started and remains parent-owned.

No fallback, alias, procedural animation, transform-only action, new rat mesh, new rat tag, subtype model, Rat King model, or runtime mutation was used.
