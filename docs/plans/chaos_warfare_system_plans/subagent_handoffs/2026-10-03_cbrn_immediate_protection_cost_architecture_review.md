# CBRN immediate protection cost architecture review

Status: read-only source contract review completed; implementation and native acceptance remain parent-owned.
Acceptance basis: parent assignment records the user-approved CBRN overhaul and continued Event 001–040 work, preserving full physical mask issue and allowing canonical discount quotation for PP/service fees and consumed auxiliary materials.
This handoff reviews only `cbrn_emergency_state_mask_distribution` and `cbrn_protect_hospitals_and_utilities`.
It proposes no new cost values, balance targets, timers, native factory variants, or periodic hooks.
Only this handoff was written; no gameplay, staging, commit, server, game, or log operation was performed.

## Findings by purchase

| Surface | Actual existing cost | Outcome and payment scope | Discount/conservation contract |
| --- | --- | --- | --- |
| Emergency state masks | Fixed PP service fee plus the full stock-capped physical issue from five real mask models | COUNTRY ROOT selects STATE FROM; target requires `is_controlled_by = ROOT`, so controller pays stock and PP | Quote PP fee only; never discount physical issue, need, distribution cost/wastage, fitting, filters, or model ledger increments |
| Hospitals and utilities | Fixed PP fee, population-scaled consumed mask material, and population-scaled consumed `support_equipment_1` | STATE FROM; masks/support debit controller; PP debit ROOT; target requires controller = ROOT | PP and consumed auxiliary materials may use accepted canonical whole-unit quotes; retain exact mask-model allocation and refund identity; never add civilian mask ledger crates for discounted consumption |

Emergency uses PP 10 from `constant:cbrn_protection_decision_cost.emergency_distribution_pp` and the live need/stock quote.
Hospital uses PP 10 and stored state costs `cbrn_response_hospital_mask_cost` and `cbrn_response_hospital_support_cost`.
Those state ordinary costs are calculated on verified alert registration from population times their existing ratio, clamped to their existing bounds, then rounded.
This review selects no replacement constants or rounding policy for the ordinary baseline.
The existing hospital constants include `protect_hospitals_factories`, but the reviewed decision has no factory modifier or timer; do not add a factory payment from that unused anchor.

## Existing emergency contract

`common/decisions/cbrn_protection_decisions.txt:341–365` uses the same country gate for availability, custom cost, and the immediate selection recheck, then calls the STATE helper on FROM.
Its cooldown is native `days_re_enable`; its action has no remove/cancel phase.
`cbrn_country_can_pay_emergency_state_mask_distribution` at `common/scripted_triggers/cbrn_protection_triggers.txt:564–573` requires public emergency, inclusive ordinary PP affordability, valid emergency target, and a positive stock-capped crate quote.
Target rules at lines 477–482 require ROOT control, positive population, alert or chemical contamination, no surge-used flag, and an actual effective-coverage gap.

`cbrn_quote_emergency_state_mask_reservation` at lines 546–559 calculates full need with the existing emergency target, wastage, fitting, and filter inputs, then caps the payable physical issue at the five-model ROOT stock total.
No Event 026 ratio is present or appropriate in that physical quote.
`GetCbrnEmergencyMaskDistributionQuote` in `common/scripted_localisation/cbrn_protection_cost_scripted_localisation.txt:78–87` initializes its output before calling the STATE quote and exposes the same crate quantity.
Its PP cost text currently uses the ordinary getter `GetCbrnValueEmergencyDistributionPp` in both normal and blocked cost rows.

`cbrn_complete_emergency_state_distribution` at `common/scripted_effects/cbrn_protection_decision_effects.txt:145–162` initializes `cbrn_distribution_consumed_crates`, calls the physical distributor, and charges PP/publishes surge-used/congestion only if consumed crates are positive.
It has no transaction ID, formal returned action proof, refund branch, or recoverable model issue receipt.
`cbrn_distribute_emergency_masks_to_state` at `common/scripted_effects/cbrn_protection_effects.txt:1889–1895` calls the existing general physical distributor with emergency settings.
The internal distributor at lines 1477–1800 recomputes current effective need, debits each actual model in controller scope, adds usable model counts to state/country civilian ledgers, and updates fitting/filter points and replacement demand.
It distinguishes consumed crates from usable crates; wastage is real, and no adapter should collapse those two results.
The reviewed success condition is positive consumed crates, not an arbitrary replacement threshold or generic payment success.

Minimal adapter flow: fresh context/stock/PP preflight; canonical PP quote; pay and record the PP fee with a still-refundable receipt; call a physical-issue/outcome-only owner helper; require positive actual consumption; publish the existing surge/congestion/maintenance behavior; settle once and report success.
If physical issue produces zero consumption, refund the actual PP fee and do not publish surge/congestion/success.
If PP debit succeeds but recording fails, credit that unrecorded debit explicitly before any physical issue.
Do not call the unchanged existing completion wrapper after adapter payment: it would charge ordinary PP again.
Do not refund physically issued crates while retaining their ledger protection; the current distributor is not a reversible ledger transaction.
Any failure after positive ledger mutation requires explicit committed-outcome handling or a documented blocker, not a generic equipment credit that creates masks.
The immediate branch must keep receipt settlement after the required action proof, rather than copying an adjacent adapter's settlement-before-outcome order without review.

## Existing hospital contract

`common/decisions/cbrn_protection_decisions.txt:428–443` uses STATE `cbrn_state_hospital_payment_ready` for availability and custom cost, then calls `cbrn_apply_hospital_utility_protection` on FROM.
`cbrn_state_can_protect_hospitals_and_utilities` at `common/scripted_triggers/cbrn_protection_triggers.txt:766–771` is the resource-independent target rule: controlled by ROOT, exact alert active, and no secured flag.
The payment gate at lines 773–776 adds ordinary material and PP affordability.
Material affordability at lines 736–748 currently checks aggregate archetypes using meta-trigger insertion of stored state costs.
The debit implementations actually remove concrete mask models and `support_equipment_1`; a new adapter must preflight the concrete dispatch it will perform rather than rely solely on archetype availability.

`cbrn_apply_hospital_utility_protection` at `common/scripted_effects/cbrn_protection_decision_effects.txt:552–574` rechecks the ordinary gate, removes masks oldest-first, removes support equipment, compares both actual completed totals to their requested costs, then debits ordinary PP and grants the existing secured flag plus 14-day protected modifier.
It does not call the civilian mask distributor, add issued-mask crates, update civilian model/fitting/filter ledgers, or reserve masks in an escrow.
Thus these masks are consumed hospital-protection materials in the present mechanic, distinct from the emergency action's physical civilian issue.
The state modifier itself remains unchanged; its consumer effects are not redesigned by cost adaptation.

The current hospital action has no rollback when a partial mask/support debit fails the final comparison, no persistent transaction receipt, and no explicit returned success proof.
Its `cbrn_mask_stock_debit_completed` and `cbrn_support_equipment_debit_completed` are first created inside called helpers rather than initialized in the outer hospital frame.
The source-only lifetime risk is documented by offline Data structures and the shared receipt API; actual engine behavior was not executed here.
`cbrn_debit_mask_stockpile_oldest_first` at `common/scripted_effects/cbrn_protection_effects.txt:1898–1964` exports an aggregate completed amount and reusable model scratch, not a five-model durable refund breakdown.
An aggregate credit cannot restore the model identity of this debit.
`cbrn_debit_requested_support_equipment` at `common/scripted_effects/cbrn_protection_decision_effects.txt:17–32` caps and rounds its request against concrete support model stock; it does not refund earlier costs.

Minimal adapter flow: validate the existing resource-independent target and required stored cost variables; quote PP, one aggregate hospital mask-material cost, and support cost; allocate the quoted aggregate masks in the same oldest-first model order; check every component before the first debit; pay and record concrete model components and PP/support under one payer receipt; publish only the paid-outcome-only state helper; settle on confirmed owner outcome; otherwise refund recorded actual payments once.
If the current component debit succeeds but its receipt record fails, credit that unrecorded component explicitly, then refund prior recorded components.
Never report rollback successful without the credit/refund result checks.
Do not call the unchanged ordinary hospital helper after discount payment: it would recheck ordinary affordability and debit masks/support/PP a second time.
Extract the flag/modifier publication to an outcome-only helper guarded by target context and verified payment, not by the now-consumed stock balance.

Quote the mask aggregate once, then allocate the resulting whole-unit cost across models.
Do not discount or round each model independently: that changes the total quote and makes model mix a price exploit.
Use distinct receipt component IDs for the five concrete gas-mask kinds and record each actual model payment.
Maintain aggregate ordinary and aggregate quoted totals in the receipt decomposition; where discounted affordability provides fewer models than the ordinary counterfactual price, store the unpaid ordinary remainder as accounting only, using the framework's documented participating/zero-paid component contract.
Never debit that counterfactual remainder.
Shared concrete mask resource kinds already exist, so no shared resource dispatcher or central framework extension is needed.
Refund restores model quantities, while native stockpile credit cannot reconstruct original producer or design-variant provenance; carry that documented framework limitation forward.

## Proposed helper map and ownership boundaries

Proposed names below are local recommendations, not implemented identifiers.

| Local helper | Scope, inputs, defaults | Outputs, side effects, direct call sites |
| --- | --- | --- |
| `cbrn_quote_emergency_distribution_payment` | COUNTRY, ROOT payer/FROM state; ordinary PP constant and full existing physical quote; explicit whole-unit quantum | Dedicated PP cost/valid/affordable plus unchanged physical issue quote; temporary-only; decision gates and PP display getter |
| `cbrn_apply_emergency_distribution_purchase` | COUNTRY ROOT/FROM state; fresh target validation and enclosing result storage | PP receipt, one physical issue, outcome proof, exact PP rollback on zero issue; immediate complete effect |
| `cbrn_complete_emergency_distribution_paid_outcome` | STATE FROM, ROOT = controller; caller-created consumed/usable result storage | Existing full physical issue and success-only surge/congestion/maintenance, no PP debit; adapter callback |
| `cbrn_quote_hospital_protection_payment` | COUNTRY ROOT/FROM state; required stored mask/support cost variables, ordinary PP; explicit quantum one | Dedicated PP/mask/support costs, validity/affordability and oldest-first allocation; temporary-only; both decision gates and all three cost getters |
| `cbrn_apply_hospital_protection_purchase` | COUNTRY ROOT/FROM state; fresh context, quotes and concrete allocation; fail-closed results | One exact payer receipt, concrete component debits/refunds, paid outcome proof; immediate complete effect |
| `cbrn_complete_hospital_protection_paid_outcome` | STATE FROM; ROOT/controller equality and confirmed payment supplied by caller | Existing timed secured flag/dynamic modifier, explicit proof; no resource gate or debit; adapter callback |

Keep new local quote/payment helpers in a bounded CBRN owner module or the existing CBRN protection decision modules, with matching documentation.
The parent owns the direct call sites in `common/decisions/cbrn_protection_decisions.txt`, the two relevant existing trigger adapters, the two owner effects, cost getters, and matching English cost text.
Register new helper documentation in `common/scripted_effects/chaosx_dynamic_effects.md` as required by repository helper guidance.
Only the Event 026 owner should update its explicit coverage registry after implementation/evidence exists; this review does not promote the four parent-reported unadapted rows to implemented.
`026_black_friday_effects.txt`, `026_black_friday_triggers.txt`, and all shared universal source/quote/payment/refund implementations are examples or dependencies, not this reviewer's edit surface.
Leave adjacent shelter, procurement, timed projects, and Protective Aid source behavior untouched.

The existing shelter adapter at `common/scripted_effects/026_black_friday_effects.txt:3177–3340` demonstrates concrete support/train payment, one receipt, and component refund, while its trigger-side quote is at `common/scripted_triggers/026_black_friday_triggers.txt:469` onward.
Mirror its source eligibility, quote, and receipt concepts only after reviewing result lifetimes and commit order; do not copy its body as proof of a complete transaction.

## Public quote/receipt return contract

`common/scripted_effects/chaosx_universal_cost_effects.md:150–198` requires ordinary current cost plus family mask and rounding quantum, emits final/displayed/saved cost, primary source and source count, and marks malformed/nonrepresentable quotes invalid.
Use PP family for fees and equipment family for consumed support/mask material, as the adjacent CBRN adapters do.
During an active Event 026 sale require both its global active predicate and its registered canonical source; a missing source or invalid quote fails closed.
Outside the sale retain the current ordinary owner costs and ordinary gameplay.
No bespoke ratio calculation, hardcoded half-price math, silent quote clamp, or fallback cached price is needed.

Each enclosing caller declares every output it reads before invoking the helper.
This applies independently to decision gates, complete-effect callers, quote adapters, and scripted-localisation trigger blocks.
An initializer scripted helper that first creates the values internally does not establish outer storage.

| Called API | Required caller-created outputs when read |
| --- | --- |
| `black_friday_quote_custom_cost` | `black_friday_quote_final_cost`, `black_friday_quote_valid`, plus ratio if used; explicit requested quantum input |
| `universal_cost_quote_integer` | `universal_cost_quote_final_cost`, displayed/saved cost, valid, source count, primary source ID, ratio if read |
| `universal_cost_check_quote_affordable` | `universal_cost_quote_affordable` |
| `black_friday_allocate_owner_transaction` | `black_friday_owner_transaction_id` |
| `universal_cost_pay_component` / `universal_cost_credit_component` | `universal_cost_payment_result` / `universal_cost_credit_result` |
| `universal_cost_record_transaction` | `universal_cost_record_transaction_result`, component index if read |
| `universal_cost_settle_transaction` | `universal_cost_settle_transaction_result` |
| `universal_cost_refund_transaction` | `universal_cost_refund_transaction_result`, refunded total, unhandled total |
| Physical distribution / existing debit helpers | `cbrn_distribution_consumed_crates`, usable crates if read; mask/support completed totals if read |
| New owner wrappers | Dedicated action/payment success and every quote/affordability/allocation value used by caller |

Initialize success/validity/affordability to fail-closed values and copy each component quote to dedicated scratch before the generic final output is reused for the next component.
Reset result storage for each new operation; do not reset inherited refund cursors or accumulated refund totals between component callbacks.
The receipt contract uses an owner-allocated ID with allocation proof, one distinct component ID per paid model/resource, quoted equal to actual-paid per component, and one settle or refund per logical transaction.
Zero/negative payment amounts are documented successful no-ops; that does not make a no-op emergency distribution a successful action.

## Constants, event targets, cleanup, and migration

Reuse all existing ordinary fee, ratio/bound, effect duration, physical target/wastage/filter, and cooldown constants.
There is no new tuning table or balance target in this recommendation.
Use quantum one from the shared framework for discounted fee/material amounts; preserve existing rounding for ordinary population-scaled hospital anchors.
Retain the existing emergency one-surge flag and hospital secured-flag lifecycles, including exact-alert registration cleanup.

ROOT/FROM already carry the payer/state for each immediate action, so no global event targets or persistent target pointers are needed.
If a regular event target makes a nested callback clearer, it is local to the immediate chain and needs no durable cleanup.
Payer transaction arrays retain accounting proof; settle successful immediate transactions once after action commitment and refund failed precommit transactions through recorded actual paid components.
Clear unconsumed allocation proof if failure occurs before the first receipt row.
Do not add the Protective Aid selected-variant/cooldown scheme to these immediate actions.

Migration order: isolate paid-outcome-only owner paths; establish pure quote/eligibility helpers and enclosing output initialization; implement preflight/payment/record/refund/commit wrapper; switch the two direct decision gates/callbacks; replace fee/material cost getters with fresh canonical component quotes while leaving emergency crate getter physical; update matching cost text and helper docs; then update Event 026 coverage status with parent validation limits.
For hospital ordinary costs, the current API uses alert-cached state cost fields.
Do not recompute those fields only at payment while displaying old values; either consistently retain the existing alert anchors in display/gate/payment or explicitly mirror the live ordinary computation at all three surfaces within accepted parent scope.
Resource-independent target visibility must remain separate from affordability so discounted affordability can expose valid actions without requiring ordinary-cost stock first.

## Source references and meaningful checks

Source review checked both exact decision callbacks, direct owner debit/outcome ordering, concrete stock dispatch, physical issue/model ledgers, affordability scope, current cost display tokens, the universal quote/receipt contract, and the adjacent shelter precedent.
It found hospital partial-debit/no-rollback exposure, hospital outer-output lifetime exposure, and double-debit risk from reusing either unchanged ordinary owner effect after adapter payment.

Offline reference sections read for this review are `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2253–2256` for native stock edits, `Triggers - Hearts of Iron 4 Wiki.md:723` and `1516` for PP/equipment comparisons, plus the previously read Data structures temporary lifetime section at 437–442, Scopes ROOT/FROM section at 260–263, Decision modding immediate/custom-cost sections, and Localisation scripted-localisation section at 656–681.
Installed reference sections are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:1153–1170`, `1252–1264`, `1854–1861`, and `triggers_documentation.md:3835–3841`, `4547–4554`.
The installed constants schema/support rules read in the preceding handoff remain applicable to these shared costs.
Vanilla source precedent is installed `common/decisions/_generic_decisions.txt:272–298`, which checks stock in a decision and changes concrete equipment in its complete effect.
Vanilla does not provide this owner-specific conserved issue and multi-cost rollback contract; the existing local CBRN ledger and universal receipt contract are the relevant implementation precedents.

Connected `ALL_TOOLS` contains no `mcp__hoi4_agent_tools__*` routes, including reference context/search/read, source lookup, script validation, and probability inspect/evaluate/compare.
No second server/client was started.
The parent owns its isolated SDK client and mandatory eventual MCP evidence.
No event chain, focus, scripted GUI, or map-data change is proposed; these are unchanged native state-target decision surfaces.
AI willingness and PP hint validation remain parent/probability-auditor work; source eligibility/refund review is not AI scoring evidence.

Parent checks should cover exact ordinary and discounted PP balances; masks available but PP missing; zero physical emergency need; partial emergency stock; oldest-first model conservation with full/quarter sale; no emergency mask discount; hospital affordable only at discounted stock; aggregate-once mask rounding across mixed models; concrete support shortfall despite archetype availability; later payment/record failure restoring exact earlier model quantities; repeated refund/settlement; missing active sale source; invalid canonical quote; stale target/control/alert; and action proof absent despite payment success.
Native resource mutation, exact model stockpile effects, script-call lifetime, action execution, and rollback were not executed by this reviewer.
The generic engine does not provide atomic rollback over physical ledger mutations; emergency issue commitment must be treated explicitly.
No design simplification is proposed, and none was implemented.

## Sampled worktree identities

These SHA-256 identities describe sampled bytes in a concurrently edited worktree, not immutable before-source fixtures or committed revision proof.

| Source | SHA-256 |
| --- | --- |
| `common/decisions/cbrn_protection_decisions.txt` | `1cea14ecf1bd15929d90a15fca5c115c529d5edc3af936eb888fa2eac9d91d03` |
| `common/scripted_effects/cbrn_protection_decision_effects.txt` | `eacb3a35edbf6aeb4d095dbcb14c4030e9b5a6bf554c4d8822903a2bdf273818` |
| `common/scripted_effects/cbrn_protection_effects.txt` | `ff04b3decb07dd1fa7fd21ce9070d6de1622a320fbb960bc2380126ad2c3dfce` |
| `common/scripted_triggers/cbrn_protection_triggers.txt` | `a681319bf4f59c64cb270e3b9b89f07de07d8c2f6f971ae5edc893521c17f698` |
| `common/scripted_localisation/cbrn_protection_cost_scripted_localisation.txt` | `8de563a631715d94a7b6e130acb9ac457e7a242491c0353a1ff79972a863713f` |
| `localisation/english/cbrn_protection_l_english.yml` | `0f5f7cae5fcb49dd8bf48dd6bf531db66d906116649487fdcf8e341d3497529c` |
| `common/scripted_effects/chaosx_universal_cost_effects.md` | `73a959729dfcdba65e69839657ad2b8d02b57793d09b5f747b9a821c2edbc4f1` |

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or updated.

## Final read-only review of implemented owner adapters

Disposition: parent implementation resolves the earlier direct-double-debit, physical-emergency-discount, aggregate-model-refund, and nested-output concerns for these two orders.
One bounded pre-receipt allocator cleanup finding remains in the source sampled below.
This section is an implementation review, superseding earlier proposed helper names where the parent chose different names.
No gameplay edits, staging, commits, or new design/tuning proposals were made by this reviewer.

Reviewed implementation files are `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt`, `common/scripted_effects/cbrn_immediate_response_cost_effects.txt`, their delegated old gates/state entry points, and the matching immediate cost-localisation module.
The current universal receipt implementation/documentation and Event 026 quote/typed-proof code were read as dependencies; other owners' edits were preserved.

### Caller storage and current source eligibility

`cbrn_quote_immediate_response_component` declares generic Black Friday result storage before invoking `black_friday_quote_custom_cost` and explicitly forwards `universal_cost_quote_valid` before native quoted affordability.
The enclosing fee/bundle helper declares its component result storage before calling the component quote.
Country payment gates declare the validity/affordability outputs they read after the fee/bundle returns.
Order callbacks declare the fee/price/model outputs they need after quote return, plus native allocator and settlement results before those calls.
The component payer declares native debit, record, and unrecorded-credit results; the refund helper declares its three public refund outputs.
`cbrn_response_all_paid` is created in the order before the component helper modifies it, preserving the failure latch through all seven hospital component calls.
Emergency physical consumed/usable outputs exist in the order frame before the nested distributor runs.
The matching getters initialize their displayed amount and tested validity/affordability fields before invoking their quote helper.
No new missing outer storage was found on the inspected quote/payment/record/settle/physical-consumption return paths.

A globally active sale requires registered source 26 before its quote can become valid.
Invalid/missing sale source leaves affordability false; ordinary source-zero orders retain ordinary fees.
The hospital bundle prices the mask aggregate once, allocates that whole quote oldest-first across the five real models, and separately quotes concrete support model 1.
Its native resource affordability uses declared quote validity.
The observed quote path therefore avoids the prior ordinary-resource prerequisite and per-model-rounding traps.

### Typed receipt and exact model contract

`cbrn_pay_and_record_response_component` forwards the four typed achievement inputs before EVERY record call, including the zero-paid model rows.
Resource kinds are distinct component IDs within each order: PP, concrete support, reconditioned mask, and mask models 1–4.
Every row records the actual quoted amount as actual paid, preserving model identity for native refund.

Emergency metadata is family `political_power`, basis `primary_component`, exact primary ID PP 1, and member one on its sole PP component.
Hospital metadata is family `state_project`, basis `primary_group`, primary ID zero, PP member zero, and support/mask members one.
The required tuple remains consistent across each receipt, while membership selects only hospital materials for its achievement claim.
The first model's ordinary-only counterfactual remainder restores the ordinary aggregate mask total without debiting or issuing that remainder.
For example, an ordinary mask fee ten quoted to five and paid entirely from basic masks yields a reconditioned accounting row ordinary five/paid zero plus a basic row ordinary five/paid five: selected ordinary ten, paid five, actual native basic debit five.
The current proof validator accepts nonnegative per-row ordinary/paid amounts, including these zero-paid rows, and requires positive exact selected aggregate equality.
Its checks at `026_black_friday_effects.txt:140–215` therefore agree with this decomposition.

The old state entry points now delegate through ROOT to the country order, avoiding ordinary duplicate debits.
Hospital pays and records every component before settlement/outcome.
An unrecorded debit is credited to the same concrete kind if record rejects; prior recorded components are refunded by their actual stored kinds/amounts.
Settlement failure runs the unfinished refund path before any hospital outcome.
On settlement success the hospital outcome is an unconditional secured-flag/modifier publication; it contains no affordability recheck or second debit.
There is no inspected source rejection branch after successful hospital settlement that would consume payment without the source outcome call.
Native flag/modifier execution remains a separate unexecuted boundary.

### Emergency commitment and post-issue receipt validity

The physical issue remains the existing full distributor; no canonical discount enters its need, wastage, model, fitting, filter, or ledger calculation.
Only a positive `cbrn_distribution_consumed_crates` result marks the payer's receipt ID committed and publishes the original surge/congestion outcome.
Zero physical issue invokes the fee refund path and leaves the success-only outcome absent.
The owner refund helper refuses to refund a committed emergency ID, preventing a retained civilian ledger issue from being paired with a refunded service fee.
Achievement publication occurs only after settlement success, with PP-only permission and no post-expiry allowance.
The committed-ID marker is retained as transaction-specific proof, not a shared national action flag.

No inspected physical distributor, snapshot/source-modifier helper, or paid emergency outcome writes universal receipt arrays, typed metadata, allocator proof, or `cbrn_response_transaction`.
The paid outcome's maintenance call only sets its maintenance-active flag and schedules `cbrn_protection.1` with the existing positive delay (`cbrn_protection_effects.txt:2425–2431`), so it does not run a same-chain callback before settlement.
The emergency order reassigns `universal_cost_transaction_id` from its enclosing `cbrn_response_transaction` immediately before settlement, eliminating reliance on generic scratch retained from payment.
Thus no normal source path that invalidates a freshly recorded emergency receipt between issue and settlement was identified.
The feared late settlement failure is a defensive corrupted-state/native-boundary case, not an observed source bug or a reason to remove the real paid issue.
If that case occurs, source behavior retains committed protection and fee, gives no achievement credit, and forbids the owner's ordinary refund path.
This review does not assert that native execution, save persistence, or an unrelated external receipt mutator was validated.

### Remaining bounded source finding

If the first component payment or record fails before a receipt row is created, `black_friday_allocate_owner_transaction` has already written `universal_cost_allocated_transaction_id_@var:cbrn_response_transaction`.
The unfinished refund helper calls generic refund but contains no allocation-proof cleanup.
Generic refund does not clear that proof when no row exists; record consumes it only after creating a receipt row.
The source therefore retains an unused allocation token on this pre-receipt failure path.
This is a local cleanup finding, not a discovered free-coverage path: first-component failure prevents physical emergency issue and prevents every hospital outcome.
Recorded later-component failures still use the exact receipt refund path.
The parent must disposition or repair this owner cleanup before treating failure cleanup as fully closed.

Credit/refund result variables are initialized, but the owner does not expose or check their returned values after invoking them.
The reviewed orders use only supported concrete native kinds and nonnegative paid amounts, so no ordinary source dispatch failure was identified here.
The current native helper reports dispatch success after issuing the resource effect, rather than measuring the engine's resulting stockpile balance.
Accordingly, exact engine restoration is still native validation uncertainty; this review does not claim runtime rollback proof merely from the source calls.

### Follow-up evidence and validation limits

This review checked current caller result lifetimes, active-source gating, aggregate model decomposition, typed proof membership, zero-paid counterfactual rows, unrecorded-credit/recorded-refund split, delegated scopes, post-issue mutation paths, and settlement/outcome ordering.
These are source contract findings, not executed scenario outputs.
No SDK/MCP server or client was started; the parent owns its isolated SDK client 3.6.0 and the same-scenario probability audit/compare evidence.
The parent's scenario results should carry the allocator failure cleanup disposition and native resource/ledger/receipt limits separately from ordinary source success evidence.

Sampled SHA-256 identities for this final review are:

| Source | SHA-256 |
| --- | --- |
| `common/scripted_triggers/cbrn_immediate_response_cost_triggers.txt` | `fdae491b5c113092b63518d8a0217e2c209e25bb18705a583fd7aa0610abde4c` |
| `common/scripted_effects/cbrn_immediate_response_cost_effects.txt` | `5fd2b437db1adbb6e0b488948c9419f6a990fb64841255d82e3a1752f93c70b3` |
| `common/scripted_effects/chaosx_universal_cost_effects.txt` | `d2d04617d66ccb6dbd240e82cca8b1fabde24a2fec7fadc9bfa54c6de768d7f8` |
| `common/scripted_effects/chaosx_universal_cost_effects.md` | `48ca540cf0e44a91ce329849aba36fa4895c64d0627f1ada5d3a72fba7b8e0b2` |
| `common/scripted_effects/026_black_friday_effects.txt` | `02f16b293e6aa4c33d85d4b123a12126343b5547d7393dd07ad451a7f98b53fc` |
| `common/scripted_triggers/026_black_friday_triggers.txt` | `53783b7a3d8b125eb1c24bef6f59cdfd6b5265b89a0f6cfc67e45948afb43d5b` |

The shared worktree remained concurrently edited; these samples identify reviewed bytes, not immutable baseline or committed revision proof.

### Allocator cleanup follow-up: resolved in source

The parent corrected `cbrn_refund_unfinished_response_transaction`, and this reviewer checked the actual current file.
After the refund attempt, `common/scripted_effects/cbrn_immediate_response_cost_effects.txt:94–99` clears the unused targeted allocation proof when no normal transaction row mapping exists.
The committed emergency guard still excludes actual issued transactions from ordinary refund.
The source allocator cleanup finding above is therefore resolved; its old sampled source hash predates this correction.
The current helper also preserves failed unrecorded native credits for retry and records rejected/partial refund status, improving the earlier result-observability limit.
Native resource restoration remains unexecuted by this reviewer.
The parent's reported repair of 14 owned YAML keys was outside this allocator check and is not independently verified here.
