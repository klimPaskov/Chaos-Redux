# Event 018 Resources Found Planning Package

This package is the accepted source design for Chaos Redux Event 018, Resources Found.
Event 018 is implemented.
The current implementation record is [`docs/events/018_resources_found/overview.md`](../../events/018_resources_found/overview.md), with the cave country in [`cave_country.md`](../../events/018_resources_found/cave_country.md) and the helper contracts in [`helper_contracts.md`](../../events/018_resources_found/helper_contracts.md).
The latest accepted presentation and cost decisions are in [`agent_decisions_2026-10-05.md`](../../plans/018_resources_found_plans/agent_decisions_2026-10-05.md).
The specification parts keep their planning-era requirement language for design traceability; where a part says "should", the implemented behavior is described in the overview, and the 2026-10-10 notes inside each part mark where the current source differs from or resolves the planning text.

The event remains Minor Repeatable and is the required primary-trigger member of Positive Economy, cluster 7, at Medium severity.
The cluster unlocks at Chaos Meter tier 3 (`constant:event_cluster_economy_positive.unlock_tier`), and the Event 018 member row uses the same minimum tier (`chaosx_event_cluster_effects.txt`, `load_event_cluster_members`).
Its ordinary firing is a large strategic-resource discovery.
Repeated investment can turn that discovery into a trade center, a concession struggle, a border crisis, a lethal excavation, a public monster emergency, and finally a playable nonhuman cave country.
The world-end branch begins only after the cave country consumes a continent and global chaos is above 1000.

Labels described as working labels are internal design handles, not final localisation.
The implemented player-facing names are listed under Implemented identity resolution below.

## Package statistics

- 8 sequential source-spec parts
- 6 implementation matrices
- 1 focus architecture map
- 6 historical implementation prompts
- 4 research and review notes

The root `manifest.md` records current file sizes, word counts, and SHA-256 checksums.
Current workflow ownership comes from [the routing owner skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md), rather than dated runtime limitations.

## Package map

### Specifications

- `specs/018_resources_found_spec_part_1_core_and_baseline.md`
- `specs/018_resources_found_spec_part_2_resource_field_mechanic.md`
- `specs/018_resources_found_spec_part_3_trade_diplomacy_and_border_conflict.md`
- `specs/018_resources_found_spec_part_4_evolutions.md`
- `specs/018_resources_found_spec_part_5_cave_country_package.md`
- `specs/018_resources_found_spec_part_6_focus_tree_and_brood_warfare.md`
- `specs/018_resources_found_spec_part_7_world_end_aftermath_and_connections.md`
- `specs/018_resources_found_spec_part_8_ai_text_assets_and_acceptance.md`

### Matrices

- `matrices/event_chain_map.md`
- `matrices/decision_mission_matrix.md`
- `matrices/ai_strategy_matrix.md`
- `matrices/country_package_matrix.md`
- `matrices/tuning_and_balance_framework.md`
- `matrices/acceptance_criteria.md`

### Focus architecture

- `focus_graphs/cave_host_focus_architecture.md`

### Research and review

- `research/catalog_reconciliation.md`
- `research/historical_and_folklore_research.md`
- `research/improvement_loop_review.md`
- `research/source_corpus_read_log.md`

### Historical implementation prompts

These prompts are the original build contracts.
Event 018 is implemented, so they must not be re-executed as build orders.
New work starts from the overview, the open questions below, and the current source.

- `prompts/resources_found_asset_prompt.md`
- `prompts/resources_found_super_event_prompt.md`
- `prompts/resources_found_achievement_prompt.md`
- `prompts/resources_found_decision_mission_prompt.md`
- `prompts/resources_found_coding_prompt.md`
- `prompts/resources_found_goal_prompt.md`

## Design non-negotiables

1. The discovered resource type is fully random across the standard strategic-resource pool.
2. The baseline deposit is large, centered around 100 resource production in one valid state.
3. Event-added resources are tracked separately from the state’s original resources so successful closure removes only Event 018 additions.
4. Repeated discoveries can stack the same resource in the same state.
5. The owner receives a decision category with a compact resource-field management surface.
6. Trade, concessions, smuggling, espionage, demilitarization, and border conflict react to the value and location of the field.
7. Evolution II and Evolution III progress gradually even when the first firing occurs at a high evolution stage.
8. A successful pre-breach closure permanently prevents the cave-country branch for that site and removes every Event 018 resource addition from the state.
9. Evolution IV creates a fully playable nonhuman country led by a literal cave monster.
10. The cave country has no manpower or equipment economy and cannot train normal divisions.
11. Its starting army scales with historical exploitation and is capped at 30 divisions.
12. The starting state is excluded from future captured-state brood calculations.
13. Each captured resource state provides one brood-capacity point per 10 total resources, capped at 10 points for that state.
14. New cave divisions appear automatically from captured resource capacity.
15. Cave units are very slow, heavily armored, and countered primarily by serious hard attack.
16. The cave country declares war on every current and newly created land neighbor.
17. The world-end branch requires a consumed continent, chaos above 1000, and no existing world-end state.
18. The world-end branch opens stronger cave footholds on other continents and freezes incompatible random-event progression.
19. The event’s first layers remain economically attractive. The horror is earned through excavation choices and repeated escalation rather than revealed in the first popup.
20. No fallback, placeholder asset, unresearched super-event text, or generic country package counts as completion.

## Implemented identity resolution

The planning parts use working labels.
The implementation resolved them as follows; the overview and the cave-country document remain the authority for details.

| Working label or open choice | Implemented identity |
| --- | --- |
| The Deep Host, persistent cave country | Tag `DHO`, the Oth-Kesh Host, sub-ideology `resonant_brood_hierarchy`, ruling institution The Resonant Maw, sovereign Vhorruk |
| World-end cosmetic identity | The World Below |
| Cave Monster Brood division family | Five templates: War-Brood, Stone Phalanx, Burrow Column, Scree Pack, Feeding Guard |
| Event chain ordinals | `chaosx.nr18.1` to `.99` as listed in `matrices/event_chain_map.md`, plus `.33` for unsuccessful manual survey preparation, and news events `chaosx.news.84` to `.89` |
| Super-event slots | Displays 82 emergence, 83 world end, 84 global defeat, with audio IDs 54, 55, 56, documented in `docs/super_events/018_resources_found/overview.md` |
| Achievement concepts | Fifteen achievements, documented in `docs/achievements/018_resources_found/achievements.md` |
| Focus tree scale | 67 focuses in `common/national_focus/018_resources_found_cave_focus_tree.txt` |
| Field header | Three core values (Yield, Depth, Safety) plus one contextual slot, accepted 2026-10-05 |
| Tuning | `common/script_constants/018_resources_found_constants.txt`, `018_resources_found_decision_constants.txt`, `018_resources_found_cave_constants.txt`, `018_resources_found_foreign_interest_constants.txt` |

## Formal review note

The supplied custom subagent briefs were read and applied as review lenses throughout this package.
`research/improvement_loop_review.md` preserves the parent-performed planning-stage review as historical context.

The mandatory independent `chaosx_improvement_loop_planner` pass later completed against the implemented Event 018 package.
Its [closure handoff](../../plans/018_resources_found_plans/improvement_loop_closure_handoff.md) closes RF-018-01 through RF-018-08, confirms that RF-018-01 through RF-018-05 were promoted where they changed accepted design, and requires no new depth addendum or further planner run.
The accepted optional exclusions remain outside completion scope and do not block Event 018.

The 363 checked acceptance items describe the implemented design under the documented static proof boundary.
The probability evidence that earlier audits could not obtain from the MCP adapters is a recorded validation limitation under CLAUDE.md section 5, not a design gap; see the evidence gates at the end of `matrices/acceptance_criteria.md`.
The cave-monster 3D package is complete within the user-approved static, no-HOI4 boundary.

## Open questions

Everything in this section is proposed (spec audit 2026-10-10) and unaccepted unless a line says otherwise.
Each item names the existing identifiers it would use; none is implemented.

1. Survey breakthrough options that change nothing.
   Event `chaosx.nr18.3` follows geological appraisal.
   Its option b sets only `resources_found_transport_survey_prioritized`, and option a sets `resources_found_deeper_survey_authorized` beside the stage change; no rule reads either flag, and `resources_found_survey_restrained` from option c is also unread.
   Option b promises corridor preparation in its tooltip, and Part 1 specifies the survey breakthrough as a larger confirmed reserve, a yield gain or a special opportunity, none of which `.3` currently grants.
   Proposal: let option b and the Map the Basin flag `resources_found_corridor_route_mapped` (also unread) shorten the next Extend Corridor project through the existing project duration factors, or remove option b.
2. Medical inspection has no mechanical effect.
   `resources_found_medical_inspection_active` is set by the field hospital and by several Evolution II investigation options, but no trigger, MTTH entry or loss formula reads it.
   Part 2 promises earlier detection and fewer deaths.
   Proposal: apply the existing `resources_found_mtth_factor.inspection` to the Evolution II and III active intervals in `common/mtth/018_resources_found_mtth.txt` when that flag is set (today the factor applies only to `resources_found_commission_active`), and drop the flag otherwise.
3. Repeatable value pumps on the Safety page.
   Shorten Shifts (`resources_found_shorten_shifts_rotate_crews`, Yield minus 10 and Safety plus 15 while Safety is below 60), Reinforce Shafts (Safety plus 20 while below 100) and Recruit Regional Labor (Yield plus 10, Safety minus 5 while Safety is above 40) can be bought repeatedly, and Compensate Families repeats while any casualty is recorded.
   Their flags `resources_found_crew_rotation_active`, `resources_found_shafts_reinforced`, `resources_found_regional_labor_recruited`, `resources_found_compensation_offered` and `resources_found_family_compensation_priority` are never read.
   Proposal: follow Part 2's own staged-institution rule; Reinforce Shafts and the field hospital become one-time stages, crew rotation becomes a standing operating rule that Maximum Shifts clears, and compensation is offered once per new block of `resources_found_field_deaths` above the last compensated total.
   This removes repeated clicks without removing any value or route.
4. Public-breach flight into the Migration system.
   Part 4's Regional flight paragraph has no hook in current source.
   The Migration specification already lists Event 018 cave hazards as an eligible source (`famine_and_migration_system_spec_part_7_cross_system_connections.md`, Other event consequences).
   Proposal: the settlement attack (`.62`), city intrusion (`.64`) and failed evacuation (`.69`) submit flight pressure for the field state through `migration_request_internal_displacement` (inputs `migration_displacement_request_amount`, `migration_displacement_request_proven`, `migration_displacement_request_actor_proven`, `migration_displacement_owner_proven`), scaled from surviving state population after the Event 018 death has been applied.
   Event 018 keeps its own organized evacuation decisions; Migration alone moves people.
5. International price for an exposed cover-up.
   Concealment today changes only local values and loss scaling.
   Proposal: when The Hidden List Reaches Daylight (`.58`) resolves with option c (seize every copy), call `condemnation_add_source` with `condemnation_source.coverup`, `condemnation_context.concealment_operation` and `condemnation_civilian_deaths` from `resources_found_field_deaths`, as Event 029 (`029_riches_found_harm_effects.txt`) and Event 031 already do for their concealment branches.
   Options a and e (admission and compensation) stay free of condemnation.
6. Positive Economy is a one-member cluster.
   Event 018 is the only member row of `constant:event_cluster_id.economy_positive`, so the cluster currently behaves as an alias for Event 018.
   Proposal for the cluster registry owner: evaluate adding economic events such as Event 029 Riches Found as optional members, keeping Event 018 required.
7. Dead tuning table in source.
   `resources_found_project_cost` in `018_resources_found_constants.txt` has no consumer; live costs come from `resources_found_decision_cost` and the cost profiles.
   `resources_found_project_duration` is still read for some projects beside `resources_found_decision_duration`.
   Proposal for the Event 018 code owner: delete the dead cost table and fold the remaining project durations into one duration table.
8. Unimplemented cross-event hooks.
   The Event 8 Tensions Rising and Event 50 Great Embargo interactions in Parts 3 and 7 have no hook in current source and remain unresolved suggestions.
   The Event 13 geological-impact contract in Part 7 was accepted by the parent on 8 October 2026; its implementation seam remains unresolved because no Event 018 disaster listener exists.
9. Documentation and catalog conflicts owned by other surfaces.
   These were found by this audit and left unedited because the owning surface is outside the package.
   `docs/events/018_resources_found/overview.md` states that Event 018 is not assigned to an event cluster, while source and this package register it in Positive Economy.
   `docs/plans/018_resources_found_plans/agent_decisions_2026-10-05.md` says `.90` explains an unsuccessful manual survey preparation, while source uses `chaosx.nr18.33` and `.90` is the quarter-continent milestone.
   The cluster catalog lists Positive Economy at Chaos level 1 with members 18, 34, 55, 57 and 58, while source unlocks the cluster at tier 3 with Event 018 as the only member.
   Proposal for the owners of those surfaces: correct the overview and the decision note, and reconcile the workbook row with the registered cluster.

## Changelog

- 2026-10-10, spec audit.
  - Replaced the dated reconciliation banner with a short status section that points to the current implementation record.
  - Recorded the implemented Positive Economy unlock and member tier (tier 3) next to the cluster assignment.
  - Added the Implemented identity resolution table so the working labels in the parts no longer read as open choices.
  - Marked the six prompts as historical build contracts and repointed live skill links from `.agents/skills/` to the canonical `.claude/skills/` and from `AGENTS.md` to `CLAUDE.md`.
  - Restated the probability-evidence gate as a validation limitation, consistent with CLAUDE.md section 5; no acceptance item changed state.
  - Part 2 now lists the six numeric field values and two records that exist, and states that transport, security, smuggling, contract and closure conditions are discrete states rather than extra meters; the planning list of hidden labor-strain, ownership-share and smuggling meters was never implemented and is no longer requested.
  - Part 2 value tooltips explain the actions that raise or lower each value instead of listing contributor breakdowns.
  - Parts 3 and 7 point the Event 13 hook to the accepted Part 7 contract, record that the border war uses native `start_border_war` because Event 78 has no shared helper, record the implemented Event 26 Black Friday pricing, and mark the Event 8 and Event 50 hooks unresolved.
  - Part 4 links Regional flight to open question 4 and notes the implemented cave-country identity.
  - The tuning framework records the implemented constants beside the planning ranges, including step values that differ (heavy machinery, worker settlement, maximum shifts, hunts) and the absence of a periodic field-value pulse.
  - The acceptance criteria reflect the accepted 2026-10-05 four-slot header.
  - The event chain map, decision matrix, focus architecture and research notes point to the implemented IDs, costing rule, route coverage and cluster tier.
  - No historical date gate exists in Event 018 source, so the 10 October date-gate rule required no change.
  - Added open questions 1 to 9 as proposals; no accepted requirement was removed.
  - Added dated implementation-status notes to Parts 1 to 8 where the implementation resolves or differs from the planning text, including the unresolved Event 8 and Event 50 hooks and the Positive Economy member status.
  - Added an Implemented values section to the tuning framework, an implemented-ids note to the event chain map, and implementation pointers to the decision matrix, focus architecture and catalog reconciliation.
  - Added historical-build-contract banners to the six prompts and repointed their `AGENTS.md` and `.agents/skills/` references to `CLAUDE.md` and `.claude/skills/`.
  - Adopted the same-task audit agent's earlier uncommitted README and Part 2 edits after checking them against current source.
  - Refreshed `manifest.md` hashes and sizes for every changed file.
