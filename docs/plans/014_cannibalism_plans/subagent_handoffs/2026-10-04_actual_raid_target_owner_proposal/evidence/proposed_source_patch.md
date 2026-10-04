# Proposed Event 014 raid-target source patch

Status: parent accepted and queued; this file is not Clausewitz source and this subagent made no runtime source change.

The source owner may be editing the assigned runtime files in the shared tree; this proposal continues to describe the captured prepatch snapshot and does not review those in-progress contents.

## Recommended bounded change

Keep `cannibalism_march_raid_supply_depot` and its existing category, focus unlock, icon, Larder payment, command-power payment, 30-day native re-enable value, base modifier duration, duration bonuses, and AI formula.

Make this existing decision state-targeted with the native `state_target = yes` and `on_map_mode = map_and_decisions_view` pattern already used by `cannibalism_raise_bone_guard` in `common/decisions/014_cannibalism_decisions.txt:2297-2316`.

Add one state-scoped trigger, provisionally named `cannibalism_warlord_march_raid_target_is_valid`, for a live, passable supply-node state whose owner and controller are countries at war with `ROOT`, with at least one neighboring passable state controlled by `ROOT`.

Require exactly one supply node in that state with `building_count_trigger = { supply_node < 2 }` plus `supply_node > 0`, and require `non_damaged_building_level = { building = supply_node level = 1 }`.

The vanilla building definition limits each province to one supply node, but a state can contain several such provinces; the uniqueness gate makes the state-scoped effect's documented first-match lookup unambiguous and prevents charging for a fully damaged sole node.

States with multiple supply nodes remain ineligible under this state-target contract; supporting them requires an accepted and verified exact-province target path, with no random or scored province choice.

The native decision selects a state, not a province, so persist the selected stable state and report the state-level target/result. Do not guess or score a province, claim a province-specific selection, or add an unverified province-target decision interface.

Use the existing state decision's target trigger to select only those states, repeat the target predicate in `available`, and recheck it in `cannibalism_begin_march_supply_raid_operation` before any payment.

Add `march_raid_supply_node_damage = 0.50` to the existing fixed-point `cannibalism_warlord_decision` constants group.

On a valid target, apply `damage_building = { type = supply_node damage = constant:cannibalism_warlord_decision.march_raid_supply_node_damage }` in the exact target-state scope, then start the current country-scoped March Supply Raid Operation and its existing route recovery contract.

Return an explicit transaction result to the decision wrapper and display the success effect tooltip only after the strike succeeds; a stale target or refunded failure must not show the success text or publish a success receipt.

The parent has selected `0.50` as the damage amount in building damage units; the installed effect documentation identifies the parameter as a float but does not define it as a percentage.

The vanilla supply-node definition has no `value` health field, so do not call `0.50` "50% health" unless a primary source establishes the omitted field's default.

The target-specific building damage is the actual raid outcome, while the existing country dynamic modifier remains preparation and campaign support.

Do not describe the result as a seized depot or recovered supplies; the source effect damages the selected state's supply node.

Do not add a mission, second cost, population or equipment payment, native raid type, GUI button, map rewrite, global event target, periodic hook, or target-weight table for this immediate operation.

## Target receipt and owner boundaries

Extend the accepted Event 014 GUI data owner with a transaction writer provisionally named `cannibalism_ui_record_march_raid_target` and the existing proposed reader `GetCannibalismUiRaidTarget`.

Publish a receipt only after the supply-node effect and existing operation setup succeed; retain the stable target state, target kind `march_supply_raid`, result `supply_node_damaged`, date, the `ROOT` actor generation, and the controller's current country generation when the controller is a registered Event 014 actor.

Keep the receipt owner-scoped and generation-checked; do not use a single global target or the view-only `cannibalism_command_gui_selected_raid_state` proposed in the 2026-10-03 Data API plan.

Render the card as the last committed target and result, with the exact action kind; show an empty record only before a real operation has succeeded.

On target-owner generation mismatch, preserve the historical state name and result while suppressing the recycled country's current identity.

Clear the command receipt on the existing Warlord slot or actor-generation reset, and preserve the previous successful receipt when a new attempt aborts before payment or is refunded.

The UI worker owns only the layout of the accepted card in `cannibalism_warlord_command_window`; the parent or designated data owner owns the receipt source and getter contract.

## Atomicity and costs

Use `cannibalism_warlord_can_pay_march_operation_cost` as the existing authoritative affordability predicate and `cannibalism_pay_warlord_operation_cost` once, after the target and actor generations pass their completion-time checks.

Keep the current Larder amount, command-power amount, command-power gate, duration, re-enable duration, and AI block unchanged.

If the target fails a completion-time recheck before payment, do not charge, grant the preparation modifier, grant route recoveries, or replace the prior success receipt.

If the target unexpectedly fails after a debit, return the exact Larder and command-power amounts from the same stored quote and suppress every success-only effect and receipt; test whether the native decision cooldown still applies to that aborted click and report that engine behavior separately.

Preserve the existing two displayed spendable types and their icons; the Larder texticon and command-power texticon are present, while the repeated literal `Larder` label should be removed from the inline cost string without changing payment.

Keep `days_re_enable = constant:cannibalism_warlord_decision.long_reenable_days` as the sole operation cooldown.

Use a transaction-in-progress flag around the single debit, damage, receipt, and modifier block; clear it on both success and refund so a reentrant duplicate returns before payment without extending the accepted cooldown to the full preparation duration.

## AI and source application gate

Preserve the exact current `ai_will_do` base and war modifier; use the same state target predicate for player and AI selection.

Do not add a target score or change the parent-selected damage amount in this proposal.

Before any source edit, let the designated probability auditor capture the complete current source and candidate-pool baseline, including fixtures for no target, one unique damageable hub, a multiple-hub state, a fully damaged sole hub, recycled Event 014 controller generation, and the existing resource boundaries where the connected schema supports them.

After an owner-applied patch, run `hoi4.probability_compare` through `chaosx_ai_probability_auditor` with the exact before source and the same named scenario set; do not compare the source to itself.

The targeted-decision pool must be reported as incomplete if the available scenario adapter cannot supply or enumerate its real state candidates.
