# 070 Cookie Click: rewards and edible values

## Reward quality

Rewards should vary in practical use as well as size.
One day may help an army recover, another may strengthen the government, and another may supply the railways.
The cookie should occasionally provide something the country could not quickly obtain through ordinary production.
It should never award a nonexistent resource, unusable DLC currency, incompatible doctrine or empty equipment token.

The reward track is generated once at cycle opening and saved.
The window reveals the next milestone's family and quantity.
Later milestone families appear as identifiable silhouettes until earned.
Opening the window, saving, loading, changing a selected state or inspecting a tooltip does not reroll anything.

## Daily budget

Use this authored starting formula.

```text
B = round_to_5(
    (100 + 10 × (L - 1) + 5 × floor(C / 10000))
    × evolution_reward_factor
)

evolution_reward_factor = 1.0, 1.5, 2.0, 3.0
```

`B` is an internal balancing value.
The player sees actual reward quantities.
The reward value ledger `V` increases only by the registered value of what was actually delivered.
Queued rewards, rejected outcomes, overflow and promised assets do not count.

Treat this budget as a common comparison unit for Event 070.
It is not a claim that 5 Stability has the same economic value in every country.
Scenario testing must compare small countries, majors, wartime shortages and saturated economies before locking release balance.

## Baseline packets

The following are the first implementation targets.
They are minimum indivisible packets.
Larger packets should remain clean multiples of 5 where the underlying value permits it.
Buildings, technologies, integer unlocks and naturally discrete counts are exceptions.

| Packet | Minimum delivered quantity | Internal value | Validity and targeting |
| --- | --- | ---: | --- |
| Political support | 5 Political Power | 5 | Country has room below its effective cap |
| Command support | 5 Command Power | 10 | Actual capacity exists |
| Army training | 5 Army Experience | 10 | Army experience exists and can increase |
| Naval training | 5 Navy Experience | 10 | A navy or an available naval development route makes it useful |
| Air training | 5 Air Experience | 10 | An air force or an available air development route makes it useful |
| Public confidence | 5 percentage points of Stability | 25 | Do not exceed the effective cap |
| Mobilization support | 5 percentage points of War Support | 25 | Do not exceed the effective cap |
| Volunteers | 1,000 manpower | 20 | A valid national manpower pool exists |
| Fuel deliveries | 1,000 fuel | 10 | Fuel capacity and a valid consumer exist |
| Small arms | 50 items of a valid infantry equipment family | 15 | Prefer currently deployed or produced compatible equipment |
| Support supplies | 25 support equipment | 15 | Valid researched equipment and a useful target |
| Field artillery | 25 artillery | 20 | Valid deployed or researched artillery family |
| Railway stock | 5 trains | 25 | The equipment and railway consumer exist |
| Shipping | 5 convoys | 20 | Owner can use convoys or has a concrete coastal route |
| Construction assistance | A 5-day, 10 percent construction modifier | 40 | Attach to the single Cookie reward modifier, not a new spirit per payout |
| Production assistance | A 5-day, 10 percent factory-output modifier | 40 | A usable production base exists |

Small early milestones will usually draw cheaper packets.
Larger milestones may combine several packets from one family.
A high-value packet cannot be granted for an insufficient budget merely to force variety.

Temporary bonuses merge into one reward contract.
Repeated grants extend its remaining duration up to 30 days at that tier.
They do not stack dozens of independent output multipliers.
A higher unlocked tier replaces the weaker tier and preserves only the permitted remaining duration.

## Evolved packets

Evolution I adds stronger equipment packages, larger logistics grants, longer production assistance and targeted construction.
Evolution II adds factories, state infrastructure programs, military research bonuses and supported country-mechanic rewards.
Evolution III permits advanced equipment, major industry programs, compatible technology grants and unusual registered Chaos Redux rewards.

A technology reward has an explicit acquisition contract.
It must check the technology's existence, DLC requirements, exclusivity, prerequisites, ownership and grant side effects.
Use a compatible research bonus when an exact grant is invalid only if that alternative was part of the saved track.
Do not use a blind donor-tech union as a generic random-tech prize.

Building rewards select and save a real eligible state.
Show the state before the reward becomes claimable.
A reward cannot exceed the state's valid building level or slot limits.
Target loss causes one documented revalidation into the saved ranked alternate list.
It does not let the player repeatedly move the reward to a preferred state.

Research-slot rewards are not part of ordinary daily tracks.
One permanent additional slot may be a late Level 50 development reward if the owner remains below the project-approved limit.
Otherwise its saved alternative is a substantial compatible research bonus.
This prevents a long campaign from producing unlimited research slots.

Nuclear weapons, special projects, strategic resources and other unusual rewards require a separate audited adapter.
No category name alone grants permission to manufacture unsupported effects.

## Family selection

Draw families before drawing exact tokens within those families.
An equipment family with hundreds of variants must not become hundreds of times more likely than Political Power.

Starting family weights are government 25, military knowledge 20, manpower and logistics 25, equipment 25, and industry or research 5.
These are relative design weights for a complete declared pool.
They are not presented as measured in-game probabilities.
Evolution I changes the last family to 15 and reduces government to 15.
Evolution II gives industry or research 25, government 10, military knowledge 15, manpower and logistics 25, and equipment 25.
Evolution III uses government 5, military knowledge 10, manpower and logistics 20, equipment 30, and industry or research 35.

Remove invalid families before selection.
Limit a family to two appearances within the four-milestone day unless fewer than three families remain valid.
A family used in three consecutive full days receives half its normal selection weight for the next day.
The minimum positive family weight remains 5.
The exact candidate pool and all these modifiers belong in the probability audit.

A bonus outcome has a 10 percent design weight at the final milestone.
It upgrades a packet or adds up to 25 percent of the current budget.
It never rerolls the entire day or pays an already completed threshold again.

## Development rewards

A milestone Level reward has an internal budget of five ordinary daily budgets at the newly reached level.
Its ceiling rises through evolution, but its effect remains a clear package.
At least one meaningful special reward accompanies Levels 10, 20, 30 and 50.

| Threshold | Mechanical direction |
| --- | --- |
| 5 | A complete equipment or logistics package and an appearance change |
| 10 | A selected state construction program or a major temporary production contract |
| 15 | A useful compatible military research package |
| 20 | A substantial industrial expansion tied to one state and its supply needs |
| 30 | A powerful advanced equipment package or a supported event-mechanic reward |
| 40 | A multi-state construction program with actual slot and control checks |
| 50 | A rare technology-related payoff, with a research-slot alternative only under the explicit cap contract |

The owner chooses between two valid reward directions for major thresholds.
A default choice resolves after 5 simulation days so the system cannot accumulate an unlimited queue of modal rewards.
Default selection uses the country's concrete shortage.
No unopened choice prevents hunger or pauses the feeding clock.

## A common value description

Event 070 needs a broad inventory of values that can be increased or consumed.
Each value is explicitly registered.
“Dynamic” means its availability, amount, target and family respond to the country and game state.
It does not mean the script can discover every arbitrary variable in every installed mod without a definition.

Each registration needs an owner namespace, family, validity test, scope, current amount reader, safe lower and upper bounds, preferred increment, positive grant contract, negative consumption contract, actual-change result, value conversion, flavour identity, UI icon, DLC or feature requirements, and test cases.
Unsupported values remain absent from live pools with a named reason.

Event 066 Abundance may use the same neutral description format.
No Abundance implementation or shared registry is assumed to exist.
Event 070 must work with its own registrations until a verified common owner is available.
Cookie appetite, hunger, reward history, maturity and revolt scaling remain Event 070 data.

## Consumption families

| Family | Earliest evolution | Permitted operation |
| --- | --- | --- |
| Political and command values | 0 | Remove a clamped actual amount |
| Army, navy and air experience | 0 | Remove from the valid current pool |
| Stability and War Support | 0 | Reduce by a bounded amount above the chosen safety floor |
| Manpower and fuel | I | Remove actual reserves, with separate population handling |
| Equipment, trains and convoys | I | Remove actual available stockpile items |
| Construction and production capacity | II | Apply a finite impairment or a verified progress debit |
| Research progress | II | Debit verified progress, never silently replace it with a research-speed penalty |
| Factories and other buildings | II | Damage or remove an actual existing level with exact accounting |
| Supported national mechanic values | II | Use that system owner's explicit safe debit contract |
| Civilian population | III | Remove an actual number through the shared population-loss helper |
| Infrastructure and major national assets | III | Consume actual valid levels or registered assets |

The table is an initial family map, not a closed whitelist.
The implementation must inventory additional safe values from the installed base game, enabled DLC and Chaos Redux systems.
Every accepted addition receives a test and an owner-approved interpretation.

Do not consume country identity, player-control settings, event-enable toggles, achievement flags, country tags, state IDs, event history, registry entries, global Chaos, death totals, migration bookkeeping, or another system's private variables.
A number existing in a save does not make it edible.
Research slots, diplomatic relationships, leaders, deployed divisions and nuclear devices are excluded unless a separate concrete gameplay contract authorizes them.

## Exact losses and caps

A bite records the amount actually removed.
A capped resource cannot fall below its registered floor.
An invalid or empty resource contributes zero and is removed from that bite's candidate set.
At most three candidate attempts occur within one bite.
If none are valid, the cookie remains hungry without inventing a loss.

Equipment helpers that mutate a temporary amount require a fresh input before every call.
Country stockpiles are country assets.
Do not describe them as stockpiles attached to a captured state.

Damage and destruction are different entries.
A damaged factory can be repaired through ordinary play and earns only the lower damage value.
A consumed building level is actually removed and earns the destruction value.
Repairing damage and damaging it again cannot repeatedly fund a large army because the repeat conversion value is reduced and the cooldown is retained.

Civilian population loss, reserve manpower loss and migration are separate.
Removing reserve manpower must not also be reported as civilian deaths.
If civilian consumption would otherwise add recruitable manpower through a native side effect, use the supplied neutralizing helper.
Report deaths once through the shared death system.
Never restore consumed people when the crisis ends.

## Stable reward payment

Every saved reward has an entitlement ID containing the instance, cycle or level threshold, and slot.
Payment validates that entitlement, revalidates the actual recipient, performs one grant, records its actual result and marks it resolved.
A dead recipient resolves to no payment.
A capped resource uses its preselected alternate once.
No valid alternate means a clearly recorded lost or reduced reward, with no fabricated ledger value.

This is a transaction contract for implementation.
It is not a claim that HOI4 exposes database transactions.
The coder must prove the corresponding one-shot behavior across repeated callbacks and save/load.
