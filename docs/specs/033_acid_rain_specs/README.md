# Event 033 Acid Rain specification package

## Event identity

| Field | Accepted value |
| --- | --- |
| Event ID | `33` |
| Event slug | `acid_rain` |
| Event name | Acid Rain |
| Event type | Major, fires once per campaign |
| Catalog status | Needs Testing (agent decision D21, applied to the workbook in commit `02cf2601e`) |
| Chaos level | 2, Gathering Storm minimum |
| Cluster | Natural Disasters (cluster 5), sixth optional member after Event 13's five logical slots |
| Cluster role | Severe optional member |
| Ordinary endpoint | Dissipation after complete coverage of the frozen valid states |

## Accepted event concept

An anomalous and possibly supernatural acid-rain system forms over one world region and moves through changing state footprints.
The rain is intrinsically lethal: direct exposure, corrosive aerosol, poisoned runoff and the collapse of exposed services kill civilians.
Every opening shock and sustained pulse removes real civilian population from the affected state and records the exact applied loss once in the shared Deaths ledger.
Transport damage, building damage, supply penalties and environmental aftermath accompany those losses.
The system cannot become eligible to dissipate until every frozen valid state has been touched at least once.

## Implementation status

Event 033 is implemented in source and is in the active Events 1-40 milestone; the runtime description lives in [the event overview](../../events/033_acid_rain/overview.md).
This package is the design the implementation must satisfy.
Each spec part opens with a status line that separates implemented design from pending work.
Live-game behavior (actual population removal, save and reload, multiplayer, performance, layout, animation and audio playback) is verified by the user; agents supply source and offline evidence only.

| Area | Status | Owning section |
| --- | --- | --- |
| Major registration, Chaos level 2, cluster slot 6, mixed Major pacing | `implemented` | Parts 7 and 11 |
| Formation transaction, frozen registry, region index, generation IDs, bounded host worker | `implemented` | Part 2 |
| Fronts, warnings, coverage, revisits, islands, dissipation ladders | `implemented` | Part 3 |
| Exact state-population mortality (Deaths reason 34, `acid_rain`) | `implemented` | Part 4 and the population-loss contract |
| Damage pressure, acute bands, seven-input aftermath classifier | `implemented` | Part 4 and the consequence repair acceptance |
| Preparedness, projects, urgent operations, recovery, costs | `implemented`; the costs match the decision cost matrix | Part 5 |
| Decision AI | `implemented`; the probability comparison at current source pins is pending | Part 8 |
| Air source 5 with 1,500 bp lifetime and 5,000 bp ceiling caps | `implemented` | Part 11 |
| Three cumulative evolutions with per-stage enable controls | `implemented` | Part 7 |
| Reports, world notices, super-event 117 with verified quote and audio | `implemented` | Part 9 |
| World map and category inlay | `implemented`; D37 regional state strips `accepted and queued`; the player-facing value budget is `implemented` | Part 6 |
| Visual assets and animations | delivered; D37 regional overlays in production | Part 10 |
| Ten achievements and Event Details status | `implemented` | Part 10 |
| Humanitarian (famine) pressure addition | `implemented` | Parts 4 and 11 |
| Source-specific Humanitarian retirement | dropped (accepted); the famine owner's disaster context expires on its own | Consequence repair acceptance, Open questions |
| Event 13 overlap exclusion | dropped (accepted); never implemented | Part 7, Open questions |
| Prototype save migration | `implemented` | Part 11 |
| Legacy severe-report receipt migration (F7) | `unresolved` | [Runtime resume](../../plans/033_acid_rain_plans/runtime_resume_2026_10_08.md) |

## Reading authority

1. The two accepted addenda refine the numbered parts where they overlap: [achievement threshold and launch origin](specs/033_acid_rain_achievement_threshold_and_launch_acceptance.md) and [consequence repair acceptance](specs/033_acid_rain_consequence_repair_acceptance_2026_10_03.md).
2. Each part's "Accepted implementation decisions" section records agent decisions D1 to D37 from [the agent decision log](../../plans/033_acid_rain_plans/agent_decisions_2026-10-04.md), taken under the full Event 033 design authority the user granted on 2026-10-04.
3. The numbered parts and matrices hold the remaining design.
4. Prompts are resume handoffs that point to those owners; they carry no independent requirements.
5. Research, alignment, readiness and quality files are supporting records.

Resume from current source and the plans folder before scheduling any work, and never restart from the retired continent prototype.

## Invariants

Each invariant has one owning section; other files point to it rather than restating it.

- Mortality is a real state-population transaction through `apply_exact_state_civilian_population_loss`: Part 4 and the population-loss contract.
- Air additions are clamped to the request, the 1,500 bp lifetime allowance and the 5,000 bp global ceiling: Part 11.
- Runtime work is bounded to event-owned registries, with no daily or weekly world scan: Part 2.
- Dissipation needs complete coverage and always reaches a guaranteed check: Part 3.
- Event 33 adds direct Chaos only at mapped physical outcomes and never repeats the Deaths or Air conversions: Part 1.
- Preparedness is the only national value the player manages; everything else shown is status or history: Part 6.

## File index

### Specifications

| File | Purpose |
| --- | --- |
| `specs/033_acid_rain_spec_part_1_core_and_player_loop.md` | Concept, phases, player loop, managed value, outcomes and direct Chaos |
| `specs/033_acid_rain_spec_part_2_runtime_and_state_contract.md` | Data model, formation transaction, pulses, cleanup and performance contract |
| `specs/033_acid_rain_spec_part_3_fronts_coverage_and_dissipation.md` | Region selection, footprints, warnings, coverage and guaranteed dissipation |
| `specs/033_acid_rain_spec_part_4_mortality_damage_and_environment.md` | Mortality model, Deaths integration, building pressure, acute bands and aftermath |
| `specs/033_acid_rain_spec_part_5_preparedness_decisions_and_recovery.md` | Preparedness, projects, urgent operations, country scaling and recovery |
| `specs/033_acid_rain_spec_part_6_scripted_gui_and_presentation.md` | World map, category inlay, player-facing value budget and GUI read model |
| `specs/033_acid_rain_spec_part_7_evolutions_and_cluster_integration.md` | Evolutions, cluster role, mixed Major pacing and Event 13 overlap |
| `specs/033_acid_rain_spec_part_8_ai_balance_and_probability.md` | AI priorities, reserves, balance levers and probability evidence |
| `specs/033_acid_rain_spec_part_9_reports_super_event_and_text_direction.md` | Event graph, reports, super-event and writing direction |
| `specs/033_acid_rain_spec_part_10_assets_animation_and_achievements.md` | Asset inventory, animation and the ten achievements |
| `specs/033_acid_rain_spec_part_11_integrations_migration_and_save_safety.md` | Deaths, Air, CBRN, Humanitarian, migration, save safety and terminal transitions |
| `specs/033_acid_rain_spec_part_12_validation_and_acceptance.md` | Acceptance gates, split into agent evidence and user live checks |
| `specs/033_acid_rain_achievement_threshold_and_launch_acceptance.md` | Accepted per-state evacuation threshold and durable launch origin |
| `specs/033_acid_rain_consequence_repair_acceptance_2026_10_03.md` | Accepted consequence repairs and current claim dispositions |

### Matrices

| File | Purpose |
| --- | --- |
| `matrices/033_acid_rain_front_state_matrix.md` | Phase, front-slot and state-exposure transitions |
| `matrices/033_acid_rain_decision_cost_matrix.md` | Project, urgent and recovery costs and durations, matching the constants file |
| `matrices/033_acid_rain_ai_acceptance_matrix.md` | Twenty AI cases A1 to A20 |
| `matrices/033_acid_rain_requirement_traceability.md` | User requirement to specification and gate map |
| `matrices/033_acid_rain_population_loss_contract.md` | Exact state-population transaction and failure criteria |

### Supporting records

| File | Purpose |
| --- | --- |
| `research/033_acid_rain_science_and_source_research.md` | Environmental references and the verified quote and audio sources |
| `research/033_acid_rain_visual_reference_board.md` | Ten-reference visual board with license notes |
| `docs_alignment/033_acid_rain_catalog_and_cluster_alignment.md` | Catalog, cluster and Event Details alignment, now applied |
| `implementation_readiness/033_acid_rain_file_map_and_migration.md` | Implemented file map and remaining work |
| `quality/033_acid_rain_improvement_loop_review.md` | Original design review with current resolution notes |

### Prompts

| File | Purpose |
| --- | --- |
| `prompts/033_acid_rain_goal_prompt.md` | Short resume objective for the remaining Event 033 work |
| `prompts/033_acid_rain_coding_prompt.md` | Implementation resume handoff and completion blockers |
| `prompts/033_acid_rain_decision_mission_prompt.md` | Decision and AI resume handoff |
| `prompts/033_acid_rain_achievement_prompt.md` | Achievement audit handoff |
| `prompts/033_acid_rain_asset_prompt.md` | Remaining asset production handoff (D37 regional strips) |
| `prompts/033_acid_rain_super_event_prompt.md` | Super-event record and change rules |

## Open questions

Parent acceptance, 2026-10-10 (release orchestrator, under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger): items 1 to 5 are accepted as proposed, with urgent actions resolving inside the 7-day warning, and are `accepted and queued` for the Event 033 implementation owner.
They supersede the conflicting parts of the 2026-10-03 consequence acceptance and agent decision D33 named below.
Still `unresolved`: the F7 receipt migration, the probability comparison, and the D37 regional art.
Implemented 2026-10-10 by the Event 033 owner: the player-facing value budget (item 3), national urgent actions of 4, 5, 5 and 6 days (Shelter, Medical, Transport, Water and Food; item 2), the Gathering Storm exception in `event_cluster_get_member_effective_min_tier` (item 4), and removal of the Humanitarian retirement and Event 13 exclusion requirements from code and documents (items 1 and 5).

1. **Humanitarian retirement (accepted).** The 2026-10-03 consequence acceptance keeps source-specific retirement of Acid Rain famine pressure as a required dependency.
   Since the 2026-10-10 famine rework, an accepted request adds a self-decaying food shock and renews a 60-day disaster food context that expires on its own and does not stack.
   Proposal: retire the reversible source-33 ledger requirement and treat the expiring famine context as the complete integration, because the proposed owner patch adds a private ledger for a contribution the player cannot see separately.
2. **Urgent action timing (accepted: resolve inside the 7-day warning).** The accepted matrix gives Shelter Protocols, Medical Surge and Reroute Transport 14 days and emergency water 21 days, while a front warning gives 7 days, so no urgent action started on a warning protects the opening shock.
   Proposal: either shorten the national urgent actions to 5 to 7 days or grant half their protection after one full day, as evacuation already does, so the warning becomes a real decision point.
3. **Player-facing value budget (accepted).** Part 6 proposes removing the remaining Air allowance, current global Air, the national Air line, the visit quota and visit progress, front active-state counts and separate global-phase clocks from the interface; this trims surfaces that agent decision D33 implemented.
4. **Cluster Severe floor (accepted: Gathering Storm entry stands).** `docs/systems/event_system/event_clusters_spec.md` records a common Severe-member floor of Chaos Tier, while Part 7 gives Acid Rain a 20 percent participation from Gathering Storm; the cluster owner must confirm the exception.
5. **Event 13 overlap (accepted: exclusion dropped).** Part 7's original rule that Event 13 may not place a weather impact under an Acid Rain severe cell was never implemented and needs an Event 13 change.
   Proposal: drop the exclusion and keep the implemented integration, in which an open Event 13 card adds one point to the Acid Rain aftermath classifier.

## Changelog

### 2026-10-10 orchestrator review

- Recorded the parent acceptance of open questions 1 to 5 and the items that remain unresolved.

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Merged the redundant `manifest.md` file index into this README and deleted it; replaced the obsolete implementation order with an implementation status table.
- Updated the catalog status to Needs Testing, the Deaths cause to reason 34, the Air source to id 5 and the super-event to id 117 with its verified quote and audio.
- Marked every spec part with its implementation status and reconciled stale claims: prototype replacement and migration are done, event IDs are fixed, the asset paths and frame sheets match the delivered files, and the 1920x1080 renderer limit is historical.
- Removed Codex-specific instructions (`fork_turns`, `.agents` skill links, `AGENTS.md`, native ImageGen) and the debug-playtest tool requirement; agents never launch the game, so live checks are user-owned in Part 12.
- Trimmed the prompts to resume handoffs that point to their owning parts instead of restating costs, gates, achievement text and probability tool lists.
- Reconciled Humanitarian text with the famine rework: requests open a 60-day disaster food context and a decaying shock, and evacuation stays disaster pressure rather than a migration cohort.
- Replaced the unimplemented Event 33 source-pressure estimate with the shared Air ledger's current row, which the dissipation penalty already reads.

Pass 2, design improvement:

- Reframed World Coverage as a progress readout and Preparedness as the only managed national value.
- Added a player-facing value budget to Part 6 that keeps only values tied to a player decision and moves internal clocks, quotas and caps to the debug overlay.
- Recorded the urgent-timing, Humanitarian retirement, cluster-floor and Event 13 overlap proposals as open questions instead of overriding accepted decisions.
- Stated that the division-level CBRN attrition reduction is not required because no shared division interface exists, and added the indirect famine-to-migration link and the absence of a condemnation link to Part 11.
