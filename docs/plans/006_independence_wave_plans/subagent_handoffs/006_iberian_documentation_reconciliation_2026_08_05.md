# Event 006 Iberian documentation reconciliation handoff

Date: 2026-08-05.

Scope: documentation-only reconciliation for the current IW-013/NAV, IW-015/GLC, and FORM-07 Iberian tranche.

Gameplay, localisation, assets, GFX, country history, map, and workbook files were not edited by this reconciliation.

## Current source-of-truth map

| Surface | Current authority | Status |
| --- | --- | --- |
| Whole-event routing | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current Event 006 router; its IW-013/IW-015 override and current fifteen-package authority are now explicit, while dated pre-TRA paragraphs remain traceability. |
| Country registry API | `docs/events/006_independence_wave/systems/country_registry.md` and `docs/events/006_independence_wave/country_api.md` | Current package-ID/anchor API; registered Iberian carriers are source-wired vanilla reuse rows, not new tags or readiness shortcuts. |
| Formable registry | `docs/events/006_independence_wave/systems/formable_registry.md` | FORM-07 current fail-closed contract; CAT 165, NAV 792 compact with optional 172/806, and GLC 171 are the accepted corridor anchors. |
| Iberian package record | `docs/events/006_independence_wave/iberian_registered_packages.md` | Current package surface for NAV/GLC ledgers, framework, forces, routes, AI, decisions, dispatch, and generation-safe cleanup. |
| CAT event record | `docs/events/006_independence_wave/catalonia_package.md` | Current CAT HOLD record; it now distinguishes source-wired NAV/GLC adapters from unresolved FORM-07 and central attestation gates. |
| Runtime evidence | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`, `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`, and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | Source evidence only; setup, final-validation, and cleanup dispatches exist for IW-013/NAV and IW-015/GLC. |
| Admission evidence | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | IW-013 and IW-015 are in the adapter/preflight surface but not in the central content-attestation OR; runtime and scenario admission remain fail-closed. |

## Promoted current facts

- IW-013 reuses vanilla `NAV` and uses installed-map state 792 (País Vasco) as its compact anchor.
- NAV states 172 (Navarra) and 806 (French Basque) remain optional extension objectives and are not compact release/readiness anchors.
- IW-015 reuses vanilla `GLC` and uses state 171 (Galicia) as its compact anchor.
- Both carriers preserve vanilla history and leader rosters while receiving the shared Event 006 full framework and package-specific ledgers, routes, forces, AI, decisions, host/network/league/formable hooks, and generation-safe cleanup.
- The NAV/GLC setup, final-validation, and cleanup adapters are source-wired through the Iberian package effects and central dispatch.
- Central content attestation remains fail-closed because IW-013 and IW-015 are not in the exact attestation OR.
- Independent source, identity, flag, portrait, and country-package audits remain open for both carriers.
- FORM-07 remains fail-closed until its researched Iberian X identity, complete flag package, identity review, and member/integration contract are approved.
- No advisor icons or advisor portrait assets were created or authorized for the Iberian tranche.

## Plan and handoff disposition

| Document | Disposition | Reason or boundary |
| --- | --- | --- |
| `docs/events/006_independence_wave/iberian_registered_packages.md` | Current package documentation | Carries the accepted 792/171 map contract, source-wired adapters, package surfaces, fail-closed admission boundary, and no-advisor-icon statement. |
| `docs/events/006_independence_wave/systems/country_registry.md` | Current API documentation | Adds package-ID resolution and explicit source-wired NAV/GLC dispatch semantics without changing registry gameplay. |
| `docs/events/006_independence_wave/country_api.md` | Current API documentation | Adds the registered-Iberian carrier subsection and preserves the collection-not-admission rule. |
| `docs/events/006_independence_wave/systems/formable_registry.md` | Current FORM-07 documentation | Records 792 as the compact NAV anchor, 172/806 as optional extensions, source-level NAV/GLC adapter surfaces, and unresolved central gates. |
| `docs/events/006_independence_wave/catalonia_package.md` | Current CAT documentation | Rewords the dated implementation paragraph to reflect source-wired NAV/GLC adapters while keeping CAT HOLD. |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current routing map | Updates CAT/FORM-07 rows and the parent decision list to the source-wired NAV/GLC state and current fifteen-package attestation authority; dated historical counts remain identified. |
| `subagent_handoffs/006_form07_iberian_adapter_implementation_2026-08-01.md` | Historical snapshot with current amendment | The pre-adapter body is retained; its amendment records the current anchors, source-wired NAV/GLC adapters, fail-closed gates, and no-advisor boundary. |
| `subagent_handoffs/006_iw013_iw015_iberian_package_audit_2026-08-03.md` | Historical pre-adapter audit with current amendment | The old 172-versus-792 and missing-adapter findings remain dated evidence; the amendment promotes the installed-map/source-wired contract without admitting either package. |
| `subagent_handoffs/006_iw014_cat_admission_audit_current_2026_08_03.md` | Current CAT HOLD audit with amendment | CAT remains fail-closed; only the NAV/GLC blocker wording was narrowed from missing adapters to source-wired but unaccepted package surfaces. |

No plan was promoted into the accepted spec, rejected, or deleted by this reconciliation.

## Contradictions resolved

| Contradiction | Resolution |
| --- | --- |
| NAV state 172 was described as the compact anchor in older FORM-07 and IW-013 evidence, while the installed-map binding and current loader use 792. | Current docs use 792 as compact NAV anchor and retain 172/806 only as optional extensions; the dated 172 wording remains explicitly historical. |
| Dated handoffs said NAV/GLC runtime adapters were absent or incomplete. | Dated bodies are preserved with amendment notices; current docs state that setup, final-validation, and cleanup adapters are source-wired. |
| Source-level corridor proof could be mistaken for FORM-07 readiness. | Current FORM-07 text distinguishes source-level NAV/GLC adapters from unresolved identity, flag, portrait/source, member-policy, integration, and central attestation gates. |
| Older map text called the attestation set fourteen packages after TRA admission. | The current routing decision lists fifteen packages including IW-023; fourteen-package paragraphs are marked as pre-TRA traceability. |
| Iberian visual scope could be read as requiring advisor art. | Current API/package/CAT text records that no advisor icons or advisor portrait assets were created or authorized. |

## Contradictions still open

- IW-013 and IW-015 remain outside central content attestation and therefore cannot enter runtime or scenario release capacity.
- Independent source, identity, flag, portrait, and country-package audits are not promoted for either carrier.
- FORM-07 still lacks an approved Iberian X identity, complete flag package, and final member/integration contract.
- Static source wiring is not live execution, save/load, or player-owned runtime evidence.

## Duplicate, superseded, and stale-document record

- The dated FORM-07 implementation handoff and IW-013/IW-015 package audit remain in place for traceability and now carry supersession/amendment notices rather than being deleted.
- The dated IW-014 CAT admission audit remains the CAT HOLD authority with its current wording amendment; it does not become an Iberian package admission audit.
- Older dated CAT contract, focus, next-admission, resume, and whole-event paragraphs that still mention missing NAV/GLC adapters remain historical evidence unless a later current override names them; they are not instructions to redo the adapter tranche.
- No stale prompt file was found in the named Iberian documentation scope, and no obsolete pasted flag log was used.

## Markdown hard-wrap audit

- Joined mid-sentence paragraphs in the current country-registry Iberian section and FORM-07 section so each prose sentence occupies one physical line.
- Kept Markdown tables, headings, lists, and dated historical handoff structure intact.
- Added one-line prose sentences in the API subsection, CAT record, source-map corrections, and current handoff amendments.
- No binary, spreadsheet, or generated asset documentation was opened or modified.

### Outstanding hard-wrap issue list

- `docs/events/006_independence_wave/systems/country_registry.md` still contains older mid-sentence wraps in the general collection/API prose outside the Iberian section, such as the static collection paragraphs after the current carrier table; those were left unchanged to avoid unrelated documentation churn.
- `docs/events/006_independence_wave/systems/formable_registry.md` still contains older mid-sentence wraps in the general registry and formation-flow prose outside the current FORM-07 section; those were left unchanged to preserve the accepted historical structure.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` contains many dated historical hard wraps outside the current Iberian corrections; those were left unchanged because they are traceability material and not current Iberian instructions.
- No new current Iberian paragraph or amended handoff introduced a mid-sentence hard wrap.

## Meaningful validation

- Targeted `Select-String` checks confirm current docs name NAV state 792, optional 172/806, GLC state 171, and source-wired setup/final-validation/cleanup adapters.
- Targeted `Select-String` checks confirm old missing-adapter and state-172 wording remains only in dated historical bodies or explicitly preserved traceability paragraphs.
- Targeted `rg`/`Select-String` checks confirm IW-013 and IW-015 remain in the adapter/preflight surface but outside the central content-attestation OR in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- Scoped `git diff --check -- docs/events/006_independence_wave docs/plans/006_independence_wave_plans/006_source_of_truth_map.md docs/plans/006_independence_wave_plans/subagent_handoffs/006_form07_iberian_adapter_implementation_2026-08-01.md docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_iberian_package_audit_2026-08-03.md docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw014_cat_admission_audit_current_2026_08_03.md` is the relevant whitespace check for this documentation scope.

## Skipped meaningful validation

No Hearts of Iron IV process, live release, save/load, MCP gameplay render, package audit rerun, asset review, map write, or workbook/export check was run because this handoff is documentation-only and those surfaces remain parent-owned.

No commit was created because the shared worktree contains concurrent parent and subagent changes on several reconciled documentation files; the parent should review and stage this scoped documentation patch with the surrounding tranche.

## Recommended parent decisions

1. Keep IW-013/NAV, IW-015/GLC, and CAT/FORM-07 fail-closed until the independent source, identity, flag, portrait, and country-package audits are promoted together.
2. Treat the 792/171 compact-anchor contract as current and do not re-open the older 172-as-compact proposal without a new installed-map decision.
3. Do not add advisor icons, generic portraits, borrowed flags, fallback identities, or attestation entries as a shortcut.
4. Re-audit FORM-07 only after the Iberian X identity, flag package, member policy, and integration contract are independently accepted.

## Remaining risks

The source documentation now distinguishes source-wired adapters from runtime admission, but the central attestation and grounded visual gates remain unresolved and no live execution evidence exists.
