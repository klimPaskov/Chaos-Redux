# Occupied distribution transaction helper handoff

Status: implemented helper package; parent native decision wiring, localisation, lifecycle scenarios, audit, and commit remain pending.
Acceptance basis: the parent task reports user approval of full CBRN/Event 026 implementation and the exact architecture in [the accepted architecture review](2026-10-03_cbrn_export_occupied_cost_architecture_review.md).
Ownership: only the three new occupied transaction script files and this handoff were edited.
Existing decisions, state escrow, Event 026/core APIs, constants, localisation YAML, on-actions, tests, and Git index remain parent/other-worker owned.
No staging, commit, launch, game operation, periodic hook, equipment grant, CXT content, GUI, or design simplification was added.

## Files and helper map

- common/scripted_effects/cbrn_occupied_transaction_effects.txt
- common/scripted_triggers/cbrn_occupied_transaction_triggers.txt
- common/scripted_localisation/cbrn_occupied_transaction_localisation.txt
- docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-03_cbrn_occupied_transaction_helpers.md

COUNTRY ROOT is the selecting donor for every country helper.
FROM is unused.
STATE iterator scopes change THIS/PREV and preserve ROOT.
No regular or global event target was added; existing normal STATE donor pointers remain authoritative.

| Helper | Scope, inputs and defaults | Outputs | Side effects and parent call site |
| --- | --- | --- | --- |
| cbrn_occupied_quote_transaction_costs | COUNTRY; existing ordinary PP25/factories2 constants and live canonical source; quantum1 through cbrn_quote_immediate_response_component | Temporary cbrn_occupied_fee, fee_valid, fee_source, fee_affordable, factory_quote, factory_quote_valid | Temporary quote only; gate/getter/selection use |
| cbrn_occupied_current_purchase_is_ordinary / _sale | COUNTRY; fresh factory quote | Boolean matching native two/one factory tier | Native visibility branch |
| cbrn_occupied_country_selection_ready | COUNTRY; country/emergency/target/physical-stock/fresh-fee/source, inactive program, no unresolved recovery | Boolean; quotes as above if caller initialized them | Selection gate omits freshly committed factories and cooldown |
| cbrn_occupied_country_preflight | COUNTRY; selection gate, shared cooldown, native quoted free-factory tier | Boolean | Both available/custom_cost_trigger |
| cbrn_occupied_ordinary_payment_ready / _sale_payment_ready | COUNTRY; corresponding mode plus preflight | Boolean | Variant-specific available/custom_cost_trigger |
| cbrn_occupied_requested_variant_matches_quote | COUNTRY; temporary requested_variant must equal ordinary or sale enum | Boolean | Immediate post-selection factory-tier identity |
| cbrn_occupied_state_has_owned_receipt | STATE; target marker, active occupied escrow, stored donor tag ROOT | Boolean | Every completion/refund iteration; ignores unrelated donor receipts |
| cbrn_occupied_country_has_active_program / holds_ordinary_program / holds_sale_program | COUNTRY; own active flag, existing national active flag, positive frozen transaction, matching variant | Boolean | Paid native timer visibility; independent of stock/source expiry |
| cbrn_occupied_country_can_continue / should_cancel | COUNTRY; existence/noncapitulation, active receipt, at least one valid owned STATE receipt with live need | Boolean | Shared cancel_trigger, no fresh stock/PP/factory/cooldown gate |
| cbrn_occupied_begin_selected_program | COUNTRY; caller temporary requested_variant, none rejected; fees freshly quoted | Temporary payment_success, program_reserved, transaction, refund aggregates if enclosing caller creates them | Stamp cooldown unconditionally; reserve five models per state; one PP payment/typed receipt; publish program only on positive reserve and successful record |
| cbrn_occupied_pay_and_record_fee | Internal COUNTRY; temporary frozen fee/source, positive allocator id | Temporary payment_success and transaction | One native PP debit; one PP-only component; failed record credits actual debit, checks credit, preserves unhandled evidence; unused allocator proof cleared if no receipt mapping |
| cbrn_occupied_refund_owned_targets | Internal COUNTRY; marked owned STATE receipts | Temporary program_refunded/program_refund_blocked | Exact existing five-model refund to original donor, clears successfully returned targets; lost states handled by existing control-change hook |
| cbrn_occupied_finish_selected_program | COUNTRY; active program; fresh per-state need/control and stored donor | Temporary actual program_usable/program_consumed; persistent last_delivered_usable/consumed | Existing state distribution/outcomes and unused-model refund; fee settlement; positive actual consumed and usable proof precedes achievement request; program clears once |
| cbrn_occupied_cancel_selected_program | COUNTRY; active program | Zero-delivery proof; refund outputs internal | Exact mask refund, settle spent service fee without achievement, clear once; repeated calls no-op |
| cbrn_occupied_settle_committed_fee | Internal COUNTRY; frozen receipt plus caller actual usable/consumed (cancellation initializes zero) | Shared settlement result internal | Closes fee, conditionally submits existing explicit delayed PP-only achievement claim, preserves failed settlement identity and claims |
| cbrn_occupied_clear_committed_program | Internal COUNTRY; active owner fields | None | Clears own native active/fee/mode/target-summary fields; retains shared receipt arrays, cooldown, delivery history and recovery evidence |

All consumed temporary outputs are initialized at their immediate outer helper boundary.
External callers needing temporary return values must likewise create those output names before calling the public helper.
The parent ordinarily consumes only boolean predicates and persistent state, so callbacks need only supply requested_variant.
The canonical response quote adapter is a read-only dependency; all its four consumed outputs are created before invocation.
PP results are copied to dedicated occupied scratch before the same primitive quotes factory_commitment.

## Parent migration and presentation

For ordinary selection:
~~~txt
set_temp_variable = { cbrn_occupied_requested_variant = constant:cbrn_occupied_program_variant.ordinary }
cbrn_occupied_begin_selected_program = yes
~~~

The sale definition supplies variant.sale and calls the same callback.
Use ordinary_payment_ready or sale_payment_ready from both available and custom_cost_trigger.
Use the corresponding current_purchase_is_* branch only for inactive starts and holds_*_program for active native timer visibility.
Preserve the existing public country/emergency/occupied-work visibility requirements for starts while allowing the matching paid receipt continuity branch.
Both definitions retain the existing public name/icon, willingness block, 30-day timer and 90-day re-enable.
Native modifiers remain exact static two/one factories; no scripted factory debit or fabricated native factory receipt exists.

remove_effect calls cbrn_occupied_finish_selected_program.
cancel_trigger calls cbrn_occupied_should_cancel.
cancel_effect calls cbrn_occupied_cancel_selected_program.
Remove the old external clr_country_flag before finish/cancel; these helpers own flag cleanup.
Replace the old begin/complete/clear bodies with direct wrappers or call these callbacks directly.
Do not execute both old and new reservation/outcome paths.
Existing legacy owner gates may become wrappers around the new country predicates.

Getters:

| Name | Parent YAML key(s) and numeric field |
| --- | --- |
| GetCbrnOccupiedDistributionPoliticalCost | cbrn_occupied_fee_cost_ready / cbrn_occupied_fee_cost_short; [?cbrn_occupied_fee|.0] with PP texticon |
| GetCbrnOccupiedDistributionFactoryCost | cbrn_occupied_factory_quote; [?cbrn_occupied_factory_quote|.0] with civilian-factory texticon in full tooltip only when native row already draws factories |
| GetCbrnOccupiedDistributionCrateCost | cbrn_occupied_crates_cost_ready / cbrn_occupied_crates_cost_short; [?cbrn_mask_reservation_quote|.0] with mask texticon |

Parent must define these five YAML keys, cost base/blocked/tooltip aliases, and wire the getters.
The PP getter uses the committed fee while active; factory getter uses committed variant; crate getter uses the original reserved total while active.
The active crate total is the starting reservation, not a claim that every original state receipt remains after control changes.
No new icon asset is needed; retain GFX_decision_cbrn_supply_occupied_population and existing PP/factory/mask texticons.

## Tuning and lifecycle

Parent provided cbrn_protection_decision_cost.occupied_distribution_sale_factories=1 and new cbrn_occupied_program_variant.none=0 / ordinary=1 / sale=2.
Helpers reuse all existing PP25, factories2, timing30/90, target50%, cost/wastage, full-filter, resistance/compliance and five-model constants.
Canonical prices remain PP25/13/7 and factories2/1/1 under ordinary/half/quarter sources; physical need/reservation/consumption is never discounted.
Factory quotes outside the exact native two/one set are rejected rather than substituted.

cbrn_occupied_program_purchase_cooldown is a shared COUNTRY timed flag stamped on every native selection with existing re-enable duration through a temporary variable.
cbrn_occupied_transaction_active and the existing cbrn_civilian_distribution_program_active identify one national program.
Normal COUNTRY fields cbrn_occupied_committed_{fee,source,transaction,variant,sale_sequence,reserved} freeze the selected transaction through source expiry/empty stock.
Normal last_delivered_usable/consumed retain actual last completion proof.
Existing STATE cbrn_occupied_mask_escrow_* and cbrn_occupied_distribution_program_target remain the physical receipts.

The PP receipt has one component (political_power id1), family political_power, primary_component basis, primary id1, member1.
Masks and native factory commitment are excluded from discounted paid material receipt metadata.
Successful receipt recording is immediately followed by publication; there is no owner outcome between record and publication that could require a recorded pre-publication refund.
A failed record therefore credits the actual unrecorded fee; successful native-program cancellation retains the spent service fee and settles the recorded receipt without achievement.
Repeated finish/cancel do not refund twice or distribute twice.
No new country active counter is used.

Failed native PP credit stores cbrn_occupied_unrecorded_paid_fee/source/credit_status keyed by transaction.
Failed fee settlement stores cbrn_occupied_unsettled_status/fee/source/sale_sequence/usable/consumed keyed by transaction.
cbrn_occupied_transaction_recovery_pending fails new starts closed, preserving unresolved paid evidence rather than overwriting it.
Blocked state refunds preserve their existing escrow and target marker and set the same recovery flag.
No administrative recovery button or automatic retry was added.
The parent must retain/report those exact failures and decide any recovery outside this bounded package; generic stock credit cannot reverse positive state coverage.

## Validation and source evidence

Seven actual-source cases passed using the existing exact quotation VM and native PP balance adapter under conservative scripted-helper temporary cleanup:
ordinary PP25/factories2, half13/1, quarter7/1, active sale with missing source rejecting quotation, exact fee paid once with typed receipt, insufficient PP producing no debit, and conflicting existing receipt record rejecting then crediting the actual unrecorded PP debit.
The test loaded real owner, canonical quote, payment, credit, allocator and receipt definitions; only native PP state and country flag operations were modeled.
The existing VM's complete quote-output assertion was narrowed to the consumed final/valid outputs, matching the immediate owner contract; internal exact/receipt checks remained in force.
The script was run through stdin and did not create or modify test files.
The parent owns durable full callback/conservation fixtures and final evidence.
These cases do not establish native timer, save-persistence, model provenance, full state lifecycle, in-game balances or AI behavior.

Source review verifies all five physical models remain handled solely by existing reserve/distribute/refund helpers, donor equality in every new state iteration, positive aggregate reservation before fee/publication, positive actual usable/consumed completion before achievement request, shared cooldown across native IDs, and zero fee achievement on canceled programs.
Required parent scenarios remain exact factories2/1, all unreserved stock exhausted after reservation, one/all state losses, reduced need/unused models, zero/positive delivery, source expiry, repeated finish/cancel, settlement rejection and failed credit retention.
Parent audit/probability comparison is required after decision wiring because gate changes affect the existing decision selection surface; this worker changed no weighted helper or AI score.

Exposed read-only proxy routes were available despite the parent prompt's earlier absent-route observation.
No alternate server or client was launched.
hoi4.script_validate is absent from this worker's exposed tool list; parent private SDK validation remains required.
Reference context/search/read succeeded and missing=[], omittedSources=[] for decision context.
script_doc coverage is unavailable; installed game_doc and offline wiki were available.

Narrow decision inspection: cbrn_supply_occupied_population, scenario occupied_helper_source_baseline with actor GER and deliberately unspecified state.
Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfb13649a438cabbc2b5ef1bc68ff5338195a70daca46927b73ee63490cc7046/36dd76388018a256d284193b4924f11e8bc103bbe750ae3da31936bb36184f09/decision-4fca1d22ba6159f7b8134c0b.json.
Source revision 01089feda166993f8af6140fc315c2a5dcab0dc7a8e5f1b235e8aaac1b34f222.
Result DECISION_ANALYZED_PARTIAL, complete=false, decision-coverage failed for unbound/unsupported source inputs.
This is an inspection artifact, not scenario coverage or engine proof.
The worker did not fetch the linked full artifact; parent must read it through its resource client before treating any detailed result as evidence.

hoi4.source_lookup returned cbrn_supply_occupied_population, mod:common/decisions/cbrn_protection_decisions.txt, lines377-428, revision173d59ca2eedf5ea97dc8bff5dba9fc4e12aba1c8efde050634a060cb41f20ea, complete=true, no references requested.
The returned body was bounded at lines377-425; source continuation and complete underlying source were read locally.

Read reference sections:

| Source | Lines | Source revision/hash |
| --- | --- | --- |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md, Variable types | 435-443 | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |
| Same Data structures file, Event targets | 263-327 locally | same revision |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, Timer upon selection | 337-356 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md, Temporary variable display | 729-792 | 1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064 |
| C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md | 254-266 locally | context revision18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md, native decision scopes | 1-46 locally | context revision5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md, every_controlled_state | 3800-3819 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Same effects documentation, set_country_flag / save_event_target_as | 6730-6738 / 6496-6504 | same revision |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md, Script Constants | 216-222 | 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7 |
| C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md | 1-34 | e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c |

Native precedent read: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/GER.txt:1575-1603 uses days_remove90, civilian_factory_use2, cancel_trigger/cancel_effect, and complete_effect startup flag.
It informs structure only; existing Chaos Redux exact state and receipt APIs govern outcomes.

Relevant source SHA-256 at review (concurrent-worktree samples, not immutable before fixtures):

- Effects: c1f5cd29ebf86067fd96dd2dcece14221d4da1881cdc6af4323008d94ae1c8db
- Triggers: 4491c3198d5798923d787db33da30bf8c1caf3d30829344713752dcdc5e699f0
- Scripted localisation: 27a29338571f4f8b3e483ab0a45ac9373b5fd39f8f69d3ab533f4a24548b2586
- Existing immediate effects: fe7b34d970279f89e2e7413f7ef547670cb322ba189831f61cd70975ca2d48ed
- Existing immediate triggers: fdae491b5c113092b63518d8a0217e2c209e25bb18705a583fd7aa0610abde4c
- Existing STATE protection effects: ff04b3decb07dd1fa7fd21ce9070d6de1622a320fbb960bc2380126ad2c3dfce

The underlying exact native stock debit/refund helpers do not return independent engine delivery acknowledgements.
New owner checks their reported refunded/blocked outputs and preserves blocked receipts, but source-semantic checks cannot turn native dispatch into observed provenance proof.
No fallbacks or balance/design simplifications were used.
Parent wiring/localisation, complete artifacts, task-specific lifecycle/conservation tests, probability audit/comparison, validation and commit remain required.

Skills used: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents.
No skill created or updated; the existing explicit consumed-output and exact escrow contracts already cover this workflow.
