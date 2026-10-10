# Event 104 Rule: campaign interactions and lifecycle

## One authoritative world

Each committed transition applies once to the shared native rule state, regardless of how many recipients receive its report.
The country that executes the scripted event is an execution context.
It does not own the native rule or receive an exclusive version of the result.
Human and AI countries use the same current option through the real consumers that govern them.
Newly released countries and newly relevant targets encounter the same native state without receiving a separate Rule application.

Country-specific AI rules must prove shared native authority and a country-specific consumer before admission.
Their admission also requires the named country to exist, be AI controlled, and retain a valid future choice at the time of mutation.
A later human takeover does not receive forced AI decisions from Rule.
An annexed country does not need to remain alive to preserve the event's history.

## Change future permissions at their proper boundaries

The precise disposition of existing objects belongs to each native rule's verified semantics.
Every admitted transition must document that disposition.
The default design expectation is that new actions use the new setting and completed actions remain completed.
An implementation must not assume that expectation when the installed consumer behaves differently.

| Existing campaign object | Required treatment |
| --- | --- |
| Completed treaty or territorial settlement | Keep its completed world effects. A later rule change is not a retroactive annulment. |
| Ongoing war | Continue the existing war. Rule does not create peace or cancel belligerents merely because future war permissions change. |
| Existing war goal | Preserve the object unless the actual rule itself changes its validity. Recheck declaration conditions when used. |
| Ongoing justification | Verify whether the native setting affects creation only or also progress and completion. Admit the transition only after documenting the observed behaviour. |
| Existing faction | Preserve membership and ownership. Future invitations, joining, leaving, and calls use their actual current gates. |
| Existing guarantee or military access | Preserve or update according to the verified native consumer. Never script a mass cancellation as an assumed side effect. |
| Existing lend-lease agreement | Verify continuation, editing, and new agreement behaviour separately. A new-agreement gate alone does not prove existing shipment cancellation. |
| Deployed volunteers or expeditionary forces | Verify recall and continued deployment separately from new sending permission. No direct scripted recall is added by Rule. |
| Committed AI focus or completed route | Preserve completed choices. Exclude destinations that only matter before a branch already taken. |
| Queued construction or completed fort | Require explicit installed behaviour before admitting the limit rule. Do not erase construction to demonstrate the new limit. |

## Diplomatic tasks

A diplomatic task must distinguish its goal from the action currently available to achieve it.
If a task requires an invitation, guarantee, access agreement, volunteer deployment, or other rule-governed action, it rechecks that action at task display, action selection, payment, and final execution where those stages exist.
The same effective current rule predicate must inform its tooltip, eligibility gate, and actual effect.
Rule does not make the task ignore a native restriction simply because it was created earlier.

When a changed rule blocks the task's only valid action, the owning task system marks the task blocked and explains the concrete reason through its existing presentation.
It must not silently run down a deadline and punish the player for an action the system has made impossible.
The first implementation choice is a route already accepted by that task's design, such as an alternate valid target, an existing negotiation path, or an established cancellation outcome.
If that design has no such route, the task closes neutrally for rule-caused impossibility and requires its owner to define any reoffer later.

Neutral closure removes the obsolete native mission or pending action and its callback state.
It gives no success reward, no failure penalty, and no success credit.
Unspent reservations are released.
A payment already spent on a completed intermediate action is not automatically refunded.
Only an actual refundable outstanding payment recorded by the task's own contract can be returned.
The implementation must use that system's receipts and units rather than an estimated refund.

A purely optional action can become unavailable without cancelling the entire task when another accepted route remains achievable.
The task displays the current route options and continues normally.
The event does not invent a new diplomatic minigame to handle this integration.

### Example: faction invitation task

An active task requires inviting a particular independent country into the player's faction.
A Rule transition changes the relevant global invitation condition and the target no longer qualifies.
The task immediately stops offering a payable invitation that would fail its actual execution gate.
If the task already permits another eligible target, it can offer that target through its existing route.
If the named target is essential and no legal route remains, the task closes neutrally with an explanation that the available diplomatic conditions changed.
An invitation completed before the Rule transition stays completed.

## Partition negotiations

Partition negotiations revalidate current rule-governed diplomatic actions when a proposal is opened, when a participant commits, and before the settlement is executed.
A native rule change cannot convert an unaccepted proposal into consent.
It also cannot void a completed transfer simply because the same future proposal would now be illegal.

If the negotiation's required legal action becomes unavailable before final execution, the proposal enters its owning system's blocked or invalidated state.
No new state transfer, puppet relation, war declaration, or forced faction membership is performed on the basis of the old proposal.
The system releases only its genuine pending reservations and refunds only its recorded refundable payments.
If a revised proposal is allowed by the existing design, all affected participants must evaluate the revised terms under the current rule state.

Rule does not change bargaining scores, manufacture acceptance, change participant ideology, or remove legitimate opposition to a partition.
It changes the rules that determine which real options can be attempted.
AI evaluation therefore separates legal availability from willingness to agree.

### Example: a planned intervention

A partition proposal includes an intervention that has not yet been executed.
Rule changes the permission relevant to that intervention.
The negotiation must recheck that exact future step before completing the settlement.
If the intervention is now illegal, the parent system cannot execute an equivalent direct effect to bypass the new rule while still presenting the proposal as lawful.
An existing emergency or coercive route can remain available only if it is independently part of that event's accepted design and its presentation states its own conditions.

## Warlord campaigns

Warlord campaigns use the current rules for external guarantees, support, volunteers, access, faction membership, and new wars wherever their actual actions rely on those permissions.
Existing ownership, armies, wars, and completed campaign progress persist.
Rule does not reset the campaign or reroll its participants.

A campaign route that depends on one future external action must recheck that dependency before charging a cost or promising the result.
If the route becomes impossible, use its accepted alternative, bypass, or neutral closure.
A focus already in progress must not become an endless foreign-dependent dead end.
Its owner must implement a clear completion, bypass, or cancellation disposition consistent with that focus's actual native capabilities.

AI priorities must be recalculated when a rule-governed action is evaluated.
The AI should not continue investing in a support action that is legally unavailable.
It can still pursue an available action even if another country is unlikely to accept.
Rule does not guarantee cooperation.

## Random Idea

Event 105 Random Idea changes country ideas under its own selection and repeat rules.
Event 104 changes the native game-rule option under the contracts in this package.
Their effects can coexist on the same country or relationship.

When an idea and a global game rule both influence an action, the actual engine and shared script precedence decides the effective result.
The Rule candidate's meaningfulness test must account for that precedence.
A permissive rule cannot claim to open an action that a still-active idea or relation override independently forbids.
A restrictive global rule can qualify if it changes the effective permission despite an existing idea.

If a later Random Idea occurrence masks a previously meaningful Rule result, the earlier Rule occurrence remains historically valid.
It was meaningful when committed.
Future Rule attempts reevaluate the new effective state.
Neither event silently removes the other event's idea, restores a default rule, or grants a special exemption.

No implementation of Event 105 was verified during this planning task.
Its required interaction is a future consumer contract based on the accepted companion brief.

## Rule-aware integration boundaries

The implementation must inspect the current owners of diplomatic tasks, partitions, and warlord campaigns before editing them.
The current supplied catalogs and the inspected repository do not establish a reliable complete mapping from those concepts to final event IDs and source paths.
Do not assign guessed numeric IDs merely to make an integration table look complete.

For each real consumer found, record its current source path, owner helper, action boundary, display predicate, cost or reservation record, execution gate, callback lifecycle, and neutral invalidation route.
Only the parts that actually use a changed native rule belong in the Rule integration patch.
A direct scripted effect that intentionally ignores ordinary diplomacy is not automatically governed by a game-rule option.
That distinction must be stated and reviewed for each consumer.

## Save and reload

The native selected option is the authority after loading a save.
Rule's durable state includes schema version, the monotonic request counter including rejected request IDs, touched rule identities, visited destinations, previous successful batch, evolution unlocks, and immutable occurrence results.
It also includes unresolved transaction quarantine and whichever per-recipient queue, pinned receipt, and acknowledgement state the verified delivery route uses.
Every completed native transition must agree with its recorded result at the moment of commitment.
Later external changes may legitimately make the current native value differ from an older receipt.

Load handling must not replay a committed mutation, award Chaos again, consume another occurrence, or duplicate a report already acknowledged.
An outstanding presentation request can resume from its committed receipt if the shared presentation contract supports it.
It cannot recompute its old and new values from the current world.

If a rule or option is removed by a content update, retain its historical identity and readable archived meaning where possible.
Exclude the unresolved rule from future draws.
Do not reinterpret an old numeric registry index as a different native rule.
A schema migration must map stable native identities explicitly and retain novelty history.

## Simultaneous and same-day requests

Every request has a monotonically increasing campaign identifier or an equally strong verified unique identity.
A date alone is insufficient because two human players or a cluster route can request Rule on the same game day.
Rule commits through one synchronous authoritative execution path.
The second request reads the state after the first request's committed changes.
It cannot reuse the first request's candidate snapshot or success receipt.

Each successful request owns an immutable ordered list of transitions.
Its list records actual old and new native options, first-change or revision status, witness summary, and Chaos accounting.
A deferred popup or selected history entry refers to that request's record.
It does not refer to a single mutable global last-result array.

The implementation must prove native event payload freezing or use a verified per-recipient serial delivery context that remains pinned until acknowledgement.
Later receipts can wait in the shared presentation route while current rules continue to affect gameplay.
If the engine and current shared presentation cannot preserve the report's identity, that is an integration blocker.
It is not permission to show stale or overwritten result text.

## Executor loss and player continuity

The event's durable rules and history survive annexation, capitulation, release, civil war, and a change in the execution country.
Future scheduling selects an eligible executor through the project's existing authoritative route.
It must not clear the global touched set because the previous executor disappeared.

Achievement tracking is per eligible player-country run as defined in Part 5 and the shared achievement framework.
Observer status, a later country switch, or joining an old campaign does not automatically inherit another country's challenge credit.
The implementation must resolve actual shared player identity support before promising account-level continuity.

## Player settings and restart semantics

Turning Rule off stops future normal firings through the existing event settings.
It also pauses active-system MTTH checks and new automatic evolution unlock notifications.
It does not reset native rules.
Already unlocked stages remain unlocked, and reenabling Rule resumes background checks under current conditions without catch-up or backdated progress.
Turning a stage off stops future use of that stage's capability while preserving the already changed world.
The settings text should make that persistence understandable without offering a new reset control.

A diagnostic restart or forced request receives a new request identity and retains historical provenance unless an explicitly authorised test fixture resets the entire campaign state.
An accepted forced request may use enabled unlocked stages, or the eligible pre-first-success evolved opening, without resuming background MTTH while the master event is disabled.
It cannot clear novelty records or achievement disqualifiers as an incidental cleanup step.
Release code must not use debug repair as a hidden fallback for unsupported native behaviour.

## Integration acceptance

The integration is successful when rule-governed actions show the same legal state in their ordinary UI, their cost and eligibility gates, their AI checks, and their execution effects.
Completed world outcomes remain completed.
Pending impossible tasks close or revise through explicit owned behaviour.
All saved rule and event history remains coherent across later firings and multiplayer requests.
The validation matrix names the concrete scenarios required to demonstrate these properties.
