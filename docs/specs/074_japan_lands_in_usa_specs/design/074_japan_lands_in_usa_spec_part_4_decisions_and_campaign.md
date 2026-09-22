# Part 4: Japanese operations and American emergency defense

## Two compact decision categories

Japan receives an operations category and the United States receives an emergency-defense category after the landing commits.
These are working descriptions of the categories, not final names.
Each contains a small set of contextual actions and up to two current missions.
The selected region appears through normal state targeting or a bounded target selector supported by the existing decision framework.
Do not show a separate copy of every action for every western state at once.

Japan normally sees four primary actions.
The United States normally sees five.
Completed one-time projects disappear, unavailable later-phase actions stay hidden, and relevant but temporarily unaffordable actions remain visible with a clear reason.
Neither category requires a new scripted GUI.

Every cost below is a proposed tuning anchor.
A displayed cost, affordability check, and actual debit must agree, including after save reloads and changes in universal cost modifiers.
No action has more than four spendable cost types.
The inline row uses the proper texticons and at most three values.
A fourth cost belongs in the complete tooltip and remains part of the same single transaction.

## Ordinary project access and mission acceleration

The first authorized J03 corridor project, U01 defense batch, and U03 railway project are available immediately when their map and resource conditions permit.
A second or later project in each family normally waits until 60 days after the previous successful project or delivered batch in that family.
Only one project in a family can be preparing at a time.
If an evolution raises the lifetime allowance after that wait has already elapsed, the next project is immediately available.

J-M1 opens the next authorized J03 project early.
J-M3 opens the next authorized J03 project early again, with the same lifetime ceiling.
At most one unused early-access permission is held in each family, so two mission completions cannot create two simultaneous projects.
U-M1 opens the next authorized U01 batch and U03 railway project early.
A permission only removes the waiting date for an already authorized next project.
It does not add to the allowance, bypass resources, or survive campaign closure.
When no authorized project remains, the mission's reward is its actual territorial or defensive achievement and truthful report.

## Japanese actions

### J01: Receive a follow-on echelon

The player requests one batch of five authorized follow-on divisions at a selected working access point.
The batch has already been counted in the tier's lifetime ceiling.
The first request normally becomes available after day 30, requires enough remaining allowance and local capacity, and starts a 30-day request cooldown.
Mission J-M1 may once advance the next request date by 15 days under Part 3's timing rule.

Proposed cost is 25 Command Power, 50 convoys, and 500 trucks.
The force appears after ten days of organization at the access point.
Its embedded manpower and equipment follow Part 3's grant accounting, so the player is not charged a second full formation manifest.
The transport cost is a deliberate sacrifice to bring reserved forces into the theater.

At the request, debit and record the exact effective costs once as reserved transport resources.
If access or the bilateral war becomes invalid before delivery, cancel the request, refund that exact reservation once, and leave the units unissued.
No field benefit has begun during this organization period.
At delivery, recheck access and capacity, consume the reservation, and record the issued force in one nonyielding transaction.
Do not debit the reservation again at delivery or refund it after the force has appeared.

The AI strongly prefers this action when it has active front pressure and room for the batch.
It has zero willingness when the access point is lost, supply is inadequate, the allowance is exhausted, or the support episode has closed.

### J02: Restore an unloading point

Repair a damaged registered Japanese port and its immediate local distribution.
Proposed cost is 750 support equipment, 500 trucks, and 25 Command Power.
The project takes 20 days and repairs the selected facility up to its recorded landing or completed-project level.
It does not raise every port to a maximum level or construct an unlimited new supply hub.

Allow one emergency restoration per registered port during this episode.
Ordinary construction remains available after that.
If the port is captured while the work is underway, the project fails and the spent field materials are lost.
No part of the repair should restore a neutral or American-held facility for Japan.

The strategic tradeoff is clear: the player sacrifices equipment that could reinforce the army to keep a threatened transport anchor useful.
The AI prioritizes this above a new offensive when port damage is the main cause of supply failure.

### J03: Repair a captured transport corridor

Select one real, Japanese-controlled route from a working port toward a front-adjacent hub or important junction.
Proposed cost is 1,000 trucks, 25 trains, and 500 support equipment.
The work takes 30 days, repairs damaged links, and can raise a short deficient section to a modest verified operating level.

The route is recorded when work begins.
The action cannot create a railway through enemy territory or repair unrelated lines on the other side of the country.
Limit the episode to one completed project at baseline, two at tier I, three at tier II, and four at tier III.
An evolution raises the lifetime project allowance without clearing earlier completed projects.

Losing an essential route segment interrupts the work.
Successful reconstruction gives the army actual transport capacity and access to ordinary supply.
A second project cannot repeatedly collect benefits from the same repaired segment.

The AI uses this when it has expanded beyond the initial pocket and the chosen route supports a real front.
It does not spend trains on a redundant line while a principal port is about to fall.

### J04: Prepare the next offensive

Commit resources to one selected, reachable coastal or inland operation.
Proposed cost is 35 Command Power and 100,000 fuel.
Preparation takes ten days and provides 30 days of local operational support, with a 45-day cooldown after completion.

The intended benefit is faster concentration and recovery around that specific operation, with a modest local movement benefit around ten percent where the engine can scope it correctly.
It is not an attack bonus for every Japanese formation in the world.
The implementation must prove the local consumer before assigning exact combat or planning modifiers.
The main benefit remains a properly supplied, concentrated army moving toward a useful objective.

Only one operation can receive this preparation at a time.
Changing the objective does not stack the benefit or restore the spent fuel.
If the target becomes legally invalid, cancel remaining preparation without inventing a new enemy.
If the operation simply loses in combat, the investment is spent.

The AI uses the action when its local supply is satisfactory, there is a reachable target, and it is ready to commit.
A supply emergency outranks this purchase.

## United States actions

### U01: Mobilize regional defense formations

Raise a batch of five ordinary defensive infantry divisions in a safe American-controlled western or adjacent inland area.
Use a modest formation with limited offensive power and a short organization period of 20 days.
The exact manpower, infantry equipment, and support-equipment cost comes from the validated template manifest, plus 50 Political Power.
These are four spendable cost types.

The proposed lifetime limits are 5, 10, 15, and 20 emergency divisions at the four tiers.
All come from actual American resources.
They provide a useful local response without matching the Japanese grant division for division.
They are not a substitute for moving regular American forces toward the mainland front.

A unit must not appear in an enemy-held city, an overrun assembly area, or a province that has become inaccessible during organization.
A legal alternative within the same defense region can be selected before the final transaction.
If none exists, return the exact reserved manpower, equipment, and Political Power once and keep the unfulfilled allowance available.
Reserve the effective costs when organization begins, consume that reservation only when the force appears, and never refund a completed formation.

The AI gives this high priority when the region is exposed, the ordinary army is insufficient, and it can afford the full batch without a severe existing equipment deficit.
It must not repeatedly spend scarce equipment on new formations while leaving the frontline army empty.

### U02: Prepare a threatened city

Choose one American-controlled city or adjacent defensive approach outside the initial scripted footprint.
Proposed cost is 1,000 infantry equipment, 500 support equipment, and 25 Command Power.
Work takes 20 days and provides a modest defensive position through legal land-fort construction and a temporary local defensive-preparation benefit where supported.

Limit completed projects to one at baseline, two at tier I, and three at tiers II and III.
A city can receive the emergency project only once.
Existing stronger forts are preserved and are never reduced to the project's level.
A captured city is not fortified remotely for the former controller.

The choice trades equipment and attention for a defensible approach.
A city without a route to the American interior is a poor candidate, and the AI should normally prefer a connected position over a surrounded prestige objective.

### U03: Give the western railway system priority

Restore a real American-controlled corridor from the interior toward an active western defense sector.
Proposed cost is 1,000 trucks, 25 trains, and 25 Political Power.
The project takes 30 days and repairs a bounded chain of existing transport links.

Allow one completed corridor at baseline and tier I, two at tier II, and three at tier III.
Different projects must improve distinct meaningful routes.
The action has no effect on enemy-held sections and cannot supply a pocket across an occupied gap.
It provides an alternative to simply raising more divisions in an already undersupplied theater.

The AI values it when a real American concentration is limited by inland transport and the route can reach that concentration.

### U04: Prepare a counterattack on the bridgehead

Choose one connected Japanese pocket or a key route that can isolate it.
Proposed cost is 30 Command Power, 100,000 fuel, and 250 support equipment.
The action requires a credible American force near the operation, takes ten days to prepare, and supports a 30-day local counterattack window.

The intended effect is a bounded improvement to local concentration and planning through supported consumers.
It never transfers the target port by script, destroys Japanese divisions, drains Japanese organization, or guarantees a successful attack.
The target remains a normal battle.

Use a 60-day cooldown and prevent overlapping counterattack benefits.
The AI prefers an exposed corridor or damaged isolated pocket over a well-supplied concentration with overwhelming local strength.
The tactical result remains uncertain.

### U05: Protect another Pacific port

Fortify one American-controlled Pacific access point outside the initial footprint before Japan reaches it.
Proposed cost is 50 Political Power, 1,000 infantry equipment, and 250 support equipment.
Preparation takes 30 days and adds a modest coastal defensive position, preserving stronger existing works.

Allow one project at baseline and tier I, two at tier II, and three at tier III.
This action makes secondary ports harder to take through normal combat.
It does not block Event 074 retroactively, make every coast immune, or create a second guaranteed Japanese landing.
After the initial event, additional Japanese entry points must be won normally.

The AI chooses a port whose loss would expose another route or threaten the supply of an existing American defense.
It should not spend the project on a remote port irrelevant to the actual front.

## Mission J-M1: Consolidate the landing

Start at landing for Japan with a 120-day deadline.
Select a principal opening access point and a useful port or transport junction outside the scripted footprint.
Japan succeeds by retaining the opening access point, capturing the new objective, establishing a valid connection, and keeping that arrangement for 20 continuous days.

On success, advance the next request date for one still-unissued follow-on batch by 15 days under Part 3's floor, and unlock the next transport project within the existing lifetime allowance.
If the batch is already available, the benefit is the transport-project access and the actual improved map position.
Do not award a second army or an extra copy of captured equipment.

On failure, the army remains, normal combat continues, and that early unlock is lost.
Existing support still tapers on schedule.
After a successful J01 delivery or completion of a paid field project, combat losses never refund the completed work.
A cancelled or externally invalid target does not count as a failed military operation.

## Mission J-M2: Connect the western positions

Use this mission when at least two detached high-tier pockets exist.
Allow 180 days to connect two specified operating areas through Japanese-controlled land while retaining a working access point in each.
The connection must persist for 15 continuous days.

Successful play permits pooled use of the remaining reserved deliveries across the connected area and enables the next inland objective.
The physical land connection is the main reward because it protects against losing one port.
The mission never creates that connection itself.
Failure leaves the pockets dependent on their own surviving access and does not refresh their support clocks.

## Mission J-M3: Open an inland operating route

After consolidation, select an inland supply objective outside the original coastal footprint.
Allow 210 days to capture it and keep a real connection to a working Pacific access point for 30 continuous days.
This replaces the completed first mission rather than creating a third parallel mission.

Success unlocks the final available corridor project and a one-time contextual report about the inland campaign.
It can satisfy an event-specific Chaos milestone only when the required actual territorial gains occur.
It does not annex an inland state, force a peace conference, or grant another tier.

## Mission U-M1: Keep the western defense connected

Select one or two important American-controlled defense objectives outside the initial footprint and a valid route toward the interior.
The mission lasts 120 days.
Maintain the designated core defense arrangement for the last 60 continuous days of that window.
A breach resets the hold count without moving the absolute deadline.

Success makes the next already-authorized regional defense batch available and permits the next railway project within their lifetime limits.
This is useful preparation for a counteroffensive, not a guaranteed removal of Japan.
Failure loses the early access opportunity but does not delete regular American forces or apply a nationwide collapse penalty.

## Mission U-M2: Recover the landing coast

Use deadlines of 180, 210, 240, and 300 days from the original landing for the four tiers.
Recover every initially seized access point to non-Japanese control and deny Japan any working Pacific access for 30 continuous days.
Where the United States' allies fight on its side, legitimate allied liberation counts for this mission, but neutral conquest is reported as a different outcome.

An active evolution can move the deadline to the higher tier's absolute deadline.
It does not grant a fresh full duration from the upgrade date.
Success closes special Japanese support under the same normal access-loss rules and records the American recovery.
The Japanese-American war continues.
Failure keeps the ordinary war open and adds no scripted free Japanese territory or replacement army.

## Resolution and presentation rules

Mission completion is automatic when its real objective and hold duration are satisfied.
Do not require another click to claim an already completed military objective.
Distinguish completion, partial progress, defeat, target invalidation, and cancellation.
A partial outcome preserves whatever was genuinely repaired or captured and gives no unearned full reward.

Player-facing descriptions state the operation and its consequence.
Tooltips carry exact targets, costs, dates, remaining allowance, and blocked reasons.
Category descriptions must not become long administrative summaries.
The AI uses the same costs, targets, deadlines, and lifetime ceilings as the player.
