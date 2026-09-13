# Event 064 Border Fortifications

## Part 3: Response postures, decisions, missions, and AI

## Local response purpose

The automatic fortification wave changes the map without asking permission. The local response system determines whether a country can turn those structures into a working defense, keep them supplied, or learn how to cross the equally strong lines abroad.

The response layer should remain compact. A normal decision category with one static picture is the complete player surface for the current posture, response-window deadline, active project, and valid target actions.

The response system opens only after the global construction transaction has completed and the country result is known.

## Working-label rule

Every posture, decision, mission, modifier, and internal route label in this part is a working label, not final localisation. The implementation agent writes final player-facing text from the stated direction.

## Response report

A country with at least one local Event 064 construction result chooses one of three postures in its report:

- `Integrate the Line`
- `Keep the Roads Open`
- `Study the Breach`

The three options are mutually exclusive for the current response window.

A country with no local fortification result can choose `Study the Breach` when it has a plausible foreign land-war target. Otherwise it receives an observational acknowledgement and no persistent category.

The report option applies the posture only. It does not own the automatic construction.

### Posture duration

Starting anchor: `180` days.

A posture lasts until its response window expires or a later Event 064 report replaces it. Older posture modifiers and flags are removed before the new posture is applied. A country can never hold several Event 064 postures at once.

An active project already started under the old posture can finish after a new wave when its target remains valid. It does not grant access to new projects from the old posture.

## Posture 1: Integrate the Line

### Narrative role

The government treats the sudden defenses as a usable national system. Engineers survey sectors, commands assign garrisons, observation posts are connected, and local commanders learn which positions support one another.

### Mechanical role

The posture improves the country's ability to defend through existing forts. Use current valid modifiers that support fort defense, entrenchment, fort repair, planning on prepared ground, or another verified defensive effect. Do not invent unsupported province-combat syntax.

The effect should be noticeable and temporary. It should not make unfortified offensive divisions stronger everywhere.

### Main project access

Unlock `Reinforce a Priority Sector`.

### Preferred users

- countries at war on their land frontier
- countries weaker than a neighboring enemy
- countries with a threatened capital or core border state
- countries with adequate equipment and manpower to occupy the line
- countries whose supply network is already usable

### Tradeoff

The posture gives less offensive help against foreign fort lines. Its local project consumes equipment, manpower, and civilian industrial capacity that could support field forces.

## Posture 2: Keep the Roads Open

### Narrative role

The government focuses on the network behind the concrete. Roads, rail links, depots, transport units, communications, and repair crews become the priority.

### Mechanical role

The posture improves the use and repair of supply and transport in fortified sectors. Valid effects can include lower supply consumption, faster infrastructure or railway repair, improved transport reliability, lower attrition in supplied defensive areas, or another verified logistics modifier.

The effect should help a country sustain the line. It should not grant a broad free industrial boom.

### Main project access

Unlock `Connect the New Line`.

### Preferred users

- countries with long frontiers
- countries with poor border infrastructure
- countries suffering supply penalties
- countries with enough trains and trucks to support a program
- countries preparing to hold several sectors

### Tradeoff

The posture spends transport stockpiles and civilian capacity. It gives less direct fort-combat power than Integrate the Line and less offensive counterplay than Study the Breach.

## Posture 3: Study the Breach

### Narrative role

The country treats the global fortification wave as an offensive problem. Engineers, artillery officers, air planners, and staff colleges study weak points, obstacle clearance, concentrated fire, and the timing needed to break a fortified sector.

### Mechanical role

The posture improves attacks against land forts through current valid modifiers. It can also improve planning speed, engineer support, obstacle clearance, or another verified offensive preparation effect.

The benefit should be strongest when fighting through real fort lines. It should not become a general permanent army attack bonus.

### Main project access

Unlock `Conduct Breach Exercises`.

### Preferred users

- countries planning an offensive against a fortified land neighbor
- countries already attacking through level three or higher forts
- countries with sufficient Army Experience, support equipment, and fuel
- countries with engineers or artillery capacity
- land-borderless countries that intend to invade a continental target

### Tradeoff

The posture gives less help holding local positions. Its project consumes experience, support equipment, fuel, and command resources before the offensive begins.

## Response category presentation

Use an ordinary decision category as the complete response surface.

The category should show:

- a static category picture
- the current posture in qualitative text
- the response-window expiry or remaining duration
- the highest concrete Event 064 evolution available to this country
- the currently active project, if any
- a concise summary of why no target is available when the category remains visible

The category should not show:

- hidden strategic scores
- raw candidate arrays
- cluster roll percentages
- exact evolution maturation rolls
- a world province list

### Visibility

Show the category when at least one of these is true:

- the country has an active Event 064 response posture
- the response window remains open and at least one project has a valid target
- an Event 064 project is active
- an achievement challenge tied to the current response must remain visible through a mission

Hide the category after every related posture, project, mission, and challenge display has ended.

### Active-project cap

A country can run one Event 064 sector project at a time. This cap applies across all five project families.

The cap prevents the event from becoming a construction menu and keeps the material costs meaningful. A country can complete several projects during one response window only when durations and remaining time permit it.

## Project family 1: Reinforce a Priority Sector

### Access

- current posture is Integrate the Line
- response window is open
- country has at least one valid affected border state
- no Event 064 sector project is active

### Target

One controlled border state with at least one direct frontier province below the active strategic cap.

Target priority for the player map marker should consider current war, enemy strength, capital access, existing fort levels, and state value. Every valid state can remain selectable when the targeted-decision interface supports it cleanly.

### Duration

Starting band: `45` to `75` days.

Increase duration for a long state frontier, low infrastructure, severe damage, weak industry, or a large target package. Reduce it for a compact state, high infrastructure, strong industry, or a country already using the logistics posture from an immediately prior wave.

### Concrete costs

Use no more than four spendable types in one action.

Preferred cost bundle:

- temporary civilian factory commitment
- infantry equipment
- support equipment
- manpower assigned to engineers and garrisons

Political power is not the default cost. Command Power can replace manpower in a verified balance variant, but do not add it as a fifth cost.

### Result

- add one land-fort level to a bounded set of qualifying direct frontier or anchor provinces in the selected state
- obey the current role caps and the one-extra-project-package-per-state-per-wave limit
- do not add a level to every land province in the state
- mark the selected state as reinforced for the current wave
- update the local Event 064 decision history

### Failure and cancellation

Cancel or fail when:

- the country loses control of the target state
- the state stops containing any current foreign land frontier before completion
- the country is annexed or capitulates under a rule that ends active domestic projects
- a hard map change removes every valid building target

Consumed equipment and elapsed civilian effort are not fully refunded. A partial refund can apply when the project ends very early through a map change outside the country's control.

### AI use

AI prefers the state that protects its capital, contains an active enemy front, has the weakest relevant fort levels, or blocks the strongest hostile neighbor. It should not reinforce an allied colonial border while its capital front is open.

## Project family 2: Connect the New Line

### Access

- current posture is Keep the Roads Open
- response window is open
- country has a valid affected border or evolved defense state
- no Event 064 sector project is active

### Target

One controlled state whose Event 064 defenses are strategically useful and whose transport or supply support can materially improve.

Valid target roles include:

- low infrastructure border state
- damaged infrastructure or railway state
- state containing a supply hub with a weak connection to the frontier
- selected Fortress State
- internal redoubt state under Fortress World

### Duration

Starting band: `60` to `100` days.

Increase duration with low infrastructure, long distance from the capital network, severe damage, or a broad state package. Reduce it for an existing developed network and strong civilian capacity.

### Concrete costs

Preferred cost bundle:

- temporary civilian factory commitment
- trains
- trucks
- support equipment

Use dynamic stockpile floors so a minor does not lose every train or truck. Costs scale with the target's current network gap and country capacity.

### Result priority

1. repair or strengthen an existing damaged infrastructure or railway connection when a safe effect exists
2. add one infrastructure level to the selected state below its cap
3. improve a verified existing railway segment that directly supports the state
4. add a bounded local supply benefit for the posture duration when a physical route change cannot be represented safely

The ordinary project does not create a new supply hub. A rare hub construction route can exist only under Evolution II or III after a separate implementation audit proves valid targeting, cost, and balance.

### Failure and cancellation

Cancel or fail when the country loses the state, the route becomes invalid, the country is annexed, or every planned physical change becomes impossible.

Spent trains and trucks represent reassigned or lost transport and are not fully refunded. Avoid creating negative stockpiles.

### AI use

AI chooses the most important state with the worst current supply support, then checks whether it can pay without compromising minimum train and truck reserves. It should skip the project when its army already has critical transport shortages.

## Project family 3: Conduct Breach Exercises

### Access

- current posture is Study the Breach
- response window is open
- the country has a valid fortified foreign land-war target or a plausible prepared target
- no Event 064 sector project is active

A land-borderless country can use this project when it has a war, war goal, claim route, naval access plan, or current strategic target that can lead to land combat against fortified territory.

### Target

Prefer one foreign country and one relevant frontier or objective state. The target must contain or be protected by a meaningful fort line.

A valid target can be:

- current enemy sharing a land frontier
- likely offensive target with current war goal or claim preparation
- enemy reached through an allied front
- continental enemy expected after a naval landing, when the country has a real invasion route

Do not let the player choose a harmless minor with no forts merely to obtain a general attack bonus.

### Duration

Starting band: `45` to `75` days.

Increase duration for higher target fort levels, poor doctrine, missing engineers, low planning capacity, or weak fuel. Reduce it for relevant doctrine, engineer support, accumulated Army Experience, and recent combat against forts.

### Concrete costs

Preferred cost bundle:

- Army Experience
- support equipment
- fuel
- Command Power

A lower-cost minor variant can omit Command Power or reduce fuel. Never use more than four spendable types.

### Result

Grant a target-bound or tightly scoped temporary preparation package that improves attacks against land forts and the chosen target. Use valid current modifiers and target strategy where possible.

The reward can include:

- fort attack effectiveness
- planning speed
- engineer or obstacle-clearance effectiveness
- a temporary target-country attack plan
- faster adaptation after initial fortified combat

The reward should last long enough to support one planned operation, with a starting band of `90` to `150` days. It ends early if the target ceases to exist or becomes an ally under a verified cleanup rule.

### Failure and cancellation

The preparation can complete even if war has not started. It fails only when the target becomes invalid, the country loses the ability to conduct normal land warfare, or the country is annexed.

Do not refund consumed Army Experience after the staff work has begun.

### AI use

AI uses this project when it has an active or planned offensive against a fortified target and enough fuel, support equipment, and Army Experience to preserve operational reserves. It should not choose it while losing its capital front unless an immediate counteroffensive is plausible.

## Project family 4: Harden the Air and Coastal Flank

### Access

- Evolution II Fortress States has concretely materialized for the country or a valid current wave has selected at least one Fortress State
- response window is open
- no Event 064 sector project is active
- at least one selected state has a valid air-defense or coastal role

This project can be used under any posture. Integrate the Line receives a defensive cost or duration advantage. Keep the Roads Open receives a logistics advantage. Study the Breach receives no discount unless the target is a forward offensive base.

### Target and branch

The player selects one valid state. The project resolves one of two visible branches based on the target role.

#### Air-defense branch

Use for a selected state with important industry, airbase, supply hub, capital approach, missile site, nuclear site, or enemy air threat.

Possible result:

- one state anti-air level
- one radar level when the state has a valid warning role and is below cap
- a temporary air-defense coordination modifier

The result should use at most two physical building additions in one project.

#### Coastal branch

Use for a selected coastal border state with a port, naval base, supply role, or exposed landing approach.

Possible result:

- one coastal-fort level at the port or highest-value landing approach
- one radar or state anti-air level according to threat
- a temporary coastal-defense coordination modifier

The project does not fortify the entire coastline.

### Duration

Starting band: `60` to `100` days.

### Concrete costs

Air-defense bundle can use:

- temporary civilian factory commitment
- anti-air equipment or another verified air-defense equipment stockpile
- Air Experience
- support equipment

Coastal bundle can use:

- temporary civilian factory commitment
- convoys
- Navy Experience
- support equipment

The action selects one bundle. It never charges both Air Experience and Navy Experience for one state.

### AI use

AI selects the air branch when enemy air pressure, strategic sites, or industry justify it. It selects the coastal branch when the state contains an important port and the country faces a credible naval invasion threat. It skips the project when the state already meets the active caps.

## Project family 5: Prepare a National Redoubt

### Access

- Evolution III Fortress World has concretely materialized for the country or the current wave created a valid internal redoubt
- response window is open
- no Event 064 sector project is active
- the country has not completed another National Redoubt project during this wave

### Target

One valid capital, capital approach, major victory point, supply hub, industrial center, major port, or strategic internal site.

The capital or capital approach receives the default priority. The player can choose another valid redoubt when the target interface makes the strategic tradeoff clear.

### Duration

Starting band: `90` to `140` days.

A country with weak civilian industry can receive a longer affordable route that fits its actual capacity.

### Concrete costs

Preferred bundle:

- temporary civilian factory commitment
- trains
- support equipment
- manpower assigned to engineering and garrison work

A state with no transport role can replace trains with infantry equipment. Use one bundle with no more than four spend types.

### Result

- add one land-fort level to the selected redoubt or a bounded approach position
- obey the internal-redoubt cap
- add one supporting infrastructure, anti-air, or radar improvement only when the target's role clearly supports it and the package stays within the project's balance budget
- mark the country as having used its one redoubt project for the wave
- update any active Last Redoubt achievement challenge

The player project does not create a ring around every capital province.

### AI use

AI gives high priority to this project when the capital is threatened, core victory-point control is falling, the country is fighting a stronger enemy, or its current capital has one exposed land approach. It gives low priority during secure offensive wars far from the homeland.

## Dynamic cost model

Costs should scale with the work being ordered and the country's ability to pay.

### Cost factors

Use combinations of:

- number of qualifying target provinces
- current relevant building levels
- missing infrastructure or supply support
- country civilian factory count
- country total industry
- country manpower pool
- equipment stockpile and recent deficit
- train, truck, convoy, and fuel reserves
- relevant experience pool
- current war state
- target state infrastructure
- target state damage
- current Chaos tier
- repeated Event 064 project history in the same state

### Affordability rules

- Preserve minimum train, truck, convoy, and fuel reserves.
- Do not consume more equipment than exists.
- Give tiny countries minimum viable projects with smaller scope and longer duration.
- Make large countries pay more for a large selected sector, but cap the scale so a project remains usable.
- Do not make political power the universal substitute for material shortages.
- Do not hide a cost in localisation after the decision is available.
- Do not charge a resource whose gameplay system the actor does not use.

### Starting quantity bands

These values are planning anchors and must be tuned against the live economy.

| Project | Small-country band | Large-country band |
| --- | --- | --- |
| Reinforce Priority Sector | 250 to 500 infantry equipment, 40 to 100 support equipment, 1 to 2 civilian factories, 1,000 to 4,000 manpower | 750 to 1,500 infantry equipment, 150 to 300 support equipment, 3 to 5 civilian factories, 8,000 to 20,000 manpower |
| Connect New Line | 10 to 20 trains, 100 to 300 trucks, 40 to 100 support equipment, 1 to 2 civilian factories | 30 to 70 trains, 500 to 1,200 trucks, 150 to 300 support equipment, 3 to 6 civilian factories |
| Conduct Breach Exercises | 10 to 20 Army Experience, 40 to 100 support equipment, bounded fuel commitment, 10 to 25 Command Power | 20 to 40 Army Experience, 100 to 250 support equipment, larger bounded fuel commitment, 20 to 40 Command Power |
| Harden Air or Coastal Flank | 1 to 2 civilian factories, small equipment or convoy bundle, 5 to 15 relevant experience, 30 to 80 support equipment | 3 to 6 civilian factories, larger equipment or convoy bundle, 15 to 30 relevant experience, 100 to 250 support equipment |
| Prepare National Redoubt | 2 to 3 civilian factories, 10 to 25 trains or equivalent equipment, 50 to 150 support equipment, 2,000 to 6,000 manpower | 4 to 8 civilian factories, 30 to 80 trains or equivalent equipment, 200 to 500 support equipment, 10,000 to 30,000 manpower |

Do not copy these bands into final code without reviewing current stockpile scales and existing decision precedents.

## Mission behavior

Each sector project should use a timed mission or a timed decision pattern that makes its duration visible.

The player needs to know:

- target
- time remaining
- costs already committed
- public result
- current failure condition

Project completion applies the physical result once. Save and reload must not restart the timer or repeat the reward.

### Target loss

When target control changes:

- fail a domestic construction project if the country no longer controls the state
- end a target-country breach preparation if the target disappears or becomes invalid
- keep a completed physical building in the state after later transfer
- remove stale map markers and target flags
- do not transfer an active domestic project to the new controller

### Annexation and capitulation

- Annexation ends all active Event 064 postures and projects for the dead country.
- Capitulation can fail domestic projects when the target state is lost or the country's normal domestic project contract ends.
- A government that survives with valid territory can retain a breach preparation against an enemy if its owner contract permits it.
- A released successor does not inherit the former controller's temporary posture or active project unless the accepted country-transfer framework explicitly supports that case.

## Exploit controls

The response system must close these abuse paths:

- repeated report option selection
- posture stacking across waves
- starting several state projects at once
- selecting a state already at every relevant cap
- switching posture to collect several temporary modifiers
- cancelling immediately for a full material refund
- target transfer used to duplicate a completed reward
- reloading to reroll a physical project result
- using an unfortified target for a general breach bonus
- tiny target chosen to gain a large country-wide offensive modifier
- repeated National Redoubt construction in one wave
- repeated project construction in the same state during one wave
- negative stockpiles created by dynamic costs
- AI spending its last trains, trucks, convoys, support equipment, or fuel
- debug or manual firing unlocking achievements

Use stable incident and project tokens, one-time completion flags, active-project caps, target validation, stored costs, and cleanup effects.

## AI posture selection

AI selection happens after the country result is known. It uses full option weights and explicit invalid-state gates.

### Integrate the Line score increases when

- the country is in a defensive war
- an enemy controls an adjacent state
- the capital lies near a hostile frontier
- the country is weaker than one or more land enemies
- stability or war support is low and a defensive stance is plausible
- local fort coverage improved materially
- supply is adequate
- equipment and manpower reserves can support garrisons
- Military Preparation cluster context emphasizes defense

### Keep the Roads Open score increases when

- the country has a long frontier
- border infrastructure is poor or damaged
- the army is suffering supply problems
- the country has several selected Fortress States or redoubts
- train and truck reserves are healthy enough to invest
- the country is a large continental power
- the current war requires sustained defense across several sectors

### Study the Breach score increases when

- the country has an active offensive plan
- a current or likely enemy has level three or higher forts
- the country has a land war goal, claim route, or active invasion plan
- Army Experience, support equipment, and fuel are available
- engineer, artillery, or air-support capacity is strong
- the country has little local frontier to defend
- the country is winning and expects to advance

### Invalid or near-zero choices

- Integrate the Line is invalid when the country has no local fortification result and no local redoubt.
- Keep the Roads Open is invalid when the country has no affected state or valid network target.
- Study the Breach is invalid when no meaningful fortified foreign target can be identified.
- A special actor without normal stockpile or decision systems skips postures that rely on those systems.
- A tiny country with no affordable project can still receive a modest posture effect, but its AI should not start a project that breaks reserve floors.

### Tie handling

When two postures have similar final scores, use bounded random variation. This preserves replay without allowing a weak random roll to override an obvious capital emergency.

The implementation must define a dominant-condition floor. A country whose capital is under direct attack should almost never choose a remote logistics project or a speculative offensive study unless its survival logic proves a counteroffensive is the best available action.

## AI project selection

After selecting a posture, AI decides whether to start its main project and whether to use evolved general projects.

### General project gate

AI starts a project only when:

- one valid target exists
- the result changes a building or grants a valid target-bound preparation
- reserve floors remain intact
- the country can sustain the civilian commitment
- the project can plausibly complete before target loss
- no more urgent country-specific crisis owns the same scarce resources

### Target ranking

Use the following order as a starting model:

1. capital survival
2. active hostile front
3. major supply route
4. major victory point or industrial center
5. critical port or air-defense sector
6. strongest likely offensive target
7. allied or neutral frontier with long-term strategic value

The exact order changes by posture and project.

### AI restraint

AI can skip a project. The response system should not force every country to spend resources after every global wave.

Common skip reasons:

- no valid target below cap
- critical equipment deficit
- critical train or truck shortage
- low fuel
- very weak civilian industry
- target expected to fall before completion
- current project from an earlier wave
- special actor contract
- no meaningful fortified opponent

## Probability audit contract

The final option and target weights cannot be accepted through source reading alone.

During implementation, spawn `chaosx_ai_probability_auditor` with `fork_context=false`. Give it the complete Event 064 option blocks, project AI blocks, target pools, country scenarios, external modifiers, and required acceptance ranges.

The audit must cover:

- posture selection after no local construction
- posture selection in a defensive capital emergency
- posture selection in a supply crisis
- posture selection before a planned fortified offensive
- minor-country affordability
- major-country affordability
- island-country behavior
- subject and overlord behavior
- civil-war behavior
- special Chaos actor behavior
- cluster-context modifiers
- target-state ranking
- target-country ranking for breach preparation
- repeated-wave behavior
- invalid target cleanup

Use the probability inspection and evaluation toolchain required by the project when available. Do not claim exact probabilities from guessed factor multiplication.

## Human clarity and choice quality

The three postures should create clear strategic differences.

A choice fails when:

- one posture is best for almost every country
- a posture's public text hides its material tradeoff
- a decision only converts political power into a building
- the defensive and logistics postures produce the same practical result
- the offensive posture gives a broad attack bonus unrelated to forts
- a project changes no physical or target-bound state
- the player cannot tell why a target is invalid
- the category shows every state as a separate cluttered list item
- an island player sees defensive options with no local use

The decision category should feel useful for one response period, then close cleanly.

## Response system completion standard

The response system is complete only when:

- physical fortification occurs before posture selection
- every human country receives only valid report options
- every AI country uses the same posture model
- posture variants are mutually exclusive and replace older variants
- posture duration is visible
- the category uses a normal decision surface with a static picture
- at most one Event 064 sector project is active per country
- project targets are bounded and understandable
- concrete costs use no more than four spendable types per action
- small and large country costs scale without breaking reserve floors
- project timers persist through save and reload
- completion rewards apply once
- target loss, annexation, capitulation, and invalidation clean up safely
- no project exceeds building caps
- no response action creates a fort carpet
- offensive counterplay is useful against real fort lines
- AI can skip unaffordable or pointless work
- the mandatory probability audit covers every listed scenario
- every decision, mission, modifier, map marker, tooltip, icon, and history entry has final localisation and asset coverage
