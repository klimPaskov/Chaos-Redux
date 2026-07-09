# Values and Pressure Model Matrix

## Core national values

| Value | Meaning | Increased by | Reduced by | Unlocks or changes |
| --- | --- | --- | --- | --- |
| `camp_network_reach` | Size of active national network | building active sites, expansion decisions, country-specific escalation | dismantlement, defeat, discovery cleanup, reform | higher labor output, higher deaths, more evidence |
| `camp_labor_output` | Forced-labor economic pressure | labor quotas, colonial extraction, gulag quotas | reform, low supply, overreach, dismantlement | construction, resources, infrastructure |
| `camp_coercive_control` | Short-term repression/control | guard allocation, harsh occupation policy | low manpower, low equipment, reform | resistance suppression, hardliner pressure |
| `camp_population_loss_index` | Monthly harm intensity | expansion, radicalized sites, experiments, famine, contamination | relief, dismantlement, inspection, supply | Deaths tab, state population loss |
| `camp_resistance_pressure` | Future unrest and sabotage pressure | network size, evidence, harsh quotas, non-core states | reform, relief, negotiated settlement | uprisings, sabotage, occupation cost |
| `camp_stability_damage` | National political damage | large networks, democratic legitimacy damage, discovery | reform, propaganda, hardliner control, dismantlement | stability loss, crisis events |
| `camp_evidence_level` | Discoverable evidence depth | site type, contaminated evidence, experiments, failed cover-up | successful partial destruction, inspection handover | condemnation, tribunal severity |
| `camp_overstretch` | Guard, rail, and administrative strain | site count, harsh quotas, war pressure | guard resources, trains, administrators, dismantlement | breakdown events, efficiency loss |
| `camp_foreign_visibility` | Foreign evidence pressure | occupied foreign states, diplomats, enemy approach, refugees | closed authoritarian state, censorship, destroyed evidence | discovery without direct conquest |
| `camp_tribunal_severity` | Post-defeat accountability | discoveries, evidence depth, deaths, contamination | reform, preserved evidence, early dismantlement | trials, sanctions, leader removal |
| `camp_hardliner_pressure` | Extremist faction lock-in | radicalized escalation, SS/NKVD/Kwantung authority | reform, purges, regime change | ideology drift, coup pressure |
| `camp_democratic_legitimacy_damage` | Democratic route penalty | democratic use of camps, emergency relocation, colonial detention | court review, redress, dismantlement | democratic support loss, court events |

## State pool order

1. Occupied non-core states.
2. Colonial or subject controlled states.
3. Non-core owned states.
4. Country-specific borderland or periphery groups.
5. Core fallback with lower output and higher internal damage.

## Site types

| Site type | Output | Damage | Discovery severity | Notes |
| --- | --- | --- | --- | --- |
| Dormant infrastructure | none | none | none | historical marker only |
| Active detention site | low control, low labor | low monthly loss | low to medium | base active layer |
| Expanded labor site | medium labor and control | medium monthly loss | medium | main management layer |
| Gulag network | resource/construction pressure | medium to high | medium to high | Soviet-specific mechanics |
| Experiment-linked site | research pressure | high | high | Germany and Japan hooks |
| Radicalized atrocity site | hardliner pressure only | severe | severe | mostly negative |
| Contaminated restricted site | none or minimal | severe plus contamination | extreme | consequence branch, no efficiency mechanics |

## Dynamic death factors

Use central constants and helper effects. Do not scatter fixed values.

Factors:

- state population
- site type
- network reach
- network overreach
- occupied or non-core status
- famine pressure
- experiment permission level
- biowarfare or contaminated site flags
- guard allocation
- supply and rail strain
- high chaos tier
- retreat or cover-up decisions
- reform or relief decisions

## Resource costs

Expansion should use a varied cost palette:

- trains
- infantry equipment
- support equipment
- trucks
- manpower
- command power
- army XP for military-police organization
- civilian-factory burden
- fuel for remote logistics
- stability
- war support
- local compliance or autonomy pressure
- state control requirements

Political power can be part of costs, but not the whole design.
