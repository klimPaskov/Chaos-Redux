# Event 002 cure progress GUI release handoff

**Disposition: blocked and incomplete.** The event-owned cure panel was inspected and rendered before source edits, but its scripted-localisation values remain unresolved in the production MCP image and the 0/partial/full render matrix timed out. No gameplay, GUI, GFX, or localisation source was changed.

## Ownership and acceptance basis

Event `002_zombie_outbreak` owns the panel through `common/decisions/categories/002_zombie_outbreak_categories.txt`: category `chaosx_zzz_cure_category` attaches `zzz_cure_progress_scripted_gui`.

`common/scripted_guis/002_zombie_outbreak_scripted_guis.txt` defines `zzz_cure_progress_scripted_gui` with `context_type = decision_category`, `window_name = zzz_cure_progress_container`, the dynamic bottle property, and a player-only visibility condition.

The category is visible for normal-civilian countries while a live standard zombie outbreak exists; it is an event-owned decision-category display, not the shared event log, event-details UI, settings, or super-event window.

No directory exists at `docs/specs/002_zombie_outbreak_specs/`. The parent task explicitly assigned the existing cure GUI release repair and limited this worker to the `zzz_cure_progress_container` block plus the required evidence and handoff; that task is the acceptance basis for this bounded review.

`docs/plans/002_zombie_outbreak_plans/agent_decisions_2026-10-05.md` records that the prior Event 002 QA had no accepted source spec and did not design a new target-selection interface, category, or event branch.

## Exact surface and linked identifiers

| Surface | Identifier or path | Evidence |
|---|---|---|
| Decision entry point | `chaosx_zzz_cure_category` | `common/decisions/categories/002_zombie_outbreak_categories.txt:3` |
| Scripted GUI | `zzz_cure_progress_scripted_gui` | `common/scripted_guis/002_zombie_outbreak_scripted_guis.txt:6` |
| GUI window | `zzz_cure_progress_container` | `interface/chaosx_decisions.gui:18` |
| Bottle element | `zombie_cure_progress_bottle` | Dynamic property `[GetZombieCureCategoryBottleSprite]` |
| Header element | `zombie_cure_progress_header` | Localisation key `zzz_cure_category_progress_header` |
| Body element | `zombie_cure_progress_body` | Localisation key `zzz_cure_category_progress_body` |
| Dynamic text accessors | `GetZombieCureCategoryCurrentProgress`, `GetZombieCureCategoryResearchMode`, `GetZombieCureCategoryActivationEffect` | `common/scripted_localisation/chaosx_scripted_localisation.txt:192`, `:214`, `:230` |
| Cure sprite registration | `GFX_decision_category_zombies_cure` and `GFX_decision_category_zombies_cure_0` through `_100` in increments of 10 | `interface/chaosx_decisions.gfx:32` |
| Bottle DDS family | `gfx/interface/decisions/002_zombie_outbreak/zombie_cure/zombie_cure_<0-100>.dds` | Each registered stage is a 100x100, one-frame sprite. |
| GUI localisation | `localisation/english/chaosx_decisions_l_english.yml:7` | English header, body, local/shared research, local/shared activation, and progress values are already present. |
| Gameplay controls | None in this window | The window contains no decision buttons, costs, click effects, or AI action controls. |

No matching Event 002 asset manifest or GFX handoff naming the cure-progress sprite was found under `docs/assets/002_zombie_outbreak/`. The runtime sprite and DDS paths resolve in the MCP source graph and render; no new art was requested or produced.

## Reference and native-element mapping

The scoped baseline reference is `docs/plans/002_zombie_outbreak_plans/cure_gui_evidence/baseline_0_local_cropped.png`, with its element-bound overlay at `docs/plans/002_zombie_outbreak_plans/cure_gui_evidence/baseline_0_local_annotated.png`. The images preserve the existing composition for review; they are not approval for a broader redesign, and the unresolved dynamic text means they are not an accepted final target.

The acceptance basis for retaining the source-defined composition is the parent’s explicit repair assignment. The window has no custom background, frames, buttons, or lists; the bottle image and text remain native HOI4 elements.

| Reference region | Native element and usable bounds | Content and state | Adaptation or limitation |
|---|---|---|---|
| Left bottle | `zombie_cure_progress_bottle`, logical rect 100x100 at x=8,y=4 inside the 470x126 container | Stage sprite from `GFX_decision_category_zombies_cure_0` through `_100` | Native `iconType`; texture canvas is 100x100. The source accessor selects the stage. |
| Header | `zombie_cure_progress_header`, x=104,y=8, width 352, height 18 | Cure progress percentage and 100% target | Native left-aligned `instantTextBoxType`, font `hoi_18b`; source uses a scripted-localisation accessor. |
| Body | `zombie_cure_progress_body`, x=104,y=34, width 352, maxHeight 92 | Local/shared research profile, activation duration, and one explanatory sentence | Native left-aligned `instantTextBoxType`, font `hoi_16mbs`; the two profile lines depend on scripted-localisation accessors. |
| Panel | `zzz_cure_progress_container`, x=0,y=0, width 470, height 126 | Attached below the decision-category description | No painted background or controls are defined in the owned block. |

The vanilla precedent reviewed was `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`; its separate icon and text elements follow the same decision-category context pattern.

The installed game documentation `common/scripted_guis/_documentation.md` was read at lines 1-146, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`. It documents decision-category scope and window attachment.

The offline wiki `Interface modding` section for `instantTextBoxType` was read at lines 196-226, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`. It documents the text-box width, height, font, and alignment fields used by this panel.

The offline wiki `Scripted GUI modding` decision-category context row was read at line 157, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`.

`hoi4.source_lookup` located vanilla `sov_paranoia_system_ui_window` in `game:interface/sov_paranoia_system_scripted_gui.gui`, definition lines 20-188, source revision `2a183af8646a1857d04a1a0331b230fafb81fb21784dabdc8d5a6cb48678d61a`. The underlying vanilla interface and scripted-GUI source were read directly.

## Pre-change MCP evidence

`hoi4.gui_inspect` succeeded for `zzz_cure_progress_container`, scenario `event002_cure_zero_local_usa_1936`, with `status = GUI_INSPECTED` and `sharedRevision = 91925adfb323285dfde8361228bfde4ea6762d28e6478545eb4f9929b3bfa9e0`.

The linked inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a86698c8b07a08e8b85f8665e66da49e20bc17c836ef9932d70db09485ddd495/dea8907cf34208e92f9a2f5798a00c2d573b9021f1bb52f0ce2097b9900f217d/gui-inspect.91925adfb323285d.json`; its 475849 bytes were assembled from byte ranges and its SHA-256 was verified.

The inspect graph linked the three window children, sprite `GFX_decision_category_zombies_cure_0`, both fonts, localisation keys, parent container, source files, and zero clickable elements. It reported unresolved scripted-GUI visibility and unresolved values for the current-progress, research-mode, and activation-effect accessors.

A second `hoi4.gui_inspect` request for the local 0% scenario with country, variable, value, localisation, and outbreak-flag facts timed out after 600 seconds and produced no artifact.

The successful baseline `hoi4.gui_render` used scenario `event002_cure_zero_local_usa_1936_minimal`, date `1936.1.1`, country `{tag: USA}`, `variables.zzz_cure = 0`, `values.zzz_cure = 0`, `flags.has_zombie_outbreak = true`, empty `localisation`, `generatedScenarios: {enabled: false}`, resolution 1920x1080, and UI scale 1. Its linked layout source revision is `50b87d3ef2eb9abd7371d7d46ad95024618ca17c2d31b4661c4b17578268b678`.

The full, cropped, annotated, source-map, scenario-matrix, state-matrix, resolution-scale, and comparison images were retrieved from the MCP artifact resources, verified against their declared SHA-256 hashes, and archived in the evidence folder. The state matrix contains only `normal`, and the resolution matrix contains only 1920x1080 at UI 1.

The `comparison.png` artifact is the render route’s generic comparison view without a supplied `sourceBaseline`; it is not a source before/after comparison. No source changed in this pass, so no after-source comparison is claimed.

The rendered header is `Cure Progress: [dynamic_loc] / 100%`, and the body begins with two `[dynamic_loc]` lines. This is a visible production-render defect and blocks visual acceptance. The static explanatory sentence resolves and wraps into two lines.

The layout artifact reports the container at 470x126; bottle at 8,4 with a 100x100 sprite; header at 104,8 with a 352x18 box; and body at 104,34 with a 352x92 box. The rendered text bounds show no horizontal or vertical overflow, no missing glyphs, and no clipping; the body occupies four 16-pixel lines with the unresolved tokens. The 18-pixel header glyph run measures 219 pixels, and the body’s longest static line measures 317 pixels.

The full-window click-region PNG has the same content SHA-256 as the full-window PNG, consistent with the source containing no buttons. Its resource-provenance URI returned `MCP error -32603: Artifact provenance manifest is unavailable`; the exact image was recovered from the local MCP artifact cache and verified at `baseline_0_local_click-regions.png`. The inspect graph confirms zero clickable elements, but no independent click overlay was available.

## State, text, cost, and visual checklist

The source-defined local research branch exposes one cure-progress percentage, one research-mode statement, one activation-duration statement, and one explanatory sentence. This is one mechanic value, zero gameplay actions, zero displayed costs, and zero spendable cost types; no texticons are required.

The source-defined shared profile uses the shared research and 120-day activation strings. The local profile uses national research and a 360-day activation string. The source also switches the progress value to 100 when `cure_activated` is present and reads global progress for members of `cure_sharing`.

The first successful render only covers the local 0% scenario. The full/partial follow-up matrix and the isolated 46% render using the parent-supplied bare accessor names timed out after 600 seconds with no artifacts; therefore 46% and 100% stage visuals remain unresolved.

Hover, selected, locked, disabled, warning, and button-active states are inapplicable because the window defines no controls. Empty-list and crowded-list states are inapplicable because it defines no list. The cure-category entry is unavailable outside the outbreak source gate; an inactive-category screenshot was not produced.

The panel uses left-aligned labels rather than button text. The output’s visual bottle shape leaves clear space before the x=104 text columns; the MCP layout reports no overlap or overflow. The container has no custom background, and no asset or font is missing.

The renderer does not resolve the three scripted-localisation accessors from the supplied country, variable, value, and flag records alone. The correct source-derived value map uses bare accessor names, with `GetZombieCureCategoryCurrentProgress`, `GetZombieCureCategoryResearchMode`, `GetZombieCureCategoryActivationEffect`, and `GetZombieCureCategoryBottleSprite`; a render using those values still timed out after 600 seconds.

The live GUI schema rejects `scenario.neverRefresh = true` with `MCP error -32602: Invalid arguments for tool hoi4.gui_render: Unrecognized key: "neverRefresh" at scenario`. The exposed render schema has no top-level equivalent; all successful calls used `generatedScenarios: {enabled: false}`.

The render route returned a validation JSON link with SHA-256 `d92ed051f7e5f2fbfc0716e26eb88dec08860028da2e3b0ef815bfe1bfc8df9c` and size 7590 bytes, but that file is absent from the parent-supplied local artifact cache path. The MCP resource retry did not complete because a later same-scenario render timed out after 600 seconds; the validation JSON is not archived.

The initial validation-artifact read used an incomplete copied provenance component and failed URI validation; it is not treated as MCP evidence. The subsequent direct-cache check found no file for the declared validation hash.

## Before/after behavior and file disposition

Before this pass, the panel already mapped local or shared cure progress to the bottle sprite and displayed source-defined progress, research mode, activation timing, and explanatory text through live localisation.

After this pass, the owned cure window and gameplay behavior are unchanged. No edit was applied because the production render could not provide the source-derived dynamic text needed to review a reference-matched repair, and the baseline geometry showed no independent layout defect.

The exact pre-change block is archived at `docs/plans/002_zombie_outbreak_plans/cure_gui_evidence/before_zzz_cure_progress_container_0F99E4C1.gui-block.txt`, 792 bytes, SHA-256 `0F99E4C183D2C495F76E81CAAF572C75BCDD9DB6B78FF03E4243E24932AAA733`.

At capture, `interface/chaosx_decisions.gui` had SHA-256 `620D8D7D94E14D0E44208D3E342EEAE5A5892D6BDC6763079DBBBA6FA232BD31`. Parallel GUI workers later changed other blocks in that shared file; its current SHA-256 is `92C3C5855C0C8F8ABAEA31C81557F6A81F57F6C6440F4AC5329B1B97A538D828`, while the owned cure block remains byte-identical with the same 792-byte block SHA-256. An initial source read included the whole interface file, but no other block was audited or changed by this worker; all later source extraction was restricted to the owned cure block.

`localisation/english/chaosx_decisions_l_english.yml` also changed in the shared tree during this task from SHA-256 `0D3D39DB3648CB1F994335FEB5A7120DECAA5C6DF02A65246369D005DD2D993D` to `7616669C05CC2A989C6C222CBA95ACA7C5BFED1EEA92DE468592B4A9F681D92B`; the cure keys listed above were reread and remain as shown. This worker changed none of the source files under `interface/`, `common/scripted_guis/`, or `localisation/`.

The additions from this worker are this handoff and the MCP/source evidence files under `cure_gui_evidence/`.

## Remaining blockers and parent follow-up

This handoff is not a visual completion claim. The event-owned window still needs a resolved scripted-localisation fixture and successful local 0%, partial, full, and applicable visibility renders over matching source revisions before a release repair can be accepted.

The parent owns any localization edits, gameplay/cost/AI changes, shared GUI integration, final source review, and decision on whether to reopen this layout task after a resolved fixture is available. The user owns live-game validation.

No gameplay simplification or fallback was applied. No commit was created.

Skills used: `chaos-redux-scripted-gui`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-event-assets`. The decision/missions skill was not applied because this window has no gameplay controls, costs, AI behavior, or cleanup logic. No skills were created or updated.
