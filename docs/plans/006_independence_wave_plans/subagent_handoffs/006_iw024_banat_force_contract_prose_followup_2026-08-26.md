# IW-024 Banat force-contract prose follow-up - 2026-08-26

## Scope

This bounded follow-up covers the accepted Event 006 IW-024 Banat (`AXX`) force-profile wording and verification of the country-leader role contract.

The requested `despotism` and `liberalism` roles were already present in `AXX_independence_wave_banat_presidium` at the inspected HEAD from commit `cb9a2f341` (`Repair IW-024 Banat leader role contract`).

No character-file edit was made because adding duplicate roles would weaken the contract.

## Changed files and identifiers

- `docs/events/006_independence_wave/banat_package.md` now identifies profile `p24` / `industrial_security`, reinforcement mask `1095`, and the five accepted pathways: integrate militias, recruit regional guards, secure depots, mobilize factory or railway guards, and complete capital and border defense missions.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` now gives the AXX strategy comment the same `p24` / `industrial_security` / mask `1095` contract and pathway summary without changing any strategy factor or weight.
- `common/characters/006_independence_wave_characters_registry.txt` was verified unchanged and contains exactly one role each for `conservatism`, `marxism`, `centrism`, `despotism`, and `liberalism` on `AXX_independence_wave_banat_presidium`.
- All five AXX roles use `desc = AXX_independence_wave_banat_presidium_desc` and `traits = { }`.

The source contract remains the AXX blocks in `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt` and `common/scripted_effects/006_independence_wave_balkan_package_effects.txt`, plus `p24 = 1095` in `common/script_constants/006_independence_wave_constants_registry.txt`.

## Before and after behavior

The role behavior was already complete before this follow-up, so no promotion, admission, route, cost, balance, or runtime behavior changed.

The durable Banat package note and matching AXX AI comment previously named `industrial-security` without the accepted mask and complete pathway contract.

They now state the installed `p24` `industrial_security` profile with mask `1095` and the five source-aligned reinforcement pathways.

## Validation

The focused source assertions passed for all five AXX roles, shared descriptions, empty traits, source profile tokens, mask `1095`, five pathway helpers, and the updated Banat and AXX prose.

The six Event 006 static validators passed with exit code `0`:

- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_event6_country_api.py`
- `python -B .tools/audit_event6_flags.py --strict`
- `python -B .tools/audit_event6_form16.py`
- `python -B .tools/audit_event6_gui_matrix.py`
- `python -B .tools/audit_event6_scenario_matrix.py`

The allocator validator reported 149 publishers, 126 automatic or high-chaos selectable packages, 40 runtime adapters, and 32 attested packages.

The current read-only Event Chain Viewer inspection for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with status `ok`, zero blocking diagnostics, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac020927faacef83f2b3a07914f4ccd7ced9bbcdc7500dec62da0a5ad8128d4e/96af1a525d82ef57e20b6183a58dc64c25d0c3b14f06bdb60ed3afb0bc145c97/event-lint-744cd12bca3e.json`.

The matching read-only overview render returned `EVENT_RENDERED_PARTIAL` with status `ok`, zero blocking diagnostics, the same revision, and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a5d95a9ec5a63b1d821f92857da718f4bdbef0277756dbe6013827d987a6550/7ca72fb60b6eb09fe9833e0a8c97e7c25e37194800314fb4359699514f242288/event-overview-744cd12bca3e-manifest.json`.

No probability inspection or comparison was run because the AI edit is comment-only and leaves all AXX strategy factors and weights unchanged.

## Skipped checks and remaining risk

No HOI4 launch, save-load, or live playtest was run, as required by the task boundary.

No map, focus, GUI, technology, or balance surface was edited.

The installed HOI4 MCP tool list exposes no country or character inspection/render route, so the AXX role evidence is source and static-validator evidence rather than engine-level country inspection.

The Event Chain Viewer marked both reports partial because large-workspace helper projections and lifecycle passes were deferred, although both reports returned zero blocking diagnostics.

No files were staged or committed by this follow-up.
