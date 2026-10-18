# 106 Resistance: Complete specification

This reading copy combines the six canonical numbered parts. Edit those source parts and regenerate this file after changes. Implementation prompts, evidence, and review records remain separate files in the package.

# 106 Resistance, Part 1: The worldwide wave

## The crisis

Occupied communities across the world begin resisting at the same moment. The change reaches a distant colony, a newly conquered border region, and an annexed homeland through the same rule. The occupier's size, ideology, faction, subject status, and human or AI control do not change the immediate addition.

Resistance puts pressure on the occupations that the campaign actually contains. An empire with many occupied states has more places to secure. A small country that has just conquered one foreign state still receives the full local shock. A country controlling only its own cores experiences the event through the wider world and any consequences for its allies or enemies.

The player manages the aftermath through the occupation systems already in use. Rising native resistance can worsen partisan activity, sabotage, and garrison losses. Later events can turn the same local conditions into political change. Event 106 itself applies the resistance wave. Occupation Revolt owns the scripted uprising response described in Part 3.

## Event identity

| Field | Required value |
| --- | --- |
| Event ID | 106 |
| Event name | Resistance |
| Event type | Minor Repeatable |
| Catalog status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Domestic Unrest |
| Cluster member severity | Low |
| Event slug | `resistance` |

These are the current user-defined values. The conflicting supplied catalog rows are reconciled separately in the evidence and decisions file. They do not change this design.

## One activation, one worldwide addition

At the start of a logical firing, determine the highest active evolution and freeze its addition for the whole wave. Visit the occupied states that exist at that moment. Apply the addition once to each valid state, including territory controlled by AI minors, majors, subjects, human countries, and valid unusual or newly created controllers.

For a state with current resistance `R` and the wave's addition `A`, the result is:

`new resistance = min(100, R + A)`

`actual addition = new resistance - R`

All values in this design are percentage points on the player-facing 0 to 100 resistance scale. A baseline wave takes 25% resistance to 50%. It does not multiply 25% by 1.25, set every state to 25%, or change only the resistance target.

The direct addition happens before the public report can be acknowledged. The report's option acknowledges a completed event. It has no second application of the wave. A multiplayer client, an AI notification, or a reopened history entry cannot apply it again.

The logical firing uses one authoritative execution. If a real control or eligibility change occurs during resolution, the state must be revalidated immediately before its write. One state still receives at most one write for this firing. A stale country pointer must not redirect the addition into another state or cancel the remaining valid states.

## Which states are occupied for this event

The semantic target is a land state that can carry native occupation resistance against its current foreign controller under the active game rules. It needs a valid current state controller and an eligible native occupation relationship. It must not be a core of that controller. The occupied homeland may be dormant or annexed. A successful claimant lookup by a partner event is not required for the native wave.

The implementation must demonstrate this predicate against the installed game's occupation rules. The inspected reference material does not establish a complete exact trigger combination, particularly for resistance at zero. That technical gap cannot be resolved by narrowing the design. See evidence items E04 and E05.

| Campaign situation | Required result |
| --- | --- |
| Enemy non-core state under wartime control | Affected when native occupation resistance is valid |
| Annexed foreign non-core state whose owner and controller are the same country | Affected when native occupation resistance is valid |
| A valid occupied state currently at 0% resistance | Affected by the full addition |
| A valid occupied state with high compliance or a well supplied garrison | Affected by the same immediate addition |
| A valid occupied state already at 100% resistance | Visited and left at 100%, with actual addition zero |
| A subject occupying a foreign non-core state | Affected under that subject's own state controller identity |
| An overlord that merely has political authority over a subject's territory | Receives no duplicate write on the subject's behalf |
| Controller's core state, including a reconquered homeland core | Outside the occupation target set |
| Mixed province control inside a state | Uses the authoritative state controller and the verified native state rule |
| A state with an absent controller or no valid native occupation resistance relationship | Skipped without creating a political identity or resistance system |
| Occupation created after the completed wave | First becomes eligible for the next firing |

Neither `owner differs from controller` nor `resistance is currently nonzero` is sufficient as the event's selector. The first loses annexed non-core occupations. The second loses pacified occupations that the user explicitly intends later waves to disturb.

There is no country rank, ideology, faction, geography, or human-control filter. A shared classifier may help validate a controller, but it cannot invent an exemption for a valid occupation.

## Resistance and resistance target

The wave adds current resistance immediately. Existing resistance targets, growth and decay rules, occupation laws, compliance, garrison supply, and intelligence effects remain the causes of later native movement.

For example, a state at 10% resistance with a low resistance target reaches 35% in the baseline wave. It may then begin moving back toward its target under the game's normal rules. That later recovery is a meaningful consequence of good occupation control. It does not reduce the required immediate write.

Do not compensate for the wave with an automatic compliance grant, a scripted immediate resistance reduction, a blanket occupation-law change, or a temporary target modifier. Such compensation would obscure the event's central effect and weaken the connection to later uprisings.

## Evolutions

The event has one intensity track with three stages. The names below are supplied by the user. All additional explanatory text remains a localisation direction until implementation.

| Highest active stage | Chaos requirement for activation | Addition on future firings | Opening at 0% resistance |
| --- | ---: | ---: | ---: |
| Baseline | 0+ | +25 percentage points | 25% |
| I: Rising Resistance | 200+ | +50 percentage points | 50% |
| II: Mass Resistance | 400+ | +75 percentage points | 75% |
| III: Total Resistance | 600+ | +100 percentage points | 100% |

Reaching an eligible threshold grants the corresponding stage through the event's evolution registration. A pre-fire check catches up any qualifying stages before the first or a later firing. This is the planning skill's instantaneous opening-intensity case. It does not introduce an MTTH wait before the stated amount becomes available.

Stage activation changes future wave strength and its recorded evolution history. It adds no resistance and no Chaos by itself. Existing resistance, completed wave receipts, and earlier reports retain their original values.

Only the highest active stage supplies `A`. At Stage III a state at zero gains 100 points once. It does not receive 25 + 50 + 75 + 100, and activation of three stages does not produce three waves.

### Persistence and settings

The following persistence rule is a parent-selected expansion of the brief, whose wording does not specify what happens when Chaos later falls.

A granted stage remains unlocked for that campaign. Falling Chaos alone does not remove it. The active stage is the highest granted stage that is currently enabled through the existing evolution controls. If all granted stages are disabled, future firings use the baseline. Disabling a stage does not undo past resistance or erase its historical activation.

A disabled ungranted stage is not granted or logged while disabled. Once enabled, it can be granted when the current Chaos requirement is met. A previously granted stage becomes available again when enabled, without a new activation record or a wave. A higher stage may activate at its own threshold even when a lower stage is disabled.

When Chaos jumps over several thresholds, record each newly granted eligible stage once through the shared history contract. Use the actual grant date. Do not fabricate earlier activation dates. The wave then uses the highest active stage once.

### Sampling and feedback order

Before starting a new wave, complete any still-unobserved containment or achievement checkpoints due at that exact elapsed-day boundary under Part 4's finite scheduling contract. This order is the same whether the ordinary callback or the wave's pre-write check reaches the due record first. Then resolve the wave's stage and native writes. A missed earlier checkpoint is not a due observation that can be reconstructed now.

Resolve stage grants and freeze the active addition before changing any state's resistance and before awarding this wave's Chaos gain. Every state in a wave receives the same nominal addition. If the wave's own consequences push Chaos across the next threshold, the new stage affects the next firing.

For a fresh campaign with no previous stage grants, a baseline firing beginning at 199 Chaos adds 25 points. If its accepted Chaos gain takes the world beyond 200, Stage I may then activate, but the completed wave stays at 25 points. A first firing at 600 Chaos starts at Stage III and adds 100 points.

## Arithmetic examples

| Resistance before | Baseline +25 | Stage I +50 | Stage II +75 | Stage III +100 |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 25 | 50 | 75 | 100 |
| 10 | 35 | 60 | 85 | 100 |
| 24.5 | 49.5 | 74.5 | 99.5 | 100 |
| 25 | 50 | 75 | 100 | 100 |
| 50 | 75 | 100 | 100 | 100 |
| 75 | 100 | 100 | 100 | 100 |
| 90 | 100 | 100 | 100 | 100 |
| 100 | 100 | 100 | 100 | 100 |

The decimal example is a design oracle for supported native precision. Implementation must verify the engine scale and observed precision rather than introducing rounding to match a guessed token convention.

## Repetition follows the map

Each later firing rebuilds the eligible set from current occupations. It never replays a cached list of countries or states.

A state can move from 0 to 25 to 50 through two baseline waves. If occupation measures later reduce it to 15, another baseline wave takes it to 40. A territory conquered after those waves joins the next wave at its own current value. A state restored to its controller's cores or otherwise removed from native occupation is no longer a target.

A wave at 100% leaves the state at 100%. It may still appear in a truthful count of eligible occupations. It does not create a positive addition, a new material-wave receipt, or another force bonus for Occupation Revolt. Native resistance at 100 remains a strong live input to that event's ordinary local evaluation.

## Firing and report cases

Natural selection should require at least one valid occupied state. This gate includes valid states at zero resistance and at the cap. The shared repeatable selection and cluster systems determine when a firing occurs. Event 106 adds no separate automatic recurrence schedule.

A supported direct invocation with an empty target set completes once as an empty result. It creates no replacement target, no extra resistance, no Chaos gain, and no local interaction receipt. The shared firing history records the invocation truthfully. The implementation must not secretly turn this into the dormant-claimant behavior of another event.

One world history entry represents one firing. Human recipients see the ordinary report appropriate to their situation. An occupier's report can describe the effects in its controlled occupations. A dispossessed country can receive the occupied-homeland viewpoint only when that relationship is valid. Other recipients receive the worldwide observer viewpoint. These variants change presentation, not the wave's mechanics.

The moment of the wave remains clear in every case. A report should distinguish the nominal addition from saturation, and should not claim that every eligible state increased when some were already at 100%.

## What the event sets in motion

The useful uncertainty is what happens after the immediate surge. A well supplied occupation can bring resistance down. A stretched empire may lose equipment and control across several homelands. A later Occupation Revolt can find more local movements ready to act and can give those movements stronger locally supported forces.

106 directly releases no country and starts no independence war. High native resistance can still have engine-owned consequences. The developer's public description of the native system explicitly discusses garrison losses and large uprisings, while the exact installed thresholds remain a required runtime check. Evidence item E06 separates that native behavior from the scripted responsibilities of 106 and 095.

The remaining parts specify the local memory, the cross-event response, recovery and Chaos feedback, achievements, presentation, and acceptance conditions.

---

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

---

# 106 Resistance, Part 3: Revolts and connected events

## Resistance prepares territory for Occupation Revolt

The main connection is a later 095 Occupation Revolt finding several affected homelands ready to act. Higher native resistance makes the occupation more unstable. Recent real waves add local support. Low compliance makes that support harder for the occupier to contain. More than one distinct movement can rise during the same 095 firing, and the affected places can support stronger rebel forces.

The wave does not schedule 095 automatically. It leaves a changed occupation and bounded local evidence for a later valid firing. A player cannot press an acknowledgment to turn every occupied state into an immediate independence war.

095 remains the owner of claimant legality, ordinary selection and fallback, country creation or restoration, state transfers, rebel composition and equipment, war setup, and committed armed-outcome records. 106 supplies current resistance and the narrow local context from Part 2.

The inspected legacy 095 script selects an exiled country and has no resistance-history consumer. This package therefore includes a concrete dependency for its rework. The behavior below is required future integration, not a description of current working code. Evidence item E01 records that distinction.

## Preserve the ordinary 095 path

When no usable 106 history exists, 095's candidate pool, ordinary result, force budget, fallback, and RNG path remain the same as the accepted 095 baseline being integrated. Do not add a hidden random draw, change ordinary weights, or consume support merely while checking for its absence.

When usable history exists, preserve 095's ordinary candidate-selection process. Its selected outcome may receive the local force uplift below on the states that actually support it. Then the additional-movement branch can consider other legitimate movements.

If the ordinary path has no eligible result, its own accepted fallback remains with 095. The 106 branch can add only movements that independently pass 095's occupation, identity, territory, and armed-outcome gates. It cannot turn a generic fallback into permission to create an invented resistance country.

## Local support calculation

The following formulas are mathematical design notation. They are parent-selected initial calibration, not engine script or native uprising thresholds.

For an assigned state `s`, let `A_s` be the sum of its retained, unexpired, unconsumed 106 contributions at the time of the 095 firing. Each contribution uses the 365-day linear fading rule from Part 2.

Let `R_s` be current native resistance and `C_s` current native compliance, each on a 0 to 100 scale. Clamp only the calculation's supported input range. Do not rewrite native state values to make an input fit.

`history factor h_s = min(1, A_s / 50)`

`local control factor w_s = (R_s + 100 - C_s) / 200`

`local support b_s = h_s × w_s`

Thus `b_s` ranges from 0 to 1. A state without usable support has `b_s = 0`. Current high resistance and low compliance raise the contribution. Genuine recovery lowers it. Two recent full baseline waves can fill the history factor, while later higher resistance still changes the result.

The control factor deliberately uses native state facts that have a documented representation. The 095 owner can retain its own proven garrison and occupation conditions in its ordinary legality and readiness rules. The 106 formula does not invent a garrison-strength getter or an additional national control meter.

## Stronger forces from the actual affected states

Let `f_s` be the ordinary 095 local force-budget contribution of one state that the committed outcome actually uses. Its contribution with valid 106 support is:

`enhanced local contribution = f_s × (1 + 0.50 × b_s)`

The maximum extra contribution is 50% of that state's ordinary contribution. An unaffected or unusable state keeps its ordinary `f_s`. A tiny affected state cannot multiply the force budget of the entire restored country.

095 sums the relevant local contributions before final roster rounding and applies its own legitimate manpower, equipment, composition, and capacity rules. The owner must demonstrate a supported force representation that preserves a meaningful positive uplift where it can physically fit. Rounding each state to whole divisions before aggregation could erase the effect and does not satisfy this design.

The inspected legacy one-unit-per-owned-state implementation is not a verified local budget adapter. Building that adapter and its positive armed-result proof is part of the 095 dependency. 106 never compensates for a missing adapter by directly spawning its own units.

### Immediate examples

These examples hold the state footprint and other 095 inputs fixed. They have no elapsed fading and use compliance zero unless stated otherwise.

| Recent actual history | Current resistance | `h_s` | `b_s` | Extra local force contribution |
| --- | ---: | ---: | ---: | ---: |
| One +25 wave | 25 | 0.50 | 0.3125 | 15.625% |
| Two +25 waves | 50 | 1.00 | 0.7500 | 37.5% |
| Three +25 waves | 75 | 1.00 | 0.8750 | 43.75% |
| One +100 wave | 100 | 1.00 | 1.0000 | 50% |
| One +25 wave, compliance 80 | 25 | 0.50 | 0.1125 | 5.625% |
| One +25 receipt at age 182.5 days, resistance still 25 | 25 | 0.25 | 0.15625 | 7.8125% |
| Every retained receipt at age 365 days | Any | 0 | 0 | 0 |

Another firing while already at 100 gives no new contribution and refreshes no date. The table's large initial force effects therefore cannot be farmed by replaying a saturated state.

## Candidate identity and territory

Group candidate states by 095's canonical movement identity before creating countries or units. A homeland with several affected states is one movement. A registered package retains its exact row identity, and a final carrier-country check prevents two packages from recreating the same country.

An already existing country is not recreated. It can participate only through an existing-country restoration or reinforcement path that 095 owns and has validated. A dormant country requires 095's legitimate restoration path. Failure to prove either path makes that candidate ineligible for this integration.

First reserve the ordinary 095 outcome's territory. For the remaining candidates, resolve overlapping territorial claims and carrier conflicts using the established 095 claimant precedence, with stable canonical identity as the final tie-break. This allocation occurs before support scoring. The same state can enter only one provisional candidate footprint for the firing.

Do not let stronger support change the overlap allocation order. Candidate membership, overlap assignment, and carrier allocation depend on current legal homeland geography, independently of receipt presence, freshness, or consumption. An expired zero-support candidate is not removed early in a way that reallocates its territory to another candidate. Otherwise aging alone could make a different claimant stronger. The policy does not claim to maximize every theoretically possible arrangement of overlapping claims. It provides one deterministic, reviewable allocation.

## Population-weighted candidate support

For each candidate, freeze its provisionally assigned valid occupied homeland states and their current native population weights at the start of this 095 transaction. These form its scoring footprint.

The denominator includes every state in that assigned footprint, including states with absent, expired, or consumed 106 history. Those states have `b_s = 0`. This prevents an aging weak receipt from disappearing out of the denominator and making the candidate's support rise merely through expiry.

`candidate support B = sum(population_s × b_s) / sum(population_s)`

Use the same current native state-population basis for every candidate. A zero denominator gives `B = 0`. Do not switch between population, state count, and force weight to obtain a preferred result.

The footprint used for an additional release is a narrower subset. Only reserved states with a valid positive unspent receipt and `b_s > 0` can supply that extra outcome's transferred territory or its enhanced local forces. Unaffected homeland states can lower the candidate's average, but cannot be transferred by the 106-only extra path.

This provides two useful constraints. Broadly affected homelands can support more additional uprisings. A small affected corner cannot release or supply an army from a large unaffected homeland.

For an unchanged footprint and unchanged population weights, more usable positive history, higher resistance, or lower compliance cannot lower `B`. Decay and consumption cannot raise it. Changes to the actual occupation footprint or population weights can change the average in either direction, which is a change in the candidate's geography rather than a penalty applied to a repeated wave.

## Up to eight additional movements

After the ordinary 095 result has been reserved, the extra branch uses four alternative support bands:

| Minimum candidate support `B` | Maximum additional distinct movements permitted by that band |
| ---: | ---: |
| 0.10 | 2 |
| 0.35 | 4 |
| 0.60 | 6 |
| 0.85 | 8 |

Count the currently valid disjoint candidates meeting each threshold. A band's available result is the smaller of that count and its maximum. Choose the band yielding the largest result. If two bands yield the same result, use the higher support threshold. Within the chosen band, select the strongest candidates by `B`, using stable canonical identity as the final tie-break.

The bands are alternatives. They do not add together. The hard ceiling is eight additional movements across the entire 095 firing, including all occupiers, regions, packages, and carriers. A normal single baseline uprising plus eight extras can therefore produce nine scripted country outcomes when nine legitimate distinct identities and sufficient valid territory exist.

The additional branch makes no new random draws. The occurrence and ordinary selection of 095 retain their own randomness. The number of extras is a deterministic consequence of the local campaign state, which makes matched comparisons and replays reviewable.

### Fixed-footprint examples

Assume the ordinary 095 outcome has already reserved its separate territory. Eight further legitimate candidates each have disjoint equally supported footprints, compliance zero, and no fading.

| Every extra candidate's state history | Candidate `B` | Additional outcomes |
| --- | ---: | ---: |
| No usable 106 history | 0 | 0 |
| One actual +25 wave from zero | 0.3125 | 2 |
| Two actual +25 waves, now at 50 | 0.75 | 6 |
| Three actual +25 waves, now at 75 | 0.875 | 8 |
| One actual +100 wave from zero | 1.0 | 8 |

With only three eligible extra candidates at `B = 0.75`, the result is three extras. The maximum does not invent five more countries. With many states belonging to only one homeland, the result is at most one additional identity.

These are supported-outcome counts for the declared input pool. They are not the probability that 095 fires, a national AI click chance, or a forecast of victory in the resulting wars.

## Commit the local outcome

Before each selected extra is committed, revalidate its reserved states, live controller, occupation episode, homeland or package binding, unspent support, and country-carrier legality. Recompute its numerator from valid contributors using the frozen denominator and weights for this transaction. Invalidated members contribute zero during this recheck. They cannot make the candidate stronger by shrinking the denominator.

If it no longer meets the chosen threshold or cannot produce a valid positive armed outcome from the allowed footprint, skip that extra. Do not redraw the world, reroll a claimant, select an unrelated substitute, or backfill an unaffected capital during the transaction. The realized number may be smaller than the initial maximum when the world changes before commitment.

An extra-only territorial operation must use the exact reserved positively affected subset. A broad release-all-cores helper or a homeland-wide transfer would violate the connection even if the candidate score was calculated correctly. A capital or legal spawn location must be available within the valid footprint under 095's supported restoration rules. If it cannot be, the candidate is ineligible.

Compute force contributions only for the states the final result actually uses. A failed country creation, missing spawn location, invalid war setup, or zero physical armed result cannot publish a fresh success receipt. The 095 owner must preflight its political and military requirements and report what it actually committed.

Freeze the final validated receipt identities, values, old episode and occupier, movement binding, and allowed footprint in a 095-owned transaction frame before the outcome mutates countries, control, or forces. On physical success, consume the contributing identities once and preserve the fresh achievement proof from that frame as specified in Part 2. The outcome's own lifecycle callbacks can retire the old live support without erasing the validated provenance. Never revive old support or consume a new controller's episode. Each independent candidate has its own proof. One country's success cannot consume a global latch for all other candidates.

## Native uprisings and ordering

106 finishes its direct write and records the actual result before later native movement or a 097 recovery write can be mistaken for the immediate addition. The report can then describe what this wave actually did.

095 is a later independent firing. If a shared event sequence contains both events, use the recorded order. A 095 firing before the 106 wave sees the earlier state. A 095 firing after it sees the completed native values and committed local receipts. The cluster system must not quietly run 095 a second time merely because 106 appeared in the same burst.

The native engine may create an uprising after resistance rises. A later 095 evaluation rechecks the resulting country and map. It cannot recreate an already restored identity, return the same state twice, or count a native outcome as a scripted 095 success.

Same-tick 097 work must execute as a separate owner transaction after the direct 106 readback when it follows the wave. Strong collaboration can help subsequent recovery and can reduce later `b_s` through the current native resistance or compliance values. It never vetoes or discounts the nominal wave.

## Other named connections

| Event | Meaningful use of Resistance | Ownership and locality |
| --- | --- | --- |
| 097 Collaboration | Helps occupation recovery after the wave through its genuine native or accepted owner effects | 097 owns its networks, government registry, and recovery. 106 never calls Burn or Retire merely because resistance rose |
| 110 IMRO | A verified local movement can read recent affected territory and current native resistance when its own support or success evaluation runs | The movement must match the affected occupation. A distant wave creates no automatic nationwide IMRO bonus |
| 006 Independence Wave | Its legitimate territorial or package evaluation can take account of local resistance and a matching recent receipt | Preserve exact package-row identity. 006 owns its releases, government choices, and subsequent state changes |
| 113 The Partition | Foreign control created by its outcome becomes eligible for a later wave | No earlier wave is backfilled onto the new map or controller |
| 116 Warlords | New foreign occupations created by fragmentation can face the next wave | Local cores and genuine foreign occupations are evaluated under the same native rule |

For 110 and 006, the immediate meaningful link already exists through changed native resistance. A richer scripted reader is limited to an actual owner evaluation that has a documented use for the context. This package does not invent a new success roll, movement, release, or generic multiplier for those events. Their owner contracts must identify the exact effect before any additional weighted change is implemented.

If a partner's current identity or owner contract is unresolved, keep the native wave fully functional and leave that optional reader integration explicitly pending. The required 095 connection remains a completion dependency for this package.

## Collaboration's existing planned API

The inspected 097 specification separates its planned RestorationPressure from the old runtime script. It gives 095 responsibility for actual restoration and the related Burn or Retire calls. Evidence item E02 records this existing specification and its implementation limit.

A 106 wave is not itself a network burn, a government retirement, or a liberation. It does not spend or clear 097's planned state. If a later 095 outcome genuinely restores a country or changes the relevant government, 095 performs the accepted 097 cleanup through that owner's API and only once for the committed outcome.

Avoid treating 097's collaboration value, native compliance, and 106's hidden local support as interchangeable quantities. Only observed native `R_s` and `C_s` enter the initial 106 uplift formula. Any other approved 095 inputs remain under its own documented rules.

## Domestic Unrest cluster

Register Resistance as a Low-severity member of the semantic Domestic Unrest cluster, preserving its Minor Repeatable and Chaos level 1 identity. The supplied cluster snapshot omits 106 and contains numbering conflicts elsewhere, so the implementation must resolve the live cluster identity before changing its numeric registration.

A cluster burst uses the shared sequence and pacing contract. Every logical Resistance firing contributes one worldwide wave. Repetition from a genuinely later firing remains allowed. Duplicate delivery through the burst dispatcher and a country report is still one firing, not two.

The cluster contributes no extra 106 Chaos award for the same wave. 095 retains its own political consequences and their shared-source accounting. This keeps the connection strong while keeping each outcome attached to the event that actually produced it.

---

# 106 Resistance, Part 4: Recovery, Chaos, and achievements

## The occupation after the wave

The immediate increase creates a new demand on the occupier's existing resources and policies. The player decides how much of the war effort to commit to holding foreign territory. A well supplied garrison and favourable native recovery conditions can bring resistance down again. An overstretched country may face losses and disruption in several occupied homelands at once.

Use the installed occupation system's manpower, equipment, garrison template, law, compliance, and intelligence rules. The specification does not invent a fixed recovery rate or promise that a particular law always solves the problem. Their exact effects depend on the supported game version and the campaign's active modifiers.

The important tradeoff is practical. Resources used by occupation forces compete with other needs. Recovering recently pacified territory can delay the occupier's next offensive. A country whose homeland is occupied may exploit the same pressure through its existing army, diplomacy, and supported liberation routes.

### Campaign response matrix

| Situation | Meaningful response | What remains uncertain |
| --- | --- | --- |
| A small occupier with one foreign state | Review that occupation's garrison supply and policy before expanding further | Whether native recovery will outpace losses after the shock |
| An empire with several occupied homelands | Prioritize equipment and manpower across exposed occupations, taking account of local resistance and compliance | Which local movements a later 095 firing will find ready |
| A well established annexed occupation | Use its stronger compliance and supply position to recover the immediate rise | High compliance helps the aftermath but never cancels the wave |
| A subject holding foreign territory | Manage the subject's actual occupation under its own controller identity | Whether existing support from its overlord is enough under the native rules |
| A dispossessed human country that remains playable | Use the occupier's strain as an opportunity to recover its actual cores | Resistance does not promise a friendly uprising or a successful war |
| Several rival occupations of one homeland | Pursue each remaining occupying side and the current state of the homeland | A revolt against one occupier does not automatically settle the others |

## AI behavior

The world wave treats AI and human controllers equally. AI countries receive no automatic resistance reduction, free garrison equipment, cheaper occupation law, or immunity as compensation.

Their response uses the existing occupation AI. Validation must establish that the new resistance levels become visible to its ordinary garrison and equipment decisions. The native system already has a relationship between resistance, garrison losses, and equipment management, as the developer's public account describes in evidence item E06. The exact installed behavior still needs an observed scenario.

| AI role | Required behavior and evidence |
| --- | --- |
| Minor or major occupier | Receives every valid state addition and continues to manage garrison requirements through native occupation behavior |
| Subject occupier | Uses its own controlled states, with no duplicate processing through its overlord |
| Strongly supplied occupier | Can recover under its genuine native modifiers, without a 106-only hidden exemption |
| Occupier with weak supply or low compliance | Bears the resulting local risk and can face a stronger 095 response through the same public contract as a human occupier |
| Existing homeland country | Uses its normal military and political behavior, while 095 owns any uprising decisions and forces |
| Newly restored country or active revolt | Uses the country and military AI established by its actual owner event |

There is no random choice inside the 106 addition. The relevant weighted surfaces are the shared repeatable picker and the 095 candidate response defined in Part 3. Their probability handoffs must distinguish an event-selection probability, an independent uprising roll, an AI willingness score, and native behavior that the available tools cannot quantify.

## Chaos from actual new pressure

Let `D` be the sum of the actual positive resistance additions in this wave, measured in percentage points across all valid states. This is an internal calculation. A state moving from 90 to 100 contributes 10, regardless of the nominal wave strength. A state already at 100 contributes zero.

Use the following initial calibration. These values are parent-selected design additions under the user's request for a full expansion. They are tunable balance anchors, separate from the user's fixed wave amounts and evolution thresholds.

| This wave's actual sum `D` | Direct Chaos award before guards |
| --- | ---: |
| 0 | 0 |
| More than 0 and less than 25 | 0 |
| At least 25 and less than 250 | +2 |
| At least 250 and less than 1000 | +3 |
| At least 1000 | +5 |

Ten uncapped baseline additions produce `D = 250`. Forty produce `D = 1000`. Evolved waves reach a band through the resistance they actually add. Current Chaos does not multiply that award again.

### Repetition limits

Award positive 106 Chaos at most once every 90 elapsed days worldwide. The first eligible credited wave starts that clock. Day 90 is eligible again. Keep a gross lifetime positive ceiling of +30 for this event family across all countries, stages, and firing routes.

When a wave qualifies, its proposed gain is the smaller of the table amount and the remaining lifetime allowance. A final allowance of 1 permits a final +1. Only a positive gain actually accepted by the shared Chaos system consumes the time gate and lifetime allowance. A suppressed or zero gain creates no later reduction credit.

There is no carried balance. A wave with `D = 24` gives zero. Two such waves still give zero. A qualifying wave during the 90-day gate still changes resistance and local history, but its blocked Chaos amount is discarded. A later wave must qualify through its own actual additions.

Save and reload, stage changes, controller changes, settings changes, duplicate delivery, and completed containment do not reset the gross lifetime total. Reductions never reopen the positive allowance.

## Chaos impact map

| Milestone or outcome | Why Chaos changes | Direction and starting amount | Dynamic factors | Repeat guard | Shared-source overlap | Containment counterpart |
| --- | --- | --- | --- | --- | --- | --- |
| A qualifying wave adds resistance to occupied territory | A real new burden of instability has appeared | +2, +3, or +5 | Actual sum `D`, remaining lifetime allowance, elapsed time since credited gain | One gain per 90 days, +30 gross lifetime, one credit per wave | Counts the added occupation pressure only | Its frozen affected footprint can earn a limited reduction |
| An empty wave, a fully capped wave, or `D < 25` | This firing creates no qualifying new burden under the chosen bands | 0 | This wave's actual result only | No carryover or deferred award | Nothing duplicated | Creates no refundable credit |
| An evolution activates or is logged | Future capability changes without a new wave | 0 | Highest active stage changes future `A` | One stage history record, no Chaos award | Nothing duplicated | No reduction owed |
| 095 turns local conditions into an armed outcome | Country creation, troops, and wars belong to that outcome's owner | 0 additional from 106 for the armed outcome | 095 consumes the valid local support from Part 3 | 095 owns committed outcome receipts | Its wars and losses remain with their existing shared sources | 106 cannot refund those separate outcomes |
| A credited footprint recovers at both required checks | Most of the credited pressure has been brought back under control | Up to -1 for a +2 or +3 credit, or -2 for a +5 credit | Original affected weights, observed recovery, remaining reduction allowance | One settlement per credited wave, -10 gross lifetime ceiling | Counts recovery of resistance, not peace, deaths, or territorial transfer | Consumes the original credit once |

## A finite containment return

Only a wave with actual credited Chaos opens a containment record. Freeze every state that gained resistance in that wave, its original occupier, its occupation episode, its pre-wave resistance, and the actual addition. The actual addition is that state's fixed weight. The sum of those original weights remains the denominator for the entire record.

Check that fixed footprint at 180 and 270 elapsed days after the wave. A state contributes its weight to the final qualifying intersection only if it satisfies all the following at both observations and remains valid at settlement:

- The original occupier still directly controls it, and the original occupation episode remains valid.
- It has had no intervening control loss, transfer, release, or conversion into the occupier's core.
- Current resistance is at most its pre-wave resistance and at most 25.
- No later positive 106 addition has superseded this state's contribution to that containment record.

The same states must pass both observations. It is insufficient for one group to supply 75% at day 180 and a different group to supply 75% at day 270.

Lost, released, transferred, cored, or otherwise invalid states contribute zero while retaining their original denominator weight. A vanished controller contributes no qualifying weight. An original high-weight state cannot be removed to make the remaining footprint easier.

A later positive 106 write permanently disqualifies that state's contribution to the older pending containment record. This also applies when the later wave received no Chaos award. A capped write of zero does not supersede it. Later recovery can therefore settle at most the newest eligible credited pressure for that state, rather than refunding several overlapping shocks through one fall in resistance.

If the qualifying intersection reaches at least 75% of the original weighted footprint, propose a reduction equal to half the wave's actual credited Chaos, rounded down. Apply the remaining lifetime reduction allowance, whose gross ceiling is 10. Thus +2 permits -1, +3 permits -1, +5 permits -2, and a final +1 permits no reduction.

Close the record after its one settlement attempt. Any amount suppressed by the shared meter or lost to its zero floor is not banked for later. The reduction does not return capacity to the +30 gross positive ceiling. This keeps repeated recovery from becoming a source of unlimited negative Chaos.

### Bounded lifetime and evidence

Use two finite scheduled observations of stored cohort members. They are addressed through the verified country or shared lifecycle routes and inspect only the named footprint. The final settlement revalidates those stored members. It does not search the world for countries that happen to look recovered.

Every unsettled record expires at day 300. Retire expired records before opening a new one. The 90-day positive-award gate and the 300-day lifetime allow at most four pending containment records. Size compact lifetime credit identities for up to 30 positive integer credits under the +30 gross ceiling, so storage does not assume that the shared meter always accepts the full request. Release detailed state rows after settlement or expiry, keeping only small spent identifiers needed to reject duplicate work.

Resistance is observed at two checkpoints. The design does not claim continuous low resistance between them. Continuous control and occupation continuity are separate facts that require verified lifecycle evidence. If an actor disappears or a required observation is missed, do not invent the missing proof or reduce the denominator. The implementation must preserve the finite scheduling and overdue-expiry contract through save and reload.

This proof is separate from the 365-day local memory used by 095. An expired uprising-support receipt cannot be revived by a still-open achievement or containment record.

### Due observations and a new wave on the same date

An unobserved day-180 or day-270 containment or achievement checkpoint takes precedence over a new 106 write at that exact elapsed-day boundary. Before stage resolution and state mutation, drain only registered proof records due at that boundary through their stored cohorts. The ordinary callback and this pre-write route share the same once-only observation and settlement identity. No recurring world scan is needed.

Record the observation and any resulting settlement or achievement completion first. Then apply the new wave. Its positive additions supersede contributions in older containment records that are still pending, including a record that has just passed its first observation. A completed settlement or earned achievement is not clawed back. A zero addition does not supersede pending containment weight.

Save and reload preserve the due boundary, observation result, and completion state. A callback delivered after the checkpoint date cannot replace a missing observation with a later favorable snapshot. This precedence controls the 106 write and the named proof checks. It does not reconstruct earlier native resistance changes elsewhere in that date.

## Achievement 1: Containment mastery

Working label, not final localisation. Proposed stable achievement ID: `chaosx_106_containment_mastery`.

This challenge rewards an existing human occupier for recovering from a severe actual shock while keeping every affected occupation. It adds no gameplay reward or enrollment action.

| Field | Required design |
| --- | --- |
| Eligible country | An existing human-controlled country with valid occupied territory |
| Qualifying wave | An active Stage II or Stage III wave, nominally +75 or +100, that actually adds at least 50 points in at least five of its occupied states |
| Immutable cohort | Every occupied state under that country that receives any positive addition in the first qualifying wave |
| Observation dates | Days 180 and 270 after the qualifying attempt starts |
| Required state result | Every cohort state is still a valid occupation under that country, with resistance at most 25 and compliance at least 40 at both observations |
| Control condition | Direct control of every cohort state remains uninterrupted for the attempt |
| Attempt failures | Control loss, transfer, release, conversion into an occupier core, removal from occupation, an omitted original member, or loss of the eligible human-control route |
| Retry | A later qualifying wave may restart an attempt only with the same original cohort. At least five original cohort members must again gain at least 50 actual points, and all original members must be valid occupations under the player at the restart |
| Visibility | Visible after the applicable occupation challenge is first discovered |
| Difficulty | Very hard |
| Icon | A repaired rail junction or guarded lamp holding against extinguished sparks, with a strong 64×64 silhouette |

The original cohort never shrinks. Newly conquered states cannot replace difficult old members or supply the five-state restart condition. A later wave can make recovery harder, but it does not erase the first attempt's evidence or silently move its checkpoints. A failed attempt requires an explicit later qualifying restart.

The challenge concerns low resistance and substantial compliance at two observed dates, plus continuous territorial control. Its text must not claim uninterrupted low resistance merely from two samples. Native garrison and occupation choices, including legitimate 097 recovery, can contribute to success through their actual results.

## Achievement 2: Homeland recovery

Working label, not final localisation. Proposed stable achievement ID: `chaosx_106_home_recovery`.

This challenge follows an existing human country as it recovers occupied cores after a real locally supported 095 uprising. It requires the player to win territory through its own war effort and to keep the complete restored footprint after peace.

| Field | Required design |
| --- | --- |
| Eligible country | An existing independent human-controlled country whose cores are under hostile occupation, using an already supported control route |
| Qualifying wave | Nominal addition at least 50, with at least three occupied core states each gaining at least 25 actual points and at least 100 actual points added across its affected occupied cores |
| Immutable cohort | Every core of that country under hostile occupation that receives a positive addition in the first qualifying wave |
| Local 095 link | A later 095 firing commits a real armed outcome using a still-valid positive 106 receipt from at least one cohort state |
| Earned recovery | At least two original cohort states pass directly into the player's control through its own hostile control changes during a war against their occupying side |
| Complete recovery | The player directly owns and controls every original cohort state |
| Lasting result | Keep the complete set for 180 elapsed days after complete recovery and peace with the surviving recorded occupiers and hostile 095 actors, whichever condition becomes true last |
| Independence | Remain independent throughout the tracked recovery and the final hold |
| Control route | Remain the eligible existing human country. The challenge grants no switch into a new rebel country |
| Reset | Losing any cohort state or resuming a relevant war restarts the final hold after full recovery and the required peace are restored |
| Terminal failure | Losing independence or the eligible human-control route closes this achievement attempt as failed for the rest of the campaign, with no restart |
| Invalid shortcuts | Gifts, peaceful transfers, release effects, and ally-held territory do not supply the two own hostile recaptures. Becoming a subject invalidates the attempt |
| Visibility | Hidden until the qualifying occupation and local 095 relationship have been established |
| Difficulty | Very hard |
| Icon | Broken restraints opening around a restored home, without a country-specific flag |

The two own recaptures leave room for 095 to restore another state from the minimum three-state cohort. This avoids requiring the player to deliberately lose a newly restored state just to recapture it for credit.

Ceded states and changes in core status never remove an original cohort member. The challenge still requires direct ownership and control of the full frozen set. A destroyed occupying tag can be treated as no longer at war only after its lifecycle is verified. Renaming, tag changes, and a missing pointer cannot silently erase a still-active hostile side.

A candidate selection or attempted rebel spawn cannot satisfy the 095 link. The consumer must return committed evidence identifying the uprising, the actual state, the valid positive receipt, and the resulting armed outcome. An ordinary native uprising by itself does not satisfy this specific 095 achievement condition.

The inspected legacy 095 script has no 106 history reader. This achievement therefore remains dependent on the 095 integration specified in Part 3. It cannot be substituted with an event-fired flag. The own-hostile-recapture detector and the continuous independence and post-peace hold also require verified existing achievement or lifecycle contracts.

## Achievement tracking and presentation

Keep at most one immutable cohort per achievement for each eligible human country. Repeated waves do not create an unlimited list of attempts. A containment attempt can restart against its original cohort under the stated entry test. Homeland recovery continues against its original cohort and its genuine armed-outcome proof only while the attempt remains eligible. Loss of independence or the supported human-control route is a terminal campaign failure for that achievement. Retain the immutable cohort and closed identity so later independence, a returning player, a new wave, or a stale callback cannot restart it or reuse its old recapture and 095 evidence. Ordinary territorial loss or renewed relevant war resets only the final hold.

Use the project's established achievement eligibility, debug, and multiplayer rules. Forced test firings and synthetic fixtures do not count as earned campaign progress. If the current framework cannot distinguish the relevant test route, wire that distinction before enabling these achievements.

The achievement subjects and all three texture states are specified in Part 5. Final names and descriptions are written after the mechanics are implemented and checked. They should explain the difficult campaign objective and the few conditions the player needs to understand, leaving receipt and callback details internal.

## Why these additions belong here

The wave already supplies the event's large immediate effect. The added depth follows its consequences: native recovery, local support for a later uprising, limited Chaos feedback for real new pressure, a small return for demonstrable containment, and two demanding ways to master or exploit the resulting campaign state.

The balancing values above are explicit so implementation does not have to invent them. Runtime tuning may adjust these parent-selected secondary anchors with evidence. The fixed 25, 50, 75, and 100-point additions and the 200, 400, and 600 Chaos requirements remain the user's design.

---

# 106 Resistance, Part 5: Presentation and asset direction

All newly proposed surface and asset labels in this file are working labels, not final localisation. The event name and the three evolution names come from the user. Finished prose, option wording, tooltips, and achievement titles belong to implementation and its localisation review.

## The player's view

The event should feel immediate and widespread. Occupied streets, railways, work sites, and communities become harder to control. The reports draw their tension from people acting with unexpected resolve in many places at once. They should not invent a single world resistance command or claim to know which later liberation movement will succeed.

An affected occupier sees a completed rise in resistance and the practical strain it can place on garrisons. A country with occupied cores sees local defiance and an uncertain opportunity. An observer sees the scale of the disturbance. The same report family can carry these three viewpoints without creating different gameplay outcomes.

Keep the emotional focus on occupied people and the forces trying to hold territory. Use concrete scenes and consequences. Avoid staff-table summaries, paperwork drama, staged denials, failed-broadcast clichés, invented quotations, or a narrator announcing what the player should fear.

Humour is limited to dry or self-damning reactions where the viewpoint supports them. Garrison casualties and civilian suffering receive a serious treatment. A liberation viewpoint can show guarded hope without promising a country, an army, or a successful revolt.

## Information hierarchy

The native occupation screen remains the place to inspect current resistance, compliance, and garrison needs. The event adds no persistent player-managed currency or counter.

| Information | Presentation role |
| --- | --- |
| Native current resistance | Primary local condition, visible through the existing occupation interface |
| Native compliance and garrison condition | Existing context for recovery and later uprising readiness |
| Wave addition | Transient mechanical explanation in the report or its effects tooltip |
| Locally changed and locally saturated state counts | Optional concise report facts when available from the completed wave |
| Recent local wave memory | Hidden input to cross-event behavior, explained qualitatively only when relevant |
| Wave identifiers, episode identifiers, receipt slots, raw readiness and force calculations | Internal bookkeeping |

The new persistent custom value budget is zero. Adding a new public resistance-support gauge would duplicate native occupation information and make a simple global event harder to read.

If the report has room for only one number, show the wave's nominal addition. If it also shows affected counts, distinguish eligible states from states that actually increased. A country with ten eligible states and four already at 100% has ten eligible occupations and six changed states. Do not present all ten as positive additions.

## Text surface map

| Surface | Viewpoint and tone | Required information | Dynamic context and restraint |
| --- | --- | --- | --- |
| Event identity | Clear, direct | Resistance and its event identity | Preserve the user-supplied name across the shared event list and event details |
| Occupier report | Strained control, dry or grim reaction | A worldwide surge has reached the recipient's occupations | Use recipient-relevant states only when their completed-wave facts are valid |
| Occupied-homeland report | Local resolve, guarded hope | Resistance has increased in eligible occupied cores associated with the recipient | Do not claim that an uprising has happened or that outside help is guaranteed |
| Observer report | Serious, geographically broad | Occupations across the world were affected | Avoid assigning the observer responsibility for the wave |
| Saturated result | Concrete and accurate | Eligible occupations at the cap could not rise further | A high existing resistance level still matters to later native and 095 behavior |
| Empty direct-invocation result | Brief factual acknowledgment | The firing found no valid occupied states | Give no invented target, benefit, loss, or compensation |
| Acknowledgment option | Occupier's bitter acceptance, homeland's cautious resolve, or observer's concern | Acknowledges the already applied result | Direction only, with no mechanical choice and no second wave |
| Effects tooltip | Precise and plain | Current resistance rises by the stage's points, with a 100% cap | Distinguish percentage points from relative percentage growth and from resistance target |
| Event Details premise | Evocative and readable | Occupied communities across the world act at once | Keep mechanical instructions and effect lists in the appropriate mechanical surface |
| Wave history entry | Neutral world event record | One firing, its date, and its frozen stage | Use the shared actorless world-event representation |
| Evolution history | A lasting increase in future intensity | The recorded stage and actual activation date | Do not describe the stage entry as another wave |
| Evolution preview | Readable future behavior | User stage name, activation requirement, and future addition | Preview entries have no invented history index or date |
| Relevant 095 result | Local opportunity or breakdown | Which actual affected homeland or region helped the uprising | 095 owns the outcome text, and only committed results can describe new rebels |
| Containment feedback | Measured recovery | The tracked affected territory has recovered enough for its earned Chaos reduction | Explain the outcome without revealing receipt identifiers or suggesting a spendable reward |
| Achievement text | Ambitious campaign objective | The exact containment or homeland-restoration challenge from Part 4 | Final title and description must make the frozen cohort and disqualifications understandable |
| Catalog Name and Details | Same identity and premise as the game | Final event name and final Event Details prose | Mirror final implementation wording in the authoritative workbook |

Light-parchment report bodies use plain text, including dynamic substitutions. Put required colour and icons only in surfaces whose native formatting supports them. Do not make fake tables or meters out of punctuation inside localisation.

## Evolution expression

The progression should be legible without suggesting separate powers.

| Stage | Narrative direction | Mechanical emphasis |
| --- | --- | --- |
| Baseline | Scattered local acts occur across unrelated occupations | A sudden +25-point rise can undo recent pacification |
| Rising Resistance | Defiance is more confident and harder for occupiers to contain | Future waves add 50 points |
| Mass Resistance | Whole occupied regions can become difficult to administer | Future waves add 75 points, often approaching the cap |
| Total Resistance | The surge can fill the entire native resistance scale at once | Future waves add 100 points and cap at 100% |

These are tone directions. They do not create population participation percentages, universal strikes, separate damage rolls, or new mandatory incidents. The actual campaign consequences come from native occupation mechanics and the specified consumers.

## Required visual package

Use one coherent visual motif across the report and the two achievement subjects. Reuse the same event identity through all three evolution stages. Stage names and shared evolution metadata communicate the stronger future addition.

| Working asset identifier | Consumer | Source mode | Size and output | Visual direction |
| --- | --- | --- | --- | --- |
| `report_event_106_resistance` | The ordinary Resistance report family | Generated fictional period documentary scene | Final report card 210×176, one registered report sprite | An occupied industrial street or rail district with closed shutters, a rough obstruction, and a few watchful anonymous figures. The composition conveys local defiance without a named country or real movement |
| `chaosx_106_containment_mastery` | Containment achievement | Original transparent icon subject | 64×64 completed, grey, and not-eligible variants | A reinforced rail junction or guarded lamp surviving a ring of extinguished sparks, with one strong central silhouette |
| `chaosx_106_home_recovery` | Homeland restoration achievement | Original transparent icon subject | 64×64 completed, grey, and not-eligible variants | A broken restraint opening around a small home or homeland-shaped stone, without a specific country's flag |

The two achievement identifiers are proposed stable registrations. Check for collisions before wiring them, then use those exact registered IDs for all three DDS filenames. Do not silently rename one derivative or add an asset prefix that the achievement registry does not expect.

### Report art

The report picture uses the current project's black and white documentary treatment with a sepia finish. Compose a clear central subject that survives the small card. Leave room for the deterministic processing step that supplies tilt, transparent corners, paper border, and soft shadow.

Generate the underlying fictional scene without baked-in UI, text, captions, card borders, signatures, watermarks, or a false archival label. The processor owns the card treatment. Preserve the selected source and the processed output separately.

Avoid exact modern national flags, named historical leaders, recognizable extremist insignia, and country-specific uniforms in this global image. Their presence would make one local resistance tradition stand in for every occupation. The scene can be recognizably of the game's period without making a factual claim about a photographed incident.

A historical photograph may replace the generated route only after a separately documented source choice establishes its provenance, rights, period, and fit. Do not label a generated image as historical evidence.

### Achievement triplets

Each achievement has one original transparent colour subject. Keep the subject's scale, position, and alpha alignment identical across its three source states.

The completed composition uses the supplied unchanged `achievement_template.png`. The grey composition uses a deterministic grayscale derivative of the same subject with the supplied unchanged `achievement_template_grey.png`. The not-eligible composition uses that same grey subject and the unchanged red-cross overlay with the grey template.

The templates and overlay remain 64×64 and are not regenerated. Final textures are one-level legacy BGRA DDS files with strict decoded equality to the approved composition. Preserve the subjects, composed PNGs, final DDS files, and validation evidence.

Final achievement paths are directly under `gfx/achievements/`:

- `<registered_achievement_id>.dds`
- `<registered_achievement_id>_grey.dds`
- `<registered_achievement_id>_not_eligible.dds`

Ordinary event art belongs in the event folder directly under its asset category, with `gfx/event_pictures/106_resistance/` as the proposed report destination. The current owning GFX file and actual sprite names must be verified before final registration. Existing registered names stay stable.

## Visual and text acceptance

View the actual report with an affected occupier, a valid occupied-homeland recipient, and an observer. Check the empty and saturated cases. Use a long country name and a long state name to catch clipping and awkward substitutions.

View the main evolution history, the selected firing's related evolution history, and the Event Details evolution preview separately. Historical surfaces show real recorded metadata. The preview shows the catalog of stages. Re-enabling a stage must not create a duplicate historical row.

Inspect the Resistance identity in the actual shared list and detail consumers. The pinned shared interface resolves event text through the existing row system. Verify the name, description, and evolution mappings against ID 106 so stale catalog labels cannot display unrelated content. Evidence item E07 records the inspected consumer.

Inspect every achievement state at 64×64 in the native consumer. Check the subject silhouette, grayscale treatment, red-cross alignment, alpha edges, and filenames. A large preview cannot substitute for the native-size review.

The implementation's localisation auditor checks every final surface in the table above against the numerical rules and the current world context. It also checks tone, dynamic tokens, plain-text report bodies, and the prohibition on em dashes and semicolons in authored prose.

Planning this package creates asset briefs and text directions. It does not establish that any final art, localisation, GFX registration, or in-game render has been produced.

---

# 106 Resistance, Part 6: Acceptance and scenario matrix

## What this matrix proves

These are the required implementation scenarios. They have not been run in HOI4 for this planning task. The separate verification report identifies the arithmetic and package checks that were actually performed.

For each native wave fixture, preserve the logical wave identity, stage and nominal addition, state and controller identity, native occupation result, resistance before and immediately after, actual addition, and the final per-wave totals. Distinguish a fresh write, a capped zero, an invalidated state, and a replay.

For cross-event fixtures, also preserve the exact homeland or package identity, occupation episode, original receipt dates and values, assigned territory, current resistance and compliance, frozen population weights, candidate support, selected band, actual armed outcome, and consumption result. Use bounded debug evidence through the existing project conventions. These observations do not prescribe another public interface.

Separate the direct 106 write, later 097 recovery, the 095 outcome, and native engine consequences in the evidence. A final political map by itself cannot establish which system caused a change.

## A: Immediate arithmetic

| ID | Fixture | Required result |
| --- | --- | --- |
| A01 | Every cell of Part 1's resistance table | `after = min(100, before + addition)` exactly at supported native precision |
| A02 | Resistance 25, baseline addition 25 | Result 50, excluding a relative-percentage or set-to-value interpretation |
| A03 | Human report remains unacknowledged | Every direct state addition has already occurred |
| A04 | Low resistance target, high compliance, strong recovery modifiers | The immediate current-resistance write remains the full addition up to the cap |
| A05 | Resistance 100 under each stage and repeated firings | Remains 100, actual addition zero, no new local credit or refreshed date |
| A06 | Fractional native resistance, including the 24.5 example | Supported precision is preserved without an assumed 0-to-1 scale or unexplained rounding |

## E: Worldwide targeting

| ID | Fixture | Required result |
| --- | --- | --- |
| E01 | Major, minor, subject, human, and AI controllers each hold a valid occupied state | Every state receives the same nominal stage addition once |
| E02 | Valid unusual or dynamically created controller | Same native eligibility contract, with no unsupported country-class exclusion |
| E03 | Wartime non-core occupation, annexed non-core owner-equals-controller state, controller core, and mixed-control state | Selection follows native occupation and authoritative state control, with annexed non-core coverage |
| E04 | A valid zero-resistance occupation beside a truly prohibited resistance state | The eligible zero-valued state receives the wave without removing a genuine prohibition from the other state |
| E05 | Invalid controller and several valid states | Invalid state is skipped and does not cancel or redirect the remaining writes |
| E06 | Supported direct invocation with no valid occupation | One truthful empty result, no replacement target, no local receipt, and zero Chaos |

E03 and E04 require installed-reference and live evidence. A guessed `has_resistance` result or an owner/controller inequality cannot close them.

## V: Evolutions and sampling

| ID | Fixture | Required result |
| --- | --- | --- |
| V01 | Fresh grant state at Chaos 199, 200, 201, 399, 400, 401, 599, 600, and 601 | Nominal additions 25, 50, 50, 50, 75, 75, 75, 100, and 100 |
| V02 | Cross a threshold without firing 106 | Stage availability and its one history record change, resistance and direct Chaos do not |
| V03 | First firing after a jump from below 200 to at least 600 | Highest active addition 100 once, with no sum of stage amounts |
| V04 | A baseline wave begins at 199 and its gain crosses 200 | Every state in that wave receives 25, with Stage I applying to a future wave |
| V05 | Chaos falls below a previously granted threshold | Granted stage persists and highest enabled granted stage remains active |
| V06 | Disable an ungranted stage at its threshold, then enable it at qualifying Chaos | No grant while disabled, one later grant, and no unlock wave |
| V07 | Re-enable a previously granted stage below its threshold, or enable a higher stage while a lower one is disabled | Previous grant resumes without duplicate history, and independent higher-stage eligibility follows Part 1 |

## R: Repetition and changing occupations

| ID | Fixture | Required result |
| --- | --- | --- |
| R01 | Two baseline waves from resistance zero | 0 to 25 to 50 |
| R02 | New occupied territory appears between waves | It joins the next rebuilt target set at its own current value |
| R03 | New occupied territory appears after a wave with no later firing | It receives no capture-time or periodic 106 addition |
| R04 | Native recovery lowers resistance before another wave | The later addition uses that live value |
| R05 | A former target becomes a controller core or otherwise ineligible | It receives no stale later write |
| R06 | Duplicate country delivery, client acknowledgment, helper return, or saved callback for one logical firing | At most one state write and one aggregate credit, while a new legitimate wave remains repeatable |

## H: Local history and continuity

| ID | Fixture | Required result |
| --- | --- | --- |
| H01 | One, two, and three genuine +25 receipts on the same episode | Expected support and local force values in Part 3 |
| H02 | Fresh receipts 75, 25, and 10, followed by a real +1 admission | Existing stronger unspent support remains, with no total decrease at admission |
| H03 | The same fixture followed by a +30 receipt | The 10-point contribution is replaced |
| H04 | Receipt ages 0, 182.5, 364, and 365 days without a cleanup tick | Linear contribution, half at 182.5, and zero at 365 |
| H05 | Resistance falls from 100 to 95 before another wave | New receipt contains 5 points only, with original older dates unchanged |
| H06 | Controller A loses the state to B and later returns | New episode, with old unspent support unusable |
| H07 | Same foreign controller annexes a non-core occupation | Valid continuous homeland relationship can remain, while a changed relationship retires old support |
| H08 | Homeland or movement changes, including a change that reverses before the next read | Current mismatch is rejected, and promised interruption detection requires the actual writer or lifecycle hook |
| H09 | Movement cannot be resolved for a valid native occupation | The wave still applies, with no invented or borrowed partner binding |
| H10 | Expired, discarded, or consumed receipt followed by delivery of its old wave | Watermark rejects a new native write and fresh credit |
| H11 | Nested helper returns after an invalid or already-used read | Explicit zero and replay outputs cannot inherit another caller's positive result |
| H12 | A long-lived achievement record references an expired local receipt | Historical proof remains available, while usable uprising support stays zero |

## S: Occupation Revolt response

| ID | Fixture | Required result |
| --- | --- | --- |
| S01 | Candidate uses a matching affected state, controller episode, and homeland | Its 106 uplift is traceable to that exact local receipt |
| S02 | Unrelated territory or a newly acquired state has no matching wave history | It cannot borrow an occupier-wide or global support flag |
| S03 | Replay the same committed 095 transaction | No extra country, army package, receipt use, or achievement proof |
| S04 | Several states for one homeland | One canonical country identity, with summed valid local force contributions |
| S05 | Independent homelands under one or several occupiers | Separate valid outcomes can occur, with no single global consumed latch |
| S06 | Overlapping states or two package rows sharing a carrier | Fixed canonical allocation and one physical use per state and carrier |
| S07 | Increase support, resistance, or compliance separately on a fixed footprint and weights | More support and resistance cannot weaken uplift, while greater compliance cannot strengthen it |
| S08 | Change unrelated country's resistance or history | The tested candidate's local support and formula remain unchanged |
| S09 | Eight disjoint candidates at support 0.3125, then 0.75, then 0.875 | 2, 6, and 8 extras respectively, with the ordinary outcome kept separate |
| S10 | Three candidates at support 0.75, or many states for only one candidate | Three extras in the first fixture and at most one extra identity in the second |
| S11 | Tiny affected state in a large otherwise unaffected homeland | Zero-support states remain in the denominator, only the usable affected subset can be transferred or supply extra forces |
| S12 | Weak receipt expires or is consumed on fixed geography | Candidate numerator falls or stays equal, denominator and canonical allocation do not shrink because of freshness |
| S13 | A reserved state or claimant becomes invalid before commitment | Revalidation cannot retain its support, increase the score by shrinking the denominator, or substitute unrelated territory |
| S14 | Ordinary or extra release requires an unaffected capital or broad all-cores helper | Extra path is rejected until a valid exact-footprint outcome is available |
| S15 | No usable 106 history anywhere | Ordinary 095 pool, result, force budget, fallback, and RNG path match the immutable baseline |
| S16 | Candidate selected but its physical armed outcome fails | No fresh successful support consumption or achievement proof |
| S17 | Successful 095 restoration retires the old live episode before its success callback | Frozen validated pre-mutation provenance consumes every contributing receipt identity once and publishes one fresh earned outcome proof, without reviving support, reading the new episode, or bypassing an invalid pre-commit candidate |

## I: Named owners and native consequences

| ID | Fixture | Required result |
| --- | --- | --- |
| I01 | Strongest valid 097 recovery context before the wave | Full immediate addition remains, followed by its genuine later recovery |
| I02 | 106 and 097 writes in the same game tick | Direct 106 readback precedes its later recovery transaction, with both results attributed correctly |
| I03 | 095 before and after 106 in separate shared sequence fixtures | Each reads the state available at its own recorded order, with no automatic extra 095 firing |
| I04 | Valid local IMRO context beside unrelated territory | Only the matching local context reaches its owner evaluation |
| I05 | 006 uses a carrier shared by multiple package rows | Exact package and geography binding prevent cross-row borrowing |
| I06 | 113 or 116 creates a new foreign occupation | The next 106 wave evaluates it normally, with no backfilled prior wave |
| I07 | Inspect full 106 helper closure and dispatch graph | No 106-owned release, transfer, war declaration, civil war, or unit-creation substitute for 095 |
| I08 | Native high resistance restores a country before a later 095 firing | Correctly attribute the native outcome and prevent duplicate 095 creation or transfer |

## C: Chaos and containment

| ID | Fixture | Required result |
| --- | --- | --- |
| C01 | `D` equals 0, 24, 25, 249, 250, 999, and 1000 | Raw awards 0, 0, 2, 2, 3, 3, and 5 |
| C02 | Two separate waves with `D = 24` | Neither creates an award or carried balance |
| C03 | Qualifying wave at ages 89 and 90 days after a positive credit | Age 89 blocked and discarded, age 90 eligible |
| C04 | Lifetime gross total 29 and a qualifying +5 band | Actual proposed remainder +1, then gross ceiling 30 |
| C05 | Shared Chaos source suppresses or partially accepts an integer award | Suppression consumes no gate or allowance, while partial acceptance records only the actual positive credit and sizes lifetime identities safely for up to 30 integer credits |
| C06 | Original weights 75 and 25, with the same 75-weight member qualifying at both checks | Exact 75% passes, while anything below it fails |
| C07 | Different groups each provide 75% at the two checkpoints but their intersection is below 75% | Fails containment |
| C08 | A high-weight member is lost, transferred, released, cored, or omitted | Weight remains in the denominator and contributes zero |
| C09 | Later uncredited positive wave versus later capped zero wave | Positive write invalidates the older contribution, capped zero does not |
| C10 | A +2, +3, +5, and final +1 credited wave meets containment | Maximum reductions 1, 1, 2, and 0 before the remaining global reduction allowance |
| C11 | Floor-limited reduction, disabled reduction, or duplicate settlement | Record closes once, with no banked remainder or repeat payment |
| C12 | Four pending records, overdue cleanup, missed checkpoint, and save reload | Expiry-before-open and day-300 limit hold, no fifth pending record, no favorable late substitute for missing checkpoint evidence |
| C13 | A day-180 or day-270 check shares a date with a new positive 106 wave, including a due Chaos return near a stage threshold | Due observation and settlement run once before stage resolution and the new write. The settled meter feeds any ungranted-stage catchup. Granted stages persist. Completed results stand, while the new write supersedes only older contributions still pending |

## T: Achievements

| ID | Fixture | Required result |
| --- | --- | --- |
| T01 | Stage II or III wave with five original occupied states each gaining at least 50 | Arms containment mastery and freezes every positively affected occupation under that player |
| T02 | Five states qualify but an additional small positive state is difficult to recover | The additional original state remains mandatory |
| T03 | Every original state meets resistance 25 and compliance 40 at days 180 and 270 under continuous control, including a new wave due on an observation date | Unlocks through exact inclusive thresholds, with the due check before the new write and no clawback of earned completion |
| T04 | Lose an original state, then acquire five easier states | Failed attempt cannot replace its cohort or use new states for the restart condition |
| T05 | Later qualifying restart with five original members gaining at least 50 | Same immutable cohort and new explicit attempt dates |
| T06 | Existing independent human core owner, nominal wave at least 50, three cores gain at least 25, total actual gain at least 100 | Arms homeland recovery with the full original positively affected occupied-core cohort |
| T07 | Two own hostile recaptures and one valid 095-restored member of a three-state cohort | Can satisfy earned recovery without deliberate loss and recapture |
| T08 | Gifted, released, or ally-held states are presented as own recaptures | They do not supply the two hostile recapture proofs |
| T09 | Valid local 106 receipt is rejected by 095 or only a native uprising occurs | Does not satisfy the required committed 095 link |
| T10 | Full recovery, relevant peace, and 180-day hold, interrupted by war or a lost state | Hold starts after the last required condition and restarts after an interruption |
| T11 | Subject shortcut, unsupported player switch, or synthetic test firing | Does not produce an earned unlock under the established eligibility rules |
| T12 | Homeland attempt loses independence or its eligible human route, then regains it and receives another wave or stale callback | The campaign attempt remains terminally failed with the same immutable cohort, no restart and no reuse of its old recapture or 095 evidence |

## L: Scale, persistence, and timing

| ID | Fixture | Required result |
| --- | --- | --- |
| L01 | More than 1,000 valid occupied states, including a single large controller | Every state receives the immediate wave once, without a lost suffix or next-day remainder |
| L02 | Two human controllers and several AI controllers in multiplayer | One authoritative world execution, with no client-acknowledgment multiplication |
| L03 | Save before the firing and after the completed wave | Correct one-time result, original dates, and legitimate future repeatability |
| L04 | Save at a supported boundary with local support pending for a later 095 firing | Valid support persists and committed consumption cannot replay |
| L05 | Save between the two containment or achievement observations | Original cohort and due dates persist, with no fabricated past observation |
| L06 | Equivalent valid occupations with optional DLC enabled and disabled | Same core native addition, with optional partner systems unable to gate it |
| L07 | Many idle days after a wave | No recurring 106 resistance addition or new periodic world scan |
| L08 | Local control, core, or movement callback delivered twice | Idempotent episode invalidation and proof failure, with no cadence advancement by callback count |

## U: Presentation and catalog alignment

| ID | Fixture | Required result |
| --- | --- | --- |
| U01 | Occupier, occupied-homeland, observer, saturated, and empty reports | Truthful context, percentage-point language, and acknowledgment-only option |
| U02 | Main evolution history, related history, and Event Details preview | Correct stage and source names, real dates only in history, no duplicate grants |
| U03 | Long country and state names in supported normal and smaller resolutions | Readable text and correct dynamic substitutions without clipping |
| U04 | Report image and both achievement triplets | Correct native canvases, references, unchanged templates, alpha, filenames, and DDS validation |
| U05 | Current shared name and Details selectors plus the real workbook | 106 Resistance resolves correctly, Domestic Unrest Low is aligned, and the CSVs are generated from the workbook |

## P: Probability and deterministic-threshold handoff

The implementation's probability auditor starts with inspection of the actual source adapter. For comparisons, preserve a real immutable pre-change source and an after source under the identical scenario set. Every normalized selection surface needs its complete candidate pool. These scenario labels do not themselves constitute an engine fixture or a probability result.

| ID | Declared scenario | Expected evidence |
| --- | --- | --- |
| P01 | Shared picker with no valid occupied states, then with one valid zero-resistance occupation | 106 eligibility changes correctly within the complete pool, including its actual weight and recovery state |
| P02 | Fresh 106, recently fired 106, and recovered repeatable weight | Shared pacing and repeat recovery are preserved, with no invented event-specific timer |
| P03 | Domestic Unrest burst with 106 and its related valid members | Exact firing identities and ordering, no duplicate 106 wave or unrequested 095 dispatch |
| P04 | 095 with zero, expired, consumed, and mismatched 106 history | Immutable ordinary candidate, force, fallback, and RNG equivalence where the adapter can establish it |
| P05 | Fixed disjoint candidate pool at each support threshold minus a supported epsilon, exactly at it, and above it | Inclusive 0.10, 0.35, 0.60, and 0.85 bands, correct winning count and tie-break |
| P06 | Counts from zero to more than eight in each band, including equal-count bands | Alternative-band calculation and global eight-extra cap |
| P07 | Overlap and shared-carrier candidates with absent or expiring support | Canonical allocation remains independent of history freshness before scoring |
| P08 | Same footprint under more support, higher resistance, higher compliance, and aging | Formula monotonicity, correct deterministic count, and no false probability label |
| P09 | Any separately implemented 006, 110, or 097 weighted reader change | Owner-specific complete pool and matched before/after evidence, with missing input contracts left unresolved |

Do not call a deterministic support score an uprising probability. The extra branch adds no RNG. Do not turn an AI willingness score into a click chance or a source trace into a live timing result. If a required adapter is unavailable, preserve source evidence and mark that conclusion unresolved in the implementation handoff.

## Final acceptance gate

All fixed user mechanics must pass their relevant native fixtures. The required 095 consumer, local force representation, and exact physical footprint must be implemented and evidenced. Shared log names, evolution views, assets, achievements, and workbook alignment must match the finished behavior.

The final report must distinguish completed source work, actual tool evidence, actual runtime evidence, and remaining gaps. A mathematical oracle or a complete specification cannot be presented as a passed game test.
