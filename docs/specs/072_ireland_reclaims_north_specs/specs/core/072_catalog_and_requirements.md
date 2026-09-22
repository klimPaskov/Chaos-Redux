# Event identity and requirement contract

| Field | Required value |
| --- | --- |
| Numeric catalog ID | 72 |
| Filename prefix | 072 |
| Existing slug | ireland_reclaims_north |
| Event name | Ireland Reclaims the North |
| Type | Minor Fire-Once |
| Authoring status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Formables |
| Cluster ID | 6 |
| Cluster role | Low member |
| Existing runtime namespace | chaosx.nr72 |
| Existing dispatcher entry | chaosx.nr72.1 |
| Source spec location | docs/specs/072_ireland_reclaims_north_specs/ |
| Working plan location | docs/plans/072_ireland_reclaims_north_plans/ |

The user-supplied concept supersedes the old event's refusal-triggered civil war, holder ultimatum veto, and Britain-only victory event.
Do not rename the existing namespace to use a padded numeric suffix.
Padding applies to filenames and package ownership.

## Design acceptance requirements

| ID | Required result | Owning specification |
| --- | --- | --- |
| R01 | A valid Ireland and northern holder are resolved before event consumption | core/072_reclamation_war.md |
| R02 | An Ireland already controlling the North is excluded | core/072_reclamation_war.md |
| R03 | Immediate real divisions, equipment, personnel, and support are granted | military/072_opening_force.md |
| R04 | Opening forces scale substantially through all three Evolutions | mechanics/072_evolutions.md |
| R05 | Victory requires only the northern objective, never conquering Britain | core/072_reclamation_war.md |
| R06 | Scripted peace retains the North and preserves unrelated wars | integration/072_runtime_contract.md |
| R07 | Alternate valid holders are supported | core/072_reclamation_war.md |
| R08 | The new focus tree loads only after successful settlement | focus_tree/072_tree_architecture.md |
| R09 | Failure cannot later be converted into a free tree unlock | core/072_reclamation_war.md |
| R10 | Common integration, Gaelic, imperial, Celtic, Atlantic, army, navy, and air content are complete | focus_tree/ |
| R11 | The empire is a substantive formable with separate integration | mechanics/072_territorial_routes.md |
| R12 | The Celtic alternative does not force annexation of partners | focus_tree/072_celtic_route.md |
| R13 | AI targets the North and follows coherent postwar routes | ai/072_ai_design.md |
| R14 | Reunification and later milestones have appropriate news and assets | presentation/ |
| R15 | At most three Event 072 national spirits coexist | mechanics/072_values_and_spirits.md |
| R16 | Costs, mission phases, and route eligibility are visible and consistent | decisions/072_decisions_and_missions.md |
| R17 | Every formation category receives the exact-state puzzle | presentation/072_formable_gui.md |
| R18 | Achievements, prompts, country support, and validation handoffs are provided | presentation/, prompts/, plans |

## Catalog integration

Use the workbook as the editable catalog source during implementation.
The supplied CSV files are exported snapshots, not editing targets.
No workbook is included here and no catalog file has been changed.
Keep the authoring status until the implemented event passes the completion requirements.
The cluster member represents one initial firing.
Subsequent mission events, focus rewards, peace callbacks, and Evolution upgrades do not consume additional cluster slots.
The stronger late campaign does not silently change the user's Low classification.
