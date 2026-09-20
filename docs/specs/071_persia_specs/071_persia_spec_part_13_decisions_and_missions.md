# 071 Persia: decisions and missions

## Decision structure

The primary category contains the current imperial situation and a small set of useful actions. Its selected target determines which regional or subject actions appear. Routine actions should remain within three to five visible choices, with six only where a real branching situation requires them. The category normally shows one to three active missions.

Actions have a visible purpose, a specific target, a quoted cost, and a concrete outcome. A decision uses at most four spendable cost types. At most three values appear in its compact inline cost display, with the full cost and conditions in the tooltip. Command power costs never exceed 60. Native requirements such as control, access, a free construction slot, or an available formation are not disguised as extra hidden currencies.

All numbers below are authored initial tuning. The quoted cost is charged once from the same conditions used to show availability. A target or price change requires a fresh quote. A clicked action cannot become more expensive after confirmation.

## Principal actions

| Action label | Main gate | Proposed cost | Result and commitment |
|---|---|---|---|
| Select homeland confrontation | Foreign holder of valid homeland | No spendable cost | Selects one strategic enemy and displays the complete relevant region set |
| Present homeland settlement | Valid recipient and diplomatic authority | 50 political power | Sends a real settlement choice, with a 90-day repeat limit |
| Open regional assessment | Unlocked regional project | 25 command power and 25 army experience | Reveals supported known conditions and opens preparation, not exact victory odds |
| Fund opening supply program | Opening support active and valid corridor | 500 trucks, 500 support equipment, and 25 command power | Begins the 120-day supply mission |
| Fund replacement industry | Valid owned industrial destination | 100 political power, 1,000 support equipment, and 25 army experience | Begins the 180-day replacement program with a stated construction commitment |
| Establish a basic satrapy | Valid settled territory or consenting state | 75 political power and 500 support equipment | Offers the charter and starts its settlement process |
| Negotiate a specialized charter | Evolution I and eligible satrapy | 50 political power and a quoted material investment | Selects one charter type and starts a 180-day review restriction |
| Request an emergency levy | Valid charter, serious war, no active levy | 25 command power and 5 legitimacy | Makes one defined extra demand, with subject consent rules and a 180-day cooldown |
| Convene a charter hearing | Actual dispute | 75 political power | Opens the 120-day hearing, with remedies tied to the dispute |
| Prepare guard equipment | Guard command and legal family | Quoted equipment in batches of at most three equipment types, plus 25 army experience on the first batch only | Records paid material against one named recruitment project |
| Begin guard training | Prepared material and free capacity | 25 command power and quoted manpower | Reserves capacity and begins training, with no free duplicate personnel |
| Prepare guard conversion | Eligible formation and researched destination | Quoted equipment difference in batches of at most three types, plus 25 army experience on the first batch only | Funds one conversion project for that existing formation |
| Begin guard conversion | Prepared conversion material and reserved capacity difference | No repeated equipment payment | Converts the selected formation after training, keeping its existing personnel |
| Begin Persepolis survey | Site controlled and stable access | 50 political power and 500 support equipment | Starts the 120-day first stage |
| Fund Persepolis conservation | Survey complete and valid construction | 100 political power and 1,000 support equipment | Starts the 180-day site project with the visible construction commitment |
| Propose a Gulf agreement | Valid port holder | 75 political power | Offers a lease, investment, guarantee, or charter as one explicit proposal |
| Fund coastal readiness | Usable port and valid program | 50 naval experience, 1,000 support equipment, and 50,000 fuel | Starts the 180-day readiness program |
| Present a submission offer | Evolution III, route conclusion, legitimacy 80 | 100 political power and 25 command power | Sends a defined offer to one eligible country, with a 180-day repeat limit |
| Honor an imperial guarantee | Existing agreement and qualifying attack | No artificial activation fee | Uses supported intervention rules and accepts the real war obligation |
| Relocate central administration | Capital lost and valid destination | 50 political power and 500 trucks | Begins the 120-day command-restoration mission |
| Accept a reduced imperial settlement | Actual unresolved crisis | Loss of the abandoned claim or charter | Ends the named commitment and records its political consequences |

Guard recruitment uses separate equipment preparation and personnel training stages. Each preparation payment contains at most three named equipment types. Army experience is charged on the first batch only, so that payment uses at most four cost types. The training payment uses command power and manpower. Every batch is recorded against one project and can be paid only once. The player sees the full total commitment before beginning. A tooltip cannot hide six equipment debits under the word equipment.

Legitimacy is normally a political consequence, not a currency. The emergency levy explicitly sacrifices 5 legitimacy because it knowingly strains the charter. It must be shown in the full cost. The action therefore remains within its cost budget.

## Construction commitments

A project can reserve a limited share of construction capacity for a duration when the verified project framework supports it. That commitment appears in the tooltip alongside the spendable costs. It is not an unannounced fifth resource debit.

If construction capacity is itself represented as a spendable project currency in the actual repository, it counts toward the four-type budget. The action map must then combine or stage other costs appropriately. The player sees the same total obligation regardless of the internal implementation.

The package does not authorize a fake construction timer that awards factories while the country contributes nothing. The exact supported building program must be inspected in the repository.

## Mission A: establish the opening supply line

Duration is 120 days. The player selects a usable corridor between a surviving administrative or industrial center and an active homeland front. The mission requires a new repair or construction contribution, assignment of motor transport, and a currently usable connection. Existing infrastructure can provide the base, but clicking the mission after all work is already finished cannot manufacture a reward.

Success completes the opening logistics settlement and provides the stated local support result. Partial success retains finished repairs and extends only the unfinished objective once for 60 days when control remains viable. Failure retains paid and completed physical work but withholds the success reward. It does not delete the opening army.

## Mission B: sustain the mobilization

Duration is 180 days. The player chooses a replacement plan for the actual principal equipment families. The objectives include starting the funded industrial program, establishing at least one relevant production capability, and delivering a new training or maintenance contribution.

Success transitions the mobilization settlement to its sustainable form. Partial success allows the smaller professional settlement. Failure expires the temporary opening support normally and leaves existing units under standard supply and reinforcement rules. One paid 90-day emergency extension is available during a serious war.

## Mission C: settle a recovered region

Duration is 120 days. The mission begins after a qualifying victory or negotiated transfer. Its objectives are the chosen administration or charter, a usable regional connection, and the end of active local fighting at its essential center.

Success awards the regional first-completion milestone if it has never been earned. Partial success records military control without full political settlement. Failure opens renegotiation, a withdrawal option, or the specific local crisis. It does not automatically start a generic civil war.

## Mission D: a charter hearing

Duration is 120 days. The mission names the subject and disputed obligation. The player must perform a remedy, negotiate accepted revised terms, or complete a legally supported enforcement outcome. Already possessing political power is not the objective.

Success resolves that dispute. Partial success can produce a reduced charter or temporary delivery schedule. Failure moves only the affected subject or coalition toward defiance or secession. Unrelated loyal subjects do not change status without a cause.

## Mission E: guard training

Duration is 120 days for a new basic formation and 180 days for an advanced formation or substantial conversion. Capacity is reserved when the first equipment-preparation batch begins. Paid material is recorded across the bounded batches. Manpower and command power are charged only when training begins, and army experience is charged once in preparation. A reservation expires after 90 days if preparation has not been completed, with unconsumed material returned under the recorded transaction. The formation arrives at the appropriate training level and legal location only after the program completes.

A loss of the training site relocates or pauses the program under a stated rule. Cancellation refunds only unconsumed resources. Already consumed equipment and training are not refunded as a new free stockpile. Reopening the mission cannot duplicate the reservation.

## Mission F: Persepolis

The survey lasts 120 days, conservation 180 days, and final stability requirement 90 days. These stages are described in part 11. Each has a new action, a physical or administrative result, and an interruption policy. The final ceremony has its own political requirements.

Loss of the site suspends unfinished work and withholds the final milestone. Recovery resumes the recorded project. The player does not pay for the same finished survey again unless the actual work was destroyed and the replacement is explicitly justified.

## Mission G: coastal readiness

Duration is 180 days. Objectives include a valid usable port, completed support or dockyard work, and an operational escort or patrol force appropriate to the program. A starting reserve of convoys does not satisfy the naval force requirement by itself.

Success opens the next fleet program and can contribute to the Gulf settlement. Partial success records the port work but delays the naval milestone. Failure retains physical work, withholds the milestone, and can renegotiate an associated foreign port agreement.

## Mission H: restore central command

Duration is 120 days. A valid new center, restored communications, and a supplied loyal force are the main objectives. A political settlement or command appointment must also be resolved when it caused the crisis.

Success ends the named central crisis. Partial success preserves a smaller state with suspended outer claims. Failure can move the existing crisis toward fragmentation. It cannot invent a rival army unrelated to existing commands.

## Expiry, invalid targets, and competition

A mission completes automatically when all current conditions are met. The player does not need to click a final button before midnight. The expiry path checks success first. Losing a target, a state transfer, a subject exit, and country capitulation each have an explicit cancel, pause, or revised-target outcome.

The player cannot run contradictory charters for one subject or several identical projects for one site. Shared resources are reserved where needed so two actions cannot both spend the same equipment on the same tick. Costs and refunds use a single recorded transaction.

No active mission should demand an impossible action from a capitulated or landlocked country. When a project becomes impossible, the interface states why and offers the correct settlement. It does not leave a permanent red timer with no available response.
