# Event 014 spec receipt reconciliation

Date: 2026-10-03.
Owner: `chaosx_documentation_curator`.
Disposition: documentation patch implemented within the seven-file write scope; parent review and commit remain pending, and full Event 014 completion remains open.

## Scope and acceptance basis

The parent explicitly requested reconciliation of six spec receipt documents plus this handoff, with no gameplay, GUI, assets, spreadsheet, other-document or commit writes.
The parent instruction says “56distinctfinalportraitrequirementstaysaccepted/unfinished” and explicitly preserves seven bespoke models, nine gameplay families, approved cavalry/infantry visual reuse and no animation toggle.
That instruction establishes the preserved design requirement and archive-reconciliation scope; it does not authorize a new portrait generation route, approve old placeholders or establish all 56 source subjects' gender, human identity or framing.
The parent owns changing Feast Guard export recovery, five missing model-manifest links, implementation, final review and integration.
The curator did not change or generate portraits, models or other runtime files and did not launch HOI4 or commit.

## Source-of-truth map

| Claim | Authority or evidence | Disposition and boundary |
| --- | --- | --- |
| 56 distinct regional HOI4-style finals, eight slots/seven regions | Current parent instruction; spec part 10, lines 116-148; part 12, lines 189-201 | Accepted and queued: production/acceptance remains unfinished; the specific final-production route is unresolved. No reduction to 16. |
| H01-H16 source selection and exact preservation | Current parent instruction; August v6/v7 source/recrop handoffs; current portrait receipt, lines 9-13 | Retained specifically authorized source-placeholder branch. No default-ImageGen rejection of those already selected sources and no final-art promotion. |
| Exact archive recovery | `f440c5329`, `2026-10-03_portrait_source_archive_recovery.md`, `../evidence/2026-10-03_portrait_archive_parent_review.json` | Implemented and parent-accepted at the archive boundary only: 16 exact original/crop/candidate packages, reproducible co-located commands, exact source/crop and candidate/DDS pixels, 121 archive file hashes and 62 protected runtime/definition hashes. |
| Current runtime identity/binding receipts | `2026-10-03_event014_portrait_receipt_repair.md`; `docs/assets/portraits/014_cannibalism/hannibal_static_receipt.md` | Implemented file/format/binding evidence; external static Hannibal original/crop/creator/rights provenance and artistic/live acceptance remain unresolved. |
| Current regional texture mapping and archive subset | Curator text scan and parent-confirmed independent regex scan of `interface/014_cannibalism.gfx` | Resolved count: 64 aliases reference 56 distinct existing texture paths. The 16 recovered HATE packages are a subset; remaining 40 archive status is unknown pending the portrait audit. Subject/source/final acceptance remains open. |
| Feast Cohort selected export identity | `../evidence/2026-10-03_feast_cohort_runtime_source_receipt.json`; continuation report | Current selected `11014` mesh/eight-action identity supersedes the older mismatch assertion. No new export/recovery work was performed here. |
| Feast Guard/five model-manifest links | `../2026-10-03_continuation_report.md`, `../resume_packet.md`, subsequent parent-reviewed model handoff when supplied | Changing parent-owned recovery; this patch asserts no new manifests, exact restored export hash or fully restored source fields. |
| July zero audits and aggregate asset counts | Dated 2026-07 consolidation audits named in the six documents | Historical frozen-tranche evidence retained, not current full-package or live proof. |
| AI/probability | `2026-10-03_event014_decision_probability_audit.md` and current read-only `chaosx_ai_probability_auditor` sidecar | Incomplete scenario-specific evidence; no numeric AI conclusion or weight change. |

The recovery JSON manifest's SHA-256 is `c20b9c752ef753508637deb985a0ecec41aa4961b5a98836de4c0df666beb588`, matching the parent-review receipt.
Archive acceptance remains “Archive recovery and exact-byte/pixel reproduction only; no final-art, rights, live-game or full Event014 acceptance.”

## Files changed and document dispositions

Paths below are relative to `docs/specs/014_cannibalism_specs/` unless stated otherwise.

| Document | Changed hunks | Disposition and reason |
| --- | --- | --- |
| `README.md` | Intro/acceptance basis, warlord/presentation/portrait status, current checkpoint/model receipt, manifest caution, authority order, July audit/addendum boundaries and validation boundary | Reconciled implementation evidence; 56 finals remain accepted and queued, source recovery is limited to 16. Optional A-C remain unresolved unaccepted proposals, not an accepted queue. Historical addendum acceptance is not freshly certified. |
| `quality/package_status.md` | Status date, inventory versus consumption, Feast Cohort provenance, portrait receipt/archive recovery, audit/completion boundaries | Reconciled implementation evidence; missing H01-H16 receipt/archive/reproducibility assertions superseded by exact recovery. Rights/final/visual/live and current MCP gates remain open. |
| `quality/package_validation.md` | Date/evidence scope, portrait/file counts, frozen texture scan, current archive/model receipts and MCP limits | Reconciled validation evidence; no 56-package source restoration, current exhaustive scan or engine/live validation claim. |
| `matrices/asset_inventory_matrix.md` | Evidence/count column meanings, regional/static portrait rows, historical GFX scan, protected-sheet/recovery boundary | Reconciled inventories; final counts no longer imply accepted finals. Static/sheet hashes prove preservation, not full source-frame recovery or provenance. |
| `matrices/country_package_matrix.md` | Acceptance/current-checkpoint preface, historical country audit, portrait coverage, engine-evidence limits | Reconciled implementation evidence; design matrix retained, no current full country-package completion inferred. |
| `matrices/hidden_identity_surface_audit.md` | Audit scope/header, frozen focus evidence, warlord portrait row, design-versus-visual-acceptance wording and current receipts | Reconciled secrecy evidence; no current 56-subject likeness/gender/human/framing approval or exhaustive secrecy proof. |
| `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_spec_receipt_reconciliation.md` | This report | Implemented bounded curation deliverable for parent review; not a feature-completion certificate. |

Every spec document directly records the current 64-alias/56-texture mapping, the 16 recovered HATE subset packages and the unknown archive status of the remaining 40 pending the parent-owned portrait audit.
No documents were merged or deleted.
No runtime, model manifest, asset, spreadsheet, prompt, source spec part or other handoff was edited.
No new resume packet was created; `../resume_packet.md` remains the supplied current checkpoint with its recorded limits.

## Current parent acceptance of fictional portrait production

Recorded 2026-10-03 from the parent's subsequent explicit delegation instruction, within the existing user-authorized full Event 014 implementation scope.
The parent resolves the production-route advisory: the accepted requirement remains 56 distinct fictional warlord HOI4-style finals, and the portrait-production default native ImageGen route applies through `chaosx_portrait_creator`.
This is recorded parent acceptance within the existing authorized scope, not a claim of new explicit user approval and not approval inferred from a document date, status or old worker handoff.
Its basis is the parent instruction accepting that route, the unchanged 56-final brief in spec parts 10/12, and `.agents/skills/chaos-redux-event-assets/references/portrait-production.md` production steps 2 and 4 for fictional subjects.

No direct user decision proving a universal user-supplied/RunPod ban for fictional finals was found.
The August portrait handoffs' user-RunPod assertions remain historical, unsupported as a portrait-wide prohibition; they establish no new user authority.
The grounded real-person/institution user-operated RunPod rule remains distinct from fictional native ImageGen production.
The explicit source-only/faithful-enhancement model rule remains applicable to 3D inputs; it is not extended to fictional portrait production, and the seven bespoke model production jobs remain closed.

The parent plans to authorize a separately bounded tranche of eight European original native ImageGen fictional final candidates.
This note records the accepted production route and planned tranche, not an issued production assignment, completed generation, approved candidate or accepted final.
Canonical Hannibal statics and both animated sheets, and all current runtime portrait art, remain protected until parent review authorizes any runtime installation.
No generic, 3D or real-person substitute is approved.
The 56-final requirement is unchanged and unfinished; old source placeholders receive no acceptance promotion, and their rights, visual-fitness and provenance gates remain separate.

The advisory below and its later requests to resolve final-production authority are preserved as pre-decision evidence and superseded by this parent acceptance for the production route only.
Current source/subject review, remaining archive coverage, candidate/final artistic acceptance, rights and live evidence remain open.
This addition changes only this authority note in the authorized handoff; no portrait, runtime file, spec document or parent-owned checkpoint document was changed, and no image generation, model workflow or commit was performed.

## Portrait production authority note for the parent

Fictional high-chaos warlords are agent-producible with native ImageGen under the general owner workflow: `.agents/skills/chaos-redux-event-assets/SKILL.md`, “Fictional portraits,” and `references/portrait-production.md`, production steps 2 and 4, route that work to `chaosx_portrait_creator`.
The grounded real-person/institution `source_placeholder`/`styled_final` branch is different: the user alone operates RunPod and supplies grounded finals, and agents never invent a grounded identity.
A fictional character's use of sourced commercial concept art does not itself make that character a grounded real person.

Part 10 requires 56 distinct painted HOI4 warlord busts and explicit appearance/framing/region/identity constraints, and part 12 requires complete distinct slot-region finals.
Neither inspected part supplies a direct user decision requiring RunPod or unaltered HATE art for every future warlord final.
The current parent instruction confirms the 56-final requirement's acceptance, not a particular production route.

The limiting record is `event014_portrait_completion_2026-08-26.md`, lines 9-11, 45 and 187-193: it reports H01-H16/D01-D22/E01-E18 as source placeholders with `replacement_pending: true`, says the user must supply authorized HOI4-style RunPod replacements and attributes the no-from-scratch restriction to its brief.
That is an old worker assertion about authority; it is not a direct user decision quote or independent evidence approving all 56 source identities.
The 16-specific `event014_portrait_recrop_v7.md`, lines 5-7, 50 and 65, reports a direct-source installation with `replacement_pending: false`, no current user-final request and user-only supply if a future styled final is requested.
These statements differ in scope and disposition and must not be collapsed into one unconditional final-production rule.
The current portrait receipt, lines 9-13, and archive recovery, lines 15-19, preserve the specifically selected HATE branch only; exact recovery authorizes no repaint, substitution or final promotion.

The inspected source amendment, `../014_cannibal_model_source_direction_2026-08-22.md`, lines 5 and 9-17, explicitly governs seven unit-model source/provider inputs and faithful ImageGen enhancement.
It does not establish a blanket portrait-generation ban or a user-only fictional-final rule.
The old `../014_warlord_regional_portrait_repair.md` explicitly describes independently generated fictional busts, but its July closure label and old ledger are also historical assertions, not fresh authority for replacing the selected source branch.

Advisory conclusion: native ImageGen is the general fictional production route, but this cleanup cannot approve its use to replace the current Event 014 source-selected portraits or approve those old placeholders as finals.
No direct user-decision quote proving a universal user-supplied/RunPod/unaltered-HATE final requirement was located in the inspected records.
The parent should resolve the 16-specific versus 56-wide source/final authority using the originating explicit instruction or a recorded parent acceptance within the user's authorized scope, while reviewing the new read-only portrait audit.
Until that resolution, preserve the selected sources, keep all 56 finals unfinished and avoid both “agents cannot make fictional finals” and “the current resume authorizes replacing every source with ImageGen” as established claims.
No old `source_reference_gate: PASS (56/56)`, all-male, invented-human or framing verdict is promoted here; titles such as Female Barbarian/Female Witch Doctor/Beast Clergyman are parent-raised audit leads, not curator-verified visual findings.

Count correction and supersession: the parent acknowledges that the preexisting October 3 checkpoint incorrectly treated the 16 recovered HATE archive packages as the total active portrait set. The verified current count is 64 aliases referencing 56 distinct existing textures; 16 is the recovered HATE subset, with the remaining 40 archive status unknown pending the portrait audit. This supersedes the checkpoint's 16-total claim and this handoff's initial unresolved count treatment. The parent owns correcting the event overview, resume packet, continuation report and documentation-state ledger; the curator leaves those files untouched. No visual/source/final approval follows from the corrected count.

## Contradictions, supersession and unresolved claims

| Issue | Evidence | Outcome |
| --- | --- | --- |
| Missing portrait-worker receipt/archive/reproducibility | Old README/status assertions versus current worker receipt and exact archive parent review | Resolved for H01-H16; superseded missing-source statements only. Other 40 source packages/fields are not certified. |
| Runtime coverage confused with accepted finals | README/matrices versus current curator and parent 64-alias/56-path scans | Count resolved: 64 aliases/56 distinct existing textures. Visual fitness, source approval, remaining 40 archives and all 56 final acceptances remain unresolved pending parent audit. |
| H06 dark backdrop versus white current pixels | v6/v7 cleanup assertions versus current worker review and exact recovered candidate/DDS identity | Open visual discrepancy, preserved without image edit or approval. |
| Feast Cohort mismatch asserted current | Old package-status sentence versus selected `11014` current receipt | Resolved selected-source evidence; Feast Guard/model-link recovery remains parent-owned. |
| July zero audits presented as current full proof | Six spec documents' current/final labels | Scoped to historical frozen tranches; later gates remain explicit. |
| 16 direct-source `replacement_pending: false` versus 56 `replacement_pending: true`/RunPod instruction | August recrop/completion handoffs | Authority/disposition conflict remains open; advisory note above. |
| All-source/final-rights claims | Exact recovered 16 packages versus historical 56-row source report | Rights remain reference-only/user-authorized; no redistribution license, 56-source approval or final acceptance inferred. |

Historical v6/v7 and August audit/completion bodies remain unchanged and retain their checkpoint facts; the exact recovery supersedes their absent-source assertions only for the recovered 16.
No duplicate document was merged and no historical body was deleted.
The old regional portrait repair plan still carries July closure wording and legacy slot names `AHX`, `AIX` and `AMX`; it is outside the allowed write scope and must not drive current CBA-CBH mapping.
The README now treats original prompt files as historical orchestration inputs; no named prompt was authorized for editing or audited as a fresh production instruction.
`PACKAGE_MANIFEST.md` is outside write scope and needs a parent refresh after these six spec files change; its old hashes are not called current.

## MCP evidence and probability ownership

Verified metadata exposed matching read-only routes, but invocation returned no artifact, source revision or diagnostics coverage:

| Route | Bounded request | Actual outcome |
| --- | --- | --- |
| `hoi4.event_inspect` | `mode: trace`, selector event ID `chaosx.nr14.1`, depth 1/nodes 4/edges 6 | `MCP tool hoi4_agent_tools/hoi4.event_inspect is not available to the model` |
| `hoi4.focus_inspect` | Tree `cannibalism_unified_focus_tree` | `MCP tool hoi4_agent_tools/hoi4.focus_inspect is not available to the model` |
| `hoi4.gui_inspect` | Requested window `cannibalism_hannibal_window` | `MCP tool hoi4_agent_tools/hoi4.gui_inspect is not available to the model`; the route did not validate window identity or scenario coverage. |
| `hoi4.tech_inspect` | Unlocks for sub-unit `cannibal_feast_guard`, depth 1/nodes 4 | `MCP tool hoi4_agent_tools/hoi4.tech_inspect is not available to the model` |

Tool exposure is not verified service health, and standalone Technology Tree Viewer availability was not established.
No helper-expansion/job/native-task route was used and no new render/compare acceptance artifact was obtained.
Map data or placement was not reconciled or changed; no new map-validation claim is made.
GUI ownership/review boundaries remain unchanged and required state/resolution/hierarchy/click-region/source-comparison acceptance remains open.

The read-only `chaosx_ai_probability_auditor` sidecar used source `{path: "common/decisions/014_cannibalism_decisions.txt"}`, adapter `decision_ai_will_do` and candidate `cannibalism_emergency_ration_audit` for one `hoi4.probability_inspect` request.
It reported the call pending after about 90 seconds with no result, error code, artifact, revision or explicit route blocker before it stopped waiting; the other routes' errors are not attributed to probability.
The existing specialist handoff retains 95 source decision AI blocks, 13 timed missions and no current resolved eligible pools, score traces, ranks, scenario hashes or numeric probabilities.
Preserve its scenario IDs: `E014_DECISION_CANNIBAL_STATE_BASELINE_2026_10_03`, `E014_DECISION_ACTOR_INSUFFICIENT_RESOURCES_2026_10_03`, `E014_DECISION_NON_CANNIBAL_CONTAINMENT_ACTOR_2026_10_03`, `E014_DECISION_ORIGIN_EXCLUSIVE_ISLAND_2026_10_03`, `E014_DECISION_ORIGIN_EXCLUSIVE_SIEGE_2026_10_03`, `E014_DECISION_ORIGIN_EXCLUSIVE_MARCH_2026_10_03`, `E014_DECISION_PRE_REVEAL_CONVERGENCE_2026_10_03` and `E014_DECISION_POST_REVEAL_CLEANUP_2026_10_03`.
No weight was patched, no tuning target was selected and no source-only inventory was promoted to engine balance proof.

## Validation and remaining parent work

- Parsed the exact parent archive receipt: 16 subjects, 121 archive file hashes, 62 protected runtime/definition files and archive-only acceptance scope; the recovery JSON SHA-256 matches its recorded parent receipt.
- Bounded text-only GFX scan counted 64 aliases/56 distinct existing paths, independently confirmed by the parent. Source SHA-256: `36a0b2a28c36a4ffe2b1e420b3dceefea6db289958af7f90a6f9b612cd532abb`; observed modification timestamp `2026-08-26T08:54:51.849459+00:00` is filesystem data, not acceptance evidence. No binary art was opened or changed.
- Checked new relative Markdown links in the six documents; no missing target was found.
- Audited the six documents for accidental consecutive-prose hard wraps; none was found, so none required correction. Headings, tables, lists, paragraph boundaries and deliberate structure were preserved.
- Reviewed scoped six-file changes and searched stale receipt/current-closure phrasing; dated historical statements are retained with explicit limits.

Meaningful skipped checks: full source/gameplay completion, binary/visual portrait review, current 56-source licensing/identity/framing review, model manifest/export restoration, GUI rendering/comparison, numeric probability evaluation and live consumer testing remain with their owning parent/specialists or are blocked by the recorded route limits.
The parent-owned read-only portrait audit is pending; this handoff must be reconciled with its actual 56-file/64-alias findings before acceptance.
The parent should resolve final-production authority, H06's visual discrepancy, remaining 40 archive status and any unacceptable subject/wiring findings without reducing the 56-final requirement.
Rights, static Hannibal external provenance, final-art acceptance, GUI/probability/event-helper evidence, user-owned model/audio/counter/event/live acceptance and catalog promotion remain open.
Refresh the package manifest after integrating the six documents, review this patch and commit only the accepted bounded changes.
No new simplification or fallback was introduced.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-assets` and its portrait-production reference, with focus/scripted-GUI evidence guidance consulted for the unavailable read-only routes.
No skill was created or updated and no central MCP wrapper was introduced.
