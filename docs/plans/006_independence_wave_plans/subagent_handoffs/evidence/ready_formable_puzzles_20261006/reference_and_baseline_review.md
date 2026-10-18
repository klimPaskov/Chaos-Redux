# Event 006 formable puzzle reference and baseline review

Disposition: The source baseline and four map-projection references are preserved. The live whole-window visual gate remains open because current GUI MCP inspect and render routes returned SCAN_PATTERN_LIMIT without artifacts.

## Ownership and accepted surface

The accepted Event 006 Part 6 contract identifies the grouped formable state-puzzle consumer as group_id = independence_wave_formables, group_scripted_gui_id = independence_wave_formable_state_puzzle_scripted_gui, and group_window_id = chaosx_independence_wave_formable_state_puzzle_window.

The resolved production layout is interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui; the expected _independence_wave.gui filename is absent.

The live source lookup resolves the named window to a top-level containerWindowType at lines 7-737 of that file and resolves the scripted-GUI binding to common/scripted_guis/chaosx_formable_state_puzzles.txt:1372-1601, with context_type = decision_category.

The parent accepted four family additions, FORM17, FORM32, FORM36, and FORM37, while retaining the existing fifteen family layouts and grouped decision-category presentation.

The parent and contract worker own the route and integration decision categories, activation and qualification triggers, assets, GFX, scripted-GUI helper wiring, and all gameplay behavior; this worker's only potential source edit remains the Event 006 group layout file.

## Preserved current-source baseline

The current 15-family layout SHA-256 is 4A246C87345B83B6A1AB3BFE3C890C7EBAF2BDDC60772464F04E5252CAA7A9B8.

The current grouped scripted-GUI file SHA-256 is B44B260DFF0409BBCABC89CEEABFCE4C5F958BBADE32D86AF5B4E331849C604F.

Frozen copies are baseline_layout_before_parent_generation.gui and baseline_scripted_gui_before_parent_generation.txt; the source-derived family and state-position map is baseline_source_mapping.json.

The present window root is clipped at 440 x 206; every family overlay shares the same (0,0) bounds, the centered summary occupies 440 x 22 at y = 0, and the clipped state map occupies 440 x 180 at y = 24.

The baseline contains fifteen overlays and 52 state-piece iconTypes across FORM01, FORM02, FORM03, FORM04, FORM05, FORM07, FORM08, FORM09, FORM11, FORM12, FORM13, FORM16, FORM18, FORM39, and FORM48.

The state-to-position crosswalk is in baseline_source_mapping.json; every state piece maps to a dynamic unresolved/qualifying sprite name and its delayed state tooltip, with overlay visibility driven by one family activation helper.

This is an informational surface with no buttons or primary actions; the state silhouettes are hover targets through pdx_tooltip_delayed.

The exact source-bound layout budget is one top summary and one map region; the only cross-family display risk is overlapping co-located overlays if more than one family activation fires in a fixture.

## Selected map-projection references

The four unresolved and qualifying projections were viewed at native 440 x 180 from docs/formables/state_puzzles/006_form17_state_puzzle/, 006_form32_state_puzzle/, 006_form36_state_puzzle/, and 006_form37_state_puzzle/.

Each unresolved preview shows the existing grey diagonal hatch; each qualifying preview shows the existing green solid fill with the same exact-alpha state outlines.

These images are selected as map-region references for the accepted existing window pattern; they are not claimed as whole-window MCP captures.

The new geometry manifest paths, SHA-256 values, state positions, dynamic qualification hooks, and expected DDS names are recorded in new_geometry_reference.json.

All 28 DDS assets referenced by the four manifests exist under their declared runtime paths and match their manifest SHA-256 values.

FORM17 uses states 232, 821, and 827 at (207,8), (198,66), and (108,61) respectively.

FORM32 uses states 440, 442, 443, 986, and 1012 at (194,37), (195,8), (153,111), (240,56), and (138,100); states 440 and 986 each have a distinct visibility helper and represent mutually exclusive stored-anchor branches.

FORM32's union projection intentionally contains both anchor silhouettes as a geometry reference; a runtime family view must show only the stored 440 or 986 anchor together with the common states 442, 443, and 1012.

FORM36 uses states 673, 1050, and 1052 at (323,90), (63,8), and (275,162).

FORM37 uses states 994, 998, and 999 at (212,86), (197,8), and (214,43).

The state images remain presentation-only assets; the accepted root map bounds, hatching, green qualification treatment, and generic one-summary/one-map hierarchy are preserved.

## Source-derived fixture inputs for the later post-integration render

The GUI route rejects an actor field in scenario; the live validation message is Unrecognized key: actor at scenario.

The supported GUI scenario comment exposes flags, variables, controls, values, and visibility; closedFlags = true is therefore used to isolate named context and piece flags.

The contract worker reports the four activation flags as has_independence_wave_form17_puzzle_context, has_independence_wave_form32_puzzle_context, has_independence_wave_form36_puzzle_context, and has_independence_wave_form37_puzzle_context.

The finite piece flags are has_independence_wave_form17_state_puzzle_piece_{827,821,232}, has_independence_wave_form32_state_puzzle_piece_{440,986,443,1012,442}, has_independence_wave_form36_state_puzzle_piece_{1050,673,1052}, and has_independence_wave_form37_state_puzzle_piece_{994,999,998}.

The contract worker confirmed that FORM32 primary and secondary flags are mutually exclusive against stored anchor 440 or 986.

These fixture fields will be supplied as declared source-derived render inputs, not as observed game saves or runtime results.

## Live baseline route and historical artifact limits

hoi4.gui_inspect was called for chaosx_independence_wave_formable_state_puzzle_window with scenario E6_FORMABLE_GUI_BASELINE_FORM16_CXT_20261006, closedFlags = true, independence_wave_formable_family = 16, independence_wave_formable_profile_family = 16, and invitation family 0.

The first request included actor = CXT and was rejected by schema validation; the second, corrected request returned SCAN_PATTERN_LIMIT with no artifact and no source-level window analysis.

One matching hoi4.gui_render request used that corrected fixture at 1920 x 1080 and 1366 x 768, each at uiScale = 1, with states normal, hover, active, long-text, and missing-localisation; it also returned SCAN_PATTERN_LIMIT with no artifacts.

No current-source whole-window PNG, crop, annotation, hierarchy, click-region, fidelity report, or validation JSON was emitted.

The older 2026-08-15 FORM12/FORM13 GUI handoff is historical only: it records a different layout SHA-256, a stale source revision, aggregate nine-image output instead of one-family isolation, generic unresolved dynamic labels, and no separate crop, annotation, hierarchy, click-region, or comparison artifact.

Attempting to retrieve its stored SVG through the artifact resource template returned Artifact provenance manifest is unavailable; that older visual cannot be reviewed or used as a current baseline.

The visual acceptance gate is intentionally unresolved pending current-source post-generation family renders and matching comparison evidence.

## Reference and source records

Offline wiki Interface modding - Hearts of Iron 4 Wiki.md, revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c, was read at lines 178-195 (iconType) and 196-225 (instantTextBoxType).

Offline wiki Scripted GUI modding - Hearts of Iron 4 Wiki.md, revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30, was read at lines 40-67 (Window assignment), 144-164 (Context), and 549-628 (Template).

Installed documentation C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md, revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838, was read at lines 1-80 for decision-category context and dynamic properties.

The vanilla AST_cabinet_trust_ui scripted GUI is a relevant precedent: common/scripted_guis/AST_cabinet_trust_scripted_gui.txt:1-23 uses context_type = decision_category, a named container, and property-bound dynamic images, while interface/AST_cabinet_trust_scripted_gui.gui:4-95 defines the container and five state-image regions with associated tooltip regions.

hoi4.source_lookup resolves the Event 006 group window at source-location revision 5b4ab26ceb36ec681b6d9250b521b177889cf185ba7fddd04fd17c554f7ac4ed and the grouped scripted GUI at workspace-index revision c40c1410b0c6e5042cc85d79c6c5fad7170c8f6f6b209688f4d2c0ee21cb60f5.

hoi4.source_lookup resolved the FORM16 activation helper at workspace-index revision 9d5374a506e0d887a4bd21b5e9351789021cdfd39c38002eedccf430697ae182; direct source confirms the family constant is 16.

The hoi4.source_lookup search for the FORM16 sprite getter returned no indexed definition, so its source was verified directly in common/scripted_localisation/chaosx_formable_state_puzzles.txt:19680-19690 and its static GFX pair in interface/chaosx_formable_state_puzzles.gfx:2868-2875.

No production GUI source was edited during this baseline and reference pass.
The transparent PNG and DDS bounding rectangles have these within-family intersections, which are review targets for the later production click-region evidence and are not treated as defects without rendered hit-region proof: FORM17 states 232/821 overlap by 68 x 72; FORM32 states 440/442 by 36 x 16, 440/443 by 8 x 4, and 443/1012 by 19 x 30; FORM37 states 994/999 by 28 x 12 and 998/999 by 21 x 24.

The FORM32 440/986 mutually exclusive anchor pair is excluded from that intersection list; its alternate visibility is verified with separate render fixtures after helper wiring.
## Render fixture interpretation

The contract worker confirmed that each per-state state_puzzle_piece helper is a scripted qualification trigger that selects the qualifying green asset when its exact admitted package owns and controls the stored capital anchor and meets the root connection rule; the family puzzle_context helper selects the active family overlay.

These helper names are not country flags and will not be placed in scenario.flags or reported as gameplay results.

For layout-only color inspection, the parent authorized the live GUI scenario visibility/value override mechanism. Any forced overlay or dynamic sprite result will be labelled a declared visual assumption.

The contract worker is correcting the new helper owner-scope selection; those source changes remain outside this GUI worker's ownership and must be re-read before any claim about their behavior.

FORM32 anchor visibility is a separate concern from green qualification: the chosen stored anchor must remain visible while the other anchor stays hidden even when the chosen state is not controlled, while qualifying color still depends on actual control.
At the time these references were captured, the four geometry manifests still named the earlier generated activation and qualification helpers. The parent owns their mapping to the current contract worker triggers and may update those manifest fields before compiling the group layout; final review must use the post-integration source hashes.

The contract worker confirmed the stored-anchor selectors are has_independence_wave_form32_fdx_primary_puzzle_anchor_selected and has_independence_wave_form32_fdx_secondary_puzzle_anchor_selected. They resolve the FDX row and stored anchor independently of qualification, so the unqualified chosen anchor remains visible and the other anchor is hidden.
All declared new state-piece bounding boxes fit inside the 440 x 180 map canvas: FORM17 union is (108,8)-(331,171), FORM32 is (138,8)-(301,171), FORM36 is (63,8)-(376,171), and FORM37 is (197,8)-(242,171). This is a source/manifest bounds check, not a rendered-crop acceptance result.

## Parent integration and owned layout insertion

The parent completed the shared GFX, scripted-GUI, scripted-localisation, English localisation, and updated FORM32 manifest integration before the owned layout patch; those shared files remain outside this worker's ownership.

The accepted source candidate was C:/Users/klimp/AppData/Local/Temp/chaosx006_commit_30aa171c19e145228e008e7b3852440e/puzzle_generation/interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui.

A text diff against the frozen 15-family source contained only four added overlays, FORM17, FORM32, FORM36, and FORM37, with zero replaced or deleted lines; after applying those insertions, the owned production file matches the candidate byte-for-byte.

The post-integration production layout SHA-256 is D04C17EF591E6D4A2BED092FEFAA4D2ACD344E7BD4A403E240AE5A2A6F094D1F; a frozen copy is layout_after_parent_generation.gui.

The resulting layout has 19 family overlays and 66 state-piece iconTypes, preserving the original 15 overlays and 52 pieces and adding exactly 14 new pieces.

The current source lookup locates the window at interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui:7-931 with source-location revision 57b7108a84af6aabc8b06fc05787477108eca61dd09af9fc10b5e5bd69a6c147.

The current grouped scripted-GUI definition is at common/scripted_guis/chaosx_formable_state_puzzles.txt:1372-1665 with workspace-index revision d7f2c58814e3a187bc2df24641613e881132c6259b937b75a7e20cbd89b45288.

The final FORM32 source binds independence_wave_form32_state_440_piece_visible and independence_wave_form32_state_986_piece_visible to the separate primary and secondary stored-anchor selectors; the manifest records those same helpers independently from state qualification.

The current post-integration GFX, scripted-localisation, English localisation, new family triggers, and manifests are identified by their SHA-256 values in the takeover handoff and post_integration_manifest_audit.json.

## Current-source MCP result

After the production layout insertion, one exact window inspect used a closed-flags, explicit-visibility FORM17 scenario with generated scenarios disabled; it returned SCAN_PATTERN_LIMIT before source or element inspection, with zero artifacts.

One matching current-source render used the same FORM17 unresolved layout-assumption scenario, explicit source-derived sprite outputs, 1920 x 1080 at uiScale 1, normal and hover states, and the frozen pre-generation source as sourceBaseline; it returned the same SCAN_PATTERN_LIMIT with zero artifacts.

The exact requests and results are preserved in after_source_mcp_route.json.

Because the current source route failed before rendering, no current-family PNG/SVG, resolution matrix, crop, hierarchy, hit-region, hover tooltip, fidelity report, comparison image, or validation JSON exists.

The requested remaining FORM17 qualifying, FORM32 primary/secondary anchor and color, FORM36, FORM37, and 1366 x 768 cases were not run after the identical source-scan blocker; they are unresolved rather than presumed to match.

The source and projection bounds are reviewable, but the production GUI visual gate remains open and this handoff does not claim family-isolated visual acceptance or in-game completion.
