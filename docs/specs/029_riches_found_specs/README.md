# Event 029: Riches Found specification package

This package is the design source for Event 029, a repeatable state-bound wealth crisis: a random country finds exceptional mineral wealth in one state, gains exactly 1,000 political power, and the mine then follows whoever controls the state through development, revenue, concessions, security, raids, closure, and three high-chaos evolutions.

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).

## Status

Event 029 has a substantial source implementation; the catalog status is Needs Testing, and the user owns live testing.

The source map is [the Event 029 overview](../../events/029_riches_found/overview.md); dated decisions, audits, and evidence are in [the plans folder](../../plans/029_riches_found_plans/), with the latest checkpoint in `subagent_handoffs/parent_continuation_2026_10_08.md`.

The spec parts mark each claim as **Implemented** (source review only), **Pending** (accepted design not yet in source), or **Proposed** (awaiting acceptance).

The remaining work list is owned by [the coding prompt](029_riches_found_coding_prompt.md#remaining-work).

## Acceptance basis

- User requirements: exactly 1,000 political power on discovery; a completely random recipient; Evolution I at Chaos Tier 600+; the benefit set of ticking political power, construction speed, production efficiency, military factory output, and a civilian-factory benefit; Minor Repeatable with no cluster (2026-10-07 instruction); and the instruction to implement this package fully without simplifications, fallbacks, placeholders, or omitted routes.
- Accepted design: the rest of this package, accepted through that implementation instruction, together with the dated agent decisions in `docs/plans/029_riches_found_plans/agent_decisions_2026-10-04.md` taken under the user's full-authority grant.
- The 2026-10-10 audit changes in the changelog were made under the user's 2026-10-10 audit brief, which authorized substantial rework to remove redundant values, repetitive decisions, and micromanagement; items that touch a recorded user requirement are listed under Open questions instead.

## Package map

| File | Owns |
| --- | --- |
| [Part 1, core loop](029_riches_found_spec_part_1_core_loop.md) | Identity, recipient and state selection, Event 018 separation, profiles, transfer, visible values and header, hidden state, stages, aggregate, caps |
| [Part 2, baseline progression](029_riches_found_spec_part_2_baseline_progression.md) | Milestones and overlays, projects and bands, revenue routes, concessions, security, closure, collapse, controller-change variants |
| [Part 3, decisions and missions](029_riches_found_spec_part_3_decisions_missions_foreign_interference.md) | Decision layers, cost rules, decision and mission families, foreign targets and interference, occupation, cleanup, exploit controls |
| [Part 4, evolutions](029_riches_found_spec_part_4_evolutions.md) | The three evolutions, containment, The Gilded Sovereignty, The Bottomless Account |
| [Part 5, AI, balance, interactions](029_riches_found_spec_part_5_ai_balance_interactions.md) | AI intent, the 1,000 political power, repeatability, exploit prevention, multiplayer, shared systems, persistence |
| [Part 6, assets, writing, achievements](029_riches_found_spec_part_6_assets_localisation_achievements.md) | Asset inventory and status, writing direction, the seven achievements |
| [Research notes](029_riches_found_research_notes.md) | Historical, economic, governance, security, and folklore research and its sources |
| [AI probability scenarios](029_riches_found_ai_probability_scenarios.md) | Named scenarios, audit sequence, evidence status |
| [Acceptance criteria](029_riches_found_acceptance_criteria.md) | Test scenarios and acceptance conditions |
| [Catalog alignment](029_riches_found_catalog_alignment.md) | Catalog row, Event Details, and evolution wording rules |
| [Coding prompt](029_riches_found_coding_prompt.md) | Continuation entry point and remaining work |
| [Goal prompt](029_riches_found_goal_prompt.md) | Compact goal statement |
| [Decision and mission prompt](029_riches_found_decision_mission_prompt.md) | Decision surface audit and handoff format |
| [Achievement prompt](029_riches_found_achievement_prompt.md) | Achievement verification |
| [Asset prompt](029_riches_found_asset_prompt.md) | Remaining asset work and routing |

## Main design decisions

- Event 029 is Minor Repeatable with no cluster, chaos level 1.
- The mine belongs to the state; ongoing benefits follow the current controller through one narrow control-change hook and a bounded registry of at most 64 mines, never a whole-world scan.
- Event 029 owns windfall governance; Event 018 owns physical resources, caves, Oth-Kesh, and The World Opens Below, and the two never share a state.
- The player reads Extraction Pressure as the primary value, Local Order and Revenue Legitimacy as supporting numbers, and Mine Development as a band; everything else stays internal.
- One ordinary decision category with a static picture; a scripted GUI would add maintenance and visual weight without improving any decision.
- Only three evolutions are registered (600+, 800+, 1,000+), because the planning rule allows one per chaos tier and Evolution I is fixed at 600+; The Gilded Sovereignty and The Bottomless Account are late outcomes inside their tracks, not extra rows.

## Scope boundaries

Event 029 has no focus tree (any ordinary country can own a mine and the mine system already gives lasting play), no country tag (capture is represented through state and controller systems), no super-event (no single global threshold or terminal state), no manual scenario, no custom unit, and no portraits, flags, animation, audio, or 3D assets.

## Open questions

### Conflicts with recorded user requirements

1. Repeat windfalls: because the recipient is completely random, one country can receive several 1,000 political power windfalls in a campaign.
   A proposal to halve a country's selection weight for a few years after it receives a windfall would make repeats rarer.
   It conflicts with the completely random recipient, so it waits for the user's decision.
2. Cost scaling: the 2026-10-08 checkpoint lists a "full state/country-sensitive cost quote" as outstanding.
   This audit narrows the Part 3 rule so prices vary only with geography, damage, and repetition, while other conditions change outcomes and availability instead of price.
   Because the user asked for the package to be implemented without simplifications, the user should confirm that the narrowed rule replaces the outstanding item.

### Proposals awaiting acceptance

These do not touch a user requirement; each is marked Proposed in its part and changes no source until accepted.

1. An unmanaged rush or Predatory Extraction submits one bounded food-need component to the famine system (Part 2, Rush pressures).
2. Evacuate the Workforce moves its people through migration's organized evacuation and exact civilian transfer (Part 3, Evacuate the Workforce).
3. An Event 013 earthquake in a mine state raises collapse pressure from that disaster's existing report (Part 2, Ordinary collapse).
4. Merge foreign claim pressure into concession exposure and sealed-depth integrity into deep excavation if no consumer distinguishes them (Part 1, Hidden state).

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Replaced the original planning-environment claims (no repository, wiki, MCP, or subagent access, Codex runners, `AGENTS.md`, `fork_turns`, the `.agents/skills` mirror, and the ImageGen route name) with the current Claude workflow, `CLAUDE.md`, `.claude/skills`, and the asset skill's image route.
- Recorded the 2026-10-07 user instruction that Event 029 has no cluster, superseding agent decision D2, and refreshed the catalog file to the current row (chaos level 1, Needs Testing, wording matching localisation).
- Marked implemented, pending, and proposed behaviour across the parts against the overview and the plans folder, including the milestone and overlay model, the decision layers, the five opening policies, revenue routes, partner list, occupation set, Deny the Mine, Chaos Meter sources, Deaths reasons, hidden-abuse Condemnation, containment, Gilded constraints, account terms, and the asset and achievement state.
- Made one owner per topic: the header in Part 1, the layers and cost rules in Part 3, writing direction and achievement definitions in Part 6, scenarios and the audit sequence in the AI scenarios file; the prompts, acceptance criteria, and Part 5 now point to them instead of restating them.
- Rewrote the coding, goal, decision and mission, achievement, and asset prompts as continuation prompts with the remaining work, and trimmed the acceptance criteria's review gate, MCP gate, and completion sections to `CLAUDE.md` pointers while keeping every test scenario.
- Deleted `029_riches_found_source_review_manifest.md`, which only recorded the original upload hashes, Codex subagent TOML files, and environment limits; its design rationale moved to Scope boundaries and its sources are already cited in the research notes.
- Fixed stale names: state-modifier and controller stage names now match the source, Reopen the Mine and the Evacuate the Workforce mission joined the inventories, and the Event 016 and Event 013 links are recorded as not implemented.
- Recorded the probability tool limitation (the 3.10.0 classifier files timed decisions as missions) and the current evidence status in the AI scenarios file, and reflowed multi-sentence lines to one sentence per line across the package.

Pass 2, design improvement:

- Header: Mine Development becomes a band, the deposit, policy, and revenue lines move to the tooltips that explain them, and at most one conditional line remains, so the header carries only values that drive a decision.
- Folded the separate four-step quality band into the deposit profile, dropped the development-plateau and settlement-profile concepts as separate values (the band and policy profile already carry them), and dropped the separate controller curse spirit and five-step supernatural spirit in favour of the existing stages.
- Folded unimplemented duplicate options into existing actions (emergency concession and hands-off claims, company housing, informal growth, emergency fees, security contract, joint public venture, mixed security board), so no layer gains buttons that repeat another choice.
- Narrowed dynamic costs to geography, damage, and repetition, which the player can see and act on (see Open questions).
- Asked for two-value opening option tooltips and a shorter aggregate tooltip, removing rows of one- and two-point changes.
- Added meaningful shared-system connections as proposals (famine food need from an unmanaged rush, migration hand-off for evacuation, Event 013 earthquakes) and stated where Event 029 deliberately has no connection (camps, CBRN, fallout, Air Cleanliness, world threat).
- Required every hidden value to have a producer and a consumer with a visible effect, and proposed two merges.
