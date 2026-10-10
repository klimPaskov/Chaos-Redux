# Event 013 Natural Disasters planning package

Event 013 is implemented in source as the fresh Natural Disasters engine rooted at `chaosx.nr13.1`.
This package holds its accepted source design and the historical material that produced it.
It is not a build queue: do not restart planning or rebuild installed work from it.

## Where to start

- Live behavior, identifiers and file list: [the event overview](../../events/013_natural_disasters/overview.md).
- Current decisions and evidence limits: `docs/plans/013_natural_disasters_plans/agent_decisions_2026-10-05.md`, `2026-10-05_report_news_implementation_handoff.md` and the three `subagent_handoffs/final_*_2026-10-06.md` audits.
- Resume brief for any further work: [the implementation resume prompt](prompts/natural_disasters_implementation_resume_prompt.md).
- File-by-file dispositions: [the disposition map](docs_alignment/013_source_of_truth_and_disposition_map.md).

## Accepted source design

| File | Owns |
| --- | --- |
| `specs/013_natural_disasters_spec_part_1_core.md` | Identity, player loop, sequence model, death and damage intent. |
| `specs/013_natural_disasters_spec_part_2_reusable_system.md` | Season controller, call contract intent, warnings, impact order, chains, and the dated 2026-10-05 report/news and 2026-10-06 recovery-bill acceptances. |
| `specs/013_natural_disasters_spec_part_3_disaster_family_playbooks.md` | Compact catalogue of the 25 families. |
| `specs/013_natural_disasters_spec_part_4_aftermath_decisions_ui.md` | Aftermath category purpose, mission intent, partial success, relief and refugee intent. |
| `specs/013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md` | Evolutions, cluster role, Disaster Barrage, related events 043/046/051/099/120. |
| `specs/013_natural_disasters_spec_part_6_presentation_assets_super_events.md` | Presentation, asset families, super-event roles. |
| `specs/013_natural_disasters_spec_part_7_ai_balance_acceptance.md` | AI, balance, exploit checks, acceptance criteria. |
| `specs/013_natural_disasters_spec_part_8_deep_family_minispecs.md` | Per-family warnings, card fields, AI, report/news, modifiers, chains. |
| `specs/013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md` | Evolution III abnormal path map. |
| `specs/013_natural_disasters_spec_part_10_recovery_decision_mission_map.md` | Staged recovery, chain prevention, relief variants, caps, cleanup. |
| `matrices/013_disaster_call_contract.md` | Public call fields and outputs. |

Precedence: the dated acceptance sections in Part 2 supersede older report, news and fee prose in every part.
Part 8 is the stronger source where it and Part 3 describe the same family.
Numeric tuning lives in `common/script_constants/013_natural_disasters_constants.txt`; spec numbers are design anchors and the constants file wins on any disagreement.

## Shared-system connections in source

These hooks exist in the current source and are the only cross-system links this package treats as implemented.

| System | Identifier and owner | What it does |
| --- | --- | --- |
| Deaths and Chaos Meter | `natural_disaster_apply_population_loss` calls `chaos_meter_register_state_civilian_deaths_percent` with `constant:chaos_meter_deaths_reason.natural_disaster`. | Removes state population and records the loss under the natural-disaster cause. |
| Famine | The same effect calls `famine_adapt_natural_disaster_state` (`common/scripted_effects/famine_adapter_effects.txt`). | Every impact or chain with positive deaths submits food pressure equal to `natural_disaster_last_deaths`, keyed to the sequence id, and opens the 60-day disaster food context. |
| Air Cleanliness | `air_contamination_register_natural_disaster_source` and `air_contamination_register_natural_disaster_aftermath_source`, documented in `docs/systems/air_cleanliness/natural_sources.md`. | Regional wildfires and volcanic families add a small, sequence-keyed smoke and ash contribution. |
| Event 014 Cannibalism | `cannibalism_state_has_famine_pressure`, `cannibalism_state_has_disease_pressure` and `cannibalism_state_has_disaster_supply_pressure` read the Event 013 chain flags. | Famine and disease chains, supply collapse, open aftermath, unresolved territory and refugee chains feed Cannibalism state pressure; the 8 October review records the relief-phase boundary. `cannibalism_state_has_locust_pressure` also reads `natural_disaster_locust_pressure`, which nothing sets because Event 013 has no locust family; that dead check belongs to the Event 014 owner. |
| Event 020 Black Plague | `black_plague_state_has_refugee_pressure` reads `natural_disaster_refugee_pressure`. | Disaster refugee chains raise plague exposure. |
| Event 012 Gods of Africa | `natural_disaster_offer_neighbor_relief_for_gods_of_africa` and `natural_disaster_record_event012_civilian_weaponisation`. | Neighbor-relief bridge and the civilian-weaponisation record for hostile divine calls. |
| Event 026 Black Friday | `global.black_friday_price_natural_disaster_*` price table. | Sale prices for every material fee. |
| Migration | None. `migration_request_disaster_pressure` exists in `common/scripted_effects/migration_core_effects.txt` but has no caller. | Event 013 refugee chains stay internal (see Open questions). |

## Historical material

Everything outside the table above is historical intake, research or build-contract material.
The `implementation_readiness/` gates, the remaining `prompts/` files, the `research/` logs and `matrices/013_implementation_readiness_ledger.md` record how the original build was planned and checked.
They are kept for traceability and must not be read as open tasks.
`research/` logs are unchanged provenance and still describe the original planning environment, which had no live checkout, wiki, vanilla files or subagents.
Current routing lives in [the subagent routing skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Open questions

Each item below is proposed (spec audit 2026-10-10).
None is accepted, and each conflicts with or extends parent-accepted implemented design, so it needs an owner decision before implementation.

1. **Aftermath card value budget.**
   The implemented card description (`natural_disaster_aftermath_card_desc`) prints about seventeen values on thirteen lines: family, severity, hazard group, affected and linked state, cumulative deaths, casualty driver, damage, active modifier with three percentages, warning result, recovery need, follow-up, foreign relief, card state, phase and timing.
   This is the value-dump pattern the 10 October brief rejects.
   Proposal: keep four lines that drive a decision, namely what hit where (family, severity, state), known deaths, what is broken now (damage plus the one worst disruption), and the next action with its deadline or the pending follow-up with its date.
   Show foreign relief only while a relief status other than none is active, and drop the hazard group, casualty driver and warning result from the card while keeping them in the abnormal-history record.
   Apply the same budget to the eleven-line selected-record summary of the abnormal map.
   Owner: Event 013 localisation and Part 8's shared card contract; no gameplay value changes.
2. **One famine owner per hunger death.**
   A famine, disease or refugee chain runs `natural_disaster_apply_population_loss`, so Event 013 kills the population as natural-disaster deaths and then submits those deaths as fresh food pressure through `famine_adapt_natural_disaster_state`, which the Famine system can turn into further hunger deaths.
   The direct impact also submits food pressure for every family, including meteor, hail and tornado impacts, scaled only by deaths.
   Proposal: Event 013 keeps direct impact deaths; the famine chain stops applying its own population loss and instead submits its food receipt, letting Famine own the resulting hunger; the direct-impact receipt is limited to food-relevant families (drought, flood, hailstorm, ashfall, massive eruption, blizzard, cold wave, storm surge, dust and sandstorm) or weighted by damaged agriculture and transport rather than deaths.
   Owners: Event 013 (`natural_disaster_execute_chain_followup`, `natural_disaster_apply_population_loss`) and the Famine system (`famine_adapt_natural_disaster_state`, famine spec Part 7 "Exact hazard aftermath").
3. **Food-corridor success opens relief access.**
   Full success of `natural_disaster_chain_prevent_famine_mission` or `natural_disaster_stabilize_secure_food`, and arrival of foreign relief at a card with famine risk, currently changes only Event 013 state.
   Proposal: call the existing `famine_mark_relief_access` on that state so Famine's faster decay and relief component reflect the delivered corridor, once per card.
   Owners: Event 013 mission outcomes and the Famine core (`famine_mark_relief_access`).
4. **Refugee chains become Migration flows.**
   The refugee chain sets `natural_disaster_refugee_pressure` and kills population locally, but never reaches Migration, so no one actually moves.
   Proposal: when a refugee chain or a warning evacuation (for example `natural_disaster_warn_tsunami_inland_corridors`) resolves, submit the surviving displaced amount through `migration_request_disaster_pressure` (or `migration_request_evacuation_pressure` for ordered evacuations) with the sequence id as generation, and keep only the deaths Event 013 actually caused.
   The Event 020 and Event 014 flag readers stay unchanged.
   Owners: Event 013 chain execution and the Migration core (`migration_apply_flight_request`); the famine spec Part 7 already names Event 013 evacuation as a valid source.
5. **Event 018 field reaction.**
   The 8 October review accepted that measured Event 013 damage can affect Event 018 fields, but no Event 018 disaster listener exists in source; this stays unresolved with the implementation seam named in `docs/plans/repo_cleanup/specification_improvements_2026-10-08/handoffs/013_018.md`.

## Changelog

- 2026-10-10, spec audit.
  - Rewrote this README as the single entry point: implementation status, source precedence, verified shared-system hooks, historical material and open questions.
  - Replaced the `.agents/skills/` routing link with the canonical `.claude/skills/` path.
  - Merged the coding, goal, subagent-routing and implementation-resume prompts, the closure resume packet, the final next-agent prompt, the dependency-order plan and the simplification blocklist into one resume brief; the merged files were deleted because their rules repeat the disposition map, Part 7 and CLAUDE.md (git history keeps them).
  - Marked the remaining build prompts, readiness gates and the super-event research matrix as historical build contracts, corrected the absent `docs/assets/013_natural_disasters/` claim, and moved the asset reference paths to `.claude/skills/`.
  - Condensed the disposition map to its current source set, historical-file dispositions and negative boundaries; the pre-implementation read order and completion stance were dropped because the build they ordered is finished.
  - Aligned Parts 1 to 10, the call contract, the controller diagram and the catalog alignment with the accepted one-report-per-recipient rule, the accepted recovery bill, the implemented family pools, decision identifiers and achievement ids, the `natural_disaster_sequence` constants, and the current cluster membership (five Event 013 slots plus optional Events 033 and 051).
  - Renamed fourteen Part 8 working warning keys so all 75 map to live decisions by prefix alone.
  - Added proposals 1 to 4 for the card value budget, famine ownership, relief access and Migration flows, and recorded the Event 018 seam as unresolved.
