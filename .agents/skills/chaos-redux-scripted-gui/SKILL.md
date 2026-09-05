---
name: chaos-redux-scripted-gui
description: Design, implement, repair, or review Chaos Redux scripted GUI layouts using reference images, native HOI4 controls, and mandatory MCP visual evidence.
---

# Chaos Redux Scripted GUI

Use this skill for scripted GUI composition, layout, interaction presentation, and visual acceptance, including attached decision displays and custom windows.
It is the owner of GUI layout guidance; `chaos-redux-decisions-missions` retains presentation-layer choice, gameplay action integrity, costs, requirements, AI equivalents, cleanup, and balance.
Use `chaos-redux-event-assets` for reference-image and final asset production, and `chaos-redux-frame-animation` when the accepted interface needs animation.

## Scope and source reading

Read `AGENTS.md`, the offline `Interface modding` and `Scripted GUI modding` pages alongside the required core wiki pages, installed vanilla documentation, and the linked source for the exact window.
The installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_guis\_documentation.md` documents contexts, parent attachment, click effects and triggers, dynamic properties/lists, and dirty updates.
Consult relevant localisation and script-concept documentation under the game's `documentation` directory, and inspect an exact vanilla precedent plus the closest existing Chaos Redux pattern.
For an attached visual meter, the vanilla `interface\sov_paranoia_system_scripted_gui.gui` and `common\scripted_guis\SOV_paranoia_system_scripted_gui.txt` demonstrate separate background, meter, text, and dynamic frame consumers; choose a closer precedent when the requested interaction differs.
Verify context-specific scope, variable, and event-target support against installed documentation and actual consumers; inspect pointer lifecycle, stale-target handling, and cleanup rather than assuming support or prohibition from memory.

Name the authorized window, files, entry point, parent/context, linked assets, states, resolutions, and exclusions before editing.
Route a dedicated UI introduced and owned by one named event to `chaosx_event_ui_worker` under `chaos-redux-subagents`.
Shared event log, event details, settings, super-event framework, shared registries, and unrelated interfaces remain parent-owned and require their own task authorization.
Using this skill or opening a shared window does not authorize changing it.

## Reference image before implementation

Create reference image(s) before implementing a new or redesigned scripted GUI.
Use native ImageGen through the asset workflow, or use a supplied reference that already shows the intended design; cover materially different layouts or states with additional images where necessary.
For a small repair, create a scoped reference of the intended corrected layout, such as an annotated baseline or a reference edit of the affected region; preserve the surrounding design instead of forcing a redesign.
Keep references and their acceptance record in the owning task's design or asset workspace, never inside this reusable skill.

Translate the reference as closely as feasible into a usable native HOI4 interface.
Preserve composition, hierarchy, proportions, grouping, visual identity, and designed content regions while adapting impossible geometry, generated text/artifacts, unsupported effects, and styling that does not fit the inspected HOI4 family.
Use real controls, live localisation, native lists/meters, accurate input regions, and wired states; a flattened picture of buttons or dynamic values is not an implementation.
Decorative art may be rasterized, but interactive controls and changing information must remain functional elements.

Before source changes, record:

- reference paths and intended state/resolution;
- acceptance basis: explicit user direction or the parent's recorded selection within the current authorization;
- reference region to native element/ID mapping, including interaction, assets, and states;
- engine constraints and justified deviations, with supporting documentation or source evidence;
- missing assets and their production owners.

A file's existence, its placement in specs, a date, or an old status label does not establish approval.
Existing authorization can support parent acceptance without another permission request.
Do not silently drop behavior or substitute a fallback when adapting the image; unresolved design changes follow the repository's acceptance rules.

## Required MCP visual review and optional rewrite

Use the installed `hoi4_agent_tools` service, registered in `.codex/config.toml` through `hoi4-agent-tools.cmd`.
Discover the live schema before use; tool exposure alone does not establish service health.
The exposed GUI tools are `mcp__hoi4_agent_tools__hoi4_gui_inspect`, `mcp__hoi4_agent_tools__hoi4_gui_render`, and `mcp__hoi4_agent_tools__hoi4_gui_rewrite`.
Inspection and rendering are read-only source operations; `gui_rewrite` is an optional applying/validation route.

1. Inspect the exact linked window before editing.
   Supply `windowName` together with a valid explicit `scenario` for narrow inspection, and record source identity, hierarchy, parent/context, GFX, fonts, localisation, state logic, and click regions.
2. Render the baseline before editing, preserving full-window images and relevant detail, hierarchy, click-region, diagnostic, state, and resolution artifacts returned by the route.
   Read the fidelity report, resolve supplied runtime values and flags, and inspect the actual images.
3. Create/select the intended reference and native-element mapping above, then review the proposed source change against both reference and baseline.
4. Apply the authorized, reviewed GUI edit directly through the normal source-edit workflow, or optionally use `mcp__hoi4_agent_tools__hoi4_gui_rewrite` to apply and validate it.
   Keep dependencies and changed files inside the granted scope and review the resulting source.
   When choosing the optional rewrite route, use its discovered source/helpers/patches contract and exact file/window.
   In patches mode, use exact single scalar assignment/value ranges; whole-line replacements spanning several assignments are rejected.
   `expectedSourceHash` belongs to patches mode; do not pass it to source mode.
5. Reinspect and rerender after each accepted change over the same named scenarios, values, states, resolutions, UI scales, language, and assets as the baseline.
   Compare matching before/after source versions and artifact images, then compare the result with the reference.
   Read [references/visual-review.md](references/visual-review.md) for the required visual and usability checks before any visual completion claim.

The optional `gui_rewrite` transaction's automatic post-write/index validation and transaction success are not mandatory GUI completion gates.
If that route blocks or rolls back, review its diagnostics and current source bytes, then directly apply the already authorized, reviewed edit without another fallback approval solely because the rewrite route failed.
Record the route failure and application method; resolve actual source defects and complete the required MCP inspection, renders, click-region checks, and matched scenario/reference comparison.
Do not change the installed MCP package or configuration to remove its internal checks.

`gui_render` exposes `comparisonScenario`; use it for supported scenario comparisons, not as an assumed snapshot of older source.
There is no separately exposed GUI comparison tool: preserve pre-change artifacts and source identity, and compare them with matching post-change artifacts.
Preserve exact manifest/sourceRevision/scenarioId identities from returned evidence; never substitute whichever concurrent output has the latest filename.
For tabbed windows, prefer explicit per-control states; a global selected-state render can activate mutually exclusive tabs and create an impossible fixture.
Keep fixture choices and provenance in the evidence manifest, not invented scenario fields such as `fixtureChoices`.
For exact regression fixtures use `generatedScenarios: { enabled: false }`; generated exploratory scenarios require a stable seed and do not replace explicit boundary cases.
At 1920×1080 use `uiScale: 1`; UI scale represents the game setting, not image enlargement.

Where supported, add `scenario.expectations.visible`, `hidden`, `containedBy`, and `centeredOn` assertions against actual element selectors.
`centeredOn` checks rendered glyph bounds and can catch a visually off-center label inside an apparently centered text box.
A successful tool call or `validation.passed: true` does not prove visual acceptance; warnings and rendered defects still require review and correction.

Treat the production MCP render as the one-to-one in-game visual review surface required by `AGENTS.md`.
Every visible defect in the in-scope GUI blocks completion, including warnings the tool does not classify as fatal.
Never dismiss bad alignment, spacing, clipping, backgrounds, states, assets, or click regions as a renderer discrepancy or defer correction for lack of a separate game screenshot.
The render does not execute the game: preserve fidelity limits and unverified behavior without using them to waive visible defects.
If required inspection/render evidence, artifacts, scenarios, or dependencies are unavailable, record the exact call, selector, error, and affected evidence as blocked; source-only review is not equivalent.
An incidental defect outside authorized scope becomes a parent-owned finding, not permission to edit another interface.

## Content and interaction budget

The player should identify current state, main pressure/objective, and useful next actions at a glance.
Use meters, thresholds, icon states, stage frames, map cues, and concise labels instead of raw variable dumps or paragraphs.
Normally expose one primary mechanic value and at most two supporting values; four simultaneously visible mechanic values is the hard ceiling on the current surface/state.
A fourth needs a distinct decision, threshold, and consequence.
Each visible value needs a stable name, unit/range/direction, meaningful states, consequences, a player response where intervention is possible, and a non-colour cue alongside consistent colour identity.

Normally show three to five primary actions per visible phase, with six as the hard maximum; active missions or target controls should normally number one to three when sharing that surface.
Phase, replace, or prioritize actions; do not warehouse weak or duplicate controls in extra tabs.
These budgets govern mechanic values and gameplay actions, not an unrelated cap on records in an authorized browser/list or on ordinary navigation.

Main explanations normally fit in one to three short lines; a tooltip for one value/action normally fits in two to four.
Explain meaning, causes, relevant thresholds, consequences, and the player's response close to the affected element.
Avoid vague text such as `Improves readiness`, duplicated instructions, raw triggers, and long mixed cost strings.
Use the decision skill's cost and action-integrity rules for gameplay-changing controls, including correct texticons, at most four spendable cost types, shared validation/payment/effects, AI equivalence, and cleanup.
Every button-like element must be interactive, visibly disabled with a reason, or unmistakably decorative.

## Handoff and completion

Return exact changed files/identifiers, source precedents, reference images and acceptance basis, image-to-element/background mapping, justified native adaptations, asset/state coverage, and matched MCP before/after artifacts with scenario/source identities.
Include the completed visual-review findings, corrected defects, content/action budget assessment, and the decision owner's action-integrity evidence where gameplay controls exist.
List blockers, unresolved diagnostics, missing assets, unavailable states, remaining parent integration, and every simplification explicitly; if none, say so with the evidence.
Do not claim a complete GUI from source checks, a successful rewrite, or a single normal-state screenshot.
The parent reviews final integration; live-game validation belongs to the user under `AGENTS.md` and is not replaced by MCP evidence.
