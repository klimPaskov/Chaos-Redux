# Event 32: Missiles specification package

## Intended repository location

Extract this package so that the top-level folder becomes:

`docs/specs/032_missiles_specs/`

## Design status

This package defines the accepted design target for reworking Event 32, Missiles.

Event 32 remains a Minor Repeatable global event with no cluster assignment. Its baseline gives every valid existing country one missile technology step, an operational missile reserve, and a usable launch site. Repeat firings deepen national programs without placing a new site on every firing. Five parallel evolution tracks create saturation arsenals, unreliable guidance, special warheads, rogue launch commands, and automatic retaliation.

The design replaces the current legacy implementation, which grants two early rocket technologies and two rocket-site levels to every country in one global loop.

## Package map

| File | Purpose |
| --- | --- |
| `032_missiles_source_review.md` | Source inventory, current repository findings, subagent-role review, and tooling limitations |
| `032_missiles_research_notes.md` | Historical and technical design references for hardened sites, command control, survivability, and false warning risks |
| `032_missiles_spec_part_1_core.md` | Event identity, recipient rules, firing flow, progression, reports, and logging |
| `032_missiles_spec_part_2_program_and_launch_sites.md` | Missile program values, technology progression, site selection, capacity, capture, and succession |
| `032_missiles_spec_part_3_operations_and_consequences.md` | Strike preparation, targeting, damage, failures, payloads, shared consequences, and incident records |
| `032_missiles_spec_part_4_evolutions.md` | Full specifications for all five evolution tracks |
| `032_missiles_spec_part_5_decisions_missions_and_scenario.md` | Decision category, action families, timed missions, emergency responses, and SCN-015 |
| `032_missiles_spec_part_6_ai_and_probability.md` | AI doctrine profiles, target logic, maintenance behavior, and probability requirements |
| `032_missiles_probability_scenario_matrix.md` | Named audit scenarios for every weighted Event 32 surface |
| `032_missiles_spec_part_7_assets_text_and_achievements.md` | Visual inventory, player-facing writing direction, and achievement architecture |
| `032_missiles_system_connections.md` | Required bridges to existing Chaos Redux events and shared systems |
| `032_missiles_requirement_traceability.md` | Mapping from every supplied baseline and evolution requirement to its source-of-truth section |
| `032_missiles_spec_part_8_implementation_contract.md` | File ownership, reusable APIs, tuning, performance, lifecycle, and migration rules |
| `032_missiles_acceptance_criteria.md` | Pass or fail criteria for implementation completion |
| `032_missiles_test_matrix.md` | Static and later live test scenarios |
| `032_missiles_asset_prompt.md` | Bounded asset-production prompt |
| `032_missiles_achievement_prompt.md` | Achievement implementation and icon prompt |
| `032_missiles_decision_mission_prompt.md` | Decision and mission implementation prompt |
| `032_missiles_coding_prompt.md` | Full coding-agent implementation prompt |
| `032_missiles_goal_prompt.md` | Compact goal prompt for the implementation run |
| `032_missiles_improvement_loop_closure.md` | Near-completion depth review and anti-bloat closure |
| `032_missiles_package_manifest.md` | Package inventory, validation summary, source disclosure, and SHA-256 hashes |

## Central design decisions

1. Event 32 fires once at the global pacing level and dispatches one bounded setup transaction to each valid recipient.
2. The country program exposes three player-facing values: operational reserve, launch readiness, and command control.
3. Guidance risk, site capacity, attribution confidence, and retaliation posture remain visible as compact states or tooltips instead of additional permanent meters.
4. A normal decision category with a static category picture is sufficient. A dedicated scripted GUI is not required.
5. Existing rocket-site and missile visual surfaces should be reused where they fit. Event 32 does not require a custom unit, new country, portrait, flag, focus tree, or 3D model.
6. Conventional strikes use a normalized Event 32 strike contract. Chemical, biological, nuclear, and thermonuclear payloads call the existing shared consequence systems and consume the relevant stockpile.
7. Event 32 does not own a terminal campaign branch. A severe special-warhead exchange may satisfy the separate Fallout consequence conditions through the existing Air Cleanliness and CBRN systems.
8. Automatic retaliation uses a bounded incident queue with causal depth and participant caps. It cannot create an unbounded launch loop.
9. Manual testing and sandbox play use the next collision-free public scenario identity, planned as `SCN-015` after the current raw Fallout reservation at ID 14. Implementation must repeat the registry audit before locking the ID.
10. All tuning anchors belong in script constants or an event-owned tuning file. The implementation must not scatter literal values across events, decisions, effects, triggers, and localisation.

## Completion interpretation

These files are specifications and implementation prompts. They do not claim that Event 32 has been implemented, asset-complete, probability-audited, or tested in game.
