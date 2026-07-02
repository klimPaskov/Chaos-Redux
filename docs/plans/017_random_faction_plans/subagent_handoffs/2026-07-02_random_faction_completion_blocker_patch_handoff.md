# Event 017 Random faction completion blocker patch handoff

Date: 2026-07-02
Owner: parent implementation pass

## Source blocker report

The previous read-only completion audit at `docs/plans/017_random_faction_plans/subagent_handoffs/2026-07-02_random_faction_completion_audit.md` marked Event 17 partial/incomplete.

## Blockers addressed

| Blocker | Resolution |
| --- | --- |
| AI target choice used too few matrix factors | Added option triggers for regional reach, common enemy, positive relations, bloc strength, pressure state, and updated AI chance modifiers. |
| Evolution I scheduled too many neighbor responses | `random_faction_apply_regional_pressure` builds `random_faction_current_region_targets` and schedules at most one regional follow-up. |
| Evolution II/Evolution III were too global/neighbor-only | Added region bucket helpers with neighbor, same-continent, and coastal fallback caps; Evo II and Evo III reuse the bucket. |
| Evo III cascade could use nested scopes incorrectly | Added `random_faction_dispatch_current_country_choice`; cascade/commitment targets now open their own forced-choice event instead of joining through a parent-root helper. |
| Cleanup missed lifecycle/world-end paths | Added targeted on-actions for leave faction, capitulation/uncapitulation, puppet/release/subject annexation/annexation/government change, and `random_faction_cleanup_after_world_end` called by world-end launchers. |
| Corridor mission had weak proof | `random_faction_corridor_objective_secured` now requires route plausibility through direct border, faction-neighbor, or shared coastal reach plus convoy reserve. |
| Liaison Web did not prove distinct targets over time | Added `random_faction_liaison_web_candidate_targets`, `random_faction_start_liaison_web_candidate`, hidden event `chaosx.nr17.83`, and 180-day snapshot validation. |
| Frontier Commitment did not check all core border states | Added `random_faction_frontier_commitment_objective_secured` with capital and core-border control proof. |
| Not Everyone was global instead of regional | It now checks `random_faction_current_region_targets` and the country-local `random_faction_not_everyone_region_candidate`. |
| Animated assets were registered but not visible | `GFX_random_faction_bloc_pressure_seal_animated` is used by `random_faction_convene_neutrality_council`; `GFX_random_faction_border_warning_animated` is used by both timed missions. |
| Missing scripted-system and asset handoff evidence | Added scripted-system architect handoff and local asset completion handoff. |

## Files changed by blocker patch

- `common/script_constants/chaosx_random_faction_constants.txt`
- `common/scripted_triggers/017_random_faction_triggers.txt`
- `common/scripted_effects/017_random_faction_effects.txt`
- `common/decisions/017_random_faction_decisions.txt`
- `common/on_actions/017_random_faction_on_actions.txt`
- `events/017_join_faction.txt`
- world-end launcher files that now call `random_faction_cleanup_after_world_end`
- `localisation/english/017_join_faction_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/017_random_faction.md`
- `docs/assets/017_random_faction/gfx_handoff.md`

## Validation performed

- Checked braces on Event 17 script, triggers, decisions, on-actions, events, and GFX files.
- Checked localisation BOM on touched Event 17 localisation files.
- Ran `git diff --check`.
- Ran targeted scans for unsupported `<=`/`>=`, fixed faction-name implementation hardcode, world-end cleanup wiring, Liaison Web proof wiring, and animated sprite usage.

## Remaining risk

The regional bucket is intentionally a bounded country-array model using neighbor, same-continent, and coastal reach rather than a formal map-region id.
