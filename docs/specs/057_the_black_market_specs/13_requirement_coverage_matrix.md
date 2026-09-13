# Requirement Coverage Matrix

| Accepted requirement | Main specification location | Coverage |
| --- | --- | --- |
| Event ID `57`, The Black Market | `01_core_event_spec.md` | Complete |
| Minor Fire-Once | `01_core_event_spec.md`, `08_event_chain_logs_localisation_and_catalog_alignment.md` | One firing creates the persistent runtime |
| Chaos level `1` | `01_core_event_spec.md`, `08_event_chain_logs_localisation_and_catalog_alignment.md` | Complete |
| Positive Economy, High member | `06_evolutions_chaos_cluster_and_connections.md` | Complete |
| Small secret founding group | `01_core_event_spec.md` | Two to four founders, targeting three |
| Invitation-only membership | `02_membership_secrecy_and_government_postures.md` | Complete membership state machine |
| Outsiders receive no member category | `01_core_event_spec.md`, `05_decisions_missions_and_player_loop.md` | Outsider counterplay requires local evidence |
| Membership grows gradually | `02_membership_secrecy_and_government_postures.md` | One sponsored invitation per bounded pulse |
| Ideology and government policy affect eligibility | `02_membership_secrecy_and_government_postures.md` | Contextual scores and posture routes |
| Economic isolation, embargoes, and sanctions matter | `02_membership_secrecy_and_government_postures.md`, `06_evolutions_chaos_cluster_and_connections.md` | Demand, acceptance, routes, and Event 50 connection |
| War affects membership and trade | `02_membership_secrecy_and_government_postures.md`, `07_ai_probability_balance_and_edge_cases.md` | Demand, route risk, hostile transactions, and AI |
| Access to members and smuggling opportunities matter | `02_membership_secrecy_and_government_postures.md`, `03_smuggling_routes_and_network_growth.md` | Sponsor and route proof required |
| Repression, tolerance, previous dealings, and relations matter | `02_membership_secrecy_and_government_postures.md` | Candidate scoring, trust, and government postures |
| Some routes can be incompatible | `02_membership_secrecy_and_government_postures.md` | Hard blockers and changing circumstances |
| Members can lose access | `02_membership_secrecy_and_government_postures.md` | Dormancy, suspension, withdrawal, expulsion, and reconnection |
| Hidden member decision category | `05_decisions_missions_and_player_loop.md` | One category with phase replacement |
| Rotating and expanding inventory | `04_inventory_trade_and_provider_api.md` | Three to six slots with dynamic cadence |
| Infantry equipment | `04_inventory_trade_and_provider_api.md` | Baseline source-backed offers |
| Artillery and support equipment | `04_inventory_trade_and_provider_api.md` | Baseline validated concrete tokens |
| Trucks and trains | `04_inventory_trade_and_provider_api.md` | Baseline logistics offers and reserves |
| Fuel | `04_inventory_trade_and_provider_api.md` | Consumption-day scaling and route limits |
| Convoys | `04_inventory_trade_and_provider_api.md` | Member, captured, commercial, and Event 56 sources |
| Tanks and aircraft | `04_inventory_trade_and_provider_api.md`, `06_evolutions_chaos_cluster_and_connections.md` | Evolution I with heavy-cargo validation |
| Foreign and captured equipment | `04_inventory_trade_and_provider_api.md` | Small baseline lots and larger evolved packages |
| Large surplus stockpiles | `04_inventory_trade_and_provider_api.md` | Evolution I and exceptional Evolution III handling |
| Intelligence | `04_inventory_trade_and_provider_api.md` | Baseline through strategic evolved packages |
| Stolen industrial material | `04_inventory_trade_and_provider_api.md` | Supported temporary procurement contracts |
| Defeated and collapsed-country equipment | `04_inventory_trade_and_provider_api.md` | Owner receipt before source data disappears |
| Members sell surplus | `04_inventory_trade_and_provider_api.md`, `05_decisions_missions_and_player_loop.md` | Protected reserves, source debit, and sale flow |
| Ideology, faction, hostility, war, and embargo do not automatically ban trade | `01_core_event_spec.md`, `02_membership_secrecy_and_government_postures.md` | A valid underground route can still support a transaction |
| Land-border routes | `03_smuggling_routes_and_network_growth.md` | Complete route family |
| Neutral intermediaries | `03_smuggling_routes_and_network_growth.md` | Relay nodes without full membership |
| Ports and merchant shipping | `03_smuggling_routes_and_network_growth.md` | Maritime route family |
| Occupied territory | `03_smuggling_routes_and_network_growth.md` | Occupied-corridor route family |
| International trade corridors | `03_smuggling_routes_and_network_growth.md` | Event 55 adapter |
| Covert air transport | `03_smuggling_routes_and_network_growth.md` | Small high-risk evolved cargo |
| Route disruption by war, blockade, territory, intelligence, and crackdowns | `03_smuggling_routes_and_network_growth.md` | Dirty refresh and route states |
| Invite new countries | `02_membership_secrecy_and_government_postures.md` | Complete |
| Reconnect former members | `02_membership_secrecy_and_government_postures.md` | Complete |
| Open and join routes | `03_smuggling_routes_and_network_growth.md` | Complete |
| Increase deal size and categories | `04_inventory_trade_and_provider_api.md`, `06_evolutions_chaos_cluster_and_connections.md` | Complete |
| Connect separated regional sections | `03_smuggling_routes_and_network_growth.md` | Regional cell graph and interregional links |
| Evolution I at `200+` | `06_evolutions_chaos_cluster_and_connections.md` | International Network with paced readiness |
| Evolution II at `400+` | `06_evolutions_chaos_cluster_and_connections.md` | Underground Economy with owner providers |
| Evolution III at `600+` | `06_evolutions_chaos_cluster_and_connections.md` | Anything Has a Price and Grand Auctions |
| Experimental and unusual equipment needs approval | `04_inventory_trade_and_provider_api.md` | Versioned fail-closed provider API |
| Source event or project remains incomplete | `04_inventory_trade_and_provider_api.md`, `10_implementation_acceptance_and_validation.md` | Completion isolation is mandatory |
| Event 50 connection | `06_evolutions_chaos_cluster_and_connections.md` | Demand, invitation, route, and Chaos interaction |
| Event 54 connection | `04_inventory_trade_and_provider_api.md`, `06_evolutions_chaos_cluster_and_connections.md` | Advanced circulation without free stock creation |
| Event 56 connection | `04_inventory_trade_and_provider_api.md`, `06_evolutions_chaos_cluster_and_connections.md` | Owner-approved naval packages |
| Wars, occupations, collapse, and surrender create supply | `04_inventory_trade_and_provider_api.md` | Source-backed provider receipts |
| Event 55 ports and corridors create routes | `03_smuggling_routes_and_network_growth.md`, `06_evolutions_chaos_cluster_and_connections.md` | Complete |
| Future events can expose trade packages | `04_inventory_trade_and_provider_api.md` | Public owner provider contract |
| Dynamic costs, durations, chance, and AI | `07_ai_probability_balance_and_edge_cases.md` | Centralized factors and ten probability scenarios |
| Event log and evolutions | `08_event_chain_logs_localisation_and_catalog_alignment.md` | Sanitized history and three logged stages |
| Assets | `09_assets_and_achievements.md` | Report pictures, category art, icons, texticon, and achievement triplets |
| Achievements | `09_assets_and_achievements.md` | Seven exact designs |
| Implementation and validation | `10_implementation_acceptance_and_validation.md` | Twenty acceptance scenarios and audit order |
| Improvement-loop review | `11_improvement_loop_closure.md` | Closure reached, broad expansion deferred |
| Subagent role review | `12_specialist_review_record.md` | Every supplied role assessed, runtime failure disclosed |
