# The Partition: source reading, research, and evidence boundaries

The initial supplied-source reading gate covers every file occurrence supplied for this task, including duplicate copies and files inside the supplied archives.
Its completed audit records 132 fully read text occurrences, 3,796,965 original text bytes, 43,859 physical lines, and five fully traversed ZIP containers.
No supplied text range remains unread in that audit.
The later reference pass records full reading of 16 selected offline wiki snapshots and 17 targeted repository text files.
These are bounded reading claims about identified sources, rather than a claim that the entire repository, every referenced dependency, or the installed game was inspected.

One external source remains explicitly unread: the actual `docs/spreadsheets/chaos_redux_events_catalog.xlsx` workbook.
The fetched response contained its Git LFS pointer, which does not expose the workbook's sheets, cells, validation, formulas, or formatting.
Installed Windows game documentation, vanilla examples, and native visual reference assets were also unavailable in this environment.
The package therefore supplies design and implementation handoffs, with those production reference checks still outstanding.

## 1. Reading coverage and what the evidence establishes

| Reading layer | Recorded completed coverage | Integrity and limitation |
| --- | --- | --- |
| Supplied Project Sources | 132 text occurrences across standalone sources and recursively extracted archives | Every occurrence has complete reading receipts, including duplicates, with unchanged original hashes and no missing ranges |
| Supplied archive traversal | Five ZIP containers | Every member was compared with its extracted occurrence, and all required text descendants were fully read |
| Selected offline wiki references | 16 complete files, 85 confirmed ranges | All local hashes were checked, and all 16 pinned repository blobs match after accounting for exactly one added final LF per materialized file |
| Targeted repository text references | 17 complete text reads recorded by the parent and Reader C | The reading ledger identifies each path, reader, pinned revision, and source blob, with the materialization correction noted below |
| Historical research | Three full treaty texts and the Library of Congress's indexed map metadata | The treaty pages were opened in full, while direct Library of Congress item and plate opens returned 403 |

The supplied-source audit checks explicit source-output receipts, contiguous coverage, source integrity, archive ancestry, and reader completion statements.
It does not independently observe cognition or prove understanding from a hash.
Equal file hashes were not substituted for reading duplicate source occurrences.
The evidence compiler reviewed the audit summaries, relevant ledger metadata, actual current file hashes, source protocol, current `AGENTS.md`, source conflict findings, reference manifests, and relevant research material.
This compilation does not claim a new personal semantic read of every source previously assigned to another reader.

The initial gate was completed before substantive event design and repository research.
The additional offline wiki and targeted repository reads were completed before final specification drafting, according to the parent and reader processing statements.
Later evidence checks verify those records and do not replace the original reading pass.

### Supplied corpus provenance

| Source group | Text occurrences | Original text bytes | Physical lines |
| --- | ---: | ---: | ---: |
| Standalone text Project Sources in `project_sources/` | 23 | 1,064,163 | 12,646 |
| Current dated combined bundle and its nested role archive | 47 | 1,378,873 | 15,342 |
| Standalone subagent archive | 20 | 151,247 | 1,799 |
| Prior combined bundle and its nested role archive | 42 | 1,202,682 | 14,072 |
| Total | 132 | 3,796,965 | 43,859 |

The current combined bundle is `upload/all-project-sources(20261010-195642).zip`.
The prior combined bundle is `project_sources/24-all-project-sources.zip`.
The standalone role archive is `project_sources/01-subagents.zip`.
Both combined bundles contain a nested `subagents.zip`, producing five archive containers in total.
The current archive has 28 direct members, the prior combined archive has 23, and each of the three role archives has 20.

There are 137 total supplied file occurrences when the five containers themselves are included.
The inventory records 90 distinct text hashes and 43 groups with duplicated content.
It records no unknown binary occurrences, extraction failures, decoding failures, or archive integrity problems.
Every copy of the 20 supplied role definitions was read, across the current, prior, and standalone role archives.
Reading those definitions is distinct from executing their roles.

The initial inventory preserves creation-time reading labels.
Those labels are not the final completion authority.
The completed reader ledgers and combined coverage audit supply the later reading status.
Reader C's original-assignment completion field remains false because four whole occurrences were explicitly reassigned to the parent.
Its retained-scope completion is true, and the combined audit verifies the parent's full coverage of those delegated occurrences.

### Truncation recovery

Some initial source outputs, aggregate metadata prints, and later report excerpts exceeded output or context limits.
Affected source ranges were not credited as read from those truncated responses.
The readers recovered them through smaller complete outputs and recorded the replacement ranges in their ledgers.
The combined supplied-source audit reports no remaining uncovered ranges.

The offline wiki reading ledgers record no truncated source outputs and no pending reading confirmations.
The runtime ledger distinguishes complete source reads from repository navigation and metadata excerpts.
During this evidence compilation, a combined `AGENTS.md` and metadata output also truncated.
The complete current `AGENTS.md` was recovered in four bounded outputs, and the relevant manifests and audit metadata were reread through complete focused outputs.
No full-source reading claim relies on that truncated compilation output.

### Evidence files

| Evidence file | What it records |
| --- | --- |
| [inventory.json](inventory.json) | Every supplied occurrence, archive ancestry, byte size, encoding, hash, line count, and duplicate relationship |
| [combined_source_coverage.json](combined_source_coverage.json) | All source reading receipts, normalized ranges, integrity results, archive checks, and truncation recoveries |
| [parent_gate_check.json](parent_gate_check.json) | Parent confirmation of 132 covered occurrences, five archive containers, no gaps, and no changed sources |
| [combined_wiki_coverage.json](combined_wiki_coverage.json) | All 16 wiki paths, reader assignments, coverage ranges, local hashes, reconstructed original hashes, and exact newline accounting |
| [runtime_reading_ledger.json](runtime_reading_ledger.json) | Targeted repository text reads, source revisions, readers, explicit unread workbook, failed lookup, and environment limits |
| [contributing_recovery_check.json](contributing_recovery_check.json) | Exact recovery of a CRLF-normalized materialization and confirmation that its pinned Git blob matches |

The JSON audits preserve exact occurrence paths and source identities even when a concise table here groups related files.
Their absolute paths describe the workspace in which the checks occurred.

## 2. Selected offline wiki reference pass

The repository reference is `klimPaskov/Chaos-Redux` at commit `a3ef485c5da7e2337122eca04ac65c175050f251`.
The offline wiki snapshot date is 2026-09-19.
These are the repository's offline reference files, and no live Paradox wiki page was used for this pass.

| Complete snapshot | Reader | Principal relevance to this specification |
| --- | --- | --- |
| [AI modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/AI%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Decision scores, strategies, and the limits of treating weights as probabilities |
| [Achievement modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Achievement%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Achievement eligibility, completion conditions, and icon consumer requirements |
| [Data structures](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Data%20structures%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Architect | Persistent records, arrays, event targets, and identity-sensitive state |
| [Decision modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Decision%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Visible actions, timed missions, costs, availability, and actual completion |
| [Effects](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Effects%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Territorial changes, war and peace effects, diplomacy, and outcome checks |
| [Event modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Event%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Event chains, delayed responses, scope propagation, and popup limits |
| [Graphical asset modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Graphical%20asset%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Sprite registration, textures, and consumer-specific asset behavior |
| [Idea modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Idea%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Timed preparation and reconstruction effects, expiry, and cleanup |
| [Interface modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Interface%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Native controls, layout, text, input regions, and rendering constraints |
| [Localisation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Localisation%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Dynamic country and state names, visible conditions, and working-copy boundaries |
| [Modifiers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Modifiers%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Proposed military preparation and repair modifiers |
| [On actions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/On%20actions%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Architect | Ownership, war, peace, startup, and delayed-observation boundaries |
| [Scopes](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Scopes%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Architect | Country and state scope validity, saved targets, and callback context |
| [Scripted GUI modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Scripted%20GUI%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | The event-owned dossier, state lists, dirty updates, and actor-specific visibility |
| [State modding](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/State%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader B | Whole-state allocation, ownership, infrastructure, and adjacency evidence |
| [Triggers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/paradox_wiki/Triggers%20-%20Hearts%20of%20Iron%204%20Wiki.md) | Reader C | Current eligibility, ownership and control tests, identity checks, and comparisons |

The local materializations contain 1,279,785 bytes, 1,277,275 decoded UTF-8 characters, and 18,534 physical lines.
The exact original repository contents contain 1,279,769 bytes, 1,277,259 characters, and 18,518 physical lines.
Each materialized file has exactly one additional final LF.
Removing only that byte in memory reproduces the recorded original Git blob for all 16 files.
The audit did not alter the source files or their input reading ledgers.

Reader B covered seven files in 34 confirmed ranges, Reader C covered six in 35, and the architect covered three in 16.
The audit reconciles the readers' character coordinates and the architect's inclusive physical-line coordinates into complete file coverage.
It checks the attestations and their ranges without replaying all earlier tool-output transcripts.

The original materialization manifest still says `materialized, unread` because it records creation-time state.
The three completed reading ledgers and their combined audit establish the later full-read result.
The offline snapshots do not establish the active installed engine version, native consumers, exact war-isolation semantics, or production rendering behavior.

## 3. Targeted repository texts and integration consequences

The following complete text reads are recorded at the same pinned commit.
Reader C read the full Event 009 effect file and independently reread its matching triggers.
The parent read the other 16 listed text files.

| Fully read repository text | What its inspection contributes |
| --- | --- |
| [docs/README.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/README.md) | Distinction between accepted design, implementation documentation, working plans, and evidence |
| [docs/spreadsheets/README.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/spreadsheets/README.md) | Workbook authority, export ownership, catalogue fields, and status meanings |
| [CONTRIBUTING.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/CONTRIBUTING.md) | Repository contribution guidance and the distinction between LFS pointers and real assets |
| [events/000_chaosx_events.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/events/000_chaosx_events.txt) | Event-file overview evidence, without treating that header as a complete event registry |
| [common/scripted_effects/chaosx_crisis_pressure_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_crisis_pressure_effects.txt) | Current shared crisis-pressure owner surface |
| [common/scripted_triggers/chaosx_crisis_rescue_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_crisis_rescue_triggers.txt) | Current crisis-rescue gate surface |
| [common/scripted_triggers/009_white_peace_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/009_white_peace_triggers.txt) | Actual endpoint and pair restrictions on the existing white-peace helper |
| [common/scripted_effects/009_white_peace_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/009_white_peace_effects.txt) | Pair selection, execution, bookkeeping, exclusion memory, and source-level limitations |
| [common/scripted_effects/chaosx_events_log_effects.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_events_log_effects.md) | Shared event-history and actor-mapping responsibilities |
| [common/scripted_effects/chaosx_universal_cost_effects.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_universal_cost_effects.md) | Cost quotation, payment, and owner-defined transaction behavior |
| [common/scripted_triggers/chaosx_universal_cost_triggers.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_universal_cost_triggers.md) | Affordability and cost-related validation responsibilities |
| [docs/systems/universal_cost_modifier.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md) | Shared cost scaling and integration contract |
| [common/mtth/chaosx_mtth_variables.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/mtth/chaosx_mtth_variables.txt) | Existing weighted timing conventions and centralized score patterns |
| [common/scripted_effects/chaosx_logic_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_logic_effects.txt) | Shared event selection, pacing, and lifecycle integration evidence |
| [common/scripted_effects/chaosx_dynamic_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.txt) | Existing reusable effects and shared-system ownership |
| [common/scripted_effects/chaosx_dynamic_effects.md](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.md) | Documented dynamic helper contracts and boundaries |
| [common/scripted_triggers/chaosx_dynamic_triggers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_dynamic_triggers.txt) | Shared country classification and reusable eligibility checks |

The inspected White Peace implementation cannot be treated as a general Partition settlement API.
It applies endpoint and pair gates, including faction exclusion, and invokes native peace without passing a unique war identifier or an explicit participant list.
Its immediate counters follow the invocation without a separate check that the intended war relationship actually ended.
Its country exclusion memory also prevents one country from participating in successive pair applications in the same multipair sequence.
These source findings support the specification's requirement to observe actual outcomes and prove isolation before using a narrow authored peace path.
They do not establish the native effect's behavior in an installed game.

The shared crisis policy and dynamic helper references establish integration responsibilities rather than a verified ready-made API for every proposed Partition operation.
The three-crisis local capacity policy must be resolved against its actual owner before implementation.
The specification's Task 101 payload describes a proposed semantic contract because a live Task 101 integration API was not verified.
An existing helper name, comment, or readiness counter is not credited as proof of a completed territorial settlement.

Targeted queries for `chaosx.nr113.1`, `chaosx.nr101.1`, `chaosx.nr123.1`, and `101_tasks` did not find those definitions in the inspected search results.
That bounded search result does not establish absence from every repository path or installed override.
The guessed path `common/scripted_triggers/chaosx_logic_triggers.txt` returned 404.
No definition or absence elsewhere is inferred from that failed lookup.

### Materialization integrity correction

A later evidence check found that the local `CONTRIBUTING.md` materialization contained 2,042 characters while its original runtime ledger recorded 2,059.
The parent recovered the exact content from the already retained original connector response and fully reread it.
The difference was 17 CRLF sequences that the scratch copy had normalized to LF, with no missing semantic source text.
The original connector content had already been fully read before final specification drafting.
The restored 2,059-byte file matches Git blob `8fca8e877109aa370fc14c8c8c4581e84494aa2f` exactly.
The evidence compiler independently rechecked the restored bytes and confirmed the match.
The completed recovery is recorded in `contributing_recovery_check.json`.
All 17 runtime materializations now match their pinned source blobs, eight exactly and nine after accounting for one added final LF.
Original repository character counts and materialized local character counts remain distinct where an extra final LF was added.

## 4. Authority decisions and source conflicts

The user's present brief establishes Event 113, original catalog ID 123, the name The Partition, the two named evolutions, minor-only target eligibility, and the Task 101 connection.
Numerical design anchors and expanded mechanisms in this package are planning decisions made within that brief.
They are not assertions that those mechanisms already exist in the pinned repository.

| Conflict or distinction | Applied authority and consequence |
| --- | --- |
| Event numbering | The current user brief controls this package's Event 113 identity, with original catalog ID 123 retained as provenance |
| Supplied catalog identity | The supplied current and prior exports place Wrestling Tournament at 113 and The Partition at 123, so implementation must reconcile the collision against the real workbook before registration or catalog edits |
| Supplied catalog status | The supplied Partition export is Unavailable, while the user requests To Be Reworked, so the package preserves the requested design status without claiming the workbook or runtime was changed |
| Cluster membership | The supplied Diplomacy cluster is ID 3 and lists 8, 17, 36, and 59, while this brief specifies Partition membership at High severity, so its new membership remains an implementation alignment obligation |
| Older evolution terminology | Grand Partitions from the present brief supersedes the older Spheres of Influence direction |
| Source locations | The current dated bundle supplies current skill and role guidance, while older and standalone copies remain separately read provenance |
| Public values | The stricter planning rule limits persistent mechanic-wide values, so moving statistics between tabs does not evade the limit |
| Super-event audio length | The current owner skill's one-to-two-minute final cue contract controls over older role wording that ordinarily allowed one to three minutes |
| GUI editing route | Direct reviewed editing remains permitted, with required inspect and render evidence, while `gui_rewrite` is optional rather than an independent approval barrier |
| Visual reference roots | Current `assets/gfx_references` guidance controls over older `assets/vanilla_reference` paths |
| Models and tools in supplied configuration | The configuration describes an intended coding environment, so its thread counts, model names, and server registrations are not evidence that those capabilities were available in this session |
| Existing behavior and approval | Source inspection establishes what a file contains, while user direction and explicit parent design decisions establish acceptance within this planning task |

The authoritative catalog source is the actual XLSX workbook, and its three CSV files are generated exports.
The required implementation workflow is to reconcile the workbook, preserve its structure, and run its exporter after an accepted update.
This planning task edited neither the workbook nor its exports.
The repository's [spreadsheet source contract](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/spreadsheets/README.md) establishes that distinction.

The supplied sources also contain conflicting older 3D rigging routes, model assignments, texture policies, and provider-versus-Blender instructions.
The accepted Partition design does not require custom 3D model production.
Those conflicts were read and identified, and neither incompatible production route was silently executed or combined.
Any later addition of a custom model would require a fresh current-owner reconciliation before its production handoff.

## 5. Complete supplied skill application matrix

All 18 current skill files in the dated bundle were fully read during the initial gate.
Relevant guidance was applied to this planning package and its future owner handoffs.
Reading an implementation skill does not itself create the artifact or execute the production workflow described by that skill.
The table deliberately distinguishes applied planning guidance from inactive production surfaces.

| Current supplied skill | Application in this task | Execution boundary |
| --- | --- | --- |
| `chaos-redux-event-planning` | Full event progression, playable routes, territorial rules, evolutions, costs, AI intent, aftermath, achievements, presentation, and separate coding handoffs | The deliverable is a specification package, with implementation claims reserved for later work |
| `chaos-redux-events` | Event identity, shared registration responsibilities, repeatability, actual-outcome Chaos, evolution activation, event history, and catalog alignment | No event scripts, shared registries, catalog rows, or final localisation were changed |
| `chaos-redux-decisions-missions` | Claimant, target, and protector actions, costs, deadlines, mission ownership, actual completion, and bounded action presentation | The decision and mission review is a planning audit, with native execution evidence still required |
| `chaos-redux-mtth` | Weighted target selection, active evolution timing, centralized tuning, and named AI scenarios | Numerical weights and timing are proposed anchors, with probability inspection and comparison deferred to the installed coding environment |
| `chaos-redux-scripted-gui` | Event-owned dossier, native controls, state matrix, value budget, crowded and stale states, and resolution requirements | The paper layout review is not a production render, reference-image approval, or before-and-after GUI validation |
| `chaos-redux-event-assets` | Complete planned report, news, super-event, action, mission, spirit, and achievement asset coverage, with consumer dimensions and owner handoffs | No final generated images, processed DDS files, installed sprites, or decoded native references are claimed |
| `chaos-redux-super-events` | One rare Grand Partitions outcome, presentation direction, audio-duration contract, and specialized text and audio research handoff | No final quote, recording, licensing determination, cue export, or runtime super-event wiring was produced |
| `chaos-redux-subagents` | Self-contained bounded roles, source readers, specialist audits, ownership boundaries, and future production routing | Reading every role definition does not mean every role ran, and the role disposition report records actual work separately |
| `chaos-redux-improvement-loop` | Near-completion depth review and explicit disposition of accepted, superseded, rejected, or deferred recommendations | Closure evidence belongs in the final review record rather than a claim that planning implements gameplay |
| `chaos-redux-xlsx` | Workbook-only edit authority, ID collision handling, export synchronization, and future catalog validation | The real workbook was unread because only an LFS pointer was obtained, and spreadsheet editing did not begin |
| `chaos-redux-state-ledgers` | Exact state identity, transaction receipts, conservation principles, and shared population-owner boundaries informed the design | Territorial allocation is not a civilian migration transaction, and no cohort or population-transfer subsystem was added |
| `chaos-redux-save-inspection` | Persistent crisis identity, delayed outcomes, stale consent, and future save-state evidence requirements | No save was supplied or inspected, so save and reload behavior remains an implementation validation obligation |
| `chaos-redux-debug-playtest` | The separation between source inspection, controlled setup, and real gameplay proof informed validation boundaries | Its autonomous desktop workflow was not activated for this planning request, and no live game was launched |
| `chaos-redux-focus-trees` | The depth and integration rules were reviewed when deciding which systems the event needs | The accepted event operates through diplomacy, decisions, missions, and wars, so no focus tree surface was created or audited |
| `chaos-redux-native-raids` | Native-cost and callback ownership requirements were reviewed as supplied guidance | No native raid mechanic is part of the accepted Partition routes |
| `chaos-redux-frame-animation` | The genuine-frame requirement and asset-consumer boundary were reviewed | The accepted visual plan does not depend on animation, and no still-image transform sequence was substituted for it |
| `chaos-redux-3d-model-pipeline` | Current production ownership and conflicting older routes were identified | The event adds no custom model, skeletal action, 3D sound, or counter production task |
| `chaos-redux-shared-git-commit` | Shared-index isolation and bounded-change ownership were reviewed | No local repository checkout or shared index was available, and no Git commit was created |

The additional legacy supplied skill `chaos-redux-comfyui` was also fully read in its standalone and prior-bundle occurrences.
It describes an older portrait-production workflow.
No portrait is required by the accepted Partition design, so that workflow was not activated.
Current character portrait ownership belongs to `chaosx_portrait_creator`, as directed by the current source guidance.
No RunPod operation or portrait styling claim is made.

No project skill was created or modified for this event package.
Event-specific rules remain in the event specification and handoff documents.

## 6. Historical research and design inferences

Historical references inform the diplomatic mechanisms and visual direction.
They do not predetermine campaign countries, legitimate coercion, or override the user's rule that major powers cannot be partition targets.
The following summaries separate the source's contents from the design inference drawn from them.
No verbatim treaty language, historical quotation, or final player-facing copy is supplied here.

### Munich Agreement, 29 September 1938

The [agreement text](https://avalon.law.yale.edu/imt/munich1.asp) specifies a staged evacuation and occupation timetable, mapped territorial zones, an international commission, and preservation of existing installations during the evacuation.
Its schedule begins on 1 October and requires completion by 10 October.
The design inference is to show exact state allocations, separate agreement from completed transfer, and make staged handover interruptions visible.
The text is evidence of the agreement's provisions, rather than proof of freely given target consent or successful protection.

### Annex to the Munich Agreement

The [annex](https://avalon.law.yale.edu/imt/munich2.asp) distinguishes the British and French guarantee offer from a later German and Italian guarantee tied to settlement of specified minority questions.
The design inference is to distinguish a diplomatic promise, a conditionally available guarantee, and an actual active protection commitment.
This supports explicit activation conditions and readable expiry or withdrawal consequences in the protector route.

### German-Soviet Boundary and Friendship Treaty, 28 September 1939

The [treaty text](https://avalon.law.yale.edu/20th_century/gsbound.asp) defines a boundary through an attached map and allocates administrative responsibility on its two sides.
The design inference is to treat coalition shares as concrete territorial allocations whose agreed vector can differ from the eventual military outcome.
The treaty's self-justifying claims about order and the Polish state remain statements made by its signatories, rather than neutral historical conclusions adopted by this package.

### Maps of Poland, 1919

The Library of Congress's [indexed plate record](https://www.loc.gov/resource/g6520m.gct00401/?sp=10) identifies the British Foreign Office Historical Section and War Office Geographical Section collection published in London in 1919.
Its metadata describes a partition map showing the 1772, 1793, and 1795 divisions among Austria, Prussia, and Russia.
The design inference is progression from territorial loss to possible complete partition across different campaign conditions.
Direct access to the [item page](https://www.loc.gov/item/map46000382/) and plate page returned 403, so this task read indexed metadata rather than inspecting or downloading the actual map image.
The archive's reuse statement does not replace production-time verification of the exact asset selected for use.

The rare super-event's eventual historical quote and audio selection still require their own research, attribution, fit, and rights records.
The current package supplies a direction and a bounded research handoff without presenting an unsourced final quotation or selected recording.

## 7. Exact unread source and remaining production evidence

| Source or capability | Actual status | Consequence |
| --- | --- | --- |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | Actual workbook unread, with only a Git LFS pointer returned | Hydrate and read the workbook before resolving the 113 and 123 collision or editing catalog data |
| Workbook object identity | SHA-256 `a0ac5c0efacd7169e183b0bd393ba223d596ac74cae5d6d1a51bacb3411b613a`, declared size 95,115 bytes | The pointer identifies the required object and does not establish any cell contents |
| Installed HOI4 documentation and vanilla files | Windows installation unavailable | Exact installed syntax, current native behavior, and at least one appropriate native precedent remain future reads |
| Native GUI and visual reference families | Canonical Windows reference locations unavailable | Consumer dimensions that depend on inspection, native control behavior, alpha treatment, and rendering must be verified before asset and GUI completion |
| HOI4 MCP event, probability, GUI, map, and reference tools | Required routes were not exposed during capability discovery | No live inspection, scenario evaluation, before-and-after comparison, engine parser validation, or production render was performed |
| Complete repository checkout | Unavailable | Searches and fetched texts establish only their stated bounded coverage |
| User save or live-game evidence | No save or gameplay result was supplied for inspection | Persistence, war merging, player extinction handling, diplomacy, and AI behavior remain unverified in the game |
| Final visual and audio assets | Planned rather than produced | No asset generation, conversion, installation, licensing review, or in-game consumer proof is claimed |

The unavailable installed reference tree includes `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` and its relevant effect, trigger, scope, localisation, and script-concept documentation.
Relevant native owner references also include `common/scripted_guis/_documentation.md`, `common/script_constants/documentation.md`, and `common/ai_strategy/documentation.info` under that installation.
The canonical project visual-reference root is `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references`.
The existence of these paths in supplied guidance is not evidence that their files were accessible or read here.

Tool discovery did not expose the required HOI4 routes.
That is a capability gap rather than a failed server health probe.
No unavailable tool was simulated, and no source-only review was presented as equivalent to engine or visual evidence.

The source protocol permits external supporting-file limitations and unavailable project tooling to be carried as explicit implementation handoffs after the supplied-source gate passes.
It does not permit an unread supplied Project Source to be quietly omitted.
This task's initial supplied-source gate passed, while the external workbook and installed references remain disclosed limitations.

The later coding owner must read the active implementation dependencies that become relevant to its actual patch, rather than treating this document as a permanent substitute for source inspection.
The final acceptance matrix and specialist handoffs identify the gameplay, probability, GUI, state-transfer, cost, achievement, and Task outcome scenarios that need real implementation evidence.
The package's completeness claim is a planning claim, with the distinction between design, source findings, and unperformed production validation preserved throughout.
