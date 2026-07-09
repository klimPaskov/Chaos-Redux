# Event 020 Black Plague planning package, Part 3 candidate complete spec

This package continues the full rework specification for Event 020, Black Plague. It carries forward every Part 1 and Part 2 file, adds final acceptance criteria, updates the implementation prompts, and records the near-completion improvement-loop blocker.

This package is a candidate complete planning package. It is not fully process-final because this environment cannot spawn the mandatory `chaosx_improvement_loop_planner` subagent. The next live repository pass should run that subagent with `fork_context=false`, resolve its closure handoff or addendum, then mark the package canonical if no new design gaps remain.

## Source reading status

Part 1 recorded full reading of all uploaded project source files present in `/mnt/data`, including markdown skill and source files, custom subagent TOML files, and the three catalog CSV files. Part 2 rechecked the extracted Part 1 package and reprocessed the uploaded source files before adding focus-tree, country-package, decision, UI, rat warfare, counterplay, super-event, asset, and achievement blueprint layers.

Part 3 reprocessed the uploaded source file inventory and the extracted Part 2 package before adding the acceptance criteria, updated prompts, and blocker handoff. I did not inspect a live Chaos Redux repository tree because only uploaded source files and the Part 2 package were available in this environment. I also could not spawn project Codex subagents because only their TOML definitions were available.

## Design authority

The current user brief and continuation prompts are the design authority for Event 020. The old Event 20 catalog row remains stale source history because it describes a continent-wide temporary idea.

## New Part 3 files

- `reading/020_black_plague_part_3_reading_update.md`
- `specs/020_black_plague_spec_part_11_acceptance_criteria_and_final_prompts.md`
- `handoffs/020_black_plague_near_completion_improvement_loop_blocker_and_manual_review.md`
- updated `handoffs/temporary_continuation_prompt_not_part_of_spec.md`
- updated `prompts/020_black_plague_asset_prompt.md`
- updated `prompts/020_black_plague_super_event_prompt.md`
- updated `prompts/020_black_plague_achievement_prompt.md`
- updated `prompts/020_black_plague_decision_mission_prompt.md`
- updated `prompts/020_black_plague_coding_prompt.md`
- updated `prompts/020_black_plague_goal_prompt.md`
- updated `prompts/020_black_plague_subagent_routing_prompt.md`

## Carried-forward files

The package still includes every Part 1 and Part 2 file: core outbreak, shared disease board, spread, cure, weaponization, evolutions, rat nations, King of Rats, world-end, focus and country package deepening, decision and UI design, rat warfare, counterplay, super-events, assets, achievements, matrices, prompts, research, and reading ledgers.

## Current stopping point

The design content is complete enough for implementation planning, subject to the process blocker above. Part 11 defines acceptance criteria for the whole event, including required implementation surfaces, no-simplification rules, state-based disease requirements, shared disease-board requirements, deaths and Chaos integration, cure and weaponization boundaries, rat country package requirements, King focus tree requirements, world-end requirements, super-event and asset requirements, achievement requirements, AI requirements, documentation requirements, and spreadsheet alignment requirements.

## Required next action

In the live repository environment, run `chaosx_improvement_loop_planner` with `fork_context=false`. Use the continuation prompt in `handoffs/temporary_continuation_prompt_not_part_of_spec.md`. Resolve the planner output. If it returns closure, finalize the canonical package. If it returns an addendum, fold accepted content into the spec or record an explicit disposition before finalization.
