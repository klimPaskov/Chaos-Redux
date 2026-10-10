# Event 57: The Black Market

This package defines the full planning specification for Chaos Redux Event 57, **The Black Market**.

The event is a `Minor Fire-Once` event at Chaos level `1`. Its first firing creates a persistent, invitation-only international smuggling network. The random event itself never repeats. Later membership growth, inventory rotations, route failures, investigations, transactions, and evolutions belong to the event-owned runtime.

## Design authority and current workflow

The package attributes its premise to the supplied user brief.
The original user message and claim-level acceptance record are not reproduced here, so approval of expanded mechanics remains unresolved until the implementation owner records the supporting user decision or parent acceptance.
Historical planning reviews, catalog snapshots, and package status labels do not establish approval or current implementation.
Use current [AGENTS.md](../../../AGENTS.md), [event guidance](../../../.claude/skills/chaos-redux-events/SKILL.md), [asset guidance](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [subagent guidance](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for execution.
The source design remains in the files listed below.

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

[The former combined reading copy](057_the_black_market_full_specs.md) is superseded by the separate files in the package map. The separate files hold the editable design and bounded specialist inputs.

## Design summary

The Black Market is a hidden logistics network, not a universal shop. Its offers exist only when there is a proven source, a valid buyer, and a working route. Equipment sold by a member is removed from that member before the lot can be bought. Captured, collapsed-state, naval, intelligence, technology, chemical, biological, and special-project offers require an explicit provider receipt from their owning system.

Members track two public numbers and one stage label:

1. **Market Credit**, which pays for offers and is earned through verified sales, brokerage, and limited underwriting.
2. **Exposure**, which measures the risk that routes, governments, and transactions become known.
3. The **Network Reach** stage, a shared world value that controls membership, route capacity, offer classes, and evolution readiness. Members see its stage label, not its number, because no single member steers it directly.

The system uses one hidden member-only decision category with a static picture that changes by evolution. Each phase exposes three to five primary actions, with six as the absolute maximum and one to three active missions. Outsiders receive temporary targeted counter-smuggling actions only after they gain evidence against a specific route or cell.

The event has three paced evolutions at `200+`, `400+`, and `600+` Chaos. Evolution activation itself changes no Chaos. Event-owned Chaos changes come from concrete milestones such as the first interregional route, a successful embargo breach, a transaction between active enemies, or the delivery of an approved experimental package.

## Original planning source status

The original reading record and subagent execution status are in `00_source_and_research_record.md` and `12_specialist_review_record.md`.

## Open questions

- `unresolved`: the smuggled food lot in `06_evolutions_chaos_cluster_and_connections.md` needs the famine owner to expose its relief-delivery completion as a callable seam for a Black Market delivery.

## Changelog

### 2026-10-10 spec audit

- Network Reach is shown as a stage label instead of a third tracked number; members actively track only Market Credit and Exposure. Reach is a shared world value no single member steers, so its number did not drive decisions.
- The separate Arrange a Safer Route and Accept the Dangerous Route decisions became one path question on Acquire Current Lot, and Replace the Manifests merged into Compartmentalize the Cell; at most three Exposure actions are visible at once. This removes near-duplicate buttons from a category with a six-action budget.
- The vague famine and migration note became a concrete proposed package: a smuggled food lot that only appears when Import Food is blocked and delivers through the famine owner's relief completion.
- The README no longer repeats the original planning environment's runtime failure; that record stays in `00_source_and_research_record.md`. Subagent instructions use the Claude-first wording.
