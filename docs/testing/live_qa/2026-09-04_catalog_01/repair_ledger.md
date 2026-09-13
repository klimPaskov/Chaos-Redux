# Confirmed defects and repairs

Two pre-menu crashes and their fresh startup errors are recorded below.
Old logs were archived separately as a baseline.
No live feature case has passed, and bug evidence remains outside the teaser content dump.

## Launch 01 — startup crash, repair 01 awaiting retest

HOI4 PID 3736 launched through the supplied shortcut at 2026-09-04 23:40:51 local time and crashed at 23:41:13 before the main menu.
Fresh log timestamps confirmed the active log directory, and crash metadata identified Chaos Redux as the loaded mod with debug enabled.
The exception was C0000005; its unsymbolized stack does not yet establish the faulty asset or script.
Evidence is in `logs/launch_01/`.

- `localize.cpp:1639`: Localization file `localisation/english/012_africa_gods_l_english.yml` should be in utf-8-bom encoding.
- `pdx_localize.cpp:1031`: Missing UTF8 BOM in the same file.
- `pdx_audio.cpp:337`: Missing sound `chaosx_super_event_random_terror_false_revelation_defeat_aftermath_track` (six occurrences).
- `assetfactory_audio.cpp:577`: SoundEffect names for slots 111–116 lack a category (36 occurrences).

The localisation repair prepends the BOM without altering existing content.
The sound repair registers all six volume variants for slots 111–116 in the existing Effects category.
The missing internal sound token has 72 characters; it and its six references were shortened to `chaosx_super_event_115_track` while preserving the existing WAV, public playback IDs, volumes and intended content.
Token length is a working hypothesis, not a confirmed engine limit; fresh relaunch will determine whether the missing-sound error clears.
Original edited files are preserved under `pre_patch_01/`.
No live fix acceptance or crash resolution is claimed yet.

## Launch 02 — audio errors cleared; GUI parse errors and crash remain

PID 32932 launched on 2026-09-05 at 00:31:37 local time and crashed at 00:32:23 before the main menu.
Fresh logs contain none of the launch-01 audio category, missing-sound, or localisation BOM errors.
Both crashes have the same reported executable offsets, so the audio repair is not sufficient to explain or resolve the crash.
Evidence is in `logs/launch_02/`.

The remaining 14 errors are `persistent.cpp:67` unexpected `size` tokens in `interface/camp_repression_ledger.gui` at lines 15, 17, 20, 23, 26, 29, 34, 38, 39, 149, 152, 155, 165 and 173.
They correspond exactly to decorative `iconType` elements with explicit dimensions.
Vanilla `interface/airselectionview.gui` uses `buttonType` with `size = { x = 410 y = 30 }`, while the offline Interface modding reference documents click-through `alwaysTransparent` and frame support for buttons.
A candidate changes only those 14 element-kind tokens to `buttonType`, retaining every name, dimension, position, sprite, frame and click-through field.
The candidate is `camp_repression_ledger_candidate.gui` in this QA folder and has NOT been applied to the runtime GUI.

### GUI validation blocker

Two valid calls to `hoi4.gui_inspect` with window `repression_ledger_window` and scenario id `startup_repression_default` timed out after 180 seconds each.
Earlier requests without a scenario or without `scenario.id` were rejected by schema validation and were corrected.
Required inspect/render/rewrite evidence remains unavailable; source comparison is not a substitute for it.
Desktop control remains suspended under the user's instruction until startup crashes and errors are repaired.

### Production GUI route recovered

The installed service documentation identifies a client timeout limitation and supports longer calls with progress notifications.
A dedicated SDK client invoked the same installed production `hoi4.gui_inspect` route with a 600-second request timeout and received `GUI_INSPECTED`, status `ok`.
The request emitted source-graph progress and completed; `mcp_gui_inspect_result.json` preserves its result and artifact references.
This resolves the inspection transport blocker without changing service code, project runtime settings, or GUI source.
The baseline render and bounded rewrite remain pending.

### Bounded GUI candidate validation

The production baseline render completed for the overview panel at 2560 × 1440 with explicit panel visibility.
The first rewrite candidate changed all 14 sized icons to buttons and produced no pixel difference, but validation rejected seven passive backgrounds because buttons require effects.
That candidate was not applied.
The revised candidate uses sized containers with sprite backgrounds for the seven passive panels and sized, click-through buttons for the seven selection highlights.
Its production rewrite validation is pending; positions, dimensions, sprite references and existing selection visibility bindings are preserved.
The original all-button candidate file is superseded by the source in `gui_rewrite_arguments.json`.
Neither candidate is live-game acceptance evidence.

### Native crash evidence

Read-only minidump analysis found the same image-relative fault address in both launches: `hoi4.exe + 0xA9868A`, on matching build `a729d47...`.
The reported PhysFS export name is the nearest exported symbol rather than a reliable function attribution.
The faulting instruction dereferences `r14 + 0x20`; the available dumps do not contain a usable exception context to identify that pointer or the originating asset.
This evidence does not establish that the GUI parse errors caused the crash.
If the crash persists after the confirmed parser errors are repaired, a full crash context is the next diagnostic rather than attributing it to an arbitrary asset.

### Rewrite retry status

The revised container/button candidate timed out after 600 seconds while reporting `Preparing GUI rewrite`.
The runtime file still contains the original sized icons; no successful rewrite is claimed.
A retry of the same production route is running with a 1800-second SDK timeout, without modifying the service or project configuration.
Current execution session: `87585`; inspect its result before launching another request or changing the GUI file.
The full result, if returned, will be written to `mcp_gui_rewrite_result.json` and artifacts to `mcp_rewrite_artifacts/`.
The protected concurrent event set remains 6, 12, 16 and 23 after the user's retracted all-work-stopped message.

### Production rewrite rolled back after validation

The 1800-second retry completed with `REWRITE_POST_VALIDATION_FAILED` and `automaticRecovery: restored`.
The proposed package passed source syntax and visual preflight, and `repression_ledger_window-visual-diff.json` reports zero changed pixels at 1920 × 1080.
Post-write validation rejected unresolved vanilla sprite references including `GFX_button_148x34`, `GFX_button_238x38` and `GFX_closebutton`; their definitions were verified in installed vanilla `interface/core.gfx` lines 526 and 546 and `interface/general_stuff.gfx` line 202.
It also reported global diagnostics in other files and exceeded its graph diagnostic ceiling.
This is a production validation blocker, not successful acceptance; the runtime parser fix remains unapplied.
The exact 14-element change, reviewed against the restored current file, is `repression_parser_fix.patch`.
The downloaded bulk post-validation resource ends mid-string at 1,048,576 characters, so it is incomplete and cannot support exhaustive diagnostic claims; the execution-validation resource is readable.
The scripted-GUI skill requires applying the package through its rewrite route, so a direct application requires a user-approved workflow exception before continuing startup validation.

## Independent decision parser repairs — awaiting live acceptance

Production post-validation exposed two source errors outside the GUI transaction.
Six dust-protection checks in `common/decisions/028_asteroid_incoming_decisions.txt` combined the long-form `var =` assignment with shorthand `>` syntax.
They now use the installed `check_variable` documentation's shorthand comparison, with the same global dust variable and minimum constant.
Eight mission definitions in `common/decisions/031_random_terror_missions.txt` were top-level blocks rather than children of a decision category.
They are now nested under the already defined `random_terror_government_response_category`, matching the response decisions that activate them and the mission file's stated intent.
All mission bodies, thresholds, effects and AI weights are unchanged except for indentation.
Originals are archived under `pre_patch_02/`.
These are source repairs supported by installed trigger documentation, vanilla decision structure and the offline Decision modding reference; they have not yet passed a fresh live startup or mission behavior test.
They do not modify protected events 6, 12, 16 or 23.

### Repeated mixed comparison syntax repaired

The same malformed long/shorthand comparison appeared in 36 checks in `common/scripted_effects/029_riches_found_effects.txt` and three in `common/scripted_effects/029_riches_found_log_effects.txt`.
Only the redundant `var =` assignment was removed from those checks; operators, scopes, constants and surrounding effects were preserved.
The 39 changes cover existing public-value limits, evolution comparisons, controller caps and history-sequence guards.
Originals are in `pre_patch_02/`.
The production event inspection used selector `{ kind: event, eventId: chaosx.nr29.1 }`, trace depth 1, 8 nodes, 12 edges and helper expansion disabled.
It returned `EVENT_INSPECTED_PARTIAL`, revision `fa39cc8b8775d170afcffd913b819e19d58668724ce547e0ec5a30ae5e8610a1`; workspace-wide helper/lifecycle analysis was deferred and this is not a full event validation pass.
Artifact identity: `event-trace-fa39cc8b8775.json`, SHA256 `b56c3e3474baebf1a25d2bf6a4d6443d3f3a7c60dbb6f04aa45573c0721aac6a`.
Fresh game validation remains pending the GUI workflow exception.

## Resumed autonomous run and launch 03

The user explicitly approved direct GUI edits and autonomous testing, and the updated scripted-GUI skill makes `gui_rewrite` optional.
The previous workflow-exception blocker is resolved.
The 14-element parser fix was applied to the current file while preserving intervening title and label alignment edits.
The exact applied diff is `applied_repression_parser_fix.patch`; the current-source backup is `pre_patch_03/camp_repression_ledger.gui`.
Launch 03 began through the supplied shortcut at 2026-09-05 09:21:44 local time, PID 17756.
Its fresh `error.log` stayed empty, but the game crashed before the menu at 09:22:14 with the same native RVA as the previous launches.
Evidence is archived under `logs/launch_03/`.
This proves that the parser fixes cleared the observed startup error log but does not prove crash resolution or a clean main-menu launch.
Fresh `text.log` also reports duplicate localisation keys, including event description/option collisions; a bounded localisation worker owns those repairs outside protected events.

## Launch 04 — full exception capture

Microsoft Sysinternals ProcDump was downloaded from its official distribution and its Microsoft Authenticode signature validated.
It monitors only the launched HOI4 process for one C0000005 exception, with WER upload disabled and no system-wide debugger registration.
The supplied shortcut launched HOI4 PID 24832 at 09:24:15; ProcDump PID 24688 captured C0000005 at 09:24:33.
The full dump is being written to `.tools/qa/dumps/launch_04/hoi4.exe_260905_092433.dmp`; this large diagnostic file is not teaser or commit content.
The capture log is UTF-16LE at `.tools/qa/dumps/launch_04/procdump.log`.
Do not launch another game while this capture owns the process; verify capture completion and process state first.
The dump completed at 09:28:04 local time (4,500,024,040 bytes); ProcDump then exited and no HOI4 process remained.
Launch 04 logs and the capture transcript are archived under logs/launch_04/.


## Duplicate localisation repair checkpoint

Parent review accepted the six-file localisation repair documented in localisation_duplicate_repair_handoff.md.
Event 25 and 31 option labels now have distinct keys from their descriptions; event effects and weights are unchanged.
Eleven launch-log duplicate keys have been consolidated or renamed, with fresh engine acceptance still pending.
Eight remaining Event 16/shared raid keys have conflicting wording and remain deferred to active ownership; they are not claimed resolved.
The Chaos Meter render succeeded, but its final visual artifact still needs direct review because the worker received a truncated resource envelope.


## Launch 05 diagnostic probe

Full dump evidence implicates a parsed Form48 constant object but does not prove the failure phase.
A reversible three-line probe shortens carrier_support_equipment_availability_threshold to support_minimum in its definition and two consumers; value 99 and both comparisons are unchanged.
Original files are archived under pre_probe_05/. This is a diagnostic candidate, not an accepted permanent repair.
Event 6 MCP trace returned EVENT_INSPECTED_PARTIAL at revision f9436dee3f5cb09c3bdc4a12354936955b1f81519dcc79453867ce4504c92978; full lifecycle acceptance is not claimed.

Launch 05 PID 18116 started at 09:48:24 and crashed at 09:48:42 with the same native stack and empty error.log.
Shortening the constant identifier did not resolve the crash; the three-line diagnostic change was reversed immediately.
The original constant and consumer identifiers are restored; this experiment is rejected as a repair.


## Launch 06 diagnostic probe

A file-local constant @FORM48_SUPPORT_MINIMUM_PROBE = 99 temporarily replaces the implicated registry constant and both consumers; the registry entry is omitted for this launch only.
This isolates the registry entry/lookup path without changing the two equipment thresholds.
The original baseline remains pre_probe_05/ and this is not an accepted permanent change.

Launch 06 PID 22572 started at 09:51:13 and crashed at 09:51:20 with the same stack and empty error.log.
Removing the implicated registry entry and both lookups did not resolve the fault; the original two files were restored byte-for-byte after guarded comparison.
This rejects the single-entry probe as a repair and leaves a broader constant/schema loading failure under investigation.


## Concrete schema repair after resumed goal

The current-state scalar/array schema audit scanned 3,608 categories and found seven Event 16 tables without schema declarations plus three using unsupported any_value instead of data.
Installed common/script_constants/documentation.md requires schema first and data = int/fixed_point for scalar categories; installed country/state-group files establish the separate valid array schema.
Seven matching scalar schemas were added in 016_brilliant_scientist_raid_lifecycle_constants.txt; three any_value fields were corrected in the custom-technology and technology-action constants files.
Identifiers and numeric values are unchanged. Originals are in pre_patch_schemas/. Event 16 focused MCP trace returned EVENT_INSPECTED_PARTIAL at revision d1b1deacde71076676d9f3a8922e7d45b97be37b957c82abd5293f57c6ee523a.
Seven fractional values declared as int in events 12, 35 and 39 remain for separate targeted review.
The user goal continuation resumes necessary repair work; this launch tests confirmed schema fixes, not another single-key experiment.

Launch 07 PID 22276 remained alive past the former crash and completed substantially more startup loading, exposing later parse, reference and asset errors.
No main-menu visual proof was captured and no campaign was entered.
The recorded process was stopped for repair after logs were archived under logs/launch_07/logs/.
The schema correction removes the observed early failure in this launch, but overall startup acceptance remains failed.


## Supported effect keyword repair — pending launch validation

531 exact log-reported source occurrences across10 scripted-effect files were corrected using installed effects documentation: clear_country_flag to clr_country_flag (442), clear_global_flag to clr_global_flag (15), add_army_experience to army_experience (19), remove_idea to remove_ideas (36), and add_idea to add_ideas (19).
The candidate manifest records original source lines and identifiers; the guarded patch preserved all arguments and surrounding logic and archived originals under pre_patch_effect_aliases/.
Valid add_idea/remove_idea fields inside swap_ideas were not globally replaced; only engine-reported effect calls matched the repair manifest.
No temporary-variable cleanup, event-target semantics or weighted logic was substituted.
See effect_alias_mcp_evidence.json for focused event28/34/39 inspection artifacts; otheraffected eventinspections are part of the parallel worker evidence. Full lifecycle validation remains pending.


## Event 27 mastery parser repair — pending engine acceptance

107 add_mastery amount fields rejected constant:doctrine_research_event.mastery_point_increment, followed by misleading Invalid effect index errors.
Installed effects_documentation.md:1477 explicitly supports the index/folder/sub_doctrine/track filters, which are retained unchanged.
Only the amount field now uses a documented file-local @ constant equal to the authoritative shared increment1; the header records its source linkage.
The original is under pre_patch_mastery/. No mastery target, filter or step/readback guard is removed.
MCP tech_inspect explain for mobile_infantry returned TECHNOLOGY_NOT_FOUND; this route did not resolve the installed modern subdoctrine, so no MCP doctrine acceptance is claimed.
Installed doctrine documentation and engine error lines are the direct repair evidence; live mastery and fresh-parser acceptance remain pending.


## Timed flag keyword repair

Six calls in031_random_terror_effects.txt and one in events/030_time_traveler.txt now use set_country_flag with their existing flag/days block.
All seven days fields already use duration variables, which are retained; no timer value or flag identifier changed.
Backups are under pre_patch_timed_flags/. Event30 focused MCP trace was partial at revision4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f, artifact sha c03408744d54e22bed73f543c7ec5a6f73c543ea68e8c30e251cee15a8e59e74.
The related decision calls belong to the decision worker; other constant-duration cases remain pending.

The parent reviewed and accepted the five-file idea modifier repair for next-launch validation; its handoff is docs/plans/026_black_friday_plans/subagent_handoffs/QA idea_startup_repair_handoff.md.



## Parent review before launch 08, 2026-09-05

Accepted the containment parameter repair after reviewing all eight action mappings, cancellation conjunctions, affordability predicates, effect-input initialization, and worker-only diffs.
The source evaluator covers 27,648 predicate comparisons, 198 affordability boundaries, and 72 cancellation receipt pairs; this is intended-semantics evidence, not native execution.
The three-file repair preserves costs, timers, AI, material debits, and concurrent recipient edits.
The separate containment temporary-cleanup analysis was accepted and the single terminal unsupported cleanup command removed; every current call initializes the scratch before reading and no downstream consumer observes it.

Accepted the Event 024 opinion/idea wrapper and two trait-ID repairs after reviewing the archived source diffs, localisation, GFX registration, and documented preservation of the parent effect-keyword fixes.
Accepted the Event 016 external reward idea repair: three file-local aliases retain the shared values 0.06, 0.04, and 0.02.

Repaired 12 unsupported timed-flag commands across Event 021 decision effects (3), Event 024 effects (2), Event 030 entry (1), and Event 031 effects (6).
The five Event 021/024 calls now assign their existing shared duration constants to immediately consumed temporary variables; the other seven already had valid duration variables.
All flag IDs and duration values remain unchanged.
Originals are in pre_patch_timed_flags/; the first exact CRLF-only guard for Event 021 rejected mixed line endings before any write, then the byte-preserving replacement handled each block's existing line endings.
Installed effects documentation, offline Effects set_country_flag entry, and vanilla GER timed-flag precedent support the command shape.
Event 021 narrow MCP trace returned EVENT_INSPECTED_PARTIAL, revision 524f2937a47d4d31bd89ec3b5e6185825935909d15ff955e2e35187522458d75, artifact cd0e4814f36e447ac23d52dd3bec906b7e7c97e76659d500ca8c96ab0f0bc15c; focused analysis excludes helper validation.

Corrected nine exact launch-reported effect names in events/024_hearts_of_iron.txt (3 army_experience), events/028_asteroid_impact.txt (2 remove_ideas), events/034_industrial_boom.txt (2 clr_country_flag), and events/035_great_depression.txt (2 clr_country_flag).
The guarded line replacements preserve all arguments and archive originals in pre_patch_event_effect_aliases/.
Existing narrow MCP evidence for these event roots remains partial and does not establish engine acceptance.

Fresh launch confirmation remains pending for this review checkpoint.
No menu stability, campaign testing, screenshots, recordings, or teaser acceptance is claimed.


## Launch 08 result and next repair batch

Launch 08 verification is recorded in launch_08_results.md and committed as a4abc7b.
The former crash did not recur during the observed startup interval, but 4,598 error-log lines remain; no visual menu or country-map pass is claimed.
The doctrine index errors persisted after all malformed mastery amount constants disappeared, so the prior cascade explanation is superseded.
The Event 021 decision repair was reviewed by exact full-file transformation: six army-experience gates, 23 political-power gates, and three experience effect names changed, with all other bytes preserved.
Worker artifacts initially written with a literal root QA prefix were relocated into this run folder with resolved-path safety checks.

Subsequent source changes awaiting launch 09 include the one-key Event 021 MTTH correction, three independently traced Event 021 terminal temporary-cleanup deletions, eight same-value containment hint aliases, six Event 031 focus reward keywords, the six-file decision parser tranche, and the 113-field Event 029 hint/command-power tranche.
The Event 029 nested AI modifier brace remains untouched pending its own probability baseline and owner acceptance.
The Event 021 MTTH post-comparison attempted genuine before/after bodies and identical scenarios; PROBABILITY_SURFACE_EMPTY prevents any timing validation claim.

The parent repaired Event 024's achievement debug gate from the nonexistent force_trigger_mode_enabled trigger to has_country_flag = force_trigger_mode_enabled, matching the settings flag writer and existing eligibility conventions.
Immediate original: pre_patch_event24_debug_flag/.
The parent repaired the single Event 023 unsupported timed-country-flag call using the supported set_country_flag and an immediately initialized duration variable sourced from the same existing constant.
This isolated active-package parser repair preserves all other source bytes; its original is under pre_patch_timed_flags/.
Event 023 narrow MCP trace was partial, artifact 76ae90a180bf3d462c2816bfd2b17b02f99c453e54631abf3d8d71be491f4196, and does not certify helper runtime behavior.

The parent accepted the raid constant baseline and substituted 22 rejecting static weight fields with same-value file-local aliases in four existing game raid files.
All outcome formulas, flags, AI scores, target definitions, and values remain unchanged; the exact mapping and hashes are in raid_modifier_constant_repair.json and originals in pre_patch_raid_weights/.
The installed probability adapter has no native raid outcome surface; a post-change comparison attempt remains required and cannot be presented as a native probability pass.

The existing eight Event 031 dormant flag designs were visually and contextually reviewed against their explicit tag-reset mapping.
The parent accepted that mapping for missing no-suffix direct tag bases, intentionally shared across ideologies until the existing cosmetic identity applies.
An asset worker owns installation of exactly 24 absent base TGAs; unrelated flag package identity/runtime statuses remain pending.
The repression parameter plan was accepted for an atomic eight-TXT plus owner API documentation migration; the worker owns its guarded implementation and matching MCP GUI evidence.
No major GUI or focus redesign was authorized or introduced.


## Temporary doctrine parser probe for launch 09

The installed v1.19.2 binary rejects the documented index field in all107 exact-mastery branches; no index omission or alternate targeting has been accepted.
A disposable unreferenced helper in common/scripted_effects/zz_codex_qa_doctrine_index_probe.txt tests only parser recognition of track_index, a token identified in the same binary by the read-only analysis.
The probe has amount0, is not registered with CXT or any event, and must never be executed in gameplay.
Its parser result alone cannot establish exact-track effect behavior.
Probe SHA-256 before launch:6c6f963972f48a1b24419901ab41e85c4583f8617e4b2c9874d4572d6e214d3d.
The parent must archive the probe and delete only its hash-matching runtime file after launch09, regardless of result.


## Launch 09 verification

See launch_09_results.md and logs/launch_09/comparison_counts.json.
The timed-country-flag and literal repression STATE errors disappeared, while the doctrine index family persisted.
The zero-mastery probe failed its own amount validation and was removed after archival; exact-track semantics remain unverified.
The direct Event 31 flag copies introduced confirmed 24-bit-format warnings, assigned for pixel-preserving 32-bit conversion.
No feature-level pass is claimed from these parser results.


## Launches 10–13 verified parser repairs

Native logs confirm corrected Event31 direct flag encoding, Event39 score bounds, Event31 mission-removal commands, 28 Event24 scratch cleanup removals, Event32 scenario syntax, 107 doctrine track_index fields, and Event32 helper registration.
The Event32 brace was applied independently during launch11; parent source guards preserved it and launch12 verified its stable source snapshot.
Its mandatory probability comparison remains PROBABILITY_SURFACE_EMPTY; Event29 comparison completed with unresolved FROM scope semantics.
Comment-only Event39 histories failed launch12; empty dated blocks passed launch13 with zero country setup effects.
Runtime exact-track awards, temporary input cleanup, regular event-target cleanup, dynamic-country reservation, visible GUI defects, and all live feature coverage remain pending.
See launch_10_results.md, launch_11_results.md, launch_12_13_results.md, and the specific repair handoffs for exact evidence.

## Launch 14 checkpoint

Launch 14 reached engine frontend startup completion and cleared all targeted diagnostics from the preceding repair tranche.
The error log remains nonempty; normalized distinct lines decreased from 746 to 721, with only reload bookkeeping newly present.
Eight tracked sources stayed unchanged; Event 32 operations changed independently and has no controlled whole-file acceptance from this launch.
See launch_14_results.md for exact hashes, comparison evidence, targeted repair limits, and source-snapshot provenance.
No campaign or feature-media coverage has begun, and the clean-start gate remains pending.

## Event 35 missing cadence helper investigation

Launch 14 reports undefined great_depression_set_pulse_interval in the national pulse helper.
The active-source search finds the call and subsequent great_depression_pulse_interval comparison, but no helper definition.
The severity specification, docs/specs/035_great_depression_specs/035_great_depression_spec_part_2_severity.md lines 195–214, requires phase-sensitive bounded cadence and elapsed-day normalization.
The existing great_depression_event.pulse_days = 7 constant alone does not satisfy that contract, so substituting a fixed seven-day interval would be an unapproved simplification.
This needs a bounded owner implementation review against the accepted cadence specification and existing hooks; no replacement helper or timer change has been made in this tranche.

## Launch 15 checkpoint

Launch 15 completed engine startup in 74473ms, then was stopped at the nonempty-error gate.
Nine repaired sources remained unchanged; Event 32 operations changed independently and its actual before/after bytes are archived.
Political-power aliases, two Event 28 reserve aliases, the Event 26 refund marker, and three Event 35 cleanup calls cleared their targeted diagnostics.
Acid Rain mission cleanup exposed two missing legacy mission IDs; these require correction before that repair can be accepted.
See launch_15_results.md and logs/launch_15/ for evidence and limits.
All campaign and feature-media coverage remains untested.

## Launch 16 checkpoint

Launch 16 completed engine startup in 58391ms, remained responsive, and was stopped at the nonempty-error gate.
The stale Acid Rain mission diagnostics and two Great Depression adapter cleanup diagnostics are absent; all four captured sources stayed unchanged.
Normalized distinct diagnostic lines decreased to 697, with no new family beyond an aggregate count.
See launch_16_results.md for exact evidence and runtime limits.
Current fresh native error source is logs/launch_16/logs/error.log; no HOI4 process remains.
Feature coverage, saves, teasers, all custom-unit recordings, and mechanics-guide media remain pending.

## Launch 17 checkpoint

Launch 17 completed engine startup in 117464ms and was stopped at the nonempty-error gate.
All fifteen targeted country-check corrections are parser-accepted, with ten tracked sources unchanged and no new diagnostic family beyond the aggregate count.
Normalized distinct lines are 683; fresh evidence is logs/launch_17/logs/error.log.
Event32 command-power and Event39 custom-pool probability limitations remain unresolved; no numerical probability pass is claimed.
Event24 foreign-event ROOT identity concern is recorded in launch_17_results.md and its handoff for follow-up.
Pending six Event32 core cleanup removals and 32 infrastructure comparisons were held until this launch ended.
No feature-media or campaign coverage has started.

## Launch 18 checkpoint

Launch 18 completed engine startup in 100042ms and was stopped at the nonempty-error gate; no HOI4 process remains.
Thirty-two registry infrastructure comparisons and six Event 32 core cleanup calls cleared their exact parser diagnostics.
All four tracked files stayed unchanged during launch; the current error log has 1940 lines and 678 normalized distinct lines.
See launch_18_results.md and logs/launch_18/ for full source/log evidence and runtime limits.
The next fresh-error source is logs/launch_18/logs/error.log.
No campaign, save, feature-media capture, guide media update, or custom-unit recording has occurred.
MCP probability reports remain partial where eligibility/resource/helper inputs cannot bind; no numerical acceptance is claimed.
Launch17 checkpoint commit was deferred by a shared index.lock created at12:55:11 while other Git processes were observed; it was preserved.
Completed checkpoint commits this tranche:6f0f3cddf (launch14),3681c41c9 (launch15),302e73478 (launch16).

## Launch 19 checkpoint

Launch19 completed frontend startup in78467ms without a crash and was stopped at the nonempty-error gate.
Seven tracked sources stayed unchanged, with1758 error lines remaining.
Five infrastructure comparisons, twelve building comparisons, twelve literal damage-field substitutions, and25 proven cleanup deletions cleared their targeted diagnostics.
See launch_19_results.md and logs/launch_19/ for the current native evidence.
No campaign or feature-media coverage has started; the comprehensive goal remains active.

Launch17–19 checkpoint commits remain deferred: the shared index.lock created at12:55:11 remains present, with other Git processes observed at13:41:45.
The lock is preserved; no source or checkpoint file was swept into an unrelated commit.


## Event32 observed source defect: scored state overwritten

Disposition: unresolved, source-observed and outside contracts20 repair authorization; no live behavior acceptance is claimed.
`missiles_select_operation_target_state` invokes the deterministic best-state selector and then enters `random_owned_controlled_state` whenever the selected country is valid, without requiring target_state_selection_result to be zero.
That branch assigns missiles_operation_target_state again and can overwrite the scored winner.
Evidence is in `event32_contracts20_handoff.md`, using operations source before SHA 54EAC3B29FE7980A16AA381AA860880A12D37C600B86DEC3428ED455923643CA around lines 1847–1861 and the byte-preserved continuation after contracts20.
Parent explicitly requested preservation of this unrelated random branch; a separate complete repair would require accepted fallback intent and appropriate selection/probability evidence.
