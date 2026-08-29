# Asteroid Incoming, Part 6: Decisions and Missions

## Presentation choice

Event 028 should use one ordinary decision category with a strong static category picture and dynamic category text. Normal decisions present the required state clearly, so the event does not need a separate mechanic window. The player manages one global dust state, one national recovery burden, and local crater objectives through normal decisions and missions.

The category should change its visible content by phase. It must never show the entire recovery system at once.

The category header should show only the values that affect immediate choices.

- Current global dust stage
- Current national protection state
- Current national impact-recovery burden when the country has damaged states
- Controlled crater-site count when Extraordinary Minerals is active

The raw Dust Load formula, every damaged state value, and every global contribution should remain in tooltips or internal ledgers.

## Phase structure

### Phase 0: Target emergency

This is the one pre-impact event described in Part 2. It is an event choice, not a decision category. The choice establishes one preparedness stance and then closes.

### Phase 1: Emergency response

Visible for countries with Ring 1, Ring 2, fragment-center, or heavy fragment damage. This phase normally lasts 90 days and can end earlier when the country resolves its urgent burdens.

The phase should show three or four primary actions and no more than two active missions.

### Phase 2: Reconstruction

Begins after the immediate emergency or when no severe rescue burden remains. It focuses on rail, supply, industry, and local recovery. It should show three primary actions and one to three named objectives.

### Phase 3: Dust protection

Visible to all ordinary countries while global dust remains. It should show up to three actions. Countries with no local impact damage should see only this part of the category.

### Phase 4: Crater competition

Visible only when Extraordinary Minerals is active and the country controls, borders, or is at war over a crater site. It should show up to three relevant actions for the selected current situation.

Obsolete phases and actions must hide cleanly.

## Emergency response actions

All labels below are working labels. Final localisation should use concise period language and dynamic state names.

### Deploy mobile hospitals

**Who sees it:** Countries with unresolved Ring 1, Ring 2, or fragment-center medical burden.

**Public purpose:** Move medical staff, field hospitals, water equipment, and transport into the worst surviving state.

**Requirements:** At least one valid affected state, enough support equipment and trucks, and a route to the target state.

**Costs:** Support equipment, trucks, manpower, and a short civilian-factory commitment.

**Effect:** Reduces continuing rescue-period deaths, lowers the target state's recovery burden, and shortens the catastrophic or heavy impact modifier. The action cannot restore immediate population losses.

**Targeting:** Prioritize the state with the largest expected preventable loss. The player should see the exact state before paying.

**AI:** High priority when preventable deaths are large and the route is supplied.

### Open an emergency rail corridor

**Who sees it:** Countries with damaged railways, infrastructure, or supply hubs in affected states.

**Public purpose:** Concentrate trains, fuel, engineers, and guarded work crews on one route from the backup capital or a safe supply hub to the disaster zone.

**Requirements:** A valid damaged route, train stock, fuel, and control of the route endpoints.

**Costs:** Trains, fuel, support equipment, and a civilian-factory commitment.

**Effect:** Repairs part of one named railway and infrastructure corridor, improves supply to rescue states, and advances the emergency-transport mission.

**AI:** Prioritize when the capital, main front, or largest population center is disconnected.

### Clear unstable debris

**Who sees it:** Countries with severe building and infrastructure damage.

**Public purpose:** Remove collapsed structures, extinguish local fires, and reopen one critical facility area.

**Requirements:** Control of the target state and no active enemy occupation at the work site.

**Costs:** Trucks, support equipment, manpower, and construction capacity.

**Effect:** Restores a bounded share of damaged infrastructure or a critical nonpermanent building, lowers continuing casualty risk, and prevents a linked secondary disaster when the work finishes in time.

**AI:** Prioritize supply hubs, rail junctions, ports, and high-population Ring 1 states.

### Distribute emergency water and filters

**Who sees it:** Countries with affected populated states or high dust exposure.

**Public purpose:** Protect drinking water, shelters, hospitals, and work sites from debris and dust.

**Requirements:** Support equipment or a project-defined civilian protection stockpile, plus a valid affected population.

**Costs:** Support equipment, convoys or trucks depending on route, and a short civilian-factory commitment.

**Effect:** Reduces local dust exposure, rescue-period deaths, and the country's national dust penalty for the emergency phase.

**AI:** Higher priority at Impact Winter and Severe Impact Winter stages.

## Emergency missions

### Keep the rescue route open

A timed mission asks the country to keep the backup capital or safe supply hub connected to the worst impact state for 120 to 180 days.

Success should:

- Remove part of the national recovery burden
- Upgrade the state's recovery modifier
- Reduce future emergency-action costs for that state

Failure should:

- Extend the state recovery modifier
- Cause a bounded rescue-period death entry
- Increase supply pressure temporarily

The mission should auto-complete when the route and supply conditions are met for the required period.

### Stabilize the damaged zone

A timed mission asks the country to repair named infrastructure, railway, or supply thresholds in its two worst affected states.

Success should move the country into reconstruction earlier. Failure should keep the emergency phase open and worsen one local burden. The mission must name the states and exact public thresholds.

## Reconstruction actions

### Rebuild a supply spine

**Who sees it:** Countries with several damaged states connected by one repairable route.

**Costs:** Trains, civilian-factory commitment, steel or support equipment when supported, and time.

**Effect:** Opens a staged project across named rail and infrastructure states. Completion restores a meaningful route and replaces local emergency modifiers with recovery modifiers.

This action should do map work. It should not be a generic national supply bonus.

### Restore outer-ring industry

**Who sees it:** Countries with surviving factories in Ring 2, Ring 3, or fragment outer rings.

**Costs:** Civilian-factory commitment, construction time, equipment or resource input, and temporary consumer-goods pressure where supported.

**Effect:** Restores part of damaged industrial levels in named states and advances a national recovery objective. Main crater buildings are never eligible.

The action should target a bounded state pool so it cannot become a cheap factory-construction loop.

### Rehouse displaced workers

**Who sees it:** Countries with large surviving populations in affected states and unresolved recovery burden.

**Costs:** Civilian-factory commitment, manpower, trains or trucks, and stability pressure.

**Effect:** Improves local construction and production recovery, shortens the impact-zone modifier, and reduces continuing national disruption.

This action does not restore dead population.

## Reconstruction missions

### Reconnect the national network

A 180 to 365 day objective asks the country to restore defined infrastructure and railway links between the capital, major industry, and damaged states.

Success replaces the national recovery idea with a lighter form and closes obsolete emergency decisions. Failure extends the recovery idea and raises future repair costs for a limited period.

### Restore the outer ring

A long objective asks the country to remove all timed Ring 3 and light fragment modifiers and to reduce Ring 2 burden below a defined threshold.

This objective supports the survival achievement. It must use actual state conditions and cannot auto-complete from pre-impact values.

### Rebuild the regional economy

A difficult objective for the original target country asks it to restore a meaningful share of surviving pre-impact industrial and logistical capacity outside the permanent crater. The pre-impact snapshot supplies the comparison baseline.

Success grants a lasting but measured recovery legacy, such as improved disaster repair speed or national resilience. It should not refund the destroyed state.

## Global dust-protection actions

### Harden factories against dust

**Who sees it:** Every ordinary country while dust is active.

**Costs:** Civilian-factory commitment, support equipment, and time.

**Effect:** Raises the national protection state and reduces the country's factory-output and production-efficiency penalties from dust.

The action can have staged versions. A later stage replaces the earlier protection state instead of stacking several ideas.

### Protect transport and reserves

**Who sees it:** Countries with low trains, convoys, fuel, or supply resilience during dust.

**Costs:** Trains or convoys, fuel, civilian-factory commitment, and temporary stability or consumer pressure.

**Effect:** Reduces the national supply penalty and improves resilience to dust-linked Event 013 disasters.

The exact transport cost should reflect whether the country relies more on land or maritime routes.

### Join the atmospheric observation network

**Who sees it:** Countries with research, radar, aircraft, or industrial capacity to contribute.

**Costs:** Civilian factories, fuel, convoys or aircraft commitment where appropriate, and time.

**Effect:** Improves weather warning, contributes a bounded amount to global dust decay, and reduces the country's warning delay for linked disasters.

A country can contribute once per stage or through a capped repeatable action. The global contribution needs diminishing returns.

## Crater-control actions

### Secure the crater perimeter

**Who sees it:** Current controller of a crater state.

**Requirements:** Supplied divisions in or adjacent to the crater, control of nearby access states, and no unresolved local occupation failure.

**Costs:** Support equipment, manpower, fuel, and command power within the project limit.

**Effect:** Reduces local attrition and sabotage pressure, improves defense weight, and enables the survey action. It does not increase the armour bonus.

### Survey extraordinary material

**Who sees it:** A controller that has secured the site and has research capacity.

**Costs:** Civilian factories, research opportunity cost or project capacity, support equipment, and time.

**Effect:** Reveals the site's flavor profile, improves the modifier tooltip, and grants a bounded research or intelligence benefit related to material science. It does not create another armour stack.

### Fortify the access routes

**Who sees it:** A controller of a site with valid neighboring states.

**Costs:** Construction capacity, support equipment, trains, and manpower.

**Effect:** Builds or repairs defenses and supply in neighboring normal states. The crater itself remains unusable. The action should prepare the site for war without creating buildings inside the main crater.

## Rival crater actions

Countries that border an enemy crater or are already at war with its controller can receive a small targeted family.

- Reconnoiter the site
- Disrupt extraction routes
- Prepare an offensive objective

These actions should gather intelligence, affect local supply, or guide AI strategy. They should not grant universal free war goals or direct ownership transfers.

## Costs and requirement rules

- No action may have more than four spendable cost types.
- Costs must use matching texticons.
- Military and logistical actions should rely on equipment, trains, trucks, fuel, manpower, divisions, and construction capacity more often than political power.
- Command power costs must remain conservative and never exceed the project limit.
- A state-control, route, division, supply, or threshold condition is a requirement, not a hidden fifth cost.
- Dynamic costs should scale with affected population, state count, distance, national industry, or current dust stage where that changes the real effort.
- The UI should show the exact target state and blocked reason.

## AI behavior

The AI needs an equivalent path for every useful action.

Priority order should normally be:

1. Prevent continuing deaths.
2. Restore supply to the capital and active fronts.
3. Reconnect high-population damaged states.
4. Protect national production from dust.
5. Restore outer-ring industry.
6. Secure and defend extraordinary mineral sites.
7. Contribute to global mitigation when national needs and resources allow it.

AI should refuse actions that would consume its last trains, support equipment, fuel, or construction capacity during an active existential war.

## Category cleanup

- Emergency actions hide when no severe local burden remains.
- Reconstruction actions hide when their target state is restored, lost, annexed, or invalid.
- Dust actions hide at zero Dust Load.
- Crater-controller actions refresh when control changes.
- Selected-state targets clear when the state changes controller or becomes invalid.
- Missions cancel or transfer cleanly when the country ceases to control the required route.
- The category closes entirely for countries with no local impact, no global dust, and no crater interest.

## Exploit controls

- A repaired building cannot be restored above its pre-impact or current allowed level through Event 028 actions.
- Main crater buildings cannot be rebuilt.
- A country cannot repeat a one-time emergency action on the same state.
- Repeated global mitigation has a country cap and diminishing global effect.
- Crater security actions cannot be farmed through rapid controller switching.
- Mission success records should be one-time for each incident and state group.
- Annexing a damaged state does not reset its recovery burden or reopen completed rewards.
