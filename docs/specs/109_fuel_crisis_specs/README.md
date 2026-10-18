# Event 109: Fuel Crisis planning package

## The design in one paragraph

Fuel Crisis removes every existing country's national stored fuel in one event resolution. Oil resources, refineries, imports, fuel capacity, and ordinary production continue functioning. Countries respond through normal operational restraint, oil access, delivery protection, construction, and diplomacy. Event 101 can draw an active, feasible reserve or delivered-oil challenge from a selected player's recovery. One native news announcement, a shared-log scene, and a difficult Tasks-dependent achievement complete the presentation and challenge design. There are no evolutions.

## Identity and destination

| Field | Value |
| --- | --- |
| Event | 109 Fuel Crisis |
| Original catalog ID | 114 |
| Slug | fuel_crisis |
| Type | Minor Fire-Once |
| Status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Unassigned |
| Package | 109_fuel_crisis_planning_package.zip |
| ZIP root | 109_fuel_crisis_specs/ |
| Intended repository destination | docs/specs/109_fuel_crisis_specs/ |

Extract the ZIP's single top-level folder into the repository's `docs/specs/` directory. The package contains planning documents and future execution prompts. Extracting it does not install gameplay or change a catalog row.

## Read the specification in order

| File | Purpose |
| --- | --- |
| [Part 1: core](109_fuel_crisis_spec_part_1_core.md) | Exact world change, acknowledgment, strategic identity, one-time Chaos impact, and ordinary aftermath |
| [Part 2: recovery](109_fuel_crisis_spec_part_2_recovery.md) | Land, air, naval, and reserve priorities, real opportunity costs, supply responses, country patterns, and native AI expectations |
| [Part 3: Tasks](109_fuel_crisis_spec_part_3_tasks.md) | Player-only admission, the two objective alternatives, measurable actions, frozen targets, dynamic deadlines, observed holds, outcomes, and cleanup |
| [Part 4: presentation and achievement](109_fuel_crisis_spec_part_4_presentation_and_achievement.md) | Direction-only localisation, news and report scene production, shared consumer requirements, and the complete achievement contract |
| [Part 5: acceptance](109_fuel_crisis_spec_part_5_acceptance.md) | Experience goals, campaign and task boundary scenarios, selection review, compatibility, performance, and completion evidence |

The five parts are the canonical design. The [implementation handoff](109_fuel_crisis_implementation_handoff.md) separates technical ownership, native verification, occurrence receipts, integration details, source evidence, and the Subagent Usage and MCP Usage maps from the readable game specification.

## Future execution prompts

These prompts were written after the full specification. They direct later authorized implementation and production. They do not claim that work has happened.

| File | Assignment |
| --- | --- |
| [Coding prompt](109_fuel_crisis_coding_prompt.md) | Full implementation, dependency gates, ownership, validation, and completion report |
| [Decision and mission prompt](109_fuel_crisis_decision_mission_prompt.md) | Event 101 integration and the two Fuel Crisis contracts |
| [Asset prompt](109_fuel_crisis_asset_prompt.md) | Generated depot scene, separate report and news processing, achievement icon states, provenance, and consumer evidence |
| [Achievement prompt](109_fuel_crisis_achievement_prompt.md) | Registry, eligibility, demanding unlock, minimal tracking, icon wiring, and validation |
| [Goal prompt](109_fuel_crisis_goal_prompt.md) | Compact implementation goal with the central pass or fail requirements and pointers to the complete files |

Working labels in these files identify design roles. They are not final localisation. The implementation and localisation owners must write final text from the specified meaning after the mechanics and consumers are verified.

## Evidence and review

| File | What it records |
| --- | --- |
| [Evidence and decisions](109_fuel_crisis_evidence_and_decisions.md) | Source coverage, prior Tasks brief, pinned repository observations, conflicting sources, parent design choices, and unverified claims |
| [Source inventory](109_fuel_crisis_source_inventory.csv) | Every distinct supplied text version, its hash, occurrences, reading owner, and complete-reading method |
| [Reading receipts](109_fuel_crisis_reading_receipts.json) | Original reader records and the combined supplied-source gate |
| [Repository evidence](109_fuel_crisis_repository_evidence.json) | Targeted retrieved-source identities, source hashes, directory inventories, and bounded identity searches |
| [Review and validation](109_fuel_crisis_review_and_validation.md) | Specialist review dispositions, mandatory improvement-loop result, arithmetic checks, package checks, and remaining implementation gates |
| [Package manifest](109_fuel_crisis_package_manifest.json) | Final file identities and checksums for the delivered package |

The supplied-source gate covered 90 distinct text versions across 132 text occurrences, including all catalog rows and current and earlier skill and role material. Three supplied archives and two nested archives were completely inventoried and verified. No supplied text remained unread by the team, and clipped outputs were not counted as complete reading.

Reading was collective. Current distinct text was read in complete bounded outputs. Exact duplicate copies were checked by hash and byte comparison. Older revisions were processed by matching all repeated text to an already fully read version, reading every changed passage, and reconstructing the original bytes exactly. The evidence record explains this method so that it is not confused with one agent literally rereading every duplicate file.

Repository research was narrower. It used relevant files and sections around commit `a3ef485c5da7e2337122eca04ac65c175050f251`, dated 6 October 2026. It was not a full read of the repository, all branches, or the installed game. The separately located prior Tasks brief was read in full and identified in the receipts.

## Design authority and tuning

The user supplied the current event identity, exact worldwide reserve loss, intact upstream economy, ordinary recovery, no evolutions, and Tasks connection. The source catalog snapshot has 109 as Custom laws, 114 as Fuel crisis, and older availability labels. Those historical rows do not override the current brief. Their disposition must be reconciled in the actual checkout and editable workbook before implementation writes.

The editable catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. The fully read `chaos_redux_events_catalog.csv` is an export snapshot. No workbook or CSV content was changed by this planning task.

The Chaos bands, scaled reserve and delivery targets, 90 to 180 day task duration range, observed holds, image composition, and difficult achievement are parent-authored planning choices under the request to expand the idea. They are proposed starting design and tuning. They are not attributed to existing gameplay or separate explicit user approval.

Earlier specialist alternatives were reconciled into the canonical parts. In particular, the universal 180-day task, later 365-day ceiling, and conservation-only reserve route were superseded. Use Part 3's final formulas and alternative action routes.

## Remaining implementation evidence

The native direct setter has repository precedent and offline documentation support. Its installed behavior, precision, country scope, execution order, and save boundaries still require verification.

Event 101's actual runtime interface, useful pre-wipe fuel-demand measurement, real delivered-oil measurement, conversion units, and native timer behavior were not verified. Each Tasks route and the Tasks-dependent achievement remains an implementation dependency until those requirements are met. The core wipe is independently specified, and partial implementation must be reported honestly.

HOI4 MCP tools and an installed game environment were unavailable in this session. No gameplay source, live workbook, final localisation, or runtime asset was produced. No HOI4 process was launched. The package defines the required source, native, MCP, visual, and later user-run game evidence without presenting the plan as a tested implementation.
