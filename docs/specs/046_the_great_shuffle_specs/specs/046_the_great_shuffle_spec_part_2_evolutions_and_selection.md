# Event 046: Evolutions and family selection

## Evolution model

The Great Shuffle's evolutions are capability unlocks.

They are not ordinary escalation stages and they do not create an active incident between firings.

Each evolution enlarges the allowlist, increases selected-family coverage, opens stronger range profiles, and adds new compatibility contracts.

Evolution activation itself changes no gameplay value and adds no Chaos.

The next firing uses every evolution that has already activated and remains enabled.

## Evolution activation paths

Evolutions I through IV can activate through the normal evolution pacing system after their Chaos threshold is met.

Their target pacing is centered near ninety days, with dynamic adjustment for distance above the threshold and the ordinary evolution framework.

They can activate before Event 46 has ever fired.

A pre-fire activation means the first Great Shuffle can open with more than the baseline family pool.

An activation after one or more firings affects only future firings.

There is no active Event 46 world state to retrofit.

Evolution V activates immediately at the first valid `1000+` threshold window because a normal MTTH delay could make it unreachable under the World Collapse freeze.

Its firing access follows the reachability contract in Part 1.

## Capability table

| Capability | Chaos requirement | New family domain | Selection effect | Range effect |
| --- | ---: | --- | --- | --- |
| Baseline, working label only | `0+` | Basic country values | A compact subset of baseline families | Broad legal ranges with a stronger middle than tail |
| Evolution I, working label only | `200+` | National stores | Adds inventory families and increases total coverage | Greater low and high tails for reserves and stockpiles |
| Evolution II, working label only | `400+` | Population, industry, buildings, resources | Adds state-family quotas and dependency bundles | Absolute map values can reach severe low and high outcomes |
| Evolution III, working label only | `600+` | Politics, research, production, units, commanders | Adds compatibility-sensitive country and military families | Legal edges become common and categorical outcomes widen |
| Evolution IV, working label only | `800+` | Owner-registered mechanic values | Adds adapter quotas and owner-declared ranges | Each owner selects its approved high-chaos profile |
| Evolution V, working label only | `1000+` | Every proven safe family and proven structural adapters | Core safe families become near-universal in one firing | Full legal tails and World Collapse structural profiles |

## Family coverage model

The number of selected families scales from the size of the currently eligible pool.

This avoids a fixed count becoming too small as new adapters are registered or too large when few families are valid.

The implementation centralizes the exact ratios and floors in Event 46 tuning.

The design targets are:

| Active capability | Target eligible-pool coverage | Minimum selected families when available | Identity quota |
| --- | ---: | ---: | --- |
| Baseline | `35%` to `50%` | `4` | At least two core national values |
| Evolution I | `45%` to `60%` | `6` | At least two baseline values and two national-store families |
| Evolution II | `55%` to `70%` | `8` | At least two state families, with population and industry rolled independently |
| Evolution III | `65%` to `80%` | `10` | At least two politics, production, research, unit, or commander families |
| Evolution IV | `75%` to `90%` | `12` | At least two valid owner adapters when two exist |
| Evolution V | `90%` to `100%` | All core safe families | Every non-conflicting core family and every valid mandatory adapter |

The implementation can tune these bands after probability evidence.

It must preserve the ordering that later capabilities select a larger share of the eligible pool.

## Baseline representation

Baseline families remain strongly represented at every evolution.

They define the event's identity and ensure that a high-tier firing still changes basic national conditions.

Later families do not replace them.

Selection uses a baseline quota before the remaining slots are filled from the full eligible pool.

The quota never creates memory from previous firings.

## Independent family rolls

Each family has an independent selection weight inside its eligible group.

A family's previous selection, previous result, previous severity, or previous effect on one country does not modify its next roll.

Only current capability, current legality, current owner registration, compatibility, and declared family weighting matter.

Families with narrow legal scope can have enough base weight to avoid starvation.

Families that are broad or highly disruptive can have lower weight below Evolution V without becoming impossible.

## Compatibility and dependency groups

Two selected families can conflict even when both are individually safe.

The registry handles this through explicit groups.

A compatibility group prevents two mutually exclusive alternatives from entering the same firing.

A dependency group allows related families to plan together and commit in a declared order.

Examples include shared factory capacity with factory counts, ruling ideology with party popularity, research graph changes with doctrine progress, and ownership changes with capital relocation.

A conflict is resolved during selection or planning.

The event does not discover the conflict after one family has already changed the world.

## Dynamic range principles

### Previous values are excluded

A new result does not use the scope's old value as its center, multiplier, floor, ceiling, compensation input, or direction.

The old value is read only for reporting, legal delta application, and reconciliation proof.

### Legal capacity can matter

A range can use current legal capacity when the value cannot exceed that capacity.

Fuel can use the country's pre-transaction fuel capacity.

Factory counts can use a preplanned legal shared-building capacity.

Airbase levels can use the building's legal maximum.

These capacity inputs determine legality, not entitlement.

### Stable scope facts can matter

A family can use immutable current facts such as coastal status, state category, owned core population, date, technology era, valid equipment token set, DLC state, unit domain, or registered owner profile.

The family cannot use the old amount to preserve rank or continuity.

### World anchors can matter

Large absolute families can derive tuning anchors from a frozen world snapshot.

Population can use world state-count and era bands.

Equipment can use era and global production-scale bands.

Resources can use registered resource-specific world ranges.

Every scope still draws independently.

### Tails grow with evolution

Every family declares one or more distribution profiles.

The baseline profile favors a broad middle while retaining meaningful low and high outcomes.

Later profiles increase the chance of legal extremes.

Evolution V can use the full legal tail whenever the family contract proves that an edge value remains playable.

## Distribution profiles

The registry supports a small named set of reusable distribution shapes.

- `broad_center` gives most results across the middle with lower but real edge chances.
- `two_tail` favors very low and very high outcomes and makes average results less common.
- `low_skew` creates scarcity-heavy worlds.
- `high_skew` creates abundance-heavy worlds.
- `flat_legal` gives every declared result band similar weight.
- `categorical_compatible` chooses one token from a legal compatibility group.
- `normalized_share` creates several shares that reconcile to one complete total.
- `owner_profile` delegates the shape to a registered mechanic owner.

A selected family can first roll a world mood for that firing, such as scarcity-heavy, abundance-heavy, or split-tail.

That mood applies consistently to the family without linking it to the recipient's old value.

Different families roll their moods independently.

The event never creates a hidden global compensation rule across families.

## Baseline: basic national values

The first capability allows direct rewrite of safe core country values.

The starting pool includes Stability, War Support, Political Power, Command Power, Army Experience, Navy Experience, Air Experience, reserve manpower, and fuel reserves.

Each country receives an independent result in every selected family.

Stability and War Support remain inside their legal percentage bounds.

Command Power and military experience use the current legal cap recorded in the transaction snapshot.

Fuel uses the country's frozen legal capacity.

Reserve manpower uses a safe absolute range derived from registered population and era anchors, without centering on the country's old reserve.

Baseline results can be severe.

The profile avoids making legal zero and full-cap outcomes routine before later evolutions.

## Evolution I: national stores

Evolution I opens equipment stockpiles, convoys, trains, stronger reserve profiles, and other owner-approved national inventories.

Equipment is organized by compatible equipment family.

A country receives quantities only for tokens that can legally exist in its stockpile.

The event does not create malformed equipment names, inaccessible special objects, invalid variants, or a token whose owner forbids transfer.

The country does not need to keep the same global stockpile value or the same balance among families.

One firing can create a world full of equipment.

Another can erase most national reserves.

Tiny countries are allowed to receive absurd arsenals because quantity bands are based primarily on era and registered family scale, not the recipient's old amount or industrial rank.

## Evolution II: the map is rewritten

Evolution II opens absolute state population, shared industry, eligible buildings, and registered resources.

Population and industry are independent families with independent seeds.

A highly populated state can receive little industry.

A nearly empty state can become an industrial center.

The event does not force a population-to-factory ratio.

Population uses a newly generated absolute amount inside a state-valid range.

It is an ontological rewrite and is not registered as deaths, births, famine mortality, or migration.

Factories respect a planned capacity bundle.

Dockyards, coastal forts, and naval bases require a coastal and province-valid contract.

Resources use registered legal resource types and resource-specific ranges.

Supply hubs and railway graphs remain conditional until the map contract proves safe graph reconciliation.

## Evolution III: governments and armies forget themselves

Evolution III opens compatible laws, party popularity, ruling ideology when separately proven, active research progress, doctrine progress, production-line numeric state, unit experience, planning, readiness, and commander experience.

Categorical systems use compatibility groups.

Share systems normalize correctly.

Stable object identity remains protected.

The event can create strange combinations.

It cannot create an invalid law token, impossible ideology total, broken technology graph, missing production object, invalid unit definition, or duplicate commander.

Completed technologies, national spirits, characters, traits, templates, and production identities remain protected unless a later explicit owner adapter proves a narrow safe contract.

## Evolution IV: mechanics lose their numbers

Evolution IV opens the Event 46 owner-adapter registry.

An owning system can expose current legitimacy, pressure, influence, cohesion, severity, reserves, preparedness, local crisis progress, or another mutable gameplay value.

The owner declares scope, range, profile, exclusions, compatibility, setter, reconciliation, report rules, and protected ledgers.

Event 46 does not need to understand what the value means.

It must understand how to treat it safely.

The owner can veto a firing when its lifecycle proof is incomplete.

One-way history and authoritative shared framework values cannot be exposed through this registry.

## Evolution V: everything proven safe

Evolution V selects every non-conflicting core safe family and every valid mandatory owner adapter.

Conditional families enter when their proof passes for the current world.

The range profiles use full World Collapse tails.

The capability can include proven structural adapters for territorial claims, selected ownership relationships, selected diplomatic relationships, capital relocation, and unit locations.

These structural families are not assumed safe merely because the Chaos threshold is high.

Each needs a full contract for identity, pair symmetry, map validity, country survival, supply, capital, war, faction, subject, and cleanup behavior as applicable.

The phrase **everything that can be randomized** means every surface that has passed the allowlist contract.

It never means every number found in memory.
