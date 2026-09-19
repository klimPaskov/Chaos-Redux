# Event 021 Random Civil War Specification Package

This folder is the source specification package for Chaos Redux event ID `21`, working slug `random_civil_war`.

The package defines a reusable internal-war framework that can create country-specific political uprisings, rival legal governments, regional secessions, command schisms, complete Event 006 independence actors, multi-front wars, neighboring political exposure, successor crises, and a manual global fracture scenario.

## Package identity

- Event ID: `21`
- Working event name: `Random Civil War`
- Canonical entry: `chaosx.nr21.1`
- Type: `Minor Repeatable`
- Event chaos level: `1`, Calm World
- Cluster: `1`, Wars
- Member severity: `Medium`
- Catalog status is `Needs Testing`. The rework implementation phase is complete for test entry, the runtime test-release gate is open, and final acceptance certification remains incomplete.

All event, evolution, scenario, decision, mission, achievement, idea, and UI names in this package are working labels unless a file states otherwise. Final player-facing wording belongs to implementation.

## Reading order

1. `021_random_civil_war_spec_part_1_core.md`
2. `021_random_civil_war_spec_part_2_targeting_and_baseline.md`
3. `021_random_civil_war_spec_part_3_decisions_missions_and_outcomes.md`
4. `021_random_civil_war_spec_part_4_evolution_i.md`
5. `021_random_civil_war_spec_part_5_evolution_ii.md`
6. `021_random_civil_war_spec_part_6_evolution_iii.md`
7. `021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md`
8. `021_random_civil_war_spec_part_8_cluster_scenario_ai_balance.md`
9. `021_random_civil_war_spec_part_9_presentation_assets_achievements.md`
10. `021_random_civil_war_spec_part_10_acceptance_and_implementation_handoff.md`

Supporting files include the country-package matrix, probability scenario matrix, event overlap reconciliation, research notes, source-read ledger, revision notes, prompts, and context-complete subagent prompts.

## Core design decision

Event 021 owns generic domestic fracture. It does not replace specialized Chaos Redux events that already own occupation revolts, named five-way wars, warlord events, mutinies, partisan formations, Soviet collapse, or global subject liberation.

Ordinary ideological and legal claimants preserve the parent country's existing national content. Their temporary civil-war play comes from Event 021 decisions, missions, staged crisis ideas, AI, and settlement outcomes.

An independence side uses a complete Event 006 country package. Event 021 may initialize that package even when Independence Wave has never fired. It reuses Event 006 identity, leaders, flags, focus tree, formation decisions, forces, reinforcement, AI, formables, and assets. It records a separate Event 021 origin and never consumes Event 006 event state.

## Presentation decision

The normal presentation is a standard decision category with a static category picture, concise dynamic text, phased decisions, and up to three active missions. The framework does not require a dedicated scripted GUI, animated seal, animated portrait, super-event, or custom 3D asset.

The one main visible crisis value is `State Authority`. Hidden `Fracture Pressure` drives selection and severity. This separation keeps the player-facing surface readable while preserving deep dynamic logic.

## Implementation boundary

The implementation and current evidence are recorded in `docs/events/021_random_civil_war/` and `docs/plans/021_random_civil_war_plans/`. This package remains the design source and does not itself constitute an acceptance certificate.

The catalog is intentionally marked `Needs Testing`, and the test-release runtime surfaces are enabled by `random_civil_war_rework_ready`. The player owns live consumer validation; the repository evidence records source, static, MCP, probability, and asset limits separately. This test release is not an unconditional completion certificate.

The offline Paradox wiki snapshot, installed vanilla documentation, vanilla game files, Workshop references, HOI4 MCP, and project subagent evidence used for the implementation are recorded in the source-read ledger and current handoffs.

The 2026-09-19 source tranche also closes the bounded Critical-launch convergence repair, the frozen secondary-state persistence defect, and the two same-tag scenario compatibility gaps for test entry. Those repairs do not change the catalog status: Event 021 and SCN-018 remain `Needs Testing` pending user-owned gameplay and the remaining certification gates.
