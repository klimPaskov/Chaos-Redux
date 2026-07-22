# Biological prototype reward-card icon manifest

Package: `chaos_warfare_system / stage_7_biological_warfare / prototype_reward_icons`

Date: `2026-07-22`

Related consumer: `common/special_projects/projects/biowarfare_main_projects.txt` — eleven `GFX_PLACEHOLDER_sp_project_picture` uses are intended to be rewired by the parent agent.

Asset type: fictional HOI4 special-project prototype-reward picture cards.

Source mode: `$imagegen` built-in generation, one independent source output per requested id.

Runtime: exact `198x218` RGBA source preview and legacy one-level uncompressed BGRA DDS (`32` bits per pixel; `172784` bytes per file). This size follows the current vanilla `PLACEHOLDER_sp_project_picture.dds` precedent, not the separate `161x98` special-project project-icon family.

Final folder: `gfx/interface/special_project/rewards/biowarfare/`

Suggested `.gfx` file: `interface/special_projects/biowarfare.gfx` (existing Chaos Redux special-project sprite family; the file was not edited here).

Localisation: none; these are sprite-backed art replacements only.

## Requirement-to-runtime crosswalk

| Reward id | Semantic composition | Source PNG | Keyed intermediate | Processed PNG | Final DDS | Sprite | Status |
|---|---|---|---|---|---|---|---|
| `sp_anthrax_reward_caution` | Locked canister, blank caution ledger, containment vial | `source_png/sp_anthrax_reward_caution.png` | `intermediate_png/sp_anthrax_reward_caution_keyed.png` | `processed_png/sp_anthrax_reward_caution.png` | `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_caution.dds` | `GFX_sp_anthrax_reward_caution` | `complete` |
| `sp_anthrax_reward_field_testing` | Analog field instrument, protected vials, survey markers | `source_png/sp_anthrax_reward_field_testing.png` | `intermediate_png/sp_anthrax_reward_field_testing_keyed.png` | `processed_png/sp_anthrax_reward_field_testing.png` | `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_field_testing.dds` | `GFX_sp_anthrax_reward_field_testing` | `complete` |
| `sp_anthrax_reward_antibiotics` | Medical tray, sealed ampoules, blank treatment ledger | `source_png/sp_anthrax_reward_antibiotics.png` | `intermediate_png/sp_anthrax_reward_antibiotics_keyed.png` | `processed_png/sp_anthrax_reward_antibiotics.png` | `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_antibiotics.dds` | `GFX_sp_anthrax_reward_antibiotics` | `complete` |
| `sp_plague_reward_caution` | Latched containment case, audit ledger, seal press | `source_png/sp_plague_reward_caution.png` | `intermediate_png/sp_plague_reward_caution_keyed.png` | `processed_png/sp_plague_reward_caution.png` | `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_caution.dds` | `GFX_sp_plague_reward_caution` | `complete` |
| `sp_plague_reward_field_testing` | Open survey case, analog meter, capped tubes, route marker | `source_png/sp_plague_reward_field_testing.png` | `intermediate_png/sp_plague_reward_field_testing_keyed.png` | `processed_png/sp_plague_reward_field_testing.png` | `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_field_testing.dds` | `GFX_sp_plague_reward_field_testing` | `complete` |
| `sp_plague_reward_antibiotics` | Pharmacy drawer, sealed ampoules, cold-storage jar, blank ledger | `source_png/sp_plague_reward_antibiotics.png` | `intermediate_png/sp_plague_reward_antibiotics_keyed.png` | `processed_png/sp_plague_reward_antibiotics.png` | `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_antibiotics.dds` | `GFX_sp_plague_reward_antibiotics` | `complete` |
| `sp_tularemia_reward_caution` | Nested sample case, custody ledger, balance scale, bell jar | `source_png/sp_tularemia_reward_caution.png` | `intermediate_png/sp_tularemia_reward_caution_keyed.png` | `processed_png/sp_tularemia_reward_caution.png` | `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_caution.dds` | `GFX_sp_tularemia_reward_caution` | `complete` |
| `sp_tularemia_reward_field_testing` | Survey tripod, optical marker, closed case, range stakes | `source_png/sp_tularemia_reward_field_testing.png` | `intermediate_png/sp_tularemia_reward_field_testing_keyed.png` | `processed_png/sp_tularemia_reward_field_testing.png` | `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_field_testing.dds` | `GFX_sp_tularemia_reward_field_testing` | `complete` |
| `sp_tularemia_reward_antibiotics` | Insulated ampoule case, amber bottle, blank inventory sheet | `source_png/sp_tularemia_reward_antibiotics.png` | `intermediate_png/sp_tularemia_reward_antibiotics_keyed.png` | `processed_png/sp_tularemia_reward_antibiotics.png` | `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_antibiotics.dds` | `GFX_sp_tularemia_reward_antibiotics` | `complete` |
| `sp_smallpox_reward_caution` | Containment bell jar, sealed capsule, caution ledger, cabinet fragment | `source_png/sp_smallpox_reward_caution.png` | `intermediate_png/sp_smallpox_reward_caution_keyed.png` | `processed_png/sp_smallpox_reward_caution.png` | `gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_caution.dds` | `GFX_sp_smallpox_reward_caution` | `complete` |
| `sp_smallpox_reward_field_testing` | Brass microscope, covered sampling slide, ruler, closed cassette | `source_png/sp_smallpox_reward_field_testing.png` | `intermediate_png/sp_smallpox_reward_field_testing_keyed.png` | `processed_png/sp_smallpox_reward_field_testing.png` | `gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_field_testing.dds` | `GFX_sp_smallpox_reward_field_testing` | `complete` |

## Prompt and provenance records

- Prompt records: `prompts/imagegen_prompt_records.md`.
- Matching vanilla visual reference sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/special_projects/contact_sheet.png`.
- Vanilla special-project catalog rows: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md` rows for `icons/special_projects`.
- Retained reference conversions used for inspection: `reference_inspection/`.
- SHA-256 records for every processed PNG and final DDS: `hashes/sha256.txt`.
- DDS header and exact RGBA decode validation: `validation/dds_validation.json`.
- Manual visual and safety review: `validation/visual_validation_notes.md`.
- Package-local `.gfx` handoff: `gfx_handoff.md`; parent-agent handoff: `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-22_biological_prototype_reward_icons_handoff.md`.

## Wiring contract

The parent agent should add one `spriteType` per row to the existing `interface/special_projects/biowarfare.gfx` file using the exact sprite names and texture paths listed below. This package deliberately does not edit `.gfx` or the gameplay file.

```text
spriteType = { name = "GFX_sp_anthrax_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_caution.dds" }
spriteType = { name = "GFX_sp_anthrax_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_anthrax_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_plague_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_caution.dds" }
spriteType = { name = "GFX_sp_plague_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_plague_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_caution.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_smallpox_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_caution.dds" }
spriteType = { name = "GFX_sp_smallpox_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_field_testing.dds" }
```
