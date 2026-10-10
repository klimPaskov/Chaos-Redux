# Industrial Boom specification, part 10: Achievements and acceptance

## Achievements

Achievements reward hard combinations of output, restraint and recovery, never the event merely firing.
Titles are working titles, and final descriptions are written at implementation from the conditions given.
Every achievement is for a player country, tracks one boom through its episode id (`industrial_boom_episode_id`), keeps its thresholds in the Event 34 tuning constants, and is registered in `common/achievements/chaos_redux_achievements.txt` with an icon triplet.

### The Long Fall (implemented)

`chaos_redux_034_the_long_fall` is registered and its triplet exists.
It unlocks on `great_depression_achievement_long_fall_proven`, which Event 35 sets when the country survives the collapse of an Evolution III boom, rescues an inherited industrial region, and recovers without abandoning a Depression Center or losing the country.
Event 35 owns the proof; Event 34 owns the achievement identity.
It cannot unlock until Event 34 can reach Evolution III, because every current collapse is delivered at baseline (part 5).

### Managed Expansion

`chaos_redux_034_managed_expansion`, hard, visible.
Run the Economy Hot at least twice in one boom, reach the Strained band, then complete a controlled landing in the Sustainable band with at least two Secured projects, or one when the country has a single region.
Disqualified by a crash or an Emergency Production Halt in that boom.
Icon direction: an overdriven flywheel brought back under a marked limit, rail network behind.

### The Miracle Holds

`chaos_redux_034_miracle_holds`, very hard, visible.
Under Evolution II or III, declare a Miracle Region in every region the country has (at least two), bring every one to Secured, lose none, and complete a controlled landing.
Disqualified by losing a Miracle Region, Let It Run being active at landing, or a crash.
Icon direction: a dense factory and rail complex held inside a strong frame, with one impossible crane.

### Redline Nation

`chaos_redux_034_redline_nation`, very hard, visible.
Spend at least 120 days in the Dangerous or Critical bands during one boom, 30 of them in Critical, never reach 100, and complete a controlled or rough landing with at least one Secured project.
Disqualified by a failed Prevent the Crash, an Emergency Production Halt, or a crash.
Days are counted once per day per boom so band flicker or a reload cannot double them.
Icon direction: a gauge near its maximum with the assembly line still running.

### Built to Last

`chaos_redux_034_built_to_last`, hard and long-term, visible.
Complete two controlled landings in separate booms of the same country, with no Event 34 crash between them, at least one Secured project in each, and two different project profiles across the two.
State legacy receipts prevent the same state and project from counting twice.
Icon direction: two generations of works joined by one freight line.

Earlier drafts also proposed Every Link Held, which required protected regions to absorb qualifying shocks in every region.
It is dropped because it depended on situational enemy action and on the protection level ladder this audit removed.

## Edge cases

| Situation | Behavior |
| --- | --- |
| Target stops being a major | The boom continues; major status is an entry gate only |
| Target becomes a subject | The boom continues; the overlord gains no control of the category |
| Player switches country or hands off in multiplayer | Country state stays with the country; nothing duplicates or resets |
| Capital moves | Supply and connection checks follow the new capital |
| All regions or all industrial cores lost | Projects cancel; the boom continues without projects (part 4) until it lands or crashes |
| Civil war | The ledger stays with one side; the other side's regions count as lost (part 4) |
| Annexation or deletion | The boom ends without delivery; no orphan decision, target or depression remains |
| Peace during exploitation | War demand falls and running hot loses value; the boom does not end |
| War begins during landing | The mission continues; cancelling it to run hot is the player's choice |
| Region loses core status | It stays a region until landing, but permanent legacy requires core status |
| Region changes owner during landing | Its project is excluded; no legacy converts in a state the target no longer controls |
| No valid target | The event is unavailable and does not fire |
| Evolution disabled mid-boom | An applied stage stays for this boom; no new stage applies |
| Evolution unlocked during landing | Pacing stays paused; the stage can apply to a later boom |
| Save and reload | Lifecycle state, Overheating, projects, reserve, protection, stage, incident memory and handoff state persist without re-initializing |

The anti-farming controls are in part 4.

## Acceptance scenarios

| Scenario | Setup | Pass when |
| --- | --- | --- |
| 1. Baseline controlled landing | Large major at peace, strong supply | Output rises meaningfully, a project converts, no Event 35, category cleans fully |
| 2. Player non-major | One region | Every essential action is affordable and one project can secure |
| 3. Wartime exploitation | Major war, equipment deficit | Running hot has real military value, risk is visible, a rough or controlled landing follows |
| 4. Blockaded maritime country | Import dependence, convoy losses | Supply leads the cause line, convoy costs apply, restored access lowers drift |
| 5. Region bombing | Two regions, one protected | The protected region keeps its progress once, the other pauses; damage is not duplicated |
| 6. Speculative Mania | One speculative project | Credit restraint replaces cooling, abandonment gives larger relief, a crash enters Financial Contagion |
| 7. Industrial Miracle | Two Miracle Regions, low final pressure | First Secured Miracle project records one guarded Chaos gain; budgets hold; landing reverses only that gain |
| 8. Runaway crash | Let It Run, no reserve | Event 35 starts at The Second Great Depression for the same country, spread states arrive as corridors, pacing counts once, no boom bonus remains |
| 9. Existing depression | Event 35 already active | The collapse deepens one episode with no duplicate category or idea |
| 10. Repeated booms | Several booms in one campaign | Starting pressure and legacy follow part 4, no unlimited factories or slots |
| 11. Deletion during collapse | Target annexed in Critical | No ghost depression or invalid target |
| 12. Supplier contract | Depressed country offers a contract to an active boom | Supplier gains output and pressure, a later rough landing upgrades once |
| 13. Save and reload | At opening, running, evolution, Critical, landing, handoff retry | Nothing duplicates, nothing is lost, no Chaos repeats |

## Completion coverage

Implementation is complete only when these agree with this package: target gate and weighting, opening and actor history, Overheating and its header, band effects, decisions and missions, regions, projects, reserve and protection, the four outcomes, all three evolutions with both entry paths, the Event 35 producer fields and multi-region delivery, the supplier contract additions, AI and probability evidence, guarded Chaos, legacy budgets, assets, localisation, Event History, Event Details and evolution rows, the permanent event documentation, the catalog workbook row with regenerated exports, save persistence and cleanup.

The design should stop growing until implementation or testing exposes a concrete gameplay gap.
