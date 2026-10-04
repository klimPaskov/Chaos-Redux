# Soviet famine relief when equipment is insufficient

Disposition: implemented in source after the user accepted the explicit shortfall response on 2026-10-03, with scoped audits and consumer acceptance incomplete.
Current evidence: [the implementation handoff](soviet_famine_shortfall_implementation_2026-10-03.md) and seventeen parsed-source scenarios, including the real action-to-slot-2 cooldown mapping and resolved-famine acknowledgements.
The September text below records the design and its original risk, rather than present acceptance proof.
Acceptance basis: the parent supplied the user's direct 2026-10-03 choice of the explicit no-resource response with famine/corruption penalties and no requisition debt.
The original September risk was that warning and crisis event options lacked the material trigger used by the paid decision.
Current funded options and the final helper are guarded, and current stale-order rejection returns the native decision quote.
The historical motivation below records the old source risk without describing current source as ungated.

## Current contract and exact risk

The paid `sov_emergency_famine_relief` decision requires 30 political power, 120 motorized equipment, 18 trains and 180 support equipment, with equipment checks that accept stock exactly equal to the quote.
The current `.1.a` and `.2.a` event paths share the full funded-order readiness gate and final recheck, without an additional PP charge.
No-resource choices and ongoing/eased acknowledgements keep source-consistent options available even without a valid site.
The existing event relief mission lasts 180 days, and failure raises famine, corruption and evidence pressure.
Its accepted start records the real slot-2 150-day cooldown, so a timeout can allow a subsequent fully paid attempt under the September 26 contract.
Funded event tooltips disclose three equipment texticons and the dynamic -2% stability consequence, and their hidden transaction presentation avoids duplicate generated lines.
Native payment order, final pixels and timing acceptance remain unresolved.

## Accepted design: explicit shortfall response

1. Add a country-scoped `camp_rework_soviet_relief_resources_ready` trigger using the existing centralized motorized, train and support-equipment constants with `NOT (< quote)`. Use it in the paid decision's `custom_cost_trigger` and `available`, its final dispatcher before a resource debit, and relief options `.1.a` and `.2.a`. The decision keeps its distinct 30-PP cost; the immediate crisis-event choice keeps no additional PP cost, as its current event contract already does.
2. Add one explicitly named no-resource response to each event when the exact material trigger fails. The warning response records that relief could not be mobilized and applies existing `camp_rework_soviet.famine_pressure_minor` and `camp_rework_soviet.administrator_corruption_minor` pressure, with a localised consequence tooltip. The critical-crisis response calls the existing `camp_rework_soviet_fail_famine_relief` outcome once, without activating or cancelling a mission; it raises famine, corruption and evidence pressure, and leaves the crisis active. Neither response consumes equipment or changes population directly. These are penalties for a failed mobilization, not an alternative funded relief award.
3. Keep site-specific concealment and admission as separate choices when their verified target exists. The no-resource response remains available when no such site exists, preserving at least one event option. Do not restore the repeatable post-cutover map concealment decision. Recheck the target terminal flags at event selection and effect time as the current source already does.
4. Reuse the existing report art and sound. Add only two event-option localisation keys and concise effect tooltips, update event documentation/catalog only if their player-facing option inventory changes, and retain the correct event log/Records responsibility. Use the probability adapter's event-option `ai_chance` surface for named funded, unfunded, target-valid and target-invalid scenarios; no weight target is chosen in this proposal.

Acceptance tests for this resolution: at exactly quoted equipment, funded relief consumes each equipment type once and starts one mission; one unit short in any type prevents that path and presents the shortfall response; missing site and missing resources still leave a visible event option; site-target choices cannot repeat after concealment/discovery; no response creates population, erases deaths or grants research. Inspect `.1/.2` event options with HOI4 MCP and compare the same named candidate pools before and after. These checks remain source/MCP evidence unless actual engine receipts become available.

## Rejected alternative: requisition debt

Keep an unconditional relief choice but model a measured requisition debt when stock is below the quote, carry that obligation through the next monthly protected-reserve cycle, and reduce benefit or add accountability if it cannot be paid. This changes the economic and event accounting contract, needs a centralized debt ceiling and tooltip, and has no current accepted formula. It is not implemented or assumed.

The original September proposal changed no engine source.
The October implementation has shared preflight, a final guarded transaction, stale paid-order refunds, success-only scripted cooldown, separate no-resource responses and a unique crisis option key.
The current scoped audit and engine-evidence limits are recorded in [the implementation handoff](soviet_famine_shortfall_implementation_2026-10-03.md), [`completion.md`](completion.md) and [`resume_packet.md`](resume_packet.md).
