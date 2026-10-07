# Occupation revolt: decisions, missions and political programs

## One operation contract across interfaces

A decision, focus payoff and event choice that performs the same operation must call the same operation contract.
They must not maintain contradictory quotes for the same operation or separate one-shot rewards.
A native focus and a decision counterpart may have different opportunity costs, but their material requirements and one-shot results are identical.
Native focus expenditure does not pay an equipment or construction bill, and the same explicit political setup fee is never charged twice when access changes between the two interfaces.
The operation record identifies actor, claimant, target, current phase, quoted cost, committed resources, duration, objective, outcome and cleanup.
Working operation identifiers in this chapter are proposed internal identifiers, not assertions that they already exist in the repository.

Readiness and Cohesion are consequences and eligibility conditions, never hidden currencies.
Political power, command power, equipment, fuel or other native resources are debited only when the action genuinely spends them.
A required port, available supply route, local factory, army position or level of Cohesion is a condition rather than a price.
Every tooltip must distinguish those categories.

Ordinary local organization and liaison tasks take 35 days.
Substantial training, integration and institutional programs take 70 days.
Missions normally allow 100 days for a small attainable objective, 150 days for a substantial campaign task and 180 days for a difficult divided theater.
A 30–60 day deadline is reserved for an already unfolding battlefield emergency.
The deadline starts when the mission commits and survives save/load and UI visibility changes.

## Phase budgets

| View and phase | Primary actions | Maximum concurrent event missions |
|---|---|---:|
| Existing claimant preparing underground | Organize base, coordinate stores, settle command, protect exposed network, open support talks | 2 |
| Claimant in initial war | Equip and organize, prepare next region, establish government, negotiate support, emergency withdrawal | 3 |
| Claimant in sustained restoration | Develop next region, integrate forces, execute national program, negotiate settlement, emergency withdrawal | 3 |
| Claimant in settled recovery | Fulfill settlement, rebuild, settle temporary forces, assist verified civilian return, close external obligations | 3 |
| Occupier | Contain front, act on exposed network, restore services, negotiate, withdraw | 2 |
| Foreign supporter | Establish liaison, deliver stores, return personnel, offer agreement, organize justified humanitarian access | 2 |

Only applicable actions appear.
The dormant claimant has no playable national action view before country activation.
Its initial local preparation is a finite incident process and a sponsor can perform only the sponsor-owned actions.
Political route choices are resolved through a finite event choice opened by the relevant action, rather than adding three permanent duplicate decision rows.
All views together still expose only Readiness and Cohesion as custom numeric public values.

## Claimant preparation actions

`or095_organize_base` selects one authentic home region with a surviving network and useful remaining organization capacity.
It costs 25 political power for a living claimant, takes 35 days, raises local organization by 15 and Readiness by 5 on success, and cannot exceed the evidence-based local ceiling.
A target lost to a genuine hostile disruption can fail with its actual committed cost consumed.
A stale or already satisfied target fails preflight without charge.
The AI prefers its most viable initial base rather than the largest population state regardless of geography.

`or095_coordinate_stores` allocates real compatible equipment to a verified cache or local formation.
The quote uses the selected force's supported equipment deficit and the actor's uncommitted usable stock.
It never transfers more than either amount.
This coordination has a 25 political-power organization cost only when it establishes a new regional issue operation.
Ordinary native reinforcement is not taxed repeatedly by an event decision.
A supply route is a requirement, and any transport cost must be part of the same exact quote.
The result is the actual delivered inventory, not a Readiness number standing in for weapons.

`or095_settle_command` opens the legal-continuity, resistance-compact or emergency-command choice supported by the country's profile.
The ordinary conference costs 25 political power and takes 35 days.
Its one-shot agreement grants 10 Cohesion after the promised representation or authority is actually established.
An emergency choice can accelerate the command program while creating the dated review obligation.
A dormant movement reaches the same command milestone through its preparation process without spending a nonexistent country's political power.

`or095_protect_network` responds to a currently exposed regional organization.
Dispersal is free in political power but loses 15 local organization and 5 Readiness while preserving only the actual surviving network and stores.
Relocation needs a supported route and an exact movable inventory.
Accelerated revolt uses the current force budget and available territory.
These are mutually exclusive responses to one exposure record, not three repeatable reward buttons.
The AI prefers dispersal when the armed opening is not viable and relocation only when the destination is materially safer.

`or095_support_talks` identifies a real prospective sponsor and proposes one useful supported contribution.
Opening talks has no material shipment cost.
A concluded agreement may cost 25 political power for diplomatic organization where the agreement actually requires it.
Neither party pays equipment or transport before accepting the exact contribution.
The AI does not ask a bankrupt, unreachable or diplomatically hostile country for an impossible delivery.

## Armed and sustained claimant actions

`or095_equip_and_organize` forms or converts a specified finite cohort using actual recruits, equipment and command capacity.
The ordinary institutional component costs 25 political power and takes 70 days.
The quote includes the exact incremental equipment bill rather than the full bill of the already equipped formation.
Returning existing forces is a separate receipt and does not pass through a new-unit grant routine.
Prepared Underground can provide the single incident reorganization improvement without repeating its opening grant.

`or095_prepare_region` is the 35-day, 25-political-power regional liaison from Part 06.
Its target must be a genuine currently relevant home region.
At baseline it prepares the next connected opportunity.
Evolution II permits a supported additional-center operation with a 70-day coordination period and its own finite material allocation.
The target becoming liberated by ordinary combat satisfies only the political integration portion.
It never triggers a second state transfer or opening army.

`or095_national_program` is the decision counterpart of a substantial focus-tree program from Part 09.
It commits to one named political, production, military, diplomatic or recovery objective.
The normal political-organization cost is 50 political power for a 70-day substantial institutional program.
Programs whose actual cost is native construction or material procurement show those costs separately and do not add arbitrary political-power charges merely to make the button expensive.
The program completes when its promised objective is achieved and grants the same one-shot result as the corresponding focus route.
The country can sustain one major program at Cohesion below 50 and two at Cohesion 50 or above, while remaining within the mission budget.

`or095_negotiate_settlement` opens a concrete offer to a relevant party.
The act of proposing or refusing peace is free.
Accepting a settlement commits the exact territory, status, military and diplomatic terms after full revalidation.
Any administrative cost applies to carrying out a specific institutional obligation after agreement and cannot prevent the player from surrendering or leaving an unwinnable position.
A failed or rejected proposal does not debit resources intended for an unaccepted transfer.

`or095_emergency_withdrawal` is available when the claimant is in a genuine survival crisis and has a supported exit or dispersal possibility.
It does not charge political power to acknowledge defeat.
It transfers only actual eligible surviving units or recorded movable stores through supported routes.
A no-route outcome states that no organized evacuation is available and permits the appropriate military surrender or local dispersal path without inventing safe passage.
It does not impose a fabricated civilian casualty total.

## Occupier actions

`or095_contain_front` establishes a target-specific containment objective with actual forces and supply.
Its organization cost is 25 political power and its ordinary deadline is 100 days.
The player must hold the specified approaches or isolate a viable rebel supply position through real warfare.
Completion reduces the local spread opportunity while the actual containment remains in place.
It does not add a permanent nationwide anti-revolt immunity.
Loss of the relevant position removes the factual containment benefit.

`or095_disrupt_network` requires a confirmed exposed network and sufficient real local security capacity.
It costs 25 political power and 25 command power, takes 35 days and affects the selected network only.
On success it reduces local organization by 15 and resolves any verified exposed stores.
It has no generic casualty award or universal compliance reset.
The AI cannot target unknown networks or use a human's currently selected state as its own selector.

`or095_restore_services` commits to a real local repair, administration or relief objective.
The administrative setup may cost 25 political power.
Buildings require native repair or construction and relief requires the existing system's actual supplies and transport.
The ordinary mission deadline is 100–150 days.
Successful delivery can reduce a proven local grievance contribution and improve the terms of a negotiated settlement.
It cannot cancel national claims or manufacture a blanket reduction where no grievance receipt existed.

`or095_open_negotiations` uses the common settlement contract and is free to propose.
The AI weighs military overextension, strategic value, domestic costs and attainable terms.
It can accept partial restoration or autonomy when continued occupation is less useful than a credible settlement.
It does not always refuse merely because it is a major country.
An actual nonhuman occupier without supported diplomatic agency receives no fictional negotiation counterpart.

`or095_order_withdrawal` commits to relinquishing the specified occupation under an accepted agreement or an explicit military retreat.
It is free to initiate and preserves native unit movement and war rules.
The mission distinguishes transferring sovereignty, relinquishing control, evacuating forces and moving civilians.
These are separate transactions.
Only applicable, supported parts are executed.

## Foreign supporter actions

`or095_establish_liaison` costs 25 political power and takes 35 days.
It needs a viable contact and provides the supported information and coordination relationship.
The same live liaison is not sold repeatedly.
A broken route suspends material operations without erasing every political fact.

`or095_deliver_stores` uses the dynamic offer calculation in Part 07.
It costs the exact equipment lot plus 25 political power, with route-specific supported transport costs included in the same quote.
No more than four spendable resource types may be required.
The delivery mission usually allows 100–150 days depending on route length and military risk.
It completes automatically on actual arrival.
Partial delivery is recorded as partial delivery, not a fully successful shipment with free replacement equipment.

`or095_return_personnel` offers a real unit return, native volunteer contribution or the 70-day training mission.
These are distinct mutually exclusive variants with their own exact ownership and cost semantics.
The training variant costs 25 political power and 25 command power.
A unit return does not charge its full manpower and equipment bill again if those resources already exist in the returning unit.
Unsupported native transfers remain blocked rather than approximated through unbalanced creation.

`or095_offer_agreement` proposes recognition, access, guarantee, supply terms or a major political arrangement.
Terms require explicit acceptance by the affected country or valid provisional authority.
The action cannot make a claimant a subject merely because it accepted rifles.
Recognition and guarantee use their actual native costs and consequences where present, with no double charging by a custom political-power effect.

`or095_humanitarian_access` appears only for an actual recorded civilian need and a supported relief or movement route.
It uses the separate famine, migration and humanitarian owners for their actual operations.
It does not automatically transfer population or reduce military resistance because a sponsor clicked a humanitarian button.
A failed route releases only unused reservations, and completed assistance retains its true delivered amount and responsible actors.

## Recovery actions

`or095_fulfill_settlement` selects a dated political or administrative obligation already accepted by the country.
It cannot choose a new unrelated agreement simply to collect the old reward.
The normal substantial administrative program costs 50 political power and lasts 70 days when that organization work is genuinely required.
Territory, access and military terms use their actual native operations and are not hidden behind the administrative label.
Completing the obligation clears its recorded dispute once.

`or095_rebuild` chooses one real damaged or underdeveloped national priority from the recovery program.
Native construction and repair provide progress.
A 150–180 day mission can coordinate a substantial reconstruction target without guaranteeing that a building appears on the deadline.
If the country lacks the means to finish, it can seek real aid, choose a narrower revised target with a recorded change, or accept failure.
Already repaired buildings satisfy the need without creating duplicate completion rewards.

`or095_settle_temporary_forces` integrates or demobilizes actual temporary formations according to the government agreement.
Its institutional work normally takes 70 days and costs 25 political power.
Equipment and personnel are accounted for through supported native conversion or disbanding behavior.
The action cannot destroy regular units outside its exact scope.
A threatened country may retain a supported reserve arrangement where its settlement permits it.

`or095_civilian_return` requires a real displaced cohort, consent or the explicitly supported legal movement basis, a valid origin, a safe route and verified destination reception capacity.
It delegates the exact physical movement to the shared owner.
Its mission records survivors arriving rather than treating a territorial liberation as population movement.
No claimant must perform this action when no relevant displacement exists.

`or095_close_obligations` resolves completed foreign support terms and unused reservations.
It does not reimburse equipment already delivered or remove a patron's native guarantee without the proper diplomatic action.
A breach is recorded as a breach.
A mutually agreed early termination is recorded as a new agreement and cannot be used to replay the original reward.

## Mission outcomes and cancellation

Success is automatic when the exact objective has been achieved.
Do not require a second reward-collection click.
Expiry reports what failed and applies only the agreed consequence.
Cancellation distinguishes work already done from unused resources.
A state becoming invalid, changing identity or being peacefully restored can close an obsolete task without pretending the player lost a battle.

Every mission retains its actual start date, deadline, owner and target after save/load.
A delayed callback carries an incident generation and operation identifier.
It cannot act on the current occupant of a reused array index.
When an incident closes, all pending missions receive a terminal status and clear their UI and unused reservations.
Its surviving national-history records remain separate.

## Cost presentation and equality

A quote is calculated once from the exact selected operation and shown before commitment.
The same result drives the visible amount, inclusive affordability check, debit, delivered effect and any valid refund.
Exact equality with the required resource amount must be affordable.
Native costs and custom debits cannot both remove the same payment.
Shared price changes and universal-cost rules must be applied consistently before the quote is displayed.

Use the real resource icon for each cost.
The compact inline cost display has at most three icon-value groups and four ordinary words.
Longer conditions and full multi-resource details belong in the tooltip.
No action requires more than four spendable resource types and no command-power charge exceeds 60.
The two custom values remain consequences or conditions throughout.
