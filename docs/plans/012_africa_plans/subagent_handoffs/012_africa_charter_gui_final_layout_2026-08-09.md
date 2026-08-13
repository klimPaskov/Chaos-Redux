# Event 012 Africa Charter League GUI final layout audit

Date: 2026-08-09

Scope: final layout and interaction audit of the Event 012-owned `africa_charter_window` decision-category scripted GUI. This handoff does not claim full Event 012 completion.

## Ownership and exact integration surface

The GUI is event-owned because `africa_charter_council_category` is defined in `common/decisions/categories/012_africa_categories.txt` with `scripted_gui = africa_charter_window` and `visible = { africa_is_current_host = yes }`. The category's decisions are defined in `common/decisions/012_africa_decisions.txt`; the category attachment is not a shared event-log or event-details surface.

| Surface | Exact identifier or entry | File |
| --- | --- | --- |
| Window and scripted GUI | `africa_charter_window` | `interface/012_africa_charter.gui`; `common/scripted_guis/012_africa_charter_scripted_gui.txt` |
| Decision category entry | `africa_charter_council_category` → `scripted_gui = africa_charter_window` | `common/decisions/categories/012_africa_categories.txt` |
| Decision owner | Event 012 Charter action decisions | `common/decisions/012_africa_decisions.txt` |
| Sprite registration | `GFX_012_africa_*`, including the Charter window, frames, clause tabs, overlay buttons, and static/frame-sheet fallbacks | `interface/012_africa_charter.gfx` |
| GUI localisation | `africa_charter_gui_*` and `africa_charter_action_family_*` | `localisation/english/012_africa_charter_gui_l_english.yml` |
| Scripted localisation | Dynamic Charter values, selected member/state, regional and diaspora text | `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt` |
| Approved art | Charter background, header, frames, tabs, overlays, panels, and animation sheets | `gfx/interface/012_africa/` |

## Accepted presentation disposition

The accepted layout remains a 1000x680 decision-category window with a continental status header, member dossier, regional overlay and congress view, selected state rows, rival warning, diaspora summary and selectors, project/action ledger, clause warning, and selected action family controls.

The Charter surface keeps exactly eight recurring action families: protection, accession, regional congress, integration, economy, diaspora, rival bloc, and high chaos. The six late or phase-specific families remain list-only decision content: Scramble response, world order, constitutional crises, post-unification governance, host opening, and regional restorations. This is the authoritative B2 disposition in `docs/plans/012_africa_plans/012_africa_final_improvement_loop_addendum_2026-08-01.md` (the disposition block around lines 230-268) and `docs/events/012_africa/world_order.md` (the list-only statement near the start and the permanent disposition note around line 287). The GUI therefore does not imply that those six families are unavailable; it leaves them in the normal decision list where their target, phase, cost, AI, tooltip, and cleanup owners remain authoritative.

## Change made

Only `interface/012_africa_charter.gui` was changed in this tranche. The eight diaspora selector buttons had source coordinates outside the 1000x680 window (`x = 931/1033/1136/1239`, `y = 461/539`), so their visual controls and click regions could be displaced or clipped in the engine. Their existing sprite, text, scale, tooltip, and scripted-GUI identifiers were preserved while the coordinates were aligned to the right-panel content grid:

| Row | Element IDs | New positions | Size |
| --- | --- | --- | --- |
| Diaspora origin | `africa_charter_diaspora_origin_1` through `_4` | `(670,332)`, `(744,332)`, `(818,332)`, `(892,332)` | 97x33 |
| Diaspora skill | `africa_charter_diaspora_skill_1` through `_4` | `(670,388)`, `(744,388)`, `(818,388)`, `(892,388)` | 97x33 |

No gameplay effects, costs, outcomes, AI, decision availability, shared registries, event logs, event details, settings, super-events, or unrelated GUIs were changed. `common/scripted_guis/012_africa_charter_scripted_gui.txt`, `interface/012_africa_charter.gfx`, and the Event 012 GUI localisation were inspected and left unchanged.

## Layout contract and static interaction audit

The background coverage map is intentional: the full-window background covers 1000x680; the header plate anchors title, route identity, authority ring, seal, and primary/supporting values; the member-card, regional-card, rival-bloc, diaspora-summary, and project-progress sprites each have a matching content column; clause tabs are used only for the eight recurring family controls and the diaspora selectors; the regional overlay sprite is paired with nine overlay buttons; and the animated seal and authority ring each have static fallbacks.

The visible value budget is one primary Charter Authority value plus three supporting header values (Reach, Burden, and Pressure). Member, regional, diaspora, project, and action text is contextual detail attached to its card rather than a second numerical dashboard. Values have labels, dynamic state text, and nearby consequences or action-family context.

The action budget is the accepted two-row eight-family selector. Each family is a real scripted-GUI action that calls the existing `africa_select_action_family_page` path. The six episodic families are deliberately not duplicated in this surface.

The GUI has 35 button elements. A source audit found a matching `<element>_click` effect and `<element>_click_enabled` trigger for all 35 buttons, and all 56 GUI `text`/`buttonText` keys resolve in `012_africa_charter_gui_l_english.yml`. A bounds audit found every button rectangle inside the 1000x680 window after the repair. Member and state rows remain data-gated and retain their existing target arrays, selected-state cursor, tooltips, and disabled behavior. Selected family buttons disable through the existing trigger; the high-chaos family remains route-gated; member/state rows become unavailable when their candidate arrays are empty; and the rival warning, animated seal, and authority ring remain state-driven.

## References consulted

Required repository guidance was read before editing: `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md`. The offline `Interface modding - Hearts of Iron 4 Wiki.md`, `Scripted GUI modding - Hearts of Iron 4 Wiki.md`, and `Decision modding - Hearts of Iron 4 Wiki.md` pages were consulted alongside the required core wiki pages. Vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` was read, and the vanilla `usa_congress_decision_ui` precedent was inspected in `common/decisions/categories/USA_decision_categories.txt`, `common/scripted_guis/USA_congress_scripted_gui.txt`, and `interface/usa_congress_scripted_gui.gui`.

The accepted visual direction was cross-checked against `docs/specs/012_africa_specs/specs/012_africa_spec_part_2_charter_league_integration.md` (decision-category scripted GUI, member and regional status, diaspora route) and `docs/specs/012_africa_specs/specs/012_africa_spec_part_6_presentation_achievements_assets.md` (main layout, member card, and regional view).

## MCP evidence

### Before change

- Exact inspect: `hoi4.gui_inspect`, `windowName = africa_charter_window`, `scenario = default`, returned `GUI_INSPECTED`, 87 inspected elements, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/597160793d0b654a36b2bf993e58e3f050dc0abdf3697f6130360bcb8fed3d06/aad4b24ebeade1df7550c7d0fcefca460fbdce9e588c63fd2251b4022be5a26d/gui-inspect.8a455720cb04cf95.json`. The inline diagnostics were dominated by unrelated global GUI sources and the vanilla `GFX_tiled_window_transparent` resolver limitation; no Event 012-specific missing button/effect or missing sprite was retained inline.
- Baseline partial render at 1920x1080, uiScale 1, states normal/hover/selected/warning/long-text/missing-localisation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d460bf7ed1aa7c06175b6136e09c9e746a7db24fb52c09b53c824985f373603/a8d7a57f56cb442716bdd8516cbb4ed0784d4272c1159cc9194527476915c398/africa_charter_window-full.svg`, with the corresponding cropped, annotated, click-region, hierarchy, layout, state-matrix, resolution-scale, and comparison artifacts in the same render result.
- A single pre-change request for all 14 states at all three requested resolutions timed out after 180 seconds (`hoi4.gui_render` tool call timeout). This is retained as a matrix-coverage blocker rather than treated as visual evidence.

### Rewrite route and source edit

- The required `hoi4.gui_rewrite` patch route was attempted with eight exact patches against `interface/012_africa_charter.gui`. The first call rejected the uppercase hash format; the corrected lowercase-hash call returned `GUI_SOURCE_STALE`. A source-mode whole-file rewrite was then attempted and timed out after 180 seconds. Because the adapter could not resolve the current workspace source revision, the eight-line bounded repair was applied with `apply_patch` after the source and pre-change artifacts were reviewed.

### After change

- Exact post-change inspect: `hoi4.gui_inspect`, `windowName = africa_charter_window`, `scenario = default`, returned `GUI_INSPECTED` with 87 inspected elements and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a09193521ca71cdf464b01617741821dc3e64e448fdd225f0db3fae51f2c7f7/8ca3ab382b52de2011076ab751c17f4633cabb3ea10ebe7abc8dc410288f7869/gui-inspect.90154a0ad8aab726.json`.
- Post-change 1920x1080, uiScale 1, normal/hover/selected/warning/long-text/missing-localisation render returned full, cropped, annotated, click-region, hierarchy, layout, state-matrix, resolution-scale, and comparison artifacts. Representative full and click-region artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f09f29ad212122a2e00ec45d9e4dd9a9590e3656b113b10803bec4261b2f6/7f24f7c358e394bee5b66ac25cd1bd17a54981d4551529746ff21f434a477cbb/africa_charter_window-full.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d53b00f51eece2891fdf3a5162fa25ffe52b7c214212d4b21fcb6de60a388aa3/bc08496e22fbb3e6aca3bce08d4756396cfa4e44f2108032e317288f44cc16ed/africa_charter_window-click-regions.svg`. The render reported `stateCount = 6`, `resolutionCount = 1`, and same-scenario comparison `changedPixels = 0`.
- Post-change 1920x1080, uiScale 1, locked/disabled/active/completed/empty-list/full-list/minimum-value/maximum-value render returned the same evidence variants. Representative state-matrix and comparison artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64f764bd299a80db27941af29357e4f9ba408c4b3cfa9da7aa07fb704b30640f/01f8e4cedbf26a10f5bfeb2ae6c0485d0d50ab7e1734fbf2838b0d828a371fc2/africa_charter_window-state-matrix.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9adc158e6281fc052f521427df898f2b3c8e9cd0fd90224c46f9d285479354c/eec27f870ab28d66ae46cdfb6a1b7b55991e8b4d8c665018eafcc58d373a5384/africa_charter_window-comparison.json`.
- Post-change 1366x768 and 2560x1440, uiScale 1, normal/hover/selected/warning/long-text/missing-localisation renders both returned full, cropped, annotated, click-region, hierarchy, layout, state-matrix, resolution-scale, and comparison artifacts. The 1366 full artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f09f29ad212122a2e00ec45d9e4dd9a9590e3656b113b10803bec4261b2f6/4af4845b8a7e42a1ac8b6a6afa4a291a7cc986a16f896c89efd6b213a7a209a1/africa_charter_window-full.svg`; its resolution-scale artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/509dd1aff281e505dc6f163b3f1ff8dfca1b6f88ca8a3441fa8f420880af07b2/942ca7da0a594936b9c3d6aa861c8e9ad9fe27502fbfdc1604a13289f884717b/africa_charter_window-resolution-scale.svg`. The 2560 full artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb1f09f29ad212122a2e00ec45d9e4dd9a9590e3656b113b10803bec4261b2f6/401f710aba67d876b316c33361df97ae4e139738ac5efaa817dd1f5f8eabd59f/africa_charter_window-full.svg`; its resolution-scale artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9b6b5f62ae2958a640c50294eef7e6593814967e51574115a6430787c79e017/968c807b303d4c9383125f4599a513ba2d4d5b2d1a70621b7032e064cd782ad4/africa_charter_window-resolution-scale.svg`.
- Attempts to collect the second eight-state group at 1366x768 and 2560x1440 were made after the successful six-state calls, but the code-mode host timed out while waiting for the render response. The 1920x1080 second group is therefore the complete state-matrix evidence; alternate-resolution second-group coverage remains unresolved.
- Reading the large linked inspect/layout resources independently returned `Artifact provenance manifest is unavailable`; the linked artifact URIs and inline MCP summaries are preserved here instead of claiming parsed bulk evidence.

The render tool reports `offlineRepresentation = true`, global validation false because of unrelated repository-wide diagnostics, and the known vanilla `GFX_tiled_window_transparent` missing-texture/partial-render limitation. Dynamic localisation, masked vanilla flags, and some frame-sheet provenance are also approximate in the offline renderer. These are MCP limitations and are not new Event 012 source regressions.

## Remaining parent-owned work and blockers

The parent retains gameplay, decision cost and outcome review, AI and probability review, event-chain integration, live save/runtime validation, and final in-game confirmation. This handoff does not claim full Event 012 completion.

The bounded layout repair is complete, but the GUI rewrite adapter remained unavailable (`GUI_SOURCE_STALE` and timeout), alternate-resolution second state groups timed out, and the offline MCP renderer retained global diagnostics. No new asset handoff was required because all 16 Event 012 Charter GFX texture references resolve to files under `gfx/interface/012_africa/` and existing static fallbacks remain wired.

Simplifications and omissions: no gameplay or action-family expansion was attempted; the six episodic families remain list-only by accepted design; no shared UI was touched; and no in-game completion claim is made.
