# Event 81: British Tax

## Package status

This is the authored design package for the British Tax rework of the legacy `events/081_england_tax.txt`. It covers the persistent economic system, country permissions, the long resistance route, British responses, both Evolutions, settlements, AI behaviour, achievements, presentation, and implementation prompts. It is design material, not implemented HOI4 files or finished art.

User-supplied names and the rules listed under Important preserved rules come from the user's brief. New structural names are working labels, not final localisation. Numerical anchors are proposed balance targets, accepted within the original planning brief and revised by the 10 Oct 2026 spec audit under the user's planning-package brief; they are not playtested. The catalog status remains To Be Reworked.

## Starting point

Read the [core specification](081_british_tax_spec_part_1_core.md), then follow the numbered parts. For implementation, start with the [coding-agent prompt](081_british_tax_coding_prompt.md). The [goal prompt](081_british_tax_goal_prompt.md) is ready to copy into a coding runtime and points back to this package.

## Specification parts

| Part | Subject |
|---|---|
| [1](081_british_tax_spec_part_1_core.md) | Catalog identity, experience, country hierarchy, initial assessment, persistence and successors |
| [2](081_british_tax_spec_part_2_economic_system.md) | Industrial and consumer-goods tax, bilateral trade, capacity safeguards, and the fuel and convoy levies |
| [3](081_british_tax_spec_part_3_tax_resistance.md) | Twelve projects, the final settlement, costs, immediate relief, British objections and mission outcomes |
| [4](081_british_tax_spec_part_4_british_response_and_settlements.md) | British administration, exact refusal-goal rule, enforcement, bilateral settlements and worldwide abolition |
| [5](081_british_tax_spec_part_5_evolutions.md) | Delayed active Evolutions, high-Chaos entry, preserved progress and mature Revenue Empire conditions |
| [6](081_british_tax_spec_part_6_country_play_and_connections.md) | Country archetypes, famine remission, and connections to existing national and event systems |
| [7](081_british_tax_spec_part_7_events_and_presentation.md) | Report and news map, native categories, 61 planned image consumers and super-event direction |
| [8](081_british_tax_spec_part_8_ai_and_balance.md) | Acceptance, reform, cancellation, British enforcement and probability scenario targets |
| [9](081_british_tax_spec_part_9_achievements.md) | Eight difficult achievements with eligibility, history, disqualifiers and icon directions |
| [10](081_british_tax_spec_part_10_chaos_and_player_acceptance.md) | Outcome-owned Chaos, reversals, anti-farming guards and player acceptance stories |

## Separate prompts

[Asset production](081_british_tax_asset_prompt.md), [super-event research and production](081_british_tax_super_event_prompt.md), [achievement implementation](081_british_tax_achievement_prompt.md), [decision and mission implementation](081_british_tax_decision_mission_prompt.md), [coding-agent implementation](081_british_tax_coding_prompt.md), and [copyable goal](081_british_tax_goal_prompt.md). [Research notes](081_british_tax_research_notes.md) separate legacy code evidence, engine hypotheses, verified short quotation candidates, and uncleared audio leads. `PACKAGE_MANIFEST.json` lists the current package files and hashes.

## Important preserved rules

British dependencies have no resistance or refusal route until genuinely independent. Independent British-led allies can reduce taxation only to Nominal while ENG leads. Other independents can refuse or cancel, with the exact special-goal rule for every minor and every human-controlled country, but no automatic special goal for an independent AI major.

Britain's benefits come from actual foreign charges. The two trade directions are separate. Capacity is apportioned from the full assessment before applying reform shares, so one surviving tax cannot refill capacity the player just recovered. Reforms deliver immediate domain relief, and later Evolutions preserve completed work.

## Implementation gates

Native independent-country capacity transfers, consumer-goods units and floors, dynamic two-direction bilateral trade, ownership-aware embargo and war-goal cleanup, the fuel and convoy transfers, and current lifecycle hooks need verification before implementation can be called complete. No art has been generated and no recording licensed. No `docs/plans/081_british_tax_plans/` companion exists; implementation records belong there.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- The assessment is now the schedule row plus the British-led-ally adjustment; the industrial-scale band, British relative-strength multiplier, and Chaos-per-100 step were removed as invisible fairy dust, as were the bargaining-position and diplomatic-preparation cost modifiers (Parts 2 and 3).
- Evolution claims reduced to the fuel and idle-convoy levies; the naval-production levy and strategic-resource concession were dropped because they double-charged military capacity and trade access through unproven engine channels (Parts 2, 5, 7, 9, prompts).
- The three intermediate 90-day consolidation missions were removed: a stage advances when its third project completes, and only the final settlement remains as a separate mission. The baseline route drops from about five to about four and a half years (Parts 2, 3, 7 to 10, prompts).
- Added a famine connection: Britain can grant a 180-day consumer-goods remission to a taxpayer with a starving state, a real revenue-versus-goodwill choice (Parts 4, 6, 8).
- Removed archive-era session narration from the README, research notes, and prompts, replaced Codex-specific spawning instructions with the project subagent workflow, and regenerated `PACKAGE_MANIFEST.json`.
