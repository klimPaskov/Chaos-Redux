# 10. Multiplayer, AI, and Edge Cases

## Single-player behavior

In a normal single-player campaign, the current human-controlled country is selected when it passes the target gates. The chain remains attached to that country.

A later console or gameplay tag switch leaves the chain on the original country. If the original country becomes AI-controlled, visits pause. When a human controls that country again, the chain resumes.

The event does not jump to the new player-controlled tag.

## Multiplayer target draw

At initial firing, every valid human-controlled country receives one equal ballot.

The target draw must be server-authoritative and deterministic for all clients. Only the selected country receives the first popup.

The Event 53 target marker, visit state, demand state, selected package, and receipts must remain synchronized across clients and save files.

## Player control changes

The chain is attached to the country scope. The current human controller of that country receives the next visit.

When no human controls the target:

- no demand popup opens
- no AI choice is made
- no automatic punishment fires
- one bounded pause recheck remains pending
- visit count and demand progression do not advance

This rule handles disconnects, observer changes, host migration, and country handoffs without giving the AI authority over the player's Event 53 choice.

## No target replacement

A player leaving the target country does not cause the event to select another player. A target country's annexation also does not create a new random player target.

The only transfer path is the proven legal-successor adapter.

## Existing terminal state

A shared `world_end` flag does not cancel the chain while the selected country still exists, remains human-controlled, and uses normal civilian systems. Event 53 visits are follow-up events, so the random-event freeze does not erase a pending visit.

Owner adapters may exclude consequences that conflict with the active terminal scenario. The selector rebuilds from the packages that remain valid. Direct Event 53 packages remain available.

A terminal scenario ends the chain only when it destroys the target country, transfers it through proven legal succession, or changes it into a scope that cannot use Event 53's ordinary demands. The terminal flag alone is not a countermeasure.

## Consequences affecting other players

A refusal consequence can affect other human countries through real owner mechanics. Examples include:

- a foreign player joining an embargo coalition
- a foreign player becoming a war participant
- an outbreak spreading across borders
- refugees reaching another country
- a breakaway state changing front lines
- a disaster creating regional effects
- intelligence exposure benefiting foreign governments

Other players do not receive the man's demand popup and do not vote on the target player's answer.

Owner-system multiplayer rules control any later decisions offered to affected foreign players.

## AI behavior

Automatic Event 53 selection targets human countries only. The event therefore needs no normal AI pay-or-refuse policy.

AI countries still need valid behavior inside borrowed consequence systems. The owning system handles:

- AI breakaway countries
- AI embargo participants
- AI civil-war actors
- AI foreign attackers
- AI disease response
- AI famine and migration actions
- AI disaster response
- AI military fracture actors

Event 53 cannot override those owner AI systems with generic choices.

## AI after human departure

The selected target does not receive an AI fallback choice while the chain is paused. This avoids an AI spending a player's carefully saved resource or accepting a random national catastrophe during a temporary disconnect.

The pause is country-local and creates no whole-world processing burden.

## Target becomes special or nonhuman

If the selected country later stops using normal civilian systems, the chain ends cleanly unless the transforming owner provides an explicit Event 53 continuation contract that remains compatible with ordinary demands.

An actual nonhuman transformation normally ends the chain. The event should not demand Political Power, manpower, Stability, or industrial access from a country whose owner has removed those systems.

The target is not transferred to another human country after this closure.

## No valid player at parent selection

If no valid player country exists, Event 53 is unavailable to the normal picker and should show `N/A` through the existing event-list behavior.

Force Trigger Mode can follow the project's standard debug behavior, but normal manual firing must not queue an event against a nonexistent target.

## No valid consequence except the guaranteed package

For every valid target, the government-paralysis package remains valid. Therefore, a correctly registered live pool never reaches zero.

If all owner adapters are disabled, blocked, or invalid, the pool contains direct Event 53 packages only. Equal selection still applies among those entries.

## Disabled source event

A disabled source event is absent from the Event 53 pool by default. The player-facing event toggle therefore suppresses the matching borrowed consequence as well as normal source-event selection.

An owner may expose a separate adapter toggle only when the settings UI names and explains that distinction. Without such an explicit control, Event 53 fails closed and respects the source event's enabled state.

Disabling the underlying owner mechanic also disables every dependent adapter.

## Disabled Event 53 evolution

A disabled evolution does not activate, log, or set its recorded state.

Later enabled evolutions can still provide their complete behavior when their threshold is met. They do not require the disabled milestone to be falsely activated.

Package registration reads the highest enabled active behavior, not an assumed uninterrupted evolution chain.

## Active consequence conflict

A package validity trigger must exclude conflicts it cannot safely reconcile.

Examples:

- a second civil war is invalid while the owner cannot support nested civil conflict
- a severe embargo is invalid while the same owner has an incompatible active embargo transaction
- a duplicate outbreak package is invalid when no new valid seed state exists
- an occupation revolt is invalid after qualifying territory disappears
- an assassination is invalid when every important character is protected or absent

An active crisis does not block unrelated valid packages.

## Target at peace or war

War status changes validity and severity, not the equal weighting rule.

At war:

- military fracture, external war, supply collapse, and War Support packages can become more severe
- foreign-war packages still require safe conflict relationships
- an existing war cannot be duplicated

At peace:

- military and diplomatic packages remain possible when their owner validates them
- War Support collapse must include a meaningful readiness or mobilisation consequence
- external-war packages can create a new conflict

## Subject and faction edge cases

A subject player can be selected when it owns valid territory and uses normal civilian systems.

War, embargo, border, and diplomatic packages must respect subject and faction relationships. A package cannot accidentally create war between a subject and its overlord when the owner cannot reconcile the relation. A breakaway package must define whether the new states leave the target's faction and subject network.

## Capital and state loss during selection

Every state-targeting adapter locks target proof before mutation. If a reserved state changes owner before the adapter commits, the adapter rejects before irreversible effects and triggers the bounded redraw.

A selected state's loss cannot redirect damage to a random replacement without rebuilding validity.

## Character death race

The assassination adapter locks one eligible character. If another effect removes that character before application, the adapter can choose another character only through its own locked candidate list and uniform target rule. If no candidate remains, it rejects before mutation.

This does not rebuild the Event 53 package pool unless the whole assassination package can no longer complete.

## Save and reload

The chain must preserve:

- selected target
- schedule state
- pause state
- visit counters
- payment and refusal counters
- evolution state
- locked demand type and amount when a popup is open
- selected consequence package during a resolving transaction
- owner receipts and delayed-job proof

Reload cannot duplicate a payment, refusal, release, stockpile debit, state strike, or scheduled visit.

## Source adapter unavailable after an update

If a save contains a package ID whose owner adapter no longer exists or has changed contract, Event 53 should clear only the stale in-progress selection, record a migration receipt, rebuild the current pool, and preserve the overall chain.

A package removed from the live registry does not remain as a ghost candidate.

## State corruption recovery

The implementation should include one owner-owned reconciliation effect that checks Event 53 invariants on startup or through an existing narrow event-system repair path.

It can repair:

- duplicate target markers by retaining the authoritative pointer target and clearing stale markers
- a missing pointer when exactly one valid target marker exists
- a stale locked demand outside a present or resolving state
- duplicate pending schedule flags
- a resolving state with a completed owner receipt

It must fail closed when two plausible targets exist and no authoritative proof survives. In that case it ends the chain and logs a debug error instead of guessing.

This reconciliation must not become a whole-world recurring scan. It should run from a bounded startup or Event 53 lifecycle entry point.
