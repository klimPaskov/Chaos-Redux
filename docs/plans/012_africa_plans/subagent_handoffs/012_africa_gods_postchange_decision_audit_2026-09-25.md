# Event 012 Gods Protection / Event 013 Neighbor Relief — Post-change Decision Audit

**Date:** 2026-09-25
**Disposition:** The bounded source/localisation tranche is implemented in the reviewed source, with the unresolved presentation and evidence limits below. This is implementation evidence, not additional user acceptance. Overall Event 012 completion remains unresolved and is not claimed here.

## User-fixed decisions

- Gods of Africa belongs to Event 012 / Africa Is One; Event 070 remains unassigned.
- Event 012 protection keeps its Arms Against Tyranny-gated market-access service and gated enemy intelligence, and Event 013 Relief Convoy remains a separate Foreign Disaster Relief choice.
- The four-spendable-type cap applies to Event 012 protection only. Its shared reserve decrement mirrors the same infantry-equipment shipment and is ledger bookkeeping, not another spendable type. The optional one-time convoy-or-train transfer is the possible fourth type.
- Event 013 neighbor relief keeps its existing full price and penalties. This audit makes no cost, penalty, or balance change recommendation for Event 013.

## Scope and identifiers reviewed

Reviewed source files: `common/decisions/012_africa_gods_decisions.txt`, `common/scripted_triggers/012_africa_gods_triggers.txt`, `common/scripted_effects/012_africa_gods_effects.txt`, `common/script_constants/012_africa_gods_constants.txt`, `localisation/english/012_africa_gods_l_english.yml`, `common/decisions/013_natural_disasters_decisions.txt`, `common/scripted_triggers/013_natural_disasters_triggers.txt`, `common/scripted_effects/013_natural_disasters_effects.txt`, `common/script_constants/013_natural_disasters_constants.txt`, `localisation/english/013_natural_disasters_l_english.yml`, `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`, and `common/ideas/013_natural_disasters_ideas.txt`.

Reconciled prior handoffs: `012_africa_gods_decision_feedback_reaudit_2026-09-25.md`, `012_africa_gods_event013_inbound_relief_route_gate_reaudit_2026-09-25.md`, `012_africa_gods_completion_audit_2026-09-25.md`, `012_africa_gods_protection_architecture_2026-09-25.md`, `012_africa_gods_ai_probability_baseline_2026-09-25.md`, and `012_africa_gods_ai_probability_compare_2026-09-25.md` under `docs/plans/012_africa_plans/subagent_handoffs/`.

Exact decision, helper, mission, constant, and localisation identifiers in scope include:

- Event 012 decision `gods_of_africa_protect_partner`; triggers `gods_of_africa_participant_can_receive_protection`, `gods_of_africa_host_can_fund_protection`, and `gods_of_africa_protection_package_is_affordable`; effects `gods_of_africa_protect_partner`, `gods_of_africa_deliver_protection_transport`, `gods_of_africa_rebuild_protected_partner_capital`, `gods_of_africa_grant_owned_protection_relations`, and `gods_of_africa_share_enemy_intelligence`.
- Event 013 decision `natural_disaster_offer_neighbor_convoy_relief`; trigger `natural_disaster_can_offer_neighbor_relief`; effects `natural_disaster_pay_neighbor_relief`, `natural_disaster_offer_neighbor_relief_for_gods_of_africa`, and `natural_disaster_clear_gods_of_africa_neighbor_relief_receipt`.
- Route decision `natural_disaster_route_inbound_relief`; trigger `natural_disaster_can_route_inbound_relief`; route/card helpers `natural_disaster_set_inbound_relief_route_from_state`, `natural_disaster_state_has_recovery_card`, and `natural_disaster_select_priority_open_card`; mission `natural_disaster_inbound_relief_mission`.
- Event 012 tuning keys are under `gods_of_africa_transaction` and `gods_of_africa_protection`; Event 013 payment, gate, fixed-penalty, and duration values are under `natural_disaster_cost`, `natural_disaster_cost_gate`, `natural_disaster_cost_fixed`, and `natural_disaster_aftermath`.
- Event 012 localization keys: `gods_of_africa_protect_partner_desc`, `gods_of_africa_protect_partner_effect_tt`, `gods_of_africa_protection_cost`, `gods_of_africa_protection_cost_blocked`, and `gods_of_africa_protection_cost_tooltip`.
- Event 013 localization keys: `natural_disaster_cost_neighbor_relief`, `natural_disaster_cost_neighbor_relief_blocked`, `natural_disaster_cost_neighbor_relief_tooltip`, `natural_disaster_cost_inbound_relief_routed`, `natural_disaster_cost_inbound_relief_routed_blocked`, `natural_disaster_cost_inbound_relief_routed_tooltip`, and the route-specific `natural_disaster_cost_inbound_relief_rail*` / `natural_disaster_cost_inbound_relief_convoy*` keys. Dynamic keys `GetNaturalDisasterInboundReliefRoutedCost` and `GetNaturalDisasterInboundReliefRoutedCostBlocked` select the persisted route's cost row.

## Findings by severity

### P2 — Conditional Event 012 transport payment is missing texticons and one dynamic amount

`gods_of_africa_protect_partner_effect_tt` in `localisation/english/012_africa_gods_l_english.yml` says “20-unit convoy or train” without either resource texticon and hardcodes `20` although the source amount is `constant:gods_of_africa_transaction.transport_amount`. `gods_of_africa_protection_cost_tooltip` uses the dynamic amount but still describes “convoy or train” without icons. The compact `gods_of_africa_protection_cost` row correctly shows the three base values with icons, but the conditional fourth spendable shipment is explained only in prose.

Recommended bounded localization follow-up: in both tooltips, use the dynamic transport amount and the matching convoy/train texticons, while retaining the three-value inline base row and the current “at most one”/convoy-priority behavior. The relevant identifiers are `gods_of_africa_protect_partner_effect_tt`, `gods_of_africa_protection_cost_tooltip`, and `gods_of_africa_transaction.transport_amount`; do not change the mechanic or price.

### P2 — Blocked-cost colors do not identify the actual blocker

`gods_of_africa_protection_cost_blocked` is identical to the normal Event 012 cost row and colors every value yellow. A blocked decision may be unaffordable because of infantry equipment, fuel, political power, or the non-spendable reserve-ledger requirement, but the row does not identify which condition failed.

`natural_disaster_cost_neighbor_relief_blocked` colors all five Event 013 material costs red when the combined `natural_disaster_can_offer_neighbor_relief` trigger fails. That trigger also checks Stability, War Support, and the outbound-relief lock, so a non-material blocker can make all five material values appear unaffordable. Preserve the five costs and penalties; if this presentation is refined, separate non-material requirement feedback from the material-cost blocked state rather than repricing or hiding any Event 013 value.

### P2 — Event 012 target-array density can exceed the six-action review threshold

`gods_of_africa_protect_partner` targets `gods_of_africa_participants`, while `gods_of_africa_value.max_participants` permits 64 registered participants. Current generation, registration, reliability, peace, defiance, host, and cooldown checks filter the target set, but the decision itself has no six-row display cap or phase limit. Source therefore permits more than six simultaneous target actions; the actual eligible count and rendered density were not measurable in this audit. Parent review should keep this as an unresolved density risk, not visual acceptance. If the live list exceeds six primary actions, the participant presentation needs a bounded/phase-aware treatment within the existing category rather than another button-warehouse category.

### P3 — Event 012 protection effect tooltip remains dense

`gods_of_africa_protect_partner_effect_tt` compresses several focus-dependent services, DLC gates, cooldowns, and the separate Event 013 choice into one long paragraph. Its key amounts and cooldowns are mostly dynamic and the service causes/consequences are stated, but a player must scan a dense block to distinguish sanctuary, security, logistics, relief, and expedition benefits. A later copy-only refinement could separate the conditional services into shorter, clearly gated statements without changing effects.

### P3 — Routed-relief cost explanation uses prose resource names

The route-specific inline rows selected by `GetNaturalDisasterInboundReliefRoutedCost` and `GetNaturalDisasterInboundReliefRoutedCostBlocked` use icons for manpower, exactly one of trains/convoys, and fuel. However, `natural_disaster_cost_inbound_relief_routed_tooltip` describes those spendables as “manpower, fuel” and “rail or convoy route” in prose. If that explanation is treated as cost text, add the matching texticons and keep Stability/War Support clearly separated as penalties; the inline route rows themselves have texticon coverage.

No current source-level target, affordability, payment-order, or route-lock defect was found in the bounded paths reviewed. This does not resolve the presentation findings or substitute for runtime evidence.

## Confirmed current behavior and lifecycle

### Event 012 protection

`gods_of_africa_protect_partner` is an Event 012 participant-targeted decision. The host root must be valid and at least one of the seven protection-service focus flags must be unlocked. The selected `FROM` country must exist, be a current registered reliable participant, not be defiant, be at peace with the host, and have reached its protection due day. Availability composes this participant gate with the host affordability helper; the custom-cost trigger checks the same host funding gate, and the effect rechecks the composed package helper before payment.

The base host payment is 500 infantry equipment, 500 fuel, and 10 political power. The host also requires `africa_common_defence_stockpile >= 500`, then subtracts 500 from that ledger while removing the same 500 infantry equipment from its physical stockpile; the source comment explicitly identifies the ledger as a mirror of the same shipment. The recipient receives the 500 infantry equipment and 500 fuel. Thus each execution has three base spendable types plus at most one conditional transport type, not a second infantry charge for the ledger.

With the logistics-support focus, the effect checks whether the recipient is short of 20 convoys and whether the host retains more than its configured floor plus 20; if so it sends 20 convoys. Otherwise, it may send 20 trains under the same shortage/floor test. The `if`/`else_if` ordering means at most one is sent and convoys take priority when both branches qualify. The floor is 40. No transport is sent without the focus and a qualifying recipient shortage/host stockpile.

The accepted DLC services are gated in source: market access requires Arms Against Tyranny, peace, no existing access, and the sanctuary focus; enemy intelligence requires La Résistance, agencies in both countries, an active African war, and eligible current non-capitulated enemies the recipient is not fighting. Guarantee, military access, reception capacity, stability/War Support, and capital rebuilding are also behind their respective service-focus and state checks. The repeat interval is 180 days, reduced to 120 days by the Continental Reserve focus.

### Event 013 neighbor relief and inbound route

`natural_disaster_offer_neighbor_convoy_relief` targets the current global relief-recipient array. The target must exist, differ from the donor, not be at war with it, satisfy the neighbor/faction/subject route or the major-country same-continent route, have an open aftermath and an actionable controlled recovery card, and have no active inbound relief. Root availability and the custom-cost trigger use `natural_disaster_can_offer_neighbor_relief`; click completion repeats donor/recipient/route/card checks.

Both the generic path and the Event 012 protected-participant adapter select an open actionable recovery card before donor payment or inbound flags. The selector excludes chain-only and unresolved-territory cards, applies the neighbor-convoy variant, and records a selected state. Only a successful selection invokes `natural_disaster_pay_neighbor_relief` and then sets inbound state/route flags and activates the mission. A rejected preflight or empty card selection does not charge the donor or establish inbound state.

The Event 013 donor price remains its existing five material costs: 5,000 manpower, 300 support equipment, 200 trucks, 20 convoys, and 5,000 fuel. It also applies the existing 1% Stability loss, 1% War Support loss, and 45-day light construction burden. `git diff` review found no changes to the Event 013 neighbor-price values in the constants/payment/localization paths reviewed, and the current payment helper still debits those five values. The user-fixed exception applies; this report does not propose reducing, hiding, or waiving them.

The recipient's separate `natural_disaster_route_inbound_relief` decision has its own route-specific payment: manpower, fuel, and exactly one of trains or convoys, plus Stability and War Support penalties. `natural_disaster_can_route_inbound_relief` requires the persisted route to be exclusive (not both route flags), checks the matching transport stockpile and the other route costs, and is called from both decision availability and completion before debits or `natural_disaster_inbound_relief_route_secured` is set. Route-specific dynamic localization selects the same rail/convoy type that completion charges.

| Mission field | Current source behavior |
|---|---|
| Owner | Controller of the selected recipient recovery state, where `natural_disaster_inbound_relief_state` is stored. |
| Category | `natural_disaster_aftermath_category`. |
| Region | The exact selected, controlled recovery-card state; the selector excludes chain-only and unresolved-territory cards. |
| Requirement | `natural_disaster_route_inbound_relief` must secure the recorded route while the selected state still has an open card; its helper rechecks route exclusivity and affordability at availability and completion. |
| Duration | 45 days via `constant:natural_disaster_aftermath.foreign_relief_days`. |
| Success | The mission is nonselectable and becomes available when the route is secured and the card remains open, so its success effect runs after the player takes the separate route decision. It records arrival, applies the capacity/dependency effects, updates the disaster phase score/card, clears inbound state and the donor receipt, and schedules capacity refill. |
| Failure | Timeout records misdirection/partial phase, degrades the card, applies the existing Stability and War Support losses, clears inbound/receipt state, and schedules refill. Explicit refusal records refusal and removes the mission. |
| Duplicate risk | One inbound package per recipient is enforced by `natural_disaster_inbound_relief_active`; donor outbound relief is locked by the timed light-burden idea, whose `on_remove` clears the outbound lock. Recovery-state transfer also removes the matching mission and clears the flags, variables, and receipt. |

## Cognitive load, costs, AI, and cleanup

- Event 012 visible actions are one target-array instance per currently eligible participant, with a source ceiling of 64 registered participants. The actual current count is unknown. Event 013 neighbor relief similarly creates one target decision per eligible registered recipient; this audit did not establish its runtime count. No ordinary decision-panel render was available to verify the visible row count or spacing.
- This tranche adds one nonselectable inbound-relief mission per recipient, paired with a separate actionable route decision. The mission has explicit route success, 45-day timeout failure, refusal, cancel, and state-transfer cleanup hooks in source. Runtime activation, daily mission evaluation, timeout, and cleanup were not exercised in-game.
- Event 012 values have clear source meaning: shipment amounts, the matching reserve ledger requirement/decrement, transport floor/amount, intelligence amount, and cooldown are constants. The reserve ledger is a requirement/bookkeeping mirror, not a player-spendable fourth/fifth base resource. Tooltip density and optional transport icon gaps remain as listed above.
- Event 013 neighbor relief visibly lists five material costs with corresponding manpower, support equipment, motorized equipment, convoy, and fuel texticons. The penalties and timed burden are described separately. Its five-type price is intentionally preserved by the user-fixed scope.
- The inbound route row displays manpower, the selected train-or-convoy route, and fuel with texticons; Stability and War Support are non-material penalties. The route explanation's prose naming is a remaining localization clarity point, not a source/payment mismatch.
- `gods_of_africa_protect_partner` remains at `ai_will_do = { base = 1 }`. `natural_disaster_offer_neighbor_convoy_relief` retains its low base with existing faction, opinion, dense-population, and strategic-transport modifiers. The route/refusal decision weights are unchanged in this tranche; the nonselectable mission has no independent AI score. No invalid or dead target branch was found in the reviewed target gates.
- Cooldown, recipient-generation checks, host funding recheck, recipient inbound lock, donor outbound burden lock, route rechecks, mission outcomes, receipt clearing, and state-transfer cleanup reduce repeat/duplicate and stale-target risks. No free shipment, cost bypass, or repeat-without-payment path was identified in these bounded source paths.

## Reconciliation with earlier findings

- The earlier inbound-route affordability finding is superseded for current source: `natural_disaster_can_route_inbound_relief` is now checked at both availability and completion, with the selected route and matching transport revalidated before debit/secured-route state.
- The earlier convoy-priority wording gap is superseded: the current Event 012 effect and cost tooltips state that convoys take priority when both shortages qualify. The optional transport texticon and dynamic-amount issues above remain.
- The earlier claim that the Event 012 blocked row colored all values red is stale: current normal and blocked rows are identical yellow values. The current problem is that blocked affordability is not visually distinguished or attributed to its failed resource/reserve condition.
- Base Event 012 cost texticons are now present for all three base costs. The optional conditional transport is still named without texticons in the explanatory strings.
- The previous Event 013 four-type-cap conflict is superseded by the user-fixed exception; the current five-material-cost price and existing penalties are preserved.
- The architecture handoff's `implemented` disposition applies only to the bounded protection source tranche. The prior completion handoff still leaves overall Event 012 completion unresolved; this audit does not promote it.

## Probability and visual MCP evidence limits

No decision or mission weights changed in the current source/localisation tranche, and no probability improvement is inferred. The existing `chaosx_ai_probability_auditor` baseline/compare handoffs remain the relevant weighted-logic evidence: they report score-only evaluation, unresolved target-instance/scenario factors, no normalized click probability, and no valid `hoi4.probability_compare` result. The prior compare attempt returned `INTERNAL_ERROR`; its retry was rejected for an unsupported `revision` field. Useful existing artifact references are the prior handoffs plus `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f46e2d88734b194475bd3421e8b6c17dc485c745cf8b7f82d08566ad6818a2e9/7cc625b47ab4445479516e874c6904b828ff04304a28313185ac9f29c8f16ec8/probability-inspect-9be313f99014.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03105e4ce91f141825720c133940365442c25020cc2534b1f5a02edeccc3b084/fbd20a083e4c570f28d2c6510288ec439d419eec3de1cfd4036892f71428fad7/probability-a929594c41056ec0ade7c0ec.json`.

A fresh `chaosx_ai_probability_auditor` delegation was attempted for this audit but could not start because the agent service returned `collab spawn failed: agent thread limit reached`. No additional MCP call was made after that failure. The prior auditor handoffs are retained with their explicit incomplete scenario/compare limits; they are not treated as proof of normalized odds or a before/after probability improvement.

There is no exposed ordinary decision-panel renderer for these stock decision rows. The mandatory scripted-GUI inspect/render workflow does not provide a one-to-one ordinary decision-panel view, so no `hoi4.gui_inspect`/`hoi4.gui_render` visual acceptance is claimed. The GUI limitation is specifically the absence of an ordinary decision-panel route; it does not imply a scripted GUI was in scope. No live game was launched, no log search was performed, and no runtime mission lifecycle claim is made.

## Validation performed and limits

- Read-only source review covered the target/availability/custom-cost/payment ordering, custom-cost debit effects, Event 013 card preflight/selector ordering, exact route-helper calls, dynamic route localization, mission owner and lifecycle hooks, constants, and player-facing cost text.
- Reconciled current source with the six dated Event 012 handoffs listed above. Offline `Decision modding` wiki material was used for custom-cost and nonselectable-mission semantics, alongside relevant vanilla decision and effects/triggers documentation.
- A read-only diff check found no edits to the Event 013 neighbor-relief price constants/payment/localization values reviewed. No gameplay, localization, or other documentation files were edited; only this handoff is created.
- No live-game test, log search, decision-panel visual render, or fresh probability comparison was performed. The probability and visual evidence limits above remain open.

## Remaining issues and recommended next checks

1. Fix Event 012 optional convoy/train tooltip texticons and replace hardcoded `20` in `gods_of_africa_protect_partner_effect_tt` with the existing transport constant; preserve all current costs and convoy priority.
2. Clarify blocked-cost feedback for `gods_of_africa_protection_cost_blocked` and `natural_disaster_cost_neighbor_relief_blocked` without changing Event 013 price or penalties.
3. Keep Event 012's 64-participant target-array density open until the maximum plausible eligible-list size and decision-panel layout are reviewed in an available ordinary-panel/runtime route.
4. If revising route cost copy, keep material spends icon-first and distinguish them from Stability/War Support penalties.
5. Preserve the previous AI probability scenario/compare limitations; any future AI-weight change needs a baseline and matching-scenario comparison through `chaosx_ai_probability_auditor`.

**No gameplay or localization changes were made in this audit. Event 013's existing price remains unchanged. Overall Event 012 completion is not claimed.**
