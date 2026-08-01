# Reviewed Archetype Spec: The Ghost Convoy

## Identity

The Ghost Convoy is a dormant Fallout survivor chain for the maritime remnant archetype. It follows a closed Captain's Articles memory in the West African Port Confederacies and brings an unidentified convoy onto the old Atlantic sea road. The port council must decide how much contact to permit when the ships carry no visible registry and the coast has only one working signal mast. Fallout remains a terminal consequence and is not registered as an ordinary event, evolution, or ordinary super-event.

The chain uses candidate `775`, transaction `710082`, route `7196`, event ids `chaosx.fallout.775` through `chaosx.fallout.781`, and survivor Event Log history `9188`. It is authored under `add_namespace = chaosx.fallout` and remains outside release-floor credit while scheduler activation is unset.

## Eligibility and target proof

The candidate producer runs through the reviewed registry rebuild. It requires the current `fallout_government_archetype` of `maritime_remnant`, the `west_african_port_confederacies` country memory, and a current owned state carrying the closed Captain's Articles memory flag. The selected state must retain current identity and survival rows, Supply Access, surviving population, Shelter, Adaptation, Exposure, Disease, Air Winter values, and either a coast or a surviving naval base. It must have a foreign neighboring state with a current identity row. The owner must retain durable Medicine, Cohesion, Recognition, port-route ledgers, remain in the campaign-day window, and afford at least one branch.

Every opening, result, callback, and cleanup lane revalidates the ordinary receipt, transition generation, owner, controller, target state, and frozen foreign neighbor. The registry freezes the selected state and one lowest foreign neighbor before any cost, result, opinion, or Deaths write. A changed state, owner, controller, neighbor, country memory, Captain's Articles memory, or generation fails closed and releases through authenticated cleanup.

## Authored branches

| Branch | Local decision | Cost | Convoy-contact premise |
| --- | --- | --- | --- |
| Approach | Approach with a search skiff | Food 2, Medicine 1, Recognition 4 | Send a named crew toward the lead hull and ask for its route, cargo, and landing need. |
| Shadow | Shadow the convoy | Scrap 3, Power 2, Recognition 2 | Follow the ships from the old lighthouse without opening the harbor channel. |
| Avoid | Avoid the sea road | Fuel 3, Recognition 3, Cohesion 1 | Extinguish the harbor lights and keep the convoy beyond the reef. |
| Signal publicly | Signal from the mast | Food 2, Medicine 2, Fuel 3, Recognition 3 | Publish the port's names, berth rules, and distress signal across the old route. |

The human opening and hidden AI opening use the same branch affordability and deterministic grading inputs. Hidden AI uses authored branch priorities and cannot choose an unaffordable branch.

## Delayed results and callback

The result is scheduled forty-two days after the opening choice. Grading combines frozen Supply Access, Shelter, Adaptation, Disease, Exposure, Medicine, Recognition, port legitimacy, piracy pressure, rescue duty, prize-law funds, refugee berth pressure, and fleet fatigue, with a maritime-remnant government bonus. Every branch has distinct success, partial, and failure thresholds. Results update Air Winter disease, shelter, exposure, adaptation, reclamation, Supply Access, Medicine, Cohesion, Recognition, Stability, War Support, and the dedicated convoy ledgers. Failure uses the Fallout aftermath Deaths contract with a bounded request and may damage the target state's infrastructure.

The callback is scheduled three hundred days after the result. Its score reads current port legitimacy, Cohesion, Recognition, rescue duty, prize-law funds, Cause Memory, fleet fatigue, target-state Supply Access, Reclamation, and Disease. Success, partial, and failure update the same ledgers with route memories. Callback failure uses the same Deaths-backed contract and never writes to a stale target.

## Memory, diplomacy, and Event Log

Choice, result, and callback memories are written to the survivor country's Event Log through history `9188`. The dedicated detail resolver uses `GetFalloutEvent775EventLogDetail` and concrete West African port, lighthouse watch, reef channel, signal mast, convoy hull, and neighboring-government wording. The neighbor receives branch-specific opinion modifiers and state result flags. The chain creates no tag, transfers no ownership, and does not register Fallout as an event.

The chain owns these ledgers and flags:

- `fallout_ghost_convoy_port_legitimacy_current`
- `fallout_ghost_convoy_piracy_pressure_current`
- `fallout_ghost_convoy_rescue_duty`
- `fallout_ghost_convoy_prize_law_fund`
- `fallout_ghost_convoy_refugee_berth_pressure`
- `fallout_ghost_convoy_fleet_fatigue`
- `fallout_ghost_convoy_cause_memory`
- `fallout_ghost_convoy_*_memory` and `*_contested` branch flags

Cleanup releases target and neighbor reservation flags, delayed tickets, branch costs, temporary registry state, and frozen variables idempotently.

## Presentation and assets

The human opening, delayed result, and callback use `GFX_report_event_fallout_ghost_convoy`. The dedicated fictional report card is documented in `docs/assets/775_ghost_convoy/manifest.md` and registered in `interface/fallout_world_end.gfx`. Hidden AI lanes remain silent. No zombie asset, sprite, audio, path, or ordinary super-event surface is reused.

## Review boundary

Static source review covers event identity, candidate row, constants, scripted effects, scripted triggers, dynamic modifiers, opinion modifiers, Event Log routing, localisation, asset hashes, and cleanup references. The chain is dormant and does not claim scheduler activation, host authority, save recovery, multiplayer delivery, runtime Event Log rendering, or live report presentation. Hearts of Iron IV is not launched by this workflow.
