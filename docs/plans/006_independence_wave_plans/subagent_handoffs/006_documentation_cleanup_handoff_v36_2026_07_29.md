# Event 006 documentation cleanup handoff v36

Date: 2026-07-29

Scope: documentation reconciliation for the bounded milestone that closes the shared Event 006 core loop, dynamic systems, and reusable country-registration API under source and static evidence. Country-specific package content remains outside this milestone.

## Outcome

The current Event 006 documentation now names the three v35 closure handoffs as one source-closed shared milestone. The approved automatic ladder remains 6/8/10/14/20. The 14- and 20-country targets remain source fail-closed below admitted package and reservation capacity. The whole-event status remains **HOLD / PARTIAL** because package content and other static acceptance surfaces remain incomplete.

## Source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/` | Preserved as design authority. |
| Shared automatic loop and transaction | `subagent_handoffs/006_core_loop_closure_v35_2026_07_29.md` | Source-closed shared core. Positive reserved-target validation, exact frozen-plan allocation, host survival, Event 005-first joint ordering, finalization, rollback, and cleanup are documented. |
| Shared dynamic systems | `subagent_handoffs/006_dynamic_systems_closure_v35_2026_07_29.md` | Source-closed shared systems. Country values, former-host, patron, Network, League, rival bloc, decision and mission cleanup, and the standard security cost contract are covered. |
| Country registry and reusable API | `subagent_handoffs/006_registry_api_closure_v35_2026_07_29.md` | Source-closed registry/API layer. The 206-row projection, custom and reused carriers, overlay views, bound/unbound status, and inert reservations are documented without package promotion. |
| Country-specific package content | Current package audits, the canonical registry, and the current source-of-truth map | Remains queued or fail-closed. The current static attestation set is twelve packages. Fifty-five selectable rows are unbound, seventeen reservations are inert, and thirteen identities are route-only overlays. |
| Whole-event completion | `subagent_handoffs/006_event_completion_audit_v33_2026_07_29.md` | **HOLD / PARTIAL**. The v33 static findings remain current. Runtime-only holds are optional future QA under the accepted authority. |

## Unresolved plan and handoff disposition

| Document or family | Disposition | Reason and next owner |
| --- | --- | --- |
| `006_core_loop_closure_v35_2026_07_29.md` | Implemented and source-closed | Parent keeps the exact 6/8/10/14/20 contract and the fail-closed 14/20 capacity boundary. |
| `006_dynamic_systems_closure_v35_2026_07_29.md` | Implemented and source-closed | Package-specific route writers, AI probability inputs, and balance remain parent or package-audit work. |
| `006_registry_api_closure_v35_2026_07_29.md` | Implemented and source-closed | Registry/API coverage does not promote country definitions or package content. The 55 unbound and 17 inert rows remain fail-closed. |
| `006_event_completion_audit_v33_2026_07_29.md` | Current whole-event authority | Preserve **HOLD / PARTIAL** for static package capacity, focus diagnostics, AI/source proof, assets, formables, and `6001` rights. |
| Older completion, package, registry, and portrait handoffs | Historical or superseded where the source map says so | Do not rewrite or delete them. Use the current source map and resume packet for routing. |

## Contradictions found and disposition

| File or evidence | Contradiction | Resolution |
| --- | --- | --- |
| `docs/events/006_independence_wave.md`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Existing docs described the whole event as one undifferentiated incomplete implementation, which obscured the shared core/API tranche that v35 closed. | Added a bounded milestone ledger and retained the separate package-content and whole-event **HOLD / PARTIAL** boundary. |
| Older ladder references in historical audits | Earlier material uses 3/4/5/7/10. | Current docs preserve the later user-approved 6/8/10/14/20 ladder and mark older wording historical. |
| Runtime wording in older audits and package notes | Some older rows require live execution or save/load proof. | The 2026-07-29 acceptance authority makes runtime-only evidence optional future QA. Static capacity, package, source, asset, focus, AI, route, and rights blockers remain required. |
| Registry/API presence versus package readiness | Registry rows and carrier collections can be mistaken for complete country packages. | Current docs explicitly state that registration, collections, and overlay views do not promote leaders, portraits, flags, focuses, decisions, forces, AI, formables, or assets. |

## Duplicate or superseded document list

- The three v35 closure handoffs remain separate because they cover different ownership surfaces. They are cross-linked as one milestone and are not merged into the event doc.
- `006_event_completion_audit_v33_2026_07_29.md` remains the whole-event authority. Earlier completion audits remain historical evidence and were not rewritten.
- Existing source map and resume packet remain separate. The source map is the authority ledger, while the resume packet is the continuation brief.
- Package-specific handoffs remain authoritative for their own package status and were not rewritten.

## Stale prompt or instruction list

- No current prompt file was edited. The named v35 handoffs and the current source map and resume packet now prevent a duplicate core/API implementation pass.
- Older ladder, runtime-proof, package-attestation, and portrait-shelf wording remains only where a historical handoff preserves dated evidence. Current docs point to the v33 authority and v35 closure handoffs.
- The Part 7 acceptance section already contains the current source/static acceptance rule and was left unchanged in this pass.

## Recommended parent decisions

1. Treat the shared core, dynamic systems, and registry/API milestone as closed for source/static planning purposes.
2. Do not call the full Event 006 goal complete. Continue country-specific package admission and remaining static audits from the current resume packet.
3. Keep the 6/8/10/14/20 ladder exactly as approved. Keep the 14/20 bands fail-closed until admitted package and reservation capacity is sufficient.
4. Keep registry rows, reused carriers, overlay views, and inert reservations separate from package readiness. Do not add fallback geography, identities, art, or generic package content.

## Files changed

- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_documentation_cleanup_handoff_v36_2026_07_29.md`

The Part 7 acceptance file already carries the controlling source/static evidence rule and was left unchanged. No gameplay, localisation, asset, GFX, GUI, workbook, spreadsheet, or unrelated documentation file was edited. No file was deleted. No commit was created.

## Meaningful validation

- Targeted `rg` and `Select-String` checks confirmed the current owned docs name the v33 whole-event authority, the v35 handoffs, the 6/8/10/14/20 ladder, and the twelve-package, 55-unbound, 17-inert, and 13-overlay boundaries.
- Targeted path checks confirmed all three v35 handoffs and every changed documentation path exist.
- A scope-limited `git diff --check` was run for the owned documentation paths after patching.

## Skipped meaningful validation

- No Hearts of Iron IV launch, live game, save/load, binary asset inspection, workbook edit, or in-game consumer observation was run. The parent explicitly made source, static, MCP, asset, documentation, and catalog evidence authoritative for this milestone.
- No gameplay or package audit was repeated because this task only reconciles documentation and the three v35 handoffs already contain their bounded evidence.

## Remaining risks and uncertainties

- The whole-event static **HOLD / PARTIAL** state remains. Country-specific package content, package admission, route adapters, focus diagnostics, package AI and balance evidence, formables, assets, and `6001` rights still require parent or bounded audit work.
- The v35 dynamic-systems probability inspections declare incomplete scenario pools. They are source-closure evidence, not exact comparative AI probability results.
- The 14/20 ladder is preserved as design and source behavior but remains fail-closed below admitted package and reservation capacity.
- Historical handoffs intentionally retain stale counts or runtime wording for traceability. Readers must use the current source map and resume packet.
