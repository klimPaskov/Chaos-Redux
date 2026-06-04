# Event 006 Focus Icon Manifest

## Package

- Event: 006 Independence Wave
- Asset type: focus icons
- Source mode: generated HOI4-style focus icon art
- Final size: 94x86 DDS
- Sprite file: `interface/006_independence_wave_icons.gfx`
- Final DDS folder: `gfx/interface/goals/independence_wave/`
- Source PNG folder: `docs/assets/006_independence_wave/focus_icons/source_png/`
- Processed PNG folder: `docs/assets/006_independence_wave/focus_icons/processed_png/`
- Contact sheet: `docs/assets/006_independence_wave/focus_icons/contact_sheets/focus_icons_contact_sheet.png`
- Reuse ledger: `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`

## Notes

This package gives the Event 006 focus tree a coherent non-flag visual family without using Event 005 focus art or country flag assets. Every final sprite in this package is now backed by its own generated source crop rather than a reused simple placeholder, while the focus tree may still reuse a branch-level sprite where the same governing desk, survival board, formation ledger, congress track, or strange-route bureau is intentionally represented.

The regenerated sheets were created after inspecting the repository focus and idea icon reference folders. Final icons use transparent HOI4-style silhouettes, painted objects, outlines, laurels, and period administrative/military props instead of dark rectangular cards or primitive shapes.

## Sprite Inventory

| Sprite | Final DDS | Source note | Status |
| --- | --- | --- | --- |
| `GFX_focus_independence_wave_dossier_count` | `gfx/interface/goals/independence_wave/goal_independence_wave_dossier_count.dds` | Derived from Event006 dossier category art | wired |
| `GFX_focus_independence_wave_provisional_council` | `gfx/interface/goals/independence_wave/goal_independence_wave_provisional_council.dds` | Derived from provisional committee idea art | wired |
| `GFX_focus_independence_wave_barracks` | `gfx/interface/goals/independence_wave/goal_independence_wave_barracks.dds` | Derived from loyalist decision art | wired |
| `GFX_focus_independence_wave_emergency_budget` | `gfx/interface/goals/independence_wave/goal_independence_wave_emergency_budget.dds` | Derived from patron ledger category art | wired |
| `GFX_focus_independence_wave_recognition_desk` | `gfx/interface/goals/independence_wave/goal_independence_wave_recognition_desk.dds` | Derived from recognition mission decision art | wired |
| `GFX_focus_independence_wave_observer_charter` | `gfx/interface/goals/independence_wave/goal_independence_wave_observer_charter.dds` | Derived from observer decision art | wired |
| `GFX_focus_independence_wave_officer_mandate` | `gfx/interface/goals/independence_wave/goal_independence_wave_officer_mandate.dds` | Derived from officer mandate idea art | wired |
| `GFX_focus_independence_wave_national_directory` | `gfx/interface/goals/independence_wave/goal_independence_wave_national_directory.dds` | Derived from national directorate idea art | wired |
| `GFX_focus_independence_wave_sponsored_cabinet` | `gfx/interface/goals/independence_wave/goal_independence_wave_sponsored_cabinet.dds` | Derived from patron cabinet idea art | wired |
| `GFX_focus_independence_wave_revolutionary_committee` | `gfx/interface/goals/independence_wave/goal_independence_wave_revolutionary_committee.dds` | Derived from revolutionary committee idea art | wired |
| `GFX_focus_independence_wave_military_supply` | `gfx/interface/goals/independence_wave/goal_independence_wave_military_supply.dds` | Derived from guard depot decision art | wired |
| `GFX_focus_independence_wave_railway_yard` | `gfx/interface/goals/independence_wave/goal_independence_wave_railway_yard.dds` | Derived from railway timetable decision art | wired |
| `GFX_focus_independence_wave_municipal_workshops` | `gfx/interface/goals/independence_wave/goal_independence_wave_municipal_workshops.dds` | Derived from committee survival category art | wired |
| `GFX_focus_independence_wave_port_ledger` | `gfx/interface/goals/independence_wave/goal_independence_wave_port_ledger.dds` | Derived from patronage recognition category art | wired |
| `GFX_focus_independence_wave_border_commission` | `gfx/interface/goals/independence_wave/goal_independence_wave_border_commission.dds` | Derived from border commission category art | wired |
| `GFX_focus_independence_wave_patron_balance` | `gfx/interface/goals/independence_wave/goal_independence_wave_patron_balance.dds` | Derived from patron advisers decision art | wired |
| `GFX_focus_independence_wave_congress_delegation` | `gfx/interface/goals/independence_wave/goal_independence_wave_congress_delegation.dds` | Derived from congress category art | wired |
| `GFX_focus_independence_wave_league_charter` | `gfx/interface/goals/independence_wave/goal_independence_wave_league_charter.dds` | Derived from league charter decision art | wired |
| `GFX_focus_independence_wave_archive_identity` | `gfx/interface/goals/independence_wave/goal_independence_wave_archive_identity.dds` | Derived from archive claim decision art | wired |
| `GFX_focus_independence_wave_old_name_council` | `gfx/interface/goals/independence_wave/goal_independence_wave_old_name_council.dds` | Derived from Volga old-state idea art | wired |
| `GFX_focus_independence_wave_local_land_council` | `gfx/interface/goals/independence_wave/goal_independence_wave_local_land_council.dds` | Derived from local land council decision art | wired |
| `GFX_focus_independence_wave_free_city_board` | `gfx/interface/goals/independence_wave/goal_independence_wave_free_city_board.dds` | Derived from free city board idea art | wired |
| `GFX_focus_independence_wave_sealed_bureau` | `gfx/interface/goals/independence_wave/goal_independence_wave_sealed_bureau.dds` | Derived from sealed dossier category art | wired |
| `GFX_focus_independence_wave_registry_absence` | `gfx/interface/goals/independence_wave/goal_independence_wave_registry_absence.dds` | Derived from occult registry decision art | wired |
| `GFX_focus_independence_wave_formation_ledger` | `gfx/interface/goals/independence_wave/goal_independence_wave_formation_ledger.dds` | Derived from formations category art | wired |

## Validation

- Focus references in `common/national_focus/006_independence_wave_focus.txt`: 123.
- Event006 focus sprites registered in `interface/006_independence_wave_icons.gfx`: 25.
- Final DDS files present: 25, all 94x86 with alpha.
- Processed PNG previews present: 25, all 94x86 with transparent unused canvas.
- No country flag assets are part of this package.
