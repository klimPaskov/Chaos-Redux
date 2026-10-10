# 05. Interference and counterplay

## Choosing an opponent

A sponsor chooses one registered rival in the same target. The selected rival is locked into the action record at confirmation. Changing the board's target or leading-rival display cannot redirect an operation already in progress. Another country with the same ideology is still a valid rival.

Interference uses the political slot and has its own 30-day per actor-target cooldown starting when the operation completes. All variants share that cooldown. A sponsor cannot start a new version to bypass it. The action displays the rival's current score and the maximum removable amount under its loss budget.

## Operations

The following labels are working labels, not final localisation.

| Operation | Stage | Cost | Duration | Rival loss anchor | Conditions and additional effect |
| --- | --- | --- | --- | --- | --- |
| Counter-propaganda | Baseline | 30 political power | 20 days | 10 | Rival has Influence above zero. Can challenge an active or recently completed political campaign. |
| Expose foreign interference | Influence Campaigns | 60 political power | 20 days | 15 | Rival has a valid exposed operation from the preceding 60 days. Removes that exposure record after a successful report. |
| Competing investment offer | Influence Campaigns | 50 political power and 1 civilian factory reserved | 30 days | 15 | Sponsor has delivered an investment in this target. The factory reservation funds the competing offer, not a new building. |
| Diplomatic pressure | Influence Campaigns | 75 political power and 15 command power | 25 days | 15 | Sponsor has a qualifying security relationship or a verified adjacent military position. Does not declare a war. |
| Coordinated blocking campaign | The Great Game | 100 political power | 20 days | 20 | Selected rival has at least 75 Influence. Creates a public blocking-coalition invitation for other registered sponsors. |

Counter-propaganda is usable without spies. Exposing a stronger operation can use an intelligence provider to qualify evidence, but direct visible exposure is also sufficient. A country lacking the relevant DLC is not excluded from interference.

All losses are deterministic after eligibility and completion conditions are established. Do not add an unseen random success percentage. Intelligence advantages should appear as evidence access or a clearly shown shorter duration, not a secret chance to nullify the player's expenditure. Any future stochastic operation requires a separate probability audit and a disclosed failure result.

## Loss budget and saturation

Each target participant has a rolling 30-day budget for Influence removed by rivals:

| Stage | Maximum rival-inflicted loss in a rolling 30-day window |
| --- | --- |
| Baseline | 10 |
| Influence Campaigns | 15 |
| The Great Game | 20 |

At completion, actual loss is the minimum of the operation's anchor, the rival's current Influence, and its remaining loss budget. Count all hostile sponsors together. A coalition cannot multiply this cap by adding more members. Inactivity decay is separate and does not consume the budget.

Show the remaining budget in the expanded rivalry tooltip. Starting an operation with no possible loss is disabled. A budget can be consumed by somebody else's operation before yours completes. In that case the operation makes the remaining legal reduction and refunds the unused portion of its paid political-power component proportionally, rounded down. Command power and already used industrial time are not restored. This risk is shown before confirmation.

A zero-score rival never grants a benefit. No operation gains Influence merely by targeting a weak country. Exposure and counter-propaganda affect the rival's position without transferring it to the attacker. The attacking sponsor still needs positive campaign completions to win.

## Blocking coalitions

A Great Game blocking campaign invites the other contestants to back one action against the leader. A sponsor joins by paying 25 political power and committing its political slot until the action completes. Joining only speeds the action up: with two funded members it finishes 15 days after it started, with three or more 10 days after it started, and never sooner than 5 days after the latest join. The board shows the revised date to every member.

The loss stays capped at the operation's anchor of 20 and the victim's common loss budget, so a coalition is faster, not stronger. If the initiator drops out, the oldest remaining member completes the action. When it completes the coalition dissolves, and members compete against one another again under their normal cooldowns. Weaker sponsors can slow an imminent winner this way without a permanent alliance system.

## Defending a lead

A leader can diversify action families to maintain forward progress, complete funded material work while rivals use political slots against it, replace an exposed institutional relationship, or simply conserve resources until its loss budget is exhausted. There is no paid immunity button that makes it impossible to contest the leader.

The budget protects against arbitrary dogpiling, while the action slot and time cost make attacks expensive. Balance review must confirm that saturation, inactivity, and loss limits still let contested races finish. If normal campaigns stall indefinitely, adjust the published loss cap or gains rather than adding hidden AI mercy or an automatic victory timer.
