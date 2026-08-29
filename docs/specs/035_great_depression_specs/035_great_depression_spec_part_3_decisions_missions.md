# Great Depression 2.0 specification, part 3: Decisions, recovery doctrines, and missions

## Presentation choice

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

The baseline mechanic uses one ordinary decision category with a strong static category picture and compact dynamic text. It does not begin with a separate scripted GUI.

The category header shows:

- Depression Severity.
- Severity band.
- Trend.
- Current baseline phase.
- Current recovery doctrine.
- Next meaningful threshold.
- Up to three material causes.
- The selected Depression Center when a state action is open.
- The active main objective.

The category should normally expose three to five primary actions. Six is the hard maximum for one phase. One to three missions may be visible at once. Obsolete, invalid, completed, or lower-priority actions are hidden.

A dedicated event-owned window is justified only if implementation inspection proves that the ordinary category cannot show Severity, one selected center, and the active mission clearly. Such a change requires a documented design exception, exact GUI ownership, and the event UI workflow.

## Recovery doctrine

The country chooses one current recovery doctrine during Panic and Contraction. The doctrine is a categorical policy state, not another numerical meter. It controls which actions, costs, incidents, AI preferences, and recovery legacies are available.

The six doctrines are working design labels. Final player-facing names and descriptions must follow the writing-direction rules in part 10.

1. Emergency Public Works.
2. Rescue Strategic Industry.
3. Stabilize Finance and Trade.
4. Austerity and Retrenchment.
5. Direct State Planning.
6. Let the Market Clear.

The doctrine choice should be made after the opening shock has shown the country's material problems. It cannot be a free click before the player sees the crisis.

### Doctrine switching

A country may reconsider its doctrine through a Cabinet Review action after a meaningful cooldown. Switching doctrine should:

- Consume political and administrative capacity.
- Pause some ongoing doctrine-specific projects.
- Add short policy-whiplash pressure.
- Preserve completed state work.
- Block immediate repeated switching.
- Become unavailable during the maximum-Severity emergency unless an emergency government outcome explicitly changes policy.

A reasonable initial cooldown target is `90` to `120` days. The action should use no more than four spendable costs. Political power may be one cost because the action represents a major cabinet change. It should not be the only cost.

The country can finish the crisis under a doctrine different from the one chosen at the opening. The history ledger records the opening doctrine, final doctrine, number of switches, and major route actions. This affects recovery legacy and achievements.

## Shared action families

Several action families exist across doctrines. Their effects and costs vary by route.

### Select a Depression Center

A human player can select one active center for state-targeted actions. The selected-center flow should use a compact show and hide pattern instead of displaying every state action for every center at once.

Selection requirements:

- The state is in the country's current Event 35 center registry.
- The country controls it or has a valid recovery claim under the transfer contract.
- The state is not already resolved.
- The planned action is valid for its local stage.

AI evaluates all valid centers directly and does not need the player selector.

### Emergency Relief Allocation

Represents temporary household relief, food distribution, local administration, and basic employment support. It slows demand and social deterioration while consuming civilian capacity, equipment, manpower, or stability.

It should be useful in every doctrine, but its cost and strength depend on policy. A public-works government can integrate relief into employment. An austerity government pays a higher political or stability cost. A market-clear government uses it only as an emergency floor.

This is a stabilizer, not a complete recovery route.

### Protect a Depression Center

Commits resources to keep one center connected to power, rail, fuel, orders, and basic credit.

Possible costs include:

- Civilian factory commitment.
- Trains or trucks.
- Support equipment.
- Fuel.
- Temporary output sacrifice.

The action uses no more than four spendable cost types. It gives a state protection receipt, slows local stage deterioration, and supports the national Severity trend. It does not grant free factory levels.

### Reopen or Restructure a Center

Available during Depression or Stabilization after the center's immediate emergency is controlled. The exact route depends on doctrine and local history.

Possible results include:

- Reopening existing factories.
- Converting an unfinished project into useful infrastructure.
- Consolidating several failed plants into one protected network.
- Replacing a local depression modifier with a recovery modifier.
- Accepting bounded liquidation and a long-term scar.

A center cannot be reopened through one instant purchase. It requires a timed project or mission.

### Request Foreign Support

Available only when a valid partner, route, and relationship exist. It may provide credit, equipment, convoys, fuel, industrial orders, or public works support.

The receiving country accepts a cost or dependency consequence. The provider pays real resources or industrial commitment. No aid is created from an invalid or nonexistent partner.

Evolution I and III expand this family.

### Emergency Policy Review

Appears when the current doctrine has become materially impossible. It can open an emergency doctrine switch, scaled retreat, or coalition policy. It should never become a free escape from route costs.

## Doctrine 1: Emergency Public Works

### Route identity

The government uses public construction and employment to restore demand, freight, and confidence. The route trades current civilian capacity, logistics, and equipment for steady Severity reduction and durable infrastructure.

It is strongest when:

- The country has usable civilian factories.
- Depression Centers have repairable infrastructure or railways.
- Unemployment and demand stress are major causes.
- Stability is threatened by prolonged idleness.
- The country can protect project sites.

It is weaker when:

- Core territory is being overrun.
- The country lacks trains, equipment, or construction capacity.
- Blockade prevents material supply.
- A short military emergency requires immediate armament output.

### Primary actions

#### Launch a Regional Works Program

Starts a state-targeted project in the selected Depression Center. The project should address an identified need such as rail repair, infrastructure, a port connection, anti-air protection, housing support represented through state recovery, or conversion of abandoned works.

The decision commits civilian factories and up to three additional material costs. Project duration scales with state damage, Severity, infrastructure, war state, and earlier failures.

Success:

- Lowers demand and employment stress.
- Improves the state recovery stage.
- Adds a bounded map improvement when the project corresponds to real damaged or missing infrastructure.
- Creates progress toward the public-works recovery legacy.

Failure or interruption:

- Leaves an unfinished works burden.
- Returns part of unspent resources when proof exists.
- Raises local frustration and Severity.
- Can be resumed at a reduced or increased cost depending on why it failed.

#### National Employment Guarantee

Starts a timed country objective that commits a larger share of civilian capacity to employment and relief. It lowers demand and social pressure while active. Its long duration can create fiscal stress if maintained without recovering production.

The player must keep a minimum usable civilian base and avoid losing too many project states. The objective can succeed, partially succeed, or fail.

#### Convert Works into Lasting Capacity

Available during Stabilization. It selects completed projects that can become ordinary infrastructure, railway capacity, or a long-duration state recovery modifier. It closes temporary relief administration and prevents the route from keeping permanent emergency costs after recovery.

### Route tradeoff

Public works can overextend the state. Too many simultaneous projects increase fiscal and logistics stress. The route should normally cap active major projects at one, with a second allowed only for a large economy under favorable conditions.

## Doctrine 2: Rescue Strategic Industry

### Route identity

The government protects military production, resource processing, transport nodes, and a small number of industrial regions. It preserves essential output at the cost of civilian capacity, regional equality, and possible long-term rescue dependence.

It is strongest when:

- The country is at war.
- One or two regions carry most military production.
- Military demand is still usable.
- The country has resources and logistics to keep protected plants running.

It is weaker when:

- The crisis is mainly household demand and finance.
- Protected plants have no fuel, resources, or transport.
- Stability is collapsing because civilian regions are abandoned.
- The country has too little industry to divide into strategic and nonstrategic sectors.

### Primary actions

#### Designate a Strategic Plant Network

Marks one Depression Center as a strategic rescue priority. The state receives protection against local output collapse and shuttering. The country commits civilian factories, resources, logistics, or output from other sectors.

The action cannot protect every center. Normal capacity is one protected network. A very large major may support two at a sharply rising cost.

#### Guarantee Essential Orders

Uses military procurement or another exact national demand source to keep selected plants active. It protects production efficiency and employment in the center. It raises fiscal stress and may worsen civilian shortages.

The decision should not grant military equipment for free. It preserves or improves the ability to produce equipment that the country can already support.

#### Consolidate Failing Industry

Combines or restructures failing plants. It can prevent random physical loss, but may accept one bounded factory closure, a temporary output penalty, or a regional scar in exchange for lower Severity and a more stable center.

### Route tradeoff

A country can recover aggregate output while leaving unemployment and resentment outside protected regions. High rescue concentration feeds Evolution II social strain and creates a mixed recovery legacy.

## Doctrine 3: Stabilize Finance and Trade

### Route identity

The government restores confidence, reopens viable institutions, protects trade credit, and preserves imports. It reduces volatility and international exposure while committing reserves, shipping, civilian capacity, and diplomatic flexibility.

It is strongest when:

- Banking and trade pressure are major causes.
- Ports and convoys remain usable.
- The country has foreign partners.
- Evolution I exposure is active.
- The state can distinguish viable institutions from failed ones.

It is weaker when:

- The country is blockaded.
- Core industry is physically destroyed.
- No valid partner or route exists.
- The government lacks confidence or administrative capacity.

### Primary actions

#### Declare a Temporary Bank Holiday and Audit

Briefly restricts ordinary financial activity while the state evaluates institutions. It applies a small immediate output cost, stops the fastest credit deterioration, and starts an audit mission.

Success reopens viable institutions, lowers credit stress, and enables stronger finance actions. Failure or premature reopening creates a renewed panic.

#### Recapitalize Viable Institutions

Commits civilian capacity, political authority, and possibly a foreign credit source. It lowers credit stress and reduces future bank-panic risk. Repeated use without reform creates rescue dependence and fiscal pressure.

#### Negotiate Clearing and Import Agreements

Targets a valid partner or group of partners. It uses convoys, fuel, civilian factories, diplomatic conditions, or reciprocal commitments. It reduces trade stress and can open an aid or supplier relationship.

#### Establish a Durable Credit Guarantee

Available during Stabilization after successful audit and recapitalization. It creates the finance-route recovery institution and closes temporary emergency support.

### Route tradeoff

Guarantees can become expensive. Foreign credit can create dependency. A country that protects finance while leaving factories and employment unrepaired may stabilize the meter without completing state recovery.

## Doctrine 4: Austerity and Retrenchment

### Route identity

The government cuts commitments, narrows relief, restructures debt, and attempts to restore fiscal credibility. It can lower fiscal and credit pressure quickly while worsening unemployment, demand, and political strain.

The route must be viable under some conditions. It is not written as an automatic failure or moral lesson.

It is strongest when:

- Fiscal stress is the main cause.
- Stability and institutions are strong.
- The country has reserves or external demand that can absorb cuts.
- Severity has already left the deepest bands.
- The player accepts a slower and harsher social recovery.

It is weakest when:

- Demand collapse and unemployment dominate.
- Evolution II social strain is already high.
- Stability is low.
- Several centers are shuttered.
- The country is in a severe postwar contraction.

### Primary actions

#### Balance the Emergency Budget

Cuts or suspends selected emergency commitments. It reduces fiscal stress and some civilian burden. It raises demand and social pressure for a defined period.

#### Restructure Public Obligations

Begins a debt standstill, negotiated restructuring, or domestic conversion. It can provide a strong one-time reduction in fiscal and credit pressure. It costs diplomatic flexibility, confidence, or access to future foreign support.

#### Retrench the Relief Administration

Ends selected temporary programs. It frees civilian capacity and can support the final recovery proof if unemployment and centers are already controlled. Used too early, it causes relapse.

#### Restore Ordinary Budget Rules

Stabilization action that converts emergency austerity into a bounded long-term institution. It removes the route's temporary policy burden and defines its recovery legacy.

### Route tradeoff

Austerity can produce a clean fiscal result with a damaged labor market. It carries the strongest risk of Social Collapse when used at high Severity or low stability.

## Doctrine 5: Direct State Planning

### Route identity

The government places finance, transport, production, and distribution under coordinated public control. It reduces volatility and protects essential output while consuming political legitimacy, administrative capacity, and trade flexibility.

It is strongest when:

- The country has administrative capacity.
- Several sectors must be coordinated at once.
- Trade access is weak and domestic allocation matters.
- Strategic industry and public works need a common plan.
- The government has political support for intervention.

It is weaker when:

- The state is fragmented.
- Corruption or low stability blocks execution.
- The economy depends on flexible foreign trade.
- Planning targets are repeatedly missed.

### Primary actions

#### Establish an Emergency Production Board

Creates the route's central institution. It permits state allocation actions and lowers volatility. It adds administrative and political costs.

#### Nationalize or Place Failing Industry under Trusteeship

Targets one center. It prevents immediate shuttering and allows planned reopening. It can create a compensation, resistance, or efficiency cost depending on ideology and current law.

#### Ration Strategic Inputs

Directs fuel, transport, resources, or civilian capacity toward identified priorities. It protects selected output and raises civilian or trade pressure elsewhere.

#### Complete the National Recovery Plan

A stabilization mission that requires functioning centers, controlled Severity, and completed planning targets. Success creates a bounded planning institution. Failure extends emergency controls and policy fatigue.

### Route tradeoff

Planning can solve coordination while weakening ordinary flexibility. Poor execution raises corruption, policy fatigue, and Social Collapse risk. The route should not be a universal best choice for every ideology or economy.

## Doctrine 6: Let the Market Clear

### Route identity

The government accepts closures, asset repricing, contract failure, and short-term contraction in the belief that a smaller viable economy will recover without a permanent emergency state. It has the lowest direct state cost and the highest short-term risk.

It is strongest when:

- Stability and institutions are strong.
- The country has private reserves and functioning courts or commercial administration.
- Severity is moderate or falling.
- Failing centers contain obsolete or duplicated capacity.
- The country can tolerate a short output loss.

It is weakest when:

- Severity is near maximum.
- Evolution II social strain is high.
- The country is at war and needs immediate output.
- A single center carries most national industry.
- Households and banks lack any safety floor.

### Primary actions

#### Withdraw Emergency Support

Ends selected subsidies or guarantees and increases short-term closure risk. It reduces fiscal pressure and future rescue dependence.

#### Auction or Reorganize Failed Assets

Targets a distressed center. It can reopen part of the state under new ownership, liquidate one bounded factory level, or leave an unresolved local burden. The outcome depends on credit, stability, demand, and center condition.

#### Remove Emergency Controls

Restores ordinary price, trade, or production discretion. It can improve future efficiency when the economy is ready. Used early, it raises volatility and Severity.

#### Certify the Cleared Economy

Stabilization action that proves failed obligations and plants have been resolved. It creates a lean recovery legacy and closes temporary liquidation mechanics.

### Route tradeoff

The route can recover without large state commitments. It can also turn a recoverable depression into Economic Paralysis. A country that uses it successfully should still carry visible regional or concentration consequences when major closures occurred.

## Main missions

### Halt the Panic

Opening mission during Panic and Contraction.

Goal:

- Prevent Severity from entering or remaining in Economic Paralysis.
- Resolve at least one dominant opening cause.
- Keep at least one Depression Center operating or protected.

Duration target: `70` to `100` days, scaled by opening conditions.

Success:

- Ends the strongest opening shock on schedule.
- Grants temporary stabilization momentum.
- Advances the country into the sustained Depression phase.

Failure:

- Adds one guarded shock.
- Worsens one valid center.
- Extends opening penalties for a bounded period.

### Keep Essential Freight Moving

Appears when rail, port, convoy, fuel, or train disruption is a top cause.

Goal:

- Restore a named transport condition.
- Maintain minimum logistics reserves.
- Protect the selected center's connection.

Success lowers industrial and trade pressure. Failure adds a freight-collapse shock and can interrupt state projects.

### Reopen a Depression Center

State-targeted mission available after protection or restructuring begins.

Duration target: `90` to `180` days.

Goal varies by doctrine. It may require construction commitment, stable supply, bank audit completion, protected military orders, trusteeship, or completed liquidation.

Success advances the center to reopened or resolved status. Failure preserves part of completed work and creates a route-specific setback.

### Prevent a Relapse

Stabilization mission.

Goal:

- Keep Severity below the relapse threshold.
- Maintain required center status.
- Avoid an unresolved major shock.
- Complete doctrine consolidation.

Duration target: about `90` days.

Success advances the final recovery proof. Failure returns the country to Depression without repeating the original opening event.

### Maximum-Severity emergency

Replaces ordinary missions at Economic Paralysis. The exact route reflects doctrine and current causes. It must remain payable by a crippled country through scaled costs, foreign aid, reserve use, or temporary sacrifice.

### Prevent National Breakdown

Baseline political emergency that appears after the National Breakdown warning and before a possible civil conflict.

Goal:

- Lower Severity out of the near-paralysis range.
- Resolve the active cabinet, legitimacy, or emergency-government crisis.
- Restore, protect, or credibly restructure at least one Depression Center.
- Complete one viable employment, finance, supply, or settlement action.

Duration target: `120` to `180` days, shortened only by an immediate constitutional or military crisis.

Success:

- Clears the warning.
- Blocks another baseline breakdown check for a substantial cooldown.
- Preserves the active depression and recovery work.

Failure:

- Calls the strict baseline political-outcome validator.
- Can cause a government fall, emergency rule, policy reversal, prolonged unrest, or rare civil conflict.
- Does not create a war when no coherent actor, territory, force package, or political base exists.

When Evolution II is active, its strike, mandate, coup, separatist, or civil-conflict missions replace this baseline objective. Both systems cannot run at the same time.

### Evolution missions

Evolution I, II, and III add specialized missions described in their own parts. These missions share the same active objective cap. Evolution content must replace lower-priority baseline actions and must not create a wall of new decisions.

## Cost design

Each decision uses no more than four spendable cost types. Conditions such as controlling a state or having a valid partner do not count as spendable costs.

Preferred cost families:

- Civilian factory commitment.
- Temporary military output sacrifice.
- Trains.
- Trucks.
- Convoys.
- Support equipment.
- Fuel.
- Manpower.
- Stability.
- War support.
- Political power for genuine cabinet or legal actions.
- Time and mission risk.

Costs scale from usable capacity. A country at high Severity cannot be charged against factories that the event has already made unavailable.

The UI must show the exact player-facing costs with matching texticons. Dynamic requirements receive concise custom tooltips.

## Decision visibility by phase

| Action family | Panic and Contraction | Depression | Stabilization | Recovery proof | Economic Paralysis |
| --- | --- | --- | --- | --- | --- |
| Choose doctrine | Once | Hidden | Hidden | Hidden | Hidden |
| Cabinet Review | Conditional | Available after cooldown | Conditional | Hidden | Emergency only |
| Emergency Relief | Available | Conditional | Hidden or reduced | Hidden | Emergency form |
| Protect Center | Available | Available | Complete existing only | Hidden | Emergency form |
| Doctrine primary action | Available | Available | Consolidation form | Hidden | Replaced by emergency action |
| Reopen Center | Hidden | Available after prerequisites | Available | Complete existing only | Hidden |
| Foreign Support | Conditional | Conditional | Conditional | Hidden | Emergency form |
| Halt the Panic | Active mission | Hidden | Hidden | Hidden | Hidden |
| Prevent a Relapse | Hidden | Hidden | Active mission | Can continue | Hidden |
| Maximum emergency | Hidden | Hidden | Hidden | Hidden | Active mission |

## AI equivalents

AI countries use the same costs, consequences, cooldowns, and state records. They do not receive free Severity reduction.

AI decision scoring considers:

- Severity band and trend.
- Dominant causes.
- Usable civilian and military factories.
- War state and military urgency.
- Trains, trucks, convoys, fuel, and equipment floors.
- Stability and social strain.
- Number and value of centers.
- Current doctrine and switch history.
- Expected recovery time.
- Evolution exposure.
- Foreign aid availability.
- Long-term legacy and short-term survival.

The named AI scenarios and expected orderings are defined in part 9 and the probability matrix.

## Cleanup

When the crisis ends or the country becomes invalid:

- Hide and cancel ordinary decisions.
- Cancel missions and resolve any committed-resource refund contract.
- Clear the selected-center pointer.
- Remove temporary doctrine and emergency modifiers.
- Preserve completed state receipts and recovery history.
- Remove invalid foreign targets.
- Keep only the bounded recovery legacy and scars.

No decision may remain clickable after its target state, partner, doctrine, or crisis episode is gone.
