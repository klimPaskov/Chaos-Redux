# Event 60 technology regression registry contract

## Purpose

This matrix defines the information and review needed before any technology family can be regressed by Research Failure.
It does not provide unverified technology IDs.
The implementation agent must populate the live registry from the installed technology graph and owner policies.

## Required branch record

| Field | Required content | Failure behavior |
| --- | --- | --- |
| `branch_id` | Stable Event 60 branch identity | Block entry |
| `display_domain` | Player-facing broad domain | Block decision and archive display |
| `folder_or_graph` | Actual technology folder or graph owner | Block entry |
| `ordered_nodes` | Safe predecessor order for the current tree variant | Block regression |
| `protected_roots` | Mutually exclusive roots, setup nodes, minimum surviving node | Block regression |
| `bundle_id` | Bundle linking chassis, hull, module, facility, or other dependent nodes | Block partial family mutation |
| `owner_id` | Vanilla, Chaos Redux core, or named event or system | Unknown owner means protected |
| `owner_policy` | Protected, regressible, degradable, or replaceable | Missing policy means protected |
| `max_depth` | Maximum safe generations that can be removed | Default zero |
| `legacy_consumer_policy` | Existing equipment, line, design, unit, building, and facility treatment | Block if live consumer can corrupt |
| `rediscovery_route` | Normal research, owner decision, special project, or owner callback | Block if no route exists |
| `research_bonus_category` | Safe category used by Archive Recovery | No targeted bonus if absent |
| `dlc_gate` | Exact DLC or tree condition | Skip when false |
| `mutual_exclusion_group` | Competing branches that must never be switched | Block if unresolved |
| `slot_or_system_protection` | Marks research-slot or research-system nodes | Always protect unless accepted override |
| `strategic_system_protection` | Marks nuclear, chemical, biological, alien, singularity, and similar systems | Protect without owner route |
| `validation_state` | Verified, excluded, or blocked with reason | Only verified entries enter pool |
| `graph_evidence` | MCP revision, rendered branch, compare result | No completion claim without evidence |
| `runtime_evidence` | Production, equipment, save, reload, and rediscovery tests | No completion claim without evidence |

## Technology policy classes

| Policy | Technology state during incident | Existing consumers | Recovery |
| --- | --- | --- | --- |
| Protected | Technology remains researched | Unchanged | None needed |
| Regressible | Technology node can be removed and predecessor retained | Legacy policy applies | Normal research or owner-approved grant |
| Degradable | Node remains researched but owner applies a damaged operational state | Owner controls penalties | Owner recovery project or state restoration |
| Replaceable | Node is removed or replaced with a damaged predecessor state | Owner controls conversion | Owner-defined route |

## Domain review table

The implementation must complete one row for every installed domain and tree variant.

| Domain | Baseline eligibility direction | Main safety question | Minimum coverage target |
| --- | --- | --- | --- |
| Infantry equipment | Usually eligible | Does removing a generation preserve stockpiles, lines, and variants | At least one military domain when safe |
| Support weapons and equipment | Usually eligible by safe sub-branch | Are bonuses linear and recoverable | Optional according to frontier |
| Artillery and anti-air | Usually eligible | Are equipment unlocks and upgrades bundled correctly | Weighted by production and units |
| Armour | Bundle review required | Chassis, modules, variants, designers, and lines | Weighted by active armour use |
| Aircraft | Bundle review required | Airframe, engine, weapons, modules, wings, and lines | Weighted by air production and wings |
| Naval | Bundle review required | Hulls, modules, designs, ships, and construction | Weighted by fleet and dockyards |
| Industry | Eligible within protected chosen branch | Never switch concentrated and dispersed branches | Core coverage at Evolution II and III |
| Production methods | Eligible within protected chosen branch | Never switch mutually exclusive production paths | Core coverage at Evolution II and III |
| Electronics | Usually eligible | Encryption, decryption, radar, agency interaction | Core coverage at Evolution II and III |
| Engineering | Usually eligible | Support companies, facilities, and derived unlocks | Broad coverage when safe |
| Radar | Usually eligible | Existing radar structures and detection remain valid | Weighted by infrastructure and use |
| Rocketry | Conditional | Delivery systems, stockpiles, and special projects | Normal nodes only without owner policy |
| Nuclear | Protected by default | Reactors, bombs, special projects, decisions, terminal systems | Owner opt-in only |
| Doctrine | Protected by default | Branch choice, mastery, and Event 27 ownership | Separate accepted design required |
| Chemical and biological | Protected by default | Equipment, contamination, condemnation, owner decisions | Owner opt-in only |
| Alien and Kruger | Protected by default | Event 16 lifecycle and special actors | Event 16 policy only |
| Custom mod technology | Protected by default | Unknown markers and owner behavior | Explicit owner registration only |

## Regression transaction order

1. Resolve target and incident sequence.
2. Read only verified registry entries that exist in the active DLC and mod state.
3. Identify researched frontier nodes and their valid predecessors.
4. Build bundle and descendant closure.
5. Inspect live consumers where the family policy requires it.
6. Select domains according to severity and target profile.
7. Select branch depth without crossing protected roots or maximum depth.
8. Store the complete planned node list, predecessor list, owner callbacks, and family penalties.
9. Verify that every removed node has a rediscovery route.
10. Verify that the total transaction reaches the minimum meaningful severity.
11. Apply descendants before predecessors.
12. Record one ledger entry per node and one receipt per family transaction.
13. Recalculate family penalties and AI priorities.
14. Verify the post-transaction graph.
15. Roll back or fail closed according to the verified engine method when any step fails before commitment.

## Lost-knowledge ledger record

| Field | Meaning |
| --- | --- |
| Incident sequence | Source firing or active-evolution transaction |
| Country | Current owner of the national ledger |
| Technology | Lost node identity |
| Branch and domain | Recovery and display grouping |
| Previous frontier | Highest safe node remaining |
| Depth | Generation distance lost |
| Owner and policy | System responsible for special behavior |
| Legacy consumer state | Lines, designs, units, facilities, penalties |
| Loss date | History and achievement timing |
| Recovery state | Outstanding, researched, granted, obsolete, abandoned, or owner-restored |
| Recovery source | Ordinary research, Gift, Brilliant Scientist, donor, owner project, or other approved route |
| Direct-grant disqualifier | Achievement tracking |
| Cleanup receipt | Prevent duplicate family restoration |

## Required graph scenarios

| Scenario ID | Setup | Evidence required |
| --- | --- | --- |
| `TECH-01` | Normal linear infantry branch with several researched generations | Predecessor order, descendant closure, removal, stockpile and line persistence, rediscovery |
| `TECH-02` | Concentrated industry branch | Root retained, descendant rollback, no dispersed grant or switch |
| `TECH-03` | Dispersed industry branch | Root retained, descendant rollback, no concentrated grant or switch |
| `TECH-04` | Flexible production branch | Root retained and competing path untouched |
| `TECH-05` | Streamlined production branch | Root retained and competing path untouched |
| `TECH-06` | Tank family under active armour DLC | Chassis, modules, variant, design, line, deployed unit, rediscovery |
| `TECH-07` | Aircraft family under active airframe DLC | Airframe, modules, design, line, wings, rediscovery |
| `TECH-08` | Naval hull and module family | Existing ship, construction line, design, rediscovery |
| `TECH-09` | Radar and electronics with built radar | Structure retained, effects changed safely, rediscovery |
| `TECH-10` | Rocketry with existing delivery assets | Normal node policy and strategic-system protection |
| `TECH-11` | Event-owned protected technology | No mutation, no ledger entry, owner remains valid |
| `TECH-12` | Event-owned regressible technology | Owner callback, degraded consumers, recovery, cleanup |
| `TECH-13` | Non-researchable focus grant | Protected unless owner supplies valid recovery route |
| `TECH-14` | Active research project at partial progress | Project cleared, progress loss recorded, later bonus bounded |
| `TECH-15` | Gift from Scientists restores one lost node | Compatibility, receipt, family penalty update, achievement disqualifier |
| `TECH-16` | Donor union helper called during incident | Additive grant does not remove existing tech or alter slot ledger |
| `TECH-17` | Save and reload after rollback | Exact technology and ledger state persists once |
| `TECH-18` | Civil war after rollback | Damage propagates or transfers without unaffected duplicate science |

## MCP technology evidence

Implementation must use:

- `hoi4.tech_inspect` for every candidate folder, branch, owner technology, prerequisite, unlock, grant, bonus, reference, and missing asset.
- `hoi4.tech_render` for each affected folder or branch and for the final registry coverage view.
- `hoi4.tech_compare` after source changes.

The completion report should list the MCP revision or artifact references, verified branch count, excluded branch count, blocked branch count, and the reason for every blocked normal domain.
