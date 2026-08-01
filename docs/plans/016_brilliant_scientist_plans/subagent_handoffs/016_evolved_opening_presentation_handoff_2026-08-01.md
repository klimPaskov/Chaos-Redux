# Event 016 evolved opening presentation handoff

## Scope

This tranche makes the already-wired pre-fire evolution state visible in the first public appointment and referral reports. It does not add a project family, evolution, event-log row, asset, or 3D model.

## Changed files

- `events/016_brilliant_scientist.txt`
  - `chaosx.nr16.2` now selects an Evolution I, II, III, or IV description when the host carries `brilliant_scientist_prefire_evolution_stage` at the matching stage constant.
  - `chaosx.nr16.3` uses the same stage selection for the foreign-referral opening.
  - The existing baseline descriptions remain the final branch for stage zero or an unavailable stage.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - Added eight player-facing description keys for the four evolved stages across the two opening reports.

## Runtime source of truth

`brilliant_scientist_prepare_prefire_evolution_context` stores the stage on the selected host before `chaosx.nr16.1` opens the appointment chain. The stage variable is read by the opening event before appointment or referral effects finalize the evolved opening, so the presentation branch does not alter the existing choice or reward path.

## Validation evidence

- The eight new event description keys are referenced exactly once by the event script and are present in the English localisation file.
- The changed event file has balanced braces and no unsupported comparison operators.
- The localisation file retains its UTF-8 BOM and has no duplicate keys in the added block.

## Remaining risks

Live in-game rendering of each stage branch remains user-owned because this workflow does not launch Hearts of Iron IV. The existing portrait-stage and project-seeding systems remain the runtime owners of visual and mechanical evolution state. 3D unit/model production remains explicitly deferred.
