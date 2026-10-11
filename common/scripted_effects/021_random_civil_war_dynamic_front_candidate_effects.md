# Event 021 Dynamic Front Candidate Effects

## Overview

`021_random_civil_war_dynamic_front_candidate_effects.txt` builds and transfers the variable-length optional-front candidate ledger used by the Event 021 opening planner.

The row count comes from currently viable state anchors, admitted complete Event 006 package receipts, the crisis's live front capacity, and the shared remaining front registry.

There are no `secondary`, `secondary_2`, or `event6_secondary` writer slots in the current front-plan builder.

## Helper contracts

`event021_parent_collect_dynamic_optional_front_candidates` runs in the opening host country scope.

In automatic play it reads the committed connected-state candidate array; during Fracture Cascade preflight it reads that country's frozen primary-state array.

It checks viable owned and controlled state anchors, route evidence, primary-anchor protection, complete Event 006 package admission, package uniqueness, existing front reservations, and shared active-front capacity.

It emits aligned temporary arrays for route archetype, route source, anchor state, source-front id, actor/carrier scope, actor type, relationship, objective, Event 006 package id/region/depth/package archetype, state score, route receipt, and selected state scope.

Ordinary anchors are selected in descending live anchor score, and each optional region grows through the highest-scoring currently eligible neighboring states until it reaches the dynamically computed average span for the remaining viable regions and shared front slots.

The region builder checks adjacency while it grows each span, records allocated states in the candidate ledger, and rebuilds its remaining-state pool with those states excluded so ordinary rows cannot overlap.

The valid route list is cycled so multiple regions can use the same supported archetype instead of treating each route type as a one-front slot.

Each ordinary candidate stores a variable-length connected state span and a viable anchor/capital; Event 006 rows retain their package-owned region and force adapter, and their span is the anchor plus every other state the native release hands to the carrier (`021_random_civil_war_event6_footprint_effects.md`).

The candidate collector's ordinary row count is limited by the number of viable anchors, the live severity/territory-derived belligerent capacity, the exact prepared force package, and the remaining front envelope.
It is also limited to the free dynamic civil-war tags left after the primary claimant's own tag, as counted by `event021_count_free_dynamic_tags` in `021_random_civil_war_dynamic_tag_effects.md`.

Ordinary row capacity uses `random_civil_war_requested_force_divisions` and reserves a viable primary force; it does not fall back to the host's raw division count.

Event 006 candidates are limited by complete package receipts and the same global front capacity, not by a named secondary field.

The helper sets `event021_parent_dynamic_optional_front_valid` to one before collection and changes it to zero if any aligned output array has a different row count.

`event021_parent_append_dynamic_ordinary_front_candidate` and `event021_parent_append_dynamic_event6_front_candidate` append one complete aligned candidate row with its exact state receipt; activation marks only the row currently being consumed.

The collector's scratch reset, region growth, and package loop are shared helpers so the Evolution I review of running wars uses the same implementation:

- `event021_parent_reset_dynamic_optional_front_candidates` clears every aligned candidate scratch array.
- `event021_parent_grow_dynamic_ordinary_front_regions` grows the connected ordinary regions from the scored anchor pool. With `event021_parent_dynamic_active_mode` at zero it behaves exactly as the inline opening loop did. With the mode at one, each region's size comes from the remaining `event021_parent_dynamic_region_state_budget` divided by the ordinary slots still open, the budget shrinks by each appended region, growth stops when the budget falls below `constant:event021_active_review.minimum_region_states`, and the rebuilt pool uses `event021_parent_active_source_state_candidate` through `event021_parent_dynamic_region_state_candidate`.
- `event021_parent_collect_dynamic_event6_front_candidates` runs the complete-package finder loop with its cursor, capacity gate, and early finish unchanged.

The opening collector sets the mode to zero before it runs, so its rows are unchanged.
The active collector and its contract are documented in `021_random_civil_war_active_evolution_effects.md`.

### Temporary output ownership

Temporary outputs need storage in their immediate caller before a scripted helper runs.
Every outer caller that consumes forwarded outputs must own that storage as well.
An initialization helper alone cannot establish that ownership because its newly created storage can disappear when it returns.

The public aligned output arrays share the prefix `event021_parent_dynamic_optional_front_` and these 17 suffixes:

```text
archetypes
routes
anchors
sources
actor_scopes
actor_types
relationships
goals
packages
package_regions
package_depths
package_archetypes
state_weights
state_counts
state_offsets
selected_routes
selected_states
```

Initialize these arrays directly with `clear_temp_array` before a fresh collection or replay.
Initialize `event021_parent_dynamic_optional_front_valid` and `event021_parent_dynamic_optional_front_count` to `constant:random_civil_war_value.zero` in each outer caller that consumes them after return.
The row count applies to the first 16 arrays, while `selected_states` is the flat state-span membership.
Existing row, cursor, capacity, source, and active-mode inputs must not be reset when calling an appender or continuing a grow operation.

The opening collector directly creates all 27 arrays named by `event021_parent_reset_dynamic_optional_front_candidates` before that reset call.
Those arrays include the 17 public outputs, optional source states, route types, anchor state/score pools, region source state/score pools, the candidate region, and neighbor state/score/main-index pools.
They remain present through the nested reset, grower, package collector, and appender returns.
The parent-owned active collector must establish the same scratch ownership separately.

| Helper | Scope and inputs | Caller-owned outputs and defaults |
| --- | --- | --- |
| `event021_parent_collect_dynamic_optional_front_candidates` | Opening host COUNTRY, existing primary plan or frozen primary receipt, route evidence and capacity inputs | The 17 aligned arrays start empty, validity and count start at zero |
| `event021_parent_reset_dynamic_optional_front_candidates` | COUNTRY, called only at fresh collection | All 27 scratch arrays must already exist in the collector, reset empties them |
| `event021_parent_grow_dynamic_ordinary_front_regions` | Planning COUNTRY, source-state, route and scored-anchor arrays, current row counts, capacities, active mode and optional state budget | The 17 aligned arrays and existing count/capacity/budget scalars must already exist, preserve their current values |
| `event021_parent_append_dynamic_ordinary_front_candidate` | Selected anchor STATE, current archetype, connected region, weight and source target | The 17 aligned arrays must already exist, preserve prior rows; the grower initializes `event021_dynamic_candidate_state_count` to zero before consuming its returned count |
| `event021_parent_collect_dynamic_event6_front_candidates` | Planning COUNTRY, admitted-package registry, finder bound and optional capacity | The 17 aligned arrays and optional row count must already exist, preserve prior rows |
| `event021_parent_append_dynamic_event6_front_candidate` | Planning COUNTRY, admitted package metadata and selected anchor/carrier targets | The 17 aligned arrays must already exist, preserve prior rows |
| `event021_parent_load_scenario_optional_front_rows` | Receipt owner COUNTRY, frozen optional ledger | The 17 aligned arrays start empty, validity and count start at zero in every caller consuming replay outputs |

The ordinary appender directly initializes `event021_planned_front_route` and `event021_planned_front_goal` to zero before calling the existing source and goal mappers.
Their computed values are copied into the aligned metadata arrays before the appender returns.
Every scorer call in this candidate file directly initializes `event021_anchor_state_score` to zero before consuming the returned score.
The scorer, mapper, tuning, capacity, route evidence, eligibility and selection bodies are unchanged.
No new constant, route limit, event target or persistent cleanup field is introduced by these ownership rules.

Example of an outer caller's scalar preparation:

```text
set_temp_variable = { event021_parent_dynamic_optional_front_valid = constant:random_civil_war_value.zero }
set_temp_variable = { event021_parent_dynamic_optional_front_count = constant:random_civil_war_value.zero }
# Directly clear each of the 17 full array names listed above here.
event021_parent_collect_dynamic_optional_front_candidates = yes
```

The source execution checks live in `.tools/test_event021_candidate_output_lifetime.py`.
They execute the actual collector, grower, appenders and route/goal mapper bodies with separate temporary scalar/array storage and conservative cleanup at every helper return.
They cover four ordinary metadata routes, nested opening forwarding, preservation of prior rows while spending the active state budget, Event 006 metadata forwarding and all candidate-file scorer return boundaries, and an explicitly unowned outer caller.
Adjacency, eligibility, scores, tag capacity and package admission/identity callbacks are declared fixtures rather than engine proof.
The parent opening builder, scenario freezer and frozen-plan applier directly initialize the aligned outputs before collection or replay.
The front builder replays the exact durable frozen receipt at consumption rather than assuming the topology planner forwarded temporary arrays through helper returns.
The active source caller and active collector establish their own aligned and nested scratch storage; those contracts are documented in `021_random_civil_war_active_evolution_effects.md`.
Source execution checks cover these caller prefixes, while native replay admission, complete transaction execution and allocation remain separate evidence requirements.

`event021_parent_freeze_scenario_optional_front_rows` copies the temporary ledger to aligned country-scoped arrays during `chaosx.nr21.19` and reserves each selected optional state, package, and front-capacity share before any scenario opening commits.

The freezer binds the host as `random_civil_war_scenario_receipt_owner` before entering a stored state or actor scope, returns to that country for each persistent array write, and passes the selected scope as `PREV`.

It replays the copied receipt through the same loader before publishing its frozen-plan flag or optional-front reservation; malformed receipts fail the scenario preflight and release their provisional reservations.

`event021_parent_load_scenario_optional_front_rows` restores the exact confirmation-time ledger during the country commit callback and validates every aligned array, the scalar row count, positive contiguous exhaustive spans, distinct state membership, each row's anchor membership, and current state ownership, control, population, and infrastructure.

Frozen span metadata is checked before indexed scope reads; state membership copies use scope iterators so the engine's numeric-loop iteration limit cannot truncate a large region.
Row freezing, replay, span validation, and package-reservation release also traverse their complete arrays with explicit indexes.
The freezer retains the original input validity and requires its copied count to equal the original anchor count before publication, so a self-consistent prefix cannot replace the full receipt.

Ordinary candidate drain uses the immutable optional source-state array as an iteration witness while rebuilding only the separate remaining-anchor and score pools.
Region growth uses its source-state array as a witness, adding at most one neighbor per iteration and rebuilding that source pool only after the selected region finishes.
Package attempts use the complete package-ID registry as a witness, retaining the existing finder cursor, capacity gates, and early-finish behavior.
Witness values do not choose actors or change scores; highest-score selection and source/score alignment remain authoritative.
No iterated array is mutated by its own traversal.
The parent package finder's internal numeric lookup still requires its separately audited traversal repair.

`event021_parent_clear_scenario_optional_front_receipt` releases only the owning country's optional state, package, and front-capacity reservations.

`event021_parent_clear_scenario_legacy_secondary_plan` clears stale receipts from the former fixed scenario representation before collecting the variable-length snapshot.

`event021_parent_clear_dynamic_optional_front_candidate_reservations` clears state markers and temporary package/state reservations when a candidate or whole-plan validation fails before activation.

## Front-plan integration

`event021_parent_build_front_plan` writes the mandatory host remnant and primary rows, then iterates the candidate ledger by index and allocates each optional front id from `global.random_civil_war_next_front_id`.

Ordinary rows derive stockpile, manpower, and force allocations from the immutable region weights and current dynamic force-package receipts.

The optional ordinary division budget scales with the number of viable ordinary rows and the centralized per-front share, is capped by the requested force while reserving a division for the primary actor, and is distributed by remaining region weights; each row's army ratio is recalculated against the source's remaining planned divisions.

Naval and air ratios are inherited from the live force package only when that row's connected state span contains a naval base or airfield.

Event 006 rows carry their complete package metadata and leave the package-owned force allocation to the existing Event 006 adapter.

`event021_parent_activate_planned_optional_front_rows` consumes the validated rows serially after the mandatory host and primary sides are registered, so each row stages only its own source, state, package, and front id before committing or rejecting it.

Optional source ids are the primary opposition front for ordinary nested wars and the host front for Event 006 independence fronts.

## Scenario reservation accounting

The scenario controller reserves each selected country's mandatory front capacity before freezing target plans.

Low, Medium, and High optional candidate rows can spend only the remaining global capacity after mandatory reservations.

Maximum enumerates the complete eligible normal-human roster first, derives mandatory front reservations from each country's live same-tag versus ordinary topology, and builds a temporary cap from those mandatory rows plus normal spare capacity.

That scenario-local envelope leaves `global.random_civil_war_max_active_fronts` unchanged; automatic launches and later optional fronts continue to obey the ordinary stage-specific global cap after scenario cleanup.

The Maximum candidate set applies route, ownership, terminal, successor-grace, external-queue, crisis-load, and bespoke-route gates without using the normal front cap as an eligibility test.

`global.random_civil_war_scenario_reserved_front_count` tracks mandatory and optional front reservations across the confirmation pass, while each country retains the exact amount it owns for cleanup.

Requested, eligible, selected, frozen, and committed country counts remain separate, so a capacity shortfall is not hidden by rewriting the requested count to the number actually selected.

The scenario's ownership and package reservations remain separate from the opening transaction's state reservations and are released on failed preflight, successful consumption, rollback, or scenario-batch cleanup.

## Scope and side effects

Candidate effects run in host country scope, state-scope operations execute on the selected state, and country-scoped frozen arrays persist across the preparation and commit callbacks.

Temporary arrays and variables are transaction scratch only and are not accessed through `ROOT` or `PREV` prefixes.

The candidate helpers do not create a custom tag or character and do not alter Event 006 fired history, weight, cap, evolution, league enrollment, or package ownership.

No icon, picture, portrait, GUI, animation, sound, or 3D asset is consumed by this source file; the owning Event 021 asset manifest remains the source of truth for player-facing assets.

## Reference and validation evidence

The 2026-10-07 lifetime pass successfully searched and read installed `effects_documentation.md:2763-2772` through the connected MCP, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The same task's live wiki read covers `Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, particularly the caller-preinitialized temporary lifetime rule at line 440.
Narrow source lookup located the modified opening collector at index revision `76ac93d5d8e8b7d24d6040ad266df6752504ce0007b68a57be4d7f6889d4d0a4` and returned its first ten source lines, with no override or shadowed definition.
The `clear_temp_array` and `set_temp_variable` initialization snippet returned `SCRIPT_CHECK_PARTIAL`, with syntax, command-kind and declared-scope checks performed, `valid = null`, and the assignment argument block explicitly unchecked.
The installed assignment examples at `effects_documentation.md:7820-7841` were also read locally, so the partial result is not presented as parameter or engine proof.
The current context and narrow `chaosx.nr21.20` lint requests timed out after 600 seconds, so no lifecycle certificate is claimed.
The five source execution test groups pass, and the same tests against commit `545c509bf4531d48ebece6d9c0bfcc4f211d19c0` reproduce four failing groups and seven failure records.
Older pass-specific exposure and availability statements below are retained as historical evidence rather than current tool inventory.

The earlier reference pass timed out for context, targeted search, and line reads after 600 seconds.
The current pass successfully retrieved and read the installed `add_to_array` contract at lines 2278-2292 and the offline array scope/iteration contracts at lines 1069-1077 and 1210-1221 through the live reference routes.
Their revisions are the SHA-256 values recorded below.
The context result omitted Data structures, Effects, Triggers, Scopes, On actions, Localisation, installed trigger documentation, and on-action documentation at its result limit; targeted array/effect reads establish only the coverage named here, while the earlier direct local references retain their separate scope and source evidence.
The focused `hoi4.source_lookup` request for the scenario freezer and the Maximum-cap `hoi4.mechanic_test` request timed out after 600 seconds without artifacts.
The live source-lookup schema does not expose `view` or `keyPath`, and `hoi4.script_validate` is not exposed in this session.

The route inventory contains no HOI4 service health/version or client task-negotiation endpoint, so those service details could not be independently certified.

The offline array reference is `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:1069-1090,1210-1220` (SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`).

The offline scope reference is `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:663-711` and `:737-782` (SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`).

The offline trigger reference is `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:129,1840-1844` (SHA-256 `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06`).

The offline array section documents scope-array iteration and the 1,000-iteration default bound for `while_loop_effect` and `for_loop_effect`; the scenario Maximum roster uses one explicit `every_country` pass, not a periodic world loop.

The installed vanilla effects reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2343-2358,3840-3858,4296-4309` (SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`).

The installed trigger reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2110-2132` (SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`).

The installed script-constant references are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:216-224` (SHA-256 `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7`) and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md:1-15` (SHA-256 `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C`).

Vanilla Finland's dynamic civil-war size precedent is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/finland.txt:7450-7480` (SHA-256 `13E67B2521BEAF8696BC61CFD169ABB0C5A743D6BDA83877D071F1129D57B221`).

The available `hoi4.event_inspect` trace for `chaosx.nr21.1` returns source revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb` and graph hash `65d862ddd1a7893bfede856be54280246099dc7c95c67203da75673e889a9695` even after refresh, so it is stale relative to the edited worktree and is not parser or implementation proof.

No live game was launched; in-game validation belongs to the user.

## Future depth

The opening force package is preflighted against the exact frozen primary region before optional anchors are collected; the immediate scenario transaction recomputes the same package from the unchanged live state and rejects an insufficient or invalid package without selecting replacement anchors.

Extend scenario receipts to freeze exact equipment, manpower, experience, supply, and unit commitments when those values can be snapshotted without duplicating the owning dynamic force-package calculation.

Keep the common global theater/front ceilings and bounded scheduling as the safety limits; do not restore fixed per-crisis secondary-row slots.
