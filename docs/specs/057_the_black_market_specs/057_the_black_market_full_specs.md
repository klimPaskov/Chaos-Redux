# Event 57: The Black Market, Full Specification Pack

This combined reading copy is generated from the separate source files in the package. The separate files remain authoritative for bounded implementation and specialist review.

## Included files

- `README.md`
- `00_source_and_research_record.md`
- `01_core_event_spec.md`
- `02_membership_secrecy_and_government_postures.md`
- `03_smuggling_routes_and_network_growth.md`
- `04_inventory_trade_and_provider_api.md`
- `05_decisions_missions_and_player_loop.md`
- `06_evolutions_chaos_cluster_and_connections.md`
- `07_ai_probability_balance_and_edge_cases.md`
- `08_event_chain_logs_localisation_and_catalog_alignment.md`
- `09_assets_and_achievements.md`
- `10_implementation_acceptance_and_validation.md`
- `11_improvement_loop_closure.md`
- `12_specialist_review_record.md`
- `13_requirement_coverage_matrix.md`
- `research/historical_design_anchors.md`
- `research/bibliography.md`
- `prompts/57_the_black_market_asset_prompt.md`
- `prompts/57_the_black_market_achievement_prompt.md`
- `prompts/57_the_black_market_decision_mission_prompt.md`
- `prompts/57_the_black_market_scripted_system_prompt.md`
- `prompts/57_the_black_market_ai_probability_audit_prompt.md`
- `prompts/57_the_black_market_localisation_audit_prompt.md`
- `prompts/57_the_black_market_spreadsheet_alignment_prompt.md`
- `prompts/57_the_black_market_event_completion_audit_prompt.md`
- `prompts/57_the_black_market_coding_prompt.md`
- `prompts/57_the_black_market_goal_prompt.md`



---

## Source file: `README.md`

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


---

## Source file: `00_source_and_research_record.md`

# Source and Research Record

## Reading declaration

Every top-level file listed below was read in full before the final specification was written. The three catalog CSV files were read in full. The subagent ZIP was extracted, and every TOML definition listed below was read in full.

The line counts and SHA-256 values identify the exact supplied files used for this planning pass. The ZIP is listed as a binary container, followed by its extracted definitions.

No listed source was knowingly skipped or summarized from a partial snippet during the final design pass.

## Supplied top-level files

| File | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `chaosx_dynamic_triggers.md` | 3935 | 61 | `7f6733ef08b816c38aba6d5c675f98c054e9167accd5be3bdf536b65bb60291e` |
| `chaosx_dynamic_effects.md` | 14618 | 280 | `2ed4e8f3d220d7d09fd32eabe5e2d35226816d417dbbc11a9635758080bccdf7` |
| `CHAOS_REDUX_MECHANICS(9).md` | 71678 | 1164 | `f3a4276d534056b5349c17e029df8f0821dd2b7728237af07d377375a3c38291` |
| `chaos_redux_clusters_catalog(4).csv` | 2836 | 14 | `ae37b095ccf1e264397284b1c9e2e9184433e75c5bb6957ef50ea14cef1c63f7` |
| `chaos_redux_scenarios_catalog(4).csv` | 12239 | 56 | `0704f9c5a77b6c1bb06f5eead93eb9e130986718763ed7cc212225fc84e22ce2` |
| `chaos_redux_events_catalog(4).csv` | 52722 | 252 | `a2d1edcd12a2891eb4b9040139447993f0657af93b166fa0ddd4a1b1186a6fbf` |
| `chaos-redux-improvement-loop.md` | 27478 | 287 | `dd1cea075f7d76a5a0c1c8a55ce65bc69d677afd3010cf51d42baa39054cfa53` |
| `AGENTS(10).md` | 43195 | 417 | `5fd1111fc9acb189987b5d11b371a1d4202f63c91f5d9487f6408515321d7567` |
| `chaos-redux-subagents(1).md` | 36164 | 357 | `ff5e08f96238d5cc3a353fd71253252e7f06d638f4261a6715bbb16d7d6ede9d` |
| `config(2).toml` | 11385 | 189 | `df72462c8abcafffeb8250bcd5934680928604a4c64181bd401340c57f508adb` |
| `chaos-redux-decisions-missions(1).md` | 74499 | 1166 | `8503d548c92d96ffa4419e760045d726201a69fa78a4a55a87087d855b1af5a5` |
| `chaos-redux-event-assets.md` | 124623 | 1519 | `7c15faa859cd40540cd1d64a00ff2112d68327aa37ae8dbe762763e5ba405cc8` |
| `chaos-redux-3d-model-pipeline.md` | 87136 | 413 | `ced1ca88126e46f860d55abb66d5507c48aa40b9687715855497e8b0cf71a377` |
| `chaos-redux-events(1).md` | 72941 | 804 | `91463e91407af1fe88358050729cb247793f004ac96e890e3ff659c455b85714` |
| `chaos-redux-comfyui.md` | 2123 | 16 | `128acd133fedc56b14612eed163de11d7261dac887f11eacf4c8b695dae97fa0` |
| `chaos-redux-debug-playtest.md` | 30145 | 666 | `ec9d66e433e9d964a2561844aa45281342842b973e059a09fab18f2107283a43` |
| `chaos-redux-focus-trees.md` | 98154 | 1503 | `51f741f8abde30c7772be46072fa4530361dcf4fc348da97b69c86206761789b` |
| `chaos-redux-frame-animation.md` | 27086 | 495 | `a8dd6bdcec2b849c6f5c85abffb863510a5585418f2e608c713c8ba83154aa48` |
| `chaos-redux-super-events.md` | 33028 | 793 | `d7afffcf25b70333fd50aaef1f72378c1c270b8057269597f085c96204e01607` |
| `README(20260830-071218).md` | 2351 | 37 | `bb4b9587eddce00479b5792a7897dbe6f41cc48c5a46fe67b2e129dafbaf8978` |
| `chaos-redux-event-planning(1).md` | 195156 | 2277 | `09a18e704984a9d08cb20851f6599acc494ff1939016e384fd049c3b3c412464` |
| `subagents(4).zip` | 59612 | binary | `799dfd4e95715d0840b90009558e4d719e2f42eba16db4a258644bc990bd796d` |

## Extracted subagent definitions

| File | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `subagents_extracted/chaosx_3d_model_pipeline.toml` | 24375 | 187 | `235cb326978966a6b284c64dd0dfe8acf9d2be668393b8122c5e37b88875cb92` |
| `subagents_extracted/chaosx_ai_probability_auditor.toml` | 6348 | 66 | `20336a1ec04210d7f468e364fa48ca59427a5fa1292e8765af9eb746a73e6856` |
| `subagents_extracted/chaosx_asset_source_researcher.toml` | 3017 | 58 | `4db7e102822821201eb80055d45ad89272de7cdc4c6c695953d45854bd0e8df6` |
| `subagents_extracted/chaosx_country_package_auditor.toml` | 7965 | 87 | `b140694067beb96d77ab31f6bf1eaa595eff02cf6ae83ce33e50e7ef2bedece4` |
| `subagents_extracted/chaosx_decision_mission_auditor.toml` | 8443 | 99 | `b8d579a9aec9fae7f9a6c5a291976660460ee8a3f1b69e8ef77af70535315433` |
| `subagents_extracted/chaosx_documentation_curator.toml` | 10140 | 131 | `8aea5aad0f4c5350013377041e57029d3cd296774a6713977f2e34cccf533885` |
| `subagents_extracted/chaosx_event_completion_auditor.toml` | 4117 | 66 | `59cbca30c23cd810ac31618eb0ece7a1280455b641096dd2c701e680b261aaee` |
| `subagents_extracted/chaosx_event_ui_worker.toml` | 10720 | 84 | `4afc059508881379bc272bbfac519ddbbe0c448c1fa5f46626cd78fd459f736d` |
| `subagents_extracted/chaosx_focus_tree_auditor.toml` | 4499 | 80 | `83149977d6749cfe743d8ec4c2afa769a019dbfbbc8fd62390460b3629f444e3` |
| `subagents_extracted/chaosx_generated_event_art.toml` | 3909 | 72 | `f7c85c45acf334f76b93ed95409b0165affdc801fea6dd1094651533d89ae3ea` |
| `subagents_extracted/chaosx_icon_artist.toml` | 7611 | 104 | `1afbd89167f2dab6bba6271d2da7523c923a5faba495dbeedde43950af70c0f7` |
| `subagents_extracted/chaosx_improvement_loop_planner.toml` | 7069 | 61 | `a90323b1cbbd664fa61e245186fe7dd912498018e07f3e2393e2641555fbd2bf` |
| `subagents_extracted/chaosx_localisation_auditor.toml` | 9109 | 108 | `f754134bb8df4ec8c99a50c3de69eda2c2b6a211a026aae396af600f224bf30e` |
| `subagents_extracted/chaosx_portrait_creator.toml` | 2029 | 20 | `87b001c6fb5afc33267eb77a3187ff654dbf6b03ae5d669cb2d5182bf7ac2174` |
| `subagents_extracted/chaosx_repo_explorer.toml` | 12690 | 234 | `3b7380b83e0dd6bba741b5c5cd5419e3e5bf22c284459d28d60706b246d964a1` |
| `subagents_extracted/chaosx_scripted_system_architect.toml` | 5387 | 74 | `b2e012aaec78bc875ae27275eb03f86d425aa19ece182716d2570117ff56cacf` |
| `subagents_extracted/chaosx_skill_maintainer.toml` | 3819 | 47 | `1c5efb578a007fc1e3e7f0561d7353876d73918be830f754870041f9d2f66ac2` |
| `subagents_extracted/chaosx_spreadsheet_doc_worker.toml` | 4605 | 59 | `896cb63222484317280d31c340edfc282847774f8edab31a68d7fc2b8b0be33b` |
| `subagents_extracted/chaosx_super_event_audio_researcher.toml` | 3339 | 65 | `248c26c573151ac503886da9bc8cf1942d2af41608528fb2e92161a7808f7d9b` |
| `subagents_extracted/chaosx_super_event_text_researcher.toml` | 3921 | 62 | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` |

## Source hierarchy used

The user-provided Event 57 brief is the accepted design source for the event identity.

The supplied current Events CSV still maps ID `57` to an older Radar entry. The supplied Positive Economy cluster export also predates Event 57 membership. A separate project cluster-update source found during the file review explicitly maps Event 57, The Black Market, to Positive Economy with High severity. The final specification treats the user brief as the accepted replacement and records the current catalog state as an implementation alignment task.

The CSV files remain read-only exports. Later implementation must update the authoritative workbook and run the repository exporter.

## Project rules applied

The package applies these main contracts from the supplied sources:

- Event 57 remains Minor Fire-Once and uses one canonical entry event.
- Later market behavior is persistent event-owned processing, not repeated random-event firing.
- Normal growth stages remain separate from the three logged evolutions.
- Evolution activation changes no Chaos by itself.
- Shared Chaos sources must not be counted again.
- The system uses sparse registered records instead of broad recurring country scans.
- The member-facing mechanic uses three public values.
- One phase exposes three to five primary actions, with six as the hard maximum.
- A gameplay action uses no more than four spendable cost types.
- Equipment, technology, intelligence, naval, CBRN, and special-project owners keep their own ledgers.
- Assets require correct source modes, final runtime files, manifests, sprite handoffs, and independent icon-family work.
- The authoritative XLSX is the only editable catalog source.

## External historical research

The design research used authoritative museum, archive, government, and military sources on wartime illicit trade, border smuggling, blockade evasion, neutral channels, military scandal, and captured equipment.

The detailed design translations and URLs are recorded in:

- `research/historical_design_anchors.md`
- `research/bibliography.md`

The historical sources support design patterns. They do not establish that one worldwide Black Market organization with these exact rules existed.

## Subagent execution status

The supplied archive defined twenty project subagents. Their role contracts were fully read and applied as internal specialist review passes.

An attempt to invoke the outer Codex subagent runtime failed because its MCP tunnel returned HTTP `404`. No project subagent was successfully spawned. The package does not claim otherwise.

The internal role pass and future routing plan are recorded in `12_specialist_review_record.md`.

## Environment limits

This task produced a design specification package in the current container. It did not edit the user's Chaos Redux repository, the authoritative workbook, or gameplay files. It did not launch Hearts of Iron IV, run the explicit autonomous debug skill, or claim in-game validation.

The repository's offline Paradox wiki and installed vanilla game directory were not mounted in this container. The planning task did not change engine-facing source. The implementation prompts require the later coding agent to inspect those local references before code changes.

## Simplification declaration

The specification was not shortened into a quick summary. It includes the complete accepted event loop, membership, routes, inventory, provider boundary, decisions, missions, AI, probability scenarios, evolutions, Chaos map, cluster behavior, event connections, localisation direction, assets, achievements, DLC paths, edge cases, validation, and implementation prompts.

No unapproved gameplay fallback was used. The only failed requested process was actual subagent invocation, which is reported above.


---

## Source file: `01_core_event_spec.md`

# Event 57: The Black Market

## Catalog entry

- Event ID: `57`
- Event name: The Black Market
- Type: Minor Fire-Once
- Status: To Be Reworked
- Chaos level: `1`
- Cluster: Positive Economy
- Cluster role: High member

## Playable promise

The Black Market creates a secret international economy that can move restricted military and industrial goods between countries that ordinary diplomacy keeps apart.

The event should make shortages, surplus stockpiles, blockades, neutral routes, captured equipment, intelligence contacts, corrupt officials, and foreign wars matter in a new way. A member can solve a dangerous shortage or turn useless surplus into influence, but every transaction depends on a physical route and increases the chance that governments, customs services, or intelligence agencies find part of the network.

The market must feel alive after its first event. Membership changes. Regional cells connect or break apart. Offers rotate. A route can become strained, compromised, or unusable. A member can tolerate the network, sponsor it, penetrate it, or destroy its local section. The strongest goods appear only after the network earns wider reach and the required evolutions become active.

The market is distinct from the legal international market. It uses separate rules, separate membership, separate currency, delayed deliveries, uncertain provenance, route risk, seizures, and compartmentalized knowledge. War, ideology, faction membership, hostility, and embargoes can lower trust or close particular routes, but none of them is an automatic transaction ban when a working underground path exists.

## First firing

The canonical entry is `chaosx.nr57.1`.

The entry event performs one bounded founding transaction:

1. It identifies a valid broker country.
2. It builds a connected founding cell around that broker.
3. It creates the first smuggling routes.
4. It sends private invitations to the selected governments.
5. It creates the persistent event-owned runtime.
6. It records Event 57 once in the shared event history without publishing the founders.

The target founding group is three countries. Two countries are permitted when the world state cannot support a connected three-country cell. Four countries are permitted when one additional country is required to bridge two otherwise valid route segments. The first firing must never create more than four members.

A valid founding cell requires at least one proven route between every member and the connected component. The graph can use one broker linked to two endpoints. Every founder does not need a direct route to every other founder.

The event is unavailable when fewer than two eligible ordinary countries can form a route-backed cell. Normal manual firing retains that requirement. Force Trigger Mode may bypass the event's Chaos level and selection state, but it must not create invalid countries, nonexistent ports, false borders, or route records with no endpoints.

## Founder selection

Founder selection should favor countries that have a reason to use illicit trade and a practical way to support it.

Strong positive factors include:

- an active embargo, sanction, or major trade restriction
- an equipment, fuel, convoy, train, truck, or industrial shortage
- a current war
- access to a neutral border, major port, occupied corridor, or international transport route
- a useful equipment surplus
- weak access to the legal international market
- intelligence contacts or an established agency
- previous smuggling or underground-trade memory
- relations with one selected founder
- state tolerance of criminal intermediaries or covert procurement

Strong negative factors include:

- no route to the proposed cell
- no meaningful demand, surplus, brokerage role, or intelligence role
- a recent successful suppression campaign
- very high confidence in ordinary trade access
- a government route that explicitly forbids covert foreign procurement
- a previous expulsion for betrayal that is still inside its exclusion period

The current player receives a moderate inclusion bonus when eligible. This increases the chance of direct interaction without forcing membership onto a country whose policy, geography, or circumstances make no sense. An ineligible player can first encounter the system later through an invitation, a seized shipment, a discovered intermediary, or an intelligence operation.

## Country eligibility

Ordinary human countries are the default participants.

The shared country classifiers are the first exclusion contract. Ordinary selection requires `uses_normal_civilian_systems = yes` and excludes `is_special_chaos_country = yes`. Actual nonhuman countries therefore fail automatically, and special human Chaos actors also remain outside the normal pool. An owning event can provide a narrow explicit Black Market adapter for a special human actor when its design truly supports clandestine trade, but a missing adapter means exclusion.

Eligibility must also account for:

- country existence and valid government scope
- access to at least one route family
- independence, autonomy, exile status, and host-country access
- civil-war status and control of relevant states
- capitulation and government-in-exile conditions
- subject restrictions
- current wars and hostile borders
- current policy toward the network
- temporary suspension or expulsion

Subjects can participate when they possess usable territory, stockpiles, officials, or routes. Their overlord does not automatically learn this. Integrated or powerless subjects with no independent logistics, no controllable stockpile, and no valid route are excluded until that changes.

Governments in exile can buy arms or intelligence only through a host-backed route and a verified recipient package. They cannot act as normal founding sellers without controlled stockpiles and a delivery endpoint.

## What outsiders know

Countries outside the network receive no Black Market decision category and no global member list.

The shared event history may show that Event 57 fired as a mod-level record. It must not show a founder flag, founder name, seller list, route map, inventory, or regional cell. This is meta history, not country knowledge.

Country-level knowledge is compartmentalized:

- a member knows its own government posture
- a member knows the direct routes it uses
- a buyer knows the offered goods and stated provenance class
- a direct counterparty can become known only when the offer type requires it
- a regional broker may know the adjacent cell, but not every distant member
- an outsider learns only the route, intermediary, shipment, or member proven by its evidence

A global public reveal can occur only through a concrete breach. Even then, public knowledge concerns the existence and broad scale of illicit trade. It does not reveal the complete membership ledger.

## Persistent runtime

The random event fires once. Everything after the founding transaction belongs to a persistent event-owned system.

The runtime keeps sparse registries for:

- active members
- dormant members
- suspended members
- former members
- invitation candidates
- active routes
- disrupted routes
- open offers
- active deliveries
- current evidence cases
- registered provider packages
- completed transaction receipts
- recent market imports that cannot be resold immediately

Processing should use the registered arrays and active jobs. It must not run a whole-world daily, weekly, or monthly country scan.

A bounded global pulse can process registered members and routes at an event-owned interval. Founding, invitation, transaction, route, war, annexation, capitulation, embargo, exposure, and provider events should mark only the affected records for refresh.

## Public mechanic values

Members manage three public values.

### Market Credit

Market Credit represents hard currency, barter claims, shell-company balances, favors, letters of credit, and the market's internal settlement ledger.

It is spent on offers, commissions, route services, and auctions. It is earned through verified sales, brokerage, intelligence contributions, and limited underwriting. It is not political power with another name.

Market Credit has a visible amount, a stable texticon, a country-specific cap, and clear gain or loss tooltips. The cap scales from the country's economy, market posture, and current evolution. Rejoining the network never grants a second founding balance.

### Exposure

Exposure measures how likely the country's routes, officials, and transactions are to become known.

Its range is `0` to `100`.

| Band | Public state | Main effect |
| --- | --- | --- |
| `0-24` | Hidden | Normal access and low investigation pressure |
| `25-49` | Rumored | Higher delivery risk and occasional local evidence |
| `50-74` | Under Investigation | Counterintelligence actions and route scrutiny become more common |
| `75-99` | Compromised | Severe seizure risk, member distrust, and posture restrictions |
| `100` | Network Breach | A breach incident resolves against the country and affected routes |

The exact value is visible to members because it changes immediate choices. Outsiders never see another country's Exposure score.

### Network Reach

Network Reach represents the market's shared ability to find suppliers, connect regions, clear payments, and move larger cargo.

Its range is `0` to `100`. It grows through real transactions, members, regional connections, and restored routes. It falls through seizures, expulsions, broken routes, and dismantled cells.

Network Reach never replaces the three formal evolutions. It provides the world-state proof that an evolution has earned its next capability set.

A member sees the current value, current reach stage, and the next public threshold. The contributor ledger stays hidden. The tooltip summarizes the largest actionable causes, such as successful deliveries, a lost route, or a recent breach.

## Reach stages

| Reach | Working stage label | System state |
| --- | --- | --- |
| `0-14` | Fragmented Contacts | The network is dormant or rebuilding |
| `15-34` | Local Circuit | Small regional lots and one primary route per member |
| `35-64` | Linked Regions | Wider suppliers, larger logistics lots, and Evolution I readiness |
| `65-84` | Underground Exchange | Embargo circumvention, specialist providers, and Evolution II readiness |
| `85-100` | Hidden World Market | Grand auctions, rare packages, and Evolution III readiness |

These are working labels, not final localisation.

## Baseline member experience

A member should normally make one of five kinds of decisions:

1. Buy a current lot that solves a real shortage.
2. Sell a verified surplus and gain Market Credit.
3. Repair or improve a route.
4. Change the government's relationship with the network.
5. Manage Exposure after a risky transaction or investigation.

The baseline offer pool focuses on small arms, support equipment, artillery where valid, trucks, trains, convoys, fuel, modest intelligence packages, and small source-backed foreign or captured lots. Tanks, aircraft, large captured stockpiles, unusual equipment, and complete technical packages belong to later capabilities unless the world date and a provider make an early appearance reasonable.

Every purchase creates a delivery job. The goods do not appear immediately merely because the player clicked a decision.

## Dormancy, reconstruction, and final dismantling

The network becomes dormant when it has no active route-backed cell capable of generating and delivering an offer.

Dormancy does not automatically delete the event. Former members, surviving brokers, locked credit, and old route knowledge remain. A bounded reconstruction pulse can try to reconnect a former member or build one new route after a long delay.

A full dismantling is possible only when all of these are proven:

- no active members remain
- no active routes remain
- no delivery job remains unsettled
- the clearinghouse or equivalent settlement chain has been exposed
- Network Reach has fallen below the final dismantling threshold
- no reconstruction request is already committed

Full dismantling ends automatic growth and offer rotation. It preserves history and achievement records. A later event cannot silently recreate Event 57 as a second first firing.

## Tone and text direction

The event should use period clandestine logistics as its visual and writing language.

Useful subjects include false cargo manifests, guarded warehouses, mismatched crates, railway sidings after dark, neutral freight offices, diverted fuel drums, merchant holds, captured guns with altered markings, anonymous couriers, customs seizures, and intelligence officers dealing through intermediaries.

Avoid modern digital-market terms, online-market language, generic gangster-film dialogue, ornate criminal guild lore, or a single named mastermind. The network is an international system of brokers and routes, not a new country or a central villain.

Member invitation text should convey limited knowledge and practical need. Acceptance, patronage, penetration, and refusal should have different government voices. Final wording belongs to implementation and localisation review.


---

## Source file: `02_membership_secrecy_and_government_postures.md`

# Membership, Secrecy, and Government Postures

## Membership model

The Black Market is invitation-only. Membership is a country-owned relationship with the network, not a public diplomatic status.

Each country can occupy one of the following states:

| State | Meaning | Category access |
| --- | --- | --- |
| Candidate | The network has identified a possible contact but has not sent an invitation | None |
| Invited | A live invitation is pending | Invitation report only |
| Active member | The country has at least one usable route or a committed route-opening mission | Full current phase |
| Dormant member | The country retains contacts and locked credit but has no usable route | Reconnection actions only |
| Suspended member | Access is blocked by a breach, unpaid settlement, or internal conflict | Remediation actions only |
| Former member | The country withdrew or lost access without permanent expulsion | No normal category until reconnection |
| Expelled member | The network recorded betrayal, repeated exposure, or deliberate seizure | No normal category during exclusion period |
| Dismantler | The country is running a verified counterintelligence penetration against a known cell | Counter-smuggling actions only |

A country cannot hold two contradictory states. State transitions must be idempotent and must clean up obsolete decisions, missions, selected offers, route flags, and temporary targets.

## Invitation ownership

An invitation belongs to one sponsoring member and one candidate country.

The sponsor provides the initial route proof. The candidate receives only the information needed to decide whether to accept. The invitation does not reveal the wider member list.

An invitation record should store:

- sponsoring member
- candidate
- proposed route type
- route endpoint or intermediary proof
- invitation issue date
- invitation expiry date
- current evolution
- expected founding credit or access package
- candidate acceptance score
- rejection reason when invalidated
- one-time receipt ID

A live invitation is invalidated when the sponsor disappears, the route becomes impossible, the candidate is annexed, the candidate enters a mutually incompatible policy state, or the network is dismantled.

## Invitation cadence

Membership growth occurs through event-owned pulses, not through repeated random-event firings.

Suggested starting cadence:

| Network state | Base invitation interval | Factors that shorten it | Factors that lengthen it |
| --- | ---: | --- | --- |
| Baseline | `150-240` days | war, embargoes, two successful deliveries, a new regional route | recent breach, low Reach, several refusals |
| Evolution I | `100-180` days | connected regions, broker surplus, active shortages | disrupted routes, high average Exposure |
| Evolution II | `75-150` days | major embargo pressure, neutral relays, provider demand | public investigations, suspended members |
| Evolution III | `60-120` days | Grand Auction cycle, global wars, several mature cells | regional dismantling, route saturation |

These are tuning anchors. Final intervals should be centralized and modified by live state.

A pulse chooses one active sponsor, builds a bounded candidate shortlist, and commits at most one new invitation. The same pulse cannot invite several countries merely because the network is large.

## Candidate shortlist

Candidate search should begin from the sponsor's actual connections.

Preferred candidate sources are:

- direct land neighbors
- countries connected through a valid neutral intermediary
- countries with ports that can support the sponsor's maritime route
- countries controlling part of an existing international corridor
- countries with strong relations to the sponsor
- countries currently trading, fighting, sanctioning, or sharing intelligence with the sponsor when script evidence exists
- former members with a valid reconnection route
- countries named by an owner-provided event adapter

The implementation can use a small number of bounded random candidate samples when a direct collection is unavailable. It must not iterate over every country every day or every month.

## Acceptance factors

The candidate decides whether to accept, reject, delay, or infiltrate.

### Demand

Acceptance rises when the candidate has:

- severe equipment shortages
- low fuel reserves
- inadequate convoys or trains
- a current war
- an active embargo or strategic sanction
- poor legal market access
- an urgent intelligence requirement
- a large but unusable stockpile it could sell
- an isolated or threatened government

### Route confidence

Acceptance rises when:

- the proposed route is open
- the sponsor shares a border
- the candidate owns a usable port
- a neutral intermediary is stable
- the route avoids an enemy blockade
- the candidate has sufficient convoys, trains, trucks, fuel, or airlift capacity

### Political and security fit

Ideology alone does not decide compatibility.

A stable democracy with open trade and a strong anti-corruption policy should usually reject an unnecessary invitation. The same country may accept during blockade, invasion, or acute shortage.

An authoritarian government may find state patronage easier, but a highly centralized security state can also suppress an independent criminal network. A planned economy may reject private brokerage while still using intelligence-controlled procurement. A neutral commercial state may prefer an intermediary role and decline full membership.

Relevant factors include:

- ruling ideology and route flags
- internal repression
- corruption or anti-corruption policy
- intelligence capacity
- stability
- war support
- faction obligations
- legal trade access
- recent scandals
- previous dealings with the network
- relations with the sponsor

### Trust and memory

Hidden trust rises through completed settlements, clean deliveries, route assistance, and reliable sales. It falls through missed deliveries, seizures, leaked identities, hostile posture changes, and selling the same information to several sides.

Trust is an internal input. It is not a fourth public meter.

## Candidate responses

### Accept and keep distance

The government enters active membership under the compartmentalized posture. It receives its one-time founding credit and one route. The founding credit is never granted again after withdrawal, suspension, annexation, tag restoration, or reconnection.

### Accept and sponsor the network

This response is available only when the government can commit state resources. It enters State Patronage immediately and gains stronger brokerage and route capacity at the cost of higher Exposure.

### Accept and penetrate

The country joins under Counterintelligence Penetration. It can trade enough to maintain cover, but its primary goals are evidence, control, and possible dismantling.

The route should be available only when the country has a valid intelligence or internal-security basis. Without La Résistance, base-game political and security conditions provide the equivalent route.

### Reject

Rejection does not expose the sponsor by default. The candidate can quietly refuse, threaten a local crackdown, or preserve the contact for later.

A quiet refusal creates a long invitation cooldown. A hostile refusal creates a shorter investigation opportunity and reduces trust. The network should not repeatedly invite a country that keeps rejecting it.

## Member knowledge

A member does not automatically know every other member.

The knowledge model should distinguish:

- **direct contact**, meaning a route or transaction names the counterparty
- **regional awareness**, meaning the member knows that another cell exists in a named region
- **broker knowledge**, meaning a country knows one intermediary or settlement office
- **network awareness**, meaning the member understands the market's broad reach but not its membership
- **proven identity**, meaning an evidence receipt names a specific participant

Direct trading at Evolution I can reveal a counterparty to the two participants. Hostile countries can transact at any stage when a valid route, source, and trust proof exist. Evolution III makes masked hostile transactions more frequent, larger, and easier to route without forcing identity disclosure.

## Government postures

A member chooses one active posture. These are working design labels, not final localisation.

### Compartmentalized Tolerance

This is the default member posture.

It represents officials ignoring selected routes while keeping the government formally distant.

Effects and rules:

- normal offer access
- lower Exposure per transaction
- one primary route at baseline
- lower sale volume from state stockpiles
- faster passive Exposure recovery during quiet periods
- limited ability to influence the next inventory rotation
- low diplomatic damage if a local route is exposed

AI countries use this posture when they need the market but have stable institutions, moderate shortages, or a strong fear of scandal.

### State Patronage

The government places officials, depots, transport offices, or intelligence services behind the network.

Effects and rules:

- larger sale and purchase handling capacity
- higher Market Credit cap
- faster route repair
- stronger ability to commission a category
- access to state reserve sales when readiness floors remain satisfied
- higher Exposure from every major transaction
- harsher consequences if evidence proves government direction
- more pressure from foreign intelligence and sanctions

State Patronage should be attractive for isolated regimes, countries in long wars, and governments with large surplus stockpiles. It must not become the universal best posture.

### Counterintelligence Penetration

The government allows a controlled cell to operate while security services build evidence.

Effects and rules:

- reduced ordinary offer access
- normal access to small cover transactions
- higher chance to identify an intermediary after a failed or delayed delivery
- ability to feed false manifests, mark a shipment, or prepare a coordinated seizure
- a route toward regional dismantling
- a risk that the network detects the operation and expels the country
- lower Market Credit cap

This posture needs real intelligence or security capacity. It should not be a free choice for every weak minor.

A country under penetration can remain a member for a long time. The network should react to evidence of suspicious behavior. It cannot automatically know the government's intent.

### Suppression Campaign

The government ends normal trading and attempts to destroy the local network.

Effects and rules:

- normal purchase and sale actions close
- current undisbursed credit becomes locked
- active deliveries resolve according to dispatch state
- route seizure and intermediary arrest missions become available
- Exposure rises at the start because contacts begin disappearing
- success can turn the country into a former member or regional dismantler
- failure can expose the government, destroy evidence, and produce expulsion

Suppression is a committed route, not a posture that can be toggled for one reward and immediately reversed.

## Posture changes

Changing posture requires a cooldown and a valid political or security basis.

Suggested base cooldown is `180` days, modified by:

- recent breach
- war emergency
- government change
- intelligence leadership change
- successful suppression
- major embargo activation
- network evolution

A shift from State Patronage directly into Suppression creates a betrayal incident and a large Exposure increase. A shift from Compartmentalized Tolerance into Counterintelligence Penetration is quieter but requires intelligence capacity and time.

Posture changes must not grant repeated credit, repeated route rewards, or repeated Reach.

## Voluntary withdrawal

A member can withdraw when it has no unsettled delivery and no active route mission.

Normal withdrawal:

- closes ordinary access
- preserves the former-member record
- locks most Market Credit
- settles a network fee against the remainder
- keeps one reconnection lead when Exposure is below the breach threshold
- applies a long re-entry cooldown

The country does not receive another founding balance after re-entry.

A government can burn its contacts during withdrawal. This forfeits more credit and reduces Exposure, but makes reconnection harder.

## Suspension

Suspension is temporary and can result from:

- unpaid or inconsistent transaction state
- a route breach
- Exposure reaching `100`
- loss of every route
- government collapse during an unsettled transaction
- provider package invalidation
- suspected penetration

A suspended member sees only remediation, settlement, route repair, or withdrawal actions. It cannot buy or sell until the suspension reason is cleared.

## Expulsion

Expulsion follows proven betrayal or repeated serious failure.

Possible causes include:

- a successful sting against another member
- exposing several member identities
- seizing a dispatched shipment under false pretenses
- attempting to resell recently imported market equipment
- failing several settlements
- deliberate state confiscation under State Patronage
- a detected Counterintelligence Penetration operation

Expulsion:

- closes all normal access
- cancels undisbursed offers
- resolves dispatched deliveries through the receipt ledger
- freezes or confiscates remaining Market Credit
- destroys direct trust
- records a country-specific exclusion period
- may create a targeted retaliation or false-manifest incident

Expulsion does not make the complete network public.

## Reconnection

Former and dormant members can reconnect through a surviving sponsor, old intermediary, or route reconstruction mission.

Reconnection requires:

- one valid route proof
- no active expulsion exclusion
- a compatible government posture
- no unsettled hostile case against the network
- a bounded Market Credit reconciliation

Reconnection does not increase Reach unless it restores a route or regional cell that had genuinely been lost.

## Annexation, civil war, and tag changes

Membership belongs to the current country scope and must not silently duplicate during country splits.

### Annexation

When a member is annexed:

- its active routes are marked for refresh
- undisbursed offers are canceled
- dispatched cargo keeps its transaction receipt
- its credit is frozen
- the annexer does not inherit membership automatically
- a successor can receive a reconnection invitation only through a new proof

### Civil war

A civil-war split can produce one of three outcomes:

- the original government retains membership and the breakaway knows nothing
- one side inherits the active cell because it controls the route state and depot
- the cell fractures and both sides become candidates with no normal access until the network chooses one

The split must use route, capital, stockpile, intelligence, and government evidence. It cannot copy full membership and credit to both sides.

### Cosmetic and tag changes

A cosmetic identity change preserves membership. A genuine tag replacement or release uses an explicit transfer or reconnection path. Stable transaction receipts must survive only when their buyer and seller scopes remain valid.

## Secrecy failure and evidence

Exposure is country-local. Evidence is observer-local.

An outsider's evidence record should name only what has been proven:

- suspicious cargo class
- route endpoint
- intermediary
- shipment date
- known member
- probable member
- source country when recovered serials or documents support it

Evidence can mature through several incidents. One seized truck does not reveal a global organization.

A member's Exposure breach may create evidence for:

- the route host
- the country that performed the seizure
- a current war enemy with intelligence access
- a sanctioning coalition leader
- a country named by the breach event

The breach must remain bounded. It should never notify every ordinary country through a hidden whole-world loop.


---

## Source file: `03_smuggling_routes_and_network_growth.md`

# Smuggling Routes and Network Growth

## Route graph

The market is modeled as a sparse graph.

- Members and approved intermediaries are nodes.
- Smuggling routes are edges.
- Regional cells are connected components.
- A delivery must name one valid path through the graph.

The network can have several disconnected regional cells. These cells do not share full inventory or membership until an interregional route joins them.

Each route record stores:

- stable route ID
- route type
- origin member or broker
- destination member
- optional intermediary
- endpoint states or ports when relevant
- current status
- hidden capacity
- hidden reliability
- current route pressure
- current investigation owner when one exists
- supported cargo classes
- evolution requirement
- creation and latest refresh dates
- active delivery count
- one-time regional connection receipts

Capacity and reliability remain internal. The member sees a simple status, supported cargo class, current delivery time band, and current risk class.

## Public route states

| State | Meaning | Member consequence |
| --- | --- | --- |
| Open | The path can accept normal cargo | Normal offers and delivery timing |
| Strained | War, shortage, or scrutiny reduces throughput | Smaller lots, higher costs, longer deliveries |
| Disrupted | One endpoint or segment is temporarily unusable | No new dispatch, repair action available |
| Compromised | An observer holds evidence against the route | Severe seizure risk and Exposure pressure |
| Burned | The route was dismantled and cannot be reopened through ordinary repair | A new route proof is required |

A route cannot be both Open and Compromised as two independent flags. Compromised is a status with its own restrictions.

## Route families

### Land border route

A land route uses a direct border or a verified controlled corridor between the participating countries.

Useful factors:

- direct adjacency
- terrain and weather
- railway connection
- infrastructure
- state control
- resistance and compliance
- front-line proximity
- trucks and trains
- enemy occupation
- local intelligence pressure

Land routes are the safest baseline path when the border is stable. A front-line route can carry urgent cargo, but it should have lower capacity and higher seizure risk.

The route can be disrupted by loss of the endpoint state, a new hostile controller, railway destruction, a sealed border, or an active counter-smuggling operation.

### Neutral intermediary route

A neutral country or territory can relay goods without becoming a full member.

The intermediary needs a reason to cooperate, such as:

- commercial access
- corrupt officials
- currency arbitrage
- intelligence sponsorship
- political neutrality
- a large port or rail junction
- previous smuggling memory
- diplomatic access to both endpoints

The intermediary does not receive the member category. It can gain hidden route-host status and local evidence risk.

A neutral relay should be vulnerable to diplomatic pressure, sanctions, government change, war entry, and counterintelligence.

### Port and merchant-shipping route

A maritime route requires usable ports and a supported shipping connection.

Useful factors:

- port level and control
- convoy availability
- fuel
- naval supremacy and enemy raiding
- blockade or embargo
- distance
- access to neutral ports
- occupation status
- Event 55 corridor and port improvements
- Event 56 naval escorts or surplus convoys

Maritime routes can move larger cargo than improvised land crossings, but blockades and intelligence scrutiny can make them unstable.

A purchase that uses this route can require convoys and fuel as logistics costs. The route itself should not destroy convoys on every clean delivery. Convoy loss belongs to a failed or partially intercepted outcome.

### Occupied-territory corridor

An occupied route uses controlled foreign territory, collaborators, resistance channels, captured depots, or military transport offices.

Useful factors:

- controller and owner
- compliance
- resistance
- garrison strength
- military access
- current front
- local railways and supply hubs
- intelligence network strength

This route can be profitable because official records are already confused. It is also vulnerable to partisan action, occupation changes, and military investigations.

The route should not treat civilian harm as a direct Black Market effect. Any deaths, repression, or forced movement caused by a connected event remain owned by their existing systems.

### International corridor route

Event 55 can publish a route package for major railways, highways, tunnels, bridges, ports, and trade corridors.

A published corridor can:

- increase route capacity
- reduce delivery time
- connect otherwise distant members
- create a new intermediary node
- make a route more valuable to investigators

Event 57 reads only the approved corridor receipt. It does not inspect or take ownership of Event 55's project ledger.

### Covert air route

A covert air route is an emergency or evolved option.

It requires:

- suitable airbases
- aircraft or an owner-approved transport package
- fuel
- range
- a route that is not fully covered by hostile air control
- Evolution II or an explicit event-owned exception

Air routes deliver small, valuable cargo quickly. They are poor choices for bulk tanks, large fuel reserves, or major industrial shipments.

The route should carry high Exposure and severe loss risk. It exists for urgent equipment, intelligence, technical files, and small special packages.

## Route creation

A route can be created through:

- the founding transaction
- a successful invitation
- a member decision
- a route-repair mission
- an Event 55 corridor receipt
- an Event 56 convoy or escort package
- an owner-provided special route adapter
- a successful reconstruction pulse

Every creation requires endpoint proof and a stable route ID. Repeated calls must return the existing valid route or replace a proven obsolete record. They must not create duplicate parallel copies of the same route by accident.

## Route-opening missions

The following are working mission families.

### Secure a Land Crossing

The member commits trucks, trains, equipment, and local security to one named border or corridor.

The objective should depend on real state control, rail access, and unit or security presence. It should not auto-complete from a passive stockpile condition alone.

Suggested duration is `90-150` days, modified by terrain, war, infrastructure, and local control.

Success creates or upgrades the route. Failure increases Exposure, consumes part of the committed logistics, and can create outsider evidence.

### Charter Neutral Freight

The member builds a relay through a neutral commercial partner.

Requirements can include relations, port access, convoys, Market Credit, and a valid intermediary. The mission should be longer when the intermediary is ideologically distant, under pressure, or far from the endpoints.

Success creates a neutral relay. Failure can expose the intermediary without proving the full membership chain.

### Compromise a Port Authority

The member places brokers, dock officials, and shipping agents inside one port.

The action uses intelligence capacity, Market Credit, and a temporary civilian or convoy burden. It should be unavailable when the member has no route to the port.

Success creates a maritime endpoint. Failure can raise local investigation pressure and close the port to further attempts for a long cooldown.

### Reopen the Corridor

This mission repairs a Strained or Disrupted route.

The objective can require control of named states, restored railway access, a minimum supplied unit presence, or a logistics commitment. It should not be a simple political power payment.

### Emergency Air Bridge

This evolved mission opens one short-lived air route for a named delivery or invitation.

It uses fuel, aircraft or air capacity, and Market Credit. It carries a public Extreme risk class and cannot become the normal cheapest route.

## Route selection for a delivery

A delivery chooses a path after purchase validation.

Selection should consider:

- whether the path supports the cargo class
- capacity relative to lot size
- expected delivery time
- current reliability
- buyer and seller hostility
- embargo and blockade state
- logistics the buyer can provide
- Exposure impact
- active investigation
- current number of deliveries on the path

The player sees the selected route family, time band, risk class, and important reasons. The exact hidden chance is not shown.

A player can pay for a safer available route when more than one valid path exists. This is a route choice, not a direct purchase of success.

## Delivery timing

Suggested starting bands:

| Route | Small cargo | Medium cargo | Large cargo |
| --- | ---: | ---: | ---: |
| Land border | `25-50` days | `40-75` days | `60-110` days |
| Neutral relay | `45-80` days | `70-120` days | `100-160` days |
| Maritime | `40-75` days | `65-120` days | `90-180` days |
| Occupied corridor | `35-70` days | `60-110` days | `90-150` days |
| International corridor | `20-45` days | `35-70` days | `55-100` days |
| Covert air | `10-25` days | `20-45` days | Not normally valid |

Final duration is dynamic. Distance, infrastructure, port strength, war, blockade, route pressure, evolution, cargo class, and government posture should modify it.

## Delivery capacity

Capacity controls the largest offer that can use the route.

It should be derived from:

- route family
- endpoint infrastructure or ports
- member posture
- current evolution
- logistics commitment
- convoy, train, truck, fuel, and aircraft availability
- route pressure
- active deliveries

Capacity is not displayed as another number. The offer tooltip states whether the current route can handle Small, Medium, Large, or Exceptional cargo.

## Route disruption

A route can be marked for refresh by:

- war declaration
- peace or armistice
- state-controller change
- annexation
- capitulation
- port loss
- blockade
- embargo activation or removal
- faction change
- corridor completion or destruction
- member posture change
- investigation outcome
- exposure breach
- active delivery result

The event-owned refresh processes only affected routes.

A route that loses one temporary condition becomes Disrupted. A route whose endpoint no longer exists or whose intermediary permanently rejects cooperation becomes Burned.

## Route pressure

Route pressure is an internal value that combines traffic, scrutiny, blockade, war, and recent failures.

It affects reliability and delivery time. It should not be exposed as a fourth public meter.

Pressure rises through:

- several deliveries in a short period
- large cargo
- repeated use of one intermediary
- high member Exposure
- hostile naval or air control
- sanctions
- an active investigation

Pressure falls during quiet periods, after route investment, or when traffic shifts to another path.

Quiet-period recovery can run through a bounded route pulse over the registered route array.

## Transaction outcomes

A delivery can resolve in five main ways.

### Clean delivery

The buyer receives the full reserved package. The transaction receipt is settled. Exposure changes by the stated amount. Network Reach grows according to lot size and novelty.

### Delayed delivery

The cargo remains in transit. The mission extends once, route pressure rises, and the buyer can accept the delay, pay for rerouting, or abandon the package under the stated refund rules.

A delivery cannot be delayed forever. A second failure must resolve as partial loss, seizure, cancellation, or a route-specific final outcome.

### Partial delivery

The buyer receives a bounded share of the reserved package. The source remains fully debited because the missing cargo was lost or seized. Exposure and route pressure rise.

The player sees the delivered amount and lost amount.

### Seizure

The buyer receives no ordinary cargo. The observer gains an evidence receipt. The route becomes Compromised or Burned. Credit refund depends on whether the seller, broker, or buyer caused the failure.

A seizure can transfer part of the cargo to the seizing country only when the engine and transaction record support a clear captured-stockpile result. It must not duplicate the package.

### Sting or betrayal

This rare result requires Counterintelligence Penetration, mature evidence, or a proven hostile broker.

The buyer, seller, or intermediary may lose credit, contacts, or route access. One side gains evidence. The outcome never publishes the complete network.

## Exposure changes

Exposure should respond to actions, not drift without explanation.

Suggested starting bands:

| Action | Exposure change |
| --- | ---: |
| Small clean purchase | `+1` to `+3` |
| Medium clean purchase | `+2` to `+5` |
| Large or exceptional purchase | `+4` to `+9` |
| Verified sale | `+1` to `+5` |
| Neutral relay opening | `+2` to `+6` |
| Covert air delivery | `+6` to `+12` |
| Delayed delivery | additional `+2` to `+5` |
| Partial delivery | additional `+5` to `+10` |
| Seizure | `+10` to `+25` |
| Successful cover cleanup | `-4` to `-12` |
| Quiet registered-member pulse | `-1` to `-5` |

Posture, route type, cargo class, current investigation, war, and intelligence state modify these anchors.

At Exposure `100`, a breach incident must resolve before the value can rise again. The incident should reduce Exposure to a post-breach band so the member does not remain permanently locked at `100`.

## Network Reach changes

Suggested starting contributions:

| Outcome | Reach change |
| --- | ---: |
| Small clean delivery | `+1` |
| Medium clean delivery | `+2` |
| Large clean delivery | `+3` |
| Exceptional or first-of-class delivery | `+4` |
| New active member | `+2` |
| Reconnected lost member with restored route | `+1` |
| First route into a new region | `+5` |
| First connection between two regional cells | `+5` |
| Route upgraded to a higher cargo class | `+1` |
| Delayed delivery | `0` |
| Partial delivery | `0` or `-1` |
| Seizure | `-2` to `-5` |
| Route burned | `-3` |
| Member expelled | `-2` |
| Regional cell dismantled | `-5` to `-10` |

The same transaction cannot award Reach for several labels that describe the same fact. A first interregional connection can award its one-time route milestone plus the ordinary delivery value only when a real delivery also completed.

## Regional cells

A regional cell is a connected set of active routes and members.

The system should track:

- cell ID
- member count
- route count
- regions represented
- access to ports, land corridors, and air routes
- highest supported cargo class
- active investigations
- whether it is connected to another cell

Cell identity is internal. Members can receive a qualitative regional status without seeing the full graph.

## Joining cells

Evolution I makes deliberate interregional connection more likely.

A connection requires:

- two live cells
- one shared intermediary, corridor, maritime path, or air route
- enough Network Reach
- no unresolved breach at the endpoints
- route capacity for at least one medium cargo

The first completed connection creates one event-owned Chaos milestone described in the evolution and Chaos specification. The mere creation of a route proposal changes no Chaos.

## Dormancy and reconstruction

When a cell loses every active route, its members become dormant or former according to their local state.

Reconstruction can use:

- a surviving former member
- a known intermediary
- an Event 55 corridor
- a port that changed hands
- a new war or embargo
- a successful route-opening mission
- an invitation from another active cell

The reconstruction pulse should have a long base interval, such as `240-480` days, and should commit only one route attempt at a time.

## Full dismantling

A mature network cannot be dismantled by destroying one route.

Full dismantling requires a sequence of local victories that removes the network's ability to settle accounts and rebuild:

1. Active cells are reduced to zero.
2. No delivery remains in transit.
3. At least one high-confidence clearinghouse or broker-chain case succeeds.
4. Network Reach falls below the dismantling threshold.
5. A final event-owned dismantling effect clears reconstruction eligibility.

The full dismantling outcome is intentionally difficult. It creates a one-time negative Chaos source and a permanent history state.


---

## Source file: `04_inventory_trade_and_provider_api.md`

# Inventory, Trade, and Provider API

## Inventory principle

Every offer needs three proofs:

1. A source exists.
2. At least one active member can receive the cargo.
3. A valid route can move it.

An offer that lacks any proof does not appear. The system must not create fake seller stockpiles, placeholder equipment types, empty technology grants, or cargo that no member can use.

## Offer slots and rotation

| Event state | Maximum visible slots | Normal rotation interval |
| --- | ---: | ---: |
| Baseline | `3` | `45-75` days |
| Evolution I | `4` | `40-70` days |
| Evolution II | `5` | `35-65` days |
| Evolution III | `6` | `30-60` days |

Six is the hard maximum for one inventory phase.

A rotation can preserve one unsold offer when it remains valid and has not reached its expiry. It should replace invalid, expired, or repeatedly ignored offers. It should not reroll several times in one day to search for a perfect reward.

The interval should respond to:

- Network Reach
- number of active members
- number of active routes
- recent completed deliveries
- war and embargo pressure
- route disruptions
- provider availability
- recent inventory starvation
- recent repeated offers from the same class

All values must be centralized in the Event 57 tuning source.

## Offer record

Each slot should store a complete immutable offer receipt until it is replaced or purchased.

Required fields include:

- offer ID
- source package ID
- provider ID
- source class
- seller country when one exists
- hidden source identity state
- equipment or service class
- concrete equipment token or owner effect
- quantity
- quality or era band
- Market Credit price
- network fee
- optional logistics cost
- expected Exposure band
- valid route family
- expected delivery-time band
- buyer eligibility trigger
- creation date
- expiry date
- current reservation owner
- source-debit state
- transaction state
- project-completion isolation proof for special packages

A purchased offer becomes a transaction. It must not remain available to another buyer unless the source package explicitly represents several independent lots.

## Source classes

A member sees a provenance class, not necessarily a country name.

Useful classes are:

- member surplus
- diverted state reserve
- captured battlefield stock
- surrendered or collapsed-state stock
- neutral commercial diversion
- stolen industrial shipment
- recovered depot stock
- intelligence package
- technical dossier
- owner-approved experimental package
- unknown broker lot

The source class must be truthful. A member-surplus lot cannot be relabeled as captured stock merely to conceal a debit error.

## Baseline offer families

### Small arms

Includes valid infantry equipment tokens and closely related basic weapons.

Amount should derive from:

- verified seller surplus
- buyer deficit
- buyer army size
- route capacity
- world date and equipment generation
- recent imports that cannot be resold

A baseline offer should be large enough to equip a meaningful number of battalions, but should not erase a major country's full deficit through one small route. Small foreign or captured lots can use this family when their source receipt is valid.

### Support and artillery equipment

Includes support equipment, artillery, anti-tank, anti-air, and other ordinary support classes that the current equipment registry marks valid.

The system must validate the exact token and DLC state. It should not offer an archetype with no concrete equipment implementation.

### Trucks and trains

These are high-value logistics offers for countries whose supply system is constrained.

A seller must retain a dynamic reserve based on army size, active fronts, supply use, and current route commitments.

### Fuel

Fuel offers should scale to a number of days of current consumption.

Suggested handling bands:

- emergency lot: roughly `7-15` days of current consumption
- operational lot: roughly `15-30` days
- strategic reserve: roughly `30-45` days, later evolution only

The final amount is bounded by seller surplus or provider capacity, buyer storage, route capacity, and current evolution.

### Convoys

Convoy offers can come from member surplus, captured or surrendered stock, Event 56 packages, or verified commercial diversion.

A seller must keep enough convoys for active trade, supply, invasions, and route commitments.

### Intelligence

Baseline intelligence offers can provide one bounded temporary advantage against a named target.

Possible classes include:

- military estimates
- naval deployment information
- air-force estimates
- industrial estimates
- convoy route information
- mobilization plans
- local network access

The buyer must have a strategic reason to use the package. A generic global intelligence bonus is too broad.

## Evolution I offer families

Evolution I adds larger conventional military and logistics cargo. Small foreign and captured lots can already appear at baseline, while this evolution opens major battlefield and surrendered-stock packages.

### Tanks and armored vehicles

Offers require a valid concrete equipment token, source proof, buyer ability to use the equipment class, and a route that can handle heavy cargo.

The buyer does not need to own the source technology merely to deploy foreign equipment. The offer must not grant that technology.

### Aircraft

Aircraft offers follow the same source and buyer rules. Airframe and module compatibility must be checked against the installed DLC and equipment definition.

A buyer needs airbases and fuel before AI should value the offer highly.

### Larger artillery and transport lots

These packages can solve serious operational shortages. Their handling capacity should scale from the buyer's army, logistics, and route network.

### Captured wartime stockpiles

A captured-stock provider must publish a receipt before the source country, battlefield record, or surrender state is lost.

The receipt states:

- equipment class and token
- available amount
- captor or custodian
- whether the stock is already assigned elsewhere
- expiry
- source country when known
- whether the buyer can learn the source

Event 57 does not estimate destroyed armies and create stock from nothing.

## Evolution II offer families

### Embargo-circumvention contracts

These offers give isolated countries a temporary, route-backed way to obtain fuel, equipment, convoys, or strategic industrial inputs.

The contract should be valuable during Event 50 or a condemnation-based embargo. It should lose value or become invalid when ordinary trade access is restored.

### Industrial procurement

HOI4 does not treat most strategic resources as a country stockpile. Industrial-material lots should therefore use supported temporary procurement effects. Steel, aluminum, rubber, tungsten, and chromium cannot be assumed to exist as stored country units.

A procurement package can provide:

- temporary access to a resource source
- a bounded reduction in a named shortage
- temporary local or national resource extraction support
- a route-backed production contract
- construction material for one defined project family
- an owner-provided industrial effect

The effect needs a duration, source proof, route requirement, and cleanup.

### Naval packages

Ships and naval assets use Event 56 or another owner-provided adapter.

Valid packages may include:

- convoys
- naval equipment tokens
- a transfer of specific ships when the engine and owner contract support it
- captured hulls
- naval design information
- mines, escorts, or invasion support through an owner effect

Event 57 must not invent a generic ship-transfer fallback. When a package cannot be transferred safely, it is unavailable.

### Experimental equipment

Experimental and unusual equipment appears only through the approved provider registry.

Possible owners include:

- Brilliant Scientist systems
- Alien Technology in Antarctica
- chemical and biological warfare systems
- special projects
- unusual vehicles or aircraft
- experimental submarines
- future event-owned weapons

An owner decides which package can be traded, at which evolution, in what quantity, and with what consequences.

## Evolution III offer families

### Exceptional stockpiles

These are very large, source-backed military packages from collapsing powers, surrendered depots, major surplus releases, or event-owned caches.

The amount is limited by:

- verified source quantity
- route handling capacity
- buyer storage and organizational capacity
- recent market imports
- one exceptional-lot cooldown

The event should permit a dramatic military change when the source and route justify it. It should not hand every minor country a major power's full arsenal without handling limits.

### Strategic intelligence

These packages can reveal important plans, networks, research direction, naval deployments, or mobilization windows.

They need a named target, a bounded duration, a strategic use, and strong Exposure.

### Complete technical dossiers

A complete dossier can grant one normal technology only when all of these are true:

- the owner or normal technology registry marks it tradeable
- the technology is compatible with the buyer's tree
- it does not create a mutually exclusive conflict
- the buyer does not already hold it
- the package has a verified source
- the current evolution permits it
- the buyer completes the delivery

Partial dossiers should normally give a research bonus or ahead-of-time reduction instead of the full technology.

The broad shared technology-union helper is not appropriate for one Black Market offer because it grants every compatible missing technology from a donor. Event 57 needs a bounded single-package contract.

### Rare owner packages

Evolution III can admit high-value assets such as special-project equipment, unusual weapons, event-owned technology, or unique intelligence.

Every package remains owner-controlled. Anything Has a Price is an access tier, not permission to bypass another system's lifecycle.

## Member surplus sales

Selling is a real stockpile transaction.

The member selects a supported sale family. The system calculates a saleable amount above a readiness reserve, presents the amount and credit return, then debits the source before publishing the lot.

A sale must fail closed when the debit cannot be proven.

### Dynamic readiness reserve

The reserve should consider:

- deployed army and air force
- active fronts
- war state
- mobilization plans
- current deficits
- fuel consumption
- convoy commitments
- trains and trucks required for supply
- equipment already reserved for another transaction
- recent market imports
- member posture

A country at or below its reserve cannot sell that category.

State Patronage can lower the safety margin, but it cannot reduce it to zero for essential equipment.

### Sale amount bands

The member can choose a Small, Medium, or Large sale when enough surplus exists.

The exact amounts are dynamic. A Large sale should represent a larger share of surplus and create more Exposure, not a fixed universal number.

### Source debit timing

The seller's stockpile is debited when the offer becomes committed for sale, not when the buyer receives it.

Possible transaction states are:

1. listed and not reserved
2. reserved by buyer
3. debited and dispatched
4. settled
5. canceled before debit
6. lost after debit

A seller cannot cancel after dispatch and recover the goods.

### Seller proceeds

The seller receives Market Credit only when the lot is reserved and the source debit succeeds.

A portion of the buyer's price becomes a network fee. Suggested starting seller yield is `60-80%` of the buyer's Market Credit price, modified by posture, scarcity, route risk, and broker role.

This spread is an important anti-arbitrage sink.

## Recently imported equipment lock

A buyer cannot immediately resell the same market cargo for profit.

Each completed purchase adds a category-level recent-import ledger amount. That amount is subtracted from the country's saleable surplus for a long lock period, suggested at `365` days.

The lock can reduce earlier when the equipment is demonstrably consumed or lost through an owner-supported receipt. It must not require scanning every individual item.

A recent-import lock follows the equipment category and transaction ID. Repeated purchases add to the locked amount without duplicating the receipt.

## Market Credit economy

### Sources

Valid credit sources include:

- verified equipment and fuel sales
- brokerage missions
- route service for another member
- intelligence contributions
- limited government underwriting
- a Grand Auction refund or settlement
- owner-approved event payments

### Government underwriting

A country with no saleable surplus needs a bounded way to enter the market.

A working decision family can commit civilian industrial capacity for `90-180` days in exchange for Market Credit. The amount scales from the country's economy and current credit cap. It has a long cooldown and increases Exposure under State Patronage.

Underwriting is not an unlimited credit exchange. It should not let a rich major buy the entire inventory every rotation.

### Credit cap

The cap should scale from:

- civilian and military factory total
- current evolution
- government posture
- completed settlements
- broker role

The implementation should use a floor and cap so small countries can participate while major countries cannot store limitless credit.

A transaction that would exceed the cap should show the payable amount before confirmation. Excess value can remain unsold or be converted into a smaller lot. It should not disappear after the player commits unknowingly.

### Credit on withdrawal and expulsion

- Voluntary withdrawal locks the remaining credit and settles a network fee.
- Dormancy preserves locked credit.
- Reconnection restores only the surviving balance.
- Suppression forfeits a larger share and can turn it into counter-smuggling resources.
- Expulsion freezes or confiscates the balance according to the betrayal outcome.
- Annexation does not transfer the credit automatically to the annexer.

## Pricing

Price should derive from equipment value, quantity, scarcity, source class, route risk, delivery time, and current evolution.

Useful price tendencies:

- member surplus is cheaper than a commissioned shortage lot
- collapsed-state and captured stock can be discounted
- embargo pressure creates a markup
- a dangerous route can lower the posted price while increasing expected loss and Exposure
- technical dossiers and intelligence use strategic value for pricing
- an exceptional lot includes a high network fee

The player sees the final Market Credit cost and all additional spendable costs. Internal valuation components stay in the tooltip only when they explain a material difference.

## Cost budget

A purchase or sale action can use at most four spendable cost types. Most offers should use two or three.

Typical purchase costs are:

- Market Credit
- one route-specific logistics cost, such as convoys, trains, trucks, fuel, or aircraft capacity
- an optional temporary civilian-factory burden for handling or concealment

Exposure is a consequence, not a spendable cost.

A route requirement such as controlling a port is a requirement, not a cost.

Every visible cost needs the correct texticon. Market Credit requires its own texticon before the decision can ship.

## Demand weighting

Inventory generation should respond to registered member demand.

Demand inputs include:

- equipment deficits
- fuel days
- convoy and train shortages
- current war
- planned invasions
- airbase and port capacity
- legal market access
- embargoes
- current offers
- recent purchases
- technology and equipment compatibility
- AI strategy

The global demand model can aggregate only active members. It does not need a world scan.

A baseline rotation should try to include at least one broadly useful logistics or small-arms lot when a valid source exists. It should not guarantee a reward when no source exists.

## Commissions

Evolution I unlocks a commission action.

A commission lets one member influence the next rotation toward one broad class, such as small arms, fuel, transport, armor, aircraft, intelligence, or industrial procurement.

It does not select an exact token or guarantee success.

The action uses Market Credit, has a cooldown, increases route pressure, and can fail when no valid source enters the registry.

A failed commission should refund part of the credit and explain that no supplier accepted the request. It must not generate fake stock to satisfy the player.

## Grand Auction

Evolution III unlocks a recurring Grand Auction mission for one exceptional lot.

The auction should occur at a long interval, suggested at `180-360` days, only when a valid exceptional provider package exists.

Members submit bids based on:

- Market Credit
- route handling capability
- strategic need
- Exposure tolerance
- government posture
- trust

The player receives the lot details, minimum handling requirement, bid cost, expected Exposure, and settlement date. Other bidder identities remain hidden.

The winner pays the committed bid and receives a delivery job. Losing bidders receive the documented refundable share after settlement. A bid cannot exceed the bidder's current credit or route capacity.

AI must not bid for prestige alone when it cannot use the cargo.

## Technology isolation

Receiving equipment never grants its technology.

Receiving a research bonus does not mark a source project complete.

Receiving an owner-approved special technology does not fire the source event, set the source event's completion flag, unlock unrelated source branches, or count as winning the source project.

The provider receipt must state which exact effect is allowed.

## Condemnation and dangerous packages

A chemical, biological, nuclear, atrocity-linked, or otherwise condemned package can appear only when its owner permits trade.

The provider must state:

- whether possession is public or hidden
- whether delivery creates condemnation
- whether use creates condemnation through the existing owner system
- whether a seizure exposes the buyer or seller
- whether special storage or equipment support is required

Event 57 does not create a second condemnation ledger. It calls the owning consequence path when the approved transaction requires it.

## Provider registry

The Black Market needs an event-owned public provider API so other events can offer packages without giving Event 57 ownership of their systems.

Suggested owner files:

- `common/scripted_effects/057_the_black_market_provider_effects.txt`
- `common/scripted_triggers/057_the_black_market_provider_triggers.txt`
- `docs/events/057_the_black_market/systems/provider_api.md`

The shared dynamic-effects registry can index this API for discovery. It should not copy the event-owned implementation.

## Provider package contract

Every package registers:

| Field | Required meaning |
| --- | --- |
| `provider_id` | Stable owning event or system |
| `package_id` | Stable package identity |
| `offer_class` | Equipment, fuel, intelligence, industrial, technology, naval, or special |
| `minimum_evolution` | Earliest allowed Event 57 evolution |
| `availability_trigger` | Source-world condition that must still be true |
| `buyer_trigger` | Countries allowed to receive it |
| `source_debit_effect` | Exact stockpile or owner-ledger debit |
| `delivery_effect` | Exact buyer effect after successful settlement |
| `quantity_rule` | Dynamic amount and bounds |
| `price_rule` | Market Credit valuation |
| `route_rule` | Supported route classes and capacity |
| `exposure_rule` | Expected transaction risk |
| `reveal_rule` | Evidence and public-consequence behavior |
| `completion_isolation` | Proof that source lifecycle remains unchanged |
| `DLC_rule` | No-DLC and enhanced paths |
| `cleanup_rule` | Invalidation, expiry, annexation, and duplication handling |

Missing required fields make the package unavailable.

## Request and receipt flow

A provider request should be versioned and fail closed.

Conceptual flow:

1. Event 57 submits a package request with a unique request ID.
2. The owner validates current availability and buyer eligibility.
3. The owner returns a bounded offer receipt.
4. Event 57 stores the receipt in one inventory slot.
5. Purchase reserves the receipt.
6. Dispatch calls the owner debit once.
7. Successful delivery calls the owner delivery effect once.
8. Settlement returns a final status to the owner.
9. Expiry or invalidation clears the request without changing the source system.

Public inputs and outputs should be reset after each call. A stale request must not be reused for a different buyer.

## Provider safety

The API must prevent:

- a missing source from creating goods
- the same source package being sold twice
- a buyer receiving an incompatible token
- a seller avoiding the debit
- Event 57 completing the source event
- an unapproved experimental package entering the pool
- a package remaining valid after its owner removes permission
- a DLC-only token appearing without its DLC
- a delivery effect firing twice after reload

## Event connection adapters

### Event 50: The Great Embargo

Event 50 publishes target and restriction pressure. Event 57 uses that proof to raise demand, mark embargo-circumvention offers, alter invitation scoring, and create the related Chaos milestone after a successful delivery.

Event 57 does not remove the embargo.

### Event 54: Gift from Scientists

Event 54 can move advanced normal technology into world circulation earlier. Event 57 can then find equipment produced by countries that possess those technologies.

Event 54 does not automatically create a Black Market lot. A country or owner still needs to publish real equipment or a technical package.

### Event 55: The Great Infrastructure Project

Event 55 can publish ports, railways, highways, tunnels, bridges, and trade corridors as route assets.

Event 57 reads the route receipt and leaves project ownership with Event 55.

### Event 56: The Navy

Event 56 can publish convoys, captured naval assets, unusual naval equipment, or supported ship-transfer packages.

Event 57 accepts only packages that Event 56 marks tradeable and safe.

### Wars, occupations, and collapse

War and surrender systems can publish captured or abandoned stock before their source records disappear.

Event 57 does not infer exact equipment from casualties, deaths, annexation, or a country ceasing to exist.

## International market distinction

Where the Arms Against Tyranny international market is available, the Black Market remains separate.

The legal market is public and follows legal access, seller visibility, and ordinary restrictions. The Black Market uses invitation-only membership, Market Credit, hidden source classes, route jobs, Exposure, seizures, and owner approvals.

The DLC path may reuse verified valuation or equipment-compatibility logic when safe. It must not expose Black Market offers on the legal market or require the DLC for Event 57's core loop.


---

## Source file: `05_decisions_missions_and_player_loop.md`

# Decisions, Missions, and Player Loop

## Presentation layer

The member experience uses one hidden decision category with a static category picture that changes by evolution.

The category is visible only to:

- active members
- dormant or suspended members with remediation actions
- former members with a live reconnection offer

Outsiders do not receive this category. A country with evidence against one route receives a separate temporary counter-smuggling category tied to that case.

The category header shows:

- Market Credit
- Exposure
- Network Reach
- current government posture
- primary route status
- next offer-rotation date or current delivery mission

Market Credit, Exposure, and Network Reach are the only persistent custom values the member must actively track.

## Clarity budget

A normal phase should show three to five primary actions. Six is the absolute maximum.

The category should show one to three active missions.

When the inventory has more offers than the action budget can show cleanly, use a selected-offer flow:

1. one selector action cycles or selects an offer
2. only the chosen offer's details and purchase action are active
3. one close action clears the selection
4. AI evaluates every valid offer directly without using the player selector

The implementation must not solve clutter by creating several similar categories or a decorative full-screen interface.

## Category phases

### Active trading

Visible content normally includes:

- current offer access
- list surplus
- route action
- government posture action
- Exposure response when relevant

### Delivery in progress

The category replaces weak actions with:

- active delivery mission
- reroute or reinforce delivery when valid
- current route status
- one continuing trade action when capacity remains

### Dormant network access

The category shows:

- restore a route
- contact a former sponsor
- reconcile locked credit
- withdraw permanently

Normal offers are hidden.

### Suspension

The category shows only the actions that address the suspension reason, such as settle an account, replace a compromised route, cooperate with an inquiry, or withdraw.

### Suppression campaign

Normal trading disappears. The category shows the local route and intermediary objectives required to dismantle the cell.

## Purchase flow

A purchase should use the following player sequence:

1. Review the offer class, amount, quality band, provenance class, price, route family, delivery-time band, and risk class.
2. Confirm that the buyer can pay the visible costs and use the cargo.
3. Reserve the offer.
4. Debit Market Credit and any immediate logistics commitment.
5. Dispatch the source package through its provider receipt.
6. Start the delivery mission.
7. Resolve success, delay, partial loss, seizure, cancellation, or sting.
8. Settle the receipt once.

The purchase tooltip must explain all visible costs, the expected Exposure increase, the delivery-time band, and the main blocked reason. It should not reveal the exact hidden outcome chance.

## Purchase decision families

Working design labels are used below. Implementation should write final localisation from their purpose.

### Acquire Current Lot

This is the main offer purchase action.

It changes with the selected offer and uses dynamic localisation for:

- equipment or service class
- amount
- price
- route
- risk
- delivery time
- blocked reason

One generic decision should not expose raw internal equipment tokens.

### Reserve the Lot

High-demand or auction-linked offers can require a short reservation step. Reservation commits credit but does not dispatch until route proof passes.

Reservation is useful only when it creates a real contest or route problem. Ordinary small offers should not require an extra click.

### Commission a Category

Evolution I unlocks a request for one broad offer family in the next rotation.

The action has a long cooldown, Market Credit cost, and partial refund when no supplier appears.

### Arrange a Safer Route

When two paths are valid, the member can commit extra logistics or credit to use the safer path. This changes time, cost, and risk. It does not guarantee success.

### Accept the Dangerous Route

A member can choose the high-risk path when the cargo is urgent. The tooltip must state the risk class and likely Exposure consequence plainly.

## Sale flow

### List Surplus

The member chooses one valid sale family.

The action opens a bounded report with only categories that have verified surplus. The player chooses Small, Medium, or Large where the reserve supports them.

The final confirmation states:

- exact amount to be removed
- protected reserve after the sale
- expected Market Credit return
- expected Exposure
- listing duration
- whether the lot can expire unsold

### Withdraw an Unsold Lot

A seller can withdraw before reservation. The stock returns only when it was never debited or dispatched.

The action has a cooldown to prevent free inventory manipulation.

### State Reserve Release

State Patronage can list a larger government lot. This action has higher Exposure and a stricter readiness check.

### Contribute Intelligence

A member with usable intelligence can publish a bounded information package through the provider API and receive credit after another member buys it.

The action must not expose all agency or operative state to Event 57.

## Route decisions

### Open a New Route

The member selects a valid route family based on geography and evolution. The action starts the relevant mission.

### Repair a Disrupted Route

The action creates a state, port, or logistics objective. It should auto-complete when the player satisfies the condition.

### Shift Traffic

A member with more than one route can move future deliveries away from a pressured path. This lowers pressure on one route and raises it on another.

### Burn the Route

A member can permanently destroy one compromised route to reduce Exposure. The action also reduces Reach and can strand a delivery. It must ask for confirmation when a transaction is still in transit.

## Exposure decisions

### Compartmentalize the Cell

The member spends Market Credit and temporary administrative or intelligence capacity to remove compromised contacts.

It lowers Exposure, reduces route capacity for a period, and can delay the next offer rotation.

### Replace the Manifests

A route-specific action lowers investigation pressure and changes the cargo cover. It is effective only once per investigation episode.

### Sacrifice an Intermediary

A severe action can save a route or government identity by burning one broker. It destroys trust, reduces Reach, and blocks that intermediary from immediate reuse.

### Cooperate with an Inquiry

A penetration or legalist government can allow a bounded investigation. This can lower national Exposure while creating evidence against one route or counterparty.

### Deny State Involvement

State Patronage can attempt to isolate the scandal from the government. Success preserves access. Failure creates harsher evidence and diplomatic effects.

## Government posture decisions

Posture changes should use one selector or event choice. Four permanent buttons would clutter the category.

The player sees:

- current posture
- public effect direction
- change cooldown
- immediate cost or consequence
- route and offer changes

The decision should not reveal hidden infiltration detection chances.

## Delivery missions

### Standard Delivery

Every dispatched purchase starts a visible timed mission.

The mission shows:

- cargo class
- expected arrival range
- current route state
- public risk class
- one or two actions that can materially change the route

The mission auto-completes on settlement. The player does not pay a second click to receive goods.

### Route Security Objective

A large land or occupied-corridor delivery can require the player to hold named states, keep a railway connected, or place supplied divisions along the route.

The objective should use a duration of at least `90` days when the player must move units or repair infrastructure.

Success improves the delivery outcome. Failure can spare part of the cargo while creating a substantial risk increase.

### Escort the Freight

A maritime delivery can require convoys, fuel, and a naval-security condition. Where direct naval supremacy checks are supported, the mission can read them. Otherwise it should use verified convoy and escort proxies.

### Clear the Air Corridor

A covert air delivery can require airbase control, fuel, and a minimum air condition. It is a short emergency mission with severe Exposure.

### Delivery Crisis

A delayed or compromised transaction can create one short follow-up mission. The member chooses to reinforce, reroute, abandon, or accept partial delivery.

A transaction cannot create an endless chain of rescue missions.

## Brokerage missions

### Move Another Member's Cargo

A broker country can earn Market Credit by carrying a delivery between two other members.

The broker commits route capacity and accepts Exposure. It does not learn both endpoint identities unless the route contract requires it.

### Restore a Regional Link

A broker can reconnect two cells through a named port, border, or corridor. Success creates Reach and can prepare Evolution I.

## Grand Auction mission

Evolution III can create one exceptional-lot auction.

The mission sequence is:

1. a valid provider publishes the lot
2. eligible members receive a private bidding event
3. each member submits one bid or abstains
4. the auction closes after a fixed short window
5. the winner and losing refunds are recorded
6. the winning route is validated
7. the delivery begins

The auction should not display a list of member countries or bids.

A player can improve a bid through one bounded action, such as providing better handling capacity or accepting greater Exposure. It should not become a repeated click competition.

## Outsider discovery

An outsider receives no counter-smuggling actions without evidence.

Evidence can come from:

- a seized shipment in owned or controlled territory
- a compromised route through one of its ports
- an intelligence operation
- a member's Exposure breach
- a courier or intermediary arrest
- a former member sharing records
- an owner event that publishes a valid evidence receipt

The first evidence event identifies one case, not the whole network.

## Temporary counter-smuggling category

The category is tied to one known route, intermediary, or member.

It shows:

- evidence confidence as a qualitative state
- known route or cargo class
- investigation deadline
- current action

Evidence confidence can remain internal if the qualitative state and blocked reasons are clear. It should not become a fourth persistent Black Market meter for outsiders.

## Outsider decision families

### Inspect Suspicious Cargo

The country commits customs, intelligence, or military resources to one route endpoint.

Success can seize one shipment or increase evidence. Failure raises route caution and can close the case.

### Watch the Rail Depots

The country places a real state or railway objective on a known corridor.

### Pressure the Intermediary

The country uses diplomacy, sanctions, or security pressure against one proven intermediary.

This action should not reveal countries with no evidence connection.

### Turn a Broker

An intelligence-backed action can convert one intermediary into a source. It is unavailable without sufficient evidence and an intelligence basis.

### Coordinate a Seizure

A mature case can target one active delivery. Success creates a seizure result and route damage. Failure can expose the investigation.

### Dismantle the Local Cell

This is a capstone objective that requires several completed proofs, no active unresolved delivery, and control over the relevant route area.

Success removes the regional route set. It does not automatically end the global network.

## Suppression campaign missions

A member that starts Suppression uses its local knowledge against the network.

The campaign should normally include two or three objectives selected from:

- seize the local clearing account
- close the primary route
- arrest or turn the intermediary
- secure the depot
- prevent one evacuation delivery
- expose a foreign sponsor

The player should not see every possible mission at once.

Partial success can burn the route but fail to expose the clearinghouse. Failure can lead to expulsion and retaliation.

## Decision costs

Costs should match the action.

Useful cost families include:

- Market Credit
- convoys
- trains
- trucks
- fuel
- infantry or support equipment
- civilian factory burden
- army, navy, or air experience
- command power within the project's conservative cap
- political power for real government or diplomatic actions
- stability or war support as a consequence of public exposure
- temporary intelligence exposure
- tied-down divisions through mission requirements

A single action can use no more than four spendable cost types.

Costs must be icon-first and use matching texticons. Requirements such as holding a port or fielding supplied divisions belong in the requirement tooltip.

## Effects that should feel meaningful

A purchase should solve a visible military or logistics problem, create a strategic option, or provide useful intelligence.

A sale should convert genuine surplus into enough credit to matter.

A route mission should open, restore, or protect an actual path.

An Exposure response should save access, reduce risk, or sacrifice capability.

Avoid decisions whose whole result is a tiny generic modifier, a trivial amount of political power, or a token stockpile.

## Decision cleanup

The event-owned cleanup contract must remove or replace decisions when:

- an offer expires
- a selected offer is bought or invalidated
- a route disappears
- a country leaves membership
- a member becomes dormant or suspended
- a posture changes
- a delivery settles
- an investigation closes
- a target country disappears
- a known intermediary changes government or enters war
- the network is dismantled

No stale target, route, offer, or transaction decision should remain visible.

## AI equivalents

Every action available to AI members must have an AI path that does not depend on clicking a player-only selector.

The AI should:

- evaluate all valid offers
- buy only strategically useful cargo
- respect protected reserves when selling
- choose route missions it can complete
- respond to high Exposure
- avoid impossible state or port objectives
- use penetration only with intelligence capacity
- avoid suppression when an existential shortage makes withdrawal irrational
- abstain from auctions it cannot handle

Detailed scenario expectations are defined in the AI and balance specification.


---

## Source file: `06_evolutions_chaos_cluster_and_connections.md`

# Evolutions, Chaos, Cluster Behavior, and Connections

## Evolution model

The three evolutions are paced global network milestones.

They use one evolution track with three stages. Ordinary changes in Network Reach, membership, routes, offers, and deliveries are baseline progression and do not create evolution log entries.

Each evolution requires:

- its Chaos threshold
- the previous evolution where applicable
- a live network
- a Network Reach threshold
- a membership and regional proof
- an enabled evolution setting
- an event-owned MTTH process

Evolution activation changes no Chaos by itself.

The current Reach can continue growing before the Chaos threshold, but offer classes remain capped by the active evolution.

## Evolution I: International Network

- Chaos requirement: `200+`
- Network Reach requirement: `35+`
- Suggested base MTTH: `120` days

Readiness requires one of these network shapes:

- at least five active members across at least two regions with three active routes
- at least eight active members in one region with five active routes and a proven maritime or neutral relay

Useful MTTH factors:

- shorter after the first regional-cell connection
- shorter during several simultaneous wars or embargoes
- shorter after two large clean deliveries
- longer after a breach
- longer when average member Exposure is high
- blocked when every route is Disrupted or Compromised

### Capabilities

Evolution I unlocks:

- four inventory slots
- tanks and armored vehicles
- aircraft
- larger fuel, convoy, artillery, truck, and train lots
- verified captured wartime stockpiles
- direct commissions for a broad offer class
- two active routes per established member when route proof exists
- faster membership growth
- deliberate links between regional cells
- direct transactions between known members when both accept identity disclosure

### Member experience

The market begins to feel international. Members see more distant provenance classes, larger cargo, and more route choices. A member still does not receive the complete membership list.

### Evolution text direction

The report should focus on cargo appearing from several regions, new shipping marks, unfamiliar weapons, and brokers offering routes that no local cell could have built alone.

Do not describe the evolution as a generic upgrade or announce every unlocked category in prose.

## Evolution II: The Underground Economy

- Chaos requirement: `400+`
- Network Reach requirement: `65+`
- Suggested base MTTH: `180` days

Readiness requires Evolution I and one of these proofs:

- at least eight active members across three regions, with one embargoed or heavily isolated member
- at least fourteen active members across two regions, ten completed deliveries, and one mature neutral relay

Useful MTTH factors:

- shorter while Event 50 targets an active member
- shorter after a successful large embargo-circumvention delivery
- shorter when Event 55 corridors connect cells
- longer after several seizures
- longer when the network has no valid industrial or specialist provider

### Capabilities

Evolution II unlocks:

- five inventory slots
- industrial procurement contracts
- stronger embargo-circumvention packages
- owner-approved experimental equipment
- owner-approved chemical or biological equipment
- owner-approved special-project equipment
- naval packages through Event 56 or another verified owner
- technical dossiers and advanced intelligence
- covert air routes
- three routes for a mature broker when route proof exists
- stronger reconstruction after a regional collapse

### Owner boundary

An experimental package can appear only after its owner registers it. Delivery does not complete the owner event or project.

Possession and use consequences remain owned by the source system.

### Member experience

The network becomes an alternative economy for isolated states. Members can work around major restrictions, but exceptional transactions produce high Exposure and attract state-level countermeasures.

### Evolution text direction

The report should show ordinary restrictions losing force through layered routes, substitute paperwork, neutral warehouses, and cargo whose origin cannot be explained through legal trade.

Avoid direct claims that every embargo can now be ignored. Access remains route-backed and finite.

## Evolution III: Anything Has a Price

- Chaos requirement: `600+`
- Network Reach requirement: `85+`
- Suggested base MTTH: `240` days

Readiness requires Evolution II and one of these proofs:

- at least twelve active members across four regions, twenty completed deliveries, and two interregional links
- at least twenty active members across three regions, thirty completed deliveries, and one exceptional provider package

Useful MTTH factors:

- shorter after a successful transaction between active enemies
- shorter after an approved experimental delivery
- shorter when several major powers are embargoed or at war
- longer after a regional cell is dismantled
- blocked while the network is dormant

### Capabilities

Evolution III unlocks:

- six inventory slots
- exceptional military stockpiles
- strategic intelligence packages
- complete normal-technology dossiers where approved
- rare owner-approved equipment and technology
- Grand Auctions
- higher-capacity and more frequent transactions between active enemies through masked brokers
- broader cross-regional route recovery
- the highest Market Credit and handling caps

### Member experience

A member can obtain assets that would normally be unavailable through diplomacy, ideology, faction, or legal trade. The strongest offers remain rare, source-backed, expensive, and difficult to move.

### Evolution text direction

The report should emphasize the market's confidence and range through specific objects and routes. It should not use abstract language about omnipotence or reveal a central organization that does not exist.

## Evolution pacing and logging

The shared evolution context should record Event 57, one network-evolution type, the correct stage, tier, and no actor.

Disabled evolutions must not:

- set their recorded flags
- raise the offer-slot cap
- unlock provider classes
- shorten invitation cadence
- enable Grand Auctions
- raise route limits

Baseline trading must continue safely when an evolution is disabled.

## Chaos impact map

Event 57 is classified as a beneficial economic event. Its secret growth can still increase global instability when it materially defeats ordinary restrictions or connects enemies.

### Zero-Chaos state changes

The following always give zero direct Chaos:

- first firing and founding invitations
- accepting or rejecting membership
- normal small and medium trades
- ordinary Network Reach gain
- normal route creation within one region
- evolution eligibility
- evolution activation and logging
- inventory rotation
- Market Credit gain or spending
- a government posture change

### Positive Event 57 Chaos sources

| Milestone | Starting Chaos | Proof and guard |
| --- | ---: | --- |
| First completed interregional route and delivery | `+5` | One-time global receipt, requires two previously disconnected regional cells and a settled delivery |
| First successful transaction between countries actively at war with each other | `+5` | One-time global receipt, requires hostile scopes at dispatch and settlement through a neutral or masked route |
| First successful major embargo-circumvention delivery | `+5` | One-time global receipt, requires an active Event 50 or shared strategic embargo proof and meaningful cargo |
| First approved experimental package delivered | `+10` | One-time global receipt, provider marks the package experimental and delivery settles |
| First exceptional stockpile delivered | `+5` | One-time global receipt, requires Evolution III and the exceptional-lot provider class |
| First network connection across four regions | `+10` | One-time global reach milestone, requires active route-backed cells in four regions |

Values are tuning anchors. A provider can request a different bounded amount when its package has clearly greater or lower abnormal significance.

### Negative Event 57 Chaos sources

| Reversal | Starting Chaos | Proof and guard |
| --- | ---: | --- |
| Mature regional cell dismantled | `-5` | Once per cell, requires active routes and meaningful prior trade history |
| Whole network reduced to verified dormancy after International Network or later | `-5` | One-time per dormancy episode with cooldown, no active routes or deliveries |
| Full network dismantled | `-10` | One-time campaign receipt, requires final dismantling proof |

A reconstruction after dormancy does not repay the same Chaos milestone automatically. It must reach a genuinely new milestone to generate another event-owned source.

### Shared-source overlap

Event 57 must not duplicate Chaos already produced by:

- wars
- annexations
- puppeting
- faction changes
- deaths
- air contamination
- nuclear use
- chemical or biological use
- condemnation
- world tension
- military buildup

For example, a seized chemical shipment may create Event 57 Exposure and route consequences, while chemical use or public responsibility remains in the CBRN and Condemnation systems.

## Positive Economy cluster

Event 57 is a High member of Positive Economy.

Its cluster role reflects the scale of the benefit available to participating countries. It does not mean the event is safe, public, or universally accessible.

The Positive Economy cluster remains a separate repeatable root. Event 57 retains its fire-once lifecycle.

When Event 57 fires through a cluster:

- the cluster counts as one global pacing event
- Event 57 creates its founding network once
- Event 57 records its own fire-once history and weight removal
- optional member outcomes do not create extra pacing transactions
- the founders remain hidden

## Cluster interaction with Resources Found

The current Positive Economy design includes Event 18, Resources Found.

When both events participate in one cluster incident, their connection can use an owner adapter:

- Event 18 publishes one tradeable resource or industrial opportunity
- Event 57 can use it as an initial industrial-procurement source when a route and buyer exist
- Event 57 does not take ownership of the resource field
- Event 18 does not automatically reveal the Black Market
- a missing or invalid provider receipt means no connected offer

When Event 18 is selected first and Event 57 remains unfired, Event 57 can be considered as an optional High member only when a valid founding cell exists.

When Event 57 is selected first, Event 18 can provide an optional economic source according to the cluster's member rules.

## Event 50: The Great Embargo

Event 50 is the strongest ordinary connection.

An active embargo against a member should:

- raise invitation acceptance
- increase demand for fuel, convoys, military equipment, and industrial procurement
- increase scarcity prices
- raise the value of neutral and maritime routes
- shorten commission and invitation intervals within limits
- create the first major embargo-circumvention Chaos milestone after a successful delivery
- increase outsider investigation pressure when the route is exposed

Event 57 does not cancel, weaken, or mark Event 50 complete.

## Event 54: Gift from Scientists

Advanced technology from Event 54 can cause later equipment to enter world production earlier.

Black Market inventory should respond only after a country has produced, captured, or registered a valid package. Research alone does not create a free lot.

## Event 55: The Great Infrastructure Project

Major ports and international corridors can:

- create route candidates
- improve capacity
- shorten delivery time
- reconnect regional cells
- become valuable investigation targets

The Event 55 owner publishes the route asset and keeps project ownership.

## Event 56: The Navy

Event 56 can provide:

- surplus convoys
- escort capacity
- unusual naval equipment
- captured hulls
- supported ship transfers
- naval intelligence

Every package needs a route and owner receipt.

## Wars and collapsing countries

Wars increase both demand and supply.

Potential sources include:

- surrendered depots
- captured equipment
- abandoned stock
- surplus after demobilization
- occupation diversions
- collapsing government reserves

A war outcome must publish a bounded package before source data disappears. Event 57 never estimates the stock from casualties alone.

## Intelligence systems

La Résistance can deepen:

- invitation discovery
- broker penetration
- evidence maturity
- strategic intelligence packages
- route protection
- stings

The no-DLC path uses supported base-game intelligence, political, and temporary military effects. Core membership, trade, routes, and counterplay remain available.

## Condemnation and sanctions

Condemnation can increase demand and reduce legal trade access.

A public seizure of forbidden goods can add condemnation only through the owning consequence system. Event 57 provides the transaction, buyer, seller when known, route, and evidence receipt.

## Famine and migration

A future approved adapter could allow humanitarian contraband such as food, medicine, transport, or evacuation capacity.

The adapter must remain versioned and proof-carrying. Event 57 must not read or modify famine reserves, migration cohorts, or humanitarian ledgers directly.

This connection should be implemented only when the owning systems define a valid package and consequence contract.

## Future provider standard

Any future event that creates tradeable equipment, intelligence, technology, fuel, convoys, industrial access, or restricted resources should decide whether it exposes a Black Market package.

The owner's decision must state:

- what can be traded
- when it becomes available
- who can receive it
- how much exists
- how the source is debited
- what delivery does
- what discovery does
- whether use triggers another consequence
- whether the source event remains incomplete


---

## Source file: `07_ai_probability_balance_and_edge_cases.md`

# AI, Probability, Balance, and Edge Cases

## AI design goal

AI countries should use the Black Market to solve real strategic problems and dispose of real surplus. They should not join, buy, sell, sponsor, suppress, or bid merely because an action is available.

AI decisions must respect:

- membership state
- route validity
- current war
- equipment deficits and reserves
- fuel and convoy position
- legal market access
- embargoes
- government posture
- stability and war support
- intelligence capacity
- Network Reach
- Exposure
- provider permissions
- current delivery capacity
- active investigations
- recent transaction history

## AI strategic roles

The system can derive one or more hidden roles for each member.

### Desperate buyer

Typical conditions:

- at war
- major equipment or fuel deficit
- poor legal market access
- embargoed or isolated
- valid route

Behavior:

- accepts invitations readily
- values useful current offers
- tolerates higher Exposure
- invests in route security
- avoids selling essential stock

### Surplus seller

Typical conditions:

- stockpile well above readiness reserve
- weak need for the equipment class
- low current Market Credit
- reliable route

Behavior:

- lists bounded surplus
- avoids selling below reserve
- favors Compartmentalized Tolerance or State Patronage according to government type
- does not buy back the same category while a recent-import lock exists

### Broker

Typical conditions:

- central location
- several borders or ports
- good relations with several members
- strong routes
- moderate equipment demand

Behavior:

- opens and repairs routes
- carries third-party cargo
- values Network Reach
- protects Exposure to retain access

### State patron

Typical conditions:

- authoritarian or security-led route
- prolonged war or embargo
- large state stockpile
- high tolerance for diplomatic risk

Behavior:

- chooses State Patronage
- underwrites Market Credit
- sells larger surplus lots
- pays for route capacity
- reacts strongly to investigations

### Penetrator

Typical conditions:

- strong intelligence or internal-security capacity
- low ordinary demand
- high anti-corruption or hostile-network policy
- evidence of a route

Behavior:

- uses cover trades sparingly
- builds evidence
- attempts one coordinated seizure
- avoids random exposure-generating purchases
- abandons penetration if an existential shortage makes access more valuable than suppression

### Opportunistic auction bidder

Typical conditions:

- high credit
- route capacity
- strong need for the exceptional lot
- ability to deploy or use it

Behavior:

- bids within reserve
- abstains when the lot has no strategic use
- invests in handling only when the expected value is high

## Invitation AI

An AI candidate first checks hard blockers.

Hard zero conditions include:

- no valid route proposal
- actual nonhuman or excluded special-country state
- active permanent dismantlement policy
- current expulsion exclusion
- no government scope capable of accepting
- the network is fully dismantled
- the candidate cannot use, sell, broker, or investigate anything in the current cell

Acceptance score then considers need, access, politics, trust, and risk.

### Desired ordering

A country under embargo, at war, with a severe equipment shortage and a valid land route should score far above a peaceful country with open legal trade and no shortage.

A country with a direct border and moderate relations should normally score above a friendly country with no physical route.

A recent rejection or suppression campaign should dominate small positive factors.

## Government posture AI

### Compartmentalized Tolerance

Preferred when:

- the country needs access
- Exposure is moderate
- institutions fear scandal
- trade volume is limited
- the country lacks capacity for State Patronage

### State Patronage

Preferred when:

- war or embargo creates high demand
- the government can commit state resources
- a large surplus exists
- Exposure is low or the government accepts the risk
- intelligence and route capacity are sufficient

Avoid when:

- Exposure is already high
- a public scandal would threaten regime stability
- there is no large trade opportunity

### Counterintelligence Penetration

Preferred when:

- the country has intelligence capacity
- ordinary market need is low
- evidence or policy supports suppression
- at least one route or broker can be investigated

Avoid when:

- the country lacks a valid intelligence path
- the network is the only realistic source of essential equipment
- active war makes the cover operation too costly

### Suppression Campaign

Preferred when:

- Exposure is severe
- strategic need is low
- an investigation has mature proof
- the government has the resources to close the route
- the network threatens internal policy or diplomatic survival

Avoid when:

- an existential equipment or fuel deficit remains
- every route objective is impossible
- the government has an unsettled exceptional delivery it urgently needs

## Purchase AI

The AI should rank offers by strategic utility, not nominal rarity.

Utility inputs include:

- current deficit in the exact equipment class
- current production and time to solve the deficit legally
- current and expected war
- equipment age and compatibility
- fuel and storage
- airbases, ports, and templates
- route cost and risk
- Market Credit reserve
- current Exposure
- recent import lock
- legal market alternatives
- expected delivery time

### Hard zero purchase conditions

- invalid or unsupported equipment token
- no valid route
- insufficient credit
- insufficient required logistics
- buyer cannot use the package
- purchase would exceed handling capacity
- provider permission expired
- buyer is suspended
- buyer is the source seller when self-purchase is forbidden
- recent-import lock or transaction state makes the action exploitative

### Credit reserve

AI should retain a dynamic credit reserve for:

- emergency fuel
- route repair
- active delivery crisis
- expected commission
- current auction commitment

A normal purchase should not spend the final reserve unless the cargo solves an existential problem.

## Sale AI

The AI calculates protected reserve before listing.

Hard zero sale conditions include:

- stock at or below reserve
- recent-import lock covers the apparent surplus
- equipment is reserved for another transaction
- sale would create an immediate deployment deficit
- no valid buyer or route class exists
- seller is suspended

A seller with at least `150%` of its dynamic reserve should receive a strong positive score for a Small or Medium lot. A seller near `110%` should usually score zero. A Large lot should require a much higher surplus and favorable war conditions.

## Route AI

Route selection order should be contextual.

Typical preference:

1. open direct land route
2. reliable international corridor
3. stable maritime route
4. neutral relay
5. occupied corridor
6. covert air route

This order can change for islands, blockades, poor infrastructure, hostile fronts, or urgent intelligence cargo.

AI must not start a route mission whose state, port, intermediary, or logistics requirement is impossible.

## Exposure AI

Exposure should change AI behavior before it reaches `100`.

| Exposure band | AI response |
| --- | --- |
| Hidden | Normal strategic use |
| Rumored | Prefer low-risk routes and limit low-value trades |
| Under Investigation | Spend on cover, shift traffic, avoid large nonessential lots |
| Compromised | Repair, burn, withdraw, or suppress according to need and posture |
| Breach | Resolve the breach before ordinary trading resumes |

A desperate country can accept higher Exposure for essential cargo. That exception should be tied to measurable shortage and war state.

## Auction AI

AI bids only when:

- the package is valid
- it can use the package
- a route can carry it
- the strategic utility exceeds a threshold
- the bid leaves an acceptable reserve, unless the need is existential

AI should not bid more than about `70%` of available credit in ordinary circumstances. A higher bid requires an existential strategic condition and a viable delivery route.

The AI should not bid on a rare technology it already owns, aircraft it cannot base or fuel, ships it cannot receive, or equipment with no valid template use.

## Counter-smuggling AI

An outsider needs evidence before acting.

AI evaluates:

- confidence of evidence
- route through its territory
- hostile or sanctioned participant
- value of the suspected cargo
- cost of investigation
- current war and internal priorities
- diplomatic consequences

A country should prioritize a route that carries enemy strategic material through its own territory. It should ignore weak rumors with no route or target.

## Named probability scenarios

Every weighted surface must receive a baseline inspection, owner patch, and post-change comparison through `chaosx_ai_probability_auditor`.

The auditor starts with `hoi4.probability_inspect` and uses the same named scenarios before and after implementation changes.

### BM-P01: Invitation under desperation

| Input | Candidate A | Candidate B |
| --- | --- | --- |
| War | active defensive war | peace |
| Embargo | active major embargo | none |
| Equipment | severe infantry deficit | full reserve |
| Legal market | poor access | open access |
| Route | open land route | open land route |
| Expected result | strong acceptance | low acceptance |

Acceptance score for Candidate A should be at least three times Candidate B before normalization, unless a hard political blocker applies.

### BM-P02: Route proof over friendly relations

| Input | Candidate A | Candidate B |
| --- | --- | --- |
| Relations to sponsor | moderate | high |
| Route | direct border | no valid route |
| Need | moderate | high |
| Expected result | eligible | hard zero |

A friendly country with no route must not enter the normalized invitation pool.

### BM-P03: Safe surplus sale

| Input | Seller A | Seller B |
| --- | --- | --- |
| Stock relative to reserve | `180%` | `108%` |
| War | peace | active war |
| Recent imports | none | present |
| Expected result | Small and Medium valid | all sale sizes zero |

### BM-P04: Fuel purchase utility

| Input | Buyer A | Buyer B |
| --- | --- | --- |
| Navy and air demand | high | low |
| Fuel days | fewer than `10` | more than `90` |
| Route | maritime valid | land valid |
| Expected result | fuel offer ranks first | fuel offer low or zero |

### BM-P05: Route selection

| Input | Route A | Route B |
| --- | --- | --- |
| Type | land | maritime |
| Status | Open | Strained |
| Time | shorter | longer |
| Risk | Low | High |
| Cargo | medium small arms | medium small arms |
| Expected result | land dominates | maritime selected only after material state change |

A separate island variant should reverse the hard feasibility result when no land route exists.

### BM-P06: High-Exposure posture response

| Input | Member A | Member B |
| --- | --- | --- |
| Exposure | `82` | `18` |
| Posture | State Patronage | Compartmentalized Tolerance |
| Strategic shortage | low | moderate |
| Expected result | cover, route burn, withdrawal, or suppression preferred | normal trade preferred |

### BM-P07: Provider approval gate

| Input | Package A | Package B |
| --- | --- | --- |
| Owner registration | valid | missing |
| Minimum evolution | met | met |
| Source debit | proven | unproven |
| Expected result | eligible pool entry | exact zero and reject reason |

No modifier may rescue Package B.

### BM-P08: Grand Auction utility

| Input | Bidder A | Bidder B |
| --- | --- | --- |
| Package use | fills severe tank deficit | no armored template use |
| Credit | adequate | abundant |
| Route | heavy cargo valid | heavy cargo valid |
| Expected result | bids within reserve | abstains despite more credit |

### BM-P09: Embargo-circumvention demand

Compare the same member before and during Event 50.

Expected changes:

- invitation score rises
- fuel and equipment commission scores rise
- neutral and maritime route value rises
- Exposure tolerance rises only when shortage is real

The embargo flag alone should not make every package desirable.

### BM-P10: Counter-smuggling evidence

| Input | Observer A | Observer B |
| --- | --- | --- |
| Evidence | mature route receipt | rumor only |
| Route through territory | yes | no |
| Enemy cargo | proven | unknown |
| Expected result | investigation and seizure actions score high | no active action |

## Probability evidence methods

Use:

- `hoi4.probability_evaluate` for complete invitation, option, offer, and bid pools
- `hoi4.probability_sweep` for Exposure, shortage, reserve, and route-pressure thresholds
- `hoi4.probability_compare` after every weight patch
- `hoi4.probability_simulate` for offer rotations and invitations when exact pools are too large but fully declared
- `hoi4.probability_sequence` only after cadence, recovery, caps, offer expiry, invitations, cooldowns, route loss, and terminal states are fully declared
- `hoi4.probability_render` for matrix and sensitivity evidence when it improves review

The audit must label evidence as exact, bounded, sampled, score-only, or unresolved.

## Balance anchors

### Founding

- target founders: `3`
- minimum founders: `2`
- maximum founders: `4`
- one initial route per founder where possible
- one-time founding credit only

### Offer slots

- baseline: `3`
- Evolution I: `4`
- Evolution II: `5`
- Evolution III: `6`

### Route limits

- baseline ordinary member: `1`
- Evolution I established member: up to `2`
- Evolution II or III mature broker: up to `3`

These are caps, not guaranteed free routes.

### Active jobs

- one selected offer for the human-facing flow
- no more than two ordinary deliveries per member without additional capacity
- one Grand Auction commitment per member
- one to three visible missions in the category

### Reach and evolution

- Evolution I Reach: `35+`
- Evolution II Reach: `65+`
- Evolution III Reach: `85+`

Evolution also needs Chaos, membership, region, route, and MTTH proof.

### Exposure

Exposure must rise enough that repeated large transactions force a response. It should fall slowly enough that the player cannot erase every risk between rotations.

A member using Compartmentalized Tolerance for small occasional trades can remain hidden with active management. A State Patron moving large exceptional packages should approach investigation or breach unless it invests heavily in routes and cover.

### Lot handling

Amounts should be limited by the smaller of:

- verified source amount
- buyer need
- route capacity
- buyer handling capacity
- current evolution's lot band

An exceptional source can create a large effect, but handling capacity should stop a tiny route from moving a major power's entire arsenal at once.

## Credit pricing and sinks

Important sinks are:

- purchase price
- network fee
- route opening and repair
- commissions
- Exposure cleanup
- auction bids
- withdrawal settlement

Credit income must remain lower than the buyer price for the same lot.

The recent-import lock, network fee, seller reserve, and one-time receipt prevent simple buy and resale farming.

## Exploit controls

### Founding credit farming

- one permanent country receipt
- no second grant after reconnection, civil war, annexation, release, or tag transfer
- a genuine successor needs a new invitation and receives only the normal successor package defined by the implementation

### Buy and resale loop

- recent-import ledger subtracts purchased cargo from saleable surplus
- seller yield is below buyer price
- self-purchase is forbidden
- same transaction cannot create a new provider lot

### Stockpile duplication

- source debit occurs once before dispatch
- transaction state is persisted
- delivery effect checks settlement receipt
- partial delivery uses the already-debited source
- seizure cannot give full cargo to both observer and buyer

### Offer reroll abuse

- rotation interval is persistent
- commission has a cooldown
- opening and closing the category cannot reroll offers
- reloading cannot reroll a committed rotation

### Route mission farming

- route IDs are stable
- reopening the same unchanged route does not award new Reach or credit
- broker rewards require a settled third-party delivery
- burned routes require new proof

### Exposure cleanup farming

- cleanup actions have cooldowns
- each investigation episode has one-use responses
- burning a route creates a real capacity and Reach loss
- changing posture cannot reset Exposure

### Auction abuse

- one bid per member
- one bounded bid-improvement action
- full route and use validation
- losing refund lower than committed bid when a real handling cost was spent
- no repeated auction for the same provider receipt

### Civil-war duplication

- membership, credit, recent imports, offers, and routes transfer to at most one side through explicit proof
- unresolved state produces candidates, not copied active members

### Annexation inheritance

- annexer receives no automatic membership, credit, or provider rights
- dispatched cargo resolves against persisted buyer scope or cancels through explicit successor rules

## Important edge cases

### No valid founding cell

Event 57 is unavailable. It remains unfired and keeps its normal future eligibility.

### Only two eligible countries

Create a two-country founding cell with lower starting Reach and prioritize a third invitation after the first successful delivery.

### Player is not invited

The system proceeds under AI control. The player can later be invited or discover a route.

### All founders reject

The founding transaction retries only through one bounded alternate cell attempt. If that also fails, the event returns to unfired availability through the normal event-system rejection contract and leaves no half-created network.

The implementation must confirm whether the random-event framework supports transactional rollback before choosing the exact firing order.

### Seller disappears before debit

Cancel the offer and clear the reservation. No buyer delivery starts.

### Seller disappears after dispatch

The cargo remains a debited anonymous shipment. It can arrive, be delayed, or be seized according to the route.

### Buyer disappears before dispatch

Cancel and refund according to the reservation contract.

### Buyer disappears after dispatch

Use the explicit successor or seizure rule. Never grant the cargo twice.

### Route disappears during delivery

The job enters a delivery crisis once. It can reroute, partially deliver, or fail.

### Equipment definition becomes invalid

Invalidate the offer before purchase. A dispatched transaction requires an owner migration or safe cancellation contract.

### DLC changes between saves

DLC-dependent packages must fail closed and settle safely. The core member, credit, route, and exposure ledgers remain valid.

### Network reaches zero active members

Enter dormancy. Stop normal rotations. Keep sparse reconstruction records and history.

### Network is fully dismantled

Clear reconstruction eligibility, settle jobs, retain logs and achievements, and prevent a second initial firing.

### World-end state begins

The ordinary global event system stops according to shared rules. Event 57 should stop new invitations and rotations, then settle or freeze active transactions according to the owning terminal system's compatibility contract.

It must not run an independent world-end process.

## Performance constraints

- no whole-world daily, weekly, or monthly scan
- registered member and route arrays only
- bounded candidate samples
- dirty-route refresh after relevant world changes
- one committed invitation per growth pulse
- one rotation job for the global market
- one receipt per offer and transaction
- cleanup of invalid records before new generation

## Balance review scenarios

Implementation balance review should run at least these campaign states:

1. small neutral member in peace with modest surplus
2. embargoed minor in defensive war
3. major power with huge stockpile and several legal alternatives
4. island member under blockade
5. landlocked member with one neutral corridor
6. State Patron at high Exposure
7. penetrator with mature evidence
8. Evolution I network with two regional cells
9. Evolution II network with one experimental provider
10. Evolution III Grand Auction with several valid AI bidders
11. all routes destroyed and reconstruction pending
12. full dismantling attempt

The report should record actual offers, prices, route times, AI choices, Exposure movement, Reach movement, and exploit findings. A statement that the system feels balanced is insufficient.


---

## Source file: `08_event_chain_logs_localisation_and_catalog_alignment.md`

# Event Chain, Logs, Localisation, and Catalog Alignment

## Event namespace

The event chain uses the `chaosx.nr57.*` namespace.

The exact final subevent numbering belongs to implementation, but the following role bands should be preserved so later maintenance remains readable.

| Working range | Role |
| --- | --- |
| `chaosx.nr57.1-9` | entry, founder selection, invitations, and initial member reports |
| `chaosx.nr57.10-19` | offer rotations, purchases, dispatch, and delivery outcomes |
| `chaosx.nr57.20-29` | invitations, reconnections, suspensions, withdrawals, and expulsions |
| `chaosx.nr57.30-39` | evolutions and major network milestones |
| `chaosx.nr57.40-49` | Grand Auctions and exceptional packages |
| `chaosx.nr57.50-59` | outsider discovery, investigations, seizures, and regional dismantling |
| `chaosx.nr57.60-69` | dormancy, reconstruction, and full dismantling |
| `chaosx.nr57.70+` | owner-adapter reports and rare validated outcomes |

These are implementation role labels, not player-facing event names.

## Entry transaction

`chaosx.nr57.1` should be a hidden or minimally visible bootstrap event that owns the founding transaction.

It should:

1. validate that the event can still fire
2. clear temporary selection state
3. build a candidate broker shortlist
4. select a connected founding cell
5. create pending invitations and route proposals
6. resolve AI responses
7. send the player a private invitation only when the player is selected
8. commit the network only after minimum membership and route proof exist
9. register the event in the fire-once system
10. record the sanitized event history row

The implementation must use a transactional order that does not consume the fire-once event if every proposed founder rejects and no valid replacement cell exists.

If the current event framework cannot roll back after `handle_fired_event`, founder acceptance must be resolved before the shared fire-once commit. This ordering requires source inspection and an MCP event-chain pass.

## Founder invitation reports

A player-selected founder receives a private report that explains:

- a controlled contact has arrived
- the offer concerns restricted goods and routes
- the government will know only its direct contact
- accepting creates access, credit, and Exposure
- rejecting closes the invitation for a long period
- an intelligence-capable government may enter under penetration

The report should not reveal the other founders, a global headquarters, or an omniscient organization.

AI founder responses use the same valid options and consequences.

## First member report

After the network commits, every accepted member receives a local setup event or hidden effect that:

- initializes one-time Market Credit
- assigns the accepted posture
- activates the first route
- adds the member to the sparse registry
- opens the category
- schedules the first offer rotation
- records the founding receipt

Only the current player needs a visible report. AI countries can receive hidden equivalent effects unless their response creates a world-visible consequence.

## Offer and delivery events

Offer rotation should be a hidden global event-owned process over registered providers and active members.

Player-facing reports are reserved for:

- a commissioned supplier being found or failing
- a delayed delivery that requires a choice
- a partial delivery
- a seizure
- a betrayal or sting
- an exceptional package
- a Grand Auction

Clean ordinary delivery should normally resolve through the mission and a concise notification. A full popup is unnecessary for every routine shipment.

## Membership events

Visible events are appropriate for:

- receiving an invitation
- suspension after a breach
- expulsion
- a government posture crisis
- reconnection after long dormancy
- a successful suppression campaign

Routine AI membership growth can resolve through hidden events and effects.

## Evolution events

Each evolution uses a global milestone event with no country actor.

The event should:

- verify Chaos and world-state readiness
- verify the evolution is enabled
- set the shared evolution context
- record the evolution entry
- activate the capability set
- update category presentation
- schedule the next relevant pulse

It should not award Chaos merely for activation.

## Outsider events

An outsider receives a local report only after evidence is created.

Useful incident subjects include:

- a customs seizure
- a train manifest that does not match its cargo
- weapons with altered markings
- a broker arrested at a border
- a neutral port authority exposed
- a courier carrying several currencies and route notes

The report names only the proven route, cargo, intermediary, or participant.

## Event history

Event 57 appears once in the main History tab.

The row should show:

- event ID and final event name
- Minor Fire-Once type
- firing date
- no actor flag
- no founder or member identity

The detail view explains the premise of a hidden invitation-only network. It should not list exact effects, hidden values, active members, routes, or future provider classes.

The event row remains available after the network is dormant or dismantled because the event fired historically.

## Evolution log

The Evolutions tab records exactly three Event 57 milestones.

Suggested data model:

- event ID: `57`
- type: one stable network-evolution type
- stage: `1`, `2`, and `3`
- tier: corresponding Chaos tier display
- actor: none

The main Evolutions tab and History-related evolution list use actual logged date and sequence metadata.

The Event Details evolution catalog shows premise and stage description only. It must not show fake history dates or sequence numbers.

## Event Details

Event Details should include:

- accepted name
- event type
- Chaos level `1`
- Positive Economy cluster and High member role
- premise description
- three evolution previews
- current enabled state
- fire-once status

The premise should explain that a small secret network moves restricted goods through covert routes and expands after its first appearance.

It must not show:

- active members
- route endpoints
- seller identities
- Market Credit balances
- current inventory
- exact evolution readiness values
- hidden investigation state

## Event enable state

The current catalog status is To Be Reworked. Event 57 should remain disabled by default in the reworked-event allowlist until the complete implementation, assets, AI, docs, workbook, and audits are ready.

When implementation is complete, the same change should:

- register Event 57 as fire-once
- register Chaos level `1`
- restore it to the default enabled allowlist
- add its Positive Economy membership
- add event-name and detail selectors
- add evolution selectors

## Localisation surfaces

Implementation needs finished player-facing text for:

- event name
- founder invitation
- acceptance, patronage, penetration, delay, and rejection options
- first member report
- decision category and status header
- Market Credit, Exposure, and Network Reach labels and tooltips
- reach stages
- government postures
- offer classes
- provenance classes
- route types and states
- risk classes
- purchase, sale, route, posture, cover, and suppression decisions
- delivery missions
- transaction outcome reports
- outsider evidence and counter-smuggling actions
- evolution titles and descriptions
- Event Details
- event history and evolution selectors
- achievements
- catalog-facing summaries

## Writing direction

### General voice

Use clear period logistics and political language.

The text should focus on:

- shortages
- neutral freight
- false paperwork
- state depots
- corrupt officials
- captured stock
- shipping routes
- intelligence contacts
- customs searches
- government risk

Avoid:

- digital-market language
- modern internet slang
- theatrical crime-boss language
- a single named mastermind
- generic office-report prose
- raw variable names
- direct explanations of script caps or tuning
- claims that every member knows the full network

### Founder invitation

The viewpoint is the receiving government. The contact provides enough evidence to prove access without revealing the network.

The serious acceptance route should sound pragmatic. State Patronage should sound opportunistic and controlled. Penetration should sound cold and security-minded. Rejection can be legalist, ideological, or cautious according to the government.

Final option wording must be researched only when it uses a cultural or historical allusion. Plain period wording needs no external quotation.

### Member category

Use short natural lines. Do not simulate a table with divider characters.

Each visible value needs:

- name
- current value or stage
- consequence
- next threshold
- one clear action that can change it

### Offers

An offer should state the cargo, amount, price, route, risk, and expected delivery time without revealing hidden source identity.

Use provenance descriptions such as diverted reserve, captured stock, neutral commercial lot, or unknown broker only when the source receipt supports them.

### Evolutions

Evolution text should show increasing reach through cargo and routes. It should not announce a generic level-up or list every mechanic.

### Outsider discovery

Use observed evidence. The text should not announce that the entire world has discovered the organization.

### Dismantling

Regional success should describe closed routes, seized accounts, and lost contacts. Full dismantling should describe the network's inability to settle or reconnect without claiming that illicit trade has disappeared from human society.

## Dynamic localisation

Dynamic text should support:

- selected offer class and amount
- Market Credit price
- route family
- delivery-time band
- risk class
- current Exposure band
- current Reach stage
- current posture
- named state, port, intermediary, buyer, seller when legitimately known
- blocked reason
- investigation target
- transaction result

The default branch must be neutral and safe. It cannot leak another country's text or an internal key.

## Key naming

Use stable lowercase snake_case with the Event 57 namespace where needed.

Working families include:

- `black_market_*`
- `chaosx_nr57_*`
- `events_log_event_57_*`
- `black_market_route_*`
- `black_market_offer_*`
- `black_market_achievement_*`

Final implementation should follow existing repository conventions after inspecting neighboring event files.

## Catalog conflict

The supplied current Events CSV maps ID `57` to an older event named The Radar and classifies it as Minor Repeatable.

The accepted Event 57 design in this package replaces that stale row with:

- The Black Market
- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member
- To Be Reworked until implementation is complete

A supplied cluster-update source also identifies Event 57 as The Black Market in Positive Economy with High severity. That source confirms the accepted membership and should be reconciled with the authoritative workbook.

## Workbook alignment

The only editable catalog source is the authoritative workbook at:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

After implementation facts are final, `chaosx_spreadsheet_doc_worker` should update:

- Event 57 name
- details
- type
- Chaos level
- cluster
- member severity
- three evolution summaries
- status
- Positive Economy member list and details when needed

Then run:

`python .tools/export_event_catalog_csv.py`

The three CSV exports must not be edited directly.

Spreadsheet text must match the in-game Event Details and evolution wording. It should describe the premise and progression, not raw effects or implementation history.

## Documentation surfaces

Recommended permanent documentation:

- `docs/events/057_the_black_market/overview.md`
- `docs/events/057_the_black_market/membership_and_secrecy.md`
- `docs/events/057_the_black_market/routes_and_deliveries.md`
- `docs/events/057_the_black_market/inventory_and_credit.md`
- `docs/events/057_the_black_market/provider_api.md`
- `docs/events/057_the_black_market/ai_and_balance.md`
- `docs/events/057_the_black_market/validation.md`

Accepted design remains under:

- `docs/specs/057_the_black_market_specs/`

Working plans and handoffs belong under:

- `docs/plans/057_the_black_market_plans/`

## Event chain MCP pass

Before editing and after final source changes, implementation must use the event MCP route to inspect and compare:

- `chaosx.nr57.1` entry flow
- founder transaction order
- invitation options
- transaction state flow
- evolution events
- outsider evidence events
- dormancy and dismantling

Use narrow `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` calls.

Weighted options, invitations, offer pools, and AI actions require the separate probability workflow.


---

## Source file: `09_assets_and_achievements.md`

# Assets and Achievements

## Visual direction

Event 57 should look like a period clandestine logistics system.

The visual identity should use:

- railway sidings
- guarded warehouses
- merchant holds
- false crate markings
- fuel drums
- mixed military equipment
- shipping papers without readable generated text
- customs lamps and inspections
- neutral ports
- folded route notes
- anonymous brokers shown from a distance or without identifiable portrait framing

The palette can use aged paper, dark wood, steel, canvas, oil, muted military paint, and low industrial light.

Avoid modern containers, computers, neon crime imagery, online-market symbolism, skull emblems, gangster caricatures, national stereotypes, readable generated labels, and generic money piles as the main subject.

## Asset source mode

The event is fictional and international. Its report art and category pictures should use generated period-authentic documentary scenes.

Gameplay icons and achievement icons should use generated transparent icon art through the correct icon workflow.

The asset package does not need a grounded person or institutional portrait.

## Reference inspection

Before production, asset workers must inspect the exact matching reference families under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Required families:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/achievements/`

The decision-category-picture folder must contain its own labeled `contact_sheet.png`. When missing, the asset worker must create it and update the reference README and catalog before generating Event 57 pictures.

## Report event pictures

### First Contact

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_first_contact` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_first_contact` |

Composition direction:

- a dim wartime depot or railway warehouse
- several crates from different military origins
- one guarded exchange between officials and anonymous intermediaries
- no clear national insignia that identifies founders
- documentary framing from outside the conversation
- 1936 to 1945 clothing, transport, lighting, and materials
- no readable generated text

### Seized Shipment

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_seized_shipment` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_seized_shipment` |

Composition direction:

- customs or military personnel opening a concealed cargo compartment
- mismatched weapons, fuel drums, or technical cases
- route evidence visible through objects, not readable documents
- tense but non-cinematic lighting
- no gore
- no modern equipment

### Grand Auction

| Field | Requirement |
| --- | --- |
| Working basename | `black_market_grand_auction` |
| Type | report event picture |
| Size | `210x176` |
| Source mode | generated period documentary scene |
| Runtime folder | `gfx/event_pictures/057_the_black_market/` |
| Proposed sprite | `GFX_report_event_057_black_market_grand_auction` |

Composition direction:

- a large hidden depot with one exceptional military or technical lot
- masked national identity through plain coats, crates, shadows, and intermediaries
- period telephones, paper ledgers, and transport equipment
- no modern auction room
- no readable generated bids or signs

## Decision category icon

| Field | Requirement |
| --- | --- |
| Basename | `black_market_category` |
| Type | decision category icon |
| Target | inspect active consumer, expected compact category icon |
| Source mode | generated transparent icon |
| Proposed sprite | `GFX_decision_category_057_black_market` |

Icon direction:

- one sealed crate crossed by a folded route line or key
- clear silhouette
- transparent unused canvas
- dark outline and subtle shadow
- readable at the final size
- no text, coins, skull, or modern padlock

## Evolution category pictures

The same category changes its static picture after each evolution. Each picture is separate source art designed for the category-picture consumer.

The current reference family uses `114x101`, but final size must be confirmed from the active sprite and GUI consumer.

### Baseline picture

Working basename: `black_market_category_local_circuit`

Direction:

- one compact rail or warehouse exchange
- small mixed cargo
- local shadows and limited scale
- one clear visual route

### Evolution I picture

Working basename: `black_market_category_international_network`

Direction:

- linked rail, port, and distant freight cues in one coherent period scene
- larger cargo and wider origin variety
- no painted world map as the main subject

### Evolution II picture

Working basename: `black_market_category_underground_economy`

Direction:

- embargoed cargo moving through layered neutral paperwork and hidden depots
- technical cases and industrial material
- state officials present indirectly

### Evolution III picture

Working basename: `black_market_category_anything_has_a_price`

Direction:

- exceptional guarded stock, technical dossiers, unusual equipment cases, and large clearing activity
- broad scale without fantasy spectacle
- the market feels powerful but remains period-authentic

Proposed sprites:

- `GFX_057_black_market_category_local_circuit`
- `GFX_057_black_market_category_international_network`
- `GFX_057_black_market_category_underground_economy`
- `GFX_057_black_market_category_anything_has_a_price`

## Decision icon family

All decision icons are independent `32x32` assets. They can share motifs and palette, but none should be a resized copy of another asset type.

| Basename | Use | Visual direction |
| --- | --- | --- |
| `black_market_buy_lot` | purchase current offer | open crate with one clear military silhouette |
| `black_market_sell_surplus` | list member surplus | outbound crate and inventory tag without text |
| `black_market_commission` | request offer class | sealed request case and broker key |
| `black_market_open_route` | create or repair route | rail, road, or port route symbol |
| `black_market_safer_route` | reroute delivery | split route with guarded branch |
| `black_market_intelligence` | buy or sell intelligence | closed dossier and lens motif |
| `black_market_compartmentalize` | reduce Exposure | separated ledger pages or locked compartments |
| `black_market_burn_route` | destroy compromised route | broken rail or burned manifest motif without flames dominating |
| `black_market_penetration` | counterintelligence posture | marked cargo and surveillance symbol |
| `black_market_suppression` | close local cell | customs seal over route symbol |
| `black_market_grand_auction` | exceptional auction | large sealed case with bid marker, no text |
| `black_market_underwrite` | convert industrial burden into credit | factory silhouette and sealed account book |

Every icon should have native transparency, stable centering, readable silhouette, and no opaque square background.

## Texticons

Market Credit requires a dedicated texticon with a stable token before any decision uses it as a visible cost.

Working asset:

- basename: `black_market_credit_texticon`
- motif: small stamped account chit, ledger mark, or trade token
- transparent unused canvas
- no readable generated text

The exact dimensions and sprite registration must follow an inspected existing custom texticon precedent.

## Achievement set

The seven achievements below use working titles. Final player-facing wording should be written during implementation and localisation audit.

Each achievement needs:

- exact achievement ID
- tracking flags or variables
- current-player eligibility
- disqualifiers
- completed icon
- grey icon
- not-eligible icon
- documentation
- catalog or achievement list alignment when the project exposes one

### 1. No Questions Asked

- Proposed ID: `57_the_black_market_no_questions_asked`
- Visibility: visible
- Eligible country: any ordinary player country that becomes a member
- Goal: complete purchases from every baseline cargo family during one campaign while Exposure never reaches `50`
- Baseline families: small arms, support or artillery, transport, fuel or convoys, and intelligence
- Disqualifiers: Force Trigger debug state, full network dismantling before completion, any player Exposure record of `50+`
- Why it is difficult: the player must use several offer classes without relying on high-risk bulk trade
- Tracking: one receipt flag per cargo family plus highest Exposure reached
- Icon direction: several different sealed crates arranged behind one intact customs seal

### 2. Enemy of My Enemy's Quartermaster

- Proposed ID: `57_the_black_market_enemy_quartermaster`
- Visibility: visible
- Eligible country: active member
- Goal: receive a settled equipment delivery whose proven source country is currently at war with the buyer at both dispatch and settlement
- Additional requirement: source identity never becomes public through that transaction
- Disqualifiers: self-created civil-war copy, source and buyer become allies before settlement, duplicated provider receipt
- Why it is difficult: the route must survive active hostility and the source must be real
- Tracking: buyer, source, hostility proof at dispatch and settlement, secrecy outcome
- Icon direction: two opposing helmets divided by one anonymous supply crate

### 3. The Embargo Has Holes

- Proposed ID: `57_the_black_market_embargo_has_holes`
- Visibility: visible
- Eligible country: current target of Event 50 or a shared major strategic embargo
- Goal: while the embargo remains active, complete one fuel delivery, one military-equipment delivery, and one industrial-procurement delivery
- Disqualifiers: embargo removed before any required delivery settles, packages with no route proof
- Why it is difficult: three cargo classes need surviving routes under active restriction
- Tracking: active embargo proof and three settled package receipts
- Icon direction: blocked trade gate with three concealed cargo paths passing beneath it

### 4. Liquid Assets

- Proposed ID: `57_the_black_market_liquid_assets`
- Visibility: visible
- Eligible country: active member that never adopts State Patronage
- Goal: win and receive a Grand Auction lot after earning at least the winning bid's Market Credit value through verified sales
- Disqualifiers: State Patronage, debug credit, duplicated sale receipts, winning cargo not delivered
- Why it is difficult: the player must build a real seller economy and preserve enough route capacity for the auction
- Tracking: sale-earned credit total, non-sale credit sources, posture history, bid, auction settlement
- Icon direction: stacked sealed crates transforming into one large locked case, without literal liquid imagery

### 5. Invisible Empire

- Proposed ID: `57_the_black_market_invisible_empire`
- Visibility: hidden until Event 57 fires
- Eligible country: founding member
- Goal: remain a member until Evolution III activates while the country's Exposure stays below `25`, with no route ever reaching Compromised
- Disqualifiers: withdrawal, expulsion, Exposure `25+`, compromised route, player joining after founding
- Why it is difficult: growth must come through careful small trade, brokerage, and route management
- Tracking: founder receipt, maximum Exposure, route-compromise history, Evolution III activation
- Icon direction: broad network of crates and routes hidden behind one plain closed warehouse door

### 6. Customs Seizure

- Proposed ID: `57_the_black_market_customs_seizure`
- Visibility: visible
- Eligible country: a player country that has never been a member
- Goal: dismantle every active Black Market route that passes through owned or controlled territory and cause the connected regional cell to become dormant
- Disqualifiers: any membership acceptance, route created by player infiltration without eventual dismantling, incomplete cell dormancy proof
- Why it is difficult: the player needs evidence, local control, several successful actions, and a live target cell
- Tracking: never-member flag, route IDs touching player territory, dismantled receipts, cell dormancy receipt
- Icon direction: customs officer seal over an opened false cargo compartment, without a character portrait

### 7. Prototype Without a Project

- Proposed ID: `57_the_black_market_prototype_without_a_project`
- Visibility: hidden until Evolution II or the first approved experimental offer
- Eligible country: active member
- Goal: receive and field or validly use one owner-approved experimental package while the owning source project remains incomplete
- Disqualifiers: generic unapproved token, source project completed before delivery, package not fielded or used, debug grant
- Why it is difficult: it depends on a rare owner package, route handling, and project-state isolation
- Tracking: provider ID, package ID, source project state at dispatch and settlement, recipient use proof
- Icon direction: unusual covered machine or weapon crate with an unfinished technical drawing motif, no readable text

## Achievement asset paths

Achievement files follow the root-only achievement convention in `gfx/achievements/`.

For each exact ID, create:

- `<achievement_id>.dds`
- `<achievement_id>_grey.dds`
- `<achievement_id>_not_eligible.dds`

Completed source art is generated first. Grey and not-eligible variants follow the established achievement workflow and overlay reference.

## Asset manifest

The temporary event workspace should contain:

- source art
- processed PNGs
- final review contact sheets
- prompt records
- source-mode records
- DDS outputs before runtime placement
- dimensions
- alpha validation
- sprite handoff
- achievement triplet coverage

Recommended temporary path:

`docs/assets/057_the_black_market/`

Before full event completion, durable provenance, prompt, review, and runtime crosswalk facts must move into permanent event or plan documentation. Final assets move to runtime folders. No runtime path may reference `docs/assets/`. The completed temporary event workspace should then be deleted according to the asset workflow.

## Asset acceptance

The asset package is not complete until:

- every required source exists
- all event pictures are `210x176`
- category pictures match the inspected consumer
- all decision icons are independent `32x32` designs
- the Market Credit texticon is wired and readable
- every achievement has three final states
- transparent assets retain real alpha
- no white matte, checkerboard, halo, or opaque square remains
- all sprites and runtime paths are registered
- category pictures switch with evolution state
- the first-contact, seizure, and auction events use the correct art
- contact sheets show final assets at native size
- manifests and permanent evidence are aligned


---

## Source file: `10_implementation_acceptance_and_validation.md`

# Implementation Acceptance and Validation

## Implementation goal

Implement Event 57 as a complete fire-once bootstrap plus persistent event-owned Black Market system.

The completed feature must preserve:

- invitation-only membership
- compartmentalized country knowledge
- a connected founding cell
- sparse member, route, offer, delivery, evidence, and provider registries
- real source debits
- Market Credit
- Exposure
- Network Reach
- route-backed delayed deliveries
- rotating inventory
- government postures
- outsider evidence and counterplay
- three paced evolutions
- Event 57 Chaos milestones and reversals
- Positive Economy High membership
- AI behavior
- DLC compatibility
- event logs and Event Details
- assets
- achievements
- permanent docs and workbook alignment

## Required source review before code

Implementation must follow the current repository versions of:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- the offline Paradox wiki pages required by the touched systems
- current vanilla documentation and precedents
- current Chaos Redux event, decision, scripted-effect, event-log, cluster, achievement, and catalog patterns

Any current repository rule that is stricter than this planning package remains binding.

## Likely implementation files

Final paths must follow the current repository convention after inspection.

### Event-owned gameplay

- `events/057_the_black_market.txt`
- `common/decisions/057_the_black_market_decisions.txt`
- `common/decisions/categories/057_the_black_market_categories.txt`
- `common/scripted_effects/057_the_black_market_effects.txt`
- `common/scripted_effects/057_the_black_market_provider_effects.txt`
- `common/scripted_triggers/057_the_black_market_triggers.txt`
- `common/scripted_triggers/057_the_black_market_provider_triggers.txt`
- `common/script_constants/057_the_black_market_constants.txt`
- `common/on_actions/057_the_black_market_on_actions.txt` for narrow event-owned change hooks only
- `common/ideas/057_the_black_market_ideas.txt` for modifier-free carriers or visible posture ideas only when the final UI needs them
- `common/ai_strategy/057_the_black_market_ai_strategy.txt` when persistent strategy support is useful
- `common/scripted_localisation/057_the_black_market_scripted_localisation.txt`

### Shared event integration

- event-category registration
- Chaos-level registration
- reworked-event default allowlist
- event-name selectors
- event history and Event Details
- evolution log selectors
- Positive Economy cluster definitions and member arrays
- event manual-fire validation
- Chaos history source selectors

### Localisation

- Event 57 event and decision localisation
- shared event-name localisation
- Event Details and evolution localisation
- scripted localisation
- achievement localisation
- texticon localisation when required

### Assets

- `gfx/event_pictures/057_the_black_market/`
- event-owned decision and category asset folders
- root achievement assets
- event-owned `.gfx` registration
- Market Credit texticon registration

### Documentation

- `docs/events/057_the_black_market/`
- `docs/specs/057_the_black_market_specs/`
- `docs/plans/057_the_black_market_plans/`
- authoritative event catalog workbook
- regenerated CSV exports

## Script architecture

### Owner-owned helpers

Event 57 should own:

- founder selection
- membership state changes
- route creation and refresh
- offer generation
- Market Credit transactions
- Exposure changes
- Network Reach changes
- transaction receipts
- recent-import locks
- invitation cadence
- evolution readiness
- provider request and receipt handling
- outsider evidence
- dormancy and dismantling

### Shared helpers

Reuse the shared dynamic effects when their contracts fit.

Examples include supported stockpile debit helpers for infantry equipment, support equipment, motorized equipment, convoys, trains, plague bombs, and fuel.

When a needed neutral debit or transaction helper has callers across several systems, add it to the shared dynamic registry and document its purpose, scope, inputs, outputs, defaults, side effects, and usage.

One-event orchestration remains in Event 57 files.

### Tuning

Centralize:

- founder counts
- offer-slot caps
- rotation intervals
- invitation intervals
- Exposure bands and changes
- Reach thresholds and changes
- route limits
- transaction time bands
- credit floors and caps
- seller reserve factors
- price factors
- recent-import lock duration
- auction cadence
- evolution MTTH factors
- AI weights
- Chaos milestone values

Use script constants where the engine field accepts them. Use documented local constants or variables where it does not.

## No whole-world recurring scan

The system must use:

- member arrays
- route arrays
- active offer arrays
- active delivery arrays
- evidence-case arrays
- provider registry
- dirty records
- bounded candidate sampling

Do not add a whole-world `on_daily`, `on_weekly`, `on_monthly`, or equivalent scan.

A bounded event-owned pulse can iterate only the registered records.

## Transaction state machine

Every offer and delivery must pass through an explicit state machine.

Minimum states:

- generated
- available
- reserved
- source debit pending
- dispatched
- delayed
- partially settled
- settled
- seized
- canceled
- invalidated

Each state transition must be idempotent.

A save and reload at any state must not:

- duplicate equipment
- duplicate Market Credit
- reroll the outcome
- lose the debit
- restore an expired offer
- create a second mission
- clear the buyer or seller incorrectly

## Membership state machine

Minimum states:

- candidate
- invited
- active
- dormant
- suspended
- former
- expelled
- dismantler

Every transition must clean obsolete category content and keep one stable country receipt.

## Provider API acceptance

The provider API must:

- be event-owned and documented
- be versioned
- fail closed
- require explicit owner registration
- validate source and buyer
- debit the source once
- deliver once
- preserve owner event completion state
- return reject reasons
- expire safely
- survive save and reload
- prevent duplicate sale of one package
- support no-DLC paths

Event 54, Event 55, Event 56, Event 50, captured-stock systems, and future equipment owners should use adapters and avoid direct ledger access.

## Event and probability MCP evidence

### Event chain

Use:

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`

Inspect entry ordering, invitation branches, transaction scope, evolution flow, outsider evidence, dormancy, and dismantling.

### Weighted logic

`chaosx_ai_probability_auditor` must inspect every weighted surface before patching and compare it after patching.

Use the named BM-P01 through BM-P10 scenarios from the AI specification.

Required surfaces include:

- founder and broker selection
- candidate invitations
- candidate responses
- posture choice
- offer generation
- source and package selection
- purchase choice
- sale size
- route selection
- delivery outcome
- investigation action
- auction bidding
- evolution MTTH

## Decision audit

After implementation, `chaosx_decision_mission_auditor` should inspect and patch only bounded issues.

The audit must cover:

- category lifecycle
- three-value clarity
- visible action cap
- active mission cap
- cost icons
- route requirements
- auto-completion
- success, partial success, and failure
- stale targets
- cleanup
- AI validity
- exploit risk
- impact of rewards and penalties

A broad design gap returns to the parent or improvement planner.

## Localisation audit

`chaosx_localisation_auditor` should review:

- missing and duplicate keys
- encoding
- raw keys
- dynamic offer text
- route and risk text
- blocked reasons
- category clarity
- history and Event Details alignment
- evolution text
- achievement text
- workbook-facing wording
- absence of implementation-history language
- absence of modern digital-market language

## Asset acceptance pass

The asset workers should create the exact package in the asset specification.

The parent must verify:

- source evidence
- reference inspection
- dimensions
- transparency
- independent icon types
- category-picture switching
- event-picture consumers
- Market Credit texticon
- achievement triplets
- runtime paths
- sprite names
- final in-game consumers
- deletion of the temporary event asset workspace after durable evidence is promoted

## DLC matrix

### No DLC

Core requirements:

- founding network
- membership
- Market Credit
- Exposure
- Network Reach
- routes
- rotating offers
- stockpile sales and purchases
- fuel and convoy trade
- base intelligence packages
- counter-smuggling
- three evolutions
- AI
- achievements

### La Résistance

Enhancements:

- agency-backed invitations
- intelligence packages
- penetration
- evidence maturity
- route operations

No core action depends on the DLC.

### Arms Against Tyranny

Enhancements:

- verified legal-market valuation or equipment compatibility where useful
- stronger contrast between legal and illicit access
- supported equipment-market integrations

Black Market membership and offers remain separate from the legal market.

### No Step Back

Enhancements:

- trains and railway objectives
- tank designer compatibility
- route logistics depth

Base-game alternatives preserve transport and armored-package play.

### By Blood Alone

Enhancements:

- aircraft designer compatibility
- shared embargo consequences where present

Base-game aircraft tokens and Event 50's no-DLC embargo path remain valid.

### Man the Guns

Enhancements:

- naval design and ship-package depth where Event 56 supports it

No unsupported ship transfer is invented.

### Special-project DLC surfaces

Special-project equipment appears only through owner adapters. Core Event 57 progression does not require one.

## Acceptance scenarios

### BM-A01: Founding three-country cell

Setup:

- three eligible ordinary countries
- one broker
- two valid routes
- player selected as one founder

Pass conditions:

- one Event 57 firing
- private invitation
- no founder list in global history
- three accepted members or valid bounded replacement
- one-time founding credit
- active category
- first rotation scheduled

### BM-A02: Player excluded from founding

Pass conditions:

- AI network commits
- player receives no member category
- global history remains sanitized
- player can later receive valid invitation or evidence

### BM-A03: No valid cell

Pass conditions:

- event is N/A or rejects before fire-once commit
- no partial registry
- no consumed event weight
- no stale invitations

### BM-A04: Real surplus sale

Pass conditions:

- displayed protected reserve is correct
- source debit occurs once
- seller receives bounded credit
- offer appears once
- recent-import lock prevents resale farming

### BM-A05: Clean land delivery

Pass conditions:

- Market Credit spent once
- delivery mission appears
- source already debited
- cargo arrives once
- receipt settles
- Exposure and Reach change once

### BM-A06: Maritime seizure

Pass conditions:

- no buyer cargo grant
- observer receives bounded evidence
- route becomes Compromised or Burned
- source remains debited
- no duplicate cargo
- member Exposure rises

### BM-A07: Event 50 embargo connection

Pass conditions:

- demand and invitation scores change
- legal restriction remains active
- successful meaningful delivery records the one-time embargo-circumvention Chaos milestone
- no duplicate embargo Chaos

### BM-A08: Event 55 route adapter

Pass conditions:

- corridor receipt improves or creates one route
- Event 55 project state remains owner-controlled
- route invalidates correctly when corridor proof disappears

### BM-A09: Event 56 naval package

Pass conditions:

- only owner-approved package appears
- unsupported ship transfer remains unavailable
- source debit and buyer delivery are exact

### BM-A10: Experimental provider

Pass conditions:

- unapproved package has zero eligibility
- approved package appears only at allowed evolution
- delivery does not complete source project
- possession or use consequences call the owner

### BM-A11: Evolution I

Pass conditions:

- Chaos, Reach, members, regions, routes, enabled state, and MTTH all pass
- evolution log appears once
- no direct Chaos from activation
- four slots and new conventional classes unlock

### BM-A12: Evolution II disabled

Pass conditions:

- baseline and Evolution I trading continue
- no provider classes or flags from Evolution II activate
- no false evolution record

### BM-A13: Evolution III Grand Auction

Pass conditions:

- valid exceptional source
- eligible bidder pool
- unusable AI bidders abstain
- one winner
- one settled bid and delivery
- losing refunds exact
- no member list exposed

### BM-A14: Penetration and regional dismantling

Pass conditions:

- intelligence-capable member enters penetration
- cover trades maintain state
- evidence grows through actions
- one regional cell can be dismantled
- other disconnected cells survive
- regional negative Chaos receipt is one-time

### BM-A15: Full dismantling

Pass conditions:

- no active members, routes, or deliveries
- clearinghouse proof exists
- Reach below threshold
- reconstruction disabled
- final negative Chaos source once
- history preserved

### BM-A16: Civil war

Pass conditions:

- membership and credit do not copy to both sides
- route control decides inheritance or fracture
- active transaction settles safely

### BM-A17: Annexation during delivery

Run before and after dispatch.

Pass conditions:

- before dispatch cancels cleanly
- after dispatch uses successor, seizure, or cancellation rule
- no duplicate equipment or credit

### BM-A18: Save and reload

Save at:

- invitation pending
- offer available
- purchase reserved
- source debited
- delivery delayed
- auction open
- network dormant

Every state must resume without reroll, duplication, or stale UI.

### BM-A19: Multiplayer

Pass conditions:

- each player sees only its own membership and knowledge
- shared Network Reach remains synchronized
- one player cannot reveal another member without evidence
- offer reservation resolves deterministically
- auction winner is unique

### BM-A20: Performance

Pass conditions:

- no broad recurring country scan
- registered arrays remain bounded
- invalid records clean up
- long AI-only operation does not create event or decision spam

## Completion audits

Before completion claim:

1. probability baseline and comparison pass
2. decision and mission audit
3. localisation audit
4. asset coverage audit
5. documentation curation
6. authoritative workbook update and CSV export
7. improvement-loop pass
8. read-only event completion audit
9. parent review and concrete completion report

## Completion report contents

The final implementation report should list:

- files changed
- event and persistent-system identifiers
- member, route, offer, transaction, provider, and evidence architecture
- public values and thresholds
- decisions and missions
- AI scenarios and probability evidence
- Chaos sources and reversals
- cluster integration
- event connections
- DLC paths
- assets and consumers
- achievements
- docs and workbook updates
- task-specific validation findings
- blockers or simplifications

Do not claim completion while any accepted provider, route, decision, AI, localisation, asset, achievement, log, doc, or workbook surface is missing.


---

## Source file: `11_improvement_loop_closure.md`

# Improvement Loop Closure

## Playable promise reviewed

The event promises a secret economy that crosses diplomatic and military barriers.

The completed design supports that promise through:

- invitation-only membership
- route-backed access
- rotating source-proven offers
- real seller debits
- delayed deliveries
- Market Credit
- Exposure
- Network Reach
- government postures
- regional cells
- outsider evidence
- three evolutions
- event connections
- AI and probability scenarios
- regional and full dismantling

The mechanic changes player decisions. It does not rely on a flat national spirit or free equipment grant.

## Main weaknesses found in the rough concept

### The inventory risked becoming a store

The rough idea listed many goods but did not define how stock entered the market, how it moved, or how abuse was prevented.

The specification resolves this with provider receipts, source debit, route capacity, delayed delivery, recent-import locks, pricing, and transaction state.

### Membership growth lacked a bounded process

The rough idea described gradual invitations but did not define candidate search, sponsor ownership, rejection, dormancy, or performance limits.

The specification resolves this with one sponsor, one candidate, one route proof, one committed invitation per pulse, sparse registries, and explicit membership states.

### Secrecy lacked country-local knowledge

A single hidden category was not enough to explain what members and outsiders know.

The specification separates direct contact, regional awareness, proven identity, observer evidence, and sanitized global history.

### Routes needed gameplay

A route list without missions would have been passive flavor.

The specification turns routes into state, port, corridor, convoy, train, fuel, and intelligence commitments with disruption and repair.

### Evolutions risked being larger reward lists

The three evolutions now require Network Reach, members, regions, routes, Chaos, enabled state, and MTTH. They unlock new systems and owner packages instead of only bigger numbers.

### Positive Economy classification needed justification

The event creates genuine economic access and converts surplus into useful credit. Its benefits are strong enough for a High cluster role. Exposure, route failure, and counterplay limit it without changing its beneficial cluster identity.

## Accepted design limits

Broad expansion should stop at the current specification.

The event should not add a country, faction, leader roster, focus tree, territorial formable, or central criminal empire. Those additions would shift attention away from the logistics and trade system.

The chosen presentation remains one member category with evolving static pictures. The three public values and selected-offer flow can present the accepted mechanic without another persistent interface.

The event should not absorb legal international trade, embargo, condemnation, famine, migration, CBRN, naval, technology, or special-project ledgers. Provider and evidence adapters preserve ownership.

The event should not create ordinary goods without a source merely to keep every inventory slot full. An empty slot is better than a false transaction.

The event should not reveal every member at Evolution III. Anything Has a Price expands reach and capability, not omniscience.

## Rejected expansion ideas

### Central Black Market country

A hidden country tag or territorial headquarters would make the network easier to attack, but it would contradict the distributed route design and create unnecessary country-package work.

### Full scripted world map

A custom map of every route would expose information that members should not know. It would also add heavy GUI and refresh complexity. Route status is better shown through selected decisions, named endpoints, and category state.

### Black Market focus tree

A shared focus tree would attach a country-level system to unrelated governments and create generic routes. Government postures and existing country mechanics are better integration points.

### Separate criminality and trust meters

Both values are useful internally. Exposing them would raise the public mechanic to five values when Market Credit, Exposure, and Network Reach already explain the player's choices.

### Passive national modifiers

A permanent trade or production bonus would reward membership without route use and make the event feel static. The benefit should come from actual transactions.

### Automatic technology theft

Granting technology from equipment purchases would collapse the distinction between goods, research, and source projects. Technology remains an explicit rare package.

### Unlimited ship trading

Ship transfer is engine-sensitive and owner-dependent. Only verified naval packages should enter the market.

### Global anti-market decision category

Countries without evidence should have no actionable knowledge. Counterplay stays targeted and temporary.

## Replay value

Different campaigns change:

- founders
- route families
- member postures
- legal market access
- wars and embargoes
- seller surpluses
- buyer shortages
- provider packages
- regional cells
- exposure incidents
- auction lots
- outsider investigations
- evolution timing

A landlocked sanctioned minor should use the system differently from a neutral maritime broker or a major power running State Patronage.

## Closure handoff

The design is deep enough for implementation. Another broad planning expansion is not recommended before the first implementation and audit tranche.

The next improvement-loop pass should occur only after:

- the core registries and transaction state exist
- the member category is playable
- baseline offers and routes work
- at least one owner provider is integrated
- the probability baseline is available
- the first implementation audit identifies a new design gap

Before final completion, the improvement planner should return either a bounded addendum based on implemented evidence or a closure handoff. Any accepted addendum must be implemented, folded into the source specs, queued with a reason, or rejected with a reason.

## Final small tasks after implementation

When the runtime matches the specification, closure should focus on:

- final tuning from named probability scenarios
- category wording and value clarity
- transaction edge-case validation
- provider documentation
- asset consumer verification
- workbook alignment
- event-completion audit

These are finalization tasks, not reasons to add another large mechanic.


---

## Source file: `12_specialist_review_record.md`

# Specialist Review Record

## Execution status

The supplied subagent archive contained twenty current TOML definitions. Every definition was read in full.

An attempt was made to access the supplied outer Codex subagent runtime. The MCP tunnel returned HTTP `404`, so no project subagent was successfully spawned for this planning task.

The reviews below are internal role-based passes that apply the supplied subagent contracts. They are not represented as independent agent execution.

## Improvement-loop planner pass

Role applied: `chaosx_improvement_loop_planner`

Findings:

- The rough event had a strong persistent premise but lacked source accounting, pressure, counterplay, and failure states.
- The central playable loop is route-backed trade. A larger button list would add clutter.
- Three public values are sufficient.
- Expansion into countries, focus trees, or a large GUI would add maintenance without improving the core promise.
- The current design reaches closure for pre-implementation planning.

Disposition:

- accepted into the source specification
- broad further expansion rejected until implementation evidence exists

## Scripted-system architect pass

Role applied: `chaosx_scripted_system_architect`

Findings:

- The system needs sparse registries for members, routes, offers, deliveries, evidence, and providers.
- Offer and transaction IDs must persist across save and reload.
- Provider calls need versioned request and receipt state.
- Missing proof must fail closed.
- A recent-import ledger is required to stop buy and resale loops.
- Registered pulses replace whole-world recurring scans.
- Shared stockpile debit helpers should be reused where valid.

Disposition:

- accepted into the registry, provider, transaction, and performance specifications

## Decision and mission pass

Role applied: `chaosx_decision_mission_auditor`

Findings:

- One category can carry the system when it uses phase replacement and selected offers.
- The phase cap is three to five primary actions, with six as the hard maximum.
- Active missions should remain between one and three.
- Route creation must use state, port, corridor, and logistics objectives.
- Delivery should auto-complete after settlement.
- Costs must use concrete logistics and Market Credit, with four spendable types as the hard maximum.
- Exposure cleanup needs real capacity or route sacrifices.

Disposition:

- accepted into the decision and mission specification

## AI probability pass

Role applied: `chaosx_ai_probability_auditor`

Findings:

- Invitation, posture, offer, route, delivery, sale, auction, and investigation logic all contain weighted surfaces.
- Hard validity must be separated from score modifiers.
- Ten named scenarios provide stable before-and-after evidence.
- Exact probability claims are inappropriate when the normalized candidate pool is incomplete.
- The implementation needs baseline inspection, owner patch, and comparison.

Disposition:

- accepted into BM-P01 through BM-P10 and the audit prompt

## Localisation pass

Role applied: `chaosx_localisation_auditor`

Findings:

- The event needs period clandestine logistics, not modern digital-market language.
- Member knowledge must remain bounded in every dynamic line.
- Category status cannot become a pipe-separated telemetry row.
- Final offer text needs exact cargo, amount, price, route, risk, and delivery time.
- Evolution and workbook text should explain premise and progression without raw effects.

Disposition:

- accepted into the text-direction and localisation prompt

## Generated event art pass

Role applied: `chaosx_generated_event_art`

Findings:

- The event needs generated fictional documentary art because no single archival scene can represent the dynamic international network.
- Three report pictures cover first contact, seizure, and Grand Auction.
- Four static category pictures communicate growth without animation.
- No national identity, flag, or character portrait is needed.

Disposition:

- accepted into the asset inventory

## Icon artist pass

Role applied: `chaosx_icon_artist`

Findings:

- Decision icons must remain independent from category and achievement art.
- Market Credit needs a texticon.
- Twelve decision icons cover the accepted action families.
- Seven achievement triplets are required.
- Native transparency and final-size readability are hard gates.

Disposition:

- accepted into the asset inventory and asset prompt

## Asset source researcher pass

Role applied: `chaosx_asset_source_researcher`

Findings:

- Historical sources are valuable for design research, but the accepted runtime scenes are fictional composites.
- No specific real person, real photographed event, historical flag, or unique archival artifact is required.
- Runtime art should therefore use generated period-authentic scenes.

Disposition:

- research sources retained for design anchors, not runtime-image sourcing

## Event UI worker pass

Role applied: `chaosx_event_ui_worker`

Findings:

- The accepted event does not require a dedicated event-owned mechanic window.
- The normal category, selected-offer flow, evolving static picture, and dynamic tooltips meet the clarity budget.
- A future GUI should be considered only after implemented evidence proves that the category cannot present the system cleanly.

Disposition:

- no UI implementation handoff created

## Focus-tree pass

Role applied: `chaosx_focus_tree_auditor`

Findings:

- A Black Market focus tree would be generic across unrelated countries.
- Existing country routes can influence acceptance, posture, intelligence, or logistics through narrow hooks.
- The event should not own a new tree.

Disposition:

- no focus-tree prompt created

## Country-package pass

Role applied: `chaosx_country_package_auditor`

Findings:

- The event creates no country or territorial identity.
- Membership survives cosmetic changes but needs explicit rules for civil wars, annexation, release, and tag replacement.

Disposition:

- accepted into the membership and edge-case specifications

## Portrait pass

Role applied: `chaosx_portrait_creator`

Findings:

- No named leader, operative, broker, council, or officeholder is required.
- Report art should avoid identifiable portrait framing.

Disposition:

- no portrait package created

## Three-dimensional asset pass

Role applied: `chaosx_3d_model_pipeline`

Findings:

- The event trades existing equipment and owner-provided packages.
- It does not introduce a new visible unit, building, vehicle, aircraft, ship, creature, or map entity.

Disposition:

- no 3D job created

## Super-event text and audio passes

Roles applied:

- `chaosx_super_event_text_researcher`
- `chaosx_super_event_audio_researcher`

Findings:

- The event remains Minor Fire-Once and its evolutions do not create a campaign threshold that needs a super-event package.
- Report events and evolving category art provide proportionate presentation.

Disposition:

- no super-event prompt created

## Documentation curator pass

Role applied: `chaosx_documentation_curator`

Findings:

- Source design belongs in a bounded spec folder.
- Provider contracts and runtime behavior need permanent event docs after implementation.
- The stale Radar row and Positive Economy export conflict need explicit tracking.
- Internal role passes and actual subagent execution must not be confused.

Disposition:

- accepted into package structure and source record

## Spreadsheet pass

Role applied: `chaosx_spreadsheet_doc_worker`

Findings:

- The authoritative workbook must replace the stale Event 57 row.
- The cluster membership must be added as Positive Economy, High.
- CSV exports are not editable source.
- Workbook wording must match final in-game Event Details and evolution text.

Disposition:

- bounded spreadsheet-alignment prompt created for post-implementation use

## Completion-audit pass

Role applied: `chaosx_event_completion_auditor`

Pre-implementation findings:

- Completion must cover entry, persistence, decisions, AI, provider API, Chaos, cluster, assets, achievements, docs, and workbook.
- A working baseline shop without source debits or outsider counterplay would fail the spec.
- A source-only review cannot replace event and probability MCP evidence where those routes are available.

Disposition:

- completion-audit prompt created

## Repo explorer pass

Role applied: `chaosx_repo_explorer`

Finding:

- The implementation file map is broad enough that a repo explorer is useful before code, especially for event registration, event logs, cluster arrays, texticons, achievements, and existing provider patterns.

Disposition:

- future implementation should use the repo explorer only if current file locations or patterns remain unclear after direct inspection

## Skill-maintainer pass

Role applied: `chaosx_skill_maintainer`

Finding:

- The provider-receipt pattern may become reusable across several future trade and equipment events.
- It should become a skill update only after implementation proves the workflow and exposes a repeated need.

Disposition:

- no speculative skill edit planned


---

## Source file: `13_requirement_coverage_matrix.md`

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


---

## Source file: `research/historical_design_anchors.md`

# Historical Design Anchors

## Research purpose

This research pass did not try to reproduce one historical organization. It identified recurring conditions that made wartime illicit trade possible and translated them into Event 57 mechanics.

The event remains fictional. Historical sources support the route, scarcity, enforcement, intelligence, and captured-equipment logic.

## Scarcity creates demand

Wartime rationing and price controls created large differences between legal supply and what buyers wanted. The United States National Park Service describes illicit participation across producers, suppliers, sellers, buyers, counterfeit-coupon rings, and organized crime. It also records fuel-coupon theft, diverted livestock, hidden cash payments, and government concern that excess wartime income could drive inflation.

Design consequences:

- invitation acceptance should rise with shortages and unusable cash or industrial capacity
- the market should include producers, state depots, brokers, transport workers, and buyers
- Market Credit should represent several settlement methods
- supply can be diverted before goods reach the legal market
- governments need enforcement and propaganda responses
- a weak local deal and a large strategic shipment should not carry the same Exposure

## Enforcement is selective and limited

The same National Park Service source notes that fewer than 3,000 Office of Price Administration investigators covered the United States and focused on large violations. Public reporting, coupon verification, local authorities, criminal charges, and economic controls were also used.

Design consequences:

- outsiders need evidence before they receive counter-smuggling actions
- enforcement should focus on one route or case
- small occasional trades can remain hidden
- exceptional lots attract stronger investigation
- public scandal can matter even when the wider network survives
- full dismantling requires several local successes

## Borders and terrain shape routes

The Swiss National Museum describes wartime smuggling across the southern Swiss border. The flow changed with the war in northern Italy, refugee and partisan conditions, state rationing, currency values, and local border knowledge. Cargo included food, shoes, tires, silk, animals, weapons, money, and people. Allied intelligence services also relied on smugglers to move funds and weapons to resistance forces.

Design consequences:

- routes need real borders, terrain, ports, corridors, and intermediaries
- exchange conditions can make an unexpected direction profitable
- intelligence services can sponsor or penetrate the same route
- smugglers can carry several cargo classes without belonging to one ideology
- a neutral country can be a relay without becoming a full member
- war and government change can reverse a route's direction or reliability

## Blockades encourage strategic smuggling

United States National Archives records on economic warfare describe Allied efforts to control neutral shipping and stop strategic goods from reaching the Axis. The records state that smuggling of easily concealed strategic items increased as German supplies became thinner in 1942 and 1943. They also describe concern over neutral shipping, searches, blacklists, financing, and blockade evasion.

Design consequences:

- embargoes and blockades should increase demand and invitation willingness
- neutral channels are central to long routes
- searches and seizures should target shipping and cargo records
- strategic cargo should be more valuable and more exposed than ordinary goods
- Event 50 can create a meaningful Black Market interaction without being canceled by it
- maritime routes need convoy, port, blockade, and investigation state

## Money and diplomatic channels can become route assets

National Archives intelligence records describe gold moving through diplomatic pouches into Turkey and being smuggled onward into southeastern Europe. The records link the trade to currency confidence, exchange-rate differences, diplomats, banks, commercial transactions, and air transport.

Design consequences:

- Market Credit can include gold, currency, bank balances, barter claims, and diplomatic favors
- exchange and scarcity can change price direction
- officials and diplomatic access can create high-capacity but high-Exposure routes
- governments can participate through State Patronage without public acknowledgment
- covert air transport fits small, valuable cargo

## Military organizations can participate and create scandal

The United States National Archives account of the postwar Berlin black market records soldiers and civilians trading together and notes that allegations of American military personnel profiting from black markets created a serious public-relations problem and investigations.

Design consequences:

- military depots and occupation forces can become supply sources
- State Patronage and occupied-corridor routes need scandal consequences
- exposure can damage a government even when the cargo transaction succeeds
- a participant's official role does not make the trade legal or visible

## Captured equipment is a real strategic asset

United States Army historical material records technical intelligence teams seeking, evaluating, and transporting captured German weapons and equipment, including V-1 and V-2 specimens.

Design consequences:

- captured equipment and technical dossiers can become valuable lots
- equipment and technology must remain separate
- a physical weapon can be moved without granting the buyer every associated technology
- a complete technical package needs an explicit owner contract
- exceptional captured technology should be rare and source-backed

## Combined design rule

The Black Market should emerge from the interaction of scarcity, route opportunity, political tolerance, intelligence access, transport capacity, and enforcement pressure.

A universal catalog available to every country would contradict the research. The accepted design instead uses invitation-only membership, regional cells, route proofs, limited knowledge, real source debits, delayed delivery, neutral relays, government postures, and targeted investigations.


---

## Source file: `research/bibliography.md`

# Research Bibliography

## National Park Service

Megan E. Springate, “Home Front Illicit Trade and Black Markets in World War II.” National Park Service.

https://www.nps.gov/articles/000/home-front-illicit-trade-and-black-markets-in-world-war-ii.htm

Used for wartime scarcity, supply-chain diversion, counterfeit ration documents, gasoline coupons, public reporting, selective enforcement, propaganda, and inflation-control context.

## United States National Archives, Postwar Berlin

Kevin Conley Ruffner, “The Black Market in Postwar Berlin: Colonel Miller and an Army Scandal.” National Archives, Prologue, Fall 2002.

https://www.archives.gov/publications/prologue/2002/fall/berlin-black-market-1.html

Used for military and civilian participation, occupation conditions, investigation, discipline, and public-relations consequences.

## Swiss National Museum

Jean-Luc Rickenbacher, “The Smuggler Invasion.” Swiss history blog, Swiss National Museum.

https://blog.nationalmuseum.ch/en/2018/04/the-smuggler-invasion/

Used for border geography, wartime route reversal, currency incentives, convoys of smugglers, refugee and partisan conditions, weapons circulation, and intelligence-service use of smugglers.

## United States National Archives, Economic Warfare Records

“Military Agency Records, Record Group 169.” National Archives.

https://www.archives.gov/research/holocaust/finding-aid/civilian/rg-169.html

Used for neutral shipping controls, strategic smuggling, blockade enforcement, search and seizure, financing, and the increase in illicit trade as shortages deepened.

## United States National Archives, Office of Strategic Services Records

“Military Agency Records, Record Group 226.” National Archives.

https://www.archives.gov/research/holocaust/finding-aid/military/rg-226-3c.html

Used for gold smuggling through diplomatic channels, exchange-rate arbitrage, banks, diplomats, commercial transactions, and air transport.

## United States National Archives, War Department Records

“Military Agency Records, Record Group 107.” National Archives.

https://www.archives.gov/research/holocaust/finding-aid/military/rg-107-2.html

Used for smuggling of oil, diamonds, minerals, aviation fuel, neutral-country trade, and blockade policy.

## United States Army, Redstone Arsenal History

“Holger Nelson Toftoy.” Redstone Arsenal Historical Information.

https://history.redstone.army.mil/bio-toftoy.html

Used for captured enemy weapons, technical evaluation, transport of specimens, and the separation between possessing equipment and acquiring full research capability.

## Research limits

The sources describe several separate historical settings. They do not prove that one worldwide invitation-only organization existed with the mechanics in this specification.

Event 57 is a fictional Chaos Redux system built from recurring historical patterns. Names, values, membership rules, evolutions, achievements, and provider contracts are original design work.


---

## Source file: `prompts/57_the_black_market_asset_prompt.md`

# Event 57 Asset Production Prompt

Create the complete visual asset package for Chaos Redux Event 57, The Black Market, from `docs/specs/057_the_black_market_specs/09_assets_and_achievements.md`.

Follow the current repository versions of `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` when an inherited consumer proves animation is required, and `chaos-redux-subagents`.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Required reference inspection

Inspect the exact canonical families under:

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.agents\skills\chaos-redux-event-assets\assets\vanilla_reference`

Required folders:

- `event_art/report/`
- `icons/decision_categories/`
- `icons/decision_categories/pictures/`
- `icons/decisions/`
- `icons/achievements/`

Confirm the active runtime consumer and native size for every asset type. The decision-category-picture folder must have a labeled `contact_sheet.png`. Create it and update the reference README and catalog when missing.

## Report pictures

Create independent generated period-documentary scenes at `210x176` for:

1. `black_market_first_contact`
2. `black_market_seized_shipment`
3. `black_market_grand_auction`

Use 1936 to 1945 clothing, cargo, architecture, lighting, vehicles, and materials. Show guarded depots, concealed cargo, false logistics, mixed military stock, neutral transport, and anonymous intermediaries. Do not use modern containers, computers, neon crime imagery, readable generated text, national stereotypes, gore, or a central crime boss.

Final runtime folder:

`gfx/event_pictures/057_the_black_market/`

Proposed sprites:

- `GFX_report_event_057_black_market_first_contact`
- `GFX_report_event_057_black_market_seized_shipment`
- `GFX_report_event_057_black_market_grand_auction`

## Category icon and texticon

Create:

- `black_market_category`, a compact decision-category icon with a sealed crate and route or key motif
- `black_market_credit_texticon`, a small stamped account chit or ledger token for Market Credit

Use genuine native transparency, a dark outline, subtle shadow, stable centering, and strong readability at final size. No text, skulls, modern padlocks, coins as the main subject, fake checkerboards, white matte, or opaque square background.

Confirm the exact texticon precedent and dimensions before production.

## Category pictures

Create four separate static category pictures, each designed for the inspected consumer:

- `black_market_category_local_circuit`
- `black_market_category_international_network`
- `black_market_category_underground_economy`
- `black_market_category_anything_has_a_price`

The current reference family uses `114x101`, but do not assume that size without inspecting the live consumer.

The pictures should show increasing scale through depots, rail, ports, neutral freight, industrial material, technical cases, and exceptional guarded cargo. Do not use a world map as the main subject. Do not paint fake buttons, meters, values, or controls into the image.

Proposed sprites:

- `GFX_057_black_market_category_local_circuit`
- `GFX_057_black_market_category_international_network`
- `GFX_057_black_market_category_underground_economy`
- `GFX_057_black_market_category_anything_has_a_price`

## Decision icons

Create independent transparent `32x32` art for:

- `black_market_buy_lot`
- `black_market_sell_surplus`
- `black_market_commission`
- `black_market_open_route`
- `black_market_safer_route`
- `black_market_intelligence`
- `black_market_compartmentalize`
- `black_market_burn_route`
- `black_market_penetration`
- `black_market_suppression`
- `black_market_grand_auction`
- `black_market_underwrite`

Each icon needs its own source art and final-size composition. Do not resize category, focus, idea, or achievement art to satisfy a decision icon.

## Achievements

Create completed `64x64` art and the required grey and not-eligible states for these exact proposed IDs:

- `57_the_black_market_no_questions_asked`
- `57_the_black_market_enemy_quartermaster`
- `57_the_black_market_embargo_has_holes`
- `57_the_black_market_liquid_assets`
- `57_the_black_market_invisible_empire`
- `57_the_black_market_customs_seizure`
- `57_the_black_market_prototype_without_a_project`

Use the icon directions in the source spec. Achievement DDS files stay directly under `gfx/achievements/` and use the full achievement ID as basename.

## Workflow and outputs

Use narrow asset subagents according to the current asset skill. Generated scenes belong to `chaosx_generated_event_art`. Icons and achievement triplets belong to `chaosx_icon_artist`.

For each asset:

- retain source evidence
- retain the exact prompt and source mode
- preserve native alpha where required
- create processed PNG preview
- create final DDS
- validate dimensions, framing, readability, transparency, and edge quality
- create contact sheets at native size
- record proposed sprite and runtime path
- write a manifest and `gfx_handoff.md`

Use the temporary workspace:

`docs/assets/057_the_black_market/`

The parent owns final non-portrait `.gfx` wiring and gameplay consumers. Before full completion, promote durable provenance, prompt, review, and runtime crosswalk facts into permanent Event 57 documentation, confirm that no runtime path points into `docs/assets/`, then delete the completed temporary event workspace.

Do not substitute an unrelated existing icon, primitive local drawing, opaque placeholder, sourced modern photo, or weak resize. Mark a blocked asset honestly.


---

## Source file: `prompts/57_the_black_market_achievement_prompt.md`

# Event 57 Achievement Implementation Prompt

Implement the complete Event 57 achievement set from `docs/specs/057_the_black_market_specs/09_assets_and_achievements.md`.

Follow the current repository achievement pattern, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the Event 57 transaction, membership, exposure, route, evolution, embargo, provider, and auction receipts.

## Achievements

### `57_the_black_market_no_questions_asked`

Track settled purchases from all baseline cargo families while the player country remains below Exposure `50` for the whole attempt.

Required families are small arms, support or artillery, transport, fuel or convoys, and intelligence.

Track the highest Exposure reached. Debug grants and Force Trigger testing disqualify the run.

### `57_the_black_market_enemy_quartermaster`

Award after a settled equipment delivery whose proven source country is at war with the player at dispatch and settlement, while the transaction does not publicly expose that source.

Reject civil-war duplication, alliance before settlement, and any package without source proof.

### `57_the_black_market_embargo_has_holes`

While the player remains the target of Event 50 or another shared major strategic embargo, settle one fuel delivery, one military-equipment delivery, and one industrial-procurement delivery.

Every delivery must finish while the embargo is active.

### `57_the_black_market_liquid_assets`

The player must never adopt State Patronage. Track verified Market Credit earned from actual sales. Award after the player wins and receives a Grand Auction lot with sale-earned credit at least equal to the winning bid.

Debug credit, duplicated sale receipts, and an unsettled auction do not qualify.

### `57_the_black_market_invisible_empire`

Founding-member route. Award when Evolution III activates while the player has never reached Exposure `25`, never held a Compromised route, and never left membership.

This achievement is hidden until Event 57 fires.

### `57_the_black_market_customs_seizure`

The player must never accept membership. Track every active Black Market route through owned or controlled territory. Award after the player dismantles all of them and the connected regional cell enters verified dormancy.

### `57_the_black_market_prototype_without_a_project`

Award after an active member receives and validly fields or uses one owner-approved experimental package while the source project remains incomplete at dispatch and settlement.

An unapproved token, debug grant, or package whose owner project already completed does not qualify.

## Implementation rules

Use one-time receipts and stable tracking state. Save and reload must preserve progress without duplicate awards.

Do not infer source, hostility, route, cargo class, embargo, provider approval, project state, or settlement from loose flags when the Event 57 receipt already carries proof.

Player-country tracking must survive cosmetic changes. Civil-war and tag replacement behavior must follow the Event 57 membership-transfer contract and must not copy one achievement attempt to both sides.

Add exact localisation for title, description, hidden state, and completion. Final wording should follow the source spec direction and avoid raw mechanics or debug terms.

Add the achievement entries to the existing single Chaos Redux achievement registry. Do not create a new registry with another unique ID.

Coordinate with the asset package so each exact ID has:

- `<id>.dds`
- `<id>_grey.dds`
- `<id>_not_eligible.dds`

Update permanent Event 57 documentation with eligibility, proof, disqualifiers, and asset paths.

Run task-specific checks for:

- one-time award
- save and reload
- tag and cosmetic changes
- civil-war duplication
- debug disqualification
- source and transaction proof
- embargo timing
- Exposure maximum
- route compromise history
- auction settlement
- provider project isolation

Report any engine limitation that prevents an exact condition. Do not weaken the achievement silently.


---

## Source file: `prompts/57_the_black_market_decision_mission_prompt.md`

# Event 57 Decision and Mission Implementation Prompt

Implement the member and outsider decision systems from:

- `docs/specs/057_the_black_market_specs/02_membership_secrecy_and_government_postures.md`
- `docs/specs/057_the_black_market_specs/03_smuggling_routes_and_network_growth.md`
- `docs/specs/057_the_black_market_specs/05_decisions_missions_and_player_loop.md`
- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`

Follow the current repository versions of `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and the current vanilla decision documentation and precedents.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Presentation

Use one hidden member-only decision category with an evolution-dependent static category picture.

Show exactly three persistent custom values:

- Market Credit
- Exposure
- Network Reach

Show current posture and route status as qualitative state, not additional meters.

A normal phase exposes three to five primary actions. Six is the hard maximum. Keep visible active missions between one and three.

Use a selected-offer show and hide flow when the inventory cannot fit the action budget. AI must evaluate all valid offers without using the player selector.

Outsiders receive a separate temporary targeted counter-smuggling category only after a valid evidence receipt. Do not reveal a global membership list.

## Member action families

Implement the complete accepted families:

- acquire current lot
- list verified surplus
- commission a broad offer class after Evolution I
- open, repair, shift, or burn a route
- choose or change government posture
- underwrite limited Market Credit
- compartmentalize contacts and manage Exposure
- contribute or buy intelligence packages
- Grand Auction bidding after Evolution III
- dormant, suspended, withdrawal, expulsion, and reconnection actions

Use working labels only as design identifiers. Write final player-facing text during implementation.

## Missions

Implement route and delivery objectives that use real state, port, railway, convoy, fuel, airbase, unit-presence, and intelligence conditions where applicable.

Every dispatched purchase starts one visible delivery mission. It auto-completes when the transaction settles. A delayed delivery can create one bounded crisis mission, then must resolve.

Route-opening and repair objectives need enough time for the player and AI to act. Use the dynamic bands in the source specs. Avoid passive stockpile-check missions and second confirmation clicks after the objective is already complete.

## Costs

Use concrete costs that match the action:

- Market Credit
- convoys
- trains
- trucks
- fuel
- equipment
- civilian factory burden
- relevant XP
- conservative command power
- political power only for genuine government or diplomatic action

A single action may use no more than four spendable cost types. Every visible cost needs the matching texticon. Exposure is a consequence, not a spendable cost.

## Transaction safety

Every decision must call the Event 57 validation and receipt helpers. Do not place source debit, buyer grant, credit movement, route selection, and settlement as unrelated inline effects.

Prevent:

- double clicks
- stale selected offers
- duplicate source debit
- duplicate delivery
- repeated founding credit
- recent-import resale
- self-purchase
- route reward farming
- offer reroll by reopening the category
- auction bid duplication

## Postures

Implement:

- Compartmentalized Tolerance
- State Patronage
- Counterintelligence Penetration
- Suppression Campaign

Posture changes need a cooldown, valid political or security basis, and full category replacement. Switching posture cannot reset Exposure or grant another access package.

## Outsider counterplay

Implement evidence-gated actions for:

- inspect suspicious cargo
- watch a route or depot
- pressure a proven intermediary
- turn a broker
- coordinate a seizure
- dismantle a local cell

Each action targets one proven route, intermediary, delivery, or member. Failure can expose the investigation or close the case. Regional success must not destroy unrelated cells.

## AI

Every action needs AI validity and strategic weighting. Use BM-P01 through BM-P10. A patch to any weight requires the audit, patch, and compare cycle with `chaosx_ai_probability_auditor`.

## Cleanup

Remove or replace actions when:

- offers expire or settle
- selected targets become invalid
- routes change
- membership state changes
- posture changes
- deliveries settle
- investigations close
- countries disappear
- the network becomes dormant or dismantled

## Audit

After implementation, route the complete category to `chaosx_decision_mission_auditor`. It may patch bounded local issues and must write a handoff under `docs/plans/057_the_black_market_plans/subagent_handoffs/`.

Do not claim the decision layer complete while it exceeds the action budget, uses placeholder text, lacks AI, exposes raw triggers, leaves stale targets, or permits a repeatable reward loop.


---

## Source file: `prompts/57_the_black_market_scripted_system_prompt.md`

# Event 57 Scripted-System Architecture Prompt

Design and implement the reusable Event 57 scripted architecture from:

- `docs/specs/057_the_black_market_specs/01_core_event_spec.md`
- `docs/specs/057_the_black_market_specs/02_membership_secrecy_and_government_postures.md`
- `docs/specs/057_the_black_market_specs/03_smuggling_routes_and_network_growth.md`
- `docs/specs/057_the_black_market_specs/04_inventory_trade_and_provider_api.md`
- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`

Follow the current repository versions of `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the shared dynamic-effect and trigger registries, the offline wiki, vanilla documentation, and current Chaos Redux patterns.

Use `chaosx_scripted_system_architect` for the bounded architecture work. The parent retains final event, decision, localisation, asset, workbook, and completion ownership.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Required registries

Use `uses_normal_civilian_systems = yes` and exclude `is_special_chaos_country = yes` in the ordinary participant trigger. Allow a special human actor only through an explicit owner adapter.

Create sparse event-owned registries for:

- candidate, invited, active, dormant, suspended, former, and expelled members
- active, disrupted, compromised, and burned routes
- regional cells
- inventory offers
- active deliveries
- outsider evidence cases
- provider packages
- recent imports
- completed transaction and milestone receipts

Use stable IDs, aligned arrays or another verified repository pattern, explicit bounds, and cleanup.

## State machines

Implement idempotent state transitions for membership, routes, offers, and transactions.

Transaction states must cover generated, available, reserved, source debit pending, dispatched, delayed, partial, settled, seized, canceled, and invalidated.

A repeated call after save and reload must return the existing result or a safe reject reason. It must never repeat a debit, grant, credit movement, Chaos milestone, or achievement receipt.

## Public values

Implement country Market Credit and Exposure plus global Network Reach.

Centralize all floors, caps, bands, gains, losses, and durations. Provide concise scripted-localisation accessors and fail-closed setters.

Do not expose hidden trust, route pressure, capacity, reliability, provider proofs, or candidate scores as extra public values.

## Route API

Create helpers for:

- endpoint validation
- route creation
- route lookup
- status refresh
- capacity class
- risk class
- route selection
- route pressure
- regional-cell rebuild
- route burn and cleanup

Refresh only affected route records after world changes. Do not create a broad recurring world scan.

## Offer and transaction API

Create helpers for:

- demand registration from active members
- bounded offer generation
- source proof
- buyer validity
- reservation
- source debit
- dispatch
- delivery outcome
- settlement
- recent-import lock
- expiration
- cancellation

Reuse existing shared stockpile debit helpers when their contracts fit. Add a neutral shared helper only when several systems genuinely need it and update the matching dynamic-effect documentation in the same change.

## Provider API

Create owner files and permanent documentation for the versioned provider request and receipt contract.

Require:

- provider ID
- package ID
- offer class
- minimum evolution
- availability trigger
- buyer trigger
- source debit
- delivery effect
- quantity and price rules
- route rule
- Exposure rule
- reveal rule
- completion isolation
- DLC rule
- cleanup rule

Missing proof returns a stable reject reason and queues no offer.

An owner package remains owned by its source event. Event 57 must not set its completion flags, read its private ledger, or infer stock that was never published.

## Pulse architecture

Use one bounded event-owned scheduler for:

- inventory rotation
- invitation attempt
- registered Exposure recovery
- route-pressure recovery
- dormancy reconstruction
- evolution MTTH checks

Each pulse iterates only registered arrays or one bounded candidate sample. Do not add a whole-world daily, weekly, or monthly on-action.

Use narrow on-action adapters only when a relevant country, state, war, embargo, annexation, capitulation, route, or provider fact changes.

## Tuning

Place shared Event 57 tuning in `common/script_constants/057_the_black_market_constants.txt` where supported.

Centralize founder counts, slot caps, cadence, route limits, Exposure bands, Reach thresholds, price factors, reserve factors, handling classes, auction timing, recent-import lock, evolution MTTH, AI anchors, and Chaos values.

## Evidence and handoff

List every created helper, trigger, constant group, array, event target, state transition, call site, and public input or output in the handoff.

Document request proofs, reject reasons, default behavior, cleanup, and save safety.

Run source-level tests for duplicate IDs, array alignment, state transitions, one-time receipts, invalid scopes, missing cleanup, and public input reset.

Do not invent a generic global trade framework beyond what Event 57 and declared providers need.


---

## Source file: `prompts/57_the_black_market_ai_probability_audit_prompt.md`

# Event 57 AI Probability Audit Prompt

Audit every weighted Event 57 surface as `chaosx_ai_probability_auditor` in read-only mode.

Read:

- `docs/specs/057_the_black_market_specs/07_ai_probability_balance_and_edge_cases.md`
- Event 57 event, decision, scripted-effect, scripted-trigger, constants, and AI files
- the current probability tool documentation and repository rules

Start every surface with `hoi4.probability_inspect`.

## Required weighted surfaces

Inspect:

- founding broker selection
- founding member selection
- invitation candidate selection
- candidate response and posture
- offer class generation
- provider-package selection
- seller and source selection
- purchase choice
- sale choice and size
- route selection
- delivery outcome
- Exposure response
- outsider investigation action
- auction bidding
- evolution MTTH

Separate hard validity from score modifiers. State whether each pool is complete. Never report an exact normalized probability from an incomplete candidate pool.

## Named scenarios

Use the same scenario IDs before and after any patch:

- `BM-P01` invitation under desperation
- `BM-P02` route proof over friendly relations
- `BM-P03` safe surplus sale
- `BM-P04` fuel purchase utility
- `BM-P05` route selection
- `BM-P06` high-Exposure posture response
- `BM-P07` provider approval gate
- `BM-P08` Grand Auction utility
- `BM-P09` embargo-circumvention demand
- `BM-P10` counter-smuggling evidence

Use the exact scenario facts and expected ordering in the source spec.

## Evidence methods

Use:

- `hoi4.probability_evaluate` when the full normalized pool is known
- `hoi4.probability_sweep` for shortage, reserve, Exposure, route pressure, embargo, and strategic-utility thresholds
- `hoi4.probability_simulate` for declared offer and invitation pools when sampling is appropriate
- `hoi4.probability_sequence` only when cadence, cooldowns, caps, recovery, expiry, route loss, and terminal states are completely declared
- `hoi4.probability_compare` after the owner patches any weight
- `hoi4.probability_render` for matrix, sensitivity, timing, or comparison evidence when useful

Label each result exact, bounded, sampled, score-only, or unresolved.

## Pass expectations

- A valid desperate embargoed wartime buyer strongly outranks a peaceful open-trade country.
- A no-route invitation candidate has hard zero regardless of relations.
- A seller near its readiness reserve has zero sale score.
- A fuel-starved naval or air power values fuel above unrelated prestige cargo.
- An open land route outranks a strained maritime route for ordinary medium cargo, while an island case reverses feasibility.
- A State Patron above Exposure `75` prioritizes cover, route burn, withdrawal, or suppression when shortage is low.
- An unapproved provider package has exact zero.
- An AI bidder abstains from an exceptional package it cannot use even when it has abundant credit.
- Event 50 raises demand only for strategically relevant packages.
- An outsider with rumor only and no route has no active seizure action.

## Audit cycle

For every weight patch:

1. record baseline inspect and scenario evidence
2. return the bounded issue to the owner
3. do not edit source
4. after the owner patch, run `hoi4.probability_compare` with the same scenarios
5. report improvement, regression, dominance, starvation, unresolved factors, and candidate-pool completeness

## Handoff

Write the audit under:

`docs/plans/057_the_black_market_plans/subagent_handoffs/`

Include:

- surface and source identifiers
- scenario hashes
- candidate-pool completeness
- baseline result
- expected ordering
- post-patch comparison when applicable
- exact blockers
- recommended owner action

Do not choose a new balance philosophy or patch gameplay.


---

## Source file: `prompts/57_the_black_market_localisation_audit_prompt.md`

# Event 57 Localisation Audit Prompt

Audit Event 57 player-facing and scripted localisation as `chaosx_localisation_auditor`.

Read:

- `docs/specs/057_the_black_market_specs/08_event_chain_logs_localisation_and_catalog_alignment.md`
- all Event 57 event, decision, mission, achievement, Event Details, evolution, scripted-localisation, and workbook-facing text
- current repository localisation rules

## Required tone

Use period clandestine logistics and government language. Focus on restricted cargo, depots, neutral freight, false paperwork, corrupt officials, captured stock, intelligence contacts, route risk, customs searches, and political exposure.

Remove modern online-market language, dark-web language, gangster caricature, central-mastermind lore, generic dramatic filler, raw script terms, tuning history, and implementation notes.

## Secrecy

Check every line for unauthorized knowledge.

- Outsiders cannot see the member list.
- Members know only direct contacts, routes, and proven counterparties.
- Offer provenance must match the receipt.
- A seizure exposes only the proven route, cargo, intermediary, or participant.
- Evolution text must not reveal every hidden capability.

## Category clarity

The category must show Market Credit, Exposure, and Network Reach clearly without a debug-style telemetry row.

Each value needs a concise cause, consequence, next threshold, and response. Do not use divider characters to simulate columns.

Offer text must state cargo, amount, Market Credit price, other visible costs, route family, risk class, delivery-time band, and the main blocked reason.

## Dynamic text

Audit all branches for:

- selected offer
- quantity
- route
- risk
- delivery time
- posture
- Reach stage
- Exposure band
- known country or state
- evidence target
- transaction outcome

Every selector needs a neutral default that cannot leak another country or raw key.

## Event and log alignment

Check:

- Event 57 name
- founder invitation
- first member report
- transaction reports
- outsider reports
- three evolutions
- main History row
- History details
- Evolution history rows
- Event Details catalog previews
- achievement text

History remains sanitized and actorless. Event Details does not show active members, routes, balances, inventory, or readiness formulas.

## Workbook-facing wording

Compare final in-game Event Details and evolution descriptions with the catalog text that the spreadsheet worker will use. Flag any mismatch before workbook update.

## Patch authority

Patch bounded localisation defects directly. List every changed key in the handoff. Do not redesign the mechanic or reveal hidden content to make a tooltip easier.

Write the handoff under:

`docs/plans/057_the_black_market_plans/subagent_handoffs/`


---

## Source file: `prompts/57_the_black_market_spreadsheet_alignment_prompt.md`

# Event 57 Catalog Alignment Prompt

Update only the authoritative workbook:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Use `chaosx_spreadsheet_doc_worker` and the current spreadsheet skill.

Read the final implemented Event 57 name, Event Details text, evolution text, cluster membership, and status. Do not use the stale CSV row as source of truth.

## Event row

Replace the old Event 57 Radar identity with:

- ID `57`
- The Black Market
- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member
- final implementation status proven by the parent

Write concise player-facing details that match the in-game Event Details premise.

Add summaries for:

- Evolution I, International Network, `200+`
- Evolution II, The Underground Economy, `400+`
- Evolution III, Anything Has a Price, `600+`

Do not list raw modifiers, hidden formulas, internal values, source file names, or implementation history.

## Cluster row

Add Event 57 to Positive Economy with High member severity while preserving many-to-many and repeated-slot semantics in the current workbook model.

Do not remove Event 18 or unrelated members.

## Export

After saving the workbook, run:

`python .tools/export_event_catalog_csv.py`

Verify that the Events, Clusters, and Scenarios CSV exports regenerate successfully. Never edit those CSVs directly.

## Preservation

Preserve workbook structure, formatting, formulas, filters, validation, and unrelated rows.

Return a handoff with changed sheets, row identifiers, exact fields, export result, and any mismatch that still requires parent action.


---

## Source file: `prompts/57_the_black_market_event_completion_audit_prompt.md`

# Event 57 Completion Audit Prompt

Audit the final Event 57 implementation as `chaosx_event_completion_auditor` in read-only mode.

Compare the repository against every file under:

`docs/specs/057_the_black_market_specs/`

Also inspect all accepted plans and subagent handoffs under:

`docs/plans/057_the_black_market_plans/`

## Required coverage

Verify:

- canonical `chaosx.nr57.1` entry
- fire-once registration and Chaos level
- connected founding transaction and rollback safety
- sanitized history and actor handling
- membership states and secrecy
- Market Credit, Exposure, and Network Reach
- sparse processing
- route types, states, missions, and refresh
- offer rotation and slot caps
- real source debits
- recent-import lock
- transaction state and save safety
- government postures
- outsider evidence and counterplay
- provider API and owner isolation
- Events 50, 54, 55, and 56 connections
- three paced evolutions and enable behavior
- Event 57 Chaos sources and reversals
- Positive Economy High membership
- AI and probability evidence
- DLC paths
- decision and mission audit
- localisation audit
- report art, category pictures, icons, texticon, and achievement triplets
- seven achievements
- permanent docs
- authoritative workbook and regenerated CSV exports
- temporary asset-workspace cleanup

## Evidence gates

Confirm that event-chain MCP evidence exists for the final source.

Confirm that every weighted surface has baseline and post-patch comparison evidence through the same BM-P01 to BM-P10 scenarios.

Do not treat source inspection as equivalent when the required MCP route was available.

## Simplification audit

Flag any:

- free or source-less goods
- missing route proof
- immediate delivery replacing missions
- unlimited credit conversion
- buy and resale loop
- copied membership after civil war
- global member list leak
- outsider actions without evidence
- missing AI
- missing DLC fallback
- disabled evolution that still unlocks content
- stale catalog row
- placeholder or reused asset
- unimplemented achievement
- unreported provider limitation
- broad recurring world scan

## Plan disposition

Every accepted addendum must be implemented, folded into specs, queued with a reason, or rejected with a reason.

Return a report under:

`docs/plans/057_the_black_market_plans/`

Separate implemented, partially implemented, missing, blocked, simplified, and unverified items. Do not patch gameplay or claim completion.


---

## Source file: `prompts/57_the_black_market_coding_prompt.md`

# Event 57 Implementation Prompt

Implement Chaos Redux Event 57, The Black Market, to the complete source specification under:

`docs/specs/057_the_black_market_specs/`

Read every file in that folder before editing. Also read the current repository versions of `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, all required offline Paradox wiki pages, current vanilla documentation, and relevant Chaos Redux precedents.


Spawn every project subagent with a complete self-contained prompt and `fork_context=false`.

## Core event

Keep the canonical entry `chaosx.nr57.1`.

Register Event 57 as:

- Minor Fire-Once
- Chaos level `1`
- Positive Economy
- High member

The entry must create one connected invitation-only founding cell with two to four countries, targeting three. Favor the player only when eligible. Do not force invalid membership or create a route without endpoint proof.

Resolve founder acceptance before consuming the fire-once event when the event framework requires that ordering. If no valid accepted cell can form, leave the event unfired and clean every temporary record.

The global history row must not reveal founders, members, routes, inventory, or an actor flag.

## Persistent system

The random event fires once. Later invitations, routes, offers, deliveries, investigations, evolutions, dormancy, and reconstruction belong to the event-owned runtime.

Create sparse registries for members, routes, cells, offers, deliveries, evidence, providers, recent imports, and one-time receipts. Use bounded registered pulses and narrow change hooks. Do not add a whole-world recurring daily, weekly, or monthly scan.

Implement idempotent membership, route, offer, and transaction state machines. Save and reload must not reroll outcomes, duplicate equipment, repeat credit, repeat Chaos, or create duplicate missions.

## Public mechanic

Expose only:

- Market Credit
- Exposure
- Network Reach

Use the bands, thresholds, and stage meanings in the specs. Keep trust, capacity, reliability, route pressure, candidate scores, demand components, and provider proofs internal.

Implement government postures:

- Compartmentalized Tolerance
- State Patronage
- Counterintelligence Penetration
- Suppression Campaign

Posture changes require cooldowns and valid conditions. They cannot reset Exposure or grant another founding package.

## Routes

Implement land borders, neutral intermediaries, maritime shipping, occupied corridors, Event 55 international corridors, and evolved covert air routes.

Routes need stable IDs, endpoint proof, Open, Strained, Disrupted, Compromised, and Burned states, cargo capacity class, risk class, delivery-time band, pressure, investigations, and cleanup.

Route opening and repair must use real state, port, railway, convoy, fuel, airbase, intelligence, or unit-presence objectives. Do not reduce them to political power purchases.

## Inventory and trade

Implement the exact slot caps:

- baseline `3`
- Evolution I `4`
- Evolution II `5`
- Evolution III `6`

Every offer needs a source, eligible buyer, and route. Preserve an immutable offer receipt. War, ideology, faction membership, hostility, and embargoes are never automatic transaction bans when a valid underground path exists.

Member sales must calculate a dynamic readiness reserve, debit real stock before dispatch, and pay bounded Market Credit. Use the recent-import ledger to prevent immediate resale. Prevent self-purchase, duplicate source debit, repeated listing rewards, and offer rerolls through UI or reload.

Every purchase starts a delayed delivery mission. Support clean, delayed, partial, seized, canceled, and sting outcomes. A delayed job can create one bounded crisis step, then must resolve.

Implement Market Credit sources, caps, network fees, limited underwriting, withdrawal settlement, auction bids, and anti-arbitrage controls. It cannot become unlimited converted political power.

## Provider API

Implement the event-owned versioned provider contract in dedicated Event 57 effects, triggers, and documentation.

Require provider ID, package ID, offer class, minimum evolution, availability, buyer eligibility, source debit, delivery effect, amount, price, route, Exposure, reveal, completion isolation, DLC behavior, and cleanup.

Missing proof returns a reject reason and creates no offer.

Integrate approved adapters for Events 50, 54, 55, and 56, captured or collapsed stock, intelligence, normal technology, naval assets, CBRN equipment, and special projects only where their owners publish valid packages.

Receiving goods must not grant technology. Receiving a technical or experimental package must not complete the source event or project unless its owner explicitly defines that exact result.

## Decisions and missions

Use one hidden member category with evolution-dependent static art. Show three to five primary actions, never more than six, and one to three active missions.

Use a selected-offer flow when needed. AI evaluates all valid offers directly.

Implement member purchase, sale, commission, route, posture, underwriting, Exposure, intelligence, delivery, auction, dormancy, suspension, withdrawal, expulsion, and reconnection actions.

Implement a separate temporary evidence-gated outsider category for investigation, seizure, intermediary pressure, broker turning, local cell dismantling, and member suppression.

Every cost needs the correct texticon and no action may use more than four spendable cost types.

## Evolutions

Implement:

1. International Network at `200+` Chaos, Reach `35+`, world proof, and paced MTTH
2. The Underground Economy at `400+` Chaos, Reach `65+`, world proof, and paced MTTH
3. Anything Has a Price at `600+` Chaos, Reach `85+`, world proof, and paced MTTH

Use the member, region, route, delivery, and alternate readiness packages in the source specs.

Evolution activation gives zero Chaos. Disabled evolutions must not set recorded flags or unlock their content. Baseline trading must continue safely.

## Chaos

Implement the complete guarded Event 57 map:

- first completed interregional delivery
- first completed trade between active enemies
- first major embargo-circumvention delivery
- first approved experimental delivery
- first exceptional stockpile delivery
- first route-backed connection across four regions
- mature regional cell dismantling
- verified network dormancy after Evolution I or later
- full network dismantling

Use one-time or episode receipts and the source values from the spec as tuning anchors. Do not duplicate wars, annexations, deaths, contamination, nuclear use, condemnation, world tension, or other shared sources.

## AI and probability

Implement strategic AI for invitation, posture, purchase, sale, route, Exposure response, penetration, suppression, outsider investigations, and auctions.

Before any weighted patch, run `chaosx_ai_probability_auditor` with `hoi4.probability_inspect` and BM-P01 through BM-P10. The owner applies the patch. The auditor then runs `hoi4.probability_compare` with the same scenarios.

Hard-invalid options must be zero before weighting.

## Event logs and text

Wire event name, debug name, history, actor handling, Event Details, and three evolution records across all required shared surfaces.

Write final localisation from the spec's period clandestine-logistics direction. Do not paste working labels as final text. Preserve country-local knowledge and avoid modern digital-market terms, raw variables, debug phrasing, and implementation history.

## Assets and achievements

Create and wire the complete asset package from the asset prompt:

- three report pictures
- category icon
- Market Credit texticon
- four evolution-dependent category pictures
- twelve decision icons
- seven achievement triplets

Implement all seven achievements from the achievement prompt with exact receipt-based tracking and disqualifiers.

Use generated event art and icon subagents according to the current asset workflow. No placeholder or resized unrelated asset counts as complete.

## DLC support

Implement the no-DLC core and the relevant La Résistance, Arms Against Tyranny, No Step Back, By Blood Alone, Man the Guns, and owner special-project enhancements described in the acceptance spec.

DLC absence must never block the core event lifecycle.

## Catalog and documentation

Replace the stale Event 57 Radar identity in the authoritative XLSX after implementation facts are final. Add Positive Economy High membership and all three evolution summaries. Run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

Write permanent Event 57 overview, membership, route, inventory, provider, AI, balance, and validation documentation.

## Required audits

Use the event MCP inspect, render, and compare workflow for the final event chain.

Run:

- scripted-system architecture review
- probability baseline and comparison
- decision and mission audit
- localisation audit
- asset coverage review
- documentation curation
- workbook alignment
- improvement-loop pass
- read-only event completion audit

Resolve every accepted addendum. Do not claim completion while a required system, provider, decision, AI path, text key, asset, achievement, log, doc, workbook field, or validation gate is missing.

Report every blocker or simplification. Do not use an unapproved fallback.


---

## Source file: `prompts/57_the_black_market_goal_prompt.md`

# /goal: Implement Event 57, The Black Market

Implement Event 57 to the fullest extent from `docs/specs/057_the_black_market_specs/`. Read every source spec before editing, plus the coding, decision, scripted-system, asset, and achievement prompts in that folder. Follow current `AGENTS.md`, the relevant project skills, required offline wiki pages, vanilla documentation, and Chaos Redux precedents.

Keep `chaosx.nr57.1` as the canonical entry. Register ID 57 as Minor Fire-Once, Chaos level 1, and Positive Economy High. The first firing must create a valid connected invitation-only cell of two to four countries, targeting three, with the player included only when eligible. Resolve failure before the fire-once commit so an impossible or rejected cell leaves no partial network or consumed event.

Build the persistent runtime after the single firing. Use sparse registered members, routes, regional cells, offers, deliveries, evidence cases, providers, recent imports, and one-time receipts. Do not add a broad recurring country scan. Membership, route, offer, and transaction states must be idempotent and save-safe.

Expose only Market Credit, Exposure, and Network Reach as persistent custom values. Implement Compartmentalized Tolerance, State Patronage, Counterintelligence Penetration, and Suppression Campaign. Keep member knowledge compartmentalized and the global history actorless and sanitized.

Every offer requires a real source, eligible buyer, and valid route. Seller stock must be debited before dispatch. Implement protected reserves, network fees, credit caps, limited underwriting, recent-import resale locks, delayed delivery, partial loss, seizure, stings, route pressure, and regional or full dismantling. Prevent source-less goods, duplicate debit, instant resale, self-purchase, repeated founding credit, and reload rerolls.

Implement the versioned owner provider API and approved adapters for Events 50, 54, 55, and 56 and other approved equipment, intelligence, naval, CBRN, technology, and special-project owners. Missing proof must fail closed. Goods must not grant unrelated technology or complete the source event or project.

Use one member decision category with evolution-dependent static pictures, three to five primary actions, six as the hard maximum, and one to three active missions. Add the separate evidence-gated outsider category. Use real state, route, logistics, and intelligence requirements. No action may use more than four spendable cost types and every visible cost needs the correct texticon.

Implement all three paced evolutions with Chaos, Reach, member, region, route, enabled-state, and MTTH proof. Evolution activation gives zero Chaos. Implement every guarded Event 57 Chaos milestone and reversal without duplicating shared Chaos sources.

Implement strategic AI. Run `chaosx_ai_probability_auditor` with `hoi4.probability_inspect` on BM-P01 through BM-P10 before weight changes, then `hoi4.probability_compare` after the owner patch. Use the event MCP inspect, render, and compare workflow for the final chain.

Create and wire the complete accepted asset package and all seven achievements. Do not use placeholders, resized unrelated assets, or unreported substitutes. Preserve the no-DLC core and relevant DLC enhancements.

Update Event History, Event Details, evolution logs, localisation, docs, the authoritative workbook, and regenerated CSV exports. Never edit the CSV exports directly.

Near completion, spawn `chaosx_improvement_loop_planner` with a complete prompt and `fork_context=false` and resolve its addendum or closure handoff. Run the decision, localisation, probability, documentation, and read-only completion audits. Keep iterating until every mapped system and acceptance scenario is complete. Do not claim completion until the implemented files satisfy the full specification. Report every blocker, omission, fallback, and simplification clearly.
