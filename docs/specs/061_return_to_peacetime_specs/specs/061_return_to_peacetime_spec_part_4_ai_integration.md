# Event 061: Return to Peacetime

## Part 4: AI policy, cross-event integration, and world behavior

## AI design purpose

AI countries should treat Return to Peacetime as a strategic transition.

The AI must choose a policy from its military danger, economic capacity, alliance role, current laws, and previous Event 61 state.

Ideology can influence the decision at the margin. Strategic survival takes priority.

The AI should not disarm during direct danger merely because its government is pacifist. It should not spend most of its civilian economy on rearmament when it is isolated, secure, and incapable of using the restored capacity.

## Hidden strategic inputs

The AI can use many hidden inputs without exposing them as player values.

Recommended inputs:

- active defensive war
- active offensive war
- occupied core territory
- enemy war goals or visible preparation
- hostile land border
- hostile naval access for an island state
- relative division strength against likely enemies
- relative military factory strength
- current stockpile shortages
- current air and naval exposure
- faction membership
- faction leadership
- subject status and autonomy
- overlord posture
- major status
- guarantees and defensive commitments
- global tension and current Chaos tier
- current economy and conscription laws
- unresolved Event 61 factory ledger
- current Rearmament Readiness
- Industrial Reconversion Shock phase
- embargo, depression, or construction crisis state
- Event 59 aggressive AI posture
- Event 82 law restoration
- Event 148 pacifist pressure when implemented
- recent defeat or capitulation risk
- recent Event 61 emergency use

These inputs feed one of three policy stances.

## AI stance 1: Reconstruction Pacifist

### Strategic profile

This stance fits a country that is:

- at peace
- secure from immediate attack
- not a faction leader
- not responsible for a large alliance front
- not facing a stronger hostile border
- stable enough to use civilian reconstruction
- politically compatible with demobilization

### Readiness target

Target range: 0 to 30.

### Behavior

The AI should:

- accept most of the initial conversion
- avoid expensive law restoration
- preserve only equipment families needed to prevent immediate shortage
- accept or accelerate some division demobilization
- prefer Central Reconstruction or Civilian Auctions according to economic state
- consider making some factory conversions permanent
- consider voluntary Permanent Peace only under the strict safety test below

### Voluntary Permanent Peace safety test

The AI may voluntarily accept the two extreme laws only when all major safety conditions pass:

- not at war
- no occupied core territory
- no enemy war goal or immediate hostile preparation
- no dangerous hostile land border, or no land border at all
- not a major power
- not a faction leader
- no alliance obligation that requires a standing army
- no likely invasion route under the naval threat check
- high Stability
- low or moderate War Support
- enough civilian capacity to benefit from the route
- no active aggressive strategy from Event 59
- no recent emergency rearmament

The AI should choose voluntary Permanent Peace in roughly 60 to 80 percent of fully qualified secure pacifist cases, subject to probability audit.

A country can qualify for the Reconstruction Pacifist stance without qualifying for voluntary Permanent Peace.

## AI stance 2: Cautious Hedge

### Strategic profile

This stance fits a country that is at peace but has a credible defence concern.

Examples:

- hostile border
- stronger nearby rival
- faction membership
- guarantee obligations
- unresolved claims
- strategic island exposure
- low equipment reserves
- high world tension
- major status
- recent war

### Readiness target

Target range: 50 to 70.

### Behavior

The AI should:

- restart arms contracts
- reopen a limited number of high-value state arsenals
- restore the economy law at least to the recorded pre-event target when affordable
- restore conscription to the pre-event target when threat and War Support justify it
- reconstitute the general staff
- protect the most important stockpile family
- retain cadres and border formations
- avoid Emergency Rearmament unless the danger becomes immediate
- seek the normal Evolution III exemption

A major or faction leader should normally use this stance as its peacetime minimum.

## AI stance 3: Wartime Rearmament

### Strategic profile

This stance fits a country that is:

- in a defensive war
- in a serious offensive war
- losing core territory
- facing an imminent declared attack
- carrying the main burden of a faction war
- under direct high-confidence threat

### Readiness target

Target range: 80 to 100.

### Behavior

The AI should:

- use Emergency Rearmament when normal project time would be dangerous
- protect shortage equipment and logistics
- cancel or avoid voluntary stockpile liquidation
- retain all valid divisions during a defensive war
- reopen the largest safe arsenal states
- restore economy and conscription laws rapidly
- complete the general staff and defence ministry paths
- reject voluntary Permanent Peace
- use Emergency National Defence immediately if trapped under the extreme laws

Defensive war takes priority over ideology and civilian optimization.

## Stance selection score

Use a centralized score model.

A suggested structure:

`rearmament_need = immediate_threat + strategic_role + military_weakness + war_commitment + prior_policy - economic_constraint - security_confidence`

The implementation should not expose this raw score.

Suggested qualitative weights:

| Input | Effect on rearmament need |
| --- | --- |
| Active defensive war | overwhelming increase |
| Occupied core state | overwhelming increase |
| Enemy war goal or visible preparation | very large increase |
| Active offensive war | large increase |
| Faction leader | large increase |
| Major power | moderate to large increase |
| Hostile stronger neighbor | large increase |
| Event 59 aggressive posture | large increase |
| Event 82 law movement | confirm rearmament intent |
| Equipment shortage | increase protection, mixed effect on plant reopening |
| Severe economic depression | reduce normal spending, increase emergency preference if threatened |
| High Stability and secure isolation | large reduction |
| Pacifist political state | moderate reduction only when secure |
| Strong allies covering every front | moderate reduction |
| Low civilian industry | reduce project count, not survival response |

The exact numerical weights require the mandatory probability audit.

## AI decision order

When several actions are valid, use this priority order:

1. avoid immediate military collapse
2. prevent irreversible equipment or division losses
3. protect shortage stockpiles
4. retain essential cadres and threatened-border units
5. restart arms contracts
6. reopen high-value factory ledger capacity
7. restore economy law
8. restore conscription law
9. improve public defence support
10. abandon ledger capacity only when the current stance does not need it

The order is strategic, not a fixed script sequence. The AI can restore a law before a plant when a short law project gives a critical exemption and the plant project cannot finish in time.

## AI economic safety

The AI should not start a normal rearmament project when its required civilian factory commitment would leave too little construction capacity for basic recovery.

Suggested project-cap rule:

- secure small countries run one project at a time
- medium countries run up to two
- large majors run up to three
- defensive-war emergency action can exceed the ordinary cap once

The exact threshold should use available civilian factories after consumer goods and existing commitments.

Do not use total civilian factories without accounting for factories already tied to other systems.

## AI factory target selection

The AI evaluates all valid ledger states even though the human category shows only three.

Preferred states:

- core states
- controlled states with low occupation risk
- states with several ledger units
- states with low building damage
- states connected to the capital or a valid supply network
- states away from an exposed front unless immediate local production is strategically necessary
- states with existing military-industrial concentration when that concentration is safe

Avoid:

- states likely to be lost before project completion
- states with no civilian factory available for conversion
- states whose ledger changed after the decision was evaluated
- non-core occupied territory when a safer core target exists

The AI should not open more projects than its project-cap rule allows.

## AI stockpile protection

The AI evaluates each family from:

- current stockpile surplus after reserve floor
- fielded demand
- production deficit
- active template usage
- current war role
- doctrine and force composition
- replacement time

Priority examples:

- infantry equipment first during general army shortage
- trains during a supply crisis
- convoys for an island or overseas war
- aircraft for a country whose air defence is already weak
- armour for a doctrine and production base built around armoured formations

The AI should not spend resources to protect a family whose eligible liquidation is zero.

## AI division protection

During Mustering Out, AI retention priority should use:

- active defensive front
- capital and port defence
- hostile border assignment
- experience
- equipment percentage
- template role
- replacement difficulty
- strategic mobility

A defensive-war AI should force the involuntary demobilization target to zero when the safety rules allow.

An offensive-war AI should retain enough divisions for its active fronts and may accept a small rear-area reduction.

A secure pacifist AI can accelerate mustering out when civilian benefits are strong and its minimum army remains coherent.

## Subject and overlord behavior

Subjects remain separate country actors.

They receive their own baseline transaction, ledger, Readiness, decisions, and law targets when they use normal civilian systems.

### Low-autonomy subject

A low-autonomy subject should usually follow the overlord's stance unless local direct danger is higher.

- rearming overlord adds a strong rearmament preference
- pacifist overlord reduces subject rearmament preference when the subject has no direct threat
- subject in a defensive war ignores a pacifist overlord
- subject does not reopen more capacity than its own civilian economy can sustain

### High-autonomy subject

A high-autonomy subject weighs the overlord as one foreign factor and can choose a different stance.

### Overlord resource abuse guard

The overlord cannot pay a subject's Event 61 costs through an implicit free transfer.

A future integration may add explicit aid decisions. Such aid needs real civilian, equipment, or convoy costs and must respect the four-cost limit.

### Independence during active transition

A subject that becomes independent keeps:

- its country Readiness
- its active decisions and missions
- its law restoration targets
- its state ledger capacity in states it now owns

It immediately recalculates stance without the overlord modifier.

## Faction behavior

Faction leaders tend toward Cautious Hedge or Wartime Rearmament.

A faction member can remain Reconstruction Pacifist when:

- it has no threatened front
- the faction leader and allies cover its defence
- faction cohesion or strategy does not require a force contribution
- it is not a major

The event does not create a new faction mechanic.

Existing faction systems can use Event 61 Readiness as an input when relevant.

The AI should not leave a faction solely because of Return to Peacetime.

## Major power behavior

Majors have a higher minimum Readiness target because they are more likely to lead alliances, face distant threats, and rebuild military production.

At peace, a major normally targets 50 to 70.

A secure major can accept broad civilian conversion but should preserve a skeletal industrial and planning structure.

The historical research supports this design direction through documented postwar concern about retaining plans and institutions for future mobilization.

## Island and overseas-country threat logic

A country without a hostile land border is not automatically secure.

The AI should examine:

- enemy naval access
- exposed ports
- overseas core territories
- convoy dependence
- hostile nearby naval bases
- current naval and air strength
- faction naval protection

An island major or colonial power can require high Readiness even without a land border.

## Cross-event integration matrix

## Event 9: White Peace

White Peace and Return to Peacetime share the Peace cluster.

Order:

1. White Peace attempts valid war settlements.
2. Return to Peacetime applies the global demobilization transaction.

When White Peace ends a war:

- the country is treated as at peace for the Event 61 baseline and evolved war checks
- any peace-related Chaos reduction belongs to White Peace or the shared peace system
- Event 61 can begin normal demobilization without duplicating the peace result

When White Peace skips:

- Event 61 still fires if valid
- the cluster records the member skip reason

## Event 59: The Offensive

The Offensive changes AI strategy toward aggression.

While its aggressive strategy is active:

- add a strong rearmament-need modifier
- strongly reduce voluntary Permanent Peace willingness
- favor contracts, factory reopening, law restoration, and cadre retention
- retain normal economic safety unless the country is at war

Event 61 does not remove or overwrite Event 59 strategy.

## Event 82: Law Upgrade

Event 82 is the direct inverse law pressure.

Integration rules:

- use shared law-rank helpers
- one Event 82 upward law step counts as actual structural state for Readiness
- Event 61 must not offer another restoration step for the same already-restored rank
- Event 82 does not reopen converted factories
- Event 82 can help a country pass the Evolution III exemption
- challenge achievements can disqualify Event 82 as an external shortcut

When Event 82 moves a country out of Peacetime Economy or No Army, Event 61 should recognize the new law and continue any remaining institutional and factory recovery.

## Event 94: Half Gone

Event 94 removes half of a target's equipment stockpile.

Integration rules:

- Swords into Ploughshares calculates eligible surplus at resolution, not at warning start
- Event 94 can reduce or eliminate a family before Event 61 resolves
- Event 61 never removes equipment below its reserve floor to compensate for an earlier Event 94 loss
- each event records its own stockpile outcome

## Event 103: Conscription

The future rework should use the same conscription law order and rank helpers.

If Event 103 changes conscription while Event 61 is active:

- recalculate Readiness
- compare current law to the Event 61 restoration target
- do not duplicate a step already gained

Event 103 should own its War Support based policy. Event 61 owns the global peacetime reduction and its recovery debt.

## Event 124: Demilitarization

The current catalog concept overlaps strongly with Event 61.

Future design should avoid a second countrywide system that removes ordinary military use from nearly every state.

Recommended differentiation:

- Event 61 owns global economic and military demobilization
- Event 124 can become a geographically bounded demilitarized-zone, treaty, border, occupation, or inspection system

If Event 124 retains state restrictions, it should read Event 61 law and Readiness state without duplicating factory conversion or standing-army abolition.

## Event 131: Widespread Mutiny

Mutiny formations are not orderly demobilization candidates.

Event 61 division selectors must exclude units owned or marked by the mutiny system until that owner resolves them.

A mutiny can increase rearmament need for the government while simultaneously making normal cadre retention harder.

## Event 148: Pacifism

When implemented, Pacifism should:

- increase AI willingness to accept civilian conversion
- reduce normal law-restoration priority when secure
- increase voluntary Permanent Peace willingness under the safety test
- never force pacifist AI to ignore an active defensive war

Event 148 should not set Event 61 Readiness directly. It changes policy preference and can change public values through its own mechanics.

## War events and diplomatic threats

Events 4, 7, 8, 17, and other systems that create wars or imminent war should increase Event 61 urgency through actual campaign state.

The preferred integration is generic:

- active war
- enemy war goal
- occupied core
- hostile border
- faction obligation

Use an event-specific direct flag only when the threat is not represented by ordinary game state.

## Economic events

Industrial Boom, Great Depression 2.0, The Great Embargo, The Black Market, and other economy events can affect Event 61 project cost or duration when they expose stable owner APIs.

Recommended direction:

- boom shortens retooling time but can increase overheating risk in its own system
- depression increases project time and civilian burden
- embargo increases reopening cost and stockpile protection need
- black-market access may create a costly shortcut for tools or components

Event 61 remains complete without those events.

A Black Market shortcut should disqualify challenge achievements that test self-financed recovery.

## Infrastructure and supply events

A strong railway and infrastructure network can modestly reduce factory reopening and demobilization duration.

A damaged supply network can increase the need to protect trains and convoys.

Do not grant Event 61 a large automatic bonus from infrastructure alone. The main inputs remain physical factory capacity, laws, institutions, and public support.

## Navy treatment

Event 61 does not dismantle ships.

Baseline and Peacetime Economy penalties can reduce dockyard output.

Swords into Ploughshares can remove convoys when they are eligible surplus and not protected.

Naval units remain outside The Great Demobilization and No Army division selection.

A future naval demobilization system would need a separate design and safe ship handling.

## Air force treatment

Aircraft in national stockpile can be eligible for Swords into Ploughshares after reserve floors.

Deployed air wings are not directly deleted by Event 61.

Peacetime Economy and Industrial Reconversion Shock reduce the country's ability to replace aircraft through production.

## Special equipment and unit owner contracts

Event 61 should use owner-side disposition where available.

For each unusual equipment or unit family, the implementation inventory should classify it as:

- ordinary and safe for Event 61
- protected by owner package
- incompatible and skipped
- blocked pending owner documentation

Do not maintain a large central hardcoded list when owner APIs can declare safety.

The default for unknown special content is exclusion.

## Law compatibility

Before moving any law, verify that:

- the country uses the ordinary economy or conscription law group
- the current token exists in the ordered helper
- the target token exists and is legal
- another event-owned immutable law system does not forbid the transition

An incompatible law component resolves at zero and records an internal reason.

The player report should use a concise explanation only when the missing change would otherwise look like a bug.

## AI probability audit scenarios

The implementation must route all complex `ai_will_do`, decision weighting, and random selection through `chaosx_ai_probability_auditor` and the HOI4 probability tools.

Required named scenarios:

- `AI61_PEACE_ISOLATED`
- `AI61_BORDER_THREAT`
- `AI61_DEFENSIVE_WAR`
- `AI61_OFFENSIVE_WAR`
- `AI61_EQUIPMENT_POOR`
- `AI61_INDUSTRIAL_MAJOR`
- `AI61_PERMANENT_PEACE_RISK`
- `AI61_EVENT82_OVERRIDE`
- `AI61_SUBJECT_FOLLOWS_OVERLORD`

The full inputs and target outcomes appear in the research probability file.

## Target outcome bands

These are balance goals, not source-only proof.

| Scenario | Expected leading behavior |
| --- | --- |
| Defensive war | Emergency or full rearmament in at least 90% of valid evaluations, voluntary Permanent Peace at 0% |
| Offensive war | Rearmament in at least 80% of valid evaluations |
| Stronger hostile border | Rearmament in roughly 70 to 90% of valid evaluations |
| Secure isolated minor | Reconstruction or pacifist route in roughly 60 to 80% of valid evaluations |
| Peaceful major or faction leader | Cautious rearmament in roughly 60 to 80% of valid evaluations |
| Severe equipment shortage | Protect shortage families before other stockpile decisions |
| Event 82 upward law step | Recognize restored structure and avoid duplicate law action |
| Low-autonomy subject | Follow overlord stance unless local direct threat is stronger |

The probability auditor must evaluate complete option pools when weights normalize against each other.

## Event system integration

Event 61 remains in `global.repeatable_events`.

Its weight, current cap, recovery, and repeat-halving follow the shared Minor Repeatable rules.

A normal firing should not bypass its repeat cap merely because it is also a cluster member.

The event should return to the reworked-event default enable allowlist only when the implementation and testing surfaces are ready.

Until then, it remains disabled by default under the project contract for unreworked events.

## Cluster catalog integration

Cluster 4 currently contains a duplicate member entry for Event 9 in the export snapshot.

The authoritative workbook should be corrected to:

`9, 61`

The cluster detail should explain that it can first end eligible wars and then force countries to dismantle wartime economic and military structures.

The export CSV should be regenerated after the workbook edit.

## Documentation integration

Implementation should create or update:

- Event 61 public event documentation
- decision and mission documentation
- law documentation for Peacetime Economy and No Army
- Event Logs and evolution coverage
- Peace cluster documentation
- achievement documentation
- asset manifest and permanent handoff facts
- catalog workbook and regenerated CSV exports

The documentation should describe actual implemented behavior after validation. It should not copy speculative values that were changed during balance work.

## Integration acceptance conditions

The AI and integration layer is complete only when:

- every AI country resolves to a coherent stance
- direct military danger overrides pacifist preference
- secure minor countries can choose civilian reconstruction
- majors and faction leaders preserve a mobilisation skeleton
- decision weights are evaluated through the probability tools
- AI cannot take invalid, unaffordable, duplicated, or stale-target actions
- subjects and overlords remain separate state holders
- external law changes update Readiness and block duplicate restoration
- Event 9 resolves before Event 61 inside the Peace cluster
- the Peace cluster member list is corrected in the authoritative workbook
- special units and equipment fail closed unless their owners mark them safe
- navy, air, and land handling follow their defined boundaries
- Event 61 remains repeatable under the shared weight and cap rules
- documentation and catalog exports match the implemented state
