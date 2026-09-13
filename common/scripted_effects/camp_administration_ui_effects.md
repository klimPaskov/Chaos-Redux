# Administration controls and material records

All public commands are country scoped and shared by GUI and ordinary decisions.
The caller supplies temporary `camp_admin_control_requested` using the centralized priority, mandate, budget or role enum.
`camp_admin_set_priority`, `camp_admin_set_budget`, `camp_admin_set_mandate` and `camp_admin_set_selected_role` refresh the shared quote, validate the same eligibility predicate, pay once and consume the request.
A rejected or unchanged request pays nothing.
Control changes do not execute monthly production, replenish the current month's budget, advance projects or award research.
`camp_admin_refresh_command_quotes` maintains the display, affordability and payment values from current network size and centralized administrative coefficients.
Political power here pays for a deliberate administrative change; routine operation uses the foundation's material budget.

`camp_admin_toggle_selected_work` pauses or resumes production at the selected valid controlled institution.
Custody, maintenance obligations and mortality remain owned by the foundation.
`camp_admin_release_selected` releases the finite surviving detainees through the shared camp foundation and stops production there.
Neither operation changes physical population or mints military manpower.
Role conversion changes a separate primary role and never follows automatically from industrial priority.
Killing-center conversion requires both the regime gate and an explicitly authorized radical mandate.

`camp_admin_refresh_interface` builds `camp_admin_gui_states` from the country's existing bounded active-site registry, applies the selected filter and validates selection.
It performs no world scan or gameplay simulation.
`camp_admin_view` and `camp_admin_location_filter` are enum values, while suspended/closed states remain flags.

`camp_admin_record_history` accepts temporary `camp_admin_record_kind` and optional `camp_admin_record_state_id` (zero for a national record).
It appends an immutable ID, kind, state and calendar date to five aligned arrays, consumes both inputs, and retains the latest 96 material records.
Older entries increment an archive count; cumulative losses and completed-project totals remain in their owning simulation ledgers.
Only actual accepted outcomes should call this helper.
Routine production or maintenance does not append records or notify the player.
The helper uses the foundation's documented calendar calculation rather than an unsupported month export.

The original responsible country's journal is not reassigned when a state is captured.
History is a projection of gameplay outcomes and never performs a population debit.
The parent integration owner must call interface refresh at the existing open/rebuild boundaries and append material project/research/liberation/closure outcomes at their accepted transaction boundaries.
