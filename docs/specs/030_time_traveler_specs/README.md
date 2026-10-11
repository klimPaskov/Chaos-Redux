# Event 030 Time Traveler Source Specification

This package expands Event 030, Time Traveler, into a complete major-event design.
One verified traveler starts a contest over future knowledge.
Later evolutions bring a political struggle around the traveler, returned figures from the past, visitors from later eras, material temporal incidents, a war of temporal stances, and the Machine Extinction War.

Workflow owners: [event integration](../../../.claude/skills/chaos-redux-events/SKILL.md), [event planning](../../../.claude/skills/chaos-redux-event-planning/SKILL.md), [subagent routing](../../../.claude/skills/chaos-redux-subagents/SKILL.md), and [asset production](../../../.claude/skills/chaos-redux-event-assets/SKILL.md).
Names marked as working labels are structural and get final localisation after research.

## Event identity

- Event ID: `30`
- Entry event: `chaosx.nr30.1`
- Classification: Major
- Chaos level: `1`, Calm World
- Cluster: none
- Public values: Credibility, Exposure, and Timeline Divergence, with Temporal Stability shown in place of Divergence during Evolution V
- Evolution I threshold: Gathering Storm, `200+` Chaos
- Evolution II threshold: Rising Chaos, `400+` Chaos
- Evolution III threshold: Chaos Tier, `600+` Chaos
- Evolution IV threshold: Totalen Chaos, `800+` Chaos
- Evolution V threshold: World Collapse, `1000+` Chaos
- Public world-end branch: Machine Extinction War
- Triggerable scenario: All Times at Once, reserved `SCN-020`, raw triggerable ID `20`, in the [shared identifier registry](../shared_identifier_registry.md)

## Status and acceptance

The package is implementation-ready as a design, but its expanded design is not yet accepted.
Each part opens with its acceptance status.

| Claim | Basis | Disposition |
| --- | --- | --- |
| `SCN-020`, raw ID `20`, for All Times at Once | user allocation instruction of 7 October 2026, recorded in the shared identifier registry | accepted identifier only, recheck runtime and workbook occupancy before integration |
| the three public value names and Temporal Stability in Evolution V | the user's Event 030 brief, listed in the [planning receipt](research/source_reading_manifest.md) | user-brief requirement |
| the nine historical figures and the three named future visitors | the user's Event 030 brief | user-brief requirement |
| prehistoric animals with Africa as a prominent region | the user's Event 030 brief | user-brief requirement |
| a traveler who warns governments away from lost wars, Napoleon's return, and a robot invasion from the future | the legacy catalog row and the user's brief | user-brief requirement |
| Parts 1, 2 and 3: baseline custody, three public values with three bands, four access arrangements, six consultation families, four countermeasures, four rival operations, institutional spirit stages, remembered war variants for Germany and the United States, durable outcomes | release-pass parent decision of 2026-10-11 | Accepted by parent 2026-10-11 |
| Evolution I and Evolution II designs (Parts 4 and 5), Evolution II restricted to Napoleon Bonaparte, Joan of Arc and Frederick the Great (open question 2) | release-pass parent decision of 2026-10-11 | Accepted by parent 2026-10-11 |
| open question 1: keep the label Timeline Divergence throughout and name the Evolution V band Collapsing | release-pass parent decision of 2026-10-11 | Accepted by parent 2026-10-11 |
| Evolutions III to V, the Closed Future country, the modern named visitors (open question 3), the Machine Extinction War, All Times at Once and the remaining figures of Part 5 | release-pass parent decision of 2026-10-11 | Deferred to a later pass. The modern visitors are living public figures and stay out until the user confirms the names |
| everything else in the twelve parts and matrices | planning-session proposal and the 2026-10-10 audit | `unresolved` until the parent or user records acceptance |

Implementation does not start on an `unresolved` or deferred part until acceptance is recorded here or in `docs/plans/030_time_traveler_plans/`.
The release pass of 2026-10-11 implemented the accepted parts. The record is `docs/events/030_time_traveler.md` and `docs/plans/030_time_traveler_plans/subagent_handoffs/030_release_pass_2026-10-11.md`.

## Implementation status

The runtime is a short legacy chain that predates this design.

| Runtime surface | Current behavior | Disposition |
| --- | --- | --- |
| `chaosx.nr30.1` hidden entry | resolves a host through `time_traveler_select_weighted_prefire_host`, using the individual-crisis ticket weight over every existing country, then reserves it with `time_traveler_prefire_pending` | retained, host pool and exclusions pending (Part 1) |
| `time_traveler_prepare_random_event_fire` | defined but not called, because the entry event selects its own host | retained helper, wire or remove during implementation |
| `chaosx.nr30.2` report and `chaosx.news.33` | grants the timed `time_traveler` idea for 365 days | superseded by verification, arrangements, and the staged spirit (Parts 1 and 2) |
| `time_traveler` idea | `+20%` research speed, `+100%` planning speed, `+50%` offence, `+20%` army experience, and AI factors | superseded, far above the spirit strength anchor in Part 2 |
| `chaosx.nr30.3` to `chaosx.nr30.6` and `chaosx.news.34` | Germany may propose a Berlin-Moscow Axis to the Soviet Union regardless of who hosts the traveler | superseded by the remembered war variant of the diplomatic forecast (Part 3) |
| `chaosx.nr30.7` and `chaosx.news.35` | the United States gains intelligence on Japan regardless of who hosts the traveler | superseded by the remembered war variant of the diplomatic forecast (Part 3) |
| Event 016 contact bridge | `brilliant_scientist_try_schedule_time_traveler_contact` and the Temporal Theory gate read `has_idea = time_traveler` | retained, must survive the idea's retirement (Part 10) |
| individual-crisis provider | counts the prefire flag or the timed idea | retained, provider moves to the custody marker (Part 10) |
| legacy localisation | includes option text that breaks the event writing style | superseded |

Everything else in the package is pending.
There is no `docs/plans/030_time_traveler_plans/` folder and no `docs/events/030_time_traveler/` overview yet.

## Central design decisions

The event uses one original fictional traveler with a knowledge profile.
Foreign countries compete for the traveler and copied knowledge through a hidden network level, and the traveler can change custody, defect, disappear, or die.
Copied knowledge survives loss through a weaker legacy spirit, and Timeline Divergence survives the traveler.

The player tracks three values with three bands each.
The bands decide what the player can do: Credibility sets the consultation tier, Exposure sets which rival operations exist, and Divergence sets forecast precision and how fast later evolutions arrive.
Every other score stays internal.

The custodian uses one decision category, a static category picture, and a compact three-value header.
Four access arrangements, six consultation families, four countermeasures, and four rival operations make up the baseline action set.
No separate mechanic window is required.

Returned people remain characters, movements, claimants, commanders, or advisors inside existing countries.
Only the Closed Future becomes a new country package, because only it holds territory, runs an economy, and fights a long war.
Its ground force reuses the shared autonomous robot family, so the only new model is a drone aircraft.

Event 030 connects to shared systems only through their owners: Deaths, migration, famine, camps, biological outbreaks, condemnation, Air Cleanliness, world threat, individual-crisis targeting, and the Event 016 and Event 027 APIs.

## Package map

- `specs/` contains the twelve source specification parts, and [Part 12](specs/030_time_traveler_spec_part_12_acceptance_criteria.md) owns completion criteria.
- `matrices/` contains compact maps that point back to their owning parts.
- `focus_graphs/` contains Mermaid diagrams for escalation, ambition, and the Closed Future tree.
- `research/` contains historical research, research-to-design links, and the planning-session receipt.
- `prompts/` contains bounded implementation and audit prompts that point to the parts instead of restating them.
- `quality/` contains the acceptance traceability matrix, the anti-bloat audit that owns the design limits, and the original manual improvement review.
- `030_time_traveler_full_spec.md` links the twelve parts in order.
- `PACKAGE_MANIFEST.md` records byte counts, line counts, and SHA-256 hashes.

## Open questions

These proposals conflict with recorded user-brief requirements or need a user or parent decision, so the specification does not adopt them.

1. Temporal Stability label.
   The brief asks for Temporal Stability in Evolution V, which inverts the third number mid-campaign, so a rising value suddenly means improvement.
   Proposal: keep Timeline Divergence as the label throughout and use Collapsing as the Evolution V band name, which removes one conversion tooltip and one label set.
2. Historical figure tranches.
   The brief names nine figures, and each needs research, a sourced portrait, routes, AI, and cleanup.
   Proposal: ship the shared scaffold with Napoleon, Joan of Arc, and Frederick the Great first, because they share European hosts and test both the commander and the symbol routes, then add the other six in later tranches, each reported as pending until done.
3. Named modern visitors.
   The brief names Donald Trump, Vladimir Putin, and Xi Jinping.
   Proposal: confirm the names before research starts, because these are living public figures whose portrayal needs the most careful neutral handling in the package.
4. Closed Future ground model.
   Foundry Frames now reuse the shared robot model.
   Decision needed: whether the machine invasion deserves a distinct ground silhouette, which would add one 3D package.
5. Design acceptance.
   Decision needed: which parts the user or parent accepts for implementation, recorded in the Status table above.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:

- Recorded the acceptance basis for each claim, separating the user's `SCN-020` allocation and user-brief requirements from unresolved proposals, and added an acceptance line to every part.
- Reconciled the package with the legacy runtime: documented what the current `events/030_time_traveler.txt`, idea, helpers, and Event 016 bridge do, which parts are retained, and which are superseded.
- Corrected the host pool to match the individual-crisis targeting layer and moved the crisis slot to the custody marker.
- Replaced stale famine wording that relied on the removed famine incident events with the current famine adapter request contract, and aligned migration, Deaths, condemnation, and world-threat wording with their owner docs.
- Fixed integration names: Event 032 is Missiles and Event 039 is Murder Mystery.
- Replaced `.agents/skills` links, `AGENTS.md` references, and Codex, Qoder, and Cursor spawning rules with `.claude/skills`, `CLAUDE.md`, and the Claude Code Agent tool.
- Aligned tool-evidence rules with `CLAUDE.md`: an unavailable MCP route is a recorded limitation, not a completion blocker.
- Trimmed the coding, goal, decision, asset, achievement, and audit prompts to pointers at the owning parts, and made Part 12 the single owner of completion criteria.
- Merged `quality/package_status.md`, `quality/package_validation.md`, `quality/tooling_limitations.md`, and `research/repo_inspection_notes.md` into `research/source_reading_manifest.md`, because all four repeated the same historical limits.
- Relabelled unattributed "accepted" claims in the manual improvement review as proposals and moved the design limits to the anti-bloat audit.

Pass 2, design improvement:

- Reduced each public value from five bands to three and tied each band to one decision, so the header shows three numbers, three band names, and short cause lists instead of fifteen stage labels.
- Made Divergence an MTTH factor for Evolutions II to V instead of an undefined hard gate, so restraint slows temporal collapse without locking content.
- Merged the six access arrangements into four, because Military and Scientific access duplicated the knowledge profile and Restrict Access duplicated arrangement revision.
- Merged seven rival operations into four with a hidden network ladder, and six countermeasures into four, which removes repetitive decisions while keeping escalation.
- Collapsed five consultation result classes into success, partial, and failed with a named cause.
- Kept the legacy premise of warning governments away from lost wars as country-specific remembered war forecasts for Germany and the United States, delivered to the custodian or through shared forecasts.
- Set a strength anchor for the institutional spirit far below the legacy idea's bonuses.
- Replaced six hidden support sectors with three blocs seeded by the access arrangement.
- Connected preventive detention to the existing camp custody intake and Kruger's temporal deployment to Timeline Divergence.
- Turned generic future visitors into four fictional single-role specialist categories without movement packages.
- Merged unrealized-timeline objects into a timeline rift family and gave every incident exactly three actions.
- Reduced Evolution V to four stances with two signature actions each plus three shared node actions, and turned alternate-state delegations into a fracture incident.
- Reused the shared autonomous robot family for Foundry Frames, folded siege groups into its refinements, replaced the Automated Foundry building model with a state modifier, and left the drone as the only new model.
- Added the temporal incident and machine extermination Deaths reasons and the Closed Future world-threat source flag.
- Removed The Last Archive achievement, which needed an archive ledger that no other mechanic used, and aligned the remaining thresholds with the value bands.
