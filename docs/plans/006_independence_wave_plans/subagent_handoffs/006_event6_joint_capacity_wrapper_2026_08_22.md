# Event 006 joint-capacity wrapper repair — 2026-08-22

## Scope

This handoff records a narrow runtime repair for the Event 005 + Event 006 synchronized liberation allocator. It does not promote any new country package, alter package content attestations, or weaken the fail-closed runtime gates.

## Source changes

`common/scripted_triggers/006_independence_wave_triggers.txt` now contains runtime-ready witnesses and joint-capacity reservation tries for the nine already-admitted package IDs that were present in the central adapter/content-attestation registries but absent from the shared capacity wrapper:

- IW-024 — AXX / state 82 / `rg_danube_borderland`
- IW-027 — BAX / state 184 / `rg_184`
- IW-028 — BBX / state 185 / `rg_185`
- IW-030 — MNT / state 105 / `rg_105`
- IW-031 — KOS / state 802 / `rg_danube_borderland`
- IW-038 — RUT / state 73 / `rg_73`
- IW-040 — KUB / state 234 / `rg_don_kuban`
- IW-044 — TAT / state 249 / `rg_middle_volga_kazan`
- IW-045 — BSK / state 651 / `rg_651`

Each wrapper preserves the existing allocator contract: package-specific exact-tag and runtime preflight checks, chaos-band eligibility, Event 005 country/anchor/host exclusion, duplicate country/anchor/group exclusion, and one-count reservation of package, carrier, anchor, and reservation group. The nine calls are placed in the shared `is_independence_wave_liberations_cluster_member_capacity_available` sequence before the later package families.

## Why this is safe

All nine package IDs already have package-local region triggers/effects and are already represented in the central runtime adapter and content-attestation lists. Their exact carrier/state/group bindings match the package constants and existing standalone planner triggers. This repair only makes their accepted contracts visible to the Event 005 + Event 006 capacity transaction; it does not make unattested packages selectable.

The shared `rg_danube_borderland` reservation group intentionally keeps IW-024, IW-023, and IW-031 mutually exclusive. The allocator continues to require a complete target count and equal-length reservation arrays before committing the plan.

## Validation evidence

- `python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 40 adapters, 32 attestations, 29 compatible groups, static standalone witness 20, and retired pre-event crisis surface.
- `python -B .tools/audit_event6_country_api.py` passed: 242 broad tags, 191 resolved carriers, no missing or duplicate carrier entries.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- A fresh read-only `hoi4_event_inspect` state-flow pass for `chaosx.nr6.1` completed with `status: ok`; the only diagnostic was the expected inline-file truncation notice. The MCP validation field remains false because workspace-wide helper projections/lifecycle validation is deferred by the server.

## Remaining boundary

This source-only repair does not constitute live HOI4 acceptance. The user must still verify an actual synchronized allocation in a loaded game/save. Packages that fail their existing exact/preflight/host/anchor gates remain intentionally unselectable.
