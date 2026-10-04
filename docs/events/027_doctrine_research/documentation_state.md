# Event 027 documentation state and resume map

Status date: 2026-10-03.
Disposition: superseded by `docs/events/027_doctrine_research/overview.md` and `docs/plans/027_doctrine_research_plans/agent_decisions_2026-10-04.md`. The rows below describe the 2026-10-03 source; the empty-track gate, firing publication, Special Forces, and evolution rows are no longer current.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Relative paths below resolve under that workspace.
Bare handoff names and `subagent_handoffs\` references resolve under `docs\plans\027_doctrine_research_plans\`.
Bare closure, MCP, fixture, and probability-baseline paths in the tables also resolve under that plans folder.

## Authority and exact cleanup scope

The current parent instruction requires the complete `docs\specs\027_doctrine_research_specs\` package as acceptance criteria and authorizes documentation reconciliation only.
The parent's acceptance attestation is also recorded in `docs\plans\027_doctrine_research_plans\subagent_handoffs\firing_profile_transaction_review_2026-10-03.md`.
This is the acceptance basis for retaining the full design requirements, independently of spec dates, folder placement, unchecked criteria, and older handoff labels.
It establishes intended scope, not implementation acceptance or playability.
No proposal in an audit is promoted into accepted design here.

This ledger is the current bounded documentation and resume authority.
It replaces the September status claims in `docs\plans\027_doctrine_research_plans\documentation_state.md`, `review_closure_refresh_2026-09-04.md`, and `mcp_evidence.md` as current evidence.
The plans-folder ledger is retained unchanged because it is outside this curator's write ownership.
The parent owns `docs\events\027_doctrine_research\overview.md`.
Only this ledger, the September closure addendum, the MCP evidence ledger, and `docs\plans\027_doctrine_research_plans\subagent_handoffs\documentation_refresh_2026-10-03.md` are curator-owned.
No spec, gameplay, localisation, GUI, asset, spreadsheet, index, or commit change is authorized.

## Current source-of-truth map

| Surface | Evidence owner and path | Current disposition and limits |
| --- | --- | --- |
| Full design and completion requirements | All 16 files in `docs\specs\027_doctrine_research_specs\`, particularly `027_doctrine_research_acceptance_criteria.md` and `027_doctrine_research_goal_prompt.md` | Accepted implementation scope by current parent direction. Feature acceptance remains unresolved. |
| Native grant compatibility repair | Commit `f9978e9ab7fb70e347f7157170c3386d2e979a83` and `subagent_handoffs\live_qa_index_filter_repair_2026-10-03.md` | Implemented bounded startup repair. The supplied live HOI4 1.19.2 result rejects `add_mastery.index`. All 107 grants omit both numeric grant filters and retain folder/subdoctrine/unique track type. Post-repair startup and native mastery proof remain pending. |
| Native target uniqueness | `docs\plans\027_doctrine_research_plans\live_qa_filter_uniqueness_2026-10-03.json`, referenced by the repair handoff | Reopened JSON covers all 107 grants with maximum one matching track and no ambiguous target rows. Special Forces uses distinct `special_forces_first` and `special_forces_second` types. Token reuse still leaves a separate level-readback ambiguity. The recorded vanilla `SOURCE_UNCLOSED_BLOCK` diagnostic remains a source-parser limitation. No engine transaction proof follows. |
| Level getter grouping | `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt` and current parent facts | Parent reports source equivalence for 99 identities, 20 read levels, and 2,079 source cases including level zero. This is source evidence, without measured native performance or banking proof. |
| Receipt alignment and AI closure | `subagent_handoffs\parent_queue_correction_2026-10-03.md`, current effects/triggers | Implemented in source. Receipt columns align with receipt IDs, not batch count. Zero-choice AI completion promotes queued work. Mandatory mechanic and runtime evidence remain blocked. |
| Receipt finalization and exact pending identity | `subagent_handoffs\parent_native_repairs_2026-10-03.md`, current effects | Implemented in source. Finalization requires effect-applied receipt, matching batch/choice, and positive remaining choices, then clears selected action after result capture. Recovery matches pending receipt ID as well as batch/choice. Interruption atomicity and native idempotency remain unresolved. |
| Empty-track capability | `common\scripted_triggers\027_doctrine_research_triggers.txt`, `doctrine_research_empty_track_is_verified` | Implemented guard: `doctrine_research_empty_track_is_verified` is `always = no`, and the registry-level empty adapter delegates to it. Assignment plus first step is blocked pending local native bank evidence. The full accepted empty-track requirement is retained. |
| Adoption and assigned-track mastery | Current triggers and `native_transaction_audit_2026-10-03.md` | Source actions remain available in their existing eligible states. Registry initialization and static identities do not prove exact native mastery, free assignment, bank preservation, or full feature playability. |
| Human-start migration and achievement exclusion | Current effects/triggers, achievement helpers, and latest parent controller-edge decision | Implemented source metadata and campaign exclusions. Missing historical human-start tail entries append zero rather than inferring today's controller. Eligibility uses human control at batch start and the country's own consumed Event027 receipts, which may be resolved by AI after a controller change. Existing campaign-valid checks remain. No per-receipt HumanExecuted condition or additional AI-execution ban was added. Full origin coverage, positive/negative cases, and long-ledger behavior remain unresolved. |
| Native Milestone summary | `localisation_audit_resume_2026-10-03.md` read-only appendix | Implemented source correction: summary uses the display helper's native `has_completed_track` readback, replacing maximum-level inference. Native execution remains unverified. |
| Shared selectors and catalog previews | Same localisation appendix, current shared effects/localisation | Implemented in source: nine selectors, five guarded saved-size History descriptions, generic zero-payload fallback, and four aligned evolution catalog rows. Current consumer inspection/render evidence is blocked. |
| Global firing profile and History producer | Current parent refresh, binder-fix/AST report, `integration_audit_current_2026-10-03.md`, `firing_profile_transaction_review_2026-10-03.md`, and current source reads | Implemented owner source structure: six persistent envelope arrays, country firing-ID column, one collect scan, pure append pass, direct dispatch, forced console root, and `.14` wake without profile inputs. Corrected binder is in the normal History recorder after Brilliant Scientist callbacks and before override reset. Parent reports AST-confirmed one normal-recorder call and no system-recorder call. Reentrant review and MCP/native delivery proof remain separate unresolved evidence. |
| Failed publication | Latest parent direction and `doctrine_research_fire_global_batch` / `doctrine_research_bind_firing_history` | Implemented source recovery: quarantine only the current firing's newly appended last rows on aligned captured countries, clear recipients, record one actorless pacing attempt with payload 0, and bind the actual sequence through the blocked branch without wakes. Earlier rows are not selected for quarantine by that branch. Runtime failure/reentry proof remains unresolved. |
| Special Forces adoption no-replacement guard | Latest parent correction and `doctrine_research_special_forces_adoption_available` | Implemented source guard `NOT = { has_any_grand_doctrine = special_forces }`, protecting unknown custom active Grand Doctrines in the folder as well as the recognized native tokens. Other domains are unchanged by this correction. Installed trigger documentation lines 3156-3170 establishes the generic current-folder test. No new MCP/native result proves it. |
| Weighted logic | `subagent_handoffs\probability_baseline_resume_2026-10-03.md` | Blocked specialized audit by `chaosx_ai_probability_auditor`. Four frozen sources and the 37 named scenario matrix exist. No successful current probability inspection, normalization, sequence analysis, or baseline/final comparison exists. |
| Assets | `achievement_asset_visual_refresh_2026-10-03.md` and latest parent visual approval | Specialist static/DDS checks cover nine earlier runtime states, with First Lesson and Single School visually passing and original Joint Curriculum clipping recorded. Parent approved the new Joint Curriculum 1280 master and 64x64 subject with all four motifs complete. Specialist promotion of its three corrected final states is in progress. That approval supersedes the earlier candidate-wait finding, without assuming the handoff's older 1254 candidate hash identifies the approved 1280 artwork. Final promoted identities and consumer proof remain pending. No binary asset was inspected by this curator. |
| Catalog and National Breakthroughs | `spreadsheet_refresh_2026-10-03.md`, latest parent correction, current cluster source | Implemented bounded catalog repair: Events!M28 is `To Be Reworked`, and Cluster Memberships!G44 says `Optional member of the National Breakthroughs cluster.` Exactly those two cell values changed. Details and evolutions already exactly matched source, disproving the earlier stale-wording claim. All three exports ran, with only the event export changing. Cluster9 remains `Partially Available` with seven concept members. Runtime 9/27/9001 and exact Calm override remain as recorded. Full gameplay/cluster acceptance is unresolved. |
| MCP evidence | `docs\plans\027_doctrine_research_plans\mcp_evidence.md` and current owner handoffs | Blocked domain evidence. This curator exposes no HOI4 routes. Successful reference calls in other auditors and an earlier production v3.6.0 handshake do not prove working current event, doctrine, GUI, or probability analysis. Standalone viewer availability is a separate unresolved/package-gap question. |

## Acceptance coverage and remaining work

### Latest parent evidence refresh

The parent reports one AST-confirmed binder call in the normal recorder and none in the system recorder.
This closes the earlier pending placement-count check, not the broader reentry, wake, MCP, or native transaction proof.
Publication failure records an honest payload-zero attempt rather than a granted-size claim, and its blocked binder stores the actual sequence without waking countries.
The current Special Forces folder guard blocks replacement of an unregistered active Grand Doctrine.
The peer controller-edge contract counts qualifying own Event027 receipts from a human-started batch even if AI resolves them, without a new per-receipt execution-owner condition.

The spreadsheet worker's exact two-cell repair is implemented and exported.
The prior parent claim that Event Details and evolutions were stale is superseded by the worker's exact-match source evidence.
The semantic Event Details mechanics-versus-premise rule conflict remains a separate design/wording decision.
Joint Curriculum source/subject approval is explicitly parent visual evidence, with final state promotion still owned by the specialist.

Fresh parent production stdio initialized within the 30-second bound as `hoi4-agent-tools` 3.6.0 and verified the live `reference_search` schema.
Its corrected HasAnyGrand query used `game_doc` and limit 1, then timed out after 30 seconds with zero stderr bytes.
Initialization and schema delivery succeeded, while the query delivered no source citation, revision, analysis artifact, or engine verdict.
This is newer transport evidence than the earlier initialization timeouts and supplies no successful current domain/MCP proof.

Every criterion remains subject to the full acceptance file.
The following groups map the complete checklist to resume work, without marking any criterion passed from a status label.

| Acceptance group | Source evidence or owner work | Disposition |
| --- | --- | --- |
| Event identity and registration | Canonical forced console root and Minor Repeatable registration exist. Settings now has a separate direct Event027 dispatch. Default enablement includes 27. Cluster 9/member 9001 exists. | Implemented source registration, unresolved readiness and complete dispatch validation. |
| Global participant snapshot | Late owner source separates captured recipients, append-only publication, and wake scheduling. Architecture and final source integration are still under review. | Unresolved implementation review and overlap/lifecycle validation. |
| Baseline choice rules | Adoption and assigned-track actions exist. Empty-track first-step gate is closed. | Implemented source surfaces, blocked empty-track capability and native reward proof. |
| Exact mastery behavior | Grouped getter and point/readback loops exist. Low/middle/final, fractional, banked, completion, and interrupted cases lack native proof. | Blocked. |
| Doctrine-domain registry | Static domain/track identities exist. Special Forces both-occupied readback remains fail-closed. Future custom rows require full contracts. | Unresolved graph, DLC, level coverage, and current domain MCP validation. |
| Chaos Warfare integrity | Existing source owner gates remain design requirements. No downstream unlock or readiness acceptance is inferred from registry presence. | Unresolved owner-system/native scenario validation. |
| Evolved batch sizes | One through five size constants and stage recording exist. Immutable per-firing snapshot delivery and timing remain open. | Implemented source definitions, unresolved timing and delivery. |
| Stacking and distribution | Choice chain and per-choice rebuilding exist. Empty-track closure limits adoption-to-first-step and fresh-branch routes. | Blocked full-route acceptance. |
| Batch queue and persistence | Alignment, zero-choice AI closure, finalization guard, and pending ID repairs exist. Long scans, control changes, annexation/release, and interruption require proof. | Implemented source repairs, unresolved queue/persistence acceptance. |
| Human choice flow | Current localisation audit repaired concise labels, People's War maximum display, and ambiguous closure wording. | Implemented bounded text fixes, blocked current fit/navigation/popup evidence. |
| AI behavior | Four source chooser pools and centralized scores exist. Neutral Navy floor, future maritime plan signal, generic factors, parity, and rescoring require named evidence. | Blocked specialized probability validation, recommendations unresolved. |
| Repeatable-event balance | Shared cap/recovery source exists. Complete active pool, cadence, resets, starvation, and sequence manifest are unbound. | Blocked probability/sequence conclusions. |
| National Breakthroughs cluster | Runtime now has cluster 9 and one Event027 member 9001. Six accepted future concept members remain runtime-absent until their own reworks. Exact Calm override affects this row only. | Implemented bounded source registration, blocked cluster probability comparison and unresolved complete runtime/catalog crosswalk. |
| Event Logs and Event Details | Nine selectors and four catalog rows exist. A late owner payload producer/binder is present, with exact actorless single-row sequencing still under review. | Implemented selector repair, owner producer implementation in progress, blocked transaction/consumer evidence. |
| Achievements | Country-owned receipts, human-start metadata, debug/forced exclusions, and native summary readback exist. | Implemented source corrections, unresolved complete predicates/origin coverage and positive/negative cases. |
| Assets and presentation | Existing report and nine achievement files have historical evidence and an active independent visual review. | Unresolved fresh DDS/consumer review. |
| Documentation and catalog | This ledger reconciles current bounded status. Overview remains parent-owned. Spreadsheet owner changed only M28/G44, verified Details/evolution exact matches, and ran all exports. | Implemented bounded documentation/catalog reconciliation, unresolved full feature closure and separate Event Details rule conflict. |
| Mandatory evidence and audits | Current October source/reference handoffs exist. Required event/doctrine/GUI/probability outputs are absent or failed. | Blocked. |
| Completion claim | Full criteria remain required with no accepted reduced feature. | Unresolved. No feature completion or current playability approval. |

## Confirmed source risks and validation boundaries

### Late shared-tree observation

Source hashes changed during final curation, so the earlier October owner handoffs are not a frozen final implementation snapshot.
The latest observed `doctrine_research_fire_global_batch` allocates persistent firing envelope arrays and captures participant scopes before an append pass.
The append helper writes the firing ID and captured profile into each country batch without directly starting that batch.
The owner supplies a History size override, defines `doctrine_research_bind_firing_history`, adds `doctrine_research_wake_country_batches` and receiver `chaosx.nr27.14`, and adds an Event027 direct dispatcher arm separate from generic root/type handling.
The console root explicitly records forced setup before calling the same owner transaction.
The producer performs no owned work after the shared repeatable handler, matching the parent's requested reentry boundary.
These are source edits observed while the owner is implementing the architect's recommendation, and the parent explicitly reports an active reentrant architect review.
The earlier snapshot at shared-log SHA-256 `F8C48D9F273E5757A199CB7B23F42A935851B125A46E024934354ABBED129D6B` placed the sole binder call in `record_events_log_system_history_entry`.
That historical finding is superseded by the parent's immediate source correction, explicitly confirmed in the current follow-up instruction.
Current shared-log SHA-256 `7FDE6B681E3BD62A38EB2C01A22FFAB8FC262AD2B0E37E7D0FEDE43C028D9B81` has one call at line 819 inside `record_events_log_history_entry`, after the Brilliant Scientist callbacks and before override reset at line 821.
The system recorder contains no binder call in this source read.
Disposition: binder placement implemented in parent source, with the latest parent report confirming the normal-recorder AST call count of one and no system-recorder call.
The curator's bounded source read is separate from that parent AST report and supplies no MCP or native execution proof.
Complete delivery, reentry/overlap, delayed execution, and required MCP/native evidence remain unresolved.

| Source | Latest observed SHA-256 |
| --- | --- |
| `common\scripted_effects\027_doctrine_research_effects.txt`, publication-failure correction | `B17677AD2809791243A6E2107331F43F2B9A62233DDE1FBF01D500FEED9E6DCD` |
| `common\scripted_triggers\027_doctrine_research_triggers.txt`, Special Forces folder guard | `F072DD1D70F7C8AEE0EBFC002D2967E119578AA08733FCA65806F4C6619D0A60` |
| `common\scripted_effects\027_doctrine_research_achievement_effects.txt`, unchanged owner receipt tracking | `809EDBF5DF1BC4CBEB7E0AF8B908BACA994678DAB72A503149ACDC4C1D0BA2FE` |
| `common\scripted_effects\027_doctrine_research_exact_mastery_effects.txt` | `F71A4E67065DBA82C9ABC7944EF8BC8FF6F3ACCE837E3AEE6D385ADC3F1F32CD` |
| `common\scripted_effects\chaosx_events_log_effects.txt`, parent binder correction | `7FDE6B681E3BD62A38EB2C01A22FFAB8FC262AD2B0E37E7D0FEDE43C028D9B81` |
| `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` | `641A78580E2291C97C0F45FF8EFC0397E26812CAD39A25C9A6B759BF34DCDB8A` |
| `common\scripted_effects\chaosx_settings_effects.txt` | `12090796F3234663EAD13AD3B755DB683947440C37592A910239115529C59A29` |
| `common\scripted_effects\chaosx_event_cluster_effects.txt` | `589D0AF4E736B62C234B438FCA3922893E48D3C520F3E93ACB4C6FB3C895EF41` |
| `common\script_constants\event_cluster_constants.txt` | `C76988B9618E0D2EDDBDDA275DDF8A910613129061DCA335EEECB59C457625F7` |

These identify observed bytes, not verified MCP revisions or an immutable complete worktree.
Relocate source citations by helper name after further owner edits.

### Open engine and owner limits

Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:3156-3170` was read directly for `has_any_grand_doctrine`.
It describes a country-scoped check for any currently assigned Grand Doctrine in the given folder, at SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.
The parent cites the installed Special Forces native-folder definition at line 37, without a concrete folder-file path in this prompt.
That parent folder evidence is retained without inventing a file citation or executed trigger verdict.

The current `doctrine_research_start_next_batch` scans `doctrine_research_batch_ids^num` from the first index.
The current receipt finder scans `doctrine_research_receipt_ids^num` from the first index, and parent-link validation nests receipt and batch scans.
The human-start migration also uses `for_loop_effect` over its missing tail.
Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\defines\00_defines.lua:25` sets `MAX_EFFECT_ITERATION = 1000`.
Unlimited queue reachability, receipt recovery, migration coverage, and nested-scan correctness therefore remain unresolved for growing append-only ledgers.
Moving activation into a receiver alone does not resolve those bounds.

Current `doctrine_research_mastery_transaction_is_verified` still tests registry initialization, while the selected native adapter also checks built-in domain identity.
The empty-track wrapper is separately closed.
Treat available assigned-track mastery as source availability, not native transaction verification.
The native audit's repeated-point mutation, unmeasured bank, delayed readback, and no-rollback findings remain open.

The probability baseline records a positive neutral Navy adoption floor without current readiness, no explicit future maritime plan predicate, and broad shared score terms.
These are conditional source risks, not measured shares, dominance, or approved tuning targets.
The empty-track gate changes the weighted valid pool and still requires the specialized same-scenario baseline/final comparison.
Preserve the four frozen source files and the scenario matrix unchanged.
Do not duplicate the ongoing probability owner audit or compare a current file to itself.

The cluster repair additionally preserves two before-source files under `docs\plans\027_doctrine_research_plans\probability_cluster_baseline_20261003\`.
`chaosx_event_cluster_effects.txt` hashes to `D8211DA66BB429A5C00D2C51EEFDC462D36D8A210BDE1BC3DF2D66F8DC25BDC2`.
`event_cluster_constants.txt` hashes to `E74A71FA4612452F80DFB651D762B39EB5AD6DD7EB41A3D08FA1FA5E741D349F`.
Both were reopened and hashed without editing them.
The parent reports participation-matrix coefficients unchanged and requests a real cluster probability comparison.
This curator inspected the exact effective-min override, not a numeric probability result.

## Contradictions, stale instructions, and disposition table

| Document or claim | Disposition | Evidence, replacement, or exact blocker |
| --- | --- | --- |
| `review_closure_refresh_2026-09-04.md` current/source-playable and evidence-only claims | Superseded | This ledger and the October closure notice replace current status. Owner History/cluster repairs, corrected binder placement, and parent-reported one-call AST check exist. Empty capability, long ledgers, and acceptance remain open. September findings are preserved as dated evidence. |
| `mcp_evidence.md` September current-authority, playability, indexed grant, and accepted-asset claims | Superseded as current status | October header distinguishes current blockers from historical URIs/revisions. Live index rejection supersedes numeric grant syntax recommendations. Parent approved the new Joint Curriculum master/subject. Final promoted states and MCP/native evidence remain pending. |
| `docs\plans\027_doctrine_research_plans\documentation_state.md` September ledger | Superseded as current status | Replacement is this events-folder ledger. Old source hashes, successful partial tools, spreadsheet status, and claimed source playability are historical. File left unchanged outside ownership. |
| `native_transaction_audit_2026-10-03.md` and `parent_native_repairs_2026-10-03.md` numeric grant-filter recommendation | Superseded for grant-filter spelling | `live_qa_index_filter_repair_2026-10-03.md` and commit `f9978e9` replace that recommendation. Native banking/mutation findings remain open. Numeric `set_sub_doctrine.track` is preserved. |
| `parent_queue_correction_2026-10-03.md` | Implemented in source | Alignment, zero-choice AI closure, and guarded finalization directly confirmed. Saved mechanic fixture has no successful verdict. |
| `parent_native_repairs_2026-10-03.md` exact pending ID and level delta separation | Implemented in source | Current receipt lookup matches ID/batch/choice. Engine, repeated-finalization, and interruption tests remain unresolved. |
| `integration_audit_current_2026-10-03.md` missing nine selectors/four previews | Superseded for those source findings | Current source and the localisation handoff appendix confirm the parent repair. Its producer, readiness, actorless History, and MCP limitations remain relevant. |
| `localisation_audit_resume_2026-10-03.md` bounded fixes and follow-up appendix | Implemented in source | Latest appendix supersedes maximum-level Milestone inference and missing-selector findings. Spreadsheet owner verified exact current Details/evolution matches. Text fit, eligibility wording caveat, and the separate mechanics/premise policy remain open. |
| `probability_baseline_resume_2026-10-03.md` | Blocked | Correct `random_list` inspect timed out after 600 seconds. Narrow stdio initialization/listTools timed out after 60 seconds. No analysis artifacts or accepted scenario results exist. |
| `firing_profile_transaction_review_2026-10-03.md` direct dispatch recommendation | Implemented in owner source with unresolved review | Parent records direct dispatch, persistent envelopes, append-before-wake, forced console bridge, failed-publication recovery, and one normal-recorder AST binder call. Active reentrant review and missing MCP/native evidence prevent an acceptance claim. |
| Older August/September handoffs and spreadsheet/asset passes | Superseded as current status authorities | Preserve provenance and artifact identities. Use October owner reports and this ledger for current claims. No deletion or approval revocation is performed. |
| `027_doctrine_research_catalog_cluster_handoff.md` provisional 9 and “Implemented” catalog suggestion | Implemented source identity and bounded catalog policy correction | Runtime 9/member 9001 is present. Spreadsheet owner corrected M28 to `To Be Reworked` under the current post-20 root policy, without Playable approval. Spec's outdated status suggestion remains preserved for parent reconciliation. |
| National Breakthroughs members 54, 65, 67, 83, 85, and 89 | Accepted and queued | Latest parent direction preserves all six accepted future concept members. They stay runtime-absent because their own reworks are unfinished. The Event027-only runtime row does not approve their implementation or a permanently reduced cluster. |
| Earlier current cluster-absence finding | Superseded by owner repair | Cluster 9 and Event027 row 9001 now exist. Current effective-min override is exactly 9/27/9001 at tier 0. Frozen cluster before-source and mandatory comparison remain. |
| Misplaced repeatable History binder hook | Implemented parent source correction, original finding superseded | Parent confirms normal-recorder insertion after Brilliant Scientist callbacks and before override reset, then reports AST count 1 there and no system-recorder call. Source read agrees at revision `7FDE6B681E3BD62A38EB2C01A22FFAB8FC262AD2B0E37E7D0FEDE43C028D9B81`. All MCP/native delivery proof remains pending. |
| Publication-failure accounting | Implemented source recovery | Parent direction and source show current-firing-only last-row quarantine, cleared recipients, one actorless pacing attempt at payload 0, and blocked-sequence binding with no wake. Runtime failure-case proof remains open. |
| Special Forces custom-active doctrine replacement gap | Implemented source guard | Folder-wide `has_any_grand_doctrine = special_forces` blocks adoption when any Grand Doctrine is active. Parent reports native-folder identity evidence, and installed trigger documentation was read locally. Other domain predicates were not changed. Native/MCP proof remains unavailable. |
| Peer controller-edge achievement restriction | Accepted existing contract preserved | Latest parent explicitly preserves human-at-batch-start eligibility and own Event027 receipts, including AI-resolved receipts. No per-receipt HumanExecuted field or additional ban is authorized or added. Existing campaign-valid checks remain. |
| Current workbook stale Details/evolution claim | Superseded by exact-match evidence | `spreadsheet_refresh_2026-10-03.md` disproves the earlier parent claim. C28 and D28:G28 already matched source. Only M28 status and G44 membership note changed, followed by export. |
| `spreadsheet_refresh_2026-10-03.md` | Implemented bounded catalog repair | Exactly M28 and G44 changed, with no other cell/style changes reported. Event export changed, cluster/scenario export hashes stayed identical. Workbook after hash is `3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67`. No gameplay acceptance follows. |
| `achievement_asset_visual_refresh_2026-10-03.md` candidate-awaiting-approval finding | Superseded for approval, final promotion in progress | Latest parent visually approved the new 1280 master and 64x64 subject with complete four-part artwork. The older handoff's candidate dimensions/hashes are not assumed to identify that approved artwork. Specialist is promoting three corrected final states. |
| `027_doctrine_research_doctrine_registry_matrix.md` present-tense empty-track support | Blocked implementation claim | The accepted safe-transaction requirement remains. Current empty-track capability is closed pending its native proof. Do not reroute into a fallback reward or silently remove the criterion. |
| Default enabled source versus acceptance criteria readiness | Unresolved | `chaosx_settings_triggers.txt:25` includes 27. Acceptance criteria require full rework readiness before default enablement. Source inclusion is not acceptance evidence. |
| Presentation spec mechanics wording versus current prose-only Event Details rule | Unresolved | Part 4 asks for adoption/mastery and choice-count explanation. The localisation audit flags its conflict with AGENTS.md. Parent must record precedence within the user-authorized scope. |

No documents are merged or deleted.
The two older owned documents retain historical records with named replacement notices.
The spec prompts remain full-scope implementation instructions, not proof that their described feature exists.
Their role names and source paths are preserved.
The spec README's “complete playable loop” is a design description and cannot establish current playability.
Do not repeat completed compatibility, selector, or localisation repairs from an earlier handoff.

## Parent resume sequence and decisions

1. Review the bounded source repairs against current bytes and retain `f9978e9` as the committed compatibility repair only.
2. Retain the parent-reported one-call normal-recorder AST check and review the success/failure publication paths, then verify one immutable profile/participant snapshot, all country rows before wakes, truthful actorless attempt/grant History, and overlap/delayed delivery through the required evidence routes.
3. Address finite-ledger scan coverage and migration/recovery reachability without claiming unbounded queue support.
4. Keep empty-track assignment blocked until its accepted native bank transaction is supported by evidence.
   Do not describe Grand Doctrine adoption or assigned-track actions as full feature playability.
5. Resume the probability auditor from the unchanged frozen sources and 37 named scenarios, with exact native inputs and a complete recurrence/cluster manifest where required.
   The changed valid pool still needs the real baseline/final comparison.
6. Verify the new cluster 9/member 9001 source and exact Calm override through the specialized comparison without treating the six queued concept members as implemented.
   Preserve the implemented M28 `To Be Reworked` policy and exact-match catalog wording, while resolving default-enable readiness and the separate Event Details mechanics/premise precedence.
7. Review specialist promotion of the parent-approved Joint Curriculum artwork and fresh final triplet identities without repeating source approval or assuming the older candidate hash identifies the approved master.
8. Refresh required event/doctrine/GUI comparisons and source-specific audits before any feature completion claim.

The historical ledger's old index-lock and commit instructions are not current authority.
No index state was inspected or modified by this curator, and no commit is requested or created.
No save was supplied and no game was launched.
No accepted criterion was reduced, no gameplay substitute was introduced, and no skill was created or updated.
