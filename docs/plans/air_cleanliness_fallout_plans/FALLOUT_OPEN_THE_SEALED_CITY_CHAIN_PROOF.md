# Fallout Open the Sealed City chain proof

## Identity

- Candidate: `740`
- Transaction: `710077`
- Route: `7186`
- Event Log history: `9183`
- Events: `chaosx.fallout.740` through `chaosx.fallout.746`
- Namespace: `chaosx.fallout`
- Status: dormant, authored, statically wired

## Engine-sensitive surfaces recorded

| Surface | Evidence |
| --- | --- |
| State target | `fallout_event_740_state_is_current` requires the current state identity, survival row, Supply Access row, city or large-city category, current Air Winter ledgers, a completed Border Inspection memory, and owner control. |
| Candidate selection | The Fallout candidate producer selects the lowest valid owned state id and stores the target as a state subject. |
| Delayed result | The result transaction freezes state and country values, schedules a human or hidden-AI event after the constant delay, and rechecks owner, state, generation, and registry identity. |
| Callback | The callback uses the same registry and state target, applies current district and branch ledgers, records history `9183`, and prepares authenticated cleanup. |
| Deaths | Result and callback failures route exact state population loss through `apply_exact_state_civilian_population_loss` with the Fallout aftermath reason. |
| Air Winter | Result and callback mutate Shelter, Supply Access, Reclamation, Exposure, and Disease through the live state variables, with clamping and no pretransition snapshot dependency. |
| Event Log | `GetFalloutEvent740EventLogDetail` reads `events_log_history_selected_payload`, while shared history detail routing, shared history name routing, and dedicated localisation cover every choice, result, callback, and cancellation payload. |
| Asset | The same dedicated sprite is used by opening, result, and callback. Hidden AI lanes remain picture-free. Documentation and runtime DDS copies match. |
| Cleanup | The cleanup event authenticates the delayed cleanup token and registry before removing reservation flags, temporary variables, and dedicated modifiers. |

## Static checks performed

- Event ids `.740` through `.746` occur exactly once in `events/fallout_world_end_events.txt`.
- The new effect, trigger, constants, dynamic modifier, and scripted localisation files have balanced Clausewitz braces.
- The new source surface contains no unsupported `<=` or `>=` operators.
- New English localisation is UTF-8 with BOM and contains no em dash or semicolon.
- Dedicated constant references are reconciled against the new `fallout_event_740_*` constant blocks.
- The report DDS is one-level uncompressed A8R8G8B8 at 210 x 176. Documentation and runtime copies share hash `BC88B76AAFC5769B36D2263919A93EFC5376CD54091F8D1B0C23DDBC9D560E66`.
- The candidate producer, event ids, namespace, sprite key, Event Log history, and workbook row are cross-referenced by source inspection.

Runtime dispatch, save recovery, multiplayer delivery, Event Log rendering, and in-game visual validation remain user-owned gates. HOI4 was not launched.
