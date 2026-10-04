# Camp native cleanup repair, 4 October 2026

Disposition: source repair verified; live retest belongs to the orchestrator.
The user explicitly requested these fixes and a shared-tree commit after supplying the live errors.
No agent launched Hearts of Iron IV, requested additional logs or modified shared core accounting.

## Supplied live evidence

- Launch: `Unknown effect-type: clear_temp_variable` in `common/scripted_effects/camp_administration_origin_effects.txt` near lines 292/293 and 353/354 of the launched snapshot.
- Long Fallout run, 2026-10-03 17:00: 64 instances of `remove_dynamic_modifier modifier does not exist: camp_admin_country_economy`, then near `camp_administration_effects.txt:390`.

The current source locations had moved after the supplied snapshot.
The identifiers and their whole caller chains were inventoried before repair.

## Temporary input inventory and repair

| Identifier family | Writers and readers | Repair and observable contract |
| --- | --- | --- |
| `camp_origin_single_reconcile_contract`, `_sequence`, `_amount_k` | Custody `camp_admin_consume_outside_rows` and occupation `camp_occ_distribute_known_origin_removal` stage all three. Only the acknowledgment reads them, requiring contract value one. Callers consume the separate accepted result, not request absence. | Reset contract to zero on both paths. Retained sequence/amount cannot authorize replay; every provider overwrites both before rearming. |
| `camp_origin_known_contract`, observation sequence and four before/after snapshots | Custody death, occupation death and parameterized endpoint observation stage a complete six-value envelope. Only `camp_origin_adjust_known_receipt` reads its inputs, behind contract value one. Continuations read its accepted result and unrelated measurements. | Reset contract to zero on both paths. Retained snapshots cannot authorize an unarmed call or stale sequence; a fresh complete envelope remains usable. |
| `camp_origin_terminal_close_contract` | Explicit country/site terminal adapters stage one before close. Ordinary closes can follow in the same effect chain and require the prior intent to be consumed. | Working-tree terminal integration resets the token to zero. Deleting this cleanup would wrongly permit a later ordinary uncertain close. That newer terminal body is outside the passive repair publication. |
| `camp_admin_origin_projection_host` | Each active/occupation projection iteration writes its current host before the membership reads. No other source reads this identifier. | Its terminal cleanup is deleted in working-tree interface integration. A poisoned retained value is overwritten and cannot change counts. This newer projection body is outside the passive repair publication. |

Temporary absence is not assumed equivalent to zero.
The two receipt APIs use an explicit one/zero authorization sentinel, and their numeric snapshots remain temporary scratch data.
The API documentation describes that contract.
No `clear_temp_variable` is renamed to `clear_variable`.

## Modifier removal

Nonpositive national economic contribution now removes `camp_admin_country_economy` only if the country actually has that dynamic modifier.
Positive contribution still adds it through the existing path.
A present modifier is removed once, repeated absent refreshes are inert and unrelated modifiers are untouched.

## Commit boundary

The origin source, trigger and constant files were untracked at repair start.
Publishing just the effect file would introduce undefined scripted callees and constants.
The [dependency review](commit_boundary_review.md) identified the minimal complete passive definition library: origin effects/triggers/constants, the existing working-tree bodies of `camp_admin_consume_rows`, `camp_admin_consume_outside_rows`, `camp_occ_distribute_known_origin_removal`, two file constants, one row-ID constant and the active/released row-status enum.
Those definitions do not change existing HEAD callbacks.
Only the guarded modifier-removal branch changes an existing callback in this repair publication.
The rest of the older camps integration and other agents' staged/unstaged work remain outside the isolated commit.

## Meaningful verification

Four parsed production-source cases in `source_results.json` cover 64 absent refreshes, one present removal and repeat, consumed/unarmed/stale receipt replay with fresh rearming, terminal intent followed by ordinary close, and retained projection scratch overwrite/deduplication.
The existing source suites passed 24 observer, 16 owner integration, two terminal lifecycle and 35 foundation cases after the cleanup repair.
The test harness no longer treats `clear_temp_variable` as a supported native primitive.
These are working-tree source interpreter checks with native primitives mocked, not a live engine, population or clean-log retest.
The fixture runner and broader integration-dependent tests remain part of the unfinished camps test tranche.

## Required references

- Offline `Data structures - Hearts of Iron 4 Wiki.md`, variable lifetime/unscoped rules 435–443 and operators 555–568, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, read through MCP. `clear_variable` is restricted to regular variables.
- Installed `effects_documentation.md`, `set_temp_variable` 7820–7827 and `remove_dynamic_modifier` 5978–5991, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, read through MCP.
- Installed `triggers_documentation.md`, `has_dynamic_modifier` 3775–3781, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, read through MCP.
- Vanilla `AUS_display_right_communism_spirit`, `AUS_scripted_effects.txt` 271–291, source-lookup revision `eeda58a404cf7c981ad1f97cfd593ffaa6b6f05639ca30c4adb9dd321c46d063`, verifies the structured `has_dynamic_modifier = { modifier = ... }` guard precedent.

Skills applied: the user-invoked temporary-variable cleanup rule from `chaos-redux-debug-playtest`, existing state-ledger guidance and `chaos-redux-shared-git-commit`.
No autonomous live-playtest workflow was started.
The full camps rework remains incomplete at its previously documented GUI/native/historical/AI/restoration gates.
