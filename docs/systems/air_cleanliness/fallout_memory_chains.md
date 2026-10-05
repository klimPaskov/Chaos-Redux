# Fallout Country-Memory Opening Chains

Every country memory that a vanilla 1936 major power receives after the Fallout has its own opening chain. The chain asks the survivor how it will rebuild authority in its capital in the first season, settles the result after forty days, and reviews it after the first winter. Agent decision A17 in `docs/plans/air_cleanliness_fallout_plans/agent_decisions_2026-10-04.md` records the design choices; the event ids are in `FALLOUT_EVENT_ID_LEDGER.md`.

## Chains

| Memory | Usual survivor | Chain | Events | Choices | Institutions a branch can found |
| --- | --- | --- | --- | --- | --- |
| `federal_continuity_zone` | USA | The Broken Federal Chain | 1102 to 1108 | emergency congress, state guard bargain, military custodian | Emergency Congress, State Guard Compact, Federal Supply Custodian |
| `british_emergency_isles` | ENG | The Island Ration Book | 1109 to 1115 | ration parliament, North Sea convoys, royal shelters | Ration Parliament, North Sea Convoys, Royal Shelter Order |
| `french_loire_continuity` | FRA | The Prefects Return | 1116 to 1122 | prefects, Loire ration state, column to Paris | Prefectoral Administration, Loire Ration State, Claim of Paris |
| `rhine_dead_cities` | GER | Factory Ghosts | 1123 to 1129 | licensed salvage crews, restart in place, guild charter | Licensed Salvage Crews, Dead-City Works, Guild Works Charter |
| `italian_apennine_communes` | ITA | The Parish Granaries | 1130 to 1136 | parish kitchens, mountain toll roads, plains salvage | Parish Kitchen Network, Apennine Toll Roads, Plains Salvage Company |
| `ural_continuity_directorate` | SOV | The Command Archive | 1137 to 1143 | command lines, reactor privilege, marshals in the pit towns | Restored Command Lines, Reactor Privilege, Marshal's Pit Towns |
| `japanese_shelter_archipelago` | JAP | Dense Shelter Rules | 1144 to 1150 | ward associations, fisheries, imperial shelter court | Shelter Ward Associations, Fisheries Under Ash, Imperial Shelter Court |
| `yellow_river_famine_councils` | CHI | River Grain Quotas | 1151 to 1157 | equal quotas, army districts, floodgate repair | Yellow River Granaries, Grain Army Districts, Floodgate Corps |

## How a chain runs

1. The living-world candidate review (`fallout_event_build_country_candidate_registry`) adds the chain's row for a country with the memory, once orientation is complete, when its capital has current survival and Air Winter rows, Cohesion and Recognition meet the minimums, and it can pay for at least one choice. The row uses primary family `successor_country_memory`, cooldown family `successor_memory`, and a country-memory match, so the scheduler favours it.
2. Opening (N, hidden AI N+1): three choices with survival-resource costs. The hidden AI takes the affordable choice with the highest priority, plus a bonus for the choice its government archetype favours.
3. The choice is graded at once from the capital's Supply Access and shelter, the chain's standing, Cohesion and one or two survival resources. After forty days the result (N+2, N+3) applies resource, Cohesion, standing, Supply Access and Air Winter changes in the capital. A success or partial result founds the branch's institution (a permanent national modifier); a failure adds a setback modifier for 180 days and costs lives in the capital.
4. After about nine months the review (N+4, N+5) adds standing, Cohesion, Recognition, Supply Access and reclamation to a score. Success confirms the institution (or founds it late) and adds a 300-day recovery modifier; failure dissolves the institution and adds a 300-day modifier for the lost authority.
5. Cleanup (N+6) releases the scheduler rows and closes the chain for the Fallout generation. `fallout_<chain>_opening_route` keeps the chosen branch for later content.

Country loss and generation change cancel pending rows through the scheduler's delayed-row reconciliation. All values are script constants in the `fallout_event_<N>_*` categories of `common/script_constants/fallout_consolidated_constants.txt`.

## Memory protection

Each of these memories is now protected in `fallout_country_memory_candidate_is_protected`, so a second survivor seated in the same area receives a neighbouring memory instead of sharing the chain: Scottish Hydro Parliament for the British Isles, Breton Port League for the Loire, Balkan Mountain Wards for the Apennines, Volga Ash Host for the Urals, Hokkaido Snow Administration for Japan and Sichuan Interior Shelter for the Yellow River. A neighbour that is itself a taken protected memory passes on once more (a second Manchurian survivor reaches Sichuan through the Yellow River).

## Icons and art

The chains reuse Fallout report art already registered in `interface/fallout_consolidated.gfx`: `GFX_report_event_fallout_vault_of_voices`, `GFX_report_event_fallout_ship_that_will_not_dock`, `GFX_report_event_fallout_river_ration_league`, `GFX_report_event_fallout_working_machine`, `GFX_report_event_fallout_mountain_pass_census`, `GFX_report_event_fallout_mine_generator`, `GFX_report_event_fallout_metro_republic_below` and `GFX_report_event_fallout_canal_schedule`. Institution and outcome modifiers use vanilla generic idea sprites (listed in each `fallout_<chain>_*` block of `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`). No new sprite is required.

## Future plans

- A second chain for each memory, keyed on `fallout_<chain>_opening_route` and the institution it founded (for example the Emergency Congress facing a shelter vote crisis, or the Reactor Privilege facing a strike).
- Dedicated report art for each memory.
- Chains for the memories that medium powers receive (Canada, Australia, the Raj, South Africa).
