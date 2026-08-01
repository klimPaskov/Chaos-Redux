# Fallout The Fertility Question chain proof

This proof covers the dormant ordinary Fallout chain The Fertility Question. It does not claim Fallout activation, blackout delivery, host authority, save recovery, multiplayer behavior, exact province sweep execution, scheduler activation, or HOI4 runtime acceptance.

## Identity and ownership

- Candidate id `894` uses transaction key `710099` and route `7230`.
- The chain uses `chaosx.fallout.970` through `chaosx.fallout.976` because the existing manual Fallout entry uses `900`, the manual callback uses `903`, and the thermonuclear batch and verifier occupy the `910` through `966` range. The unique event constants map the Fertility Question names to these ids.
- Event Log history id `9205` is routed through dedicated Fertility Question localisation.
- Fallout remains a consequence and is not registered as an ordinary event, evolution, scenario log entry, or super-event.

## Deterministic boundary

The candidate admits the Congo Green Basin mutant-polity country memory from campaign day `1200` through `10000`. It selects the lowest current controlled state with a closed Mixed Settlement Petition memory, valid survival identity, durable Air Winter and Supply Access rows, living population, Shelter, Adaptation, bounded Exposure and Disease Pressure, and a foreign neighbor. The owner must retain family legitimacy, cohort pressure, Medicine, Cohesion, Recognition, and one affordable branch.

The registry freezes state and witness receipts, owner and controller, transition generation, Air Winter, Supply Access, and household ledgers. Every delayed lane revalidates those receipts. A changed receipt cancels the chain and authenticated cleanup releases reserved transaction rows.

## Branch and delayed mechanics

The four branches are Offer Voluntary Household Support, Build Public Cohort Services, Open Two-Witness Adoption Houses, and Keep an Emergency Register Only. Costs are Food 2, Medicine 3, Recognition 2 for voluntary support, Scrap 2, Power 2, Recognition 2 for public services, Fuel 1, Recognition 2, and Cohesion 1 for adoption houses, and Food 1, Medicine 1, Fuel 1, Recognition 1 for the emergency register.

The result delay is `49` days and the next-generation review delay is `365` days. Success, partial, and failure outcomes alter Air Winter and Supply Access, apply bounded Deaths failure paths, add dedicated country presentation, write bilateral opinion, and preserve branch memories. The callback settles household ledgers and closes the state memory only after both delayed transactions settle.

## Wiring evidence

- Gameplay: `events/fallout_world_end_events.txt`, `common/scripted_triggers/fallout_world_end_fertility_question_event_triggers.txt`, `common/scripted_effects/fallout_world_end_fertility_question_event_effects.txt`, and `common/dynamic_modifiers/fallout_world_end_fertility_question_dynamic_modifiers.txt`.
- Constants and candidate registry: `common/script_constants/fallout_world_end_fertility_question_constants.txt`, `common/script_constants/fallout_world_end_event_constants.txt`, and `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`.
- Event Log: `common/scripted_localisation/fallout_world_end_fertility_question_event_log_scripted_localisation.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `localisation/english/fallout_world_end_fertility_question_l_english.yml`.
- Opinion and assets: `common/opinion_modifiers/fallout_fertility_question_opinion_modifiers.txt`, `interface/fallout_world_end.gfx`, `gfx/event_pictures/fertility_question/report_event_fallout_fertility_question.dds`, and `docs/assets/894_fertility_question/`.

Static audit covers duplicate ids, constants, predecessor memory gating, candidate wiring, branch and delayed references, Event Log history routing, localisation key coverage, dedicated art wiring, and wording hygiene. No HOI4 runtime was launched.

The focused read-only Event Inspector lint for `chaosx.fallout.970` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, `blockers: []`, and `blockingDiagnostics: 0` on revision `4873e18aa80628118c4e5057539a08cedf281d9e70862c073aab63d71dd5aabd`. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c7bfc4060d9a15761d5ae438fb977e7491c86f992fa9e046efd448a609dfa98/9e8085f831b6305f3d2bfa5524b06fe5156566e779a413a66d3e16adde1d08ae/event-lint-4873e18aa806.json`. The tool reports a workspace-wide helper-analysis deferral, so this is focused source evidence rather than a runtime or full-workspace acceptance claim.
