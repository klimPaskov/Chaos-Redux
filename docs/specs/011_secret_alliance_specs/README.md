# Event 011 Secret Alliance Specs

Status: source specification package for a future implementation pass.

Working labels, titles, decision names, achievement names, and super-event directions in this package are planning handles only. They are not final localisation and should not be pasted into player-facing files without a normal implementation writing pass.

## Catalog

- Event ID: `11`
- Event name: Secret Alliance
- Entry event root: `chaosx.nr11.1`
- Type: Minor Fire-Once
- Current implementation status: not implemented; existing repo references still identify Event 011 as unavailable
- Core promise: three hidden countries form an Anti-[player country] Pact, recruit others, sabotage and isolate the player, then reveal as a faction and war coalition if any pact member enters war with the player

## Package Map

- `specs/011_secret_alliance_spec_part_1_core_pact.md`: core identity, setup, roster, hidden values, member roles, baseline reports, reveal rule, and integration promise
- `specs/011_secret_alliance_spec_part_2_evolutions.md`: baseline progression, Evolution I, Evolution II, Evolution III, pre-fire evolved openings, public bloc state, and collapse handling
- `specs/011_secret_alliance_spec_part_3_decisions_sabotage.md`: player decision category, targeted decisions, missions, sabotage packets, border wars, cleanup, and UI direction
- `specs/011_secret_alliance_spec_part_4_ai_balance_assets_acceptance.md`: AI behavior, balance, exploit guards, assets, animation, super-event direction, achievements, localisation direction, and completion criteria
- `matrices/011_secret_alliance_scripted_system_architecture.md`: planned script files, state model, helper map, constants, MTTH entries, on-action strategy, and reveal architecture
- `matrices/011_secret_alliance_decision_map.md`: compact decision and mission matrix
- `matrices/011_secret_alliance_implementation_handoff.md`: implementation order, file touchpoints, validation expectations, and unresolved technical gates
- `research/011_secret_alliance_research_notes.md`: historical inspiration anchors and super-event quote research summary
- `research/011_secret_alliance_source_review_manifest.md`: wiki, vanilla, repo, skill, and subagent references consulted for this package
- `prompts/011_secret_alliance_coding_prompt.md`: follow-up coding prompt for implementation
- `prompts/011_secret_alliance_asset_prompt.md`: follow-up asset production prompt
- `prompts/011_secret_alliance_super_event_prompt.md`: follow-up super-event research and wiring prompt
- `prompts/011_secret_alliance_decision_mission_prompt.md`: follow-up decisions and missions prompt
- `prompts/011_secret_alliance_achievement_prompt.md`: follow-up achievement implementation prompt

## Accepted Working Plans

The following planning handoffs were accepted into the source spec:

- `docs/plans/011_secret_alliance_plans/011_secret_alliance_improvement_addendum.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_scripted_system_architecture.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_decision_mission_handoff.md`
- `docs/plans/011_secret_alliance_plans/011_secret_alliance_super_event_text_research.md`

If a later implementation disagrees with one of those plan files, update this source package first or record a rejected-plan note under `docs/plans/011_secret_alliance_plans/`.

## Scope Locks

The requested event scope does not include a world-end branch, manual triggerable scenario, cluster membership, focus tree, country package, formable, or broad supernatural threat framework. The event should stay a dangerous anti-player diplomatic and military conspiracy with a reveal super-event.

## Completion Standard For Future Implementation

A future implementation is not complete unless it wires the Event 011 entry event, random-event registration, hidden roster state, evolutions, decisions, on-actions, faction reveal, super-event, event logs, event details, localisation, icons, docs, and any spreadsheet/event catalog alignment together in the same implementation plan.

No fallback or simplification is approved in this spec. If dynamic faction naming, war joining, or candidate selection cannot be implemented exactly enough, the implementation pass must stop and request design approval rather than silently replacing the mechanic with a weaker static substitute.

