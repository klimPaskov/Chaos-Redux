# Military Operations Under Extreme Heat

## Military design goal

Heat Wave should change how armies are deployed and supplied. The system should reward preparation, acclimatization, water access, night operations, unit rotation, and cooler defensive positions. It should punish sustained exertion, undersupply, overcrowded fronts, repeated attacks, and large mechanized formations operating through poor infrastructure.

The player should be able to keep fighting in hot states, but doing so should become a conscious strategic choice.

## Two layers of military pressure

Military pressure has a state layer and a division layer.

### State operational heat

This comes from Local Heat Stress, supply, infrastructure, terrain, and regional amplification. It sets the maximum environmental pressure that units in the state can receive.

### Division heat exposure

This tracks how long a division has remained active in severe conditions and how much exertion it has performed. It distinguishes a fresh formation passing through a hot state from an exhausted formation fighting there for months.

Division heat exposure stays hidden. The player sees a compact condition such as Fresh, Strained, Heat-Exhausted, or Critical when selecting an affected unit or viewing a relevant tooltip.

## Exposure gain

A division gains heat exposure when it is in a Dangerous, Extreme, or Scorched state. Gain should increase through:

- active combat
- offensive combat
- strategic redeployment into an affected area
- movement through low-infrastructure terrain
- training or exercising
- low organization
- low supply
- high local military density
- high fuel consumption
- desert, jungle, marsh, or other difficult local conditions
- a recent arrival without acclimatization
- failed army heat protocols

Gain should decrease through:

- remaining in a cooler state
- successful unit rotation
- sustained rest
- high supply and functioning local water logistics
- active army heat protocols
- night-operations policy
- acclimatization over time
- medical and support equipment coverage when the live engine supports a meaningful link

## Acclimatization

A division gradually acclimatizes after sustained presence in hot conditions. Suggested full acclimatization window: 10 to 14 days, modified by organization, supply, training status, and prior heat exposure.

Acclimatization should:

- reduce future exposure gain
- reduce organization-recovery penalties
- reduce heat casualty risk
- improve movement and training performance in hot states
- decay after a long period in cool conditions, but not instantly

A division should not become fully acclimatized while repeatedly strategic redeploying between climates or remaining completely inactive without the required exposure period.

## Unit condition bands

Working division condition bands:

| Condition | Meaning | Typical consequence |
| --- | --- | --- |
| Fresh | Low accumulated exposure | State penalties only |
| Strained | Material heat fatigue | Lower organization recovery and movement efficiency |
| Heat-Exhausted | Prolonged severe exposure | Higher supply use, attrition, reinforcement delay, and weaker combat |
| Critical | Extreme exposure under bad conditions | Evolution I manpower-loss risk and severe operational penalties |

The exact exposure score remains internal.

## State-band military effects

### Manageable

- small training and movement pressure in vulnerable terrain
- flavour reports only unless local supply is already failing

### Strained

- lower organization recovery
- slightly slower movement
- higher supply and water-logistics burden
- reduced training efficiency

### Dangerous

- meaningful organization and reinforcement penalties
- higher attrition
- higher motorized and fuel burden
- slower planning and entrenchment recovery where supported
- stronger penalty for undersupplied divisions

### Extreme

- severe organization recovery loss
- reduced movement and combat performance
- strong attrition and supply consumption
- training becomes inefficient or unsafe
- offensive operations sharply increase exposure
- airbase and logistics support pressure becomes material

### Scorched

- ordinary sustained operations become extremely costly
- non-acclimatized units rapidly reach Critical condition
- supply and fuel burden can make mechanized warfare impractical
- Evolution I can apply recurring military manpower loss
- Evolution III can treat some states as temporarily near-uninhabitable for sustained occupation

## Supply interaction

Heat penalties should scale with the division's actual supply condition.

A well-supplied division in an Extreme state should still suffer. An undersupplied division should suffer much more through multiplicative or staged effects.

Supply-sensitive effects can include:

- additional supply consumption
- slower organization recovery
- reinforcement delay
- equipment attrition
- movement reduction
- fuel inefficiency
- stronger exposure gain
- heat casualty chance at Evolution I

The event should not consume a universal water stockpile. Military water is represented through supply condition, state water pressure, logistics measures, and mission outcomes.

## Unit density

A state with a large concentration of divisions should create higher military water and transport pressure. This prevents the player from parking an unlimited army in one protected city or supply hub.

Density pressure should consider:

- total divisions
- manpower or combat width proxy
- mechanized and armored share
- active combat
- local supply capacity
- local infrastructure
- port or hub dependence

The density contribution should be capped and should not require expensive daily counting across the entire world.

## Offensive operations

Attacking in Extreme or Scorched heat should cause a larger exposure gain than defending. The aim is to create a real reason to delay an offensive, use a shorter operation, or attack at night.

A country can choose a temporary **Night Operations** stance through the army heat protocol system. It should:

- reduce heat exposure gain and selected daytime penalties
- reduce some offensive coordination, air support, or planning benefits unless the country has relevant preparation
- increase fuel, transport, or command burden
- interact with visibility and current doctrine only if a safe supported path exists

This should be a tradeoff, not a free mitigation toggle.

## Unit rotation

The event should identify overexposed formations and offer a rotation mission when a cooler defensible location exists.

A rotation succeeds when:

- named or selected overexposed divisions leave the severe state
- replacement strength remains above a minimum defensive threshold where the mission requires holding a line
- the moved divisions spend a confirmation period in lower Heat Stress
- local supply is not immediately overloaded at the receiving area

Success should:

- reduce division exposure
- improve acclimatized reserve availability
- lower local military load
- strengthen the Army Heat Protocols mitigation package

Failure should:

- raise exposure
- worsen organization recovery
- increase casualty risk at Evolution I
- generate a factual front-line report

The player should not receive a mission that requires abandoning an encircled unit or an irreplaceable capital defense. Mission target selection must check military feasibility.

## Army heat protocols

The national action should establish an event-owned protocol package with staged strength.

The package can include:

- acclimatization schedule
- enforced rest cycles
- drinking-water discipline
- shade and cooling at depots
- adjusted marching hours
- medical screening
- night movement
- forward water distribution
- rotation planning

The action should cost army XP or command power, support equipment, trucks, fuel, or temporary training efficiency. It must stay within four spendable cost types.

Its strength should scale with actual stockpiles and supply. A country should not gain full protection by paying a token command cost while having no trucks or support equipment.

## Mechanized and armored forces

Mechanized forces should face distinct pressure:

- high fuel demand
- engine and cooling strain represented through attrition or reliability pressure when supported
- increased supply load
- slower movement in severe low-infrastructure states
- strong benefit from rail and road maintenance

The event should avoid direct equipment destruction that bypasses the normal attrition and reliability systems unless a specific report event proves a local breakdown incident.

## Air operations

Heat can affect air operations indirectly through:

- overheated airfields
- fuel handling and maintenance burden
- reduced ground-crew productivity
- damaged runways or power service
- high state Heat Stress at the airbase

These effects should remain lighter than land-force effects. They can reduce mission efficiency or airbase throughput where supported, especially during Evolution III. The event should not create a new aircraft heat meter.

## Naval and port operations

Ships at sea should not receive the same state heat treatment as land units. Ports and dockyards can suffer through state industry, water, labor, and power pressure.

Possible effects:

- slower repair and dockyard work
- higher port supply pressure
- reduced loading efficiency
- crew-health reports in enclosed ships during severe port heat

The system should not apply arbitrary naval combat penalties far from affected ports.

## Evolution I military mortality

Systematic military manpower loss begins only with The Killing Heat.

A casualty transaction should require:

- division in Extreme or Scorched state
- sufficient accumulated exposure
- poor supply, failed protocols, active combat, or Critical condition
- a per-division and per-state cooldown
- valid shared military casualty recording

Loss should scale with division manpower and conditions. It should never delete a healthy division in one pulse or bypass the protected logic of the shared casualty system.

Repeated casualties should become less likely after successful rotation and acclimatization. A division that remains in Critical condition should continue to face risk.

## AI behavior

AI military response should consider:

- current war state
- front importance
- enemy strength
- defensible cooler alternatives
- supply map
- current offensive plan
- division exposure
- available reserves
- capital and victory-point defense
- fuel and motorized stockpiles

AI should:

- cancel or delay low-priority offensives in Scorched states
- rotate exhausted units when a valid reserve exists
- keep necessary defensive forces in place when withdrawal would be worse
- prioritize heat protocols during desert or jungle wars
- avoid moving new non-acclimatized units directly into the worst front when acclimatization time exists
- reduce training in severe states

AI must not abandon an entire front because one state crossed a threshold.

## Acceptance cases

1. A supplied acclimatized army in a desert state remains combat-capable but pays a visible logistics cost.
2. An undersupplied offensive army in the same state rapidly loses organization and accumulates exposure.
3. Rotated units recover over time in a cooler state.
4. A fresh division does not lose manpower immediately on arrival during Evolution I.
5. A Critical division in prolonged Extreme heat can take recorded military casualties.
6. A northern mountain front remains less affected than a damaged humid jungle front at the same global intensity.
7. Naval task forces at sea do not receive land-state heat penalties.
