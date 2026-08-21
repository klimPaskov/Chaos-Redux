# Event 018 decision-category field GUI independent audit — 2026-08-21

## Disposition

Status: `superseded_after_parent_review`.

Parent disposition: the valid selected-pointer recovery finding was accepted and fixed, the six-value presentation was retained because the Event 018 design explicitly requires the four core metrics plus evolution-gated disturbance and breach values, the ledger detail was retained because the separate six-resource additions are required, and the registry-count observation remains unpatched because the audit did not prove a failing lifecycle path. The final source state and MCP evidence are recorded in `event018_decision_category_gui_final_audit_2026-08-21.md`.

The bounded source audit found no unequivocal attachment, element-name, localisation-key, sprite-reference, state-exclusivity, or click-effect defect in `resources_found_field_management_category`, `resources_found_field_scripted_gui`, or `resources_found_field_window`.

No gameplay, GUI, scripted-localisation, or localisation source was changed by this audit.

The pending arrow update was preserved in `interface/018_resources_found.gfx` and `interface/018_resources_found.gui`: the controls use vanilla `arrow_left_small.dds` and `arrow_right_small.dds` at `(31,261)` and `(79,261)`.

## Scope and reviewed files

The audit was limited to the requested Event 018 surface and the directly called field-selection helpers needed to verify its guards and effects.

- `common/decisions/categories/018_resources_found_categories.txt`
- `common/scripted_guis/018_resources_found_scripted_gui.txt`
- `interface/018_resources_found.gui`
- `interface/018_resources_found.gfx`
- `localisation/english/018_resources_found_system_l_english.yml`
- `common/scripted_localisation/018_resources_found_scripted_localisation.txt`
- Directly called selection and registry helpers in `common/scripted_effects/018_resources_found_ui_effects.txt`, `common/scripted_effects/018_resources_found_effects.txt`, and `common/scripted_triggers/018_resources_found_triggers.txt`.

## Severity-sorted findings

### P1/P2 — visible metric load exceeds the decision-surface contract

The active and closed panels expose six live field values: resource total/added summary, four workboard values (`Developed Yield`, `Excavation Depth`, `Workforce Safety`, and `Foreign Pressure`), `Subsurface Disturbance`, and `Breach Pressure` (`interface/018_resources_found.gui:78-137`, `:148-152`; localisation `localisation/english/018_resources_found_system_l_english.yml:76-86`).

The decision-missions skill allows one primary value, two supporting values, and four values only as a hard ceiling; this panel reaches that ceiling before counting the resource ledger summary and lifecycle status.

Every displayed value has a label, a dynamic band, and a tooltip explaining cause, consequence, or response, so this is a cognitive-load and hierarchy finding rather than a missing-significance defect.

Recommended parent review: keep one primary output value and no more than two supporting values in the always-visible block, and represent disturbance/breach as one crisis indicator or threshold-framed warning; alternatively phase the metrics by workboard page while keeping the primary field state visible.

### P2 — selection recovery path is not proven for an invalid pointer

`resources_found_gui_state_visible` and all active field state icons require `resources_found_selected_field` to be a valid active field (`common/scripted_guis/018_resources_found_scripted_gui.txt:60-66`, `:81-182`).

The `goto` button only enables when the selected pointer is valid or closed history is active (`common/scripted_guis/018_resources_found_scripted_gui.txt:45-53`), while the previous/next buttons require `resources_found_owned_fields^num > 1` (`:37-44`).

If an active field remains but the selected pointer is absent or invalid and the owner registry contains exactly one field, the category can show no active data and no enabled recovery control until another external helper runs `resources_found_validate_country_field_selection`.

This condition was not proved to occur during the bounded static audit because binding and removal helpers normally repair the pointer (`common/scripted_effects/018_resources_found_effects.txt:42-65`, `:78-141`).

Recommended parent review: confirm ownership-transfer, annexation, and field-conversion paths always run pointer validation before the category is redrawn; if not, enable `goto` when an active field exists but the pointer is invalid, or add an explicit local recovery call.

### P2 — two field-count sources can diverge

The arrow enabled guards read the persistent `resources_found_owned_fields` registry, but each arrow effect rebuilds `resources_found_gui_fields` from current `every_owned_state` active fields (`common/scripted_guis/018_resources_found_scripted_gui.txt:37-44`; `common/scripted_effects/018_resources_found_ui_effects.txt:19-47`, `:50-89`).

The registry is removed and rebound during ownership handling (`common/scripted_effects/018_resources_found_effects.txt:991-1030`), and the removal helper validates selection, so no concrete exploit or guaranteed wrong click was established.

This remains an unresolved consistency risk: a stale registry can enable a harmless arrow click when only one current field exists, or disable cycling when the rebuilt current list has more than one field.

Recommended parent review: use one authoritative current-list count for both enabled guards and cycling, or prove that all state ownership and active-field cleanup paths synchronously maintain `resources_found_owned_fields`.

### P2 — tooltip and ledger text are dense

`resources_found.gui.values.tt`, `resources_found.gui.resources.tt`, and `resources_found.gui.closed_resources.tt` contain multiple sentences and several values, exceeding the skill's normal short-tooltip guidance (`localisation/english/018_resources_found_system_l_english.yml:77-86`, `:89-95`).

The text is specific and explains significance, so it is not a correctness gap, but it adds to the six-value scan burden.

Recommended parent review: shorten the tooltip to the immediate consequence and move secondary explanations into decision tooltips or the staged workboard description after the value hierarchy is reduced.

### No P0 or confirmed runtime blocker

No source-level defect was confirmed in GUI attachment, scripted-GUI context, element names, click wiring, localisation coverage, dynamic localisation, sprite paths, state exclusivity, or control bounds.

## Decision-category lifecycle and context

`resources_found_field_management_category` attaches `resources_found_field_scripted_gui` and is visible only while an active owned field exists or a valid exact-seal history record exists, while `resources_found_cave_world_end` suppresses the category (`common/decisions/categories/018_resources_found_categories.txt:15-29`).

The scripted GUI uses `context_type = decision_category` and `window_name = "resources_found_field_window"` (`common/scripted_guis/018_resources_found_scripted_gui.txt:10-13`), matching the offline scripted-GUI guidance and the vanilla `GER_monroe_doctrine_ui` decision-category precedent.

The root window is an independent, non-moveable `470x304` container with no parent window (`interface/018_resources_found.gui:11-15`).

Normal mode shows the active record unless `resources_found_gui_closed_history_view` is set and valid exact-seal history exists; history mode shows only the last closed field.

History is read-only by contract: the closed-state localisation says the record cannot receive another discovery or field project, arrows are disabled in history mode, `goto` only centers the map, and the history control toggles back to active mode (`common/scripted_guis/018_resources_found_scripted_gui.txt:37-59`, `common/scripted_effects/018_resources_found_ui_effects.txt:92-118`, localisation `:72-73`, `:164`).

The active state icon guards are mutually exclusive by status flags, safety threshold, and animation flag: sealing supersedes breach/disturbance/suspension, breach supersedes disturbance, and animated/static pairs split on `resources_found_animations_disabled` (`common/scripted_guis/018_resources_found_scripted_gui.txt:81-182`).

## Cognitive-load notes

There are five visible primary controls: previous, next, show state, animation, and history (`interface/018_resources_found.gui:155-208`).

Five controls remain within the six-action ceiling, although the animation toggle is secondary and may be a candidate for a settings-level treatment if the surface needs more room.

No mission is exposed by this exact scripted GUI; active missions and mission duplication are outside this bounded GUI surface.

The panel exposes six live field values as described above, with clear labels and dynamic bands but no meter, threshold marker, or visual warning frame for the disturbance/breach thresholds.

Text density is high in the four-line value block, the two incident rows, the three-line status block, and the multi-sentence tooltips; the right-side state image supplies visual context but does not replace the numeric scan.

## Mission, cost, and requirement audit

Mission quality is not applicable to this exact GUI: no mission definition or active-mission row is rendered by `resources_found_field_window`.

The five GUI actions are navigation, map centering, history mode, and animation toggling; none consumes a resource or exposes a gameplay-changing spendable cost.

Cost-count audit: zero spendable cost types in the GUI; texticon coverage is therefore not applicable. The decision costs in the category remain outside this exact GUI-only audit.

The `goto` action is guarded by a valid selected state or valid closed history, and the arrows are disabled while history mode is active.

## AI validity and route-lock notes

The scripted GUI is intentionally player-only: root `visible` requires `is_ai = no`, and `ai_enabled = { always = no }` (`common/scripted_guis/018_resources_found_scripted_gui.txt:14-21`, `:201-203`).

All five controls have `element_*_click` effects and matching `element_*_click_enabled` guards, and the wiki specifies that invisible elements cannot be clicked by AI; no AI equivalent is required for these non-gameplay navigation controls.

No AI weight, decision score, MTTH, random-list weight, or probability-bearing modifier exists in this exact scripted GUI, so the mandatory probability-auditor route is not applicable.

No invalid country target, dead target, route lock, or map-center safety issue was proven in the bounded source review; ownership-transfer consistency is the unresolved edge noted above.

## Localisation, tooltip, and asset notes

All `text` and `pdx_tooltip` keys referenced by `interface/018_resources_found.gui` resolve in `localisation/english/018_resources_found_system_l_english.yml`.

All relevant `[GetResourcesFound...]` calls used by the active and closed GUI strings resolve to definitions in `common/scripted_localisation/018_resources_found_scripted_localisation.txt`.

All GUI sprite names resolve in `interface/018_resources_found.gfx`, including static and animated state fallbacks and the pending vanilla arrow sprites (`interface/018_resources_found.gfx:7-25`).

The panel is `470x304`; the vanilla arrows are `24x24` and the three action buttons are `100x29`, so the pending positions remain inside the panel bounds.

## Cleanup and exploit-risk notes

No GUI cost loop, free-resource loop, war-goal loop, core loop, or cooldown bypass is present because the GUI only navigates or toggles presentation state.

The history path is read-only and requires both the closed-state and exact-ledger-reversed flags through `resources_found_gui_has_closed_field_history`.

Pointer and registry cleanup are implemented in directly called helpers, but the ownership-transfer/current-list synchronization edge remains unresolved pending parent review.

## MCP GUI evidence and limitations

Required read-only GUI inspection completed with `hoi4.gui_inspect` for `resources_found_field_window` in scenario `normal`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b759a49b7a3a5a7bb6d1ca49a9996d5873138bc8a461f95ca60cc5fe02d4ab28/ef0f099d4558b935fe3b09cbe6fa452f70214d7cebea8a00865f856f644c8d68/gui-inspect.a5cbb1f47d745f72.json`.

The artifact reported `complete=true`, `windowName=resources_found_field_window`, `nodes=64657`, `elements=25341`, `sprites=28300`, `scriptedGuis=106`, and `inspectedElementCount=34`.

The inspect result was repository-wide and capped by global diagnostic/file truncation, so retained diagnostics such as overlap, unsupported texture, unresolved value, clipping, and scripted-context codes were not safely attributable to Event 018; no Event018-specific error was confirmed.

Required read-only GUI render completed with `hoi4.gui_render` for the same window, requesting normal/hover/selected/disabled/warning/active/completed/empty-list/full-list/minimum-value/maximum-value/long-text/missing-localisation states at `1920x1080` and `2560x1440`.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c79f4c02dd7310bce01f140af5e722d037191382a7ad20910687f4c394f4c2b3/9c4f4b9b245b34c0d1aa55289e092d3a7163704576f2f841a4c4ed434473a288/resources_found_field_window-full.svg`.

The server returned only one full SVG (`1920x1080`) and did not return separate state, click-region, hierarchy, or `2560x1440` artifacts; the SVG response was truncated by the MCP transport at 32768 bytes.

These tool limitations prevent a complete visual click-region and supported-resolution comparison, but they do not invalidate the source cross-reference findings above.

## Validation and skipped validation

Completed task-specific checks: source cross-reference of category attachment, scripted-GUI effect/trigger names, GUI element names, localisation keys, scripted-localisation calls, GFX sprite paths, static/animated state guard exclusivity, control bounds, and direct helper guard/effect flow.

Vanilla precedent checked: decision-category scripted GUI attachment in `common/decisions/categories/GER_decision_categories.txt`, `GER_monroe_doctrine_ui` in `common/scripted_guis/GER_monroe_doctrine_scripted_gui.txt`, and vanilla arrow paths in `interface/options.gfx`.

HOI4 was not launched, as required by repository policy; live gameplay, live save-state transitions, and final player-side visual validation remain skipped.

No `hoi4.gui_rewrite` was used because no unequivocal in-scope defect was found and the user explicitly required reporting before any patch.

The probability-auditor route was skipped because this bounded GUI has no probability-bearing logic.

## Recommended parent actions and remaining issues

1. Review the six-value presentation against the decision-missions cognitive-load ceiling and reduce or stage the always-visible metric set.
2. Verify invalid selected-pointer recovery after ownership transfer, annexation, active-field closure, and conversion paths.
3. Align arrow enabled guards with the same current active-field list used by `resources_found_gui_rebuild_field_list`, or document the invariant that keeps the registry exact.
4. Shorten the dense ledger/value tooltips after the metric hierarchy is settled.
5. Repeat MCP visual inspection/rendering when the server can return Event018-specific click regions, state views, and both requested resolutions.

Remaining uncertainty is limited to the P2 presentation/selection-consistency findings and MCP visual artifact limitations; no confirmed source defect or exploit was found.

## Changes and handoff

Changed files: only this handoff document was created by this audit.

Gameplay, GUI, GFX, scripted-localisation, and localisation files were not edited; the other agents' existing worktree changes were preserved.

No commit was created because the shared worktree contains unrelated pending changes and the parent agent owns the final integration/commit decision.

No simplification or fallback was introduced by this audit.
