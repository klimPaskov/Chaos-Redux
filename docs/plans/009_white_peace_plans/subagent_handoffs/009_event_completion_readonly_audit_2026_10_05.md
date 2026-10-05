# Event 009 White Peace completion audit

Date: 2026-10-05.
Mode: read-only source and asset audit, with report artifacts only.
Audited baseline: Git HEAD `d5dca6a71a29a8d67e023a88cd6598bb51b300b2`, before the parent repair tranche.
Disposition: `blocked` for completion certification, with implemented source surfaces and the partial or unresolved requirements below.
No gameplay, localisation, GFX, workbook, CSV, or installed-game files were edited by this auditor.

## Authority and scope

The parent explicitly designated four documents as accepted source design for this task: `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md`, `009_white_peace_event_text_log_cluster.md`, `009_white_peace_dynamic_weight_model.md`, and `docs/specs/009_white_peace_specs/matrices/009_white_peace_safety_ai_acceptance_matrix.md`.
That current parent acceptance is the acceptance basis used here.
Older document locations, labels, and source implementation were not treated as additional approval.
The parent also supplied fresh USA 1936-01-01 force-entry feedback with Italy versus Ethiopia as the only war and skip reason `3`, `major_locked`.
The user requires an invalid force attempt to explain its reason or select a valid pair.

The parent gates are plain report/news text, at most one human popup per chain, aggregate success, concrete period prose, clear proportionate effects, visible asset quality, design authority, and useful invalid-entry feedback.
The audit covers Event 009 registration, dispatch, reports, evolutions, effects, triggers, constants, achievements, logs, details, assets, documentation, and current plan dispositions.
The accepted package deliberately excludes custom countries, focus trees, formables, dedicated scripted GUI, portraits, skeletal models, animated presentation, world-end branches, and super-events.
Those absent systems are outside the accepted requirement set and are not completion gaps.
Shared settings, event-log, and event-details windows do not require a `chaosx_event_ui_worker` handoff merely because Event 009 appears in them.

## Completion by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Root and registration | Implemented in source | `events/009_white_peace.txt:8` defines `chaosx.nr9.1`; `common/scripted_effects/chaosx_logic_effects.txt:288` retains repeatable event 9; `common/scripted_effects/chaosx_event_cluster_effects.txt:1349` registers the White Peace member. Required MCP inspection is blocked. |
| Automatic selection and cap integration | Partial | `chaosx_logic_effects.txt:534` calls the dynamic-cap helper and `:664` reads the availability trigger. Probability certification is delegated to the parent probability auditor and remains dependent on its result. |
| Forced entry | Partial, fails G7 | `chaosx_settings_effects.txt:4246` prepares targets and prevents dispatch when readiness is zero. This protects the major-stage rule, but no Event 009 reason is displayed from that rejection path. |
| Reports | Partial | `.2` through `.5` each have one acknowledgement option and reuse the report sprite. Current source targets only the selected primary country and executes the settlement from the option. |
| Aggregate successful settlement | Partial | `009_white_peace_effects.txt:1089` publishes the final pair count, but reports are written before that result exists and do not show it. Shared history is recorded before a human option can succeed. |
| Participant and war safety | Partial, unresolved engine boundary | Country and pair vetoes exist. There is no full participant closure, isolated-war proof, or verified narrower native settlement guarantee for a selected relation inside a larger war. |
| Evolutions | Partial | Stage calculation, branch weights, flags, history, and preview rows exist. The enable toggle gates recording but does not gate actual stage selection. |
| Chaos and memory | Implemented in source with validation limits | Pair and country flags, opinion memory, and capped branch-level Chaos deltas are present. Native callback timing and third-participant effects are not proved by this audit. |
| Achievements | Partial | All five registry entries, localisation, tracking paths, and icon triplets exist. Distinct-war tracking for The Circular is not proved and same-war five-pair behavior is not demonstrated. |
| Log, details, cluster text | Partial | Primary actor mapping, event details, evolution previews, and cluster skip-reason text exist. Dispatch-time history and stale or unavailable feedback remain gaps. |
| Report colour gate | Passed for audited baseline | `python .tools/report_colour_audit.py --event 009` returned `total keys with colour: 0`. This is text-path evidence, not a popup screenshot. |
| Runtime visual files | Implemented, raw assets reviewed | One report DDS and fifteen achievement DDSs decode at their expected sizes and resolve from GFX. Raw native-size review found no clear asset defect. Popup layout is not certified. |
| Asset provenance and production handoff | Blocked | Permanent documentation retains runtime paths and an absent historical archive reference, but no verified replacement provenance, prompt lineage, source licensing, or current final-review crosswalk was found in the bounded package. |
| Event documentation and plans | Partial or stale | Overview and old validation matrix are present, but several claims overstate the inspected source. Existing handoffs require reconciliation with the repair tranche. |
| Catalog | Unverified by this auditor | Workbook and CSV files were not edited or used as the authoritative source. The old workbook handoff is stale and the parent catalog owner must provide current workbook facts. |
| MCP event inspect/render/compare | Blocked | Live inspect returned an unavailable-route error; render and compare were not callable. No new event MCP artifact was produced. |
| Live-game proof | Unavailable for successful White Peace | The supplied sheet contains unrelated vanilla reports and news. The named White Peace screenshot is absent. |

## Findings that require parent action

### F1. Invalid force entry silently stops

`common/scripted_effects/chaosx_settings_effects.txt:4246` calls `prepare_white_peace_runtime_context` for event 9 and sets `event_single_fire_allowed = 0` when `global.white_peace_context_ready < 1`.
`009_white_peace_effects.txt:445` maps a safe major relationship before stage II to `constant:white_peace_skip_reason.major_locked`.
The fresh Italy versus Ethiopia world therefore has a plausible intended safety refusal, rather than an eligible base minor pair.
The current source does not connect that refusal to a visible Event 009 explanation at the manual attempt.
The existing `GetWhitePeaceClusterUnavailableReason` text is a cluster availability surface and does not satisfy feedback for an individual forced entry.
Recommended next action: expose the already calculated reason on the force caller and continue choosing globally among valid pairs when any exist.
Do not silently make the fresh major war eligible by bypassing the accepted major-stage safety rule.

### F2. Report options read mutable global dispatch data

Reports `.2` through `.5` call `apply_white_peace_current_context` from their options.
That helper reads `global.white_peace_selected_branch`, `global.white_peace_selected_stage`, and `global.white_peace_selected_pair_cap` at `009_white_peace_effects.txt:1033` through `:1035`.
Those values are assigned by each successful runtime preparation at `:789` through `:791`.
The selected event targets are regular targets carried by the event chain, but the branch values are shared across all chains.
A second preparation can replace those shared values while an earlier human report remains open.
Dynamic cap preparation also resets `global.white_peace_context_ready` and `global.white_peace_stage`, with the latter read by major eligibility.
Recommended next action: resolve the authorized settlement atomically at dispatch or use per-chain immutable pending state with revalidation and explicit invalidation.
An immediate-resolution change must receive a recorded disposition because the accepted source spec currently requests option-applied settlement.

### F3. Successful history is written before settlement succeeds

`chaosx_settings_effects.txt:4553` invokes `on_repeatable_event_fired` after root dispatch.
`chaosx_logic_effects.txt:1216` reduces the repeatable cap, updates event firing state, and records event history without checking `global.white_peace_last_settled_pair_count`.
The dispatcher can return after opening a human report while the actual peace effect still waits in that report's option.
A pair that becomes invalid before acknowledgement can produce zero settlements after the dispatch was already counted and logged.
The current log therefore proves dispatch, not aggregate settlement success.
Recommended next action: preserve one shared pacing incident while tying Event 009 outcome history and any success claim to its final successful result.

### F4. Larger-war settlement safety is unproved

`can_country_be_white_peace_target` rejects subjects, every faction member, protected actors, special actors, civil-war participants, unsafe capitals, and near-capitulation cases.
`can_pair_receive_white_peace` validates the two selected countries only.
It does not require them to have exactly one enemy, require the war to have only those two participants, or check all other participants for protection.
The minor-pair gate also does not veto `has_war_with_major = yes`; the no-major condition is a positive score factor rather than a hard base Tier A gate.
`apply_white_peace_pair` issues native `white_peace` at `009_white_peace_effects.txt:888`.
The installed documentation and offline wiki establish the effect syntax, but do not establish the accepted package's narrow-relationship isolation promise inside a larger war.
Vanilla Finland separately handles faction and overlord relations, which reinforces the need to validate surrounding war state rather than assuming isolation.
This report does not assert an observed whole-war engine result.
Recommended next action: bound the eligible war shape or obtain genuine native evidence for the broader relation before certifying that protected third participants remain untouched.
Any loss of the accepted same-war broad branches must be disclosed with its design disposition.

### F5. Disabled evolution can still change gameplay

`determine_white_peace_stage` at `009_white_peace_effects.txt:167` reads permanent unlock flags and pressure thresholds without `is_current_evolution_enabled`.
`select_white_peace_branch` consumes that stage and enables evolved branches.
The only evolution enable check is inside `record_white_peace_evolution_if_needed` at `:1157`, after a successful settlement.
Disabling evolution therefore stops its record and newly recorded flags, but does not prevent pressure from selecting stronger evolved behavior.
Recommended next action: enforce the selected evolution's enable state where the gameplay stage is chosen and preserve a valid base route when disabled.

### F6. Broad achievements lack distinct-conflict proof

`global.white_peace_broad_conflicts_settled` increments once for each successful broad-branch pair at `009_white_peace_effects.txt:915`.
No unique war identity or distinct-conflict registry is recorded there.
The Circular checks that counter against three or the pair counter against five at `:1107` through `:1119`.
The source therefore does not by itself prove the advertised three separate conflicts.
Timed country memory is set after every pair, so additional pairs sharing either selected country are immediately vetoed.
No source or scenario evidence demonstrates the accepted alternate five-pairs-in-one-war route.
Recommended next action: define and track the actual distinct settlement unit, preserve the accepted challenge, and reconcile the achievement tooltip and docs with that unit.

### F7. Human report and observer behavior are incomplete

`fire_white_peace_report_event` at `009_white_peace_effects.txt:1193` always fires the report on `white_peace_primary`.
There is no preference for a human partner, no human observer summary, no event-specific news event, and no aggregate result-dependent notification.
The baseline has at most one report dispatch, but a human chosen only as partner can receive no Event 009 report, and a USA observer sees nothing for an AI settlement.
News was optional in the accepted package, so its absence is not independently a missing base-spec feature.
It remains an unresolved presentation decision under the parent's current observer-news check.
Recommended next action: explicitly route one appropriate human report or one observer notice for a successful chain and ensure news broadcast cannot replay gameplay effects.

### F8. Prose is plain but weakly tied to actual outcomes

The current report descriptions contain no colour markup and no forbidden literal process nouns from the parent's list.
`localisation/english/009_white_peace_l_english.yml:6` focuses on moving delegates through files, and `:10` focuses on blank spaces and a clerk's stamp.
Those descriptions do not identify the resolved belligerents, actual settlement count, or concrete aftermath.
The multi and broad tooltips promise several wars before the actual loop has established how many remain valid.
Recommended next action: write from the final resolved outcome, using plain country names, troop orders, restored borders, and the actual number of settled conflicts.
The current `.2` description already uses correctly formed regular-target country-name syntax.

### F9. Historical documentation overstates current proof

The old `009_white_peace_validation_matrix.md` explicitly describes static/script-path validation, not in-game validation.
Its claims that every higher stage lowers chance, each broad count proves a separate conflict, and all evolution rows record once are stronger than the source evidence reviewed here.
The final cap floor can flatten stage or repeatable decreases, and reaching a higher stage first does not record all skipped lower-stage rows.
`subagent_handoffs/scripted_system_architect.md` describes load-time `@WHITE_PEACE_BRANCH_*` mirrors that do not exist in the current effects file, which instead loads temporary branch-weight variables.
It also describes excluding faction leaders where the actual trigger excludes all faction membership.
Its parent integration note is historical implementation evidence and cannot certify the current audit gates.
`subagent_handoffs/white_peace_event_catalog_workbook_handoff.md` uses the obsolete `Implemented` catalog status and old detail wording.
Recommended next action: reconcile every affected handoff and the event overview with the final repair, retain historical limits, and obtain fresh authoritative workbook alignment from the catalog owner.

### F10. Asset provenance was not promoted into a verified permanent crosswalk

All required runtime files exist, decode, and have GFX consumers.
The event overview references deleted `docs/assets/009_white_peace/` and deletion commit `87d441ac758d515e1abca34167fcd45b51acf028`.
That object was not available in the current repository when `git ls-tree` was attempted.
The absence of a cleaned temporary workspace is not itself a blocker.
The missing verified durable source mode, original prompt or source-page licensing, selected candidate lineage, current requirement-to-runtime crosswalk, and final review evidence are the gaps.
The runtime report is a restrained tilted period photograph and the achievement states are visually distinct at 64x64.
No new art requirement is inferred from those evidence gaps.
Recommended next action: recover and promote the existing production facts where possible, or explicitly record irrecoverable provenance and the accepted disposition instead of inventing it.

## Accepted-plan disposition

| Document or requirement family | Disposition | Basis and next action |
| --- | --- | --- |
| Four source-design documents named by parent | Accepted source design, implementation partial | Current parent task designation supplies acceptance. The mapped missing or unresolved behavior above remains required until accepted amendment or implementation. |
| Base minor settlement and dynamic cap | Implemented in source, validation blocked | Source helpers and registration exist. Probability and native event validation must use their required routes. |
| Higher stages and same-war broad shapes | Partial | Source stages exist, but toggle enforcement and wider-war isolation are unresolved. No silent narrower fallback is accepted by this audit. |
| Option-applied forced settlement | Implemented, safety repair disposition required | Matches the explicit source spec. Current mutable shared state makes the delayed application unsafe to certify. |
| Existing validation matrix | Stale implementation-evidence record | It establishes its original static review method only. Reconcile claims and append actual new evidence. |
| Existing scripted-system/localisation/workbook handoffs | Historical implementation records | Files and identifiers are useful evidence. Correct stale claims without promoting them as design approval. |
| Optional stage III news | Unresolved proposal | The overview retains it as a future proposal. The current parent observer-news gate must receive an explicit implementation or disposition. |
| Future reusable Peace interface or new mechanical expansion | Unresolved, outside current accepted event | No new dedicated UI or broader mechanics are required by this audit. |
| New probability pass | Parent-owned routed audit, pending | Parent assigned `/root/event009/wp009_probability_audit` as `chaosx_ai_probability_auditor`; no duplicate probability audit was spawned. Same-scenario compare remains mandatory for weighted patches. |

No new improvement addendum was found in the bounded Event 009 plan folder.
The old package's plans and handoffs do not supply a recorded rejection or accepted queue reason for the missing same-war shapes and provenance proof.
Those gaps remain open rather than being hidden as future work.

## Meaningful validation and evidence

`python .tools/report_colour_audit.py --event 009` passed the audited report-title, description, and reachable scripted-localisation colour gate with zero colour-bearing keys.
All four report events have exactly one acknowledgement option in source.
Native decoding verified the report DDS as RGBA `210x176` and all five completed/grey/not-eligible icon triplets as RGBA `64x64`.
No runtime visual file inspected was a Git LFS pointer.
Native-size asset previews were viewed, with no clear raw visual defect found.
These checks do not prove event-window fit, trigger execution, correct successful settlement, or native popup counts.

Read-only audit artifacts are under `subagent_handoffs/evidence_2026_10_05/`:

- `009_audited_source_revisions.json` records SHA-256 identities for the audited event, helper, integration, localisation, achievement, GFX, overview, and old matrix files.
- `009_runtime_asset_metadata.json` records file paths, hashes, decode sizes, modes, and pointer checks for all sixteen runtime visuals.
- `009_report_runtime_preview.png` is a decoded report review artifact.
- `009_achievement_runtime_contact_sheet.png` is a native-size runtime-triplet review sheet.

The supplied `C:\Users\klimp\Videos\chaos_redux_trailer\records\qa\evt009_sheet.jpg` was inspected visually.
It shows numbered pop00 through pop06 with vanilla USA/Japan popup cards, Rhineland/Aussa news, and a map view.
None visibly shows White Peace, so the sheet provides no successful Event 009 report, news, or layout acceptance evidence.

## MCP route blockers

Tool metadata advertised `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
The live `hoi4.reference_context` call returned `MCP tool hoi4_agent_tools/hoi4.reference_context is not available to the model` with `isError = true`.
The live `hoi4.event_inspect` call returned `MCP tool hoi4_agent_tools/hoi4.event_inspect is not available to the model` with `isError = true`.
A later callable check reported `undefined` for all seven methods.
Attempting the required event render produced `TypeError: tools.mcp__hoi4_agent_tools__hoi4_event_render is not a function`.
Event compare was therefore not callable, despite a Git baseline existing.
No event graph render, scope/target projection, state-flow artifact, compare artifact, or scenario-model result was obtained by this auditor.
The source-only findings above are not equivalent MCP or engine evidence.

The 2026-09-05 documentation cleanup record retains an older Event 009 trace with revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, `EVENT_INSPECTED_PARTIAL`, deferred projections, and validation false.
That historical trace is not current successful inspection or rendered comparison evidence.
No native helper-expansion or job route was used without verified health and task negotiation.

## Local reference fallback

MCP reference discovery and reads were unavailable, so pertinent offline wiki and installed sections were read directly.
The following identities are local SHA-256 revisions, not fabricated MCP revision identifiers.

| Source and span | Relevant rule | SHA-256 |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md:8588` through `8602` | COUNTRY white-peace syntax, supported targets, ROOT winner and target loser significance for peace-conference callbacks | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/effects_documentation.md:2943` through `2966` | Country-event dispatch and delay fields | Same revision as above |
| Installed `documentation/effects_documentation.md:6496` through `6512` | Regular and global event-target effects | Same revision as above |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1507` | White-peace target/message syntax | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:145` through `188` | Triggered events, major/show-major broadcast behavior, options, immediate/after, timeout, hidden events | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263` through `327` | Target lifetime, carrying regular targets through a chain, localisation namespaces | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Installed `events/AAT_Finland.txt:2738` through `2778` | Vanilla peace option with explicit faction-leader and overlord handling | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |

These references support syntax and source interpretation.
They do not prove a live whole-war settlement, protected third-party survival, callback timing, AI option resolution, or the exact popup count.

## Remaining blockers and recommended order

1. Implement useful invalid-entry feedback while retaining normal safety vetoes.
2. Resolve the per-chain mutation and dispatch-versus-success problem with recorded authority for any option-to-immediate change.
3. Prove or conservatively bound the eligible war shape and disclose any accepted broad-route reduction.
4. Enforce evolution toggle behavior and correct distinct settlement tracking.
5. Tie the human or observer notification to the final aggregate result and review plain period prose.
6. Consume the routed probability auditor's baseline and mandatory same-scenario compare for weighted changes.
7. Reconcile the overview, old matrix, handoffs, asset provenance crosswalk, and authoritative catalog.
8. Restore the required MCP event inspect/render/compare and probability routes or carry their exact blockers into the parent completion report.

The event is incomplete under the current completion standard.
No gameplay fallback, new mechanics, or balance target was chosen by this auditor.
Skills applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, and the relevant report, achievement, provenance, and completion sections of `chaos-redux-event-assets`.
