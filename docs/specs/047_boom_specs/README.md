# Event 47: BOOM specification package

## Package identity

- Event ID: `47`
- Event slug: `boom`
- Source specification folder: `docs/specs/047_boom_specs/`
- Working plan folder: `docs/plans/047_boom_plans/`
- Package filename: `047_boom_specs.zip`
- Event type: Minor Repeatable
- Event Chaos level: 1
- Cluster: Various Anomalies (live cluster ID 11, member row 11002, registered as an optional Low member and disabled by default until this rework is implemented)
- Proposed member severity: Severe (see Open questions)

## Design summary

BOOM selects one eligible state and applies an unexplained regional blast.
The camera moves to the first epicenter and a large mushroom-cloud effect appears before the main report.
The blast removes real civilian population, damages existing buildings, disrupts forces inside the affected states, and records exact deaths through the shared Deaths system.
It never calls the nuclear-strike path and never creates a weapon owner, fallout, condemnation, Air Cleanliness pressure, or nuclear history.

Evolution I widens and strengthens the blast.
Evolution II permits two or three distant epicenters during one Event 47 firing.
All states, blast rings, and overlap priorities are frozen before damage begins.
A state touched by several blast zones receives one population transaction and one damage package at the strongest applicable intensity.

The blast hands its aftermath to the shared systems that already own it.
Survivors flee the epicenter through the migration event-pressure adapter, and the wrecked farms, rail, and depots of the epicenter and first ring enter the famine disaster food window.
The player answers the aftermath with the existing Famine and Migration decisions instead of a BOOM-specific layer.

The event introduces no player-facing meter, decision category, investigation, persistent crisis, country package, focus tree, scripted GUI, or super-event.
Every later firing is a new incident and can revisit an earlier state when that state remains eligible.

## Important reconciliations

The planning-source event catalog export described a random province and gave Event 47 no cluster assignment.
The design uses states because population, buildings, adjacency, and Deaths accounting are state-owned.

Various Anomalies is registered in the live cluster runtime at ID 11, and Event 47 already holds member row 11002 there (see `docs/systems/event_system/event_clusters.md`).
The row records its disabled reason until this rework is implemented; implementation enables the existing row and must not create a second membership.

The workbook and live registry label Event 47 as a Low member.
This package recommends Severe because a repeatable incident that can kill most of a state's population, destroy regional infrastructure, and strike several continents does not fit Low.
The event type and Chaos level remain unchanged.

## File index

### Source specifications

- `047_boom_spec_part_1_core.md`
- `047_boom_spec_part_2_evolutions_and_presentation.md`
- `047_boom_spec_part_3_integrations_balance_and_acceptance.md`

### Implementation and specialist handoffs

- `047_boom_asset_prompt.md`
- `047_boom_achievement_prompt.md`
- `047_boom_coding_prompt.md`
- `047_boom_goal_prompt.md`
- `047_boom_localisation_handoff.md`
- `047_boom_probability_audit_prompt.md`
- `047_boom_completion_audit_prompt.md`

### Research and quality evidence

- `047_boom_source_reading_ledger.md`
- `047_boom_acceptance_matrix.md`

### Working plans and reconciliation notes

- [047_boom_catalog_reconciliation.md](../../plans/047_boom_plans/047_boom_catalog_reconciliation.md)
- [047_boom_parent_improvement_review.md](../../plans/047_boom_plans/047_boom_parent_improvement_review.md)
- [047_boom_process_blockers.md](../../plans/047_boom_plans/047_boom_process_blockers.md)

## Status and evidence boundary

The package's acceptance language records requested design direction, but the package contains no attributable user or parent acceptance record, so those acceptance claims remain `unresolved` until an explicit basis is recorded.

The runtime slot `events/047_boom.txt` still holds the legacy single-event stub; no part of this package is implemented.
The tool-availability statements in `047_boom_source_reading_ledger.md` describe the original package-generation session only.

## Open questions

- Member severity: the live registry and workbook say Low, this package recommends Severe.
  The workbook is the authoritative catalog, so the change needs a user decision before the catalog row and the cluster row 11002 are edited.
- Direct-hit response choice (proposal, not part of the accepted scope): the parent review deliberately keeps BOOM free of a management layer.
  A single direct-hit option pair could still give the victim one meaningful answer: pay political power for an organized evacuation of the epicenter's survivors through `migration_request_organized_evacuation`, or keep them in place and accept the famine window at full strength.
  It is left out until the user decides whether BOOM should offer any choice at all.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Replaced the stale "Various Anomalies has no stable ID, cluster wiring blocked" rule everywhere with the live registration (cluster 11, row 11002, disabled until rework).
- Moved the severity conflict into Open questions instead of treating Severe as settled.
- Replaced `AGENTS.md` references with `CLAUDE.md`, trimmed the goal prompt to a pointer at the coding prompt, and reduced the completion-audit checklist and the part 3 acceptance list to pointers at the acceptance matrix, which owns the scenarios.
- Recorded that the runtime slot is still the legacy stub and that tool-availability notes are historical, and removed the obsolete ZIP extraction instructions.
- Clarified the Evolution II pacing factor that could never be false before Evolution II existed.

Pass 2, design improvement:
- Gave the blast real aftermath through existing adapters: survivor flight from the epicenter via `migration_request_event_pressure` and a disaster food window for the epicenter and first ring via `famine_request_disaster_pressure`.
  Before, the spec only hoped ordinary famine and migration would notice the damage, which neither system does without an explicit owner request.
- Kept every adapter request free of a second population debit and free of new player-facing values; the player responds through the existing Famine and Migration categories.
- Recorded a direct-hit choice as a proposal only, because the accepted direction excludes a BOOM management layer.
