# File Surface Matrix

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Air Winter core

| Surface | Existing file | Planned action | Tranche |
| --- | --- | --- | --- |
| host monthly hook | `common/on_actions/chaosx_on_actions_chaos_meter.txt` | keep one host call and route into new phase helpers | 1 |
| global Air logic | `common/scripted_effects/chaos_meter_effects.txt` | extract Air Winter logic into a dedicated subsystem file or clearly bounded section | 1 |
| Air constants | `common/script_constants/chaos_meter_constants.txt` | retain global contamination thresholds and move new winter tables to a dedicated constants file | 1 |
| state phase triggers | new `common/scripted_triggers/fallout_consolidated_triggers.txt` | add phase, escalation, recovery, mitigation, and valid-state checks | 1 |
| state phase effects | new `common/scripted_effects/fallout_consolidated_effects.txt` | own phase calculation, modifier refresh, damage, recovery, aggregation, and flavour queues | 1 |
| state modifiers | new or existing dynamic modifier file | add phase-specific persistent modifiers and avoid reusing generic atomic effects for all phases | 1 |
| state population loss | `common/scripted_effects/chaos_meter_effects.txt` | add shared winter and Fallout death reasons and call shared death registration | 1 |
| state building damage | new Air Winter effects file | apply bounded phase and exposure damage through a single monthly selection | 2 |
| state category damage | existing degradation helper plus new Air Winter effects | preserve original category memory and gate sustained downgrades | 2 |
| winter flavour events | new `events/air_cleanliness_winter_events.txt` or a clear contamination namespace extension | add phase, regional, recovery, mitigation, and failure incidents | 2 |
| winter decisions | new `common/decisions/fallout_consolidated_decisions.txt` | state-target mitigation, evacuation, shelter, repair, and rationing actions | 2 |
| winter categories | new category file | keep response decisions staged and uncluttered | 2 |
| winter AI | decision weights plus strategy file if needed | choose responses from phase, industry, war, food, and survival pressure | 2 |
| treaty | existing treaty helpers, events, decisions, opinion modifiers | restore with cached membership and performance-safe updates | 2 |

## Winter mapmode

| Surface | Existing file | Planned action | Tranche |
| --- | --- | --- | --- |
| mapmode definition | `common/map_modes/chaosx_state_map_modes.txt` | add `air_winter_state_map_mode` | 1 |
| mapmode constants | `common/script_constants/state_map_modes_constants.txt` | add phase palette, thickness, highlight, and background values | 1 |
| mapmode triggers | `common/scripted_triggers/cbw_triggers.txt` or dedicated mapmode trigger file | add active phase and visibility checks | 1 |
| scripted tooltip | `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` | show phase, direction, exposure, forecast, impacts, monitoring, and response state | 1 |
| visible localisation | `localisation/english/chaosx_map_modes_l_english.yml` | add direction-only implementation keys with final prose written during implementation | 1 |
| button strip | `gfx/interface/mapmode/mapmode_buttons_selected_small.dds` and deselected strip | append verified winter frame | 1 |
| strip sprite metadata | `interface/mapmodes_interface.gfx` | correct current frame count and add winter frame count | 1 |
| mapmode docs | `docs/systems/state_map_modes.md` | document exact verified slot and phase colors | 1 |

## Fallout request and transition

| Surface | Existing file | Planned action | Tranche |
| --- | --- | --- | --- |
| stale Fallout event | `events/chemical_warfare_events.txt` | delete the Fallout block and keep only Air Contamination and chemical events | 3 |
| Fallout constants | new `common/script_constants/fallout_consolidated_constants.txt` | source ids, beat timing, grade thresholds, batch limits, and AI values | 3 |
| Fallout effects | new `common/scripted_effects/fallout_consolidated_effects.txt` | request, snapshot, blackout, state grade, world rewrite, cleanup, player handoff | 3 and 4 |
| Fallout triggers | new `common/scripted_triggers/fallout_consolidated_triggers.txt` | request eligibility, valid state, valid successor, transition safety, cleanup checks | 3 and 4 |
| Fallout events | new `events/fallout_world_end_events.txt` | own every Fallout entry, blackout, rewrite, manual scenario, recovery, and aftermath event under `chaosx.fallout` | 3 onward |
| Fallout on-actions | new Fallout-owned on-action only where needed | use narrow hooks, not a new global daily country loop | 3 |
| blackout GUI | new `interface/fallout_consolidated.gui` | full-screen black independent container, centered text, no close action during processing | 3 |
| blackout GFX | new `interface/fallout_consolidated.gfx` | background, subtle treatment, beat states, static fallbacks | 3 |
| blackout scripted GUI | new `common/scripted_guis/fallout_consolidated_scripted_gui.txt` | visibility, properties, dynamic player-choice list, dirty-variable update | 3 and 4 |
| blackout scripted localisation | new `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt` | map phase values to researched final beat keys during implementation | 3 |
| blackout localisation | new English localisation file | final text written after implementation state is stable | 3 |
| sound | `sound/fallout_world_end/` and optional `music/fallout_world_end/` | use only Fallout-owned files and wrappers, never a normal super-event audio id | 3 |

## World rewrite and successors

| Surface | Existing file | Planned action | Tranche |
| --- | --- | --- | --- |
| state grading | new Fallout effects and triggers | compute deterministic grade and state class | 4 |
| state population and buildings | shared deaths plus Fallout effects | apply grade-based one-time and persistent consequences | 4 |
| ownership rewrite | Fallout effects | transfer state ownership in validated regional batches | 4 and 6 onward |
| diplomacy cleanup | Fallout effects | end or remap wars, guarantees, factions, subjects, access, and exile state | 4 |
| tag ledger | new plan and implementation data file | record candidate source, current ownership, collision state, package assignment | 4 and 6 |
| cosmetic tags | existing cosmetic pattern and localisation files | add selected successor identities | 6 onward |
| base tags | `common/country_tags/chaosx_countries.txt` and related package files | add only where cosmetic or existing tags cannot satisfy the package | 6 onward |
| country packages | country, history, character, idea, unit, and AI files | implement reviewed regional batches | 6 onward |
| focus trees | `common/national_focus/` | compose archetype, regional, and memory content | 6 onward |
| shared focuses | new focus files if verified | reuse branch logic without erasing country memory | 6 onward |
| decisions | Fallout-owned survivor and archetype files | survival, reconstruction, diplomacy, expansion, and mutation systems | 6 onward |
| ideas | Fallout-owned idea files | starting crisis, staged recovery, route identity, and failure forms | 6 onward |
| units | templates, OOB, and dynamic spawns | give every fighting successor a real starting package and growth path | 6 onward |
| assets | `docs/assets/fallout_world_end/`, dedicated Fallout GFX folders, and engine-required root flag folders | create Fallout-owned flags, portraits, icons, UI, report images, and animations | 6 onward |

| Thaw Water ordinary chain | `events/fallout_world_end_events.txt`, `common/scripted_effects/fallout_consolidated_effects.txt`, `common/scripted_triggers/fallout_consolidated_triggers.txt`, `common/script_constants/fallout_consolidated_constants.txt`, `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`, `localisation/english/fallout_consolidated_l_english.yml` | Four thaw policies, deterministic result and callback, Air Winter water and disease updates, Deaths-backed failure, and authenticated cleanup | reviewed tranche |

## Manual scenario

| Surface | Existing file | Planned action | Tranche |
| --- | --- | --- | --- |
| scenario ids | `common/script_constants/chaosx_triggerable_scenarios_constants.txt` | scan all assigned ids and append Fallout at the next integer after the current maximum without moving existing entries | 5 |
| registry and sorting | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | keep Fallout out of public registry and sort paths, then audit the Fallout-owned reservation and dispatch boundary | 5 |
| launch gate | `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt` | block active terminal state and invalid setup only | 5 |
| GUI click and confirmation | `common/scripted_guis/chaosx_scripted_gui_settings.txt` | route selected Fallout scenario through normal confirmation | 5 |
| scripted localisation | `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` | add name, id, detail, type, and intensity mappings | 5 |
| visible localisation | `localisation/english/chaosx_gui_l_english.yml` | add final player-facing text after behavior is stable | 5 |
| scenario event | `events/fallout_world_end_events.txt` | own Fallout confirmation, launch, countdown, and completion events while the generic scenario system only calls the entry | 5 |
| strike helper | new Fallout effects file | apply exact thermonuclear province sweep and aggregate logging | 5 |
| countdown | new Fallout effects and events | persist seven-day countdown and survive save-load | 5 |
| documentation | `docs/systems/event_system/triggerable_scenarios.md` and Fallout system docs | document the allocated scenario id and launch behavior | 5 |

## Cross-surface documentation and records

| Surface | Planned action | Tranche |
| --- | --- | --- |
| `docs/systems/air_cleanliness/air_contamination_mechanic.md` | rewrite against implemented phases, treaty, triggers, and transition | each tranche |
| `docs/systems/state_map_modes.md` | update verified slots and winter behavior | 1 |
| Fallout event doc | add one canonical implementation document | 3 onward |
| `CHAOS_REDUX_MECHANICS.md` | add Fallout as an explicit exception to ordinary chaos-above-1000 world ends | 4 |
| event catalog workbook | update only after final in-game text exists | finalization |
| scenario catalog | align SCN identifiers and descriptions | 5 and finalization |
| asset manifests | record every generated, sourced, converted, wired, blocked, and reviewed asset | each country batch |
| plan disposition ledger | record implemented, queued, rejected, or blocked status for every accepted plan | each tranche |
