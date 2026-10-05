# Event 002 refund receipt API handoff

Disposition: implemented within the parent's bounded refund correctness task dated 2026-10-05.
The parent authorized sequence-aware receipt wrappers, caller integration after file freeze, exact existing Political Power refunds, and a bounded actual-source regression fixture.
Historical reversal after a replacement sale and revocation of an awarded achievement remain unsupported, as requested in the task's limitation contract.
The parent owns final review and commit isolation.

## Files and exact ownership

- `common/scripted_effects/026_black_friday_effects.txt`: appended only `black_friday_credit_political_power_purchase_with_receipt` and `black_friday_withdraw_political_power_purchase_with_receipt` beside the existing Political Power API.
- `common/scripted_effects/026_black_friday_simple_cost_api.md`: receipt API table rows, native refundable decision lifecycle, usage examples, and historical/index limits.
- `common/decisions/002_zombie_outbreak_decisions.txt`: only receipt capture, guarded withdrawal, and persistent receipt cleanup in 25 refundable decisions, including 26 refund branches and 25 successful cleanup branches.
- This handoff, `refund_receipt_scenarios_20261005.py`, and the two isolated `.patch` files in this folder.

The source file also contains other agents' changes.
Use `refund_receipt_shared_api_only_20261005.patch` for the reviewed append and API-documentation hunks, and `refund_receipt_002_only_20261005.patch` for the caller hunks.
No staging or commit was performed.
The caller patch's inverse was verified byte-for-byte against the frozen pre-edit SHA256 `5644d3d528ccdc5aed3d65e9feb5e07bf986fa79c25025c44579c0a46b693c40`.
The caller file after this integration has SHA256 `801e222166733aa43d43a523f6d3b950bcc54ebb36ed9539731ad4d47487cdd3`.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- | --- |
| `black_friday_credit_political_power_purchase_with_receipt` | Payer country | Caller initializes temps `black_friday_political_power_receipt_credited` and `black_friday_political_power_receipt_sale_sequence` to zero in the same effect chain. | Temps become 1 and the current sequence only if the targeted committed-family count actually increased. They remain zero otherwise. | Calls unchanged `black_friday_credit_political_power_purchase`, with the existing eligibility and award exclusions. Internal `black_friday_political_power_receipt_before_count` is normalized to zero when the PP-family generation differs from this sale. Writes existing family/count progress only through the existing helper. Each refundable decision selection persists the outputs. |
| `black_friday_withdraw_political_power_purchase_with_receipt` | Payer country | Caller initializes the credited temp to zero, sets it to one from its own credit flag, and loads its own normal sale-sequence variable into the sequence temp. | Both input temps are consumed to zero. | Calls unchanged `black_friday_withdraw_political_power_purchase` only for a positive recorded sequence matching both `global.black_friday_sale_sequence` and the country's `black_friday_achievement_indexed_sale_sequence`. Owners keep their exact currency refund and clear their persistent receipt afterward. |

The helpers do not debit or refund currency.
The owner continues to record the existing native table price in its existing paid-PP variable and refunds exactly that recorded amount.
Boolean persistent proof uses `<decision_id>_sale_credit` country flags, while sequence persistence uses `<decision_id>_sale_sequence` normal country variables.
Each native decision has one active instance per country and its own receipt pair.
The eight counterstrain decisions retain the existing shared paid-amount variable and their existing searching-for-cure exclusivity, while their achievement proof is per decision.

## Call sites and migration

- `develop_weaponized_zombie_infected_counterstrain`.
- `develop_weaponized_zombie_rabid_counterstrain`.
- `develop_weaponized_zombie_parasitic_counterstrain`.
- `develop_weaponized_zombie_mutant_counterstrain`.
- `develop_weaponized_zombie_undead_counterstrain`.
- `develop_weaponized_zombie_necrotic_counterstrain`.
- `develop_weaponized_zombie_demonic_counterstrain`.
- `develop_weaponized_zombie_wendigo_counterstrain`.
- `find_cure_tier_0`.
- `find_cure_tier_1`.
- `find_cure_tier_2`.
- `find_cure_tier_3`.
- `enforce_hygiene_measures`.
- `restrict_migration`.
- `quarantine_protocols`.
- `close_borders_completely`.
- `extreme_martial_law`.
- `revoke_hygiene_measures`.
- `revoke_migration_restrictions`.
- `revoke_quarantine_protocols`.
- `reopen_borders`.
- `revoke_extreme_martial_law`.
- `form_anti_zombie_league`.
- `invest_in_league_research`.
- `disband_anti_zombie_league`.

The research investment's rejected `remove_effect` branch also uses its receipt before refunding.
All successful `remove_effect` paths clear their private receipt without withdrawing the earned credit.
Every refund clears its private flag and sequence, and the existing paid amount is cleared, so repeating the financial path cannot reverse an unrelated purchase or repeat a positive currency refund.
Immediate purchases in Event 002 and other owners keep the existing legacy API.
The two legacy helper definitions remain unchanged for backward compatibility.
There are no new event targets, constants, tuning values, costs, AI weights, icons, localisation keys, periodic hooks, or history ledger.
The receipt uses existing shared zero, one, and Political Power constants.
The only migration is the refundable caller paths listed above.

## Meaningful validation

Executed `python docs/plans/002_zombie_outbreak_plans/subagent_handoffs/refund_receipt_scenarios_20261005.py`.
All five scenario groups passed against the actual source helpers and caller financial blocks.

1. All 25 owners: a same-sale count of three becomes four on selection, returns to three after cancellation, refunds the fixture's recorded 37 PP, consumes the receipt, and a repeated cancellation makes no second positive refund or credit withdrawal.
2. All 25 owners: an outside-sale purchase or an earlier-sale credited purchase followed by a different sale cannot withdraw any of the four current-sale credits when cancelled, while its exact owner currency refund is preserved.
3. All 25 owners under six exclusions each: AI, debug, manual sale, forced sale, already awarded, or unprepared achievement index produces no credit receipt and cannot remove another credit during its refund.
4. All 25 owners: successful completion consumes the private receipt, retains the earned current-sale credit, and makes no currency refund.
5. Research investment: a stale family generation with seven old receipts resets to one on actual credit, records the receipt, and a rejected completion after expiry withdraws that one retained indexed credit and refunds once, including repeated invocation.

The fixture extracts the existing repository Clausewitz parser function without importing unrelated test fixtures.
It executes the actual receipt wrappers, legacy PP helpers, committed-family add/remove, sale eligibility predicates, achievement-family publication, and the financial projection of each actual owner complete/cancel/remove block.
It conservatively drops helper-created temps on helper return unless the caller initialized them, so the caller-output contract is exercised.
Native PP debit is explicitly represented by a fixture balance after a 37 PP charge.
The native PP refund, flags, variables, and arrays are modeled primitives.
Country existence, AI/debug/special identity, and the investment reward eligibility are explicit fixture inputs.
Owner rewards, ideas, scopes unrelated to payments, native timers, engine UI, and live achievement delivery are excluded from the financial projection.
The fixture is source evidence and does not establish native execution or timer behavior.
The byte-verified isolated caller patch additionally proves preservation of the frozen file's unrelated lifecycle and AI hunks.
Both isolated patches passed `git apply --reverse --check` against the current working files, establishing that their hunks precisely identify this worker's changes without staging or changing files.

## Required MCP gap and local references

The connected tool inventory exposed no `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, or `hoi4.script_validate` routes to this worker.
There was no route to call or timeout to retry, and no repo scan, refresh, helper expansion, GUI action, desktop window, or HOI4 launch was performed.
Reference sections were read directly from the local offline wiki and installed game documentation.
Engine/domain evidence through MCP remains blocked by missing tool exposure and is not replaced by the source scenario fixture.
No probability-bearing helper or AI weight was changed, and broader decision AI audit remains the parent's owning workflow.

| Local source | Read line spans | Source revision SHA256 |
| --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 106-122, 436-451, 551-566 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 261 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 4683-4697 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 268-355 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | 1854-1861, 2773-2800, 6730-6738, 7820-7840, 7888-7907 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` | 2110-2133, 5006-5013 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 216-245 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md` | 1-37 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AST.txt` | 55-73 | `aad50da745f5a93c5f7470e06ed990a49a5416c81810849c8a2312600e81f4f2` |

Installed effects/triggers documentation establishes variable writes, comparison syntax, flag and variable cleanup, and their scopes.
The wiki establishes caller-initialized temporary helper output lifetime, variable targeting, normal-variable persistence, native decision cost and timer lifecycle, and scripted-effect call structure.
Vanilla `AST.txt` supplies the bounded cancellation flag-cleanup precedent.
The current Chaos Redux committed-family helpers are the authoritative implementation precedent for generation handling and count reversal.

## Simplifications, omissions, and blockers

The accepted narrow receipt guard was implemented without weakening the existing payment or credit conditions.
No simplifications were made within the authorized receipt guard and caller migration.
Historical progress cannot be reversed after a later sale replaces the indexed generation because the existing storage tracks only the current index.
An awarded achievement remains awarded under the unchanged committed-family helper.
Other owners that still use the unreceipted legacy withdrawal API retain its current-sale behavior and require their own receipt migration if their payments can outlive a sale.
The financial tests do not prove native engine timer execution, award delivery, or country state.
Required MCP inspection and script validation remain blocked by missing route exposure.
No broad ledger redesign, balance target, asset, localisation, or periodic scan was introduced.
Parent review and isolated final commit remain pending.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was changed.
