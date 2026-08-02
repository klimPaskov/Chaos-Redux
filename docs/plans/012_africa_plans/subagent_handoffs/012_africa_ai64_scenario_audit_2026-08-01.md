# Event 012 Africa B4 AI 64-profile scenario audit

## Scope and outcome

This bounded audit covers the 64 entries in `docs/specs/012_africa_specs/matrices/012_africa_ai_route_matrix.csv`, the profile predicates and loaders, the AI focus and strategy plans, the shared action dispatcher, natural-disaster actions, priority package registration, and world-order action gates.

No gameplay or localisation file was changed.

Static registration is complete: all 64 matrix keys have one `africa_ai_profile_<key>_is_active` predicate, one `africa_ai_apply_profile_<key>` loader, and one call in `africa_ai_refresh_profile_registry`.

The profile inventory resolves to 9 regional overlays, 22 specific hosts, 7 constitutional routes, 8 member or rival profiles, 5 external-power profiles, 6 high-chaos profiles, and 7 world profiles.

## Issue list, sorted by severity

### Medium — Scramble classification does not itself prove material readiness

`africa_ai_classify_scramble_response` classifies an AI actor as expedition, withdrawal, sanctions, recognition, or opportunist from colonial-interest, faction-leader, foreign-base-holder, war-support, stability, and recognition flags.

It does not itself test naval access, deployable force, port capacity, distance, or target-strength ratio.

The shared target/action pipeline still calls `africa_validate_action_specific_requirements`, re-quotes the action, reserves and pays the player-equivalent cost, and clears selection if the action cannot begin, so this is not a confirmed unsafe launch or cost bypass.

Recommended follow-up: run one scenario per Scramble class with a materially incapable candidate and record whether the policy merely ranks it or produces a rejected launch; if it can rank-starve valid candidates, add a narrow capability check to the classifier or the relevant policy factor.

### Medium — strategy-plan probability adapter has no matching surface

`hoi4.probability_inspect` identified the workspace, but the attempted strategy-plan surface returned `PROBABILITY_SURFACE_EMPTY` for `common/ai_strategy_plans/012_africa_focus_plans.txt`.

No rank, starvation, or variance claim can therefore be made from the probability adapter for the 13 priority packages, Scramble classes, or world plans.

Recommended follow-up: use an adapter that understands AI strategy-plan `focus_factors`, or record bounded runtime score evidence from the existing dispatcher rather than treating the empty artifact as a passing simulation.

### Low — full scenario execution remains user-owned evidence

The source audit establishes registration, route locks, final action validation, and cleanup, but it cannot prove all 64 positive and negative scenarios execute in a live campaign.

This is an evidence limitation, not a code simplification or a source defect.

## Decision category lifecycle and action quality

The active AI controller is limited to AI current hosts with an open action-capacity slot and no active first-proof mission.

The late controller is additionally restricted to Scramble, world-order, or terminal Africa-world states, and requires the first-proof condition to be resolved or failed.

Every dispatch refreshes the bounded African and external target rosters, resets the registry, snapshots host policy, prepares family weights, evaluates a candidate, rechecks the specific action requirements, and starts the normal quoted action flow.

The shared action cleanup removes the active target arrays, action flags, quote target, exact mission, temporary action state, and natural-disaster reservation when applicable, while restoring bounded action capacity and reducing the active-action count.

The retry gate blocks repeated action-target pairs unless the recorded partial, failure, or cancellation policy permits another attempt.

No free-unit, equipment-farming, war-goal-spam, core-spam, or capacity-loop path was demonstrated in this bounded source review.

## Mission quality notes

The audit did not add or alter a mission.

The owner is the current Africa host through the common action dispatcher and the action-specific effects.

Action missions use the selected target or package context, enforce action-specific requirements before launch, and remove their exact mission on success, failure, cancellation, or ordinary cleanup.

The natural-disaster actions use a hostile country target, a dynamic strength ladder, event-result records, cooldown, and reserved-cost cleanup; a neutral or non-existent target cannot enter the launch path because `africa_natural_disaster_weapon_target_is_valid` requires a current war with the host.

Duplicate risk is controlled by action-target retry facts, active-action capacity, exact mission removal, and the reservation reset, subject to live execution evidence.

## Cost and requirement clarity

`africa_ai_try_selected_late_action_against_target` does not launch directly from an AI preference: it re-evaluates the target, requires `africa_validate_action_specific_requirements`, requires a positive specific result, invokes `africa_begin_quoted_action_against_target`, and clears state if begin fails.

This preserves the ordinary player-equivalent cost, availability, cooldown, and cap checks for both early and late AI actions.

Actions 69 and 70 require natural-disaster actor eligibility, an active war, available political-power and chaos-pressure costs, and a valid hostile target.

`africa_prepare_hostile_natural_disaster_strength` derives and clamps strength from route commitment, priority status, caller reservation, ecological pressure, readiness, and target industrial/state scale rather than using a static severity value.

## AI validity and route-lock findings

The registry resets all family weights, risk tolerance, retry policy, profile count, and current-profile identifiers before applying layers, preventing stale layers after a host or route changes.

The seven constitutional profiles have exact constitution values, while the eight member/rival, five foreign, six high-chaos, and seven world profiles use ordered `else_if` selection to choose one profile per family.

The profile predicates fail closed for a missing host, invalid capital region, closed route, dead or invalid target, world-end conflict, or unavailable evolution.

Profile 42, `world_africa_world`, is the intentional terminal exception: it uses `africa_ai_host_profile_base_is_active` and accepts `world_end_africa_the_world`, while W5 execution remains separately gated.

`africa_terminal_world_identity_can_commit` requires the presentation package flag, world order, Continental Wars, Africa Is One, terminal route and settled packages, sovereign and terminal completion thresholds, no unresolved package actor, terminal chaos, no disabled/world-end conflict, no constitutional review, and no unresolved war with a package actor.

Actions 85 through 92 retain their world-package, world-order, target, Continental Wars, W5, and terminal-identity gates; no terminal action is enabled solely by the profile.

The static strategy-plan inventory contains the uncommitted continental plan plus all seven constitutional continental plans, all nine regional overlay mandates, 22 host plans, and 32 external/world plan blocks.

## Priority package evidence

The source matrix lists 16 package identities.

The current country-package audit resolves 13 conditionally reachable carrier-or-origin pathways: Asante, Oyo, Sokoto, Kanem-Bornu, Manden, Kongo, Buganda, Aksum, Harar, Nubia, Great Zimbabwe, Merina, and Zulu. Aksum/TIG, Nubia/SUD, and Great Zimbabwe/ZIM use the supported nonmatching vanilla-carrier predicate after their exact origin marker is recorded.

The three dormant identities are Luba/DYX, Lunda/DZX, and Kilwa/EMX. Their distinct package scripts and existing Event 006 tags remain present, but the installed Event 006 map-binding ledger has no accepted unique current state, so their live-receipt and map gates remain closed. No broad Congo or Tanganyika substitute is allowed.

`africa_priority_member_can_register_package` also requires Event 012 activation, a valid Africa host event target with host commitment complete, no existing package or requalification lock, a non-Soviet Event 006 origin, promotion approval, and valid origin proof.

This is a static pass for the required 13 reachable and 3 rejection cases; it is not a runtime proof that every package AI finishes its entire focus, action, and post-settlement path.

## Scenario acceptance matrix

| Family | Positive scenario and expected result | Negative scenario and expected result | Source result |
| --- | --- | --- | --- |
| Regional overlays | Current valid Nile/Horn host in the active preterminal event applies `host_nile_horn`. | World end, an invalid host, or a non-African host capital prevents the overlay. | Static pass. |
| Specific hosts | A valid current host with its exact host identity applies its matching one of 22 profiles. | Changing current host or losing the legal host state clears the specific layer on registry refresh. | Static pass. |
| Constitutional routes | A current host on each exact constitution with its route tree applies the matching one of seven route profiles. | A covenant host without Evolution III, commitment, reveal, or actor proof fails the high-chaos constitutional profile. | Static pass. |
| Member and rival | A valid protected, associate, chartered, federal, resistant, outside, or rival relationship selects one ordered member profile. | A dead, invalid, or route-closed partner has no candidate profile. | Static pass. |
| External power and Scramble | Colonial faction leader selects expedition; weak foreign base holder selects withdrawal; the other named interest cases select sanctions, recognition, or opportunist. | Non-AI or common-profile-invalid actor leaves the class at none. | Static pass; material-readiness gap remains. |
| High chaos and nonhuman | An Evolution III eligible host with its disease, rain/drought, stoneborn, gorilla, Pan, or Green state selects the corresponding profile; an enemy at war can be a natural-disaster target when costs are available. | No Evolution III, closed route, insufficient cost, or a neutral target rejects the profile or action. | Static pass. |
| World order | W1 eligible package path selects its world profile; W5 uses profile 42 only with the Africa-world route state, and Actions 90–92 also require their terminal gates. | Missing W5/presentation/package proof or an invalid world target prevents the terminal action. | Static pass. |

## Localisation and tooltip notes

No player-facing string or GUI surface changed in this audit.

The audited action requirements are routed through common requirement validation and existing custom tooltip surfaces rather than exposing raw AI profile triggers to the player.

No new localisation gap was demonstrated in the owned AI profile, effect, or strategy-plan surface.

## Cleanup and exploit-risk notes

The registry reset and cleanup calls are the critical stale-state protections.

Natural-disaster cost reservation is cleared by ordinary action cleanup, including cancel/fail paths, and the event-result helper applies cooldown and records only after the event result is accepted.

The main remaining exploit-risk uncertainty is behavioural rather than structural: the Scramble classifier may consider an incapable actor before the shared final validator rejects it.

## Validation performed and skipped

Performed a static matrix-to-source cross-check: 64 matrix rows, 64 active predicates, 64 profile loaders, and no missing registry call.

Performed source tracing for dispatcher refresh, late dispatch, action-specific final validation, quote/cost flow, target retry, action cleanup, W5 terminal gate, natural-disaster target and strength gate, priority registration, and strategy-plan route inventory.

Read the Event 012 AI matrix, current improvement addendum section 10, required decision/event/focus/subagent guidance, relevant offline wiki pages, and vanilla scripting documentation before the audit.

`hoi4.probability_inspect` returned `PROBABILITY_SURFACE_EMPTY` for the strategy-plan surface, so no probability/ranking evidence is claimed; artifact reference: workspace `mod_chaos_redux_ea3b2d67c2c0`, no generated surface artifact.

Skipped live save, game launch, and 64 runtime profiles because live consumer validation is user-owned and the parent requested completion after this bounded registration/scenario pass.

## Handoff

Changed file: this handoff only.

Changed decision, mission, scripted GUI, or localisation identifiers: none.

Before and after behaviour: unchanged; this audit found no small, demonstrated defect inside the permitted AI profile trigger, effect, or strategy-plan files that justified a patch.

Recommended next owner action: retain the two medium findings as acceptance blockers until a compatible strategy-plan score probe and one materially incapable Scramble scenario are recorded, then attach the evidence to the B4 acceptance ledger.

No broad mechanic expansion is recommended by this audit because the existing Event 012 improvement addendum remains the active plan; the narrow Scramble readiness check should be handled as a follow-up scenario or an explicitly accepted policy refinement.
