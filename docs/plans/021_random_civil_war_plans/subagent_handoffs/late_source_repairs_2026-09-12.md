# Event 021 late source repair handoff — 2026-09-12

Status: implemented for test entry. Acceptance and automatic release remain unresolved.

The regional exposure effect in `common/scripted_effects/021_random_civil_war_effects.txt` set `random_civil_war_exposure_active`, while the Event 021 category, decision, AI, and scripted-localisation surfaces read `random_civil_war_neighbor_exposure`. The missing presentation marker meant a valid neighboring exposure could remain invisible to those surfaces even though the underlying exposure registry was active.

The effect now sets both markers in the same successful exposure branch. Existing lifecycle cleanup already clears both markers, so the repair does not widen eligibility or alter the regional exposure cap.

Validation: a focused source search now shows one setter in `event021_apply_regional_exposure`, all consumer reads, and cleanup in the lifecycle and parent cleanup paths. The current narrow `hoi4.event_inspect` lint for `chaosx.nr21.1` remains `EVENT_INSPECTED_PARTIAL` with revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`; the MCP result still defers workspace-wide helper and lifecycle projection and reports one deferred blocking diagnostic.

No live Hearts of Iron IV run or runtime consumer validation is claimed.

## Pre-commit route repair

The target gate required `random_civil_war_opposition_leader_ready` or `random_civil_war_opposition_force_ready` before the opening transaction could create the ordinary opposition actor. Those receipts are produced by actor initialization, so the automatic target pool could reject every ordinary route before it reached the validator. `random_civil_war_has_valid_opposition_route` now relies on proven route evidence and the existing `random_civil_war_no_valid_opposition` veto. The opening validator remains the final proof for the actor, force, capital, and Event 006 package contract.

The three decision AI modifiers that read the never-published `random_civil_war_low_authority` flag now call `random_civil_war_authority_is_failing`, which is the derived State Authority predicate already used by the target and route planners.

The same-tag route previously admitted one-state or all-island topology without requiring an unsafe condition, and the route-valid trigger rejected every all-island country with more than one controlled state. The route evidence pass now requires live political, military, administrative, territorial, war, exposure, or authority stress before registering that route, publishes an all-island receipt only when every owned state is an island, and accepts that receipt as the bounded multi-state exception. Stable one-state targets therefore remain outside the same-tag route, while unsafe one-state and all-island targets can reach the normal opening validator.

## Completion-audit source repairs

The Event 006 local-content and player-surface gates now accept a complete Event 021-origin package through `is_independence_wave_event021_package_country`. Preparation remains closed, and the branch does not set Event 006 active-origin, firing, evolution, league, or network state. This restores the accepted package tree, decisions, formables, and AI reuse contract.

`random_civil_war_authority_is_collapsed` now requires an initialized State Authority value at or below the Collapse threshold. The prior predicate required the variable to be absent before comparing it, which made the initialized Collapse band unreachable.

The Event 021 package-country compatibility predicate now also requires a normal human country. This makes the existing Event 006 content bridge explicitly honor `is_actual_nonhuman_country` immunity even if an invalid adapter flag combination is present.

The three Transcaucasus package roots now use `is_independence_wave_package_origin_compatible`. A real Event 006 origin still uses the Event 006 origin value, while an Event 021 adapter can satisfy the package root only during its validated setup window or after its complete human-package receipt. Event 021 does not write the Event 006 origin value.

Disposition: implemented for test entry. Acceptance and release remain unresolved pending the required MCP probability comparison, focused event helper and lifecycle validation, and user-owned live testing.
