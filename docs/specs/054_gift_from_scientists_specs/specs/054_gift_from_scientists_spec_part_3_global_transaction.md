# Event 54: Global Grant Transaction

## One bounded world transaction

Each firing resolves through one bounded transaction tied to Event 54. The event does not install daily, weekly, or monthly world scans.

The transaction begins by fixing the current recipient list and current grant intensity. It then resolves every recipient independently and ends after reports and receipts are prepared.

The event should remain safe when a country disappears, changes tag, changes owner type, completes research, or becomes incompatible during resolution.

## Transaction sequence

The world transaction follows this order:

1. Determine the highest enabled evolution stage available at the current Chaos value.
2. Set the grant target to one, three, five, or ten technologies.
3. Freeze the current valid recipient list in a stable order.
4. For each recipient, build the safe eligible pool for the current stage.
5. Draw one candidate uniformly from that pool.
6. Revalidate the candidate immediately before granting it.
7. Apply its grant profile.
8. Record the granted technology, provider, category, and safety result.
9. Remove the selected technology and every package-added technology from the temporary pool.
10. Recheck the remaining pool before the next slot.
11. Stop for that country when the target count is reached or no eligible candidate remains.
12. Prepare a consolidated report for every affected human country.
13. Record one global Event History entry and any first-use evolution or Chaos milestones.
14. Clear all temporary recipient and candidate state.

A rejected candidate does not consume a grant slot. The country rerolls from the remaining valid candidates.

## Independent country rolls

Every country starts from its own technology state and receives its own random sequence.

The process must not use a world-wide technology list with shared removal. A technology granted to France can still be granted to Brazil, Bhutan, or a civil-war country during the same firing.

The event should use a stable country order so the synchronized random sequence remains reproducible in multiplayer and debugging. Stable order does not make results identical between countries because their pools and prior draws differ.

## Without-replacement selection

A country cannot receive the same technology more than once in one firing.

The rule also covers aliases and package contents. When one selected breakthrough grants several required nodes, every granted node is treated as owned before the next draw.

A later repeat can never grant a technology that the country still owns. If another system removes a technology through a supported mechanic, it may become eligible again only after a full safety review confirms that regranting it is valid.

## Pool exhaustion

A country stops early when its safe pool is smaller than the current grant target.

Examples:

- a country with two eligible technologies during Evolution II receives both and stops
- a country with no eligible technologies receives none
- a country with ten candidates during Scientific Deluge may receive fewer than ten if a selected branch removes opposing candidates
- a grant package may reduce the remaining pool by more than one node

Pool exhaustion is a valid outcome. It should appear in the human report and debug receipt. It is never repaired by selecting an excluded technology.

## Candidate rejection

A candidate can fail its final validation because the country state changed, an owner callback declined, a prerequisite package became invalid, or an incompatibility appeared after the pool was built.

The candidate is removed from the current attempt and the country rerolls. Repeated rejection cannot create an infinite loop. Every failed candidate must leave the temporary pool for that recipient and slot.

All rejectable conditions must be resolved before mutation begins. Once an approved grant package or callback starts, its bounded effects must complete without a later rejection branch. No failed validation may leave partial owner state.

## Grant receipts

The event should keep bounded receipts long enough to build reports, test results, and achievement tracking.

Each recipient receipt records:

- the intended grant count
- the actual grant count
- the list of granted technology identities
- the player-facing names
- the provider identity for registered technologies
- whether the ordinary or expanded pool supplied each result
- whether a package was applied
- whether the pool was exhausted
- how many candidates were rejected
- the evolution stage used
- the firing sequence identity

Receipts are not a permanent public ledger. Player-facing history needs the event firing and the player's own report. Detailed receipts can be retained only where later achievements or owner callbacks need them.

## Human report handling

Each human recipient receives one report after its grants are complete.

The report should distinguish:

- full delivery
- partial delivery caused by pool exhaustion
- no compatible breakthrough
- one or more registered Chaos technologies

It should never imply that a missing grant was lost through bad luck. A missing slot means no safe technology remained.

The exact technology list should be available through scripted localization or a custom effect tooltip. Internal candidate IDs, provider IDs, rejection reasons, and safety profiles remain hidden.

A human country that is not a valid recipient receives no misleading report.

## Technology popup control

The normal individual technology-complete popup should be disabled for Event 54 grants.

The consolidated report replaces those popups. This is especially important for Evolution III, where ten technology popups would obscure the event and create multiplayer disruption.

Suppressing popups must not suppress the technology's actual unlocks, equipment access, modules, or research graph state.

## Multiplayer behavior

The global transaction runs once for the shared world state.

Every human player sees only the report for the country controlled at the time the report is delivered. A tag switch after resolution does not create a second report or expose another country's receipt.

The world transaction and random draws must be synchronized. No result may depend on local GUI state, local settings, tooltip evaluation, or unsynchronized client data.

The event adds one global pacing transaction. Human report events are presentation events and do not advance timers, add major-event weight, reduce repeatable caps, or create duplicate cluster counts.

## Save and reload behavior

A completed firing must not repeat after save and reload.

The transaction needs a short-lived sequence identity so delayed reports can prove which grant receipt they belong to. Every country may consume a given receipt once.

A save made after grants but before a player closes the report keeps the report and does not regrant technology.

A save made during an incomplete transaction should either finish from the persisted recipient and sequence state or fail closed without duplicating completed recipients. The implementation should prefer completing the bounded transaction in one effect chain so this edge case remains small.

## Country transformation behavior

When a country changes identity during the transaction, the recipient proof should follow the actual country scope only when that transformation preserves the technology state safely.

A country deleted and replaced by a new tag does not inherit an unfinished grant automatically. The new country can participate in a later firing.

Civil-war and release systems should not be interrupted. Countries inside a protected creation transaction are skipped and become eligible after their owner clears the protection.

## Owner callback behavior

An owner callback runs only for the selected registered technology and recipient.

The callback can:

- apply the minimum hidden state needed for that technology to function
- publish a player-facing technology name when the node lacks normal text
- register a bounded achievement-use hook
- record that the recipient obtained the technology through Event 54

The callback cannot:

- call the owner event
- mark the owner event fired
- advance the owner evolution
- start a country route
- create the owner character or institution
- grant the owner's normal reward package
- consume a unique owner reward
- change unrelated countries

A callback must be safe when called once and harmless when a recovery path checks it again.

## Performance boundary

The event is allowed to inspect the current country set when it fires because global distribution is its core effect. It should not create a permanent all-country on-action.

The technology pool should come from reviewed candidate data and bounded owner providers. The transaction should not scan every script file or rebuild a global source inventory at runtime.

Candidate checks can be detailed, but they run only during a firing and only for the current recipient and candidate pool.

## Debug and validation visibility

Debug output should identify:

- firing sequence
- current stage
- recipient count
- intended and actual grants by country
- pool exhaustion
- rejected candidate count and reason category
- registered provider grants
- owner callback failures
- duplicate or incompatible candidates blocked

Debug text must stay out of player-facing reports, Event Details, cluster details, and spreadsheet wording.

## Failure standard

The transaction fails closed.

A missing candidate mapping, invalid technology, missing provider, failed owner check, incompatible branch, missing DLC node, or stale registration can reduce a country's pool. It can never justify a guessed technology, a placeholder grant, a partial owner event, or a direct script error.

The global event can still finish when one country has no valid result. One bad registration must not block every other country.
