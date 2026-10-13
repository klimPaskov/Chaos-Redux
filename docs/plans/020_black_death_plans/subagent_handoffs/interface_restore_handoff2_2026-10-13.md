# Event 020 response-window restoration handoff (2026-10-13)

Disposition: implemented in the bounded event-owned GUI source, with visual preview checks pending the parent’s coordinated renderer pass.

## Ownership and acceptance

The dedicated category `black_plague_response_category` is declared in `common/decisions/categories/020_black_plague_response_categories.txt` and attaches `black_plague_response_category_scripted_gui` to `black_plague_response_category_window` in decision-category context.
This is Event 020’s national response readout; selected-state containment remains in the separate `chaosx_disease_containment_category` surface, whose Disease Containment Board was rejected by owner item A12.

The parent’s explicit task prompt authorizes restoring the named Event 020 presentation changes.
The basis is the owner’s restore direction recorded in `docs/plans/handoffs_2026-10-13/00_common_rules.md` and the A-INTERFACE scope in `docs/plans/chaos_redux_restore_plan_2026-10-12.md`; the audit document’s earlier `retain pending owner decision` classifications were not treated as approval on their own.

## Files and identifiers

Changed: `interface/020_black_plague_response.gui` and this handoff.

Unchanged and preserved: `common/scripted_guis/020_black_plague_response_scripted_guis.txt`, `interface/020_black_plague_response.gfx`, `localisation/english/020_black_plague_response_l_english.yml`, the category registration, Event 020 decisions, and the separate Disease Containment Board.

The owning scripted-GUI identifier is `black_plague_response_category_scripted_gui`, with `context_type = decision_category` and `window_name = "black_plague_response_category_window"`.
The restored layout uses `black_plague_response_category_picture`, `black_plague_response_gui_title`, `black_plague_response_gui_programme_status`, `black_plague_response_gui_progress_label`, `black_plague_response_gui_progress_value`, the five `black_plague_response_gui_progress_empty_N` and five `black_plague_response_gui_progress_fill_N` icons, `black_plague_response_gui_medical_reserve`, `black_plague_response_gui_response_capacity`, `black_plague_response_gui_capacity_unorganized`, `black_plague_response_gui_capacity_warning`, `black_plague_response_gui_outbreak_ledger`, and `black_plague_response_gui_international_status`.

No localisation keys changed.
Existing keys reused include `black_plague_response_gui_title`, `black_plague_response_gui_programme_status`, `black_plague_response_gui_medical_reserve`, `black_plague_response_gui_response_capacity`, `black_plague_response_gui_capacity_unorganized`, `black_plague_response_gui_capacity_warning`, `black_plague_response_gui_outbreak_ledger`, `black_plague_response_gui_international_status`, and their existing tooltips.

## Historical reference and exact source comparison

The restored base is the exact earlier file from `e4443d948e92dbf8461fe101ed1e6c60f3079d44:interface/020_black_plague_response.gui`, SHA-256 `b39158a2eaa50e36b44d6f854b309dce0a928c21a49c0f4a3705c3b2cfb07f81`.
The final source differs from that historical source only by the 11-line `black_plague_response_gui_capacity_unorganized` informational node, required to keep the current zero/uninitialized-capacity presentation.
The current scripted-GUI file has SHA-256 `c2669749de9103c29c3b62485c07433a1bff14a207e715489c81dd814bd1f04d`, matching its pre-edit snapshot byte-for-byte.

Pre-edit bytes and diffs are retained under `.tmp/interface_restore_handoff2/event020/`. `020_black_plague_response.gui.before` has SHA-256 `f13f89cb4bfdcd050fa77198a490456e288bbdc85b2252d68d3d78f7b1b11ac1`; `after_vs_pre_edit.diff`, `pre_edit_vs_e444.diff`, `after_vs_e444.diff`, and exact raw historical GUI snapshots are present there.
The `historical_source_hashes.json` records hashes for the `e444` parent, `4efc01fc87f1137e98c864f928dd5603e6b7d2f1` parent, `33b6946dd923` revision, and `6e68b4384486` revision.

There is a historical layout conflict: the `33b6946dd923` parent `4efc01fc87f1137e98c864f928dd5603e6b7d2f1` and the `6e68b4384486` commit have identical 520px tiled-meter layouts, while the older `6e68b4384486` parent `e4443d948e92dbf8461fe101ed1e6c60f3079d44` is the 470px checkbox layout with the reserve and international rows.
The parent explicitly called for the 470px layout, checkboxes, and those earlier readouts, so the older complete source was selected rather than synthesizing two incompatible progress designs.
This returns the full earlier layout and also restores the category picture and earlier title/status placement; it does not retain the later tiled progress-meter sections from the `4efc` snapshot.

## Native mapping and layout

| Historical region | Restored native IDs and logical bounds | State and asset mapping | Adaptation |
| --- | --- | --- | --- |
| Tiled category card | Root `black_plague_response_category_window`, 470×272; background `GFX_tiled_window` | Independent container attached to the Event 020 decision category | Exact historical parent source |
| Category identity | `black_plague_response_category_picture` at (16,14), scale 0.58; title at (94,15), 350×30; programme phase at (94,49), 350×34 | `GFX_decision_cat_picture_black_plague_response`; live title and scripted phase text | Exact historical parent source; current dynamic status localisation retained |
| Countermeasure progress | Label at (22,92), value at (322,92); five empty and five threshold-fill icons at x=28,108,188,268,348 and y=120, scale 0.34 | `GFX_chaosx_checkbox_unchecked` is always visible; each `GFX_chaosx_checkbox_checked` overlay follows its existing named progress threshold | Exact historical parent source; current guarded threshold triggers retained |
| Reserve and capacity | Medical Reserve at (22,160), 202×28; organized capacity and unorganized-capacity alternatives at (246,160), 202×28 | Existing dynamic reserve and capacity text; the two capacity nodes are mutually exclusive under existing visibility predicates | The unorganized state node is retained from current source logic and added to the historical geometry |
| Warning and status rows | Capacity warning at (22,191); death ledger at (22,216); international response at (22,242), each 426×22 | Existing live warning, national-death value, and international-response localisation/tooltips | Exact historical parent source and current dynamic localisation |

The category-picture DDS exists at `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds` and is 114×101 pixels; at the historical 0.58 scale its nominal bounds are approximately 66×59, ending near x=82 and leaving a 12px gap to the title at x=94.
The picture is registered as `GFX_decision_cat_picture_black_plague_response` in `interface/020_black_plague_response.gfx`.
The checkbox sprites are registered in `interface/chaosx.gfx` at lines 125 and 129, and their referenced textures exist.
The historical `GFX_tiled_progress_bar_coloured` fill sections and the newer custom `GFX_black_plague_response_progress_fill` were not wired into the restored window.
No new art was requested or produced; there are no missing assets for the restored controls.

The restored window has no `buttonType` or scripted-GUI click effect.
Its icons and text are informational and provide their existing tooltips; the decision actions remain ordinary category decisions and were not changed.
There are no GUI-owned costs, requirements, AI actions, outcome effects, or cleanup paths to audit.

## Before and after behavior and state coverage

Before, the 520×282 command-board layout omitted the category picture, used a custom tiled-row fill, displayed response capacity in a summary card, and did not show Medical Reserve or International Response as separate rows.
After, the 470×272 historical category layout restores the category picture, original title and phase placement, checkbox progress bands, Medical Reserve, response capacity, warning, death ledger, and International Response.
The newer `capacity_unorganized` state remains available beside organized capacity at the same logical bounds.

| Source-derived case | Expected current source behavior | Visual evidence |
| --- | --- | --- |
| Progress absent or zero | Existing `has_variable = black_plague_countermeasure_progress` guards keep all five filled overlays hidden; empty checkbox bases remain | Not rendered by this agent |
| Each low-to-maximum progress band | Existing `black_plague_response_gui_progress_fill_N_visible` predicates show the corresponding checked overlay at the named `black_plague_value` thresholds | Not rendered by this agent |
| Capacity absent or zero | `black_plague_response_gui_capacity_unorganized_visible` selects the unorganized readout; organized capacity remains hidden | Not rendered by this agent |
| Organized capacity available | `black_plague_response_gui_response_capacity_visible` selects the existing remaining/total readout | Not rendered by this agent |
| Capacity exhausted or remaining value absent | Existing guarded `black_plague_response_gui_capacity_warning_visible` displays the warning only when total capacity exists and is positive while remaining capacity is missing or not positive | Not rendered by this agent |
| Normal phase, completion phase, and international response variants | Existing scripted localisation supplies the current phase and international-response text; the readout positions stay fixed | Not rendered by this agent |

All rows are text/icon readouts and have no action hitboxes.
The source geometry is fixed at 470×272 logical pixels; the requested comparison targets are 1920×1080 at UI scale 1 and 1366×768 at UI scale 1.
This agent was told to leave `hoi4_gui_inspect` and `hoi4_gui_render` to the parent, so neither a baseline, intermediate, nor final MCP image, hierarchy, state report, tooltip report, or click-region artifact was produced.
No in-game validation was performed or claimed.
The parent’s coordinated render should use matching normal, progress-threshold, capacity-unorganized, organized-capacity, and exhausted-capacity scenarios at both target resolutions.

The restored design exposes four quantitative value groups in its normal state: countermeasure progress, Medical Reserve, response capacity, and national deaths.
Programme phase and International Response are qualitative status lines; the capacity warning is conditional.
If the review policy counts the qualitative International Response state or every numerator/denominator as separate mechanic values, the exact historical layout exceeds the GUI skill’s four-visible-value ceiling.
I retained the owner-directed historical readouts rather than silently deleting one and have flagged this for parent review.

## References, validation limits, and remaining integration

The relevant installed game documentation was retrieved through `hoi4.reference_context`/`hoi4.reference_read`: `common/scripted_guis/_documentation.md`, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, lines 1–80 and 81–146.
It defines `decision_category` context, `window_name`, element triggers, properties, and update behavior.
Offline wiki excerpts were retrieved from `Scripted GUI modding - Hearts of Iron 4 Wiki.md`, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, assignment lines 40–67, visibility lines 173–178, and element trigger lines 194–205; `Interface modding - Hearts of Iron 4 Wiki.md`, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, overview lines 29–34.
These support the standalone-container assignment, z-order by declaration, and per-element visibility behavior.

The exact vanilla precedent was inspected locally because `hoi4.source_lookup` did not complete.
The first call was rejected for `maxLines = 100` and a missing `line`; one corrected request for `interface/sov_paranoia_system_scripted_gui.gui`, line 1, `maxLines = 80` remained pending for approximately 90 seconds and was terminated under the shared retry limit.
The local installed files were read directly: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/sov_paranoia_system_scripted_gui.gui`, lines 20–52, and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, lines 1–81.
The vanilla window separates meter artwork, dynamic frame-driven meter, and text; it is a useful display-layer precedent but does not verify this Event 020 layout.

Remaining parent work is to inspect the matched before/after rendered images, hierarchy, state visibility, tooltip extents, and any parent-context click regions at the two target resolutions and to assess the noted value-budget ambiguity.
Because this window contains no actions, decision action-integrity evidence remains with the decision owner and was outside this patch.
No gameplay or action simplification was made; the only presentation choice is the documented historical-source precedence between the incompatible tiled-meter and checkbox versions.
