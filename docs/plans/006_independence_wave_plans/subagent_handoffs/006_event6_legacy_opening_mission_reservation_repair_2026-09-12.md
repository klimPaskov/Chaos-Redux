# Event 006 legacy opening-mission reservation repair

Date: 2026-09-12.

Disposition: **implemented / narrow lifecycle repair; whole event remains HOLD / PARTIAL**.

## Scope

The package-local founding missions for TRA, RHI, BAY, AJX, AFX, AGX, BRI, and CAT already existed and already published their matching crisis-resolution receipts, but their package `has_*_active_package_project` triggers only tested paid decisions. An ordinary project could therefore be considered available while that package's opening mission was still active.

## Source changes

Added the existing founding mission as an active-project member in:

- `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt` (`independence_wave_tra_hold_border_council_together`)
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_saar_package_triggers.txt` (`independence_wave_rhi_keep_rhine_arteries_open`, `independence_wave_bay_hold_the_state_together`, `independence_wave_ajx_hold_saar_compact_together`)
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt` (`independence_wave_afx_prevent_industrial_stoppage`, `independence_wave_agx_hold_the_waterline`)
- `common/scripted_triggers/006_independence_wave_western_package_triggers.txt` (`independence_wave_bri_hold_breton_settlement_together`, `independence_wave_cat_hold_industrial_compact_together`)

The patch changes only reservation predicates. It does not add a decision category, pressure, cost, queue, pre-event mission, admission row, AI weight, asset, or fallback.

## Intentional exclusions

The Iceland harbour mission remains excluded because its source comment and decision contract define it as a persistent survival deadline rather than a serialized paid project. Scotland and Wales have no corresponding package-local founding mission in the inspected decision sources, so no synthetic mission gate was added.

## Validation

Focused Event 006 allocator strict, country API, strict flag families, FORM-16, Statehood Ledger GUI source matrix, and SCN-008 scenario matrix validators all passed after the edit. Direct source assertions confirmed all eight mission reservations and confirmed that the Iceland harbour mission was not added. `git diff --check` reported no whitespace errors on the four touched trigger files.

The required read-only Event MCP refresh for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, and overview layout hash `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a42e66bba1d7ec2aab21c7554c1cdb33c280ad19574efaf394db215a58bb9b2/531223b030697766b20a140a5a6b79e5d4d61c7fee35e53a4281ef8f1a184dee/event-lint-4bccb6ec7fe1.json`; the overview manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/815f9a73b0135574e9f14bd3c3a3dd573f4cb2902b3bd635a5dd0865c6c3f589/14fb4cef058adb85dfd8409075e0aa2280323f8d40f562437c216db4aa197808/event-overview-4bccb6ec7fe1-manifest.json`. The large-workspace helper/lifecycle projection remains deferred and validation is false with one aggregate blocking diagnostic, so this handoff makes no live engine, save/load, or runtime completion claim.

## Remaining limits

This repair closes only the active-project reservation gap. It does not introduce new package-ready wrappers or rewrite every ordinary decision's visibility/availability to require the matching opening receipt; those broader changes remain outside this bounded tranche. Identity, rights, portrait, flag, formable, audio, GUI dynamic-state, probability, and live-runtime gates remain documented in the current Event 006 source-of-truth map.
