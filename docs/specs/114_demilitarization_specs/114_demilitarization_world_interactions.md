# Demilitarization: world behaviour, Chaos, and balance

All labels are working labels, not final localisation. The numerical values in this document are authored starting targets. Existing shared policies are identified separately.

## Countries should experience different problems

| Country situation | Main pressure | Preferred response and narrative emphasis |
| --- | --- | --- |
| Large continental power with a deep interior | Long relocation distances and forward staging areas lost. | Service conditions and cadre continuity. Writing follows the movement of garrisons inland. |
| Thin or small border country | Little or no remaining domestic military space. | Preserve actual formations through the validated DMZ behaviour. Service choices become expensive relative to resources. |
| Island country without a foreign land frontier | Limited early geographic effect, followed by service discontent and later Total restrictions. | Clear reports that do not invent an initial border. Its wider usable space reduces early pressure. |
| Country with detached possessions | Several separate frontier belts and potentially isolated forces. | Treat each land component honestly. Do not invent a legal transport corridor. |
| Recently peaceful mass army | Expectations of release and interrupted wartime organisation. | Transparent service conditions, cadres, and deliberate consolidation. |
| Small professional army | Loss of a few experienced formations matters greatly. | Cadres first. Full-dissolution size and last-formation guards protect against an arbitrary total wipeout. |
| Country with low stability and existing military unrest | Cohesion can deteriorate rapidly and enforcement can backfire. | Clear risk information and meaningful constructive alternatives where affordable. |
| Subject or faction partner | Friendly borders remain international borders. | Same territorial rule and valid domestic choices. No free exemption through diplomatic status. |

These variants use the same mechanics. Historical and regional context changes the emphasis of the writing and art, not hidden national superiority or permanent immunity.

## Other military crises

### Event 096: Divisions lock

Event 096 owns its army allowance and template-unlock conditions. Event 114 may change the real army size by desertion or lawful consolidation. The owning 096 system can observe that fact through a read-only refresh.

Event 114 must never clear the lock marker, unlock a template, create an allowance, or count entry into war as satisfaction of a separate condition. Apply this rule to opening, reviews, decisions, war callbacks, peace callbacks, save reconciliation, and cleanup.

The inspected Event 096 source currently has a timed template-release implementation. That does not authorise Event 114 to rewrite the independent contract in the current brief. The implementation handoff records the discrepancy and requires reconciliation with the current owner.

### Mutiny and military collapse

An already active military-collapse event can add up to 4 negative cohesion per review and increase evolution pacing pressure. Use the actual owner's state, not a similarly named localisation key.

A severe Event 114 loss or enforcement backlash may submit one pressure receipt to the existing crisis. That owner decides whether its own escalation conditions are met. The same incident cannot be counted repeatedly by both systems.

If both systems can delete or transfer a formation, the first committed owner holds the transaction. The other revalidates and skips the vanished target. A single unit cannot be dissolved twice.

### Resistance and civil unrest

Military desertion does not directly add civilian population or subtract it. A response backlash can affect national stability as specified. Any state-level resistance consequence requires an actual applicable owner, state, and trigger.

Do not convert all living deserters into resistance strength by default. Discontent can provide a connection without claiming that every departing soldier joined an armed opposition movement.

### Other DMZ systems

Communist Lockdown, Resources Found arrangements, vanilla treaty restrictions, and other installed writers can overlap Event 114.

The physical DMZ is the result of all current valid source claims. War suspension removes the Event 114 claim for the belligerent controller. A treaty or another active event can still keep the state restricted.

Preserve existing forts, factories, infrastructure, state ownership, and resources. Do not import the fort-destruction or resource-allocation rules of another event merely because it also uses a DMZ.

## Peace cluster

Use the existing Peace cluster, ID 4, with Event 114 as a High-severity optional member that can act as the initiating selected member. When 114 is the valid trigger, its own participation is assured through the shared trigger-member policy. Its inclusion in a burst initiated elsewhere follows the existing High-band participation rules.

The catalog's Chaos level 1 and High member severity describe different things. Preserve Event 114's ordinary entry requirement. Preserve the current shared High-severity cluster floor, which the inspected constants set at tier 2. Do not silently raise standalone entry to that floor or lower the shared cluster floor.

A Peace burst must be possible when an eligible 114 member is selected and no White Peace settlement exists. Prepare runtime context for the actual selected members. A missing settlement candidate skips the settlement member. It must not erase a valid peacetime demilitarization context.

This is a concrete integration change. The inspected Peace setup currently prepares a White Peace context unconditionally. It must become member-scoped. The current repository has two White Peace logical rows, while the supplied CSV lists five legacy rows. Reconcile the live definition and canonical workbook instead of copying the CSV list.

When White Peace occurs before 114 in a valid burst, the resulting actual last-war peace transition can make countries eligible for demilitarization. Revalidate at dispatch. A country still fighting another war remains suspended.

One cluster burst uses the shared pacing and logging contract. Do not charge an additional Event 114 selection cost or invent a cluster-wide Chaos bonus for the same incidents.

## Chaos impact map

Chaos reflects the abnormal military consequences. A formal evolution milestone, selection roll, or status refresh has zero direct effect.

The map below is the full Event 114 direct contribution model. Generic war, peace, military buildup, annexation, and Deaths effects remain owned by their shared systems.

| Milestone or outcome | Why Chaos changes | Direction and starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | --- | --- | --- | --- |
| First material territorial manifestation | Peaceful military deployment becomes subject to a worldwide abnormal rule. | +3 for one affected country, +10 for 2–9, +20 for 10 or more. | Count countries with at least one state physically newly restricted by 114. | One global first-manifestation receipt. | Pre-existing DMZs do not count as new physical restrictions. | Territorial suspension by war is not containment. |
| First material Deeper expansion after opening | The restriction reaches a new interior layer. | +3 for 1–2 newly affected countries, +5 for 3 or more. | Count countries gaining at least one physically new DMZ state. | One global receipt for this expansion footprint. | No separate charge for stage activation. | Stable service recovery can reduce the military breakdown contribution, not erase this territorial fact. |
| First material Total expansion after opening | The remaining national military geography contracts sharply. | +5 for one country, +10 for 2–9, +15 for 10 or more. | Actual added physical restrictions, not countries already fully covered. | One global receipt. | An opening already at Total uses the opening charge only. | Same territorial rule as above. |
| Accumulated measured desertion reaches a national milestone | A meaningful part of the real fielded army has left service. | +2 for a minor, +3 for a major. | Partial-desertion receipts total at least 5% of that country's enrolment manpower and at least 1,000 actual departures within 180 days. Full dissolutions are excluded from this milestone. | Once per country per campaign. | No Deaths charge for living deserters. | Eligible sustained recovery may reverse this own charge once. |
| First spontaneous formation dissolution in a country | A real military formation ceases to exist through service collapse. | +3 for a minor, +5 for a major. | Requires the committed full-dissolution receipt and actual loss. | Once per country, with a global direct-dissolution cap of +15 per rolling 180 days. | A unit removed by another crisis receives no 114 charge. | M114-02 can reverse up to 2 of this country's unreversed 114 charge. |
| Durable recovery after a charged personnel or formation loss | Cohesive service and a substantial army are restored. | −2, limited by that country's unreversed eligible direct charge. | M114-02 complete or the equivalent recovery after a charged personnel milestone. | Once per country per 180 days, with each original charge consumed at most once. | Generic peace reductions remain separate. | A new loss requires a new legitimate receipt and its own applicable guard. |
| Repetition, war suspension, peace restoration, programme purchase, or evolution logging | These operations alone do not establish a new abnormal consequence. | 0 | Material effects can separately meet a row above. | Transaction identity. | Avoid duplicate generic war and peace effects. | No automatic refund. |

When the first firing is already evolved, combine its simultaneous territorial changes into one opening transaction and one opening charge. Mark the included territorial milestones as already represented, so a later callback cannot bill the same footprint again.

The same precedence applies when the first material manifestation was deferred. The first later transaction that actually restricts territory receives the first-manifestation charge. Any Deeper or Total footprint created by that same transaction is marked as represented by that charge. It cannot receive a second territorial charge under a different row.

If an opening adds only overlapping claims, defer its first-material receipt until Event 114 actually makes a state newly restricted. Do not count a state once per neighbouring country.

Apply a combined global cap of +30 per rolling 180 calendar days to the country-level partial-desertion and full-dissolution sources. The full-dissolution subset also retains its +15 cap. An exhausted cap never prevents the actual military consequence. Mark the milestone observed with its actual charged amount, which can be zero, and do not queue a deferred charge. A later recovery can reverse only an actual eligible charge. Territorial manifestation and expansion use their separate one-time receipts.

Use the shared Chaos change and history path, including its disabled-meter and upper-state behaviour. The event does not bypass a shared clamp or meter lock. Reports must distinguish an attempted mapped charge from the actual applied shared result.

For a recovery reduction, select the oldest unreversed eligible actual charge covered by the completed objective, with the stable receipt identity breaking a same-date tie. Request at most 2 points and never more than that charge's actual unreversed amount. One successful reduction consumes that original charge's whole recovery eligibility, even when part of its historical positive contribution remains. There is no reusable remainder from that charge. If the shared path applies zero reduction, record that result and retire this completion's submission without repeated callbacks. A later independently earned recovery completion may use the still-unreversed charge. The 180-calendar-day country reversal cooldown starts only on an actual reduction. Never manufacture an entitlement from a requested positive charge that the shared meter did not apply.

## AI policy

The AI receives the same information, costs, cooldowns, and eligibility as the player. It must not need a popup option with a default that accidentally dissolves a formation.

Priorities are ordered, then resolved among valid choices:

1. Handle an endangered formation when a valid cadre programme can finish by the deadline.
2. Improve service conditions when sustained deterioration can be addressed industrially.
3. Consolidate an actually depleted formation when fragmentation is the main problem and the sacrifice is affordable.
4. Enforce attendance only when immediate breakdown outweighs the stated political risk.
5. Preserve resources when cohesion is stable and no response has a meaningful benefit.

Use one authored country-worker chooser containing the four action families and an explicit wait outcome. Normalise its valid weights for one selection per reconsideration. These are this custom pool's authored weights, not native decision-click probabilities. A resource shortage or invalid unit sets the action's weight to zero before selection. Re-evaluate at execution and call the same paid, guarded action path used by the player. A failed revalidation ends that reconsideration without a second draw or substitute target.

For cadre targets, choose the valid endangered formation when one exists and completion can meet its deadline. Otherwise choose the valid formation with the greatest verified service age, breaking ties by actual manpower and then stable identity. For consolidation, prefer the valid endangered formation. Otherwise choose the lowest ratio of current actual manpower to its verified 90-day high, breaking ties by lower actual manpower and then stable identity. Conditions and enforcement are country actions. Commit at most one action per reconsideration, even when the instant consolidation leaves the programme slot free.

Evaluate policy at enrolment, a review, an urgent notice, and programme completion or cancellation. While idle with cohesion below 75 or an open notice, schedule at most one additional country-local reconsideration every 7 accumulated peacetime days. Stop that callback during war or an active programme.

Wait has weight 20 at cohesion 75 or more, 6 at 45–74, 2 at 25–44, and 1 below 25. If an open notice has any affordable response that can meaningfully settle it, wait has weight 0. If every action is invalid, wait is the sole outcome. When cohesion is at least 75, no notice exists, and the next review under current known contributors would remain at least 75, all spending weights are 0. This overrides the calm row and prevents purposeless purchases.

| Situation | Starting relative policy weights: conditions / cadres / consolidation / enforcement | Intended behaviour |
| --- | --- | --- |
| Cohesion at least 75, no notice | 1 / 1 / 0 / 0 | Mostly wait. Act only when a real forecasted decline or vulnerable cadre justifies it. |
| Cohesion 45–74, no notice | 6 / 3 / 2 / 0 | Prefer sustained constructive management. |
| Cohesion 25–44, no notice | 5 / 5 / 4 / 2 | Use resources or reduce fragmentation before severe state. |
| Below 25, valid notice with time for cadres | 2 / 12 / 6 / 4 | Protect a real endangered unit. |
| Below 25, notice cannot be met constructively | 1 / 0 / 8 / 10 | Weigh a controlled sacrifice against political backlash. |
| Stability below 35% | Enforcement weight multiplied by 0.25. | A fragile government should understand the risk it creates. |
| No industrial capacity | Conditions weight 0. | No fictitious paid programme. |
| No valid depleted unit | Consolidation weight 0. | No token-unit invention. |
| Country at war | All peacetime programme weights 0. | No peacetime spending or losses. |

These are policy starting points, not a claim that their probabilities have been evaluated. The probability audit must inspect the actual nesting, modifiers, timing, and validity filters.

The event does not direct the AI to fabricate wars to escape demilitarization. Its ordinary geopolitical strategy remains responsible for war decisions.

## Balance questions to answer in implementation

The base rule is already powerful for compact countries. Do not add a flat national penalty before Desertion Crisis simply to make the opening feel busy.

The one-hop belt should materially affect forward deployment. If geography is wrong, stronger modifiers will not repair the event. Validate land connections and inward depth before tuning the army effects.

Desertion should be visible over several reviews. The first severe formation crisis must allow a real response interval. Full dissolution is rare, capped, and targeted. Partial losses can still become significant across a sustained service collapse.

Industrial spending should be a viable stabiliser for a medium army. Cadre retention should be competitive when a valuable formation is threatened. Consolidation should be attractive when the player accepts a smaller army. Enforcement should produce a distinct short-term benefit and a real aftermath.

War deliberately releases geography and service penalties. The military damage remains because personnel and formation identity have their own histories. This is the central tradeoff, not an exploit to be patched away.

## Required probability scenarios

| Scenario | What must be inspected or evaluated |
| --- | --- |
| One, ten, and one hundred eligible formations at the same total manpower | Splitting cannot increase total expected loss or duplicate selection. |
| Cohesion immediately above and below 70, 45, and 25 | Correct band and pressure ordering, with no double review at a boundary. |
| Service programme and enforcement active in separate runs | No illegal programme stacking and correct conditional chance. |
| No eligible divisions | No random draw with an empty pool, no loss, no award. |
| Endangered formation and 13 days remaining | Feasibility-aware AI and one due outcome. |
| Two short wars between reviews | Remaining peace clock preserved, with no catch-up losses. |
| Chaos 199/200, 399/400, and 799/800 | Exact live evolution eligibility and enabled-stage handling. |
| Evolved first opening | One initialisation, one first review interval, and no triple Chaos charge. |
| Peace cluster without settlement targets | Valid 114 runtime context and honest unavailable settlement members. |
| Repeat under the 180-day guard | No extra cohesion shock or hidden roll. |
| Low stability enforcement | One committed backlash draw, no reload or callback reroll. |
| Many countries dissolve formations in one period | Correct global Chaos cap without suppressing the actual military outcomes. |

Use inspect, evaluate, sweep, compare, render, and sequence tools as appropriate to the implemented surface. Simulation answers timing and outcome-distribution questions after exact eligibility and accounting are correct. It cannot establish native unit-mutation semantics.

