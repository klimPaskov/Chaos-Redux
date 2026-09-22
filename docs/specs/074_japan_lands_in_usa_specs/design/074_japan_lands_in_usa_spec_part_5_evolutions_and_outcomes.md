# Part 5: Evolutions and the end of special support

## Starting tier

Read the current Chaos value and the enabled stages when the landing commits.
Choose the highest enabled tier whose threshold is met.
The baseline applies below 200 Chaos or when no eligible evolution is enabled.
The tier is then frozen for that opening transaction.
The army does not change halfway through a report because another event modifies Chaos.

| Stage | User-supplied name | Chaos threshold | Main change |
| --- | --- | ---: | --- |
| Baseline | Japan Lands in USA | Below the first enabled threshold | A compact but substantial mainland front |
| I | Pacific Army | 200 | A larger and better-supported regional army |
| II | The Western Invasion | 400 | Several coastal positions and a wider western campaign |
| III | Invasion of America | 600 | A very large continental army and several secured entry points |

A stage toggle controls that stage's activation and presentation.
An enabled higher stage may be selected even if a lower stage is disabled.
That selection does not record the disabled stage as having activated, play its report, or grant its package separately.
The selected higher-tier budget already includes the force appropriate to that tier.

## Active evolution

An ongoing supported expedition can evolve after its opening.
Crossing a threshold makes the next enabled higher stage eligible for a delayed activation process with a proposed MTTH around 90 days while its conditions remain valid.
This is a timing design target, not a verified cumulative probability.
The current game-version timing adapter must determine actual behavior during implementation.

The active expedition must still have working Pacific access, remain in the Japanese-American war, and have a valid receiving area.
An ended episode, a permanently closed support system, or an extinguished country cannot evolve.
Falling below the relevant threshold pauses eligibility.
A completed evolution is not reversed merely because Chaos later falls.

Only one next enabled stage is considered at a time.
After it activates, a separate delayed process can consider the following stage.
A sudden increase to 600 Chaos during a baseline campaign does not deliver three full armies in the same hour.
A disabled intervening stage is skipped without producing its own effects or report.

## Upgrades are differences, not replacements

The opening scale factor remains the same.
For every grant family, compare the new authorized cumulative ceiling with the amount this event has already issued.
Issue only the positive difference due at that stage.
Current stockpiles and current surviving divisions are irrelevant to the calculation.
Losses and disbanding do not reduce the amount previously issued.

For example, a baseline expedition that has already received 30 opening divisions and both five-division follow-on batches has received 40 divisions in total.
At unscaled tier I, the immediate cumulative target is 60.
The upgrade can add 20 divisions, followed later by no more than the remaining allowance up to the tier I lifetime ceiling of 75.
It does not add a fresh 60 on top of the earlier 40.
If some earlier divisions were destroyed, they remain counted against these totals.

Use the same principle for embedded manpower and equipment, aircraft, loose reserves, and completed projects.
When a delivery is not physically possible at that moment, keep the undelivered amount bounded and explicitly pending.
Do not change an enemy province to Japanese control merely to find room for it.
Do not label a pending force as already present in America.

## Evolution I: Pacific Army

The expedition receives its first major increase in force, artillery, aircraft, replacement stocks, and follow-on capacity.
The larger army should be able to hold its coast while forming an offensive concentration.
It should not simply double the number of divisions standing on the same port tile.

At initial tier I entry, the broader starting position normally has two working ports and greater deployment depth.
During an active upgrade, additional troops use retained access and controlled territory.
New ports outside the opening still have to be captured.

The extended support horizon is 240 days from the original landing.
This gives the player more time to restore transport and establish a second operating direction, while the original full-support grace period remains spent.

## Evolution II: The Western Invasion

At initial tier II entry, Japan can begin with several coastal positions in more than one state.
Each pocket receives a coherent defensive force, transport access, and an objective that can connect it to the wider campaign.
The increased air and reserve package supports more than one active front.

During an active upgrade, the army and support budget grows through existing access.
A second region that Japan has captured through normal fighting becomes a valid recipient.
The event does not grant another surprise occupation behind the American line.

The new operational problem is whether to connect coastal pockets, deepen the main California front, or use a northern position to stretch American defenses.
The support horizon becomes 300 days from the original landing.

## Evolution III: Invasion of America

At initial tier III entry, the landing is a large coordinated invasion with several prepared Pacific access points and an enormous army.
Prefer a California-centered operation with substantial northern positions when the actual American-owned coast permits it.
The army must have enough space, supply, aircraft basing, and command organization to create a major theater immediately.

At active tier III entry, issue the remaining authorized increase through retained access.
The map decides how broad the realized invasion is.
The event may have a huge army in a narrower surviving front if the United States has already retaken the northern coast.
Reports must describe that actual situation instead of claiming that several states were just occupied by script.

The support horizon becomes 360 days from the original landing.
This is the last support tier.
Further Chaos increases do not create more stages, another landing episode, unlimited supply, nuclear weapons, or a world-ending route.

## High-tier presentation

Ordinary news covers every committed landing.
A separate tier III super-event is justified only after a large force has actually arrived and the realized front has several useful access points in at least two Pacific states.
The proposed material threshold is at least 90 percent of the tier III immediate cumulative force target issued into the episode and at least three working access points.
A research-backed presentation package is required before this special presentation is considered complete.

If an initial high-tier landing is constrained to one legal region, ordinary news and reports still describe the large army.
The super-event waits for the geographic condition during the supported episode and can play only once.
This presentation gate does not reduce the military grant or add a strategic availability condition to Event 074.

## Loss of access

A detached pocket first enters local isolation when it loses its working port and has no land route to another working registered access point.
Its reserved deliveries stop immediately and its local support contribution tapers away over seven days.
Other supplied Japanese pockets keep operating.

If all Pacific access remains lost for 30 continuous days, close special support permanently.
The army can still fight inland and recapture a port through ordinary combat, but doing so after closure does not reopen reserved grants or the active evolution process.
This prevents a series of free late landings disguised as reinforcement.

A port regained before the 30-day closure can restore only the unspent support that still fits inside the original absolute support horizon.
It does not reset the horizon, restore spent materials, or revive a previously destroyed follow-on batch.

## Ordinary ending states

| Observed outcome | Event response |
| --- | --- |
| Japan loses the coast but continues fighting inland | Close or suspend support according to the access clock and describe coastal loss accurately |
| Japan loses its American positions | Record containment, remove transient support, and keep normal war rules |
| Japan holds a large American theater after support expires | Remove exceptional support and let the ordinary campaign continue |
| The United States capitulates | Observe the normal result, preserve ordinary ownership rules, and close completed mission surfaces |
| Japan capitulates but continues to exist in the war | Let the engine's ordinary country and unit rules operate, with no invented rescue state |
| Japan ceases to exist | End callbacks and pending grants without recreating Japan |
| The Japanese-American war ends | Cancel this episode's future military effects and respect the actual settlement |
| War resumes later | Do not reopen Event 074 or restore its expired support |

## Settlement and cleanup

Support closure removes exceptional landing supply, unissued reserve lots, unissued granted formations, J01 access, and future active evolutions.
It does not end an ongoing mainland war or delete paid projects merely because their owner has reached the support deadline.
J02 through J04 and the American actions may continue within their original lifetime allowances while meaningful mainland operations remain.
Operational missions keep their original deadlines and may complete through ordinary combat after support has ended.
Their grant-acceleration reward has no effect once the relevant grant system has permanently closed.
Mainland AI priority remains while the actual front requires it, with ordinary retreat and home-defense considerations.

Campaign-operation cleanup occurs when the bilateral war ends, a required country ceases to exist, the United States capitulates and the invasion mission set resolves, or no Japanese mainland operating force or occupied operating area remains for 30 days.
That cleanup removes remaining event-owned operational modifiers, pending paid projects through their cancellation rules, missions, and temporary AI strategies.
It preserves surviving ordinary units, real buildings, actual territorial settlement, fired history, earned achievement evidence, and already-recorded Chaos receipts.
Achievement tracking can continue after operational cleanup where a defined later accomplishment requires it, such as the American original-capital objective.
Use bounded shared achievement hooks and the original deadline, not a surviving event decision category as proof of eligibility.

Do not automatically return every selected province to the United States at the end of the war.
Do not leave Japanese ownership behind because the opening used the wrong transfer effect.
Do not revoke another event's supply support, national spirit, AI strategy, or occupation effect when removing Event 074's own contribution.

Support expiry and war ending are terminal for this event's grants.
The normal Japanese and American campaigns continue beyond the event's management layer.
