# Stage 9 Targeted Occupation Decision and Mission Audit Handoff

Audit date: 2026-07-25.

Scope was limited to engine and transaction safety for the Stage 9 occupation package.

No assets, GFX, shared pipelines, specs, matrices, or unrelated gameplay files were edited.

## Changed files

- `common/decisions/cbrn_occupation_decisions.txt`
  - Replaced `state_trigger` with the current vanilla and offline-wiki `state_target` field for `cbrn_nerve_suppression_sarin`, `cbrn_nerve_suppression_soman`, `cbrn_deploy_protective_aid`, `cbrn_seal_state`, `cbrn_destroy_contaminated_records`, `cbrn_admit_accidental_release`, and `cbrn_permit_inspection`.
  - The installed `common/decisions/_documentation.md` conflicts with those current game files by naming the field `state_trigger`. Because current 1.19 vanilla decisions are the engine-consumed precedent and use `state_target` throughout, this package follows `state_target` and records the documentation conflict instead of relying on the contradictory spelling.
  - After: the engine receives the current vanilla-proven state targeting key, `FROM` is the selected state, and the actions retain their existing `any` or `any_controlled_state` target domains.
- `common/scripted_triggers/cbrn_occupation_triggers.txt`
  - Added `NOT = { has_state_flag = cbrn_occupation_external_aid_project_active }` to `cbrn_occupation_state_can_receive_external_protective_aid`.
  - Before: separate suppliers could begin concurrent aid projects against the same state before either completed.
  - After: the first active delivery reserves the state until completion or cancellation, while removal clears the same flag before final delivery revalidation.
- `common/on_actions/cbrn_occupation_on_actions.txt`
  - The `on_state_control_changed` state scope now clears `cbrn_occupation_target_loss_risk_cleared` for every control transfer.
  - Before: a hold-clearance proof could survive a loss and later recapture of the state.
  - After: any control change invalidates that proof, requiring a future verified provider to establish it again.
- `docs/plans/chaos_warfare_system_plans/stage_9_decision_mission_audit_handoff.md`
  - This audit handoff.

## Findings, sorted by severity

1. Critical, resolved against the current vanilla precedent: every state-facing action used `state_trigger`, while current 1.19 vanilla state-targeted decisions and the offline wiki use `state_target`.
   - The installed `common/decisions/_documentation.md` contradicts those files by naming `state_trigger`. The conflict is retained in this handoff rather than hidden.
   - Current vanilla files are the working engine-consumed examples required by `AGENTS.md`, so `state_target` governs this implementation.
   - The replacement is mechanical and does not alter target eligibility, resource costs, durations, or effects.

2. High, unresolved external integration blocker: nerve suppression deliberately remains fail-closed until verified condition inputs and the target-loss clearance proof are supplied.
   - `cbrn_occupation_country_can_prepare_nerve_suppression` requires the `cbrn_occupation_*` condition variables validated by `cbrn_occupation_action_conditions_are_supplied`.
   - `cbrn_occupation_state_is_valid_nerve_target` also requires `cbrn_occupation_target_loss_risk_cleared`.
   - Within the audited files, those inputs are consumed, copied into the action context, or cleared, but are not supplied by a verified adapter.
   - This is safe because it blocks the release before payload debit. It also means the two nerve actions cannot complete until the external adapter establishes fresh values and proof. No approximated target, forecast, weather, terrain, or fallback selector was added.

3. Medium, resolved: target-loss clearance was stale across state-control changes.
   - Clearing the proof from the native state-control hook closes the recapture path without deleting historical records, trauma, cooldown, or discovery data.

4. Medium, resolved: external aid lacked an in-progress state gate.
   - The project flag was written and cleared by the decision, but the state eligibility helper did not read it.
   - The new symmetric gate prevents parallel supplier actions without changing final stock debit behavior.

5. Low, resolved during parent review: Sarin and Soman preparations could previously be started against the same state before either reached final revalidation.
   - Both preparations now reserve the selected state with `cbrn_occupation_nerve_suppression_preparation_active`.
   - The shared reservation is set for the exact preparation duration, blocks the other target entry, and is explicitly cleared on completion, cancellation, or state-control change.
   - Final operation eligibility remains independently revalidated, so the reservation is not treated as authorization or target-loss proof.

## Decision category lifecycle

`cbrn_occupation_measures_category` is visible only when its dedicated visibility trigger passes and remains hidden when it has no visible decisions.

The two authorization decisions are one-time actions with matching visible and available requirement helpers.

The exact-state actions use `target_root_trigger` for country prechecks, `target_trigger` for state eligibility, custom tooltips for the available check, and final helper revalidation for transaction safety.

The two nerve preparations have a 21-day active decision period, cancellation when route, stock, target, or war conditions fail, a 270-day state cooldown after accepted execution, and no cost debit on cancellation.

Protective aid holds political power and civilian-factory commitment at start, marks the selected state as in progress, clears the marker on cancellation or completion, and revalidates supplier and state conditions before external stock is consumed.

The record actions are immediate state-targeted decisions with target-specific availability helpers and re-enable cooldowns.

## Timed mission and objective notes

The package defines no `days_mission_timeout`, `timeout_effect`, or selectable mission blocks.

The three `days_remove` actions are timed decisions rather than engine missions: `cbrn_nerve_suppression_sarin`, `cbrn_nerve_suppression_soman`, and `cbrn_deploy_protective_aid`.

| Timed action | Owner | Category | Region | Requirement | Duration | Success or completion | Failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cbrn_nerve_suppression_sarin` | Acting country | `cbrn_occupation_measures_category` | Exact controlled enemy-owned state | Route, stock, occupation law, unit, safety, forecast, condition-input, and no-active-preparation gates | 21 days | Final revalidation, then shared payload and operation-cost debit followed by accepted execution | Cancels with no debit and releases the state reservation when a final prerequisite fails | Shared reservation blocks a competing Soman preparation |
| `cbrn_nerve_suppression_soman` | Acting country | `cbrn_occupation_measures_category` | Exact controlled enemy-owned state | Same state and country gates with the Soman stock requirement | 21 days | Same final transaction sequence | Same cancellation and reservation cleanup behavior | Shared reservation blocks a competing Sarin preparation |
| `cbrn_deploy_protective_aid` | External supplier | `cbrn_occupation_measures_category` | Exact foreign-occupied non-core state | Supplier program, factory capacity, stock, population, and distribution-gap gates | 21 days | Final state and supplier revalidation, then external stock distribution | Project flag clears on cancellation and no external stock is debited | Resolved for concurrent aid projects by the active-project gate |

## Cost and requirement clarity

The nerve actions correctly use a custom cost display without a parallel political-power `cost` field.

Their tooltip explicitly states that stock is consumed only after final exact-state revalidation, which matches the payload-first and operation-cost-second helper sequence.

Protective aid pays political power at decision start, applies its temporary factory burden during the preparation, and delegates population-scaled stock consumption to the final external-delivery helper.

The two authorization actions and the four record actions use ordinary political-power costs with matching custom trigger tooltips where requirements are nontrivial.

All decision, custom-cost, custom-trigger, and custom-effect localisation keys in the audited decision file resolve in the supplied Stage 9 localisation file.

The occupation-law tooltips resolve in the existing `localisation/english/chaosx_occupation_laws_l_english.yml` file and were not changed.

## AI validity and route-lock notes

`decision_ai_will_do` inspection found six ordinary decision surfaces.

`mission_ai_will_do` inspection classified the three `days_remove` actions as mission-score surfaces. This six-versus-three adapter split reflects timed-action classification; it is not evidence for either state-target field spelling.

The two nerve actions have factor-zero blockers for invalid route or material gates and invalid target or agreement states.

The coercive occupation law starts at zero and has a factor-zero gate through `cbrn_occupation_ai_can_select_coercive_law`.

The restrictive record actions also have explicit factor-zero route blockers.

Protective aid, admission, and inspection remain available to any AI that passes their ordinary availability conditions because they are not destructive route actions.

No weighted scenario was evaluated because no complete country, state, target, stock, or route profile was provided and the audit must not infer one.

## Cleanup and exploit-risk notes

The state-control hook already ends responsible-country operational modifiers, clears delayed backlash scheduling, and conditionally records liberation discovery.

This audit adds target-loss-proof invalidation to that same hook.

Nerve execution rechecks all operation conditions before shared payload debit, then requires a positive payload proof before charging the non-payload operation costs.

No free-unit, equipment-farming, core, war-goal, or cooldown-bypass loop was found in the audited files.

The competing-preparation path is closed by a shared exact-state reservation with completion, cancellation, timed-expiry, and control-change cleanup.

## Task-specific validation

- Consulted the installed HOI4 decision, trigger, effect, scope, state-control, script-constant, and occupation-law documentation plus the required offline wiki pages.
- Recorded the state-target-field source conflict: installed `common/decisions/_documentation.md` says `state_trigger`, while the offline wiki and current vanilla `CHI_decisions.txt`, `AFG.txt`, and the wider current decision corpus use `state_target`.
- Followed the current vanilla `state_target` precedent and confirmed the native `on_state_control_changed` scope contract in installed vanilla on-actions.
- Parent-reviewed `decision_ai_will_do` inspection after the exact-state preparation reservation found six decision surfaces with zero unresolved adapter diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/941a349a0a8ce8cd19942eb114d5ac6054b98db3fd283326e80caecf54a2740e/2da9a715ab4fe7b5ff21d1c09fc6c0ed22ffc0f174a5e08e59b7b9e8a591caab/probability-inspect-1d318e0aa817.json`.
- Parent-reviewed `mission_ai_will_do` inspection after the exact-state preparation reservation found the three timed-action surfaces with zero unresolved adapter diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e0bb1456c0d26b7d64b7dd4e52896cbee0e98fbae1c5d4bf4b8120ee1742f60/f89fa19379f229f4be469682118effe3ba76b7547faabc0a2c64472d62fdee96/probability-inspect-1d318e0aa817.json`.
- The read-only event state-flow inspection produced a bounded partial graph with no package-specific diagnostic. Its global graph cap makes it non-authoritative for this package, so source review remained authoritative: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c70fe9d0ee5a2ebea5c34d26e535d105115599cdda8223e638a3285bda34f134/00c4558d43fc39495326cf4faae6bb9b8a597e4cf6a7640caeecae9a537636a5/event-state_flow-8ec24fbf8233.json`.
- Confirmed seven `state_target` definitions and no remaining `state_trigger` definitions in the scoped decision file.

## Skipped validation

No live game session was launched, as live consumer validation belongs to the user.

No AI score scenario was fabricated, so this handoff reports score-surface discovery and safety gates rather than a probability or timing claim.

## Remaining issues and required follow-up

The package remains blocked from actual nerve-release completion until the verified external condition and target-loss adapters provide fresh values.

No separate expansion plan was created because the unresolved adapter is outside the exact permitted files and must be owned by the parent or its existing adapter surface.

No commit was created.
