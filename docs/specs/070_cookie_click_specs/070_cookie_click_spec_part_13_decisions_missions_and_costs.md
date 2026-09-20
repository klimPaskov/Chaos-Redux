# 070 Cookie Click: decisions, missions and costs

## Action surfaces

The pet has one animated feeding window and a small ordinary decision list for meaningful interventions.
The Empire uses its converted Cookie window for appetite and Level, with ordinary phase-filtered categories for administration and military projects.
Opponents use ordinary response categories with an eligible static category picture.
Do not add a decorative category picture beside the Cookie's already animated interactive window.

Show three to five relevant actions in an ordinary category, with six as the absolute normal limit.
Show no more than three active missions per actor from this package.
Other valid actions stay hidden until their phase, method or target becomes relevant.
Use one selected operation per state and one active project per military institution.

Every action preview identifies its real target, all costs, duration, expected effect and interruption rule.
The inline summary uses at most three resource icons and short labels.
The full tooltip lists every spendable resource.
No action spends more than four distinct resources.
No Command Power cost exceeds 60.

## Cost scale

For host preparation and opponent programs, define a country scale `q = clamp(1, 10, ceil((civilian_factories + military_factories) / 25))`.
For Empire programs use the same factory scale with a minimum of one.
This is an authored balancing rule.
Keep its calculation in one documented helper.

A cost written as `50q` means 50 multiplied by q.
Equipment counts and quantities remain in readable multiples of five.
Percent-of-stockpile costs always have an explicit protected reserve, an upper cap and a saved preview amount.
Do not recalculate a percentage between payment and completion to increase the bill.
Manpower committed to a project is unavailable while committed and returns only where the action explicitly says so.
Lost manpower is distinct from civilian deaths.

Small-country actions use their minimum packet and can be unavailable when the country genuinely cannot pay.
They do not silently charge negative stockpiles.
The player can still feed the pet, attempt weak starvation, or fight using ordinary forces without buying an intervention.

## Pet and host actions

The identifiers below are design action IDs.
Their prose describes the action.
They are not final localization keys or player-facing names.

| ID and function | Availability and target | Cost and time | Result and interruption |
| --- | --- | --- | --- |
| H-01, protect a reserve family | Evolution I or above, hungry pet, one owned valid material family | 10 Army, Navy or Air Experience relevant to that family, plus 25q support equipment, 5 days | Excludes that family from self-feeding for the next 5 cycles, then a 10-cycle cooldown. Does not exclude all families or stop revolt |
| H-02, relocate exposed equipment | An exposed bakery anchor and movable national stocks | 5q trains and 100q fuel, 10 days | Protects up to 25 percent of the snapshot's eligible starting equipment transfer component. The national stockpile remains real. Cancellation keeps paid transport costs |
| H-03, evacuate an exposed state | A revealed anchor with civilians and a valid receiving state | 5q trains, 50q support equipment and 100q fuel, 15 days | Moves up to 5 percent of that state's current civilians, capped by reception and transport. Reduces only the population component actually moved. Migration and deaths remain separate |
| H-04, disable an anchor workshop | A revealed anchor, host control and a real workshop target | 25 Army Experience and 50q support equipment, 10 days | Removes or damages the selected real workshop and reduces its uprising industry contribution by up to 25 percent. The building loss is real and is not refunded if the cookie calms |
| H-05, direct emergency feeding | Living pet with current room in the daily target | Actual individual clicks only | Opens and focuses the existing Cookie window. It never pays resources to replace clicks or creates a second feeding action |
| H-06, inspect current danger | Mature or hungry pet | Free, no repeated gameplay effect | Opens a concise current-state explanation, active warning deadline and available responses. Does not reveal exact hidden random draws or add a new meter |

H-01 chooses one family from the currently valid pool and saves the exact protection interval.
Selecting another family cannot extend the original interval.
If every other edible family becomes invalid, that does not authorize eating the protected family before its expiry.
The cookie remains hungry and revolt timing continues.

H-02 does not make national equipment physically belong to a state.
It records a limited, paid reduction of the upcoming stock-transfer allocation.
It cannot protect resources already consumed.
H-03 uses actual state-to-state migration and a receiving-capacity check.
Neither action changes Cookie Level or gives the host a free army.

A last-minute 75 percent feeding milestone cancels an armed revolt warning immediately, before its deadline callback.
The host does not have to wait until the next daily boundary.
H-02 through H-04 may continue afterward only where their consequences still make sense.
They never generate a cash refund merely because danger ended.

## Empire administration

| ID and function | Target and prerequisite | Cost and duration | Complete, partial and failure behavior |
| --- | --- | --- | --- |
| E-01, process captured equipment | Owned compatible material lots, EB-03 | Debit a selected batch of 100 to 1,000 items, 5 days | Converts actual debited items at the registered rate. Unsupported or lost items do not pay. No new source lot is invented |
| E-02, establish a feeding territory | Supplied controlled state, farming method, population and infrastructure sufficient | 100q support equipment, 500q manpower committed and 5q trains, 90 days | Creates prepared state status. Manpower remains committed to that operating territory. Control loss ends the project and returns only surviving uncommitted personnel |
| E-03, operate a prepared territory | A completed E-02 site | Per 30 days, 25q support equipment and 100q replacement manpower. Existing committed staff are not charged again | Supplies the authored daily farm yield while valid. Missing supplies pauses future output. No automatic back-payment for days that were not productive |
| E-04, convert a population group | Conversion method, controlled state above its floor | 100 Cookie-body equipment, 25 support equipment and 5,000 actual civilians, 90 days | Produces 2,500 Cookie manpower and 150 Cookie-body equipment. Those are co-products of one transformation. No food is also awarded for those people |
| E-05, strip an industrial level | Controlled state with a real eligible factory level | 50q Cookie-body equipment and 10 days, plus destruction of the selected factory level | Grants 500 food for a civilian factory or 750 for a military factory before method bonuses. Incomplete work leaves recorded damage with at most proportional food |
| E-06, consume a civilian group | Actual controlled civilians above the current floor | 1,000 actual civilians, 5 days | Grants 100 food before method bonuses and logs actual civilian deaths once. Fullness capacity can waste surplus, shown before confirmation |
| E-07, repair a feeding territory | A disrupted prepared territory with population and control | 50q support equipment, 5q trains and 30 days | Restores only prepared-operation functionality after actual infrastructure and control requirements are satisfied. Does not restore population or destroyed factories |
| E-08, set reserve policy | Existing Empire | No lump-sum currency cost, one change per 5 days | Changes automatic feeding priorities. Actual subsequent debits remain subject to displayed floors and recipe validity |
| E-09, establish tribute | Valid Cookie subject after SE-02 | Negotiated actual equipment, fuel or food-conversion commitment, 30-day intervals | Transfers actual payable resources with a domestic floor. The subject can fail an obligation, prompting the designed response. No hidden negative balances |
| E-10, reduce a failed tribute demand | A genuine missed obligation | Forego 25 percent of that subject's next three demands, 90 days | Makes future compliance possible without creating a new resource. A later increase requires a new review |
| E-11, integrate a direct administration | Eligible controlled region after SE-04 | 50q support equipment and 500q committed manpower, 180 days | Completes real supply and occupation objectives, then replaces temporary administration with the method's settled state treatment. Does not grant all cores |
| E-12, release a managed subject | Valid surviving identity and owned releasable territory after SE-01 | Transfer real control and the agreed operating stock reserve, 30-day settlement | Creates an actual dependent administration and removes its territory from direct-state appetite. No repeatable liberation reward |

Food returns in E-05 and E-06 are new authored conversion rates.
They are not inferred exchange rates from native factory production or human population.
The imbalance between urgent feeding and permanent losses is intentional.
Use the actual quantity delivered, with capacity limits applied after conversion.
The preview warns when part of the output would be wasted.
No wasted food is paid as political power or stored in an unlimited hidden bank.

E-04 stages the actual population debit and conversion reward together at completion.
Until then, those civilians remain present but are reserved against overlapping conversion operations.
A lost target cancels the reservation and keeps real spent equipment spent.
For a partially completed supported conversion, debit and award the same proportional complete batch, with 1,000 civilians as the minimum completed batch.
Return 500 Cookie manpower and 30 body equipment per such batch.
Do not add the whole 5,000-population debit after awarding an earlier partial batch.
The initial 100 body-equipment input is a real process cost.
Its net body-equipment return is therefore 50 for the full operation, before any method-specific change.

Food consumption uses a first-registration population baseline per state.
Store that baseline when the state first enters this instance's consumption system.
Ownership changes do not reset it.
Natural later population changes remain real.
The ordinary protected floor is 10 percent of this stored baseline, further constrained by any mandatory shared-system minimum.
World-end permission can lower the event-owned floor, but cannot bypass the shared helper's supported safety bounds.

## Military programs

| ID | Program | Concrete cost and objective | Completion and failure |
| --- | --- | --- | --- |
| M-01 | Equip the first brigade institution | 25 Army Experience, 250q body equipment and 90 days with designated supplied formations at 75 percent equipment or higher | Opens the appropriate template and training standard. Partial progress keeps the template only when its equipment test was met |
| M-02 | Establish the Chocolate Guard | 50 Army Experience, 250q durable body equipment and 100q support equipment, 120 days | Unlocks Guard recruitment within its cap. Failure keeps research progress but gives no free Guard divisions |
| M-03 | Establish Oven Artillery | 25 Army Experience, 100q artillery-equivalent Cookie equipment, 50q support equipment and 120 days | Unlocks the supplied artillery institution and production line. Actual siege objective provides its one-time experience reward |
| M-04 | Field the first Dough Golem | 50 Army Experience, 250q heavy body equipment and 250q fuel or verified non-fuel operating equivalent, 180 days | Unlocks the heavy formation after a supplied field exercise. No bypass creates a finished formation |
| M-05 | Field Wafer Riders | 25 Army Experience, 150q mobile body equipment and 100q support equipment, 120 days | Unlocks the selected movement role and template after a real exploitation or interception objective |
| M-06 | Organize the naval institution | 25 Navy Experience, 10q convoys and 100q fuel, 120 days with a controlled port | Opens the naval program and relevant production acceleration. Losing every port pauses the objective and eventually fails it |
| M-07 | Organize aviation | 25 Air Experience, 25q valid existing aircraft and 250q fuel, 120 days with a usable airfield | Assigns aircraft to a concrete defensive or support role. The aircraft are committed, not destroyed as an unexplained fee |
| M-08 | Emergency military reinforcement | Severe frontline shortage and unused emergency cooldown | Actual body equipment and Cookie manpower equal to the receiving formations' recorded deficits, 5 days | Fills only those real deficits through a verified reinforcement path. It cannot create an extra force from missing input |
| M-09 | Construct a great oven | FF-03, a supplied production state and elite capacity | 500q heavy body equipment, 100q support equipment and 180 days | Unlocks and equips one allowable late formation. The saved recipe prevents repeated free grants |
| M-10 | Establish the final guard | FF-04 and elite capacity | 500q durable body equipment, 50 Army Experience and 180 days | Completes one final-guard institution and equips only a paid formation within the shared elite allowance |

Every equipment family in this table needs an actual validated equipment registration.
The descriptive terms for Cookie-body tiers are planning labels.
Do not spend a fictional stockpile whose engine type has not been implemented.
Where two family outputs share a native equipment category, preserve separate equipment identities and validate the intended production and reinforcement behavior.

Focus completion can open a program, reduce a specific cost, accelerate its work or provide one saved institution setup package.
It cannot also award the same finished formation if the program already supplies it.
The focus audit must assign a single owner to each reward.

## Campaign missions

| ID | Focus groups | Duration | Proof and result |
| --- | --- | --- | --- |
| C-01 | FB-02 and FB-05 | 90 days normally, 30 days for the named emergency recovery | Control and supply a real bakery or defensive objective. One target replacement is allowed after a genuine invalidation |
| C-02 | EB-02 and EB-04 | 120 days | Complete the selected rail, hub, port or industrial site and keep it operating for 30 days |
| C-03 | EB-06, EB-08 and HS-08 | 180 days | Maintain method-specific output, food and control for the declared consecutive interval |
| C-04 | LD-09 | 180 days | Maintain a supplied mixed force and complete its selected campaign objective. Repeat attempts have a 90-day cooldown |
| C-05 | EN-01 through EN-05 | 90 to 180 days according to front size | Control the selected capital, supply region or route and hold it for 30 days. A province touch is insufficient |
| C-06 | EN-06 and SE-04 | 180 days | Establish real postwar control, supply and the chosen administration method |
| C-07 | SE-02, SE-05 and SE-06 | 90 to 180 days | Complete actual tribute cycles, defend a corridor or resolve a declared member dispute |
| C-08 | FF-01 and FF-05 | 90-day preparation, 180-day global objective | Meet the specified reserve, supply and surviving-opposition conditions |

Start a mission only after a real target is selected and saved.
A target invalidated by another event is replaced once when a comparable valid target exists.
Otherwise void the impossible objective without granting its success reward.
A player deliberately abandoning a still-valid target is ordinary failure, not a free void.

Completed objective evidence resolves the mission automatically.
Do not force the player to click a claim button before a deadline when the gameplay objective was already met.
Partial results must correspond to durable work actually completed.
A factory built, a transport cost paid and a population loss suffered remain real after failure.
Political rewards and route-completion flags do not appear on partial failure.

## Opponent responses

| ID | Action | Cost and time | Effect |
| --- | --- | --- | --- |
| O-01 | Evacuate a threatened state | 5q trains, 100q fuel and 50q support equipment, 30 days | Moves a bounded population group to a real receiving state through shared migration rules |
| O-02 | Deny a threatened reserve | Actual selected equipment or fuel lot, 5 days | Moves a supported lot through real logistics or destroys it. Only the actual denied quantity reduces capture or consumption |
| O-03 | Secure a critical port or hub | 25 Army Experience, 50q support equipment and a 90-day objective | Requires a real garrison, supply and fortification program. Grants no permanent immunity |
| O-04 | Supply an anti-Cookie partner | 100q infantry equipment, 25q support equipment and 5q convoys where sea shipment is needed, 30 days | Delivers actual aid through a valid route. Sender and receiver ledgers agree |
| O-05 | Restore a liberated state | 100q support equipment, 5q trains and a 180-day construction objective | Repairs surviving infrastructure and restarts civilian production. It cannot recreate consumed people |
| O-06 | Leave emergency coordination | Existing participant | Loss of active coordination benefit and its future aid commitments | Ends only this package's agreement and leaves ordinary existing faction relationships intact |

Opponents cannot buy immunity from the Empire's external-neighbor war policy.
Their actions improve survival through actual resources, population protection, supply and defense.
The AI prioritizes feasible evacuation and key supply nodes instead of spending every available point on abstract warnings.

## Universal action contract

Before payment, validate owner, target, instance, resource quantities, route, cooldown and active-operation capacity.
After payment, record actual quantities, protected reserves and the exact promised result.
At completion, revalidate target control, eligibility and prior payment.
Apply each promised result at most once.

If an action is canceled, return only explicitly refundable surviving commitments.
Time already spent, transported fuel, consumed equipment, actual damage and lost civilians are not automatically refunded.
Each action has a saved completion state and a meaningful failure message.
Closing the interface does not cancel an operation.
Reloading does not redraw a cheaper target or repay a completed action.
