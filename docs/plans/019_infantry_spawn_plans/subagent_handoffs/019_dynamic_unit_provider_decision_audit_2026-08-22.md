# Event 19 Dynamic Unit Provider Decision Audit

Date: 2026-08-22.

Scope: The Event 19 decision-only infantry spawn management surface after the dynamic provider and equipment migration.

Owner: Decision and mission audit subagent.

## Outcome

The initial findings-only pass is retained below as the baseline audit. The coordinated decision-only remediation was subsequently applied to the bounded Event 19 files and is recorded in the superseding status section at the end of this handoff.

The remediation preserves the dynamic provider transaction, selected-lot dynamic equipment accounting, affordability, settlement, demobilization salvage, Provider 508 sequencing, derivative cleanup, route locks, and AI action reuse while correcting the player-facing cost, icon, phasing, and provider-payment gate defects identified below.

The exact four-type presentation rule remains bounded by two truthful-obligation surfaces: standardization can consume seven exact material classes, and exact settlement can show six standard classes plus provider-owned dynamic rows. The handoff records this as a concrete design-approval blocker rather than concealing an obligation or changing Event 19 balance semantics.

The accepted Event 19 surface remains explicitly decision-only. No scripted GUI was created, and no unrelated interface was changed.

## Files and identifiers audited

Gameplay files inspected:

- `common/decisions/019_infantry_spawn_decisions.txt`.
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`.
- `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt`.
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt` as a cleanup dependency.
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` as the Provider 508 callback owner.
- `common/scripted_effects/016_alien_infantry_api_effects.txt` as the Provider 508 debit, commit, and rollback API owner.
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`.
- `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt`.
- `localisation/english/019_infrantry_spawn_l_english.yml`.

The scoped gameplay files already had concurrent working-tree modifications. I preserved unrelated hunks and applied only the bounded Event 19 remediation listed in the superseding status section below.

Core decision and category identifiers:

- `infantry_spawn_formation_management_category`.
- `infantry_spawn_review_formation_ledger`.
- `infantry_spawn_cycle_anomalous_family_decision`.
- `infantry_spawn_settle_selected_lot_obligations`.
- `infantry_spawn_open_standardization_cycle`.
- `infantry_spawn_supervised_demobilization`.
- `infantry_spawn_request_selected_anomalous_family`.
- `infantry_spawn_open_selected_family_cantonment_decision`.
- `infantry_spawn_sustain_selected_family_decision`.
- `infantry_spawn_seal_selected_family_breach_decision`.
- `infantry_spawn_disperse_selected_anomalous_lot_decision`.

Core dynamic accounting identifiers:

- `infantry_spawn_exact_dynamic_equipment_token_entries`.
- `infantry_spawn_exact_dynamic_equipment_amount_entries`.
- `infantry_spawn_clear_exact_profile_totals`.
- `infantry_spawn_add_current_dynamic_equipment_to_exact_totals`.
- `infantry_spawn_evaluate_dynamic_equipment_affordability`.
- `infantry_spawn_apply_dynamic_equipment_totals_to_country`.
- `infantry_spawn_refresh_selected_lot_exact_obligations`.
- `infantry_spawn_apply_exact_profile_totals_to_country`.
- `infantry_spawn_build_exact_teardown_salvage`.
- `infantry_spawn_forfeit_remaining_lot_obligations_for_cleanup`.

Core request transaction identifiers:

- `infantry_spawn_snapshot_management_request_payment_resources`.
- `infantry_spawn_snapshot_management_request_transaction`.
- `verify_family_pre_payment_equipment_balances`.
- `verify_family_transaction_equipment_balances`.
- `rollback_management_request_transaction`.
- `execute_selected_family_train_or_spawn_unlocked`.

Provider 508 identifiers:

- `chaos_unit_family_provider_508_event19_materialize_landing`.
- `chaos_unit_family_provider_508_event19_commit_landing`.
- `chaos_unit_family_provider_508_event19_rollback_landing`.
- `alien_infantry_spawn_landing_cohort`.
- `alien_infantry_commit_event19_landing`.
- `alien_infantry_rollback_event19_landing`.

The provider registry contains Event 19 providers `501` through `514`, `518`, and `520` through `523`.

## Baseline severity-ranked findings (pre-remediation)

### High: dynamic exact obligations are not visible in settlement cost text

The settlement mechanics persist exact custom equipment obligations in the aligned country arrays `infantry_spawn_exact_dynamic_equipment_token_entries` and `infantry_spawn_exact_dynamic_equipment_amount_entries`.

`infantry_spawn_refresh_selected_lot_exact_obligations`, `infantry_spawn_evaluate_dynamic_equipment_affordability`, and `infantry_spawn_apply_dynamic_equipment_totals_to_country` use those arrays for preflight, payment, and application.

`infantry_spawn_selected_lot_exact_obligation_cost`, `infantry_spawn_selected_lot_exact_obligation_cost_blocked`, and `infantry_spawn_selected_lot_exact_obligation_cost_tooltip` only print the scalar standard equipment, chassis, fuel, train, manpower, row-count, and debt variables.

They never iterate or summarise the dynamic token and amount arrays, so a player can be shown an affordable-looking or blocked-looking settlement without seeing the custom equipment that the action will consume.

This is directly material for Providers 503, 504, 505, 506, 507, 508, 509, 510, and 522, and for any future provider that publishes custom tokens.

Recommended owner and fix: coordinate `common/scripted_effects/019_infantry_spawn_management_effects.txt` with `localisation/english/019_infrantry_spawn_l_english.yml` to expose a compact dynamic obligation summary that uses the provider token presentation and registered texticons, or clearly states a provider-specific ledger obligation when no stockpile debit occurs.

### High: visible costs exceed the four-spendable-type budget

The ordinary request cost keys `infantry_spawn_field_request_cost`, `infantry_spawn_mobile_request_cost`, `infantry_spawn_territorial_request_cost`, `infantry_spawn_specialist_firepower_request_cost`, `infantry_spawn_numbers_request_cost`, `infantry_spawn_discipline_request_cost`, `infantry_spawn_firepower_request_cost`, `infantry_spawn_mobility_request_cost`, and `infantry_spawn_anything_request_cost` present political power, command power, army experience, infantry equipment, support equipment, trucks or motorized equipment, trains, fuel, and manpower across the request path.

The current ordinary request profiles expose seven or more distinct spendable types on a single player action even where the exact payment code is correct.

Recommended owner and fix: reduce each visible request to a maximum of four spendable types or move non-spendable context into a separate requirement line, then align the decision `custom_cost_text`, `custom_cost_trigger`, payment effects, and AI gates.

### High: provider custom equipment names lack icon-first cost presentation

The provider presentation chain is wired, but these localisation profiles contain literal or non-texticon equipment labels: `infantry_spawn_family_sustainment_cost_profile_coal_golem`, `infantry_spawn_family_sustainment_cost_profile_clone_infantry`, `infantry_spawn_family_sustainment_cost_profile_autonomous_robot`, `infantry_spawn_family_sustainment_cost_profile_paleogenetic_creature`, `infantry_spawn_family_sustainment_cost_profile_xenobiological_organism`, `infantry_spawn_family_sustainment_cost_profile_alien_infantry`, `infantry_spawn_family_sustainment_cost_profile_portal_raider`, `infantry_spawn_family_sustainment_cost_profile_temporal_guard`, and the corresponding request profiles.

Existing interface definitions cover some of these assets, including `GFX_alien_laser_weapon_equipment_medium`, `GFX_autonomous_robot_equipment_medium`, `GFX_coal_golem_equipment_medium`, and `GFX_archetype_clone_equipment_medium`, but no inspected Event 19 interface definition covered all paleogenetic, xenobiological, portal, or temporal equipment labels.

Recommended owner and fix: use registered texticons for every displayed spendable custom equipment value and route missing icon definition work through the parent and the appropriate asset/interface owner; do not add a new GUI or unrelated interface here.

### High: category cognitive load is above the accepted decision-only limit

The single `infantry_spawn_formation_management_category` contains approximately forty-one decision identifiers before its eleven mission identifiers, including audit, lot records, integration, supply, movement, demobilization, request, claimant, anomalous-family, achievement, and cooldown actions.

Evolution III and Evolution IV states can expose overlapping ordinary actions, selected-family actions, and request actions, while achievement and mission flags add further visible cards.

The accepted decision surface has no runtime GUI tabs or phase frame to partition these actions. This violates the six-primary-action guidance in realistic active states and makes the player scan a wall of unrelated controls.

Recommended owner and fix: phase or hide action groups using existing state flags and lifecycle requirements, retaining the decision-only surface; do not recreate the removed scripted GUI.

### Medium: standardization cost is also raw prose and label-heavy

`infantry_spawn_standardization_cycle_cost`, `infantry_spawn_standardization_cycle_cost_blocked`, and `infantry_spawn_standardization_cycle_cost_tooltip` print raw labels such as `Rifles`, `Artillery`, `Support`, `Trucks`, `Anti-Tank`, `Anti-Air`, and `Fuel` rather than icon-first values.

Standardization is limited to ordinary profiles, so this does not cause the dynamic provider omission above, but it still fails the repository cost-display rule and adds to the category's text density.

### Medium: direct probability evidence is partial, not a balance proof

The source inspection found forty decision candidates, but the pool was not complete and the adapter did not normalize the meta-dispatched provider family pool.

A direct evaluation with scenarios `ordinary_evolution_ii` and `anomalous_evolution_iv` returned `PROBABILITY_ANALYZED_PARTIAL`, fifty unresolved candidate/scenario outcomes, and a warning that `infantry_spawn_request_selected_anomalous_family` was never eligible in the synthetic scenarios.

That warning is not treated as a confirmed code defect because the scenario omitted runtime registry and selected-lot state that the decision requires.

The named `chaosx_ai_probability_auditor` route was not callable in this runtime, so a dedicated auditor comparison pass remains blocked.

### Low: historical GUI localisation names remain in the file

The localisation file still contains `infantry_spawn_muster_gui_*` keys, but the accepted specification removes the runtime scripted GUI and the inspected decision/effect paths do not instantiate it.

This is stale naming and not a runtime defect in this audit. Remove or rename only as part of a deliberate localisation cleanup after confirming no historical documentation or compatibility consumer needs the keys.

## Decision-category lifecycle notes

`infantry_spawn_ordinary_management_category_is_relevant` gates the category through active-country, transaction-idle, non-derivative, non-scenario, non-takeover, and non-achievement-revolt checks, then delegates to `infantry_spawn_ordinary_management_crisis_is_active`. The same gate is used by the claimant category, so a completed takeover or achievement-marked claimant or derivative revolt hides both management categories even if another claimant row remains; peaceful closeout still waits for the ordinary obligations, claimants, and operations to clear.

The crisis trigger considers unresolved generation, active lots, unaccounted formations, claimant state, deferred actions, prefire state, audit, standardization, demobilization, training, muster districts, integration staff, specialist preservation, prototype state, rail state, request cooldown, and related management flags.

The category therefore disappears when all management work is closed during peaceful closeout, while takeover and achievement-marked claimant or derivative revolt are immediate terminal relevance stops; the broad OR trigger intentionally keeps it alive for many independent state families before those outcomes.

The muster-board decisions additionally require Evolution III and no world-end state through `infantry_spawn_muster_board_is_available`.

The category has no dedicated runtime GUI, no separate tabs, and no compact phase summary; the lifecycle is decision visibility and mission flags only.

## Cognitive-load notes

Visible primary actions are distributed across audit, records, integration, supply, movement, demobilization, requests, claimant, anomalous-family, and achievement groups inside one category.

There are eleven mission cards in the current source: `infantry_spawn_achievement_combat_trial_mission`, `infantry_spawn_formation_roll_call_mission`, `infantry_spawn_standardization_cycle_mission`, `infantry_spawn_supervised_demobilization_mission`, `infantry_spawn_training_cycle_mission`, `infantry_spawn_muster_districts_mission`, `infantry_spawn_officer_search_mission`, `infantry_spawn_specialist_preservation_mission`, `infantry_spawn_prototype_maintenance_trial_mission`, `infantry_spawn_rail_corridor_mission`, and `infantry_spawn_request_cooldown_mission`.

Most missions are state-gated and non-selectable, which prevents arbitrary duplicate starts, but overlapping active states can still put far more than the usual one-to-three active mission cards in the same category.

The selected-lot index, lot status, obligation row count, debt value, scalar equipment totals, manpower, and cooldown values have clear mechanical significance in source triggers, but the player-facing exact cost text does not explain or display custom provider token amounts.

The provider family name and request or sustainment profile are dynamically supplied through `get_presentation`, and a coverage check found all twenty-six inspected provider presentation token references localised.

The text density is highest in the exact settlement cost strings and in request profiles that combine administration overhead with provider-specific costs in one paragraph.

## Mission quality notes

`infantry_spawn_achievement_combat_trial_mission` is owned by the achievement trial state, uses the achievement trial timeout constant, and cancels the trial on timeout or cancellation.

`infantry_spawn_formation_roll_call_mission` is owned by the selected lot audit, uses the audit duration constant, and defers or completes the selected-lot audit on timeout.

`infantry_spawn_standardization_cycle_mission` is owned by selected-lot standardization, uses the standardization mission duration, and invokes the standardization timeout completion path.

`infantry_spawn_supervised_demobilization_mission` is owned by selected-lot demobilization, uses the demobilization duration, and invokes the demobilization timeout completion path.

`infantry_spawn_training_cycle_mission` is owned by selected-lot training, uses the training duration, and invokes the training timeout completion path.

`infantry_spawn_muster_districts_mission` is owned by country muster institutions, uses the muster-district duration, and invokes the district timeout path.

`infantry_spawn_officer_search_mission` is owned by country officer search, uses the officer-search duration, and invokes the officer timeout path.

`infantry_spawn_specialist_preservation_mission` is owned by selected-lot specialist preservation, uses the specialist-preservation duration, and invokes the specialist timeout path.

`infantry_spawn_prototype_maintenance_trial_mission` is owned by the selected prototype, uses the prototype duration with the source clamp, and invokes the prototype timeout path.

`infantry_spawn_rail_corridor_mission` is owned by the selected lot and origin state, uses the rail-corridor duration, and invokes the rail timeout path.

`infantry_spawn_request_cooldown_mission` is owned by the family request cooldown state, uses the dynamic cooldown duration, and finishes the cooldown on timeout.

The mission starters use state flags and action gates to suppress duplicate starts, and the timeout paths are distinct from success paths. The main quality issue is presentation density rather than a confirmed missing timeout, failure, or cleanup path.

## Dynamic equipment, cost, and requirement audit

`infantry_spawn_clear_exact_profile_totals` resets scalar exact totals and clears both persistent dynamic equipment arrays before each selected-lot rebuild.

`infantry_spawn_add_current_dynamic_equipment_to_exact_totals` collapses repeated provider tokens into aligned token and amount arrays.

`infantry_spawn_evaluate_dynamic_equipment_affordability` checks `num_equipment@[EQUIPMENT]` against every dynamic amount, and `infantry_spawn_apply_dynamic_equipment_totals_to_country` applies the exact amounts through the meta-dispatched equipment effect.

Settlement and teardown preflight reject malformed or unresolved provider tokens, so custom obligations are not silently converted to ordinary infantry equipment.

Provider 508 consumes exactly two thousand laser units inside the deferred landing API, then commits only after the outer transaction verifies the created formation. A failed outer transaction rolls back the exact debit once; a successful commit deliberately retains the debit and records the landing.

Request snapshots capture political power, command power, army experience, manpower, fuel, ordinary equipment, and provider-published custom equipment before payment and again before the outer transaction.

The provider callback is refunded only after a successful provider payment followed by a later transaction failure. Provider 508's payment callback itself does not debit; its deferred materialization callback owns the exact debit. This sequencing is internally consistent.

Ordinary demobilization and specialist salvage are zero-balance preflight paths for outstanding obligations, while cleanup and prototype-cannibalization paths explicitly allow forfeiture. No free-unit, double-refund, or repeated-equipment-farming loop was found in the inspected sequence.

The source check found zero missing localisation keys among seventy-one decision custom-cost or custom-tooltip references and zero missing keys among twenty-six provider presentation references.

## AI validity and route-lock notes

`infantry_spawn_run_anomalous_family_ai` rebuilds the same provider view used by player actions, selects the highest-pressure valid family, and calls the same management or train/spawn transaction effects after the same gates.

Containment and dispersal are selected only under critical pressure, while sustainment, cantonment, restriction, and liaison are selected under lower pressure when their player-facing gates pass. Training or spawning is additionally restricted to war or strong-control states.

All nineteen provider IDs have the expected thirteen Event 19 callbacks, and Provider 508 additionally exposes materialize, commit, and rollback helpers.

The inspected registry modes are `trainable_and_spawnable` or `spawn_only`; no train-only provider was found, so the muster view's initial `can_spawn` filter does not currently hide a train-only family.

Derivative management is proof-gated through `infantry_spawn_derivative_dispatch_provider_cleanup`; Provider 508 setup and cleanup grant and revoke the expected contact source.

The AI and route-lock source review found no invalid target or dead-provider route. Detailed probability balance remains unresolved because the named auditor route was unavailable and the direct MCP evaluate was partial.

## MCP evidence and blockers

`hoi4.event_inspect` scanned `chaosx.nr19.1` with helper expansion and returned `EVENT_INSPECTED_PARTIAL` with structural diagnostics `MCP_INLINE_FILES_TRUNCATED`; the artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a02b9a253cd26f814944d2c30b62b472fe1e57cb005fb96774477186b53ac989/2378b2dd33aad06f8e9ab06df4e633161a771b80abb10a7826f882bf48671d9d/event-scan-43f28961e452.json`.

`hoi4.event_render` rendered the downstream neighborhood and returned `EVENT_RENDERED_PARTIAL` with deferred event analysis; manifest artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/269da7290da7342037da1db3932368aa5c258d63bc98fc4f5f259bbcb6435c71/1cdc50e8fa1dd7eab1a493a2a9bd0a910301799ba93700b4c8a31cefadb52275/event-neighborhood-43f28961e452-manifest.json`.

`hoi4.probability_inspect` on `common/decisions/019_infantry_spawn_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20dd5b1c4762314e55b412335e8913c61118bd0f437e22808b866c98fdac57ba/e273c8e5a5dda1e65c3d5d56d1f43158047d6971a020fb0c9b10293a64897019/probability-inspect-f1f83c730d7d.json`.

The direct scenario evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, with JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8b7ede54cb12217098387bedc6573f6c099ccc3be824a4ddae484159102c92/a3501bb77565216b29a48c5ad69c64c891adf5b024e1943d2bc71de20b91e3fa/probability-aa7813c8d5f747d47e280fc1.json` and fifty unresolved outcomes.

The exact blocker is that the named `chaosx_ai_probability_auditor` subagent route was not exposed as a callable tool in this runtime. The direct MCP adapter also does not fully normalise the meta-dispatched provider pool, so its warning about `infantry_spawn_request_selected_anomalous_family` was recorded as uncertainty rather than a source defect.

GUI inspection and rendering were intentionally not run because Event 19 has no accepted runtime scripted GUI or decision-owned layout in scope. Running GUI rewrite or recreating a GUI would violate the task boundary.

## Baseline recommended follow-up fixes (superseded by the remediation section below)

- Parent-owned coordinated localisation and helper change: add an icon-first dynamic equipment summary for `infantry_spawn_selected_lot_exact_obligation_cost`, `infantry_spawn_selected_lot_exact_obligation_cost_blocked`, and `infantry_spawn_selected_lot_exact_obligation_cost_tooltip`.
- Parent-owned cost redesign: bring the ordinary request decision cost surfaces to no more than four spendable types and keep requirements separate from consumed resources.
- Provider/interface owner follow-up: replace literal custom equipment labels in the `infantry_spawn_family_request_cost_profile_*` and `infantry_spawn_family_sustainment_cost_profile_*` payloads with registered texticons, adding missing icon definitions only through the appropriate asset/interface route.
- Parent-owned category lifecycle pass: phase or hide low-priority decision groups so realistic states do not expose more than six primary actions and eleven simultaneous mission cards.
- Probability-auditor follow-up: rerun named scenario baseline and compare passes through `chaosx_ai_probability_auditor` after a callable route is available, using complete registry, selected-lot, cooldown, and evolution state.

## Validation and skipped validation

Meaningful checks run were MCP event inspection and rendering, MCP probability source inspection and partial scenario evaluation, provider callback coverage, dynamic-array source tracing, provider mode and route-lock enumeration, decision-localisation key coverage, and provider presentation key coverage.

The source checks found all referenced decision cost or tooltip keys and all inspected provider presentation keys, and found thirteen of thirteen expected callbacks for each of the nineteen provider IDs.

Live HOI4 execution, save-state transaction simulation, and gameplay GUI capture were not run because the repository instructions assign live consumer validation to the user and the accepted surface has no runtime scripted GUI.

The initial findings-only pass made no gameplay patch; the coordinated before/after behavior and changed files are recorded in the superseding remediation section below.

## Baseline remaining issues and simplifications (superseded status below)

The audit is incomplete for detailed probability balance until the named auditor route and a complete provider-aware scenario state are available.

The cost and category findings were queued during the initial findings-only pass; they are resolved or explicitly bounded in the superseding remediation section below.

No unrelated interface, shared GUI, event log, provider callback, or gameplay balance file was changed.

## Superseding remediation and re-audit status (2026-08-22 continuation)

The baseline findings above describe the pre-remediation source state. The following section is authoritative for the current working tree and distinguishes resolved findings from remaining evidence or design blockers.

### Resolved findings

- Dynamic exact settlement obligations are now rebuilt from provider-owned data in common/scripted_effects/019_infantry_spawn_management_effects.txt. infantry_spawn_clear_exact_profile_totals clears the persistent token, amount, and icon arrays and resets the display cursor. infantry_spawn_add_current_dynamic_equipment_to_exact_totals collapses repeated provider tokens into aligned token and amount arrays. infantry_spawn_build_exact_dynamic_equipment_icon_tokens derives each token's token:[EQUIPMENT]_text_icon key through the provider token, without an Event 19 family or equipment switch. infantry_spawn_evaluate_dynamic_equipment_affordability checks every dynamic amount against the country stockpile. infantry_spawn_apply_dynamic_equipment_totals_to_country is called by infantry_spawn_apply_exact_profile_totals_to_country, so settlement payment, teardown salvage, and cleanup use the same exact arrays.
- The selected-lot settlement strings now include the standard obligation rows and the recursive provider-owned equipment rows through GetInfantrySpawnExactDynamicEquipmentCost. The scripted localisation in common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt resets the cursor in the effect, emits one icon-first row per aligned array entry, increments the temporary cursor, and terminates with an empty end key when the cursor reaches the icon-array length. The parent-confirmed scripted-localisation pattern permits set_temp_variable, add_to_temp_variable, and recursive array printing in trigger blocks.
- Ordinary request actions are normalized in infantry_spawn_refresh_request_costs in common/scripted_effects/019_infantry_spawn_management_effects.txt. Each of the nine request modes now has four or fewer nonzero consumed types, and omitted slots are explicitly zeroed before payment. The existing seven-slot snapshot, payment, verification, rollback, refund, and AI transaction paths remain shared, so the visible four-type rows and actual debit/refund paths are symmetric. The decision and localisation cost rows in common/decisions/019_infantry_spawn_decisions.txt and localisation/english/019_infrantry_spawn_l_english.yml match the normalized mode table.
- Provider request and sustainment profile strings are icon-first in localisation/english/019_infrantry_spawn_l_english.yml. An automated publisher-token audit found twenty custom provider equipment tokens and no missing Event 19 token_text_icon localisation key. All twenty corresponding rasters are registered in existing interface files. Teleportation deliberately reuses the existing portal-warfare raster because no separate teleport raster exists; no invented fallback asset was added.
- The selected-lot standardization rows now use existing archetype texticons rather than literal material names. This remains a truthful seven-class material obligation and is therefore listed below as the one unresolved literal four-type design boundary rather than falsely collapsing it.
- The decision-only surface now has mutually exclusive Evolution II and Evolution III request lanes, selected-family stable/crisis lanes, and an Event 19 management mission slot gate. The helper identifiers are infantry_spawn_event19_evolution_ii_peacetime_request_lane, infantry_spawn_event19_evolution_ii_frontline_request_lane, infantry_spawn_event19_evolution_iii_peacetime_request_lane, infantry_spawn_event19_evolution_iii_frontline_request_lane, infantry_spawn_event19_selected_family_stable_lane, infantry_spawn_event19_selected_family_crisis_lane, infantry_spawn_event19_management_mission_is_running, and infantry_spawn_event19_management_mission_slot_is_free in common/scripted_triggers/019_infantry_spawn_triggers.txt. The mission-slot gate is applied to the ten management mission starters and the four achievement trial starts in common/decisions/019_infantry_spawn_decisions.txt. All eleven mission definitions remain available for their original lifecycle routes.
- Provider payment no longer depends on the shared Event 19 overhead variable. In common/scripted_effects/019_infantry_spawn_muster_board_effects.txt, infantry_spawn_execute_selected_family_train_or_spawn_unlocked now gates the inner materialization transaction on infantry_spawn_family_provider_payment_succeeded > 0. The provider-pay -> snapshot -> train/spawn -> verify -> success/cooldown or rollback -> provider refund sequence therefore still runs when Event 19's shared PP/CP overhead is intentionally zero.
- The requested derivative idea localisation was added in localisation/english/019_infrantry_spawn_l_english.yml: infantry_spawn_derivative_local_asset_shortfall and infantry_spawn_derivative_local_asset_shortfall_desc. The file retains its UTF-8 BOM.

### Remaining findings, blockers, and uncertainty

- Concrete design-approval blocker: the standardization decision can truthfully consume and display seven exact material classes, and exact settlement can truthfully display six standard classes plus every provider-owned dynamic row. Applying a literal maximum of four spendable types to these two exact-settlement/standardization actions would hide or misstate obligations or require an approved aggregate-resource mechanic. No balance-changing aggregation or hidden fifth cost was invented. Parent/user approval is required to choose a truthful four-type presentation policy for those exact-obligation actions.
- Direct probability evidence remains partial. The named chaosx_ai_probability_auditor route was not exposed as a callable tool in this runtime. Direct MCP probability inspection, evaluation, and comparison were run, but the adapter cannot fully resolve provider meta-dispatch or complete save-state inputs. This is an evidence limitation, not a source defect.
- Decision-category density is source-bounded rather than rendered. Request lanes are mutually exclusive for human states, management mission starters are serialized by the slot gate, and the request cooldown is hidden by its own cooldown state. Existing active flags from an earlier state can still coexist, and no runtime layout renderer exists for this ordinary decision category. A complete save-state proof of no more than six visible primary actions remains assigned to parent/user validation.
- GUI inspect/render were intentionally skipped because the source has no Event 19 scripted GUI or decision-owned layout. Creating one to satisfy a renderer requirement would violate the explicit decisions-only scope. No GUI MCP blocker is being misreported as a gameplay source defect.
- Future providers must continue publishing a matching token_text_icon key and registered raster. The current twenty published custom tokens pass this audit; future-provider compliance cannot be proven from today's source.
- The concurrent worktree contains unrelated edits and large pre-existing Event 19 hunks. No isolated commit was created because committing the shared files would risk including concurrent work.

### Changed files and identifiers

- common/decisions/019_infantry_spawn_decisions.txt: request-lane visibility helpers and management/achievement mission-slot gates.
- common/scripted_effects/019_infantry_spawn_management_effects.txt: dynamic exact-obligation array rebuild, icon token derivation, affordability, payment/salvage application, selected-lot refresh, and four-type ordinary request normalization.
- common/scripted_effects/019_infantry_spawn_muster_board_effects.txt: provider-payment-success transaction gate and zero Event 19 overhead handling.
- common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt: GetInfantrySpawnExactDynamicEquipmentCost recursive icon-first row formatter.
- common/scripted_triggers/019_infantry_spawn_triggers.txt: lane helpers and management mission-slot helpers, plus dynamic exact-affordability integration.
- common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt: selected-lot exact dynamic affordability is included in the settlement affordability path.
- localisation/english/019_infrantry_spawn_l_english.yml: exact settlement dynamic rows, four-type request rows, icon-first provider and standardization rows, twenty provider token_text_icon keys, and derivative local-asset-shortfall idea strings.

### Before and after behavior

Before remediation, exact settlement charged persistent provider equipment obligations without showing them, ordinary request rows could expose more than four consumed types, provider custom-equipment profiles used literal labels, mission starts could overlap without a shared management slot gate, and the provider train/spawn inner transaction was suppressed when the shared overhead was zero.

After remediation, the selected-lot cost text recursively prints every provider-owned dynamic obligation with its token-derived icon and exact amount; the ordinary request modes expose and debit four or fewer nonzero types with symmetric snapshot/refund behavior; all currently published provider tokens have icon-first presentation; phase and mission-slot gates reduce simultaneous decision pressure while retaining routes; and provider payment success, rather than the zero shared overhead, controls materialization.

### Post-change MCP artifacts

- hoi4.probability_inspect returned PROBABILITY_SOURCE_INSPECTED for common/decisions/019_infantry_spawn_decisions.txt with forty candidates and sixteen required inputs. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/328aa38bb7d4819a3b1650e630f2314e9841d3c97cb127802e0dbea21344c8f0/195b09ada85ba2b90edcf088275a0267b7fdb23b138196a18d2bf95e661ccdab/probability-inspect-4e5230b3f9c3.json.
- hoi4.probability_evaluate returned PROBABILITY_ANALYZED_PARTIAL for ordinary_evolution_ii and anomalous_evolution_iv. It covered eighty candidates, reported 856 unresolved runtime-dependent outcomes, and passed uncertainty-visible validation. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df3e3377e02e8a3479671e2f78d691cd01a9d11aed359565787bc1179ea0809d/54d3d6c9e0de2597466fd8d5a14ff214dfcf4acac859025854003cb320c16c37/probability-e68f5c679791811f9499cf96.json.
- hoi4.probability_compare used the repository HEAD decision source as the before inlineClausewitz snapshot and the current file as after. It returned PROBABILITY_ANALYZED_PARTIAL with comparisonChanges=0, 898 unresolved runtime-dependent outcomes, and uncertainty-visible validation passed. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5648fb9f1ed5b35cb21cae4a7e47e3766af423aaf89dae0d93a86b297a47eb03/70eb59b6ce6019576561bc83486317e1bf33de2d8a55682b275ae6ee55efdff2/probability-ff7801bc9a19085980612a72.json. Comparison rendering: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/ac870ae600c5b4a1601f76d92540a03ffb5c349864c85923edcae992b90f074b/probability-probability-ff7801bc9a19085980612a72-comparison.svg.
- hoi4.event_inspect scanned chaosx.nr19.1 with helper expansion and returned EVENT_INSPECTED_PARTIAL because the large workspace deferred 367 inline files. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a806be24500c2662814aeedd684a7b723f65a8379dc07c440730ad80c3f78bb/e664c777d782e18f2f4573014ca1b49e871c76e7cf07ecdad019bea97d1c7404/event-scan-23147097ed55.json. Blocking diagnostics were zero.
- hoi4.event_render rendered the chaosx.nr19.1 neighborhood and returned EVENT_RENDERED_PARTIAL because the large workspace omitted unrelated nodes; blocking diagnostics were zero. Manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d92e1c113af3148f5953313822760ff0cc70738f61efbccaa578e04ad7913490/63342ba404976a7365e323b18a9b1c963681f373ef65ab2ef873a20029da5768/event-neighborhood-23147097ed55-manifest.json.
- GUI inspect/render were not run for the explicit reason above: no runtime scripted GUI or decision-owned layout exists in the Event 19 source, and the task forbids recreating one.

### Required audit outputs and validation

- Cost-count audit: all nine ordinary request modes resolve to four nonzero consumed types or fewer; provider request callbacks inspected in scope resolve to four or fewer immediate provider-owned types; exact settlement and standardization remain the truthful-obligation blocker described above.
- Texticon audit: all twenty custom provider equipment tokens found under publish_custom_equipment_tokens have matching Event 19 token_text_icon localisation keys and registered rasters; teleportation reuses the existing portal raster.
- Dynamic recursion audit: persistent arrays and cursor reset on every exact-profile rebuild; the scripted-localisation row branch increments a temporary cursor and the end branch resets it, so empty and nonempty arrays terminate without stale rows.
- Mission audit: all eleven mission definitions retain their original owners, durations, success/failure or timeout paths, and cleanup routes; fourteen mission-start decisions are now guarded by the management slot helper.
- Cleanup and exploit audit: exact dynamic arrays are cleared before rebuild, payment/refund/salvage use the shared exact totals, Provider 508 commit/rollback callbacks remain unchanged, and no new GUI or alternate payment route was introduced.
- Live HOI4 execution, save-state transaction simulation, and in-game GUI capture were not run because repository policy assigns live consumer validation to the user and the accepted Event 19 surface has no scripted GUI.

### Handoff conclusion

The four original high findings are not left queued: dynamic obligation visibility, ordinary four-type request presentation, icon-first custom costs, and phased decision/mission visibility are implemented in the bounded files and re-audited above. The only source-design blocker is the literal four-type rule for exact standardization/settlement obligations, where an unapproved aggregate would be misleading. The remaining MCP/auditor items are explicitly evidence limitations. No simplification or fallback was introduced without being recorded.
