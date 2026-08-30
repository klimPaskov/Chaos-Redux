# Germany Mengele Black Friday adapter handoff

Status: the bounded source adapter is complete for the four reachable Germany Mengele custom-cost decisions, but final tranche acceptance remains blocked and must stay blocked until the required GUI and probability evidence routes are available.

## Scope and disposition

Owner scope is the Germany Mengele clone-army decision category and its directly referenced owner triggers, effects, and English localisation.

Covered custom-cost rows are `raise_clone_infantry_wave`, `raise_clone_assault_wave`, `raise_clone_guard_wave`, and `activate_continental_assault_protocols` in `common/decisions/germany_mengele_decisions.txt` at the current decision callsites beginning on lines 450, 481, 512, and 566.

Rejected custom-cost rows: none of the four reachable custom-cost rows were rejected from the source adapter.

Out of scope: every other Germany Mengele decision row remains unchanged, including ordinary `cost =` rows that are not custom-cost actions; no shared Event 26 or universal framework file was edited.

## Exact adapter actions and callsites

The four decision `custom_cost_trigger` fields call `mengele_clone_army_black_friday_has_clone_deployment_command_power` or `mengele_clone_black_friday_has_continental_assault_command_power` in `common/decisions/germany_mengele_decisions.txt`.

The four decision `custom_cost_text` fields call `mengele_clone_black_friday_clone_deployment_command_power_cost` or `mengele_clone_black_friday_continental_assault_command_power_cost`.

Each decision `complete_effect` calls exactly one hidden payment wrapper and releases its original gameplay effect or timed idea only when `mengele_clone_black_friday_payment_success` equals the shared success constant.

The clone-wave wrappers call `mengele_clone_army_set_clone_deployment_command_power_cost`, capture `mengele_clone_deployment_command_power_spend`, and then call `mengele_clone_army_black_friday_pay_command_power`.

The continental wrapper captures `constant:mengele_clone_decision.continental_assault_command_power` and then calls `mengele_clone_army_black_friday_pay_command_power`.

The shared adapter call sequence in `common/scripted_effects/germany_mengele_effects.txt:586` is `black_friday_allocate_owner_transaction`, `universal_cost_quote_integer`, `universal_cost_check_quote_affordable`, `universal_cost_pay_component`, `universal_cost_record_transaction`, `universal_cost_settle_transaction`, and `black_friday_record_achievement_transaction`, with `universal_cost_refund_transaction` on record or settlement failure.

The normal-price branch performs one direct negative command-power adjustment using the captured ordinary cost and then allows the original action to run.

## Component and family mapping

Every covered action has exactly one command-power component, `constant:black_friday_event.owner_component_command_power`, with resource kind `constant:universal_cost_resource_kind.command_power` and resource id `constant:universal_cost_framework.zero`.

Every receipt records `constant:universal_cost_family.command_power` as the primary component and family, with one owner transaction id allocated by `black_friday_allocate_owner_transaction`.

The actual paid amount is the same quoted amount passed to `universal_cost_pay_component` and recorded in `universal_cost_transaction_actual_paid_cost` before settlement.

## Cost examples

The three clone-wave rows use the existing ordinary cost selection and preserve its flag precedence: ordinary 25, discounted 20, and streamlined 15 command power.

At a 50 percent Black Friday quote, those three ordinary costs become 13, 10, and 8 command power respectively.

At a 75 percent Black Friday quote, those three ordinary costs become 7, 5, and 4 command power respectively.

The continental assault row remains ordinary 75 command power, becomes 38 at 50 percent, and becomes 19 at 75 percent.

The manpower, infantry-equipment, clone-equipment, division-spawn, reserve-refresh, and timed-idea effects are not discounted or otherwise altered.

All displayed spendable costs use the command-power texticon through the six owner localisation keys added at `localisation/english/germany_mengele_l_english.yml:289-294`.

## Lifecycle, preservation, and cognitive load

The existing category `mengele_clone_army_category` remains the sole category, and no scripted GUI, tab, mission, or new visible action was introduced.

The four rows retain their existing visibility, availability, route flags, target scope, action limits, re-enable constants, idea gate, timed duration, and AI base values.

The category has four covered primary actions in this tranche, and each presents one icon-first dynamic command-power value rather than a raw multi-resource value dump.

The displayed quote is recomputed from the current ordinary cost and the shared sale ratio, while route and cooldown requirements remain separate decision requirements.

No owner mission or timed-objective surface exists for these rows, so mission owner, category, region, requirement, duration, success, failure, and duplicate-risk fields are not applicable.

## AI and route-lock notes

The AI candidates remain exactly one per decision, using the existing `constant:mengele_clone_decision_ai.raise_clone_infantry_wave` or `constant:mengele_clone_decision_ai.activate_continental_assault_protocols` base.

No AI weight, target, route flag, or cooldown was introduced or changed, and no `ai_hint_pp_cost` was added for these command-power custom costs.

The adapter checks the active Black Friday source before applying a sale quote and falls back to the ordinary path when the source is inactive.

The ordinary fallback affordability checks were corrected from strict `>` to inclusive `NOT = { command_power < ... }` for the three clone-wave tiers and the continental cost.

## Cleanup, settlement, and exploit audit

The payment helper starts with failure status, allocates one transaction, debits at most once, records the actual payment, and settles the receipt before exposing the gameplay effect.

If transaction recording or settlement fails after payment, the helper calls the shared refund path and leaves the gameplay effect gated off.

No new persistent flag, event target, mission, action loop, equipment grant, war goal, core, or cooldown bypass was added.

The existing decision cooldowns remain the only re-enable protection for the covered actions.

## Changed files

- `common/decisions/germany_mengele_decisions.txt` wires the four custom-cost rows to the owner payment wrappers and gates the original effects on successful payment.
- `common/scripted_triggers/germany_mengele_triggers.txt` adds the exact ordinary-cost quote triggers, active-source affordability checks, and inclusive ordinary fallback checks.
- `common/scripted_effects/germany_mengele_effects.txt` adds the command-power quote, pay, receipt, settlement, and refund adapter wrappers.
- `localisation/english/germany_mengele_l_english.yml` adds the clone-deployment and continental-assault cost, blocked-cost, and tooltip keys.
- `docs/plans/026_black_friday_plans/subagent_handoffs/germany_mengele_adapter.md` records this handoff.

`common/script_constants/germany_mengele_constants.txt` exists and was not changed because the owner already provides the ordinary tier and cooldown constants and the universal identifiers are shared inputs.

## Validation and blockers

Focused source review confirmed one custom-cost trigger, one custom-cost text key, one payment wrapper, one success gate, one original action, and one AI candidate for each of the four covered decision ids.

Focused reference checks confirmed every newly called helper and every new localisation key is defined, and the English localisation file is UTF-8 with BOM.

The source diff was limited to the Germany Mengele owner files and this handoff; no shared Event 26 or universal framework file was part of the adapter patch.

Required GUI evidence is blocked because `mcp__hoi4_agent_tools__hoi4_gui_inspect` returned `MCP tool hoi4_agent_tools/hoi4.gui_inspect is not available to the model`, `hoi4.gui_render` was unavailable as `tools.mcp__hoi4_agent_tools__hoi4_gui_render is not a function`, and no production render or click-region proof exists.

Required weighted-AI evidence is blocked because `hoi4.probability_inspect` was unavailable as `tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`, so no `chaosx_ai_probability_auditor` baseline or comparison can be claimed.

Live gameplay proof was not run because the repository instructions prohibit agents from launching Hearts of Iron IV and the request explicitly excludes live proof.

Final disposition: source changes are coherent and ready for parent review, but the tranche must remain blocked for final acceptance until the mandatory GUI inspect/render and probability evidence routes can run.
