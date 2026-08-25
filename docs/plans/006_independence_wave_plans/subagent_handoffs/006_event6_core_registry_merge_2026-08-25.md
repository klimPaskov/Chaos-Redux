# Event 006 core registry consolidation handoff

## Disposition

This source-layout pass is complete and behavior-neutral. It removes seven small Event 006 parser files while preserving every moved identifier, namespace, and executable body.

The whole Event 006 implementation remains HOLD / PARTIAL at 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. No package was promoted and no admission or reservation gate changed.

## Receivers

- `events/006_independence_wave.txt` now contains the SCN-008 launch barrier and frozen summary events formerly in `events/006_independence_wave_scenario.txt`.
- `common/decisions/006_independence_wave_decisions.txt` now contains the SCN-008 zero-reward ledger controls formerly in `common/decisions/006_independence_wave_scenario_decisions.txt`.
- `common/scripted_triggers/006_independence_wave_triggers.txt` now contains the Join predicates formerly in `common/scripted_triggers/006_independence_wave_join_triggers.txt` and the SCN-008 selector/barrier predicates formerly in `common/scripted_triggers/006_independence_wave_scenario_triggers.txt`.
- `common/scripted_effects/006_independence_wave_effects.txt` now contains the roster checkpoint, automatic allocator, and package-dispatch effects formerly in the three corresponding small effect files.

The large scenario allocation-effects file remains separate because it is a distinct, large scenario-owned surface. The package-dispatch trigger registry also remains separate because its admission and preflight predicates are already maintained as a dedicated central trigger surface.

## Preservation evidence

Each deleted file's normalized source body remains present verbatim in its receiver after the one-line `SOURCE` marker. The normalized body checks passed for all seven moved files.

The active audit tools now read the receivers: `.tools/audit_event6_allocator.py` reads the merged package-dispatch effects, and `.tools/audit_event6_scenario_matrix.py` reads the merged SCN-008 event, decision, and trigger registries.

The source-layout change removes seven parser files and adds approximately 710 bytes of provenance markers and spacing after normalization; it does not add gameplay content or duplicate executable definitions.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 adapters, 32 attestations, 29 reservation groups, and the exact 3/4/5/7/10 plus World Collapse 10 ladder.
- `python -B .tools/audit_event6_country_api.py` passed with 242 broad tags, 191 resolved carriers, zero missing carriers, zero duplicates, and the IW-031 crosswalk pass.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `python -B .tools/audit_event6_flags.py --strict` passed all 102 flag families.
- `python -B .tools/audit_event6_form16.py` passed the ARM/GEO/AZR FORM-16 contract.
- `python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic matrix.
- The read-only `hoi4.event_inspect` lint refresh returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; the workspace-wide helper/lifecycle projection remains deferred by the MCP adapter.

No live gameplay, save/load, or parser-runtime claim is made by this handoff.
