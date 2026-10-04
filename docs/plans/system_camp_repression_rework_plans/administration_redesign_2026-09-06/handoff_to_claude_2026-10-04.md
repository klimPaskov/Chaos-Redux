# Camps, forced labor and repression handoff to Claude

## 1. Objective and authority

The full goal is incomplete.
This workstream covers the existing camps/repression package, not implementation or live acceptance of every unrelated event 1–40.
The orchestrator owns the live game and supplies evidence; engineers must not launch HOI4 or request a restart, new save or additional logs as a default response.
The user authorizes recommended implementation choices without waiting, requires honest omissions, and requires completed changes to use the shared-tree commit workflow.

All paths below are relative to `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.
`A` means the exact directory `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/`.
`S` means `docs/specs/system_camp_repression_rework_specs/specs/`.
`Q` means `docs/testing/live_qa/20261004_camp_native_cleanup/`.
These prefix definitions apply to every suffix in this document and its inventory.

### Source of truth

- `A/accepted_implementation.md` is the accepted administration contract, including the current parent decisions and their acceptance basis.
- `S/system_camp_repression_rework_spec_part_1_core_loop.md`, `S/system_camp_repression_rework_spec_part_2_country_systems_major_powers.md`, `S/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md`, `S/system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md`, `S/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md`, `S/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md`, and `S/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md` are the older package specifications; the accepted administration contract overrides conflicting routine-purchase/UI assumptions.
- `docs/specs/system_camp_repression_rework_specs/package_index.md` and `docs/specs/system_camp_repression_rework_specs/README.md` navigate the specifications.
- `A/source_inventory.json` and `A/reconciliation.md` retain identifier-level legacy action/mission accounting.
- `A/completion.md`, `A/resume_packet.md`, `A/continuation_report_2026-10-03.md`, and `A/scoped_diff_review_2026-10-03.md` contain implementation/evidence ledgers, not independent approval.
- `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` has an older July claim of implementation completion; do not use it as acceptance of this administration goal.

### Finished-system contract

One bounded monthly processor operates over the package's registered countries/sites.
National priority, mandate and spending ceiling fund maintenance before development; one economic and one institutional slot share protected reserves.
Economic output uses surviving, supported, exclusively assigned workers and real local industry/resources/projects, retaining the 40% participating-industry, 25% national, 40% construction and 40% extraction ceilings.
Infrastructure persists after closure/reform.
Paid institutional work needs continuing authority, support and a valid site; completion grants one eligible 50–100% research bonus with one use, no repeat/category stacking and at most two awards per calendar year.
Deaths never advance work or grant research.

Detention, forced labor, penal labor and killing centers remain separate roles.
Killing-center conversion requires separate radical authority, ends productive allocation and retains population, stability, resistance, evidence and accountability consequences.
Finite custody and occupation cohorts retain original origin/root and responsible authority through one measured physical source debit/destination credit and later deaths at their actual location.
No death is restored on release/reform, inferred from a quota or attributed through a protected-group selector.
Shared Chaos Meter/Deaths accounting is called through existing APIs, not edited.

Germany has SS administration, occupied-territory persecution and Auschwitz/Mengele authority no earlier than 1943-05-30.
Japan has occupied-China labor, Pingfang, army review and evidence/outbreak risk.
The USSR has Gulag labor, paranoia/famine and finite survivor release.
Britain has domestic internment; Raj has colonial detention/labor, autonomy and negotiated release.
USA, France/Vichy, Italy and Belgium/Congo retain their separate paths.

The existing `repression_ledger_window`, decision-category entry and 900×540 native layout have Administration, Locations and Records.
Actions are contextual, quotes/requirements/reasons/consequences belong in tooltips, every control/text/list/state is native, monthly work is quiet and notifications are material crises/exposure/reform/aftermath only.
Required visual acceptance includes valid populated vanilla references and matched current views/pickers at 1280×720, 1920×1080 and 125% scale across hover/selected/disabled/shortage/empty/full/long-name/large-number/scroll fixtures.

### Explicit decisions

- Germany retains one paid exact living-cohort national transfer order, selecting the oldest eligible source, revalidating and paying only on acceptance.
- Soviet military-release national relief occurs only on the first measured positive successful order; later paid orders release survivors without repeating it.
- Unlabelled outside loss at a mixed-origin host pauses origin-specific actions until a legitimate complete labelled receipt restores provenance; no proportional/newest/unknown-pool fallback is approved.
- Soviet famine shortage gets explicit no-resource responses with famine/corruption penalties; no debt.
- Current parent acceptance covers unrecorded pre-administration closure with zero recorded survivor claim, and finite Riga/Salonika source anchors within unchanged national ceilings; these are current authorized parent choices, not invented earlier human replies.
- Automatic Mengele reports are evidence-only; monthly custody mortality owns harm.
- Three duplicate foreign-subject purchases are retired after administration; no fabricated foreign transport replaces them.
- An immutable original-authority known-site archive is required for closed uncertain Records/Locations/reform checks, with one archive-only bootstrap through existing startup migration and no new recurring world hook.

## 2. Committed state and verification

Two commits belong to this continuation:

| Commit | Exact scope |
| --- | --- |
| `888e5045359e16e2a8616de3ed8ba576f2dbbe2d` | Two reusable skill insertions for real production action-contract tests and MCP transport/task recovery, plus `A/skill_workflow_handoff_2026-10-03.md`. Other skill hunks were preserved. |
| `1e77a17b994df96e8b5639fdff459688f7734c07` | Native-cleanup repair: complete passive origin effects/triggers/constants library and paired doc; exactly three missing row-consumer definitions and required constants; guarded national economy-modifier removal; one harness primitive correction; `Q/repair.md`, `Q/commit_boundary_review.md`, `Q/source_results.json`. |

The second commit is **not the complete camps integration**.
The origin files were untracked, so adding them alone would create undefined scripted callees/constants.
The isolated commit includes `camp_admin_consume_rows`, `camp_admin_consume_outside_rows`, `camp_occ_distribute_known_origin_removal`, file constants release=2/outside=3, `camp_occ_value.row_first_id=1`, and active/released row-status enums.
Existing HEAD callbacks remain unchanged except the economy-removal guard.
The broader working-tree callers, row initialization, timers, country/UI integration and terminal/projection cleanup are still outside that publication.
Claude must preserve this distinction when staging remaining work; do not assume the earlier source reports describe HEAD alone.

Supplied live QA reached the menu and reported malformed quoted localisation plus duplicate famine description, then unsupported `clear_temp_variable` and 64 missing `camp_admin_country_economy` removals during Fallout.
The current working tree uses escaped newlines and unique `soviet_gulag.2.d`/`.2.shortfall` keys.
The committed origin receipt APIs disarm mandatory value-one contract tokens to zero after success/rejection; callers overwrite snapshots before rearming, and no caller observes temporary absence.
Modifier removal checks `has_dynamic_modifier` first.
The working-tree terminal close also consumes its token with zero; the UI scratch host has no terminal clear because every iteration assigns before reading.
These latter two bodies remain part of the uncommitted integration.
No engineer-run live retest or fresh clean `error.log` is claimed.

Source verification executes production bodies with native primitives mocked.
The October 4 repair passed four targeted cases: 64 absent modifier refreshes without removal, one present removal/repeat, unarmed/stale receipt replay with fresh rearming, terminal intent followed by ordinary close, and scratch overwrite/deduplication.
Observer24, owner16, lifecycle2, projection3 and foundation35 suites passed after the cleanup repair.
The harness no longer accepts the nonexistent `clear_temp_variable` primitive.

The October 3 source audit passed foundation35, major15, institutional32, country/civil18, observer24, joined owners16, closed archive13, Records3, lifecycle2, famine17, Soviet release5, foreign retirement33 and USA7 source cases/groups.
Institution display has 11 progress, seven status, four quote and nine saved-place fixtures, plus ten contextual-tooltip branches.
The localisation audit resolves 1,213 explicit visible references across 68 scoped files; it does not prove every implicit engine consumer or native pixels.
Independent final source audit reproduced no remaining bounded gameplay defect after the three import, USA receipt and closed-archive fixes.
Those results precede later concurrent changes; rehash/rerun relevant cases rather than claiming their old identities as current.

## 3. Working-tree state and ownership

**Do not bulk-stage the shared tree.**
The exact inventory at the end of this document lists every current dirty path in the workstream-owned source/spec/plan/system/QA boundaries, including mixed files and generated artifacts.
It is a snapshot, not proof that every hunk is ours.
Some unrelated Event16/26 and orchestrator repairs share the same files.
Each entry has a disposition/purpose classification; review the actual index and HEAD delta before committing, finishing or dropping it.

### Source changes remaining beyond the two commits

| Exact files/family | Disposition and purpose |
| --- | --- |
| `common/scripted_effects/camp_administration_effects.txt`, `camp_administration_effects.md`; `common/scripted_triggers/camp_administration_triggers.txt` | Source implemented, integration/engine acceptance incomplete: finite row initialization/admission/death/release, known-receipt hooks, persistent infrastructure/civilian replacement, alignment/reform union and known-site archive. Retain the committed modifier guard and API definitions. |
| `common/scripted_effects/camp_administration_occupation_effects.txt`, paired `.md`; `common/scripted_triggers/camp_administration_occupation_triggers.txt`; occupation constants | Source implemented, historical/native acceptance partial: sparse origin rows, measured cross-state movement/custody bind/inverse quarantine, oldest-source manual order, Łódź route and finite geographical anchors. Preserve committed row-consumer/enum support. Generic occupation-to-occupation movement has no approved production caller. |
| `common/scripted_effects/camp_administration_country_effects.txt`, paired `.md`, census effects; country triggers/constants/decisions | Source implemented, engine/AI acceptance incomplete: exact selected programme/site gate, paid work and final award limits, deferred engineer receipt, first/repeat release policy and exact stock/PP authorization. |
| `common/scripted_effects/camp_administration_civil_effects.txt`, paired `.md`; civil triggers | Source implemented, engine/AI acceptance incomplete: British/Raj/USA/FRA-VIC/ITA/BEL-COG authority, paid review/claims/release and full custody/occupation/known-site reform preflight. |
| Integration effects/triggers and paired `.md`; `events/camp_administration_country_events.txt`; dispatch constants | Source implemented, native scheduling incomplete: calendar guard and eligible-country hidden 28-day timer, existing registry adapters, CXT contract, terminal cleanup, known-site bootstrap and records-only open. No new recurring world scan. |
| UI effects/triggers, paired `.md`, country/UI scripted localisation, `interface/camp_repression_ledger.gui`, `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, UI constants and English files | Source implemented, visual acceptance incomplete: native three views, locked/active controls, known-site list, cause-separated Records, actual progress/status/place, contextual costs and metadata-only action rejection. UI scratch cleanup is repaired in working tree and unpublished. |
| Repression generic/major/colonial decisions, dispatcher, major/colonial/rework effects, rework triggers/constants and English files | Source implemented, mission/native/AI acceptance incomplete: legacy cutover, shared quotes/actions, refund/success receipt paths, closure/cancel/retry and consequence projection. |
| `events/soviet_gulag.txt`; major effects/dispatcher/rework triggers; matching locale | Source implemented: exact funded/shortfall/ongoing/eased option partition, stale refund and real cooldown mapper. Native resource consumption, mission ordering and AI remain unproved. |
| `common/decisions/germany_mengele_decisions.txt`; `common/scripted_effects/germany_mengele_effects.txt`, paired `.md`; related genocide crisis decisions/effects/triggers/constants | Camp-owned source implemented: reports submit no extra deaths, three import purchases inert/refunding, exact national transfer retained and routine harm purchases retired. **Mixed ownership:** preserve clone/Black Friday output/achievement inputs and current orchestrator target-cancel fixes. Do not add the whole effects file. |
| `common/ideas/germany_mengele_ideas.txt`, `localisation/english/germany_mengele_l_english.yml` | Mixed older camp/other Event16 work: camp research/free-manpower removal or consequence text must be separated from independent cloning routes. Authorship of every current hunk is not established by this handoff. |
| `common/dynamic_modifiers/camp_repression_italy_security_dynamic_modifiers.txt` | Source implemented, limited modifier/probability evidence: Italy security sweep uses its own carrier; consult its handoffs before staging. |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | Mixed file: only UWR camp aftermath receipt/target gating belongs here; unrelated collapse work is another owner. See `A/uwr_aftermath_receipt_handoff_2026-09-27.md`. |
| Modified spec parts3/5 and `docs/systems/cbrn_warfare/genocide/genocide_crisis_system.md` | Documentation reconciliation, source facts partially verified. Keep accepted decisions separate from proposals and standalone CBRN implementation. |
| Two dirty skill files | Committed reusable paragraphs coexist with earlier uncommitted fractional-quote/finite-release and probability-schema edits. Review hunks; do not recommit others' work as this QA fix. |

No source change is intentionally abandoned.
Unaccepted historical-route proposals and invalid render fixtures are not implementations.
The duplicated `A/mcp/after/gui351_current_matrix/` artifact copy is superseded diagnostic material, excluded from eventual staging; an earlier deletion was rejected, so it was preserved.
The full plan folder includes archived before snapshots, scripts, partial MCP results and references; their presence is evidence/provenance, not completion.
`Q/before/` and `Q/source_tests.py` are uncommitted repair snapshots/fixture code.
`Q/repair.md` explicitly qualifies publication versus working-tree integration.

## 4. Priority queue and acceptance checks

1. **Live-QA repair acceptance and source publication boundary.** Read `Q/repair.md` and `Q/commit_boundary_review.md`; preserve commit `1e77a17b...`. The orchestrator must supply current outcomes for receipt cleanup and 64-repeat modifier spam. Check actual origin receipts consume tokens without replay and economy modifier adds/removes safely; no fresh clean log is established here. Decide publication of the remaining terminal/UI/source integration only after hunk/dependency review.
2. **Publish the remaining coherent source tranche.** Use `A/scoped_diff_review_2026-10-03.md` and the inventory below. In particular join foundation rows, origin consumers, occupation rows, country/civil receivers, integration timer and known-site bootstrap. Require no missing scripted callee/constant, no duplicate definitions, current relevant source suites and preserved other staged hunks. Do not confuse passive library publication with an activated monthly pipeline.
3. **Finish GUI acceptance.** Exact consumers: `repression_ledger_window`, `camp_admin_*` native controls in the `.gui`, scripted-GUI, UI effects/triggers and localisation files listed above. Use `A/references/postqualified_2026-09-27/provenance_handoff.md`, `A/references/native_element_mapping.md`, `A/mcp/origin_pause_gui_2026-10-03/review.md`. Render valid mutually exclusive panels, current archived closed/uncertain and healthy zero-live states, all pickers and required states/scales. Inspect pixels and click regions, fix every actual defect, retain matched before/after source/scenario hashes. Font advances105–215px in388px are not image acceptance. Original reference-before-initial-edit ordering was missed; do not retroactively claim it.
4. **Native transaction/timer proof.** Exact API owners: `camp_admin_record_deaths`, `camp_admin_release_detainees`, occupation transfer/bind/inverse helpers, `camp_origin_adjust_known_receipt`, `camp_admin_monthly_state`, `camp_administration_country.1/.2`, `camp_admin_integration_monthly_country_recipient`. Require one physical debit/credit, one accepted Deaths receipt, original responsibility, survivor release without new population, reserves/no double payment, calendar replay protection, research category/year limits and save persistence. Test empty/small/developed/overstretched/shortage/capture/annexation/reform/twelve-month cases using orchestrator evidence.
5. **Legitimate labelled restoration provider.** `camp_administration_origin_effects/triggers` intentionally never clears mixed ambiguity on growth, closure, arbitrary credits, structural repair or engineer release. No complete production provider exists. Specify a real caller and complete source-labelled cohort/physical receipt contract before implementing recovery; do not fabricate an API/button merely to clear a flag or modify shared Deaths attribution.
6. **Historical coverage and calibration.** Read `A/occupation/historical_benchmark_2026-09-25.md`, `A/historical_campaign_expansion_addendum_2026-09-26.md`, dated Europe/Japan sensitivity and geographical allocation files. Current thirteen-state Europe subtotal is partial, the Danish no-rescue scenario is rejected, Hungary/other-center routes are proposals, and the generic movement helper has no production caller. Validate real dated controllers, source populations, documented living movement/rescue and destination deaths; keep China's combined occupation losses separate from Pingfang. Do not tune toward six million or fill missing cohorts from casualty quotas.
7. **Final AI audits.** Use `hoi4.probability_inspect` before weighted changes and exact same pools/scenarios for evaluate/sweep/compare; include uniform native target selection. `A/ai_evidence/soviet_famine_shortfall_probability_2026-10-03.md` is partial: complete local3→5/4→6 option pools, decision raw40/incomplete category, unresolved stock/mission/scopes and an invalid-GER probability1/false eligibility/weight0 anomaly. `A/occupation/mengele_foreign_purchase_retirement_2026-10-03/mengele_import_ai_handoff.md` has no baseline analysis. Country/USA evidence under `A/ai_evidence/origin_country_civil_2026-10-03/` has Transport closed. `direct_random` in installed3.6 represents `random { chance=... }`, not `random_scope_in_array`; do not claim a two-state diagnostic exact native selection probability.
8. **Reconcile final docs/catalog/audits and commit.** Rehash source before trusting owner manifests. `A/current_completion_audit_2026-10-03.md`, `A/current_country_audit_2026-10-03.md`, `A/current_localisation_audit_2026-10-03.md` exist. The final decision/mission and cumulative origin AI handoffs were requested but their named files were absent at this handoff inspection; do not invent completed results. Resolve the Event22 catalog identity in its separate workstream before any workbook change. Only the `.xlsx` is editable, followed by `.tools/export_event_catalog_csv.py`. Commit only reviewed completed tranches through isolated-index/CAS publication.

## 5. Known limits, defects and design debt

- Full goal and clean live log acceptance remain incomplete despite passing source tests.
- Working-tree terminal/projection fixes and test assertions belong to unpublished integration; the passive QA commit deliberately does not activate them on HEAD.
- `A/continuation_report_2026-10-03.md` and older ledgers can say no package source commit or tool absence; qualify them with the October4 passive publication and healthy reference routes. Do not silently relabel old snapshots as current.
- Closed custody-only uncertainty formerly disappeared after unregister and falsely permitted reform. The known-site archive source fix and13 cases resolve that issue; its deceased-country setter and native>1000 iterator behavior remain unobserved.
- A zero-live closed history formerly showed a false warning after unrelated loss. The source predicate fix preserves sticky/structural reasons and strict action freshness; it is not an attribution recovery.
- Native USA release uses20PP/180support and success-only150-day scripted cooldown; stale orders refund PP and spend no support. Reach is derived active-site count, so descriptions do not promise lasting reach reduction. Legacy GUI compatibility executors have no current caller; current button2 dispatches `camp_admin_ui_action_two` civil review.
- Soviet relief uses30PP/120motorized/18trains/180support, one180-day mission and150-day success flag. A later fully paid retry after timeout is accepted; no free relief/duplicate mission. First Soviet positive prisoner settlement can occur for one survivor, by explicit acceptance; repeat policy relief is forbidden.
- Foreign purchases are retired IDs `import_subjects_from_japanese_china`, `_india`, `_africa`; stale native80/75/75 refunds are trusted already-charged completion callbacks. Direct import helpers grant nothing. State and country `camp_admin_initialized` are different flags; model them separately.
- A future redesign should prioritize genuine receipt provenance and complete native scenario inputs over more tuning/expansion. Source-only arithmetic, capped material history, partial candidate pools and manually forced visibility cannot prove the requested historical/AI/UI behavior.

## 6. Reproduction tools and flakiness

From the mod root, meaningful source runners are:

```text
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/foundation_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/major_countries_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/institutional_mortality_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/dispatch_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_famine_shortfall_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_release_integrity_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_observer_helper_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_observer_owner_integration_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_country_civil_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_closed_archive_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_parent_lifecycle_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_records_projection_source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/mengele_foreign_purchase_retirement_2026-10-03/source_tests.py
python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/usa_legacy_release_2026-10-03/usa_release_source_tests.py
python docs/testing/live_qa/20261004_camp_native_cleanup/source_tests.py
```

Some runners rewrite result JSON and capture whole-file hashes; they can fail preservation assertions after an unrelated shared edit.
Preserve original temporal freezes, review exact outside hunks and label any reconstructed comparison baseline explicitly; never weaken gameplay assertions or reset others' source.
The foreign preservation assertion was reconciled only for four exact Black Friday achievement inputs before `universal_cost_record_transaction`.
Several older test loaders mocked production selectors/cooldown mappers or nonexistent native commands; the real missing famine mapper and unsupported cleanup were repaired, and current tests must execute actual helper chains.

MCP reference_context/search/read/source_lookup were healthy on October4 for this QA repair; citation paths/spans/revisions are in `Q/repair.md`.
October3 GUI full/narrow tasks returned `INTERNAL_ERROR` or `JOB_WORKER_EXIT` with zero images, and ordinary event/tech/map/GUI routes often timed out after narrower retries.
Installed global transport was `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools/dist/bin/stdio.js` version3.6.0.
Projects checkout `C:/Users/klimp/Documents/Projects/hoi4-agent-tools` reported3.7.0 and failed startup for missing `fast-glob`; do not alter external tool packages to hide that.
SDK1.30.0 was available from that checkout's dependencies.
Verify the actual current configured process/version, schemas and task negotiation again.
`camp_famine_oct3`/`camp_origin_gui_oct3` are private-client workspaces; connected calls can return `WORKSPACE_NOT_REGISTERED` for them.
No `script_validate`, source_lookup body/keyPath or standalone Technology Tree Viewer was confirmed in the3.6 route set.

Preserve queued foreign baseline handle `mod_chaos_redux_ea3b2d67c2c0:job_7feeb5acb54a43fde08ab09950abd625fc7bd5a71590a8af5928c56c2eef60ad` and its config/evidence before retrying.
It was queued without analysis after30minutes; queued/working is not a terminal failure, and a completed task envelope can contain a tool-level error.
`A/mcp/origin_pause_gui_2026-10-03/task-preview.mjs`, its runtime/config record and review retain full/narrow GUI handles.
Functions session storage was not reliable across desktop/context interruption; durable files/IDs are authoritative.
Read actual UTF-8 bytes before treating console replacement glyphs as source corruption.

## 7. Interfaces and invariants

- Shared Deaths/population APIs remain in `common/scripted_effects/chaos_meter_effects.txt` and existing dynamic population helpers. Do not modify their accounting or invent attribution.
- Existing active registries include `global.camp_repression_active_countries`, `global.genocide_active_camp_states`, country `camp_active_site_states`, `camp_occ_states`, `camp_admin_civilian_states`. Known-site archive is separate metadata and must not retain periodic work.
- Existing startup migration and registered-country hidden timer own dispatch; no new daily/weekly/monthly all-country hook.
- Country/civil/repression GUI and native decisions share helper gates/quotes/effects. Contextual operating-site explanation is broader than proven action readiness; do not hide the records-locked reason by merging them.
- One-shot envelopes are unscoped temporary variables. Current disarming uses contract=0 and mandatory contract=1 checks, not absence. `clear_variable` remains regular-only.
- Release/reform/closure preserve deaths, original authority and history; captured/closed uncertain rows stay frozen without claimed survivors or output.
- Core event log/details, settings, diplomacy, super-events and registry frameworks are outside this task. Dirty core files and clone/Black Friday hunks are other owners.
- CXT uses the existing package extension carrier/setup contract; no periodic grants or unregistered test content.
- `common/scripted_effects/005_soviet_collapse_effects.txt` UWR adapter must grant/clean up only after its camp receipt; preserve unrelated collapse work.
- Repository skills and AGENTS require offline wiki plus installed-game documentation and scoped MCP evidence. Failed routes are blockers, not source-equivalent passes.
- Shared index may change while reading. Isolate exact owned paths/hunks; `commit-tree`, guarded `update-ref`, reconcile only affected entries. Never broad-stage/reset or remove an active lock. For a lock, verify Git processes, wait/retry and remove only a provably stale file.

## 8. Exact uncommitted-path inventory

The following inventory is generated from current `git status --porcelain=v1 -z --untracked-files=all` within the declared workstream boundaries immediately before handoff publication.
It includes every dirty source/spec/plan/system/QA path selected by those boundaries, and therefore explicitly includes uncertain mixed ownership instead of omitting it.
Paths outside these boundaries are not claimed by this workstream.
Source ownership/purpose is defined in section3; detailed plan/test/artifact dispositions are assigned by group below.
For the requested finished/half-done/abandoned classification: gameplay/UI/AI-dependent source groups are half-done as a publishable accepted tranche despite implemented bodies; snapshots/results/references/audits are finished evidence with stated limitations; proposals are half-done/unresolved design; the explicitly superseded duplicate group is abandoned diagnostic output.
`M` means dirty tracked content, `??` means untracked and any first-column status means shared-index content; preserve its exact staged state.
Generated artifacts and snapshots are finished evidence, not executable implementation or engine acceptance.
The handoff file itself is excluded because it is the only file committed by this turn.

Inventory snapshot HEAD: `7cbd3faeaf416b300a3b3b025f9bafe9af51a772`.

Entries: 1292.

### Mixed skill files

Disposition/purpose for every listed entry: committed paragraphs plus earlier uncommitted shared rules; hunk ownership must be separated.

Exact path prefix: `.agents/skills/` (expand A/Q as defined above).

```text
 M chaos-redux-decisions-missions/SKILL.md
 M chaos-redux-subagents/SKILL.md
```

### Dirty source and localisation files

Disposition/purpose for every listed entry: source implemented in shared tree; coupled publication/native/UI/AI acceptance incomplete; mixed files require hunk review.

```text
 M common/decisions/camp_administration_country_decisions.txt
 M common/decisions/camp_repression_colonial_country_decisions.txt
 M common/decisions/camp_repression_generic_decisions.txt
 M common/decisions/camp_repression_major_country_decisions.txt
 M common/decisions/genocide_crisis_decisions.txt
 M common/decisions/germany_mengele_decisions.txt
?? common/dynamic_modifiers/camp_repression_italy_security_dynamic_modifiers.txt
 M common/ideas/germany_mengele_ideas.txt
 M common/script_constants/camp_administration_constants.txt
 M common/script_constants/camp_administration_country_constants.txt
?? common/script_constants/camp_administration_dispatch_constants.txt
 M common/script_constants/camp_administration_occupation_constants.txt
 M common/script_constants/camp_administration_ui_constants.txt
 M common/script_constants/camp_repression_rework_constants.txt
 M common/script_constants/genocide_crisis_constants.txt
 M common/scripted_effects/005_soviet_collapse_effects.txt
 M common/scripted_effects/camp_administration_civil_effects.md
 M common/scripted_effects/camp_administration_civil_effects.txt
 M common/scripted_effects/camp_administration_country_census_effects.txt
 M common/scripted_effects/camp_administration_country_effects.md
 M common/scripted_effects/camp_administration_country_effects.txt
 M common/scripted_effects/camp_administration_effects.md
 M common/scripted_effects/camp_administration_effects.txt
 M common/scripted_effects/camp_administration_integration_effects.md
 M common/scripted_effects/camp_administration_integration_effects.txt
 M common/scripted_effects/camp_administration_occupation_effects.md
 M common/scripted_effects/camp_administration_occupation_effects.txt
 M common/scripted_effects/camp_administration_ui_effects.md
 M common/scripted_effects/camp_administration_ui_effects.txt
 M common/scripted_effects/camp_repression_action_dispatcher_effects.txt
 M common/scripted_effects/camp_repression_colonial_country_effects.txt
?? common/scripted_effects/camp_repression_major_country_effects.md
 M common/scripted_effects/camp_repression_major_country_effects.txt
 M common/scripted_effects/camp_repression_rework_effects.txt
 M common/scripted_effects/genocide_crisis_effects.txt
?? common/scripted_effects/germany_mengele_effects.md
 M common/scripted_effects/germany_mengele_effects.txt
 M common/scripted_guis/camp_repression_ledger_scripted_gui.txt
 M common/scripted_localisation/camp_administration_country_localisation.txt
 M common/scripted_localisation/camp_administration_ui_localisation.txt
 M common/scripted_localisation/camp_repression_ui_scripted_localisation.txt
 M common/scripted_triggers/camp_administration_civil_triggers.txt
 M common/scripted_triggers/camp_administration_country_triggers.txt
 M common/scripted_triggers/camp_administration_integration_triggers.txt
 M common/scripted_triggers/camp_administration_occupation_triggers.txt
 M common/scripted_triggers/camp_administration_triggers.txt
 M common/scripted_triggers/camp_administration_ui_triggers.txt
 M common/scripted_triggers/camp_repression_rework_triggers.txt
 M common/scripted_triggers/genocide_crisis_triggers.txt
 M events/camp_administration_country_events.txt
 M events/soviet_gulag.txt
 M interface/camp_repression_ledger.gui
 M localisation/english/camp_administration_country_l_english.yml
 M localisation/english/camp_administration_integration_l_english.yml
 M localisation/english/camp_administration_ui_l_english.yml
 M localisation/english/camp_repression_country_kits_l_english.yml
 M localisation/english/camp_repression_requirement_flags_l_english.yml
 M localisation/english/camp_repression_rework_l_english.yml
 M localisation/english/camp_repression_ui_l_english.yml
 M localisation/english/germany_mengele_l_english.yml
```

### Administration plans, audits and test scripts/results

Disposition/purpose for every listed entry: finished source/documentation evidence or queued requirement as named; package incomplete.

Exact path prefix: `A/` (expand A/Q as defined above).

```text
 M accepted_implementation.md
 M ai_audit.md
?? ai_probability_handoff_2026-09-25.md
?? camp_documentation_oct3_reconcile.md
?? catalog_fact_check_2026-09-27.md
?? catalog_id22_reconciliation_2026-09-27.md
 M civil_scenario_results.json
 M civil_scenarios.py
?? colocated_custody_receipt_skill_handoff_2026-09-27.md
?? completion.md
?? continuation_report_2026-10-03.md
?? current_completion_audit_2026-10-03.md
?? current_country_audit_2026-10-03.md
?? current_institution_projection_source_results_2026-10-03.json
?? current_institution_projection_source_tests_2026-10-03.py
?? current_localisation_audit_2026-10-03.md
?? current_localisation_getter_fixtures_2026-10-03.json
?? current_usa_localisation_coverage_2026-10-03.json
?? decision_cutover_handoff_2026-09-25.md
?? dispatch_source_tests.py
?? documentation_cleanup_handoff.md
?? documentation_consistency_2026-09-27.md
 M foundation_handoff.md
 M foundation_source_tests.py
 M foundation_test_results.json
?? generic_activation_exact_cost_2026-09-27.md
?? generic_reform_preflight_handoff_2026-09-26.md
?? genocide_crisis_dispositions_handoff_2026-09-25.md
?? gui_state_effect_contract_skill_handoff_2026-09-27.md
?? handoff_prompt_2026-10-03.md
?? implementation_execution_2026-09-25.md
?? institutional_mortality_mcp_audit_2026-09-27.md
?? institutional_mortality_source_results.json
?? institutional_mortality_source_tests.py
 M integration_handoff.md
?? italy_security_modifier_source_tests.py
?? italy_security_sweep_reconciliation_2026-09-27.md
?? legacy_dismantlement_cutover_handoff_2026-09-27.md
?? legacy_failure_recovery_plan_2026-09-27.md
 M major_countries_source_results.json
 M major_countries_source_tests.py
?? pre_administration_custody_disposition_2026-09-27.md
 M reconciliation.md
?? resume_packet.md
?? scoped_diff_review_2026-09-27.md
?? scoped_diff_review_2026-10-03.md
?? selected_release_row_integrity_2026-09-27.md
 M source_inventory.json
?? soviet_famine_cutover_handoff_2026-09-26.md
?? soviet_famine_shortfall_decision_audit_2026-10-03.md
?? soviet_famine_shortfall_implementation_2026-10-03.md
?? soviet_famine_shortfall_localisation_2026-10-03.md
?? soviet_famine_shortfall_source_results.json
?? soviet_famine_shortfall_source_tests.py
?? soviet_famine_terminal_scenarios.py
?? soviet_release_integrity_2026-09-27.md
?? soviet_release_integrity_source_results.json
?? soviet_release_integrity_source_tests.py
?? usa_legacy_release_2026-10-03/handoff.md
?? usa_legacy_release_2026-10-03/source_before/common__decisions__camp_repression_colonial_country_decisions.txt
?? usa_legacy_release_2026-10-03/source_before/common__scripted_effects__camp_repression_action_dispatcher_effects.txt
?? usa_legacy_release_2026-10-03/source_before/common__scripted_effects__camp_repression_colonial_country_effects.txt
?? usa_legacy_release_2026-10-03/source_before/common__scripted_effects__camp_repression_rework_effects.txt
?? usa_legacy_release_2026-10-03/source_before/common__scripted_triggers__camp_repression_rework_triggers.txt
?? usa_legacy_release_2026-10-03/source_before/localisation__english__camp_repression_rework_l_english.yml
?? usa_legacy_release_2026-10-03/source_before/manifest.csv
?? usa_legacy_release_2026-10-03/usa_release_source_scenarios.json
?? usa_legacy_release_2026-10-03/usa_release_source_test_result.json
?? usa_legacy_release_2026-10-03/usa_release_source_tests.py
?? uwr_aftermath_receipt_handoff_2026-09-27.md
?? uwr_aftermath_receipt_source_tests.py
```

### Probability evidence and immutable source fixtures

Disposition/purpose for every listed entry: partial/blocked AI audit evidence; not exact probability or engine proof.

Exact path prefix: `A/ai_evidence/` (expand A/Q as defined above).

```text
?? camp_repression_major_country_decisions_pre_sov_famine_2026-09-26.txt
?? generic_activation_cap_order_2026-09-27.md
?? generic_activation_decisions_before_2026-09-27.txt
?? generic_activation_effects_before_2026-09-27.txt
?? generic_activation_exact_cost_probability_2026-09-27.md
?? generic_activation_triggers_before_2026-09-27.txt
?? generic_activation_weight_order_before_2026-09-27.txt
?? generic_reform_preflight_probability_2026-09-26.json
?? generic_reform_preflight_scenarios_2026-09-26.json
?? genocide_crisis_decisions_pre_edit_2026-09-26.txt
?? ger_mengele_10_full_source_2026-09-27/hoi4-probability_evaluate.json
?? ger_mengele_10_full_source_2026-09-27/hoi4-probability_inspect.json
?? ger_mengele_10_full_source_2026-09-27/input.json
?? ger_mengele_10_full_source_2026-09-27/manifest.json
?? ger_mengele_10_full_source_2026-09-27/probability-9936a9ed103663831c7b1f97.json
?? ger_mengele_10_full_source_2026-09-27/probability-inspect-ed1c70133d90.json
?? ger_mengele_10_full_source_2026-09-27/probability-probability-9936a9ed103663831c7b1f97-matrix.png
?? ger_mengele_10_full_source_2026-09-27/probability-probability-9936a9ed103663831c7b1f97-matrix.svg
?? ger_mengele_10_full_source_2026-09-27/probability-probability-9936a9ed103663831c7b1f97-unresolved.png
?? ger_mengele_10_full_source_2026-09-27/probability-probability-9936a9ed103663831c7b1f97-unresolved.svg
?? ger_mengele_10_full_source_2026-09-27/review.md
?? ger_mengele_10_inline_2026-09-27/hoi4-probability_evaluate.json
?? ger_mengele_10_inline_2026-09-27/hoi4-probability_inspect.json
?? ger_mengele_10_inline_2026-09-27/input.json
?? ger_mengele_10_inline_2026-09-27/manifest.json
?? ger_mengele_10_inline_2026-09-27/probability-9bfc0b24a7322564d1442820.json
?? ger_mengele_10_inline_2026-09-27/probability-inspect-cb6d1efc7758.json
?? ger_mengele_10_inline_2026-09-27/probability-probability-9bfc0b24a7322564d1442820-matrix.png
?? ger_mengele_10_inline_2026-09-27/probability-probability-9bfc0b24a7322564d1442820-matrix.svg
?? ger_mengele_10_inline_2026-09-27/probability-probability-9bfc0b24a7322564d1442820-unresolved.png
?? ger_mengele_10_inline_2026-09-27/probability-probability-9bfc0b24a7322564d1442820-unresolved.svg
?? ger_mengele_10_inline_2026-09-27/review.md
?? italy_focus_reform_before_2026-09-27.txt
?? italy_focus_reform_score_2026-09-27.md
?? italy_security_decision_before_2026-09-27.txt
?? italy_security_probability_2026-09-27.md
?? origin_country_civil_2026-10-03/mcp_attempts.json
?? origin_country_civil_2026-10-03/reference_evidence.json
?? origin_country_civil_2026-10-03/sdk_schema_evidence.json
?? origin_country_civil_2026-10-03/source_lookup_usa.json
?? origin_country_civil_2026-10-03/usa_probability_scenarios.json
?? origin_country_civil_2026-10-03/usa_probability_scenarios_before_owner_metadata.json
?? origin_country_civil_2026-10-03/usa_random_selection_scenarios.json
?? origin_country_civil_2026-10-03/usa_stock_sensitivity_scenario.json
?? sov_famine_cutover_scenarios_2026-09-26.json
?? sov_release_decisions_before_row_gate_2026-09-27.txt
?? soviet_famine_shortfall_probability_2026-10-03.md
?? soviet_famine_shortfall_scenario_set_2026-10-03.json
?? soviet_famine_shortfall_sweep_scenarios_2026-10-03.json
?? transfer_availability_decisions_before_2026-09-27.txt
?? transfer_availability_probability_2026-09-27.md
?? transfer_availability_triggers_before_2026-09-27.txt
?? transfer_decision_baseline_2026-09-26.md
?? usa_sunset_mission_before_terminal_cancel_2026-09-27.txt
?? usa_sunset_terminal_probability_2026-09-27.md
?? uwr_aftercare_probability_2026-09-27.md
?? uwr_aftermath_decision_before_2026-09-27.txt
?? uwr_aftermath_probability_2026-09-27.md
?? uwr_secure_exploit_decisions_before_2026-09-27.txt
```

### MCP scripts, requests and artifacts

Disposition/purpose for every listed entry: finished or failed read-only evidence; validation incomplete, retain exact results/IDs.

Exact path prefix: `A/mcp/` (expand A/Q as defined above).

```text
?? after/admin_125_final.json
?? after/admin_125_final.png
?? after/admin_1280_final.json
?? after/admin_1280_final.png
?? after/admin_1920_final.png
?? after/admin_country_action_short_support_after_125.json
?? after/admin_country_action_short_support_after_125.svg
?? after/admin_country_action_short_support_after_125_inspect.json
?? after/admin_country_action_short_support_after_125_preview.png
?? after/admin_country_action_short_support_after_1280.json
?? after/admin_country_action_short_support_after_1280.svg
?? after/admin_country_action_short_support_after_1280_preview.png
?? after/admin_country_action_short_support_after_1920.json
?? after/admin_country_action_short_support_after_1920.svg
?? after/admin_country_action_short_support_after_1920_preview.png
?? after/admin_country_action_short_support_before_125.json
?? after/admin_country_action_two_blocked_before_125.json
?? after/admin_country_action_two_generic_blocked_after_125.json
?? after/admin_country_action_two_generic_blocked_after_125.svg
?? after/admin_country_action_two_generic_blocked_after_125_preview.png
?? after/admin_country_action_two_generic_blocked_after_1280.json
?? after/admin_country_action_two_generic_blocked_after_1280.svg
?? after/admin_country_action_two_generic_blocked_after_1280_preview.png
?? after/admin_country_action_two_generic_blocked_after_1920.json
?? after/admin_country_action_two_generic_blocked_after_1920.svg
?? after/admin_country_action_two_generic_blocked_after_1920_preview.png
?? after/admin_country_action_two_generic_blocked_before_125.json
?? after/admin_country_action_two_generic_blocked_before_125.svg
?? after/admin_country_action_two_generic_blocked_before_125_preview.png
?? after/admin_country_action_two_generic_blocked_rejected_125.json
?? after/admin_country_action_two_generic_blocked_rejected_125.svg
?? after/admin_country_action_two_generic_blocked_rejected_125_preview.png
?? after/admin_country_action_two_rows_mismatch_locked_125.json
?? after/admin_country_actions_hover_current_125.json
?? after/admin_country_actions_hover_current_125.svg
?? after/admin_country_actions_hover_current_125_preview.png
?? after/admin_country_actions_hover_current_1280.json
?? after/admin_country_actions_hover_current_1280.svg
?? after/admin_country_actions_hover_current_1280_preview.png
?? after/admin_country_actions_hover_current_1920.json
?? after/admin_country_actions_hover_current_1920.svg
?? after/admin_country_actions_hover_current_1920_preview.png
?? after/admin_current_source_125.png
?? after/admin_current_source_1280.png
?? after/admin_current_source_1920.png
?? after/admin_ger_1942_06_01_valid.json
?? after/gui351_current_contact_admin.png
?? after/gui351_current_contact_locations.png
?? after/gui351_current_contact_picker.png
?? after/gui351_current_contact_records.png
?? after/locations_125_final.json
?? after/locations_125_final.png
?? after/locations_1280_final.json
?? after/locations_1280_final.png
?? after/locations_1920_final.png
?? after/locations_authority_locked_current_1280.json
?? after/locations_authority_locked_final_1280.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-cropped.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-full.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-layout.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_125/repression_ledger_window-validation.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-cropped.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-full.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-layout.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1280/repression_ledger_window-validation.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-cropped.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-full.png
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-layout.json
?? after/locations_brandenburg_custody_locked_3_5_1/brandenburg_custody_locked_1920/repression_ledger_window-validation.json
?? after/locations_brandenburg_custody_locked_3_5_1/cases.json
?? after/locations_brandenburg_custody_locked_3_5_1/manifest.json
?? after/locations_brandenburg_custody_locked_work_hover_125.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-cropped.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-full.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-layout.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_125/repression_ledger_window-validation.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-cropped.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-full.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-layout.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1280/repression_ledger_window-validation.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-click-regions.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-cropped.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-fidelity.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-full.png
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-layout.json
?? after/locations_brandenburg_resource_locked_3_5_1/brandenburg_resource_locked_1920/repression_ledger_window-validation.json
?? after/locations_brandenburg_resource_locked_3_5_1/cases.json
?? after/locations_brandenburg_resource_locked_3_5_1/manifest.json
?? after/locations_brandenburg_resource_locked_work_hover_125.json
?? after/locations_closed_site_locked_current_125.json
?? after/locations_closed_site_locked_final_125.png
?? after/locations_current_source_125.png
?? after/locations_current_source_1280.png
?? after/locations_current_source_1920.png
?? after/locations_dismantle_125.json
?? after/locations_dismantle_1280.json
?? after/locations_dismantle_1920.json
?? after/locations_dismantle_current_125_cropped.png
?? after/locations_dismantle_current_1280_cropped.png
?? after/locations_dismantle_current_1920_cropped.png
?? after/locations_dismantle_custody_locked_125.json
?? after/locations_dismantle_custody_locked_125_cropped.png
?? after/locations_dismantle_empty_125.json
?? after/locations_dismantle_empty_125_cropped.png
?? after/locations_dismantle_empty_1280.json
?? after/locations_dismantle_empty_1280_final.json
?? after/locations_dismantle_empty_1280_final_cropped.png
?? after/locations_dismantle_empty_1920.json
?? after/locations_dismantle_empty_1920_final.json
?? after/locations_dismantle_empty_1920_final_cropped.png
?? after/locations_dismantle_hover_125.json
?? after/locations_dismantle_progress_locked_125.json
?? after/locations_dismantle_progress_locked_125_cropped.png
?? after/locations_dismantle_resources_locked_125.json
?? after/locations_dismantle_resources_locked_125_cropped.png
?? after/locations_dismantle_resources_locked_click_regions_125.png
?? after/locations_dismantle_stress_125.json
?? after/locations_dismantle_stress_125_cropped.png
?? after/locations_dismantle_stress_1280.json
?? after/locations_dismantle_stress_1280_cropped.png
?? after/locations_dismantle_stress_1920.json
?? after/locations_dismantle_stress_1920_final.json
?? after/locations_dismantle_stress_1920_final_cropped.png
?? after/locations_dismantle_targeted_click_regions_125.png
?? after/locations_dismantle_targeted_hover_125_cropped.png
?? after/locations_empty_custody_before_reason_priority_125.png
?? after/locations_empty_custody_click_regions_before_reason_priority_125.png
?? after/locations_empty_custody_click_regions_final_125.png
?? after/locations_empty_custody_locked_current_125.json
?? after/locations_empty_custody_locked_final_125.png
?? after/locations_empty_custody_work_hover_current_125.json
?? after/locations_empty_labor_1942_click_regions_125.png
?? after/locations_empty_labor_1942_current_125.json
?? after/locations_empty_labor_1942_current_125.png
?? after/locations_empty_labor_1942_current_1280.json
?? after/locations_empty_labor_1942_current_1280.png
?? after/locations_empty_labor_1942_current_1920.json
?? after/locations_empty_labor_1942_current_1920.png
?? after/locations_empty_labor_filter_hover_1942_current_125.json
?? after/locations_empty_labor_filter_hover_1942_current_125.png
?? after/locations_full_bottom_1942_click_regions_125.png
?? after/locations_full_bottom_1942_current_125.json
?? after/locations_full_bottom_1942_current_125.png
?? after/locations_full_bottom_1942_current_1280.json
?? after/locations_full_bottom_1942_current_1280.png
?? after/locations_full_bottom_1942_current_1920.json
?? after/locations_full_bottom_1942_current_1920.png
?? after/locations_ger_1936_empty_hover.json
?? after/locations_ger_1936_empty_hover.svg
?? after/locations_ger_1936_empty_hover_preview.png
?? after/locations_ger_1942_06_01_final.json
?? after/locations_ger_1942_06_01_locked_125.json
?? after/locations_ger_1942_06_01_locked_125.svg
?? after/locations_ger_1942_06_01_locked_125_preview.png
?? after/locations_ger_1942_06_01_locked_1280.json
?? after/locations_ger_1942_06_01_locked_1280.svg
?? after/locations_ger_1942_06_01_locked_1280_preview.png
?? after/locations_ger_1942_06_01_locked_1920.json
?? after/locations_ger_1942_06_01_locked_1920.svg
?? after/locations_ger_1942_06_01_locked_1920_preview.png
?? after/locations_ger_1942_stress_locked_125.json
?? after/locations_ger_1942_stress_locked_125.svg
?? after/locations_ger_1942_stress_locked_125_preview.png
?? after/locations_locked_label_current_source_1280.png
?? after/locations_locked_label_current_source_1920.png
?? after/locations_long_number_hover_click_regions_125.png
?? after/locations_long_number_hover_current_125.json
?? after/locations_long_number_hover_current_125.png
?? after/locations_long_number_hover_current_1280.json
?? after/locations_long_number_hover_current_1280.png
?? after/locations_long_number_hover_current_1920.json
?? after/locations_long_number_hover_current_1920.png
?? after/locations_mandate_locked_current_125.json
?? after/locations_mandate_locked_final_125.png
?? after/locations_purpose_locked_current_125.json
?? after/locations_purpose_locked_final_125.png
?? after/locations_release_records_locked_125.json
?? after/locations_release_records_locked_3_5_1/cases.json
?? after/locations_release_records_locked_3_5_1/manifest.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-click-regions.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-cropped.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-fidelity.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-full.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-layout.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-validation.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/request.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/result.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-click-regions.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-cropped.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-fidelity.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-full.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-layout.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-validation.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/request.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/result.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-click-regions.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-cropped.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-fidelity.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-full.png
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-layout.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-validation.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/request.json
?? after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/result.json
?? after/locations_release_valid_rows_125.json
?? after/locations_release_valid_rows_125_3_5_1/manifest.json
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-click-regions.png
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-cropped.png
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-fidelity.json
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-full.png
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-layout.json
?? after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-validation.json
?? after/locations_release_valid_rows_125_3_5_1/request.json
?? after/locations_release_valid_rows_125_3_5_1/result.json
?? after/locations_stress_current_source_125.png
?? after/locations_stress_locked_label_current_source_125.png
?? after/picker_125_final.json
?? after/picker_125_final.png
?? after/picker_1280_final.json
?? after/picker_1280_final.png
?? after/picker_1920_final.png
?? after/picker_budget_hover_click_regions_125.png
?? after/picker_budget_hover_current_125.json
?? after/picker_budget_hover_current_125.png
?? after/picker_budget_hover_current_1280.json
?? after/picker_budget_hover_current_1280.png
?? after/picker_budget_hover_current_1920.json
?? after/picker_budget_hover_current_1920.png
?? after/picker_current_source_1280.png
?? after/picker_current_source_1920.png
?? after/picker_filter_hover_click_regions_125.png
?? after/picker_filter_hover_current_125.json
?? after/picker_filter_hover_current_125.png
?? after/picker_filter_hover_current_1280.json
?? after/picker_filter_hover_current_1280.png
?? after/picker_filter_hover_current_1920.json
?? after/picker_filter_hover_current_1920.png
?? after/picker_ger_1942_06_01_valid.json
?? after/picker_ger_1944_radical_active_125.json
?? after/picker_ger_1944_radical_hover_125.json
?? after/picker_hover_manifest_2026-09-26.json
?? after/picker_locked_before_label_1280.png
?? after/picker_locked_current_source_125.png
?? after/picker_locked_current_source_1280.png
?? after/picker_locked_current_source_1920.png
?? after/picker_mandate_hover_click_regions_125.png
?? after/picker_mandate_hover_current_125.json
?? after/picker_mandate_hover_current_125.png
?? after/picker_mandate_hover_current_1280.json
?? after/picker_mandate_hover_current_1280.png
?? after/picker_mandate_hover_current_1920.json
?? after/picker_mandate_hover_current_1920.png
?? after/picker_priority_hover_click_regions_125.png
?? after/picker_priority_hover_current_125.json
?? after/picker_priority_hover_current_125.png
?? after/picker_priority_hover_current_1280.json
?? after/picker_priority_hover_current_1280.png
?? after/picker_priority_hover_current_1920.json
?? after/picker_priority_hover_current_1920.png
?? after/picker_radical_active_current_source_125.png
?? after/picker_radical_hover_current_source_125.png
?? after/records_125_final.json
?? after/records_125_final.png
?? after/records_1280_2026_09_26_current.png
?? after/records_1280_2026_09_26_current.svg
?? after/records_1280_2026_09_26_final.png
?? after/records_1280_2026_09_26_final.svg
?? after/records_1280_2026_09_26_final_tabs_crop.png
?? after/records_1280_2026_09_26_inspect.json
?? after/records_1280_2026_09_26_tabmark_after.png
?? after/records_1280_2026_09_26_tabmark_after.svg
?? after/records_1280_2026_09_26_tabmark_after_inspect.json
?? after/records_1280_final.json
?? after/records_1280_final.png
?? after/records_1920_final.png
?? after/records_1944_10_01_current_source_125.png
?? after/records_1944_10_01_current_source_1280.png
?? after/records_1944_10_01_current_source_1920.png
?? after/records_1944_10_01_rejected_global_hover_125.png
?? after/records_1944_10_01_rejected_mixed_125.png
?? after/records_1944_10_01_rejected_mixed_1280.png
?? after/records_1944_10_01_rejected_mixed_1920.png
?? after/records_1944_10_01_rejected_month_order_125.png
?? after/records_1944_10_01_rejected_month_order_1280.png
?? after/records_1944_10_01_rejected_month_order_1920.png
?? after/records_1944_10_01_rejected_wave_history_125.png
?? after/records_1944_10_01_rejected_wave_history_1280.png
?? after/records_1944_10_01_rejected_wave_history_1920.png
?? after/records_1944_10_01_source_sensitivity_125.json
?? after/records_1944_10_01_source_sensitivity_1280.json
?? after/records_1944_10_01_source_sensitivity_1920.json
?? after/records_empty_current_125.json
?? after/records_empty_current_125.png
?? after/records_empty_current_1280.json
?? after/records_empty_current_1280.png
?? after/records_empty_current_1920.json
?? after/records_empty_current_1920.png
?? after/records_full_bottom_click_regions_125.png
?? after/records_full_bottom_current_125.json
?? after/records_full_bottom_current_125.png
?? after/records_full_bottom_current_1280.json
?? after/records_full_bottom_current_1280.png
?? after/records_full_bottom_current_1920.json
?? after/records_full_bottom_current_1920.png
?? after/records_full_bottom_tab_hover_125.json
?? after/records_full_bottom_tab_hover_125.png
?? after/records_full_bottom_tab_hover_125.svg
?? after/records_full_bottom_tab_hover_1280.json
?? after/records_full_bottom_tab_hover_1280.png
?? after/records_full_bottom_tab_hover_1280.svg
?? after/records_full_bottom_tab_hover_1920.json
?? after/records_full_bottom_tab_hover_1920.png
?? after/records_full_bottom_tab_hover_1920.svg
?? after/records_ger_1942_06_01_valid.json
?? after/records_ger_institutional_1943_06_125.json
?? after/records_ger_institutional_1943_06_1280.json
?? after/records_ger_institutional_1943_06_1920.json
?? after/records_ger_institutional_3_5_1/manifest.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-click-regions.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-cropped.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-fidelity.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-full.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-layout.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/repression_ledger_window-validation.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/request.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_125/result.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-click-regions.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-cropped.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-fidelity.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-full.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-layout.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/repression_ledger_window-validation.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/request.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1280/result.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-click-regions.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-cropped.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-fidelity.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-full.png
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-layout.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/repression_ledger_window-validation.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/request.json
?? after/records_ger_institutional_3_5_1/records_ger_institutional_1943_06_1920/result.json
?? after/records_ger_institutional_3_5_1/review.md
?? after/records_ger_institutional_3_5_1/worker-0-initial-inspection.json
?? after/records_ger_institutional_3_5_1/worker-0-report.json
?? after/records_ger_institutional_3_5_1/worker-1-initial-inspection.json
?? after/records_ger_institutional_3_5_1/worker-1-report.json
?? after/selected_release_localisation_audit.json
?? after/shortage_125_final.json
?? after/shortage_125_final.png
?? after/shortage_1280_final.json
?? after/shortage_1280_final.png
?? after/shortage_1920_final.png
?? after/shortage_active_after_125.json
?? after/shortage_active_after_125.png
?? after/shortage_active_after_1280.json
?? after/shortage_active_after_1280.png
?? after/shortage_active_after_1920.json
?? after/shortage_active_after_1920.png
?? after/shortage_already_paused_after_125.json
?? after/shortage_already_paused_after_125.png
?? after/shortage_already_paused_after_1280.json
?? after/shortage_already_paused_after_1280.png
?? after/shortage_already_paused_after_1920.json
?? after/shortage_already_paused_after_1920.png
?? after/shortage_already_paused_before_125.json
?? after/shortage_already_paused_before_125.png
?? after/shortage_already_paused_click_regions_125.png
?? after/shortage_current_source_125.png
?? after/shortage_current_source_1280.png
?? after/shortage_current_source_1920.png
?? after/shortage_ger_1942_06_01_valid.json
?? before/locations_release_bad_rows_125.json
?? before/locations_release_bad_rows_3_5_1/manifest.json
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-click-regions.png
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-cropped.png
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-fidelity.json
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-full.png
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-layout.json
?? before/locations_release_bad_rows_3_5_1/repression_ledger_window-validation.json
?? before/locations_release_bad_rows_3_5_1/request.json
?? before/locations_release_bad_rows_3_5_1/result.json
?? camp_admin_reference_locations_1280.json
?? dispatch_event_3_6_0_2026-09-27/event-timing-f3299e7496fd-manifest.json
?? dispatch_event_3_6_0_2026-09-27/event-timing-f3299e7496fd.json
?? dispatch_event_3_6_0_2026-09-27/event-timing-f3299e7496fd.png
?? dispatch_event_3_6_0_2026-09-27/event-timing-f3299e7496fd.svg
?? dispatch_event_3_6_0_2026-09-27/event-trace-f3299e7496fd.json
?? dispatch_event_3_6_0_2026-09-27/game-country-event.json
?? dispatch_event_3_6_0_2026-09-27/helper-attempt.json
?? dispatch_event_3_6_0_2026-09-27/manifest.json
?? dispatch_event_3_6_0_2026-09-27/reference-context.json
?? dispatch_event_3_6_0_2026-09-27/reference-search.json
?? dispatch_event_3_6_0_2026-09-27/review.md
?? dispatch_event_3_6_0_2026-09-27/timing.json
?? dispatch_event_3_6_0_2026-09-27/tool-list.json
?? dispatch_event_3_6_0_2026-09-27/trace.json
?? dispatch_event_3_6_0_2026-09-27/wiki-event-effect.json
?? dispatch_event_3_6_0_2026-09-27/wiki-event-triggering.json
?? gui_acceptance_2026-09-25.md
?? local_reference_evidence_2026-09-26.md
?? locations_custody_locked_actions_2026-09-27.md
?? locations_dismantle_native_2026-09-27.md
?? locations_localisation_audit_2026-09-26.md
?? locations_resource_locked_actions_2026-09-27.md
?? origin_pause_gui_2026-10-03/after-inspect-error.txt
?? origin_pause_gui_2026-10-03/after-inspect-narrow-error.txt
?? origin_pause_gui_2026-10-03/after-inspect-narrow-request.json
?? origin_pause_gui_2026-10-03/after-inspect-request.json
?? origin_pause_gui_2026-10-03/after-render-1280-error.txt
?? origin_pause_gui_2026-10-03/after-render-1280-request.json
?? origin_pause_gui_2026-10-03/after-server.json
?? origin_pause_gui_2026-10-03/after-sources.json
?? origin_pause_gui_2026-10-03/before-inspect-error.txt
?? origin_pause_gui_2026-10-03/before-inspect-narrow-error.txt
?? origin_pause_gui_2026-10-03/before-inspect-narrow-request.json
?? origin_pause_gui_2026-10-03/before-inspect-request.json
?? origin_pause_gui_2026-10-03/before-render-1280-error.txt
?? origin_pause_gui_2026-10-03/before-render-1280-request.json
?? origin_pause_gui_2026-10-03/before-server.json
?? origin_pause_gui_2026-10-03/before-sources.json
?? origin_pause_gui_2026-10-03/before_camp_administration_ui_effects.txt
?? origin_pause_gui_2026-10-03/before_camp_administration_ui_l_english.yml
?? origin_pause_gui_2026-10-03/before_camp_administration_ui_localisation.txt
?? origin_pause_gui_2026-10-03/before_camp_repression_ledger.gui
?? origin_pause_gui_2026-10-03/before_camp_repression_ledger_scripted_gui.txt
?? origin_pause_gui_2026-10-03/native-inspect-request.json
?? origin_pause_gui_2026-10-03/native-inspect-result.json
?? origin_pause_gui_2026-10-03/native-inspect-status.json
?? origin_pause_gui_2026-10-03/native-inspect-task.json
?? origin_pause_gui_2026-10-03/native-narrow-inspect-request.json
?? origin_pause_gui_2026-10-03/native-narrow-inspect-result.json
?? origin_pause_gui_2026-10-03/native-narrow-inspect-status.json
?? origin_pause_gui_2026-10-03/native-narrow-inspect-task.json
?? origin_pause_gui_2026-10-03/native-narrow-render-1280-request.json
?? origin_pause_gui_2026-10-03/native-narrow-render-1280-status.json
?? origin_pause_gui_2026-10-03/native-narrow-render-1280-task.json
?? origin_pause_gui_2026-10-03/native-narrow-server.json
?? origin_pause_gui_2026-10-03/native-narrow-sources-closing.json
?? origin_pause_gui_2026-10-03/native-narrow-sources-opening.json
?? origin_pause_gui_2026-10-03/native-narrow-task-error.txt
?? origin_pause_gui_2026-10-03/native-render-1280-request.json
?? origin_pause_gui_2026-10-03/native-render-1280-status.json
?? origin_pause_gui_2026-10-03/native-render-1280-task.json
?? origin_pause_gui_2026-10-03/native-task-error.txt
?? origin_pause_gui_2026-10-03/preview.mjs
?? origin_pause_gui_2026-10-03/review.md
?? origin_pause_gui_2026-10-03/runtime.json
?? origin_pause_gui_2026-10-03/scenario.json
?? origin_pause_gui_2026-10-03/task-preview.mjs
?? origin_pause_gui_2026-10-03/task-server.json
?? origin_pause_gui_2026-10-03/task-sources-closing.json
?? origin_pause_gui_2026-10-03/task-sources-opening.json
?? repression_admin_current.png
?? repression_admin_current.svg
?? repression_records_current.png
?? repression_records_current.svg
?? soviet_famine_2026-10-03/after-array-decision-score-evaluate-task-status.json
?? soviet_famine_2026-10-03/after-array-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/after-array-decision-score-evaluate.json
?? soviet_famine_2026-10-03/after-decision-probability-inspect-task-status.json
?? soviet_famine_2026-10-03/after-decision-probability-inspect-task.json
?? soviet_famine_2026-10-03/after-decision-probability-inspect.json
?? soviet_famine_2026-10-03/after-decision-score-evaluate-resource.json
?? soviet_famine_2026-10-03/after-decision-score-evaluate-task-status.json
?? soviet_famine_2026-10-03/after-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/after-decision-score-evaluate.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-evaluate-resource.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-evaluate-task-status.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-evaluate-task.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-evaluate.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-inspect-task-status.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-inspect-task.json
?? soviet_famine_2026-10-03/after-event-crisis-probability-inspect.json
?? soviet_famine_2026-10-03/after-event-warning-probability-evaluate-resource.json
?? soviet_famine_2026-10-03/after-event-warning-probability-evaluate-task-status.json
?? soviet_famine_2026-10-03/after-event-warning-probability-evaluate-task.json
?? soviet_famine_2026-10-03/after-event-warning-probability-evaluate.json
?? soviet_famine_2026-10-03/after-event-warning-probability-inspect-task-status.json
?? soviet_famine_2026-10-03/after-event-warning-probability-inspect-task.json
?? soviet_famine_2026-10-03/after-event-warning-probability-inspect.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-1.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-2.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-3.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-4.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-5.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-6.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-7.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-8.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-artifact-9.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate-task.json
?? soviet_famine_2026-10-03/after-final-event-crisis-evaluate.json
?? soviet_famine_2026-10-03/after-final-event-warning-evaluate-artifact.json
?? soviet_famine_2026-10-03/after-final-event-warning-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/after-final-event-warning-evaluate-task.json
?? soviet_famine_2026-10-03/after-final-event-warning-evaluate.json
?? soviet_famine_2026-10-03/after_camp_repression_major_country_decisions.txt
?? soviet_famine_2026-10-03/after_camp_repression_major_country_decisions_final_2026-10-03.txt
?? soviet_famine_2026-10-03/after_soviet_gulag.txt
?? soviet_famine_2026-10-03/after_soviet_gulag_final_2026-10-03.txt
?? soviet_famine_2026-10-03/ai-modding-chance-reference-read.json
?? soviet_famine_2026-10-03/artifact-resource-templates.json
?? soviet_famine_2026-10-03/baseline-array-decision-score-evaluate-task-status.json
?? soviet_famine_2026-10-03/baseline-array-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/baseline-array-decision-score-evaluate.json
?? soviet_famine_2026-10-03/baseline-array-event-crisis-task-status.json
?? soviet_famine_2026-10-03/baseline-array-event-crisis-task.json
?? soviet_famine_2026-10-03/baseline-array-event-crisis.json
?? soviet_famine_2026-10-03/baseline-array-event-warning-task-status.json
?? soviet_famine_2026-10-03/baseline-array-event-warning-task.json
?? soviet_famine_2026-10-03/baseline-array-event-warning.json
?? soviet_famine_2026-10-03/baseline-clean-event-crisis-task-status.json
?? soviet_famine_2026-10-03/baseline-clean-event-crisis-task.json
?? soviet_famine_2026-10-03/baseline-clean-event-crisis.json
?? soviet_famine_2026-10-03/baseline-clean-event-warning-status-poll.json
?? soviet_famine_2026-10-03/baseline-clean-event-warning-task-status.json
?? soviet_famine_2026-10-03/baseline-clean-event-warning-task.json
?? soviet_famine_2026-10-03/baseline-clean-event-warning.json
?? soviet_famine_2026-10-03/baseline-clean-warning-render-task.json
?? soviet_famine_2026-10-03/baseline-clean-warning-render.json
?? soviet_famine_2026-10-03/baseline-decision-inspect-task-status.json
?? soviet_famine_2026-10-03/baseline-decision-inspect-task.json
?? soviet_famine_2026-10-03/baseline-decision-probability-inspect-error.txt
?? soviet_famine_2026-10-03/baseline-decision-probability-inspect.json
?? soviet_famine_2026-10-03/baseline-decision-score-evaluate-resource.json
?? soviet_famine_2026-10-03/baseline-decision-score-evaluate-status-poll.json
?? soviet_famine_2026-10-03/baseline-decision-score-evaluate-task-status.json
?? soviet_famine_2026-10-03/baseline-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/baseline-decision-score-evaluate.json
?? soviet_famine_2026-10-03/baseline-event-crisis-probability-sweep-task.json
?? soviet_famine_2026-10-03/baseline-event-crisis-probability-sweep.json
?? soviet_famine_2026-10-03/baseline-event-warning-probability-sweep-task.json
?? soviet_famine_2026-10-03/baseline-event-warning-probability-sweep.json
?? soviet_famine_2026-10-03/baseline-probability-inspect-error.txt
?? soviet_famine_2026-10-03/baseline-probability-inspect-resource.json
?? soviet_famine_2026-10-03/baseline-probability-inspect.json
?? soviet_famine_2026-10-03/baseline-probability-task-log.json
?? soviet_famine_2026-10-03/baseline-probability-task-poll.json
?? soviet_famine_2026-10-03/baseline-probability-task-status.json
?? soviet_famine_2026-10-03/baseline-probability-task.json
?? soviet_famine_2026-10-03/before-event-crisis-probability-evaluate-resource.json
?? soviet_famine_2026-10-03/before-event-crisis-probability-evaluate-task-status.json
?? soviet_famine_2026-10-03/before-event-crisis-probability-evaluate-task.json
?? soviet_famine_2026-10-03/before-event-crisis-probability-evaluate.json
?? soviet_famine_2026-10-03/before-event-warning-probability-evaluate-resource.json
?? soviet_famine_2026-10-03/before-event-warning-probability-evaluate-task-status.json
?? soviet_famine_2026-10-03/before-event-warning-probability-evaluate-task.json
?? soviet_famine_2026-10-03/before-event-warning-probability-evaluate.json
?? soviet_famine_2026-10-03/before-event-warning-probability-resource-part-0.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-1.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-2.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-3.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-4.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-5.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-6.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-7.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-8.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-artifact-9.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/before-final-event-crisis-evaluate-task.json
?? soviet_famine_2026-10-03/before-final-event-warning-evaluate-artifact.json
?? soviet_famine_2026-10-03/before-final-event-warning-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/before-final-event-warning-evaluate-task.json
?? soviet_famine_2026-10-03/before-final-event-warning-evaluate.json
?? soviet_famine_2026-10-03/before_camp_repression_action_dispatcher_effects.txt
?? soviet_famine_2026-10-03/before_camp_repression_major_country_decisions.txt
?? soviet_famine_2026-10-03/before_camp_repression_major_country_effects.txt
?? soviet_famine_2026-10-03/before_camp_repression_rework_triggers.txt
?? soviet_famine_2026-10-03/before_soviet_gulag.txt
?? soviet_famine_2026-10-03/compare_decision_scores.mjs
?? soviet_famine_2026-10-03/compare_decision_scores_final.mjs
?? soviet_famine_2026-10-03/compare_final_event_probabilities.mjs
?? soviet_famine_2026-10-03/compare_final_event_structure.mjs
?? soviet_famine_2026-10-03/complete-event-context.json
?? soviet_famine_2026-10-03/cost-search.json
?? soviet_famine_2026-10-03/decision-modding-ai-reference-read.json
?? soviet_famine_2026-10-03/decision-score-probability-compare-task.json
?? soviet_famine_2026-10-03/decision-score-probability-compare.json
?? soviet_famine_2026-10-03/decision-score-probability-sweep-mission-alternative-blocker-task.json
?? soviet_famine_2026-10-03/decision-score-probability-sweep-mission-alternative-blocker.json
?? soviet_famine_2026-10-03/decision-score-probability-sweep-task.json
?? soviet_famine_2026-10-03/decision-score-probability-sweep.json
?? soviet_famine_2026-10-03/equipment-search.json
?? soviet_famine_2026-10-03/evaluate_array_baselines.mjs
?? soviet_famine_2026-10-03/evaluate_array_decision_scores.mjs
?? soviet_famine_2026-10-03/evaluate_clean_baselines.mjs
?? soviet_famine_2026-10-03/evaluate_decision_scores.mjs
?? soviet_famine_2026-10-03/evaluate_event_scenario_pools.mjs
?? soviet_famine_2026-10-03/evaluate_final_decision_scores.mjs
?? soviet_famine_2026-10-03/evaluate_pointer_event_pools.mjs
?? soviet_famine_2026-10-03/evaluate_scope_pointer_probe.mjs
?? soviet_famine_2026-10-03/event-context.json
?? soviet_famine_2026-10-03/exact-option-search.json
?? soviet_famine_2026-10-03/final-after-decision-probability-inspect-recovered-result.json
?? soviet_famine_2026-10-03/final-after-decision-probability-inspect-task.json
?? soviet_famine_2026-10-03/final-after-decision-probability-inspect.json
?? soviet_famine_2026-10-03/final-after-decision-score-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/final-after-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/final-after-event-crisis-probability-inspect-recovered-result.json
?? soviet_famine_2026-10-03/final-after-event-crisis-probability-inspect-task.json
?? soviet_famine_2026-10-03/final-after-event-crisis-probability-inspect.json
?? soviet_famine_2026-10-03/final-after-event-warning-probability-inspect-recovered-result.json
?? soviet_famine_2026-10-03/final-after-event-warning-probability-inspect-task.json
?? soviet_famine_2026-10-03/final-after-event-warning-probability-inspect.json
?? soviet_famine_2026-10-03/final-baseline-decision-score-evaluate-recovered-result.json
?? soviet_famine_2026-10-03/final-baseline-decision-score-evaluate-task.json
?? soviet_famine_2026-10-03/final-baseline-decision-score-evaluate.json
?? soviet_famine_2026-10-03/final-decision-before-evaluate-artifact.json
?? soviet_famine_2026-10-03/final-decision-score-compare-artifact.json
?? soviet_famine_2026-10-03/final-decision-score-probability-compare-recovered-result.json
?? soviet_famine_2026-10-03/final-decision-score-probability-compare-task.json
?? soviet_famine_2026-10-03/final-decision-score-probability-compare.json
?? soviet_famine_2026-10-03/final-decision-score-probability-sweep-famine-only-task.json
?? soviet_famine_2026-10-03/final-decision-score-probability-sweep-famine-only.json
?? soviet_famine_2026-10-03/final-decision-score-probability-sweep-task.json
?? soviet_famine_2026-10-03/final-decision-score-probability-sweep.json
?? soviet_famine_2026-10-03/final-event-crisis-options-render-recovered-result.json
?? soviet_famine_2026-10-03/final-event-crisis-options-render-task.json
?? soviet_famine_2026-10-03/final-event-crisis-options-render.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-compare-artifact.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-compare-recovered-result.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-compare-task.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-sweep-famine-only-task.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-sweep-famine-only.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-sweep-task.json
?? soviet_famine_2026-10-03/final-event-crisis-probability-sweep.json
?? soviet_famine_2026-10-03/final-event-crisis-structural-trace-recovered-result.json
?? soviet_famine_2026-10-03/final-event-crisis-structural-trace-task.json
?? soviet_famine_2026-10-03/final-event-crisis-structural-trace.json
?? soviet_famine_2026-10-03/final-event-structural-compare-recovered-result.json
?? soviet_famine_2026-10-03/final-event-structural-compare-task.json
?? soviet_famine_2026-10-03/final-event-warning-options-render-recovered-result.json
?? soviet_famine_2026-10-03/final-event-warning-options-render-task.json
?? soviet_famine_2026-10-03/final-event-warning-options-render.json
?? soviet_famine_2026-10-03/final-event-warning-probability-compare-artifact.json
?? soviet_famine_2026-10-03/final-event-warning-probability-compare-recovered-result.json
?? soviet_famine_2026-10-03/final-event-warning-probability-compare-task.json
?? soviet_famine_2026-10-03/final-event-warning-probability-compare.json
?? soviet_famine_2026-10-03/final-event-warning-probability-sweep-artifact.json
?? soviet_famine_2026-10-03/final-event-warning-probability-sweep-task.json
?? soviet_famine_2026-10-03/final-event-warning-probability-sweep.json
?? soviet_famine_2026-10-03/final-event-warning-structural-trace-recovered-result.json
?? soviet_famine_2026-10-03/final-event-warning-structural-trace-task.json
?? soviet_famine_2026-10-03/final-event-warning-structural-trace.json
?? soviet_famine_2026-10-03/inspect_active_jobs.mjs
?? soviet_famine_2026-10-03/inspect_after_surfaces.mjs
?? soviet_famine_2026-10-03/inspect_decision_baseline.mjs
?? soviet_famine_2026-10-03/inspect_final_sources.mjs
?? soviet_famine_2026-10-03/job-status-before-final-event-warning-evaluate.json
?? soviet_famine_2026-10-03/job-status-decision-score-probability-sweep.json
?? soviet_famine_2026-10-03/job-status-final-after-decision-probability-inspect.json
?? soviet_famine_2026-10-03/job-status-final-after-event-crisis-probability-inspect.json
?? soviet_famine_2026-10-03/job-status-final-after-event-warning-probability-inspect.json
?? soviet_famine_2026-10-03/job-status-final-event-crisis-options-render.json
?? soviet_famine_2026-10-03/job-status-final-event-warning-probability-compare.json
?? soviet_famine_2026-10-03/job-status-final-event-warning-structural-trace.json
?? soviet_famine_2026-10-03/local_reference_reads.json
?? soviet_famine_2026-10-03/lookup_vanilla_afg_source.mjs
?? soviet_famine_2026-10-03/option-search.json
?? soviet_famine_2026-10-03/poll_final_inspect_task.mjs
?? soviet_famine_2026-10-03/poll_final_probability_jobs.mjs
?? soviet_famine_2026-10-03/poll_probability_task.mjs
?? soviet_famine_2026-10-03/probability-runtime.json
?? soviet_famine_2026-10-03/probability-server-live.json
?? soviet_famine_2026-10-03/probability-server.json
?? soviet_famine_2026-10-03/probability-task-negotiation.json
?? soviet_famine_2026-10-03/read-costs-wiki-284.json
?? soviet_famine_2026-10-03/read-costs-wiki-387.json
?? soviet_famine_2026-10-03/read-equipment-game_doc.json
?? soviet_famine_2026-10-03/read-equipment-wiki.json
?? soviet_famine_2026-10-03/read-options-151.json
?? soviet_famine_2026-10-03/read_ai_decision_sections.mjs
?? soviet_famine_2026-10-03/read_ai_source_references.mjs
?? soviet_famine_2026-10-03/read_baseline_probability_artifact.mjs
?? soviet_famine_2026-10-03/read_decision_evaluate_artifacts.mjs
?? soviet_famine_2026-10-03/read_probability_artifact_range.mjs
?? soviet_famine_2026-10-03/read_probability_evaluate_artifacts.mjs
?? soviet_famine_2026-10-03/read_references.mjs
?? soviet_famine_2026-10-03/reference_context_decision-reference_context_decision.json
?? soviet_famine_2026-10-03/reference_read_ai_modding_chance-reference_read_ai_modding_chance.json
?? soviet_famine_2026-10-03/reference_search_ai_chance-reference_search_ai_chance.json
?? soviet_famine_2026-10-03/reference_search_decision_ai-reference_search_decision_ai.json
?? soviet_famine_2026-10-03/render-final-warning-compare.json
?? soviet_famine_2026-10-03/render_baseline_clean_warning.mjs
?? soviet_famine_2026-10-03/run_final_event_structural_review.mjs
?? soviet_famine_2026-10-03/run_probability_audit.mjs
?? soviet_famine_2026-10-03/run_probability_inspect.mjs
?? soviet_famine_2026-10-03/run_probability_task.mjs
?? soviet_famine_2026-10-03/scope-pointer-probe-task.json
?? soviet_famine_2026-10-03/scope-pointer-probe.json
?? soviet_famine_2026-10-03/server.json
?? soviet_famine_2026-10-03/sweep_baseline_event_pools.mjs
?? soviet_famine_2026-10-03/sweep_decision_score.mjs
?? soviet_famine_2026-10-03/vanilla-afg-source-lookup-error.txt
?? soviet_famine_2026-10-03/vanilla-decision-gates-reference-read.json
?? soviet_release_decision_3_6_0_2026-09-27/decision-eff82362661b7a107643e8f5.json
?? soviet_release_decision_3_6_0_2026-09-27/decision-request.json
?? soviet_release_decision_3_6_0_2026-09-27/decision-result.json
?? soviet_release_decision_3_6_0_2026-09-27/manifest.json
?? soviet_release_decision_3_6_0_2026-09-27/review.md
?? soviet_release_policy_references_3_6_0_2026-10-03/manifest.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-flag-context.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-flag-game_doc.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-flag-search.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-flag-wiki-effects.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-loc-context.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-loc-read.json
?? soviet_release_policy_references_3_6_0_2026-10-03/policy-loc-search.json
?? soviet_release_references_3_6_0_2026-09-27/installed-add-pp.json
?? soviet_release_references_3_6_0_2026-09-27/installed-all-of-scopes.json
?? soviet_release_references_3_6_0_2026-09-27/installed-decision-doc.json
?? soviet_release_references_3_6_0_2026-09-27/manifest.json
?? soviet_release_references_3_6_0_2026-09-27/reference-all-of-scopes.json
?? soviet_release_references_3_6_0_2026-09-27/reference-context.json
?? soviet_release_references_3_6_0_2026-09-27/reference-decision-cost.json
?? soviet_release_references_3_6_0_2026-09-27/reference-refund.json
?? soviet_release_references_3_6_0_2026-09-27/search-custom-tooltip.json
?? soviet_release_references_3_6_0_2026-09-27/source-lookup-vanilla.json
?? soviet_release_references_3_6_0_2026-09-27/wiki-decision-cost.json
?? technology_bonus_coverage_2026-09-25.md
?? vanilla_reference_2026-09-27/README.md
?? vanilla_reference_2026-09-27/manifest.json
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-click-regions.png
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-cropped.png
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-fidelity.json
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-full.png
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-layout.json
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/countrydecisionview-validation.json
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/request.json
?? vanilla_reference_2026-09-27/rendered/vanilla_eng_1937_worker_conditions_visible/result.json
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-click-regions.png
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-cropped.png
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-fidelity.json
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-full.png
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-layout.json
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/countryoccupationview-validation.json
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/request.json
?? vanilla_reference_2026-09-27/rendered/vanilla_ger_pol_two_state_occupation_declared/result.json
?? vanilla_reference_2026-09-27/requests/vanilla_eng_1937_worker_conditions_visible.json
?? vanilla_reference_2026-09-27/requests/vanilla_ger_pol_two_state_occupation_declared.json
```

### Superseded duplicate MCP artifact copy

Disposition/purpose for every listed entry: abandoned diagnostic copy; preserved, exclude from staging.

Exact path prefix: `A/mcp/after/gui351_current_matrix/` (expand A/Q as defined above).

```text
?? archive-manifest.json
?? cases.json
?? gui351_current_01-click-regions.png
?? gui351_current_01-crop.png
?? gui351_current_02-click-regions.png
?? gui351_current_02-crop.png
?? gui351_current_03-click-regions.png
?? gui351_current_03-crop.png
?? gui351_current_04-click-regions.png
?? gui351_current_04-crop.png
?? gui351_current_05-click-regions.png
?? gui351_current_05-crop.png
?? gui351_current_06-click-regions.png
?? gui351_current_06-crop.png
?? gui351_current_07-click-regions.png
?? gui351_current_07-crop.png
?? gui351_current_08-click-regions.png
?? gui351_current_08-crop.png
?? gui351_current_09-click-regions.png
?? gui351_current_09-crop.png
?? gui351_current_10-click-regions.png
?? gui351_current_10-crop.png
?? gui351_current_11-click-regions.png
?? gui351_current_11-crop.png
?? gui351_current_12-click-regions.png
?? gui351_current_12-crop.png
?? gui351_current_13-click-regions.png
?? gui351_current_13-crop.png
?? gui351_current_14-click-regions.png
?? gui351_current_14-crop.png
?? gui351_current_15-click-regions.png
?? gui351_current_15-crop.png
?? gui351_current_16-click-regions.png
?? gui351_current_16-crop.png
?? gui351_current_17-click-regions.png
?? gui351_current_17-crop.png
?? gui351_current_18-click-regions.png
?? gui351_current_18-crop.png
?? gui351_current_19-click-regions.png
?? gui351_current_19-crop.png
?? gui351_current_20-click-regions.png
?? gui351_current_20-crop.png
?? gui351_current_21-click-regions.png
?? gui351_current_21-crop.png
?? gui351_current_22-click-regions.png
?? gui351_current_22-crop.png
?? gui351_current_23-click-regions.png
?? gui351_current_23-crop.png
?? gui351_current_24-click-regions.png
?? gui351_current_24-crop.png
?? gui351_current_25-click-regions.png
?? gui351_current_25-crop.png
?? gui351_current_26-click-regions.png
?? gui351_current_26-crop.png
?? gui351_current_27-click-regions.png
?? gui351_current_27-crop.png
?? gui351_current_28-click-regions.png
?? gui351_current_28-crop.png
?? gui351_current_29-click-regions.png
?? gui351_current_29-crop.png
?? gui351_current_30-click-regions.png
?? gui351_current_30-crop.png
?? gui351_current_31-click-regions.png
?? gui351_current_31-crop.png
?? gui351_current_32-click-regions.png
?? gui351_current_32-crop.png
?? gui351_current_33-click-regions.png
?? gui351_current_33-crop.png
?? gui351_current_34-click-regions.png
?? gui351_current_34-crop.png
?? gui351_current_35-click-regions.png
?? gui351_current_35-crop.png
?? gui351_current_36-click-regions.png
?? gui351_current_36-crop.png
?? gui351_current_37-click-regions.png
?? gui351_current_37-crop.png
?? gui351_current_38-click-regions.png
?? gui351_current_38-crop.png
?? gui351_current_39-click-regions.png
?? gui351_current_39-crop.png
?? gui351_current_40-click-regions.png
?? gui351_current_40-crop.png
?? gui351_current_41-click-regions.png
?? gui351_current_41-crop.png
?? gui351_current_42-click-regions.png
?? gui351_current_42-crop.png
?? gui351_current_43-click-regions.png
?? gui351_current_43-crop.png
?? gui351_current_44-click-regions.png
?? gui351_current_44-crop.png
?? gui351_current_45-click-regions.png
?? gui351_current_45-crop.png
?? review-geometry-and-integrity.json
?? worker-0-report.json
?? worker-1-report.json
```

### Origin, movement and history implementation evidence

Disposition/purpose for every listed entry: source/test/handoff finished within stated scope; native/historical/AI acceptance incomplete.

Exact path prefix: `A/occupation/` (expand A/Q as defined above).

```text
 M accounting_results.json
?? cross_state_movement_handoff.md
?? custody_origin_rows_handoff.md
?? europe_origin_coverage_matrix_2026-09-26.md
?? historical_benchmark_2026-09-25.md
 M historical_envelope_results.json
?? integrate_country_provenance_sources.py
?? integrate_engineer_release_receipts.py
?? integrate_movement_origin_receipts.py
?? integrate_observer_owned_sources.py
?? integrate_terminal_origin_containment.py
?? japan_dated_control_sensitivity_2026-09-27.md
?? manual_transfer_live_availability_2026-09-27.md
?? manual_transfer_target_density_2026-09-26.md
?? mengele_adapter_mcp_2026-10-03.mjs
?? mengele_adapter_mcp_2026-10-03/after_germany_mengele_effects.txt
?? mengele_adapter_mcp_2026-10-03/event_inspect.json
?? mengele_adapter_mcp_2026-10-03/event_inspect_final_narrow-error.txt
?? mengele_adapter_mcp_2026-10-03/event_inspect_retry-error.txt
?? mengele_adapter_mcp_2026-10-03/final_owned_sources.json
?? mengele_adapter_mcp_2026-10-03/map_inspect-error.txt
?? mengele_adapter_mcp_2026-10-03/map_inspect_retry-error.txt
?? mengele_adapter_mcp_2026-10-03/reference_context.json
?? mengele_adapter_mcp_2026-10-03/reference_context_complete.json
?? mengele_adapter_mcp_2026-10-03/reference_read_loop.json
?? mengele_adapter_mcp_2026-10-03/reference_read_wiki_arrays.json
?? mengele_adapter_mcp_2026-10-03/reference_search.json
?? mengele_adapter_mcp_2026-10-03/server.json
?? mengele_adapter_mcp_2026-10-03/source_and_local_reference_evidence.json
?? mengele_adapter_mcp_2026-10-03/source_lookup-error.txt
?? mengele_adapter_mcp_2026-10-03/source_lookup_retry-error.txt
?? mengele_exact_custody_adapter_2026-10-03.md
?? mengele_foreign_purchase_retirement_2026-10-03/after_germany_mengele_decisions.txt
?? mengele_foreign_purchase_retirement_2026-10-03/after_germany_mengele_effects.txt
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/baseline_blocker.md
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_evidence.json
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_get.log
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_get.mjs
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_inspect.log
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_inspect.mjs
?? mengele_foreign_purchase_retirement_2026-10-03/ai_evidence/mengele_import_retirement_2026-10-03/native_task_inspect_current.log
?? mengele_foreign_purchase_retirement_2026-10-03/decision-inspect-error.txt
?? mengele_foreign_purchase_retirement_2026-10-03/decision-inspect-retry-error.txt
?? mengele_foreign_purchase_retirement_2026-10-03/event-inspect-error.txt
?? mengele_foreign_purchase_retirement_2026-10-03/event-inspect-retry-error.txt
?? mengele_foreign_purchase_retirement_2026-10-03/handoff.md
?? mengele_foreign_purchase_retirement_2026-10-03/inspect.mjs
?? mengele_foreign_purchase_retirement_2026-10-03/local_reference_evidence.json
?? mengele_foreign_purchase_retirement_2026-10-03/mengele_import_ai_handoff.md
?? mengele_foreign_purchase_retirement_2026-10-03/reference-context.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-read-decision-gates.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-read-wiki-cost.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-read-wiki-gates.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search-pp-read-0.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search-pp-read-1.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search-pp.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search-read-0.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search-read-1.json
?? mengele_foreign_purchase_retirement_2026-10-03/reference-search.json
?? mengele_foreign_purchase_retirement_2026-10-03/server.json
?? mengele_foreign_purchase_retirement_2026-10-03/shared_current_outside_baseline_germany_mengele_effects.txt
?? mengele_foreign_purchase_retirement_2026-10-03/shared_preservation.json
?? mengele_foreign_purchase_retirement_2026-10-03/source_results.json
?? mengele_foreign_purchase_retirement_2026-10-03/source_tests.py
?? origin_ambiguity_audit_2026-09-27.md
?? origin_ambiguity_containment_architecture_2026-10-03.md
?? origin_ambiguity_mcp_2026-10-03/bounded_inspect.mjs
?? origin_ambiguity_mcp_2026-10-03/bounded_summary.json
?? origin_ambiguity_mcp_2026-10-03/config.json
?? origin_ambiguity_mcp_2026-10-03/context.json
?? origin_ambiguity_mcp_2026-10-03/corrected_surface_inspect.mjs
?? origin_ambiguity_mcp_2026-10-03/decision.json
?? origin_ambiguity_mcp_2026-10-03/decision_with_scenario.json
?? origin_ambiguity_mcp_2026-10-03/discover.mjs
?? origin_ambiguity_mcp_2026-10-03/event-scan-fe29c3107ffb.json
?? origin_ambiguity_mcp_2026-10-03/event_artifact_retention.json
?? origin_ambiguity_mcp_2026-10-03/events.json
?? origin_ambiguity_mcp_2026-10-03/gui.json
?? origin_ambiguity_mcp_2026-10-03/gui_with_scenario.json
?? origin_ambiguity_mcp_2026-10-03/inspect.mjs
?? origin_ambiguity_mcp_2026-10-03/local_reference_evidence.json
?? origin_ambiguity_mcp_2026-10-03/map_failure.json
?? origin_ambiguity_mcp_2026-10-03/read_constants_concept.json
?? origin_ambiguity_mcp_2026-10-03/read_constants_schema.json
?? origin_ambiguity_mcp_2026-10-03/read_flag_trigger.json
?? origin_ambiguity_mcp_2026-10-03/read_flags.json
?? origin_ambiguity_mcp_2026-10-03/read_population.json
?? origin_ambiguity_mcp_2026-10-03/read_scoping.json
?? origin_ambiguity_mcp_2026-10-03/read_target_effect.json
?? origin_ambiguity_mcp_2026-10-03/read_targets.json
?? origin_ambiguity_mcp_2026-10-03/search_add_state_population.json
?? origin_ambiguity_mcp_2026-10-03/search_has_state_flag.json
?? origin_ambiguity_mcp_2026-10-03/search_save_event_target_as.json
?? origin_ambiguity_mcp_2026-10-03/search_script_constants.json
?? origin_ambiguity_mcp_2026-10-03/search_state_population_k.json
?? origin_ambiguity_mcp_2026-10-03/server_and_schemas.json
?? origin_ambiguity_mcp_2026-10-03/source_apply_exact_state_civilian_population_loss.json
?? origin_ambiguity_mcp_2026-10-03/source_camp_admin_refresh_capacity.json
?? origin_ambiguity_mcp_2026-10-03/source_camp_occ_reconcile_external_population.json
?? origin_ambiguity_mcp_2026-10-03/source_manifest.json
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__script_constants__camp_administration_constants.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__script_constants__camp_administration_occupation_constants.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_effects__camp_administration_country_effects.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_effects__camp_administration_effects.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_effects__camp_administration_integration_effects.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_effects__camp_administration_occupation_effects.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_localisation__camp_administration_ui_localisation.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_triggers__camp_administration_occupation_triggers.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_triggers__camp_administration_triggers.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_triggers__camp_administration_ui_triggers.txt
?? origin_ambiguity_mcp_2026-10-03/source_snapshots/common__scripted_triggers__camp_repression_rework_triggers.txt
?? origin_closed_archive_current_manifest.json
?? origin_closed_archive_reference_evidence.json
?? origin_closed_archive_reproduction_before.json
?? origin_closed_archive_source_results.json
?? origin_closed_archive_source_tests.py
?? origin_closed_archive_validation_runs.json
?? origin_closed_empty_warning_before.json
?? origin_closed_site_archive_integration_2026-10-03.md
?? origin_country_civil_integration_2026-10-03.md
?? origin_country_civil_integration_manifest.json
?? origin_country_civil_source_results.json
?? origin_country_civil_source_tests.py
?? origin_observer_helper_implementation_2026-10-03.md
?? origin_observer_helper_local_references.json
?? origin_observer_helper_source_manifest.json
?? origin_observer_helper_source_results.json
?? origin_observer_helper_source_tests.py
?? origin_observer_owner_foundation_results.json
?? origin_observer_owner_integration_2026-10-03.md
?? origin_observer_owner_integration_manifest.json
?? origin_observer_owner_integration_source_results.json
?? origin_observer_owner_integration_source_tests.py
?? origin_parent_lifecycle_source_results.json
?? origin_parent_lifecycle_source_tests.py
?? origin_records_projection_source_results.json
?? origin_records_projection_source_tests.py
?? staged_state_control_sensitivity_2026-09-26.md
?? supplementary_direct_control_sensitivity_2026-09-27.md
?? test_cross_state_transfer.py
?? test_custody_origin_rows.py
 M test_historical_envelopes.py
?? test_krakow_setup.py
 M test_occupation_accounting.py
?? test_occupation_custody_transfer.py
```

### Immutable origin/ledger before snapshots

Disposition/purpose for every listed entry: finished provenance snapshots; do not modify originals.

Exact path prefix: `A/occupation/` (expand A/Q as defined above).

```text
?? before_closed_archive_2026-10-03/archive_reads.mjs
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_effects.md
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_effects.txt
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_integration_effects.md
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_integration_effects.txt
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_ui_effects.md
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_administration_ui_effects.txt
?? before_closed_archive_2026-10-03/common__scripted_effects__camp_repression_rework_effects.txt
?? before_closed_archive_2026-10-03/common__scripted_triggers__camp_administration_country_triggers.txt
?? before_closed_archive_2026-10-03/common__scripted_triggers__camp_administration_integration_triggers.txt
?? before_closed_archive_2026-10-03/common__scripted_triggers__camp_administration_triggers.txt
?? before_closed_archive_2026-10-03/common__scripted_triggers__camp_administration_ui_triggers.txt
?? before_closed_archive_2026-10-03/common__scripted_triggers__camp_repression_rework_triggers.txt
?? before_closed_archive_2026-10-03/discover_installed.mjs
?? before_closed_archive_2026-10-03/domain_reads.json
?? before_closed_archive_2026-10-03/gui_archive_inspect.mjs
?? before_closed_archive_2026-10-03/gui_archive_inspect_after.mjs
?? before_closed_archive_2026-10-03/installed_server_capabilities.json
?? before_closed_archive_2026-10-03/source_manifest.json
?? before_closed_empty_warning_2026-10-03/common__scripted_effects__camp_administration_ui_effects.md
?? before_closed_empty_warning_2026-10-03/common__scripted_triggers__camp_administration_ui_triggers.txt
?? before_closed_empty_warning_2026-10-03/docs__plans__system_camp_repression_rework_plans__administration_redesign_2026-09-06__occupation__origin_closed_archive_source_tests.py
?? before_closed_empty_warning_2026-10-03/source_manifest.json
?? before_country_civil_pause_2026-10-03/AGENTS.md
?? before_country_civil_pause_2026-10-03/common__scripted_effects__camp_administration_civil_effects.md
?? before_country_civil_pause_2026-10-03/common__scripted_effects__camp_administration_civil_effects.txt
?? before_country_civil_pause_2026-10-03/common__scripted_effects__camp_administration_country_effects.md
?? before_country_civil_pause_2026-10-03/common__scripted_effects__camp_administration_country_effects.txt
?? before_country_civil_pause_2026-10-03/common__scripted_triggers__camp_administration_civil_triggers.txt
?? before_country_civil_pause_2026-10-03/common__scripted_triggers__camp_administration_country_triggers.txt
?? before_country_civil_pause_2026-10-03/discover.mjs
?? before_country_civil_pause_2026-10-03/discover_installed.mjs
?? before_country_civil_pause_2026-10-03/domain_reads.json
?? before_country_civil_pause_2026-10-03/domain_reads.mjs
?? before_country_civil_pause_2026-10-03/foundation_before_pending_helper_loader.json
?? before_country_civil_pause_2026-10-03/foundation_before_pending_helper_loader.py
?? before_country_civil_pause_2026-10-03/installed_server_capabilities.json
?? before_country_civil_pause_2026-10-03/live_schemas.json
?? before_country_civil_pause_2026-10-03/source_manifest.json
?? before_country_quote_boundary_2026-10-03/common__scripted_effects__camp_administration_country_effects.md
?? before_country_quote_boundary_2026-10-03/common__scripted_triggers__camp_administration_country_triggers.txt
?? before_country_quote_boundary_2026-10-03/docs__plans__system_camp_repression_rework_plans__administration_redesign_2026-09-06__occupation__origin_country_civil_source_tests.py
?? before_country_quote_boundary_2026-10-03/domain_reads.json
?? before_country_quote_boundary_2026-10-03/quote_boundary_evidence.json
?? before_country_quote_boundary_2026-10-03/quote_reads.mjs
?? before_country_quote_boundary_2026-10-03/source_manifest.json
?? before_parent_lifecycle_2026-10-03/camp_administration_integration_effects.txt
?? before_parent_lifecycle_2026-10-03/camp_repression_rework_effects.txt
?? before_parent_lifecycle_2026-10-03/source_manifest.json
?? before_pause_2026-10-03/AGENTS.md
?? before_pause_2026-10-03/common__script_constants__camp_administration_origin_constants.txt
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_effects.md
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_effects.txt
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_occupation_effects.md
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_occupation_effects.txt
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_origin_effects.md
?? before_pause_2026-10-03/common__scripted_effects__camp_administration_origin_effects.txt
?? before_pause_2026-10-03/common__scripted_triggers__camp_administration_occupation_triggers.txt
?? before_pause_2026-10-03/common__scripted_triggers__camp_administration_origin_triggers.txt
?? before_pause_2026-10-03/common__scripted_triggers__camp_administration_triggers.txt
?? before_pause_2026-10-03/docs__plans__system_camp_repression_rework_plans__administration_redesign_2026-09-06__foundation_source_tests.py
?? before_pause_2026-10-03/mcp_narrow_source_queries.json
?? before_pause_2026-10-03/mcp_narrow_source_queries.mjs
?? before_pause_2026-10-03/source_manifest.json
?? mengele_adapter_mcp_2026-10-03/before_germany_mengele_effects.txt
?? mengele_adapter_mcp_2026-10-03/before_institutional_mortality_source_tests.py
?? mengele_adapter_mcp_2026-10-03/before_source_hash.json
?? mengele_foreign_purchase_retirement_2026-10-03/before_germany_mengele_decisions.txt
?? mengele_foreign_purchase_retirement_2026-10-03/before_germany_mengele_effects.txt
?? mengele_foreign_purchase_retirement_2026-10-03/before_hashes.json
```

### Historical/ledger proposals

Disposition/purpose for every listed entry: unresolved or accepted-and-queued as stated by owning document; not implemented by presence.

Exact path prefix: `A/occupation/` (expand A/Q as defined above).

```text
?? geographic_source_allocation_proposal_2026-09-27.md
?? historical_campaign_expansion_addendum_2026-09-26.md
```

### Reference artwork and native-element mapping

Disposition/purpose for every listed entry: finished reference/provenance artifacts; current native acceptance incomplete, older variants superseded.

Exact path prefix: `A/references/` (expand A/Q as defined above).

```text
?? camp_admin_administration_reference.png
?? camp_admin_locations_records_locked_reference_v4.png
?? camp_admin_locations_records_locked_reference_v4_handoff.md
?? camp_admin_locations_reference.png
?? camp_admin_locations_reference_v2.png
?? camp_admin_locations_reference_v2_handoff.md
?? camp_admin_locations_resource_locked_reference_v3.png
?? camp_admin_locations_resource_locked_reference_v3_handoff.md
?? camp_admin_records_reference.png
?? camp_admin_records_reference_before_label_fix.png
?? camp_admin_records_reference_before_site_violence_label.png
?? camp_admin_records_reference_v2.png
?? camp_admin_records_reference_v2_handoff.md
?? camp_admin_shortage_reference.png
?? killing_role_locked_reference_2026-09-26.md
?? location_locked_actions_reference_2026-09-26.md
?? location_locked_tooltips_reference_2026-09-26.md
?? national_action_locked_reference_2026-09-26.md
?? native_element_mapping.md
?? postqualified_2026-09-27/administration.png
?? postqualified_2026-09-27/locations.png
?? postqualified_2026-09-27/maintenance_shortage.png
?? postqualified_2026-09-27/provenance_handoff.md
?? postqualified_2026-09-27/records.png
 M provenance.md
?? shortage_paused_action_reference_2026-09-26.md
```

### Administration proposals and accepted-choice notes

Disposition/purpose for every listed entry: documentary disposition requires accepted_implementation cross-check; not automatic code approval.

Exact path prefix: `A/` (expand A/Q as defined above).

```text
?? soviet_famine_relief_shortfall_proposal_2026-09-26.md
```

### Other existing system plan files

Disposition/purpose for every listed entry: older evidence/design; current acceptance contract takes precedence, ownership review required.

Exact path prefix: `docs/plans/system_camp_repression_rework_plans/` (expand A/Q as defined above).

```text
 M core_script_architecture_handoff.md
```

### Modified specification text

Disposition/purpose for every listed entry: finished documentary reconciliation with unresolved acceptance/evidence limits.

Exact path prefix: `docs/specs/` (expand A/Q as defined above).

```text
 M system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_3_germany_japan_soviet_deepening.md
 M system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md
```

### System contract documents

Disposition/purpose for every listed entry: finished source-contract prose; mixed CBRN ownership and native acceptance need review.

Exact path prefix: `docs/systems/` (expand A/Q as defined above).

```text
?? camp_administration_dispatch.md
?? camp_exact_cohort_transfer.md
?? camp_institutional_mortality.md
 M cbrn_warfare/genocide/genocide_crisis_system.md
```

### Unpublished native-QA fixture and before snapshots

Disposition/purpose for every listed entry: finished working-tree QA source fixture/provenance; live retest and broader integration publication pending.

Exact path prefix: `Q/` (expand A/Q as defined above).

```text
?? before/camp_administration_effects.txt
?? before/camp_administration_origin_effects.txt
?? before/camp_administration_ui_effects.txt
?? source_tests.py
```
