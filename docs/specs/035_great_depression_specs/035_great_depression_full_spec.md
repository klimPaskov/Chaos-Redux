# Great Depression 2.0 full specification

This consolidated file reproduces the specification index and the eleven canonical source parts in order. The individual files remain authoritative for editing and review.


---

<!-- Source: 035_great_depression_spec_index.md -->

# Event 35 Great Depression 2.0 specification index

## Catalog identity

- Event ID: `35`
- Event name: Great Depression 2.0
- Event type: Minor Repeatable
- Status at planning time: To Be Reworked
- Chaos level: 1
- Cluster: Negative Economy
- Cluster member severity: Low
- Direct source event: Event 34 Industrial Boom


## Reading and environment boundary

Every file supplied with this task was read in full, including the three catalog exports, all twenty subagent definitions, and every Markdown file in the accepted Event 34 planning package. The live public repository was inspected for Event 34 and Event 35 migration context.

The Windows-only offline Paradox wiki snapshot, installed Hearts of Iron IV documentation, installed vanilla game files, and local HOI4 MCP server were not mounted in this ChatGPT environment. This package therefore does not claim engine-syntax validation, vanilla-precedent inspection, MCP event-chain evidence, or live-game validation. The coding prompt makes those checks mandatory before implementation.

## Design promise

Great Depression 2.0 places one major country or player-controlled country inside a long economic crisis that changes production, construction, logistics, politics, and state development. The player manages one public value, `Depression Severity`, through a compact decision category and a small set of state recovery projects. An independent firing begins as a severe but recoverable national depression. A collapse from Event 34 begins from the same reusable crisis package, inherits the boom's evolution floor, and converts the failed boom's regions, reserves, projects, and management history into the opening depression state.

The event remains playable at maximum Severity. Deep failure causes industrial paralysis, closures, unrest, political transformation, and possible civil conflict through bounded conditions. It does not erase the country through one threshold. Recovery requires sustained improvement, reopened Depression Centers, and a final proof period. Repeat firings remember reforms and scars without becoming a renewable factory deletion or permanent reward exploit.

## Specification files

1. `035_great_depression_spec_part_1_core.md`
   - Event identity, target selection, independent and inherited entry, baseline phases, crisis outcomes, and active-crisis rules.
2. `035_great_depression_spec_part_2_severity.md`
   - Depression Severity scale, hidden contributors, thresholds, trend, shocks, relief, relapse, and tuning model.
3. `035_great_depression_spec_part_3_decisions_missions.md`
   - Decision category, six recovery philosophies, timed objectives, dynamic costs, visibility, AI equivalents, and cleanup.
4. `035_great_depression_spec_part_4_centers_recovery_repeatability.md`
   - Depression Centers, local state progression, closures, reopening, permanent scars, recovery legacies, and repeatability controls.
5. `035_great_depression_spec_part_5_financial_contagion.md`
   - Evolution I exposure network, secondary-country pressure, foreign intervention, full-crisis conversion, and spread controls.
6. `035_great_depression_spec_part_6_social_collapse.md`
   - Evolution II strikes, occupations, riots, radical movements, emergency governments, coups, separatism, civil conflict, and political aftermath.
7. `035_great_depression_spec_part_7_second_great_depression.md`
   - Evolution III worldwide pressure, international stages, supplier booms, global recovery, and worldwide news role.
8. `035_great_depression_spec_part_8_inheritance_connections_chaos_cluster.md`
   - Event 34 handoff, reusable crisis API, cross-event adapters, conflict precedence, Chaos accounting, and Negative Economy cluster behavior.
9. `035_great_depression_spec_part_9_ai_probability_balance.md`
   - AI profiles, target selection, action ranking, probability scenarios, balance goals, exploit controls, and performance limits.
10. `035_great_depression_spec_part_10_presentation_assets_text.md`
    - Presentation hierarchy, player-facing writing direction, report and news roles, visual asset inventory, accessibility, and Evolution III worldwide-news direction.
11. `035_great_depression_spec_part_11_achievements_acceptance.md`
    - Achievement contracts, edge cases, acceptance scenarios, completion evidence, and improvement-loop closure.

## Supporting files

- `035_great_depression_decision_map.md`
- `035_great_depression_state_lifecycle_map.md`
- `035_great_depression_ai_probability_matrix.md`
- `035_great_depression_chaos_impact_map.md`
- `035_great_depression_reusable_crisis_api.md`
- `035_great_depression_research_notes.md`
- `035_great_depression_repository_crosscheck.md`
- `035_great_depression_source_reading_ledger.md`
- `035_great_depression_subagent_review.md`
- `035_great_depression_package_manifest.md`

## Prompt files

- `035_great_depression_asset_prompt.md`
- `035_great_depression_achievement_prompt.md`
- `035_great_depression_decision_mission_prompt.md`
- `035_great_depression_coding_prompt.md`
- `035_great_depression_super_event_prompt.md`
- `035_great_depression_goal_prompt.md`

## Consolidated reading copy

- `035_great_depression_full_spec.md`

This file combines the index and all eleven source specification parts in their canonical order. Supporting maps, research, prompts, and ledgers remain separate to keep the design source readable.

## Presentation choice

The main mechanic uses the ordinary decision interface with a strong category picture, one Depression Severity meter or compact progress display, a trend indicator, the next threshold, up to three material causes, and a phased action list. A separate event-owned scripted GUI is not the planned baseline because the player has one public value and no more than five primary actions in one phase. The implementation agent may escalate to a dedicated window only after direct inspection proves that the ordinary category cannot present the severity state, selected Depression Center, and active mission clearly. Such a change requires a recorded design exception and the event UI workflow.


---

<!-- Source: 035_great_depression_spec_part_1_core.md -->

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


---

<!-- Source: 035_great_depression_spec_part_2_severity.md -->

# Great Depression 2.0 specification, part 2: Depression Severity

## Public mechanic

`Depression Severity` is the only persistent event-specific number the player must manage. It uses a `0` to `100` scale. The category shows the current value, a named band, a qualitative trend, the next threshold, and up to three material causes. It does not expose the hidden component ledger or require the player to track separate unemployment, banking, demand, trade, confidence, and fiscal meters.

The value measures the country's ability to keep production, construction, employment, credit, trade, transport, and public confidence working at the same time. A low value means the economy has regained ordinary coordination. A high value means firms cannot obtain orders or finance, workers cannot find employment, public authorities cannot support every failing sector, and industrial regions are becoming disconnected from national recovery.

## Initial tuning scale

| Severity | Working band label | Player-facing meaning | Main gameplay change |
| ---: | --- | --- | --- |
| `0-14` | Recovery Floor | Ordinary coordination has returned, but the recovery still needs proof | Final recovery mission becomes possible |
| `15-29` | Stabilizing Economy | Output and confidence are returning while the country remains vulnerable | Harshest penalties continue to weaken |
| `30-49` | Fragile Economy | Growth is possible, yet closures and unemployment can return after a shock | Stabilization progress can be lost |
| `50-69` | Depression | Persistent contraction defines national planning | Full baseline decision loop is active |
| `70-84` | Deep Depression | Credit, demand, freight, and employment failures reinforce each other | Stronger national and state penalties apply |
| `85-99` | Systemic Breakdown | The state cannot protect every region or institution | Emergency actions and severe incidents become eligible |
| `100` | Economic Paralysis | National economic coordination has reached its worst supported state | A guarded maximum-Severity emergency begins |

These bands are initial design targets. The implementation should centralize them in Event 35 script constants and tune them through scenario comparison. Their ordering and gameplay meaning are fixed. Small numeric adjustments are allowed when testing proves that phase transitions occur too quickly or that a crippled country lacks a viable recovery path.

## Severity is distinct from phase

The four baseline phases and the seven Severity bands serve different purposes.

- The phase records where the country is in the event lifecycle.
- The Severity band records how damaged the economy is now.
- Panic and Contraction can begin at several high bands.
- The Depression phase can continue after Severity first falls below `50` because stabilization must be sustained.
- Stabilization can relapse into Depression.
- Recovery requires a low Severity band plus state and mission proof.

A phase change therefore cannot be inferred from one value check. The country must satisfy duration, mission, and state conditions as well.

## Hidden component model

The simulation may track the following internal components. They are hidden inputs and must not become additional player-facing counters.

### Credit and banking stress

Represents bank closures, frozen lending, capital flight, deposit fear, failed refinancing, distressed public debt, and the inability of firms to finance payroll or working capital.

It rises through:

- Banking or credit incidents.
- Repeated policy reversals.
- High instability.
- Evolution I exposure to another failing economy.
- A failed finance mission.
- Loss of a major commercial center.
- Unfunded rescue commitments.

It falls through:

- A successful banking audit or temporary bank holiday.
- Deposit or credit guarantees that the country can sustain.
- Recapitalization of viable institutions.
- A credible debt standstill or restructuring path.
- Foreign credit support.
- Sustained low Severity without a new panic.

### Demand and employment stress

Represents cancelled orders, falling household purchases, unemployment, inventory liquidation, falling wages, and idle plants.

It rises through:

- Shuttered Depression Centers.
- Austerity or liquidation without a compensating recovery source.
- Postwar demobilization when the economy relied on military orders.
- Failed public works or employment missions.
- Severe trade contraction.
- Long exposure to high Severity.

It falls through:

- Public works.
- Reopened industrial states.
- Stable military demand when supply is secure.
- Foreign reconstruction orders.
- Social relief that preserves purchasing power.
- Successful local employment projects.

### Trade and external-finance stress

Represents lost export markets, collapsed trade credit, foreign-exchange pressure, blocked imports, convoy losses, failed clearing arrangements, and dependence on a distressed partner.

It rises through:

- Port or convoy disruption.
- Blockade.
- Loss of trade access.
- Evolution I contagion.
- Evolution III world contraction.
- Dependence on one supplier or market that becomes unavailable.
- Sanctions or embargoes that have an exact registered source.

It falls through:

- Restored ports and convoys.
- Clearing agreements.
- Diversified imports.
- A foreign aid corridor.
- A stable supplier relationship.
- Recovery of exposed partners.

### Industrial and logistics disruption

Represents lost industrial states, broken railways, damaged infrastructure, bombing, natural disasters, fuel shortages, train shortages, and supply-chain interruption.

It rises through:

- Loss or occupation of a Depression Center.
- Damage to factories, railways, ports, infrastructure, or supply hubs.
- Low trains, trucks, fuel, or convoys relative to the country's burden.
- Failed center protection.
- An Event 34 inherited network collapse.
- Registered natural-disaster or strategic-attack shocks.

It falls through:

- Restored state control.
- Railway and infrastructure repair.
- Protected industrial regions.
- Adequate logistics reserves.
- Successful strategic-industry rescue.
- Completed public works that solve an identified bottleneck.

### Fiscal and policy stress

Represents the cost of relief, debt service, emergency subsidies, administrative overload, expensive economic laws, policy contradiction, and the inability to finance every intervention.

It rises through:

- Several expensive programs at once.
- Emergency economic laws unsupported by production.
- Frequent changes in recovery doctrine.
- Failed public commitments.
- Prolonged high-cost rescue policy.
- Large subject or ally support burdens.

It falls through:

- A credible budget settlement.
- Prioritization of a smaller set of programs.
- Debt restructuring.
- Recovered tax and production capacity.
- Austerity that does not trigger a larger demand collapse.
- External grants or aid that have a real provider.

### Social confidence and institutional stress

Represents confidence in the government, willingness to keep deposits and contracts in normal channels, labor peace, public patience, and the ability of institutions to carry out policy.

It rises through:

- Falling stability.
- Repeated failed missions.
- Long unemployment in the same regions.
- Repression, riots, and unresolved strikes.
- Corruption or exposed favoritism.
- A failed government or cabinet crisis.

It falls through:

- Clear and sustained recovery policy.
- Reopened centers.
- Negotiated labor settlements.
- Visible employment gains.
- High stability.
- Successful relief and confidence actions.
- Recovery without unexplained policy reversals.

### War-demand relief and war burden

War is evaluated as a mixed internal factor instead of a flat modifier.

War demand can lower demand and employment stress when:

- Military factories have secure inputs.
- The country controls its industrial regions.
- Supply and fuel are adequate.
- Foreign or domestic orders are rising.
- The state can protect civilian consumption from total collapse.

War burden raises Severity when:

- Ports, convoys, fuel, trains, or imported resources are failing.
- Core industrial states are bombed or occupied.
- The country has severe equipment and manpower shortages.
- Civilian construction is fully displaced by emergency demand.
- The government maintains expensive laws that the depressed economy cannot support.

## Severity evaluation pulse

Event 35 uses a sparse active-country schedule. Only countries with an active national crisis, a registered contagion condition, or Evolution III pressure are evaluated. The event must not introduce an unauthorized recurring scan across every country.

The normal national evaluation cadence is dynamic but bounded. Panic and Contraction or Economic Paralysis normally schedule the next pulse in `3` to `5` days. Sustained Depression normally uses about `7` days. Stabilization normally uses `10` to `14` days, while final recovery proof uses `7` to `10` days. A new major shock or highly volatile trend can shorten the next interval. Immediate decisions, state loss, registered attacks, inherited Event 34 collapse, and other exact shocks may update Severity between scheduled evaluations.

Only one next-pulse receipt may exist for one country and episode. Cadence changes reschedule that country instead of stacking parallel timers. The drift calculation normalizes pressure by elapsed days so a shorter emergency cadence does not multiply the seven-day-equivalent pressure.

Each normal pulse follows this logic:

1. Read the current phase and Severity band.
2. Rebuild the hidden material contributors from current country and registered state conditions.
3. Add active policy pressure and relief.
4. Apply external-shock memories that have not expired.
5. Apply evolution-specific pressure.
6. Calculate a bounded Severity change.
7. Clamp the value between `0` and `100`.
8. Update the short trend history.
9. Check one-shot thresholds, phase progress, missions, state progression, and incidents.
10. Schedule the next active-country pulse.

Normal drift should usually be small enough that decisions and external shocks remain meaningful. One scheduled pulse should not move the country from Deep Depression to the Recovery Floor without a major mission result. Large changes belong to opening shock conversion, a serious state loss, Event 34 collapse, a bank panic, a coordinated rescue, or another visible incident.

## Drift structure

The implementation should calculate a net pressure score from hidden contributors, then convert it into one bounded Severity change.

A useful initial structure is:

```text
base phase pressure
+ credit and banking pressure
+ demand and employment pressure
+ trade and external pressure
+ industrial and logistics pressure
+ fiscal and policy pressure
+ social and institutional pressure
+ evolution pressure
+ recent shock memory
- active relief
- completed project relief
- stable war demand relief
- foreign support
= net pressure
```

The net score should map to a limited seven-day equivalent movement band, then scale by the actual bounded interval. The exact mapping belongs in script constants. As a starting balance target:

- Very strong recovery conditions can lower Severity by roughly `2` to `4` in a week.
- Normal successful policy lowers it by roughly `1` to `2`.
- A broadly balanced week moves it by `0` or `1`.
- Material deterioration raises it by roughly `1` to `3`.
- A severe registered shock may raise it by `4` to `10` immediately.

These are tuning targets, not player-facing promises. They prevent one ordinary pulse from deciding the whole event.

## Public trend

The trend is derived from recent Severity movement and material shock state. It is qualitative.

| Working trend | Meaning | Suggested evidence window |
| --- | --- | --- |
| Rapidly Improving | Several recent pulses and missions produced strong net relief | Last three normal pulses plus current mission result |
| Improving | Recent net movement is clearly downward | Last three normal pulses |
| Stable | Movement is small or alternating | Last three normal pulses |
| Worsening | Recent net movement is clearly upward | Last three normal pulses |
| Accelerating | Worsening pressure is increasing or a major unresolved shock is active | Last three pulses plus shock memory |

The category should pair the label with an icon or arrow. Color is supporting information. The player must not need color vision to understand the direction.

The public cause list shows no more than three current reasons. It should prefer causes the player can act on. Examples include frozen credit, shuttered industrial regions, broken freight, blockade, war orders, public works, stable banking, or foreign support. It should not show raw formulas or every minor contributor.

## Independent starting Severity

An independent firing begins in a severe but recoverable range. The initial target is usually between `58` and `74`.

Starting Severity rises with:

- Falling or very low stability.
- A major industrial state recently lost or damaged.
- Severe blockade or trade disruption.
- Low trains, convoys, or fuel relative to need.
- Existing famine, migration, or humanitarian pressure with a valid shared context.
- A recent failed economic recovery.
- A prior hollow Event 35 outcome.
- An expensive war that has lost its supply base.

Starting Severity falls with:

- Strong reserves and infrastructure.
- Secure trade and ports.
- Stable government.
- Earlier durable recovery reforms.
- A recent successful Event 34 controlled landing without collapse.
- A small industrial base that cannot support the normal upper opening range.

The independent path should not start below the normal Depression band. Event 35 must change production and construction planning from its first day.

## Inherited starting Severity

An Event 34 collapse begins from the frozen boom snapshot. The initial target can range from the upper Depression band to near Economic Paralysis.

The calculation must use:

- Final Overheating.
- Peak Overheating.
- Time spent in dangerous Overheating bands.
- Final Overheating trend.
- Boom evolution floor.
- Reserve condition.
- Controlled-landing preparation and failure state.
- Number and condition of Industrial Regions.
- Completed, protected, speculative, unfinished, fragile, or abandoned projects.
- Event 34 external shocks.
- Earlier boom crashes and depression episodes.
- Current stability, trade, logistics, and state control.

A high Overheating number alone must not determine the result. A country that built reserves, protected regions, and attempted a landing should begin below an equally overheated country that ran without reserves and lost its core industrial network.

Suggested inherited entry bands:

| Snapshot result | Starting Severity direction |
| --- | --- |
| Baseline crash with reserves and partial landing preparation | Severe but recoverable |
| Baseline or Evolution I crash with weak reserves and speculative exposure | Deep Depression |
| Evolution II crash with fragile Miracle Regions | Systemic Breakdown |
| Evolution III network collapse with failed emergency halt | Very high Systemic Breakdown or Economic Paralysis |

## Contagion and worldwide conversion starts

A country that converts from Economic Contagion usually starts lower than the origin country. Its initial range should reflect local vulnerability and the strength of the connection. A stable country with one exposed market can begin around the Fragile Economy or lower Depression bands. A dependent subject, lender, or trade hub with several failed links can begin in Deep Depression.

Evolution III conversion uses the worldwide pressure state plus local vulnerability. It must not give every country the same starting value. Self-sufficient, stable, and lightly connected countries should remain under the lighter global condition for longer. Highly connected or already unstable countries may enter the full crisis quickly.

## Immediate shocks

An immediate shock is a one-time or short-memory change tied to a visible event. It must have an exact source and a repeat guard.

### Supported shock families

- Loss of a Depression Center.
- Destruction or heavy damage in a registered industrial state.
- Port, convoy, rail, supply-hub, or infrastructure collapse.
- Bank panic or credit freeze.
- Trade or clearing agreement failure.
- Major policy reversal.
- Failed recovery mission.
- Event 34 collapse.
- Contagion from a registered source country.
- Evolution III world-market contraction.
- Postwar cancellation of military orders.
- A registered embargo or sanction with a material economic effect.

### Shock memory

A severe shock can affect several following pulses without reapplying its full immediate value. The event records a decaying shock memory. It is cleared after its defined duration or after a direct recovery action resolves it.

The same state loss, bank failure, or mission failure cannot create a new full shock every pulse. A new shock requires a new receipt, new source, or new threshold.

## Threshold behavior

Thresholds change available content and modifiers. Crossing a threshold is recorded once in each direction where useful.

### Crossing into Deep Depression

- Stronger national penalties apply.
- A second Depression Center may be selected for a large economy if the normal cap allows it.
- Emergency finance, employment, or freight actions become more important.
- Evolution I spread receives more source pressure when active.

### Crossing into Systemic Breakdown

- Ordinary aggressive or low-urgency actions are hidden.
- Emergency recovery missions replace them.
- Depression Centers can progress toward shuttering after sustained exposure.
- Baseline strikes, radicalization, cabinet crises, and National Breakdown warnings become eligible through their own strict conditions.
- Social incidents receive stronger valid weights and use the organized movement ladder when Evolution II is active.
- The country can no longer change doctrine freely.

### Reaching Economic Paralysis

- Apply the deepest national dynamic modifier once.
- Start one maximum-Severity emergency objective.
- Freeze repeated destructive threshold effects behind receipts and cooldowns.
- Allow limited emergency aid and forced stabilization actions even for a country with little remaining civilian capacity.
- Keep the country playable.

### Falling below the Stabilization threshold

- Start or advance the sustained stabilization timer.
- Weaken the harshest penalties gradually.
- Unlock center reopening and policy consolidation.
- Do not close the crisis yet.

### Reaching the Recovery Floor

- Start the final recovery proof only when required centers and emergencies are resolved.
- A single shock can pause or reset the proof.
- The active event closes only after the proof duration is complete.

## Phase timers and proof periods

Initial tuning targets:

- Panic and Contraction minimum duration: about `35` days.
- Stabilization qualification: Severity below `40` for about `42` consecutive days.
- Recovery Floor proof: Severity at or below `14` for about `60` consecutive days.
- Post-recovery safeguard against independent refiring: at least `180` days, increasing modestly after repeated episodes.

The implementation may tune these values through constants. It must preserve the need for sustained improvement.

## Relapse

A relapse is a return from Stabilization to Depression after the economy appeared to be recovering.

Relapse can occur when:

- Severity returns to `50` or higher.
- Severity remains above the stabilizing range for a sustained period.
- A required center closes again.
- A major bank, trade, or war shock occurs.
- The player withdraws support before completing the recovery proof.
- Evolution I or III creates a new external contraction.

The player receives a visible fragile-recovery status before normal drift alone can cause relapse. A sudden major shock may trigger it immediately. The relapse removes accumulated proof progress and restores the appropriate sustained penalties. It does not repeat the full opening shock unless a new crisis source justifies one.

## Maximum-Severity emergency

The maximum-Severity objective should last long enough to permit response, normally between `90` and `150` days depending on country capacity and active evolutions.

Success requires a combination of:

- A material Severity reduction.
- At least one operating or protected Depression Center.
- No unresolved bank panic or freight collapse.
- Payment of the selected emergency policy's real costs.

Success returns the country to Systemic Breakdown or Deep Depression with a temporary no-relapse breathing period. It does not end Event 35.

Failure may:

- Shutter one eligible Depression Center.
- Apply a bounded factory or infrastructure loss in an already distressed state.
- Trigger a baseline government crisis or advance the visible National Breakdown warning.
- Call the rare baseline civil-conflict validator after the full gate and failed prevention objective.
- Activate or advance the organized Social Collapse ladder when Evolution II conditions are met.
- Increase international pressure when Evolution I or III is active.

Failure does not repeat automatically while Severity remains at `100`. A new maximum-Severity emergency requires a cooldown and a new failure condition. The baseline civil-conflict validator can return a nonwar political outcome when the actor, territory, force, or recent-war requirements are not met.

## Baseline National Breakdown gate

The baseline political failure route uses a separate guarded state, not a hidden automatic threshold effect.

Initial tuning direction:

- Severity near `95` or higher for about `90` to `120` consecutive days.
- Very low stability or a proved government-legitimacy failure.
- At least two failed major recovery, emergency, or political responses.
- One coherent opposing political or military base.
- At least one valid territorial and force package.
- No recent civil war or protected aftermath.

The warning state starts Prevent National Breakdown. Success clears the immediate breakdown risk and applies a cooldown. Failure makes civil conflict eligible, but does not guarantee it. The final outcome can be a government replacement, emergency rule, policy reversal, prolonged unrest, or civil conflict according to the validated country state.

When Evolution II is active, Social Collapse owns the movement, coup, separatist, and civil-conflict outcome selection. The baseline gate is suspended so the same economic failure cannot create two political chains.

## National penalty model

Use one event-owned dynamic modifier or a small staged family that reads Severity and phase. Do not stack one separate national spirit for every threshold.

The model should affect:

- Factory output.
- Production-efficiency growth.
- Usable production-efficiency ceiling where appropriate.
- Construction speed.
- Civilian economic capacity.
- Trade and logistics resilience.
- Stability pressure.
- Political or law-maintenance pressure where supported.

The opening shock is a separate short modifier because it is intentionally harsher than the sustained state. Recovery legacies and scars are separate because they persist after the active crisis.

At severe levels, the player should need to change production and construction plans. At maximum Severity, ordinary output may approach paralysis. The event must preserve enough residual capacity, emergency aid access, or scaled-down action costs to avoid a scripted soft lock.

## Severity reduction cannot be purchased directly

No decision should be a simple political-power purchase that removes a large fixed amount of Severity. Every large reduction must come from a policy action, state project, foreign agreement, emergency mission, or accepted sacrifice with real requirements and time.

Small immediate changes are acceptable when they represent the first effect of a larger action. The main result should be delivered through sustained relief, project completion, or mission success.

## Scaling and fairness

Costs and relief scale from the target country's usable economy, not raw total factories alone. A depressed country with many locked factories must not receive costs calculated as if every factory were available.

The implementation should consider:

- Total and usable civilian factories.
- Total and usable military factories.
- Number of Depression Centers.
- Severity band.
- Current war state.
- Stockpile floors.
- Country size.
- Player or AI control.
- Prior failed actions.

A small player country must have a viable one-center recovery loop. A large major must pay more and manage more regional exposure. The event should remain serious in both cases.

## Save continuity and reconciliation

On load or runtime rebuild, Event 35 must reconcile:

- Active crisis flag and episode ID.
- Current Severity and phase.
- Recent trend history.
- Active shock memories.
- Doctrine and policy history.
- Depression Center registry.
- Evolution floor and active evolution modules.
- Contagion source and exposure links.
- Stabilization and recovery proof progress.
- Maximum-Severity receipt and cooldown.

Missing or malformed history should fail closed into a safe active crisis state. It must not reset Severity to zero, duplicate the opening shock, repeat threshold damage, or create a second category.

## Tuning ownership

All thresholds, duration bands, maximum changes, scaling steps, caps, AI weights, and evolution multipliers belong in Event 35 script constants or another documented tuning surface. The design should avoid scattered literals across events, decisions, effects, triggers, and localisation.

The implementation report must list the final constants and the scenario evidence used to tune them.


---

<!-- Source: 035_great_depression_spec_part_3_decisions_missions.md -->

# Great Depression 2.0 specification, part 3: Decisions, recovery doctrines, and missions

## Presentation choice

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

The baseline mechanic uses one ordinary decision category with a strong static category picture and compact dynamic text. It does not begin with a separate scripted GUI.

The category header shows:

- Depression Severity.
- Severity band.
- Trend.
- Current baseline phase.
- Current recovery doctrine.
- Next meaningful threshold.
- Up to three material causes.
- The selected Depression Center when a state action is open.
- The active main objective.

The category should normally expose three to five primary actions. Six is the hard maximum for one phase. One to three missions may be visible at once. Obsolete, invalid, completed, or lower-priority actions are hidden.

A dedicated event-owned window is justified only if implementation inspection proves that the ordinary category cannot show Severity, one selected center, and the active mission clearly. Such a change requires a documented design exception, exact GUI ownership, and the event UI workflow.

## Recovery doctrine

The country chooses one current recovery doctrine during Panic and Contraction. The doctrine is a categorical policy state, not another numerical meter. It controls which actions, costs, incidents, AI preferences, and recovery legacies are available.

The six doctrines are working design labels. Final player-facing names and descriptions must follow the writing-direction rules in part 10.

1. Emergency Public Works.
2. Rescue Strategic Industry.
3. Stabilize Finance and Trade.
4. Austerity and Retrenchment.
5. Direct State Planning.
6. Let the Market Clear.

The doctrine choice should be made after the opening shock has shown the country's material problems. It cannot be a free click before the player sees the crisis.

### Doctrine switching

A country may reconsider its doctrine through a Cabinet Review action after a meaningful cooldown. Switching doctrine should:

- Consume political and administrative capacity.
- Pause some ongoing doctrine-specific projects.
- Add short policy-whiplash pressure.
- Preserve completed state work.
- Block immediate repeated switching.
- Become unavailable during the maximum-Severity emergency unless an emergency government outcome explicitly changes policy.

A reasonable initial cooldown target is `90` to `120` days. The action should use no more than four spendable costs. Political power may be one cost because the action represents a major cabinet change. It should not be the only cost.

The country can finish the crisis under a doctrine different from the one chosen at the opening. The history ledger records the opening doctrine, final doctrine, number of switches, and major route actions. This affects recovery legacy and achievements.

## Shared action families

Several action families exist across doctrines. Their effects and costs vary by route.

### Select a Depression Center

A human player can select one active center for state-targeted actions. The selected-center flow should use a compact show and hide pattern instead of displaying every state action for every center at once.

Selection requirements:

- The state is in the country's current Event 35 center registry.
- The country controls it or has a valid recovery claim under the transfer contract.
- The state is not already resolved.
- The planned action is valid for its local stage.

AI evaluates all valid centers directly and does not need the player selector.

### Emergency Relief Allocation

Represents temporary household relief, food distribution, local administration, and basic employment support. It slows demand and social deterioration while consuming civilian capacity, equipment, manpower, or stability.

It should be useful in every doctrine, but its cost and strength depend on policy. A public-works government can integrate relief into employment. An austerity government pays a higher political or stability cost. A market-clear government uses it only as an emergency floor.

This is a stabilizer, not a complete recovery route.

### Protect a Depression Center

Commits resources to keep one center connected to power, rail, fuel, orders, and basic credit.

Possible costs include:

- Civilian factory commitment.
- Trains or trucks.
- Support equipment.
- Fuel.
- Temporary output sacrifice.

The action uses no more than four spendable cost types. It gives a state protection receipt, slows local stage deterioration, and supports the national Severity trend. It does not grant free factory levels.

### Reopen or Restructure a Center

Available during Depression or Stabilization after the center's immediate emergency is controlled. The exact route depends on doctrine and local history.

Possible results include:

- Reopening existing factories.
- Converting an unfinished project into useful infrastructure.
- Consolidating several failed plants into one protected network.
- Replacing a local depression modifier with a recovery modifier.
- Accepting bounded liquidation and a long-term scar.

A center cannot be reopened through one instant purchase. It requires a timed project or mission.

### Request Foreign Support

Available only when a valid partner, route, and relationship exist. It may provide credit, equipment, convoys, fuel, industrial orders, or public works support.

The receiving country accepts a cost or dependency consequence. The provider pays real resources or industrial commitment. No aid is created from an invalid or nonexistent partner.

Evolution I and III expand this family.

### Emergency Policy Review

Appears when the current doctrine has become materially impossible. It can open an emergency doctrine switch, scaled retreat, or coalition policy. It should never become a free escape from route costs.

## Doctrine 1: Emergency Public Works

### Route identity

The government uses public construction and employment to restore demand, freight, and confidence. The route trades current civilian capacity, logistics, and equipment for steady Severity reduction and durable infrastructure.

It is strongest when:

- The country has usable civilian factories.
- Depression Centers have repairable infrastructure or railways.
- Unemployment and demand stress are major causes.
- Stability is threatened by prolonged idleness.
- The country can protect project sites.

It is weaker when:

- Core territory is being overrun.
- The country lacks trains, equipment, or construction capacity.
- Blockade prevents material supply.
- A short military emergency requires immediate armament output.

### Primary actions

#### Launch a Regional Works Program

Starts a state-targeted project in the selected Depression Center. The project should address an identified need such as rail repair, infrastructure, a port connection, anti-air protection, housing support represented through state recovery, or conversion of abandoned works.

The decision commits civilian factories and up to three additional material costs. Project duration scales with state damage, Severity, infrastructure, war state, and earlier failures.

Success:

- Lowers demand and employment stress.
- Improves the state recovery stage.
- Adds a bounded map improvement when the project corresponds to real damaged or missing infrastructure.
- Creates progress toward the public-works recovery legacy.

Failure or interruption:

- Leaves an unfinished works burden.
- Returns part of unspent resources when proof exists.
- Raises local frustration and Severity.
- Can be resumed at a reduced or increased cost depending on why it failed.

#### National Employment Guarantee

Starts a timed country objective that commits a larger share of civilian capacity to employment and relief. It lowers demand and social pressure while active. Its long duration can create fiscal stress if maintained without recovering production.

The player must keep a minimum usable civilian base and avoid losing too many project states. The objective can succeed, partially succeed, or fail.

#### Convert Works into Lasting Capacity

Available during Stabilization. It selects completed projects that can become ordinary infrastructure, railway capacity, or a long-duration state recovery modifier. It closes temporary relief administration and prevents the route from keeping permanent emergency costs after recovery.

### Route tradeoff

Public works can overextend the state. Too many simultaneous projects increase fiscal and logistics stress. The route should normally cap active major projects at one, with a second allowed only for a large economy under favorable conditions.

## Doctrine 2: Rescue Strategic Industry

### Route identity

The government protects military production, resource processing, transport nodes, and a small number of industrial regions. It preserves essential output at the cost of civilian capacity, regional equality, and possible long-term rescue dependence.

It is strongest when:

- The country is at war.
- One or two regions carry most military production.
- Military demand is still usable.
- The country has resources and logistics to keep protected plants running.

It is weaker when:

- The crisis is mainly household demand and finance.
- Protected plants have no fuel, resources, or transport.
- Stability is collapsing because civilian regions are abandoned.
- The country has too little industry to divide into strategic and nonstrategic sectors.

### Primary actions

#### Designate a Strategic Plant Network

Marks one Depression Center as a strategic rescue priority. The state receives protection against local output collapse and shuttering. The country commits civilian factories, resources, logistics, or output from other sectors.

The action cannot protect every center. Normal capacity is one protected network. A very large major may support two at a sharply rising cost.

#### Guarantee Essential Orders

Uses military procurement or another exact national demand source to keep selected plants active. It protects production efficiency and employment in the center. It raises fiscal stress and may worsen civilian shortages.

The decision should not grant military equipment for free. It preserves or improves the ability to produce equipment that the country can already support.

#### Consolidate Failing Industry

Combines or restructures failing plants. It can prevent random physical loss, but may accept one bounded factory closure, a temporary output penalty, or a regional scar in exchange for lower Severity and a more stable center.

### Route tradeoff

A country can recover aggregate output while leaving unemployment and resentment outside protected regions. High rescue concentration feeds Evolution II social strain and creates a mixed recovery legacy.

## Doctrine 3: Stabilize Finance and Trade

### Route identity

The government restores confidence, reopens viable institutions, protects trade credit, and preserves imports. It reduces volatility and international exposure while committing reserves, shipping, civilian capacity, and diplomatic flexibility.

It is strongest when:

- Banking and trade pressure are major causes.
- Ports and convoys remain usable.
- The country has foreign partners.
- Evolution I exposure is active.
- The state can distinguish viable institutions from failed ones.

It is weaker when:

- The country is blockaded.
- Core industry is physically destroyed.
- No valid partner or route exists.
- The government lacks confidence or administrative capacity.

### Primary actions

#### Declare a Temporary Bank Holiday and Audit

Briefly restricts ordinary financial activity while the state evaluates institutions. It applies a small immediate output cost, stops the fastest credit deterioration, and starts an audit mission.

Success reopens viable institutions, lowers credit stress, and enables stronger finance actions. Failure or premature reopening creates a renewed panic.

#### Recapitalize Viable Institutions

Commits civilian capacity, political authority, and possibly a foreign credit source. It lowers credit stress and reduces future bank-panic risk. Repeated use without reform creates rescue dependence and fiscal pressure.

#### Negotiate Clearing and Import Agreements

Targets a valid partner or group of partners. It uses convoys, fuel, civilian factories, diplomatic conditions, or reciprocal commitments. It reduces trade stress and can open an aid or supplier relationship.

#### Establish a Durable Credit Guarantee

Available during Stabilization after successful audit and recapitalization. It creates the finance-route recovery institution and closes temporary emergency support.

### Route tradeoff

Guarantees can become expensive. Foreign credit can create dependency. A country that protects finance while leaving factories and employment unrepaired may stabilize the meter without completing state recovery.

## Doctrine 4: Austerity and Retrenchment

### Route identity

The government cuts commitments, narrows relief, restructures debt, and attempts to restore fiscal credibility. It can lower fiscal and credit pressure quickly while worsening unemployment, demand, and political strain.

The route must be viable under some conditions. It is not written as an automatic failure or moral lesson.

It is strongest when:

- Fiscal stress is the main cause.
- Stability and institutions are strong.
- The country has reserves or external demand that can absorb cuts.
- Severity has already left the deepest bands.
- The player accepts a slower and harsher social recovery.

It is weakest when:

- Demand collapse and unemployment dominate.
- Evolution II social strain is already high.
- Stability is low.
- Several centers are shuttered.
- The country is in a severe postwar contraction.

### Primary actions

#### Balance the Emergency Budget

Cuts or suspends selected emergency commitments. It reduces fiscal stress and some civilian burden. It raises demand and social pressure for a defined period.

#### Restructure Public Obligations

Begins a debt standstill, negotiated restructuring, or domestic conversion. It can provide a strong one-time reduction in fiscal and credit pressure. It costs diplomatic flexibility, confidence, or access to future foreign support.

#### Retrench the Relief Administration

Ends selected temporary programs. It frees civilian capacity and can support the final recovery proof if unemployment and centers are already controlled. Used too early, it causes relapse.

#### Restore Ordinary Budget Rules

Stabilization action that converts emergency austerity into a bounded long-term institution. It removes the route's temporary policy burden and defines its recovery legacy.

### Route tradeoff

Austerity can produce a clean fiscal result with a damaged labor market. It carries the strongest risk of Social Collapse when used at high Severity or low stability.

## Doctrine 5: Direct State Planning

### Route identity

The government places finance, transport, production, and distribution under coordinated public control. It reduces volatility and protects essential output while consuming political legitimacy, administrative capacity, and trade flexibility.

It is strongest when:

- The country has administrative capacity.
- Several sectors must be coordinated at once.
- Trade access is weak and domestic allocation matters.
- Strategic industry and public works need a common plan.
- The government has political support for intervention.

It is weaker when:

- The state is fragmented.
- Corruption or low stability blocks execution.
- The economy depends on flexible foreign trade.
- Planning targets are repeatedly missed.

### Primary actions

#### Establish an Emergency Production Board

Creates the route's central institution. It permits state allocation actions and lowers volatility. It adds administrative and political costs.

#### Nationalize or Place Failing Industry under Trusteeship

Targets one center. It prevents immediate shuttering and allows planned reopening. It can create a compensation, resistance, or efficiency cost depending on ideology and current law.

#### Ration Strategic Inputs

Directs fuel, transport, resources, or civilian capacity toward identified priorities. It protects selected output and raises civilian or trade pressure elsewhere.

#### Complete the National Recovery Plan

A stabilization mission that requires functioning centers, controlled Severity, and completed planning targets. Success creates a bounded planning institution. Failure extends emergency controls and policy fatigue.

### Route tradeoff

Planning can solve coordination while weakening ordinary flexibility. Poor execution raises corruption, policy fatigue, and Social Collapse risk. The route should not be a universal best choice for every ideology or economy.

## Doctrine 6: Let the Market Clear

### Route identity

The government accepts closures, asset repricing, contract failure, and short-term contraction in the belief that a smaller viable economy will recover without a permanent emergency state. It has the lowest direct state cost and the highest short-term risk.

It is strongest when:

- Stability and institutions are strong.
- The country has private reserves and functioning courts or commercial administration.
- Severity is moderate or falling.
- Failing centers contain obsolete or duplicated capacity.
- The country can tolerate a short output loss.

It is weakest when:

- Severity is near maximum.
- Evolution II social strain is high.
- The country is at war and needs immediate output.
- A single center carries most national industry.
- Households and banks lack any safety floor.

### Primary actions

#### Withdraw Emergency Support

Ends selected subsidies or guarantees and increases short-term closure risk. It reduces fiscal pressure and future rescue dependence.

#### Auction or Reorganize Failed Assets

Targets a distressed center. It can reopen part of the state under new ownership, liquidate one bounded factory level, or leave an unresolved local burden. The outcome depends on credit, stability, demand, and center condition.

#### Remove Emergency Controls

Restores ordinary price, trade, or production discretion. It can improve future efficiency when the economy is ready. Used early, it raises volatility and Severity.

#### Certify the Cleared Economy

Stabilization action that proves failed obligations and plants have been resolved. It creates a lean recovery legacy and closes temporary liquidation mechanics.

### Route tradeoff

The route can recover without large state commitments. It can also turn a recoverable depression into Economic Paralysis. A country that uses it successfully should still carry visible regional or concentration consequences when major closures occurred.

## Main missions

### Halt the Panic

Opening mission during Panic and Contraction.

Goal:

- Prevent Severity from entering or remaining in Economic Paralysis.
- Resolve at least one dominant opening cause.
- Keep at least one Depression Center operating or protected.

Duration target: `70` to `100` days, scaled by opening conditions.

Success:

- Ends the strongest opening shock on schedule.
- Grants temporary stabilization momentum.
- Advances the country into the sustained Depression phase.

Failure:

- Adds one guarded shock.
- Worsens one valid center.
- Extends opening penalties for a bounded period.

### Keep Essential Freight Moving

Appears when rail, port, convoy, fuel, or train disruption is a top cause.

Goal:

- Restore a named transport condition.
- Maintain minimum logistics reserves.
- Protect the selected center's connection.

Success lowers industrial and trade pressure. Failure adds a freight-collapse shock and can interrupt state projects.

### Reopen a Depression Center

State-targeted mission available after protection or restructuring begins.

Duration target: `90` to `180` days.

Goal varies by doctrine. It may require construction commitment, stable supply, bank audit completion, protected military orders, trusteeship, or completed liquidation.

Success advances the center to reopened or resolved status. Failure preserves part of completed work and creates a route-specific setback.

### Prevent a Relapse

Stabilization mission.

Goal:

- Keep Severity below the relapse threshold.
- Maintain required center status.
- Avoid an unresolved major shock.
- Complete doctrine consolidation.

Duration target: about `90` days.

Success advances the final recovery proof. Failure returns the country to Depression without repeating the original opening event.

### Maximum-Severity emergency

Replaces ordinary missions at Economic Paralysis. The exact route reflects doctrine and current causes. It must remain payable by a crippled country through scaled costs, foreign aid, reserve use, or temporary sacrifice.

### Prevent National Breakdown

Baseline political emergency that appears after the National Breakdown warning and before a possible civil conflict.

Goal:

- Lower Severity out of the near-paralysis range.
- Resolve the active cabinet, legitimacy, or emergency-government crisis.
- Restore, protect, or credibly restructure at least one Depression Center.
- Complete one viable employment, finance, supply, or settlement action.

Duration target: `120` to `180` days, shortened only by an immediate constitutional or military crisis.

Success:

- Clears the warning.
- Blocks another baseline breakdown check for a substantial cooldown.
- Preserves the active depression and recovery work.

Failure:

- Calls the strict baseline political-outcome validator.
- Can cause a government fall, emergency rule, policy reversal, prolonged unrest, or rare civil conflict.
- Does not create a war when no coherent actor, territory, force package, or political base exists.

When Evolution II is active, its strike, mandate, coup, separatist, or civil-conflict missions replace this baseline objective. Both systems cannot run at the same time.

### Evolution missions

Evolution I, II, and III add specialized missions described in their own parts. These missions share the same active objective cap. Evolution content must replace lower-priority baseline actions and must not create a wall of new decisions.

## Cost design

Each decision uses no more than four spendable cost types. Conditions such as controlling a state or having a valid partner do not count as spendable costs.

Preferred cost families:

- Civilian factory commitment.
- Temporary military output sacrifice.
- Trains.
- Trucks.
- Convoys.
- Support equipment.
- Fuel.
- Manpower.
- Stability.
- War support.
- Political power for genuine cabinet or legal actions.
- Time and mission risk.

Costs scale from usable capacity. A country at high Severity cannot be charged against factories that the event has already made unavailable.

The UI must show the exact player-facing costs with matching texticons. Dynamic requirements receive concise custom tooltips.

## Decision visibility by phase

| Action family | Panic and Contraction | Depression | Stabilization | Recovery proof | Economic Paralysis |
| --- | --- | --- | --- | --- | --- |
| Choose doctrine | Once | Hidden | Hidden | Hidden | Hidden |
| Cabinet Review | Conditional | Available after cooldown | Conditional | Hidden | Emergency only |
| Emergency Relief | Available | Conditional | Hidden or reduced | Hidden | Emergency form |
| Protect Center | Available | Available | Complete existing only | Hidden | Emergency form |
| Doctrine primary action | Available | Available | Consolidation form | Hidden | Replaced by emergency action |
| Reopen Center | Hidden | Available after prerequisites | Available | Complete existing only | Hidden |
| Foreign Support | Conditional | Conditional | Conditional | Hidden | Emergency form |
| Halt the Panic | Active mission | Hidden | Hidden | Hidden | Hidden |
| Prevent a Relapse | Hidden | Hidden | Active mission | Can continue | Hidden |
| Maximum emergency | Hidden | Hidden | Hidden | Hidden | Active mission |

## AI equivalents

AI countries use the same costs, consequences, cooldowns, and state records. They do not receive free Severity reduction.

AI decision scoring considers:

- Severity band and trend.
- Dominant causes.
- Usable civilian and military factories.
- War state and military urgency.
- Trains, trucks, convoys, fuel, and equipment floors.
- Stability and social strain.
- Number and value of centers.
- Current doctrine and switch history.
- Expected recovery time.
- Evolution exposure.
- Foreign aid availability.
- Long-term legacy and short-term survival.

The named AI scenarios and expected orderings are defined in part 9 and the probability matrix.

## Cleanup

When the crisis ends or the country becomes invalid:

- Hide and cancel ordinary decisions.
- Cancel missions and resolve any committed-resource refund contract.
- Clear the selected-center pointer.
- Remove temporary doctrine and emergency modifiers.
- Preserve completed state receipts and recovery history.
- Remove invalid foreign targets.
- Keep only the bounded recovery legacy and scars.

No decision may remain clickable after its target state, partner, doctrine, or crisis episode is gone.


---

<!-- Source: 035_great_depression_spec_part_4_centers_recovery_repeatability.md -->

# Great Depression 2.0 specification, part 4: Depression Centers, recovery outcomes, and repeatability

## State-level purpose

Event 35 needs visible local consequences without turning the player into the manager of every state. A small sparse set of `Depression Centers` represents the industrial regions where closures, unemployment, abandoned projects, freight failure, and recovery work are concentrated.

The national Severity value remains the main mechanic. Centers provide concrete state targets, explain important causes, and preserve history after the national category closes.

## Center count

Initial count targets:

- Small economy: one center.
- Medium economy: one or two centers.
- Large major: two or three centers.
- Evolution III inherited corridor: a fourth center only when several distinct high-value regions must be represented.

Three is the normal visible cap. The implementation can keep additional inherited state receipts internally when needed, but it should summarize them instead of exposing a long state list.

## Center selection score

A state is a strong candidate when it is:

- A core state.
- Controlled by the target country.
- Populated.
- Important for civilian or military industry.
- A major resource-processing, railway, port, or supply location.
- An Event 34 Industrial Region.
- The site of an unfinished or fragile boom project.
- Recently damaged in a way that affects national production.

A state receives lower or zero weight when it is:

- Impassable.
- Empty or nearly empty.
- A remote holding with little national economic connection.
- Already selected.
- Under a stronger owner system that forbids conversion.
- Temporarily controlled without a valid recovery claim.

The selector should avoid choosing only the capital when another state carries more industrial weight. It should also avoid choosing three adjacent states that represent one economic region unless an inherited Event 34 corridor makes that concentration meaningful.

## Event 34 conversion priority

When the crisis comes from Event 34, the state registry is not rerolled from scratch.

Priority order:

1. Fragile Miracle Regions.
2. Unfinished or abandoned boom projects.
3. High-value Industrial Regions with failed protection.
4. Runaway Industrialization corridor states.
5. Other high-value industrial states when the inherited registry does not fill the normal center count.

Each inherited state carries its boom history into the local opening condition.

## Local depression stage

Every center has one local depression stage. The exact numeric implementation may remain hidden, but the player sees a named state condition.

| Local stage | Working condition | Meaning |
| ---: | --- | --- |
| `0` | Reopened | Ordinary production and employment have resumed |
| `1` | Distressed | Closures and unemployment are growing, but the center still operates |
| `2` | Idled | A large share of capacity is inactive and freight or credit support is failing |
| `3` | Shuttered | Most supported activity has stopped and reopening requires a major project |
| `4` | Abandoned or Liquidated | Capacity has been deliberately or physically lost and the state needs long reconstruction |

A center can also carry one temporary treatment or protection state, such as protected, under public works, under trusteeship, guaranteed orders, audited finance, or asset liquidation. Treatment is distinct from local stage.

The design should prefer one local dynamic modifier whose strength reads the stage, plus limited treatment modifiers. It should avoid a stack of unrelated state modifiers.

## Opening local conditions

### Independent firing

An independent center normally begins Distressed or Idled. The opening may begin one center at Shuttered only when the target already has severe industrial damage, blockade, or a registered economic shock.

### Event 34 inherited firing

- Completed and protected boom project: Distressed with a strong reopening opportunity.
- Completed but fragile Miracle Region: Idled or Shuttered with high national pressure.
- Unfinished project: Idled with an abandoned-works burden.
- Failed speculative project: Shuttered with credit and unemployment pressure.
- Lost or heavily damaged Industrial Region: Shuttered and disconnected.
- Evolution III corridor state: stage depends on network fragility, protection, and current control.

The inherited path should create a recognizable reversal of the boom. It must not delete the Event 34 state history before Event 35 records the conversion.

## Local progression

A center worsens through sustained national and local pressure. It does not advance one stage every pulse.

Progression factors include:

- Severity band and duration.
- State damage.
- Infrastructure, rail, port, and supply condition.
- Factory concentration.
- Current control.
- Active treatment.
- Doctrine.
- War demand and bombing.
- Local famine or migration pressure from a valid shared context.
- Failed missions.
- Evolution II unrest.

A stage change requires a progress threshold, warning state, or failed objective. The player should see that a center is at risk before normal drift causes a serious closure.

## Physical factory and building loss

The event's baseline identity is economic paralysis. Physical loss is a later consequence.

Rules:

- No factory deletion on the opening day.
- No recurring random deletion while Severity remains high.
- A state must be Shuttered or Abandoned, remain there for a sustained period, and fail a recovery or protection opportunity before involuntary factory loss is eligible.
- Each center has a strict per-episode physical-loss cap.
- A state retains minimum viable capacity where possible.
- Deliberate liquidation is recorded separately from involuntary loss.
- Existing building damage from bombing or disaster is not counted again as Event 35 deletion.
- Building slots are never removed through an unsupported substitute.

A bounded loss may affect one civilian factory, one military factory, infrastructure, or another fitting building based on the state's actual economy and the cause. The implementation should prefer temporary shutdown and damage before permanent level removal.

## Center treatment by doctrine

### Public Works treatment

- Creates employment and construction activity.
- Repairs infrastructure or rail when there is real damage or missing capacity.
- Slows local deterioration.
- Can leave a useful map improvement after recovery.
- Creates unfinished-works risk when interrupted.

### Strategic Industry treatment

- Protects essential factories and production efficiency.
- Requires resources, logistics, and orders.
- Can leave nonstrategic local employment unresolved.
- Creates rescue dependence when kept too long.

### Finance and Trade treatment

- Restores credit and commercial connections.
- Requires an audit, viable institutions, and trade or fiscal support.
- Is less effective when the state is physically destroyed or cut off.

### Austerity treatment

- Cuts subsidies and may close unviable plants.
- Reduces fiscal stress.
- Raises short-term unemployment and social strain.
- Can produce a lean but scarred center.

### Direct Planning treatment

- Places plants under trusteeship, nationalization, or allocation control.
- Protects essential capacity.
- Requires administration and political support.
- Can create long-term efficiency or legitimacy costs.

### Market-Clear treatment

- Allows failure, auction, merger, or liquidation.
- Uses the least direct public capacity.
- Can reopen a smaller viable center.
- Carries the highest risk of permanent factory loss and concentrated ownership.

## Center reopening

Reopening requires more than low national Severity.

A center normally needs:

- Control by the crisis country or a valid successor.
- A completed doctrine-specific project.
- Restored basic transport and supply.
- No unresolved local emergency.
- National Severity below a route-appropriate threshold.
- A successful reopening mission.

A center can be resolved without returning to its exact starting structure. Reopened, restructured, liquidated, or converted outcomes are all valid. The final recovery result distinguishes them.

## Local incidents

Incidents should be sparse and tied to real state conditions.

Baseline incident families:

- Factory gate closures.
- Unpaid wages.
- Freight yards standing idle.
- Local credit cooperatives or emergency finance.
- Municipal relief failure.
- A successful reopening shift.
- Skilled workers leaving the region.
- A contractor or owner abandoning unfinished works.
- A regional authority requesting national aid.
- War orders temporarily reviving one center.

Evolution II adds organized social and political incidents. Incidents should mention the exact state and current treatment. They must not fire for a center that no longer exists or is no longer relevant.

## State control changes

### Temporary loss of control

- Pause active projects.
- Stop country payments for the lost state.
- Preserve completed project receipts.
- Add a national shock based on the state's real industrial importance.
- Allow the new controller to receive a temporary local burden when it uses normal civilian systems.

### Regaining control

- Reconcile the center's current buildings and modifiers.
- Resume or redesign a paused project.
- Do not restore buildings lost through combat or occupation for free.
- Apply a reopening cost based on current state condition.

### Permanent transfer

The original country retains historical loss and national shock records, but stops owning the live center. The new owner can adopt the center into its own Event 35 crisis or manage the local burden through a limited state action. One state cannot be registered as an active center for two countries at once.

## Civil war transfer

A civil war can split Depression Centers between participants. The transfer follows state control and economic continuity.

Rules:

- One side retains the original national episode ID and Severity history.
- A second side receives only the local center burdens it controls, plus a derived crisis condition when its economy is large enough.
- The event cannot clone the full national decision category onto every minor participant.
- Treatment and project receipts move with the state.
- National doctrine does not automatically transfer to an opposing government.
- Evolution II political origins are recorded for later aftermath.

## Recovery proof and center requirement

The national crisis cannot close while a required center is Shuttered without a deliberate resolution. The player must reopen, restructure, liquidate, abandon, or permanently lose it under the state contract.

Strong recovery normally requires every center Reopened or successfully restructured.

Uneven recovery may allow one mixed or scarred center.

Hollow recovery may allow deliberate liquidation or abandonment, with the corresponding permanent cost.

## Recovery legacy budget

A completed episode may leave:

- One main country recovery institution or legacy.
- Up to two meaningful state recovery or scar modifiers under normal conditions.
- Temporary post-recovery safeguard and rebuilding effects.

It should not leave a large stack of small national spirits.

### Public Works legacy

Possible direction:

- Stronger infrastructure maintenance.
- Better construction mobilization during future crises.
- Reduced starting demand stress in a later Event 35 episode.

Cost or limitation:

- A temporary fiscal or consumer burden.
- Maintenance needs for the new works.

### Strategic Industry legacy

Possible direction:

- Better protection of key production regions.
- Faster recovery of production efficiency after an industrial shock.

Cost or limitation:

- Regional inequality.
- Rescue dependence or civilian-sector weakness.

### Finance and Trade legacy

Possible direction:

- Lower future banking-panic risk.
- Better resistance to Evolution I exposure.
- Stronger clearing or trade support actions.

Cost or limitation:

- Foreign dependency or regulatory burden.

### Austerity legacy

Possible direction:

- Lower fiscal stress in a later episode.
- Cheaper maintenance of ordinary government programs.

Cost or limitation:

- Higher social strain after unemployment shocks.
- Weaker relief capacity.

### Direct Planning legacy

Possible direction:

- Better coordination of essential production and logistics.
- Stronger emergency allocation.

Cost or limitation:

- Lower ordinary flexibility.
- Political or administrative burden.

### Market-Clear legacy

Possible direction:

- Lower future rescue dependence.
- Faster reopening of viable private capacity under stable conditions.

Cost or limitation:

- Concentrated ownership.
- Reduced regional capacity or stronger unemployment scars.

## Recovery scars

Scars are used only when the episode created lasting damage.

Possible state scars:

- Hollowed Industrial District.
- Long-Term Unemployment.
- Abandoned Works.
- Rescue-Dependent Industry.
- Concentrated Ownership.
- Broken Freight Connection.

Possible country scars:

- Debt Overhang.
- Policy Fatigue.
- Emergency Controls.
- Labor Bitterness.
- Foreign Credit Dependence.

A scar needs a real source receipt and a future mitigation path where appropriate. It cannot be added because the event simply lasted a long time without a specific consequence.

## Repeat episode memory

Each country stores a compact Event 35 history:

- Episode count.
- Highest Severity reached.
- Entry source.
- Opening and final doctrine.
- Number of doctrine changes.
- Strong, uneven, or hollow recovery result.
- Centers reopened, restructured, liquidated, lost, or abandoned.
- Evolution stages experienced.
- Contagion sent or received.
- Social-collapse outcome.
- Evolution III participation.
- Event 34 collapse count.
- Retained legacy and scars.

The event does not need to preserve every weekly calculation after recovery.

## Repeat target suppression

After recovery, the country receives a safeguard period. Independent target weight remains low during this period. It rises gradually after the safeguard ends.

A consequence path can bypass the safeguard when:

- Event 34 collapses in the same country.
- A valid contagion source converts the country.
- Evolution III pressure crosses the local conversion threshold.

Bypassing independent target suppression does not erase the prior episode. It starts or deepens a new consequence episode with its source recorded.

## Strong reforms and future resistance

A successful recovery can make a later episode easier.

Examples:

- Finance reform lowers initial credit stress.
- Public works improve infrastructure and project speed.
- Strategic rescue protects one center automatically at the next opening.
- Planning improves emergency allocation.
- Austerity reduces initial fiscal stress.
- Market restructuring reduces rescue dependence.

Each reform has a countervailing weakness or limited scope. No route grants permanent immunity.

## Repeated failures

Repeated hollow recovery, Event 34 collapse, or center abandonment can make a later opening worse. The increase is bounded. A country should never become permanently unable to recover because it experienced the event several times.

Anti-death-spiral rules:

- Starting Severity has a cap below Economic Paralysis for ordinary independent firing.
- At least one viable center is selected when the country has one.
- Emergency costs scale down with usable capacity.
- Permanent factory losses have per-state and per-episode caps.
- Strong reforms can offset prior scars.
- A small economy is not asked to support large-major project counts.

## Exploit controls

### Factory-loss farming

A player cannot deliberately lose one cheap factory to gain a stronger permanent legacy. Recovery legacy is based on completed policy and state work. Liquidation reduces the legacy budget and adds scars.

### Building-slot farming

Event 35 does not create free building slots. Public works can add or repair real buildings under a strict project budget. Repeat episodes use diminishing state returns.

### Transfer farming

Transferring a center cannot reset its project, recreate costs, or duplicate its recovery reward. State receipts move with the state and retain the episode ID.

### Aid farming

Foreign aid consumes real provider resources and uses source-target cooldowns. The same package cannot be claimed twice through faction, subject, and bilateral paths.

### Doctrine-switch farming

Switching has a cooldown and policy-whiplash cost. Completed doctrine actions cannot be repeated merely by leaving and returning to the doctrine.

### Maximum-Severity farming

Reaching `100` cannot repeatedly grant emergency aid or trigger the same factory loss. The maximum emergency uses one-shot receipts and cooldowns.

## Cleanup after recovery

After the recovery result is frozen:

1. Cancel active state projects that cannot continue.
2. Resolve refundable commitments through exact receipts.
3. Remove temporary center treatments.
4. Convert state stages into reopened, mixed, or scar outcomes.
5. Apply the bounded national legacy.
6. Clear active arrays and selected-state pointers.
7. Preserve compact history and state receipts.
8. Start the post-recovery safeguard.

No active Event 35 state modifier, mission, or decision should remain without a documented post-recovery purpose.


---

<!-- Source: 035_great_depression_spec_part_5_financial_contagion.md -->

# Great Depression 2.0 specification, part 5: Evolution I, Financial Contagion

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

Financial Contagion turns one national depression into an international economic risk. It adds a sparse relationship network, lighter secondary-country pressure, foreign intervention, supplier opportunities, and the possibility that another country develops a full Event 35 crisis.

The evolution does not give every related country the full decision category. Most secondary countries receive a compact Economic Contagion condition and a small action set. Full Event 35 activation requires sustained exposure plus local vulnerability.

## Availability and activation

Financial Contagion becomes available at Rising Chaos.

Normal active-event activation should require:

- Event 35 is active in a valid origin country.
- Evolution I is enabled in Event Details.
- The origin has meaningful external relationships.
- Severity or one hidden external component is high enough to create an international risk.
- The evolution has not already been recorded for this episode.
- The dynamic evolution delay has elapsed.

A base timing target near `90` days is appropriate under strong conditions. Lower Severity, secure trade, successful finance policy, weak international links, and coordinated aid should slow activation. Deep Depression, failed finance missions, large external exposure, and an Event 34 speculative collapse should accelerate it.

An Event 34 Evolution I collapse activates the enabled Financial Contagion module immediately when Event 35 begins. It still records the Event 35 evolution context once. The Event 34 evolution log is not reused as the Event 35 log.

Evolution activation itself adds zero Chaos. Chaos changes belong to concrete spread outcomes described later.

## Evolution logging

The evolution record uses:

- Parent event ID `35`.
- Evolution type for Financial Contagion.
- Evolution stage `1`.
- Display tier Rising Chaos.
- Origin country as actor.
- Current crisis episode ID in the Event 35 ledger.

The event-detail preview explains international financial exposure, aid, market retreat, and possible spread. It must not state that a specific country will be infected before a valid relationship and pressure exist.

## Exposure network

The network is built from relationships the game can prove. It must not claim exact bilateral trade volume when script cannot observe it.

### Strong exposure links

- Subject to overlord.
- Overlord to subject.
- Shared economic market when the relevant system and DLC are present.
- Explicit Event 35 credit, clearing, rescue, supplier, or reconstruction agreement.
- A country that has provided a large Event 34 or Event 35 industrial support package.
- A creditor or debtor link created by an Event 35 decision.

### Medium exposure links

- Faction membership.
- Direct land adjacency with substantial normal economic contact.
- Guarantee or close alliance with an active aid relationship.
- Shared war economy with an exact equipment, convoy, or industrial-support transaction.
- A major port or clearing partner created by the event.

### Light exposure links

- High opinion and a valid commercial relationship.
- Regional proximity.
- Common dependence on an explicit distressed supplier.
- A one-time distressed-asset transaction.

A light link alone should rarely cause a full crisis. It can add a minor condition, open a decision, or combine with other links.

## Sparse registry

The evolution should maintain a sparse list of exposed countries for each origin episode.

Each row records:

- Origin episode ID.
- Origin country.
- Exposed country.
- Relationship type.
- Current exposure stage.
- Peak exposure stage.
- Last material source.
- Aid or abandonment state.
- Full-crisis conversion receipt.
- Propagation depth.
- Cooldown and cleanup state.

The registry should be built from bounded candidate scopes when the evolution activates and when an event-owned relationship changes. It must not create a new recurring whole-world scan.

## Economic Contagion condition

Secondary countries see one qualitative condition. It is not a new public numerical meter.

| Exposure stage | Working condition | Effect direction | Available response |
| ---: | --- | --- | --- |
| `1` | Exposed Markets | Small confidence and trade pressure | Monitor or reduce exposure |
| `2` | Credit Strain | Lending and construction begin to weaken | Ring-fence finance or support partner |
| `3` | Contracting Economy | Output, construction, and stability pressure become material | Strong intervention, retreat, or aid |
| `4` | Near Depression | Local conditions can convert into full Event 35 | Emergency containment mission |

The exact effects scale with the exposed country's vulnerability. A small subject tied to one market may suffer more than a diversified major at the same qualitative stage.

## Exposure pressure

Exposure rises through:

- Origin Severity and trend.
- Origin bank panic or trade-credit failure.
- Strong relationship type.
- Failed foreign aid.
- Abandonment of a distressed partner.
- Shared dependence on a failed supplier or debtor.
- Evolution III world pressure.
- A boom supplier that accepts excessive distressed demand and later fails.
- Currency, debt, or clearing incidents created by this evolution.

Exposure falls through:

- Origin recovery.
- Ring-fencing domestic institutions.
- A successful coordinated rescue.
- A clearing agreement.
- Diversification of trade or supply.
- Temporary capital controls where valid.
- Debt standstill or restructuring.
- Ending the exact relationship that created exposure, with its political and economic consequences.

## Secondary-country actions

The exposed country receives a compact decision category or a small section in an existing Event 35 category when it already has the full crisis.

### Ring-Fence Domestic Finance

Restricts the transmission of credit and banking stress. It costs administrative and civilian capacity, may reduce foreign flexibility, and lowers exposure drift.

It is strongest for countries with stable institutions. It is weaker after the country reaches Near Depression.

### Extend Emergency Credit

Supports the origin through a real resource or industrial commitment. It can lower origin Severity and the provider's future exposure. It risks larger losses if the origin continues to deteriorate.

The provider chooses the scale. Costs may include civilian factories, political authority, convoys, fuel, or another exact transfer. No more than four spendable costs are shown.

### Shift Import and Contract Dependence

Reduces exposure to the origin by finding another supplier or market. It requires a valid alternative, time, convoys, and possible output disruption. It can raise relations or dependence with the new partner.

### Abandon the Distressed Market

Cuts the strongest relationship quickly. It reduces future exposure while causing an immediate shock to the origin, diplomatic damage, and possible loss of investment or supply.

The action should be attractive when the origin is near Economic Paralysis and the exposed country has little ability to help. It should not be a free universal solution.

### Acquire Distressed Assets

Uses spare capital, industrial capacity, or a current Industrial Boom to purchase failed assets, contracts, or concessions. It gives the origin short-term relief and the buyer a bounded advantage. It can create dependency, resentment, or later political action.

### Coordinate an International Rescue

Available to a major, overlord, faction leader, or coalition of valid providers. It requires several material contributions and a timed mission. Success reduces exposure across the registered network. Failure can accelerate several countries at once.

## Origin-country actions

### Request Emergency Credit

Seeks a valid provider. The origin accepts dependency, concessions, or oversight. The provider must be able and willing to pay.

### Offer a Debt Standstill

Temporarily suspends or restructures event-created obligations. It lowers immediate credit pressure and can reduce contagion. It harms confidence, relations, or future access according to the relationship.

### Sell Distressed Assets

Raises immediate support by transferring a bounded economic interest to another country. It cannot sell the same asset twice. A state, concession, or industrial receipt must have one owner.

### Establish a Clearing Bloc

Creates a limited group of countries that keep essential exchange working through reciprocal commitments. It lowers trade pressure while reducing flexibility outside the bloc.

### Accept External Supervision

A desperate country accepts stronger foreign control over finance, trade, or reconstruction. It provides relief and can create subject pressure, influence, or an event-specific dependency. It cannot silently change autonomy without a visible consequence chain.

## Full-crisis conversion

An exposed country converts into full Event 35 only when all of the following are true:

- It uses normal civilian systems.
- It does not already have Event 35 active.
- Exposure has reached Near Depression or an equivalent severe state.
- Local vulnerability is high enough.
- A conversion delay or incident has resolved.
- No conversion receipt exists for this origin episode.
- Event 35 is enabled for the country and no conflict contract blocks activation.

Local vulnerability considers:

- Stability.
- Trade and convoy dependence.
- Industrial concentration.
- Existing damage or famine pressure.
- Strong subject, market, or creditor dependence.
- Earlier depression scars.
- Current war and blockade.
- Recovery reforms.

The new crisis records:

- Entry source Financial Contagion.
- Origin country and origin episode.
- Propagation depth.
- Starting exposure stage.
- Foreign actions already taken.
- Starting Severity based on exposure and local vulnerability.

The conversion is a consequence call. It does not consume another normal random-event pacing transaction.

## Propagation depth and anti-loop rules

A country converted through contagion can become a new source only after its own Financial Contagion evolution is valid and active. The new propagation link records its depth from the original episode.

Initial rules:

- Direct origin links have depth `1`.
- A converted country's links begin at depth `2` or greater.
- Pressure declines with each additional depth.
- No country can convert twice from the same original episode.
- The network cannot immediately send the same shock back to the country that sent it.
- A source-target pair has a cooldown after aid, abandonment, or conversion.
- A recovered country clears outgoing spread after a proof period.
- Duplicate faction, subject, and event-created links are merged into one strongest relationship row.

These rules prevent rapid ping-pong spread and repeated consequence farming.

## Industrial Boom interaction

A country with an active Event 34 Industrial Boom becomes a special potential supplier.

### Supply Depressed Markets

The boom country accepts large foreign orders. It gains stronger output demand and project opportunity. Its Overheating rises through added order, freight, labor, and credit pressure.

The depressed recipient receives lower trade, demand, or logistics stress. The transaction uses a real relationship receipt and cooldown.

### Finance Reconstruction

The boom country commits civilian capacity, convoys, fuel, equipment, or credit to a recovery project. It can create a lasting trade relationship or foreign influence. It raises Overheating more slowly than unrestricted supplier demand.

### Acquire Distressed Industry

The boom country buys assets or concessions. It receives a bounded benefit and stronger long-term exposure to the recipient. The recipient gains immediate relief but can incur dependency and Social Collapse pressure.

### Refuse the Orders

The boom country protects its Overheating and gives up the foreign opportunity. The recipient receives no new arbitrary penalty unless it had already committed to the supplier relationship.

### Boom collapse during rescue

If the supplier boom collapses:

- Event 34 hands the supplier into Event 35.
- Existing rescue agreements are frozen.
- Recipient countries receive a registered trade or credit shock.
- Evolution III world pressure can rise.
- The same failed agreement is not counted once for Event 34 and again for every Event 35 origin without separate receipts.

## Foreign aid and exploitation balance

Aid and exploitation are both supported. Neither is a free optimal path.

Aid risks:

- Provider Overheating or fiscal strain.
- Losses if the origin fails.
- Convoy and equipment burden.
- Domestic criticism.

Exploitation risks:

- Dependency and resentment.
- Evolution II political backlash.
- Exposure to the purchased market.
- Condemnation or diplomatic pressure only when another registered system supports it.

Abandonment risks:

- Origin shock.
- Lost influence and investment.
- Faction or subject strain.
- A stronger chance that the crisis spreads through another route.

## Contagion incidents

Incident families include:

- A correspondent institution fails.
- A foreign-currency obligation becomes unpayable.
- Trade credit is withdrawn.
- A bank holiday is declared in an exposed country.
- A debt conference opens.
- A rescue loan fails to arrive.
- A supplier demands concessions.
- Capital leaves one market for another.
- A clearing bloc forms.
- A coordinated rescue succeeds.
- A country abandons an exposed partner.

Every incident names the relevant countries and relationship. It should not use generic global text when only two countries are involved.

## Event and news presentation

The origin receives a report when the evolution activates and when a major foreign action changes the network. Exposed countries receive local reports only when their own pressure becomes material.

World news is reserved for:

- A major international rescue.
- The first full secondary depression from one origin.
- Collapse of a major clearing or credit network.
- A large market bloc abandoning the origin.

Routine exposure changes remain in the category and event history.

## Chaos impact

Financial Contagion activation adds zero Chaos.

Concrete one-shot outcomes may add Event 35 Chaos:

- First secondary country enters full Event 35 from one origin episode.
- A third or later country enters the same contagion chain.
- A major international rescue fails and causes several new severe exposures.
- A large clearing or credit network breaks apart.

The values should be small and guarded, for example `+1` for first spread and a larger one-time milestone for a genuine multi-country chain. Generic Chaos from war, annexation, ideology change, deaths, or world tension is not repeated.

Recovery can remove only the matching Event 35 spread pressure that was previously added. It cannot subtract Chaos for ordinary aid or one country's recovery when the wider chain remains active.

## Resolution

The origin's contagion episode enters resolution when:

- Origin Severity remains below the safe range.
- No exposed country remains at Near Depression.
- No unresolved rescue or abandonment mission remains.
- No new transmission occurs during the proof period.

Resolution:

- Stops new exposure from the origin episode.
- Decays lighter conditions.
- Preserves converted countries as independent Event 35 crises.
- Records countries aided, abandoned, exploited, or converted.
- Removes temporary foreign decisions.
- Preserves valid dependency or clearing agreements that have a post-crisis purpose.

A converted country does not recover automatically because the origin recovered.

## AI behavior

AI evaluates exposure according to:

- Own stability and Severity.
- Relationship strength.
- Faction or subject responsibility.
- Provider resources.
- War state.
- Convoys and trade access.
- Existing foreign influence.
- Origin importance.
- Expected contagion risk.
- Event 34 Overheating when the provider has an active boom.

An AI should aid a vital subject or ally when it can afford the cost. It should ring-fence or abandon an origin that is unlikely to recover and threatens its own survival. A boom AI should not accept every distressed order when Overheating is already dangerous.

Named scenarios are defined in part 9.

## Disabled evolution behavior

If Financial Contagion is disabled:

- No new exposure registry is created.
- Existing lighter exposure from a previously enabled state is retired safely.
- No full-crisis conversion can occur through this module.
- Event 34 inherited Evolution I still affects starting Severity and state conversion, but does not activate disabled contagion content.
- Baseline recovery remains fully possible.
- A higher enabled evolution does not silently recreate this module.


---

<!-- Source: 035_great_depression_spec_part_6_social_collapse.md -->

# Great Depression 2.0 specification, part 6: Evolution II, Social Collapse

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

Baseline Event 35 already permits ordinary strikes, radicalization, government crises, and a rare generic civil conflict after the National Breakdown gate. Social Collapse expands that compact failure route into a direct political and social struggle. It adds organized strikes, factory occupations, riots, defined radical movements, mutinies, emergency governments, coups, separatist pressure, and a richer civil-conflict path.

The evolution does not make civil war inevitable. Severe outcomes require long economic failure, weak institutions, an organized movement, and failed response. A country can recover economically while changing government, labor institutions, ownership, or regional relations. When this module is active, it owns the political incident ladder and suspends the simpler baseline breakdown chain so outcomes cannot duplicate.

Evolution II normally includes Financial Contagion when Evolution I is enabled. The project settings remain authoritative. A disabled lower evolution stays disabled and is not silently activated by Evolution II.

## Availability and activation

Social Collapse becomes available at Chaos Tier.

Normal active-event activation should require:

- Event 35 is active.
- Evolution II is enabled.
- The country has spent a sustained period in Depression, Deep Depression, or Systemic Breakdown.
- Social and institutional stress is material.
- The evolution has not already been recorded for the episode.
- The dynamic evolution delay has elapsed.

A base timing target near `120` days is appropriate under strong conditions.

Activation accelerators:

- Severity above `80`.
- Several Distressed, Idled, or Shuttered centers.
- Low or falling stability.
- Repeated mission failure.
- Harsh austerity or liquidation at high unemployment.
- Selective strategic rescue that abandons other regions.
- Failed relief or public works.
- Repression or exposed corruption.
- Famine or migration pressure from a valid shared context.
- An Event 34 Evolution II collapse with fragile Miracle Regions.

Activation reducers:

- Reopened centers.
- Successful employment programs.
- High stability.
- A negotiated labor settlement.
- Effective relief.
- Low Severity and improving trend.
- A government with strong institutional legitimacy.

An inherited Event 34 Evolution II collapse activates enabled Evolutions I and II immediately. Disabled lower modules remain off.

Evolution activation adds zero Chaos.

## Hidden social-strain model

The event may track `Social Strain` internally. It is not a second public number. The category shows a qualitative social condition and the strongest cause.

Suggested conditions:

- Contained Discontent.
- Organized Protest.
- National Unrest.
- Government Crisis.
- Revolutionary Breakdown.

Social Strain rises through:

- High Severity and duration.
- Unemployment in the same centers.
- Hunger, famine, or housing pressure from an exact registered source.
- Failed relief.
- Factory liquidation.
- Wage, contract, or pension failure.
- Unequal strategic rescue.
- Repression.
- Political exclusion.
- Failed government response.
- Existing radical party or movement strength.
- Regional identity where an abandoned center is concentrated.

It falls through:

- Employment and public works.
- Reopened centers.
- Negotiated settlements.
- Credible social insurance or relief.
- High stability.
- Political inclusion.
- A successful emergency government with a defined mandate.
- Recovery progress.

The implementation should rebuild the qualitative state from hidden pressure and current incidents. It should not show a raw social score.

## Movement formation

Social Collapse can create one primary organized movement and, in a large or fragmented country, one secondary rival. It should not generate many interchangeable factions.

Movement type depends on:

- Current ideology and ruling institutions.
- Existing party popularity.
- Labor organization and route history.
- Regional identity.
- Military discontent.
- Recovery doctrine.
- Foreign influence.
- Prior civil conflict.

Possible movement families:

- Trade-union and social-democratic coalition.
- Communist council movement.
- Syndicalist or factory-occupation movement.
- Nationalist or fascist mass movement.
- Military emergency faction.
- Monarchist or traditional-authority restoration group.
- Regional autonomy or separatist movement.
- Business and creditor emergency coalition.
- Rural protest movement when agricultural and famine pressure is valid.

The event should use existing parties, leaders, characters, and regional identities when they exist. It must not invent a historical person or grounded portrait merely to fill a movement role. A council or institution can represent a movement when no valid person exists.

## Incident ladder

### Stage 1: Organized protest

Possible incidents:

- Local strike committee forms.
- Unemployed workers organize a march.
- Factory owners close a plant during a wage dispute.
- Municipal relief offices are overwhelmed.
- Veterans or soldiers demand employment.
- A regional council refuses a national retrenchment order.

Gameplay:

- Small stability or production pressure.
- One visible response decision.
- A chance to negotiate before the movement hardens.

### Stage 2: Sector conflict

Possible incidents:

- Rail, mining, port, or armament strike.
- Factory occupation.
- Coordinated refusal of layoffs.
- Business lockout.
- Large relief demonstration.
- Security force refusal or sympathy.

Gameplay:

- State or sector production loss.
- Timed negotiation, relief, or enforcement objective.
- Movement support and government legitimacy consequences.

### Stage 3: National unrest

Possible incidents:

- General strike.
- Nationwide factory occupations.
- Hunger riots tied to a valid food crisis.
- Mutiny or refusal of orders.
- Emergency cabinet collapse.
- Rival movements fighting for control of relief or workplaces.

Gameplay:

- Strong national penalties.
- Emergency government or national settlement choices.
- Higher risk of coup, regional break, or civil conflict after failure.

### Stage 4: Government crisis

Possible incidents:

- Cabinet loses authority.
- Parliament or ruling council cannot pass a recovery program.
- Army leadership demands emergency powers.
- A movement establishes parallel administration in one or more centers.
- Regional authorities threaten secession.
- A foreign patron conditions aid on government change.

Gameplay:

- Leadership or government route decision.
- Strict timed objective.
- Potential ideology, law, leader, council, or autonomy change.

### Stage 5: Revolutionary breakdown

Possible outcomes:

- Coup attempt.
- Limited regional uprising.
- Separatist conflict.
- Full civil war.
- Negotiated transfer of power.
- Emergency dictatorship.
- Revolutionary coalition government.

This stage requires the full extreme-outcome gate. It is never selected from one high Severity check.

## Response families

The category shows only responses relevant to the current incident and government.

### Negotiate with Strike Committees

Commits political authority, relief, and policy concessions. It can end strikes and reduce social pressure. It may strengthen labor institutions, reduce owner confidence, or change the recovery doctrine.

### National Employment Compact

Combines public works, wage support, and industrial reopening into one national settlement. It has high civilian and fiscal costs and can create a durable social institution.

### Deploy Security Forces

Uses command power, equipment, manpower, and stability risk. Command power remains conservative and never exceeds the project limit. The action can restore control quickly, but may create deaths, radicalization, condemnation from another valid system, and longer social scars.

Any civilian loss must use the shared exact population and Deaths contracts. Event 35 must not subtract population through a duplicate path.

### Break the Occupations

Targets occupied factories or a center. It may use negotiation, legal action, police, military units, or owner concessions according to government type. A forceful solution can damage the state or production.

### Recognize Workplace or Regional Councils

Shares authority with organized local bodies. It reduces immediate strain and can move the country toward a new political settlement. It may weaken central control or alter ideology support.

### Form an Emergency Government

Creates a coalition, military cabinet, royal ministry, planning council, or other government form supported by current institutions. It grants temporary crisis authority and starts a mandate mission.

The emergency government must have a clear end condition. It can return power, become permanent through a visible route, fail, or trigger opposition.

### Nationalize or Socialize Occupied Industry

Available where politics and doctrine support it. It can resolve occupations and protect production. It changes ownership, foreign relations, and long-term institutions.

### Guarantee Property and Credit

Available to governments seeking business support. It can end lockouts and restore finance while increasing public rescue costs and labor opposition.

## Government and ideology variants

The route logic uses current institutions without turning every ideology into the same event with renamed buttons.

### Democratic and parliamentary governments

Likely tools:

- Coalition cabinet.
- Labor negotiation.
- Public works and social insurance.
- Emergency legislation with an expiry.
- Election or confidence vote.

Main risks:

- Cabinet fragmentation.
- Radical opposition.
- Permanent emergency rule.
- Foreign creditor pressure.

### Communist governments

Likely tools:

- State planning.
- Workplace councils.
- Party discipline.
- Nationalization.
- Conflict between central planners and independent labor movements.

Main risks:

- Rival council or syndicalist power.
- Purge and repression.
- Regional resistance.
- Administrative failure.

### Fascist governments

Likely tools:

- Corporatist agreements.
- Strategic rescue.
- Compulsory labor or production controls.
- Paramilitary or police response.
- Business-state bargaining.

Main risks:

- Violent repression.
- Rival radical factions.
- Military intervention.
- Collapse of corporatist promises.

### Nonaligned, monarchist, or military governments

Likely tools:

- Royal or presidential commission.
- Patronage relief.
- Military cabinet.
- Conservative labor settlement.
- Provincial bargaining.

Main risks:

- Palace or officer coup.
- Regional separatism.
- Weak party legitimacy.
- Dependence on one institution.

These are design tendencies. AI and player options must remain sensitive to the actual country, party support, characters, laws, and campaign state.

## Political transformation

A country may recover under a transformed government.

Supported outcomes include:

- Negotiated social settlement.
- Reformed parliamentary government.
- Corporate or creditor government.
- State-planning administration.
- Military emergency regime.
- Revolutionary council government.
- Restored monarchy or traditional authority where a valid route exists.
- Regional autonomy settlement.
- Fragmented or civil-war aftermath.

A transformation needs visible steps, valid leaders or institutional identities, localisation, portraits when a real character changes, AI strategy, and cleanup. The event must not perform a silent ideology swap from one incident.

## Extreme-outcome gate

A coup, separatist conflict, or civil war requires all relevant conditions:

- Social Collapse is active.
- Severity has remained very high for a sustained period.
- Social condition has reached Government Crisis or Revolutionary Breakdown.
- Stability is very low or government legitimacy has failed.
- A valid organized movement exists.
- At least one major response or mandate mission failed.
- No recent civil war or protected aftermath blocks another conflict.
- Valid states and actors exist.
- The movement can receive a coherent territory and force package.

A starting target near Severity `90` for at least `90` to `120` days is reasonable. Exact values need tuning.

## Coup design

A coup is used when the movement has elite or military support but lacks a coherent regional base.

The coup can:

- Replace the leader or cabinet.
- Change ruling party or law.
- Install an emergency national spirit with a lifecycle.
- Start a legitimacy or mandate objective.
- Fail and strengthen another movement.

A coup should not create a civil war automatically unless the country has a valid opposing base and the coup failure opens that branch.

## Separatist design

Separatism requires:

- A valid regional identity or existing tag.
- One or more Depression Centers in the region.
- Long abandonment, unequal rescue, or repression.
- Enough state control and organization to create a viable actor.

The event must use existing country-carrier and tag rules. It does not invent a new tag in the planning stage. A separatist route needs territory, capital, forces, equipment, leader or council, flag, localisation, AI, claims, diplomacy, and later settlement. If those cannot be supplied, use autonomy or regional crisis instead of a fake country.

## Civil-war design

A full civil war is the rare failure outcome.

Rules:

- Territory follows organized support, Depression Centers, regional identity, and current control.
- The split should not default to half the country.
- Starting forces and equipment scale from the states and movement.
- The original Event 35 crisis is divided through the state-transfer contract.
- Both sides receive only the economic burden they actually control.
- The war uses the shared generic Chaos and deaths systems. Event 35 does not duplicate those changes.
- Victory does not automatically end depression.
- Postwar recovery and reconciliation remain necessary.

## Strike and occupation missions

### Restore Essential Production

Goal:

- Resolve one strike or occupation in a named center.
- Keep basic supply and transport working.
- Choose negotiation or force.

Success restores part of local output. Failure raises social condition and can widen the action.

### Prevent a General Strike

Goal:

- Reach a settlement with major sectors.
- Keep Severity below the emergency threshold.
- Reopen or protect at least one center.

Duration target: `90` to `150` days.

### Emergency Government Mandate

Goal depends on government form:

- Pass a recovery program.
- Restore center operation.
- Reduce Severity.
- Avoid repression or opposition thresholds.
- Prepare a return to ordinary government or a visible permanent transition.

Failure opens leadership crisis, coup, or civil-conflict branches when valid.

## Humanitarian connections

Economic depression can worsen humanitarian conditions, but Event 35 does not invent famine, migration, or deaths through unsupported shortcuts.

Use shared adapters when:

- A state already has food pressure.
- Long unemployment and blockade create a valid famine context.
- A center's closure creates a registered migration or exodus pressure.
- Repression or riot resolution creates an exact civilian loss.

Event 35 supplies source, state, actor, and pressure proof. The humanitarian system owns food stages, migration cohorts, exact transfers, deaths, and cleanup.

## Chaos impact

Social Collapse activation adds zero Chaos.

Concrete event-owned outcomes may add guarded Chaos when generic systems do not already cover them:

- First nationwide general strike that paralyzes several centers.
- A government falls through the Event 35 crisis.
- A parallel administration takes durable control.
- A rare non-war political breakdown spreads to another country.

Civil war, ideology change, deaths, annexation, and state transfer already use shared generic sources. Event 35 does not add a second change for those outcomes.

A negotiated settlement can remove only the matching Event 35 one-shot pressure that its earlier outcome added. Ordinary repression or recovery does not subtract generic Chaos.

## Resolution and aftermath

Social Collapse resolves when:

- The primary movement is settled, defeated, integrated, or transformed into government.
- No national strike, occupation, coup, or civil-conflict objective remains.
- Severity is below the social emergency range.
- A proof period passes without a new organized breakdown.

The country keeps one coherent political aftermath where earned:

- Social compact.
- Emergency rule.
- Planning settlement.
- Corporate rescue order.
- Labor scar.
- Regional autonomy.
- Post-civil-war reconstruction.

The aftermath must interact with future Event 35 episodes and current government. It should not remain as an unexplained permanent modifier.

## AI behavior

AI response considers:

- Severity and trend.
- Stability.
- Movement type and support.
- Current ideology and government.
- War state and army loyalty.
- Available civilian capacity.
- Repression cost and risk.
- Foreign aid and patron pressure.
- Recovery doctrine.
- Probability of settlement.
- Territory and civil-war validity.

AI should negotiate when a settlement is affordable and movement support is broad. It may use force when the state is strong, the movement is small, and vital wartime production is threatened. It should avoid a doctrine or response that predictably triggers civil war when a safer route exists.

## Disabled evolution behavior

If Social Collapse is disabled:

- No organized social-strain incident ladder activates.
- Baseline strikes, radicalization, government crises, and the guarded National Breakdown chain remain available.
- No Evolution II factory-occupation system, coup route, separatist country, movement-specific civil war, or political transformation package is created.
- A rare baseline generic civil conflict can still occur after its own full gate and failed prevention objective.
- Event 34 inherited Evolution II still affects starting Severity and state conversion.
- Financial Contagion remains active only if its own evolution is enabled.
- Baseline recovery remains complete and valid.


---

<!-- Source: 035_great_depression_spec_part_7_second_great_depression.md -->

# Great Depression 2.0 specification, part 7: Evolution III, The Second Great Depression

## Evolution role

The action, mission, incident, and stage labels in this file are structural working labels unless they come directly from the accepted brief. Final player-facing wording belongs to implementation.

The Second Great Depression turns Event 35 into a worldwide economic condition. International trade contracts, industrial orders weaken, construction slows, expensive policy becomes harder to maintain, and countries with existing Event 35 crises face stronger pressure.

The evolution creates one global episode and many local pressure states. It does not open the full national Event 35 category for every country on the same day. A country converts into the full crisis only when local vulnerability and world pressure justify it.

This evolution creates a recoverable global economic crisis while ordinary event play continues. Countries can recover, cooperate, exploit the crisis, or fragment into separate economic blocs.

## Availability and activation

The Second Great Depression becomes available at Totalen Chaos.

Normal activation should require:

- Event 35 is active in at least one valid country.
- Evolution III is enabled.
- The source country has active Evolution II or an inherited Evolution III floor.
- International contraction or contagion has reached a material scale.
- No global Event 35 episode is already active.
- The dynamic evolution delay has elapsed.

A base timing target near `120` days is appropriate after the conditions are met.

Activation accelerators:

- Several countries have Event 35 active.
- Financial Contagion has converted another major.
- A large origin reaches Economic Paralysis.
- A major Event 34 supplier boom collapses.
- Several important ports, markets, or clearing agreements fail.
- Totalen Chaos world conditions already include severe trade disruption.

Activation reducers:

- Most exposed countries are stabilizing.
- A coordinated rescue is active.
- Major supplier countries remain stable.
- World trade and convoy conditions are secure.
- The source country is recovering rapidly.

An Event 34 Evolution III collapse activates the enabled worldwide module immediately. It starts the global episode at a high opening condition, but it still uses the normal one-time registry and global-news contract.

Evolution logging adds zero Chaos. The first actual worldwide pressure application is a separate concrete outcome.

## Global episode identity

Only one active Second Great Depression global episode exists at a time.

The global ledger records:

- Episode ID.
- Activation date.
- Source country and source national episode.
- Activation source, including Event 34 collapse when relevant.
- Highest world contraction stage.
- Countries under lighter pressure.
- Countries converted into full Event 35.
- Active supplier countries.
- Major international agreements.
- Recovery proof progress.
- Guarded Chaos receipts.
- Global announcement receipt.

A later Event 35 Evolution III activation joins the active global episode and deepens it when valid. It does not create a second global category or worldwide announcement.

## Public global state

The player does not track a second raw global number. The system uses one qualitative world stage supported by hidden global pressure.

| World stage | Working label | Meaning |
| ---: | --- | --- |
| `1` | Market Shock | Credit, orders, and trade begin contracting across several countries |
| `2` | General Contraction | Most connected economies experience material output and construction pressure |
| `3` | Worldwide Depression | Full national crises are common and international recovery is failing |
| `4` | Fragmented Recovery | Some blocs and countries recover while others remain deeply depressed |
| `5` | International Reconstruction | World pressure is declining and final recovery proof has begun |

The stage appears in Event Details, relevant categories, and the global episode report. It is a category, not another player-managed meter.

## Hidden world pressure

The global system may calculate a hidden pressure score from:

- Industrial weight of countries in active Event 35.
- Severity of major economies.
- Number and strength of contagion links.
- Global convoy and trade disruption.
- Major supplier capacity.
- Active Event 34 boom demand.
- Collapse of supplier booms.
- International rescue commitments.
- Number of countries in recovery.
- World tension and war disruption only where they materially affect the economy.
- Major disaster, famine, or contamination pressure through registered shared sources.

The hidden score moves the qualitative stage and local pressure. It must not be shown as a raw global total.

## Initial world registration

On activation, Event 35 performs one bounded initialization over valid normal civilian countries. It classifies each country into:

- Protected or lightly exposed.
- Global Contraction pressure.
- Severe exposure.
- Existing full Event 35.
- Active Industrial Boom supplier.
- Invalid special actor.

After initialization, only registered countries are processed through sparse schedules. The event must not add a recurring daily or weekly scan over the whole world.

A later country can enter the registry through exact relationship, country-creation, Event 34, or Event 35 adapters.

## Global Contraction condition

Countries without the full crisis receive a dynamic national condition whose strength depends on local exposure.

It can affect:

- Factory output.
- Construction speed.
- Production-efficiency growth.
- Consumer or administrative capacity.
- Trade and convoy resilience.
- Stability pressure.

The condition should remain lighter than full Event 35 at the same time. It cannot become a substitute full crisis with no decisions.

Local pressure rises through:

- Trade and market dependence.
- Faction, subject, or credit links to depressed majors.
- Existing economic scars.
- Low stability.
- Concentrated industry.
- Blockade or convoy failure.
- Dependence on one supplier.
- Collapse of an active supplier boom.

Local pressure falls through:

- Self-sufficiency.
- Stable institutions.
- Diversified trade.
- Strong reserves.
- Recovery reforms.
- A successful regional clearing agreement.
- Aid from a stable supplier.
- Low exposure to the global market.

## Conversion into full Event 35

A country converts when:

- Global pressure is severe enough.
- Local exposure is high.
- The country remains materially vulnerable for the conversion delay.
- It uses normal civilian systems.
- It does not already have Event 35.
- No conflict contract blocks activation.
- A global conversion receipt does not already exist for the episode.

The consequence call records entry source The Second Great Depression, global episode ID, starting world stage, local exposure, supplier dependence, and starting Severity.

Conversion remains country-specific. Some countries can pass through the entire global episode under lighter pressure without opening the full category.

## International action families

### Regional Clearing Agreement

A group of valid countries keeps essential trade and payments working. Members commit convoys, fuel, civilian capacity, or reciprocal access. The agreement lowers exposure and can form an economic bloc.

Membership rules:

- Existing diplomatic or geographic relationship.
- At least two valid countries.
- A leader with enough capacity.
- No conflicting exclusive agreement.
- Clear exit and failure conditions.

### Coordinated Public Works and Reconstruction

Countries contribute to shared transport, ports, or industrial rebuilding. Projects target exact states or routes. Contributors receive trade, influence, or recovery benefits. Failed projects create a registered international shock.

### International Debt Conference

Countries negotiate standstills, restructuring, relief, or creditor guarantees. It can lower global finance pressure. It may create concessions, delayed payments, or blocs. It never grants a free global reduction.

### Protectionist Bloc

Members restrict outside trade and support internal supply. It can protect members from some external pressure while weakening global recovery, relations, and nonmember trade.

### Competitive Devaluation or Currency Break

A country seeks export or fiscal relief through currency action represented by event effects and trade policy. It can help locally while raising pressure on partners. The design should avoid claiming engine-level exchange rates that do not exist.

### Reconstruction Supplier Compact

Stable industrial countries commit orders and material to depressed partners. It creates demand for suppliers and relief for recipients. It also concentrates risk.

### Global Recovery Conference

Available during Fragmented Recovery or International Reconstruction. It requires several major participants, declining national Severity, and material contributions. Success advances the global proof. Failure can delay recovery or strengthen rival blocs.

## Industrial Boom supplier role

An active Event 34 country becomes an important supplier because foreign orders rise while other economies contract.

### Supplier demand

The boom gains:

- Stronger usable demand.
- Faster project progress where Event 34 permits it.
- Foreign influence or concessions from exact agreements.
- A chance to stabilize recipients.

The boom also receives:

- Higher Overheating.
- Freight and convoy pressure.
- Labor and maintenance strain.
- Greater exposure to foreign default.
- Stronger collapse consequences.

### Supplier choices

- Accept World Orders.
- Ration Foreign Contracts.
- Finance Reconstruction.
- Demand Concessions.
- Build a Supplier Bloc.
- Refuse Further Exposure.

These actions belong to Event 34's category through a reusable Event 35 adapter. Event 35 must not duplicate the full boom mechanic.

### Supplier collapse

When a supplier boom collapses:

- Event 34 starts or deepens Event 35 in the supplier.
- Global pressure rises through one guarded supplier-collapse receipt.
- Dependent countries receive exact local shocks.
- Unfinished reconstruction agreements are frozen or transferred.
- The worldwide stage may deepen.
- The supplier cannot remain marked as a stable boom.

## Stable non-boom suppliers

A country without Event 34 can still provide ordinary aid or reconstruction supply. It receives smaller benefits and costs. It does not gain Event 34's extreme output or Overheating system.

## Global stage progression

### Market Shock

- First worldwide pressure package applies.
- Worldwide news event fires once.
- Countries receive initial exposure classifications.
- Emergency national and regional decisions open.

### General Contraction

- Lighter global modifiers strengthen.
- More countries become eligible for full conversion.
- Supplier and protectionist blocs form.
- International rescue becomes important.

### Worldwide Depression

- Several industrially important countries have full Event 35 or high pressure.
- Trade and construction penalties are strongest.
- National recovery is harder.
- Social Collapse and contagion consequences become more common where enabled.

### Fragmented Recovery

- Some major economies have recovered or stabilized.
- Global pressure stops rising.
- Economic blocs compete over reconstruction.
- Countries can relapse if supplier or credit arrangements fail.

### International Reconstruction

- Most industrial weight is outside severe crisis.
- Final global recovery missions open.
- Lighter country pressure decays.
- Remaining national depressions continue independently.

## Global recovery calculation

Global recovery should consider industrial weight and should not rely on country count alone.

Positive factors:

- Major industrial countries in Stabilization or Recovery.
- Declining average Severity among active major crises.
- Reopened Depression Centers.
- Stable supplier capacity.
- Restored ports, convoys, and trade links.
- Successful clearing, debt, or reconstruction agreements.
- No recent large contagion conversion.

Negative factors:

- Major economies in Economic Paralysis.
- Supplier boom collapse.
- Several new full-crisis conversions.
- Failed international rescue.
- Severe global trade disruption.
- Major war or disaster shocks with real economic effect.

The final recovery proof should last at least `120` days under stable conditions. A major supplier collapse or new major-country depression can pause or reset it.

## End of global episode

The global episode ends when:

- The world stage has reached International Reconstruction.
- Weighted severe-depression pressure remains below the recovery threshold.
- No unresolved global emergency or supplier-collapse chain remains.
- The proof period completes.

Resolution:

- Removes or decays Global Contraction conditions.
- Closes international emergency decisions.
- Preserves valid economic blocs and agreements with post-crisis purpose.
- Leaves active national Event 35 crises in place.
- Records the final world stage, recovered industrial weight, supplier outcomes, and political blocs.
- Applies a guarded Chaos reversal only for matching Event 35 global pressure previously added.

## Global announcement role

The first actual worldwide pressure application uses one global news event and one dedicated super-event. They fire when several countries receive the worldwide condition, not when the evolution variable is logged.

The news event identifies the contraction as an international economic state, shows several kinds of public evidence, and names the origin country only when that origin is known. It must not imply that every country has the full national Event 35 crisis.

The super-event marks the first worldwide economic consequence of Evolution III. It receives one stable slot, one generated period scene, one verified quote, one unique licensed musical cue, and one guarded receipt. It must present a worldwide contraction that remains recoverable and must not fire again when later origins join the same global episode.

## News and reports

World news should cover:

- First application of worldwide pressure.
- Formation of a major clearing or protectionist bloc.
- Collapse of a critical supplier boom.
- Failure of a major recovery conference.
- Entry into International Reconstruction.
- End of the global episode.

Routine national conversions use country reports and Event 35 history.

## Chaos impact

Evolution III activation adds zero Chaos.

The first concrete worldwide pressure application may add one guarded major Event 35 Chaos change because it imposes real contraction across several countries. An initial working target around `+20` is proportionate to a worldwide economic outcome, subject to the shared Chaos balance review.

Additional guarded outcomes may include:

- Collapse of a critical supplier network.
- Several major-country conversions.
- Failure of a world recovery conference that deepens the stage.

Generic Chaos from war, deaths, annexation, ideology change, contamination, and world tension is not duplicated.

Ending the global episode may remove only the matching Event 35 global pressure that was previously added. The reversal should be capped by the recorded Event 35 contribution.

## Interaction with event clusters

A Negative Economy cluster firing cannot activate The Second Great Depression merely because several economic events fire together. The global evolution still requires Totalen Chaos, enabled evolution state, Event 35 source conditions, and its own dynamic progression or inherited Event 34 Evolution III collapse.

Cluster members can create economic shocks that later affect the hidden world pressure through exact adapters.

## Multiplayer

Every player sees the same global stage and world episode. Each country manages its own national Severity and decisions.

Foreign aid, supplier, bloc, and conference actions require clear source and target ownership. One player cannot pay another player's costs through a local-only UI without an accepted transaction.

The worldwide news event fires once globally. Country reports remain targeted.

## AI behavior

AI evaluates:

- Local Severity or exposure.
- Industrial weight.
- Trade and convoy condition.
- Stability.
- Faction and subject responsibilities.
- Supplier capacity.
- Active Event 34 Overheating.
- Expected bloc benefits.
- War state.
- Ability to pay international commitments.
- Rival influence.
- Global recovery stage.

AI should form or join blocs that match its actual relationships and needs. It should avoid accepting supplier orders that would push an Event 34 boom near collapse without a strong strategic reason. It should contribute to global recovery when the cost is affordable and the agreement protects vital partners.

## Disabled evolution behavior

If The Second Great Depression is disabled:

- No global episode starts.
- No worldwide pressure package applies.
- No Evolution III worldwide news event fires.
- Existing national Event 35 and enabled lower evolutions continue.
- Event 34 inherited Evolution III still raises national starting Severity and converts inherited regions, but global content remains off.
- A previously active global episode retires through a safe cleanup path without ending national crises or granting a recovery reward.


---

<!-- Source: 035_great_depression_spec_part_8_inheritance_connections_chaos_cluster.md -->

# Great Depression 2.0 specification, part 8: Event 34 inheritance, connections, Chaos, and cluster behavior

## Event 34 relationship

Event 35 is the direct failure state of Event 34 Industrial Boom. The relationship is a consequence contract between two separate events. Event 34 owns the boom until the collapse transaction begins. Event 35 owns the depression from the moment the handoff commits.

The handoff must preserve enough history to make a failed boom feel different from an independent depression. It must also remain bounded. Event 35 receives a frozen collapse snapshot once, converts it into depression state, and then continues from its own ledger. It must not keep reading mutable Event 34 working variables after Event 34 cleanup.

## Required Event 34 collapse snapshot

The accepted Event 34 specification requires the collapse handoff to preserve the following information when it exists:

- The exact target country.
- Event 34 as the source event.
- The Event 34 firing or episode identity.
- The collapse date and collapse cause.
- The inherited evolution floor.
- Proof that all lower evolutions are active where required.
- Final Overheating.
- Peak Overheating.
- Time spent in dangerous Overheating bands.
- Recent economic shocks.
- Recent hot-running history.
- Whether the economy was actively being pushed when it collapsed.
- Whether cooling or landing work was active.
- Industrial reserve state and recent reserve use.
- Landing attempt type and failure reason.
- Speculative exposure and liquidation history.
- Primary Industrial Region state identities.
- Project profiles and stages.
- Protection, fragility, control, loss, and damage state.
- Secured but unconverted legacy receipts.
- Evolution III secondary spread state links and status.
- Repeat crash history.
- Inherited state exhaustion.

Event 35 should consume only fields that were supplied and validated. Missing optional fields use safe neutral defaults. Missing required target, source, episode, evolution, final Overheating, or one-shot proof rejects the handoff.

## Evolution inheritance

The inheritance floor is direct.

| Industrial Boom state at collapse | Event 35 active evolution floor | Opening depression character |
| --- | --- | --- |
| Baseline | Baseline | Severe national contraction |
| Evolution I Speculative Mania | Evolution I Financial Contagion | Severe contraction with exposed credit and trade links |
| Evolution II The Industrial Miracle | Evolutions I and II | Deep contraction with fragile miracle regions and immediate social pressure |
| Evolution III Runaway Industrialization | Evolutions I, II, and III | Very high Severity with worldwide depression active from the opening |

The inherited level is a floor. Event 35 may later evolve further when campaign conditions allow. It may not downgrade the inherited state because the global tier fell after the collapse.

## Inherited starting Severity

The final formula belongs in implementation tuning, but it must preserve the following ordering:

1. Final and peak Overheating provide the main severity basis.
2. Higher Event 34 evolution raises the minimum opening band.
3. Depleted reserves raise the opening shock.
4. Failed or abandoned landing work raises the opening shock.
5. Fragile or damaged Industrial Regions raise local and national pressure.
6. Completed protection and reserve preparation reduce part of the opening shock.
7. Secured but unconverted project work can be salvaged only through Event 35 recovery projects.
8. Repeat crash history raises vulnerability without making recovery impossible.

Working opening bands:

| Inherited level | Working starting Severity band |
| --- | ---: |
| Baseline | `64-78` |
| Evolution I | `72-86` |
| Evolution II | `80-93` |
| Evolution III | `90-98` |

An Event 34 collapse can reach Severity `100` only through an additional proven catastrophic condition, such as extreme final Overheating, exhausted reserves, failed emergency landing, and major regional damage. Evolution III alone should not force the exact maximum because the player still needs room to see the worsening trend and respond.

## Conversion of Industrial Regions

Event 34 regions become priority Depression Center candidates.

### Protected and completed regions

A protected region with completed or nearly completed work begins with lower local depression pressure. It may retain infrastructure, railway, resource, or production knowledge that can be salvaged through recovery. It does not automatically receive a permanent reward.

### Fragile miracle regions

A high-output region with weak logistics, heavy credit exposure, or labor exhaustion begins as a deep Depression Center. Temporary shutdowns and unemployment should replace the boom bonuses immediately. Physical building loss remains a later consequence.

### Unfinished projects

An unfinished project becomes one of:

- An abandoned works site.
- A stranded industrial order book.
- A credit-frozen plant network.
- A partially usable transport project.
- A salvageable public works foundation.

The project can be completed, restructured, liquidated, or abandoned through Event 35. Failed Event 34 work never becomes free factories or building slots.

### Evolution III spread corridors

Runaway Industrialization states remain linked by a corridor receipt. Event 35 can select a small number of the most important states as visible Depression Centers and keep the rest as hidden corridor liabilities. Recovery can restore the corridor, break it into regional networks, or leave permanent disconnected scars.

## Reserve conversion

Event 34 reserves are not carried forward as a permanent second currency.

At collapse:

- Strong reserves absorb part of the immediate efficiency and confidence shock.
- Limited reserves protect one selected center or finance one emergency action.
- Depleted reserves provide no opening protection.
- Reserve abuse or duplicate consumption is blocked by one-shot receipts.

After conversion, the reserve state becomes Event 35 history. Event 35 recovery uses its own action costs and commitments.

## Existing Event 35 crisis

A country already suffering Event 35 cannot receive a duplicate category, duplicate Severity value, duplicate state ledger, or duplicate active-crisis idea.

An Event 34 collapse into an active depression should:

1. Validate the exact target and collapse receipt.
2. Freeze the current Event 35 state for rollback safety.
3. Raise the active evolution floor when needed.
4. Add a bounded Severity increase based on the collapse snapshot.
5. Convert new Event 34 regions into the existing Depression Center ledger.
6. Apply the stronger of the current and inherited opening-shock profiles.
7. Record a deepening history entry linked to Event 34.
8. Preserve the existing doctrine and active recovery work unless the collapse invalidates them.
9. Recalculate missions and costs from the new state.
10. Commit once and clear the call inputs.

The collapse does not create a second global pacing event. The original Event 34 firing remains the pacing event. Event 35 deepening is a consequence.

## Reusable crisis entry contract

Event 35 should expose one public country-scope entry point with a working identifier such as `great_depression_start_or_deepen`.

The final implementation name may follow repository naming conventions, but the contract must remain recognizable and documented in the reusable-effects registry.

The entry point supports:

- Independent Event 35 selection.
- Event 34 collapse.
- Evolution I full-crisis conversion.
- Evolution III national conversion.
- A future approved external economic-shock caller.

It must not become a generic route for unrelated events to apply arbitrary penalties without supplying a valid source, target, severity profile, and one-shot receipt.

The complete proposed input and output surface appears in `035_great_depression_reusable_crisis_api.md`.

## Cross-event adapters

### Event 34 Industrial Boom

Event 34 can interact with Event 35 in three directions:

- A failed boom starts or deepens Event 35.
- A surviving boom can sell into depressed markets during Financial Contagion or Evolution III.
- Extraordinary global demand raises Event 34 Overheating through a public adapter owned by Event 34.

Event 35 should never write Event 34 internal Overheating directly. It submits a validated pressure request and reads the returned result.

### Random Riches and resource booms

A country with a strong resource or riches effect may gain export opportunity while other economies contract. The opportunity can improve foreign-exchange pressure or employment in resource states. It can also increase corruption, dependency, and regional inequality when those systems exist.

Event 35 should read public ideas, flags, or adapters. It should not duplicate the source event's mine, riches, or corruption logic.

### Black Friday cost discounts

A global cost-discount event must not turn depression recovery into nearly free permanent relief. Event 35 material commitments may use the shared discount system only when that system is intended to affect them. Minimum real costs, project duration, opportunity cost, and state requirements remain.

A discount may reduce purchase-style inputs. It cannot erase tied civilian factories, mission time, production sacrifice, political consequence, or risk.

### Famine and migration

Severe depression can raise humanitarian pressure through unemployment, transport breakdown, food access failure, and state abandonment. Event 35 should submit bounded pressure requests to the famine and migration system when its causal conditions are real.

It must not create famine or migration through an unproven shortcut. The humanitarian system owns food pressure, blockade proof, migration routes, cohorts, population transfer, deaths, and cleanup.

Public Works, transport recovery, foreign aid, and restored trade can reduce Event 35 contributions to humanitarian pressure. Event 35 cannot clear pressure caused by war, blockade, contamination, or another owner.

### Natural disasters

A natural disaster striking an active Depression Center raises local damage, unemployment, logistics failure, and Severity. Event 35 reads the disaster aftermath or receives a bounded shock adapter. It does not call a disaster merely to make the depression harder.

Recovery work completed before the disaster can reduce the added pressure where infrastructure and reserves logically help.

### Air contamination and CBRN systems

Air contamination, chemical damage, biological outbreaks, and nuclear fallout can damage trade, population, infrastructure, and productive capacity. Event 35 may convert those visible conditions into hidden economic pressure.

It does not duplicate contamination, deaths, condemnation, sanctions, or outbreak processing. The source systems remain authoritative.

### Condemnation and sanctions

A condemned country with embargoes or bilateral restrictions faces higher trade and finance pressure. A severe depression can make compliance or diplomatic repair more valuable, but Event 35 does not remove condemnation.

A country that uses recovery aid for prohibited military production may trigger existing condemnation or diplomatic consequences only through the owning systems.

### War, occupation, bombing, and state loss

War can support military demand while damaging civilian recovery. Occupation, bombing, rail damage, port loss, and industrial-state loss raise pressure through proven state and country conditions.

Event 35 must not count generic war, annexation, deaths, bombing, or state damage as separate Event 35 Chaos when the shared systems already record them.

### Peace and reconstruction

Peace can remove military demand and expose hidden unemployment. It can also restore trade access, allow demobilized labor to enter public works, and reduce transport damage. The net result depends on current doctrine, centers, supply, and external links.

No universal peace bonus should ignore these conditions.

## Conflict precedence

When several economic effects are active, ownership must remain clear.

| Situation | Owning rule |
| --- | --- |
| Event 34 active, Event 35 inactive | Event 34 owns the boom and Overheating |
| Event 34 crashes | Event 34 freezes and transfers, Event 35 owns the resulting crisis |
| Event 35 active, Event 34 selected independently | Target is normally invalid for a new boom unless a later approved coexistence design exists |
| Event 35 active, new Event 34 collapse occurs | Event 35 deepens in place |
| Several contagion sources reach one country | Event 35 merges exposure by source receipts and converts once |
| Evolution III reaches a country already depressed | Global pressure modifies the existing crisis without a duplicate national package |
| Humanitarian crisis overlaps | Humanitarian system owns food, cohorts, population, and deaths |
| Sanctions overlap | Condemnation system owns sanctions and bilateral enforcement |
| Disaster overlaps | Event 013 owns disaster damage and aftermath |

## Chaos accounting

Evolution unlocks and activations add zero Chaos by themselves. Event 35 adds Chaos only for concrete outcomes that exceed generic economic decline.

Provisional Event 35 Chaos map:

| Outcome | Working change | Guard |
| --- | ---: | --- |
| Independent opening | `0` | Event selection already represents the incident |
| Event 34 inherited opening | `0` | Avoid a second consequence charge |
| Evolution activation | `0` | Evolution state alone never changes Chaos |
| First prolonged Economic Paralysis in one crisis | `+1` to `+2` provisional | One receipt per episode |
| Full depression created in another country by contagion | `+2` | Global and source caps |
| Durable national social-collapse outcome that changes government policy or control | `+2` to `+3` provisional | Only when the outcome is not already counted elsewhere |
| Coup, separatist rupture, or civil conflict caused by the crisis | `+3` to `+5` | Do not duplicate generic war or ideology changes |
| First worldwide Evolution III wave | `+20` working target | One global receipt |
| Coordinated international recovery | Up to `-10` | Cannot remove more Event 35 Chaos than Event 35 recorded |
| National strong recovery after Event 35-owned paralysis | Up to `-2` | One receipt per episode and bounded by recorded Event 35 Chaos |

Every amount is provisional and requires implementation-stage balance review against the shared Chaos Meter and named probability scenarios. Event 35 should never add Chaos for routine Severity drift, ordinary decisions, state modifier refreshes, failed mission ticks, or the same repeated strike.

All changes use the shared Chaos Meter and Chaos History path with event, country, cause, and receipt context.

## Negative Economy cluster

The accepted catalog assignment places Event 35 in the `Negative Economy` cluster as a `Low` member.

The current export snapshot does not yet provide a complete usable cluster definition. The authoritative workbook must be reconciled during implementation.

Cluster behavior should follow these rules:

- Event 35 remains independently eligible at Chaos level 1.
- Cluster membership does not change the direct Event 34 failure path.
- A cluster firing that includes Event 35 counts as one global pacing event.
- Event 35 still records its own country, entry source, Severity, evolution state, and repeat history.
- A country already in Event 35 is skipped as an independent cluster target unless the cluster explicitly calls the reusable deepening contract with a valid reason.
- Event 34 collapse does not trigger the whole Negative Economy cluster.
- Evolution III worldwide spread does not replay the cluster.
- Member severity `Low` describes the baseline cluster role. It does not cap evolved consequences.

The cluster should not become a simultaneous pile of full national economic crises without country separation, actor validity, or recovery capacity. Member ordering and compatibility require an implementation-stage cluster audit.

## Event log and Event Details

Event 35 should record:

- Independent firing with the affected country.
- Inherited start linked to Event 34 without a second pacing count.
- Contagion conversion with the source country when available.
- Evolution milestones with the affected country as actor.
- Worldwide Evolution III activation as one global milestone with an origin country.
- Final recovery outcome.
- Deepening from a later Event 34 collapse.

Ordinary phase changes are not evolution rows.

Event Details should explain the premise, one public value, recovery philosophies, evolutions, and direct Event 34 relationship without exposing hidden formulas, secret incidents, or achievement routes.

## Save continuity

The cross-event contract must persist:

- Active Event 35 episode identity.
- Source type and source episode.
- Event 34 collapse receipt when inherited.
- Evolution floor.
- Converted region receipts.
- Contagion sources and exposure rows.
- Worldwide origin and global episode when Evolution III is active.
- Event 35 Chaos receipts.

Load reconciliation must never replay the Event 34 handoff, consume reserves twice, add the opening shock twice, or duplicate a converted center.

## Acceptance standard

The inheritance and connection layer is complete only when:

- Event 34 sends one frozen validated snapshot.
- Event 35 starts or deepens through one reusable fail-closed entry point.
- Evolution mapping is direct and complete.
- Existing Event 35 crises deepen without duplication.
- Industrial Regions convert into bounded local depression state.
- Failed Event 34 projects never become free permanent capacity.
- Cross-event pressure uses public adapters or proven state.
- Humanitarian, disaster, contamination, condemnation, and death ownership remains with their systems.
- Chaos changes occur only for guarded concrete outcomes.
- Direct consequences do not count as extra pacing events.
- Negative Economy cluster behavior preserves one-pacing-event semantics.
- Event logs, Event Details, docs, and the workbook distinguish independent, inherited, contagion, and worldwide entry.


---

<!-- Source: 035_great_depression_spec_part_9_ai_probability_balance.md -->

# Great Depression 2.0 specification, part 9: AI, probability, balance, exploits, and performance

## AI design goals

AI countries must understand Event 35 as a long economic crisis. They should select a recovery doctrine that fits their material position, protect valuable Depression Centers, pay real costs, respond to evolutions, and stop using actions that have become invalid.

AI receives no hidden free Severity reduction, free resources, free center reopening, or immunity from failure. It may use bounded simplifications only when the engine cannot expose the same target-selection interface used by a human. The economic result must remain equivalent.

## AI decision layers

AI behavior is divided into five layers.

1. Target-country selection for independent Event 35.
2. Opening doctrine selection.
3. Scheduled-pulse or decision-cycle action ranking.
4. State and foreign target selection.
5. Evolution-specific international and political response.

Each layer uses its own complete candidate pool and named audit scenarios.

## Target-country selection

Every valid major and player-controlled country needs a meaningful nonzero path. Weighting should produce variety without ignoring vulnerability.

### Positive target factors

- Major industrial base.
- High trade dependence.
- Recent industrial expansion.
- Low or falling stability.
- Recent industrial-state loss.
- Severe blockade or supply disruption.
- Prior rough Event 34 landing.
- Long expensive war.
- Earlier hollow Event 35 recovery after its safeguard expires.

### Negative target factors

- Active Event 35.
- Active Event 34 in the same country.
- Post-recovery safeguard.
- Very recent economic-event targeting.
- Special or nonhuman actor.
- No meaningful industrial state.
- Conflicting owner system.
- Repeated selection of the same large major while comparable countries remain untouched.

### Target fairness

A player non-major remains eligible. The event should not always choose the largest country merely because factory count is a positive factor. Use caps, normalized bands, or diminishing weight so one industrial giant does not dominate every firing.

A country with severe vulnerability should rank higher than a comparable stable country. Vulnerability should not make the result deterministic.

## AI recovery profiles

Profiles are scoring tendencies. They do not replace current country conditions.

### Relief Coalition

Prefers:

- Emergency Public Works.
- Relief and employment.
- Negotiated Social Collapse responses.
- Foreign support when dependency is acceptable.

Avoids:

- Early austerity at high unemployment.
- Market liquidation during low stability.
- Force against broad movements when settlement is possible.

Likely contexts:

- Stable democratic or coalition government.
- Large usable civilian base.
- High demand and social pressure.

### Strategic Mobilizer

Prefers:

- Rescue Strategic Industry.
- Protected military centers.
- Guaranteed war orders.
- Planning or rationing during severe war.

Avoids:

- Broad public works that consume urgent military capacity.
- Market liquidation of vital wartime plants.
- Foreign commitments that weaken the front.

Likely contexts:

- Major war.
- High military demand.
- Strong resources and logistics.

### Financial Stabilizer

Prefers:

- Stabilize Finance and Trade.
- Bank audit.
- Clearing agreements.
- Coordinated rescue.
- Ring-fencing contagion.

Avoids:

- Unsupported guarantees.
- Trade actions under total blockade.
- Repeated recapitalization without reform.

Likely contexts:

- Strong ports and convoys.
- High credit and trade pressure.
- Important international relationships.

### State Coordinator

Prefers:

- Direct State Planning.
- Trusteeship or nationalization.
- Rationing and national recovery plans.
- Strong central response to Social Collapse.

Avoids:

- Market-clearing actions that abandon strategic regions.
- Foreign dependency when domestic allocation is viable.

Likely contexts:

- Interventionist government.
- Weak trade access.
- Several sectors requiring coordinated allocation.

### Fiscal Retrencher

Prefers:

- Austerity and Retrenchment.
- Debt restructuring.
- Ending unsustainable emergency commitments.
- Late stabilization consolidation.

Avoids:

- Austerity when social strain is extreme.
- New long public works when usable capacity is too low.
- Repeated doctrine switching.

Likely contexts:

- Fiscal stress dominates.
- Stability remains high.
- Severity is moderate or improving.

### Liquidation Gambler

Prefers:

- Let the Market Clear.
- Asset reorganization.
- Withdrawal of support.
- Short-term acceptance of closure.

Avoids:

- Liquidation of the only vital center.
- Market clearing during war emergency.
- High-risk action at low stability and extreme Social Collapse.

Likely contexts:

- Strong institutions.
- High private capacity.
- Moderate Severity.
- Obsolete or duplicated industry.

## Doctrine selection model

Doctrine choice should consider:

- Dominant Severity causes.
- Usable civilian and military capacity.
- War state.
- Stability.
- Trade, convoys, ports, fuel, trains, and resources.
- Center count and concentration.
- Government and ideology.
- Existing reforms and scars.
- Event 34 inheritance.
- Active evolutions.
- Expected time horizon.

Ideology can modify preference. It should not force one doctrine regardless of material conditions.

## Doctrine switch model

AI considers a switch only after the normal cooldown and when:

- The current doctrine's core actions are invalid.
- Dominant causes changed materially.
- War or peace changed the time horizon.
- A major evolution changed the crisis.
- A current doctrine repeatedly failed.
- A different doctrine offers a clearly better expected recovery path after switch cost.

AI should not switch for a small score advantage. Require a meaningful margin and account for policy-whiplash pressure.

## Action scoring

Every action score should use:

- Immediate survival value.
- Expected Severity effect.
- State value.
- Cost affordability.
- Opportunity cost.
- Mission duration.
- Risk of failure.
- Doctrine fit.
- Evolution effect.
- Recovery legacy.
- Current active objective cap.

Emergency actions outrank long-term consolidation at Economic Paralysis. Long-term projects outrank small relief purchases during stable improvement.

## State-target scoring

The AI should prioritize centers by:

- Industrial share.
- Current local stage.
- Risk of physical loss.
- Railway, port, supply, and resource importance.
- Inherited Event 34 project value.
- Current control and front risk.
- Cost to recover.
- Ability to keep the state supplied.
- Doctrine fit.

An AI should not spend most of its economy protecting a low-value exposed state while its main industrial center is Shuttered.

A state near imminent occupation receives low investment score unless protection has military value or the state can realistically be held.

## Foreign-target scoring

For aid, contagion, supplier, and global decisions, AI considers:

- Faction, subject, alliance, and guarantee ties.
- Origin importance.
- Exposure risk.
- Provider resources.
- Convoy route.
- War alignment.
- Existing dependency or influence.
- Expected recipient recovery.
- Event 34 Overheating.
- Global recovery value.

The same source-target pair cannot be selected through several duplicate relationship rows.

## Baseline political-breakdown AI

Without Evolution II, AI countries still respond to ordinary strikes, radicalization, government crises, and the National Breakdown warning.

AI scoring considers:

- Severity duration and trend.
- Stability and government legitimacy.
- Failed recovery and emergency responses.
- Depression Center condition.
- Available relief, settlement, cabinet, and emergency-government options.
- Existence of a coherent opposing political or military base.
- Recent civil war and protected aftermath.
- Territory, force, equipment, leader, and country-package validity.

The AI should treat preventing breakdown as an emergency priority. Civil conflict is never a selectable recovery policy. It is a rare validated failure outcome after the prevention objective fails and safer political outcomes are unavailable or have also failed.

## Social Collapse AI

AI response to strikes, occupations, government crisis, and civil-conflict risk considers:

- Movement support.
- Severity.
- Stability.
- Army and police reliability.
- War urgency.
- Ideology and government.
- Expected negotiation cost.
- Expected repression deaths and radicalization.
- Valid political transformation.
- Civil-war viability.

The AI should prefer negotiation when a movement is broad and the state is weak. It may use force against a limited occupation when vital war production is at risk and the state can absorb the consequence. It should not select civil war as a normal recovery action.

## Evolution III AI

AI countries under Global Contraction decide whether to:

- Join or form a clearing bloc.
- Protect internal trade.
- Seek a supplier.
- Provide reconstruction aid.
- Exploit distressed markets.
- Enter a debt conference.
- Contribute to global recovery.

A country with active Event 34 must include Overheating in every supplier decision. High Overheating sharply lowers acceptance of new world orders unless survival, war, or faction responsibility provides a strong reason.

## Probability evidence standard

Every weighted surface requires a named baseline audit, owner-applied tuning, and comparison through the same scenarios.

Use `chaosx_ai_probability_auditor` with the HOI4 MCP probability workflow for:

- Independent target selection.
- Doctrine selection.
- AI decision weights.
- State-target pools.
- Contagion relationship selection.
- Random incidents.
- Evolution timing.
- Full-crisis conversion.
- Baseline National Breakdown outcome selection.
- Social Collapse outcome selection.
- Evolution III bloc and conference choices.

The auditor begins with `hoi4.probability_inspect`.

Use exact probability only when the complete pool and all external factors are supplied. Otherwise report score ordering, bounded probability, sampled result, or unresolved dependency.

## Named target scenarios

| ID | Scenario | Complete input requirement | Expected result |
| --- | --- | --- | --- |
| `TGT-01` | Several stable majors and one player non-major | Full valid country pool | Player non-major has meaningful weight and no single major dominates |
| `TGT-02` | One country has active Event 35 | Full pool | Active country has zero independent eligibility |
| `TGT-03` | One country has active Event 34 | Full pool | Boom country has zero independent eligibility |
| `TGT-04` | One country recently recovered | Full pool and safeguard state | Recent recipient ranks below comparable untouched countries |
| `TGT-05` | One country lost a major industrial state | Full pool and exact loss history | Vulnerable country ranks above comparable stable country |
| `TGT-06` | Several countries have prior episodes | Full history | Strong reform lowers weight while hollow recovery raises it after safeguard |
| `TGT-07` | One valid country remains | Complete pool | Remaining country receives all live weight |
| `TGT-08` | No valid country remains | Empty pool | Event is unavailable and no call is queued |
| `TGT-09` | Multiplayer with several player countries | Full player and major pool | No hidden local-player dominance |
| `TGT-10` | Event selected as Negative Economy cluster anchor | Cluster actor and member pool | Event uses cluster actor and does not reroll another country |

## Named doctrine scenarios

### `DOC-01`: Peacetime demand collapse

Inputs:

- Severity `64` and worsening.
- High demand and employment stress.
- Strong usable civilian factories.
- Good infrastructure.
- Stable government.
- No war.

Expected ordering:

1. Emergency Public Works.
2. Stabilize Finance and Trade when credit stress is also material.
3. Direct State Planning.
4. Austerity only below the first three.
5. Market Clear below safe intervention routes.
6. Strategic Industry lowest without strategic demand.

### `DOC-02`: Wartime industrial emergency

Inputs:

- Severity `74`.
- Major war.
- Strong military demand.
- Adequate fuel and resources.
- One vital military center.

Expected ordering:

1. Rescue Strategic Industry.
2. Direct State Planning.
3. Stabilize Finance and Trade when imports matter.
4. Public Works.
5. Austerity.
6. Market Clear.

### `DOC-03`: Blockaded economy

Inputs:

- Severity `78`.
- Ports blocked.
- Convoys and fuel low.
- Several domestic centers.

Expected ordering:

1. Direct State Planning.
2. Emergency Public Works when local logistics are viable.
3. Rescue Strategic Industry.
4. Austerity only with high stability.
5. Finance and Trade ranks low because its core route is blocked.
6. Market Clear ranks low if the only center is vital.

### `DOC-04`: Fiscal crisis with strong institutions

Inputs:

- Severity `48` and stable.
- Fiscal pressure is dominant.
- Stability high.
- Centers Distressed but operating.
- Strong reserves.

Expected ordering:

1. Austerity and Retrenchment.
2. Stabilize Finance and Trade.
3. Market Clear becomes plausible.
4. Public Works.
5. Direct Planning.
6. Strategic rescue.

### `DOC-05`: Social emergency

Inputs:

- Severity `88`.
- Evolution II active.
- Stability low.
- National Unrest.
- High unemployment.

Expected ordering:

1. Public Works or a valid negotiated emergency policy.
2. Direct State Planning when administration remains viable.
3. Strategic rescue only when vital centers are threatened.
4. Finance route when bank panic is dominant.
5. Austerity sharply reduced.
6. Market Clear near zero.

### `DOC-06`: Private-capacity recovery

Inputs:

- Severity `42` and improving.
- Strong stability.
- One duplicated or obsolete center.
- Low social strain.
- High private or financial capacity.

Expected ordering:

1. Market Clear or Finance and Trade.
2. Austerity.
3. Public Works.
4. Strategic rescue.
5. Planning.

Market Clear should be viable without becoming dominant in unrelated scenarios.

### `DOC-07`: Event 34 Evolution III inheritance

Inputs:

- Starting Severity `96`.
- Fragile corridor centers.
- Weak reserves.
- Financial Contagion, Social Collapse, and worldwide pressure enabled.

Expected ordering:

1. Emergency survival action before ordinary doctrine optimization.
2. Strategic rescue, planning, or public works based on actual centers.
3. Finance action when a bank panic is active.
4. Austerity and Market Clear remain near zero until the emergency is controlled.

## Named action scenarios

### `ACT-01`: Low Severity stabilization

- Severity `28`.
- Improving trend.
- All centers protected.
- One active consolidation project.

Expected:

- Complete consolidation and Prevent a Relapse rank highest.
- Emergency Relief and new major projects rank low.
- Doctrine switch ranks near zero.

### `ACT-02`: Freight collapse

- Severity `72`.
- Rail and train pressure dominant.
- One center Idled.

Expected:

- Keep Essential Freight Moving and center protection rank highest.
- Unrelated finance or political actions do not dominate.

### `ACT-03`: Economic Paralysis

- Severity `100`.
- Maximum emergency active.
- Limited usable civilian capacity.

Expected:

- Only emergency actions and valid foreign aid receive meaningful weight.
- Long projects, doctrine switching, and aggressive consolidation receive zero or near-zero weight.

### `ACT-04`: Imminent state loss

- Center on active losing front.
- Low chance of holding it.

Expected:

- Expensive long project ranks low.
- Emergency evacuation, minimal protection, or no investment can rank above it.
- AI does not repeatedly restart the same doomed project.

### `ACT-05`: Relapse risk

- Stabilization phase.
- Severity `36` and worsening.
- One unresolved center.

Expected:

- Prevent a Relapse and center reopening rank above budget consolidation or policy withdrawal.

## Named contagion scenarios

| ID | Scenario | Expected result |
| --- | --- | --- |
| `CTG-01` | Stable major faction ally exposed to one origin | Ring-fence or limited aid ranks above abandonment |
| `CTG-02` | Weak subject tied to collapsing overlord | Emergency aid or diversification appears, conversion risk is high |
| `CTG-03` | Unrelated neighbor with only one light link | Exposure remains light and full conversion is rare |
| `CTG-04` | Provider cannot afford aid | Aid weight reaches zero and ring-fence or abandonment remains valid |
| `CTG-05` | Origin improving rapidly | New exposure drift falls and aggressive abandonment ranks lower |
| `CTG-06` | Origin at Economic Paralysis with failed rescue | Abandonment and emergency ring-fence rise, conversion risk increases |
| `CTG-07` | Same source-target pair has faction and subject links | One merged strongest row, no duplicate pressure |
| `CTG-08` | Country already converted from origin episode | No second conversion or reward |
| `CTG-09` | Depth-three propagation | Pressure is lower and anti-loop rules hold |
| `CTG-10` | Industrial Boom supplier at high Overheating | New supplier commitments rank below restraint |

## Named baseline breakdown scenarios

### `BDP-01`: Deep Depression with contained unrest

- Severity below the National Breakdown gate.
- Stability strained but functioning.
- One ordinary strike or cabinet dispute.

Expected:

- Relief, settlement, or recovery action is available.
- Civil conflict has zero eligibility.

### `BDP-02`: Economic Paralysis without a coherent opposing side

- Severity near maximum for the required duration.
- Stability critically low.
- Prevention objective failed.
- No valid political actor, territorial base, leader, or force package.

Expected:

- Government fall, emergency rule, policy reversal, or prolonged unrest can resolve the crisis.
- Civil conflict has zero eligibility.

### `BDP-03`: Full baseline breakdown gate

- Sustained near-maximum Severity.
- Critically weak legitimacy.
- Several failed responses.
- Valid opposing political or military base.
- Valid territory, forces, equipment, and leadership.
- No recent civil war block.

Expected:

- Civil conflict receives a bounded nonzero failure weight.
- It does not dominate government replacement or emergency settlement automatically.

### `BDP-04`: Recent civil war

Expected:

- New baseline Event 35 civil conflict has zero eligibility.
- Recovery, cabinet replacement, and emergency settlement remain possible.

## Named Social Collapse scenarios

### `SOC-01`: Broad strike with viable settlement

- Movement support high.
- Government stable enough to negotiate.
- No immediate front emergency.

Expected:

- Negotiation and employment compact outrank force.
- Civil war has zero eligibility.

### `SOC-02`: Small occupation in vital wartime plant

- Movement support low.
- War urgency high.
- State can use force.

Expected:

- Targeted enforcement or negotiated quick settlement can rank highest.
- National emergency government ranks low.

### `SOC-03`: Failed government crisis

- Severity above `90` for sustained duration.
- Stability very low.
- Organized movement and failed mandate.
- Valid coup actor.

Expected:

- Coup or transfer-of-power outcomes are eligible.
- Civil war remains ineligible when no coherent territorial base exists.

### `SOC-04`: Regional separatist pressure

- Valid regional identity.
- Abandoned center in region.
- Strong local movement.
- Valid territory and actor package.

Expected:

- Autonomy, settlement, or separatist conflict are eligible.
- A random unrelated ideology civil war is ineligible.

### `SOC-05`: Recent civil war

Expected:

- New civil conflict has zero eligibility.
- Recovery, settlement, or emergency government remain valid.

## Named global scenarios

| ID | Scenario | Expected result |
| --- | --- | --- |
| `GLB-01` | Evolution III activates with one major origin | One global episode and one super-event receipt |
| `GLB-02` | Ten stable countries under light pressure | Lighter condition applies without full Event 35 categories |
| `GLB-03` | Highly exposed unstable country | Full conversion ranks above stable self-sufficient peers |
| `GLB-04` | Active boom supplier with low Overheating | Supplier and reconstruction actions are viable |
| `GLB-05` | Active boom supplier with dangerous Overheating | Restraint outranks accepting more orders |
| `GLB-06` | Supplier boom collapses | One global shock receipt and exact dependent-country shocks |
| `GLB-07` | Most industrial weight recovers | World stage advances toward reconstruction |
| `GLB-08` | New major crisis during proof period | Global recovery proof pauses or resets |
| `GLB-09` | Evolution III already active from another origin | New source joins or deepens existing episode, no duplicate super-event |
| `GLB-10` | Evolution III disabled | No global pressure or super-event |

## Evolution timing scenarios

| ID | Inputs | Expected timing relationship |
| --- | --- | --- |
| `EVO-01` | Evolution I, Severity `75`, strong links, worsening | Faster than base |
| `EVO-02` | Evolution I, Severity `48`, improving, weak links | Slower than base |
| `EVO-03` | Evolution II, long high Severity, low stability | Faster than base |
| `EVO-04` | Evolution II, reopened centers, high stability | Slower or ineligible |
| `EVO-05` | Evolution III, several major depressions | Faster than base |
| `EVO-06` | Evolution III, one recovering small origin | Slower or ineligible |
| `EVO-07` | Event 34 inherited evolution | Immediate enabled activation |
| `EVO-08` | Evolution disabled | Zero activation probability |

Probability auditing should compare median and tail timing under scheduled state changes. It should not claim exact MTTH from source text alone.

## Incident-pool balance

Incident pools should be complete and conditional.

Rules:

- Ineligible incidents have zero weight.
- One generic event should not dominate every context.
- Positive and negative incidents remain possible when conditions support them.
- Severe incidents require severe inputs.
- The same incident family uses cooldowns and receipts.
- Country, state, and relationship targets are validated before selection.
- A no-op fallback exists when no meaningful incident is eligible.

The probability auditor should inspect the full pool for at least one scenario in every Severity band and active evolution.

## National modifier balance targets

The event must force replanning without removing all agency.

Initial effect direction by band:

| Band | Output direction | Construction direction | Civilian capacity direction | Stability direction |
| --- | --- | --- | --- | --- |
| Fragile Economy | Noticeable penalty | Noticeable penalty | Light pressure | Light pressure |
| Depression | Strong penalty | Strong penalty | Material pressure | Material pressure |
| Deep Depression | Very strong penalty | Very strong penalty | Heavy pressure | Strong pressure |
| Systemic Breakdown | Near-paralysis in unprotected sectors | Severe restriction | Very heavy pressure | Severe pressure |
| Economic Paralysis | Deepest supported penalty with emergency floor | Ordinary construction nearly stopped | Emergency minimum preserved | Crisis state |

Exact modifiers require implementation testing. The design rejects a decorative `5%` crisis. It also rejects a total soft lock that makes the recovery decisions impossible to pay.

## Opening-shock balance

The opening shock should be stronger than the sustained modifier for about `30` to `60` days. It needs to affect current production and construction planning immediately.

It should not:

- Delete factories.
- Clear all production efficiency without limit.
- Force a law change instantly.
- Apply twice on save load.
- Reapply in full after an ordinary relapse.

## Recovery-action balance

Large actions should have delayed results and real costs. One action cannot lower Severity from Deep Depression to Stabilizing.

A normal successful project should:

- Move Severity enough to matter.
- Improve one hidden cause.
- Change a state or institutional receipt.
- Create a cost or risk that affects the next choice.

Small relief can slow deterioration. It should not replace structural recovery.

## AI resource floors

AI must protect minimum reserves before paying actions.

Suggested floors:

- Trains and trucks needed for current supply.
- Convoys needed for essential trade and troop movement.
- Fuel needed for active war plans.
- Equipment needed to keep divisions viable.
- A minimum usable civilian base.
- Stability floor before risky austerity or force.

The floors are dynamic. A country at peace can commit more than a country on several active fronts.

## Exploit audit

### Repeated action farming

Every major decision uses cooldowns, project state, or one-shot receipts. A player cannot start and cancel the same action to gain partial relief repeatedly.

### Refund symmetry

Committed stockpiles are refunded only when the action proves they were reserved and not consumed. Failure, state loss, or country deletion cannot duplicate the resources.

### Doctrine cycling

Doctrine actions retain completion receipts across switches. Returning to a doctrine does not reset its one-time rewards.

### State transfer

A center cannot pay recovery rewards to two owners. The state record moves or is closed.

### Foreign aid loops

The provider pays exact resources. Source-target transactions have stable IDs. Subject, faction, and bilateral paths cannot claim the same package several times.

### Contagion farming

One origin episode can convert one target once. Recovery and renewed exposure do not create another first-spread Chaos or reward receipt.

### Global supplier farming

Supplier orders create Overheating or real capacity cost. A boom cannot accept unlimited orders for free.

### Maximum-Severity farming

Emergency aid, factory loss, and political incidents are guarded. Keeping Severity at `100` cannot create recurring payouts or repeated destruction.

### Achievement manipulation

Achievements use episode start, peak Severity, doctrine, center, and disqualifier receipts. Tag switching, state transfer, manual debug, or late joining cannot satisfy them improperly.

## Performance limits

- Sparse active-country registry.
- Sparse center registry.
- Sparse origin-target contagion rows.
- One global episode registry.
- No unauthorized recurring whole-world scan.
- No per-state daily evaluation.
- Phase-scaled national evaluation that averages about weekly and accelerates only for bounded emergencies.
- State progression checked through registered centers only.
- Dynamic localisation reads cached public values.
- Cleanup removes invalid rows promptly.
- Random target pools are built only when a decision or incident needs them.

## Multiplayer balance

- Same target-selection rules for all players.
- Foreign transactions identify payer and recipient.
- One global Evolution III stage.
- One super-event receipt.
- Player-facing decisions remain country-local.
- AI can act without using a human-only selected-state interface.
- No local player receives hidden extra target weight.

## DLC and engine compatibility

The event should use core HOI4 industry, construction, stability, state, decision, and event systems. DLC-specific markets, embargoes, or economic features need guarded branches and a core fallback that preserves the design through existing relationships and modifiers.

A fallback cannot invent exact bilateral trade data. It may use proven faction, subject, adjacency, convoy, and event-created agreement links.

## Required implementation evidence

The completion report must include:

- Baseline and comparison revision for every named probability surface.
- Scenario IDs and complete inputs.
- Candidate-pool completeness statement.
- Exact, bounded, sampled, score-only, or unresolved classification.
- Before and after ordering.
- Starvation and dominance checks.
- AI affordability and resource-floor checks.
- State-target selection examples.
- Contagion anti-loop evidence.
- Evolution timing evidence.
- Performance ownership and schedule.
- Every unresolved probability dependency.


---

<!-- Source: 035_great_depression_spec_part_10_presentation_assets_text.md -->

# Great Depression 2.0 specification, part 10: Presentation, assets, and writing direction

## Presentation hierarchy

The event should be readable from the normal decision interface.

Primary presentation:

1. Opening report event.
2. One Great Depression 2.0 decision category.
3. Depression Severity display.
4. Trend and next threshold.
5. One selected Depression Center at a time.
6. One main objective and up to two supporting missions.
7. State modifiers and map highlighting for registered centers.
8. Event Details and evolution history.

Evolution III adds one global super-event and one qualitative world-stage line. It does not require a separate permanent scripted GUI.

## Category layout

The category header should answer five questions quickly:

- How severe is the crisis?
- Is it improving or worsening?
- What threshold matters next?
- Which recovery doctrine is active?
- What can the player do now?

Recommended order:

```text
Category picture
Depression Severity meter or compact progress display
Severity band and trend
Current phase and recovery doctrine
Next threshold
Top material causes
Selected Depression Center and local condition
Active objective
Current primary decisions
```

Do not place a paragraph above the actions. Use a concise summary and tooltips.

## Severity display

The display needs:

- Value from `0` to `100`.
- Named band.
- Qualitative trend.
- Threshold marker.
- Distinct Economic Paralysis state.
- Label and icon support in addition to color.

Suggested color direction:

- Recovery and stabilization use restrained green or blue.
- Fragile Economy uses yellow.
- Depression and Deep Depression use orange.
- Systemic Breakdown and Economic Paralysis use red and dark red.

The exact colors should follow existing Chaos Redux and vanilla UI contrast. Color must not carry the meaning alone.

## Category picture

Use one static decision category picture as the baseline. It should establish the event's identity without drawing fake controls.

Visual direction:

- Period industrial district during a shutdown.
- Idle factory gate, dark windows, quiet rail sidings, and a line of unemployed workers or families.
- Country-neutral 1936 to 1945 setting.
- Documentary or period press photography treatment.
- Strong readable industrial subject at the category picture's actual size.
- No readable generated text.
- No stock-market graph, modern skyline, computer display, or modern clothing.
- No map as the main subject.

The asset worker must inspect the active category-picture consumer and the canonical reference family before fixing size. The current reference family uses `114x101`, but that is not a universal assumption.

A phase-variant or animated category picture is not required. The Severity display already communicates changing state. Additional motion would add production cost without improving the main decision.

## Opening report image

The current repository uses `GFX_report_event_great_depression`. Treat that sprite as a stable migration anchor until inspection proves a reason to rename it.

Source mode direction:

- Generated period documentary scene is preferred because Event 35 can affect any country and needs a country-neutral composition.
- Sourced archival photography is acceptable when rights, date, and geographic implication fit the final event.
- Do not reuse a modern recession photograph.

Composition direction:

- Foreground workers, closed plant, empty construction site, or idle freight yard.
- Visible human and industrial consequences.
- Strong horizontal event-picture crop.
- Serious treatment without theatrical destruction.

The opening image should communicate halted work. It should not show the final political or global evolutions.

## News image

The ordinary news event may reuse the opening report family when the existing news surface and crop support it. A separate news image is justified if the news event uses a different canvas or if the opening art is too local to read as an international report.

News direction:

- Broad industrial slowdown.
- Closed exchanges, idle docks, or silent factories.
- No national flag that would make the image wrong for other target countries.
- No readable newspaper headline generated inside the art.

## Evolution I visual direction

Financial Contagion needs a report image or event-art variant only for its first major activation and important international incidents.

Subject direction:

- Crowded banking hall, closed bank doors, queues, brokers or clerks handling failed payment notices, or freight documents that no longer clear.
- Several countries implied through travelers, shipping, or correspondence without using a map as the main composition.
- Period clothing and architecture.
- Anxiety shown through action and queues, not abstract red arrows.

## Evolution II visual direction

Social Collapse needs one report image family for national unrest.

Subject direction:

- Factory occupation, organized strike line, relief march, or guarded industrial gate.
- Show the political and labor conflict created by prolonged unemployment.
- Keep violence restrained unless the exact incident is violent.
- Avoid cheap comedy or spectacle.
- Avoid using a specific real political symbol unless the country and movement justify it.

Country-specific political events may reuse existing valid leader or party assets. New grounded portraits are not inferred by this spec.

## Evolution III super-event image

The worldwide escalation needs one unique super-event image.

Source mode:

- Generated period documentary or symbolic scene.

Subject direction:

- A major international port, freight exchange, or industrial city brought to a halt.
- Idle cranes, silent locomotives, dark factory districts, and crowds seeking work.
- Several regions of the world implied through shipping, uniforms, cargo, or architecture while keeping one coherent scene.
- Global scale communicated through the collapse of exchange and movement.
- No map collage.
- No readable text.
- No modern financial screens.
- No apocalyptic ruins because the event is an economic world crisis, not physical annihilation.

The image should support the global-contraction super-event role through grounded economic shutdown and human hardship, without apocalyptic framing.

## Icon inventory

Every generated alpha-backed icon requests native transparency and preserves it through DDS conversion.

### Category and doctrine icons

| Working asset | Type | Visual direction | Proposed runtime folder |
| --- | --- | --- | --- |
| Great Depression category | Decision category icon | Dark factory gate, idle gear, or closed plant symbol | `gfx/interface/decisions/035_great_depression/` |
| Emergency Public Works | Decision icon | Worker, shovel, rail, and public structure in one simple silhouette | Same event folder |
| Rescue Strategic Industry | Decision icon | Protected factory or shielded gear | Same event folder |
| Stabilize Finance and Trade | Decision icon | Bank ledger, secure coin, ship, or linked trade document | Same event folder |
| Austerity and Retrenchment | Decision icon | Cut ledger, tied budget, or narrowed scale | Same event folder |
| Direct State Planning | Decision icon | Planning board, factory grid, or state allocation emblem | Same event folder |
| Let the Market Clear | Decision icon | Auction hammer, reopened shopfront, or broken chain with surviving gear | Same event folder |
| Cabinet Review | Decision icon | Cabinet table, policy folder, or rotating doctrine symbol | Same event folder |

The icons should be distinct at `32x32`. They should not be resized focus icons or one shared icon with recolors.

### Mission icons

| Working asset | Type | Visual direction |
| --- | --- | --- |
| Halt the Panic | Mission icon | Closed bank and stabilizing barrier |
| Keep Essential Freight Moving | Mission icon | Locomotive, rail switch, or freight crate |
| Reopen Depression Center | Mission icon | Factory lights returning or gate reopening |
| Prevent a Relapse | Mission icon | Fragile upward line supported by brace, without modern chart styling |
| Maximum-Severity Emergency | Mission icon | Dark factory and emergency beacon |
| Contain Financial Contagion | Mission icon | Linked institutions separated by a firebreak |
| Prevent a General Strike | Mission icon | Factory gate and negotiation table |
| International Reconstruction | Mission icon | Crane, rail, ship, and cooperative emblem |

Mission icons need the exact mission reference family. They are not decision icons with different filenames.

### Idea and national-condition icons

| Working asset | Surface | Direction |
| --- | --- | --- |
| Opening Economic Shock | Timed idea | Sudden factory shutdown and falling order book |
| Active Great Depression | Dynamic national condition | Idle factory and unemployment queue |
| Economic Contagion | Secondary-country condition | Linked banks or markets under strain |
| Global Contraction | Evolution III condition | World shipping and factory exchange halted |
| Post-Depression Recovery | Timed recovery safeguard | Reopened gate, workers returning, and repaired rail |
| Recovery doctrine legacies | Route-specific idea family | One unique symbol for each durable institution |
| Recovery scars | Country or state idea family | Broken rail, hollow plant, debt ledger, or emergency control symbol |

Prefer one staged active-depression icon family. Avoid many near-identical national spirits.

### State modifier icons

| Working state | Direction |
| --- | --- |
| Distressed Center | Factory with partial shutdown |
| Idled Center | Dark gear or stopped conveyor |
| Shuttered Center | Closed gate and chain |
| Abandoned Works | Unfinished structure and idle crane |
| Protected Center | Factory under shield |
| Public Works Active | Worker and rail or road |
| Reopened Center | Lit factory and open gate |
| Hollowed Industrial District | Empty factory shell |

State icons must remain readable in the state-view consumer. They should use the state-modifier reference family, not decision art.

### Evolution icons

Each evolution needs one Event Details and history icon if the shared interface supports event-specific evolution art.

- Financial Contagion: linked banks or contracts transmitting failure.
- Social Collapse: occupied factory or broken civic order.
- The Second Great Depression: halted global shipping and industry.

## Achievement icons

Every accepted achievement needs a complete root-level achievement triplet:

- Eligible color asset.
- Grey locked asset.
- Not-eligible asset using the verified overlay workflow.

Filenames must match final achievement IDs. Achievement assets stay directly under `gfx/achievements/` unless current engine inspection proves another requirement.

## Asset production routing

Use:

- `chaosx_generated_event_art` for generated report, news, category-picture, and super-event scenes.
- `chaosx_asset_source_researcher` when the final choice requires real archival Great Depression material.
- `chaosx_icon_artist` for decisions, missions, ideas, state modifiers, evolution icons, and achievements.
- `chaosx_super_event_audio_researcher` for the Evolution III musical cue.
- `chaosx_super_event_text_researcher` for quote and cultural-reaction research.

There are no character portraits, flags, faction emblems, 3D models, unit counters, or skeletal animations required by the baseline specification.

Social Collapse can create a leader or country identity only when a valid existing political route supports it. Any resulting portrait, flag, country, or unit asset becomes a separate accepted requirement and follows the full source, tag, portrait, flag, country, and force-package workflow.

## Temporary asset workspace

During implementation, use:

```text
docs/assets/035_great_depression/
```

for sources, prompts, previews, provenance, contact sheets, and handoffs.

Final runtime assets belong in engine-facing event folders. Before completion, promote durable evidence into permanent Event 35 documentation, verify that no runtime reference points into `docs/assets/`, and delete the temporary event workspace.

## Asset QA

For every asset:

- Inspect the exact vanilla or Chaos Redux reference family.
- Confirm canvas and consumer.
- Preserve native transparency for alpha-backed icons.
- Verify no white halo, fake checkerboard, opaque square, or clipped silhouette.
- Review at native size and enlarged nearest-neighbor size.
- Confirm sprite name and path before final wiring.
- Create contact sheets for each asset family.
- Record source mode, prompt or source, rights, dimensions, checksums, and final status.

Generated event scenes must be checked for modern props, readable false text, wrong era clothing, and country-specific symbols that break reuse.

## Player-facing writing standard

The planning package defines direction. It does not provide pasteable localisation.

All final text must:

- Use concrete in-world observations.
- Describe idle plants, failed orders, lost work, freight disruption, bank queues, and policy action.
- Explain visible costs and requirements clearly.
- Name dynamic countries and states where relevant.
- Keep hidden formulas, incident pools, and future evolutions secret.
- Avoid process history and rework language.
- Avoid em dashes and semicolons.
- Avoid staccato sentence chains.
- Avoid contrast formulas and generic dramatic templates.
- Avoid cheap humor around mass unemployment, hunger, repression, or civil conflict.

## Opening event text direction

### Viewpoint

National government receiving evidence from factories, banks, local administrations, and transport authorities.

### Driving force

Orders are cancelled, credit stops circulating, construction closes, and unemployment spreads through the industrial regions.

### Information shown

- The country has entered a severe economic contraction.
- Production and construction will fall sharply.
- A decision category has opened.
- The first Depression Centers are visible.
- The government must choose a recovery direction.

### Information withheld

- Exact hidden component formula.
- Future evolution branches.
- Exact incident probabilities.
- Achievement conditions.
- Whether a civil war or worldwide depression will occur.

### Tone

Serious, specific, and administrative without becoming paperwork-centered. The human effect should be visible through lost work and halted industry.

### Option direction

The opening option acknowledges the need for immediate economic action. It can use restrained official confidence or grim administrative understatement. It should not joke about unemployment or use a generic statement that the world will never be the same.

## Independent news text direction

### Viewpoint

Foreign press and governments observing the target country's industrial contraction.

### Information shown

- Major plants and construction are slowing.
- Unemployment and financial stress are spreading inside the named country.
- Foreign partners are reconsidering exposure.

### Information withheld

- Hidden Severity.
- Future contagion target.
- Event 34 inheritance details unless the source was publicly known.

### Tone

Period news report with concrete economic observations. Avoid broad claims that every market is already collapsing.

## Event 34 collapse text direction

### Viewpoint

The boom country witnesses the reversal of its own expansion.

### Driving force

Orders, credit, transport, and investment built for extraordinary growth fail together. Protected and unfinished Industrial Regions should be named where possible.

### Information shown

- The boom has ended.
- Event 35 has begun or deepened.
- The starting crisis reflects the failed boom.
- The player must manage inherited centers.

### Information withheld

- Raw Overheating formula.
- Snapshot fields.
- Direct code mapping.

### Tone

Abrupt reversal and material failure. Avoid moralizing that the boom was always doomed.

## Severity and category text direction

The category summary should use one or two short paragraphs at most.

It should dynamically mention:

- Current band.
- Trend.
- Main cause.
- Next threshold.
- Selected center.
- Active doctrine.

Tooltips explain:

- What changes Severity.
- What the next threshold does.
- Why the current action is blocked.
- Which cost is committed.
- What happens on success or failure.

Do not expose a long hidden contributor ledger.

## Doctrine text direction

### Emergency Public Works

Speaker and stance:

- Government presenting employment and construction as a national recovery program.

Tone:

- Practical, mobilizing, and public-facing.

Visible promise:

- Jobs, transport, and state reconstruction at a large immediate cost.

Avoid:

- Claiming projects are free.
- Generic praise of infrastructure.

### Rescue Strategic Industry

Speaker and stance:

- War ministry, industrial board, or cabinet choosing which plants must survive.

Tone:

- Hard prioritization and strategic necessity.

Visible promise:

- Preserve essential production while other sectors bear more pressure.

Avoid:

- Treating all factories as equally strategic.

### Stabilize Finance and Trade

Speaker and stance:

- Treasury, central bank equivalent, commercial ministry, and foreign partners.

Tone:

- Controlled confidence and concrete institutional action.

Visible promise:

- Reopen viable finance and preserve essential exchange.

Avoid:

- Modern central-bank jargon.
- Claiming exact exchange rates that the game does not model.

### Austerity and Retrenchment

Speaker and stance:

- Treasury or cabinet arguing that the state cannot sustain every commitment.

Tone:

- Severe, sober, and politically contested.

Visible promise:

- Lower fiscal pressure with an explicit unemployment and stability risk.

Avoid:

- Presenting austerity as automatically wise or evil.

### Direct State Planning

Speaker and stance:

- Emergency planning authority coordinating production, transport, and distribution.

Tone:

- Directive and organized.

Visible promise:

- Lower volatility and protect essential sectors at political and flexibility cost.

Avoid:

- Generic ideological slogans unless the country route supports them.

### Let the Market Clear

Speaker and stance:

- Government or commercial coalition accepting closure and repricing.

Tone:

- Cold confidence, resignation, or commercial pragmatism according to country.

Visible promise:

- Lower state commitment and a possible later recovery with high short-term risk.

Avoid:

- Hidden promise that the route will succeed.

## Depression Center text direction

State text should name:

- The state.
- Its current local condition.
- The industry, transport, port, or project that makes it important.
- Current treatment.
- What will happen if the mission succeeds or fails.

Avoid a generic sentence used for every state.

## Financial Contagion text direction

### Origin report

Show:

- Foreign credit and contracts are reacting to the national crisis.
- Specific partners are exposed when valid.
- New international actions are available.

Keep uncertain:

- Which country will enter a full depression.
- Exact conversion chance.

Tone:

- International economic fear shown through banks, shipping, and contracts.

### Exposed-country report

Show:

- The named origin and relationship.
- Local banking, trade, or contract pressure.
- Ring-fence, aid, diversification, or abandonment choices.

Do not say the country has Event 35 until conversion actually occurs.

## Social Collapse text direction

### Viewpoint

Workers, local authorities, movements, employers, government, and security institutions according to incident.

### Information shown

- Exact strike, occupation, riot, or government crisis.
- Named state or sector.
- Visible movement and demand.
- Available response and cost.

### Information withheld

- Hidden Social Strain.
- Future coup or civil-war roll.
- Secret support values.

### Tone

Serious and political. Official euphemism, propaganda, or bitter understatement can be used when it exposes the speaker's position. Cheap jokes are forbidden.

## Evolution III super-event text direction

### Role

First concrete worldwide economic contraction.

### Title direction

Short and specific to a second global depression. Research period economic, literary, or political references before final choice. Do not use generic titles about darkness, flames, or the end.

### Description direction

Show the simultaneous slowing of factories, ports, trade credit, and construction across several countries. State that the crisis is worldwide. Do not list modifiers or claim that every country is equally affected.

### Reaction direction

Brief, grim, and suitable for a global economic crisis. A sourced cultural allusion may be used only after verification. Do not use an unsourced quotation or lyric.

### Quote direction

Research public-domain or otherwise suitable historical, economic, political, literary, or religious text about unemployment, credit, hunger, work, or international collapse. Verify exact wording and attribution. The planning package selects no final quote.

### Audio direction

Use an intentional musical recording with a restrained, period-suitable, mournful or processional character. Research composition and recording rights separately. Do not use drones, test tones, abstract noise, or another super-event's track.

## Recovery text direction

Recovery reports should distinguish:

- Strong recovery.
- Uneven recovery.
- Hollow recovery.
- End of worldwide depression.

They should name what reopened, what institution remains, and what cost persists. Avoid a generic celebration that ignores scars.

## Event Details direction

The Event Details premise should explain:

- A major or player country can enter a long depression.
- One Severity value is managed.
- The event can start independently or from Event 34 collapse.
- Recovery doctrine and Depression Centers shape the result.

Evolution details explain the visible premise of each stage without listing raw effects or hidden conditions.

The cluster detail identifies Event 35 as a Low member of Negative Economy after the authoritative cluster registry is completed.

## Spreadsheet direction

After implementation, the workbook row should use final in-game wording for:

- Event Details.
- Evolution I details.
- Evolution II details.
- Evolution III details.
- Cluster name and Low danger.
- Cross-event Event 34 relation.
- Super-event presence for Evolution III.

The workbook is authoritative. Regenerate all three CSV exports through the repository exporter.


---

<!-- Source: 035_great_depression_spec_part_11_achievements_acceptance.md -->

# Great Depression 2.0 specification, part 11: Achievements, acceptance scenarios, and completion standard

## Achievement role

Event 35 achievements should reward national recovery, center reopening, prevention of evolved spread, survival of Social Collapse, difficult liquidation, and resolution of the worldwide crisis. They must use stable episode receipts and clear disqualifiers.

Event 34 owns the cross-event Evolution III crash-and-recovery achievement through its accepted `The Long Fall` contract. Event 35 supplies the recovery receipts that contract needs and does not create a duplicate inherited-crash achievement.

The labels below are working labels. Final names and descriptions need implementation writing and icon review.

## Achievement 1: Back to Work

### Mastery goal

Recover from a severe independent Event 35 episode while preserving every original Depression Center and losing no civilian or military factory level through Event 35.

### Required conditions

- Player country enters Event 35 through an independent firing.
- Starting Severity meets the final severe minimum.
- The opening Depression Center registry is frozen for the achievement.
- Every original center reaches Recovered or another approved positive restructured state.
- No original center is abandoned.
- No Event 35 factory-loss receipt is recorded.
- Recovery proof completes for the same player-owned episode.

### Disqualifiers

- Event 34 inherited source.
- Any Event 35 factory-loss receipt.
- Deliberate center abandonment or liquidation.
- State transfer, annexation, puppeting, or tag switching used to remove a failing center from the requirement.
- Debug, force completion, or achievement tracking that begins after the opening snapshot.

### Tracking

Freeze the original center IDs and their civilian and military factory levels at the accepted opening transaction. Ordinary combat damage does not disqualify the achievement unless Event 35 records the loss as its own consequence. The achievement evaluates during recovery completion before active episode data is cleared.

### Icon direction

An open factory gate with workers returning and every industrial building still intact.

## Achievement 2: Every Center Reopened

### Mastery goal

Reach Economic Paralysis and recover every Depression Center without abandoning one.

### Required conditions

- Peak Severity reaches `100`.
- The country survives the maximum-Severity emergency.
- The episode contains at least three centers, or every valid center available to a smaller economy.
- Every registered center reaches Recovered or an approved positive restructured state.
- Final national result is Strong or Uneven Recovery.

### Disqualifiers

- Any center ends Abandoned, Shuttered, unresolved, or invalidly removed from the ledger.
- A center is liquidated as the final solution.
- Recovery closes through debug or forced cleanup.
- State transfer is used to bypass a center requirement.

### Tracking

Use the episode center registry, highest Severity receipt, maximum-emergency completion, and final center-state counts. A later valid center addition becomes part of the requirement once registered.

### Icon direction

Several industrial bays or workshops with their lights restored, shown as one readable district.

## Achievement 3: Containment Line

### Mastery goal

Contain material Financial Contagion without allowing any foreign country materially exposed by the player's source crisis to convert into a full Event 35 crisis.

### Required conditions

- Financial Contagion is active in the player's source episode.
- Source Severity reaches the final deep-contraction threshold.
- At least the required number of valid foreign countries reaches Observed Exposure or a stronger stage, scaled for the valid pool.
- At least one aid, ring-fence, clearing, diversification, or coordinated-rescue action completes.
- No attributable foreign full-crisis conversion occurs.
- All outgoing source links resolve as Contained or through source recovery.
- The source country recovers.

### Disqualifiers

- A foreign conversion materially attributed to the player's source episode.
- Deleting, annexing, or invalidly cleaning an exposed country to remove the link.
- Disabling the evolution after exposure begins.
- Debug or force cleanup.
- Loss of source-country ownership.

### Tracking

Multi-source exposure needs attribution. A conversion disqualifies the achievement when the player source was a material dominant or secondary contributor. An unrelated source does not disqualify it unless the player's exposure record crossed the final contribution threshold.

### Icon direction

A chain of banks, factories, and freight links stopped by a clear economic firebreak. Avoid disease imagery.

## Achievement 4: The Social Peace

### Mastery goal

Recover from Social Collapse after near-maximum Severity without a successful coup, Event 35 civil conflict, or permanent emergency rule.

### Required conditions

- Social Collapse is active.
- Peak Severity reaches at least `90`.
- At least one major strike, occupation, riot, mutiny, or government crisis occurs.
- The final social settlement or peace objective succeeds.
- No successful coup receipt exists.
- No Event 35 civil-conflict receipt exists.
- Emergency rule is absent at recovery completion.
- Stability meets the final tuned floor.

### Disqualifiers

- A permanent military or emergency government created by the crisis.
- Successful coup, separatist conflict, or Event 35 civil conflict.
- Debug incident clearing.
- Crisis ownership moved to another country.

### Tracking

Track major Social Collapse incident families, response outcomes, coup and civil-conflict receipts, emergency-government lifecycle, final settlement, stability, and recovery ownership. A baseline strike before Evolution II can count as history but cannot satisfy the required Social Collapse incident by itself.

### Icon direction

A reopened factory after a negotiated settlement, with workers and guards withdrawn from confrontation. Do not include readable document text.

## Achievement 5: Lean but Standing

### Mastery goal

Complete a liquidation-led recovery after accepting real Event 35 industrial loss while retaining national viability and avoiding political collapse.

### Required conditions

- Let the Market Clear or an approved liquidation-led route remains the final recovery philosophy.
- At least one center is consolidated, auctioned, or deliberately resolved through that route.
- At least one exact civilian or military factory level is lost through a validated Event 35 liquidation transaction.
- The country retains the protected industrial floor.
- No successful coup, separatist conflict, or Event 35 civil conflict occurs.
- Recovery proof succeeds for the same episode.

### Disqualifiers

- All industrial loss came from war, bombing, disaster, occupation, or another event.
- No real Event 35 industrial loss occurred.
- Doctrine switching or later program history removes liquidation-route ownership.
- Country falls below the protected viability floor.
- Debug completion.

### Tracking

Record the exact state, building type, amount, liquidation receipt, route ownership, national industrial floor, political-collapse receipts, and final recovery result. Final localisation should present survival after a harsh choice and should not praise unemployment or suffering.

### Icon direction

One surviving active plant beside closed capacity, with clear repair and continued production rather than triumphal imagery.

## Achievement 6: Recovery of Nations

### Mastery goal

Lead or materially support international recovery during The Second Great Depression while preserving the player's own national stability.

### Required conditions

- The Second Great Depression is active.
- The player performs a substantial validated set of aid, clearing, reconstruction, coordinated-demand, or supplier actions.
- At least one major recipient improves through the player's support.
- The player either recovers from Event 35 or remains below national conversion throughout the episode.
- The worldwide lifecycle reaches International Reconstruction.
- Final global recovery proof completes.
- No major Event 34 supplier collapse occurs during the final global proof period.
- The player country remains independent and valid.

### Disqualifiers

- Contribution transactions are refunded, duplicated, or registered after global recovery was already secured.
- The player triggers a critical supplier collapse during the final proof.
- The global episode is force-ended.
- The player is deleted, changes tags without valid continuity, or is a special actor outside normal civilian-system coverage.

### Tracking

Use the global episode ID, contribution receipts, major-recipient improvement receipts, player national state, final-stage entry date, supplier-collapse proof period, and recovery completion transaction. Current modifiers alone are not enough.

### Icon direction

Freight, port, rail, and factory activity returning across linked countries without a world-map graphic or handshake.

## Achievement implementation rules

Every achievement requires:

- Stable achievement ID.
- Game-rule and eligibility checks consistent with current Chaos Redux achievements.
- Episode receipts.
- Positive trigger.
- Disqualifiers.
- Save persistence.
- Final name and description.
- Icon triplet.
- Documentation.
- Test cases for positive and negative routes.

Do not implement achievements as a final-event option that fires automatically without verifying the whole episode.

## Acceptance scenario groups

The implementation is complete only after every applicable scenario below is tested through source inspection, HOI4 MCP evidence where supported, and the project's final user-run in-game validation path. This planning package does not claim that live testing has occurred.

## A. Targeting and entry

### `A-01`: Independent major target

- Several valid majors exist.
- Event 35 is selected automatically or through normal manual event firing.
- One exact major is chosen.
- One history row is recorded.
- Opening report, shock, category, Severity, phase, doctrine choice, and centers appear once.

### `A-02`: Player non-major target

- Player country is not a major.
- It remains eligible.
- Costs and center count scale to the smaller economy.
- The crisis remains severe and recoverable.

### `A-03`: Active Event 35 exclusion

- One country has Event 35 active.
- Independent target selection gives it zero eligibility.
- A consequence call deepens the existing crisis instead of creating a duplicate.

### `A-04`: Active Event 34 exclusion

- One country has Industrial Boom active.
- It cannot receive independent Event 35.
- Lighter contagion or global pressure uses Event 34 adapters.

### `A-05`: No valid target

- No major or player country passes normal civilian and industrial gates.
- Event list shows unavailable.
- No random country call or empty actor history is created.

### `A-06`: Negative Economy cluster actor

- Event 35 is selected as cluster anchor.
- Cluster uses one exact actor.
- Event 35 does not reroll another country.
- One global pacing event is counted.

## B. Opening and Severity

### `B-01`: Independent opening range

- Stable target begins in the intended severe but recoverable range.
- Opening shock is stronger than sustained penalties.
- No factory is deleted.

### `B-02`: Vulnerable opening

- Blockaded, unstable target with damaged industry begins higher.
- The cause list names material problems.
- Emergency actions remain payable.

### `B-03`: Dynamic drift cadence

- Panic and Economic Paralysis use a shorter bounded interval than Stabilization.
- Several normalized pulses under worsening conditions increase Severity gradually.
- Several normalized pulses under strong recovery lower it gradually.
- One ordinary pulse cannot resolve the entire crisis.
- Rescheduling never creates two active pulse receipts for one episode.

### `B-04`: Trend

- Rapid improvement, improvement, stable, worsening, and accelerating conditions are reproduced.
- Trend follows recent movement and shock memory.
- Save and load preserve correct trend history.

### `B-05`: Threshold crossings

- Every band changes intended modifiers and action availability.
- Crossing a threshold does not repeat its one-shot incident each pulse.
- Falling thresholds updates the category and phase proof correctly.

### `B-06`: Economic Paralysis

- Severity reaches `100`.
- Deepest modifier and emergency objective appear once.
- Country retains a viable emergency action path.
- Remaining at `100` does not repeat factory loss or aid.

### `B-07`: Relapse

- Country enters Stabilization.
- A new shock returns Severity to the Depression range.
- Stabilization proof resets.
- Opening shock does not reapply without a new source.

### `B-08`: Baseline political pressure

- Evolution II is disabled.
- Sustained Deep Depression creates an ordinary strike, radicalization event, or government crisis through valid conditions.
- No Evolution II movement registry or occupation system appears.

### `B-09`: Baseline National Breakdown

- Evolution II is disabled.
- Full National Breakdown conditions and a failed prevention objective make civil conflict a bounded possibility.
- Missing actor, territory, force, leader, or recent-war proof forces a nonwar political outcome.
- The event does not clone the national crisis onto every participant.

## C. Recovery doctrines

Run separate checkpoints for every doctrine.

### `C-01`: Emergency Public Works

- Major project consumes real resources.
- State and employment conditions improve.
- Interruption preserves valid partial work and prevents refund duplication.
- Final legacy reflects completed projects.

### `C-02`: Rescue Strategic Industry

- Vital center receives protection.
- Nonprotected sectors bear visible cost.
- Military output is preserved without free equipment.
- Rescue dependence can appear.

### `C-03`: Stabilize Finance and Trade

- Bank holiday and audit sequence works.
- Trade action requires valid routes and partners.
- Blockade makes inappropriate actions invalid.
- Durable credit reform requires completed prerequisites.

### `C-04`: Austerity and Retrenchment

- Fiscal pressure falls.
- Demand and social pressure rise.
- Route can succeed under strong conditions.
- Route carries severe Social Collapse risk under weak conditions.

### `C-05`: Direct State Planning

- Planning board opens coordinated actions.
- Nationalization or trusteeship targets exact center.
- Input rationing protects one sector and creates a cost elsewhere.
- Plan completion creates one bounded institution.

### `C-06`: Let the Market Clear

- Support withdrawal produces real short-term risk.
- Asset reorganization can succeed, partially succeed, or liquidate capacity.
- No repeated auction reward.
- Route remains viable only under suitable conditions.

### `C-07`: Doctrine switch

- Switch unavailable before cooldown.
- Switch pays real cost and creates policy whiplash.
- Completed action receipts persist.
- Repeated switching cannot farm rewards.

### `C-08`: Objective capacity

- No more than one main objective and two supporting missions appear.
- Economic Paralysis replaces ordinary missions.
- Obsolete actions hide.

## D. Depression Centers

### `D-01`: Small economy center count

- One meaningful state is selected.
- Costs and project duration scale correctly.

### `D-02`: Large major center count

- Two or three distinct high-value centers are selected.
- Selection does not default to capital-only or duplicate region.

### `D-03`: Local progression

- Distressed center can become Idled and Shuttered only after sustained pressure.
- Warning or objective appears before serious physical loss.

### `D-04`: Reopening

- Doctrine-specific project and supply requirements work.
- Reopened state lowers national pressure.
- No free building restoration occurs.

### `D-05`: State loss

- Active project pauses.
- National shock scales with industrial importance.
- Previous owner stops paying.
- New controller cannot duplicate reward.

### `D-06`: State regain

- Existing project and damage reconcile.
- Lost combat buildings do not return for free.

### `D-07`: Permanent transfer

- One live state record owner.
- Historical loss remains with original episode.
- New owner can adopt local burden through valid contract.

### `D-08`: Involuntary physical loss

- Requires Shuttered or Abandoned state, sustained exposure, failed recovery opportunity, and unused receipt.
- Per-state and per-episode caps hold.

### `D-09`: Deliberate liquidation

- Player receives short-term relief and permanent scar.
- Liquidated factory cannot be restored and rewarded in the same episode.

## E. Event 34 inheritance

### `E-01`: Baseline boom collapse

- Frozen snapshot accepted.
- Same country enters baseline Event 35.
- Boom bonuses are removed before depression penalties.
- Starting Severity reflects reserves and landing preparation.

### `E-02`: Evolution I collapse

- Financial Contagion activates when enabled.
- Speculative regions convert correctly.
- Disabled Financial Contagion remains off while severity inheritance remains.

### `E-03`: Evolution II collapse

- Enabled Evolutions I and II activate.
- Fragile Miracle Regions convert.
- Social Collapse module is ready without duplicate evolution records.

### `E-04`: Evolution III collapse

- Enabled Evolutions I, II, and III activate.
- Starting Severity is very high.
- Global episode starts or deepens once.
- Super-event receipt fires once on actual worldwide pressure.

### `E-05`: Existing Event 35

- Event 34 collapse deepens the same episode.
- Category, base modifier, and center registry are not duplicated.
- Evolution floor only rises.

### `E-06`: Duplicate transaction

- Second call with same collapse ID rejects safely.
- No duplicate shock, center, or history.

### `E-07`: Interrupted handoff

- Frozen snapshot remains recoverable.
- Boom actions stay closed after terminal collapse.
- Repair or cleanup does not leave mixed active modifiers.

### `E-08`: Deleted target

- Invalid target fails closed.
- Source registry cleans without creating a random replacement.

## F. Financial Contagion

### `F-01`: Exposure registry

- Strong, medium, and light relationships create one merged row per source-target pair.
- Invalid special actors are excluded.

### `F-02`: Secondary condition

- Exposed country receives qualitative pressure and compact actions.
- It does not receive the full Event 35 category immediately.

### `F-03`: Aid

- Provider pays exact resources.
- Origin Severity or exposure changes once.
- Refund and cancellation are symmetric.

### `F-04`: Abandonment

- Relationship closes.
- Origin receives one shock.
- Diplomatic and investment consequences apply.
- No repeated abandonment.

### `F-05`: Full conversion

- Vulnerable target converts after sustained Near Depression.
- Entry source, origin, depth, and episode are recorded.
- No random pacing event is counted.

### `F-06`: Anti-loop

- Origin cannot receive immediate return shock through the same link.
- Depth reduces pressure.
- One target converts once per origin episode.

### `F-07`: Origin recovery

- New exposure stops.
- Lighter conditions decay.
- Already converted countries remain active independently.

### `F-08`: Disabled evolution

- No new exposure or conversion.
- Cleanup does not grant rewards or alter baseline recovery.

## G. Social Collapse

### `G-01`: Organized protest

- Prolonged unemployment creates one valid movement.
- Country-specific political context shapes it.
- Player receives a bounded response set.

### `G-02`: Negotiated settlement

- Costs and concessions apply.
- Strike or occupation ends.
- Social condition improves.
- Durable settlement is recorded.

### `G-03`: Force response

- Command power remains within project limit.
- Equipment and manpower costs apply.
- Exact deaths use shared API.
- Repression can worsen later strain.

### `G-04`: Emergency government

- Correct government form is selected from valid institutions.
- Mandate mission opens.
- It returns power, becomes permanent through visible route, or fails.

### `G-05`: Coup without regional base

- Valid elite or military actor exists.
- Coup can occur.
- Civil war remains ineligible without territory.

### `G-06`: Separatist route

- Valid regional identity and package exist.
- Territory and force setup are coherent.
- If package is absent, autonomy or regional crisis replaces country creation.

### `G-07`: Civil war gate

- All extreme conditions are satisfied.
- Territory follows support and centers.
- Full national crisis is not cloned onto every participant.
- Shared war and death Chaos is not duplicated.

### `G-08`: Recent civil war block

- New Event 35 civil conflict has zero eligibility.
- Recovery and settlement remain available.

### `G-09`: Disabled evolution

- No Evolution II movement ladder, factory-occupation system, coup route, separatist conflict, or movement-specific civil war appears.
- Baseline strikes, radicalization, government crises, and the guarded National Breakdown chain remain functional.
- A baseline civil conflict still requires the full baseline gate and failed prevention objective.

## H. The Second Great Depression

### `H-01`: First global activation

- One global episode ID.
- One bounded world registration.
- One actual pressure package.
- One super-event receipt.
- One guarded Chaos source.

### `H-02`: Lighter pressure

- Stable country receives Global Contraction.
- Full Event 35 category does not open.
- Condition scales with exposure.

### `H-03`: Local conversion

- Highly exposed country converts.
- Stable self-sufficient country remains lighter.
- Entry source and global episode are recorded.

### `H-04`: Supplier boom

- Active Event 34 country receives world orders.
- Benefits and Overheating both change.
- AI and player can refuse further exposure.

### `H-05`: Supplier collapse

- Supplier enters or deepens Event 35.
- Dependent countries receive exact shocks.
- World stage deepens once.

### `H-06`: Global recovery

- Industrially weighted recovery advances stage.
- Final proof lasts required period.
- New major crisis pauses or resets proof.

### `H-07`: Global resolution

- Lighter pressure decays.
- Active national depressions remain.
- International agreements with a post-crisis role persist.
- Matching Chaos reversal is capped by recorded source.

### `H-08`: Existing global episode

- New Evolution III origin joins or deepens it.
- No second world registry or super-event.

### `H-09`: Disabled evolution

- No global pressure, super-event, or worldwide conversion.
- Inherited national severity remains valid.

## I. Repeatability and country changes

### `I-01`: Strong reform repeat

- Country recovers strongly.
- Safeguard blocks early independent refiring.
- Later episode starts with bounded reform benefit.

### `I-02`: Hollow recovery repeat

- Country retains scars.
- Later vulnerability rises within cap.
- Recovery remains possible.

### `I-03`: Civil war during active crisis

- One national episode owner remains.
- Center burdens divide by control.
- No duplicate categories across every small side.

### `I-04`: Annexation

- Active country cleanup removes arrays, decisions, exposure, and missions.
- No replacement target inherits the whole crisis at random.

### `I-05`: Release or successor

- A valid successor adopts local burden only through explicit state and country contract.
- History remains with original episode.

### `I-06`: Save and reload

- Severity, phase, trend, doctrine, centers, evolutions, exposure, world stage, missions, and receipts persist.
- Opening shock and threshold events do not repeat.

## J. Cluster, logs, and presentation

### `J-01`: Event list

- Event ID, name, type, Chaos level, and availability display correctly.
- No valid target shows `N/A`.

### `J-02`: Event history

- Independent firing has one pacing history row.
- Event 34, contagion, and global consequence entries do not create extra pacing events.
- Source remains visible in Event 35 details.

### `J-03`: Evolution history

- Each enabled evolution logs once with actor, date, tier, and stage.
- Disabled evolution does not set recorded flags.
- Event Details preview has no fake history date.

### `J-04`: Negative Economy cluster

- Low danger appears after cluster registry completion.
- Optional participation and selected-anchor behavior match part 8.
- Cluster counts one pacing event.

### `J-05`: Category clarity

- Player can identify Severity, trend, phase, doctrine, next threshold, center, and action without reading a long paragraph.
- Visible action and mission caps hold.

### `J-06`: Assets

- Every required asset has source, processed PNG, final DDS, sprite, consumer, manifest, and handoff.
- No placeholder, white halo, opaque icon square, modern prop, or wrong-era scene remains.

### `J-07`: Super-event

- Slot, title, description, reaction, quote, image, audio, settings-aware playback, docs, and workbook agree.
- Quote and audio rights are verified.
- No default or reused unapproved track.

### `J-08`: Writing

- No raw keys or implementation text.
- No hidden formulas or future spoilers.
- Dynamic countries and states resolve.
- Visible costs and requirements are clear.
- Project writing rules are followed.

## K. AI and probability

### `K-01`: Target scenarios

Run `TGT-01` through `TGT-10` with complete pools.

### `K-02`: Doctrine scenarios

Run `DOC-01` through `DOC-07` and confirm expected ordering.

### `K-03`: Action scenarios

Run `ACT-01` through `ACT-05`.

### `K-04`: Contagion scenarios

Run `CTG-01` through `CTG-10`.

### `K-05`: Baseline breakdown scenarios

Run `BDP-01` through `BDP-04` and confirm the baseline route remains compact, guarded, and distinct from Evolution II.

### `K-06`: Social scenarios

Run `SOC-01` through `SOC-05`.

### `K-07`: Global scenarios

Run `GLB-01` through `GLB-10`.

### `K-08`: Evolution timing

Run `EVO-01` through `EVO-08` with scheduled state changes.

### `K-09`: Incident pools

Inspect complete candidate pools in every Severity band and evolution state. Confirm no invalid incident receives weight and no generic incident dominates every context.

## L. Achievement tests

Every achievement needs:

- One positive scenario.
- One near-miss.
- One exploit attempt.
- One save and reload case.
- One disqualifier case.

No achievement should unlock from debug or manual force paths unless the project's existing achievement framework explicitly permits it.

## Completion evidence

Before Event 35 is called implemented, the final report must include:

- Files changed.
- Event IDs and new subevents.
- Scripted effects, triggers, constants, variables, flags, arrays, and event targets.
- Crisis API contract and rejection reasons.
- Event 34 snapshot version and field coverage.
- Decision and mission coverage.
- Doctrine route coverage.
- Depression Center lifecycle coverage.
- Evolution coverage.
- AI and probability comparison evidence.
- Cluster registry and workbook alignment.
- Chaos source and reversal receipts.
- Asset inventory and final runtime paths.
- Super-event research and wiring.
- Achievement coverage.
- Event log and Event Details coverage.
- Documentation and authoritative workbook updates.
- Accepted improvement addendum disposition.
- Task-specific validation findings.
- Every blocker, simplification, omission, fallback, substitution, or unimplemented requirement.

## Improvement-loop conclusion

The project custom-subagent runtime was unavailable, so `chaosx_improvement_loop_planner` could not be executed. Its supplied role definition was applied manually to the assembled package as a final depth and anti-bloat review.

The manual result is closure. The six recovery philosophies, Depression Centers, guarded baseline National Breakdown, Financial Contagion, Social Collapse, The Second Great Depression, the Event 34 handoff, AI scenarios, assets, achievements, and acceptance cases form a complete implementation target. Another broad planning expansion before implementation would add bloat.

The next executable improvement-loop pass belongs after a meaningful implementation tranche, when actual decisions, state logic, and evolutions can be compared with the design. That pass should either produce a bounded addendum for a concrete implemented weakness or recommend closure when the event is connected, readable, replayable, and complete.

It should not add another public meter, a full focus tree, automatic custom countries, 3D models, a permanent scripted GUI, or extra global systems without a new accepted gameplay need.

## Planning completion statement

The planning package is complete when all files in the manifest exist, cross-references resolve, the consolidated specification includes every part, and the package passes the content audits. Planning completion does not claim gameplay implementation, final assets, subagent execution, HOI4 MCP evidence, workbook changes, or live game validation.
