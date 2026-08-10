# Event 016 Mengele project bridge handoff

## Status

Implemented the narrow Mengele Directorate bridge for the nine non-cloning Event 016 native prototype projects. The existing `sp_mengele_cloning` project remains the only Mengele cloning project and continues to call `clone_select_mengele_refinement`. Strategic Singularity remains gated by the Kruger State trigger and was not widened.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects |
| --- | --- | --- | --- | --- |
| `brilliant_scientist_mengele_project_provider_is_valid` | Country trigger | Existing `is_mengele_clone_directorate_country` identity | Boolean provider gate | Fails closed for current-host and incident flags; never calls `brilliant_scientist_is_current_host` |
| `brilliant_scientist_can_research_mengele_*_prototype` (9) | Country trigger through native project `FROM` scope | Family availability/all-available flag and completion flag | Boolean project visibility/availability | Does not read Event 016 facility targets, stage arrays, or capacity |
| `brilliant_scientist_record_mengele_project_prototype` | Country effect | Temporary `brilliant_scientist_project_family` | Provider completion flag and result | Clears the family availability flag; adds the three provider dynamic modifiers or grants one mapped custom operational family; resets selectors; refreshes dynamic modifiers |
| `chaosx_grant_custom_operational_technology` | Country effect (existing public API) | Temporary `chaosx_custom_technology_family` | Existing hidden custom tech, external grant flags, capped template/equipment/provider runtime, and grant result | No Event 016 project history or host ledger; clone selector is Mengele-aware |

Family mapping is computation -> provider modifier, materials -> provider modifier, biomedical -> provider modifier, teleportation -> portal API, robotics -> robot API, paleogenetics -> paleogenetic API, xenobiological synthesis -> xenobiological API, alien arms -> exotic API, and temporal -> temporal API. Cloning is intentionally absent from this dispatcher because `sp_mengele_cloning` owns it.

## Constants and tuning

`common/script_constants/016_mengele_project_bridge_constants.txt` centralizes the provider prototype results: computation research/encryption, materials efficiency/resource penalty, and biomedical weekly manpower/experience loss. `directorate_special_project_availability` now gives the nine families equal default random weights alongside the existing zombie and cloning weights; the parent agent owns the required probability compare pass.

The three provider dynamic modifiers and the neutral completion tooltips have matching English localisation entries in `localisation/english/016_brilliant_scientist_projects_l_english.yml`.

## Event targets and cleanup

The bridge creates no event targets and never initializes or mutates Event 016 ledgers. Completion clears the matching `directorate_special_project_*_available` flag, sets the matching `directorate_special_project_*_completed` flag, resets temporary family selectors to neutral values, and refreshes provider dynamic modifiers. `make_all_directorate_special_projects_researchable` sets all ten family availability flags; `make_random_directorate_special_project_researchable` selects one ungranted family with equal weights and falls back to the complete portfolio when no fresh choice remains.

## Migration and call sites

The nine native Event 016 project definitions now OR their original Kruger gate with the matching Mengele gate for both `visible` and `available`. Their existing `project_output.country_effects` still call `brilliant_scientist_record_new_project_prototype`; that effect dispatches to the Mengele bridge only for a Mengele Directorate country and preserves the original Kruger ledger path otherwise. Existing cloning and all six Singularity project definitions remain unchanged.

## Evidence and validation

- Required offline Paradox wiki pages and vanilla Special Projects, project, specialization, prototype-reward, script-constant, effects, and triggers documentation were read before editing.
- `hoi4_tech_inspect` trace for `clone_infantry_access_tech` returned workspace `mod_chaos_redux_ea3b2d67c2c0`, code `TECH_INSPECTED_PARTIAL`, artifact `6deab75961672bba76f38cdf20145144cb94c99473c70df33b80553907fea62e`.
- A refreshed `hoi4_tech_inspect` lint returned code `TECH_INSPECTED_PARTIAL`, artifact `b8b5dfe09f1af060f643addc6fd60f6d16a9afb10bda417a8504325467a14619`, and no MCP blockers; the report remains partial because helper projections were deferred in this large workspace.
- Bracket-depth checks returned zero for every touched Clausewitz script. No unsupported `<=`/`>=` operators or temporary-variable clearing effects were added.

The installed MCP exposes no dedicated special-project inspection route, so project visibility/facility behavior could not receive engine-backed special-project evidence here. Live game and save validation remain parent-owned.

## Risks and limitations

The bridge intentionally does not provide Event 016 theory/deployment/weaponization, event-log, evolution, containment, facility-target, or Singularity state to Mengele. Native project specialization/facility availability still belongs to the normal special-project engine and should be checked by the parent in the live consumer. Public custom-tech grants intentionally rebuild the neutral capped-template/equipment/provider runtime required to make those technologies usable; they do not create Event 016 project history or Kruger host state.
