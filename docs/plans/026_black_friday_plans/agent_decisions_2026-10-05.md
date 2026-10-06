# Black Friday takeover decisions

Recorded on 2026-10-06 under the director's 5 October quality rules and authorization to repair the interrupted 026 workstream.
The earlier decisions remain in [agent_decisions_2026-10-04.md](agent_decisions_2026-10-04.md).

## D38. Preserve native discount and achievement helper outputs

Disposition: implemented in source.
The acceptance basis is the requested correctness review of the takeover and the existing caller-storage contract in the events skill.

`black_friday_native_sale_apply` owns the eight linked-factor output temporaries before calling `black_friday_native_sale_read_linked_ordinaries`.
Both native achievement callers own their three law identifiers and two slot counts before calling the reading helpers.
The offline Data structures reference, lines 435–442, states that helper-created temporary variables can disappear on return and caller-created variables retain helper modifications.

The conservative source VM reproduced lost linked discounts at both sale rates and zero law/slot readings before this repair.
The repaired production helpers retain the outputs, refresh without compounding their own contribution, and clear all 580 contributions on removal.
Native engine price composition and rounding are separate acceptance requirements.

## D39. Preserve the simple custom-cost API's nested outputs

Disposition: implemented in source.
The acceptance basis is the same caller-storage rule and the requirement that affordability, payment, and shown prices agree.

The payment wrapper owns payable amount, quote status, validity, family, and native payment result before consuming them.
The quote owns its family-reader output, and the affordability wrapper owns the returned affordability result.
The scoped caller audit found four missing boundaries and reports zero after the repair across 776 inspected calls.
The API documentation includes the required outer output declarations for display and outcome callers.
Source execution checks a 50 Political Power purchase at ordinary price 50, baseline price 25, and Evolution I price 13, accepts an exact balance, and refuses a second charge with no funds.

The two old audit parsers retain bare token-list atoms so legitimate `slots` lists no longer prevent the receipt and caller audits from loading current production source.
This parser repair does not teach the VM to execute native slot-count triggers.
Historical preservation assertions against the September/3 October implementation remain unchanged and can reject intentional later takeover changes.

## D40. Explain a rejected manual entry without repeated reports

Disposition: implemented in source.
The acceptance basis is G7 and G2 in the director's task.

The event's own entry captures one reason when a human's manual or forced request cannot open the sale.
`chaosx.nr26.3` explains an active sale, an ended fire-once sale, disabled Black Friday, paused events, the terminal world state, an existing reservation, or insufficient Chaos.
It reuses the Black Friday report picture and has no payment, reward, history row, or selection-weight effect.
One country flag allows at most one rejection report per human country, while the normal chain has one activation report per human country.
The combined source limit is two reports, and repeated clicks do not duplicate the rejection report.
Automatic reservation and automatic rejected candidates remain silent.
An unset or zero dispatch mode on a direct root invocation is treated as manual, preserving achievement disqualification.

## D41. Require spending evidence for inferred institutional credit

Disposition: implemented in source, with the inference limitation unresolved.
The acceptance basis is the achievement's positive-cost and successful-payment requirements in specification Part 7 and the director's authority to improve weak design.

Activation records Political Power alongside the existing native readings.
A changed law or increased political-advisor count requires a net Political Power decrease.
Increased military staff requires a net Political Power or Command Power decrease, including a commander appointed as advisor.
This prevents free focus/event changes alone from earning institutional families.
The Political Power reading is cleared with the other activation readings.

This is still bounded inference, not proof of an individual paid transaction.
Unrelated spending can coincide with a free change, and same-day gains can mask a real purchase.
Experience and Command Power decreases likewise cannot distinguish an engine purchase from an unrelated scripted loss.
These limits prevent an exact achievement-completion claim.

## D42. Keep native composition and coverage limitations explicit

Disposition: implemented for truthful text and documentation, blocked for complete native pricing.
The acceptance basis is G3, the no-free-purchase rule, and the requirement to disclose every simplification.

D36's conservative linked-factor treatment can give some appointments a smaller reduction than the advertised sale rate.
The report and sale tooltip disclose that limitation, and only decision prices are described as rounding upward.
The broad claim that every engine-priced purchase can never become free is withdrawn from player text because it has not been established.

The production source model also exposes a stronger defect: an Evolution I contribution computed at ordinary factor zero is -0.75, and an ordinary -0.25 factor acquired afterward produces a zero multiplier until the explicit sale refresh runs.
The checked installed on-action sources expose no general law/advisor/idea-purchase hook that can safely refresh every such change.
No recurring whole-world hook, override of other owners' idea/character files, or unverified engine fallback is authorized by this pass.
Exact composition across changing native factors, overlapping design keys, and engine rounding remains blocked pending a supported native integration and engine evidence.
The regression command prints this counterexample as a limitation, separately from its passing storage and payment scenarios.

The event documentation must not claim the workbook matches current wording while [catalog_changes_pending.md](catalog_changes_pending.md) still queues changes for its owner.
No workbook or CSV is edited by this pass.

## D43. Retain the price table's negative debit output

Disposition: implemented in source.
The acceptance basis is the takeover's matching quote/payment requirement and the documented helper-output lifetime.

`black_friday_price_table_refresh_entries` owns `black_friday_price_spend` before calling the quote helper or the nested Soviet Collapse table writer.
The nested writer's negative globals therefore retain the quote's actual negation rather than reading an absent temporary as zero.
The source regression reproduced zero negative outputs at full, half, and quarter price before the repair, and verifies matching positive/negative outputs afterward.
The price table version advances from 17 to 18 so initialization rebuilds already-stamped values.
No ordinary amount, sale ratio, owner outcome, or AI weight changes.

## D44. Remove achievement tag lettering and preserve the state family

Disposition: implemented in the three existing runtime DDS files.
The acceptance basis is the director's no-baked-text rule and the parent's visual acceptance of the corrected source and native-size states.
The completed achievement tag is blank, all purchasing objects and five checks remain present, and the grey and ineligible states derive from that same corrected layer.
The supplied completed/grey templates and red-X overlay are unchanged.
The report, idea, sprite identifiers, consumer paths, and achievement identity remain stable.
The permanent asset handoff records hashes and provenance, while the incomplete event-scoped workspace stays on disk under the assets skill.
No replacement asset family or runtime fallback was introduced.

## References and checks

- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435–442: temporary helper lifetime.
- Offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`, lines 57–59 and 108–145: additive contributions, `modifier@`, dynamic modifier values and update order.
- Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, lines 45–76: localisation and conditional descriptions.
- Installed `documentation/effects_documentation.md`, lines 1153–1172, 2681–2693, 2943–2967, 4372–4381, 5978–5992: add, clamp, country report dispatch, update, and remove operations.
- Installed `documentation/dynamic_variables_documentation.md`, lines 496–498: country modifier readings.
- Installed `events/PoliticalEvents.txt`, lines 2181–2193: conditional event-description precedent.
- Installed `common/peace_conference/cost_modifiers/_documentation.md`, lines 1–45: multiplicative peace demand costs.
- `node docs/plans/026_black_friday_plans/verification/native_sale_lifetime_tests.js`: production storage, native arithmetic, inferred credit, simple cost payment, and rejection-notice scenarios, with declared native fixtures.
- `node docs/plans/026_black_friday_plans/subagent_handoffs/black_friday_outer_caller_contract_audit.js`: scoped caller declarations.
- `python .tools/report_colour_audit.py --event 026`: parchment text, including conditional rejection descriptions.
