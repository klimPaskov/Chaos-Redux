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
- The actual reception-capacity helper was first checked with absent/zero/below/equal/over-capacity cases; that check found equality rejected. The accepted Part 6 wording was then applied directly: equality now passes and only overload rejects. Current source-derived cases below cover absent, zero, below, equal, and above loads.
- `python .tmp/c11/check_pressure_contract.py`: bounded callback/source contract passes, including the AAA/BBB `PREV.PREV.CONTROLLER` front, caller-owned temporary outputs and a 250k state submitting 5k flight above the 37.5k protected floor, without a physical population/death mutation in the adapter.
- Final source inspection proves restored identifiers, current cost/localisation/constant wiring and all successful-payment guards.

Installed vanilla `localisation/english/TAOG_decisions_l_english.yml`, line 503, directly uses `[?constant:...]`, confirming the restored support-stock and reception-supply constant displays.

The probability inspector classified decisions as missions and returned no decision candidates, so its returned revision is not a final scenario comparison.
The source-derived calculations above replace that unavailable adapter, with no engine frequency or candidate-pool probability claim. `python .tmp/live_verification_2026-10-13/final_parser_repair/test_contract.py` passes 29 source cases, including the two corrected priority comparisons.
The repair-owned 50-case production transport interpreter and its 11-case famine adapter both pass. An additional contract scenario passed each of the four lane-specific tokens/temporary API inputs through actual transport payment, saved receipt, refund replay and shortage gates. The ordinary maintained famine runner still lacks native `meta_trigger` interpretation, and the unadapted c11 cost contract harness does not mock `var:migration_transport_target`; the temporary repair adapter is the meaningful result for those cases.
Parameterized script validation returned partial coverage (`valid = null`, unresolved TARGET bindings, parameters unchecked and 39 unchecked argument blocks); its one narrower explicit-bound retry did not return.
The parent's changed-file validation requests also did not return and were terminated; no validation result is claimed for those requests.
The pressure worker's map request did not return; map geometry is unchanged and its script-only scope does not require a geometry rewrite proof.
These capability limits are verification limits, not missing source implementation.
No HOI4 process was launched and no live execution or visual rendering is claimed.

## What history cannot restore and the spec-based implementation

The historical vulnerable/worker descriptions and specifications discuss priority selection and industrial recovery, but the recoverable parent routes use the same exact cohort-transfer primitive and contain no distinct priority registry or industrial-output recovery consumer.
Parent completed a connectivity-only fsck over 5,087 unreachable commits and found 12 migration/famine candidates. Full candidate-tree search found no cohort-priority or machinery-recovery implementation. The inspected 4a3770ba7321176f3b1ff028cc06e045721364dc `fm_evacuate_vulnerable` decision uses a generic state-population transfer and undifferentiated cohort record. Across 23 installed Workshop directories, no Chaos Redux descriptor or migration-source copy was located. Evidence is retained in `.tmp/handoff3/migration/fsck_connectivity.txt`, `unreachable_migration_history.txt`, and `dangling_priority_candidates.txt`; no historical implementation was restored.
This package is a new specification-based implementation, accepted under the current C11 followup. Design basis: `famine_and_migration_system_spec_part_6_decisions_ai_presentation.md`, lines 175–193, and `famine_and_migration_system_spec_part_3_displacement_migration_return.md`, lines 384–400 and 463–469.
The exact cohort ID stores `general`, `vulnerable`, `industrial`, or `administrative` priority. The player selects the moved group; no ages, jobs, or household composition are assigned to the remaining residents.
Vulnerable evacuation moves half the standard prepared batch. Industrial evacuation keeps the standard batch and retains its support-equipment prerequisite and heavier train cost. Administrative evacuation uses a standard batch, the standard train/fuel/convoy profile, and the same route, pressure, preparation, and reception rules.
The signed industrial workforce balance subtracts the measured debit from the origin and credits only survivors at the destination. Its current controller’s factory-output contribution is the signed state workforce share multiplied by the state industrial-complex and arms-factory levels divided by the controller’s `num_of_factories`; dockyard output uses dockyard levels over the same denominator. Local construction and industrial-complex repair shift by twice the signed state share, capped at +/-50%. No factory or machinery object changes owner or location.
Example: an origin with 100,000 people and 10 of the owner’s 100 factories transfers 5,000 industrial-priority people. After debit, its workforce share is -5,000 / 95,000 = -5.263%, contributing -0.526% owner factory output and -10.526% local construction/repair. If 4,900 survive a route that kills 100 and arrive in a 100,000-person destination, the post-credit population is 104,900, so its workforce share is +4.6711%; at a 10% factory share this contributes +0.4671% factory output and +9.3422% local construction/repair. Conservation is debit 5,000 = route deaths 100 + survivor credit 4,900; residual 0. A later transit subtracts that debit from the current host before crediting only survivors at the next host, so the old host does not retain industrial credit and the same generation cannot be counted twice.
The administrative class has no separate reception or administration modifier because the accepted specification provides no such outcome; its source/destination behavior otherwise uses the ordinary exact-transfer and reception contract.
No unrelated system simplification or substitute asset was introduced. Source validation limits and runtime behavior are recorded in `.tmp/handoff3/migration/migration_depth_evidence.md`.

## C11 follow-up: recovered general lane and priority/output implementation

The recovered `migration_evacuate_civilians` source at commit `839850b0d` was a combined preparation-and-transfer action that charged political power. The current design keeps preparation as its own action and prohibits political-power evacuation costs, so the decision surface uses its historic identity and no-PP standard transport contract inside the current prepared-route lifecycle. This is a source-guided current implementation, not a byte-for-byte restore of obsolete costs or staging behavior.

All four exact cohort classes now have player choices: `migration_evacuate_civilians` (general), `migration_evacuate_vulnerable`, `migration_evacuate_administration`, and `migration_evacuate_workers` (industrial). General and administration use the standard train/fuel/sea-convoy profile; vulnerable moves half the standard transfer batch; industrial keeps the support-equipment and heavier-train gate. All lanes require current real-pressure targeting, an already prepared origin, valid exact movement and the shared national reception gate. The shared gate admits equality and blocks only `load > capacity`; missing capacity still blocks a positive-load country.

The concurrent parser/API repair from `.tmp/live_verification_2026-10-13/migration_load_repair/repair_only.patch` is included as a necessary current dependency, with provenance recorded; it changes unsupported parameter-shaped helper calls into documented explicit temporary inputs and native meta bindings, while preserving transport profiles and saved refunds. The repair's superseded `migration_priority_apply_industrial_recovery` additions are excluded; the generation-guarded `migration_priority_reconcile_industrial_transfer` owner below is authoritative, and the repair's Event 34 three-line hunk remains untouched. The concurrent `.tmp/live_verification_2026-10-13/final_parser_repair.md` correction is also retained for the two nonzero comparisons in the priority effect helpers, using installed `check_variable` enum `not_equals`; its unrelated CBRN, occupation-law, and Chaos Meter hunks are outside this change.

The general action reuses its existing localisation keys and no-PP fee display, adds the current standard transport receipt, and records `general` on the exact cohort. Its recovered willingness formula remains base 13, multiplied by 4 for trapped population and by 2 at war; these are AI scores, not probabilities. A source-derived contract check and independent decision audit cover standard/general, vulnerable, administration, and worker costs and receipts, including cancelled actions, stale payer cleanup, corridor completion, and direct transfer.

Capacity boundary scenarios now produce: missing load/zero load pass the existing unburdened branches; positive load below capacity passes; load exactly at capacity passes; load above capacity fails. The corrected rule comes from Part 6 line 193 and is shared by all four migration evacuation options and the famine evacuation seam. Admission and transit predicates remain unchanged.

The industrial output projection is a derived country modifier rather than a construction-only proxy. Per state it computes `signed workforce share × (industrial complexes + arms factories) / controller num_of_factories` for factory output and `signed workforce share × dockyards / controller num_of_factories` for dockyard output; state construction and industrial-complex repair separately use twice the share, clamped to ±50%. Each contribution is replaced on exact cohort transfer, controller changes, and the existing sparse registered-state modifier refresh. Factory levels, factory ownership, population, and the Deaths ledger are untouched. A stored producer receipt subtracts the exact old contribution when occupation changes and credits the new controller. A nonzero integrated workforce balance remains in the existing sparse state registry without setting displacement-active; zero balance retires normally. The existing registered-state processor refreshes modifiers for nonzero workforce balances, so later building/population changes are incorporated without a new global scan.

The independent decision audit found the added administration lane ties vulnerable at AI scores 52 without positive flight pressure and 156 with it. General remains distinct by its trapped-population and wartime factors (base 13 × 4 for trapped × 2 at war). These willingness values are not a candidate-pool probability. The MCP adapter response was partial/unresolved, so no choice probability or actual execution frequency is claimed.

The historical audit remains conclusive: parent inspected all 5,087 unreachable commits and 12 migration/famine candidates. A broader `-G` scan across `common` and `events` found 19 candidates; the Event 13 industrial-evacuation match contained no selected cohort or transfer record. No cohort-priority or industrial-recovery implementation was found, and no Chaos Redux descriptor appeared among 23 installed Workshop mod directories. Results remain in `.tmp/handoff3/migration/fsck_connectivity.txt`, `unreachable_migration_history.txt`, `dangling_priority_candidates.txt`, `unreachable_all_scripts_priority_history.txt`, and `broad_priority_matches.txt`.

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
