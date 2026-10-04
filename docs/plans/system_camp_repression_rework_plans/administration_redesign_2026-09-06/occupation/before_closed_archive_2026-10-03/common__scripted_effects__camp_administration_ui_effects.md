# Administration controls and material records

All public commands are country scoped and shared by GUI and ordinary decisions.
The caller supplies temporary `camp_admin_control_requested` using the centralized priority, mandate, budget or role enum.
`camp_admin_set_priority`, `camp_admin_set_budget`, `camp_admin_set_mandate` and `camp_admin_set_selected_role` refresh the shared quote, validate the same eligibility predicate, pay once and consume the request.
A rejected or unchanged request pays nothing.
Control changes do not execute monthly production, replenish the current month's budget, advance projects or award research.
`camp_admin_refresh_command_quotes` maintains the display, affordability and payment values from current network size and centralized administrative coefficients.
Political power here pays for a deliberate administrative change; routine operation uses the foundation's material budget.

`camp_admin_toggle_selected_work` pauses or resumes production only at a selected operating site with living custody, a labor or penal purpose, and a coercive national mandate.
The GUI click predicate and the effect use the same `camp_admin_can_toggle_selected_work` trigger; a rejected call records no work order.
Custody, maintenance obligations and mortality remain owned by the foundation.
`camp_admin_release_selected` requires reconciled living custody rows before its native button or effect can proceed, releases finite survivors through the shared camp foundation, and stops production there.
It writes a release history entry only when the foundation reports a positive actual release receipt. If a newly observed external population loss consumes all recorded survivors during the click, intake and assignments still stop, but no false survivor-release entry is written.
Neither operation changes physical population or mints military manpower.
Role conversion changes a separate primary role and never follows automatically from industrial priority.
Killing-center conversion requires both the regime gate and an explicitly authorized radical mandate.
The selected site must have a concentration-camp level available for conversion and must not already contain an extermination-camp level.
The command calls the existing genocide conversion and consequence API before taking the administrative political-power payment; a failed conversion pays nothing.
On success it registers the radicalized site in the existing bounded camp registry, ends its productive assignment, refreshes the finite-capacity calculation and economic contribution, and applies the package's established stability, resistance, evidence, visibility and accountability consequences.
The extermination building cannot be reversed by changing the primary role; closure and survivor release use their distinct lifecycle actions.

`camp_admin_refresh_interface` builds `camp_admin_gui_states` from the country's existing bounded active-site registry, applies the selected filter and validates selection.
It performs no world scan or gameplay simulation.
`camp_admin_view` and `camp_admin_location_filter` are enum values, while suspended/closed states remain flags.
The GUI cache also exposes separate custody, workforce, maintenance, current deaths and capacity values for the selected location, plus countrywide cause-separated monthly and cumulative death totals.

`camp_admin_project_institution_progress` reads the actual civilian claims, civilian review, major-country archive and oversight counters before falling back to an active or saved suspended major-country program.
It writes only `camp_admin_gui_institution_progress` and `camp_admin_gui_institution_target`, divides by the matching configured duration, and clamps the displayed fraction from zero to one.
It runs at interface refresh and never advances work, pays costs, changes custody, assigns deaths or changes the institutional slot.
An inactive slot with no paid program remains blank, while a suspended program retains its funded progress beside its suspended status.
`GetCampAdminCivilInstitutionStatus` supplies short states for the native status row, and `GetCampAdminCivilInstitutionSummary` retains the full country-specific descriptions and funded-month counts for broader summaries.

`camp_admin_project_origin_uncertainty` is a country-scoped display projection over the existing active-site and occupation-state arrays.
It counts a co-located custody and occupation host once, includes occupation-only hosts, and uses `camp_admin_gui_host_records_uncertain` to expose fresh, sticky or structurally invalid survivor records.
It runs at interface refresh and never changes physical population, custody rows, causes, original responsibility or shared Deaths.
Records shows the resulting location count through `GetCampAdminUnknownOriginNote`; it does not manufacture an unknown-origin death pool.
Administration and the selected-site panel say recorded custody because an uncertain quantity is the last verified stock and cannot authorize supported work or survivor orders.
The three production-source projection fixtures in `origin_records_projection_source_results.json` cover union deduplication, occupation-only uncertainty and a healthy empty host without gameplay mutation.
The current full-window and narrower Records inspection plus 1280 render timed out in `mcp/origin_pause_gui_2026-10-03`; final pixels and click regions remain unresolved.

`camp_admin_record_history` accepts temporary `camp_admin_record_kind` and optional `camp_admin_record_state_id` (zero for a national record).
It appends an immutable ID, kind, state and calendar date to five aligned arrays, consumes both inputs, and retains the latest 96 material records.
Older entries increment an archive count; cumulative losses and completed-project totals remain in their owning simulation ledgers.
Only actual accepted outcomes should call this helper.
Routine production or maintenance does not append records or notify the player.
The helper uses the foundation's documented calendar calculation rather than an unsupported month export.

The original responsible country's journal is not reassigned when a state is captured.
History is a projection of gameplay outcomes and never performs a population debit.
The parent integration owner must call interface refresh at the existing open/rebuild boundaries and append material project/research/liberation/closure outcomes at their accepted transaction boundaries.
