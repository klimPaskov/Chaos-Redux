# Event 037 balance matrix

## Purpose

This file defines planning anchors for population creation, pressure, recovery, and exploit control. Final values must be validated against the installed state-population distribution and the full shared Famine, Migration, Deaths, construction, and recruitment mechanics.

The goal is a useful baseline manifestation, a major Evolution I opportunity, a dangerous Evolution II crisis, and an extreme Evolution III demographic transformation.

## Grant model

For pre-fire state population `P`:

1. Calculate the stage ratio grant.
2. Calculate a practical floor equal to the smaller of the nominal floor and the state's small-state ceiling.
3. Use the larger of ratio grant and practical floor.
4. Apply the per-state cap.
5. Round to whole people.

```text
practical floor = minimum of nominal floor and P multiplied by local ceiling
grant = minimum of stage cap and maximum of P multiplied by stage ratio and practical floor
```

## Planning values

| Stage | Ratio | Nominal floor | Per-state cap | Small-state ceiling |
| --- | ---: | ---: | ---: | ---: |
| Baseline | `2.5%` | `1,000` | `1,500,000` | `5%` |
| Evolution I | `6%` | `2,500` | `3,000,000` | `10%` |
| Evolution II | `12%` | `5,000` | `7,500,000` | `20%` |
| Evolution III | `25%` | `10,000` | `20,000,000` | `40%` |

## State examples

| Pre-fire population | Baseline | Evolution I | Evolution II | Evolution III |
| ---: | ---: | ---: | ---: | ---: |
| `5,000` | `250` | `500` | `1,000` | `2,000` |
| `20,000` | `1,000` | `2,000` | `4,000` | `8,000` |
| `100,000` | `2,500` | `6,000` | `12,000` | `25,000` |
| `1,000,000` | `25,000` | `60,000` | `120,000` | `250,000` |
| `5,000,000` | `125,000` | `300,000` | `600,000` | `1,250,000` |
| `20,000,000` | `500,000` | `1,200,000` | `2,400,000` | `5,000,000` |
| `60,000,000` | `1,500,000` | `3,000,000` | `7,200,000` | `15,000,000` |
| `100,000,000` | `1,500,000` | `3,000,000` | `7,500,000` | `20,000,000` |

## Intended interpretation

### Baseline

- Small inhabited states grow by a noticeable local share without an absurd fixed minimum.
- Normal industrial states gain tens or hundreds of thousands.
- Very large states can reach the `1.5` million cap.
- Stable countries should usually absorb the first manifestation with limited investment.

### Evolution I

- The increase changes national development priorities.
- Small islands and rural states remain locally bounded.
- Large states can gain millions.
- Housing and services become meaningful before Famine is inevitable.

### Evolution II

- One firing can destabilize food and transport.
- Most uncapped states gain close to `12%`.
- Poor, damaged, blockaded, and refugee-heavy states can enter genuine crisis.
- Prepared countries can preserve the advantage.

### Evolution III

- Most uncapped states gain roughly one quarter of population.
- The largest states still gain tens of millions within caps.
- Repeated firings can make mysterious people a majority.
- The world faces extreme food, construction, settlement, and political pressure.

## World-impact review

For a representative 1936 setup, record:

- total valid states
- total qualifying population
- total population created at each stage
- created population as a share of pre-fire world population
- states affected by the practical floor
- states affected by the cap
- largest and smallest grants
- countries crossing each pressure threshold
- first-month and first-year Famine and Migration outcomes without intervention

Expected character:

| Stage | Intended world effect |
| --- | --- |
| Baseline | several percent of qualifying population, usually manageable in stable states |
| Evolution I | large surge requiring widespread capacity work |
| Evolution II | crisis-scale increase creating Famine and Migration risk |
| Evolution III | extreme increase transforming world demographics |

If baseline is too weak to change play, raise ratio or cap. If it causes immediate universal Famine in a stable setup, reduce first-order pressure or grant scale while retaining real population.

## Repeat compounding

For an uncapped state with no deaths or migration:

| Stage | After one firing | After two | After three |
| --- | ---: | ---: | ---: |
| Baseline `2.5%` | `102.5%` | `105.1%` | `107.7%` |
| Evolution I `6%` | `106%` | `112.4%` | `119.1%` |
| Evolution II `12%` | `112%` | `125.4%` | `140.5%` |
| Evolution III `25%` | `125%` | `156.3%` | `195.3%` |

The shared repeatable-event weight provides frequency control. Do not add a hidden grant-reduction factor that makes later firings feel false.

## Pressure scale

| Stage | Range | Intended response |
| --- | --- | --- |
| Absorbing | `0` to below `20` | exploit workforce, invest selectively, maintain integration |
| Strained | `20` to below `40` | begin housing, service, agriculture, or settlement work |
| Overcrowded | `40` to below `60` | commit real resources and coordinate humanitarian systems |
| Emergency | `60` to below `80` | prioritize relief, routes, redistribution, and crisis missions |
| Breakdown | `80` to `100` | prevent sustained mortality, forced movement, repression, or collapse |

## Pressure behavior tests

- One tiny catastrophic state raises concern but cannot place a huge country at Breakdown alone.
- A capital or major industrial state at Breakdown materially affects national pressure.
- Many moderate states can create national crisis.
- High mysterious share with strong food, housing, and transport can remain manageable.
- Low mysterious share in a bombed, blockaded, starving state can still be severe.
- Settlement shifts pressure according to real origin and destination capacity.
- Deaths lower demand, but event text identifies mortality or atrocity as the cause.

A useful aggregation shape is a population-weighted average plus a smaller worst-state component. Final weights require scenario evidence.

## Demographic-dividend balance

Desired behavior:

- no full dividend before meaningful integration
- benefit scales with integrated population
- spare capacity and low pressure strengthen it
- Overcrowded pressure largely neutralizes it
- Emergency and Breakdown replace it with strain
- excluded, trapped, starving, or imprisoned people cannot produce full benefit
- recruitment benefit arrives after integration

Compare construction, production, and recruitable manpower before firing, immediately after firing, and after integration for a minor and a major country. Check threshold oscillation and stacking with existing economic modifiers.

## Project-cost balance

### Housing

- affordable enough to save an important state
- expensive enough that every state cannot be solved instantly
- slower and costlier after bombing or repeated manifestations
- permanent capacity only after completion

### Transport and utilities

- uses trains or trucks where appropriate
- uses fuel where motor transport matters
- competes with military logistics in war
- weak without a valid route connection

### Services

- improves integration and pressure
- requires real civilian or support capacity
- responds to occupation, Famine, and state damage

### Planned settlement

- cost follows cohort, distance, route, and destination preparation
- no movement without a valid Migration result
- failed preparation can consume real resources without deleting people

### New cities

- major Evolution III program
- long duration and major construction commitment
- durable state development
- no city-scale name for a small temporary modifier

## Direct Chaos balance

| Milestone | Chaos |
| --- | ---: |
| First manifestation | `+2` |
| Living mysterious population reaches `1%` of world population | `+2` |
| Reaches `5%` | `+3` |
| Reaches `10%` | `+5` |
| Reaches `25%` | `+10` |
| One firing creates at least `5%` of pre-fire world population | `+5` once |

Indirect Chaos through deaths, famine, displacement, wars, and atrocities remains with shared systems.

The recovery milestone removes `2` Chaos only after a proven crisis and a full stable year. It cannot repeat without a new material crisis.

## Exploit controls

### Population duplication

- one state transaction per firing
- applied results saved before reports
- delayed reports do not reapply
- cluster and multiplayer presentation cannot duplicate

### Manpower

- real population appears immediately
- full military use waits for integration
- conscription cannot bypass integration
- integration delay does not protect civilians from ordinary mortality

### Construction

- mysterious houses do not grant strategic buildings
- housing and cities need costs and time
- temporary capacity does not become permanent without completion

### Settlement

- Migration owns origin debit and destination credit
- Event 037 moves provenance from proven results
- failed and trapped cohorts remain accounted for

### Pressure farming

- no repeated reward for threshold oscillation
- one-shot flags persist
- mission rewards require active work
- dividend follows sustained integration and capacity

### Atrocity as economic policy

- population loss can reduce pressure
- atrocities create resistance, Condemnation, sanctions, evidence, isolation, labor loss, and history
- viable support actions dominate ordinary incentives
- systematic killing cannot be the cheapest general response

### Donor and reception abuse

- donors cannot send missing resources
- destinations inherit real pressure
- aid can create dependency and cooldowns
- one cohort cannot be promised to several destinations

## Required balance cases

1. Stable industrial major after baseline.
2. Small island after baseline.
3. Poor agrarian state after Evolution I.
4. Blockaded island at Evolution II.
5. Major at world war during Evolution II.
6. High-capacity Evolution III country building cities.
7. Damaged Evolution III country at Breakdown.
8. Forced relocation.
9. Systematic killing.
10. Three firings without intervention.
11. Three firings with strong intervention.
12. Ownership transfer after each major transaction.
13. Mysterious-majority state hit by famine, bombing, and migration.
14. Nonhuman actor controlling otherwise valid territory.
15. Multiplayer with several human reports from one firing.

## Balance acceptance

Balance passes when baseline creates a clear benefit, Evolution I changes investment, Evolution II creates serious but avoidable crisis, Evolution III transforms demographics while rewarding preparation, state size bounds work, no transaction duplicates population, mass death is not the dominant cheap strategy, AI ordering matches named scenarios, and shared repeatable frequency remains authoritative.
