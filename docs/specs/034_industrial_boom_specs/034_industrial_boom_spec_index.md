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

No attributable user or parent acceptance record exists for the design in this package, so its design claims remain `unresolved` under `CLAUDE.md`.
Catalog identity above is user-maintained source data.
Implementation status below is evidence of what exists, not design approval.
The 2026-10-10 audit changes are proposals inside that unresolved design and are listed in the changelog.

## Design in one paragraph

One major or player country receives an extreme, immediate industrial boost and one public value, Overheating, with four bands, a trend and a single leading cause.
A compact decision category lets the country run hot, stabilize supply, hold one reserve, cool down, and build up to three regional projects that can become capped permanent legacy.
The boom ends through a controlled, rough or forced landing, or crashes into Event 35 through a frozen snapshot that already works today.
Three evolutions change the source of power and deepen the inherited depression, and Chaos moves only for concrete abnormal outcomes.

## Implementation status

Checked against the working tree on 2026-10-10.

### Implemented

| Surface | Source | Notes |
| --- | --- | --- |
| Hidden entry `chaosx.nr34.1` | `events/034_industrial_boom.txt` | Random major or player country passing `great_depression_has_viable_economy` and the boom and depression exclusion flags; allocates the episode receipt; joins an active worldwide depression as supplier; seeds snapshot fields; freezes one random industrial state; adds the idea; schedules the visible event and the landing |
| Visible opening `chaosx.nr34.2` and `chaosx.news.39` | same file, `events/_chaosx_news.txt` | Vanilla report picture, interim text |
| Landing `chaosx.nr34.3` and retry `chaosx.nr34.4` | same file | Freezes the snapshot, removes the idea, delivers to Event 35 with bounded retries |
| Event 35 collapse request and region freezer | `common/scripted_effects/034_industrial_boom_collapse_handoff_effects.txt` | Full call contract, evolution-to-profile mapping, one primary region (part 6) |
| Supplier contract adapter | `common/scripted_effects/034_industrial_boom_adapter_effects.txt`, `common/scripted_triggers/034_industrial_boom_adapter_triggers.txt` | Event 35's Offer Boom Supply Contract raises the supplier's Overheating and opens a timed contract (part 7) |
| Tuning | `common/script_constants/034_industrial_boom_constants.txt`, `034_industrial_boom_handoff_constants.txt` | |
| Interim idea | `common/ideas/034_industrial_boom_ideas.txt` | Static `industrial_boom` modifier bundle with `allowed_civil_war = { always = no }` |
| Achievement The Long Fall | `common/achievements/chaos_redux_achievements.txt`, `gfx/achievements/chaos_redux_034_the_long_fall*.dds` | Proof flag set by Event 35 |
| Localisation | `localisation/english/034_industrial_boom_l_english.yml`, `034_industrial_boom_requirement_flags_l_english.yml` | Includes the Event Details line and requirement-flag keys |
| Repeatable registration | `common/scripted_effects/chaosx_logic_effects.txt` | `global.repeatable_events` |
| Event 39 read | `common/scripted_effects/039_murder_mystery_lifecycle_effects.txt` | Reads `industrial_boom_active` |

### Interim behavior that the design replaces

- The boom lasts exactly 180 days (`active_days`) and then always crashes into Event 35; no landing avoids the depression.
- Starting Overheating is 35 plus two per civilian factory, so large economies start at or near 100.
- The idea grants static bonuses including research speed and local resources, with no erosion.
- Evolution is always 0, so every collapse enters Event 35 at baseline and The Long Fall cannot unlock.
- Target selection is unweighted and the inherited region is a random industrial state.
- There is no decision category, project, reserve, incident, AI behavior or permanent event document (`docs/events/034_industrial_boom.md` does not exist).

### Pending

Everything in parts 1 to 5 and 8 to 10 that the table above does not list, the producer side of part 6, and the Event 34 side of part 7.
The [coding prompt](034_industrial_boom_coding_prompt.md) orders the work.

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

Parent acceptance, 2026-10-10 (release orchestrator, under the user's 2026-10-10 brief section 2.2 authority, recorded in the release ledger): every 2026-10-10 audit cut is accepted, cluster 7 (Positive Economy) is confirmed, and automatic refusal of Event 35 supply contracts from 70 Overheating is accepted (items 1, 2 and 4).
These are `accepted and queued` for the Event 034 implementation owner, who also owns the interim always-crash defect in item 3.
Item 5 stays open until the famine and migration owners expose the two triggers.

1. **Cluster assignment.** The original planning pass recorded that the user specified no cluster for Event 34. The current catalog places it in Positive Economy as the Low member. The package now follows the catalog (part 7); confirm that the catalog assignment is the current decision.
2. **Supplier refusal.** The implemented adapter accepts every valid Event 35 supply contract, even in the Dangerous band, where the contract is marked at risk. Proposal: the supplier refuses automatically from 70 Overheating upward, so a contract can never push a boom into Critical. This changes implemented Event 35-facing behavior and needs acceptance.
3. **Interim always-crash.** Until the rework lands, every Industrial Boom ends in a Great Depression after 180 days, and large economies hand Event 35 an Overheating near 100. Proposal: before the full rework, let the stub land without a depression unless the seeded Overheating is in the Critical band, and cap the seed at the part 2 Fragile range. Not applied, because it changes live gameplay outside this document audit.
4. **Audit design changes.** The 2026-10-10 audit removed or merged several drafted mechanics (see the changelog). Because the package had no recorded acceptance, these are proposals; confirm or restore specific items.
5. **Famine and migration seams.** The links in part 7 need a famine-owned state trigger for an active famine stage and a migration-owned trigger for recent local integration in a state. Both owners must expose them before Event 34 can read them.

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
