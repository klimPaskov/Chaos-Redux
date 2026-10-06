# AOX focus icon repair report

The 47 AOX focus slots now have individually generated, native-alpha icon packages installed at their existing runtime paths. The parent reviewed all 47 native-size DDS sheets and selected the arc-free AOX_extreme_path revision. Each selected focus has a source PNG, exact prompt record, 94x86 processed PNG, staged DDS, current sprite/runtime crosswalk, native-size review evidence and strict DDS roundtrip evidence.

## Scope and output

The live consumer is AOX_soviet_collapse_focus_tree in common/national_focus/005_soviet_collapse_custom_splinters.txt. The existing registry interface/005_soviet_collapse_focus_icons.gfx defines 47 base sprites and 47 shine aliases; the matching runtime paths are gfx/interface/goals/005_soviet_collapse/focus_005_aox_<suffix>.dds.

The package contains 60 retained native-alpha ImageGen candidates for 47 unique focus slots, 47 final processed PNGs and 47 staged DDS files under docs/assets/005_soviet_collapse/gfx_fix_aox/. Every focus has its own prompt and original source artwork. The anchor-star identity emblem is used only for AOX_birth.

The final art is staged beneath docs/assets/005_soviet_collapse/gfx_fix_aox/staged_runtime/gfx/interface/goals/005_soviet_collapse/. The staged-to-runtime crosswalk is docs/assets/005_soviet_collapse/gfx_fix_aox/staged_to_runtime_crosswalk.csv. The parent replaced all 47 runtime DDS files after independent source, native-size and pixel review; no .gfx, national-focus, localization or gameplay script was edited.

## Reference and consumer evidence

The canonical national-focus contact sheet at .agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/national_focus/contact_sheet.png was inspected before its individual references. Focuses aus_reestablish_austrian_navy, aus_danubian_socialist_communes, bra_ulasr and eth_expand_the_levy informed the aged, painted HOI4 emblem treatment. The canonical reference family uses 100x88 images; the exact current AOX DDS consumer is 94x86, and the parent prompt explicitly set 94x86, so every final PNG and DDS uses 94x86.

The matching focus_pieces and focus_backgrounds component contact sheets and CATALOG.md were inspected as reference material only. No canonical GFX image or component source was copied, recolored or layered into the final icons.

The installed vanilla reference interface/goals.gfx defines GFX_goal_generic_navy_battleship at line 566 using gfx/interface/goals/goal_generic_navy_battleship.dds; that DDS was decoded and visually inspected at 82x82. A workspace-index source_lookup query returned zero installed-game definitions, so the exact installed definition and texture were read directly from the Steam game directory.

## Verification

The baseline had 47 live AOX texture paths but only one unique DDS file hash and one unique decoded-pixel hash. The staged package has 47 unique DDS hashes and 47 unique decoded-pixel hashes.

All 47 DDS files passed strict 94x86 header, BGRA pixel-format, alpha, exact 32,464-byte file-length and PNG-to-DDS pixel-equality checks. The verifier checked DDS magic, 124-byte header, flags 0x100F, 32-bit BGRA masks, texture caps 0x1000, zero mipmaps and decoded alpha/pixels. The detailed results are in docs/assets/005_soviet_collapse/gfx_fix_aox/notes/dds_roundtrip_report.json.

Native review sheets show the before and after icons on checker and dark backgrounds, with an enlarged smooth set. Separate DDS roundtrip sheets show each decoded texture at native size on both backgrounds; lineage sheets show the selected ImageGen source, processed PNG, enlargement and DDS decode together. All 47 subjects were reviewed individually at source resolution and native 94x86.

Source alpha remained native and true through processing. The crop threshold only excluded isolated source alpha below 8 outside the visible subject; alpha inside the crop was retained. Aspect ratio was preserved when fitting into an 88x80 content box. The conditional edge-color pass changed RGB only on 12 visually confirmed partial-alpha edge pixels where magenta/green color disagreed with the nearest opaque interior; all alpha bytes and core RGB remained unchanged, and no alpha erosion was applied.

The required focus inspect and raster routes both completed successfully for the named AOX tree. MCP workspace and artifact identifiers are recorded in docs/assets/005_soviet_collapse/gfx_fix_aox/notes/mcp_evidence.md. The inspect found 47 focuses. The initial raster request included an invalid columns parameter for national mode; the retry without columns succeeded and its image was reviewed.

## Plan dispositions

The relevant plan rows are in C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md.

| Plan row | Disposition |
| --- | --- |
| Line 101, cross-cutting 005/015 chroma-edge finding | Addressed for the AOX generated set with a selective edge RGB pass, unchanged alpha and post-correction dark/checker review. The direct AOX placeholder row itself did not identify chroma as its defect; this issue came from the separate cross-cutting row. Other focus families named there remain outside this AOX handoff. |
| Line 102, 005 trees reusing one placeholder | Addressed for AOX: 47 individually generated focus subjects replace the repeated texture in the installed textures. Other trees named in that backlog remain outside this package. |
| Line 186, GFX_focus_AOX_birth placeholder row | Addressed for all 47 current AOX focus slots. The plan suggests 100x88 art and keeping the anchor-star for birth/legitimacy identities; this package follows the exact 94x86 live AOX consumer and the parent instruction to retain the anchor-star only on birth. |

Five suffixes in the old plan list differ from current focus ids and registry names: icebound_supply maps to icebound_supply_ledger; petrograd_signal maps to petrograd_signal_watch; red_fleet_signal maps to red_fleet_signal_posts; sailor_worker_deputies maps to sailor_worker_defense_council; sailors_assembly maps to sailors_assembly_registers. The handoff follows the live registry and consumer paths exactly.

## Review state and remaining work

No AOX focus slot is blocked or omitted. The parent promoted all 47 reviewed rows and independently verified installed hashes and decoded pixels. The post-installation named-tree raster returned Transport closed; final_mcp_failure.json retains the exact failure. No post-change MCP visual or live-game acceptance is claimed.

No fallback art, generic icon, reused cross-type artwork or atlas-derived slot was used. The only design adjustments were the documented per-candidate revisions, the exact consumer size, and the parent-directed edge correction. The complete candidate lineage, source inventory, manifest and GFX handoff are in docs/assets/005_soviet_collapse/gfx_fix_aox/.

## Orchestrator live checks

Use a separate paused 1936 USA session at 1920x1080 and UI scale 1.
Run `effect load_focus_tree = { tree = AOX_soviet_collapse_focus_tree }` and open the focus tree.
Inspect every branch at normal and close zoom, then hover available and unavailable focuses and inspect their shine state.
Expect distinct naval, industrial, assembly, communications and diplomacy subjects; the anchor-star identity appears only on Birth, Extreme Path uses physical harbor lamps without neon arcs, and the endgame shows a fortified harbor rather than a UI selector.
Every subject should be centered without clipping or a colored halo on the game background; stable sprite names must retain normal hover and shine behavior.
