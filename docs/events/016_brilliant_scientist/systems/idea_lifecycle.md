# Event 16 Directorate and Kruger State idea lifecycle

Event 16 uses a state-driven national-spirit lifecycle for the host's relationship with Doctor Warren Kruger. The lifecycle does not duplicate Kruger's unique advisor bonus. His advisor trait remains the sole source of the promised `+100%` research speed.

## Host lifecycle

The current host carries exactly one relationship spirit.

| State | Idea | Cause |
| --- | --- | --- |
| Initial appointment | `brilliant_scientist_kruger_appointment` | Kruger is active and no later institutional state has priority. |
| National dependence | `brilliant_scientist_national_scientific_dependence` | Dependence reaches the centralized lifecycle threshold. |
| Kruger Method | `brilliant_scientist_kruger_method` | Publication is complete and at least three project families have independent institutional replication. |
| Public renaissance | `brilliant_scientist_public_scientific_renaissance` | A public host publishes the work or establishes the regional science compact. |
| Controlled secret compact | `brilliant_scientist_controlled_secret_compact` | A secret host accepts negotiated limits or the safe regional compact. |
| Unrestricted laboratory state | `brilliant_scientist_unrestricted_laboratory_state` | The host grants the Evolution IV sovereignty concession. |
| Former-host vacuum | `brilliant_scientist_scientific_vacuum` | Kruger has departed and the country is recorded as a former host. |

The refresh effect is `brilliant_scientist_refresh_directorate_idea_lifecycle`. Directorate value changes, project-count reconciliation, transfers, and world-threat state changes call it explicitly. Repeated calls remove stale lifecycle ideas before applying the one state that currently has priority.

The Kruger State can independently carry `brilliant_scientist_world_threat_project_state` while its shared world-threat source is active. The idea is removed when the source clears or the state enters defeat aftermath.

## Tuning

`common/script_constants/016_brilliant_scientist_idea_constants.txt` owns lifecycle thresholds and modifier values. These values are separate from the general Directorate tuning tables so idea balance can be reviewed without changing project costs, evolution timing, or containment scores.

## Visual assets

The 13 idea sprites are registered in `interface/016_brilliant_scientist_idea_icons.gfx`.

Runtime DDS files live under `gfx/interface/ideas/016_brilliant_scientist/`.

The five Kruger State starting liabilities use:

- `GFX_idea_brilliant_scientist_improvised_laboratory_state`
- `GFX_idea_brilliant_scientist_inherited_project_portfolio`
- `GFX_idea_brilliant_scientist_fragmented_command`
- `GFX_idea_brilliant_scientist_experimental_supply_chain`
- `GFX_idea_brilliant_scientist_scientific_exodus`

The host and world-threat lifecycle uses:

- `GFX_idea_brilliant_scientist_kruger_appointment`
- `GFX_idea_brilliant_scientist_kruger_method`
- `GFX_idea_brilliant_scientist_national_scientific_dependence`
- `GFX_idea_brilliant_scientist_public_scientific_renaissance`
- `GFX_idea_brilliant_scientist_controlled_secret_compact`
- `GFX_idea_brilliant_scientist_unrestricted_laboratory_state`
- `GFX_idea_brilliant_scientist_scientific_vacuum`
- `GFX_idea_brilliant_scientist_world_threat_project_state`

Source art, processed previews, decoded DDS evidence, manifest data, and contact sheets remain under `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/` until the Event 16 goal reaches final acceptance.

## Former-host recovery transition

After Kruger departs, the former host exposes a separate recovery category with four one-time actions: reconstruct independent research, secure one selected abandoned archive, offer amnesty to surviving assistants, and request international inspection. Each action consumes factories and concrete equipment or manpower, records a success or failure receipt, and changes the hidden Independent Capacity, Grievance, or Exposure values. Three successful actions are required before `brilliant_scientist_former_host_recovery_complete` suppresses Scientific Vacuum; a failed action remains historical and cannot be clicked again, so the country must succeed with the remaining actions or live with the vacuum.

The recovery category reuses the existing reconstruction seal `GFX_decision_category_brilliant_scientist_aftermath_reconstruction` rather than introducing an unregistered asset. The gameplay source is `common/decisions/016_brilliant_scientist_former_host_recovery_decisions.txt`, with tuning in `common/script_constants/016_brilliant_scientist_constants.txt` and lifecycle calls in `common/scripted_effects/016_brilliant_scientist_recovery_effects.txt`.

Additional Kruger State lifecycle upgrades should reuse or replace the five existing liability families instead of adding another permanent stack.
