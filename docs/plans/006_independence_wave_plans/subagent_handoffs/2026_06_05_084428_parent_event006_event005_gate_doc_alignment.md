# Event 006 Event 005 Gate Alignment

Parent tranche: 2026-06-05 08:44 UTC

## Changed files

- `docs/events/006_independence_wave.md`
- `common/scripted_triggers/006_independence_wave_triggers.txt`

## Scope

Aligned the Event 006 documentation with the current resolver behavior after the Event 005-origin candidate/host suppression gate was removed from gameplay script.

## Before

- The live Event 006 trigger file no longer contained `has_independence_wave_soviet_collapse_runtime_state` or direct `soviet_collapse_*` gate checks in the release candidate path.
- `docs/events/006_independence_wave.md` still claimed candidate gates rejected Soviet Collapse origin, breakaway, event-created republic, and high-chaos successor flags.
- The ITZ package gate in `can_independence_wave_use_candidate_tag` had an extra indentation level.

## After

- The Event 006 documentation now says candidate gates use Event 006-owned origin, existence, package, state, and host-survival checks and do not read Soviet Collapse runtime flags.
- The ITZ package gate indentation now matches the surrounding package gates.

## Validation

- Follow-up validation should confirm no `soviet_collapse_*`, `chaosx_release_origin_soviet*`, or `has_independence_wave_soviet_collapse_runtime_state` tokens remain in Event 006 gameplay files.
- This tranche does not claim Event 006 completion.

## Remaining gaps

- Decision/mission tooltip hardening remains open for later targeted decisions.
- Scripted GUI remains a display surface backed by decisions, not an interactive button layer.
- Major route-state animation packages still need source frames, frame sheets, static fallbacks, manifests, and GFX handoffs before final completion.
