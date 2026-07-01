# Event 015 decision and mission audit handoff

## Files changed

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`

## Changed ids

- `decision_utopia_urgent_service`
- `mission_utopia_harvest_rotation`
- `mission_utopia_household_guard`
- `mission_utopia_league_aid_corridor`
- `mission_utopia_renunciation_vote`
- `utopia_manifesto_apply_apprenticeships_decision`
- `utopia_manifesto_start_rural_rotation_mission`
- `utopia_manifesto_start_guard_mission`
- `utopia_manifesto_start_league_aid_mission`
- `utopia_manifesto_start_renunciation_vote_mission`

## Before and after behavior

- Before: urgent-service AI referenced undefined trigger `utopia_manifesto_need_critical`.
- After: urgent-service AI reads existing crisis trigger `utopia_manifesto_need_crisis`.

- Before: apprenticeship completion called undefined helper `utopia_manifesto_refresh_ledger_status_flags`, so display variables and flags could go stale or error.
- After: apprenticeship completion calls existing `utopia_manifesto_refresh_ledger`.

- Before: four mission start helpers activated non-existent mission ids.
- After: the helpers activate the defined mission ids:
  - `mission_utopia_harvest_rotation`
  - `mission_utopia_household_guard`
  - `mission_utopia_league_aid_corridor`
  - `mission_utopia_renunciation_vote`

## Validation

- Searched the scoped decision, effect, and trigger files for the old undefined trigger, helper, and mission ids. No matches remain.
- Compared `activate_mission = ...` ids in `common/scripted_effects/015_utopia_manifesto_effects.txt` against mission ids defined in `common/decisions/015_utopia_manifesto_decisions.txt`. All four activated ids are defined.

## Skipped validation

- No in-game run was performed.
- No full parser run was performed because the Event 015 package is currently untracked within a large dirty working tree owned by concurrent work.

## Remaining issues

- Missions still resolve mostly as timed ledger checks and do not enforce the map objectives described in the spec.
- Needful Land arbitration immediately creates a claim instead of running a 120 to 180 day arbitration mission with success, refusal, compensation, or guarantee outcomes.
- Relationship and League target flags are not safely scoped per Utopian country.
- The scripted GUI ledger is display-only and has no action buttons, costs, AI equivalents, card cleanup, trend display, route display, geography display, or project count.
- Several localisation cost/value strings appear to use literal `?` markers where colour or variable formatting was likely intended.
