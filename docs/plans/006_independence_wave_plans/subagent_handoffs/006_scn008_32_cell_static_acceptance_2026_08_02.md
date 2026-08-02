# Event 006 SCN-008 32-cell static acceptance matrix

This handoff records the source-level acceptance surface for proposed scenario `SCN-008`, Independence Wave. It is a static matrix, not live or in-game evidence. The scenario implementation attempts every viable current-map-bound candidate before commit, records rejected and unbound rows, and applies type behavior only after the synchronized release transaction succeeds.

## Cell contract

Every cell is the Cartesian product of one scenario mode and one intensity. The four intensity values are implemented by `independence_wave_scenario_set_intensity_tuning` in `common/scripted_effects/006_independence_wave_scenario_effects.txt`:

| Intensity | Chaos band | Territory | Forces | Value profile |
| --- | --- | --- | --- | --- |
| Low | Calm | Anchor | Fragile | Low legitimacy, recognition, capacity, and security; low instability |
| Medium | Rising | Compact | Viable | Medium legitimacy, recognition, capacity, and security; medium instability |
| High | Totalen | Extended | Armed | High legitimacy, recognition, capacity, and security; high instability; ambition acceleration |
| Maximum | World Collapse | Extended | High chaos | Maximum value profile; high-chaos lane, World Collapse ambition, and hidden-formable discovery |

`Great Partition` advances the territory tier once before reservations when the intensity would otherwise be Anchor or Compact. It never bypasses anchor uniqueness or host survival.

## Mode cells

The six engine type values plus the three bounded Universal Belligerence rules produce eight player-facing modes. Each row below contains Low, Medium, High, and Maximum cells in that order.

| Mode | Low | Medium | High | Maximum | Type-owned behavior after commit |
| --- | --- | --- | --- | --- | --- |
| Sovereign Scatter | `SCN-008/sovereign_scatter/low` | `SCN-008/sovereign_scatter/medium` | `SCN-008/sovereign_scatter/high` | `SCN-008/sovereign_scatter/maximum` | Releases remain outside a pre-formed league; countries receive survival AI seeds and existing faction membership is left only where the type contract permits it. |
| Common Congress | `SCN-008/common_congress/low` | `SCN-008/common_congress/medium` | `SCN-008/common_congress/high` | `SCN-008/common_congress/maximum` | Registers every released country in Network and League collections, elects the first released row as leader, and forms the consultative/formal league state according to intensity. |
| Wars of Separation | `SCN-008/wars_of_separation/low` | `SCN-008/wars_of_separation/medium` | `SCN-008/wars_of_separation/high` | `SCN-008/wars_of_separation/maximum` | Clears prior host relation deltas, writes paid host-claim/hostility/security pressure, and starts one bounded host war per released country after commit. |
| Universal Belligerence: former hosts | `SCN-008/universal_belligerence/former_hosts/low` | `SCN-008/universal_belligerence/former_hosts/medium` | `SCN-008/universal_belligerence/former_hosts/high` | `SCN-008/universal_belligerence/former_hosts/maximum` | Targets former hosts with one unique actor policy per release, marks the danger batch at Maximum, and clears target marks after declarations or failed declarations. |
| Universal Belligerence: neighboring releases | `SCN-008/universal_belligerence/neighboring_releases/low` | `SCN-008/universal_belligerence/neighboring_releases/medium` | `SCN-008/universal_belligerence/neighboring_releases/high` | `SCN-008/universal_belligerence/neighboring_releases/maximum` | Each released country may select one neighboring released country, with duplicate-target marks, bounded declaration checks, and cleanup. |
| Universal Belligerence: nearby non-league | `SCN-008/universal_belligerence/nearby_nonleague/low` | `SCN-008/universal_belligerence/nearby_nonleague/medium` | `SCN-008/universal_belligerence/nearby_nonleague/high` | `SCN-008/universal_belligerence/nearby_nonleague/maximum` | Each released country may select one nearby non-league, non-subject country; duplicate-target marks and failed-declaration recovery remain bounded to this launch. |
| Patron Worlds | `SCN-008/patron_worlds/low` | `SCN-008/patron_worlds/medium` | `SCN-008/patron_worlds/high` | `SCN-008/patron_worlds/maximum` | Selects a nearby major patron matching the new government's ideology where possible, otherwise a neutral major, and writes the patron ledger through the normal bilateral API. |
| Great Partition | `SCN-008/great_partition/low` | `SCN-008/great_partition/medium` | `SCN-008/great_partition/high` | `SCN-008/great_partition/maximum` | Consumes one additional optional-territory tier where valid, opens regional ambition, writes host border pressure and partition instability, and does not change candidate readiness. |

## Shared acceptance rules for all 32 cells

1. `independence_wave_scenario_rebuild_ranked_registry` rebuilds the deterministic package-ID order for every launch.
2. `independence_wave_scenario_attempt_ranked_packages` attempts every ranked current-map-bound row at every intensity. Unready content is recorded as `package_unready`; living tags, host-remnant failures, duplicate anchors, Event 005 collisions, and territory failures are recorded by the shared rejection ledger.
3. `independence_wave_allocate_scenario_packages` freezes the selected rows and refuses commit when the selected array is empty, optional expansion breaks alignment, or the plan is not in the triggerable-scenario allocation phase.
4. Intensity modifies territory, forces, and visible country values. It never silently changes the candidate registry or makes a research-gated identity complete.
5. Type controls league, host-war, belligerence, patron, and partition setup only after release finalization. Ordinary waves do not call these type effects.
6. `independence_wave_scenario_reset_summary` clears prior release, target-mark, rejection, and ledger arrays before the next launch, preventing stale cells from inheriting old countries or wars.

## Source crosswalk

| Surface | Source |
| --- | --- |
| Type/intensity controls | `common/scripted_effects/006_independence_wave_scenario_effects.txt` (`independence_wave_scenario_type_next`, `independence_wave_scenario_type_previous`, `independence_wave_scenario_set_intensity_tuning`) |
| Type gates and queued validation | `common/scripted_triggers/006_independence_wave_scenario_triggers.txt` |
| Ranked candidate attempt and frozen selection | `common/scripted_effects/006_independence_wave_scenario_effects.txt` (`independence_wave_scenario_rebuild_ranked_registry`, `independence_wave_scenario_attempt_ranked_packages`, `independence_wave_allocate_scenario_packages`) |
| Post-commit mode behavior | `common/scripted_effects/006_independence_wave_scenario_effects.txt` (`independence_wave_scenario_mark_current_release`, `independence_wave_scenario_apply_type`) |
| Scenario UI and decisions | `common/decisions/categories/006_independence_wave_scenario_categories.txt`, `common/decisions/006_independence_wave_scenario_decisions.txt`, and `interface/006_independence_wave.gui` |
| Player-facing names and detail wording | `localisation/english/006_independence_wave_scenario_l_english.yml` |

This matrix closes the static documentation gap for the 32 accepted mode/intensity cells. It does not claim live execution, save/load, or player-owned evidence.
