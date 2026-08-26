# Event 006 IW-007 AGX setup-receipt cancellation guard

Date: 2026-08-26

Status: source-applied, bounded lifecycle repair; whole Event 006 remains HOLD / PARTIAL.

## Finding

The admitted IW-007 Frisia package mission `independence_wave_agx_hold_the_waterline` activated only with `independence_wave_iw_007_setup_complete`, but its `cancel_trigger` did not cancel when that setup receipt disappeared. The package setup effect clears the receipt before rebuilding a generation and restores it only after preparation succeeds. Without the matching cancellation guard, an aborted or independently retried setup could leave the mission active outside its setup contract.

The narrow repair adds `NOT = { has_country_flag = independence_wave_iw_007_setup_complete }` to that mission's existing cancellation OR block. Package identity, waterline success, capital control, timeout behavior, failure effects, admission, and cleanup dispatch are unchanged.

## Changed file

- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
  - `independence_wave_agx_hold_the_waterline.cancel_trigger`

The cancellation effect remains idempotent for the package scope: setup loss takes the existing package failure branch once, and the mission is removed by the engine cancellation path. No terminal crisis flag was added to the trigger.

## Evidence and validation

- Offline mission rules in `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` distinguish activation checks from explicit cancellation checks, supporting the paired setup guard.
- The package audit confirmed the setup writer/clear lifecycle in `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` and found no other AGX defect in this bounded pass.
- Targeted source check: the AGX mission contains both its activation setup receipt and the matching cancellation guard, with one cancellation block.
- `python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 40 adapters, 32 attestations, 29 reservation groups, and the 3/4/5/7/10 ladder with World Collapse 10.
- `python -B .tools/audit_event6_country_api.py` passed: 242 broad rows, 191 unique carriers, zero missing, zero duplicates, IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered tags and 102 complete flag families.
- `python -B .tools/audit_event6_form16.py` passed.
- `python -B .tools/audit_event6_gui_matrix.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed for all 32 cells and eight edge cases.
- Post-change `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b18cee17f1014bf47ec11c0948acc2e8a53be824af5fe59f5e052c35f45960db/71d0944ea603b4e6da3fb1caf6f7bc7b18bef7db007ddb29e580cd2c3066e0e7/event-lint-744cd12bca3e.json`. The MCP result remained partial because large workspace helper/lifecycle projections were deferred; no live game claim is made.

## Remaining boundary

No central admission, allocator, Join, scenario, identity, map, force, portrait, flag, AI, or cost surface changed. Live setup, mission cancellation, save/load, and terminal-receipt evidence remain user-owned validation work.
