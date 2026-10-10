# Event 82: Law Upgrade
## Full planning package

**Catalog:** Minor Repeatable · Chaos level 1 · Military Preparation · Low member.

This package preserves the user's worldwide one-step law progression, War Support grants, evolution thresholds, two 99% extreme laws, and doubled manual reversal costs. It expands them into complete authored design, balance proposals, compatibility and AI contracts, presentation, achievements, and implementation handoffs.

**Status:** proposed design, not implemented; the legacy `events/082_law_upgrade.txt` remains in place.

## Repository entry point

This package is installed at `docs/specs/082_law_upgrade_specs/`.
The original delivery's companion folder `docs/plans/082_law_upgrade_plans/` was never installed; implementation records belong there when work starts.
Start the implementation agent with [the goal prompt](082_law_upgrade_goal_prompt.md).

## Specification parts

| Part | File | Main subject |
| --- | --- | --- |
| 1 | [Core](082_law_upgrade_spec_part_1_core.md) | Fixed catalog, worldwide premise, recipient scope, decision stakes |
| 2 | [Progression](082_law_upgrade_spec_part_2_progression.md) | Exact single-step advancement, snapshots, caps, concrete examples |
| 3 | [Evolutions](082_law_upgrade_spec_part_3_evolutions.md) | Thresholds, shared timing, cumulative settings, voluntary entry |
| 4 | [Totalen Krieg!!!](082_law_upgrade_spec_part_4_totalen_krieg.md) | 99% economic commitment, wartime benefits, civilian penalties |
| 5 | [Totalen Menschen!!!](082_law_upgrade_spec_part_5_totalen_menschen.md) | 99% legal recruitment, workforce collapse, population integrity |
| 6 | [Support and reversal](082_law_upgrade_spec_part_6_support_and_reversal.md) | Current-support formula, combined balance, two exact-price exits |
| 7 | [Compatibility and world](082_law_upgrade_spec_part_7_compatibility_and_world.md) | Owner systems, trade and crisis interactions, bounded Chaos |
| 8 | [AI and campaign play](082_law_upgrade_spec_part_8_ai_and_campaign_play.md) | Actual shortages, marginal recovery, saving and scenario priorities |
| 9 | [Presentation](082_law_upgrade_spec_part_9_presentation.md) | Native surfaces, writing direction, 17-image asset package |
| 10 | [Achievements and acceptance](082_law_upgrade_spec_part_10_achievements_and_acceptance.md) | Three sustained campaign achievements and release conditions |

The numbered parts explain the mechanic. Engine implementation instructions are in the separate handoffs.

## Companion contracts

[Compatibility matrix](082_law_upgrade_compatibility_matrix.md) defines the owner interface and open inventory.

[Probability scenarios](082_law_upgrade_probability_scenarios.md) defines inspector-first MTTH and AI evidence, without inventing probabilities.

[Acceptance matrix](082_law_upgrade_acceptance_matrix.md) contains 81 planned integration cases.

[Research and sources](082_law_upgrade_research_and_sources.md) distinguishes user requirements, observed legacy source, research, and incomplete external source closure.

## Four ready prompts

[Goal prompt](082_law_upgrade_goal_prompt.md) starts the implementation workflow.

[Coding prompt](082_law_upgrade_coding_prompt.md) owns gameplay, exact law/cost integration, persistence, AI, catalogs, and validation.

[Asset prompt](082_law_upgrade_asset_prompt.md) routes four reports, two law icons, two reversal icons, and nine achievement-state outputs.

[Achievement prompt](082_law_upgrade_achievement_prompt.md) covers all three achievements, conditions, disqualifiers, tracking, text direction, and states.

There is no super-event prompt because no super-event is mapped. The two reversal actions do not justify a separate large decision/mission system or its own prompt.

## Important design clarifications

Each firing grants one profile's support, not the sum of every evolution. Effects occur before the acknowledgment. A capped law produces no replacement Political Power.

Current War Support continuously mitigates the extreme laws' penalties. The two laws' own overlapping capacity effects combine multiplicatively so the economy bonus cannot erase the recruitment penalty by simple addition.

The two authoritative manual reversal actions return to the immediate vanilla predecessors. The charge is twice the resolved ordinary current price. An ordinary 113 PP quote means a 226 PP reversal.

The 99% recruitment law is not an instant manpower grant. The economy's legal allocation is distinguished from actual consumer-goods results. Both require exact installed-game evidence.

## Original planning-session evidence

The 22 September delivery read its 42 supplied files, ran no subagents or HOI4 tools, and passed 18 abstract arithmetic checks that test none of the 80 integration cases.
Its proposed balance and engine-sensitive mappings are not validated.

## Revision log

### 2026-10-10 spec audit

- Added an accepted and queued famine connection: Totalen Menschen!!! feeds a farm-labor production pressure into already vulnerable states through the famine owner, so the extreme recruitment law has a felt agricultural cost without starting famine in healthy states (Parts 5 and 7).
- Replaced the stale Event 61 placeholder note with the actual Return to Peacetime inverse-pressure contract (Part 7).
- Condensed the README status and planning-session narrative, and removed Codex-specific `fork_turns` instructions from the goal and coding prompts.
- Pass 2 review otherwise retained the design: War Support is the only support value, the two extreme laws have asymmetric exits, and every number drives a reversal decision.
