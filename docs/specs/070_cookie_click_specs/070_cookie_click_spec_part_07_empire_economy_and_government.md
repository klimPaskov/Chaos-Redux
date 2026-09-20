# 070 Cookie Click: the Empire's economy and government

## Feeding a country

The Cookie Empire keeps Cookie Fullness and Cookie Level as its two public custom values.
Fullness now represents food held for the state and its forces.
It no longer represents mouse clicks.
The former pet rewards cannot be collected by the Empire.

The internal reserve is measured in registered food value.
The visible bar shows the fraction of the current storage capacity that is filled.
It is a different operating phase of the same mechanic, with a clear transition explanation.

Use this starting daily appetite.

```text
A = round_to_5(
    50
    + 5 × Cookie_Level
    + 5 × active_land_divisions
    + 10 × directly_controlled_states
    + 5 × operating_military_factories
)

storage_capacity = 5 × A
Fullness = min(100, 100 × stored_food / storage_capacity)
```

Five days of reserves fill the bar.
Changing army size or territory changes capacity and demand at the next daily review.
It does not create food to preserve the old percentage.
If capacity falls, retain existing absolute food up to ten days of the new appetite, with a visible temporary surplus state.
Further excess cannot be converted into a second reward.

Divisions in training do not count until deployed.
Empty deployment spam therefore increases appetite without creating an advantage.
After the relevant branches unlock, add 5 appetite per five active operational air wings, 5 per five active light naval task forces, and 10 per active capital-ship task force, with a combined ordinary air-and-navy addition cap of 100.
Use actual supported active-force grouping and a documented substitute based on active aircraft or ships when wing or task-force enumeration is unavailable.
A substitute must preserve the same measured operating burden and pass the naval and air scenarios.
Stored aircraft, unused ships and empty formations do not create additional food demand.
These are authored initial operating coefficients, not native engine supply values.

## Startup reserves

Initial setup fills at most the normal five-day food capacity.
Its input value is allocated from the saved country-creation or world-end reserve package.
The remainder of a promised 30-day operating package arrives as actual compatible Cookie equipment in the normal stockpile, available for later conversion.
It is not stored as an unlimited invisible food balance.
The package explicitly divides frontline equipment, reinforcement reserves and material intended for later feeding.
Using that last material to reinforce an army leaves less to eat.
No component is credited twice.

## Supply and appetite

Ordinary military supply, fuel and equipment remain relevant.
Fullness does not replace supply hubs, railways, ports or logistics.
A full Empire can still lose a badly supplied battle.
A hungry Empire suffers additional cookie-specific problems.

| Fullness | Country effect direction |
| --- | --- |
| 75 to 100 percent | Stable reinforcement and up to 15 percent organization recovery from the appetite spirit |
| 50 to below 75 percent | Normal operation, with no extra penalty |
| 25 to below 50 percent | 10 percent lower organization recovery and 10 percent higher attrition |
| Above zero to below 25 percent | 25 percent lower recovery and 25 percent higher attrition, with emergency feeding actions emphasized |
| Empty | No new scripted reinforcement packages, 50 percent lower recovery and 25 percent lower attack until fed |

Do not remove deployed divisions simply because Fullness reaches zero.
Losses arise through combat, attrition and defined breakdown events.
The country can recover by obtaining and consuming real assets.
A weak enemy should be able to exploit a hungry Empire without needing a special anti-cookie damage type.

## Where food comes from

The Empire has four food sources: captured assets, regular Cookie equipment production, managed feeding territories, and actual consumption of population or buildings.
Their availability changes through the focus tree.

Regular industry produces Cookie body equipment.
Some of that stock can be used to replenish formations and some can be consumed as food.
This creates a real choice between reserve strength and appetite.
There is no separate mandatory ration equipment meter.

The player sets a national feeding policy: preserve military reserves, balanced use, or emergency consumption.
The default is balanced.
The policy determines which registered stockpiles may be automatically consumed at the daily review.
It never consumes another player's assets without the appropriate subject agreement or occupation contract.

Food conversion pays only the amount that can enter storage.
The preview shows any unconverted stock.
Do not debit 1,000 equipment when only 100 could be usefully converted.
Actual depletion is recorded before food is credited.

## Conversion efficiency

Captured foreign equipment converts at a base 50 percent of its registered food value.
Compatible Cookie body equipment converts at 75 percent.
Specialized bakery programs can raise either figure by 25 percentage points, up to 100 percent.
There is no recipe that creates more registered input value than it consumes.

Conversion to replacement equipment is a separate recipe.
It cannot also fill the food reserve with the same input.
When a process produces multiple outputs, its manifest divides one input budget between those outputs.
A factory level cannot be eaten for food and simultaneously counted as intact industrial production.

Converting obsolete captured weapons is useful.
Destroying a new high-quality army solely to feed the Empire is expensive.
The AI should prefer unusable surplus before useful equipment needed by an active front.


## Level after the uprising

Save the Level at formation as `birth_level`.
The Empire no longer gains Level through mouse clicks.
It gains a hidden growth score G from actual food used to meet daily appetite and from the first successful settlement of a real state.

Add one G per food unit actually consumed for current daily appetite.
Food merely transferred into storage or wasted at capacity gives no G.
Add 1,000 G the first time each state completes its valid method-specific settlement under this instance.
Reconquest, release, re-annexation and repeated settlement of that state cannot pay this addition again.

```text
Empire_Level = birth_level + floor(sqrt(G / 1000))
```

This preserves the strength inherited from the pet and permits a lower-Level uprising to develop toward the final branch.
The next daily demand calculation uses the new Level.
There are no pet milestone payouts or fresh clicking targets after formation.
Manual presets initialize birth Level explicitly and start G at zero without inventing past settlement.

## Registered food inputs

Food value is a separate operating conversion unit.
It is not the pet reward-budget value or the uprising's historical reward-value ledger.
Keep those namespaces distinct.

| Actual stored input | Raw food value per item before conversion efficiency |
| --- | ---: |
| Basic Cookie body equipment | 2 |
| Durable Cookie body equipment | 4 |
| Heavy Cookie body equipment | 10 |
| Mobile Cookie body equipment | 4 |
| Cookie oven equipment | 20 |
| Conventional infantry equipment | 0.5 |
| Conventional support equipment | 2 |
| Conventional artillery equipment | 5 |
| Train | 25 |
| Convoy | 20 |
| Fuel | 0.02 per fuel unit |
| A compatible stockpiled aircraft | 20 |

Apply the captured-material 50 percent or Cookie-equipment 75 percent conversion once, then its permitted improvement.
The table contains authored starting exchange rates.
Additional equipment types need explicit safe adapter and value registration.
Aircraft already assigned to wings are not stockpiled aircraft and cannot be consumed through the stockpile entry.

Foreign equipment values do not change because the player temporarily changes its equipment name.
Quality-specific variants can have bounded registered values after actual equipment inspection.
Do not apply a higher value merely from a display string.
Use complete input packets and fixed-point arithmetic supported by the engine.

## Four governing methods

The state makes one major commitment between the following methods after its survival branch.
That commitment changes the second half of the government and economy routes.
Basic logistics and military branches remain available under every method.

| Method | Main benefit | Main cost | Late result |
| --- | --- | --- | --- |
| Rapid consumption | Immediate reserves and reinforcement from conquest | Quickly exhausts useful territory and raises appetite | A fast offensive state that must keep advancing |
| Long-term farming | Renewable food from productive feeding territories | Slower opening and the need to protect infrastructure and civilians | A stable empire with supply corridors and managed subjects |
| Population conversion | New Cookie manpower and specialist formations | Permanent demographic change, resistance and conversion capacity limits | A growing nonhuman state with an expensive occupation burden |
| Direct destruction | The strongest immediate food and siege returns | Removes the industry and population needed for long campaigns | A destructive army with little sustainable rear area |

The Monster remains ruler in every method.
The choice changes how it governs, recruits and uses territory.
It is not a set of cosmetic ideology labels with identical bonuses.

Methods are mutually exclusive once their central commitment is completed.
Changing an ordinary emergency feeding policy does not change the governing method.
The final world-end branch can intensify any method without refunding its earlier sacrifices.

## Managed feeding territories

Long-term farming designates real controlled states as feeding territories.
A state needs surviving population, usable infrastructure, supply access and no active severe famine.
Its first preparation takes 90 days.
The state remains a place with civilians and industry, not a free off-map food generator.

After preparation, a 30-day production cycle yields food according to population, infrastructure and current control.
Use a conservative initial value of `10 + 5 × infrastructure_level + 5 × complete_millions_of_population`, capped at 100 food per day equivalent for a fully operating state.
Occupation, damage and famine reduce the yield in 25 percent steps.
These are authored yields of this new mechanic, not claims about native agricultural output.

Each cycle requires an actual equipment and manpower commitment through its governing program.
The recurring commitment is published in the action preview.
Missing inputs pause production and do not become negative stockpiles.
Prepared state status can be productive, disrupted, resting or depleted.
Use those qualitative states instead of a third public soil-health meter.

Destructive harvesting of the same territory ends its current farm cycle and removes the prepared status until it is rebuilt.
Its former yield cannot continue after the population or infrastructure has been consumed.
The regime must choose between today's army and tomorrow's food.

## Population conversion

Conversion is a distinct recipe from eating people.
A conversion operation removes a clamped actual civilian population amount and produces a bounded quantity of Cookie manpower or body equipment.
Its required inputs include actual Cookie equipment, time and control of the state.

The initial recipe converts 5,000 civilians over 90 days into 2,500 Cookie manpower and 150 body equipment, after spending the 100 body equipment and other inputs specified in E-04.
This represents one transformation process with defined outputs, not two removals of the same people.
The mechanical population debit must suppress any unrelated native recruitable-manpower credit before awarding the explicit Cookie result.

Report this demographic change separately from confirmed deaths.
The shared helper path must support that distinction.
If it cannot, conversion requires a new narrowly reviewed helper before the route can be implemented.
Do not falsely record all converted people as killed simply because the existing convenient effect also logs deaths.

Conversion leaves a persistent state history.
The state cannot repeat its first-conversion reward after changing owner and being reconquered.
Repeated programs use only the current remaining population above the protected floor.
They raise resistance and can disrupt output through actual occupation conditions.

## Destructive harvesting

Destructive harvesting has separate entries for equipment, building levels and people.
The exact target and amount are visible before payment.
A population-eating operation records deaths through the shared system once.
A factory-eating operation removes actual levels.
A damaged-building operation uses the lower yield and preserves its damage history.

Ordinary pre-world-end harvesting keeps a minimum civilian population floor of 10 percent of the state's population at the start of this instance.
The Final Bite can reduce that floor under its explicit world-end rules.
The floor is not replenished by changing owner, changing method or reloading.

One state can have only one active major Cookie operation.
A farm, conversion program and destructive harvest cannot run on the same people and buildings in parallel.
Losing control cancels remaining work and preserves already completed real losses.

## Institutions and the three spirits

The appetite spirit represents current hunger and the governing method.
The bakery-network spirit represents economy and conversion efficiency.
The military-shaping spirit represents the chosen specialist doctrine.

An unlock changes or replaces a stage inside those lifecycles.
It does not append a new permanent spirit.
Use ordinary advisors, state modifiers, technologies and decisions only when they communicate a genuinely different part of the system.

The bakery institution opens safe equipment processing and sustainable production.
The logistics institution opens reserve policies and supply-corridor missions.
The shaping institution opens specialist bodies and reinforcement recipes.
None of these institutions gives unconditional infinite manpower.

## Subjects and food obligations

A Cookie subject can be a converted administration or a human-managed feeding territory.
It remains a real country with a defined capital, government, army and resource obligations.
The parent Empire can demand only registered available assets under the relationship's rules.

A normal tribute cycle lasts 30 days.
Its demand scales from the subject's actual economy and retains a minimum domestic reserve.
A subject that cannot pay receives a warning and a finite corrective objective.
Failure can trigger direct occupation, loss of subject privileges or a revolt.
It does not conjure the missing tribute from nowhere.

Human-managed subjects use their ordinary civilian systems.
Converted administrations use the appropriate special-country classification but still account for any remaining human population.
Do not let the classification exemption erase famine or death tracking.

Creating subjects is a long-term alternative to direct extraction.
The Empire gives up direct factory control and must defend their borders.
In return it receives sustainable tribute and fewer directly administered states in its appetite formula.
Diplomatic freedom remains limited by the Monster's war policy.

## Defeat and recovery

Losing a key bakery reduces production, not Cookie Level.
Losing territory reduces future food sources and may lower appetite, but it does not refill the reserve.
A threatened Empire may consume its own equipment to remain active, weakening its next offensive.

Retaking a lost state restores only the assets that still exist.
Its harvest and conversion history remains.
A player who repeatedly trades a state across a front cannot farm first-capture grants, population conversions or factory-eating rewards.
