# 03. An army sized to the world

## Scale military capacity, not just a modifier

The opening is built from real divisions, complete legal templates, actual equipment, human and nonhuman recruitment pathways, operational special systems, fuel, supply and production. Attack bonuses alone cannot satisfy it. The setup snapshot includes the world's existing military, industry, population, technology, major powers and campaign maturity before the Directorate receives anything.

Exclude dormant CXT inventory, provisional Directorate assets, dead tags and duplicated subject accounting from the snapshot. Count actual deployed and usable strength rather than division names alone. One hundred nearly empty divisions must not be treated as equivalent to one hundred equipped formations. Where precise native measurements are unavailable, document a conservative source-backed estimator and its blind spots in the implementation evidence.

## Proposed land-force anchor

Use normalized combat-division equivalents to compare armies. A reference equivalent is a broadly serviceable twenty-width formation at full strength, including its expected combat equipment. This is an accounting reference, not a mandatory template copied onto every family.

Let `Dworld` be the outside world's usable land equivalents, `Dmajor` the strongest surviving major's equivalents, and `Dfront` the combined equivalents of initial enemies. The initial target is:

`D0 = intensity × chaos factor × excess-age factor × max(150, 0.35Dworld, 1.50Dmajor, 1.25Dfront)`

Proposed natural-arrival intensity is 1.00. The scenario multipliers are in Part 09. The floor of 150 makes the opening a large army even in an early or depleted world. A developed world can demand many hundreds of equivalents. These anchors deliberately favor the boss.

The Chaos factor begins at 1.00 near 1000 and rises by approximately 15 percent per additional 250 Chaos, with diminishing marginal gain after the first 1000 excess Chaos. The excess-age factor begins at 1.00 and adds approximately 10 percent per qualifying year beyond the grace, also with diminishing marginal gain. Neither factor falls below its opening value after spawn. Subsequent reductions in Chaos do not erase troops or remove the boss.

Campaign maturity, technology and unit quality are applied to the composition and equipment budgets, not multiplied again into this land total. Population determines the human reserve and replacement pathway. Industry determines sustainable production and repair. This avoids multiplying correlated indicators until the army becomes an accidental arithmetic explosion.

### Example design calculations

| World snapshot | Largest term before intensity and Chaos | Interpretation |
| --- | ---: | --- |
| 500 world equivalents, 100 strongest major, 120 initial enemies | 175 | A very large opening army even against modest neighbors |
| 1400 world equivalents, 300 strongest major, 500 initial enemies | 625 | A major continental coalition receives a correspondingly large opponent |
| 3500 world equivalents, 800 strongest major, 700 initial enemies | 1225 | Late-game scale follows the developed world |
| 100 world equivalents after devastation | 150 | The final boss retains an enormous minimum presence |

These are arithmetic illustrations of the proposed formula. They are not observed game outcomes and do not imply that each equivalent must become a separate engine division.

## Composition with real family identity

Every installed combat family gets a valid opening formation at natural intensity when its owner adapter can legally materialize it. Related families may share a formation only when their native grouping, equipment and support exclusions permit it. If the minimum legal roster exceeds the numerical target, increase the roster target. Do not drop unusual families to preserve a quantity quota.

The remainder fills battlefield roles dynamically. The initial land planning mix allocates about 40 percent to line holding and assault, 25 percent to breakthrough and exploitation, 20 percent to specialist terrain or anomalous roles, and 15 percent to reserve and replacement depth. These are role priorities after minimum family coverage, not fixed template quotas. Air, naval and delivery-support budgets are additional separate ledgers sized to the operational theater.

The mix adapts to local terrain and enemy equipment. Robots do not erase their native forest, jungle and marsh weaknesses. Elephant, cave, rat, ghost, clone, zombie, revolutionary and experimental forces retain their actual unit behavior. CBRN supports obey compatibility and exclusion rules. The country fields a combined force instead of forcing every support company into an illegal universal template.

A family may be trainable, owner-spawned, projected through a special operation or attached to another formation. Universal access preserves those real forms. The player must have a documented way to obtain and use each family, even when ordinary recruitment is impossible for that unit type.

## Personnel and equipment

Opening manpower covers all human personnel required by the committed force plus a substantial replacement reserve. The reserve target combines roughly 120 days of heavy projected losses with a floor based on the largest enemy army's personnel. World population limits the scale comparison, not the physical population of the single spawn state.

This opening reserve is explicitly anomalous military materialization. Record it separately from civilian population. Do not subtract people from random countries, add the same amount to state population, or increase the shared Deaths ledger. Nonhuman bodies that use zero human manpower remain zero-manpower units. Clones and other manufactured troops use their real equipment or production obligations.

Stockpiles cover the exact committed formations at full strength, their operational support needs and an initial 120-day replacement horizon. Concrete equipment variants are created before their stockpile and unit consumers. Equipment quantities are derived from the real template and provider manifests. A generic infantry stockpile is not an acceptable substitute for a missing robot, clone, elephant, payload or protective-equipment requirement.

All installed technologies are available through the universal contract in Part 04. The opening force's standard equipment follows the better of contemporary world capability and the boss's advanced initial profile. Experimental equipment appears alongside it immediately. Keeping some future equipment in smaller operational lots gives production choices a purpose without pretending it remains locked.

## Industry in one state

The spawn state receives the highest legal useful levels of infrastructure, supply support and military production that the installed map and building rules permit. Existing factories and stockpiles are measured before transfer. Grants do not overwrite them or count them twice as both captured wealth and new materialization.

The industrial target is approximately the greater of one leading major's usable military output and one quarter of world military output, scaled by scenario intensity. Native buildings supply as much of that target as the one state can legally hold. Freeze the remaining absolute output allowance once at successful setup as `A0 = max(0, opening target - legal native output at commit)`. A Directorate-owned industrial adapter supplies that allowance through actual legal production capacity. Recalculate the adapter's percentage as native capacity changes, without recalculating `A0` from the later world.

The current base envelope is `Qbase = current usable native output + A0`. Thus a genuinely conquered factory increases net output. It does not merely replace an invisible minimum-output floor, and it does not multiply the entire opening allowance again. Native output includes only real current controlled capacity and its ordinary usable contribution, excluding the Directorate adapter, Event 103 focus additions and terminal amplification. At zero legal native production capacity, the adapter cannot divide by zero or create free stockpiles. Production resumes only when a valid physical production consumer is restored.

### One capacity calculation for focus and terminal changes

Each focus or operation declares the capacity it changes, its real opportunity cost, duration and single accounting owner. An allocation changes the share assigned to a role inside the existing envelope. A permanent output improvement enters the approved additive output-bonus sum once. A preparation, repair or transport improvement affects its named operation and is not also counted as military factory output.

For effects that genuinely increase the same output dimension, the accounting target is `Qtarget = phase factor × Qbase × (1 + sum of approved additive output improvements)`. The terminal phase factor is 1.50 only after the one committed ending transition. Native modifier wiring must reach that one target rather than stack the adapter, focus, spirit and terminal consumer as independent copies of the reward. Existing native multiplicative behavior must be measured and compensated in the adapter if required. No output improvement also grants its implied future production as a free equipment shipment.

The output surge in Part 06 reallocates approximately 15 percent toward its selected requirement by deferring equivalent productive or repair work. It is not an extra 15 percent permanent addition to every line. Servicing and later efficiency investments use their explicit earned improvement once. Replace spirit stages from the current ledger, never apply their previous total again on refresh or recapture.

There is no illegal building-stack workaround and no automatic acquisition of a second state for campuses. The initial industry is deliberately extraordinary, but it remains attached to a visible country and vulnerable territory. Capture of the last state removes the country and its output.

Civilian capacity prioritizes supply, repairs, airfields, coast access and restoration of captured industry. Military production maintains the active force and reserve. Dockyards and legal ship deployment begin once an owned coastal state exists. An inland origin receives transport research, designs, convoys in reserve and an explicit coastal campaign objective immediately.

## Keeping the opening army functional

A huge army in one state needs exceptional supply support. The opening package therefore combines a legal local hub and infrastructure, abundant trains and trucks, fuel, equipment reserves, strong supply grace and a temporary extraordinary reduction in supply consumption. The target is usable combat organization and movement at first contact, not merely a large division counter stack.

The first tuning band for the foothold supply reduction is 70 to 90 percent. That band is not a ceiling or a substitute for readiness proof. Measure the complete committed army's unmodified demand `D` and the chosen state's verified usable delivered throughput `T`, including its actual native network and legal support. For positive `D` and `T`, the initial reduction must be at least `1 - T / (1.10 × D)`, rounded toward sufficient support within the verified native range. The 10 percent margin is a proposed opening buffer. Recheck the resulting demand against actual delivery after the engine has applied the setup, rather than trusting the requested modifier value.

Readiness requires full planned personnel and equipment, usable reinforcement, fuel for active consumers, legal placement, and at least 90 percent of each opening formation's currently supported maximum organization as a tuning target. The complete first-contact land force must fit the measured reduced demand with the buffer. A zero-demand family contributes no fictitious demand. Zero delivered throughput is a failed logistics setup until a real legal route supplies it.

If the required reduction exceeds 90 percent, increase the extraordinary support within verified native limits and prove the resulting operation. If the engine cannot meet the committed plan with legal support, the configuration remains an implementation blocker and provisional setup rolls back. Do not drop families, shrink the world-scaled force, add a second state, hide units in an unusable reserve or publicly announce a half-functional country to pass this gate. Reviewed formation compression under the later performance rule must preserve the same serviceable force and cannot substitute for supply proof.

This allowance belongs to the existing war-economy or sustainment spirit slot, not an invisible stack of independent grants. It relaxes toward a powerful mature-war allowance only when real connected centers can carry the active theater plan. As an initial safeguard, reduce the concession by no more than five percentage points in a thirty-day interval, and only after a full fourteen days in which verified usable throughput would cover the complete active force at the proposed next value. A new deficit pauses relaxation. The rule never removes the allowance just because a date or focus has passed.

Enemy action remains meaningful. Destroyed hubs, disconnected fronts, lost airfields, convoy losses, fuel shortages and isolation of newly deployed armies reduce local effectiveness. The central allowance keeps the boss viable while sustained interruption slows its expansion. It does not make all units immune to encirclement, attrition or combat losses.

Opening air capability includes real aircraft and wings suited to the available airfield and intended operations. Unbased aircraft remain in stock until legal bases are secured. Initial raid capacity may use only legally supported bases and delivery systems. A landlocked origin does not receive a fleet in an inland province.

## Growth after arrival

After setup, production and conquest become the primary growth paths. New factories, population access, stockpiles, scientists, logistics and strategic assets are processed through the real absorption rules. The opening snapshot is not recalculated into a fresh free army every week.

An owner pulse may update target composition and replacement priorities from current enemies and owned resources. It may not continually match enemy losses with free replenishment, turn changes of controller into fresh grants or include its own troops in a world-scaling feedback loop. New package registration adds newly installed capabilities through a one-time version receipt. It does not rerun the baseline materialization.

There is no gameplay power cap chosen to make the final boss ordinary. If engine performance requires fewer entities, preserve family coverage and equivalent manpower, equipment, frontage roles and combat power through reviewed legal formation sizing. Any compression has to be reported with the before-and-after force accounting. Silent removal of families or a disguised large vanilla template fails acceptance.

## Sustainment coverage indicator

The second dedicated public indicator summarizes whether the present planned force can be maintained. Compute it from the limiting relevant coverage of reinforcement equipment, manpower or manufactured bodies, fuel and supply throughput. Show the Directorate player a broad condition and a rounded percentage, with the limiting component in a tooltip. A zero-manpower robot formation does not create a fictitious manpower deficit.

Do not include unavailable ocean facilities in the first-hour land-force denominator. Once a naval or airborne campaign becomes active, its real transport and basing needs join the planned requirement. This value supports an operational decision. It is not another resource to spend or a score that directly creates units.

For initial tuning, use a rolling 30-day active-force sustainment target rather than the full opening reserve horizon. Calculate equipment coverage from the least supplied essential active equipment class, personnel coverage from the relevant human or manufactured-body replacement requirement, fuel coverage from the active fuel-consuming force, and supply coverage from the active theater's delivered throughput against demand. The public ratio is 100 times the lowest applicable normalized coverage, clamped between zero and 100. A requirement absent from the active plan is omitted, never divided by zero. A rare nonessential reserve prototype cannot reduce the whole indicator to zero merely because it is not yet mass-produced. It remains visible in its own native production or operation context.

The 30-day horizon makes the measure useful while the much larger opening reserve protects the country against immediate collapse. It does not create fuel, equipment or manpower. Countries observing the boss receive only the precision permitted by their actual intelligence, as specified in Part 10. Without intelligence they see the broad condition. The limiting component and the supply node behind it come from a live Reconnaissance receipt (Part 07), which is what turns the indicator into a target.
