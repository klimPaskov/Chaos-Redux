# Dedicated-save sequence

Status: prepared, not executed.
Startup must reach a stable main menu with clean fresh logs before any campaign checkpoint.

1. Start a fresh 1936 non-Ironman United States campaign and save `crqa_normal_1936_baseline` before activating test fixtures.
2. Inspect ordinary startup grants, settings, event eligibility and empty shared logs; preserve this save for natural progression checks.
3. Save a separate `crqa_cxt_initialization` branch, open the game console and invoke the documented `e chaosx_test` command.
4. Verify the player is CXT, the former capital is retained, the expected test roster and facilities exist, and fresh logs remain clean.
5. Save `crqa_cxt_baseline`, invoke the setup again, and compare roster/template counts and fixture state to test idempotence.
6. Reload the CXT baseline for each independent shared-system case; save before a destructive or terminal branch.
7. Test catalog events one at a time using a suitable normal-country or CXT branch, documenting the owner and setup method before triggering.
8. Record all custom 3D units later in a dedicated CXT recording save, reconciling actual units/entities against `unit_recording_inventory.md`.

The CXT command switches the player and annexes the former country without transferring its troops.
It also allocates foreign states for occupation and facilities, grants technologies and projects, stocks equipment and replenishes resources.
These changes are confined to disposable QA saves.
CXT therefore demonstrates fixture behavior and accessible controls but cannot prove natural research, affordability, ordinary eligibility or event progression.
Those require the preserved normal campaign or a separate country-specific save.

The source contract is `docs/testing/chaosx_test_country.md`.
Its package readiness flags for events 21, 23, 24, 27, 28, 29, 32 and 35 do not prove those events fired or their mechanics succeeded.
Runtime observations, save identities, fresh-log results and actual media must be recorded before promoting any case to passed.
