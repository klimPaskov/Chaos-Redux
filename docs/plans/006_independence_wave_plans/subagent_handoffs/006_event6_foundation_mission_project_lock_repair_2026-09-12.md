# Event 006 founding-mission project-lock repair — 2026-09-12

Status: implemented, pending parent validation and live/save-load evidence.

## Scope

The regional founding missions already have package setup activation contracts and are removed by their package cleanup effects. Their ordinary costed decisions use the package active-project helper to prevent a second material commitment while the founding mission is running. Twelve helper omissions meant that an active founding mission was not represented by that lock for the Mediterranean island packages, Karelia/Crimea, Pacific packages, or Transcaucasus.

## Changes

- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`: added the COR, ARX, and ASX founding missions to their existing active-project helpers.
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`: added both KAR and CRI statehood-foundation missions to the shared active-project helper.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`: added the HBX, HAW, FSM, and FIJ founding missions to their package helpers.
- `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt`: added the ARM, GEO, and AZR founding missions to their package helpers.

The Iceland harbour mission remains intentionally excluded because its source contract identifies it as a persistent survival deadline rather than a serialized project. Overlay watch missions remain outside these package helpers because they are separately activated guard objectives with their own running/completed flags and no shared costed-project gate.

## Evidence and limits

The mission ids were checked against the corresponding `activation` blocks in the Event 006 decision files and the package cleanup `remove_mission` calls. The patch changes no activation, setup, cost, category visibility, pre-event pressure, or country-admission logic. Focused source validators and the read-only Event MCP inspect/render route were rerun after the patch; live engine and save/load proof remain outside this handoff.

Focused allocator, country API, flags, FORM-16, Statehood Ledger GUI matrix, and SCN-008 scenario matrix audits all passed after the patch. Direct assertions found all twelve intended mission locks and confirmed the Iceland persistent deadline remains excluded. `git diff --check` reported no whitespace errors on the four trigger files.

The refreshed Event MCP route returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, and overview layout hash `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac8318d3c5fe9b8f241f0cbaaba891b8b6756e0bb550e9fb54db41409d6c53f0/ff43b98228d0ea99fe1b6080e3cebc840f478503f6f0f93a91113465f913bc69/event-lint-4bccb6ec7fe1.json`; the overview manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/815f9a73b0135574e9f14bd3c3a3dd573f4cb2902b3bd635a5dd0865c6c3f589/14fb4cef058adb85dfd8409075e0aa2280323f8d40f562437c216db4aa197808/event-overview-4bccb6ec7fe1-manifest.json`. The MCP analysis remains partial/deferred for workspace-wide lifecycle projections, so it is not live engine proof.
