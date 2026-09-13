# Event 059: The Offensive

## Part 1: Core event design

## Catalog entry

- Event ID: `59`
- Event name: The Offensive
- Type: Minor Fire-Once
- Minimum Chaos level: 1
- Primary cluster: Diplomacy
- Member severity: High
- Cluster role and chance: Authoritative Diplomacy defaults after registry inspection

## Premise

A worldwide change in military planning takes hold among AI-controlled governments. General staffs shorten preparation cycles, give more authority to field commanders, move reserves toward decisive sectors, and treat enemy weakness as an opportunity that should be used quickly. Armies that once accepted static fronts begin trying to change them. Maritime powers prepare more landings. Governments with claims, war goals, or exposed rivals become less willing to let those opportunities expire.

The event changes how the AI chooses and executes strategy. It does not alter the underlying combat rules. No country receives attack, breakthrough, organisation, planning, supply, production-output, research-speed, or equipment-stat bonuses from the event.

## Player experience

The event should be visible through changed world behavior rather than a large new interface. Human players receive a global report explaining that military planning has shifted across AI-run states. Afterward, players should notice more active fronts, stronger concentration on useful attack sectors, more serious attempts to exploit weak enemies, better-supported naval invasions where the AI has the means, and greater willingness to use existing claims or war goals.

The change must remain legible without exposing strategy weights. A player should understand that AI governments have adopted a more offensive posture, that the posture grows stronger through evolutions, and that human-controlled countries are exempt. The event should not display raw readiness scores, target values, front ratios, production weights, or internal safety floors.

## Global activation

The first firing creates one permanent global event state. The normal event history records the firing once. The event's Fire-Once weight is then removed from future random selection.

Activation has these immediate results:

- every currently AI-controlled ordinary country begins using the baseline offensive posture
- countries currently controlled by a human remain under human command and receive no automated strategy behavior
- countries created, released, restored, or split after activation become covered when they are AI-controlled
- a country taken over by a human stops using the event's AI behavior
- a country handed back to the AI begins using the active behavior again
- all human players receive the global report in multiplayer
- the event remains active across save and reload

The event should use current control as the decisive condition. Control at the moment of firing must not permanently include or exclude a country.

## Control model

The preferred design is a declarative AI strategy layer that checks the permanent global event state and whether the country is currently controlled by the AI. This avoids a recurring whole-world scan.

An implementation that needs country-local strategy registration may attach dormant AI strategy state to every eligible country once, including human-controlled countries, provided that state has no gameplay effect while a human is in control. New-country and release hooks must then register later countries without a daily or weekly global sweep. The observable contract remains the same in either implementation.

Cooperative control counts as human control. A player takeover during an active war must stop Event 059 from issuing or evaluating AI choices for that country. Returning the country to AI control must restore the correct baseline and evolution layers without refiring the event.

## Baseline strategic identity

The baseline is a measured global offensive doctrine. It should make AI countries more active and less wasteful without making them suicidal.

### Front conduct

AI countries should become more willing to:

- activate prepared battle plans on favorable fronts
- attack on slightly uncertain fronts when supply, equipment, manpower, and reserves remain adequate
- concentrate more combat power on a limited number of useful sectors
- reinforce successful attacks and exploit a broken line
- pressure exposed flanks, weakly held provinces, supply routes, ports, rail junctions, and important victory points
- move mobile and high-breakthrough formations toward sectors where they can matter
- pause less often after limited gains when the next attack remains supportable
- abandon attacks that have become materially unsustainable

Encirclement is an intended battlefield outcome, not a claim that the script can directly command an encirclement. The implementation should use verified front, target, reserve, concentration, and exploitation controls that make encirclement more likely when the map offers it.

### Force concentration

The posture should reduce passive force scattering. Each country should identify a manageable number of priority fronts based on its size and capacity.

- a minor usually concentrates on one main front
- a regional power can support one main front and one secondary objective
- a major can coordinate several theaters when logistics and reserves permit
- an island or maritime power can treat a viable landing zone as a priority front
- a country under immediate invasion must preserve enough forces for critical home defense

The event should not order every unit forward. It should move forces away from low-value inactivity while preserving capital defense, threatened ports, active invasion zones, essential garrisons, and a real reserve.

### Production posture

AI production should support the strategy the country can actually sustain. The event should raise the value of offensive formations and enabling equipment, but it must not impose one force model on every country.

Common priorities include:

- infantry equipment and support equipment needed to keep active formations supplied
- artillery where industry and technology support it
- trucks, trains, and logistics equipment needed to move and sustain attacks
- armour and motorised or mechanised formations for countries with adequate industry, technology, fuel, and replacement capacity
- fighters and close air support for countries able to maintain useful air operations
- transport and convoy capacity for viable maritime powers
- naval forces that support invasion, escort, and control of the sea lanes required by the country's actual strategy

The posture must preserve replacement and garrison needs. A poor minor should not starve its infantry to pursue an impossible tank program. A landlocked state should not divert industry into a naval plan. A fuel-starved country should not build a force it cannot operate.

### Air conduct

AI air power should move more decisively toward active offensive sectors when aircraft, range, airfields, fuel, and mission capacity permit it. Fighters should contest the relevant air region. Close air support and tactical support should follow important ground operations. Strategic home defense must remain when enemy bombing or invasion makes it necessary.

The event should improve mission allocation and support priorities. It must not grant aircraft, mission efficiency, range, air superiority, or combat bonuses.

### Naval and amphibious conduct

Coastal AI countries should become more willing to prepare and execute naval invasions when they have:

- a useful target
- transport capacity
- enough convoys
- a practical route
- adequate naval or air support
- a credible chance to seize and supply a port or coastal lodgment
- enough forces to defend the home front while the landing is underway

Preferred targets include exposed ports, isolated coastal sectors, islands with strategic value, and coastlines that can open a useful new front. The event should not create repeated unsupported landings into defended provinces with no supply plan.

### Existing war goals and obligations

At baseline, the event chiefly changes conduct inside existing conflicts and the use of opportunities already recognised by normal country content.

AI countries should become more willing to:

- execute existing war goals when the target and timing are reasonable
- answer calls to arms when participation advances their strategic interests and does not create an impossible war
- join faction wars that protect allies, secure a shared front, or prevent a hostile victory
- use available claims and scripted territorial objectives more decisively

The baseline should not create arbitrary claims, bypass diplomatic rules, or turn every weak neighbor into a legal target. The broader predatory behavior belongs to Evolution II.

## Safety envelope

Aggression must remain conditional. The following conditions should block or sharply suppress a proposed offensive action:

- the country is human-controlled
- there is no valid enemy, front, target, or legal war path for the action
- the country has capitulated or cannot conduct the proposed operation in its current state
- trained manpower is critically depleted
- essential equipment deficits are severe and worsening
- the proposed front is critically undersupplied
- fuel availability cannot sustain the planned force
- the country lacks the convoys, naval access, or transport capacity required by an invasion
- the country has no defensible reserve for its capital, core ports, threatened homeland, or another critical front
- existing wars already exceed the country's sustainable strategic capacity
- a subject is being asked to perform an independent diplomatic action that its status does not permit
- an event-created or special actor has a hard owner strategy that conflicts with the generic layer

Soft conditions should scale willingness rather than produce a simple yes or no result. Important factors include local strength, reserve strength, supply trend, equipment trend, manpower trend, terrain, weather, air support, naval support, target value, strategic distance, enemy isolation, allied support, front length, active war count, recent losses, and the expected cost of opening another theater.

## Country archetype scaling

The event uses one strategic idea with different practical expressions.

### Continental major

A continental major can coordinate combined arms, several priority fronts, reserve movement, air support, and sustained production for breakthrough forces. It can accept a moderate increase in multi-front risk while preserving the defense of its core industrial regions.

### Maritime major

A maritime major can invest more heavily in transports, escorts, air cover, ports, and amphibious operations. It should still refuse an invasion when control of the route or follow-up supply is implausible.

### Regional power

A regional power should concentrate on one decisive theater and keep a smaller reserve for secondary borders. It may build armour or a strong air arm when its economy supports one, but should not imitate the full program of a major.

### Industrially weak minor

A weak minor should favor concentrated infantry, artillery, support equipment, local mobile reserves, and attainable objectives. It should avoid equipment families that would hollow out the rest of its army.

### Landlocked country

A landlocked country receives no naval or amphibious emphasis. Its offensive posture should focus on supply, artillery, mobile reserves, air support when feasible, and decisive local fronts.

### Subject country

A subject should support offensive operations inside its overlord's wars and answer valid calls according to subject rules. The event must not grant independent diplomatic powers that the subject does not possess.

### Government in exile or capitulated country

Most independent offensive and war-opening layers should be inactive. Valid exile support, expeditionary, air, naval, and liberation behavior can remain where the base game already supports it.

### Event-created and special countries

New ordinary countries use the global posture when AI-controlled. Special Chaos actors keep the strategy that defines their event identity. Event 059 may add compatible behavior, but it cannot overwrite a hard owner plan, remove unique targeting restrictions, or make a contained actor violate its own rules.

## Cluster role

The Offensive belongs to the Diplomacy cluster with High member severity. The accepted cluster update treats the old Diplomatic Panic name as the same cluster and forbids preserving it as a separate alias.

The cluster update fixes membership and severity but does not prescribe a special Event 059 role or chance. The implementation must inspect the authoritative aligned member arrays and use current Diplomacy defaults for required or optional role, participation chance when relevant, and member minimum tier. No event-specific participation override belongs in the design.

When Event 059 is selected as the anchor, it fires normally and the Diplomacy cluster may roll eligible companion events according to their own rules. When it joins another Diplomacy incident as a member, it still becomes permanently fired and cannot join again.

The cluster must count as one global pacing event. Event 059 keeps its own history entry, Fire-Once removal, evolution state, and one-time Chaos manifestation. Companion events keep their own consequences. The cluster must not duplicate the event's activation or apply a second Chaos grant for the same global doctrinal shift.

## Initial Chaos effect

The first worldwide adoption of the offensive posture is a concrete global destabilisation and should add a small one-time amount of Chaos.

The starting band is 15 to 25 Chaos. The final amount should scale within that band using the number of living ordinary AI countries and AI-controlled major powers affected at activation. It is applied once and guarded permanently.

Evolution eligibility and activation add no Chaos. Later wars, annexations, casualties, faction changes, and world tension use the shared Chaos systems. Event 059 should not add another premium merely because its AI preferences contributed to those ordinary outcomes.

## Achievement role

The event supports one difficult player achievement. It rewards a non-major country for surviving and defeating a stronger AI major during Total Offensive without protection from a major ally. It does not unlock merely because the event fires or because the player waits through an evolution. The detailed conditions and asset direction are defined in the separate achievement prompt and acceptance matrix.
