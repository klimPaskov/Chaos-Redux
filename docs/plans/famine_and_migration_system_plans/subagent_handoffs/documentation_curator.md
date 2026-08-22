# Documentation Curator Handoff

Status: Documentation reconciliation is complete for the current source snapshot, with gameplay, localisation, assets, spreadsheets, and unrelated implementation files left outside this worker's write scope.

No gameplay completion claim is made.

## Files changed

- `common/scripted_effects/chaosx_dynamic_effects.md` now documents `famine_migration_refresh_decision_phase_from_state`, `famine_migration_retire_inactive_displacement_country`, trapped-population normalized pressure, the narrower dormant-ledger cleanup contract, and the bounded CXT fixture.
- `docs/systems/famine_and_migration_system.md` is the permanent shared-system ledger covering formulas, exact transfer and Deaths ownership, sparse registries/jobs, lifecycle reveal and retirement, decisions, adapters, all 15 historical profiles, exactly two dedicated mapmodes, eight achievements, assets, Event 149, CXT, MCP evidence, and blockers.
- `docs/systems/state_map_modes.md` now distinguishes stage-driven famine colors from score tooltips, documents state-local migration projections and exact mapmode count, and records current map/GUI evidence limits.
- `docs/plans/famine_and_migration_system_plans/source_of_truth_map.md` records authority order, canonical implementation paths, surface status, exact mapmode/profile inventories, evidence artifacts, and future-edit rules.
- `docs/plans/famine_and_migration_system_plans/handoff_dispositions.md` now records explicit current dispositions for every completed handoff and the exact decision-file MCP lint timeout.
- `docs/assets/famine_and_migration_system/gfx_handoff.md` now records the completed Deaths texticons and current inline localisation consumers.
- `docs/assets/famine_and_migration_system/manifest.csv`, `docs/assets/famine_and_migration_system/mapmode/manifest.csv`, `docs/assets/famine_and_migration_system/category_picture/manifest.md`, and `docs/assets/famine_and_migration_system/report_art/manifest.md` now reflect current source registration and completed asset-package status while retaining runtime-consumer gates.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_artist.md` now records current Deaths texticon localisation wiring while retaining the original 44-row icon-package validation evidence.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/generated_event_art.md` and `mapmode_icon_artist.md` now distinguish current GFX registration from remaining report/visual runtime validation.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/documentation_curator.md` is this handoff.
- `docs/plans/famine_and_migration_system_plans/resume_packet.md` is the concise parent resume packet for the remaining blockers.

## Dispositions

The current disposition table in `handoff_dispositions.md` covers repository exploration, the pre-change AI baseline, map inspection/validation, decision-mission audit, generated art, icon and achievement art, localisation audit, mapmode icon art, mapmode repository exploration, scripted-system architecture, and skill maintenance.

Accepted source work includes the bounded registries, formulas, exact transfer conservation, decision and mission declarations, 15-profile matrix, eight achievement IDs, asset provenance, localisation key audit, and reusable state-ledger skill.

Modified historical findings include the pre-change weighted baseline, stale “contracts absent” exploration notes, stale mapmode setter concerns, stale third-country regular-bind concern, stale parent-wiring notes, and obsolete Deaths-icon absence.

Queued work includes the 20-scenario probability inspect/compare, owner-local cross-system adapters, report-event consumers, achievement disqualifier/lifecycle audit, supported mapmode GUI/render evidence, food-reserve representation, unrelated map locator diagnostics, and parent runtime checks.

Rejected interpretations are the invention of a replacement Event 149, a third famine or migration mapmode, fabricated catalog-only event sources, and the obsolete claim that Deaths reason texticons should remain absent.

No handoff was deleted or silently treated as gameplay approval.

## Source-of-truth reconciliation

The source spec folder remains the accepted design authority, the scripted effects remain implementation evidence, the ordinary decision files own category/mission/decision presentation, and the mapmode source owns exactly `famine_state_map_mode` and `migration_state_map_mode`.

The public helper reference and permanent system ledger now agree that the category is hidden at campaign start and emerges only from sustained or large food, incident, flight, trapped, or reception thresholds.

The public helper reference and permanent system ledger now agree that dormant scheduler retirement removes only transient country registration state and preserves integrated, resettled, and returned historical ledgers.

The public helper reference, permanent ledger, and mapmode documentation now agree that trapped population contributes normalized pressure to both need and vulnerability, and that migration mapmode state projections do not represent persistent route geometry.

The public helper reference and permanent system ledger now agree that short destination credit restores the uncredited residual to origin, removes incidental owner/controller manpower gains, recomputes the debit equation, and requires positive debit with zero residual.

The permanent system ledger now records that ideology is a bounded AI modifier only after valid policy, destination, and route gates pass, and that persecution, famine, bombing, camps, occupation conduct, and contamination override affinity without authorizing unsafe routes.

The Deaths asset and localisation documents now agree that `fm_deaths_famine` and `fm_deaths_displacement` are delivered 18x18 BGRA8 one-mip texticons, registered in `interface/chaosx_texticons.gfx`, and consumed by the current cause localisation.

## Contradictions resolved

| File or handoff | Earlier claim | Current resolution |
| --- | --- | --- |
| `docs/plans/famine_and_migration_system_plans/ai_probability_baseline.md` | Shared weighted surfaces were absent. | Retained as a pre-change baseline; current weighted balance remains unproven because the post-change 20-scenario evaluation timed out. |
| `docs/plans/famine_and_migration_system_plans/repo_exploration.md` | Shared contracts and Event 149 design were still open. | Contracts and retirement policy are accepted in the current source/spec; Event 149 remains absent and absorbed without a replacement ID. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/mapmode_repo_explorer.md` | Reception, overcrowding, and return setters were not found. | Current source contains reception-context refresh plus resettlement and return projection setters. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/decision_mission_audit.md` and `localisation_auditor.md` | Safe third-country resettlement risk involved a regular bind after exact movement. | Current decisions call the safe resettlement rebind contract; parent runtime validation remains required. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_artist.md` | Deaths reason texticons were not a live asset surface. | The two texticons are now delivered, registered, and consumed by cause localisation. |
| `docs/assets/famine_and_migration_system/gfx_handoff.md` | Deaths texticon localisation wiring was pending. | Current localisation contains both inline texticons and retains the UTF-8 BOM. |
| `docs/systems/state_map_modes.md` | Famine score and stage could be read as one visual distinction. | Stage drives map color; score remains an authorized tooltip ledger. |
| `docs/spreadsheets/chaos_redux_events_catalog.csv:311` | Event 149 was described as a random major-country migration drain. | The exported row now says it is retired and absorbed into the shared dynamic famine and migration system and remains unavailable as a random event. |

## Duplicates and superseded documents

No documentation file was deleted.

`docs/systems/famine_and_migration_system.md` is the permanent system ledger, while `common/scripted_effects/chaosx_dynamic_effects.md` remains the reusable helper-contract reference and `docs/systems/state_map_modes.md` remains the mapmode presentation reference.

`ai_probability_baseline.md` is retained as historical pre-change evidence rather than a duplicate current audit.

The historical sections of `handoff_dispositions.md` and individual handoffs remain for provenance, while its curator reconciliation table is the current disposition authority.

The obsolete Deaths-icon absence interpretation, stale mapmode no-setter statement, stale regular-bind risk, and stale parent-wiring statements are superseded by current source evidence and are not treated as active requirements.

## Stale prompts and instructions

The named documentation-curator prompt remains current and still correctly forbids gameplay, localisation, asset, spreadsheet, and broad source edits.

No stale prompt file required editing in this pass.

The stale instructions that could cause duplicate work are historical handoff statements listed in the contradiction table, especially the pre-change probability baseline, the mapmode no-setter note, the old regular-bind risk, and the obsolete Deaths-icon absence note.

## Markdown hard-wrap audit

The targeted hard-wrap audit found no accidental mid-sentence or mid-clause candidates in the seven patched Markdown surfaces.

The same audit covered all 35 Markdown files under `docs/specs/famine_and_migration_system_specs` and found zero candidates.

The same audit covered all 13 Markdown files under `docs/plans/famine_and_migration_system_plans` and found zero candidates.

Headings, lists, tables, block quotes, and fenced code blocks were excluded from the candidate check and preserved.

No Markdown hard-wrap correction was required beyond keeping new prose sentences on one physical line.

## Evidence and validation

- `rg` confirms the eight achievement definitions remain present in `common/achievements/chaos_redux_achievements.txt`.
- A current manifest count reports 46 rows: one category icon, nine state modifier icons, ten decision icons, 24 achievement variants, and two Deaths reason texticons.
- `rg` confirms the two dedicated mapmode identifiers in the current mapmode source and interface files, with no third famine/migration mapmode added.
- The current bounded `hoi4.map_inspect` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34498d56d4bf765796f793b12431c8e42bf07506d9484b1c7f3a961900f58b1d/66c0aca0d881147df54e388a8d987bf4f8422ed0c1b6fa779fc8ea008ddb3eb0/map-inspect.456c28c5a8e6bad1.json`; it passed requested state/geometry checks but retained unrelated `map/buildings.txt` locator diagnostics.
- The required decision-file `hoi4.event_inspect` lint request with file selector `common/decisions/famine_migration_decisions.txt`, helper expansion, `maxNodes = 800`, `maxEdges = 1600`, and workspace `chaos_redux` was accepted but timed out at 180 seconds without diagnostics.
- The current mapmode GUI route modeled zero hardcoded `mapmodes` elements and timed out on render, so source/GFX evidence is not claimed as a complete visual runtime gate.
- The post-change 20-scenario probability evaluation timed out, and no completed before/after probability compare is claimed.
- Read-only `rg` checks confirm the new helper names, exact mapmode names, achievement IDs, CXT token, death texticons, and reconciled Event 149 catalog wording.
- Read-only source checks confirm `famine_migration_restore_origin_population_residual` is called by the exact transfer path and that the transfer recomputes debit, survivor credit, route deaths, and residual before accepting the result.
- Source review confirms decision AI modifiers are bounded on valid policy choices while route, destination, persecution, famine, bombing, camps, occupation-conduct, and contamination checks remain gate-level blockers.

## Skipped validation

No game launch, live save, in-game mapmode, CXT, achievement-unlock, or runtime population transaction validation was run because those checks are parent/user-owned and this worker is documentation-only.

No workbook or CSV export validation was run because the event catalog workbook and its exports belong to the spreadsheet worker.

No new weighted-logic MCP run was initiated in this pass because the existing post-change handoff already records the exact 180-second 20-scenario timeout and no stable scenario compare inputs were available.

## Remaining risks for parent review

The current source contains the documented helper contracts and decision wiring, but source presence is not equivalent to gameplay completion.

Food-reserve representation remains a design choice because current decisions use bounded relief/pressure inputs rather than a distinct reserve stockpile.

Owner-local pressure and direct-death adapters remain API-only where no authoritative caller was identified.

Report assets and labels are present, but the compatible existing report-picture carrier and shared report/event registry consumer are not identified in the current source snapshot.

The carrier conflict must be resolved without allocating a replacement Event 149 ID or random-event pool entry.

Achievement IDs, predicates, localisation, and assets are present, but disqualifier producers and lifecycle-proof coverage remain under the active achievement audit and are not promoted to completion.

The mapmode GUI/render route and the decision-file event lint route remain engine-evidence blockers.

The unrelated `map/buildings.txt` locator diagnostics remain outside this documentation scope.

## Proposed cleanup if a future documentation patch is blocked

If the shared helper reference cannot be patched safely because of a concurrent edit, the parent should append the two lifecycle-helper contracts, trapped normalization, and CXT fixture note without rewriting neighboring sections.

If a future workbook export diverges from the reconciled Event 149 retirement wording, the spreadsheet owner should restore the unavailable status and retirement note without adding a replacement event ID.

If an engine artifact remains unavailable, retain the exact MCP request, timeout, and artifact limitation in the handoff rather than promoting source-only checks to engine evidence.
