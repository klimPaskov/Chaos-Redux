# Event 32: Missiles specification package

## Location and role

This package lives at `docs/specs/032_missiles_specs/` and is the design source for Event 32, Missiles.
The numbered spec parts and `032_missiles_system_connections.md` own the design.
The matrices, acceptance criteria and prompts point back to those owning sections instead of restating them.
Repository rules come from [CLAUDE.md](../../../CLAUDE.md), and subagent routing comes from [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Design summary

Event 32 is a Minor Repeatable global event with no cluster assignment and a Calm World minimum.
Each firing gives every valid existing country one missile technology step (or a mature-program package at the end of the line), an operational missile reserve and a usable launch state.
Repeat firings strengthen existing sites before adding new ones.
Five independent evolution tracks add Saturation Arsenals, Unreliable Guidance, Special Warheads, Rogue Launch Commands and Automatic Retaliation.

## Implementation status

Event 32 has a substantial runtime implementation in the active Events 1-40 milestone.
The runtime contract is documented in `docs/events/032_missiles.md`, `docs/events/032_missiles/overview.md` and the system notes under `docs/events/032_missiles/systems/`.
Implementation tranches, agent decisions and test results live in `docs/plans/032_missiles_plans/`.
Event 32 is in the reworked-event default-enable allowlist, while its catalog status stays `To Be Reworked` until the remaining items below are closed (`docs/plans/032_missiles_plans/catalog_changes_pending.md`).

| Surface | Status | Evidence or remaining work |
| --- | --- | --- |
| Global firing, recipients, technology adapter, reserve, sites | `implemented` in source | `docs/events/032_missiles.md` runtime and country-program sections |
| Operations, guidance, damage, Deaths, custody, capture, succession | `implemented` in source | Operation API section, `systems/ordinary_preparation.md`, reserve-custody and site-work plans |
| Special payloads (all four families held at preparation) | `implemented` in source | `032_chemical_receipt_implementation_2026-10-07.md` and `docs/systems/cbrn_warfare/chemical_payload_reservations.md` |
| Five evolution tracks and native MTTH pacing | `implemented` in source | `systems/evolution_pacing.md`, `032_native_evolution_implementation_2026-10-08.md` |
| Decision category, missions, crisis actions | `implemented` in source | Part 5 here and `agent_decisions_2026-10-04.md` |
| SCN-015 Missile Age at raw ID 15 | `implemented` in source | `systems/triggerable_scenario.md` |
| Assets (82 runtime DDS files) and eight achievements | `implemented` in source | `docs/plans/032_missiles_plans/asset_audit.md` |
| Event Logs, Event Details, five evolution rows | `implemented` in source | Event Logs bindings in `docs/events/032_missiles.md` |
| Reach against real target distance | pending | Part 3, Reach: the current band is never compared with distance |
| Territory-scaled site cap | pending | Part 2, Site count cap: only the flat cap of four is enforced |
| Denial exposure, Event 52 fuel-crisis slowdown | pending | Part 5, Deny responsibility; system connections, Event 52 |
| Asset workspace cleanup | pending | Part 7, Asset paths |
| Event doc pacing section | stale | `docs/events/032_missiles.md` still describes the retired delayed-job pacing; `systems/evolution_pacing.md` is current |
| Direct Chaos Meter budgets | `unresolved` | Part 1 Chaos effects; constants exist in `missiles_tuning` but nothing pays them |
| Probability evidence for weighted surfaces | `blocked` by repeated `hoi4.probability_inspect` `INTERNAL_ERROR`; source-derived calculations still owed | Part 6 and `032_missiles_test_results.md` |
| Live-game validation | user-owned | `032_missiles_test_matrix.md` |
| Catalog status promotion | `accepted and queued` until the rows above close | `catalog_changes_pending.md` |

Implementation evidence proves what exists in source; it does not prove live engine behaviour.

## Acceptance basis

The user granted the implementing agent full authority over the Event 32 implementation and asked for the complete design in this package.
Decisions taken under that grant are recorded with their basis in `docs/plans/032_missiles_plans/agent_decisions_2026-10-04.md` and the later dated plan files, and they count as parent acceptance within the user-authorized scope.
The one explicit user instruction recorded for this event is the presentation rule: one ordinary decision category with a static picture and no dedicated scripted GUI.
Proposals added by the 2026-10-10 audit are marked `unresolved` where they appear and are listed under Open questions.

## Central design decisions

1. Event 32 fires once at the global pacing level and dispatches one bounded transaction to each frozen valid recipient.
2. The country program exposes three player-facing values: Operational Reserve, Launch Readiness and Command Control.
3. Guidance grade, site status and retaliation posture are compact labels, not further meters (part 2, Player-facing value budget).
4. One ordinary decision category with a static picture presents the program; there is no dedicated scripted GUI (explicit user instruction).
5. Strikes use the event-owned scripted operation adapter; no native raid adapter or raid icon is added because the RaidInstance API cannot authenticate the launch state and multi-site custody (part 8).
6. Special payloads need existing technology, policy, stockpile and site custody, are held at preparation and consumed once at release through the owning CBRN systems.
7. Event 32 owns no terminal branch; a severe nuclear exchange can reach Fallout only through the shared Air Cleanliness route.
8. Automatic retaliation runs through a bounded incident queue with generation, participant, incident and queue caps.
9. An evolution unlock grants access only; Saturation doctrine and retaliation posture are explicit country choices.
10. All tuning sits in `common/script_constants/032_missiles_*constants.txt`.

## Package map

| File | Purpose |
| --- | --- |
| `032_missiles_spec_part_1_core.md` | Identity, recipients, firing flow, progression, reports, Event Logs and the Chaos budget proposal |
| `032_missiles_spec_part_2_program_and_launch_sites.md` | Program values, visible value budget, technology adapter, sites, capture and succession |
| `032_missiles_spec_part_3_operations_and_consequences.md` | Operations, targeting, guidance, damage, payloads, incidents and retaliation bridge |
| `032_missiles_spec_part_4_evolutions.md` | The five evolution tracks, pacing and logging |
| `032_missiles_spec_part_5_decisions_missions_and_scenario.md` | Decision category, phases, actions, missions and SCN-015 |
| `032_missiles_spec_part_6_ai_and_probability.md` | AI profiles, scoring and probability evidence rules |
| `032_missiles_spec_part_7_assets_text_and_achievements.md` | Visual inventory, writing direction and achievement architecture |
| `032_missiles_spec_part_8_implementation_contract.md` | Ownership, APIs, runtime boundaries and performance limits |
| `032_missiles_system_connections.md` | Bridges to other events and shared systems, including proposed humanitarian links |
| `032_missiles_probability_scenario_matrix.md` | Named scenarios for weighted surfaces |
| `032_missiles_acceptance_criteria.md` | Completion checklist with per-section status |
| `032_missiles_test_matrix.md` | Static and live test cases |
| `032_missiles_requirement_traceability.md` | Mapping from the supplied requirements to owning sections |
| `032_missiles_achievement_prompt.md` | Owning definitions of the eight achievements |
| `032_missiles_asset_prompt.md` | Asset production brief (delivered) |
| `032_missiles_decision_mission_prompt.md` | Decision and mission audit prompt |
| `032_missiles_coding_prompt.md` | Continuation prompt for the remaining implementation work |
| `032_missiles_goal_prompt.md` | Compact continuation goal |
| `032_missiles_improvement_loop_closure.md` | Planning-time depth review and rejected expansions |
| `032_missiles_research_notes.md` | Historical and technical design references |
| `032_missiles_source_review.md` | Historical record of the original planning inputs |

## Open questions

These are `unresolved` proposals from the 2026-10-10 audit.
Each one would change accepted implemented behaviour or an unaccepted proposal, so none is a requirement until the user or parent accepts it.

1. Chaos budgets (part 1): accept the direct Chaos map, and drop the Saturation Arsenals budget entirely because the track has no distinct abnormal outcome.
   The unused constants `missiles_tuning.*_unlock_chaos` are named for unlock payment, which the map forbids, so wiring them as named would contradict the design.
2. Inspect the Incident (part 5): the decision mainly closes the incident response, which is a ceremonial click.
   Proposal: close an incident automatically when no response action remains and keep the report as the inspection surface.
3. Special-payload policy for human players (part 4): a human already chooses the payload for every strike, so the five-option policy only matters for delegated and automatic responses and for AI.
   Proposal: show policy to humans only once a Delegated or Automatic posture exists, and fold it into the posture choice.
4. Site security and hardening (part 2): two hidden per-site values have separate improvement paths but the player sees one site status.
   Proposal: merge them into one site protection value, with national Command Control carrying the authority side.
5. Humanitarian aftermath (system connections): route populated-state strike damage into the migration bombing adapter and logistics-strike railway damage into the famine transport adapter.
   Both receiving systems already accept bombing as a proven source; the Event 32 side needs a design decision on thresholds.
6. Captured-site diplomatic transfer was rejected for this round (agent decision); reopen only if Event 6 or Event 5 needs a negotiated custody transfer.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Rewrote this README around current implementation status, the acceptance basis and a per-surface status table; replaced the `AGENTS.md` and `.agents/` links with `CLAUDE.md` and `.claude/skills/`.
- Deleted `032_missiles_package_manifest.md`: its SHA-256 table and archive receipts were stale and duplicated this file index.
- Reconciled parts 1, 2, 4, 5 and 8 with implemented behaviour: default enablement, scripted operation adapter, four captured-site resolutions, native MTTH evolution clocks, canonical evolution log identity (type 32, stage = catalog number), SCN-015 locked at raw ID 15, payload holds for all four families, and the explicit Saturation doctrine and posture decisions.
- Removed requirements the implementation rejected with a recorded basis: changing the participating site or preparation effort of a prepared operation, retargeting a retaliation after new evidence, and diplomatic transfer of captured sites.
- Replaced the recommended file list, API names and subevent ranges in part 8 with pointers to the real runtime files and ID map.
- Rewrote the coding, goal and decision-mission prompts as short continuation prompts that point to owning sections; replaced Codex `fork_turns` instructions with the Claude subagent rule.
- Added a status table to the acceptance criteria, removed checklist lines that only restate CLAUDE.md rules, and fixed stale lines (disabled-by-default, raid icons, redirect action).
- Updated the test matrix pacing cases to the native MTTH model and noted the live-test and probability ID namespaces.
- Recorded gaps found by comparing the spec with source: reach is never compared with target distance, the territory-scaled site cap constants are unused, the Chaos constants are unused, the Event 52 fuel bridge is absent, the asset workspace is not cleaned, and the event doc's pacing section is stale.
- Pointed the probability workflow at the CLAUDE.md retry limit and source-derived calculations, since every `hoi4.probability_inspect` call has failed.

Pass 2, design improvement:

- Added a player-facing value budget (part 2): three national values plus one guidance grade, one site status and one posture label; hardening, security, capacity, pressure scores and receipts stay internal.
- Reduced the program idea to a three-state identity and moved numbers out of it.
- Marked the direct Chaos map `unresolved` and not implemented, and proposed removing the Saturation budget that had no qualifying outcome.
- Simplified the special-payload integration record to the states players act on.
- Added proposed humanitarian links (migration flight from populated-state strikes, famine transport pressure from logistics strikes) as `unresolved` connections with owner-side APIs named.
- Listed ceremonial or duplicated surfaces (incident inspection, human payload policy, separate site security) as open questions instead of silently changing accepted behaviour.
