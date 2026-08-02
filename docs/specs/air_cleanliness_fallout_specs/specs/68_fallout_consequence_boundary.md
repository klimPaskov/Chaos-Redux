# Fallout consequence boundary and population-loss contract

## Status

This correction is accepted for implementation. Fallout is a world consequence transition. It replaces the retired Final Silence world-end selector row, but it is not an ordinary Event Log event, an evolution entry, or an ordinary super-event. The transition may still use country events for blackout presentation, phase scheduling, recovery, and later survivor chains. Those later chains are ordinary post-consequence content and may keep their own event history.

## Public ownership

`common/scripted_effects/chaosx_events_log_effects.txt` is the public world-end selector registry. Fallout occupies the appended replacement row for the retired Final Silence selector. It is not registered in the ordinary country Event Log or evolution registries. Its stable settings-ledger value lives in `fallout_consequence_id` inside `common/script_constants/fallout_consolidated_constants.txt`, while its world-end selector identity is `world_end_scenario_id = fallout`.

The public world-end selector has a Fallout title, owner, and details branch so the replacement is visible in the world-end settings surface. That selector row is the only Fallout consequence details surface. No ordinary country Event Log row, ordinary evolution, ordinary Event Details card, or ordinary super-event registration is added. The New Zealand survivor card remains a post-consequence card and does not embed a world-end scenario description. The ordinary super-event GUI is hidden whenever `world_end_fallout` is set. The full-screen blackout GUI and dramatic sound remain Fallout-owned.

## Permanent Air Contamination lock

`fallout_air_contamination_permanent_99` is the durable Fallout-owned contamination lock. The standard coordinator and manual route set it through the idempotent `fallout_enforce_permanent_air_contamination` effect after admission. That effect writes exactly 9,900 basis points and assigns all 9,900 basis points to the Fallout source. Chemical, biological, natural, wildfire, volcanic, ash, nuclear callback, and decay inputs are zeroed so no later source can increase or decrease the total. The permanent flag and 9,900 value are authoritative. The temporary `fallout_air_cleanliness_request_paused` flag and `fallout_air_cleanliness_disabled` marker belong only to reversible request validation. The permanent lock clears both. Save migration calls the same lock whenever `world_end_fallout` is already present.

The host manual reconciliation also repairs the permanent 9,900-basis-point lock for an admitted manual transaction after save recovery. It requires a sweep, native-strike, countdown, request, or launcher receipt, so an invalid-intensity error that never admitted the sweep does not change Air Contamination.

The flag is consumed by the Air Cleanliness boundary surfaces:

- `air_contamination_apply_delta_bp` delegates to the idempotent permanent lock instead of applying the requested delta.
- Chemical and biological contribution update, clear, and rebuild helpers reject the permanent flag.
- Natural wildfire smoke, volcanic ash, and ashfall aftermath registration returns zero after the permanent flag. The monthly natural source reservoir and pulse are cleared.
- The Black Plague Air source refresh clears its disease-derived reservoir and previous contribution after the permanent flag.
- The global state modifier and country pressure tiers remain active against the fixed 9,900-basis-point value.
- `air_winter_system_enabled` treats the permanent flag as an enabled Air system even if the pre-Fallout settings toggle was off.
- `fallout_transition_active` pauses the Air Winter begin, state, event, and finalize work while the blackout and world rewrite own the state snapshot.
- Air Winter resumes through its ordinary host-owned monthly route after `fallout_transition_active` clears. Its phase, exposure, recovery, adaptation, food, shelter, water, reclamation, building, supply, military, disease, population, mapmode, and normal-map consumers continue against the fixed atmosphere.
- Treaty membership eligibility, pending invitations, decision visibility, host lifecycle pulses, and late violation callbacks remain closed after Fallout.
- The Air Cleanliness settings checkbox and exported settings row show the value as permanently locked. The settings toggle cannot alter it, and the scripted GUI click trigger rejects `fallout_air_contamination_permanent_99`.

The permanent lock is deliberately separate from the retired Final Silence marker. Fallout is terminal for the Air Contamination value, but it does not disable the Air Cleanliness and Air Winter consequences that consume that value.

Startup reconstruction re-enters the idempotent lock when a saved game already carries the permanent Fallout flag. Legacy saves that still carry an active Final Silence world-end flag retire that runtime flag and queue the same Fallout request coordinator. The completed Final Silence cause-memory flag remains available for historical text and achievements, while the old wave callbacks no longer have an active trigger.

Once the locked snapshot is ready, the admission transaction settles all active wars, exiles, volunteers, and civil-war targets before blackout presentation. The later diplomacy transaction remains responsible for subjects, access, markets, trade, intelligence, and its exhaustive map-return receipts.

Retired Final Silence callbacks cannot take ownership of the Air Contamination value or replace the Fallout request coordinator.

## Standard Fallout population loss

The accepted state loss ladder is defined in `common/script_constants/fallout_consolidated_constants.txt` by `fallout_population_loss_percent`:

| State grade | Direct population loss |
| --- | ---: |
| Remote refuge | 90 percent |
| Scarred province | 91 percent |
| Ash zone | 92 percent |
| Dead city | 93 percent |
| Wasteland | 94 percent |
| Vitrified zone | 95 percent |

`fallout_apply_transition_phase_population_loss` scans every valid state in the frozen world snapshot. `fallout_apply_state_population_loss` computes the grade-specific target from the captured pre-transition population. `fallout_reconcile_population_loss_receipt` records the live delta and calls `chaos_meter_register_deaths` with `chaos_deaths_reason = fallout_aftermath` after the state population mutation. The receipt is generation-bound and idempotent. The standard path therefore deletes 90 to 95 percent from each state and feeds the same loss into the Deaths ledger rather than applying a variable-only shortcut.

Fallout-owned registration is mandatory even if the general Deaths setting is disabled. The shared Deaths effect and exact population-loss helper explicitly admit the request-time pause, Fallout transition, active Fallout, and manual scenario flags. Ordinary non-Fallout losses retain the setting gate. New Fallout receipts therefore resolve to zero-loss or registered-loss only.

The shared `air_contamination_update_threshold_flags` effect rebuilds the 25, 50, and 75 percent read model for the fixed value but suppresses ordinary contamination news while `fallout_air_contamination_permanent_99` is set.

## Manual sweep population loss

The manual scenario captures every state's pre-strike population before native strike callbacks. Each struck state is then processed by `fallout_manual_apply_state_aggregate_consequence`. The aggregate death percentage is clamped between `fallout_manual_aggregate.death_percent_base` and `fallout_manual_aggregate.death_percent_max`, which are the approved 90 and 95 percent endpoints.

The effect computes the exact remaining-population target, supplies the state population-loss contract, and calls `apply_exact_state_civilian_population_loss`. Its provenance receipt then measures the complete pre-strike-to-post-strike loss after native callbacks and exact reconciliation, adding that observed amount to `global.fallout_manual_total_civilian_deaths` and `chaos_state_civilian_deaths_total`. After the state loop, `fallout_manual_apply_aggregate_consequences` calls `chaos_meter_register_deaths` with civilian mode enabled, `chaos_deaths_reason = fallout_aftermath`, and state population application disabled because the exact state mutations have already occurred. This prevents double deletion while keeping the complete observed loss in the Deaths system rather than only the direct mod adjustment.

The later standard population phase reuses the same frozen survivor target but reads live `state_population_k` after native and aggregate mutations. It requests only the remaining delta. When the aggregate already reached the target, the standard receipt records zero loss and does not issue another Deaths registration. The frozen pre-strike population is retained for provenance and target arithmetic only.

Manual receipt validation uses the generation-bound preflight live-baseline value for the mutation's before-loss population. Ordinary Fallout rows retain the frozen pretransition-baseline check. A manual row therefore cannot pass by silently substituting a stale snapshot, and a correct zero-loss reconciliation remains durable.

After each state records its synthetic Fallout intensity and expiry ledger, `fallout_manual_apply_state_aggregate_consequence` removes the ordinary `nuclear_fallout_state` modifier. A native strike therefore cannot leave a second daily nuclear Air contamination or Deaths source behind the durable fixed Fallout source.

## Engine-sensitive proof boundary

The state mutation and aggregate Deaths routing are source-proven by the effects named above. The vanilla references document `launch_nuke` inputs but do not prove an exact engine-native sweep across every valid installed-map province. The manual scenario therefore remains dormant behind its existing static proof gate. No variable-only fallout, one-strike-per-state substitute, or public Event Details registration may be presented as equivalent proof. Live playtesting is a later user validation handoff and is not a completion requirement for the static core-mechanics tranche.

## Review checklist

- Fallout replaces the retired Final Silence row in the world-end selector registry.
- Fallout has no ordinary Event Log row, evolution entry, or ordinary super-event registration.
- Fallout blackout display text and audio remain dedicated to the consequence transition.
- Air Contamination is permanently locked at 99 percent by `fallout_air_contamination_permanent_99`.
- Wildfire, volcanic, ashfall, treaty, settings, and delta boundaries consume that flag.
- Air Winter resumes after the transition pause and continues to consume the fixed 99 percent atmosphere.
- Standard and manual state population loss both use the approved 90 to 95 percent band.
- Both paths record the observed civilian loss through Deaths after state population mutation.
- Fallout-owned Deaths registration remains mandatory when the general Deaths setting is disabled.
- The exact native manual sweep remains blocked by missing static engine proof, not by missing user live validation.
