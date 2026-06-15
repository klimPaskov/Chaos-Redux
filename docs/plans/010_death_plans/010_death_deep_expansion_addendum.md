# Event 010 Death - Deep Expansion Addendum

Plan-only handoff for parent review. Do not treat this file as implementation completion.

This addendum expands `/docs/specs/010_death_specs/010 - Death.md` into an implementation-ready design layer. If accepted, the parent should fold the selected material into `docs/specs/010_death_specs/010 - Death.md` or split it into source spec parts under `docs/specs/010_death_specs/`.

No prior Death addendum was found under `docs/plans/010_death_plans/` before this file was written.

## Design Promise

Death should feel like a geographical fact that becomes a country only because HOI4 needs a tag. It starts as a black island whose existence is administratively plausible, then becomes a silence on charts, then a naval rumor, then an impossible coastal war, then a terminal world condition. The player loop must therefore be about noticing absence, deciding how much to spend before proof exists, containing coastlines before the public understands why, and later fighting a foe that does not occupy territory so much as remove it from history.

This should not become a zombie outbreak, demon invasion, plague, cult rebellion, or normal necromancer tag. Ghost divisions are not resurrected soldiers with personalities. They are battlefield pressure made visible: weak, cold, anonymous formations that mark where countries can no longer keep names attached to bodies.

## Research Anchors For Tone

Use these as inspiration and naming anchors, not as claims that Death is literally any one tradition.

- Remote island mystery: the Flannan Isles lighthouse case gives the exact early-event mood: no response, no bodies, tidy traces, delayed discovery, official uncertainty. National Records of Scotland notes that the light was not seen for days, the relief crew found no sign of life, and the investigation remained haunting even with a likely wave explanation. Source: https://blog.nrscotland.gov.uk/2023/12/12/flannan-isles-lighthouse-keepers-the-disappearance/
- Phantom islands: historical cartography contained islands that stayed on maps for centuries because of myth, error, mirage, or false reports. This supports the origin logic: Death can be a place that the world cannot classify, not a monster that announces itself. Source: https://www.nationalgeographic.com/travel/article/these-fabled-ghost-islands-exist-only-in-atlases
- Thanatos and Charon: Britannica frames Thanatos as the personification of death, and Charon as a ferryman of the dead. These support internal Death focus names such as "The Allotted Time", "No Ferryman", and "The Unpaid Passage" without turning the country into Greek mythology. Sources: https://www.britannica.com/topic/Thanatos-Greek-mythology and https://www.britannica.com/topic/Charon-Greek-mythology
- Danse macabre: Britannica describes the Dance of Death as an equalizing procession where living figures of every rank are led by the dead. This is a strong visual and achievement anchor for world-end escalation: no class, ideology, or faction receives exemption. Source: https://www.britannica.com/art/dance-of-death-art-motif
- Lazaretto and quarantine islands: Venice's island quarantine model and later quarantine-island systems support ordinary-country containment mechanics: isolation stations, cordons, inspection boards, port closures, and naval interdiction. Source: https://www.britannica.com/science/lazaretto and https://www.nps.gov/places/quarantine-islands.htm

## Stronger Playable Loop

### Phase 0 - The Island That Passes Inspection

Death appears on a random small remote island state, preferably a tiny or small island with low population, low industry, no land border, and limited strategic value. The selected state should be saved as the origin state and receive a hidden `death_origin_island` state flag. Death receives the state, cores it, and is assigned a black map color, Zol as leader, and a "Not Yet A Country" country spirit that suppresses normal diplomacy and AI aggression.

The world should not receive an immediate news event. Instead, create a hidden discovery schedule:

- After a delayed interval, one nearby or relevant observer receives a rumor event such as "The Unanswered Light". Eligible observers are former owner, nearest naval base owner, a country with convoy routes in the sea region, a country with intelligence agency, or a major naval country.
- The event describes absence only: no radio response, no port traffic, no bodies, no flag, old paperwork that says the island is still inhabited.
- The observer can archive the report, send a survey, or conceal it. These options change `death_notice` and `death_silence` values without revealing Death globally.

The early mystery should matter. Countries that investigate early can unlock containment tools earlier, but spending resources before proof should have domestic cost.

### Phase 1 - Silent Island Spread

Death spreads through a hidden island-consumption pulse. This pulse should not use a whole-world daily or weekly on action. Use event-driven timers, state-control callbacks, delayed events, or scheduled hidden events scoped to Death and active candidate states.

Target priority:

1. Small islands in the same sea region.
2. Small islands in adjacent sea regions.
3. Islands owned by weak or isolated countries with low local garrison.
4. Ports or islands whose owner ignored prior reports.
5. Higher-population islands only after low-population targets are exhausted.

Death should not use normal naval invasion gameplay in the earliest phase. It can transfer or consume eligible small islands through hidden event logic because the horror is that nobody saw an invasion. However, this power must be bounded:

- Only non-capital low-population islands before reveal.
- Never consume a state with a player-owned capital before global reveal.
- Never bypass a state with present hostile divisions if the state belongs to a country that has begun active investigation or containment.
- Each consumed state increments `global.death_consumed_states`, `global.death_consumed_population_k`, and `death_silence`.
- Every consumed state gets a state flag and a severe Death dynamic modifier.

Player-facing feedback is delayed and inconsistent:

- "No Mail From [island name]" for the owner.
- "A Weather Station Goes Quiet" for naval powers.
- "The Island Is Still On The Map" for countries that have investigated at least twice.

### Phase 2 - Mainland Reveal

The first Death-controlled mainland or populous coastal state should trigger the public reveal. The current rough threshold of more than 100k population is good, but the final design should combine population and political visibility:

- Reveal if Death consumes any mainland coastal state with population above the configured threshold.
- Reveal if Death consumes any state with a victory point above a configured threshold.
- Reveal if Death consumes a state controlled by a major, a faction leader, or the player.
- Reveal if cumulative consumed population passes a global threshold even without mainland spread.

The reveal super-event should not overexplain. It should tell the player that governments have finally agreed on the name already present on naval lists: Death.

After reveal:

- Set `world_threat_source_death` and refresh the shared `world_in_threat` framework.
- Death automatically declares war on neighboring countries that share a land border with consumed mainland states.
- Ordinary countries unlock anti-Death decisions.
- The "Dead Waters" decision category becomes visible to relevant naval countries.
- Death starts withering neighboring states, but only if the owner fails to keep supplied divisions, forts, or quarantine works present.

### Phase 3 - Containment War

The main play loop for ordinary countries should be a defensive logistics problem, not a cure research race.

Countries fight Death by:

- Holding named coastal belts and ports.
- Creating exclusion zones around consumed states.
- Keeping supplied divisions in threatened neighboring states.
- Evacuating civilians before withering completes.
- Running naval patrols and convoy interdiction in adjacent sea regions.
- Paying hard costs in convoys, trains, trucks, support equipment, infantry equipment, command power, fuel, and stability.
- Choosing whether to centralize a coalition or preserve national control.

Death advances by:

- Consuming under-defended adjacent states.
- Selecting new coastal footholds when pushed off a mainland shore, with a cooldown and only if it still has enough consumed population.
- Raising weak ghost formations as the consumed population grows.
- Turning old fronts into attrition traps rather than high-attack fronts.

Death should be vulnerable when small. If the world commits early, Death can be destroyed by full occupation and loss of all consumed states. The difficulty curve should come from delay, not from early unfair strength.

### Phase 4 - Continental Threat

When Death consumes enough mainland states or a whole continent and chaos is high enough, it stops being a local crisis. This should be an evolution milestone before the true world-end branch unless chaos is already over the world-end gate.

Effects:

- Coalition formation becomes easier and more urgent.
- Neutral countries near Death receive forced defensive missions.
- Ghost divisions become more numerous and can attack limited objectives.
- Withering jumps from adjacency-only to "coastal shadow" rules: coastal states in the same strategic sea region can become target candidates if no containment patrol is active.
- Faction leaders can call "Black Shore Conferences" to coordinate containment.

### Phase 5 - World-End Escalation

The terminal branch should require both systemic danger and Chaos Redux's world-end rule:

- Chaos value over 1000 or the mod's established equivalent world-end eligibility.
- Not already `world_end`.
- Death has consumed a configured population or state share, or consumed an entire continent.
- Death is not currently in a contained/defeated state.

World-end behavior:

- Set `world_end` and `world_end_death`.
- Death gains footholds on every continent in random eligible coastal states.
- Foothold selection avoids impassable states, unowned states that would break effects, and already consumed states.
- Each foothold creates a "Black Landing" state flag and spawns ghost divisions scaled by consumed population, chaos tier, and local resistance.
- Death AI switches from passive pressure to aggressive world consumption.
- Ordinary coalition decisions become emergency-only and no longer require diplomatic preparation.

### Phase 6 - World Consumed

If Death controls or has consumed all valid states, fire a final super-event and achievement. This is not just "Death wins a war". It is a terminal world state:

- Stop incompatible random event branches that need ordinary countries.
- Record final death count and consumed state count.
- Add an event-log terminal entry.
- Show the final state of Zol only if the player is Death or the world is gone. Otherwise, keep Zol unexplained.

## Death Country Package

Recommended tag: reserve a clear event tag such as `DTH` if available. If `DTH` is unavailable, choose a stable unused tag and record it in the spec. Death should be registered as both a special Chaos country and an actual nonhuman country in shared classification docs when implemented.

Country identity:

- Name: Death.
- Adjective: Deathless or Death, depending existing localisation style. Prefer "Death" for starkness.
- Leader: Zol. Fictional/symbolic. Do not source a real portrait. Use generated or symbolic portrait assets.
- Ruling party: "The Stillness" or "The Black Registry".
- Ideology: use the least misleading existing ideology slot, but localize party/government text so the UI does not imply normal politics.
- Map color: pure or near-pure black, with enough contrast to be selectable.
- Diplomacy: cannot join normal factions, cannot guarantee, cannot send volunteers, cannot participate in normal ideology systems.
- Surrender: 0 percent. Defeat requires full occupation or a scripted defeat condition checking no controlled consumed states and no active footholds.

Starting spirits:

| Idea | Role | Lifecycle |
| --- | --- | --- |
| `death_not_yet_a_country` | Suppresses normal aggression and makes Death easy to ignore early. | Replaced at reveal by `death_named_by_the_living`. |
| `death_empty_administration` | Death has no economy, no normal recruitable population, and no reason to use factories. | Replaced by branch-specific internal method spirits. |
| `death_black_shore` | Applies defensive island concealment and weak naval detection resistance. | Upgraded by island-spread focuses; removed after world-end when concealment no longer matters. |
| `death_the_counting` | Tracks consumed population into power, but starts inert. | Upgraded through ghost and withering branches. |

Death should not have a normal advisor cabinet. If advisors exist, they should be fixed-purpose offices with no personal names: "The Empty Chair", "The Last Clerk", "The Unlit Harbor", "The Bell Without Rope". They should alter the method of spread, ghost behavior, and containment resistance rather than ideology.

## Death Focus Tree Architecture

Death is a fixed-purpose country, so it should not have democratic/fascist/communist/monarchist politics. It still needs meaningful internal choices. The tree should be compact but real, with routes that change how Death spreads and how countries respond.

### Lane Map

```text
The First Shore
  -> No Herald / No Envoy / No Tax Ledger
  -> route lock fork:
     A. The Quiet Census       (slow, stealth, more delayed reveal)
     B. The Black Tide         (faster coastal spread, easier reveal)
     C. The Still Front        (stronger withering, weaker island reach)

Support lanes:
  - Empty Economy              (turn consumed industry into spread pressure, not factories)
  - The Unnamed Ranks          (ghost unit progression)
  - Charts Without Coastlines  (island/sea-region target logic)
  - When The Mainland Learns   (post-reveal transition)
  - The Last Continent         (world-end eligibility and final aggression)
```

### Opening Focus Group - The First Shore

Purpose: establish Death's early constraints and hidden identity.

Anchor focuses:

- `The First Shore`: confirms origin state, locks starting focus branch, initializes Death variables.
- `No Herald`: improves secrecy; lowers early observer chance but slows spread.
- `No Envoy`: disables normal diplomacy and reduces opinion/event spam.
- `No Tax Ledger`: removes normal industry expectations; consumed factories become hunger/pressure values instead of usable economy.

Rewards should mostly initialize decisions, variables, target arrays, and spirits. Avoid factory rewards.

### Main Method Fork

Only one method route should be chosen. These are not political ideologies; they are fixed-purpose internal modes.

#### A. The Quiet Census

Narrative: Death counts places before taking them. The world receives fewer warnings, but Death spreads more slowly.

Mechanics:

- Lower early news and investigation probability.
- Higher chance to target neglected islands with no garrison.
- Withering starts weaker but stores more consumed population as future ghost capacity.
- Unlocks decisions/focuses that mark candidate states with "Listed" flags before consumption.

Tradeoff:

- If an ordinary country discovers a Listed state, containment work is more effective and can cancel the listing.

AI:

- Default route if Death is AI and origin is isolated with many island candidates.

#### B. The Black Tide

Narrative: the sea itself becomes the border.

Mechanics:

- Faster island and coastal jump cooldowns.
- Stronger sea-region targeting after reveal.
- Lower stealth and earlier reveal.
- More vulnerable to naval patrol/interdiction decisions.
- Ghost divisions stay weaker until late.

Tradeoff:

- Countries with navies can contain this route more reliably if they act early.

AI:

- Choose when origin is near island chains, naval powers are weak, or chaos tier is high.

#### C. The Still Front

Narrative: Death stops moving quickly and makes every front impossible to hold.

Mechanics:

- Lower jump frequency.
- Stronger adjacent-state withering.
- Higher attrition/movement penalties in Death states.
- Earlier passive ghost border formations, but fewer total coastal jumps.

Tradeoff:

- If surrounded before it reaches multiple coasts, it can be starved of new targets.

AI:

- Choose when Death already has a mainland foothold, high consumed population, or strong neighbors that prevent naval jumps.

### Empty Economy Lane

Death should not build an economy. This lane converts removed industry into abstract pressure.

Mechanics:

- On state consumption, count deleted civilian factories, military factories, dockyards, ports, rail, infrastructure, and population into `death_consumption_yield`.
- Focuses spend this yield on spread cooldown reductions, withering intensity, ghost capacity, and foothold eligibility.
- Death cannot exploit consumed factories as production. This prevents a black superpower with normal industry.

Anchor focuses:

- `Factories Without Hands`: deleted factories increase pressure, not usable building slots.
- `Ports That Receive Nothing`: consumed ports improve coastal target range but do not build navies.
- `The Last Inventory`: high consumed industry improves world-end foothold count.

### The Unnamed Ranks Lane

Ghost divisions should progress through three visible but restrained stages.

Stage 1: `Pale Companies`

- Unlock at around tier-600 evolution equivalent or consumed-population threshold.
- Very low organization, low HP, low attack, slow movement, no planning bonus.
- Spawn only on Death-controlled borders and mostly hold.
- Purpose is to force countries to occupy and clear Death, not to overrun the world.

Stage 2: `Mute Regiments`

- Unlock at around tier-800 equivalent or after mainland reveal plus high consumed population.
- More numerous, still weaker than infantry.
- Can counterattack local border states and punish unsupported pushes.

Stage 3: `The Final Muster`

- World-end only.
- Comparable to infantry in basic combat, still unusual in supply/attrition behavior.
- Aggressive battle plans allowed.

Exploit guard:

- Ghost spawn capacity must be derived from consumed population/state count and capped per controlled state/front.
- No free infinite spawn loops on recapture.
- Ghosts should not drop equipment or manpower rewards to enemies if avoidable.
- If using a custom unit, register it cleanly and avoid creating a normal recruitable unit for other countries.

### Reveal And Endgame Lane

Focuses here should be bypassed or auto-completed based on world state, not require the AI to select them at the wrong time.

Anchor focuses:

- `The Name Arrives Before The Army`: post-reveal transition; unlocks public war behavior.
- `Every Shore Is A Door`: enables limited post-reveal coastal jumps.
- `The Last Continent`: world-end readiness; only active at high chaos and high consumed-state count.
- `No More Maps`: terminal/final focus, useful only for Death player or AI world-end.

## Ordinary Country Decision And Mission Families

Create decision categories that evolve by phase. Do not show every action at once.

### 1. The Missing Islands File

Visible before reveal only to observers with reason to notice.

Decisions:

| Decision | Who sees it | Cost | Effect |
| --- | --- | --- | --- |
| `send_lighthouse_tender` | former owner, nearby naval power, island owner | convoys, small navy XP or PP, 30-45 days | raises discovery chance, may reveal one consumed island state flag to the country |
| `compare_admiralty_charts` | majors/naval powers/intel agencies | PP, command power, 20 days | adds `death_notice`; may identify a sea region at risk |
| `bury_the_report` | authoritarian or unstable governments | PP gain or stability protection, hidden risk | delays public panic but increases `death_silence` and worsens later reveal penalty |
| `publish_the_empty_harbor_story` | democracies, free press paths, player | stability/war support cost | raises global notice and unlocks early coalition prep if another country confirms |

Missions:

- `restore_contact_with_[island]`: 90-day mission; success if owner places a supplied division or naval patrol in the island/sea region before Death consumes it. Failure increases silence and may make the island eligible for immediate consumption.

### 2. Black Shore Containment

Visible after reveal to countries with threatened coastlines, neighboring states, or faction leadership.

State-targeted decisions:

| Decision | Target | Cost | Effect |
| --- | --- | --- | --- |
| `establish_black_cordon` | owned coastal or adjacent threatened state | infantry equipment, support equipment, command power | adds containment progress; slows withering if supplied units present |
| `evacuate_the_shore` | target at withering depth 1-3 | trains, convoys, trucks, stability, timed mission | saves a portion of population into refugee pressure instead of civilian deaths |
| `salt_the_railheads` | adjacent state with rail/supply hub | rail damage, support equipment, CP | makes Death consume the state slower if it falls; hurts friendly logistics |
| `hold_the_lighthouses` | coastal state in threatened sea region | fuel, convoys, naval XP | reduces Death coastal jump chance in that sea region |
| `burn_the_records` | desperate/authoritarian route | stability and legitimacy cost | prevents Death from gaining full yield from that state if consumed; worsens postwar recovery |

Timed missions:

- `guard_the_cordon_line`: 120-180 days. Requires supplied divisions in named threatened states. Success lowers local withering and raises coalition confidence. Failure advances withering or opens a Death jump.
- `keep_the_port_lit`: 90-120 days. Requires port control, convoy availability, no Death control adjacent. Success locks the state out of coastal jump target pool for a cooldown.
- `last_train_out`: 90 days. Requires trains/trucks/convoys and no active combat in target state. Success saves population; failure adds deaths and refugee panic.

### 3. Coalition Of The Living

The coalition should not be automatic on first reveal. It should form when enough countries are threatened or when a major invests in diplomacy.

Formation conditions:

- Death revealed.
- At least one mainland state consumed or a configured consumed-population threshold reached.
- Candidate leader is not Death, not a nonhuman chaos country, not capitulated, not a subject unless allowed by faction leader.
- Candidate leader has either major status, regional proximity, or has completed enough containment actions.
- A minimum number of threatened countries can join or at least one faction leader sponsors the compact.

Faction name direction: "The Living Compact", "The Black Shore Compact", or "The Conference of the Living". Avoid heroic names that make the tone too pulp.

Coalition values:

- `living_compact_cohesion`: affects shared decision costs and member willingness.
- `living_compact_command`: affects joint missions and AI coordination.
- `death_public_dread`: increases when Death consumes populous states; high dread helps formation but hurts stability.

Shared decisions:

| Decision | Cost | Requirement | Result |
| --- | --- | --- | --- |
| `convene_black_shore_conference` | PP, command power, 30 days | reveal plus enough threat | starts formation mission |
| `pool_cordon_equipment` | infantry/support equipment from members | compact exists | grants temporary containment discounts to frontline members |
| `assign_coalition_fronts` | command power, army XP | members bordering Death | raises mission success chance for guard missions |
| `standardize_evacuation_orders` | trains, convoys, PP | high dread | improves evacuation efficiency but reduces stability if overused |
| `declare_the_dead_coast` | coalition leader | Death coastal threat high | creates shared naval patrol mission and sea-region target lists |

Failure states:

- Low cohesion blocks joint offensives and causes members to prefer national containment.
- High dread without cohesion creates panic events and member refusal.
- If leader capitulates or is consumed, leadership passes to highest-valid member or the compact enters emergency mode.

### 4. Necromancy And Joining Temptation

This path should be rare, ugly, and costly. It must not become a powerful normal alliance with Death.

Unlock conditions:

- Death revealed.
- Country has suffered severe losses, high chaos, occult/high-chaos route flags from other events, extremist government, or a special research/leader condition.
- Not already a stable coalition leader unless deliberately betraying the compact.

Decision family names:

- `listen_to_the_last_clerk`
- `open_the_black_register`
- `petition_zol`
- `offer_the_unburied`

Player choices:

1. Study Death to fight it.
   - Costs political stability and intelligence exposure.
   - Unlocks stronger containment but risks `death_temptation`.
2. Use forbidden rites/logistics.
   - Sacrifices manpower, stability, war support, or state population to slow Death locally.
   - Can disqualify containment achievements.
3. Join Death.
   - Only as a terminal betrayal or hidden challenge path.
   - Country becomes a marked client, not a normal ally.
   - Death may eventually consume the client anyway unless the player completes a hard "Remain Uncounted" route.

Do not let AI countries freely join Death. AI should only take study/forbidden containment options under extreme threat and should almost never petition to join unless high chaos, already doomed, and not important to a human player's core war.

### 5. Anti-Death War Logistics

These decisions should be available to countries at war with Death or coalition members.

Actions:

- `issue_white_map_orders`: reduces movement penalty for a limited number of divisions in Death states for a timed offensive.
- `supply_the_living_columns`: consumes trucks, trains, fuel, and support equipment to reduce withering strength loss in target front states.
- `mark_the_return_paths`: requires recon/engineers or army XP; reduces encirclement/retreat risks and lowers attrition.
- `silence_the_empty_broadcasts`: intelligence/agency decision that reduces Death dread and ghost spawn chance in one region.
- `count_the_missing`: post-battle decision that records casualties, improves coalition cohesion, and may reveal actual consumed population.

Offensive missions:

- `occupy_every_tile_in_[state_group]`: auto-completes when no Death-controlled province remains in target state group.
- `hold_the_black_capital`: 180-day mission after Death origin state is occupied; if all footholds are cleared during the timer, Death is defeated.
- `clear_the_footholds`: world-end emergency mission with continent target groups and partial success rewards.

## Withering And State Consumption Rules

Use state flags, state variables, and dynamic modifiers. The player should see the current danger in state decisions or scripted localisation, not only hidden flags.

Recommended state progression:

| Depth | Public name | Trigger | Effects direction |
| --- | --- | --- | --- |
| 0 | Watched Shore | neighboring Death or listed target | mild warning, enables cordon |
| 1 | Withering Shore | no sufficient defense, Death adjacent or coastal-shadow target | movement/supply penalties, evacuation possible |
| 2 | Black Cordon Failure | failed mission or repeated pulse | severe attrition, industry damage begins |
| 3 | Emptying State | no defense and high Death pressure | population loss ticks, factories removed, surrender risk |
| 4 | Consumed Wasteland | Death takes or completes consumption | population removed, civilian deaths registered, industry deleted, Death core added |

Consumption should do all of the following:

- Save pre-consumption population and industry into temporary variables.
- Add population loss to civilian deaths using the existing civilian-death framework if available; if not, the parent should design a shared helper before implementing.
- Remove or damage buildings in a consistent order, with script constants controlling severity.
- Set state category toward `wasteland` where valid.
- Add core of Death.
- Apply a Death state dynamic modifier for movement, supply, attrition, and local recovery lock.
- Clear ordinary containment missions and target flags for that state.
- Increment global Death counters.

Defense should never be a single static division check. Use a defense score:

- supplied divisions present
- forts/coastal forts
- port and rail link
- active cordon decision
- coalition support
- naval patrol in adjacent sea region
- owner stability and command power
- local withering depth penalty

Death pressure score:

- consumed population
- consumed state count
- Death route
- chaos tier
- ghost stage
- adjacent Death states
- previous failed containment
- high-dread world state

The pulse compares defense score and pressure score. If defense wins, withering stalls or regresses one depth. If Death wins, depth advances.

## Dynamic Values And Tuning

Create a dedicated script constants file if accepted, for example `common/script_constants/010_death_constants.txt`.

Constant groups should cover:

- origin island eligibility population and industry caps
- delayed rumor timing bands
- reveal thresholds for population, victory points, consumed population, and major/player involvement
- island spread cooldowns by route
- coastal jump cooldowns by route and phase
- withering depth thresholds
- defense-score weights
- Death pressure-score weights
- evacuation saved-population ratios
- civilian death conversion ratios
- ghost spawn capacity per consumed population and per consumed state
- ghost unit stat tiers
- coalition formation thresholds
- coalition cohesion gains/losses
- necromancy temptation thresholds and costs
- AI willingness weights
- world-end thresholds

Use MTTH variables for:

- early rumor firing
- Death island-spread target selection weight
- public reveal acceleration
- AI coalition joining
- AI containment decision weights
- AI forbidden-study temptation
- world-end readiness pacing

Do not scatter route and cost values across event, decision, focus, and scripted effect files.

## AI Behavior

Death AI:

- Starts passive and should not justify normal wars.
- Prioritizes island consumption by low population and low defense.
- Avoids immediate player capital consumption before reveal unless the player ignores repeated warnings and the state is a valid target.
- Chooses focus route based on geography and threat:
  - Quiet Census for isolated origins and low naval opposition.
  - Black Tide for island chains and weak naval containment.
  - Still Front after early mainland foothold or strong adjacent land-front opportunities.
- After reveal, declares on adjacent countries through scripted rules, not normal ideology aggression.
- In world-end, uses aggressive plans and front assignment.

Ordinary-country AI:

- Investigates early only if naval, nearby, former owner, player ally, or high intelligence capacity.
- Does not bankrupt itself chasing rumors before reveal.
- Forms or joins coalition based on proximity, threat, ideology, major status, and current war burden.
- Prioritizes cordon and evacuation for owned high-population coastal states.
- Uses naval patrol decisions if it has spare fuel/convoys/naval XP and threatened sea regions.
- Avoids forbidden necromancy unless severe threat, high chaos, low stability, and no viable coalition path.
- Never petitions Death casually.

Coalition AI:

- Leader funds shared equipment and front assignment first.
- Frontline members request aid and guard state missions.
- Distant members contribute equipment/convoys instead of suicidal declarations.
- AI should not leave existing factions unless the Death compact is designed to override normal diplomacy. Prefer an additive compact/decision layer if possible.

## Exploit Checks And Cleanup

Required exploit guards:

- No repeated ghost spawn from toggling state control.
- No farming Death ghost units for equipment or XP.
- No free factories from consumed states.
- No repeated evacuation of the same population.
- No containment decision re-click loops without cooldown or cost.
- No coalition equipment pool duplication when members join/leave.
- No player joining Death to avoid all penalties while keeping normal industry.
- No instant full cores for ordinary countries on recovered wastelands.
- No world-end foothold in invalid states.
- No hidden early consumption of major/player capitals without reveal rules.

Cleanup:

- When Death is defeated, clear `world_threat_source_death` and refresh world threat state.
- Clear global Death event targets if global targets are used for origin, current target, or coalition leader.
- Remove active Death target flags from states that are no longer threatened.
- Cancel obsolete containment and evacuation missions.
- Convert consumed/recovered wasteland states into a postwar reconstruction state, not instant normal recovery.
- Keep civilian deaths recorded; do not reverse casualty counters.
- If world-end has fired, defeat should trigger aftermath rather than full cleanup to pre-crisis normal.

## Evolutions

Separate baseline phases from true evolutions.

Recommended evolution tracks:

1. `death_public_reveal`
   - Stage 1: The Name On The Chart - mainland or major reveal.
   - Stage 2: The Black Shore - multiple coastal regions threatened.
2. `death_ghost_muster`
   - Stage 1: Pale Companies.
   - Stage 2: Mute Regiments.
   - Stage 3: Final Muster, world-end only.
3. `death_containment_failure`
   - Stage 1: First failed cordon on mainland.
   - Stage 2: First consumed capital or major port.
   - Stage 3: First continent effectively lost.
4. `death_forbidden_compacts`
   - Stage 1: first country studies Death.
   - Stage 2: first country uses sacrificial/necromantic containment.
   - Stage 3: first country petitions or joins Death.
5. `death_world_end`
   - Stage 1: footholds on every continent.
   - Stage 2: the final consumed continent.
   - Stage 3: world consumed.

Each evolution should record actor where meaningful: Death for its own milestones, coalition leader for compact milestones, betraying country for forbidden compact milestones.

## Super-Events

Use super-events sparingly but decisively.

### 1. Mainland Reveal - "The Name On The Chart"

Role: first public reveal.

Trigger: first valid mainland/populous/major/player reveal.

Tone: quiet official terror. Governments realize the word "Death" was not metaphor.

Image direction: generated period-authentic black-and-white or muted super-event image of a coastal administrative office, empty harbor, black shore, and clerks staring at a map whose coastline is inked out. No readable generated text.

Quote direction:

- Shakespeare, Hamlet: "The undiscovered country..." can fit the reveal if kept short and sourced.
- Ecclesiastes 9:5 can fit if using a short public-domain Bible translation and source notes.

### 2. Coalition Formation - "The Living Compact"

Role: faction/compact formation.

Trigger: first successful coalition formation with enough members or a major leader.

Tone: not triumph, but grim bureaucracy.

Image direction: conference room with black shoreline maps, covered windows, ash or salt on tables, period uniforms and civil officials.

Quote direction: danse macabre/equality of death inspiration, but use a verified public-domain line or scripture. Avoid invented quotes.

### 3. World-End - "No More Shores"

Role: terminal scenario.

Trigger: world-end branch.

Tone: final, sparse, not bombastic.

Image direction: world coastline fading into black sea, abandoned ports, no armies as hero subjects.

Quote direction:

- Revelation 6:8 "his name... Death" works thematically, but verify exact translation and copyright status. KJV is public domain in the US.
- Alternative: Ecclesiastes 9:5 short excerpt.

### 4. Defeat Aftermath - "The Shore Returns Empty"

Role: if Death was a global or near-global crisis and then defeated.

Trigger: Death fully occupied/cleared after public reveal and significant casualties.

Tone: survival with no restoration fantasy.

Image direction: soldiers and civilians at a recovered coast, blank memorial boards, no visible corpses.

Rules: only fire if Death reached mainland and killed enough population or controlled enough states. Do not use a super-event for a quick early island cleanup.

### 5. World Consumed - "The Last Entry"

Role: final total-consumption state.

Trigger: all valid states consumed/controlled by Death.

Tone: almost silent.

Image direction: black ledger, extinguished lamp, coastline gone. This can be more symbolic than the reveal.

## Achievements

Achievements should reward hard play, not event firing.

| Achievement | Conditions |
| --- | --- |
| `Not One Step Into The Sea` | As an ordinary country, defeat Death before it consumes any mainland state. Must not use forbidden/necromancy decisions. |
| `The Lighthouse Was Enough` | Discover Death before public reveal and prevent the first mainland reveal for a long configured duration. |
| `Conference Of The Living` | Form the Living Compact with members from at least three continents and keep cohesion above threshold until Death is defeated. |
| `No Names For The Dead` | As Death, consume a configured population threshold before public reveal. |
| `Every Shore A Door` | As Death, establish footholds on every continent without triggering world-end yet. |
| `The Last Clerk` | Use the forbidden route to survive as a Death-marked client until world-end without being consumed. Very rare/hard. |
| `The Dead Know Nothing` | As Death, consume every valid state. |
| `A Map With Islands Still On It` | As a small island country, survive Death's island phase and help defeat it. |

## UI, Animation, And Assets

Use normal decision categories for most actions. Add a scripted GUI only if the parent wants a central crisis board after reveal.

Recommended presentation:

- Decision category header: "Death: The Black Shore" with dynamic summary lines for consumed population, known withering fronts, coalition cohesion, and current ghost stage.
- Optional scripted GUI: "Black Shore Board" with tabs for Threatened Coasts, Coalition, Death Count, and Forbidden Files.
- State map decisions should use highlights for watched/withering/consumed states.
- Event Details window should explain the premise and current public understanding, not list mechanical penalties.

Asset families:

| Asset | Source mode | Notes |
| --- | --- | --- |
| Death flag | generated/symbolic | black field with minimal emblem; avoid skull-and-crossbones pirate reading. |
| Zol portrait | generated/symbolic | still figure, unreadable face, period-compatible leader portrait; not a skeleton caricature. |
| Death report image origin | generated documentary | abandoned island station/empty harbor. |
| Death reveal super-event image | generated | black coast/map office. |
| World-end super-event image | generated symbolic/documentary | no gore, no generic monster horde. |
| Decision icons | icon artist | lighthouse, black cordon, evacuation train, blank ledger, unlit harbor, sealed chart. |
| Idea icons | icon artist | black shore, empty chair, counting ledger, white map orders. |
| Focus icons | icon artist | first shore, black tide, quiet census, unnamed ranks, no more maps. |
| Achievement icons | icon artist | lighthouse, intact island map, living compact seal, last ledger. |

Animation:

- Optional animated decision category seal: a black coastal line slowly swallowing a small white shoreline. Must use real source frames, not transform-only animation.
- Optional warning pulse for withering depth 3 in scripted GUI.
- Optional Zol portrait overlay only after world-end or Death player route. Do not animate Zol from the start; mystery is stronger when the portrait is nearly still.

Frame-animation handoff notes if accepted:

- Write a full animation brief per animated asset.
- Provide static fallback sprites.
- Use `frameAnimatedSpriteType` frame sheets.
- Do not use GIFs as final assets.
- Do not make final animation from a single shifted/recolored still.

## Source-Mode And Documentation Notes

If accepted into source specs, add sections for:

- Event flow and baseline phases.
- Death country package.
- Death focus tree architecture.
- Ordinary-country decision categories.
- State withering and consumption.
- Coalition system.
- Forbidden/necromancy route.
- Evolutions and super-events.
- Achievements.
- Asset manifest requirements.
- AI behavior.
- Cleanup and exploit checks.

Implementation surfaces likely affected:

- `events/010_*.txt` replacing obsolete War/Peace event.
- Event registration, event names, event logs, event details, and evolution catalog.
- `common/script_constants/010_death_constants.txt`.
- `common/scripted_effects/010_death_effects.txt`.
- `common/scripted_triggers/010_death_triggers.txt`.
- `common/decisions/010_death_decisions.txt` and category file.
- Death country history, characters, flags, and focus tree.
- Dynamic modifiers for Death states.
- Shared world-threat effects/triggers with `world_threat_source_death`.
- Super-event localisation, image, and audio package.
- Achievement tracking.
- Asset manifests under `docs/assets/010_death/` when assets are produced.
- Event docs and spreadsheet after implementation facts exist.

## What Should Not Be Added

Do not add:

- Zombie infection, corpse resurrection, bite mechanics, cure research, or named undead personalities.
- A normal Death ideology route where Zol runs elections, reforms, monarchism, communism, fascism, or diplomacy like a normal state.
- A large pantheon of death gods. Mythological references can name focuses or quotes, but Death should remain unknowable.
- A global plague system. Withering is territorial absence, not disease spread.
- Normal economic development for Death. Consumed industry becomes pressure, not factories.
- A huge necromancer country package for every nation. The forbidden path should be rare and costly.
- Cartoon skull UI, gore-heavy art, or monster-horde super-event images.
- Repeated super-events for every consumed capital. Use event log/evolutions for most milestones.
- Whole-world daily or weekly polling unless the parent explicitly approves it. Prefer scoped scheduled pulses and event-driven hooks.
- Instant full recovery of consumed states after Death is beaten. Recovery should be partial, slow, and mostly outside the main crisis loop.

## Acceptance Criteria For Parent Review

The accepted Death spec should be considered implementation-ready only when it defines:

- Origin state eligibility and failure fallback behavior.
- Phase progression, reveal triggers, and world-end conditions.
- Death tag, leader, country classification, starting spirits, and focus route architecture.
- State withering depth rules, state modifiers, population-death accounting, industry deletion, Death coring, and recovery cleanup.
- Ghost unit stages, spawn capacity, behavior, and exploit guards.
- Ordinary-country decisions, costs, missions, AI behavior, and clutter control.
- Coalition membership, formation, values, shared decisions, leadership transfer, and failure states.
- Forbidden/necromancy route reveal, costs, disqualifiers, AI limits, and betrayal outcomes.
- Dynamic tuning constants and MTTH entries.
- Evolution tracks, super-event roles, and achievement hooks.
- UI and asset families with source modes and animation requirements.
- Explicit list of rejected bloat items.

Recommended disposition: promote accepted portions into `docs/specs/010_death_specs/010 - Death.md` before implementation begins. Leave this plan in `docs/plans/010_death_plans/` as the improvement-loop handoff and mark it accepted, partially accepted, queued, or rejected in a parent note once reviewed.
