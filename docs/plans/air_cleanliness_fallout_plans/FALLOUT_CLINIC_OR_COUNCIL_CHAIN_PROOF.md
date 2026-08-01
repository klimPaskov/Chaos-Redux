# Fallout Clinic or Council chain proof

This proof covers the dormant ordinary Fallout chain Clinic or Council. It does not claim Fallout activation, blackout delivery, host authority, save recovery, multiplayer behavior, exact province sweep execution, scheduler activation, or HOI4 runtime acceptance.

## Identity and ownership

- Candidate id `880` uses transaction key `710097` and route `7226`.
- Human opening, hidden AI opening, human result, hidden AI result, human callback, hidden AI callback, and cleanup use suffixes `880` through `886`.
- Event Log history id `9203` is routed through dedicated Clinic or Council localisation.
- Fallout remains a consequence and is not registered as an ordinary event, evolution, scenario log entry, or super-event.

## Deterministic boundary

The candidate admits the Congo Green Basin mutant-polity country memory from campaign day `420` through day `7200`. It selects the lowest current controlled state with a closed The Name We Choose memory, valid survival identity, durable Air Winter and Supply Access rows, living population, Shelter, Adaptation, bounded Disease Pressure, and a foreign neighbor. The owner must retain Clinic Legitimacy, Outside Medicine Pressure, Medicine, Cohesion, Recognition, and one affordable branch.

The registry freezes state and witness receipts, owner and controller, transition generation, Air Winter, Supply Access, and care-governance ledgers. Every delayed lane revalidates those receipts. A changed receipt cancels the chain and authenticated cleanup releases reserved transaction rows.

## Branch and delayed mechanics

The four branches are Give the Clinic Board Oversight, Elect a Ward Council, Bind Board and Council Together, and Reject the Outside Medicine Office. Costs are Food 1, Medicine 4, Recognition 2 for Medical Oversight, Scrap 2, Power 2, Recognition 3 for Elected Council, Fuel 2 and Recognition 2 with a Cohesion cost for Joint Rule, and Food 3, Medicine 1, Fuel 1, Recognition 1 for Reject Outside Medicine.

The result delay is `35` days and the first-season review delay is `240` days. Success, partial, and failure outcomes alter Air Winter and Supply Access, apply bounded Deaths failure paths, add dedicated country presentation, write bilateral opinion, and preserve branch memories. The callback settles care ledgers and closes the state memory only after both delayed transactions settle.

## Wiring evidence

- Gameplay: `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_world_end_clinic_or_council_event_triggers.txt`, `common/scripted_effects/fallout_world_end_clinic_or_council_event_effects.txt`, and `common/dynamic_modifiers/fallout_world_end_clinic_or_council_dynamic_modifiers.txt`.
- Constants and candidate registry: `common/script_constants/fallout_world_end_clinic_or_council_constants.txt`, `common/script_constants/fallout_world_end_event_constants.txt`, and `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Event Log: `common/scripted_localisation/fallout_world_end_clinic_or_council_event_log_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `localisation/english/fallout_world_end_clinic_or_council_l_english.yml`.
- Opinion and assets: `common/opinion_modifiers/fallout_clinic_or_council_opinion_modifiers.txt`, `interface/fallout_world_end.gfx`, `gfx/event_pictures/clinic_or_council/report_event_fallout_clinic_or_council.dds`, and `docs/assets/880_clinic_or_council/`.

Static audit covers duplicate ids, constants, predecessor memory gating, candidate wiring, branch and delayed references, Event Log history routing, localisation key coverage, dedicated art wiring, and wording hygiene. No HOI4 runtime was launched.

The focused read-only Event Inspector lint for `chaosx.fallout.880` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, `blockers: []`, and `blockingDiagnostics: 0` on revision `1add9859f89363a304c752a4d09b259f52dbc15817e5eed49fcb1f4ca2598de6`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81a4dd39097966dc020448b655aff0dcae6fdcef42453407cea732109a2cc30e/d34731df56f6a399dccda5dddd66e75912b33d9112e9a9531adc2531e7259474/event-lint-1add9859f893.json`. The tool reports a workspace-wide helper-analysis deferral, so this is focused source evidence rather than a runtime or full-workspace acceptance claim.
