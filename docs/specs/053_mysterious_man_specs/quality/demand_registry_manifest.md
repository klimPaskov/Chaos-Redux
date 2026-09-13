# Event 53 Demand Registry Manifest

A demand type enters the active demand pool once when its applicability trigger passes. Affordability is checked after the type and amount are locked.

Baseline behavior uses Political Power only. Evolution I, II, and III can use the full valid demand registry. Every valid type has equal selection probability.

## Registry

| ID | Demand type | Applicability | Amount anchors | Payment transaction | Important bound | Readiness |
| --- | --- | --- | --- | --- | --- | --- |
| `mm_d01` | Political Power | Every normal target | Government scale, current Political Power, visit, payment, refusal, tier | Exact Political Power debit | Meaningful minimum and bounded cap | Event 53 implementation required |
| `mm_d02` | Command Power | Target uses ordinary command system | Army size, command capacity, current reserve, progression | Exact Command Power debit | Maximum 60 | Event 53 implementation required |
| `mm_d03` | Army Experience | Meaningful land military system | Army size, doctrine use, current reserve, progression | Exact Army Experience debit | Whole-value rounding | Event 53 implementation required |
| `mm_d04` | Navy Experience | Navy, dockyards, naval production, or established naval institution | Naval scale, current reserve, progression | Exact Navy Experience debit | Invalid for a country with no meaningful naval system | Event 53 implementation required |
| `mm_d05` | Air Experience | Air force, aircraft production, airbase network, or established air institution | Air scale, current reserve, progression | Exact Air Experience debit | Invalid when no meaningful air system exists | Event 53 implementation required |
| `mm_d06` | Infantry equipment | Military uses supported infantry equipment | Fielded force, production capacity, current stockpile, progression | Supported stockpile debit | Structural floor prevents dumping exploit | Gateway available through infantry helper |
| `mm_d07` | Support equipment | Military uses support equipment | Support-company use, production, current stockpile, progression | Supported stockpile debit | Structural floor and whole units | Gateway available through support helper |
| `mm_d08` | Artillery | Military uses a safely resolved artillery equipment token | Artillery battalions, production, current stockpile, progression | Exact supported artillery stockpile debit | Requires a verified dynamic token or adapter | Owner adapter required |
| `mm_d09` | Trucks | Military or logistics system uses motorized equipment | Motorized formations, logistics, production, current stockpile | Supported motorized stockpile debit | Structural floor and whole units | Gateway available through motorized helper |
| `mm_d10` | Trains | Meaningful rail network or train stockpile | Rail network, supply use, current stockpile, progression | Supported train stockpile debit | Whole trains, network-aware cap | Gateway available through train helper |
| `mm_d11` | Convoys | Port, overseas territory, maritime supply, trade, or convoy stockpile | Maritime dependence, current stockpile, progression | Supported convoy stockpile debit | Invalid for no meaningful convoy system | Gateway available through convoy helper |
| `mm_d12` | Fuel | Meaningful fuel use or reserve | Consumption, army, navy, air use, current reserve, progression | Supported fuel debit | Several-week or reserve-share anchor | Gateway available through fuel helper |
| `mm_d13` | Manpower | Ordinary manpower system | Free manpower, eligible population, mobilisation scale, progression | Free manpower debit | Never remove state population | Event 53 implementation required |
| `mm_d14` | Temporary civilian capacity | Enough civilian factories for a meaningful burden | Civilian factory count, economy scale, progression | Timed civilian-capacity burden | No permanent factory deletion | Event 53 implementation required |
| `mm_d15` | Temporary military capacity | Enough military factories for a meaningful burden | Military factory count, war state, progression | Timed military-capacity burden | No permanent factory deletion | Event 53 implementation required |
| `mm_d16` | Stability | Every normal political target | Current Stability, country scale, progression | Exact Stability deduction | Protected payment floor | Event 53 implementation required |
| `mm_d17` | War Support | Every normal political target | Current War Support, war state, progression | Exact War Support deduction | Protected payment floor | Event 53 implementation required |

## Uniform selection

At Evolution I and higher, the demand selector:

1. evaluates applicability only
2. adds each valid demand ID once
3. selects one uniform random ID
4. calculates the amount for that family
5. locks type and amount
6. evaluates affordability for the pay option

A valid demand with insufficient current holdings remains selected and forces refusal unless the country gains enough resource before the outcome is applied through an engine-safe refresh path.

## Amount components

Every family calculator should expose these debug components:

- minimum
- structural anchor
- current reserve anchor
- visit multiplier
- payment multiplier
- refusal multiplier
- tier multiplier
- pre-cap amount
- cap
- final rounded amount

The player sees only the final amount and blocked reason. Debug components remain outside player-facing localisation.

## Structural anchors

Use stable capacity measures that fit the demand:

- government and industrial scale for Political Power
- armed-force and command capacity for Command Power
- branch scale for experience
- fielded force and production for equipment
- network and supply dependence for trains
- maritime dependence for convoys
- consumption and reserve structure for fuel
- free manpower and mobilisation base for manpower
- relevant factory count for temporary capacity

A structural anchor prevents deliberate reserve dumping from producing a token demand.

## Progression

Successful payments increase the strongest persistent demand multiplier. Visit count and refusal history can add smaller bounded pressure. Higher active behavior tiers raise minimums and caps.

The final curve should rise clearly across early visits and flatten before overflow or unavoidable permanent refusal.

## Payment receipts

Every demand transaction records:

- visit sequence ID
- demand ID
- displayed amount
- affordability result
- exact debit or timed burden applied
- post-payment value or burden end date
- success or failure

A failed transaction cannot increment payment count.

## Presentation

Every cost uses the correct resource icon or texticon supported by the event popup. The blocked tooltip states the exact shortfall or protected floor. Temporary industrial demands state their duration and practical burden.

No demand description exposes structural anchors, progression multipliers, or caps.
