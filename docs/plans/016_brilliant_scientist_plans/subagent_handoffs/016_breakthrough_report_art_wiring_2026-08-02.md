# Event 016 family-specific breakthrough report-art wiring handoff

Date: 2026-08-02

## Scope

This bounded non-model tranche promotes the two existing family-specific first-Prototype report masters and routes them through the shared `chaosx.nr16.6` report. It does not add an evolution, project reward, project family, decision, mission, country, focus, unit, model, or new event fire path.

## Runtime assets and consumers

| Runtime DDS | Sprite | Picture branch |
| --- | --- | --- |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_breakthrough_computation_electronics.dds` | `GFX_report_event_016_brilliant_scientist_breakthrough_computation_electronics` | Computation and Electronics |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_breakthrough_materials_rocketry.dds` | `GFX_report_event_016_brilliant_scientist_breakthrough_materials_rocketry` | Advanced Materials and Rocketry |

The source masters remain in the ignored asset workspace under `docs/assets/016_brilliant_scientist/report_news_expansion/source_masters/report/`. Both processed previews and evidence DDS files are retained there. Runtime DDS files are `210x176` uncompressed 32-bit BGRA with the existing Event 016 report header contract and exact size `147968` bytes.

## Script routing

`GetBrilliantScientistBreakthroughPicture` in `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` reads the already-persistent `brilliant_scientist_last_breakthrough_project_family` value. The computation or electronics branch returns the machine-room sprite, the materials or rocketry branch returns the guarded ordnance-workshop sprite, and the safe default returns `GFX_report_event_016_brilliant_scientist_directorate_dossier` for every other family. `events/016_brilliant_scientist_directorate_outcomes.txt` uses `picture = "[GetBrilliantScientistBreakthroughPicture]"` only on `chaosx.nr16.6`; `.10` and `.11` retain their existing dossier-specific pictures.

## Ownership and validation

The parent owns the `.gfx` registration, scripted-localisation routing, event picture assignment, documentation, and final checks. The two scenes were visually reviewed at native `210x176` size. Both runtime DDS headers were checked for width, height, uncompressed BGRA masks, 32-bit pixels, and exact payload length. The offline Event Inspector was run against `chaosx.nr16.6`; it returned `status=ok`, `EVENT_INSPECTED_PARTIAL`, and no blockers, with the documented workspace-wide helper/lifecycle analysis deferral.

## Remaining art boundary

Qualifying defeat and project-remnant report variants remain queued because they require distinct aftermath consumers and should not be substituted into the existing defeat or terminal surfaces without a reviewed trigger contract.
