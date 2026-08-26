# Event 006 documentation current-status reconciliation handoff

Date: 2026-08-26.

Scope: documentation-only reconciliation of the Event 006 source-of-truth map, resume packet, specification acceptance checklist, overview, and the directly related Iberian package authority note.

## Current source-of-truth map

| Surface | Current authority | Current disposition |
| --- | --- | --- |
| Startup character registry | `history/general/006_independence_wave_character_recruitment_registry.txt`, commit `5895d0b69` | Current source with 25 guarded country blocks and 54 `recruit_character` calls; IW-057 FER remains intentionally absent while rights-gated. |
| FSM focus lifecycle | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` and `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`, commit `35ab74212` | Lifecycle hardening is committed; FSM remains adapter-only and fail-closed, with no portrait fallback. |
| Shared focus and overlay | `common/national_focus/006_independence_wave_focus.txt` and `006_event6_focus_overlay_gap_audit_2026-08-26.md` | MCP geometry is 184 focuses and 195 connectors with zero layout diagnostics; the overlay audit found no safe patch without changing accepted geometry or widening admission. |
| Portrait consumers | `006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md` | NAV Aguirre and GLC Castelao are the only current `styled_final` consumers with exact existing Event 006 matches; GLC Bóveda remains an unmapped supplied styled output. |
| Package boundary | `006_full_spec_gap_map_2026-08-26.md` and the package closure handoffs | Event 006 remains HOLD / PARTIAL at 32 content-attested packages, 29 compatible reservation groups, 40 adapters, and 161 unattested selectable rows; eight adapter-only rows remain fail-closed. |
| Next implementation footprint | `006_event6_first_footprint_admission_improvement_addendum_2026-08-26.md` and `006_event6_first_footprint_improvement_handoff_2026-08-26.md` | Plan written and implementation queued; no admission or gameplay completion claim. |

## Files changed

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` received a latest-evidence section, the startup-registry commit reference, current portrait states, overlay-audit result, full-spec gap-map/first-footprint status, and current MCP/probability limitations.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` received the same bounded current-evidence refresh and the startup-registry commit reference.
- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md` received current implementation wording for the registry, FSM hardening, overlay audit, portrait states, queued gap-map work, and the blocked probability route.
- `docs/events/006_independence_wave/overview.md` replaced the stale current portrait sentence, recorded the overlay-audit result and probability limitation, and linked this reconciliation handoff with the registry and FSM commits.
- `docs/events/006_independence_wave/iberian_registered_packages.md` replaced the stale claim that no styled-final request existed with the bounded NAV/GLC styled-final and GLC Bóveda unmapped status.

No gameplay, asset, specification design matrix, workbook, CSV, or generated file was edited, staged, or committed.

## Unresolved plan and handoff disposition

| Item | Disposition | Reason or remaining boundary |
| --- | --- | --- |
| Full-spec gap map | Current reference | Whole event remains HOLD / PARTIAL and the map records the 32/29/40/161 boundary plus unresolved package breadth, formable, decision receipt, probability, super-event, visual, and GUI gaps. |
| First-footprint addendum | Queued | IW-095 DAH is the proposed first footprint; no gameplay patch or package admission was performed in this documentation pass. |
| Focus-overlay gap audit | No safe patch identified | Preserve the accepted 184-focus geometry and package boundary pending a parent decision. |
| NAV and GLC package admissions | Fail-closed | Styled-final consumer matches do not close rights, identity, duplicate-person, country-package, probability, or central-attestation gates. |
| FSM package | Fail-closed | Commit `35ab74212` hardens lifecycle cleanup but does not promote FSM or restore its withdrawn portrait. |
| Typed probability evidence | Blocked | The required auditor route remains recorded as `Transport closed`; no quantitative balance claim is made. |

## Contradictions and stale references

- Dated 2026-08-22 and 2026-08-24 paragraphs still describe the earlier 38 source-placeholder/13-unmapped portrait snapshot; they are preserved as historical evidence and are superseded by the current 2026-08-26 portrait audit.
- The prior Iberian package authority claimed that no styled-final request existed; that current-status contradiction is corrected in `docs/events/006_independence_wave/iberian_registered_packages.md`.
- The latest FIJ closure handoff contains a stale seven-adapter-only count in its static summary, while the settled current authority and the reconciled docs retain the eight-ID fail-closed list; parent review should decide whether to append a correction to that historical handoff.
- Event MCP inspection is partial because helper/lifecycle projections remain deferred despite zero blocking diagnostics, and focus inspection passes with only the unrelated vanilla `continuous_restrict_freedom_desc` warning; neither result closes whole-event or live-runtime acceptance.

## Duplicate or superseded documents

- `006_event6_docs_authority_cleanup_2026_08_26.md` remains dated provenance and is superseded for the latest registry, FSM, overlay, portrait, and queued-footprint status by this handoff.
- `006_event6_docs_source_layout_reconcile_2026-08-26.md` remains the source-layout evidence for the registry merge; this handoff only adds the cross-document current-status reconciliation.
- The 2026-08-22 portrait wiring and consumer-gap handoffs remain historical evidence for the earlier source-placeholder snapshot; the 2026-08-26 portrait audit is current for NAV/GLC supplied outputs.
- No documentation file was deleted or merged in this pass.

## Stale prompt or instruction list

No stale prompt or instruction file was changed in the bounded scope, and no current target document retains the former startup registry as a current source path after the edits.

## Markdown hard-wrap audit

The edited current-status paragraphs are each one physical line per sentence, and the checklist's current authority paragraph is now one physical line.

No historical paragraphs were reflowed because preserving dated evidence was part of the requested scope; any remaining historical hard wraps should be handled in a separate formatting-only pass if the parent wants that provenance rewritten.

## MCP and validation evidence

The read-only event inspection of `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, with zero blocking diagnostics and deferred helper/lifecycle projections.

The read-only focus inspection of `independence_wave_focus_tree` returned `FOCUS_INSPECTED` at revision `e751d1b2a47f0b39bae57a1686b5f41e1a99bbb3a4918a3df4b133a244af47ce`, with validation passed, 184 focuses, 195 connectors, and zero layout diagnostics apart from the unrelated vanilla warning.

Targeted diff review confirmed that only the five documentation paths listed above are modified by this pass, and `git diff --check` reports no whitespace errors.

Skipped validation: no live HOI4 execution, save/load test, asset inspection, workbook audit, or gameplay source audit was run because this task is documentation-only and those surfaces were explicitly out of scope.

## Recommended parent decisions

- Decide whether the stale seven-adapter-only sentence in the FIJ closure handoff should receive a dated correction without rewriting its historical evidence.
- Decide whether the queued first-footprint addendum should be promoted into implementation work; this handoff intentionally does not promote it.
- Keep all eight package gates fail-closed until rights, identity, country-package, probability, and central-attestation evidence is independently closed.

## Remaining risks

The current docs now distinguish exact portrait consumer matching from package admission, but older dated documents can still be mistaken for current status if readers skip their superseding headers.

The MCP event projection remains partial and typed probability evidence remains unavailable, so this reconciliation is not a gameplay completion claim.
