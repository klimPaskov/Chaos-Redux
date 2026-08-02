# Event 016 Context Receipt Persistence Handoff

## Scope

This tranche preserves durable Event 016 consequences when Doctor Warren Kruger moves to another valid host or when failed containment forms the fixed Kruger State. The affected receipts are the Event 060 rescue and Event 089 technology-sharing posture choices.

## Gameplay changes

- `common/scripted_effects/016_brilliant_scientist_effects.txt` copies `brilliant_scientist_research_failure_prevented`, `brilliant_scientist_tech_sharing_choice_recorded`, `brilliant_scientist_tech_sharing_network_joined`, and `brilliant_scientist_tech_sharing_refused` from the former host during ordinary transfer.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt` copies the same four receipts from the former host during KRG formation.
- Physical spacecraft custody flags remain host-bound by design; this tranche does not migrate them.

## Runtime contract

The existing Event 060 and Event 089 helpers still guard the active Kruger host and their existing receipt flags. Transfer and formation now preserve those guards' history, preventing a second salvage intervention or a second sharing-posture adjustment after the identity changes country.

## Validation evidence

- Exact receipt IDs were checked in both transfer and formation copy blocks.
- Touched Clausewitz files remain brace-balanced and contain no unsupported comparison operators.
- The two gameplay files were reviewed without staging unrelated worktree edits.

## Remaining risks

This is persistence hardening only. It does not add Event 016 log entries, evolutions, projects, assets, or 3D models. Event 137 and Event 151 remain documented future links because the repository has no corresponding source events to wire.
