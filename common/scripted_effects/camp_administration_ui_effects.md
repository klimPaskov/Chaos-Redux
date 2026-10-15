# Administration controls and material records

All public commands are country scoped and shared by GUI and ordinary decisions.
The caller supplies temporary `camp_admin_control_requested` using the centralized priority, mandate, budget or role enum.
`camp_admin_set_priority`, `camp_admin_set_budget`, `camp_admin_set_mandate` and `camp_admin_set_selected_role` refresh the shared quote, validate the same eligibility predicate, pay once and consume the request.
A rejected or unchanged request pays nothing.
Control changes do not execute monthly production, replenish the current month's budget, advance projects or award research.
`camp_admin_refresh_command_quotes` maintains the display, affordability and payment values from current network size and centralized administrative coefficients.
Political power here pays for a deliberate administrative change; routine operation uses the foundation's material budget.
These orders charge the Event 026 sale price: after computing the ordinary policy, mandate and role quotes, `camp_admin_refresh_command_quotes` passes each through the production `black_friday_price_table_quote` at the ratio the sale price table holds and stores that ratio in `camp_admin_command_quote_sale_ratio`.
`black_friday_price_table_refresh_owner_quotes` refreshes every country whose stored ratio differs from the table when a sale starts or ends, so the window shows the price the next order charges.
Each paid order credits one Political Power sale purchase.

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
The window shows at most four values per view: people held, output, maintenance and deaths this month; workforce, capacity and cumulative site deaths live in their tooltips, and Records lists cumulative deaths by cause only.
Monthly deaths display in people through `camp_admin_gui_month_deaths_people` and `camp_admin_gui_site_month_deaths_people` (thousands times `camp_admin_value.people_per_k`).
`camp_admin_gui_economy_frame` and `camp_admin_gui_institution_frame` drive the eleven-frame `GFX_camp_admin_meter` (frame 1 empty, frame 11 full, `camp_admin_meter` constants); the meters show only while an economic project slot is active or an institutional target exists.

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

## Lasting closed records

Locations builds a duplicate-free display union of active custody, civilian replacement and immutable original-authority `camp_admin_known_site_states`.
`camp_admin_gui_site_record_visible` is a read-only state predicate with PREV as the display country: original authority must match, and either current authority is valid or the site is closed.
The existing all/labor/custody filters retain the recorded role; attention also recognizes provenance uncertainty.
Records uncertainty counts each host once across known, active custody and occupation registries.
The fallback warning excludes an aligned exact zero-live history after unrelated territorial/shared loss, using the existing known-site reform proof; historical row count alone does not represent living held exposure.
Explicit sticky, structural, unverified, transaction, counter-regression and pending-reconciliation reasons still warn, and malformed zero aggregate with a live row cannot satisfy the empty-history proof.
This display exception never changes current action freshness, flags, original rows or registry membership.
Closed custody-only ambiguity therefore survives active unregister, capture and evidence resolution in the original country's warning count.
The other controller receives no original-country archive entry.

`camp_admin_gui_site_has_current_output` reads original authority and current control, then requires either a currently proven supported operational workforce or the existing positive civilian workforce and civilian replacement registry.
Archive-only stale allocations do not become displayed productive workers or economic factors.
The selected cache reads recorded custody/death quantities while using zero productive values when this output predicate fails; it does not edit the source state's allocations.
`camp_admin_has_selected_proven_operating_site` composes current operating-site context with fresh host provenance before role/work/release actions.
The contextual `camp_admin_has_selected_operating_site` remains available to Records-locked status getters so they can explain why an otherwise operating host's actions are unavailable.
National policy controls and country actions require a currently existing initialized actor; archive display itself initializes no policy.
No new layout, window, localisation key, asset or sprite is introduced.

All new display predicates have no input defaults, no persistent state writes and no cleanup; their PREV actor comes from the existing country display/selection scope.
The display-source scratch array and observation pointer retain their existing cleanup after each refresh.

```txt
# Country scope; rebuild read-only Locations/Records from retained metadata.
camp_admin_refresh_interface = yes
# In its state iteration, PREV remains the country display owner.
if = { limit = { camp_admin_gui_site_record_visible = yes } camp_admin_cache_selected_site = yes }
```

The 2026-10-03 archive source scenarios and mandatory MCP route gaps are recorded in `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/origin_closed_site_archive_integration_2026-10-03.md`.
Source list membership and enablement tests are not GUI pixel or native engine evidence.

## Automatic open-window observation

`camp_rework_open_ledger` requests the shared [automatic panel observer](national_policy_panel_effects.md) after its ordinary opening path.
Each hourly open-human delivery invokes only `camp_admin_refresh_interface`, which reads published existing registry, policy, work and site data without invoking the opener, registration, initialization, population reconciliation or work advancement.
Existing command and owner display callbacks retain their immediate refresh paths, while native controls and tooltips have no dirty gate.
All seven UI foreach passes reset private break variables before traversal, and the two project quote outputs are initialized by the interface caller before consuming the helper result.
Closed windows perform no projection, and the shared delivery retires when no eligible panel is open.
