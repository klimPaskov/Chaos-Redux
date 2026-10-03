# Event 35 synchronous API scope repair, first tranche

## Disposition

Implemented source changes within the exact-current-country API requirement.
Parent acceptance is based on the original user goal, the country-scope promise in the reusable API spec, and the concrete defects documented by `api_root_context_audit_2026-10-03.md`.
The full coupled repair remains in progress and is not a finished completion plan.
No synchronous API call or public output was replaced by queued delivery.

## Implemented changes

- `great_depression_register_initial_centers` resets its registration-failure scratch at every call, checks direct state children against PREV, and appends their ledgers to the actual actor country.
- State civilian and military baselines are captured before returning to country scope, rather than reading state game variables from a country.
- Owner-country entries use THIS in the returned actor-country block.
- Required centre count is limited to the exact valid state pool, with the existing minimum retained for an empty pool so rejection remains fail-closed.
- `great_depression_initialize_achievement_tracking` freezes centre arrays on the actor through PREV and checks capital control against its immediate country parent.
- `great_depression_store_call_context` requires the supplied source proof, records that exact source directly, and stores an actor-owned normal source-country pointer plus its proof flag.
- `great_depression_register_contagion_candidate` returns to its actual source country through PREV.
- The network target helper has an explicit direct-child source contract and excludes that source through PREV.
- Outgoing multi-source cleanup matches the closing source through PREV.PREV at the documented two-country nesting depth.

## Remaining work and ownership

The architect is implementing only `great_depression_apply_exposure`, its private conversion-frame cleanup helper, and direct callsites under the same original API contract.
That frame must preserve the source country, episode, receipt, row indexes, and propagation depth across nested evolution initialization while retaining public outputs and material-source attribution.
The Event 34 handoff specialist owns collapse snapshot refresh, exact region-pointer retention, receipt-preserving bounded retry, and successful-only snapshot consumption.
The parent retains the inherited-region companion's complete contract, exact precommit state registration, validator identity gaps, centre-score neighbour actor check, final wiring, and validation.

This first-tranche handoff is superseded for current ownership and source status by `inherited_region_contract_repair_2026-10-03.md`, `source_identity_repair_2026-10-03.md`, `transaction_order_and_duration_repair_2026-10-03.md`, and `center_owner_postpatch_accepted_rows_2026-10-03.md`.
The companion is implemented with the complete mapped metadata and receipt/output contract.
The neighbor-owner, first-valid-candidate, and permission-gate repairs have preserved before-source and source-only post comparisons.
Required native comparison and whole-transaction acceptance remain unresolved.

## Verification boundary

The helper transitions were reviewed against the source-linked PREV depths and vanilla precedents in the architect handoff.
The capped state-pool calculation preserves one to three normal centres and the existing Evolution III cap when enough states exist.
These are source relationships, not executed campaign scenarios.
Current domain MCP calls repeatedly terminate after 600 seconds, while artifact resource discovery responds.
Exposure and Event 34 worker handles are live at this tranche boundary and must be resumed instead of duplicated on an observation timeout.

This handoff records the earlier incomplete tranche, not a whole-feature completion claim.
The separate availability repair is committed as `37c6b472a9cb44c54fcea9214309fdf87facf00d`, and its five real-index entries are reconciled.
