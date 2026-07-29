# Supported-core completion audit

Date: 2026-07-29

Audit mode: read-only final source audit against the latest binding supported-core scope.

## Supported-core blockers

### CW-B1 — active Chemical releases still manufacture missing condition inputs

The selected-state raid target, native outcome, and payload debit are genuine engine receipts, but the active raid adapter converts the native result tier into values presented to the shared exposure calculator as weather, terrain, target-density, forecast, command, evidence-control, and friendly-risk inputs.

- `common/scripted_effects/cbrn_chemical_raid_effects.txt:280-322`, `cbrn_chemical_air_raid_set_native_condition_receipt_internal`, derives every condition field solely from `cbrn_raid_result` and marks `cbrn_action_native_raid_condition_receipt` supplied.
- `common/script_constants/cbrn_chemical_delivery_constants.txt:237-279`, `cbrn_chemical_air_raid_condition_receipt`, acknowledges that the current raid API supplies no verified target-state weather or terrain while defining synthetic partial/success/catastrophic weather and terrain multipliers.
- `common/scripted_effects/cbrn_chemical_raid_effects.txt:345-367` passes that constructed record through `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record`.
- `common/scripted_effects/cbrn_exposure_effects.txt:639-703` rejects a release without resolved conditions, so the outcome translation is not presentation-only; it supplies otherwise-missing inputs that materially affect accepted harm.

This affects all eleven active native routes in `common/raids/cbrn_chemical_air_raids.txt`: `chemical_chlorine_strike`, `chemical_phosgene_strike`, `chemical_mustard_strike`, `chemical_lewisite_strike`, `chemical_tabun_strike`, `chemical_sarin_strike`, `chemical_soman_strike`, `chemical_malodor_strike`, `chemical_aphrodisiac_strike`, `chemical_sarin_rocket_strike`, and `chemical_soman_rocket_strike`.

The Chemical doomsday route has the same contract problem in fixed form: `cbrn_chemical_doomsday_set_action_conditions` assigns route constants to weather, terrain, density, forecast, command, and friendly risk, then marks condition proof supplied (`common/scripted_effects/cbrn_chemical_doomsday_effects.txt:132-143`) before dispatch (`:148-183`). This is a fixed/neutral condition receipt rather than live target-condition evidence.

These are prohibited proxy/neutral receipts under the binding scope. The fact that the approximation is documented does not make it a real engine receipt. The active Chemical pipeline is therefore not supported-core complete.

Active Chemical route mapping otherwise resolves to the intended common endpoint:

- Native selected-state raids and rockets: `cbrn_resolve_chemical_air_raid_outcome` → `cbrn_prepare_chemical_action_record` → `cbrn_dispatch_chemical_action_record`.
- Chemical doomsday: `cbrn_chemical_doomsday_resolve_current_state` → the same prepare/dispatch pair.
- Separately authorized restricted camp site: `camp_rework_apply_chemical_escalation_in_action_state` → the same prepare/dispatch pair (`common/scripted_effects/camp_repression_rework_effects.txt:4426-4467`). This route requires an already valid camp-system target and does not let doctrine create camp or genocide infrastructure.
- Ground Chemical and nerve-suppression call sites exist in `cbrn_battlefield_operation_effects.txt:822` and `cbrn_occupation_effects.txt:351`, but their false current-version hooks make those calls unreachable.

### CW-B2 — accepted disposition is not fully promoted across documentation

The active eleven-achievement runtime surface is internally aligned, but completion documentation still presents the superseded fifteen-achievement package as complete.

- `docs/systems/cbrn_warfare/overview.md:119` still claims assets for all fifteen achievements.
- `common/scripted_effects/cbrn_achievement_effects.txt:5-6` still describes fifteen accepted achievements.
- `docs/plans/chaos_warfare_system_plans/2026-07-29_near_completion_improvement_loop_closure.md:146` still claims all fifteen are defined and tracked.
- `docs/plans/chaos_warfare_system_plans/2026-07-13_requirement_traceability_and_migration_ledger.md:34,78-79,129,243,265` retains stale `in progress` or legacy-route migration findings rather than disposing them against the current supported-core authority.
- `docs/plans/chaos_warfare_system_plans/documentation_cleanup_handoff.md:53-56,76,88-89` continues to queue design work for achievements that the later binding scope removed.

The eleven active achievements themselves are present and aligned at `common/achievements/chaos_redux_achievements.txt:3714-3768`, `common/scripted_triggers/cbrn_achievement_triggers.txt:16-197`, `localisation/english/cbrn_achievements_l_english.yml:3-35`, and `interface/chaosx_achievements.gfx:1486-1518`. This is a documentation/accepted-plan disposition blocker, not an achievement runtime blocker.

## Genuine engine and user-owned blockers allowed to remain

- Exact live target-state weather and terrain are not exposed to the current selected-state raid outcome effect. This is a genuine engine boundary, but it does not authorize CW-B1's synthetic replacement.
- Ground Chemical operations remain correctly fail-closed through `cbrn_battlefield_current_version_condition_hook_verified = { always = no }` in `common/scripted_triggers/cbrn_battlefield_operation_triggers.txt:23-25`. The selector and all preparation controls inherit the same false gate; `cbrn_battlefield_cycle_agent` is both hidden and unavailable.
- Nerve suppression remains correctly fail-closed through `cbrn_occupation_current_version_condition_hook_verified = { always = no }` in `common/scripted_triggers/cbrn_occupation_triggers.txt:364-369`. `cbrn_commission_nerve_suppression` and the Sarin/Soman preparation controls inherit that gate.
- The historical Japan Chemical campaign is safely inactive through `cbrn_japan_chemical_campaign_shared_adapter_is_valid = { always = no }` in `common/scripted_triggers/cbrn_chemical_delivery_triggers.txt:15-17`; its selector and attack decision are hidden and cannot commit costs.
- Legacy commander Chemical abilities are safely unavailable through `cbrn_chemical_ability_target_receipt_is_valid = { always = no }` in `common/scripted_triggers/cbrn_chemical_raid_triggers.txt:150-155`.
- The installed script surface cannot remove a selected respirator model directly from deployed divisions. The implementation leaves native division-equipment losses to the engine and debits only the separately issued-mask ledger; it does not use a stockpile debit or estimated field loss as a substitute.
- Live raid target presentation, random native outcomes, equipment collection, AI campaign pacing, UI readability, and long-duration cleanup are user-owned in-game validation. Their absence from this source audit is not a source defect.

## Explicit skipped or inactive surfaces

- Continuous Chemical air missions are absent. `common/scripted_effects/chemical_air_bomb_effects.txt` contains no release effect; `events/chemical_air_bomb_events.txt:10-18` only clears legacy heat/flag state and never reschedules; `cbrn_prepare_chemical_action_record` explicitly rejects `continuous_air_mission` at `common/scripted_effects/cbrn_exposure_effects.txt:670-673`. Idle aircraft cannot contaminate.
- Ground Chemical operations and nerve suppression are inactive behind the false hooks listed above. Their player controls are not dead-visible and their resolvers cannot commit payload or operational costs without the missing proof.
- `Air Is Still Breathable`, `No Wind Is Friendly`, `The Antidote Arrived`, and `Unbroken Supply Corridor` are absent from active achievement registry, triggers, GFX registration, and localisation. Unreferenced archived DDS triplets are harmless archive material.
- Hardened Mobile Plant is removed rather than approximated.
- National MIO names and exact live production-share claims are skipped.
- The Japan Chemical campaign and legacy commander abilities are inactive rather than adapted through a neutral condition receipt.
- Legacy direct Chemical contamination remains unreachable: `chem_apply_state_contamination` is enclosed by `always = no` in `common/scripted_effects/chemical_ability_effects.txt:476-482`.
- No active broad all-country CBRN resolution pulse was found. The `every_country` use in `common/on_actions/chaosx_on_actions_chemical_warfare.txt:12-41` is startup migration/tactic synchronization, not exposure targeting or contamination resolution.
- Doctrine does not create or reveal camp/genocide infrastructure and mitigates only Condemnation. Biological lifecycle potency remains `Tularemia < Anthrax < Plague < Smallpox`, only Smallpox uses the severe result, and ordinary native biological raid success factors remain agent-neutral.

## Readiness recommendation

**NOT READY**

The supported core cannot be certified while active selected-state Chemical raids and Chemical doomsday releases satisfy mandatory condition proof with outcome-derived or fixed weather/terrain-style inputs. After that source blocker is removed without a proxy, neutral receipt, fallback, or estimator, the remaining engine-bound routes may stay fail-closed and live consumer validation may remain user-owned. The accepted eleven-achievement disposition and migration ledger also need one authoritative documentation promotion before a completion claim.

## Closure re-audit - 2026-07-29

This section supersedes the initial readiness recommendation above and is limited to CW-B1 and CW-B2.

### CW-B1 - CLOSED

The patched active Chemical routes no longer manufacture environmental, command, evidence-control, Condemnation-context, forecast, or friendly-risk receipts.

- All eleven selected-state raid IDs remain active in `common/raids/cbrn_chemical_air_raids.txt:63-834`. Their outcome wrappers converge on `cbrn_resolve_chemical_air_raid_outcome`, which calls the shared prepare/dispatch pair at `common/scripted_effects/cbrn_chemical_raid_effects.txt:301-327`. The route writes a positive `cbrn_action_release_efficiency_mult` only when native reserved payload consumption and intended delivered dose are both positive (`:177-197`); no optional condition field or condition-proof writer remains in the raid adapter.
- Chemical doomsday supplies only its explicit positive batch-release receipt at `common/scripted_effects/cbrn_chemical_doomsday_effects.txt:132-134`, after exact allocated payload/debit inputs, and then uses the shared prepare/dispatch pair at `:138-173`. The former fixed weather, terrain, density, command, forecast, and friendly-risk receipt helper is absent.
- Restricted camp dispatch derives only release efficiency from positive Chemical Readiness and the selected method factor in `common/scripted_effects/cbrn_camp_effects.txt:69-75`. Its readiness gate is `common/scripted_triggers/cbrn_camp_triggers.txt:18-24`, and its exact-state route enters the shared prepare/dispatch pair at `common/scripted_effects/camp_repression_rework_effects.txt:4426-4467`. Neither adapter file writes optional condition fields or condition proof.
- The shared contract now separates release proof from optional conditions. `cbrn_action_release_is_resolved` requires `cbrn_action_release_efficiency_mult > 0` (`common/scripted_triggers/cbrn_triggers.txt:376-379`), and `cbrn_prepare_chemical_action_record` rejects a missing/non-positive release at `common/scripted_effects/cbrn_exposure_effects.txt:722-729`. The calculator initializes optional condition locals to zero and reads/applies them only under `cbrn_action_conditions_are_resolved` (`:326-360`, `:380-388`, `:534-540`, `:585-590`, `:609-614`), so an absent optional receipt is omitted rather than replaced by a neutral multiplier.

The unsupported live weather/terrain boundary therefore remains honestly absent and no longer blocks these supported routes.

### CW-B2 - OPEN

The eleven-achievement disposition is promoted on the principal current-state surfaces: `docs/systems/cbrn_warfare/overview.md:119`, `common/scripted_effects/cbrn_achievement_effects.txt:5-6`, `docs/plans/chaos_warfare_system_plans/2026-07-29_near_completion_improvement_loop_closure.md:146`, `docs/plans/chaos_warfare_system_plans/documentation_state.md:32-40`, `docs/plans/chaos_warfare_system_plans/documentation_cleanup_handoff.md:50-55,73,79`, and `docs/plans/chaos_warfare_system_plans/2026-07-13_requirement_traceability_and_migration_ledger.md:171,176-185,210`. The active registry contains exactly eleven entries at `common/achievements/chaos_redux_achievements.txt:3714-3768`, and the four skipped achievement names have zero matches across the active registry, trigger, GFX, and localisation files.

Two current completion records still contradict that promotion:

- `docs/plans/chaos_warfare_system_plans/2026-07-29_near_completion_improvement_loop_closure.md:203-225` labels the section superseded and not an open core blocker, but line 225 still says the three unavailable-receipt achievements remain explicit completion blockers.
- `docs/specs/chaos_warfare_system_specs/handoffs/completion_audit_checklist.md:128` still leaves final reachability, localisation, icon, anti-exploit, and package-scenario evidence for the eleven active achievements unchecked.

No skipped achievement is requested for implementation, and this is not a runtime achievement defect. CW-B2 remains a documentation/accepted-disposition blocker until those two completion records agree with the promoted eleven-achievement supported scope.

## Updated readiness recommendation

**NOT READY**

CW-B1 is closed. CW-B2 remains the sole blocker in this narrow re-audit.

## Final narrow closure check - 2026-07-29

This section supersedes the preceding narrow re-audit recommendation. CW-B1 remains closed and was not re-opened or re-audited.

### CW-B2 - CLOSED

- `docs/plans/chaos_warfare_system_plans/2026-07-29_near_completion_improvement_loop_closure.md:225` now states that the three unavailable-receipt proposals remain omitted and archive-only when no exact hooks exist and do not block supported-core readiness.
- `docs/specs/chaos_warfare_system_specs/handoffs/completion_audit_checklist.md:127` now marks the eleven active achievements' source-audited reachability predicates, localisation, icon triplets, anti-exploit receipts, and package scenario evidence complete.

The two recorded CW-B2 contradictions are resolved. No skipped achievement has been reopened or requested.

## Final supported-core recommendation

**READY**

CW-B1 and CW-B2 are closed. Previously recorded genuine engine and user-owned validation boundaries remain allowed and do not prevent supported-core readiness.
