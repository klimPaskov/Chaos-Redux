# Event 015 Utopian Manifesto GFX handoff

## Event pictures

The final package installs these exact runtime identities under `gfx/event_pictures/015_utopia_manifesto/`:

- Reports: `found`, `ledger`, `calling`, `store`, `settlement`, `island`, `defense`, `foreign_commonwealth`, `necessary_ground`, `stewardship`, `league`, `formation`, `contradiction`, and `evolution`.
- News: `league`, `necessary_ground_war`, and `colony_revolt`.

Target registry: `interface/015_utopia_manifesto.gfx`. That shared file was deliberately not edited by the final non-icon asset pass. `GFX_report_event_utopia_manifesto_found` already exists there and must not be duplicated. Add the following missing blocks inside its existing `spriteTypes = { ... }` block:

```txt
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_ledger"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_ledger.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_calling"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_calling.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_store"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_store.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_settlement"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_settlement.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_island"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_island.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_defense"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_defense.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_foreign_commonwealth"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_foreign_commonwealth.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_necessary_ground"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_necessary_ground.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_stewardship"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_stewardship.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_league"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_league.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_formation"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_formation.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_contradiction"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_contradiction.dds"
	}
	spriteType = {
		name = "GFX_report_event_utopia_manifesto_evolution"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_evolution.dds"
	}
	spriteType = {
		name = "GFX_news_event_utopia_manifesto_league"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_league.dds"
	}
	spriteType = {
		name = "GFX_news_event_utopia_manifesto_necessary_ground_war"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_necessary_ground_war.dds"
	}
	spriteType = {
		name = "GFX_news_event_utopia_manifesto_colony_revolt"
		texturefile = "gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_colony_revolt.dds"
	}
```

Script alignment required in the parent integration pass:

- Replace the current `GFX_report_event_utopia_manifesto_military` picture references with `GFX_report_event_utopia_manifesto_defense`; the final package intentionally uses the requested `defense` identity and does not provide a duplicate alias.
- Assign `GFX_report_event_utopia_manifesto_island`, `GFX_report_event_utopia_manifesto_foreign_commonwealth`, and `GFX_report_event_utopia_manifesto_formation` to their intended event families. Their final art exists, but these three identities were not referenced by the event script at asset handoff time.
- The older `GFX_news_event_utopia_boundary_crisis` asset remains a separate legacy picture and is not a substitute for any of the three final news identities.

## Super-events

The five current route images are complete and already registered by `interface/015_utopia_manifesto_super_event.gfx`; no registration edit is required:

- `GFX_super_event_015_consent_of_households` -> `gfx/super_events/015_utopia_manifesto/super_event_015_consent_of_households.dds`
- `GFX_super_event_015_common_table` -> `gfx/super_events/015_utopia_manifesto/super_event_015_common_table.dds`
- `GFX_super_event_015_guardians_of_measure` -> `gfx/super_events/015_utopia_manifesto/super_event_015_guardians_of_measure.dds`
- `GFX_super_event_015_closed_island` -> `gfx/super_events/015_utopia_manifesto/super_event_015_closed_island.dds`
- `GFX_super_event_015_joke_understood` -> `gfx/super_events/015_utopia_manifesto/super_event_015_joke_understood.dds`

The two entries below are retained legacy super-event art and are not fallbacks for the route-specific package.

- Final DDS path: `gfx/super_events/015_utopia_manifesto/super_event_utopia_new_utopia.dds`
- Proposed sprite name: `GFX_super_event_utopia_new_utopia`
- Suggested `.gfx` file: `interface/chaosx_super_events.gfx`
- Related use: Event 015 New Utopia proclamation super-event

- Final DDS path: `gfx/super_events/015_utopia_manifesto/super_event_utopia_marked_bounds.dds`
- Proposed sprite name: `GFX_super_event_utopia_marked_bounds`
- Suggested `.gfx` file: `interface/chaosx_super_events.gfx`
- Related use: Event 015 Marked Bounds doctrine super-event

## Scripted GUI pack

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_ledger_background_panel.dds`
- Proposed sprite name: `GFX_utopia_ledger_background_panel`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: base decorative background for the Utopian Ledger scripted GUI

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_ledger_header_plate.dds`
- Proposed sprite name: `GFX_utopia_ledger_header_plate`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: static top plate for the Utopian Ledger scripted GUI

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_ledger_warning_panel.dds`
- Proposed sprite name: `GFX_utopia_ledger_warning_panel`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: warning-state panel for Overreach or Marked Bounds copy blocks

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_ledger_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_ledger_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated Ledger seal in `interface/015_utopia_manifesto_ledger.gui`

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_overreach_warning_sheet.dds`
- Runtime sprite name: `GFX_utopia_overreach_warning_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: retained legacy animation; registered but not referenced by the current Ledger GUI

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_storehouse_fill_sheet.dds`
- Runtime sprite name: `GFX_utopia_storehouse_fill_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: retained legacy animation; registered but not referenced by the current Ledger GUI

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_new_utopia_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_new_utopia_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: retained legacy animation; registered but not referenced by the current Ledger GUI

- Final DDS path: `gfx/interface/015_utopia_manifesto/utopia_marked_bounds_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_marked_bounds_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: retained legacy animation; registered but not referenced by the current Ledger GUI

- Final DDS paths: `gfx/interface/015_utopia_manifesto/utopia_need_warning_{static,sheet}.dds`
- Runtime sprite names: `GFX_utopia_need_warning_static`, `GFX_utopia_need_warning_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: eight-frame live Need/crisis warning in `interface/015_utopia_manifesto_ledger.gui`

- Final DDS paths: `gfx/interface/015_utopia_manifesto/utopia_reserve_fill_{static,sheet}.dds`
- Runtime sprite names: `GFX_utopia_reserve_fill_static`, `GFX_utopia_reserve_fill_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: eight-frame live public-reserve meter in `interface/015_utopia_manifesto_ledger.gui`

- Final DDS paths: `gfx/interface/015_utopia_manifesto/utopia_formation_ready_seal_{static,sheet}.dds`
- Runtime sprite names: `GFX_utopia_formation_ready_seal_static`, `GFX_utopia_formation_ready_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: ten-frame live formation-ready seal in `interface/015_utopia_manifesto_ledger.gui`

## Implementation notes

- General Event 015 runtime registration lives in `interface/015_utopia_manifesto.gfx`; the current five route super-event sprites live in `interface/015_utopia_manifesto_super_event.gfx`.
- The final report/news DDS package is complete, but its `13` missing report blocks and `3` news blocks remain the explicit parent registration task given above. The existing `found` block must be retained rather than duplicated.
- Legacy super-event pictures, focus icons, decision icons, idea icons, explicit achievement aliases, static GUI art, and animated GUI sheets are registered through the general Event 015 sprite file.
- The Utopian Ledger GUI uses `interface/015_utopia_manifesto_ledger.gui` and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`.
- The runtime texture root is `gfx/interface/015_utopia_manifesto/`. The current GUI references the Ledger seal plus the Need warning, reserve fill, and formation-ready seal; the four older route/value animation sequences remain registered legacy assets.
- Exact decision/category/mission assignments are documented in `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`; gameplay `icon =` fields remain a parent integration task.
