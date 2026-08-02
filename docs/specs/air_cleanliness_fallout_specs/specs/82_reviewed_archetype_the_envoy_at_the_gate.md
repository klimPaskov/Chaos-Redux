# Reviewed Archetype Spec: The Envoy at the Gate

## Identity

The Envoy at the Gate is a dormant Fallout survivor chain for the fictional mutant polity archetype. It follows the Congo Green Basin memory and gives the altered river council its first formal contact with a foreign government. The altered community is fictional high-chaos content. The text treats its people as a political community and does not present fictional traits as ordinary radiation science. Fallout remains a terminal consequence and is not registered as an ordinary event, evolution, or ordinary super-event.

The chain uses candidate `761`, transaction `710080`, route `7192`, event ids `chaosx.fallout.761` through `chaosx.fallout.767`, and survivor Event Log history `9186`. It is authored under `add_namespace = chaosx.fallout` and remains outside release-floor credit while scheduler activation is unset.

## Eligibility and target proof

The candidate producer runs through the reviewed registry rebuild. It first requires a current `fallout_government_archetype` of `mutant_polity` and `fallout_country_memory_id` `congo_green_basin`. It initializes the dedicated envoy ledgers before selecting the lowest owned state id with current identity and survival rows, current Supply Access, surviving population, usable Shelter, Adaptation, Exposure, Disease, and Air Winter values, plus at least one foreign neighboring state. The owner must retain durable Medicine, Cohesion, Recognition, and registry rows, remain in the campaign-day window, and afford at least one branch.

Every opening, result, callback, and cleanup lane revalidates the ordinary receipt, transition generation, owner, controller, target state, and frozen foreign neighbor. The registry freezes the selected state and one lowest foreign neighbor before any cost, result, opinion, or Deaths write. A changed state, owner, controller, neighbor, country memory, or generation fails closed and releases through authenticated cleanup.

## Authored branches

| Branch | Local decision | Cost | River-gate premise |
| --- | --- | --- | --- |
| Open recognition | Open recognition | Food 3, Medicine 1, Recognition 3 | Publish a reciprocal rights charter and give the envoy a public seat. |
| Medical inspection | Offer a voluntary inspection | Scrap 2, Power 3, Recognition 3 | Let both sides inspect records by consent, with no detention and matching terms. |
| Symbolic meeting | Hold a symbolic meeting | Fuel 4, Recognition 2, Cohesion 2 | Meet on the bridge and exchange seals without opening settlement access. |
| Refuse contact | Refuse contact | Food 2, Medicine 3, Fuel 2, Recognition 2 | Close the gate, record the refusal, and return the envoy by a named route. |

The human opening and hidden AI opening use the same branch affordability and deterministic grading inputs. Hidden AI uses authored branch priorities and cannot choose an unaffordable branch.

## Delayed results and callback

The result is scheduled forty-two days after the opening choice. Grading combines frozen Supply Access, Shelter, Adaptation, Disease, Exposure, Medicine, Recognition, Corridor Security, Refugee Pressure, Border Fatigue, and a small mutant-polity civic bonus. Every branch has distinct success, partial, and failure thresholds. Results update Air Winter disease, shelter, exposure, adaptation, reclamation, Supply Access, Medicine, Cohesion, Recognition, Stability, War Support, and the dedicated envoy ledgers. Failure uses the Fallout aftermath Deaths contract with a bounded request and may damage the target state's infrastructure.

The callback is scheduled three hundred days after the result. Its score reads current civic legitimacy, external pressure, Corridor Security, Partner Trust, Cause Memory, Refugee Pressure, Border Fatigue, target-state Supply Access, Reclamation, and Disease. Success, partial, and failure update the same ledgers with separate bilateral memories. Callback failure uses the same Deaths-backed contract and never writes to a stale target.

## Memory, diplomacy, and Event Log

Choice, result, and callback memories are written to the survivor country's Event Log through history `9186`. The dedicated detail resolver uses `GetFalloutEvent761EventLogDetail` and concrete Congo Green Basin, river gate, bridge seal, consent, medicine, liaison, and neighboring-government wording. The neighbor receives branch-specific opinion modifiers and state result flags. The chain creates no tag, transfers no ownership, and does not register Fallout as an event.

The chain owns these ledgers and flags:

- `fallout_mutant_envoy_gate_civic_legitimacy_current`
- `fallout_mutant_envoy_gate_external_pressure_current`
- `fallout_mutant_envoy_gate_corridor_security`
- `fallout_mutant_envoy_gate_partner_trust_fund`
- `fallout_mutant_envoy_gate_refugee_pressure`
- `fallout_mutant_envoy_gate_border_fatigue`
- `fallout_mutant_envoy_gate_cause_memory`
- `fallout_mutant_envoy_gate_*_memory` and `*_contested` branch flags

Cleanup releases target and neighbor reservation flags, delayed tickets, branch costs, temporary registry state, and frozen variables idempotently.

## Presentation and assets

The human opening, delayed result, and callback use `GFX_report_event_fallout_mutant_envoy_at_gate`. The dedicated fictional report card is documented in `docs/assets/761_mutant_envoy_at_gate/manifest.md` and registered in `interface/fallout_consolidated.gfx`. Hidden AI lanes remain silent. No zombie asset, sprite, audio, path, or ordinary super-event surface is reused.

## Review boundary

Static source review covers event identity, candidate row, constants, scripted effects, scripted triggers, dynamic modifiers, opinion modifiers, Event Log routing, localisation, asset hashes, and cleanup references. The chain is dormant and does not claim scheduler activation, host authority, save recovery, multiplayer delivery, runtime Event Log rendering, or live report presentation. Hearts of Iron IV is not launched by this workflow.
