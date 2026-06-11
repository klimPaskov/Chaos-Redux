# 007 Fury decisions and missions specification

## Decision category role

Working category name: `Fury War Office`.

The category exists for Fury countries and is primarily AI-used because random Fury never selects a player. It can still display if a player uses console or tag switching, but ordinary gameplay should not grant it to the player.

The category controls:

- target preparation.
- finite reinforcement reserve controls.
- depot conversion.
- occupation and compliance.
- coring.
- cooperation or rivalry with other Fury countries.
- no-neighbor and world-end setup.

A small anti-Fury category or decision family can appear for non-Fury player countries only after Fury becomes major or world-end begins.

## Category visibility

Fury War Office is visible if:

- the country has Fury actor flag.
- the country is not capitulated.
- the Fury system is active.
- the country has the Fury idea.

It should hide or clear if:

- Fury is defeated.
- the country no longer exists.
- the country loses the Fury actor flag.
- the terminal branch ends.
- cleanup removes Fury decisions.

## Core Fury decision values

Decision tooltips should reference these values through scripted localisation where possible.

| Value | Use in decisions |
| --- | --- |
| Fury Momentum | cost reduction for target preparation, better reserve-spawned unit quality while reserve remains |
| Fury Overextension | blocks new wars if too high, raises integration costs |
| Compliance Drive | improves coring and occupation decisions |
| Fury Reach | unlocks no-neighbor and world-end decisions |
| Fury Pact Cohesion | unlocks shared decisions or rivalry consequences |

## Decision family: choose and prepare target

### Find the Next Weak Neighbor

Role: sets the next target if no active Fury war exists.

Availability:

- Fury actor has no active target.
- at least one valid neighbor exists.
- overextension is below a hard danger threshold or Evolution III is active.
- not in no-neighbor state.

Costs and requirements:

- command power.
- army XP if the country has too few staff-related focuses.
- target must pass weaker-neighbor score.
- if supply is poor, requires trains or trucks.
- if the border region is rough terrain, requires additional equipment or preparation time.

Effects:

- saves target.
- raises target preparation value.
- starts a short hidden delay before declaration.
- AI almost always takes this if valid and Fury has momentum.

### Cut the Border Rail

Role: weakens a target before war.

Availability:

- target selected.
- Fury controls a border state or has a direct land border.
- target is valid under the Fury target rules and has a direct land border.

Costs:

- infantry equipment.
- support equipment.
- army XP.
- possible stability loss if repeated.

Effects:

- short target combat penalty.
- lower target supply in border states if implementation supports state effects.
- raises target warning chance if failed.
- increases Fury overextension slightly.

### Capital First Plan

Role: improves offensive against selected target capital.

Costs:

- command power.
- army XP.
- fuel if Fury has motorized support.
- planning time.

Effects:

- temporary attack bonus toward capital area.
- increases AI focus on target victory points.
- no direct uncapped units.

## Decision family: finite reinforcement reserve control

Reserve-spawned units should be automatic only while the hidden reinforcement reserve pool has units remaining. Every reserve spawn consumes that pool, and the weekly loop only draws at a slow cadence. When the pool reaches zero, free weekly spawning stops completely. Decisions can change quality, source, strain, or add a limited reserve refill, but no decision may create an uncapped unit loop. All scripted reserve grants share the same 100-division per-actor cap, and repeatable reserve decisions must use long cooldowns so the cap cannot be filled instantly.

### Open the Depots

Role: consumes equipment to improve upcoming reserve-spawned units or add a small capped reserve refill.

Costs:

- infantry equipment.
- support equipment.
- trains or trucks if logistics branch is used.
- command power.

Effects:

- a small capped reserve refill is added on a long cooldown.
- increases overextension or supply strain.
- AI uses when at war and equipment reserve is high.

### Empty the Training Yards

Role: draws more of the finite reserve quickly with lower quality.

Costs:

- manpower.
- stability.
- infantry equipment.
- training penalty for reserve-spawned units.

Effects:

- increases next weekly draw from the existing pool or adds a capped emergency refill.
- units arrive undertrained.
- raises overextension.
- AI uses when losing a war or when Evolution III has multiple fronts.

### Depot Cadre Conversion

Role: turns occupied depot work into capped garrison reserve or support units.

Availability:

- controls conquered non-core states.
- has occupation branch focus.
- not at extreme resistance risk.

Costs:

- support equipment.
- manpower.
- compliance threshold.

Effects:

- spawns one-time garrison units or adds a capped garrison reserve refill.
- improves compliance drive.
- reduces resistance damage in selected states.

## Decision family: conquest settlement

### Install the Settlement Office

Role: begins postwar absorption after defeating a target.

Availability:

- defeated AI target exists or recently capitulated.
- Fury controls target capital or key state.
- settlement has not already processed.

Costs:

- command power.
- support equipment.
- manpower.
- overextension increase based on target size.

Effects:

- transfers or consolidates eligible states through scripted settlement.
- adds compliance.
- raises momentum.
- raises overextension.
- unlocks integration decisions.

### Count the Captured Registers

Role: improves compliance in a newly conquered state group.

Costs:

- support equipment.
- infantry equipment.
- time.
- local control.

Effects:

- compliance gain.
- resistance reduction.
- small stability cost if harsh occupation path is active.

### Core the First Ring

Role: cores the first conquered neighboring region.

Availability:

- compliance threshold met.
- owns and controls state group.
- not at extreme overextension.
- has occupation branch focus.

Costs:

- support equipment.
- manpower.
- command power.
- stability or war support risk.
- possibly trains if region requires rail administration.

Effects:

- cores small state group.
- reduces overextension.
- increases momentum.
- one-time per state group.

### Core by March

Role: faster coring through military pressure.

Availability:

- has harsh integration focus.
- active war or high momentum.
- compliance requirement lower than administrative path.

Costs:

- infantry equipment.
- manpower.
- stability.
- resistance risk.
- overextension.

Effects:

- cores state faster.
- adds resistance or temporary local penalty.
- AI uses only at high momentum or in terminal branch.

### Core by Administration

Role: slower and safer coring.

Availability:

- has administrative focus.
- compliance threshold higher.
- no active severe resistance.

Costs:

- support equipment.
- command power.
- time.
- lower stability cost.

Effects:

- cores state group.
- reduces overextension more than harsh path.
- AI uses when not under severe military pressure.

## Implemented occupation pressure loop

The current implementation uses the following concrete state and country surfaces:

- `fury_occupation_pressure` is recalculated during the scoped Fury weekly actor loop from non-core controlled states, active wars, resistance, registered states, rail registry completion, and `fury_garrison_capacity`.
- High pressure adds `fury_overextension`, weakens reserve-spawned unit quality or draw, and raises occupation decision priority.
- Extreme pressure sets `fury_occupation_crisis_active`, blocks ordinary target selection unless Evolution III or terminal Fury overrides it, and activates `fury_restore_the_registers_mission`.
- `fury_count_captured_registers` starts administrative register work on a non-core controlled state.
- `fury_rail_registry_survey` marks a registered state with `fury_rail_registry_complete` and reduces pressure.
- `fury_garrison_the_names_mission` is a timed hold mission; success lowers pressure and improves compliance, while failure raises resistance and overextension.
- `fury_core_state_by_administration` requires `fury_admin_coring_unlocked`, high compliance, and no recent integration failure.
- `fury_core_state_by_march` requires `fury_march_coring_unlocked`, lower compliance, and pays higher manpower/equipment/stability cost.

## Decision family: Fury cooperation

Available when Evolution II is active and pact type is enabled.

### Open Shared War Tables

Role: starts Fury coordination with another Fury actor.

Costs:

- command power.
- army XP.
- Fury Pact Cohesion minimum.

Effects:

- joins or strengthens Fury faction.
- sets cooperation target.
- unlocks joint aid.

### Send Cadres to the Other Fury

Role: stronger Fury supports weaker Fury.

Costs:

- manpower.
- infantry equipment.
- support equipment.
- convoys or trains if overseas.

Effects:

- weaker Fury receives units or equipment.
- sender loses equipment and gains pact cohesion.
- can only be used a limited number of times.

### Partition Before Victory

Role: reduces target dispute between Fury partners.

Costs:

- political power can be used here because this is bureaucratic diplomacy.
- command power.
- target region requirement.

Effects:

- reduces risk of Fury-on-Fury war.
- improves postwar settlement.
- reduces pact cohesion if both want same capital.

Current implemented cooperation decisions are `fury_form_war_table`, `fury_share_terminal_reserves`, and `fury_assign_terminal_fronts`. The terminal reserve decision spends command power, manpower, rifles, and support stores to supply another `fury_world_end_actor`; the terminal fronts decision spends command power and army experience to raise pact cohesion, target preparation, momentum, and overextension relief across terminal Fury actors.

## Decision family: Fury rivalry

Available when Evolution II hostile type is active or pact cohesion collapses.

### Mark the Rival Fury

Role: designates another Fury country as a future target.

Availability:

- no smaller valid neighbors remain or hostile scenario type allows early rivalry.
- both countries are Fury actors.

Costs:

- command power.
- army XP.
- momentum.

Effects:

- adds rivalry target.
- unlocks Fury-on-Fury war after a delay.
- raises overextension.

### Absorb the Rival Fire

Role: reward for defeating another Fury actor.

Availability:

- rival Fury capitulated to this Fury.
- settlement not processed.

Costs:

- support equipment.
- manpower.
- high overextension.

Effects:

- absorbs part of rival momentum.
- takes selected land if safe.
- may inherit part of rival focus progress or pact claim.
- raises world-end eligibility.

## Decision family: no-neighbor and world-end setup

### Survey Beyond the Continent

Role: begins reach buildup when no valid local neighbors remain.

Availability:

- no valid AI land neighbor on current continent.
- Fury is not capitulated.
- no ordinary target active.

Costs:

- command power.
- convoys if coastal.
- fuel or trains depending on route.
- overextension threshold.

Effects:

- raises Fury Reach.
- unlocks no-neighbor focus path.
- if world-end threshold is not met, gives internal pressure rather than instant expansion.

### Carry Orders Overseas

Role: prepares world-end continental seeding.

Availability:

- world-end eligibility is met.
- main Fury actor exists.
- no world-end state exists.
- no-neighbor or major-Fury branch completed.

Costs:

- high Fury Reach.
- command power.
- army XP.
- convoys or trains.
- overextension risk.
- main Fury must control enough industry or ports if using overseas spread.

Effects:

- queues world-end branch.
- fires world-end super-event through event effect.
- seeds other continents.

## Anti-Fury decisions for non-Fury countries

These appear only after a Fury major exists or world-end begins.

### Border Watch Mission

Role: timed objective for countries bordering Fury.

Requirement:

- place supplied divisions in border states.
- hold capital and border rail access for duration.

Success:

- reduces Fury target confidence against this country.
- gives temporary defense against Fury.
- may lower Fury momentum if Fury is currently targeting the country.

Failure:

- raises Fury confidence.
- may make the country a valid target sooner in terminal branch.

### Emergency Aid to the Target

Role: send equipment to an AI country currently attacked by Fury.

Costs:

- infantry equipment.
- support equipment.
- convoys or trains.
- diplomatic exposure or stability risk.

Effects:

- target gets equipment.
- Fury momentum gain from victory is reduced if target lasts long.
- AI majors can use this when Fury is near their region.

### Firebreak Staff Talks

Role: limited coalition coordination after major-Fury threshold.

Costs:

- command power.
- army XP.
- political power as a small diplomatic cost.
- relations or faction compatibility.

Effects:

- temporary defense planning against Fury.
- unlocks shared anti-Fury AI weights.
- does not create a full anti-Fury faction unless world-end is active.

### Supply Denial

Role: timed mission started by countries bordering Fury.

Costs:

- command power.
- infantry equipment.

Effects:

- starts `anti_fury_supply_denial_mission`.
- success raises containment pressure, raises neighboring Fury overextension, and lowers Fury momentum.
- failure relieves some neighboring Fury pressure.

### Recognition Denial

Role: diplomatic refusal after Fury becomes a visible major threat.

Costs:

- command power.

Effects:

- lowers one Fury pact cohesion record.
- raises containment pressure and contribution tracking.

Current implemented anti-Fury decisions are `anti_fury_border_watch`, `anti_fury_send_emergency_aid`, `anti_fury_firebreak_staff_talks`, `anti_fury_start_supply_denial`, and `anti_fury_recognition_denial`. Border Watch, Emergency Aid, and Supply Denial each start a timed mission rather than resolving as a single instant bonus.

## Missions

Missions should ask countries to act on the map, not passively wait.

| Mission | Owner | Objective | Duration direction | Success | Failure |
| --- | --- | --- | --- | --- | --- |
| Guard the Fury Capital | Fury | keep capital supplied and controlled while at war | medium | stronger reserve-spawned units while reserve remains | weaker reinforcements and momentum loss |
| Secure the First Depot Belt | Fury | control named depot or rail states near first target | medium | better settlement and unit quality | overextension rises |
| Hold the New Registers | Fury | keep newly conquered state group under control | long | compliance gain and coring unlock | resistance and overextension |
| Border Watch | non-Fury neighbor | place supplied divisions in border states | medium | defense bonus and target deterrence | Fury target score rises |
| Keep the Aid Route Open | aid sender | maintain convoy or rail route to target | medium | aid arrives | equipment lost and target morale reduced |

Named states and regions should be generated or printed through scripted localisation. Avoid raw state ids in player-facing text.

## Decision clutter control

The category should show only decisions that matter.

Rules:

- show one target-selection decision when no target exists.
- show target-preparation decisions only when a target is selected.
- show settlement decisions only after a victory.
- show integration decisions only for state groups that Fury owns and controls.
- show cooperation decisions only if another Fury actor exists and pact type allows it.
- show rivalry decisions only if hostile type or pact collapse allows it.
- show world-end decisions only after no-neighbor or major threshold.
- hide obsolete decisions after target, war, or state group becomes invalid.

AI can use hidden or scoped versions of decisions, but the visible category should remain readable if a player ever views it.

## Costs and blocked localisation

Cost text should be icon-first and short.

Examples:

- `1,500 infantry equipment`.
- `200 support equipment`.
- `20 army XP`.
- `Supplied divisions on the border`.
- `Control the target capital`.
- `Compliance in the first ring`.

If a decision has many requirements, use a short summary and a detailed tooltip. Missing costs should be red in localisation, but the exact formatting belongs to implementation.

## Cleanup

Decision cleanup must remove:

- active target decisions when the target dies or becomes invalid.
- preparation flags when war starts.
- settlement flags after settlement processing.
- coring decisions after a state group is cored.
- pact target flags when a Fury partner dies.
- anti-Fury missions after the Fury major threat ends.
- scenario setup flags after launch.

No decision should remain visible for a dead target, protected invalid target, or invalid state group.
