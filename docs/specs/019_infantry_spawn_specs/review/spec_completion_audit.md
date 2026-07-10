# Event 19 Planning Completion Audit

## User requirement coverage

| Requirement | Coverage | Source files |
| --- | --- | --- |
| One basic division on almost every controlled state with diminishing large-country tradeoff | Complete design | Parts 1 and 2, spawn matrix |
| Random irregular, cavalry, infantry, artillery, and support types | Complete design | Part 2, spawn matrix |
| Evolution I stronger organization, equipment, and templates | Complete design | Part 3 |
| Evolution II more units per state, armor, mechanized, armored cars, helicopters where valid, and weird lots | Complete design | Part 3, spawn matrix |
| Wartime countries can receive stronger units | Complete design with burden | Parts 1 and 3 |
| Supply strain, command confusion, training penalties | Complete design | Parts 1, 2, and 7 |
| Flavor events with real effects | Complete incident families | Parts 2, 3, and 4 |
| Decision category and random on-demand units | Complete design | Parts 3, 4, and 7, decision map |
| Evolution III no normal automatic unit by default | Complete design | Part 4 |
| Fully random battalions, counts, and support | Complete design with safety rules | Part 4, spawn matrix |
| Possessed generals, demands, revolt | Complete design | Part 4, general matrix |
| Twenty scary generic portraits | Complete production plan | general matrix, asset prompt |
| Evolution IV zombies, ghosts, golems, and future units | Complete registry design | Part 5 |
| Dynamic future-unit onboarding | Complete opt-in registry design | Part 5 |
| Train-versus-spawn distinction | Complete | Part 5 |
| Base zombie only, no stronger types | Complete explicit boundary | Part 5 |
| Weaker distinct zombie, ghost, and golem countries | Complete packages | Parts 5 and 6, country matrix |
| Derivative countries attack everyone aggressively | Complete as continuing aggression against every reachable ordinary country, with safe strategic prioritization | Parts 5 and 6, AI matrix |
| Parent events unaffected | Complete isolation contract, local verification pending | Parts 5 and 8, blockers |
| Ghost slow wasteland and population effect | Complete design | Parts 5 and 6 |
| Triggerable mass spawn and instant revolt wars | Complete scenario design | Part 8 |
| No direct world end | Preserved | Parts 1, 5, 6, and 8 |
| Cluster status | Deliberately remains unclustered | Part 8 |

## Planning surface status

| Surface | Status | Notes |
| --- | --- | --- |
| Core event promise | Complete | recurring generation system and management loop |
| Baseline | Complete | state curve, lots, families, accounting, decisions, AI |
| Evolution I | Complete | active and pre-fire paths |
| Evolution II | Complete | serious units, requests, tech-locked handling |
| Evolution III | Complete | random generator and claimant system |
| Evolution IV | Complete | registry, saturation, derivatives |
| Derivative countries | Complete design | implementation identifier verification required |
| Decisions and missions | Complete design | exact costs and syntax belong to implementation |
| Scripted GUI | Complete design | exact dimensions belong to implementation |
| AI | Complete design | tuning belongs to implementation |
| Focus architecture | Complete path design | final focus list and layout belong to implementation |
| Triggerable scenario | Complete design | final ID registration to verify |
| Achievements | Complete design | 11 achievements |
| Assets | Complete inventory and prompt | files not produced in planning |
| Super-event | Deliberately not needed | scope decision documented |
| Event cluster | Deliberately unassigned | future gate documented |
| Localisation | Direction complete | final copy belongs to implementation |
| Documentation | Planning docs complete | gameplay docs belong after implementation |
| Spreadsheet | Handoff complete | no workbook edit before final wording |

## Accepted plans and disposition

This package contains no separate unresolved improvement addendum. The manual improvement review’s accepted changes were folded directly into the source specification.

Future implementation plans and subagent handoffs must receive one of these dispositions:

- implemented
- promoted into this spec
- queued with reason
- rejected with reason
- superseded by a named file
- blocked

## Meaningful validation performed

- Checked complete source inventory and hashes for all 30 supplied files.
- Cross-mapped every user requirement to one or more specification surfaces.
- Compared current public Event 19 behavior against the proposed scope.
- Audited parent zombie and Death identity risks at planning level.
- Separated ordinary lifecycle from four true evolutions.
- Audited anti-bloat boundaries and super-event threshold.
- Checked derivative packages for forces, reinforcement, AI, identity, focuses, decisions, assets, and cleanup.
- Checked request and demobilization design for equipment-farming and reroll exploits.
- Checked microstate handling for invalid civil-war partition.

## Validation not possible here

- Clausewitz syntax and engine parsing
- local helper and identifier existence
- in-game random template construction
- dynamic-country creation
- GUI layout and animation wiring
- parent-event isolation in live script
- AI balance in campaign
- asset production and dimensions
- final localisation and workbook alignment

## Completion recommendation

The event planning package is ready for implementation, subject to the blockers and local verification in `blockers_and_uncertainty.md`.

The implementation goal must not be marked complete until the real improvement-loop planner and final completion auditor have run, all assets exist and are wired, all derivative parent-isolation checks pass, and the catalog mirrors final in-game text.
