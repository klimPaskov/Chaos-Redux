# CBRN Operations surface

## Player-facing surface

Chaos Warfare uses the native decision-category presentation accepted by Stage 11 of the implementation plan. The `cbrn_operations_category` category is the national command surface for doctrine establishment, Chemical Readiness, use policy, headquarters preparation, and conditional technology commissions. Related categories expose procurement, civil defence, occupation measures, and international response without duplicating the same transaction.

The category uses native decision targeting, exact-state targets, trigger tooltips, AI scoring, cooldowns, and cleanup. The existing Chaos Meter tabs remain the readout for global contamination, while the CBRN decision categories provide the operation controls.

All CBRN categories are dormant at new-game startup. Starting technologies, facilities, stockpiles, reserves, and inherited doctrine remain intact but do not reveal decision surfaces by themselves. Post-start CBRN research, Chaos Warfare adoption, completion of an ordinary biological-agent or nerve-agent project, activation of the Mengele pathogen-cadre or Unconventional Warfare successor route, or a live alert, contamination, outbreak, evidence record, inspection demand, or sanction activates only the relevant family. Empty categories remain hidden.

Routine civilian mask issue, full distribution, filter replacement, and occupied-population supply use one national timed card per program. At completion, each program applies the existing population-scaled state transaction to eligible controlled states while real stock remains, serving the capital first where applicable. A program cancels and releases its shared lock if stock is exhausted or no eligible work remains. Exact-state cards are retained only where the player is responding to or selecting a real local incident or operation.

## Category mapping

| Surface | Native category | Responsibility |
| --- | --- | --- |
| Command and doctrine | `cbrn_operations_category` | Institution, doctrine, use policy, readiness, HQ preparation, and conditional commissions. |
| National protection | `cbrn_program_management_category` | Gas-mask models, filters, reserves, issue, maintenance, and national procurement. |
| Civilian protection | `cbrn_civil_defence_category` | National population-scaled distribution and filter programs, plus exact-state alarms, shelters, emergency issue, and medical response for live incidents. |
| International response | `cbrn_international_response_category` | Inspections, sanctions, protective aid, retaliation, and stockpile destruction. |
| Occupation measures | `cbrn_occupation_measures_category` | Coercive Security authorization and exact-state nerve-agent suppression. |
| Chemical battlefield release | state-targeted decisions plus native chemical raids | Explicit target-state operations. Idle aircraft and continuous missions never call the exposure pipeline. |
| Biological release | native biological raids, exact covert sabotage surfaces, Japan-China decisions, and the doomsday decision | Route-specific deployment. The four ordinary agents share lifecycle helpers but not delivery success odds. |

## Visible values and tooltip contract

The category decisions expose current resources and requirements through native decision tooltips: Chemical Readiness, Command Power, payload lots, support equipment, gas-mask reserve and filter condition, decontamination equipment, medical capacity, headquarters and regimental support, cooldowns, route shortage, selected state, selected agent, evidence, attribution, contamination, Condemnation, and cleanup. A transaction must repeat its exact target, payload, policy, protection, and consequence gates in the completion effect.

The operation category does not authorize a delivery by itself. Headquarters preparation supplies authorization and preparation. Delivery surfaces consume payload and dispatch the shared chemical or biological lifecycle. Doctrine may make an authorized CBRN action more potent and reduce its Condemnation impact, but it does not erase evidence, attribution, deaths, contamination, medical saturation, resistance trauma, or responsibility.

## Engine boundaries

The custom scripted-GUI window described as optional in the implementation surface map is not used. Stage 11 explicitly permits the native decision-category surface. The timed chemical battlefield family remains registered but fail-closed because the current build does not provide a verified selected-state weather/terrain receipt. Continuous chemical-air contamination is also fail-closed until eligible mission activity can be proven; aircraft presence or idleness never counts as delivery.

The five battlefield-operation DDS outputs are packaged and registered at their dedicated decision paths, with provenance and final-size validation in the Stage 6 asset manifest. No placeholder, resized cross-type substitute, or silent fallback is accepted. Asset completion does not relax the fail-closed engine-hook gate.
