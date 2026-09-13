---
name: chaos-redux-scripted-gui
description: Design, implement, repair, or review Chaos Redux scripted GUI layouts using reference images, native HOI4 controls, and active MCP live previews throughout construction.
---

# Chaos Redux Scripted GUI

Use this skill for scripted GUI composition, layout, interaction presentation, and visual acceptance, including attached decision displays and custom windows. It is the owner of GUI layout guidance. Actively use MCP live previews while building or repairing the GUI: edit, render, inspect the images, correct defects, and rerender throughout implementation. Do not postpone visual review until the whole window is built or treat a final screenshot as a substitute for this loop. `chaos-redux-decisions-missions` retains presentation-layer choice, gameplay action integrity, costs, requirements, AI equivalents, cleanup, and balance. Use `chaos-redux-event-assets` for reference-image and final asset production, and `chaos-redux-frame-animation` when the accepted interface needs animation.

Prose paragraphs must not be hard-wrapped; line breaks belong only between paragraphs or structural Markdown elements.

## Scope and source reading

Read `AGENTS.md`, the offline `Interface modding` and `Scripted GUI modding` pages alongside the required core wiki pages, installed vanilla documentation, and the linked source for the exact window. The installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_guis\_documentation.md` documents contexts, parent attachment, click effects and triggers, dynamic properties/lists, and dirty updates. Consult relevant localisation and script-concept documentation under the game's `documentation` directory, and inspect an exact vanilla precedent plus the closest existing Chaos Redux pattern. For an attached visual meter, the vanilla `interface\sov_paranoia_system_scripted_gui.gui` and `common\scripted_guis\SOV_paranoia_system_scripted_gui.txt` demonstrate separate background, meter, text, and dynamic frame consumers. Choose a closer precedent when the requested interaction differs. Verify context-specific scope, variable, and event-target support against installed documentation and actual consumers. Inspect pointer lifecycle, stale-target handling, and cleanup rather than assuming support or prohibition from memory.

Name the authorized window, files, entry point, parent/context, linked assets, states, resolutions, and exclusions before editing. Route a dedicated UI introduced and owned by one named event to `chaosx_event_ui_worker` under `chaos-redux-subagents`. Shared event log, event details, settings, super-event framework, shared registries, and unrelated interfaces remain parent-owned and require their own task authorization. Using this skill or opening a shared window does not authorize changing it.

## Reference image before implementation

Create reference image(s) before implementing a new or redesigned scripted GUI. Use native ImageGen through the asset workflow, or use a supplied reference that already shows the intended design. Cover materially different layouts or states with additional images where necessary. For a small repair, create a scoped reference of the intended corrected layout, such as an annotated baseline or a reference edit of the affected region. Preserve the surrounding design instead of forcing a redesign. Keep references and their acceptance record in the owning task's design or asset workspace, never inside this reusable skill.

Translate the reference as closely as feasible into a usable native HOI4 interface. Preserve composition, hierarchy, proportions, grouping, visual identity, and designed content regions while adapting impossible geometry, generated text/artifacts, unsupported effects, and styling that does not fit the inspected HOI4 family. Use real controls, live localisation, native lists/meters, accurate input regions, and wired states. A flattened picture of buttons or dynamic values is not an implementation. Decorative art may be rasterized, but interactive controls and changing information must remain functional elements.

Before source changes, record:

- reference paths and intended state/resolution
- acceptance basis: explicit user direction or the parent's recorded selection within the current authorization
- reference region to native element/ID mapping, including interaction, assets, and states
- engine constraints and justified deviations, with supporting documentation or source evidence
- missing assets and their production owners.

A file's existence, its placement in specs, a date, or an old status label does not establish approval. Existing authorization can support parent acceptance without another permission request. Do not silently drop behavior or substitute a fallback when adapting the image. Unresolved design changes follow the repository's acceptance rules.

## Content and interaction budget

The player should identify current state, main pressure/objective, and useful next actions at a glance. Use meters, thresholds, icon states, stage frames, map cues, and concise labels instead of raw variable dumps or paragraphs. Normally expose one primary mechanic value and at most two supporting values. Four simultaneously visible mechanic values is the hard ceiling on the current surface/state. A fourth needs a distinct decision, threshold, and consequence. Each visible value needs a stable name, unit/range/direction, meaningful states, consequences, a player response where intervention is possible, and a non-colour cue alongside consistent colour identity.

Normally show three to five primary actions per visible phase, with six as the hard maximum. Active missions or target controls should normally number one to three when sharing that surface. Phase, replace, or prioritize actions. Do not warehouse weak or duplicate controls in extra tabs. These budgets govern mechanic values and gameplay actions, not an unrelated cap on records in an authorized browser/list or on ordinary navigation.

Main explanations normally fit in one to three short lines. A tooltip for one value/action normally fits in two to four. Explain meaning, causes, relevant thresholds, consequences, and the player's response close to the affected element. Avoid vague text such as `Improves readiness`, duplicated instructions, raw triggers, and long mixed cost strings. Use the decision skill's cost and action-integrity rules for gameplay-changing controls, including correct texticons, at most four spendable cost types, shared validation/payment/effects, AI equivalence, and cleanup. Every button-like element must be interactive, visibly disabled with a reason, or unmistakably decorative.

## Required MCP visual review and optional rewrite

Use the installed `hoi4_agent_tools` service, registered in `.codex/config.toml` through `hoi4-agent-tools.cmd`. Discover the live schema before use. Tool exposure alone does not establish service health. The exposed GUI tools are `mcp__hoi4_agent_tools__hoi4_gui_inspect`, `mcp__hoi4_agent_tools__hoi4_gui_render`, and `mcp__hoi4_agent_tools__hoi4_gui_rewrite`. Inspection and rendering are read-only source operations. `gui_rewrite` is an optional applying/validation route.

Use `gui_render` as the live preview of the current source after each meaningful layout, asset, text, or state-wiring change, including intermediate construction stages. Inspect the returned full-window image and affected detail/state views before proceeding to the next layout tranche; a tool success message or artifact path is not an image review. Fix visible defects in the current tranche and rerender the affected scenarios before building further on that layout. For a new window with no renderable baseline, record that absence and render as soon as the first native container is renderable, then continue the same preview loop. Keep intermediate source/scenario identities and findings in the owning task's evidence so the final handoff demonstrates iterative review as well as the final comparison.

1. Inspect the exact linked window before editing. Supply `windowName` together with a valid explicit `scenario` for narrow inspection, and record source identity, hierarchy, parent/context, GFX, fonts, localisation, state logic, and click regions.
2. Render the baseline before editing, preserving full-window images and relevant detail, hierarchy, click-region, diagnostic, state, and resolution artifacts returned by the route. Read the fidelity report, resolve supplied runtime values and flags, and inspect the actual images.
3. Create/select the intended reference and native-element mapping above, then review the proposed source change against both reference and baseline.
4. Apply the authorized, reviewed GUI edit directly through the normal source-edit workflow, or optionally use `mcp__hoi4_agent_tools__hoi4_gui_rewrite` to apply and validate it. Keep dependencies and changed files inside the granted scope and review the resulting source. When choosing the optional rewrite route, use its discovered source/helpers/patches contract and exact file/window. In patches mode, use exact single scalar assignment/value ranges. Whole-line replacements spanning several assignments are rejected. `expectedSourceHash` belongs to patches mode. Do not pass it to source mode.
5. Reinspect and rerender after each accepted change over the same named scenarios, values, states, resolutions, UI scales, language, and assets as the baseline. Compare matching before/after source versions and artifact images, then compare the result with the reference. Apply the visual and usability checks below before any visual completion claim.

The optional `gui_rewrite` transaction's automatic post-write/index validation and transaction success are not mandatory GUI completion gates. If that route blocks or rolls back, review its diagnostics and current source bytes, then directly apply the already authorized, reviewed edit without another fallback approval solely because the rewrite route failed. Record the route failure and application method. Resolve actual source defects and complete the required MCP inspection, renders, click-region checks, and matched scenario/reference comparison. Do not change the installed MCP package or configuration to remove its internal checks.

`gui_render` exposes `comparisonScenario`. Use it for supported scenario comparisons, not as an assumed snapshot of older source. There is no separately exposed GUI comparison tool: preserve pre-change artifacts and source identity, and compare them with matching post-change artifacts. Preserve exact manifest/sourceRevision/scenarioId identities from returned evidence. Never substitute whichever concurrent output has the latest filename. For tabbed windows, prefer explicit per-control states. A global selected-state render can activate mutually exclusive tabs and create an impossible fixture. Keep fixture choices and provenance in the evidence manifest, not invented scenario fields such as `fixtureChoices`. For exact regression fixtures use `generatedScenarios: { enabled: false }`. Generated exploratory scenarios require a stable seed and do not replace explicit boundary cases. At 1920×1080 use `uiScale: 1`. UI scale represents the game setting, not image enlargement.

Where supported, add `scenario.expectations.visible`, `hidden`, `containedBy`, and `centeredOn` assertions against actual element selectors. `centeredOn` checks rendered glyph bounds and can catch a visually off-center label inside an apparently centered text box. A successful tool call or `validation.passed: true` does not prove visual acceptance. Warnings and rendered defects still require review and correction.

Treat the production MCP render as the one-to-one in-game visual review surface required by `AGENTS.md`. Every visible defect in the in-scope GUI blocks completion, including warnings the tool does not classify as fatal. Never dismiss bad alignment, spacing, clipping, backgrounds, states, assets, or click regions as a renderer discrepancy or defer correction for lack of a separate game screenshot. The render does not execute the game: preserve fidelity limits and unverified behavior without using them to waive visible defects. If required inspection/render evidence, artifacts, scenarios, or dependencies are unavailable, record the exact call, selector, error, and affected evidence as blocked. Source-only review is not equivalent. An incidental defect outside authorized scope becomes a parent-owned finding, not permission to edit another interface.

### Scripted GUI visual and usability review

Use this checklist when designing the native mapping and reviewing baseline and post-change MCP artifacts. Inspect the full composition at native output size and detailed crops for text and edges; record measurements where they reveal or verify a defect. Every applicable visible defect blocks visual completion regardless of the source-edit method or optional rewrite transaction outcome. Do not resize the preview or change UI scale to disguise a layout problem.

#### Geometry, typography, and control bounds

Distinguish the source texture canvas, the painted/alpha-visible shape, its designed usable interior, the logical GUI rectangle, the rendered glyph bounds, and the effective click region. Transparent padding, bevels, asymmetric ornaments, glyph bearings, borders, sprite frame dimensions, and parent transforms can make these differ. Measure the actual element after its scale, anchor/orientation, parent offsets, and frame selection; nominal texture width alone does not prove alignment.

| Check | Acceptance evidence |
| --- | --- |
| Button labels | Center the rendered text horizontally and vertically in the button's usable face, accounting for glyph metrics and line height; compare left/right and top/bottom space, including hover, selected, and disabled states. |
| Text box versus visible label | `format = center` alone does not prove vertical or optical centering; verify final glyph bounds, native font/baseline, border offsets, wrapping, and the relationship to the painted face. |
| Icon plus label | Center the combined group when the design calls for it, keep a consistent icon/text gap and baseline, and prevent the icon from shifting the label accidentally. |
| Margins and rhythm | Use consistent outer margins, inner padding, row pitch, column gutters, header gaps, card/button sizes, and divider spacing within the same family. |
| Alignment and symmetry | Align related edges, centers, baselines, and paired controls; preserve intentional asymmetry from the reference and correct unexplained imbalance. |
| Scaling and anchoring | Confirm parent-relative placement and usable bounds across the declared resolution/UI-scale matrix; art, text, borders, and hitboxes must remain aligned without distortion or unreadable shrinkage. |
| Clipping and overflow | Inspect all container and scroll boundaries, text boxes, list rows, panels, and tooltips; no truncated labels, cut glyphs, hidden costs, half rows, or controls outside their intended region. |
| Contrast and font consistency | Match the inspected HOI4 font family and hierarchy; retain readable text and meaningful non-colour state cues against art in every state. |

Use actual native properties documented by the installed game and existing consumers. Do not invent CSS-style alignment fields or assume a sprite's `scale` transforms label metrics and hit geometry identically. If native button text cannot meet the layout, use a proven native text/control composition with verified click-through and state synchronization; do not leave a second painted label underneath.

#### Background and reference coverage

Treat a designed background as the composition blueprint. Map each prominent panel, inset, slot, medallion, divider, illustration, ornament, and functional anchor before placing content. Preserve intentional negative space while assigning each designed usable region a purpose; a crowded corner next to abandoned functional panels is a defect. Keep text and controls inside the intended usable interiors, clear of borders, handles, seals, illustrations, and other important art. If content cannot fit the art, revise the composition or background within the accepted design instead of layering an unrelated generic layout over it.

Record one mapping that covers both the reference and background:

| Reference/background region | Native GUI IDs and usable bounds | Content and interaction | Assets/states | Constraint or deviation and acceptance basis |
| --- | --- | --- | --- | --- |

Compare full-window renders with the reference at corresponding aspect/scale and with the actual source background. Check composition, hierarchy, focal points, proportions, button placement, density, illustration clearance, borders, and intentional empty space. Generated gibberish, fake labels, impossible components, and non-HOI4 effects must be replaced with usable native design and recorded adaptations. No reference button, meter, list, selection, or dynamic label may survive merely as flattened art when it represents actual interaction/state.

#### Click regions, overlap, and state behavior

- Match the effective hitbox to the visible intended control face after scaling and parent transforms; inspect edge and center coverage and separation between adjacent controls.
- No invisible blocker may swallow input; decorative overlays and separate labels must have appropriate click-through behavior supported by their native element type.
- Review z-order and hierarchy for backgrounds, cards, icons, text, highlights, tooltips, popups, and selection overlays; required controls and text must not be occluded.
- Check hover, pressed, selected, active, completed, locked, warning, available, and disabled treatment where the control supports them; missing tool support is an evidence limitation, not permission to claim a tested state.
- Keep frame size, label position, hitbox, contrast, and icon placement stable across states unless the reference intentionally specifies a supported change.
- Confirm selected/active states follow the displayed choice, disabled controls cannot perform the action, and their tooltip explains the blocked reason without relying on colour alone.
- Verify hidden/inactive panels cannot intercept clicks; mutually exclusive panels and actions must not overlap visibly or remain simultaneously interactive.
- Inspect close/back/open, tabs, target selection, list scrolling, and tooltip placement in the actual parent context; navigation must stay discoverable and usable in crowded states.
- Distinguish decorative texture, informational panels, and real controls visually; reject button-shaped decoration, dead controls, empty click boxes, and controls added to fill space.

#### Scenario coverage and evidence

Derive normal review scenarios from the linked source and accepted behavior, with coherent values and controls that can coexist on the same route. Label synthetic maximum-control stress fixtures explicitly and keep them separate from route-valid normal screens; do not present mutually impossible controls as normal behavior. Trace every rendered number to declared scenario inputs and its actual display source; for costs, also trace the value to the affordability checks and payment contract. Keep exact fixture values, selection, visibility/enabled state, localisation, list rows, reference version, source identity, and resource identities in the evidence manifest. Read each emitted scenario's actual resolution and UI scale before claiming coverage; an explicit scenario resolution can override a render request's resolution list. Use separately identified scenarios with explicit resolution and scale when the emitted matrix does not contain the requested combinations. Use the live route's supported scenario fields and selectors; keep commentary and fixture provenance outside tool requests.

Cover the applicable normal, hover, selected, disabled/locked, warning, active/completed, empty-list, full-list/crowded, minimum-value, maximum-value, long-text, and missing-localisation cases, plus actual open/closed panels and mutually exclusive phases. Include the longest real labels, multi-line content where supported, large cost/value strings, selected targets with long names, and boundary rows in scrollable lists. Declare the supported resolution/UI-scale matrix from the brief and actual consumer, with 1920×1080 at scale 1 as the baseline unless the task specifies another target. Rerun matching scenarios after the patch; a different seed, runtime value, language, source dependency, or scale must not masquerade as an improvement.

Use supported `expectations.centeredOn` for label/button relationships, `containedBy` for intended parent/background regions, and `visible`/`hidden` for known state boundaries. Review warnings, source diagnostics, fidelity limits, hit-region artifacts, and the images themselves alongside assertions. Record findings by element/state/resolution with before/after evidence and disposition; a passing validation boolean never overrides a visible defect.

#### Usability and integration

Check that the player can identify the current state, main objective or pressure, next meaningful action, and its consequences without cross-referencing documentation. Keep related status, thresholds, costs, blocked reasons, and actions together, with concise labels and precise tooltips. Label counters truthfully as cumulative, periodic, or latest-receipt values, and distinguish all-cause totals from contributions attributed to the owning system. Show retained reserves as non-consumed requirements, separate from consumed costs, and make the actual debit clear. Apply the skill's mechanic-value/action budgets without using extra tabs to evade them. For gameplay controls, obtain the decision owner's evidence that shown costs and requirements match selection checks, payment, effect, AI equivalent, and cleanup; a visual pass cannot establish gameplay balance. For information-only or navigation controls, verify their declared purpose and enabled/selected behavior instead of demanding a gameplay effect. Report any out-of-scope shared-interface problem to the parent without editing it.

## Handoff and completion

Return exact changed files/identifiers, source precedents, reference images and acceptance basis, image-to-element/background mapping, justified native adaptations, asset/state coverage, and matched MCP before/after artifacts with scenario/source identities. Include the intermediate MCP preview evidence and corrections, completed visual-review findings, content/action budget assessment, and the decision owner's action-integrity evidence where gameplay controls exist. List blockers, unresolved diagnostics, missing assets, unavailable states, remaining parent integration, and every simplification explicitly. If none, say so with the evidence. Do not claim a complete GUI from source checks, a successful rewrite, or a single normal-state screenshot. The parent reviews final integration. Live-game validation belongs to the user under `AGENTS.md` and is not replaced by MCP evidence.
