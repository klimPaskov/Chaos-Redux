# Second Dust Bowl Localisation Audit Handoff

Date: 2026-07-27

Status note: The cancellation non-wiring finding below is a historical pre-parent-wiring observation. Parent gameplay now records the authenticated cancellation payload through the history recorder, as reflected in `FALLOUT_SECOND_DUST_BOWL_PROOF.md` and the current Second Dust Bowl effects. Runtime acceptance remains unproven.

## Files changed

- `localisation/english/fallout_consolidated_l_english.yml`

No event script or scripted-localisation file was changed.

## Changed keys

- `chaosx.fallout.656.d` now names the dynamic candidate state directly instead of calling it authenticated.
- `chaosx.fallout.656.d.tt` now names the dynamic candidate state directly.
- `chaosx.fallout.658.move.success.d` and `chaosx.fallout.658.abandon.success.d` now describe the same state without implementation language.
- `fallout.event_log.second_dust_bowl.detail.shelter_success`, `move_success`, and `abandon_success` now use selected-state wording.
- `fallout.event_log.second_dust_bowl.detail.cancelled` was added for the existing cancellation payload constant.
- The two Event Log boundary keys were indented under `l_english` so the dedicated file parses as one YAML mapping.

## Behavior and display

Before the patch, player-facing text exposed the internal word authenticated for the target plains state.

After the patch, popup text uses the live state name and result text uses the same-state or selected-state wording.

Historical pre-wiring finding: the cancellation key was not wired because the then-current Second Dust Bowl effects did not emit the cancellation payload.

## Validation

- Confirmed all event-localisation references in events 656, 658, and 660 resolve to keys in the dedicated yml.
- Confirmed event names 656 through 662 are present.
- Confirmed all twenty-one dedicated scripted-localisation output keys resolve to dedicated yml keys, including the explicit callback-failure and unknown-payload branches.
- Confirmed the central Event Log file maps the 9171 history ID to the Second Dust Bowl name and detail keys exactly once.
- Confirmed the yml retains its UTF-8 BOM.
- Confirmed the dedicated yml parses with a standard YAML parser after the indentation repair.
- Confirmed no em dash or semicolon remains in the three scoped localisation files.
- Confirmed no duplicate key exists in the dedicated yml.

## Remaining risks

The dedicated scripted-localisation fallback now displays a neutral unknown-payload line instead of mislabeling an unrecognized payload as callback failure.

The cancellation payload is now emitted by the opening receipt cancellation effect and selected by the dedicated scripted-localisation branch. Runtime cancellation reachability remains engine-sensitive and unproven.

The human event options expose scripted affordability triggers without dedicated blocked-requirement custom tooltip keys. The four opening tooltips now name the issued target state and result timing.

Runtime Event Log rendering and state-name fallback behavior remain engine-sensitive and were not run.
