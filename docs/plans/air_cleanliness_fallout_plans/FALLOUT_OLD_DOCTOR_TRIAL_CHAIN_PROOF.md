# Fallout The Old Doctor's Trial chain proof

This proof covers the dormant ordinary Fallout chain The Old Doctor's Trial. It does not claim Fallout activation, blackout delivery, host authority, save recovery, multiplayer behavior, scheduler release-floor credit, or HOI4 runtime acceptance.

## Identity and ownership

- Candidate id `901` uses transaction key `710100` and route `7232`.
- The chain uses `chaosx.fallout.1023` through `chaosx.fallout.1029`, leaving the manual Fallout entry at `900`, the manual callback at `903`, and the existing occupied range through `1022` untouched.
- Event Log history id `9206` routes through dedicated Old Doctor's Trial localisation and `GetFalloutEvent901EventLogDetail`.
- Fallout remains a consequence and is not registered as an ordinary event, evolution, scenario log entry, or super-event.

## Deterministic boundary

The candidate admits the Congo Green Basin mutant-polity country memory from campaign day `1600` through `11000`. It requires current country and survival rows, Medicine `14`, Cohesion `32`, Recognition `18`, trial legitimacy `55`, atrocity pressure `5`, one affordable branch, and no active chain receipt. It selects the lowest controlled state with current identity and resource rows, living population, Shelter `22`, Supply Access `16`, Adaptation `18`, bounded Disease Pressure `20` through `89`, bounded Exposure `10` through `89`, a valid Air Winter phase, and a foreign neighbor. The state must carry the closed `fallout_event_894_memory_closed` flag.

The registry freezes country, state, controller, witness, transition generation, Air Winter values, Supply Access, and the seven Old Doctor's Trial ledgers. Every delayed lane revalidates those receipts. A changed receipt cancels the chain and authenticated cleanup releases the state and witness reservations.

## Branch and delayed mechanics

The four branches are Open a Public Trial, Convene a Truth Commission, Pardon the Doctor for Retained Knowledge, and Keep the Records Under Seal. Their costs are Food `2`, Medicine `3`, Recognition `2`; Scrap `2`, Power `2`, Recognition `2`; Fuel `1`, Recognition `2`, and Cohesion `1`; and Food `1`, Medicine `1`, Fuel `1`, Recognition `1`.

The result resolves after exactly `56` days and the witness review after exactly `420` days. Success, partial, and failure outcomes alter Air Winter and Supply Access, apply bounded Deaths failure paths, add dedicated country presentation, write branch and cause memories, write bilateral opinion, record Event Log payloads, and preserve hidden-AI parity. Cleanup is idempotent and closes the state memory only after both delayed receipts settle.

## Wiring evidence

- Gameplay: `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_consolidated_triggers.txt`, `common/scripted_effects/fallout_consolidated_effects.txt`, and `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`.
- Constants and candidate registry: `common/script_constants/fallout_consolidated_constants.txt`, `common/script_constants/fallout_consolidated_constants.txt`, and `common/scripted_effects/fallout_consolidated_effects.txt`.
- Event Log and localisation: `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `localisation/english/fallout_consolidated_l_english.yml`.
- Opinion and assets: `common/opinion_modifiers/fallout_consolidated_opinion_modifiers.txt`, `interface/fallout_consolidated.gfx`, `gfx/event_pictures/fallout/report_event_fallout_old_doctor_trial.dds`, and `docs/assets/901_old_doctor_trial/`.
- Catalog and source design: `docs/specs/air_cleanliness_fallout_specs/specs/102_reviewed_archetype_old_doctors_trial.md` and the authoritative workbook row `FALLOUT-901`.

Static audit must verify duplicate ids, constants, predecessor-memory gating, candidate wiring, branch and delayed references, Event Log history routing, localisation key coverage and BOM, dedicated art wiring, and wording hygiene. Focused Event Inspector lint may document blocking diagnostics for `chaosx.fallout.1023`, but no HOI4 runtime claim is made.

The focused read-only Event Inspector lint for `chaosx.fallout.1023` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, `blockers: []`, and `blockingDiagnostics: 0` on revision `c53024830035104df61c33565fca7813bd8aede649e739a38f3463a86a22ab04e`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e64f93ca495710b385b8c4a33ea06e7fdf5b6559c8cae1afbffb36658762741/b0db53b72634368ed0221cd05be7514ecd8e77293e383060d84deccc3a66b5f4/event-lint-c53024830035.json`. The tool reports a workspace-wide helper-analysis deferral, so this is focused source evidence rather than a runtime or full-workspace acceptance claim.
