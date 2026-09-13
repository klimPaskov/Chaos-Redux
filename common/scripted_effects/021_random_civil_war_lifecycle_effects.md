# Event 021 lifecycle helper contract

This file documents the bounded lifecycle effects in `021_random_civil_war_lifecycle_effects.txt` and the matching front-capacity trigger in `common/scripted_triggers/021_random_civil_war_lifecycle_triggers.txt`.

The helpers have no player-facing text, localisation, icon, sprite, GUI, or asset surface.

## Helper map

`event021_refresh_target_pool_membership` runs in the current country scope after the existing bounded parent review has examined that country.

`event021_handle_annexed_country` runs in the annexed country scope and consumes the vanilla `on_annex` contract in which `ROOT` is the annexer and `FROM` is the disappearing country.

`event021_cleanup_absorbed_event6_adapter` runs in a consenting Event 006 adapter-member country scope before formable absorption and removes only Event 021 adapter bridge state.

`random_civil_war_front_capacity_available` runs as a country trigger for a secondary-front candidate and reads the published global front counter and cap.

The existing parent effects and Event 006 formable registry are the call sites; no existing call site was edited in this change.

## Target-pool membership

The target pool has no country array, so the existing `random_civil_war_target_pool_candidate` flag is the per-country receipt and `global.random_civil_war_live_target_count` is the aggregate count.

The refresh effect first snapshots whether the receipt existed, then reuses `event021_random_civil_war_prepare_target` for normal human countries and clears the weight and receipt for every other country.

A country is a valid member only when it is a normal human country, is registered, appears in `global.random_civil_war_registered_countries`, passes `random_civil_war_country_can_be_automatic_target`, retains the candidate receipt, and has a weight above `constant:random_civil_war_target_weight.minimum`.

The count transition is idempotent because it compares the old receipt with the new validity result.

| Old receipt | New validity | Count transition | Country result |
| --- | --- | --- | --- |
| absent | valid | add one | keep candidate receipt and weight |
| present | valid | no change | keep candidate receipt and weight |
| present | invalid | subtract one when the count is positive | set minimum weight and clear candidate/ready receipts |
| absent | invalid | no change | set minimum weight and clear candidate/ready receipts |

The parent initializer must seed the aggregate count before bounded country transitions begin.

If a save has a missing aggregate count, the helper initializes it to zero and processes only the current country; it deliberately does not scan the world or reconstruct unobserved receipts.

The annex helper applies the same present-receipt transition directly before removing the country, so an annexed or otherwise disappearing candidate cannot keep live target capacity.

## Annex and successor lifecycle

The annex helper removes the current country from the registered-country array, Critical queue, exposed-country array, CXT extension array, and active-theater array using reverse index loops.

The registered, prefire, and Critical cursors are repaired whenever a removed row lies before the cursor, and each cursor wraps to zero when it reaches the surviving array length.

The registered-country and Critical counts are derived from their surviving arrays, and active theater and active front counts are derived from their authoritative surviving arrays.

Front rows use `global.random_civil_war_front_ids` as the authoritative row count and remove or preserve every aligned row at the same index.

The aligned front arrays are `front_ids`, `front_actors`, `front_states`, `front_hosts`, `front_capitals`, `front_generations`, `front_crisis_ids`, `front_archetypes`, `front_route_sources`, `front_package_ids`, `front_region_counts`, `front_goals`, `front_statuses`, `front_settlements`, and `front_registered_dates`.

When a row is removed, the helper clears an actor's `random_civil_war_front_registered` receipt and clears its front id/date only when that actor's stored id equals the removed row id.

The actor's broader Event 021 role flags are not cleared when the row is removed because one actor may still own another crisis-related role or front; the parent-owned role lifecycle remains responsible for that decision.

The helper clears the global priority-front and anchor-state pointers only when their state is the state of a removed row.

The helper clears global host, opposition, launch, exposure, and scenario pointers only when they point at the disappearing country.

### Successor transfer boundary

The vanilla `on_annex` contract is used to distinguish ordinary teardown from an ordinary Event 021 succession.

The helper accepts a surviving transfer only when `ROOT` exists, has `random_civil_war_successor_claimed`, has `random_civil_war_host_country_scope`, and that pointer still identifies the current `FROM` country.

The transfer proof also requires `random_civil_war_crisis_id` on both `ROOT` and `FROM`, with both values nonmissing and equal; a successor flag or host pointer by itself cannot preserve a front from another crisis.

For that exact transaction, a front row whose actor crisis-host pointer or optional `front_hosts` row identifies the disappearing country is rebound to `ROOT` instead of being removed.

Each surviving actor's `random_civil_war_crisis_host_scope` is rebound when it points to `FROM`, and its `random_civil_war_host_country_scope` is rebound only when it also points to `FROM`.

For the successor actor itself, an immediate-opponent pointer to the defeated predecessor is cleared rather than rebound to the successor; this prevents a self-opponent receipt. Other surviving actors rebind an immediate-opponent pointer from `FROM` to `ROOT`.

The optional `front_hosts` row is replaced at the same index, preserving all front metadata and row alignment.

When at least one row is rebound, the old theater row is replaced by `ROOT` in `global.random_civil_war_active_theaters` and `ROOT` receives `random_civil_war_theater_registered`.

The global host pointer is rebound to `ROOT` only when it previously pointed at `FROM` and the same successor proof is present.

The parent promotion sequence must preserve the old host in the successor's `random_civil_war_host_country_scope`, preserve the matching `random_civil_war_crisis_id` on both countries, set `random_civil_war_successor_claimed`, and perform `annex_country` while all three transfer receipts remain available.

The history-only successor helper does not certify front transfer by itself.

If the parent clears the predecessor pointer or successor receipt before annexation, the lifecycle helper intentionally falls back to teardown and cannot infer a safe transfer without risking an unrelated theater.

This is the explicit integration boundary for the parent owner and remains a runtime-sequence validation item.

### War continuity boundary

The source proves that Event 021 can have real Clausewitz war relations: ordinary branches call `start_civil_war`, Event 006 actor paths call `declare_war_on`, and both systems use `has_war_with` before treating a war as present.

The lifecycle helper only rebinds Event 021 scope pointers and aligned registry rows; it does not transfer a war relation.

The available `annex_country` documentation describes annexation and optional troop transfer but does not specify inheritance of the disappearing country's wars by `ROOT`, and the current Event 021 state stores only external-war evidence flags rather than an enemy-country roster.

Therefore surviving-front war continuity is not source-proven by this helper or by `annex_country`; the parent must snapshot each required enemy while the predecessor exists, explicitly use the documented war effect needed for that enemy, and verify `has_war_with` on the successor or surviving actor after the transition.

Without that parent-owned war-transfer step, the helper can preserve script registry continuity while the actual remaining external war relation remains unresolved.

## Event 006 adapter preservation

`event021_cleanup_absorbed_event6_adapter` is guarded by an Event 021 adapter receipt or an adapter setup receipt, calls the bounded lifecycle cleanup, and clears only Event 021 bridge flags plus the two explicit adapter bridge flags.

It does not call `event021_cleanup_crisis` or an Event 006 normal-origin end effect.

It preserves `random_civil_war_event6_identity_ready`, the durable canonical origin receipt `random_civil_war_event6_origin_recorded`, Event 021 package identity variables, Event 021 origin history, all `independence_wave_*` package content, and Event 006 package ids.

`random_civil_war_event6_origin` is different: it marks the currently selected Event 006 actor/front role and is transient lifecycle state, so the annex cleanup intentionally clears it. Clearing that role flag must never be treated as clearing the durable `random_civil_war_event6_origin_recorded` receipt.

The helper does clear Event 021 adapter-preparation, admission-candidate, and completion receipts, which are transient bridge state rather than Event 006 package identity.

## Front capacity trigger

`random_civil_war_front_capacity_available` follows the existing fail-open capacity-initialization contract and returns true when capacity has not yet been initialized or when `global.random_civil_war_active_front_count` is below `global.random_civil_war_max_active_fronts`.

It does not check theater capacity because a secondary front consumes a front slot inside an existing theater, and it has no side effects or weighted choice.

## Constants, migration, and assets

No constants were added or changed.

The effects use the existing `random_civil_war_value.zero`, `random_civil_war_value.one`, and `random_civil_war_target_weight.minimum` values.

The undefined parent calls now resolve by file discovery, while parent-owned typos and hooks remain outside this change.

No localisation, icon, sprite, GUI, or asset wiring is required for these hidden lifecycle helpers.

## Future plans and validation boundary

The parent owner should certify the ordinary successor sequence with one primary front, one or more surviving secondary fronts, a removed old-host registry row, a rehomed active-theater row, and cursor/count assertions before declaring front transfer complete.

That fixture must separately prove actual war continuity for every surviving enemy; registry rebinding and `transfer_troops = yes` are not evidence that an ongoing war relation moved to the successor.

The parent owner should also decide whether any future front metadata array receives writers; if it does, its writer must append every aligned field at the same row index used by this cleanup.

There is no safe world-scan repair for a missing target-count aggregate or a pre-existing misaligned front metadata array, so those states remain explicit migration/repair work rather than inferred behavior.
