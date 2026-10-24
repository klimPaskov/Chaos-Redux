# Investment sources, decisions and review

Prepared on **23 October 2026** for the supplied **121 Investment** brief. This report distinguishes supplied-source reading, targeted repository inspection, authored design, analytical checks and unperformed implementation work.

## Full Project Source reading

The required reading gate passed before substantive design authoring and repository research. The root assistant and three actual source readers collectively read all **152 distinct supplied text files**, representing **194 text occurrences**, **five archive occurrences** and **3,211,939 distinct text bytes**.

| Actual reader | Distinct texts | Distinct bytes |
|---|---:|---:|
| Root | 10 | 347,016 |
| `source_coverage_audit` | 71 | 1,116,807 |
| `source_planning_reader` | 34 | 874,436 |
| `source_runtime_reader` | 37 | 873,680 |
| Total | 152 | 3,211,939 |

This is team coverage. It does not mean the root personally read every file. The root took over current event and event-log integration sources, indices 88 and 89, from the runtime assignment. Their final attribution belongs to the root. Every distinct old and current source version was read independently. Full-file copies with identical SHA-256 hashes were covered by the identical content read. Filenames, search hits and hashes were used to organize and verify coverage, not as substitutes for reading content.

Some initial source outputs were truncated. The affected ranges were reread in bounded outputs before the gate passed. No required source range remains unread. The portable [coverage ledger](121_investment_source_coverage.json) retains each source identity, exact hash, copies, complete byte range, actual reader and tool receipt. Original character coordinates were mapped to original UTF-8 byte offsets, accounting for universal-newline normalization and CRLF line endings. That conversion preserves the original character ranges as additional evidence.

| Source archive | Bytes | SHA-256 |
|---|---:|---|
| `upload/all-project-sources(20261023-170950).zip` | 738,995 | `82fd1eb220e9b903e7f0d597ece677b7ad88054c81ca4721b43a636b60791237` |
| `project_sources/24-all-project-sources.zip` | 418,567 | `658006c9a1fdde344db7a647a329c70478bb2dac564371c2eac4bc4cf01ee318` |

The archive count includes nested archive occurrences. The coverage ledger records all contained text identities, including old loose source copies and both generations of subagent definitions. The original brief is source index 43. The Project Source protocol is index 42.

The package has not shortened the requested feature to accelerate delivery. All four sectors, both evolutions and their complete control and consequence paths remain in scope. Choosing two public values, a basic decision category and bounded site counts is an authored usability and runtime decision. It does not represent omitted source reading or omitted requested evolutions.

## Source register

For supplied sources, the index below refers to the exact entry in `121_investment_source_coverage.json`. Paths beginning `.claude/` are within the current uploaded archive. The ledger preserves the complete archive locator and hash for every entry. The register highlights design authority without duplicating the full 152-entry manifest.

| Source | Ledger indices | Applied responsibility |
|---|---|---|
| `121 - Investment.md` | 43 | Requested identity, sectors, country scope, funding, trouble and both evolution thresholds |
| `CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | 42 | Full reading before substantive work, version reconciliation and honest coverage |
| Current `AGENTS.md`, `CHAOS_REDUX_MECHANICS.md`, `README.md` | 120–122 | Project behavior, current Chaos framework, implementation and review boundaries |
| `.claude/skills/chaos-redux-event-planning/SKILL.md` and all seven supplied references | 80–87 | Full design, player-facing text direction, presentation, assets and specification delivery |
| Current events skill and four references | 88–92 | Actor selection, shared history, evolution/cluster integration and scripted-system ownership |
| Decisions/missions skill, four references and supplied templates | 58–67 | Inclusive costs, phase transactions, ordinary category, public values and finite missions |
| AI strategy skill and references | 50–52 | Legal choices, distinct AI mechanisms and source-grounded scoring |
| Event assets skill and six references | 73–79 | Consumer manifests, documentary scenes, independent icon families, achievement triplets and lineage |
| Ideas/modifiers skill | 97 | Consolidated visible effects and exact source-owned contributions |
| Improvement-loop skill | 98 | Bounded substantive review and correction |
| Map/states skill and references | 99–101 | Legal states, coastal provinces, rail geometry and owner ledgers |
| Scripted GUI skill | 105 | Review of presentation options, with a basic native category selected for this design |
| Current subagents skill, configuration and canonical definitions | 107, 128–151 | Self-contained assignments, ownership, available-role honesty and future specialist routing |
| Debug/playtest, save inspection and MTTH skills | 57, 104, 102 | Evidence limits, history migration and qualified timing analysis |
| XLSX skill and references | 116–119 | Workbook authority, targeted catalog changes and preservation |
| Current catalogs and shared helper registries | 123–127 | Current event/cluster context, date conversion, exact building damage and population-loss interfaces |
| All other supplied old/current sources | Remaining ledger entries | Fully read under the protocol, retained for compatibility and applicability decisions |

All 23 current canonical role definitions were read. The supplied configuration registers 20. The newer equipment/units, map/states and technology-tree workers have source definitions without corresponding entries in that configuration. Their presence in the archive is not evidence that this session could dispatch their configured runtimes.

### Pinned repository evidence

Repository research is pinned to **`klimPaskov/Chaos-Redux@41bc4e5045a7b5c131be69dda2f08079d478634c`**, whose default branch was `master` when inspected. Current implementation must inspect relevant changes from that pin. No working checkout was mutated by this planning task.

| Repository source | Actual reading or inspection | Material finding |
|---|---|---|
| [Authoritative events workbook](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/spreadsheets/chaos_redux_events_catalog.xlsx) | Binary fetched and relevant rows/sheets parsed | Events row 122 assigns 121 to The Pact. Row 133 assigns 132 to Investment. Both have Unavailable status and blank proposed classification fields |
| [Industrial Boom documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/034_industrial_boom.md) | Full 185-line document | Real civilian commitment precedent and event-owned lifecycle |
| [Great Depression documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/events/035_great_depression.md) | Lines 1–156, with an initially truncated subsection repaired | Existing crisis owner, external caller and consequence context |
| [Universal cost documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/universal_cost_modifier.md) | Full document read, then pinned identity reconfirmed | A quote is separate from payment. Exact paid receipts govern refunds. Factory commitments require an explicit adapter |
| [CXT testing documentation](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/testing/chaosx_test_country.md) | Lines 185–235 and 294–312 | Facility-group, construction, ownership, supply and coastal constraints. Prepared test content does not establish normal gameplay eligibility |

The [repository evidence manifest](121_investment_repository_evidence.json) retains exact returned Git blob identities, local evidence normalization and retrieval/inspection distinctions. Runtime research fetched nine complete Event 34/35 files and verified their Git blob hashes. The reader inspected named relevant sections and direct contracts, not every line of all nine files. A separate Event 35 contract read covered lines 1–120 only. Its returned full-file blob identity is not presented as a hash of that local excerpt.

Event 34's commitment aggregate and `civilian_factory_use` modifier provide a useful mechanism. Its reserve helpers also own Boom state and Overheating, so Investment needs independent reservation ownership. The inspected reserve decision does not establish a complete usable-capacity preflight. Its major-or-human target restriction would exclude eligible AI minors and is deliberately replaced in this design.

Event 35's current gateway recognizes six callers and no Investment production caller. The required extension must authenticate real Investment loss. Fresh accepted results are exactly 1, 2 and 3. Duplicate result 4 and other positive results cannot prove fresh acceptance. Context and ledger-cap checks can occur before duplicate detection, which makes durable Investment acknowledgment necessary. The existing non-independent history path also requires an owner-reviewed context-preserving adaptation. Parts 3 and 7 specify these changes explicitly.

The presentation inspection covered the shared achievement registry's root and relevant economic examples, the achievement alias header/first triplet, initial English achievement keys and the full Event 34 GFX file. It established the shared owners and existing naming conventions. Proposed `interface/121_investment.gfx` is a new allocation. The narrow directory and identifier checks do not claim whole-repository collision clearance.

### Catalog and version decisions

| Observed difference | Historical package disposition |
|---|---|
| Brief requests 121 while the authoritative workbook still has Investment132 and Pact121 | The 2026-10-24 user decision accepts Investment 121 and authorizes catalog migration while preserving displaced concept records. Identity/migration is implemented in the workbook and registry, with The Pact preserved as a displaced concept and no replacement ID invented |
| Brief says To Be Reworked while the workbook says Unavailable | The current workbook status is Unavailable; To Be Reworked is historical brief wording. No status upgrade is evidenced |
| Current Positive Economy cluster 7 contains 18, 34, 55, 57 and 58 | Historical proposal: consider cluster membership only through a future authorized workbook change. No catalog update is authorized here |
| Older loose skills differ from the current split skills | Apply the current archive's `.claude/skills/` contracts, using older versions as historical context |
| Old and current Chaos/evolution material differ | Use the current six Chaos bands, the requested 200/600 thresholds and zero Chaos for evolution access itself |
| Canonical role definitions and registered runtime roles differ | Follow current definitions, verify actual runtime availability and disclose any generic collaborator fallback |
| Planning requested all supplied sources, while repository research is targeted | Report complete supplied-source reading and bounded external inspection separately |

## Brief coverage

| User requirement | Complete specification coverage |
|---|---|
| One country per firing, including AI minors and human players | Parts 1, 6 and 7 define uniform eligible-country selection, the actor before history and legality without a major-only gate |
| Civilian, military, naval and special industry | Part 2 defines each output bundle, variants, legal placement, dividends and special-feature alternatives |
| Real funding and construction over time | Parts 1 and 4 define integer capacity holds, actual funded work, three phases, exact quotes and automatic earned delivery |
| Factories, infrastructure, ports, dockyards and special facilities | Parts 2, 3 and 7 bind each result to a legal state, province, route or native facility |
| Corruption, delay and overruns | Parts 1, 3 and 4 define frozen incidents, bounded work changes, investigations and revised agreements |
| Fund, investigate or abandon | Parts 3 and 4 define all responses, inclusive affordability, free construction wind-down and paid emergency alternatives |
| Megaproject Fever at 200+ | Part 3 defines two-to-four-state programs, sequential/parallel funding, early assets, systemic failure and the Event 35 integration |
| Impossible Industry at 600+ | Part 3 defines self-assembly, extraction, throughput, prototype/full-risk routes, finite service, malfunction, disappearance and disaster |
| Full planning and supplied subagents | Part 8 documents actual generic collaborators and complete future canonical assignments, with honest capability limits |
| Full reading and disclosure | This report and the coverage ledger account for every supplied source and repaired truncation |

## Primary research

The following research informed conventional industrial situations and visual direction. The numerical mechanics and fictional anomalous methods are authored design. No historical source is offered as validation of their balance or feasibility.

| Primary source | Applied design inference |
|---|---|
| [The Henry Ford, Willow Run Bomber Plant](https://www.thehenryford.org/collections/explore/sets/detail/willow-run-bomber-plant) | Training, organized assembly and costly design changes support staged military production and genuine overruns |
| [TVA, Building a Better Life for the Tennessee Valley](https://www.tva.com/about-tva/our-history/built-for-the-people/building-a-better-life-for-the-tennessee-valley) | Coordinated power and transport works support the utility/corridor option's enabling infrastructure |
| [U.S. Maritime Administration, Emergency Shipbuilding Program](https://www.maritime.dot.gov/multimedia/emergency-shipbuilding-program) | Expanding yards under capacity and component constraints supports naval construction and logistics choices |
| [U.S. Department of Energy, Oak Ridge history](https://www.energy.gov/orem/history) | Distinct specialized sites and long-lived cleanup obligations support differentiated engineering facilities and meaningful closure |

## Actual work and evidence limits

Actual work includes full supplied-source reading by the named team, pinned connected GitHub retrieval, workbook parsing, targeted source inspection, primary-source web research, all eight specifications, five handoff prompts, independent bounded review and local arithmetic and package checks.

The independent reviewer is an actual generic collaboration agent applying the supplied current improvement-planner contract. It is additional to the three source readers. It read the complete eight-part specification and existing prompts, reported a finite correction set and performed the recorded focused recheck. This does not claim that the project's configured canonical production worker ran.

No HOI4 or Clausewitz service was exposed in the current tool inventory. No HOI4 MCP validation, probability-tool execution, installed vanilla lookup, native timer or capacity observation, GUI render, live-game run, final art production or final localisation authoring took place. Analytical incident probabilities are explicitly conditional arithmetic. Source-level confidence does not establish native behavior.

The user has not been asked to run the game or supply screenshots as a planning completion gate. Implementation instructions retain the named native questions and require honest evidence boundaries. A missing optional tool does not authorize leaving an identified source defect unresolved or repeatedly retrying the same unavailable capability.

## Bounded review and corrections

The independent reviewer fully read all eight original specification parts and the four existing specialist prompts in untruncated outputs. It subsequently read the README, goal prompt and this source report. It parsed the portable coverage ledger and checked its complete ranges, totals and attribution. That ledger inspection is evidence verification, rather than a claim that the reviewer personally repeated all 152 source reads.

The review recommended a finite correction set and no broad feature expansion. The following eight groups were accepted and incorporated across the controlling rules and handoffs.

| Finding | Completed design correction |
|---|---|
| Engineering throughput could charge continuing service after issuing only one-time research bonuses | Added licensed research speed of +10% ordinary/+15% mega for inspected operation and +20%/+30% at full risk. The existing two extra one-use bonuses remain separate. Same-type research benefits do not stack |
| Ordinary Fever had no authored numeric route from its maximum base risk to the financial-shock threshold | Added exact contextual and incident Exposure contributions, clipped source residuals, bounded inspection order, correction ownership and a reachable 90-day warning example. Added exact site work factors and a separate ordinary Special duration range. Threshold 2 also requires verified conventional paid-work loss of at least 25% of the frozen accepted construction budget, without shrinking that denominator through reduction or cleanup |
| Special Fever and self-assembly outputs had ambiguous building types and counting | Split refinery Materials networks from Engineering facilities. Defined U/B-based extra counts and civilian/military/dockyard types, with no facility or refinery duplication. Required paid commissioned scope before operation and bounded first-service activation |
| Full and reduced network dividends lacked exact values and receipt timing | One program-level dividend, using the selected route's amplitude for 180 days at full completion or 90 at agreed reduced commissioning. Early sites provide buildings without repeated dividend clocks |
| Promised aftermath recovery lacked an executable action contract | One quoted base-25 PP recovery attempt, one/three actual held civilians, 30 funded days within 60 calendar days, and a once-only reduction of min(90, remaining distress days). Failure and owner takeover release the hold without resetting dates |
| Achievement conditions disagreed with the single risk meter, malfunction timing and discounted costs | A03 uses final program-wide Exposure. A05 has an explicit first-fault eligibility clock without changing malfunction expiry. Genuine discounted or zero political quotes qualify with authentic service authorization. Emergency fees use the exact quoted base cost capped by available PP |
| Future coding instructions could reuse this task's reading gate across a new task | Current `AGENTS.md` governs task-relevant reading. Read the applicable current skills, references and touched source; reuse evidence while inputs are unchanged and re-read/recheck changed inputs. The historical ledger remains provenance only |
| Writing direction and achievement metadata needed explicit authoring decisions | Added option-family viewpoint, tone, humour, disclosed facts, dynamic variation and research guards, plus all five difficulty and reveal rules. No final player-facing wording was inserted |

The parent also reconciled the already identified transaction seams: phase-specific upward rounding, actual held capacity, duplicate and stale callbacks, output observation before success, absolute anomaly expiry, a 30-day warning response followed by 30 funded cleanup days within 60 calendar days, pending self-assembly coupon retirement, exact same-case fee coverage and Event 35's fresh-acceptance set. These changes preserve the original requested scope.

No native test result is inferred from the successful design review. The focused recheck and final package verification are recorded below.

### Final focused recheck

On 23 October 2026, the independent `bounded_spec_review` collaborator returned **PASS for the requested complete planning package**. All eight original finding groups are closed. The single focused recheck found no remaining concrete contradiction within its stated scope and recommended no further broad design expansion or review cycle.

The recheck covered the changed controlling rules and their corresponding handoffs. It also confirmed the flagship's cumulative dormancy rule across the evolution, action, presentation and runtime contracts. Retained allowances of 0, 20 and 120 days yield first-service windows of 0, 20 and 90 days. It separately verified the final threshold 2 paid-loss floor, its non-shrinking conventional budget, service exclusions and the acceptance case's below-boundary and exact-boundary checks. The unchanged threshold 1 example remains reachable with 2,400 actual paid factory-days written off.

One overlarge review output was replaced by complete bounded reads before the reviewer accepted the affected text. No affected review range remained unread. The review verified the team's portable coverage evidence without claiming to repeat every original source read or fully reaudit the external repository.

### Final document verification

| Check actually performed | Result |
|---|---|
| Package inventory | 17 content files: eight specification parts, five execution prompts, README, source/review report and two JSON evidence manifests |
| Specification extent | 39,153 whitespace-delimited words across the eight controlling parts |
| Compact prompt limits | Goal prompt 3,928 characters. Decision/mission prompt 3,997 characters. Both fit their 4,000-character limits |
| Internal links and heading anchors | All 78 package-internal link occurrences resolve, including the relocated Event 35 technical handoff |
| Intentional external skill links | Three link occurrences point to two repository skill destinations, documented in README and intended to resolve after installation under `docs/specs/` |
| Source ledger | All 152 source hashes match their retained original bytes. Every normalized byte range is contiguous from zero to its file's full length. Copies total 194 and distinct text bytes total 3,211,939 |
| Evidence portability | Both JSON files parse. Neither includes scratch absolute paths. Repository evidence distinguishes 19 inspected source files from full-repository coverage |
| Asset and achievement inventory | 24 unique non-achievement rows plus five unique achievement IDs with three states each, totaling 39 planned DDS outputs |
| Acceptance matrix | 48 distinct named future acceptance scenarios, including the updated national paid-loss and first-service boundary cases |
| Analytical probabilities | Recomputed two- and three-check incident probabilities, the 5%→15% and 5%→15%→30% paths, and the conditional 9.45% upper-band warning/cascade product |
| Prose and completion markers | All 15 Markdown files contain no em dashes, semicolons or unfinished-work placeholders |

These are document, evidence, arithmetic and consistency checks. They do not substitute for the explicitly unperformed engine, interface, art or live-game work.
