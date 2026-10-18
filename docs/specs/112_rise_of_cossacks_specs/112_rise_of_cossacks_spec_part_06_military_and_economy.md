# Part 06. Army, modernization, production, and service economy

## Military identity

The opening army is built around cavalry because the host is a mobile frontier rising.
Its long-term strength comes from organization, local knowledge, infantry cooperation, reconnaissance, and a sustainable supply system.
Modernization keeps those traditions useful while introducing artillery, engineering, communications, vehicles, and broader recruitment.
The player decides how much of the army remains mounted and what the country can afford to support.

The event uses native cavalry, infantry, motorized, and eventually mechanized or armored components.
No new combat archetype, horse currency, or fictional weapon technology is required.
The two custom model entities are visual treatments of accepted native cavalry and infantry consumers.
Their production is specified in part 12.

The design supports four recognizable native template families.
Opening units use smaller recipes drawn from the same military identity.
They do not arrive as full late-game divisions.
All exact manpower, equipment, combat-width, experience, and support-company values must come from the installed native definitions before engine implementation.

## Four template families

| Code | Working template family | Proposed mature composition | Main role | Material and operational weakness |
| --- | --- | --- | --- | --- |
| T01 | Mounted host regiment | Six native cavalry battalions, with reconnaissance and engineers only after their programs and equipment are available | Screening, movement through suitable country, reserve defense, pursuit, and raids | Vulnerable to well-supported infantry, armor, air attack, and prolonged frontal combat |
| T02 | Plastun infantry group | Six native infantry battalions with reconnaissance and optional engineers, then ordinary supporting artillery when sustainable | Dismounted reconnaissance, concealed approach, difficult ground, river and settlement defense | Slower operational movement and continuing need for fire support |
| T03 | Territorial defense group | Four native infantry battalions, with optional engineers at important crossings | Hold settlements, crossings, depots, and the home frontier while field formations deploy | Limited offensive power and equipment quality |
| T04 | Modern mobile group | Six native motorized infantry battalions with available reconnaissance, engineers, and an affordable support package | A small operational reserve working with artillery and later armor | Fuel, truck replacement, repair, and road dependence |

These recipes are proposed organizational targets.
The focus and decision text must disclose the actual implemented composition.
The template auditor may revise battalion counts to fit current combat and supply rules while preserving each role and its relative cost.
A revision changes the authoritative recipe and all related budget examples together.

A country receives the template definitions only when it earns the appropriate organizational capability.
It receives no free full-strength copy of each template.
Converting existing units uses native template and reinforcement behavior with the actual manpower and equipment consequences.
A conversion cannot refund losses, duplicate veterans, or turn a few cavalry squadrons into a fully equipped motorized group.

The foot plastun identity is especially important for Kuban content.
The historical host included infantry scouts alongside cavalry.
That supports a distinct training and employment program.
It does not justify a universal special-forces multiplier.
The historical basis is the [Kuban Cossack Host entry](https://www.encyclopediaofukraine.com/display.asp?linkpath=pages%5CK%5CU%5CKubanCossackHost).

## Opening order of battle

Part 03 owns the dynamic muster formula, immutable snapshot, exact receipts, and roster packing.
The opening must preserve at least 20 percent of the final delivered manpower authorization as replacement manpower.
At least 70 percent of the initial fielded combat manpower is cavalry.
A small infantry component replaces part of that budget when the budget permits it.
It never arrives as an extra uncosted formation.

The smallest accepted rising fields a viable native formation and retains replacements.
A larger state under a stronger, destabilized authority can field several small formations.
The opening has at most eight divisions.
A larger formula result improves the total authorized manpower and equipment within its caps rather than multiplying fixed full-strength divisions.

The opening force should have a clear practical order.
It protects the capital, one deployment or supply corridor, and the approaches needed for negotiation or survival.
It is not placed across every newly acquired or claimed state.
The spawn transaction transfers only one state.

Initial experience represents a mixture of military veterans and irregular recruits.
The force begins below the standard of a fully professional army.
Actual defecting formations preserve their appropriate experience only through the audited defection route.
A local mobilization grant does not claim the combat history of a unit that never existed.

The old authority keeps its other troops.
Units already in the transferred state must follow a specifically validated retreat, removal from the selected province, or war-participation rule.
The design does not delete an enemy army to make room for the host.

## Military development programs

### M01. Cadres and service register

This is the first common military program.
It identifies serving households, current volunteers, professional instructors, and troops that must remain near home.
It establishes reliable unit organization without changing the state's total population.

The proposed cost is 20 Army Experience and 40 Political Power.
The associated 120-day mission requires at least two functioning formations or the entire smaller opening force to complete native training and retain adequate equipment.
Training uses actual native experience and equipment loss.
Completing the program unlocks the mature T01 template and the first limited adoption slot for another host tradition.
It improves Host Cohesion by 5 once if the agreed service obligations were honored.

The program fails or suspends if the capital is lost or the force is destroyed.
The state can recover by rebuilding a viable cadre.
It does not regain the original muster grant.

### M02. Foot reconnaissance and plastun school

A Kuban founding tradition can begin this after the first service register.
Another host needs actual Kuban or relevant infantry-scout contact and an adopted training agreement.
The program costs 25 Army Experience, 50 Political Power, and 150 support equipment.
It takes 150 days and requires an equipped infantry formation assigned to the exercise.

At the funded start, expose the provisional T02 native infantry template or an audited compatible existing template so the required formation can actually be recruited, converted and trained.
That template access grants no unit, manpower or equipment.
Completion records the trained T02 capability and replaces the appropriate military spirit tier with a reconnaissance-oriented version.
Its proposed advantage is at most 5 percent in one selected relevant reconnaissance, entrenchment, or terrain-related native effect.
The implementer must verify that the modifier actually affects the intended units and cannot leak to unrelated forces.
Where a clean unit-specific binding does not exist, use a narrower training or template benefit rather than a misleading nationwide terrain buff.

The field army temporarily loses the use of its training formation.
A country cannot assign the same division to two simultaneous schools.
This physical commitment is part of the cost.

### M03. Artillery and engineering cooperation

This common program teaches the mounted and foot formations to work with ordinary artillery and engineers.
It costs 30 Army Experience and 60 Political Power and requires delivery of the actual selected support equipment and artillery allowance through normal production or a real supplier.
The equipment delivery is the mission objective rather than an invented third price if the project already uses the maximum allowed price display.

The 150-day mission completes after a combined exercise and adequate replacement stock for the selected support package.
It unlocks support additions to T01 and T02 and relevant native research bonuses where the current focus system supports them.
Any research bonus is limited to the named conventional technology family and consumed once.
It does not grant the donor's whole technology tree.

The player chooses whether scarce artillery strengthens a field regiment or a territorial defense group.
That choice changes the army's practical role.
There is no universal all-army attack reward.

### M04. Common standards between hosts

This program is available after a second tradition or an actual allied-host training agreement.
It costs 60 Political Power and 25 Army Experience and lasts 180 days.
Its objective is a shared equipment model or a workable supply agreement between the participating units.
Different models can remain where native reinforcement supports them.
The important requirement is an actual sustainable supply plan.

Completion unlocks coordinated training and a limited common operation request.
It can remove a temporary incompatible-command penalty introduced by the corresponding agreement.
It does not stack a fresh permanent bonus for every host admitted.

A partner that refuses standardization can keep its own forces.
The principal host may accept a slower coalition or pay for a separate support arrangement.
Forced conversion breaches the partner's charter if that charter reserved military organization.

### M05. Motorized reserve

This program is optional.
A host needs a reliable truck source, a viable fuel position, completed staff training, and enough remaining home defense.
It costs 75 Political Power and 35 Army Experience.
The 180-day mission requires production or actual delivery of the T04 equipment allowance and the native training of one mobile formation.

At the funded start, expose provisional T04 or an audited compatible native motorized template after its real technology prerequisites pass.
This permits the required recruitment, conversion and training without granting a formation, technology or equipment.
Completion records the trained T04 capability and its ordinary reinforcement rules.
An interrupted school does not delete a legitimate native template or recreate any resources, while the unearned doctrine benefit stays unavailable.
The state may convert a selected existing formation through native mechanics.
It receives no free trucks, fuel, manpower, or armored units on top of that conversion.

The AI must compare truck replacement and fuel consumption with the country's actual available supply.
A mounted army with support weapons is a viable endpoint.
Motorization is not a mandatory badge of competence.

### M06. Armor and mechanized cooperation

A major successor state or a well-supported regional host can pursue this after the motorized program.
It requires actual conventional research, armor production or delivered purchases, maintenance capacity, and a usable combined-arms doctrine path.
It is not a unique Cossack technology tree.

A 180-day exercise costs 40 Army Experience and 80 Political Power.
The mission requires the selected native armored or mechanized force to exist and retain an adequate equipment ratio.
Its reward is one limited research or training advantage for the selected family and a staff integration outcome.
It does not supply a tank army.

A country unable to afford the program can keep cavalry for reconnaissance, reserve work, and operations where its mobility remains useful.
The game should not punish an economically sensible force composition by locking all political endings behind tanks.

## Tradition adoption and stacking

The founding tradition is a durable identity and a source of contextual content.
The host can adopt at most two additional traditions.
A contact, joint service, invited cadre, or admitted host supplies the connection.
A map claim or historical enthusiasm does not.

The first adoption requires 120 to 180 days of funded training or institutional exchange.
The second requires a mature state and a separate 180-day program.
Each uses actual instructors, equipment, a participating formation or civil institution, and a charter that defines the relationship.
The exact action appears in part 08.

Adoption adds a distinctive option or replaces a selected military emphasis.
It does not award a permanent all-stat bonus for every tradition.
The player chooses one current doctrine emphasis from the accepted tradition combinations.
Changing that emphasis costs time and Army Experience and retrains the affected formation.

An adopted host retains its own history and partners.
Kuban plastun methods do not make the Don government Ukrainian by default.
A Siberian transport program does not grant eastern territorial sovereignty.
Nekrasov civilian sanctuary does not create a special military race.

## Raiding as bounded military work

Two native raid mission families carry the raiding fantasy.
Their exact engine definitions, actor and target scopes, native costs, and settlement receipts are owned by part 03.
The ordinary decisions only prepare or reveal those native operations.
They do not create a duplicate decision-based raid system.

| Raid family | Intended military objective | Required physical basis | Bounded result | Main counterplay |
| --- | --- | --- | --- | --- |
| R01 | Infrastructure Disruption at a valid military logistics target | Host access to a valid hostile border target, an eligible trained formation, and native operation resources | Only the bounded infrastructure damage by outcome tier in part 03, without equipment capture | Target defense, security, interception and actual operation losses |
| R02 | Military Stores Capture, with a coastal or river extraction adapter only where verified | A valid hostile military-store target and actual land access, or a separately verified usable river or coastal route with required native craft | Measured capture bounded at 400 compatible rifles or 30 support equipment and the actual victim debit, with no extra infrastructure payoff | Target security, escort strength, blocked access, and actual operation risk |

The missions target hostile military resources under valid diplomatic and war conditions.
The two baseline missions are ordinary frontier land raids.
The coastal and river extraction treatment belongs to R02 and activates only after the exact native route, craft, cost, and callback support has been proved.
A missing adapter leaves the real land mission available and cannot be disguised as a completed naval operation.
An ally, own subject, protected treaty partner or current truce partner remains excluded under part 03.
Incurring a charter breach does not itself make that actor a valid raid target.
Any required relationship must first lawfully end or change, and the target must independently satisfy the native war or accepted unresolved-dispute conditions after fresh revalidation.
A peaceful country is not silently treated as already at war.

Equipment capture uses a measured source and a compatible model.
The raid cannot remove equipment from a national stockpile that the target no longer possesses.
It cannot repeatedly harvest the same depot through reload, parallel raid instances, or a captured state.
The victim and actor receive matching receipt information.

Civilian plunder is a failure of the host's settlement.
If a narrative incident offers coercive requisition, its loss of Legitimacy and specific diplomatic or local consequences remain visible.
The route does not make unbounded civilian destruction the best way to finance the state.
Deaths, if actually caused by an implemented event, use the shared measured death contract and are not credited twice.

The host can succeed as a raiding tradition through reconnaissance, supply disruption, interception, and limited recovery of military material.
Its stronger regular army can eventually rely less on raids.
The content should reward professional restraint and reliable logistics as well as daring.

## The service economy

### A finite local beginning

The starting state transfers its actual buildings.
The event does not copy the losing country's factories or receive a second industrial complex through country history.
The finite local cache and local mobilization allowance are disclosed as scripted founding resources.
Actual source transfers are recorded separately.
The player can see which resources came from which origin.

The early one-time workshop bridge is owned by part 03.
Its purpose is to prevent a viable but industrially poor host from depending permanently on repeated gifts.
Its output is one ordinary military factory in the actual selected state after the construction objective and valid slot checks.
The bridge cannot be repeated after moving the capital, changing the country's name, or reforming the government.
It does not replace the normal construction economy.

A host that already has adequate military production can use the corresponding organizational or repair objective instead.
It does not receive both a free replacement project and the original factory.
The source state and target building must be explicit.

### E01. Agricultural service rotation

The host agrees which formations remain near home and when extended service is justified.
A 45 Political Power policy and a 120-day mission require honoring the selected home-service arrangement while recovering the productive base.
Completion can replace an emergency economic penalty with the ordinary service economy tier.
It does not add a new permanent bonus on top of that tier.

Calling the protected formations into an external offensive is possible under a declared emergency.
It breaks or suspends the corresponding agreement and triggers its visible political consequence.
The same troops cannot count as deployed abroad and performing home service.

### E02. Workshops and repair districts

Once basic production exists, the state can specialize in infantry equipment and support repair or in transport and later vehicle maintenance.
A 60 Political Power, 150-day program requires an actual construction, conversion, or production milestone.
The reward is one limited production or repair advantage, proposed at no more than 5 percent in its selected native family.

The player must choose the factory allocation.
The program cannot promise both a major arsenal and a large truck industry to a one-state economy.
Ordinary civilian and military factory totals remain the capacity constraint.

### E03. River and port revenues

Don, Kuban, Ural, and Pontic content can use actual river access, transport improvements, trade agreements, and ports.
The game does not have a fish or customs currency added for this event.
Revenue is represented through the ordinary economic rules and a small conditional economic modifier.

The benefit requires the named access and commercial settlement to remain valid.
Losing the port or breaching the passage agreement suspends the related benefit.
It does not delete completed buildings or compensate the country with an unrelated inland factory.

### E04. Land and civilian reconstruction

The state must settle the relationship between serving households, existing residents, returning families, municipalities, and allied communities.
One common 180-day reconstruction mission supports each major postwar settlement.
Its cost is 60 Political Power plus the selected actual construction or delivered support requirement.
No more than four distinct spendable types are attached to one action.

An inclusive settlement can improve Legitimacy while reducing support among those expecting exclusive military privileges.
A service-estate settlement can retain Cohesion while delaying wider acceptance.
The event resolves those changes through the two public values and specific commitments.
It does not invent a separate estate influence meter.

Property changes are political settlements within the game's represented population and state systems.
They do not create or destroy people.
Any physical relocation follows the exact state-ledger route and requires a real destination.

### E05. Education and technical capacity

A new generic host begins with two research slots.
An admitted preexisting carrier preserves a legitimate existing slot count, subject to the shared country adapter.
The event does not downgrade a living or meaningfully initialized carrier for visual consistency.

A third-slot program requires an established host, a civilian education or technical institution, at least two working civilian factories in the actual country or an accepted sustained sponsor arrangement, and a real arms-production or repair base.
The proposed preparation costs 100 Political Power and takes 180 days.
It grants the third slot once.

A fourth slot belongs to a mature national or federal project with at least six working civilian factories or an explicitly audited equivalent joint research institution, broad civilian representation, and a second 180-day institution program.
A tiny isolated host cannot buy a major-power research establishment with Political Power alone.
No fifth slot is granted by Event 112.

Research assistance uses specific conventional fields and a finite licensed or bonus route.
It never applies an unrestricted technology union to a returning officer, an adopted tradition, or a captured province.
A full sovereign merger needs a separate explicit technology continuity policy.

## Arms purchases, sponsors, and volunteers

A supplier must be a real country with suitable equipment and a usable delivery route.
An offer records equipment model, quantity, delivery deadline, consideration, passage, and cancellation.
The host pays the agreed price through the same quoted-cost contract used by other actions.
The supplier's actual debit and the host's actual receipt must agree.

A sponsor can provide staff training, equipment, a production license where supported, or a defensive guarantee.
It receives the specific concession in the agreement.
An unrelated offensive expedition, permanent base, or exclusive port access cannot be smuggled into a generic friendship modifier.

Arms delivery fails if the stock disappears, the route closes, or the supplier withdraws under the agreed terms.
The system records a partial delivery and applies the agreed refund or renegotiation to the undelivered part.
It does not convert every failed delivery into a full local cache.

Military volunteers are finite actual people.
Civilian returnees remain civilians until they enter an ordinary and permitted recruitment process.
The existence of a community does not authorize the host to seize every adult as manpower.
Part 03 distinguishes military-pool transfers, existing unit defections, civilian movement, and symbolic diplomatic support.

## Three visible event-owned spirit slots

The event keeps its own country-level spirit presentation compact.
Other unrelated game systems retain their own ideas.

| Slot | Scope | Proposed finite progression | Stacking rule |
| --- | --- | --- | --- |
| S01 | Institutions and service settlement | Emergency host, ratified charter, selected regional or national constitution | New constitutional tier replaces the previous tier |
| S02 | Army organization | Irregular muster, registered cadres, selected modern doctrine emphasis | One current military emphasis, with retraining to switch |
| S03 | Civil economy and reconstruction | A temporary crisis tier only when applicable, working service economy, selected mature specialization | One current economic tier, with access-dependent benefits suspended when their conditions fail |

The opening normally uses S01 and S02.
A severe existing local economic crisis can justify S03 immediately.
Focus rewards upgrade or replace these slots.
They do not accumulate a separate spirit for each host, workshop, congress, officer, treaty, and victory.

Short-lived operational conditions should use the narrowest supported state, unit, decision, or mission surface.
They must not disguise additional persistent public management values.
Every temporary condition has an explicit expiry and cleanup owner.
Expiry is based on elapsed campaign time and the actual native duration contract.

## Illustrative campaign choices

A small Don host can remain largely mounted, protect its capital with territorial infantry, and finance artillery through one military factory and a real arms agreement.
Its civilian route can become a durable regional republic before considering Moscow.

A Kuban host can invest early in plastun infantry and port recovery.
Its slower territorial consolidation may be more sustainable than immediately converting the cavalry into motorized units.
A Ukrainian federation is a political choice after that recovery, with actual partner terms.

A Ural host can preserve enough people near the river to maintain its economic base.
Sending every formation west may yield a short military opportunity while destroying the capacity to replace losses.
Its later coalition can succeed through accepted passage and defense agreements.

A Golden Horde claimant can use cavalry to secure communications while building a Lower Volga arsenal and negotiated partner contingents.
The title itself adds no industrial capacity.
An unrecognized empire with empty depots should face the same practical limitations as another country with empty depots.

## Acceptance criteria

The military package passes only when the exact native templates, fielded inventories, reserves, training costs, and reinforcement paths reconcile.
A trained formation cannot be simultaneously deployed, transferred, counted in two schools, and pledged as a home garrison.
A cosmetic change cannot alter its physical inventory.
The AI must be able to train, equip, maintain, and replace the same force the player receives.

The economic package passes only when every production benefit has a real industrial or contractual basis and every building reward is bounded and placed in a valid state.
A lost capital, annexed partner, failed delivery, or suspended access agreement must leave a coherent country.
No returnee, tradition, raid, government change, or formation action may reset the finite opening cache.


## Postwar cost precedence

E04 and A21 use the common 60 Political Power, 180-day reconstruction review only where the original P or GP promise has no more specific priced contract.
A combined regional and great-project review of the same actual promise uses that original owner and one payment, objective and failure receipt.
The concrete eight-project default review and A19 recovery contracts are in part 05.
