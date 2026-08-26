# Event 006 event-registry merge handoff

## Scope

This source-layout tranche merges the small same-namespace Rhineland/Bavaria incident-event parser into the existing Event 006 support-event registry. It reduces parser-file count without changing event identifiers, triggers, options, AI weighting, scripted-effect calls, localisation, package admission, or runtime behavior.

## Changed paths

- Receiver: `events/006_independence_wave_support_events.txt`
- Removed parser: `events/006_independence_wave_rhineland_bavaria.txt`
- Source-of-truth updates: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Preserved contract

- `add_namespace = chaosx.nr6` remains defined once by the receiver.
- Event IDs `chaosx.nr6.11` through `chaosx.nr6.17` remain present exactly once.
- The seven event bodies from the removed parser are content-equivalent from their first `country_event` block through the final closing brace.
- The receiver has one source marker for the moved block, with a condensed comment header only.
- No package, decision, focus, localisation, asset, cost, queue, pressure, pre-event, or admission surface was added or removed.

## Size and file-count result

The removed parser was 22,328 UTF-8 source bytes. The receiver grew by 21,864 bytes after the redundant namespace and banner were removed, for a net source saving of 464 bytes and one fewer parser file.

## Validation

- Exact source comparison: `rhi_body_exact=True`, seven original IDs, seven moved IDs, one source marker.
- `python -B .tools/audit_event6_allocator.py`: passed. The 149-publisher, 40-adapter, 32-attestation, 29-group, 20-package witness, and `3/4/5/7/10` ladder checks remain unchanged.
- `python -B .tools/audit_event6_country_api.py`: passed.
- `python -B .tools/audit_event6_flags.py --strict`: passed with 102 complete flag families.
- `python -B .tools/audit_event6_form16.py`: passed.
- `python -B .tools/audit_event6_gui_matrix.py`: passed.
- `python -B .tools/audit_event6_scenario_matrix.py`: passed.
- Read-only `hoi4.event_inspect` on `events/006_independence_wave_support_events.txt` returned `EVENT_INSPECTED_PARTIAL`, revision `fab35382fdcc93071f18456479aebb85f79ae06342389d47d2d976f8f2c2a898`, with zero blocking diagnostics. The tool deferred workspace-wide helper projections, so this is parser/graph evidence only.
- Read-only `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` for the same revision and graph hash, with four linked overview artifacts and zero blocking diagnostics. It is not a live in-game claim.

## Remaining boundary

The whole Event 006 implementation remains **HOLD / PARTIAL**. Country shells, package-local gameplay, on-action callback ownership, active Kosovo edits, localisation ownership, and other larger surfaces remain separate where concatenation could change parser composition or interfere with current work.
