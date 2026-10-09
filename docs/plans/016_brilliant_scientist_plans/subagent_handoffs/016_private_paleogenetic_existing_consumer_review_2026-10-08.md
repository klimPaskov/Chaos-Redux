# Event016 private Paleogenetics: existing consumers and recommended full contract

Date: 2026-10-08.
Owner: chaosx_scripted_system_architect; bounded read-only architecture handoff.
Disposition: **unresolved proposal awaiting parent-recorded acceptance**, not gameplay implementation or full Event016 completion.
The accepted final completion contract requires distinct stage payoffs, physical capability, containment/handler/transport vulnerabilities and authentic neutral Prototype access.
The Paleogenetics section of `016_private_custom_deployment_payoffs_2026-09-08.md` supplies a proposal, not acceptance of the quantities or interfaces below.
The latest parent direction asks for one complete recommended contract; all additional tuning below is a proposed parent choice.
Only this new report was written.
Disk and HEAD absence were checked before creation; `Test-Path` returned false and `git cat-file -e HEAD:<report path>` returned 128 with the explicit absent-path diagnostic.
No gameplay, assets, models, unit packages, index or Git mutation; no HOI4 launch.

## Findings that change implementation

1. There is already a KRG physical reserve/hatchery/transport consumer and a creature breeding consumer.
   Reuse its physical concepts and installed equipment IDs, not its provider wrappers, flags, counters or uniform legacy payment recipe.
   The bounded private-source search found no equivalent private reserve/hatchery or supplemental creature-production consumer; it found stage grants and project availability instead.
2. Current private Deployment buys **130 PP, 975 support equipment, 1,500 fuel and four native committed CIC for 480 days**.
   It does not buy the unrelated trucks, trains, manpower, army XP or MIC listed elsewhere in the broader project-cost table.
   Keep that full existing recipe; commissioning the pair is its included output, not a second purchase.
3. Generic stage entry already rechecks direct resources only; native availability owns free-CIC admission.
   There is no evidence of the alleged generic CIC double-counting defect.
   Preserve this split and require source-bound native admission for any specialized entry exception.
4. Generic finish clears the active paid receipt before output and fully refunds when `mengele_event016_project_output_applied = 0`.
   It cannot safely own partially delivered reserve/hatchery construction without a narrow specialized transaction branch before that clear/refund seam.
5. Freeze **quantity +1 for each component**, not an absolute payment-time building target as the delivery obligation.
   Freeze each attempt's immediate pre-level and expected post-level when the first actual attempt occurs.
   Competing construction never counts as our output; it may consume capacity and delay an undelivered component.
6. KRG handler recruitment increases a roster and veterinary support sets a flag; neither establishes a private workforce or site-qualified product.
   New private staffing needs a real committed workforce plus paid training, and transport needs the actual additional infrastructure increment.
7. Returning a fixed 75 support while universally discounting its entire input can create support equipment.
   The recommended private cycle treats those 75 as a separately tracked, returnable handling-kit deposit, not manufactured support byproduct.
   This is an explicit proposed economic interpretation; KRG's existing inline 75-support grant remains untouched.

## Current source and caller map

Paths in this section are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
All values are current source facts unless marked proposed.

| Existing consumer | Scope, authority and actual output | Current price and native timing | Source |
|---|---|---|---|
| `brilliant_scientist_krg_designate_paleogenetic_reserve` | Owned/controlled construction STATE through `FROM`; active KRG plus paid-site focus flag; +1 infrastructure, shared reserve flag and capability rebuilds | 65 PP, 200 support, 50 trucks, 1,500 fuel, CIC4; 120 days | `common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt:14-53` |
| `brilliant_scientist_krg_construct_paleogenetic_hatchery` | Same construction gate; an owned reserve exists; +1 industrial_complex, shared hatchery flag and rebuilds | Same heavy recipe and 120 days | Same file:55-95 |
| `brilliant_scientist_krg_recruit_paleogenetic_handler` | KRG active/focus; roster below six; adds one roster count only | 40 PP, 100 support, 25 trucks, 750 fuel, CIC2; 60 days/30 re-enable | Same file:97-114 |
| `brilliant_scientist_krg_establish_paleogenetic_veterinary_support` | KRG active/focus, roster positive, vet flag absent; sets vet country flag | Standard recipe above, CIC2; 90 days | Same file:116-133 |
| `brilliant_scientist_krg_construct_paleogenetic_transport_pen` | Owned/controlled reserve OR hatchery STATE; +1 infrastructure and KRG pen flag | Standard recipe above, CIC2; 90 days | Same file:135-176 |
| `brilliant_scientist_krg_authorize_paleogenetic_shock_pack_recruitment` | KRG operational, shared sites ready and roster positive; runtime rebuild and KRG authorization flag | 40 PP; 30 days | Same file:178-197 |
| `brilliant_scientist_krg_run_bounded_paleogenetic_breeding_cycle` | KRG operational; raid-AI branch OR veterinary flag plus owned pen; outputs 275 `paleogenetic_creature_equipment_1` and 75 `support_equipment_1`, adds KRG cycle history | 65 PP, 150 support, 50 trucks, 1,000 fuel, 1,000 manpower, CIC4; 90 days/30 cooldown; cap6 | Same file:199-240 |
| `mengele_event016_paleogenetics_deployment` | COUNTRY, Biological Programs; strict private provider, private Prototype predecessor and empty family receipt; repeated neutral operational grant plus Deployment flag/modifier | 130 PP/975 support/1,500 fuel/CIC4; 480 days | `common/decisions/016_mengele_paleogenetics_stage_decisions.txt:117-155`; `common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt`; stage quote effects:475-482 |

KRG price helpers are `brilliant_scientist_krg_pay_standard_material_cost`, `brilliant_scientist_krg_pay_heavy_material_cost` and `brilliant_scientist_krg_pay_project_batch_cost` in `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`.
Their matching preflights are in `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:229-252`.
The batch preflight also requires `num_of_military_factories > constant:brilliant_scientist_krg_value.zero`; this is a non-consumed industry prerequisite, not another price.
The old breeding action exceeds the four-spendable-type budget and is not the accepted new private recipe.
KRG physical cancellation gates do not supply exact paid refund receipts or construction-delta recovery.
Its construction helper at trigger lines328-332 validates ownership/control and positive infrastructure, not actual unlocked factory slots or remaining infrastructure capacity.
KRG hatchery selection does not prohibit choosing the reserve state; the new private pair must explicitly be distinct.
The breeding raid-AI branch bypasses veterinary/pen availability and finish does not revalidate them; do not inherit that bypass into the private chain.

Shared KRG project Deployment marks reserve/hatchery sites and `brilliant_scientist_paleogenetic_sites_ready` in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:647-655`.
Those are KRG facility/history consumers, not neutral physical commission APIs.
Do not call either capability rebuild simply to make a private flag functional: its dependencies and KRG history must remain isolated.

Private family is `brilliant_scientist_project_family.paleogenetics` (10), aligned receipt index9.
`brilliant_scientist_mengele_project_stage_provider_is_valid` in `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16-56` remains the sole strict provider gate, including country existence, private registry/program identity, host exclusion, incident/provider-loss and terminal-world exclusions.
Authentic private Prototype uses the neutral bridge in `common/scripted_effects/016_mengele_project_bridge_effects.txt:59-70`, requiring Theory/Prototype and native completed project or fresh native receipt.
`common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:65+` grants `brilliant_scientist_paleogenetic_formations_tech` and neutral `chaosx_custom_technology_paleogenetic_operational` access.
The equipment production definition already recognizes neutral operational access.
Ordinary factory manufacture and training must retain that access without private site, crew, transport or cycle-history gates.

## Recommended complete acceptance contract

The following is one coherent recommendation, **not recorded approval**.
It adds only internal helpers, receipts, constants and narrow actions in existing presentation; no family, category, window, focus, country, project, technology, unit or achievement.

### Selection and Deployment commissioning

Before paying Deployment, offer two free map/state selections in the existing private presentation: reserve, then distinct hatchery.
Selection creates only actor-owned candidate pointers, never buildings, entitlement, KRG flags or a paid receipt.
Allow free reselection while no funded/recovery transaction exists.
Use owned-state targeting with explicit current control; do not select random states or a fixed sample pair.
Country-root gates go in `target_root_trigger`; state checks run in `FROM`, with immediate commit revalidation because daily target enumeration is not a click-time guarantee.
Bind the actual payer through an explicit country pointer, not an unrelated callback `ROOT`.
Render selected state names using existing state localisation scope; no new GUI or asset is needed.

Reserve admission requires currently owned and controlled STATE, positive infrastructure and room for one infrastructure level.
Hatchery admission requires a different currently owned and controlled STATE, positive infrastructure, one **unlocked** shared factory slot and room for one later transport infrastructure level.
Use `free_building_slots` for the appropriate building; `include_locked = no` for industrial_complex, and the current building cap for infrastructure.
Do not add extra shared slots to evade a full state.
Do not demand an additional railway, supply-node resolver or third state: this contract's physical benefits are explicit ordinary state infrastructure and civilian industry.

Existing Deployment's entire nominal 130/975/1,500/CIC4/480-day recipe funds +1 infrastructure in the reserve and +1 industrial_complex in the hatchery.
No second fee, shorter timer or Portal recipe substitution.
At native entry, publish one actor/action/family/stage/serial-bound receipt **before** the first debit; reject duplicate entry without changing existing records.
Capture frozen pair pointers, expected quantities one/one, quote/source/nominal/actual resource values, native admission provenance and timer phase.
Retain payment-time levels for audit only; they are not evidence that later external construction fulfilled our output.
Current entry resource gate is direct-only; UI admission includes the exact four free CIC.
Any native-admission marker must be set by the actual decision source and consumed on every exit; do not open a bare API bypass.
Native reservation timing remains an engine-proof limit, even with that source-bound seam.

At expiry, revalidate strict provider, Prototype predecessor, neutral operational entitlement, matching paid receipt, frozen actor/pair and both current owned/controlled targets.
Do not repurchase resources or test four free CIC after the native reservation.
For each still-undelivered component, check current capacity and record **immediate attempt pre-level**, quantity one and `attempt_target = attempt_pre + one`, invoke literal STATE construction, then measure post minus pre.
Set that component delivered only on a matching measured positive increment, capped at its remaining obligation.
Record which attempt actually changed the level; external improvements reaching any old target are never our delivery.
A full state caused by competing construction suspends the undelivered component; recovery may proceed when capacity returns in the same frozen state.
No alternate state substitution after payment.
If no component has yet delivered, a deliberate cancel may refund matching actual direct payments once; uncertainty about delayed output is not proof of zero delivery.
If either component delivered, retain funded authority and its exact remaining quantity, expose bounded output recovery, and prohibit blind full refund or success history.
Recovery supplies only the outstanding increment, without another payment, timer, CIC commitment or replay of the delivered component.
Never remove buildings, cancel other construction, grant unlocked slots or replace a paid increment with a site flag.

After measured delivery of both components and current target qualification, settle costs and write `mengele_event016_paleogenetics_deployment_completed` once through the existing stage-history/modifier seam.
Neither neutral regrant nor a Boolean `output_applied` substitutes for two physical receipts.
The pair's actual post-attempt levels become its operational minimums; require corresponding current non-damaged levels for supplemental breeding.
These are aggregate STATE building readers: they prove enough live capacity, not the identity or health of a uniquely identifiable factory.
Damage does not reopen delivered construction authority; repair uses ordinary construction.

### Transport and real staffing qualification

After full Deployment, separately commission transport in the **frozen hatchery state**, consuming a proposed 100 concrete support equipment, 25 `motorized_equipment_1`, 750 fuel and CIC2 for 90 days.
This is four spendable types; no additional political fee.
It delivers another measured +1 infrastructure, with the same exact increment/capacity/control/partial-proof rules and private receipt.
The action represents road/loading capacity; its real benefit is infrastructure, not a new native pen building, supply hub or magical supply modifier.
Require a current non-damaged level at least its successful attempt post-level for transport qualification.
An initial hatchery at infrastructure cap is ineligible for this full chain; later competing construction can delay the pen, without counting as delivery.

Separately train one combined handler/veterinary team for the frozen pair: proposed 100 support equipment, CIC2 and 60 days, plus **250 manpower committed as a returnable noncombat workforce** (proposed allocation: 100 handlers and 150 veterinary staff).
Three spendable/committed resource types; no recurring human casualty payment and no formation grant.
Read available manpower using supported thousand-unit/native affordability readers and convert explicitly; a raw deprecated manpower dynamic value is not acceptable.
The 250 personnel are actual removed reserve manpower held in the actor's crew allocation receipt, not a roster flag alone.
At successful training, consumed support and completed training remain history, while the actual committed workforce remains allocated until demobilization.
Staff supports only this frozen pair; it cannot qualify several facilities simultaneously.
Site loss suspends qualification, rather than killing those personnel by assumption.
Demobilization releases the matching actual held workforce once and disables breeding until a new paid training/allocation completes; do not refund already consumed training materials.
Zero-output training cancellation returns only its matching actual paid materials/workforce once.
Fixed required headcount is allocation, not a discountable fee: discounts on training support cannot create 250 staff from fewer allocated people.
Receipt and explicit quantity are the mechanic; flags merely cache qualified/completed status.
This workforce allocation and its proposed quantities require parent acceptance and native debit/credit evidence; no existing KRG vet flag is equivalent proof.

### Supplemental breeding and support conservation

Require strict provider, exact private Deployment completion, neutral operational entitlement, both frozen live sites, qualified transport, trained allocated crew, noncapitulation and at least one military factory at admission.
No AI bypass of sites/staff/transport.
The one-military-factory gate follows the current KRG industry precedent; it is not consumed and is not a repurchase gate at expiry.
Allow one paid cycle at a time, existing **90-day native timer, 30-day cooldown, 275 creatures plus 75 support returned, lifetime cap six successful private cycles**.
These output/timer/cap anchors come from current KRG source; applying cap six to new private history is a proposed parent tuning choice.
No KRG count is read or written to account for private cycles.

Recommended ordinary cycle recipe: **375 concrete support equipment total, 75 motorized_equipment_1, 1,500 fuel and CIC4**.
The 375 comprises 300 consumed support and a separate 75-unit returnable handling-kit deposit.
Thus four spendable types, with no PP or burnt manpower; trained staff is a pre-existing allocation, not a fifth per-cycle cost.
Discounts quote the 300 support service/material fee, trucks and fuel using shared exact UNIVERSAL resource-family masks; the returned deposit is held at its real quantity and never discounted or counted as an achievement purchase.
The displayed support amount is quoted fee plus 75 held kits, with exact inclusive affordability for that total.
Do not use mask zero as a fictional discount exclusion: current UNIVERSAL constants explicitly define zero as all families.
Escrow is owner-managed capacity with nominal/actual held quantity, separate from shared fee receipts, following the existing separation of escrow and purchase demonstrated in Event026.
Its debit/credit may use shared native component APIs, but its state is not a purchased component that is blindly refunded twice.

At success, deliver measured total 275 creature equipment to the payer with `producer = THIS`, then return only the matching held 75 support once.
The returned kits may have native producer/design provenance limits; they are not newly fabricated support.
Full success and private cycle history require both acknowledged creature delivery and acknowledged kit return.
If creature output is zero and conclusively synchronous, cancel/refund actual fees and deposit once.
Positive partial creature delivery retains funded authority and remaining creature quantity; no full material refund with retained creatures.
Kit-return failure after full creature delivery retains only matching owed-kit recovery and settlement/history pending; it cannot authorize another 275 creatures.
Recovery uses no new purchase, native timer, CIC commitment or cap consumption.
Do not settle the shared fees before full success, and do not delete possibly consumed creature equipment as compensation.
Cancellation before any creature output refunds recorded actual fees plus separately acknowledged escrow; record failure after debit retains an owner emergency debit receipt until compensation is acknowledged.
Partially delivered cycles suspend on site/provider loss with original payer authority; they do not transfer free output authority to a captor.

## Proposed interfaces and stored data

Every identifier in this section is a proposed exact implementation name, not an installed declaration.
Literal parameter-free owner wrappers are preferred; inputs and consumed temporary outputs must be initialized by each caller before every nested helper boundary.
Persistent booleans are flags; numeric phases, identities, amounts and levels are normal variables.

| API name | Scope and inputs | Caller-owned outputs / side effects |
|---|---|---|
| `brilliant_scientist_mengele_paleo_reserve_candidate_is_valid` / `brilliant_scientist_mengele_paleo_hatchery_candidate_is_valid` | Pure STATE; explicit `paleo_actor` country pointer; other selected STATE pointer for distinctness | Predicate only; no selection, debit or output |
| `brilliant_scientist_mengele_paleo_select_reserve` / `brilliant_scientist_mengele_paleo_select_hatchery` | COUNTRY literal source wrapper; explicit selected STATE pointer, strict provider, no paid authority | `paleo_selection_applied`; saves actor-owned candidate pointer only |
| `brilliant_scientist_mengele_paleo_pair_is_operational` | Pure COUNTRY; authentic completed pair receipt and explicit stored targets | Shared site/control/current non-damaged-level gate; no grant |
| `brilliant_scientist_mengele_begin_paleo_deployment` / `brilliant_scientist_mengele_finish_paleo_deployment` / `brilliant_scientist_mengele_cancel_paleo_deployment` | COUNTRY; frozen actor/family10/stage/serial plus source-bound entry marker at begin | `paleo_transaction_result`; matching specialized payment/component authority, no KRG state |
| `brilliant_scientist_mengele_recover_paleo_deployment_output` / `brilliant_scientist_mengele_recover_paleo_refund` | COUNTRY; exact pending authority and original actor | `paleo_transaction_result`; outstanding construction or matching owed refund only |
| `brilliant_scientist_add_paleo_reserve_infrastructure` / `brilliant_scientist_add_paleo_hatchery_factory` / `brilliant_scientist_add_paleo_transport_infrastructure` | Neutral STATE literal building wrappers; caller-owned `paleo_building_amount`, explicit actor; current control/capacity | `paleo_building_before`, `paleo_building_after`, `paleo_building_delivered`, `paleo_building_measurement_valid`; consumes input amount to zero on every exit, no history |
| `brilliant_scientist_mengele_begin_paleo_transport` / `brilliant_scientist_mengele_finish_paleo_transport` / `brilliant_scientist_mengele_cancel_paleo_transport` | COUNTRY; frozen hatchery and matching receipt, native entry marker at begin | `paleo_transaction_result`; paid measured transport component |
| `brilliant_scientist_mengele_begin_paleo_staff_training` / `brilliant_scientist_mengele_finish_paleo_staff_training` / `brilliant_scientist_mengele_cancel_paleo_staff_training` / `brilliant_scientist_mengele_demobilize_paleo_staff` | COUNTRY; frozen pair and explicit held-workforce receipt | `paleo_transaction_result`; one workforce allocation/release, training materials and qualification |
| `brilliant_scientist_mengele_paleo_staff_is_qualified` / `brilliant_scientist_mengele_paleo_transport_is_qualified` | Pure COUNTRY; matching trained workforce / delivered transport receipt and current pair | Predicate only, no KRG flags |
| `brilliant_scientist_mengele_quote_paleo_breeding_cycle` | Pure COUNTRY; live UNIVERSAL sources, nominal private constants | `paleo_quote_support_fee`, `paleo_quote_support_deposit`, `paleo_quote_support_total`, `paleo_quote_motorized`, `paleo_quote_fuel`, `paleo_quote_valid`; consumed source-proof arrays caller-owned too |
| `brilliant_scientist_mengele_paleo_can_pay_support` / `brilliant_scientist_mengele_paleo_can_pay_motorized` / `brilliant_scientist_mengele_paleo_can_pay_fuel` | Pure COUNTRY, already caller-owned fresh quote values/valid | Same inclusive component predicates for UI colours and direct payment admission |
| `brilliant_scientist_mengele_paleo_breeding_can_start` | Pure COUNTRY; one fresh quote, qualified chain, no live/pending receipt, successes below cap | Full selection including CIC4; no native admission-marker requirement in UI |
| `brilliant_scientist_mengele_begin_paleo_breeding_cycle` / `brilliant_scientist_mengele_finish_paleo_breeding_cycle` / `brilliant_scientist_mengele_cancel_paleo_breeding_cycle` | COUNTRY; source marker at begin, then immutable receipt | `paleo_transaction_result`; one exact direct transaction and kit escrow, native timer externally owned |
| `brilliant_scientist_add_paleogenetic_creature_equipment` | Neutral COUNTRY; explicit positive `paleo_equipment_amount`, actual Portal-independent paleo tech required | `paleo_equipment_delivered`, `paleo_equipment_measurement_valid`; concrete stockpile delta, producer THIS, input cleared on every exit; no private/KRG history |
| `brilliant_scientist_mengele_paleo_output_recovery_is_pending` / `brilliant_scientist_mengele_paleo_refund_recovery_is_pending` / `brilliant_scientist_mengele_paleo_can_recover_output` / `brilliant_scientist_mengele_paleo_can_recover_refund` | Pure COUNTRY; action/serial/phase-specific pending receipt | Mutually exclusive ordinary/output/refund controls; controls cannot authorize a different action's receipt |
| `brilliant_scientist_mengele_recover_paleo_breeding_output` / `brilliant_scientist_mengele_recover_paleo_breeding_refund` / `brilliant_scientist_mengele_cleanup_paleo_transactions` | COUNTRY original payer; explicit matching pending/cleanup authority | `paleo_transaction_result`; only remaining output/owed refund, explicit cleanup after authority retirement |

COUNTRY normal receipt fields should use the `mengele_event016_paleo_` prefix: `actor`, `action`, `serial`, `transaction`, `phase`, `reserve_state`, `hatchery_state`, `quantity_expected`, `quantity_delivered`, `output_expected`, `output_delivered`, `crew_actual_held`, `kit_actual_held`, `kit_actual_returned`, `breeding_successes`.
For each construction role retain `payment_level`, `attempt_before`, `attempt_target`, `attempt_after`, `delivered` and `measurement_status`; arrays keyed by the bounded role/action index are appropriate.
Payment component arrays retain resource kind, model, nominal, final, source/source count, actual debit, record acknowledgment, refund owed and refund acknowledgment.
State mirrors need exact actor/action/serial/role identity, not an unqualified shared site flag; reject foreign/corrupted mirrors and never clear another actor's mirror.
Use normal stored scope pointers for durable actor/pair identity and regular event targets only as ephemeral aliases within a call.
Do not rely on `scope_exists` alone for saved pointers or on mutable serial equality to prove stale same-action native callbacks cannot match a newer action.
Expose frozen names, current damage/control and remaining obligations in existing tooltips; do not print raw internal flags.
Parent must document the final stored-field layout and helper defaults in the matching implementation markdown before wiring.

Centralize proposed tuning under one schema-first `mengele_paleo_deployment` category: reserve/pen infra quantities1, hatchery CIV quantity1, staff handlers100/vets150/total250, training support100/CIC2/days60, transport support100/trucks25/fuel750/CIC2/days90, breeding support_fee300/kit_deposit75/trucks75/fuel1500/CIC4/days90/cooldown30/output275/cap6.
Existing Deployment 130/975/1,500/4/480 remains authoritative in its current shared stage tables; do not duplicate or retune it in this new category.
Use literal native modifier macros only where constants are unsupported, with documented equality to their shared tuning.

## Extraction, quotes and cleanup boundaries

Modify only the Paleogenetics Deployment branch of `brilliant_scientist_mengele_begin_project_stage`, `brilliant_scientist_mengele_finish_project_stage` and `brilliant_scientist_mengele_cancel_project_stage` when implementing this accepted contract.
The authenticated special branch must execute before general active-row clearing at effects:777 or cancellation:752.
Ordinary generic finish remains unchanged for unrelated families.
An authenticated partial specialized receipt is neither generic success nor generic zero-output refund; preserve its paid snapshots and block new family entry until acknowledged completion/refund.
A missing or corrupted specialized receipt is not permission to suppress every generic refund or mint another pair; retain an explicit audit/recovery fault and reconcile the exact original payment row.
On full success, bridge to existing completion/modifier and incident dispatch once; do not trigger incidents on partial attempts or repeat recovery.

Current direct stage payment at effects:727-734 debits an aggregate support archetype and stores quoted amounts after debit.
Do not assert it already measures concrete actual payment or supports UNIVERSAL source receipts.
The specialized adapter must measure and retain actual component/model debits before adopting stronger exact-refund claims.
If support remains aggregate at admission, distribute the aggregate quote across actual concrete models using shared owner-adapter semantics; do not silently change the stage's accepted support currency or assume original producer/design provenance is recoverable.
The current three direct nominal amounts remain the stage quote basis; future shared discount integration must follow the authoritative owner framework rather than adding private discounts.

Use `universal_cost_quote_exact`, `universal_cost_pay_component`, `universal_cost_record_transaction`, `universal_cost_refund_transaction` and `universal_cost_settle_transaction` for new purchase components.
Allocate unique owner IDs through `black_friday_allocate_owner_transaction` (Event026 effects:972-980), preserve every consumed temp output across boundaries and forward typed metadata explicitly for each component.
Existing masks are support32, motorized64, fuel8, PP1; concrete support kind11 and motorized_1 kind29 are supported shared resource kinds.
Native CIC remains fixed occupancy with its discount-adapter limitation; do not pretend a direct-payment discount changes native reserved factories.
Logical achievement family/primary component must follow an existing registry-defined owner contract, not be inferred from PP or invented from the word Paleogenetics.
Parent must resolve that exact registry mapping when implementing new purchasing owners; this report does not create one.
Shared record rejects actual-paid/quote mismatch; if native debit differs, retain measured debit outside the shared row and compensate/resolve it explicitly, rather than recording fictional equality.
On any record/refund failure, preserve the matching live obligation and block output until actual funding is proved.
Support kit and workforce escrows are separately acknowledged held assets, not arbitrary extra discounts or duplicate shared refunds.

Integrate specialized cleanup **before** the family cleanup loop in `brilliant_scientist_mengele_cleanup_provider_receipts` (`016_mengele_project_stage_effects.txt:1934-1989`, generic cancel at1962).
Otherwise the generic loop can erase partial paid authority.
Existing program reject/close/expire/victory/defeat and terminal callers already reach that provider cleanup; preserve their scope and add the narrow hook there rather than a scheduler.
Known call sites include `germany_mengele_effects.txt:1564,1719,1735,1749,2049,2057` and `016_mengele_singularity_terminal_effects.txt:180`.
Retire delivery authority before any explicit native decision removal; ordinary native cancellation owns its removal and should not recursively remove itself.
Zero-output cancellations retire authority then acknowledge exact refunds; failed refunds retain debt for explicit retry.
Partial irreversible output on terminal provider loss is retained as suspended/retired partial history with no full refund, no captor transfer and no further output while provider invalid.
Release the original owner's held workforce/kits only under exact once-only escrow acknowledgments; never compensate from a new owner's reserves.
Do not erase unresolved shared payment/refund rows during country cleanup.
Site loss needs no global on-action: click, native cancel/finish and explicit recovery revalidate the bounded pair; learned tech/equipment/buildings remain.

Presentation reuses existing Deployment/reserve/hatchery/transport icons, including `GFX_decision_brilliant_scientist_project_paleogenetics_deployment` and the KRG reserve/hatchery/transport action sprites already named in the inspected decision file.
Reuse artwork only; new private tooltip/receipt text is parent-owned.
No asset inspection or production occurred.
Recovery and staged selection/training/transport rows must be mutually exclusive as appropriate so the existing category remains readable; parent owns the decision audit and any weighted AI scenarios.
CXT may observe frozen actors/sites, actual deltas, component acknowledgments and pending recovery through an existing player-triggered probe; no grants, new package or periodic maintenance hook.

## Economic justification and test boundaries

Current creature equipment costs 8 equipment IC and consumes two steel/two rubber in ordinary production; fuel consumption is 0.50 (`common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:32-43,354-358,434-440`).
A 275-creature batch represents 2,200 nominal equipment IC; it remains stockpile output and never grants a formation.
Vanilla support costs4 IC (`common/units/equipment/support.txt:23`); motorized costs2.5 IC (`motorized.txt:26`).
Legacy KRG input equipment is 725 IC, its 75 support output is300 IC, giving425 net equipment IC plus fuel/PP/manpower/factory time; that is a precedent, not proof of balance.
Proposed private consumed materials are 300 support (1,200 IC) plus75 trucks (187.5 IC), with1,500 fuel and360 CIC-days per cycle;75 kits are returned capital, not another300 IC of free production.
At cap6, full output is1,650 creatures; six kit returns cannot mint450 support because each returns only its actually held75.
Discounts may reduce consumed material prices, but never create more returned kits than held; test the strongest stacked and expired-source prices.
The vanilla infrastructure/factory pair costs6,000+10,800=16,800 nominal construction IC (`common/buildings/00_buildings.txt:34-82`), with infrastructure cap5 and CIV shared state cap20 plus unlocked-slot constraints.
Deployment commits1,920 CIC-days plus3,900 nominal support-equipment IC,1,500 fuel and130 PP.
Construction IC, military-equipment IC, fuel and time are different economies; these calculations establish tangible scale and opportunity cost, not balance equivalence or an accepted price.
The extra civilian factory has permanent production value, while roads and workforce/transport dependency distinguish this chain from a generic equipment purchase.
No probability balance was audited here; parent acceptance and dedicated auditor own tuning and AI evidence.

Required source fixtures for implementation: Prototype-only ordinary production; free selection/reselection and same-state rejection; foreign ROOT; exact resource/factory boundary and bare native-entry rejection; full/locked slot and infrastructure cap; rival construction before first attempt; actual +1 despite rival construction; one-component success/second-component failure; damaged or captured site; partial recovery after capacity returns with no delivered replay; unrelated external repair/build never counted as paid delivery; corrupt/missing actor/serial/receipt; payment/record failure and owed-refund retry; workforce allocation/demobilization repeat; insufficient/discounted support fee versus75-kit escrow; source expiry while funded; zero/positive partial creature output; failed kit return; depleted reserves at expiry; sixth/seventh success; repeated finish/cancel/recovery and modeled nested callbacks; terminal cleanup before generic clearing.
These are a required validation contract, not tests run for unimplemented helpers.
Parent's independent current reference/source evidence confirms building_level and actual +1 output delta; that is source/reference acceptance, not an observed engine session.

## Bounded reference receipts and remaining proof

Live `hoi4.reference_context` for decision surface, `reference_search`, revision-bound `reference_read`, `source_lookup` and `script_validate` were exposed and successfully called.
No timeout occurred in these narrow calls; no broad graph, probability, map-catalogue, focus, GUI or technology inspection was launched.
Initial context omitted Decision modding/Scopes/Localisation under its result limit; targeted decision sections were read separately, and this report makes no claim of complete documentation coverage.
Map geometry and Portal exact-node/health proof are parent-owned and were not duplicated.

| Directly read reference | Exact path and lines | Revision |
|---|---|---|
| STATE construction | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:839-847` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Slot reader | Same documentation root, `triggers_documentation.md:2901-2915` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Current undamaged level | `triggers_documentation.md:6554-6569` | Same trigger revision |
| Total and undamaged dynamic levels | `dynamic_variables_documentation.md:1101-1103,1139-1141` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Workforce native credit/debit command scope | `effects_documentation.md:1468-1476` | Same effects revision |
| State-target / daily versus frame scopes | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46` | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| Offline construction syntax | Repo `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:3614` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline slot syntax | Repo `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:1834` | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline state selection | Repo `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:576-595` | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |

Vanilla native decision precedent is `invite_GER_henschel_organization`, `game:common/decisions/aat_mio_decisions.txt:70-85`: owned fully controlled STATE, free building slots, literal +1 instant construction.
Its source-location MCP revision is `ffb50bb7cb1f4bd6abb65282d5cf0ef304e2c462fc8a976076b1a1b4a581705b`.
It adds a shared slot and permits locked slots; those details are deliberately not proposed here.
MCP exact KRG breeding definition was read at199-240 under workspace index revision `df95db40a904be757bd273cf6fc2ce4708fc5dd794b35113bc0d075d623afa6d` (returned text truncated near237; local source supplied the remaining output/history lines).
MCP generic finish `if[0]` was read at770-784 under index revision `108db46475e9b98b607cf5622b428578c33de59a8defb3319d33d0708f758c49`; local759-788 supplied the complete bounded body.
An initial lookup using the nonexistent `brilliant_scientist_mengele_finish_paid_project_stage` returned zero definitions; it was corrected to the actual symbol, not treated as evidence of missing finish.

STATE snippet validation returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, syntax/kind/scope checks only, `parametersChecked = false`.
The two construction commands had two unchecked argument blocks; the three slot/undamaged predicates had three unchecked blocks and one omitted supported finding under limit5.
Installed validation documentation revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
No parameter or runtime proof is inferred from that result.

Remaining exact blockers/inputs are parent acceptance of this full tuning and escrow/workforce interpretation; final owner registry/achievement mapping and concrete aggregate-support refund handling; native synchronous building/equipment readback versus delayed recount; interruption between effect and receipt acknowledgment; exact damaged-level thresholds with variables; state-control semantics for partly occupied states; workforce allocation/refund behavior and country destruction; and native cancellation/expiry/stale same-action callback ordering.
If synchronous readback is not established, mark measurement uncertain and retain authority; do not infer a safe zero-output refund or retry an effect that may already have applied.
A mutable serial alone does not prove stale native callback isolation.
An aggregate building reader cannot recover construction provenance or unique building identity; the receipt proves this script's immediate measured increment only.
Native concrete stockpile restoration cannot recover original producer/design provenance.
Documented native remove_decision does not run remove_effect or put the decision on cooldown (installed effects:5959-5967, same effects revision, parent-provided receipt); cancel_effect ordering remains separate uncertainty.
Any modeled reentry is a robustness fixture, not a claim of observed native behavior.

## Snapshot identities and disposition

SHA-256 of the source snapshots read in this bounded audit:

| Repo-relative source | SHA-256 |
|---|---|
| Final completion contract | `85083446610d0cae9c8c52ce2afa829ab799a170c38dc9249557e9f171a3ef48` |
| Prior private payoff proposal | `82f881d513aabb0dae1ae67287ac19f5c220ddee5c35344bdc45e2218d3457b5` |
| KRG paleo/xeno decisions | `296f153cadc21132a0085af9b497c13d818e607bea52244368212dee616bcfec` |
| Private Paleo stage decisions | `4bf57705a70d201a8e44a2fec8de571d6e556bbe22830a1a2773df7617dcb941` |
| Private Paleo stage decision triggers | `a457bd6f889ea2ef163ea4f0d536aab8213377737dde496a63f2f35a8d8bcf0a` |
| Private generic stage effects | `209ee22fc5461e9e07463c39349723685510052294ee2e8ca4f6db42a4a6425c` |
| Private generic stage triggers | `6675660ef5967de9fbf1a729b9e33bcef68fe05bb0542ef1ef8a080644ebf706` |
| KRG decision constants | `c7f4b8af4aeb9ffcf208cea948b9390aff72445340ca8faf3ad403d199a28978` |
| Main Event016 constants | `adfee7fe6093933c394c34c8a6a162795d4bdb4575512c476b417c1173b6e4a6` |
| Event016 project constants | `a95301ed9cbc7bb8fcb751885165f62ae5aa8c6b315eadb0c5cdaf79350ce131` |
| Private Prototype bridge effects | `b32728f700de61d66efd2e40262825365ee233d780ca69f6c0f0fd9da54e0714` |
| Custom technology API effects | `67993f2cb733c0de4b8b2ec96ac55ce68bcbc65ef0ed79f08f9e4a6f66b0f604` |
| Existing project-force equipment economic definition | `4687027a01dbc8cd1bee2ea0a872ec418fa85628ef2c554857a2c6320285a2e0` |
| Vanilla `common/buildings/00_buildings.txt` | `9fa27d266f726de04c71311551698c6466257636dcc34d2573a3568d397bd539` |
| Vanilla `common/units/equipment/support.txt` | `fd41d5223c62cf955d650bbad0b1adecfae6be9e1cc43904fb0118fb5d3e5385` |
| Vanilla `common/units/equipment/motorized.txt` | `b25c3797280f471b89a43da5b02e135091cf205acdf37c09d547a88df52d5128` |

Concurrent parent changes can supersede these snapshots; re-read the narrow wiring seam before implementation.
Skills applied: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents; no skill changes.
Completed: bounded existing-consumer audit, economic comparison, exact proposed API/data contract and partial-paid migration/cleanup map.
Queued pending acceptance/implementation: full private pair, staffing, transport and breeding adapters and their owner tests/audits.
No simplification was implemented or approved; the complete physical recommendation and every unresolved native proof remain explicit.

## Parent disposition, 2026-10-09

The parent reviewed the complete recommendation and recorded acceptance in [the private deployment contract](../016_private_paleogenetics_deployment_acceptance_2026-10-08.md), under the user's instruction to continue autonomously and take the recommended option.
The real 250-person allocated workforce, transport recipe and conserved 75-kit breeding deposit supersede the preliminary non-consumed staffing requirement and supplemental recipes in that acceptance document.
Those supplemental actions remain accepted and queued after the paired construction transaction.
The implemented pair uses the exact interfaces and stored fields in [its owner API](../../../../common/scripted_effects/016_mengele_paleogenetics_deployment_effects.md), which supersede the proposed names in this report for that implemented surface.
The source snapshots and initial unresolved-proposal disposition above are retained as dated research evidence and do not override this recorded acceptance.
Native ordering, measurement and refund-provenance limits remain open, and acceptance does not establish implementation or engine completion of the full payoff.
