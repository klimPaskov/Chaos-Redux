# Frontier allocation and chain behavior

## Terms

A wave is one accepted Event 078 firing.
A pair is an unordered relationship between two current country identities.
A root is a newly allocated initial dispute in a wave.
A chain is a root that has successfully seeded Border Momentum and its sequential descendants.
A conflict is one native battle with one staging state and one disputed state.
A reservation is the exclusive right to use an endpoint for that conflict until safe release.
A spent target is a state already admitted as a disputed target in that wave.

Current country identity includes the actual country object or equivalent verified identity and a generation marker when the engine can reuse a tag.
An old tag string alone cannot authorize a future transfer.
A cosmetic name change does not create a different country.
A newly released country reusing a historical tag does not inherit a dead country's active disputes.

## Validity layers

| Layer | Required checks | What is not a blanket exclusion |
| --- | --- | --- |
| Country | Existing native participant capable of owning the endpoint and entering the mechanic | Player status, major status, ideology, ordinary army strength |
| Relationship | Distinct countries with a valid land frontier, not in a normal war against each other | A normal war against a third country |
| Endpoint | State belongs to the participant whose side it represents, current control is compatible with native battle participation, direct legal land connection exists | Capital status, high economic value, or being a core |
| Conflict | Native battle can be created and its two endpoint footprints are available | Another battle on a disjoint frontier of the same country |
| Wave | Stake not already spent by this wave, no duplicate root identity or duplicate ongoing stake | Previous resolved Event 078 participation in a different wave |
| Continuation | Same original opponents, newly adjacent target created by the last capture, valid endpoint and reservation | The existence of an unrelated normal war |

Owner and controller must both be checked.
The default candidate construction uses states owned and controlled by the corresponding side because the documented native effect identifies countries from state ownership.
A foreign-occupied state is not silently treated as a border between its controller and another country.
Any broader owner/controller arrangement needs an installed-engine fixture that proves both participation and settlement remain correct.
This restriction applies to affected states and does not disqualify all of their owner's other borders.

Do not copy a preexisting helper containing `has_war = no` or `has_border_war = no` as the country admission rule.
Existing Event 008 and resource-dispute patterns can inform scope discipline, but their single-incident gates do not implement this event's wider participation contract.
Same-faction, subject-overlord, common-overlord, non-aggression-pact, demilitarized-state, expeditionary-force, and volunteer cases belong in the native compatibility matrix.
There is no design-level diplomatic immunity beyond a direct normal war.
Do not dissolve diplomacy merely to force a failed native case to work.

## One firing, two allocation passes

First enumerate current legal land relationships and deduplicate them by canonical pair identity.
Build candidate state-front data without starting any battle during discovery.
The discovery result is a snapshot of possible relationships, not permission to skip the final live checks.

The first allocation pass gives every pair its baseline opportunity.
Pair order is shuffled using the synchronized game RNG and stable input ordering.
For each pair, remove candidates invalidated by earlier reservations, select one distinct target state uniformly, then one legal staging state uniformly.
Reserve, revalidate, and start the native battle as one controlled admission sequence.
Only a confirmed native start commits the root to history and counts toward Chaos or achievement exposure.
A failed start leaves no partial territorial result and releases only its own provisional reservations.

The second pass handles evolved extra roots.
Build a disjoint frontier-slot set for each eligible pair using seeded selection from the remaining valid endpoint graph, also counting existing compatible Event 078 fronts as occupied slots.
This is a constructed feasible set, not a claim that a runtime maximum-matching solver has found the unique largest possible set.
Its size is F.
Apply the evolution quota and allocate one extra root per pair per round until every quota is filled or no usable slot remains.

The baseline root's state sampling remains uniform over valid states.
Extra-front sampling is conditional on earlier selections and state exclusivity.
It is not represented as an unconditional uniform draw over the map.
Tie ordering and seed inputs must be recorded for reproducible tests.

A collision can make a previously discovered pair temporarily unusable.
Do not silently change its stake to an inland state, take an already occupied state, or transfer territory without a native battle.
Record the pair and the exact reason.
Do not introduce a deferred country-by-country combat queue to conceal an engine-wide concurrency limit.

## Repeated waves and overlapping work

Every new wave receives a distinct wave identity and its own spent-target set.
Existing live reservations from every source remain visible to new admission.
A baseline wave does not create another unresolved Event 078 dispute for an already active pair.
An evolved wave can create additional distinct roots when Multiple Frontiers is enabled and the pair's existing active fronts leave room inside the newly calculated frontier budget.
The new wave records only the roots it actually starts.

The total active Event 078 fronts for a pair, including older waves, consume the pair's concurrency quota for the new admission.
A lower-profile new wave does not cancel older valid battles when their existing count exceeds its quota.
It simply admits no new fronts for that pair.
The quota limits new admission and never retroactively changes declared stakes.

An evolved wave's root-admission count is cumulative.
Resolved roots still count as opportunities already consumed by that wave.
An evolution raising the quota can add only the difference between its new quota and the wave's already admitted roots, further limited by current global occupancy.
It cannot turn a recently ended conflict into a free replacement root.

Wave A resolving after wave B has started cannot claim wave B's reservation, state target, evolutionary history, or achievement record.
Country totals are summaries derived from the active records and cannot be used as an opponent pointer.

## Settlement transaction

The transaction uses the conflict identity, side, recorded country identities, both endpoint identities, and the current battle or reservation generation.
The implementation must prove how that identity reaches each result callback before enabling concurrent play.
A country-scoped callback without a conflict identity is not enough.

A terminal result performs this sequence:

1. Resolve the exact still-current conflict record and reject an already consumed or stale result.
2. Freeze its terminal status before invoking an effect capable of causing more callbacks.
3. Revalidate countries, ownership, control, direct-war status, endpoint reservations, and the correspondence with the native battle.
4. For a valid attacking victory, record the relevant pre-transfer adjacency set and transfer only the declared target.
5. Recheck the resulting ownership and mark the actual transfer receipt.
6. Update root, chain, achievement, and event-owned Chaos evidence from the confirmed result.
7. Consider the next momentum step using the updated local map.
8. Release or hand over this conflict's own reservations only when all possible native result deliveries are safe.
9. Queue participant reporting from the immutable receipt.

The attacker and defender can both receive callbacks for the same native result.
They must converge on one transaction.
A second callback may acknowledge the same receipt but cannot transfer again, roll momentum again, grant another Chaos award, or increment achievements twice.

A target already owned by the attacker at callback time is not automatically proof of an Event 078 victory.
The ownership change could have come from another system.
Without an attributable native result and a valid transaction, do not count it as a capture.

## Territorial result table

| Observed result | Target state | Staging state | Momentum |
| --- | --- | --- | --- |
| Valid attacker win | Transfer to attacker exactly once | Remains with its current legitimate owner | May seed or continue |
| Valid defender win | Retained by defender | No award | Advancing chain stops |
| Native draw | No Event 078 transfer | No award | Stops |
| Native cancellation | No Event 078 transfer | No award | Stops |
| Direct normal war starts | No Event 078 transfer after invalidation | No award | Stops |
| Third-party ownership or control invalidates battle | Do not take from third party | No award | Stops |
| Stale or duplicate callback | No new effect | No new effect | No new roll |
| Debug-forced result | Only in an isolated test fixture | Only fixture behavior | Disqualified from campaign rewards |

The old `change_state_after_war = yes` path must be replaced for this design.
Use the documented option to disable automatic transfer and perform the one-state settlement through the authoritative transaction.
Do not assume the native automatic rule is asymmetric in the way this specification requires.

## Exact momentum geography

Let S be the newly captured state and A the advancing country.
Before transfer, inspect S's directly connected land-neighbor states.
Record which of those already border any valid state of A.
After transfer, a continuation candidate T must meet all of the following conditions:

- T is still owned and validly controlled by the same original opponent.
- T directly borders S through a valid native land connection.
- T did not border A immediately before S changed ownership.
- T is now legally adjacent to A because of that capture.
- S and T can form the next native conflict and neither footprint is incompatibly reserved.
- T is not a spent target of this wave.

Select uniformly among distinct eligible T states.
Use S as the next staging state.
A different staging state is not substituted simply to keep a chain alive when S cannot legally support the next battle.
No valid T means the chain ends.

Consider a row of states A0, B1, B2, B3, where A owns A0 and B owns the others.
A capture of B1 newly exposes B2, so B2 can be the next stake.
A capture of B2 can expose B3.
By contrast, a second B state that already touched A0 before B1 fell is an old frontier and is not a momentum target from that capture.
It may be an extra root under Multiple Frontiers or a stake in another wave.

A chain has one continuing head.
Borders in Motion produces more roots and more seeded chains, not branching trees in which a single victory creates attacks against every neighboring state.
This preserves the user's advancing-until-stopped rule and keeps one victory from multiplying into an uncontrolled callback tree.

## Endurance and finite behavior

No authored chain-length cap ends a valid advance.
Its length is limited by actual military results, the geography of newly exposed states, remaining opponent territory, and the wave's spent-target set.
The event gives no recovery package between steps.
A victory that fails to open a new frontier still counts as a valid capture but does not extend the chain.

A wave closes when it has no active native conflicts, no committed immediate continuation, and no pending safe result cleanup.
Future MTTH opportunities do not keep it open.
Achievement hold checks and containment confirmation can survive as small independent receipts after the fighting wave closes.
They do not keep states reserved or permit new root admission.

## Settings and abnormal transitions

An evolution setting is checked both when a capability is considered and immediately before a new battle is created.
A disabled setting cannot be bypassed by an old delayed event.
Already active battles retain their one-state settlement contract.
A disabled momentum setting stops the chain after the current battle resolves, with no new continuation.

Country annexation, civil-war splits, releases, ownership changes, and controller changes are handled through exact identity validation.
A cosmetic flag or name change preserves a still-valid country identity.
A reused tag does not.
When safe identity cannot be established, hold the affected result for cleanup and report the technical failure without granting land.
The rest of the world's valid conflicts continue independently.
