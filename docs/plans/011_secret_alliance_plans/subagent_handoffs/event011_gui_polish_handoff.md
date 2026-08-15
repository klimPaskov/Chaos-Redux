# Event 011 Secret Alliance GUI polish handoff

## Ownership and scope

This handoff covers only the dedicated Event 011 counter-network scripted GUI, `secret_alliance_counter_network_scripted_gui`, attached to the vanilla `decision_category` context and rendered in `secret_alliance_counter_network_container`.

Event ownership is proven by `common/decisions/categories/011_secret_alliance_categories.txt`: both `secret_alliance_foreign_interference` and `secret_alliance_coalition_crisis` point to the exact scripted GUI, and no shared Event Log, Event Details, settings, super-event, or unrelated GUI was edited.

The decision entry points remain `secret_alliance_response_category_visible = yes` and `secret_alliance_coalition_crisis_visible = yes`; gameplay costs, effects, AI, hidden-member logic, event mechanics, and scripted-GUI effects/triggers were not changed.

## Exact identifiers and assets

- GUI window: `secret_alliance_counter_network_container`.
- Scripted GUI: `secret_alliance_counter_network_scripted_gui`.
- Context: `decision_category`.
- Decision categories: `secret_alliance_foreign_interference`, `secret_alliance_coalition_crisis`.
- Event-owned GUI source: `interface/011_secret_alliance.gui`.
- Event-owned scripted-GUI wiring: `common/scripted_guis/011_secret_alliance_scripted_gui.txt` (verified unchanged in this pass).
- Category registration: `common/decisions/categories/011_secret_alliance_categories.txt`.
- Event-owned GFX registration: `interface/011_secret_alliance.gfx` (reused unchanged).
- Background sprite: `GFX_011_secret_alliance_counter_network_panel` from `gfx/interface/011_secret_alliance/counter_network_panel.dds`.
- Meter sprites: `GFX_011_secret_alliance_evidence_meter_frame`, `GFX_011_secret_alliance_evidence_meter_fill`, `GFX_011_secret_alliance_preparedness_meter_frame`, and `GFX_011_secret_alliance_preparedness_meter_fill`.
- Suspect sprite: `GFX_011_secret_alliance_suspect_card_states` with four frames from `suspect_card_states.dds`.
- Warning sprites: `GFX_011_secret_alliance_coalition_closure_warning` and `GFX_011_secret_alliance_coalition_closure_warning_animated`, preserving the existing static fallback and eight-frame animation.
- Status sprites: `GFX_011_secret_alliance_status_recent_operation`, `GFX_011_secret_alliance_status_turned_channel`, `GFX_011_secret_alliance_status_false_lead`, and `GFX_011_secret_alliance_status_war_pressure`.
- GUI localisation keys are the existing `secret_alliance_gui_*` keys in `localisation/english/011_secret_alliance_l_english.yml`; the parent shortened the meter and recent-operation strings while preserving concurrent Event 011 prose edits.

## Files changed in the current bounded pass

- `interface/011_secret_alliance.gui`: compact 500x250 category-bound layout, 0.695 background/art scale, 178x17 meter clips, three 128x67 suspect cards at x=13/174/335 and y=71, compact status/objective row, warning band, in-bounds Motion button, and valid vanilla font identifiers (`hoi_16mbs` and `hoi_18b`) replacing unsupported `hoi_14mbs` and `hoi_16b` references.
- `common/decisions/categories/011_secret_alliance_categories.txt`: removed `picture = GFX_011_secret_alliance_counter_network_panel` from both event-owned category blocks so the panel is painted once by the attached scripted GUI instead of once by the category description and again by the GUI.
- `localisation/english/011_secret_alliance_l_english.yml`: contains concurrent parent prose work and parent-owned GUI-key shortening; no unrelated line was reverted or overwritten by this handoff.
- `common/script_constants/011_secret_alliance_constants.txt`: currently contains the parent’s GUI meter presentation constants (`gui_meter_width`, `gui_meter_scale`, `gui_meter_min`, and `gui_meter_max`); no non-GUI balance constant was changed in this pass.
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/event011_gui_polish_handoff.md`: this handoff.

`common/scripted_guis/011_secret_alliance_scripted_gui.txt` and `interface/011_secret_alliance.gfx` were inspected and left unchanged. No gameplay source, shared framework, or unrelated interface was edited.

## Layout and value/action budget

The attached surface now uses a 500x250 outer clip matching the vanilla decision-category width evidence rather than a standalone 720x360 window. The 720x360 background art is scaled to the category surface, the header gives the phase title and selected lead one top row, the evidence and preparedness meters have equal 178px visual weight, and all three suspect selectors remain visible in a single compact row.

The visible value budget is one primary counter-network phase/status title, two supporting meters, the selected lead, and supporting operation/objective/war-pressure readouts. The action budget remains three suspect selectors, one clear-selection action, and the existing Evolution III Motion toggle; no fake controls or gameplay actions were added.

The lower row keeps recent operation and scrollable active objectives aligned, while the Evolution III warning/static-fallback pair and War Pressure occupy a compact lower band. The existing scripted-GUI visibility and click-enabled bindings continue to control empty, selected, locked, disabled, animated, static, and revealed states.

## Before and after behavior

Before the patch, both decision categories painted `GFX_011_secret_alliance_counter_network_panel` through `picture`, while the scripted GUI painted the same panel again, producing the empty duplicate panel visible in the attached screenshot. The scripted GUI was 720x360, so the third suspect, selected-lead text, preparedness text, and right edge were clipped by the native category viewport.

After the bounded layout pass, the category picture path is removed, the dedicated GUI owns the single panel presentation, the outer surface is 500x250, the three selector regions stay inside the 500px width, the status/objective surfaces are moved above the warning band, and the full Motion button is bounded to the lower-right region. The valid-font correction removed MCP approximation entries for `hoi_14mbs` and `hoi_16b` without changing any gameplay or localisation semantics.

## MCP evidence

Pre-change exact-window inspection succeeded with the linked-category selector and returned a complete 31-element graph. The parent’s fresh pre-change artifact was:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcfc806890a5c638a95131507620449996ebdaa0adcfe65712d8facafdfefe50/16a7b6df3b3e66ebdbf472800ddf910d9d5f2b8d7fd316f16941886ca8b1035a/gui-inspect.7bbeefa26f37d7634482c39dc84abec69ca7590cfed66bb719edfca6ad8636f3.json`

The earlier pre-change full render artifact was:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbc55ab5c7f9075acaf2bb1f8ad9725c92fe0e4cbd54d0f4f9fb2f5a0606997f/cabb25358b914e217344e7bec189744aa9ccc21563ce2f033a6a80bd514984bf/secret_alliance_counter_network_container-full.svg`

The parent’s post-change inspection before the final font correction was:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/017bd71bd916422e76dd54fa1120b55509ee9459c6ba1900a5bff5c09116a411/31c6d26cd106ca4bd05fcdddbb9604d39cc1f05dea8e79a1d00d3befb38e1c8f/gui-inspect.3f0af103b3d9cb3f0a1c3ab1b001a64cf38765c8d969f41dfe6b91c482b150f8.json`

The final post-font-change inspection succeeded with `GUI_INSPECTED`, `complete = true`, 31 Event 011 elements, shared revision `aaa292f1f19dfc6ece6fca176f54d42e48790edf2348e0fc3342164149a27952`, and fidelity counts of 263 modelled, 3 approximated, 40 ignored, 2 missing, 14 unsupported, and 12 unresolved. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e309ac2d37b490c40f4e7c357a145fdfbdba818ee8d222518ac82888f9f6772a/026a9c30c418a6a4ab8c49db2b62598ac8ae627d6b4d6feee7a0439a3c6a9625/gui-inspect.aaa292f1f19dfc6e.json`

The final post-font-change render request succeeded with `GUI_RENDERED` for the requested state set and 1280x720, 1366x768, 1600x900, and 1920x1080 at UI scale 1.0. Its full-window artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4ee852ce09f603330f3cac65504ba9019e9aef444acf1d0d83eb3dec045b88a/38b60ab80b328e1eb7373961c6ae30d5cd510f52a184e8d59d26172f90daef4f/secret_alliance_counter_network_container-full.svg`

The linked render manifest records source revision `aaa292f1f19dfc6ece6fca176f54d42e48790edf2348e0fc3342164149a27952` and the offline renderer’s 263 modelled, 3 approximated, 40 ignored, 2 missing, 14 unsupported, and 12 unresolved fidelity counts.

## State and resolution coverage

The final render request covered `normal`, `hover`, `selected`, `locked`, `disabled`, `warning`, `active`, `completed`, `empty-list`, `full-list`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation` at 1280x720, 1366x768, 1600x900, and 1920x1080.

The source and scripted-GUI audit covers Evolution II concealed/no-suspect, one-suspect, all-three-suspect, selected-lead, unresolved border-conflict lock, Evolution III animated warning, Evolution III static fallback, and revealed Coalition Crisis visibility conditions. The MCP route did not expose a runtime flag/variable scenario injector for those named Event 011 states, so the artifact is a generic offline state render rather than proof of each live flag combination.

The MCP response exposed one full SVG artifact rather than separate crop, hierarchy, annotated, click-region, state-gallery, or per-resolution files and reported `MCP_RESPONSE_TRUNCATED`. The linked inspect graph does expose the 31 target elements and click-region source geometry; parent-owned expanded MCP renders remain required for dedicated hierarchy/click-region/state/resolution comparisons.

## Parent resolution and final validation

The worker's inverse-scale finding was accepted and resolved. HOI4 applies sprite scale to source position and dimensions together, so the parent restored the scaled card, meter-frame, recent-operation, warning, and Motion art to their original 720x360 blueprint anchors. They now resolve once into the compact coordinates beneath the unscaled 500x250 text, clips, and click regions. The meter effect also keeps its 256-pixel source range and 2.56 source scale so the rendered 178-pixel fill can travel from fully hidden to fully shown instead of receiving a second scale reduction.

The corrected inspection completed for all 31 Event 011 elements at shared revision `059f6f9f823cc8936db39ff5c57c9015d5c4f55abab0d87954fd6146f1af472a`. It returned no Event 011-targeted diagnostic. The final expanded render succeeded for 1280x720, 1366x768, 1600x900, 1920x1080, and 2560x1440 at UI scale 1 plus 1920x1080 at UI scale 1.25 across normal, hover, selected, locked, disabled, warning, active, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecf37a9a3db380537812f788a59a475d17efe40c07313f4c3da55372fa37b76a/d1c64f5fe8778b3cc51d18aeb672e3d785cde1a18241353501f8f70f7bbc9a68/secret_alliance_counter_network_container-full.svg`

The duplicate category picture is gone, all card click boxes stay inside the 500x250 surface, and the final SVG places the scaled Motion button at approximately `(401.8,219.8)` with a rendered 86.1x25.2 footprint ending at `(487.9,245)`. `docs/events/011_secret_alliance/overview.md` is reconciled with the compact layout and records the source-versus-visual meter range.

The inspection still reports repository-wide GUI source-graph and aggregate overlap failures from unrelated surfaces, and the generic offline scenario cannot prove every live Event 011 flag combination or every unusually long dynamic country name. No in-engine playtest or live consumer validation is claimed.

## Rewrite blocker and skipped validation

`hoi4.gui_rewrite` was attempted on the exact Event 011 file and window after the inspect/render review. Source-mode calls were rejected by the adapter’s incompatible hash/patch validation, a whole-file patch was rejected with `GUI_UNSAFE_PATCH_RANGE` because complete source replacement is forbidden, and the parent’s bounded whole-source/constants/scalar attempts consistently returned `REWRITE_STRUCTURE_LIMIT`. No rewrite call mutated the repository; the compact source was applied through the normal bounded file-edit workflow.

Dedicated per-state runtime flag injection, per-resolution artifact splitting, hierarchy/click-region crop export, and live Hearts of Iron IV validation were skipped or unavailable through the current MCP route. These remain parent-owned follow-up checks; no claim of in-game completion is made.

No commit was created.
