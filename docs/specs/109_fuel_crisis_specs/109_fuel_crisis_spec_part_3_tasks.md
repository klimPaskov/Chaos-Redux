# Fuel Crisis: the Tasks connection

## A challenge drawn from the real shortage

Event 101 may use Fuel Crisis as context for a timed objective while a selected player country is recovering. It can ask the player to rebuild a usable reserve or secure a dependable oil source. Event 101 owns selection, assignment, progress, deadlines, success rewards, failure consequences, and cleanup.

The earlier Tasks brief explicitly limits assignments to players. In singleplayer, its selected recipient is the player. In multiplayer, Event 101 selects one valid player-controlled country under its own rules. Fuel Crisis does not change that recipient selection or assign a mission to every affected country.

The connection is a defined integration contract. The supplied Tasks catalog entry and prior brief do not establish a runtime API. Targeted repository inspection did not locate an implementation to bind. Both objective templates therefore remain implementation dependencies until the Event 101 owner and the necessary native measurements are verified.

The core world wipe can be implemented independently. The complete requested connection must still be reported as pending if either its required owner lifecycle or its selected measurement path is missing.

## How a Fuel Crisis objective enters the pool

The following are proposed starting selection rules:

1. A successfully committed Fuel Crisis occurrence supplies a receipt and an onset date to Tasks.
2. Event 101 follows its ordinary trigger, enabled-state, player-selection, active-task limit, diversity, and crisis-family rules.
3. For its already selected player, it may consider Fuel Crisis candidates during the first 90 days after the occurrence.
4. The country must have belonged to that occurrence, lost a positive reserve, and still have a meaningful fuel recovery or supply gap.
5. At least one ordinary action must be both achievable and measurable under the selected template.
6. At most one Fuel Crisis task may be issued to a country for that occurrence. There is never more than one active Fuel Crisis task for that country.

There is no guaranteed Fuel Crisis assignment. If the selected player is ineligible, Event 101 uses another appropriate objective or its own no-valid-task behavior. It does not reroll the multiplayer recipient merely to find a country that can receive this connection.

The 90-day period is an offer window. It is not a production penalty or a deadline for national recovery. An assigned task receives its own full calculated duration. Finishing a task does not reopen eligibility for another task from the same occurrence.

## Shared measurements and frozen values

All rate quantities below use a common **fuel-equivalent per game day**. This is a semantic unit for the specification. It is not an asserted engine accessor. Raw oil resource units, fuel stored in thousands, nominal imports, and actual fuel output must not be added together without a verified conversion.

| Symbol | Meaning and capture time |
| --- | --- |
| D0 | Meaningful daily fuel demand implied by the country's active commitments immediately before the wipe |
| C0 | National fuel capacity immediately before the wipe |
| F0 | Positive national stored fuel immediately before the wipe |
| S | Actual national stored fuel at task assignment |
| J0 | Dependable recurring usable fuel inflow at task assignment, before military consumption |
| Da | Daily demand implied by active commitments at assignment, measured independently of starvation-limited actual consumption |
| Ca | Actual national fuel capacity at assignment, used to bound the refill projection |
| A | Feasible lead time from assignment until the selected ordinary action can take effect |
| D1 | Sustainable demand expected after the selected action |
| J1 | Dependable usable inflow expected after that action |
| Q0 | Assignment-time delivered fuel-equivalent flow from a selected oil source |
| Jother | Assignment-time dependable inflow excluding that selected source |

Tasks must use a documented demand measurement that is not merely the post-wipe collapse of actual consumption. Fuel starvation can reduce observed use even when the player changes no orders. That reduction is not evidence of a conservation action.

Capture D0, C0, and F0 once during the already required onset pass when the verified Tasks integration is present. Their use must not delay or limit the unconditional world wipe. They are private context. The country should not gain a second visible fuel meter.

At assignment, freeze the target, selected action contract, source identity where needed, deadline, and difficulty inputs. Later silos, orders, trade changes, or UI refreshes must not silently move the target. Current fuel and delivered supply remain live measurements.

If the installed game and Event 101 cannot provide a required quantity accurately, that candidate is unavailable. Do not replace an unknown demand with zero, infer delivery from a diplomatic promise, or quietly treat nominal oil units as fuel.

## Template A: rebuild a usable reserve

The working identifier is **fuel reserve recovery**. It is a role label, not final localisation.

The country must take one qualifying ordinary action and rebuild the frozen reserve target. Tasks chooses an observable feasible action route when assigning the objective:

| Action route | Required change | Evidence rule |
| --- | --- | --- |
| Conservation | A deliberate change reduces sustainable demand to at most 80% of both D0 and Da | Require a meaningful post-assignment reduction from current commitments as well as the onset reference. An observable activity change must distinguish player action from automatic fuel starvation |
| Supply improvement | A new or expanded ordinary supply arrangement creates a meaningful usable inflow increase | Measure an actual post-assignment improvement with a verified source or delivery predicate |

These routes are alternative ways to satisfy the same reserve template. They are not additional missions. A route that cannot be observed reliably must not be offered. For example, a supported supply measurement can enable a reserve task even when native order changes cannot be attributed safely.

The conservation action threshold is `min(0.8 × D0, 0.8 × Da)`, frozen at assignment. Requiring the reduction from Da prevents an already reduced pre-assignment operating tempo from earning credit through a token change or increased activity. Both demand measurements describe commitments that would use fuel if supplied.

For a supply-improvement route, the proposed minimum increase is 25% of D0 in recurring usable fuel-equivalent flow. A one-off gift or stockpile injection does not satisfy that continuing-supply condition. Ordinary assistance may still help the player meet the reserve quantity if the underlying rules allow it.

The reserve target is:

**R = minimum of 14 × D0 and 50% × C0.**

Require D0 to be positive and C0 to be at least 14 × D0. This makes the selected target worth between seven and fourteen days of the frozen reference demand. The capacity cap avoids requiring every country to fill a large empty storage system.

Current capacity must also be able to hold R at assignment. Stored fuel must be below R. The feasible action must create a positive projected refill balance.

Success requires the qualifying action to remain effective and stored fuel to remain at or above R through a seven-day observed hold. The fuel is retained. There is no fuel payment when the mission succeeds.

The reference target stays fixed when the player later reduces consumption. Conservation is an intended recovery strategy. The active-action and feasibility gates prevent unchanged passive refill from being mistaken for a deliberate task solution.

### Excluding automatic recovery

Use the no-action forecast based on Da and dependable inflow J0 at assignment, with D0 retained as the scaling reference. When J0 is greater than Da, forecast the remaining reserve gap at that positive rate. A nonpositive balance does not forecast automatic recovery. Never substitute starvation-limited actual consumption for Da.

If unchanged play is expected to reach R within 60 days and no active intervention is needed, skip this reserve candidate. Also skip it if the player has already made the required intervention before assignment and the remaining objective is only to wait for its result. The task is drawn from a present decision, not awarded retroactively.

This gate must use reliable measurements. An uncertain forecast is not evidence that a country needs a difficult task.

## Template B: secure dependable oil access

The working identifier is **delivered oil access**. It is a role label, not final localisation.

Select an existing, reachable source opportunity from the real campaign. It may involve establishing a new normal trade route, expanding an existing one, restoring a disrupted source, or making an already available domestic oil source usable through an ordinary supported action. Tasks must identify what the player can do and verify that the action is legal and achievable for this country.

The objective requires a post-assignment source action and actual usable oil delivery. Relations, a signed agreement, nominal trade allocation, a new refinery icon, or ownership of an oil state alone are insufficient.

The selected source's proposed target is:

**Qtarget = maximum of Q0 + 25% × D0, and D0 − Jother + 10% × D0.**

This requires a material improvement over the selected source's existing flow. It also asks the source to close the assignment-time supply deficit with a modest buffer. The target is fixed after assignment.

Require positive D0 and `Q0 + Jother < 1.10 × D0`, using the same assignment-time fuel-equivalent-per-day units as Qtarget. A country that already has a dependable operating margin does not need this particular challenge.

The selected source must deliver at least Qtarget for a fourteen-day observed hold before the task deadline. Its actual delivered oil must have increased or become newly usable through the chosen action. An unrelated technology change must not count as proof that the player established the required oil access.

The conversion from delivered oil to usable fuel-equivalent output must use the supported game rules, including the relevant production factors. If only a nominal contracted-oil value can be read, this template stays unavailable until actual delivery can be established.

Completing this objective proves that the selected source met its contract. It does not certify that every later operation or unrelated supply loss will remain sustainable.

## Dynamic deadlines

Deadlines are calculated for the selected objective. The following tuning is proposed for this small crisis connection:

| Parameter | Starting rule |
| --- | --- |
| Earliest normal cutoff | 90 days after assignment |
| Latest Fuel Crisis task cutoff | 180 days after assignment |
| Forecast uncertainty margin | 30% on both reserve action lead and refill time, or on oil-source action lead |
| Reserve hold | Seven observed game days |
| Oil delivery hold | Fourteen observed game days |
| Presentation rounding | Round the calculated duration upward to a multiple of five days |

The floor follows the current mission guidance and still allows immediate progress and early completion. The cap keeps these crisis-specific assignments close to the original recovery problem. A longer development project can remain an ordinary strategic response or belong to another Tasks family. Do not shorten an infeasible forecast to fit the cap.

For the reserve template, calculate the expected stock at the time the action takes effect as `min(Ca, max(0, S + A × (J0 − Da)))`. This uses assignment stock, the selected lead time, and the commitment-based no-action balance, bounded by the native storage floor and assignment capacity. It is a planning forecast rather than a replacement engine fuel calculation.

Let **G = max(0, R − projected stock)** be the remaining nonnegative gap to R. Let **N = J1 − D1** be the sustainable post-action refill rate. Reject the candidate if N is not positive or if the action cannot realistically produce the assumed rate.

Let **B** be the number of days required to accumulate G at rate N, rounded upward. Calculate the duration as:

**Reserve duration = round upward to five days of max(90, 1.30 × (A + B) + 7).**

The 30% reserve margin covers both achieving the action and accumulating the remaining fuel. The seven-day hold is added afterward. This avoids treating an uncertain action lead as guaranteed while padding only refill time.

For the oil-access template, let A include the entire plausible lead to real delivery, including access work or a selected construction project where relevant. Calculate:

**Oil-access duration = round upward to five days of max(90, 1.30 × A + 14 + 7).**

The final seven days in the oil calculation provide a completion margin. Reject either candidate if its rounded duration exceeds 180 days. Also reject forecasts that depend on an impossible purchase, unavailable construction, guaranteed enemy cooperation, an unverified conversion, or an assumed victory outside the player's realistic reach.

Event 101 owns any difficulty or stakes scaling. Recheck feasibility after that scaling and freeze the resulting contract once. A later change to Tasks difficulty must not silently rewrite an active mission.

## Worked calibration examples

The examples use invented rates. They validate the proposed arithmetic and its interpretation, not native game behavior.

| Case | Inputs and calculation | Result |
| --- | --- | --- |
| Reserve recovery under a small deficit | D0 = Da = 100, C0 = Ca = 3,000, S = 200. R = 1,400. J0 = 90. A seven-day lead projects stock of 130. Conservation gives D1 = 80, J1 = 90, N = 10. The gap is 1,270 and B = 127. The duration is 1.30 × (7 + 127) + 7 = 181.2 before rounding. | 185 days. Reject this forecast above the cap, rather than shorten the task. |
| A feasible upper-bound response | Same deficit, target, and action outcome, with a feasible five-day lead. Projected stock is 150, G = 1,250, and B = 125. The duration is 1.30 × (5 + 125) + 7 = 176 before rounding. | 180 days. This candidate can proceed if action and rates are observable and feasible. |
| Faster reserve response | Same D0, Da, C0, Ca, S, and seven-day lead, but J0 = J1 = 100. Projected stock stays 200. D1 = 80 gives N = 20 and B = 60. The duration is 1.30 × (7 + 60) + 7 = 94.1 before rounding. | 95 days after rounding. The stronger balance changes the deadline. |
| Conservation cannot solve the deficit | D0 = 100 and J1 = 70, with D1 = 80. | Negative refill forecast. Reject that action route. A separately feasible supply route may still qualify. |
| Already recovering without action | R = 1,400, S = 200, usable inflow = 130, current demand = 100. | No-action refill takes 40 days. Skip the reserve task. |
| New oil source | D0 = 100, Q0 = 0, Jother = 70. Qtarget = max(25, 40) = 40. Source lead A = 100 days. | 155-day deadline after the margin and hold. |
| Small capacity | D0 = 100, C0 = 1,400. | R = 700, a seven-day reference reserve. The minimum capacity gate passes. |
| Insufficient capacity | D0 = 100, C0 = 1,000. | Reject the reserve template. A feasible oil-access template can still be considered. |
| Excessively long source project | Source lead A = 150 days. The calculation is 195 + 14 + 7. | 220 days after rounding. Reject this Fuel Crisis candidate instead of forcing a 180-day timer. |
| Commitments already reduced before assignment | D0 = 100 and Da = 60. A new conservation action must reach at most min(80, 48) = 48. | Increasing demand to 70 or making a token reduction to 59 cannot earn a conservation task. An independently feasible supply route can still qualify. |

The formulas scale through actual demand, storage, supply, and feasible action time. They do not require a universal major-power stockpile target or an arbitrary country whitelist.

## Hold evaluation and the deadline boundary

Use Event 101's verified progress evaluator. The starting contract uses daily observations for active missions only. It does not request a new Event 109 country scan.

The first qualifying observation starts a hold at zero elapsed days. Seven complete observed intervals require that observation plus seven subsequent daily confirmations. Fourteen intervals require fourteen subsequent confirmations. A failed condition resets the hold. A missed interval cannot be inferred from the current stock or filled in from a loaded save.

The display and tooltip must describe this observed daily hold accurately. Do not claim that daily samples prove every intraday value. If Event 101 already supplies a stricter validated continuous hold, it may satisfy this contract without weakening it.

The original assignment cutoff remains authoritative. A success already recorded before expiry wins over a later timeout callback. At a final permitted evaluation, evaluate the complete success contract first and resolve it once if still within the permitted cutoff. An observation after the cutoff cannot rescue an expired task.

The implementation must document its exact native date and tick convention, synchronize the displayed mission timer to the stored cutoff, and test the final permitted observation and the first expired observation. A UI countdown must not disagree with the owner resolver.

## Success, failure, and cancellation

| Outcome | Event 101 behavior | Event 109 behavior |
| --- | --- | --- |
| Valid timely success | Resolve once through the selected task's normal reward path, using its frozen difficulty | No extra fuel grant or second reward |
| Deadline missed | Resolve once through the normal consequence path, scaled to the task and survivable as an ordinary task failure | No new wipe or follow-up drain |
| Reserve or delivery falls during a hold | Reset the observed hold while the original deadline continues | No event-level escalation |
| Ordinary wartime disruption or player inaction while retaining control | Apply the original task's risk and deadline rules | No automatic cancellation that erases a foreseeable failure |
| Country ceases to exist | Neutral cancellation and cleanup | No transfer of the task or achievement provenance to a successor |
| Player relinquishes the country to AI | Neutral cancellation at the Tasks owner's next validated lifecycle check | No AI task continuation or reward |
| Tasks is disabled or the objective becomes technically invalid | Neutral cancellation under the owner lifecycle | Core historical wipe remains complete |
| Duplicate delivery of the same Fuel Crisis receipt | No new assignment or reset | No new world write |
| A deliberate fresh forced occurrence replaces the crisis context | Neutral cancellation of an active task from the old context, then normal new-context eligibility | One new admitted wipe |

Losing a source to a foreseeable campaign risk is different from a missing script definition or disabled feature. The former can lead to ordinary task failure. The latter must not punish the player for an invalid contract. Self-created inability to complete a task must not become a reward-free reroll.

Task completion consumes its active record before reward or penalty dispatch. A repeated callback must find no unresolved contract. Native timeout and any recovery resolver must share that same terminal guard.

Rewards and consequences come from Event 101's logistics or crisis task rules. This package supplies the outcome category, effort, exposure, and causal receipt. It does not invent a second reward table or claim that uninspected reward functions already exist.

## Persistence and eligibility changes

Save and load preserve the occurrence receipt, recipient, chosen action, target, deadline, hold evidence, and terminal disposition. Loading cannot refill fuel, rerun the wipe, extend time, reconstruct missed hold intervals, or issue a second task.

A country created after impact is ineligible for this occurrence. A country that existed at impact and later comes under human control can be considered only if its original valid context is available and the ordinary Tasks selector allows it. An eliminated and later recreated country must not inherit an old active contract.

The offer context can expire through its stored date and the Tasks owner's normal lifecycle. Old context must never reactivate because a displayed flag disappears, a global initializer reruns, or a country tag is reused.

Once the offer window closes, Event 109 needs no continuing recovery monitor. Active tasks continue through Event 101. Their records are cleaned at resolution while the minimum terminal and achievement provenance remains with its proper owner.

## Player information

An assigned task should show its chosen objective and action route, the target, observed hold progress, and deadline through the existing Tasks interface. Use no more than three primary numeric groups: target or current progress, hold progress, and time remaining. Existing fuel information remains the place for detailed rates and military consumption.

The tooltip can explain the frozen baseline, the required real action, why nominal trade is insufficient, and what happens on success or failure. It must distinguish a held reserve from a fuel cost. Native trade and construction costs stay on their existing actions.

Localisation is written during implementation. This specification supplies meaning and exact conditions only.

## Integration acceptance

The connection is ready for implementation only when the owner can:

- Receive or read a committed occurrence without triggering Tasks from inside the fuel sweep.
- Preserve the player-only selector and issue at most one Fuel Crisis task per country per occurrence.
- Produce at least one truthful, active, feasible template from verified inputs.
- Freeze its contract and synchronize the native timer.
- Evaluate the declared hold and resolve success, failure, or neutral cancellation once.
- Preserve and clean the right state across saves, country changes, feature disablement, and force replay.

Each unsupported template or action route must remain visibly pending in the implementation report. A working oil objective does not prove that a conservation predicate also works. A working core wipe does not prove that the accepted Tasks connection has shipped.
