# Event 57: The Black Market

This package defines the full planning specification for Chaos Redux Event 57, **The Black Market**.

The event is a `Minor Fire-Once` event at Chaos level `1`. Its first firing creates a persistent, invitation-only international smuggling network. The random event itself never repeats. Later membership growth, inventory rotations, route failures, investigations, transactions, and evolutions belong to the event-owned runtime.

## Accepted catalog identity

| Field | Accepted value |
| --- | --- |
| Event ID | `57` |
| Event name | `The Black Market` |
| Event type | `Minor Fire-Once` |
| Status before implementation | `To Be Reworked` |
| Chaos level | `1` |
| Cluster | `Positive Economy` |
| Cluster role | `High member` |

The supplied event catalog export still assigns Event 57 to an older Radar entry. The supplied cluster export also predates the accepted Black Market membership. Implementation must update the authoritative catalog workbook and regenerate its CSV exports. The CSV files are evidence snapshots and must not be edited directly.

## Package map

| File | Purpose |
| --- | --- |
| `00_source_and_research_record.md` | Reading record, source conflicts, research boundaries, and subagent execution status |
| `01_core_event_spec.md` | Event promise, first firing, founding network, public state, lifecycle, and player experience |
| `02_membership_secrecy_and_government_postures.md` | Membership states, invitation logic, awareness, secrecy, postures, withdrawal, and expulsion |
| `03_smuggling_routes_and_network_growth.md` | Route graph, delivery paths, disruption, reconstruction, exposure, and network reach |
| `04_inventory_trade_and_provider_api.md` | Offer generation, real stockpile transfers, Market Credit, seller safeguards, technology rules, and owner APIs |
| `05_decisions_missions_and_player_loop.md` | Member category, decisions, missions, outsider counterplay, action budgets, and transaction outcomes |
| `06_evolutions_chaos_cluster_and_connections.md` | Three evolutions, Chaos map, Positive Economy cluster behavior, and event connections |
| `07_ai_probability_balance_and_edge_cases.md` | AI plans, named probability scenarios, balance anchors, exploit controls, and edge cases |
| `08_event_chain_logs_localisation_and_catalog_alignment.md` | Event chain roles, event log behavior, text direction, documentation, and workbook alignment |
| `09_assets_and_achievements.md` | Complete accepted asset inventory and seven achievement designs |
| `10_implementation_acceptance_and_validation.md` | File map, acceptance scenarios, DLC coverage, audit order, and completion proof |
| `11_improvement_loop_closure.md` | Final depth review, accepted limits, and closure handoff |
| `12_specialist_review_record.md` | Role-by-role internal review and future subagent routing |
| `13_requirement_coverage_matrix.md` | Direct mapping from the accepted brief to the specification files |
| `research/historical_design_anchors.md` | Historical findings translated into design rules |
| `research/bibliography.md` | Web sources used for the historical design pass |
| `prompts/` | Bounded implementation, asset, achievement, decision, scripted-system, AI, localisation, catalog, and completion prompts |

`057_the_black_market_full_specs.md` is a combined reading copy generated from the source files in this package. The separate files remain authoritative because they allow implementation agents and specialist auditors to work from bounded scopes.

## Design summary

The Black Market is a hidden logistics network, not a universal shop. Its offers exist only when there is a proven source, a valid buyer, and a working route. Equipment sold by a member is removed from that member before the lot can be bought. Captured, collapsed-state, naval, intelligence, technology, chemical, biological, and special-project offers require an explicit provider receipt from their owning system.

Members manage three public values:

1. **Market Credit**, which pays for offers and is earned through verified sales, brokerage, and limited underwriting.
2. **Exposure**, which measures the risk that routes, governments, and transactions become known.
3. **Network Reach**, which controls membership, route capacity, offer classes, and evolution readiness.

The system uses one hidden member-only decision category with a static picture that changes by evolution. Each phase exposes three to five primary actions, with six as the absolute maximum and one to three active missions. Outsiders receive temporary targeted counter-smuggling actions only after they gain evidence against a specific route or cell.

The event has three paced evolutions at `200+`, `400+`, and `600+` Chaos. Evolution activation itself changes no Chaos. Event-owned Chaos changes come from concrete milestones such as the first interregional route, a successful embargo breach, a transaction between active enemies, or the delivery of an approved experimental package.

## Source status

Every top-level source file supplied for this task was read in full. The three CSV catalogs were read in full. The subagent ZIP was extracted, and all twenty current subagent TOML definitions were read in full. No source file was knowingly truncated during the final design pass.

The supplied Codex subagent runtime could not be invoked because its MCP tunnel returned an HTTP `404`. The package therefore records internal role-based passes that apply the provided subagent contracts. It does not claim that project subagents were successfully spawned.
