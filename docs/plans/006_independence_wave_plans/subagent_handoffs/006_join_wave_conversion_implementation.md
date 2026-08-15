# Event 006 Join-Wave Conversion — Implementation Handoff

## Ownership and changed files

- `common/script_constants/006_independence_wave_constants.txt` adds `independence_wave_join` thresholds, cooldown, ordinary Event 006 report IDs 36–39, and history payload values.
- `common/scripted_triggers/006_independence_wave_join_triggers.txt` owns source eligibility, reduction proof, and the explicit zero-host predicate.
- `common/scripted_effects/006_independence_wave_join_effects.txt` owns the peak baseline, package probe, one-row plan, report dispatch, accept/decline lifecycle, history receipt, cleanup, and post-mutation failure route.
- `common/on_actions/006_independence_wave_join_on_actions.txt` observes both belligerents on `on_war_relation_added`, then evaluates only scoped state-control, peace-conference, capitulation, and release callbacks.
- `events/006_independence_wave_join.txt` defines `chaosx.nr6.36` (normal offer), `.37` (hidden accept), `.38` (hidden decline), and `.39` (normal failure receipt).
- `localisation/english/006_independence_wave_join_l_english.yml` supplies the four report titles/descriptions/options and is stored as UTF-8 with BOM.
- `docs/events/006_independence_wave/join_wave.md` documents the player-facing and transaction contract.
- Narrow shared zero-host edits are in `common/scripted_effects/006_independence_wave_package_planner_effects.txt`, `common/scripted_effects/chaosx_liberation_release_effects.txt`, `common/scripted_triggers/chaosx_liberation_release_triggers.txt`, and `common/scripted_triggers/006_independence_wave_join_triggers.txt`.

No formable GUI/category generator, IW031 portrait, broad diplomacy copier, or unrelated country package was changed.

## Identifiers and exact invariants

- The source is rejected when it is absent, an active Event 006/Event 005 origin, an Event 006 registry-owned tag, the Event 012 `africa_priority_member_package_active` carrier flag, already pending/active, or in the timed `independence_wave_join_cooldown`.
- The callback baseline is `independence_wave_join_peak_owned_state_count`. War entry records a pre-loss observation for both belligerents. A country first encountered after a peaceful loss reconstructs the baseline from the larger of current territory and its core-state footprint. Later callbacks only raise the peak. No world iteration is used.
- The source must be independent and at peace. This prevents conversion from erasing an active war or silently escaping an overlord.
- Thresholds are `reduction_percent = 50`, `minimum_states_lost = 2`, and `cooldown_days = 90`.
- The plan call uses `liberation_plan_mode.triggerable_scenario`, `liberation_plan_owner.independence_wave`, and one expected country. A package probe can leave at most one selected row.
- The package list is the current content-attested set: IW-001, 002, 004, 006, 007, 008, 009, 010, 012, 014, 017, 018, 019, 023, 024, 026, 027, 028, 029, 030, 033, 041, 070, 071, 072, 173, and 184. Every probe calls the existing `independence_wave_reserve_package_iw_*` wrapper; no package setup is duplicated.
- After a wrapper returns, `global.liberation_plan_states` row delta must equal the source's current `num_owned_states`, and `every_owned_state` must confirm that no source state remains outside the current reservation. Any mismatch invokes the coordinator's reversible candidate rollback. Together these checks are the exact all-remaining-owned-state contract.
- `independence_wave_join_conversion_active` is raised for the single-flight reservation probe so the shared host-capacity helper can admit a candidate whose complete footprint equals every remaining source state; failed probes clear the contribution and this flag before the next trial, and it is cleared on decline, success, or failure receipt. `independence_wave_join_zero_host_allowed` is set only for the accepted source during execution.
- Shared host validators allow equality only while `global.independence_wave_join_active_plan_id` equals the active liberation plan identifier and the owner remains Event 006. The normal path still requires a surviving protected host state. The join path skips capital relocation because every host state is about to transfer, but retains pre-mutation ownership, controller, and core snapshots.
- Offer, accept, and decline compare the stored plan identifier, plan owner, source, selected package, phase, and selected count. A stale report clears only join-local state and cannot abort or inherit a newer shared release plan.
- Accept reconstructs `independence_wave_join_target` from `global.liberation_plan_countries^0` before locking, so the delayed report option does not depend on short-lived event-target persistence. It then invokes `liberation_release_lock_plan` and `independence_wave_execute_standalone_frozen_plan`; package setup, generic focus assignment, force/package mechanics, final validation, Event Log/history, and commit remain the ordinary Event 006 path. `change_tag_from = ROOT` is evaluated in the target scope only after the commit phase and only when the source was human.
- Decline clears package metadata, reservations, scope marks, coordinator arrays, pending flags, target pointers, and applies the cooldown. Post-mutation failures emit `.39`; if compensation is still legal, `liberation_release_execute_compensating_rollback` is used before cleanup.

## Source validation performed

- Required offline Paradox wiki pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and the scripted GUI/interface pages.
- Required vanilla documentation was consulted for effects/triggers, event targets, variables, `change_tag_from`, `release`, `every_owned_state`, scoped on_actions, and script constants. Vanilla on_action precedents were checked for `on_state_control_changed`, `on_peaceconference_ended`, `on_capitulation_immediate`, and release callbacks.
- Required Chaos Redux skills were read: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
- Mandatory narrow MCP event inspection returned partial structural evidence for `chaosx.nr6.36`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e473a8c4e127209786d7c756195be20a819cb67423b8cf5b5021e7d0c7a062b1/46af0c604b25c112e99be9cca265c4ce2fe4be66af6fd935de87879d1aa4841d/event-trace-550da12aba6a.json`. The deterministic package probe has no weighted package-selection probability. The probability adapter cannot resolve it without a declared custom-pool manifest, so no normalized probability claim is made.
- Static review checked touched IDs, package wrapper names, unsupported broad daily callbacks, and the shared-plan call sequence. No Hearts of Iron IV executable was launched.

## Simplifications and remaining risks

- The package candidate order is explicit rather than an engine-backed generated array, because the current package registry exposes adapter effects but no safe runtime enumeration surface. The list is limited to the attested adapters above and should be regenerated when the registry changes.
- Event inspection/render evidence is partial and source-linked only; the probability/map Transport-closed blocker remains. Parent review and user live validation remain required.
- Existing package adapters may have identity-specific assumptions about a surviving former host. The ordinary final-validation path is deliberately retained; any adapter that cannot satisfy the explicit zero-host branch fails closed and emits the failure receipt rather than receiving a bespoke unsupported copy path.
