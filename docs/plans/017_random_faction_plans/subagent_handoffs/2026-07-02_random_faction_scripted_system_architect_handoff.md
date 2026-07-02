# Event 017 Random faction scripted-system architect handoff

Date: 2026-07-02
Subagent: `chaosx_scripted_system_architect`

## Files inspected

- `AGENTS.md`
- `docs/specs/017_random_faction_specs/`
- `common/scripted_effects/017_random_faction_effects.txt`
- `common/scripted_triggers/017_random_faction_triggers.txt`
- `common/script_constants/chaosx_random_faction_constants.txt`
- `common/on_actions/017_random_faction_on_actions.txt`
- `events/017_join_faction.txt`
- `common/decisions/017_random_faction_decisions.txt`

## Subagent changes

None. The architect returned a read-only handoff.

## Findings

Resolved scripted-system blockers:

- Dynamic faction options are not hardcoded to fixed faction names or country tags.
- AI option logic uses ideology, regional reach, common enemy, relations, bloc strength, and pressure state.
- Evolution I schedules one regional follow-up from the region bucket.
- Evolution III uses `random_faction_current_region_targets` and max-followup gating rather than a global unbucketed country pool.
- Cleanup uses targeted lifecycle on-actions plus Event 17 array refreshes.
- World-end launchers call `random_faction_cleanup_after_world_end`.
- Corridor objective proof requires a valid stored target plus land, faction-neighbor, or coastal route plausibility.
- Distinct liaison target tracking uses `random_faction_supported_minor_targets`.

Architect risk found:

- Liaison Web still unlocked immediately once a leader had three valid supported targets, while the spec asks for a 180-day proof window without target capitulation or direct-enemy failure.

## Parent follow-up patch

The parent resolved the Liaison Web risk after the handoff:

- Added `random_faction_liaison_web_candidate_targets`.
- Added `random_faction_start_liaison_web_candidate`.
- Added `random_faction_check_liaison_web_candidate_achievement`.
- Added hidden event `chaosx.nr17.83`.
- Updated achievement tooltip and event documentation.

The achievement now snapshots the distinct supported target set, waits 180 days, and awards only if the same snapshot still has at least three valid, alive, non-subject targets that are not direct enemies of the leader.

## Remaining risk

The regional bucket is a pragmatic country-array bucket built from neighbor, continent, and coastal reach rather than a formal map-region id. It is intentionally bounded by the Event 17 region bucket and cascade caps.
