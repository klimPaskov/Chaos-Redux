# Event 19 AI, Balance, Performance, Isolation, and Exploit Live-Final Reaudit

## Audit disposition

This was a fresh audit of the live Event 19 source. Existing Event 19 audit and handoff conclusions were not used as evidence.

| Severity | Count |
|---|---:|
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| Total findings | 0 |

No evidence-backed AI-parity defect, balance exploit, performance regression, cross-event contamination, scenario leak, transaction duplication, or unsupported fallback was found in the audited surface.

## Scope and acceptance basis

The audit treated Event 19 as a Minor Repeatable event and checked the live implementation against the eight-part Event 19 specification and the accepted near-completion improvement addendum. In particular, the following two substitutes were treated as explicitly approved acceptance paths:

1. Four controlled one-formation border trials for the four combat achievements.
2. Exact recorded-formation recreation, proof, and source deletion for loyal formation transfer.

No other fallback or substitute was accepted.

Evidence was established from the current script paths, call paths, variables, flags, arrays, constants, triggers, and scope iteration. The result is a source-level audit; no runtime behavior was inferred from an earlier audit report.

## Findings

No P0, P1, or P2 findings.

## AI parity matrix

| Surface | Live evidence | Result |
|---|---|---|
| Main decisions and missions | The three Event 19 decision files contain 68 top-level decisions and 14 missions. All 68 decisions have an ai_will_do block. Timed mission behavior is also gated and weighted through the same country state used by the player-facing system. | Pass |
| Player GUI actions | common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt delegates actions to shared scripted effects. GUI-open and selection-mirror decisions are intentionally AI-disabled because they are presentation/state-selection helpers, not a separate gameplay transaction. | Pass |
| Country management pulse | infantry_spawn_run_country_management_pulse in common/scripted_effects/019_infantry_spawn_management_effects.txt selects the weakest lot under severe congestion, the strongest lot during war, and the first valid lot otherwise; it settles the first exactly affordable obligation before dispatching an incident. | Pass |
| Anomalous family management | infantry_spawn_run_anomalous_family_ai in common/scripted_effects/019_infantry_spawn_muster_board_effects.txt selects the highest-pressure family, prioritizes containment or dispersal at critical pressure, otherwise weights sustainment, cantonment, restriction, and liaison, and can run the train-or-spawn transaction when conditions permit. | Pass |
| Family payment parity | Family actions use the same eligibility, provider payment, overhead, proof, commit, refund, and cooldown effects used by player actions. Cooldowns and request counters advance only after proof-backed commit. | Pass |
| Claimant choices | Claimant decisions and event options have contextual AI choices. Deferred choices preserve the frozen claimant UID and demand and quarantine an impossible replay rather than selecting a different claimant or silently succeeding. | Pass |
| Derivative country decisions | All 23 derivative decisions have AI weights. Their triggers are route-, family-, war-, pressure-, and resource-aware. | Pass |
| Derivative focus routes | The live derivative tree contains 45 focus blocks: 30 shared and five per family. Each family can access 35 focuses and all focus blocks have AI weighting. | Pass |
| Scenario actors | Dedicated scenario AI strategies are applied to the dynamically created actors; scenario actors remain excluded from ordinary Event 19 evolution contribution. | Pass |
| Invalid AI action prevention | Shared availability triggers, transaction locks, exact affordability checks, cooldown flags, pending-choice checks, and proof-before-commit logic gate both AI and player execution. | Pass |

Decision inventory checked:

| File | Decisions | Missions |
|---|---:|---:|
| common/decisions/019_infantry_spawn_decisions.txt | 39 | 11 |
| common/decisions/019_infantry_spawn_claimant_decisions.txt | 6 | 0 |
| common/decisions/019_infantry_spawn_derivative_decisions.txt | 23 | 3 |
| Total | 68 | 14 |

## Balance and exploit-resistance matrix

### Manifestation coverage

The state-selection curve is continuous at every bracket transition and its marginal coverage declines as the country grows.

| Eligible states | Coverage rule | Balance property |
|---|---|---|
| Fewer than 6 | All eligible states | Tiny countries receive a legible manifestation without an empty result. |
| 6 to 15 | Base 5 plus a 7/9 marginal slope | Coverage grows, but slower than country size. |
| 16 to 35 | Base 12 plus a 9/19 marginal slope | The marginal share declines. |
| 36 to 70 | Base 21 plus a 10/34 marginal slope | Large-country spread remains bounded. |
| 71 or more | Base 31 plus a 0.25 marginal slope | Very large countries do not receive linear map saturation. |

The final value is rounded and clamped between one and the eligible-state count. Selection uses a temporary weighted pool and removes every copy of the selected state, producing weighted selection without replacement.

State weight evidence:

| Signal | Weight behavior |
|---|---|
| Base | 4 |
| Capital | +8 |
| Core | +3 |
| Industry | +2 or +4 by tier |
| Supply hub | +5 |
| Railway | +3 |
| Port | +3, with a further +3 at the higher tier |
| Urban | +3 |
| Population | +3 |
| Active front | +4 |
| Occupied | +1 |
| Resistance | -3 |
| Island | -2 |
| Final bound | 1 through 32 |

This avoids deterministic capital-only placement while still preferring militarily and economically meaningful states.

### Formation lots and equipment

| Curve | Live values or behavior | Audit result |
|---|---|---|
| Lot size | Typical baseline 6, organized 7, arsenal 9; command-fracture lots use 2, 8, or 12. | Distinct profiles without a single dominant lot size. |
| Units per state | Baseline 88/12; organized 72/28; arsenal 45/40/15, with capacity, front, and congestion modifiers. | Larger formations are concentrated in the profiles that pay the corresponding logistical burden. |
| Quality | Baseline 22/43/28/7; organized 6/28/44/20/2; arsenal 5/22/38/30/5. | Higher quality is profile-weighted rather than guaranteed. |
| Supply burden | Baseline 35/50/13/2; organized 20/55/22/3; arsenal 8/37/45/10. | Arsenal strength carries materially worse sustainment risk. |
| Coherence | Baseline 10/20/45/25; organized 4/12/42/42; arsenal 8/22/42/28, shifted by control and congestion. | Control and congestion affect formation reliability instead of acting as cosmetic values. |
| Accounting | Per-battalion manpower 500, equipment 45, support 20, fuel 40, prototype 90, anomalous 100. | Liability is tied to recorded composition. |
| Initial fill | War 0.65, peace 0.45, organized +0.15, arsenal +0.10, clamped 0.20 to 0.90. | No full-strength free-army path. |

### Muster Control and Army Congestion

Muster Control begins from 45 plus a stability contribution, with a wartime penalty. Audits, standardization, territorial organization, and demobilization can recover control; emergency integration, stacked generations, requests, and failures reduce it. It is clamped to 0 through 100, with meaningful bands at 25, 45, 70, and 85.

Army Congestion is derived from active divisions relative to controlled states, active lots, unresolved generations, stacked generations, family pressure, and relief. It is clamped to 0 through 100 with the same four meaningful bands.

| Risk | Counter-pressure in live code | Result |
|---|---|---|
| Repeated requests | Request scale includes controlled states, active divisions, congestion, active lots, control shortfall, and prior request count; war grants only a small offset. | Costs grow with both country size and accumulated burden. |
| Request specialization | Baseline request liabilities are profile-scaled; anything and anomalous requests use higher multipliers. | The broadest requests do not undercut specialized requests. |
| Standardization loop | Standardization pays its material loss through a transaction and applies a one-time lot status. | It cannot be repeated for free value. |
| Demobilization loop | Demobilization salvages only recorded paid material and is gated by one-time status and exact ledger updates. | It cannot mint unrecorded equipment or repeatedly salvage one lot. |
| Prototype cannibalization | Uses the higher salvage factor but consumes the recorded status and liability surface. | Stronger return has a real opportunity cost. |
| Emergency integration | Raises control pressure and related liabilities instead of erasing the system's costs. | No free congestion reset. |
| Exact obligations | An obligation is settled only when the exact affordable ledger row is selected and committed. | No partial-pay/full-reward route. |

The request scaling formula is monotonic in every burden term. Its base costs are 8 army XP, 350 infantry equipment, 35 support equipment, 20 trucks, one train, 250 fuel, and 1,200 manpower liability before profile and accumulated-burden scaling.

### Ledger and lifetime scaling

| Surface | Live bound | Result |
|---|---|---|
| Compaction cadence | Country-scoped, every 30 days while relevant | No recurring world scan. |
| Rows scanned per pulse | 24 | Work is bounded. |
| Lot batch | 4 | Work is bounded. |
| Generation batch | 4 | Work is bounded. |
| Maximum ledger rows processed per lot batch | 64 | Pathological lifetime growth is capped per pass. |
| Retry behavior | Delayed country event with a scheduled flag | No same-day recursive retry or duplicate schedule. |

## Evolution counter and performance matrix

| Check | Live evidence | Result |
|---|---|---|
| Recurring whole-world iteration | Event 19 defines no on_daily, on_weekly, on_monthly, or on_yearly on_action. Its country maintenance loop is the delayed country event chaosx.nr19.900 and is scheduled only while Event 19 state requires it. | Pass |
| Authorized every_country use | One manifestation pass in 019_infantry_spawn_core_effects.txt, four one-time evolution stage activation passes in 019_infantry_spawn_evolution_effects.txt, and scenario launch/cleanup passes in 019_infantry_spawn_scenario_effects.txt. | Pass |
| Country division iteration | every_country_division calls are scoped to the current country for exact formation, ledger, transfer, and trial proof. They are not country-world loops. | Pass |
| Scenario terminal hostile check | One any_country query in 019_infantry_spawn_scenario_triggers.txt is gated by the active scenario launch serial and frozen scenario roster and is evaluated on the scenario terminal path, not periodically. | Pass |
| Epoch rebuild | A rebuild increments the global epoch, zeroes the maintained counters, marks rebuild in progress, and lets the one-time world pass discard stale receipts before closing the epoch. | Pass |
| Receipt adoption | A country can adopt the ready epoch without a receipt only when it has no prior receipts; conflicting receipt state closes readiness and records an invariant failure. | Pass |
| Underflow protection | Current-epoch unregister checks the maintained count before subtracting. An attempted underflow retains the receipt, closes readiness, and records failure instead of creating a negative count. | Pass |
| Stale receipt cleanup | Stale-epoch receipts clear without subtracting from the new epoch. | Pass |
| Counter ordering | Participant receipts are removed after derivative receipts; world-war receipts are removed before world-country receipts. | Pass |
| Local reconciliation | War, peace, release, government change, annexation, and country-death reconciliation operate from the affected country scope. | Pass |
| Counter validity | Validation checks nonnegative counters and subset relationships before the global ready flag can remain active. | Pass |
| Evolution timing | The MTTH due date advances before scoring, preventing a same-day duplicate score. | Pass |
| Evolution activation | Each of the four evolutions has both active-state and pre-fire eligibility paths, then performs one activation pass. | Pass |
| Stage scoring | Stage progress uses maintained multi-signal state, not one easily farmed counter. | Pass |

Evolution thresholds are monotonic across the four tiers, including generation requirements 2, 4, 6, and 8 and formation requirements 20, 60, 110, and 180. No lower tier requires more than a later tier on the audited principal progression counters.

## Registry, identities, and fixed visual slots

| Check | Evidence | Result |
|---|---|---|
| Sole Event 19 provider registry | Repository-wide provider-definition search found chaos_unit_family_provider_501_event19, 502, and 503 definitions only in common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt. | Pass |
| Provider registration | Zombie 501 is registered from 002_zombie_outbreak_on_actions.txt, ghost 502 from 010_death_on_actions.txt, and golem 503 from 005_soviet_collapse_on_actions.txt. | Pass |
| Fixed identity slots | 20 claimant portraits, six host identity portraits, and one neutral unassigned-muster portrait are defined and wired: 27 slots total. | Pass |
| Claimant leaders | create_corps_commander explicitly uses female = no, and identity proof requires is_female = no. | Pass |
| Scenario and derivative leaders | All Event 19 gameplay leader creation paths explicitly use female = no, with corresponding proof checks. | Pass |

The six host slots cover commander and council identities for zombie, ghost, and golem hosts. The neutral slot is not reused as a gameplay leader fallback.

## Derivative country matrix

| Surface | Live behavior | Result |
|---|---|---|
| Opening weakness | Unrecognized host, seized districts, former-state weakness, claimant burdens, and family-specific weakness ideas impose stability, political power, organization, supply, reinforcement, training, speed, or efficiency costs as appropriate. | Pass |
| Route progression | Focuses replace or transform opening burdens rather than stacking permanent penalties indefinitely. | Pass |
| Private history | Derivative package rows are private to the derivative ledger; scenario and derivative participants do not become ordinary Event 19 evolution contributors. | Pass |
| Zombie reinforcement | Provider 501 supports the training path once its provider eligibility permits it. | Pass |
| Ghost reinforcement | Provider 502 uses spawning rather than training. | Pass |
| Golem reinforcement | Provider 503 uses spawning rather than training. | Pass |
| Train-vs-spawn transaction | A fresh lot and template are built, eligibility and provider payment are proven, the provider performs training or spawning, and commit occurs only after formation proof; otherwise the path rolls back and refunds. | Pass |
| Ghost decline cadence | One eligible positive-population controlled state is selected every 180 days. Base decline is 0.25%, anchored 0.20%, managed 0.15%, capped by 0.50% and an absolute 5,000. | Pass |
| Death integration | Ghost decline reports exactly one death-registration reason, chaos_meter_deaths_reason.infantry_spawn_ghost_decline, and does not mutate Event 10 soul-consumption state. | Pass |
| Defeat recording | The defeat handler is guarded by the one-time defeat-recorded state before history/report dispatch. | Pass |

## Exact natural derivative and loyal transfer matrix

| Release mode or edge case | Proof and safety behavior | Result |
|---|---|---|
| Ordinary claimant | Freezes exact units, lots, templates, generations, obligations, live signature, gates, and nonce before country creation. | Pass |
| Anomalous claimant | Uses the same exact transaction surface plus the selected family/provider proof. | Pass |
| Independent family | Uses the exact family set and provider setup path. | Pass |
| Country creation | Uses create_dynamic_country with original_tag = THIS. No fixed output tag fallback exists. | Pass |
| Loyal formations | Approved substitute is implemented: recreate the exact recorded formation on the target, prove it, delete the exact source UID/cohort, prove absence, then commit accounting. | Pass |
| Formation fidelity | Recreated rows preserve UID, template manifest, initial factors, cohort, ledger metadata, and live metadata within the approved recreate/prove/delete model. | Pass |
| Precommit failure | Restores the source transaction and applies the defined failure consequence. | Pass |
| Postcommit uncertainty | Both sides remain locked and fail closed until proof-backed cleanup can complete. | Pass |
| One-state independent family | Same-tag takeover requires every live division to belong to the frozen claimant-free family and proves unchanged row/count state after provider setup. | Pass |
| One-state claimant | Region preflight cannot pass; source state is restored before the selected claimant's failed-coup effect arrests the claimant, restores lot control, decrements active claimant accounting, and records the failure once. | Pass |
| Fixed-tag identity filters | ZZZ, DTH, and KMB appear only as explicit parent/origin exclusions in host validity, not as output-tag fallbacks. | Pass |

No transfer_units_fraction path is present.

## SCN-013 intensity constants

| Intensity | Host share | Revolt pressure | State coverage | Generation passes | Random lots | Family formations | Fronts | Regional wars | Manpower |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Low / localized | 10% | 45 | 20% | 3 | 2 | 2 | 1 | 0 | 50,000 |
| Medium / regional | 25% | 60 | 35% | 4 | 4 | 4 | 1 | 0 | 80,000 |
| High / continental | 50% | 75 | 55% | 5 | 6 | 6 | 2 | 2 | 120,000 |
| Maximum / global | 100% | 90 | 80% | 6 | 8 | 8 | 3 | 8 | 180,000 |

Country share is converted to the percentage scale expected by random chance before host selection.

## SCN-013 16-combination matrix

Every type/intensity input pair is explicitly admitted by the launch input gates. Dispatch covers all four types; the final branch is anomalous only after the input gate has proven type 4.

| Type | Intensity | Expected package proof | Result |
|---|---|---|---|
| Conventional manifestation | Low | Exactly 3 new generation rows; each generated lot/unit count is positive; 20% state coverage; low global pressure package. | Pass |
| Conventional manifestation | Medium | Exactly 4 new generation rows; each generated lot/unit count is positive; 35% state coverage; medium global pressure package. | Pass |
| Conventional manifestation | High | Exactly 5 new generation rows; each generated lot/unit count is positive; 55% state coverage; high global pressure package. | Pass |
| Conventional manifestation | Maximum | Exactly 6 new generation rows; each generated lot/unit count is positive; 80% state coverage; maximum global pressure package. | Pass |
| Arsenal lottery | Low | Exactly 3 arsenal generation rows with positive lots/units; 20% state coverage; arsenal profile retained in proof. | Pass |
| Arsenal lottery | Medium | Exactly 4 arsenal generation rows with positive lots/units; 35% state coverage; arsenal profile retained in proof. | Pass |
| Arsenal lottery | High | Exactly 5 arsenal generation rows with positive lots/units; 55% state coverage; arsenal profile retained in proof. | Pass |
| Arsenal lottery | Maximum | Exactly 6 arsenal generation rows with positive lots/units; 80% state coverage; arsenal profile retained in proof. | Pass |
| General mutiny | Low | Exactly one scenario generation, 2 exact random lots with positive unit rows, and exactly one claimant. | Pass |
| General mutiny | Medium | Exactly one scenario generation, 4 exact random lots with positive unit rows, and exactly one claimant. | Pass |
| General mutiny | High | Exactly one scenario generation, 6 exact random lots with positive unit rows, and exactly one claimant. | Pass |
| General mutiny | Maximum | Exactly one scenario generation, 8 exact random lots with positive unit rows, and exactly one claimant. | Pass |
| Anomalous takeover | Low | A derivative-capable family is preflighted; exact family target is frozen; one scenario generation and 2 exact family formations are proven. | Pass |
| Anomalous takeover | Medium | A derivative-capable family is preflighted; exact family target is frozen; one scenario generation and 4 exact family formations are proven. | Pass |
| Anomalous takeover | High | A derivative-capable family is preflighted; exact family target is frozen; one scenario generation and 6 exact family formations are proven. | Pass |
| Anomalous takeover | Maximum | A derivative-capable family is preflighted; exact family target is frozen; one scenario generation and 8 exact family formations are proven. | Pass |

Common proof for all 16 combinations:

- Host eligibility excludes Event 19 parent identities, derivatives, active combat trials, cleanup quarantine, and pending transactions.
- The origin is processed once, then other valid countries are selected without duplicate host processing.
- Microstates and all-island countries take the same-tag transaction path rather than a fixed-tag fallback.
- Package commit requires aligned Event 19 ledgers.
- Scenario actors are marked non-contributors to ordinary evolution history.
- Bypass/profile flags are cleared immediately on the normal path and by the scenario cleanup pass if residue remains.
- Same-tag state is snapshotted, package objects are deleted and proven absent on rollback, ledger tails are restored, and chaosx.nr19.955 retries cleanup while the lock remains.
- Dynamic-actor rollback uses chaosx.nr19.954 and retains the corresponding lock until proof.
- Event 19 scenario code neither sets nor clears world_end.

## Controlled combat trial exploit matrix

| Exploit surface | Live guard | Result |
|---|---|---|
| Farming with a full army | The attacker state must contain exactly one attacker division, matching the frozen Event 19 unit identity, with no foreign division present. | Blocked |
| Farming against a normal stack | The defender is a generated, locked one-battalion formation; the defender state must prove exactly that one formation and no foreign division. | Blocked |
| Reusing another trial type | Trial type, nonce, attacker identity, states, and opponent are frozen and re-proven on callbacks. | Blocked |
| Territory theft | start_border_war uses change_state_after_war = no. | Blocked |
| Starting during normal war or civil war | Host and opponent eligibility require the peaceful, non-civil-war state and no existing border war. | Blocked |
| Duplicate start cost | Costs are debited only after both states prove that the border war actually started. | Blocked |
| Stuck trial | Minimum duration is 14 days, timeout is 45 days, and timeout/cancel cancels the border war before cleanup. | Blocked |
| Immediate refarm | A 90-day cooldown is applied after resolution/cleanup. | Blocked |
| Orphan defender | Cleanup deletes the exact defender UID and exact template, then proves absence. | Blocked |
| Unprovable cleanup | The opponent remains quarantined from trial and scenario eligibility rather than unlocking a possibly dirty state. | Fail closed |
| Duplicate callback | Attacker and opponent callbacks route through frozen state and one-time resolution flags. | Blocked |

There are four immutable trial types, one for each approved combat-achievement substitute.

## Isolation and lifecycle matrix

| Event edge | Duplicate/isolation behavior | Result |
|---|---|---|
| Manifestation | The only core world pass is the manifestation pass. It registers Event 19 state without recurring world iteration. | Pass |
| Stage activation | Each stage activation uses its own one-time global state and does not reuse scenario or derivative actor receipts. | Pass |
| Evolution | Active and pre-fire paths use the maintained epoch counters and ordinary-contributor filters. | Pass |
| Super-event | Event 19 has no super-event wiring or super-event mutation. | Pass |
| World end | Event 19 only reads world-end gates; it does not set or clear world_end. | Pass |
| War and peace | Reconciliation is affected-country scoped and receipt-idempotent. | Pass |
| Civil war/release | Exact dynamic-country or same-tag transaction logic is used; invalid one-state claimant release becomes the defined failed coup after restoration. | Pass |
| Capitulation | Derivative defeat history and report dispatch are protected by the defeat-recorded one-time state. | Pass |
| Annexation | Exact formation/template cleanup is proof-backed. Migration retry arrays use unique membership and a single scheduled flag. Repeated on-annex callers see cleared source arrays. | Pass |
| Country death | Receipt unregister and migration are idempotent; stale epochs clear without touching new counters. | Pass |
| Formation transfer | Target recreation is proven before exact source deletion; deletion is proven before accounting commit. | Pass |
| Scenario bypass | Launch-scoped flags are cleared on success and by the authorized scenario cleanup pass. | Pass |
| Parent/origin safety | Dynamic children inherit original_tag = THIS; fixed tags are used only to exclude incompatible Chaos identities from host selection. | Pass |
| Lock safety | Pending claimant choices, family actions, natural derivative release, scenarios, same-tag cleanup, and combat trials retain locks through proof or retry. | Pass |
| Cooldown safety | Requests, family actions, and combat trials apply cooldowns only on their defined commit/resolution path. | Pass |

## Files inspected

### Repository and implementation guidance

- AGENTS.md
- .agents/skills/chaos-redux-events/SKILL.md
- .agents/skills/chaos-redux-subagents/SKILL.md
- .agents/skills/chaos-redux-decisions-missions/SKILL.md
- .agents/skills/chaos-redux-focus-trees/SKILL.md
- .agents/skills/chaos-redux-mtth/SKILL.md

### Offline wiki and vanilla documentation

- The required offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus, Interface Modding, Scripted GUI Modding, Achievements, Divisions, Characters, and Equipment.
- Vanilla effects_documentation.md, triggers_documentation.md, modifiers_documentation.md, script_concept_documentation.md, dynamic_variables_documentation.md, scripted GUI documentation, decision documentation, character documentation, equipment documentation, MTTH documentation, on-action documentation, and common/script_constants/documentation.md.
- Vanilla army-leader combat callback, dynamic unit creation/deletion, and one-state civil-war/release precedents.

### Event 19 design sources

- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_1_core.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_2_spawn_engine_and_baseline.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_3_evolutions_i_and_ii.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_4_evolution_iii.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_5_evolution_iv.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md
- docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md
- docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md
- Event 19 route graph, AI matrix, country package matrix, decision/mission map, evolution entry/cleanup matrix, possessed-general matrix, spawn-composition matrix, research notes, scope-boundary review, and acceptance review files under docs/specs/019_infantry_spawn_specs.

### Live Event 19 gameplay

- events/019_infantry_spawn.txt
- events/019_infantry_spawn_scenario.txt
- common/decisions/019_infantry_spawn_decisions.txt
- common/decisions/019_infantry_spawn_claimant_decisions.txt
- common/decisions/019_infantry_spawn_derivative_decisions.txt
- common/decisions/categories/019_infantry_spawn_decision_categories.txt
- common/decisions/categories/019_infantry_spawn_claimant_categories.txt
- common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt
- common/on_actions/019_infantry_spawn_achievement_on_actions.txt
- common/on_actions/019_infantry_spawn_derivative_on_actions.txt
- common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt
- common/ai_strategy/019_infantry_spawn_scenario_ai_strategy.txt
- common/ideas/019_infantry_spawn_ideas.txt
- common/ideas/019_infantry_spawn_derivative_ideas.txt
- common/mtth/019_infantry_spawn_mtth.txt
- common/national_focus/019_infantry_spawn_derivative_focus.txt
- All 17 common/scripted_effects/019_infantry_spawn_*.txt live files.
- All eight common/scripted_triggers/019_infantry_spawn_*.txt live files.
- All seven common/script_constants/019_infantry_spawn_*.txt live files.
- common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt
- common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt
- common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt
- interface/019_infantry_spawn.gfx
- interface/019_infantry_spawn_muster_board.gui
- localisation/english/019_infrantry_spawn_l_english.yml

### Cross-event registration and death accounting

- common/on_actions/002_zombie_outbreak_on_actions.txt
- common/on_actions/005_soviet_collapse_on_actions.txt
- common/on_actions/010_death_on_actions.txt
- common/script_constants/chaos_meter_constants.txt
- common/scripted_effects/chaosx_dynamic_effects.txt and its documentation where called by Event 19.

Existing Event 19 audit and handoff reports in the plans folder were not consulted for their findings.

## Targeted validation evidence

- Repository-wide provider-definition search returned exactly one Event 19 provider-definition file: common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt.
- Direct parse counted 68 decision ai_will_do blocks for 68 decisions.
- Direct parse counted 45 derivative focus blocks.
- Direct visual-slot inventory counted 20 claimant, six host, and one neutral slot.
- Event 19 on-action scan found no daily, weekly, monthly, or yearly on_action.
- World-scope scan found only manifestation, four stage activations, scenario launch/cleanup, and the scenario-roster terminal query described above.
- Dynamic-country output scan found original_tag = THIS on both scenario and natural-derivative creation paths.
- No transfer_units_fraction or Event 19 world_end mutation was found.
- The 16 SCN-013 type/intensity combinations were traced individually through input validation, dispatch, package proof, and cleanup.

## Simplifications, omissions, and blockers

| Category | Count | Detail |
|---|---:|---|
| Unapproved simplifications | 0 | None. |
| Unapproved fallbacks | 0 | None. |
| Accepted substitutes | 2 | Controlled one-formation border trials for four combat achievements; exact recorded-formation recreate/prove/delete for loyal transfer. |
| Audit omissions | 0 | All requested AI, balance, performance, isolation, scenario, transaction, lifecycle, and exploit surfaces were inspected. |
| Blockers | 0 | None. |

## Final conclusion

The audited live Event 19 implementation has zero P0, zero P1, and zero P2 findings in the requested AI, balance, performance, isolation, scenario-safety, and exploit surface. No gameplay, documentation, asset, localisation, interface, or workbook file was changed by this audit; this handoff is the sole audit artifact.
