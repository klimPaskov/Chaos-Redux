# 007 Fury spec, part 2: evolutions, world-end, and presentation

## Baseline stages and evolutions

Fury has ordinary stages and separate evolutions.

Ordinary stages are:

1. selection.
2. first war.
3. first conquest.
4. repeated neighbor wars.
5. major threshold or collapse.
6. no-neighbor branch.
7. world-end eligibility.

Evolutions are not these stages. Evolutions change how future Fury actors appear and how existing Fury actors behave.

Each evolution supports two entry paths.

| Entry path | Meaning |
| --- | --- |
| Active-event evolution | A Fury actor already exists, and the evolution changes that actor immediately |
| Pre-fire evolved opening | A future first firing starts in a stronger or stranger form because the world is already unstable |

## Evolution I: Hardened Fury

Working log name: `Hardened Fury`.

### Role

The first evolution makes the Fury pattern more professional. It does not add more Fury countries. It makes the existing or next Fury actor harder to stop.

### Possible conditions

Active-event entry can occur when:

- a Fury actor wins its first war and still has momentum.
- a Fury actor survives beyond an early duration band.
- a Fury actor defeats a target that had more industry than expected.
- a Fury actor completes early military or depot focuses.
- chaos value and war pressure make the pattern more severe.

Pre-fire evolved opening can occur when:

- Fury has fired before in the campaign.
- a previous Fury reached first conquest.
- chaos tier is higher.
- the Wars cluster has fired repeatedly.
- many AI minors have been defeated by sudden wars.

### Active-event effects

If a Fury actor already exists, Evolution I should:

- upgrade `National Fury` into `Hardened Fury`.
- improve reserve-spawned unit quality and slightly increase the capped reserve pool.
- unlock hardened military focuses.
- unlock depot seizure decisions.
- unlock better target-preparation decisions.
- add a small compliance drive boost.
- raise the AI desire to finish current wars.
- avoid resetting the Fury actor or restarting its current war.

### Pre-fire evolved opening

If Fury has not fired yet in the current active cycle, the first Fury opens with:

- a stronger starting army.
- better template families.
- slightly larger equipment stockpile and capped hidden reserve pool.
- the `Hardened Fury` idea at start.
- first expansion branch focuses unlocked earlier.
- higher chance to choose a target with two states rather than only one.
- the same player exclusion rules.

### Focus tree unlocks

Evolution I unlocks:

- `Harden the Columns`.
- `Depot Officers Without Leave`.
- `Forced March Tables`.
- `The Second Border Is Already Drawn`.
- `Occupation as Recruitment`.
- `No Clerk Can Stop The War Office`.

These are focus directions, not final focus counts.

### Gameplay limits

Evolution I should not make Fury instantly unbeatable. It should improve the quality of the first war and make repeated wars more likely, while leaving overextension and containment meaningful.

## Evolution II: Two Fires

Working log name: `Two Fires`.

### Role

The second evolution makes Fury no longer unique. Two Fury actors can appear at the same time. Cooperation mechanics become available when they are not hostile to each other.

### Possible conditions

Active-event entry can occur when:

- one Fury actor becomes locally secure.
- one Fury actor has won two wars.
- a Fury actor has no immediate neighbor but has not reached world-end conditions.
- another eligible minor exists on a different border region.
- chaos and active Wars cluster pressure are high enough.

Pre-fire evolved opening can occur when:

- the event fires after Evolution II is enabled.
- the custom scenario chooses medium or higher intensity.
- a previous Fury actor became a major.
- the world already has high war density.

### Active-event effects

If one Fury actor already exists, Evolution II should:

- select a second eligible AI minor.
- prefer a different region or continent from the first Fury.
- initialize the second Fury with the current evolution level.
- unlock Fury-to-Fury diplomacy decisions.
- enable pact or rivalry logic depending on type.
- add Fury Pact Cohesion if the actors cooperate.
- add target-partition decisions if both actors are near the same region.

### Pre-fire evolved opening

A new Fury cycle begins with two Fury actors.

Selection rules:

- avoid selecting countries that share the same immediate target pool if possible.
- avoid selecting any player country or player-linked country.
- avoid placing both Fury actors where one will destroy the other in the first month unless the type is hostile.
- if only one safe candidate exists, fire one Fury and record that the second slot could not be safely filled.

### Cooperation mechanics

If the Fury type is pact or ordinary cooperative mode, Fury actors can:

- join the same Fury faction after a threshold.
- share target warnings.
- send volunteer-style reinforcement packages to the weaker Fury.
- coordinate wars against non-player AI states.
- partition conquered land by continent or claimed front.
- use joint decisions to reduce overextension.

If the Fury type is hostile, Fury actors can:

- treat each other as valid targets only after they run out of smaller neighbors.
- gain momentum from defeating another Fury.
- suffer pact cohesion penalties because no pact exists.
- unlock rivalry focuses instead of cooperation focuses.

### Focus tree unlocks

Evolution II unlocks:

- `The Other Fire Answers`.
- `Officers Across The Border`.
- `Shared War Tables`.
- `Partition Before Victory`.
- `Two Capitals, One Map`.
- `When Fury Meets Fury`.
- `Deny The Other March`.

These focuses are split between pact and hostile paths.

## Evolution III: All Borders at Once

Working log name: `All Borders at Once`.

### Role

The third evolution turns Fury from sequential local conquest into broad border rupture. Three Fury actors can appear. Each Fury country is stronger and can declare on all valid neighbors at once.

### Possible conditions

Active-event entry can occur when:

- a Fury actor becomes a major.
- two Fury actors both win wars.
- a Fury actor reaches no-neighbor state on its continent.
- world tension and chaos are high.
- the Wars cluster has produced repeated conflicts.
- the custom scenario uses high or maximum intensity.

Pre-fire evolved opening can occur when:

- Evolution III is already enabled.
- the custom scenario uses high or maximum intensity.
- a previous Fury major existed.
- the world has already entered a severe chaos state.

### Active-event effects

If Fury actors already exist, Evolution III should:

- select up to three total Fury actors.
- upgrade all active Fury ideas.
- improve reserve-spawned unit quality and starting stockpiles within capped pools.
- unlock all-neighbor declaration logic.
- unlock high-chaos focus branches.
- allow Fury actors to attack all valid neighbors at once.
- strengthen occupation and coring tools to keep the loop moving.
- increase overextension sharply to keep the system from becoming a free win.
- raise anti-Fury response availability.

### Pre-fire evolved opening

A new Fury cycle begins with three Fury actors if enough safe candidates exist.

Opening rules:

- choose different regions or continents where possible.
- exclude players and player-linked countries.
- initialize each with a stronger package.
- use all-neighbor declaration only after a short preparation delay unless scenario maximum intensity explicitly starts immediately.
- fire a stronger global report after the first set of declarations.

### All-neighbor declaration rules

Evolution III Fury declares on every valid neighbor at once.

Valid targets still exclude:

- countries already in direct player wars if transfer logic would interfere.
- targets that would create an immediate world war unless the terminal branch is active.

Fury should not declare on a much stronger neighbor just because it shares a border. Each target must pass a scaled validity check. A local major can become valid only if Fury has reached major threshold or terminal state.

## Evolution logging

Each evolution should record a real evolution entry.

Suggested event log fields:

| Evolution | Stage | Chaos Tier | Actor |
| --- | --- | --- | --- |
| Hardened Fury | 1 | Gatherig Storm | strongest Fury actor |
| Two Fires | 2 | Rising Chaos | strongest Fury actor |
| All Borders at Once | 3 | Chaos Tier | strongest Fury actor |

Disabled evolutions must not unlock their branches, spawn additional Fury actors, or set recorded flags that later systems read.

## World-end branch: The World in Fury

The terminal world-end branch uses the same name as the triggerable scenario, but they are separate systems.

The triggerable scenario is a manual setup. The world-end branch is a terminal campaign state.

### World-end role

The world-end branch begins when Fury has stopped being a local pattern and becomes the operating rule of the world. A main Fury actor has no valid local neighbors left or has become a large power, then exports the Fury pattern to other continents. Minor countries in other continents become Fury and join the main Fury faction.

### Eligibility

The terminal branch should require:

- no existing world-end state.
- world-end chaos threshold.
- at least one active Fury actor.
- a main Fury actor that is major, continent-dominant, or has no valid continental neighbors.
- the relevant world-end focus or no-neighbor branch completed.
- enough eligible AI minors in other continents to spread the pattern, or a visible blocked outcome if too few exist.

### World-end opening effects

When the branch starts:

1. set the global world-end state.
2. set a Fury-specific world-end flag.
3. identify the main Fury actor.
4. create or rename the Fury faction as the main Fury faction.
5. seed Fury actors in other continents.
6. make seeded Fury actors join the main Fury faction.
7. give seeded Fury actors a stronger evolved opening.
8. unlock world-end focus branch for all Fury actors.
9. warn player countries before any terminal player threat can be enabled.
10. fire the world-end super-event.

Current implementation note: `fury_try_start_world_end` and `fury_start_world_end` provide the first terminal starter. The branch sets `world_end`, `world_end_fury`, `fury_world_end_active`, `world_threat_source_fury`, creates `The World in Fury`, seeds safe AI Fury actors across unrepresented continents first, fills toward the required terminal actor count, and reports `fury_world_end_seed_blocked` if the safe seed pool is insufficient.

### Continental spread

The branch should try to seed one Fury actor per continent first.

Priority order:

1. continents with many small AI minors.
2. continents without an active Fury actor.
3. continents with high war density.
4. continents where a Fury actor can reach valid targets.
5. continents near the main Fury faction's strategic path.

After each continent has at least one Fury actor or no safe candidate, the branch can create additional Fury actors if the terminal state demands more pressure.

### Fury faction

Working name directions:

- `Fury Pact`.
- `The World in Fury`.
- `March Pact`.
- `Borderless War Office`.

The faction should not be a normal ideological bloc. It exists to coordinate the Fury pattern.

Faction behavior:

- Fury members do not onlyify ordinary diplomacy.
- Fury members prefer war coordination and partition targets.
- Fury members share limited reserve decisions.
- Fury members do not accept ordinary peace with target states while terminal state is active.
- Fury members can compete for conquered land, but the main Fury actor remains faction leader unless defeated.

Current implementation note: the terminal starter leaves any prior faction, creates `The World in Fury`, adds active and seeded Fury actors to the leader's faction, and flags them with `fury_pact_member` and `fury_world_end_actor`. Terminal actors can use `fury_share_terminal_reserves` to move manpower and equipment to another terminal Fury actor, and `fury_assign_terminal_fronts` to raise pact cohesion, target preparation, momentum, and overextension relief across the terminal pact.

### Terminal targeting rules

The world-end branch may eventually threaten player countries beyond the ordinary neighbor loop, but this should be a terminal state with clear warning. The ordinary neighbor loop can still target player-controlled countries when they meet normal target gates.

Terminal target rules:

- ordinary valid targets can be AI or player-controlled countries.
- terminal out-of-neighbor threats still use warning and delay before direct player pressure.
- the player should receive warning events and response tools.
- Fury does not give the player the Fury package even if the player is in the faction through unusual modded conditions.
- subject and faction logic must avoid stealing player-controlled peace outcomes.

Current implementation note: `chaosx.nr7.50` warns all player countries and `fury_player_warning_grace_active` marks the grace period. Ordinary target selection can hit player-controlled countries that meet the normal target gates. After the grace flag expires, world-end actors that have no valid neighbor can use `fury_terminal_can_threaten_player_linked_country` through `fury_try_terminal_player_target`, which sends `chaosx.nr7.52` before the direct terminal war declaration.

### World-end failure and defeat

If all Fury actors are defeated during the terminal branch:

- fire a defeat aftermath report or super-event if the war was large enough.
- remove Fury world-threat source.
- close Fury expansion decisions.
- remove or downgrade temporary anti-Fury ideas after a delay.
- keep scars such as reconstruction decisions or memorial ideas only if the campaign cost was high.

## Super-events

Fury needs two planned super-events and one optional aftermath super-event.

### Super-event 1: A Fury country becomes a major

Role: escalation.

Trigger: first active Fury actor becomes major or crosses the Fury major threshold.

Tone: the world realizes a local border anomaly has become a power.

Image direction: period-style super-event image of a small capital war room, maps covering walls, officers and clerks moving without a clear leader, no readable generated text.

Quote direction: real historical or literary quote about unchecked expansion, force becoming policy, or borders losing meaning. Use super-event research workflow before final selection.

Button direction: cold and short. Example direction: `The map keeps moving`.

Current implementation note: slot `59` uses generated final image art at `gfx/super_events/fury_becomes_a_state.dds`, with source and processed PNGs under `docs/assets/007_fury/super_events/fury_becomes_a_state/`. Its final sourced audio uses ID `59`, `music/fury_becomes_a_state.ogg`, and `sound/chaosx_super_event_fury_becomes_a_state.wav`; source and license details are recorded in `docs/super_events/super_event_audio_packages.md`.

### Super-event 2: The World in Fury

Role: world-end reveal.

Trigger: terminal branch begins.

Tone: the pattern is no longer contained by continent or region.

Image direction: global map room with multiple small flags, radio operators, dispatch sheets, and a central table. No modern screens. No readable generated text.

Quote direction: real quote about war spreading through imitation, the end of order, or the logic of force. Use super-event research workflow.

Button direction: short and terminal. Example direction: `Every border is a front`.

Current implementation note: slot `60` uses generated final image art at `gfx/super_events/super_event_world_in_fury.dds`, with source and processed PNGs under `docs/assets/007_fury/super_events/world_in_fury/`. Its final sourced audio uses ID `60`, `music/super_event_world_in_fury.ogg`, and `sound/chaosx_super_event_world_in_fury.wav`; source and license details are recorded in `docs/super_events/super_event_audio_packages.md`.

### Optional super-event 3: Fury defeated after terminal branch

Role: aftermath.

Trigger: all Fury actors defeated after a long terminal crisis or after the Fury faction held enough states to reshape the campaign.

Tone: tired relief, not clean victory.

Image direction: abandoned border office, burned maps, officials restoring archives, soldiers guarding checkpoints.

Quote direction: real quote about rebuilding order after war or the cost of victory.

Button direction: restrained. Example direction: `Count what remains`.

## News and report events

Fury should include a small set of non-super-event presentation beats.

| Beat | Scope | Purpose |
| --- | --- | --- |
| Fury appears | hidden or local report | nearby states may notice mobilization if they are close |
| First declaration | optional report | only shown if the player is near, guaranteeing, or intelligence-aware |
| First conquest | global news | reveals Fury pattern |
| Fury stalls | report | shows overextension, resistance, or supply problems |
| Fury defeated | news or report | closure if the actor had at least one conquest |
| Fury becomes major | super-event | escalation |
| No-neighbor branch | report | hints that Fury has reached the edge of its continent |
| World in Fury | super-event | terminal branch |

## World threat framework

When Fury becomes major or the world-end branch begins, it should become a world threat source.

Suggested source flag direction:

- `world_threat_source_fury`.

Activation:

- active while a Fury major exists.
- active while world-end Fury branch exists.
- inactive when all major or terminal Fury actors are defeated.

Effects on other systems:

- future cooperation mechanics can read the shared `world_in_threat` flag.
- anti-Fury player decisions can unlock from the source flag.
- other hostile event systems can avoid nonsensical cooperation with Fury.

## Anti-Fury response layer

The baseline event does not need a large global anti-Fury system. It should stay minor repeatable until escalation. However, once Fury becomes major or world-end begins, other countries need limited response tools.

Response families:

| Response | Who can use it | Purpose |
| --- | --- | --- |
| Firebreak Guarantees | AI and player neighbors | deter the next Fury war without giving free land |
| Border Watch Missions | countries bordering Fury | place divisions in border states by a deadline |
| Supply Denial | countries near Fury | reduce Fury reinforcement quality if rail or supply hubs are held |
| Recognition Denial | majors and regional powers | slows Fury diplomatic reach and pact cohesion |
| Coalition Staff Talks | non-Fury countries | limited cooperation only after major-Fury threshold |
| Emergency Aid to Target | majors and nearby countries | send equipment to a Fury target without joining the war |

These should use concrete costs like equipment, convoys, army XP, command power, relations, border divisions, and stability risk. Avoid a list of political power buttons.

## Interactions with other Chaos Redux events

Fury should interact with existing systems only where the connection matters.

Suggested connections:

| System | Interaction |
| --- | --- |
| Random War | Fury belongs to Wars cluster and should not duplicate a Random War on the same target in the same short window |
| Independence Wave | newly released tiny countries can become Fury later if they meet eligibility and cooldown rules |
| Soviet Collapse | breakaway republics can become Fury only if they are AI, small, and not protected by special collapse logic |
| Holy Realm | Holy Realm and similar special tags should be excluded unless a future route explicitly allows it |
| Zombie or non-human countries | excluded from Fury selection and ordinary target selection if their systems require special handling |
| World threat | Fury major and world-end Fury use the shared world-threat state |
| Triggerable scenarios | The World in Fury scenario bypasses normal random timing but still uses safe player exclusion |

## Containment and collapse

Fury can fail.

Failure routes:

| Failure | Cause | Result |
| --- | --- | --- |
| Quick defeat | Fury loses first war or capitulates early | remove Fury package |
| Overextension stall | resistance, supply, and non-core land exceed momentum | pause target selection, raise internal crisis |
| Target reversal | target survives and counterattacks | Fury loses momentum and reserve-spawned unit quality |
| Fury civil fracture | high overextension with hostile Fury type | chance of an internal collapse event or splinter penalties |
| Pact dispute | multiple Fury actors compete for same region | cohesion loss or rivalry branch |
| Terminal defeat | all Fury actors destroyed after world-end | aftermath package |

A Fury defeat should not erase the event from history. It should remain and should contribute to future evolution memory only if it reached meaningful milestones.

## Cleanup

Cleanup must cover:

- finite reserve pulse flags and reserve variables.
- Fury ideas.
- Fury decisions and active missions.
- target event targets.
- pact membership helpers.
- active Fury arrays or variables.
- no-neighbor state.
- overextension variables.
- hidden scenario bypass flags.
- world-threat source flag.
- focus tree handling where reversible.
- anti-Fury decisions after a delay.

Cleanup should not remove ordinary conquered territory automatically unless a separate peace or defeat effect says so. If Fury conquered land and then became a normal country after defeat of its Fury system, the map state should be handled through peace and aftermath logic, not hidden rollback.
