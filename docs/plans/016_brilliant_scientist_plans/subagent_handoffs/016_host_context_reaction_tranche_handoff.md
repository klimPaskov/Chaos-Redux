# Event 016 host-context reaction tranche handoff

Date: 2026-08-01

Status: implemented as a bounded ordinary-report slice; parent-owned live acceptance remains open.

## Scope

The planner addendum `docs/plans/016_brilliant_scientist_plans/016_host_context_reaction_tranche_addendum.md` was implemented without adding a decision category, GUI, focus route, country, evolution, cluster entry, new report art, or 3D package.

| Event | Gate | Resolution |
| --- | --- | --- |
| `chaosx.nr16.7` | First resolved Prototype and a valid primary facility | Civic compact, restricted district, or industrial charter |
| `chaosx.nr16.8` | Second resolved Prototype | Public trust, executive reserve, or patent pool for the snapshotted family |
| `chaosx.nr16.9` | First detected foreign operation resolved after a Prototype | Controlled exchange, private warning, or public accusation |

All three are ordinary dossier reports. They do not advance a project, issue a second project reward, create an evolution, add an event-log row, or change the blank Event 016 cluster field.

## Runtime files and identifiers

- `common/script_constants/016_brilliant_scientist_host_reaction_constants.txt` owns delays, small meter deltas, the restricted-district foreign-operation penalty, foreign-interest increment, AI factors, and opinion values.
- `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt` owns scheduling, once-only resolution, history arrays, transfer copy, terminal cleanup, and nine outcome effects.
- `events/016_brilliant_scientist_host_reaction_events.txt` owns `.7`, `.8`, and `.9` with `ai_chance`, trigger-gated controlled exchange, effect tooltips, and the registered Directorate dossier picture.
- `common/scripted_effects/016_brilliant_scientist_breakthrough_effects.txt` schedules `.7` and `.8` after the existing public or classified report resolvers.
- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` schedules `.9` from the existing foreign-resolution transaction and applies the restricted-district success penalty.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` initializes reaction arrays and flags, copies history during ordinary transfer, applies facility and custody accident pressure, and clears pending reaction state at terminal markers.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt` clears former-host reaction presentation state after Kruger State sovereignty formation while retaining character history.
- `common/scripted_localisation/016_brilliant_scientist_foreign_scripted_localisation.txt` maps the custody family and named foreign operation to existing or new localisation keys.
- `common/opinion_modifiers/016_brilliant_scientist_foreign_opinion_modifiers.txt` defines the three bilateral response modifiers.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` contains event text, effect tooltips, operation labels, and dynamic family wording dependencies.

## Persistence contract

The host owns resolved flags and custody-family history arrays. The fixed `KRG_warren_kruger` character owns matching pending and resolved reaction flags. Ordinary transfer initializes a clean recipient, carries only unresolved facility or custody obligations and the `.8` family snapshot, then clears pending host variables on the old carrier. Resolved facility and custody consequences remain on the old host and physical state; character pending flags are not cleared during the `.7` or `.8` handoff, so the same identity remains the authoritative receipt on the recipient. A pending `.9` is deliberately not transferred. Terminal and confirmed-death cleanup clears host and character pending state but preserves resolved host receipts. Kruger State formation clears the former-host presentation flags and arrays after the character history has been retained.

## Static validation

- Focused `hoi4.event_inspect` lint for `.7`, `.8`, and `.9` returned `status: ok` with `blockingDiagnostics: 0`. The tool reported a workspace-wide partial analysis and linked its large report; this is not a game-load or live-scenario proof.
- New and touched Clausewitz files have balanced braces and no whitespace errors in the Event 016 diff.
- New localisation keys are present, unique, and UTF-8 with BOM.
- Constants referenced by the new effects resolve to existing Event 016 or new host-reaction constant tables.

## Remaining risks and owner

- User-owned live scenarios still need to confirm delayed event-target lifetime across a foreign host response and `foreign_finish_operation`, transfer during a pending `.7` or `.8`, and terminal transition while a reaction is queued.
- The existing workspace contains unrelated dirty Event 006, Fallout, and workbook changes; they must not be included in the Event 016 commit.
- Broader country-specific flavour, bespoke project/news/remnant presentation, quantitative balance evidence, and all seven Event 016 3D route packages remain queued. No models were produced in this tranche.
