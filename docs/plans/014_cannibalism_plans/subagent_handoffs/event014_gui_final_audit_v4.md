# Event 014 Cannibalism Scripted GUI Final Audit V4

## Status

This audit covers only the five dedicated scripted GUI windows introduced by Event 014 Cannibalism.

The source audit found no Event 014 layout defect that justified another source edit. The current layout stays inside every painted background, all eleven visible controls have matching scripted GUI click handlers, and the five surfaces stay within the value and action budgets defined by the decisions and missions skill.

Mandatory MCP post-change visual comparison is not complete. All five post-change `hoi4.gui_inspect` calls succeeded, but the post-change `hoi4.gui_render` comparison calls timed out. A parent retry on 2026-08-24 successfully inspected and rendered the Warlord window at 1920 by 1080 in its normal state, closing the missing single-window render gap. The requested four-resolution matrix then returned `ARTIFACT_STORAGE_LIMIT`, so this handoff still does not claim full state-and-resolution visual completion or in-game completion.

No gameplay cost, effect, AI, probability, decision, mission, shared UI, or non-014 file was changed by this audit.

## Event ownership and entry points

Event 014 owns this UI directly.

- Entry event: `chaosx.nr14.1` in `events/014_cannibalism.txt`.
- Early decision-category attachment: `cannibalism_containment_category` and `cannibalism_network_alerts_category` attach `cannibalism_early_header_scripted_gui`.
- Warlord decision-category attachment: `cannibalism_warlord_command_category` attaches `cannibalism_warlord_command_scripted_gui`.
- Revealed decision-category attachment: `cannibalism_unified_command_category` attaches `cannibalism_revealed_command_scripted_gui`.
- Wendigo decision-category attachment: `cannibalism_wendigo_command_category` attaches `cannibalism_wendigo_command_scripted_gui`.
- Network entry point: `cannibalism_network_open_button` opens the Event 014 `player_context` window `cannibalism_network_window` from the early header.

The shared Events Log, Event Details framework, settings UI, super-event framework, shared registries, and every non-014 GUI were excluded.

## Exact identifiers and files

### GUI windows

- `cannibalism_early_header_window`, 470 by 304 pixels.
- `cannibalism_network_window`, 860 by 620 pixels.
- `cannibalism_warlord_command_window`, 470 by 340 pixels.
- `cannibalism_revealed_command_window`, 470 by 380 pixels.
- `cannibalism_wendigo_command_window`, 470 by 400 pixels.

### Scripted GUI identifiers

- `cannibalism_early_header_scripted_gui`.
- `cannibalism_network_scripted_gui`.
- `cannibalism_warlord_command_scripted_gui`.
- `cannibalism_revealed_command_scripted_gui`.
- `cannibalism_wendigo_command_scripted_gui`.

### Owned source files inspected

- `interface/014_cannibalism_frontline_hunger.gui`.
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`.
- `interface/014_cannibalism.gfx`.
- `localisation/english/014_cannibalism_l_english.yml`.
- `common/decisions/categories/014_cannibalism_categories.txt`.
- `events/014_cannibalism.txt`.

### Background sprites

- `GFX_cannibalism_early_category_background`.
- `GFX_cannibalism_network_window_background`.
- `GFX_cannibalism_warlord_command_background`.
- `GFX_cannibalism_revealed_command_background`.
- `GFX_cannibalism_wendigo_command_background`.

The five DDS payloads exist and have dimensions matched by their owning windows. Their file sizes were 571,648 bytes, 2,132,928 bytes, 639,328 bytes, 714,528 bytes, and 752,128 bytes respectively.

### Localisation family

The visible UI uses the `cannibalism.gui.*` family in `localisation/english/014_cannibalism_l_english.yml`. All GUI localisation keys referenced by the five windows are present. No key in that family mentions animation, animated display, animation preferences, or an animation toggle.

## Sources and precedents inspected

- Repository `AGENTS.md`.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, including its complete scripted GUI layout, value-budget, action-budget, background-first, cost, and interactive-design rules.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`.
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`.
- Event 014 asset, animation, and localisation requirements in spec part 10.
- `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md`.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-08-20_decision_category_gui_full_audit.md`.
- Offline `paradox_wiki/Interface Modding - Hearts of Iron 4 Wiki.md`.
- Offline `paradox_wiki/Scripted GUI Modding - Hearts of Iron 4 Wiki.md`.
- Required offline core wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.
- Vanilla `common/scripted_guis/_documentation.md`.
- Vanilla `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`.
- Vanilla `interface/sov_paranoia_system_scripted_gui.gui`.
- Vanilla Soviet decision-category scripted GUI attachment precedent.

## Layout hierarchy and background coverage

| Window | Primary hierarchy | Painted background coverage | Result |
| --- | --- | --- | --- |
| Early | Title, three meter rows, primary-theater card, active-objective text, network-ledger button | Each meter follows its painted horizontal channel. State and objective text occupy the lower information field. The sole control sits in the painted lower-right action anchor. | No audited element leaves the 470 by 304 panel. |
| Network | Title and close control, summary, five filter tabs, sort and refresh controls, country and state lists, selected evidence card | The summary occupies the header field. Toolbar controls follow the painted strip. Two lists align to the two ledger columns. Selection details stay in the painted evidence-card region. | No audited element leaves the 860 by 620 panel. |
| Warlord | Title, Larder, Frenzy, Alignment, feeding-state summary, raised-formation capacity | Three values occupy the main painted meter rows. Feeding-state and capacity text remain in lower information anchors. | No audited element leaves the 470 by 340 panel. |
| Revealed | Title, portrait and seal treatment, Global Larder, Network Reach, integrated-warlord summary, continental target summary, terminal progress | Portrait and seal use the painted medallion region. Values and summaries stay in the corresponding central and lower command fields. | No audited element leaves the 470 by 380 panel. |
| Wendigo | Title, portrait, live and broken anchor card, transformation progress, pack capacity, winter victories, terminal lock | Portrait, anchor pulse, progress frame, capacity, and terminal treatment map to distinct painted regions. | No audited element leaves the 470 by 400 panel. |

Existing annotated background maps were visually reviewed at `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_gui_final_audit_assets/early_layout_annotated.png`, `network_layout_annotated.png`, `warlord_layout_annotated.png`, `revealed_layout_annotated.png`, and `wendigo_layout_annotated.png`. These artifacts were already present in the shared worktree before this audit and were not authored or modified by this worker.

## Value budget, action budget, and cost audit

| Window | Visible mechanic values | Primary actions | Budget result |
| --- | --- | --- | --- |
| Early | Field Hunger, Command Integrity, and conditional Cult Cohesion | One read-only navigation action to open the ledger | Three values and one action pass. |
| Network | Known actors, confirmed nodes, and Network Reach | Five filters plus sort, refresh, and close presentation controls | Three summary values pass. The controls are navigation and presentation controls rather than eight gameplay actions. |
| Warlord | Larder, Frenzy, Alignment, and formation capacity | None | Four values meet the hard ceiling. Feeding-state and consumed-population text form supporting context rather than independent controls. |
| Revealed | Global Larder, Network Reach, integrated warlords, and terminal progress | None | Four values meet the hard ceiling. Controlled-state and consumed-population text remain a single supporting theater summary. |
| Wendigo | Anchor condition, transformation progress, pack capacity, and terminal state | None | Four values meet the hard ceiling. Live and broken anchors are presented together as one causal anchor card. Winter victories are supporting transformation context. |

The dedicated GUI contains no gameplay-changing spend control. All paid actions remain in Event 014 decisions. The GUI cost count is therefore zero and a GUI texticon cost audit is not applicable. No requirement is disguised as a spendable cost in the window.

## Text density and localisation expansion

- Titles and primary labels are concise and occupy one line in their normal English form.
- The longest normal blocks are the two-line network summary, two-line list entries, two-line feeding summaries, and the selected evidence card.
- Tooltips state what each value measures, which related decision surface controls it, or why a blocked state matters.
- No visible label contains an implementation note, fallback note, asset note, or animation instruction.
- Missing-localisation keys were not found in the source key cross-check.
- The MCP long-text and missing-localisation requests did not yield distinct state artifacts. This remains part of the render blocker rather than source-proven visual coverage.

## Click regions and interactive integrity

All eleven button controls declared in the Event 014 GUI have matching `_click` handlers in `common/scripted_guis/014_cannibalism_scripted_gui.txt`.

- Early network button visual bounds at scale 0.86 are approximately x 335 to 440.78 and y 266 to 295.24 inside the 470 by 304 window.
- Network close control bounds are approximately x 720 to 825.78 and y 14 to 43.24 inside the 860 by 620 window.
- Network filter, sort, and refresh controls align on the toolbar at y 88 to 90 after the current shared-worktree alignment edit.
- Network refresh bounds are approximately x 770 to 841.34 inside the window.
- Country and state entry click boxes are 374 by 64 pixels and match their list cards.
- There are no painted button-like controls without an interaction, disabled treatment, or clearly decorative role in the inspected source.

## Automatic animation contract

Animation is cosmetic and automatic.

- Each animated UI family has an Event 014 GFX registration and a static sibling.
- Scripted GUI visibility enables the animated sibling automatically and hides the static sibling.
- Animated definitions use looping playback and `play_on_show` where applicable.
- The GUI defines no animation preference button, animation toggle, animation cost, or animation player choice.
- The `cannibalism.gui.*` localisation family contains no player-facing animation mention.

The MCP renderer approximated animated-frame semantics and reported missing source glyph fallbacks. That renderer limitation does not alter the source contract, but live animation behavior remains parent-owned runtime validation.

## State and resolution matrix

The MCP render request covered `normal`, `hover`, `selected`, `locked`, `disabled`, `warning`, `active`, `completed`, `empty-list`, `full-list`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation` scenarios.

The requested resolutions were 1280 by 720, 1600 by 900, 1920 by 1080, and 2560 by 1440 at UI scale 1.0.

The server produced only one full-window SVG for each successful multi-state call. It did not produce distinct cropped, annotated, hierarchy, click-region, state, or resolution artifacts for the full requested matrix. The source geometry and annotated PNGs support the bounds findings, but they are not a substitute for the missing MCP state and resolution evidence.

## Pre-change MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

### Inspect artifacts

- Early: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e7f0e1f410cc2eab6d10b319911826b91350a335915c6065ab48653fcb8e565/1a0be1eedf446ad64f3819a7001fed1887d174ad288d8c39b6f37aeda6acd5a7/gui-inspect.8f34a9ce73b8d56e.json`.
- Network: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3204d3cc70e4c2bb1a7c43120ea2852cb20b03efc112b453f255e3c3ae902a86/c8b61f073708e64df374c55a0d0ef8e1bdcc3a181b4e490c58b9f3c8c575ff09/gui-inspect.7f950ec5cdad3872.json`.
- Warlord: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a90e72162734eafe7a261ddb80538ab73b6e0e38826619b5d12a0d2765727b6/555304979bcea2213b0ebe62d742b4d7644cca0c4d308f012e44912cf13fadb6/gui-inspect.baa33ec84ebc231a.json`.
- Revealed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a47aec58f5e5cd31db70b51e0524c2ce90a9c64efa10e62a7d150e7030424558/73c784051dbcb7d7d99edb4c3be967ab1caa397db095e71c629f9b5c04748c34/gui-inspect.a7079c5598117f91.json`.
- Wendigo: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/405834936e7561b1bd952bb536120395baea7f91b5d1761471c528018f427510/d5a8d3699affbc80afed0ad539eef5b39705e70f58cf266b370a345f106cdae5/gui-inspect.5b1b73344741d070.json`.

The element counts were 17, 27, 17, 17, and 17. Event 014 selector filtering found no Event 014-specific visible-overlap, clipping, context, spacing, or alignment diagnostic. The workspace-wide graph did report unrelated Event 003 and Event 005 symbol collisions and graph truncation.

### Render artifacts

- Early full SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/adec1d803e99ab49ecbee29f74f0268658d5b63fa7a5921be4f8da974d88d826/d862a3241106d8be28ce9cba704791dcb767b08d7ad01f3190dc962d7bac1fba/cannibalism_early_header_window-full.svg`.
- Network full SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0583bafca6d3c2b2b428f5660917aaa421b493fd0e375a8f82465af86b748d0/e48639254e14c53e16ea15a7a5555465d2d9432e5cb8b10fc4c66ace379466d8/cannibalism_network_window-full.svg`.
- Revealed full SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c26360404c9cbefabffdc40760683904f83e6a0c824d8b2573c19b572176615/5244aff159524fac6ae57ae00dac9f42b47b0bd69855965462161a3e51323b0a/cannibalism_revealed_command_window-full.svg`.
- Wendigo full SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f42ed1c98dea41b4de72a1824f77675e196afeabc744bbe2eba832f01b2cf506/35ea23c1dfdbc0e4685a5361c42b07fe9b750e5236d2867f52dd22f74c0055d3/cannibalism_wendigo_command_window-full.svg`.

The original Warlord full render returned `INTERNAL_ERROR`, then returned `ARTIFACT_STORAGE_LIMIT` on retry. A later exact-selector retry with scenario `{ id = event014_warlord_current_layout_recheck_2026_08_24 }`, state `normal`, and resolution 1920 by 1080 returned `GUI_INSPECTED` with one artifact and `GUI_RENDERED` with one artifact. The immediately following normal-state request for 1280 by 720, 1600 by 900, 1920 by 1080, and 2560 by 1440 returned `ARTIFACT_STORAGE_LIMIT` with zero artifacts. Some successful artifact URIs were reclaimed quickly and later resource reads reported that the provenance manifest was unavailable.

## Rewrite review and before-after comparison

The required `hoi4.gui_rewrite` call used source mode on `interface/014_cannibalism_frontline_hunger.gui`, exact selector `cannibalism_network_window`, and scenario `event014_final_audit_v4_current_layout_review`.

The rewrite returned `GUI_CHANGES_BLOCKED` because the workspace-wide graph contains unrelated Event 003 and Event 005 symbol collisions and graph truncation. It changed no file. Its proposed source diff added only a final newline.

- Before PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f3965842061290b7ef8da3d4ed164235e718d794ba05c5ea88a8f70a883762e/699a1d05c46eb55736e55d319972bdfb2041431d35036ab5a3689a64c6762eee/cannibalism_network_window-before.png`.
- Proposed PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f3965842061290b7ef8da3d4ed164235e718d794ba05c5ea88a8f70a883762e/fc553cf9a9cf3ee11de8fd381603c5fa8af11e1e864f9b43fca66b2e5a965245/cannibalism_network_window-proposed.png`.
- Visual diff PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca46559e00bc7b20b6e5a5ffbf3a6c89c9d662f7afa1371f5c78bc12d6a12c2a/215225a15c310a7a6278d3251a2ed2fe215eff5f6c886f9837df6a08e07bfc06/cannibalism_network_window-visual-diff.png`.
- Visual diff JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/2c37e4e5782370adc2d0c2846346f9d876ce4b7c1c9b23ad99b553c2f781cbac/cannibalism_network_window-visual-diff.json`.
- Proposed fidelity report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d483061d7eac3c734e894461a418c5f9581b670db6169c5a9b7993b43867753/7b892986dee328018bd89525af930de6f4b6d78b1986533dbc86e2abb3f475ae/cannibalism_network_window-proposed-fidelity.json`.
- Rewrite validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/737a8a1735662b98f32348e164614d8be87792a2444cf62251fac057d234c734/4f1293fca7843b56d902dc8ce7cb31eeae4c029d4a4e8124d18d1c23c6b6dc7e/cannibalism_network_window-rewrite-validation.json`.
- Source diff: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6909d8b5f3f9ce3579f018f59b0f5af96fad3c0f71c83e0f5ab18477cb03321/dd374915ffd602bb1f3be75f2650bf9970defe6c11068b0b63ad1fc68318302d/014_cannibalism_frontline_hunger.gui.diff`.

The visual diff reported `changedPixels: 0` and `changedRatio: 0`. No layout patch was applied because the inspected current source and proposed source were visually identical.

## Post-change MCP inspect evidence

- Early: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08945af4664acdcd4f472b24f4079de70b7fd0d0f10d739f25962cf0b6ffb21a/9380c599e7070b01ecb1e978e844f3151346e48c840c8909485c04493835d72a/gui-inspect.efcc30d8957daab7.json`.
- Network: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/338663721720fc06eb56d6fc53874049897ced5438ebb8b0c72cff7b60088592/09008dfb9cf897573387ffddb2eeca3a31bf1483af71f866e52b74c67e4adc6d/gui-inspect.1cbde0fb94521db9.json`.
- Warlord: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36b15c40448ca90b7d26719653d683c95009ebea20442e92cd15b9cc37509236/8f702db897977f910618da0fb16e04cfee9c4a44d880b564debdabcbfec5ef3a/gui-inspect.e2c89ef80971fc61.json`.
- Revealed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b348cc69cb33aa05d8c43c90dcef988d2ad28acdf868548482e0df739f69406d/0bc3300bd2407d3932dfd776d358644a4ebb5168b324d1da3850d486b1a95c76/gui-inspect.f2c61ea8d7a79ad4.json`.
- Wendigo: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40bb57feeaa7a6f212a73acd97889e268a210df9524920ef56c5db2a23d32e8c/7717c9f189ba80ed9c24465b9ba900189310543130ef0e3896f64af8380a4479/gui-inspect.4002fcc2a0f0c76e.json`.

Post-inspect element counts and fidelity counts match the pre-inspect results for every Event 014 selector.

## Unresolved MCP blockers and simplifications

1. The Warlord exact-selector normal-state render now succeeds at 1920 by 1080, but the four-resolution retry hit `ARTIFACT_STORAGE_LIMIT` and did not produce a matrix.
2. Post-change `hoi4.gui_render` comparison calls for all five exact selectors timed out at 180 seconds. There is no complete post-change state, resolution, hierarchy, click-region, or visual comparison artifact set for the five-window matrix.
3. The rewrite route was blocked by workspace-global Event 003 and Event 005 symbol collisions and graph truncation. Those diagnostics are outside Event 014 ownership and were not patched.
4. Successful multi-state render calls returned one full-window SVG rather than distinct requested views and scenarios.
5. Some MCP artifact provenance manifests became unavailable after artifact reclamation.
6. Source geometry and existing annotated PNGs were used to document bounds and background coverage, but they are not represented as a substitute for the missing MCP post-render matrix.
7. No source patch was made because the exact rewrite comparison showed zero changed pixels and no Event 014-specific source defect was identified.

These limitations mean the mandatory visual completion standard remains unresolved. No simplification was introduced into the Event 014 GUI implementation itself.

## Files changed by this audit

- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_gui_final_audit_v4.md`.

The existing changes in `interface/014_cannibalism_frontline_hunger.gui`, `localisation/english/014_cannibalism_l_english.yml`, and the annotated evidence directory predated this worker's edit and remain owned by their concurrent authors.

## Remaining parent-owned validation

- Retry the exact five-window MCP render and comparison matrix after artifact storage and render-timeout conditions clear.
- Review hover, pressed, selected, active, disabled, warning, completed, empty, crowded, long-text, and missing-localisation visuals from distinct successful artifacts.
- Review 1280 by 720, 1600 by 900, 1920 by 1080, and 2560 by 1440 output at the supported UI scale.
- Confirm live engine attachment, focus order, clipping, scroll behavior, click behavior, tooltip placement, and automatic animation playback in the consumer.
- Keep gameplay effects, costs, AI, balance, final integration, and live in-game validation parent-owned.

## Commit decision

No commit was created by this worker. The requested commit was limited to a complete isolated GUI tranche, while mandatory MCP post-render evidence remains incomplete. Committing an audit as a complete GUI tranche would overstate its completion status.
