# Event 027: Doctrine Research specification package

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).

This folder is the source specification for Event 027, Doctrine Research.
The implemented behaviour is described in `docs/events/027_doctrine_research/overview.md`, and implementation decisions, evidence, and handoffs live in `docs/plans/027_doctrine_research_plans/`.

## Design in brief

Event 027 is a global Minor Repeatable positive event.
One firing gives every live country that has a doctrine system and a valid doctrine action a curriculum of choices: one at baseline, rising to five at Evolution IV.
Each choice selects a doctrine domain and either establishes one eligible Grand Doctrine, which spends the choice without mastery, or advances one subdoctrine by exactly one mastery level, assigning an empty track first when needed.
Choices can be stacked on one branch or spread across tracks and domains, the event's own action costs no experience, and an exhausted country receives no substitute.
Army, Navy, Air, Special Forces, and Chaos Warfare take part through fail-closed adapters, and Chaos Warfare shares the Army `land` folder.
Humans resolve a chain of country events, AI countries resolve the same pool silently with scores built on real force structure and the native doctrine preferences, and every country owns a queue of curricula that survives save, reload, and control changes.
The event records one actorless History row per firing, belongs to the National Breakthroughs cluster, and carries one report image and three achievements.

## Files

| File | Owns |
| --- | --- |
| `027_doctrine_research_spec_part_1_core.md` | Identity, terminology, choice rules, costs, banked mastery, participation, queue, persistence, and connections with other systems. |
| `027_doctrine_research_spec_part_2_choice_flow.md` | Page flow, direct advance, the result page, the general staff option, Special Forces handling, AI resolution steps, and edge cases. |
| `027_doctrine_research_spec_part_3_evolutions_balance_ai.md` | Evolutions, AI scoring model, balance intent, exploit controls, and the cluster role. |
| `027_doctrine_research_spec_part_4_presentation_assets_achievements.md` | Writing direction, the visible-value budget, Event Details, assets, and achievements. |
| `027_doctrine_research_doctrine_registry_matrix.md` | The doctrine-domain adapter contract and the registration path for future domains. |
| `027_doctrine_research_research_notes.md` | Official doctrine-system findings, design inferences, and the engine questions the implementation answered. |
| `027_doctrine_research_probability_scenarios.md` | Named AI and selection scenarios with their evidence status. |
| `027_doctrine_research_catalog_cluster_handoff.md` | Workbook row state and National Breakthroughs membership. |
| `027_doctrine_research_acceptance_criteria.md` | Completion checklist with implemented, pending, and live-check status. |
| `027_doctrine_research_asset_prompt.md` | Replacement brief for the report image and achievement icons. |
| `027_doctrine_research_achievement_prompt.md` | Achievement validation cases to re-run after changes. |
| `027_doctrine_research_coding_prompt.md` | Continuation prompt for the open evidence. |

## Status and acceptance basis

| Claim group | Disposition | Basis |
| --- | --- | --- |
| Global Minor Repeatable event, curriculum sizes 1 to 5, adoption spending a choice without mastery, National Breakthroughs membership | Implemented | The user's original Event 027 brief. |
| Domain scoping, empty-track assignment, free actions, no compensation, queues, adapters, AI model, evolutions, exploit controls, achievements, assets | Implemented | Accepted under the full-authority mandate the user granted for the Event 027 takeover, recorded as D1 to D25 in `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`. |
| Engine behaviour listed under *(live)* in the acceptance criteria | Implemented, live check | Source evidence only; the user validates in a live session. |
| Flow revisions: first-choice premise on the domain menu, direct advance of an assigned track, the result page with the next step, the Chaos Warfare cost line, the outcome summary, trimmed option labels, and the general staff option | Implemented | Accepted under the 2026-10-10 full-authority release brief, which directs removing busywork, repetitive decisions, and bloated player-facing values. Special Forces entries keep their subdoctrine page, and the Milestone marker on domain options is not implemented. |
| Group E timeline, zero-reset subdoctrine comparison, group F recurrence | Accepted and queued | Required by the probability scenarios; queued because the automatic-selection pool and a second cluster member are not yet bound. |
| Workbook status change | Accepted and queued | `docs/plans/027_doctrine_research_plans/catalog_changes_pending.md`; queued for the workbook owner. |

## Open questions

None. The flow revisions proposed by the 2026-10-10 audit were accepted and implemented (see the changelog), including counting general staff choices for achievements.

## Provenance

The original package was written in a session without access to the repository, the offline wiki, vanilla files, the workbook, subagents, or the HOI4 MCP, from uploaded copies of the project rules, skills, catalog CSV exports, and subagent definitions.
Its full input inventory and its manual role-by-role review were removed in the 2026-10-10 audit and remain in Git history (`027_doctrine_research_source_review.md` and `027_doctrine_research_review_and_closure.md` at commit `db3a87c57`).
Every gap that session recorded was later answered by the implementation and is summarised in the research notes.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Reconciled the package with the implemented source and D1 to D25: Chaos Warfare is a `land` Grand Doctrine that uses the Army tracks and excludes an Army Grand Doctrine, so the earlier "four Chaos Warfare tracks beside Army" model, the Joint Curriculum case across Army and Chaos Warfare, and the "Special Forces absent when both tracks are occupied" rule were corrected.
- Recorded final achievement IDs, the player-facing word "curriculum", stage names, cluster 9 and row 9001, the 120-day cluster cooldown, the nonhuman participation gate, the mastery-gain-factor guard, and the Event 016 adoption record.
- Corrected the probability file: the event picker selects across all events, repeatable weight recovers on pacing pulses rather than monthly, and DR-F04 cannot be built until a second member exists; added an evidence-status table per weighted surface.
- Answered the research notes' fourteen engine questions from the implementation and moved the remaining unknowns to explicit live checks.
- Rewrote the acceptance criteria as a status checklist and removed the copies of `CLAUDE.md` rules, MCP mandates, and CSV rules restated across the criteria, prompts, and spec parts.
- Replaced the original implementation prompts, which named `AGENTS.md`, `.agents/skills`, a Codex thread, and a retired spawn parameter, with a continuation prompt and goal prompt for the remaining work; trimmed the asset and achievement prompts to replacement briefs and validation cases because part 4 owns the design.
- Deleted the source review and the manual review-and-closure files as stale provenance and duplicated closure text; their surviving points moved to this README and part 3.
- Removed absence notes (empty Evolution V and world-end fields, no 3D or animation, no super-event) and pointed the catalog handoff at `catalog_changes_pending.md` instead of restating workbook rows.

Pass 2, design improvement:

- Proposed R1 to R3 because the implemented flow costs six clicks per mastery step on an assigned track, and the result and continue pages carry no decision.
- Proposed R5, a general staff option, because an unanswered event times out after 13 days and the implemented flow would then spend choices through the first-listed domain, track, and confirmation.
- Proposed R4 to connect the free Chaos Warfare adoption with its real Deaths-ledger cost through the Chaos Meter combat collateral model.
- Proposed R6 and R7 to bring the summary and option labels within the planning skill's visible-value budget; the summary's eight counters drove no decision.
- Considered and rejected connections to famine, migration, camps, air cleanliness, and Condemnation, because Doctrine Research changes no state those systems read beyond the native Chaos Warfare consequences that R4 surfaces, and a link would be decoration.

### 2026-10-10 release pass

- Implemented the audit's flow revisions: the first domain menu carries the curriculum premise and size, an assigned track advances from the track menu, the result page carries the next step and closes the curriculum with its outcome, the general staff option runs the AI resolver for the remaining choices and shows the summary, and the Chaos Warfare adoption confirmation states its civilian-death cost.
- Replaced the eight summary counters with the outcomes that apply, and trimmed domain and track options and tooltips.
- Removed the opening page, the continue page, and the unused summary tallies.
- Kept Special Forces entries on their subdoctrine page and left out the domain-menu Milestone marker.
