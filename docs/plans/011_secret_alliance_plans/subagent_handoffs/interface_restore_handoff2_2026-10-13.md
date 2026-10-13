# Event 011 interface restore handoff

Disposition: implemented within the accepted restore scope; final visual acceptance remains with the parent render pass.

## Acceptance and ownership

The accepted basis is the owner's standing restore direction recorded in `docs/plans/handoffs_2026-10-13/00_common_rules.md` and `02_interface_restores_left_undecided.md`: unresolved presentation changes restore their exact earlier state unless the owner plan requests them, they belong to a genuinely new mechanic, or they are bug fixes without redesign.

The interface audit rows 74–75 identify the two Event 011 decisions: commit `b224aba5bed6` removed the hidden-state, recent-operation, and objectives information; commit `1b87b3f5cf39` resized the window from 720×360 to 500×250 without exact acceptance for that composition choice.

Exclusive ownership is evidenced by the dedicated `secret_alliance_counter_network_container` window and the `secret_alliance_counter_network_scripted_gui` assignment in `common/decisions/categories/011_secret_alliance_categories.txt`; the GUI is embedded in the two Event 011 decision categories there.

## Changed files and identifiers

- `interface/011_secret_alliance.gui`: restored the 720×360 container, original background and text positions, three-card row, hidden-state text, recent-operation indicator, objectives scroll panel, coalition warning, war-pressure text, and animation toggle.
- `common/scripted_guis/011_secret_alliance_scripted_gui.txt`: restored `secret_alliance_hidden_state_text_visible` with its historical conditions; retained the existing selected-card effects, click guards, dynamic meter values, and card-frame properties.
- No localisation keys changed. Existing keys `secret_alliance_gui_hidden_state`, `secret_alliance_gui_recent_operation`, and `secret_alliance_gui_objectives` remain in `localisation/english/011_secret_alliance_l_english.yml`; the compact `secret_alliance_gui_status` key remains untouched and is no longer referenced by this window.
- Existing assets remain wired: `GFX_011_secret_alliance_counter_network_panel`, `GFX_011_secret_alliance_evidence_meter_{fill,frame}`, `GFX_011_secret_alliance_preparedness_meter_{fill,frame}`, `GFX_011_secret_alliance_suspect_card_states`, `GFX_011_secret_alliance_status_recent_operation`, `GFX_011_secret_alliance_coalition_closure_warning`, and `GFX_011_secret_alliance_coalition_closure_warning_animated`.
- Existing native controls remain: `secret_alliance_suspect_card_{1,2,3}_select`, `secret_alliance_gui_clear_selection`, and `secret_alliance_toggle_animation`.

## Historical reference and native mapping

The exact geometry and content reference is `1cb65e610120894598ff48d2808a3af3fa04d897:interface/011_secret_alliance.gui`, the parent of resize commit `1b87b3f5cf39`. The hidden-state visibility trigger and pre-removal GUI content are taken from `268fcd384aa5ab0ea5d0cac10e20755237ccbabf`, the parent of `b224aba5bed6`.

No separate mockup image was created because the accepted task is an exact restoration and the historical GUI source itself is the authoritative reference; its regions are mapped to their native controls below.

The background panel and recent-operation symbol are static native `iconType` elements; title, meter values, suspect names, hidden-state summary, recent-operation text, objectives, and war pressure are live native text elements. Each evidence/preparedness meter uses a clipped child container with the existing dynamic fill and scaled frame. The three suspect cards remain multi-frame icons driven by scripted frame properties, with a transparent native button over each card's restored legacy bounds. The objectives remain in their original native clipped, scrollable container, not flattened artwork. The warning remains the original static/animated sprite pair, selected by the existing animation flags.

The vanilla precedent inspected was the Soviet paranoia scripted GUI at `interface/sov_paranoia_system_scripted_gui.gui` and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, which uses a dedicated native container, separate sprite/text controls, and scripted frame properties. The relevant local references are `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md` sections Containers (lines 73–127), iconType (178–195), instantTextBoxType (196–226), buttonType (227–256), and Position and orientation (369–385); and `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md` sections Window assignment (40–67), Context (144–164), Visible (173–177), and Triggers (194–205). The connected parent retrieved installed scripted-GUI documentation lines 1–80 at revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838` and offline interface icon/text sections at revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.

The subagent's reference MCP calls returned “not available to the model” on the initial context/search attempt. The parent confirmed its own reference routes are healthy and supplied the installed-documentation and offline-interface revisions above; no further child retries were made.

## Restored layout and retained behavior

The outer container is 720×360 at local origin (0,0), with the historical unscaled panel sprite. The title is at (22,12), selected lead at (504,12), meter clips at (24,53) and (394,53), and their historical value labels at (28,56) and (398,56). The suspect card art and native hitboxes begin at (18,102), (250,102), and (482,102); each clickable region is 184×96 and each historical name label is at y=114. The clear-selection button is at (678,12).

The restored information row places the hidden-state summary at (24,201), recent-operation symbol/text at (24,224)/(60,228), and objectives panel at (392,218) with a 300×64 clipped scrolling region. The legacy warning pair is at (24,262), war-pressure text at (160,288), and animation toggle at (574,314). These coordinates fit the restored 720×360 local bounds; the bottom controls no longer need the compact-window offsets.

The later meter rendering corrections remain: 0.5 meter scale, 128×12 clip, frame and fill co-located in the clipped child, and current evidence/preparedness tooltips. The legacy card row retains the current four-frame scripted card selection, card-select effects, border-conflict click guards, and a native hitbox aligned to the restored 184×96 card area. Animation warning selection and toggle conditions are unchanged. No Event 011 gameplay effects, costs, AI, incident probabilities, or Event C10 incident-variation logic were edited.

## State and interaction review

| State | Source behavior and local geometry review |
| --- | --- |
| Hidden, pre-reveal | `secret_alliance_hidden_state_text_visible` shows the historical summary only when the reveal flag is absent and evolution II or unresolved border conflict is active. Recent operation and active objectives retain their historical information controls. |
| Revealed | The hidden-state summary is hidden by its reveal guard; the window's existing visibility condition permits the revealed presentation. |
| Selected card | A card is shown only when its visible-suspect index exists; its effect stores that selected scope and refreshes the prepared border pair. The clear-selection control appears only when a selection variable exists. |
| Empty suspect pool | All three cards and their click regions are hidden by their existing visible-count triggers. The clear control also stays hidden without a selected-suspect variable. |
| Border conflict | Card selection and clearing remain disabled by the existing unresolved-conflict guards. |
| Evolution III warning | Animated and static warning elements remain mutually exclusive on the existing animation-disabled flag; war pressure is visible in Evolution III; the toggle is available only before reveal. |
| Hitboxes | Each card button uses the same (x,y) and 184×96 bounds as its historical card slot. Clear-selection and animation-toggle bounds remain inside the restored parent rectangle. |

The window has five primary action controls: three suspect selectors, clear selection, and the animation toggle. The ordinary visible numeric values are the two meter values plus conditional hidden-state/war-pressure summaries; the restored historical objectives panel can contain multiple active objective lines, so its full maximum text density was not measured in a runtime render.

Source geometry was checked for 1920×1080 at UI scale 1 and 1366×768 by verifying the native 720×360 bounds and each restored control rectangle against the source coordinates. This is source-only geometry evidence; it does not establish the engine's final category placement or pixel rendering at either display resolution.

## Before/after and validation limits

Before this patch, the board was 500×250, the three legacy information elements were absent, and the hidden-state visibility trigger had been removed. After this patch, the exact historical 720×360 arrangement and information surfaces are restored while current dynamic values, card selection behavior, current meter rendering improvements, and later click-guard logic remain.

Before-edit bytes and the scoped pre-existing diff capture are under ignored `.tmp/interface_restore_handoff2/event011/`; it also contains the historical 720×360 GUI and pre-information-removal GUI/script baselines. Both owned source files had no pre-existing diff at capture time. The resulting source blobs are `bcd5b80d1791bfe8050cbb8eca608f8ab38294c6` for the GUI and `d8e4a6bc091b8203cc730a072bd61b4396e766e0` for the scripted GUI.

No baseline, intermediate, or final MCP inspect/render artifact was produced by this subagent, as directed; the parent owns the final matched render pass. Therefore hover, pressed, active, disabled, warning, completed, and engine-rendered click-region appearance at both resolutions remain visually unchecked. The source predicates, current animated/static states, local bounds, and selected/empty-state visibility were reviewed directly. No in-game or live-game validation was run.

No simplifications or missing assets were introduced. The restored objective panel's potentially crowded multi-line state is the one remaining content-density limitation for the parent's render review; resolving it would change the historical layout and is outside this exact-source restoration.
