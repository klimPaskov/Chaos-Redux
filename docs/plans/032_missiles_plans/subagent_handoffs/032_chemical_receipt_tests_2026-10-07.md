# Event 032 chemical receipt source tests, 2026-10-07

Disposition: `implemented` for the existing 40-method offline test, with the requested consequence-dispatch follow-up `blocked` as detailed below.
Parent integration and engine evidence remain unresolved.
Acceptance basis: the parent explicitly assigned an actual-source regression restricted to the two files below, post-validator transitions, audit R2/R3 regressions, fractional sanctions disposal, and bounded Event32 public receipt-caller integration.

Files created, both absent before creation:

- `.tools\test_cbrn_payload_reservations.py`.
- This handoff.

No gameplay, helper documentation, constants, call sites, localisation, assets, Git/index, or other files were written.
No agents, game launch, log search, or weighting changes occurred.

Run from the repository root:

```powershell
python -B .tools/test_cbrn_payload_reservations.py
```

## Execution coverage

The final run passes 40 test methods with named subcases and executes 82 production helper definitions, comprising 66 CBRN, 14 Event32 and two sanctions helpers.
The loader reparses production bytes on every invocation, prints all 25 source SHA-256 identities, and fails if any source changes during the run.
Production receipt source SHA-256 is `fd8535a93429919eff2a0b22e0d9b5906872ee78c34d6fa96f4dbd9fe07c02f2`.
Reservation native source is `a583e9e786593678a1a59ed32b97a90a0d9c3e6241a7ca04084d9a0c459a4add`, receipt triggers are `af9316cdf8ed8cf9a21e7986df78bcf6524e69dce763499a7c0ea6b9a45f45e0`, and receipt constants are `498d969175382aca6e8157806746e1438eac09e283e5b8df5557347c9f0cc293`.
Payload/profile source is `d61d67bdd9dc77366c894ca7a5cf42d0a0db1a1eeb9d3272d9ce5abe8012ef34`, shared exposure/reset source is `bb23620b4f16f62b4f808b3524b6a59e6bcf57a12f62802c816b1ceb824aae72`, and designer triggers are `cdd8d76ba23b8e485e8ee6e1457c2bbbe4246fa19841a79cdccf9bf0ad776dd9`.
Event32 receipt effects are `c0c1f9a5882c5a5a5cc8d652d96ed8da1810686c5b7a22e2172d25b918306834`, receipt triggers are `9da2e18a7114153600196fffabc94fe21c4fbd6c393d664f3b20db84acde4998`, operations triggers are `e845bd7a545c91c27a5b1f2aa2f95dc0bfdf52cfb40fd98ae7c23f4d6d233777`, main missile triggers are `11bf9495ad7c1daaabe0af1d5caad5cd444fd6873a14da48b031ba1df148a611`, and missile constants are `1dabadf3281586ef3106819e5b130f0685c726c85d495a5ef59798fa3c368a94`.
Current operations effects are `f1344d6acd266da99abce45a6880fc582ad299b6a32b139eff0b7e2689f2037a`, with only `missiles_consume_special_payload` and `missiles_consume_chemical_payload` loaded from that file for the owning consumption boundary.
Sanctions response effects are `96cc1f4e773d783acdd8af1766b3023a1a27c78e0e68700de42bbe7faeb1f077`, sanctions triggers are `f7182d70de24ccb0fe416ce5bdb6c53bf60fd4f4dc24e96424e2d8cddb796753`, and sanctions constants are `dfce011762ed73f489e34537351621ac703df6101dc59434c78069cd727d92f9`.
These identify the tested draft, not later parent changes.
The parent separately reported passing the earlier 26-method version before this follow-up.

- All nine agents reserve, reserve again without another payment, consume once with zero free stock, reject duplicate consumption, and return twice without duplicate credit.
- All nine agents survive sealed capture with original agent/model/quantity/provenance and no native credit or technology grant, then integrate only with the matching profile and current technology/project.
- All four models execute full, bounded partial, zero, negative-input and invalid before/after native measurement cases through both wrapper and shared meta-helper bodies.
- Partial debit retains only observed stock, partial return preserves its remainder, invalid observations quarantine, and deliberately wrong-model mutations cannot establish full debit or full return.
- Wrong nonce, consumer, handle, actor, agent, route, target and source reject, as do lost current policy, technology, profile, custody, war or sufficient new-preparation stock.
- Foreign-ROOT refund credits the original holder despite lost launch eligibility and rejects captured source, corrupted site identity, changed profile or a removed actor.
- The real `cbrn_validate_payload_reservation` returns before an injected consumed/returned/destroyed/transferred tombstone or changed binding is applied.
  Consume then rejects without new native writes, fresh accepted result, duplicate consumption or reversal of the injected closure.
- Selected-receipt counter deltas survive repeated refresh, multiple captured receipts, retirement, and an unrelated registry suffix exceeding 1,000 entries.
  Copied foreign ledger initialization resets the owner marker, counters and consumer slots without authorizing the copied receipt.
- `cbrn_settle_site_payload_reservations` executes recover, hold, destroy, capture and integrate through the real settlement helpers, preserving an unrelated site's receipt and cleaning its temporary handle array.
- R3 supplies caller-owned `break = 1` and stale private collect/settle breaks of 1 to the real site selector.
  Two matching receipts separated by an unrelated receipt are constructed through actual reserve/transfer bodies, then both matching receipts are destroyed or integrated while the unrelated row remains unchanged.
  The default break remains 1 and production resets both private break outputs to 0.
- R2 freezes state A, changes its stored pointer to state B controlled by receiver R, and attempts capture for receipt handles 1 and 2.
  Both reject without changing held quantity, creating receiver ledger/receipt storage, or making any native call.
- The actual `cbrn_change_air_payload_profile` rejects an unlocked alternative while a receipt remains open and preserves its original agent.
  After full return it changes the profile, executes the ordinary stock wastage and supplies the source-defined timed flag without rewriting the closed receipt's agent.
  The complete legacy migration helper also rejects its air-default setter with an open receipt, then permits that setter after explicit disposal in a zero-legacy-stock scenario.
- Fractional disposal reads the existing sanctions constant 0.75 and executes the real `cbrn_dispose_reserved_payload_fraction` on each of the four reservation models.
  From 240 held, it records 180 destroyed and 60 recovery-pending, invalidates full-hold preparation, preserves another actor's independently constructed receipt/input state, and later credits only 60 without another debit.
  Sealed captured receipts retain captured phase, exact origin and agent, with only 60 eligible for later authorized integration.
  Repeated counter refresh and disposal of an already closed registry are harmless, while repeated disposal of an open remainder is a separate compliance action rather than an idempotence claim.
- Normal and captured quarantined receipts return the quarantined result, zero disposal reward quantity, unchanged receipts and stable counters.
  `condemnation_has_chemical_stockpile` detects a positive held balance or quarantine count, including a zero-held native mismatch.
  The complete `condemnation_destroy_chemical_stockpiles` runs against empty free stock, preserves the quarantine result, and supplies no decay credit, compliance-state change, destruction/restriction flag, response-duration helper or achievement call.
- Event32's new direct public reserve helper freezes operation 42, source/target IDs, receipt handle/active mirror and exact agent, then removes 240 through the real CBRN API.
  Commit succeeds with free stock zero and consume supplies fresh 240 quantity/debit proof without another native removal on all four models.
  Repeated consume clears the stale proof, and repeated release cannot credit a consumed row.
  Voluntary return and foreign-ROOT loss of another participant refund the original actor, primary-source capture creates sealed receiver custody without credit, and primary-source destruction supplies no refund.
  Changed current technology, profile, policy, source, missile custody, evolution toggle, nonce or target ID rejects commitment and consumption.
  Event32 fractional disposal also rejects commit and returns only 60 through the actual cleanup-release helper.

The shared authorization closure includes actual static metadata, route-agent eligibility, technology/project unlock, profile, exact-target policy and stock predicates.
Authorization, dispatch to measured stock helpers, measurement status, receipt closure and counter effects are never mocked as success.
The Event32 scope fixture and public helpers use this same interpreter.
The chosen bounded entry is `missiles_reserve_chemical_payload_receipt`, not the full operation reservation orchestrator.
Executed Missile predicates include reliable special-payload custody, special-warhead toggle/adoption, payload policy, registered-site checks and the paid chemical receipt predicate.
An additional source-boundary assertion verifies that the receipt adapter adds no native stock mapping or mutation, supplementing the actual payment paths rather than replacing their execution evidence.

## Model and injected leaves

The independent parser retains operators, repeated keys, order and source lines.
It does not reuse the operator-dropping recipient-scope parser.
Typed country/state objects retain persistent normal variables and arrays independently of the ROOT/PREV/current scope stack.
Dynamic `@var:` keys resolve against the current frame and scope, including cross-holder targeted reads during capture.
Every scripted effect, scripted trigger and meta expansion gets a temporary frame.
New scalar/array storage disappears on return, while modifications to caller-preinitialized storage survive, including nested native scratch.
Separate interpreter probes verify this and reject unknown commands, stock argument fields and unsupported scoped getters.

Scenario mocks are limited to `num_equipment@model` observations, `add_equipment_to_stockpile` mutation outcomes, native flag/duration storage, and world facts used by native existence/control/war/technology/project/MIO/equipment predicates.
Stock calls record requested country/model/amount and injected actual model/delta.
Explicit full, half, zero, negative, opposite-sign, excessive and mismatched outcomes are independent of production acceptance.
Physical custody/recovery/loss/transfer proofs are scenario inputs supplied to the real API.
The post-validator mutation is an explicit boundary injection, not a replacement validator.
Loop entry no longer resets a selected break variable in the interpreter, which would mask R3.
A separate counterexample preserves caller `break = 1` and demonstrates truncation of the default-break loop under the chosen after-body break check.
Native first-iteration break timing remains unobserved, while the production private-break resets avoid either timing ambiguity.
Profile change executes its real designer trigger over an explicitly empty organization inventory, not a designer-helper success stub.
Nonempty MIO inventory analysis fails loudly, timed flags are recorded without clock/expiry simulation, and rounding uses Decimal half-up on integral wastage quantities in these cases.
Unmeasured stock mutation is permitted only inside the actual air-profile wastage helper, plus the sanctions owner's zero-amount free-stock calls, and remains recorded in `nativecalls`.
Zero-amount calls do not create stock entries, and the reservation model family remains the original four prepared-air models.
Bare event-target values retain typed scope pointers, state/global flags use explicit fixture sets, and `has_war` reads declared war partners.
`scope_exists` checks the typed scope object and is not credited as ownership or live-country proof.

Chosen `has_variable` model sees live unscoped temporary storage as well as current-scope normal storage, with those stores kept separate.
Installed trigger documentation only says it checks whether a variable exists in a scope and does not settle temporary visibility explicitly.
A normal-only counterexample is tested: reservation rejects at `cbrn_action_target_state_is_valid`, and a separate stock predicate rejects its temporary `cbrn_action_payload_required`.
This uncertainty remains an engine evidence gap, not a green runtime claim.

## Limits and parent follow-up

No gameplay simplification or fallback was introduced.
No requested direct receipt case is omitted.
The bounded Event32 receipt callers execute from current source, while broader preparation/launch orchestration, authenticity of owner-supplied physical proofs, callback site/nonce mirrors, save persistence, native equipment producer/variant handling, engine fixed-point limits and actual temporary lifetime remain unproven.
No Event32 consequence dispatch, contamination, casualty, evidence, Condemnation-release or confirmed-use pipeline is included in execution coverage.
The new removal helper's `for_each_scope_loop`, broader Missile `any_owned_state`, `any_controlled_state` and `any_of_scopes` predicates, nonempty MIO inventory, and global-clock retaliation expiry are not modeled or executed.
The nonquarantined sanctions reward path is not executed here, including `clamp_variable`, `condemnation_apply_response_duration` and `cbrn_achievement_record_stockpile_destruction`.
Nonzero sanctions free-stock mutation is explicitly rejected by this bounded interpreter instead of being claimed as covered.
There are no unresolved native leaves on the assigned executed caller scenarios.
Target-specific retaliation expiry and its global clock are outside these scenarios, which use unrestricted strategic policy and explicit denial cases.
The small selector loop model rejects more than 1,000 rows and mutation of its iterated array rather than pretending to prove recovery of a large selected queue.
The long-registry test proves only that the counter helper does not scan that registry.
Parent review and another run after integration are required.

## References and MCP limits

Read inputs: `AGENTS.md`, events and subagents skills, [architecture handoff](032_chemical_escrow_api_architecture_2026-10-07.md), and [native primitives handoff](032_chemical_native_primitives_2026-10-07.md).
Existing dynamic helper source and documentation were inspected.
No skill was created or updated.

Local sections read, with SHA-256 revisions:

| Source | Lines | Revision |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 435-443, 543-555, 1213-1234 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 254-270 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 66-88 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Installed `documentation\effects_documentation.md` | 1252-1266, 4279-4304, 4833-4853, 6476-6492, 6730-6763, 7820-7841 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | 2110-2136, 3991-4003, 4827-4839, 5006-5018, 5024-5037, 7450-7466 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\script_concept_documentation.md` | 216-223 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

Installed paths are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Reference tools were exposed and `hoi4.reference_search` returned the temporary-lifetime section at line 440 under the wiki revision above.
Its subsequent revision-bound `hoi4.reference_read` yielded no result during the bounded wait and the waiting execution was terminated, with no result, job handle or artifact observed.
The local section was read directly, and the request outcome remains unobserved rather than declared a server failure.
No domain MCP/engine proof or new artifact is claimed by this offline test assignment.
Prior domain artifact references and their limitations remain in the native primitives handoff.

## Bounded consequence-dispatch follow-up, 2026-10-07

Disposition: `blocked` for the requested additional regression.
Acceptance basis: the parent requested inspection first and explicitly directed return of exact missing evidence if full dispatch requires substantial unsupported interpreter expansion.
Only this handoff changed in this follow-up.
The test script and all gameplay files remain unchanged, with no success stubs, additional tooling, agents, Git writes, game launch or log search.

The exact adapter is `missiles_dispatch_chemical_payload` at `common\scripted_effects\032_missiles_operations_effects.txt`:4372, not `missiles_dispatch_chemical_consequence`.
Its caller-owned action/protection/result outputs are visibly initialized before nested calls.
`cbrn_calculate_chemical_action_outputs` at `cbrn_exposure_effects.txt`:319 initializes private route/class/agent profile output storage.
`cbrn_resolve_action_target_protection` at `cbrn_protection_effects.txt`:1028 initializes outputs consumed after the nested protection calculator returns.
Source presence of those initializers does not prove survival through the full consequence chain.

A read-only in-memory diagnostic used the existing interpreter and real Event32 reserve/consume fixture, then parsed the actual dispatch body and protection helper definitions without altering them.
The scenario supplied paid quantity 240, frozen Chlorine agent 101, one native debit, the exact impact-state pointer and on-target guidance.
It stopped at `Unmodeled command controller at source line 1041` inside the real `cbrn_resolve_action_target_protection`, reached from the real missile dispatcher.
There was still exactly one native stock call after that stop.
This lowercase scope spelling is an initial interpreter gap, not a gameplay defect.
No calculation result, protection proof, contamination, deaths, evidence, Condemnation or completed dispatch was established by that diagnostic.
Its partial trace is not included in the 39-method or 80-definition passing coverage totals.

Source review identifies the additional required gaps beyond scope-case normalization:

- Protection snapshots require normal-variable `clamp_variable`, `round_variable` and `divide_variable`, temporary division, `num_equipment_in_armies@...`, `deployed_army_manpower_k`, `state_population_k`, and real `every_controlled_state` pooling.
  Examples are `cbrn_protection_effects.txt`:197, 607-623, 867-900 and 911.
- The calculator requires `divide_temp_variable` at `cbrn_exposure_effects.txt`:347 and executes actual country snapshots and route/class/agent setters.
  Those calculations cannot be replaced by neutral or accepted-output fixtures without losing the requested evidence.
- Unit consequences require native `damage_units` with its target/war/faction filters at `cbrn_consequence_effects.txt`:161 and 190.
- State consequences require `global.num_days` at line 241, actual `chaos_meter_register_state_civilian_deaths_percent` at line 257, actual contamination/evidence helpers, and scheduled `state_event` calls at lines 303, 321 and 356.
  Continuing contamination modifier/death scheduling, strategic mask losses and achievement hooks also remain outside the interpreter's current closure.
- Condemnation requires the real `condemnation_add_source` at `cbrn_consequence_effects.txt`:477, including liability/relief accounting and its history/treaty consumers.
  A recorded call with fabricated success cannot prove those effects.
- The adapter invokes `humanitarian_corridor_handle_exact_state_attack`, whose body at `humanitarian_corridor_effects.txt`:1021 requires a global sparse-country registry and `for_each_scope_loop` even when the local contract branch is inactive.

The following source observation describes the raw helper's record boundary, not a confirmed caller defect or an independent-idempotence requirement.
Each call to the missile dispatcher initializes `cbrn_action_dispatch_proof` to missing, then `cbrn_reset_action_context` resets it again at `cbrn_exposure_effects.txt`:1170.
The shared dispatcher at `cbrn_consequence_effects.txt`:612 guards only that temporary action proof and marks it supplied within the current call.
The missile adapter neither consumes nor clears `missiles_operation_payload_debit_verified` after dispatch, while cleanup clears it later at `032_missiles_operations_effects.txt`:6257.
Thus the raw helper's temporary proof protects the current action record rather than establishing durable per-operation idempotence on arbitrary reentry.
The normal resolution path invokes cleanup, so this is not an executed claim of duplicate live consequences.
Per the parent's clarification, no-duplicate release is evaluated at the owning commit/consume boundary rather than by independently recalling the raw consequence helper.
The additional owning-consumer regression below establishes once-only consumption and loss of fresh release eligibility, while full commit/resolution/consequence execution remains outside coverage.

Existing suite validation was rerun on current source: all 39 methods pass with 80 executed helper definitions, comprising 66 CBRN, 12 Event32 and two sanctions helpers.
No consequence-dispatch test was added and no successful consequence execution is claimed.
Parent follow-up is a separately bounded full-chain execution harness or native evidence covering the listed calculations and consequence owners, with duplicate validation at the owning commit/consume boundary.

Inspected consequence source identities:

| Source under `common\scripted_effects` | SHA-256 |
| --- | --- |
| `032_missiles_operations_effects.txt` | `ad7a67b56b157a76336bf7e9a3887c6ccc12442b8023518541b4e80bafa40953` |
| `cbrn_protection_effects.txt` | `9f3b758880f3cdff6fe6a536745b36c78628d7a60e237b5b9b7f12207ef5a8d3` |
| `cbrn_exposure_effects.txt` | `bb23620b4f16f62b4f808b3524b6a59e6bcf57a12f62802c816b1ceb824aae72` |
| `cbrn_consequence_effects.txt` | `43b8546fb77cf3086940020739f8f9f6e29d8dbe513b12b1e1387219f643692b` |
| `cbrn_diplomacy_effects.txt` | `60b8c4c70a018328e64f19c8e2c5caf7cbbbfcbb99928f5c0b538b1d53278042` |
| `cbrn_doctrine_effects.txt` | `32f684dc0022b2bc0149a06028ed9a8a158222df8b21630f20102999f4523d18` |
| `humanitarian_corridor_effects.txt` | `d7efe1857b3e79936ce0a44e857277606d73cd82f312c9bdb540224023661159` |

## Owning commit/consume boundary clarification, 2026-10-07

Acceptance basis: the parent specified the owning commit/consume boundary for duplicate-release checks, reported the commit invalidation repair, and kept broader sequence/no-recursion work separate.
The source inspection confirms that `missiles_operation_preparation_remains_valid` requires the paid chemical receipt at `032_missiles_operations_triggers.txt`:269-273.
It also confirms `missiles_record_preparation_failure` checks chemical receipt failure at operations effects:3573-3579, and the final uncommitted invalidation branch calls that reason helper, abort and cleanup at lines 6173-6178.
Those commit/cleanup observations are source evidence, not an executed commit test in this fixture.
Full commit execution still requires the previously listed program/site predicates, global date, scoped-site iteration and native mission cancellation.

One actual-source test was added at `missiles_consume_special_payload`, which delegates the chemical branch through `missiles_consume_chemical_payload` to the real receipt consumer.
The first call publishes paid 240 and fresh debit verification, closes the chemical hold, and makes no second native debit.
The second owning-consumer call publishes zero and clears debit verification, so the caller no longer has fresh release eligibility.
Two subsequent chemical cleanup-release calls neither refund the consumed material nor create another stock call.
The row's consumed total stays 240 and returned total stays zero.
No authorization/payment/consequence success stub was used, and no raw consequence-helper reentry was asserted as a valid production sequence.

Current validation passes all 40 methods and executes 82 production helpers, comprising 66 CBRN, 14 Event32 and two sanctions helpers.
Only the owned test and this handoff changed, with no gameplay/Git writes or additional tooling.
The parent's 137-event-test run was reported as ongoing and pending final results, and is not claimed as passed here.
The full consequence regression remains blocked and excluded from coverage, while the requested bounded owning-consumer duplicate check is implemented.

## Parent integration and quote tests

The parent added three actual-source preparation-quote tests after the worker handoff and reran the suite: 43 methods pass, executing 87 production helpers (68 CBRN, 17 Event 032 and two sanctions).
The exact shared chemical stock quote checks all nine agents at 239, 240 and 241 prepared lots against the unchanged strategic-route cost, rejects a different active profile and makes no native mutation.
The consumer-slot quote blocks a current unresolved hold but does not mistake a copied foreign ledger marker for this country's hold.
The actual Event 032 selected-payload predicate checks all nine chemical agents, all four biological agents and both nuclear families at missing/sufficient inventory and lost technology boundaries.
Nuclear inventory is an explicit COUNTRY-native scenario fact for `num_of_nukes`, following installed `triggers_documentation.md:6813–6820` under the previously recorded revision; it is not a mocked payment or nuclear-custody claim.
The parent reran the complete Event 032 source-contract suite: 139 tests pass, including conventional-versus-special fee gating, chemical failure cleanup and the removal wrapper's private loop-break initializer.
The broader consequence and native callback limits above remain unchanged.
