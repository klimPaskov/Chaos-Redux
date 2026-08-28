# Event 006 IW-095 trade-project reward and ledger repair

Date: 2026-08-28

## Scope

This bounded repair corrects the IW-095 West African trade-mission focus callback. The callback previously applied the shared Network cooperation reward and Dahomey compact-ledger gains in its wrapper and then applied the same transaction again through the package-owned network-project helper.

## Changed file

- `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt`

## Repair

`independence_wave_iw095_focus_open_west_african_trade_mission` now retains its ambition reward, invokes `independence_wave_dahomey_reward_network_project` once, and sets the completion flag. The wrapper no longer applies Network cooperation, council/revenue deltas, or `independence_wave_change_dahomey_compact_values`; `independence_wave_dahomey_reward_network_project` remains the single atomic owner of those effects and the `dah_west_african_trade_mission` idea.

This restores the intended single Network corridor transaction and prevents the callback from over-granting the council and revenue ledgers. It does not change package identity, rights, central admission, allocator counts, pre-event visibility, or any other package.

## Validation

- The focused source check finds zero direct Network cooperation calls in the wrapper and one call in the package helper.
- `python .tools/audit_event6_allocator.py --strict` passed with the existing 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and `3/4/5/7/10` automatic ladder.
- `python .tools/audit_event6_country_api.py` passed with no missing or duplicate carriers.
- `python .tools/audit_event6_flags.py --strict` passed with 102 complete flag families.
- `python .tools/audit_event6_form16.py` passed.
- `python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- Mandatory current Event 006 MCP inspection remains blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no artifacts, so no engine or live-game claim is made.

## Boundary and remaining blockers

IW-095 remains package-local and fail-closed. The DAH country shell, attested identity and rights receipt, neutral flag/emblem, approved portrait roster, central adapter/publisher/preflight/Join receipts, typed probability evidence, repaired MCP artifact manifest, and SCN-008 admission remain unresolved. No fallback asset or pre-event surface was introduced.

