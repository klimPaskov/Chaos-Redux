# Automatic national policy panel observation

Migration, Famine and Camps use native per-tick scripted GUI evaluation without a `dirty` gate.
Current native getters, action requirements, affordability, enabled controls and tooltips therefore reevaluate at the engine's GUI update cadence.
Effects still own cached lists, selected-state copies, totals and meter frames.
The parent accepted automatic owner notifications plus a bounded hourly open-human observer for those projections within the user's instruction that panels update automatically and have no Update reports button.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `national_policy_panel_has_open_window` | Country, existing panel open flags and existing eligibility predicates | True for an existing human with at least one eligible open window, no writes | Observer request |
| `national_policy_panel_refresh_open` | Actual country, existing published subsystem data and open flags | Refreshes only open eligible panel projections, invalidates an ineligible open panel's UI, no enrollment or gameplay writes | Observer, six immediate native/GUI humanitarian action receivers, old/new controller publication callbacks |
| `national_policy_panel_request_observer` | Actual country, no caller-owned temporary inputs | Reserves at most one pending delivery, records `national_policy_panel_observer_owner`, saves a regular actor event target, queues `national_policy_panel.1` | Both humanitarian openers, actual camp ledger opener, observer continuation |
| `national_policy_panel_observe` | Receiving country, matching pending owner and chain-local actor | Consumes its delivery, refreshes open projections, requests one successor only while an eligible human window remains open | Hidden triggered-only `national_policy_panel.1` |
| `national_policy_panel_observer_is_due` | Country and existing `national_policy_panel_observer_earliest` | True only at or after the reserved delivery hour, no writes | Observer receiver |
| `national_policy_panel_retire_country` | Country at terminal/release boundary | Clears observer flag, owner and earliest date, closes panel flags, clears UI selections and arrays only | Annexed country, camp terminal country close, released-country initialization, inherited identity cleanup |
| `national_policy_panel_reconcile_observer_identity` | Existing country during ordinary initialization | Retires copied observer/UI state when its stored owner is another country, preserves a matching live actor's chain | `national_policy_initialize_country` |

There are no helper parameters, numeric temporary outputs or implicit gameplay defaults.
The observer calls `camp_admin_refresh_interface` and never calls `camp_rework_open_ledger`, `camp_rework_rebuild_display_values`, initialization, reconciliation, registration, maintenance, work advancement or cost payment.
The camp projection now resets seven private foreach break temporaries before their actual loops and initializes the two caller-owned project quote outputs before the quote helper returns.
Its state lists use existing active, civilian and retained-record registries, and its selected-site cache reads only those source records.
Humanitarian projection retains native owned/controlled-state iteration and its existing published-data relevance filters.

## Tuning, target lifecycle and cleanup

`@national_policy_panel_refresh_hours = 1` in `national_policy_panel_effects.txt` is the sole cadence setting.
It is file scoped because the single native event scheduling call is in that file and takes the expanded literal.
No shared constant category, gameplay coefficient, AI weight or probability is added.
Scheduling derives `national_policy_panel_observer_earliest` by dividing that same integer hour count by existing `constant:chaosx_date_units.hours_per_date_unit`, then adding it to `global.date`.
The existing date contract represents one hour as 0.00001, so no rounded fractional-day input or assumed wall-clock timer is used.

`national_policy_panel_observer_actor` is a regular event target that carries through the one country event chain.
There are no global event targets or global registries.
The persistent pending flag and owner pointer reserve an already queued delivery across close/reopen.
Close clears the actual open flag immediately, and the outstanding event consumes its pending fields without refreshing a closed panel or queuing another delivery.
Reopening before that delivery arrives reuses it, while reopening after retirement starts one delivery.
A copied pending flag whose owner is another country cannot suppress a new country's opener, and a receiver whose chain target names another country cannot refresh it.
Eligibility loss closes only affected panel UI at the next owner notification or observer delivery and stops the chain when no eligible window remains.
The native visibility predicate hides an ineligible window independently of that delivery.

Annexation and special-country terminal closure cannot rely on their queued event arriving for a nonexistent country.
The humanitarian annex callback and terminal camp close therefore retire the UI reservation synchronously, while released-country initialization starts from cleared UI state.
Ordinary country initialization discards inherited foreign-owner UI state while preserving a valid same-actor chain.
An old delayed delivery must pass the new reservation's stored earliest hour before it can consume anything.
At the due hour the first valid delivery consumes the slot and stores the next hour, causing any second old/fresh delivery at that same hour to stop without refreshing, clearing or rescheduling.
This follows the existing camp dispatch earliest-date guard and leaves the camp monthly timer unchanged.

Example from an existing opener after its first presentation refresh:

```txt
national_policy_panel_request_observer = yes
```

Example from a synchronous owning publication callback after its transaction and scratch-input cleanup:

```txt
national_policy_panel_refresh_open = yes
```

The publication callback must preserve the actual actor contract.
The six humanitarian bridges perform their refresh after action accounting and input cleanup, while the state-control callback refreshes its documented ROOT new controller and FROM old controller separately.
Existing native law publication, registered-country processing and camp command/display callbacks retain their immediate refresh paths.

## Cadence and validation limits

Cached projections rebuild on opening, current owner publication callbacks and each elapsed game hour while open.
The observer never advances simulation and therefore cannot invent a fresh food assessment or reception-capacity proof ahead of its owner.
Native getters and enablement continue reevaluating while paused, and synchronous native humanitarian actions publish their projected result without waiting for game time.
An arbitrary external edit to a cached source that emits no owner callback is picked up on the next elapsed game hour or opening.
The event clock does not run while paused.
No source inspection establishes a wall-clock frame rate or actual native rendering behavior.

`.tools/test_national_policy_panel_updates.py` executes the actual scheduling guards, event receiver, humanitarian projections and camp cache bodies against a deterministic native event queue with copied event-target envelopes.
It covers quiet opening, close/reopen coalescing, retirement, copied pending ownership, foreign-chain rejection, capture, changing food/migration/capacity data, actual saved-date progress, camp source reads, closed-camp no-op behavior and a paused native action publication path.
Lifecycle cases execute the actual observer retirement and country initialization/release bodies, model canceled delivery on annexation and same-tag re-release, and reject stale early and same-hour deliveries after a fresh reservation.
Camp authority/provenance predicates and existing sale quote consumers are declared fixtures, while projection loops and selected caches execute their production bodies.
Unrelated starting-law profile publication is also a fixture in the observer-only lifecycle model.
The existing panel and action contract fixtures retain separate coverage of action payments, refunds, targets and generations.
No live game, log collection or GUI layout change belongs to this observer package.

No artwork, new visible controls or localisation keys are required.
Future owner publication callbacks should call the existing open-only refresh helper at a transaction boundary rather than add another clock or world scan.
