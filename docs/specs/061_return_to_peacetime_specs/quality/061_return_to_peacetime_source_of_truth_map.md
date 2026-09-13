# Event 061 source-of-truth map

## Purpose

This map prevents the source specification, implementation, documentation, workbook, and generated catalog exports from drifting apart.

## Authority order

| Question | Authoritative source after implementation |
| --- | --- |
| Event identity and accepted design | Event 61 source specifications in this directory, updated only through an accepted design change |
| Actual gameplay behavior | Final event-owned and shared scripted source files |
| Exact tuning constants | Event 61 script constants and verified implementation documentation |
| Current event status and catalog metadata | Authoritative event XLSX workbook |
| CSV catalog files | Generated exports from the workbook |
| Player-facing wording | Final localisation files |
| Asset paths and sprites | Final `.gfx`, consumer source, and permanent asset documentation |
| Probability behavior | Current AI source plus saved HOI4 probability evidence |
| Event history behavior | Event Logs source and scripted localisation |
| Peace cluster execution | Cluster registry source plus authoritative workbook row |
| Achievement rules | Single achievement registry plus Event 61 tracking source |
| Historical design grounding | Event 61 historical research note |
| Temporary subagent findings | Handoffs under the Event 61 plan directory until resolved and promoted |

## Source specification role

The source specification defines required behavior and acceptance boundaries.

Implementation may adjust exact balance values only when:

- engine limits require a change
- probability evidence shows a target is wrong
- live balance proves a value harmful
- the change preserves the core event promise
- the final documentation records the implemented value
- the completion report identifies the deviation

A coding agent cannot silently remove a route, evolution response, achievement, asset, or anti-exploit rule for convenience.

## Generated catalog rule

The three CSV catalog files are generated snapshots.

Workflow:

1. edit authoritative XLSX
2. run `python .tools/export_event_catalog_csv.py`
3. review generated CSV diff
4. commit workbook and generated exports together

Do not treat an edited CSV as the source of truth.

## Design and implementation crosswalk

| Design surface | Source spec | Expected implementation authority | Documentation authority |
| --- | --- | --- | --- |
| Baseline global transaction | Part 1 | Event 61 entry and baseline effects | Event 61 overview |
| State factory ledger | Parts 1, 2, 5, 7 and ledger diagram | Event-owned state effects and triggers | Event 61 factory-ledger system doc |
| Law ladders and restore targets | Parts 1, 2, 5, 7 | Shared or event-owned law helpers and law definitions | Event 61 laws doc |
| Industrial Reconversion Shock | Parts 1, 5, 7 | Event-owned ideas and scheduler | Event 61 effects doc |
| Readiness | Part 2 and lifecycle diagram | Event-owned calculation effect and scripted localisation | Return to Rearmament doc |
| Decisions and missions | Parts 2 and 3 | Event-owned decision files | Decision-system doc |
| Evolution I | Part 3 | Event chain, stockpile helpers, ideas | Evolution doc |
| Evolution II | Part 3 | Event chain, safe unit selector and disband | Evolution doc |
| Evolution III | Part 3 | Event chain, law definitions, recovery decisions | Evolution and law docs |
| AI | Part 4 and probability scenarios | Decision weights, strategy, triggers | AI handoff and probability evidence |
| Cross-event behavior | Part 4 | Shared helpers and narrow event hooks | Event integration matrix |
| Balance and exploits | Part 5 | Script constants, guards, tests | Validation report |
| Presentation | Part 6 and localisation handoff | Localisation, GFX, assets, consumers | Event and asset docs |
| Achievements | Part 6 and achievement prompt | Achievement registry and tracking effects | Achievement docs |
| Cluster | Parts 1, 4, 7 and catalog handoff | Cluster registry | Cluster docs and workbook |
| Event Logs | Parts 1, 6, 7 | Event Logs effects and selectors | Event Logs docs |

## Temporary workspace rule

Temporary event asset and subagent workspaces can hold research, source files, previews, and handoffs while work is active.

Before full completion:

- promote durable facts into event, system, asset, achievement, probability, or plan documentation
- verify no runtime path points into a temporary docs workspace
- remove only the Event 61 temporary workspace that is fully accepted
- preserve reusable skill reference libraries and unrelated workspaces

## Deviation record

Any implementation deviation needs:

- source requirement
- implemented behavior
- reason
- engine or balance evidence
- affected files
- player-facing effect
- accepted reviewer or owner decision

Place the record in the Event 61 implementation plan and summarize it in the final completion report.

## Completion truth

A feature is complete only when source, assets, localisation, documentation, workbook, generated exports, probability evidence, and validation agree.

A parser pass alone does not make the event complete.

A finished source specification does not mean the gameplay implementation exists.
