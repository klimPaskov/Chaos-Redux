# Event 021 dynamic tag capacity

This file documents `021_random_civil_war_dynamic_tag_effects.txt`.

Every ordinary Event 021 claimant is created by vanilla `start_civil_war`, which takes a tag from the shared dynamic pool that vanilla declares in `common/country_tags/zz_dynamic_countries.txt` (D01 to D75).
Other events start civil wars from the same pool, and the offline Country creation reference warns that running out of dynamic countries can crash the game.
Event 021 therefore counts the pool before it plans a new ordinary claimant.
Same-tag contests and Event 006 package carriers use no dynamic tag and are never limited by this guard.
A shortfall trims, defers, or rejects the plan with the existing `cap_reached` skip reason; it never converts an ordinary plan into a same-tag contest.

## Effects

`event021_count_live_dynamic_tags` runs in COUNTRY scope because `meta_trigger` needs a country or state scope.
It walks the declared pool with two bounded `for_loop_effect` passes, D01 to D09 and D10 to D75, and tests each tag with `country_exists` through `meta_trigger`.
It does not use `is_dynamic_country`, whose installed documentation names D01 to D50 while vanilla declares D01 to D75.
Output: `event021_dynamic_tag_live_count`.
The probe variable `event021_dynamic_tag_probe` on the calling country is cleared before return.

`event021_count_free_dynamic_tags` returns `event021_dynamic_tag_free`: the pool size, less the tags in use, the reserve, and tags held for other countries' frozen Fracture Cascade plans in `global.random_civil_war_scenario_reserved_dynamic_tags`.
A country with its own `random_civil_war_scenario_frozen_dynamic_tags` counts that reservation as available to itself.
The result never falls below zero.

`event021_reserve_scenario_dynamic_tags` runs on a country whose Fracture Cascade plan just froze.
It needs one tag for an ordinary primary claimant and one for each frozen ordinary optional row, releases any earlier hold of its own, and either holds the whole need or reports `event021_scenario_dynamic_tags_ready = 0`.
`event021_release_scenario_dynamic_tags` returns a country's held tags.

## Callers

- `event021_parent_validate_opening_plan` rejects an ordinary or regional opening with `cap_reached` when no tag is free; Event 006 and same-tag openings, including a same-tag plan that fails its own remnant check, are unaffected. It reports the shortfall in `event021_dynamic_tag_short`, which the cluster opening caller creates before the call, so a reserved target rejected for tags is not counted a second time as a failed state reservation.
- `event021_parent_collect_dynamic_optional_front_candidates` limits optional ordinary rows to the free tags left after the primary claimant's own tag.
- `event021_parent_freeze_scenario_plan` holds the tags of every frozen ordinary plan, so a Maximum batch cannot plan past the pool; a plan that cannot be covered is skipped and counted by the existing scenario skip counters with `cap_reached` as the last skip reason.
- The scenario controller releases a country's hold right after its commit, resets the batch total at confirmation, and clears it when the batch ends; `event021_parent_clear_scenario_plan_receipt` also releases it on rollback or cleanup.
- `event021_parent_collect_active_front_candidates` limits an Evolution I review's ordinary rows to the free tags, and an exhausted pool defers that source's review instead of closing it.

## Tuning

`event021_dynamic_tags` in `common/script_constants/021_random_civil_war_constants.txt` holds the loop bounds, the declared pool size, and the reserve kept free for other events.
The shared vanilla pool is not extended by Event 021.

## Example

With 60 dynamic tags alive and a reserve of 10, five tags are free.
A host whose plan has one primary claimant and six optional ordinary rows keeps the primary and four optional rows; the other two regions stay with the primary claimant.
