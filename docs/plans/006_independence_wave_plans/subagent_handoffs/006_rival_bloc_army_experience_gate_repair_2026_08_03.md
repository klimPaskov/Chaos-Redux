# Event 006 rival-bloc army-experience gate repair

Date: 2026-08-03.

Scope: verify and restore the engine-backed army-experience trigger used by the Event 006 rival-bloc leadership mission. The supplied flag-atlas error family was already closed separately; this handoff records the independent source diagnostic found by the completion re-audit and its current corrected source state.

## Patch

`common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt` uses:

```text
army_experience > constant:independence_wave_rival_bloc_cost.leadership_army_experience
```

instead of reading the engine resource through `check_variable`. The helper is consumed by both `available` and `custom_cost_trigger` in `common/decisions/006_independence_wave_rival_bloc_decisions.txt`, so the leadership mission evaluates the same concrete resource in both surfaces. The current checkout contains the corrected expression; no duplicate gameplay diff is staged by this documentation-only receipt because the source was concurrently restored in the shared worktree before commit.

## Validation

- The previous `check_variable` reference at the leadership gate is absent.
- The trigger remains centralized and uses the existing tuning constant; no magic number or new fallback was added.
- The Event 006 flag audit remains clean: 102 registered tags, 102 complete flag families, 0 incomplete.
- The fresh focus inspection remains source-clean for Event 006 geometry: 184 focuses, 192 connectors, no crossings, intersections, long connectors, or too-close pairs.

## Boundary

This is a narrow source repair. It does not promote a package, change the accepted focus-tree design, alter flags, add advisor art, or claim whole-event completion. The whole event remains HOLD / PARTIAL under the current completion authority.
