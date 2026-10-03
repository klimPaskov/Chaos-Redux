# Protective Aid native factory variant architecture review

Status: source contract review completed; implementation belongs to the parent; native execution and MCP evidence remain unresolved.
Scope: Protective Aid native factory commitment from two to one during an eligible Event 026 sale, preserving full model-specific mask escrow, refund, delayed delivery, and PP receipt settlement.
Acceptance basis: parent assignment states user approval of CBRN and full-shipment escrow/reserve/refund, and requests the two native decision variants plus donor/state shared cooldown.
The architecture names below are proposed local names, not claims that implementation already exists.
Only this handoff was written by this reviewer.
No gameplay files, staged content, commits, game sessions, or logs were changed or accessed for validation.

## Concrete recommendations

1. Preserve `cbrn_deploy_protective_aid` and add `cbrn_deploy_protective_aid_sale`, sharing public name, description, icon, duration, callbacks, and willingness logic.
Give their native `civilian_factory_use` definitions static ordinary/sale values of two/one from the existing generated file-local constants, with canonical source values in `cbrn_occupation_decision_cost`.
2. Pre-click eligibility must use the live canonical factory quote, require an inclusive available-factory check for the matching native quote, and reject every quote outside the supported native values.
Never clamp a different quote to one or two.
An active global sale with a missing registry source or invalid quote must fail closed.
3. Stamp `cbrn_external_aid_purchase_cooldown_@ROOT` on `FROM` unconditionally at native selection, before transaction guards, for `constant:cbrn_occupation_timing.protective_aid_reenable_days` through an initialized temporary duration and `days = var:<duration>`.
Both pre-click IDs check the same targeted state flag.
The post-click transaction recheck deliberately omits this freshly stamped cooldown and the factories already reserved by the native decision.
4. Preserve selected ordinary/sale state markers while their escrow is active, including after Event 026 expiry.
Use the marker together with the stored-donor equality check for variant visibility; do not expose the other ID as an active version of the same project.
Do not put live sale eligibility in cancellation or completion requirements.
Clear both selection markers through the existing common reservation-close helper, while retaining the cooldown until its own expiry.
5. Establish caller-owned temporary outputs before every nested PP quote/payment call and every scripted localisation getter that reads those outputs.
The existing Event 026 generic quote helper explicitly requires this contract.
Initialize in the enclosing caller that subsequently reads the result; a new initializer helper whose variables are first created internally does not solve the boundary problem by itself.
6. Copy the factory result to dedicated CBRN temporary outputs before PP quotation overwrites generic `black_friday_quote_final_cost`.
Reset the quantum input before PP quotation so the factory override cannot leak into it.
7. Extract only the duplicated selection, completion, cancellation, and preflight logic into the planned local CBRN modules.
Keep the shared Event 026 quote/payment/receipt code owned by its current framework editor.
Existing general dynamic helpers contain no matching native targeted-decision transaction helper; the local feature module is justified.

## PP quote and payment boundary finding

`common/scripted_triggers/026_black_friday_triggers.txt:157–205` initializes generic outputs inside `black_friday_quote_custom_cost` and states at lines 158–159 that the OUTER caller must predefine every output read afterward.
Its active branch delegates to the aligned exact quote producer and copies `final_cost`, `valid`, and `composed_ratio` back.
`black_friday_quote_cbrn_external_aid_pp_fee` at lines 1535–1561 and `black_friday_can_pay_cbrn_external_aid_pp_fee` at lines 1563–1567 currently initialize the aid outputs only inside their nested adapters.
`GetCbrnExternalAidPoliticalPowerQuote` in `common/scripted_localisation/cbrn_protection_cost_scripted_localisation.txt:25–30` directly invokes the PP adapter without outer initialization.
These are concrete boundaries the parent should repair in CBRN callers without editing the dirty Event 026 framework files.

Initialize the following before the nested PP adapter/can-pay/payment path:

| Temporary | Initial value | Purpose |
| --- | --- | --- |
| `black_friday_cbrn_external_aid_pp_cost` | `constant:cbrn_occupation_decision_cost.protective_aid_pp` | Outer PP quote result storage, ordinary value 25 |
| `black_friday_cbrn_external_aid_pp_quote_valid` | zero | Fail-closed PP validity output |
| `black_friday_cbrn_external_aid_pp_affordable` | zero | Fail-closed PP affordability output |
| `black_friday_quote_final_cost` | ordinary PP cost | Generic nested result used by PP adapter |
| `black_friday_quote_valid` | zero | Generic nested validity output |
| `black_friday_quote_composed_ratio` | zero | Generic ratio output, if read or retained |
| `black_friday_quote_requested_quantum` | zero | Reset any preceding factory override |
| `black_friday_cbrn_external_aid_pp_payment_success` | zero | Selection caller must own/reset this before escrow and payment branches |

For factory quotation initialize its dedicated cost and validity outputs, generic final cost to ordinary two, generic validity/ratio to zero, ordinary cost to two, family to `constant:universal_cost_family.factory_commitment`, and requested quantum to one.
Require `black_friday_is_active` plus `universal_cost_source_query_id = constant:universal_cost_framework.black_friday_source_id` with `universal_cost_source_is_active` before a sale request can pass.
The registry membership trigger is defined in `common/scripted_triggers/chaosx_universal_cost_triggers.txt:9–18`.
Factory family 512 is declared at `common/script_constants/chaosx_universal_cost_constants.txt:102`.
After the canonical producer returns, copy its native-compatible result into distinct CBRN variables and use those copied values for the variant check and factory requirement.
For nominal half and quarter sale ratios, mathematical ceiling with quantum one gives `ceil(2 × 0.5) = 1` and `ceil(2 × 0.25) = 1`.
This arithmetic checks the intended values; it is not evidence that native HOI4 executed the helper.

`black_friday_pay_cbrn_external_aid_pp_fee` in `common/scripted_effects/026_black_friday_effects.txt:4132–4184` resets its success internally, calls PP affordability, checks the target escrow/donor, allocates and records the PP transaction, and writes its transaction ID and sale sequence to the state.
The outer selection must initialize the PP result storage before this call and must use the outer success value for registration/refund branches.
The ordinary path debits the fixed PP fee and marks payment successful; its current caller must have performed the immediate PP recheck first.
Do not add a second manual factory debit or make the conserved respirator transfer a discounted spend.

## Proposed helper map

| Proposed helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `cbrn_protective_aid_sale_source_is_active` | COUNTRY; global flag and registry source query | Boolean; temporary query only | Variant presentation and preflight |
| `cbrn_protective_aid_quote_factory_commitment` | COUNTRY; outer quote storage; ordinary two, family 512, quantum one | Dedicated factory cost and validity; no native reservation | Preflight, immediate click recheck, factory display |
| `cbrn_protective_aid_ordinary_payment_ready` / `cbrn_protective_aid_sale_payment_ready` | COUNTRY, ROOT donor, FROM state | Boolean; require country, stock, PP, target, shared cooldown, inclusive factories, matching quote | Both `available` and `custom_cost_trigger` blocks |
| `cbrn_protective_aid_apply_selection` | COUNTRY, ROOT donor, FROM state; requested variant ordinary one/sale two; enclosing result storage | Stamp cooldown; fresh recheck; reserve full five-model receipt; pay PP; publish selected marker/project flag/count only after success; refund masks on payment failure | Both `complete_effect` blocks |
| `cbrn_protective_aid_complete_selection` | COUNTRY, ROOT donor, FROM recorded state; enclosing completion-proof storage | Common close, existing delivery/refund, existing success-only delayed PP receipt settlement | Both `remove_effect` blocks |
| `cbrn_protective_aid_selection_should_cancel` | COUNTRY, ROOT donor, FROM state | Boolean from existing continuing-country, stored-donor, and continuing-target contract; no free-stock/factory/live-sale check | Both `cancel_trigger` blocks |
| `cbrn_protective_aid_cancel_selection` | COUNTRY, ROOT donor, FROM recorded state | Common close, stored-donor model refund, clear project marker, failed PP receipt settlement | Both `cancel_effect` blocks |
| Existing `cbrn_occupation_close_external_aid_reservation` extension | STATE with stored donor receipt | Idempotent donor count decrement; clear both variant markers; retain cooldown, donor/model receipt until distribution/refund consumes them | Completion, cancellation, and existing control-transfer refund callers |

The proposed new files are `common/scripted_effects/cbrn_protective_aid_decision_effects.txt` and `common/scripted_triggers/cbrn_protective_aid_decision_triggers.txt`.
Document the contracts, defaults, outputs, side effects, call sites, and usage in the matching feature documentation and register the helper documentation in the dynamic effects documentation where appropriate.
This review creates no helpers without call sites.

## Constants, lifecycle, and migration

Reuse the existing ordinary PP 25, factories two, duration 21, and re-enable 90 constants.
The parent worktree already contains `protective_aid_sale_factories = 1` and `protective_aid_sale_pp_ai_hint = 1` when sampled; their presence is implementation evidence owned by the parent, not this reviewer's edit or AI validation.
Do not invent a ratio table separate from the canonical discount registry.
Use constants for variant request enumeration where existing framework one/two values already fit the contract.

Keep existing regular event targets `cbrn_external_aid_transaction_target_state` and `cbrn_occupation_target_state` local to their callback effect chains.
Keep the supplier target recreated by the existing delivery helper and the durable donor pointer/model counts/transaction ID/sale sequence on the state.
No global target, national blanket cooldown, daily loop, or worldwide hook is necessary.
The shared cooldown survives failed/stale native selection, cancellation, completion, and sale expiry, preserving the native after-selection cooldown intent across both IDs.
Its location on the target state plus donor tag suffix gives a donor/state key; another target or another donor has a different key.
One active escrow still serializes simultaneous suppliers to the same state under the existing state active flags.

Migration order: establish quote/preflight contracts; extract the current callback bodies into the local module; switch the ordinary ID to those calls; add the sale ID; add selected-marker visibility and common close cleanup; add outer initialization to PP and factory display getters; update helper docs and review both variants together.
Preserve the original selection's positive escrow-completed guard, PP-success registration, payment-failure mask refund, completion proof, and delayed receipt settlement order.
Preserve the original cleanup's idempotent counted flag and stored-donor refund behavior, including retained recovery receipt when the donor does not exist.
Current escrow documentation is `common/scripted_effects/cbrn_scripted_effects.md:735–758`.

## Source evidence and limits

- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:270–280`: complete effect starts on selection and `days_re_enable` delays reappearance after taken.
- Same source lines 337–355: native timer/modifier lifecycle and distinct cancellation callback.
- Same source lines 584–586: state targeting uses FROM as the state scope.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:118–125`: state flag equivalence and targeted flag support for `@ROOT`.
- Same source lines 303–305 and 437–442: local event target lifetime, outer-created temporary helper outputs, and unscoped temporary storage.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4683–4695`, `Triggers - Hearts of Iron 4 Wiki.md:2359–2371`, and `Localisation - Hearts of Iron 4 Wiki.md:656–681`: helper definitions and temporary values in scripted-localisation trigger blocks.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:216–245` and `common/script_constants/documentation.md`: shared constants schema and explicit support limitation.
- Installed `documentation/effects_documentation.md:6496–6503`, `7716–7723`, and `7820–7839`: event-target, STATE flag, and temporary-variable commands.
- Vanilla `common/decisions/_generic_decisions.txt:155–181` under the installed game: timed decision with static civilian factory modifier.
- Mod precedent `common/decisions/cbrn_diplomacy_decisions.txt:178–237` and `284–345`: ordinary/sale native factory variants with shared public name and selected-variant visibility retention.
- Current Protective Aid `common/decisions/cbrn_occupation_decisions.txt:89–240`: 21-day native operation, 90-day cooldown, post-reservation factory omission, conserved escrow, payment refund, completion and cancellation.

Connected metadata exposes no `mcp__hoi4_agent_tools__*` tools.
Exact missing routes for this review are `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.script_validate`, `hoi4.probability_inspect`, and the probability evaluation/compare routes.
No MCP artifact URI, server revision, native inspection, or scenario execution exists for this handoff.
Local source reading is recorded as source evidence only.
There is no linked focus, scripted GUI, event callback, or map-data modification in this bounded helper proposal; the on-map decision position is the unchanged native state-target surface.
AI willingness/source eligibility evidence belongs to the parent's probability auditor and remains blocked by the absent route.
Copying willingness blocks or changing the PP hint is not probability validation.

## Meaningful review scenarios and remaining uncertainty

The source contract was checked for factory-result overwrite by PP quotation, outer temporary storage, stale success values, native factory reservation ordering, variant-switch cooldown bypass, sale expiry during a running shipment, stored-donor cleanup ordering, and duplicated shipment debits.
The findings above require outer initialization and a post-click gate without cooldown/free-factory checks.
No engine or live-consumer scenarios were executed.

Parent validation should retain cases for ordinary two factories at exactly two available, sale one at exactly one available, half/quarter ratios producing one, an unsupported composite quote failing closed, active global sale with missing registry entry failing closed, and sale expiry during a selected project preserving its native one-factory commitment.
Also retain cases for same donor/state cooldown across ID switches, independent other state/donor keys, stale click with no new escrow or PP charge, PP-payment failure refunding the original five-model counts, successful completion after expiry settling the stored PP sequence once, cancellation returning unused model counts, and double close leaving the donor count nonnegative.

Native cooldown timing is inferred from the offline decision rule and the existing timer structure; the exact engine interaction between a timed decision and `days_re_enable`, failed selections, target enumeration, and variant visibility remains unexecuted.
Installed state-flag documentation is terse and does not independently document the complete timed targeted flag syntax; the targeted/time behavior is supported by offline data structures, repository rules, and existing usage, with runtime acceptance unresolved.
This reviewer did not inspect the universal quantizer implementation end-to-end or validate PP receipt achievement behavior beyond the owner call contract.
No design simplification is proposed; missing native/MCP proof and parent implementation are explicit remaining work.

## Sampled source identities

These hashes identify sampled worktree bytes, not immutable baseline snapshots or committed revisions.
Other owners were editing the shared tree during this review; reread exact relevant definitions before final integration.

| Source | SHA-256 |
| --- | --- |
| `common/scripted_triggers/026_black_friday_triggers.txt` | `6ffc13f17e09feebf68c35aec7ec4424ed6540f9771d4f1d10eaff05afb5f716` |
| `common/scripted_effects/026_black_friday_effects.txt` | `798a111c80407e4a5d5259df45660d04688474e907c6bfeb21033e7f77cba49e` |
| `common/decisions/cbrn_occupation_decisions.txt` | `f2520421e40f0e3cdb58a144b840ed7e723f2aa805c3b0d4991d621a7f722b52` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Installed `documentation/script_concept_documentation.md` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `documentation/effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or updated by this read-only contract review.
