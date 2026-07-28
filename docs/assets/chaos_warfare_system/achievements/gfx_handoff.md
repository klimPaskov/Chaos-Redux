# Chaos Warfare achievement icon GFX handoff

Status: complete for asset production; parent-owned gameplay and GFX registration remain separate.

## Runtime contract

- Final DDS folder: `gfx/achievements/`.
- Final size: exact `64x64` for every completed, grey, and not-eligible variant.
- Encoding: one-level uncompressed BGRA DDS with real alpha and no mip chain.
- Target registration file: `interface/chaosx_achievements.gfx`.
- Completed sprite: `GFX_achievement_<achievement_id>`.
- Grey sprite: `GFX_achievement_<achievement_id>_grey`.
- Not-eligible sprite: `GFX_achievement_<achievement_id>_not_eligible`.
- Not-eligible treatment: mechanically grayscale-derived base plus the canonical red-X overlay at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`.

## Exact handoff rows

| Achievement ID | Completed DDS | Grey DDS | Not-eligible DDS | Sprite triplet |
| --- | --- | --- | --- | --- |
| `chaos_warfare_air_still_breathable` | `gfx/achievements/chaos_warfare_air_still_breathable.dds` | `gfx/achievements/chaos_warfare_air_still_breathable_grey.dds` | `gfx/achievements/chaos_warfare_air_still_breathable_not_eligible.dds` | `GFX_achievement_chaos_warfare_air_still_breathable{,_grey,_not_eligible}` |
| `chaos_warfare_masks_before_guns` | `gfx/achievements/chaos_warfare_masks_before_guns.dds` | `gfx/achievements/chaos_warfare_masks_before_guns_grey.dds` | `gfx/achievements/chaos_warfare_masks_before_guns_not_eligible.dds` | `GFX_achievement_chaos_warfare_masks_before_guns{,_grey,_not_eligible}` |
| `chaos_warfare_prepared_army` | `gfx/achievements/chaos_warfare_prepared_army.dds` | `gfx/achievements/chaos_warfare_prepared_army_grey.dds` | `gfx/achievements/chaos_warfare_prepared_army_not_eligible.dds` | `GFX_achievement_chaos_warfare_prepared_army{,_grey,_not_eligible}` |
| `chaos_warfare_poisoned_victory` | `gfx/achievements/chaos_warfare_poisoned_victory.dds` | `gfx/achievements/chaos_warfare_poisoned_victory_grey.dds` | `gfx/achievements/chaos_warfare_poisoned_victory_not_eligible.dds` | `GFX_achievement_chaos_warfare_poisoned_victory{,_grey,_not_eligible}` |
| `chaos_warfare_clean_hands_dirty_work` | `gfx/achievements/chaos_warfare_clean_hands_dirty_work.dds` | `gfx/achievements/chaos_warfare_clean_hands_dirty_work_grey.dds` | `gfx/achievements/chaos_warfare_clean_hands_dirty_work_not_eligible.dds` | `GFX_achievement_chaos_warfare_clean_hands_dirty_work{,_grey,_not_eligible}` |
| `chaos_warfare_evidence_survives` | `gfx/achievements/chaos_warfare_evidence_survives.dds` | `gfx/achievements/chaos_warfare_evidence_survives_grey.dds` | `gfx/achievements/chaos_warfare_evidence_survives_not_eligible.dds` | `GFX_achievement_chaos_warfare_evidence_survives{,_grey,_not_eligible}` |
| `chaos_warfare_no_wind_is_friendly` | `gfx/achievements/chaos_warfare_no_wind_is_friendly.dds` | `gfx/achievements/chaos_warfare_no_wind_is_friendly_grey.dds` | `gfx/achievements/chaos_warfare_no_wind_is_friendly_not_eligible.dds` | `GFX_achievement_chaos_warfare_no_wind_is_friendly{,_grey,_not_eligible}` |
| `chaos_warfare_antidote_arrived` | `gfx/achievements/chaos_warfare_antidote_arrived.dds` | `gfx/achievements/chaos_warfare_antidote_arrived_grey.dds` | `gfx/achievements/chaos_warfare_antidote_arrived_not_eligible.dds` | `GFX_achievement_chaos_warfare_antidote_arrived{,_grey,_not_eligible}` |
| `chaos_warfare_quarantine_without_collapse` | `gfx/achievements/chaos_warfare_quarantine_without_collapse.dds` | `gfx/achievements/chaos_warfare_quarantine_without_collapse_grey.dds` | `gfx/achievements/chaos_warfare_quarantine_without_collapse_not_eligible.dds` | `GFX_achievement_chaos_warfare_quarantine_without_collapse{,_grey,_not_eligible}` |
| `chaos_warfare_arsenal_dismantled` | `gfx/achievements/chaos_warfare_arsenal_dismantled.dds` | `gfx/achievements/chaos_warfare_arsenal_dismantled_grey.dds` | `gfx/achievements/chaos_warfare_arsenal_dismantled_not_eligible.dds` | `GFX_achievement_chaos_warfare_arsenal_dismantled{,_grey,_not_eligible}` |
| `chaos_warfare_terminal_contagion` | `gfx/achievements/chaos_warfare_terminal_contagion.dds` | `gfx/achievements/chaos_warfare_terminal_contagion_grey.dds` | `gfx/achievements/chaos_warfare_terminal_contagion_not_eligible.dds` | `GFX_achievement_chaos_warfare_terminal_contagion{,_grey,_not_eligible}` |
| `chaos_warfare_mask_for_every_door` | `gfx/achievements/chaos_warfare_mask_for_every_door.dds` | `gfx/achievements/chaos_warfare_mask_for_every_door_grey.dds` | `gfx/achievements/chaos_warfare_mask_for_every_door_not_eligible.dds` | `GFX_achievement_chaos_warfare_mask_for_every_door{,_grey,_not_eligible}` |
| `chaos_warfare_weapon_turns_home` | `gfx/achievements/chaos_warfare_weapon_turns_home.dds` | `gfx/achievements/chaos_warfare_weapon_turns_home_grey.dds` | `gfx/achievements/chaos_warfare_weapon_turns_home_not_eligible.dds` | `GFX_achievement_chaos_warfare_weapon_turns_home{,_grey,_not_eligible}` |
| `chaos_warfare_unbroken_supply_corridor` | `gfx/achievements/chaos_warfare_unbroken_supply_corridor.dds` | `gfx/achievements/chaos_warfare_unbroken_supply_corridor_grey.dds` | `gfx/achievements/chaos_warfare_unbroken_supply_corridor_not_eligible.dds` | `GFX_achievement_chaos_warfare_unbroken_supply_corridor{,_grey,_not_eligible}` |
| `chaos_warfare_first_user_pays` | `gfx/achievements/chaos_warfare_first_user_pays.dds` | `gfx/achievements/chaos_warfare_first_user_pays_grey.dds` | `gfx/achievements/chaos_warfare_first_user_pays_not_eligible.dds` | `GFX_achievement_chaos_warfare_first_user_pays{,_grey,_not_eligible}` |

## Evidence and validation

- Source masters: `docs/assets/chaos_warfare_system/achievements/source_png/`.
- Chroma-key alpha masters and byte-preserved archives: `docs/assets/chaos_warfare_system/achievements/archive/`.
- Exact processed previews: `docs/assets/chaos_warfare_system/achievements/processed_png/`.
- Prompt and provenance ledger: `docs/assets/chaos_warfare_system/achievements/prompts/achievement_generation_ledger.md`.
- Manifest with every variant, path, sprite, status, and SHA-256: `docs/assets/chaos_warfare_system/achievements/manifest/achievement_manifest.json`.
- Per-variant validation and hashes: `docs/assets/chaos_warfare_system/achievements/validation/achievement_icon_validation.tsv`.
- Summary validation report: `docs/assets/chaos_warfare_system/achievements/validation/validation_report.json`.
- Review contact sheet: `docs/assets/chaos_warfare_system/achievements/contact_sheets/achievement_triplets_contact_sheet.png`.

Validation result: 15 achievement identities, 45 PNG variants, 45 DDS variants, 15 unique completed processed masters, all exact `64x64`, all DDS pixel-identical to their processed PNG, no visible key-color pixels, grey variants monochrome, and red-X not-eligible variants present.

No `.gfx`, gameplay, localisation, GUI, achievement registry, or spreadsheet file was edited in this asset-only tranche.
