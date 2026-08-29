# Industrial Boom specification, part 4: Regions, legacy, and repeatability

## Industrial Regions

Industrial Regions are a small set of states that concentrate the boom's physical development. They give state loss, bombing, infrastructure, and permanent conversion a concrete map presence without asking the player to track every industrial state.

A country should normally manage:

- One region when it is a small player-controlled country.
- Two regions when it has a medium industrial base.
- Three regions when it is a large major or has Evolution II or III capacity.

Three active primary regions is the normal hard cap. Evolution III can create temporary secondary spread states, but these remain connected to a primary region and do not become additional full public region slots.

## Region eligibility

A valid Industrial Region should:

- Be controlled by the target country.
- Normally be a core state.
- Have population and industrial capacity.
- Have a viable connection to the country's economy.
- Be neither impassable nor a purely remote holding.
- Be free of an incompatible state-level economic crisis that would make project progress meaningless.

The selection should prefer industrial concentration, infrastructure, rail access, resources, ports, and adjacency to other productive states. It should also consider risk. The strongest state is not always the best project state when it is exposed to enemy bombing or imminent loss.

## Region roles

Each region can hold one primary project role during a boom. The role creates state-specific development pressure and a possible legacy reward.

### Production Practices

Represents standardized components, better scheduling, tool reuse, worker training, and production-line organization.

Temporary contribution:

- Faster production-efficiency growth.
- Lower maintenance pressure.
- Better use of Run the Economy Hot at low Overheating.

Legacy direction:

- Long-duration or permanent production practice improvement.
- Small production-efficiency cap or growth improvement.
- Faster conversion between production lines.

The legacy should not grant a free factory level by default.

### Rail and Supply Integration

Represents rail links, sidings, depots, port handling, road access, and coordinated transport scheduling.

Temporary contribution:

- Lower supply and material pressure.
- Better protection against trade and transport shocks.
- Faster region project progress.

Legacy direction:

- Infrastructure or railway improvement.
- Repair speed.
- Supply and logistics benefit.
- A bounded long-duration transport modifier when physical map improvement is not appropriate.

### Factory Conversion Capacity

Represents adaptable layouts, machine-tool pools, common components, and facilities that can change production more quickly.

Temporary contribution:

- Construction and conversion benefit.
- Faster setup of new lines.
- Better rough-landing outcome.

Legacy direction:

- Conversion speed.
- Repair or construction efficiency.
- A limited factory or slot reward when the state has completed real project stages and remains within the legacy budget.

### Industrial Repair Network

Represents spare parts, mobile repair teams, fire control, machine-tool reserve, and redundant utilities.

Temporary contribution:

- Lower accident impact.
- Faster recovery from bombing and disasters.
- Stronger regional protection.

Legacy direction:

- Repair speed.
- Reduced local disruption from compatible future events.
- Infrastructure or anti-air support when the state and project justify it.

### Resource Efficiency

Represents recycling, substitution, scrap recovery, reduced waste, and better use of local materials.

Temporary contribution:

- Lower material pressure.
- Reduced import dependence.
- Better supply-chain action efficiency.

Legacy direction:

- Resource extraction or resource-use efficiency.
- Synthetic or recycling support under Evolution II.
- A bounded resource increase only when the state has an appropriate economic basis.

The project must not invent arbitrary oil, rubber, tungsten, or chromium in every country.

## Project stages

Each state project moves through four ordinary stages.

### Stage 1: Designated

The state is chosen and the project profile is locked.

- The project begins to add a small amount of Overheating.
- The player sees its purpose and target conditions.
- No permanent reward exists yet.
- The project may be cancelled with a limited loss.

### Stage 2: Expansion work

Factories, railways, depots, utilities, or production systems are actively being expanded.

- Progress benefits from low Overheating and stable supply.
- Run the Economy Hot may accelerate progress while reducing final quality.
- State damage or control loss pauses progress.
- Cancellation leaves unfinished works and loses most progress.

### Stage 3: Integration

The project is being connected to ordinary national production and logistics.

- Progress requires a sustained period below a pressure threshold.
- Reserve status and region protection improve success.
- High Overheating creates fragility and can reverse progress.
- The project can still be suspended to preserve part of its work.

### Stage 4: Secured legacy

The project has earned a potential post-boom reward.

- The reward is not applied until the landing resolves.
- A later state loss or critical incident can still damage the result.
- A crash passes the secured state into Event 35, which may preserve, idle, or damage it according to inherited severity.

A project at Stage 4 should feel valuable enough that the player may cool the economy to protect it.

## Project progress factors

Progress rises with:

- Low or falling Overheating.
- Stable control.
- High infrastructure.
- Rail and port access.
- Adequate fuel and logistics.
- Region protection.
- Reserve status.
- Compatible project synergies.
- A limited early use of Run the Economy Hot.

Progress slows or reverses with:

- Dangerous Overheating.
- State damage.
- Blockade or trade loss.
- Fuel collapse.
- Control loss.
- Repeated accidents.
- Too many simultaneous projects for the country's economy.
- Evolution III spread that outruns infrastructure.

The game should explain the strongest current cause through a short project status. It should not expose a separate project-pressure formula.

## Project synergies

Projects can support one another without creating mandatory combinations.

Examples:

- Rail and Supply Integration improves every project in that region and lowers material pressure.
- Industrial Repair Network protects Production Practices from accident setbacks.
- Resource Efficiency reduces the supply burden of Factory Conversion Capacity.
- Production Practices improves the quality of a later permanent factory or slot conversion.

A country with only one region should still have a complete path. Synergies reward larger economies without making small players unable to land successfully.

## Protection and fragility

### Protected region state

Protection has three levels of state behavior:

- Prepared: local disruption is reduced and project loss is less likely.
- Tested: protection has absorbed a major incident and is temporarily weakened.
- Compromised: repeated shocks or state damage have exhausted the protection package.

These are qualitative state statuses, not another numeric meter.

Protection can be restored through repair work when the state remains controlled. It cannot survive annexation as though the original country still owns the network.

### Fragile region state

Evolution II and III can create Fragile Industrial Regions. Fragility means the state contains exceptional capacity tied to narrow supply chains, overextended utilities, speculative financing, and exhausted labor.

Fragility rises with:

- High Overheating.
- Rapid project acceleration.
- Repeated use of Run the Economy Hot.
- Unprotected project concentration.
- Industrial spread into weak infrastructure.

Fragility falls with:

- Low Overheating.
- Completed integration.
- Protection.
- Reserve support.
- Controlled landing preparation.

Fragility remains hidden as a precise value. The player sees a state status and the consequence risk.

## State control changes

### Temporary control loss

When an Industrial Region is occupied:

- Project progress pauses.
- The state loses active protection benefits for the original country.
- National Overheating receives a shock based on the state's industrial share and project stage.
- The project enters a threatened state.
- The player receives a bounded recovery period.

If the state is retaken within the recovery period:

- Part of project progress returns.
- Protection may remain weakened.
- The state can rejoin the landing calculation.

### Permanent loss or annexation

When the target country no longer has a viable claim to recover the state:

- The project is cancelled for the original country.
- No permanent reward is granted.
- The state receives an unfinished or disrupted local consequence when appropriate.
- The original country receives an Overheating shock and landing-quality loss.
- The new controller does not inherit the Event 34 project automatically.

A future shared state-project transfer contract could permit negotiated transfer, but Event 34 does not assume one.

### Release and civil war

When the target country releases territory or enters a civil war:

- Project ownership follows the country that retains the Event 34 active ledger only when it controls the state.
- A new country does not receive a duplicate boom unless a specific split event defines it.
- The landing requirement recalculates from valid remaining regions.
- The player is never trapped by a mission that still requires an invalid state.

## Controlled landing

Controlled landing is the best ordinary resolution. It converts a bounded share of temporary development into lasting capacity while removing the extreme modifier.

### Readiness

Landing readiness should consider:

- Overheating below the dangerous range.
- Falling or stable trend.
- At least Limited reserve status.
- One or more projects at Integration or Secured Legacy.
- Valid control of the relevant regions.
- No active Run the Economy Hot period.
- No unresolved critical incident.
- A minimum period of active boom experience.

A player can attempt an earlier landing with weak readiness, but the forecast should show that the permanent result will be limited.

### Transition sequence

The transition occurs in stages:

1. Aggressive temporary actions end.
2. The highest temporary bonuses reduce.
3. The landing mission checks sustained control and pressure.
4. Projects receive a final quality assessment.
5. Temporary effects are removed.
6. Lasting and long-duration legacy is applied within the country and state caps.
7. A transition modifier represents reconversion and cautious normalization.
8. Event 34 active state cleans up.

The landing should not remove the entire bonus in one unexplained instant when the mission has succeeded. A short visible transition helps the player adjust production and construction.

## Landing result bands

### Exceptional landing

Requirements:

- Low Overheating.
- Falling trend.
- Strong reserves.
- Several secured projects.
- No lost primary region.
- No unresolved serious incident.
- Sustained final transition discipline.

Rewards:

- Highest permitted project conversion.
- Strong long-duration production practice benefit.
- Preserved infrastructure and supply gains.
- Reduced repeat-firing starting pressure through institutional experience.

The result still respects the cumulative legacy budget.

### Controlled landing

Requirements:

- Overheating below danger.
- Limited or Strong reserves.
- At least one completed or integrated project.
- Valid region control.

Rewards:

- Normal project conversion.
- Moderate long-duration national benefit.
- Clean end to the crisis.

### Rough landing

Conditions:

- Overheating remains high.
- Reserves are weak or depleted.
- Projects are unfinished.
- The player ends the boom before terminal collapse.

Results:

- Small permanent or long-duration legacy.
- Temporary industrial exhaustion.
- Partial project cancellation.
- A post-boom vulnerability period during which a major external shock can still activate Event 35.

### Forced landing

Conditions:

- Emergency halt near collapse.
- Severe active pressure.
- Some reserve or project structure still survives.

Results:

- Major temporary economic penalty.
- Most temporary growth lost.
- Strong chance of project damage.
- Event 35 avoided only when the emergency calculation succeeds.
- If it fails, the frozen forced-landing state becomes part of Event 35 severity.

## Permanent legacy model

### Country legacy budget

Every country has a cumulative Event 34 legacy budget. It scales from the economy the country had before its first boom and can grow modestly when the country expands normally. It should not rise one-for-one with Event 34 rewards.

The budget controls:

- Number of permanent factory levels attributable to Event 34.
- Number of permanent building slots attributable to Event 34.
- Strength of permanent national industrial practice modifiers.
- Number of states that can retain the strongest project form.

Once the raw capacity budget is mostly used, later landings favor:

- Timed output benefits.
- Conversion speed.
- Repair speed.
- Infrastructure.
- Railway integration.
- Resource efficiency.
- Safer future boom management.

This keeps repeat firings valuable without allowing exponential factory growth.

### State legacy cap

A state can receive one strong Event 34 legacy package and a limited number of supporting upgrades across the campaign.

A state that already holds a strong legacy can:

- Upgrade its quality when the previous form was weak.
- Receive a different supporting project.
- Reactivate temporary efficiency during a later boom.
- Become more resistant to disruption.

It should not receive another free factory or slot every time Event 34 fires.

### Legacy reward profiles

A secured project may convert into one of these profiles:

| Profile | Physical reward direction | National reward direction | Main cap |
| --- | --- | --- | --- |
| Production Practices | Limited factory or no physical change | Efficiency growth, conversion, output quality | Country practice cap |
| Rail and Supply Integration | Infrastructure, railway, supply support | Logistics and repair | State transport cap |
| Factory Conversion Capacity | Limited factory or slot when justified | Conversion and construction | Country raw-capacity budget |
| Industrial Repair Network | Repair, infrastructure, local protection | Repair speed and resilience | State support cap |
| Resource Efficiency | Appropriate extraction or no physical change | Resource use, recycling, synthetic support | Resource plausibility and country cap |

The implementation should prefer map changes when they represent completed physical work. It should prefer modifiers when a physical building would create a balance or plausibility problem.

## Temporary legacy

Not every successful landing needs a permanent reward. Timed legacy is valuable when it lasts long enough to shape a campaign.

Possible timed forms:

- Experienced production boards.
- Retained conversion crews.
- Improved industrial scheduling.
- Reserve machine-tool pool.
- Reconstruction and normalization capacity.

Timed benefits can last one to several years according to landing quality. They should be stronger than tiny decorative modifiers.

## Exhaustion and scars

Poor outcomes can leave state and country scars.

### Country exhaustion

Represents deferred maintenance, cancelled orders, labor fatigue, and financial cleanup.

- Reduces part of industrial performance temporarily.
- Makes an immediate repeat firing more dangerous.
- Can be shortened through ordinary repair and stable supply.
- Is replaced by Event 35 effects when collapse occurs.

### State exhaustion

Represents unfinished works, worn machinery, overloaded utilities, or a failed project.

- Reduces future Event 34 project quality in the state.
- Can be repaired during a later boom or through compatible construction.
- Prevents the state from serving as an effortless repeated raw-capacity reward target.

### Crash scars

A state involved in an Event 34 crash passes its project stage, protection state, fragility, and exhaustion to Event 35. Event 35 decides whether the state becomes idle, damaged, rescued, or abandoned.

## Repeat firing behavior

### Successful prior boom

A country with a previous controlled landing receives:

- Better landing forecast accuracy.
- Faster survey and consolidation.
- Lower maintenance pressure in experienced regions.
- Smaller raw-capacity reward potential.
- Higher costs for new untouched expansion.

### Prior rough or forced landing

The country receives:

- Higher starting Overheating.
- Existing exhaustion.
- Stronger political support for early reserves.
- Weaker project conversion until scars are repaired.

### Prior crash

The country receives:

- A meaningful selection-weight penalty for a long recovery period.
- Higher speculative and maintenance pressure.
- Stronger resistance to Run the Economy Hot.
- A larger Event 35 inheritance multiplier if it crashes again.
- Access to experienced emergency responses that can improve survival.

A previous failure creates memory without permanently banning the event.

## Anti-farming rules

The design rejects the following loops:

- Repeatedly designating and cancelling a project to gain relief or construction.
- Repeatedly protecting the same state to stack local modifiers.
- Repeatedly landing early to collect a small permanent reward.
- Allowing a puppet release or annexation to reset state legacy caps.
- Allowing tag switching to erase country boom history.
- Allowing occupation and reconquest to duplicate project rewards.
- Allowing Event 35 activation to preserve the full Event 34 positive modifier.
- Allowing several simultaneous booms in one country.

Controls include one-time project receipts, country and state persistent memory, cooldowns, bounded reserve states, frozen result snapshots, and reward conversion only at final landing.

## Regional acceptance tests

The region and legacy design passes when:

- A small player country can complete one meaningful project.
- A major cannot manage more than a readable number of primary regions.
- State loss matters in proportion to project importance.
- Retaking a state can recover some progress without duplicating rewards.
- A controlled landing gives a lasting result that reflects completed work.
- Repeat firings remain valuable after raw-capacity caps are reached.
- No state can produce unlimited factories or slots through repeated booms.
- Event 35 receives enough state memory to continue the crisis coherently.
