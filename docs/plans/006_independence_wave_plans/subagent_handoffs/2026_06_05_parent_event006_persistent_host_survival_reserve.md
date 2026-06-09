# Event006 Persistent Host Survival Reserve

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `common/scripted_effects/006_independence_wave_effects.txt`.

`independence_wave_clear_pending_candidate_state` no longer clears `independence_wave_host_survival_reserved` from `event_target:independence_wave_protected_host_state`.

## Reason

The completion auditor found that host-survival protection was set before a release and then immediately cleared during generic candidate cleanup. That made the immediate release resolver safer, but it meant later release passes and Border Commission targeting could not rely on the reserve state.

The reserve flag is intentionally read by:

- `can_independence_wave_host_release_current_candidate_safely`
- `is_independence_wave_border_commission_target_state`
- reduced release footprint selection helpers

Keeping it persistent makes the documented host-survival contract match active behavior: later Event006 releases and targeted border-transfer decisions cannot consume the host state reserved for survival.

## Validation

Passed parent validation:

- brace balance returned `0` for the scoped Event006 event, news, on_action, decision, idea, AI strategy, focus, script constant, scripted effect, scripted GUI, scripted localisation, scripted trigger, interface, and localisation files
- unsupported less-equal/greater-equal operator scan found no invalid script tokens in the scoped Event006 files
- scoped `git diff --check` returned clean
- localisation BOM check passed for `006_independence_wave_l_english.yml`, `chaosx_countries_l_english.yml`, and `chaosx_achievements_l_english.yml`
- host-survival flag reference scan found no remaining `clr_state_flag = independence_wave_host_survival_reserved`

## Remaining Scope

This does not complete the full Event006 source-spec pack. It only closes the concrete persistent host-survival blocker found during the generic-playability completion audit.
