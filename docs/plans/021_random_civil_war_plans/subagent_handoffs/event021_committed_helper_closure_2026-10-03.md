# Event 021 committed helper closure and repair boundaries

Disposition: committed source dependency audit completed, M1 and L1/L2 temporary-storage corrections source-reviewed, final secondary-mutation guard source-reviewed, mandatory MCP and broader acceptance evidence blocked or pending.
This handoff does not certify Event 021 completion, balance, active Evolution I implementation, or engine behavior.
Authority is the parent's read-only audit assignment and its two subsequent bounded evolution-log review additions.
Only this Markdown report was written by this worker.
No gameplay source, index, commit, design, weight, or timing was changed.

## Committed unknown-trigger risk

The audit pinned the initial observed HEAD `c3c91450ca9d9c37bd386c3f560160991410ba1a` rather than reading dirty files as committed source.
It contains sponsor repair `1f90ca368a06d2e12a6db4dd897a605908f6458b`.
Later observed HEAD `9d7862dcb78ae097f61eb95e07e3ff2e911f75db` has no changes to the Event 021 effects, triggers, constants, event file, or event-owned on-actions relative to that pin.
Other agents advanced HEAD during the audit.
The wider transitive graph inventory below is pinned to `c3c91450`, not a claim that every other subsystem stayed byte-identical.

The committed literal reference `event021_sponsor_repayment_receipt_valid = yes` resolves to a committed COUNTRY-scoped trigger.
Its settlement consumer is `common/scripted_effects/021_random_civil_war_parent_effects.txt:5439` in the pinned Git object.
The trigger definition is `common/scripted_triggers/021_random_civil_war_sponsor_receipt_triggers.txt:5`.
The trigger requires received/evidence flags, the sponsor scope and ID, a live sponsor, an active sponsor commitment, and reciprocal country IDs through PREV and THIS.
The committed sponsor receipt writer stores `random_civil_war_sponsor_scope = ROOT` in `event021_record_received_sponsor_commitment`.
These definitions establish source closure for the reported unknown trigger, without proving the live reciprocal receipt outcome.

| Committed source | Git blob at the audited pin |
| --- | --- |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `c70e6f7853b2889bff7cd2412b2992bb6873943c` |
| `common/scripted_effects/021_random_civil_war_decision_effects.txt` | `7a34a07dfdfa6c5da1e4142f192dfadeefda363d` |
| `common/scripted_triggers/021_random_civil_war_sponsor_receipt_triggers.txt` | `6e3100fffdc585aea69d8a4d6c8c3a7a78467a2f` |

No additional committed reference to a working-tree-only custom effect or trigger definition was found.
The independent cross-check matched all uncommitted top-level helper names against assignments in committed Event 021 and Event 006 adapter-registry sources, rather than checking only an `event021_` prefix.
No unresolved Event 021-owned `constant:random_civil_war*.key` or `constant:event021*.key` reference was found in those Event 021 committed sources.
The three requested candidate, ledger, and active-evolution helper source files are absent from the pinned commit, and their new consumers are also uncommitted.
Their presence in the shared working tree does not repair or invalidate the committed closure result.

The source inventory read 1,075 committed `.txt` files from effects, triggers, constants, events, and on-actions using `git ls-tree` and `git cat-file --batch`.
It indexed 35,444 top-level mod helper names, seeded 396 Event 021 and adapter-registry helper definitions, and followed 1,823 known literal helper definitions transitively.
The traversal matched the repository's ordinary `helper = yes/no` invocation form.
The separate working-tree-only assignment check also covered assignment-shaped calls that were not in that ordinary form.
These are lexical source checks with manual classification of remaining candidates, not a Clausewitz parser, scope validator, campaign graph, or executed test.
Quoted generated script, database merge behavior, dynamically emitted names, and runtime receipts remain separate obligations.
The actual committed event namespace is `chaosx.nr21`, including `chaosx.nr21.1`.

## Literal names, dynamic constructors, and native fields

Two apparent unmatched literal names resolve to installed vanilla scripted triggers rather than missing mod definitions.
`has_same_ideology` is defined in installed `common/scripted_triggers/00_scripted_triggers.txt:732-753` and is used at committed parent-trigger lines 868, 874, 884, and 890.
`can_unlock_second_track_of_sf_doctrine` is defined in that same vanilla file at lines 1418-1432 and occurs in the transitive doctrine-trigger dependency.
The vanilla file SHA-256 is `c8470b1937095f1aec1c09ee78365d770fab1aa7e28eb21d35924ca1253dd1db`.
Neither name belongs in an unresolved-helper repair list.

The direct Event 021 dynamic trigger constructors occur in committed `021_random_civil_war_parent_triggers.txt:108,121,127`.
Their shapes are `has_prepared_independence_wave_iw_00[PACKAGE_ID]_package_setup`, `has_prepared_independence_wave_iw_0[PACKAGE_ID]_package_setup`, and `has_prepared_independence_wave_iw_[PACKAGE_ID]_package_setup`.
The transitive Event 006 scenario dispatcher similarly constructs `independence_wave_load_package_iw_00[PACKAGE_ID]`, `independence_wave_load_package_iw_0[PACKAGE_ID]`, and `independence_wave_load_package_iw_[PACKAGE_ID]` in `006_independence_wave_scenario_effects.txt`.
These are runtime substitutions, not literal missing helper names.
This pass did not certify every allowed package ID's padded expansion, registry admission, or successful package callback.
That constructor coverage remains explicitly unresolved, with no proposed static replacement or fallback.

The following apparent boolean-call candidates are native fields inside their documented owning commands.
Native command headings were also excluded using installed effects/trigger documentation, including `exists`, `has_war`, `has_civil_war`, `is_ai`, `has_capitulated`, `scope_exists`, and the usual country/state predicates.
Argument-field exclusion does not validate the enclosing effect's parameters or scope.

| Excluded field | Exact local contract |
| --- | --- |
| `keep_political_leader`, `keep_political_party_members`, `keep_all_characters` | Installed `documentation/effects_documentation.md:8030-8059`, `start_civil_war` |
| `keep_completed` | Installed effects documentation `4771-4783`, `load_focus_tree` |
| `disband` | Installed effects documentation `3480-3518`, unit deletion commands |
| `active` | Installed effects documentation `3564-3576`, `diplomatic_relation` |
| `elections_allowed` | Installed effects documentation `7526-7538`, `set_politics` |
| `ruling_only` | Installed `documentation/triggers_documentation.md:3640-3654`, `has_country_leader` |
| `allow_spawning_on_enemy_provs` | Installed effects documentation `3278-3300`, `create_unit` |
| `remember_old_capital` | Installed effects documentation `6655-6667`, `set_capital` |
| `transfer_troops` | Installed effects documentation `2495-2498` identifies `annex_country`, offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1504` documents the argument |
| `instant_build` | Installed effects documentation `839-846` identifies `add_building_construction`, offline Effects `3614` documents the argument |
| `is_triggered_only`, `major`, `hidden` | Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:145,149,188` documents event metadata |

## Dependency-minimal dynamic ledger repair

The three bounded source findings and the final secondary-transfer guard pass the latest source re-review below.
This does not establish complete ledger, probability, capacity, engine, or Event 021 acceptance.
The two temporary-output defects have owner corrections and public caller-storage documentation verified in the latest review.
The smallest coherent source bundle is the three new helper files with their direct producer, consumer, replay, and cleanup hunks.
Helper ownership remains event-local, with no central router or wrapper skill.
Use function anchors below to select hunks because other agents are editing the same files and line offsets are moving.
The full current parent effects file contains separate external-war and metadata edits as well as the ledger repair.
Whole-file staging would expand the bundle beyond this recommendation.

| File under `common/` | Required repair surface |
| --- | --- |
| `scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt` | All nine definitions as one coherent candidate/freeze/replay/cleanup API |
| `scripted_effects/021_random_civil_war_front_ledger_effects.txt` | All seven definitions, including exact span validation, secondary-transfer receipt, retained membership, and owner-checked completed-template release |
| `scripted_effects/021_random_civil_war_active_evolution_effects.txt` | Only the existing three provenance-foundation definitions, with capture, commit, and inherited-stage call sites |
| `scripted_effects/021_random_civil_war_parent_effects.txt` | Ledger initialization, candidate construction, validation, allocation, serial activation, executor gates, frozen scenario replay, marker release, retained receipts, and rollback hunks listed below |
| `scripted_effects/021_random_civil_war_effects.txt` | `event021_prepare_force_package`, provenance call in `event021_random_civil_war_commit_opening`, `event021_unregister_front`, `event021_bind_front_plan_row`, `event021_reject_pending_front_plan_row`, scenario-capacity state in `event021_refresh_global_capacity`, source-front cleanup in `event021_cleanup_crisis` |
| `scripted_triggers/021_random_civil_war_parent_triggers.txt` | Secondary candidate/route rules, recorded-source state ownership checks, three scenario-capacity/reserved-target predicates, and scenario eligibility needed by the new reservation flow |
| `scripted_triggers/021_random_civil_war_triggers.txt` | `random_civil_war_scenario_launch_valid` call-site migration to `event021_parent_scenario_reserved_plan_target_valid` |
| `scripted_triggers/021_random_civil_war_lifecycle_triggers.txt` | Dynamic Maximum-scenario envelope branch in `random_civil_war_front_capacity_available` |
| `scripted_effects/021_random_civil_war_lifecycle_effects.txt` | Only `random_civil_war_event6_secondary_origin` and `random_civil_war_source_front_id` teardown in `event021_handle_annexed_country` |
| `scripted_effects/021_random_civil_war_successor_effects.txt` | `event021_prepare_successor_roster_adoption` stale-flag removal and `event021_rebuild_successor_roster` aligned current-crisis roster reconstruction, avoiding the old two-slot interpretation |

The candidate API is `event021_parent_append_dynamic_ordinary_front_candidate`, `event021_parent_append_dynamic_event6_front_candidate`, `event021_parent_clear_scenario_optional_front_receipt`, `event021_parent_clear_scenario_legacy_secondary_plan`, `event021_parent_freeze_scenario_optional_front_rows`, `event021_parent_load_scenario_optional_front_rows`, `event021_parent_validate_dynamic_optional_front_state_spans`, `event021_parent_clear_dynamic_optional_front_candidate_reservations`, and `event021_parent_collect_dynamic_optional_front_candidates`.
The collector calls parent-owned package lookup, source/force preparation, Event 006 identity save/restore, and existing admission predicates.
The freezer depends on parent base-front reservation and the loader, and the loader depends on the optional-span validator.
Freeze/load callers must retain the exact owner-country arrays and publish frozen readiness only after validation.
This API cannot be committed as an isolated file and described as a functioning migration.

The ledger API is `event021_parent_release_completed_front_plan`, `event021_parent_validate_secondary_transfer_receipt`, `event021_parent_refresh_retained_front_receipt`, `event021_parent_validate_front_ledger_identity`, `event021_parent_validate_front_ledger_members`, `event021_parent_validate_front_ledger_row_span`, and `event021_parent_validate_front_ledger_spans`.
Its parent dependencies include `event021_parent_clear_front_plan` and `event021_parent_capture_actual_actor_force_receipt`.
The outer validator already initializes `event021_planned_front_plan_valid`, which nested identity/member/span helpers modify.
Readiness publication remains parent-owned.

The provenance API is `event021_capture_pending_opening_evolution_stage`, `event021_commit_opening_evolution_provenance`, and `event021_inherit_crisis_opening_evolution_provenance`.
It uses normal global/country fields, so these outputs do not depend on temporary-variable return lifetime.
Capture belongs in `event021_parent_prepare_crisis_identity`, commitment in the host, ordinary primary, and Event 006 primary paths, and inheritance in ordinary and Event 006 secondary paths.
The completed-template release and rollback/startup paths must clear serial pending provenance together with the owning ledger.
These helpers do not implement active-war theater review or its management decisions.

The parent effects hunk groups that must travel together are:

- Initialization and admission: `event021_parent_initialize_global_runtime`, the candidate-reservation exclusion in `event021_parent_find_event6_package`, `event021_parent_scenario_reserve_base_front_capacity`, and `event021_parent_prepare_maximum_scenario_front_envelope`.
- Territorial planning: `event021_parent_compute_region_target`, `event021_parent_expand_connected_region`, `event021_parent_freeze_secondary_opening`, `event021_parent_prepare_second_secondary_opening`, `event021_parent_clear_front_plan`, `event021_parent_append_front_plan_row`, `event021_parent_validate_front_plan`, `event021_parent_build_front_plan`, and `event021_parent_build_same_tag_front_plan`.
- Exact row/force consumers: `event021_parent_load_planned_primary_front`, `event021_parent_load_planned_secondary_front`, `event021_parent_copy_planned_front_state_span`, `event021_parent_plan_connected_states`, `event021_parent_copy_opening_state_receipts`, `event021_parent_mark_opening_states`, `event021_parent_record_force_state_context`, `event021_parent_prepare_dynamic_force_package`, and `event021_parent_prepare_crisis_identity`.
- Pending receipts and activation: `event021_parent_clear_pending_force_transaction`, `event021_parent_clear_preplanned_secondary_opening`, `event021_parent_clear_preplanned_secondary_2_opening`, `event021_parent_initialize_primary_opposition_actor`, `event021_parent_initialize_secondary_opposition_actor`, `event021_parent_find_registered_front_source`, `event021_parent_clear_planned_front_state_markers`, `event021_parent_activate_planned_optional_front_rows`, `event021_parent_finish_ordinary_host`, `event021_parent_prepare_secondary_route`, `event021_parent_try_secondary_front`, and `event021_parent_start_secondary_civil_war`.
- Mutation gates and Event 006 state restoration: `event021_parent_clear_transfer_flags`, `event021_parent_start_ordinary_civil_war`, `event021_parent_execute_ordinary_civil_war`, `event021_parent_save_event6_host_identity`, `event021_parent_restore_event6_host_identity`, `event021_parent_try_event6_secondary_front`, `event021_parent_start_event6_front`, `event021_parent_execute_event6_front`, `event021_parent_initialize_same_tag_contest`, `event021_parent_commit_same_tag_takeover`, `event021_parent_execute_same_tag_takeover`, and `event021_parent_finalize_event6_secondary_actor`.
- Durable variable-length roster consumers: `event021_parent_review_event6_secondary_front`, `event021_parent_refresh_event6_secondary_presence`, `event021_parent_review_secondary_front`, `event021_parent_review_registered_ordinary_fronts`, `event021_parent_close_secondary_front`, `event021_parent_refresh_ordinary_secondary_presence`, and `event021_parent_update_front_resolution_receipts`.
- Scenario and cleanup: ledger/candidate/provenance cleanup in `event021_parent_rollback_transaction`, `event021_parent_remove_scenario_target_tickets`, `event021_parent_scenario_record_frozen_state`, `event021_parent_freeze_scenario_plan`, `event021_parent_apply_frozen_scenario_plan`, `event021_parent_clear_scenario_plan_receipt`, and `random_civil_war_trigger_manual_scenario`.

These named groups are dependency boundaries, not approval of every working-tree line inside those functions.
In particular, exclude the external-war queue additions embedded in initialization, admission, rollback, and crisis cleanup, and exclude the three evolution-log callback changes for their separate metadata repair.
Keep existing committed entry points and signatures callable while migrating the bodies.
The two lifetime repairs below must be included in the owning function groups and companion API documentation.

Constants already committed cover the new ledger and provenance helpers.
No new tuning category or value is needed merely to close these names.
The working-tree constants removals are `random_civil_war_capacity.maximum_multifront_states`, `maximum_planned_fronts`, `maximum_force_divisions`, `random_civil_war_force.serious_division_count`, `severe_division_count`, `critical_division_count`, `one_state_division_count`, `air_share`, `navy_share`, and `event021_parent_tuning.maximum_major_belligerents`, `maximum_minor_belligerents`.
These removal hunks may accompany their fully migrated consumers, but are unnecessary for bare symbol closure and must not precede the consumer migration.
The new `random_civil_war_cluster_skip_reason.external_continuity_pending = 10` belongs to the separate external-war bundle.

No runtime hunk in shared `common/scripted_effects/chaosx_dynamic_effects.txt` is required by the inspected ledger helper references.
Its current dirty changes concern civilian population-loss accounting, which is outside this repair.
The relevant shared change is the owner API documentation index row `event021_exact_front_ledger` in `chaosx_dynamic_effects.md`.
Shared logger, logic, and settings source changes are not required for this literal dependency migration.
Keep their existing committed implementations as dependencies, rather than staging unrelated shared-file edits.

Required documentation travels with each new `.txt` as its companion `.md`, plus the affected parent effects, core effects, lifecycle effects, successor effects, parent-trigger contracts, and the ledger index row in `chaosx_dynamic_effects.md`.
The existing `event021_dynamic_front_ledger_repair_2026-10-03.md` should retain unresolved validation and any new lifetime findings until corrected.
No localisation, new asset, focus file, GUI rewrite, or spreadsheet mutation is needed to fix the literal dependencies identified by this audit.
Changes to player-facing management or active Evolution I remain parent-owned separate work.

## Separate working-tree dependencies that must not leak into the ledger commit

The dirty source also calls `event021_external_queue_blocks_new_crisis`, `event021_external_snapshot_predecessor`, `event021_external_post_adoption`, `event021_external_queue_receipt_valid`, `event021_external_snapshot_receipt_valid`, `event021_external_clear_queue`, and `event021_external_clear_queue_receipts`.
Their definitions are in uncommitted `021_random_civil_war_external_war_effects.txt` and `021_random_civil_war_external_war_triggers.txt`.
Publishing those callers alone would create the same class of source-closure failure as the sponsor incident.
If the owner includes those queue hunks instead of isolating them, the external effects, triggers, receiver events in `events/021_random_civil_war_external_war_events.txt`, and successor/on-action bridges become a separate required bundle.
Its event receiver IDs, eligibility, UI, and probability acceptance are not certified here.

The dirty mission resolver calls the new `event021_secure_rail_mission_target_valid` in parent triggers.
That belongs with its mission/decision and state-control hook repair, not the front-ledger dependency minimum.
The dirty `event021_country_can_resolve_sponsor_repayment` and sponsor decision changes are also separate from the committed narrow sponsor-trigger definition.
Changes to `event021_evolution_has_extra_active_actor` and `event021_evolution_has_active_event6_actor` are MTTH/eligibility consumers and require their own probability-auditor evidence before publication.
They are not required to make the three new helper files' literal names resolve.

## Source findings that affect a reviewed ledger commit

### L1: initial ledger row-count lifetime finding, corrected in source

At the initial reviewed working-tree revision, `event021_parent_validate_front_ledger_members` calls `event021_parent_validate_front_ledger_row_span`, then adds `event021_ledger_count` to `event021_ledger_expected_offset` at ledger source lines 292-293.
The row-span helper first creates `event021_ledger_count` at line 305.
There is no initialization in the member helper before that call.
Under the required conservative temporary call-frame model, the count is discarded on row-span return, so the offset accumulation cannot rely on the intended count.
This can reject an otherwise valid contiguous ledger or read stale caller scratch.
The owner should initialize the count in the member caller before each row-span call, document it as a caller-owned output, and recheck contiguous multi-row and single-row receipts with frame cleanup enabled.
This is a source contract defect, not an observed live failure.

### L2: initial secondary-transfer lifetime finding, corrected in source

At the initial reviewed source, `event021_parent_start_secondary_civil_war` calls `event021_parent_validate_secondary_transfer_receipt` at parent source line 4262 and consumes `event021_secondary_transfer_valid` in its gate at line 4265.
The receipt helper first creates that output at ledger source line 85 and writes success at line 140.
No Event 021 caller initializes the output before the first call.
Under conservative frame cleanup, a valid receipt's success output is lost before the war gate.
The owner should preinitialize this scalar in the immediate parent caller and include both the initial gate and the second revalidation call in its contract review.
The normal country army-ratio and global state-count outputs are persistent and do not have this particular return-lifetime defect.
This finding does not authorize a change to the ratio, eligibility, weight, or timing model.

## Bounded evolution-log metadata review

The reviewed selector is `common/scripted_effects/021_random_civil_war_evolution_log_effects.txt`, with companion documentation.
The same selector was read directly from the parent's proposed Git tree `b6d22378f4cc8669a79e65440cb36b98d0bb2962`, where its blob is `2a4cd4dc95a8e586ffb6fc707dfd693545794fa8`.
It uses already committed `random_civil_war_is_normal_human_country` and existing constants.
Its isolated dependency bundle is the new selector `.txt` and `.md`, the three parent callback actor-assignment replacement hunks, the caller-owned event ID/type initialization hunks, and the core effects documentation paragraph.
It needs no ledger, active-review driver, external-war, or shared logger edit.

The selector correctly checks equal lengths for the five arrays it indexes before traversal, rejects nonpositive front/crisis IDs and nonactive rows, and checks live human host and actor existence through the existing shared classifier.
It verifies actor active state, theater-registration flag, theater membership, and matching actor front/crisis IDs.
It selects the first verified row in the existing registry order.
It does not choose a random actor or change gameplay admission.

The parent callbacks now create `events_log_evolution_event_id` and `events_log_evolution_type` before `event021_prepare_evolution_log_context`.
The context helper's assignments therefore survive conservative return cleanup.
Each callback explicitly sets its stage and tier afterward.
The callbacks likewise create `events_log_evolution_has_actor = 0` before the selector.
Its success assignment survives return, while private selector temporaries need not survive.
Nested Evolution II/I and III/II callbacks establish their own context after the lower callback returns, which avoids reusing the lower stage's context.

No-actor handling is sound at the source level.
The selector resets the caller-owned actor indicator to zero even if a regular `events_log_evolution_actor` target was set earlier in the effect chain.
Committed shared `record_events_log_evolution_entry` at lines 1065-1098 requires both that target and an indicator greater than zero, and otherwise appends explicit no-actor values.
It resets the indicator at line 1100.
Regular-target cleanup is not needed or attempted.
Shared sanitization and recording remain in their existing owner file.

### M1: initial canonical-host identity finding, corrected in source

At the initial reviewed source, the selector's host branch proves a live active human country with the row's crisis ID, but does not require host front/theater registration or compare that row host with the actor's durable `random_civil_war_crisis_host_scope`.
The actor branch also omits its `random_civil_war_front_registered` receipt.
A malformed row whose host points to another active same-crisis participant can satisfy the current host test.
An active theater with a stale front-registration flag can likewise satisfy the actor test if its IDs remain.
The five-array length check cannot detect either mismatch.
This is a remaining metadata consistency risk, not a missing-helper or probability finding.
Before describing the selector as proving canonical host identity, the owner should verify the actor's durable host pointer against the row host, require the appropriate existing registration receipts, and recheck host-row, opposition-row, successor-host, mismatched-host, removed-registration, and no-actor cases.
Any successor-specific exception must follow the actual existing ownership contract.
No registration predicate or gameplay change was invented by this worker.
The parent reports ten passing actual-source unit methods against the proposed tree, including 14 invalid-actor cases, nine sponsor cases, stale targets, 1,002 rows, and three-callback storage.
This worker inspected the test methods in that Git tree without rerunning them or creating test artifacts.
The invalid-actor table tests the actor's theater-registration flag, but does not test its front-registration flag, canonical-host pointer equality, or the host's registration receipts.
Those reported tests therefore support the storage/no-actor review and the modeled cases without resolving M1.
The initial source-only verdict was that output storage and stale-target safety pass, while the stronger canonical-host identity claim remained unresolved.
The correction review below supersedes that verdict for the inspected current source.

## Source-only correction re-review on 2026-10-03

The parent requested this bounded read-only follow-up, with the existing unavailable MCP routes retained and no rerun requested.
Observed HEAD was `888e5045359e16e2a8616de3ed8ba576f2dbbe2d`.
The corrections were reviewed as working-tree source, without treating them as committed implementation.
Only this existing Markdown handoff was updated by the reviewer.

### M1 resolution

Status: corrected in source and source review passed.
The selector initializes private `event021_evolution_log_host_id` at line 26 and captures the validated registry row host's `THIS.id` at line 41.
Host front/theater registration and active-theater membership are required at lines 34-36.
The actor requires its front/theater registration and membership at lines 52-54.
At lines 57-61 its durable `random_civil_war_crisis_host_scope` must exist as a country and match the captured row-host country ID.
The actor's front and crisis IDs still match their row at lines 62-63.
The private host-ID storage is created in the selector before nested calls and consumed inside that same selector frame.
It is not an output that must survive selector return.
Caller-owned actor-indicator and event ID/type outputs retain the earlier passing lifetime review.
Stale-target no-actor safety remains intact.
The selector companion Markdown now documents both registration checks and exact durable host-pointer identity.

The current `.tools/test_event021_evolution_log.py` contains the new substituted-same-crisis-host rejection at lines 237-242 and matching successor pointer/registry acceptance at lines 244-250.
Its invalid-receipt table also adds missing actor front registration, missing host front/theater registration and membership, and missing canonical pointer.
The parent reports twelve passing methods and nineteen invalid metadata cases.
This reviewer inspected the current source methods and cases but did not rerun the suite.
Those modeled results remain separate from game execution, probability evidence, and automatic proof that the actual successor mutation always publishes those receipts correctly.
M1 is resolved within this selector's bounded source contract.

### L1 resolution

Status: temporary-output lifetime defect corrected in source and source review passed.
`event021_parent_validate_front_ledger_members` initializes `event021_ledger_count = constant:random_civil_war_value.zero` at ledger line 292 immediately before the row-span call at line 293.
The subsequent accumulation at line 294 therefore consumes caller-owned storage whose helper modifications survive conservative return cleanup.
The row-span helper assigns that output at line 306.
Initialization occurs once per row and does not reset the accumulated `event021_ledger_expected_offset`.
This closes the previously identified call-frame lifetime defect.
The ledger companion Markdown still needs to document the row-span count's caller-owned output storage requirement.
A contiguous-ledger scenario or engine pass was not rerun in this review.

### L2 correction review before the final guard was applied

Status at that review: temporary-output lifetime defect corrected in source and source review passed, final revalidation-to-mutation gate unresolved.
The starter initializes `event021_secondary_transfer_valid = constant:random_civil_war_value.zero` at parent line 4262 before its first receipt call at line 4263.
The first gate reads that caller-owned output at line 4266.
The second receipt call at line 4286 updates the same existing caller-owned storage, so another lifetime seed is not needed there.
The receipt helper resets validity on each call, including a failed second validation.

The inspected source then writes the pending army ratio at line 4287, calls `missiles_preflight_country_split` at line 4288, and enters the government branches without checking the second validity result.
The four engine mutations are at lines 4293, 4320, 4347, and 4373.
Thus the original L2 storage defect is resolved, while a false second result still has a source path to mutation under the already-entered first gate.
This is not a claim that live source state changed between the two checks.
It is a missing fail-closed consumption of the explicit revalidation result.
The owner should gate the common mutation path, including its final fallback government branch, on the updated validity output and preserve rejection cleanup for failure.
Adding a validity condition only to the first three ideology branches would still allow the fallback branch to mutate.
The existing outer `else` at lines 4402-4411 is attached to the first receipt gate and does not handle failure of the second check after that gate has been entered.
This remaining gate must be reviewed after the owner patch before clearing the secondary mutation path.
The ledger companion Markdown also still needs the receipt output's caller-preinitialization contract.

| Current re-review source | SHA-256 |
| --- | --- |
| `common/scripted_effects/021_random_civil_war_evolution_log_effects.txt` | `629f5605bbf0732c2d0b86c16948e36c782ab2e5cb37b926e2d8f8d415c2cdc8` |
| `common/scripted_effects/021_random_civil_war_front_ledger_effects.txt` | `64ae170001403e36eb3ce3fd4809394ddeca5deb24f137d6e45f6ab4d7e8775e` |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `4413e207da9e7235fb20a45689ccb184f09674cfea0badf57138307c4013aa2b` |
| `.tools/test_event021_evolution_log.py` | `4b4ae6d18a2bc43cd93331ec5b88a225ae7599c51c926e607cdabff27c548ae7` |

The initial committed dependency audit is unchanged by this bounded re-review.
Broader probability and native tag-capacity evidence remain pending.
No MCP, game, balance, full ledger, active Evolution I, or full Event 021 acceptance is implied.
No source edits, commits, implementation simplifications, or fallbacks were made by this reviewer.

## Final secondary-preflight source review

The parent supplied commit `8fc6276c7fe4a7ea772a959069b3482d00902d45` for M1 and its twelve-method source tests.
This reviewer inspected the committed selector's host-ID, registration, and durable-pointer checks directly from that Git object.
The committed selector blob is `f60ea60c698cf4b3649afd063a6913f6e1a2deda`.
M1 remains resolved within its bounded selector contract, with the parent-reported test results retaining source-model status.
The current resume packet `docs/plans/021_random_civil_war_plans/resume_packet_2026-10-03_dynamic_repair.md` was read as the parent handoff.
Its pending final-boundary review is addressed here.

The first source read in this follow-up had both explicit validity seeds, before the initial call at parent lines 4262-4263 and before the final call at lines 4286-4287.
Its parent source SHA-256 was `ec5ed15cff2d8be4fd8e040671345045842d975a6b4bfca6b83ab8dbc980540e`.
The final output was still unconsumed by a guard in that revision.

The exact intermediate loader, `event021_parent_load_planned_secondary_front` at parent lines 2403-2435, copies the pending size, state count, army/navy/air ratios, archetype, goal, and anchor target from the selected row.
It does not modify plan readiness, the pending secondary front ID, the source country front ID, the plan's IDs/source IDs/offsets/counts/state entries/force-division entries, current ownership/control, transfer markers, or live division count.
These are the inputs used by `event021_parent_validate_secondary_transfer_receipt` at ledger lines 84-148.
The intervening country/global ratio assignments likewise do not alter those predicate inputs.
Both calls execute in the same source country, and both save the same receipt-source target.
Consequently, this source trace does not demonstrate a loader-induced true-to-false validity transition within the current synchronous immutable-plan contract.

This narrows the earlier finding.
An unconsumed false final result has a path to mutation in the unguarded revision, but this worker did not establish a reachable current-loader case that produces that false result after a true first check.
The extra guard is defensive enforcement of the explicit revalidation API, not proof of an observed race, live receipt corruption, or newly demonstrated invalidating loader.
The loader's emitted ratio and anchor parameter semantics remain separate from the receipt helper's state/force predicate and were not balance-validated here.

The direct `missiles_preflight_country_split` body was also read at `032_missiles_operations_effects.txt:5337-5380`, with its immediate abort/cleanup helpers at `4820-4829` and `4831-4914`.
It publishes missile-specific split/site receipts and can abort and clean an active missile operation.
It is not a consumer of `event021_secondary_transfer_valid` and cannot serve as the missing Event 021 guard.
This limited read does not certify every transitive missile helper's behavior or engine-side callbacks.
The missile source SHA-256 was `14ee6b64cf792fc2e983e3901f158992c25db3a9a88420572156b74bd6f24c34`.

The parent applied the common guard during this review.
The final inspected parent source SHA-256 is `a83b6789cb013cde98bfc3935bc3d884ae37ae48058c3811af68bce3174c7e8a`.
At lines 4288-4289, a fresh `if.limit` requires `event021_secondary_transfer_valid = constant:random_civil_war_value.one` after the second call.
It contains the pending army-ratio publication, `missiles_preflight_country_split`, and the complete four-government native mutation chain, including its final fallback branch.
The final rejection branch at line 4400 and the initial rejection branch at line 4408 call `event021_parent_reject_secondary_transfer`.
That helper at lines 4414-4424 preserves the previous initial rejection cleanup's pending-force clearing, rejection flag, pending flag/target release, pending IDs/goal/archetype clearing, and route-prepared flag clearing.
The existing post-attempt pending-force and marker cleanup remains outside the guarded mutation block.

A bounded read-only token-tree check on the actual current starter found all four `start_civil_war` blocks and its one missile-preflight call under that exact final validity guard.
It also found one final and two total rejection-helper calls in the starter.
No scratch file, source edit, or execution of Clausewitz/native effects was used for this check.
The new rejection helper definition is present in the same parent source and belongs in the coherent ledger publication bundle.
This check provides task-specific source control-flow evidence, not engine execution or full dependency revalidation.

Status: both L2 seeds and the common final mutation guard pass bounded source review.
L1 remains resolved, with ledger source SHA-256 `64ae170001403e36eb3ce3fd4809394ddeca5deb24f137d6e45f6ab4d7e8775e`.
The ledger companion Markdown now documents caller-owned count/validity storage, both receipt seeds, the common final guard, and shared rejection cleanup.
Its reviewed SHA-256 is `af35aa0da15d1176aeae303ebed7d7703803e8195ec79ef98578fc3f46f48600`.
Those documentation obligations from the earlier correction review are satisfied in the inspected working tree.
The MCP gap was retained without rerunning unavailable routes.
Broader probability, tag capacity, active Evolution I, and Event 021 acceptance remain unchanged and pending.
Only this handoff was updated, with no source edit, commit, simplification, or fallback by this reviewer.

### Final formatted AST and rejection-scope verdict

The parent's final formatted working-tree starter was inspected again after the inner-body indentation pass.
Its SHA-256 is `0dbd60bf8259f6848413f84db79f988d6d29cabb26fa09c283066a7a03e1df61`.
This supersedes the prior pre-formatting parent identity `a83b6789cb013cde98bfc3935bc3d884ae37ae48058c3811af68bce3174c7e8a` for the final bounded verdict.
The read-only actual-source token-tree check again found four of four native splits and one of one missile-preflight calls beneath the common post-second-call validity guard.
Both initial and final failure branches contain a direct `event021_parent_reject_secondary_transfer = yes` call.
Their enclosing `if` and `else` control blocks do not enter another country scope, so rejection remains on the starter's same serial source country.
The helper's country rejection flag consequently belongs to that source, while global receipt cleanup retains its explicit global targets.

The extracted helper's parsed effect sequence was compared directly with the original starter's outer `else` from committed Git object `c3c91450:common/scripted_effects/021_random_civil_war_parent_effects.txt`.
The sequences are equal after excluding comments and whitespace.
That comparison covers all nine original cleanup statements in their original order, including the pending-force helper call, country rejection flag, pending flag, both global targets, all three pending metadata variables, and route-prepared flag.
This is stronger preservation evidence than a matching list of effect names alone.
The existing post-attempt force and marker cleanup remains outside the common native guard and retains its prior condition and clearing operations.
Repeated pending-field and target clears introduce no new grants or mutation in this inspected source path.

Final verdict: M1, L1, L2 caller-storage handling, and the final secondary-preflight mutation/rejection boundary pass bounded source review.
The new same-file rejection helper and its call sites remain part of the uncommitted coherent ledger bundle.
The verified committed M1 metadata repair is separate from that bundle.
No confirmed loader-induced invalidation was found, and the common guard enforces rejection if the final receipt result is false.
This review makes no engine, probability, native tag-capacity, active Evolution I, or full Event 021 completion claim.

The parent subsequently added uncommitted `.tools/test_event021_front_ledger_contract.py`, reviewed SHA-256 `7105196b7fada5bb14f2c229a6bb6b924d0d27861b5ca530621813d4a95d8cb6`.
This worker read its three actual-source methods without running it or creating Python cache artifacts.
The row-count method executes the caller seed, actual row-span helper, and offset accumulation for contiguous counts `[1, 2]`, offsets `[0, 1]`, and three state entries using the conservative helper-cleanup model.
The guard method checks the actual post-second-call guard, all four guarded native split blocks, missile preflight, and the direct false-result rejection branch, then evaluates the guard for validity zero and one.
The rejection method checks both shared-helper call sites and selected cleanup statements.
The independent Git-object AST equality check above supplies full nine-statement cleanup preservation beyond that method's selected assertions.
The current parent source hash remained `0dbd60bf8259f6848413f84db79f988d6d29cabb26fa09c283066a7a03e1df61` when those methods were inspected.
The parent reports all three methods and the twelve metadata methods passing.
That is recorded as parent-run source-model evidence, not an independently rerun suite or native force, rollback, campaign, or engine proof.

## References and MCP blockers

Installed paths in this report are rooted at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Repository paths are rooted at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/`.

| Reference read | Relevant sections and SHA-256 revision |
| --- | --- |
| Offline Data structures | Event targets `263-292`, temporary-variable types `435-442`, arrays `1069-1077`, iteration `1210-1221`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline Effects | Scripted effects `4683-4696`, native fields `1504,3614`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline Triggers | Scripted triggers `2359-2377`, vanilla `has_same_ideology` entry `2536`, revision `abc51ad18a2c46e46d47baa795c5a840ebaF7c4ae3e777426c64a9f4c0c0ce06` |
| Installed effects documentation | Native exclusions above, array iteration `4279-4312`, meta effect `4833-4851`, targets `6496-6513`, civil war `8030-8059`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed triggers documentation | Native heading index, `has_variable` `5006-5013`, meta trigger `6404-6422`, revision `7d27ed77ddadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed script concept documentation | Script constants `216-224`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed constants schema | `common/script_constants/documentation.md:1-15`, previously recorded revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

The initial connected inventory exposed `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` schemas.
The direct narrow source request for `event021_sponsor_repayment_receipt_valid` returned `MCP tool hoi4_agent_tools/hoi4.source_lookup is not available to the model`.
The narrow event trace and event reference-context requests returned the same unavailable-to-model error for their respective routes.
The first event request used the standard padded root name, so it did not inspect the actual `chaosx.nr21.1` root.
The request failed before producing any domain result.
The narrower retry reduced the source request to one definition and eight lines, but the route was then absent as a callable function, producing `TypeError: tools.mcp__hoi4_agent_tools__hoi4_source_lookup is not a function`.
At that point `ALL_TOOLS` contained no `hoi4_agent_tools` routes.
The attempted batch stopped before its targeted reference search and narrower event request could dispatch.
No reference-read citation, inspect artifact, render, comparison, continuation URI, source revision, or engine verdict was returned by this session.
Local reference reads are therefore recorded as documentation evidence under the reference-route gap, while MCP event/helper evidence remains blocked.
No `helper_expansion`, job, native task, or unverified health/client route was used.

Earlier parent evidence in `event021_dynamic_front_ledger_repair_2026-10-03.md` includes a partial render revision `82b429b79b5bb8deae56efb4446b4dffb418556fba66ce3b30b8b469d3fdb003`, with deferred helper/lifecycle coverage and only 64 of 386 paths inline.
It also records 600-second probability/inspect/validation timeouts.
Those historical artifacts and arithmetic fixtures were not rerun or promoted into current-helper engine proof here.
No numeric balance or weighted eligibility conclusion is made by this worker.
Probability changes and the existing MTTH consumer migration remain subject to `chaosx_ai_probability_auditor` and identical-scenario comparison.
The missing live routes prevent providing that evidence here.

## Reviewed working-tree source identities

| Source | SHA-256 at bounded review |
| --- | --- |
| Dynamic front candidates | `c64207a9fa9ea19178243173447e2d94578d641dc2e4d8785fa013ccc7561d3e` |
| Front ledger | `83d1a71fcd8fc747b343cb41efc5d4fb1d41bbe55812ce84acebee247978182c` |
| Active-evolution foundation | `325c414c91272a5b1df5970acb603f8763f778bd5ab6a73c925f1d22d4146c23` |
| Parent effects | `25557668f2a6f8481984957593ee388261ef6805dcbc2303c387be89be91bd1a` |
| Core effects | `6d9077920f2045783ffbcac00dd20f6b3e403a3070e7e7608f13da41bc0052d7` |
| Parent triggers | `57bd2b2dc3169d6105380a29667a8892528b0d4dfb98a4cf37b6854b78aafa46` |
| Evolution-log selector | `32ebb89c6e1558a8ad1dcc76188c5c02619f1064f5992918c221fa4f4c6e43be` |

## Validation, omissions, and ownership

Completed checks were committed-versus-working-tree definition separation, the known literal transitive helper walk, the independent committed assignment check for all working-tree-only helper names, Event 021 constant membership, exact vanilla-helper resolution, native-field classification, source call-path review, and conservative temporary-output lifetime review.
No generated report program or scratch source file was added to the repository.
No game was launched, no logs were requested or searched, no runtime fixture was fabricated, and no shared index was touched.
The report preserves the source-only status of L1, L2, and M1.
Engine validation, exhaustive dynamic package expansion, scenario probability comparison, current live receipts, stockpile/unit rounding, active-war Evolution I acceptance, GUI/focus/map consumer validation, and full Event 021 completion were not certified.
There was no implementation simplification or fallback because this worker made no implementation change.
The reporting limitation is unavailable mandatory MCP evidence, not substituted engine proof.
Skills used were `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or changed.
The parent owns corrections, re-review, coherent publication, and the continuing Event 021 implementation.
