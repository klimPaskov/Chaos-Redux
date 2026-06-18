# Event 012 Africa Settlement-Fork Decision Audit Handoff

Date: 2026-06-18
Subagent scope: Protected Seat and Regional Authority Office settlement additions around Authority Atlas historical dossiers.

## Files Inspected

- `common/decisions/012_africa_decisions.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `common/ai_strategy/012_africa.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`

Required references consulted: repo `AGENTS.md`, `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, offline wiki decision/event/trigger/effect/localisation/scope/on-action/modifier/idea/AI pages, vanilla decision documentation, vanilla trigger/effect documentation, script constants documentation, and vanilla decision precedent.

## Patch Applied

Changed file:

- `common/scripted_effects/012_africa_effects.txt`

Changed scripted effect ids:

- `africa_start_dossier_resistance_watch_for_selected_observer_settlement`
- `africa_start_dossier_resistance_watch_for_selected_protected_settlement`
- `africa_start_dossier_resistance_watch_for_selected_direct_archive_settlement`
- `africa_start_dossier_resistance_watch_for_selected_regional_office_settlement`

Before:

- Watch-start helpers required both no active watch and no `africa_archive_resistance_dossier_id`.
- Successful and failed reports intentionally keep stored dossier/seat context for localisation.
- After the first resistance watch resolved, the old stored context could therefore block later settlements from creating a new watch, even though `africa_dossier_resistance_watch_active` had been cleared.

After:

- The four watch-start helpers now gate only on historical dossier, stored selected seat, and no active watch.
- A new settlement after the previous watch resolves can overwrite the stored dossier/seat context and create its own resistance watch.
- The one-at-a-time exploit protection remains through `africa_dossier_resistance_watch_active` and `can_africa_settle_selected_dossier`.

## Findings Sorted by Severity

### High: Patched stale-context watch lock

Resolved locally in `common/scripted_effects/012_africa_effects.txt`. The stale `africa_archive_resistance_dossier_id` guard could make only the first post-settlement watch playable. The fix is narrow and inside the existing helper family.

### Medium: Persistent report context remains intentional but fragile

`africa_complete_dossier_resistance_watch` and `africa_fail_dossier_resistance_watch` leave stored dossier/seat/mode context in place so report text and category status can name the finished case. New watch starts clear the success/failure and method flags, then overwrite the stored id/seat. This is playable, but if report events are evaluated late after the player immediately starts another settlement, the text could theoretically reflect the new context. A broader fix would split active watch context from last-report context; I did not patch that because it is a larger helper design change.

### Low: No blocking route/cost/localisation/doc mismatch found

Protected Seat and Regional Authority Office requirements, spends, watch modes, AI strategy, category header text, and docs align with the current implementation.

## Decision Category Lifecycle Notes

- Owner/category: African unifier, `africa_authority_atlas_category`.
- Visibility and route locks: the category remains tied to the Authority Atlas surface; the two new settlement decisions are gated by selected dossier local office, old-seat guard, secured old-seat state, unsettled dossier, and no active resistance watch.
- Protected Seat route: requires respect/federal/sovereign-seat route state plus Regional Trust and Authority gates.
- Regional Authority Office route: requires regional authorities plus documents-before-consent or Authority Register state, then Authority and League Cohesion gates.
- Further settlements are blocked while `africa_dossier_resistance_watch_active` exists; after success/failure, later settlements can proceed and start new watches after this patch.
- Reset/cleanup surfaces clear protected/regional watch mode flags and fork counters through the existing runtime and Authority Atlas cleanup helpers.

## Mission Quality Notes

- `africa_selected_dossier_survey_mission`: owner African unifier; category Authority Atlas; region selected historical dossier seat; duration `africa_decision_days.dossier_survey`; success opens/surveys the selected dossier; failure raises Restoration Debt and Local Sovereignty pressure and allows retry; duplicate risk is controlled by active survey and archive guard flags.
- `africa_archive_guard_deadline_mission`: owner African unifier; category Authority Atlas; region stored surveyed dossier seat; duration `africa_decision_days.dossier_review`; success requires local office, guard, settlement, and secure stored seat; failure raises Restoration Debt and sovereignty pressure; duplicate risk is controlled by stored mission context and active flag.
- `africa_dossier_resistance_watch_mission`: owner African unifier; category Authority Atlas; region stored settled dossier seat; duration `@africa_dossier_resistance_watch_days`; success requires stored seat security plus settlement-mode value gates; failure applies mode and generic pressure penalties; duplicate risk is controlled by the active watch flag and, after this patch, no longer turns into a permanent one-ever lock.
- `africa_mediate_dossier_resistance_watch`: timed decision, not a mission; duration `africa_decision_days.dossier_resistance_intervention`; resolves observer/protected watches if context remains valid; otherwise fails the watch.
- `africa_enforce_dossier_resistance_watch`: timed decision, not a mission; duration `africa_decision_days.dossier_resistance_intervention`; resolves direct/regional watches if context remains valid; otherwise fails the watch.

## Cost and Requirement Clarity Notes

- Protected Seat cost is concrete and spent: political power, infantry equipment, support equipment, and manpower.
- Regional Authority Office cost is concrete and spent: political power, support equipment, train equipment, and manpower.
- Mediation cost is concrete and spent: political power, support equipment, manpower, plus profile logistics.
- Enforcement cost is concrete and spent: political power, infantry equipment, support equipment, manpower, command power, plus profile logistics.
- Profile logistics are gated and spent by profile: convoys, infantry equipment, motorized equipment plus army XP, or trains. Vanilla precedent uses generic train equipment gates with `train_equipment_1` spends, so the regional-office and southern-profile train handling is consistent enough for this slice.
- Localisation exposes the same costs and threshold gates used by triggers/constants.

## AI Validity and Route-Lock Notes

- The two settlement decisions have route/profile-sensitive `ai_will_do` modifiers.
- AI strategy bands exist for protected-seat and regional-office active watches, including production/build nudges for infantry, support, trains, infrastructure, and restraint.
- Mediation and enforcement AI weights prefer routes that match the branch and lower willingness on routes that should avoid that intervention style.
- No dead country targets or unsafe target scopes were found in this slice; watch state uses stored dossier id and state variables, not country targets.

## Localisation and Tooltip Gaps

- No blocking localisation gap found.
- The Authority Atlas header exposes all four fork counters plus local watch status.
- Requirement/cost/effect tooltips for protected seats, regional offices, mediation, enforcement, and passive watch completion reflect current triggers and costs.
- Scripted localisation covers resistance dossier name, seat name, settlement mode, intervention method, watch status, and profile resolution.

## Cleanup and Exploit-Risk Notes

- Patched exploit/blocker: stale report context no longer prevents later watches from being created.
- The active watch flag remains the one-at-a-time lock, so players cannot start multiple watch interventions at once.
- Mediation/enforcement set an intervention-active flag and the passive watch completion trigger blocks while that flag is active, preventing double-resolution by passive success during an active timed intervention.
- Settlement helper checks prevent repeat-settling the same selected dossier.
- Remaining risk: report context persistence is serving two purposes, active context and last-report context. It is currently playable after the patch, but a future helper split would be cleaner.

## Validation

- Confirmed `NOT = { has_variable = africa_archive_resistance_dossier_id }` no longer exists in the four watch-start helpers.
- Confirmed `africa_dossier_resistance_watch_active` remains in all four watch-start helper limits and in the base settlement trigger as the one-at-a-time gate.
- Confirmed protected/regional settlement decisions call their matching mark effects, spend their displayed resources, then advance the selected dossier.
- Confirmed mediation/enforcement trigger and effect paths include the new protected/regional modes.
- Confirmed `git diff --check` reports no whitespace errors on the scoped files.

Skipped validation:

- No in-game run was performed from this subagent audit. The validation here is static and task-specific.

## Remaining Issues and Recommended Fixes

1. Consider a future cleanup in `common/scripted_effects/012_africa_effects.txt` and `common/scripted_localisation/012_africa_scripted_localisation.txt`: split active watch variables from last-report variables if event text ever proves late-bound against a newly started watch.
2. No immediate patch recommended for route locks, costs/spends, manpower/equipment/train handling, category header visibility, AI behavior, or docs alignment in the audited slice.
