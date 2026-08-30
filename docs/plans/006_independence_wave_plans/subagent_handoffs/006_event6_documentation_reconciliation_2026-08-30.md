# Event 006 documentation reconciliation handoff

Date: 2026-08-30.

## Scope and disposition

This pass reconciled the Event 006 implementation ledger against the latest dated handoffs and commits without editing gameplay, localisation, assets, the workbook, or generated CSV files.

The whole-event disposition remains **HOLD / PARTIAL** at 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows.

The automatic ladder remains `3/4/5/7/10`, World Collapse also targets `10`, and nothing is visible before Event 006 fires.

The named overview, resume packet, and source-of-truth map already contain parent-owned staged and unstaged edits in the super-event-23 paragraph, so they were intentionally left untouched to preserve that worktree state.

The package manifest received the only in-place reconciliation because it had no competing parent edit; this handoff is the current dated overlay for the three parent-owned operational documents until their existing edits are folded.

## Current source-of-truth map

| Surface | Current authority | Status |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/` and its seven specification parts | Unchanged design authority. |
| Current operational ledger | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | Parent-owned 2026-08-29 authority plus this dated 2026-08-30 overlay. |
| Event overview | `docs/events/006_independence_wave/overview.md` | Parent-owned 2026-08-29 authority; no source count or admission widening is implied by later receipts. |
| Country admission | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_join_effects.txt`, and `006_event6_country_tranche_global_2026_08_30.md` | 32 attested packages and 40 adapters remain authoritative; IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179 remain fail-closed in the latest tranche, with IW-070, IW-071, IW-072, IW-173, and IW-184 verified as admitted package rows. |
| Character source layout | `history/general/006_independence_wave_character_recruitment_registry.txt` and `common/characters/006_independence_wave_characters_registry.txt` | Current working-tree inspection records 25 guarded blocks, 65 recruitment calls, and 58 portrait blocks; the older 54-call/47-reference figures remain historical snapshots and do not admit a package. |
| Focus | `common/national_focus/006_independence_wave_focus.txt` plus the 2026-08-30 focus-gap handoff | Shared tree is 184 focuses and 195 connectors with zero Event 006 geometry diagnostics; package reachability and AI balance remain separate gates. |
| Decision and mission lifecycle | `common/decisions/categories/006_independence_wave_categories.txt` and the 2026-08-30 decision handoffs | Six category shells now require matching setup receipts, and fourteen instant strategic-cost rows use the non-reserving cost display; no package admission or AI value changed. |
| Formable and League | `006_event6_formable_league_completion_2026-08-30.md` and the accepted formable registry/specification | Fourteen reviewed state-puzzle families remain bounded, while 34 registry rows remain fail-closed; FORM-48 remains FSM-gated. |
| Asset registry | `interface/006_independence_wave_small_assets.gfx` and `006_event6_asset_docs_path_reconcile_2026-08-30.md` | Consolidated small-assets registry is current; rights, ownership, alias, emblem, BWX, and chunk-3 blockers remain open. |
| SCN-008 publication | `3ce4b3468`, `713306f2e`, and `006_scn008_publication_boundary_patch_2026-08-29.md` | Success-only source/static publication is closed; live and engine transaction receipts remain unproven. |
| Super-events | `4d81a3227`, `006_event6_super_event_text_rights_handoff_2026-08-30.md`, and the separate audio-rights handoffs | Slot 23 text is approved but audio is blocked; slot 24 KJV wording carries a jurisdiction caveat and WEB requires explicit approval. |

## Latest plan and handoff dispositions

| Commit or handoff | Disposition |
| --- | --- |
| `e2a1403ed`, `006_event6_residual_localisation_cleanup_2026-08-30.md` | Implemented as a localisation-only clarity repair by its owner; no gameplay or catalog change was made, and this curator did not edit localisation. |
| `51da79665`, `006_event6_asset_rights_research_2026-08-30.md` | Research complete; ASSET-046, BWX, chunk-3, AEX, NWE aliases, and row-level metadata remain blocked, hold, or needs-user-review as recorded. |
| `d9d56e1b4`, `006_event6_focus_gap_probe_2026-08-30.md` | Audited and left unchanged; no safe focus patch, no geometry rewrite, and no quantitative AI claim. |
| `4d81a3227`, `006_event6_super_event_text_rights_handoff_2026-08-30.md` | Text research accepted for slot 23 and conditionally accepted for slot 24; no runtime text or audio change. |
| `3ce4b3468` and `713306f2e`, SCN-008 publication handoffs | Implemented and source/static closed; any earlier instruction that the parent must still add the publication gate is superseded by these commits. |
| `cbee847f8`, `006_event6_decision_mission_current_cost_lifecycle_audit_2026-08-30.md` | Implemented as fourteen instant strategic-cost display corrections; costs, effects, lifecycle, and AI weights were not changed. |
| `ce19e6741`, `006_iw179_fsm_portrait_source_gate_retry_2026_08_30.md` | Blocked and fail-closed; no FSM identity, portrait, or fallback was admitted. |
| `730cb572b`, `006_event6_asset_docs_path_reconcile_2026-08-30.md` | Implemented as path-only documentation reconciliation; legacy registry-path references remain explicitly historical. |
| `844a24d2b`, `006_event6_decision_surface_completion_2026-08-30.md` | Implemented as six setup-receipt category gates; no package was promoted and the state-puzzle inspect timeout remains open. |
| `43ddcfc32`, `006_event6_country_tranche_global_2026_08_30.md` | Implemented as the narrow IW-058 setup identity-receipt repair; IW-058 remains central-attestation and Join blocked. IW-070, IW-071, IW-072, IW-173, and IW-184 remain verified admitted rows rather than a new boundary change. |
| `711ca668e`, `006_event6_formable_league_completion_2026-08-30.md` | Audited with no source patch; the 14-family formable boundary and 34-row fail-closed boundary remain. |
| `7bb338554`, `006_allocator_runtime_probe_no_change_2026-08-30.md` | Audited with no source patch; the zero-country observation is runtime-unresolved and no fallback is authorized. |

## Contradictions and corrections

1. The 2026-08-29 overview, resume packet, and source map predate the 2026-08-30 receipts; this handoff and the package-manifest section provide the dated current overlay, while the parent-owned edits remain preserved for later fold-in.

2. `006_event6_post_p0_completion_audit_2026-08-29.md` contains an earlier parent-patch instruction before its later completion addendum; `3ce4b3468` and `713306f2e` are the current source/static authority and the earlier instruction is superseded.

3. `006_event6_asset_rights_research_2026-08-30.md` records that the FORM-48 package manifest still says sprite registration is pending even though the consolidated registry contains `GFX_independence_wave_formable_form_48`; the live registry wins, and the ignored package manifest wording remains a documentation drift item.

4. The latest formable/League handoff calls the state-puzzle set “14” while listing 13 adapter IDs and separately discussing FORM-05; the accepted registry and prior formable audit include FORM-05, so the parent should correct the count/list together rather than silently choose one.

5. `006_event6_country_tranche_global_2026_08_30.md` flags contradictory IW-173 admission wording in `docs/events/006_independence_wave/pacific_country_packages.md` and stale Samuel Wilder King metadata; the package admission receipt is current, but the country-package documentation still needs an owner decision.

6. Historical focus handoffs cite `common/ai_strategy/006_independence_wave_generic.txt`, while the current source is `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`; the old path is retained only in dated evidence and must not guide new routing.

7. The parent-owned super-event-23 paragraph has a staged version without the Jeremiah Clarke candidate and an unstaged version with it; this pass did not choose between those parent edits. The current rights state is that the original London Brass Players audio remains blocked and the Clarke candidates remain unselected until parent selection, audition, attribution, provenance, and composition-jurisdiction review are complete.

## Duplicate, superseded, and stale-document list

| Document or surface | Disposition |
| --- | --- |
| `006_event6_post_p0_completion_audit_2026-08-29.md` | Retain as dated evidence, but supersede its pre-addendum parent-patch instruction with `3ce4b3468` and `713306f2e`. |
| `006_event6_assets_audit_current_2026-08-29.md` | Retain as the preceding asset audit; use the 2026-08-30 rights and path handoffs for current source/rights/path decisions. |
| `006_event6_formable_contract_audit_2026-08-29.md` | Retain for the cost, capacity, and failed-transaction-category blockers; the 2026-08-30 formable audit confirms no new family or patch. |
| Older 2026-08-29 country tranche audits | Retain as package-local evidence; the 2026-08-30 global tranche supersedes only where it records the IW-058 receipt repair and current admitted rows. |
| Removed parser-path references in asset manifests | Retain only where explicitly marked former or historical; the consolidated `interface/006_independence_wave_small_assets.gfx` path is current. |
| Parent-owned overview, resume, and source map edits | Not duplicated or overwritten; this handoff is the dated reconciliation overlay. |

No file was deleted or archived.

## Stale prompt and instruction list

The Event 006 super-event prompt still intentionally names the blocked London Brass Players recording and KJV quote, so it is not stale, but slot-24 worldwide distribution remains a parent decision because the latest text receipt documents the United Kingdom Crown-rights caveat.

Historical focus assignment handoffs that name `006_independence_wave_generic.txt` are stale as routing instructions and should point future work to the consolidated AI-strategy registry; they remain untouched because they are dated evidence.

The historical FORM-48 implementation plan retains its original sprite-registration wording and is already marked superseded by current plan and source-map authority; no active prompt was found that authorizes a fallback FSM identity or unreviewed formable admission.

## Markdown hard-wrap audit

No accidental mid-sentence hard wrap was introduced in the package-manifest section or this handoff; each prose sentence is kept on one physical line.

The parent-owned overview, resume packet, and source map were not rewritten, so their existing line structure was not normalized in this pass.

The prior path-reconciliation handoff records unrelated hard wraps in `docs/assets/006_independence_wave/manifest.md:6-8` and `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md:15-18`; those ignored asset-package files are outside this documentation scope and were left unchanged.

## Parent decisions and remaining HOLD/PARTIAL blockers

- Keep the whole-event boundary at 32/29/40/161 and keep all unadmitted packages fail-closed.
- Decide whether slot-24 uses the approved KJV wording with its jurisdiction caveat or the documented WEB alternative.
- Keep slot-23 audio blocked until the exact London Brass Players recording receives worldwide permission or the parent explicitly selects and audits a replacement candidate.
- Resolve ASSET-046 formable identity and UI-consumer ownership before producing missing emblems, and decide the BWX route before approving its flag.
- Resolve the Event 005 AEX ownership collision and the 48 NWE ideology-alias policy before deleting, renaming, or wiring any alias.
- Keep IW-179 FSM and FORM-48 source-gated until a named adult 1936-role subject, stable image, and derivative/reuse rights are all accepted.
- Reconcile IW-173 documentation and stale Samuel Wilder King metadata against the current admission receipt.
- Correct the formable handoff's 14-versus-13 list/count mismatch and preserve FORM-05's dedicated charter route.
- Treat AI balance, package-level probability, live release, save/load, and whole-event completion as unresolved until the required owner-routed MCP and live evidence exists.

## Validation and limitations

The current focused static receipts remain the allocator, country API, strict flag-family, SCN-008 scenario matrix, FORM-16, and GUI semantic checks recorded by the dated handoffs; no new gameplay validator was run by this documentation-only pass.

A read-only `hoi4_map_inspect` call covered 32 current Event 006-related state IDs and returned `MAP_INSPECTED` at revision `2f0393fc04266f53`, with selected state membership and networks available in the linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c5a660f8eb47bf5d55a11af4a41e23c2c6408d85a455f851aa05e52f2e865cb/556e6fa3e6d7ce49be0669359c965b12f5acf19ae6b779b82142824aafac4dcf/map-inspect.2f0393fc04266f53.json`; overall validation remained false because the workspace diagnostic ceiling retained unrelated map-position/port errors and an unrelated missing-BOM localisation diagnostic.

The required event, focus, GUI, and probability routes were attempted read-only, but the first payload shapes were rejected and the corrected batch was terminated at the parent request before producing a new receipt; existing dated MCP artifacts in `d9d56e1b4`, `711ca668e`, `844a24d2b`, and `f2ec2ae72` remain the evidence, with the custom `chaosx_ai_probability_auditor` route unavailable.

No live Hearts of Iron IV process, save/load test, asset generation, localisation edit, workbook update, or CSV export was performed.

## Changed files and handoff

- `docs/specs/006_independence_wave_specs/quality/package_manifest.md` received the concise 2026-08-30 authority overlay.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_documentation_reconciliation_2026-08-30.md` is the new dated reconciliation handoff.
- `docs/events/006_independence_wave/overview.md`, `006_independence_wave_resume_packet.md`, and `006_source_of_truth_map.md` were intentionally left unchanged to preserve parent-owned staged/unstaged edits.

No simplification or fallback was introduced by this documentation pass, and no gameplay completion claim is made.
