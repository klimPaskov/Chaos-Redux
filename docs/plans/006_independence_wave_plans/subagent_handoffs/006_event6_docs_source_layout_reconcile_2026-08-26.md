# Event 006 documentation source-layout reconciliation

Date: 2026-08-26

Owner: `chaosx_documentation_curator`

Status: Documentation reconciliation complete for the bounded map/resume scope; gameplay, localisation, assets, workbook, CSV, and historical evidence remain unchanged.

## Scope

This pass reconciled only the current-facing Event 006 source-of-truth map, resume packet, and their handoff index against the current working tree, `HEAD`, the current3 completion audit, the accepted quality notes, and the current Event 006 source entrypoints.

The accepted seven-part specification remains design authority, while the source-of-truth map and resume packet remain implementation-routing authority for the partial current state.

No dated evidence body was rewritten, no gameplay or localisation file was edited, and no workbook or export CSV was opened for modification.

## Current source-of-truth map

| Surface | Current authority | Disposition |
| --- | --- | --- |
| Accepted Event 006 design | `docs/specs/006_independence_wave_specs/` and its seven specification parts | Active design authority; not rewritten to fit partial implementation. |
| Current implementation ledger | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Updated with the startup-recruitment source-layout blocker and current bounded handoffs. |
| Resume routing | `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Updated with the same blocker and current bounded handoffs. |
| Event entrypoints | `events/006_independence_wave.txt` and the current support-event registry | Source evidence; hidden `.3` cleanup, empty `.10` checkpoint, and checkpoint-driven `.350` remain distinct. |
| Startup recruitment candidate | `history/general/006_independence_wave_character_recruitment_registry.txt` | Untracked working-tree candidate only; not promoted to committed source authority. |
| Startup recruitment at `HEAD` | `history/general/006_independence_wave_character_recruitment.txt` and `history/general/006_independence_wave_additional_character_recruitment.txt` | Dated `HEAD` provenance only because both paths are deleted in the current working tree. |

The current operational boundary remains 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows.

The eight adapter-only rows remain IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM, all fail-closed.

The active automatic ladder remains `3/4/5/7/10`, with World Collapse also targeting `10`.

The no-pre-event closure remains explicit: nothing is visible before Event 006 fires, the public report is committed-only, and the retired crisis helpers remain inert compatibility surfaces without a pressure category, mission, cost, queue, history row, or early request.

## Startup-recruitment relocation reconciliation

The current working tree contains `history/general/006_independence_wave_character_recruitment_registry.txt` as an untracked candidate that combines the two startup files present at `HEAD`, `history/general/006_independence_wave_character_recruitment.txt` and `history/general/006_independence_wave_additional_character_recruitment.txt`.

Both former startup paths are deleted in the working tree but remain available at `HEAD`, so the relocation is a pending parent source-layout decision rather than a completed promotion.

A read-only structural comparison found 108 structural lines and 55 `recruit_character` calls in the candidate and in the combined `HEAD` inputs, and the candidate intentionally contains no FER record.

The structural match is evidence of the candidate's scope, not an approval of its load order, parser status, or package admission.

Current source inspection shows that `chaosx.nr6.10` is a hidden trigger-only event with an empty immediate block, while `chaosx.nr6.350` invokes `independence_wave_apply_roster_checkpoint`.

The current Event 006 event file contains no `recruit_character` calls, and all current working-tree Event 006 startup calls are in the candidate history registry.

Until the parent promotes or rejects the candidate, the former paths must be cited only as dated `HEAD` provenance and the registry must be cited only as an uncommitted working-tree candidate.

The candidate also excludes FER, while the dated IW-057 addendum still proposes adding FER to the former additional startup file; this remains a parent decision and a package-local admission blocker.

This relocation status does not alter the no-pre-event invariant, the 32/29/40/161 boundary, the eight adapter-only rows, or the `3/4/5/7/10` ladder.

## Authorities promoted, superseded, or left unchanged

| Document or evidence | Disposition | Reason |
| --- | --- | --- |
| `006_source_of_truth_map.md` | Promoted as current implementation map for this pass | It now distinguishes committed `HEAD` provenance from the untracked startup-registry candidate and links this handoff. |
| `006_independence_wave_resume_packet.md` | Promoted as current resume routing for this pass | It carries the same boundary, no-pre-event closure, startup-path blocker, and bounded handoff references. |
| `subagent_handoffs/006_event6_docs_authority_cleanup_2026_08_26.md` | Remains current for its original cleanup scope; superseded only for startup-path status | That earlier cleanup did not include the subsequent startup-file relocation conflict. |
| `subagent_handoffs/006_event6_completion_audit_current3_2026-08-25.md` | Remains current dated whole-event audit evidence | Its 32/29/40/161 boundary, ladder, HOLD/PARTIAL disposition, and focus-closure limits remain consistent with this pass. |
| `subagent_handoffs/006_event6_cost_localisation_clarity_2026-08-26.md` | Current bounded localisation evidence, committed by `a4bbc030b` | It confirms no pre-event localisation leak and preserves cost mechanics without changing the current admission boundary. |
| `subagent_handoffs/006_iw024_banat_force_contract_prose_followup_2026-08-26.md` | Current bounded Banat prose evidence, committed by `2005d92c6` | It records p24 `industrial_security`, mask `1095`, and five pathways without changing admission or runtime behavior. |
| Dated plans, audits, and handoffs containing old arithmetic or startup paths | Left unchanged as historical evidence | Rewriting dated evidence would destroy traceability; current map/resume now identify the current authority and the unresolved relocation. |

## Plan and handoff disposition

| Plan or handoff class | Disposition | Current interpretation |
| --- | --- | --- |
| Seven accepted specification parts | Active design authority | The partial 32-package implementation must not rewrite the accepted design. |
| Prior documentation authority cleanup | Implemented for its named scope | Retains its dated evidence and remains superseded only where this pass explicitly records the later startup-path conflict. |
| Source-layout merges already recorded in the map and resume packet | Implemented or source-evidenced under their named handoffs | Current receiver paths remain authoritative where the source-layout handoff and current files agree. |
| Startup recruitment registry relocation | `QUEUED / PARENT DECISION REQUIRED` | Candidate is untracked, old `HEAD` paths are deleted in the worktree, and no committed replacement authority exists. |
| IW-057 FER startup-recruitment request | `QUEUED / BLOCKED` | The dated addendum targets the former additional file, the candidate registry excludes FER, and the identity, symbol, roster, and typed-probability gates remain open. |
| Event 006 regional docs that say `.10` recruits advisors | `STALE / UNCHANGED BY SCOPE` | Current source has an empty `.10`; parent should route a future docs-only correction if those package docs are brought into scope. |
| IW-043/IW-058 signature doc that says setup recruits selected characters | `STALE OR DESIGN-CONFLICTED / UNCHANGED BY SCOPE` | Current candidate startup history owns the fixed-tag records, while current package setup applies roster checkpoints and leader roles; parent must resolve whether the doc is historical or requires a bounded correction. |
| Historical focus-ladder statements | `HISTORICAL / LEFT UNCHANGED` | Older `6/8/10/14/20` statements remain dated evidence; current routing is `3/4/5/7/10`. |

## Contradictions

| Path | Evidence of contradiction | Resolution |
| --- | --- | --- |
| `docs/events/006_independence_wave/northern_western_europe_packages.md:85,608` versus `events/006_independence_wave.txt:125-149` | Regional prose says hidden `.10` recruits static advisors, while current `.10` is an empty immediate block and `.350` is the checkpoint event. | Recorded as stale and left unchanged because the parent limited this pass to map/resume. |
| `docs/events/006_independence_wave/systems/iw043_iw058_signature_packages.md:56,69` versus `history/general/006_independence_wave_character_recruitment_registry.txt` and `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` | The doc says records are not recruited at load and setup recruits them, while the current candidate pre-recruits fixed-tag records and package setup applies roster checkpoints and leader roles. | Recorded as unresolved design/documentation conflict; no choice was guessed. |
| `docs/plans/006_independence_wave_plans/006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md:153-155` versus the current working tree | The addendum names the deleted former additional startup file and proposes FER recruitment there, while the candidate registry excludes FER. | Kept as dated plan history and marked `QUEUED / BLOCKED`; parent decision required. |
| `docs/events/006_independence_wave/overview.md:293` versus its current authority at lines 3-5 and 318-322 | A historical paragraph says the earlier `3/4/5/7/10` ladder was superseded by `6/8/10/14/20`, while the current override and source use `3/4/5/7/10`. | Kept as historical evidence and recorded as a future current-facing docs correction; not rewritten under the map/resume-only scope. |
| Prior completion and architect handoffs versus current source | Dated handoffs describe runtime recruitment in `.10` or `.350`, while current source has no event-local `recruit_character` calls. | Dated evidence remains unchanged and the map/resume now carry the current source observation and relocation blocker. |

## Duplicate or superseded document list

- `006_event6_docs_source_layout_reconcile_2026-08-26.md` is the unique handoff for this bounded reconciliation.
- `006_event6_docs_authority_cleanup_2026_08_26.md` remains the earlier cleanup handoff and is not duplicated; this handoff supersedes only its startup-path status.
- The two former startup history files remain `HEAD` provenance and were not deleted by this documentation pass.
- The untracked startup registry is a working-tree candidate, not a promoted documentation or gameplay authority.
- Dated plans and audit handoffs retaining old ladder arithmetic or old recruitment paths remain historical evidence and were not rewritten.

## Stale prompt or instruction list

No active Event 006 prompt in `docs/specs/006_independence_wave_specs/prompts/` was found to require the deleted startup path or the superseded `6/8/10/14/20` ladder.

The dated IW-057 addendum is the actionable stale plan text because it names the former additional startup path and must remain queued until the parent decides whether FER belongs in the candidate registry.

Historical architect and audit handoffs retain old runtime-recruitment observations, but they are dated evidence rather than active instructions.

## Markdown hard-wrap audit

The two patched map/resume sections use one physical line per prose sentence and preserve headings, tables, and block quotes.

The broader named Event 006 documents contain pre-existing hard-wrapped historical prose, especially `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md` and older dated handoffs; those files were left unchanged because the parent restricted patching to the current authority map and resume packet.

No hard-wrap was introduced by this pass.

## Validation

The current source was inspected around `chaosx.nr6.1`, `.2`, `.3`, `.10`, `.350`, and `.309` in `events/006_independence_wave.txt`.

Targeted source search confirmed that current Event 006 event source contains no `recruit_character` calls and that the only current working-tree Event 006 startup calls are in `history/general/006_independence_wave_character_recruitment_registry.txt`.

A read-only structural comparison found 108 structural lines and 55 `recruit_character` calls in the candidate registry and in the concatenated `HEAD` startup files, with no FER record in the candidate.

Read-only `hoi4.event_inspect` for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with status `ok`, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, graph hash `4b0d98848c436e8f6c8363056e3ae62cfad7785e4b2f1396ac9f1439f91de8df`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d18099d6351ca0ab8560f3ee4156c6f2c322a9703cc718fbc20ffe4dd5ce9cdd/703159a2c13d5602b0b8d2e418cea8fc78a8489522c49fa4746b3bf259318617/event-lint-744cd12bca3e.json`.

Read-only `hoi4.focus_inspect` for the current national focus path returned `FOCUS_INSPECTED` with source-linked revision `3f8540dcbbcb78d13a986ae73acf6bb1b2df1e0efe28cca1b03237022e1f9e3a`, 184 focuses, 195 connectors, zero crossings, zero node intersections, and zero long connectors, but its explicit `nodeSpacing=80` request produced parameter-sensitive same-row spacing diagnostics; the existing closure handoff remains the current focus authority and was not replaced.

Targeted document search confirmed that the current map and resume packet state the 32/29/40/161 boundary, `3/4/5/7/10` ladder, no-pre-event invariant, current source-layout receivers, cost-localisation handoff, and IW-024 prose handoff.

No files were staged or committed.

## Skipped meaningful validation

No probability, GUI, or map rewrite was run because this pass made no weighted-logic, interface, map, gameplay, or localisation change; existing current3 and named bounded handoffs remain the evidence for those surfaces.

No live Hearts of Iron IV session, save/load observation, or player-owned runtime receipt was run or claimed.

No historical dated handoff was mechanically reflowed because doing so would rewrite evidence outside the parent-granted scope.

## Remaining risks and recommended parent decisions

- Decide whether to promote `history/general/006_independence_wave_character_recruitment_registry.txt` as the committed replacement for the two deleted `HEAD` startup paths or restore a different committed layout.
- Decide whether FER should be added to the startup registry candidate, remain package-local without startup recruitment, or retain its queued addendum until identity and rights gates close.
- After the source-layout decision, reconcile the stale `.10` recruitment wording in the Northern/Western package document and the CHU/ASY signature-package recruitment wording.
- Decide whether the historical ladder sentence in `docs/events/006_independence_wave/overview.md:293` should receive a superseded-authority note while preserving its dated evidence.
- Keep Event 006 at **HOLD / PARTIAL** and preserve the 32/29/40/161 boundary until package admission, probability, GUI, super-event, asset, and runtime evidence independently close.

## Parent handoff

Files changed: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`, and this handoff.

The map and resume packet now link the current cost-localisation clarity handoff and IW-024 force-contract prose handoff, restate the no-pre-event, 32/29/40/161, and `3/4/5/7/10` authorities, and mark the startup registry relocation as uncommitted and pending parent decision.

No gameplay, localisation, asset, workbook, CSV, or historical dated evidence file was changed.

No plan was marked implemented or complete by inference, and no gameplay completion claim is made.
