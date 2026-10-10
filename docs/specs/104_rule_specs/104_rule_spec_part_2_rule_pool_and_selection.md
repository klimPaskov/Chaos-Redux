# Event 104 Rule: rule pool and selection

## Admission contract

The runtime pool is an explicit allowlist of actual game rules.
It is built from the effective installed rule definitions and their consumers, then reviewed and versioned with the implementation.
It is never a wildcard sweep of every setting under `common/game_rules`.
Discovery can enumerate all loaded definitions during development, but discovery does not grant runtime eligibility.

Each rule must pass all admission tests below before it receives a runtime registry row.

| Test | Required evidence |
| --- | --- |
| Native identity | Exact rule key, effective source file, load order, source revision, canonical default, and complete option list. |
| Runtime writer | A documented and validated operation that changes this native option during play. |
| Readback | Exact native option query immediately before and after mutation. |
| Continuing consumer | A current gameplay consumer that reads the option after startup. |
| Material transition | At least one destination with a demonstrated difference in a current reachable action or behaviour. |
| Persistence | The option and its effects survive save and reload. |
| Global authority | The setting agrees across human and AI consumers and multiplayer peers. |
| Compatibility | Required content exists, relevant DLC is enabled, and other authoritative restrictions retain their documented precedence. |
| Reversibility of rejection | A rejected attempt either leaves native state unchanged or returns an exact verified committed outcome. |
| Presentation | The rule and all admitted options have reliable localised names and an accurate consequence description. |

The original planning session's certified runtime pool contained **zero rows**.
This is an evidence status, not the intended shipped design.
The supplied files do not contain installed vanilla rule definitions or a demonstrated native runtime writer.
The candidate register below is the complete proposed investigation scope for this specification.
It does not mislabel unverified candidates as working rules.
The implementation must finish the exact installed-option inventory before admitting any candidate.

## Candidate register

The row codes in this table are planning identifiers.
They are not invented native rule keys.
Only a key actually found in the effective loaded definitions can become a runtime row.
Where a family contains more than one native rule, each real rule receives its own row and each changed rule consumes one batch slot.

| Planning row | Candidate family | What could make a transition meaningful now | Principal exclusion or proof requirement |
| --- | --- | --- | --- |
| R01 | War-goal justification rules | A currently existing actor and target gain or lose a valid justification route, or a verified native prerequisite changes. | Distinguish new justification, ongoing justification, existing war goals, and actual declaration. Never assume one setting controls all four. |
| R02 | Faction creation rules | At least one independent actor has a legal partner and a changed rule gate for creating a faction. | Preserve country, ideology, subject, and event-specific restrictions. A changed global label masked for every actor is ineligible. |
| R03 | Faction joining or invitation rules | A current faction and outside country have a changed invitation or joining gate. | Existing membership must have a verified disposition. Do not dissolve factions by script to manufacture an effect. |
| R04 | Guarantees | A current actor and target gain or lose the ability to create a guarantee. | Audit incoming and outgoing gates, independence, existing guarantees, and relation-specific restrictions. |
| R05 | Revocation of guarantees | A current guarantee has a changed legal revocation action. | No existing guarantee means no current witness. Cancellation of the guarantee is still a player's or AI's action. |
| R06 | Military access | A current pair has a changed access request, grant, or revocation gate. | Do not confuse permission to request access with permission to traverse territory. Preserve current treaty behaviour unless native evidence establishes a change. |
| R07 | Lend-lease | A current donor and recipient have a changed new-agreement gate under `allow_lend_lease`. | Native key and five referenced options are evidenced, but default, writer, hard-coded differences, and existing-agreement behaviour still require installed proof. Preserve bilateral arms embargoes. |
| R08 | Volunteers | A current eligible sender, recipient, and conflict have a changed volunteer permission. | Preserve independent capacity, war, ideology, and diplomatic restrictions. Prove treatment of volunteers already deployed. |
| R09 | Expeditionary forces | A current actor has an eligible force and recipient whose expeditionary action changes. | Do not substitute a volunteer rule or direct unit transfer. Admit only if a distinct native game rule actually exists. |
| R10 | Foreign political activity | A current country has a changed supported action involving ideological influence or a coup. | Split real native rules by their exact definitions. Agency, operation, and DLC conditions must be met. Do not add an idea or change a government as the result. |
| R11 | Continuing construction limits | A current legal construction opportunity changes under an actual native limit, such as a fort-level rule. | This family is held back until hard-coded runtime consumption, queued construction, and existing structures are all proven. No demolition or reimbursement is invented. |
| R12 | Country AI behaviour | An existing AI country has a reachable, uncommitted alternative branch that consumes its actual behaviour rule. | Exclude startup-random options, completed paths, human countries, missing countries, incompatible branch states, and changes that would require replaying history. |

International-market permissions or other continuing campaign systems may be considered only when the installed inventory identifies a real native rule and the same tests can be completed.
They are outside the initial admission target rather than assumed core content.
An additional candidate requires its own evidence row, meaningful transition predicates, option inventory, compatibility review, presentation, and scenario coverage.
It cannot enter through a broad catch-all runtime branch.

## Directly evidenced option references

The repository snapshot inspected for this package is `a3ef485c5da7e2337122eca04ac65c175050f251`.
The following references establish names and consumers within that snapshot.
They do not establish a native runtime writer.
Exact source links and evidence boundaries are in `104_rule_native_feasibility.md`.

### Lend-lease

`common/scripted_triggers/zz_condemnation_diplomacy_overrides.txt` reads `allow_lend_lease` in both outgoing and incoming lend-lease gates.
The referenced options are `FREE`, `LIMITED`, `SAME_IDEOLOGY`, `SAME_FACTION`, and `BLOCKED`.
The script also checks a bilateral arms embargo.
The eligibility predicate must preserve that independent restriction.

The inspected script allows both `FREE` and `LIMITED` through its own branch.
It does not prove that the engine treats them identically, because additional native conditions may distinguish them.
It also does not identify the rule's canonical default.
The complete installed definition and native consumer behaviour must resolve both points.

Useful proof scenarios include a cross-ideology pair outside the same faction, a same-ideology pair outside the same faction, a same-faction pair, and a pair blocked by an independent embargo.
A proposed `SAME_FACTION` destination must not claim to disable an agreement whose pair is already in the same faction.
A proposed `FREE` destination must not claim to overcome a separately enforced embargo.

### Country AI rules found in the repository

The sole active file in the inspected repository's `common/game_rules` directory is `chaosx_game_rules.txt`.
Its five active rule definitions are listed below.
Its introductory comment explains that these identifiers were retained to validate vanilla scripted triggers when the corresponding DLC was absent in that installation.
That compatibility purpose is not evidence that every listed option can be used in every installation.

| Native rule | Declared default | Other declared options | Required DLC on alternatives |
| --- | --- | --- | --- |
| `AFG_ai_behavior` | `DEFAULT` | `HISTORICAL`, `FASCISM`, `DEMOCRATIC`, `COMMUNIST`, `CALIPHATE`, `EMPIRE`, `MUGHALS`, `RANDOM` | Graveyard of Empires |
| `BUL_ai_behavior` | `DEFAULT` | `HISTORICAL`, `COMMUNIST`, `COMMUNIST_BALKAN_FEDERATION`, `FASCIST`, `THE_RETURN_OF_FERDINAND`, `DEMOCRATIC_SOCIALIST`, `DEMOCRATIC_LIBERAL`, `RANDOM` | Battle for the Bosporus |
| `GRE_ai_behavior` | `DEFAULT` | `HISTORICAL`, `MONARCHIST`, `MONARCHIST_ALTERNATE`, `COMMUNIST`, `COMMUNIST_ALTERNATE`, `DEMOCRATIC`, `FASCISM`, `FASCISM_ALTERNATE`, `RANDOM` | Battle for the Bosporus |
| `INS_ai_behavior` | `DEFAULT` | `TRUE_HISTORICAL`, `LOYALIST`, `REVOLUTION_DEMOCRATIC`, `REVOLUTION_UNALIGNED`, `REVOLUTION_COMMUNIST`, `RANDOM` | Thunder at Our Gates |
| `TUR_ai_behavior` | `DEFAULT` | `HISTORICAL`, `ALTERNATE_KEMALIST`, `TUR_DEMOCRATIC_KEMALIST`, `TUR_DEMOCRATIC_ALTERNATE`, `FASCISM_TUR_AI`, `TUR_FASCISM_ALTERNATE`, `COMMUNIST_TUR_AI`, `TUR_COMMUNISM_ALTERNATE`, `BALKAN_ENTENTE`, `OTTOMAN`, `RANDOM` | Battle for the Bosporus |

`RANDOM` is excluded from the proposed mid-campaign destination set unless an inspected consumer demonstrably performs a new supported random choice during play.
A startup flag chosen once is insufficient.
The other alternatives remain conditional candidates until their still-reachable route consumers and persistence are proved.
Changing an AI rule does not automatically change ideology, undo completed focuses, install a leader, or create a civil war.

## Protected and excluded settings

Chaos Redux player configuration is protected regardless of its storage format or category label.
This includes event enablement, evolution toggles, cluster participation controls, scenario controls, starting Chaos controls, timers, debug and force modes, audio and volume, interface preferences, accessibility choices, and any related configuration mechanism.
The allowlist is evaluated after this protection boundary.
A configuration setting cannot be admitted simply because it uses a game-rule definition.

Initial map fragmentation, starting borders, decolonisation performed only at startup, starting governments, historical start packages, bookmark setup, and one-time country creation are excluded.
Cosmetic names, graphical settings, music choices, purely visual focus hiding, and achievement permission switches are excluded.
Difficulty sliders and country-strength modifiers are excluded from this event's rule pool.
They are not substituted for the requested continuing rule changes.

A native rule that combines a continuing effect with a startup-only effect is admitted only if its continuing part can change safely and honestly without replaying the startup part.
The report must describe the actual continuing result.
If the only meaningful interpretation would require replaying startup, the rule is excluded.

## Registry row requirements

Each admitted row stores or generates the following development facts.
The implementation can encode them as static branches, constants, or verified data structures appropriate to the engine.
This table is a semantic contract rather than an invented script schema.

| Field | Meaning |
| --- | --- |
| Rule identity | Stable native key and stable Event 104 registry identity. |
| Effective source | Definition path, precedence, revision, and content hash. |
| Canonical default | Exact loaded default option, not a remembered label. |
| Supported options | Complete option identifiers, DLC gates, and localised-name keys. |
| Allowed transitions | Exact directed pairs supported during a running campaign. |
| Consumer family | War, faction, diplomacy, intervention, political behaviour, AI, or continuing construction. |
| Meaningfulness predicate | Current witness and all independent conditions required to demonstrate an effect. |
| Compatibility predicates | Conditions that would mask the result or make another selected transition invalid. |
| Writer and reader | Verified native mechanisms with scope and failure semantics. |
| Existing-object behaviour | Treatment of active treaties, wars, shipments, deployed forces, queued construction, and committed AI plans where relevant. |
| Fresh and revised history | Whether Rule has ever successfully changed the rule, and which destinations it has successfully used. |
| Presentation | Rule name, option names, effect direction, and affected subject if country-specific. |
| Validation fixtures | Named acceptance scenarios for first change, repeat, rejection, save/load, and multiplayer. |

No generic mapping treats native option names such as `FREE`, `ALLOWED`, `DEFAULT`, or `HISTORICAL` as universally equivalent.
The semantics belong to the individual rule and effective consumer.

## Selection model

Let `S` be the current authoritative campaign state and `r` an admitted rule.
Let `O(r)` be its admitted runtime options, `d(r)` its canonical default, and `c(r,S)` its current option.
Let `D(r,S)` contain options in `O(r)` that differ from both `d(r)` and `c(r,S)`, satisfy all content and transition gates, and make a verified meaningful difference in `S`.
A rule is a candidate only when `D(r,S)` is nonempty.

The **fresh set F** contains candidate rules never successfully changed by Event 104.
The **revision set R** contains candidate rules previously changed by Event 104.
Freshness records event provenance, not whether the native rule is default.
The current game's selected options are always read again.

Before revision permission, the selection set is `F`.
With Evolution II or IV active, it can include `F ∪ R`.
Each batch selects distinct rules without replacement.
Every selected rule gets at most one destination during that firing.
The count and Evolution IV mix are specified in Part 3.

## Ordinary random draws

For the baseline and Evolutions I through III, every rule in the currently eligible draw stratum has equal weight.
After choosing a rule, every currently valid destination for that rule has equal weight.
There is no player-country preference, winner preference, stronger-country preference, or hidden preference for a harmful outcome.

With revisions enabled, recently changed rules receive a soft respite.
Rules outside the immediately previous successful batch are drawn first whenever any such candidates remain.
Once that outside set is exhausted, still-eligible rules from the previous batch can fill remaining requested slots.
If the previous batch contains every current candidate, selection can use those candidates immediately.
This prevents an empty firing caused solely by the respite preference.
It also preserves revision behaviour in a small late-game pool.

The previous-batch record is updated only after a successful occurrence and contains only actually committed rules.
A rejected firing does not erase it.
An external rule change does not replace it.

## Compatible batches

Compatibility is checked against the state created by the already committed prefix of the batch.
After each verified transition, remaining candidate rules and destinations are reevaluated before the next draw.
This prevents a later rule from consuming a slot when an earlier change has made its entire effect irrelevant.
The event can still combine restrictive and permissive settings in different systems.
An unusual combination is not automatically incompatible.

An admitted combination must leave at least one meaningful consumer for every newly committed change at the end of the batch.
Before the next random draw, filter its prospective destination set to transitions that preserve a meaningful consumer for every existing committed row and for the new row itself.
The test is a pre-write extension predicate, so a successful irreversible write is never rejected afterward as a way of repairing an invalid combination.
Where the prospective result cannot be established safely through supported predicates, use conservative directed incompatibility exclusions between the transitions within a single firing.
They may occur in separate firings if each is independently meaningful at the time.

The initial rule order is random.
Sequential reevaluation therefore makes the final batch distribution conditional on earlier results.
The package claims exact equal probability within each current draw stratum and its prefiltered destination set.
It does not claim that every possible final combination has equal probability.
Probability validation must inspect the complete transition process and its compatibility conditions.

## Bounded execution and failure

At request start, prepare a finite ordered inventory of admitted rule identities.
At most one attempt is made for each identity during that request.
An attempted rule is removed from the request even if its application is rejected.
The loop stops when it reaches the requested success count or has exhausted the initial inventory.
Each attempted row can choose at most one currently valid destination.
No unbounded reroll loop is allowed.

An eligibility rejection can be skipped and another unattempted candidate drawn.
A write returning the unchanged native value is a failed row and may be skipped only when the writer's unchanged-state semantics are proven.
A verified successful write becomes a committed result immediately.
An unexpected or unreadable native result stops the request and blocks release of that writer or transition until investigated.
The code must never call that uncertainty a clean no-op.

### Runtime quarantine

An ambiguous or unintended native result stops all further Rule writes in that request and blocks subsequent automatic, cluster, and manual Rule mutation requests.
Retain the request identity, attempted rule, before state, intended destination, every actual readback, and the already verified successful prefix.
Store the unresolved row separately from ordinary committed transitions.
Give the unresolved row no speculative touched, novelty, achievement, or Chaos credit.
Save and reload must preserve the quarantine.
Preserve the immutable evidence, touched membership, and visited-destination facts of every prefix row that was successfully verified before the incident.
If a later unknown write masks or changes such a row, move its current disposition into incident reconciliation without erasing its earlier observed commit or relabelling it a definite no-op.
Only the still-confirmed final subset receives ordinary final occurrence credit.
Reconciliation must settle any deferred or uncredited accounting explicitly and cannot create a second award for the same observed transition.

Recheck the known prefix against the observable post-incident native state.
If at least one prefix row remains verified and meaningful, record and account for that confirmed subset once, with an explicit unresolved-incident status attached to the receipt.
The occurrence report lists only confirmed transitions and gives a restrained notice that further Rule changes are suspended pending reconciliation.
If no row remains confirmed, do not call the normal successful-firing handler.
Retain an incident receipt without claiming that the world was unchanged.
History and diagnostic ownership must keep this incident distinct from a normal empty-pool rejection.

Clearing quarantine requires an explicit verified reconciliation of native state and event provenance.
It cannot occur through another random firing, a force-mode bypass, a load callback, or an automatic restoration to defaults.
The implementation owner must document the observed state and any repair before re-enabling writes.
This exceptional path is an internal integrity condition, not a new player management interface.

The initial inventory size is the algorithm's natural finite bound.
Implementation limits must not silently cut off rows and change probabilities.
If the engine's supported loop limits are lower than the validated inventory, use an explicitly equivalent bounded representation and audit it.
The maximum successful cascade count is eight, but the registry may contain more than eight rules.

## Worked abstract fixtures

These are mathematical fixtures for the picker.
Their option letters do not assert that any native rule has the same values.

| Fixture | Current state | Valid destination result |
| --- | --- | --- |
| Binary fresh rule | Options `D, A`, default `D`, current `D`, untouched | `A` is eligible if meaningful. |
| Binary touched rule | Options `D, A`, default `D`, current `A`, touched | No destination, even with Evolution IV. |
| Custom initial setting | Options `D, A, B`, default `D`, current `A`, untouched | `B` can be selected and becomes the rule's first Event 104 change. |
| Revisable rule | Options `D, A, B`, default `D`, current `A`, touched, revision permission active | `B` can be selected if still meaningful. |
| Masked alternative | Options `D, A, B`, current `A`, but `B` changes no unmasked current consumer | No destination. |
| Restored by another system | Options `D, A`, current `D`, historically touched | Excluded before revision permission, eligible for `A` afterward if meaningful. |

For three eligible rules with respectively one, two, and four valid destinations, each rule has a one-third chance on an ordinary first draw.
Each individual destination then has probability one-third, one-sixth, or one-twelfth according to its rule's destination count.
Those probabilities follow from the proposed rule-first algorithm.
They are not measurements of a live implementation.

## Base-game completeness and pool breadth

The release pool must work without DLC.
Optional DLC-specific AI and political rules can expand variety but cannot be the sole source of meaningful revisions or cascades.
The base-game acceptance fixture must demonstrate at least eight compatible meaningful rule transitions available for a broad late-game firing and at least four revisable altered rules with valid non-default alternatives.
These are release breadth targets chosen to substantiate the specified maximum cascade and reshuffle behaviour.
Ordinary campaigns may have smaller eligible pools and use the graceful shortening rules.

If the real base-game inventory cannot meet those targets, record the precise shortfall.
Do not invent additional native rules, waive non-default destinations, grant DLC, or add a parallel policy system to reach the numbers.
The parent and user can then review an explicitly revised design.
Until that review, the full current specification remains the target and the implementation remains blocked at the affected capability.
