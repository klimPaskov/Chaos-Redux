# Industrial Boom specification, part 8: AI, probability, and balance

## AI design goal

AI countries should use Industrial Boom as an economic strategy under uncertainty. They must understand that short-term output, permanent development, and crash avoidance are different goals. Contextual scoring should combine war, supply, state exposure, reserves, project value, and Overheating. A fixed threshold script is inadequate.

The player should observe recognizable differences between a cautious peacetime major, a well-supplied wartime power, a blockaded maritime country, and a losing country that needs equipment immediately.

## AI strategic profiles

Profiles are decision styles, not permanent personality labels. A country can change profile when its strategic situation changes.

### Cautious consolidator

Typical situation:

- At peace or in a limited war.
- Adequate equipment.
- Valuable projects already active.
- High stability.
- No immediate military deadline.

Behavior:

- Builds reserves early.
- Protects the most valuable region.
- Uses Run the Economy Hot rarely.
- Prioritizes supply and integration projects.
- Begins controlled landing once good legacy is secured.
- Avoids unrestricted Evolution III spread.

### Balanced developer

Typical situation:

- Moderate equipment demand.
- Stable logistics.
- Enough civilian industry to invest.
- No severe blockade.

Behavior:

- Uses one early hot-running window.
- Builds Limited reserves.
- Designates one or two projects.
- Stabilizes near Visible Strain.
- Attempts a normal controlled landing.

### Wartime exploiter

Typical situation:

- Major war.
- Equipment deficit or planned offensive.
- Secure supply and fuel.
- Low or moderate Overheating.

Behavior:

- Uses Run the Economy Hot while the output window matters.
- Favors production and conversion projects.
- Delays landing while the military benefit remains larger than expected crash cost.
- Builds reserves when the war is long.
- Switches toward cooling after the military deadline or when supply worsens.

### Desperate gambler

Typical situation:

- Losing a major war.
- Severe equipment deficit.
- Threatened capital or industrial core.
- Limited time before defeat.

Behavior:

- Accepts high-risk output actions.
- May approve speculative projects.
- May use unrestricted Evolution III spread below Pre-crash.
- Protects one critical region if resources permit.
- Accepts a rough or forced landing when survival improves.
- Avoids long civilian commitments that cannot finish before military collapse.

This profile should be rare. It should not justify irrational actions after the country has already lost the capacity to use the output.

### Fragile retrencher

Typical situation:

- Blockade, fuel shortage, severe state damage, low stability, or prior crash.

Behavior:

- Stabilizes supply first.
- Builds or rebuilds reserves.
- Suspends fragile projects.
- Avoids running hot.
- Attempts an early controlled or rough landing.
- Refuses new Miracle or spread projects when their supply basis is missing.

## AI threshold behavior

Thresholds guide behavior but do not replace situation evaluation.

### Overheating below 25

AI may:

- Run the economy hot when wartime demand is high.
- Begin reserves.
- Designate projects.
- Protect exposed regions.

AI should not cool without a cause unless it is beginning a landing.

### Overheating from 25 to 44

AI may:

- Use one additional aggressive window with strong logistics.
- Prioritize reserves and supply.
- Continue project development.
- Begin evaluating landing value.

### Overheating from 45 to 64

AI should:

- Stop routine aggressive pushes.
- Stabilize the strongest cause.
- Protect or suspend fragile projects.
- Begin controlled landing when enough legacy is secured.

A desperate gambler can still push when a defined military deadline outweighs expected crash loss.

### Overheating from 65 to 79

AI should:

- Cool the expansion.
- Use emergency supply action when appropriate.
- Cancel weak speculative projects.
- Stop new project designation.
- Prepare a landing.

### Overheating from 80 to 94

AI should:

- End all aggressive actions.
- Start Prevent the Crash.
- Use reserves and emergency stabilization.
- Choose forced landing when controlled landing is no longer viable.

### Overheating from 95 to 99

AI should:

- Use only actions with a credible path below the emergency threshold.
- Avoid spending scarce resources on projects that cannot affect survival.
- Choose emergency halt when its success chance exceeds passive collapse.

## AI action evaluation

Every decision score should include:

- Current threshold and trend.
- Dominant pressure cause.
- Expected immediate Overheating change.
- Expected output change during the relevant strategic window.
- Resource affordability.
- War state and equipment need.
- Project value.
- Reserve status.
- Region exposure.
- Landing readiness.
- Event 35 inherited severity risk.
- Previous use and cooldown.

The AI should compare marginal value. It should not take Stabilize Supply Chains simply because the decision is available when the country has no material or transport pressure.

## AI project selection

### State ranking

AI ranks candidate regions by:

- Industrial share.
- Infrastructure and rail access.
- Resource or port value.
- Control stability.
- Enemy bombing and invasion risk.
- Existing protection.
- Project synergy.
- Remaining state legacy capacity.
- Adjacent spread potential under Evolution III.

AI should avoid putting every project in the capital when another state offers safer or more useful development.

### Profile ranking

AI chooses a project profile according to its bottleneck.

| Bottleneck or goal | Preferred project |
| --- | --- |
| Low production efficiency | Production Practices |
| Weak rail or internal supply | Rail and Supply Integration |
| Need to switch lines rapidly | Factory Conversion Capacity |
| Heavy bombing or disaster exposure | Industrial Repair Network |
| Resource and import pressure | Resource Efficiency |
| Evolution II raw-capacity opportunity with safe logistics | Permanent Industrial Capacity |
| Evolution II chronic material shortage | Synthetic and Recycling Complex |
| Evolution III strategic depth | Controlled Industrial Corridor |

AI should not choose a resource project merely because it has the highest generic reward.

## AI landing decision

AI calculates the value of remaining in the boom against expected crash loss.

Factors supporting continued boom:

- Critical wartime equipment demand.
- Low Overheating.
- Strong reserves.
- Valuable incomplete project close to integration.
- Strong supply and state control.
- Short military deadline.

Factors supporting landing:

- Secured project legacy.
- Rising Overheating.
- Weak supply.
- Exposed regions.
- High Event 35 severity risk.
- Completed military objective.
- Exhausted reserves.
- Previous crash history.

Cautious and balanced AI should begin landing before the first emergency band when sufficient legacy is available. Desperate AI can remain longer.

## Country target probability

The normal Event 34 target pool includes valid majors and player countries.

### Fairness goals

- A player-controlled non-major must have a meaningful chance.
- The same largest major should not receive most firings.
- A country with an active boom has zero eligibility.
- Recent recipients receive a strong temporary penalty.
- Previous crash history lowers weight for a recovery period without permanent exclusion.
- Strong and fragile economies both remain possible targets.

### Target scenarios

Target probability must be inspected with complete candidate pools under at least these world states:

1. Historical 1936 opening with ordinary majors and one player non-major.
2. Midwar world with several majors eliminated.
3. Multiplayer world with several player countries.
4. World where one country has active Event 34.
5. World where several countries are under Event 35 or other incompatible crises.
6. Late high-Chaos world with evolved opening eligibility.
7. World with only one valid target.
8. World with no valid target.

The audit should report exact normalized chance only when the complete pool and all external factors are supplied. Otherwise it should report ordering, bounds, or unresolved factors.

## Evolution pacing probability

Each active evolution is a timing surface.

### Pacing goals

- Evolution I should not fire immediately after the opening under normal conditions.
- Long active booms and repeated aggressive actions should bring it forward.
- Evolution II and III should require their lower stages and world thresholds.
- Landing preparation should lower or pause evolution risk.
- A boom that ends quickly may never evolve.
- An evolved opening should not log a new active evolution merely because the stage was already active at start.

### Timing scenarios

- Low Overheating, cautious management.
- Low Overheating, repeated hot-running periods.
- High Overheating, several projects.
- Controlled landing in progress.
- Evolution I active below the Evolution II world threshold.
- Evolution II threshold crossed while the boom remains active.
- High Chaos with Evolution III enabled.
- Disabled evolution stage.

## Incident probability

Incident selection should follow current causes.

### Incident pool rules

- Light incidents dominate early bands.
- Serious incidents require strain or strong exposure.
- Critical incidents require dangerous pressure or a severe external shock.
- Speculative incidents require Evolution I and speculative pressure.
- Miracle incidents require Evolution II and a valid Miracle Region.
- Spread incidents require Evolution III and a valid corridor or secondary state.
- A recent incident in one family lowers its repeat weight.
- An incident with no valid state target has zero weight.

### Starvation and dominance tests

The probability audit should confirm:

- No common generic incident starves evolution-specific content.
- No dramatic rare incident dominates because other branches become invalid.
- Protected regions materially reduce damaging incident weight.
- A country with no maritime dependence does not receive a convoy-specific incident.
- The same state is not repeatedly selected while its prior incident remains active.

## Decision probability scenarios

The supporting matrix contains detailed scenarios. The core required cases are:

1. Peacetime industrial major with strong logistics.
2. Winning wartime major with equipment demand and strong supply.
3. Losing wartime major with severe equipment deficit.
4. Blockaded maritime major.
5. Bombed major with one protected and one unprotected region.
6. Small player-controlled non-major.
7. Evolution I with active speculative project.
8. Evolution II with one fragile Miracle Region.
9. Evolution III with one controlled corridor and one unrestricted option.
10. Pre-crash country with depleted reserves.
11. Controlled landing nearly complete.
12. Country with previous Event 34 crash.

For each scenario, the audit should compare action ordering and identify any invalid action with nonzero score.

## Required probability workflow

Implementation should use the project probability workflow.

1. Inspect the exact weighted surface.
2. Declare candidate pool and external factors.
3. Evaluate named scenarios.
4. Sweep the important continuous factors, especially Overheating, equipment need, supply, and reserve state.
5. Simulate only when exact evaluation cannot capture repeated timing or incident sequences.
6. Compare the same scenarios after tuning.
7. Render a matrix or sensitivity view when it improves review.

A source-only reading of `ai_will_do`, MTTH, or random-list weights does not replace this evidence.

## Balance target for the opening bonus

The event should feel roughly comparable to doubling practical industrial productivity. This is a functional target, not a demand for one literal modifier.

### Baseline target

A representative major should experience:

- A clear increase in monthly equipment output.
- Faster ramp-up of a newly opened line.
- A construction queue that finishes materially earlier.
- Enough benefit to justify reorganizing production.
- Enough strain that the boost cannot remain indefinitely at no cost.

### Modifier mix direction

The implementation should spread power across:

- Factory output.
- Production-efficiency growth.
- Limited production-efficiency cap.
- Construction speed.
- Repair and conversion.
- Dockyard output where relevant.

It should avoid stacking maximum values on every modifier. The balance pass should compare total practical output under representative technologies, laws, and existing national spirits.

### Evolution scaling direction

- Evolution I raises immediate output and project speed moderately, while pressure rises faster.
- Evolution II raises state development and resource efficiency, with stronger permanent potential.
- Evolution III creates the strongest temporary output and map spread, with severe volatility.

Each evolution should change the source of power. A larger baseline country modifier alone does not meet this standard.

## Duration balance

The event uses dynamic duration. Desired ordinary outcomes:

| Style | Likely duration | Result goal |
| --- | --- | --- |
| Early wartime exploitation | Several months | Strong temporary output, rough or controlled landing |
| Balanced baseline management | Roughly half a year to one year | One or more meaningful legacy projects |
| Patient consolidation | Longer than one year when conditions stay sound | Exceptional landing within reward caps |
| Ignored Evolution III | One production campaign to terminal danger | High chance of Event 35 |

These ranges should be tested under actual evaluation cadence and decision cooldowns.

## Cost balance

### Affordability goals

- A small player country can take every essential safety action at a scaled cost.
- A major cannot trivialize the event because one train or one factory is enough.
- Stabilization costs compete with production and construction plans.
- Emergency actions are more expensive than early preparation.
- Reserves require a real sacrifice but remain cheaper than a crash.

### No dominant cost strategy

The balance pass should reject:

- One resource type paying for every action.
- Political power as the universal answer.
- Fuel costs so small that they never matter.
- Civilian factory commitments so large that a small country cannot play.
- Equipment costs disconnected from the action.
- Full cost debits on partial or invalid outcomes.

## Landing reward balance

### Reward goals

- A controlled landing is clearly better than letting the boom expire with no preparation.
- An exceptional landing feels campaign-defining.
- A rough landing preserves less.
- A crash never preserves the full intended legacy automatically.
- Repeat firings remain useful after raw-capacity caps.

### Snowball controls

- Country legacy budget.
- State legacy cap.
- Diminishing raw-capacity rewards.
- Later emphasis on logistics, repair, conversion, and timed benefits.
- Higher pressure after repeated booms.
- No reward conversion before landing.

The balance test should include a major receiving several successful booms across a long campaign. The resulting industry must remain strong but bounded.

## Event 35 risk balance

A crash should be serious enough that players respect Overheating. It should remain playable.

- Baseline crash should disrupt war plans and require active recovery.
- Evolution I crash should feel financially deeper.
- Evolution II crash should make Miracle Regions major recovery problems.
- Evolution III crash should create near-paralysis without deleting the country automatically.
- Reserves and protection should matter.
- Repeated crash history should worsen risk without making recovery impossible.

## AI acceptance criteria

AI behavior passes when:

- It can finish the event without player-only actions.
- It does not run hot at terminal pressure.
- It chooses state projects that match real bottlenecks.
- It protects vulnerable valuable regions.
- It lands after securing value in normal conditions.
- It can make a deliberate wartime gamble.
- It changes strategy after blockade, state loss, or fuel collapse.
- It respects disabled evolutions and invalid states.
- Its weighted choices pass the named scenario comparison.
- It does not produce decision spam or repeated failed missions.

AI behavior fails when:

- Every country follows the same route.
- A single action has dominant weight in every scenario.
- The AI spends resources it cannot afford.
- It starts projects after the landing mission begins.
- It continues unrestricted spread in Pre-crash.
- It ignores a protected region and repeatedly targets an invalid state.
- It receives hidden free relief unavailable to the player.
