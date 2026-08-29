# Event 006 documentation and source-of-truth authority handoff

Date: 2026-08-20.

Scope: reconcile the seven accepted Event 006 specification parts, current implementation evidence, package-admission authority, post-`7858a2b1f` dormant-carrier semantics, and later committed changes.

Disposition: documentation-only audit and durable handoff.

No gameplay, localisation, asset, GUI, map, technology, or workbook file was edited by this pass.

No gameplay completion claim is made.

## Executive current boundary

The current allocator audit passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 runtime adapters, 32 content-attested packages, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

The current automatic ladder is 3/4/5/7/10, with World Collapse also targeting 10.

The current adapter-only fail-closed IDs are IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179.

The current 32-package content-attestation set is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, and IW-184.

The current package-local or research-only boundary includes IW-046, IW-047, IW-048, IW-049, IW-050, IW-051, IW-052, IW-053, IW-054, IW-055, IW-057, and IW-060, while the eight adapter-only IDs remain separately fail-closed.

The current whole-event disposition remains HOLD / PARTIAL.

The command `python -B .tools/audit_event6_allocator.py` produced this boundary on 2026-08-20.

## Source-of-truth map

| Surface | Current authority | Status and boundary |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md` through `006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` | These seven files remain the design authority and are not replaced by working plans or handoffs. |
| Candidate identity and broad coverage | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, and `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md` | Use the candidate registry for identity, the installed-map bindings for current anchors and hosts, and the collision audit for tag reuse and overlay rules. |
| Current package counts and admission | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`, `docs/events/006_independence_wave/overview.md`, and the 2026-08-20 allocator audit | The current 149/126/138/40/32/29/161 boundary is consistent across the current authority documents and the fresh static audit. |
| Current release-gate semantics | Commit `7858a2b1f` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_dormant_empty_shell_release_fix_2026_08_20.md` | `is_independence_wave_dormant_country_scope` accepts either an absent tag or an existing empty startup shell with zero owned states, zero controlled states, no active Event 006 origin, and no prepared or committed origin marker. A living country remains fail-closed. |
| No-pre-event boundary | Part 2 and Part 3 of the accepted specs plus `006_pre_event_crisis_spec_supersession_2026_08_15.md`, `006_pre_event_crisis_surface_removed_2026_08_15.md`, and `006_pre_event_crisis_callback_neutralized_2026_08_15.md` | No player-facing category, mission, cost, queue, history row, or pressure surface exists before the public Event 006 report. Legacy crisis helpers are parser-compatibility residue only. |
| Joint partial-wave count | Commit `d6abc3792` and `subagent_handoffs/006_joint_partial_wave_expected_count_repair_2026_08_20.md` | The joint wrapper now recomputes the shared expected count from the actual Event 005 and Event 006 selected counts before optional expansion and locking. The previous cross-event count blocker is resolved at source, but broader joint execution remains unclaimed. |
| Focus architecture | Part 4 and Part 7 of the accepted specs plus `006_post_iw045_focus_authored_diagnostic_closure_addendum_2026_08_14.md` | The shared tree has 184 focuses and 196 connectors with zero crossings and zero node intersections in the current layout evidence. Fresh MCP inspection still reports 15 blocking workspace diagnostics, so this is bounded focus evidence rather than whole-event acceptance. |
| Grouped formable and GUI contract | Part 6 and Part 7 of the accepted specs plus the current formable state-puzzle handoffs | Fourteen runtime-authored families, seventeen attached decision categories, 50 candidate-state rows, and 100 DDS pieces remain the current grouped surface. FORM-07 and FORM-48 remain fail-closed, and FORM-08 remains below its required three-state threshold. |
| Weighted-logic evidence | `006_admitted_package_ai_evidence_tranche_addendum_2026_08_13.md` and the scenario-specific probability handoffs | The next evidence tranche is queued for IW-040 KUB and IW-044 TAT. Fresh KUB mission inspection found 11 candidates, zero available candidates, 15 required inputs, zero unresolved inputs, and `poolComplete=false`, so no quantitative balance claim is valid. |
| Whole-event acceptance | `subagent_handoffs/006_event6_completion_audit_current_2026_08_15_followup.md`, `quality/spec_acceptance_checklist.md`, and `quality/simplifications_omissions_and_blockers.md` | Static bounded passes do not close package, probability, GUI, live execution, save/load, catalog, or whole-event gates. Preserve HOLD / PARTIAL. |

## Seven-part specification reconciliation

| Accepted spec part | Current implementation evidence | Reconciliation |
| --- | --- | --- |
| Part 1, core event design | The allocator reports the exact 3/4/5/7/10 ladder, protected-host witness, anchor-to-compact-to-extended ordering, and no pre-event crisis surface. Commit `7858a2b1f` also closes the empty-shell release boundary without relaxing living-tag protection. | Source design and current bounded implementation evidence align. Shortfalls remain blocked wave slots rather than host annexation or overlapping ownership. |
| Part 2, event flow and evolutions | The accepted no-pre-event section is reflected by the 2026-08-15 supersession/removal handoffs. The hidden `chaosx.nr6.40` Join retry and the joint partial-wave count repair are source-documented. | Source design aligns with current source evidence. Fresh Event MCP inspection is partial because the workspace-wide graph is large, and it reports zero selected blocking diagnostics rather than complete runtime proof. |
| Part 3, mechanics and decisions | The shared country values, relationship layers, package-local ledgers, route decisions, and post-event gating are present in the accepted design and current package handoffs. The no-pre-event decision boundary is explicit in both the spec and source handoffs. | The bounded mechanics are source-wired, but package-specific AI, live consumer behavior, and whole-event acceptance remain open. Do not promote the old crisis category or queue wording. |
| Part 4, focus-tree architecture | The accepted one-tree scope is implemented as `independence_wave_focus_tree`, with reviewed additive-carrier treatment for IW-012 ICE. Fresh focus MCP evidence reports 184 focuses, 196 connectors, zero crossings, zero node intersections, and two long connectors, but validation is false because unrelated workspace diagnostics remain. | The accepted architecture is current. Keep the broad focus expansion closed and route remaining work through bounded evidence or package-owned hooks. |
| Part 5, country packages and regional overlays | The current admission set is 32 packages across 29 groups, with eight adapter-only fail-closed IDs and package-local IW-046/IW-047/IW-048/IW-049/IW-050/IW-051/IW-052/IW-053/IW-054/IW-055/IW-057/IW-060 boundaries. Part 5's IW-043 and IW-058 signature contract remains source-implemented but unadmitted. | Package admission is the current source-of-truth boundary. Do not promote a package from a tag, history shell, adapter, portrait, flag, or formable row alone. |
| Part 6, formables, league, super-events, and scenario | Current documentation and source evidence retain the fourteen-family grouped state puzzle, six numeric scenario families, eight player-facing scenario modes, four intensities, FORM-07/FORM-48 fail-closed gates, and the FORM-08 two-state research limitation. Fresh GUI MCP inspection is complete for the named window but reports 1,999 retained diagnostics, 273 visible-overlap findings, and truncated global graph diagnostics. | The grouped source contract is current, but visual and family-isolated acceptance is not proven. Preserve the accepted formable gates and the ordinary super-event 23 audio block. |
| Part 7, AI, balance, assets, achievements, and acceptance | The shared-tree and grouped-GUI scope is current. Fresh KUB probability inspection is source-valid but has no available candidates and an incomplete pool, while the current AI tranche explicitly remains evidence-blocked. Fresh map inspection passes state membership, networks, adjacencies, supply, and railways but fails workspace-wide locator validation with truncated unrelated diagnostics. | The acceptance boundary remains partial. Keep AI evidence scenario-specific, preserve asset rights and provenance gates, and do not convert source-only or partial MCP evidence into live balance or gameplay completion. |

## Contradictions and stale claims

| ID | Files and evidence | Disposition and parent action |
| --- | --- | --- |
| C-01 | `subagent_handoffs/006_event6_completion_audit_current_2026_08_15_followup.md:51-55` says package preflight and execution require `exists = no`, and `subagent_handoffs/006_event6_dormant_release_audit_2026_08_15.md:72` repeats that claim. Commit `7858a2b1f` changes the preflight and execution paths to `is_independence_wave_dormant_country_scope`. | Superseded for release semantics by `006_dormant_empty_shell_release_fix_2026_08_20.md`. Retain the August 15 audits for their other evidence, but do not use their `exists = no` wording as current authority. |
| C-02 | `006_source_of_truth_map.md:167` instructs the parent to preserve a “crisis queue sentence,” while Part 2 and Part 3 and the August 15 crisis supersession handoffs prohibit a player-facing pre-event queue. `006_event6_completion_audit_current_2026_08_15_followup.md:47` already labels the source-map instruction stale. | Open documentation cleanup item. Remove or replace the phrase with current post-report public-summary wording in the next parent docs pass. Do not restore a crisis queue in source. |
| C-03 | `006_iw038_ruthenia_implementation_plan_current_2026_08_10.md:143` says IW-038 remains a registry row with zero allocation weight until future gates pass. `subagent_handoffs/006_iw038_ruthenia_country_package_final_audit_2026_08_10.md` says the package is source-complete and admitted, and IW-038 is in the current 32-package set. | Open plan-disposition issue. Mark the old implementation-plan status superseded or promoted to the current admitted handoff, while retaining any remaining non-admission caveats such as live QA. |
| C-04 | `006_iw014_cat_standalone_admission_and_form07_late_binding_addendum_2026_08_05.md:5` still says “proposed narrow improvement tranche” and retains a historical 15/14 arithmetic snapshot. The CAT admission handoff and current source map include IW-014 in the 32-package attestation set. | Open plan-disposition issue. Mark the addendum implemented/promoted for CAT admission and retain FORM-07 as a separate fail-closed gate. |
| C-05 | `006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md:3` says proposed package-local tranche, while current package-local handoffs document implemented constants, effects, decisions, AI, localisation, and shared-focus callbacks. | Partially implemented and still queued, not contradictory on central admission. Update its disposition to implemented package-local work with identity, roster, flag, typed-probability, and route-leadership gates still open. |
| C-06 | The top current override in `006_source_of_truth_map.md` and the resume packet name IW-055 and IW-057 as current package boundaries, while `006_source_of_truth_map.md:172` omits both from the parent follow-up package list. | Open list-reconciliation issue. Add IW-055 research-only and IW-057 package-local entries to the follow-up list or explicitly state that the list is intentionally narrower than the top authority block. |
| C-07 | `006_core_dynamic_system_improvement_addendum_v67_2026_08_01.md:21` describes a connected “crisis queue” in its retained core-family summary, while the accepted no-pre-event rule retires the player-facing crisis surface. | Treat the plan sentence as historical residue and mark it superseded in a future documentation pass. Preserve the bounded Universal Belligerence repair and its source handoff. |
| C-08 | `documentation_cleanup_handoff_2026_08_11.md` and `documentation_cleanup_handoff_current_2026_08_10.md` retain 29/26/164/37 bodies under explicit supersession notices, and older current-authority sections retain 27/25/166, 28/25/165, and related arithmetic. | No current count contradiction exists because the notices label these values historical. Do not delete the traceability bodies, but do not use them for implementation decisions. |
| C-09 | August 15 audits described the joint Event 005 plus Event 006 expected-count overwrite as unresolved. Commit `d6abc3792` adds the actual selected-count recomputation in `common/scripted_effects/005_006_liberations_collision_effects.txt` and its 2026-08-20 handoff. | Resolved at source. Mark the old blocker finding superseded, preserve the failed historical comparison result, and retain broader joint execution as unproven. |

## Plan and handoff disposition ledger

| Document | Disposition | Current action |
| --- | --- | --- |
| `006_admitted_package_ai_evidence_tranche_addendum_2026_08_13.md` | Executed / evidence-blocked | Queue the next bounded KUB/TAT probability and route-selection evidence pass. |
| `006_core_dynamic_system_improvement_addendum_v67_2026_08_01.md` | Bounded repair implemented; broad expansion stopped | Preserve the Universal Belligerence uniqueness repair and retire crisis-queue wording. |
| `006_form03_language_industry_progression_addendum_2026_07_15.md` | Source-implemented; live validation and route readiness queued | Keep the addendum as a validation queue, not a completion claim. |
| `006_form48_pacific_federation_implementation_plan_2026_07_16.md` | Design tranche implemented; runtime admission blocked; superseded as next-tranche status | Preserve the locked FORM-48 design and fail-closed FSM, member, and identity gates. |
| `006_generic_focus_contract_closure_handoff_2026_08_02.md` | Broad focus expansion closed; bounded evidence queued | Use current post-IW-045 focus evidence and do not create bespoke trees. |
| `006_iw012_formal_route_ai_closure_addendum_2026_07_28.md` | Source-implemented; final probability and whole-event acceptance queued | Keep IW-012 ICE as the reviewed additive-carrier exception. |
| `006_iw014_cat_standalone_admission_and_form07_late_binding_addendum_2026_08_05.md` | Implemented admission design with stale proposed status | Parent should promote CAT admission in the plan header and leave FORM-07 fail-closed. |
| `006_iw033_iw041_focus_depth_plan_2026_08_05.md` | Superseded as implementation blocker | Preserve the one-tree decision and treat country-specific focus breadth as waived. |
| `006_iw038_ruthenia_implementation_plan_current_2026_08_10.md` | Source-complete/admitted in current handoff; plan status stale | Parent should supersede the zero-weight sentence and retain remaining live-QA caveats. |
| `006_iw043_iw058_signature_packages_improvement_addendum_2026_07_18.md` | Source implemented; package admission blocked | Keep IW-043 and IW-058 outside central attestation until identity, rights, asset, and full-package gates close. |
| `006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md` | Package-local implementation tranche partially implemented; central admission blocked | Queue identity, roster, symbol, typed probability, and route-leadership evidence. |
| `006_iw070_iw072_transcaucasus_source_complete_tranche_addendum_2026_08_05.md` | Bounded implementation implemented and audited | Preserve current ARM, GEO, and AZR admission with FORM-16 readiness gates. |
| `006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md` | Accepted implementation handoff; runtime admission blocked | Keep IW-093 and IW-098 adapter-only and fail-closed. |
| `006_post_iw045_focus_authored_diagnostic_closure_addendum_2026_08_14.md` | Implemented and MCP-validated bounded focus cleanup | Queue only authored-diagnostic follow-up and KUB/TAT probability evidence. |
| `006_rival_bloc_invitation_response_expiry_followup_2026_07_22.md` | Implemented and resolved | No additional work is authorized by this follow-up. |
| `006_dormant_empty_shell_release_fix_2026_08_20.md` | Implemented current release-gate correction | Use this as the current dormant-carrier release authority. |
| `006_joint_partial_wave_expected_count_repair_2026_08_20.md` | Implemented current joint-count correction | Use this as the current expected-count authority and do not reopen the old overwrite blocker. |
| `006_event6_completion_audit_current_2026_08_15_followup.md` | Current count and whole-event audit with stale release-gate wording | Retain counts, HOLD / PARTIAL, and other evidence, but supersede `exists = no` passages and the resolved joint blocker. |
| `006_event6_dormant_release_audit_2026_08_15.md` | Current dormant-release audit with stale `exists = no` wording | Retain fixed-capital and rollback evidence, but use the 8/20 handoff for dormant-shell semantics. |
| `006_pre_event_crisis_spec_supersession_2026_08_15.md`, `006_pre_event_crisis_surface_removed_2026_08_15.md`, and `006_pre_event_crisis_callback_neutralized_2026_08_15.md` | Current no-pre-event authority | Preserve these as the no-category, no-mission, no-cost, no-queue boundary. |
| `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | Current count and resume authority with stale parent-follow-up wording | Add the 8/20 release note and remove the crisis-queue instruction during the next docs-only pass. |
| `documentation_cleanup_handoff_2026_08_11.md`, `documentation_cleanup_handoff_current_2026_08_10.md`, and `documentation_cleanup_handoff.md` | Historical or superseded cleanup records | Retain for traceability and do not use their old arithmetic as current status. |

## Duplicate and superseded document list

The two August 10 and August 11 cleanup handoffs duplicate older arithmetic and already carry supersession notices.

The July 28 cleanup handoff is historical CHU and portrait-shelf routing evidence and is not current Event 006 authority.

The August 15 completion and dormant-release audits overlap the August 20 release-gate handoff and are superseded only for their `exists = no` claims.

The August 15 no-pre-event crisis handoffs overlap each other by design and should remain as dated evidence rather than being merged into a new gameplay design.

No document was deleted or merged by this pass.

## Stale prompt and instruction list

`006_source_of_truth_map.md:167` is a stale parent instruction because it asks for a crisis queue sentence that the accepted Part 2 and Part 3 design explicitly removes.

`006_iw038_ruthenia_implementation_plan_current_2026_08_10.md:143` is a stale implementation instruction because it says IW-038 has zero allocation weight after the package was admitted.

`006_iw014_cat_standalone_admission_and_form07_late_binding_addendum_2026_08_05.md:5` is a stale plan status, although its FORM-07 fail-closed boundary remains current.

`006_core_dynamic_system_improvement_addendum_v67_2026_08_01.md:21` contains stale crisis-queue language in a retained plan summary.

The Event 006 routing prompt remains the routing authority and no stale package-admission instruction was identified there, but its prose contains the hard-wrap issues listed below.

The August 15 `exists = no` passages are stale handoff evidence rather than current prompts, and they must not drive new implementation.

## Markdown hard-wrap issue list

The targeted prose audit found accidental mid-sentence physical line breaks in `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md:25-29`.

The targeted prose audit found multiple mid-sentence breaks in `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:84-164`.

The targeted prose audit found mid-sentence breaks in `docs/specs/006_independence_wave_specs/prompts/independence_wave_subagent_routing_and_briefs.md:85-89`.

The targeted prose audit found mid-sentence breaks in `docs/plans/006_independence_wave_plans/006_form03_language_industry_progression_addendum_2026_07_15.md:3-10`.

The targeted prose audit found mid-sentence breaks in `docs/plans/006_independence_wave_plans/006_form48_pacific_federation_implementation_plan_2026_07_16.md:15-28`.

The targeted prose audit found multiple mid-sentence breaks in `docs/plans/006_independence_wave_plans/006_iw043_iw058_signature_packages_improvement_addendum_2026_07_18.md:5-10`.

The targeted prose audit found multiple mid-sentence breaks in `docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md:3-10`.

The targeted prose audit found mid-sentence breaks in `docs/plans/006_independence_wave_plans/006_rival_bloc_invitation_response_expiry_followup_2026_07_22.md:5-18`.

The specification README also contains deliberate historical hard wraps in its final implementation-reconciliation paragraphs and should be normalized only in a separate documentation pass.

These hard wraps were not changed because the requested scope is a durable authority handoff and the parent did not authorize a broad documentation rewrite.

## MCP and validation evidence

The fresh allocator audit passed with the current 149/126/138/40/32/29/161 boundary and the 3/4/5/7/10 ladder.

Fresh `hoi4.event_inspect` lint for `chaosx.nr6.1` and `chaosx.nr6.40` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics at revision `56319cc12de881e50904384f7991f675b88c92bf9c05828ec8c86ff0efb828fa`, with linked artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58530f673f723616face83d999254758bbf486fce85dd986200c1b9b1b7d01a0/f38e5ffa6a2991f8327163b22a024477337c0e309cd431f2c85863353a737cef/event-lint-56319cc12de8.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/895c25334cee158487bc13f19137d75d7e65a7489f0728ef65eac0eb7f6df6d2/9ecc3078631a8f72f964cb13bfa5c5975c0beaa4b0811c3af15fe0d1cb14f8c4/event-lint-56319cc12de8.json`.

The Event MCP result remains partial because the workspace graph deferred large helper and lifecycle projections, and it is not a live-game result.

Fresh `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `independence_wave_focus_tree`, with 184 focuses, 196 connectors, zero crossings, zero node intersections, two long connectors, and 15 blocking workspace diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c332a4a6a2b65e6489b28fbd990dc883fccf409f0bd735a1f959ba17258173c/e4b8a361109374995dffa9f90f4efb458292b3651415659a9d4e24e0fd795560/focus-inspect.c57a08425ee62eda.json`.

The focus inspection is bounded source evidence and does not certify the tree or whole event as complete.

Fresh `hoi4.gui_inspect` returned `GUI_INSPECTED` for `chaosx_independence_wave_formable_state_puzzle_window` under `E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09`, with 93 inspected elements, 1,999 retained diagnostics, and 273 visible-overlap findings, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9ae969a60ffb273d122398424bb8260bac511eb8af8fff0bcc2901d557694e2/946c3a87c8251ef87c7d308c8b2e116ed47d880c8a41e2515d06c318d104ec42/gui-inspect.09be51e499799bbd.json`.

The GUI evidence therefore preserves the aggregate grouped contract but does not prove family-isolated visual acceptance.

Fresh `hoi4.probability_inspect` for `common/decisions/006_independence_wave_kuban_decisions.txt` with `mission_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED`, 11 candidates, zero available candidates, 15 required inputs, zero unresolved inputs, and `poolComplete=false` at source hash `87ba7c79b4c87b980b378f0a6c08cd27051363bea3b9b44eaec4a7ee49a4f25c`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/151d1a9583bbf284e29f605327ad2b19efe9943a6df94df892088a60848e43d6/44238ad09cd6e17a75aaf71573611a1a2e52449f46bcb44aa24bbb910069329a/probability-inspect-87ba7c79b4c8.json`.

The probability result supports the evidence-blocked status and makes no balance, timing, dominance, or starvation claim.

Fresh `hoi4.map_inspect` for states 73, 408, 409, 234, 249, and 651 passed state membership, networks, adjacencies, supply, and railways, but failed workspace-wide locator validation with truncated unrelated building and port diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f40803ae00c7383fd17db246d41125faf5f6794ef1c8bce6944fa1043c23285/3519cd82c02f53b206f7b70fb707144a063f4923920182e40e97a8e8adf6793d/map-inspect.7c0b0196de715c91.json`.

The map result is evidence for the named bindings and not a whole-map completion claim.

The joint repair handoff records a fresh Event MCP lint and render with zero selected blocking diagnostics, while `hoi4.event_compare` returned `EVENT_REVISION_NOT_CACHED`; no before/after graph delta claim is made.

No live Hearts of Iron IV session was launched.

No workbook or CSV export was edited.

## Files changed by this pass

Only `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_docs_authority_2026_08_20.md` was created.

No accepted spec, plan, handoff, source implementation, asset manifest, localisation, GUI, map, or workbook file was merged, superseded in place, promoted, queued, or rejected by this pass.

The disposition changes above are recommendations for the parent and are not silently applied to older documents.

## Recommended parent decisions and cleanup actions

1. Use the 2026-08-20 dormant-shell handoff and commit `7858a2b1f` as the release-gate authority for existing empty startup shells.

2. Use the 2026-08-20 joint-count handoff and commit `d6abc3792` as the expected-count authority for partial Event 005 plus Event 006 waves.

3. Remove the source-map “crisis queue sentence” instruction and retain the no-pre-event rule from Part 2, Part 3, and the August 15 crisis supersession handoffs.

4. Mark the IW-038 plan as superseded or promoted to the admitted package handoff, mark the IW-014 plan as implemented admission with FORM-07 still fail-closed, and mark IW-057 as partially implemented package-local work with its remaining evidence gates.

5. Correct the source-map parent follow-up list so IW-055 and IW-057 are not silently omitted from the current package-local boundary.

6. Run the next accepted tranche through `chaosx_ai_probability_auditor` for IW-040 KUB and IW-044 TAT using typed scenario fixtures and same-scenario comparison evidence before any AI-weight or package-admission change.

7. Do not open a new country, focus, formable, super-event, or crisis-surface tranche while the admitted-package AI evidence tranche remains `EXECUTED / EVIDENCE-BLOCKED`.

8. Schedule a separate Markdown normalization pass for the listed hard-wrap files, preserving headings, lists, tables, block quotes, code blocks, and historical supersession notices.

## Remaining risks

Event 006 still has no live release, save/load, player-observation, or whole-event runtime acceptance evidence.

The package-admission boundary is source and audit bounded, not a claim that all 149 publishers are playable or that all 32 admitted packages have live balance proof.

The fresh MCP focus, GUI, map, and event inspections are partial or workspace-diagnostic-limited, and the probability surface has no available candidates under the supplied source-only inspection.

The parent must review and apply the recommended documentation dispositions before relying on older current-sounding plan paragraphs.
