# demonic_zombies requirement-to-runtime crosswalk

| Requirement | Evidence | Status |
| --- | --- | --- |
| Accepted single input | `refs/original/meshy_input.png` and `input_manifest.json` | complete |
| Distinct Meshy 7 geometry | `job.yaml` resolved model, `blender/reports/creature_components.json (296 renderable components; 47 zero-face fragments discarded)` | complete |
| PDX packed materials | `blender/reports/pdx_material_pack.json` and `textures/dds/` | complete |
| Rig and bounded weights | `blender/reports/creature_rig.json` | complete |
| Idle/move/attack/death skeletal actions | `blender/reports/creature_action_*.json and validation/export_reimport_status.md` | complete |
| `.mesh`/four `.anim` exports and reimport proofs | `export/mesh/`, `export/anim/`, `validation/` | complete |
| Sourced audio and selection consumer | `sound/source_provenance.md`, `sound/chaosx_zombies_sound.asset#ZZZ_infantry_idle` | complete; tag/original-tag scope |
| Bespoke vanilla-green counters | `counters/manifest.md`, `counters/contact_sheet.png`, runtime DDS paths | complete |
| Runtime entity/GFX/unit wiring | `gfx/entities/chaosx_demonic_zombies.*`, `gfx/models/units/chaosx_demonic_zombies/`, `common/units/zombies.txt#demonic_zombies` | complete |
| Live consumer/in-game evidence | User-owned live HOI4 validation | pending user validation |
