# Event 017 Random Faction Completion Audit Handoff

- Date: 2026-07-11
- Auditor role: `chaosx_event_completion_auditor`
- Mode: read-only completion audit
- Commit: none
- Source of truth: `docs/specs/017_random_faction_specs/`

## Verdict

**PASS. Event 017 Random Faction is complete against the accepted specification package in the live tree.**

The implementation contains the required repeatable-event registration, weighted dynamic country and faction selection, forced human choice, slot-neutral AI choice, baseline consequences, all three evolutions, the complete Bloc Pressure decision and mission surface, targeted lifecycle cleanup, exact Event Log result binding, Event Details previews, Diplomatic Panic integration, six achievements, final localisation, wired static and animated assets, canonical documentation, and exact workbook alignment.

No gameplay blocker, missing route, missing decision family, missing AI behavior, missing localisation, missing runtime asset, stale workbook field, unimplemented accepted plan, fallback, or simplification remains. Unrelated camp-repression and genocide-crisis changes in the working tree were excluded from this verdict.

## Audit Basis

The audit read the complete Event 017 specification, matrices, research notes, prompts, source-review manifest, improvement-loop closure handoff, architecture report, canonical event documentation, asset records, workbook handoff, and prior bounded audit handoffs.

Repository guidance used:

- `chaos-redux-events`
- `chaos-redux-event-planning`
- `chaos-redux-subagents`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `xlsx`

The required offline wiki pages and relevant vanilla documentation were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, achievements, event targets, script constants, meta triggers, faction-entry hooks, and mission objectives. Vanilla faction-entry, variable equipment, dynamic mission-threshold, and on-action precedents were compared with the live implementation.

## Completion Matrix

| Accepted surface | Result | Live evidence |
| --- | --- | --- |
| Event identity and registration | Pass | Repeatable event ID 17, root `chaosx.nr17.1`, final name mapping, availability rejection without a dispatchable context, and weighted runtime preparation are wired through `events/017_join_faction.txt`, `common/scripted_effects/chaosx_logic_effects.txt`, and `common/scripted_effects/chaosx_settings_effects.txt`. |
| Dynamic country selection | Pass | `random_faction_prepare_runtime_context` builds a weighted eligible-country pool from current world state. Human countries remain eligible without receiving a preference. Invalid, subject, faction-member, special, capitulated, or optionless countries do not enter a ready context. |
| Dynamic faction options | Pass | `random_faction_collect_faction_options` discovers living faction leaders, removes each selected leader from the pool, and saves exactly `min(valid leaders, 4)` unique regular event targets. No faction tag list or faction-name hardcode is used. |
| Human forced choice | Pass | `chaosx.nr17.10` exposes one to four saved valid options and no baseline decline. The final option is only a same-country invalid-option revalidation route when every saved option has died or become invalid. |
| AI choice | Pass | `chaosx.nr17.20` consumes the same four saved option targets as the human event. Each slot uses the same base chance and the same class of geographic, diplomatic, war, cohesion, pressure, and chaos modifiers; slot number itself carries no preference. |
| Join contract and baseline result | Pass | The selected leader is revalidated immediately before `add_to_faction`; direct enemies and enemy-faction members are rejected. Success applies Alignment Shock, accession pressure/resilience, recent-alignment memory, faction-leader memory, regional pressure, optional wartime coordination, opinion effects, evolution checks, achievement checks, and news. |
| Evolution I | Pass | Regional Bloc Race creates at most one delayed pressured-neighbor response from a unique valid target and opens the intended neutral and faction-leader interactions. |
| Evolution II | Pass | Pressured Neutrality admits only valid war, war-adjacent, or pressured candidates and retains the strict direct-enemy exclusion. Wartime choices require real land, continental, common-enemy, or convoy-backed coastal reach; the option scorer cannot make an unreachable overseas faction legal. |
| Evolution III | Pass | Collapse of Neutrality uses unique candidates and a local response budget equal to the smallest of half rounded up, candidate count minus one, and five. It starts only with at least two candidates, preserves outside-faction capacity, and applies a 45-day dynamic region lock against overlapping full cascades. |
| Bloc Pressure decisions and missions | Pass | All eleven specified families are present as twelve visible decision/mission identifiers: three newly aligned actions, four pressured-neutral actions including Reinforce Border Posts, and four leader families including the corridor decision/mission pair. Costs, availability, target revalidation, AI, outcomes, and cleanup are implemented. |
| Mission thresholds | Pass | Reinforce Border Posts snapshots the exact state and launch division count, displays `N+1`, and completes only above `N`. Guarantee Corridor snapshots the launch train stockpile and requires exactly five additional trains plus fifteen convoys and a still-valid route. Both mission durations are initialized before activation. |
| Pressure and lifecycle state | Pass | Compact tracked arrays and targeted on actions replace periodic world iteration. Each later timed pressure or liaison effect schedules its own buffered cleanup probe. Active achievement proofs survive ordinary pressure expiry, then re-enter cleanup when their hidden proof event resolves. |
| Faction-leader succession | Pass | `on_assume_faction_leadership` transfers supported-minor, chosen-leader, pressure-source, recent-member, region-anchor, and cohesion memory to a valid successor and clears the departed leader's owned state. The tracked "leader" is a country scope, so political-character death needs no separate hook. |
| Special and world-end cleanup | Pass | Holy Realm, Fury, and Death conversion paths mark the special state before Event 017 reconciliation, so the country fails normal validity during cleanup. Every direct world-end path invokes `random_faction_cleanup_after_world_end`, including Final Silence. |
| Event Log exact result | Pass | The dispatcher marks only the baseline selected country as awaiting a history result. Sequence binding and successful leader binding can occur in either order, but finalization writes the secondary actor only to the row matching the exact history sequence and Event ID 17. Pressure and Evolution III follow-up joins cannot write pending history state. |
| Event Details and evolution history | Pass | Bound-leader, lost-leader, and unresolved result branches are present in both History and Event Details. Event Details pushes exactly three previews: Regional Bloc Race at tier 1, Pressured Neutrality at tier 2, and Collapse of Neutrality at tier 3. |
| Diplomatic Panic cluster | Pass | Event 017 is an optional low-danger member beside Event 8, with a 65% participation chance, dynamic availability, selected-trigger promotion, and normal cluster delay/dispatch behavior. |
| Achievements | Pass | Four Doors, Hold the Neutral Line, Crowded Border, Liaison Web, Frontier Commitment, and Not Everyone Signed are registered, localised, sprite-wired, and backed by the required timed or regional proof. Continuous proofs use reciprocal ledgers or stored state arrays where substitution or recovery would otherwise be exploitable. |
| Localisation | Pass | The Event 017, achievement, Event Log, name, and cluster surfaces resolve without missing or duplicate relevant keys. The four touched English localisation files retain UTF-8 BOM encoding. Player-facing wording matches the live forced choice, costs, outcomes, achievement predicates, result branches, and evolution behavior. |
| Assets | Pass | All 44 runtime DDS files are present: 4 report pictures, 13 decision/category/background files, 5 ideas, 4 animation sheet/fallback files, and 18 achievement triplet files. `interface/017_random_faction.gfx` has 26 texture references and all 26 resolve. Each animation has eight unique authored source frames, an eight-frame runtime sheet, a static fallback, a contact sheet, and a preview. |
| Documentation and plans | Pass | `docs/events/017_random_faction.md` is the canonical live implementation record. The improvement-loop blockers, architecture tuning issue, continuous-proof findings, decision audit, localisation audit, asset handoff, and workbook handoff are all resolved or explicitly rejected as unnecessary expansion. |
| Spreadsheet | Pass | Workbook readback matches the final in-game Event Details and Evolution I-III wording at `Events!B18:F18`, retains Minor Repeatable / Diplomatic Panic / Low metadata, and records cluster members `8, 17` with the final Diplomatic Panic description in `Clusters!4`. |

## Adversarial and Balance Scenarios

The following failure-prone cases were traced through the final live scripts:

1. **No valid country or faction:** the event is unavailable before history dispatch; it does not fire a reduced substitute.
2. **One, two, three, or four valid factions:** the saved target count matches the live pool and every displayed option has its matching current-validity trigger.
3. **A saved leader dies or loses eligibility before choice:** the selected country re-collects current leaders. If none remain, it cancels and clears its pending baseline history and selection state.
4. **Human versus AI selection:** both routes read the same saved scopes; no player-country bonus and no slot-position bonus exists.
5. **Direct enemy and impossible overseas choices:** direct war with the leader or any member rejects the faction. Evolution II wartime overseas selection also requires the centralized convoy-backed reach contract rather than AI preference alone.
6. **Evolution I fan-out:** one baseline accession can schedule no more than one valid neighbor response.
7. **Evolution III small and large pools:** the verified maximum responses are 0 of 0-1, 1 of 2, 2 of 3, 2 of 4, 3 of 5, 4 of 8, and 5 at 9 or more. A same-region second anchor cannot receive another full budget during the lock.
8. **Leader reaction spam:** every accession still updates membership and cohesion memory, while `chaosx.nr17.40` is limited by the 180-day leader reaction cooldown.
9. **Mission off-by-one behavior:** the border objective requires one genuinely additional division, and the corridor requires five genuinely additional trains rather than accepting the launch stockpile.
10. **Pressure extension after an earlier cleanup was scheduled:** every later timed idea schedules a new probe, so the original 270-day regional-pressure probe cannot strand a 365-day proof or a later liaison/polarization effect.
11. **History resolution order:** the baseline-only marker supports both "history row first" and "choice first" ordering. Terminal cancellation, lifecycle cleanup, successful finalization, and world cleanup remove the marker and both pending variables.
12. **Achievement substitution attempts:** Liaison Web retains its exact original three targets, Not Everyone Signed retains only the original survivor cohort, and Frontier Commitment permanently cancels on the first stored-state loss even if control is recovered later.
13. **Crowded Border false positives:** the neutral must be living, normal, independent, non-major, outside a faction, and part of Event 017's active regional-pressure population before three distinct neighboring live factions are counted.
14. **Frontier Commitment false positives:** the launch condition is exactly Evolution II plus either existing war or a border with a member of a faction at war with the chosen faction. Generic pressure or an unrelated neighboring war does not qualify.
15. **Capitulation, subject conversion, annexation, invalid government, special conversion, succession, and world end:** the narrow lifecycle paths disqualify continuous proofs where required, clean reciprocal ledgers, reconcile tracked arrays, and remove active missions and obsolete state.

## Findings Resolved During the Completion Audit

The completion pass found and the parent corrected these issues before this final verdict:

- Evolution II's overseas reach was originally only an AI score. It is now a hard join-validity condition with centralized convoy tuning and shared root/previous-scope helpers.
- Special-country cleanup originally ran before the Holy Realm, Fury, or Death identity became invalid to normal-country checks. Those conversion paths now set the special identity first.
- Regional-bucket targets rebuilt after the initial pressure pass could outlive tracking. They now enter the compact pressure array and receive a cleanup probe.
- The faction-leader reaction event could fire on every accession. Its reaction event is now on a 180-day cooldown while memory still updates on every join.
- Later pressure and liaison durations could outlive the original cleanup worker, and ordinary expiry could remove a longer achievement proof. Every later application now schedules its own probe, and proof candidates guard ordinary expiry until their proof event closes.
- Crowded Border could scan unrelated neutrals anywhere in the world. It now requires Event 017 regional or pressure membership plus normal, independent, non-major neutral validity.
- Frontier Commitment's launch gate and player-facing text were broader than the accepted war/enemy-border contract. Script, canonical documentation, and achievement tooltip now use the exact accepted predicate.
- Follow-up joins could leave `random_faction_pending_history_leader`, and option counts could persist after terminal routes. Baseline history writes now require `random_faction_history_result_pending`; follow-ups cannot write them, history state participates in tracked-state cleanup, and option count clears on join, resistance, cancellation, and retirement.
- The unused alignment-anchor variable was removed rather than retained as dead state.

No audit finding remains open.

## Independent Audit Evidence

- The engine-sensitive subaudit passed the `meta_trigger` construction used for variable `divisions_in_state`, the variable `has_equipment` checks, both mission threshold calculations, and the pre-activation mission-duration assignments. It specifically confirmed the border `N + 1` and train `current + 5` semantics against official documentation and vanilla precedents.
- The shared-integration subaudit passed Event Log paired-array sanitation/copying, exact sequence-bound secondary actors, Event Details' three previews, repeatable/settings/cluster registration, all six achievement ledgers, faction succession, special conversion, and every world-end cleanup caller.
- Static integration validation found all 150 Event 017 constant references defined and used, all 177 Event 017 helper calls backed by definitions, and no faction-name hardcode in the implementation.
- The prior decision/mission, localisation, asset, documentation, and spreadsheet handoffs all record a final pass with no remaining blocker in their owned surface.

## Simplifications, Omissions, and Blockers

- Simplifications: none.
- Fallback or substitute mechanics: none. Invalid option recovery re-runs the full live selection contract; it does not provide a weaker alternative result.
- Omitted accepted content: none.
- Missing AI, localisation, decision/mission behavior, achievements, runtime assets, documentation, or workbook alignment: none.
- Completion blockers: none.

The country-specific flavour events, extra evolutions, custom GUI, focus content, formables, country packages, super-events, and additional asset variants listed as future ideas are not part of the accepted Event 017 completion scope and remain intentionally unimplemented.

One non-runtime reproducibility note remains: `docs/assets/017_random_faction/_tooling/process_random_faction_assets.py` still assumes deleted reference/overlay inputs and superseded matte processing. The completed source frames, processed frames, sheets, previews, package DDS files, and runtime DDS files are present and validated, so this does not block the shipped asset package. The old helper must be repaired and its external inputs restored before attempting a clean regeneration.

## Auditor Changes

This audit created only:

- `docs/plans/017_random_faction_plans/subagent_handoffs/017_random_faction_event_completion_audit_handoff.md`

No gameplay, localisation, asset, workbook, specification, or other documentation file was edited by the completion auditor. No commit was created.
