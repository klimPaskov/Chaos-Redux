# Spec: Rework the Communism Spread Event into a State-Based Insurgency System

## Goal

Completely rework the current communism spread event into a dynamic, state-based communist insurgency system.

The old version should be removed or replaced. The new version should make communist influence feel like a growing internal territorial crisis rather than a simple national modifier. The player should see which states are under communist control, feel the economic and military damage from those states, and decide whether to contain the movement locally or risk a brutal nationwide emergency intervention.

## Core Design

The communism spread event should now create and maintain a national communist spread idea that only increases daily communism support.

Remove anything from the old design that gives weekly stability, weekly war support, or similar passive weekly effects.

The national idea should represent the overall growth of communist support inside the country. Its daily communism support gain should scale dynamically based on how many states are under communist control.

Each communist-controlled state adds +0.01 to the daily communism support tick.

Example:
- 0 controlled states: only the base national effect applies
- 3 controlled states: daily communism support is increased by base effect plus +0.03
- 10 controlled states: daily communism support is increased by base effect plus +0.10

The exact base value can be balanced by the agent, but it should be low enough that the system escalates through states first and national ideology second.

## State-Based Communist Control

Communist influence should now exist at the state level.

When communists gain control of a state, that state receives a visible state modifier and map highlight. The state should be outlined or otherwise highlighted to show that it is under communist influence.

The visual intensity should reflect control level:
- Level 1: light red outline or subtle red highlight
- Level 2: stronger red outline or darker red highlight
- Level 3: strongest red outline, visibly dangerous and permanent until emergency action

Use an existing three-stage state control structure if possible, similar in spirit to systems used by Norway or Sweden. The player should immediately understand that these are infected or occupied political zones.

## Control Levels

### Level 1: Agitation Zone

This is the first stage. The communists recently gained influence in the state.

Meaning:
- Local cells are forming
- Strikes and propaganda are spreading
- Police and local authorities are still able to act
- The state can still be recovered through regular military intervention

Effects should be noticeable but not crippling.

Suggested effects:
- Slight construction speed penalty
- Slight factory output penalty
- Small recruitable manpower penalty
- Small resistance or local unrest effect
- Minor supply or infrastructure disruption if appropriate

Gameplay role:
- Warning stage
- Cheap to handle if the player reacts early
- Low risk in emergency conversion

### Level 2: Insurgent Stronghold

This is the second stage. Communist cells have turned into organized local power structures.

Meaning:
- Militias operate openly
- Industry is raided and disrupted
- Local administration is compromised
- State recovery becomes harder and more expensive

Effects should be significantly stronger.

Suggested effects:
- Medium construction speed penalty
- Medium factory output penalty
- Stronger recruitable manpower penalty
- Higher local resistance or unrest
- Possible reduced local resources
- Possible reduced supply efficiency
- Possible periodic sabotage events

Gameplay role:
- Main pressure stage
- Player must decide whether to spend resources to contain it
- High risk in emergency conversion

### Level 3: Communist Lockdown

This is the final stage. The state is effectively lost to communist control.

Meaning:
- The communists have created a parallel local government
- Loyalist administration has collapsed
- Militias, unions, and revolutionary committees control the state
- Regular intervention can no longer remove communist control

Effects should be severe.

Suggested effects:
- Heavy construction speed penalty
- Heavy factory output penalty
- Heavy recruitable manpower penalty
- Severe local instability
- Industry disruption
- Possible blocked or heavily reduced state development
- Possible hostile militia presence in flavor events

Gameplay role:
- Permanent crisis state
- Cannot be cleared by normal state decisions
- Can only be addressed through the emergency national decision
- Always converts during the emergency civil war outcome
- Provides the strongest rebel force if civil war happens

## State Progression

Communist-controlled states should escalate over time if ignored.

A Level 1 state can become Level 2.

A Level 2 state can become Level 3.

Level 3 is locked until the emergency decision is taken.

The speed of escalation should depend on balance, but the system should avoid feeling fully random. The player should feel that inaction allows communists to consolidate control.

Possible factors that can increase escalation:
- Low stability
- High communism support
- War exhaustion
- Losing a war
- Low manpower
- High number of already controlled states
- Neighboring states already under communist control
- Major industry in the state
- High victory point value

Possible factors that can slow escalation:
- High stability
- Strong anti-communist laws or decisions
- Recent local military intervention
- Low national communism support
- High political power investment
- Strong internal security measures

## State Targeting Logic

The communists should not choose states fully at random.

They should prefer states that make sense politically and strategically.

Suggested target priority:
- Industrial states
- High population states
- High victory point states
- States neighboring existing communist-controlled states
- States with major supply hubs or infrastructure
- States with arms factories or civilian factories
- States in countries with rising communism support
- States in countries with low stability
- States in countries currently at war

This makes the crisis feel more intelligent. Communists should aim to disrupt the country, not simply paint random provinces red.

## Rework: "Communists Are Targeting Our Industry" Event

Completely rework the current industry targeting event.

The new version should represent communist cells moving beyond propaganda and into economic sabotage, factory intimidation, strike coordination, equipment theft, and attacks on state logistics.

This event should now be tied to communist-controlled states.

Possible event themes:
- Railway sabotage in a controlled state
- Militia raids on arms factories
- Red unions forcing factory shutdowns
- Revolutionary committees seizing local warehouses
- Communist sympathizers leaking production schedules
- Workers refusing orders from the central government
- Local administrators hiding equipment from the army
- Supply hubs being disrupted by strikes
- Factory managers requesting army protection

The event should feel different depending on control level.

Level 1 version:
- Mostly strikes, propaganda, intimidation
- Smaller damage
- Gives player a chance to react early

Level 2 version:
- Organized sabotage and raids
- Medium damage
- May worsen state control if ignored

Level 3 version:
- The state is no longer reliable
- Industry is effectively under revolutionary pressure
- Heavy damage or long-term state penalty
- Should reinforce that normal control has failed

The event should not be a generic national penalty anymore. It should point to a specific state and make the player care about that state.

## Regular Military Intervention Decisions

The existing military intervention decisions should become state-based decisions.

The player should be able to intervene in individual communist-controlled states.

Regular intervention should work only against Level 1 and Level 2 states.

Level 3 states cannot be recovered through normal intervention.

State intervention should cost meaningful resources.

Possible costs:
- Political power
- Command power
- Infantry equipment
- Manpower
- Stability
- Temporary state damage
- Temporary national tension
- Possible casualties

The cost should scale with the control level.

Level 1 intervention:
- Lower cost
- Higher chance of success
- Lower damage to the state
- Lower chance of backlash

Level 2 intervention:
- Higher cost
- Lower chance of success
- Higher chance of worsening local anger
- May reduce Level 2 to Level 1 instead of fully clearing it
- May fail and push the state closer to Level 3

Possible outcomes:
- Full success: communist control removed
- Partial success: state control reduced by one level
- Failure: no change
- Bad failure: control increases or a sabotage event fires
- Crackdown scandal: small national stability loss or communism support gain

The player should be rewarded for early action and punished for waiting.

## Emergency National Intervention Decision

Keep the emergency decision as a generic national decision, but completely rework its purpose.

This decision should affect all communist-controlled states at once.

It should be extreme, expensive, and risky.

Availability:
- Available if communists control at least 50% of the country’s states
- Also available if at least one state reaches Level 3

The decision should represent a nationwide military emergency:
- Martial law
- Mass arrests
- Army raids
- Factory occupation
- Forced disarmament of militias
- Suppression of revolutionary committees
- Emergency mobilization of loyalist forces

Costs should be severe.

Possible costs:
- Large manpower cost
- Large infantry equipment cost
- Political power cost
- Command power cost
- Stability loss
- War support loss
- Temporary national production disruption
- Possible temporary penalties to construction, output, or mobilization

This should feel like a desperate measure, not a normal optimization button.

## Emergency Decision Civil War Risk

The emergency decision should have a chance to trigger a communist uprising.

This must not use the normal HOI4 civil war logic where the country is split normally and equipment is shared.

Instead, if the uprising happens:
- Communist-controlled states may convert to a new communist rebel country
- The rebel country should receive its own name
- The rebel country should receive a communist leader
- Rebels should spawn their own divisions
- Rebels should not receive half of the original country’s equipment
- Rebel strength should be generated from the controlled states and the target country’s strength

The conversion chance should depend on each state’s control level.

State conversion chance:
- Level 1: 40%
- Level 2: 80%
- Level 3: 100%

Division spawning should also depend on state level.

Level 1 converted state:
- Lower chance to convert
- If converted, spawns fewer and weaker rebel divisions
- Represents scattered cells and rushed militias

Level 2 converted state:
- High chance to convert
- Spawns a moderate rebel force
- Represents organized revolutionary militias

Level 3 converted state:
- Always converts
- Spawns the strongest rebel force
- Represents a fully prepared revolutionary stronghold

## Rebel Strength Scaling

The rebellion should scale with the target country.

A small country with weak industry should not spawn an absurd number of rebels.

A major industrial country should face a dangerous uprising if many industrial states are communist-controlled.

Rebel strength should consider:
- Number of converted states
- Control level of each converted state
- Number of military factories in converted states
- Number of civilian factories in converted states
- State population
- Victory points
- Country industry size
- Country army size
- Country manpower pool
- National communism support
- Whether the country is at war

Suggested direction:
- Small countries get fewer rebel units
- Large industrial countries get more rebel units
- Level 3 industrial states should be especially dangerous
- Rebel divisions should be stronger if the state had high communist control
- Rebels should spawn with enough force to be a real threat, but not always an instant death sentence

## Emergency Decision Outcomes

If no uprising happens:
- Level 1 states should usually be cleared
- Level 2 states should usually be reduced or cleared
- Level 3 states should be reduced or cleared only through this decision
- The country should suffer heavy costs and temporary damage

If an uprising happens:
- Some communist states convert to the rebel country based on level chance
- Non-converted Level 1 and Level 2 states may be cleared or reduced
- Level 3 states always join the rebels
- The player fights the new communist rebel country
- The original country keeps its equipment stockpile
- Rebels receive spawned forces instead of inherited stockpiles

The emergency decision should be risky enough that the player may hesitate before clicking it.

## Map and UI Expectations

The player must be able to clearly identify communist-controlled states.

Every controlled state should be highlighted.

Level 1 should be visible but mild.

Level 2 should be clearly dangerous.

Level 3 should be the reddest and most alarming.

The UI should communicate:
- Which states are controlled
- What level each state is at
- What the penalties are
- Whether regular intervention is possible
- Whether only emergency intervention can solve the problem

The player should not need to guess why national communism support is rising. The controlled states should visually explain it.

## Gameplay Feel

The system should create a clear gameplay loop:

1. Communism begins spreading nationally.
2. Communists gain control of a state.
3. The state receives visible red influence and negative effects.
4. The state contributes +0.01 daily communism support.
5. The player can intervene locally.
6. Ignored states escalate to higher levels.
7. Level 3 states become locked revolutionary zones.
8. If enough states are controlled, or any state reaches Level 3, emergency intervention becomes available.
9. Emergency intervention can save the country or trigger a communist uprising.
10. If rebellion happens, the rebel country is created from converted communist states with spawned divisions.

The system should encourage early containment, punish neglect, and create memorable internal crises.

## Flavor Direction

Use grounded political crisis language.

Good tone:
- Revolutionary committees
- Local cells
- Red militias
- Factory seizures
- Coordinated strikes
- Army intervention
- Emergency powers
- Industrial sabotage
- Political collapse
- Loyalist administration
- Parallel authority
- Insurgent stronghold

Avoid making it too cartoonish. It should feel like a serious internal security crisis with clear gameplay consequences.

## Balance Direction

The system should be dangerous but manageable.

Early states should be annoying, not devastating.

A few ignored states should become a serious problem.

Many ignored states should threaten civil war.

Level 3 states should feel like a failure point.

Emergency intervention should be powerful, but its costs and civil war risk should make it a last resort.

Do not make the system instantly fatal. The player should have chances to react.

## Documentation and Tracking Requirements

Follow the event implementation skill.

Update every relevant file connected to this system.

This includes:
- Event files
- Decision files
- State modifier files
- Dynamic modifier files
- Idea files
- Localization files
- GUI or map highlight files if applicable
- Scripted effects
- Scripted triggers
- Scripted localization
- Balance notes
- Event log
- Any spreadsheet that tracks events, decisions, modifiers, or system status
- Any TODO, roadmap, or design document where this communism spread event is listed

Make sure the event log clearly records:
- The old communism spread event was replaced
- The national communism spread idea was simplified to daily communism support
- State-based communist control was added
- Three state control levels were added
- State-based military interventions were added
- Emergency national intervention was reworked
- Emergency civil war behavior was added
- Industry sabotage events were made state-based

## Cleanup Requirements

Remove or disable obsolete old behavior.

Specifically remove:
- Weekly stability effects from the communism spread idea
- Weekly war support effects from the communism spread idea
- Old generic industry disruption behavior
- Old generic military intervention decisions that are no longer state-based
- Any duplicate or conflicting version of the old communism spread event

Do not leave dead systems that still fire in the background.

## Acceptance Criteria

The rework is complete when:

- Communism spread uses a national dynamic idea focused only on daily communism support
- Each communist-controlled state increases the daily communism support tick by +0.01
- Communist control exists at state level
- Controlled states are visibly highlighted
- State control has three levels
- Each level has stronger negative state effects
- Level 3 states cannot be cleared by normal intervention
- Regular military intervention decisions are state-based
- Emergency intervention remains national and affects all controlled states
- Emergency intervention is only available at 50% controlled states or at least one Level 3 state
- Emergency intervention has severe costs
- Emergency intervention can trigger a custom communist uprising
- State conversion chance is 40% for Level 1, 80% for Level 2, and 100% for Level 3
- Rebel divisions spawn based on state level and country strength
- The uprising does not use normal equipment splitting
- The industry targeting events are state-based and tied to controlled states
- All relevant documentation, spreadsheets, and event logs are updated
- Old conflicting mechanics are removed

## Creative Additions to Consider

Add small narrative details that make the system feel alive.

Possible additions:
- Neighboring states are more likely to fall if one state is already communist-controlled
- Level 2 and Level 3 states can trigger local sabotage events
- Industrial states can suffer targeted factory raids
- High population states can generate more communist pressure
- Victory point states can create larger political shocks
- Failed local interventions can increase national communism support
- Successful interventions can create a temporary crackdown modifier that slows future spread in that state
- Level 3 states can occasionally issue propaganda events that increase communism support nationally
- Emergency intervention can create post-crackdown scars, such as temporary state recovery penalties
- If rebels win, the resulting communist country should feel like it came from the controlled states rather than from a generic civil war split

Keep the final implementation readable, modular, and easy to balance later.

## Pacing and Event Frequency

The system should not become too spammy.

There must be breathing room between events, state escalations, sabotage incidents, and intervention-related outcomes.

The communist insurgency should feel like a growing crisis, not constant pop-up spam.

Use pacing rules so that:
- Communist spread events do not fire too frequently
- Industry sabotage events have cooldowns
- State escalation has delays between stages
- The player has time to react before the next crisis appears
- Large countries do not get flooded with many communist state events at once
- Multiple state changes can be grouped or summarized when appropriate
- Important events still feel meaningful when they appear

The system should create pressure over time, not interrupt the player every few days.

## Communist Party Size and State Spread

The chance that a state becomes communist-controlled should depend strongly on the size of the communist party.

Higher communist support means communist cells have more public sympathy, more recruits, more local protection, and better access to unions, factories, and local administration.

However, even at very high communist support, the spread should still be gradual.

A country with 100% communist support should eventually be at risk of losing up to around 90% of its states to communist control if the player does nothing. This should not happen instantly. It should represent a long collapse of state authority.

Communist support should influence:
- How likely a new state is to fall under communist control
- How quickly existing communist states escalate
- How difficult local intervention becomes
- How likely sabotage events are
- How likely emergency intervention triggers an uprising
- How many rebels can be raised during the uprising

Communist support should not be the only factor.

State spread should also scale with:
- National stability
- War support
- Current war status
- Industrial strength
- Number of factories
- Number of already controlled states
- Number of Level 2 and Level 3 states
- State population
- State victory points
- Neighboring controlled states
- Whether the state is industrial, urban, or strategically important
- Whether the country is a minor, regional power, or major

A large country with many states should not suddenly get communist control in many random places at once. Spread should scale intelligently and slowly.

The more unstable and industrialized a country is, the more dangerous the movement becomes.

## Spread Ceiling and Long-Term Control

The system should have a soft ceiling based on communist support.

Example direction:
- Low communist support: only rare state control, mostly Level 1
- Medium communist support: several vulnerable states may fall over time
- High communist support: the movement becomes a major national crisis
- Very high communist support: communists may eventually control most of the country if not stopped
- 100% communist support: communists can eventually control around 90% of states

This should be a soft target, not an instant trigger.

The system should slowly move toward that pressure level over time if the player does nothing.

## Revolutionary War Event

If communist influence becomes strong enough, the country should face a chance of war even before the player clicks the emergency decision.

This should happen through an event.

Trigger direction:
- Communists control at least 50% of the country’s states
- Or communists control at least 2 Level 3 states

When this happens, an event should warn the player that communist forces are preparing open revolt.

Possible event framing:
- Red militias are openly mobilizing
- Revolutionary committees are coordinating across controlled states
- Loyalist police have lost access to several regions
- Factories are refusing central government orders
- Army officers warn that delay could lead to organized rebellion

The event should give the player choices.

Possible choices:
- Launch emergency intervention immediately
- Attempt negotiations or concessions
- Delay and monitor the situation
- Prepare loyalist forces
- Crack down on revolutionary networks

These options should have different costs and risks.

Do not make every option cost political power. Use more varied costs and consequences.

Possible costs and tradeoffs:
- Manpower losses
- Infantry equipment losses
- Command power
- Temporary factory disruption
- Stability loss
- War support loss
- Temporary construction penalties
- Temporary supply disruption
- Reduced mobilization speed
- Reduced recruitable population in affected states
- Army experience cost
- Loss of local resources
- Temporary consumer goods penalty
- Short-term reduction of communist escalation
- Long-term increase in communist anger
- Higher or lower civil war risk later

If the player refuses to act while communist control is high, the chance of a communist uprising should increase over time.

## Cost Design

Avoid making political power the default cost for every action.

Political power can be used sometimes, but the system should use varied costs that fit the action.

Examples:
- Military intervention should cost equipment, manpower, command power, and stability
- Industrial protection should cost factory output or temporary construction penalties
- Intelligence operations should cost command power, army experience, or temporary political consequences
- Local concessions should reduce state penalties but increase communist support
- Harsh crackdowns should reduce control but risk backlash
- Emergency intervention should cost a mix of manpower, equipment, stability, war support, and economic disruption

Costs should feel connected to what the player is doing.

A military crackdown should hurt the army and stability.

Factory protection should affect production.

Negotiations should affect ideology and future escalation.

Emergency intervention should feel like a national trauma.

## World Revolution Major Event Hook

This communism state-control system should be tied to the major event called World Revolution.

Do not fully integrate World Revolution yet.

For now, the communism spread system should only unlock the possibility for that major event to appear later.

As soon as the communism spread event fires, set a flag showing that World Revolution is now allowed to enter the major event pool.

This means:
- World Revolution should not fire directly from this communism spread event
- No full World Revolution event chain should be implemented yet
- No special global effects should be added yet
- No additional World Revolution mechanics should be created yet
- The communism spread event should only set the correct flag or condition so World Revolution can now fire through the normal major event system

Before the communism spread event fires, World Revolution should be locked out and should display as unavailable in the major event system.

After the communism spread event fires, World Revolution should no longer be locked at zero weight. Its weight can then begin increasing through the normal major event system.

## Major Event Weight Display

Also rework the major event weight display logic.

If an event cannot currently fire because its trigger conditions are not met, do not display its weight as `0`.

Instead, display `N/A` in red.

This is important because `0` should mean the event is unlocked, valid, and technically able to fire, but its current calculated weight is actually zero.

`N/A` should mean the event is locked by conditions and cannot fire at all right now.

Display rules:
- If the event is locked by trigger conditions: show red `N/A`
- If the event is unlocked but its calculated weight is actually 0: show `0`
- If the event is unlocked and has a positive weight: show the normal weight value
- Once World Revolution is unlocked by the communism spread event flag, stop showing `N/A` and show its real calculated weight

This should make the major event UI clearer and avoid misleading the player.

## Event Evolutions

The communism spread event should support the Chaos Redux evolution system, but evolutions should not radically change the core behavior of the system.

Evolutions should mainly make the crisis less predictable and more unstable.

They should add unusual event outcomes, rare surprise escalations, stranger worker-related incidents, and small changes to uprising strength.

Do not make evolutions turn the event into an instant country-killer. A weak country should still face a reasonable crisis. If a random state revolts, it should get a little more strength than normal, but not enough to instantly destroy the country unless the country was already collapsing.

## Evolution Structure

Use only 3 evolution stages.

The system does not need many evolution stages. A smaller number of meaningful evolutions is better.

Suggested structure:
- Base version: normal communist spread
- Evolution 1: unstable revolutionary activity
- Evolution 2: occult worker radicalization
- Evolution 3: ties with the world revolution event, whispers of a revolution, that lenin has been resurrected and is coming.

## Evolution 1: Unstable Revolutionary Activity

This evolution should make the system more unpredictable, but not massively stronger.

Theme:
The communist movement becomes harder to read. Some groups act without central coordination. Local cells may launch sudden uprisings, seize buildings, or provoke the army before the wider movement is ready.

New possible behavior:
- Rare chance for a random controlled state to suddenly declare itself revolutionary territory
- Rare chance for a Level 2 or Level 3 state to trigger a local armed revolt
- A revolting state may spawn slightly more divisions than normal
- Rebel divisions from this evolution may have slightly better organization or strength
- The revolt should still scale with the country and state strength
- Small countries should not be destroyed by absurd rebel spawns
- Stronger countries can face a more serious fight if industrial states revolt

This evolution should create surprise, not guaranteed disaster.

Possible strange events:
- A factory guard unit joins the revolutionaries
- A local militia declares the state liberated
- A red banner is raised over the state capital
- Revolutionary committees block army access to industrial districts
- A loyalist governor disappears before a crackdown can begin

## Evolution 2: Dark Worker Rituals

This evolution adds stranger Chaos Redux flavor.

Theme:
Some parts of the communist movement begin mixing revolutionary politics with dark mass rituals, cult-like worker gatherings, and disturbing factory symbolism.

This should be weird and unsettling, but it should not fully turn the system into a supernatural apocalypse unless another major event later does that.

The rituals can be ambiguous. Maybe they are psychological warfare. Maybe they are mass hysteria. Maybe something darker is happening.

New possible behavior:
- Rare strange worker events can fire in controlled industrial states
- Ritual events can slightly increase local control level pressure
- Ritual events can increase fear, reduce stability, or damage local production
- Some ritual events can make intervention riskier in that state
- A state affected by a ritual may be more likely to join a later uprising
- Effects should be limited and paced

Possible event ideas:
- Workers chant through the night inside a locked factory
- Machines keep running after the power is cut
- A foreman reports symbols painted in oil and blood
- A factory shift refuses to leave and calls itself the Red Choir
- Local police find burned production ledgers arranged in a circle
- A railway depot becomes the site of mass chanting
- Workers claim the factory has chosen the revolution
- A missing manager returns speaking only in slogans
- A night shift produces equipment that no one ordered
- Loyalist soldiers sent to disperse a crowd desert after hearing the chanting

Possible state effects:
- Temporary production disruption
- Temporary construction speed penalty
- Small local manpower penalty
- Higher chance of state escalation
- Higher chance of joining a revolutionary uprising
- Small chaos increase
- Small stability loss
- Small increase in communism support

Design rule:
These events should be rare enough to feel special.

They should add atmosphere and uncertainty. They should not replace the political state-control system.

## Evolution 3: Whispers of the World Revolution


Theme:
The communist crisis begins connecting to the World Revolution major event.

The movement is no longer only about local revolutionary cells. Rumors spread that something much larger is coming. Workers, soldiers, and party radicals whisper that Lenin has returned, or that he will soon return, to lead the final revolution.

This should feel strange, ideological, and threatening.

Do not fully integrate the World Revolution event yet. This evolution should only create atmosphere and strengthen the connection between the communism spread system and the World Revolution major event. This evolution should make the world revolution super event available now. If before it was unlocked by simply the event being fired, now it should unlock once the evolution stage 3 is reached (Chaos Tier).

New possible behavior:
- News events mention whispers of World Revolution
- Controlled states may spread rumors that Lenin has been resurrected
- Dark worker ritual events can reference Lenin’s return
- Revolutionary propaganda may claim that the old revolutionary spirit has physically returned
- Some communist-controlled states may become more unstable after these rumors spread
- The World Revolution major event can gain more weight through the normal major event system after the communism spread event has unlocked it
- Rare local breakaway events can frame themselves as the first spark of the coming World Revolution

Possible event ideas:
- Workers gather around a hidden portrait of Lenin and chant that he is coming
- A factory night shift claims they heard Lenin’s voice through the machines
- Red pamphlets appear across controlled states with the phrase: "He has returned"
- Local communist leaders deny the rumors in public, but their followers begin acting with new confidence
- A captured revolutionary says the uprising is only preparation for Lenin’s arrival
- Soldiers report hearing crowds chanting Lenin’s name before a crackdown begins
- A Level 3 state declares itself the first territory of the coming World Revolution
- A railway depot is covered in red symbols and slogans about the resurrected leader

Possible effects:
- Small chaos increase
- Small national stability loss
- Slight increase in communist support
- Slightly higher chance for controlled states to escalate
- Slightly higher chance for Level 3 states to join a later uprising
- Slightly stronger rebel divisions if a breakaway crisis happens
- Increased World Revolution major event weight through the normal major event system

Design rule:
This evolution should foreshadow World Revolution, not launch it. Each news event about the world revolution coming should increase the weight of the world revolution major event by 200.

Lenin’s resurrection should be presented as rumor, propaganda, mass hysteria, or something possibly darker.

The player should feel that the communist crisis has started pointing toward a much larger event.

## Evolution Pacing

Evolved events need cooldowns.

The strange events should feel rare.

Do not allow worker ritual events or sudden state revolts to fire constantly.

Suggested pacing:
- Strange worker ritual events should be occasional
- Surprise state revolts should be rare
- Breakaway crises should be very rare
- A country should not get multiple surprise breakaways in a short time
- Large countries can have more activity, but still need breathing room
- Repeated strange events should be logged and spaced out

## Event Log and Evolution Tab Requirements

The event log and evolutions tab should explain the evolution in player-facing language.

The player should see that the communism spread event has evolved, but the description should focus on instability and unpredictability rather than raw power.

Example evolution text:

"Communist activity has become harder to predict. Local cells may now act without central direction, and controlled states can produce sudden revolutionary incidents."

Example dark ritual evolution text:

"Reports from controlled industrial states describe strange worker gatherings, night-shift chants, and factory rituals. The movement is no longer only political."

The log should record:
- Which evolution stage is active
- What unlocked it
- What new rare events are now possible
- Whether sudden state revolts are possible
- Whether dark worker ritual events are possible
- Whether breakaway crises are possible

## World Revolution State Integration

When the World Revolution major event eventually fires, it should use the communist state-control system as its main territorial basis.

The World Revolution should no longer simply calculate communist party popularity and randomly choose states.

Instead, it should prioritize the states that are already under communist control from the communism spread system.

This means:
- Level 1 communist-controlled states can join the World Revolution, but with lower strength
- Level 2 communist-controlled states are much more likely to join and should spawn stronger forces
- Level 3 communist-controlled states should almost always join and should provide the strongest revolutionary forces
- States not under communist control should not be the main basis of the World Revolution

If communist rebel states already exist as their own country before World Revolution fires, then the World Revolution should annex or absorb those rebel countries.

When absorbing an existing communist rebel country:
- Keep its existing divisions
- Keep its controlled territory
- Transfer it cleanly into the World Revolution country
- Do not delete its army and recreate everything from nothing
- Do not treat it as a normal random civil war split

If the communist rebels are still only represented through controlled states, then the World Revolution country should spawn from those controlled states.

Division spawning should scale by control level:
- Level 1 states spawn fewer revolutionary divisions
- Level 2 states spawn a moderate number of better revolutionary divisions
- Level 3 states spawn the strongest revolutionary divisions
- Industrial states should support stronger spawns
- High-population states should support stronger spawns
- Weak countries should still receive reasonable rebel strength, not absurd rebel stacks

The World Revolution should feel like it is emerging from the communist-controlled territory that already existed on the map.

When The World Revolution happens, then communist insurgency system is then disabled for every country

The player should understand that ignoring communist state control earlier helped create the World Revolution later.