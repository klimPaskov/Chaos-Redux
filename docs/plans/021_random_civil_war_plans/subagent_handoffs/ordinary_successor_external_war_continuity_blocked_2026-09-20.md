# Event 021 ordinary-successor external-war continuity investigation

Date: 2026-09-20.

Disposition: **blocked**. The documented HOI4 contract cannot identify a particular predecessor war after annexation or guarantee that a participant joined through `add_to_war` remains in that war when its `targeted_alliance` is immediately annexed. This handoff is the only edit. Gameplay source, constants, and helper documentation remain unchanged. No external-war continuity or Event 021 completion claim is made.

## Accepted task boundary and observed behavior

The current assignment asks for an ordinary successor to continue every surviving external war of its same-crisis predecessor. The Event 021 opposition-victory spec also requires remaining fronts to continue and the Evolution III spec lists foreign obligations among successor inheritances. The accepted task permits a bounded transaction only when the installed effects contract supports the war identity and restoration steps.

`event021_parent_promote_ordinary_successor` in `common/scripted_effects/021_random_civil_war_parent_effects.txt` binds `event021_history_predecessor`, prepares the successor roster, white-peaces the predecessor against the successor, then calls `annex_country` with `transfer_troops = yes`. Natural victory calls `event021_parent_prepare_annex_successor` from `on_civil_war_end_before_annexation`. The `on_annex` callback calls preparation again, then `event021_treaty_rebind_successor`, `event021_handle_annexed_country`, and `event021_adopt_successor_roster`. The latter helpers rebind registry and role receipts. They neither enumerate nor restore external wars. The historical `random_civil_war_external_war_at_opening` receipt is a boolean, while `random_civil_war_immediate_opponent_scope` names only one opponent.

The current source has no pre-annex array of all predecessor enemies, no `add_to_war` between white peace and annexation, and no post-annex per-enemy `has_war_with` check. Troop transfer is documented separately from war membership. No war-transfer behavior is inferred from it.

## Engine-contract blocker

Installed `documentation/effects_documentation.md` documents `every_enemy_country` as a bounded enemy-country iterator, `add_to_war` as joining a specified ally against an enemy through `targeted_alliance`, `enemy`, and optional `single_target_only`, `white_peace` as a country relation effect, and `declare_war_on` as declaring a war. Its `annex_country` entry gives a country target and optional troop transfer but no war-transfer guarantee. Installed `documentation/triggers_documentation.md` documents `has_war_with` as a country relation check and `has_war_together_with` as sharing a side in a war. The installed `common/on_actions/_documentation.md` lists the annex and civil-war callbacks. The offline wiki Effects, Scopes, Data structures, and On actions pages corroborate the iterator, event-target/array lifetimes, and the pre-annex ROOT/FROM callback boundary.

`add_to_war = { targeted_alliance = <surviving ally> enemy = <predecessor enemy> single_target_only = yes }` has documented syntax, but a pairwise check that the ally fights the enemy plus a pairwise check that the ally fights alongside the predecessor does not prove all three countries occupy the same named war. The two relations can be true in different simultaneous wars. Using the predecessor as `targeted_alliance` identifies its current war before annexation, but the docs do not say what happens to the joined successor when that named ally is annexed immediately afterward. `has_war_with` can prove that a country relation exists after the callback, not that the original war, side, participants, or war goals persisted. The documented effects and triggers do not expose a war identifier, war scope, or equivalent unambiguous per-war participant query for this transaction. This is a documentation limit, not a claim that the engine has no internal identity.

Vanilla `common/decisions/SOV.txt` uses `add_to_war = { targeted_alliance = FROM enemy = PREV ... }` for a living civil-war ally. Vanilla `events/AAT_Finland.txt` joins Finland to a living ally's war. Neither precedent annexes `targeted_alliance` immediately afterward. `declare_war_on` would create a separate war with a selected goal and could alter the front or diplomatic context. It cannot be used as an unapproved continuity substitute.

The exact missing contract is the fate of a successor joined to each predecessor war through `add_to_war` when the targeted predecessor is then removed by `annex_country`, including multi-war and multi-front cases. A supported way to identify a surviving co-belligerent in that *same* named war, or an engine-observed fixture that proves the join and post-annex survival for each expected enemy, is needed before a restoration write. A post-annex hostility relation alone is insufficient to certify same-war continuity.

## Proposed helper map after contract proof

These names are proposals only. None was added to source.

| Proposed helper | Scope and inputs | Outputs and side effects | Direct call sites |
| --- | --- | --- | --- |
| `event021_snapshot_successor_enemy_relations` | Ordinary successor with current `event021_history_predecessor`, matching crisis IDs, and the predecessor's live `every_enemy_country` set | Clear and fill a successor-local country-scope `random_civil_war_successor_enemy_scopes` array. Save a matching `random_civil_war_successor_enemy_crisis_id` receipt and pending flag. Include every predecessor enemy except the successor, while marking same-crisis fronts separately from external enemies. No war mutation. | Scripted promotion before white peace, and natural `on_civil_war_end_before_annexation` before engine annexation. |
| `event021_restore_successor_external_wars` | Same proven successor, predecessor, and bounded enemy snapshot, with a documented same-war side witness for each external row | Use only documented `add_to_war` when the exact old war is provable. Do not declare a replacement war. Fail closed for ambiguous or vanished wars. | After snapshot and before scripted annexation, with the corresponding natural pre-annex call. |
| `event021_verify_successor_enemy_relations` | ROOT successor after `event021_handle_annexed_country`, same-crisis snapshot and current lifecycle witness | Test `has_war_with` against each expected living enemy, record missing relations, and distinguish relation proof from same-war proof. No war mutation. | In `on_annex` after lifecycle adoption and before receipt cleanup. |
| `event021_clear_successor_enemy_snapshot` | Successor country with its local pending receipt | Clear the array, crisis receipt, pending flag, and any per-enemy failure receipts. Regular event targets expire with the chain. | Successful verification, failed join, abandoned promotion, rollback, unrelated annexation, and terminal Event 021 cleanup. |

The proposed array stores country scopes through documented `add_to_array` and `for_each_scope_loop` behavior. A regular event target can carry the predecessor through the current effect chain, but cannot represent every enemy or a war. A global target is unnecessary. The `global.random_civil_war_front_*` arrays remain the bounded same-crisis front witness and must not be confused with the complete external enemy set.

## Constants, cleanup, and migration

No numeric constant or tuning table is justified. The transaction is about country and war identity, not balance. No AI weight or probability-bearing helper is involved.

If the missing contract becomes available, add the snapshot directly before the current scripted white peace and in the natural pre-annex callback. Keep the existing preparation, white-peace, annex, treaty, lifecycle, and roster sequence. Restore only external rows whose exact war and hostile side are proven. The existing front ledger continues to own unresolved Event 021 front identity. After annexation, verify every expected living enemy with `has_war_with`, report any missing relation, and clear receipts on both success and failure. Also clear receipts from `event021_parent_rollback_transaction`, the ordinary crisis terminal cleanup path, and the `on_annex` branch for a different winner or crisis. A failed or ambiguous row must not be converted into a new `declare_war_on` call. Check all cleanup callers before adding a persistent array.

The strongest safe partial improvement available from the documented contract is a diagnostic-only pre-annex enemy snapshot with post-annex per-enemy relation checks. It would expose losses but would not restore a particular war. The task explicitly requires gameplay source to remain unchanged if safe restoration is unavailable, so this diagnostic code was not added.

## Evidence and validation limits

- Offline wiki core pages were opened, with relevant Effects, Scopes, On actions, and Data structures passages read. Installed vanilla effects, triggers, script concepts, script constants, and on-action documentation were consulted. Existing `chaosx_dynamic_effects.txt` and its markdown registry have no war-continuity helper.
- Focused read-only `hoi4.event_inspect` trace for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL`, revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44989e109ff80f61136168e361f68438aa18eeb012ca2ed229ace1d39dc74f46/a3389cce9c0e0944e96e15b4d6e77a2d14444f5e09c2efa8bbb9986f0ef7de52/event-trace-a8fde3e58546.json`.
- Focused read-only event lint returned the same revision, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3abab494ac8df3bbbb9e2340c22ccdb315cb3f5f255a00030d340d596cf54304/79da600c686aefa03b2f3274b62b02151db55f314af990a0b5b57e5aaace7ec6/event-lint-a8fde3e58546.json`. Both focused routes reported `helpers = 0` and deferred workspace-wide lifecycle checks. They do not establish helper behavior or runtime war continuity.
- Task-specific lexical checks found balanced script blocks outside strings and comments in the three in-scope gameplay files. The inspected call sites show preparation before scripted white peace and annexation, and the natural pre-annex hook before `on_annex`. No source changed after these checks.
- No `hoi4.event_compare`, probability audit, game launch, live war fixture, or post-edit source parse was performed. There is no gameplay change to compare. The unresolved meaningful fixture is one successor with multiple concurrent external wars and an unresolved same-crisis front, checked both through scripted promotion and natural annexation for exact war participation and every expected `has_war_with` relation.

## Changed files and parent follow-up

Changed file: this handoff only. Implemented helper identifiers: none. New variable, flag, array, or event-target identifiers: none. Constants added or changed: none. Cleanup logic added: none. Gameplay behavior before and after: identical. No simplification or fallback was applied.

The parent should treat external-war continuity as blocked until the same-war and post-annex survival contract is established through supported engine documentation or a reviewed runtime fixture. Then it can authorize the bounded transaction above and reconcile the resulting verification with Event 021's existing front and treaty lifecycle. The parent still owns final integration and any Event 021 completion claim.
