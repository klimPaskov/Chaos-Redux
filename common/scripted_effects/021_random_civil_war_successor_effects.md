# Event 021 successor roster effects

This file documents the reusable effects in `021_random_civil_war_successor_effects.txt`. They are Event 021 transaction helpers for an ordinary same-crisis successor, not generic country-annexing utilities.

## Helper map

`event021_prepare_successor_roster_adoption` runs in the promoted successor country before white peace and annexation.

`event021_adopt_successor_roster` runs in ROOT after FROM has completed `event021_handle_annexed_country`.

`event021_rebuild_successor_roster` is an internal bounded worker called by both public effects.

The matching predicates are `event021_successor_adoption_context_valid`, `event021_successor_adoption_after_annex_valid`, and `event021_successor_roster_actor_valid` in `021_random_civil_war_successor_triggers.txt`.

No localisation, icon, sprite, GUI, sound, portrait, or other asset is introduced by these hidden helpers.

## Before-annex preparation contract

Scope: the ordinary opposition successor in ROOT or the current country scope used by the parent promotion path.

Required caller state: `event021_history_predecessor` must be a regular chain-local event target for the explicit predecessor, and the successor's `random_civil_war_host_country_scope` must point to that target.

The predicate also requires normal human status, a living non-capitulated predecessor and successor, active/government and opposition roles in their expected countries, a non-Event-006 ordinary path, and equal nonmissing `random_civil_war_crisis_id` values.

The predecessor must expose the existing host counters `random_civil_war_total_belligerent_count`, `random_civil_war_belligerent_cap`, and `random_civil_war_route_evidence_count`.

The effect saves chain-local successor, predecessor, and expected-host targets, stores the crisis id in `random_civil_war_successor_adoption_crisis_id`, and sets the two transient pending receipts.

It copies only host operational counters and the existing host multifront role flags. It does not copy or clear Event 006 package identity, origin history, recurrence memory, achievement history, settlement facts, terminal receipts, or war state.

The preparation worker may rebuild the successor's current local actor array from the front ledger, but the predecessor remains the expected host until the annex lifecycle callback runs.

The parent must call this effect after same-crisis successor recognition and before white peace or annexation. The parent must not clear the predecessor's crisis id, host role, front registry, or explicit event target before `on_annex` receives them.

## After-annex adoption contract

Scope: ROOT, the surviving successor, immediately after `FROM = { event021_handle_annexed_country = yes }`.

The after predicate requires the pending receipts and matching successor crisis receipt, the chain-local preparation target, `event021_lifecycle_successor_transfer` equal to one from the current lifecycle call, and `event021_lifecycle_successor` resolving to the current ROOT with the same crisis id. A saved successor target without this current lifecycle witness cannot authorize adoption.

The effect sets the successor active and government roles, clears only its opposition-side and opposition-actor role flags, and points both existing host-scope variables at the successor itself.

It clears an immediate-opponent pointer only when that pointer resolves to the successor itself. It never assigns the successor as its own opponent. The lifecycle helper is responsible for clearing the defeated predecessor pointer and rebinding other surviving actors.

The effect then rebuilds `random_civil_war_opposition_actors` and the existing `random_civil_war_opposition_actor_scope` and `random_civil_war_secondary_actor_scope` pointers from surviving active front rows, records `random_civil_war_successor_roster_count`, saves a chain-local completion target, clears the transient crisis receipt, and clears the two pending receipts.

The successor-side `random_civil_war_successor_side` and `random_civil_war_successor_claimed` receipts remain intact. Event 006 actors may remain in the adopted roster when they pass the live actor predicate; no Event 006 flag, package variable, durable origin marker, or `independence_wave_*` state is copied, cleared, or rewritten here.

If no eligible actor remains, adoption completes with a zero roster count and no opposition actor pointer. The parent must route that state to a deliberate settlement or closure decision and must not start multifront selection from a missing actor scope.

## Front-ledger and role contracts

`global.random_civil_war_front_ids^num` is the authoritative bounded row count.

Every inspected row must have a current actor row in `global.random_civil_war_front_actors`, and that actor's `random_civil_war_front_id` must equal the same-index `global.random_civil_war_front_ids` value. The actor's live crisis id must equal the adoption crisis. When `global.random_civil_war_front_crisis_ids` has a row at the same index, it is an additional aligned witness and must also equal the adoption crisis.

When `global.random_civil_war_front_statuses` has a row at the same index, only `constant:random_civil_war_front_status.active` is unresolved; a missing or short status array is treated as unresolved for compatibility with partially initialized ledgers.

A row is associated with the predecessor before annex when its optional `global.random_civil_war_front_hosts` row, actor `random_civil_war_crisis_host_scope`, or actor `random_civil_war_host_country_scope` identifies the explicit predecessor.

A row is associated with the successor after annex when the same fields identify the successor. The after pass can repair a surviving actor's host pointers to the successor when the lifecycle transferred the row's host evidence but the actor pointer itself was missing.

Actors must be existing normal-human, non-capitulated countries with owned states, active/opposition/actor role flags, the same nonmissing crisis id, and a live registered front id present in `global.random_civil_war_front_ids`. A separate internal-front completion receipt does not exclude an actor when its current front row and role remain active.

The current successor is excluded from its own opposition roster. This is intentional: a winning actor's own surviving ledger row is not another opposition actor. The helper does not unregister or rewrite that row; the parent/front resolver owns any later interpretation or settlement of a successor-actor row.

The roster append is guarded by `is_in_array`, so repeated calls do not duplicate actor rows. The worker clears and rebuilds the successor's local array once per authorized transaction, and the preparation/completion event-target receipts block repeated before/after calls without leaving a recurrence-sticky country flag.

The worker does not modify any aligned global front array, active-theater array, queue, cursor, or global count. `event021_handle_annexed_country` remains the sole lifecycle owner of row removal/rebinding and cursor/count repair.

## Exact parent call sequence

For scripted promotion, the parent must prove an ordinary opposition winner and bind `event021_history_predecessor` to the distinct living same-crisis predecessor before calling `event021_prepare_successor_roster_adoption = yes`.

The parent must call the preparation effect before `white_peace` or `annex_country`, while the predecessor still owns the host role, actor array, and front receipts.

For natural `on_annex`, ROOT must be the ordinary opposition winner and FROM must be the explicit same-crisis government predecessor. The parent recognition helper must run first and must bind the same `event021_history_predecessor` target in the chain before the preparation effect.

The parent then performs any separately proven pre-annex war handling, followed by the existing annex operation. The lifecycle order is `FROM = { event021_handle_annexed_country = yes }` before predecessor cleanup or receipt clearing.

Immediately after that lifecycle call, the parent must call `event021_adopt_successor_roster = yes` in ROOT before any parent-owned role, roster, front, or settlement cleanup can discard the transferred context.

The parent must not treat a successful roster adoption as proof that any real war continues.

## War-continuity precondition

The available vanilla documentation describes `annex_country` and optional `transfer_troops`, but it does not specify that annexation transfers every remaining war relation from FROM to ROOT.

The Event 021 source stores `random_civil_war_external_war_at_opening` as a historical boolean and `random_civil_war_immediate_opponent_scope` as one pointer, not a complete enemy roster.

Therefore actual surviving-front continuity requires a separate parent-owned pre-annex snapshot of every required enemy, an explicit documented `add_to_war` or `declare_war_on` operation in the correct war context, and post-annex `has_war_with` verification for each relation.

No helper in this file declares, joins, ends, white-peaces, or otherwise mutates a war.

## Constants, migration, and future work

No constants were added. Existing `random_civil_war_value.zero`, `random_civil_war_value.one`, and `random_civil_war_front_status.active` values are reused.

No existing gameplay file or call site is edited by this tranche. The parent owns wiring the exact before/after sequence and reconciling any target-name changes before integration.

If an authorized preparation transaction is abandoned before annexation, the parent must clear the two pending receipts and `random_civil_war_successor_adoption_crisis_id`; the regular event targets expire with the chain.

Future work is to certify natural and scripted successor fixtures with one primary front, multiple secondary fronts, invalid/dead/different-crisis actors, a zero-roster outcome, and independent verification of every actual war relation.
