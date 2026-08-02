# Event 006 documentation reconciliation v97

Date: 2026-08-02.

> **Superseded for current routing (2026-08-02):** v102 current completion evidence and the current portrait-shelf index reconciliation supersede this v97 documentation snapshot. Preserve its dated findings only. Current whole-event state is incomplete and active with an 80-master all-indexed-or-explicitly-recorded shelf, 318 unique and 345 raw focus entries, the 6/8/10/14/20 ladder, fourteen attestations across thirteen compatible groups and fourteen anchors, the FSM fail-closed gate, blocked 6001 audio, one generic tree, and no live tests in scope.

Scope: documentation-only reconciliation of the Event 006 source-of-truth map, resume packet, and overview against the v96 whole-event audit, v97 focus-ownership audit, CAT decision, Barsoum v94 promotion, and current shelf evidence. This handoff does not claim gameplay completion, package admission, focus validation, CAT admission, asset completion, or runtime evidence.

## Current source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Whole event | `subagent_handoffs/006_event6_completion_audit_v96_2026_08_02.md` (`9926f6d55`) | Current authority; partial and blocked. Fourteen packages remain attested, 180 selectable rows remain unattested, and no fallback or new admission is authorized. |
| Focus ownership and geometry | `subagent_handoffs/006_event6_focus_geometry_ownership_audit_v97_2026-08-02.md` (`16953759c`, corrected CAT references `333c4a27`) | Current bounded focus authority; CAT uses the full Event 006 framework under the accepted minimal-tree exception. The v82 static after-state is retained; current MCP inspect/render is `SCAN_BYTE_LIMIT`, so focus remains PARTIAL/HOLD. |
| CAT package and FORM-07 | `catalonia_package.md`, `006_iw014_cat_package_implementation_2026-08-01.md`, and `006_form07_iberian_adapter_implementation_2026-08-01.md` | Full-framework minimal-tree CAT draft, not attested. Vanilla history, flag, `CAT_lluis_companys`, and non-focus carrier surfaces remain preserved. CAT/FORM-07 remain fail-closed for identity, flag, member-adapter, and readiness gates. |
| Portrait shelf and Barsoum | v96 audit plus Barsoum v93/v94 evidence (`4b8c82faa`, `706c159be`) | 78 physical original-size PNG masters, 73 indexed rows, five physical-but-unindexed masters. Barsoum v94 promotes only the existing concordat-council DDS consumer; no advisor/small/dossier portrait, wider IW-058 admission, or attestation follows. |
| Super-event `6001` | v96 audit and v22 audio research | Dormant DDS and registered sprite remain without runtime dispatch/localisation/audio/WAV/wrappers/firing package. Accepted recording rights remain blocked; no fallback is authorized. |
| Event-facing overview | `docs/events/006_independence_wave/overview.md` and `006_overview_reconciliation_v96_2026_08_02.md` | Current v96/v82/SCAN/CAT wording retained. Only a historical cross-reference was changed in this pass to point to v96. |

## Files changed in this pass

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/events/006_independence_wave/overview.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_documentation_reconciliation_v97_2026_08_02.md`

The source map and resume packet now place v96 at the current whole-event authority boundary, retain v70 metrics only as pre-v82 historical evidence, record v82 static geometry and current `SCAN_BYTE_LIMIT`, and describe CAT as the accepted full-framework minimal-tree exception. Current Barsoum rows now record v93 audit plus v94 narrow DDS promotion. The overview was already current under `88c251854`; its one historical paragraph now points to v96 rather than v33 for current routing.

## Plan and handoff dispositions

| Artifact or family | Disposition | Notes |
| --- | --- | --- |
| v96 whole-event completion audit | Current authority; partial and blocked | No new package or fallback. |
| v97 focus-ownership audit | Current bounded authority; PARTIAL/HOLD | Resolves CAT ownership only; it does not close focus geometry or probability evidence. |
| v70 focus final audit | Historical baseline | Retained for dated 14-blocker/45-crossing/7-intersection evidence; superseded for current metrics by v82 and v97. |
| CAT additive/full-framework wording | Resolved for current routing | Full framework under the accepted minimal-tree exception; historical additive wording remains traceability only. |
| Barsoum v2 evidence package | Unadmitted evidence | v94 promotion is limited to the existing concordat-council DDS consumer. |
| `6001` art/audio package | Blocked/queued | Dormant art and sprite registration remain; rights and runtime package are unresolved. |
| Existing asset manifests and README files | Left unchanged | Latest parent scope bounded this pass to source map, resume packet, and overview. Their older shelf/promotion wording remains a follow-up risk for the owning asset-doc pass. |

## Contradictions resolved

- The current documentation no longer treats the CAT carrier as an unresolved additive/full-framework design choice. Vanilla CAT exposes only `generic_focus`; the accepted contract is full Event 006 framework assignment under a minimal-tree exception, while CAT/FORM-07 remain fail-closed.
- The v70 focus figures are explicitly historical pre-v82 evidence. Current static values are v82; current MCP inspection is `SCAN_BYTE_LIMIT` with no diagnostics.
- v33 is explicitly historical. v96 controls current whole-event disposition, while dated v33 findings remain useful only where v96 does not supersede them.
- Barsoum v94 is recorded as a narrow existing-DDS promotion rather than a wider IW-058 or advisor/small-portrait admission.

## Remaining contradictions and parent decisions

- The v96 audit itself records the older “CAT has no valid owning-tree contract” limitation. The v97 focus-ownership audit supersedes that limitation for current routing, but focus geometry/probability evidence remains open and CAT/FORM-07 admission is still fail-closed.
- Some older downstream rows in historical tables retain the phrase “Barsoum v2 pending independent audit.” The current source-map v94 override states that these rows are historical evidence and that only the concordat-council DDS promotion is current.
- Asset manifests outside this pass may still use older 68/63 shelf or “no runtime promotion” language. Do not treat those surfaces as current authority until the asset-documentation owner reconciles them.
- No parent decision is requested for CAT ownership; the accepted minimal-tree decision is recorded. Parent decisions remain required for source-approved CAT/Iberian X identity and flag, complete NAV/GLC adapters, focus validation after the byte limit clears, `6001` rights, package admission, and whole-event closure.

## Validation performed

- `rg` checks across the source map, resume packet, and overview confirmed current references to v96, v97, v82, `SCAN_BYTE_LIMIT`, the accepted CAT minimal-tree contract, and the Barsoum v94 narrow promotion.
- `Test-Path` confirmed the v97 focus-ownership handoff exists at `subagent_handoffs/006_event6_focus_geometry_ownership_audit_v97_2026-08-02.md`.
- Diff review was limited to the four documentation files listed above; unrelated gameplay, asset, spreadsheet, and concurrent working-tree changes were not staged or modified.

Skipped meaningful validation: no gameplay launch, live MCP retry, binary asset inspection, workbook inspection, or runtime transaction test was performed because this is a documentation-only reconciliation and those checks are outside the curator boundary.

## Parent handoff

Use `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` as the current continuation ledger. Preserve the whole-event **partial and blocked** disposition. Do not reopen the CAT ownership decision, promote CAT/FORM-07, infer package admission from the narrow Barsoum DDS promotion, or register/fire `6001`. Remaining work is implementation/audit work owned outside this documentation pass.
