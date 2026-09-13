# Event 021 Random Civil War Documentation Source-of-Truth Map

Date: 2026-09-02

Current test-release update (2026-09-13): the rework is complete for test entry, Event 021 remains `Needs Testing`, and the runtime test-release gate plus default reworked-event registration are open. Final acceptance certification remains separate and unresolved; the dated rows below retain their historical gate state unless superseded by the current acceptance ledger or `test_release_gate_2026-09-13.md`.

Purpose: record which Event 021 documents are authoritative, which are historical evidence, which remain queued, and which contradictions require an owner decision.

## Authority order

The accepted design source is the complete `docs/specs/021_random_civil_war_specs/` package, including its master spec, ten numbered parts, matrices, research notes, revision notes, role review, manifests, and prompts.

The current implementation is evidenced by the checked-out Event 021 source and the current read-only MCP artifacts listed below; implementation files are not documentation authorities for changing the accepted design.

`docs/events/021_random_civil_war/overview.md` is the concise current implementation summary.

`docs/events/021_random_civil_war/acceptance_evidence.md` is the current acceptance ledger and the authoritative record of open certification gates.

`docs/plans/021_random_civil_war_plans/post_fix_improvement_loop_closure_addendum_2026-08-31.md` is the current closure plan and evidence queue.

Other plans and subagent handoffs are historical evidence or bounded owner handoffs unless they explicitly point to the current acceptance ledger.

## Current-state ledger

| Surface | Current evidence | Disposition |
| --- | --- | --- |
| Resumed Event graph trace | Focused downstream trace revision `8cde42798e040fdadd5e86c2c299c46a8802c4ba48ebe7af4175cc8665b7864d`, graph hash `46db6136a16ab3119b59fa9c08b10cfb018dcbbdfbef7cdbaf77d618720da6e8`, and current authoritative trace artifact. The matching helper-expanded retry returned `INTERNAL_ERROR` with zero files or artifacts. Artifact-backed compare returned `EVENT_GRAPH_ARTIFACT_INVALID` even for a fresh-artifact self-comparison, and revision-backed self-comparison returned `EVENT_REVISION_NOT_CACHED`. | Current focused evidence. Helper-expanded lifecycle and semantic comparison remain isolated MCP service blockers. |
| Event graph | Lint revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, graph hash `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`, zero selected Event 021 issues, partial only because workspace-wide helper/lifecycle projection was deferred | Current focused evidence; a post-source-fix refresh returned this unchanged cached revision, so no post-fix helper/lifecycle proof is inferred |
| Event overview layout | Layout hash `3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8` at the current Event 021 overview render | Current focused evidence; no older-revision compare claimed |
| Full helper state flow | Revision `4be54f093cb023219f3d13a2c8706e5d07a072c1225eaf4e498f5aab078c9572`; the unused remnant-capital leak is gone and remaining warnings are guarded cross-helper transaction reads | Pre-trigger-fix evidence; three post-fix refresh attempts returned MCP `INTERNAL_ERROR` without an artifact |
| Decision probability | 18 candidates, zero unresolved source inputs, source revision `5caf58267a9b52758269a0b0919eee5b8d5d5475bc25254b826f176379abd081` | Current targeted evidence; full named matrix pending |
| Mission probability | 3 candidates, zero unresolved source inputs, source revision `5caf58267a9b52758269a0b0919eee5b8d5d5475bc25254b826f176379abd081` | Current targeted evidence; full named matrix pending |
| Strange incident probability | 8% incident, 92% no incident, zero unresolved inputs, scenario hash `dfc486d2c35bd1237686439b22e74de17dbed503085b3e52346d81252640e284` | Current targeted evidence; full named matrix pending |
| Target-weight parent diagnostic | Stable 122, weak 916, invalid 0 and ineligible, zero unresolved inputs, analysis `probability-75458d26511189833fd24427`, scenario hash `29240122aa242e26156dda7b172370506bbb5823b14d53054c5fd0566feeb8f9` | Current manifest-backed parent evidence; specialist certificate and full named matrix remain pending |
| Recurrence parent pre/post diagnostic | REC-05 exposed a missing broken-guarantee contribution. The owner patch adds centralized settlement-violation and unresolved-sponsor pressure. Post-change REC-01 through REC-06 resolve to 0, 100, 0, 55, 60, and 0; the supplementary sponsor fixture resolves to 45. Same-scenario raw-score comparison attributes only +25 to REC-05 and +10 to sponsor dependence, with zero unresolved inputs and no regressions. | Current manifest-backed parent evidence and demonstrated source defect fixed; independent specialist certificate and full named matrix remain pending |
| Sponsor AI parent diagnostic | SPN-01 through SPN-05 complete against the current three-decision source pool with zero unresolved inputs. The result proves exact score and eligibility relationships while retaining the adapter's score-only boundary. | Current source-backed parent evidence; independent specialist certificate and full named matrix remain pending |
| Settlement SET deterministic review | SET-01 through SET-06 map to ordered surviving-actor, topology, talks, authority, and legal-route branches. SET-04 exposed a missing recurrence classification for hardliner non-negotiated government victory; the owner patch now marks it harsh and failed before recurrence preparation. | Current source-backed deterministic evidence and demonstrated defect fixed; independent disposition and lifecycle sequence remain pending |
| Front-count FRT deterministic review | FRT-01 through FRT-04 consume one distinct live ordinary route per opposition actor and stop on evidence, host, or global caps. The review removed the fixed-archetype FRT-04 defect. FRT-05 now uses a separate package-owned Event 006 additional-front transaction with exact package and anchor proof, actual-war proof, belligerent/front caps, narrow rollback, and distinct primary/secondary lifecycle pointers. | Current source-backed deterministic evidence and demonstrated defects fixed; live Event 006 additional-front lifecycle remains pending |
| Global queue GLB deterministic review | GLB-01 through GLB-07 map to target proof, pressure-band review dates, persistent Critical admission, launch-time capacity, annex cleanup, successor grace, and normal-human immunity. GLB-04 exposed a capacity check at the wrong lifecycle stage; queue admission now persists while launch remains capped. A second review defect could retry a failed opening twice in one bounded country review; dispatch now occurs exactly once from the frozen due marker. | Current source-backed deterministic evidence and demonstrated defects fixed; live scheduler sequence remains pending |
| Wars cluster CLU deterministic review | CLU-01 through CLU-05 map to row 1003, low-chaos role separation, the narrow high-pressure Event 004 overlap, Fury exclusion, package reroll safety, exact no-target skip receipts, and one cluster pacing event. The review removed a stale Domestic Unrest registration and added the missing low-chaos Event 004 reservation boundary. | Current source-backed deterministic evidence and demonstrated defects fixed; live cluster sequence remains pending |
| Fracture Cascade SCN deterministic review | SCN-01 through SCN-07 map to verified ID 18, four types, four intensities, centralized target shares, severity bands, normal-human eligibility, same-tag fallback, and immediate setup. Maximum now freezes its eligible pool before committing any crisis, so countries created during the run cannot join that run. Every type selects the prepared same-tag route first for unsafe one-state or all-island countries, and High/Maximum setup can enter the bounded multi-front transaction without a globally active Evolution I. | Current source-backed deterministic evidence and demonstrated defects fixed; Low minor preference and High major preference await the exact probability baseline and compare cycle; live timing remains pending |
| Fresh independent archetype and severity audit | Current ARC-01 through ARC-08 and SEV-01 through SEV-06 completed in worker commentary; the worker then wedged in zero-weight strange-incident analysis and was shut down without a durable handoff | Supplementary evidence only; not a full-matrix certificate |
| Final missing-family probability certificate | One full missing-family auditor, two disjoint replacements, three earlier TGT-only attempts, one exact REC-only retry, and later bounded retries failed to return an independent certificate. The latest TGT-only worker wrote `subagent_handoffs/ai_probability_tgt_independent_2026-09-01.md`, but interruption preceded its first MCP call and the exact validated manifest body was not preserved in the parent handoff. The validated TGT, REC, and SPN requests succeed through the parent MCP route, proving the service and fixtures work while the specialist execution path remains stuck. | Repeated specialist/tooling blocker with a durable blocked handoff; bounded parent diagnostics pass for TGT, REC, and SPN, but the release gate remains closed |
| Shared focus tree | Revision `55a900cb833aadee310a6c5b0f480af8cf0ea73522de74cef01f334788f351ae`, 184 focuses, 195 connectors, no tree-local diagnostic, one unrelated vanilla localisation warning | Current focus inspection/render evidence; Event 006 shared surface |
| Event 006 static integration | Current country API, scenario matrix, allocator, FORM-16, and flag audits pass. Results include 242 broad tags, 191 resolved carriers, 149 publishers, 138 ranked scenario-selectable packages, 32 content-attested packages, 29 compatible reservation groups, and 102 complete flag families with zero incomplete families. | Current static contract evidence; engine-backed Event 021 launch matrix remains pending |
| Map | Revision `fa76cadf611a1bf937556584a71b1e1e0bbde4b0a9b8364ca86614218e0918be` passes state/region membership and adjacency, supply, and railway checks | Current map evidence; unrelated position/port/localisation diagnostics remain outside Event 021 |
| Event 021 assets | Current `interface/021_random_civil_war.gfx` contains 40 unique texture references and all 40 referenced runtime files resolve | Current source/runtime asset evidence; user live consumer review pending |
| Event 021 GUI | Event 021 owns no custom GUI. A current shared-window inspection and multi-state render resolved the reported checkbox overlap as mutually exclusive checked and unchecked variants occupying one visual slot. | No Event 021 GUI patch required; shared repository symbol collisions remain outside Event 021 ownership |
| Final completion re-audit | `subagent_handoffs/event_completion_reaudit_final_2026-08-31.md` demonstrated a duplicate Event 006 opening append: a zero/default host-scoped receipt row followed by the actual actor-scoped row. The host-scoped append has been removed; the remaining actor call follows actual receipt capture and mirrors its snapshot to the host. `subagent_handoffs/event_completion_reaudit_post_patch_addendum_2026-08-31.md` independently verifies the source correction. The required final audit `subagent_handoffs/event_completion_final_audit_2026-09-01.md` found no remaining demonstrated actionable source defect and assigned `INCOMPLETE` because certification and runtime evidence remain open. | Demonstrated source defect fixed; release gate remains closed pending probability, MCP lifecycle/comparison, engine-matrix, runtime-sequence, and user-owned live evidence |
| Workbook/catalog | A stale Domestic Unrest/Low Event 021 entry was removed from the authoritative workbook. The export now succeeds with Event 021 as Minor Repeatable, chaos level 1, `Needs Testing`, and only Cluster 1/Wars/Medium; SCN-018 contains four types and four intensities and retains `Needs Testing`. Current Events/Clusters/Scenarios export hashes are `2094ed00142065b75ac53c9e30cae46848e5416613a4e796b24dd8d13a6f445a`, `6df8ee8871b5896f98e65b736377c49eb98eecfb834774261ba9285c2c184308`, and `96d076700cd9da866ca13c2da9eaa89ddc738613e80d5986c5680e4856183602`. | Current workbook/export parity; `Needs Testing` remains non-final pending certification. Repair handoff: `subagent_handoffs/spreadsheet_event021_cluster_alignment_2026-09-01.md` |

## Duplicate or superseded document list

`improvement_loop_addendum.md` repeats `Acceptance checks`, `Current contradiction`, and `Required design` headings for separate historical tranches; those repeated headings are deliberate tranche structure, not duplicate active design sources.

`subagent_handoffs/event_completion_auditor.md` is a superseded pre-improvement completion audit and must not override the current acceptance ledger.

The original icon and generated-art handoffs are superseded for current integration status by the current GFX/runtime evidence recorded in the event docs.

The original probability, localisation, and scripted-system handoffs are bounded historical reports whose current status is superseded by the current acceptance ledger and closure addendum.

## Current artifact references

Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59c2b4f586f3e23f7b826f022bfae2e1e9bd82c6db110b4cac62dcb01f5e98aa/beb2e27bb56b2f9654e975afb6b479595ed4a2e5a728eb578bdd02b2bae9061d/event-lint-cfdc65be2a28.json`

Event overview JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5dbdb151512bb9f51eefb1b45ffccbde8b0219691c5c7ee657fe4deccfcf331/de16a9e81bf9df7c8f4c99a3df2d83c2e07c64b276702adc05e90ac99798e3e9/event-overview-cfdc65be2a28.json`

Full helper state flow: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e70f7b0a7ae3d7476198812fd7beedb78094c263ce349ccd7547bf4e5e3ac022/e77635ab84777c00c45ba8b3c6657ff6cc88a6dec9d3b6699aa450cddc2d7f78/event-state_flow-4be54f093cb0.json`

Decision probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e01749c7c382c20c56d3807dd25d2337c237c8af6066334d4b3afb1c25bb54c3/85884afa06f5a2d5a1a1ec07a984a6d3eb885329147f64e9c97b280db8aea681/probability-inspect-b012bf7ee578.json`

Mission probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ac4f796958eeea867d6297249f86a53b050c047d1b45b51c2aefb12127dafcd/71da69ca9a08de6e0434e0951f45039f0811e0e8a3e416b98bacc33532beb221/probability-inspect-b012bf7ee578.json`

Strange incident probability: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2620789887970e9d0c561b0f3b1a98565ea727d3a1c11b205d84d59e6f4d68d2/6777be1e3da5a8d3fb3f7ed453f8adfe725fd318db29f22fea07701909d946f0/probability-6238523a08ebef03f0a38e07.json`

Target-weight parent diagnostic: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c55b09805cb98885e7b2881831e92bd9dd49b233af6d30b80bc117acbe64b72/44399017e8619eae29d8136e70ddc77f3d389e32b2fb1ccd8c4a9d7fd986f820/probability-75458d26511189833fd24427.json`

Recurrence parent pre-change evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ac464e59babe597ec77c48d3f502887722391f8d67be46bdbc39dfac724b697/4d9692c1f3e5046cb4cd6f6275d67c6c4bc96893302439df99103f99d4ab1869/probability-8a7fc81c4c46099c41d31e98.json`

Recurrence parent post-change evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c57cd24c2e0bb5913d8007c005bdac0738f6a90c3dcc49b5dc4410bc27becf7/903c2dcfe4453b749b702ac533fbbf0a2ea76b14e9c73c9cec80e1b531a09e94/probability-1c92baf1311590250c04dfce.json`

Recurrence parent same-scenario comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f45b71ea36b4df7367e1bb10d13fe6472bc0df2a6d0b073049c109f32727e63/a667c4d366333c474db9505d1be778daec7e5630fdf23022c193feeb9e72a076/probability-2e2594e85891304baa026a5d.json`

Sponsor AI parent diagnostic: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa33ec717bf707f57688d565e00fa118951e6d82cbded06efa8afa8b1614b102/3b70efca158195ff62b13d0d9f11ca20f119c3154702d7e758e0c8f5260f9752/probability-b5163d0f1c04bd490bff6dcc.json`

Settlement deterministic review: `subagent_handoffs/settlement_set_parent_deterministic_review_2026-09-01.md`

Wars cluster deterministic review: `subagent_handoffs/cluster_clu_parent_deterministic_review_2026-09-01.md`

Map inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/651df21c50ba4a34fa23fc0dd189c218e16f4c22d48d83cb34276b86c458f3cc/f74217fcabe7a87601c15915957ad718454df5d9c98cd4bd5fc7525ac2d50b5d/map-inspect.fa76cadf611a1bf9.json`

Focus inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/216299e58f92ab3c5d3255cb2990bc2e9eb28359c80f523c83e7f044d096ddcc/1f9f19c8e338f6714ab69403327f651a105088ef4643e4735a8b86ecf629d3d7/focus-inspect.55a900cb833aadee.json`

Focus render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/934f5a1fa8f3ffefd35a0bfa747f1606ab1341c02ccaaa8c8dd7f783bfcd168e/7fb699cb574c5f7b423f0a9a751fc9f764d1df207a372ab3c049be02acc39eef/independence_wave_focus_tree.focus.json`

## Plan and handoff dispositions

| Document | Disposition | Current owner or next gate |
| --- | --- | --- |
| `docs/plans/021_random_civil_war_plans/improvement_loop_addendum.md` | Implementation findings resolved; retained as the historical acceptance crosswalk and not a second active design source | Parent closure evidence |
| `docs/plans/021_random_civil_war_plans/post_fix_improvement_loop_closure_addendum_2026-08-31.md` | Current closure plan; accepted P0/P1 work is implemented and its evidence queue remains open | Parent and specialist auditors |
| `subagent_handoffs/icon_artist_handoff.md` | Historical production snapshot with missing triplet/action blockers superseded by current runtime/GFX coverage | User live consumer review remains pending |
| `subagent_handoffs/generated_event_art_handoff.md` | Original art handoff retained; current GFX registration supersedes its parent-registration instruction | User live consumer review remains pending |
| `subagent_handoffs/ai_probability_audit.md` | Historical pre-change probability baseline; its old minimal-implementation status is superseded | Full named matrix and compare evidence |
| `subagent_handoffs/localisation_auditor.md` | Historical bounded localisation audit; source patch remains provenance and older MCP totals are superseded | Remaining target/presentation follow-ups |
| `subagent_handoffs/scripted_system_architect_handoff.md` | Complete within its bounded scripted scope; evidence snapshot is historical | Parent integration and current acceptance ledger |
| `subagent_handoffs/event_completion_auditor.md` | Superseded pre-improvement completion audit | Current acceptance evidence and final parent audit |
| `subagent_handoffs/event_completion_reaudit_final_2026-08-31.md` | Current final completion re-audit; its demonstrated duplicate Event 006 opening defect has been owner-patched | Post-patch addendum, probability certificate, and runtime acceptance |
| `subagent_handoffs/event_completion_reaudit_post_patch_addendum_2026-08-31.md` | Bounded independent verification that the duplicate Event 006 opening append is fixed in current source | Probability certificate and runtime acceptance |
| `subagent_handoffs/spreadsheet_doc_worker_handoff.md` | Current catalog handoff with intentionally non-final workbook statuses | Spreadsheet owner and user evidence |

## Contradictions and resolutions

The icon handoff's old missing `fractals_of_sovereignty` and `the_terms_hold` triplet claims are historical production blockers, not current runtime coverage blockers, because current GFX and runtime inspection resolve all 18 state files.

The icon handoff's old missing `relief_corridor` and `reconstruction` action coverage claim is historical, not current runtime status, because current GFX and runtime inspection resolve both action sprites.

The old achievement path instruction under `gfx/interface/achievements/021_random_civil_war/` conflicts with the current GFX consumer, which reads root `gfx/achievements/021_random_civil_war_*.dds`; the handoff and event docs now identify the old path as historical provenance.

The generated-art handoff's proposed category sprite name `GFX_decision_cat_picture_021_civil_war` differs from the current GFX name `GFX_decision_category_picture_021_civil_war`; the proposed block is historical and current wiring is documented separately.

The older acceptance and closure documents described the current event route as unavailable, stale, or transport-closed; those claims are superseded by the current Event 021 lint and overview artifacts, while the workspace-wide partial boundary remains explicit.

The older acceptance and closure documents said no current map artifact existed; that claim is superseded by the current map inspection, while unrelated map-position, port, and localisation diagnostics remain open outside Event 021.

The older focus scan-byte-limit claim is superseded by the current focus inspection and render; the one remaining focus warning is a vanilla continuous-focus localisation warning outside Event 021.

The shared Event Details GUI disposition is closed for Event 021. Current MCP inspection and rendering show that the reported checkbox overlap belongs to mutually exclusive visual variants, so Event 021 must not add a custom GUI or patch the shared window for that finding.

## Stale prompts and instructions

The original icon handoff's explicit interface-achievement path is stale for current consumer wiring but is preserved as historical provenance in the handoff.

The generated-art handoff's ready-to-copy category sprite name is stale for current GFX wiring but is preserved as a historical proposal.

The requested `021_random_civil_war_spec_part_9_assets_achievements_testing_acceptance.md` filename is not present; the matching `021_random_civil_war_spec_part_9_presentation_assets_achievements.md` file was used and the filename discrepancy remains recorded.

The asset-owner documents `docs/assets/021_random_civil_war/manifest.md` and `gfx_handoff.md` now mark the root achievement paths and `interface/021_random_civil_war.gfx` as authoritative; older path language is historical provenance only.

No current gameplay prompt, accepted spec, or plan was silently rewritten into a new design.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wraps were found in the scoped Event 021 event and plan Markdown files on 2026-08-31.

Headings, list items, table rows, block quotes, code blocks, and deliberate paragraph boundaries were preserved.

## Recommended parent decisions

Complete the remaining named TGT, ARC, SEV, EVO, SPN, STR, REC, GLB, and SCN weighted matrix and same-scenario comparisons when the dedicated weighted-logic route can return durable reports. SET, FRT, and CLU have current deterministic parent reviews. The FRT source implementation now includes a complete Event 006 package as an additional Evolution I front with separate rollback, lifecycle, and cleanup; its mapped runtime lifecycle fixtures remain pending.

Run the named runtime acceptance fixtures for scheduler, cluster, depot, rail, settlement, recurrence, maximum-generation, and annex-cleanup behavior.

Retain the closed shared Event Details disposition: the checked and unchecked variants are mutually exclusive, and no Event 021-owned patch is required.

Retain the reconciled asset manifest and GFX handoff as the authoritative asset-owner record unless runtime wiring changes.

Keep Event 021 and SCN-018 workbook statuses non-final until the spreadsheet owner receives current audit and user consumer evidence.

Do not mark Event 021 complete from the focused lint, targeted weighted inspections, map inspection, or asset/GFX resolution alone.

## 2026-09-02 supersession addendum

The current narrow Event 021 lint is the `d9bc467fb6be` artifact recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`; the older rows above remain historical MCP evidence.

The current target-pool projection was inspected, evaluated, and compared through `hoi4.probability_*` under the same ten named scenarios; its three artifacts are recorded in the acceptance ledger, while the live country-registry matrix and remaining weighted families remain uncertified.

The authoritative workbook was reopened and exported with 166 Event rows, 20 Cluster rows, and 16 Scenario rows including headers; current export hashes and the `spreadsheet_alignment_2026-09-02.md` handoff are authoritative.

## 2026-09-13 current test-entry tranche

The rework implementation phase is complete for test entry, and Event 021 plus SCN-018 are intentionally marked `Needs Testing`; this status is not a final acceptance claim.

The test-release gate is open through `random_civil_war_rework_ready`, while the existing final acceptance boundary remains separate and unresolved.

The latest parent source hashes are `events/021_random_civil_war.txt` `78d8eb2bb5e3cbb0a5e113789df73d03690b7fd895d1fe58bda43f8e72e33bd8`, `common/scripted_effects/021_random_civil_war_parent_effects.txt` `a007b3b87e582e2fb1c3383d8a1a74940a90b47b60f9465bcf822895c70db95a`, `common/scripted_effects/021_random_civil_war_effects.txt` `a70c458b96b2796de57657e852466dd86c72b809b2dab2b6f449fc7e5aa56b62`, `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` `019dfa864dfab233d8e760017ce243251264d1df3e252c502bf653be8697f670`, `common/scripted_triggers/021_random_civil_war_triggers.txt` `781e383f6a4e9a085c7a44ac42366e2687d8c98218cd6780c15e6306911a0391`, and `common/script_constants/021_random_civil_war_constants.txt` `d6c0febae3ef8fb6e734c33eb1f7e0df90437ac2af0911f7739a03f5bf3b27a8`.

The latest focused `hoi4.event_inspect` lint for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources, but validation remains false because the large workspace defers helper and lifecycle projections.

The current lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af08fe5b64e177be59e63d29a5a38f52483b94eab1068a690256eabfaa969825/5ad2fc3f58637f764706accb077d2c355f8ae4f4bcf30d8c7375b57fdf30795e/event-lint-ece7356e35dc.json` at revision `ece7356e35dcc9c2d4ab28eee66f573503821339c977879ef556cc72a00e18a`.

The latest parent-owned scenario tranche freezes the selected archetype, severity, front objective, anchor, bounded connected state set, optional ordinary secondary route, optional Event 006 secondary package, actor receipt, and scenario reservation before the immediate callback consumes the plan.

The latest bounded scheduler tranche separates Critical admission and launch budgets and revalidates the Critical pressure band at launch; no whole-world Event 021 review loop was added.

Maintained Event 006 allocator, country API, flag-family, and SCN-008 audits pass on the current checkout with 149 publishers, 242 broad tags, 191 resolved carriers, 102 complete flag families, and 32 static scenario cells plus eight edge cases.

The independent current completion, probability, and improvement-loop sidecars remain in progress or pending durable handoff at the time of this update.

Open acceptance gates remain live game validation, full current probability evaluation and comparison, helper-expanded lifecycle evidence, exact Event 006 package reachability and asset provenance, runtime scenario and scheduler sequences, and the shared individual-crisis fixed-target provider contract recorded in `subagent_handoffs/individual_crisis_fixed_target_contract_2026-09-13.md`.

No seven-day deterministic setup fallback was introduced because no measured one-frame performance failure has been recorded.

The improvement-loop convergence addendum `critical_launch_convergence_addendum_2026-09-13.md` is accepted and queued for post-test repair of the due-review-to-Critical-queue handoff; it is not promoted into the current test-entry source.
Its GLB and REC fixtures, current-source recheck, and lifecycle evidence remain pending, while the September 13 release status remains `Needs Testing` rather than final acceptance.
