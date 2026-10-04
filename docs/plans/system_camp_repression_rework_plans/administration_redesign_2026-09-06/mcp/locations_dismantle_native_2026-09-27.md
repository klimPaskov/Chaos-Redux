# Locations selected-site dismantlement: native layout evidence

Disposition: implemented in source and visually reviewed for normal, targeted hover, and resource-locked states; native tooltip display and click execution remain unproved.
The hashes and graph revisions below identify the archived render fixtures; this report does not certify a fresh render of every state against later shared-tree source edits or engine execution.
Acceptance basis: the user-approved three-view interface and explicit legacy closure-choice contract, with `camp_admin_locations_reference_v2.png` created before the native layout edit.

The 900×540 `repression_ledger_window` now places four independent 120×38 selected-site actions at panel x positions 18, 150, 282 and 414, y=340.
Work, purpose and release retain separate native active/locked variants; the fourth Dismantle Site action has one active element and five reason-specific neutral locked elements.
Only `camp_admin_site_dismantle` has a click effect, which sets the retained `dismantle_selected_site` action id and calls the existing dispatcher under the same availability trigger used by its visible and click-enabled state.

## Reference and fixture provenance

The [review-only v2 reference](../references/camp_admin_locations_reference_v2.png) and [handoff](../references/camp_admin_locations_reference_v2_handoff.md) use the original clean Locations reference, the populated current-source MCP render, and an inspected institutional-board family.
The new normal fixtures `after/locations_dismantle_1920.json`, `after/locations_dismantle_1280.json`, and `after/locations_dismantle_125.json` declare a synthetic 1945-05-01 German reform-transition site with living, reconciled Brandenburg custody, funded maintenance, six visible registry rows and one selected state.
The date and authority are declared in the fixture description; the GUI MCP scenario schema cannot bind actual game date, government, state controller, or a save receipt, so these are source-informed layout fixtures, not engine route proof.
The hovered and resource-locked fixtures are `after/locations_dismantle_hover_125.json` and `after/locations_dismantle_resources_locked_125.json`.

## Current-source image review

`hoi4.gui_inspect` returned `GUI_INSPECTED` for the normal 1920 scenario at shared revision `8b5e7aeb81d3a59caae93ce0ccc1e54dd22cbffd81adfa7b1b6671b31dfaa5ae`, with no skipped sources or missing GUI elements; [inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2acdb814ea71be69233b7fb3eb92d2056a0d8af9e076c78f38d563b22a6e3d4a/3b25211ce66b3bb1e802d19e0454931976f02227dd4d414a907b599fe011fd59/gui-inspect.8b5e7aeb81d3a59c.json).
The matching resource-locked 125% inspection returned `GUI_INSPECTED` at shared revision `fa89f03df1b745bfe5deb07c6d2f6d4e4fd4205543fc342bf68fa20c40f63814`; [inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/435d051c63dfed84b4455fa61e0a4b72229725b5ec3ea271ddc5bb34ae9d9ca8/5ce2abcdeaf9c4fc6deb983e28ffef881efd61ae0f8e3d994fd32104d9aa14fb/gui-inspect.fa89f03df1b745bf.json).
Both validations report 18 nonblocking overlap findings across the whole window; the reviewed bottom action row itself shows four distinct button faces and no clipped or overlapping glyphs in the images.

| Fixture | Local image and MCP SHA-256 | Review |
| --- | --- | --- |
| 1920×1080, 100% normal | [cropped PNG](after/locations_dismantle_current_1920_cropped.png), `EBEFABFFD476CA317863E5A672E959DEDC25EBB18AFFE7E18D26A91C9C0FCFEC935` | Four action labels fit; the fourth face is distinct from Release. |
| 1280×720, 100% normal | [cropped PNG](after/locations_dismantle_current_1280_cropped.png), `E6CB92C208B28F85348E9CD52C7ED489229D548A16394335E48CCFC437740E44` | Four faces and labels remain separate in the smaller window. |
| 1920×1080, 125% normal | [cropped PNG](after/locations_dismantle_current_125_cropped.png), `F71709D00B180442CE474D2FAE9EEA031AE912461AE917F93E09D3BD45A3B771` | No bottom-row text clipping; Release Survivors and Dismantle Site remain legible. |
| 125%, element-specific Dismantle hover | [cropped PNG](after/locations_dismantle_targeted_hover_125_cropped.png), `3706FA68351D2FEF68AAF491B804389AB6FE71451DBD2A6EAF30F4C999C9FC97` | Only Dismantle Site highlights; a prior global-hover request that lit every button was rejected. |
| 125%, element-specific hover click regions | [full PNG](after/locations_dismantle_targeted_click_regions_125.png), `50DA752FE374921D9791569CE9DE3EBA9A26EE3E9284AA19E77C178A8D14811F` | Four separated 120×38 action rectangles with gaps; no action-to-action hit-region overlap. |
| 125%, insufficient resources | [cropped PNG](after/locations_dismantle_resources_locked_125_cropped.png), `75150E29D3151FBE8E2A22D00A5A3A8AC748C27C81E0AFA84B78948DB5EF1A4B` | Neutral `Closure Locked` face; no active green highlight. |
| 125%, locked click regions | [full PNG](after/locations_dismantle_resources_locked_click_regions_125.png), `0908AC667225DCAC192E9C183C238C089B32D62CD58A0634EA289CA2ED183BFD` | The locked face occupies only its own rectangle; its scripted GUI binding has `always = no` click-enabled and no effect. |
| 125%, long name, large values, bottom scroll | [cropped PNG](after/locations_dismantle_stress_125_cropped.png), `BC5DA8EA6E824354B27104E8C40E623DAFBFA01234A01BC5FB4E722D9A4BCBB2` | Schleswig-Holstein, 99.875-thousand custody, 120-thousand capacity, last roster row, Purpose hover and two neutral locked actions remain fully visible. |
| 1280×720, long name, large values, bottom scroll | [cropped PNG](after/locations_dismantle_stress_1280_cropped.png), `66421D18B35CB063F9774B988F3BC6E14230EE003084749C1E034F1699548C20` | The same text and four action faces fit at 720p, though the standard HOI4 scaled text is small. |
| 1920×1080, long name, large values, bottom scroll | [cropped PNG](after/locations_dismantle_stress_1920_final_cropped.png), `3C3481C24F708F2CC0646FAFE5FAABB7C2EADC51FAAF2CEE4FFF84EBFD0AB635` | A no-hover retry after the first artifact-read failure shows the long name, six complete bottom rows, large values and two locked labels without clipping. |
| 125%, empty registry | [cropped PNG](after/locations_dismantle_empty_125_cropped.png), `27CFB76BA8D1520FA8B7453E48C3C13E8F8D79FF12C018AB42F73A45CC8960A7` | The message is readable; the selected-site panel and all four contextual controls are hidden. |
| 1280×720, empty registry | [cropped PNG](after/locations_dismantle_empty_1280_final_cropped.png), `86D2FAFBDAA156219810E1CF6D536FAF6EE851BBE894139A079101D74BDFFE4A` | No phantom Dismantle control or clipped empty-state text. |
| 1920×1080, empty registry | [cropped PNG](after/locations_dismantle_empty_1920_final_cropped.png), `92690A783E21918C40BB91257E8019785E53EE0EA23E1F0C64FC64668D4B7519` | No phantom selected-site pane; empty message and navigation remain inside the frame. |
| 125%, closure in progress | [cropped PNG](after/locations_dismantle_progress_locked_125_cropped.png), `1FC6C63B5E7FC0521516824763318A81482961EA43090DBD4DD21BB0DF915FB9` | Zero living custody, 0% maintenance support and a neutral Closure Locked control fit with the status line. The first draft's 100% support at a closed site was rejected and corrected before archival. |
| 125%, closed by a separate order | [cropped PNG](after/locations_dismantle_custody_locked_125_cropped.png), `7B78F419B2B72FD0A0B3573C79519717BFEA3E733B0F994CDCBB7D6D0A14ACE1` | Closed zero-custody site and the custody/closure lock fit. The status line was revised to describe the separate closure order without implying an investigation. |

The normal 1920 and 1280 click-region resources returned `Artifact provenance manifest is unavailable` when read, despite `GUI_RENDERED` linking them; the later 125% targeted and locked click-region resources were retrieved in exact byte ranges and their saved SHA-256 values match MCP.
All retrieved PNGs were visually inspected after full range assembly; direct unbounded resource reads were rejected when the transport inserted an ellipsis into base64.

## Remaining acceptance limits

The renderer does not display the actual contextual tooltip or execute a native click, debit, mission timeout, release, or save/reload state.
The active, hover and resource-locked images were produced under different workspace graph revisions while other agents worked in the shared tree; their exact artifact/source identities are retained rather than presented as a single matched-source pixel diff.
The no-selection state now has inspected empty-registry PNGs at all three requested scales; the selected-site panel hides the button row. Progress and custody locked variants have inspected 125% images. A route-locked long-name/large-number/bottom-scroll stress fixture has inspected PNGs at all three scales. The first 1920 stress render returned `GUI_RENDERED` with cropped PNG SHA-256 `CE8DD51F7CD01D1BCE2F262C3165FF0D76388FD9781095A0D3B6886D9CBC372A`, but its resource read returned `Artifact provenance manifest is unavailable`; the no-hover sibling fixture was rerendered, retrieved and inspected with the hash above. The first 1280 and 1920 empty-hover artifacts had the same retrieval problem; no-hover sibling fixtures were used for verified images.
The parent owns final gameplay, cost, localisation, AI and package-only diff acceptance.
