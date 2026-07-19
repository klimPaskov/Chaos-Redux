# Event 006 IW-093 / IW-098 decision effects

## Purpose

`006_independence_wave_iw093_iw098_decision_effects.txt` owns the local paid
decision ledger, project completion, staged-idea lifecycle, and reset cleanup
for the Asante and Sokoto signature categories. It does not create formations,
grant stockpiled equipment, set runtime content attestations, or proclaim a
formable.

## Scope and transaction inputs

All helpers run in country scope. Before calling a `begin_paid_decision_transaction`
helper, the decision sets the package-prefixed temporary cost variables. IW-093
accepts command power, infantry equipment, trains, and convoys; IW-098 also
accepts support equipment. A successful start spends those resources, records
the normal `paid_*` variables, and sets one transaction flag. Closing the
transaction clears its ledger only; it never refunds resources.

## Lifecycle helpers

- `independence_wave_iw093_initialize_decision_content` and its IW-098
  counterpart add the opening staged idea in either prepared or active package
  scope. The owning package setup calls this after its values initialize.
- `independence_wave_iw093_resolve_cocoa_depot_project` and
  `independence_wave_iw093_resolve_kumasi_rail_project` validate state 274,
  then apply the paid reconstruction result or failure.
- `independence_wave_iw098_resolve_caravan_wells_project` and
  `independence_wave_iw098_resolve_livestock_market_project` do the same for
  state 902.
- `independence_wave_iw093_cleanup_decision_content` and
  `independence_wave_iw098_cleanup_decision_content` remove all package
  decisions, flags, ledgers, and staged ideas. The owning package cleanup must
  call them before it clears package setup state.

## Example

An IW-093 decision sets the four `independence_wave_iw093_decision_*_cost`
temporary variables, calls `independence_wave_iw093_begin_paid_decision_transaction`,
and checks `independence_wave_iw093_decision_transaction_result`. Its completion,
failure, and cancellation branches close the same transaction and clear their
active flag.
