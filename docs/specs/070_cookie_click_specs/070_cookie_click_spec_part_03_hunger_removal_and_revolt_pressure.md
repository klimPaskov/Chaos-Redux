# 070 Cookie Click: hunger, removal and revolt pressure

## A missed feeding

A missed feeding does not immediately destroy the country.
The first incomplete cycle changes the expression and gives a small factual warning.
Subsequent hungry cycles permit self-feeding.
Resources taken by the cookie stay lost even when the relationship recovers.

The system records an internal hunger count `H`, a severe-starvation count `Z`, and consecutive completely unfed cycles `N`.
These are not additional public meters.
The player sees the present condition, the next known consequence and the available response.

At a cycle boundary, evaluate its completed feeding fraction.

| Feeding achieved | Hunger `H` | Severe starvation `Z` | Completely unfed `N` |
| --- | --- | --- | --- |
| Exactly 100 percent | Clear to zero | Clear to zero | Clear to zero |
| At least 75 but below 100 percent | Reduce by 1, minimum zero | Clear to zero | Clear to zero |
| At least 50 but below 75 percent | Unchanged | Unchanged | Clear to zero |
| At least 25 but below 50 percent | Increase by 1 | Unchanged | Clear to zero |
| Above zero but below 25 percent | Increase by 1 | Increase by 1 | Clear to zero |
| Zero accepted clicks | Increase by 1 | Increase by 1 | Increase by 1 |

A partial day can calm the cookie without paying the final reward.
That is a valid compromise, not a hidden failure.
It still adds lifetime clicks and therefore continues development.
Stopping at 75 percent forever cannot freeze the cookie at a low Level.

## Condition bands

A current empty bar is ordinary at the start of a day.
The face must therefore use feeding history as well as current Fullness.
An empty bar on the first morning is expectant, not already starving.

| Condition | Meaning and visible behavior |
| --- | --- |
| Expectant | A new cycle with no established hunger, eyes follow the pointer and the body leans forward |
| Happy | Recent feeding and a healthy relationship, bright crumbs and brief hearts |
| Satisfied | Today's target reached, slow contented animation and a locked feeding control |
| Hungry | `H` from 1 to 4, impatient movements and attention to resource icons |
| Starving | `H` at least 5 or `Z` at least 3, cracks, smoke, shaking and visible teeth |
| Angry | Repeated shortfalls after material predation has become available |
| Threatening | The revolt route is currently possible and its warning period has begun |
| Revolting | The uprising commit has started, feeding is permanently disabled |
| Recovering | A dangerous cookie is being fed again, hostile effects subside in clear stages |

Angry is a presentation state within hunger, not another score.
A satisfied high-Level cookie can still look physically dangerous without showing a false active threat.

## Bites

A hungry pet may take at most one mechanically significant bite per cycle.
At Evolution 0 the bite is small and uses soft national values.
Evolution I adds stockpiles and reserves.
Evolution II permits productive assets.
Evolution III permits major destructive consumption.

Starting internal bite budgets are 10, 25, 50 and 100 for Evolutions 0 through III.
Multiply by `1 + 0.25 × min(H, 10)`.
Then multiply by `1 + 0.05 × min(L - 1, 40)`.
Round to 5 and use actual registered packet values.
A weak cookie under the early-removal threshold is capped at 25 internal bite value per cycle.

A bite's severity and family must be saved before its effect is applied.
Its flavour follows the successful actual loss.
The cookie cannot announce that it ate trains after the selected train stockpile became empty and the fallback removed Political Power.

Do not let resource scarcity make the cookie harmless.
An empty pool leaves it hungry and advances eligible starvation pressure.
It does not create fictitious assets, negative equipment or unlimited compensation.

## Returning to feeding

Every accepted click immediately changes the face and suspends a bite that has not yet happened.
The suspension lasts until the next owner-local quarter-cycle review, at most 6 simulation hours.
It does not refund an earlier bite.

At that review, feeding progress of at least 5 percentage points since the previous review extends the suspension.
Reaching 75 percent suspends further predation for the rest of that cycle.
Reaching 100 percent clears hunger and cancels a pending revolt before commitment.

A single click cannot renew the pause repeatedly within the same quarter-cycle.
The quarter-cycle stores its last accepted progress checkpoint.
The cycle boundary still updates `H`, `Z` and `N` from actual progress.
A player who supplies isolated token clicks may delay individual bites but cannot erase severe starvation or a due revolt.

This is the precise meaning of returning to feeding: intervention stops the immediate next loss, while sustained progress determines whether the recovery lasts.
The tooltip shows the next review and the needed progress when this matters.
That timer is a temporary consequence notice, not a permanent third meter.

## Killing a weak cookie

At Evolution 0 a non-mature cookie dies after 10 consecutive completely unfed cycles.
At Evolution I it dies after 5 consecutive completely unfed cycles.
The lower maturity threshold at Evolution I makes the safe opportunity shorter.
Evolution II and III close the route entirely.

During those days it can still take small bites.
Its self-feeding does not reset the completely unfed count.
The distinction is intentional: early survival requires attention from the player, and scavenging national resources only delays visible deterioration within a day.
Self-feeding cannot make the weak cookie immortal.

Any accepted player click resets `N` at the next boundary.
The current removal attempt therefore ends when the player resumes feeding.
A click after the death commit is rejected.
An evolution or Level increase that permanently matures the cookie before the death boundary also closes this route, with a visible warning beforehand when the change was pending.

The death sequence has four visible stages: dryness, surface cracks, collapse into crumbs, and an empty plate.
The window then disappears after the player acknowledges the outcome.
All recurring pet callbacks become inert.
The normal fire-once history remains spent.
No reward, refund or positive national spirit is granted for this ending.

## A developed cookie

A mature cookie survives ordinary starvation.
Its hunger can reduce reward quality, deepen the next bite and eventually create a revolt opportunity.
There is no arbitrary instant-kill decision, permanent storage button, paid immunity, or unlimited “send it away” escape.

The host receives limited preparations that help fight the eventual uprising.
Those preparations do not erase Cookie Level or its historical rewards.
The player may destroy a real bakery anchor, distribute emergency equipment or evacuate an exposed state once those places and risks have become visible.
These are costly military preparations, not another way to collect daily rewards.

## Revolt eligibility

Evolution II requires Level 20, `H` at least 10 and `Z` at least 5.
Evolution III requires Level 15, `H` at least 5 and `Z` at least 3.
A valid host, valid uprising territory and a reserved country identity must also exist.

Once eligible, the cookie enters a 5-cycle warning period.
The player sees that the next step is a military uprising.
The exact army and territory are not guaranteed before the final snapshot, but the window identifies the threatened region and the broad strength band.
Feeding to at least 75 percent during a cycle cancels the pending revolt and reduces hunger normally.
Full feeding clears it immediately.

At Evolution II, after the 5-cycle warning, the design revolt weight is 20 against 80 for delay on each eligible cycle.
Commit by the tenth eligible post-warning cycle if recovery has still not occurred.
At Evolution III the corresponding weights are 40 against 60, with commitment by the fifth eligible post-warning cycle.
These are authored probabilities for the declared two-outcome pool, subject to the required engine probability audit.
No chance roll occurs on GUI open or click.

The deterministic latest deadline prevents indefinitely lucky starvation.
The warning and recovery rule prevent an unannounced random civil war.
The player cannot cancel a committed uprising by leaving a modal event unanswered.

## Loss of a viable host

Capitulation does not itself erase the cookie.
If the government remains playable with valid controlled territory, its feeding system continues.
If the owner is annexed or no longer exists, end the pet instance without transferring it to the annexing country and without returning consumed assets.

If the owner loses the territory needed to create both sides of the uprising, freeze the revolt countdown at its current warning stage.
Do not confiscate a foreign state or instantly annex the one remaining host state.
Cap destructive bites at the Evolution I material tier while the topology is invalid.
The window states that the uprising is blocked by territorial collapse.
Ordinary feeding and its costs continue.

Recheck that structural condition when the owner gains or loses a state.
The player can deliberately give up territory, but pays that real strategic cost and does not regain the safe starvation-death route.
This limitation must remain visible in acceptance tests.

## Host preparation and resistance

The host may prepare a reserve force, move civilians from the threatened industrial area, and disable one exposed bakery site.
These actions appear only after a concrete site or threat exists.
They can reduce a specific uprising component by up to 25 percent.
They cannot stack to eliminate the army, remove all starting territory or permanently halt the revolt.

Evacuation uses the shared migration contract and actual receiving capacity.
It is not population destruction.
Destroying a bakery removes or damages real buildings and reduces only the industrial part of the Cookie reserve.
After revolt, the same prepared depot can supply the host's resistance campaign.

A successful defence kills the Cookie Monster and ends that instance.
The host receives relief and reconstruction opportunities.
It does not get its historical rewards paid a second time or its consumed population restored.
