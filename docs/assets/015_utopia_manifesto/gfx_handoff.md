# Event 015 Current GFX Handoff

Snapshot: `2026-07-16`

Status: **PASS - current runtime wiring is complete.**

## Registry truth

| Surface | Result |
| --- | --- |
| `interface/015_utopia_manifesto.gfx` | `459` unique definitions, duplicate names `0` |
| `interface/015_utopia_manifesto_super_event.gfx` | `5` unique route-super-event definitions |
| Combined | `464` unique definitions, cross-file duplicate names `0` |
| `interface/015_utopia_manifesto_ledger.gui` | `46` unique sprite references, unresolved references `0` |
| `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | exact visibility/state bindings for live Ledger elements |

The Event 015 decision category attaches `utopia_manifesto_ledger_scripted_gui`; the four panels are controlled by the Overview, Callings, Stores/Settlements, and Necessary Ground tab flags.

## Live repaired Ledger statics

| Family | Sprite/consumer contract | Live layout and state |
| --- | --- | --- |
| Values | `GFX_utopia_ledger_value_need`, `_plenty`, `_concord`, `_balance` | Four distinct `32x32` icons at root `(30,104)`, `(194,104)`, `(358,104)`, `(522,104)`; live score text sits beside each icon |
| Callings | `GFX_utopia_ledger_calling_provisioning`, `_workshops`, `_civic_works`, `_learning_and_care`, `_maritime_and_settlement`, `_defense_and_watches` | Six `48x48` icons, scaled `0.75`, at panel-relative x `280` or `606` and y `4`, `74`, `144`; visible with `utopia_ledger_callings_panel` |
| Case cards | `GFX_utopia_ledger_case_*` for ten exact states | Ten `300x96` consumers share `(8,4)` in `utopia_ledger_ground_panel`; scripted visibility is mutually exclusive across no target, eligible, selected, pending, counteroffer, refusal, ultimatum, expired, stewardship, and associate |
| District roles | `GFX_utopia_ledger_district_role_*` for seven exact roles | Seven `300x96` consumers share `(334,4)` in **`utopia_ledger_stores_panel` (Stores/Settlements tab)**; `utopia_manifesto_district_visual_role` binds all seven constants |
| District states | `GFX_utopia_ledger_district_state_*` for six exact states | Six `48x48` overlays share `(578,12)` in the same Stores/Settlements panel; surveyed, planned, building, blocked, complete, and disputed use exact phase/flag priority |

The planned District state is not an alias: `utopia_manifesto_district_plan_committed_recent` is set for `constant:utopia_manifesto_durations.district_plan_card_days` (`7` days) when a plan is committed and is cleared by terminal cleanup. Port town, research town, and Inland Island ring have explicit durable role assignments; they do not reuse another role card.

## Live animation wiring

| Animation | Registered sprites | GUI consumer | Runtime state |
| --- | --- | --- | --- |
| Ledger seal, `8` frames, `64x64`, `12 fps`, loop | `GFX_utopia_ledger_seal_{static,animated}` | `utopia_ledger_seal` at `(18,16)` | visible until one of five identity-emblem flags selects a route emblem |
| Need warning, `8`, `64x64`, `5 fps`, loop | `GFX_utopia_need_warning_{static,animated}` | `utopia_ledger_need_warning` at `(24,430)` | high Need, low Plenty, or constitutional crisis |
| Reserve fill, `8`, `300x24`, `4 fps`, loop | `GFX_utopia_reserve_fill_{static,animated}` | `utopia_ledger_reserve_fill` at Stores-panel `(8,12)` | `utopia_reserve_band` exists; extra presentation animation, not an accepted-row substitute |
| Toward Choice, `8`, `158x24`, `5 fps`, no loop | `GFX_utopia_balance_to_choice_{static,animated}` | `utopia_ledger_balance_to_choice` at `(516,70)` | route-resolved Assignment-band crossing downward; three-day direction flag |
| Toward Assignment, `8`, `158x24`, `5 fps`, no loop | `GFX_utopia_balance_to_assignment_{static,animated}` | `utopia_ledger_balance_to_assignment` at `(516,70)` | route-resolved Assignment-band crossing upward; three-day direction flag |
| Formation-ready, `10`, `96x96`, `5 fps`, loop | `GFX_utopia_formation_ready_seal_{static,animated}` | `utopia_ledger_formation_ready_seal` at `(610,0)`, scale `0.72` | current route can form and commonwealth is not formed |

All animated definitions use sheet DDS paths, exact `noOfFrames`, `play_on_show = yes`, and the audited loop setting. Static fallbacks are registered. First-refresh suppression, opposite balance-flag clearing, and terminal cleanup are present; no daily, weekly, or monthly scan drives the balance animations.

## Other live registrations

- Reports/news: all `14` report and `3` news sprites are registered in `015_utopia_manifesto.gfx` and consumed by Event 015 events.
- Route super-events: five `457x328` sprites are registered separately and selected by scripted-localisation slots `96`-`100`.
- Focuses: `74` live base sprites plus matching shine registrations cover `124` focus uses.
- Decisions/categories/missions: `174` mapping rows resolve to live `32x32` registrations, covering `9` categories, `121` decisions, and `44` missions. `165` gameplay assignments are present. Current mapping authority is `decision_icon_mapping.csv`.
- Ideas: `12` registered pictures cover `50` entries.
- Achievements: `42` current base/grey/not-eligible variants are registered.
- Institutional characters: four `156x210` people-free tableau sprites serve eight leader entries.
- Advisors: sixteen `65x67` dossier sprites serve sixteen advisor entries.
- League emblems: five `64x64` sprites occupy the header position and use five exact route flags.
- Flags: no GFX registration is required; `25` filenames at three engine sizes provide `75` TGAs.

## Completion gate

The previous Values, Callings, Case-card, and District-card P2 gaps are resolved. No reserved-but-unimplemented name remains in this handoff. Simplifications, omissions, fallbacks, and open blockers: none.

## Historical event-picture handoff (already integrated; superseded)

The older instructions below are retained only as package history. Every referenced report/news registration and consumer is already integrated; do not re-add duplicate blocks.

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
