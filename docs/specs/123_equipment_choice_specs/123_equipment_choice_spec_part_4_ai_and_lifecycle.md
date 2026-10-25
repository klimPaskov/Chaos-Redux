# Equipment Choice
## Part 4. National priorities and repeatable behavior

## AI uses the same opportunity

Every AI country receives the same format choices, category allowance, concrete equipment resolver, unusual-family draw, and setback rules that a human would receive in its circumstances.
It resolves a normal offer promptly through the common commitment path.
It does not need to wait for the human selection deadline.
Automatic selection for an unattended human offer uses the same resolver.

Eligibility is evaluated before preference.
A category with no legal stockpile grant, valid finished design, compatible consumer or honest permitted reserve use is excluded.
Positive preference cannot restore an excluded category.
The special-country classifier, ideology, major status, and human control are not preference shortcuts.

## Need and practical use

Evaluate the selected manifest against each recipient's actual military needs.
Use the group's primary equipment family as its anchor and include ordinary supplements when checking whether a package is materially usable.
The implementation must declare how the current engine variables measure each input.
A cached offer snapshot is sufficient for size and initial preference.
The delivery preflight still validates live legality.

| Need value N | Evidence |
| --- | --- |
| 4 | A compatible fielded family has an equipment deficit of at least 25% of its verified target demand |
| 3 | A compatible fielded family has a deficit of at least 10% and strictly less than 25% |
| 2 | A smaller positive fielded deficit exists, or useful reserves are below 25% of verified target equipment demand |
| 1 | A valid existing consumer has less than one target-demand equivalent in reserve, or a documented force plan can use the package with present manpower, fuel, supply, and training access |
| 0 | The category is an honest longer-term reserve, a saturated category, or a new force without a concrete current use |

Choose the highest applicable N before evaluating the remaining score factors.

Demand, stockpile, fielded quantity, and equipment deficit are separate facts.
Land equipment uses verified army target and fielded quantities.
Aircraft require a verified wing or air-role target and actual deployed aircraft of that role.
Maritime logistics uses verified operational convoy demand and assigned shipping, with reserve convoys as stock.
Do not apply an army-equipment target query to aircraft or convoys and call that a useful domain assessment.
A domain whose demand query remains unavailable receives only the lower need supported by a concrete sustainable plan or permitted reserve use, with the measurement limit stated in developer evidence.
Where an input is unavailable, declare it unknown and avoid assigning an emergency need level from a proxy such as division count.
Reserve-only profiles remain possible, with their limited purpose shown honestly.

For each legal category, calculate the following planning score:

`S = max(1, 10 + 30 N + 15 F + 10 W + 10 L + 20 V - 40 G - 25 H - 20 T - 15 Q)`

F is one when the primary family is already fielded in a compatible force.
W is one when its role addresses a verified current wartime requirement.
L is one for a transport or maritime profile addressing an actual logistics-equipment shortfall.
V is one when an existing owner-supported unusual family fills a concrete capability gap that the recipient can presently sustain.
For example, a verified zero-manpower robot consumer can receive V when manpower prevents a useful conventional expansion.
V cannot be awarded solely because a family is unusual.
G is one for a material fuel gap affecting that profile.
H is one for a material recruitment-manpower gap.
T is one when a single-category reference projection would add a severe ordinary handling load.
For an evolved offer, use the frozen concentrated manifest at 3 B for this reference projection.
At baseline, T is zero because ordinary overload is inactive.
Rank categories once using that common reference, then evaluate the chosen pair's format-specific loads in the format policy.
Do not rescore T from a format that is itself being selected by those scores.
Q is one when the same group appeared among the recipient's previous two chosen natural packages and N is at most one.

All flags are zero or one.
These are planned score inputs, not claimed native AI probabilities.
Calculate the score for every legal category.
A currently useful manifest has N of at least one and either an existing compatible operational consumer with a present reinforcement, deployment, or reserve need, or a verified sustainable force plan with present manpower, fuel, supply, and training access.
Use the same current-use fact shown in the manifest, evaluated alongside N from the same scoring snapshot.
An unusual manifest without that current use can remain a legal reserve only through its documented permitted-reserve contract.
While any currently useful conventional manifest remains among the unselected choices, defer reserve-only unusual manifests from the AI's preference comparison.
This is an explicit preference filter. Human legality, family weights, frozen cargo, and the score formula remain unchanged.
When no currently useful conventional choice remains, restore every legal reserve candidate to that comparison.
Choose the highest score among the remaining preference candidates deterministically.
Resolve exact ties by the greater verified deficit fraction of the primary family's target demand, then lower projected handling load, then a stable category order: infantry, fire support, mobility, aircraft, maritime, unusual.
Unknown or zero target demand cannot outrank a verified positive deficit fraction.
When neither category has a verified positive fraction, continue to the handling comparison.
Raw rifle and aircraft counts are never compared as the same tie metric.
Never use a numeric sentinel that can reject the first legal candidate.
An empty legal pool preserves an unresolved entitlement and records the missing contract.
It cannot award successful-delivery state.

Existing compatible formations use the new stock through normal reinforcement.
For a new unusual force, N=1 from a force plan or V=1 requires a verified AI template-adoption and normal recruitment path, in addition to material, manpower, supply, and training access.
Template existence alone cannot prove that path.
Any bounded adaptation must keep ordinary recruitment costs and stop when its intended finite force or stock condition is met.
The event does not spawn an AI-only free formation.

## Delivery-format choice

At baseline, choose the highest-scoring category.
For an evolved offer, apply the reserve preference filter first, then compare the two best distinct remaining preference candidates.

1. Choose concentrated delivery when only one of the top two categories has N of at least three, when fewer than two preference candidates remain, or when both top categories have N at most one.
The count in this rule uses only the selected top pair, so an unused third category cannot change their delivery format.
2. When the two best categories both have N of at least three, choose combined immediate if its projected R is at most 1.5.
3. During war, also allow combined immediate when both categories have N of four and projected R is at most three.
4. Otherwise choose combined staged when the top two categories both have N of at least two.
5. Use concentrated delivery for the remaining cases.

After a human commits the first combined category, automatic completion evaluates the remaining distinct legal categories.
Apply the same reserve preference filter to those remaining choices.
It cannot replace the human's first selection merely because another category now scores higher.
Where legality changed, the same explicit correction rules as a manual selection apply.

The score resolver and format policy are the reference behavior.
Native decision priority is not a substitute for evaluating this complete opportunity.
The implementation may call the common resolver from a recipient-rooted hidden event and use ordinary decisions for the human surface.
Both routes consume the same entitlement and the same quoted material.

## Named score scenarios

The following complete category vectors isolate the planned arithmetic.
Each numeric cell gives the finished score after the stated factors and before the reserve preference filter.
A dash means the category is ineligible.
They are design fixtures for a source calculation, not observed campaign outcomes.

| Scenario | Infantry | Fire support | Mobility | Aircraft | Maritime | Unusual | Expected category priority |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Land army with severe rifle deficit | 155 | 125 | 105 | 65 | Excluded | 10 | Infantry first, fire support second |
| Peacetime maritime shortage | 25 | 55 | 65 | 55 | 155 | 10 | Maritime first |
| Wartime air emergency | 95 | 95 | 125 | 155 | 65 | 50 | Aircraft first, mobility second |
| Saturated conventional reserves with a viable unusual force plan | 10 | 10 | 10 | 10 | Excluded | 60 | Unusual first |
| Sole legal support-reserve profile | 1 | Excluded | Excluded | Excluded | Excluded | Excluded | That legal profile, never an absent first option |

Scenario factor definitions and boundary calculations belong in the validation record.
Check ties, N thresholds just below and at 10% and 25%, unknown demand, zero target demand, severe handling, no fuel, and manpower-free versus manpower-consuming families.
The pool-weight audit separately covers unusual-family selection, setback probability, and evolution timing.
Do not normalize these category scores into percentages.
Also check a useful conventional plan with N=1, T=1, Q=1 and all other flags zero, scoring five, against a reserve-only unusual manifest with N=0 and all flags zero, scoring ten.
The conventional plan must be selected because the unusual reserve is deferred by the explicit preference rule.

## From the global firing to national receipts

One global firing snapshots the active recipient identities and its evolution profile.
It creates one event-history entry and one repeatable-event accounting action through the shared dispatcher.
It then publishes one independent national entitlement per captured identity.
The global entry remains actorless because the event has no single receiving country.
Country-specific payloads identify their own recipient explicitly.

Changing country scope does not automatically change the engine's ROOT contract.
The implementation passes an explicit recipient to helpers or uses recipient-rooted hidden event relays where the called helper requires ROOT.
All normal routes, cluster routes, manual tests, automatic selections, and staged deliveries eventually reach the same narrow national grant transaction.
Reports and log details never call that transaction as a side effect of being viewed.

| National state | What can happen | What persists |
| --- | --- | --- |
| Offered | Format selection where applicable, then one or two category selections | Frozen allowance, all manifests, family draw, stage, recipient identity, deadline |
| Committed | Immediate delivery begins, or both staged consignments are scheduled | Exact selected rows and quantities, random setback result, consumption receipt |
| Partly delivered | Only missing rows or the scheduled second consignment can arrive | Per-row actual amounts, original consignment dates, unresolved remainder |
| Delivered | Receipt and achievements can use completed material proof | Final amounts, country identity, natural or manual origin, selected groups |
| Closed | Transient selection state is cleared | Compact historical receipt and any still-live bounded achievement or handling state |
| Recipient ended | Pending work is cancelled for that identity | Historical actual delivery remains, new tag incarnations receive no inherited entitlement |

Opening or cancelling a report is not a transition that consumes the offer.
A visible confirmation keeps its immutable quote receipt until its after-block closes.
Expiry and later offers may queue work, but cannot replace that receipt or auto-grant the same entitlement concurrently.
A duplicated commitment or a delayed callback must observe the already-consumed receipt and leave stock unchanged.
A receipt from a previous firing cannot authorize a new grant.

## Changes while an offer is open

A political change or cosmetic tag change with the same country identity keeps the offer.
A civil-war split leaves the original entitlement with its captured recipient identity.
A new participant receives its own entitlement at the next global firing.
It does not clone the parent's pending offer or handling history.
Existing stock partitions through ordinary engine behavior.

A port or airbase loss invalidates only the affected deployment claim.
A still-legal reserve profile may remain if its future use is documented and disclosed.
A lost consumer permission cannot be restored through a broad technology grant.
An evolution toggle changes future offer creation and does not mutate an already committed delivery.

A manual or forced firing is visibly identified in developer evidence and carries its origin through every national and delayed receipt.
It cannot become natural through retargeting, a country relay, an automatic selection, or a later callback.
This origin determines achievement eligibility.
Ordinary physical consequences and the finite guarded Chaos map still use actual material proof.

## Bounded processing and save persistence

Persist the exact current state before scheduling later work.
Selection, staged arrival, expiry, and cleanup callbacks must all survive save and reload without resampling or duplicating stock.
Use bounded work over the captured recipient and entitlement records.
Preserve unvisited work when a batch reaches its limit.
Remove completed records after traversal or through a safe separate cleanup pass.

No recurring whole-world scan is needed for this event.
The worldwide distribution happens once per firing. It requires explicit user permission under AGENTS section 1, rule 8, before implementation, and the import review keeps that permission open.
Country-owned delayed callbacks and existing shared event or evolution hooks handle later work.
Every helper's temporary outputs are initialized by its caller, especially across nested grants and foreach loops.
Reentrant work must preserve the recipient, firing, consignment, and current-row identity before another helper can overwrite scratch state.

## Clusters and repeatability

Sudden Abundance is cluster 15 and Military Preparation is cluster 18.
The selected member role for Equipment Choice is optional, with a 100% participation chance when enabled and eligible, Medium display severity, and minimum runtime tier zero corresponding to proposed Chaos level 1.
A cluster can therefore include one universal Equipment Choice wave without making the entire cluster depend on it.
The same root/member transaction key deduplicates it when it is encountered twice.

Keep the existing Sudden Abundance repeatable lifecycle and its 120-day runtime cooldown.
Military Preparation needs its first actual runtime registration at the inspected revision.
Adopt a 120-day cooldown for that repeatable cluster as the initial parent-selected planning value, aligned with the equivalent abundance cluster and its existing Chaos-level-1 catalog identity.
This is a new design decision, not a claim that the missing runtime row already exists.
Add only the accepted Event 123 membership in the implementation and preserve the catalog's other members for their own registered eligibility and rework status.

The cluster counts once for shared pacing.
Equipment Choice still records its own fired count and repeatable-weight change once under the existing dispatcher contract.
National choices and staged arrivals add no pacing events.
Use the project's shared ordinary repeatable-event starting weight, cap reduction, and recovery rules.
The shipment system adds no separate event-frequency boost.
