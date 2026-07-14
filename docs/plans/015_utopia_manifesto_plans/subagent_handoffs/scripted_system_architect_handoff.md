# Event 15 scripted-system architecture audit

## Scope and outcome

This is a read-only architecture audit of the final pre-removal Event 15 sidecar at commit `0bce9e9a4`, which includes the implementation introduced by `5483e20d3` and its targeting/load/balance follow-ups.

No gameplay file was restored or edited. The current Event 15 specification is materially broader than the removed implementation, so none of these historical files should be restored wholesale:

- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`

The historical files are useful as a pattern library. They are not a safe current implementation of recipient selection, the Commonwealth Ledger, Necessary Ground cases, routes, formation, or cleanup.

## Historical baseline: safe reuse map

| Historical surface at `0bce9e9a4` | Disposition | Reason |
| --- | --- | --- |
| `utopia_manifesto_country_has_coast`, `utopia_manifesto_country_island_capital`, `utopia_manifesto_country_landlocked` | Reuse as narrow geography primitives after confirming current scope semantics | These are small, side-effect-free tests. They are not sufficient recipient gates and should be paired with valid-capital and controllable-core checks. Inland Island must follow the current capital-route design rather than treating every non-coastal country identically. |
| Short-lived `save_event_target_as = utopia_manifesto_target` use inside `utopia_manifesto_select_target` | Reuse the event-target lifetime pattern only | A regular event target is appropriate for carrying the chosen recipient into the entry event in the same effect chain. The old selector itself is not reusable. Persistent GUI/case targets need actor-owned state and explicit cleanup. |
| Clamp-and-mutate structure in `utopia_manifesto_clamp_ledger` and the `utopia_manifesto_add_*` effects | Reuse the small-helper pattern, rewrite the contract | Central clamping and prepared deltas are sound. The historical variables and thresholds implement a different Ledger and the old refresh effect has excessive unrelated side effects. |
| Numeric route variable plus named route triggers | Reuse the representation pattern, rewrite every route identifier and setter | A single enum-like variable is useful. Historical setters do not clear prior route flags and use an obsolete six-route taxonomy. |
| Counter-safe cleanup pattern in `utopia_manifesto_cleanup_project_state` | Reuse the decrement/clamp idea only | Current district, Need-case, stewardship, and selected-target states are different. Cleanup must also handle ownership changes, invalid targets, mission cancellation, route changes, and terminal states. |
| Array cleanup in `utopia_manifesto_clear_boundary_arbitration_targets`, `utopia_manifesto_clear_marked_district_targets`, and `utopia_manifesto_clear_league_aid_targets` | Reuse the explicit-clear pattern, not the old arrays or missions | The old arrays represent one-step neighboring claims and aid missions, not the current case, associate, league, and stewardship model. |
| `utopia_manifesto_clear_active_mission_flags` | Rewrite and expand | It clears only six old country flags and does not remove selected targets, cases, state markers, stewardship, emergency levies, or counters. |

No complete historical definition beyond the three narrow geography tests is suitable for unchanged restoration.

## Historical helpers that conflict with the current specification

### Recipient selection

The following historical definitions must be rewritten rather than restored:

- `utopia_manifesto_has_valid_target_available`
- `utopia_manifesto_has_dispatchable_target_available`
- `is_valid_utopia_manifesto_target`
- `is_valid_utopia_manifesto_player_target`
- `is_valid_utopia_manifesto_automatic_target`
- `utopia_manifesto_prepare_random_event_fire`
- `utopia_manifesto_select_target`
- `utopia_manifesto_prepare_target_weight`
- `utopia_manifesto_add_current_country_to_target_pool`

Conflicts:

- The old selector merges humans and AI into one weighted pool. The accepted design requires three ordered candidate classes and selection from the first nonempty class.
- Human control is an `+18` random weight in the old implementation, not a hard first-class priority.
- The old selector duplicates each country in a temporary array once per weight point and then chooses randomly. It does not produce the required dynamic weak-country score or deterministic comparison/tie-break behavior.
- The old gates do not test protected or mature focus routes, active/recent full transformations, civil war, near capitulation, full offensive war, dominant faction leadership, extensive subjects, extensive occupation, or a valid controlled core capital route.
- The old capital test checks control only. It does not prove that the capital is a core or that a recoverable national center exists.
- The old automatic gate admits peaceful subjects with modest stability. The current specification leaves the subject route unapproved; subjects must remain excluded until a complete autonomy-compatible route is reviewed.
- The old implementation has fixed caps (`45` factories, `25` military factories, `18` naval factories, `18` controlled states, and `70` divisions). Current specs require reviewed tuning bands rather than treating these values as accepted balance.
- There is no rejection-reason state for manual/debug inspection and no stronger override boundary for special, nonhuman, protected-package, or invalid-capital targets.

### Ledger and route state

The historical Ledger is a different mechanic. It stores:

- `utopia_need`
- `utopia_consent`
- `utopia_surplus`
- `utopia_overreach`
- `utopia_vocation_balance`
- `utopia_foreign_suspicion`
- `utopia_league_confidence`
- five equal vocation shares

The current public core is Need, Plenty, Concord, and one Choice-versus-Assignment axis. It also requires six calling families, a distinct six-band reserve system, visible value breakdown inputs, route-dependent consequences, and case/stewardship state. Therefore these historical helpers are not directly reusable:

- `utopia_manifesto_initialize_ledger`
- `utopia_manifesto_refresh_ledger`
- `utopia_manifesto_refresh_ledger_display_variables`
- `utopia_manifesto_refresh_ledger_flags`
- all historical Ledger band triggers and `utopia_manifesto_add_*` effects

The old `utopia_manifesto_refresh_ledger` also recalculates AI weights, dirties focus layout, and checks achievements on every value mutation. The replacement refresh contract should be pure: clamp values, derive public bands, and update breakdown/display inputs. AI, achievements, focus layout, and event firing should be invoked by their owning call sites.

Historical routes are also obsolete:

- `living_humanism`
- `common_store_state`
- `island_discipline`
- `guild_commonwealth`
- `marked_bounds`
- `new_utopia`

They do not map one-to-one onto Consent of Households, Common Table, Guardians of Measure, Closed Island, and The Joke Understood. The old setters leave previous route flags behind, so route switching can create contradictory state.

### Necessary Ground, integration, and league logic

Do not restore `utopia_manifesto_can_open_needful_land`, the old neighbor target/claim helpers, boundary arbitration/marked district mission effects, or `utopia_manifesto_complete_integration_project` as the current external system.

The historical implementation chooses neighboring non-core states, creates claims after a single mission outcome, and can add a core after a compliance gate. It does not model:

- a real visible deficit and domestic-alternative proof
- one active case and a selected-target lifecycle
- target relevance, proportionality, transport, or housing plans
- purchase, lease, joint-rule, associate, ultimatum, and war stages
- case integrity and local support
- expiry when Need falls or the target stops solving the deficit
- temporary stewardship obligations and deadlines
- return, autonomy, association, integration, or revolt outcomes
- partner sovereignty, obligations, exit/status review, and league cohesion

The historical relationship flags and friend/member arrays can inform storage style, but they are insufficient as current league state. Counts must remain synchronized with valid partners and must distinguish associates, league members, recognized agreements, observers/sponsors, and coercive dependents.

### Acceptance, decisions, units, achievements, and super-events

Do not restore `utopia_manifesto_accept_manifesto` or `utopia_manifesto_reject_manifesto` unchanged. Acceptance immediately loads the old tree and ideas rather than completing the staged founding survey. Rejection cleanup knows only the historical variables and leaves no contract for the expanded selected-target, case, stewardship, reserve, calling, route, and evolution state.

Historical decision cost/pay effects, unit spawners, reward packages, achievements, identity effects, and the two hard-wired super-event calls are implementation-coupled and outside this narrow helper architecture. They need review against the current decision, focus, country-package, balance, asset, and super-event specs before selective recovery.

## Replacement helper contract

The names below are the recommended stable interface for the selective recovery. Exact numeric tuning remains a parent balance decision.

### 1. Eligibility and deterministic weak-country score

Recommended constants groups:

- `utopia_manifesto_candidate_gate`: reviewed industry, occupation, subject-network, capitulation, focus-depth, and faction-network bands.
- `utopia_manifesto_candidate_score`: base score plus per-factor additions, penalties, score minimum, and score maximum.
- `utopia_manifesto_candidate_class`: human-safe, AI-generic/approved, AI-lightly-developed-approved, and invalid values.

Recommended country triggers:

- `utopia_manifesto_candidate_has_viable_capital`
- `utopia_manifesto_candidate_tree_is_replaceable`
- `utopia_manifesto_candidate_has_mature_identity_route`
- `utopia_manifesto_candidate_has_dominant_faction_network`
- `utopia_manifesto_candidate_has_extensive_subject_network`
- `utopia_manifesto_candidate_has_extensive_occupation`
- `utopia_manifesto_candidate_is_safe`
- `utopia_manifesto_candidate_is_safe_human`
- `utopia_manifesto_candidate_is_safe_ai_generic`
- `utopia_manifesto_candidate_is_safe_ai_approved`
- `utopia_manifesto_candidate_requires_strong_override`
- `utopia_manifesto_prepared_candidate_outranks_prepared_best`

`utopia_manifesto_candidate_is_safe` should hard-exclude majors, special/nonhuman/terminal/world-end actors, Event 15 actors, protected packages, active/recent transformations, mature routes, strong industry, subjects while the subject route is disabled, civil war, near capitulation, full offensive war, invalid capital/core control, dominant faction networks, extensive subjects, and extensive occupation.

Recommended country effects:

- `utopia_manifesto_clear_candidate_reason_flags`
- `utopia_manifesto_refresh_candidate_reason_flags`
- `utopia_manifesto_prepare_candidate_comparison`
- `utopia_manifesto_promote_prepared_candidate_to_best`

The reason refresh should set one primary reason flag in a documented priority order, for example major, protected tree, mature route, active transformation, special actor, strong industry, subject route disabled, civil war, capitulation risk, offensive war, invalid capital, faction dominance, subject network, occupation, or already selected actor.

`utopia_manifesto_prepare_candidate_comparison` should output preinitialized temporary variables:

- `utopia_manifesto_candidate_class`
- `utopia_manifesto_candidate_score`
- `utopia_manifesto_candidate_id`

The score should reward weak industry, weak infrastructure/research, small state count, stable capital, replaceable tree, weak international protection, compatible migration/trade/housing pressure, and viable island/coastal/Inland Island context. It should penalize war, mature focus progress, strong growth, guarantees, subject/occupation burden, and recent transformations.

Selection order must be deterministic at comparison time: lower valid class wins, then higher score, then lower country ID as the stable tie-break. The parent should orchestrate class scanning through a country scorer or bounded dispatch helper. Do not restore the historical repeated-entry weighted array.

### 2. Four-value Commonwealth Ledger

Recommended stored values, all clamped to `0..100`:

- `utopia_need`: higher means a larger unresolved deficit.
- `utopia_plenty`: higher means stronger practical provision.
- `utopia_concord`: higher means greater trust and consent.
- `utopia_assignment`: `0` is maximum Choice; `100` is maximum Assignment.

Recommended derived band variables:

- `utopia_need_band`
- `utopia_plenty_band`
- `utopia_concord_band`
- `utopia_assignment_band`

Each public value uses five bands. Localisation must map them exactly to the accepted wording:

- Need: resolved, manageable, pressing, severe, existential.
- Plenty: scarcity, fragile provision, stable provision, abundance, surplus commonwealth.
- Concord: fractured, doubtful, cooperative, trusted, common purpose.
- Axis: free callings, guided choice, guaranteed placement, planned assignment, compulsory service.

Recommended country effects:

- `utopia_manifesto_clear_ledger_breakdown`
- `utopia_manifesto_initialize_ledger`
- `utopia_manifesto_clamp_ledger_values`
- `utopia_manifesto_refresh_ledger_bands`
- `utopia_manifesto_clamp_and_refresh_ledger`
- `utopia_manifesto_apply_prepared_ledger_delta`
- `utopia_manifesto_clear_ledger_runtime`

Initialization should be route-neutral and should store component variables used by the GUI/tooltips. At minimum, expose contributions from industry, infrastructure/transport, war/blockade, occupation, capital security, migration/housing/trade pressure, stability, and representative political institutions. The sum of displayed contributions must reconcile with each initialized value after clamping.

`utopia_manifesto_apply_prepared_ledger_delta` should require callers to preinitialize these temporary inputs, even when zero:

- `utopia_manifesto_need_delta`
- `utopia_manifesto_plenty_delta`
- `utopia_manifesto_concord_delta`
- `utopia_manifesto_assignment_delta`

It should record last-change inputs for breakdown localisation, add all four values once, clamp once, and refresh bands once. It should not check achievements, change focus layout, select AI routes, or fire events.

Reserve state is separate from Plenty. Recommended identifiers are `utopia_reserve_band` plus `utopia_manifesto_refresh_reserve_band`, using the six accepted states: empty stores, emergency stores, seasonal reserve, one-year security, two-year security, and surplus commonwealth.

Calling state should cover all six current families rather than restoring the old five equal shares. Use one severity variable and one boolean shortage flag per family:

- provisioning/agriculture
- workshops/arsenal
- civic works/transport
- learning/care
- maritime/settlement, with Inland Island adaptation
- defense/watches

Method state should distinguish Open Call, Guaranteed Placement, Assignment Quota, and Emergency Levy. Emergency Levy requires an expiry/extension counter and explicit cleanup.

### 3. Selected targets, case integrity, and local support

The GUI selection and the active Need case are different lifecycles and should not share one global event target.

Recommended selection interface:

- `utopia_manifesto_selected_country_target_is_valid`
- `utopia_manifesto_save_from_as_selected_country_target`
- `utopia_manifesto_clear_selected_country_target`

Persist the selected scope on the Event 15 actor through an actor-owned scope variable or another verified persistent pointer. A close action clears it. AI target evaluation remains separate and must not mutate the human GUI selection.

Recommended active-case interface:

- `utopia_manifesto_active_need_case_is_valid`
- `utopia_manifesto_prepare_case_integrity`
- `utopia_manifesto_refresh_case_local_support`
- `utopia_manifesto_record_case_method`
- `utopia_manifesto_close_active_need_case`

The active case should store one target, one target state when relevant, case family, deficit severity, domestic alternatives attempted, peaceful offers made, transport/housing readiness, proportionality, current method/stage, integrity, local support, unrelated-land penalty, expiry, and outcome. Boolean state should use flags; values and enums should use variables.

Case integrity must be computed from the current spec inputs, not inferred from route alone. Local support should be target/state-specific and should react to provision delivered, local consent, resistance, damage, promises kept, and route conduct. A case must close or demand an explicit costly continuation when Need falls, its target disappears, or the target no longer solves the deficit.

Recommended stewardship interface:

- `utopia_manifesto_stewardship_target_is_valid`
- `utopia_manifesto_refresh_stewardship_proof`
- `utopia_manifesto_clear_stewardship_runtime`

Proof should cover provision, transport, charter/local administration, resistance/local support, deadline, and final status choice. It must not grant a core merely because a compliance threshold was reached.

### 4. Cleanup and lifecycle ownership

Recommended aggregate effects:

- `utopia_manifesto_clear_recipient_selection_runtime`
- `utopia_manifesto_clear_active_need_case`
- `utopia_manifesto_clear_stewardship_runtime`
- `utopia_manifesto_clear_emergency_calling_runtime`
- `utopia_manifesto_clear_route_runtime`
- `utopia_manifesto_clear_all_temporary_runtime`

Call cleanup from concrete lifecycle events rather than adding a world-iterating daily/weekly/monthly pulse:

- selected-target close action
- target invalidation or annexation
- state ownership/control change
- war end or case expiry
- mission cancellation or timeout
- route switch
- opening rejection
- Event 15 actor annexation
- approved superseding transformation
- terminal world state

Cleanup should clear pointers/arrays before clearing flags and should make counters idempotent. Where possible, recompute counts from valid arrays instead of decrementing blindly from several termination paths.

### 5. Route state and formation proof

Recommended route constants:

- `unresolved = 0`
- `consent_of_households = 1`
- `common_table = 2`
- `guardians_of_measure = 3`
- `closed_island = 4`
- `joke_understood = 5`

Each route setter should clear every old route flag, set exactly one route variable and one route flag, then refresh route-dependent availability. Do not alias the removed route identifiers to these values.

Recommended triggers:

- `utopia_manifesto_common_formation_proof_met`
- `utopia_manifesto_can_form_voluntary_commonwealth`
- `utopia_manifesto_can_form_council_union`
- `utopia_manifesto_can_form_planned_utopia`
- `utopia_manifesto_can_form_closed_island_state`
- `utopia_manifesto_can_form_practical_commonwealth`
- `utopia_manifesto_can_form_current_route`
- `utopia_manifesto_super_event_network_threshold_met`

Common proof must require the route capstone, island/capital-ring project, stable or improving Plenty, route-appropriate Concord and axis band, first external case with recorded method, at least one valid associate/league member/recognized compact, no active founding crisis, and no unresolved stewardship failure.

Route proof must additionally enforce:

- Voluntary: high Concord and Choice, no penal labor, no unjustified enforced case, and a consensual partner.
- Council: functioning calling councils, strong stores, council autonomy retained, and an external commune/member.
- Planned: high Plenty, completed city network, route-stable Assignment, and no active data scandal or district revolt.
- Closed Island: completed separation project, high Assignment, strong reserves and defense; low Concord is permitted but its consequences remain.
- Practical: hidden humanist route, high Concord and Choice, mixed property settlement, peacefully resolved or abandoned false cases, and broad recognition.

Formation network proof and super-event proof are intentionally different: formation requires at least one meaningful external relationship; the super-event requires at least three plus the regional objective.

## Parent-owned integration surfaces and remaining gaps

The parent must own or delegate these surfaces; they were intentionally not implemented here:

- Candidate-pool traversal and final recipient persistence in the event dispatcher or `common/scorers/country/`. The helper contract above supplies classification, score outputs, and deterministic comparison only.
- A repository-level replaceable/protected focus-tree registry and mature-route tests. Until that exists, generic trees plus explicit approvals are the conservative eligible set.
- Final numeric target, Ledger, reserve, formation, AI, and dynamic-scaling constants after live balance review.
- Persistent selected-target wiring in scripted GUI and decisions, including close behavior and localisation.
- Active Need-case, state-target, stewardship, partner, and league call sites. These cannot be made safe without the owning decisions, missions, events, and state-transfer hooks.
- Ledger band and breakdown scripted localisation. The helpers should expose numeric band variables and contribution inputs; localisation owns the accepted public labels.
- Calling shortages, reserve measurement, district proof, local support, and league cohesion calculations from their gameplay systems.
- Evolution context. Active-event and pre-fire evolution states must be recorded separately, must feed initialization/AI/event pacing, and must never force a route automatically.
- Formation cosmetic identity, faction/league transition, achievements, event log, and super-event dispatch.

## Validation and risk record

Compared the final pre-removal constants, triggers, effects, and original architect handoff at `0bce9e9a4` against the current recipient-selection, four-value Ledger, decision/mission, formation, evolution, AI/balance/compatibility, cleanup, and acceptance specifications. The audit also checked the final historical follow-up sequence through `996a32c43` rather than assessing only the initial `5483e20d3` implementation.

No gameplay validation was run because no gameplay files were restored or changed. The principal remaining risks are missing exact balance thresholds, absence of a current tree-replacement registry, and unresolved persistent-pointer/call-site ownership for selected targets and cases. Subject eligibility remains deliberately disabled pending the full implementation review required by the specification.

## Files changed

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/scripted_system_architect_handoff.md`

No gameplay, localisation, UI, asset, spreadsheet, or source-spec file was edited. No simplification or fallback was silently introduced; selective restoration is deferred because restoring the obsolete helper model would conflict with the accepted current design.
