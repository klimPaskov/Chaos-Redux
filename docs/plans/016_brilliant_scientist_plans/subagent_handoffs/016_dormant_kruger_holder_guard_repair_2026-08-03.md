# Event 016 dormant Kruger holder guard repair

Date: 2026-08-03

## Scope

This bounded repair keeps the fixed Kruger identity loader-safe while preserving duplicate prevention for every real appointment or forwarding transaction.

## Finding

`history/countries/KRG - Kruger State.txt` intentionally recruits `KRG_warren_kruger` during history initialization so the later Kruger State formation has a stable character token. The Event 016 availability, opening appointment, and initial send-away effects previously rejected any world state containing that character, so the dormant KRG holder could block the default opening before a host was selected.

## Changes

- Added `brilliant_scientist_has_non_dormant_kruger_holder` to `common/scripted_triggers/016_brilliant_scientist_triggers.txt`.
- The helper scans country scopes for `KRG_warren_kruger` but ignores the intentional `original_tag = KRG` holder.
- Replaced the raw global duplicate guards in `brilliant_scientist_automatic_event_is_available`, `brilliant_scientist_appoint_kruger_from_opening`, and `brilliant_scientist_forward_opening_to_selected_recipient`.
- Local role, transfer-recipient, project-force, evolution, and country-state checks were not changed.

## Validation evidence

- Both touched script files have balanced braces: triggers `315/315`, effects `2485/2485`.
- No unsupported `<=` or `>=` operators occur in either touched file.
- Static identity audit reports one helper definition, three helper guard references, zero remaining raw global duplicate guards, and one intentional dormant history recruitment.
- Focused read-only `hoi4_event_inspect` lint for `chaosx.nr16.1` returned `status = ok`, `EVENT_INSPECTED_PARTIAL`, no blockers, and zero blocking diagnostics. The analyzer still deferred workspace-wide helper and lifecycle passes, so this is source-level evidence rather than live campaign acceptance.
- No HOI4 runtime was launched.

## Boundaries

No 3D model package, native CBRN callback, project balance change, localization change, or unapproved fallback was introduced by this repair. Event 019 live provider scenarios, native CBRN integration, and user-owned campaign validation remain open in the Event 016 completion status.
