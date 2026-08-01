# Fallout Reactor Shift chain proof

## Scope

The Reactor Shift is a dormant ordinary Fallout technate chain. It uses candidate `810`, transaction `710087`, route `7206`, history `9193`, events `810` through `816`, and no world-end scenario id.

## Source surfaces

- Candidate producer: `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- Constants: `common/script_constants/fallout_world_end_event_constants.txt` and `common/script_constants/fallout_world_end_reactor_shift_constants.txt`
- Triggers: `common/scripted_triggers/fallout_world_end_reactor_shift_event_triggers.txt`
- Effects: `common/scripted_effects/fallout_world_end_reactor_shift_event_effects.txt`
- Events: `events/fallout_world_end_events.txt`
- Localisation: `localisation/english/fallout_world_end_reactor_shift_l_english.yml`
- Event Log routing: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and `common/scripted_localisation/fallout_world_end_reactor_shift_event_log_scripted_localisation.txt`
- Presentation: `interface/fallout_world_end.gfx`, `common/dynamic_modifiers/fallout_world_end_reactor_shift_dynamic_modifiers.txt`, and the dedicated report DDS

## Mechanics proof

The candidate is restricted to the East Asia region, Manchurian Reactor Keeps country memory, the technate archetype, a closed Load Shedding state memory, current Air Winter and Supply Access receipts, a power or industrial building, and an external neighboring state. It selects the lowest eligible state and uses the existing Fallout scheduler row contract.

The four branches use distinct survival costs and safety ledgers. The delayed result freezes the state, owner, controller, generation, Air Winter values, Supply Access values, population, and foreign neighbor. It grades safety legitimacy, operator fatigue, operator trust, power reserve, operator capacity, spare parts, Medicine, Recognition, Cohesion, the technate bonus, and the selected branch.

The result updates Air Winter, Supply Access, Medicine, Recognition, Cohesion, Stability, War Support, technical ledgers, branch memory, bilateral opinion, and bounded Deaths failure. The callback updates the same state receipts, technical ledgers, callback memory, dynamic modifier, and bounded Deaths failure. One failed result also damages a native infrastructure level.

Hidden AI uses the same four affordability checks, weighted branch choices, delayed tickets, result and callback effects, Event Log payloads, and cleanup path as human play.

## Engine-sensitive surface record

The event block uses `is_triggered_only = yes` and receives only the existing Fallout ordinary scheduler dispatch. It does not add an `add_namespace` entry, normal Fallout consequence event, evolution row, or scenario registration.

The candidate row is appended only by the Fallout candidate registry and remains dormant until the scheduler opens it. The opening, delayed result, callback, and cleanup effects all revalidate current owner, controller, generation, state identity, Air Winter, Supply Access, neighbor, and ticket receipts before mutating state.

The player branch uses the normal event option path. The AI branch is hidden and uses the same branch scheduler. Delayed results and callbacks use the existing Fallout delayed transaction coordinator, so save recovery and host authority remain inside that shared coordinator rather than in a second request path.

The Deaths path supplies `state_civilian_population_loss_requested`, a minimum remaining population, the Fallout aftermath reason, and the target country before `apply_exact_state_civilian_population_loss`. This avoids a direct population subtraction and retains the project Deaths ledger.

## Static audit record

The tranche is audited for unique event ids `810` through `816`, preservation of the preceding `803` through `809` rows, balanced Clausewitz braces and quotes in the dedicated scripts, resolved dedicated constant and localisation references, no unsupported comparison operators in authored sources, no em dashes or semicolons in authored prose, and UTF-8 BOM on the dedicated localisation file.

The source image, processed report PNG, DDS dimensions, hashes, sprite registration, and event picture consumers are recorded in `docs/assets/810_reactor_shift/manifest.md` and `gfx_handoff.md`.

A read-only Event Inspector lint was requested for `chaosx.fallout.810` with `expandHelpers = false`, depth `1`, twenty nodes, forty edges, and refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` with status `ok`, zero blocking diagnostics, and artifact `event-lint-046cd6739bc7.json` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The report marked validation incomplete because workspace-wide helper and lifecycle projections were deferred. That tooling boundary is recorded rather than treated as live campaign acceptance. No Hearts of Iron IV process is launched.

Scheduler activation, host authority, save recovery, multiplayer delivery, and live Event Log presentation remain user-owned runtime checks. The exact native all-valid-province thermonuclear sweep remains a separate Fallout consequence blocker.
