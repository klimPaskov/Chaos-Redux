# Reviewed Archetype Spec: The Captain's Articles

## Identity

The Captain's Articles is a dormant Fallout survivor chain for the maritime remnant archetype. It follows the West African Port Confederacies memory and asks a working Atlantic port to decide how rescue duty, salvaged cargo, armed patrols, and crew authority will be recorded. The chain treats the port as a political community shaped by ash, cold rain, scarce fuel, and displaced families. Fallout remains a terminal consequence and is not registered as an ordinary event, evolution, or ordinary super-event.

The chain uses candidate `768`, transaction `710081`, route `7194`, event ids `chaosx.fallout.768` through `chaosx.fallout.774`, and survivor Event Log history `9187`. It is authored under `add_namespace = chaosx.fallout` and remains outside release-floor credit while scheduler activation is unset.

## Eligibility and target proof

The candidate producer runs through the reviewed registry rebuild. It first requires a current `fallout_government_archetype` of `maritime_remnant` and `fallout_country_memory_id` `west_african_port_confederacies`. It initializes the dedicated port ledgers before selecting the lowest owned state id with current identity and survival rows, current Supply Access, surviving population, usable Shelter, Adaptation, Exposure, Disease, Air Winter values, and either a coastal state or a state with a surviving naval base. The owner must retain durable Medicine, Cohesion, Recognition, port legitimacy, piracy pressure, and registry rows, remain in the campaign-day window, and afford at least one branch.

Every opening, result, callback, and cleanup lane revalidates the ordinary receipt, transition generation, owner, controller, target state, and frozen foreign neighbor. The registry freezes the selected state and one lowest foreign neighbor before any cost, result, opinion, or Deaths write. A changed state, owner, controller, neighbor, country memory, or generation fails closed and releases through authenticated cleanup.

## Authored branches

| Branch | Local decision | Cost | Port-law premise |
| --- | --- | --- | --- |
| Rescue articles | Write the rescue articles | Food 3, Medicine 1, Recognition 3 | Make a family berth and a fuel allotment a public rescue duty with a named return roster. |
| Prize court | Seat a prize court | Scrap 2, Power 3, Recognition 3 | Hear salvaged-cargo disputes in public before private seizure becomes port law. |
| Harbor muster | Call a harbor muster | Fuel 4, Recognition 2, Cohesion 2 | Put armed patrols under an accountable harbor council while the anchorage remains exposed. |
| Fleet split | Split the fleet by vote | Food 2, Medicine 3, Fuel 2, Recognition 2 | Let crews form a separate rescue flotilla before a single command turns coercive. |

The human opening and hidden AI opening use the same branch affordability and deterministic grading inputs. Hidden AI uses authored branch priorities and cannot choose an unaffordable branch.

## Delayed results and callback

The result is scheduled forty-two days after the opening choice. Grading combines frozen Supply Access, Shelter, Adaptation, Disease, Exposure, Medicine, Recognition, port legitimacy, piracy pressure, rescue duty, refugee berth pressure, and a maritime-remnant civic bonus. Every branch has distinct success, partial, and failure thresholds. Results update Air Winter disease, shelter, exposure, adaptation, reclamation, Supply Access, Medicine, Cohesion, Recognition, Stability, War Support, and the dedicated port ledgers. Failure uses the Fallout aftermath Deaths contract with a bounded request and may damage the target state's infrastructure.

The callback is scheduled three hundred days after the result. Its score reads current port legitimacy, Cohesion, Recognition, rescue duty, prize-law funds, Cause Memory, target-state Supply Access, Reclamation, and Disease. Success, partial, and failure update the same ledgers with separate port-law memories. Callback failure uses the same Deaths-backed contract and never writes to a stale target.

## Memory, diplomacy, and Event Log

Choice, result, and callback memories are written to the survivor country's Event Log through history `9187`. The dedicated detail resolver uses `GetFalloutEvent768EventLogDetail` and concrete West African port, rescue berth, prize hearing, harbor council, crew vote, and neighboring-government wording. The neighbor receives branch-specific opinion modifiers and state result flags. The chain creates no tag, transfers no ownership, and does not register Fallout as an event.

The chain owns these ledgers and flags:

- `fallout_captains_articles_port_legitimacy_current`
- `fallout_captains_articles_piracy_pressure_current`
- `fallout_captains_articles_rescue_duty`
- `fallout_captains_articles_prize_law_fund`
- `fallout_captains_articles_refugee_berth_pressure`
- `fallout_captains_articles_fleet_fatigue`
- `fallout_captains_articles_cause_memory`
- `fallout_captains_articles_*_memory` and `*_contested` branch flags

Cleanup releases target and neighbor reservation flags, delayed tickets, branch costs, temporary registry state, and frozen variables idempotently.

## Presentation and assets

The human opening, delayed result, and callback use `GFX_report_event_fallout_captains_articles`. The dedicated fictional report card is documented in `docs/assets/768_captains_articles/manifest.md` and registered in `interface/fallout_world_end.gfx`. Hidden AI lanes remain silent. No zombie asset, sprite, audio, path, or ordinary super-event surface is reused.

## Review boundary

Static source review covers event identity, candidate row, constants, scripted effects, scripted triggers, dynamic modifiers, opinion modifiers, Event Log routing, localisation, asset hashes, and cleanup references. The chain is dormant and does not claim scheduler activation, host authority, save recovery, multiplayer delivery, runtime Event Log rendering, or live report presentation. Hearts of Iron IV is not launched by this workflow.
