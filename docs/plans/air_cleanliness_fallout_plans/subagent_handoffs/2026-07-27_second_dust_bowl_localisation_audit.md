# Second Dust Bowl Localisation Audit Handoff

Date: 2026-07-27

## Files changed

- `localisation/english/fallout_world_end_second_dust_bowl_l_english.yml`

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

The cancellation key is not wired because the current Second Dust Bowl effects do not emit the cancellation payload.

## Validation

- Confirmed all event-localisation references in events 656, 658, and 660 resolve to keys in the dedicated yml.
- Confirmed event names 656 through 662 are present.
- Confirmed all fifteen dedicated scripted-localisation output keys resolve to dedicated yml keys.
- Confirmed the central Event Log file maps the 9171 history ID to the Second Dust Bowl name and detail keys exactly once.
- Confirmed the yml retains its UTF-8 BOM.
- Confirmed the dedicated yml parses with a standard YAML parser after the indentation repair.
- Confirmed no em dash or semicolon remains in the three scoped localisation files.
- Confirmed no duplicate key exists in the dedicated yml.

## Remaining risks

The dedicated scripted-localisation fallback still displays callback failure for an unrecognized or unassigned payload.

The existing cancellation constant has no gameplay assignment and the new cancellation key has no selector branch.

The human event options expose scripted affordability triggers without dedicated blocked-requirement custom tooltip keys.

Runtime Event Log rendering and state-name fallback behavior remain engine-sensitive and were not run.
