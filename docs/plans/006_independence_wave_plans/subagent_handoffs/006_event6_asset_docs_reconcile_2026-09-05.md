# Event 006 visual-asset documentation reconciliation handoff

Date: `2026-09-05` (Europe/Kyiv).

Owner: `chaosx_documentation_curator`.

Scope: reconcile the Event 006 visual-asset audit against the accepted asset registry, current portrait, flag, emblem, GUI, focus, event, map, source-of-truth, and resume records.

Disposition: `implemented` as a documentation-only reconciliation handoff; no unresolved visual asset was promoted.

## Change boundary

Only this handoff was added.

No gameplay, localisation, GFX, GUI, runtime asset, source asset, flag, portrait, emblem, spreadsheet, or central-admission file was edited.

No file was staged or committed.

The strict no-pre-event surface and all no-fallback, source, identity, rights, era-fit, community-review, and redistribution gates remain fail-closed.

## Source-of-truth map

| Surface | Current authority | Reconciled evidence and disposition |
| --- | --- | --- |
| Accepted design | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\specs\006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` and its 2026-07-16 user-direction record | Accepted visual source modes, men-only Event 006 personal/command/collective portraits, historical-source and rights gates, truly fictional-only generated portraits, and no custom advisor icons remain the design basis. |
| Accepted asset IDs | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\matrices\006_asset_family_registry.csv` | All 49 accepted asset IDs remain in scope; the registry is not evidence that every row is runtime-complete. |
| Aggregate visual audit | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_visual_asset_audit_2026-09-03.md` | Current inventory remains 330 Event 006 DDS files, 1,530 flag files for 102 tags across five variants and three ladders, 48 achievement states, and 104 Event 006 state-puzzle pieces. The audit's repairs are retained, but ASSET-005, ASSET-006, ASSET-039, ASSET-044, ASSET-045, and ASSET-046 remain gated. |
| Exact portrait routing | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_portrait_wiring_reconciliation_2026-08-30.md` | 51 selected supplied DDS inputs yield 38 safe hash-matching source-to-runtime mappings and 13 unresolved inputs; all selected rows remain `source_placeholder`, with no `replacement_pending` or provider-backed styled-final promotion. |
| Portrait semantic and rights gate | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_portrait_gate_research_2026-09-05.md` | The same 13 rows remain `BLOCKED` / `source_placeholder_candidate_hold`; none has a safe identity, role/date, rights, or admitted consumer closure. |
| Portrait archive layout/count | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_portrait_archive_count_reconciliation_2026-09-05.md` | The archive has 59 direct original image files and 72 files under its single `processed` child; no normalized 156x210 archive file or runtime admission changed. |
| Flag provenance | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_flag_provenance_research_2026-09-05.md` | The reviewed 19 main tag families have complete technical ladders, but unresolved identity, era, community, provider-term, redistribution, map, or cross-event ownership gates remain. NWE unsuffixed bases may remain technically handed off; NWE suffix aliases remain `needs_user_review`; BWX remains blocked/evidence-only; all 14 chunk-3 rows remain `needs_user_review`; GLC is conditional carrier reuse; CHU and ASY opening families remain `needs_user_review`. |
| Formable and league emblems | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_formable_emblem_research_2026-09-05.md` | Only the existing FORM-05 `MIX` and FORM-48 `PFX` family emblems are present and distinct; FORM-13, FORM-43, unresolved families, and the shared league emblem remain `blocked`. No flag, faction reference, generic seal, or family emblem was reused as a substitute. |
| GLC portrait/flag edge cases | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_iw015_glc_portrait_gate_2026-09-03.md` and `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_iw015_glc_flag_identity_2026-09-03.md` | GLC carrier identity is preserved conditionally; the actual democratic opening and redistribution/period gates remain `needs_user_review`. The older painted-output `styled_final` wording and current `source_placeholder` wording remain a parent-owned terminology decision. |
| GUI follow-up | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_gui_scale_mcp_retry_2026-09-05.md` | The 0.72-to-0.75 source repair is applied. The exact fixture inspected 48 elements and rendered aggregate and isolated states, but dynamic tab visibility, live click behavior, and blendframe playback remain unproved; ASSET-039 stays `needs_user_review`. |
| Current ledger and resume | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\006_source_of_truth_map.md` and `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\006_independence_wave_resume_packet.md` | Both were reviewed and left unchanged. The current 32/29/40/161 boundary, absolute no-pre-event invariant, and **HOLD / PARTIAL** status remain consistent with the visual audit; the source map is parent-owned and may have concurrent edits. |

The implementation evidence above describes what is present and does not establish acceptance of unresolved design, identity, rights, or runtime claims.

## Read-only MCP evidence used before reconciliation

The installed read-only HOI4 routes were called for the represented Event 006 event, GUI, focus, and map surfaces.

The exact bounded event call used `mode = lint`, selector `{ kind: event, eventId: chaosx.nr6.1 }`, downstream direction, depth `1`, 40 nodes, 80 edges, `expandHelpers = false`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `EVENT_INSPECTED_PARTIAL` at revision `4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f`, graph hash `5e3d139e6f05e68b3a6113d31899826893cdcd622d7328cf49b05b1daa10c66f`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7075a49cef9421a74c2c5f097108ede5cfcea051f0bc1e3ff99579f6da616308/de1f50f7e6dc4ea858f77805ae0c998d19ec537e33cdb584d01aca1a060ab119/event-lint-4520c3ceb2ac.json`.

The event result had validation `false` because workspace-wide helper and lifecycle projections were deferred, reported one aggregate blocking diagnostic in the data summary, and skipped zero sources; it is partial structural evidence only.

The exact GUI call used `windowName = independence_wave_status_window`, scenario `{ id: independence_wave_status_default }`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `GUI_INSPECTED` with validation `true`, shared revision `14dacd1045e21d94165dd9c7cf1172a77f677e8db24a4bfd2e35ae2b6dea566a`, 48 inspected Event 006 elements, 64 nonblocking visible-overlap findings, four animated-sprite static-fallback warnings, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d75768538354cfe1910cbbcdf5bd34f91cfef8032159fb256b29b78b5b42ed52/c800dad0f474fe51bca0b343ce1b3319c21bd0736be3c8d95ee4003787bd0315/gui-inspect.14dacd1045e21d94.json`.

The GUI result proves source-graph extraction and bounded diagnostics only; the current 2026-09-05 GUI render handoff remains the authority for aggregate and isolated render limitations.

The exact focus call used `relativePath = common/national_focus/006_independence_wave_focus.txt`, `treeId = independence_wave_focus_tree`, `mode = national`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `FOCUS_INSPECTED` with validation `true`, revision `a2638209c7ad241582f37028815f277a8026bf230f569f20127eca75653c6534`, 184 focuses, 195 connectors, zero crossings, zero node intersections, zero long connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7547891339174763077bf9914ececbf8c4246ead419a2da2037b5c8a621b31e9/6bc1d4296416b3668e32e1770c70d490902c275420b3fa5cda2f30c23158a9d2/focus-inspect.a2638209c7ad2415.json`.

The only focus warning is the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

The bounded map call inspected states `123` and `171` with an overview in workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `MAP_INSPECTED` for two selected states with validation `false` because the workspace-wide result retained 2,654 omitted position/port errors, including `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`; the selected state and network checks passed, and no map rewrite was performed.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3be524bfb6662f34a6d6e891f119bfec8ddb18fa8f3e4de5e319d3089ebb4854/75a97c1d8f2cfad12fce5e3f280d6ec69db94434bd5f869135ebb6126e7c5bc9/map-inspect.f307a444eabf8bd0.json`.

These MCP receipts are evidence for the documentation boundary and do not override the accepted design, asset provenance, rights gates, or parent review.

## Plan and handoff disposition table

| Document or surface | Disposition | Acceptance basis, implementation evidence, reason, replacement, or blocker |
| --- | --- | --- |
| `006_asset_family_registry.csv` | `accepted and queued` | Accepted registry and Part 7 visual direction define the 49-row contract; current evidence does not promote unresolved rows. |
| `006_event6_visual_asset_audit_2026-09-03.md` | `implemented` | Aggregate audit is the current visual inventory and repair authority; its dated title is retained because the 2026-09-04 and 2026-09-05 follow-ups are explicitly linked. |
| `006_portrait_wiring_reconciliation_2026-08-30.md` | `implemented` | Exact 51/38/13 routing matrix remains valid; the 2026-09-05 portrait gate supplements it rather than replacing the exact-file evidence. |
| `006_event6_portrait_gate_research_2026-09-05.md` | `blocked` | All 13 unresolved supplied rows lack a safe identity/role/date/rights/consumer closure; no substitute is authorized. |
| `006_event6_portrait_archive_count_reconciliation_2026-09-05.md` | `implemented` | Physical archive counts and the single `processed` child were reconciled without runtime or admission change. |
| `006_event6_flag_provenance_research_2026-09-05.md` | `implemented` | Bounded provenance review confirms technical ladders but leaves the named identity, era, rights, community, and ownership rows gated. |
| `006_event6_formable_emblem_source_audit_2026-09-02.md` | `superseded` | Its technical inventory remains useful, but current unresolved emblem research is now `006_event6_formable_emblem_research_2026-09-05.md`; no existing FORM-05 or FORM-48 emblem is a universal league substitute. |
| `006_event6_formable_emblem_research_2026-09-05.md` | `blocked` | FORM-13, FORM-43, and the shared league emblem lack a defensible accepted source/identity/consumer; no asset was created or promoted. |
| `006_event6_iw015_glc_portrait_gate_2026-09-03.md` and `006_event6_iw015_glc_flag_identity_2026-09-03.md` | `unresolved` | GLC carrier preservation is conditional, democratic opening period/rights remain open, and `styled_final` versus `source_placeholder` terminology requires parent decision. |
| `006_event6_gui_scale_mcp_retry_2026-09-05.md` | `implemented` | Source-scale repair and bounded inspect/render evidence are recorded; dynamic tab, click, and animation proof remain open. |
| `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | `implemented` | Both current ledgers were reviewed and left unchanged because their current asset counts and fail-closed boundary do not contain a proven contradiction; the source map remains parent-owned. |

## Contradictions and stale crosswalks

| File and evidence | Finding | Action in this handoff |
| --- | --- | --- |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\quality\package_manifest.md:69,71` | Line 69 says the post-change GUI retries timed out with no render pass, while line 71 records the completed 2026-09-05 inspect and `GUI_RENDERED` aggregate. | Not patched because the parent restricted this tranche away from broad manifests; parent should replace the timeout-only sentence with the current retry wording while retaining the dynamic-state limitation. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\quality\package_manifest.md:15,17` | The current reconciliation first presents the older Event MCP revision `2725045...` and then presents the 2026-09-05 refresh `fa39cc...` as current. | Preserve both only after relabelling the older paragraph as a prior dated receipt; parent decision required because the fresh bounded call below is a different projection. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_visual_asset_audit_2026-09-03.md:105` | The aggregate audit links the 2026-08-30 portrait matrix and 2026-09-03 GLC flag handoff but omits the newer 2026-09-05 portrait, archive-count, flag-provenance, and emblem-research follow-ups. | No source audit rewrite was made; parent should add current supplemental links if the audit remains the public crosswalk. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\README.md:31` and `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\quality\spec_acceptance_checklist.md:31` | Both retain the correct 49-row/count/status summary but do not name the latest 2026-09-05 portrait gate, archive-count, or emblem-research handoffs. | No broad spec README/checklist edit was made; add links only if parent wants the accepted-spec index to expose every current follow-up. |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\assets\006_independence_wave\manifest.md:131-145` | The wording that ASSET-046 is partially produced for four formable families can be read as emblem coverage, while the current emblem research says only FORM-05 and FORM-48 have separate emblems; the surrounding text appears to describe flag coverage. | Not edited because this manifest has concurrent changes; parent should clarify “flag packages” versus “UI emblems” in one precise sentence if needed. |
| `006_event6_iw015_glc_portrait_gate_2026-09-03.md` versus `006_portrait_wiring_reconciliation_2026-08-30.md` and `006_event6_portrait_gate_research_2026-09-05.md` | The older GLC gate preserves historical painted-output `styled_final` wording, while current exact-input and 2026-09-05 semantic gate records use `source_placeholder`; the latest gate explicitly keeps the lifecycle terminology unresolved. | Retain both dated evidence records and require the parent decision; no relabel or promotion was performed. |
| Current source map/package entries versus this exact Event MCP call | The current 2026-09-05 full-refresh references report zero blocking diagnostics at revision `fa39cc...`, whereas this bounded downstream retry reports one aggregate blocking diagnostic at revision `4520c3...` because helper/lifecycle projections were deferred. | Record both as scenario/projection-specific evidence; parent owns the current Event MCP status wording. |

## Duplicate and superseded-document list

No document was deleted or merged.

`006_event6_formable_emblem_source_audit_2026-09-02.md` is superseded for current unresolved emblem research by `006_event6_formable_emblem_research_2026-09-05.md`, but its technical inventory remains useful historical evidence.

`006_event6_gui_fractional_scale_repair_2026-09-04.md` remains the source-change record and is superseded for current MCP route status by `006_event6_gui_scale_mcp_retry_2026-09-05.md`.

`006_portrait_wiring_reconciliation_2026-08-30.md` is not superseded for exact 51/38/13 file routing; `006_event6_portrait_gate_research_2026-09-05.md` is its semantic and rights-gate supplement.

`006_event6_iw015_glc_flag_identity_2026-09-03.md` remains the GLC-specific flag record; `006_event6_flag_provenance_research_2026-09-05.md` is the aggregate provenance supplement, not a replacement for GLC-specific identity evidence.

The aggregate visual audit remains the inventory authority; its later dated GUI, flag, emblem, portrait, and archive handoffs are supplements rather than duplicate inventories.

## Stale prompt or instruction list

`C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\006_independence_wave_specs\prompts\independence_wave_asset_prompt.md` remains an accepted design/production prompt, not a current status ledger, and is not stale solely because it describes the complete intended package.

No stale prompt was found that authorizes fallback art, generic emblems, copied vanilla binaries, unapproved portrait promotion, or pre-event visibility.

The stale operational wording identified above is in the package manifest and aggregate audit crosswalk, not in an asset-production prompt.

## Markdown hard-wrap audit

The reviewed current audit, handoff, spec, resume, and source-map sections contain no accidental mid-sentence or mid-clause physical line breaks.

Intentional Markdown structures, table rows, list items, code spans, and historical evidence paragraphs were preserved.

## Recommended parent decisions

1. Replace or relabel the package-manifest timeout-only GUI sentence and the older current-section Event MCP paragraph.

2. Decide whether the aggregate visual audit, accepted-spec README, checklist, source map, and resume packet should cross-link all four 2026-09-05 asset follow-ups without duplicating their evidence.

3. Resolve the GLC portrait lifecycle vocabulary and the exact 1936 democratic-opening flag/rights decision.

4. Resolve NWE suffix ownership, BWX identity/map/provenance, and the fourteen chunk-3 identity/community/rights rows without removing or promoting aliases.

5. Decide FORM-13, FORM-43, and universal-versus-route-specific league emblem identity and consumer before any ASSET-046 production.

6. Reconcile the scenario-specific Event MCP diagnostic wording and preserve its helper/lifecycle deferral as an evidence limitation.

7. Keep ASSET-039 open until dynamic tab, click-region, and blendframe behavior is evidenced by an appropriate route, and keep ASSET-005/006 open until audio/firing and reachability gates close.

## Proposed cleanup if parent patching is not authorized

Leave all existing asset bytes, GFX, GUI, runtime, and localisation files unchanged.

Add only cross-reference sentences to the accepted-spec README, resume packet, and source map that point to the 2026-09-05 portrait, flag, emblem, archive-count, and GUI handoffs.

Relabel old package-manifest and aggregate-audit sentences as historical or prior receipts without changing their evidence.

Do not promote any blocked or `needs_user_review` row, delete NWE aliases or orphan portraits, copy vanilla GLC files, or create a generic/shared emblem.

## Validation and remaining risks

Targeted `rg` checks confirmed the current 49/330/1,530/48/104 aggregate counts, the 51/38/13 portrait counts, the ASSET-005/006/039/044/045/046 dispositions, and all four 2026-09-05 follow-up paths.

The targeted Markdown hard-wrap scan found no possible accidental prose wraps in the reviewed files.

The read-only Event, GUI, focus, and map MCP calls above were completed before this reconciliation; no write-capable MCP route was used.

No new GUI render, probability inspection, live game launch, save/load, binary asset decode, or spreadsheet check was run by this documentation-only tranche because current dated evidence already covers those surfaces and the parent did not authorize broader validation.

The Event MCP bounded retry and map inspect retain partial/global diagnostic limits, the GUI offline renderer does not execute dynamic behavior, portrait and flag rights remain unresolved, and current asset inventory must not be mistaken for runtime or gameplay completion.

The parent receives this handoff as a documentation record only; no gameplay completion claim is made.
