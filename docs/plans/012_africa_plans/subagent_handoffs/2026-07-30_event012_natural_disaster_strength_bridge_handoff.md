# Event 012 -> Event 013 hostile nature-call strength bridge handoff

Date: 2026-07-30.

Status: complete for the bounded Event 012 caller-side strength bridge. No Event 013 gameplay source, country tag, map, GUI, 3D asset, or world-order readiness surface was changed, and no commit was created.

## Changed files

- `common/script_constants/012_africa_action_constants.txt` adds the fixed-point `africa_natural_disaster_strength` tuning category.
- `common/scripted_effects/012_africa_action_effects.txt` adds `africa_prepare_hostile_natural_disaster_strength`, seeds its inputs from the existing action target, and calls it from `africa_call_hostile_natural_disaster_from_action` before `call_natural_disaster = yes`.
- `docs/events/012_africa/natural_disaster_weapons.md` documents the strength ladder, scale mapping, observability variable, and unchanged Event 013 boundary.
- This handoff records the architecture, migration, validation, artifacts, risks, and follow-up notes.

## Helper map

| Helper or call site | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `africa_prepare_hostile_natural_disaster_strength` | Event 012 host country | Temporary `africa_natural_disaster_weapon_action_id`, temporary `africa_natural_disaster_weapon_cost_reserved`, regular `event_target:natural_disaster_call_target_country`, live host route flags, `africa_ecological_wrath`, and `africa_continental_war_readiness` | Temporary `africa_natural_disaster_weapon_strength`, five `natural_disaster_call_*_scale` inputs, and intermediate strength/scale temporaries | No new persistent target or flag; clamps the strength and all five public scales; the caller persists only the last attempted strength | `africa_call_hostile_natural_disaster_from_action` in the existing full-result path |
| `africa_call_hostile_natural_disaster_from_action` | Existing resolved action target, then existing Event 012 host target | Existing action ID, reservation proof, exact hostile target, and helper outputs | Existing Event 013 result ledger plus `africa_last_natural_disaster_call_strength` | Preserves the regular selected-country target, passes the five scales and existing hostile proof fields to `call_natural_disaster`, then relies on existing Event 013 reset and Event 012 cleanup | `africa_apply_current_action_outcome` on a full action outcome only |

## Constants and tuning table

`africa_natural_disaster_strength` centralises the base/floor ladder, route strengths, reserved-payment and drought increments, ecological and readiness increments, selected-target factory/state thresholds, and five fixed-point scale increments.

The route floor is priority promotion 2, committed covenant 3, favour-and-wrath 4, warfare doctrine 5, and capstone 6, with capstone precedence rather than additive intermediate flags.

The base strength is 1 and the maximum is 10. A valid reserved nature-call payment adds 1 point, and `defy_the_drought` adds 1 point.

Ecological wrath above the existing Africa measure bands 25, 50, and 75 adds one point per band; continental war-readiness above 50 and 75 adds one point per band.

The exact selected enemy adds one point when it exceeds 30 factories and one point when it exceeds 12 controlled states; these two points are an impact-envelope adjustment so the same actor's disaster is not normalised to a minor target, not a claim that target size increases Africa actor capability.

Starting from a base scale of 1.00, each point above strength 1 adds death 0.20, building damage 0.18, warning chance 0.05, recovery burden 0.15, and supply disruption 0.20.

All five scales are clamped against Event 013's shared `natural_disaster_call_scale.minimum` and `.maximum` constants (0.25 and 4.00).

## Event-target and cleanup plan

The existing action target still executes `save_event_target_as = natural_disaster_call_target_country` immediately before entering the host scope.

The helper reads only that regular target for target-size scoring; it does not iterate countries, select a replacement, widen to a region, or create a global target.

The Event 013 public wrapper still receives `natural_disaster_call_target_mode = selected_country` and `natural_disaster_call_target_country_supplied = 1`, so exact-target semantics remain unchanged.

Event 013 resets its public temporary inputs after `call_natural_disaster = yes`. Event 012 retains the existing 180-day cooldown, accepted/rejected flags, reservation cleanup, and `africa_cleanup_action` lifecycle; the helper adds no persistent flag or event target that requires a new cleanup hook.

## Migration from duplicated logic

Before this change, the caller set severity and other public API fields but left every optional impact scale absent, causing Event 013 to default all five scales to 1.00.

The caller now seeds the action ID and reservation from the same `PREV` target used by the existing severity check, invokes one local helper, stores its strength for auditability, and passes the resulting scales through the unchanged public API.

Event 013 remains the source of truth for family selection, exact target-state eligibility, scale validation, sequence allocation, result identifiers, reports, news, aftermath, and reset behavior.

## Balance scenarios

| Scenario | Strength | Death | Building | Warning | Recovery | Supply |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Priority route, `petition_the_rain`, no pressure/readiness band, reserved payment | 3 | 1.40 | 1.36 | 1.10 | 1.30 | 1.40 |
| Priority route, `defy_the_drought`, wrath above 25, readiness above 50, reserved payment | 6 | 2.00 | 1.90 | 1.25 | 1.75 | 2.00 |
| Capstone `defy_the_drought`, wrath/readiness above 75, target above both size thresholds | 10 (clamped) | 2.80 | 2.62 | 1.45 | 2.35 | 2.80 |

These scenarios preserve the existing severity ladder while making route progression, live pressure, war readiness, payment, action choice, and selected-enemy impact envelope materially visible in Event 013's random disaster impact.

## Validation and MCP evidence

Static inspection confirmed the new helper is called only from the existing Event 012 full-result caller, all five Event 013 scale inputs are initialised before the public call, all scales are clamped to Event 013 bounds, and no new `on_daily`, `on_weekly`, `on_monthly`, country tag, map, or GUI surface was added.

The focused arithmetic check reproduced the three scenario rows above (strength 3, 6, and clamped 10) with death/building/warning/recovery/supply outputs of 1.40/1.36/1.10/1.30/1.40, 2.00/1.90/1.25/1.75/2.00, and 2.80/2.62/1.45/2.35/2.80.

Offline wiki and vanilla documentation were consulted for event targets, `check_variable`, `set_temp_variable`, `multiply_temp_variable`, `clamp_temp_variable`, random-event contracts, and script constants. Existing Chaos Redux precedents confirm direct `num_of_factories` and `num_of_controlled_states` reads and `event_target:* = { ... }` target-size checks.

Read-only Event Chain Viewer artifacts were captured before and after the patch: workspace-wide scan `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b98086096f66616870ab736bffb713f818c25e5be21cca9cce93309ad8c027c0/3304ed69de65d3bcf5213bf216e8c240d2f6e390e153d0e0164db48401b46b6a/event-scan-f84da2c23776.json`, Event 012 state-flow inspection `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8e4a4460ed74f28ef2692104d6f2925d7ee309e788597bdd30f3954f03c651b/839801c15c60ed0da0497cfbb1d9b276315d8e25d9c2ec3bc3868cd4657dabef/event-state_flow-f84da2c23776.json`, Event 013 state-flow inspection `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eeed12260b65db7ccead89681d923c478e784a3016d83e963351e754c3ae1c0f/31889213122bc1ea7e864eadfb839c991843cf5abd1bda62091c1018c48040c4/event-state_flow-f84da2c23776.json`, and post-patch source lint `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cd7070ea0a27617deafbbceb8c6b8cecf6822b9220910d919f54b3e958ebdc4/ff7376821df28b966008d3a5ccd95de219f95c0399228d23b9866d94bed718e9/event-lint-f84da2c23776.json`.

The MCP analyses were partial because the workspace-wide helper projection was deferred and the inline source inventory was limited to 64 paths; the artifacts report 2,022 non-blocking diagnostics/unresolved analyses. The relevant Event 012 and Event 013 source contracts were therefore checked directly against the repository and vanilla documentation.

No live Hearts of Iron IV run was performed because in-game execution is parent/user-owned and prohibited for this subagent.

## Risks and limitations

The strength helper intentionally uses a bounded additive ladder rather than changing Event 013 family probabilities or target selection, so a random family can still be rejected when the selected enemy has no eligible controlled state.

Warning scale increases with impact strength, preserving a larger visible warning window for larger disasters; this is a signal-visibility choice, not a damage reduction, and does not reduce deaths, damage, recovery burden, or supply disruption.

The caller copies action and reservation values through the existing `PREV` scope pattern. If a future caller changes the action-target nesting, that copy must be re-audited with the Event 012 action contract.

No fallback or simplification was introduced. No additional asset, localisation, country, map, GUI, or world-order work is required for this bounded bridge.
