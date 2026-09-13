# KRG clone maturation core handoff

## Parent integration disposition

The isolated-core status below is historical.
After freezing `E016_CLONE_MATURATION_2026_09_08`, the parent wired the existing KRG growth-cycle decision to the new four-cost presentation and begin/cancel/finish transaction, retaining its AI base and native timer/cooldown.
The native factory modifier uses a dedicated file-local mirror of `clone_maturation.civilian_factories`, and native political-power cost is zero because the receipt owns payment.
The old completion helper is a receipt-gated compatibility wrapper, with no rifle/support reward or lifetime paid-cycle cap.
World-end cleanup calls `brilliant_scientist_krg_cleanup_clone_maturation`, which retires/refunds authority before removing the native timer.
Current source review is recorded in `016_clone_maturation_source_review_2026-09-08.md`; durable transaction tests and matching probability comparison remain pending, so this is not final implementation acceptance or a commit claim.

## Isolated-core handoff

Disposition: isolated source core implemented under the accepted “Clone maturation production correction” contract; live integration pending parent baseline and wiring.
Changed files are exactly the new effects/companion, triggers, constants and this handoff.
No existing decision, helper, AI, localisation, framework, state or asset was edited; no commit was made.

Primary contract: `common/scripted_effects/016_clone_maturation_effects.md`.
Public callbacks are `brilliant_scientist_krg_begin_clone_maturation`, `brilliant_scientist_krg_cancel_clone_maturation`, and `brilliant_scientist_krg_finish_clone_maturation`, all COUNTRY scope with no selector input and documented 0/1 temp result.
Admission is `brilliant_scientist_krg_clone_maturation_can_start`; callback direct affordability is `brilliant_scientist_krg_clone_maturation_can_pay_direct`.
The `clone_maturation` profile owns 65 PP, 150 support, 1,000 fuel, four CIC, 90 days, 30 cooldown and 100 clone equipment.
The exact receipt freezes PP/support/fuel/output and is consumed before any refund or reward.
Actual output is `clone_equipment_1`; reconciliation calls existing `clone_refresh_reserve_manpower`.

Parent-accepted physical eligibility includes either existing STATE marker, `brilliant_scientist_krg_clone_growth_site` or `brilliant_scientist_cloning_growth_site`, while owned and controlled by the invoking KRG country.
Country operational flags cannot satisfy it.
The paid-designation source is `brilliant_scientist_krg_designate_clone_growth_site`; the inherited marker is authored at Kruger cloning Deployment in `016_brilliant_scientist_project_effects.txt`.
The active-KRG gate resolves through `brilliant_scientist_krg_decisions_are_active` to current sovereign identity, living Kruger, terminal/world-end locks; the new core also rejects capitulation.
Cloning operation uses the existing unsuspended/undamaged/undismantled reader plus actual `clone_infantry_access_tech`.
Inside the owned-state iterator, PREV is deliberately used instead of ROOT, consistent with the offline Scopes reference's immediate-parent semantics.

The old history/crisis body is copied exactly behind a one-shot internal finish authority.
The lifetime maximum remains eight in its existing source for other consumers, but no new admission reads it.
The actual identity-pressure trigger remains four cycles; it is not confused with that old maximum.
Ordinary factory production and training are unchanged.

Source validation: 59 transaction assertions and two distinct-outer-ROOT scope scenarios passed using the existing interpreter in memory.
Both modeled native ordering cases (CIC available four or zero at begin after admission) pay once and settle identically.
Malformed receipts produce neither speculative refunds nor equipment; successful repeated callbacks cannot repeat output/history; invalidation refunds exact stored direct costs once.
An AST comparison proved exact preservation of the old history/crisis body after removing only its rifle/support outputs.
Provider/operational state and reserve-refresh execution were explicitly stubbed in those scenarios; receipt predicates, real site predicates, payments, output and history ran from source.
No durable evaluator file was changed because this isolated tranche owns only its new core/docs.
The parent should incorporate these scenarios into its existing test suite when wiring the decision.

Required reading used: events, decisions/missions and subagents skill guidance; accepted completion contract; offline Data Structures/Scopes/Decision modding references; installed vanilla decision documentation and effects/script-constants documentation; shared dynamic stockpile debit helper documentation; private conventional-incident exact receipt precedent; actual clone equipment and reserve consumer.
No focus/GUI/map layout was designed or changed.
Existing event inspection for this chain remains partial and does not certify the isolated receipt lifecycle; parent-owned focused MCP/decision/probability evidence remains pending.

Critical wiring notes: native PP cost must be zero with truthful custom-cost display/planning because begin pays PP; do not retain the old manpower/truck payment helper.
Native CIC/timer/cooldown remain parent-owned, independent of callback order.
Cancel for absent receipt or invalid live operation, and route parent removal/cleanup through cancellation before removing the native timer.
Replace the old completion helper with a new-finish wrapper only after the frozen baseline.
No private Mengele country eligibility, new paid construction, alternate qualifying site, free division, direct manpower reward or lifetime cap was introduced.

SHA-256 source evidence:

| File | Hash |
| --- | --- |
| New effects | `7a3e9065529b3b2b06fda9522351c2657dda310c726ec00837c7c52db99d91b0` |
| New triggers | `a7c596b3283039c03a8f292092d0043929f3f768299e8488bc64e5c6a5a609c5` |
| New constants | `767daad3cf47e1e8d7c0b0041874bd6489e52f80f3b675e2a50b6ed9c3d44b8e` |

## Cost and lifecycle localisation tranche

Disposition: isolated localisation implemented at the parent's request; live wrapper integration remains parent-owned.
Added only `common/scripted_localisation/016_clone_maturation_localisation.txt` and `localisation/english/016_clone_maturation_l_english.yml` in this tranche, plus this handoff append.
No existing title, description, decision, effect, AI or localisation key was changed.

The four selectors are `GetCloneMaturationPoliticalPower`, `GetCloneMaturationSupportEquipment`, `GetCloneMaturationFuel`, and `GetCloneMaturationCivilianFactories`.
Each independently compares the current resource against its `clone_maturation` profile value with inclusive affordability.
Satisfied components use the existing yellow/normal presentation, and only insufficient components become red.
Their eight localisation keys are `clone_maturation_political_power`, `clone_maturation_support_equipment`, `clone_maturation_fuel`, `clone_maturation_civilian_factories`, and each corresponding `_blocked` key.
The exact amount-plus-icon aggregate is `clone_maturation_custom_cost`, containing those four selectors without a literal Cost label or extra resource.

Parent wrapper keys:

- `clone_maturation_requirements_tt`: active KRG cloning operations, clone-production technology, currently owned-and-controlled growth site, no capitulation and no other cycle.
- `clone_maturation_started_tt`: profile clone output and duration, with native factories committed until the cycle ends.
- `clone_maturation_completed_tt`: profile quantity of actual Clone Equipment, and the shared `clone_system.weekly_manpower_per_equipment` rate only while equipment remains in stockpile; explicitly no divisions or immediate manpower.
- `clone_maturation_cancelled_tt`: return any actual PP/support/fuel paid for this cycle, release native factories and produce no equipment.

Amounts and duration interpolate the accepted constants rather than duplicate numeric prose.
The completed tooltip describes the current profile; the gameplay receipt remains authoritative for actual output if tuning changes during an already paid timer.
Use the requirement key in `custom_trigger_tooltip` around the shared requirement predicate; do not expose its nested source triggers.
Use the aggregate for custom-cost display with the existing shared inclusive affordability predicate on both admission and custom cost trigger.
Native PP payment must remain zero because the core debits the custom PP cost; parent owns the corresponding AI PP hint and native timer release wiring.
The existing `GFX_decision_brilliant_scientist_krg_clone_growth` art is reused.
Cost text uses existing `pol_power`, `support_equipment_text_icon`, `GFX_fuel_texticon` and `civ_factory` text icons; no new asset or sprite was created.

The decisions skill's four-cost, independent shortage-colour, concise requirement and no-raw-trigger rules determined this presentation.
Source evaluation covered all 16 combinations of exact-price and one-short resource states, yielding 64 matching independent colour results.
All four aggregate selectors and their eight text branches resolve; all 13 new localisation keys were reviewed.
No engine or visual-render claim is made for the not-yet-wired wrapper.
No simplification was introduced in the requested localisation surface; parent integration and its existing audit/baseline requirements remain pending.

SHA-256: scripted localisation `5373ed54aa0350b22da01b2b7c19781390d18f6ea6000eb9303df4497df7655f`; English localisation `291f6c5578147bb365f2ac1b8e07be7268b2ebb43d523196ae02172c92d58eb9`.
