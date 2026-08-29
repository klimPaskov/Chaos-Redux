# Event 006 absent-country release scope repair — 2026-08-29

## Status

Completed a narrow source repair for Event 006 standalone execution when a selected registered tag is not instantiated at runtime. This handoff makes no live-game, save/load, or in-engine country-release claim.

## Finding

The frozen plan stores a selected country target before that tag exists. The release executor previously entered the absent target through `event_target:...execution_country` and then called `release = PREV` from the former-host scope. An event-target block cannot provide a valid country object for an absent tag, so the release branch could leave the selected country uninstantiated and the final instantiated-count check failed closed. The same scope shape existed in the shared Event 005 + Event 006 joint release helper.

## Source changes

- Updated `independence_wave_release_one_frozen_country` in `common/scripted_effects/006_independence_wave_execution_effects.txt` to keep the absent target as the current `every_possible_country` scope (`exists = no`, matching the frozen target tag), enter the former host, and call `release = PREV`.
- Updated `soviet_collapse_joint_release_one_frozen_country` in `common/scripted_effects/005_006_liberations_collision_effects.txt` with the same absent-candidate scope shape so the joint Event 005 + Event 006 path cannot retain the invalid direct event-target release.
- Existing dormant-shell handling remains unchanged: registered shells that already exist continue through the state-transfer branch, while living countries remain rejected by plan validation. No admission, attestation, identity, asset, or package gate was weakened.

## Engine precedent

The corrected shape follows the vanilla `common/on_actions/13_goe_on_actions.txt` release pattern, where `every_possible_country` selects an `exists = no` candidate and the former-host event target calls `release = PREV`. The offline Scopes/Data Structures wiki pages and vanilla `effects_documentation.md` confirm that `every_possible_country` may visit absent country tags and that `release` accepts a scope-stack target such as `PREV`.

## Invariants and pre-event boundary

The public `chaosx.nr6.2` report remains gated on a committed non-empty plan. The retired `chaosx.nr6.3` callback still only clears stale compatibility flags. No wave-pressure value, decision category, mission, queue, or other pre-event surface was added or re-enabled.

## Evidence

After the patch, the focused Event 006 allocator, country API, country-flag, FORM-16, and SCN-008 scenario-matrix audits passed in strict mode. Source search confirms that no direct `release = event_target:independence_wave_execution_country` or Soviet joint equivalent remains. The old split Balkan trigger paths named in the pasted `capital_scope` log are absent from the current tree; current Banat, Thrace, and Epirus package checks use fixed anchors instead of dereferencing an empty capital.

## Remaining risk

The user must verify `event chaosx.nr6.1` in a live session to confirm country instantiation and state transfer. Whole Event 006 remains HOLD / PARTIAL for the existing package, asset, weighted-probability, MCP-artifact, and live-runtime evidence gaps. The separate static SCO/WLS history-roster concern remains unpatched because runtime character recruitment is not a supported fallback and it is not proven to be the cause of every package selection failing.
