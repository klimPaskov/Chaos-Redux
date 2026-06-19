# Event 012 Old-Seat Arbitration Decision/Mission Audit Handoff

Date: 2026-06-19
Subagent: `chaosx_decision_mission_auditor`

## Findings And Patch

- No blocking decision/mission issues remained after the patch.
- `africa_convene_old_seat_arbitration` now uses `days_re_enable = constant:africa_decision_days.old_seat_arbitration` instead of a stale `days_remove` timer. The decision starts the mission immediately in `complete_effect`, so the 60-day value is a cooldown, not a timed setup period.
- `africa_convene_old_seat_arbitration_desc` now says the next eligible case is convened, matching `africa_start_old_seat_arbitration` auto-selecting the first eligible pair by priority.

## Evidence

- Start gates require the Authority Register, Old-Seat Mission Calendar, no active arbitration, one unresolved pair, and settled prerequisite dossiers.
- The 120-day mission checks a stored seat plus pair-specific values before success.
- Political power, support equipment, manpower, command power, and army experience are spent through the scripted cost helper, so the decision is not a political-power store.
- The one-active cap comes from `africa_old_seat_arbitration_active`.

## Validation

- Confirmed the 120-day mission timeout remains intentional and separate from the 60-day convene cooldown.
- Confirmed `days_re_enable = constant:...` has vanilla and local precedents.
- Confirmed localisation still names the auto-picked case accurately.
