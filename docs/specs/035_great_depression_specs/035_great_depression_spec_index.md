# Event 35: Great Depression 2.0 specification package

## Location and role

This package lives at `docs/specs/035_great_depression_specs/` and is the design source for Event 35, Great Depression 2.0.
This index is the package README.
The eleven numbered parts own the design.
The decision map, state lifecycle map, AI probability matrix and reusable crisis API are supporting design files that the parts point to.
The prompts are short continuation prompts that point back to owning sections instead of restating them.
Repository rules come from [CLAUDE.md](../../../CLAUDE.md), and subagent routing comes from [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Catalog identity

- Event ID: `35`, entry event `chaosx.nr35.1`.
- Event name: Great Depression 2.0.
- Type: Minor Repeatable.
- Chaos level: 1 (Calm World).
- Cluster: Negative Economy (cluster ID 10), Low member, with Event 50 The Great Embargo as the optional Medium member.
- Direct source event: Event 34 Industrial Boom.

## Design promise

Great Depression 2.0 places one major country or player-controlled country inside a long economic crisis that changes production, construction, logistics, politics and state development.
The player manages one public number, Depression Severity, through one ordinary decision category and a small set of state recovery projects in its Depression Centers.
An independent firing begins as a severe but recoverable national depression.
A collapse from Event 34 starts or deepens the same crisis, inherits the boom's evolution floor and converts the failed boom into the opening depression state.
The event remains playable at maximum Severity, and deep failure works through bounded, visible chains rather than one threshold.
Recovery requires sustained improvement, resolved centers and a final proof period.
Repeat firings remember reforms and scars without becoming a renewable factory deletion or a permanent reward.

## Implementation status

Event 35 has a substantial runtime implementation in the active Events 1-40 milestone.
The runtime contract is documented in [`docs/events/035_great_depression.md`](../../events/035_great_depression.md) and the companion effect documents under `common/scripted_effects/035_great_depression_*.md`.
Implementation tranches, agent decisions, audits and test results live in [`docs/plans/035_great_depression_plans/`](../../plans/035_great_depression_plans/), with the current requirement ledger in `current_requirement_state_2026-10-07.md` and catalog work in `catalog_changes_pending.md`.
Implementation evidence proves what exists in source; it does not prove live engine behaviour or balance.

| Surface | Status | Evidence or remaining work |
| --- | --- | --- |
| Targeting, event-pool availability, rejected-firing report `chaosx.nr35.22` | `implemented` in source | Event doc, Overview and Report and news pacing |
| Start-or-deepen API, five callers, private receivers `.8` and `.9` | `implemented` in source | [Reusable crisis API](035_great_depression_reusable_crisis_api.md), event doc Reusable crisis API |
| Severity, bands, trend, phases, relapse, maximum emergency, National Breakdown | `implemented` in source | Part 2; the national pulse is a fixed weekly pulse |
| Six doctrines, 68 ordinary decisions and 17 missions, merged action families, phase-gated visible-action budget, custom costs, tooltips without hidden points | `implemented` in source | Part 3, decision map; counts from `.tools/test_event035_visible_actions.py` |
| Bank holiday, 21-day audit and 42-day recapitalization | `implemented` in source | Part 3 Doctrine 3 |
| Depression Centers, condition-scaled project duration, transfer and cleanup | `implemented` in source | Part 4 |
| Regional Works Program physical results (nine needs) | `implemented` in source | Part 3 Doctrine 1 |
| Public Works unused-budget return | `implemented` in source | Part 3 Doctrine 1; escrow helpers are wired into payment, completion, failure, transfer and cleanup |
| Lasting-capacity closure | pending | The physical legacy of Convert Works into Lasting Capacity is not built |
| Recovery outcome, legacies, five country scars, two district outcomes, recovery report | `implemented` in source | Part 4 Recovery outcomes |
| Financial Contagion network, partner actions, conversion, reports and news | `implemented` in source | Part 5 |
| Social Collapse ladder, movements, coup, autonomy, Event 21 civil-conflict handoff, political aftermath | `implemented` in source | Part 6 |
| The Second Great Depression, conference, devaluation, withdrawal, blocs, world news, super-event | `implemented` in source | Part 7 |
| Event 34 supplier choices inside Event 34's category | two choices (accept, refuse) on the Event 34 side; the Event 35 quote adapter is `implemented` | Part 7 Supplier choices |
| Event 34 inheritance: snapshot, evolution floor, inherited-liability pressure | `implemented` in source | Part 8 |
| Inherited hidden-row paid paths, corridor outcomes, salvage, multi-region priority | `rejected` | Part 8; hidden corridor states stay national inheritance pressure and recovery runs through the visible centers |
| Famine and migration center adapters, Event 21 civil-conflict adapter | `implemented` in source | Part 8 Connections |
| Famine-to-depression feedback and hunger-riot gate, contamination hold on reopening certification, sanction trade stress and Finance and Trade cost | `implemented` in source | Part 8 Connections; `.tools/test_event035_connections.py` |
| Disaster adapter | pending | Part 8 Connections |
| Event 35 Chaos receipts | `implemented` in source | Part 8 Chaos accounting; the worldwide wave is 10, contagion pays once per chain, national recovery relief is removed |
| Six achievements, Event 34 Long Fall assets, 80 runtime DDS files, super-event slot 105 and audio 106 | `implemented` in source | Part 10, Part 11 |
| Asset workspace `docs/assets/035_great_depression/` cleanup | pending | Part 10 Asset workspace |
| Probability evidence for named scenarios | partial | Part 9 and the matrix; several `hoi4.probability_*` runs timed out or returned partial results, so source-derived calculations remain owed for most surfaces |
| Catalog workbook rows | `accepted and queued` | `catalog_changes_pending.md` |
| Live-game validation | user-owned | Part 11 acceptance groups |

## Acceptance basis

U1, the user's explicit instruction recorded in `current_requirement_state_2026-10-07.md`, accepts this package as the full implementation target without simplifications.
The user also granted the implementing agent full design authority for the Event 35 takeover (G6).
Decisions taken under that grant are recorded with their basis in `agent_decisions_2026-10-04.md` (D1-D30 and lead decisions L1-L8) and `agent_decisions_2026-10-05.md` (D31-D44), and they count as parent acceptance within the user-authorized scope.
Where a recorded decision narrowed a U1 requirement (D4 and L8 on inherited hidden rows and Event 34 supplier choices), the 2026-10-10 parent acceptance settles it: hidden-row work is `rejected` and the supplier choices are two choices on the Event 34 side (Decisions below).
The presentation choice is settled by the October 6 takeover decision under G6: one ordinary category with its static picture and a three-line formatted header, no meter and no dedicated scripted GUI (part 3 Presentation).
The proposals of the 2026-10-10 audit were accepted and implemented on the same day (Decisions below).

## Central design decisions

1. Depression Severity (0 to 100) is the only number the player manages; everything else the player sees is a short label (part 2, Player-facing value budget).
2. One ordinary decision category with a static picture presents the crisis; there is no dedicated scripted GUI.
3. One fail-closed start-or-deepen transaction serves every entry; only independent firing owns normal pacing.
4. Depression Centers are a small sparse state set (one to three, rarely four) that carry the local face of the crisis.
5. Physical factory loss happens only after sustained failure in a closed center or through deliberate liquidation.
6. Evolution activation adds zero Chaos; Event 35 adds Chaos only for concrete abnormal outcomes that no shared counter already records.
7. Shared owners keep food, displacement, deaths, civil war, condemnation, contamination and disaster damage; Event 35 submits bounded requests and reads public state.
8. All tuning lives in `common/script_constants/035_great_depression_constants.txt` and `035_great_depression_region_constants.txt`.

## Package map

| File | Purpose |
| --- | --- |
| `035_great_depression_spec_part_1_core.md` | Identity, targeting, entry modes, opening shock, phases, outcome bands, war and peace, country changes |
| `035_great_depression_spec_part_2_severity.md` | Severity scale, player-facing value budget, hidden components, pulse, thresholds, relapse, maximum emergency |
| `035_great_depression_spec_part_3_decisions_missions.md` | Presentation, doctrines, action families, missions, costs, decision-surface budget |
| `035_great_depression_spec_part_4_centers_recovery_repeatability.md` | Depression Centers, projects, factory loss, recovery outcomes, legacies, scars, repeatability, exploits |
| `035_great_depression_spec_part_5_financial_contagion.md` | Evolution I network, partner actions, conversion, anti-loop rules |
| `035_great_depression_spec_part_6_social_collapse.md` | Evolution II ladder, movements, responses, extreme gates, aftermath |
| `035_great_depression_spec_part_7_second_great_depression.md` | Evolution III global lifecycle, international actions, suppliers, global recovery |
| `035_great_depression_spec_part_8_inheritance_connections_chaos_cluster.md` | Event 34 inheritance, cross-system connections, Chaos accounting, cluster, logs |
| `035_great_depression_spec_part_9_ai_probability_balance.md` | AI profiles, named scenarios, balance targets, exploit audit, performance |
| `035_great_depression_spec_part_10_presentation_assets_text.md` | Presentation hierarchy, asset families, writing direction |
| `035_great_depression_spec_part_11_achievements_acceptance.md` | Six achievement contracts, acceptance scenario groups, completion evidence |
| `035_great_depression_decision_map.md` | Phase visibility matrix, doctrine action map, route flows, mission capacity, cost families |
| `035_great_depression_state_lifecycle_map.md` | National and center lifecycles, ownership and civil-war maps, recovery and cleanup maps |
| `035_great_depression_ai_probability_matrix.md` | Weighted-surface inventory and comparison contract for the part 9 scenarios |
| `035_great_depression_reusable_crisis_api.md` | Accepted field contract of `great_depression_start_or_deepen` |
| `035_great_depression_research_notes.md` | Historical and economic design references |
| `035_great_depression_coding_prompt.md` | Continuation prompt for the remaining implementation work |
| `035_great_depression_goal_prompt.md` | Compact continuation goal |
| `035_great_depression_decision_mission_prompt.md` | Decision and mission audit prompt |
| `035_great_depression_asset_prompt.md` | Asset repair brief (production delivered) |
| `035_great_depression_achievement_prompt.md` | Achievement audit brief (contracts implemented) |
| `035_great_depression_super_event_prompt.md` | Super-event repair brief (super-event delivered) |

## Decisions

Parent acceptance, 2026-10-10 (release orchestrator, under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger): the seven audit proposals were accepted and are `implemented` by the Event 035 owner on 2026-10-10, except where noted.

1. Weekly pulse (part 2): `implemented`.
   The national pulse is a fixed 7-day pulse with elapsed-day normalization; the phase intervals are removed.
2. Decision surface (part 3): `implemented`.
   Clearing Agreement replaces the four clearing actions, Protect the Home Market the three protectionist actions, Abandon the Distressed Market (with a quiet form for allies) the two market exits, Emergency Credit the three partner-aid actions and Coordinated Public Works and Reconstruction the four reconstruction actions.
   Lead decision L2 is superseded by this merge.
   Every action shows only in its phases, and part 3 records the measured visible counts.
3. Tooltip detail (part 3): `implemented`.
   Tooltips state the effect in plain words and print no hidden component points.
4. Chaos values (part 8): `implemented`.
   The worldwide wave adds 10, a contagion chain pays 2 once plus one 3 milestone at its third conversion, and the 2-point national recovery relief is removed.
5. Event 34 supplier choices (part 7): `implemented` on the Event 34 side as two choices, Accept World Orders and Refuse Further Exposure, through the Event 35 quote adapter.
6. Inherited hidden rows (part 8): `rejected`.
   Paid actions on hidden rows and salvage are dropped; hidden corridor states stay national inheritance pressure and corridor recovery runs through the visible centers.
7. Public Works unused-budget return (part 3): `implemented`.
   The return is shown as one line on interruption with no running balance.

## Changelog

### 2026-10-10 orchestrator review

- Recorded the parent acceptance of all seven open proposals.

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Turned this index into the package README with an implementation status table, the acceptance basis (U1, G6, D and L records) and a package map; replaced `AGENTS.md` and `.agents/` links with `CLAUDE.md` and `.claude/skills/`.
- Removed the stale planning-environment statements (ChatGPT container, unmounted wiki and MCP, "public repository" stub migration).
- Deleted six redundant files: `035_great_depression_full_spec.md` (superseded reading guide), `035_great_depression_package_manifest.md` (stale hash inventory), `035_great_depression_repository_crosscheck.md` (pre-implementation stub migration), `035_great_depression_source_reading_ledger.md` and `035_great_depression_subagent_review.md` (planning-pass records superseded by the plans folder and the subagent skill), and `035_great_depression_chaos_impact_map.md` (merged into part 8 Chaos accounting).
- Recorded the presentation choice as settled by the October 6 takeover decision: static picture with a three-line formatted header, causes and next threshold on the national-spirit hover, no meter.
- Reconciled the parts with implemented behaviour: bank audit and recapitalization timing, condition-scaled project duration, Regional Works needs, Strategic Industry closers, market exits that charge the partner, conference and bloc rules, recovery legacies and scars, district outcomes, recovery and evolution reports, world news, MTTH bases, center stage set, and achievement identifiers.
- Rewrote the coding, goal, decision-mission, asset, achievement and super-event prompts as short continuation or audit prompts that point to owning sections; removed their stale mission, status and stage names.
- Replaced the planning-completion and improvement-loop sections of part 11 with the current acceptance boundary.

Pass 2, design improvement:

- Added a player-facing value budget (part 2): Severity is the only number, and band and trend, phase and doctrine, center condition, partner exposure stage, social condition and world stage are single labels.
- Added a decision-surface budget and a measurable visible-action check (part 3) and listed the duplicated actions as a consolidation proposal.
- Rebuilt the Chaos accounting in part 8 around the implemented receipts, checked them against the shared counters (Event 35 coups do not fire the shared coup counter, the shared civil-war counter is disabled and Event 21 adds no Chaos, so neither receipt double counts today), and proposed values scaled to the shared Chaos meter.
- Reworked cross-system connections in part 8: kept famine, migration and Event 21 adapters, added a famine-to-depression feedback and a hunger-riot gate on the famine owner's food stage, made contamination and fallout block center reopening rather than add another number, routed sanctions through Event 50 and condemnation, and dropped the Random Riches link and any camp link as decoration.
- Removed the claim that security responses create Event 35 deaths; deaths reach the Deaths ledger only through famine and Event 21.
- Replaced the six-item state scar list with the two implemented district outcomes, and replaced the old reform examples with the implemented legacy relief and weakness pairs.

### 2026-10-10 implementation

- Fixed the weekly pulse, merged the duplicated actions, removed hidden pressure points from tooltips, rescaled the Chaos receipts and wired the Public Works return.
- Added the phase-gated visible-action budget and its measured counts to part 3 and the decision map, with a regression test.
- Implemented the famine, contamination and sanction connections of part 8 and removed the Random Riches and camp links from the plan.
- Recorded the two Event 34 supplier choices as an Event 34 surface and dropped the inherited hidden-row work.
