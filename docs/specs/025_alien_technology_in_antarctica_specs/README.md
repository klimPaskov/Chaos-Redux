# Event 025 Alien Technology in Antarctica planning package

This package expands Event ID `25`, Alien Technology in Antarctica, into a complete source specification for Chaos Redux.

A damaged craft falls somewhere on the Antarctic continent. Its descent is detected through scattered radio reports, unusual weather observations, interrupted magnetic instruments, and a brief light seen over the ice. Major powers and every human-controlled country can enter a bounded expedition race. Participants must build a viable route south, establish an outpost, narrow the search area, protect personnel and supplies, contest rival expeditions, and complete a final recovery operation. The ordinary race can be won without any evolution.

The winner receives one random advanced technology from the existing Event 016 custom operational technology system. Player-facing text treats the discovery as alien-derived knowledge and never identifies it as Kruger technology. Event 016 remains the owner of the technology runtime package. Event 025 owns expedition state, recovery proof, winner selection, fragment rewards, and the shared alien-recovery ledger used to prevent duplicate rewards with Event 036 Alien Spacecraft.

## Accepted design summary

| Field | Accepted design |
| --- | --- |
| Event ID | `25` |
| Display name | Alien Technology in Antarctica |
| Type | Major |
| Minimum chaos level | Calm World, tier 1 |
| Runtime cluster | None |
| Major presentation | One opening super-event |
| Core mechanic | International expedition race with an event-owned scripted GUI |
| Human eligibility | Every valid human-controlled country may enter, including special actors when the player controls them |
| AI eligibility | Selected valid AI major countries, plus a narrow Kruger State exception |
| Baseline completion | Secure the primary recovery core before rivals |
| Primary reward | One random unresearched Event 016 custom operational technology |
| Losing reward | Fragment rewards scaled by verified progress and recovered material |
| Evolutions | Five, mapped to Gathering Storm through World Collapse |
| New countries | None |
| Focus trees | None |
| New combat units | None |
| New character portraits | None |
| Required 3D models | None |
| Event 036 relationship | Shared reward arbitration and upgraded result when alien-aircraft content overlaps |

## Package map

| Path | Purpose |
| --- | --- |
| `specs/001_event_identity_and_player_experience.md` | Event identity, firing, eligibility, pacing, and campaign role |
| `specs/002_expedition_race_system.md` | Participant ledgers, visible values, route burden, progress, hazards, and pulse model |
| `specs/003_baseline_phase_map.md` | Complete baseline progression from detection to recovery and aftermath |
| `specs/004_evolutions.md` | Five evolution tracks, active-chain entry, evolved openings, and enable behavior |
| `specs/005_decisions_missions_and_costs.md` | Player actions, mission families, cost rules, clutter control, and cleanup |
| `specs/006_outcomes_rewards_and_aftermath.md` | Winner proof, fragment rewards, technology grants, Event 036 arbitration, and Evolution V aftermath |
| `specs/007_world_reactions_and_event_connections.md` | Diplomacy, incidents, shared systems, and cross-event integration |
| `specs/008_scripted_gui_and_presentation.md` | Expedition Board layout, states, values, click behavior, and accessibility |
| `specs/009_ai_strategy_and_probability.md` | Participant selection, phase behavior, rival targeting, and named audit scenarios |
| `specs/010_assets_animation_and_super_event.md` | Full asset inventory, frame animation direction, and super-event research brief |
| `specs/011_achievements.md` | Achievement set, tracking, disqualifiers, icons, and testing |
| `specs/012_localisation_and_narrative_direction.md` | Player-facing writing direction across every visible surface |
| `specs/013_implementation_architecture.md` | File map, helper contracts, arrays, events, constants, logs, and cleanup |
| `specs/014_acceptance_criteria.md` | Implementation, balance, asset, AI, documentation, and audit completion gates |
| `matrices/025_event_chain_map.md` | State and phase flow |
| `matrices/025_participant_and_route_matrix.md` | Eligibility, gateways, route bands, and special cases |
| `matrices/025_phase_action_matrix.md` | Action availability and consequences by phase |
| `matrices/025_evolution_entry_matrix.md` | Evolution entry during active and pre-fire states |
| `matrices/025_reward_arbitration_matrix.md` | Event 016 and Event 036 reward resolution |
| `matrices/025_ai_probability_scenarios.md` | Named probability and timing audit cases |
| `matrices/025_asset_inventory.md` | Requirement-to-runtime asset coverage |
| `matrices/025_requirement_coverage.md` | User request to specification crosswalk |
| `research/025_historical_scientific_research.md` | Source-grounded Antarctic design anchors |
| `research/025_source_reading_ledger.md` | Uploaded-source and subagent-file reading record with hashes |
| `research/025_catalog_and_cross_event_audit.md` | Catalog findings and Event 016, 025, 036 boundaries |
| `research/025_improvement_loop_closure.md` | Parent anti-bloat review and remaining independent planner gate |
| `prompts/` | Context-complete prompts for implementation and relevant project subagents |
| `handoffs/025_process_limitations.md` | Tooling limits, unavailable evidence routes, and exact continuation actions |

## Non-negotiable event rules

1. The baseline race must remain fully completable with all five evolutions disabled.
2. Evolutions may change hazards, actions, and aftermath. They may not replace the normal expedition phases.
3. The opening event must not reveal the exact nature of the craft, survivor, or technology.
4. The winner receives an Event 016 technology through the neutral external-grant contract. Event 025 must not create Kruger ownership, Directorate state, Event 016 project history, free units, or Event 016 evolution progress.
5. Player-facing text must describe alien-derived research and recovered systems. It must never say that the technology originated from Kruger.
6. Event 036 must not give an identical alien-aircraft reward after Event 025 without converting the later reward into a higher tier or another valid result.
7. All human-controlled countries may enter. Distance and access affect cost and timing, not basic human eligibility.
8. The runtime must evaluate only stored participants and active rivals. It must not use a recurring whole-world daily, weekly, or monthly scan.
9. The Expedition Board may show only Expedition Progress, Logistics Readiness, and Exposure Risk as the main visible values.
10. Every phase exposes three to five primary actions. Six visible primary actions is the hard maximum.
11. One action may use no more than four spendable cost types.
12. Rival actions must have counterplay, attribution states, target validity, cooldowns, and cleanup.
13. Evolution III militarisation may cause Antarctic clashes and diplomatic incidents. It must not force ordinary countries into a global war.
14. No new country, focus tree, combat unit, character portrait, or required 3D model is part of this event.

## Process status

The design was written from the complete supplied project source set, the extracted subagent configuration files, the three catalog CSV snapshots, and focused external research from official Antarctic institutions.

This interface did not expose the project custom Codex subagent launcher, the installed `hoi4-agent-tools` MCP routes, the live Chaos Redux repository, the offline Paradox wiki snapshot, the installed vanilla game files, or the authoritative event-catalog XLSX. The package therefore includes context-complete prompts and exact evidence requirements for those later passes. It does not claim source implementation, MCP validation, live repository inspection, workbook editing, Git commits, or in-game testing.

No event-design route was shortened into a fallback. The tooling limitations above remain explicit process blockers for implementation validation and independent subagent closure.
