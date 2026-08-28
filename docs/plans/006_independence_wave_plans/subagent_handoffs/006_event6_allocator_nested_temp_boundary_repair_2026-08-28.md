# Event 006 nested allocator temporary-scope repair — 2026-08-28

## Disposition

Bounded gameplay repair for the parent commit. The repair addresses a second HOI4 temporary-variable lifetime boundary exposed after the durable live candidate registry fix. It does not widen the 32 content-attested package boundary, alter package admission, reintroduce a pre-event crisis surface, or claim live execution.

## Evidence and source review

The offline Paradox wiki Data structures page states that a temporary variable must exist in the caller block before a nested scripted effect writes it if the caller needs the value after the nested call. Vanilla `common/scripted_effects/013_natural_disasters_effects.txt` provides the matching predeclaration pattern for nested scoring effects. Event 006's allocator had region totals, per-package weights, and candidate metadata created inside nested package/region preparation effects and then read by the outer selector. Wave tuning and force-probe outputs had the same nested-output shape at their planner, execution, joint, and decode call sites.

## Changed files

- `common/scripted_effects/006_independence_wave_effects.txt`: declares the candidate metadata, 14 regional totals, 144 per-package weights, and aggregate automatic weight in `independence_wave_select_one_automatic_package` before nested preparation and region selection.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`: seeds wave-tuning outputs before `independence_wave_capture_wave_tuning` and force-probe outputs before `independence_wave_probe_force_package_mapping`.
- `common/scripted_effects/006_independence_wave_execution_effects.txt`: seeds force-probe outputs in execution metadata validation and wave-tuning outputs in standalone execution.
- `common/scripted_effects/005_006_liberations_collision_effects.txt`: seeds wave-tuning outputs before the joint Event 005/006 plan begins.
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`: seeds decode outputs in the probe and the complete probe contract in the mutating loader.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`: record the repair, evidence boundary, and remaining MCP limitation.

## Validation

The strict allocator, country API, flag-family, FORM-16, and SCN-008 matrix audits pass with 32 content-attested packages, 29 compatible reservation groups, 40 adapters, 161 unattested selectable rows, and the 3/4/5/7/10 automatic ladder including World Collapse 10. Targeted brace/quote and diff checks pass. Fresh `hoi4.event_inspect` and `hoi4.event_render` retries for `chaosx.nr6.1` remain blocked before source scanning by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero artifacts because the provenance manifest does not match its immutable address.

## Remaining risks and ownership

No Hearts of Iron IV process, save/load cycle, or live country-instantiation result was run by the agent. The parent owner must re-run the Event 006 MCP inspect/render route after the artifact manifest is repaired and perform the live standalone and joint release checks. Whole-event status remains HOLD / PARTIAL; no simplifications were introduced by this tranche.
