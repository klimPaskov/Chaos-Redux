# Event 059: The Offensive

## Part 3: Evolutions and pacing

## Evolution structure

The Offensive has three evolutions. Each one occupies one Chaos tier and adds a distinct AI behavior layer.

| Evolution | Chaos requirement | Main change |
| --- | ---: | --- |
| Evolution I: Relentless Offensives | 200+ | Longer pressure, stronger follow-up, greater operational commitment |
| Evolution II: Predatory Powers | 400+ | More aggressive use of claims, war goals, intervention, and weak-neighbor opportunities |
| Evolution III: Total Offensive | 600+ | Larger operations, higher accepted strategic risk, more ambitious theater plans |

Evolution state does not add Chaos. Chaos changes only through the first global manifestation and through ordinary shared systems that measure later wars, casualties, annexations, faction changes, and other consequences.

## Entry paths

Every evolution supports two entry paths.

### Active-event evolution

The event has already fired. Once the Chaos requirement is met and the evolution is enabled, the evolution enters an MTTH process. When it activates, its AI layer begins working immediately for every AI-controlled eligible country. The source event does not fire again.

Human-controlled countries remain unaffected. A country returned to AI control later receives all active layers.

### Pre-fire evolved opening

The event first fires after one or more evolution thresholds have already been reached. Every enabled evolution whose threshold is already satisfied activates as part of the opening package.

The opening uses one player-facing global report. The event history records the source event once. The evolution history records each enabled evolution in stage order on the firing date. This avoids three consecutive global popups while preserving complete evolution records.

A disabled evolution is skipped. A higher enabled evolution can activate without a lower disabled evolution, but it provides only its own behavior.

## Evolution toggle behavior

Evolution controls gate whether an evolution can activate.

- a disabled evolution does not enter MTTH
- a disabled evolution is not included in a pre-fire evolved opening
- a disabled evolution does not log a milestone or set its recorded state
- re-enabling an unactivated evolution after its threshold begins the normal active-event MTTH process
- disabling an evolution after it has already activated does not roll back campaign history or remove its fired milestone

The last rule protects save stability and avoids rapid strategic changes from settings toggles. The shared evolution UI should distinguish enabled status from already activated history.

## Evolution I: Relentless Offensives

### Chaos requirement

`200+`

### Strategic role

Relentless Offensives deepens conduct inside current wars. It does not create the predatory peacetime behavior assigned to Evolution II.

AI countries become more willing to sustain a promising operation through its full cycle. They commit follow-up forces, repair supply, move air support, reinforce landings, and keep pressure on an enemy whose line remains unstable.

### Immediate active-event changes

When the evolution activates, every current AI country should reassess active fronts and operations. It should:

- reduce avoidable delay before launching a prepared attack
- concentrate more reserves behind priority sectors
- reinforce successful attacks more quickly
- maintain offensive pressure after the first territorial gains
- continue toward nearby supply, port, rail, and victory-point objectives when feasible
- place greater production emphasis on replacement flow, artillery, logistics, mobile forces, and air support needed by active operations
- keep viable naval landings supplied and reinforced
- shorten recovery from a failed operation after the plan has materially changed

The evolution should not cause repeated unsupported attacks against the same fortified sector.

### Persistence model

A Relentless operation continues while all of these remain broadly true:

- supply stays inside the safe band
- replacement losses remain supportable
- the operation retains a useful objective
- reserves can answer another critical front
- the enemy has not established a much stronger line
- weather and terrain have not made the operation materially worse
- the homeland is not under a more urgent threat

Pressure falls when these conditions deteriorate. The AI should pause, reorganize, repair supply, move the axis, or end the operation.

### Country scaling

- majors can sustain several linked phases of one large operation
- regional powers should sustain one main operation and a limited supporting action
- minors should keep pressure on one attainable axis
- maritime powers should reinforce a successful landing rather than scatter new landings
- weak or exhausted countries should use the evolution chiefly to concentrate and recover, not to attack without resources

### Active-event pacing target

The base MTTH target is 90 days after reaching 200 Chaos.

Suggested pacing bands:

| Campaign state | Target pacing |
| --- | --- |
| 200 to 299 Chaos | about 90 days |
| 300 to 399 Chaos | about 75 days |
| 400+ Chaos | about 60 days |

The process can become somewhat faster when several major wars are active and somewhat slower when the world is largely at peace. The implementation must use existing bounded world-state information or native event factors. It must not add a new global scan merely to estimate stagnation.

### Evolution log direction

The evolution record should communicate that attack plans no longer end after the first failed push or limited gain. It should focus on continuing pressure, reinforcement, supply preparation, and commanders being ordered to finish operational objectives.

## Evolution II: Predatory Powers

### Chaos requirement

`400+`

### Strategic role

Predatory Powers changes strategic and diplomatic opportunity use. AI governments become more willing to act against exposed rivals, use available claims and war goals, answer useful calls to arms, intervene in favorable conflicts, and open another war when the opportunity is strong and their capacity permits it.

This evolution is the main boundary between an offensive military doctrine and a more dangerous international order.

### Immediate active-event changes

When the evolution activates, every current AI country should reassess valid strategic opportunities. It should:

- give more weight to active claims, cores, war goals, and scripted expansion objectives
- identify weak, isolated, distracted, or overextended rivals connected to those objectives
- consider joining faction or allied wars that protect its position or weaken a major rival
- use calls to arms more decisively when participation is feasible
- consider limited intervention where the country's route, faction, ideology, or regional interests support it
- exploit a target already committed to another war when opening the new front is strategically sustainable
- value ports, resources, industrial regions, border security, and strategic corridors inside valid objectives

### Validity boundary

The evolution must not:

- invent arbitrary claims
- bypass war-goal or diplomatic rules
- break subject restrictions
- ignore non-aggression or guarantee consequences
- attack a distant weak country with no route connection or strategic reason
- open another war when the country cannot protect its homeland or supply the new front
- override an event or focus route that explicitly forbids the action

Weakness alone is not a sufficient target reason. The target must be connected to a valid legal, strategic, factional, ideological, or event-owned interest.

### Opportunity score

The opportunity score should rise with:

- an existing claim, core, or war goal
- a target already fighting a costly war
- target isolation or weak likely support
- favorable comparative strength
- a short and supplyable border or sea route
- strategic value of the objective
- support from allies or faction members
- a chance to protect an ally or prevent a rival victory
- recent intelligence showing exposed forces or depleted stockpiles

It should fall with:

- several demanding existing wars
- severe replacement, manpower, fuel, or supply pressure
- strong expected intervention against the attacker
- a long or impractical route
- an exposed homeland
- an enemy alliance much stronger than the apparent target
- a country route that values neutrality, consolidation, or another explicit restraint

### Additional-war budget

The evolution should allow opportunistic war without creating unrestricted war stacking.

A minor usually has no capacity for another independent war while fighting a serious conflict. A regional power can consider one additional limited opportunity. A major can consider more than one theater when the existing wars are supportable, but the expected enemy coalition and homeland risk remain part of the decision.

Evolution III can raise this budget. It cannot remove it.

### Active-event pacing target

The base MTTH target is 105 days after reaching 400 Chaos.

Suggested pacing bands:

| Campaign state | Target pacing |
| --- | --- |
| 400 to 499 Chaos | about 105 days |
| 500 to 599 Chaos | about 85 days |
| 600+ Chaos | about 70 days |

The process can become faster when several major powers possess unresolved war goals or when many countries are already exposed by large wars. It can become slower when few valid legal opportunities exist. Any factor must use bounded existing information.

### Evolution log direction

The record should communicate that governments have begun treating weakness, isolation, and distraction as reasons to act. It should mention claims, intervention plans, and opportunistic timetables without listing hidden targets or strategy scores.

## Evolution III: Total Offensive

### Chaos requirement

`600+`

### Strategic role

Total Offensive increases scale, frequency, and accepted strategic risk. It should create dangerous AI behavior without turning the AI into a self-destructive attack loop.

The evolution affects operations already valid under the baseline and active lower layers. It can make them larger, broader, and harder to stop.

### Immediate active-event changes

When the evolution activates, AI countries should:

- commit a larger share of available reserves to selected decisive operations
- accept parity or limited local inferiority for high-value attacks when support and follow-up are strong
- coordinate more than one offensive axis when country capacity permits it
- prepare larger amphibious operations and secondary landing axes when transport, route control, and supply are credible
- move air and mobile forces more aggressively between theaters
- shorten the interval between completed operations and the next viable plan
- continue pressure through higher losses when replacement and strategic value justify it
- accept a thinner but still real home reserve during a decisive campaign
- seek to finish vulnerable enemies before turning to less urgent fronts

### Independent behavior boundary

Total Offensive has its own scale and risk layer.

When Relentless Offensives is disabled, Total Offensive can launch larger operations but does not gain the longer continuation and shorter recovery rules from Evolution I.

When Predatory Powers is disabled, Total Offensive can use more theaters inside existing wars but does not gain the additional opportunity-war behavior from Evolution II.

### Risk ceiling

The evolution can reduce safety margins. It cannot cancel hard safety limits.

It must still block or suppress:

- attacks through critical supply collapse
- operations that cannot receive fuel or replacements
- naval invasions with no viable transport, route control, port plan, or follow-up force
- commitment of every effective reserve while the homeland is threatened
- unlimited additional wars
- attacks with no valid enemy or legal path
- repeated use of the same failed axis without changed conditions
- generic behavior that breaks a special country's owner rules

### Decisive-campaign logic

The highest aggression should appear when a country has a plausible chance to achieve a decisive result.

Examples include:

- a major enemy is near capitulation
- a breakthrough can seize the supply system of a large front
- a landing can open a sustainable second front
- an enemy has committed most forces elsewhere
- a valuable ally is close to defeat and intervention can still save it
- a claimed rival is isolated and the attacker has the capacity to finish the war quickly

The AI should be less willing to create a new distant theater merely because this evolution is active.

### Active-event pacing target

The base MTTH target is 120 days after reaching 600 Chaos.

Suggested pacing bands:

| Campaign state | Target pacing |
| --- | --- |
| 600 to 799 Chaos | about 120 days |
| 800 to 999 Chaos | about 95 days |
| 1000+ Chaos | about 75 days |

Higher Chaos shortens the wait but does not make the evolution immediate after an already active event. The pre-fire evolved opening remains immediate when the event first fires after the threshold.

### Evolution log direction

The record should communicate that states now accept larger campaigns, thinner reserves, and more ambitious invasions. It should show the scale of military commitment through mobilised formations, crowded ports, packed airfields, and expanded front orders. It should not claim that attack bonuses have been granted.

## Evolution interaction table

| Active layers | Expected behavior |
| --- | --- |
| Baseline only | More active current wars, better concentration, viable invasions, stronger use of existing objectives |
| Baseline + I | Current wars gain sustained pressure and stronger follow-up |
| Baseline + II | Current wars are more active and valid external opportunities are pursued more aggressively |
| Baseline + III | Current wars use larger operations and greater risk, without added persistence or predation from disabled layers |
| Baseline + I + II | Sustained current wars plus greater use of legal strategic opportunities |
| Baseline + I + III | Large and persistent operations inside existing wars, without Evolution II's additional-war pressure |
| Baseline + II + III | Larger operations and stronger opportunity use, without Evolution I's persistence rules |
| All layers | The full event identity, with sustained operations, predatory opportunity use, and high but bounded strategic risk |

## Evolution notification cadence

An active-event evolution should create one concise global report to each human player and one evolution log entry. Reports should not repeat hidden formulas or enumerate every AI behavior change.

When several evolutions activate through the pre-fire opening, use one combined opening report. The evolution log still records each stage separately.

## Save and reload

Each activated layer must persist across save and reload. MTTH progress should follow the normal event system's save behavior. Reopening Event Details must show the correct enabled state, activation history, tier, and stage.

A save made while a country is human-controlled and loaded after it returns to AI must restore the active layers without another event or evolution popup.
