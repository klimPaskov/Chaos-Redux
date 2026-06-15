# Event 010 - Death

## Event Contract

| Field | Value |
| --- | --- |
| Event ID | `10` |
| Root event | `chaosx.nr10.1` |
| Event name | Death |
| Type | Minor Fire-Once |
| Cluster | No cluster |
| Primary actor | `DTH`, fixed country tag reserved for Death |
| Leader | Zol |
| Player-facing promise | A quiet island absence becomes a country, then a coastline, then a world condition. |

Death completely replaces the obsolete `Spirit of War/Peace` event. It has no lore, mechanical, or asset dependency on that event. Implementation must preserve Event ID `10` and namespace `chaosx.nr10`, but remove or replace the old War/Peace script, localisation, ideas, news entries, event-name mappings, event-log mappings, settings display, and spreadsheet row. Do not delete `GFX_report_event_war_or_peace` while Event 004 still uses it.

The source design is split across this package:

- `010 - Death.md`: source-of-truth event, systems, escalation, state, log, and implementation contract.
- `010_death_country_package.md`: Death tag, leader, country files, flags, units, AI, and defeat rules.
- `010_death_focus_tree.md`: Zol/Death focus-tree architecture.
- `010_death_decisions_ai.md`: ordinary-country decisions, missions, coalition, forbidden route, and AI rules.
- `010_death_assets_prompt.md`: asset and animation brief.
- `010_death_super_event_prompt.md`: super-event text, image, audio, and wiring brief.
- `010_death_achievements_prompt.md`: achievement hooks.
- `010_death_coding_prompt.md`: implementation prompt and touched-file checklist.
- `010_death_catalog_update.md`: spreadsheet/catalog update brief.
- `010_death_research_notes.md`: tone, source, and precedent notes.
- `010_death_goal_prompt.txt`: compact implementation goal prompt.

## Design Promise

Death should feel like a geographical fact that becomes a country because the engine needs a tag. At first there is only a black administrative oddity on a remote island: no government statement, no invasion report, no monster, no plague, no zombie horde. The world learns through absence. A lighthouse stops answering. A harbor sends no mail. An island remains on the chart but no longer has people attached to it.

The playable loop is therefore not "research a cure." It is noticing absence early enough, choosing whether to spend resources before proof exists, holding coasts and ports after proof arrives, and fighting a foe that does not occupy land so much as remove land from ordinary history.

Death must be dangerous because it was ignored, not because it begins as an unbeatable black superpower. A committed world can contain and destroy it before the mainland reveal. Delay, denial, poor coastline defense, and rising chaos make it impossible later.

## Non-Goals

Do not turn Death into any of these:

- a zombie outbreak or corpse-infection system
- a plague event or Black Death replacement
- a demon invasion with named monsters
- a normal political route where Zol runs ideology gameplay
- a large pantheon of death gods
- a normal country that uses factories, diplomacy, volunteers, guarantees, and advisors like everyone else
- a cure-race science minigame
- a gore-heavy or cartoon-skull presentation
- a silent replacement for unrelated Event 004 War/Peace assets

Ghost divisions are not undead characters. They are battlefield pressure made visible: weak, anonymous formations that appear where countries can no longer keep names attached to bodies.

## Required Implementation Principles

1. Death is event-driven and actor-scoped. Do not add whole-world `on_daily`, `on_weekly`, or similar all-country polling without explicit user approval.
2. If no valid remote island origin exists, Event 010 must not fire. Do not silently substitute a mainland start or an invalid island.
3. All thresholds, costs, cooldowns, weights, route modifiers, and unit counts belong in `common/script_constants/010_death_constants.txt` or MTTH variables. Do not scatter magic numbers across event, decision, focus, and effect files.
4. Death state population removal must register civilian deaths through the existing Chaos Meter death pipeline. Do not use `modify_state_population_by_percent` as the primary helper because its documentation says it still needs deaths-system integration.
5. Death-controlled consumed states are cored by Death to avoid resistance noise, but ordinary countries never receive instant full recovery or free cores after liberation.
6. Death does not gain normal factories from consumed states. Industry becomes abstract pressure and is then deleted or disabled.
7. Public reveal and world-threat registration are separate. Hidden island activity must not set `world_threat_source_death`; reveal and world-end stages must.
8. Death defeat is scripted full clearance, not ordinary surrender alone. A zero-surrender idea may support the fantasy, but completion checks must verify no active Death footholds, controlled consumed states, or pending world-end roots remain.
9. Fallbacks are not allowed. When an implementation cannot satisfy an eligibility rule, it should block, retry through an explicit scripted schedule, or surface a design blocker for review.

## Obsolete Event 010 Replacement

Implementation must replace these old War/Peace surfaces:

| Surface | Required action |
| --- | --- |
| `events/010_war_or_peace_symbol.txt` | Replace with `events/010_death.txt` or fully rewrite in place, keeping namespace `chaosx.nr10`. |
| `localisation/english/010_war_or_peace_symbol_l_english.yml` | Replace with `010_death_l_english.yml`; remove old `chaosx.nr10.*` and old `chaosx.news.7/8` wording. |
| `_chaosx_news.txt` | Remove or replace old War/Peace news `chaosx.news.7/8`; reserve new Death news IDs without colliding. |
| `symbol_of_war`, `symbol_of_peace` ideas | Remove if no other event uses them; verify references before deletion. |
| `GFX_news_symbol_of_war`, `GFX_news_symbol_of_peace` | Remove if no longer referenced. |
| `GFX_report_event_war_or_peace` | Keep while Event 004 uses it. |
| Event registry/comment | Keep fire-once ID `10`, update label to Death. |
| Event names/settings/debug/log selectors | Update Event 10 display from War/Peace to Death. |
| Event catalog workbook | Replace row 10 fields after implementation facts are final. Leave unrelated planned columns alone unless spreadsheet owner requests cleanup. |

## Country Identity

Death uses fixed tag `DTH`. Repo inspection found no current `DTH`, `DEA`, or `ZOL` country package in country tags, country files, history files, character files, name files, or English country localisation; implementation should rerun a full collision search immediately before adding the tag.

Core identity:

- Country name: Death.
- Adjective: Death.
- Leader: Zol.
- Map color: black or near-black, with enough UI contrast to select and read borders.
- Ruling party: The Stillness.
- Government UI: localized so it does not imply normal politics.
- Classification: special Chaos country and actual nonhuman country.
- Diplomacy: blocked from normal factions, guarantees, volunteers, ideology drift, and generic diplomacy.
- Start: no visible country until the event transfers the origin island.
- Economy: no normal industry loop; consumed industry becomes pressure variables.

Death gets a compact fixed-purpose country package and focus tree. It should not have a normal cabinet. Any "advisors" should be offices or absences such as `The Empty Chair`, `The Last Clerk`, `The Unlit Harbor`, and `The Bell Without Rope`.

See `010_death_country_package.md` and `010_death_focus_tree.md`.

## Baseline Flow

### Phase 0 - Eligibility And Island Selection

The event system may select Event 010 as a fire-once event only when all of these are true:

- `DTH` does not already exist on map.
- Event 010 has not fired and has not been disabled by settings.
- No other world-end branch is active unless the implementation explicitly allows Death as a world-end-compatible escalation.
- At least one valid origin state exists.

Origin state requirements:

- island state or one-state island group with no land border to a mainland
- coastal and reachable by sea-region logic
- not impassable
- not wasteland already
- low population under `constant:death_origin.population_cap_k`
- low industry under `constant:death_origin.industry_cap`
- not a national capital, player capital, or state containing a configured protected victory point
- not already controlled by another special nonhuman chaos country
- preferably remote from major-front land wars

If no valid origin exists, Event 010 is unavailable for the roll. It can be retried later by the event system if the availability trigger becomes true. It must not choose a mainland state as a substitute.

The root event saves the origin as an event target for the current chain and writes any persistent origin/candidate data through global variables or global event targets only if later events require persistence. Global event targets must be cleared on defeat, cleanup, or event cancellation.

### Phase 1 - The Island That Passes Inspection

Death receives the origin state, cores it, sets its capital there, applies `death_origin_island`, and gains the early spirits:

- `death_not_yet_a_country`
- `death_empty_administration`
- `death_black_shore`
- `death_the_counting`

No global news fires. Death has no starting divisions. Normal diplomacy and aggression remain suppressed.

The first public-facing clue is delayed by a hidden schedule, using MTTH or a delayed country event:

- Eligible observers are the former owner, nearest naval-base owner, a country with convoy routes or sea-region presence, a major naval country, or a country with high intelligence capacity.
- The clue does not name Death. It describes absence: no mail, no radio response, no lighthouse signal, no bodies, and no obvious invasion.
- Observer choices raise or lower `death_notice`, `death_silence`, and early containment access.

Representative early event names:

- `The Unanswered Light`
- `No Mail From [State.GetName]`
- `The Island Is Still On The Map`
- `A Weather Station Goes Quiet`

### Phase 2 - Silent Island Spread

Death consumes low-population islands through scoped scheduled pulses, not normal naval invasion gameplay. Target priority:

1. small islands in the same sea region
2. small islands in adjacent sea regions
3. neglected low-population islands owned by weak or distracted countries
4. islands whose owner ignored or concealed prior reports
5. higher-population islands only after low-population targets are exhausted

Boundaries:

- no player capital or major capital before reveal
- no state with active hostile divisions when that owner has begun investigation or containment
- no invalid, impassable, protected, or already consumed state
- no repeated consumption of the same state

Each consumed island:

- runs `death_consume_state`
- increments global consumed-state and consumed-population counters
- raises `death_silence`
- records a hidden event-log milestone if the event log system supports hidden-to-revealed evolution text
- may notify the owner or observer with ambiguous local text

Early countries can investigate. Investigation does not reveal Death by default; it exposes threatened sea regions or state flags and unlocks early defensive decisions.

### Phase 3 - Mainland Reveal

Death becomes public when any configured reveal trigger is true:

- Death consumes a mainland coastal state above `constant:death_reveal.mainland_population_k`.
- Death consumes a state with victory points above `constant:death_reveal.victory_point_threshold`.
- Death consumes a state controlled by a major, faction leader, or player.
- Cumulative consumed population exceeds `constant:death_reveal.consumed_population_k`.
- A coalition of investigators reaches `constant:death_reveal.notice_threshold`.

Reveal effects:

- fire reveal super-event `The Name On The Chart`
- set `death_revealed`
- set `world_threat_source_death`
- call `refresh_world_threat_state`
- replace early concealment spirits with revealed-stage spirits
- unlock ordinary-country Death decisions
- unlock Death post-reveal focus branch
- record event-log history and evolution detail
- enable scripted war declarations against valid land neighbors of consumed mainland states

After reveal, Death withers adjacent mainland states and can perform constrained coastal jumps. A coastal jump is not an uncontrolled escape hatch: it must consume Death pressure, respect cooldowns, select from valid coastal target arrays, avoid protected states, and fail cleanly if no valid target exists.

### Phase 4 - Containment War

The main ordinary-country loop is defensive logistics:

- hold named coastal belts and ports
- keep supplied divisions in watched and withering states
- run cordon, evacuation, lighthouse, and naval-patrol missions
- spend convoys, trains, trucks, support equipment, infantry equipment, fuel, command power, political power, army XP, and stability
- decide whether to form a compact or preserve national control
- decide whether forbidden study is worth achievement disqualification and internal damage

Death advances by:

- consuming under-defended adjacent states
- raising withering depth when defense score loses to Death pressure
- selecting new coastal footholds on cooldown when pressured off a coast
- converting consumed population and deleted industry into pressure, ghost capacity, and route upgrades

Death is still beatable here. If all Death states and footholds are occupied and the origin clearance mission succeeds, Death is defeated and the aftermath branch fires if the crisis was public or severe enough.

### Phase 5 - Continental Threat

Death enters continental-threat status when it controls or consumes a configured share of a continent, consumes a configured number of mainland states, or consumes a configured population threshold after reveal.

Effects:

- record `death_continental_threat`
- intensify coalition and frontline AI urgency
- unlock higher ghost stage if the consumed population supports it
- allow coastal-shadow targeting inside threatened sea regions
- make Living Compact formation easier
- unlock Black Shore Conference events
- raise dread and stability pressure in threatened countries

This phase is an evolution milestone, not automatically world-end. It becomes world-end only when the global Chaos Redux world-end condition is also met.

### Phase 6 - World-End Escalation

Death world-end requires all of these:

- `world_end` is not already set.
- global chaos meets the established world-end threshold, represented in implementation through the shared chaos-meter constant or existing world-end gate.
- Death has consumed an entire continent, enough mainland states, or enough population according to Death constants.
- Death is not defeated or contained by an active successful clearance mission.

World-end effects:

- set `world_end`
- set `world_end_death`
- set or keep `world_threat_source_death`
- refresh world-threat state
- fire world-end super-event `No More Shores`
- seed footholds on every valid continent through explicit coastal target selection
- spawn world-end ghost formations scaled by consumed population and chaos tier
- switch Death AI from pressure/containment testing to aggressive world consumption
- unlock emergency ordinary-country decisions and continent-clearing missions

Foothold selection must avoid impassable states, invalid unowned states, protected capitals unless reveal/world-end rules allow them, already consumed states, and states that would break ownership transfer or state-scope effects.

### Phase 7 - World Consumed

If Death controls or has consumed every valid state, fire terminal super-event `The Last Entry` and grant the Death victory achievement. This is not a normal conquest win. It records:

- final consumed-state count
- final recorded civilian deaths
- final Death pressure and ghost stage
- final event-log terminal entry
- shutdown or disabling notes for incompatible random events that require living ordinary countries

Zol should remain unexplained. If the player is Death or the world is gone, the UI may show Zol's final portrait/title. Otherwise the postwar text treats Zol as a name governments used because they needed a field to fill in.

## State Withering And Consumption

Death states use a staged state progression. The progression must be visible through decisions, event details, scripted localisation, or map-state indicators after reveal.

| Depth | Public state | Role |
| --- | --- | --- |
| 0 | Watched Shore | Neighboring Death, listed target, or at-risk sea region. Enables cordon and investigation. |
| 1 | Withering Shore | Local defenses are insufficient. Movement and supply penalties begin. |
| 2 | Black Cordon Failure | Cordon failed or Death pressure wins repeated pulses. Attrition and damage become severe. |
| 3 | Emptying State | Evacuation window is closing. Population-loss ticks and industry damage begin. |
| 4 | Consumed Wasteland | State is removed from normal play, cored by Death, and counts toward Death power. |

### Defense Score

Defense is not a single division check. Calculate or approximate a score from:

- supplied divisions present
- forts and coastal forts
- port, rail, supply hub, and infrastructure status
- active cordon decision
- active evacuation mission
- coalition support
- naval patrol in adjacent sea region
- owner stability and command power
- owner proximity and war state
- withering-depth penalty

### Death Pressure Score

Death pressure comes from:

- consumed population
- consumed state count
- Death route
- chaos tier
- ghost stage
- adjacent Death states
- coastal-shadow eligibility
- failed containment history
- high global dread
- deleted industry converted into pressure

If defense wins, withering stalls or regresses one depth. If Death wins, depth advances. The exact comparison should use MTTH variables or scripted scoring helpers so decision AI and Death pulses use the same numbers.

### `death_consume_state`

Create a reusable state-scope effect `death_consume_state` in `common/scripted_effects/010_death_effects.txt`.

Required behavior:

1. Validate the current state is eligible and not already consumed.
2. Save pre-consumption population, owner/controller, victory points where needed, and industry totals into variables.
3. Register civilian deaths through the Chaos Meter civilian-death framework, with a new Death cause line.
4. Convert deleted industry and infrastructure into Death pressure variables.
5. Delete or fully disable civilian factories, military factories, dockyards, naval bases, air bases, supply nodes, railways, forts, coastal forts, anti-air, radar, reactors, refineries, silos, and other state buildings covered by local precedent.
6. Set `death_consumed_state` and route/phase flags.
7. Set state category toward `wasteland` where valid.
8. Add `DTH` core.
9. Transfer or control the state for Death according to the phase.
10. Apply `death_consumed_wasteland` dynamic modifier.
11. Clear watched/withering/mission flags from that state.
12. Increment global and actor counters.
13. Call reveal/evolution/world-end checks.

Do not reverse recorded deaths on liberation.

### Death Dynamic Modifiers

Create Death state dynamic modifiers in a new file such as `common/dynamic_modifiers/010_death_state_modifiers.txt`.

Needed modifiers:

- `death_watched_shore_state`: mild warning and decision visibility support.
- `death_withering_shore_state`: movement, supply, and organization penalties for non-Death forces.
- `death_emptying_state`: severe local damage, attrition, and evacuation pressure.
- `death_consumed_wasteland`: extreme supply, movement, attrition, local industry, local manpower, and recovery lock.
- `death_recovered_wasteland`: post-defeat scar state; not instant normal recovery.

Strength loss for divisions lingering in Death states should be implemented through scoped state/front pulses or targeted events, not whole-world polling.

## Ghost Divisions

Ghost units progress through three stages.

| Stage | Unlock | Behavior |
| --- | --- | --- |
| Pale Companies | around the 600-tier equivalent or configured consumed-population threshold | very weak, low org, low HP, low attack, border-holding only |
| Mute Regiments | around the 800-tier equivalent or post-reveal high consumed population | more numerous, still weaker than infantry, local counterattacks |
| Final Muster | world-end only | comparable to basic infantry, aggressive battle plans |

Rules:

- Spawn capacity derives from consumed population, consumed states, route, and chaos tier.
- Capacity is capped per state/front.
- Recapture/control toggles cannot duplicate units.
- Ghosts should not provide useful equipment or manpower farming rewards.
- If a custom unit is used, register icons and unit localisation. If equipment archetypes are added, update `common/script_enums.txt`.
- Ghost templates should be locked and spawned by scripted effects; ordinary countries must not recruit them.

## Ordinary-Country Response

Ordinary-country mechanics are in `010_death_decisions_ai.md`.

Required response families:

- Missing Islands File: early observer decisions and missions before reveal.
- Black Shore Containment: state-targeted cordon, evacuation, patrol, and denial decisions.
- Living Compact: coalition/compact formation, cohesion, command, equipment pooling, leadership transfer, and failure states.
- Forbidden Files: necromancy/study route with severe costs and achievement disqualifiers.
- Anti-Death War Logistics: offensive clearance missions and support actions.

Early information should matter. A country that investigates before reveal gets better containment access but pays political, stability, or resource costs for acting on unconfirmed reports.

## Living Compact

The Living Compact is a crisis compact, not necessarily a normal faction replacement. Prefer an additive decision/faction-rule layer unless implementation proves a template-backed faction is cleaner.

Formation requirements:

- Death revealed.
- At least one mainland state consumed or configured consumed-population threshold reached.
- Candidate leader is not Death, not a nonhuman chaos country, not capitulated, and not blocked by subject rules.
- Candidate leader is a major, a regional threatened country, a faction leader, or has completed enough containment actions.
- Enough threatened countries are willing to join, or a major/faction leader sponsors the compact.

Values:

- `living_compact_cohesion`: affects shared costs, AI willingness, and failure events.
- `living_compact_command`: affects frontline missions and coordinated offensives.
- `death_public_dread`: rises with consumed population and visible failures; helps formation but hurts stability.

Failure states:

- low cohesion blocks shared offensives
- high dread without cohesion causes panic events and refusal
- leader capitulation transfers leadership to the highest-valid member or triggers emergency mode

## Forbidden Route

The forbidden route lets countries study, bargain with, or petition Death. It must be rare, costly, and ugly.

Unlock pressure:

- Death revealed
- high chaos
- severe casualties or territorial losses
- low stability
- occult/high-chaos route flags from other systems
- extremist or desperate government
- no viable coalition path

Player route options:

1. Study Death to fight it: better containment, internal dread, intelligence exposure.
2. Use forbidden logistics/rites: sacrifices manpower, stability, war support, or local population to slow Death.
3. Petition Zol: terminal betrayal or challenge path; the country becomes a marked client, not a normal ally.

AI must almost never petition Death. AI forbidden study should require severe local threat and lack of viable coalition support.

## Death AI

Death AI phases:

- hidden: passive, no normal war justifications, low-population island target pulses only
- revealed: scripted declarations on valid neighbors, withering and bounded coastal jumps
- continental: pressure routes and local ghost counterattacks
- world-end: aggressive plans and continent foothold expansion

Route selection:

- Quiet Census: isolated origin, many island targets, strong need for stealth.
- Black Tide: island chains and weak naval containment.
- Still Front: early mainland foothold or strong adjacent land-front opportunities.

AI must not consume a protected major/player capital before reveal. After reveal/world-end, protected status changes only through explicit scripted rules.

## Dynamic Values

Create `common/script_constants/010_death_constants.txt` with grouped constants:

- `death_origin`: island eligibility caps and protected-state rules
- `death_rumor`: delay bands and observer weights
- `death_reveal`: population, victory point, consumed population, and notice thresholds
- `death_spread`: island and coastal jump cooldowns by route/phase
- `death_withering`: depth thresholds, regression rules, and pressure weights
- `death_defense`: score weights for divisions, forts, ports, patrols, and coalition support
- `death_consumption`: civilian-death ratios, industry conversion, and building deletion severity
- `death_ghosts`: stage thresholds, capacity, and unit counts
- `death_compact`: cohesion, command, dread, formation, and failure thresholds
- `death_forbidden`: temptation weights, costs, and disqualifiers
- `death_world_end`: continent, population, chaos, and foothold thresholds

Use explicit fixed-point access such as `constant:death_reveal.mainland_population_k`. For effect fields that do not parse constants, assign the constant to a normal or temporary variable first.

Use MTTH variables for:

- early rumor firing
- island target selection weights
- reveal acceleration
- Death route and focus AI
- AI containment decisions
- coalition joining and leadership
- forbidden temptation
- world-end readiness pacing

## Event Log And Evolutions

Event 010 needs full event-log and event-detail integration.

Baseline event details:

- before reveal: public text says the event is unresolved and mentions only confirmed disappearances if the viewer has observer flags
- after reveal: details name Death, Zol, known consumed population, known threatened regions, and current public phase
- world-end: details explain that Death is no longer a regional actor and list continent footholds
- defeated: details preserve scars, civilian death count, and unresolved origin notes

Evolution tracks:

| Track | Stages |
| --- | --- |
| `death_public_reveal` | The Name On The Chart; The Black Shore |
| `death_ghost_muster` | Pale Companies; Mute Regiments; Final Muster |
| `death_containment_failure` | First failed mainland cordon; first consumed capital or major port; first continent lost |
| `death_forbidden_compacts` | first study; first forbidden containment; first petition/client |
| `death_world_end` | footholds on every continent; final consumed continent; world consumed |

Actors:

- Death for spread, reveal, ghost, and world-end milestones.
- Living Compact leader for coalition milestones.
- Betraying or forbidden-study country for forbidden milestones.
- Former owner or observer for early island report milestones when Death is still hidden.

## Super-Events

Super-event details are in `010_death_super_event_prompt.md`.

Required super-events:

| Role | Title | Trigger |
| --- | --- | --- |
| Reveal | The Name On The Chart | First valid mainland/populous/major/player reveal |
| Compact | The Living Compact | First successful compact formation with sufficient membership |
| World-end | No More Shores | Death world-end branch |
| Defeat aftermath | The Shore Returns Empty | Death defeated after public/severe crisis |
| World consumed | The Last Entry | All valid states consumed/controlled by Death |

Quote package:

- Reveal: Jeremiah 9:21 KJV, "For death is come up into our windows..."
- Reveal button: Isaiah 21:11 KJV, "Watchman, what of the night?"
- World-end: Revelation 8:1 KJV, "there was silence in heaven..."
- World-end button: Milton, `Paradise Lost`, "Darkness visible"
- Defeat aftermath: Emily Dickinson, "After great pain, a formal feeling comes -"
- Defeat button: Isaiah 21:12 KJV, "The morning cometh, and also the night."

Audio still needs a dedicated `chaosx_super_event_audio_researcher` pass before implementation. Do not wire placeholder audio.

## Achievements

Achievement details are in `010_death_achievements_prompt.md`.

Achievement themes:

- discovering Death early
- preventing mainland reveal
- forming and preserving the Living Compact
- defeating Death without forbidden decisions
- surviving as a small island country
- using forbidden study to win at a moral cost
- serving Death as a marked client
- consuming the world as Death

Each achievement needs a custom icon, `.gfx` sprite aliases, localisation, and a precise trigger/flag lifecycle.

## Asset Direction

Asset details are in `010_death_assets_prompt.md`.

Style:

- period-compatible, austere, documentary or symbolic
- black coasts, empty harbors, missing lighthouse crews, covered charts, unlit offices
- no gore focus
- no cartoon skull language
- no generic monster horde
- no real-person portrait for Zol

Animated assets are optional but must follow the frame-animation workflow: real source frames, horizontal frame sheet, static fallback, contact sheet, manifest, and `.gfx` handoff. Final animation must not be made only by shifting, rotating, recoloring, blurring, or warping a single still image.

## Implementation Touchpoints

The coding prompt lists the full checklist. Core files likely include:

- `events/010_death.txt`
- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `common/decisions/010_death_decisions.txt`
- `common/national_focus/010_death_focus_tree.txt`
- `common/country_tags/chaosx_countries.txt`
- `common/countries/DTH - Death.txt`
- `history/countries/DTH - Death.txt`
- `common/characters/DTH.txt`
- `common/ai_strategy/DTH.txt`
- `common/factions/templates/living_compact.txt` if template-backed compact is chosen
- event registry, settings, debug, event-log, event-detail, world-threat, special-country classifiers, triggerable scenario, super-event, achievement, localisation, interface, and spreadsheet surfaces

## Completion Criteria For Implementation

Implementation is not complete until all of these are done:

- obsolete War/Peace Event 010 is fully removed or replaced
- Death country package exists and is registered
- root event, hidden origin, spread, reveal, world-end, defeat, and world-consumed branches are wired
- state consumption registers civilian deaths and deletes/locks state industry
- decisions, missions, coalition, forbidden route, and AI are localized and have tooltips
- focus tree is real, routed, AI-weighted, and non-generic
- world-threat, event-log, event-detail, evolution, super-event, triggerable-scenario, and achievement systems are aligned
- assets are registered and placeholder sprites are copied where final art is not ready
- spreadsheet/catalog row is updated after implementation facts are stable
- no whole-world polling was added without explicit approval
- no unsupported operators or dynamic-value-invalid fields are used
- all dynamic helpers added to `chaosx_dynamic_effects.txt` are documented in `chaosx_dynamic_effects.md`
- audit subagents have reviewed the country package, focus tree, decisions/missions, localisation, and event completion

## Accepted Planning Handoff

`docs/plans/010_death_plans/010_death_deep_expansion_addendum.md` is accepted as the improvement-loop handoff for this spec. Its research anchors and mechanical expansion have been promoted into this source package; remaining open work is implementation, asset production, audio research, and final audits.
