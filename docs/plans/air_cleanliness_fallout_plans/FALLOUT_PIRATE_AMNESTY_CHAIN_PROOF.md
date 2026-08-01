# Fallout Pirate Amnesty Chain Proof

This proof records the static implementation of The Pirate Amnesty. The chain is survivor-country content that becomes eligible only through the Fallout-owned candidate registry and scheduler. It is not Fallout itself. It does not create a normal Fallout Event Log entry for the Fallout consequence, evolution, ordinary super-event, country tag, state transfer, or automatic scheduler activation.

## Identity

| Surface | Value |
|---|---|
| Candidate | `789` |
| Transaction | `710084` |
| Route | `7200` through `7201` |
| Event blocks | `chaosx.fallout.789` through `chaosx.fallout.795` |
| Survivor Event Log history | `9190` |
| Government archetype | `constant:fallout_government_archetype.maritime_remnant` `10` |
| Country memory | `constant:fallout_country_memory.west_african_port_confederacies` `74` |
| Required state memory | `fallout_event_782_memory_closed` |
| Target shape | Lowest owned current coastal or naval-base state with a foreign neighbor |
| Result delay | `35` days |
| Callback delay | `270` days |

## Source evidence

The producer block in `common/scripted_effects/fallout_world_end_event_candidate_effects.txt` initializes the dedicated ledgers, selects the lowest eligible state, and appends one candidate row with candidate `789`, transaction `710084`, route `7200`, Fuel resource pressure, Air Winter severity, state subject type, and the selected target state.

`common/scripted_triggers/fallout_world_end_pirate_amnesty_event_triggers.txt` authenticates the current West African Port Confederacies maritime-remnant row, current generation, owner, controller, target state, foreign neighbor, Supply Access, survival resources, Air Winter, the closed Harbor Without a City memory, and all branch affordability checks.

`common/scripted_effects/fallout_world_end_pirate_amnesty_event_effects.txt` freezes target and neighbor receipts, pays and refunds branch costs, resolves deterministic result and callback grades, uses bounded Deaths requests with cause `fallout_aftermath`, writes Air Winter and Supply Access consequences, records branch-aware memories, schedules hidden AI and human delayed lanes, appends the survivor Event Log payload, and closes through authenticated idempotent cleanup.

`events/fallout_world_end_events.txt` defines the human opening, hidden AI opening, human and hidden AI result, human and hidden AI callback, and cleanup blocks with the dedicated `GFX_report_event_fallout_pirate_amnesty` picture on visible lanes.

The dedicated scripted localisation maps history `9190` payloads to branch and outcome detail. Shared Event Log routing maps history `9190` to `fallout.event_log.pirate_amnesty` for both the detail and name surfaces.

## Static checks recorded

The source package has one unique event block for each id `789` through `795`. Dedicated scripted effect, trigger, modifier, opinion, Event Log, localisation, sprite, and report DDS references are present. The localisation file is UTF-8 with BOM. The report source is retained at `docs/assets/789_pirate_amnesty/pirate_amnesty_source.png`, processed art is `210` by `176`, and the runtime DDS has a `DDS ` header with `147968` bytes.

The chain remains dormant and outside release-floor credit. Scheduler activation, host authority, save recovery, delayed delivery, multiplayer behavior, Deaths readback, runtime Event Log rendering, and player-visible art remain unproven because Hearts of Iron IV was not launched.

## Read-only Event Inspector evidence

The focused Event Inspector lint for `chaosx.fallout.789` returned `EVENT_INSPECTED_PARTIAL` with `status=ok`, `blockingDiagnostics=0`, and a large-workspace deferral notice. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/327aa24d6a6f032a0f9124744994b5e0f95214408570bdc14ea5dccbf1a82190/0124d3da814d6b6936cf0dd4ad4e16880e104ec3391b67c3cd8fd03cfedd99de/event-lint-7b66d2203e4e.json`. This is read-only source evidence and not live campaign validation.
