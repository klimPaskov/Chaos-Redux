# Event 005 Soviet Collapse Parent Focus Layout And Payload Guard Tranche

Date: 2026-06-04

## Scope

Parent-side bounded implementation after the full focus audit handoff. This tranche only touched:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

No `gfx/flags/*` files were edited.

## Implemented

- Added a temporary per-effect-chain guard to `soviet_collapse_apply_high_chaos_focus_payload`, so focuses that call multiple shared reward helpers do not repeat the same high-chaos claims, AI war pressure, and identity package in one completion reward.
- Removed the Ukraine Directory capstone prerequisite on `ukr_soviet_collapse_the_western_question_cannot_wait`, because it tied a military political end-state to an unrelated expansion branch and forced a long pathline through the tree.
- Reworked the Ukraine right-side expansion/foreign lane into a cleaner compact route:
  - direct national claims, western question, Black Sea hegemony, breadbasket empire, Great Steppe plan, and outside-old-map endgame now read as a right-side expansion sequence.
  - foreign advisers, ports, equipment corridor, Romanian/Turkish/Carpathian follow-ups were shifted to avoid crossing the political and military center.
- Reworked the Belarus opening/rail/route area into compact lanes:
  - the route selector, military transit, state-between-armies, railway neutrality, timetable, central dispatch, league supply, and Baltic/foreign nodes were shifted to remove direct static pathline-through-focus risks.

## Validation

- Static focus pathline audit for `soviet_collapse_ukraine_focus_tree`: `0` risks.
- Static focus pathline audit for `soviet_collapse_belarus_focus_tree`: `0` risks.
- Brace balance:
  - `common/national_focus/005_soviet_collapse_republics.txt`: depth `0`, min depth `0`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`: depth `0`, min depth `0`
- `git diff --check` passed for the touched script files and this handoff.
- `rg -n "<=|>="` found no unsupported comparison operators in the touched script files.

## Remaining Work

The full focus-tree goal is not complete. The subagent audit identified 41 Soviet Collapse focus trees and 1,698 focuses, with the next priority tranches:

- Top reward-spam sites in custom splinters and factory successors.
- Short chaos tree depth for `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `PRA`, and `OGB`.
- Ancient restoration mechanics for `KZR`, `SOG`, `KHW`, and `ALN`.
- More explicit focus-to-decision unlock visibility across Kazakhstan, Moldova, PRA, MFR, CFR, returned names, and custom splinter routes.
- CFR/MFR/Moldova and short-tree mutex layout review.

