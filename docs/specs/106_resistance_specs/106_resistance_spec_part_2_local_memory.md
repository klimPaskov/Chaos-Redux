# 106 Resistance, Part 2: Local memory and continuity

## Remember the place that changed

The immediate resistance value already carries much of the wave's aftermath. A later event can read that native value directly. A small hidden local memory supplies the additional fact that one or more recent Resistance waves actually raised resistance in this particular occupation.

That memory belongs to the state, the occupying controller's current tenure, and a proved homeland or movement relationship. It is not a national bonus that follows the occupier into new conquests. It is not a world pool that an unrelated rebel movement can spend.

The memory has one purpose: make genuine recent shocks available to the events that act in the affected territory. It cannot create countries, transfer land, add units, declare wars, or schedule another Resistance wave.

## Separate the facts

| Fact | Meaning | Later use |
| --- | --- | --- |
| Eligible state visited | The state was a valid occupation for the firing | Truthful wave counts and coverage evidence |
| Positive actual addition | Native current resistance increased in the completed write | Local support admission and this wave's aggregate Chaos calculation |
| Saturated zero addition | The state was already at the cap | Truthful reporting, with no new support credit |
| Retained local receipt | One of the bounded recent positive additions still has usable support | A matching partner can read it under its own rules |
| 095 commitment | 095 actually produced its valid armed outcome using named local support | Consumption and the relevant achievement proof |
| Containment or achievement cohort | A frozen proof set for the challenges in Part 4 | Long-term outcome checks, with no extension of uprising support |

A returned status must distinguish a fresh positive result, a capped result, an invalidated state, and a replay. A caller cannot treat all four as success and issue another reward.

## The occupation episode

An episode starts with one controller's continuous occupation of a state. A change to another controller ends that episode. If the first occupier returns later, it begins a new episode with no inherited unspent support from the earlier tenure.

Legal ownership can change while the same foreign controller remains. Annexing occupied non-core territory does not automatically end native occupation. Revalidate the native relationship and the recorded homeland. Preserve the episode only if those facts still describe the same continuous occupation. If the relationship genuinely changes, retire its old support.

The identity record contains the state, the controller, the episode generation, and the proved homeland relationship. If a partner uses a registered movement package, retain its exact stable package identity as well as its current carrier country. Event 006's inspected registry explicitly warns that carrier tag alone cannot identify a package row. Evidence item E08 covers that distinction.

The occupied homeland may be annexed or dormant. Requiring it to be a currently independent living country would lose legitimate occupations. The exact resolver for those identities is a required implementation proof.

### An unresolved movement does not block the wave

Native wave eligibility and partner movement eligibility are separate. A valid state still receives its full resistance addition when a partner cannot prove a matching claimant. Its measured addition still counts toward the truthful wave result and applicable Chaos calculation.

The unresolved binding cannot be lent to a nearby nation, a newly invented generic rebel, or a core acquired after the wave. Partner uplift requires proof that the claimed identity belonged to the affected occupation. If the implementation cannot preserve that proof, the affected binding remains an integration gap to fix. It is not an intended exclusion from worldwide native targeting.

## Three bounded support receipts

Each state episode retains at most three positive-wave support receipts. Each receipt records its wave identity, original elapsed-day timestamp, actual added percentage points, identity binding, and whether 095 has already consumed it.

Keep a separate newest-evaluated-wave watermark on the state. That watermark is replay protection, not support. It remains effective when a receipt is discarded, consumed, expired, or retired. A repeated delivery of an old wave cannot become fresh merely because its support slot is now empty.

The episode header, watermark, and fixed receipt slots are the durable local record. A single last-result diagnostic may be retained where the existing debug surface needs it. There is no growing per-state list of every historical firing.

## Time and fading

Each receipt's usable contribution fades linearly over 365 elapsed days from its original write:

`remaining contribution = actual added points × max(0, 1 - age in days / 365)`

At age zero it contributes its actual addition. At age 182.5 days it contributes half. At age 365 days it contributes zero, whether or not a cleanup callback has run.

Use the established elapsed-day clock and its verified date helpers. Do not subtract encoded game dates as if they were ordinary day counts. The current repository has targeted elapsed-day and state provenance precedents, while the exact helper usage must follow the current implementation contract. Evidence items E04 and E09 identify the inspected material.

Reading a receipt never moves its date. A wave at the cap never refreshes its date. A long-lived achievement proof never makes it recent again.

Compute fading on a new wave, a partner read, or a local lifecycle change. Expired support is already zero in the calculation. Physical cleanup can occur at those same bounded seams, with no recurring world scan.

## Admission preserves stronger existing support

On a new positive write, compare the new receipt with the remaining contributions already stored at that moment. Retain the three greatest usable unspent contributions. Ties prefer the newer wave, then the stable wave identity. An already consumed receipt yields its slot before an unspent receipt.

A small new top-up cannot evict a stronger unspent contribution and make the total current support smaller. A fourth weak receipt may therefore affect native resistance without occupying a support slot. This is intentional bounded memory.

The rule preserves the best three at admission. It does not claim to reconstruct the best three out of all discarded history at every future date. No discarded history is stored for that purpose.

For example, suppose three fresh unspent receipts contribute 75, 25, and 10 points. A real new addition of 1 point still increases native resistance, but it does not replace any of those stronger receipts. A new 30-point receipt replaces the 10-point contribution. The receipt's original amount and date remain the basis for its later fading.

The examples describe support admission in isolation. They do not imply that a state can exceed 100 resistance or receive several additions without intervening native recovery.

## Saturation and repeated waves

A state at 100 has no room for another addition. The next wave can mark it visited, but it creates no material receipt and no refresh. Current resistance still enters 095's ordinary local evaluation and the support formula when older valid receipts remain.

If native recovery lowers the state from 100 to 95, a later wave raises it to 100 and creates a receipt for 5 actual points. It does not create a 25, 50, 75, or 100-point receipt merely because that was the nominal stage amount.

Repeated positive waves can increase the sum of recent support, increase current resistance, and cross higher uprising-support bands. The state capacity, aging rule, local formula cap, and actual-addition accounting keep near-cap repeats bounded.

## Local lifecycle table

| Change | Required local disposition |
| --- | --- |
| Controller changes from A to B | Retire A's live support and start B's episode only when its occupation becomes valid |
| Controller changes A to B to A | The returning A receives a new episode, with no revived old support |
| State becomes a core of its controller | End its occupation support and invalidate the relevant continuous-occupation proofs |
| State ceases to support native occupation resistance | Treat its live local support as unusable |
| Same controller annexes the same foreign non-core occupation | Revalidate the homeland and native relationship, preserving continuity only when it remains the same occupation |
| Recorded homeland or registered movement is retired or replaced | Old support cannot be reattached to the replacement identity |
| A new country acquires a core in the state after the wave | That fact alone does not give it the earlier receipt |
| 095 or the native engine restores territory | Revalidate control and identity immediately through the actual outcome's lifecycle path |
| A recipient or report context disappears | It cannot move the underlying state support to another recipient |
| Save and reload | Preserve the original dates, episode, watermark, consumption status, and earned proof records |

The local control-change seam is particularly important because ordinary country scope changes do not rebind ROOT. The supplied event skill identifies the new controller, old controller, and changed state separately. Capture the intended actors before nested work and keep the state as the durable owner.

Current-value revalidation catches stale identities at use time. It cannot prove that a core or movement briefly changed and changed back between observations. Implementation must cover the relevant writers and lifecycle hooks for the promised continuity rules. Missing coverage remains a stated acceptance blocker, not a reason to claim continuous history from two matching snapshots.

## Read and commit contract

A partner first asks for local context for an exact state, expected occupier, expected homeland or movement, and current time. The reader returns zero usable support when any required identity is invalid, expired, mismatched, or already spent for that consumer.

The reader is read-only with respect to countries, territory, wars, and forces. It may prune locally expired bookkeeping. It never grants a gameplay outcome merely because support exists.

095 reserves the exact territory it will use and computes its final result. Immediately before commitment, it revalidates the state set and recomputes support from the surviving valid contributors. A failed or stale proposal cannot consume unrelated support.

Before its first political or military mutation, 095 freezes the validated contributing receipt identities, original dates and usable values, old occupation episode and occupier, exact homeland or movement binding, and final allowed state footprint in its own transaction frame. This frame records the final pre-mutation proof. It is not another live support bank.

Only a positive committed 095 outcome consumes the contributing receipts for 095. The outcome proof identifies the 095 transaction, canonical movement, actual territory, produced armed result, and the 106 receipt identities it used. An already-consumed return is different from a fresh successful use.

The authorized outcome may itself change control or restore territory, causing lifecycle callbacks to retire the old live episode before 095 publishes success. In that case, commit the consumed identities and earned achievement provenance from the frozen frame after physical success. Do not require the now-retired live support to pass a new post-outcome read. This does not revive that support, consume a new controller's episode, excuse a pre-commit invalidation, or turn an unrelated state change into a successful outcome. An unsuccessful transaction publishes no fresh successful-use proof.

Consumption covers every retained receipt that contributed to the committed candidate support or force uplift in an assigned state, including a receipt whose points lay beyond the formula's saturation threshold. Do not split a saturated pool into arbitrary invisible leftovers that can fund another identical armed result.

A consumed receipt can remain as bounded historical context for another legitimate owner until replacement or expiry. It cannot provide another 095 uplift. Partners do not extend its lifetime or copy it into their own unlimited support bank.

## Independent movements and overlapping claims

Different legitimate homelands can use their own affected territory during the same 095 firing. Consuming one movement's assigned support does not close a global flag that blocks all other movements.

Overlapping claims do not duplicate a state. 095's own canonical claimant rule assigns it to at most one outcome for that firing. The same state population, local force contribution, and support receipts cannot be counted twice through two tags or two registered package rows. Part 3 defines the candidate and reservation order.

Grouping occurs before any country creation. Several states supporting one homeland produce one country identity. If the country already exists, 095 must use an approved route for that existing identity rather than recreate it.

## Distinct record lifetimes

| Record | Lifetime and limit | Purpose |
| --- | --- | --- |
| Granted evolution stage | Campaign persistence, with current enable state | Future wave intensity |
| Newest-evaluated-wave watermark | Persistent replay protection | Prevent a delivered wave from being applied again |
| Local support | Three retained receipts per episode, each fading to zero at 365 days | Territorial 095 and matching partner context |
| 095 successful-use proof | Small durable consumed identity under its owner | Prevent duplicate armed outcomes and support achievement evidence |
| Chaos accounting | Global 90-day gate and +30 gross positive lifetime ceiling | Limit event-specific feedback |
| Containment proof | At most four pending credited footprints, expiring at day 300 | Two-checkpoint recovery reduction |
| Achievement proof | One immutable cohort per achievement per eligible human country | Campaign mastery and homeland recovery |

These records answer different questions. A support receipt can expire while an achievement still needs to prove what happened. Keeping that proof does not authorize another uprising bonus, another resistance write, or another Chaos award.
