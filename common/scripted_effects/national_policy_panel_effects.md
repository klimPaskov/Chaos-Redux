# Immediate national policy panel publication

Migration, Famine and Camps use native per-tick scripted GUI evaluation without a dirty gate.
Simple selected-state selectors, requirements, affordability and numeric getters read actual scoped source values.
Owner mutations publish cached humanitarian lists and aggregates before returning.
The camp location list and provenance-warning count derive temporary projections from bounded existing registries on each native GUI evaluation, including external population freshness changes that have no camp callback.
The accepted behavior is the user's explicit direction that changes appear immediately, including while paused.
No delayed event or timer is scheduled, and obsolete `national_policy_panel.1` has an empty body.
The publisher dispatches hidden `national_policy_panel.2` without any delay field; this immediately projects within an isolated country event context.

## Helper map and owner contract

| Helper | Scope and inputs | Outputs and side effects | Consumers |
| --- | --- | --- | --- |
| `national_policy_panel_refresh_open` | Actual country, open flags and committed subsystem facts | Synchronously rebuilds eligible open projections; coalesces a request inside a country batch; closed panels have no writes | Owning country actions, publication and lifecycle callbacks |
| `national_policy_panel_publish_state` | Actual state after its transaction commits | Publishes to its actual owner and distinct controller; a regular chain-local owner target deduplicates them | Owning state mutations |
| `national_policy_panel_begin_update` | Actual country before a multi-write transaction | Increments private presentation nesting depth only for an open human viewer | Outer owning transactions |
| `national_policy_panel_end_update` | Same actual country after all outcomes and rollbacks settle | Decrements nesting, clears final depth and synchronously consumes any pending request | Every matching transaction exit |
| `national_policy_panel_project_open` | Actual existing human country in no-delay `national_policy_panel.2` | Rebuilds only open humanitarian/camp projections or closes an ineligible panel; never registers, assesses, reconciles population or advances gameplay | Private publisher implementation |
| `national_policy_panel_reconcile_identity` | Initializing country | Closes presentation copied from another actor; clears obsolete observer fields | Ordinary national-policy initialization |
| `national_policy_panel_retire_country` | Country at removal/release boundary | Clears presentation identity, pending/nesting state, selections, arrays and open flags | Existing terminal and released-country callbacks |
| `national_policy_panel_has_open_window` | Country | Pure open-flag predicate; projection owns eligibility-loss cleanup | Publisher/batch entry |

All helpers are parameterless and have no caller-owned temporary outputs.
The batch depth uses existing `constant:humanitarian_panel.zero/one`; no timing tuning, gameplay constant or weighted selection is added.

A country transaction can coalesce repeated state notifications:

```text
national_policy_panel_begin_update = yes
# Complete authoritative mutations and accounting here.
national_policy_panel_refresh_open = yes
national_policy_panel_end_update = yes
```

A state transaction publishes only after its accepted or rejected outcome has settled:

```text
national_policy_panel_publish_state = yes
```

The owner must explicitly notify an independent receiving country, a former controller, or a responsible authority that is neither current owner nor current controller.
Enter that exact country scope and call `national_policy_panel_refresh_open` after its last mutation.
If both countries are modified in stages, both require their own matching batch boundaries.
The immediate event establishes the receiving country as ROOT and isolates every temporary scalar/array from the owning transaction, including quote, date, cohort-inspection and capacity outputs.
No brittle scratch-variable preservation inventory is maintained.
Never publish from a read-only projection or paint getter: such a cycle violates the API and is stopped by `national_policy_panel_publishing`.
The source publisher does not discover arbitrary external writes and deliberately has no polling fallback.

## Native bindings and derived data

Selected humanitarian condition/status selectors read the selected state's current published flags and variables.
Migration reception capacity checks read current validated country capacity/load.
Invalidating that proof immediately changes the live display to unknown; publication of a fresh proof immediately exposes its value.
The gameplay assessment timing remains unchanged, and paint never recalculates capacity or shortens an action delay.
Numeric display getters live in `common/scripted_localisation/national_policy_panel_numbers.txt` and consume live values or explicit owner-published aggregates.
Famine and Migration work meter frames calculate from current date and published action start/due values in their element trigger, writing only temporary variables consumed by that element's frame property.
The camp economy meter similarly derives its frame from live progress and target.
Institution progress, sorted humanitarian state lists, country aggregates, selected derived causes and quote projections remain owner-published values.
The camp location list uses its own element-trigger temporary array, with matching live empty/selection predicates and direct actual-row selection.
The camp records warning similarly uses a fresh temporary count, preserving current authority and original co-located-host deduplication.
Paint never calls crisis assessment, registration, progression, payments, population accounting or native event scheduling.

Offline `Data structures - Hearts of Iron 4 Wiki.md` lines435-443 revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` states that temporary variables do not carry over into events.
Offline `Event modding - Hearts of Iron 4 Wiki.md` lines192-229 revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` specifies instant firing without delay.
Installed `documentation/effects_documentation.md` lines2943-2967 revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` defines `country_event` and all delay fields as optional; the existing humanitarian action bridges use the same immediate country-context structure.
These references establish the no-delay/temporary-context source contract; paused native event execution has not been observed by this task.

The installed `common/scripted_guis/_documentation.md` lines65-105 revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838` defines dynamic frame variables, dynamic lists and default per-tick updates.
The offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md` lines165-172 and206-248 revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30` explicitly documents element-trigger temporary values consumed by properties, including the trigger-to-property example.
Installed vanilla `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` lines7-82 provides persistent variable frame precedents; no vanilla temporary-frame precedent was located.
Temporary scripted-localisation calculations are documented in offline `Localisation - Hearts of Iron 4 Wiki.md` lines729-792 revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.

## Lifecycle and validation

`national_policy_panel_owner` identifies the actual opener; ordinary close only clears the existing open flag.
Terminal/release retirement removes batch and identity state synchronously.
The only event target is the short-lived state-owner pointer, which expires with the effect chain; no global target or registry is introduced.
The previous observer fields are cleared for migration only and never schedule work.

`.tools/tests/test_national_policy_panel_updates.py` executes the production country/state publishers, nesting guard, projections, selection and retirement at an unchanged date.
Scenarios cover both owner and controller, capture with explicit former-controller notification, nested transactions, idle closed panels, inert obsolete delivery, copied actor identity, and camp projection without work advancement.
The documented native no-delay event boundary is modeled as an immediate receiving-country context with fresh temporary storage and no date change.
Inherited quote, date, provenance and capacity scratch remains intact across publication; native meter arithmetic also reads changed progress at the same date without a publication call.
Its owner/provenance native predicates and quote helpers remain declared fixtures; fixture mutation followed by the actual publisher proves publisher behavior, not coverage of every production writer callback or native rendering.
The parent integration handoff owns the complete writer-to-callback matrix and actual-writer scenarios.
MCP source validation returned partial coverage with unchecked native argument blocks and unknown mixed root scopes; that is not full engine validation.
No live game execution or visual layout change is claimed.
No new artwork, icons or player controls are needed.
Future owner families must publish synchronously at their transaction boundary and retain the closed-panel no-op contract.
