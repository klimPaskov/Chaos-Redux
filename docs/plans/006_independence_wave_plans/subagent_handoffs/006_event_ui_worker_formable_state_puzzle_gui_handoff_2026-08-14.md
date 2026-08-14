# Event 006 state-puzzle GUI worker handoff

## Scope and verdict

This handoff covers only the Event 006 grouped scripted GUI window `chaosx_independence_wave_formable_state_puzzle_window`.

The accepted Event 006 formable specification names this surface as the grouped consumer for fourteen runtime-authored families, gives it the grouped GUI id `independence_wave_formable_state_puzzle_scripted_gui`, and assigns it to the `independence_wave_formables` group.

The same specification limits the surface to human-player presentation and leaves decisions, missions, formation effects, AI, and the shared event framework as gameplay owners.

The current whole-event source-of-truth map keeps Event 006 at HOLD / PARTIAL, but that whole-event status does not transfer ownership of any shared UI to this worker.

No source or layout rewrite was justified by the evidence, and no source file was changed by this worker.

## Event ownership proof

The accepted contract is in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md` under “Grouped state-puzzle consumer contract”.

That contract names `group_id = independence_wave_formables`, `group_scripted_gui_id = independence_wave_formable_state_puzzle_scripted_gui`, and `group_window_id = chaosx_independence_wave_formable_state_puzzle_window` for the Event 006 formable consumer.

The acceptance spec at `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` records the same surface as an Event 006 addition and explicitly excludes it from whole-event completion claims.

The owning `.gui` file is `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui` and its root window name is `chaosx_independence_wave_formable_state_puzzle_window`.

The owning scripted-GUI block is `independence_wave_formable_state_puzzle_scripted_gui` in `common/scripted_guis/chaosx_formable_state_puzzles.txt`.

The grouped consumer attaches to seventeen Event 006 decision categories, as crosswalked in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_formable_state_puzzle_category_attachment_audit_2026-08-09.md`.

## Exact identifiers and dependencies

The fourteen runtime family overlays are `independence_wave_form01_overlay`, `independence_wave_form02_overlay`, `independence_wave_form03_overlay`, `independence_wave_form04_overlay`, `independence_wave_form05_overlay`, `independence_wave_form07_overlay`, `independence_wave_form08_overlay`, `independence_wave_form09_overlay`, `independence_wave_form12_overlay`, `independence_wave_form13_overlay`, `independence_wave_form16_overlay`, `independence_wave_form18_overlay`, `independence_wave_form39_overlay`, and `independence_wave_form48_overlay`.

The fourteen activation helpers are `independence_wave_formable_state_puzzle_form01_activation`, `independence_wave_formable_state_puzzle_form02_activation`, `independence_wave_formable_state_puzzle_form03_activation`, `independence_wave_formable_state_puzzle_form04_activation`, `independence_wave_formable_state_puzzle_form05_activation`, `independence_wave_formable_state_puzzle_form07_activation`, `independence_wave_formable_state_puzzle_form08_activation`, `independence_wave_formable_state_puzzle_form09_activation`, `independence_wave_formable_state_puzzle_form12_activation`, `independence_wave_formable_state_puzzle_form13_activation`, `independence_wave_formable_state_puzzle_form16_activation`, `independence_wave_formable_state_puzzle_form18_activation`, `independence_wave_formable_state_puzzle_form39_activation`, and `independence_wave_formable_state_puzzle_form48_activation`.

The GUI state-piece sprite identifiers use `GFX_independence_wave_formXX_state_<state>_unresolved` and `GFX_independence_wave_formXX_state_<state>_qualifying` in `interface/chaosx_formable_state_puzzles.gfx`.

The corresponding static DDS pieces live under `gfx/interface/formables/state_puzzles/006_formXX_state_puzzle/states/` and are linked by that GFX file.

The GUI localisation file is `localisation/english/chaosx_formable_state_puzzles_l_english.yml`.

The grouped summary keys are `chaosx_formable_state_puzzle_independence_wave_formXX_summary` and the delayed state tooltip keys follow `chaosx_formable_state_puzzle_independence_wave_formXX_state_<state>_tt`.

The linked scripted-localisation source is `common/scripted_localisation/chaosx_formable_state_puzzles.txt`.

The seventeen decision-category entry identifiers are `independence_wave_formables_category`, `independence_wave_formable_transaction_category`, `independence_wave_form0124_membership_category`, `independence_wave_form01_congress_category`, `independence_wave_form02_union_category`, `independence_wave_form04_league_category`, `independence_wave_form03_low_countries_category`, `independence_wave_form05_charter_category`, `independence_wave_form08_danube_category`, `independence_wave_form09_balkan_category`, `independence_wave_iw043_middle_volga_congress_category`, `independence_wave_iw058_council_of_communities_category`, `independence_wave_form16_integration_category`, `independence_wave_form39_invitation_category`, `independence_wave_form39_federal_compact_category`, `independence_wave_form48_invitation_category`, and `independence_wave_form48_federal_compact_category`.

## Files changed

No Event 006 GUI, scripted-GUI, GFX, sprite, localisation, decision, or gameplay file was changed by this worker.

This handoff is the only file added by this worker.

Concurrent modifications already present in the worktree were preserved.

## References inspected

The required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.

The installed vanilla documentation consulted included `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, and `modifiers_documentation.md`.

The exact vanilla decision-category precedent inspected was `USA_congress_decision_ui` in `common/scripted_guis/USA_congress_scripted_gui.txt`, `interface/usa_congress_scripted_gui.gui`, and `common/decisions/categories/USA_decision_categories.txt`.

The Chaos Redux guidance consulted was `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation`.

The frame-animation guidance was reviewed because the event-assets rules require an animation decision for animated surfaces, but this window uses static state pieces only and no animation asset was introduced.

## Pre-change MCP evidence

The exact GUI inspect route was `hoi4.gui_inspect` for window `chaosx_independence_wave_formable_state_puzzle_window` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The settled scenario `{id: "E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09"}` returned `GUI_INSPECTED` at shared revision `57e77f6caf31f9ae8dfa206fb9f6e5beedb84936ba0a958f9b34d77a3da3b018` with 93 inspected elements.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1310393403f1901299095abace14584fad3bde23591917b8f71ec59a6d277687/353fa6bb457a36cba4ffe7ae54d2f68d5216ebf7be8e47a9e739a3863b8992cf/gui-inspect.57e77f6caf31f9ae.json`.

The current rebound scenario `{id: "E6_FORMABLE_STATE_PUZZLE_GUI_REBOUND_2026_08_14"}` returned `GUI_INSPECTED` at the same shared revision with 93 inspected elements.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21be13ab6870d29fc00700b10914414ca65de1d11e38dc842c097ae239f44646/5f72b31b47986112bf97d8513260af74972da128a998278f0aa8b5db537be42e/gui-inspect.57e77f6caf31f9ae.json`.

The current inspect retained 1,999 source-graph diagnostics and 1,999 combined validation diagnostics after truncation.

The retained validation summary reported 521 `GUI_VISIBLE_OVERLAP` findings, 48 `GUI_SCRIPTED_CONTEXT_INVALID` findings, 14 `GUI_UNRESOLVED_DYNAMIC_VALUE` findings, two inconsistent-alignment findings, and one inconsistent-spacing finding in the bounded set.

The workspace-wide symbol-collision and unresolved-reference findings dominate the retained source graph, so they are not evidence of a defect in the Event 006 root geometry.

The exact GUI render route was `hoi4.gui_render` for the same window, current rebound scenario, 1920x1080 and 1366x768 resolutions, and the generic normal, hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states.

The settled render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/a819039efc96934ff58a2190d5749c2630c348b061a88d61ed0986b9bba7fb7b/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The current rebound render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/4e3988a4cdc5e68a2cf92de5b276c4928cfeccac39686470257752c0257f6ad1/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The render route returned one linked full-window SVG and a wire-budget truncation warning rather than separate linked crop, annotation, hierarchy, click-region, state-matrix, resolution-matrix, and comparison artifacts.

The renderer marked the output as offline and approximated the project font glyphs, so the SVG is not a live HOI4 consumer proof.

An explicit FORM-08 family-isolated scenario mock was also rendered with the fourteen activation helpers set false except `independence_wave_formable_state_puzzle_form08_activation = true` and the corresponding overlay visibility map.

That render returned `GUI_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb1693d28fbe5e5639d0564cdd9afa0fb57bcbd8c9ce77c8633c8841853e690d/5a08bb6309efd7ee55dff958b81ee0ce0ec4f8a359bc5356db8ef36faa10df19/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The matching family-isolated inspect mock returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d17aa38bf40cca5d44af1b1ffa1c7edb58dd22ecf5b2962810c8ce41e5914bd1/948f48c35049a2f1fac20187f59a5bc78c38d87c6957a46c636b81c2f0d1ac62/gui-inspect.57e77f6caf31f9ae.json`.

The family-isolated request still retained aggregate workspace diagnostics, including 1,290 visible-overlap findings after the related scenario matrix was included, and therefore does not close family-isolated acceptance.

The render and inspect routes were available and resolved the exact event-owned window, so there is no route-unavailable blocker.

## Layout hierarchy and budgets

The root `containerWindowType` is 440 by 206 pixels at position 0,0 and clips to that authored area.

Each family overlay occupies that same 440 by 206 rectangle and is runtime-visible only through its family activation helper.

Each overlay places one 440-pixel summary text box at y=0 with a 22-pixel maximum height.

Each overlay places one clipped 440 by 180 map container at y=24 and keeps state pieces at the exact generated map coordinates.

The owned surface does not paint a separate background panel, frame, divider, medallion, or illustration.

The background coverage map is therefore the transparent 440 by 206 overlay area, the summary strip at y=0 to y=22, and the exact state-piece map area at y=24 to y=204.

The decision-category chrome and any shared host panel remain outside this worker's scope.

The visible value budget is one primary value per active family, namely qualifying state count versus the family required count and the readiness status.

The state-piece delayed tooltip supplies owner, controller, formation status, and core status as local supporting context.

The action budget is zero inside this window because every state piece is an informational `iconType` with a delayed tooltip and no `buttonType` or scripted-GUI effect.

The formation and membership decisions remain the actionable controls and are not part of this window.

No visible element in the owned source crosses another family's intended map geometry at runtime because the fourteen overlays are mutually exclusive by the scripted-GUI visibility triggers.

## State and resolution matrix

Normal runtime presentation shows one human-player family overlay selected by one activation helper.

Unresolved and qualifying state treatment is provided by the dynamic `properties` image mapping in `independence_wave_formable_state_puzzle_scripted_gui`.

Hover treatment is a delayed state tooltip and not a clickable action.

Selected, locked, disabled, warning, active, and completed generic states are not authored button states for this informational surface.

Empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation generic states are not a list or action model for this window, and the offline renderer cannot prove their runtime-specific dynamic localisation behavior.

FORM-08 intentionally displays states 82 and 84 while its summary required count remains three and its territory helper remains false.

FORM-07 and FORM-48 remain readiness-controlled and fail closed, so visibility of their map pieces must not be interpreted as formation admission.

The baseline render request covered 1920x1080 and 1366x768.

The GUI MCP route returned only the full-window artifact even when multiple resolutions and generic states were requested, so separate cropped, annotated, hierarchy, click-region, state-gallery, resolution-gallery, and comparison receipts remain unresolved.

## Rewrite decision and before/after behavior

No `hoi4.gui_rewrite` call was made because the only layout diagnostic that appears local to this window is the aggregate overlap caused by intentionally co-located mutually exclusive family overlays.

Moving or deleting those overlays would change exact state geometry, break the accepted generated consumer contract, or weaken runtime family selection.

Adding a new background or button would change the accepted presentation and action budgets without a source-backed defect or an approved asset handoff.

Before and after behavior are therefore identical: one human-only grouped scripted GUI, one active family overlay at runtime, dynamic unresolved or qualifying state sprites, and informational state tooltips.

There is no post-source-change inspect/render comparison because this worker made no source change.

The latest rebound and FORM-08 mock receipts above are current read-only evidence, not an after-rewrite claim.

## Assets and missing evidence

No missing asset or unapproved fallback was introduced.

The existing static state-piece DDS ladders and their GFX registrations were reused as linked dependencies.

No animation asset is required for this static window.

The unresolved evidence is family-isolated runtime visual acceptance, not asset availability.

The installed GUI MCP returned aggregate graph and overlap diagnostics and only one full-window SVG link, so clean per-family hierarchy, click-region, crop, state, resolution, and comparison artifacts remain parent-owned follow-up evidence.

## Parent-owned follow-up

The parent retains gameplay admission, Join, attestation, territory helpers, formation effects, decision costs, AI behavior, package readiness, event-log integration, runtime loading, live HOI4 validation, and final whole-event completion claims.

The parent should preserve the no-rewrite result unless a future family-isolated engine-backed receipt identifies a concrete authored layout defect.

If a later rewrite is approved, it must remain inside `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui` and any explicitly approved presentation-only helper or localisation dependency, then rerun inspect, full and family-isolated renders, hierarchy, click-region, resolution, state, and comparison evidence.

## Simplifications, omissions, and blockers

No gameplay or source simplification was made.

No new art, placeholder art, animation, button, localisation rewrite, GFX rewrite, or generated geometry change was made.

Family-isolated acceptance remains unresolved because the offline MCP scenario matrix continues to aggregate mutually exclusive overlays and workspace diagnostics.

Separate crop, annotation, hierarchy, click-region, state-matrix, resolution-matrix, and before/after comparison artifacts were not exposed by the installed `hoi4.gui_render` response despite the requested state and resolution inputs.

This handoff does not claim in-game completion.

## Parent MCP recheck — 2026-08-14

The parent repeated `hoi4.gui_inspect` for `chaosx_independence_wave_formable_state_puzzle_window` with `E6_FORMABLE_STATE_PUZZLE_GUI_REBOUND_2026_08_14` and received the same `GUI_INSPECTED` receipt at shared revision `57e77f6caf31f9ae8dfa206fb9f6e5beedb84936ba0a958f9b34d77a3da3b018`, with 93 inspected elements and the existing aggregate/truncated diagnostics.

The parent repeated `hoi4.gui_render` for the same scenario at 1920x1080 and 1366x768 across the requested generic states and received the same `GUI_RENDERED` full-window SVG; the renderer still did not expose family-isolated crop, hierarchy, click-region, resolution, state-gallery, or comparison artifacts.

No source or layout change was made after this recheck, and no `hoi4.gui_rewrite` is justified without a concrete family-isolated authored defect.
