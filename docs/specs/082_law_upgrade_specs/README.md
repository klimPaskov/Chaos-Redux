# Event 82: Law Upgrade
## Full planning package

**Catalog:** Minor Repeatable · Chaos level 1 · Military Preparation · Low member.

This package preserves the user's worldwide one-step law progression, War Support grants, evolution thresholds, two 99% extreme laws, and doubled manual reversal costs. It expands them into complete authored design, balance proposals, compatibility and AI contracts, presentation, achievements, and implementation handoffs.

**Status:** specification authored. Gameplay, native engine validation, final assets, authoritative workbook changes, and required independent specialist reviews are not complete.

## Install the planning files

Extract `082_law_upgrade_specs.zip` into the repository's `docs/specs/` directory. The ZIP already contains the top-level `082_law_upgrade_specs/` folder.

Extract the separate `082_law_upgrade_plans.zip` into `docs/plans/`. It contains source coverage, same-author review, the executed arithmetic suite, and six ready isolated-review prompts. These are planning records, not gameplay files.

Start the implementation agent with [the goal prompt](082_law_upgrade_goal_prompt.md). It points to the detailed specification and companion prompts. It is 3,997 characters including its final newline.

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

[Acceptance matrix](082_law_upgrade_acceptance_matrix.md) contains 80 planned integration cases.

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

## Reading and capability disclosure

All 42 supplied text files were read end to end before drafting, including every supplied skill and all 20 agent definitions. Four additional repository documents or source files were fully read. Some other external references were only partially inspected or were unavailable.

Not every transitive must-read source was completed. In particular, the current installed-game documentation, full vanilla/DLC law source closure, exact native price provider, and all core offline wiki pages were not fully read. The detailed supplemental source audit lists each disposition.

No supplied subagent was actually spawned, and no HOI4 probability or live-game tool ran. The independent improvement-loop and probability reviews remain open.

The supplied abstract suite has 18 passing test methods. It checks arithmetic and ordinal rules only. It does not pass any of the 80 HOI4 integration cases.

No supplied text was intentionally abbreviated for speed. The complete authored specification does not claim that its proposed balance or engine-sensitive mappings have already been validated.
