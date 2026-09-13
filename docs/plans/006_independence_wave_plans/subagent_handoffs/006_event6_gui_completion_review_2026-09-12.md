# Event 006 Statehood Ledger completion review

Date: 2026-09-12.
Disposition: **blocked visual review; no source edit; no GUI completion claim**.
Event: `006_independence_wave`.

## Scope, authority, and preservation

The parent assigned only `independence_wave_status_window` in `interface/006_independence_wave.gui`, its Event 006 GFX registrations, and `common/scripted_guis/006_independence_wave_scripted_gui.txt`.
The controller names `independence_wave_status_scripted_gui`, uses `context_type = decision_category`, binds this exact window, and gates visibility with `is_independence_wave_active_country`.
The GUI and controller headers explicitly identify the Event 006 Statehood Ledger and reserve gameplay actions to normal decisions and missions.
This is an event-owned surface, not the shared Event Log, details, settings, or super-event framework.

The parent's supplemental authority names specification parts 6 and 7, `006_source_of_truth_map.md`, and the warning-placement, mission-overlap, and 2026-09-05 scale-retry handoffs.
The parent explicitly requires preserving legitimacy, recognition, capacity, security, instability, all five tabs, animation/static siblings, and no-pre-event visibility.
Those requirements were preserved without modification.
The parent's five-value acceptance is recorded, but this worker's governing four-value completion ceiling remains a certification conflict; it is not permission to remove accepted Event 006 content.

Only this handoff was authored.
No GUI, scripted GUI, GFX, localisation, DDS, gameplay, cost, admission, AI, or shared-interface file was changed.
No staging, commit, live-game operation, fallback, or simplification was performed.

## Current source evidence and native mapping

The GUI SHA-256 is `d8b2a3dde2e33b6643664eb4560243647a9069da3ba58987c33bd284f52e677f`.
The GUI/controller diff against the checkout was empty when checked.
The current inspected shared revision is `c0132d675f23f06423c8df3baff38e0e6073bf364ae0062076f2e6a36f5d4bf4`; it must not be conflated with the earlier `4df34107e11d2a71...` receipt.

| Region | Native mapping | Review status |
| --- | --- | --- |
| Background | `GFX_independence_wave_status_panel`, 700 × 500 | Source retained; image unavailable. |
| Founding values | Five `independence_wave_status_*` text/icon pairs at x74/x24, y92–292 | All five retained; rendered density not certified. |
| Mission | `independence_wave_status_mission`, x366/y410, 220 × 40, `hoi_16mbs` | Logical bottom is y450. |
| Tab detail | Five `independence_wave_status_{government,recognition,security,league,ambitions}_panel` texts at x280/y444, 386 × 42 | Six-pixel logical intersection with mission remains a risk, not newly observed glyph collision. |
| Warning | `independence_wave_status_instability_warning`, x318/y384, scale 0.75 | Prior repair preserved. |
| Navigation | Five tab buttons plus Animate and Refresh | Source handlers retained; effective hitboxes and label centering not visually certified. |
| Status art | Recognition, dependency, league-charter, formable-seal static/state/animated families | Source siblings retained; playback blocked. |

Each tab handler sets its own flag and clears the other four.
Government is the default detail when no other tab flag is selected.
The animation flag `independence_wave_status_gui_show_animation` switches visibility between four state-strip and animated sibling pairs.
The four static-state frame properties use `ROOT.independence_wave_gui_{recognition,dependency,league,formable}_frame`.
These are source observations, not proof of executed click behavior, tab isolation, pre-event visibility, or cleanup.

The linked localisation file is `localisation/english/006_independence_wave_gui_l_english.yml`, with `independence_wave_status_gui_*` display keys.
The mission substitution is `[This.GetIndependenceWaveMissionStatus]`; real long cases include “A formable congress or charter is in progress.” and “No timed commitment is currently active.”
No concrete rendered substitution was available in this pass, so mission-height or detail-position changes would be speculative.

The owning GFX family is registered in `interface/006_independence_wave.gfx`, including `GFX_independence_wave_{recognition_seal,dependency_warning,league_charter_activation,formable_eligibility_seal}_{states,animated,static}`.
Animated sheets use 5, 3, 4, and 4 frames respectively, 5 FPS, looping, and `play_on_show`.
The parent also named `interface/006_independence_wave_small_assets.gfx` and `interface/006_independence_wave_iw093_iw098_focus.gfx`; neither was edited.
No new asset or asset-production handoff was required or created.

## Fresh MCP inspection

The first inspect request was rejected because `scenario.id` was absent and `uiScale` was placed inside `scenario.resolution`.
The corrected request was:

```json
{"windowName":"independence_wave_status_window","scenario":{"id":"event6_completion_review_20260912","resolution":{"width":1920,"height":1080},"uiScale":1}}
```

It returned `GUI_INSPECTED`, 48 selected-window elements, and `validation.passed = true`.
Generated scenarios were not disabled on this exploratory inspection, and the returned scenario identity is `event6_completion_review_20260912-generated-1`; it is not an exact deterministic regression fixture.
Fidelity counts were 557 modelled, five approximated, 15 ignored, zero missing, four unsupported, and zero unresolved in that generated fixture.
The generated zero-unresolved count does not establish real runtime dynamic-text execution.
The response also records 63 nonblocking overlap findings; passing validation does not waive them.

Inspection artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d659dc456d892edce626ea54a54cf6c424beeff5fa1595b35823b15033a9f935/14b6c2859056bb59e584d70489b05c0605bef12b57ca93fa74501060f97225e4/gui-inspect.c0132d675f23f064.json`.

Four `GUI_ANIMATION_STATIC_FALLBACK_MISSING` warnings name the recognition seal, dependency warning, league charter activation, and formable eligibility animated sprites.
The source has separate static registrations; no unsupported fallback field was invented.
`GUI_SPRITE_RENDER_PARTIAL` explicitly states: `Effect gfx/FX/buttonstate_blendframes.lua is retained in the source graph but is not executed by the offline renderer.`
That is the exact animation-execution blocker, not permission to certify playback or to replace the animation.

## Reference retrieval and deterministic render blockers

The selected reference was the parent's post-warning cropped production image, as permitted in the supplemental assignment:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9f30eb962758ee93d79dbcb9aca2e75eacdce13392f2540cfd9f4f8319365c/c5f147265017bd9309b074a83c303200ce1fb5a7a89778c0b7358bb21ea927cb/independence_wave_status_window-cropped.png`.

`read_mcp_resource` on server `hoi4_agent_tools` for this exact URI failed with MCP `-32603`: `Artifact provenance manifest is unavailable`.
The reference image was not available for actual visual review in this pass.

The fresh deterministic render request was:

```json
{"windowName":"independence_wave_status_window","scenario":{"id":"event6_completion_review_explicit_20260912","uiScale":1},"generatedScenarios":{"enabled":false},"states":["normal","long-text","missing-localisation"],"resolutions":[{"width":1920,"height":1080,"uiScale":1},{"width":1366,"height":768,"uiScale":1}]}
```

It failed with `tool call failed for hoi4_agent_tools/hoi4.gui_render`, caused by `timed out awaiting tools/call after 180s`.
No render artifact or emitted resolution/state matrix was returned to this worker.
Thus neither requested resolution, long-text/missing-data behavior, full/cropped/annotated view, hierarchy, click-region image, nor comparison can be claimed visually reviewed.
No source edit occurred, so there is no after-source revision or repair comparison.
Older artifact identities remain historical receipts only and were not substituted for the failed fresh render.

## Reading and remaining acceptance work

`AGENTS.md` and the complete current `chaos-redux-scripted-gui/SKILL.md` were read, and the core offline wiki pages were consulted alongside Interface and Scripted GUI context/visibility guidance.
Installed `common/scripted_guis/_documentation.md` and `interface/sov_paranoia_system_scripted_gui.gui` were read as native context and text-box precedents.
The three parent-named dated GUI handoffs and exact GUI/controller sources were read.
The worker-required `chaos-redux-scripted-gui/references/visual-review.md` path is absent; the current main skill embeds its visual checklist inline.
Bulk reads of the additional required skills, broad specifications/source-of-truth map, and ancillary GFX sources were truncated; exhaustive required reading is not claimed complete and must precede any implementation continuation.

The visual checklist remains unresolved for reference fidelity, painted/logical/glyph bounds, two-axis label centering, background clearance, spacing, z-order, scale, clipping, text density, tab-specific visibility, and effective click regions.
The source contains five founding values plus host/patron/network context; no reduced-value design was introduced.
The seven buttons are five navigation controls and two utility controls, not seven spendable gameplay actions.
No displayed spendable cost string exists on these controls; cost-count/texticon payment review and substantive decisions remain with the decision owner.
No gameplay-action integrity or balance claim follows from this UI pass.

Normal, long-text, and missing-localisation rendering was attempted but blocked.
Hover, selected, active, disabled, warning, completed, empty/crowded, coherent per-tab fixtures, no-pre-event hidden state, animation playback, static return, and matching resolution/click-region evidence remain unverified in this pass.
Parent integration and the existing user-owned live-consumer evidence remain pending.
The six-pixel logical mission/detail overlap remains unresolved because no source-safe repair was proven by reviewed production imagery.
ASSET-039 and whole-event GUI completion are not closed by this handoff.
