# Fallout Metro Republic Below tranche proof

Status: implemented as a dormant ordinary Fallout chain, statically reconciled, and excluded from release-floor credit.

## Identity and ownership

The European chain uses `chaosx.fallout.614` for the human opening, `chaosx.fallout.615` for hidden AI opening, `chaosx.fallout.616` for the human delayed result, `chaosx.fallout.617` for hidden AI result, `chaosx.fallout.618` for the human callback, `chaosx.fallout.619` for hidden AI callback, and `chaosx.fallout.620` for cleanup.

The candidate id is `614`, the transaction key is `710059`, the route id is `7159`, the route upper bound is `7160`, and Event Log history is `9165`.

All event blocks live in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout` and use dedicated Fallout constants, scripted triggers, scripted effects, localisation, dynamic modifiers, Event Log payloads, and report art.

No zombie event id, file, asset, audio, sprite, or path is reused.

## Candidate admission

The candidate registry scans every owned state and keeps the lowest native state id that passes `fallout_event_614_state_is_current`.

The state must be in Europe, have a current Fallout row and produced Air Winter snapshot, use the native `city` or `large_city` category, retain population above `8000`, shelter capacity from `30` through `100`, Supply Access at least `15`, Reclamation at least `5`, infrastructure at least `1`, exposure below `80`, and disease below `70` when disease is present.

State selection rejects reserved, committed, and closed registry flags, and the country row reauthenticates ownership, control, generation, campaign day, Food, Medicine, Power, Recognition, Cohesion, and one affordable branch.

The candidate stores the pretransition shelter and exposure receipts and uses the native state target as the transaction subject.

The producer remains idempotent because the candidate row is appended only inside the current Fallout registry build and the shared scheduler keeps the activation flags unset.

## Branch and cost proof

| Branch | Native or survival cost | Durable direction |
| --- | --- | --- |
| Open a surface council | Food `5`, Scrap `3`, Recognition `3` | surface legitimacy, district trust, salvage access, and faction pressure |
| Keep the wards autonomous | Food `4`, Power `4`, Scrap `2`, Recognition `2` | tunnel autonomy, district trust, evacuation readiness, and faction pressure |
| Integrate the military corridor | Food `4`, Fuel `2`, Support Equipment `3`, Command Power `12` | military integration, salvage access, War Support, and a Cohesion tradeoff |
| Evacuate the lower districts | Food `6`, Medicine `3`, Fuel `3`, Recognition `1` | evacuation readiness, district trust, shelter movement, and exposure control |

Military payment uses native `remove_equipment_to_stockpile` for Support Equipment and native `add_command_power` with an exact whole-number cost.

The seven country ledgers initialize once and clamp to `0` through `100`.

## Deterministic result and callback

The opening freezes shelter, Supply Access, Reclamation, infrastructure, Food, Medicine, Power, Recognition, Cohesion, exposure, disease, and state population before payment.

The result is scheduled for `35` days and grades ten normalized survival components plus a branch-specific signal.

Success thresholds are `60`, `57`, `63`, and `59` for surface council, tunnel autonomy, military integration, and evacuation.

Partial thresholds are `40`, `37`, `43`, and `39` for the same branch order.

Success improves Supply Access, shelter, Reclamation, Recognition, Cohesion, exposure, and branch-specific ledgers.

Partial success gives smaller Supply Access, shelter, Reclamation, Cohesion, and branch-ledger improvements.

Failure subtracts Supply Access and shelter, raises exposure and disease pressure, reduces Cohesion, and requests bounded population loss through `apply_exact_state_civilian_population_loss` with the Fallout aftermath reason.

The callback is scheduled `270` days after the result and reauthenticates country, state, owner, controller, generation, branch, result receipt, and callback ticket before grading.

Callback success, partial, and failure use district trust, the selected branch ledger, inverse faction pressure, Supply Access, shelter, Reclamation, Recognition, Cohesion, and inverse exposure and disease.

Callback failure subtracts Supply Access and shelter, raises exposure, reduces Cohesion, and requests bounded Deaths-system population loss.

Result and callback memories are state flags and durable country ledgers, while cleanup removes only transient receipts and reservation flags.

## Event Log and presentation

History `9165` routes four choice payloads, twelve branch result payloads, three callback payloads, and one cancellation payload.

The country is the primary actor and the authenticated metro state is the secondary actor.

The dedicated report sprite is `GFX_report_event_fallout_metro_republic_below` and the runtime DDS is `gfx/event_pictures/fallout_world_end/report_event_fallout_metro_republic_below.dds`.

Asset source, processed preview, runtime hash, DDS header, prompt, and handoff are recorded under `docs/assets/614_metro_republic_below/manifest.json` and its companion files.

The final report card is a generated fictional European metro shelter scene with no readable text, real flags, or identifiable people.

The authoritative event catalog row is owned by `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and is exported through `.tools/export_event_catalog_csv.py`.

## Cleanup and abort behavior

The generation reset calls `fallout_event_614_abort_on_generation_change` after the existing Tunnel Ward reset hook.

Opening, result, callback, and cleanup each reauthenticate the current transaction and target before applying state effects.

Target loss or generation change releases payment and state reservations before a cleanup receipt is accepted.

Cleanup clears transient branch, target, ticket, result, callback, reservation, and payment flags while preserving durable outcome memories and ledger history.

No Metro Republic effect writes `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

## Engine-sensitive evidence and limits

Static source checks confirm balanced braces, unique event ids, dedicated localisation keys, no zero-width characters in the new gameplay files, no literal unsupported comparison operators, and no standalone plus-sign script lines.

The DDS has `DDS ` magic, a `124` byte header, `210` by `176` dimensions, `840` byte pitch, one mip level, 32-bit BGRA pixels, and `147968` total bytes.

The installed documentation and offline wiki references were consulted for event scope, delayed effects, dynamic modifiers, native equipment payment, Command Power, state variables, and Event Log routing.

HOI4 was not launched, as requested.

The optional event-inspector service returned its existing transport closure before producing an artifact, so native popup delivery, hidden AI issuance, save recovery, multiplayer host authority, Event Log rendering, dynamic modifier display, and delayed target retention remain unobserved.

The exact engine-native all-valid-province thermonuclear sweep for the manual Fallout scenario remains a separate blocker and is not claimed by this tranche.

## Release status

This tranche adds `7` defined blocks and one ordinary candidate row, bringing the dormant reviewed pilot to `59` ordinary rows and `495` defined blocks.

The release-floor count remains `0 of 660` because scheduler activation, the full event library, runtime review, and the required human campaign pacing evidence are not complete.
