# Industrial Boom specification, part 10: Achievements and acceptance

## Achievement design role

Industrial Boom rewards management across a long event lifecycle. Achievements should test difficult combinations of output, restraint, region protection, evolution control, and failure recovery. An achievement that unlocks because Event 34 fired or because the player completed any landing would add little.

The labels below are working labels. Final titles and descriptions should be written during implementation from the stated direction.

## Achievement 1: Managed Expansion

### Working key

`chaos_redux_034_managed_expansion`

### Title direction

A concise phrase about using a boom aggressively while still bringing it under control.

### Description direction

Tell the player to exploit the boom more than once, complete a controlled landing at low Overheating, and preserve real regional development.

### Eligibility

- Any player-controlled country.
- Event 34 must have fired normally or through an approved test-independent gameplay route.

### Unlock conditions

- Use Run the Economy Hot at least twice during one Event 34 firing.
- Reach at least Visible Strain.
- Complete a controlled or exceptional landing.
- Finish with Overheating at or below 25.
- Convert at least two project legacies, or the maximum possible for a small country when its project cap is one.
- Avoid Event 35 activation from that firing.

### Disqualifiers

- Force-trigger or debug proof when achievements normally exclude debug modes.
- Emergency halt used during the final landing.
- A project reward duplicated through state transfer or reload abuse.

### Difficulty

Hard.

### Visibility

Visible.

### Why it is not trivial

The player must accept real pressure, then reverse it while protecting project progress and landing quality.

### Icon direction

An overdriven industrial flywheel brought back under a marked limit, with a factory or rail network behind it.

### Tracking notes

Track hot-running completions, highest threshold reached, final landing type, final Overheating, and converted project count for one firing receipt.

## Achievement 2: The Miracle Holds

### Working key

`chaos_redux_034_miracle_holds`

### Title direction

A compact phrase about preserving impossible development through disciplined integration.

### Description direction

Tell the player to stabilize an Evolution II or III boom with the full primary region cap, preserve every primary region, and retain major legacy.

### Eligibility

- Any player-controlled country.
- Evolution II or III enabled and active.

### Unlock conditions

- Designate the maximum primary Miracle Regions available to the country, up to the normal cap of three.
- Complete at least one secured project in every primary region.
- Lose no primary region before landing.
- Finish with at least Limited reserves.
- Complete a controlled or exceptional landing.
- Retain at least one physical map improvement and one national production-practice legacy.

### Disqualifiers

- Any primary region permanently lost during the firing.
- Unrestricted Evolution III spread active at landing.
- Event 35 activation.

### Difficulty

Very hard.

### Visibility

Visible after Evolution II has been encountered once, or visible from the start when the project achievement pattern prefers full disclosure.

### Why it is not trivial

The player must manage several valuable and fragile states without allowing their combined pressure to reach collapse.

### Icon direction

A dense factory and railway complex held inside a strong structural frame, with one impossible tower or crane detail.

### Tracking notes

Track available primary cap at designation time, designated regions, secured project stages, region-loss receipts, reserve status, landing result, and legacy types.

## Achievement 3: Redline Nation

### Working key

`chaos_redux_034_redline_nation`

### Title direction

A restrained mechanical phrase about operating near the limit for an extended period.

### Description direction

Tell the player to keep an Industrial Boom in Dangerous Imbalance for a long sustained period, avoid Event 35, and land successfully.

### Eligibility

- Any player-controlled country.

### Unlock conditions

- Accumulate at least 120 days in the 65 to 94 Overheating range during one firing.
- Spend at least 30 of those days at 80 or above.
- Never reach 100.
- Complete a controlled or rough landing without a forced emergency halt.
- Preserve at least one project legacy.

### Disqualifiers

- Prevent the Crash mission fails.
- Emergency production halt used.
- Event 35 activation.

### Difficulty

Very hard.

### Visibility

Visible.

### Why it is not trivial

The player must remain close to collapse long enough to gain military value while still building a path out.

### Icon direction

A pressure or heat gauge near its maximum with a running assembly line and one intact safety boundary.

### Tracking notes

Use cumulative day counters by threshold band and one firing receipt. Do not allow save or threshold flicker to double-count the same day.

## Achievement 4: The Long Fall

### Working key

`chaos_redux_034_the_long_fall`

### Title direction

A sober phrase about surviving the full reversal from impossible expansion into severe depression.

### Description direction

Tell the player to crash an Evolution III boom into Event 35, then recover fully without losing the country.

### Eligibility

- Any player-controlled country.
- Evolutions I, II, and III active at Event 34 collapse.
- Event 35 must implement a full recovery state.

### Unlock conditions

- Event 34 collapses at Evolution III.
- Event 35 begins with very high inherited Depression Severity.
- The player completes Event 35 recovery.
- At least one inherited Miracle Region is rescued and remains active.
- The country still exists and controls its capital at recovery.

### Disqualifiers

- Tag switching to another country during the crisis when the achievement framework can detect it.
- Event 35 bypassed or removed through debug action.
- Country annexed and later released after the crisis.

### Difficulty

Extreme.

### Visibility

Hidden until the player has experienced an Event 34 crash or Event 35 once.

### Why it is not trivial

It rewards recovery from the worst failure route. A simple safe landing does not qualify.

### Icon direction

A towering industrial skyline falling into dark idle factories, with one relit plant or repaired rail line in the foreground.

### Tracking notes

Requires a cross-event receipt linking one Event 34 firing to one Event 35 recovery. Event 35 owns the final unlock check.

## Achievement 5: Built to Last

### Working key

`chaos_redux_034_built_to_last`

### Title direction

A practical phrase about institutional learning across repeated booms.

### Description direction

Tell the player to complete two successful Industrial Boom landings in the same country, preserve distinct legacy, and avoid any boom-caused depression.

### Eligibility

- Any player-controlled country.

### Unlock conditions

- Complete two controlled or exceptional landings in the same country across separate Event 34 firings.
- Convert at least one project in each firing.
- Use at least two distinct project profiles across the two firings.
- Never trigger Event 35 from Event 34 before the second landing.
- Finish the second landing below Visible Strain.

### Disqualifiers

- Country history reset through an invalid tag transfer.
- Same state and same project receipt counted twice.
- A crash into Event 35 between the two successful landings.

### Difficulty

Hard and long-term.

### Visibility

Visible.

### Why it is not trivial

The second boom has higher pressure and lower raw-capacity potential. The player must use institutional memory to solve a distinct second route.

### Icon direction

Two layered industrial eras in one state, with older works integrated into a stronger rail and factory network.

### Tracking notes

Track successful landing receipts, distinct project profiles, crash history, and country continuity.

## Achievement 6: Every Link Held

### Working key

`chaos_redux_034_every_link_held`

### Title direction

A logistics phrase about keeping an industrial network intact under attack.

### Description direction

Tell the player to complete an evolved boom while every primary region suffers a serious external shock and none is lost or abandoned.

### Eligibility

- Any player-controlled country at war.
- Evolution II or III active.
- At least two primary Industrial Regions.

### Unlock conditions

- Every primary region experiences at least one serious qualifying shock from bombing, disaster, transport disruption, or temporary control loss.
- Every primary region is protected before or survives the shock through reserves and repair.
- No primary region is permanently lost.
- No primary project is abandoned.
- Complete a controlled or exceptional landing.

### Disqualifiers

- Self-created trivial shock that does not meet the serious-source threshold.
- Duplicate receipt counted as shocks in several regions.
- Event 35 activation.

### Difficulty

Extreme and situational.

### Visibility

Hidden.

### Why it is not trivial

The achievement requires both external danger and successful state-level preparation. It cannot be farmed through ordinary low-impact incidents.

### Icon direction

A linked railway and factory network with damaged outer sections and an intact central flow.

### Tracking notes

Use source-qualified state shock receipts, unique state IDs, protection state, project abandonment flags, and landing result.

## Achievement coverage balance

The set covers:

- Aggressive success.
- Multi-region evolved success.
- Sustained risk.
- Catastrophic failure recovery.
- Repeat-event mastery.
- External-shock resilience.

It does not require a country-specific route because Event 34 can target any major or player country.

## Edge-case matrix

### Target becomes non-major

The active boom continues. Major status is an entry condition, not a maintenance condition. A player-controlled country remains valid. A country that becomes a special or nonhuman actor should resolve through the owning transformation contract or end Event 34 safely.

### Target becomes a subject

The boom continues when the country still controls a valid economy. Subject trade and factory obligations may change pressure. The overlord does not gain direct control of the decision category.

### Target changes player control

Country-owned event state remains with the country. Multiplayer handoff should not duplicate decisions or reset history.

### Capital moves

Supply and connection calculations update to the new capital or ordinary supply network. Existing region projects remain state-based.

### Capital or all industrial cores are lost

The event enters emergency handling. Invalid projects cancel or pause. If no viable industrial economy remains, the event performs a forced resolution or Event 35 handoff according to the frozen state.

### Civil war

The original Event 34 ledger stays with one country according to the project's existing country identity and event-target rules. The other side does not receive a duplicate boom. Project states recalculate from actual control.

### Annexation

The active event ends safely for a deleted target. No invalid decision or Event 35 country target remains. Persistent state rewards are not transferred as free active projects.

### Government in exile

Event 34 continues only when the country still uses a playable civilian economy and has valid controlled states. Otherwise it resolves safely.

### Peace during wartime exploitation

Military demand falls, which can reduce the strategic value of running hot and may change pressure. The event does not end automatically.

### War begins during landing

The landing mission continues. New military demand can tempt the player to cancel it. The game should show the opportunity cost clearly.

### Blockade ends

Supply and material pressure improve through normal evaluation. No separate reward popup is required unless the change resolves an active emergency objective.

### Region loses core status

The project may continue only through a deliberately defined long-term ownership rule. Default behavior requires core status for permanent legacy conversion.

### Region changes owner during landing

The landing pauses or recalculates. It does not convert a reward in a state the target no longer controls.

### Event 34 selected while no target exists

The event is unavailable and should not fire.

### Event 34 selected while Event 35 is active in every valid country

The event is unavailable unless a later coexistence rule is explicitly implemented.

### Evolution disabled during an active boom

The project-wide evolution settings contract decides whether already active content remains or is removed. Event 34 must not create a half-active stage. The safer design is to preserve an already recorded active evolution for that firing while preventing new stage activation, unless the shared framework defines live removal.

### Evolution threshold crossed during landing

Pacing pauses during the final landing window. The stage can apply to a later firing.

### Save and reload

All active phase, Overheating, trend memory, projects, selected states, reserves, protection, evolution, incidents, landing, and handoff data must persist without duplicating initialization.

## Exploit-control matrix

| Exploit risk | Required control |
| --- | --- |
| Repeated Run the Economy Hot stacking | One active period, cooldown, rising marginal pressure |
| Cooling while keeping full positive modifier | Cooling removes or weakens output during its duration |
| Repeated reserve accumulation | Bounded qualitative states, shock consumption, rebuild cooldown |
| Repeated project designation and cancellation | One receipt per state and profile per firing, cancellation loss |
| Early landing reward farming | Minimum active and structural readiness, reward quality scaling |
| Infinite factories and slots | Country legacy budget and state legacy cap |
| Occupation and reconquest duplication | State receipt persists through control changes |
| Puppet release reset | Country and state history follows stable identity and state receipts |
| Tag-switch reset | Country ledger persists independently of current player |
| Event 35 duplicate category | Deepen existing crisis through one shared package |
| Double event pacing | Direct Event 35 handoff marked as consequence |
| Double Chaos | Event-owned abnormal receipts separated from generic sources |
| Incident repeat farming | Recent-family and state cooldowns |
| AI free safety | AI pays the same costs and uses the same outcomes |
| State selector clutter | Show only current relevant regions and one selected target |
| Invalid cost debit | Validate target and affordability before payment, refund failed transaction |

## Acceptance scenario set

### Scenario 1: Baseline major, controlled landing

Setup:

- Large major at peace.
- Strong infrastructure and supply.
- Baseline evolution state.

Expected play:

- Immediate output increase.
- One early hot-running period.
- Reserves and two projects.
- Controlled landing below danger.

Pass conditions:

- Meaningful temporary output.
- At least one project converts.
- No Event 35.
- Category cleans fully.

### Scenario 2: Player non-major

Setup:

- Small player country with one valid Industrial Region.

Expected play:

- Scaled costs.
- One complete project path.
- Viable controlled landing.

Pass conditions:

- Essential decisions are affordable.
- Reward is smaller but meaningful.
- No major-country quantity assumptions appear.

### Scenario 3: Wartime exploitation

Setup:

- Major war.
- Equipment deficit.
- Good supply.

Expected play:

- Run the economy hot.
- Increased military output.
- Later cooling and rough or controlled landing.

Pass conditions:

- Aggressive route has real military value.
- Risk rises visibly.
- AI and player can choose it rationally.

### Scenario 4: Blockaded maritime country

Setup:

- Import dependence.
- Convoy and port pressure.

Expected play:

- Strong supply-driven Overheating.
- Maritime stabilization costs.
- Early landing or crisis.

Pass conditions:

- Convoys and ports matter.
- Land-only costs do not dominate.
- Restored access improves trend.

### Scenario 5: Region bombing

Setup:

- Two primary regions, one protected.
- Repeated strategic bombing.

Expected play:

- Protected region suffers less project loss and pressure.
- Unprotected region becomes fragile.

Pass conditions:

- Difference is visible and material.
- Bombing damage is not duplicated.

### Scenario 6: Evolution I success

Setup:

- Speculative Mania active.
- One speculative project.

Expected play:

- Stronger output and resistance to cooling.
- Credit restraint or liquidation.
- Landing with selected real development.

Pass conditions:

- Evolution changes decisions and incidents.
- No Chaos for activation.
- Speculative failure changes Event 35 severity if collapse occurs.

### Scenario 7: Evolution II exceptional landing

Setup:

- Several Miracle Regions.
- Low final pressure.
- Strong reserves.

Expected play:

- Physically abnormal project completion.
- One guarded Chaos source.
- Strong but capped permanent legacy.

Pass conditions:

- Project reward requires integration.
- Chaos source has a receipt.
- State and country caps hold.

### Scenario 8: Evolution III collapse

Setup:

- Runaway expansion.
- Fragile spread network.
- Depleted reserves.

Expected play:

- Rapid pressure.
- Failed emergency response.
- Event 35 at Evolution III and very high severity.

Pass conditions:

- Same country receives Event 35.
- State network transfers.
- Event pacing counts once.
- Positive boom modifier is gone.

### Scenario 9: Event 35 already active

Setup:

- Approved overlap path with an active depression.

Expected play:

- Collapse deepens one category.

Pass conditions:

- No duplicate ideas, category, or severity ledger.
- Higher inherited evolution is applied as a minimum.

### Scenario 10: Repeated successful booms

Setup:

- Same country receives Event 34 several times across a long campaign.

Expected play:

- Higher starting pressure.
- Institutional experience.
- Diminishing raw capacity.
- Continued value through logistics and practices.

Pass conditions:

- No unlimited factory or slot growth.
- Later firings remain useful.
- State receipts persist.

### Scenario 11: Country deletion during handoff

Setup:

- Target is annexed during terminal instability.

Expected play:

- Safe cleanup.

Pass conditions:

- No ghost Event 35.
- No invalid state or country targets.
- History remains coherent.

### Scenario 12: Save and reload at every phase

Checkpoints:

- Opening.
- Expansion with projects.
- Active evolution.
- Pre-crash.
- Landing mission.
- Event 35 handoff.

Pass conditions:

- No duplicate initialization.
- No lost projects.
- No changed target.
- No repeated Chaos milestone.
- No duplicated decision cost.

## Completion coverage

Implementation is complete only when the following are aligned:

- Event classification and valid target behavior.
- Opening event and actor history.
- Overheating and trend presentation.
- Threshold effects.
- Core decisions and missions.
- State project system.
- Reserves and protection.
- Controlled, rough, forced, and crash outcomes.
- All three evolutions and both entry paths.
- Event 35 inheritance and existing-crisis behavior.
- AI decision, project, landing, and target logic.
- Weighted-surface probability evidence.
- Chaos sources, reversals, receipts, and overlap controls.
- Repeatability and permanent reward caps.
- Final event, decision, idea, state, achievement, and category assets.
- Final localisation and scripted localisation.
- Event History, Event Details, and evolution rows.
- Event documentation.
- Authoritative event catalog workbook and regenerated CSV exports.
- Save persistence and cleanup.
- Specialist audits and final improvement-loop disposition.

## Anti-bloat conclusion

The specification has enough depth to make Industrial Boom replayable and connected. Expansion should stop until implementation or testing exposes a concrete gameplay gap. Any later addition should strengthen the central choice between immediate output, structural conversion, and crash risk while preserving the one-value public mechanic.

The appropriate next step is implementation, specialist audit, and tuning against the acceptance scenarios.
