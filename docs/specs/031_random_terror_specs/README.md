# Event 31 Random Terror planning package

## Purpose

This package is the source specification for Event 31, Random Terror.

It defines a repeatable security crisis that can affect several countries in one firing, a compact national response loop, five evolutions, territorial extremist countries with a shared focus framework, the Global Jihad manual scenario, the public world-end branch The False Revelation, cross-event behavior, AI requirements, assets, achievements, and acceptance cases.

The package states the design the implementation must satisfy.
It does not contain Clausewitz code or final localisation.

## Reading authority

The thirteen numbered parts are the canonical design.
The three matrices hold row-level detail that the parts point to.
When a prompt, review, or matrix disagrees with a part, the part wins.

Acceptance basis:

- The user granted full design authority for the Event 31 takeover on 2026-10-04 and treated this folder as the accepted design, as recorded in [the agent decisions file](../../plans/031_random_terror_plans/agent_decisions_20261004.md).
- The decisions D1 to D13 and R1 to R47 in that file resolve gaps and contradictions under the same authority and are accepted design where they apply.
- The parent's 2026-10-07 instruction to complete every accepted file in this folder is recorded in [the current completion audit](../../plans/031_random_terror_plans/subagent_handoffs/031_current_completion_audit_20261007.md).
- The 2026-10-10 spec audit revisions listed in the changelog were made under the user's spec-audit brief, which authorized substantial rework of this package. They are design requirements whose implementation is pending unless a part says otherwise.

Implementation evidence proves what exists in source and does not establish design approval.
Live-game validation belongs to the user.

Repository rules come from `CLAUDE.md` at the repository root.
Workflow and subagent boundaries follow [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Implementation status

Event 31 has a substantial runtime implementation and is enabled by default (R41).
The implemented behavior is described in [the event documentation](../../events/031_random_terror/overview.md).
The latest completion verdict is "partial", with the open findings C01 to C14 listed in the completion audit linked above.

| Part | Status | Main open items |
| --- | --- | --- |
| 1 Identity and player loop | Implemented core loop, first emphasis, recurring pulse and closure | Campaign and multiplayer validation |
| 2 Targeting and incidents | Implemented engine and exact state losses | Valid incident pools (C13), distinct Deaths reasons (C11), migration adapter for relief strain (audit revision) |
| 3 Government response | All matrix decisions and eight missions exist, plus Press the Safe-Haven Host and Terminal Counteroffensive | Scaled costs and maintained commitments (C09), hostage approach choice (audit revision) |
| 4 Evolutions | Scheduling, enable checks, reports and logging implemented | Per-organization identity and support profile (Evolution I), disabled-after-unlock cases |
| 5 Country packages | Eight carriers, leaders, flags, research slots, technology inheritance, real formations | Resource-grounded forces and safe capitals (C07), merger and takeover reconciliation (C08), leadership contest defect (C05) |
| 6 Focus tree | 114 focuses with routes, filters, navigation and idea slots | Forge the Seal core rule, specialist route review |
| 7 Global Jihad | Five types, four intensities, preflight and cleanup | Type geography and Random Pattern mixture (C06) |
| 8 False Revelation | Gate, entity, five slots, objective-based strengths, uprising wave, both super-events | Terminal category access (C01), dominant-player choice (C02), commit revalidation (C03), victory and unity meaning (C04), aftermath (C10) |
| 9 AI and balance | Weights authored and reviewed in source | Named scenario evidence, Chaos feedback balance (audit revision) |
| 10 Cross-event | Event 14 rivalry, Event 21 guard, special-country classifier, world-threat source | Chaos impact map (audit revision replacing per-incident Chaos), famine, migration and camp bridges (audit revision) |
| 11 Assets | 444 inventoried runtime files plus map buttons | Entity animation state binding, 36 stale achievement hashes, flag cycle disposition |
| 12 Achievements | Twelve IDs, trackers, localisation and icon triplets | Cut Every Route network proof and safe-haven receipt (C12), full valid and invalid cases |
| 13 Documentation and catalog | Selectors, Event Details, SCN-016 row | Evolution IV workbook wording and status change queued in [catalog_changes_pending.md](../../plans/031_random_terror_plans/catalog_changes_pending.md) |

## Core design decision

Each affected government manages one primary visible value, Terror Pressure, and one supporting value, Response Legitimacy.

State activity is shown through one stage ladder, a staged state modifier and the Terror Activity map mode.

The ordinary response stays compact: three to five relevant actions per phase and no more than three active missions.

Deeper content appears only when the crisis escalates.
Territorial actors, focus routes, transnational coordination, foreign fighters, faction behavior and world-end content do not crowd the early response surface.

## Representation rule

Every organization created by Event 31 is invented for the game.
This is a design constraint on names, symbols, leaders and doctrine.
In-world text names the movements directly and does not call them fictional (D13); only the Triggerable Scenarios premise keeps a framing sentence.

The event does not associate terrorism with any religion, nationality, civilization, ethnicity, or ordinary political ideology.

Evolution IV introduces one invented jihadist movement as a specific extremist branch.
Muslim communities, clerics, soldiers, and governments can become its main opponents.
The movement treats many Muslim governments as priority enemies because it calls them illegitimate.
The event never treats ordinary Muslims as members, sympathizers, recruits, or security risks.

The False Revelation never confirms that its entity is Allah.

No asset may depict Allah, use Quranic calligraphy as villain branding, use a real extremist symbol, or use sacred Islamic audio as an enemy cue.

## Package map

Canonical parts:

1. [Part 1](031_random_terror_spec_part_1_event_identity_and_player_loop.md) event identity, values, stages, pacing and player loop.
2. [Part 2](031_random_terror_spec_part_2_targeting_and_incident_engine.md) country and state selection, incident families, spread, deaths, damage and cleanup.
3. [Part 3](031_random_terror_spec_part_3_government_response_decisions_and_missions.md) response category, decisions, missions, costs and outcomes.
4. [Part 4](031_random_terror_spec_part_4_evolutions_and_escalation.md) the five evolutions and their logging.
5. [Part 5](031_random_terror_spec_part_5_territorial_insurgency_and_country_packages.md) territorial seizure and country packages.
6. [Part 6](031_random_terror_spec_part_6_focus_tree_and_political_routes.md) the shared actor focus framework and idea lifecycles.
7. [Part 7](031_random_terror_spec_part_7_global_jihad_scenario.md) the Global Jihad scenario, `SCN-016`.
8. [Part 8](031_random_terror_spec_part_8_false_revelation_world_end.md) The False Revelation world-end branch.
9. [Part 9](031_random_terror_spec_part_9_ai_balance_probability.md) AI, balance and named probability scenarios.
10. [Part 10](031_random_terror_spec_part_10_cross_event_system_interactions.md) cross-event and shared-system interactions, including the Chaos impact map.
11. [Part 11](031_random_terror_spec_part_11_assets_presentation_and_localisation.md) assets, presentation and writing direction.
12. [Part 12](031_random_terror_spec_part_12_achievements.md) the achievement package.
13. [Part 13](031_random_terror_spec_part_13_documentation_catalog_and_acceptance.md) logs, Event Details, catalog, documentation and acceptance cases.

Matrices:

- [Decision and mission matrix](031_random_terror_decision_mission_matrix.md)
- [Country package matrix](031_random_terror_country_package_matrix.md)
- [AI and probability scenario matrix](031_random_terror_ai_scenario_matrix.md)

Prompts (pointers to the parts, scoped to remaining work):

- [Implementation continuation prompt](031_random_terror_coding_prompt.md) and its [short goal form](031_random_terror_goal_prompt.md)
- [Decision and mission prompt](031_random_terror_decision_mission_prompt.md)
- [Achievement prompt](031_random_terror_achievement_prompt.md)
- [Asset prompt](031_random_terror_asset_prompt.md)
- [Super-event prompt](031_random_terror_super_event_prompt.md)
- [Subagent routing](031_random_terror_subagent_routing_prompts.md)

Historical planning records (evidence only, not current instructions):

- [Research notes](031_random_terror_research_notes.md)
- [Improvement-loop review](031_random_terror_improvement_loop_review.md)
- [Source audit and limitations](031_random_terror_source_audit_and_limitations.md)
- [Reading guide](031_random_terror_complete_spec.md), a `superseded` compilation kept because older handoffs link to it
- [Manifest](031_random_terror_manifest.json) with file statistics and hashes

## Stable accepted terms

- Catalog event name `Random Terror`, Event ID `31`, type `Minor Repeatable`, Chaos level `1`, entry event `chaosx.nr31.1`.
- Evolution names `Organized Cells`, `Transnational Terror Network`, `Territorial Insurgency`, `The Jihadist International`, and `The Final Jihad`.
- Manual scenario `Global Jihad` at `SCN-016`, raw scenario ID `16`, compact list label `#016`, under [the shared identifier registry](../shared_identifier_registry.md) and [its JSON ledger](../shared_identifier_registry.json).
- Public world-end branch `The False Revelation`.
- Current catalog cluster membership Domestic Unrest, raw `event_cluster_id` `16`.
- The optional Internal Fracture proposal reserves raw `event_cluster_id` `22` (parent identity correction, 2026-10-07). The reservation does not approve or register the proposal and does not change current membership. Raw cluster `9` belongs to National Breakthroughs.

Check the authoritative workbook, live registries and shared reservations before adding or changing any registration.

## Scope boundaries

No custom combat battalion, equipment archetype, aircraft, ship, vehicle, building model, or 3D entity is required.
Spawned countries use existing land unit types, so no Event 19 provider, custom unit sound, bespoke counter, or 3D pipeline work is needed.
This is an accepted scope decision, not a fallback.

No dedicated Event 31 scripted GUI is required.
The response uses ordinary decision categories, static category pictures, dynamic category text, targeted state decisions, and the event-owned state map mode.

The entity of The False Revelation may use one animated portrait because it is an impossible subject and the animation marks a world-end identity change.

## Open questions

These proposals came from the 2026-10-10 audit but touch accepted decisions, so they wait for a user or parent decision.

1. Response Capacity in the category header (R37). The value grows automatically with every response, so the number itself rarely drives a choice. Proposal: drop it from the header and keep it only in the Targeted Raid and Intelligence Sweep tooltips, where it explains the better odds. The header would then show Terror Pressure, Response Legitimacy and the crisis-state count.
2. Terminal Counteroffensive as the only coalition action (D12, amended by R38). Proposal: after C01 restores government access at world end, keep it as the single terminal action and express the other counterplay through existing decisions (Prepare Retake on a command capital, Isolate the Enclave on a corridor state, Stop the Coordinated Uprising) rather than adding new terminal decisions.
3. Global firing scale at Evolutions IV and V (15 and up to 20 newly affected countries per firing, Part 1). With recurring pulses and spread, this may produce more simultaneous crises than the AI and the Chaos Meter can absorb. Proposal: cap newly affected countries at 10 per firing and let higher evolutions intensify existing crises instead. This changes implemented tuning (`random_terror_tuning.jihadist_targets`, `final_targets`).

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Rewrote this README: acceptance basis now cites the user's 2026-10-04 design authority and the D and R decisions instead of an unresolved blanket claim, and a status table maps each part to the implementation and to the completion-audit findings C01 to C14.
- Replaced `AGENTS.md` and `.agents/skills/` references with `CLAUDE.md` and `.claude/skills/`, and removed Codex-specific `fork_turns` instructions and "repository not present" claims across the prompts.
- Reconciled the parts with implemented behavior: event enabled by default (R41), in-world wording without "fictional" labels (D13), Domestic Unrest cluster membership, first emphasis choice (R32), recurring pulse (D4), crisis closure (R30), safe havens (R42), surrender terms (R46), civil-war ideology rule (R45), world-threat source (R47) and objective-based terminal strengths (R38).
- Added an implementation-status section to every part, naming what is implemented and which audit findings remain open, without deleting the requirements those findings measure.
- Cut the prompts to pointers: the coding, goal, decision, achievement, asset, super-event and routing prompts no longer restate the parts and now list only remaining work with links to the owning sections.
- Marked the source audit and improvement review as historical records and removed their stale blocker lists.
- Fixed a heading level in Part 4 and changed achievement "Proposed ID" labels to the registered IDs.

Pass 2, design improvement:

- Added a Chaos impact map to Part 10. Ordinary incidents no longer add direct Chaos (the implemented `+5` per incident would push the meter toward later evolutions through repetition alone); Chaos comes from milestones such as actor formation, captured capitals and coups, with reversals and a rolling cap.
- Connected Event 31 to the reworked famine and migration systems: relief strain and captured-territory flight go through migration's owner-proven requests, coerced extraction feeds famine's extraction component, and the actor economy failure form becomes Supply Collapse so it no longer imitates the famine system.
- Connected camps: a government that runs camps in its own crisis states is treated as using collective punishment, with legitimacy, recruitment and achievement consequences.
- Set a terminal presentation budget: the final command shows its three strengths and the command-capital state, and the government category must stay usable after world end.
- Turned the hostage response into one choice on the hostage report (negotiate, prepare a rescue, storm at once) instead of a wider decision set.
- Replaced the four-phase terminal campaign with objective-driven beats and condensed the defeat aftermath to a few consequential choices.
- Condensed the six government AI profiles in Part 9 into one table and added a Chaos feedback balance scenario.
