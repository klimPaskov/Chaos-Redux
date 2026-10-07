# Implementation contracts and integration order

This is a future coding handoff, not a shipped implementation. All native operations below are semantic contracts until the capability matrix is resolved. The specification parts contain the accepted gameplay design.

## 1. Establish the native backend before broad wiring

Resolve C01 through C07 with current installed documentation, the required offline wiki, and actual vanilla examples. Separate four operations: reading C(A,B), adding to C(A,B), applying legitimate occupied-state compliance, and creating a native collaboration government. Prove the direction of each operation independently.

The existing `add_collaboration` call is evidence of an older intended effect, not proof that the current API accepts all country types or DLC combinations. Do not write speculative argument blocks and declare them validated because a generic brace checker passes.

Establish a readback method for actual change and a native validity predicate. If the effect clamps internally, read back the result rather than claiming the requested amount was added. If clamping must be done explicitly, prove both units and cap first.

## 2. Global firing transaction

Retain `chaosx.nr97.1` as the inspected hidden entry identity unless current consumers require a documented migration. The normal transaction should have these stages:

```text
validate shared availability and firing identity
  -> snapshot political countries and active capabilities
  -> read relevant directed values and requested grants
  -> apply each valid directed grant once
  -> record actual gains and distinct target threshold crossings
  -> finish one shared repeatable occurrence and one direct Chaos impact
  -> dispatch informational reports
```

An immutable firing identity distinguishes duplicate delivery from a legitimate later firing. Two genuinely separate timer firings in one game tick must not be collapsed merely because the date is equal. Conversely, several recipients of one manifestation must not create several transactions.

The global matrix is native state. Do not store a second persistent N-by-N matrix in event variables. A temporary snapshot for one firing is permitted. At most N times (N minus 1) directed pairs exist for N countries, excluding self-pairs. This is a bounded event operation, not a periodic background task.

Before applying any effect, fix sponsor, target, and event-generation context explicitly. Deep nested `PREV` assumptions are insufficient. Revalidate existence and native support before writing a pair whose country could have been removed by another synchronous consequence.

Record success based on actual native changes. A wholly capped pair is not an application failure. An unsupported pair is a distinct capability failure that must be surfaced rather than silently counted as success.

## 3. Shared framework transaction ownership

Resolve actual root registration, category arrays, event details, cluster membership, repeat recovery, evolution settings, and logging by reading their current implementation. Do not invent a parallel event selector.

The Intelligence cluster currently needs a lifecycle correction. Keep the repeatable event's recovery and each fire-once sibling's exhaustion independent. The ordinary recovery maximum is halved after an occurrence, not permanently fixed at 1,000. Use the existing recovery mechanism and verify the event's immediate post-fire weight against current source.

A shared pre-fire logger may run before the hidden event's immediate block. Prepare an actorless manifestation context at the proper upstream point. Do not fabricate an actor because a human timer happened to select the event. Actor-specific incident history needs the actual sponsor and target.

Set the shared evolution context before its gate, including the event identity, type, stage, and whether an actor exists. Live evolution activation and pre-evolved first activation must converge on one capability calculation, not two sets of grants.

## 4. Minimal persistent receipts

Persist only facts that the native system does not already own and that are required to prevent repeat effects or prove achievements:

| Receipt | Key | Lifetime and purpose |
| --- | --- | --- |
| Global delivery | Genuine firing identity | Prevent replay, preserve separate legitimate occurrences |
| Administrative offer | Sponsor identity, defeated political identity, state | Highest offered F, not a copy of current compliance or collaboration |
| Fifth Column stages | Sponsor identity, target identity | Stage resolution and actual positive award, first-stage time, generation |
| Government readiness | Sponsor identity, defeated identity | One readiness offer, territory snapshot, result and created native identity when applicable |
| Achievement observation | Achievement and relevant identity/cohort | Actual preconditions, immutable cohorts, deadlines and resets |

These are sparse histories for actual interactions. They are not a global second collaboration matrix or a player-facing administration resource.

Country identity must follow a documented native/project identity convention. Cosmetic renaming never resets it. Release, annexation, restoration, and civil-war identity changes must be explicitly mapped before anti-farming is considered complete. Do not assume raw dynamic tag reuse is a stable political identity.

## 5. Administration transaction

Read the real new controller, previous controller, and state from the verified callback. The supplied guide describes `on_state_control_changed` roles as ROOT new controller, FROM old controller, and FROM.FROM state, but the installed game reference must confirm this before code relies on it.

Resolve one actual target polity for the occupation. Require hostile acquisition or a valid one-time activation review, target homeland, non-core status for the sponsor, and supported native compliance. A peaceful allied transfer is not a new hostile capture.

On the first qualifying offer, use `max(current compliance, F)` and record F even if no increase occurs. On a later higher offer, use the lesser of the new F and current compliance plus the newly offered difference, preserving any current value already above F. Mark the actual result for achievement credit.

Read native post-capitulation conversion before applying any subsequent event-owned handover. Do not subtract native compliance to enforce an event balance ceiling. Distinguish native conversion from the event's spent offer.

Relevant callbacks, activation reviews, and normal firings can schedule bounded evaluation of affected occupation tuples. Do not add a world-wide compliance maintenance pulse.

## 6. Fifth Column transaction and threshold changes

Resolve the actual P and T read path first. Snapshot B's P and T and all relevant sponsors' eligibility for one incident. Commit each sponsor's independent award once, using native clamps. Verify that the engine can complete the eligible incident batch before native capitulation resolution changes the meaning of later awards. If an effect resolves capitulation synchronously and prevents that behavior, report the ordering conflict and obtain a design decision. Do not claim atomic native behavior without proof. Do not let iteration order create additional same-incident eligibility.

The first and second stages are separate. The second cannot run earlier than five actual days after the first. At execution, recheck settings, existence, war, target capitulation, foothold, C, P, T, and stage resolution. A failed recheck leaves an unused opportunity where the specification permits later eligibility, without repeatedly emitting warnings.

Only register ongoing work for actual active fronts or pending stage opportunities. Material changes in territorial progress, native threshold modifiers, collaboration, war membership, or country status must invalidate the relevant assessment. If no authoritative callback covers a material native change, resolve that observer gap explicitly. Do not claim perfect detection from only state-control changes.

A bounded active-front evaluator can be considered only under the project's scheduler rules and with a measured scope. It must never become a daily or weekly iteration of the entire world's directed country matrix. Document worst-case active-front size and evaluate save/load cleanup.

Compare threshold boundaries using the installed engine's verified numeric precision and a safe integer/fixed-point or equivalent comparison. The Python model found a binary-float exact-boundary failure, so do not casually divide and round a ratio at 75% or 90%. This is a numeric implementation requirement, not proof about native HOI4 rounding.

Use the established time conversion helper for custom date arithmetic. The supplied guide uses encoded hours and days and names `chaosx_convert_days_to_date_offset`. Do not add raw day counts directly to `global.date`. Prefer a verified native day delay where that is the correct pattern.

## 7. Government transaction

Resolve the native government's state bundle, Q requirement, creation route, identity, and sponsor relationship. Preserve native eligibility before Evolution IV. Create no substitute subject type.

At a qualified defeat, use a verified pre-defeat C snapshot for the 60-point requirement. A native conversion or consumption must not erase that eligibility. Then take the territorial and compliance readiness snapshot after native occupation conversion and current territorial settlement. The activation review may use a valid current C value or an actually recorded pre-defeat value, never a reconstruction from later compliance. Raise only eligible sponsor-held states as needed. Record the offer even if native conversion already supplied readiness.

A readiness notice stores no authority to take land later. The actual creation action re-resolves the native territorial bundle, relationship, political identity, and settings. Invalid or changed states cannot be pulled back into the old bundle through cached references.

For democracy, prove a narrowly scoped native exception. Do not replace the entire country rule set, enable unrelated puppeting, use a temporary ideology change, or overwrite another system's rule changes when cleaning up an exception. Where the native engine cannot provide an isolated route, return C05 as blocked with exact evidence.

Observe actual native subject creation and route the shared puppet Chaos source exactly once. An offer, a compliance write, and a created government are three different facts.

## 8. Temporary values and helper boundaries

Use the project's public helper convention and actual live schema. Public helpers normally use their established `= yes` form with explicit input variables unless a documented meta-effect contract says otherwise. Do not invent named-parameter syntax.

Initialize caller-owned temporary outputs before calling any helper, including outputs forwarded to nested helpers. Document scope, input values, output values, reset behavior, and native identity ownership. Use constants and integer/fixed-point conventions according to the supplied dynamic helper guides and current installed documentation.

Avoid hand-writing unsupported relational operators in Clausewitz from mathematical notation in the design. Read the installed trigger syntax and compile/test the actual forms.

## 9. Achievement observers

A1 requires prewar snapshots. A2 requires a fixed five-state cohort with continuous thresholds. A3 requires an actual positive breakthrough and two deadlines. A4 requires actual native government identities and current relationships. A5 and A6 require authoritative external event receipts, not narrative inference.

Continuous conditions must be observable throughout the interval. If a relevant native compliance, resistance, or relationship change has no callback, use only a permitted bounded cohort monitor and report the remaining temporal resolution limitation. A start/end-only test does not prove an unbroken 180-day interval.

Do not backfill missing history by inspecting the present map. Reject replayed callbacks and maintain stable cohorts across save/load. Completed status is owned by the shared achievement framework.

## 10. Safe implementation sequence

Resolve the native backend and its blockers first. Then implement one global baseline transaction and the shared registration correction. Add repeat and evolution controls, early administration, Fifth Column, and native government readiness in that order. Wire connected systems only after their contracts are available. Integrate presentation, AI, Chaos, and achievements against actual results rather than optimistic event messages.

Complete the required source/MCP checks, independent audits, and asset processing before requesting user-run live-game evidence. No automatic game launch, bench launch, broad repository cleanup, unrelated skill edits, or CSV rewriting belongs to this handoff.
