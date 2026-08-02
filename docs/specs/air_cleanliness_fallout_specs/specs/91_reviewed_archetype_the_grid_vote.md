# Reviewed archetype: The Grid Vote

Status: accepted bounded implementation tranche. The chain is dormant until the Fallout scheduler activation contract opens. It does not register Fallout as an ordinary event, create a successor country, or add a world iterator.

The Grid Vote is a Technate chain for a Manchurian Reactor Keeps district after The Patent After the End closes. The surviving cable network can no longer provide full current to the reactor wards, neighboring settlements, and military corridors at once. The player chooses equal neighboring shares, priority for the settlements that rebuilt the lines, domestic reserve first, or a protected military network.

## Ownership set

| Surface | Identity |
| --- | --- |
| Candidate and opening | `824` |
| Hidden AI opening | `825` |
| Human delayed result | `826` |
| Hidden AI delayed result | `827` |
| Human callback | `828` |
| Hidden AI callback | `829` |
| Cleanup | `830` |
| Transaction | `710089` |
| Scheduler route | `7210` |
| Event Log history | `9195` |
| Region | East Asia |
| Required predecessor | state flag `fallout_event_817_memory_closed` |

The candidate selector chooses the lowest eligible native state and freezes only that host. The chain uses the existing Fallout ordinary receipt, delayed result, callback, and exact cleanup contract.

## Choices and mechanics

The four branches spend distinct survival resources and write different grid memories.

| Branch | Cost | Primary consequence |
| --- | --- | --- |
| Share power with every neighbor | Food 2, Medicine 2, Recognition 2 | Equal rationed current improves bilateral trust and trade while reducing reserve power. |
| Favor the settlements that built the lines | Fuel 2, Recognition 3, Cohesion 2 | Repair clients gain priority, production capacity, and a durable client dependency. |
| Reserve power for domestic districts | Scrap 2, Power 2, Medicine 2 | The Manchurian Reactor Keeps protects its clinics and pumps while neighboring trust weakens. |
| Bind the grid to military corridors | Food 2, Fuel 2, Recognition 2 | A guarded corridor gains strategic reach while civilian lines accumulate grievance. |

Each result grades Air Winter, Supply Access, Medicine, Cohesion, Recognition, grid legitimacy, dependency pressure, export trust, reserve power, client capacity, diplomatic power, and grid memory. Failure routes bounded Deaths through the existing system and damages one infrastructure level in the host state. The first result arrives after `42` days. The second-year review arrives after `330` days and uses a deterministic score with success, partial, and failure outcomes.

The chain records bilateral opinion, state memories for the selected neighbor, country memories for the chosen power order, Event Log history `9195`, hidden-AI parity, and authenticated cleanup. It never calls the Fallout consequence coordinator.

## File ownership

| Surface | File |
| --- | --- |
| Constants | `common/script_constants/fallout_world_end_grid_vote_constants.txt` |
| Candidate registration | `common/scripted_effects/fallout_world_end_event_candidate_effects.txt` |
| Triggers | `common/scripted_triggers/fallout_world_end_grid_vote_event_triggers.txt` |
| Effects | `common/scripted_effects/fallout_world_end_grid_vote_event_effects.txt` |
| Events | `events/fallout_world_end_events.txt` |
| Localisation | `localisation/english/fallout_world_end_grid_vote_l_english.yml` |
| Event Log routing | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_localisation/fallout_world_end_grid_vote_event_log_scripted_localisation.txt` |
| Report art | `gfx/event_pictures/fallout/report_event_fallout_grid_vote.dds` |
| Sprite registration | `interface/fallout_world_end.gfx` as `GFX_report_event_fallout_grid_vote` |

The chain is a dormant source package. Scheduler activation, host authority, save recovery, multiplayer delivery, runtime Event Log rendering, and release-floor credit remain unproven by design.
