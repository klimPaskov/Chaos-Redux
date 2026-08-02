# Reviewed Archetype Spec: The Pirate Amnesty

The Pirate Amnesty is a dormant Fallout survivor chain for the maritime remnant archetype. It follows the closed Harbor Without a City state memory in the West African Port Confederacies and brings four raider crews to a working ash coast. Their charts and captured stores could restore the sea road, but their old violence cannot be forgotten. The port council must choose a conditional pardon, a privateer charter, a public trial, or exile beyond the reef.

Fallout remains a terminal consequence and is not registered as an ordinary event, evolution, or ordinary super-event. This chain is survivor-country content that becomes eligible only through the Fallout-owned candidate registry and scheduler.

## Candidate and admission

The reviewed candidate is `789` with transaction key `710084`, route `7200`, route upper bound `7201`, and survivor Event Log history `9190`. The event blocks are `chaosx.fallout.789` through `chaosx.fallout.795`. The human opening is `789`, the hidden AI opening is `790`, the delayed result pair is `791` and `792`, the callback pair is `793` and `794`, and cleanup is `795`.

The candidate producer runs through the reviewed registry rebuild. It requires the current `fallout_government_archetype` value `maritime_remnant`, country memory `west_african_port_confederacies`, and Sub-Saharan Africa. The selected target is the lowest owned current coastal state or state with a surviving naval base that carries the closed Harbor Without a City memory `fallout_event_782_memory_closed`. The state must retain current identity and survival rows, Supply Access, surviving population, Shelter, Adaptation, Exposure, Disease, Air Winter, and a foreign neighboring state with a current identity row.

The owner must retain durable Medicine, Cohesion, Recognition, and the dedicated raider ledgers. The country remains inside the campaign-day window from `4200` through `9600` and must afford at least one complete branch. The row remains dormant because both scheduler activation flags remain unset.

## Frozen ledgers and branch costs

The opening freezes transition generation, owner, controller, target state, foreign neighbor, Air Winter, Supply Access, and the raider ledgers. The dedicated country variables are `fallout_pirate_amnesty_crew_legitimacy_current`, `fallout_pirate_amnesty_piracy_pressure_current`, `fallout_pirate_amnesty_escort_trust`, `fallout_pirate_amnesty_prize_law_fund`, `fallout_pirate_amnesty_crew_capacity`, `fallout_pirate_amnesty_seized_stores`, and `fallout_pirate_amnesty_raid_memory`.

The four branches use distinct costs.

| Branch | Cost | Intended identity |
|---|---|---|
| Conditional amnesty | Food 2, Medicine 2, Recognition 2 | Register the crews under a rescue oath and return named cargo. |
| Privateer service | Fuel 2, Recognition 3, Cohesion 2 | Issue a fixed patrol charter and prize ledger. |
| Public trial | Scrap 2, Power 2, Medicine 2 | Secure witnesses, inspect holds, and hold a public prize court. |
| Reef exile | Food 2, Fuel 2, Recognition 2 | Escort the crews away and preserve their charts in the archive. |

The player-facing opening, branch tooltips, delayed results, callback, Event Log detail, and cleanup wording are in `localisation/english/fallout_world_end_pirate_amnesty_l_english.yml`.

## Resolution contract

The result resolves after exactly `35` days. The callback resolves after exactly `270` days. The result uses frozen state and country values plus branch thresholds. The callback uses current same-generation Air Winter, Supply Access, survival, and raider ledgers. Success, partial, and failure outcomes are deterministic with a fixed branch tie order.

Failure losses are routed through the Deaths system with cause `fallout_aftermath`. The result and callback write bounded Air Winter state effects, Supply Access changes, survival-resource changes, native infrastructure damage on failure, branch-aware country memories, state memory `fallout_event_789_memory_closed`, bilateral opinion memory, and survivor Event Log payloads. The chain never writes the Fallout transition, blackout, population sweep, or Air Cleanliness state as an ordinary event.

The hidden AI route uses the same branch affordability, frozen receipts, deterministic grading, delayed tokens, outcome effects, and cleanup. Cleanup is idempotent and refuses stale owner, controller, target, neighbor, generation, or ordinary-receipt rows before releasing reservations.

## Source and asset wiring

| Surface | File |
|---|---|
| Constants | `common/script_constants/fallout_world_end_pirate_amnesty_constants.txt` |
| Effects | `common/scripted_effects/fallout_world_end_pirate_amnesty_event_effects.txt` |
| Triggers | `common/scripted_triggers/fallout_world_end_pirate_amnesty_event_triggers.txt` |
| Dynamic modifiers | `common/dynamic_modifiers/fallout_world_end_pirate_amnesty_dynamic_modifiers.txt` |
| Opinion modifiers | `common/opinion_modifiers/fallout_pirate_amnesty_opinion_modifiers.txt` |
| Event script | `events/fallout_world_end_events.txt` |
| Event Log scripted localisation | `common/scripted_localisation/fallout_world_end_pirate_amnesty_event_log_scripted_localisation.txt` |
| Shared Event Log routing | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` |
| Localisation | `localisation/english/fallout_world_end_pirate_amnesty_l_english.yml` |
| Sprite registration | `interface/fallout_world_end.gfx` |
| Runtime report DDS | `gfx/event_pictures/fallout/report_event_fallout_pirate_amnesty.dds` |

The dedicated asset manifest and handoff are under `docs/assets/789_pirate_amnesty/`.

## Review status

The chain is statically wired and dormant. It is outside release-floor credit until scheduler activation, save recovery, multiplayer behavior, Deaths readback, and runtime Event Log rendering are reviewed in a live campaign by the user.

