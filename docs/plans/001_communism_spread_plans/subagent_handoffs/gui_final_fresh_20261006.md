# Event001 Fresh GUI Release QA Handoff

Status: incomplete visual acceptance. The current dashboard inspect succeeded, but the one minimal current-source production render returned Transport closed. The corrected mapicon inspect also returned Transport closed, so this handoff makes no current visual completion claim.

## Ownership and acceptance

The audited surfaces belong exclusively to Event001, 001_communism_spread. The entry point is the Event001 decision category chaosx_communism_fight_category in common/decisions/categories/001_communism_spread_categories.txt. Its scripted_gui attachment names communism_spread_dashboard_scripted_gui, which binds decision_category context to communism_spread_dashboard_container. The same Event001 scripted-GUI file binds communism_control_state_mapicon_scripted_gui with state_mapicon context to communism_control_state_mapicon_container.

The shared interface/chaosx_decisions.gui file also contains other event-owned windows. This audit inspected only the two Event001 container identifiers and did not change source.

The parent accepted the narrow G5/G6 dashboard repair recorded in gui_release_20261005.md. Its accepted basis is the parent-selected dashboard reference and direction to retain the authoritative threat score and stage, replace the aggregate total and daily drift row with a short map-selection prompt, and center the three level groups in the existing 470 by 174 panel. The accepted correction does not resolve broader Event001 specification or release acceptance.

## Identifiers and files reviewed

- Layout: interface/chaosx_decisions.gui, containers communism_spread_dashboard_container and communism_control_state_mapicon_container.
- Scripted-GUI bindings: common/scripted_guis/001_communism_spread_scripted_guis.txt, identifiers communism_spread_dashboard_scripted_gui and communism_control_state_mapicon_scripted_gui.
- Decision entry: common/decisions/categories/001_communism_spread_categories.txt, category chaosx_communism_fight_category.
- GUI localisation: localisation/english/chaosx_decisions_l_english.yml, keys communism_dashboard_status, communism_dashboard_counts, communism_dashboard_level_1_count, communism_dashboard_level_2_count, communism_dashboard_level_3_count, communism_threat_meter_tt, communism_controlled_states_tt, communism_control_level_1_tt, communism_control_level_2_tt, communism_control_level_3_tt, and communism_control_state_mapicon_tt.
- Meter sprites: interface/001_communism_spread.gfx registers GFX_revolutionary_threat_meter_000 through GFX_revolutionary_threat_meter_100, including the fixture-selected GFX_revolutionary_threat_meter_030.
- Tier sprites: interface/chaosx_texticons.gfx registers GFX_communism_control_level_1_texticon, GFX_communism_control_level_2_texticon, and GFX_communism_control_level_3_texticon. They use the existing AAT-derived decision_NOR_prepare_state_comm_1.dds, decision_NOR_prepare_state_comm_2.dds, and decision_NOR_prepare_state_comm_3.dds textures.
- Font consumers: hoi_18b resolves from the installed interface/core.gfx font definition. hoi_16mbs resolves from the installed gfx/fonts/hoi_16mbs.fnt asset.
- Animation: no animated element is defined or required by the accepted interface.
- Assets: no custom background, frame, icon, button, or DDS asset was added or is missing for the accepted design.

Current file hashes and the current Event001 block hashes are recorded in gui_final_fresh_20261006_evidence/mcp_evidence.json. The parent later updated the Event002 cure block and three cure localisation keys in shared files. Those changes are outside this audit. The current Event001 dashboard block is semantically equal to the accepted worker snapshot after normalizing newline representation, and the mapicon block hash remains unchanged.

## References and source precedent

The offline Scripted GUI modding page was read at the decision_category row, line 157, state_mapicon row, line 161, and Window assignment section, lines 40 to 67, revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30. The offline Interface modding snapshot was read at lines 81 to 109, revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c. Installed scripted-GUI documentation was read at lines 1 to 80, revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838.

The vanilla precedent inspected was interface/sov_paranoia_system_scripted_gui.gui with common/scripted_guis/SOV_paranoia_system_scripted_gui.txt. It uses an independent container with native icon and text elements and attaches that container through decision_category context. Source lookup revisions are recorded in the evidence JSON.

## Reference mapping and accepted hierarchy

The dashboard reference preserves the existing meter and status row. Its second row is a concise state-selection prompt. Three level icons and their live count textboxes form one centered group. Dynamic text, the meter, state counts, and the state mapicon remain native HOI4 elements.

| Reference region | Native element and usable bounds | State and assets | Adaptation |
| --- | --- | --- | --- |
| Threat meter | communism_threat_meter at x=38, y=0 in the 470 by 174 container | Dynamic GFX_revolutionary_threat_meter_000 through GFX_revolutionary_threat_meter_100 | The getter selects a native static meter frame, so the value remains represented as usable sprite art. |
| Threat label | communism_dashboard_status at x=8, y=76, maximum width 454 | hoi_18b and source-localised stage plus threat percentage | Retains the qualitative stage beside the authoritative score. |
| Response prompt | communism_dashboard_counts at x=8, y=102, maximum width 454 and maximum height 22 | hoi_16mbs, communism_dashboard_counts | Replaces the prior aggregate total and daily drift display with the accepted prompt. |
| Level 1 count | icon x=80, y=132 and count x=114, y=142 | GFX_communism_control_level_1_texticon and live level-1 count | The icon and count stay separate native elements. |
| Level 2 count | icon x=186, y=132 and count x=220, y=142 | GFX_communism_control_level_2_texticon and live level-2 count | The icon and count stay separate native elements. |
| Level 3 count | icon x=292, y=132 and count x=326, y=142 | GFX_communism_control_level_3_texticon and live level-3 count | The icon and count stay separate native elements. |
| State marker | Three mutually exclusive centered icons in the 42 by 42 state_mapicon container | The same three level texticons, selected by their state flag triggers | The marker is informational. The tooltip points to the Communist Insurgency decisions. |

The accepted hierarchy is the threat meter, threat status and score, state-selection prompt, then the three level counts. The map marker is centered on its state and does not become a button.

## Current inspect and visual review

The current-source dashboard inspection succeeded in workspace mod_chaos_redux_ea3b2d67c2c0 at shared revision 3b78f3368606947f14903a650f6b3b6141a270a186bb512148da5c19b4230ecf. The result reports a complete graph, zero unresolved and missing sources, no visible-overlap diagnostic, and nine intentionally omitted pdx_tooltip fields. Its only layout diagnostic is GUI_INCONSISTENT_SPACING, which reports sibling vertical gaps from 4 to 8 pixels at communism_dashboard_level_3_count, interface/chaosx_decisions.gui lines 138 to 146.

The current inspect artifact URI, SHA-256, byte size, and exact resource-read error are in the evidence JSON. A bounded read at offset 0 with length 32768 returned Transport closed. It was not retried.

The corrected USA dashboard fixture declares USA, original_tag USA, is_ai false, democratic government, communism_spread_idea, and no cosmetic tag through scenario.values. scenario.flags contains communism_spread true and explicit source-relevant negative country flags for the shared special-country classifiers. The values map supplies threat 34, counts 1/1/1, Growing Unrest, and GFX_revolutionary_threat_meter_030. This resolved the dashboard scripted-GUI visibility predicate in the successful current inspect.

The previous fact-corrected dashboard inspect before the parent's shared-file update also succeeded with zero unresolved findings at shared revision 1a82e8474eed0137b2f9ab89796be2c0a8ef7c233092243279968a2812b6e421. The current-source inspect is the release binding. The earlier initial inspect with an incomplete USA fixture had one unresolved visibility finding and is superseded.

The saved pre-edit production render remains useful as a matched reference for the 34 percent USA fixture. Its full, cropped, and annotated PNGs are listed in the evidence JSON. That earlier image shows the former aggregate and daily drift row and level groups placed left of the container center. It does not show the accepted current source.

The current minimal production render request used only the 34 percent and 1/1/1 USA fixture, normal state, 1920 by 1080 at UI scale 1, and generated scenarios disabled. It returned the exact error Transport closed and produced no image, crop, annotation, hierarchy, click-region, resolution, or comparison artifact. A prior broader render request with 0, 34, and 100 percent related scenarios and a sourceBaseline timed out after 600 seconds without an artifact. Neither request proves current visual behavior or sourceComparison.

The current source contains no buttonType or gameplay-changing control in either Event001 window. The dashboard shows four mechanic values: threat plus one count for each of three levels. The stage is a qualitative label and the meter repeats the same threat value visually. This stays within the four-value ceiling. The dashboard itself has zero visible actions and zero spendable costs, so there is no cost-count or cost-texticon requirement on this surface. The ordinary decision list supplies intervention actions outside the GUI. The state mapicon is informational.

The three level count sprites supply tier cues beside live counts. The source-localised tier tooltips name each level and describe its consequences, but all nine dashboard pdx_tooltip fields are omitted from the offline render. Tooltip placement and readable in-render prose remain unverified. The production image is also missing, so label centering, margins, sprite-to-text baseline, clipping, z-order, state coherence, and visible spacing remain unresolved. The spacing diagnostic alone does not justify a layout edit without the requested production image.

## Mapicon state coverage and route gap

The first fresh mapicon inspect succeeded, but its fixture used unqualified state flag keys. The inspector correctly reported that the level flags were undeclared, drew the three mutually exclusive icons together, reported overlap, and left the whole-window visibility predicate unresolved. Its clipping warning changes a 51.300000000000004 pixel sprite bound to 51.299999999999955 pixels. These findings are fixture-bound and are not current visual acceptance.

The parent supplied the live evaluator schema. For each corrected fixture, country facts belong in scenario.values, root country and global flags belong in scenario.flags, and PREV state facts use scopes.PREV.state with dotted keys such as flag.communist_control_level_1. The prepared corrected scenarios use USA state 378 with owner and controller USA, communist_controlled_state true, and exactly one of the level flags true. Related fixtures were prepared for levels 1, 2, and 3.

The corrected three-level mapicon inspect request returned Transport closed before producing an artifact. No further GUI MCP calls were made after the render route failed. The available archived pre-edit mapicon render covers a level-1 mark only. Current level-1, level-2, and level-3 mapicon visuals, whole-window visibility, click-region behavior, and current tooltip presentation remain unresolved.

## Behavior and visual rationale

Before the accepted repair, the dashboard displayed total controlled states and daily drift on its response row, and the three level groups sat left of the 470 pixel panel center. The accepted source keeps the threat score and qualitative stage, shows a state-selection prompt, and centers the three level groups while retaining their separate live counts.

The current Event001 source still expresses that accepted composition. The source layout does not replace the meter, count icons, or changing values with art. No source edit was made in this audit because the current production image was unavailable and the only remaining spacing diagnostic has no visual confirmation.

## Missing evidence, simplifications, and handoff

- Current dashboard visual acceptance is unresolved because the minimal gui_render call returned Transport closed and the broader comparison request timed out after 600 seconds.
- Current sourceComparison is unresolved. The final minimal request intentionally had no sourceBaseline after parent direction, and no comparison artifact was returned.
- Threat 0 and threat 100 screens were included only in the broad request that timed out. Their visuals remain unresolved.
- Current mapicon visual acceptance is unresolved. The corrected level-1/2/3 inspect request returned Transport closed, and no current mapicon render artifact exists.
- The nine tooltip fields are not represented by the offline renderer. Their source localisation is present, but tooltip visuals remain unresolved.
- No custom asset handoff is missing. Existing meter art and level texticons are reused. No new raster art, GUI localisation, scripted-GUI wiring, or gameplay logic was changed by this audit.
- No source edit, index change, commit, spreadsheet edit, or game launch was made.
- No simplification was applied to the accepted design. Required visual evidence is incomplete, so this is not a GUI completion handoff.

The parent owns final integration, the dashboard spacing decision after a production image becomes available, Event001 gameplay and decision action integrity, and release status. The user owns live-game consumer validation. Neither the successful source inspections nor the archived pre-edit images replace that evidence.

## Skills used

Read and followed AGENTS.md, chaos-redux-scripted-gui, chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents. No skill was created or changed.
