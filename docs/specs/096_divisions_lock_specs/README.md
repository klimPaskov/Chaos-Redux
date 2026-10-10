# Event 096: Divisions lock

This package specifies the global native template lock, a live allowance for each country, structural army measurement, optional random demobilization, and four increasingly severe inspection regimes.
It was imported on 8 October 2026 and audited on 10 October 2026; it is a design specification, not an implementation.

| Identity or metadata | Retained planning intent |
| --- | --- |
| Event ID and name | `096`, Divisions lock |
| Type and Chaos level | Minor Repeatable, 1 |
| Existing catalog status | To Be Reworked, according to the parent workbook read |
| Target cluster membership | Peace, cluster `4`, High member; the current workbook does not yet include 096 |
| Canonical event entry | Preserve `chaosx.nr96.1` |
| Source specs | `docs/specs/096_divisions_lock_specs/` |
| Working evidence and handoffs | `docs/plans/096_divisions_lock_plans/` |

## Design map

| File | Retained scope |
| --- | --- |
| [Part 1: core](096_divisions_lock_part_1_core.md) | Player experience, release condition, repeat behavior, country lifecycle |
| [Part 2: allowance](096_divisions_lock_part_2_allowance.md) | Force and capacity formulas, weights, accounting boundaries, examples |
| [Part 3: decisions](096_divisions_lock_part_3_decisions.md) | Two optional actions, random pool, confirmation, execution and cleanup |
| [Part 4: evolutions](096_divisions_lock_part_4_evolutions.md) | Both entry paths, four regimes, fixed review counts and intervals |
| [Part 5: AI and Chaos](096_divisions_lock_part_5_ai_chaos.md) | Sticky posture, score policy, once-per-firing Chaos consequences |
| [Part 6: presentation and achievements](096_divisions_lock_part_6_presentation_achievements.md) | Compact information model, narrative, eight image subjects, three objectives |
| [Part 7: architecture](096_divisions_lock_part_7_architecture.md) | Native gates, current shared-owner evidence, concurrency and migration |
| [Part 8: validation](096_divisions_lock_part_8_validation.md) | Original-brief traceability and specified future acceptance scenarios |

The [coding](096_divisions_lock_coding_prompt.md), [asset](096_divisions_lock_asset_prompt.md), [achievement](096_divisions_lock_achievement_prompt.md), [decision](096_divisions_lock_decision_mission_prompt.md), and [goal](096_divisions_lock_goal_prompt.md) prompts are implementation handoffs.
New labels identify proposed design objects and do not supply final localisation.

## Authority and current workflow

The original brief is not preserved in this package; Part 8 traces its requirements, and the event and evolution names, thresholds, Peace High membership and the two optional removal actions come from it.
The archive's self-reported planning-parent acceptance (IL096-01 through IL096-04) is provenance, not current approval.
The 10 October 2026 changes listed in the revision log are accepted under the user's planning-package brief; the remaining proposals stay unresolved until the parent or user accepts them.
[The import handoff](../../plans/096_divisions_lock_plans/096_import_review_2026-10-08.md) records the import dispositions.

Follow [CLAUDE.md](../../../CLAUDE.md) and the owner skills in `.claude/skills/`: [event planning](../../../.claude/skills/chaos-redux-event-planning/SKILL.md), [events](../../../.claude/skills/chaos-redux-events/SKILL.md), [decisions and missions](../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [event assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), [MTTH](../../../.claude/skills/chaos-redux-mtth/SKILL.md) and [subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md).
Do not allocate a new scenario or tag; evolution/log presentation and achievement identifiers need checks in their own registries.

## Current source and native limits

The current `events/096_divisions_lock.txt` locks countries, sets `division_template_lock_event_active`, and schedules `.3`, which clears the native lock and marker unconditionally after ninety days.
Cannibalism is also a current caller of the native lock; Part 7 lists every owner.

G1 requires exact fielded structure, support, foreign ownership and factory accounting.
G2 requires exact selected refundable demobilization under a retained lock and safe native confirmation receipts.
G3 requires all lock-owner lifecycles, elapsed floor timing, repeats, callbacks, settings, migration and succession.
These capabilities remain unproved.
The documented locked training and ordinary-disband consequences must be checked against the installed build; temporary unlock and silent destruction remain forbidden design substitutions.

## Preserved original receipts

Seven appendices remain byte-identical to the supplied archive: [research](096_divisions_lock_research_evidence.md), [source reading](096_divisions_lock_source_reading_audit.md), [usage map](096_divisions_lock_skill_subagent_usage.md), [review dispositions](096_divisions_lock_improvement_disposition.md), [completion audit](096_divisions_lock_completion_audit.md), [arithmetic](096_divisions_lock_arithmetic_evidence.md), and [manifest](096_divisions_lock_package_manifest.md).
They are original planning receipts: their environment findings, scratch paths, tool availability and hashes describe the archive, not this checkout, and the usage map is a prior run ledger rather than a routing manual.
The arithmetic receipt's checks of peak-excess review budgets and delays, the Evolution II watch baseline and the force-weighted Chaos coverage describe pre-audit rules that the 10 October 2026 audit replaced; its other checks still apply.
None of them proves native counters, refunds, randomness, MTTH, timing, ownership or campaign balance.

## Open questions

- **Proportional extension (resolved).** The hold now ends at compliance or after `7 + ceiling(60 × e)` days from the lock, whichever comes first, where e is the excess at the lock (Part 1, Section 2).
  Disposition: accepted by the orchestrator on 10 October 2026 and promoted into Part 1.
- **Evolution and achievement identifiers.** The evolution/log rows and the three achievement tokens still need their owner-registry collision checks.
- **Catalog row.** The workbook still has a blank cluster for Event 096; Peace High membership and the evolution names wait for the workbook workflow.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Evolutions II-IV use fixed review counts (1, 3, 5), fixed intervals (30, 20, 10 days) and one relock margin each (F above 1.25A, 1.15A, 1.05A); the peak-excess review formula, peak-scaled delays and the Evolution II watch-baseline test are removed, so the next-review time is predictable and no hidden severity state is stored (Parts 4, 7, 8, prompts).
- Chaos accounting is a fixed table: +20 per genuine firing that newly removes editing access, +5 for the first evolved relock and +5 when relocks reach a quarter of participants, -5 for full legitimate restoration, inside the existing 30-per-90-days ceiling; force-weighted quartiles and the lineage-partition machinery for succession are removed (Parts 1, 4, 5, 7, 8).
- The MTTH pacing factor based on entry-force weight now checks whether any major country is in an oversized hold (Part 4).
- Part 2 lists the current Chaos Redux sub-unit families that need explicit weight profiles, gives Livens projectors the heavy-weapon profile and keeps CBRN support companies at the support baseline; Part 4 states how famine, migration, camps, condemnation and fallout reach the event only through live inputs.
- Proposed a finite proportional cap for the brief's extension rule; the orchestrator accepted it the same day, and Part 1 now releases a hold at compliance or after `7 + ceiling(60 × e)` days, whichever comes first, with the latest release day shown to the player.
- Repointed owner links from `.agents/skills/` and `AGENTS.md` to `.claude/skills/` and `CLAUDE.md`, fixed the achievement-icon anchor, removed historical tool-availability narration from Parts 5 and 7, rewrote the goal prompt (3,340 characters), and made the prompts hand live-game validation to the user.
- Reflowed the parts and prompts to one sentence per line; the seven original receipts are unchanged.
