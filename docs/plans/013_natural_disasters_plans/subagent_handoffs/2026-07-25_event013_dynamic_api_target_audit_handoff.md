# Event 013 dynamic API and target-domain audit

Date: 2026-07-25

## Scope

This audit covers the reusable Event 013 call wrapper, target and origin validation, delayed sequence geography, external callers, Evolution-gated family eligibility, category selection, and scripted GUI state preparation.

The required Chaos Redux skills, offline Paradox wiki pages, vanilla documentation, Event 013 specification and implementation resume prompt, architecture plan, call-contract matrix, event scripts, queue and state-control hooks, category definition, and abnormal-path scripted GUI were reviewed before editing.

Read-only MCP inspections were also performed before the local patch.

## Concrete defects corrected

`natural_disaster_resolve_target` no longer falls through to a random country after a selected-state sequence or a caller-provided sequence with a pinned state has already consumed its first hit.

The blocked segment is now left unresolved and counted as skipped, preserving the caller's exact state domain instead of silently teleporting a later segment.

`natural_disaster_select_ocean_impact_proxy` now preserves pinned-state and caller-provided state domains, and its final random-country branch is limited to `random_valid`, `coast`, `nearby_enemy`, and `dense_state` modes.

Ocean Skyfall proxy candidates now honor nearby-enemy and dense-state predicates through the state-scope trigger `natural_disaster_ocean_proxy_target_matches_mode`.

Invalid selected-state, selected-country, selected-region, or caller-pinned ocean requests therefore fail or skip without widening to a global exposed coast.

`natural_disaster_validate_call` now rejects standalone top-level calls that request `natural_disaster_log_mode.none`.

Silent mode remains available only when the validated internal physical-chain continuation proof is present.

Target-state, target-country, caller-cost, caller-cooldown, and target-legitimacy proof inputs are now fail-closed binary values.

Any value outside `0` or `1` is rejected with the existing target or scenario reject reason instead of being treated as an implicit proof.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `natural_disaster_ocean_proxy_target_matches_mode` | State scope with `ROOT` as the originating call scope | `ROOT.natural_disaster_call_target_mode`; current state's neighbor ownership or population density | Boolean trigger result | None | Two state candidate limits in `natural_disaster_select_ocean_impact_proxy` |
| `natural_disaster_select_ocean_impact_proxy` | Country caller scope with state and country candidate subscopes | Existing target mode, supplied target event targets, resolved origin family, and target-domain inputs | `natural_disaster_impact_state`, `natural_disaster_target_country`, candidate proof temporaries | Saves regular event targets and candidate proof flags only | `natural_disaster_resolve_target` ocean-origin branch |
| `natural_disaster_resolve_target` pinned-domain guard | Country caller scope | `natural_disaster_path_target_required`, target mode, supplied state proof, and sequence index | Existing resolved/skipped target behavior | Prevents fallback widening; no new state is created | Existing Event 013 sequence planner |

No new public wrapper or generic router was introduced.

## Constants and tuning table

No new constants were needed.

The patch reuses `natural_disaster_target_mode.*`, `natural_disaster_log_mode.*`, `natural_disaster_call_reject_reason.*`, and existing scale and threshold constants from the Event 013 script-constant files.

No severity, death, building, supply, warning, recovery, evolution, delay, or AI tuning values were changed.

## Event targets and cleanup

No new event targets were introduced.

The patch keeps `natural_disaster_call_target_state`, `natural_disaster_call_target_country`, `natural_disaster_impact_state`, and `natural_disaster_target_country` as regular short-lived event targets owned by the existing call chain.

The existing `natural_disaster_reset_call_inputs` cleanup still clears caller inputs after `call_natural_disaster` returns.

The new silent-log validation prevents a top-level accepted sequence from bypassing the existing history row and cleanup lifecycle.

Delayed queue workers, aftermath cards, affected-controller reports, and state-control transfer cleanup were inspected and were not changed.

## Migration plan

Existing callers require no call-site edits because Event 013, Event 099, triggerable scenarios, and event clusters already select an explicit target mode, supply the required target proof, and use a history-bearing log mode.

The Event 013 physical follow-up remains the only live use of `log_mode.none`, `sequence_id_override`, and `internal_chain_override`.

If a future subsystem needs to join an existing sequence, it must add a separately validated causal continuation contract rather than reusing the reserved fields directly.

## Validation evidence

The touched effect and trigger files have balanced Clausewitz braces: `8678/8678` and `902/902`, respectively.

`git diff --check` reported no whitespace errors for the touched files.

The new trigger has one definition and two call sites.

The Event 013 geography registry was cross-checked against vanilla state and strategic-region IDs before the patch; all registered state IDs were within the 1081 vanilla states and all region IDs were within the 304 vanilla strategic regions.

The read-only Event 013 scan produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36bed4e036f56194ba58757b3569998995472ca8732b0f268405c93d276cfb68/33ab5b7fc7a04fa4ba05bc7d865c10994329bcf863f2f6ada2812ea1e911d817/event-scan-bc0cffe127f8.json`.

The read-only GUI inspection produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea92a6d5c272dbb5394f96fce9568bae5858b8c9cd16f43ba35ece7565d60c3c/459661c9ad8908ecbacdb4779255e97787fc2ed1d5aaaceaf1cfd56182257c20/gui-inspect.93b627f38ca8b7bb.json`.

The read-only map inspection produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c54a6ebcf5c289b3df6a0087487254e1119c40c66f882c4d4dda5e0b881f0e8/9b23486146dcc242622011c2db09635af05e89c479fda020651c0d40c7c3ce17/map-inspect.ddf7a3fc21cc2627.json` and confirmed valid state-region membership for sampled states and regions.

The narrow scripted-effect lint request produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0dc5d2357b274b91da78a9692dfe9a5f0e53d570916f5d96172a1d500ffd3c36/60eb1907e8ef34350b5bb250ad988b6ff4811005082944b061c3e2a10c992c3d/event-lint-40d0a73babf6.json` but the MCP tool reported a partial whole-game scan rather than targeted inline diagnostics.

## Skipped checks and limitations

The game was not launched, in accordance with repository policy that live HOI4 validation belongs to the user.

The GUI inspector reported an unknown `player_context` vocabulary and a missing window for the queried alias; the source uses `natural_disaster_abnormal_path_window`, and the same analyzer warning affects many existing Chaos Redux scripted GUIs, so no GUI rewrite was justified.

The map inspector also reported unrelated existing building-position and port-adjacency diagnostics outside Event 013.

The draft architecture's separate death or damage override mode names are not live API fields; the implementation uses validated death, building, compatibility damage, warning, recovery, and supply multipliers.

`natural_disaster_gui_selected_record_exists` now rejects negative persisted selected indices before any selected-array dereference.

No fallback or mechanic simplification was introduced in this audit scope.
