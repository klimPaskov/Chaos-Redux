# Main Menu Layout and Native Logo Restoration

## Result and acceptance

The original 2560×1440 logo anchor and native rendering from `06e4c5aaa7` are restored.
The exact combined request remains incomplete: the current foreground panel exposes more of the wrist than the original reference, and the native icon is larger than the requested current-size 1080 logo.
This is the temporary restoration explicitly authorized by the user's fallback instruction, not acceptance of either deviation as a finished design.
The accepted reference was corrected by the user to the original May layout, before `13b8fabb9e`; `d6d0087de4` is not the accepted reference.
The user authorized isolated Linux captures, changes to both Linux settings files with byte-exact restoration, and a shared-index-safe commit.

## Resumed constraint audit — 12 October 2026

The resumed instruction permits further implementation only when it can satisfy the original targets without changing the agreed artwork or protected controls and layout; the fallback must remain until a better candidate has actual verification.
The working frontend GUI is byte-identical to `9e43b45002` (Git blob `004525461a4ae7f105099f479740afa6eb6270ef`), and the logo DDS and GFX definition have no changes from that restoration.
There are no concurrent edits in the owned GUI, GFX, or report paths.
The current source still declares a 355 px bottom-anchored panel, while the original reference declares 410 px with the same -10 offset, retaining the measured 55 px occlusion difference.
The original 1440 pose fixes the artwork's position and sampling; changing position or size to conceal the additional wrist changes the required reference pixels.
Clipping alone cannot recreate the reference's translucent foreground border and would leave a cut wrist above the protected current panel.
The recorded alternative still meets the current 1080 size but relaxes the 1440 appearance, so it remains unaccepted and uninstalled.
No new candidate satisfying the complete allowed target was identified, and no new GUI, artwork, settings-control, or panel modification was made.
The earlier native measurements were reused because their source and asset inputs are unchanged; no game was launched and no lease or settings file was touched in this audit.
The current MCP definition lookup again returned the same mod window and vanilla precedent, workspace-index revision `53ebe7d933ccbd3d4b8ad0e58a02209d0f0af8ae8afec271af242642b72ca747`; the documentation revisions are unchanged from the recorded reads below.
The strict goal remains incomplete under the unchanged constraints; this finding does not assert that every undocumented engine capability is impossible.
Skills used for this resumed audit: `chaos-redux-scripted-gui` and `chaos-redux-shared-git-commit`.

## Implementation

Only `interface/frontendmainview.gui` and this document change.
All non-logo frontend definitions and tuning are preserved.
The 1070×355 lower panel, its bottom offset of 10 px, navigation buttons, about/community columns, background selection behavior, and single-player submenu remain unchanged.
The native `logo_art` icon uses the unchanged `GFX_chaos_redux_logo`, texture `gfx/interface/chaos_redux_logo.dds`, original local offset (-15,-17), and original scale 1.05.
Its 592×669 `logo_reserve` is centred inside a canvas with height 160% of the virtual screen, minimum height 1600, and settled y offset -422.
At 1440 this gives the original top-left (969,379) and native 622 px painted width.
At 1080 it gives top-left (649,91), keeps REDUX visible, and places the entire cut edge behind the foreground panel.
The native icon retains its original size at both targets; it is 622 px wide at 1080 instead of the requested 588 px.
The minimum canvas yields a settled native top of 27 virtual pixels for shorter canvases; this bound is source-derived, while the two target resolutions were observed in the engine.
Animation starts 240 px below the settled logo position and rises over the existing 1200 ms, so its entrance does not cross above its settled top.
The hidden direct child `frontend_game_logo` remains available to the hard-coded frontend controller.
The decorative icon remains in `mainmenu_panel_upperleft/logo_reserve/logo_art`.
No artwork, localisation, gameplay, country setup, or shared settings-control file was changed.

`frontend_background` retains the existing centred, aspect-preserving 4:3 cover layout and registered `chaosx_main_menu` background.
`mainmenu_single_player` retains the current lower-panel placement.
Navigation buttons remain direct children of their hard-coded menu windows.
Commit `baaeb00fc5` superseded the All Settings implementation introduced by `13b8fabb9e` with System Settings.
The current `system_settings_button`, its click binding, `interface/chaosx_system_settings.gui`, and related effects remain untouched; preservation is verified by change scope, not a campaign click test.

## Real screenshot evidence

Captures are native Linux HOI4 1.19.3 on private Xvfb :95, UI scale 1.0, using a separate test mod tree.
No screenshot was simulated from geometry or resized to stand in for another resolution.
The original reference used the complete exact `06e4c5aaa7:interface/frontendmainview.gui` in the Linux test copy only.
The Windows repository file was not rolled back wholesale.
Artifacts are ignored files under `.tmp/menu_logo/evidence/`.

| State | Native screenshot |
| --- | --- |
| Original 2560×1440 reference | `reference_06e4c5aaa7_2560x1440.png` |
| Before, 2560×1440 | `before_2560x1440.png` |
| Native restoration, 2560×1440 | `after_restored_2560x1440.png` |
| Before, 1920×1080 | `before_fresh_1920x1080.png` |
| Native restoration, 1920×1080 | `after_restored_1920x1080.png` |
| Proposed panel anchor, 1920×1080 | `proposal_panel_anchor_1920x1080.png` |

Matched native no-logo fixtures isolate the actual painted pixels from the scene and foreground panels.
The reference's visible logo bounds are [969,379,1591,1025); the restored native logo has the same unoccluded rendering and continues to y=1080 because the current panel is lower.
All 247,888 reference-painted pixels above y=1020 match exactly, with zero channel differences.
The original panel's translucent border changes 351 logo pixels at [1228,1021,1317,1025), and the current panel exposes 3,773 additional wrist pixels at [1215,1024,1315,1080).
The original panel's logical/opaque tops are 1020/1025; the current panel's are 1075/1080.
These differences prevent a claim that the complete visible logo matches the reference pixel-for-pixel while the current panel stays unchanged.
`occlusion_comparison.json` and the paired comparison JSON files retain counts, bounds, and screenshot hashes.

At 1080 the current background-rendered logo is 588×665, with painted top y=86 and foreground coverage at y=720.
The restored native icon is 622 px wide, with painted top y=91; native inspection confirms the full diagonal bottom edge is covered and the top is clear.
The size requirement is therefore not met by this temporary restoration.

## Iteration findings and limits

The current layout was captured before each target's restoration.
GUI file-watcher reloads worked; eight-second settling waits were used after the first reload capture caught the entrance animation.
That transient `candidate_c_2560x1440.png` was rejected; the later settled capture was used for analysis.
Integer background sizes (622×703 and 622×702) and fractional size declarations (621.6×702.45) did not reproduce the original 1.05-scaled native icon's sampling.
The fractional declaration rendered a 621 px width, not the original 622 px painted width.
Background `scale = 1.05` did not enlarge either the tiled or simple background consumer; both tests rendered at 592×669 and produced identical screenshots.
The native-icon control restored the original unoccluded pixels exactly.
These tests establish the limitations of the supported paths examined; they are not an exhaustive proof about every undocumented engine capability.
No supported route meeting the full strict pair was demonstrated.
Cropping the wrist to the old panel boundary would create a detached flat cut above the current panel, so it was not used to manufacture a pixel-match claim.
The optional 1920×1200 and 2560×1080 captures were not taken because each resolution requires another native launch.
No campaign, All Settings/System Settings runtime test, or Windows-renderer pixel comparison was performed.

Both Linux `settings.txt` and `pdx_settings.txt` were backed up before the first launch and restored byte-for-byte after the owned game and helpers stopped.
`settings_restoration.json` records the restored hashes.
The lease was released immediately after those native checks; the shared Windows settings and other displays were untouched.

## Proposed alternative — unresolved

Anchor the aspect-preserving background-rendered logo to the lower panel instead of preserving the original 1440p pixel rendering.
The prototype is `proposal_panel_anchor.gui`, retained only in ignored scratch.
Its native 1080 capture is byte-for-byte identical to the current 1080 before image, preserving the 588×665 size, top clearance, and complete hand-edge coverage.
It uses bottom-centred orientation/origo, the existing 26/389 margins, and a 60 px inset; its 1440 placement is source-derived and has not been captured in the engine.
It accepts a different 1440 look and texture sampling, so it requires the user's selection before installation.
Another design choice is to restore the original panel's 1440 occlusion as well, which changes a protected non-logo surface and also needs approval.
Neither alternative is accepted or wired into the repository.

## Assets and references

| Consumer | Sprite | Asset and definition |
| --- | --- | --- |
| Visible native logo | `GFX_chaos_redux_logo` | `gfx/interface/chaos_redux_logo.dds`; `interface/frontendmainviewbg.gfx` |
| Retained adaptive-logo definition/prototype | `GFX_chaos_redux_logo_scaled` | Same unchanged DDS and GFX file |
| Scene background | `GFX_frontend_bg`, `GFX_frontend_bg_basic` | `gfx/loadingscreens/chaosx_main_menu.dds`; frontend GFX files and `common/frontend/backgrounds/base_backgrounds.txt` |
| About/community and navigation | Existing menu sprites and text | Existing frontend GUI, `interface/chaosx.gfx`, and `localisation/english/chaosx_gui_l_english.yml` |
| Community buttons | `GFX_discord_button`, `GFX_donation_button`, `GFX_homepage_button`, `GFX_github_button`, `GFX_documentation_button`, `GFX_chaosx_youtube_button` | `gfx/interface/*.dds`; `interface/chaosx.gfx` |

The background manager selects the single `chaosx_main_menu` entry in `common/frontend/backgrounds/base_backgrounds.txt` and substitutes its texture for `GFX_frontend_bg`.
The existing background picker remains hidden because there is only one registered painting.
Visible custom menu text retains `chaosx_main_menu_about`, `chaosx_welcome_intro_loc`, `chaosx_main_menu_community`, and `chaosx_main_menu_version` in `localisation/english/chaosx_gui_l_english.yml`.
The existing unresolved future proposal to provide a small picker thumbnail if several menu paintings are introduced is retained; it is outside this restoration.

Earlier rounds had no exposed coding reference/source/GUI routes and used direct local reads.
During final review the routes became available, and `reference_context`, targeted `reference_search`, `reference_read`, and `source_lookup` returned the same cited documentation revisions and the current mod/vanilla window definitions.
The context reported no missing required wiki/game-documentation sources, no omitted source kinds, and no known-mistake findings.
The first source-lookup request combined symbol and path and was rejected; its single corrected symbol-only request succeeded.
No MCP GUI render or script-validation pass is claimed; visual evidence comes from the native captures.
The complete returned reference data is retained in `.tmp/menu_logo/evidence/mcp_reference_evidence.json`.
Offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, lines 75–105 and 124, covers containers, percentage sizes, orientation/origo, animation positions and margins; SHA-256 `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.
Installed `common/scripted_guis/_documentation.md`, lines 1–40, covers attachment; SHA-256 `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.
Installed `interface/frontendmainview.gui`, lines 1–18 and its native `mainmenu_panel_upperleft`, supplies the frontend precedent; SHA-256 `17e5f3cde42d170b9e4ac40bb2312cd2d505767920b6e995c5c58b48c38efd1b`.
Installed `interface/AST_cabinet_trust_scripted_gui.gui`, lines 16–21, supplies centre-up placement; SHA-256 `ef072fb932861d32f189d40365f82c07caf74ee069a806cc23b5d7081936b6f4`.
Installed `interface/combatlogview.gui`, lines 393–429, supplies nested percentage layout; SHA-256 `2a0f4a8679891835068de10c125731b369205eade41497304a4f3ba3a38f5a5f`.
Native screenshots, rather than inferred geometry, determine the measured positions and renderer comparisons above.
The final MCP reads covered Interface modding Arguments lines 81–109 and Position/orientation lines 369–386, and installed scripted-GUI documentation lines 1–40.
The definition lookup returned current `mod:interface/frontendmainview.gui` lines 299–337 and overridden `game:interface/frontendmainview.gui` lines 210–225, workspace-index revision `ef07ca5fcc9cdae7692bfc61e910f697625c8ba02696417e157c2efcc7be148e`.
The parent performed the source and visual review because this shared frontend is outside the named-event GUI worker's scope.
Skills used: `chaos-redux-scripted-gui`, `chaos-redux-debug-playtest` under the explicit Linux launcher/capture authorization, and `chaos-redux-shared-git-commit`.
No skill was created or changed.
