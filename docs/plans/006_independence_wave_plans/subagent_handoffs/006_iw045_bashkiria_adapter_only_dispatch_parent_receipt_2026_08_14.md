# IW-045 Bashkiria adapter-only dispatch receipt — 2026-08-14

## Disposition

IW-045 Bashkiria has a package-local setup, final-validation, cleanup, focus-hook, decision, idea, AI, flag, and portrait-runtime surface, and it is now registered in the central runtime adapter dispatcher. It remains deliberately fail-closed and is not content-attested, released through Join, or admitted to normal or SCN-008 execution.

## Central changes

- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` now calls the Bashkiria setup, final-validation, and cleanup adapters in all three shared phases.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` now includes `iw_045` in the runtime adapter registry and exact dormant-tag preflight branches for normal and SCN-008 paths.
- `iw_045` is absent from `has_independence_wave_runtime_package_content_attestation_for_execution_id`; the shared preflight therefore rejects it before runtime materialization.
- `.tools/audit_event6_allocator.py` accepts the current adapter closure and 26 central dispatcher families while preserving the 31-package content-attestation closure.
- No Event 006 Join order, content-attestation list, scenario admission list, or Soviet-Collapse origin branch was widened.

## Current authority

The allocator audit reports 40 runtime adapters, 31 content-attested packages, 9 adapter-only fail-closed IDs (`IW-013`, `IW-015`, `IW-043`, `IW-045`, `IW-058`, `IW-093`, `IW-098`, `IW-177`, and `IW-179`), and 28 compatible reservation groups. The 162 selectable-but-unattested rows remain outside the executable package closure. Automatic counts remain 3, 4, 5, 7, and 10, with World Collapse at 10.

## Validation evidence

- `python .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 31 attested packages, 28 groups, and the 3/4/5/7/10 ladder.
- `python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases.
- `python .tools/audit_event6_flags.py` passed 102 registered and complete flag families.
- `python .tools/audit_chaosx_country_tags.py` passed with 136 protected tags and no external country-definition or identity-surface collisions.
- Current `hoi4.event_inspect` for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL`, revision `d21fdfa2723e4a624054076fb1104ba638c4fbb1f733358a99b24aac1839ace2`, with zero blocking diagnostics. The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0cba4ce84ec0b206bb8e66d6d0c1dec6cbfeb86468d348038098a5556ee1273/e050f9b03023b41397b6239967e0782165798608bbea928c110f1107ac302d1f/event-state_flow-d21fdfa2723e.json`.
- Current `hoi4.event_render` for the same selector and revision returned `EVENT_RENDERED_PARTIAL`, with zero blocking diagnostics. The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0f7faaaa4c44e4244483f25657f9906a8819239d36602009c5601d8d2a09ad3/c14da708ded51c4314233374f3f74538099b5176a1df4e0d88a8af4af75be529/event-state-d21fdfa2723e-manifest.json`.

The Event MCP result remains partial because the large workspace defers workspace-wide helper and lifecycle projections; it is not a selected IW-045 blocker. Package-specific weighted AI evidence remains adapter-limited and does not support a quantitative balance claim. Central content attestation, Join admission, typed probability scenarios, and final whole-event completion remain parent-level gates.
