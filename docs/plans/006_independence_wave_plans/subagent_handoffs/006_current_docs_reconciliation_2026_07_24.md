# Event 006 current documentation reconciliation

Date: 2026-07-24

Scope: documentation-only reconciliation for Event 006. The accepted specification area, current implementation authorities, event documentation, FORM-48 plan, and the 2026-07-24 content-attestation repair were reviewed. No gameplay, localisation, asset, spreadsheet, source-spec, source-of-truth-map, or resume-packet file was edited.

> **Later same-day supersession:** This reconciliation predates the independently approved IW-009 Bavaria post-wire promotion. The canonical set is now IW-001, IW-004, IW-007, IW-008, IW-009, IW-017, and IW-019. The 3/4/5/7 bands are conditionally plannable from those seven packages, while both ten-country bands remain fail-closed below capacity. Use the source-of-truth map and `006_iw009_bavaria_postwire_country_package_audit_2026_07_24.md` for current admission status.

## Source-of-truth map

| Surface | Authority | Current interpretation |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/` | All files remain accepted design. They describe the intended differentiated registry, wave ladder, formables, assets, achievements, and validation scope rather than current runtime admission. |
| Current implementation status | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Use as the implementation ledger, with the same-day gap audit and content-gate handoff resolving stale historical passages. |
| Current completion gaps | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_completion_gap_audit_2026_07_24.md` | Event 006 remains incomplete. The exact current gate admits IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019 only. |
| Automatic gate repair | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_automatic_content_attestation_weight_gate_2026_07_24.md` | Unadmitted IDs receive zero automatic weight and fail with `package_unready` before anchor reservation. This is the current allocator and reservation boundary. |
| Event documentation | `docs/events/006_independence_wave/overview.md` | The new current-status section is authoritative for this event doc. The prior 2026-07-22 admission section is explicitly historical and superseded. |
| FORM-48 plan | `docs/plans/006_independence_wave_plans/006_form48_pacific_federation_implementation_plan_2026_07_16.md` | The design and gameplay tranche remain implemented. Runtime admission is blocked because HAW, FSM, and HBX are outside the exact six-package gate. |

## Files changed

| File | Change |
| --- | --- |
| `docs/events/006_independence_wave/overview.md` | Added a 2026-07-24 current runtime admission section, marked the former three-package section superseded, documented conditional 3/4/5 reliability, the 7/10 and World Collapse capacity block, FORM-48 reachability, portrait policy, advisor-asset absence, ASSET040-ASSET043 gaps, 6001 and 6002 status, and Radical Bloc reachability. Updated the release, asset, and dangerous-milestone summaries to match. |
| `docs/plans/006_independence_wave_plans/006_form48_pacific_federation_implementation_plan_2026-07-16.md` | Replaced the stale 2026-07-18 promotion note with a current exact-six admission note and a clearly labeled historical supersession note. The plan status now says the design tranche is implemented while runtime admission is blocked. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_docs_reconciliation_2026-07-24.md` | Created this reconciliation handoff. |

## Plan and handoff disposition

| Document or tranche | Disposition | Evidence and remaining boundary |
| --- | --- | --- |
| All accepted Event 006 specs | Accepted source design | Preserved unchanged. The current six-package gate is an implementation boundary, not a rewrite of accepted design. |
| FORM-48 implementation plan | Implemented design tranche, queued runtime admission | HBX remains the carrier design and HAW/FSM remain sovereign members, but all three package IDs are unadmitted. No compliant FORM-48 execution or reason-4 reachability proof exists yet. |
| Automatic content-attestation weight gate | Implemented repair | Weight calculation and anchor reservation share the canonical content gate. This removes unadmitted automatic contamination without admitting a package. |
| Event 006 event documentation | Reconciled current status with historical traceability | Current claims now use the exact six-package set. The old three-package paragraph remains only under a superseded heading. |
| 6002 dangerous milestone | Implemented source package, partially reachable | Slot, audio, wrappers, Event Log payload, FIFO, and predicates exist. Hidden-formable and ten-country paths remain unavailable under the current admission and capacity boundaries. |
| 6001 super-event | Blocked | Exact recording rights remain unresolved. No fallback or substitute is authorized. |
| ASSET040-ASSET043 | Queued and missing | Authored frames, static fallbacks, manifests, previews, GUI dimensions, and runtime consumers are still absent. |
| Event 006 advisor icons | Explicitly absent by accepted policy | No custom advisor icons, assets, sprites, or portrait blocks are authorized or present. Advisor mechanics remain a separate gameplay concern. |

## Contradictions resolved

- The event doc's three-package current admission wording was replaced by the exact six-package set IW-001, IW-004, IW-007, IW-008, IW-017, and IW-019.
- The event doc and FORM-48 plan no longer imply that HAW, FSM, or HBX are runtime-admitted. Their gameplay and formable contracts remain documented as implemented design, while runtime reachability is blocked.
- The event doc now records BAY's protected Rupprecht and independently approved/runtime-promoted Heinrich Held without treating BAY as admitted. Its commander and fresh package audit remain open.
- The automatic wave summary now reflects the repaired content gate. The 3/4/5 bands are conditionally viable when six admitted packages pass live gates. The 7/10 bands and ten-country World Collapse remain fail-closed below capacity. World Collapse remains a count of ten.
- The event doc no longer implies that ASSET040-ASSET043 animation packages are wired. It records them as missing and unwired.
- The event doc now distinguishes the implemented 6002 source package from its partial reachability and retains the exact-recording-rights block on 6001.
- The event doc now states that the Radical Bloc definition and trigger scaffolding exist, while no currently admitted route proves the full containment-survival condition.

## Contradictions still open

- `006_source_of_truth_map.md` contains current six-package sections but also preserves stale parent-decision or historical lines mentioning sixteen attestations and superseded Pacific or CHU/ASY admission. It was explicitly outside this task scope and remains unchanged.
- `006_independence_wave_resume_packet.md` contains current six-package sections but also alternates between older two-package, three-package, and sixteen-package wording and overstates 3/4/5 reliability in historical passages. It was explicitly outside this task scope and remains unchanged.
- Accepted spec text can describe CHU/ASY, FORM-48, and the full 3/4/5/7/10 target design as intended content while the current runtime gate keeps those packages closed. This is a design-versus-implementation distinction, not authorization to rewrite the specs.
- The six admitted packages do not provide a deterministic in-engine proof for every 3/4/5 host, anchor, collision, and origin combination. Conditional viability is the current honest status, not a completion claim.

## Duplicate and superseded documentation

- The former `Current portrait-gated admission (2026-07-22)` section inside `docs/events/006_independence_wave/overview.md` is retained as a historical section and superseded by the new 2026-07-24 section.
- The 2026-07-18 FORM-48 promotion wording is retained as a labeled historical note inside the plan and no longer describes runtime admission.
- Earlier portrait promotion handoffs remain historical evidence under `subagent_handoffs/`, while the current sourced-only portrait policy and exact gate control admission.
- No documentation file was deleted. No accepted plan was rejected because it is currently fail-closed.

## Stale prompt or instruction list

- The stale FORM-48 promotion note in the plan was updated and labeled as historical.
- No accepted spec prompt was edited. The prompt and spec area remains design authority and should not be used as a runtime-admission ledger.
- The source-of-truth map and resume packet still need a later scoped cleanup pass if the parent wants all internal historical admission language moved behind explicit supersession labels.

## Recommended parent decisions

1. Keep the exact six-package content gate and the repaired zero-weight plus pre-anchor reservation rule as the sole current automatic-admission authority.
2. Treat 3/4/5 as conditionally viable only after live host, anchor, reservation, Event 005 collision, force, chaos-band, and transaction checks pass. Keep 7/10 and World Collapse at ten fail-closed below capacity.
3. Keep FORM-48 queued until HAW, FSM, and HBX each receive compliant sourced real-male portrait packages and fresh complete package audits.
4. Keep ASSET040-ASSET043 missing and unwired, keep 6001 rights-blocked with no fallback, and do not claim 6002 fully reachable.
5. Keep the Radical Bloc definition as implemented scaffolding with reachability blocked until an admitted route proves containment and survival.
6. Do not claim Event 006 complete. If desired, authorize a separate documentation pass for stale internal sections in the source-of-truth map and resume packet.

## Validation

- Read AGENTS.md, the full `chaos-redux-events` skill, the full `chaos-redux-subagents` skill, all markdown files in the accepted Event 006 spec area, the named source-of-truth map, resume packet, completion-gap audit, content-gate handoff, event doc, and FORM-48 plan.
- Compared the exact package IDs, wave counts, gate behavior, FORM-48 state, portrait policy, advisor boundary, asset gaps, Radical Bloc status, and 6001/6002 status with the named current authorities.
- Ran targeted `rg` checks for admission IDs, stale promotion terms, ASSET040-ASSET043, advisor assets, FORM-48, Radical Bloc, and 6001/6002 in the scoped docs.
- Reviewed the exact diff for the two owned docs before writing this handoff.
- Skipped gameplay lint, live release tests, weighted simulation, asset inspection, localisation checks, spreadsheet checks, and MCP event diagnostics because this task is documentation-only and the parent explicitly required no gameplay or asset edits.

## Resume packet and remaining risks

No new resume packet was created because `006_independence_wave_resume_packet.md` is an explicitly protected input for this task. The parent can resume from this handoff plus the current source-of-truth map, gap audit, and content-gate repair.

Remaining risks are stale historical wording in the protected source-of-truth map and resume packet, the absence of deterministic 3/4/5 runtime proof across all live conditions, FORM-48's closed carrier/member admission, missing ASSET040-ASSET043 animation packages, the exact-recording-rights block on 6001, and the lack of a currently admitted Radical Bloc containment-survival route.
