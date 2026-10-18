# Event 033 current GUI gate review, 2026-10-07

## Current bounded repair conclusion, 2026-10-09

The new source-layout tranche supersedes the finished ABI task.
Independent source repairs are implemented, while geographically aligned regional artwork and synchronized D37 promotion remain accepted and queued.
This is not a full GUI or Event033 completion claim.
The older audit below retains its original source scope, status, diagnostics and identities.

Five live files changed: `interface/033_acid_rain.gui`, `interface/033_acid_rain.gfx`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, GUI-only keys in `localisation/english/033_acid_rain_l_english.yml`, and only the authorized visual rows in `common/script_constants/033_acid_rain_constants.txt`.
The finished GUI effects/getter ABI code remains byte-identical at D8DA2914... and 326CF6D0....
Its historical 149-assertion replay is preserved rather than rerun against altered visual fixtures.
The 38 other-owner Main_14 substitutions remain exact.
The parent-verified plain/dynamic descriptions for nr33.101/104/105/106/107.d and all non-GUI localisation remain unchanged.
No gameplay, costs, AI, weights, shared UI, root/triggers, assets, Git/index/commit, game, desktop, logs, saves, external tooling or other agents were changed or operated.

### Implemented source repairs

- Existing card DDS now uses a proven native cornered-tile consumer, preserving its 8px edges and filling both 272x86 fronts and 272x267 global/empty panels.
- Coverage uses a fixed clipped track plus fixed-size native tiled fill, translated only with documented x positioning from temporary trigger data.
The actual 536x24 frame has 19px painted side caps, so its usable span is 498px at local x31.
The count-based source calculation is x = (498 * clamp(touched,0,eligible) / eligible) - 498 for positive eligible, and x = -498 for zero or negative eligible, with unchanged fixed dimensions.
The trigger multiplies the clamped touched count before dividing, retaining fractional coverage rather than first flooring the ratio or consuming the caption.
The caption's established integer convention remains unchanged.
The earlier claim of exact actual-ratio coverage was incorrect while the trigger consumed `global.acid_rain_gui_coverage_percent`, and this correction supersedes that claim.
Only `acid_rain_world_scripted_gui.triggers.acid_rain_coverage_fill_1_visible` changed in this follow-up, with the same `acid_rain_gui_coverage_fill_x` temporary and native x property.
No persistent variables, gameplay state, dimensions or controls changed, and the staged D37 scripted-GUI draft has the same corrected trigger to prevent a later regression.
No unsupported dynamic width, generated frame art or functionality fallback was introduced.
- Seven completion indicators select the actual installed native checkbox's second frame, keeping their existing visibility and row positions.
- The inlay's single-line status is at y66,h14, giving Garamond/Main_14 baseline77 beside the existing 36px button/Hoi16 baseline77.
The new dominant-status label retains other counts through the existing status item's hover.
- Warning/exposed tooltip intervals end at358 and457, leaving one-pixel source gaps before the next items at359 and458.
- Coverage and Preparedness remain the two foreground active values.
National auxiliary counts, Air/current-added-remaining and deaths remain available through their existing hoverable items, without deleted controls or facts.
Global elapsed/minimum dates move to Phase Clock hover, leaving its next check window and storm count as two supporting values.
The four readiness indicators, seven region records and maximum three front/storm records remain.
- The global clock explicitly says next check window rather than a guaranteed dissipation date.
- Region eligibility is now qualification rather than automatic activation.
Live legacy pieces require current/future weather or prior touch and are excluded under the global layer.
Their old storm-painted asset identity remains incorrect until D37 promotion, so this source qualification is not an asset-completion claim.

### Measured map anchors and parent F10 preservation

The neutral base was viewed directly and retained unchanged.
Representative land points were measured on its actual 1672x941 canvas, then transformed by scale0.3188 and offset13,0.
The ordinary static marker's alpha32 painted box is [16,10,111,112], with scaled centre offset22.660991,21.768826 from the published upper-left origin.
Warnings and severe markers differ by less than one logical pixel in centre offset.
The chosen points and native coordinate annotation are in ignored `.tmp/033_gui_layout/base_measured_targets.png`, with a separately labeled synthetic anchor atlas.
These are texture/geometry diagnostics, not campaign-valid multi-front or MCP/game screenshots.

| Region | Actual base target | Published native upper-left x/y |
| --- | --- | --- |
| Europe, central mainland | 860,310 | 265,77 |
| Middle East, Iranian plateau | 985,415 | 304,111 |
| Asia, central mainland | 1215,370 | 378,96 |
| Africa, central interior | 880,595 | 271,168 |
| Australia/Pacific, Australian interior | 1385,710 | 432,205 |
| North America, central mainland | 370,360 | 108,93 |
| South America, Brazilian interior | 565,650 | 170,185 |

Shared-region displacement is -48, preserving separation and keeping three storm boxes inside the map at every anchor.
The previous +48 would clip the third Australia/Pacific storm after geographic correction.
The full constant-file after SHA-256 is `7eedee426071c13b4a205747a27adb78b1f735e81db15e6ac3e4f09881c01708`.
After masking only the authorized 14 coordinate values and shared offset, every other physical byte matches the parent's `6838c2fcdfad25c6147045544c2253ca05b29cc5273dd4071ba9622e824b0a85` snapshot, preserving F10 tuning for the probability owner.
The old constant/helper comments that describe enlarged-overlay weighted middles or rightward shift were intentionally not altered under the numeric-only constant scope and unchanged ABI-code constraint.
The current contract in this section records the actual measured interpretation and leftward displacement for parent documentation promotion.

### Causal asset findings and accepted D37 staging

The neutral base is not the source of the dense weather.
Its DDS hash remains `64c59f745f6bb9c7213d55284e09e8784568bc44763a3357fc6ddb70fccc12cc`.
All seven `GFX_acid_rain_region_overlay_i` IDs resolve only to their corresponding `gfx/interface/033_acid_rain/gui/acid_rain_region_overlay_i.dds` single-frame paths.
Each current texture is 1672x941, but its painted continent is enlarged independently rather than aligned to the retained base.
Overlay1's alpha128 box is [258,34,1067,646], proving the oversized Europe painting.
All seven eligibility flags were positive in the retained one-front/aftercare fixtures.
Compositing only the base plus those seven actual DDS textures reproduces the storm-heavy aftercare appearance.
Adding visited and ordinary veils reproduces the denser green regional appearance.
The ordinary veil has nonzero alpha over70.52 percent of its canvas, while the visited veil covers63.39 percent and contains cloud/drip weather rather than quiet history.
No forced base replacement is needed.

D37 is accepted and queued, not final-art approval.
The parent identifies accepted-plan commit `b19d2e4eb40a4166b2246e0172768087fec571f1` and the separately assigned Europe candidate producer `01a12189-a01f-7d01-bb00-ce0e9f013aa3`.
This worker did not operate that producer or overlap its API, asset or source work.
The three replacement consumer drafts and complete promotion hunks are staged only under `.tmp/033_gui_layout/promotion/` and `promotion_after_assets.patch`.
They have not been copied to runtime files.
Current runtime regional GFX remains noOfFrames1 against the old DDS files, preventing false four-frame wiring.

The production contract preserves the same seven IDs and runtime paths, with four horizontal 560x300 frames per2240x300 static strip.
Native region consumer scale is1 and origin0,0.
Frames are 1 fully transparent inactive, 2 slate non-weather visited history, 3 amber non-rain approaching warning, 4 translucent active cloud/rain with base geography readable.
Each staged visible trigger directly calculates its own `acid_rain_gui_region_frame_i` temporary, and each staged property binds that temporary to its matching icon.
Cached over2 selects4, approaching1 selects3, otherwise touched>0 selects2, otherwise1.
Global cached status3 or global-layer activity hides regional pieces and uses the existing independently animated global family and its static partner.
All four real animation families and their accessibility partners remain unchanged.

D37's region frames replace the ordinary/warning/visited broad-world veil roles at synchronized promotion.
The staged GUI removes those three instances and their scripted visibility hooks, while old GFX registrations, source assets and manifests remain historical until parent-approved replacement proof permits retirement.
The parent-assigned producer must deliver aligned alpha outside each geographic region, the frame1 all-transparent condition, distinct colour and non-colour history/warning/active cues, real ImageGen active weather lineage, independent source/native-size review and strict DDS round-trip proof.
No final art, recolouring, placeholder, generation or asset promotion was performed by this worker.

### Source checks, hunks and visual limits

Ignored scratch/output is confined to `.tmp/033_gui_layout/`.
Before-source snapshots include the font-owner-inclusive GUI and the parent's current F10 constant file.
`our_layout_hunks.patch` contains only this worker's changes relative to those snapshots, so the parent can separate mixed GUI hunks from the 38 existing font edits.
`check_layout.py` passes373 local assertions for actual source/native texture consumers, meter boundary/ratio cases, all seven live and staged state selectors, unchanged controls/effect/phase/static wiring, font baselines and text widths, painted card interiors, six centered resolution/scale cases, anchor centring and all three-storm bounds.
These are local source/model checks, not MCP or native engine execution.
The count correction's raw before file is `.tmp/033_gui_layout/coverage_before_counts_033_acid_rain_scripted_guis.txt`, SHA-256 `3d2497e6450fedb6b66ecab4bea7676cde1a4ff203a9c0fdcbaad8f80380faa1`.
Its complete focused delta is `coverage_counts_delta.patch`, and all bytes outside that one trigger match the before snapshot.
The current check script SHA-256 is `4f026ba5caa4a879bf72d3ffc4464a34bd3c6c30a13f364d7b5ecedc437cda46`, its saved `layout_checks.json` is `b58408cf72752e5004ff807c3103cc53fc7b1ee657827375aecf328125ab153b`, and the focused delta is `513c334fa45f1b4a89074d6757daf17f82aac5e4e83b78696f8becafa0327824`.
The complete own-layout hunks are `e2273c7b2d5dd249f6b83bb6cac0febb621f36cea17db8bd869b027d1e077b3f`, and the still-unapplied D37 promotion hunks are `ee6c008b6fed1adb934aaaf703a0b6cb42cf558da55d6d7c7258f01f29898ec3`.
The previous 252-assertion metadata remains preserved as `coverage_before_counts_layout_checks.json`, SHA-256 `984e6e1b83f3031c72de374c21f5fce69adef9f5973e8a4ce9aeaec12570e00b`.
The new check executes the actual parsed before and after trigger bodies against identical 285/800, 799/800 and 1/1001 count/caption fixtures, then separately poisons the caption to confirm that the new fill is independent of it.

| Count case | Unchanged caption | Rational source fill width in the 498px interior |
| --- | --- | --- |
| 285/800 | 35% | 177.4125, replacing the before-source 174.3 |
| 799/800 | 99% | 497.3775, replacing the before-source 493.02 |
| 1/1001 | 0% | 498/1001, approximately 0.4975024975, replacing the before-source 0 |
| 280/800, 440/800, 600/800 | 35%, 55%, 75% | 174.3, 273.9, 373.5 |
| 0/800, 10/0, 10/-800, -5/800 | Invalid cases are synthetic guard tests, not caption claims | 0 with x=-498, and no division on non-positive eligibility |
| 1000/1000, 801/800 | Over-eligible case is a synthetic clamp test | 498 with x=0 |

These widths are exact rational source-operation results, not a claim that the game paints arbitrary fractional pixels exactly.
The offline Data structures snapshot, lines425-434, describes five fractional digits with truncation, while installed `documentation/script_concept_documentation.md`, lines184-215, establishes fixed-point math without documenting this trigger sequence's native rounding or GUI rasterization.
The actual-source checks therefore model positive division truncation at 0.00001 logical pixels and a separately labeled coarser 0.001 sensitivity case, preserving exact empty/full boundaries in both models.
For example, 1/1001 becomes 0.4975 or 0.497 logical pixels under those stated models, and 799/800 becomes 497.3775 or 497.377.
Multiplication is performed before division so precision loss is on the logical-pixel quotient rather than an already truncated ratio.
Native coordinate conversion, pixel-edge rounding, alpha filtering and visibility of subpixel coverage remain unmeasured at every resolution and UI scale, with no new render or engine-execution claim.
The prior ABI test is distinct and was not rerun.
Per-file hashes, primary source paths/line spans and detailed metadata are retained in the temporary check outputs.

The source-derived physical boards are900x600 at scale1 and1125x750 at scale1.25.
Their top-left coordinates at1920x1080,1600x900,1366x768 are510/240,350/150,233/84 at scale1 and397.5/165,237.5/75,120.5/9 at scale1.25.
The 500x92 inlay becomes625x115 under uniform1.25 scaling, with unchanged logical containment.
This does not assert a new rendered125-percent image.

Renderer/global/cold/tooltip and helper/provenance initial-plus-narrow attempts are already exhausted under the replacement rules.
No new name, geometry edit or successful status response resets that underlying failure.
No renderer retry, helper expansion or provenance recovery was issued in this tranche.
Relevant offline wiki and installed native/scripted GUI/font/texture consumers were read directly, and their concrete paths, spans and hashes are recorded in `primary_references.json`.
A future attempt requires new tool/input information that addresses the underlying failure, not another unchanged poll.
Absent current images limit visual claims rather than blocking these completed independent source fixes.
Aligned region asset promotion remains a real requested production dependency and is not marked complete.

| Live source | After SHA-256 |
| --- | --- |
| interface/033_acid_rain.gui | `9ee516149a5343b2d865061251677dffbf96927aebeca84ac011b3698b145656` |
| interface/033_acid_rain.gfx | `357911989b3d49c7001505fa283c2daa3d3a2de7e6d0b42354c465df0b7ceee0` |
| common/scripted_guis/033_acid_rain_scripted_guis.txt | `5c0e9bb589ecfb79efc0347b7010d8f762b460c3fd7089cf1a87708f17255125` |
| localisation/english/033_acid_rain_l_english.yml | `38f71ce5bee9b5471a7de6cc4c9de68ff1c962ffabfdd2bdd7c605f4c192fcba` |
| common/script_constants/033_acid_rain_constants.txt | `7eedee426071c13b4a205747a27adb78b1f735e81db15e6ac3e4f09881c01708` |
| common/scripted_effects/033_acid_rain_gui_effects.txt, unchanged ABI | `d8da2914c924b5ee200449b811de88d971af99be9e48e4d632cedd46b70a623a` |
| common/scripted_localisation/033_acid_rain_scripted_localisation.txt, unchanged ABI | `326cf6d0b4906c0546b3cd1a719656b664e611a61f7adf5245384a43ed955223` |

No design fallback, deleted required fact, gameplay reduction or new control/tab was introduced.
Remaining work is independent asset candidate review/promotion, the staged D37 consumer adaptation, and the parent's final integration/commit.
Skills used: current chaos-redux-events, chaos-redux-subagents and chaos-redux-scripted-gui.
No skills or other agents were changed.

## Historical audit recorded 2026-10-07

Gate status: unresolved.
Current-source GUI inspect has returned for both owned windows, and the 1920x1080 normal one-front full, cropped, and click-region images have been reviewed.
The current image findings below require parent or owner disposition, while the wider phase, resolution, hover, and tooltip evidence is in progress.
No owner-applied source correction or visual approval is claimed.

## Scope, ownership, and acceptance basis

Event: `033_acid_rain` (Event 33, Acid Rain).

Owned windows: `acid_rain_world_window` and `acid_rain_category_inlay` only.

Exact owned sources reviewed: `interface/033_acid_rain.gui`, `interface/033_acid_rain.gfx`, `common/scripted_guis/033_acid_rain_scripted_guis.txt`, and `common/scripted_effects/033_acid_rain_gui_effects.txt`.

Entry points: the Event 33 national response decision category opens the category inlay; its Open Map button invokes `acid_rain_gui_open_from_category`. Event Details invokes `acid_rain_gui_open_from_event_details` through the Event 33 presentation bridge. The accepted Part 6 spec explicitly assigns the dedicated map to these two Event 33 entry points, and the exact scripted GUI file binds the named Event 33 containers.

Accepted design basis: the parent instruction explicitly accepts Parts 6 and 10 and decisions D16–D18, D24, D28, D31, and D33 in `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md`. Part 6 records the parent-approved implementation decisions and points to that decision record; the record states that Event 033 design authority was granted on 2026-10-04. This acceptance supports review of the map ledger, category inlay, regional/global/aftercare states, and D18 footer navigation.

Authorization for this task is read-only source and visual-gate review, with this handoff and task-owned validation artifacts as the only permitted writes. No source, asset, shared interface, or unrelated file has been edited. No commit was created.

## Resumption and observation identity

The replacement AGENTS.md was read on resumption.
The prior execution handles 70 (world normal 1600x900) and 75 (inlay normal 1366x768) were re-polled and returned `exec cell 70 not found` and `exec cell 75 not found`.
Neither call supplied a durable MCP job identifier, so their backend outcomes remain unknown.
The earlier `timed out awaiting tools/call after 600s` messages are client observation timeouts and do not establish backend failure.
The connected `hoi4-agent://server/status` resource returned server version 3.10.0 through the configured stdio process.
Its actual configuration places this workspace's artifacts under `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts`.

The corrected one-front 1920 request also had a client observation timeout, but its completed backend artifacts were recovered by exact scenario id `event033_current_regional_one_normal_1920_v3_20261007` and source revision `0738074b477ff9da6e16eb9ac1d5eb3bc7b2e9bfadad20c370637c76edccb2c5`.
They record UI scale 1 and zero unresolved visibility facts.
The retained artifact index under `validation/gui_current_2026_10_07/regional_one_1920_v3/` records each URI, SHA-256, provenance hash, and copied-byte identity.
Its full, cropped, and click-region PNGs have SHA-256 `3d2134b9999a09985a42a7edaffa9ac8b02d084d45a039592569cf350d7a0ae9`, `aa3c27bad676c6357c6a73187f4d0b4bea2f8103ff7de3b1288d5647d3d2c718`, and `a769ede6d528d44ea2ab871746637f96677c1ffb22f07067a0808b3a249232bd`.
The rejected language request, the earlier intensity-2/Ordinary-label fixture, and the inlay fixture with world-window expectations are retained as unqualified input history.
Their errors are fixture errors and are not attributed to the GUI source.

The requests named 1600x900 and 1366x768 initially returned primary full and click-region artifacts at 1920x1080 because their normalized scenario default overrode the primary view's resolution.
Those resources retain their actual 1920 identities and do not count as lower-resolution full-window or click-region proof.
Lower-resolution qualification must use explicit `scenario.resolution` and `scenario.uiScale = 1` as well as the render matrix request.

## Sources and identity at review start

The first recorded SHA-256 values were:

| File | SHA-256 |
| --- | --- |
| `interface/033_acid_rain.gui` | `91FAF794F739CA28DBDF637DE5A2E48DF1C31FF02180759A3FA959E6082C7629` |
| `interface/033_acid_rain.gfx` | `A24CBA2E9B7C4B567A96C0D1731AC97EE136E48CF41DB0F8E03FEF8BFF29B7F6` |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | `6F04FFDC4596F6CE54ECE1C0F87DE7EDD7AA2B8021BB915F9712836CC1893903` |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | `24B1C3767BDC82094E37C602F297EA71E92637F7B758AFF9CEEC3615CF1EF64C` |
| `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md` | `E1BF294B6C38019EC0A0ED96CD5B302A3B7C42A3079FD4F6E09C150B6BD3EE34` |
| `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png` | `2CA8693424C479BD0A40EE1FF34D8D75727A82BA22D6398117E5ADD221594BDA` |

`git status` and the exact GUI diff showed the other owner's uncommitted font substitutions in `interface/033_acid_rain.gui`: 38 `Arial12` to `Main_14` substitutions on visible numeric/status text (38 additions and 38 deletions). That patch is preserved. The baseline diff is not attributed to this review. A second hash check at 2026-10-07 12:05 UTC matched all four initial linked-source SHA-256 values above, so no source-identity change was observed during that interval. Recheck before finalizing; if bytes change during MCP review, list both identities and retain artifacts against their returned source revisions.

## Reference and native mapping

Accepted reference: `docs/assets/033_acid_rain/gui_repair_reference/acid_rain_world_window_scoped_reference_2026-10-03.png` (1536x1024 PNG; hash above). It shows the bounded dark metal dossier frame, a large left map, right-hand phase card stack, segmented coverage bar and seven region rows, a national preparedness strip, and a bottom navigation row. Blank painted bars in the reference are content regions; the current GUI keeps labels, values, icons, states, and buttons as native elements.

| Reference region | Current native elements and bounds | Intended content and interaction | Accepted constraints |
| --- | --- | --- | --- |
| Outer board and header | `acid_rain_world_window`, 900x600, centered; title/phase/ledger/close at GUI lines 100–164 | Event identity, phase, four global ledger values, close | Event-only, read-only presentation; centered at supported resolutions |
| World map | `acid_rain_map_panel`, 560x300 at local x24/y74; map base, seven overlays, veils, marker pairs and legend at lines 172–481 | Regions, ordinary front and warning/severe markers, global cloud layer; region rows provide stored hover facts | Stable region anchors and no province-level precision claim; static marker partners when motion is disabled |
| Phase cards | `acid_rain_front_stack` at x604/y74; three 272x86 front cards, one 272x267 global card, one empty/aftercare card | One, two, or three ordinary front cards, or one global card and up to three superstorm rows, or quiet empty/aftercare state | Front cards are ordered by stable front ID; global card replaces fronts; no impossible overlap presented as normal |
| Coverage | `acid_rain_coverage_panel`, 560x118 at x24/y390; segmented meter, seven rows, completion marks | Exact touched/eligible counts, percentage, per-region totals/completion | Ten native fill segments; completion has a non-danger cue |
| National strip | `acid_rain_national_strip`, 852x44 at x24/y508 | Preparedness and four component pips, warning/exposed/severe/aftermath counts, deaths, prevented estimate, contamination | Preparedness is the single active national mechanic value; remaining numbers are status/history |
| Footer | Native controls at y560: Refresh x24, Back x165, Details x306, motion toggle x753; Close remains in header | Read-only refresh, return to opener, Event 33 details navigation, reduced motion | D18 says Back returns to decision category or Event Details based on opener; Details is hidden when opened from Event Details |
| Category inlay | `acid_rain_category_inlay`, 500x92, native phase/coverage/Preparedness/status/Open Map elements | Compact phase, world coverage, national Preparedness/status, open map button | No full front list or casualty ledger; status remains a short single line |

Native adaptation basis: Parts 6/10 require live values and interactions. The decorative reference bars and icons remain native backgrounds/sprites, while all labels, changing values, phase visibility, clickable footer controls, and tooltips remain native GUI/scripted-GUI elements. The 900x600 centered board and 560x300 map follow the accepted Part 6 target. The world surface has at most five simultaneous button controls (close, Refresh, Back, Details, motion); Details is hidden when the map opens from Event Details. The category inlay contributes one Open Map button. No gameplay-changing action or cost is shown in either window.

## Exact presentation wiring and linked text/assets

`common/scripted_guis/033_acid_rain_scripted_guis.txt` defines `acid_rain_decisions_scripted_gui` (`decision_category`, window `acid_rain_category_inlay`) and `acid_rain_world_scripted_gui` (`player_context`, window `acid_rain_world_window`). The category opener is `acid_rain_category_open` / `acid_rain_category_open_click`, guarded by `acid_rain_category_open_click_enabled`; Event Details calls `acid_rain_gui_open_from_event_details`. World-window controls are `acid_rain_world_close`, `acid_rain_world_refresh`, `acid_rain_world_back`, `acid_rain_world_details`, and `acid_rain_world_motion`, each wired to the same-named `_click` effect and corresponding `_click_enabled` or `_visible` trigger. Display projection functions include `acid_rain_gui_refresh_read_only`, `acid_rain_gui_refresh_national_strip`, `acid_rain_gui_project_region_facts`, `acid_rain_gui_project_superstorm_marker`, and `acid_rain_gui_set_region_anchor`.

The window's principal sprites from `interface/033_acid_rain.gfx` are `GFX_acid_rain_map_base`; `GFX_acid_rain_region_overlay_1` through `_7`; visited, ordinary, warning, and global veils; animated/static front, warning, severe, and global sprite pairs; the three superstorm marker consumers using the severe pair; `GFX_acid_rain_card_background`; `GFX_acid_rain_coverage_frame` and `GFX_acid_rain_coverage_fill`; `GFX_acid_rain_preparedness_badge`; and `GFX_acid_rain_component_pip`. The global animation sprite is `GFX_acid_rain_global_animated` with `GFX_acid_rain_global_static` as reduced-motion fallback. D17 says `GFX_acid_rain_global_veil` is registered but not displayed. The renderer must resolve the actual linked texture files and missing assets; that MCP finding is pending.

The linked GUI text and tooltip keys are in `localisation/english/033_acid_rain_l_english.yml` (SHA-256 `5F8169AC30B4CF546D5B91B03F347BA868890A65788DF9D4724B12DB1BD51963`). The UI key groups include `acid_rain_world_*`, `acid_rain_front_card_1_*` through `_3_*`, `acid_rain_global_card_*`, `acid_rain_coverage_*`, `acid_rain_region_row_1` through `_7`, `acid_rain_national_*`, `acid_rain_category_*`, `acid_rain_gui_*_tt`, and the per-component tooltip keys. The exact file was located by keys from the two supplied GUI windows; the relevant block at lines 259–391 includes the dynamic region/preparedness tooltip copy, card/ledger text, footer labels, category status variants, and motion tooltips. Scripted-localisation calls such as `GetAcidRainGuiPhase`, `GetAcidRainGuiFront1Region`, `GetAcidRainGuiFront1Intensity`, `GetAcidRainGuiFront1NextRegion`, `GetAcidRainCategoryStatus`, `GetAcidRainGuiCoverageStatus`, and `GetAcidRainGuiMotionMode` determine runtime wording. The offline renderer's handling of those dynamic tokens remains unverified because no render returned.

The current `.gfx` file contains 28 `GFX_acid_rain_*` registrations; all 28 referenced DDS paths currently exist. Exact GUI source references 24 of those sprite IDs. The other four registrations are `GFX_acid_rain_global_veil` and the generic front, warning, and severe marker sprites; D17 explicitly says the global veil is registered but not displayed, while the exact window source uses the animated/static pairs for its markers. This is a scoped consumer note, not a request or authorization to remove registrations. Path existence is not DDS decode, source-provenance, alpha, or visual approval. Font identifiers in the current `.gui` are `hoi_20b`, `hoi_16mbs`, and `Main_14`; the 38 owner changes specifically replace earlier `Arial12` assignments with `Main_14`.

## State matrix and visible-value/text budget

Required coherent fixtures for this review: regional with one front, two fronts, and three fronts; global layer with active superstorm rows; aftercare/empty card with motion disabled and static marker fallback; category inlay normal and longest real status text. Review at 1920x1080 UI scale 1, 1600x900 UI scale 1, and 1366x768 UI scale 1. Hover/tooltip, selected navigation, active/disabled action, warning/severe, completed coverage, empty/full list, and long text must be covered where the live GUI route supports them. No synthetic maximum-control fixture may be presented as normal gameplay.

One-front normal 1920x1080 at UI scale 1 has returned and been reviewed with generated scenarios disabled.
The other phase and resolution proofs remain in progress.
The earlier 65.6-million-pixel refusal does not authorize downscaling, changing UI scale, dropping visible layers, or relabeling a reduced or misbound view as production output.

Visible-value budget from accepted Part 6: the spec names world coverage and national Preparedness as the two active values and classifies the rest as read-only counters or status/history. The visible global header has four numeric ledger values (current Air, lifetime Air added, remaining allowance, global deaths); the coverage line has percent plus touched/eligible counts; the national strip has Preparedness, four component tiers, four state counts, deaths, prevented estimate, and current contamination. Front/global phase cards add more numeric readouts. This is an explicit parent review point against the scripted-GUI hard ceiling of four simultaneously visible mechanic values: Part 6's active-versus-ledger classification may be intended to separate ordinary status records from active mechanic values, but the currently authored window displays them together. Without the production render, I cannot determine readability or assert a budget pass; the parent should resolve whether this accepted classification satisfies the four-value cap. The four ordinary-front text groups are identity, band/state count, movement window/destination, and severe-cell count; their actual line fit is pending image review. No decision costs are displayed by these windows, so there is no cost count or texticon consumer here.

Static text-density audit: the maximum regional phase has three cards with four native text elements each, and the global card has its bounded storm list and timing lines.
Coverage uses one heading, one percent/count line, and seven region rows.
The national strip uses Preparedness, six tooltip-bearing state/history labels, four component pips, and a second contamination line.
The category inlay has phase, coverage, Preparedness, a status line, and one Open Map button.
The footer has three buttons when opened from Event Details (Details hidden) or four when opened from the category, plus one noninteractive hint.
The header close button brings the visible world-control count to four or five.
The normal one-front labels fit in the reviewed render, while longer labels and large values remain open.

Tooltip text-density targets from the linked localization block: `acid_rain_gui_preparedness_breakdown` carries an overall score, four component tier/points rows, and a concluding action/consequence paragraph; `acid_rain_gui_region_tt` composes reach totals and current weather with separate over/approaching/global/clear text; `acid_rain_gui_contamination_tt` explains current Air, Event 33 additions/allowance, and deaths; and the national/status tooltips describe current counts and responses. Their exact resolved line counts, width, placement, and truncation cannot be verified from localisation source and remain open pending MCP tooltip renders. The accepted tooltip content is not compressed or removed in this read-only review.

## MCP evidence and route state

Live tool schemas were present for `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`. `hoi4.reference_context(surface="gui")` returned workspace `mod_chaos_redux_ea3b2d67c2c0`, status `ok`, and the installed scripted-GUI document plus offline Interface modding and Scripted GUI modding pages. The context bundle reported `omitted: 1`, `omittedSources: []`, and `missing: []`; detailed GUI reference pages were then read through targeted reference reads/searches. The separate `script_doc` source kind is unavailable, but the installed `game_doc` source contains the complete `common/scripted_guis/_documentation.md` (revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`).

Read reference evidence:

| Source | Path and line span | Revision / finding |
| --- | --- | --- |
| Installed scripted-GUI documentation | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`, lines 1–146 | `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`; contexts, `window_name`, visibility, effects, element triggers, dynamic properties, and AI gating |
| Offline Interface modding | `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, container lines 73–117; icon/text/button lines 156–256 | Container/background/clipping/position/orientation; native icon, text, tooltip, and button fields. The targeted MCP read directly returned `buttonType`, lines 227–256, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`. |
| Offline Scripted GUI modding | `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, window assignment lines 40–67 and parent window lines 68–143 | Revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`; independent containers are valid `window_name` targets; parent rules distinguish independent and nested containers. |
| Offline Graphical asset modding | `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `frameAnimatedSpriteType`, lines 101–140 | Revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`; sheet frame count, fps, loop, `play_on_show`, pause, and click transparency. Search returned the exact section with no omitted results. |

Exact Vanilla precedent inspected directly: `interface/sov_paranoia_system_scripted_gui.gui`, lines 20–64, and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, lines 1–84. SHA-256 values are `B8925BF8DAF88BA82E6CE66F7B5131CAE7083E6EDA5367E2CF2B6EAEF6310A85` and `00DB231BF1D3183520E8E980B3433D5E5678A101849F96C17625D6B9384D85C5` respectively. It is a decision-category GUI precedent showing separate background, meter, needle, dynamic frame properties, centred native text, tooltip, and `decision_category` context; it is a structural reference, not a visual match for the map board.

The corrected `hoi4.source_lookup` calls succeeded with `sourceScope: source_location`, `complete: true`, and zero skipped sources. The Vanilla GUI lookup resolved `game:interface/sov_paranoia_system_scripted_gui.gui` at line 20 to owner `sov_paranoia_system_ui_window` (owner lines 20–188), revision `4965a0c3e86ed8b68dc578d77058037f27c3f7ef9ff744a5e93bf8fe1109bc43`. The scripted-GUI lookup resolved `game:common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` at line 3 to owner `sov_paranoia_system_ui` (owner lines 3–84), revision `fa24329d87cc2b9c273a54da873a53294f634f4c0bdb1be81fd5e0b8eadafef6`. `definitions` and `references` were empty because these were exact source-location lookups; the returned owner and source location are the evidence.

The actual pre-font GUI source is available at commit `0b30a383a3d27d41022a72ef05c777c15113893f`, Git blob `59d292e1a3de87c50cf587b4905ba46c79a8e602` (42,088 source characters). It is a valid matching historical source for the 38 font substitutions. A single 1366x768 normal request used this real `HEAD` file as `sourceBaseline`, solely to compare the font-owner change. That `hoi4.gui_render` call timed out after 600 seconds with no artifacts; it is not an after-fix or self-comparison.

Both initial `hoi4.gui_inspect` selectors, `acid_rain_world_window` and `acid_rain_category_inlay`, returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_inspect; Caused by: timed out awaiting tools/call after 600s`. Each used workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `{id: event033_current_normal_inspect, date: 1936.1.1, closedFlags: true, flags: {acid_rain_gui_window_open: true}}`, and `generatedScenarios: { enabled: false }`. A separate minimal retry for `acid_rain_world_window` returned the same 600-second timeout using scenario `{id: event033_current_world_normal_retry, date: 1936.1.1, closedFlags: true}` with generated scenarios disabled. No inspect artifacts were returned; current-source structure, localization dependencies, parent/context resolution, and diagnostics remain unresolved.

The requested minimal production `hoi4.gui_render` retry for `acid_rain_world_window` also returned `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render; Caused by: timed out awaiting tools/call after 600s`. Its selector was workspace `mod_chaos_redux_ea3b2d67c2c0`, scenario `{id: event033_current_world_normal_1920_minimal, date: 1936.1.1, closedFlags: true}`, `states: [normal]`, resolution `1920x1080` at UI scale `1`, and `generatedScenarios: { enabled: false }`. No render artifacts were returned. The first exact Vanilla `hoi4.source_lookup` requests were rejected as invalid shape: `maxLines` exceeded the route's maximum of 80 and each request omitted the required `line` with `path`; corrected bounded source-location requests then succeeded and are recorded above. Direct reads of those precise installed Vanilla files corroborated the MCP owner locations. Do not substitute source-only review if the GUI routes fail to return. This minimal request satisfies the specified retry shape and did not change resolution, scale, scenario density, or rendered state to get around the earlier aggregate-pixel refusal.

A second one-state normal production request for `acid_rain_world_window` at the other accepted baseline resolution, 1366x768 UI scale 1, with generated scenarios disabled also returned `timed out awaiting tools/call after 600s` and no artifacts. Its scenario id was `event033_current_world_normal_1366_minimal`. A real pre-font `HEAD` source comparison at the same resolution is separately pending; neither request has returned production images.

## Findings, visual checklist, and remaining proof

| Finding | Actual current evidence | Parent or owner action |
| --- | --- | --- |
| Regional danger map is unclear | In the reviewed normal one-front fixture, only Europe is active, but dense yellow rain and clouds cover most of the world map and obscure geography. The production image does not clearly distinguish active Europe from inactive or visited regions. | Correct the owned map layer or asset-state presentation within Part 6's ordinary, warning, visited, and global distinction. Preserve the supplied render evidence. |
| Completed-region marker shows an empty circle | North America is 110/110 with its completion flag set, but `acid_rain_region_completed_6` displays the empty native checkbox frame. The source uses `frame = 1`, and the rendered sprite records the first of two frames. | Verify and use the native checked frame for all seven completion markers, then capture matching owner-applied before/after evidence. |
| Coverage graphic overstates the exact label | The label is 35% (280/800), while four full 53-pixel segments occupy 212 of the 536-pixel frame width, about 39.55%. The track interior is also difficult to distinguish against the board. | Resolve the segmented-meter adaptation against Part 6's exact coverage display and provide its acceptance basis or correct the presentation. |
| Visible-value budget remains open | Current Air, lifetime Air added, remaining Air allowance, worldwide deaths, coverage, and Preparedness are six simultaneous main numerical quantities before front and national counts. | Reconcile the accepted ledger design with the four-value hard cap. The active-versus-history wording alone is not approval for an exception. |

Normal source click regions are separate, enabled, and aligned with the five visible navigation/display controls.
The footer's real native sprite is 123x36 despite its `GFX_button_123x34` name, and the rendered labels use centered native text metrics without normal-state overflow.
These checks do not execute click effects, keyboard shortcuts, or native tooltip timing.

The required `.agents/skills/chaos-redux-scripted-gui/references/visual-review.md` path is absent.
The complete inline checklist in the read scripted-GUI skill was applied, and the missing requested companion file remains a reference-coverage gap.

Pending visual checks: painted versus logical bounds; usable background interiors; text label centering on both axes; font baseline and `Main_14` width/height; spacing and symmetry; scaling; clipping/overflow; z-order; animated/static coherence; visible and enabled state assertions; click-region alignment and overlap; diagnostic warnings; text localization fidelity; and three-resolution placement. The concurrent font edit makes these exact boxes high-priority review targets: `acid_rain_front_card_*_severe_status` and `acid_rain_region_row_*` use `Main_14` with `maxHeight = 14`; front band/window lines and `acid_rain_map_legend` use `maxHeight = 16`; the national strip uses 88–105 pixel text widths with `maxHeight = 16`; `acid_rain_category_status` has 334 pixels width by 28 pixels height. These are clipping/overflow risks to inspect in returned images, not confirmed defects without a render.

No post-fix comparison is applicable: this is a read-only audit and no owner-applied source fix is included. The one honest historical source comparison submitted was current font-owner source versus the exact pre-font `HEAD` source; it timed out and returned no artifacts. Do not compare the current source to itself or report the pre-font `HEAD` source as a post-fix state.

Separate animation ownership: the parent is reviewing the v3 global cloud frames. This review covers their current GUI placement and visual contribution in the production window render; it does not approve the frame artwork package or claim live animation playback.

The mandatory final report remains open for actual full-window, relevant cropped, annotated, hierarchy, click-region, state, resolution, and matching scenario/source evidence for both exact windows. Preserve the returned full/cropped/click-region resources under `docs/plans/033_acid_rain_plans/validation/gui_current_2026_10_07/` and cite every resource and manifest/source revision here. No before/after gate exists until an owner applies a reviewed source fix and this reviewer captures a matched post-change render.

## Explicit blockers and omissions

- `hoi4.gui_inspect` timed out after 600 seconds on both exact windows and again on the exact `acid_rain_world_window` retry. One-state normal `hoi4.gui_render` requests at both 1920x1080 and 1366x768 timed out after 600 seconds and returned no artifacts. The matching pre-font source comparison also timed out after 600 seconds with no artifacts. The 1600x900 resolution and all requested phase/state fixtures remain uncovered. Corrected Vanilla `hoi4.source_lookup` requests succeeded. Visual correctness, hover, click regions, states, resolution behavior, localization output, and current-source diagnostics are unresolved.
- The current 1920x1080 minimal render did not establish whether the one-state request clears the known aggregate-pixel refusal; the route timed out before returning its diagnostics.
- No owner-applied correction exists in this read-only assignment, so no post-change evidence is produced.
- No live game was launched and no desktop control, logs, or shared interfaces were accessed.
- No new reference art was created. The existing accepted scoped reference was reviewed.
- The global v3 source-frame package remains under the parent's separate visual review.

No source or asset simplifications were made. GUI gate completion is blocked on the pending MCP evidence and any visible defect dispositions; parent review and user live-game validation remain outstanding.
