# Japan-China Chemical Campaign Routes

## Active routes

The campaign offers two delivery routes. The direct decision flow from the 19 September 2026 source is available alongside the native raids, which remain a second route under the 20 September CBRN implementation.

`japan_chemical_campaign_cycle_agent` selects mustard, chlorine, phosgene, or lewisite at no cost. `japan_chemical_campaign_attack` targets an eligible enemy-controlled Chinese core state in Asia. It uses the selected legacy cylinder lot and the shared CBRN consequence dispatcher. It does not require an assigned division, a supply-node origin, or the native raid preparation timer.

The direct attack keeps the historical readiness, use-policy, war, technology, target, and cooldown gates. Normal price is 20 Command Power and 120 cylinders of the selected agent; the chemical command reagent idea changes the Command Power price to 16. During a Black Friday sale or evolution, the existing universal-cost quote controls both costs, records their payment, and refunds them if the effect rejects the selected target or payload. Cost quantities are read from the owning constants and sale quote.

The native raid route remains in `common/raids/japan_cbrn_campaign_raids.txt`. Its variants select one agent, require an assigned division and supply-node origin, and use five days of native preparation. Native equipment reservation and native Command Power remain owned by the raid instance. The direct decision route and raid route share the current country attack cooldown and selected-state cooldown markers, so either route temporarily closes the other after a successful release.

## Source and integration

The direct decision, category, and scripted-localisation definitions are restored from `4337957b1f`; the direct effect and Black Friday payment closures use the same source revision. The current raid definitions and outcome adapter remain in place. Both routes dispatch through the current CBRN exposure and consequence helpers, so the shared contamination, immunity, evidence, attribution, and Condemnation integrations continue to apply.

The decision files expose two direct actions in one category. The agent selector is an optional free choice; the attack is the only action required to release the selected cylinders into a chosen state. The map decision has no event or facility staging step. Its AI score is based on the historical decision block and current shared campaign constants.

Source inspection confirms the payment preflight, selected-lot debit, accepted outcome dispatch, rejection refund, command-power price, and cooldown cleanup paths. No live-game behavior is claimed here. Native raid reservation cancellation behavior remains an engine validation limit for the raid route.
