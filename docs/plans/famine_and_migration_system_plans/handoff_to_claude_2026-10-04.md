# Famine and migration engineering handoff

Date: 2026-10-04.
Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.
All paths below are repository-relative unless explicitly absolute.
The system is incomplete.
Implementation stopped at the orchestrator's handoff request; the collaboration inventory then contained only the root agent, so the former workers could not be resumed or interrupted through that inventory.
The inspected shared HEAD was `d1d19047989cdfe9e1d7d63675ad5fa120857245`; unrelated workstreams remain dirty and Claude has already published a related date/neighbor correction described below.
Only this document is authorized for this handoff commit.

## 1. Goal and accepted design

Famine and migration are separate mechanics connected through explicit adapters, not one mechanic, decision category or random event.
Use `famine_*` and `migration_*`; narrow `humanitarian_*` and `civilian_transfer_*` infrastructure is permitted.
Neither mechanic receives an event ID, event-pool registration, event-log event or pacing pulse.
Event 149 `Immigrations` is retired, without a competing flat population drain or replacement event.

Famine requires dynamic state food security, reserves, relief, supply strain, acute shortage, famine and catastrophic famine, with population-scaled severe mortality through `apply_exact_state_civilian_population_loss`, recorded as `From famine`.
Migration requires exact internal displacement, cross-border flight, evacuation, deportation, reception, integration, resettlement, voluntary/forced return and trapped populations with real consequences.
Physical movement removes population once and credits only measured route survivors; movement itself is not death.
Occupation, forced-movement, transit, trapped and famine deaths have separate authoritative ownership and cannot debit or record the same death twice.
Blockade famine requires proven war, isolation, maritime dependence, port/route disruption, convoy/escort shortage, insufficient local supply and no relief corridor.
Ideology is bounded after eligibility; persecution, camps, bombing, famine, occupation conduct and route danger can override affinity.

Both dedicated mapmodes are available from campaign start: `famine_state_map_mode` and `migration_state_map_mode`.
Their decision categories remain hidden until their own genuine starting or large/repeated/sustained problem.
Famine presents exactly Food Security, Food Reserves and Relief Access; migration presents exactly Displacement Load, Reception Capacity and Border Policy.
No shared full scripted GUI or fourth headline value is accepted.
Use active registries, exact callbacks and scheduled owner jobs, never a whole-world daily/weekly/monthly simulation scan.
All accepted adapters, AI responses, eight achievements, final DDS/sprite consumers, localisation, permanent documentation and catalog alignment are completion requirements, not optional polish.

### Binding source pack

Read `AGENTS.md`, relevant repo skills, offline wiki and installed documentation before changes.
The eight parts are:

```text
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_1_core.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_2_famine_food_security.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_3_displacement_migration_return.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_4_deaths_occupation_atrocity.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_5_historical_profiles.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_6_decisions_ai_presentation.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_7_cross_system_connections.md
docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_8_balance_acceptance.md
```

Supporting authority is the same directory's `famine_and_migration_system_coding_prompt.md`, `famine_and_migration_system_decision_mission_prompt.md`, `famine_and_migration_system_asset_prompt.md`, `famine_and_migration_system_subagent_routing.md`, `famine_and_migration_system_research_bibliography.md`, `famine_and_migration_system_improvement_loop_closure.md`, `famine_and_migration_system_decision_map.csv`, `famine_and_migration_system_integration_matrix.csv`, `famine_and_migration_system_probability_scenarios.csv`, `famine_and_migration_system_historical_profiles.csv`, `famine_and_migration_system_asset_matrix.csv`, `famine_and_migration_system_input_manifest.csv`, `famine_and_migration_system_output_manifest.csv`, and `subagent_prompts/README.md` plus every applicable prepared role prompt.
The user's separation corrections supersede retained combined-system/incident-event wording.
Folder placement, an old report or implementation evidence does not establish acceptance of a proposal.

Current accepted bounded plans:

```text
docs/plans/famine_and_migration_system_plans/prospective_reception_lifecycle_plan_20261003.md
docs/plans/famine_and_migration_system_plans/prospective_reception_parent_review_20261003.md
docs/plans/famine_and_migration_system_plans/legacy_cost_affordability_parent_acceptance_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_transaction_architecture_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/migration_mapmode_reception_lifecycle_20261003.md
```

The last document contains the accepted receiver-front intent plan and the completed capacity-display audit.
The separate `docs/plans/famine_and_migration_system_plans/2026-10-03_full_system_simplification_package/` is another owner's proposal/evidence package, not approval; in particular `fm09_service_affordability` is not an accepted replacement fixture.
An exact state-integration plan was requested but neither `exact_integration_map_projection_plan_20261003.md` nor its same-named subagent handoff exists at this snapshot.
Its findings are recorded in section 4 instead of treating an undelivered plan as approved.

## 2. Committed state and evidence

The following commits were verified to exist and be ancestors of the inspected HEAD.
These establish source publication, not in-game completion.

| Commit | Source result |
| --- | --- |
| `9a79f16f22593781af1228755090cfa6eb91755d` | Canonical positive reception-service proof 1 accepted; former greater-than-one gates corrected. |
| `32358abec0431a0e0e33253dbafd6ffe61eb0318` | Exact migration endpoint/corridor display and owner/controller privacy; 41 source Boolean cases. |
| `3bfe73111f848886b7cbe0dacf8f98beef25e672` | Real country existence in `humanitarian_country_is_valid`. |
| `6a03f3edd427243bbc683ec41de9d3d2666313b2` | Custody envelope/output cleanup and exact actor/site checks; actor approval token remains the action token, not country ID. |
| `4751110e8f5bf5588758143524c56e0ffb4f937b` | Reception/Camp callers declare temporary outputs before helper calls. |
| `52b2e7cfeadbcd694d24b3a9a99906427079f60c` | Non-advancing food observer; material assessments enqueue exact existing-registry jobs without query-triggered reveal, mortality or stock changes. |
| `59ee4eb62277982172b408e2b61ace4eb1237a47` | Audited 39-file prospective reception lifecycle: complete internal-first search, adjacent preparable hosts, exact ordinary living row, paid meaningful services/policy, rollback/refund, full offer/headroom, measured automatic passage, identity-safe pulse cleanup and repeated-small-request memory. |
| `58efb2247e05d4cab9454858c5311a97f4f165ed` | Seven-document prospective checkpoint, not full-goal completion. |
| `e6ec73bcf26a43e400353a4e2d07ba9b8d35aea8` | Twelve byte-exact legacy-cost before sources/CSV and manifest; raw Git blobs independently match all 12 hashes. |
| `a8b59870c26b402ef2475c198b3753031bf8869e` | Map capacity status delegates to complete migration validity rather than cached valid1; 13 independent source cases; incoming-front intent plan accepted but not implemented by this commit. |
| `fcdd06433582602c73366210ac9aa105e7b5c511` | Legacy 25-action audit, architecture, probability baseline and parent acceptance; runtime cost repair is not committed. |

Additional published evidence: `621df57aa7f1000778c540c220d47911b034aa65` accepts/promotes the prospective plan into Parts 3/6; `cdd43abe3b996c1bc3e5538da8d13384c9bb5b33` preserves its 29-source before archive; `2e06576ad0e0eb938533ed26e7136a2edbbc7d89` adds 50 blocked/hover aliases for the 25 legacy cost families; `72783cb91893e901bb7003ddd08ce4efe885dd38` and `f22c7cc30aaed8b4dde6f40f9733d4e3a8bb56b3` record caller-owned temporary outputs and native custom-cost key coverage in skills.
The prospective archive's 29 raw committed blobs also matched its manifest without decoding/filtering.

Important external committed change: Claude's `7cbd3faeaf416b300a3b3b025f9bafe9af51a772` fixes famine exposure/mortality/mission date units, migration mission/cooldown dates and the preparable destination's invalid state-scope `is_neighbor_of`.
`global.date` counts one game hour as **0.00001**, not one day or one integer hour.
Use the shared `chaosx_convert_days_to_date_offset` and `chaosx_convert_date_offset_to_days`; native timed-flag `days` remains days.
Preserve `famine_schedule_next_mortality_date`, `famine_set_mission_relief_deadline`, `famine_set_mission_route_hold_deadline` and the `migration_set_mission_*_deadline` helpers.
The preparable neighbor predicate is `any_neighbor_state = { state = event_target:civilian_transfer_origin }`.
Do not restore cost files from the older baseline and discard these committed fixes.
This handoff inspected that commit's source diff; it did not repeat its runtime tests.

The user-provided delegation reported pressure cleanup commit `85800a3cc432e1ddce1a70cf9b28676aa6467f28`, but that object is not present in this Git database.
The current source has the cleanup/state-and-actor binding described by that report; do not cite the missing object as locally verified publication.

### Implemented package, validation limits

Core formulas, state population transactions, separate categories, two mapmodes, typed adapters, sparse scheduler, profile tables and achievement consumers exist.
The documented food score is `clamp((1.15*production + 1.10*transport + 1.25*extraction + need + 0.80*environment + 0.90*vulnerability + 0.95*governance - 1.20*relief)/7.15, 0, 200)`, with stage thresholds 25/50/75/100 and exposure/recovery hysteresis.
Actual tuning/source and the date conversions are authoritative; documentation is not an engine test.

Eight registry IDs exist in `common/achievements/chaos_redux_achievements.txt`: `famine_break_the_blockade`, `migration_no_one_left_at_the_gate`, `migration_roads_home`, `famine_bread_across_the_front`, `migration_hungry_not_contagious`, `migration_a_place_at_the_table`, `famine_the_grain_stayed_home`, `migration_the_country_did_not_empty`.
Predicates/effects live in `common/scripted_triggers/humanitarian_achievement_triggers.txt` and `common/scripted_effects/humanitarian_achievement_effects.txt`; generated asset inventory records 61 final DDS outputs, including achievement variants, seven report scenes and four map buttons.
`subagent_handoffs/category_asset_closure.md` and `subagent_handoffs/final_asset_audit.md` contain production/consumer evidence, not live validation.
Fifteen historical profiles are described in `completion_report.md` and the historical-profile CSV, without fixed historical casualty totals.
Their reachability and source-owner gates still require the full completion review.

No live game was launched, no log was requested/read, and no clean `error.log` or live consumer result is established by this workstream.
The user/orchestrator owns those results.

## 3. Uncommitted work inventory

These lists describe this workstream's additions/hunks, not ownership of the entire shared dirty checkout.
Nothing here is authorized for the handoff-only commit.
No implementation was deliberately abandoned; unfinished drafts and missing reports must be reviewed before publication.

### A. Legacy affordability core — finished source candidates

The five new core files are source-tested and parent-read, but uncommitted:

```text
common/script_constants/humanitarian_legacy_cost_constants.txt
common/scripted_triggers/humanitarian_legacy_cost_triggers.txt
common/scripted_triggers/humanitarian_legacy_cost_triggers.md
common/scripted_effects/humanitarian_legacy_cost_effects.txt
common/scripted_effects/humanitarian_legacy_cost_effects.md
```

They contain 15 positive/debit pairs, 15 inclusive resource predicates, 18 fee-bundle predicates and `humanitarian_project_legacy_cost_quote` with 15 normal country display values.
Affordability is `NOT(native holding < fresh constant)`; cached quotes never authorize a payment/refund.
Equipment readers/debits retain `train_equipment`, `convoy`, `support_equipment`, `infantry_equipment` and `transport_plane_equipment`, not guessed model tokens.
Source tests cover 60 component cases, 204 bundle/short/poisoned-quote cases, 36 tuning mutations, quote isolation/repetition/repair and all 15 signed pairs.
Native stock readers are substituted in those models; real debit, parser and callback behavior is not proven.

### B. Decision integration — delivered draft, independent review incomplete

```text
common/decisions/famine_decisions.txt
common/decisions/migration_decisions.txt
common/scripted_triggers/famine_decision_owner_triggers.txt
common/scripted_triggers/famine_decision_owner_triggers.md
common/scripted_triggers/migration_decision_owner_triggers.txt
common/scripted_triggers/migration_decision_owner_triggers.md
common/scripted_effects/famine_decision_owner_effects.txt
common/scripted_effects/famine_decision_owner_effects.md
common/scripted_effects/migration_decision_owner_effects.txt
common/scripted_effects/migration_decision_owner_effects.md
common/scripted_triggers/famine_relief_triggers.txt
```

The report claims source implementation, not completion: 25 exact cost profiles in availability/custom cost/start guards, four immediate guarded bodies, 20 upfront delayed action/state/payer paid flags, separate unpaid negotiation pending receipt, exact relief contract/donor/generation work guards and action-local cancellation/stale cleanup.
Delayed callbacks consume ownership receipts even when downstream work becomes invalid; original five measured-zero-origin refunds remain reachable for valid paid actor/state callbacks.
No blanket cancellation/funded-work refund is accepted.
Airlift fee is 10 air XP; strict 50-XP condition is AI-only.
Workers retain strict non-spend support-equipment >50.
Every fee, duration, cooldown, numeric AI factor and three four-resource rows is retained.
Unused legacy `@..._NEG` definitions remain in the decision headers; remove only genuinely unused definitions after checking remaining hint/non-spend uses.
`ai_hint_pp_cost` literal/file-local hints remain because central-token support for that field was not established.
The report's brace/refund scans do not test the 20 remove/cancel transactions; private-guard tooltip review and independent causal callback tests are unfinished.
The integration terminalization defect below is deliberately not repaired by these wrappers.

### C. Parent quote/API/permanent-document integration — finished draft, publication blocked on B

```text
common/scripted_localisation/humanitarian_cost_scripted_localisation.txt
localisation/english/humanitarian_cost_l_english.yml
common/scripted_effects/famine_decision_phase_effects.txt
common/scripted_effects/famine_decision_phase_effects.md
common/scripted_effects/migration_decision_phase_effects.txt
common/scripted_effects/migration_decision_phase_effects.md
docs/systems/famine_system.md
docs/systems/migration_system.md
```

The 15 stable resource getters call matching inclusive components; 30 ready/blocked strings use matching normal quotes with existing texticons and aliases.
Both bounded phase providers project quotes.
The migration phase Markdown also corrects its dispatcher location to `humanitarian_runtime_effects.txt`.
Stable localisation review passed 120 parsed-source cases and found no key/icon/mapping issue; final receipt-tooltip review is pending.
A causal starting-profile trace found no current visible starting-problem path bypassing registration/quote projection, so no startup quote loop was added.
Permanent-system cost paragraphs describe the intended complete tranche and must not be treated as proof that B is independently validated.

Mixed files requiring hunk-level ownership:

| File | Pending workstream hunk |
| --- | --- |
| `common/scripted_effects/famine_core_effects.txt` | Quote projection to valid owner/different controller in `famine_register_active_state`; stale-paid-receipt cleanup in exact registration/control cleanup. Also contains an unreviewed two-output mortality caller declaration, described under exclusions. |
| `common/scripted_effects/migration_core_effects.txt` | Quote projection in `migration_register_active_country`; two state-local stale-paid cleanup calls. Preserve Claude's date helpers and unchanged integration body pending its separate repair. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Only the added `humanitarian_legacy_decision_costs` index row belongs to this tranche; many other dirty API/population/Event 012 changes do not. |

### D. Receiver-front map intent — half-done, no implementation handoff/tests delivered

```text
common/script_constants/migration_reception_front_intent_constants.txt
common/scripted_effects/migration_reception_front_intent_effects.txt
common/scripted_triggers/migration_reception_front_intent_triggers.txt
common/scripted_effects/humanitarian_corridor_effects.txt
common/scripted_effects/migration_reception_preparation_effects.txt
common/map_modes/chaosx_state_map_modes.txt
common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt
localisation/english/chaosx_map_modes_l_english.yml
```

Drafts contain front-local aligned origin/generation/requester/receiver/cohort/phase metadata, cached qualitative selection, readers and submit/paid-preparation/inner-accept/measured-pass/terminal-cleanup hooks.
They must not contain population/load/capacity/route grants or change mechanical success because a presentation write fails.
Consent reveal qualification is captured before pending status changes; consent publication occurs only inside real inner success.
The planned priority is requested → prepared → agreed, then newest generation and lowest origin ID, preserving all simultaneous records.
Real trapped/overcrowded/arrival/outflow roles retain priority; intent is owner/controller-only and tiny unrevealed offers cannot reveal a category.
Source-only pressure labels are split from actual transfer history, with an actual spontaneous-exodus classifier branch authorized.
No final source model was delivered, so do not assume the hooks/readers are correct or complete.

Missing at this snapshot: `common/scripted_effects/migration_reception_front_intent_effects.md`, `common/scripted_triggers/migration_reception_front_intent_triggers.md`, paired intent hook documentation in `humanitarian_corridor_effects.md` and `migration_reception_preparation_effects.md`, public API/permanent documentation, and `subagent_handoffs/migration_reception_front_intent_implementation_20261003.md`.
The committed capacity-selector correction in the shared localisation file must survive any draft cleanup.

### E. Documentation/report candidates — uncommitted

Six checkpoint files contain a dated partial-tranche reconciliation, still requiring a final source/status review:

```text
docs/plans/famine_and_migration_system_plans/completion_report.md
docs/plans/famine_and_migration_system_plans/source_of_truth_map.md
docs/plans/famine_and_migration_system_plans/handoff_dispositions.md
docs/plans/famine_and_migration_system_plans/mapmode_validation.md
docs/plans/famine_and_migration_system_plans/ai_probability_current.md
docs/plans/famine_and_migration_system_plans/current_resume_20261003.md
```

Their 19:17:59 UTC checkpoint predates delivered decision wrappers and Claude's date correction; some pending-language/hash/line references are stale.
`docs/plans/famine_and_migration_system_plans/subagent_handoffs/current_mapmode_projection_audit_20261003.md` has a finished uncommitted schema-evidence correction: mechanic scenario facts are flat numeric `state`, not nested `state.variables`; equals assertions require `id`, `path={key=...}` and `expected`.

Untracked reports from this workstream:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/bounded_system_patch_completion_audit_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/current_workbook_alignment_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/event_owner_connections_reaudit_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_and_map_checkpoint_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_core_implementation_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_decision_implementation_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_localisation_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/normal_destination_bootstrap_audit_20261003.md
docs/plans/famine_and_migration_system_plans/subagent_handoffs/probability_capability_reaudit_20261003.md
```

All are delivered source/evidence reports, not abandoned drafts; the localisation report explicitly has final guard review pending, and the documentation report is a partial checkpoint.
The bounded completion report was saved/read before that agent's later capacity error; its saved source audit remains evidence, not native execution.
Reconcile each disposition exactly once after final source review; do not pre-register absent reports or infer approval from filenames.

### Shared-tree exclusions and uncertain provenance

`common/scripted_effects/migration_adapter_effects.txt` and `.md` have external Event 012 Gods reception additions; preserve them and coordinate with that owner.
The Gods capacity helper paragraphs still contain greater-than-one proof wording despite canonical positive proof1; do not use that stale wording to retune the guard.
Dirty skill files `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-state-ledgers/SKILL.md` and `.agents/skills/chaos-redux-subagents/SKILL.md` have other-owner changes; our temporary-output/native-cost-key paragraphs are already committed.
Camp, CBRN, Event 001–040, workbook and exported CSV dirty changes are not owned by this tranche.

Two related unreviewed mortality caller hunks are present: `common/scripted_effects/famine_adapter_effects.txt` sets `state_civilian_population_loss_minimum_remaining` unconditionally and declares `state_civilian_population_loss_applied/result` before the exact API; `famine_core_effects.txt` declares those outputs before famine mortality.
The decision worker identified them as parent-owned, but their editing provenance was not established in this handoff capture.
Review/coordinate them separately; do not silently include or drop them with cost work.

## 4. Remaining work, priority and acceptance

1. **Repair the proven integration terminalization defect before claiming valid integration.**
   Exact sites: `migration_local_integration` in `common/decisions/migration_decisions.txt`, `migration_integrate_displaced_cohort`, `migration_apply_reception_delta` and `migration_cleanup_cohort_record` in `common/scripted_effects/migration_core_effects.txt`, and matching owner/core trigger and API documentation.
   The action resolves the whole positive hosted row and requires both state/country reception loads to cover it, but increments national integration first, then debits reception, then calls cleanup without setting row status completed and amount zero.
   Cleanup accepts only a unique completed/invalid zero row, so the integrated positive bound row remains live; a failed debit can leave premature national credit, and another hosted cohort's remaining country load makes replay/counter divergence possible.
   Design an exact whole-cohort settlement transaction: prove cohort/current host/actor/amount and both ledgers, settle once, terminalize with existing completed+zero representation, and credit measured integration only after all owned changes succeed, with narrow rollback on rejection.
   Integration does not alter native state population and must never call `migration_record_transfer_projection`, which requires real physical origin debit.
   Preserve fee ownership separately; partial integration/new enum/global GUI is not approved by the undelivered review.
   Acceptance: two hosted cohorts in one country; repeating the settled row cannot consume the other's load or credit again; failed/partial debit leaves no national credit/terminal loss; native population unchanged; exact state history only on successful measured settlement.
   A country-only API cannot establish an integration destination from a national delta alone.

2. **Finish and independently audit the legacy cost tranche A–C.**
   Review every one of the 25 mappings in `subagent_handoffs/legacy_cost_decision_implementation_20261003.md` against the accepted plan and baseline, then complete private flag/tooltips and paired docs.
   Test actual decision guard/receipt/debit/refund bodies, not only the 33 cost predicates: exact stock, each one-short component, late stock loss, failed/new relief setup versus pre-existing invitation, exhausted stock after paid work, wrong action/state/payer, repeated removal, two states/actions, state-control loss, expired/replaced contract, successful/rejected deferred offer and all five zero-origin refunds versus positive actual debit.
   Ensure an expired work contract consumes only its matching paid receipt without blocking future activation or clearing another contract.
   Native callback exclusivity/same-payer ABA remains unproven; do not invent a UID or generic dedupe.
   Review the mixed core/index hunks, preserve `7cbd3fae`, obtain final independent review, then publish only this completed tranche with shared-tree commits.

3. **Complete receiver-front intent D and map classifier proof.**
   Author missing API/hook docs, run the accepted 14-case matrix in `subagent_handoffs/migration_mapmode_reception_lifecycle_20261003.md`, and inspect every real writer/caller/reader.
   Older accepted and newer pending requests at one front must survive each other's passage/rejection/expiry; simultaneous incoming/outgoing and reversed/new-controller contexts must remain distinct.
   Map hover/color must use only cache/local scalar checks and at most the exact selected-origin lookup, with no ledger traversal, food observation, recalculation or mutation.
   No arrival/host/binding/usable-route/capacity assertion before physical proof; no new amounts in intent receipts, no public foreign intent disclosure, no category reveal or fourth value.
   Pressure-only evacuation/deportation/cross-border/internal labels must say pressure, while actual deportation/spontaneous transfer history has explicit actual-role labels ahead of pressure fallbacks.
   After item1, consider exact **settlement-history** state projection for proven integration, not a fabricated transfer role or current-resident count from cumulative totals.

4. **Close mandatory current probability and native evidence, without substituting source tests.**
   Archives: `validation_baselines/legacy_cost_affordability_20261003/` (12), `validation_baselines/prospective_reception_20261003/` (29), and `evidence/20261003_country_validity/before/humanitarian_validation_triggers.txt` beneath this plans folder.
   Keep distinct actual before/after paths and identical named scenarios; never compare current against itself or reuse August results as October certification.
   Cases include official famine/migration CSV scenarios plus `cost_stock_exact`, `cost_stock_one_short`, `cost_stock_late_deficit`; prospective internal/persecution destination, corridor/border, capacity/hazard/whole-row/headroom, repeated/stale/expiry and exact-cost cases; observer quiet/material/retired/crisis/repeated; live versus dormant/annexed targets.
   Complete baseline → owner patch → same-case `hoi4.probability_compare` through the project auditor for every changed weighted eligibility surface, with numeric limitations explicit.

5. **Close actual external adapter ownership gaps.**
   Read `famine_and_migration_system_integration_matrix.csv`, `subagent_handoffs/current_owner_blocker_reaudit.md`, `subagent_handoffs/event_owner_connections_reaudit_20261003.md` and `completion_report.md`'s adapter section.
   Definition-only seams include `famine_request_occupation_pressure`, `famine_request_bombing_pressure`, `famine_request_war_pressure`, `famine_request_peace_pressure`, `famine_request_cluster_pressure`, `famine_request_scenario_pressure`, their migration counterparts and `famine_condemn_relief_obstruction`.
   Require exact state/actor/cause/positive owned amount/generation/revision/request and cohort/route/custody facts as the endpoint demands; no total-population, intensity, recency, reserve-unit, deaths or dispatcher metadata proxies.
   Camp's actual living-row callback `camp_rework_commit_exact_cohort_custody` → `migration_record_current_state_cohort_custody_exact` is custody-only, not permission for another movement output.
   Generic occupation/control callbacks identify state/controllers but not affected people or capture versus liberation; war/peace and cluster/scenario callbacks do not supply state-local losses/routes; bombing and obstruction lack complete receipts.
   Events 118 `Plague of locust`, 120 `Massive Volcano Eruption` and 131 `Widespread Mutiny` have no recoverable roots in the documented search.
   Event 013 volcanoes and Event 019 General Mutiny are not aliases; missing event design needs explicit acceptance rather than fabricated IDs/content.
   No generic persisted dedupe is safe for current Camp/CBRN date-based request tokens; exact durable replay identity belongs to their authoritative owner.

6. **Finish full completion/doc/asset/catalog acceptance.**
   Re-run all applicable prepared audit routes on final source, disposition every delivered handoff, reconcile six checkpoint files and permanent/API docs, and report every remaining mechanic/adapter/AI/profile/asset/achievement/localisation omission.
   Current catalog needs no scoped edit: `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, Events row150, has ID149/name Immigrations, retirement text in C150, Unavailable in M150, and appropriate blank D:L.
   Scoped IDs5/13/15/20 text matches localisation and ID118 remains unavailable; existing three CSV exports logically matched during the read-only audit.
   Workbook hash `3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67`; Events CSV has 166 records including header at that snapshot, not the August count.
   No workbook save/export was performed by this tranche; any future actual save must preserve concurrent rows/formulas/styles and run `python .tools/export_event_catalog_csv.py` from the root, never edit CSVs directly.
   Asset runtime and clean-game evidence remains user/orchestrator-owned; do not launch the game or request/search logs.

## 5. Tools, tests and flaky routes

Skills used include `.agents/skills/chaos-redux-subagents/SKILL.md`, `chaos-redux-state-ledgers`, `chaos-redux-decisions-missions`, `chaos-redux-shared-git-commit`, `chaos-redux-improvement-loop`, relevant events/assets guidance and `.agents/skills/xlsx/SKILL.md`.
The official skill-creator guidance was used for the two committed skill paragraphs.

Local references: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines305–355/576–610; Effects2253 and4683–4715; Triggers2359–2400; Data structures event targets/temporary variables; Localisation184–210.
Installed references under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`: `documentation/script_concept_documentation.md` Script Constants; complete `common/script_constants/documentation.md`; resource/country scopes in `documentation/triggers_documentation.md`; `documentation/effects_documentation.md`; complete `common/map_modes/documentation.md`; `common/decisions/_documentation.md`; AFG490–500, PHI2352–2380 and BUL4245–4260 cost/negative-archetype precedents.
Installed documentation outranks conflicting wiki defaults; both must be read.
Do not use the live Paradox wiki.

Source tests were in-memory Python via PowerShell here-string piped to `python -`, not permanent test scripts.
Their AST/native-leaf substitution boundaries and counts are in the cost core/localisation and prospective/observer/map handoffs.
The first `python -c` quoting attempt failed before running; stdin fixed that launch issue.
Reconstruct reproducible tests of actual production bodies rather than relying on the reported counts.
Raw archives were verified using `git cat-file blob <commit>:<path>` read through `.NET Process.StandardOutput.BaseStream` and SHA-256, without decoding/filters/checkout.
Normal checks used `rg`, bounded `Get-Content`, `Get-FileHash`, `git diff/show/status/merge-base`.

Mandatory HOI4 MCP routes were discovered by live `ALL_TOOLS` schemas.
Earlier corrected reference/probability/mechanic/event/map requests often returned actual `timed out awaiting tools/call after 600s`; ten-second caller yields/terminated handles are not timeouts.
Retry narrower after a real timeout, not repeated broad load.
Fresh legacy `probability_inspect` succeeded with `PROBABILITY_SOURCE_DISCOVERED` but `decision_ai_will_do` returned `requested_adapter_empty`; 10 famine/15 requested migration candidates appeared only under suggested `mission_ai_will_do`.
A single suggested mission probe returned `INTERNAL_ERROR` without files/artifact; it was not used as a valid decision-score fallback.
No legacy/prospective/observer/country current comparison is established; supported complete fixture/target bindings are missing.
Historical August partial evaluations/comparisons and unresolved pools are provenance only.

`decision_inspect` for `migration_negotiate_corridor` with official `prob_corridor_acceptance` and empty state returned `DECISION_ANALYZED_PARTIAL`, false coverage/unbound scenario, not native behavior.
Map lookup for province406/state96/region39 returned `MAP_LOOKUP_COMPLETED`, revision `bcccf5a7783c4412afe1e1c4a25b41c4f90cb00ac485beef3e5396ed954d2f67`, 64/2065 inline paths and zero adjacency/supply/railway query matches.
Its metadata does not prove a route or complete inventory.
The exposed geographical renderer cannot execute custom mapmode colors/tooltips; older GUI artifacts cover static buttons/headers, not state logic or live clicks.
Artifact templates exist, but resources/list was empty; generic `read_mcp_resource` was incorrectly tried on an unlisted artifact URI and failed `-32603 Artifact provenance manifest is unavailable`.
Do not repeat that contract-invalid accessor or invent an SDK route; bodies remain unread.
`hoi4.script_validate` is not exposed.
Native jobs/helper-expansion/task routes require verified service version/health/schema/task negotiation; none is assumed here.

Exact URIs/revisions, source hashes and limitations are retained in `ai_probability_current.md`, `mapmode_validation.md` and the named probability/map handoffs.
Most source hashes/line positions there predate working wrappers/date corrections; distinguish copied-byte hashes from MCP sourceHash/sourceRevision.

## 6. Interfaces and constraints

`apply_exact_state_civilian_population_loss` is in `common/scripted_effects/chaosx_dynamic_effects.txt` with paired API documentation.
`civilian_transfer_execute_transaction`, `civilian_transfer_finalize` and `civilian_transfer_commit_accounting` are in `common/scripted_effects/civilian_transfer_effects.txt`; do not duplicate their native debit, survivor credit, rollback or deaths ownership.
Migration cohort host/amount/status and reception reconciliation remain migration-owned aligned arrays, not map or famine mutations.
Respect complete alignment, unique exact IDs, current host/control, protected population floor, generation and measured conservation; zero/negative/ambiguous pointers cannot co-opt an implicit row.

`common/scripted_effects/humanitarian_runtime_effects.txt` is thin dispatch over `global.famine_active_states`, historical anchors/candidates, `global.migration_active_states`, reception candidates, active countries and sparse relief donors.
`common/on_actions/humanitarian_runtime_on_actions.txt` scopes control/annex/war/peace/nuclear callbacks; its dirty Event023 changes belong elsewhere.
Its CXT registration is idempotent/pending-only; grants belong to player debug actions under `docs/testing/chaosx_test_country.md`, not periodic hooks.
Keep `famine_to_migration_*` food-safety and `migration_to_famine_reception_demand_*` adapters versioned/owned; observation cannot advance food simulation or infer unknown food as safe.

Corridor state/host mirrors/pulses require matching origin/front/requester/receiver/cohort/generation; receiving and outgoing identities can coexist.
Acceptance is consent, not movement or headroom reservation.
Actual passage alone writes reception/transfer history and achievements; exact terminal cleanup preserves other mirrors, paid services and durable outcomes.
Famine evacuation crosses migration-owned APIs instead of editing its raw ledgers.

UI/GFX: `interface/famine_system.gfx`, `interface/migration_system.gfx`, their report pictures/header files, `interface/mapmodes_interface.gfx` and `interface/chaosx_texticons.gfx` retain registered DDS/texticon consumers.
Do not create a shared full GUI, fake geographic arrows or placeholder art.
Player text describes current choices/results, not implementation history, hidden weights, raw receipt names or tuning caps.
Private flags belong in hidden guards/effects; meaningful public requirements need readable tooltips.
English YML is UTF-8 with BOM; stable getter/base/blocked/tooltip consumers must stay aligned.

Temporary outputs are declared by the caller before nested helper use, especially through `if.limit`; they are unscoped and cannot use `ROOT.`/`PREV.`.
Use flags for persistent booleans, fresh centralized constants for tuning, no unary negated variable tokens or unsupported `<=`/`>=` operators.
Direct `$ACTION$` parameterized helpers were not established for HOI4; use proven Boolean helpers or documented meta effects/triggers.
No source-only result certifies native UI, physical movement, normalized AI probabilities or a clean game.

## 7. Publication and resumption

Resume against current HEAD, not an older baseline checkout.
Do not commit the entire dirty checkout or these unfinished tranches automatically.
Use `.agents/skills/chaos-redux-shared-git-commit/SKILL.md`: capture HEAD/ref/relevant real-index entries, isolate `GIT_INDEX_FILE`, stage exact owned paths/hunks, prepare reconciliation, `write-tree`, `commit-tree`, recheck and `update-ref HEAD <new> <old>` compare-and-swap, then reconcile only owned index entries.
If HEAD changes, rebuild; never force the old tree.
For `.git/index.lock`, verify active Git processes and lock identity/age, wait/retry, and remove only a provably stale lock.
Preserve other owners' staged and unstaged work.
The root remains responsible for accepted-design disposition, complete final wiring/review and honest completion; project workers use explicit self-contained prompts without inherited context.
The existing goal tool reported paused and offered no resume API despite the user's continuation request; no replacement goal or false completion status was created.
The orchestrator's handoff request supersedes further implementation in this turn.
