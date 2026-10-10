# Event Logs: Clusters tab and Cluster Details redesign (10 Oct 2026)

Disposition: implemented. Acceptance basis: user brief of 10 Oct 2026, section 4.2 ("Event Clusters UI ... redesign where needed"), routed to the decision-density agent by the parent orchestrator. Live-game validation belongs to the user.

## Scope

- `interface/chaosx_events_log_popup.gui`: `events_log_clusters_content_window`, `events_log_cluster_details_window`, row templates `events_log_cluster_entry_generic`, `events_log_cluster_entry_country`, `events_log_cluster_detail_member_entry`, and the new `events_log_all_clusters_label` in the shell window.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`: row text visibility triggers and the all-clusters label trigger.
- `common/scripted_localisation/chaosx_events_log_cluster_details_scripted_localisation.txt`: fact cells 2, 3, 4 and 6 switch between the catalogue view and the history view.
- `localisation/english/chaosx_gui_l_english.yml`: cluster tab, row, fact-cell and member-row keys.
- Not touched: settings window, camps window, other Event Logs tabs.

## Defects fixed

- The filter and sort controls sat inside the scrolling list: they were clipped by the list margin (arrows 16x16 cut to 16x14, labels 20 to 16 px high) and scrolled away with the rows. They now form a fixed toolbar with `Show:` and `Sort:` labels above a separate scrolling list container.
- Actor rows drew two overlapping text boxes: the element named `cluster_entry_text_generic_visible` had no trigger of its own (the trigger of that name belonged to `cluster_entry_text_generic`), so it was always shown at x=12 on top of the flag and the actor text at x=55. Rows now use separately named name, meta and status boxes with matching `_visible` triggers.
- Each row was one two-line text box crammed with `ID: Type: Status:` labels. Rows now show the cluster name with the status right-aligned under a `Status` heading, a second line `#id  type  Activation  Fired`, and the auto-fire checkbox under an `Auto` heading.
- The all-clusters checkbox at the bottom right had no label; it now reads `All clusters`.
- Cluster Details showed three cramped meta lines, a 64 px description box with a permanent scrollbar, and member rows whose 449x41 row art sat in 426x58 slots. It now shows a two-column grid of six facts, an 84 px description with auto-hidden scrollbar, a `Member Events` list of 449x41 rows (about five visible) with name and status on line one and role, severity and chance on line two (the first tier moves into the row tooltip), and the trigger button with an aligned `Fires automatically` checkbox.
- The empty-list text now also shows before the first view rebuild (`NOT = { ^num > 0 }`), matching the History tab.

## Visual review

MCP `gui_render` (hoi4-agent-tools 3.9.0, closedFlags scenarios, 1920x1080 at UI scale 1). Images are kept outside the repository in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/clusters_ui_2026-10-10/`: `before_clusters_tab_mcp.png`, `reference_clusters_tab.png`, `reference_cluster_details.png`, `intermediate_*`, `after_clusters_tab_mcp.png`, `after_cluster_details_mcp.png`.

- The first intermediate render showed the column headings 5 px right of the row text (the grid box ignores the entry's own x offset); headings were moved and rechecked.
- The first details render showed the member second line wrapping into the row below; the tier moved into the tooltip and the line was rechecked.
- Limits: the renderer does not model `autohide_scrollbars`, country-scope actor rows or real scripted-localisation output; fixtures supply stand-in values. No in-game check was made.
