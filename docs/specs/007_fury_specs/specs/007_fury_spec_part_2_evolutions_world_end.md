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

Evolutions are not these stages.
Evolutions change how future Fury actors appear and how existing Fury actors behave.

Each evolution supports two entry paths.

| Entry path | Meaning |
| --- | --- |
| Active-event evolution | A Fury actor already exists, and the evolution changes that actor immediately |
| Pre-fire evolved opening | A future first firing starts in a stronger or stranger form because the world is already unstable |

Current unlock rule: `fury_sync_evolution_unlocks` unlocks Evolution I, II, and III at Chaos Meter tiers 1, 2, and 3 respectively, and only while that stage's evolution checkbox is enabled.
The weekly actor tick and `chaosx.nr7.40` then apply an unlocked stage to every existing actor, and new actors open with every unlocked stage.
Manual intensity may bypass the tier gate but never a disabled checkbox.
The "possible conditions" lists below are design intent for weighting and presentation; they are not separate gates in the current implementation.
A proposal to make actor milestones decide the active-event application is recorded in the README's open questions.

## Evolution I: Hardened Fury

Working log name: `Hardened Fury`.

### Role

The first evolution makes the Fury pattern more professional.
It does not add more Fury countries.
It makes the existing or next Fury actor harder to stop.

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

If a Fury actor already exists, Evolution I currently:

- replaces `National Fury` with `Hardened Fury`, including its five-point recruitable population bonus.
- adds momentum, which enlarges later direct waves.
- opens the `Hardened Doctrine` focus branch, whose `Depot Officers Without Leave` adds finite reserves.
- raises later direct-wave size and the target-score evolution bonus.
- never resets the Fury actor or restarts its current war.

Separate depot-seizure and target-preparation decisions and a compliance boost were planned but not adopted.

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

Evolution I unlocks the `Hardened Doctrine` branch: `Harden the Columns`, `Depot Officers Without Leave`, `Forced March Tables`, and `Occupation as Recruitment`.
The earlier working names `The Second Border Is Already Drawn` and `No Clerk Can Stop The War Office` were not adopted.

### Gameplay limits

Evolution I should not make Fury instantly unbeatable.
It should improve the quality of the first war and make repeated wars more likely, while leaving overextension and containment meaningful.

## Evolution II: Two Fires

Working log name: `Two Fires`.

### Role

The second evolution makes Fury no longer unique.
Two Fury actors can appear at the same time.
Cooperation mechanics become available when they are not hostile to each other.

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
- prefer a different region or continent from the first Fury (design intent; the ordinary weighted pool does not yet weigh distance, while the challenge and world-end seeders already spread by continent).
- initialize the second Fury with the current evolution level.
- unlock Fury-to-Fury diplomacy decisions.
- enable pact or rivalry logic depending on type.
- use the existing project-pact membership and reserve-sharing rules when the actors cooperate.
- let rivalry influence pursuit of the same legal third-country target. Joint plans provide their accepted preparation, command, and truck rewards without partitioning territory.

### Pre-fire evolved opening

A new Fury cycle begins with two Fury actors.

Selection rules:

- avoid selecting countries that share the same immediate target pool if possible.
- avoid selecting any player country or player-linked country.
- avoid placing both Fury actors where one will destroy the other in the first month unless the type is hostile.
- if only one safe candidate exists, fire one Fury and record that the second slot could not be safely filled.

### Cooperation mechanics

An actor commits to one route, either through the paid `Form a Fury War Table` or `Mark a Rival Column` decision or through the first focus of that branch; each choice locks the other.

On the cooperation route, Fury actors:

- become project-pact members and gain the `Fury Pact Command` idea.
- mark eligible non-hostile partners through `The Other Fire Answers`.
- open physical reserve sharing through `Fury Pact Command` before any native faction exists.
- receive the preparation, command, and truck rewards of `Shared War Tables` and `Joint Campaign Plans` (`fury_partition_before_victory`) without any territorial partition.

On the rivalry route, Fury actors:

- treat each other as valid targets only after ordinary legal neighbours are exhausted, or earlier as Hostile Fury challenge actors.
- add the centrally tuned shared-rival score to a legal third-country target also pursued by a non-allied rival (`Claim the Same Victim`).
- gain the `Rival Fury Doctrine` idea and can reach terminal preparation as the last surviving rival through `Last Fury Standing`.

### Focus tree unlocks

Evolution II unlocks the cooperation branch (`Second War Table`, `The Other Fire Answers`, `Shared War Tables`, `Joint Campaign Plans`, `Joint Cadre Transfers`, `Fury Pact Command`) and the mutually exclusive rivalry branch (`Rival Column`, `No Second Fury`, `Claim the Same Victim`, `Absorb the Rival Fire`, `Last Fury Standing`).
The earlier working names `Officers Across The Border`, `Two Capitals, One Map`, `When Fury Meets Fury`, and `Deny The Other March` were not adopted.

## Evolution III: All Borders at Once

Working log name: `All Borders at Once`.

### Role

The third evolution turns Fury from sequential local conquest into broad border rupture.
Three Fury actors can appear.
Each Fury country is stronger and can declare on all valid neighbors at once.

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

If Fury actors already exist, Evolution III currently:

- selects actors up to three in total, each opening with the largest package.
- declares on every valid neighbour of each existing actor.
- opens the `All Borders` focus branch, which adds supply equipment and a capped wave and raises overextension sharply.
- lets actors keep finding targets at extreme occupation pressure, so the strain shows as the idea and crisis instead of a pause.
- raises later direct-wave size and the target-score evolution bonus.

Anti-Fury availability is tied to the major super-event and the world-end branch, not to this evolution.

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

Fury should not declare on a much stronger neighbor just because it shares a border.
Each target must pass a scaled validity check.
A local major can become valid only if Fury has reached major threshold or terminal state.

## Evolution logging

Each evolution should record a real evolution entry.

Suggested event log fields:

| Evolution | Stage | Chaos Tier | Actor |
| --- | --- | --- | --- |
| Hardened Fury | 1 | Gathering Storm | strongest Fury actor |
| Two Fires | 2 | Rising Chaos | strongest Fury actor |
| All Borders at Once | 3 | Chaos Tier | strongest Fury actor |

Disabled evolutions must not unlock their branches, spawn additional Fury actors, or set recorded flags that later systems read.

## World-end branch: The World in Fury

The terminal world-end branch uses the same name as the triggerable scenario, but they are separate systems.

The triggerable scenario is a manual setup.
The world-end branch is a terminal campaign state.

### World-end role

The world-end branch begins when Fury has stopped being a local pattern and becomes the operating rule of the world.
A main Fury actor has no valid local neighbors left or has become a large power, then exports the Fury pattern to other continents.
Minor countries in other continents become Fury and join the main Fury faction.

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

Current implementation note: `fury_try_start_world_end` and `fury_start_world_end` provide the first terminal starter.
The branch sets `world_end`, `world_end_fury`, `fury_world_end_active`, `world_threat_source_fury`, creates `The World in Fury`, seeds safe AI Fury actors across unrepresented continents first, fills toward the required terminal actor count, and reports `fury_world_end_seed_blocked` if the safe seed pool is insufficient.

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

The faction should not be a normal ideological bloc.
It exists to coordinate the Fury pattern.

Faction behavior:

- Fury members ignore ordinary diplomatic courtship and coordinate war instead.
- Fury members share physical reserves through the terminal reserve decision.
- Fury members do not accept ordinary peace with target states while terminal state is active.
- Fury members can compete for conquered land, but the main Fury actor remains faction leader unless defeated.
- No member partitions conquered territory by script; land changes hands through ordinary peace.

Current implementation note: the terminal starter leaves any prior faction, creates `The World in Fury`, adds active and seeded Fury actors to the leader's faction, grants the `fury_world_in_fury` idea, and flags them with `fury_pact_member` and `fury_world_end_actor`.
Terminal actors can use `fury_share_terminal_reserves` to move the actual paid manpower, rifles, and support equipment to another terminal Fury actor, and `fury_assign_terminal_fronts` to add target preparation and momentum and relieve overextension across the terminal pact.
Pact Cohesion is retired, so neither decision raises a cohesion value.

### Terminal targeting rules

The world-end branch may eventually threaten player countries beyond the ordinary neighbor loop, but this should be a terminal state with clear warning.
The ordinary neighbor loop can still target player-controlled countries when they meet normal target gates.

Terminal target rules:

- ordinary valid targets can be AI or player-controlled countries.
- terminal out-of-neighbor threats still use warning and delay before direct player pressure.
- the player should receive warning events and response tools.
- Fury does not give the player the Fury package even if the player is in the faction through unusual modded conditions.
- subject and faction logic must avoid stealing player-controlled peace outcomes.

Current implementation note: `chaosx.nr7.50` warns all player countries and `fury_player_warning_grace_active` marks the grace period.
Ordinary target selection can hit player-controlled countries that meet the normal target gates.
After the grace flag expires, world-end actors that have no valid neighbor can use `fury_terminal_can_threaten_player_linked_country` through `fury_try_terminal_player_target`, which sends `chaosx.nr7.52` before the direct terminal war declaration.

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

Quote direction: real historical or literary quote about unchecked expansion, force becoming policy, or borders losing meaning.
Use super-event research workflow before final selection.

Button direction: cold and short.
Example direction: `The map keeps moving`.

Current implementation note: slot `59` uses generated final image art at `gfx/super_events/007_fury/fury_becomes_a_state.dds` and sourced audio ID `29` at `sound/007_fury/super_event_29_fury_becomes_a_state.wav`; source and license details are recorded in `docs/super_events/super_event_audio_packages.md`.
The source and processed PNG folder once cited under `docs/assets/007_fury/super_events/` is not present in the repository, so image provenance remains part of the unresolved legacy asset provenance in the release review.

### Super-event 2: The World in Fury

Role: world-end reveal.

Trigger: terminal branch begins.

Tone: the pattern is no longer contained by continent or region.

Image direction: global map room with multiple small flags, radio operators, dispatch sheets, and a central table.
No modern screens.
No readable generated text.

Quote direction: real quote about war spreading through imitation, the end of order, or the logic of force.
Use super-event research workflow.

Button direction: short and terminal.
Example direction: `Every border is a front`.

Current implementation note: slot `60` uses generated final image art at `gfx/super_events/007_fury/super_event_world_in_fury.dds` and sourced audio ID `30` at `sound/007_fury/super_event_30_world_in_fury.wav`; source and license details are recorded in `docs/super_events/super_event_audio_packages.md`.
Its source PNG folder is likewise absent and covered by the same provenance item.

### Optional super-event 3: Fury defeated after terminal branch

Role: aftermath.

Trigger: all Fury actors defeated after a long terminal crisis or after the Fury faction held enough states to reshape the campaign.

Tone: tired relief, not clean victory.

Image direction: abandoned border office, burned maps, officials restoring archives, soldiers guarding checkpoints.

Quote direction: real quote about rebuilding order after war or the cost of victory.

Button direction: restrained.
Example direction: `Count what remains`.

## News and report events

Fury keeps a small set of non-super-event presentation beats, each marking a distinct moment.

| Beat | Current event | Scope |
| --- | --- | --- |
| Outbreak batch | `chaosx.news.7008`, one per successful ordinary or manual preparation batch, single or aggregate text | World News |
| First territorial gain | `chaosx.news.7007`, once per campaign | World News |
| Invalid manual request | `chaosx.nr7.3` to the requesting human only | report |
| Fury becomes major-sized | slot `59` super-event | super-event |
| World in Fury begins | slot `60` super-event and `chaosx.nr7.50` warning to each human | super-event and report |
| Terminal seed blocked | `chaosx.nr7.51`, once per human | report |
| Terminal player target | `chaosx.nr7.52` to the threatened human before the declaration | report |
| Last terminal Fury falls | `chaosx.nr7.53` | report |
| South American conquest | `chaosx.nr7.60` to the United States | report with choice |

`chaosx.nr7.2` is the actor's own takeover report and is normally seen only by the AI.
A stall report, a no-neighbour report, and ordinary per-country defeat news are not implemented.
Per-country defeat news remains unresolved in the README; the other two are not required because the occupation crisis and the major super-event already mark those moments.

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

The baseline event does not need a large global anti-Fury system.
It should stay minor repeatable until escalation.
However, once Fury becomes major or world-end begins, other countries need limited response tools.

Implemented response families use `anti_fury_response_category`, which appears after the major super-event or world-end branch for countries bordering a Fury actor and for majors.

| Response | Who can use it | Purpose |
| --- | --- | --- |
| Border Watch | countries bordering Fury | timed mission that lowers Fury momentum on success |
| Supply Denial | countries bordering Fury | timed mission that raises Fury overextension and lowers momentum on success |
| Firebreak Staff Talks | eligible non-Fury countries | temporary defensive planning idea |
| Emergency Aid | eligible non-Fury countries | equipment to a non-player Fury target, followed by an aid-route mission |

Firebreak Guarantees were not adopted, and Recognition Denial is retired because its payment produced no readable consequence.
The decision audit's unresolved finding still applies: the three missions do not yet check supplied border divisions, rail access, or an aid route, and a proposal is recorded in the README.
Costs use command power, rifles, support equipment, trains, and army experience rather than political power.

## Interactions with other Chaos Redux events

Fury should interact with existing systems only where the connection matters.

Suggested connections:

| System | Interaction |
| --- | --- |
| Random War | Fury belongs to the Wars cluster; avoiding a Random War target in the same short window is design intent without a current guard, recorded as a proposal in the README |
| Other release events | newly released tiny countries can become Fury later if they meet eligibility and cooldown rules |
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
| Fury civil fracture | sustained extreme occupation pressure | not implemented; proposed in the README as a release of unregistered occupied land |
| Pact dispute | multiple Fury actors compete for same region | rivalry route through the shared-rival target score; no cohesion value exists |
| Terminal defeat | all Fury actors destroyed after world-end | aftermath package |

A Fury defeat should not erase the event from history.
It should remain and should contribute to future evolution memory only if it reached meaningful milestones.

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

Cleanup should not remove ordinary conquered territory automatically unless a separate peace or defeat effect says so.
If Fury conquered land and then became a normal country after defeat of its Fury system, the map state should be handled through peace and aftermath logic, not hidden rollback.
