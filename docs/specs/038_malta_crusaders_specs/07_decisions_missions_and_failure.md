# Decisions, missions, and failure recovery

## Decision design principles

Event 38 decisions are military, political, logistical, territorial, religious, and diplomatic actions.
They are not a store where political power buys small modifiers.

Each phase shows three to five primary actions, with six as the hard maximum, and one to three missions can be active.
An action has at most four spendable cost types.
Costs are icon-first, and complex requirements use a concise summary with named-state tooltips.
The full action list with IDs, costs, and risks is `25_decision_register.md`, which owns the row-level detail.
This file owns the principles, the phase structure, and the rules behind them.

A decision exists only when it asks the player to choose between real alternatives or to commit scarce resources to a risk.
These were removed as busywork: preparation chains that each unlock the next click (coast surveys, local contacts, landing-fleet and depot staging before a regional crusade), repeated construction slots (depots, remount services, siege workshops), and one-click temporary supply boosts.
Their costs and requirements moved into the action they used to precede.

## Decision categories

1. **The Crusade Council** for order, relic, and government actions.
2. **Mediterranean Campaigns** for target selection, regional crusades, logistics, and settlements.
3. **Crusader Principalities** for subject obligations and disputes.
4. **The Eleventh Crusade**, only during failure recovery.
5. **The Holy World**, only during public terminal preparation and the terminal war.

There is no category per order or region.
Target selectors and phase visibility keep the categories readable.

## Council actions

The Crusade Council category offers the demand answers (Accept, Compromise, Refuse), Convene Joint Command, Arbitrate Jerusalem, Reform the Crusade Council, Name the Dominant Order, and a few route-specific actions listed in the register.
The mechanics behind them are in `04_crusade_council_mechanic.md`.

### Convene Joint Command

**Purpose:** raise Cohesion and coordinate a front.
**Requirements:** Cohesion of 50 or more, at least two seated orders, and no recent failed conference.
**Costs:** command power, army experience, and a short planning delay.
**Success:** raises Cohesion and gives a timed mixed-order command bonus.
**Failure:** exposes the rivalry, opens an incident, and lowers Command Standing by one step for 90 days.

### Arbitrate Jerusalem

**Purpose:** settle competing claims over sacred and administrative control.
**Requirements:** Jerusalem held for 120 days and at least one claimant order.
**Outcomes:** central administration, order custody, principality custody, a local church compact, or Papal administration.
**Consequences:** large Cohesion and Legitimacy movement.
It is not repeatable without a major constitutional change.

### Reform the Crusade Council

**Purpose:** enact the settlement chosen by focuses.
**Requirements:** route focus, Functional standing or better, and no open incident.
**Result:** transforms opening ideas, changes decision families, and may install a dominant order or confederation.

## Logistics actions

Logistics has four actions.
Each is a timed mission with a real failure outcome.

### Escort the Sea Road

**Goal:** protect a named sea route for 120 to 180 days.
**Costs:** fuel, convoys, and naval commitment.
**Success:** keeps the sea-road anchor safe and improves supply.
**Failure:** convoy losses, delayed reinforcements, and a risk to the sea-road anchor.

### Repair the Holy Land Rail

**Goal:** control and repair named rail and supply nodes and the depot they feed.
**Costs:** trains, support equipment, and civilian factory commitment.
**Duration:** 120 to 180 days depending on damage and war.
**Success:** visible infrastructure improvement and lower future campaign costs.

### Fortify a Port

**Target:** one selected eligible coastal state, including Malta after bombing.
**Costs:** civilian capacity, equipment, and time.
**Result:** naval base repair, coastal defence, and order headquarters eligibility.
**Limit:** a bounded project ledger per region prevents port spam.

### Emergency Air Bridge

**Availability:** land and sea routes are blocked or severely disrupted.
**Costs:** transport aircraft, fuel, and air commitment.
**Result:** limited supply relief and evacuation support, with a risk of aircraft loss.

## Recruitment actions

### Raise a banner

One action per family (Armored Knights, Mounted Knights, Ranged Company covering Archers and Crossbows by technology, Siege Host, Blessed Guard, Crusader Engineers).
**Requirements:** provider eligibility, order capacity, manpower, complete equipment, and a training state.
**Costs:** equipment, manpower, army experience, and training time.
**Result:** one formation only after the mission completes, never an instant free unit.

### Convert captured equipment

**Target:** a selected captured stockpile family.
**Costs:** captured equipment and factory burden.
**Result:** crusader equipment at a dynamic conversion rate, with a loss on every conversion so the action never produces net value.

### Request foreign equipment

**Requirements:** an eligible sponsor.
**Costs:** diplomatic obligation, convoys, or sponsor influence.
**Result:** a bounded equipment or convoy package with a cooldown and refusal memory.

## Campaign actions

The human player selects one regional objective at a time, and the AI evaluates every valid target directly.
Target families are Jerusalem and Jordan restoration, the Levantine frontier, Cyprus and the Aegean, southern Anatolia and Cilicia, the Greek mainland, North African ports, and Rome under valid routes.
Selecting a target activates only its relevant actions and missions.

### Issue Crusader Ultimatum

**Requirements:** Functional standing or better and a credible force.
**Outcome:** the target accepts, bargains, or refuses, and a refusal leaves the regional crusade available.

### Launch the Regional Crusade

**Requirements:** a selected valid target, supplied forces, convoys and fuel for the crossing when the target is overseas, and no duplicate war.
**Costs:** command power and an equipment reserve.
**Result:** a limited war or intervention.
It never declares against every holder in one step.

### Request Papal Blessing and Call Foreign Chapters

Request Papal Blessing needs a Papal relation and yields Legitimacy and volunteers with Papal conditions.
Call Foreign Chapters needs Evolution I and yields officers and volunteers at a sponsor obligation.

## Hold and secure missions

Mission timers are 90 days at the shortest outside a real emergency.
Examples are Hold Jerusalem for 120 days, Keep Malta Connected for 150 days, Guard the Jordan Corridor, Protect the Grand Harbour, Break a Named Fortress Line with a Siege Host, and Relieve a Principality Capital.
Missions are the register's `mission_*` rows.

## Settlement actions

After victory, the player chooses a governance form for each eligible region.

| Form | Benefit | Cost |
| --- | --- | --- |
| Direct commandery | direct output and military access | occupation burden, resistance, lower Cohesion if orders expected land |
| Grant to an order | specialist units and local administration | order autonomy and rival grievance |
| Charter a principality | local recruitment, lower occupation burden | lower direct output and succession risk |
| Restore local Christian government | Legitimacy and local acceptance | reduced direct control |
| Papal administration | Legitimacy and Papal route support | clerical control and church disputes |
| Return under treaty | peace, lower Condemnation, possible small Chaos reduction | territorial ambition and a Command Standing step for 90 days |

The settlement freezes the selected region and owner facts before applying effects and cannot be used twice on the same settlement generation.

## Relic actions

Relic actions exist only from Evolution III and are limited to four: Sponsor an Expedition, Examine the Claim, Display in Jerusalem, and Transfer Custody (to an order, to Jerusalem, or to the Pope).
Protecting the pilgrimage route is a mission, not a repeatable action.
Details are in `04_crusade_council_mechanic.md`.

## Eleventh Crusade failure route

### Activation

The category activates when any of these holds for a sustained period:

- Jerusalem and the Holy Land command are lost
- Malta controls fewer than the minimum expeditionary footholds
- the maritime bridge is lost and no alternative route exists
- Command Standing stays Fractured after a major defeat

A one-day occupation change never triggers it.

### Phases

**Phase 1, Count the survivors.** Evacuate exposed orders, fortify Malta (which also consolidates equipment), and optionally seek temporary refuge.
The mission is to preserve a trained core and one viable port.

**Phase 2, Rebuild the crusade.** Call for volunteers, rebuild transports and reopen workshops, and select a new landing target.
The mission is to assemble a dynamic invasion package.

**Phase 3, Launch the Eleventh Crusade.** Launching stages the fleet, secures local allies where they exist, and lands the knight banners in one action with a hold mission afterward.

**Phase 4, Settlement.** Restore Jerusalem, establish an alternative principality, negotiate a protectorate, accept a Fortress Malta ending, or dissolve the expedition into a humanitarian order state.

A second failed crusade raises costs and can close aggressive routes.
It never produces an infinite loop of free armies, and a final negotiated or island-focused route stays open when possible.
Recovery requires time, equipment, sponsors, and a real military plan, so it cannot restore the original state for free.

## Holy World decisions

Preparation and terminal decisions are in `12_holy_world_terminal.md`.
The category stays hidden until the route is publicly available.

## AI behavior

Decision AI reads the current phase and active mission, supply and equipment, Command Standing and the two meters, target strength and distance, naval access, order seats, sponsor availability, local resistance, principality loyalty, war burden, and terminal or hidden-route state.
It must not launch an invasion without a viable route and supplied force, create a principality without a valid country package, or spend scarce convoys on a relic expedition during a supply collapse.

## Exploit controls

Required controls include one regional target for human presentation, one relic expedition, one major demand, region settlement generation flags, escalating unit-raising costs, formation caps, no equipment refund above remaining strength, cooldowns after failed sponsor requests, no repeated port construction in the same slot, no duplicate war creation, cleanup after owner or target invalidation, and AI visibility separate from human target selection.

## Decision audit evidence

Completion requires category lifecycle and phased visibility, named-state tooltips, icon-first costs, meaningful success and failure, varied mission durations, one to three active missions, route-specific AI, target cleanup, save and reload persistence, an exploit audit, a probability audit for every weighted decision or target selection, and alignment with the event-owned GUI helpers.
