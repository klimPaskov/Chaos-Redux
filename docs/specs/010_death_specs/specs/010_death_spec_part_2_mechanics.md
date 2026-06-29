# Event 010 - Death: Mechanics, State Effects, Evolutions, and Defeat

## Core variables and flags

The implementation should centralize tuning in script constants and shared helper effects rather than scattering numbers across events, decisions, focuses, and AI.

Suggested global variables:

| Variable | Purpose |
| --- | --- |
| `death_consumed_population` | Total population deleted by Death, used for spread speed and ghost scaling. |
| `death_consumed_states` | Number of states Death has consumed. |
| `death_mainland_states` | Number of mainland states consumed. |
| `death_island_states` | Number of island states consumed before or after reveal. |
| `death_spread_pressure` | Current spread tempo value. Rises with consumed population, chaos, world-end state, and ignored reports. Falls with containment work. |
| `death_soul_power_total` | Death's generated soul-power budget from consumed states, consumed population, and last-shore footholds after world end begins. It has no storage cap. |
| `death_soul_power_available` | Generated soul power not yet spent on spread actions or ghost hosts. |
| `death_soul_power_spent` | Soul power already bound into spread actions or ghost hosts. |
| `death_reveal_state` | `0` hidden, `1` delayed rumours, `2` public Death reveal, `3` world-end. |
| `death_ghost_tier` | `0` no ghosts, `1` weak ghosts, `2` strengthened ghosts, `3` world-end hosts. |
| `death_coastal_jump_cooldown` | Prevents repeated coastal-jump spam after a failed or pushed-back mainland foothold. |
| `death_containment_pressure` | Coalition and national containment work that slows spread without trivializing it. |
| `death_world_end_footholds_created` | Ensures world-end footholds are created once. |

Suggested state flags/variables:

| State flag or variable | Purpose |
| --- | --- |
| `death_origin_state` | First island state. |
| `death_consumed_state` | State was consumed by Death at least once. |
| `death_active_wasteland` | Death currently controls it and the hostile wasteland effects are active. |
| `death_recaptured_wasteland` | Non-Death country controls it after Death was pushed out. Population and industry remain gone. |
| `death_wither_target` | State is being withered from an adjacent Death mainland state. |
| `death_wither_progress` | Progress toward consumption in a neighboring target state. |
| `death_quarantine_line` | A country has active containment work in this state. |
| `death_purification_project` | A recaptured wasteland has an active cleanup/rebuild mission. |

Suggested country flags:

| Country flag | Purpose |
| --- | --- |
| `death_country_created` | Set on Death after creation. |
| `death_publicly_revealed` | Set globally once the reveal super-event fires. |
| `death_containment_member` | Country participates in the Living Containment Compact. |
| `death_has_declared_containment_war` | Country has publicly entered the war against Death. |
| `death_necromancy_unlocked` | Country has opened the dark methods branch. |
| `death_herald_of_zol` | Country has pledged itself to Zol. |
| `death_black_oath_broken` | Country betrayed or escaped the Herald path. |

## The consumption effect

Every Death state should pass through one shared scripted effect, even if the call comes from origin creation, island spread, withering, coastal jump, world-end foothold creation, or a manual scenario. This prevents drift between versions.

A consumed state must:

1. save its pre-consumption population.
2. add that value to Death's consumed-population variable.
3. send the value to the shared civilian deaths tracker when enabled.
4. set the state population to zero.
5. delete all civilian factories, military factories, dockyards, synthetic refineries, fuel silos, airbases, anti-air, radar, forts, coastal forts, naval bases, railways, supply hubs, infrastructure, and other strategic buildings if the engine can remove them.
6. remove or neutralize resources and local building slots through state modifiers if raw deletion is not possible.
7. transfer owner and controller to Death.
8. add a Death core.
9. apply the Death wasteland state modifier.
10. clear resistance, compliance, garrison, and occupation-state concerns from Death by making the state a Death core.
11. mark the state as consumed permanently.
12. update consumed-state counters and spread pressure.
13. update event-log and chaos/death history if the reveal state allows the player to know what happened.

If some building category cannot be literally deleted by script, the implementation must document the unsupported field and use an equivalent state modifier or scripted cleanup that makes the state strategically useless. This is not a design fallback. It is the engine-specific representation of the same requirement.

## Wasteland effects

A Death wasteland should be worse than an ordinary low-supply state. The player should not be able to use Death territory as a shortcut or a supply base.

### While Death controls the state

Death-controlled wastelands should apply:

- near-total local supply failure.
- severe division movement speed reduction.
- severe attrition.
- no usable industry.
- no usable ports, airfields, rail, or supply hubs.
- no local manpower.
- no resistance against Death.
- a dark/fog/storm visual state if possible.
- a ticking wither effect against non-Death divisions that remain too long.

The movement penalty should be absurd enough to make crossing Death territory feel like marching through a dead storm. The intent is not a small debuff. Divisions can still occupy tiles to defeat Death, but they should need preparation, supply support, and time.

### While a non-Death country controls a recaptured wasteland

Recaptured wastelands remain empty. Reoccupation does not restore population or industry.

The state should keep:

- zero population.
- no industry.
- damaged or absent infrastructure and supply.
- a milder lingering wasteland modifier.
- long rebuilding projects if the player wants limited strategic use.
- no automatic restoration of resources or ports.

A recaptured wasteland can be made less lethal through purification/outpost decisions, but it should not become a normal state again during the same campaign unless a later accepted feature deliberately creates an extraordinary restoration system.

## Ticking strength loss

Divisions that remain in a Death-controlled state should slowly wither. This should not require a daily all-world division scan. Use the narrowest feasible pulse over tracked Death states, active Death fronts, or state targets.

Design direction:

| Stage | Wither behavior |
| --- | --- |
| Hidden island stage | No active strength loss unless a country has already found and invaded the island. |
| Revealed mainland stage | Non-Death divisions in Death-controlled states suffer small weekly strength loss after a grace period. |
| 600 ghost tier | Wither loss increases and interacts with ghost divisions. |
| 800 ghost tier | Wither loss becomes a serious occupation cost. |
| World-end | Wither loss becomes a major reason to use containment preparation instead of charging blindly. |

The wither pulse should check for protection from relevant containment decisions, special equipment, route flags, and temporary operations. Protection should reduce the damage, not remove all danger.

## Spread mechanics

Death does not expand like a normal country at first. It consumes.

### Spread pressure

`death_spread_pressure` determines when the next spread attempt happens. It rises from:

- total consumed population.
- consumed-state count.
- chaos tier and chaos value.
- Death's current evolution stage.
- mainland reveal state.
- world-end state.
- failed containment missions.
- countries ignoring delayed island reports.
- Heralds of Zol feeding states or names to Death.

It falls from:

- active coastal watch networks.
- quarantine lines with divisions present.
- successful investigation work before reveal.
- successful purification projects on recaptured states.
- Living Containment Compact coordination.
- naval patrol and convoy-watch decisions.
- temporary high-cost emergency measures.

### Black Ledger and soul power

Active DTH has a Black Ledger decision category. It shows consumed states, consumed islands, consumed mainland states, consumed population, spread pressure, generated soul power, available soul power, spent soul power, host counts, and the current availability of island spread, mainland spread, and ghost hosts.

Soul power is an uncapped budget derived from consumed states and consumed population, with extra points from last-shore footholds after world end begins. Death spends this budget through DTH decisions. Island spread starts at a small amount, still needs Second Shore plus an island-spread focus, and raises the next forced island cost by one after each successful Black Ledger island consumption. Mainland spread spends more, still needs Mainland Smell plus either the normal pressure route or the living-war bypass after Second Shore, and raises the next forced mainland cost by two after a successful use. Ghost host decisions spend the same budget and are limited by the current host stage and valid spawnable Death wastelands. Each host raised adds 0.25 soul power to later host costs. These Death-side actions do not use political power. Spread pressure unlocks the normal mainland route, increases withering progress at high and extreme pressure, shortens coastal-jump cooldowns at those thresholds, and lets Death keep attempting coastal jumps once pressure is high enough.

Spread should accelerate as Death eats more population, but the formula should have floors and caps so it is slow early and terrifying later. The hidden opening must not behave like a weekly expansion loop. A calm-world origin waits several months before the first follow-up island attempt, using a randomized four-to-six-month pulse band, then steps down through slower early bands before reaching the faster revealed and world-end schedules.

| Situation | Spread feel |
| --- | --- |
| Origin only | Four to six months of silence before the next hidden spread attempt. |
| Few small islands | Slow, missable, with delayed marine-office packets arriving as local evidence rather than instant global notification. |
| Several islands | Pattern emerges for attentive players. |
| First mainland | Reveal. Spread becomes a visible crisis. |
| Millions consumed | Spread pulses become frequent. |
| 600 tier | Ghosts make occupation and containment harder. |
| 800 tier | Death can recover from setbacks through coastal jumps. |
| World-end | Continents receive simultaneous footholds and front pressure. |

### Island target selection

Before reveal, target selection prefers:

1. island states near Death's current consumed islands.
2. sub-100,000-population nearby islands with no divisions.
3. if no nearby sub-100,000 island exists, any eligible sub-100,000 island.
4. the broader low-population island pool only after the sub-100,000 pool cannot satisfy the attempt.
5. islands without major capitals, major industry, or heavy ports.
6. islands owned by countries unlikely to notice immediately.

The target should not be chosen because it is dramatic. Death starts by eating the places the world ignores.

### Mainland target selection

Death can attempt mainland consumption naturally only after Mainland Hunger has been recorded, the mainland focus has been taken, and enough island spread pressure has accumulated. This blocks first-month mainland reveals and forces the early event to remain an island pattern before the public crisis. If a living country declares war after Second Shore, the mainland focus can record Mainland Hunger early and try one valid mainland target. This bypass never works during baseline silence. The triggerable scenario is separate and can create an immediate mainland reveal without using natural evolution gates. The first mainland target should prefer:

- nearby coastal states.
- low-defense states.
- states without divisions.
- states with more than 100,000 population only when the reveal is ready.
- states that are not major capitals for the first mainland reveal unless the campaign is already high chaos.

The first mainland state over 100,000 consumed by Death triggers the reveal super-event.

### Neighbor withering

Once Death controls a mainland state, it can wither neighboring states.

A wither target:

- must neighbor a Death-controlled mainland state.
- must not already be Death-consumed.
- must not contain non-Death enemy divisions.
- must not be protected by an active successful quarantine line.
- must belong to a country Death is at war with or will automatically declare war on.
- should be weighted toward lower population early and higher strategic effect later.

If a target state gains non-Death divisions, consumption progress pauses or decays. The player should learn that physically holding the line matters, but border troops should not be able to sit indefinitely without cost: a weaker border-withering state modifier and narrow daily unit damage continue while the state borders an active Death wasteland.

If wither progress reaches completion, the target state is consumed by the shared consumption effect.

### Automatic war on neighbors

After reveal, Death automatically declares war on any country that controls a neighboring state. This should happen when:

- Death takes a mainland state.
- Death's border changes.
- a non-Death country takes or receives a neighboring state.
- Death creates a world-end foothold.

Avoid daily world scanning. Hook the check into Death state changes, war/peace changes, event pulses, or targeted periodic refreshes.

### Coastal jumps

If Death is pushed back from a mainland foothold or has no viable land wither route, it can jump to a nearby coastal state after a cooldown.

Coastal jump rules:

- only after public reveal, except in a high-chaos pre-fire evolved opening explicitly starting on the mainland.
- uses a cooldown to avoid whack-a-mole spam.
- target must be coastal.
- target should prefer low-defense states without divisions.
- target should prefer continents where Death has no current foothold.
- target should not have Coastal Watch unless Death has completed No Ferry Returns.
- target should be blocked or delayed by coastal watch networks, naval patrol decisions, and high containment pressure.
- target cannot be a protected state with a successful emergency quarantine mission unless world-end rules override it.

Coastal jumps are the reason Death remains dangerous after being pushed off one shore. They should not fire instantly after every loss.

## Defeating Death

Death should not be defeated by normal capitulation shortcuts. It should have a 0% surrender/capitulation threshold where supported, but the reliable rule is a custom defeat check:

Death is defeated when every state it owns or controls is occupied by an enemy or Death controls no states.

On defeat:

- Death is removed or annexed through a clean scripted effect.
- active wither targets are cleared.
- coastal-jump cooldowns and spread pulses stop.
- ghost divisions are deleted.
- `world_in_threat` is refreshed and Death's source flag is cleared.
- recaptured wastelands remain empty.
- countries that occupied Death states receive cleanup/rebuild decisions.
- a defeat aftermath super-event fires if Death was publicly revealed and consumed enough population to become a world crisis.
- no defeat super-event fires if Death was quietly eliminated before public reveal unless the player was directly involved and receives a local report.

The defeat effect should be idempotent. It must be safe if called from a war event, occupation event, manual scenario cleanup, or debug force action.

## Ghost divisions

Death has no starting divisions. Ghost divisions are an evolution mechanic.

### Unit identity

Suggested custom unit type: `death_ghost_host`

Suggested template families:

| Tier | Template name direction | Role |
| --- | --- | --- |
| 600 tier | `Thin Ghost Host` / `Pale Column` | Weak, low-org border body. |
| 800 tier | `Mourning Host` / `Ashen Line` | Still weaker than infantry, more numerous. |
| World-end | `Ruin Host` / `Black Infantry` | Comparable to infantry and aggressive. |

Ghost units should not need normal manpower or equipment. They are spawned by consumed population and event stage, not recruited through industry. Each ghost battalion uses one dummy manpower and one dummy infantry equipment only because the engine expects non-empty unit requirements. They should still be limited by formulas so Death does not generate infinite divisions from tiny islands.

### 600-tier evolution

At around Chaos Tier 600, if Death is active or if Death first fires in a high-chaos world, it can unlock weak ghost divisions.

Rules:

- spawn small numbers based on consumed population and state count.
- divisions have very low organization and poor stats.
- they are passive on borders and should not attack.
- their main job is to make occupying Death states less trivial.
- they should be easy to push by prepared infantry.

### 800-tier evolution

At around Chaos Tier 800, Death can spawn more ghost divisions.

Rules:

- more divisions per consumed-state/population band.
- slightly better organization and defense.
- still weaker than normal infantry.
- still generally passive, with only limited local attacks if an enemy is badly weakened.
- stronger interaction with wither state effects.

### World-end stage

During the world-end scenario:

- ghost divisions spawn in every continental foothold.
- templates are roughly on par with ordinary infantry.
- Death receives aggressive AI strategy.
- ghosts may attack, pin, and exploit withered states.
- withering and coastal jumps become much more frequent.

Death should feel almost impossible to stop once it reaches this level, but not because it cheats instantly. It should feel impossible because the player ignored too many stages and allowed the consumed-population engine to scale.

## Evolution tracks

Evolutions are unlock milestones layered on top of the baseline crisis. They are not ordinary progress reports, reveal markers, or alternate scenario presets. Baseline Death consumes one small random island, schedules subtle delayed reports, and then waits. Until the first evolution and a matching Death focus are present, the country should be easy to defeat if discovered early and should usually be ignored by AI countries.

### Evolution I: Second Shore

| Field | Design |
| --- | --- |
| Chaos band | Around 200+ |
| Type | First spread unlock |
| Active-event entry | Death records the stage once the crisis is active at the first chaos threshold or higher. |
| Focus unlock | Opens the Shroud, Hunger, Census, and island-spread focus group. |
| Behavior unlock | Once an island-spread focus is taken, Death can consume one more island and then spread to other low-population islands slowly. |
| Player-facing content | The world still sees only maritime errata and quiet local investigations. |
| Log title direction | `Second Shore` |

This evolution should not reveal Death or create a military front. It only turns the first island into a slow hidden pattern.

### Evolution II: Mainland Hunger

| Field | Design |
| --- | --- |
| Chaos band | Around 400+ |
| Type | Faster island pattern and mainland approach |
| Active-event entry | Death records the stage only after Second Shore, enough consumed-state pressure, and the second chaos threshold exist. |
| Focus unlock | Opens the mainland focus path that can create the first public mainland consumption. |
| Behavior unlock | Island consumption can move through faster spread bands and the mainland route becomes possible once the focus is taken. |
| Player-facing content | Reports can suggest a wider pattern without naming Death before reveal. |
| Log title direction | `Mainland Hunger` |

This evolution makes the hidden crisis ready to become public. It should not create ghosts by itself.

### Evolution III: First Hosts

| Field | Design |
| --- | --- |
| Chaos band | Chaos Tier, around 600+ |
| Type | Weak military mutation |
| Active-event entry | Death records the stage when it exists at the 600-tier threshold and has not been defeated. |
| Unit unlock | Weak custom ghost hosts using `death_weak_ghost_host`. |
| Behavior unlock | Hosts are passive border blockers with very low organization and should be easier to push than ordinary infantry. |
| Player-facing content | After reveal, reports can describe thin figures holding roads without much initiative. |
| Log title direction | `First Hosts` |

This is the first military evolution. It should help Death survive a little longer, not let it conquer like a normal army.

### Evolution IV: Hollow Hosts

| Field | Design |
| --- | --- |
| Chaos band | Totalen Chaos, around 800+ |
| Type | Stronger military mutation |
| Active-event entry | Death records the stage when it exists at the 800-tier threshold and has not been defeated. |
| Unit unlock | More custom ghost hosts using `death_hollow_ghost_host`. |
| Behavior unlock | Hosts have higher strength and organization than the first host tier, while staying weaker than ordinary infantry. |
| Player-facing content | Revealed Death can hold more wasteland fronts and becomes harder to clean up casually. |
| Log title direction | `Hollow Hosts` |

This evolution is where containment should become coordinated. Local victories should still work, but unattended fronts should no longer stay quiet.

### Evolution V: World End

| Field | Design |
| --- | --- |
| Chaos band | World Collapse, around 1000+ |
| Type | Terminal host and aggression mutation |
| Active-event entry | Death records the stage only after the world-end branch starts. |
| Unit unlock | Numerous custom hosts using `death_last_shore_ghost_host`. |
| Behavior unlock | Hosts are roughly on par with infantry and Death begins aggressive attack behavior. |
| Player-facing content | The world-end super-event handles the public shock. The evolution detail describes the terminal Death state. |
| Log title direction | `World End` |

This evolution must not bypass the required condition that a full continent is consumed before the world-end scenario begins.

## World-end footholds

When world-end begins, create one random coastal foothold per continent that does not already contain Death.

Foothold target rules:

- coastal state.
- not already Death-consumed.
- not a scripted protected exception unless no other coastal state exists.
- can be a populated state because the world-end branch is supposed to be catastrophic.
- should prefer lower defense but does not need to stay low population.
- if possible, avoid selecting a state currently containing large allied armies unless world-end pressure is already overwhelming.

Each foothold is immediately consumed and receives world-end ghost divisions. The owning country is pulled into war against Death if not already at war.

## Chaos, deaths, and air cleanliness links

Death is fundamentally a deaths-system event. Every consumed population should be treated as civilian deaths when the deaths system is enabled. Every 1,000,000 total deaths should still affect Chaos through the shared Chaos Meter rules. But with this event, move it to 10million. So deaths caused from the death country are 1/10.

Death should not create air contamination by default. A Death wasteland is not a chemical cloud or biological outbreak. It may use dark-storm visuals, but those are supernatural/visual and should not automatically alter Air Cleanliness unless a later accepted feature explicitly links Death with contamination.

Condemnation should not rise just because Death kills people. Condemnation is blame for countries using unconventional weapons. Countries using necromancy or deliberate sacrificial anti-Death methods may gain condemnation or a new public-horror value if the implementation has a suitable system.

## World-threat integration

After Death consumes a continent, it should become a world threat source using the shared world-threat framework. Public mainland reveal alone should not set the world-threat source. Death should not create a parallel global threat flag.

Suggested source flag: `world_threat_source_death`

The Death threat source should be true while:

- Death exists and
- Death has consumed at least one continent or is in world-end state and
- Death controls at least one state or has active world-end foothold logic.

It should clear when Death is defeated. The shared `refresh_world_threat_state` should then recalculate `world_in_threat` based on all active threat sources.

## Manual triggerable scenario

Death should have a triggerable scenario after implementation. It is a manual sandbox/challenge setup, not a normal prerequisite-bound event.

Suggested scenario ID: `SCN-006`

Scenario type:

| Type | Meaning |
| --- | --- |
| Instant Outbreak | Consumes a hidden island origin, some intensity-scaled islands, and at least one mainland reveal state immediately. |

Intensity stops:

| Intensity | Starting territory | Starting ghosts |
| --- | --- | --- |
| Low | One tiny island, one mainland reveal state, and no extra chaos-meter pressure. | One weak passive host attempt. |
| Medium | Origin, a small island pattern, one mainland reveal state, and a little extra mainland pressure. | Two weak passive host attempts. |
| High | Origin, a wider island pattern, mainland reveal, and stronger opening pressure around the world. | Two stronger host attempts. |
| Maximum | Origin, the widest instant island pattern, multiple mainland pressure points, and a maximum opening crisis footprint. | Four stronger host attempts. |

Manual launch should only block impossible or conflicting states, such as an already active Death crisis or no valid origin and mainland targets. It must not require live Chaos Meter progression, prior reports, date gates, or natural evolution unlocks. It must not set the Chaos Meter, record natural evolutions by shortcut, or start world-end. Chaos should rise only from Death's later natural kills and shared deaths-system links after the scenario has begun.

## Balance philosophy

Death should be frightening because it is allowed to become a crisis, not because it instantly overpowers the world.

Early Death is beatable if the player notices the island, declares war, and occupies it. Midgame Death is costly but containable with coordinated war and border presence. Late Death is a world crisis. World-end Death is meant to become almost impossible unless the player prepared earlier.

Important balance anchors:

- long hidden origin delay.
- low-pop target preference early.
- no starting army.
- withering blocked by divisions in target states.
- coastal jumps limited by cooldowns and watch decisions.
- ghost divisions weak at first.
- consumed population as the main speed scaler.
- world-end branch gated by continent consumption and Chaos above 1000.
- recaptured states remain damaged, so victory is costly even when successful.
