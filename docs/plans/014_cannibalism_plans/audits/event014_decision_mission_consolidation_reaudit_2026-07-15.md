# Event 014 Decision and Mission Consolidation Reaudit

Date: 2026-07-15

## Verdict

The consolidated Event 014 decision, mission, scripted-GUI, scenario, achievement, consumption, recruitment, reset, terminal, and AI surfaces have no unresolved finding in the assigned audit scope.

One P1 population-safety defect was found and fixed during the audit. After that remediation, the open finding count is:

| Severity | Open | Closed during this audit |
| --- | ---: | ---: |
| P0 | 0 | 0 |
| P1 | 0 | 1 |
| P2 | 0 | 0 |
| P3 | 0 | 0 |

This is a source-level audit of the live shared working tree after Event 014 runtime-file consolidation. It does not claim completion for unrelated Event 014 asset, focus, audio, or country-package work.

## Closed Finding

### P1-01: recovering states could become consumable again before stabilization

Before remediation, `cannibalism_can_consume_current_state` excluded the initial `cannibalism_liberated_emergency` stage and the final `cannibalism_state_stabilized` stage, but it did not exclude the persistent `cannibalism_recovery_active` flag.

`cannibalism_begin_current_state_recovery` sets `cannibalism_recovery_active`. The recovery pulse then advances through identification recovery, institutional recovery, and long trauma while retaining that flag, and clears it only after the state reaches stabilization. Once the first stage flag was replaced, unified and Wendigo consumers that relied on the canonical predicate could therefore consume population or recruit from a state still undergoing recovery.

The fix adds this canonical guard to `cannibalism_can_consume_current_state`:

```txt
NOT = { has_state_flag = cannibalism_recovery_active }
```

`cannibalism_can_recruit_from_current_state` inherits the corrected consumption predicate. Every canonical population transaction reaches the predicate through `cannibalism_prepare_consumption_context` and `cannibalism_consume_current_state`, so the fix covers feeding, silent-Larder, battlefield, prisoner, unified, warlord, and Wendigo recruitment consumers without route-specific duplication.

Changed runtime file:

- `common/scripted_triggers/014_cannibalism_triggers.txt`

## Consolidated Runtime Inventory

The audited runtime now has one Event 014 file in each assigned subsystem:

- `common/decisions/014_cannibalism_decisions.txt`
- `common/decisions/categories/014_cannibalism_categories.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/mtth/014_cannibalism_mtth.txt`
- `common/scorers/country/014_cannibalism_target_scorers.txt`
- `common/script_constants/014_cannibalism_constants.txt`
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`
- `interface/014_cannibalism_frontline_hunger.gui`
- `interface/014_cannibalism.gfx`
- `events/014_cannibalism.txt`
- `localisation/english/014_cannibalism_l_english.yml`

Mechanical inventory against those consolidated sources found:

| Surface | Count | Result |
| --- | ---: | --- |
| Decision entries | 127 | 127 unique IDs; no duplicate decision ID |
| Paid selectable decisions | 94 | Every entry has both `custom_cost_trigger` and `custom_cost_text` |
| Timed missions | 14 | Complete activation, cancellation, timeout, and reset coverage |
| Read-only achievement tracker entries | 18 | No gameplay effect, cost, cooldown, or AI block |
| Other selectable non-mission decisions | 1 | `cannibalism_end_terror_exploitation`, with AI handling |
| Selectable non-mission decisions with `ai_will_do` | 95 of 95 | Complete AI coverage |
| Decision category blocks | 18 | 13 unique categories |
| Registered Event 014 decision categories | 13 | Exact set equality with the 13 used categories |
| Scripted effects | 786 | No duplicate top-level identifier |
| Scripted triggers | 428 | No duplicate top-level identifier |
| MTTH entries | 5 | No duplicate top-level identifier |
| Country scorers | 2 | No duplicate top-level identifier |
| Script-constant namespaces | 107 | No duplicate top-level identifier |

Repeated top-level blocks for four decision categories are intentional category extensions. Their child decision IDs remain unique.

## Maintained Missions and Actions

### Eight objective mission families

The two baseline objectives and six maintained objectives all retain explicit success, partial, failure, cancellation, and pure runtime-clear paths:

1. `cannibalism_restore_supply_corridor_mission`
2. `cannibalism_rotate_compromised_formations_mission`
3. `cannibalism_investigation_mission`
4. `cannibalism_hold_prison_mission`
5. `cannibalism_reach_island_mission`
6. `cannibalism_break_network_mission`
7. `cannibalism_stop_unification_mission`
8. `cannibalism_stop_transformation_mission`

The mission decisions expose persisted objective predicates rather than implementation variables. Their cancellation resolvers re-evaluate full and partial thresholds before selecting an outcome. The family clear effects remove only runtime state; outcome flags remain in the explicit success, partial, and failure effects.

### Seven maintained paid action families

The maintained action set remains fully represented:

1. `cannibalism_replace_compromised_officer_chain`
2. `cannibalism_infiltrate_ritual_cell`
3. `cannibalism_break_ritual_economy`
4. `cannibalism_reconnoiter_silent_island`
5. `cannibalism_liberate_feeding_state`
6. `cannibalism_prepare_network_submission`
7. `cannibalism_prepare_network_resistance`

Each action has a click-time availability contract, paired dynamic cost text, explicit payment in its execution effect, a localized outcome tooltip, and an `ai_will_do` block. State and country targets use persisted identity or generation checks where the action spans pulses.

### Additional timed mission families

The complete 14-mission inventory also contains:

- `cannibalism_maintain_international_inspection_compact`;
- the four unified receipt missions for command, Larder, war machine, and counterwar;
- `cannibalism_wendigo_terminal_hunt_mission`.

The inspection compact intentionally resolves success, partial success, or failure at timeout rather than through an early `complete_effect`.

## Cost, Tooltip, and Balance Contracts

- The 94 paid decisions have 94 `custom_cost_trigger` references and 94 paired `custom_cost_text` references.
- Those references resolve to 90 unique localized cost keys; none is missing from `014_cannibalism_l_english.yml`.
- Strict scalar affordability uses a value immediately below the amount spent: one person below for manpower and `0.01` below for fixed-point command, political, experience, or fuel costs.
- Inclusive equipment checks retain the full spend amount through `NOT = { has_equipment = { type < cost } }`; their separate numeric `_gate` constants are not used as engine comparisons.
- Larder affordability uses inclusive `greater_than_or_equals` checks.
- `cannibalism_unified_refresh_affordability_gates` derives 43 runtime gates after hostility pressure is refreshed. All 43 are assigned, reduced by the correct step, and consumed by unified affordability triggers. Execution effects spend the unreduced cost variables.
- No paid decision relies on `custom_cost_text` to perform payment; the corresponding execution effects remove the real resources.

Exact displayed balances therefore remain usable after consolidation, including hostility-adjusted unified costs.

## Mission Reset and Cleanup

`cannibalism_clear_all_current_country_mission_runtime` is the first cleanup called by the Event 014 country-incarnation reset.

The set of all `days_mission_timeout` decision IDs is exactly equal to the set of guarded `remove_mission` calls in that helper:

- timed mission IDs: 14;
- guarded mission removals: 14;
- missing IDs: 0;
- extra IDs: 0.

After removing mission objects, the helper calls the family-specific clear effects. Those clears remain idempotent and do not grant success, partial success, failure, achievements, or reconstruction completion. Wendigo terminal-hunt global target cleanup remains owner-scoped, so resetting a different Event 014 actor cannot erase another actor's active hunt.

## Population, Larder, and Recruitment Safety

### Canonical transaction

`cannibalism_prepare_consumption_context` creates a monotonically increasing request identity and delegates to `cannibalism_consume_current_state`. The state transaction:

- rejects an already-consumed request identity;
- calls the canonical usable-state predicate before mutation;
- applies population loss through `apply_exact_state_civilian_population_loss`;
- records the actual applied loss in `cannibalism_population_loss_applied`;
- derives global and country consumed-population totals from the applied loss;
- derives Larder gain from the applied loss;
- records Deaths once, with the prisoner-feeding branch using its explicit mixed-death ledger rather than a duplicate generic entry.

The usable-state contract excludes wasteland, consumed Death states, nuclear fallout, severe chemical or biological contamination, irreversible air contamination, nonhuman owners other than the canonical transformed Wendigo country, exhausted population, exhausted action count, consumption cooldown, stabilization, liberated emergency, and now every active recovery stage.

### Recruitment

The operational recruitment transactions remain population-backed:

- warlord recruitment: `cannibalism_execute_warlord_recruitment_transaction`;
- unified recruitment: `cannibalism_unified_execute_recruitment`;
- ordinary paid Wendigo Pack muster: `cannibalism_train_wendigo_pack_from_selected_anchor`;
- receipt-backed Wendigo Pack muster: `cannibalism_muster_wendigo_pack_from_enemy_death_receipt_effect`.

Each requires an applied population result exactly equal to the requested amount before it adds manpower or creates a unit. Larder, equipment, command, receipt, cooldown, and capacity checks remain attached to their respective routes. The created operational formations start with zero equipment and zero manpower; experience-only start factors do not create hidden fighting strength. Scenario and warlord founding forces are bounded setup packages, not repeatable recruitment actions.

No duplicate-consumption path, free operational recruitment path, or Larder-from-unusable-state path remains after P1-01.

## Gameplay Route Wiring

| System | Evidence in consolidated runtime |
| --- | --- |
| Baseline containment | Ration audit, logistics, rotation, forensic, burial, court-martial, and amnesty decisions retain cost, tooltip, effect, mission, and AI contracts. |
| Humane response | Public court martial, conditional amnesty, humane inbound screening, liberation, and recovery effects remain connected. |
| Concealment | Transfer-record sealing and inbound-route sealing preserve their lower-cost but escalation-prone route. |
| Terror exploitation | Terror battalion, prisoner feeding, explicit exploitation exit, achievement history, and route cleanup remain connected. |
| Foreign spread | The aligned spread ledger preserves source country, source state, target country, target state, route, row ID, and generation-safe terminal status. |
| External reinfection | A locally contained country can receive a valid later spread arrival; reinfection protection and achievement history remain distinct from first infection. |
| Local and global cleanup | Local victory retires active country runtime and starts state recovery; global cleanup clears Event 014 registries, targets, convergence, scenario, and scheduler state without restoring dead population. |
| Convergence | Paid likely-host interdiction, the stop-unification objective, convergence break/rebuild, player-safe host selection, and ordinary/Wendigo reveal transactions remain connected. |
| Terminal routes | Ordinary world end and Wendigo lock both pass the shared strict Chaos threshold and route-specific readiness before setting a terminal flag. |

## Scripted GUI and Interface Actions

The interface contains 16 Event 014 buttons and the scripted GUI defines exactly 16 matching `_click` callbacks:

- missing callback: 0;
- orphan callback: 0.

The callbacks only toggle animation, open or close the network view, refresh or sort view data, change tabs, or select a displayed row. They do not pay resources, consume population, recruit units, seed cells, fire convergence, or advance a terminal route. Gameplay actions remain decisions with independent AI paths.

All five scripted GUI roots use `is_ai = no`. The early, network, and warlord surfaces require the pre-reveal state. The revealed command surface requires `cannibalism_reveal_complete` and the unified-country identity. The Wendigo surface requires `cannibalism_reveal_complete`, the pre-lock Wendigo state, and the transformed-country identity. No scripted GUI block uses an event target.

## Hannibal Secrecy, Origin Set, and Portraits

The public ordinary reveal event `chaosx.nr14.70` requires `cannibalism_reveal_complete`, the unified country, and `CBL_hannibal`. The public Wendigo reveal event `chaosx.nr14.72` requires the same global reveal flag, the transformed original-ZZZ identity, the pre-lock state, and `ZZZ_hannibal_wendigo`.

Other player-facing Hannibal surfaces remain stage-gated:

- the revealed and Wendigo GUIs require the reveal flag;
- the defeat-Hannibal tracker entry requires the reveal flag;
- public submission, resistance, news, focus, Event Details, super-event, and character-outcome content is downstream of the reveal transaction;
- early decisions, early GUI, scenario labels, and pre-reveal event text do not disclose the identity.

Canonical static portrait wiring is intact and the files exist:

- `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` use `gfx/leaders/014_cannibalism/hannibal.dds`;
- `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static` use `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.

The active warlord origin set is exactly:

1. Island Host;
2. Siege Commune;
3. March Host.

There is no `Prison Host` origin, flag, setup branch, scenario profile, or localization entry. The hold-prison objective and prison-route scoring remain ordinary mechanics and do not define an origin.

## Terminal Thresholds

`constant:cannibalism_evolution_threshold.world_end_chaos` is `1000`.

- `cannibalism_can_complete_ordinary_world_end` compares global Chaos with `compare = greater_than`.
- The two ordinary terminal focus gates repeat the explicit `global.chaos_meter_value > constant:cannibalism_evolution_threshold.world_end_chaos` check before their effects.
- `cannibalism_wendigo_can_start_countdown` uses the same `compare = greater_than` contract.
- `cannibalism_wendigo_can_lock_terminal_form` calls that countdown predicate before the final lock.
- Achievement 15 and achievement 16 also require Chaos strictly above the same threshold.

Exactly `1000` is insufficient for either world-end branch; both require a value greater than `1000`.

## Achievements

The Event 014 achievement package has exact one-to-one coverage:

- 18 `014_cannibalism_*` registry entries;
- 18 calls from those registry entries to numbered completion triggers 01 through 18;
- 18 numbered read-only tracker decisions;
- 18 scripted-localization status selectors using the same completion triggers.

The tracker entries are permanently unavailable and effect-free. Late trackers use staged visibility; in particular, the defeat-Hannibal tracker is hidden until `cannibalism_reveal_complete`. The ordinary and Wendigo world-end achievements require their distinct terminal flags and the strict Chaos threshold.

## SCN-010

The Event 014 triggerable-scenario registry remains ID 10 and exposes exactly five public launch types:

1. Discipline Collapse;
2. Ritual Cells;
3. Silent Islands;
4. Warlord States;
5. Convergence.

The constants define a minimum type of 1 and maximum type of 5. `cannibalism_scenario_can_launch`, the manual preflight planner, `trigger_cannibalism_scenario`, and the five `cannibalism_scenario_setup_*` effects all branch across the same set.

Manual launch builds and validates the required actor, state, origin, and reusable-slot manifest before `cannibalism_scenario_prepare_runtime` or another Event 014 gameplay mutation. Failed preflight clears planning arrays and records only launch failure. The three origin allocations used by Warlord States and Convergence are Island, Siege, and March only.

## Route-Aware AI

All 95 selectable non-mission decisions have `ai_will_do`. Objective missions activate from their persisted flags and are driven by the same costed actions available to AI countries.

Country targeting remains route-aware through two dynamic scorers and matching MTTH decision weights:

- `cannibalism_unified_target_scorer` / `cannibalism_unified_target_decision_weight`;
- `cannibalism_wendigo_target_scorer` / `cannibalism_wendigo_target_decision_weight`.

The target weights mirror population, supply, cell, prison-route, port-route, stability, rail/naval reach, coalition, enemy, adjacency, contamination, distance, and overextension factors. The Wendigo weight additionally mirrors pre-lock cold-front preference and post-lock population/capital preference.

Eight targeted decisions consume those route-aware MTTH values:

- six unified actions: collapse enemy front, seed a major enemy army, prepare a global campaign, issue a terror ultimatum, provoke a border incident, and destroy a coalition hub;
- two Wendigo actions: launch the terminal hunt and activate an inherited winter cell.

## References Consulted

Repository guidance:

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Event 014 specifications and matrices under `docs/specs/014_cannibalism_specs/`
- the prior Event 014 decision/mission audit, remediation handoff, anti-spoiler audit, package validation, and runtime-consolidation handoff

Offline Paradox wiki snapshot:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Interface Modding
- Scripted GUI Modding

Vanilla documentation and precedents:

- `common/decisions/_documentation.md`
- `common/scripted_guis/_documentation.md`
- `documentation/script_concept_documentation.md`, Script Constants section
- `common/script_constants/documentation.md`
- relevant effect and trigger documentation entries
- vanilla timed-mission, RAJ famine/Graveyard of Empires, RAJ tax-fraud GUI, and SOV paranoia GUI implementations

## Simplifications, Omissions, and Blockers

None within the assigned audit scope. P1-01 was fixed at the canonical predicate rather than with a route-specific fallback. No route, mission family, action family, scenario type, achievement, AI consumer, origin, GUI callback, payment, or terminal threshold was omitted or replaced with a weaker substitute.
