# Event 006 visual-asset audit reconciliation

Date: 2026-09-13.

Disposition: implemented audit and prior repairs retained; HOLD / PARTIAL remains.

This parent receipt reconciles the six bounded visual-family audits performed against the accepted Event 006 Independence Wave asset matrix. It is an implementation receipt, not a completion claim. Existing runtime repairs were preserved, no speculative artwork was added, and no blocked identity, rights, provenance, or reachability gate was promoted.

## Inventory and family receipts

The accepted registry contains 49 asset IDs. The current runtime inventory contains 324 Event 006 DDS files, 1,530 standard-roster flag TGAs for 102 tags, 132 route/formable flag TGAs, 48 achievement states, 104 Event 006 state-puzzle pieces, 64 registered leader portrait DDS files, 121 focus icons, 43 idea or national-spirit icons, 69 decision/category DDS files, 16 report/news/super-event scenes, eight animation DDS files, and the 700x500 Statehood Ledger panel.

The static-icon receipt `006_static_icon_audit_repair_2026-09-13.md` individually reviewed the 13 focus families, eight idea families, 12 decision or mission families, all 16 achievement triplets including Assyria, and the authorized FORM-05 and FORM-48 emblems. All final source, processed, and DDS outputs pass family-specific dimensions, alpha, pixel-equality, readability, canonical-reference, and runtime-path checks. No repair was justified.

The scene-art receipt `006_event6_scene_art_audit_2026-09-13.md` individually reviewed 23 final DDS assets and their source and processed chains, covering report, news, super-event, panel, category, regional-report, and FORM-05/FORM-48 emblem art. All final outputs decode at the expected consumer size and match their processed sources. No crop, clipping, matte, alpha, aspect, or processing repair was justified.

The portrait receipt `006_event6_portrait_asset_audit_2026-09-13.md` individually reviewed the pre-cleanup 70 runtime 156x210 DDS files at native and 4x nearest-neighbour scale, 64 GFX texture mappings, 72 character references, and the flat source shelf with its sole `processed` child. The bounded cleanup receipt `006_event6_portrait_orphan_cleanup_2026-09-13.md` then removed the six unregistered legacy outputs from the engine-facing folder after the source and processed evidence was confirmed. The current runtime therefore contains 64 registered portrait DDS files with no unconsumed Event 006 portrait output; 13 supplied grounded rows remain blocked by identity, role/date, rights, or consumer gates.

The flag receipt `006_event6_flag_asset_audit_2026-09-13.md` reviewed all 1,530 standard tag ladders and 132 route/formable ladders through decoded contact sheets and exact TGA checks. All accepted ladders are complete, upright, opaque, correctly dimensioned, and in the engine-required flag roots. No runtime flag file was changed. Provenance and identity gates remain open for BWX, chunk-3, NWE aliases, GLC, CHU, ASY, MFX, several route packages, and the YAK cosmetic-definition boundary; the BLX checksum ledger was reconciled to the verified runtime TGA hashes without changing TGA bytes.

The animation receipt `006_event6_animation_asset_audit_2026-09-13.md` individually reviewed all 16 authored source states, chroma-removed intermediates, processed frames, four sheets, four static fallbacks, GIF previews, and eight runtime DDS files. Frame counts, order, dimensions, anchors, alpha bounds, sheet widths, fallback equality, and DDS round trips pass. The bounded follow-up `006_event6_animation_fallback_wiring_repair_2026-09-13.md` adds the installed vanilla `*_animated_static` registry aliases and `INGAME`/`transparencecheck` properties; the GUI inspector now resolves all four fallback siblings. The four families remain `needs_user_review` because the source masters are opaque chroma-key RGB and the documented remover helper is absent from this checkout, while the offline GUI route cannot prove live blendframe playback.

The GUI receipt `006_event6_asset_gui_repair_2026-09-13.md` inspected the Statehood Ledger with the required GUI MCP route at 1920x1080 and uiScale 1. Explicit five-tab fixtures render without the empty-fixture prose overprint or dynamic-token placeholders, and the active-value crop is readable on unchanged source. No unambiguous GUI source defect was established. Runtime category visibility, dynamic tab isolation, click-region fidelity, blendframe playback, and the accepted five-value contract remain unresolved.

## Runtime wiring and repair state

The existing accepted repairs remain in place: the two isolated magenta/alpha spill pixels were removed and reconverted; ASSET-004 was restored to strict grayscale; invalid idea and decision picture references were redirected to registered same-family sprites; the Statehood Ledger icon footprint uses the accepted 0.75 scale; animation sheets retain exact 5/3/4/4 frame families; and the merged Event 006 registries resolve the runtime texture paths with correct case.

The current interface scan finds no Event 006 runtime texture reference into `docs/assets/`, no missing texture path, no unconsumed Event 006 DDS file, and no duplicate Event 006 sprite identifier in the audited registries. The four special category `picture =` consumers intentionally remain in `interface/visual_consistency_repair.gfx` because their 114x101 presentation family is distinct from the four 52x40 Event 006 category icons; this is documented wiring, not an orphan or cross-family resize. The four animated families now also expose the vanilla-compatible `*_animated_static` aliases documented in `006_event6_animation_fallback_wiring_repair_2026-09-13.md`; these aliases reuse the audited static DDS bytes and do not add art.

The verified BLX normal, medium, and small runtime flag hashes were reconciled in `docs/assets/006_independence_wave/form09_balkan_federation_flag_2026_08_09/checksums.json`; all five ideology aliases in each size family now match the current engine-facing TGA bytes.

The separate strict-origin repair receipt `006_event6_decision_runtime_audit_2026-09-13.md` confirms that player-facing Event 006 categories, decisions, missions, and costs remain gated by a real active Event 006 origin. No pre-event pressure, queue, cost, category, or GUI surface was added or exposed by the asset audit.

## Validation

`python .tools/audit_event6_flags.py --strict` reports 102 complete Event 006 standard flag families and zero incomplete families.

`python .tools/audit_event6_gui_matrix.py` passes the five-tab, four animation-sibling, frame-cleanup, and static/animated source contract.

`python .tools/audit_event6_scenario_matrix.py` passes all 32 SCN-008 cells and eight edge cases.

The parent DDS/path census confirms that the reviewed runtime DDS files decode, the family dimensions match their consumers, all 435 unique Event 006 texture paths resolve, and no runtime registry points into `docs/assets/`. The family receipts provide the required source, processed, final DDS, native-size, enlarged, contact-sheet, and consumer evidence for the surfaces they own.

No live Hearts of Iron IV launch, save/load proof, or user-owned RunPod portrait validation was performed. The installed GUI and weighted-logic MCP routes remain read-only and incomplete for dynamic runtime state and full probability pools.

## Remaining blockers and simplifications

ASSET-005 remains `needs_user_review` for slot-23 audio rights and firing or dispatch reachability even though its image passes.

ASSET-006 remains `needs_user_review` for host, collision, and formable reachability even though its image passes.

ASSET-039 remains `needs_user_review` for live dynamic GUI state, click regions, blendframe playback, and the preserved five-value display contract.

ASSET-044 remains visually complete but provenance, rights, alias ownership, and route-admission gates remain open for the families named above.

ASSET-045 remains blocked for the 13 supplied grounded portrait rows; no identity substitution or speculative wiring was made. The six legacy unregistered DDS outputs were removed from runtime by `006_event6_portrait_orphan_cleanup_2026-09-13.md` and remain represented by preserved source/processed evidence.

ASSET-046 remains blocked beyond the authorized FORM-05 and FORM-48 art because unresolved formable identities, league-emblem admission, and package reachability do not authorize generic emblems.

No asset simplification, cross-family substitute, fake transparency, fallback image, invented source, or unapproved replacement was introduced by this audit.

## Parent integration follow-up

The parent reopened the icon, flag, portrait, animation, and panel contact sheets and confirmed the family-specific visual evidence at review scale. A read-only runtime registry census found 503 Event 006 texture references across the audited GFX registries, zero missing files, zero references into `docs/assets/`, and 263 unique Event 006 sprite identifiers with no duplicate IDs. The prescribed achievement processor audit passed all 16 Event 006 achievement triplets. The accepted spec README, acceptance checklist, package manifest, and simplifications ledger now point to the 2026-09-13 completion refresh and asset reconciliation as the current bounded authority while retaining **HOLD / PARTIAL** and all user-owned gates.

## Working asset audit table

The table is the parent-level crosswalk for all 49 accepted asset IDs. The linked family receipts expand each row to the individual source, processed, final DDS/TGA, native-size, enlarged, and consumer reviews; `fixed` records a source or wiring repair already applied, while `needs_user_review` and `blocked` are non-art acceptance gates rather than unreviewed pixels.

| Asset | Asset family | Gameplay consumer | Sprite or registry | Source or master | Final runtime path | Expected / actual | Alpha or frame treatment | Visual defects | Wiring defects | Repair performed | Final status |
|---|---|---|---|---|---|---|---|---|---|---|
| ASSET-001–003, 048 | Report-event scenes | `chaosx.nr6.2`, regional report events, FORM-03 | `interface/006_independence_wave_small_assets.gfx` report sprites | `docs/assets/006_independence_wave/source_png/` and package report masters | `gfx/event_pictures/006_independence_wave/` | 210x176 / matched | Transparent report-card corners and opaque scene body | None after native/enlarged review | None | Preserved existing report-card treatment | pass |
| ASSET-004 | News-event scene | `chaosx.nr6.35` | `GFX_news_event_006_asset_004_league_congress` | `source_png/event_pictures/news_event_006_asset_004_league_congress_source.png` | `gfx/event_pictures/006_independence_wave/news_event_006_asset_004_league_congress.dds` | 397x153 / matched | Opaque strict grayscale | Magenta spill removed in prior repair | None | Removed two spill pixels and reconverted DDS | fixed |
| ASSET-005–006 | Super-event scenes | Super-event slots 23 and 24 | `GFX_super_event_006_asset_005_league_formation`, `GFX_super_event_006_asset_006_revisionist_milestone` | `source_png/super_events/` | `gfx/super_events/006_independence_wave/` | 457x328 / matched | Opaque full-canvas scene | None | Slot-23 audio/dispatch and slot-24 reachability remain external gates | No image change justified | needs_user_review |
| ASSET-007–019 | National-focus icons | Event 006 shared focus tree | `interface/006_independence_wave.gfx` goal sprites | `docs/assets/006_independence_wave/processed_png/focuses/` and package masters | `gfx/interface/goals/006_independence_wave/` | 94x86 / matched | Opaque icon family with vanilla goal treatment | None | No stale or cross-family focus references | No repair justified | pass |
| ASSET-020–026, 049 | Idea and national-spirit icons | Lifecycle ideas and Post-Release Instability | `interface/006_independence_wave.gfx` idea sprites | `docs/assets/006_independence_wave/processed_png/ideas/` | `gfx/interface/ideas/006_independence_wave/` | 64x64 / matched | Alpha-backed compact symbols | None | Invalid picture references redirected to registered same-family sprites | Redirected the affected idea and decision picture references in the prior repair | fixed |
| ASSET-027–038 | Decision and mission icons | Event 006 decisions and missions | `interface/006_independence_wave.gfx` decision sprites | `docs/assets/006_independence_wave/processed_png/decisions/` | `gfx/interface/decisions/006_independence_wave/` | 32x32 / matched | Alpha-backed high-contrast silhouettes | None | Invalid or missing references repaired to registered same-family sprites | Repaired decision and mission sprite paths | fixed |
| ASSET-039 | Scripted GUI panel | `independence_wave_status_window` | `GFX_independence_wave_status_panel` | `source_png/gui/independence_wave_status_panel_source.png` | `gfx/interface/006_independence_wave/independence_wave_status_panel.dds` | 700x500 / matched | Opaque panel art with open functional field | None in panel art | Dynamic visibility, click-region, blendframe, and five-value runtime evidence remain open | Moved warning into existing tab gap and normalized icon footprint | needs_user_review |
| ASSET-040–043 | Animated GUI state families | Statehood Ledger state cues | Four frame-sheet and fallback registries in `interface/006_independence_wave.gfx` | `docs/assets/006_independence_wave/processed_png/gui/animations/` | `gfx/interface/006_independence_wave/animations/` | 5/3/4/4 frames / matched | Real frame sheets, static fallbacks, alpha-preserving DDS | None in reviewed frames | Blendframe playback, source-remover provenance, and live selection remain open | Preserved frame order, anchors, fallbacks, and corrected sheets; added vanilla-compatible `*_animated_static` aliases without changing DDS bytes | needs_user_review |
| ASSET-044 | Country flags | Event 006 countries and route identities | Engine flag basenames and cosmetic aliases | Package source masters and processed ladders | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | 82x52, 41x26, 10x7 / matched | Opaque flat TGA ladders | None | Provenance, alias ownership, and package admission remain open for named families | Reconciled BLX checksum metadata; no image rewrite | needs_user_review |
| ASSET-045 | Leader and commander portraits | Event 006 character registry and package effects | Portrait sprites in three Event 006 GFX registries | Flat `docs/assets/portraits/006_independence_wave/` source shelf plus `processed/` evidence | `gfx/leaders/006_independence_wave/` | 156x210 / matched | Opaque legacy BGRA DDS; no advisor-card substitute | None across the 64 registered runtime DDS files; six legacy orphan outputs removed | Thirteen supplied grounded rows remain consumer/rights gated | Removed six unconsumed runtime outputs; preserved identity-safe wiring with no speculative relabel or substitute | blocked |
| ASSET-046 | Formable flags and emblems | FORM-05, FORM-48, League/formable surfaces | Flag roots plus `interface/006_independence_wave_small_assets.gfx` emblem sprites | FORM-05 and FORM-48 package masters | `gfx/flags/` ladders and `gfx/interface/006_independence_wave/emblems/` | Flag triplets and 128x128 emblems / matched | Opaque flags and alpha-backed emblems | None | Wider formable identity, League emblem admission, and reachability remain open | Preserved distinct FORM-05 and FORM-48 art | blocked |
| ASSET-047 | Achievement icon triplets | Sixteen Event 006 achievements | Achievement IDs under engine root | `docs/assets/006_independence_wave/processed_png/achievements/` | `gfx/achievements/` | 64x64 triplets / matched | Normal, grey, and not-eligible state triplets | None | No runtime path defect | Reconciled and audited all 16 triplets | pass |
