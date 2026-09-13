# Implementation Architecture and File Map

## Status of identifiers

Identifiers in this file are proposed. The implementation agent must inspect the live repository for collisions, current folder conventions, and existing Event 51 remnants before creating or renaming files.

## Event namespace

- Entry event: `chaosx.nr51.1`
- Follow-up events: same `chaosx.nr51.*` namespace
- Reports, hidden pulses, surge events, evolution events, and recovery events should use a documented internal ID map
- Keep existing IDs stable when a current Event 51 chain already occupies them

## Proposed event files

- `events/051_heat_wave_events.txt`
- optional separate report file only if the repository's event loading and documentation conventions support splitting the namespace cleanly

The event file should include an overview comment that maps ID ranges to entry, reports, lifecycle, evolution, recovery, and hidden processing.

## Script constants

Proposed file:

- `common/script_constants/051_heat_wave_constants.txt`

Constant families:

- public intensity thresholds
- state stress thresholds and recovery hysteresis
- lifecycle duration bands
- pulse intervals
- surge gaps and caps
- regional amplification caps
- exposure thresholds
- mortality confirmation and caps
- building-damage confirmation and caps
- environmental degradation thresholds and caps
- decision cost anchors
- mission durations
- AI score anchors
- Chaos milestone values
- report cooldowns
- achievement thresholds

Use `constant:category.key` access where supported. Fields that reject constants should receive values through variables following the repository rules.

## Event-owned scripted triggers

Proposed file:

- `common/scripted_triggers/051_heat_wave_triggers.txt`

Trigger families:

- event entry eligibility
- valid normal civilian country
- valid heat state
- state environmental family
- state agricultural role
- state industrial role
- state military hotspot
- water-pressure stage
- stress-band checks
- exposure confirmation
- mortality eligibility
- wildfire request eligibility
- Famine request eligibility
- Migration request eligibility
- environmental warning and degradation eligibility
- critical corridor validity
- decision target validity
- mission success, partial success, and failure
- recovery and cleanup readiness
- achievement conditions

Triggers should be read-only and fail closed when proof is incomplete.

## Event-owned scripted effects

Suggested files:

- `common/scripted_effects/051_heat_wave_lifecycle_effects.txt`
- `common/scripted_effects/051_heat_wave_state_effects.txt`
- `common/scripted_effects/051_heat_wave_response_effects.txt`
- `common/scripted_effects/051_heat_wave_adapter_effects.txt`
- `common/scripted_effects/051_heat_wave_presentation_effects.txt`

### Lifecycle effects

- initialize new episode generation
- roll opening profile
- register valid countries and states
- process global intensity pulse
- start and end surge
- start and end regional amplification
- transition phases
- start recovery
- run idempotent cleanup

### State effects

- calculate cached vulnerability
- calculate target Heat Stress
- apply band modifier
- update trend and hysteresis
- accumulate exposure
- process water, agriculture, military, industry, and environmental consequences
- register and remove urgent states
- rebuild hotspots

### Response effects

- select and change national priority
- apply state mitigation
- start decisions and missions
- process success, partial success, failure, cancellation, and cleanup
- debit supported stockpiles through existing helpers

### Adapter effects

- build and submit Event 013 request
- build and submit Famine request
- build and submit Migration request
- apply exact civilian loss
- submit military casualty transaction
- publish and consume versioned facts
- clear request proofs and results

### Presentation effects

- record event and evolution logs
- set Event Details state
- select reports
- update last-episode summary
- trigger Evolution III super-event request
- record achievements

## Shared dynamic effects

Reuse current helpers before adding any shared helper.

Expected reuse:

- `call_natural_disaster`
- `apply_exact_state_civilian_population_loss`
- `apply_state_population_loss_without_recruitable_manpower_gain`
- stockpile debit helpers

A new helper belongs in `chaosx_dynamic_effects` only if it is neutral and useful across several systems. Document purpose, scope, inputs, outputs, defaults, side effects, and example in the same change.

## Shared classifiers

Use:

- `is_desert_state`
- `is_special_chaos_country`
- `is_actual_nonhuman_country`
- `uses_normal_civilian_systems`

Do not add Event 51 lifecycle or eligibility to the shared classifier registry.

## On-actions and runtime hooks

Proposed event-owned file:

- `common/on_actions/051_heat_wave_on_actions.txt`

The implementation should prefer delayed event pulses or narrow registered callbacks. A whole-world periodic country iteration requires explicit user approval and should not be introduced by default.

Potential narrow hooks:

- state controller change notification
- country annexation cleanup
- building or supply change only if an existing owner hook already publishes it
- save-compatible event pulse schedule

## Dynamic modifiers and ideas

Proposed files:

- `common/dynamic_modifiers/051_heat_wave_dynamic_modifiers.txt`
- `common/ideas/051_heat_wave_ideas.txt` only when a country idea is needed for national priority or active emergency state

Prefer band replacement and dynamic modifiers over stacking many ideas.

Potential dynamic modifier families:

- state Heat Stress band
- local water-system failure
- environmental degradation stage
- national response priority where country dynamic modifiers are supported
- controlled industrial shutdown
- recovery burden

## Decisions and categories

Proposed files:

- `common/decisions/051_heat_wave_decisions.txt`
- `common/decisions/categories/051_heat_wave_categories.txt`

The decision file owns all Event 51 categories and missions. Keep the main category compact and phase-aware.

## State map mode

Inspect the current shared map-mode framework and documentation.

Potential file touchpoints:

- existing shared state map-mode scripted effects and triggers
- Event 51 scripted localisation
- interface and GFX only when the current framework requires it

The map mode should show Heat Stress during active and recovery phases. Permanent degradation should use its own persistent map presentation.

## Event registration and logs

Likely touchpoints after live inspection:

- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- event name localisation
- event-log scripted GUI only where current data registration requires it
- Event Details evolution rows
- reworked-event default-enabled allowlist

Use MCP event inspection before and after source changes.

## Cluster files

Inspect the live cluster registry and workbook. Likely touchpoints include:

- cluster script constants
- cluster initialization effects
- member eligibility and skip-reason logic
- scripted localisation for cluster detail
- authoritative workbook

Do not infer exact filenames from the CSV export.

## Famine and Migration

Inspect owner docs and source:

- `common/scripted_effects/famine_core_effects.txt`
- `common/scripted_effects/famine_adapter_effects.txt`
- `common/scripted_effects/migration_core_effects.txt`
- `common/scripted_effects/migration_adapter_effects.txt`
- humanitarian validation triggers
- destination selection and forced movement triggers
- owner documentation

Event 51 should add an owner-specific adapter caller, not copy core logic.

## Deaths

Inspect:

- Deaths reason constants and localisation
- exact population transaction call sites
- military casualty registration
- Chaos synchronization
- country and cause views

Add one heat-specific reason through the established pattern.

## Event 013

Inspect:

- `docs/events/013_natural_disasters/overview.md`
- Natural Disaster gateway constants
- family IDs
- target modes
- request result values
- wildfire impact and Air Cleanliness handling

Event 51 must consume the public gateway only.

## Achievements

Touch the single root achievement registry:

- `common/achievements/chaos_redux_achievements.txt`

Add tracking only where shared outcomes cannot be queried safely. Final icon triplets remain in `gfx/achievements/` root with filenames matching IDs.

## Assets and GFX

Potential files:

- event-owned event-picture GFX registry
- decision and category picture GFX registry
- state or idea icon GFX registry
- `interface/chaosx_super_events.gfx`
- sound definitions
- event-owned runtime asset folders

The asset worker creates source, PNG, DDS, manifests, and handoffs. The main implementation agent owns non-portrait GFX and gameplay wiring.

## Super-event

Inspect:

- available super-event slots
- scripted localisation getters
- image GFX
- visibility effects
- audio ID registry
- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`

Use the settings-aware playback helper.

## Localisation

Potential files:

- `localisation/english/051_heat_wave_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml` where shared UI needs labels
- `common/scripted_localisation/051_heat_wave_scripted_localisation.txt`
- event log and super-event scripted localisation

All visible text must be aligned in one change and encoded as UTF-8 with BOM.

## Documentation

Permanent documents after implementation:

- `docs/events/051_heat_wave/overview.md`
- `docs/events/051_heat_wave/lifecycle.md`
- `docs/events/051_heat_wave/decisions_and_missions.md`
- `docs/events/051_heat_wave/integrations.md`
- `docs/events/051_heat_wave/assets_and_presentation.md`
- `docs/super_events/051_heat_wave_super_event_research.md`
- completion report under the event's plan folder

Accepted source design remains under `docs/specs/051_heat_wave_specs/`.

## Spreadsheet

Edit only:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Then run:

- `python .tools/export_event_catalog_csv.py`

Never edit export CSV files directly.

## MCP requirements

### Event chain

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`

### Weighted logic

- probability inspect, evaluate, sweep, and compare through the probability auditor

### Map and terrain

- `hoi4.map_inspect`
- supported rewrite and comparison before any actual terrain conversion

### GUI

The ordinary decision category does not justify a dedicated event GUI. Use GUI tools only if the implementation must change a linked shared or category layout. A dedicated Event UI worker should not be spawned without an accepted event-owned GUI brief.

## Vanilla and wiki reading

Before source changes, read the required offline wiki and installed vanilla documentation for:

- data structures
- triggers
- effects
- modifiers
- localisation
- scopes
- on-actions
- events
- decisions and missions
- ideas
- AI
- map and terrain editing
- graphical assets
- interface behavior where touched

Inspect at least one vanilla precedent for each implemented engine surface.

## CXT test-country registration

Event 51 should not add a land sub-unit, concrete equipment type, special project, facility, doctrine, or general shared system. No CXT package registration is expected.

If implementation introduces any such object, it must follow the CXT contract and cannot be treated as a hidden Event 51 detail.

## Recommended implementation tranches

1. Repository and owner-API mapping.
2. Lifecycle, constants, and state model.
3. Temporary state and military effects.
4. Decisions and missions.
5. Mortality, Famine, Migration, and wildfire adapters.
6. Evolution II and III environmental logic.
7. Logs, cluster, repeatability, and presentation.
8. Assets, super-event, and achievements.
9. Workbook and documentation.
10. Audits, comparison, and user live validation.
