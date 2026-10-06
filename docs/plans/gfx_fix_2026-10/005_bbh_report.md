# Event 005 BBH focus icon repair report

## Status

The parent reviewed and installed all 47 BBH focus textures at their existing runtime paths.

All 47 focuses have a source PNG, processed 94x86 PNG preview, staged DDS, exact sprite-alias mapping, manifest entry, and handoff.

Forty-six final source PNGs use native-alpha ImageGen outputs and retained prompts: 43 direct generations and three focused ImageGen edits.

The bespoke endgame artwork is the one retained source DDS; the birth wing-and-star identity is preserved in a new balanced framed icon.

There are no asset-generation or DDS-conversion blockers.

Runtime promotion is verified in parent_installed.json; final MCP raster and live acceptance remain blocked or pending.

## Findings and implementation

The BBH row at line 187 of the supplied `gfx_fix_plan.md` reports 46 of 47 duplicate focus icons and identifies the endgame texture as bespoke.

That row is implemented in the runtime textures: the newly framed birth identity art remains only on `BBH_birth`, `BBH_endgame` retains its existing design, and the other 45 foci have distinct generated art tied to their focus wording and reward blocks.

The retained endgame art was normalized from 100x88 to the exact 94x86 consumer canvas without changing its design.

The existing BBH normal and shine sprite names remain unchanged; each maps to the same established runtime DDS path shown in the manifest crosswalk.

The parent replaced the 47 runtime DDS textures; focus definitions, localisation, gameplay scripts and sprite registrations were not edited.

All generated sources requested genuine transparent backgrounds in their first ImageGen calls.

The accepted generated sources have true alpha, and the final processed PNGs preserve that alpha through contour cleaning and premultiplied resize.

No opaque-background removal, chroma background, fake checkerboard, reference-layer compositing, or transform-only substitute was used.

The canonical national-focus contact sheet was inspected first, then matching vanilla focus references, followed by the visual-components catalog and the focus-piece and focus-background contact sheets.

The component shelf remains reference-only; the icons were generated as original complete focus art.

The installed `GFX_goal_generic_national_unity` sprite and `goal_generic_national_unity.dds` were inspected as the exact 94x86 vanilla precedent.

## Supplied cross-cutting issue dispositions

| Rule | BBH disposition |
| --- | --- |
| 1. Chroma-key focus-icon fringe | The accepted BBH sources were processed with one-pixel external-contour erosion, interior-color bleed for semitransparent outer-edge pixels, premultiplied resizing, and native-size checker/dark review; no background-removal fallback was needed. |
| 2. Whole focus trees on one placeholder | All 47 runtime textures were installed: 46 generated final icons and one retained bespoke endgame design. |
| 3. Foreign flags, coats of arms, and foreign lettering | No foreign or national flags, coats of arms, letters, or readable lettering remain in accepted BBH art; circled-A-like league tokens were replaced, and the anti-protectorate apparent mark was confirmed to be envelope-fold shading. |
| 4. Ghosted alpha | Every processed icon has alpha range 0-255 and mean alpha above 200 across visible pixels; the stricter DDS decode check confirms the range is preserved. |
| 5. Unit-counter conventions | Not applicable to BBH focus icons. |
| 6. Decision-category icon sizing | Not applicable to BBH focus icons. |
| 7. Report and news picture house style | Not applicable to BBH focus icons. |
| 8. Baked text and logos | No lettering, labels, logos, or watermarks remain in accepted BBH artwork; the revised blank wax seal and rejected league candidates are recorded in candidate lineage. |
| 9. Painted miniatures in flat-pictogram families | Not applicable; these are national-focus icons and follow the inspected painted focus-icon family. |
| 10. Oversized or mis-sized assets | All 47 staged targets are 94x86; the existing 100x88 endgame art is normalized to the exact consumer canvas. |
| 11. Debug overlays and modern UI glyphs | No debug overlays, neon UI marks, or modern glyph overlays are present. |
| 12. Achievement state variants | Not applicable to BBH focus icons. |
| 13. Undersized or clipped subjects | All processed subjects fit inside the 94x86 canvas with at least a 3 px transparent margin and no clipped alpha bounds; the birth identity was reframed, and the retained endgame emblem preserves its original tall aspect ratio. |
| 14. Portrait set consistency | Not applicable to BBH focus icons. |
| 15. Frame-animation continuity | Not applicable; no animated icon was requested. |
| 16. Stale wholesale GFX overrides | No GFX file was edited; existing stable sprite registrations remain in place. |

The BBH asset row and relevant cross-cutting art fixes are installed; this is not full focus-tree or Event 005 completion.

Cross-cutting findings for other event tags and asset families remain outside this subtask.

## Source review and visual coverage

The manifest records the exact focus id, title, description, completion-reward block, planned subject, palette family, source PNG, prompt path, processed PNG, normal and shine aliases, staged DDS path, runtime target, and hashes for all 47 nodes.

The visual subjects reflect actual BBH wording and rewards, including tachanka columns, captured depots, broken ministry authority, mobile courts, prison escapes, commune assemblies, rail sabotage, and the black-banner endgame. A post-staging parent review found that the league house tokens read as circled As and the birth emblem was underframed. The league tokens were replaced by blank commune seals and the birth identity was widened into a framed medallion. The anti-protectorate seal was also revised to a blank wax disk; parent review confirmed its apparent native A was envelope-fold shading, not lettering. The rejected candidates remain preserved, and the regenerated 47-icon native and enlarged sheets were audited again.

Military, industry/logistics, political/commune, diplomatic, and high-chaos icons use distinct accent palettes while sharing aged painted relief and the Black Banner Host identity.

The accepted league icon uses three smooth unmarked commune seals linked by thick cord around a central knot, with no letterforms.

The free-city icon was revised from medieval imagery to a period municipal gate and mounted column.

The full accepted set has a row-level visual symbol audit in `evidence/symbol_audit.json`, and rejected candidates with exact prompts remain hash-listed in `evidence/candidate_lineage.json`.

The birth source contains only its requested wing, standard, and single-star identity motif; the anti-protectorate seal is blank and the three league seals are unmarked.

## DDS and asset validation

The bundled `convert_to_dds.py` converter produced all 47 files as one-level, uncompressed BGRA32 DDS textures.

Every staged DDS has the standard 128-byte header, 94x86 dimensions, exact BGRA channel masks, `DDSCAPS_TEXTURE`, no mipmaps, and a 32,464-byte length.

Every DDS decodes pixel-for-pixel equal to its processed PNG and preserves alpha range 0-255.

All 47 source PNG hashes, staged DDS hashes, and decoded-pixel hashes are unique.

The row-level crosswalk passes for all 47 focus consumers and 94 registered normal/shine aliases.

The ignored Git status is expected because `.gitignore:80` ignores `docs/assets/`; the parent owns any later force-add and commit after review.

## HOI4 MCP evidence and limits

The bounded read-only `hoi4_focus_inspect` succeeded for `BBH_soviet_collapse_focus_tree` and reported 47 focuses with no blocking diagnostics.

The initial focus raster succeeded at 3824x1744 and showed the duplicated emblem across the BBH tree before this asset pass.

The inspection reported two existing linear-detour warnings, from `BBH_anti_protectorate_letters` to `BBH_temporary_free_city_pacts` and from `BBH_enemy_front` to `BBH_war_plan`; this task did not alter focus layout.

The inspection also reported an unrelated missing `continuous_restrict_freedom_desc` localisation key in the vanilla continuous-focus source; this task did not alter that file.

The parent attempted the same named-tree raster after installation; the route returned `Transport closed`. The exact failed result is retained in final_mcp_failure.json. No post-promotion MCP render or in-game acceptance is claimed.

## Parent review and promotion

Review `docs/assets/005_soviet_collapse/gfx_fix_bbh/previews/after_native_checker.png`, `after_native_dark.png`, and `after_enlarged_review.png`, together with the manifest, candidate lineage, symbol audit, coverage audit, and DDS round-trip receipt.

The parent promoted the 47 staged DDS files from `docs/assets/005_soviet_collapse/gfx_fix_bbh/runtime/` to the exact targets under `gfx/interface/goals/005_soviet_collapse/` shown in the handoff crosswalk.

No `.gfx` edit is required because the existing normal and shine aliases already resolve to those target filenames.

The parent completed runtime promotion and owns the focused commit; the orchestrator owns live-game validation.

## Simplifications, omissions, and blockers

No requested BBH focus icon is missing from the installed package, and no generic or unrelated icon was used as a substitute.

The birth identity is preserved in a new framed ImageGen edit, while the bespoke endgame art is the only retained design; all other focus slots use generated subject art.

Remaining acceptance work is the unavailable post-change MCP render and the orchestrator live checks below.

Skills used: chaos-redux-event-assets, chaos-redux-focus-trees, and the official ImageGen skill; no skill files were changed.

## Orchestrator live checks

Use a separate paused 1936 USA session at 1920x1080 and UI scale 1.
Run `effect load_focus_tree = { tree = BBH_soviet_collapse_focus_tree }` and open the focus tree.
Inspect every branch at normal and close zoom, then hover available and unavailable focuses and inspect their shine state.
Expect distinct commune, tachanka, logistics, diplomacy and military subjects; only Birth carries the original identity motif, the league seals and anti-protectorate seal carry no letters, and the endgame retains its bespoke black-banner design.
Every subject should be centered without clipping or a colored halo on the game background; stable sprite names must retain normal hover and shine behavior.
