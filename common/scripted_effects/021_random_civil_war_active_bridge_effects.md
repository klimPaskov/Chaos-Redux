# Event 021 active transaction bridge

This documents the two effects in `021_random_civil_war_active_bridge_effects.txt`.
They preserve serial global scratch borrowed by an Evolution I active-front commit across ordinary and Event 006 secondary adapter work.
Integration is parent-owned.
The refreshed source shows the existing active commit wrappers calling these effects at the boundaries below.
The parent's narrow active-row cleanup and wider transaction validation remain separate work.
The bounded retry prompt of 2026-10-07 authorizes these helpers and source tests, and explicitly reserves existing active and parent source files to the parent.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects | Intended call site |
| --- | --- | --- | --- | --- | --- |
| `event021_parent_save_active_transaction_bridge` | COUNTRY, reviewing government | Current presence and values of the 30 global scalars, seven global targets, eight global flags below | Normal country copies and country flag `event021_active_transaction_bridge_saved` | Clears this helper's old private copies before capturing the current frame, leaves borrowed globals unchanged | Parent-owned `event021_parent_save_active_commit_bridge` wrapper, before outer commit guards and target overwrites |
| `event021_parent_restore_active_transaction_bridge` | COUNTRY, same government | Its saved normal variables and country flags | Exact saved global presence/value/pointer and flag presence | Clears absent-at-save globals and consumes every private copy after restoration, no action without the saved-frame flag | Parent-owned `event021_parent_restore_active_commit_bridge` wrapper, after all rows and adapter cleanup |

Invoke both with `= yes`.
There are no named parameter blocks, `$FIELD$` substitutions, temporary outputs, dynamic dispatch, or helper-created event targets.
Native field identifiers below are the API contract.
The private normal-variable existence represents original scalar or target presence, including a scalar whose value is zero.
Private country flags represent original global flag presence.
Restore on another country, or a second restore after consumption, is a no-op.
Save replaces an earlier frame on the same country, so this is one synchronous frame per government and not a nested stack.
The caller must prevent nested commits and restore before releasing that protection.

## Scalar coverage

Every public scalar below has the prefix `global.random_civil_war_`.
Every private copy has the prefix `event021_active_transaction_value_` followed by the identical suffix.

| Public suffixes | Destructive or overwriting closure |
| --- | --- |
| `pending_generation`, `pending_severity`, `pending_crisis_id`, `pending_archetype`, `pending_opposition_front_id` | Outer commit, ordinary row generation, Event 006 secondary adapter identity publication |
| `pending_opening_size`, `pending_army_ratio`, `pending_navy_ratio`, `pending_air_ratio` | Broad `event021_parent_clear_pending_force_transaction`, retained in this snapshot even after the parent's active guard protects primary force inputs |
| `pending_secondary_front_id`, `pending_secondary_anchor_state_id` | Active row publication, secondary loader, ordinary rejection and preplanned cleanup |
| `pending_secondary_opening_size`, `pending_secondary_opening_state_count`, `pending_secondary_army_ratio`, `pending_secondary_navy_ratio`, `pending_secondary_air_ratio` | Active loader and validator, starter, broad force cleanup |
| `pending_secondary_archetype`, `pending_secondary_front_goal` | Active loader, ordinary initializer, rejection and preplanned cleanup |
| `planned_secondary_archetype`, `planned_secondary_front_goal` | Preplanned cleanup, legacy opening inputs retained for an outer transaction |
| `event6_pending_package_id`, `event6_pending_region`, `event6_pending_depth`, `event6_pending_archetype`, `event6_pending_opening_state_count` | Event 006 secondary publication and `event021_parent_clear_event6_package_transaction` |
| `pending_event6_secondary_front_id`, `event6_secondary_planned_package_id`, `event6_secondary_planned_region`, `event6_secondary_planned_depth`, `event6_secondary_planned_archetype` | Active Event 006 row staging and package cleanup |

## Target and flag coverage

Public targets and flags in this table have the prefix `random_civil_war_`.
Private target variables have the prefix `event021_active_transaction_target_` and private flag mirrors use `event021_active_transaction_flag_`.

| Target suffix | Native pointed scope | Closure |
| --- | --- | --- |
| `global_host_country` | COUNTRY | Outer active commit |
| `secondary_anchor_state` | STATE | Ordinary active loader, success, rejection and preplanned cleanup |
| `secondary_source_country` | COUNTRY | Ordinary active row, success and rejection |
| `preplanned_secondary_anchor_state` | STATE | Broad preplanned cleanup, retained for compatibility after parent narrows active cleanup |
| `event6_secondary_planned_anchor` | STATE | Active Event 006 row staging and package cleanup |
| `event6_secondary_planned_actor` | COUNTRY | Active Event 006 row staging and package cleanup |
| `active_front_commit_owner` | COUNTRY | Outer active commit owner publication and cleanup |

| Flag suffix | Closure |
| --- | --- |
| `secondary_front_pending`, `secondary_route_prepared`, `secondary_front_preplanned` | Ordinary row, initializer, rejection and preplanned cleanup |
| `event6_secondary_search_active`, `event6_secondary_front_pending`, `event6_secondary_front_preplanned` | Event 006 secondary staging and package cleanup |
| `dynamic_front_activation_active`, `active_front_commit_in_progress` | Outer synchronous commit recursion guard and lock |

Pointer copies are read as normal variables and restored with `var:<private_copy> = { save_global_event_target_as = <public_name> }`.
They preserve the native object reference without replacing it with ROOT, PREV, a new target, or an inferred live country.
Dormant country pointers are preserved too.
This assumes the pointer still identifies a native object after the synchronous transaction and that these seven names have no chain-local target shadow.
The source inspection found no regular `save_event_target_as` declarations for these seven names in `common/` or `events/`.
The native `has_event_target` trigger checks both regular and global targets, so a future regular alias using one of these names would violate this API.
Flag restoration covers presence only, as requested.
Flag dates, values and durations are not copied, so only plain serial guards belong here.

## Constants and durable outputs

No constants or tuning tables are added or changed because the bridge performs identity copies and boolean presence restoration without arithmetic.
Existing Event 006 fired history, weights, caps, evolution delivery and league membership are untouched.
Durable front IDs, registry arrays and row statuses, capacity counts, next-ID counters, actor memberships, priority-front publication and logs must retain committed results.
In particular, `global.random_civil_war_next_front_id`, `random_civil_war_priority_front_state` and `random_civil_war_priority_front_active` are outside this snapshot.
The Event 006 host identity save/restore effects remain responsible for country-local package identity.
No icons, localisation, GUI, decisions or focus surfaces are introduced.

## Parent migration contract

1. Replace the bodies of the old `event021_parent_save_active_commit_bridge` and `event021_parent_restore_active_commit_bridge` with boolean calls to the corresponding new helpers.
2. Call save on the reviewing government before setting `random_civil_war_active_front_commit_in_progress` or `random_civil_war_dynamic_front_activation_active`, and before saving `random_civil_war_active_front_commit_owner` or overwriting host and identity globals.
3. Keep the commit lock and recursion guard active across every row, all native child callbacks, and every cleanup return.
4. Release the transaction's own owner target, dynamic guard and lock after all adapter cleanup, then call restore once on the same government as the last global-restoration step.
5. Keep all unconditional clearing before restore because clearing afterward would destroy restored presence.
6. Retain the parent's active guard around broad primary force cleanup and its narrow replacement of active-row preplanned cleanup.
7. Review the object and row mutations below before claiming full transaction isolation.

The private copies are cleaned at save entry and after successful restoration.
No asynchronous event may depend on the temporary serial globals after this restore.
No global snapshot target requires its own cleanup because the snapshot is stored entirely on the country.
If a transaction exits without restoration, the caller must repair that control path rather than silently discard its frame.

Example parent boundary:

```txt
# COUNTRY scope, after rejecting a nested commit but before overwriting guards.
event021_parent_save_active_commit_bridge = yes
set_global_flag = random_civil_war_active_front_commit_in_progress
set_global_flag = random_civil_war_dynamic_front_activation_active
save_global_event_target_as = random_civil_war_active_front_commit_owner
# Existing synchronous row execution and cleanup.
clear_global_event_target = random_civil_war_active_front_commit_owner
clr_global_flag = random_civil_war_dynamic_front_activation_active
# Keep the active lock until the bridge restores its original flag last.
event021_parent_restore_active_commit_bridge = yes
```

## Destructive effects that require parent review

`event021_parent_clear_preplanned_secondary_opening` enters the old preplanned STATE target and clears `random_civil_war_secondary_transfer_state`.
Restoring its target cannot restore the deleted state flag.
Active rows use `event021_parent_clear_active_secondary_pending`, not this broad preplanned cleanup.
The live-remnant gate rejects a preexisting transfer marker before marking a row; the final native gate permits only the already verified current row markers.
The active marker cleanup still clears its complete owned row across current holders after success or rollback.

`event021_parent_clear_event6_package_transaction` enters regular `random_civil_war_event6_selected_actor` whenever that target is present and deletes that actor's adapter setup flag and previous-generation copy.
The active row calls this cleanup before loading its new selection.
A target left by an earlier transaction must not mutate an unrelated actor even though the globals are later restored.
The parent cleanup now requires the current selection owner, its actor-validity flag, and matching positive owner/actor package IDs before deleting actor setup scratch.
Regular selection owner, selected actor, selected anchor and previous capital targets cannot be cleared with `clear_global_event_target`.
They require their existing validity flags, exact ownership checks and deliberate rebinding before use.

`event021_bind_front_plan_row` routes an active commit first, before any ready global opening plan.
`event021_reject_pending_front_plan_row` likewise rejects only the active owner's row while the lock is held.
An absent active owner fails closed instead of falling back to the outer plan.
These durable row mutations are deliberately not undone by the bridge; routing fixtures cover an outer row with the same ID and the no-owner case.
Legacy second-secondary activation, cleanup and recursion are guarded by `NOT = { has_global_flag = random_civil_war_dynamic_front_activation_active }` and must remain excluded during an active commit.
Refreshed source and branch-selection tests establish active-first precedence in `event021_parent_load_planned_secondary_front`, `event021_parent_copy_planned_front_state_span`, `event021_parent_copy_opening_state_receipts` and `event021_parent_validate_secondary_transfer_receipt` with borrowed secondary preplanned/route flags and a ready outer plan present.
Those four branch checks complement the separate actual-source binding/rejection fixtures in `.tools/tests/test_event021_active_row_routing.py`.

The current parsed native Event 006 release crosswalk contains 32 carrier branches; the earlier excerpt count of 29 was incomplete.
Native release transfers every owned carrier core state, including uncontrolled states, and removes source cores, while the current active package receipt freezes one anchor with count one.
The planner owns the complete release-footprint correction.
This metadata bridge does not change that registry, state selection, core behavior or receipt size, and must not be interpreted as certification of an anchor-only release contract.

`missiles_preflight_country_split` aborts/cleans a source's live missile operation and marks sites as pending split before the native civil war.
That system uses ROOT in some source/state accounting, which requires particular care when an active row's source differs from the reviewing government.
The bridge cannot undo missile bookkeeping, native state transfers, new-country creation, annexation, capital restoration or Event 006 package setup.
These are separate owner validations, not missing scalar snapshot entries.

## Evidence and limits

`python -B .tools/tests/test_event021_active_bridge.py` executes the saved/restored source and the current parent cleanup effects against separate global, country, temporary and array stores.
The nine-test suite covers 24 ordinary/Event 006 success/rejection fixture combinations, absent/present/zero scalars, mixed flag and target presence, country and state pointers including dormant countries, untouched same-name country variables, durable publication, repeated restore, wrong-country restore, stale private-copy replacement and conservative helper-return cleanup.
It also executes the parent wrappers and checks their ordering, plus the four active-first helper branches with borrowed legacy flags present.
It also verifies borrowed-marker preservation and actor cleanup only for matching current owner/package receipts through the actual cleanup source.
Adapter overwrites and durable publication are declared fixture inputs.
The suite does not execute `start_civil_war`, Event 006 dispatch, ownership changes, native callbacks or live timing.

The connected MCP reference, event inspection, source lookup and script validation routes answered.
The focused Event 021 trace reports `EVENT_INSPECTED_PARTIAL`, `analysisMode = focused`, `counts.helpers = 0`, so it is not closure coverage.
Whole-file script validation reports `SCRIPT_CHECK_PARTIAL`, `valid = null`, 455 checked commands, 67 unchecked native argument blocks and two roots with unknown inferred scope.
COUNTRY-scoped snippet checks additionally establish the requested declared scope but retain unchecked variable argument blocks.
No engine validation or full Event 021 completion is claimed.
Exact source revisions, citations, MCP artifact URI and integration limits are recorded in the accompanying handoff.

Future work is limited to completing parent wiring and proving the same closure after those owner edits.
A general transaction router, parameter wrapper or shared skill is unnecessary for this bounded contract.
