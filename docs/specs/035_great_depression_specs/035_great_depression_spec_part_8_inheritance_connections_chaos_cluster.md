# Great Depression 2.0 specification, part 8: Event 34 inheritance, connections, Chaos, and cluster behavior

Status: the Event 34 handoff, evolution floor, deepening, inherited-liability pressure, the famine, migration, contamination, sanction and Event 21 connections, the Chaos receipts, cluster registration and the Event Log rows are `implemented` in source.
The disaster adapter is pending and the inherited hidden-row work is `rejected`.

## Event 34 relationship

Event 35 is the direct failure state of Event 34 Industrial Boom.
The relationship is a consequence contract between two separate events.
Event 34 owns the boom until the collapse transaction begins.
Event 35 owns the depression from the moment the handoff commits.

The handoff must preserve enough history to make a failed boom feel different from an independent depression.
It must also remain bounded.
Event 35 receives a frozen collapse snapshot once, converts it into depression state, and then continues from its own ledger.
It must not keep reading mutable Event 34 working variables after Event 34 cleanup.

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

Event 35 should consume only fields that were supplied and validated.
Missing optional fields use safe neutral defaults.
Missing required target, source, episode, evolution, final Overheating, or one-shot proof rejects the handoff.

The current Event 34 freezer supplies the national fields and one legacy primary region, plus optional per-region fields when they exist.
Event 34 has no producer for authentic per-region project facts, corridor membership or secured-value amounts, so Event 35 cannot honestly consume them yet and must not manufacture them.
Event 35 adopts inherited regions as ongoing hidden national pressure (implemented inherited-liability consumer, decision D4).

## Evolution inheritance

The inheritance floor is direct.

| Industrial Boom state at collapse | Event 35 active evolution floor | Opening depression character |
| --- | --- | --- |
| Baseline | Baseline | Severe national contraction |
| Evolution I Speculative Mania | Evolution I Financial Contagion | Severe contraction with exposed credit and trade links |
| Evolution II The Industrial Miracle | Evolutions I and II | Deep contraction with fragile miracle regions and immediate social pressure |
| Evolution III Runaway Industrialization | Evolutions I, II, and III | Very high Severity with worldwide depression active from the opening |

The inherited level is a floor.
Event 35 may later evolve further when campaign conditions allow.
It may not downgrade the inherited state because the global tier fell after the collapse.

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

An Event 34 collapse can reach Severity `100` only through an additional proven catastrophic condition, such as extreme final Overheating, exhausted reserves, failed emergency landing, and major regional damage.
Evolution III alone should not force the exact maximum because the player still needs room to see the worsening trend and respond.

## Conversion of Industrial Regions

Event 34 regions become priority Depression Center candidates.

### Protected and completed regions

A protected region with completed or nearly completed work begins with lower local depression pressure.
It may retain infrastructure, railway, resource, or production knowledge that can be salvaged through recovery.
It does not automatically receive a permanent reward.

### Fragile miracle regions

A high-output region with weak logistics, heavy credit exposure, or labor exhaustion begins as a deep Depression Center.
Temporary shutdowns and unemployment should replace the boom bonuses immediately.
Physical building loss remains a later consequence.

### Unfinished projects

An unfinished project becomes one of:

- An abandoned works site.
- A stranded industrial order book.
- A credit-frozen plant network.
- A partially usable transport project.
- A salvageable public works foundation.

The project can be completed, restructured, liquidated, or abandoned through Event 35.
Failed Event 34 work never becomes free factories or building slots.

### Evolution III spread corridors

Runaway Industrialization states remain linked by a corridor receipt.
Event 35 can select a small number of the most important states as visible Depression Centers and keep the rest as hidden corridor liabilities.
Recovery can restore the corridor, break it into regional networks, or leave permanent disconnected scars.

Disposition `rejected` (2026-10-10 parent acceptance): paid actions on hidden rows, corridor restoration and breakup, secured-value salvage and multi-region priority are not built.
Hidden corridor states stay national inheritance pressure, and corridor recovery runs through the visible centers.
Event 34 delivers its Industrial Regions and spread states as authentic registered rows (role primary or corridor) through `great_depression_register_inherited_region`.

## Reserve conversion

Event 34 reserves are not carried forward as a permanent second currency.

At collapse:

- Strong reserves absorb part of the immediate efficiency and confidence shock.
- Limited reserves protect one selected center or finance one emergency action.
- Depleted reserves provide no opening protection.
- Reserve abuse or duplicate consumption is blocked by one-shot receipts.

After conversion, the reserve state becomes Event 35 history.
Event 35 recovery uses its own action costs and commitments.

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

The collapse does not create a second global pacing event.
The original Event 34 firing remains the pacing event.
Event 35 deepening is a consequence.

## Reusable crisis entry contract

Event 35 exposes one public country-scope entry point, `great_depression_start_or_deepen` in `common/scripted_effects/035_great_depression_effects.txt`, documented in `035_great_depression_effects.md`.

The entry point supports:

- Independent Event 35 selection (through the private `chaosx.nr35.9` receiver, which keeps the chosen country).
- Event 34 collapse.
- Evolution I full-crisis conversion.
- Evolution III national conversion.
- Relapse after a completed episode.
- A future approved external economic-shock caller.

It must not become a generic route for unrelated events to apply arbitrary penalties without supplying a valid source, target, severity profile, and one-shot receipt.

The complete proposed input and output surface appears in `035_great_depression_reusable_crisis_api.md`.

## Connections

A connection belongs here only when it changes a player decision or a consequence another system owns.
Event 35 never writes another system's internal state; it submits a validated request to the owner's public adapter or reads the owner's public trigger.

| Connection | Direction | What it does | Status |
| --- | --- | --- | --- |
| Event 34 Industrial Boom | Both | Collapse starts or deepens Event 35; surviving booms quote and join reconstruction as suppliers; supplier collapse is a global shock | `implemented`; supplier choices pending (part 7) |
| Famine | Event 35 to famine | A hollowed or abandoned center at Systemic Breakdown or worse submits one bounded food-pressure request per state and crisis (`great_depression_submit_humanitarian_center_pressure`); the famine owner decides whether a food problem exists and owns every death | `implemented` |
| Migration | Event 35 to migration | The same center failure submits one bounded flight request per state and crisis; migration owns cohorts and transfers | `implemented` |
| Famine | Famine to Event 35 | A Depression Center where the famine owner reports a visible food problem (`famine_state_has_visible_food_problem`) adds one point of hidden demand and one of social stress per update, holds reopening certification while it lasts (the project pauses and fails after `28` days of continuous hold), and is the only place the hunger-riot incident can occur | `implemented` |
| Event 21 Random Civil War | Event 35 to Event 21 | National Breakdown and Social Collapse hand a proven outcome to the Event 21 opening adapter, which owns route, forces, war and Deaths; a rejected admission becomes a non-war outcome | `implemented` |
| Occupation and state loss | Shared to Event 35 | A native control change records a major industrial state loss for targeting and pauses or transfers center work; the occupation profile is read through the famine owner | `implemented` |
| Event 50 The Great Embargo and condemnation | Shared to Event 35 | An active condemnation sanction against a depressed country (`great_depression_trade_isolation_is_active`, which Event 50 will join when it ships) adds hidden trade stress and makes the Finance and Trade doctrine pay 25% more convoys and political authority; Event 50 adds isolation pressure without a second depression penalty (Event 50 part 8) | `implemented` for condemnation sanctions |
| Natural disasters and Acid Rain | Shared to Event 35 | A confirmed disaster loss in a center gives one economic shock per incident and can interrupt project proof; disaster damage is never an Event 35 factory-loss receipt and reopening never repairs it | pending |
| Air contamination, CBRN and fallout | Shared to Event 35 | A center inside a state with severe chemical contamination or the fallout modifier cannot certify reopening until the owner clears it; no extra pressure number is added | `implemented` |
| Black Friday cost discounts | Shared to Event 35 | A shared discount may lower purchase-style inputs only; tied civilian factories, mission time, output sacrifice and risk stay | guard only |
| Readers of Event 35 | Event 35 to others | The public read is `great_depression_has_active_crisis`; Event 39 currently reads the `great_depression_active` flag directly, and the Event 44 and Event 50 specs plan to read the active crisis; Event 35 publishes no other cross-event value | `implemented` for Event 39 |

Rejected as decoration:

- Random Riches and resource booms: no owner adapter exists, and an export-opportunity modifier would not change a depression decision.
- Camps and forced labor: Event 35 creates no detention, labor or camp route, and the camp rework owns those systems.
- Event 35 casualties from security responses: see part 6, Deploy Security Forces.

### Event 34 interaction rules

Event 34 can interact with Event 35 in three directions:

- A failed boom starts or deepens Event 35.
- A surviving boom can sell into depressed markets during Financial Contagion or Evolution III.
- Extraordinary global demand raises Event 34 Overheating through a public adapter owned by Event 34.

Event 35 never writes Event 34 internal Overheating directly.
It submits a validated pressure request and reads the returned result.

### Disaster rules

The player chooses whether to preserve an existing recovery project through disruption or redirect the center toward its permitted restructuring or liquidation route.
Completion must still prove the project's current requirements.
A reopened economic center may retain [Acid Rain](../033_acid_rain_specs/specs/033_acid_rain_spec_part_4_mortality_damage_and_environment.md) aftermath, and clearing rain aftermath alone does not certify economic recovery; [its recovery rules](../033_acid_rain_specs/specs/033_acid_rain_spec_part_5_preparedness_decisions_and_recovery.md) remain authoritative.
If an incident was already included in an Event 34 collapse snapshot, it is inherited condition rather than a second arrival shock.
Acceptance case: corrosion hits a center during certification after a boom collapse; the inherited old damage is not charged again, new damage can interrupt proof, and reopening grants neither a replacement factory nor clearance of Acid Rain aftermath.

### War and peace

War can support military demand while damaging civilian recovery.
Occupation, bombing, rail damage, port loss and industrial-state loss raise pressure through proven state and country conditions.
Peace can remove military demand and expose hidden unemployment, and can also restore trade access and reduce transport damage.
No universal war or peace modifier ignores these conditions.

## Conflict precedence

When several economic effects are active, ownership must remain clear.

| Situation | Owning rule |
| --- | --- |
| Event 34 active, Event 35 inactive | Event 34 owns the boom and Overheating |
| Event 34 crashes | Event 34 freezes and transfers, Event 35 owns the resulting crisis |
| Event 35 active, Event 34 selected independently | Target is invalid for a new boom |
| Event 35 active, new Event 34 collapse occurs | Event 35 deepens in place |
| Several contagion sources reach one country | Event 35 merges exposure by source receipts and converts once |
| Evolution III reaches a country already depressed | Global pressure modifies the existing crisis without a duplicate national package |
| Humanitarian crisis overlaps | Famine and migration own food, cohorts, population and deaths |
| Sanctions overlap | Condemnation and Event 50 own sanctions and enforcement |
| Disaster overlaps | Event 13 and Event 33 own disaster damage and aftermath |
| Civil war | Event 21 owns route, forces, war and deaths; Event 35 owns the one civil-conflict Chaos receipt while no shared counter records civil wars |

## Chaos accounting

Event 35 changes global Chaos only for a concrete abnormal outcome that no shared counter already records.
Eligibility, evolution availability and activation, phase movement, Severity drift, decision clicks, modifier refreshes and threshold display add zero.
Every non-zero entry goes through the shared Chaos Meter and Chaos History path with the event, episode, country, cause and a one-shot receipt, and respects the Chaos-meter-disabled setting.

For scale, the shared meter uses tiers of 200 points with a monthly decay of 1, a major war declaration adds 5, a major coup 3, a major annexation 10 and the first nuclear use 10.

| Outcome | Implemented change | Receipt | Audit finding |
| --- | ---: | --- | --- |
| Independent or inherited opening | `0` | None | Correct |
| Evolution activation | `0` | None | Correct |
| Sustained Economic Paralysis consequence | `+1` | One per episode | Below notice; keep only as a history marker or raise to `+2` |
| Contagion conversion into a full depression | `+2` once per spreading chain and one `+3` milestone at the chain's third conversion | One per chain (the global chain ledger keeps the 16 most recent chains) | Several conversions of one chain no longer pay again |
| Social Collapse outcome (coup success, rejected autonomy, non-war breakdown, failed response) | `+2` | One per episode | Correct: the Event 35 coup changes the government through `set_politics` and does not fire the shared coup or ideology counters |
| Civil conflict caused by the crisis | `+3` | One per episode | Correct today: the shared civil-war counter is commented out and Event 21 adds no Chaos of its own; re-check if either starts counting civil wars |
| First worldwide wave of Evolution III | `+10` | One per global episode | The scale of the first nuclear use |
| Supplier boom collapse | `+2` | One per global episode | Correct |
| Recovery conference failure | `+2` | One per global episode | Correct |
| International recovery ends the worldwide episode | up to `-10` | One per global episode, capped by recorded Event 35 global Chaos | Correct; scale with the wave if the wave changes |
| Strong national recovery after Event 35-owned paralysis | `0` | None | The earlier 2-point relief was too small to notice and is removed |

The civil-conflict receipt is the only Chaos record of a crisis-caused civil war, so it must become `0` in the same change that enables a shared civil-war counter or an Event 21 Chaos payment.

Exploit rules:

- Crossing a threshold repeatedly, reloading, or transferring a center cannot replay a receipt.
- Several contagion sources converting one country produce one conversion amount.
- Recovery never removes generic war, death, contamination, condemnation or another event's Chaos, and never more than Event 35 recorded.

## Negative Economy cluster

The accepted catalog assignment places Event 35 in the `Negative Economy` cluster as a `Low` member.

Implemented: Negative Economy is cluster ID 10, a one-time cluster at Chaos level 1, with Event 35 as its required Low trigger row and Event 50 The Great Embargo as its optional Medium row.
A cluster pick chooses one weighted country that is not already in a depression and keeps the cluster's pacing lane, and the cluster is unavailable with the same reason as the event when no valid country exists.

Cluster behavior should follow these rules:

- Event 35 remains independently eligible at Chaos level 1.
- Cluster membership does not change the direct Event 34 failure path.
- A cluster firing that includes Event 35 counts as one global pacing event.
- Event 35 still records its own country, entry source, Severity, evolution state, and repeat history.
- A country already in Event 35 is skipped as an independent cluster target unless the cluster explicitly calls the reusable deepening contract with a valid reason.
- Event 34 collapse does not trigger the whole Negative Economy cluster.
- Evolution III worldwide spread does not replay the cluster.
- Member severity `Low` describes the baseline cluster role. It does not cap evolved consequences.

The cluster should not become a simultaneous pile of full national economic crises without country separation, actor validity, or recovery capacity.
Member ordering and compatibility require an implementation-stage cluster audit.

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
