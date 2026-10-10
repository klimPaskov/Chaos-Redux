# Event 007 Fury planning package

## Authority and resume boundary

Read [accepted release corrections](specs/007_fury_release_corrections_2026-10-05.md) before the core, scenario, focus, decision, acceptance, and production documents.
They cite the user's 5 October G1-G7 instruction and parent acceptance and take precedence only for their bounded claims.
[Parent decisions](../../plans/007_fury_plans/agent_decisions_2026-10-05.md) retain implementation and validation dispositions, and the [release review](../../plans/007_fury_plans/release_review_2026-10-05.md) lists the validation still owed.
The Internal Fury branch and ordinary per-country defeat news remain unresolved; see Open questions.
Select remaining work from the [coding prompt](prompts/007_fury_coding_prompt.md), not from older planning text.
Use [chaos-redux-subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for current ownership and evidence rules.

This package specifies Event ID `7`, `Fury`, which replaced the old expansionism placeholder with a dynamic repeatable war event.
A small AI country is taken by a fast expansion system, receives an initial army and a finite hidden reinforcement reserve capped at 100 scripted divisions per actor, attacks weaker eligible neighbours, absorbs territory through compliance and coring work, and either burns out or grows into a continental threat.

Implementation status: implemented in source, with release validation incomplete.
The specs describe the current implementation; unadopted drafts are marked where they appear, and design not yet accepted lives only in Open questions.

## Package map

| Path | Role |
| --- | --- |
| `specs/007_fury_release_corrections_2026-10-05.md` | Accepted release corrections; overrides older claims within its scope |
| `specs/007_fury_spec_part_1_core.md` | Core identity, eligibility, targeting, package, internal values, settlement, shared-system connections |
| `specs/007_fury_spec_part_2_evolutions_world_end.md` | Evolutions, world-end branch, super-events, presentation beats, anti-Fury layer, cleanup |
| `specs/007_fury_focus_tree_spec.md` | Implemented 52-focus tree, branch roles, ideas, AI behavior |
| `specs/007_fury_decisions_missions_spec.md` | Both decision categories, missions, unadopted drafts |
| `specs/007_fury_triggerable_scenario_spec.md` | Triggerable scenario `The World in Fury` (SCN-005) |
| `specs/007_fury_achievements_spec.md` | Ten achievement designs and their source IDs |
| `matrices/007_fury_country_package_matrix.md` | Dynamic country package for transformed minors |
| `matrices/007_fury_ai_balance_matrix.md` | Target scoring, reserve scaling, strain and momentum, exploit checks |
| `matrices/007_fury_event_flow_map.md` | Text flow of the loop and overlays |
| `focus_graphs/007_fury_focus_tree_route_map.mmd` | Focus prerequisite graph mirrored from source |
| `prompts/007_fury_coding_prompt.md` | Remaining source work and decision-gated work |
| `prompts/007_fury_goal_prompt.md` | Compact `/goal` prompt for the remaining work |
| `prompts/007_fury_asset_prompt.md` | Installed assets and open asset items |
| `prompts/007_fury_super_event_prompt.md` | Implemented super-events and the optional aftermath super-event |
| `research/007_fury_research_notes.md` | Source notes and design constraints |
| `acceptance/007_fury_acceptance_criteria.md` | Pass or fail criteria |

## Core non-negotiables

- Fury is AI-selected only in random and triggerable setup.
- The player, player allies, and player subjects are never granted the Fury package by this event.
- Baseline target selection can choose AI or player-controlled countries when normal target gates allow it; player exclusion applies to Fury actor selection.
- Fury candidates are dynamic small mainland minors with few states and a valid land-neighbour target.
- Initial units, finite reserve-spawned reinforcements, coring, war declarations, target choice, and AI behavior scale dynamically. Reserve-spawned reinforcements draw one unit per weekly tick from the hidden reserve instead of becoming infinite weekly divisions.
- Baseline Fury fights one weaker neighbour at a time.
- Evolution II allows two Fury actors and the mutually exclusive cooperation or rivalry route.
- Evolution III allows three Fury actors and all-neighbour declarations.
- Evolution checkboxes govern every stage, including manual content.
- The custom triggerable scenario is named `The World in Fury`, has the normal four intensity stops, excludes the player, and has pact or hostile type choices.
- Maximum intensity creates up to sixteen dispersed Fury minors when enough eligible AI countries exist.
- One opening World News marks each successful outbreak batch, and a campaign-once news marks the first genuine territorial gain.
- A super-event marks the first Fury actor becoming major-sized.
- A terminal world-end branch can spread Fury to other continents and bind new Fury countries to the main Fury faction.
- Fury's internal values never appear as player-facing numbers.

## Open questions

Each item below is `unresolved` until the user or parent records a disposition.
Items marked "proposed (spec audit 2026-10-10)" are new design from the 10 October audit, not accepted design.

### Carried unresolved items

1. Internal Fury branch.
   The original focus spec named three political paths (War Directorate, Civil Mobilization, Compliance Administration); the 52-focus implementation omits them and no decision accepts their removal.
   Proposed (spec audit 2026-10-10): reject the three-path family.
   Fury is AI-only, so the player never sees the choice; Civil Mobilization would duplicate Army of the March and Hardened Fury's recruitable-population bonus, Compliance Administration would duplicate the occupation branch and `Core by Administration`, and a War Directorate leader swap is cosmetic for an AI actor.
   If the user prefers to keep a visible internal identity, the smallest useful form is one late focus that replaces the leader with the institutional War Directorate, with its portrait routed to `chaosx_portrait_creator`.
2. Ordinary per-country defeat news.
   Only the terminal-wide `chaosx.nr7.53` report exists.
   Proposed (spec audit 2026-10-10): send one report, not World News, to human countries that fought or bordered a defeated actor that had gained territory, so containment has a visible payoff without adding a broadcast to every defeat.

### Design proposals from the 10 October audit

All items are proposed (spec audit 2026-10-10).
Any accepted change to weights, scores, or reserves needs a before-and-after comparison through `chaosx_ai_probability_auditor`.

3. Momentum as a signal, not a clock.
   `fury_momentum` gains a fixed amount every week regardless of results, so after a year it mostly measures age, and anti-Fury successes of one point are erased within weeks.
   Gain weekly momentum only when the actor controls more states than at the previous tick or its target left the war; lose it weekly while at war without territorial gain.
   Anti-Fury mission successes then visibly slow the actor, and stalled actors produce smaller waves.
4. One strain value.
   `fury_overextension` seeds `fury_occupation_pressure` every week, and the two are read against separate gates (target score and the selection decision versus the idea, crisis, and target block).
   Keep only occupation pressure as the strain value and move every consumer and tuning gate onto it, removing a duplicated internal value without changing any player-visible surface.
5. Target preparation is spent per war.
   Preparation accumulates forever and adds the same bonus to every candidate, so it only widens the score gate.
   Spend it when a war is declared, so preparation becomes the deliberate way an actor reaches one stronger target rather than a permanent drift toward any target.
6. Anti-Fury missions that ask for map action.
   Border Watch and Supply Denial succeed by waiting out the timer, and Emergency Aid does not check its route.
   Require supplied divisions in the responder's states bordering the Fury actor at timeout for Border Watch, control of those border states for Supply Denial, and a target still at war and not capitulated for the aid route; this closes the decision audit's unresolved finding.
7. Harsh coring as a migration cause.
   `Core by March` could submit `migration_request_occupation_pressure` for the cored state, so forced registration produces flight through the existing migration owner while `Core by Administration` does not.
   This uses an existing entry point and adds no new value.
8. Random War overlap.
   Part 2 intends Fury to avoid a target already fighting an Event 004 war in the same short window, but no guard exists.
   Add a target-score penalty read from an Event 004-owned trigger; this needs the Event 004 owner to expose that trigger.
9. Internal fracture.
   Extreme pressure currently pauses targeting but has no failure outcome beyond the crisis mission.
   If the restore-registers crisis fails while pressure stays extreme, release the original owner of the largest unregistered annexed block through vanilla `release` when that tag no longer exists and still holds cores there, provided no other event's release transaction owns those states.
10. Actor milestones apply evolutions.
    Evolutions unlock purely by Chaos tier and apply to every existing actor at once.
    Keep the tier as the unlock for new openings, but apply Hardened Fury to an existing actor only after its first territorial gain and Two Fires only after it wins a war, so tier influences and gameplay decides, consistent with the user's 10 October direction on date gates.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency: the focus spec, route map, and decision spec were rewritten around the implemented 52-focus tree and decision set, with unadopted drafts listed once instead of described as requirements.
Retired Pact Cohesion, Reach, partition, Recognition Denial, extra templates, and Improvised Command were removed from Parts 1 and 2, the matrices, the scenario spec, and the flow map; the major threshold, settlement, evolution unlock rule, news beats, and anti-Fury layer now match source.
Broken super-event asset paths, `.agents/skills` links, and a garbled faction rule were fixed; the consumed decision and achievement prompts were removed because their content is implemented and covered by the specs, and the coding, goal, asset, and super-event prompts now list only remaining work.
Pass 2, design: Fury values are defined as internal AI drivers with no player-facing numbers, existing shared-system connections are recorded, and ten open questions carry the two unresolved items plus eight proposals.
Source defects found but not edited here: stale pact-cohesion tooltips, two unused cohesion constants, and literal tuning values, all listed in the coding prompt.
