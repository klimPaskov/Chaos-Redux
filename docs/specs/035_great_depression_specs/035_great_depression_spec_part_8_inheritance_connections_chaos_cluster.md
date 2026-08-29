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
