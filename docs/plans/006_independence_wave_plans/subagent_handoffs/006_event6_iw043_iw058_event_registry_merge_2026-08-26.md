# Event 006 IW-043/IW-058 event-registry merge handoff

## Scope

This source-layout tranche merges the standalone IW-043/IW-058 incident-event parser into the existing Event 006 support-event registry. It reduces parser-file count without changing event identifiers, triggers, options, AI weighting, scripted-effect calls, localisation, package admission, or runtime behavior.

## Changed paths

- Receiver: `events/006_independence_wave_support_events.txt`
- Removed parser: `events/006_independence_wave_iw043_iw058.txt`
- Source-of-truth updates: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Preserved contract

- The moved file declared no `add_namespace` block and no file-scoped constants, so the receiver's existing namespace declaration remains unchanged.
- All 26 absolute event IDs remain present exactly once: `chaosx.nr006.4301` through `.4314` and `chaosx.nr006.5801` through `.5812`.
- The moved event bodies from the first `country_event` through the final closing brace compare exactly after line-ending normalization.
- The receiver has one source marker for the moved block; only the redundant standalone banner was omitted.
- No package, decision, focus, localisation, asset, cost, queue, pressure, pre-event, adapter, or admission surface was added or removed.

## Size and file-count result

The removed parser was 66,579 UTF-8 bytes. Its 65,903-byte executable body is retained in the receiver, and the condensed source marker/header yields a net source saving of 520 UTF-8 bytes and one fewer parser file.

## Validation

- Exact source comparison: `body_exact=True`, 26 original IDs, 26 moved IDs, one source marker, and all receiver event IDs unique.
- `python -B .tools/audit_event6_allocator.py`: passed with 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, 20 static witnesses, and the `3/4/5/7/10` ladder.
- `python -B .tools/audit_event6_country_api.py`: passed with zero missing or duplicate country API entries.
- `python -B .tools/audit_event6_flags.py --strict`: passed with 102 complete flag families.
- `python -B .tools/audit_event6_form16.py`: passed.
- `python -B .tools/audit_event6_gui_matrix.py`: passed.
- `python -B .tools/audit_event6_scenario_matrix.py`: passed.
- Read-only `hoi4.event_inspect` on `events/006_independence_wave_support_events.txt` returned `EVENT_INSPECTED_PARTIAL`, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, with zero blocking diagnostics. The tool deferred workspace-wide helper/lifecycle projections, so this is parser/graph evidence only.
- Read-only `hoi4.event_render` overview returned `EVENT_RENDERED_PARTIAL` for the same revision and graph hash `4b0d98848c436e8f6c8363056e3ae62cfad7785e4b2f1396ac9f1439f91de8df`, with four linked overview artifacts and zero blocking diagnostics. It is not a live in-game claim.

## Remaining boundary

The whole Event 006 implementation remains **HOLD / PARTIAL**. Country shells, package-local gameplay, on-action callback ownership, active Kosovo edits, localisation ownership, and other larger surfaces remain separate where concatenation could change parser composition or interfere with current work.
