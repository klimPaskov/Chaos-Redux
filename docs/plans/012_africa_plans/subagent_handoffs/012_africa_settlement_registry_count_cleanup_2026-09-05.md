# Event 012 Gods of Africa settlement registry-count cleanup

## Disposition

Implemented. This is a narrow owner-side lifecycle repair inside the accepted Event 012 Gods of Africa settlement contract.

## Finding

`gods_of_africa_commit_final_settlement` resolves each participant, queues its `.608` receipt, and then calls `gods_of_africa_clean_system`. The cleanup already cleared `gods_of_africa_participants`, but it did not reset `gods_of_africa_participant_count`. The acknowledgement event runs later and therefore could leave a stale nonzero host count whenever a settlement receipt remained unacknowledged.

## Change

`common/scripted_effects/012_africa_gods_effects.txt` now sets `gods_of_africa_participant_count` to the zero constant at the same time that final settlement clears the live participant array. The receipt remains presentation-only: `gods_of_africa_acknowledge_settlement` still clears the participant presentation flag and safely skips count subtraction once the host count is already zero.

## Evidence

- `gods_of_africa_commit_final_settlement` calls `gods_of_africa_clean_system` after queuing `chaosx.nr12.608` for each participant.
- `gods_of_africa_acknowledge_settlement` is a later receipt action and already guards subtraction with `participant_count > 0`.
- The vanilla/event source contract therefore has an empty live host registry immediately at settlement commit, independent of receipt timing.

## Validation boundary

The parent reran the focused HOI4 MCP event inspection for Event 012 after this edit. MCP remains an aggregate partial projection because the workspace defers large helper/lifecycle analysis; no focused blocking diagnostic was returned. Live save/playback confirmation remains owner-owned.
