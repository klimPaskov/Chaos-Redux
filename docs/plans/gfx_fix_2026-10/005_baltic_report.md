# Event 005 Baltic GFX Fix Report

## Final parent follow-up

The independent audit found Riga Corridor Switchyards visibly undersized at 64x60 inside its 94x86 canvas.
The parent accepted a complete original native-alpha painting with a rail junction, manual point lever, physical semaphore, blank dispatch panel and Riga harbor skyline.
Its visible subject is 88x79 with transparent margins of 3/3/3/4 pixels, and the installed DDS exactly matches the approved PNG.
The complete active tree retains 42 distinct 94x86 images, with 40 focus textures and ten legacy textures promoted and two focus textures retained.
Four current retained headers used inconsistent mip-count or depth fields and were normalized through the approved writer, preserving their entire BGRA payloads and decoded RGBA pixels.
The header receipt is `header_normalization_followup/parent_installed.json`, and all 42 active DDS files pass the canonical base-level header check.
The earlier 45-file receipt is the first promotion tranche, and the Riga follow-up receipt is `riga_followup/notes/parent_installed.json`.
The updated current 42-row crosswalk and full-tree sheet supersede the earlier seven-retained staging state.
The legacy Pan-Baltic normal/shine mapping remains blocked by the user size/frame-only `.gfx` rule, and final MCP rendering remains unavailable.
The Riga focus description's literal `Riga?s` was corrected to `Riga's` in isolated commit `b313c2a8d`.
For the live Riga check, use a paused 1936 LAT fixture, run `effect set_global_flag = { flag = chaos_tier value = 3 }` and `effect load_focus_tree = { tree = soviet_collapse_baltic_focus_tree }`, then hover Riga Corridor Switchyards.
Expect a full-size rail-control emblem with no lettering or colored fringe, and the description should display `Riga's`.
Repeat the tree review as EST and LIT for their country-only branches.
The earlier USA-only fixture cannot show all six tag-specific Baltic focuses.

**Disposition:** 50 reviewed runtime textures are installed; the legacy Warroom alias correction and final engine acceptance remain unresolved.

**Acceptance basis:** The parent task explicitly authorizes all Event 005 Baltic-family GFX review repairs and names the canonical reference root, row set, 94x86 target, native-transparency workflow, output ownership, and no-runtime/no-`.gfx` boundary.

**Status:** All Baltic per-sprite source repairs are independently reviewed and installed or verified as previously repaired, except the legacy Warroom alias mapping. The complete 42-focus tree also has a consistent 94x86 texture set, with 25 existing 100x88 focus files normalized in place at their registered texture paths. The direct Pan-Baltic legacy alias path remains parent-owned. All source, processed PNG, and DDS candidates are in `docs/assets/005_soviet_collapse/gfx_fix_baltic/`; the parent installed 50 runtime DDS textures after exact pixel proof; `.gfx`, focus, localisation and gameplay scripts were not changed.

The focus tree is `soviet_collapse_baltic_focus_tree` in `common/national_focus/005_soviet_collapse_republics.txt`. It contains 42 focus nodes. Matching labels and rewards were read from `localisation/english/005_soviet_collapse_l_english.yml` and the same focus source. The assets are grounded in their focus subjects: the Baltic Defense focus establishes a league defense charter, the Pan-Baltic War Room coordinates maps and reserves, the Tallinn-Riga-Vilnius Rotation shares the chair, German Border Pressure watches pressure from the southwest, and the Estonian Forest-Coast Guard joins coastal batteries and forest posts.

## Row-level outcomes

| Severity | Review sprite or row | Outcome |
| --- | --- | --- |
| 1 | `GFX_baltic_soviet_collapse_military_border_government` | Verified in the current direct DDS; its hash matches the previously accepted review output and magenta/green edge counts are zero. Its separate focus alias is installed at 94x86. |
| 1 | `GFX_baltic_soviet_collapse_german_border_pressure` | Replaced with original painted eagle-and-border-map art; the same clean subject is installed for the focus alias. |
| 1 | `GFX_baltic_soviet_collapse_no_retreat_from_the_capital` | Already resolved in the current direct DDS; accepted output hash and zero magenta/green edge counts verified. Its separate focus alias is installed at 94x86. |
| 1 | `GFX_baltic_soviet_collapse_latvian_port_guard_boards` | Already resolved in the current direct DDS; the focus alias also has zero magenta/green edge counts. |
| 1 | `GFX_baltic_soviet_collapse_coastal_defense_batteries` | Already resolved in the current direct DDS; accepted output hash and zero magenta/green edge counts verified. Its separate focus alias is installed at 94x86. |
| 1 | `GFX_baltic_soviet_collapse_the_border_front_at_home` | Already resolved in the current direct DDS; accepted output hash and zero magenta/green edge counts verified. Its separate focus alias is installed at 94x86. |
| 1 | `GFX_baltic_soviet_collapse_volunteer_rifle_societies` | Already resolved in the current direct DDS; accepted output hash and zero magenta/green edge counts verified. Its separate focus alias is installed at 94x86. |
| 1 | `GFX_baltic_soviet_collapse_university_volunteer_lists` | Already resolved in the current direct DDS; accepted output hash and zero magenta/green edge counts verified. Its separate focus alias is installed at 94x86. |
| 2 | `GFX_baltic_soviet_collapse_scandinavian_listening_mission` | Existing magenta spill was already cleared; the medallion is scaled to clear its top edge and installed for both direct and focus aliases. |
| 2 | `GFX_baltic_soviet_collapse_home_guard_staff` | Replaced by a coastal home-guard badge with a watch post, pine shore, and crossed rifles. |
| 2 | `GFX_baltic_soviet_collapse_restoration_pact` | Replaced by a blank treaty scroll, seal, and three recognizable Baltic flags. The original and rejected flag iterations are retained. |
| 2 | `GFX_baltic_soviet_collapse_pan_baltic_war_room` | The new legacy war-room DDS is installed but unconsumed; its normal and shine aliases still point to Home Guard. Their correction awaits an explicit exception to the user size/frame-only rule below. |
| 2 | `GFX_focus_baltic_soviet_collapse_baltic_defense_compact` | Replaced by three linked shields with a shared clasp and crossed rifles; no mountain duplicate remains in the staged focus DDS. |
| 2 | `GFX_focus_baltic_soviet_collapse_german_border_pressure` | Replaced by the painted eagle-and-border-map icon; the warning triangle and red arrows are absent. |
| 2 | `GFX_focus_baltic_soviet_collapse_latvian_port_guard_boards` | Already resolved in the current focus DDS; no magenta/green edge pixels remain. |
| 2 | `GFX_focus_baltic_soviet_collapse_tallinn_riga_vilnius_rotation` | Staged as three distinct city seals linked by a rotating chair, separate from the defense compact. |
| 3 | `GFX_baltic_soviet_collapse_british_naval_observers` | Scaled inward to clear the top edge and installed for the direct and focus aliases. |
| 3 | `GFX_baltic_soviet_collapse_baltic_recognition_dossier` | Scaled inward to clear the top edge and installed for the direct and focus aliases. |
| 3 | `GFX_baltic_soviet_collapse_the_port_economy` | One-pixel alpha erosion tightens the fuzzy edge; RGB remains byte-identical to the decoded source. |
| 3 | `GFX_focus_baltic_soviet_collapse_scandinavian_listening_mission` | Reframed to clear the top edge; its direct alias uses the matching installed pixels. |
| 3 | `GFX_focus_baltic_soviet_collapse_sponsor_fleet_rights` | Reframed to clear the top edge; direct and focus aliases share the matching installed pixels. |
| 3 | `GFX_focus_baltic_soviet_collapse_baltic_recognition_dossier` | Reframed to clear the top edge; its direct alias uses the matching installed pixels. |
| 3 | `GFX_focus_baltic_soviet_collapse_british_naval_observers` | Reframed to clear the top edge; its direct alias uses the matching installed pixels. |
| 3 | `GFX_focus_baltic_soviet_collapse_foreign_advisers_under_baltic_law` | Reframed to clear the top edge; direct and focus aliases share the matching installed pixels. |
| 3 | `GFX_focus_baltic_soviet_collapse_estonian_forest_coast_guard` | Replaced the small terrain vignette with a full coastal battery, forest watch post, and shoreline focus icon. |
| 3 | `GFX_focus_baltic_soviet_collapse_pan_baltic_war_room` | Replaced the mountain vignette with the staged map-table and officer icon. |
| 3 | `GFX_focus_baltic_soviet_collapse_baltic_defense_compact` | Replaced the mountain vignette with the staged three-shield defense icon. |

The reframe set covers Scandinavian Listening Mission, British Naval Observers, Baltic Recognition Dossier, Sponsor Fleet Rights, and Foreign Advisers Under Baltic Law. Their direct and focus source DDS files were pixel-identical at preflight; each final path has a separately named DDS output.

## Full focus-tree size normalization

The 42-focus audit found 25 original focus textures at 100x88 beside 17 at 94x86. All 25 oversized inputs were normalized with aspect-preserving premultiplied-alpha resampling inside an 88x80 fit window on a transparent 94x86 canvas. This preserves the original illustrations and registered paths. Original DDS bytes and decoded PNGs remain under `docs/assets/005_soviet_collapse/gfx_fix_baltic/source_dds/live/` and `source_png/runtime_decoded/`.

The resize exposed 111 confirmed green or magenta pixels on transparent subject edges; their RGB values were replaced from the nearest clean opaque interior pixel, with alpha unchanged and no erosion. The 25 final assets have 94x86 canvases, pass the configured focus bounds test, show zero chroma-edge pixels, and pass exact DDS round trips. After staging, all 42 registered Baltic focus textures measure 94x86. The focus IDs, exact registered paths, old and final hashes, bounds, margins, and DDS evidence are in `docs/assets/005_soviet_collapse/gfx_fix_baltic/notes/focus_100x88_normalization_all25.json` and `focus_tree_42_crosswalk.json`.


## Native-alpha production and flag review

The seven selected new subjects were produced through the built-in ImageGen tool with genuine transparency requested in the first call. The selected source PNGs retain zero-alpha corners; each selected processed PNG is 94x86 and preserves native alpha. No background-removal fallback, opaque background, fake checkerboard, component background, or cross-type resize was used.

The restoration pact and war-room prompts used the locally verified flag patterns: Estonia’s equal blue-black-white bands, Latvia’s carmine-white-carmine bands, and Lithuania’s equal yellow-green-red bands. Those patterns are documented by the [President of Estonia](https://president.ee/en/republic-of-estonia/symbols/index.html), [Latvian flag law](https://likumi.lv/ta/en/en/id/200642-law-on-the-national-flag-of-latvia), and [Lithuanian state-flag law](https://www.e-tar.lt/rs/legalact/TAR.07CAE5E6C2B3/). The restoration scroll is blank and the flags are distinct; the war-room flags are flat panels so their orders remain readable at native size.

The canonical focus reference contact sheet and selected individual Vanilla references were inspected before generation. The visual-component contact sheets were reviewed and the catalog marks those pieces as references, so none was layered into the art. The installed Vanilla `GFX_goal_generic_major_alliance` sprite points to `goal_generic_major_alliance.dds` (89x79); it served as a style precedent, while the task’s 94x86 target was kept for all staged outputs.

## Verification evidence

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` and status `ok` for `soviet_collapse_baltic_focus_tree`, with 42 focus nodes and no blockers. It reported five unrelated Baltic layout-detour warnings and one generic continuous-focus localisation-reference warning. The saved inspect result and manifest are in `notes/mcp_focus_inspect.json` and `notes/mcp_focus_inspect.manifest.json`.
- `hoi4.focus_raster` returned `FOCUS_RASTERIZED`, validation passed, and produced a 4176x1280 baseline tree image at review scale 1. Its SHA-256 is `ae9f5e2a7957203fe516fbe1f55d6f175d8d8c73d9cd599584b03e173de69220`; the image and manifest are saved under the package. The response also reported `MCP_RESPONSE_TRUNCATED` because its JSON exceeded the wire limit, but the PNG artifact was present locally and hash-verified.
- `contact_sheets/before_native.png` and `contact_sheets/after_native_final.png` match the supplied 168-pixel checker-sheet style and stay limited to the Baltic review sprites. `contact_sheets/full_42_baltic_focus_tree_before.jpg` and `full_42_baltic_focus_tree_after_final.jpg` show all 42 focus consumers before and after normalization; every after tile reports 94x86.
- `contact_sheets/before_changed_contrast.png` compares the affected pre-change DDS assets on checker, dark, and light backgrounds. `contact_sheets/qa_final_lineage_roundtrip_v2.png` shows source, processed PNG, decoded DDS, and enlarged smooth preview; `contact_sheets/qa_final_contrast_v2.png` shows final DDS round trips on checker, dark, and light backgrounds.
- All 38 unique processed PNGs pass the alpha and focus-size audits in `notes/alpha_audit_final.json` and `notes/size_audit_final.json`. They retain full alpha, have zero chroma-edge pixels, and have no 94x86 size findings.
- All 45 staged DDS outputs pass the exact 128-byte uncompressed BGRA header, 94x86 dimensions, alpha range, no-mipmap, and pixel-identical PNG round-trip checks in `notes/dds_validation_final.json`.
- The nine current direct DDS files with accepted 005 contact-sheet outputs match their recorded `output_sha256` values, and their current edge measurements show zero magenta and green pixels; see `notes/previous_review_match.json`.

## Parent-side wiring and remaining review

The direct Pan-Baltic normal and shine sprites are the only identified path blocker. In `interface/005_soviet_collapse.gfx`, lines 848 and 1252 both point `GFX_baltic_soviet_collapse_pan_baltic_war_room` and its `_shine` alias at `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_home_guard_staff.dds`. The staged direct war-room file is `gfx/interface/goals/005_soviet_collapse/baltic_soviet_collapse_pan_baltic_war_room.dds`; the proposed repair is to point both aliases at that path. The user expressly restricts .gfx edits to size or frame changes, so this two-path exception was asked asynchronously and has not been authorized. No registry edit was made. The focus-tree Pan-Baltic sprite already has its separate registered path and staged focus DDS.

No `.gfx` size or frame adjustment is required for the staged 94x86 outputs. The seven previously resolved direct S1 rows and the focus Latvian Port Guard Boards row keep their accepted pixels; all 25 focus textures that had measured 100x88 now have consistent 94x86 staged outputs. Every Baltic per-sprite artwork repair is implemented apart from the blocked legacy Warroom consumer mapping. The legacy Pan-Baltic alias path correction remains pending; all 50 reviewed files are installed, including the unused legacy Warroom texture. The active focus-prefixed Warroom already uses its correct installed texture.

## Scope and untouched findings

No visual-content fallback or simplification was used. All 42 active focus textures have consistent 94x86 dimensions. The legacy Warroom row remains unresolved because its registry aliases still consume Home Guard. The staged focus normalizations preserve source illustrations and alpha while repairing only confirmed chroma-colored edge RGB. The direct Pan-Baltic normal and shine path correction remains the sole parent-owned integration dependency.

The parent reviewed all 42 focus tiles and the 25 normalized dark/light contrasts, then installed 50 DDS files with source-hash guards and exact approved-PNG equality. The saved MCP inspect and raster remain baseline evidence; the correct post-installation named-tree raster returned Transport closed. final_mcp_failure.json retains that result. No .gfx, focus or gameplay script was modified. The only localisation edit corrects the Riga possessive punctuation. No game was launched. The unresolved legacy alias correction and unavailable final MCP view prevent a full Baltic completion claim.

## Orchestrator live checks

Use a separate paused 1936 USA session at 1920x1080 and UI scale 1.
Run `effect load_focus_tree = { tree = soviet_collapse_baltic_focus_tree }` and open the tree at normal and close zoom.
Inspect all 42 icons and hover their available, unavailable and shine states; expect consistent framing and no colored halo or clipped subjects.
Defense Compact should show three shields and rifles, Pan-Baltic War Room officers and a map table, Tallinn-Riga-Vilnius Rotation three architectural city seals, German Border Pressure a painted border map and eagle, and Estonian Forest-Coast Guard a coastal battery and forest.
Restoration Pact and War Room must show Estonia blue-black-white, Latvia carmine-white-carmine with a narrow white stripe, and Lithuania yellow-green-red.
The active focus War Room is correct; the legacy GFX_baltic_soviet_collapse_pan_baltic_war_room alias still shows Home Guard until the pending path correction is authorized.
