# Event 006 opening-mission serialization repair — 2026-09-12

## Disposition

Implemented a bounded package-local lifecycle repair for the existing Event 006 founding missions whose ordinary project triggers were still open before their compact-resolution receipt. The repair applies the same two-part contract already accepted for KUB, RUT, TAT, BSK, and IW-095: ordinary projects require the success receipt, and the active-project helper reserves the founding mission while it is running.

## Changed source

- `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt` — FER.
- `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt` — MEL.
- `common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt` — KUR.
- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` — KOM.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` — NAV and GLC.
- `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt` — ALT, BYA, KHA, and YAK.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt` — UDM.

For each package, `is_independence_wave_*_project_ready` now requires its existing `*_compact_crisis_resolved` receipt, while retaining its existing setup, force-generation, origin, anchor, and failure guards. `has_independence_wave_*_active_package_project` now includes the existing founding mission identifier. No decision, mission, cost, AI weight, admission, central attestation, Join, asset, country identity, or fallback source was changed.

## Source evidence

Every affected mission already exists in the current decision registries with `available = { always = no }`, activation guards that reject the matching resolution/failure receipts, a success path that publishes the matching `*_compact_crisis_resolved` flag, and timeout or invalidation paths that publish the matching failure receipt. Therefore the new readiness gate cannot deadlock mission activation: the mission does not call the project-ready trigger, while paid projects inherit it through their existing visibility and availability blocks.

The affected package rows remain package-local where their parent admission, identity, rights, roster, flag, probability, or engine gates are unresolved. This repair does not promote any package into the central release pool or weaken a fail-closed boundary.

## Validation

- `.tools/audit_event6_allocator.py --strict` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-ranked packages, 40 adapters, 32 attestations, 29 compatible groups, exact 3/4/5/7/10 ladder, and no pre-event category/mission/cost/queue.
- `.tools/audit_event6_country_api.py` passed: 242 broad rows, 191 resolved carriers, zero missing or duplicate tags, IW-031 crosswalk pass.
- `.tools/audit_event6_flags.py --strict` passed: 102 registered tags and 102 complete flag families.
- `.tools/audit_event6_form16.py` passed.
- `.tools/audit_event6_gui_matrix.py` passed.
- `.tools/audit_event6_scenario_matrix.py` passed all 32 cells and eight edge cases.
- A direct source assertion confirmed all eleven affected trigger blocks contain both the matching resolution receipt and founding-mission reservation.
- Read-only `hoi4.event_inspect` and `hoi4.event_render` were rerun for `chaosx.nr6.1`; both returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, with `helpers = 0`, `validation.passed = false`, and the known large-workspace helper/lifecycle deferral plus one aggregate blocking diagnostic. This is structural evidence only and does not prove live execution.

## Remaining limits

No live game, save/load, central admission, portrait/flag rights, typed probability, or package identity claim follows. The Event 006 whole-event status remains **HOLD / PARTIAL**. The unrelated working-tree edits and active Git processes were preserved; no staging or commit was performed.
