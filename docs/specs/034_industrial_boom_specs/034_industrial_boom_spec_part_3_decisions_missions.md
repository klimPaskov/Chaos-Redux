# Industrial Boom specification, part 3: Decisions and missions

## Decision category role

Industrial Boom uses one temporary decision category for the affected country. The category is a management surface, not an economic shop. It should show the current state of the boom and present only the actions that matter in the current phase.

The category remains visible from the opening until Event 34 cleanup. It changes its picture state, header, available actions, and active objective as the boom moves through Ignition, Expansion, Strain, and Landing.

## Presentation hierarchy

The planned presentation uses:

1. One category icon.
2. One static category picture with phase variants when useful.
3. One Overheating progress display or equivalent compact meter.
4. One trend indicator.
5. One next-threshold line.
6. One reserve status line.
7. Up to three short cause indicators.
8. Three to five primary actions in normal phases.
9. One to two active missions.

A separate scripted GUI is unnecessary at planning stage. One public numeric value, one qualitative reserve state, and a small action set fit the normal decision interface. The implementation agent may propose a compact event-owned window only after inspecting the live category and proving that state selection or meter presentation cannot be made clear in the normal surface.

## Action visibility budget

The category follows a strict visibility budget.

| Phase | Normal visible primary actions | Active missions | State-targeted rows |
| --- | ---: | ---: | ---: |
| Ignition | 3 to 4 | 0 to 1 | Hidden until region work begins |
| Expansion | 4 to 5 | 1 | Only the selected region or a compact selector |
| Strain | 3 to 5 | 1 to 2 | Current vulnerable regions only |
| Pre-crash | 2 to 4 | 1 emergency mission | No ordinary expansion rows |
| Landing | 2 to 3 | 1 landing mission | Only project completion or cancellation rows |

Six primary actions is the hard maximum in any phase. Obsolete actions must disappear or be replaced by stronger versions.

## Cost scaling model

Every cost scales to the country's economy and current pressure. A small player-controlled country must be able to manage the event. A major must commit enough resources to feel the sacrifice.

Useful scaling inputs include:

- Total civilian and military factories.
- Number of active Industrial Regions.
- Current evolution level.
- Current Overheating band.
- Number of previous Event 34 firings.
- War state.
- Convoy dependence.
- Fuel and logistics condition.
- Project count.

Each action has no more than four spendable cost types. Non-consumed requirements such as controlling a region do not count as costs.

Costs should normally use:

- Temporary civilian factory commitment.
- Trains.
- Trucks.
- Convoys.
- Fuel.
- Support equipment.
- Infantry equipment when it represents guards, work crews, or emergency stores.
- Stability or war support when policy resistance is central.
- Temporary factory output or construction sacrifice.

Political power should be rare. It may support a coercive price-control, credit-control, or forced shutdown incident, but it should not become the default payment for managing the economy.

## Core action family

The names below are working labels inherited from the concept. Final localisation should follow the direction in part 9.

### Run the Economy Hot

#### Player meaning

The government, firms, procurement offices, or industrial authorities accept the highest available order volume and defer maintenance, reserve building, and caution. The decision creates a clear short-term production window.

#### Availability

- Available during Ignition and Expansion.
- Available during early Visible Strain only when Overheating is below the emergency lock.
- Blocked in Pre-crash and Terminal Instability.
- Blocked while a previous hot-running period is active.
- Blocked during controlled landing.

#### Costs and commitments

- Immediate Overheating increase.
- Additional Overheating drift during the active period.
- Temporary increase in maintenance pressure.
- Optional stability or war support cost under Evolution I when restraint has become politically difficult.

It should not consume an arbitrary equipment stockpile merely to create cost variety. Its real price is the increased risk and deferred maintenance.

#### Benefits

- Strong temporary factory output.
- Strong production-efficiency growth.
- Construction acceleration where the current phase supports it.
- Faster project progress at low pressure.
- Reduced project quality and higher accident risk at high pressure.

#### Tradeoff

The action is efficient while the economy has slack and becomes inefficient near danger. This makes early exploitation rational and late repeated use reckless.

#### AI behavior

AI may use it when:

- Overheating is low.
- Supply and fuel are sound.
- A major war creates an equipment need.
- The country has reserve protection.
- The expected production window matters before a front or operation.

AI avoids it when:

- Overheating is high.
- A controlled landing is nearly ready.
- The country is blockaded.
- A key Industrial Region is damaged or lost.
- Event 35 inheritance would be especially severe.

### Stabilize Supply Chains

#### Player meaning

The country commits transport, fuel, civilian capacity, and priority authority to move materials and repair critical links. The action addresses the largest baseline source of avoidable Overheating.

#### Availability

- Available in every active phase before collapse.
- Replaced by an emergency variant in Pre-crash.
- Requires at least one valid logistics or material pressure source.
- A low-pressure country can still use it as preparation, but receives less immediate relief.

#### Dynamic costs

The action draws from up to four of these according to country profile:

- Trains.
- Trucks.
- Fuel.
- Convoys for maritime or import-dependent economies.
- Temporary civilian factory commitment.

A landlocked self-sufficient country should not pay a large convoy cost. A maritime empire should not stabilize an import crisis with trains alone.

#### Benefits

- Immediate Overheating relief scaled by actual pressure.
- Temporary reduction in supply and material drift.
- Faster recovery of damaged region logistics.
- Better success chance for supply objectives.
- Reduced severity from the next trade or transport shock.

#### Failure and partial success

The action can give partial relief when the country lacks enough fuel, loses a target region, or remains under blockade. It should never debit full costs and silently do nothing. The player sees why the result was reduced.

#### AI behavior

AI prioritizes this action when supply pressure is among the strongest causes, when Overheating is rising, or when an Industrial Region has transport damage.

### Build Industrial Reserves

#### Player meaning

The country deliberately leaves some machine time, spare parts, transport, material stock, and repair capacity unused. The immediate economy slows so the next shock or landing does less damage.

#### Availability

- Available during Ignition, Expansion, and early Strain.
- Hidden when reserve status is Strong.
- Replaced by a rebuilding action when reserves are Depleted.
- Blocked during the final landing transition.

#### Costs

- Temporary reduction in factory output.
- Temporary reduction in construction speed.
- Civilian factory commitment.
- Optional support equipment, trains, or fuel according to the reserve profile.

#### Benefits

- Improves reserve status by one bounded step.
- Lowers a small amount of Overheating because immediate utilization falls.
- Absorbs part of a later shock.
- Improves controlled-landing quality.
- Reduces inherited Depression Severity after a crash when some reserves remain.

#### Tradeoff

Reserve building is strongest when begun early. Rebuilding depleted reserves near collapse is expensive and slow. A player who waits until the last threshold cannot buy complete safety instantly.

#### AI behavior

AI builds reserves when Overheating is below the danger band and one of these is true:

- The country expects a long war.
- Industrial Regions are exposed to bombing.
- Trade is fragile.
- Evolution II or III is active.
- A landing objective requires reserve strength.

### Cool the Expansion

#### Player meaning

The country restrains credit, delays contracts, cancels marginal construction, reduces shift intensity, and returns part of the economy to sustainable operation.

#### Availability

- Available in Expansion and Strain.
- Always available in Pre-crash through an emergency variant.
- Hidden in early Ignition unless Overheating started unusually high.
- Cannot overlap with Run the Economy Hot.

#### Costs

- Strong temporary loss of boom output.
- Strong temporary reduction in construction speed.
- Slower project progress.
- Under Evolution I, possible stability or war support pressure because firms and workers resist restraint.

#### Benefits

- Large immediate Overheating reduction.
- Lower drift during the cooling period.
- Faster maintenance recovery.
- Better landing forecast.
- Reduced serious-incident chance.

#### Tradeoff

Cooling is the safest large relief action and has the highest opportunity cost. The output lost during the cooling window should matter in war. The action must not allow a player to keep the full boom modifier while resetting the meter.

#### AI behavior

AI chooses cooling when Overheating is dangerous, a landing is close, the country can tolerate reduced output, or an external shock has made further expansion inefficient.

### Protect Key Industrial Regions

#### Player meaning

The country invests in redundancy, repair stores, transport alternatives, fire control, dispersal, civil defense, and priority material access in one important state.

#### Availability

- The action opens a compact target selector.
- Valid targets are current Industrial Regions or active project states.
- Each state can receive the protection package once per boom.
- The country has a capped number of protected regions based on economy and evolution.

#### Costs

- Civilian factory commitment.
- Trains or trucks.
- Support equipment or infantry equipment for repair and guard functions.
- Fuel when the protection plan depends on transport redundancy.

#### Benefits

- Reduces the state's contribution to shocks.
- Protects project progress from bombing, disaster, and infrastructure loss.
- Speeds local repair.
- Improves landing conversion when the state remains controlled.
- Reduces Event 35 local shutdown severity after a crash.

#### Tradeoff

Protection is state-specific. It does not reduce every national pressure. Choosing one region leaves another exposed.

#### AI behavior

AI targets the most valuable vulnerable region, considering industry share, project progress, infrastructure, bombing risk, port dependence, and loss risk.

## Structural development actions

These actions appear during Expansion and are hidden when no valid state exists.

### Survey Lasting Capacity

This early action evaluates the current Industrial Regions and identifies where temporary growth can become lasting capacity. It should normally be completed once per boom.

Effects:

- Reveals or confirms valid long-term project states.
- Establishes the maximum number of active regional projects.
- Improves landing forecast accuracy.
- Does not grant a permanent reward by itself.

The survey uses civilian capacity and time. Avoid a large political power cost.

### Designate an Industrial Project

The player selects one valid Industrial Region and one available project profile. The number of simultaneous projects remains small.

Baseline project profiles:

- Production Practices.
- Rail and Supply Integration.
- Factory Conversion Capacity.
- Industrial Repair Network.
- Resource Efficiency when the state and economy support it.

Evolution II and III add stronger project profiles described in part 5.

Project designation does not immediately grant factories or slots. It creates a timed and state-sensitive development path.

### Suspend a Fragile Project

The player pauses a project to stop its pressure and protect part of its progress.

- Available when Overheating is high or the target state is threatened.
- Reduces project-related drift.
- Slows or stops permanent conversion.
- May preserve the right to resume after the crisis improves.
- Repeated suspension can reduce final project quality.

### Abandon a Project

The country cancels a project that can no longer be supported.

- Reduces Overheating immediately.
- Removes continuing project pressure.
- Loses most unfinished progress.
- May create a temporary local disappointment or unfinished-works modifier.
- Prevents a dangerous project from worsening Event 35 inheritance.

A player should not be forced to maintain an invalid project after state loss or blockade.

## Phase-specific emergency actions

### Emergency Logistics Command

Appears in Pre-crash when supply or material pressure is dominant.

- Uses a larger one-time commitment of trains, trucks, fuel, convoys, and civilian capacity.
- Gives immediate relief and a short protected period.
- Cannot be repeated until the protected period ends.
- Consumes reserve status when the country lacks enough physical resources.

### Liquidate Speculative Projects

Appears under Evolution I when speculative pressure is active.

- Cancels high-risk projects.
- Reduces Overheating sharply.
- Damages temporary output and stability.
- May create a local unfinished-project modifier.
- Improves Event 35 severity if collapse still occurs because less speculative exposure remains.

### Order an Emergency Production Halt

Appears at Terminal Instability.

- Ends aggressive output modifiers immediately.
- Cancels Run the Economy Hot.
- Freezes ordinary project growth.
- Attempts a forced landing.
- Carries a major temporary production and construction penalty.
- Can prevent Event 35 only when enough reserve, protection, and structural control remain.

This is a last-resort action, not a guaranteed escape.

## Mission and objective family

Missions represent sustained work. They should auto-complete when the required conditions are met.

### Secure the Material Flow

#### Role

A medium-duration objective that proves the economy can feed its current industrial pace.

#### Typical requirements

- Maintain a viable train and truck reserve.
- Maintain acceptable fuel access.
- Keep required ports or rail connections controlled.
- Avoid a severe material deficit.
- Keep Overheating below a defined danger threshold for the final part of the mission.

The exact objective should adapt to the country. A landlocked country receives rail and resource requirements. A maritime country receives port, convoy, and import requirements.

#### Duration

Normally 120 to 180 days, adjusted by economy, evolution, and current disruption.

#### Success

- Reduces supply and material drift.
- Improves project progress.
- Improves landing quality.
- May convert a temporary supply measure into a long-duration logistics benefit.

#### Failure

- Raises Overheating.
- Marks the strongest weak link.
- Can trigger a serious transport or material incident.
- Does not duplicate a failure penalty already caused by losing the required state.

### Consolidate Industrial Capacity

#### Role

An Expansion-phase objective that converts emergency growth into reliable practices.

#### Typical requirements

- Complete a minimum amount of regional project progress.
- Keep key project states controlled.
- Avoid Pre-crash for a sustained period.
- Maintain at least Limited reserves.
- Do not run the economy hot during the final consolidation window.

#### Duration

Normally 150 to 240 days. Evolution II and III increase difficulty or require more regional proof.

#### Success

- Opens Controlled Landing.
- Improves permanent legacy quality.
- Reduces maintenance drift.

#### Failure

- Does not automatically crash the economy.
- Removes some project progress.
- Raises maintenance pressure.
- Allows a later retry with higher cost or a shorter emergency route.

### Prepare a Controlled Landing

#### Role

The main resolution objective.

#### Availability

- Requires structural development or a minimum active duration.
- Requires Overheating below Pre-crash.
- Requires valid control of at least one Industrial Region.
- Becomes easier after Consolidate Industrial Capacity.

#### Public requirements

The category should show a concise checklist:

- Keep Overheating below the stated band.
- Maintain or rebuild reserves.
- Keep selected Industrial Regions controlled.
- Avoid Run the Economy Hot during the final transition.
- Complete or safely close active projects.

#### Duration

Normally 90 to 180 days. A well-prepared baseline economy can land faster. Evolution III needs a longer confirmation period unless special stabilization projects are complete.

#### Success

- Ends the extraordinary phase.
- Applies the landing result.
- Converts eligible projects.
- Applies temporary transition modifiers.
- Begins Event 34 cleanup.

#### Failure

Failure depends on cause:

- Threshold breach returns the economy to Strain or Pre-crash.
- State loss pauses or cancels the relevant part.
- A major shock can force an emergency landing check.
- Deliberate Run the Economy Hot cancels the mission and records the choice.

The player should not lose the entire boom merely because one objective tick occurred during a temporary state mismatch.

### Prevent the Crash

#### Role

A short emergency mission at Pre-crash or Terminal Instability.

#### Requirements

- Lower Overheating below the emergency threshold.
- End aggressive output actions.
- Resolve or suspend critical projects.
- Restore at least one viable supply route.

#### Duration

Normally 60 to 90 days, with a shorter duration when the economy is already at 95 or above.

#### Success

- Returns the event to Strain.
- Applies a temporary no-push recovery period.
- Preserves remaining projects.

#### Failure

- Performs the Event 35 handoff.
- Uses the final state of the mission to calculate severity.

## Incident response decisions

Incidents should not add a permanent wall of buttons. Each incident exposes at most two or three responses and closes when resolved.

Response families can use:

- Repair and compensate.
- Reroute production.
- Accept the shutdown.
- Force continued operation.
- Cancel a project.
- Use reserves.

Each response should change Overheating, state condition, project progress, output, or stability in a way that matches the incident.

## AI equivalent

AI countries use the same decisions and missions through weighted choices. No action should depend on a human-only click path. The AI can receive hidden evaluation helpers, but its costs and results must match the player action.

AI should:

- Understand its current threshold.
- Preserve a safety margin when not under urgent wartime pressure.
- Use reserves before severe shocks when possible.
- Protect valuable vulnerable states.
- Stop starting projects when Overheating is dangerous.
- Begin landing when the expected permanent return is high enough.
- Accept a rough landing when war needs outweigh long-term value.
- Avoid repeated emergency actions that cannot succeed.

## Cleanup rules

When the event ends:

- Hide and remove all Event 34 decisions and missions.
- Release temporary civilian factory commitments.
- End temporary action modifiers.
- Clear selected-state markers and invalid project targets.
- Consume or convert reserve status according to outcome.
- Preserve only documented country and state memory.
- Pass the frozen collapse snapshot to Event 35 before clearing the active boom state.
- Restore repeatable eligibility only after the result cooldown.

No decision may remain visible because a state target or mission flag survived cleanup.
