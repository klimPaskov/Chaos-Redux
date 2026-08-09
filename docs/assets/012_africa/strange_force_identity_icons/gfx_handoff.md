# Event 012 strange-force identity icon GFX handoff

This package supplies eight static identity families and accepts the existing sixteen vanilla-green custom counter DDS surfaces from the per-unit counter manifests. No gameplay or `.gfx` file was edited by this handoff; the parent agent owns final registration and promotion.

## Runtime texture roots

| Surface | Runtime root | Target size | Sprite ID pattern |
| --- | --- | --- | --- |
| Technology | `gfx/interface/technologies/012_africa/` | 64x64 | `GFX_tech_012_africa_<unit>` |
| Decision | `gfx/interface/decisions/012_africa/` | 32x32 | `GFX_decision_012_africa_<unit>` |
| Focus/goal | `gfx/interface/goals/012_africa/` | 94x86 | `GFX_goal_012_africa_<unit>` |
| Division emblem large | `gfx/interface/division_template_emblems/012_africa/` | 76x42 | `GFX_division_emblem_012_africa_<unit>` |
| Division emblem small | `gfx/interface/division_template_emblems/012_africa/` | 30x12 | `GFX_division_emblem_012_africa_<unit>_small` |
| Large counter | `gfx/interface/counters/divisions_large/` | 152x42 canvas, 76x42 frames | `GFX_unit_<unit>_icon_medium` |
| On-map counter | `gfx/interface/counters/divisions_small/` | 60x12 canvas, 30x12 frames | `GFX_unit_<unit>_icon_medium_white` |

Replace `<unit>` with `gorilla_heavy_infantry`, `pan_sappers`, `stone_cohorts`, `riverborn`, `forest_giants`, `oracle_recon`, `disaster_wardens`, or `plague_carriers`.

Technology DDS filenames are `tech_012_africa_<unit>.dds`. Decision DDS filenames are `decision_012_africa_<unit>.dds`. Goal DDS filenames are `goal_012_africa_<unit>.dds`. Large emblem DDS filenames are `division_emblem_012_africa_<unit>.dds`, while small emblem DDS filenames add `_small.dds`.

The proposed parent-owned registration target is `interface/012_africa_strange_force_icons.gfx`. Existing counter registrations are in `interface/012_africa_strange_force_counters.gfx`; that file already contains the base counter sprite IDs for all eight units and the `GFX_unit_chaosx_<unit>_icon_medium` aliases for Gorilla, Pan, Stone, Forest, and Oracle where present.

## Consumer crosswalk

| Unit | Gameplay/entity token | Route or action consumer | Dedicated decision status |
| --- | --- | --- | --- |
| Gorilla Heavy Infantry | `chaosx_gorilla_heavy_infantry` | Action 75 `train_gorilla_heavy_infantry` | `africa_select_train_gorilla_heavy_infantry` |
| Pan Sappers | `chaosx_pan_sappers` | Action 76 `organise_pan_sappers` | `africa_select_organise_pan_sappers` |
| Stone Cohorts | `chaosx_stone_cohorts` | Action 74 `awaken_stone_cohort` | `africa_select_awaken_stone_cohort` |
| Riverborn | `riverborn` | Covenant route node 10 with overlay-active gate | `africa_select_expand_river_transport` route context |
| Forest Giants | `chaosx_forest_giants` | Action 68 bounded Green compact result | No dedicated decision found; reserved package surface |
| Oracle Recon | `chaosx_oracle_recon` | Action 67 `consult_oracle_network` | `africa_select_consult_oracle_network` |
| Disaster Wardens | `disaster_wardens` | Natural-disaster bridge Actions 69/70 | No dedicated decision found; reserved package surface |
| Plague Carriers | `plague_carriers` | Action 73 full route | No dedicated decision found; reserved package surface |

The hidden technology consumer for each unit is `africa_<unit>_tech`, and the equipment consumer is `africa_<unit>_equipment_1`. No direct focus icon ID is currently wired for these package surfaces; focus sprites remain reserved for parent-owned integration.

## Evidence

`manifest.json` records source, processed, alpha-intermediate, decoded, DDS header, SHA-256, dimensions, alpha extrema, and pixel round-trip evidence for every identity surface. The four contact sheets in this directory provide source/processed and counter visual review. Counter palette and frame behavior are inherited only from the inspected vanilla references and are documented in each per-unit counter manifest under `docs/assets/012_africa/models_3d/<unit>/counters/`.
