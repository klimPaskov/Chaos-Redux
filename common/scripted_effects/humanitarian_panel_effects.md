# Humanitarian panel presentation helpers

The parent accepted the famine and migration panel backends and their reference images for the national policy and humanitarian panels task on 15 October 2026.
These helpers read gameplay state and write country presentation state only.
They never initialize a humanitarian subsystem, register a country or state, assess food, reconcile laws, pay costs, move people, create receipts or advance work.

## Public contract

All public helpers and predicates below use the actual actor country.

| API | Inputs and defaults | Outputs and side effects | Caller |
| --- | --- | --- | --- |
| `famine_panel_open_window`, `migration_panel_open_window` | Eligible actor, optional existing view/group | Sets its open flag, clears and dirties the other panel, defaults only missing view/group to overview/group 1, refreshes presentation | Parent category or GUI opener |
| `famine_panel_close_window`, `migration_panel_close_window` | Actor | Eligible close clears its own open flag and advances its matching dirty counter, invalid actor invokes pointer invalidation | Parent close controls |
| `famine_panel_refresh`, `migration_panel_refresh` | Actor, optional `*_panel_selected_state` | Rebuilds the bounded state list, validates selection, copies overview/selection/work presentation and increments `*_panel_dirty` | Opener, state click and existing registered-country processor while open |
| `famine_panel_is_eligible`, `migration_panel_is_eligible` | Actor | Existing human country using normal civilian systems, excluding special Chaos countries and AI | Parent visible/click guards and effects |
| `famine_panel_has_selected_state`, `migration_panel_has_selected_state` | Actor and stored selection | Requires current list membership and exact current ownership or control in the actual state scope | Parent state/action surfaces and getters |

Set `*_panel_selected_state` to an actual listed state before refreshing.
The list arrays `famine_panel_states` and `migration_panel_states` contain actual state values for a native dynamic list with `change_scope = yes`.
The state row keys are `famine_panel_state_row` and `migration_panel_state_row`.
Rows use `This.GetName` and the existing state-stage/header selectors through the panel's small assessment-aware row selectors.

The panel eligibility boundary intentionally retains the original category presentation exclusion.
It does not change the separate Holy Realm exception for native civilian laws or humanitarian simulation.
Effect-time eligibility loss closes both panels, clears both selected pointers and clears both UI lists, then advances both dirty counters once.
A normal close advances only the matching dirty counter once, while opening across panels advances the other counter once and its own counter through the existing refresh.
These changes invalidate native GUI caches without changing gameplay or other presentation values.
No `scope_exists` test is used to validate a stored selection.

## State list and selection

Refresh saves the actor as the chain-local `humanitarian_panel_actor` event target.
The two existing native `every_owned_state` and `every_controlled_state` passes now collect every relevant state directly, without traversing a global active-state registry.
Relevance requires published active food or movement flags, positive live counters or obligations, a nonzero industrial workforce balance, explicit prepared/mission/corridor work or exact actor-owned pending-action membership.
Mere ownership and zero-filled fields do not qualify.
The pending-action membership check reads the actor's existing array through a native predicate, without iterating its rows for collection.
The candidate array is deduplicated and filtered against the current actor's actual ownership or control.
This removes dependence on a state's position in a large global registry while retaining the same two bounded native state passes and unchanged local priority passes.
No world sweep or simulation registration is introduced.

Famine rows are ordered catastrophic famine, famine, acute shortage, supply strain, then stable or unassessed work.
Migration rows put trapped civilians first, retaining native collection order for each group.
A selection missing from the rebuilt list or no longer owned/controlled is cleared.
The first valid row becomes the fallback selection, and an empty list leaves no pointer.
An arbitrary owned state cannot be selected unless it is genuinely in the list.

Each foreach invocation resets an explicit private break temporary immediately before use.
Food-stage and dominant-cause helper outputs are declared by every caller that consumes them after return.
The source fixture discards helper-local temporary storage after return rather than assuming one flat temporary dictionary.
The event target is regular and expires with the effect chain.
No global event target or durable gameplay pointer is added.

## Projection fields

Every regular write in this package is a country variable, array or flag under `famine_panel_*` or `migration_panel_*`.
State reads never create or repair state data.

Famine overview fields are `famine_panel_food_stage`, `famine_panel_reserve_amount`, `famine_panel_reserve_need`, `famine_panel_reserve_days`, `famine_panel_relief` and `famine_panel_priority_cause`.
The `famine_panel_food_assessed` and `famine_panel_reserves_assessed` flags distinguish missing assessment from a measured zero.
Recorded reserve days divide only published reserve amounts by positive published daily need in candidate states with initialized reserve receipts.
A pending first food observation does not establish a completed assessment.
The dominant pressure of the worst state uses the existing food component values and never recalculates food security.

Migration overview fields are `migration_panel_fleeing`, `migration_panel_trapped`, `migration_panel_sheltered`, `migration_panel_capacity` and `migration_panel_capacity_used`.
Flight and trapped amounts remain separate and are never summed into an invented displaced total.
`migration_panel_displacement_assessed` records whether a published movement counter was read.
`migration_panel_capacity_assessed` requires the migration owner's real capacity validation trigger and a published load.
Missing or stale capacity remains unassessed and is never initialized by observation.
Reception and departure text reads native laws directly without reconciling them.

Selected-state values are copied into matching country `*_panel_selected_<field>` variables.
Only the title dereferences the validated selected state, using the requested `[?*_panel_selected_state.GetName]` form.
Other selected text reads copied country UI values.
The selection flag/predicate is rechecked by the selected title, summary and details getters.

| Frame variable | Meaning |
| --- | --- |
| `famine_panel_food_stage_frame` | 1 unassessed, 2 stable, 3 strain, 4 acute, 5 famine, 6 catastrophic |
| `famine_panel_relief_frame` | 1 unassessed or not required, 2 open, 3 blocked |
| `migration_panel_displacement_frame` | 1 unassessed or calm, 2 fleeing, 3 trapped |
| `migration_panel_capacity_frame` | 1 unassessed, 2 spare capacity, 3 full or overloaded |

The parent owns whether these optional frame fields are consumed by sprites or text.
Their values do not imply an asset with the corresponding frame count has been supplied.

## Active work progress

`famine_panel_project_work` and `migration_panel_project_work` read the exact five aligned actor-owned pending arrays `*_action_ids`, `*_action_types`, `*_action_states`, `*_action_dates` and `*_action_starts`.
Only a positive UID on the selected state with a due date later than its recorded start can qualify.
The earliest due row wins, with stable row order for ties.
The helpers write `*_panel_has_active_work`, `*_panel_work_uid`, `*_panel_work_action`, `*_panel_work_start`, `*_panel_work_due`, `*_panel_work_remaining_days` and `*_panel_work_frame`.
The parent uses the existing eleven-frame `GFX_camp_admin_meter` with frame 1 through 11.

Progress is rounded to the nearest tenth from `(current date - saved start) / (saved due - saved start)`, clamped to the supported interval and shifted to frame 1 through 11.
Remaining whole days use the existing `chaosx_convert_date_offset_to_days` helper with caller-owned output storage.
The saved start and due timestamps are the action owner's original metadata, so no duration is estimated or reconstructed from current tuning.
Unaligned or missing start metadata never creates an invented clock.
Past-due work remains visible at frame 11 with zero remaining days until its owner resolves it.
These helpers never dispatch or complete an operation.

Refresh also calls the existing `famine_gui_refresh_selected_action_status` or `migration_gui_refresh_selected_action_status` presentation seam.
The action owner remains responsible for action validation, timing, refunds, costs, receipts, pending arrays and execution.

## Getters and ownership

`common/scripted_localisation/humanitarian_panel_localisation.txt` defines the exact requested getters:

- `GetMigrationPanelDisplacement`, `GetMigrationPanelCapacity`, `GetMigrationPanelReceptionLaw`, `GetMigrationPanelDepartureLaw`, `GetMigrationPanelSituation`, `GetMigrationPanelStateTitle`, `GetMigrationPanelStateSummary`, `GetMigrationPanelStateDetails` and `GetMigrationPanelActiveWork`.
- `GetFaminePanelFoodStage`, `GetFaminePanelReserveSummary`, `GetFaminePanelReliefAccess`, `GetFaminePanelSituation`, `GetFaminePanelStateTitle`, `GetFaminePanelStateSummary`, `GetFaminePanelStateDetails` and `GetFaminePanelActiveWork`.

Auxiliary selected-value, cause, row-status and work-title getters stay local to this presentation package.
Panel-specific values live in `localisation/english/humanitarian_panel_values_l_english.yml`.
The parent owns the action labels `*_panel_action_<suffix>_label`, the shared `humanitarian_panel_select_state` prompt, actual GUI/scripted-GUI files and all art wiring.
The work-title getters deliberately consume those safe actor-context labels rather than native decision titles that can require `FROM`.

The reference images are `.tmp/national_policy_panels/gui/migration_states_reference.png` and `famine_overview_reference.png`, accepted by the parent within the current task.
Their overview cards map to the exact getters above, state-browser rows map to the two arrays and row keys, selected details map to validated copied projections, and the work bar maps to the recorded progress fields.
This worker owns no layout, click rectangle, new art, GUI render or visual acceptance claim.
Three famine values and four migration values follow the parent's accepted budget, with admission and departure remaining distinct policy choices.

## Tuning and validation

`common/script_constants/humanitarian_panel_constants.txt` owns view/group IDs, presentation states, cause IDs, frame bounds and progress steps.
Food stages and real action clocks remain their existing owners' constants and receipts.
No gameplay balance or AI weight is changed.

The maintained production-source fixture `.tools/test_humanitarian_panels.py` checks quiet opening without gameplay writes, mutual exclusion, view/group retention, bounded filtering and ordering, mission retention, stale/spoof target rejection, copied projections, real-versus-stale capacity proof, exact progress and eligibility cleanup.
It also imposes a hypothetical 1,000-row foreach limit on a 1,201-row registry and confirms late owned/controlled states remain listed while unrelated zero-filled states stay excluded.
The numeric while/for loop ceiling is documented, but no foreach ceiling is asserted from that stress assumption.
Usage is `python .tools/test_humanitarian_panels.py`, with JSON results written only under `.tmp/national_policy_panels/`.
It executes the shared date conversion body and models conservative helper-local temporary lifetimes.
The owner's action-status presentation call is recorded as an approved external seam, and its internals are covered by the action owner's own checks.
No render or live game execution is claimed here.

Future presentation fields should extend this package's UI prefixes and reuse published owner state.
Opening or refreshing a panel must never become an initialization or simulation endpoint.
