# IW-040 founding-anchor loss guard

> Historical pre-IW-044 snapshot: its 30/27/163/38 package-boundary wording is superseded by the current 31/28/162/39 IW-044 authority in `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md`.

This handoff is a historical IW-040-only lifecycle patch receipt; its source correction remains applicable to KUB, but its package arithmetic and MCP status do not describe current Event 006 authority.

The admitted IW-040 Kuban founding mission now cancels when exact state 234 is no longer both owned and controlled by the active KUB origin, even if capital relocation leaves the replacement capital controlled.

## Source change

`common/decisions/006_independence_wave_kuban_decisions.txt` adds `234 = { NOT = { is_owned_and_controlled_by = ROOT } }` to `independence_wave_kub_hold_mounted_compact_together.cancel_trigger`.

The existing `cancel_effect` therefore follows its failure branch, sets `independence_wave_kub_compact_crisis_failed`, and calls `independence_wave_kub_apply_project_failure`; no new flag, effect, localisation key, AI weight, dispatcher, attestation, or Join entry was added.

## Contract basis

`docs/events/006_independence_wave/kuban_package.md` requires ownership and control of state 234 throughout the 600-day founding mission, and the package trigger contract identifies state 234 as the exact KUB anchor and capital state.

## Validation and boundaries

The mission block remains balanced and its success branch still requires stable ledgers, a selected government, state-234 ownership/control, and current capital control. This is a source/spec-backed lifecycle correction only; no current HOI4 MCP evidence is claimed because the workspace route is blocked by `ARTIFACT_MANIFEST_INVALID` (Artifact provenance manifest is invalid). Whole Event 006 remained HOLD/PARTIAL at the handoff snapshot; current routing uses the 31/28/162/39 IW-044 authority.
