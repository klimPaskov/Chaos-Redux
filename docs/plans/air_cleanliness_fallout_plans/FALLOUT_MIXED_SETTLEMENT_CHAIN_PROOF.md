# Fallout Mixed Settlement Petition chain proof

This proof covers the dormant ordinary Fallout chain Mixed Settlement Petition. It does not claim Fallout activation, blackout delivery, host authority, save recovery, multiplayer behavior, exact province sweep execution, scheduler activation, or HOI4 runtime acceptance.

## Identity and ownership

- Candidate id `887` uses transaction key `710098` and route `7228`.
- Human opening, hidden AI opening, human result, hidden AI result, human callback, hidden AI callback, and cleanup use suffixes `887` through `893`.
- Event Log history id `9204` is routed through dedicated Mixed Settlement Petition localisation.
- Fallout remains a consequence and is not registered as an ordinary event, evolution, scenario log entry, or super-event.

## Deterministic boundary

The candidate admits the Congo Green Basin mutant-polity country memory from campaign day `720` through day `9000`. It selects the lowest current controlled state with a closed Clinic or Council memory, valid survival identity, durable Air Winter and Supply Access rows, living population, Shelter, Adaptation, bounded Disease Pressure, and a foreign neighbor. The owner must retain Settlement Legitimacy, Settlement Boundary Pressure, Medicine, Cohesion, Recognition, and one affordable branch.

The registry freezes state and witness receipts, owner and controller, transition generation, Air Winter, Supply Access, and settlement ledgers. Every delayed lane revalidates those receipts. A changed receipt cancels the chain and authenticated cleanup releases reserved transaction rows.

## Branch and delayed mechanics

The four branches are Grant Equal Citizenship, Keep Separate Districts, Supervise the Integration, and Refuse the Settlement Petition. Costs are Food 2, Medicine 2, Recognition 3 for Equal Citizenship, Scrap 3, Power 1, Recognition 2 for Separate Districts, Fuel 2, Recognition 2, and Cohesion 2 for Supervised Integration, and Food 3, Medicine 2, Fuel 1, Recognition 1 for Refuse Settlement.

The result delay is `42` days and the first-year review delay is `300` days. Success, partial, and failure outcomes alter Air Winter and Supply Access, apply bounded Deaths failure paths, add dedicated country presentation, write bilateral opinion, and preserve branch memories. The callback settles settlement ledgers and closes the state memory only after both delayed transactions settle.

## Wiring evidence

- Gameplay: `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_consolidated_triggers.txt`, `common/scripted_effects/fallout_consolidated_effects.txt`, and `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`.
- Constants and candidate registry: `common/script_constants/fallout_consolidated_constants.txt`, `common/script_constants/fallout_consolidated_constants.txt`, and `common/scripted_effects/fallout_consolidated_effects.txt`.
- Event Log: `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `localisation/english/fallout_consolidated_l_english.yml`.
- Opinion and assets: `common/opinion_modifiers/fallout_consolidated_opinion_modifiers.txt`, `interface/fallout_consolidated.gfx`, `gfx/event_pictures/fallout/report_event_fallout_mixed_settlement.dds`, and `docs/assets/887_mixed_settlement/`.

Static audit covers duplicate ids, constants, predecessor memory gating, candidate wiring, branch and delayed references, Event Log history routing, localisation key coverage, dedicated art wiring, and wording hygiene. No HOI4 runtime was launched.

The focused read-only Event Inspector lint for `chaosx.fallout.887` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, `blockers: []`, and `blockingDiagnostics: 0` on revision `c62e6b795a2ee329582a2be8dfd4638916ce0c0ef1784614e39530d9585b6b7f`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16abde6d4a80c3666222a25041e61501b306ee850898949fd80fa319d984e32b/d9cc9ed54a79ae7c928b0adffa9df07ac43361dec9b208f4269abb6d91eeb9bc/event-lint-c62e6b795a2e.json`. The tool reports a workspace-wide helper-analysis deferral, so this is focused source evidence rather than a runtime or full-workspace acceptance claim.
