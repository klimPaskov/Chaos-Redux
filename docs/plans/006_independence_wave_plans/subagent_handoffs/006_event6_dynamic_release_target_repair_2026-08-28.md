# Event 006 dynamic release-target repair — 2026-08-28

## Disposition

Bounded execution repair for the parent Event 006 tranche. It fixes the target form used when an admitted frozen candidate has no country object yet, and applies the identical correction to the shared Event 005+006 joint release path. It does not widen admission, alter reservation order, restore any pre-event crisis surface, or claim live execution.

## Evidence and source review

The offline Paradox wiki Data structures and Scopes pages were reviewed together with vanilla `documentation/effects_documentation.md`. The vanilla `release` effect accepts a scope-stack target such as `THIS`, `ROOT`, `PREV`, `FROM`, `OWNER`, `CONTROLLER`, `OCCUPIED`, or `CAPITAL`; it does not accept an `event_target:` token as the release argument. Vanilla `common/on_actions/13_goe_on_actions.txt` uses `every_possible_country` followed by `event_target:UK_INDIA = { release = PREV }`, establishing the candidate-scope/host-scope pattern used here.

## Changed files

- `common/scripted_effects/006_independence_wave_execution_effects.txt`: `independence_wave_release_one_frozen_country` now enters `event_target:independence_wave_execution_country`, then the former-host scope, calls `release = PREV`, and uses the candidate `PREV` scope for the autonomy cleanup check and effect.
- `common/scripted_effects/005_006_liberations_collision_effects.txt`: `soviet_collapse_joint_release_one_frozen_country` now follows the same supported candidate/host scope-stack release pattern.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`: record the supported release-target contract, removed invalid dynamic form, evidence boundary, and remaining MCP limitation.

## Validation

The focused release-target assertion confirms both functions contain nested candidate and former-host scopes, `release = PREV`, candidate-scoped autonomy cleanup, and no `release = event_target:` call. The strict allocator, country API, flag-family, FORM-16, and SCN-008 matrix audits pass with 32 content-attested packages, 29 compatible reservation groups, 40 adapters, 161 unattested rows, and the 3/4/5/7/10 ladder including World Collapse 10. Fresh `hoi4.event_inspect` and `hoi4.event_render` retries for `chaosx.nr6.1` still stop before source scanning with `ARTIFACT_MANIFEST_INTEGRITY_FAILED`, zero artifacts, and no diagnostics because the artifact provenance manifest does not match its immutable address.

## Remaining risks and ownership

No Hearts of Iron IV process, save/load cycle, or live country-instantiation result was run by the agent. The parent owner must repair the MCP artifact manifest, rerun Event 006 inspect/render, and perform the live standalone and joint release checks. Whole-event status remains HOLD / PARTIAL; no simplifications were introduced by this tranche.
