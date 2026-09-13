# Event 58 completion-audit prompt

Use the project custom subagent `chaosx_event_completion_auditor` in read-only mode with no inherited context.

## Task

Audit the completed implementation of Event 58, Random Buildings, against every accepted requirement in:

- `docs/specs/058_random_buildings_specs/README.md`
- `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_1_core.md`
- `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_2_state_layers.md`
- `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_3_provincial_exceptional.md`
- `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_4_integration_presentation_balance.md`
- `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_5_achievements.md`
- `docs/specs/058_random_buildings_specs/quality/058_random_buildings_probability_scenarios.md`
- `docs/specs/058_random_buildings_specs/quality/058_random_buildings_acceptance_matrix.md`
- every accepted Event 58 plan or subagent handoff under `docs/plans/058_random_buildings_plans/`

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, and `chaos-redux-event-assets` before auditing.

## Required inspection

Inspect all Event 58 gameplay, localisation, scripted localisation, event-log, Event Details, evolution, cluster, Chaos, achievement, asset, documentation, and workbook surfaces.

Use the HOI4 MCP event tools to inspect and render the final event chain. Review the Event 58 probability auditor's baseline and post-change evidence. Review map evidence for land forts, coastal forts, naval bases, railways, supply hubs, dams, facilities, landmarks, and every exceptional provider that reached implemented status.

Confirm that the provider registry is owner-extensible and fail-closed. Verify that malformed providers cannot enter selection. Confirm that provider-owned special structures retain their normal mechanics, lifecycle, responsibility, evidence, and cleanup. Confirm that Event 58 does not duplicate or partially initialize an owner system.

## Audit questions

Determine whether the implementation actually delivers:

1. one independent baseline state-building roll in every eligible world state
2. additive Evolution I state construction at `200+`
3. additive Evolution II province packages at `400+`
4. a limited Evolution III exceptional wave at `600+`
5. safe capacity, geography, DLC, technology, uniqueness, and owner-system validation
6. risk-band protection that prevents rare structures from becoming common through candidate exhaustion
7. exact province-package placement with no arbitrary province selection
8. one bounded global transaction with no recurring whole-world scan
9. compact reporting without per-state popup spam or unbounded persistent history
10. correct repeatable weight, cap, recovery, timer, event-log, and cluster behavior
11. correct evolution enablement, first-use logging, and additive stacking
12. bounded Event 58 Chaos registration without generic-source duplication
13. multiplayer-safe human reporting
14. complete report-image and achievement assets with final consumers
15. final player-facing localisation without implementation notes or exposed probabilities
16. Event 58 documentation and authoritative workbook alignment
17. removal of the stale `The Industrial Complex` identity from ID 58 wherever Event 58 should appear
18. the absence of any unapproved fallback, placeholder, hidden simplification, or weaker substitute

## Required output

Write the report to:

`docs/plans/058_random_buildings_plans/058_random_buildings_completion_audit.md`

Use clear statuses for every accepted requirement: `pass`, `partial`, `missing`, `blocked`, or `not applicable`.

List exact files, identifiers, and evidence for every finding. Separate source inspection, MCP evidence, probability evidence, asset evidence, and documentation evidence. Identify every unresolved accepted plan or handoff.

Do not patch files. Do not propose broad new design unless an implementation gap proves that the accepted spec cannot work. Report every simplification and blocker directly. Event 58 cannot be marked complete while any required layer, provider contract, owner callback, report surface, achievement, asset, probability comparison, map proof, documentation update, or workbook update remains unresolved.
