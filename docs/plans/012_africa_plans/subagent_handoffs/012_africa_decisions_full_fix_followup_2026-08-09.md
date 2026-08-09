# Event 012 bounded-roster and cancellation follow-up

Date: 2026-08-09

Owner: `chaosx_decision_mission_auditor` (`/root/event12_decisions_finish_now`)

Scope: repair of the two recurring Event 012 country-roster scans and the shared cancellation result path. Actions 71-76 and GUI layout remain excluded.

Patch boundary: only the bounded-roster and cancellation hunks listed below are in this follow-up. Event 019 provider additions, the diaspora returnee jobs/education gate, and strange-force selection sounds remain unstaged and were deliberately preserved for their owners.

## Changed source and behavior

- `common/scripted_effects/012_africa_effects.txt`
  - `africa_refresh_bounded_african_target_roster` now iterates the maintained `africa_relationship_countries` array.
  - `africa_refresh_bounded_external_target_roster` now iterates maintained package, Scramble, sponsorship, and registered-war-partner arrays.
  - New registration helpers preserve relationship/overlay/target validity, selected-target capacity, duplicate suppression, and target flags.
  - The 14-day profiled AI cycle therefore consumes maintained bounded rosters instead of opening `every_country`; the player and RSA refresh entry points keep the same helper contract.
- `common/scripted_effects/012_africa_action_effects.txt`
  - `africa_refresh_priority_member_natural_disaster_targets` now enters `event_target:africa_host` and iterates the same maintained Event 012 arrays. `ROOT` remains the priority member, so the existing hostile-target trigger and member-owned `africa_natural_disaster_enemy_targets` array remain correct.
  - `africa_register_current_natural_disaster_roster_target` suppresses duplicates and caps the member array at `constant:africa_capacity.maximum_selected_target_cap` (16), while allowing existing entries to survive a full roster check.
  - `africa_cancel_action` now snapshots the last action id, outcome, objective, and generation, marks history, saves `africa_action_result_target`, and fires `chaosx.nr12.220` before idempotent cleanup. Cancellation now follows the normal resolve-result event path without changing Action 71-76 semantics.

Changed identifiers: `africa_register_current_ai_african_roster_target`, `africa_register_current_ai_external_roster_target`, `africa_refresh_bounded_african_target_roster`, `africa_refresh_bounded_external_target_roster`, `africa_register_current_natural_disaster_roster_target`, `africa_refresh_priority_member_natural_disaster_targets`, and `africa_cancel_action`.

## Timeout grammar decision

The shared missions retain `days_mission_timeout = FROM.africa_active_action_duration_days`. The offline Data structures page supports scoped variables and dual-scope references, and installed `dynamic_variables_documentation.md` documents `days_mission_timeout`; vanilla `common/decisions/CHI_decisions.txt` supplies dynamic timeout precedents. Event lint accepts the source with zero blocking diagnostics. No unsupported fallback or host-global substitute was introduced. Runtime target-scope proof remains a parent/live-session item.

## Event 012 `every_country` classification after the repair

Only explicit one-shot passes remain:

1. `common/scripted_effects/012_africa_effects.txt:138` (`africa_build_prefire_contact_pool`) is an explicit pre-fire temporary contact census, then frozen to 3-5 contacts.
2. `common/scripted_effects/012_africa_effects.txt:247` (`africa_select_weighted_prefire_host`) is the explicit fire-once host selector; its temporary candidate pool is cleared.
3. `common/scripted_effects/012_africa_world_order_effects.txt:29` (`africa_world_emit_super_event`) is one-shot per global super-event gate and iterates only human clients to play audio.
4. `common/scripted_effects/012_africa_world_order_effects.txt:848,872` is the post-unification Scramble participant census. It is guarded by initialization state, uses `participant_census_cap`, and records `africa_scramble_interest_census_complete`.
5. `common/scripted_effects/012_africa_world_order_effects.txt:1500,1527,1554,1581,1608,1635` are six continent-specific package-foundation passes. They run only from explicit package installation/successor resolution, are guarded by package flags and `africa_world_package_polity_foundation_initialised`, and register into constituent arrays.

The previously recurring paths are absent from the 14-day profiled AI cycle and 180-day natural-disaster AI refresh. No Event 012 `every_country` remains in `012_africa_action_effects.txt`, `012_africa_ai_profile_effects.txt`, or the bounded refresh helpers.

## MCP evidence

- Fresh focused event lint after the staged source repair used selector `chaosx.nr12.220` and returned `EVENT_INSPECTED_PARTIAL`, revision `9fb823494441deea77896128d266200c2f4f1bf6181ccb426606e85ca6450e12`, graph hash `6daddf91d20fcc32ee00e955d9e53c4869cb97dfc60dbd9e7e14745e31c25d16`, zero blocking diagnostics, and one informational workspace-deferral diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ff083f5519b19b1d6bd6f5731e6c4c2caaef18f5a350d9561b49b613b5fab15/d13db521b22b1d93573e0f697a42c11995648da99273b2eab72d2ba3b7069581/event-lint-9fb823494441.json`.
- Fresh probability inspection used adapter `random_list` on `common/scripted_effects/012_africa_action_effects.txt` after the retained patch was present. It returned `PROBABILITY_SOURCE_INSPECTED`, source revision `b4858b795aeb0f2640b7de4b902fe15844be55d8e1a2d5fac9739cf867598b9a`, source hash `9198d32858855561ed62a2fd86524dd407e64375eb92a9e8eae482488194c9f1`, 14 candidates, zero required inputs, one unresolved construct, and `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dea2894f8102e8ea065ad15c593571cc42b1e3239cfaadf0d1fdddbf581292ff/dc3d65f996a97c2ec01eeee55dedcda4ba331a07938ce6076698fa30b4e57ea6/probability-inspect-9198d3285885.json`.
- The retained Event 012 probability audit remains the supporting scenario evidence for the same action surface: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_ai_probability_audit_2026-08-06.md`. It classifies dynamic target identity as unresolved because the adapter does not resolve `random_scope_in_array` and classifies action/decision AI as bounded score-only rather than normalized click probability. No balance target was changed by this follow-up.

- Event lint (fresh after the source repair): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7451b698dba51ce673c6b222da69908ce08d803f29da470c6b9a2730c9a6d857/35348d2fd670e1acbe862d5abeb12d798de9e130949c584989e24b26fe7d3f69/event-lint-0da00e5a91a9.json`. Status `EVENT_INSPECTED_PARTIAL`; 0 blocking diagnostics. The workspace report is intentionally partial because helper projections and the inline source inventory are bounded by MCP limits.
- Main decision probability inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2437fdc5d8d9028eaf4cbea5eba68fcff0796c479d85e8b6aa12da2250a8fedf/0518243e16e721787171d9d89d09336adf6d0c365d57fc686edb3c63627c05af/probability-inspect-3c0d9e2379a8.json` (`decision_ai_will_do`, 207 candidates, 23 required inputs, 0 unresolved, `poolComplete=false`).
- Priority-member decision probability inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81058cadc109446c6b828a3acefafe8ead84b77f848e228c41eab04608759ffa/f421b1401c52e3b96411d5f746adb8cbe99d87b1e597adee561a16b77a498841/probability-inspect-8c5b3a7eae78.json` (54 candidates, 15 required inputs, 0 unresolved, `poolComplete=false`).
- Mission adapter on the shared decision source returned `PROBABILITY_SURFACE_EMPTY`; these missions are system-owned and receive AI selection through the controller decision, so no direct mission score comparison was available.

## Validation and remaining uncertainty

- Source search confirms no `every_country` in `common/scripted_effects/012_africa_action_effects.txt`; the profiled AI file has no country scans; only the five explicit one-shot groups above remain in Event 012 sources.
- The host-wrapped array loop mirrors existing Event 012 host-transfer/RSA `for_each_scope_loop` precedents (`PREV` is the array element and `ROOT` remains the actor).
- The staged index contains only the two scripted-effect files and these bounded-roster/cancellation hunks; the explicitly preserved Event 019 provider, returnee-gate, and sound hunks remain unstaged in the working tree.
- No game launch was performed. Mission timeout target-scope behavior and runtime event presentation still require parent/live-session confirmation.
- No source simplification was introduced and no Action 71-76 code was changed by this follow-up.
