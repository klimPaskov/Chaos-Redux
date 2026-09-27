# Base zombie rebuild: final actions, export, and runtime wiring (2026-09-27)

Disposition: `implemented` — model, eight actions, textures, entity, sound, and sprite wiring are in the mod; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework plan on 2026-09-27 (“okay, go ahead”), with the robot first and the base zombie second.

## Starting point

The 2026-09-26 Blender session had authored `move_shamble`, `retreat`, `support_attack`, `idle`, `defend`, and a supine `death` on the 90k Meshy lineage (`blender/checkpoints/62_death_supine_root_settle.blend`).
`attack` and `training` were still the Meshy “Punch Forward with Both Fists” and “Boxing Practice” transfers.
The rejected walk was already replaced by the authored shamble, so no Mummy Stagger purchase was needed and no credits were spent in this pass.

## Review findings and fixes

| Role | Finding | Fix |
|---|---|---|
| `training` | Boxer's guard with closed fists; feet hop up to 0.80 and sink 9 cm below the floor on 14 frames | Arms, hands, and fingers re-authored as zombie choreography on the retained Meshy footwork: overhead claw wind-ups and cross-body swipes, a two-handed grab, a lunging seizure, and a hands-to-mouth feeding and tearing cycle; open claw hands; per-frame measured Hips height correction to 4 mm contact |
| `attack` | Reads as a two-handed claw lunge, but floats 0.24–0.44 above the floor on every frame | Per-frame measured Hips height correction to 4 mm contact |
| `death` | Arms hang in the rest A-pose through frames 1–39 while the torso whips back | New arm keys at frames 8, 16, 24, 32, 40: hit jolt, asymmetric fling, one arm dropping and flailing, arms trailing through the topple; keys from frame 47 onward are unchanged |
| Mesh | 89,882 triangles (113,609 export vertices) exceeds the PDX stream ceiling and triples the project's 30k unit norm (vanilla infantry is 3,030) | Collapse decimation to 29,999 triangles, weights limited to four normalised influences; front, three-quarter, side, rear, and face reviews show no visible loss at map scale |
| Export | Four actions carried the slot `OBArmature` while the rig is `Armature.001`, so they exported with no animated channels | Slots renamed; every action re-exported and re-proved |

Rejected actions are preserved in the checkpoints as `meshy_candidate_chaosx_zombies_training_boxing_rejected`, `blender_candidate_chaosx_zombies_training_ungrounded`, `meshy_candidate_chaosx_zombies_attack_floating`, and `blender_candidate_chaosx_zombies_death_rejected_v3`.

## Checkpoints and export

| Checkpoint | Content |
|---|---|
| `63_training_death_attack_final.blend` | Final eight actions on the 90k mesh |
| `64_decimated_30k.blend` (SHA-256 `731185CA…0632`) | 30k mesh, calibration images removed |
| `65b_export_batches.blend` | Adapter partition into four ≤8,000-triangle streams |
| `65c_export_batches_slots.blend` (SHA-256 `C55E69F4…9A89`) | Slot fix; source of every runtime export |

Exports: `export/mesh/chaosx_zombies_65c.mesh` and `export/anim/65c/chaosx_zombies_{idle,move,attack,defend,support_attack,retreat,training,death}.anim`.
Actual-byte reimport proofs `reimport_65c_<role>` exist for all eight roles, with previews under `blender/previews/`.
The mesh is 7.353 tall against the vanilla infantry source height of 7.352, so the entity keeps the vanilla scale 0.8.
Reimported ground contact stays within ±6 mm on every sampled frame, except `move` at 2.5–3.2 cm (about 0.4% of body height) after decimation reshaped the soles, and the death fall frames, which are airborne by design.

## Runtime files

| File | Role |
|---|---|
| `gfx/models/units/chaosx_zombies/chaosx_zombies.mesh`, eight `.anim` files, three `.dds` textures | Hash-identical copies of the exports; hashes in `docs/assets/.../zombies/runtime_sync_20260927.sha256` |
| `gfx/models/units/chaosx_zombies/animation_chaosx_zombies.asset` | Animation registrations |
| `gfx/entities/chaosx_zombies.gfx` | `chaosx_zombies_mesh`, eight animation ids, four `char1.003` mesh settings |
| `gfx/entities/chaosx_zombies.asset` | `chaosx_zombies_entity`, eight distinct states with measured sound and particle events |
| `sound/chaosx_base_zombie_sound.asset`, `sound/002_zombie_outbreak/zombies/base/` | Base voices and impacts, with attribution |
| `common/units/zombies.txt` | `zombies` uses `sprite = chaosx_zombies`; `wendigo_zombies` stays `infantry` |

Textures follow the project convention for unit models (uncompressed 1024² RGBA without mipmaps).
The existing counter set (`GFX_unit_zombies_icon_medium`, `_medium_white`, `_small`) already shows a unique zombie silhouette and needed no change.
Sound roles and timing are documented in `docs/systems/3d_model_pipeline/chaosx_zombie_unit_sound_design.md`.

## Remaining risks

- No listening tool was available; audio quality and loudness balance are unverified by ear.
- The 2026-09-27 01:35 renderer crash happened while the base unit still used the vanilla infantry sprite, so the crash points at a variant zombie model or another entity, not at this rebuild; it remains open.
- The seven variant zombie models remain at 30k triangles and are unreviewed under the rework plan.

# Soldier rebuild (supersedes the civilian body above), 2026-09-27

The user judged the civilian-shirt rebuild too generic; the ZZZ leader portraits show zombified Second World War infantry, so the base zombie was regenerated as an undead soldier.

- Reference: `refs/original/meshy_input_v3_soldier.png`, made from `portrait_ZZZ_leader_3/4` with plain steel helmet, torn field-grey uniform, empty pouches, boots, glowing eyes, and no insignia.
- Provider: Meshy 7 body `01a0e273-c1a8-7201-8b5c-b31eefaacce6` (30), rig `01a0e277-c619-7060-ac2e-cfb10e7d19a5` (5), presets Long Breathe and Look Around (idle), Mummy Stagger (move), Injured Walk Backward (retreat), Hit Reaction (defend), Shot and Fall Backward (death), Zombie Scream (training), and prime text-to-motion attack and support attack applied to the rig; the full ledger is `docs/plans/system_unit_model_rework_plans/credit_ledger.json`.
- Intake: `.tools/3d_pipeline/review/provider_intake.py` with `blender/working/soldier_v3b/intake_manifest.json` (prepare against the vanilla infantry height, per-role provenance receipts, chained imports).
- Review fixes: every provider action floated 4–250 cm; `lab_actions.ground_action` keyed the root so the lowest vertex sits at 4 mm on every frame; slot identifiers and one NLA track were repaired before partitioning.
- Export: `blender/working/soldier_v3b/blender/checkpoints/21b_export_batches.blend` → `export/v3/`, 31,054 triangles in four `char1.001` streams; all eight reimport proofs hold 4 mm contact (`export/v3/export_report.json`).
- Textures: `.tools/3d_pipeline/review/pdx_textures.py` from the body's PBR maps with the humanoid profile gamma 0.72.
- Runtime: files in `gfx/models/units/chaosx_zombies/` are hash-identical to `export/v3` (`runtime_sync_v3.sha256`); `gfx/entities/chaosx_zombies.asset` events follow the soldier's measured phases.
