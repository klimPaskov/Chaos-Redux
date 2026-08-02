# Event 012 host-transfer lifecycle handoff

## Scope

This handoff closes the ordinary-host-annexation lifecycle gap identified by the Event 012 completion audit.
It does not claim full Event 012 acceptance, live-save validation, or completion of the requested visual and model matrix.

## Changed surfaces

- `common/script_constants/012_africa_constants.txt` adds the review and designation political-power costs and the one-candidate threshold.
- `common/scripted_triggers/012_africa_host_transfer_triggers.txt` defines pending, designatable-candidate, staged-candidate, selected-successor, designated-successor, and resolver-open gates.
- `common/scripted_effects/012_africa_host_transfer_effects.txt` stages the host ledger and bounded arrays, cancels action callbacks, transfers one successor, or preserves a suspended crisis docket.
- `common/on_actions/012_africa_world_order_on_actions.txt` calls the staging bridge before the annexed host disappears.
- `common/decisions/categories/012_africa_categories.txt` exposes the host succession category both for pre-annex designation and post-annex congress review.
- `common/decisions/012_africa_decisions.txt` adds the targeted designation and successor-commit decisions.
- `events/012_african_union.txt` adds the resolver, suspended-host, and successor-notice events `chaosx.nr12.230`, `chaosx.nr12.231`, and `chaosx.nr12.232`.
- `common/script_constants/012_africa_event_log_constants.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, and `localisation/english/012_africa_event_log_l_english.yml` add dedicated succession and suspended-host history rows.
- `docs/events/012_africa/overview.md` and `docs/events/012_africa/charter_autonomy_and_focus_ai.md` record the lifecycle and its remaining boundary.

## Runtime contract

The on-annex bridge treats `ROOT` as the annexer and `FROM` as the still-existing victim.
It stages only when `FROM` is the committed Event 12 host and no prior successor transaction has been consumed.
The old host's relationship roster is the only candidate source; no opinion scan or generic tag is created.

Before the old country is removed, active action records and peace-exemption missions are closed through their existing cleanup owners, the old Charter subject statuses are released, the scalar campaign ledger is copied into global staging, and bounded relationship, dossier, project, warning, congress, and world-package arrays are copied into staging arrays.
The staging snapshot contains the old host generation, so delayed callbacks and action responses cannot mutate the new host through a stale generation receipt.

A host-side designation is optional and costs political power.
When it exists, the designated member receives the staged ledger during the same on-annex chain while `africa_previous_host` still points to the old country, allowing completed continental focuses to be copied before the old scope disappears.

Without a designation, the annexer receives `chaosx.nr12.230`.
One valid recorded candidate is committed explicitly by the sole-candidate option.
Several valid candidates open the targeted Host Succession Congress and require a paid decision selecting one exact candidate.
An empty pool or an explicit unresolved option enters `africa_host_transfer_suspended`, records `host_succession_suspended`, and leaves the staged docket intact.

The successful successor path retargets the global `africa_host`, restores the origin host id and playbook, increments the host and action generations once, rebuilds all copied rosters on the successor, removes the successor from its old member arrays, adds it to the host action target array, updates every surviving member generation, reapplies the existing autonomy helper, reconciles capacity caps, refreshes the focus layout, records `host_succession`, clears staging, and fires the successor notice.
The one-use guard `africa_host_successor_consumed` prevents a second automatic transfer.

## Validation evidence

The focused Event Inspector lint was run against `chaosx.nr12.230` with helper expansion and returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics.
Static review confirmed one on-annex callsite, one-use successor guard, dedicated event ids, localized resolver options, BOM-preserved localisation, and no new country or cosmetic tags.

## Remaining risks and live proofs

- The staged post-annex congress cannot copy completed focus state from a country that has already been removed, so it reloads the continental tree and marks `africa_host_focus_completion_transfer_deferred`.
- The resolver and targeted decision need a live annexation scenario with one candidate, several candidates, and no candidates.
- A live scenario must verify action cleanup, peace-exemption mission cleanup, autonomy reapplication, event-log actor rendering, and the one-use generation invalidation.
- Suspended staging intentionally remains resident; a later constitutional recovery surface is not part of this tranche and must not silently clear it.
