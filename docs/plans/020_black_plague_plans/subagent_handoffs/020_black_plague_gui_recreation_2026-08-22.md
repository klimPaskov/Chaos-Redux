# Event 020 Black Plague GUI Recreation Handoff

## Outcome

The rejected Event 020 dashboard was recreated as a wider, read-only plague response command board in the two event-owned runtime files listed below. The mandatory `hoi4.gui_rewrite` call was attempted before any source edit, but the adapter failed at its repository scan ceiling with `SCAN_BYTE_LIMIT`. The parent authorized the repository's documented bounded adapter exception after that exact attempt. The normal patch is not equivalent to a successful MCP rewrite.

The registered post-change `hoi4.gui_inspect` and `hoi4.gui_render` routes remained blocked by the same pre-scan adapter error. The parent recovered post-change render evidence by invoking the same installed `hoi4-agent-tools` MCP implementation through an in-memory MCP server with `scanMaxBytes` raised from 128 MiB to 256 MiB. This changed only the scanner ceiling and did not alter Event 020 source, render logic, or validation logic.

## Event ownership proof

- Event id and slug: `020_black_plague`.
- `common/decisions/categories/020_black_plague_response_categories.txt` owns `black_plague_response_category` and attaches `scripted_gui = black_plague_response_category_scripted_gui`.
- `common/scripted_guis/020_black_plague_response_scripted_guis.txt` defines `black_plague_response_category_scripted_gui` with `context_type = decision_category` and `window_name = "black_plague_response_category_window"`.
- `interface/020_black_plague_response.gui` defines only that Event 020 window.
- The surface is not shared with the event log, Event Details, settings, super-events, or another event.

## Exact identifiers and entry point

- Window: `black_plague_response_category_window`.
- Scripted GUI: `black_plague_response_category_scripted_gui`.
- Decision category: `black_plague_response_category`.
- Category picture sprite: `GFX_decision_cat_picture_black_plague_response`.
- Category picture texture: `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`.
- GUI layout: `interface/020_black_plague_response.gui`.
- Presentation binding: `common/scripted_guis/020_black_plague_response_scripted_guis.txt`.
- Sprite registry: `interface/020_black_plague_response.gfx`.
- GUI localisation: `localisation/english/020_black_plague_response_l_english.yml`.
- Category entry point: `common/decisions/categories/020_black_plague_response_categories.txt`.

## Files changed

- `interface/020_black_plague_response.gui`.
- `localisation/english/020_black_plague_response_l_english.yml`.
- `docs/plans/020_black_plague_plans/subagent_handoffs/020_black_plague_gui_recreation_2026-08-22.md`.

No gameplay decision, cost, effect, AI, category identity, scripted-GUI behavior, GFX registration, DDS asset, shared UI, Event 003 file, or Event 005 file changed.

## References inspected

- Repository `AGENTS.md`.
- `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-event-assets` skills.
- Offline Interface Modding and Scripted GUI Modding wiki snapshots plus the repository-required core wiki set.
- Installed vanilla `common/scripted_guis/_documentation.md`.
- Exact decision-category precedent: `interface/RAJ_famine.gui` and `common/scripted_guis/RAJ_famine_scripted_gui.txt`.
- Vanilla meter assets: `GFX_tiled_progress_bar` and `GFX_tiled_progress_bar_coloured` in `interface/countryofficercorpview.gfx`.
- Additional vanilla meter layout precedent: `interface/ast_right_vs_left_campaign_scripted_gui.gui`.
- Current Event 020 GUI, GFX, scripted GUI, localisation, and category source.
- Rejected handoff `020_black_plague_gui_redesign_2026-08-21.md` only to identify the rejected structure and blocker history. Its proposal was not reused as the design basis.

## Pre-change MCP evidence

### Inspect

The exact pre-change `hoi4.gui_inspect` succeeded for `black_plague_response_category_window` under representative Event 020 values.

- Result: `status = ok`, `code = GUI_INSPECTED`.
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Shared revision: `0991a59384f878a5de6d8eb605f653a88825dfc8e628222f5ca061bd53e35d7f`.
- Inspected Event 020 elements: 21.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bef517f27681b6287d51ddab7e3fa2ca533916e2b8d87cc3b53ab7311a354cb8/03d4e9e3d194ddb9f5c4f04d93a1a494362250fa81774203c97d2f5070b24a75/gui-inspect.0991a59384f878a5.json`.
- Global diagnostic ceiling: `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, with 1,999 retained and 1,518 dropped diagnostics. The dropped set included 1,398 `INDEX_SYMBOL_COLLISION` findings, principally unrelated repeated texture aliases in `interface/003_holy_realm.gfx` and `interface/005_soviet_collapse.gfx`.
- Scoped pre-change diagnostics included 11 visible overlaps plus clipping, alignment, spacing, and unresolved dynamic-value findings within the bounded validation set.

### Render

The broad state and resolution request exceeded the adapter's 180-second call timeout. A bounded 1920x1080 normal render then succeeded before editing.

- Result: `status = ok`, `code = GUI_RENDERED`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/864949744301256fd05c470d5737420995624e131d16dc7e6b6f79218a3afe3f/3e03aca61653cfea097fa2b30464d3ddbfd144e2c235998d6cc6e2990c46d546/black_plague_response_category_window-full.svg`.
- Artifact SHA-256: `864949744301256fd05c470d5737420995624e131d16dc7e6b6f79218a3afe3f`.
- The old 470x272 source used ten scaled checkbox sprites as five empty and five filled progress pieces, two unframed supporting-value lines, and three lower status rows. This is the rejected small-card and checkbox-led structure.

## Mandatory rewrite attempt and adapter exception

`hoi4.gui_rewrite` was called in `source` mode before any Event 020 source edit with these exact selectors:

- `relativePath = interface/020_black_plague_response.gui`.
- `windowName = black_plague_response_category_window`.
- `workspaceId = mod_chaos_redux_ea3b2d67c2c0`.
- Scenario id: `event20_gui_recreation_baseline`.

The call failed before scanning or proposal validation:

- `status = error`.
- `code = SCAN_BYTE_LIMIT`.
- Blocker message: `Scan exceeds the configured byte limit`.
- `filesScanned = []`.
- `changedFiles = []`.
- `artifacts = []`.

After the parent authorized the documented adapter exception, the fresh Event 020 source package was applied with a bounded normal patch. No Event 003 or Event 005 remediation was attempted in this task.

## Fresh layout hierarchy

1. A 520x282 dark category-attached command board.
2. A larger plague-doctor category picture at upper left as the event identity anchor.
3. A concise title and live programme-stage line in the upper-right header field.
4. One dominant 480x27 Countermeasure Progress meter using the inspected vanilla tiled progress-bar background and coloured fill assets.
5. Five contiguous 20-point fill regions driven by the already-wired Event 020 visibility triggers, reading as one meter rather than a checkbox row.
6. A large, coloured percentage at the meter heading.
7. One full-width lower summary band split into balanced National Deaths and Response Capacity columns.
8. One short capacity-exhausted warning visible only when the existing presentation trigger exposes it.

The board contains no buttons, checkboxes, tabs, click effects, fake controls, or button-shaped information cards. Ordinary decisions below the attachment remain the action surface.

## Background coverage map

| Region | Intended content | GUI elements | Interaction or state | Status |
| --- | --- | --- | --- | --- |
| Full 520x282 canvas | Dark HOI4 command-board frame | `Background`, `GFX_tiled_window` | Decorative, non-interactive | Implemented |
| Upper-left identity anchor | Event-owned plague-doctor/cat category art | `black_plague_response_category_picture` | Informational tooltip, click-through | Implemented |
| Upper-right header | Title and current countermeasure programme state | `black_plague_response_gui_title`, `black_plague_response_gui_programme_status` | Informational tooltips | Implemented |
| Central full-width meter band | Primary 0-100 countermeasure progress | Label, percentage, meter background, five contiguous fills | Existing fill visibility triggers at Event 020 thresholds | Implemented |
| Lower summary band | National deaths and remaining/total response capacity | `black_plague_response_gui_outbreak_summary`, `black_plague_response_gui_outbreak_ledger`, `black_plague_response_gui_response_capacity` | Informational tooltips | Implemented |
| Bottom warning line | Exhausted response-capacity condition | `black_plague_response_gui_capacity_warning` | Existing warning visibility trigger | Implemented |

## Visible value, action, text, and cost audits

- Primary mechanic value: Countermeasure Progress, shown as one 0-100 meter and exact percentage.
- Supporting mechanic values: national deaths and response capacity.
- Global deaths remain available in the National Deaths tooltip and are not a third main-panel value.
- Status cue: the current cure programme stage remains a named state rather than an extra numeric mechanic.
- Gameplay-changing GUI controls: 0.
- Primary GUI actions: 0.
- Active missions or target controls in this panel: 0.
- Spendable cost types shown: 0.
- Texticon coverage: not applicable because the panel displays no costs.
- Fake buttons or dead click regions: 0 by source design.
- Main explanatory prose: 0 paragraphs. The panel uses one title, short state labels, one compact ledger line, one coordination line, and one conditional warning.
- The progress tooltip remains the detailed explanation surface. It explains sources, consequences, the completion threshold, and the ordinary-decision response.

## State matrix

| State | Intended behavior | Post-change evidence |
| --- | --- | --- |
| Normal representative | 60 percent, first three contiguous meter fills, current programme state, national deaths, and remaining/total response capacity | Rendered at all requested resolutions |
| Hover | Informational tooltips only, no clickable controls | Source and click-region audit confirm zero controls |
| Warning | Capacity warning appears below the summary band without displacing the meter | Rendered in the warning state |
| Minimum | 0 percent and no coloured fill regions | Rendered in the minimum-value state |
| Maximum/completed | 100 percent and all five coloured fill regions | Rendered in the maximum-value state |
| Long text | Fixed header and summary bounds preserve separation | Rendered in the long-text state |
| Missing localisation | Review state exposes unresolved keys | Rendered in the missing-localisation state |
| Selected, active, disabled | No applicable controls. Read-only information remains visually stable | Not applicable to this read-only window |

## Before and after behavior

Before, the progress surface was a row of scaled checkbox sprites and the lower half presented several isolated text values with weak visual hierarchy. The progress value also displayed an implementation-facing dynamic threshold expression in the MCP review scenario.

After, the same Event 020 state is organized around one dominant vanilla-styled meter with a direct percentage. The board retains only two supporting numeric values, National Deaths and Response Capacity, in one balanced lower band. Global deaths remain in the deaths tooltip. International status and Medical Reserve are omitted from the main panel. The conditional warning remains subordinate. No gameplay outcome or visibility rule changed.

## Post-change MCP evidence and registered-route blocker

Three exact post-change calls were attempted:

1. `hoi4.gui_inspect` with the existing workspace and normal, warning, minimum, and maximum scenarios.
2. `hoi4.gui_inspect` without an explicit workspace and with the representative scenario only.
3. `hoi4.gui_render` for the exact window at 1920x1080 normal state.

Each call failed before scanning with the same result:

- `status = error`.
- `code = SCAN_BYTE_LIMIT`.
- Blocker message: `Scan exceeds the configured byte limit`.
- `filesScanned = []`.
- `changedFiles = []`.
- `artifacts = []`.

The parent then ran the same installed MCP implementation with only its scan ceiling raised and received `status = ok`, `code = GUI_RENDERED` for the final matrix. The matrix covered 1366x768, 1920x1080, and 2560x1440 at UI scale 1.25 across normal, warning, minimum-value, maximum-value, long-text, and missing-localisation states.

- Matrix folder: `C:/Users/klimp/.codex/visualizations/2026/07/14/019f6062-6114-7ff3-9061-e2570d1a8d03/event20_mcp_review_final_matrix`.
- Full PNG: `C:/Users/klimp/.codex/visualizations/2026/07/14/019f6062-6114-7ff3-9061-e2570d1a8d03/black_plague_gui_final.png`.
- Cropped PNG: `C:/Users/klimp/.codex/visualizations/2026/07/14/019f6062-6114-7ff3-9061-e2570d1a8d03/black_plague_gui_final_cropped.png`.
- Event 020-local retained diagnostics: 0.
- The global graph still reports unrelated Event 003 and Event 005 repeated texture-alias collisions and diagnostic truncation, so repository-wide GUI validation is not claimed.
- The offline renderer represents unresolved tiled textures with magenta diagnostic boxes; those boxes are render diagnostics rather than Event 020 source art.

## Assets and registrations

- Reused final Event 020 asset: `GFX_decision_cat_picture_black_plague_response`.
- Reused inspected vanilla assets: `GFX_tiled_window`, `GFX_tiled_window_transparent`, `GFX_tiled_progress_bar`, and `GFX_tiled_progress_bar_coloured`.
- New raster art: none.
- New sprite registration: none.
- Missing asset handoff: none.
- `interface/020_black_plague_response.gfx` was not changed.

## Remaining parent-owned work and risks

- The registered MCP route still needs a higher scan ceiling or narrower index scope to avoid `SCAN_BYTE_LIMIT` without the recovered MCP invocation.
- Repository-wide GUI graph cleanup remains outside Event 020 ownership because its retained collisions are in Event 003 and Event 005 assets.
- Parent/user retain final in-game consumer validation and the commit.

## Simplifications, omissions, and blockers

- Blocker: the registered mandatory rewrite, post-change inspect, and post-change render routes hit `SCAN_BYTE_LIMIT` before scanning any file.
- Recovered evidence: the final matrix and PNGs were produced with the installed MCP implementation after raising only its scan ceiling.
- Documented exception: a bounded normal patch was used only after the exact rewrite attempt and explicit parent authorization. It is not presented as equivalent MCP rewrite evidence.
- No fallback art, fake control, gameplay simplification, action substitution, shared UI change, or unapproved Event 003/Event 005 edit was used.
