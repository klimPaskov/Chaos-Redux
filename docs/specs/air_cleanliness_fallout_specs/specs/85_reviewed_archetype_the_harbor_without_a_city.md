# Reviewed Archetype Spec: The Harbor Without a City

## Identity

The Harbor Without a City is a dormant Fallout survivor chain for the maritime remnant archetype. It follows a closed Ghost Convoy memory in the West African Port Confederacies after inland authority disappears from the harbor road. The port council must decide whether the working piers become a republic, bind themselves to inland wards, accept a garrison, or evacuate the remaining families and records. Fallout remains a terminal consequence and is not registered as an ordinary event, evolution, or ordinary super-event.

The chain uses candidate `782`, transaction `710083`, route `7198`, event ids `chaosx.fallout.782` through `chaosx.fallout.788`, and survivor Event Log history `9189`. It is authored under `add_namespace = chaosx.fallout` and remains outside release-floor credit while scheduler activation is unset.

## Eligibility and target proof

The candidate producer runs through the reviewed registry rebuild. It requires the current `fallout_government_archetype` of `maritime_remnant`, the `west_african_port_confederacies` country memory, and a current owned state carrying the closed Ghost Convoy memory flag. The selected state must retain current identity and survival rows, Supply Access, surviving population, Shelter, Adaptation, Exposure, Disease, Air Winter values, and either a coast or a surviving naval base. It must have a foreign neighboring state with a current identity row. The owner must retain durable Medicine, Cohesion, Recognition, harbor ledgers, remain in the campaign-day window, and afford at least one branch.

Every opening, result, callback, and cleanup lane revalidates the ordinary receipt, transition generation, owner, controller, target state, and frozen foreign neighbor. The registry freezes the selected state and one lowest foreign neighbor before any cost, result, opinion, or Deaths write. A changed state, owner, controller, neighbor, country memory, Ghost Convoy memory, or generation fails closed and releases through authenticated cleanup.

## Authored branches

| Branch | Local decision | Cost | Harbor-governance premise |
| --- | --- | --- | --- |
| Port republic | Build a port republic | Food 3, Medicine 2, Recognition 2 | Elect a dock council that keeps the cranes, berth rules, food reserve, and lighthouse under a named civic register. |
| Inland alliance | Bind an inland alliance | Scrap 2, Power 3, Recognition 3 | Share the harbor stores and road seal with named inland wards without pretending the capital returned. |
| Military occupation | Accept military occupation | Fuel 2, Recognition 3, Cohesion 2 | Let a garrison control the gates and cranes while the port keeps a limited civilian quay. |
| Evacuate | Evacuate the harbor | Food 3, Medicine 2, Fuel 2, Recognition 2 | Move families, tools, clinic ledgers, and berth records onto the surviving convoy route. |

The human opening and hidden AI opening use the same branch affordability and deterministic grading inputs. Hidden AI uses authored branch priorities and cannot choose an unaffordable branch.

## Delayed results and callback

The result is scheduled forty-five days after the opening choice. Grading combines frozen Supply Access, Shelter, Adaptation, Disease, Exposure, Medicine, Recognition, harbor authority, inland grievance, garrison trust, evacuee capacity, and maritime-remnant government strength. Every branch has distinct success, partial, and failure thresholds. Results update Air Winter disease, shelter, exposure, adaptation, reclamation, Supply Access, Medicine, Cohesion, Recognition, Stability, War Support, and the dedicated harbor ledgers. Failure uses the Fallout aftermath Deaths contract with a bounded request and may damage the target state's infrastructure.

The callback is scheduled three hundred thirty days after the result. Its score reads current harbor authority, Cohesion, Recognition, garrison trust, claim pressure, Cause Memory, target-state Supply Access, Reclamation, Disease, inland grievance, evacuee capacity, and port food reserve. Success, partial, and failure update the same ledgers with government memories. Callback failure uses the same Deaths-backed contract and never writes to a stale target.

## Memory, diplomacy, and Event Log

Choice, result, and callback memories are written to the survivor country's Event Log through history `9189`. The dedicated detail resolver uses `GetFalloutEvent782EventLogDetail` and concrete dock council, inland road, garrison gate, lighthouse, clinic ledger, and convoy evacuation wording. The neighbor receives branch-specific opinion modifiers and state result flags. The chain creates no tag, transfers no ownership, and does not register Fallout as an event.

The chain owns these ledgers and flags:

- `fallout_harbor_without_city_authority_current`
- `fallout_harbor_without_city_inland_grievance_current`
- `fallout_harbor_without_city_garrison_trust`
- `fallout_harbor_without_city_claim_pressure_fund`
- `fallout_harbor_without_city_evacuee_capacity`
- `fallout_harbor_without_city_port_food_reserve`
- `fallout_harbor_without_city_cause_memory`
- `fallout_harbor_without_city_*_memory` and `*_contested` branch flags

Cleanup releases target and neighbor reservation flags, delayed tickets, branch costs, temporary registry state, and frozen variables idempotently.

## Presentation and assets

The human opening, delayed result, and callback use `GFX_report_event_fallout_harbor_without_city`. The dedicated fictional report card is documented in `docs/assets/782_harbor_without_city/manifest.md` and registered in `interface/fallout_consolidated.gfx`. Hidden AI lanes remain silent. No zombie asset, sprite, audio, path, or ordinary super-event surface is reused.

## Review boundary

Static source review covers event identity, candidate row, constants, scripted effects, scripted triggers, Event Log routing, localisation, asset hashes, and cleanup references. The chain is dormant and does not claim scheduler activation, host authority, save recovery, multiplayer delivery, runtime Event Log rendering, or live report presentation. Hearts of Iron IV is not launched by this workflow.
