# Event 34 Industrial Boom specification package

This file is the package README and entry point; `docs/specs/README.md` links here.

## Catalog identity

From the authoritative workbook row (`docs/spreadsheets/chaos_redux_events_catalog.xlsx`):

- Event ID `34`, Industrial Boom.
- Minor Repeatable, Chaos level 1.
- Cluster 7, Positive Economy, as its Low member ([event clusters](../../systems/event_system/event_clusters.md)).
- Status: To Be Reworked.
- No evolution columns are filled yet; the three evolutions in part 5 are added to the row at implementation.
- Direct consequence: Event 35 Great Depression 2.0.

## Acceptance basis

Catalog identity above is user-maintained source data.
The 2026-10-10 audit cuts, cluster 7 (Positive Economy) membership and automatic refusal of Event 35 supply contracts from 70 Overheating were accepted by the release orchestrator under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger.
Parts 1 to 10 are `implemented` in source; the permanent description of what exists is [docs/events/034_industrial_boom.md](../../events/034_industrial_boom.md).

## Design in one paragraph

One major or player country receives an extreme, immediate industrial boost and one public value, Overheating, with four bands, a trend and a single leading cause.
A compact decision category lets the country run hot, stabilize supply, hold one reserve, cool down, and build up to three regional projects that can become capped permanent legacy.
The boom ends through a controlled, rough or forced landing, or crashes into Event 35 through a frozen snapshot that already works today.
Three evolutions change the source of power and deepen the inherited depression, and Chaos moves only for concrete abnormal outcomes.

## Implementation status

Implemented in source on 2026-10-10 as described in [docs/events/034_industrial_boom.md](../../events/034_industrial_boom.md).
The earlier interim behavior (a fixed 180-day boom that always crashed into Event 35, a starting Overheating of 35 plus two per civilian factory, a static idea bundle and an always-zero evolution) is removed.
Recorded limitations: no shock-request adapter exists because no owner submits one, Stabilize Supply Chains always pays trains, band and trend words carry colour without separate texticons, and the Event 35 consumers of the extra region and corridor rows remain Event 35 work.
Validation is source review, local reference checks and MCP `script_validate` with no findings; there is no live-game evidence.

## Files

| File | Owns |
| --- | --- |
| [Part 1](034_industrial_boom_spec_part_1_core.md) | Premise, targeting, opening, lifecycle, outcomes, repeatability |
| [Part 2](034_industrial_boom_spec_part_2_overheating.md) | Overheating, bands, drift drivers, shocks, incidents |
| [Part 3](034_industrial_boom_spec_part_3_decisions_missions.md) | Category budget, costs, actions, missions, cleanup |
| [Part 4](034_industrial_boom_spec_part_4_regions_legacy_repeatability.md) | Regions, projects, protection, control changes, legacy budgets, anti-farming |
| [Part 5](034_industrial_boom_spec_part_5_evolutions.md) | The three evolutions and their entry paths |
| [Part 6](034_industrial_boom_spec_part_6_event_35_inheritance.md) | Event 35 handoff, snapshot fields, region delivery |
| [Part 7](034_industrial_boom_spec_part_7_connections_chaos_cluster.md) | Cross-system connections, Chaos, cluster role |
| [Part 8](034_industrial_boom_spec_part_8_ai_probability_balance.md) | AI profiles, weighted surfaces, balance targets |
| [Part 9](034_industrial_boom_spec_part_9_presentation_assets_text.md) | Presentation choice, header, tooltips, text direction, asset inventory |
| [Part 10](034_industrial_boom_spec_part_10_achievements_acceptance.md) | Achievements, edge cases, acceptance scenarios, completion coverage |
| [Decision map](034_industrial_boom_decision_map.md) | Row visibility by state and band, typical routes |
| [AI and probability matrix](034_industrial_boom_ai_probability_matrix.md) | Named scenarios for every weighted surface |
| [Research notes](034_industrial_boom_research_notes.md) | Historical mechanisms and sources |
| [Coding prompt](034_industrial_boom_coding_prompt.md) | Implementation handoff and work order |
| [Goal prompt](034_industrial_boom_goal_prompt.md) | One-screen implementation goal |
| [Asset prompt](034_industrial_boom_asset_prompt.md) | Asset production handoff |

No plans folder exists for this event; implementation handoffs go to `docs/plans/034_industrial_boom_plans/`.

## Open questions

None open.
Cluster assignment (Positive Economy, Low member), supplier refusal from 70 Overheating, the interim always-crash defect and the audit cuts are resolved by the acceptance above.
The famine and migration seams are `famine_food_stage_requires_mortality` and `migration_state_has_recent_local_integration`.

## Changelog

### 2026-10-10 orchestrator review

- Recorded the parent acceptance of the audit cuts, the cluster 7 assignment, and supplier auto-refusal at 70 Overheating.

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Turned the spec index into the package README with catalog identity, an acceptance-basis statement, a source-checked implementation status (implemented, interim, pending) and a file table.
- Recorded the implemented Event 35 handoff, bounded retry, supplier contract, worldwide-supplier hook, Event 39 read and The Long Fall achievement, which the parts did not mention, and tied part 6 to the real snapshot fields, constants and Event 35 region constants.
- Replaced the stale "unclustered" rule with the catalog's Positive Economy Low membership and defined cluster dispatch behavior; corrected the claim that Event 35 has no cluster.
- Fixed `AGENTS.md` and `.agents/skills` references to `CLAUDE.md` and `.claude/skills`, removed the old picture-versus-meter conflict by choosing one presentation, and fixed research-note references to merged decisions.
- Deleted the decision and mission prompt and the achievement prompt, which restated parts 3 and 10 and contradicted part 10 on two achievements; deleted the package manifest, repository cross-check, source-reading ledger and subagent review, which held August planning hashes, Codex-era source receipts and observations now superseded by the implementation status section (all remain in git history).
- Rewrote the coding, goal and asset prompts as short pointer-based handoffs with the remaining work order instead of restating the spec.
- Reflowed every rewritten file to one sentence per line.

Pass 2, design:

- Overheating: seven bands became four (Sustainable, Strained, Dangerous, Critical), five trend states became three, and three cause lines became one leading cause; eight hidden pressure families became four internal drivers. Fewer visible values, same decisions.
- Lifecycle: the four phases overlapping the bands became three lifecycle states (Opening, Running, Landing), and the five landing bands became four outcomes, with exceptional landing folded into legacy scaling.
- Decisions: about twenty actions and missions became four core actions, three region actions, one evolution action per stage, two missions and one emergency halt, with a hard row budget. Survey, Suspend, separate emergency logistics, separate liquidation, credit restraint as its own row, and the material-flow and consolidation missions were merged or removed as micromanagement.
- Reserves became one held reserve instead of a four-step ladder, and protection became yes or no instead of three levels; both are spent by the shock they absorb.
- Projects: five baseline profiles became three, the four-stage ladder became three stages, and each Miracle form is now an upgrade of a base profile instead of five extra profiles. Evolution III spread uses one entry choice and two state statuses.
- Rough landings no longer arm a hidden later depression trigger; they set Event 35's existing recent-expansion target signal instead.
- Connections: the Event 35 supply contract becomes a real choice by giving the supplier an output opportunity and a one-time landing upgrade; famine, migration (local integration as labor), contamination, camps and Deaths now have explicit, owner-respecting rules.
- Chaos: Speculative Mania no longer adds Chaos, the Runaway milestone list shrank to one source, and reversal is limited to closing recorded sources at a controlled landing.
- Achievements: Every Link Held was dropped and the remaining four were rewritten against the new bands; The Long Fall is recorded as implemented.
- Assets: the meter, phase pictures, project icon family and several state and idea icons were removed in line with the simpler presentation.
