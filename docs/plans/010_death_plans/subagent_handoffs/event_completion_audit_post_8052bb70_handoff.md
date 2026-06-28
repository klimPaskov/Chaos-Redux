# Event 010 Death Completion Audit After 8052bb70

Audit date: 2026-06-15
Auditor: chaosx_event_completion_auditor
Scope: read-only audit after commit `8052bb70` against `docs/specs/010_death_specs/{specs,matrices,prompts}`, current plans, and the prior latest audit handoff.

## Verdict

Parent resolved the active completion blocker identified by this audit.

Commit `8052bb70` resolves the prior host-budget, strict world-end target-filter, named-achievement, SCN-006 host-spawn, Event Details late-preview, and DTH convoy-history blockers by static inspection. This audit identified one remaining blocker in the world-end continent gate: `death_create_world_end_footholds` skipped a continent if any state on that continent was ever consumed, not if Death currently had an active presence there. The parent fix replaces that historical guard with active Death-presence helpers.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Shared Death ghost-host budget and caps | Resolved by static inspection | `common/scripted_effects/010_death_effects.txt:1979` prepares a global budget from consumed states, consumed population, and world-end footholds; spawn helpers at `common/scripted_effects/010_death_effects.txt:1998`, `common/scripted_effects/010_death_effects.txt:2024`, and `common/scripted_effects/010_death_effects.txt:2051` check shared spend and per-tier caps. |
| Natural/focus/world-end/SCN-006 host paths | Resolved by static inspection | Natural tier helpers are at `common/scripted_effects/010_death_effects.txt:2099` and `common/scripted_effects/010_death_effects.txt:2123`; DTH focus rewards call those helpers at `common/national_focus/010_death_focus_tree.txt:253`, `common/national_focus/010_death_focus_tree.txt:420`, `common/national_focus/010_death_focus_tree.txt:438`, and `common/national_focus/010_death_focus_tree.txt:456`; SCN-006 calls them at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1960` and `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1966`. |
| World-end foothold fallback target tiers | Resolved after parent fix | Target tiers relax from strict to relaxed, defended, then last resort in `common/scripted_triggers/010_death_triggers.txt`; each continent uses the tier chain in `common/scripted_effects/010_death_effects.txt`, and the outer skip condition now checks active DTH-controlled wasteland presence rather than historical consumption. |
| World-end owner/controller war declaration | Resolved by static inspection | `death_declare_war_on_current_state_owner` saves owner/controller event targets and declares war when possible at `common/scripted_effects/010_death_effects.txt:247`; foothold creation calls it before consumption at `common/scripted_effects/010_death_effects.txt:2236`. |
| Achievement predicates named in prior blocker | Resolved by static inspection | Defeat marking now uses capital-continent mainland counters, Last Ferry consumption credit, Counted Every Name cleanliness/coordination/pre-800 gates, and Black Tide foothold/Herald checks in `common/scripted_effects/010_death_effects.txt:1516`; helper triggers are at `common/scripted_triggers/010_death_triggers.txt:433` and `common/scripted_triggers/010_death_triggers.txt:504`; tooltip text matches at `localisation/english/chaosx_achievements_l_english.yml:413`. |
| Event Details late preview gate | Resolved by static inspection | Mainland reveal, Last Shores, and world-consumed previews are gated behind `death_world_reported` at `common/scripted_effects/chaosx_events_log_effects.txt:1450`. |
| SCN-006 cleanup and budgeted host behavior | Superseded by the current Death evolution/scenario rework | `trigger_death_scenario` now uses one Instant Outbreak type, consumes intensity-scaled islands and mainland reveal states, creates intensity-scaled starting hosts directly, charges the host counters afterward, and clears scenario context. It no longer launches Last Shores from the triggerable scenario path. |
| DTH country history convoys | Resolved | `history/countries/DTH - Death.txt:1` through `history/countries/DTH - Death.txt:24` has no `set_convoys`. |
| Active obsolete Spirit of War/Peace surfaces | Resolved in active files checked | Targeted search across `events`, `common`, `localisation`, `interface`, `history`, `docs/events`, and `docs/assets` found no active `Spirit of War`, `Spirit of Peace`, `spirit_of_war`, or `spirit_of_peace` hits. Remaining mentions are in specs/prompts/audit history, not active player-facing surfaces. |

## Resolved Audit Blocker

### World-end can skip a continent where Death has no active foothold

Source requirement:

- `docs/specs/010_death_specs/specs/010_death_spec_part_1_core_flow.md:100` says the world-end branch creates "a random coastal foothold ... on every remaining continent that does not already contain Death."
- `docs/specs/010_death_specs/specs/010_death_spec_part_2_mechanics.md:158` defines world-end as simultaneous continent footholds and front pressure.

Audit finding before parent fix:

- `common/scripted_effects/010_death_effects.txt:2265` through `common/scripted_effects/010_death_effects.txt:2391` guards each continent with `NOT = { any_state = { is_on_continent = <continent> death_is_consumed_state = yes } }`.
- `death_is_consumed_state` is permanent historical consumption. Recaptured states keep that status: `common/scripted_effects/010_death_effects.txt:2410` through `common/scripted_effects/010_death_effects.txt:2428` applies recaptured wasteland and counts foothold recapture, but does not and should not clear `death_consumed_state`.

Impact:

If Death consumed a state on a continent earlier and was pushed out before Last Shores, that continent "does not already contain Death" in the active gameplay sense, but the world-end foothold creation skips it because the historical consumed-state flag remains. The new fallback target tiers do not help this scenario because they only run after the continent passes the initial skip condition.

Recommended fix:

Replace the per-continent skip predicate with an active Death-presence predicate rather than historical consumption, for example a helper that checks for a state on the continent that is currently controlled by `DTH` and has `death_active_wasteland` or `death_consumed_state`. Keep the target filters excluding already consumed states so a new foothold is still placed on an unconsumed coastal state.

## Accepted Plans And Disposition

| Plan or handoff | Disposition |
| --- | --- |
| `docs/plans/010_death_plans/focus_tree_depth_followup_plan.md` | Implemented in the 26-node DTH focus tree; no new blocker found in this focused audit. |
| `docs/plans/010_death_plans/improvement_loop_remaining_routes_addendum.md` | Implemented or promoted across living-country routes, achievements, Black Oath/Apostolate, Black Atlas, and docs; no unresolved planner addendum found for the post-8052bb70 blockers. |
| `docs/plans/010_death_plans/subagent_handoffs/event_completion_audit_latest_handoff.md` | Resolved by parent commits. The final narrowed world-end foothold presence/skip mismatch is recorded above with its parent resolution. |

## Meaningful Validation

Performed:

- Compared the world-end foothold branch to the source spec and current event documentation.
- Followed the changed host-spawn paths from natural helper, focus rewards, world-end creation, and SCN-006 to the shared budgeted helpers.
- Checked the named achievement predicates against their helper triggers and tooltip text.
- Checked Event Details late-preview registration for the `death_world_reported` gate.
- Checked the new owner/controller war declaration pattern against local/vanilla event-target declaration precedents and HOI4 docs for `save_event_target_as`.
- Checked `clamp_temp_variable` and variable-to-variable `check_variable` usage against vanilla documentation and existing repo patterns.

Not performed:

- No in-game runtime validation of SCN-006 Instant Outbreak, world-end foothold creation after recapture, or Event Details rendering.
- No full parser/load validation in the HOI4 engine. Static syntax/precedent review did not reveal a new engine-risk blocker in the changed budget, declaration, or SCN-006 logic.

## Asset And Documentation Gaps

No new active asset blocker was found in this focused post-commit audit. I did not re-audit DDS dimensions, audio, frame sheets, or generated-art manifests.

The event documentation now accurately describes the shared host budget, stricter achievements, late Event Details gate, and active Death-presence world-end foothold guard after parent resolution.

## Remaining Blockers

No implementation blockers remain from this focused audit after parent resolution.

## Parent Resolution

Resolved after this audit. `common/scripted_triggers/010_death_triggers.txt` now defines per-continent active Death-presence helpers that require current DTH control plus an active/consumed Death wasteland marker, and `death_create_world_end_footholds` now uses those helpers for the per-continent skip guards. Recaptured historical wastelands no longer prevent Last Shores from creating a fresh foothold on a continent where Death has no active controlled presence.

## Recommended Next Actions

1. Runtime validate a Last Shores/SCN-006 run where Death previously consumed and then lost a state on a continent before world-end. Confirm the continent still receives a foothold if DTH has no active state there.
2. Runtime validate Event Details before and after `death_world_reported` to confirm only origin/island previews appear before reveal and late previews appear after reveal.

## Improvement Loop Recommendation

Do not spawn `chaosx_improvement_loop_planner` for this audit result. The identified issue was implementation fidelity to the existing source spec, not missing design depth, and it has been resolved. The accepted improvement addendum already appears implemented or closed.
