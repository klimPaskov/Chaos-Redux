# Origin-tagged destination custody foundation handoff

Disposition: implemented foundation helper patch and source-level occupation caller; engine receipt proof remains blocked.
Acceptance basis: parent assignment under the user-authorized camp, forced-labor and repression rework, with the seven-step transaction in `cross_state_movement_handoff.md` as the bounded contract.
The parent owns occupation transfer changes and final integration.

## Files and helper map

- `common/scripted_effects/camp_administration_effects.txt`: added site-owned aligned custody rows, local admission enrollment, read-only import quote, exact bind and inverse, row-aware deaths, release and outside-loss reconciliation.
- `common/scripted_effects/camp_administration_effects.md`: documented row data, helper inputs and outputs, side effects, transaction order and uncertainty.
- `occupation/test_custody_origin_rows.py`: focused source and arithmetic scenarios for the contract.

`camp_admin_initialize_rows` is state scoped and adopts a preexisting aggregate once as a local origin row without changing population.
`camp_admin_append_row` is state scoped and accepts temporary origin state, original authority country, occupation root ID and live amount in thousands; it appends all nine aligned fields and returns `camp_admin_appended_row_id`.
`camp_admin_check_rows` and `camp_admin_count_live_rows` are state scoped and return temporary alignment, authority and live-sum evidence without changing durable state.
`camp_admin_consume_rows` is state scoped and consumes a previously validated amount for death, release or outside removal, optionally restricted by a positive row ID; it changes the matching live amount and cause-specific row record, never physical population.

`camp_admin_preflight_import` is state scoped and reads temporary `camp_admin_import_requested_people` as a positive whole-person amount, `camp_admin_import_origin` as an occupation-registered original state, `camp_admin_import_authority` as the original country, and `camp_admin_import_occupation_root_id` as a positive root ID.
It returns temporary `camp_admin_import_preflight_valid`, `camp_admin_import_preflight_row_id` and a snapshot of inputs and precredit whole-person population.
It requires the package-designated state 88 with an extermination-camp building and operational killing-center role, matching immutable original site authority, direct control, aligned rows, adequate capacity, postcredit population-share headroom, finite uncommitted host population and the maximum receipt limit. The optional Mengele experiment marker is not an import gate.
It performs no durable mutation, population effect, Deaths projection or new event-target save.

`camp_admin_bind_import` is state scoped and must follow an exact measured physical destination credit in the same effect chain.
It checks that the current population minus the preflight population equals the quoted whole-person request, that inputs and next row slot still match, and that the existing live rows still sum to the site aggregate.
It appends one origin-tagged row and increments only `camp_admin_detainees_k` and `camp_admin_total_admitted_k` by the credited survivor amount.
It returns temporary `camp_admin_import_bind_accepted_people`, `camp_admin_import_bound_row_id` and `camp_admin_import_bind_pending_inverse = 1`, then consumes the preflight token.
A repeated bind during that chain preserves the original row and receipt.

`camp_admin_inverse_import_bind` is state scoped and accepts the same-chain bound row ID and still-live request context.
It verifies the returned last row's ID, amount, origin, authority, root and aggregate cover, marks only that row void, subtracts its custody addition, and returns `camp_admin_import_inverse_accepted_people`.
It leaves all physical population unchanged and a repeated inverse returns zero without changing the aggregate.
The implemented occupation caller compares the inverse receipt with its bound amount before performing and checking both physical inverse operations.

The row arrays are `camp_admin_row_ids`, `camp_admin_row_origins`, `camp_admin_row_authorities`, `camp_admin_row_occupation_roots`, `camp_admin_row_amounts_k`, `camp_admin_row_deaths_k`, `camp_admin_row_released_k`, `camp_admin_row_removed_k` and `camp_admin_row_statuses`.
State `camp_admin_row_count` and `camp_admin_next_row_id` guard alignment and monotonic identity.
Statuses are active 1, exhausted 0 and inverse-void -1; rows are retained as history and no array element is removed.
The only new tuning tokens are file-local row-operation/status markers `@CAMP_ADMIN_ROW_RELEASE`, `@CAMP_ADMIN_ROW_OUTSIDE` and `@CAMP_ADMIN_ROW_VOID`; capacity, person conversion, protected floor, share and maximum receipt still use the existing `camp_admin_value` script constants.

## Caller migration and conservation

The parent occupation owner implemented these steps in `camp_occ_transfer_to_custody_exact`: preflight the source row, source physical headroom, direct control and destination control before mutation, then call foundation preflight in the destination state using the regular destination event target.
After one measured source debit and one measured destination credit, the caller binds custody and requires `camp_admin_import_bind_accepted_people` to equal both physical receipts.
Only then does it reduce the source occupation row and `camp_occ_remaining_k`; it appends no destination occupation row.
On postbind failure, it calls custody inverse first, verifies that receipt, then undoes destination credit and restores source debit, setting a sticky rollback-failed flag if an inverse differs.
The dated `camp_occ_try_lodz_auschwitz_transfer` caller invokes that transaction inside the occupation monthly processor after its strict date, authority, site and living-row gates.
No physical movement or source metadata mutation was added by the original foundation patch itself.

Local admissions still use the existing finite, source-proven admission helper, and each accepted local amount appends a separate local row even if imported rows already exist.
The existing monthly death calculation and cause gates are unchanged; an optional `camp_admin_death_row_id` can select one origin row, while a zero selector consumes live rows newest first after one measured state death receipt.
That one receipt still invokes the existing shared Deaths projection once with the immutable site authority and current destination state.
Release, closure and reform consume only live row amounts; neither death nor release changes the stored origin or original authority.

## Validation and limits

`python -m unittest discover -s docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation -p 'test_*.py'` passed 33/33 focused occupation and custody source/model tests, including imported-then-local admission, selected imported death, survivor-only release and idempotent inverse with a local row present.
The source check confirms preflight has no durable mutation and bind/inverse contain no physical-population or Deaths call.
The read-only `hoi4.map_inspect` for states 87 and 88 returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b270ae5e891d5ccb06dc303c1c6ed78fce0844109cac699b5098bf77307d34da/0c230d8cf67c60d639ad255897b32e8a3e6f9319a77af2a5b2409a6413692cf0/map-inspect.1f528671b86e4069.json`.
The map result reports unrelated building-position and port-adjacency diagnostics and truncates their detail; it is source map inspection, not scenario-time control or engine custody receipt evidence.

No engine-backed check has established fixed-point row arithmetic, variable-held state/country comparison, exact `state_population_k` inverse receipts, or live destination behavior.
The occupation adapter and dated caller are wired in source, while their engine receipts, dated control, supported destination capacity and later death attribution remain unverified.
The preflight currently requires the original state to retain `camp_occ_registered`; a future chain that intentionally retires that marker before delivery needs an explicit alternative provenance proof.
Unlabelled outside population losses are allocated newest first because the shared physical ledger does not identify victims by origin; that row attribution is an accounting rule rather than historical proof.
No GUI, localisation, icon, AI weight, world on-action, shared migration, shared Deaths implementation or Chaos Meter source was changed.
No quota or death conversion was added.

## Later two-origin source scenario (2026-09-27)

The original 33-test count above describes this handoff's earlier bounded snapshot; the current full occupation suite passes 63 tests after subsequent administration and transfer changes.
The added `test_two_documented_origins_keep_one_physical_movement_and_distinct_deaths` uses separate Łódź and Kaunas origin/root rows at state 88 under the same original GER authority.
It debits each physical source once, credits the destination once per living movement, records later deaths at state 88 against the two distinct original rows, and releases only the survivors without restoring population.
Its source arithmetic retains `initial source plus destination population = surviving physical population plus the two measured death receipts` and does not allocate an unlabelled outside loss, which remains a pending policy decision.
This is a restricted arithmetic fixture with known row IDs and no engine controller, chronological deportation or in-game receipt proof.

No commit was made from this subagent because the foundation file already had uncommitted edits outside these row changes and the parent is integrating the caller concurrently.
