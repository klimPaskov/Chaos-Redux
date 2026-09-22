# Decisions and missions

Each phase presents a small useful set of actions.
Keep three to five primary visible actions and normally one to three active missions in the current category.
A hard ceiling of six primary actions prevents a long shopping list.
Targets and completed options are filtered by relevance.
A collapsed or separately revealed advanced category is preferable to showing all possible future offers at once.
The full action inventory is in 072_action_register.json.

## Categories

| Working category | Available period | Main actions | Territorial display |
| --- | --- | --- | --- |
| Reclamation | Active attempt | Opening objective, preparations, extension, holder response | Compact northern objective state display |
| United Ireland | Successful campaign | Constitution, repairs, services, integration | Exact Irish integration state puzzle |
| National Development | Successful campaign | Army, production, culture, air and fleet programs | Normal focused project status |
| Gaelic Empire | Imperial commitment onward | Scottish settlement, claims, integration, proclamation | Exact imperial state puzzle |
| Celtic Compact | Cooperative opening onward | Offers, charters, league and federation | Exact member-qualification state puzzle |
| Atlantic Policy | Maritime opening onward | Access offers, port programs, overseas capacity | Exact finite access and administration state puzzle |

Every category containing formation or territorial integration actions is included in the strict attachment audit.
National Development has no territorial formation or integration action and is explicitly outside that family.
Do not move a formation decision into that category later without adding the corresponding puzzle attachment.

## Objective mission

The 180-day reclamation mission begins only after successful commitment of the opening war.
It shows the northern province-control requirement, five-day holding period, time remaining, and the new-tree reward.
Its success callback invokes settlement resolution automatically.
The holder's report states the same rule.
A maximum one-time 90-day extension follows the requirements in the war specification.
No focus or Political Power payment is required after victory to obtain the peace or tree.

## Domestic project sequence

The constitutional mission lasts 90 days and consumes the chosen policy's accepted investment once.
A 120-day reconstruction project can run alongside it.
The first public-service agreement lasts 90 days and follows the chosen staffing approach.
The North's full integration contract requires the appropriate Settlement level and 180 days of secure Irish ownership and control where a core still needs to be earned.

Direct central rule begins its administrative effect earlier but does not instantly fulfill a civic guarantee it has declined.
A failed worksite due to occupation pauses its remaining committed work and exposes a recovery condition.
If the government changes the project's own policy to an incompatible one, it cancels the remaining work under the recorded refund rule.
Completed benefits do not reverse unless the policy explicitly replaces them.

## Foreign offers

An offer records its recipient, current sovereign holder, target states, type of agreement, exact cost, accepted obligations, and expiry.
A standard diplomatic offer expires after 30 days.
Resource payment occurs only after a valid acceptance and a second affordability check.
Displaying an offer or sending a refusal does not spend the proposed transfer.
Preparation fees are separate, explicit, and non-refundable only when the decision describes that cost before submission.

An accepted offer can begin a 90-day charter or a 180-day investment mission.
A rejected offer has a 180-day cooldown against the same counterpart and agreement type.
A materially changed state of sovereignty, government, war threat, or Irish policy may allow a new proposal under an explicit rule.
The system does not secretly increase the acceptance probability after repeated payment.

## Investment commitments

A civilian-factory commitment is capacity reserved for a finite project, not a permanent factory deletion.
Implementation must use an existing verified repository mechanism or another documented engine-supported representation.
If that mechanism is unavailable, replace the project with a disclosed finite construction-resource cost before shipping and update every display and helper.
Do not invent a Clausewitz effect that directly subtracts factory-days.

The stated design commitment is one or two available civilian factories for the recorded number of days.
The capacity is released on completion, cancellation, country loss, or project invalidation.
It is not released twice by both a mission callback and an event callback.
A lack of capacity blocks acceptance.
A later temporary shortfall pauses work without manufacturing negative factories or continuing a free project.

## Cost contract

Each action has at most four distinct spendable resource types.
Political Power, Army Experience, manpower, equipment families, and factory commitments count as separate types when actually spent.
A duration, cooldown, Settlement requirement, Strain threshold, or number of target states is not a spendable resource.
Display up to three cost icons inline and all costs in the full tooltip.
Use the actual final modified amounts and the established text icons.

One helper supplies affordability and another single owned payment path executes the exact quoted cost.
The display, AI eligibility, decision availability, acceptance recheck, and payment use the same frozen offer or project values.
A balance exactly equal to the cost must pass.
Rounding is performed once using the supported project increment and never differs between the tooltip and effect.

The decision click or accepted offer must recheck all target and cost conditions immediately before commitment.
A stale popup cannot transfer territory, reserve capacity, or deduct stockpiles after the recipient has changed.
Double clicks and multiplayer callbacks are idempotent.
If the transaction cannot complete, no uncommitted resource is spent and the player receives the actual reason.

## Refunds and interrupted work

Military training and procurement fees are consumed when work begins and are not refunded after ordinary military losses.
Unaccepted diplomatic offers spend no transfer resources.
Reserved civilian capacity is released when future work ends.
Completed factory-days do not become a Political Power refund.
A sovereignty-transfer offer that fails revalidation pays nothing.

A cancelled contract that held an explicit equipment escrow returns the recorded surviving escrow once, provided the implementation supports that representation reliably.
Prefer payment at delivery or acceptance over inventing a complex escrow system.
No arbitrary multiplier creates more equipment than was originally committed.
The action register specifies which operations are immediate, mission-based, or recipient-accepted.

## Mission design and failure

A mission must state a reachable objective, total duration, actual progress condition, success reward, interruption rule, and final failure result.
Costs alone are not the objective of an operational exercise.
A fleet exercise needs a suitable fleet and facilities.
A federal charter needs accepted member obligations.
An integration project needs the actual state group.

Do not punish a failed minor training program with an unrelated nationwide crisis.
Its natural loss is spent preparation, delayed capability, and a cooldown before retrying.
An interrupted treaty can suspend the benefit and create a targeted diplomatic repair action.
Failures should offer a sensible recovery choice without erasing the opening victory or awarding new free forces.
