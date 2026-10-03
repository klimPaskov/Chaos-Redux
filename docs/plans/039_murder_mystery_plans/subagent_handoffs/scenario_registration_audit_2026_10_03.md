# Event 039 Assassin Network registration audit

Audit date: 2026-10-03.
Mode: read-only source audit with one authorized documentation handoff.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Bounded verdict

The SCN-019 registration is implemented in source and the reviewed registry additions preserve the existing identities and shared controls.
No blocking defect was found in the ID allocation, registry insertion, getter linkage, or dispatcher addition itself.
This is not a completed scenario acceptance claim.
Mandatory MCP visual, comparison, helper/lifecycle, probability, and observed launch evidence remain incomplete.
Existing launch-gate and failure-cleanup defects below also prevent treating the newly reachable payload as fully accepted.
Full Event 039 and the Part 18 matrix remain incomplete.

Only this handoff was authored by this auditor.
No gameplay, localisation, GUI, workbook, export, index, or staged content was changed, and no commit or game launch was performed.

## Completion by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Stable identity | Finished in source, catalog handoff confirmed | Shared constants line 33 use `assassin_network = 19`; Event 039 constants lines 841-843 use runtime/catalog 19; public row label is `#019` at `localisation\english\039_murder_mystery_l_english.yml:16`. |
| Existing identities | Preserved in reviewed repair | Baseline/current constants comparison retains Fallout 14 and Fracture Cascade 18, with no ID 17 entry; the four shared before-copy diffs add Assassin Network without modifying the prior scenario branches. |
| Registry and four sort views | Finished in source | `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt:211`, `:230`, `:501`, `:515`, and `:781` add the paired ID/name-sort values. Parent independently reports 17 unique rows and four paired 17-row views. That mechanical check is source evidence. |
| Shared getters and public keys | Finished registration linkage, limited text review | Selected name, row name, row ID, description, single type, four warnings, and status resolve through `common\scripted_localisation\chaosx_scripted_localisation_scenarios.txt:128`, `:215`, `:302`, `:690`, `:1147`, `:1583`, and `:1904`. The inspected keys at `localisation\english\039_murder_mystery_l_english.yml:9-20` exist. This does not accept unrelated mixed mission localisation. |
| Shared eligibility and dispatch | Finished bridge, payload acceptance partial | `common\scripted_triggers\chaosx_triggerable_scenarios_triggers.txt:285` delegates to the Event 039 gate; `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt:1299-1303` dispatches to the existing wrapper. The delegated gate has the limitations below. |
| Shared GUI selection, confirmation, cancellation | Source flow reviewed, visual gate blocked/open | Existing entry click reads the selected array row at `common\scripted_guis\chaosx_scripted_gui_settings.txt:2636-2637`; the trigger opens confirmation at `:2704`; Confirm dispatches at `:2810-2812`, while Cancel only closes confirmation at `:2815-2816`. Before-copy/current shared scripted-GUI comparison is unchanged. |
| Four intensity selectors | Source routing finished, full setup partial | Constants use Low/Medium/High/Maximum = 1/2/3/4. The existing four stop clicks call the shared setters at `common\scripted_guis\chaosx_scripted_gui_settings.txt:2664-2677`. The wrapper freezes intensity at confirmation, and the root clears it after execution. Full cells, split, derivatives, and rollback are not validated. |
| Catalog | Reservation finished by specialist, final alignment pending parent reconciliation | `scenario_catalog_019.md` records A14 reservation before code and exporter success. `scenario_catalog_019_intensity.md` records E14 alignment and exports. The parent subsequently reports another worker aligning D14/E14. This audit did not independently read the workbook or certify the final concurrent workbook bytes. |
| Documentation | Registration documentation present, whole event documentation partial | Shared scenario doc has the SCN-019 section at `docs\systems\event_system\triggerable_scenarios.md:270-289`; repair evidence explicitly limits completion. `docs\events\039_murder_mystery.md` remains focused on incomplete mission work and does not establish full Part 11 coverage. |
| Assets and dedicated event GUI | Outside this repair | No visual production, custom 3D package, audio, portraits, or dedicated event-owned window was added. Shared settings/scenario UI reuse does not require a `chaosx_event_ui_worker` handoff. No wider Event 039 asset acceptance was performed. |

## Confirmation and intensity source findings

`open_triggerable_scenario_confirmation` and `close_triggerable_scenario_confirmation` at `common\scripted_effects\chaosx_triggerable_scenarios_effects.txt:830-837` only initialize settings and toggle the popup flag.
The initializer preserves already stored selection and intensity, rather than overwriting them.
`trigger_selected_chaosx_scenario` at lines 1105-1107 reads the current selected scenario into its launch ID at confirmation time.
The Event 039 wrapper rechecks eligibility and copies the current intensity into `global.murder_mystery_scenario_launch_intensity` at `common\scripted_effects\039_murder_mystery_integration_effects.txt:59-79`.
There is one scenario type, so no additional type variable is needed for this repair.
An Event 039 host preference control is not present in this shared flow, which remains a separate Part 11 consideration.

| Intensity | Source setup values: Case / Reach / Cohesion / cell target | Activated stage | Additional source path |
| --- | --- | --- | --- |
| Low, 1 | 20 / 15 / 35 / 3 | I | Unconditional `else` at integration-effects lines 163-166 calls the stage-I setup. |
| Medium, 2 | 45 / 35 / 50 / 6 | II | First threshold branch at lines 154-162. |
| High, 3 | 70 / 60 / 65 / 7 | III | High branch at lines 167-175, then split/country commit calls at lines 206-212. |
| Maximum, 4 | 85 / 80 / 80 / 10 | IV | Maximum branch at lines 176-184, then derivative attempt target 3 at lines 213-235 if the Assassin State exists. |

Values are defined in `common\script_constants\039_murder_mystery_constants.txt:846-865`.
Higher intensities pass through preceding threshold branches, with the final stage/value assignments overriding the earlier values.
These are source branches and target counts, not proof of successful cell creation, war, derivatives, faction setup, or their history records.
The corrected four warning strings describe these stage families and no longer use a generic four-level strength claim.
The root applies scenario setup only after `murder_mystery_opening_transaction_committed` at `events\039_murder_mystery.txt:38-44`, then clears the launch flag and cached intensity at lines 46-47.
The cached-intensity cleanup addition is bounded and does not alter an AI weight.

## Relevant existing payload defects and validation gaps

These are findings about the existing adapter exposed by registration, not evidence that the repair introduced them.
The repair's own mixed integration-effects scope is only the Low fallback `else` hunk.

1. **Launch can be blocked by disabling world-end mechanics without any terminal state being active.** `murder_mystery_triggerable_scenario_can_launch` at `common\scripted_triggers\039_murder_mystery_integration_triggers.txt:201-206` calls `murder_mystery_event_is_available`, whose line 53 rejects `world_end_disabled`. This flag is the optional world-end mechanic setting, set by `toggle_world_end` at `common\scripted_effects\chaosx_settings_effects.txt:3458-3477`, rather than an active terminal condition. Part 11 lines 13-23 requires blocking incompatible terminal states, not this unrelated setting. The inherited host gate also applies `individual_crisis_load_is_below_cap` at integration-triggers line 29, so manual launch still inherits a normal-event load restriction. Parent should separate scenario safety from ordinary-event eligibility in a later owned change.

2. **Delayed-root rejection can strand the launch lock.** The wrapper sets the global launch flag and cached intensity before queuing `chaosx.nr39.1 days = 1` at integration-effects lines 66-72. The root's trigger at `events\039_murder_mystery.txt:21-23` rechecks the host. If that trigger is false at delivery, its immediate block cannot execute the cleanup at lines 46-47. The only other reviewed cleanup of those two launch fields is the wrapper's immediate no-target branch at integration-effects lines 75-79. Repository searches found no delayed failure-recovery owner. The offline Event modding Triggering section, lines 117-150, explicitly says delayed events still require their trigger at delivery. This is a source-supported failure path, not an observed runtime incident.

3. **High/Maximum capacity and character/territory preflight are not established by the launch gate.** The gate checks event availability, duplicate/setup flags, and any eligible host. Its host predicate checks ordinary major/player status, state count, and the presence of a country leader at integration-triggers lines 12-34. It does not vary by intensity or verify the split/remnant plan, derivative capacity, or protected-character disposition required by Part 11. `murder_mystery_prepare_opening_package` sets `murder_mystery_assassin_carrier_reserved` at integration-effects line 348 without a demonstrated capacity reservation. The later split calls do not make the launch gate an accepted preflight. Keep the High/Maximum transaction acceptance cases open.

4. **Setup success and cleanup remain partial.** The root sets `murder_mystery_scenario_launched` before the intensity payload at lines 43-44. The payload attempts cells, split, and derivatives, but does not return one overall success receipt or unwind the complete opening when a later transaction fails. The cell and derivative loops assign their progress counter to the target when no candidate exists at integration-effects lines 202-204 and 232-234, so those counters cannot independently prove actual creation counts. The prefire host target and scenario target counters are not cleared by the root, and the inspected shared runtime cleanup at `common\scripted_effects\039_murder_mystery_runtime_effects.txt:1996-2077` does not clear the prefire host. Retained shared UI selections may be intentional, but Part 11 cleanup and failure acceptance need explicit disposition.

5. **Status text conflates resolved and active lifecycles.** The newly linked status branch at `common\scripted_localisation\chaosx_scripted_localisation_scenarios.txt:1920-1923` includes `murder_mystery_runtime_resolved`, then displays the key whose value is “Assassin Network is already active.” at `localisation\english\039_murder_mystery_l_english.yml:19`. Relaunch policy after complete resolution remains unaccepted by this audit, and resolved-state wording should not claim an active network.

The broader Part 11 cell-stage mix, safe succession, split and derivative setup, scenario-specific history/intensity receipt, terminal gate execution, and all rollback paths remain unproved.
No whole-country, focus, achievement, animation, model, portrait, or super-event audit is inferred from this bounded review.

## MCP calls, evidence, and limits

The live tool inventory exposed Event inspect/render/compare, GUI inspect/render, probability routes, reference context/search/read, and source lookup.
That exposure does not prove route health.
The live source-lookup schema lacked `view` and `keyPath`, and `hoi4.script_validate` was not exposed.
No helper expansion, job control, native MCP task, GUI rewrite, or engine launch was attempted.

| Request | Result available at handoff cutoff |
| --- | --- |
| Auditor `hoi4.event_inspect`, mode `trace`, selector `{ kind: "event", eventId: "chaosx.nr39.1" }`, depth 1, nodes 12, edges 16, helpers false | Failed with `timed out awaiting tools/call after 600s`. Two earlier malformed selector probes returned input-validation errors and provide no inspection evidence. |
| Auditor `hoi4.event_render`, same root selector, view `state`, depth 1, nodes 12, helpers false, HTML false | Collector cell 24 completed with `timed out awaiting tools/call after 600s`. No render artifact or visual acceptance evidence was returned. |
| Auditor `hoi4.event_compare`, root selector, chain/render bound 12, render false, four immutable shared before-copy source overlays | Collector cell 29 completed with `timed out awaiting tools/call after 600s`. Intended direction was current-to-before using saved pre-registration registry overlays. No comparison artifact was returned. Those copies do not supply an immutable pre-edit Event 039 root or integration-effects source, so those two hunks were outside the requested comparison coverage. |
| Auditor `hoi4.gui_inspect`, window `chaosx_scenario_confirm_window`, generated scenarios disabled | Collector cell 23 completed with `timed out awaiting tools/call after 600s`. Its exploratory fixture incorrectly used intensity 0, while Low is 1, so it is excluded from acceptance evidence independently of the route timeout. |
| Auditor `hoi4.gui_render`, window `chaosx_scenario_confirm_window`, scenario `e39-scn019-confirm-low-valid`, selected 19, intensity 1, popup flag true, 1920×1080, scale 1, normal state | Submitted through the confirmed live schema, collector cell 31. Exact current name/type/intensity text was supplied as declared display values. No completed render/artifact was available at cutoff. These declarations would not prove runtime eligibility or getter execution. |
| Parent shared GUI inspection and narrower `triggerable_scenario_entry_generic` inspection | Parent reports both timed out after 600s. No successful state, hierarchy, click-region, resolution, or matched baseline/current visual evidence is available here. |

The parent separately reports narrow Event lint as `EVENT_INSPECTED_PARTIAL`, revision `8cff6caa71c9f1de7f7a76b61c662306289fbaa4573c5f106a8e4d0d6058bdd1`, graph `5a95d052792aee07688ded4f5f52d553f8604fec3d4e1fec9297cdf4524f6af6`.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c97e1b33d3e360feaea77e0f573c763562c49498176ccd866e81d54921571fee/2af09190d15d8c6c2f926255342b788faa2fc5fdd384a84a5f9d3caba8728ac6/event-lint-8cff6caa71c9.json`, reported size 2,039,845 bytes.
The parent reports reading all 2,039,845 bytes through 24K resource chunks.
Its focused report has zero issues, `complete = false`, and an unresolved inventory of 8,958 entries with 2,000 retained and truncation.
Nine retained Event 039 unresolved helper references have exact definitions confirmed by the parent with `rg`, including integration lines 573, 1168, 1343, 1373, 1398, and 1632, CXT line 12, and shared audio line 4504.
These are focused-analysis coverage limits, not evidence of missing source files or authorization to repair those helpers.
The parent reports artifact Event 039 source SHA-256 `5b582c80df580c85dba01077cccd734154f6cf2329deaec2c454501d79edc367` matches the working tree.
The reported 2,193 workspace diagnostics and zero blocking diagnostics do not establish full lifecycle acceptance.
This auditor relies on the parent's complete artifact read for those results and has not independently read that artifact.
Helpers and lifecycle remain deferred.
The parent's narrow child render remains pending in parent cell 38 and supplies no completed visual evidence at this cutoff.

The parent's completed source lookup of `murder_mystery_triggerable_scenario_launch` covers lines 59-81 with revision `bcb661e2c2c5f10ef154908d7b9310e2b6b590cde713430cac3aa4a4c514e430`, `complete = true`, and no overrides.
This verifies the retrieved source definition, not execution.
The parent's array reference-read result was pending when supplied and is not counted as completed here.

### Probability specialist

The read-only probability pass was routed to `chaosx_ai_probability_auditor`, agent `01a1010f-4e0f-71e3-835f-e2a4bddca5f7`.
It returned unresolved inline findings and authored no files.
It started with `hoi4.probability_inspect` on shared scenario effects, then the Event 039 integration-effects source object `{ path: "common/scripted_effects/039_murder_mystery_integration_effects.txt" }`.
Both inspections remained pending for about 124 seconds and were manually cancelled by the specialist.
Neither returned a status, candidate pool, diagnostics, artifact URI, source revision, analysis ID, or scenario hash.
No evaluate, sweep, simulation, sequence, render, or probability comparison result exists.
No source-only calculation or invented host pool substitutes for that missing evidence.
The bounded repair does not change host weights, cell-count tuning, or an AI option score, so a numerical weight-change comparison is not claimed or required for these registration hunks.
The existing host-selection probability behavior remains unaudited.

### References actually read

The auditor completed `hoi4.reference_search` for delayed event triggering and `hoi4.reference_read` of offline Event modding, Triggering, lines 117-150, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
The read ID is `8bbe2e58d576588f859f7562369979e50455130015df94bceca9edb2bb7bf627`, with no next line.
The GUI context bundle completed, but included `omittedSources = [Localisation, Scopes]` and only identified wiki top-level headings.
It is not full documentation coverage.
Installed `common\scripted_guis\_documentation.md` lines 1-102 were directly read for player context, window attachment, click predicates, and dynamic lists, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838` supplied by that completed context result.
The bounded registration evidence file's other offline/vanilla reference citations remain parent evidence rather than independently completed auditor MCP reads.

## Accepted-plan disposition and parent next actions

The user's explicit 2026-10-03 direction supports the next verified free ID and shared registration repair.
The provisional Part 11 SCN-014 suggestion is superseded for allocation by SCN-019, with reservation documented in `subagent_handoffs\scenario_catalog_019.md`.
The bounded registry plan is implemented in source with validation limits, not promoted into a full scenario completion claim.
Part 11 and the remaining Event 039 payload requirements remain accepted work outside this repair, with implementation and validation gaps retained.
This audit does not resolve them by relabeling them as future suggestions.

Recommended next actions are to reconcile the final D14/E14 worker handoff and refreshed exports, extract target-specific findings from the parent's lint artifact, and retain the open render/comparison/GUI/probability gates in the parent report.
The parent should own a separate repair of the manual gate, delayed failure recovery, and intensity-dependent preflight before certifying all launch states.
Do not include unfinished capture/mission hunks in the bounded registration commit or mark mixed Event 039 localisation as fully audited.
No new fallback or simplified design is accepted by this registration repair.

Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and `chaos-redux-scripted-gui`.
No skills were created or changed.

## Post-registration follow-on: manual setting gate

Read-only follow-on review on 2026-10-03 after registration commit `2f8a05eff`.
The parent owns this separate source change.
Comparison of the working-tree integration-trigger file against that commit shows exactly one changed block, `murder_mystery_triggerable_scenario_can_launch`.
Reviewed file SHA-256: `16f2972dd0085000611bbfc5530458f6c7ae80bae6bd80b4409860765861c2b7`.

At `common\scripted_triggers\039_murder_mystery_integration_triggers.txt:203-205`, the former `murder_mystery_event_is_available = yes` alias is replaced by exactly three explicit guards: `NOT murder_mystery_runtime_active`, `NOT murder_mystery_runtime_resolved`, and `NOT world_end`, each expressed through `has_global_flag`.
The existing `NOT murder_mystery_scenario_launch_in_progress`, `NOT murder_mystery_scenario_launched`, and `murder_mystery_has_any_eligible_host = yes` remain unchanged at lines 206-208.
The manual gate no longer inherits `world_end_disabled` from the automatic-availability alias.

The terminal setting predicate is unchanged: `murder_mystery_world_branch_is_enabled` at lines 148-151 still rejects both `murder_mystery_world_branch_disabled` and `world_end_disabled`.
`murder_mystery_terminal_option_is_available` at lines 196-199 still requires that predicate together with `murder_mystery_world_end_activation_is_valid`.
Automatic availability at lines 49-54 and the host predicate at lines 12-34, including `individual_crisis_load_is_below_cap`, are unchanged against the registration commit.
This patch does not touch the separate host-weight implementation.

Disposition: the world-end-setting portion of finding 1 is resolved in source by this separate bounded change.
The inherited host-load restriction, probability coverage, delayed-root cleanup, intensity preflight, payload outcomes, and full Part 11/Part 18 acceptance remain open.
The parent's manual-exclusion and terminal-setting checks are reported as passing parent evidence, with no observed launch result inferred.
No new MCP query was submitted for this follow-on review.
The parent's gate source lookup and narrow root render/compare retries remain pending as supplied context.
Only this handoff appendix was edited by the auditor, with no gameplay edit, staging, commit, or launch.
