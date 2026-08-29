# Great Depression 2.0 specification, part 4: Depression Centers, recovery outcomes, and repeatability

## State-level purpose

Event 35 needs visible local consequences without turning the player into the manager of every state. A small sparse set of `Depression Centers` represents the industrial regions where closures, unemployment, abandoned projects, freight failure, and recovery work are concentrated.

The national Severity value remains the main mechanic. Centers provide concrete state targets, explain important causes, and preserve history after the national category closes.

## Center count

Initial count targets:

- Small economy: one center.
- Medium economy: one or two centers.
- Large major: two or three centers.
- Evolution III inherited corridor: a fourth center only when several distinct high-value regions must be represented.

Three is the normal visible cap. The implementation can keep additional inherited state receipts internally when needed, but it should summarize them instead of exposing a long state list.

## Center selection score

A state is a strong candidate when it is:

- A core state.
- Controlled by the target country.
- Populated.
- Important for civilian or military industry.
- A major resource-processing, railway, port, or supply location.
- An Event 34 Industrial Region.
- The site of an unfinished or fragile boom project.
- Recently damaged in a way that affects national production.

A state receives lower or zero weight when it is:

- Impassable.
- Empty or nearly empty.
- A remote holding with little national economic connection.
- Already selected.
- Under a stronger owner system that forbids conversion.
- Temporarily controlled without a valid recovery claim.

The selector should avoid choosing only the capital when another state carries more industrial weight. It should also avoid choosing three adjacent states that represent one economic region unless an inherited Event 34 corridor makes that concentration meaningful.

## Event 34 conversion priority

When the crisis comes from Event 34, the state registry is not rerolled from scratch.

Priority order:

1. Fragile Miracle Regions.
2. Unfinished or abandoned boom projects.
3. High-value Industrial Regions with failed protection.
4. Runaway Industrialization corridor states.
5. Other high-value industrial states when the inherited registry does not fill the normal center count.

Each inherited state carries its boom history into the local opening condition.

## Local depression stage

Every center has one local depression stage. The exact numeric implementation may remain hidden, but the player sees a named state condition.

| Local stage | Working condition | Meaning |
| ---: | --- | --- |
| `0` | Reopened | Ordinary production and employment have resumed |
| `1` | Distressed | Closures and unemployment are growing, but the center still operates |
| `2` | Idled | A large share of capacity is inactive and freight or credit support is failing |
| `3` | Shuttered | Most supported activity has stopped and reopening requires a major project |
| `4` | Abandoned or Liquidated | Capacity has been deliberately or physically lost and the state needs long reconstruction |

A center can also carry one temporary treatment or protection state, such as protected, under public works, under trusteeship, guaranteed orders, audited finance, or asset liquidation. Treatment is distinct from local stage.

The design should prefer one local dynamic modifier whose strength reads the stage, plus limited treatment modifiers. It should avoid a stack of unrelated state modifiers.

## Opening local conditions

### Independent firing

An independent center normally begins Distressed or Idled. The opening may begin one center at Shuttered only when the target already has severe industrial damage, blockade, or a registered economic shock.

### Event 34 inherited firing

- Completed and protected boom project: Distressed with a strong reopening opportunity.
- Completed but fragile Miracle Region: Idled or Shuttered with high national pressure.
- Unfinished project: Idled with an abandoned-works burden.
- Failed speculative project: Shuttered with credit and unemployment pressure.
- Lost or heavily damaged Industrial Region: Shuttered and disconnected.
- Evolution III corridor state: stage depends on network fragility, protection, and current control.

The inherited path should create a recognizable reversal of the boom. It must not delete the Event 34 state history before Event 35 records the conversion.

## Local progression

A center worsens through sustained national and local pressure. It does not advance one stage every pulse.

Progression factors include:

- Severity band and duration.
- State damage.
- Infrastructure, rail, port, and supply condition.
- Factory concentration.
- Current control.
- Active treatment.
- Doctrine.
- War demand and bombing.
- Local famine or migration pressure from a valid shared context.
- Failed missions.
- Evolution II unrest.

A stage change requires a progress threshold, warning state, or failed objective. The player should see that a center is at risk before normal drift causes a serious closure.

## Physical factory and building loss

The event's baseline identity is economic paralysis. Physical loss is a later consequence.

Rules:

- No factory deletion on the opening day.
- No recurring random deletion while Severity remains high.
- A state must be Shuttered or Abandoned, remain there for a sustained period, and fail a recovery or protection opportunity before involuntary factory loss is eligible.
- Each center has a strict per-episode physical-loss cap.
- A state retains minimum viable capacity where possible.
- Deliberate liquidation is recorded separately from involuntary loss.
- Existing building damage from bombing or disaster is not counted again as Event 35 deletion.
- Building slots are never removed through an unsupported substitute.

A bounded loss may affect one civilian factory, one military factory, infrastructure, or another fitting building based on the state's actual economy and the cause. The implementation should prefer temporary shutdown and damage before permanent level removal.

## Center treatment by doctrine

### Public Works treatment

- Creates employment and construction activity.
- Repairs infrastructure or rail when there is real damage or missing capacity.
- Slows local deterioration.
- Can leave a useful map improvement after recovery.
- Creates unfinished-works risk when interrupted.

### Strategic Industry treatment

- Protects essential factories and production efficiency.
- Requires resources, logistics, and orders.
- Can leave nonstrategic local employment unresolved.
- Creates rescue dependence when kept too long.

### Finance and Trade treatment

- Restores credit and commercial connections.
- Requires an audit, viable institutions, and trade or fiscal support.
- Is less effective when the state is physically destroyed or cut off.

### Austerity treatment

- Cuts subsidies and may close unviable plants.
- Reduces fiscal stress.
- Raises short-term unemployment and social strain.
- Can produce a lean but scarred center.

### Direct Planning treatment

- Places plants under trusteeship, nationalization, or allocation control.
- Protects essential capacity.
- Requires administration and political support.
- Can create long-term efficiency or legitimacy costs.

### Market-Clear treatment

- Allows failure, auction, merger, or liquidation.
- Uses the least direct public capacity.
- Can reopen a smaller viable center.
- Carries the highest risk of permanent factory loss and concentrated ownership.

## Center reopening

Reopening requires more than low national Severity.

A center normally needs:

- Control by the crisis country or a valid successor.
- A completed doctrine-specific project.
- Restored basic transport and supply.
- No unresolved local emergency.
- National Severity below a route-appropriate threshold.
- A successful reopening mission.

A center can be resolved without returning to its exact starting structure. Reopened, restructured, liquidated, or converted outcomes are all valid. The final recovery result distinguishes them.

## Local incidents

Incidents should be sparse and tied to real state conditions.

Baseline incident families:

- Factory gate closures.
- Unpaid wages.
- Freight yards standing idle.
- Local credit cooperatives or emergency finance.
- Municipal relief failure.
- A successful reopening shift.
- Skilled workers leaving the region.
- A contractor or owner abandoning unfinished works.
- A regional authority requesting national aid.
- War orders temporarily reviving one center.

Evolution II adds organized social and political incidents. Incidents should mention the exact state and current treatment. They must not fire for a center that no longer exists or is no longer relevant.

## State control changes

### Temporary loss of control

- Pause active projects.
- Stop country payments for the lost state.
- Preserve completed project receipts.
- Add a national shock based on the state's real industrial importance.
- Allow the new controller to receive a temporary local burden when it uses normal civilian systems.

### Regaining control

- Reconcile the center's current buildings and modifiers.
- Resume or redesign a paused project.
- Do not restore buildings lost through combat or occupation for free.
- Apply a reopening cost based on current state condition.

### Permanent transfer

The original country retains historical loss and national shock records, but stops owning the live center. The new owner can adopt the center into its own Event 35 crisis or manage the local burden through a limited state action. One state cannot be registered as an active center for two countries at once.

## Civil war transfer

A civil war can split Depression Centers between participants. The transfer follows state control and economic continuity.

Rules:

- One side retains the original national episode ID and Severity history.
- A second side receives only the local center burdens it controls, plus a derived crisis condition when its economy is large enough.
- The event cannot clone the full national decision category onto every minor participant.
- Treatment and project receipts move with the state.
- National doctrine does not automatically transfer to an opposing government.
- Evolution II political origins are recorded for later aftermath.

## Recovery proof and center requirement

The national crisis cannot close while a required center is Shuttered without a deliberate resolution. The player must reopen, restructure, liquidate, abandon, or permanently lose it under the state contract.

Strong recovery normally requires every center Reopened or successfully restructured.

Uneven recovery may allow one mixed or scarred center.

Hollow recovery may allow deliberate liquidation or abandonment, with the corresponding permanent cost.

## Recovery legacy budget

A completed episode may leave:

- One main country recovery institution or legacy.
- Up to two meaningful state recovery or scar modifiers under normal conditions.
- Temporary post-recovery safeguard and rebuilding effects.

It should not leave a large stack of small national spirits.

### Public Works legacy

Possible direction:

- Stronger infrastructure maintenance.
- Better construction mobilization during future crises.
- Reduced starting demand stress in a later Event 35 episode.

Cost or limitation:

- A temporary fiscal or consumer burden.
- Maintenance needs for the new works.

### Strategic Industry legacy

Possible direction:

- Better protection of key production regions.
- Faster recovery of production efficiency after an industrial shock.

Cost or limitation:

- Regional inequality.
- Rescue dependence or civilian-sector weakness.

### Finance and Trade legacy

Possible direction:

- Lower future banking-panic risk.
- Better resistance to Evolution I exposure.
- Stronger clearing or trade support actions.

Cost or limitation:

- Foreign dependency or regulatory burden.

### Austerity legacy

Possible direction:

- Lower fiscal stress in a later episode.
- Cheaper maintenance of ordinary government programs.

Cost or limitation:

- Higher social strain after unemployment shocks.
- Weaker relief capacity.

### Direct Planning legacy

Possible direction:

- Better coordination of essential production and logistics.
- Stronger emergency allocation.

Cost or limitation:

- Lower ordinary flexibility.
- Political or administrative burden.

### Market-Clear legacy

Possible direction:

- Lower future rescue dependence.
- Faster reopening of viable private capacity under stable conditions.

Cost or limitation:

- Concentrated ownership.
- Reduced regional capacity or stronger unemployment scars.

## Recovery scars

Scars are used only when the episode created lasting damage.

Possible state scars:

- Hollowed Industrial District.
- Long-Term Unemployment.
- Abandoned Works.
- Rescue-Dependent Industry.
- Concentrated Ownership.
- Broken Freight Connection.

Possible country scars:

- Debt Overhang.
- Policy Fatigue.
- Emergency Controls.
- Labor Bitterness.
- Foreign Credit Dependence.

A scar needs a real source receipt and a future mitigation path where appropriate. It cannot be added because the event simply lasted a long time without a specific consequence.

## Repeat episode memory

Each country stores a compact Event 35 history:

- Episode count.
- Highest Severity reached.
- Entry source.
- Opening and final doctrine.
- Number of doctrine changes.
- Strong, uneven, or hollow recovery result.
- Centers reopened, restructured, liquidated, lost, or abandoned.
- Evolution stages experienced.
- Contagion sent or received.
- Social-collapse outcome.
- Evolution III participation.
- Event 34 collapse count.
- Retained legacy and scars.

The event does not need to preserve every weekly calculation after recovery.

## Repeat target suppression

After recovery, the country receives a safeguard period. Independent target weight remains low during this period. It rises gradually after the safeguard ends.

A consequence path can bypass the safeguard when:

- Event 34 collapses in the same country.
- A valid contagion source converts the country.
- Evolution III pressure crosses the local conversion threshold.

Bypassing independent target suppression does not erase the prior episode. It starts or deepens a new consequence episode with its source recorded.

## Strong reforms and future resistance

A successful recovery can make a later episode easier.

Examples:

- Finance reform lowers initial credit stress.
- Public works improve infrastructure and project speed.
- Strategic rescue protects one center automatically at the next opening.
- Planning improves emergency allocation.
- Austerity reduces initial fiscal stress.
- Market restructuring reduces rescue dependence.

Each reform has a countervailing weakness or limited scope. No route grants permanent immunity.

## Repeated failures

Repeated hollow recovery, Event 34 collapse, or center abandonment can make a later opening worse. The increase is bounded. A country should never become permanently unable to recover because it experienced the event several times.

Anti-death-spiral rules:

- Starting Severity has a cap below Economic Paralysis for ordinary independent firing.
- At least one viable center is selected when the country has one.
- Emergency costs scale down with usable capacity.
- Permanent factory losses have per-state and per-episode caps.
- Strong reforms can offset prior scars.
- A small economy is not asked to support large-major project counts.

## Exploit controls

### Factory-loss farming

A player cannot deliberately lose one cheap factory to gain a stronger permanent legacy. Recovery legacy is based on completed policy and state work. Liquidation reduces the legacy budget and adds scars.

### Building-slot farming

Event 35 does not create free building slots. Public works can add or repair real buildings under a strict project budget. Repeat episodes use diminishing state returns.

### Transfer farming

Transferring a center cannot reset its project, recreate costs, or duplicate its recovery reward. State receipts move with the state and retain the episode ID.

### Aid farming

Foreign aid consumes real provider resources and uses source-target cooldowns. The same package cannot be claimed twice through faction, subject, and bilateral paths.

### Doctrine-switch farming

Switching has a cooldown and policy-whiplash cost. Completed doctrine actions cannot be repeated merely by leaving and returning to the doctrine.

### Maximum-Severity farming

Reaching `100` cannot repeatedly grant emergency aid or trigger the same factory loss. The maximum emergency uses one-shot receipts and cooldowns.

## Cleanup after recovery

After the recovery result is frozen:

1. Cancel active state projects that cannot continue.
2. Resolve refundable commitments through exact receipts.
3. Remove temporary center treatments.
4. Convert state stages into reopened, mixed, or scar outcomes.
5. Apply the bounded national legacy.
6. Clear active arrays and selected-state pointers.
7. Preserve compact history and state receipts.
8. Start the post-recovery safeguard.

No active Event 35 state modifier, mission, or decision should remain without a documented post-recovery purpose.
