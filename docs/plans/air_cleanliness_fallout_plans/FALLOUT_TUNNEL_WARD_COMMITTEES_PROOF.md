# Fallout Tunnel Ward Committees tranche proof

Status: implemented as a dormant ordinary Fallout chain, statically reconciled, and excluded from release-floor credit.

## Identity and ownership

The East Asia chain uses `chaosx.fallout.607` for the human opening, `chaosx.fallout.608` for hidden AI opening, `chaosx.fallout.609` for the human delayed result, `chaosx.fallout.610` for hidden AI result, `chaosx.fallout.611` for the human callback, `chaosx.fallout.612` for hidden AI callback, and `chaosx.fallout.613` for cleanup.

The candidate id is `607`, the transaction key is `710058`, the route id is `7158`, the route upper bound is `7159`, and Event Log history is `9164`.

All event blocks live in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout` and use dedicated Fallout constants, scripted triggers, scripted effects, localisation, dynamic modifiers, Event Log payloads, and report art.

No zombie event id, file, asset, audio, sprite, or path is reused.

## Candidate admission

The candidate registry scans every owned state and keeps the lowest native state id that passes `fallout_event_607_state_is_current`.

The state must have a current Fallout state row, a current generation, a produced Air Winter snapshot, an East Asia region match, a `large_town`, `city`, or `large_city` category, surviving population above `6000`, at least `24` pretransition shelter capacity, Supply Access at least `12`, Reclamation at least `6`, exposure below `78`, disease pressure below `72`, one non-damaged infrastructure level, and no reservation, commitment, closure, evacuation, or conflicting state transaction.

The candidate stores `fallout_pretransition_air_winter_shelter_capacity` and `fallout_pretransition_air_winter_exposure` in the row. It does not substitute the native `bunker` building for the Air Winter shelter receipt.

Country admission authenticates the current Fallout country row, generation, East Asia region, campaign-day band, minimum Food, Medicine, Power, Recognition, Cohesion, and one affordable branch.

The producer remains idempotent because it appends the row only when the country registry has not already built the current candidate generation.

## Branch and cost proof

The human and hidden-AI lanes share the same branch ids and result reservation.

| Branch | Native or survival cost | Durable direction |
| --- | --- | --- |
| Recognize the ward councils | Food `5`, Medicine `3`, Recognition `3` | Committee trust, representation, ward autonomy, and refugee integration |
| Centralize appointments | Food `4`, Power `5`, Scrap `3`, Recognition `2` | Central capacity and register integrity with less ward autonomy |
| Establish military wards | Food `4`, Support Equipment `3`, Command Power `12` | Security control and military roster with a cohesion tradeoff |
| Rotate ward leadership | Food `5`, Medicine `2`, Power `3`, Recognition `3` | Representation, committee trust, and refugee integration |

Military payment uses native `remove_equipment_to_stockpile` for Support Equipment and native `add_command_power` with an exact whole-number cost.

The seven country ledgers initialize once at `35`, `35`, `30`, `20`, `25`, `25`, and `20`, then clamp to `0` through `100`.

## Deterministic result and callback

The opening freezes shelter, Supply Access, Reclamation, infrastructure, Food, Medicine, Power, Recognition, Cohesion, exposure, disease, and population before payment.

The result is scheduled for `28` days and grades ten equal components, including a combined inverse exposure and disease signal.

Success thresholds are `58`, `61`, `62`, and `56` for recognize, centralize, military, and rotate respectively.

Partial thresholds are `38`, `41`, `42`, and `36` for the same branch order.

Success improves Supply Access, shelter, Reclamation, Recognition, Cohesion, exposure, and country stability.

Branch-specific durable ledgers change on every result band, including committee trust, central capacity, ward autonomy, security control, representation, refugee integration, and faction pressure. A successful military ward result also uses native War Support `0.02` and a small Cohesion tradeoff.

Partial success gives a smaller Supply Access, shelter, and Reclamation improvement.

Failure subtracts Supply Access and shelter, raises exposure and disease pressure, reduces Cohesion, and requests bounded population loss through `apply_exact_state_civilian_population_loss` with the Fallout aftermath reason.

The callback is scheduled `210` days after the result and reauthenticates country, state, owner, controller, generation, branch, result receipt, and callback ticket before grading.

Callback success, partial, and failure use committee trust, the branch primary ledger, representation, refugee integration, inverse faction pressure, Supply Access, shelter, Recognition, Cohesion, and inverse exposure and disease.

The callback thresholds are `65` for success and `42` for partial.

Callback failure subtracts Supply Access and shelter, raises exposure, reduces Cohesion, and requests bounded Deaths-system population loss.

Result and callback memories are state flags and durable country ledgers, while cleanup removes only transient receipts and reservation flags.

## Event Log and presentation

History `9164` routes four choice payloads, twelve branch result payloads, three callback payloads, and one cancellation payload.

The country is the primary actor and the authenticated shelter state is the secondary actor.

The dedicated report sprite is `GFX_report_event_fallout_tunnel_ward_committees` and the runtime DDS is `gfx/event_pictures/fallout/report_event_fallout_tunnel_ward_committees.dds`.

Asset source, processed preview, runtime hash, DDS header, prompt, and handoff are recorded under `docs/assets/607_tunnel_ward_committees/manifest.json` and its companion files.

The final report card is a generated fictional shelter scene with no readable text, real flags, or identifiable people.

The authoritative event catalog is updated in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` at Events row `249`, with the exported Events CSV ending in FALLOUT-607.

## Cleanup and abort behavior

The generation reset calls `fallout_event_607_abort_on_generation_change` after the existing Radio Island reset hook.

If an uncommitted opening receipt points at a state that is no longer current, the reset route snapshots `fallout_event_dispatch_issued_target` into `fallout_event_607_target_state_id` before cancelling the exact ordinary receipt. An accepted cancellation records payload `99`, refunds any unresolved paid branch, releases the state reservation and committed flag, and clears the frozen row. This keeps stale opening cleanup bound to the state that issued the receipt.

Opening, result, callback, and cleanup each reauthenticate the current transaction and target before applying state effects.

Target loss records Event Log cancellation payload `99`, applies no frozen result effects, releases the state reservation, and prepares the cleanup receipt.

Cleanup clears transient branch, target, ticket, result, callback, reservation, and payment flags while preserving durable outcome memories and ledger history.

No Tunnel Ward effect writes `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

## Engine-sensitive evidence and limits

Static source checks confirm balanced braces, unique event ids, dedicated localisation keys, no zero-width characters in the new gameplay files, no literal unsupported comparison operators, and no standalone plus-sign script lines.

The DDS has `DDS ` magic, a `124` byte header, `210` by `176` dimensions, `840` byte pitch, one mip level, 32-bit BGRA pixels, and `147968` total bytes.

The installed documentation and offline wiki references were consulted for event scope, delayed effects, dynamic modifiers, native equipment payment, Command Power, and state variables.

HOI4 was not launched, as requested.

The optional event-inspector service returned its existing transport closure before producing an artifact, so native popup delivery, hidden AI issuance, save recovery, multiplayer host authority, Event Log rendering, dynamic modifier display, and delayed target retention remain unobserved.

The exact engine-native all-valid-province thermonuclear sweep for the manual Fallout scenario remains a separate blocker and is not claimed by this tranche.

## Release status

This tranche adds `7` defined blocks and one ordinary candidate row, bringing the dormant reviewed pilot to `58` ordinary rows and `488` defined blocks.

The release-floor count remains `0 of 660` because scheduler activation, the full event library, runtime review, and the required human campaign pacing evidence are not complete.
