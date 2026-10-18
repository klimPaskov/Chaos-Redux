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
