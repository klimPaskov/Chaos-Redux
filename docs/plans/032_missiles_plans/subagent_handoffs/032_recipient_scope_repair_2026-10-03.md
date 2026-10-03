# Event 032 recipient scope repair

Disposition: implemented in source, with full MCP lifecycle and scenario validation still pending.
Acceptance basis: the user requires every frozen valid country to process once, receive valid owned launch infrastructure, preserve Event 16's reaction helper, and pass SCN-015 preflight before mutation.

## Findings and changes

The global firing and SCN-015 commit loops entered recipient countries without rebinding `ROOT`.
Site helpers use `ROOT` for ownership, controller checks, registry writes, and programme ledgers, so recipients other than the initiating country could fail site selection or mutate the initiator's records.

Immediate hidden receivers `chaosx.nr32.5` and `chaosx.nr32.6` bind recipient `ROOT` before programme and scenario helpers run.
The ordinary receiver checks frozen membership and the firing receipt around the entire recipient transaction, including adoption, rogue evaluation, and pressure accounting.
The scenario receiver checks frozen membership and its setup receipt before applying the package synchronously.
Neither receiver owns pacing, history, news, or a player popup.

SCN-015's owned-state preflight now checks recipient control through `PREV`.
It shares `missiles_state_has_valid_site_geography` with ordinary site selection, whose physical requirements use the actual controller instead of the initiating ROOT.

The first-package Event 16 call delegates host and personal receipt checks to `brilliant_scientist_record_missile_crisis`.
The prior Event 032 global bridge flag was consumed by the first non-host recipient and could suppress an AI host's later reaction.
No Event 16 helper or owner state was changed.

Site registration now reads `PREV.missiles_site_capacity` when adding its state capacity to the country total.
The former unqualified value was read in country scope after entering ROOT and could leave the initial total at zero.
The existing network recalculation already uses this state-relative read.

The first package always invokes the normalized next-step adapter, including recipients that entered with rocket research already completed.
The exhausted-line branch accepts the mature programme without granting another technology or publishing an unresolved-mapping result.
Supported technology grants use `popup = no` and rely on the single country report.
The installed technology definitions and set-technology documentation were read directly, while the requested technology inspector returned a 600-second client timeout.

Event 32 was removed from `event_log_event_is_reworked_default_enabled` until the accepted completion gates are proved, as required by the source coding prompt and acceptance criteria.
Persistent player toggle choices are not reset by this default registration change.

## Files and identifiers

- `events/032_missile_crisis.txt`: `.5` and `.6` immediate hidden receivers.
- `common/scripted_effects/032_missiles_effects.txt`: frozen dispatch, `missiles_process_frozen_recipient`, and Event 16 bridge call.
- `common/scripted_effects/032_missiles_scenario_effects.txt`: immediate `.6` package dispatch.
- `common/scripted_triggers/032_missiles_triggers.txt`: `missiles_state_has_valid_site_geography` and site ownership wrapper.
- `common/scripted_triggers/032_missiles_scenario_triggers.txt`: recipient-relative site preflight.
- `common/scripted_triggers/chaosx_settings_triggers.txt`: default-enable completion gate.
- `.tools/test_event32_recipient_scope.py`: offline ROOT-boundary regression.
- `docs/specs/032_missiles_specs/032_missiles_test_matrix.md`: `BASE-05` recipient and host-order test.
- `docs/events/032_missiles.md` and `docs/events/032_missiles/systems/triggerable_scenario.md`: current dispatch and receipt documentation.
- `docs/events/032_missiles/asset_audit.md`: corrected checksums for Keys Returned not-eligible and Sky Full of Steel completed.

## Reference evidence

The connected `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` routes returned both installed and offline wiki sources under workspace `mod_chaos_redux_ea3b2d67c2c0`.
No required source kind was excluded through `omittedSources`, and `missing` was empty.

- Installed `documentation/effects_documentation.md`, lines 2943–2967, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: country-event delivery and optional delay fields.
- Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 23–36, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`: the receiving country is ROOT and regular event targets carry into child events.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 260–263, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`: ROOT remains inherent to the block, while PREV follows the containing scope.
- Vanilla `common/scripted_effects/WTT_china_political_struggle_effects.txt`, helper `WTT_fire_add_support_status_events`, lines 382–423: immediate country-event delivery from a scoped recipient.
- Current shared `common/scripted_effects/016_brilliant_scientist_context_effects.txt`, lines 424–452: host-specific and character-specific idempotent reaction receipts.

## Preserved source identities

The immutable pre-repair copies live under `docs/plans/032_missiles_plans/baselines/2026-10-03_recipient_root/`.

| Baseline file | SHA-256 |
| --- | --- |
| `032_missile_crisis.txt` | `fee0b45854c7ed3a55c826eba4bbfb9e8af254b9d716e2f5213ef7f030781041` |
| `032_missiles_effects.txt` | `457e2e8fb8aed64bafc585fa74b0b324ae8db226d89edd6b0615fbed85f51111` |
| `032_missiles_scenario_effects.txt` | `2551ab4ca642fe35d47ddf8d31c889d42e92f9d975ed9cb80894a49e1c41db4a` |
| `032_missiles_scenario_triggers.txt` | `6a6be0fb2760371108f4696995586be8c0c27ad2d8ea1f37c122ffbad449f87e` |
| `032_missiles_triggers.txt` | `0e154b8c5d3d39252fcc936fab000210159a93f5587eb040c663f7b9fa1f13ad` |

## Validation and limits

The offline regression passes ten tests on the current source.
The preserved baseline fails the recipient ROOT paths for Germany, Canada, and Luxembourg when England initiates, fails recipient-relative scenario preflight and receiver presence, and retains the suppressing Event 16 global gate.
Event-option weight blocks remain identical to the preserved baseline.
This regression models documented scope delivery only and does not prove runtime resource, casualty, raid, or probability outcomes.

All 82 asset-table paths exist and their recorded checksums match the current DDS bytes after the two metadata corrections.
No image pixels or sprite registrations changed in this repair.

The fresh focused Event trace returned `EVENT_INSPECTED_PARTIAL`, revision `9632ca4524ded062f0beebccbb91f0593efa38cb58d00af4b079afca066fc2ad`, with zero indexed helpers and 8,945 unresolved nodes.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a8f37a7f6dc77f0ff807f9e899e6e0cb53aa6f696737857b85779517fbbb6cc/153aa40c3c1465d1f56ef85e0affb7ae3c1daedfd563422cc5a4be27aa6b7d2c/event-trace-9632ca4524de.json`.
Its focused boundary does not prove helper lifecycle coverage.
The full impact request for `missiles_process_frozen_recipient` returned a client error, `timed out awaiting tools/call after 600s`, without a domain result or job ID.
The ordinary `hoi4.source_lookup` request for the exact vanilla helper also returned that 600-second client timeout.
The vanilla precedent was read directly from the installed source and its SHA-256 is `6391dda75ca20c7858fd368715100ebdbe750a8056e232cfe03e4ac3d865b57a`.
These observation timeouts do not establish that the server-side work stopped.

The first native-raid auditor failed with `workspace routing discovery timed out`.
The first probability auditor disappeared from the runner with `not_found` before returning its baseline audit.
The initial reference and Event calls lost their continuation handles, and retries with the explicit confirmed workspace ID restored the ordinary MCP routes.
A replacement read-only probability auditor was dispatched with no inherited context and the exact immutable before sources for same-scenario comparison.
No weight or tuning value was changed, and numeric probability claims remain pending.

The event is incomplete while the remaining accepted native parity, probability matrix, lifecycle comparison, asset-consumer, and independent closure gates remain unresolved.
