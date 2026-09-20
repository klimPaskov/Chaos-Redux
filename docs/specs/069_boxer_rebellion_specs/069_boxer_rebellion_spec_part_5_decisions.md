# Decisions and their costs

The catalog below defines action families, not forty-six buttons shown together.
All action labels are implementation-facing working descriptions.
Final player-facing titles, descriptions, and tooltips must be written and reviewed during implementation.

## Common action contract

An action validates its actor, target, current phase, ownership relationship, resource bill, route, cooldown, and existing objective before payment.
The same validation is used by the visible decision, any event confirmation, and the AI path.
Payment and activation occur once in one reviewed operation.
A stale target cannot receive a second payment, create a second mission, or deliver a reward to its former owner.

An operation can reserve equipment or transport, spend consumables, or commit an existing formation.
The interface must distinguish those cases.
Unused reserved assets are released when an operation is cancelled.
Delivered assets belong to their recorded recipient or allocation.
Destroyed, captured, or genuinely consumed assets are not refunded.
A change of stance or country tag cannot duplicate any of those assets.

Each action has at most four distinct spendable or committed cost types.
Command Power never exceeds 60 per action.
The cost line shows no more than three inline quantities, with the complete bill in the tooltip and confirmation when needed.
A prerequisite, such as controlling a port, is not a hidden payment.
An exclusive force commitment is a real opportunity cost and counts toward the four-type limit.

## Scaling notation

`S` is a local operation scale, normally between 0.25 and 2.00.
Calculate it from the target's opening population band, the size of the threatened operation, and the required route, then round to a 0.05 step.
Lock the reference population and objective identity for the operation so that migration, recapture, or reopening a menu cannot reroll its price.
The initial balance model takes the square root of the ratio `target_population / locked_median_population`, rounds to the nearest 0.05 with ties upward, and clamps the result to the stated interval.
Both population inputs must be positive and must be locked before the bill is quoted.
This is a design formula, not proposed Clausewitz syntax.
Route requirements can replace that scale when a convoy or garrison operation has a better physical bill.

Equipment examples such as `100S support equipment` are rounded upward to a usable quantity, normally a multiple of 5.
Indivisible factories, trains, convoys, formations, and engine-calculated template bills use whole units.
Those physical counts are documented exceptions to the multiples-of-five tuning preference.

`C` is a temporary civilian construction commitment calculated as 10% of available civilian factories, rounded upward to a whole factory, with a minimum of one and maximum of five factories.
Availability is checked after other commitments.
A country with no available capacity must free capacity or choose another action.
Implementation must verify how the current project actually reserves that capacity before exposing the bill.

`Template bill` means the real remaining manpower and equipment requirements of the selected verified template.
It never means a second full bill for a formation that already exists.
`Transport` means the required convoys or land transport for the selected route, not both unless the actual route needs both and the action still fits the cost budget.

## Chinese government actions

| ID and working action | Cost and timing | Conditions, effect, failure, and AI |
| --- | --- | --- |
| D01 Suppress the movement | 50 Political Power for a later policy change. Initial stance is free. 90-day policy commitment | Available to a government with authority in an affected region. Opens security and disarmament operations. It provides no instant Strength reduction. AI prefers it when it can protect sites and defeat local networks without abandoning an essential foreign front. |
| D02 Tolerate local societies | 25 Political Power for a later change. Initial stance is free. 90-day commitment | Suspends general repression without granting formal command. Local societies gain room to organize. Repeated attacks make denial less credible. AI uses it when immediate suppression is too costly and a controlled accommodation is still plausible. |
| D03 Declare support | 50 Political Power for a later change. Initial stance is free. 90-day commitment | Creates a public political relationship and opens D09 and D19. Arms and units are not granted by the declaration. Interested foreign powers reassess the responsible government. AI rejects the action when it cannot support the compact or cannot legally break an incompatible patron relationship. |
| D04 Protect a threatened district | 15 Command Power, 50S support equipment, and 25S trucks. 30-day preparation or immediate commitment to an active emergency | Requires an actual protection force or a supported local security institution. Opens M01 or M02. Successful protection reduces Pressure for the resolved threat. Losing access leaves a partial or failed mission, with assets accounted for at the site. |
| D05 Interdict an armed network | 15 Command Power, 25S support equipment, and 2500S fuel. 30-day preparation, 60-day local cooldown | Requires controlled approaches and a valid network. Interrupts a named recruitment or delivery route while an operation is maintained. It does not remove unrelated networks or civilians. AI selects routes that materially sustain an armed center. |
| D06 Negotiate local disarmament | 35 Political Power and 50S support equipment for an agreed support package. 90-day verification | Requires a society willing to bargain and a government able to honor the terms. Opens M04 or M05. Surrendered arms come from an existing allocation. Breach by either side restores the unresolved dispute without recreating the original equipment. |
| D07 Investigate an incident | 25 Political Power and 25S support equipment. 30 days, once per incident | Resolves attributable evidence, identifies a responsible network, or records genuine uncertainty. It cannot always exonerate the payer. AI prioritizes investigations when disputed responsibility blocks a useful agreement. |
| D08 Restore a railway connection | C civilian factories, 5S trains allocated to the route, and 100S support equipment. 90 days | Requires a damaged or interrupted real connection and access to the work sites. Opens M03. Completion repairs only the recorded damage or restores the agreed service. Lost access pauses or fails the project without granting new building levels. |
| D09 Supply an affiliated society | 20 Command Power, 500S infantry equipment, and 100S support equipment. Delivery normally takes 30 to 60 days | Requires an accepted recipient and a valid delivery path. The shipment is debited once, then delivered, delayed, captured, or lost. Successful initial deliveries strengthen the compact. Repeating deliveries maintains forces but does not repeatedly award the initial political gain. |
| D10 Organize civilian relief | Proposed land bill of 100S support equipment, 25S trucks, and 2500S fuel, reconciled with the verified shared relief provider. 90-day ordinary project | Uses the shared famine and relief system. Sea delivery replaces the land route with a verified transport bill, keeping at most four cost types. Opens M14 where reconstruction is needed. No duplicate food or refugee pool is created. |
| D11 Withdraw recognition from auxiliaries | 50 Political Power and 20 Command Power. 90-day demobilization process | Requires an existing compact. Opens M05 with integration, disarmament, or negotiated separation choices. Units do not disappear on click. AI chooses it when attacks or command refusal outweigh the military value of the relationship. |
| D12 Offer a foreign protection guarantee | 50 Political Power. 90-day verification | Names the protected site and the guarantee's limits. Opens M02 and a diplomatic counterproposal. Completing the guarantee can satisfy a foreign demand. Repeated promises without protection do not reduce Pressure. |
| D13 Replace a compromised local administration | 50 Political Power and C civilian capacity for 90 days | Requires actual control and a documented authority dispute. Opens a local settlement with officials, societies, and civilian interests. It can remove a grievance while preserving central authority. AI avoids it during a battle it cannot afford to disrupt. |

## Boxer and affiliated-movement actions

| ID and working action | Cost and timing | Conditions, effect, failure, and AI |
| --- | --- | --- |
| D14 Raise a local militia formation | Verified template bill. Proposed 60-day training period, with local capacity recovery over 90 days | Requires eligible local recruits, arms, supply, and a safe deployment site. A government sponsor or the Boxer country owns the formation through one explicit path. No anonymous global manpower grant occurs. AI respects reinforcement needs and avoids raising more unsupported units. |
| D15 Contest a military depot | 20 Command Power and 50S support equipment for the operation. A 90-day objective | Requires a registered depot allocation and a credible military route. Opens M07 where territorial action is required. Captured equipment is a finite transfer. Failure cannot produce a second hidden stockpile reward. |
| D16 Regularize an existing formation | 25 Command Power plus the verified reinforcement difference, using at most three equipment or manpower types. 90 days | Converts or retrains an actual formation through a supported engine path. Preserves its identity and removes its earlier allocation before applying the new bill. AI prioritizes a sustainable core army over conversion of every militia at once. |
| D17 Conclude a civilian protection compact | 35 Political Power and 100S support equipment. 90-day verification | Commits the society to protect named communities and routes. Opens M02 or M17. Genuine compliance reduces a specific source of Pressure and improves government cooperation. Violations suspend the benefit and create a leadership dispute. |
| D18 Convene regional delegates | 75 Political Power and 20 Command Power. 90-day organizing process | Requires several functioning societies and contact between them. Opens M10. It can establish regional command under Evolution I or a smaller ordinary compact without that evolution. AI waits until delegates and routes can actually participate. |
| D19 Accept an auxiliary compact | 35 Political Power. 30-day agreement, followed by M05 | Requires a valid Chinese sponsor and negotiated command terms. Units and equipment follow the agreed ownership path. Refusal preserves independent organization. Acceptance does not automatically annex the Boxer country or surrender all local political authority. |
| D20 Prepare a ritual school operation | 20 Command Power and 50S support equipment assigned to training and medical support. 30-day preparation, 90-day school cooldown | Requires an enabled and revealed Evolution II school, a supplied eligible formation, and its specific operational conditions. Activates one bounded rite from Part 7. It never restores dead soldiers or replaces ammunition. |
| D21 Enforce command discipline | 25 Command Power and 100S support equipment. 60-day program | Targets an actual command dispute or a failed compact. Can restore cooperation, replace an institutional representative, or separate an unreliable society. It does not guarantee obedience. AI uses it before a planned joint operation when failure would be costly. |
| D22 Develop a controlled arsenal | C civilian factories and 250S support equipment over 180 days | Requires a valid industrial site, the relevant focus unlock, and a sustained supply connection. Opens M06 or M14. The outcome is a funded production or repair capability, with exact building and technology effects verified during implementation. Repeating the project cannot grant the same factory twice. |
| D23 Join the Chinese anti-intervention pact | 50 Political Power, 15 Command Power, and an accepted contribution with at most two further cost types. 30-day organization | Requires the pact conditions in Part 7. Opens M09 or a supply contribution. The actor keeps its government and existing faction. AI refuses a commitment that would require an impossible ceasefire or an unsupplied offensive. |
| D24 Proclaim a durable Boxer government | 100 Political Power and 30 Command Power. Requires an already completed 90-day institutional hold | Requires genuine controlled strongholds, a viable country carrier, forces, administration, and a valid territory transfer path. Activates the country package without duplicating existing assets. A failed carrier or map check blocks activation and must not consume the cost. |

## Foreign response and coalition actions

| ID and working action | Cost and timing | Conditions, effect, failure, and AI |
| --- | --- | --- |
| D25 Evacuate a threatened site | 15 Command Power, route transport, and fuel. Sea anchor is 5S convoys and 5000S fuel. Land anchor is 25S trucks and 2500S fuel | Opens emergency M01 with a justified 30- or 60-day window. Requires a safe destination and an actual route or negotiated passage. Partial evacuation counts only those who departed. AI prefers evacuation when holding the site is not worth a larger war. |
| D26 Reinforce an existing position | 20 Command Power, required transport, fuel, and an assigned force commitment. 30-day preparation | Uses real formations and normal reinforcement bills. Opens M02. It does not create soldiers by spending Command Power. AI compares the site's value, supply, and risk of escalation with withdrawal. |
| D27 Issue a specific ultimatum | 50 Political Power. Proposed 30-day response window, 180-day repeat limit for the same demand | Names an achievable demand, responsible recipient, and intended next step. Opens a diplomatic response. AI must be prepared to enforce or revise the demand. A refusal does not force war when engine relationships make it impossible. |
| D28 Commit an expedition | 30 Command Power, transport, fuel, and existing force commitments. Typical sea anchor is 10S convoys and 10000S fuel. 30-day preparation | Opens M08 and records the mandate. Actual troop deployment and supply are required. No transfer occurs outside a verified engine mechanism. AI reserves enough capacity for its other essential fronts. |
| D29 Call an intervention conference | 75 Political Power. 30-day process | Requires at least two eligible independent powers willing to discuss a joint operation. Establishes the mandate and member positions. It does not create an engine faction. AI calls it when cooperation can achieve an objective that unilateral action cannot safely achieve. |
| D30 Join an agreed mandate | 35 Political Power plus an explicit contribution with at most three further cost types. 15-day agreement | Records the member's objective and obligations. Requires a viable contribution and compatible diplomatic status. AI can offer limited aid instead of an expedition. Membership does not copy another member's territorial claims. |
| D31 Leave the coalition | 25 Political Power for the diplomatic action. Existing withdrawal obligations remain | Ends new coalition commitments and begins or continues orderly withdrawal. It does not teleport forces or refund consumed supplies. AI leaves when its mandate is complete, the mandate becomes unacceptable, or continued participation is unsustainable. |
| D32 Narrow the mandate | 50 Political Power. 15-day conference | Opens M12 or a direct revision when all affected members agree. Can replace punitive aims with evacuation or protection. Dissenting members must accept the revision or leave. The proposal alone does not reduce Pressure. |
| D33 Propose expanded demands | 75 Political Power and 20 Command Power. 30-day conference | Requires actual leverage and an identified new objective. Other members can refuse. Chinese actors receive the revised demand. AI avoids expansion when supply, domestic priorities, or coalition support are inadequate. |
| D34 Maintain a shared supply corridor | 100S support equipment, 5000S fuel, and either 5S trains or route convoys. 90-day commitment | Opens M03 and allocates support to one actual route. Losses and delivered supplies are recorded once. AI prefers routes serving its accepted objective and avoids funding duplicate projects on the same segment. |
| D35 Conduct an anti-Boxer operation | 30 Command Power, 5000S fuel, and assigned forces. 180-day ordinary campaign objective | Opens M07 with named strongholds or networks. Requires real military access or a war relationship. Success follows the map and disarmament evidence, not a paid result roll. AI rejects attacks that cannot be supplied. |
| D36 Present a compensation claim | 50 Political Power. 30-day evidence and conference process | Requires documented event-related loss and a valid responsible party. The claim is bounded by the verified loss and enforceable capacity. It cannot be repeated for the same incident or converted into a claim on all Chinese territory. |
| D37 Withdraw the expedition | 15 Command Power plus transport and fuel for the remaining force. Normal 90-day withdrawal objective | Opens M13. Ends obligations only after the relevant forces and allocations have actually left or been lawfully transferred. AI uses it promptly after a limited mandate succeeds. A blocked route produces a negotiated extension or partial withdrawal. |
| D38 Recognize a Chinese security compact | 50 Political Power. 15-day agreement, followed by 90-day verification | Accepts an enforceable local or national protection arrangement. Can satisfy suppression or protection objectives without direct occupation. AI evaluates actual past compliance and current ability to enforce the compact. |

## Settlement and reconstruction actions

| ID and working action | Cost and timing | Conditions, effect, failure, and AI |
| --- | --- | --- |
| D39 Guarantee a settlement site | 35 Political Power plus a named security or relief commitment with at most three additional cost types. 90-day verification | Opens M11 or M17. Uses the actual site and signatories. A guarantee that cannot be implemented is unavailable. AI favors a limited guarantee it can maintain over a broad unenforceable promise. |
| D40 Meet a scheduled reparation installment | The contract's verified civilian capacity or supported resource bill. No extra Political Power fee | Applies payment to one due installment. It cannot overpay, duplicate a receipt, or send resources to a dead recipient. Remaining obligations appear as normal contract terms and deadlines, not a third crisis meter. |
| D41 Request a payment moratorium | 50 Political Power. 30-day negotiation | Requires genuine capacity loss or a disputed obligation. A successful request can pause or reschedule payments within the contract's maximum extension. It does not erase the principal or repeatedly reset the treaty. AI requests relief before a predictable default. |
| D42 Verify a demilitarized area | 15 Command Power and an agreed observer commitment. 90-day verification | Checks the named area and permitted exceptions. It grants no general military access. If exact deployment restrictions cannot be represented safely, that term is blocked until a supported implementation is agreed. |
| D43 Reconstruct a damaged district | C civilian capacity, 200S support equipment, and 50S trucks. 180 days | Opens M14. Repairs documented damage and restores services through the shared systems. It does not create a fresh industrial reward every time the state changes hands. AI prioritizes population and supply recovery over prestige projects. |
| D44 Negotiate an amended protocol | 75 Political Power and 20 Command Power. 90-day negotiation | Requires completed obligations, changed leverage, or an accepted dispute. Can end a privilege, shorten occupation, or revise remaining duties. The result depends on consent or a separate actual victory. Clicking the decision does not cancel foreign ownership. |
| D45 Integrate a cooperating region | 75 Political Power, 100S support equipment, and C civilian capacity. 180-day process | Opens M15 after a political agreement or a supported postwar settlement. Keeps civilian, military, and administrative assets in one ownership path. Cores are granted only under the reviewed homeland and integration policy. |
| D46 Close the intervention conference | 25 Political Power. Available after its mandate and settlement responsibilities are resolved | Dissolves event-owned coordination and clears obsolete commitments. It does not dissolve an engine faction or terminate unrelated wars. Remaining bilateral treaties retain their own lifecycle. |

## Presentation and access

Use one principal event category at a time for the actor's current role and phase.
The header contains the two formatted values and a short explanation of the current issue.
A static category picture is allowed because this design uses ordinary decisions and formatted text, without a custom meter panel or extra category controls.

Show three to five primary actions, with six as a hard maximum for the current event surface.
Show one to three active missions.
Emergency actions take priority, followed by an active commitment, a viable next operation, and policy review.
Pure navigation can use a normal event menu or an established targeted-decision interaction.
It must not make a paid choice or commit resources before the real confirmation.

The priority system must not permanently hide a necessary action.
Policy review, withdrawal, negotiation, and settlement compliance remain reachable while relevant.
A target selector exposes the valid targets for one action family, not every action for every country at once.
The AI evaluates the complete valid target pool independently of whichever target the human last selected.

## Cancellation and invalidation

Ordinary loss of access pauses a project when recovery remains plausible.
A destroyed target, resolved incident, extinct actor, or incompatible ownership change closes or reassigns the objective according to its mission contract.
The implementation records what was consumed, what remains reserved, and who owns any delivered assets before cleanup.

A cancelled political proposal refunds no spent political effort.
A cancelled shipment releases only its undelivered and unconsumed allocation.
An abandoned military commitment leaves the actual forces where the engine places them and opens withdrawal or reassignment.
No cancellation grants the mission's success reward.
