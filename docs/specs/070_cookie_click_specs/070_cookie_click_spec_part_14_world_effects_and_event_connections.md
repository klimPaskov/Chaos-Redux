# 070 Cookie Click: world effects and cross-event behavior

## Chaos impact

Cookie behavior contributes to Chaos through meaningful consequences.
The ordinary event's catalog Chaos level remains 1.
That catalog classification does not require every internal daily click to add Chaos.
The values below are authored milestone contributions, separate from generic war, death, annexation and tension sources.

| Milestone | Event-owned Chaos | Once-only or anti-farming rule |
| --- | --- | --- |
| First living Cookie becomes publicly active | +2 | Once per normal campaign opening |
| First material reserve is actually consumed | +3 | Once per instance, not per equipment family |
| First factory level is permanently consumed by a pet | +5 | Once per instance after an actual level debit |
| Cookie Empire forms and demonstrates a viable armed uprising | +10 | Once at committed formation, distinct from generic war declarations |
| Empire first establishes a working region of five controlled states | +5 | Once, using actual maintained control |
| First Cookie subject or converted administration becomes operational | +5 | Once, not per release or re-annexation |
| Empire first reaches a second major geographic theater with a supplied force | +10 | Once, not for each border touch |
| A major late military capability becomes operational | +5 | Once for the first such capability, not for each template or technology |
| The Final Bite begins its global consumption campaign | +25 | Once, not per queued declaration |
| A weak pet is permanently starved before material escalation | -2 | Once, never more than the event-owned disturbance it actually created |
| An established Cookie Empire is defeated before The Final Bite | -10 | Once after real defeat |
| An active Final Bite campaign is defeated | -25 | Replaces the previous defeat reduction, not an additional reward |
| Final Cookie-world result | No arbitrary second launch spike | The actual campaign has already produced its escalation and shared losses |

These additions do not replace shared effects.
Actual civilian deaths go through the shared death system.
Actual war declarations and annexations keep their generic consequences.
Do not add an extra per-million population loss directly in Event 070 when the shared system already accounts for that loss.

Manual launch records current actual manifestations once.
It does not reproduce the normal opening's fictional history or pay the milestones of events that never happened.
Scenario initialization must distinguish an immediate real uprising from synthetic strength information.

Containment reductions cannot be farmed by repeated subject release, capital moves, cosmetic tag changes, temporary loss of control or an old defeated instance's callbacks.
The chosen milestone history survives save and reload.
Natural later changes in Chaos do not erase it.

## World threat

A dangerous uprising and The Final Bite contribute a Cookie-owned world-threat source.
The normal small living pet does not automatically mark the entire world under threat.
Register the new Cookie source in the shared aggregator before using it.
The documented `refresh_world_threat_state` helper only aggregates registered sources.
Setting an arbitrary unregistered flag would not be sufficient.

The Cookie source becomes active when a viable Cookie Empire is fighting or when its established destructive campaign remains unresolved.
It ends on confirmed defeat or the settled terminal result where no organized opposition remains.
Clearing it removes only Event 070's source and then refreshes the aggregate.
Do not directly clear the shared `world_in_threat` flag while plague, zombies or another source is still active.

## Population, recruitment and migration

Population consumption reduces actual state civilians and records the actual resulting deaths.
Population conversion reduces civilians and creates Cookie manpower through a distinct documented transformation outcome.
Evacuation moves living people to a valid destination.
Manpower spent on a Cookie military process is neither automatic civilian death nor automatic migration.

Use `apply_exact_state_civilian_population_loss` for an exact supported civilian debit when its death-reporting behavior matches the operation.
Use the documented population-loss helper to avoid native recruitable-manpower side effects where required.
Read their current parameters and output variables in the repository before implementation.
Do not infer a transformation-safe option solely from the helper name.

The affected state's actual available population, configured floor and shared safety constraints clamp every operation.
The tooltip and result use the actual amount, not the requested amount.
Where a full requested batch is impossible, a smaller complete supported batch can resolve.
An unsupported conversion outcome remains blocked until its helper contract exists.

People already evacuated cannot later be eaten from their former state.
People eaten cannot be restored by repairing a railway.
A reconquered state carries its demographic loss and relevant migration history.

## Infrastructure and destruction

Eating equipment, damaging a building and destroying a building level are three different transactions.
Damage uses an appropriately smaller food return.
Permanent destruction removes actual levels and reduces future industrial and feeding capacity.
A single asset can be counted once at the time of its actual irreversible consumption.

A stored building-consumption history is not itself a second penalty.
It prevents the same physical damage from being claimed repeatedly.
Legitimate new construction creates a new real asset that can later be consumed, with its actual cost paid by whoever rebuilt it.
There is no free first-time grant when control changes.

Ordinary repairs follow ordinary construction constraints.
Special reconstruction programs accelerate real work at a cost.
They do not create invisible factories outside state slots or repair an occupied enemy state through an unchecked effect.

## Diplomacy and postwar outcomes

The host stays a meaningful country throughout a viable initial uprising.
Its existing focus tree, history and leaders remain unless actual war outcomes change them.
Victory over the Monster creates a reconstruction phase and ends the pet permanently.
A failed host can be occupied, annexed or converted through the Empire's chosen postwar method.

The Cookie Empire does not borrow an existing living vanilla tag.
Ordinary countries released as Cookie subjects keep appropriate existing identities and meaningful trees.
Where a conversion program changes their political identity, the change receives a deliberate cosmetic and political package.
No cosmetic tag grants free cores or silently replaces every local character.

The Empire's capital uses the strongest valid city in its compact starting region, prioritizing a real supply node.
Save a backup capital from remaining owned controlled eligible states.
Re-evaluate only when control or ownership changes.
Use a descriptive cookie-themed administrative name for the capital and the first major bakery only after final localization is written.
Do not rename every city just because it was temporarily occupied.

A region under direct long-term Cookie conversion can receive a bounded naming pass for its capital, important industrial city and major port.
Farming administrations retain local geographic names because their purpose is to preserve functioning human administration.
Temporary front occupations retain existing names.
These differences express the route's method without inventing a large irrelevant map-name system.

## Event 066, Abundance

The new brief proposes sharing value-registration information with Abundance.
The supplied catalog snapshot still identifies Event 066 differently, so the design must not assume a finished Abundance implementation or registry already exists.
The desired shared boundary is a neutral resource registration with valid scopes, bounds and safe operations.

Event 066 owns its selection, increases and reward presentation.
Event 070 owns appetite, selection for consumption, debits, Fullness, Level and revolt.
Neither event calls the other event's private progression logic.
A neutral adapter can expose a value to both, one or neither system according to supported operations.

Abundance can replenish a real stockpile that the Cookie can later consume.
That is a meaningful interaction.
It does not count as a Cookie reward for lifetime reward scaling.
Only a payout actually owned by the Cookie system increases its reward-value history.

## Other event connections

| Connected system or event | Allowed interaction | Boundary |
| --- | --- | --- |
| Great Depression and industrial crises | Damaged output makes farming and reserve production harder, and can alter valid reward families | Do not cancel the other event's modifiers or remove its private state |
| Industrial Boom and new infrastructure | Actual extra industry, routes and stocks can support the Cookie economy or become edible assets | Do not treat promised construction as a completed asset |
| Black Market | Purchased compatible material can be fed or converted after it is actually received | Cookie logic never edits market contract completion |
| Abundance | Real valid increases can replenish edible values | Cookie reward history counts only Cookie-owned payouts |
| Population increase and migration | Actual current civilians and receiving capacity change valid consumption and evacuation | No synthetic population, migration or death double counting |
| Zombies, plague and other civilian crises | Existing damage and displacement influence valid population, control and farming | No automatic immunity because the ruler is a biscuit |
| Research Failure and scientific events | Current supported research state can affect valid research gifts and edible progress | Unsupported progress setters are not replaced by unrelated speed modifiers |
| Border Fortifications | Actual forts can slow an uprising and form defensive objectives | No special bypass through a hidden Cookie attack bonus |
| Divisions Lock | Recruitment and scripted formation grants obey the active shared restrictions unless an explicit inter-owner exemption is agreed | Do not silently defeat another event's central rule |
| Country fragmentation and independence | New borders can create valid new enemies and invalidate old mission targets | Rebuild only relevant actor and border sets, with saved history retained |
| Other world-end campaigns | Their active conditions coexist unless the shared scenario policy expressly excludes them | No unconditional cleanup of another owner or false global victory |

A connection requires a real published interface or a narrow reviewed extension.
Listing an interaction here does not claim that the corresponding current repository implementation supports it.
Unsupported links remain visible implementation blockers with their proposed owner.

## Cookies without the original player

Normal opening selection is human-only.
An existing cookie stays owned by its country when the human disconnects or changes control.
It does not move to the next human player and does not reopen an already paid cycle.

The default session policy keeps the ordinary simulation-time feeding rules.
No hidden AI auto-clicker feeds the cookie, grants free human-click progress or replaces the player's effort.
Multiplayer groups can pause the simulation through their ordinary controls while a player reconnects.
The Cookie system itself does not pause the whole game.

For a permanently AI-controlled former host, expose one explicit host-authorized continuity setting in campaign setup.
Its alternative suspends future pet hunger and feeding rewards together while no human controls the country.
It freezes the remaining warning interval and cycle state without awarding clicks, Level, rewards or achievements.
This alternative is disabled by default because the brief makes neglect consequential.
Its active periods disqualify continuous-care achievements.
A human cannot toggle it from the feeding window to escape an imminent revolt.

A Cookie Empire is different.
Its country AI uses the actual economy, reserve policies, units and focus routes.
It never needs pet clicks after the uprising.
Changing between human and AI Empire control does not change its food recipe, free starting package or declared wars.

## Saved world and completion

All permanent reward entitlements, population losses, consumed assets, milestones, manual eligibility and country-creation stages belong to an instance.
Country control and tag changes do not transfer old history to an unrelated actor.
The main system ends through weak death, confirmed Empire defeat, a settled terminal world result, or owner removal under its documented lifecycle.

Completion removes recurring pet callbacks, stale targets, pending warnings and event-owned presentation.
It does not erase actual war damage, living countries, spent equipment, completed technologies or properly granted permanent rewards.
Temporary contracts expire according to their own terms.
No cleanup routine deletes another event's modifiers because their names contain a similar word.
