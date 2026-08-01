# Event 012 achievement owner closure: B3 tranche (2026-08-01)

## Scope and result

This tranche implements only exact transition owners that are already exposed by the Event 012 action, diaspora, and priority-member systems.

The tranche covers row 24 recognised rival confederation, row 28 measured local project ownership, row 28 local-ownership loss, and the bounded weather-owner closure used by row 38.

No shared acceptance ledger, workbook, asset package, focus tree, country tag, model file, recurring world scan, or generic action-success proxy was edited.

No fallback or simplification was used for rows 30, 32, 33, or 38.

The prior partial-owner handoff's statement that an accepted hostile disaster call proves row 37 civilian weaponisation is superseded by this handoff because the selected hostile target is not a civilian-casualty witness.

## Helper map

| Helper | Scope and exact input | Output and side effects | Exact callsite |
| --- | --- | --- | --- |
| `africa_achievement_record_recognised_rival_confederation` | COUNTRY scope on the priority member after `africa_priority_member_record_rival_bloc_victory`; requires validated player origin, refused League offer, rival-bloc victory, rival relationship, and the existing `africa_host` event target. | HOST receives `africa_achievement_member_refusal_owner_ready`; the helper injects the existing `priority_member_alternative_recognised` milestone and therefore sets `africa_achievement_recognised_african_confederation` through the single milestone owner. | The final host-target block of `africa_priority_member_record_rival_bloc_victory` in `common/scripted_effects/012_africa_priority_member_effects.txt`. The helper remains fail-closed when any exact member predicate is absent. |
| `africa_achievement_record_measured_local_project_ownership` | HOST scope inside the full diaspora investment-bond outcome after the diaspora ledger writes `africa_diaspora_local_ownership_share` from the full-local-ownership constant. | Copies the measured ledger value into global `africa_achievement_local_ownership_share` and sets `africa_achievement_local_ownership_owner_ready`; it does not infer ownership from the startup floor or project count. | `africa_diaspora_apply_full_outcome` in `common/scripted_effects/012_africa_diaspora_effects.txt`, immediately after the full bond host write. |
| `africa_achievement_record_local_ownership_loss` | HOST scope from an exact diaspora housing-failure or diaspora-bond-failure branch after the target receives `africa_diaspora_local_ownership_lost`. | Sets sticky global `africa_achievement_local_ownership_lost`, so a later favourable ownership value cannot erase a real owner loss. | Both failure branches of `africa_diaspora_apply_failure_outcome` in `common/scripted_effects/012_africa_diaspora_effects.txt`. |
| `africa_achievement_record_weather_campaign_backfire` | HOST scope when the existing Event 012 hostile-disaster wrapper records an accepted-call random backfire or a rejected call after the reserved cost/cooldown path. | Sets sticky global `africa_achievement_weather_campaign_backfire`; it is separate from civilian-target, neutral-target, maximum-tier member, and ecological-wrath owners. | Accepted random branch and rejection branch of `africa_call_hostile_natural_disaster_from_action` in `common/scripted_effects/012_africa_action_effects.txt`. |
| `africa_achievement_record_weather_army_defeated` and `africa_achievement_record_weather_war_won` | The accepted Event 013 target is marked on the target country. On capitulation, the target must be the capitulated country and the current Event 012 host must be the direct winner. | Counts one distinct weather-marked target and opens the owner gate plus the existing weather-war milestone. Ordinary peace and third-party victories do not count. | The accepted target branch in `common/scripted_effects/012_africa_action_effects.txt` and the bounded `on_capitulation` owner in `common/on_actions/012_africa_world_order_on_actions.txt`. |
| `africa_achievement_record_weather_member_disaster` and `africa_achievement_record_weather_neutral_african` | Accepted Event 013 calls classify the resolved target using current-generation/cooperative relationship state or an African capital plus the outside relationship state. | Set the corresponding lifetime member-disaster or neutral-African disqualifier. Rejected calls do not classify a target. | The accepted target branch in `common/scripted_effects/012_africa_action_effects.txt`. |
| `africa_achievement_record_weather_wrath_collapse` | Host ecological wrath is checked after clamping at `africa_achievement_ratio.ecological_rampage_threshold`. | Sets the lifetime ecological-wrath collapse disqualifier. | Weather backfire/rejection branches and high-chaos failure resolution in `common/scripted_effects/012_africa_action_effects.txt`. |

The existing `africa_achievement_record_disaster_weaponised_against_civilians` definition remains available for a future exact civilian-damage owner but has no call from the selected hostile-country wrapper.

## Trigger gates and row dispositions

Row 24 now has a real positive owner call from the bounded rival-bloc victory transaction, while its existing rival-count, League-destruction, puppet, and terminal-chaos disqualifier owners remain subject to the broader achievement audit.

Row 28 now has a measured local-ownership writer and a sticky local-ownership-loss disqualifier, while foreign or diaspora government capture and unresolved corruption retain their existing gates and still require their own exact owner review where callers are absent.

Row 30 remains blocked because no exact measured foreign-concession-share writer was found; `africa_achievement_ore_leaves_as_machines_owner_ready` is not opened.

Row 32 remains blocked because no exact project-exploitation-scandal owner was found; `africa_achievement_development_owner_ready` is unchanged and remains closed.

Row 33's earlier B3 audit remains superseded for this surface. The dedicated `012_africa_common_reserve_deployment_2026-08-01.md` handoff now records the deployment, deadline, protected-capital, and offensive-abuse owners; `africa_achievement_common_reserve_owner_ready` is opened only after the first exact deployment. Six-war live acceptance remains blocked.

Row 38 now has bounded owners for distinct weather-marked target defeat, direct host campaign victory, member/neutral-African target disqualifiers, and canonical wrath collapse. The owner gate opens only after a direct host-capitulation receipt; the row remains blocked until three distinct hostile targets and all remaining eligibility conditions are accepted live.

Row 37 is explicitly fail-closed by `africa_achievement_ecological_covenant_owner_ready` because no exact civilian-damage owner replaces the removed accepted-hostile-call proxy; the gate has no writer in this tranche.

## Constants, variables, flags, and event targets

No script constants or tuning values were added.

The measured local-ownership helper reuses the existing full-local-ownership constant written by the diaspora ledger and the existing achievement ratio checks.

The existing `africa_host` event target is the only scope pointer used; no global event target or new target lifecycle was introduced.

The new owner and disqualifier flags are lifetime global flags and do not need cleanup because they represent irreversible achievement evidence or owner readiness.

No timer, deadline, AI weight, duration band, array, or recurring on-action was added.

## Migration plan

Priority-member victory callers should continue to invoke `africa_priority_member_record_rival_bloc_victory`; that function is now the single row 24 positive owner and no package-specific event or decision writes should duplicate the milestone.

The diaspora full-bond branch remains the only measured local-ownership writer for row 28; future project writers must call the same helper only after committing a measured ledger share.

Diaspora housing or bond failures should continue to route through `africa_achievement_record_local_ownership_loss` instead of setting a second achievement flag directly.

Hostile weather actions should continue through `africa_call_hostile_natural_disaster_from_action`; its accepted selected-country result classifies member and neutral-African disqualifiers but is not a campaign-victory proof until the marked target capitulates directly to the current host. Exact backfire/rejection branches retain the backfire disqualifier.

## Risks and unsupported analysis

`africa_priority_member_record_rival_bloc_victory` now has the parent-owned bounded `on_capitulation` caller for a rival priority member defeating the current host. A non-capitulation peace winner receipt remains intentionally deferred; ordinary peace still cannot infer victory.

The Event 013 result does not expose a separate civilian-casualty field to Event 012, so no civilian-damage owner was inferred from accepted result, impact scales, wrath values, or aftermath flags.

The Event 013 wrapper does not expose a delayed campaign-victory or army-defeat callback for the weather call; Event 012 therefore owns the proof through its existing accepted-target flag and bounded `on_capitulation` callback. No Event 013 source edit or broad war scan was introduced.

The MCP event scan returned `status: ok` and `code: EVENT_INSPECTED_PARTIAL` for event `chaosx.nr12.1`, but reported `validation: false` because large-workspace helper and lifecycle analysis was deferred; this is recorded as unresolved partial analysis, not a passing validation.

## Validation performed

The required offline Paradox wiki pages and vanilla documentation for event targets, flags, scopes, triggers, effects, on-actions, and script constants were consulted before editing.

The five touched script files were checked for balanced braces with zero final depth and no negative depth.

Targeted `rg` checks confirmed one definition and the intended callsite for each new helper, no remaining call to the removed hostile-civilian proxy, an exact writer for `africa_achievement_rain_command_owner_ready` after host victory, and no writer for `africa_achievement_ecological_covenant_owner_ready`.

The narrow MCP scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51e43c2c7b9da99ff9ed6a8cd2049bee1168063d64b245125e4381312aa6f85f/184d66a7e4bfc8735de2b31da128521d7b9722740ab242b63231538da88d4367/event-scan-6d2c72dc3531.json`.

The focused MCP lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/929d232d0b8260657ec30262612d36037a7226547f3bc9cedaa98a9dd74e351c/4862ff2a6b83d2a8859730f82dbe783c8843544e14a9b22e1d6fb88da8bf2af3/event-lint-6d2c72dc3531.json` and has the same deferred large-workspace validation status with no blocking diagnostics.

Hearts of Iron IV was not launched and no live-save validation was performed, per repository instructions.

No commit was created because the parent explicitly requested an uncommitted handoff.

## Files changed

- `common/scripted_effects/012_africa_achievement_effects.txt`
- `common/scripted_effects/012_africa_diaspora_effects.txt`
- `common/scripted_effects/012_africa_priority_member_effects.txt`
- `common/scripted_effects/012_africa_action_effects.txt`
- `common/scripted_triggers/012_africa_achievement_triggers.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_b3_achievement_owner_closure_2026-08-01.md`

## Simplifications, omissions, and blockers

No fallback was used.

Rows 30, 32, and 33 remain intentionally incomplete because their exact owner lifecycles or live acceptance are unresolved. Row 38 now has source owners but remains blocked until the three-target campaign proof is observed.

Row 37 remains intentionally fail-closed until an exact civilian-damage owner is implemented.

The parent must carry the MCP deferred-analysis limitation and the unresolved external caller reachability into the final report.
