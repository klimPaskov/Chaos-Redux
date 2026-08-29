# Great Depression 2.0 specification, part 1: Core event and baseline lifecycle

## Catalog entry

- Event ID: `35`
- Event name: Great Depression 2.0
- Type: Minor Repeatable
- Status: To Be Reworked
- Chaos level: 1
- Cluster: Negative Economy
- Cluster member severity: Low

## Event premise

A major country or player-controlled country enters a severe economic depression. Factories remain standing while orders disappear, production lines lose efficiency, construction sites close, freight movement falls, firms fail, and households lose work. The opening shock is immediate enough to force a production and construction review. The crisis then becomes a long management problem instead of a fixed timed penalty.

The country manages one public value, `Depression Severity`. It summarizes contraction, unemployment, credit failure, falling demand, business closures, public confidence, trade disruption, and state financial stress. The simulation may track several hidden contributors, but the player sees one total, its trend, the next threshold, and the strongest causes that can be acted upon.

Event 35 has two valid entry paths. An independent firing selects a valid country and creates a severe but recoverable national crisis. An inherited firing begins when Event 34 Industrial Boom collapses. The inherited path targets the same boom country, reads one frozen collapse snapshot, raises the depression to the corresponding evolution floor, and converts the boom's projects and industrial regions into depression conditions.

The event is dangerous without being automatically terminal. Maximum Severity represents national economic paralysis. It can cause closures, unrest, political crises, and long recovery. It does not instantly remove every factory, delete the country, or force a civil war. Those outcomes require sustained conditions and their own visible chains.

## Core player experience

The baseline event creates six linked experiences.

1. **A sudden loss of economic freedom**
   - Existing production lines become less efficient.
   - Construction capacity falls enough to reorder the build queue.
   - Consumer and administrative pressure removes civilian capacity.
   - The opening penalty is stronger than the later sustained depression.

2. **One readable crisis value**
   - Depression Severity shows the current national condition.
   - A trend state explains whether the crisis is improving, stable, worsening, or accelerating.
   - The next threshold tells the player what will change if the present direction continues.
   - Up to three actionable causes explain the current movement without showing a full component ledger.

3. **Competing recovery philosophies**
   - Public works trade present civilian capacity for employment and infrastructure.
   - Strategic rescue protects critical military and industrial regions while leaving other sectors exposed.
   - Finance and trade stabilization slows deterioration by committing reserves, shipping, fuel, and administrative capacity.
   - Austerity, direct planning, and market liquidation offer different time horizons and political costs.

4. **State-level consequences**
   - A small number of Depression Centers represent the industrial regions where unemployment, closures, idle plants, and abandoned projects are concentrated.
   - The player can protect, reopen, restructure, or abandon these centers.
   - Local conditions feed the national crisis and create campaign memory after recovery.

5. **Recovery that must be proved**
   - Lowering Severity once does not end the event.
   - The country must hold the crisis below dangerous bands, restore key centers, and complete a recovery objective.
   - A premature withdrawal from recovery policy can cause a visible relapse.

6. **Escalation beyond one country**
   - Financial Contagion creates international exposure without giving every exposed country the full event immediately.
   - Social Collapse makes sustained economic failure a political and social struggle.
   - The Second Great Depression turns the crisis into a worldwide economic condition with a separate global lifecycle.

## Valid target selection

### Independent firing eligibility

A country is eligible for an independent Event 35 firing when all of the following are true:

- It exists.
- It is a major country or is controlled by a human player.
- It uses ordinary civilian and industrial systems.
- It controls at least one populated state with meaningful civilian or military industry.
- It does not have an active Great Depression 2.0 crisis.
- It is not inside the unresolved Event 34 to Event 35 transition.
- It does not have another economic state whose ownership contract makes a simultaneous depression incoherent.

A human-controlled non-major remains eligible. All costs, Depression Center counts, state effects, and recovery requirements scale from its actual economy.

### Ordinary civilian economy gate

Special Chaos actors and actual nonhuman countries should not receive the event through normal selection because the event assumes ordinary employment, consumption, trade, credit, political legitimacy, and household hardship. The implementation should use the existing shared civilian-system classifiers. An owning system may later provide a specific adapter for a special actor, but Event 35 should not infer one.

### Active depression exclusion

A country with an active Event 35 crisis is excluded from another independent target roll. A new consequence that reaches the same country uses the deepen path. It may increase Severity, raise the evolution floor, add state records, or extend relapse risk, but it does not create a second decision category, second crisis idea, second state registry, or duplicate event-history row.

### Target weighting

Every valid country needs a nonzero selection path. Weighting may rise with:

- A large civilian and military industrial base.
- High dependence on trade, convoys, ports, or imported resources.
- Recent rapid industrial expansion.
- Low or falling stability.
- Major infrastructure or supply disruption.
- A prolonged war with exhausted civilian capacity.
- Recent loss of a core industrial region.
- An earlier rough landing from Event 34.
- A player country that has not recently received a major economic event.

Weighting may fall with:

- A recent Event 35 firing in the same country.
- An active post-depression recovery safeguard.
- Very small industrial capacity that would make the normal opening incoherent.
- Strong stable infrastructure, trade access, and reserves.
- A conflicting event-owned crisis whose source contract blocks simultaneous activation.
- Repeated selection of the same largest major while other valid countries have not been targeted.

The weights create variety and plausible vulnerability. They do not guarantee that the weakest or largest country is selected.

### No valid target

When no valid country exists, Event 35 contributes no live candidate to automatic selection. The event list should display it as unavailable. The system should not queue a random country call that can resolve to nothing or a special actor.

## Entry modes

### Independent national depression

The ordinary entry performs these steps:

1. Select and freeze the valid target.
2. Record one Event 35 random-pool firing and actor.
3. Determine the independent starting Severity from the country's economic condition.
4. Select the opening Depression Centers.
5. Apply the immediate shock before the sustained crisis package.
6. Open the decision category and first stabilization objective.
7. Schedule the opening report and public news according to existing news settings.
8. Begin the sparse country and state evaluation schedule.

An independent firing normally starts in a severe but recoverable band. A weak country may begin higher because of blockade, collapsing stability, lost industry, or broken supply. A stable country may begin lower, but the opening must still matter.

### Industrial Boom collapse

The inherited entry is a consequence call owned by Event 34 and consumed by Event 35. It performs these steps:

1. Receive the exact target country and one frozen Event 34 snapshot.
2. Remove boom-only bonuses before applying depression penalties.
3. Convert Industrial Regions and unfinished projects into Event 35 state records.
4. Calculate inherited starting Severity from Overheating, evolution, reserves, regions, management history, and current country conditions.
5. Raise the Event 35 evolution floor to the inherited level.
6. Start or deepen the same Event 35 crisis.
7. Record the source as Industrial Boom collapse.
8. Avoid a second global pacing transaction.

The inherited opening needs separate player-facing direction. It should show the reversal in orders, investment, transport, wages, and plant operation. It should not print raw Overheating values or describe the handoff implementation.

### Financial Contagion conversion

When Evolution I creates enough exposure in another country, that country may convert from a lighter Economic Contagion condition into a full Event 35 crisis. This entry records its origin country and contagion chain, starts at a lower or moderate crisis band unless local conditions are already severe, and does not consume another normal random-pool selection.

### Worldwide depression conversion

Evolution III can place countries under a lighter worldwide pressure state. A country crosses into the full national crisis only when its local pressure and vulnerability meet the conversion threshold. This prevents the worldwide evolution from opening a large decision category for every country on the same day.

## Immediate economic shock

The opening shock is a short, severe state that makes the event visible before the slower depression model takes over.

It should affect:

- Factory output.
- Production-efficiency growth and, when appropriate, the usable efficiency ceiling.
- Construction speed.
- Civilian economic capacity through consumer or administrative pressure.
- Trade and logistics resilience.
- Stability or political confidence.
- Selected industrial states through local idle-plant and unemployment conditions.

The opening shock should be stronger than the sustained penalty at the same Severity. It represents cancelled orders, frozen credit, runs on institutions, emergency closures, abrupt layoffs, inventory liquidation, and projects halted before contracts can be reorganized.

The opening should not delete factories. Physical building loss belongs to prolonged high Severity, deliberate liquidation, failed state recovery, combat damage, or abandonment after repeated closures.

### Production-line treatment

The player must feel that existing production plans have become harder to sustain. The implementation may use a strong temporary production-efficiency penalty, lower efficiency growth, or staged industrial output penalties. It should avoid arbitrary destruction of all existing production efficiency when engine behavior would make the result disproportionate or difficult to explain.

### Economic law pressure

The crisis may make the most demanding economic laws harder to maintain through visible missions, temporary modifiers, or policy consequences. It should not silently force a law change on the opening day. A country that keeps an expensive law during deep depression should pay a larger civilian, stability, or recovery cost.

## Depression Centers

The opening marks a small number of important industrial states as Depression Centers. These states carry the local face of the crisis and give state-targeted decisions a clear purpose.

Selection should favor:

- Core states with high civilian or military factory concentration.
- States with railways, ports, supply hubs, or resource processing that matter to the national economy.
- Event 34 Industrial Regions when the crisis is inherited.
- States with unfinished boom projects or severe infrastructure strain.
- Populated states whose closure creates meaningful unemployment pressure.

Selection should avoid:

- Impassable states.
- Uncontrolled isolated holdings with little connection to the national economy.
- Empty states with no industrial role.
- Duplicate entries.
- A long list that turns the category into state-management clutter.

A small player country normally receives one center. A medium economy receives one or two. A large major receives two or three. Evolution III may create a fourth only when the country has a large inherited corridor or several distinct industrial regions. Three should remain the normal visible cap.

## Baseline lifecycle

The baseline lifecycle has four ordinary phases. These are not evolutions and should not create evolution-log entries.

### Phase 1: Panic and Contraction

The crisis has opened and the immediate shock is active. Severity is volatile. Institutions close, firms cancel investment, workers lose jobs, and production lines struggle to retain efficiency.

Player priorities:

- Stop the fastest deterioration.
- Choose which industrial regions must remain operational.
- Restore basic finance, trade, and transport.
- Begin employment or relief before social pressure hardens.
- Decide whether the country will follow an interventionist, planning, austerity, or liquidation approach.

Available content:

- Emergency Public Works.
- Rescue Strategic Industry.
- Stabilize Finance and Trade.
- One emergency mission to halt the panic.
- Austerity, planning, or market-clear actions when their visible conditions are met.

The phase has a minimum duration so a country cannot end the opening through one large decision. It ends when the immediate shock expires and the crisis has established its sustained Severity state.

### Phase 2: Depression

The opening panic has become persistent low output and unemployment. Government policy becomes the main play layer. Depression Centers may become distressed, idled, shuttered, protected, or placed under public works.

Player priorities:

- Lower Severity without exhausting the country.
- Reopen or restructure the Depression Centers.
- Protect military production during war.
- Prevent a relapse caused by withdrawing support too early.
- Contain foreign exposure when Evolution I is active.
- Prevent organized political breakdown when Evolution II is active.

Available content:

- The complete phased recovery action set.
- State protection, public works, rescue, restructuring, and reopening.
- Medium-duration recovery missions.
- Incidents tied to Severity, state status, policy history, and current war state.

The crisis should be capable of lasting for years when mismanaged. A strong player should still need sustained recovery work. One cheap meter reset cannot end it.

### Phase 3: Stabilization

Severity has remained below the dangerous range for a sustained period and the strongest causes of deterioration are controlled. The harshest national penalties begin to weaken. State reopening becomes more effective, but the economy remains vulnerable to shocks.

Player priorities:

- Reopen every required Depression Center.
- Maintain trade, supply, and finance support long enough to prove the improvement.
- Avoid a premature austerity or liquidation withdrawal.
- Complete the recovery proof objective.
- Choose which temporary institutions should become lasting reform and which should be dismantled.

Available content:

- Recovery projects.
- Final center reopening.
- Gradual removal of opening penalties.
- Policy consolidation choices.
- Relapse prevention mission.

A bad shock or policy reversal can return the country to the Depression phase. The player should see the relapse risk through a visible fragile-stabilization status, not through unexplained random punishment.

### Phase 4: Recovery

Recovery begins when Severity reaches the recovery floor, remains controlled, required state work is complete, and the country passes the final proof period.

The crisis closes in this order:

1. Freeze the recovery result and policy history.
2. Resolve remaining center statuses.
3. Remove crisis-only national and state penalties.
4. Apply bounded scars and recovery legacies.
5. Close the category and cancel obsolete missions.
6. Start a temporary post-depression safeguard and relapse watch.
7. Record the recovery outcome in event history and documentation-facing state.
8. Preserve repeat-history memory without retaining active arrays.

The country may retain a small number of meaningful long-duration or permanent effects. They should represent infrastructure rebuilt, institutions created, industrial consolidation, labor settlement, state planning, or hollowed regions. They should not form a stack of minor generic spirits.

## Baseline outcome bands

### Strong recovery

The country reaches the recovery floor with low relapse risk, all Depression Centers reopened or converted successfully, and no severe unresolved political crisis. It retains the best bounded recovery legacy and the fewest scars.

### Uneven recovery

The national crisis ends, but one center remains structurally weak, one emergency institution persists, or the country used a costly path that solved output while leaving political or social damage. It receives a useful but mixed legacy.

### Hollow recovery

Severity falls enough to close the crisis after deliberate liquidation, abandonment, or prolonged closure. The country has lower immediate depression pressure, but loses some industrial capacity, state potential, population stability, or long-term flexibility. This is a valid route with real cost, not a cheap exploit.

### Continued depression

Severity remains above the recovery floor or rises again during stabilization. The event stays active and may deepen. There is no arbitrary maximum duration that removes the crisis while the underlying conditions remain severe.

## Maximum Severity

Depression Severity is capped at its maximum range. Reaching the cap creates the deepest baseline condition and starts an emergency stabilization state.

At maximum Severity:

- National output can approach paralysis.
- Construction becomes extremely difficult.
- Civilian capacity is heavily constrained.
- Depression Centers can become shuttered or abandoned after sustained exposure.
- Stability and political legitimacy suffer.
- Strikes, protests, radical movements, and government crises become more likely.
- Evolution-specific spread and political effects receive their strongest valid weights.

The cap does not repeat damage every evaluation. One-shot thresholds, cooldowns, per-state damage limits, and recorded incidents prevent the country from losing the same factory or stability change again every pulse.

## Baseline political breakdown

Baseline Event 35 can produce unrest before Social Collapse activates. Deep Depression and Systemic Breakdown may create ordinary strikes, demonstrations, radicalization, cabinet crises, and emergency-government pressure. These incidents remain tied to Depression Severity, unemployment, failed policy, stability, and the condition of Depression Centers.

A rare baseline National Breakdown chain can end in civil conflict. It is available only after a visible warning and all of the following broad conditions:

- Severity has remained near Economic Paralysis for a sustained period.
- Stability and government legitimacy are critically weak.
- Several serious recovery or emergency responses have failed.
- At least one coherent political opposition, military split, or existing ideological base can support the other side.
- Valid territory, forces, equipment, leadership, and postwar handling exist.
- No recent civil war, protected aftermath, or conflicting country-creation system blocks the outcome.

High Severity by itself is insufficient. The player receives a Prevent National Breakdown objective and a final chance to lower Severity, restore one center, settle the immediate political crisis, or form a viable emergency government. Failure calls a strict validator and can still resolve as a government fall, policy reversal, or prolonged unrest when a coherent civil conflict cannot be created.

The baseline chain stays compact. It does not create the organized-movement registry, factory-occupation system, coup route, separatist package, ideology-specific transformation set, or extended political aftermath owned by Evolution II. When Social Collapse is active, its richer ladder absorbs the baseline checks and prevents duplicate strikes, crises, or wars.

## War and depression

War has mixed effects and should never be reduced to a universal recovery bonus.

Military demand can:

- Protect selected military production.
- Support employment in armament regions.
- Make Rescue Strategic Industry more effective.
- Give some countries a path out of idle capacity.

War can also:

- Disrupt trade and convoys.
- Consume fuel, trains, equipment, and civilian capacity needed for recovery.
- Expose industrial states to bombing and occupation.
- Raise shortages and household pressure.
- Make public works and finance stabilization more expensive.
- Create dependence on emergency law and state control.

The simulation should evaluate the country's real material position. A well-supplied major with secure territory may receive employment relief from war demand. A blockaded country losing industrial states should deteriorate faster.

## Peace and depression

Peace helps when it restores ports, trade, infrastructure, and civilian construction. It does not automatically end the crisis. Demobilization, cancelled military orders, and a sudden demand shift may create a temporary postwar shock in a country whose recovery depended entirely on armament demand.

## Active crisis and country changes

### Annexation or country deletion

If the country ceases to exist, Event 35 removes its active registry entries, state pointers, foreign exposure links, and missions safely. It does not search for a replacement owner and continue the same national crisis under a random tag.

### Civil war

A civil war does not create a full copy of the crisis for every participant by default. The original crisis owner and the economically relevant successor retain or divide state records through a bounded transfer contract. New sides can receive a temporary crisis condition based on the industrial states they control. Duplicate Severity values and state records are forbidden.

### State transfer

A Depression Center keeps its physical state condition when control changes. The national ledger records whether the center remains economically connected to the crisis owner. A new controller may receive a temporary local burden or a later claim to the center's recovery project. The previous country cannot continue paying for a project in a state it no longer controls.

### Faction or subject change

Faction and subject relationships alter contagion exposure and foreign aid possibilities. They do not end the national crisis. An overlord may support, exploit, or abandon a subject's recovery through Evolution I content.

## Repeatable identity

Event 35 remains Minor Repeatable in the global event system. Repeatability operates at the event pool level and at the country-history level.

A recovered country can receive Event 35 again after a meaningful safeguard period. A new episode remembers:

- Previous depression count.
- Earlier entry source.
- Reforms and emergency institutions retained.
- Depression Center scars.
- Industrial capacity already lost through earlier episodes.
- Previous contagion role.
- Earlier Event 34 crashes.
- Recovery philosophy and relapse history.

Repeat history should change vulnerability, starting conditions, and available text. It should not guarantee a harder crisis every time. Strong reforms can reduce future starting Severity or improve stabilization. Hollowed regions and repeated crashes can increase vulnerability.

## Baseline event flow

```text
Independent selection or consequence call
    -> validate exact target and source
    -> start or deepen shared Event 35 crisis
    -> apply immediate shock
    -> select or convert Depression Centers
    -> Panic and Contraction
        -> Depression
            -> Stabilization
                -> Recovery
            -> relapse to Depression
        -> deepening and maximum Severity
    -> apply bounded legacy and scars
    -> close active crisis and preserve history
```

Evolutions attach to this flow. They do not replace the baseline lifecycle. Financial Contagion adds international exposure, Social Collapse adds organized political consequences, and The Second Great Depression adds a worldwide pressure lifecycle.
