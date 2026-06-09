# Event 006 Peripheral Host Release Gate

## Scope

Parent-side bugfix for the Independence Wave resolver. This tranche addresses the reported case where firing Event 006 could produce no releases in a normal campaign because the host gate only accepted the invoker or already-weak hosts.

## Changed Files

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `docs/events/006_independence_wave.md`

## Gameplay Change

Added `has_independence_wave_current_candidate_peripheral_pressure`, a country-scoped host trigger that passes when the current candidate has a non-capital core state owned and controlled by the host, and that state is not a host core.

`can_independence_wave_host_release_current_candidate_safely` now accepts this peripheral pressure gate alongside the existing invoker, war, stability, war-support, and surrender-pressure gates.

## Before

In an ordinary peacetime campaign, a colonial or peripheral holder could fail the release host gate unless it was the event invoker. That meant the event could build a candidate pool and still resolve zero releases.

## After

Colonial and peripheral release candidates can resolve from stable hosts when the state relationship is valid, while core-region releases still require the existing invoker or weakness pressure path.

## Safety Boundaries

- The host must still exist.
- The host must still control more states than the configured survival floor.
- The host must not be an Event 006 release itself.
- The release state must still be candidate-cored, host-owned, host-controlled, and non-capital.
- The candidate still cannot take a state marked as the host-survival reserve.
- The niche generic lane remains ordinary/generic and is not promoted into bespoke package or formable content.
- No Event 005 state, flags, focuses, or package logic were added.

## Validation

- Brace balance passed for:
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `events/006_independence_wave.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
- No trailing whitespace in `common/scripted_triggers/006_independence_wave_triggers.txt`.
- Repo precedent search found existing state triggers using `is_controlled_by = ROOT`.
- Search confirmed Event 6 gameplay files do not reference Event 5/Soviet Collapse origin gates.
- Search confirmed `ASN`, `KBN`, `PLM`, and `AYM` are only listed in the niche-generic restore path rather than package/formable assignment.

## Remaining Risks

- This is a resolver-gate fix, not a full batch-scoring rewrite. Combined multi-candidate host-state accounting still needs a final completion audit against the source spec.
- The local `tmp/hoi4-error-logs` folder did not contain the referenced `error.log` during this pass, so no log-line-specific errors were validated here.
