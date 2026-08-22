# Event 016 reusable alien and D’Rhondan icon package

Status: complete for the locked non-portrait source and counter tranche; parent-owned `.gfx` registration and gameplay consumer review remain separate.

The canonical reference root was the single repository reference family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`. I inspected its decision, decision-category, special-project, technology, and land-counter contact sheets before generation. The installed counter definitions were read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`; the installed vanilla large infantry DDS is 152x42 with two 76x42 frames and the on-map infantry DDS is 60x12 with two 30x12 frames.

Every source below was generated with the official built-in `$imagegen` path. Native transparency was requested and retained for all sources; no background-removal fallback was used. The one predictive-warfare source was initially labelled `native_opaque` because the preview viewer showed black around it, but direct alpha inspection confirmed transparent corners and native alpha, so it was retained without repair. No animation is claimed by this package.

## Locked runtime assets

| Sprite / consumer | Source master | Processed PNG | Final DDS | Size | Status |
| --- | --- | --- | --- | --- | --- |
| `GFX_group_alien_infantry_icon` / `GFX_unit_alien_infantry_icon_medium` | `source_png/alien_infantry_counter_symbol_source.png` | `counter_art/processed_png/unit_alien_infantry_icon.png` | `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` | 152x42, 2x 76x42 | complete |
| `GFX_unit_alien_infantry_icon_medium_white` | same source | `counter_art/processed_png/onmap_unit_alien_infantry_icon.png` | `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds` | 60x12, 2x 30x12 | complete |
| `GFX_alien_laser_weapon_equipment_medium` | `source_png/alien_laser_weapon_equipment_source.png` | `processed_png/alien_laser_weapon_equipment.png` | `gfx/interface/technologies/shared_alien_infantry/alien_laser_weapon_equipment.dds` | 132x52 | complete |
| `GFX_brilliant_scientist_alien_infantry_tech_medium` | `source_png/alien_infantry_technology_source.png` | `processed_png/tech_016_brilliant_scientist_alien_infantry.png` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_infantry.dds` | 132x52 | complete |
| `GFX_brilliant_scientist_alien_predictive_warfare_tech_medium` | `source_png/alien_predictive_warfare_source.png` | `processed_png/tech_016_brilliant_scientist_alien_predictive_warfare.png` | `gfx/interface/technologies/016_brilliant_scientist/tech_016_brilliant_scientist_alien_predictive_warfare.dds` | 132x52 | complete |
| `GFX_tactic_alien_predictive_vector_assault` | `source_png/tactic_alien_predictive_vector_assault_source.png` | `processed_png/tactic_alien_predictive_vector_assault.png` | `gfx/interface/landcombat/tactics/tactic_alien_predictive_vector_assault.dds` | 90x48 | complete |
| `GFX_tactic_alien_probability_screen` | `source_png/tactic_alien_probability_screen_source.png` | `processed_png/tactic_alien_probability_screen.png` | `gfx/interface/landcombat/tactics/tactic_alien_probability_screen.dds` | 90x48 | complete |
| `GFX_sp_dhrondan_envoy_craft` | `source_png/sp_dhrondan_envoy_craft_source.png` | `processed_png/sp_dhrondan_envoy_craft.png` | `gfx/interface/special_project/project_icons/016_brilliant_scientist/sp_dhrondan_envoy_craft.dds` | 161x98 | complete |
| `GFX_decision_send_kruger_to_dhronda` | `source_png/decision_send_kruger_to_dhronda_source.png` | `processed_png/decision_send_kruger_to_dhronda.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_send_kruger_to_dhronda.dds` | 33x32 | complete |
| `GFX_decision_send_mengele_to_dhronda` | `source_png/decision_send_mengele_to_dhronda_source.png` | `processed_png/decision_send_mengele_to_dhronda.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_send_mengele_to_dhronda.dds` | 33x32 | complete |
| `GFX_decision_dhrondan_ufo_landing` | `source_png/decision_dhrondan_ufo_landing_source.png` | `processed_png/decision_dhrondan_ufo_landing.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_ufo_landing.dds` | 33x32 | complete |
| `GFX_decision_honor_dhrondan_accord` | `source_png/decision_honor_dhrondan_accord_source.png` | `processed_png/decision_honor_dhrondan_accord.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_honor_dhrondan_accord.dds` | 33x32 | complete |
| `GFX_decision_category_dhrondan_contact` | `source_png/decision_category_dhrondan_contact_source.png` | `processed_png/decision_category_dhrondan_contact.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_category_dhrondan_contact.dds` | 52x40 | complete |
| `GFX_decision_category_dhrondan_sovereignty` | `source_png/decision_category_dhrondan_sovereignty_source.png` | `processed_png/decision_category_dhrondan_sovereignty.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_category_dhrondan_sovereignty.dds` | 52x40 | complete |
| `GFX_decision_dhrondan_reclamation` | `source_png/decision_dhrondan_reclamation_source.png` | `processed_png/decision_dhrondan_reclamation.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_reclamation.dds` | 33x32 | complete |
| `GFX_decision_dhrondan_enclave_supply` | `source_png/decision_dhrondan_enclave_supply_source.png` | `processed_png/decision_dhrondan_enclave_supply.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_enclave_supply.dds` | 33x32 | complete |
| `GFX_decision_dhrondan_state_integration` | `source_png/decision_dhrondan_state_integration_source.png` | `processed_png/decision_dhrondan_state_integration.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_state_integration.dds` | 33x32 | complete |
| `GFX_decision_dhrondan_two_world_compact` | `source_png/decision_dhrondan_two_world_compact_source.png` | `processed_png/decision_dhrondan_two_world_compact.png` | `gfx/interface/decisions/016_brilliant_scientist/dhrondan/decision_dhrondan_two_world_compact.dds` | 33x32 | complete |
| Event-detail contact/landing/accord/rebellion proposed sprites | matching `source_png/event_dhrondan_*_source.png` | matching `processed_png/event_dhrondan_*.png` | matching DDS under `gfx/interface/decisions/016_brilliant_scientist/dhrondan/` | 33x32 each | complete art; parent token confirmation pending |
| `GFX_goal_KRG_arm_the_alien_cohorts` and `_shine` | `source_png/goal_KRG_arm_the_alien_cohorts_source.png` | `processed_png/goal_KRG_arm_the_alien_cohorts.png` | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_arm_the_alien_cohorts.dds` | 100x88 | complete |
| `GFX_decision_brilliant_scientist_krg_alien_laser_batch` | `source_png/decision_alien_laser_batch_source.png` | `processed_png/decision_alien_laser_batch.png` | `gfx/interface/decisions/016_brilliant_scientist/decisions/decision_alien_laser_batch.dds` | 33x32 | complete |

## Evidence

- `package_records/process_icons.py` records deterministic alpha-preserving processing, vanilla-green counter palette mapping, and original selected-state plate construction.
- `package_records/validate_dds.py` decodes every final DDS, checks one-level uncompressed 32-bit BGRA headers, dimensions, byte lengths, alpha ranges, SHA-256 values, and writes `package_records/dds_validation.json`.
- `contact_sheet/dhrondan_icon_package_contact_sheet.png` is the native-size review sheet with decoded DDS rows and alpha evidence.
- `dds/` contains package-local final copies. Runtime DDS files are installed at the exact paths in the table above.

The existing `016_brilliant_scientist_not_from_here` achievement already has the required completed, grey, and not-eligible triplet. No achievement art was added or replaced, and the Event 016 achievement count remains exactly seventeen.

Focus production for the D’Rhondan tree's remaining 88 requested IDs is not included because no exact DHR focus sprite identifiers appeared in the workspace during this tranche. No focus filename was guessed.

Country-interface emblems and report/news/full-scene art are not included in this icon-only package. Their parent-owned event-art handoff remains the source of truth; no generic fallback or portrait was substituted.
