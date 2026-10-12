# Migration and famine history — C11, 13 October 2026

The owner authorized exact restoration of removed migration/famine depth and specifically required local crisis visibility, no political-power fees, fuel and disconnected-island convoy costs, centralized tuning, AI and tooltip alignment, and shortened large UI numbers.
This is the current C11 history and implementation report.

## History evidence

`git log -S migration_prepare_evacuation -- common/decisions/migration_decisions.txt` and `git log -S famine_invite_relief -- common/decisions/famine_decisions.txt` identify `839850b0d6c74a34c206c454ab549d6cbe99bbf7` as the removal commit.
Its parent is `ca05bb484`; all recovered action source comes directly from `git show 839850b0d^:<path>`, rather than a reconstruction.
The offending diff removes three distinct migration decisions (`migration_prepare_evacuation`, `migration_evacuate_vulnerable`, `migration_evacuate_workers`) and replaces them with `migration_evacuate_civilians`.
It also removes `famine_invite_relief` and the corresponding activation, paid-receipt, donor/contract and cleanup helpers.
The worker evacuation previously had its own support-equipment prerequisite and heavier train fee; the replacement drops that distinct requirement.
Preparation previously took its own time and payment and published the state preparation flag; the replacement publishes preparation inside the evacuation action.
These are actual lost decision roles, not merely shorter prose.

The separate Request Relief action selected a named overland donor and persisted its paid contract generation and donor before continuation.
The surviving Import Food action still selects and delivers overland donor contracts: comparing its parent and successor bodies proves that land relief itself was not removed.
Restoring Request Relief recovers its separate invitation, timing and control; the existing import/delivery behavior is retained.
The old country-wide reserve-response selector needed by that invitation is recovered with it.

The richest parent already contained internal and foreign displacement, exact civilian transfer conservation, cohort identity and visit history, protected population floors, route mortality, trapped-population accounting, bilateral corridor offers and consent, real reception services/capacity, medical reception, distribution, transit, whole-cohort integration, foreign resettlement, voluntary/forced return, relief donor selection, reserve depletion, staged famine mortality, historical food profiles, blockade evidence and sparse runtime scheduling.
The earlier implementation chain includes `00919f6cc` (shared gameplay/map modes), `8911528fc` (owner adapters), `87e04037c` (cohort visits), `1b76c8413` (corridor contracts), `03147f764` (foreign relief donors), `59ee4eb62` (paid prospective reception), `c3de4fd62` (whole-cohort integration), and `22f54df93` (Hunger Lines famine and flight).
The October rework did not delete those deeper owners: its migration core diff changes only two lines, while cohort, reception, custody, corridor and donor systems remain.
No missing earlier version of those owners is invented or substituted.

`8540b5be9` (parent `f3148c8e7`) changes only `localisation/english/famine_l_english.yml` and `migration_l_english.yml`, with 58 insertions and 58 deletions.
It compresses descriptions and omits explanations, but removes no gameplay source.
`76156787c` already restores historical famine/migration wording in the current branch; C11 recovers the deleted action lines from the removal parent and preserves other restored wording.
`f41b58e6c` supplies shortened migration/camp counters; those dynamic display values are retained.

The genuinely added October systems remain: Hunger Lines food pressure and launch stages, the independent famine-country registry, national food-crisis modifier, timed concealment, neighboring flight from special Chaos captures, and the existing overloaded-host relief responses.
Art and its consumers remain unchanged.

## Restoration and owner-rule implementation

Disposition: implemented within the owner's explicit C11 scope; source checks and independent reviews are recorded below.
The removed decision bodies, activation/receipt validators, cleanup branches, required constants and action localisation have been recovered from `839850b0d^`.
The merged evacuation is replaced by its three parent actions.
The subsequent transport and live-pressure changes implement the owner's explicit C11 direction; they are not claimed to be historical restoration.
The restored worker support requirement remains a real prerequisite and its value is moved into script constants.

## Reference and validation evidence

The connected reference_context/search/read/source_lookup routes are exposed and respond.
Installed `common/decisions/_documentation.md`, lines 1–46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, establishes country/FROM state scope and per-frame/per-day decision evaluation.
Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 284–336, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, establishes that custom cost rows do not debit resources and require explicit payment, ready/blocked/tooltip keys and a matching affordability trigger.
Installed `documentation/effects_documentation.md`, lines 1388–1396, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, establishes country scope for `add_fuel`.
The initial decision context omitted Effects and Localisation due to its limit; targeted reads/searches provide the required affected rules rather than treating its source list as coverage.
An exact source_lookup for the guessed vanilla symbol `ENG_evacuate_gibraltar` found no definition; it is not a vanilla precedent claim.
The transport worker identified the actual vanilla `is_in_home_area` precedent in the installed ENG decisions, with exact evidence recorded below on integration.
No live-game execution or rendering is claimed or requested.

## Completion evidence

The four historical actions and their required triggers, receipts, cleanup, constants and original wording are restored from `839850b0d^`.
The restored preparation uses a state-local unprepared check so the retained current phase provider cannot lock its first step, and vulnerable/worker evacuation keeps the current not-overloaded-host contract.
The owner's explicit cost/pressure changes are applied to 25 fee bundles and the separately owned reception preparation action.
All 25 payments guard equipment spending and work publication on a successful payment result.
Country policy costs remain country-scoped, while state actions and aerial relief preserve payer/action/target receipts and concurrent destinations.
Airlifts use fuel, aircraft and air experience, with no sea-convoy fee.
No art is replaced or repointed, no report event is edited, and no new worldwide periodic hook is added.

The decision specialist independently rechecked the 25 payment guards, shared reception display/activation gate, exact saved refunds and action-target cleanup, then the airlift state receipt.
It identified a missing capacity predicate in two `available` blocks; both received the same predicate used by their start helpers, and source reinspection confirms the match.
The AI specialist reviewed the actual restored formulas and named pressure/resource scenarios.
Preparation scores are 5, 15 with displacement, 10 at war, or 30 with both; workers score 8/24/16/48 for preparation and owner civilian factories; prepared vulnerable evacuation scores 52 without flight or 156 with positive flight.
The invitation scores 7 at base, or 56 with positive pressure and democracy, rising to 84/140/224 at acute shortage/famine/catastrophic stage.
Those are willingness scores, not click probabilities.
The restored formulas match the historical parent; absent actions had no active-before score, and representative surviving-action scores remain unchanged (reserve release 72 peace/108 war, distribution 108, voluntary return 200).
The auditor's scratch before snapshot was taken after restoration, so immutable Git parent/current source supports historical restoration claims instead of that late snapshot.

Meaningful checks:

- `python .tools/test_famine_takeover_20261006.py`: 11 production-source regressions pass, including reserve/refund accounting, unchanged Hunger Lines and national-crisis behavior, donor delivery outputs, scoped achievements, famine cause/profile gates and stage recovery.
- The maintained refund regression runs actual transport payment, successful-payment guard, equipment/work publication, full zero-consumption refund/cleanup and replay on connected and disconnected targets, retaining zero PP and the saved fuel/convoy quote after geography changes.
- `python .tmp/c11/migration_costs/test_contract.py`: 45 source-helper scenarios pass, covering fee boundaries, sea convoy shortages, wrong-payer and replayed refunds, parallel targets, live display/debit agreement, foreign-owned occupied island/mainland paths and independent aerial destinations.
- The actual reception-capacity helper passes absent/zero/below/equal/over-capacity cases; equality and overload reject evacuation.
- `python .tmp/c11/check_pressure_contract.py`: bounded callback/source contract passes, including the AAA/BBB `PREV.PREV.CONTROLLER` front, caller-owned temporary outputs and a 250k state submitting 5k flight above the 37.5k protected floor, without a physical population/death mutation in the adapter.
- Final source inspection proves restored identifiers, current cost/localisation/constant wiring and all successful-payment guards.

Installed vanilla `localisation/english/TAOG_decisions_l_english.yml`, line 503, directly uses `[?constant:...]`, confirming the restored support-stock and reception-supply constant displays.

The probability inspector classified decisions as missions and returned no decision candidates, so its returned revision is not a final scenario comparison.
The source-derived calculations above replace that unavailable adapter, with no engine frequency or candidate-pool probability claim.
Parameterized script validation returned partial coverage (`valid = null`, unresolved TARGET bindings, parameters unchecked and 39 unchecked argument blocks); its one narrower explicit-bound retry did not return.
The parent's changed-file validation requests also did not return and were terminated; no validation result is claimed for those requests.
The pressure worker's map request did not return; map geometry is unchanged and its script-only scope does not require a geometry rewrite proof.
These capability limits are verification limits, not missing source implementation.
No HOI4 process was launched and no live execution or visual rendering is claimed.

## What history cannot restore

The historical vulnerable/worker descriptions and specifications discuss demographic prioritization and industrial recovery, but the recovered parent routes use the same exact cohort-transfer primitive and have no distinct demographic selector or machinery/recovery consumer.
Their genuine differences are the preparation step, support-stock prerequisite, train fee and historical contextual AI weights.
No missing demographic or machinery code was found to restore, and none is invented.
Likewise, maritime evacuation, abandonment and internment/entry-priority proposals have no recovered implementation and remain outside the requested restoration.
The October merge did not remove the existing core famine, donor, cohort, corridor, reception, settlement or return systems, so there is no earlier replacement to restore for those owners.

No design simplification or substitute asset was introduced by C11.
The source-parent restoration is followed only by the owner's explicit transport/pressure requirements and the necessary current owner-contract guards described above.

## Changed files and commits

Implementation commit: `ad449f3fd243624ff9048178c77db71e903032cb` (35 source, localisation, API and regression-test files).
Documentation commit: `6ac633b0a76e5d5b9961dcd0f90a606cb78b40e1` (history report, current system/API docs, exact recovered spec sections and editable decision-map rows).
The owner-plan C11 line records the published implementation and documentation hashes.


Skills used: chaos-redux-decisions-missions (including its payment reference), chaos-redux-map-states, chaos-redux-ai-strategies, chaos-redux-subagents and chaos-redux-shared-git-commit.
The chaos-redux-xlsx skill was checked for the spreadsheet authority rule; only the editable spec decision-map CSV changed, and the catalog workbook and its export-only CSVs are untouched.
No skill was created or modified.

Exact changed-path inventory (C11-owned hunks only):

- `.tools/test_famine_takeover_20261006.py`
- `common/decisions/categories/migration_decision_category.txt`
- `common/decisions/famine_decisions.txt`
- `common/decisions/migration_decisions.txt`
- `common/on_actions/humanitarian_runtime_on_actions.txt`
- `common/script_constants/famine_decision_constants.txt`
- `common/script_constants/migration_decision_constants.txt`
- `common/script_constants/migration_reception_preparation_constants.txt`
- `common/script_constants/migration_pressure_constants.txt`
- `common/script_constants/migration_transport_cost_constants.txt`
- `common/scripted_effects/famine_adapter_effects.txt`
- `common/scripted_effects/famine_decision_owner_effects.txt`
- `common/scripted_effects/famine_decision_phase_effects.txt`
- `common/scripted_effects/migration_decision_owner_effects.txt`
- `common/scripted_effects/migration_decision_phase_effects.txt`
- `common/scripted_effects/migration_reception_preparation_effects.txt`
- `common/scripted_effects/migration_pressure_effects.txt`
- `common/scripted_effects/migration_transport_cost_effects.txt`
- `common/scripted_triggers/famine_decision_owner_triggers.txt`
- `common/scripted_triggers/migration_decision_owner_triggers.txt`
- `common/scripted_triggers/migration_decision_cost_triggers.txt`
- `common/scripted_triggers/migration_reception_preparation_triggers.txt`
- `common/scripted_triggers/migration_pressure_triggers.txt`
- `common/scripted_triggers/migration_transport_cost_triggers.txt`
- `common/scripted_localisation/migration_reception_preparation_cost_scripted_localisation.txt`
- `common/scripted_localisation/migration_transport_cost_scripted_localisation.txt`
- `localisation/english/famine_l_english.yml`
- `localisation/english/migration_l_english.yml`
- `localisation/english/migration_transport_cost_l_english.yml`
- `common/scripted_effects/migration_transport_cost_effects.md`
- `common/scripted_effects/migration_pressure_effects.md`
- `common/scripted_triggers/migration_pressure_triggers.md`
- `common/scripted_effects/migration_reception_preparation_effects.md`
- `common/scripted_triggers/migration_reception_preparation_triggers.md`
- `common/scripted_effects/migration_decision_phase_effects.md`
- `docs/plans/migration_famine_history_2026-10-13.md`
- `docs/systems/famine_system.md`
- `docs/systems/migration_system.md`
- `common/scripted_triggers/famine_decision_owner_triggers.md`
- `common/scripted_triggers/migration_decision_owner_triggers.md`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `docs/specs/famine_and_migration_system_specs/README.md`
- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_decision_map.csv`
- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_decision_mission_prompt.md`
- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_3_displacement_migration_return.md`
- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`
