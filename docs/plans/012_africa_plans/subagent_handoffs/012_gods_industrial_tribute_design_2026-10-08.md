# Gods of Africa industrial tribute: bounded F1 repair contract

Date: 2026-10-08.
Author: chaosx_improvement_loop_planner, plan only.
Disposition: promoted into the accepted full, technical and decisions/missions/UI specs on 2026-10-09 under the recorded parent acceptance.
The bounded industrial contract is implemented in source, while numeric AI and native acceptance remain unresolved.
The only file written by this planner is this handoff.
Parent acceptance selects the funded one-site native repair program, preserving the existing CPP price and proportional paid service.
The [parent reconciliation](012_gods_industry_parent_reconciliation_2026-10-09.md) identifies the current implementation and promoted specification sections.
The compact public-value GUI proceeds in its disjoint owner files.
Source findings and planner tool results below describe the pre-implementation inspection on 2026-10-08.
Earned paid service must survive ordinary contract closure, substitution and the normal secured-Africa settlement until its own native expiry or site completion, while recipient loss or replacement revokes the original recipient's program.
Normal settlement must not be treated as a hostile authority-loss callback that silently removes previously purchased repair time.
Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

## Recommended result

Keep the existing industrial tribute price and actual participant-to-Africa political-power transfer, and attach a funded native civilian-factory repair program to one damaged African state.
The program supplies +50% repair speed for industrial_complex at that site for a finite number of paid service days.
It ends when its paid time expires, the site's civilian factories finish repairing, or its recipient authority/site becomes invalid.
Full payment normally purchases 30–120 service days, calculated from the existing frozen scaled CPP quote.
Partial payment purchases only its corresponding share of days.
This is a repair program within the current industry_repair family, not a new Event 012 route.

The accepted basis is specs\012_gods_of_africa_full_spec.md:18 and :466–479 in docs\specs\012_africa_is_one_gods_of_africa_specs\.
Those requirements allow a provable finite repair program and require its burden and duration to be communicated.
The current completion audit, docs\plans\012_africa_plans\subagent_handoffs\012_gods_current_completion_audit_2026-10-08.md:F1, identifies the missing industrial consequence.
The later response-phase addendum is already dispositioned implemented in 012_gods_decision_phases_addendum_2026-10-07.md and identified by the parent as dbed4c7db0337dcce216fc9f9c545be6e0143814.
This handoff does not duplicate that phase design or reopen its target/response architecture.
The parent's Chaos normalization a2b23f1ef412b6c88e592ccca32a8d93b363064a remains with its existing owner.

Current source defines gods_of_africa_demand_family.industry_repair = 7 and transport = 6 in common\script_constants\012_africa_gods_constants.txt:154–182.
Use the named industry_repair constant throughout; do not renumber it to match the prompt's “family 6” shorthand.
The current industry_pp_amount is 20 at :412.
Its candidate quote, scaling, partial ratio, contract identity, deadline, accepted material substitutes and history owners remain authoritative.
The existing successful generic branch debits CPP, credits Africa CPP and assigns payment_delivered from the request; it does not apply an industrial effect.
The source lookup for gods_of_africa_transfer_payment selected its second if / first else at common\scripted_effects\012_africa_gods_effects.txt:2783–2808, revision a08b04c1b64df0b22f22df6f1a84848b264036f9feba5e088c63df874851092d.
That branch must receive an explicit industry handler rather than remain the industrial completion path.

## Native mechanism and evidence

The core effect is a state dynamic modifier containing state_repair_speed_industrial_complex_factor = constant:gods_of_africa_industry.repair_speed.
Installed documentation lists this state modifier family and industrial_complex among its supported building types: C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md:4879–4886, revision 00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e, read through hoi4.reference_read.
The offline wiki explicitly describes repair speed of the specified building in a state: paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:1218–1219, revision fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f, also read through the MCP.
The modifier improves repair of existing damaged civilian factories; the plan's industrial result is that native repair service and its observed repair consequences.
Do not credit equipment, manpower, construction points, new factory levels or africa_central_capacity merely because funding was paid.

Use damaged_building_level@industrial_complex as the state damage reader.
The installed reader documentation is documentation\dynamic_variables_documentation.md:1118–1120, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda.
The offline parallel is paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1676, revision 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.
Both were read through hoi4.reference_read.
These are the verified reader names; the planned record names below are ordinary variables, not additional engine readers.

Add the modifier in the frozen state with a finite normal-variable days input and scope equal to the recorded recipient country.
Installed documentation explicitly supports STATE, variable days, updating an existing cooldown, and a country-restricted state modifier: documentation\effects_documentation.md:1153–1173, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.
The offline wiki separately explains that scope controls the variable base and that matching scope is required for removal: paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:149–181, revision fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f.
The fixed repair factor avoids relying on an unverified cross-scope variable lookup inside the modifier.
Removal must use the recorded original recipient scope, as documented at effects_documentation.md:5978–5991 under the same effects revision.
Check native installation with has_dynamic_modifier and the matching scope; installed triggers_documentation.md:3775–3792, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, includes the scoped example.
The offline scoped syntax was read at paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:648, revision abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06.

Require at least one available recipient project factory at quote creation and an unfinished-site payment.
The exact reader is num_of_civilian_factories_available_for_projects: installed dynamic_variables_documentation.md:608–611 and triggers_documentation.md:6757–6765, under the revisions above, read through the MCP.
Its wiki counterpart is Data structures:1551 and Triggers:846.
This is a nonconsumed recipient capacity requirement.
It does not reserve a donor factory or prove that Africa assigned a factory to this particular repair queue.
The promised result must therefore be described as a repair-speed program; observed building repair and its timing remain native acceptance evidence.

Vanilla precedents inspected were ETH_international_red_cross_dynamic_modifier, with industry_repair_factor driven by its country variable, and ETH_state_development_dynamic_modifier, with state construction support, in common\dynamic_modifiers\bba_dynamic_modifiers.txt:242–265.
hoi4.source_lookup resolved the source location at :253 to ETH_international_red_cross_dynamic_modifier, revision f59113ee57f034dd0e11189df9a7f3d99c5c81777c2534c2353638eb39fad43f; the surrounding native definitions were read directly.
These establish native economic-support patterns, not historical claims about the fictional Gods.
The regional connection stays with the accepted rebuilding of African industry; this repair needs no new myth, faction or historical route.

The required mechanism research also read civilian_factory_use in installed modifiers_documentation.md:2202–2206 and offline Modifiers:686, and add_offsite_building in installed effects_documentation.md:1813–1821 and offline Effects:1758.
Vanilla AST_union_strike uses civilian_factory_use = 1 during days_remove = 25 in common\decisions\AST.txt:1–42.
Vanilla denmark_trade_deal.7 removes previously granted offsite civilian factories using negative levels in events\AAT_Denmark.txt:6105–6148.
Those are concrete finite-commitment and offsite-removal precedents, not permission to assume independent offsite ownership, expiry or refunds.
The recommended repair does not depend on those transfer semantics.
Native add_building_construction was read at effects_documentation.md:839–847 and offline Effects:3614 under the effects revisions above.
The damage_building sections were read at installed :3374–3416 and offline Effects:3616; they do not establish negative-damage repair or building-refund semantics.
No alternative implementation is proposed because the primary repair mechanism is feasible at the documentation/design level.

## Quote, target and tuning

Put the new tuning in common\script_constants\012_africa_gods_industry_constants.txt.
These are recommended values for parent acceptance, not an accepted rebalance of the existing CPP quote.

| Field in gods_of_africa_industry | Recommended value | Meaning |
|---|---:|---|
| repair_speed | 0.50 | Native civilian-factory repair-speed factor at the frozen site |
| base_service_days | 60 | Service at the existing 20 CPP base quote |
| minimum_service_days | 30 | Lower service bound after existing quote scaling |
| maximum_service_days | 120 | Hard per-contract paid service bound |
| minimum_site_damage | 0.50 | Minimum damaged civilian-factory level for a new program |
| available_project_factory_floor | 1 | Recipient's nonconsumed usable-capacity floor |
| maximum_host_programs | 1 | Includes unpaid reservations and surviving paid programs |

Define Q as the existing final frozen industry CPP quote, preserving every existing scale factor and actual charge.
Freeze D = clamp(floor(base_service_days * Q / constant:gods_of_africa_transaction.industry_pp_amount), minimum_service_days, maximum_service_days) once after Q is finalized.
Calculate D using the existing positive modulo-and-subtract flooring pattern in gods_of_africa_floor_equipment_amount, common\scripted_effects\012_africa_gods_equipment_effects.txt:8–12.
Keep the service-day arithmetic in the industrial helper rather than changing that equipment helper's purpose or applying equipment rounding to CPP.
Do not recompute Q or D from later Strength, Chaos, repetition or factory changes.

Add a physical eligibility conjunction to the existing industry need, leaving the existing central-capacity severity/ranking calculation with its owner.
A new industrial contract needs an available host program slot and a state the current African host owns and controls, which is its core, lies on Africa, and meets minimum_site_damage.
The existing low africa_central_capacity check alone is not proof of repair need.
Inspect only the host's owned states when selecting a new site.
Prefer its qualifying capital; otherwise choose the qualifying state with the most damaged civilian-factory levels, retaining the first encountered state on an equal damage score.
Freeze that actual state scope pointer; do not make each payment choose a new random state.
The continent predicate is the documented state trigger is_on_continent = africa, installed triggers_documentation.md:6006–6014, revision 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29, and offline Triggers:1854.
A selection pass is host-local and occurs through existing quote/need owners, not through a new recurring world iterator.

Reserve the host's single program slot when the industrial contract is created.
Do not reserve a slot merely because an unsuccessful candidate was examined.
Quote creation must bind the same contract ID, generation, authority epoch, origin and participant/host identity that the current contract ledger uses.
The quote shows the actual CPP amount, named site, +50% repair speed, total paid-day ceiling D, existing payment deadline and the condition that service ends when the site's civilian factories are repaired.
For a partial payment, show the actual partial CPP amount and newly purchased service days.
Availability and custom_cost_trigger must use the same pure preflight as execution; the existing decision phase and target owners remain intact.
Installed common\decisions\_documentation.md:1–46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019, documents the separate refresh schedules for visible, available and target checks, so a displayed cached quote cannot authorize a stale transaction.

Keep gods_of_africa_participant_has_capacity_for_family and gods_of_africa_build_capacity_profile as payer budget calculations in pre-contract selection and gods_of_africa_freeze_demand_burden.
Those callers test candidate/heavy/light CPP amounts before an active industrial receipt exists; requiring an active receipt there would incorrectly reject selection or classify every industrial burden as heavy.
Apply physical candidate validity separately during selection and binding.
For bound contracts, gods_of_africa_current_demand_can_be_paid and gods_of_africa_partial_payment_is_affordable add the appropriate industrial transaction gate.
The full gate uses demand_remaining, the partial gate uses the existing clamped partial quote, and the execution gate uses payment_amount.
Implement these as read-only proposed gods_of_africa_industry_full_payment_can_execute and gods_of_africa_industry_partial_payment_can_execute wrappers around the industrial preflight; they do not mutate the quote to evaluate it.
The exact existing receiver predicate is gods_of_africa_host_can_receive_demand_payment in common\scripted_triggers\012_africa_gods_contract_triggers.txt:148–168.
Its current generic non-fuel branch admits industry without any physical proof.
Give industry its explicit receiver branch and exclude industry from that generic branch, retaining the current fuel branches.
Its existing decision availability and zero-willingness consumers then share the same receiver validity.
Replace the fuel-only blocked explanation on the industry path with the precise industrial requirement text.

## Exact paid effect and receipt contract

Add an explicit industry_repair branch to gods_of_africa_transfer_payment before the generic political fallback.
The branch calls the proposed gods_of_africa_pay_industrial_tribute helper.
All new helper/record names in this handoff are proposed ordinary script symbols; none is asserted to exist already.

The pure preflight proves current contract/epoch ownership, matching frozen industrial terms and host reservation, positive Q/D/payment amount, a coherent original CPP balance, and the existing inclusive CPP affordability.
Before a new unfinished-site payment, it also proves the frozen site's ownership, control, core, continent and remaining damage, plus recipient capacity.
Use remaining damage greater than zero for an existing program; the 0.50 threshold is only the new-program threshold.
Require a positive quoted new service-day increment for an unfinished site, so a zero-day stale action cannot become a price-only payment.
A correctly bound, observed early-completion receipt supplies the separate finished-project settlement gate described below.

Snapshot donor and recipient CPP immediately before and after the existing exact debit and credit.
Use the verified numeric reader has_political_power, installed dynamic_variables_documentation.md:431–434, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda, read through hoi4.reference_read.
Do not copy the raw political_power reader presently used in gods_of_africa_read_contribution_native_stock's emergency branch into this new receipt.
This is a narrow industrial receipt; it does not authorize refactoring the other contribution/grading owners.
Initialize all temporary receipt inputs in the caller chain with bare names, and retain durable results as normal variables.

Define p as the independently measured donor CPP debit and matching recipient CPP credit for this transaction.
Both must equal the selected exact payment quote under the installed numeric representation before p can accrue repair service.
The current requested-amount assignment to gods_of_africa_payment_delivered is not that independent measurement.
Do not silently accept a short credit, replace it with the request, or reduce the quoted charge to bypass a receipt failure.
On a failed current transaction, reverse only its measured CPP debit/credit and any provisional native timer write; preserve all earlier successful charges, service and history.
This rollback is a failed-click refund, not a discount or waiver on a successful industrial action.
Native numeric precision and credit-bound behavior need the explicit acceptance cases below; no unsupported cap reader or speculative PP maximum is assumed.

Let C be cumulative independently receipted industrial CPP for this immutable program, and G its total service days already granted.
Compute E = floor(D * min(C + p, Q) / Q), multiplying before dividing.
When C + p is still less than Q, keep E below D to prevent fixed-point rounding from granting the last day before the full charge.
When the exact funding total reaches Q, set E to D.
The new paid service is N = E - G.
After positive N, set new_due_day = max(global.num_days, prior_due_day) + N and pass new_due_day - global.num_days through a normal variable to native days.
Thus a live term receives only N additional paid days, and an expired term restarts for only N newly purchased days.
Never refresh a full D-day term for another partial receipt.
C never exceeds Q and G never exceeds D.
The maximum boost over one contract is 0.50 * D service-days before early completion/loss, at most 60 bonus-rate-days with the proposed cap.

Publish the in-flight tuple before the debit, and consume a positive receipt once.
Require C + gods_of_africa_demand_remaining = Q before an original industrial payment.
After the new receipt increments C but before the existing owner reduces the remaining balance, this invariant prevents a second transfer under the unchanged balance.
After the owner consumes the delivery, its remaining balance restores the invariant for a later legal payment, subject to the existing partial cooldown.
Repeated clicks, replayed helper calls and stale epoch callbacks must not debit or extend twice.

Verify native modifier presence with the recorded scope before publishing the new service receipt.
If installation fails, restore the previous native due date/modifier state and reverse this transaction's measured CPP changes without setting payment success, fulfillment, compliance or a new industrial history receipt.
The native presence predicate does not expose the timer's remaining days; the exact native expiry/refresh behavior is still a user-owned acceptance case.
On success, publish p into the existing payment_delivered/payment_received outputs in CPP units and use the existing full/partial/contract/report owners once.
Keep granted days, actual damage observations and native installation proof in the industrial program record.
Do not turn service days into rifle, fuel, manpower, voluntary-aid or fabricated economic-ledger credit.

## Partial payments, substitutions and deadline behavior

For Q = 20, D = 60 and a first payment of 10, grant 30 days of +50% repair speed.
A second payment of 10 during those 30 days adds 30 paid days to the original due date.
If it arrives after the first term expires, it creates a fresh 30-day term; cumulative purchased service remains 60 days.
For fractional Q, preserve the exact CPP price and carry the fractional day entitlement through cumulative calculation rather than repeatedly flooring each receipt independently.
The final exact CPP payment grants the remaining whole-day entitlement.

Keep gods_of_africa_resolve_partial_compliance, gods_of_africa_apply_partial_delivery, gods_of_africa_compute_partial_payment_amount, the existing partial cooldown and the native demand mission as their owners.
Choosing partial payment continues to bind the remaining terms through gods_of_africa_mark_contract_agreed.
The price remains due under the existing deadline and extension rules.
An extension adds no repair days, refunds no funding and does not enlarge Q or D.
The payment deadline and purchased service expiry are distinct: a legitimate payment before the deadline may fund service that continues afterwards.
Existing defaults in gods_of_africa_demand include 45/90/120/60/150-day deadlines; this repair does not replace them with a new universal timer.

Current substitute slots offer infantry equipment, fuel and manpower.
Preserve those offers, acceptance checks, actual material transfers and honored-substitute history.
A material substitute purchases no additional industrial days.
If industrial CPP was already paid before substitution, its earned native program can finish its paid term independently of the contract's temporary response fields.
The substituted material closes only the remaining contract through the existing substitute owner; it cannot be counted a second time as CPP funding.
Keep the original industrial Q/D copied in the surviving program record when the current demand's units change.
Do not add industrial substitute slots to other families in this repair.

Early completion is a real terminal result, not permission to waive the remaining agreed CPP.
During a valid paid native term, observe that the same owned/controlled site has changed from positive civilian-factory damage to zero damage and publish an epoch/contract-bound site-completed receipt with its observations and day.
Remove the program modifier once its physical work is complete.
The outstanding agreed CPP can then settle that completed repair program without reinstalling a useless modifier or claiming another repair result.
Full compliance requires both full receipt of Q and the existing paid-program/service receipt or this measured completion receipt.
An unfinanced healthy site, a mere quote, a price-only historical payment or an unobserved completion cannot supply this settlement proof.
Do not claim a percentage of damage was caused by the program: native observations establish the site result and active support, not counterfactual attribution.

If the site becomes healthy before any native paid program exists, reject the industrial click without charging CPP.
If authority/site invalidation makes the service impossible, retain its actual funded and unpaid amounts in the industrial retirement receipt and let the existing contract interruption owners retire it unfulfilled.
Do not zero the balance to manufacture fulfillment, award full compliance, or use an automatic emergency-relief relabel.
Existing valid material negotiation remains available through its current owners.
Ordinary donor refusal/default remains with the existing failure/Wrath owners; recipient invalidation must not masquerade as donor refusal.

## Record ownership, loss and cleanup

Use one canonical host program record so its earned support does not depend on an annexed donor's country scope remaining usable.
Store its participant pointer, contract ID, generation, authority epoch, origin identity, frozen state pointer, Q, D, cumulative CPP received C, granted days G, due day, initial/last observed damage, observation day and last consumed receipt sequence.
Use flags for reserved, in-flight, native-applied and observed-site-completed state.
Participant terms carry the frozen quote/site and the binding to that record for display and pure preflight.
The host's one record covers both an open reservation and any surviving earned term; it is not another unbounded history registry.
Preserve final funded/unpaid amounts and completion/loss reason through the existing durable history/report boundary before reclaiming the record.

| Change | Required behavior |
|---|---|
| Full funding while damage remains | Close the original contract through its current owner; keep its already-paid native term until expiry, repair completion or recipient loss. |
| Partial/default/substitution closes the response | Retain previously earned service; dispose of unpaid terms through the existing owner, without granting unpurchased days. |
| Donor annexed or removed after a successful CPP receipt | The recipient keeps paid support; no donor factory is borrowed. Retire any unpaid donor contract through existing participant cleanup. |
| Recipient loses its site or its control | Country-scoped state support must not benefit the captor; remove using the recorded original recipient scope and retire unfulfilled terms once. |
| Recipient loses authority, capitulates, is annexed or changes epoch | Remove its matching program before clearing/rebinding owner pointers. Retain charges/history; no industrial compliance or ordinary failure penalty is fabricated. |
| Native service expires | Native modifier expiry ends the effect. An open partially funded industrial contract retains its record/reservation for a legal later payment; a closed record is reclaimable only when no earned term survives. No days are granted by reconciliation. |
| Replayed/stale callback | Verify the complete current tuple before touching native effect, slot, money or history; an old receipt cannot remove a new epoch's program. |
| Program disappears before its recorded expiry | Mark service evidence unresolved and block additional completion/payment until reconciled; do not silently reinstall already consumed days. |

Call proposed gods_of_africa_review_industry_program from the existing host owner clock before need selection.
A read-only quote preflight must also recognize an expired reservation immediately; its execution reconciliation can release the exact expired record before choosing a new program.
Here a releasable expired reservation means a closed/retired contract with no surviving earned term.
An expired paid interval under still-open partial industrial terms must not release or overwrite the record: its C/G/Q/D and slot are needed for the partial-after-expiry payment case.
Neither an early-completed site awaiting agreed CPP settlement nor an open unfunded contract is a free slot.
The existing native expiry is the effect's final time bound even if an owner clock stops.
Integrate proposed gods_of_africa_retire_industry_program into gods_of_africa_cancel_on_unifier_loss before revoking/clearing the old recipient object and into the corresponding current epoch retirement path.
gods_of_africa_cancel_participant may retire unpaid terms but must preserve host-owned paid service after donor loss.
gods_of_africa_clear_demand clears temporary industrial response fields only; it must not erase a paid surviving host record.
Use no new global recurring hook, whole-world gameplay scan or permanent consumer-goods penalty.

## AI, costs and presentation

The read-only chaosx_ai_probability_auditor, agent 01a11ac5-d438-7791-86ba-29246cd589b0, inspected the current response/host pools and returned findings inline without writing files.
Full and partial industry responses each have one spendable type, CPP.
Each current material substitute has one spendable type; offer payment occurs only on acceptance.
Contract creation, negotiation and host acceptance/rejection have zero row costs.
The available recipient factory is a requirement, not a spendable cost.
This recommendation adds no donor commitment and no hidden second price.

The auditor found zero-decimal CPP display at localisation\english\012_africa_gods_l_english.yml:594–598 while industry quotes remain percentage-scaled and are not equipment-floored.
Preserve the stored/debited CPP and display sufficient precision in ready, blocked, hover, partial and balance strings to agree with it.
Use an industry-aware CPP formatter, retaining integer formatting for material quantities.
The CPP cost uses the existing £pol_power texticon; service days and site capacity belong in the requirements/effects summary, not a fake factory-payment cost.
Do not apply a nominal fixed ai_hint_pp_cost to this dynamic quote without verified supported semantics.
The existing nine fixed-price AI hints are a separate repair and remain with their owner.

Keep the current numeric willingness factors.
The deterministic selector and response willingness must respect the same physical program validity as human availability, including no-site, busy-slot, lost-capacity and stale-epoch cases.
The changed eligibility needs before/after named-scenario review through the probability auditor even when no weight number changes.
Decision scores are willingness scores, not normalized click probabilities.
The current source bases reported by the auditor include comply 50, partial 15, negotiate 20 and substitute 10; those components alone do not prove actual ranking.

Use the current decision rows, phase grouping and event report wrappers.
Proposed text keys are gods_of_africa_industry_repair_program, its _desc, gods_of_africa_industry_terms_tt, gods_of_africa_industry_unavailable_tt and gods_of_africa_industry_completed_tt.
The terms summary names the state, actual remaining CPP, newly funded service days, +50% repair speed and expiry/early-completion condition.
Blocked text identifies the missing site, actual CPP, host capacity, reservation or authority requirement.
A completed-site settlement names the earned completion and remaining agreed funding.
Update current family/quote/outcome consumers so their physical result and funding units agree.
Do not add a selection window, extra participant action or new focus route to present this repair.

Reuse the verified state modifier icon GFX_modifiers_ETH_state_development.
Its mod consumer is interface\countrystateview.gfx:848–851 with texture gfx/interface/state_modifiers/modifiers_ETH_state_development.dds; the installed vanilla texture exists.
This is the existing native state-modifier family, not a sourced placeholder or newly commissioned asset.
The existing industry-priority decision keeps GFX_decision_012_africa_gods_set_priority.
No art, animation or asset-file production is required for this recommendation.

## Exact parent implementation surfaces

| File | Required symbols/work |
|---|---|
| common\scripted_effects\012_africa_gods_industry_effects.txt, proposed | gods_of_africa_select_industry_site, gods_of_africa_bind_industry_terms, gods_of_africa_pay_industrial_tribute, gods_of_africa_review_industry_program, gods_of_africa_retire_industry_program; bounded quote, receipt, service and cleanup owners |
| common\scripted_triggers\012_africa_gods_industry_triggers.txt, proposed | gods_of_africa_industry_site_is_eligible, gods_of_africa_industry_quote_is_current, gods_of_africa_industry_payment_can_execute, gods_of_africa_industry_full_payment_can_execute, gods_of_africa_industry_partial_payment_can_execute, gods_of_africa_industry_completion_is_proven; explicit host/state/currency preflights |
| common\script_constants\012_africa_gods_industry_constants.txt, proposed | The proposed schema-first tuning table above |
| common\dynamic_modifiers\012_africa_gods_industry_modifiers.txt, proposed | gods_of_africa_industry_repair_program with the native state repair factor and verified state icon |
| common\scripted_effects\012_africa_gods_effects.txt | build_need_profile, select_demand_family, calculate_demand_amount, create_demand_contract, transfer_payment, resolve_full_compliance, resolve_partial_compliance, apply_partial_delivery, resolve_substitute, clear_demand, run_owner_tick, cancel_on_unifier_loss, cancel_participant under their existing gods_of_africa_ names |
| common\scripted_triggers\012_africa_gods_triggers.txt | gods_of_africa_current_demand_can_be_paid and gods_of_africa_partial_payment_is_affordable add industrial preflight; gods_of_africa_participant_has_capacity_for_family retains the existing payer CPP budget semantics |
| common\scripted_triggers\012_africa_gods_contract_triggers.txt | gods_of_africa_host_can_receive_demand_payment adds the explicit industrial receiver branch and removes its generic non-fuel bypass |
| common\scripted_effects\012_africa_gods_contract_effects.txt | Preserve open/close/retire/agreed ledger owners; integrate exact industry retirement/output before their normal cleanup |
| common\scripted_effects\012_africa_gods_epoch_binding_effects.txt and paired triggers | Reuse current identity/authority proofs; hook industrial retirement before old owner binding is destroyed |
| common\decisions\012_africa_gods_decisions.txt | comply_demand, partial_compliance, material substitute, negotiation and industry-priority consumers under their current gods_of_africa_ identifiers; no new response family |
| common\scripted_localisation\012_africa_gods_scripted_localisation.txt and 012_africa_gods_response_scripted_localisation.txt | Existing family/quote/balance/outcome getters plus bounded repair terms and CPP precision |
| localisation\english\012_africa_gods_l_english.yml | Exact current cost strings and proposed program/terms/blocker/completion keys |
| docs\events\012_africa\gods_of_africa.md | Actual native program, CPP transfer, paid-time cap, early completion, interruption and evidence limits |
| docs\testing\chaosx_test_country.md and existing Gods CXT extension below | Inert fixture/schema initialization and the acceptance scenarios |

The existing CXT carrier is chaosx_cxt_extension_event012_africa_gods, and its registered setup effect is chaosx_cxt_extension_event012_africa_gods_apply in common\scripted_effects\012_africa_gods_cxt_test_effects.txt:20.
Extend that existing setup effect with idempotent inert industry-fixture/schema readiness for the new record; do not erase active receipts.
A second carrier, registration hook or general framework is unnecessary.
The existing common\ideas\012_africa_gods_cxt_extension_ideas.txt and common\on_actions\012_africa_gods_cxt_on_actions.txt registration remain sufficient.
Initialization must not create damage, grant factories, install a repair program, acquire a Gods host or fire Event 012.
Any physical fixture setup belongs to an existing player-triggered debug surface and user-owned native validation.
The existing CXT package extension is necessary for record/scenario coverage, not for automatic industrial grants.

## Acceptance cases

These are required parent/source and user-owned native cases, not tests executed by this planner.
No game was launched and no new tooling was generated.

| Case | Required result |
|---|---|
| IND_FULL_BASE | Q 20, eligible damaged site, host capacity: exact donor -20/recipient +20 CPP and +50% native repair for D 60 days or genuine earlier site completion; physical repair is observed before F1 acceptance. |
| IND_PARTIAL_CONTIGUOUS | Two receipted 10 payments: 30 then 30 additional days; second payment adds only its purchased time; existing balance/cooldown/history owners agree. |
| IND_PARTIAL_GAP | First 30 days expire; later remaining 10 buys only another 30 days; total G is 60, with no free renewal of earlier days. |
| IND_FRACTIONAL | Q 20.5, D 61; the actual half quote 10.25 is displayed/debited exactly; cumulative integer-day remainder produces a total of 61 days, not two independent 30-day grants. |
| IND_CPP_BOUNDARY | Below, exactly at and above each real full/partial quote: display, gate, execution and AI eligibility agree; insufficient CPP changes no money, service or contract state. |
| IND_NO_SITE | Low central-capacity meter without a physically damaged eligible site cannot produce industrial payment/compliance. |
| IND_NATIVE_FAILURE | Missing modifier/failed current receipt restores only the new debit/credit and previous native term, with no false fulfillment or extra cooldown claim. |
| IND_EARLY_COMPLETE | Genuine paid program's bound site reaches zero damage during the observed term; remove support, retain proof and settle the remaining agreed CPP without another fictitious industrial grant. |
| IND_NO_EARNED_COMPLETION | Healthy quote site or mere historical CPP-only payment supplies no completion receipt and cannot close the industrial obligation. |
| IND_SUBSTITUTE | Accepted rifles/fuel/manpower use their current measured owners; original paid repair time survives appropriately, but material gives zero new repair days. |
| IND_LOSS | Site capture, host authority loss, donor loss and late epoch replay follow the loss table; no captor benefit, duplicate refund, duplicate CPP debit, stolen new-epoch modifier or false compliance. |
| IND_CAP_AND_END | One host program/reservation, G no greater than D, native expiry even when clocks stop, and no permanent penalty or accumulated factories. An expired partial interval retains its bound open record; only a closed record without surviving service is reclaimed. |
| IND_DEADLINE | Existing negotiation extends the payment mission only; no unpaid repair-time renewal, debt-zeroing or reward on a stale/invalid receiver. |

Repeat the auditor's F1_GOA_IND_REPAIR_OPEN_LIGHT_AFFORDABLE and F1_GOA_IND_REPAIR_OPEN_HEAVY_UNAFFORDABLE with a complete real host/participant tuple, CPP state and target scopes.
Add named no-site, no-host-capacity, active-program, exact-CPP, partial-after-expiry, completed-site-settlement and stale-epoch scenarios.
Require the auditor's matching probability_compare after implementation; retain true pre-edit sources rather than comparing the current file to itself.
The intended result is coherent availability, safe CPP saving behavior and no willingness to execute an invalid program; no exact selection probability target is proposed.

## Evidence delivered, blockers and uncertainty

Verified exposed and live routes used: hoi4.reference_context, reference_search, reference_read, source_lookup, probability_inspect, event_inspect, event_render, decision_inspect, map_inspect and script_validate.
The initial decision reference bundle omitted Triggers/Scopes/Localisation at limit 4; the subsequent limit-12 bundle had omittedSources empty, and the relevant detailed native sections were read separately.
No rewrite, helper_expansion, job or native-task route was used.
Source/read-only tool results do not establish native execution or replace parent review.

Event .604 trace and options render returned EVENT_INSPECTED_PARTIAL / EVENT_RENDERED_PARTIAL, revision e59ab758e239e5ea62d20e5c085f4aa12ec8c39fae3ec9dac0d5ddca379ebd2d, with helpers deliberately unexpanded.
The render selected three nodes.
Exact retained PNG URI:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c56f87925c77d730ddd4be6e7fd0075e8e45c10b56f5d1ad23b52c524fd3b9f/f6d19a7d14273ec03ccb72d17082a083e26b2ee168b8f6805d015f65cc3e4258/event-options-e59ab758e239.png
Reading that PNG and its linked JSON failed with MCP -32603, “Artifact provenance manifest is unavailable.”
Event-chain visual evidence therefore remains unresolved; the tool's render metadata is not a reviewed image.
The parent must recover/read current affected .603/.604 evidence for implementation review.

Map lookup inspected state 275 as an illustrative record only; it is not a prescribed repair target or a runtime-damage claim.
Full read-only map inspection with overview returned revision 71f42e4994039a62cfa0fede7676402e9e2e4ab23418643f735b34e30b2db347 and one selected state.
Its overview URI is:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11/157c2cffbb81745a0aecfa46140f819b96c877f34f0c17351f0525507e9d0e59/map-overview.71f42e4994039a62.png
The full overview read returned a stringified resource envelope declaring 404850 bytes and complete = true, but only 47259 blob characters with an invalid base64 alphabet.
That is not a complete decodable payload; it was not accepted as visual evidence.
The broad map result also included diagnostics outside this industrial repair, including Event 032 localisation and floating-harbor reviews; this planner did not expand ownership to repair them or claim a clean map.
Map visual acceptance and runtime target/damage proof remain unresolved.

script_validate recognized add_dynamic_modifier as a state effect, but returned SCRIPT_CHECK_PARTIAL, valid = null and SCRIPT_ARGUMENT_BLOCK_UNCHECKED.
Its checksPerformed were syntax, command_kind and declared_scope; parametersChecked was false.
The precise variable-duration/scope behavior is grounded in the cited installed prose and still requires native acceptance.

The AI auditor's probability route reported version 3.10.0.
Its complete filtered participant/host pools still needed campaign inputs, notably scope.FROM for the host pool.
The two named open-demand probes produced 10 rows, zero eligible and 732 unresolved; the corrected two-point payment_amount sweep remained equally unresolved.
Missing host relationship, current generation and live CPP/capacity inputs prevent numeric ranking, threshold-crossing, dominance or starvation conclusions.
These diagnostics do not prove decisions are impossible in game.
The scenario hash was f830d2f3cebdb0e817c620831805cdffd3db257f63c699403d001c6a4af66fb0, and source hash was cd0846ce49fe3123c413b17d3ae9bccc92228a7b15eb5992ac6ab24197752d77.
Evaluation revision: c2f31b6d61e7b58dc5bb2c012e502af6b22035eb3212d0ffe78b96457011b6e9.
Sweep revision: 7c53be7a022a2e5aff14c5a12b56de121b5b2db426399d373b5a9dc9530eecd9.
Retained evaluation:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79a4f02712604715808e696d676cfa472147ba88983e9f6171eddbdfc37cb56c/96b550204ec942849157c2db2bfa51bd973bb56e334279b86e2517c95a580bfa/probability-c348b006166d4c4cbe64ceb8.json
Retained sweep:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ae59f3e2e5168ef6b0e3985cf8a6ccd42580e9eb1f5fe2be694614388be4a99/149d50753e97d01407a18068deb2c780119fb73b53bbf88c5e3cc630946b10a1/probability-dd598b43d37dbdd4e73be7ed.json
The auditor rejected a truncated range payload that declared 1 MiB but decoded to 35197 bytes and could not independently read the complete modifier traces.
No before/after comparison was performed because no source patch exists; the implementation comparison remains mandatory.
The planner's one declared decision probe also returned DECISION_ANALYZED_PARTIAL with complete = false; it is not evidence of complete campaign gating.

Standalone Technology Tree Viewer availability was checked independently of technology tool exposure and successful reference-service calls.
The configured npx package inspected was C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools, version 3.10.0.
Its package binaries are stdio, HTTP and setup; its distributed technology files are backend inspect/render/compare modules, with no standalone viewer entry point, viewer application or HTML app found in the inspected package.
Record standalone Technology Tree Viewer absence as a gap of that inspected package, not as a claim that no separate application exists anywhere on the machine.
Exposed technology routes do not cure that package gap.
No viewer or game was launched.

The current working tree is shared and changed during inspection; line numbers are navigational snapshots.
Final sampled SHA-256 fingerprints were:

| Source | SHA-256 |
|---|---|
| common\scripted_effects\012_africa_gods_effects.txt | D501942F6F2DCB1A70DB3EA5878A0BCE49567B3A55EA183A032DF98200697405 |
| common\scripted_triggers\012_africa_gods_triggers.txt | 7C96397192D9763777C78943B2696B1D67099A57D55D4F1EA23EC8BFB72418C2 |
| common\script_constants\012_africa_gods_constants.txt | BF0F1919D5312BC2B2A760A8D2F1F4BCE9F00428E2C8545F85707C7C192823FE |
| common\decisions\012_africa_gods_decisions.txt | AE732079D66E081B0B6A13FBBE411B42936722009652639106D42D2B2144BFB9 |

## Parent disposition and promotion

The bounded native repair contract is the recommended design.
The parent selected this contract within the full goal on 2026-10-08 and promoted it into Industrial support in the full, technical and decisions/missions/UI specs on 2026-10-09.
The source implementation and its 29 helper and 44 integration cases are recorded in the [integration review](012_gods_industry_integration_review_2026-10-09.md).
The matched AFTER AI comparison completed with partial coverage and 619 unresolved traces.
Native monetary precision, timer behavior and attributable repair remain unproved, so F1 has implemented source with outstanding native acceptance.
Record the parent's acceptance basis separately from later source/native implementation evidence.
Any event-catalog adjustment belongs to the parent's existing workbook owner after actual implementation wording is known.

Completed planning work: identified the CPP-only gap, researched native repair/construction and finite factory precedents, specified the target/tuning/payment/partial/substitute/loss contract, obtained a read-only AI/cost handoff, and recorded required evidence limits.
Remaining evidence limits: complete event/map visual coverage, resolved bound AI scenarios, native monetary precision and native repair/expiry acceptance.
Parent acceptance, source integration and the finite matched comparison are recorded above.
No gameplay, localisation, workbook, assets, Git or game operation was performed by this planner.
No implementation completion is claimed.
No CPP waiver, factory grant, permanent consumer-goods penalty or unapproved fallback is proposed.
The previous phase addendum is implemented; no separate unresolved industrial repair addendum was found in the bounded plan search.
Other completion-audit findings remain with their owners.
Further broad expansion would weaken this repair's scope; finish this accepted industrial consequence rather than add another route.

Skills applied: chaos-redux-event-planning, chaos-redux-improvement-loop, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, and chaos-redux-event-assets for verified icon reuse.
No skill was created or changed.
