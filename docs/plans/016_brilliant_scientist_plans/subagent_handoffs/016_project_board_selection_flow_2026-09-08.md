# Event 016 project-board selection-flow audit

Date: 2026-09-08

Status: read-only audit complete; source result is actionable, GUI evidence is blocked by tool timeouts, and named probability-auditor evidence remains parent-pending.

## Scope and evidence basis

This audit covers the project-board decision category, its project-stage effects and triggers, and the attached Directorate GUI.

No gameplay, decision, scripted GUI, interface, localisation, AI, or balance source was edited.

The current `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui`, and `chaos-redux-subagents` skills were read before this audit.

The required offline wiki pages were consulted, including Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.

Vanilla decision and scripted-GUI documentation was consulted, including `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/scripted_gui_documentation.md` where present and the installed `common/scripted_guis/_documentation.md` reference.

The accepted Event 016 contract, current source-of-truth map, and `016_no_dlc_closure_review_2026-09-06.md` were used as design and prior-evidence references.

## Executive result

There is no live writer anywhere in `common`, `events`, `interface`, or `localisation` for `brilliant_scientist_directorate_selected_project_family`, `brilliant_scientist_directorate_selected_project_stage`, or `brilliant_scientist_directorate_project_selection_ready`.

The six generic project-board controls that depend on those values are therefore dead in the current runtime: approve, suspend, resume, cancel, independent replication, and publish.

The actual player family-choice surface is the direct per-family decision row itself, which writes temporary family and requested-stage inputs and starts the existing stage receipt.

Do not revive the dead selector by adding an unaccepted second ledger or a new scripted GUI.

## Severity-sorted issues

### P1: six generic project controls are permanently unreachable

The only root definitions are `brilliant_scientist_approve_selected_project` at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:70`, `brilliant_scientist_suspend_selected_project` at `:161`, `brilliant_scientist_resume_selected_project` at `:198`, `brilliant_scientist_cancel_selected_project` at `:237`, `brilliant_scientist_commission_independent_replication` at `:279`, and `brilliant_scientist_publish_verified_methods` at `:400`.

Every one requires `brilliant_scientist_directorate_project_selection_ready` and a selected family or stage, while no source writer sets those values.

Their AI weights and gameplay effects are inert because the decisions never become visible.

The safest bounded disposition is to keep them out of the visible action design until an accepted selector contract exists, rather than making them appear to work by guessing a writer.

### P1: direct family rows exceed the accepted visible-action budget when a stage opens for every family

The no-DLC fallback block begins at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:5025`.

At a mature Theory state without Gotterdammerung, the fifteen `brilliant_scientist_fallback_*_prototype` rows can all be visible at once.

The native route has the same family breadth through the fifteen `brilliant_scientist_integrate_*_prototype` rows at `:488-972` and `:3508-3680`.

This violates the decision skill's normal 3–5 primary-action target and hard six-action ceiling if the decision list is treated as one visible surface.

No accepted source-level selector currently reduces this list.

### P2: the read-only Directorate GUI cannot repair the project list

`common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt:8-70` declares a `decision_category` attachment whose only effects open and close the compact panel.

`interface/016_brilliant_scientist_directorate.gui:8-180` contains identity, portrait, four meters, role text, and footer text, but no project list, selector, action button, or family picker.

The category registration at `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt:10-21` attaches that read-only window to the merged ordinary decision category.

This audit did not edit the attachment; the parent may simplify the ordinary decision-category action surface within the accepted existing UI boundary.

### P2: the GUI reports a dead selected state alongside a live active state

`common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt:549-565` correctly reads `brilliant_scientist_active_project_family` for the active-stage text, but its status branch at `:564` reads the never-written `brilliant_scientist_directorate_project_selection_ready` flag.

The selected status branch is therefore unreachable, while active, incident, damaged, and suspended branches can be live.

This is a semantic display gap, not a reason to add a selector.

## Exact writer and consumer map

### Dead selector symbols

A repo-wide literal scan over `common`, `events`, `interface`, and `localisation` returned 46 hits in exactly three files.

`common/decisions/016_brilliant_scientist_directorate_project_board.txt` contains 39 reads or downstream lock/command assignments, but no assignment to either selected variable or the selection-ready flag.

`common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:177-210` reads selected stage and family for resume and Singularity dismantle checks.

`common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt:564` reads the selection-ready flag for the GUI status string.

There are no `set_variable` assignments whose destination is `brilliant_scientist_directorate_selected_project_family` or `brilliant_scientist_directorate_selected_project_stage`, and no `set_country_flag` assignment for `brilliant_scientist_directorate_project_selection_ready` outside the inert control logic.

### Live active-project receipt

`common/scripted_effects/016_brilliant_scientist_project_effects.txt:10-65` defines `brilliant_scientist_begin_project_stage`.

The effect validates the existing board, family input, stage input, cost, and previous ledger stage, then writes `brilliant_scientist_active_project_family`, `brilliant_scientist_active_project_stage`, and `brilliant_scientist_active_project_capacity_delta` at `:30-46`.

`common/scripted_effects/016_brilliant_scientist_project_effects.txt:147-160` writes the same family and prototype stage receipt for native Prototype integration.

`common/scripted_effects/016_brilliant_scientist_project_effects.txt:71-77` clears the active receipt on finalization.

`common/scripted_effects/016_brilliant_scientist_project_effects.txt:112-143` validates matching callbacks, advances the persistent ledger, applies stage output, and finalizes the active receipt.

### Live persistent family ledger

`common/scripted_effects/016_brilliant_scientist_effects.txt:999-1025` initializes `brilliant_scientist_project_stage_entries` and `brilliant_scientist_independent_project_stage_entries` as aligned fifteen-family arrays with indexes 0–14.

`common/scripted_effects/016_brilliant_scientist_effects.txt:1077-1080` maps one-based family IDs to the zero-based array index.

`common/scripted_effects/016_brilliant_scientist_effects.txt:1122-1144` writes persistent stage progress through `brilliant_scientist_advance_project_to_requested_stage`.

`common/scripted_effects/016_brilliant_scientist_effects.txt:1210-1222` publishes a family through the existing ledger and replication path, while `:1236-1251` dismantles a family and clears its ledger stage.

### Live family-choice rows

The fifteen Theory, Deployment, and Weaponization rows are ordinary decisions beginning at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:979`.

Each direct row sets `brilliant_scientist_project_family` and `brilliant_scientist_requested_project_stage` and calls the existing stage effect, as shown by `brilliant_scientist_advance_computation_theory` at `:979-1033`.

The native Prototype rows select a family by the row itself and call `brilliant_scientist_begin_native_prototype_integration`.

The no-DLC Prototype rows select a family by the row itself and call `brilliant_scientist_begin_project_stage`, as shown by `brilliant_scientist_fallback_computation_prototype` at `:5028-5075` and the matching Singularity row at `:5714-5760`.

The fifteen current family IDs, in source order, are `computation`, `electronics`, `materials`, `rocketry`, `high_energy`, `biomedical`, `teleportation`, `cloning`, `robotics`, `paleogenetics`, `xenobiological_synthesis`, `biological_weapons`, `alien_arms`, `temporal`, and `singularity`.

The six Singularity component rows begin at `brilliant_scientist_fallback_singularity_command_core` at `:5765` and are a separate component sequence, not family selectors.

### Separate live priority policy

`common/decisions/016_brilliant_scientist_directorate_institutions.txt:320-474` contains the three live policy decisions `brilliant_scientist_prioritize_fundamental_inquiry`, `brilliant_scientist_prioritize_prototype_delivery`, and `brilliant_scientist_prioritize_distributed_replication`.

These decisions write mutually exclusive priority flags and modifiers, not a project family or stage selection.

They must not be repurposed as a hidden family selector because doing so would make access to some of the fifteen families depend on an extra paid, timed approval step.

## Recommended smallest working flow

Treat each direct family-stage row as the family choice and action in one click, using the existing persistent ledger and active receipt.

Do not add writers for the dead selected-family variables, do not add an approval step, and do not route project selection through the separate three-way priority policy unless the parent explicitly accepts that design.

Keep every family reachable through its existing direct row and use the native decision-category list's existing scrolling or viewport behavior as the only presentation mechanism available in the current UI.

Order the family rows deterministically in the existing source order and expose only the next valid stage for each family at a time; do not expose duplicate stale stage rows.

If the production decision list still presents more than six primary rows simultaneously, the parent needs an explicit accepted choice between relaxing the hard-six visual constraint and authorizing a bounded existing-category phasing rule.

The current source does not contain enough accepted selector or category infrastructure to promise both a hard-six simultaneous list and fifteen simultaneously direct-visible families without adding a new UI or an extra gate.

## Category lifecycle notes

The category remains visible for the current host or sovereign state through `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt:12-18`, including when empty.

The board lifecycle is direct stage progression: a row starts a timed receipt, the active receipt occupies capacity, a matching callback advances the family ledger, and cancellation or terminal cleanup finalizes the exact receipt.

The dead generic controls are not part of the live lifecycle because no selection-ready state can be reached.

The separate priority lifecycle is a paid timed policy change with its own cooldown and should remain independent of project family access.

## Cognitive-load notes

Visible actions: fifteen family choices can appear when a new Prototype tier opens, exceeding the normal 3–5 target and hard six-action ceiling if the full category is treated as one visible list.

Active missions: the board has family incident missions, but they are reactive incident obligations and not project selectors; no selection mission activates a family choice.

Player-facing values: the active project family and stage have a live receipt and GUI text, while the selected status is dead and can never explain a current choice.

Text density: direct rows have family-specific names, stage costs, and custom requirement/effect text; the generic action tooltip still promises a “valid Directorate project selection” that the player cannot make.

Value significance: the persistent fifteen-family stage array is meaningful and consumed by progress, capacity, technology, and output logic; it should remain the source of truth instead of duplicating it in selected-family variables.

## Mission quality notes

The incident missions are owned by individual project families, live in the same board category, and use `brilliant_scientist_*_incident_active` flags for activation.

They have explicit timeout, cancellation, timeout-effect, and AI paths, as shown by `brilliant_scientist_computation_incident_mission` at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:4005-4038`.

They are not duplicate selectors and should not be used to solve board density.

The saved no-DLC closure review records 21 visible terminal gates and 21 fallback decision cost/PP surfaces; this audit found no new mission duplication risk.

## Cost and requirement clarity

The six dead generic controls stay within the four-cost ceiling when considered independently: approval, resume, cancel, and publication use Political Power; suspension is free; replication combines Political Power, Support Equipment, motorized equipment, and fuel.

The no-DLC fallback rows use their existing family-specific custom-cost trigger and texticon-backed cost surface; the prior no-DLC closure review records four displayed burdens per fallback row and no hidden fifth spendable type.

The main clarity problem is not cost count but unreachable requirement text: `brilliant_scientist_project_board_action_requirements_tt` tells the player a selection must be ready while no action can create one.

## AI validity and route-lock notes

All six generic AI weights are unreachable because their visible triggers depend on the unwritten selection-ready state.

The direct family rows have family/stage-specific AI weights and remain the live AI action surface.

This subagent did not obtain the required named `chaosx_ai_probability_auditor` evidence; the parent-owned `/root/mengele_conventional_probability` audit is active and remains pending.

The prior no-DLC probability attempt used the direct HOI4 route and returned partial or empty surfaces, not a named-auditor acceptance result; this audit does not promote that evidence to completion.

No AI weight or route lock was changed.

## Localisation and tooltip gaps

`brilliant_scientist_project_board_action_requirements_tt` and `brilliant_scientist_project_board_action_cancel_tt` describe a selection-driven flow that has no entry point.

`GetBrilliantScientistDirectorateProjectBoardStatus` has a dead selected branch at `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt:564`.

Direct family-stage decisions have existing family-specific requirement and effect localisations and should remain the visible explanation surface.

## Cleanup and exploit-risk notes

The live active receipt has explicit matching-family/stage callback guards and exact cleanup in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:71-77` and `:112-143`.

The dead generic controls cannot currently create a gameplay exploit because they cannot become visible.

If they are ever connected, their lock variables and command receipts must be reconciled with the active family/stage receipt and cleared on visibility loss, cancellation, and terminal cleanup.

No gameplay patch was made and no new exploit was introduced by this audit.

## GUI and weighted-logic MCP evidence

Read-only `hoi4.gui_inspect` was attempted for `kruger_directorate_container` with scenario `event016_directorate_actual_normal_expanded`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and bounded wait of 180 seconds; it timed out awaiting `hoi4_agent_tools/hoi4.gui_inspect`.

Read-only `hoi4.gui_render` was attempted for the same window, scenario, workspace, 1920x1080 at UI scale 1, and the normal/hover/selected/locked/disabled/warning/active/completed states with bounded wait of 180 seconds; it timed out awaiting `hoi4_agent_tools/hoi4.gui_render`.

No fresh production render or current click-region artifact is claimed here.

This subagent did not invoke the named `chaosx_ai_probability_auditor` route, so weighted evidence is not obtained here and parent audit remains pending.

The absence of a callable child route in this subagent context is not evidence that the repository-wide named auditor is unavailable.

## Validation and handoff

Meaningful read-only checks were the repo-wide selector-symbol scan, direct root-ID extraction for the six generic controls and fifteen fallback rows, source inspection of the live stage/active-receipt effects and project triggers, category/GUI source inspection, and review of the saved no-DLC closure handoff.

The game was not launched, and no gameplay or live-save validation was attempted.

Changed files: this handoff only.

Remaining issues: parent acceptance is still needed for the existing decision-category viewport/phasing interpretation of the hard-six visual budget; GUI MCP evidence is blocked by tool timeouts; named probability-auditor evidence was not obtained in this subagent turn and remains parent-pending; the six generic selector-driven controls remain inert until an accepted selector design exists.
