# Event 020 Black Plague Response GUI Repair Handoff

## Disposition

`implemented` for the bounded source repair, with mandatory post-change production visual evidence unresolved because the registered `hoi4.gui_inspect` and `hoi4.gui_render` routes timed out before returning artifacts. The parent must keep the visual completion claim pending until the exact window is rendered and reviewed.

## Event ownership and accepted scope

The owned event is `020_black_plague` with root event `chaosx.nr20.1` in `events/020_black_death.txt`.

`common/decisions/categories/020_black_plague_response_categories.txt` owns `black_plague_response_category`, assigns the parent-owned `GFX_decision_cat_picture_black_plague_response` category picture, and attaches `black_plague_response_category_scripted_gui`.

`common/scripted_guis/020_black_plague_response_scripted_guis.txt` owns the presentation binding with `context_type = decision_category` and `window_name = "black_plague_response_category_window"`.

`interface/020_black_plague_response.gui` defines the dedicated Event 020 window, and `interface/020_black_plague_response.gfx` is its event-owned sprite registry.

The parent prompt is the acceptance basis for this bounded repair: remove only the duplicate embedded GUI picture, reclaim its header space, make zero progress visually empty, suppress the exhausted warning for an unorganized `0 / 0` capacity state, preserve ordinary decision actions and costs, and fit 1920×1080 and 2560×1440 at UI scale 1.

The category file, visibility trigger, decision effects, decision costs, AI behavior, and shared interfaces were outside this edit.

## Reference and native mapping

The supplied bad reference is `C:/Users/klimp/OneDrive/Pictures/Screenshots/Screenshot 2026-09-20 182952.png`. It shows the category picture followed by a duplicate picture in the attached window, a clipped title, five white fill pills at zero progress, and an exhausted-capacity warning for `0 / 0`.

The bounded intended reference created before editing is `docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_repair_intended.svg`. It preserves the native decision-category composition and maps the header to the full-width title and programme status, the meter to a vanilla tiled empty background plus five native visibility-gated fill icons, the lower band to the existing deaths and response-capacity text, and the bottom line to a conditional warning only when organized capacity exists and is exhausted.

The parent-owned category picture remains the event identity anchor above the attachment. The GUI no longer paints a second copy.

The progress fill reuses the installed vanilla `gfx/interface/tiles/tiled_progress_bar_color.dds` texture through the event-owned `GFX_black_plague_response_progress_fill` `corneredTileSpriteType` at 96×27. The empty background remains vanilla `GFX_tiled_progress_bar`.

| Reference region | Native implementation | Acceptance reason |
| --- | --- | --- |
| Event identity above the attached panel | Parent-owned category `picture = GFX_decision_cat_picture_black_plague_response` | Removing the duplicate GUI icon preserves one identity anchor. |
| Full-width header | `black_plague_response_gui_title` and `black_plague_response_gui_programme_status` at x=20 with maxWidth 480 | Reclaims the former picture column and prevents title/status clipping. |
| Empty or funded progress meter | Vanilla `GFX_tiled_progress_bar` background plus five named `iconType` overlays | Native scripted-GUI visibility triggers can hide each overlay at its threshold. |
| Lower status band | Existing National Deaths and Response Capacity text boxes in `GFX_tiled_window_transparent` | Keeps the accepted one-primary/two-supporting-value budget. |
| Capacity exhaustion | Existing warning text with a new positive-total-capacity gate | `0 / 0` remains neutral and does not read as exhausted. |

## Files changed

- `interface/020_black_plague_response.gui`: removed the duplicate `black_plague_response_category_picture` icon, widened the title and programme status to the 480-pixel content width, and changed each five-segment overlay from a visibility-ineligible `containerWindowType` background to a named `iconType`.
- `interface/020_black_plague_response.gfx`: registered `GFX_black_plague_response_progress_fill` as a 96×27 event-owned cornered tile using the installed vanilla coloured progress-bar texture.
- `common/scripted_guis/020_black_plague_response_scripted_guis.txt`: retained the five existing progress thresholds and changed the warning gate to require total `black_plague_response_capacity > 0` before treating missing or zero remaining capacity as exhausted.
- `docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_repair_intended.svg`: added the bounded native layout reference used for this repair.
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-09-20_event020_black_plague_gui_repair_handoff.md`: this handoff.

I did not edit `common/decisions/020_black_plague_response_decisions.txt` or the parent-owned medical-reserve localisation lines 50–54. The parent’s concurrent `Stock Reserves` label and compact cost row remain separate.

## Layout hierarchy and budgets

1. `black_plague_response_category_window` remains a 520×282 non-movable, clipped, dark `GFX_tiled_window` container.
2. The category picture is supplied by the parent-owned decision category, so the attached window header now uses the full 20–500 content span for `black_plague_response_gui_title` and `black_plague_response_gui_programme_status`.
3. `black_plague_response_gui_progress_label` and `black_plague_response_gui_progress_value` identify the one primary mechanic value.
4. `black_plague_response_gui_progress_meter` remains a 480×27 vanilla empty meter with five contiguous 96×27 icon overlays.
5. `black_plague_response_gui_outbreak_summary` remains one balanced 480×70 band for National Deaths and Response Capacity.
6. `black_plague_response_gui_capacity_warning` remains a single short conditional line.

The panel has one primary mechanic value, two supporting numeric values, one programme-stage status, zero gameplay-changing GUI actions, zero spendable cost types, and zero click regions. No cost is duplicated in the panel; ordinary decision rows retain their own exact cost and tooltip surfaces.

The neutral unorganized state keeps the existing `Response Capacity 0 / 0` live value and hides the exhausted warning because total capacity is zero. This is the accepted neutral equivalent of “Not organized” without introducing a second scripted-localisation route or a static text that would be wrong once capacity is funded.

## State matrix and source behavior

| State | Source behavior | Visual evidence status |
| --- | --- | --- |
| Before active | The existing programme status and live numeric values remain authoritative; no duplicate picture is painted by the attachment. | Post-change MCP render unavailable. |
| Active, zero progress | All five named fill icons fail their existing thresholds, leaving the vanilla dark background empty. | Post-change MCP render unavailable. |
| Active, funded | The existing threshold gates reveal contiguous 96-pixel fills at 20, 40, 60, 80, and 100 progress. | Post-change MCP render unavailable. |
| Completed | The maximum threshold reveals all five fill icons and the existing completed programme status remains visible. | Post-change MCP render unavailable. |
| Capacity exhausted | The warning appears only when total capacity is positive and remaining capacity is absent or zero. | Post-change MCP render unavailable. |
| Unorganized `0 / 0` | The live value remains neutral `0 / 0` and the exhausted warning is suppressed. | Source-gated; post-change MCP render unavailable. |
| Hover, selected, disabled | No custom controls exist, so there are no hover, selected, or disabled action variants. Existing informational tooltips remain attached to the text and meter surfaces. | Source-only; no click-region artifact returned. |

## Pre-change MCP and visual evidence

The supplied screenshot is the current bad production reference described above.

The parent-provided baseline is revision `ddf2bde08e1991b63b135a19e528c676f192abb82a4d749bc1b60da50517295f`, with the `black_plague_response_category_window-full.png` artifact in the MCP artifact family.

The earlier exact-window evidence remains useful context: the 2026-08-22 handoff recorded a successful pre-change inspect at workspace `mod_chaos_redux_ea3b2d67c2c0`, an exact 21-element window, and the normal artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/864949744301256fd05c470d5737420995624e131d16dc7e6b6f79218a3afe3f/3e03aca61653cfea097fa2b30464d3ddbfd144e2c235998d6cc6e2990c46d546/black_plague_response_category_window-full.svg`.

The earlier handoff also records the prior post-change inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d94db440fc0d6a27e0336f944f3e12423fc917f9fa2de86f8863d4adbbc2d5ac/e6e59be88672c65f60da839c070d64c1dcd0a86c250222623418b72289e8e02f/gui-inspect.235c618fde462b56.json` and its recovered matrix. Those artifacts predate this repair and do not prove the current source.

## Post-change MCP evidence

The required exact post-change `hoi4.gui_inspect` call targeted workspace `mod_chaos_redux_ea3b2d67c2c0`, window `black_plague_response_category_window`, and scenario `representative_plague_response`. It timed out after 180 seconds with `tool call failed for hoi4_agent_tools/hoi4.gui_inspect: timed out awaiting tools/call after 180s` and returned no artifacts, diagnostics, hierarchy, or click regions.

The required exact post-change `hoi4.gui_render` call targeted the same window with explicit `1920×1080` and `2560×1440` resolutions at UI scale 1 and states normal, hover, selected, active, warning, completed, minimum-value, maximum-value, and long-text. It timed out after 180 seconds with `tool call failed for hoi4_agent_tools/hoi4.gui_render: timed out awaiting tools/call after 180s` and returned no full-window, crop, hierarchy, click-region, resolution, state, or comparison artifacts.

The registered route therefore cannot establish production visual completion for this repair. The exact route, selectors, resolutions, states, and timeout errors are recorded here so the parent can retry with the documented bounded MCP scan-ceiling workaround if available.

The adjacent parent-owned Medical Reserve decision row was not independently validated by this exact window route because the route returned no category-stack or decision-row artifact. The parent should include `Stock Reserves`, its compact icon spacing, and its tooltip in the parent’s decision-surface render before final integration.

## Source checks and remaining validation

The event-owned GFX source resolves the vanilla coloured meter texture at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/tiles/tiled_progress_bar_color.dds`.

Static source checks confirmed that the duplicate picture identifier is absent from the GUI, all five fill icons use the event-owned sprite, each scripted visibility trigger has a matching icon name, the warning gate includes total-capacity positivity, and the modified files have no whitespace errors in `git diff --check`.

No live Hearts of Iron IV session was run. User live consumer validation remains pending, and the parent must not claim in-game completion from this handoff alone.

## Simplifications, omissions, and blockers

- MCP blocker: the registered post-change inspect and render calls timed out before producing artifacts, so visual, hierarchy, click-region, state, resolution, and comparison acceptance remains unresolved.
- The `0 / 0` neutral state uses the existing numeric capacity line and a suppressed warning as the equivalent of “Not organized”; no separate scripted-localisation key was added.
- No new raster art, placeholder art, animation, gameplay effect, cost, AI rule, decision, category, or shared UI was added or changed.
- The adjacent Medical Reserve decision row remains parent-owned and awaits the parent’s cost-row validation.
