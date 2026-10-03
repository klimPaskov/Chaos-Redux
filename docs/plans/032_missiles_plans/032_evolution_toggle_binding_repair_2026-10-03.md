# Event 032 evolution toggle binding repair

Disposition: implemented in source, with the same-scenario MCP comparison unresolved.
Acceptance basis: the user's full Event 32 contract requires separate evolution enable gates and safe disabled behavior for all five tracks.
The parent reviewed the context-free read-only baseline in `subagent_handoffs/032_evolution_gate_probability_baseline_2026-10-03.md` before applying the binding and consumer changes.
The baseline confirms source-binding defects and retains exact MCP timeouts, rather than claiming numeric probabilities.
The post-patch comparison uses that saved fixture and the byte-exact before sources.

## Source finding

`events_log_toggle_current_evolution_disabled` in `common/scripted_effects/chaosx_events_log_effects.txt` writes `events_log_disabled_evolution_[EVOLUTION_EVENT_ID]_[EVOLUTION_TYPE]_[EVOLUTION_STAGE]`.
Event 32's `missiles_record_evolution_unlock` records event `32`, types `1` through `5`, and stage `1`.
The before sources read `event_evolution_disabled_32_1` through `event_evolution_disabled_32_5`, which are not the flags written by the shared toggle.
The owner replaced 45 literals on 42 source rows with the canonical bindings and added retained-adoption consumer checks.

## Exact binding correction

| Track | Current read | Shared toggle read |
| --- | --- | --- |
| Saturation Arsenals | `event_evolution_disabled_32_1` | `events_log_disabled_evolution_32_1_1` |
| Unreliable Guidance | `event_evolution_disabled_32_2` | `events_log_disabled_evolution_32_2_1` |
| Special Warheads | `event_evolution_disabled_32_3` | `events_log_disabled_evolution_32_3_1` |
| Rogue Launch Commands | `event_evolution_disabled_32_4` | `events_log_disabled_evolution_32_4_1` |
| Automatic Retaliation | `event_evolution_disabled_32_5` | `events_log_disabled_evolution_32_5_1` |

All numeric weights, tuning constants, resource costs, site custody, existing unlock receipts, and Event Logs ownership are preserved.
Read-only enabled/active helpers gate decisions, AI profile selection, payload integration, guidance behavior, rogue activity, and warning creation.
The shared operation-track gate is checked at preflight, preparation completion, and commitment, while commitment also rechecks payload custody.
Rogue operation origin persists in the frozen receipt after its temporary bypass flag clears, and cleanup clears that origin.
Disabled rogue timeouts close existing incidents without launching or transferring reserve and retain compromised-site state.
Queued retaliation responses settle their warning receipt without launching when the track is disabled.
Physical reserve caps and civil-war inheritance keep their persistent adoption/custody records, without granting saturation behavior while disabled.
No disable or re-enable changes inventory, and no world scan was added.

## Evidence and validation gate

Immutable before sources are stored in `docs/plans/032_missiles_plans/baselines/2026-10-03_evolution_gates/`.
The source set includes the original five audit files plus byte-exact operations triggers, decisions, missions, the event file, and core effects captured before their consumer changes.
Use `EVO-10`, `EVO-11`, and `EVO-12` from the accepted matrix, including the actual canonical shared flags, for the baseline and after comparison.
The read-only auditor must preserve the scenario fixture and compare each exact before source with its current owning path.
Any unresolved flag, scope, eligibility, or candidate-pool binding remains an evidence gap.
Source matching and unchanged weight tokens cannot substitute for that comparison.

The focused source regression `.tools/test_event32_evolution_gates.py` passes six tests, including five retained-adoption toggles, payload-custody suspension, ordinary conventional play with all tracks disabled, saturation creation, and queued rogue-operation identity.
The existing source-path and package regressions pass eleven tests.
These are source-model tests and do not prove runtime or normalized decision probabilities.

Separate accepted operation-preparation and MTTH-pacing gaps identified by the audit remain outside this binding repair and are tracked in the test ledger.
