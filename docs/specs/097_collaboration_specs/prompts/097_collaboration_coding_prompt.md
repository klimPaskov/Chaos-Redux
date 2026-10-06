# Event 097 Collaboration: Coding-Agent Prompt

Implement Chaos Redux Event 097 Collaboration from the specification package in `docs/specs/097_collaboration_specs/`. Keep the existing namespace and the entry event `chaosx.nr97.1`. Replace the current stub in `events/097_collaboration.txt` and its localisation completely.

The event's identity comes from the user brief and must survive every implementation choice: every country gains collaboration against every other country, global and symmetrical, through the native collaboration mechanic. There is no Collaboration currency, no new meter, and no large management system. The normal collaboration mechanic is the event.

## Read first

Specification:

- `specs/097_collaboration_spec_part_1_core.md`: participants, layers, stances, opening report, application pass, hidden records, public readings, Event Details, cleanup
- `specs/097_collaboration_spec_part_2_evolutions.md`: the four evolutions, pacing, entry paths, disabled behavior
- `specs/097_collaboration_spec_part_3_occupation_capitulation_and_governments.md`: bands, prepared cadres, seats, Fifth Column, Open Gates, prepared governments, Installed Administration, Turned Regime, competing orders
- `specs/097_collaboration_spec_part_4_decisions_and_responses.md`: Divided Loyalties, Prepared Governments, Collaborators Unmasked
- `specs/097_collaboration_spec_part_5_connections_and_cluster.md`: public contract, Events 095, 052, 039, 063, Tordesillas, Intelligence cluster, Fallout
- `specs/097_collaboration_spec_part_6_ai_presentation_achievements.md`: AI, presentation, super-event, achievements, DLC, balance review
- `matrices/097_collaboration_chaos_impact_map.md`, `matrices/097_collaboration_ai_probability_scenarios.md`, `matrices/097_collaboration_edge_case_matrix.md`
- `research/097_collaboration_research_notes.md`: engine facts, uncertainties, history anchors, sensitivity boundary
- `handoffs/097_collaboration_localisation_direction.md`, `handoffs/097_collaboration_catalog_alignment.md`
- `quality/097_collaboration_acceptance_criteria.md`
- prompts in this folder: asset, super-event, achievement, decision and mission, goal

Working material in `docs/plans/097_collaboration_plans/`:

- `subagent_handoffs/097_repo_explorer_handoff.md`: every shared touchpoint with file and line evidence
- `097_collaboration_scripted_architecture_plan.md`: helper, hook, and constant architecture
- the decision and AI probability review handoffs in `subagent_handoffs/`
- `097_collaboration_plan_dispositions.md`: which plan content is accepted, queued, or unresolved

Rules and skills: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-mtth`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`. Open the required offline wiki pages in `paradox_wiki/` and the installed vanilla documentation before editing.

## Step 1: settle the engine facts and user decisions

The planning pass had no vanilla files, no vanilla documentation, and no HOI4 MCP connection. Before writing gameplay code, establish these facts from vanilla documentation, vanilla script, and MCP where available, and record each result in `docs/events/097_collaboration/`:

1. Whether `add_collaboration` accepts a negative value, and what happens below zero. A2 and the Purge option depend on it.
2. Where the native collaboration value can be read: `has_collaboration` and `core_compliance` in occupation contexts, and whether a host-owned non-core state reads anything.
3. Whether the collaboration surrender and compliance defines apply without La Résistance.
4. Whether the scripted collaboration-government creation effect honors `can_create_collaboration_government` and `can_collaborate`, which tag pool it uses, and how it names leaders.
5. Whether the puppet on-action fires for that creation effect.
6. Whether a state can change controller without changing owner by script, and whether a reliable trigger exists for friendly divisions present in a state. Open Gates depends on both.
7. Whether a subject's overlord can be changed during a war cleanly. Turned Regime depends on it.

Then bring these decisions to the user and implement only what the user chooses:

- the democratic and non-aligned installer route in Part 3, if fact 4 shows the ideology rule blocks it
- whether Evolution clocks may use the shared daily host pulse, if the architecture plan recommends it
- the war-weighted selection factor, recorded as an unresolved proposal in the package README

An engine fact that blocks a mapped feature is a blocker to report. Do not replace the feature with a substitute without user approval.

## Step 2: implement

Follow the architecture plan for file layout, helper names, and hooks, and keep every name readable and free of unnecessary prefixes.

- Constants: one Event 097 script-constant family for identity, evolution ids, layer sizes, stance multipliers, bands, thresholds, durations, caps, costs, MTTH anchors, AI anchors, and Chaos amounts. No magic numbers.
- Participants: one trigger built on the shared special-country and nonhuman classifiers.
- Opening transaction, response window, batched application pass, deepening tranche, and Fallout stand-down. The pass schedules itself and adds no periodic world hook. Pair work uses scope iterators, never counted loops.
- Registration: switch the raw registration entry to the constant, add the unavailability reasons, add the Event Details premise and current-state line, add the evolution previews and all eight evolution selectors, and add Event 097 to the reworked default-enable list in the same change that completes this wiring.
- Evolutions: MTTH pacing, one log entry each with no actor, disabled-evolution safety, active-event entries, and pre-fire openings.
- Occupation and capitulation hooks: seats, Open Ministries, prepared cadres, Fifth Column evaluation, Open Gates, capitulation offer, and registry updates. Every hook is event-driven and checks participant status, Event 097 depth, core status, and the Fallout gates.
- Installation helper shared by the capitulation offer and the Seat decision, with registry, Installed Administration lifecycle, auxiliaries, Chaos, and the competing-orders check.
- Decisions and Collaborators Unmasked through `097_collaboration_decision_mission_prompt.md`.
- The public contract from Part 5 with caller proof checks, documented in the paired reference documents.
- The complete Chaos impact map, with every row, repeat guard, reversal, history reason, and the generic-source overlap checks.
- The public value budget: the two qualitative readings and, while active, the Fifth Column band. Every other value stays hidden.
- AI from Part 6 and the probability matrix. Run `chaosx_ai_probability_auditor` for a baseline before setting weights and a `hoi4.probability_compare` pass afterward with the same named scenarios.
- Assets through `097_collaboration_asset_prompt.md`, super-event through `097_collaboration_super_event_prompt.md`, achievements through `097_collaboration_achievement_prompt.md`.
- Final localisation written from the localisation direction. No working label becomes final text, and no unresearched super-event text ships.
- A package-owned CXT test fixture under the dynamic extension contract in `docs/testing/chaosx_test_country.md`: a modifier-free hidden-idea carrier, an idempotent `_apply` setup effect that prepares Event 097 records for inspection without firing the event or adding collaboration, a startup registration, and a registration-only `on_daily_CXT` fallback.
- Intelligence cluster integration per Part 5, building the cluster if it does not exist yet, or reporting it as an open item.

Do not add `on_daily`, `on_weekly`, or `on_monthly` world iteration without explicit user permission.

## Step 3: document and align

- `docs/events/097_collaboration/overview.md` with mechanics, records, hooks, icons and sprite wiring, engine findings, and future plans, plus a row in `docs/events/README.md`.
- `common/scripted_effects/chaosx_dynamic_effects.md` for any new reusable dynamic helper.
- Catalog and cluster rows through `chaosx_spreadsheet_doc_worker`, then the export tool.

## Step 4: audit and finish

Spawn with self-contained prompts: `chaosx_decision_mission_auditor`, `chaosx_ai_probability_auditor`, `chaosx_localisation_auditor`, and `chaosx_event_completion_auditor`. Resolve their findings. Before claiming the goal is near complete, spawn `chaosx_improvement_loop_planner` and resolve its addendum or record its closure.

Record the balance scenarios from Part 6 with results. Do not use fallbacks, simplifications, temporary versions, or approximations. Report every blocker and every deviation under a clear heading. Keep iterating until the implemented files satisfy the specification, and do not claim completion before that.
