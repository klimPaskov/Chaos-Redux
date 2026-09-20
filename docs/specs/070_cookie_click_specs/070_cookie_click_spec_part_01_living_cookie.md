# 070 Cookie Click: the living cookie

## The relationship

Cookie Click begins with a living biscuit delivered to a player-controlled country.
Its first rewards should be useful immediately.
The player learns that feeding it also increases tomorrow's workload and the strength of a possible future enemy.
A country may keep feeding it, leave a weak specimen to die, manage a developed specimen through periods of shortage, or deliberately prepare for its eventual uprising.

The normal opening is Minor Fire-Once, Chaos level 1, with no cluster.
Its root is `chaosx.nr70.1`.
The opening owns a persistent country system, so daily rewards, threats, level increases and the revolt never request another Event 070 selection.
The player who receives the opening owns the cookie.
Other players receive relevant world news, not duplicate cookies.

Normal selection requires a living player-controlled country with a valid capital and at least two owned and controlled states from which a viable uprising could be formed.
This territorial requirement prevents a promised civil conflict from immediately deleting a one-state host.
The player need not have a large army, factories, a coast, a faction or a particular ideology.
Countries with one eligible state are a documented structural limitation of this plan.
Do not invent province ownership splitting to evade it.

One normal cookie instance exists globally.
The framework's shared event history records the opening once.
Country countdowns do not create independent copies of the instance.
Manual scenario launches can revive the concept after a previous instance has ended, but cannot silently destroy or overwrite another active cookie instance.

## What the player sees

The main window has two persistent public values.

| Value | Meaning | Player response |
| --- | --- | --- |
| Cookie Fullness | Feeding progress toward the current day's requirement, from 0 to 100 percent | Click the cookie, finish the day, or deliberately stop |
| Cookie Level | Permanent development from lifetime clicks and completed feeding cycles | Decide whether further rewards justify greater appetite and future danger |

The current accepted click count and today's frozen target sit beside the Fullness bar.
Lifetime clicks belong in the Level tooltip.
A short condition label communicates contentment, hunger, starvation, recovery or revolt preparations.
No separate relationship, anger, awareness, appetite, corruption, threat or experience meter is added.

Fullness uses a warm green visual identity while healthy and changes through amber to dark red as hunger becomes dangerous.
Level uses gold.
Shape, expression and concise text communicate the same information without relying on color alone.

The default opening shows a small, friendly cookie.
The early warning is concrete: feeding makes it grow, developed cookies cannot always be starved safely, and missed feeding can cost national resources.
Do not reveal the exact appearance of the final monster in the opening.

## The first day

The owner receives a complete 24-hour feeding cycle from the opening time.
The system does not demand 300 clicks in the few minutes before an unrelated global midnight.
Subsequent cycles stay aligned to that owner-specific game-time boundary.
Only simulation time advances the cycle.

A baseline cookie begins at Level 1 with a target of 300 accepted clicks.
It starts with an empty feeding bar and no inherited hunger.
The first cycle cannot cause a bite or a revolt.
This opening grace does not award any feeding reward.

The player can open and close the window without spending anything.
Closing it does not pause the cookie.
Pausing the game allows clicks within the current cycle, but cannot produce another day or another full-cycle reward.

## Daily target

The following formulas are authored starting balance, not measured engine behavior.
All their inputs are saved owner data.
The implementation should expose their constants in one Event 070 tuning surface.

Let `C` be lifetime accepted clicks, `D` completed full feeding cycles, `S` the consecutive full-cycle streak, `V` the total reward value actually paid, and `L` Cookie Level.
Let `ceil25(x)` round upward to a multiple of 25.

```text
development = C + 500 × D
L = 1 + floor(sqrt(development / 1000))

streak_step = min(10, floor(S / 5))
reward_step = min(10, floor(V / 500))
lifetime_step = floor(C / 10000)

base_target =
    300
    + 25 × (L - 1)
    + 25 × lifetime_step
    + 25 × streak_step
    + 25 × reward_step

evolution_factor = 1.0, 1.5, 2.0, 3.0 for Evolution 0, I, II, III
next_target = ceil25(base_target × evolution_factor)
```

The target can therefore grow from hundreds into thousands without changing the meaning of one click.
A 20,000-click safety ceiling protects the counter and presentation contract.
Reaching it must be reported as a saturated target, not wrapped to a smaller number.
The ceiling is a deliberate extreme-campaign limit, not an excuse to cap ordinary progression at a few hundred clicks.
Level and rewards continue to advance at that ceiling.

A broken streak reduces only the streak component.
Lifetime clicks, rewards already earned and permanent maturity are not erased.
The player cannot turn an old dangerous cookie back into a harmless one by missing a day.

Freeze the target when the cycle opens.
A level increase, an evolution activation, a change of government, or a resource cap reached during the cycle cannot move the current finish line.
Those changes affect the next cycle.
The window may show a short next-day warning after a large increase.

## Fullness and the cycle boundary

During the pet phase, Fullness is `100 × accepted_cycle_clicks / frozen_target`.
Every accepted click supplies one feeding unit.
The cookie's daily appetite consumes the previous cycle's capacity at the next boundary, so the new cycle starts at zero.
Partial feeding does not become an accumulating click debt.
Its consequences survive through hunger and lost rewards.

Resolve a boundary in this order.

1. Complete any already accepted click transaction belonging to the old cycle.
2. Resolve its unpaid milestone, final reward and level-up entitlements once.
3. Classify the old cycle's feeding result and update hunger, removal and revolt conditions.
4. Resolve a due bite or an already due revolt commit using the old cycle's result.
5. If the pet still exists, derive the next target and reward track, then open the new cycle.

A click assigned to the new cycle never repairs a completed old cycle.
A click that completed the old cycle before a revolt commit cancels that pending revolt.
After the commit, no click changes the relationship.

## Reward milestones

The milestones are 25, 50, 75 and 100 percent of the frozen target.
The required integer count for each is rounded upward.
Their paid flags belong to that cycle, not to a GUI window instance.
The last reward requires the exact target to be reached.

The four shares of the day's reward budget are 20, 20, 25 and 35 percent.
Each share buys a valid packet or combination of packets from the reward registry.
Unused sub-packet value flows to the next milestone in the same cycle.
At the final milestone, pay only complete valid packets that fit within its remaining budget.
A sub-packet remainder expires without a payout.
Never round a small remainder upward into a free minimum packet.

Each physical press causes an immediate visual response.
Only accepted clicks change the count.
A full cookie ignores further presses mechanically and gives a brief satisfied reaction instead.
No heavy resource search, equipment enumeration, world scan or probability reroll runs on every click.

## Permanent development

Level is derived from the saved development total, not from a second public experience meter.
Both clicking and completing cycles matter.
Completed cycles are deliberately more efficient than repeatedly collecting only the first milestone.

Ordinary level increases improve future daily quantities.
Crossing Levels 5, 10, 15, 20, 30, 40 and 50 also unlocks a larger development reward and a new visible or mechanical development beat.
Further Level 10 intervals retain the late-development reward pattern.
Every threshold has a permanent paid flag.
Several thresholds crossed in one transaction are resolved as a single clearly itemized package, without duplicate grants.

| Level band | Appearance | Relationship change |
| --- | --- | --- |
| 1 to 4 | Small biscuit with simple eyes, short crumb limbs and a soft expression | Easily understood early rewards and a clear removal opportunity |
| 5 to 9 | Thicker body, icing details and more deliberate reactions | Larger rewards and a noticeably higher daily requirement |
| 10 to 19 | Decorated body, small crown and a proprietary attitude | Permanent maturity at baseline, more demanding behavior |
| 20 to 29 | Oversized cookie pressing against its frame | Serious reward engine and a credible revolt route |
| 30 to 49 | Heavy crown, sharp grin and visible strain in the surface | Large national rewards with expensive neglect |
| 50 and above | Monstrous mass still capable of looking pleased | Extreme appetite and a powerful possible uprising |

Evolution overlays modify these bands.
They do not require a separate complete body for every Level number.

## Maturity

Maturity is permanent once gained.
At Evolution 0 it occurs at Level 10.
At Evolution I it occurs at Level 5.
Evolution II or III makes an existing cookie mature even below those levels.
The window warns when an already pending evolution would close the early-removal route.

A mature cookie cannot die through ordinary neglect.
Losing levels through save editing, a broken streak, a different government or a later fall in global Chaos must not clear maturity.
Normal play does not reduce Cookie Level.

## The three endings of the relationship

A weak cookie can dry out and die, permanently ending its normal instance.
A living cookie can remain a long-term source of rewards while the player continues to manage it.
A developed, starving cookie can revolt, permanently replacing feeding with a country-level military crisis.

The host is not automatically switched to the Cookie Empire.
The revolt presentation offers a clear one-time choice to remain with the host or take control of the new country when the game and multiplayer permissions permit that transfer.
The default preserves the player's country.
Choosing a side changes player control, not the army, territory or rewards used in the uprising.

## Numeric rounding

`round_to_5` and equivalent wording mean nearest multiple of five, with an exact halfway value rounded upward.
`ceil25` rounds upward to the next multiple of 25.
Item packets round down when necessary to avoid spending or awarding more than the validated available quantity.
Exact click counts and percentage thresholds do not have to be multiples of five.
