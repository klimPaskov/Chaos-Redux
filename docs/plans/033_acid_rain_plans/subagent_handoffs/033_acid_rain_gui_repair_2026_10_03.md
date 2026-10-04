# Event 033 Acid Rain GUI repair evidence and handoff

## Disposition

The explicitly authorized source wiring tranche is implemented and awaits parent review.
The complete GUI repair and visual acceptance remain incomplete.
The pre-change inspect and narrowed render retries returned 600-second tool timeouts.
The first post-wiring inspect requests for both exact roots and the category render also timed out after 600 seconds.
That series' world render was client-terminated without a delivered result, which is not a confirmed server timeout.
Following the later authorized source corrections, another narrow inspect/render series was submitted for the exact world window and category inlay at 1920x1080 UI scale 1.
Its results are tracked separately below rather than promoted to successful visual evidence.
The required visual gate remains blocked until usable matched artifacts are obtained and reviewed.
This document does not promote the old UI handoff to final acceptance and makes no live-game completion claim.

The parent explicitly instructed this worker to continue source wiring despite unavailable visual evidence, approved the existing reference for that bounded repair, and clarified that source-only evidence cannot support visual completion claims.
That instruction supersedes this worker's earlier decision to pause source application at the failed baseline gate.
The parent required existing geometry to remain, except minimal defects proven from documentation/source, and retained ownership of the shared Event Log bridge and gameplay.

## Authorization and ownership

The current parent task explicitly authorizes repair of Event `033`, slug `acid_rain`, using the accepted GUI specification in `docs/specs/033_acid_rain_specs/specs/033_acid_rain_spec_part_6_scripted_gui_and_presentation.md`.
The parent confirms that ownership derives from the user's Event33 goal and that GUI specification.
The specification assigns a dedicated world map window and national Preparedness display exclusively to this event.
Current source proves the integration: `events/033_acid_rain.txt:7` defines `chaosx.nr33.1`, its immediate block calls `acid_rain_gui_refresh_read_only`, and `common/decisions/categories/033_acid_rain_categories.txt:27` attaches `acid_rain_decisions_scripted_gui` to `chaosx_acid_rain_decision_category`.
At the resumed baseline that category binding pointed to `acid_rain_world_window` in `interface/033_acid_rain.gui`.
The repaired category binding now points to `acid_rain_category_inlay`, while the stable world root has its own player-context binding.

The authorized source write set is `interface/033_acid_rain.gui`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, `common/scripted_effects/033_acid_rain_gui_effects.txt`, and Event33 GUI keys in `localisation/english/033_acid_rain_l_english.yml`, plus this handoff.
The parent subsequently expanded the scope to append GUI-only `defined_text` helpers in `common/scripted_localisation/033_acid_rain_scripted_localisation.txt`, with all existing cost helpers preserved.
The parent separately authorized creation of a scoped corrected reference before layout implementation.
Shared Event Log, EventDetails, settings, decisions, gameplay, debits, AI, probabilities, GFX registrations, and asset production remain outside this worker's source write set.
No commit is authorized.

The parent reported retirement of the unbound `acid_rain_decisions_container`, twelve unused prototype GFX registrations, and thirty-five unused or superseded DDS files with SHA equality under `docs/assets/033_acid_rain/retired_runtime`.
The reported follow-up commit was verified as `174b1c7e723d83c7d9ef32b0e62bb0601eb79c71`, titled `Repair Acid Rain report sprite paths after asset relocation`.
Those shared and asset surfaces were not edited or re-audited by this worker.

## Current source identities

| Source | SHA-256 at resumed baseline |
| --- | --- |
| `AGENTS.md` | `38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF` |
| `interface/033_acid_rain.gui` | `77C002339D30C671F25EFCA40B28B1A22D0CB5658CA2BB7536384050C5271FDD` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `0A784B5B04A39294A501FCD2D8CB2CA237CA85E8C0A8CAD967059B4846EE7D18` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `D80FCB50B92B50FCBA8CDCA7EDDADFCAB325AE6773E679839F3E13FFEF609C56` |
| `localisation/english/033_acid_rain_l_english.yml` | `84B110206761CE78E81290564AC4180283E459FD0A57DB45AB81904430C96BF4` |
| Read-only `interface/033_acid_rain.gfx` | `A24CBA2E9B7C4B567A96C0D1731AC97EE136E48CF41DB0F8E03FEF8BFF29B7F6` |

The assigned source files had no pre-existing Git changes at the resumed baseline.
The repository contains substantial concurrent unrelated work, which remains untouched.

| Source | First wiring tranche SHA-256, superseded by the following source corrections |
| --- | --- |
| `interface/033_acid_rain.gui` | `6E6EE1F4B15891F1CF974941F843FBF84C891D6C5FFAD31C73C997FBA5E01FE5` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `D93DF3DBF670A59A0E5EF01C98DF928895AB54E4542EC283FD0D8373F8A2EA5A` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `475DBA5AD12D3B1BD92B4B44CD9757947D378B1E44DA3CCCA7A702B6A210D315` |
| `localisation/english/033_acid_rain_l_english.yml` | `1E25D85B9A25D226EF627EBA2D0ABADB303C81AD45016A7DA8895149E43E708B` |

| Source | Pre-accessibility source tranche SHA-256 |
| --- | --- |
| `interface/033_acid_rain.gui` | `503A117621694B90BBB4AB4ADD06C51C70BD0883F380903E588975318BDD6671` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `B8D29A09764EC1CA789472E06C418E5D3B3A9D204066CE7116C246F006E037C3` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `9895BC65A8F2F2E826D5C40CA9AB8823FDA04F9A394FA9C5A86815D68B856ECE` |
| `common/scripted_localisation/033_acid_rain_scripted_localisation.txt` | `9B975D66A05114BE41FFBE4DB23796892F217E6D8775C135F5E6882213EE3A86` |
| `localisation/english/033_acid_rain_l_english.yml` | `E00CEB13FD788A93E4F7B806E6999253C9D928DEF74899C2358C0EB9C6A8A3D2` |

| Source | Accessibility source before the resumed runtime-cache intake and parent parchment fix |
| --- | --- |
| `interface/033_acid_rain.gui` | `CF67A0B6E3719C959899B2CF3B4C731AF251569F89C7597E7FAFD507AB6E46A5` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `ED648B8ED21CD35316FE9A9BF0BABA23262CD7678E0FA493FD9DFEA5FCEE1225` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `AE6C4AE6D7C2AE753F1684B1914EC7098A0B329109CF3610D736432FDCC26EDA` |
| `common/scripted_localisation/033_acid_rain_scripted_localisation.txt` | `0805B41A5D42F6025EEC2B86FA5901FF086E6F6D202CF2BAE76C7FC7EB0FC0E0` |
| `localisation/english/033_acid_rain_l_english.yml` | `4836BAC8E819441E7392C408EC25A59CB28C8917103D0419D7780090470C1620` |

| Source | Current final source-review identities after resume |
| --- | --- |
| `interface/033_acid_rain.gui` | `CF67A0B6E3719C959899B2CF3B4C731AF251569F89C7597E7FAFD507AB6E46A5` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `ED648B8ED21CD35316FE9A9BF0BABA23262CD7678E0FA493FD9DFEA5FCEE1225` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `C2AD79A0535A382F0BF99E710A965FA285577943BAB9CC13232DAEB2639E51BF` |
| `common/scripted_localisation/033_acid_rain_scripted_localisation.txt` | `0805B41A5D42F6025EEC2B86FA5901FF086E6F6D202CF2BAE76C7FC7EB0FC0E0` |
| `localisation/english/033_acid_rain_l_english.yml` | `70379934C899AC089808CADE79F5571D8E065557B89ED9A0AB73DB800D91122F` |

The final English hash includes the parent's separately committed parchment-description fixes, not a GUI-worker edit of those descriptions.
Commit `02460b6d5`, `Keep Acid Rain report descriptions readable on parchment`, was verified read-only.
The five locked `chaosx.nr33.101.d`, `.104.d`, `.105.d`, `.106.d` and `.107.d` lines were compared to that commit and remain identical.
The first 98 scripted-localisation cost-selector lines and complete cost-helper prefix were freshly compared to HEAD after resume and remain identical; no cost key or selector was edited.
An unavailable in-memory prefix capture initially yielded a false boolean from its availability guard, not a source mismatch; the fresh file comparison is the authoritative resumed check.

The original scripted-localisation cost-helper text was captured before appending the GUI helpers.
Its captured prefix SHA-256 is `A455AF2B5F084C034C01D26047756B802A0B6A4F328A39CAA2E9A736AB278A10`, and the post-append prefix comparison was identical.
That is preserved-text evidence, not a claim that the whole post-append file has its earlier hash.

## Reference selection before implementation

The selected scoped composition reference is `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png`.
Its exact tool-ready absolute path is `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png`; no `C:/...` shorthand was used in image tools.
Its SHA-256 is `2CA8693424C479BD0A40EE1FF34D8D75727A82BA22D6398117E5ADD221594BDA`.
It is a 1536x1024, 3:2 composition draft produced with the built-in ImageGen tool, retained from `C:/Users/klimp/.codex/generated_images/01a1002a-a66b-7233-a18e-7e94bbf9533f/exec-909ed406-9e6e-4c06-abab-2dc0c88fc0e1.png`.
The original generated output remains in place.
The worker selected this candidate under the parent's explicit direction to create a scoped corrected reference within the accepted Event033 design.
The parent individually viewed the original candidate and refined 1536x1024 reference, then accepted the refined composition within the user-authorized design.
That instruction specifically retains seven compact informational region rows, one World Coverage meter and the four-component Preparedness breakdown.
That is the selection acceptance basis, and approval of final artwork or visual completion has not been recorded.
It does not authorize shipping its flattened panels, controls, text slots, map, or ornaments as runtime artwork.

The initial candidate was refined because it introduced seven regional mini-meters.
The selected refinement retains one coverage meter, seven compact informational region rows, the map-left and cards-right hierarchy, the Preparedness strip with four component groups, and two control placements for close and refresh.
The generation prompts requested no readable letters or numbers and no extra mechanics, tabs, actions, costs, or controls.
Its blank label areas must become native localized text.
Its decorative row boxes and completion squares must become informational native text and state icons, without invented click actions.
The generated header ornament and region illustrations are composition cues only and are not requested new runtime assets.

The selected reference used `referenced_image_paths` for the inspected initial candidate, `transparent_background = false`, and the following exact final edit prompt through the built-in tool.
The tool exposed no model selector, and no particular unreported backend model is claimed.

```text
Use case: ui-mockup
Asset type: refined compositional reference for the accepted Event033 Acid Rain HOI4 scripted window. This is a design reference only, never a runtime background.
Input Image 1: edit target. Preserve the established 900x600 landscape composition, dark HOI4 metal frame, muted storm map, map/card/coverage/national/footer hierarchy, and the exact map palette. Change only the region summary and layout density described below.
Primary request: Remove the seven separate regional mini-bars and their raised card backgrounds. Below the one full World Coverage meter, arrange seven compact, plain text summary rows in two aligned columns, each with a small neutral completion mark slot. Keep these rows informational and visually non-clickable. Keep exactly one coverage meter. In the national strip, retain one prominent Preparedness area plus four small component tier pip groups as a subordinate breakdown. Keep the three compact weather cards on the right and their marker illustrations. Keep one close control at the upper right and one refresh button in the footer. Align all panels with generous readable gaps and keep every region inside the window.
Style/medium: restrained polished Hearts of Iron IV strategy-game UI, charcoal metal and aged bronze framing, parchment text fields, muted acid-rain gray-green map overlays, amber warnings, restrained rust-red severe state. No modern dashboard styling.
Composition/framing: straight-on 3:2 screenshot-like mockup, entire 900x600 window visible and centered; preserve the original reference's map-left/cards-right hierarchy and fit the seven region rows beneath the single meter without shrinking to tiny text.
Text: no readable text, no letters or numbers. Leave simple blank label fields for native localized text.
Constraints: keep Image 1 composition and art language; modify only the regional list and its density. Region summaries are status text, not buttons, cards, or meters. Only the two existing native controls may look clickable: close and refresh. No tabs, no action tray, no extra progress bars, no new values, no additional icons, no fake interactive controls, no generated UI copy, no watermark. Any control shown is a placement guide and must remain a real native HOI4 element in implementation.
```

The initial candidate was generated from the two inspected Event033 asset sheets with the following exact prompt, using `num_last_images_to_include = 2` and an opaque background.
Its retained tool output was `C:/Users/klimp/.codex/generated_images/01a1002a-a66b-7233-a18e-7e94bbf9533f/exec-062fde0f-4812-4a79-bb30-e5882c72ec3c.png`.

```text
Use case: ui-mockup
Asset type: scoped compositional reference for the Event 033 Acid Rain scripted GUI, a non-runtime design image.
Primary request: Create a single wide 3:2 mockup of the accepted 900 by 600 Hearts of Iron IV event window. Preserve the accepted hierarchy: dark framed header with event title and phase at top; broad world map on the left with restrained corrosive weather overlays and up to three clear markers; a narrow stack of three compact weather cards on the right, designed to also accommodate one global-layer card; a coverage meter and seven small regional progress rows below the map; a lower national-preparedness strip with one preparedness reading and four component tier-pip groups; and a quiet footer with one refresh control and a small read-only hint. Put one small native-style close control at the top right.
Input images: Image 1 is the existing Event033 static GUI asset contact sheet, style and asset-family anchor only. Image 2 is the accepted map-layer composite preview, map atmosphere and color-language anchor only.
Style/medium: polished but restrained HOI4 native interface, dark charcoal and weathered bronze frame, pale readable parchment text areas, muted acidic gray-green weather with amber warning and restrained rust-red severe accents. Keep the map and functional cards crisp and uncluttered.
Composition/framing: straight-on, entire window fills frame with tight balanced margins, no perspective. Align panel edges and baselines. Preserve clear spacing between map, cards, coverage, national strip, and footer. Reserve enough unobstructed label space inside every panel.
Constraints: This is only a compositional reference. No readable text, no generated letters or numbers, no fake interactive labels, no extra controls, no tabs, no decision trays, no cost icons, no plots beyond the single coverage bar, no extra mechanic values, no invented gameplay or panels. Keep exactly one close control and one refresh control. Keep interactive controls and dynamic text intended for native HOI4 elements, not as flattened artwork. Do not copy the supplied map art pixel-for-pixel. No watermark.
```

Existing Event033 references inspected were `docs/assets/033_acid_rain/generated_event_art/contact_sheets/gui_static_assets_contact_sheet.png` and `docs/assets/033_acid_rain/generated_event_art/contact_sheets/map_layer_composite_preview.png`.
Native UI references inspected were `.agents/skills/chaos-redux-event-assets/assets/gfx_references/scripted_guis/institutional_boards/contact_sheet.png` and its native-size `skoda_priority_ingame.png`, with the corresponding installed `interface/CZE_industry_focus_scripted_gui.gui` and `common/focus_inlay_windows/cze_industry_focus_inlay_window.txt` source sections.
The installed Soviet paranoia GUI and scripted-GUI sources were also read for separate native background, text, meter, and frame consumers.
The reference-library README, scripted-GUI README, and relevant catalog entries were read.

| Reference region | Native mapping retained or proposed | Bounds and state purpose | Assets and adaptation |
| --- | --- | --- | --- |
| Framed header | `acid_rain_world_title`, `acid_rain_world_phase`, `acid_rain_world_close` | Header within the 900x600 board, close face at upper right | Existing tiled window and vanilla close sprite, native localized title and phase |
| Left world map | `acid_rain_map_panel`, base, seven regional overlays, weather veils and front markers | Existing 560x300 map interior, ordinary, warning, severe and global states | Existing Event033 sprites stay separate, generated map is not installed |
| Right cards | `acid_rain_front_stack`, cards 1-3, global and empty cards | Stable front order with mutually exclusive global and empty states | Existing card background, separate icons and localized live text |
| Coverage and regions | `acid_rain_coverage_panel`, fill segments, frame, seven rows and completion icons | One World Coverage meter with exact touched and eligible counts | Native meter layers and text rows, no regional mini-meter or fake control |
| National strip | `acid_rain_national_strip`, Preparedness value, four component pips, national status/history | Viewing player's country, component breakdown of Preparedness | Four managed tiers remain distinct, live frame and tooltip mapping still requires review |
| Footer | `acid_rain_world_refresh`, read-only hint | Presentation refresh only | Native button, live localization and verified painted/click bounds |
| Later authorized accessibility addition | `acid_rain_world_motion` in the far-right footer, with live On/Off caption | Presentation preference only, same country-owned world context | Existing native button family; reference checkbox cue becomes live text, no runtime reference artwork |
| Category entry required by accepted spec | Implemented `acid_rain_category_inlay` through the existing `acid_rain_decisions_scripted_gui` | Phase, World Coverage, Preparedness, one exposure status line and one open control | Native category context, dedicated world window uses player context, visual review pending |

No broad redesign from the generated composition was applied.
The world board keeps its 900x600 size, centered position, map/card/coverage/national/footer composition, and existing art consumers.
Native adaptation, actual glyph centering, texture painted bounds, click regions, and reference fidelity remain unreviewed until production renders are available.

The category attachment is now `acid_rain_category_inlay`, a 500x92 native container implementing the accepted compact inlay from Part 6.
It contains separate phase, coverage, Preparedness and exposure text fields plus `acid_rain_category_open`, which opens the existing world window.
Its open control occupies logical bounds x=364..487 and y=54..88 using the existing `GFX_button_123x34` family.
The world window is no longer embedded in the category description and has exactly one `player_context` binding, `acid_rain_world_scripted_gui`, attached to the default main window documented by vanilla.
No duplicate scripted-GUI binding to the same root or invented native open/close command was introduced.

Minimal existing-world geometry corrections are explicit `upper_left` orientation on nine direct children of the centered root, coverage panel height 110 to 118 to contain its fourth row, nine 128 px card markers moved from x=238 to x=232 so their 0.3-scale logical bounds fit the 272 px card, and twelve card text widths reduced to 210 so their logical right edge stops before the marker slots.
The parent separately authorized uniform map fitting after confirming the source canvas is 1672x941, whose former scale 0.335 produced approximately 560x315 inside a 560x300 map panel.
All eleven matched geography layers now use scale 0.3188 and offset (13,0), yielding 533.0336x299.9908 without stretching or cropping geography.
The original nine ordinary/warning/severe map markers retain their geographic projection anchors through the same affine transformation, factor 0.3188/0.335, with scale 0.356866 and rounded positions (154,124), (276,149), and (401,107).
Card marker geometry remains independent of this map transform.
The global animation is a native 560x300 atmospheric layer, not a 1672x941 geography canvas, so it remains at (0,0), scale 1.
The board size, centered root position and surrounding composition were not redesigned.
These are minimal corrections derived from documented orientation inheritance and source bounds, not claims of optical alignment or rendered acceptance.

## Authorized static-accessibility source tranche

The parent explicitly accepted the Part 6 line 164 requirement for an animation toggle or static fallback, tied it to the user's complete animation/static asset request, and authorized exactly one compact country-owned native presentation control on the Event033 world window.
That instruction supersedes the earlier close/refresh-only reference restriction only for this one control.
The category inlay remains open-only, and no gameplay action, extra mechanic, redesigned panel or additional asset family is authorized or implemented.

Before layout/source application, the worker used built-in ImageGen to make a bounded edit of the selected refined reference.
The additional reference is `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_motion_toggle_reference_2026-10-03.png`, 1536x1024, SHA-256 `7A73D1C28602603CB7BDBDAE8CE20F97C2FAA96D17C71B5101B2EE8FE36C5EFC`.
Its original tool output is retained at `C:/Users/klimp/.codex/generated_images/01a1002a-a66b-7233-a18e-7e94bbf9533f/exec-7a279fe9-21f6-4f43-a785-facd72b4ebf1.png`.
The worker inspected and selected that bounded footer addition under the parent's explicit authorization; no claim is made that the parent has separately reviewed this new image or accepted a production render.
The original refined reference and its recorded parent acceptance remain unchanged.
The new image is reference-only and adds one far-right footer control while preserving the map, cards, seven compact region rows, single coverage meter and four-component Preparedness composition.
Its checkbox-like state cue is adapted to a real native button with a live On/Off caption, not installed as flattened control artwork.

The built-in tool used the selected refined PNG as `referenced_image_paths`, `transparent_background = false`, and this exact prompt.
No backend model selection or unreported model is claimed.

```text
Use case: precise-object-edit
Asset type: bounded accessibility-control composition reference for the accepted Event033 Acid Rain native HOI4 window; not runtime artwork.
Input images: Image 1 is the selected refined 1536x1024 composition, edit target. Preserve its entire world-map, three weather cards, seven compact informational region rows, one World Coverage meter and four-component Preparedness strip unchanged.
Primary request: Change ONLY the far-right footer region. Shorten its blank informational field just enough to add exactly ONE small right-aligned native-looking motion-mode toggle control, with a simple restrained checkbox-like state cue and a blank label area. Match the native-style refresh control height and the existing dark metal/bronze art language. Keep the existing close and refresh controls in their current positions, preserve all other panels and negative space. This single motion toggle selects animated versus static weather presentation for the viewing country and has no gameplay action.
Composition/framing: preserve the complete landscape board, straight-on view, 3:2 canvas, all existing composition and proportions. The new control occupies the rightmost footer only, leaving clear separation from explanatory text and the existing refresh control.
Text: no readable text, letters or numbers; reserve blank native label space. Any state cue and button face are reference placement guides, not final assets.
Constraints: no added tabs, metrics, meters, navigation, action trays, gameplay controls, ornaments, asset families or redesigned panels. Do not alter geography, markers, lighting, map weather, cards, coverage rows or Preparedness groups. No new animation artwork, no opacity masking or filtering of existing weather, no watermark. Output is design reference only; all live labels, states and controls will be implemented natively.
```

The new native control is `acid_rain_world_motion` at (753,560), using the existing `GFX_button_123x34` and `hoi_12mbs`, for logical bounds x=753..876 and y=560..594.
The refresh control remains at (24,560), and close is unchanged.
Only the existing footer hint width changes from 690 to 568, leaving a 20 px logical gap before the new button; its position and font are unchanged.
The current-mode caption is localized through `GetAcidRainGuiMotionMode`, and the mode-specific tooltip through `GetAcidRainGuiMotionTooltip`.
Both captions and tooltips state motion On/Off without relying on colour and explain that forecasts, weather and response are unchanged.
Painted button bounds, glyph centering, disabled face, effective hitbox and long-string behavior remain unreviewed.

`acid_rain_world_motion_click` calls `acid_rain_gui_toggle_motion` in the existing player COUNTRY context.
The effect rechecks the human country, open flag, positive current generation, matching view generation, supported phase and no migration failure before toggling only `acid_rain_gui_motion_disabled`.
An invalid/stale call clears lifecycle UI state through the existing close helper and leaves the preference unchanged.
The preference is country-owned, does not reuse `natural_disaster_animations_disabled`, creates no global motion setting, defaults to animation when absent, and survives close/reopen and episode generations.
Open/close bridge API identifiers and their parent scope contract are unchanged.

All nineteen existing animated consumers have exactly one new static partner at identical position, scale, parent, transparency and visual-order slot.
The partners consist of nine map markers, nine card markers and the global overlay.
Each animated predicate adds NOT motion-disabled; its static predicate adds motion-disabled while preserving the identical original weather predicate.
Ordinary/warning/severe precedence remains unchanged.
The country preference cannot turn weather on or hide its status: it selects the animated or static member of each already-visible family.
The base geography, region overlays, visited/ordinary/warning veils, coverage meter, region completion cues, Preparedness pips, labels and counters are not disabled by this preference.

| Family | Animated/static registrations consumed | Matching consumer instances | Registered frames |
| --- | --- | --- | --- |
| Ordinary front | `GFX_acid_rain_front_animated` / `GFX_acid_rain_front_static` | Three map front markers and three card front markers, each static ID is the original ID plus `_static` | 8 animated, one static representative |
| Warning | `GFX_acid_rain_warning_animated` / `GFX_acid_rain_warning_static` | Three map warning markers and three card warning markers, same suffix contract | 6 animated, one static representative |
| Severe | `GFX_acid_rain_severe_animated` / `GFX_acid_rain_severe_static` | Three map severe markers and three card severe markers, same suffix contract | 8 animated, one static representative |
| Global | `GFX_acid_rain_global_animated` / `GFX_acid_rain_global_static` | `acid_rain_map_global_veil` / `acid_rain_map_global_veil_static`, (0,0), scale 1 | 8 animated, one static representative |

The 8/6/8/8 registrations are unchanged and within the accepted Part 6 ranges of 8-12/6-8/8/8-12.
The separate accepted static-GUI marker registrations `GFX_acid_rain_front_marker`, `GFX_acid_rain_warning_marker` and `GFX_acid_rain_severe_marker` were not added as additional concurrent consumers or retired here.
No GFX registration, DDS, master frame, opacity or shader was modified.
Default motion remains on; the optional static display does not approve or replace required animation, and neither global branch masks the parent's rejected art.

Source comparison verified all nineteen static blocks match their animated counterparts except ID and registered sprite, and both visibility bodies retain the original weather predicates.
A twenty-case boolean model of visible/hidden, ordinary/warning/severe precedence, global visibility and motion On/Off found no simultaneous animated/static pair or lost weather family.
These are source-model checks, not engine execution, resolved renderer visibility, motion review or click proof.
The two added GUI text helpers bring the GUI-helper total to eighteen, with the sixteen original cost helpers preserved exactly.
All ninety GUI label/tooltip references and all GUI scripted-text dependencies resolve.
The write audit now permits only the two country lifecycle flags and `acid_rain_gui_motion_disabled`; ordinary variables remain presentation-only.

The closest native project precedent was read in `common/scripted_guis/013_natural_disasters_scripted_gui.txt:35-41` and `:240-258`, `interface/013_natural_disasters.gui:435-445` and `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt:1194-1205`.
Its country flag toggle and mutually exclusive animation/static predicates support the presentation pattern, not independent engine acceptance of this new control.
The read-only Event013 scripted-GUI source SHA-256 is `B0B748293F2DFE99D08CEFCB6F0C718D3624991E344664985DCB78308574370B`.
The accompanying Event013 GUI SHA-256 is `01D881CCAFD749F40C659D8F510825C6F4F61C6A1D1987E961A587FFFD406631`, and scripted-localisation SHA-256 is `34059D30CC1D851BA964FE60F1114E47716730380CFA8DFDF83BFD559887C2B8`.
Installed scripted-GUI and scripted-localisation documentation cited above remain the primary syntax authority.

## Exact current presentation identifiers

The world GUI root is `acid_rain_world_window`, bound by the new `acid_rain_world_scripted_gui` with `context_type = player_context`.
The stable `acid_rain_decisions_scripted_gui` still has `context_type = decision_category` and is attached by the unchanged category owner source, but its window is now `acid_rain_category_inlay`.
Its structural containers are `acid_rain_map_panel`, `acid_rain_front_stack`, `acid_rain_front_card_1`, `acid_rain_front_card_2`, `acid_rain_front_card_3`, `acid_rain_global_card`, `acid_rain_empty_card`, `acid_rain_coverage_panel`, and `acid_rain_national_strip`.
The world controls are `acid_rain_world_refresh`, `acid_rain_world_close` and the explicitly authorized `acid_rain_world_motion`, and the category control remains only `acid_rain_category_open`.
The country pip elements are `acid_rain_preparedness_component_pip_1`, `_2`, `_3`, and `_4`, with frames read from `acid_rain_gui_component_1_frame`, `_2_frame`, `_3_frame`, and `_4_frame`.
The corresponding `_tier` values remain presentation copies for their individual tooltips.
Their frame mapping is managed tier 0..4 to native frame 1..5, with clamping confined to UI copies.
Country presentation reads are `acid_rain_gui_preparedness`, `acid_rain_gui_current_warning_state_count`, `acid_rain_gui_exposed_state_count`, `acid_rain_gui_severe_warning_state_count`, `acid_rain_gui_aftermath_state_count`, `acid_rain_gui_event_deaths`, `acid_rain_gui_deaths_prevented`, and `acid_rain_gui_current_contamination_bp`.
World state reads remain `global.acid_rain_gui_phase`, coverage percent/touched/eligible, seven region touched/eligible/completed families, three stable front families, and the global-layer/superstorm presentation families enumerated in the exact source and old handoff.

Current static sprites are `GFX_acid_rain_map_base`, `GFX_acid_rain_region_overlay_1` through `_7`, `GFX_acid_rain_visited_veil`, `GFX_acid_rain_warning_veil`, `GFX_acid_rain_ordinary_veil`, `GFX_acid_rain_global_veil`, `GFX_acid_rain_front_marker`, `GFX_acid_rain_warning_marker`, `GFX_acid_rain_severe_marker`, `GFX_acid_rain_card_background`, `GFX_acid_rain_coverage_frame`, `GFX_acid_rain_coverage_fill`, `GFX_acid_rain_preparedness_badge`, and `GFX_acid_rain_component_pip`.
Their paths are under `gfx/interface/033_acid_rain/gui/`, registered by the read-only `interface/033_acid_rain.gfx`.
Current native fonts are `hoi_20b`, `hoi_16mbs`, `hoi_14mbs`, `hoi_12mbs`, and `hoi_10`.
Reused native sprites are `GFX_tiled_window`, `GFX_tiled_window_transparent`, `GFX_closebutton`, `GFX_button_123x34`, and `GFX_checkbox_small`.

Current Event33 GUI localization keys are `acid_rain_gui_contamination_tt`, `acid_rain_gui_front_timer_tt`, `acid_rain_gui_severe_cell_tt`, `acid_rain_gui_global_card_tt`, `acid_rain_gui_coverage_tt`, `acid_rain_gui_preparedness_tt`, `acid_rain_gui_refresh_tt`, and `acid_rain_gui_region_1_tt` through `_7_tt`.
The close tooltip is now `acid_rain_gui_close_tt`, and the opener uses `acid_rain_gui_open_tt`.
All 48 previous world-window label/value/button strings now reference Event33 localization keys matching their exact GUI element names.
The five category keys are `acid_rain_category_phase`, `acid_rain_category_coverage`, `acid_rain_category_preparedness`, `acid_rain_category_status`, and `acid_rain_category_open`.
Added component tooltips are `acid_rain_gui_component_1_tt` through `_4_tt`, and added national tooltips are `acid_rain_gui_national_warning_tt`, `_exposed_tt`, `_severe_tt`, `_aftermath_tt`, `_deaths_tt`, and `_prevented_tt`.
Only GUI-specific localization was changed.

## Pre-change source findings and repair disposition

1. `acid_rain_world_close` has an enabled trigger but no corresponding click effect in the current scripted-GUI binding.
2. The root visibility uses `global.acid_rain_gui_window_visible`, which the refresh helper derives from global runtime flags.
3. `acid_rain_gui_open_from_event_details` sets the country flag `acid_rain_event_details_gui_open`, but no scripted GUI reads that flag.
4. The only current world-window binding is `context_type = decision_category`, so history reopening has no explicit player-context consumer.
5. The state loop in the projection initializes country counters, enters each frozen state, and then increments unqualified variables in that state scope.
6. That loop uses lifetime `acid_rain_touched` as the exposed-state count, despite the gameplay owner maintaining `acid_rain_active_exposed_states` for current exposure.
7. The four managed tiers are `acid_rain_shelter_tier`, `acid_rain_water_tier`, `acid_rain_medical_tier`, and `acid_rain_transport_tier`, confirmed in the current preparedness owner source.
8. Current pip properties directly use tier 0-4 as sprite frame values for a five-frame strip and need review against native frame indexing.
9. Direct children of the centered root mostly omit their own orientation, despite the offline interface documentation stating that child elements inherit container orientation.
10. Source bounds place the fourth region row at y=102 with height 14 inside a 110 px coverage panel, and expected 128 px card markers at x=238 and scale 0.3 exceed the 272 px card width.
11. A 1672x941 map scaled by 0.335 is approximately 560x315 inside the 560x300 clipped panel.
12. The GUI uses literal English, raw phase/region/band numbers, dense separator strings, and 10 px status text.
13. The contamination tooltip labels the remaining lifetime allowance as a weekly allowance.

These are baseline source findings, not current rendered findings.
No source-only geometry or syntax check is substituted for the required production image review.

Findings 1-8 are addressed by the source wiring, country counter publication and pip frame changes.
The inherited-anchor and logical card/row defects in findings 9-10 received only the minimal corrections listed above.
The source-proven fifteen-pixel map overflow in finding 11 is addressed by the uniform fitting described above; its rendered fidelity remains unreviewed.
Finding 12 is partially addressed: English strings are localized, developer wording/separator dumps are shortened, and appended GUI-only scripted text provides meaningful phase, region, intensity and storm status names.
Small fonts, density, long values and actual native text placement still need production review.
Finding 13 is corrected: the contamination tooltip describes remaining lifetime allowance, with the accepted 1500 bp lifetime limit and 5000 bp event ceiling.
The legacy superstorm `_band` display field actually carries target-state counts, so its row labels now say states and its lookup follows the stored stable storm ID rather than assuming IDs equal row positions.

The implemented projection copies national current exposure from `acid_rain_active_exposed_states` and front exposure from `global.acid_rain_front_active_state_count_entries`.
Ordinary warnings use `acid_rain_warning_pending`, while severe/superstorm warning counts require matching forecast generation and a start day later than `global.date`.
The earlier source tranche used one bounded `every_controlled_state` pass and an explicit regular viewer target for the three country counters then lacking published equivalents.
That census is superseded by the resumed runtime-owner cache contract described below.
Current refresh performs no state iteration, saves no viewer target, scans no frozen-state registry and copies the three authoritative country counters directly.
The seven region summaries and three ordinary-front summaries read authoritative bounded arrays.
Severe state totals still read the existing scalar severe-cell ledger, at most 32 entries per displayed front, not world states.
`global.acid_rain_front_severe_entries` was checked as a potential three-entry alternative, but current owner source only clears/initializes it and does not maintain it, so it was not substituted for correct severe-cell totals.
Global and aftercare phases do not project retained ordinary front slots back into visible cards.
The four managed country tiers are copied only from a registered country record, without initializing or repairing gameplay records.
The GUI writes only presentation variables and its two lifecycle flags plus the later authorized country motion-preference flag, and creates no global event target.
No refresh calls gameplay setup, target selection, payment, mortality, contamination, AI, scheduler or country-registration effects.
The final source write audit found no ordinary variable write outside `acid_rain_gui_*` or `global.acid_rain_gui_*`, only the declared country lifecycle/preference flags, and zero whole frozen-registry references in the GUI helper.

### Exact coverage and truthful bounded lists

The parent explicitly requires that an incomplete frozen-state count never be displayed as 100 percent.
The projection preserves `global.acid_rain_total_touched_states`, `global.acid_rain_total_valid_states`, eligibility and all state flags, copying the exact counters to the UI.
Only `global.acid_rain_gui_coverage_percent` is changed: the nonnegative percentage is floored with `round(value - 0.5)` and clamped, then a raw-count inequality guard limits any fixed-point-rounded incomplete value to 99.
The visible world line retains the exact touched/eligible counts and an explicit Complete/Incomplete/No record label.
Both the Complete label and final meter segment require positive eligibility and exact count equality.
The same floored percentage feeds the compact category display.
Source arithmetic boundary checks give 0/1050 → 0, 1/1050 → 0, 1048/1050 → 99, 1049/1050 → 99, 1050/1050 → 100, and 0/0 → 0 with No record.
These are a source/math model, not executed engine scenarios.

The global storm list now uses the current stored ID array, including forecast and active records, while its headline preserves the gameplay owner's distinct active-storm count.
Each of the first three rows reads its stable stored ID, target-state count and meaningful Forecast/Active/Inactive status.
If five records exist, the localized informational hint says that three of five are shown and two additional storms exist.
The overflow hint is only visible for a positive overflow and adds no gameplay control.
Next-region names are only disclosed for a public warning; otherwise the GUI helper returns Unannounced rather than revealing a planned destination.
The global card's strongest weather label reads Global unless the owner's current active-storm count is positive, in which case it reads Superstorm.
It no longer asserts an active Superstorm band solely from the global phase.
The severe-card totals are labeled states, matching the scalar target-state total they display rather than implying a count of cells.

The first sixteen GUI `defined_text` helpers comprise one phase helper, current/next region and intensity helpers for each of three fronts, three storm-status helpers, strongest weather, exact coverage status and bounded storm-list overflow.
Their localization-key dependencies and all GUI references resolve in the Event33 English file.

## Exact parent bridge API

### Runtime-owner country-count contract, consumed on resume

| Authoritative COUNTRY field | GUI presentation copy | Meaning |
| --- | --- | --- |
| `acid_rain_current_warning_state_count` | `acid_rain_gui_current_warning_state_count` | Current ordinary warnings assigned to this controller |
| `acid_rain_severe_warning_state_count` | `acid_rain_gui_severe_warning_state_count` | Current live severe/superstorm forecasts assigned to this controller |
| `acid_rain_aftermath_state_count` | `acid_rain_gui_aftermath_state_count` | Unresolved aftermath assigned to this controller |

The runtime owner initializes these fields in `common/scripted_effects/033_acid_rain_effects.txt:588-590` and publishes controller-aware old/new contributions in `common/scripted_effects/033_acid_rain_aftermath_effects.txt:292-346` through `acid_rain_publish_state_country_counts` and `acid_rain_sync_country_consequence_flags`.
The publisher is consumed by the runtime state-consequence transaction at that file's line 484; the GUI does not call either owner helper.
The read-only publisher-file snapshot SHA is `C5780223A1285122489E57D00A31143F98671026EEA7099503157E036678DADB`.
These exact public names were identified from current source and coordinated to the GUI presentation fields above without renaming or mutating gameplay data.
The GUI copies each field only from a registered country record with the field present, retaining its existing UI-only defaults otherwise.
The former controlled-state census, forecast recomputation, temporary tally variables and regular viewer pointer were removed from the GUI helper.
The current source audit found zero state iterators, zero whole frozen-registry references, zero calls to the gameplay publisher and zero non-GUI ordinary variable writes in the GUI effect file.
Country-cache edge completeness, migration/backfill invariants and timing remain the runtime owner's responsibility and are not promoted to engine proof by this consumer change.

### Stable presentation entry points

| Effect | Required caller scope | Implemented behavior | Evidence limit |
| --- | --- | --- | --- |
| `acid_rain_gui_open_from_event_details = yes` | Viewing player's COUNTRY scope | Clears prior UI state, rechecks record validity, refreshes presentation, stamps the current generation, sets `acid_rain_gui_window_open`, then marks `acid_rain_event_details_gui_open` | Source wired, shared bridge and rendered/runtime behavior remain parent review |
| `acid_rain_gui_close_event_details_view = yes` | The same viewing player's COUNTRY scope | Clears both UI flags and `acid_rain_gui_view_generation`, with no gameplay effect | Source wired to `acid_rain_world_close_click`, rendered ESCAPE/click behavior unverified |
| `acid_rain_gui_open_from_category = yes` | Viewing player's COUNTRY scope | Uses the same guarded opener without the EventDetails origin flag | Source wired to `acid_rain_category_open_click`, category consumer render unavailable |
| `acid_rain_gui_refresh_read_only = yes` | Viewing player's COUNTRY scope | Cleans stale UI visibility and projects stored world/current-country data | Source scope audit performed, no runtime execution evidence |
| `acid_rain_refresh_gui_projection = yes` | COUNTRY scope | Compatibility wrapper for the same refresh helper | Existing wrapper retained |
| `acid_rain_gui_open_world_window = yes` | COUNTRY scope | Common presentation-only opener used by both entry APIs | Event-owned helper, available for parent-owned formation presentation if required |
| `acid_rain_gui_toggle_motion = yes` | Viewing player's COUNTRY scope with an open, current-generation, valid-phase view | Toggles only `acid_rain_gui_motion_disabled`; invalid/stale calls close UI state without changing the preference | Source wired to the single world motion button; native input/render behavior unverified |

The parent owns the shared Event Log and EventDetails click bridge.
It must invoke the open helper in the viewing player's explicit country context rather than the selected history actor, state, or an unrelated host country.
History actor data must not determine the national strip's viewer.
The existing API names now have a country gate and explicit `player_context` consumer in source.
Their live functional behavior is not claimed without the missing render/input evidence and parent bridge review.
No guessed `open_window` or `close_window` gameplay command is proposed.
Installed scripted-GUI documentation supports button-name click effects and visibility predicates, which are sufficient to implement country-flag opening and closing.

Open-time validity requires an existing human country, a positive stored `global.acid_rain_generation_id`, a phase between Formation and Closed inclusive, and no `acid_rain_migration_failed_closed` flag.
The effect repeats the category button's record checks and fails closed without initializing gameplay.
Aftercare and retained Closed records can therefore be reopened through history without an active-runtime prerequisite.
The world root requires `acid_rain_gui_window_open`, an existing view generation equal to the global generation, valid phase bounds and no migration failure.
A changed generation hides the old window immediately through its visibility predicate, and refresh removes stale UI flags.
Closing is idempotent and only affects the caller's UI state.
The history API displays the current/latest retained episode, not a reconstructed snapshot of an older history generation.

The parent reported that its shared Event Log/EventDetails bridge is now source-wired to `acid_rain_gui_open_from_event_details` in player COUNTRY context.
It uses a mutually exclusive native-slot button at (184,475), reuses `acid_rain_category_open` and `acid_rain_gui_open_tt`, checks event ID 33, and enables only for positive valid generation, Formation through Closed and no migration failure.
The parent's exact `events_log_event_details_window` pre-inspect attempt, cell 70, was pending at that report; this worker did not inspect or modify the shared files and does not claim engine proof for that bridge.
The same close API is available to the parent when closing or leaving that shared route.
The parent retains any automatic formation-opening policy and runtime event-driven country refresh call sites.
This tranche adds no world iterator or periodic hook to refresh every player.
World caches continue to update through existing owner calls, while another viewing country's national projection is refreshed on open, manual refresh or a country-scoped owner callback.
Continuous national display freshness between those calls remains a parent integration item.

## MCP exposure, requests and health gaps

The connected catalog exposes `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.gui_rewrite`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
No dedicated service health/status route is exposed in that catalog.
The live `source_lookup` schema has `symbol`, `kind`, `includeReferences`, line bounds and revision fields, and lacks `view` and `keyPath`.
`hoi4.script_validate` is absent.
Those unavailable fields and route are recorded as capability gaps, and were not passed or invented.

The first `reference_context` request exceeded the live question length limit and returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.reference_context: Too big: expected string to have <=160 characters at question`.
That argument error was corrected with a shorter question.

The original exact-window `gui_inspect` request used `windowName = acid_rain_world_window`, scenario `{ id: event033_acid_rain_repair_baseline }`, and `generatedScenarios = { enabled: false }`.
It returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect` with `Caused by: timed out awaiting tools/call after 600s`.
No artifact or source revision was returned.

The original render request used the same window and scenario, three requested resolutions at scale 1, and normal, hover, selected, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text and missing-localisation states.
Its execution cell was unavailable after the model/host interruption, returning `exec cell 48 not found` when resumed.
That is a lost-result delivery gap, not a successful render or a confirmed render timeout.
The corrected reference-context and bundled reference-search/source-lookup execution cells were likewise unavailable after interruption (`exec cell 42 not found`, `exec cell 49 not found`).
The parent separately reported a 600-second source lookup timeout for the retired shared container, which remains parent evidence rather than an inspection of this dedicated window.

Following the explicit orchestrator instruction, each unresolved route was retried once with a narrower request.
The inspect retry uses workspace `mod_chaos_redux_ea3b2d67c2c0`, exact `acid_rain_world_window`, scenario `{ id: event033_repair_empty_1920_ui1 }`, and generated scenarios disabled.
The render retry uses the same workspace/window/scenario with only normal state and 1920x1080 at UI scale 1.
The documentation retries use GUI context with limit 2, `context_type` search over wiki/script documentation with limit 2, and exact `acid_rain_gui_refresh_read_only` source lookup with one definition, 40 lines, and references disabled.
The inspect retry returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect`, followed by `Caused by: timed out awaiting tools/call after 600s`.
The narrowed normal-state render retry returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render`, followed by the same `Caused by: timed out awaiting tools/call after 600s`.
Each required GUI route has therefore received its one narrower retry, without a successful baseline or artifact.
These baseline routes received their required narrower retry; later source-version preview attempts are recorded separately below.
No optional rewrite was attempted.
The `reference_search` retry succeeded with status `ok`, code `OK`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.
It returned the offline Scripted GUI Context section at lines 144-164, id `9daea1ecda0ad48b7e3eb46b420a72f8e27e6f2d1277d3b2ffe827bfd164eb75`, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, and Localisation Namespaces at lines 531-555, id `aa80d1fb09d34bc976ba0f5c9446c9a686d2907e86fb885dd921edefe1dc74c4`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
The search reported four total matches, two returned matches, zero skipped entries, available wiki/game-document coverage, and unavailable `script_doc` coverage with zero indexed files.
The exact installed scripted-GUI `_documentation.md` was therefore read directly rather than inferred from the context bundle.
Revision-bound `reference_read` requests were submitted for those two returned sections, using only their 21-line and 25-line spans.
The narrowed `reference_context` request returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.reference_context`, followed by `Caused by: timed out awaiting tools/call after 600s`.
The narrowed `source_lookup` request returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.source_lookup`, followed by the same 600-second timeout.
The revision-bound `reference_read` requests did not return a result before the worker stopped on the failed GUI evidence gate.
Their read-only execution cell was explicitly terminated by the worker and returned `Script terminated`.
This is a client cancellation with unresolved retrieval, not a claimed server timeout or successful section read.
The same pertinent wiki sections had been read directly from local files, and their hashes and spans remain documented separately.
No authoritative current inspect, fidelity, full-window, cropped, annotated, hierarchy, click-region, state, resolution, source comparison, or validation artifact has been obtained.

## Required explicit fixture matrix

The following fixtures are the declared source-based coverage plan, not executed campaign evidence or successful MCP scenario coverage.
They must be mapped to supported scenario fields discovered from the service before use.
Scenario IDs alone do not establish their variable and flag states.

| Fixture | Declared world state | Viewing-country state | Required presentation |
| --- | --- | --- | --- |
| Empty | Formation phase 1, no fronts/global layer, 0/1000 coverage | Preparedness 0, four tiers 0, no current counts | Empty card, unfilled meter, neutral pips |
| Regional | Phase 2, coverage 250/1000, front 1 in Europe, 8 active states, 7 days, no warning/severe | Preparedness 40, tiers 2/1/2/1 | One front card, correct map/status, visible country strip |
| Multiple | Phase 2, three stable fronts in regions 1/3/6, one warning and one severe cell | Preparedness 100, tiers 4/4/4/4 | Ordered three-card stack, coherent exclusive marker states |
| Global | Phase 4, global layer true, ordinary fronts hidden, coverage 1000/1000, 46 elapsed days, minimum 0, next check 3, five stored storms with declared forecast/active statuses | Current country Preparedness and exposure | One global card, three rows plus 3-of-5/+2 informational hint, global overlay |
| Aftercare/history reopen | Phase 5, runtime inactive, no ordinary/global active weather, retained complete coverage | History open flag true, 3 unresolved aftercare states, retained national deaths and prevented estimate | Reopen in explicit player context with current national status |
| Closed UI | Same retained data as aftercare | Both UI flags cleared and view-generation stamp absent | Hidden root and no active click regions |
| Closed episode/history reopen | Phase 7, runtime inactive, latest retained valid generation | History opener called in viewing player country | Latest retained record can reopen independently of active weather |
| Exact coverage boundary | Same eligible registry, 1049/1050 touched versus matched 1050/1050 complete fixture | Current country record unchanged | 99 percent and Incomplete for 1049; 100 percent and Complete only for exact equality; exact counts visible |
| Long values | Synthetic stress fixture with long actual region labels, 1100/1100 counts, 365-day timers, seven-digit death strings and 10000 bp air | Long national status/history strings | No clipping, overlap, tiny-font substitution or lost values |
| Motion On | Repeat each shown Empty/Regional/Multiple/Global/Aftercare/Closed-episode/long-value fixture with unchanged weather and counters | Viewing-country `acid_rain_gui_motion_disabled` absent | Original animated branch only where weather is visible; Motion: On caption and disable-motion tooltip |
| Motion Off | Exact paired fixture, same weather, country record, counters and generation | Viewing-country `acid_rain_gui_motion_disabled` present, other country's preference unchanged | Static partner only in each visible family; Motion: Off caption and enable-motion tooltip; no gameplay delta |
| Motion lifecycle/invalid click | Current shown generation versus missing/stale generation or migration failure | Preference persists through close/reopen; invalid toggle cannot change it | Native control state/regions and guarded effect behavior; source expectation only until tools resolve facts |

Every shown-world fixture also requires a human viewing country, a valid positive global generation, a matching country view-generation stamp, `acid_rain_gui_window_open` and no migration failure.
National managed-value fixtures require that country's registered record.
The history fixtures additionally use `acid_rain_event_details_gui_open` to distinguish their entry origin, while the general world visibility gate remains country-owned.

Normal, hover, disabled, warning, active, completed, empty and crowded states remain required where applicable.
Selected state is not a current map or target interaction and must not be fabricated.
The declared resolution matrix is 1920x1080 at UI scale 1, 1600x900 at UI scale 1, and 1366x768 at UI scale 1, plus the specification's 125 percent interface-scale cases.
Matching before/after requests must retain identical named fixtures, values, localization, resolution, UI scale and source dependencies, and explicitly identify source revisions.

## Budgets and visual checklist

The accepted active values are Preparedness and World Coverage.
The parent explicitly requires four managed component tier indicators as the Preparedness breakdown.
Their native display and tooltip grouping still need review against the skill's hard visible-value budget rather than inheriting the old handoff's claimed pass.
The current surface has zero gameplay-changing controls, so spendable cost types and displayed cost texticons both number zero.
The three world controls are close, read-only refresh and the accepted motion preference; the category remains one opener.
The new preference is not a mechanic counter or gameplay action and adds no resource, cost or decision family.
Navigation and read-only refresh require a real effect and verified enabled/disabled treatment, not an invented gameplay outcome or AI action.

| Acceptance item | Current disposition |
| --- | --- |
| Reference selected before implementation | Recorded, no runtime image installed |
| Native control, label, meter and background mapping | Source implementation recorded above, production review pending |
| Country visibility, close and history reopening | Dedicated consumers implemented; parent reports shared bridge source-wired; renders/input behavior remain unverified |
| Four managed tiers, Preparedness and World Coverage | Tier/frame source mapping corrected, native budget and visual review pending |
| Label centering on both axes and painted/logical bounds | Blocked pending production images |
| Spacing, symmetry, scaling, clipping and overflow | Source risks identified, production review blocked |
| Z-order, overlays and click-through behavior | Production review blocked |
| Full state/resolution/hierarchy/click-region matrix | No current artifacts, blocked |
| Concise labels, values and tooltips | Localization and precise country/component tooltips implemented, density and long-value review pending |
| Cost-count and texticon audit | Zero gameplay payments on the window, decision owner unchanged |
| Matching post-source render and source comparison | Narrow calls and exact delivery failures are recorded below; no successful baseline or current matched artifact |
| Country motion accessibility | One native control and nineteen paired consumers are source-wired; current/native On/Off fixtures, tooltips, click regions and image review remain blocked |
| Live-game consumer evidence | None supplied or invented |

## Documentation and vanilla evidence

All required skill files were read: `chaos-redux-scripted-gui`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation`, plus the official `imagegen` skill for the explicitly authorized reference.
No skill was changed.
The separate `.agents/skills/chaos-redux-scripted-gui/references/visual-review.md` requested by the worker contract does not exist in the current skill directory, which contains only `SKILL.md`.
The corresponding user-level `.agents` skill path also did not exist.
The full visual acceptance checklist in the current scripted-GUI skill was read and remains the operative checklist, with the missing separate file recorded as an instruction-resource gap.

Direct local sections were read while the MCP reference routes were unavailable: offline `Interface modding` container, element, icon and text sections, offline `Scripted GUI Modding` context, visibility, effects, triggers and dirty sections, installed `common/scripted_guis/_documentation.md:1-110`, and installed effects documentation for `add_to_variable`, `set_country_flag`, and `clr_country_flag`.
The installed documentation establishes that both `decision_category` and `player_context` scope to the player country, and click effects are attached by element name.
The country census in `common/scripted_effects/033_acid_rain_effects.txt:820` provides an exact event-owned precedent for publishing state-loop results to the intended country using an explicit country target.
The managed tier completion source was read in `common/scripted_effects/033_acid_rain_preparedness_effects.txt:712-740`.

| Reference | SHA-256 |
| --- | --- |
| Installed `common/scripted_guis/_documentation.md` | `43CE647FC5FDE27488855B060B5463C790E5E356149FCEB010D36B960B40F838` |
| Offline `Interface modding - Hearts of Iron 4 Wiki.md` | `B74AFC86BE4E5DBB3B0FC600820D73A8340F7DC1821FC5EF02C9EE1F028C0B1C` |
| Offline `Scripted GUI Modding - Hearts of Iron 4 Wiki.md` | `B07D850EA78C4E1E3FC113574059AD2F3EA37DF320B9259128D66814023C1F30` |
| Installed `interface/CZE_industry_focus_scripted_gui.gui`, inspected lines 1-125 | `E54D100E61FB5FB322F7095A0804950C811F7732966A2676C2EEECAC31307A31` |
| Installed `common/focus_inlay_windows/cze_industry_focus_inlay_window.txt`, inspected lines 1-60 | `7FD9B6A3C9086521333A14F7DDB6143E6DDB77182B2DCBE5C7D0AD5A954FA92B` |
| Installed `interface/sov_paranoia_system_scripted_gui.gui`, inspected lines 1-70 | `B8925BF8DAF88BA82E6CE66F7B5131CAE7083E6EDA5367E2CF2B6EAEF6310A85` |
| Installed `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, inspected lines 1-100 | `00DB231BF1D3183520E8E980B3433D5E5678A101849F96C17625D6B9384D85C5` |

Direct local references establish syntax guidance only and do not replace MCP layout evidence.

The regular-target and temporary-variable lifetime sections were also read directly in offline `Data structures - Hearts of Iron 4 Wiki.md:303-326` and its temporary-variable discussion at line 440.
Its source SHA-256 is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Installed `documentation/effects_documentation.md:6496-6503` documents `save_event_target_as` with supported scopes `any`.
The effects-documentation SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
This supports the regular viewer pointer's effect-chain lifetime without introducing a global pointer or manual regular-target cleanup.

For the appended GUI helpers, offline `Localisation - Hearts of Iron 4 Wiki.md:656-686` establishes `defined_text`, first-matching `text` order, country/current-scope lookup and the American spelling `localization_key`.
Its SHA-256 is `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`.
Installed `common/scripted_localisation/00_scripted_localisation.txt:1-35` contains the corresponding inline documentation and an exact native country helper with triggered entries and an untriggered final entry.
Its SHA-256 is `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587`.
Installed `documentation/effects_documentation.md:6476-6484` documents `round_temp_variable` in any scope; offline `Data structures` line 573 documents nearest-integer rounding with half ties away from zero, supporting the nonnegative floor transformation used here.
No separate scripted-localisation documentation entry was found in the installed documentation directory by the narrow exact-token search.
The installed inline documentation and exact native source were read rather than assuming their absence meant the syntax was unsupported.
Installed `documentation/effects_documentation.md:3800-3818` establishes `every_controlled_state` as a COUNTRY-scope iterator with STATE-scope children and a supported `limit` filter.
Offline `Scopes - Hearts of Iron 4 Wiki.md:534-540` provides the matching rule; its SHA-256 is `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.

## Animation dependency and remaining work

The parent resumed production of the three marker families and global overlay separately.
The active `docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/brief.md` and `frame_plan.md` were read.
The registered animated sprites are `GFX_acid_rain_front_animated`, `GFX_acid_rain_warning_animated`, `GFX_acid_rain_severe_animated`, and `GFX_acid_rain_global_animated`.
Their registered static partners are `GFX_acid_rain_front_static`, `GFX_acid_rain_warning_static`, `GFX_acid_rain_severe_static`, and `GFX_acid_rain_global_static`.
At the pre-change dependency baseline, all eight registered DDS files under `gfx/interface/033_acid_rain/animation/` were absent.
The required sheet paths are `acid_rain_front_sheet.dds`, `acid_rain_warning_sheet.dds`, `acid_rain_severe_sheet.dds`, and `acid_rain_global_sheet.dds`, with matching `_static.dds` files.
The animation brief defines marker frames at 128x128 with 8/6/8 frames and 6/5/6 FPS, and the global overlay at 560x300 with 8 frames and 4 FPS.
Static accessibility is permitted by the accepted specification, but no static asset is substituted for required animation completion.
During this source tranche, the separate production worker installed all eight registered DDS files.
The first wiring tranche retained animated consumers without a static replacement or toggle.
The subsequent explicitly authorized accessibility tranche adds the one country-owned toggle and nineteen static partners described above, while retaining required animated consumers and default motion.
Read-only header checks found real `DDS ` signatures and dimensions matching the brief, including the 160x32 five-frame component pip strip.
The GFX registration file retained its baseline SHA-256.
These checks establish file presence and logical frame canvases only, not alpha quality, motion continuity, asset acceptance or native consumer behavior.
The active animation folder still had only `brief.md` and `frame_plan.md` at its top level when checked, without a final animation manifest or wiring handoff.
The parent subsequently reported individual review of all 22 masters across the three marker families, their processed and decoded images, six sheet/static pairs and configured-footprint boards.
Marker art is acceptable to the parent pending exact prompt recovery and motion/consumer MCP evidence, not fully accepted.
The parent separately reviewed all eight global animation v2 frames and rejected them for a continuous curtain with reported alpha 205.69 instead of the planned separated banks.
The separate art worker is repairing that global package.
This worker did not reduce opacity, filter, hide or replace the rejected global consumer to mask the defect.
The parent's art judgments are recorded as parent reports, not this worker's independent frame or motion review.
Final package provenance, motion and consumer evidence, corrected global art and the asset owner's handoff remain pending.

| Runtime animation file under `gfx/interface/033_acid_rain/animation/` | Dimensions | SHA-256 observed at first source wiring, not final package acceptance |
| --- | --- | --- |
| `acid_rain_front_sheet.dds` | 1024x128 | `F650D98B62A6749F92388B0B0AC7E38DDB332AAF8F296105C26BCC12461A6C6A` |
| `acid_rain_front_static.dds` | 128x128 | `07FD706D79ACDC66964C086F49647936469F3459BC972928B4CD0AD20DC8F0E1` |
| `acid_rain_warning_sheet.dds` | 768x128 | `7B6AF89103750A5835F6C6FEC0FA884C0210D01E8F45F922F48071120E8D7E71` |
| `acid_rain_warning_static.dds` | 128x128 | `79F7FA742D9873F223B404145FB841B9EDFA56950527422D9D1297472714FAE2` |
| `acid_rain_severe_sheet.dds` | 1024x128 | `B11B1FD5E1F8E8F712719F0E31C8EE7249A5A07B66E28EA574DE7815AA03419C` |
| `acid_rain_severe_static.dds` | 128x128 | `B8D4800B1FDD94369117A103720038536CEFC998EA060555157604B3321691FB` |
| `acid_rain_global_sheet.dds` | 4480x300 | `A5A206ACFF8C651DE20DD8DDD8DDC981029F5384F228C4C431951C88AEB87281` |
| `acid_rain_global_static.dds` | 560x300 | `73CD09EBBA69E53C2319C731B0C893E68DCBB9651A28307CF21A7E40E97FC970` |

The baseline and post-wiring asset sets therefore differ because of separately owned asset delivery.
Any future comparison must identify that dependency change explicitly rather than attribute improved texture appearance to this layout/source patch.

### Animation requirement-to-consumer mapping

| Accepted requirement | Dedicated GUI consumers | Registered family | Current disposition |
| --- | --- | --- | --- |
| Ordinary moving fronts | `acid_rain_map_front_1_marker` through `_3_marker`, plus corresponding card markers | `GFX_acid_rain_front_animated` and its static partner | Existing consumers retained; marker art partially approved by parent, motion/consumer evidence blocked |
| Public ordinary-front warnings | `acid_rain_map_front_1_warning_marker` through `_3_warning_marker`, plus corresponding card markers | `GFX_acid_rain_warning_animated` and its static partner | Existing consumers retained; marker art partially approved by parent, motion/consumer evidence blocked |
| Severe regional cells | `acid_rain_map_front_1_severe_marker` through `_3_severe_marker`, plus corresponding card markers | `GFX_acid_rain_severe_animated` and its static partner | Existing consumers retained; marker art partially approved by parent, motion/consumer evidence blocked |
| Global superstorm map markers | No current dedicated positioned consumer | Parent explicitly permits reuse of `GFX_acid_rain_severe_animated`, the same localized severe-weather family | Accepted and queued; placement blocked by bounded authoritative position/region metadata and visual evidence, not a request for a fourth marker family |
| Global atmospheric rain overlay | `acid_rain_map_global_veil` | `GFX_acid_rain_global_animated` and its static partner | Existing full-size consumer retained; parent rejected v2 art and owner is repairing it |
| Animation-disabled accessibility | `acid_rain_world_motion`, country preference, nineteen matched static partner elements | Existing registered static partners for all four animation families | Source implemented under the explicit later authorization; input, rendering and asset acceptance remain blocked; static art does not substitute for required animation |

The parent-owned superstorm ledger records IDs, episode, start/end, target-state count and forecast/active status, but this source review found no maintained per-storm region/centroid or target-scope array suitable for bounded map placement.
The seven-entry `global.acid_rain_superstorm_region_active_entries` array is rebuilt while planning targets from pre-existing state flags at `common/scripted_effects/033_acid_rain_effects.txt:3935-3944`, before the newly planned target set is committed.
It is not maintained as a post-spawn/retirement presentation cache and was not silently treated as authoritative current map geography.
Reconstructing placement by scanning the whole frozen registry for every country projection is explicitly disallowed by the parent.
The parent/gameplay owner must provide or identify a correct bounded geographic record before this worker can wire positioned superstorm consumers without guessing or modifying gameplay.
The existing approved severe family remains the designated asset consumer; no extra asset family, map interaction or mechanic is proposed.

Remaining parent-owned integration includes shared bridge visual/input proof, gameplay and decisions, runtime refresh call sites, bounded superstorm geographic metadata, costs, AI, final asset promotion, and review of later live consumer evidence.
The parent also reported fixing Major queue classification and batch receipts; those gameplay changes were outside this worker's write scope and were not edited here.
The source wiring and GUI-specific localization tranche is implemented.
Broad layout/readability repair, complete before/after MCP evidence and all visual acceptance items remain unfinished.
No unapproved gameplay simplification or fallback has been applied.

## Files changed by this worker and final scope check

The worker changed the four originally assigned source files: `interface/033_acid_rain.gui`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, `common/scripted_effects/033_acid_rain_gui_effects.txt`, and GUI-specific keys in `localisation/english/033_acid_rain_l_english.yml`.
Under the explicit later scope expansion, it appended eighteen GUI-only helpers to `common/scripted_localisation/033_acid_rain_scripted_localisation.txt`, preserving the sixteen original cost helpers exactly.
The worker also created/updated this handoff and retained the original scoped reference plus the explicitly authorized bounded motion-toggle reference PNG.
The current five-file diff includes native inlay declarations, player-context wiring, presentation-only lifecycle/projection fixes, meaningful GUI localization, exact coverage display and uniform map fitting.
The final source review below describes substantive evidence rather than treating diff size as proof.
No GFX, gameplay, decision, AI, shared framework or animation source was edited.
No commit was created.

The current scripted-GUI skill explicitly states, `If required inspection/render evidence, artifacts, scenarios, or dependencies are unavailable, record the exact call, selector, error, and affected evidence as blocked. Source-only review is not equivalent.`
Under the parent's explicit continuation instruction, those failures do not prevent this bounded source implementation, but the visual evidence gate remains blocked and no GUI completion is claimed.

## Source review and post-wiring requests

The source review cross-checked both native contexts and their unique GUI roots, named click effects, open-time rechecks, country flag cleanup, view generation checks and the final authoritative country-cache reads.
All 90 label/tooltip references in the two GUI roots resolve in the Event33 English localization file.
All appended GUI `defined_text` localization keys and every referenced `GetAcidRainGui*` helper resolve, with no missing helper or key found.
No duplicate localization key was found in that file.
The projection's ordinary variable writes remain within `acid_rain_gui_*` or `global.acid_rain_gui_*`, and the GUI effect file's country flag writes are only `acid_rain_gui_window_open`, `acid_rain_event_details_gui_open` and the authorized `acid_rain_gui_motion_disabled` preference.
No new helper identifier collision was found by exact-name searches.
These source checks support parent review of the wiring and do not establish engine execution, rendered state, click geometry, optical alignment or visual completion.

The source-traced lifecycle cases are: missing or invalid episode identity fails closed, a current generation opens the viewing country's window, another country's unopened flag does not meet that country's gate, a changed generation hides the stale view, refresh clears stale UI state, retained Aftercare/Closed phases can reopen without `acid_rain_runtime_active`, and repeated close clears only UI flags/stamps.
Those are expected outcomes of the inspected predicates and effect bodies, not executed MCP scenarios or observed game outcomes.
The gameplay owner remains responsible for the managed country-record and frozen-registry invariants read by the projection.

Post-wiring `hoi4.gui_inspect` requests were submitted for exact windows `acid_rain_world_window` and `acid_rain_category_inlay`, with generated scenarios disabled and workspace `mod_chaos_redux_ea3b2d67c2c0`.
The world request retains baseline scenario id `event033_repair_empty_1920_ui1`, and the new inlay uses `event033_repair_category_1920_ui1`.
One post-wiring narrow `hoi4.gui_render` request per window uses only normal state and 1920x1080 at UI scale 1.
The world render request includes the captured pre-change `interface/033_acid_rain.gui` text as `sourceBaseline` for the route's supported source-comparison mechanism.
The inlay has no prior layout because it is the source implementation of the accepted compact attachment.
Those first post-wiring calls relate to the first wiring tranche hashes above, not the later map-fit, text-helper and exact-coverage changes.
The opaque live scenario schema has not supplied resolved runtime facts, so these scenario IDs alone do not prove empty, shown, enabled or closed state coverage.
Both post-wiring inspect requests returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect`, followed by `Caused by: timed out awaiting tools/call after 600s`.
No post-inspect artifact or source revision was returned for either exact window.
The category render in that first series returned the same 600-second `hoi4.gui_render` timeout.
The first-series world render had not delivered a result when the worker explicitly terminated execution cell 38, which returned `Script terminated`.
That client termination is not a claimed server timeout, server job cancellation, artifact or successful comparison.

After the authorized map-fit, bounded country projection, GUI text helpers and coverage changes, execution cell 60 submitted another inspect and narrow render request for each exact root with the same scenario IDs and 1920x1080 UI scale 1.
Its source-effect hash was `F3FBD4FB266199FA01CCAB6E95FD414ABDBA84F939E56CA21DBA67B3DA45FAAC` and English hash was `4AC350232A2572CC34F3CE9DE971B9F6BC3A3AC1626FDD47D5F1960EB921C226`; GUI and scripted-GUI hashes match the pre-accessibility table, and scripted localisation was `0194D8BC4DB4522DFEE9DDB09F7A0C2E56DBE342D8BA0CEE73B0C3090CA76F45` before its EOF-only cleanup.
No result was delivered before the source review found the strongest-weather and severe-state label issues.
Cell 60 was client-terminated, returning `Script terminated`, rather than allowing its unconfirmed dependency revision to stand as final-source evidence.
No server timeout or server job cancellation is inferred from that termination.

After the pre-accessibility source corrections, execution cell 76 submitted `hoi4.gui_inspect` and `hoi4.gui_render` calls for both exact roots.
Their pre-accessibility identities are listed above; no delivered service revision or job identifier has been received.
The workspace is `mod_chaos_redux_ea3b2d67c2c0`, scenarios are `{ id: event033_repair_empty_1920_ui1 }` for `acid_rain_world_window` and `{ id: event033_repair_category_1920_ui1 }` for `acid_rain_category_inlay`, and `generatedScenarios` is `{ enabled: false }`.
Both render requests use `states: [normal]` and `resolutions: [{ width: 1920, height: 1080, uiScale: 1 }]`.
The world render includes the captured original `.gui` source as `sourceBaseline`; this is a layout-only baseline, not a reconstruction of the old scripted-GUI, projection, localization or asset dependencies.
The captured baseline was compared against `git show HEAD:interface/033_acid_rain.gui` and matched after normalizing line endings and final print newlines, with no category inlay in either baseline text.
The pre-accessibility scripted-localisation EOF blank line was removed after submission, changing its hash from `0194D8BC4DB4522DFEE9DDB09F7A0C2E56DBE342D8BA0CEE73B0C3090CA76F45` to `9B975D66A05114BE41FFBE4DB23796892F217E6D8775C135F5E6882213EE3A86` without changing a helper or display key.
No service source-revision acknowledgment was received, so actual dependency bytes used by the undelivered calls remain unconfirmed.
The current world inspect returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect`, followed by `Caused by: timed out awaiting tools/call after 600s`.
The current inlay inspect subsequently returned the same 600-second `hoi4.gui_inspect` timeout.
Both current world/inlay renders subsequently returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render`, followed by `Caused by: timed out awaiting tools/call after 600s`.
Cell 76 completed with all four routes timed out and no artifacts or source revisions.
No current-source render, click-region review, matched scenario image or source-revision acknowledgment is claimed.

Following the current world-inspect timeout, execution cell 87 submitted the required narrower child-only retry for `acid_rain_map_panel`, a real named container in the assigned GUI source, with the same workspace and `{ id: event033_repair_empty_1920_ui1 }` scenario and generated scenarios disabled.
It requests both inspect and a normal-state render at 1920x1080 UI scale 1; the render includes the verified original GUI text as the layout `sourceBaseline`.
This narrower read-only request does not redefine the accepted root or replace world-window context, visibility, click regions, country state or full-matrix evidence.
Both narrowed map-child requests returned the same exact route-specific tool-call errors and `Caused by: timed out awaiting tools/call after 600s`.
Cell 87 completed with no artifact or source revision, satisfying the required narrower retry without replacing the failed full-root gate.

### Accessibility post-source attempt

Before accessibility application, the worker captured the then-current GUI text at SHA `503A117621694B90BBB4AB4ADD06C51C70BD0883F380903E588975318BDD6671`, without a motion button or static partners, as `pre_a11y_gui`.
That source capture is not a before image.
The source changed while some cell 76/87 calls were still outstanding; neither those failed calls nor any unacknowledged service revision proves which dependency bytes the service read.
After the one-control accessibility tranche, cell 98 submitted exact-world `hoi4.gui_inspect` and `hoi4.gui_render` requests for `acid_rain_world_window`, workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `{ id: event033_repair_empty_1920_ui1 }`, and generated scenarios disabled.
The render uses only normal state, 1920x1080 UI scale 1 and the captured pre-accessibility GUI as `sourceBaseline`.
The request-stage hashes match the accessibility-stage table except scripted-GUI hash `CF6A9B609A4CCFCD30308B7BD79F492594DDE7B179BFFA27B2BE2CB4D7C776B9`, followed by a comment-only header correction to `ED648B8ED21CD35316FE9A9BF0BABA23262CD7678E0FA493FD9DFEA5FCEE1225`.
No runtime mode flag or weather facts are asserted through invented scenario fields; the live schema remains opaque and scenario IDs alone do not prove On/Off coverage.
Both accessibility root requests returned their route-specific tool-call errors and `Caused by: timed out awaiting tools/call after 600s`; cell 98 completed with no artifacts or service revision.
One narrower accessibility retry was then submitted in cell 106 for `acid_rain_map_panel`, the same workspace/scenario, generated scenarios disabled and normal-state 1920x1080 UI scale 1, with the pre-accessibility GUI as `sourceBaseline`.
That child contains ten animation/static pairs and does not replace the full-root motion-control input or matrix gate.
On the later resume, `functions.wait` returned `exec cell 106 not found`; the result is a lost execution-cell delivery gap, not a confirmed server timeout, source acknowledgment or successful image.
The earlier root and narrowed map retries already returned explicit 600-second failures as recorded above.
At the parent's explicit instruction, no overlapping repeated 600-second query loop was started after this resumed cache-consumer change.
The current cache-consumer effect hash and parent parchment dependency therefore have no final-source production artifact; their visual/engine gate remains open.
No matched accessibility before/after image, resolved mode branch, effective click region or native glyph review is claimed.

| Artifact/evidence category | Exact identity or location | Current evidence |
| --- | --- | --- |
| Selected design reference | `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png`, SHA recorded above | Parent-selected composition reference only |
| Original candidate and native reference shelf images | Exact retained tool and repository paths recorded in Reference selection | Design/source adaptation evidence only |
| Resumed source baseline | Original GUI SHA and verified captured source text; no inlay in that baseline | Source comparison input, not a render |
| Required before images/reports | Root `acid_rain_world_window`, baseline and narrowed IDs recorded above | None delivered; exact timeouts/lost-cell delivery gaps recorded |
| First post-wiring images/reports | Roots world/inlay, exact IDs and first-tranche source hashes recorded above | None delivered; inspect/category-render timeouts and world client termination recorded |
| Pre-accessibility full-root evidence | Execution cell 76, roots world/inlay, pre-accessibility source table and dependency deltas noted | Both inspect and both render calls timed out after 600 seconds; no artifacts |
| Pre-accessibility narrower child retry | Execution cell 87, `acid_rain_map_panel`, same empty ID, 1920x1080 UI 1 | Both routes timed out after 600 seconds; no artifacts |
| Motion-control composition reference | Versioned PNG, `7A73D1C2...` hash and exact prompt recorded above | Inspected scoped design reference before layout application, not runtime approval |
| Accessibility post-source evidence | Execution cell 98, world root, same empty ID, pre-accessibility GUI `sourceBaseline` | Both routes timed out after 600 seconds; no artifacts |
| Accessibility narrower retry | Execution cell 106, map child, same empty ID, pre-accessibility GUI baseline, 1920x1080 UI 1 | Attempted once; cell unavailable on resume, exact delivery gap recorded |
| Final runtime-cache consumer and protected parchment dependency | Current final source-review hash table | Source-reviewed only; no final-source artifact or engine/visual pass |
| Required state/resolution, fidelity, hierarchy and hit-region artifacts | Declared fixture and resolution matrix above | No successful artifact, image review or matched after evidence |

No generated reference, source arithmetic check, DDS header, parent art judgment, successful reference search or source-diff review is presented as a production GUI render.

## Remaining visual and presentation work

The uniformly fitted map, region-overlay state fidelity, inherited fixed front-slot geography, meaningful phase/region/intensity strings, unrevealed-destination label, completion mark frames, 10 px status text, long strings, glyph centering, panel rhythm, optical margins, z-order and effective click regions still require actual production images.
The compact inlay's native category clipping, disabled button face, label centering and placement likewise remain unreviewed.
The specification's full resolution and 125 percent scale matrix, empty/regional/multiple/global/aftercare/closed fixtures, crowded and long-value states, tooltip placement and matching source/artifact comparisons remain open.
The source-only continuation did not authorize a broad redesign or invented asset/state fallback.
Static-accessibility source wiring is implemented through the existing animation/static partners; its native presentation, input and full-matrix review remain blocked, and required animation is not replaced.
The specified category-return/EventDetails navigation affordances were not added to the preserved footer in this bounded source tranche and remain queued with the broader visual/integration work.
Superstorm map marker placement, corrected global animation and final motion/consumer acceptance remain explicit dependencies, not hidden omissions.
No simplification is hidden by the source-tranche status: the broader GUI repair and every missing visual gate remain incomplete.
