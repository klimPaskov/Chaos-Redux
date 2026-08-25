# Event 016 Kruger Directorate scripted-GUI audit — 2026-08-25

## Scope and ownership

This audit covers only Event 016, `brilliant_scientist`, and its event-owned decision-category attachment. The decision category `brilliant_scientist_directorate_category` declares `scripted_gui = brilliant_scientist_directorate_scripted_gui` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`. That scripted GUI resolves `window_name = "kruger_directorate_container"` in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`. The feature label supplied to the worker, `brilliant_scientist_directorate_gui`, is the localisation prefix rather than a literal GUI window identifier.

The accepted Event 016 specification in `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_2_host_directorate_and_decisions.md` requires the Directorate display to show Mandate, Dependence, Exposure, and Project Capacity while keeping Independent Capacity and Grievance hidden. It also leaves ordinary decisions as the gameplay action surface. The current compact implementation matches that boundary. No shared event-log, event-details, settings, options, super-event, registry, or unrelated GUI file was inspected or changed as part of this audit.

## Exact owned identifiers and files

- Decision entry: `brilliant_scientist_directorate_category`.
- Scripted GUI: `brilliant_scientist_directorate_scripted_gui`.
- Root window: `kruger_directorate_container`.
- Child states: `kruger_directorate_compact_panel` and `kruger_directorate_full_panel`.
- Presentation controls: `kruger_directorate_open_button` and `kruger_directorate_close_button`.
- Layout: `interface/016_brilliant_scientist_directorate.gui`.
- Presentation/state wiring: `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
- Sprite registration: `interface/016_brilliant_scientist_directorate.gfx`.
- Dynamic sprite and text routing: `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`.
- English GUI localisation: `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.
- Active background assets: `directorate_background.dds` and `directorate_compact_header.dds` under `gfx/interface/016_brilliant_scientist/directorate/`.
- Active frame and controls: `profile_frame_human.dds`, `profile_frame_secured.dds`, `profile_frame_sovereign.dds`, `directorate_open_control.dds`, and `directorate_close_control.dds` in the same folder.
- Active meter families: `meter_mandate_*`, `meter_dependence_*`, `meter_exposure_*`, and `meter_capacity_*`.
- Portrait routing: `GetBrilliantScientistDirectoratePortraitSprite`, with the stage and route portrait sprites already registered outside this bounded layout file.

## References reviewed

The required offline wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding. Relevant installed documentation entries for `check_variable`, `custom_override_tooltip`, `custom_trigger_tooltip`, variable effects, and country-flag effects were also consulted.

The exact vanilla precedent was the Soviet paranoia decision-category surface:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/sov_paranoia_system_scripted_gui.gui`.

The precedent supports a compact decision-category status surface with state-driven icon and text routing while ordinary decisions remain outside the presentation panel.

## Pre-change MCP evidence

The first query used the supplied feature label as a window selector. Because `brilliant_scientist_directorate_gui` is not the literal window name, it produced workspace-wide index output rather than a bounded Event 016 surface:

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52e6f9000fe315046c4f84b0419bd7e3e89a954418202d77a09df4e0a6c50688/ac8f7afce129f01675e72e12511c05f2c6d060a3e6d5a11cc43c65873397882d/gui-inspect.c09c2d8b80d875.json`.
- The response reported `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`, and more than 1,500 `INDEX_SYMBOL_COLLISION` records dominated by unrelated Event 003 and Event 005 content.
- Those collisions are workspace-wide legacy/index conditions. They are not evidence of a direct Event 016 overlap, alignment, sprite, or state defect.

The selector was corrected to the literal Event 016 root window:

- Scenario: `event016_directorate_prechange`.
- Window: `kruger_directorate_container`.
- Inspect result: `GUI_INSPECTED`, status `ok`.
- Exact inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cd13fe122ca8635eda9ce2568f2dfaaf5b5bbf6b067262060770da5db36efe5/1fe5f055a10599e1ee4c76668038dba4dd3e9dda72605a25a270a8c41c457e22/gui-inspect.336e954a2b3ac806.json`.

The exact window was then rendered across both requested resolutions and the supported generic states:

- Resolutions: 1280x720 at UI scale 1 and 1920x1080 at UI scale 1.
- States requested: normal, hover, selected, active, disabled, warning, completed, empty-list, full-list, and long-text.
- Related collapsed scenario: `event016_directorate_collapsed`.
- Render result: `GUI_RENDERED`, status `ok`, no route blocker.
- Full-window artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/d2862e8334f7f388a64ec23030bae136b8b80a91c8e04e0a69db72c2a2d81d60/kruger_directorate_container-full.svg`.
- The MCP response warned `MCP_RESPONSE_TRUNCATED`; its packaged SVG is 727,134 bytes. The route did not expose a smaller crop or per-state artifact in the returned envelope.

A bounded single-resolution, normal-state retry was started to obtain a directly reviewable smaller artifact. It did not return after approximately 90 seconds and was terminated at the parent’s instruction. Exact retry selector: window `kruger_directorate_container`, scenario `event016_directorate_prechange_normal`, resolution 1280x720 at UI scale 1, state `normal`.

## Direct layout audit

### Hierarchy and background coverage

The root is a clipped 500x360 container. Its two state panels share the same origin:

- Collapsed panel: 500x58, completely covered by the registered 500x58 `directorate_compact_header.dds`.
- Expanded panel: 500x360, completely covered by the registered 500x360 `directorate_background.dds`.
- Open and close controls use 144x36 four-frame sheets, producing 36x36 button frames. Their x=422 positions keep their click regions inside the 500-pixel root with 42 pixels of right margin.
- The active portrait frame is 168x218 and is displayed at scale 0.68, matching the approximately 114x148 portrait area at x=38/y=80.

The compact and expanded painted children are each directly gated in scripted-GUI triggers. This is deliberate because decision-category consumers do not reliably honor only the visibility of a nested container. The state wiring is verbose but internally consistent and does not expose both painted panels simultaneously.

### Alignment, symmetry, overlap, and text bounds

- The expanded title occupies x=40..400 and is centered, with the close control anchored separately at x=422.
- The four meter rows use a consistent 44-pixel rhythm: y=82, 126, 170, and 214. Their values use the same +7-pixel baseline offset and identical 154x22 bounds.
- The portrait/name column and meter/value column do not overlap.
- The role/control line uses x=36, width 428, y=272, height 30. The footer uses the same horizontal bounds at y=326, height 20. Both remain inside the 360-pixel root, and the 24-pixel vertical gap between the role/control box and footer is intentional negative space.
- Current English title, profile name, four value labels, role/control string, and footer are concise. The long-text MCP request was included, but the packaged response could not be reviewed as an individual long-text crop before the retry timeout. Therefore localisation-expansion safety is source-supported but not claimed as visually proven.

No direct source-level overlap, misalignment, asymmetric row, out-of-bounds click region, missing active background, or unregistered active asset was found.

## Information and interaction budgets

- Visible mechanic values: four. Mandate is cyan, Dependence amber, Exposure red, and Project Capacity green. This is the accepted hard ceiling; hidden Independent Capacity and Grievance remain absent.
- Supporting state: one summarized government-control label combined with Kruger's current institutional role. It does not print hidden arithmetic.
- Gameplay-changing controls: zero. Directorate decisions below the attachment remain the action surface.
- Presentation controls: two mutually exclusive controls, open and close; only one is visible in a given collapsed/expanded state.
- Spendable cost types: zero in this window.
- Texticon coverage: not applicable because the window displays no spendable costs. It does not use literal resource-name fallbacks.
- Active missions or target controls: zero in this window.

## Tooltip and text-density audit

Each visible meter tooltip consists of two short lines: the first identifies what the value measures and names the systems that change it; the second states why a higher value matters. The government-control tooltip explains the summary and points the player to the decisions immediately below. Open and close tooltips describe their presentation-only result. No tooltip mixes spendable costs and non-consumed requirements, and no raw scripted trigger block is presented to the player.

The unused localisation and dormant sprite registrations left from the earlier dashboard design are outside this narrow layout correction. They do not paint or create click regions in `kruger_directorate_container`; removing them would be cleanup beyond the accepted small-patch scope.

## State matrix

| State | Expected visible surface | Interactive region | Audit result |
| --- | --- | --- | --- |
| Expanded/default | Full background, title, portrait/frame/name, four meter rows, role/control, footer, close control | 36x36 close control | Source wiring consistent; MCP full render produced |
| Collapsed | Compact background/title and open control | 36x36 open control | Source wiring consistent; related collapsed scenario requested |
| Hover/pressed/disabled | Four-frame open or close sheet state | Same 36x36 control region | Registered with `buttonstate.lua`; generic states requested |
| Selected/active/warning/completed | No additional gameplay control or card state belongs to this compact surface | No added click region | Generic variants requested; compact surface intentionally unchanged except dynamic text/sprites |
| Empty/full list | No list exists in this compact surface | None | Generic variants requested; not semantically applicable |
| Long text | Same fixed-size text boxes | Close/open control unchanged | Requested, but individual crop could not be recovered before bounded MCP timeout |

## Changes and rewrite decision

No gameplay or GUI source file was changed. The audit found no direct defect that justified a speculative geometry or localisation rewrite. In particular, changing the role/control line to an unreviewed two-line treatment would alter the accepted painted status strip without a reviewable long-text crop.

Because there was no proposed in-scope source change, `hoi4.gui_rewrite` was not called. The requirement to use `gui_rewrite` applies before an in-scope layout change; no such change was accepted here. The only new file is this handoff.

There is consequently no distinct post-change render. The pre-change artifact is also the unchanged-source after-state reference. This is not presented as a before/after comparison pass.

## Blockers, unresolved evidence, and simplifications

- Mandatory post-change comparison evidence is not applicable because no source patch was made.
- Individual annotated, hierarchy, click-region, per-state, and long-text images could not be extracted from the large packaged SVG response. The exact full-window render exists at the artifact URI above, but the response was truncated and the smaller bounded retry timed out.
- The first selector mismatch surfaced workspace-wide legacy collisions and graph truncation. Those conditions are recorded separately and were not attributed to Event 016.
- Live runtime and in-game validation remain parent/user-owned. This handoff does not claim in-game completion.
- No fallback UI, placeholder art, fake button, guessed click region, gameplay simplification, or balance change was introduced.

The Event 016 window is source-audited and has successful exact-window inspect/render route evidence, but full visual completion is unresolved because the returned render package could not be decomposed into reviewable comparison/state artifacts within the bounded MCP retry window.
