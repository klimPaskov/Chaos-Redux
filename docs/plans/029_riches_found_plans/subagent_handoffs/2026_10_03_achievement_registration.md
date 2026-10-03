# Event 029 achievement registration

Disposition: implemented registry wiring and targeted disqualifier repairs.
Full Event 029 achievement behavior and package acceptance remain unresolved.
The acceptance basis is the user's request for all seven achievements in `029_riches_found_achievement_prompt.md`.

## Implemented registry

The seven exact IDs are registered in the existing single `common/achievements/chaos_redux_achievements.txt` database.
No new database or `unique_id` was created.
Each `happened` block checks player eligibility and the existing route-specific tracking predicate.
Six state-owned routes search only the player's controlled states, including sealed states for the two containment outcomes.
All That Glitters reads the player's controller aggregate predicate.

| Achievement | Tracking predicate |
| --- | --- |
| `029_public_fortune` | `riches_found_achievement_public_fortune_route` |
| `029_claim_jumper` | `riches_found_achievement_claim_jumper_route` |
| `029_the_pay_train_runs` | `riches_found_achievement_pay_train_route` |
| `029_all_that_glitters` | `riches_found_achievement_all_that_glitters_route` |
| `029_no_man_owns_the_mountain` | `riches_found_achievement_gilded_reform_route` |
| `029_close_the_account` | `riches_found_achievement_account_closure_route` |
| `029_the_last_shift` | `riches_found_achievement_last_shift_route` |

Career Profile `_NAME` and `_DESC` keys in `localisation/english/029_riches_found_l_english.yml` reference the existing titles and descriptions.
All 21 completed, grey, and not-eligible DDS files retain their exact registered ID basenames under `gfx/achievements/`.

## Disqualifier repairs

Public Fortune rejects an active exclusive concession and the permanent achievement-specific exclusivity receipt, in addition to the retained older exclusivity-history marker.
Close the Account rejects `riches_found_achievement_account_closure_invalidated`.
The Last Shift rejects `riches_found_achievement_last_shift_invalidated`.
Those two receipts are written by the existing control-change handler, so cycling control cannot restore an invalidated containment verification through the registry.
All That Glitters permits values equal to each aggregate cap and rejects values above those caps.
Equality at a cap is a valid capped contribution, rather than proof of duplicate stacking.

## References and verification

The offline `Achievement modding - Hearts of Iron 4 Wiki.md` coding, icon, and localisation sections were read directly.
They require one custom database identity, `possible` and `happened` predicates, root DDS triplets, and `_NAME` and `_DESC` keys.
Installed vanilla `common/achievements.txt` documents the startup-only `possible` filter and recurring `happened` checks.
Existing Chaos Redux entries supply the custom override-tooltip structure and any-country startup eligibility convention.

A current-source integration check confirmed seven unique registry definitions, all referenced tracking helpers, the 14 Career Profile keys, seven objective tooltips, and all 21 native 64x64 DDS states.
The supplied user-run QA log `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log` contained no Event 029 identifiers at inspection.
That main-menu evidence predates this registry repair and does not establish unlock behavior or route acceptance.

## Shared-tree ownership and remaining work

The root achievement registry and Event 029 localisation file contain other work.
The owned patch in `../evidence/2026_10_03_achievement_owned.patch` contains only the Event 029 registration block and the 14 new localisation aliases.
The separate Event 029 achievement-trigger changes are wholly owned by this repair.
Any commit uses the isolated-index workflow and preserves the other root-registry and localisation changes.

The decision, localisation, completion, and icon audit agents returned `workspace routing discovery timed out`.
Their required final audits are not satisfied by this integration check.
The probability audit also retains unresolved scenario binding and missing compare evidence.
No simplification, placeholder, substitute icon, or extra achievement was introduced by this registration repair.
