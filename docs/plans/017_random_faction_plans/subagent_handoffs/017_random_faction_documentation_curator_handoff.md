# Event 017 Random Faction documentation curator handoff

- Date: 2026-07-10
- Agent: `chaosx_documentation_curator`
- Mode: documentation-only patching
- Commit: not created, as directed by the parent
- Source specs: reviewed and left unchanged

## Scope completed

The Event 017 documentation now describes the implemented system rather than the retired placeholder or earlier planning assumptions. The review covered the complete Event 017 spec package, research notes, matrices, prompts, implementation scripts, shared event-system integrations, English localisation, asset records, all Event 017 plans, and the available audit, asset, and spreadsheet handoffs.

The required offline Paradox wiki pages and relevant vanilla documentation were also consulted for event targets, variables and arrays, decisions and missions, scripted GUI data flow, event logging, AI, achievements, frame animation, and lifecycle behavior.

## Documentation files changed

| File | Disposition |
| --- | --- |
| `docs/events/017_random_faction/overview.md` | Rewritten as the canonical implementation record. It covers automatic dynamic minor selection, the shared human and AI saved targets, baseline and all evolutions, Bloc Pressure, AI, cleanup, sequence-bound history results, assets, achievements, and the implementation file map. |
| `docs/systems/event_system/events_log_window.md` | Added the secondary-actor source, view, selected, and open-detail state plus the Event 17 bound, lost-leader, and unresolved branches. |
| `docs/systems/event_system/events_log_evolutions_and_clusters.md` | Added Event 17's exact historical result context and three ordered evolution previews. |
| `docs/systems/event_system/event_clusters.md` | Retained Event 17 as the optional low-danger Diplomatic Panic member at 65% participation and documented that its cluster route still selects its own weighted minor. |
| `docs/assets/017_random_faction/gfx_handoff.md` | Corrected the category consumer to `random_faction_bloc_pressure_category`. |
| `docs/plans/017_random_faction_plans/017_random_faction_improvement_addendum.md` | Added a live resolution table, corrected the asset handoff path, and separated resolved implementation blockers from external catalog and audit evidence. |
| `docs/plans/017_random_faction_plans/scripted_system_architecture_report.md` | Marked its tuning-ownership blocker resolved and pointed its historical restored-draft evidence to the live closure disposition. |
| `docs/plans/017_random_faction_plans/subagent_handoffs/017_random_faction_documentation_curator_handoff.md` | Added this audit and resume record. |

## Exact implementation corrections recorded

- Supported automatic, manual settings, Event Details, and cluster dispatch all call the weighted Event 17 runtime-context helper. None prefers the current player.
- Human event `chaosx.nr17.10` and AI resolver `chaosx.nr17.20` consume the same one to four regular event targets.
- `random_faction_evo3_cascade_count` is country-scoped to the active anchor. No global cascade counter exists.
- Evolution III requires at least two unique candidates. Its response budget is the smallest of half rounded up, candidate count minus one, and five. A dynamic regional flag blocks another full cascade in the same region for 45 days.
- The faction leader chosen by a successful accession is stored against the exact Event Log history sequence and Event ID. History and Event Details distinguish bound, lost-leader, and unresolved results.
- Event Details has exactly three previews at tiers 1, 2, and 3 for Regional Bloc Race, Pressured Neutrality, and Collapse of Neutrality.
- Faction-leader reaction `chaosx.nr17.40` records both valid responses as support. Staff officers grant a 180-day liaison, remove 12 pressure, and improve mutual relations. Radio networks add 10 pressure and 240 days of Bloc Polarization. Both the visible options and their effect helpers require the same living leader, living independent target, same-faction, no-direct-war, and stored chosen-leader context; an invalid context exposes only cleanup.
- Frontier Commitment snapshots the launch capital plus every national core state bordering a non-core state in `random_faction_frontier_core_state_targets`, refuses to start unless all are controlled, and permanently cancels through `on_state_control_changed` on the first stored-state loss. Recovery cannot restore the 180-day proof.
- Liaison Web snapshots exactly three supported countries, registers the candidate leader on each target, and breaks persistently on subject conversion, capitulation, annexation, special or base-validity loss, or direct war with that leader. Faction membership remains allowed, and no replacement can enter the stored three-country cohort.
- Not Everyone Signed snapshots only the original eligible regional survivors and registers the anchor on each survivor. Faction entry, subject conversion, capitulation, annexation, special conversion, or other base-validity loss permanently removes that country, so the 180-day check can award only from the original cohort and cannot substitute a later survivor.
- Four Doors uses `random_faction_alignment_memory_is_valid` at its 365-day check, so the candidate must remain in the originally chosen faction, including a valid transferred leadership successor, rather than merely belong to any faction.
- The decision category consumer is `random_faction_bloc_pressure_category`.
- Shared script constants own Event 17 durations. Fixed delayed events and decision re-enable fields use constants directly. Computed delays, timed flags, and timed ideas use temporary-variable bridges, and mission timeouts use country variables initialized from constants before activation. Only parser-static `ai_hint_pp_cost` and maritime `random_select_amount` retain documented file-scoped values.
- Both animated decision sprites use eight authored 64 by 64 frames at 8 FPS with looping and play-on-show behavior. Their frame-000 static companions remain registered.

## Plan and handoff disposition

- The decision and mission audit is accepted as complete for all eleven families.
- The icon artist handoff and asset manifest are accepted as complete. No asset family is missing.
- The closure addendum's Evolution III budget, exact history result, and evolution-preview blockers are implemented.
- The scripted-system architecture tuning-ownership blocker is resolved. Its report now points to the live closure disposition.
- The three continuous-achievement audit findings are resolved in gameplay and recorded in the canonical achievement and cleanup sections: launch-state cancellation for Frontier Commitment, an exact-three reciprocal target registry for Liaison Web, and an original-survivor reciprocal registry for Not Everyone Signed.
- The final localisation audit passed after all four achievement proof findings were resolved. Its handoff is `017_random_faction_localisation_audit_handoff.md`; it reports no blocker, fallback, simplification, missing key, duplicate key, orphan key, or unresolved gameplay/localisation mismatch.
- The documentation and workbook portions of the catalog reconciliation blocker are complete. The spreadsheet readback is recorded in `017_random_faction_spreadsheet_alignment_handoff.md`.
- The scripted-system architecture proposals for a generic option scorer, a new MTTH table, and a larger generic lifecycle framework were not adopted. The closure addendum explicitly rejects those additions because the bounded Event 17 implementation satisfies the accepted surface without them.
- Country-specific prose branches, extra evolutions, custom GUI, focus content, formables, country packages, super-events, and extra asset variants remain rejected future expansion rather than incomplete Event 17 work.
- No Event 17 plan changed the accepted design, so nothing was promoted into `docs/specs/017_random_faction_specs/`.

## Catalog alignment record

The catalog worker copied the exact in-game strings from these keys rather than paraphrasing them:

- `chaosx.events_log.window.event_details.random_faction`
- `chaosx.events_log.window.event_details.random_faction.result`
- `chaosx.events_log.window.event_details.random_faction.result.neutral`
- `chaosx.events_log.window.event_details.random_faction.result.unresolved`
- `chaosx.events_log.window.evolution_details.random_faction.title.stage_1`
- `chaosx.events_log.window.evolution_details.random_faction.title.stage_2`
- `chaosx.events_log.window.evolution_details.random_faction.title.stage_3`
- `chaosx.events_log.window.evolution_details.random_faction.body.stage_1`
- `chaosx.events_log.window.evolution_details.random_faction.body.stage_2`
- `chaosx.events_log.window.evolution_details.random_faction.body.stage_3`

The script metadata is Minor Repeatable, Diplomatic Panic, optional low danger, and 65% cluster participation. The parallel spreadsheet worker completed the writeback and verified `Events!18` against the exact Event Details and three evolution title/body pairs. It also verified `Clusters!4` with the final Diplomatic Panic description and member list `8, 17`. This documentation agent did not modify the workbook.

## Validation and boundaries

- The stale current-player preference and nonexistent global Evolution III counter were removed from the canonical implementation document.
- The documented Evolution III budget, region lock, exact history arrays, decision identifiers, guarded leader reaction outcomes, reciprocal achievement registries, continuous disqualifier hooks, and asset consumers were checked against the live scripts and localisation.
- All paths in the implementation map were checked against the workspace.
- Read-only asset validation confirmed expected dimensions for all 44 Event 17 runtime DDS files, eight unique source-frame hashes in each animation package, and existing files for all 26 texture paths registered in `interface/017_random_faction.gfx`.
- The spreadsheet alignment handoff confirms exact localisation readback for `Events!B18:F18`, final metadata in `Events!J18:M18`, and the `8, 17` member list in `Clusters!D4` without workbook structure or style damage.
- The final localisation audit handoff passes the Event 17 and achievement wording, including the up-to-four forced choice, both guarded leader reactions and cleanup-only invalid-context response, exact history result branches, the Four Doors original-faction proof, and the final continuous Frontier, Liaison, and neutral-survivor contracts.
- The Event 17 source specs were not edited.
- No runtime gameplay, localisation, binary asset, or workbook file was changed by this agent.

## Simplifications, omissions, and blockers

No fallback, simplification, substitute mechanic, or documentation omission was introduced. The catalog workbook readback and final localisation audit are complete. The final completion audit remains external closure evidence and is not claimed complete by this documentation-only handoff until its owning agent reports it.
