# Event 101: Specialist and MCP usage maps

These maps route future implementation work.
Apply [current authority and workflow](README.md#current-authority-and-workflow), which governs delegation, retry limits, verification alternatives and completion.
The original planning roles and their findings are recorded in [the review disposition](101_tasks_review_disposition.md).
Subagents are spawned through the `chaos-redux-subagents` skill with self-contained prompts that carry every path, constraint and prior decision the role needs.

## Subagent usage map

| Role | When and input | Required output | Allowed scope and parent review |
| --- | --- | --- | --- |
| `chaosx_repo_explorer` | Before implementation, only when owner locations or native precedents are unclear | Bounded repository map, exact paths and revisions, owner gaps, closest native precedents | Read-only, parent checks that searches do not become exhaustive absence claims |
| `chaosx_scripted_system_architect` | Before final lifecycle and after lifecycle changes | Actor, generation, timer, receipt, storage, cleanup and migration contracts | Architecture only, parent reconciles semantic design with verified APIs |
| `chaosx_decision_mission_auditor` | Once the mission files exist | Mission map, costs, proof rules, partial results, cancellation and UI findings | Bounded patches only to named mission files, parent retains outcomes and final integration |
| `chaosx_ai_probability_auditor` | Selection design and actual-source review, Part 2 and the W scenarios | Country, family, archetype, target and evolution audits classified as exact, bounded, sampled or unresolved | Read-only, available probability tools or source-derived named calculations under the retry limit, parent owns tuning edits |
| `chaosx_improvement_loop_planner` | After a substantial implementation stage, only for a concrete depth or connection question | Bounded addendum with exact destinations and acceptance criteria | Planning only, parent promotes, rejects or queues every item |
| `chaosx_icon_artist` | After gameplay and reference lock, asset and achievement prompts | Six mission icons, category icon, two 64 by 64 outcome idea icons and seven achievement subjects with processed outputs | Asset-only bounded paths, parent owns sprites, modifiers, localisation and registries |
| `chaosx_generated_event_art` | After exact reference and consumer inspection, asset prompt | Six report scenes and one static category picture, processed PNG and DDS with manifest | Art-only, parent checks truthful reuse and native-size clarity |
| `chaosx_localisation_auditor` | After implementation writes final text from direction | Key coverage, dynamic token, pluralization, cost, report contrast and wording findings | Bounded language patches in named files, parent owns final source integration |
| `chaosx_spreadsheet_doc_worker` | After implementation facts and honest status are known | Workbook-owned row reconciliation and the documented CSV export | Only the named workbook and generated exports |
| `chaosx_documentation_curator` | After implementation and review disposition | Current mechanics, tuning, adapter and validation documentation | Named event docs only, no gameplay ownership |
| `chaosx_event_completion_auditor` | When the implementation is complete | Surface-by-surface finished, partial and blocked report with actual validation evidence | Read-only, parent resolves findings and never treats planning completeness as runtime completion |

The parent implements shared registration, lifecycle, final localisation, modifier consumers, achievement registry wiring and all gameplay integration.
An asset worker must not silently change a reward, mission predicate, event ID or shared registry.

No dedicated Event 101 scripted GUI is selected.
Ordinary category, mission and report review belongs to the mission, asset and completion handoffs.
The event UI worker is needed only if a later accepted change introduces a dedicated event-owned scripted GUI with a new bounded layout and MCP review contract.


## MCP usage map

The following routes are verification choices. Discover live exposure and schemas before invocation and apply the bounded alternatives in README. The original planning environment exposed none of these routes, which says nothing about the present connection.

| Surface | Route | Inputs and scenarios | Evidence to retain | Status |
| --- | --- | --- | --- | --- |
| Native event chain | `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare` | Canonical root, assignment and all terminal reports, actual baseline and changed revision | Chain topology, rendered actor and outcome states, source revision and comparison | Discover at implementation |
| Weighted selection | Begin with `hoi4.probability_inspect`, then `hoi4.probability_evaluate`, `hoi4.probability_sweep` and `hoi4.probability_compare` | Complete prepared pools, named scenarios, history modifiers and threshold cases | Candidate completeness, traces, classification, scenario hash, revision and comparison | Discover at implementation |
| Probability presentation | `hoi4.probability_render` | Country fairness, family and archetype shares, repetition and evolution comparisons | Rendered matrices or unresolved views tied to the underlying artifact | Discover at implementation |
| Uncertain inputs | `hoi4.probability_simulate` only for declared uncertainty | Explicit uncertain rate, route or owner timing inputs with reproducible seeds | Distribution assumptions, seeds and sampled classification | Conditional |
| Multi-step timing | `hoi4.probability_sequence` only when the entire tested pool, cadence and state transitions are declared | Shared repeatable draw and rest behavior, receipt transitions and terminal rules | Complete sequence model and timing limits, no Event 101-only fake scheduler | Conditional |
| Native mission and category | Inspect the actual supported native decision consumer and render through an exposed route that genuinely supports it | Assignment, progress, last day, result, repair, long names and missing owner | Actual countdown, tooltip and category states, supported route identity | An unrelated GUI render is not sufficient |
| State and route proof | Actual read-only map, state or reference route advertised by the implementation environment | Exact committed states, province, route anchors and legal controller conditions | Target identity, usable connection and relevant state revision | Semantic dependency, do not invent a route |
| Modifier and command support | Installed native documentation plus current source and advertised reference inspection | Timers, counters, scope rules, effect keys, signs, units and caps | Exact declaration and a task-specific behavior receipt | Source and offline references |

If a selected preparation subtype relies on technology, doctrine, folder, unlock or research-bonus changes, first obtain an explicit accepted scope change, then use `hoi4.tech_inspect`, `hoi4.tech_render` and `hoi4.tech_compare`. The current task package uses existing branches and does not authorize new research content.

Do not treat a tool name in this map as an observed schema or claim an unavailable MCP call ran. Source scans and hand arithmetic can establish their actual source or mathematical conclusions under the current workflow. Mockups and unrelated renders cannot establish production appearance, and no static result establishes game execution.

## Weighted-behavior scenario matrix

These scenarios apply to selection, shared pacing and achievements even though AI countries never receive Event 101 tasks. The specialist's name does not authorize an AI recipient path.

| Scenario | Complete input to construct | Expected result or ordering |
| --- | --- | --- |
| W01, single human | One eligible country and at least two valid ordinary families | Country selection is certain, family share follows normalized valid weights |
| W02, co-op fairness | Three eligible countries, one with two human seats | Three equal country entries, no extra weight for the second seat |
| W03, unequal map size | Two countries with equal eligibility, one with many more targets | Country share remains equal |
| W04, archetype target count | One family, two eligible archetypes, one with one target and one with twenty | Equal initial archetype shares, target multiplicity only affects the last draw |
| W05, peace | No threat, no crisis, valid preparation, industry and diplomacy | Offensive and defensive weights zero, other families renormalize |
| W06, pressure | The explicit fully qualifying defensive, preparation and crisis fixture in Part 2, plus mixed qualifying and unqualified targets | Base 45, 20, 40 becomes 90, 20, 160 in the fully qualifying case, weighted means restrict each target boost to the qualifying mixed-pool members |
| W07, false pressure | Same nominal Chaos but no actual pressure or live crisis, then a country with differently pressured fronts | No invented crisis or pressure factor, deterministic country row, unqualified siblings receive no target-specific boost |
| W08, threshold sweep | Chaos 199, 200, 399, 400, 599 and 600 with controlled evolution flags | Exact threshold and pre-fire eligibility behavior, no invented Evolution III |
| W09, future-only evolution | Commit a task, then activate, disable or re-enable a track | Active quantity, deadline and outcome quote remain unchanged |
| W10, repeated target | Same objective and episode plus an alternative, newest archetype conflict, three history signatures | Exact repetition excluded when another objective can survive, no duplicate history append on settlement, receipt reuse never admitted |
| W11, sole valid task | One feasible defense subtype after repetition filtering, then all surviving families recently used | Drop newest-archetype exclusion first, exact-objective exclusions oldest to newest, restore family factors to 1 only when all are penalized, retain physical, time and proof gates |
| W12, invalid selected actor | Recipient loses validity, at least two other prepared valid countries remain, then all are invalid | Uniform redraw without replacement among untried prepared countries, final revalidation, unavailable if empty, no committed empty firing |
| W13, cadence | Actual shared pool, 20-per-month recovery, halving cap, rest, competing eligible events | No private Tasks scheduler, declared recurrence estimate with complete pool or bounded classification |
| W14, multiplayer concurrency | Two shared timer callbacks select the same country | One fresh assignment receipt, other path reselects or becomes unavailable |
| W15, achievement opportunity | Actual natural firing rate, six-family availability and seven achievement requirements | Thresholds difficult but attainable in the supported campaign band, no forced hidden draws |
| W16, weak or disrupted country | Small usable capacity, high burden and limited access | Smaller feasible task or ineligible candidate, no hidden hardcoded minimum that exceeds capacity |
| W17, benefit already masked | Current live positive and negative award records and proposed quote | A useful effect window or valid related quote, no wholly valueless payoff |
| W18, live owner timing | A famine state at famine stage with relief access, a migration host with an integration backlog, and the same cases with an owner recovery time longer than the deadline | The feasible cases quote a deadline from the owner's published step holds and pace, the infeasible cases are rejected with zero weight |
| W19, reward consumer | A candidate quote whose effect has no live consumer, then the same country with queued construction or a live relief action | The idle-consumer quote is replaced or deferred, the live-consumer quote is kept |

W04 and W16 also need a target meeting both quality conditions. Its base quality is 100 multiplied by 1.5 and 0.5, giving 75 before any separate evolution factor. This is authored arithmetic for a complete synthetic input, not a measured engine result.

No exact campaign frequency is asserted from this matrix. The full competing shared pool and external state transitions must be supplied before normalization or sequence claims. If they are incomplete, preserve a bounded or unresolved result.

## Handoff discipline

Every future specialist receives the exact accepted files, current source revision, permitted paths, named scenarios and required output path in a self-contained prompt.

Use `chaosx_improvement_loop_planner` after a substantial implementation stage when a concrete depth or connection question remains. The imported review reports its seven corrections promoted. Do not reopen that unchanged pass or request another solely for a closure receipt. Give a justified new pass the complete accepted inputs and actual source, then record each proposal as implemented, promoted with acceptance basis, accepted and queued with reason, rejected, superseded, unresolved or blocked as applicable. Unaccepted proposals and separately queued work do not silently enlarge the current task.

The debug-playtest skill is invocation-only. Agents do not launch the game as an automatic final step or request or await user-owned live-game validation. Review supplied live evidence when available, keeping it distinct from source and local checks.
