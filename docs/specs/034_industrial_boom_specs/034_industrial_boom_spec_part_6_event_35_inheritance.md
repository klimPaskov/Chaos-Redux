# Industrial Boom specification, part 6: Event 35 inheritance

## Direct failure relationship

Event 35 Great Depression 2.0 is the failure state of Industrial Boom. Event 34 does not maintain a separate depression modifier, recovery category, severity value, or state shutdown system. It freezes the final boom condition and calls Event 35's reusable crisis-start or crisis-deepen package for the same country.

The direct handoff is a consequence of one Event 34 firing. It does not consume another random event selection, add another global pacing count, reset the timer again, or count as an independent Event 35 normal firing.

Event 35 can still fire independently through its own normal selection. It must know whether the crisis began independently or from Event 34.

## Ownership boundary

### Event 34 owns before handoff

- Active Industrial Boom state.
- Overheating and recent trend.
- Baseline phase.
- Active evolution level.
- Aggressive-action history.
- Reserve status.
- Industrial Region list.
- Project profiles and stages.
- Protection and fragility state.
- Region control and loss history.
- Unfinished speculative exposure.
- Landing attempt state.
- Repeat-boom history.

### Event 35 owns after handoff

- Depression Severity.
- Depression phase and recovery logic.
- Depression decisions and missions.
- State unemployment, idling, closure, rescue, or abandonment state.
- Depression evolution behavior.
- Recovery and relapse.
- Political consequences of prolonged depression.
- Final cleanup of inherited depression data.

### Frozen handoff snapshot

Event 34 should create a one-time snapshot before clearing its active state. Event 35 reads that snapshot once and stores any long-lived values in its own ledger. Event 35 should not keep reading mutable Event 34 working values after activation.

This boundary prevents cleanup order from changing starting severity and prevents future Event 34 firings from altering an active depression.

## Handoff conditions

The handoff begins when any of the following occurs:

- Overheating reaches 100.
- The Prevent the Crash mission fails at terminal pressure.
- An emergency production halt fails its forced-landing check.
- A critical shock pushes effective pressure beyond the remaining safety margin.
- A rough landing suffers a mapped post-boom failure during its vulnerability period.

The handoff should resolve after the current action or incident transaction finishes. It should not interrupt an equipment debit, state selection, or project update halfway through.

## Handoff data

The snapshot should carry the design information below. The implementation can encode it through variables, flags, arrays, state markers, or event targets according to engine constraints.

### Country identity

- Valid target country.
- Source marker: Industrial Boom collapse.
- Event 34 firing receipt or unique sequence identity.
- Date of collapse.
- Whether the collapse followed an ordinary crash, failed forced landing, failed emergency mission, or post-boom relapse.

### Evolution inheritance

- Active Event 34 evolution level.
- Proof that lower inherited stages are active.
- Whether any stage was disabled and therefore absent.
- Highest abnormal manifestation reached.

### Pressure state

- Final Overheating.
- Recent trend.
- Highest Overheating reached during the firing.
- Time spent in Dangerous Imbalance, Pre-crash, and Terminal Instability.
- Number and severity of recent major shocks.

### Management history

- Number of Run the Economy Hot uses.
- Whether an aggressive push was active at collapse.
- Whether cooling was active.
- Reserve status and whether reserves were consumed.
- Whether the country attempted a controlled or forced landing.
- Whether speculative projects were liquidated.

### Regional state

For each primary Industrial Region:

- State identity.
- Project profile.
- Project stage.
- Protection state.
- Fragility state.
- Control state.
- Damage or disruption state.
- Whether the region was lost and recovered.
- Whether a permanent legacy receipt had been secured but not converted.

For Evolution III spread:

- Primary region linkage.
- Secondary state identity.
- Spread status.
- Integration state.
- Fragility state.

### Repeat history

- Prior Event 34 crashes.
- Prior Event 35 crises caused by Event 34.
- Existing Event 34 legacy.
- Existing state exhaustion.

## Evolution mapping

The inheritance mapping is direct.

| Event 34 state at collapse | Event 35 entry |
| --- | --- |
| Baseline | Baseline Event 35 |
| Evolution I active | Event 35 Evolution I active |
| Evolution II active | Event 35 Evolutions I and II active |
| Evolution III active | Event 35 Evolutions I, II, and III active |

Event 35 should treat the inherited stage as a minimum. It may begin at a higher stage only when its own rules and current world state require that result. Event 34 does not infer or invent Event 35 stages that are disabled or unavailable.

## Starting Depression Severity

Starting Depression Severity should be dynamic. Final Overheating is the main anchor, but two crashes at the same number should not be identical when one country built reserves and another lost every Miracle Region.

### Severity contributors

Increase starting severity for:

- Higher final Overheating.
- Sharply rising trend.
- Longer time spent at dangerous pressure.
- Higher Event 34 evolution.
- Active speculative projects.
- Unfinished high-value projects.
- Depleted reserves.
- Lost primary regions.
- Damaged or compromised regions.
- Fragile Miracle Regions.
- Several Runaway spread states.
- Recent major industrial accidents.
- A failed forced landing.
- A previous Event 34 crash.
- Low stability.
- Blockade, fuel collapse, or severe trade isolation.

Reduce starting severity for:

- Limited or Strong reserves that remain available.
- Protected regions.
- Completed integration stages.
- Prior liquidation of speculative projects.
- A near-successful controlled landing.
- Stable supply and trade.
- A falling trend before one external shock caused collapse.
- Strong repair capacity.

### Severity outcome bands

The exact Event 35 scale belongs to Event 35. Event 34 should pass a severity seed that produces four broad entry outcomes.

#### Severe but recoverable

Typical source:

- Baseline crash near the threshold.
- Some reserves.
- Few damaged projects.
- No major region loss.

Event 35 begins with a strong immediate shock and a viable recovery path.

#### Deep depression

Typical source:

- Baseline or Evolution I crash with high speculative exposure.
- Weak reserves.
- Several unfinished projects.
- High trend and recent incidents.

Event 35 begins deeper and may idle more Industrial Regions.

#### Systemic industrial collapse

Typical source:

- Evolution II crash.
- Fragile Miracle Regions.
- Damaged supply network.
- Failed landing.

Event 35 begins with severe physical and financial overcapacity.

#### Near-total economic paralysis

Typical source:

- Evolution III crash.
- Unrestricted spread.
- Several fragile states.
- Depleted reserves.
- Terminal instability sustained for a long period.

Event 35 begins at Evolution III with very high Severity. The crisis remains playable and does not delete the country automatically.

## State conversion into Event 35

Inherited states should enter Event 35 according to their Event 34 condition.

### Secured and protected project

Possible Event 35 state:

- Strategic industry under stress.
- Temporarily idled but recoverable.
- Eligible for rescue decisions.
- Lower risk of physical factory loss.

### Secured but fragile Miracle Region

Possible Event 35 state:

- Overbuilt industrial center.
- High unemployment and credit failure.
- Large severity contribution.
- Valuable recovery target.

### Unfinished project

Possible Event 35 state:

- Abandoned works.
- Construction burden.
- Local stability pressure.
- Lower rescue value until basic cleanup occurs.

### Lost or damaged region

Possible Event 35 state:

- Broken supply chain.
- Idle or inaccessible industry.
- Strong initial severity contribution.
- Recovery tied to control and repair.

### Integrated Evolution III corridor

Possible Event 35 state:

- Network collapse affecting several connected states.
- Shared recovery objective.
- Strong infrastructure and capacity value if rescued.
- High relapse risk when only one part is repaired.

Event 35 should never recreate a state project reward that Event 34 did not secure. It can rescue inherited capacity, but it should not turn a failed speculative shell into free permanent factories.

## Existing Event 35 crisis

A collapse can occur while Event 35 is already active only through an approved overlap path or later event interaction. When this happens:

- Do not create a second category.
- Do not apply a duplicate base depression modifier.
- Do not reset recovery progress blindly.
- Raise Event 35 evolution to at least the inherited Event 34 level.
- Add a severity increase based on the frozen boom snapshot.
- Register new inherited states in the existing Event 35 ledger.
- Replace lower state conditions with stronger inherited conditions only when the new crash is worse.
- Record the Industrial Boom collapse as a new source episode inside the same depression.

If the active Event 35 stage is already higher than the inherited stage, keep the higher stage and deepen severity.

## Event history and player-facing continuity

### Event 34 history

Event History should record Event 34 once with the target actor. The result can later show controlled landing, rough landing, forced landing, or collapse through the selected-event details or result history when the framework supports it.

### Event 35 history

The direct crisis is a consequence, not another global pacing event. Event 35 may record a country crisis entry or source episode according to its own logging design. It should not masquerade as an independently selected random event.

### Text direction

The Event 35 opening after a boom should acknowledge:

- Production that had seemed inexhaustible stopping or reversing.
- Orders being cancelled.
- Credit or contracts failing.
- Industrial Regions idling.
- The speed of the reversal.
- The named target country and important affected states.

The text should not list inherited evolution variables, severity formulas, or raw project stages. The player already sees the consequence in Event 35's crisis surface.

## Transition of modifiers

The order matters conceptually:

1. Freeze the Event 34 snapshot.
2. End all aggressive and temporary Event 34 actions.
3. Remove the extraordinary boom bonuses.
4. Convert state project markers into Event 35 inherited states.
5. Start or deepen Event 35.
6. Apply the Event 35 opening shock.
7. Clear active Event 34 data that Event 35 has already consumed.
8. Preserve repeat-history and crash memory.

This order prevents the positive boom effect from coexisting with the final depression package and prevents Event 34 cleanup from erasing inheritance data.

## Post-boom vulnerability period

A rough landing may avoid immediate Event 35 while leaving the economy vulnerable.

During this bounded recovery period:

- Event 34 is no longer active.
- The main decision category is closed.
- Temporary exhaustion remains.
- A severe mapped economic or industrial shock can activate Event 35 with a lower inherited stage and severity seed.
- Ordinary minor setbacks do not retroactively turn every rough landing into a depression.

The vulnerability period should be visible through the exhaustion modifier. It should not maintain a hidden second version of Overheating after cleanup.

## Repeated boom and depression history

A country that has already passed from Event 34 into Event 35 should carry that memory into later firings.

Effects on later Event 34:

- Lower target selection weight for a recovery period.
- Higher starting pressure.
- Stronger speculative and maintenance risk.
- Better access to experienced emergency responses.
- Reduced remaining permanent capacity budget.

Effects on later Event 35:

- Prior crash history can increase relapse risk.
- States rescued in a prior depression can be more resilient.
- States abandoned in a prior depression can remain exhausted.

The history should not create permanent unavoidable failure. A country that recovered and prepared well can manage a later boom successfully.

## Conflict handling

The handoff must define responses to other active systems.

### Another economic crisis

When another system owns a country-wide economic crisis, Event 35 should either integrate it through a defined adapter or treat it as a severity factor. Event 34 should not create a duplicate parallel depression package.

### Natural disaster during handoff

The disaster retains ownership of its damage and deaths. Event 34 records the shock contribution. Event 35 receives the damaged state. No system applies the same building loss twice.

### State annexation during handoff

The snapshot uses the last valid state and country data. Event 35 registers only states still valid for the target. Lost regions still affect severity through broken supply and lost investment, but the target does not receive modifiers in a state it no longer owns or controls.

### Target country capitulation or deletion

If the country ceases to exist before Event 35 can start:

- The handoff ends safely.
- No invalid country target remains.
- State project markers are cleaned or transferred only through a separately approved rule.
- The Event 34 history records collapse without creating a ghost depression.

If the country survives as a government in exile or valid subject, Event 35 decides whether its ordinary civilian economy remains playable.

## Event 35 contract acceptance tests

The handoff passes when:

- The same country receives Event 35.
- The inherited evolution level is correct.
- Starting severity changes with actual boom condition.
- Reserves and protection reduce severity without erasing the crisis.
- Miracle Regions and spread states enter Event 35 coherently.
- Event 35 does not duplicate its category or modifier.
- The direct handoff does not count as a second global pacing event.
- Event 34 positive effects are gone before Event 35 penalties apply.
- Event 35 no longer depends on mutable Event 34 working values after activation.
- Invalid state and country targets clean safely.
- Repeat history records the crash.
- A saved game preserves the active depression and inherited state ledger.

The handoff fails when:

- Event 34 maintains a second depression implementation.
- Every crash starts Event 35 with the same severity.
- Evolution III can start only baseline Event 35.
- Existing Event 35 creates duplicate categories.
- Event 34 cleanup erases inherited regions.
- A crash grants permanent Event 34 project rewards.
- Generic disaster damage, deaths, or Chaos are applied twice.
