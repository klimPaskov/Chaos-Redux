# Event 006 visual-asset audit completion update

Date: 2026-09-12.

Disposition: **implemented repairs with HOLD / PARTIAL completion status**.

This update records the current parent review of the complete Event 006 visual-asset audit requested for Independence Wave. The full row-by-row working table remains authoritative in `006_event6_visual_asset_audit_2026-09-03.md`; this update reconciles its evidence with the later family-specific audits and the current runtime registry. It does not promote blocked source, rights, identity, GUI-state, audio, or reachability gates.

## Inventory and consumer coverage

The accepted matrix contains 49 asset IDs. The current audit reconciles 330 Event 006 DDS files, 1,530 flag files for 102 tags across five ideology variants and three size ladders, 48 achievement states, 104 state-puzzle pieces, 70 Event 006 portrait DDS files, 121 focus icons, 43 idea or national-spirit icons, 69 Event 006 decision-tree DDS files, 16 report/news/super-event scene DDS files, eight animation DDS files, and the dedicated Statehood Ledger panel.

The active Event 006 interface registry is `interface/006_independence_wave.gfx`, `interface/006_independence_wave_small_assets.gfx`, `interface/006_independence_wave_iw093_iw098_focus.gfx`, and `interface/006_independence_wave_portraits_registry.gfx`, with `interface/006_independence_wave.gui` as the owned GUI definition. No active Event 006 texture reference points into `docs/assets/`, and the merged registry resolves every accepted runtime texture path with correct filename case.

The portrait archive remains exactly the requested layout: original source files are flat in `docs/assets/portraits/006_independence_wave/`, the only child directory is `processed/`, and the parent contains no 156x210 DDS files. Processed portrait evidence is not a runtime consumer.

## Repairs verified

The accepted visual repair set is complete for defects that can be corrected from existing admitted source material.

| Repair | Evidence | Status |
| --- | --- | --- |
| Two isolated magenta/alpha spill pixels | Existing processed IW-098 focus and FORM-05 decision previews were repaired, reconverted, decoded, and visually checked at native size. | `fixed` |
| ASSET-004 news image | Strict grayscale was restored in the processed PNG and runtime DDS; decoded runtime pixels match the processed image. | `fixed` |
| Missing idea and decision sprites | Six patron-pressure references, five league-membership references, and two Siberian network references now resolve to registered same-family sprites. | `fixed` |
| GUI icon scale | The 11 status-window idea footprints were corrected from the fractional 0.72 scale to the accepted 0.75 footprint. | `fixed` |
| Animated status families | Four authored frame-sheet packages retain exact frame counts, stable anchors, static fallbacks, and decoded DDS equality. Documentation now matches `play_on_show = yes`. | `pass` |
| Focus, idea, decision, category, achievement, report, news, and flag families | Native dimensions, alpha treatment, crop, edge safety, readability, GFX paths, and consumer references were checked against the matching vanilla/Chaos Redux families. | `pass` |

No cross-family resize, recolour, renamed vanilla substitute, fake checkerboard, opaque alpha-backed fallback, or unapproved replacement was introduced. No new visual asset family was invented merely because a gameplay object exists.

## Current status gates

| Asset IDs | Final status | Remaining gate |
| --- | --- | --- |
| ASSET-001–004, ASSET-007–038, ASSET-040–043, ASSET-047–049 | `pass` or `fixed` | No remaining source-level visual defect in the audited consumer. |
| ASSET-005 | `needs_user_review` | Slot-23 audio rights and firing reachability remain open; the image itself passes. |
| ASSET-006 | `needs_user_review` | Host, collision, and formable reachability remain partial; the image itself passes. |
| ASSET-039 | `needs_user_review` | GUI MCP inspection/render exists, but dynamic tab visibility, click-region fidelity, blendframe playback, and the four-value content budget are not accepted. |
| ASSET-044 | `needs_user_review` | The flag pixels and ladders pass, while BWX/chunk-3/NWE-alias/GLC/CHU/ASY provenance, rights, or cross-event ownership receipts remain open. |
| ASSET-045 | `blocked` | Thirteen supplied grounded portrait rows lack an authoritative Event 006 consumer or closed identity/role/date/rights gate. Six unregistered runtime portrait DDS files remain documented `unused_orphan` evidence and were not deleted speculatively. |
| ASSET-046 | `blocked` | FORM-05 and FORM-48 emblems pass, but the remaining formable identities and the shared league emblem lack an accepted identity, source, rights, or stable consumer. |

The Statehood Ledger GUI remains an explicit design/content blocker rather than a hidden renderer failure. Its baseline render shows ten simultaneous mechanic values, bottom-right tab-panel overprint in the empty fixture, and a warning/text collision; no layout or scripted-GUI rewrite was applied without an accepted state fixture and content-priority decision.

## Validation evidence

The focused Event 006 validators currently pass: allocator strict, country API, strict flag families, FORM-16, Statehood Ledger semantic matrix, and the SCN-008 scenario matrix. The allocator still reports the exact `3/4/5/7/10` ladder and no pre-event category, mission, cost, or queue. The GUI MCP route completed read-only inspection and rendering for `independence_wave_status_window`, but its offline renderer does not execute dynamic tab visibility or `buttonstate_blendframes.lua`; no live or save/load claim is made.

The family-specific evidence is recorded in `006_event6_icon_asset_audit_2026-09-03.md`, `006_event6_animation_asset_audit_2026-09-03.md`, `006_event6_report_super_event_asset_audit_2026-09-03.md`, `006_event6_visual_asset_wiring_repair_2026-09-03.md`, `006_event6_portrait_consumer_gate_2026-08-31.md`, `006_event6_portrait_visual_repair_audit_2026-09-06.md`, `006_event6_flag_formable_visual_repair_2026-09-06.md`, and `006_event6_status_gui_repair_2026-09-12.md`.

No live Hearts of Iron IV launch, save/load proof, or unverified source/rights promotion was performed. Event 006 remains **HOLD / PARTIAL** until the listed user-owned gates close.
