# Black Atlas tabs reference and acceptance

Disposition: parent-accepted G6 redesign of the existing Event 010 Atlas.

Acceptance basis: the parent accepted a four-tab layout and native Close button under the user's full Event 010 release authorization. The redesign preserves all 11 existing mechanic values, shows no more than four values at once, defaults to Seas, and shows Book only while the existing forbidden visibility trigger is true. Fronts, Compact, and Book use three mutually exclusive country tab flags. Tab clicks clear all three flags and set the selected non-Seas flag. Opening the Atlas clears the three tab flags. Close clears the Atlas open flag and its tab state. If Book loses visibility while selected, the Seas pane remains visible as the fallback.

Reference images: black_atlas_tabs_seas_reference.svg shows the default Seas view with Book hidden. black_atlas_tabs_book_reference.svg shows the conditional Book view with the native selected tab frame. Both references use the exact installed Event 010 background and header preview plus the installed vanilla tab and close sprites. They are source-based native layout references, not production render evidence.

| Reference region | Native element and usable bounds | Content or interaction | Asset, state, and adaptation |
| --- | --- | --- | --- |
| Background | death_black_atlas_background at x=0, y=0 in a 520x236 container | Existing full-canvas Atlas artwork | GFX_death_black_atlas_background from the existing Event 010 DDS |
| Header and title | death_black_atlas_header at x=10, y=8; death_black_atlas_title at x=22, y=13 with maxWidth 450 | Existing title | Existing animated header sprite, with its static source frame shown only in the reference |
| Close | death_black_atlas_close_button at x=480, y=8, size 32x33 | Native close action clears death_black_atlas_open and the three tab state flags | Installed GFX_closebutton; title width ends at x=472, leaving an 8-pixel gap |
| Tab strip | Four 116x36 native button bounds at x=22, 142, 262, and 382, y=46 | Seas, Fronts, Compact, and conditional Book navigation | Installed GFX_tab_small_116 with frame 0 for normal and frame 1 for selected |
| Seas pane | Label/value text box pairs at x=22/194, y=82, 104, 126, and 148. Label width 160 and value width 304 | Stage, consumed states, consumed population, and coastal risk | Four values. This is the default and the fallback when selected Book loses visibility |
| Fronts pane | Label/value text box pairs at x=22/194, y=82, 104, and 126. Label width 160 and value width 304 | Watch network current and maximum, jump surcharge, and front readiness | Four values. Watch current and maximum count separately |
| Compact pane | Label/value text box pairs at x=22/194, y=82, 104, and 126. Label width 160 and value width 304 | Line status, compact status and cohesion, and world footholds | Three values |
| Book pane | One label/value text box pair at x=22/194, y=82. Label width 160 and value width 304 | Forbidden office status | One value. The button and pane are hidden when death_black_atlas_forbidden_values_visible is false |
| Footer | death_black_atlas_footer at x=22, y=206, width 478, height 22 | Coasts, watches, and fronts against Death. | Static native text, 42 characters |

The three primary tabs keep stable positions. The fourth slot is intentionally empty while Book is hidden, and has no button or click region in that state.

Every value column starts at native x=194. Labels begin at x=22 with 160 pixels of usable width, which leaves a 12-pixel gap before the 304-pixel value field. The row baselines are 108, 130, 152, and 174 in the Seas reference. The Book value uses the same x=194 column.

The four logical tab actions and Close are the only in-window actions. The paired normal and selected native button elements represent the same four tab actions, so at most five clickable choices are visible simultaneously. The selected control remains clickable and repeats the same navigation effect.

The reference sample values are illustrative text-fit assumptions. The Seas coast sample reflects the source getter's watched state at the supplied watch network value of 5. The actual values remain native localisation and scripted localisation. The SVG uses Arial for legibility and omits the engine font metrics, so MCP production renders remain required for final visual acceptance.

No new runtime art or GFX registration is introduced. The live GUI continues to use the existing Death background and animated header, the installed vanilla tab sprite, and the installed vanilla Close sprite.
