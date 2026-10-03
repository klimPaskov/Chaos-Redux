# Event 026 exact quotation implementation

Disposition: implemented in source; required MCP/native execution and consumer-performance evidence remain blocked or unresolved.
Acceptance basis: the current parent/user assignment explicitly authorizes the full reusable exact cost framework, the central `black_friday_quote_custom_cost` block, matching arithmetic/cache helpers, constants, and documentation.
This handoff continues [the reviewed quantization audit](2026-10-03_quantization_audit.md) and supersedes its queued scalar-repair architecture for this implementation surface.
It does not establish completion of Event 026 or of the parent's owner-adapter bundle.

## Completed implementation

The effect and central read-only trigger now invoke one `universal_cost_quote_exact` producer.
It extracts represented five-decimal inputs into radix-1000 integer limbs, multiplies every eligible source exactly, shifts the denominator's low limbs into a positive sticky fraction, divides the high integer part by arbitrary represented quantum ticks, and takes one exact ceiling.
It does not construct a large scalar `C*100000`, `C*R`, or `C/Q`, or use a truncated composed-ratio scalar as a price input.
The positive minimum follows from the exact ceiling, including products far below scalar precision.

New engine-capability finding: installed documentation exposes `all_of_scopes`, temporary array resizing/mutation, and temporary arithmetic as triggers.
The offline wiki explicitly describes ordered `all_` iteration and temporary array use in trigger blocks.
An array filled with the existing current `THIS` pointer can therefore provide iteration tokens for read-only arithmetic without interpreting numeric digits as scopes, generating localisation code, or adding an effect loop.
This documented route is implemented and exercised by the source interpreter; native duplicate-preserving traversal and temporary lifetime remain an engine-evidence limit.

Primary-source selection still uses minimum priority and earliest registry row for a tie.
Exact multiplication is commutative, so price traversal uses stored rows without sorting or a source-count-limited effect loop.
The family matcher subtracts each extracted low bit before dividing by two, preventing fractional residues from leaking into higher family bits.
It covers every accepted low-thirty-bit source mask and caller family combination rather than twelve canonical family rows.

The exact source cache is the live aligned source registry itself.
Existing register/clear cache entry points retain the Event 026 readiness marker and remove twelve retired scalar cache variables.
Source-identified clear removes only its own aligned row and preserves other sources and all historical receipt amounts.
Register/upsert/clear source lookup also uses current-scope token iteration, so an existing row beyond 1,000 is found correctly.

## Files changed and boundaries

All paths below are relative to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

| File | This tranche's change |
| --- | --- |
| `common\scripted_effects\chaosx_universal_cost_effects.txt` | source finder calls, exact matcher/quantizer/quote frontends, retired-cache cleanup, quoted-affordability validity gate |
| `common\scripted_effects\chaosx_universal_cost_effects.md` | public contracts, inputs/outputs, defaults, side effects, examples, cache migration and validity semantics |
| `common\scripted_triggers\chaosx_universal_cost_exact_triggers.txt` | implemented shared producer and nine internal exact arithmetic/registry predicates |
| `common\scripted_triggers\chaosx_universal_cost_exact_triggers.md` | complete helper map, arithmetic bounds, iteration capability, lifecycle, limitations and validation links |
| `common\scripted_triggers\026_black_friday_triggers.txt` | only `black_friday_quote_custom_cost`, including its consumed optional quantum override and hidden arithmetic producer call |
| `common\script_constants\chaosx_universal_cost_constants.txt` | `universal_cost_exact` representation constants; no sale tuning change |
| `common\scripted_effects\chaosx_dynamic_effects.md` | existing framework index row links to the exact predicate implementation and contracts |
| `docs\systems\universal_cost_modifier.md` | authoritative arithmetic/cache/validity contract and helper map |
| `docs\plans\026_black_friday_plans\subagent_handoffs\exact_quote_source_tests.js` | parser/interpreter of the actual helper bodies and independent direct BigInt rational oracle |
| `docs\plans\026_black_friday_plans\subagent_handoffs\exact_quote_source_results.json` | exact scenario results and hashes of the tested runtime files |
| `docs\plans\026_black_friday_plans\subagent_handoffs\exact_quote_route_evidence.json` | observed MCP outcomes and preserved effect-definition evidence |
| this handoff | implementation, ownership, reference and evidence limits |

Thirteen other effect definitions, including source wrappers, native debit/credit, recording, settlement, component-chain validation, and refund bodies, were compared with the pre-edit read and are unchanged after newline normalization.
The entire Black Friday trigger file outside the one assigned block was likewise compared and left unchanged.
Existing unrelated shared-worktree changes were preserved.
No owner file, lifecycle hook, achievement, catalog, asset, focus, GUI layout, AI weight, or event enablement was patched.
No game process was launched and no commit was created, following the explicit instruction not to commit mixed main files.

## Helper map and call sites

The [matching exact predicate documentation](../../../../common/scripted_triggers/chaosx_universal_cost_exact_triggers.md#internal-helper-map) lists every internal helper's selected scope, inputs, outputs, defaults, side effects, and direct callers.

| Public/bridge helper | Scope | Inputs | Outputs | Direct call site or side effect |
| --- | --- | --- | --- | --- |
| `universal_cost_quote_exact` | existing payer/owner-selected object trigger | current ordinary cost, family mask, optional quantum, live source registry | exact final/displayed/saved amount, source count/primary ID, validity | effect quote and central Black Friday bridge; temporary arithmetic only |
| `universal_cost_quote_integer` | same selected object effect | same public quote inputs | same public quote outputs | existing owner call sites retained; invokes the producer in `if.limit` |
| `black_friday_quote_custom_cost` | current payer trigger | ordinary cost, family mask; optional `black_friday_quote_requested_quantum` | final amount, effective quantum, validity | all existing owner trigger call sites retained; active/readiness gates preserved |
| `universal_cost_round_up_to_quantum` | selected object effect | represented amount and optional quantum | exact amount, amount-validity, scalar units/units-validity, exact unit limbs | existing API invokes `universal_cost_exact_quantize_scalar` |
| `universal_cost_source_register` / `universal_cost_source_clear` | existing owner effect scope | existing source registration/identity inputs | unchanged result fields | invokes `universal_cost_exact_find_source`; mutates only the matching aligned row |
| `universal_cost_rebuild_custom_quote_ratio_cache` / `universal_cost_clear_custom_quote_ratio_cache` | existing owner effect scope | existing registry mutation/lifecycle context | existing readiness marker | removes retired scalar fields; preserves exact registry and payer receipts |
| `universal_cost_check_quote_affordable` | payer effect scope | fresh quote validity, amount, resource kind | affordability result | invalid quotes are rejected before the existing native-resource predicate |

The Black Friday bridge keeps one-unit defaults and .01 Stability/War Support defaults.
A generic positive quantum override is consumed and reset, so it cannot silently govern the next owner call in the same temporary context.
The standalone quantizer uses its own quantum scratch and does not replace a surrounding quote's quantum input.
The producer's loop bodies remain true; validity is data checked by the bridge/caller, not a premature iteration stop.

## Constants and tuning

`universal_cost_exact` defines radix 1000, largest digit 999, tick scale 100000, decimal split 10/100, five scalar limbs, six division limbs, ten quotient-digit search steps, three denominator limbs per source, and the five positive-envelope tick limbs.
These are representation constants, not balance values or limits on product length/source count.
The scalar envelope follows the required offline variable documentation, not deprecated manpower-reader limits.
Basis 10000, sale ratios 5000/2500, registration domains, family masks, owner ordinary modifiers, and registered consumer quanta remain unchanged.
The existing comparison epsilon is not used by quotation arithmetic.

## Event targets, cache and cleanup

No event target, new persistent flag, per-payer quote cache, recurring hook, daily world scan, or enablement is required.
Scratch arrays are cleared before reuse and remain temporary in the selecting trigger/effect chain.
Separate token arrays prevent nested arithmetic from mutating an active iterator.
Retired scalar cache variables are removed only through the existing publication/expiry helpers.
Clearing source 26 invalidates Black Friday readiness but keeps other live source rows usable by generic exact quotations.
The actual-paid receipt basis is never recomputed from later source state.

## Migration and compatibility

The existing effect quote, standalone quantizer, family matcher, source mutation entry points, and central custom-cost trigger are migrated together.
Owner current-price providers, eligibility, payment, receipt recording, refunds, and call sites remain in their original files.
There is no unused proposal-only runtime helper.

The scalar `universal_cost_quote_composed_ratio` / `black_friday_quote_composed_ratio` output is retired: basis without participating sources and zero meaning unavailable with participating sources.
Zero in this retired field is never a zero price or invalid product.
No runtime consumer outside the replaced effect/cache/bridge implementation read it in the inspected repository.
New consumers must use source proof and the exact quote, not reconstruct price from that field.

A mathematical price beyond the represented scalar envelope is invalid, never saturated or substituted as an accepted quote.
The Black Friday bridge and shared quoted-affordability effect reject it.
Owner-specific confirmation/payment providers must honor `universal_cost_quote_valid` as well.
This arithmetic change does not establish native-cost universality or close inaccessible owner payment surfaces.

## Meaningful validation

Run from the mod root:

```powershell
node docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js
```

The test parser executes the actual checked-in Clausewitz helper definitions and their real effect/trigger call paths.
Its reference uses direct BigInt rational numerators/denominators rather than limb arithmetic or a copied quote implementation.
Every tested temporary operation is checked against the documented represented envelope; every division and multiplication must retain full represented precision.
Array indexing must address an existing element and iterator token arrays must remain unchanged throughout traversal.

434 named quotation scenarios passed across the read-only producer, actual effect frontend, and actual central Black Friday bridge where its positive-family contract applies.
56 standalone quantizer scenarios, nine register/upsert/clear mutations, two mutation no-ops, five family-default/override cross-call checks, three absent-quantum checks, and two invalid-quote affordability gates also passed.
Actual multiplication traversed 1,005 limbs, and quotes traversed 1,105 identity and 1,105 non-identity sources.
The largest observed bounded digit accumulator was 999999, matching the formal bound.
Tests cover small 0/1/2/3/5/101 prices, surcharge-adjusted 125, tiny 0.00001 costs, million-unit costs, the documented scalar maximum, multiple sources and reverse order, high/combined family masks, exclusions, generic multi-limb quanta, positive minimum, zero/rewards, expiry, and receipt preservation.

| Case | Exact tested result |
| --- | ---: |
| C=2.00001, Q=1, R=5000 | 2 |
| C=.04001, Q=.01, R=2500 | .02 |
| C=1000000, Q=1, R=5000 | 500000 |
| C=2, Q=1, R=9999.99999 then 5000.00001, either order | 2 |
| C=1000000, Q=.00003, 1,105 sources with R=.00001 | .00003 |
| C=125 with two 5000 sources, one remaining, then none | 32, 63, 125; stored actual-paid 32 unchanged |
| C=2147483647.99999, Q=.00001, identity source | 2147483647.99999 |
| C=2147483647.99999, Q=2000000000, identity source | validity zero; mathematical 4000000000 is not representable |

[Exact scenario artifact](exact_quote_source_results.json) contains the full named fixture/result inventory and tested runtime SHA-256 identities.
This is source-semantic evidence under documented operations, not observed engine affordability, debit, save/reload, performance, or native-consumer evidence.

## Local reference evidence

No Paradox wiki web access was used.
The following sections were read directly because no revision-bound reference citations returned from the MCP requests.
Paths under `documentation` and vanilla `common` below resolve under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Wiki paths resolve under the repository's offline `paradox_wiki` folder.

| Source | Read spans / relevance | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 264-328 event-target lifecycle; 425-490 represented variables, unscoped temporary lifetime and ordered trigger evaluation; 1070-1111 temporary arrays and indexed elements | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 739-777 array scopes and `all_of_scopes` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 2319-2402 meta-trigger arguments and ordinary scripted-trigger calls; no recursive meta generator is introduced | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | scripted-effect definition/call sections 4685-4700 consulted alongside existing dynamic/meta helper examples | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 184-206 five-decimal formatting; 657-692 scripted localisation and recursive text capability, which this implementation does not need | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `documentation\triggers_documentation.md` | 698-724 temporary arrays/arithmetic; 1052-1067 array iteration; 2110-2136 variable comparisons; 2605-2622 division; 5006-5016 existence; 5166-5181 conditional trigger; 6404-6475 meta/math; 7414-7434 resizing; 7482-7502 assignment | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `documentation\effects_documentation.md` | 2773-2783 variable cleanup; 3587-3611 division; 4986-5028 modulo/multiplication; 6476-6509 rounding and event-target declarations | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `documentation\script_concept_documentation.md` | 184-245 fixed-point math and cross-file script constants | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `documentation\script_math_functions.md` | enumerated arithmetic functions searched; 211-227 modulo/multiplication sections read | `3c7116906f0bc7590cdd014f5a8b3cf8ef9f0685044fc10e29fabd19afaf832b` |
| `common\script_constants\documentation.md` | 1-84 constant schema, fixed-point/int data and scoped constant access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `common\scripted_effects\00_scripted_effects.txt` | 498-522 vanilla `all_of_scopes` temporary arithmetic inside an effect limit | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |
| `common\scripted_localisation\00_scripted_localisation.txt` | 1-42 installed localisation documentation comments and `defined_text` precedent | `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587` |

The initially guessed `documentation\scripted_localisation_documentation.md` does not exist in this installation; the installed scripted-localisation source comments were read instead.
Existing `chaosx_dynamic_effects.txt` and its markdown were inspected before introducing the new arithmetic predicates.
They provide no exact limb quotation helper to reuse.
Installed documents do not independently prove the variable envelope, low-level multiplication/division intermediate widths, duplicate-preserving synthetic token iteration, or all consumer runtime behavior.
Those fields remain unsupported engine analysis, not invented findings.

## MCP evidence and precise blockers

The live connected catalog exposes reference context/search/read, source lookup, event inspect/render/compare, and decision inspect.
It does not expose `hoi4.script_validate`, a server health route, or a server version route in this session.
Job/helper-expansion/native-task routes were not used without the required health/version/task-negotiation verification.
No returned artifact URI, continuation URI, source revision, scenario coverage, or completed helper projection exists for this tranche.

Initial context, `meta_trigger` reference search, no-reference 20-line `universal_cost_quote_integer` source lookup, and the narrow Event 026 trace returned no result during measured 20,000 ms observation windows.
Narrower `all_of_scopes` reference search, no-reference 20-line central-trigger source lookup, and two-node event render likewise returned no result within 15,000 ms windows.
The after-change two-node event trace returned no result within 15,000 ms.
These are bounded missing-result observations, not invented completed tool timeouts or a claim that the server is absent.

The initial decision inspect returned `Decision inspection requires declared scenarios at scenarios`.
It was corrected with a named explicit GER scenario; the corrected request returned no result within 20,000 ms.
The initial event compare returned `expected string, received undefined at proposedSources[0].source` and `Unrecognized key: "content"`.
It was corrected to `source` with the pre-edit effect overlay; the corrected request returned no result within 20,000 ms.
The validation responses prove those requests reached schema validation, not that inspection/rendering completed or that service health is established.
No reference IDs/revisions returned for a valid `reference_read` request.
[Route evidence](exact_quote_route_evidence.json) records the observed responses.

Even a returned narrow event trace would not prove the helper closure: the events skill documents the focused-analysis boundary.
Recover helper/source/scenario evidence through an appropriately supported full route once the service responds.
Cost ratios here are deterministic payment fractions, not AI weights, candidate probabilities, MTTH, or random-selection scores.
No probability-bearing surface or AI patch is included, so no probability auditor result is claimed or substituted.

## Simplifications, omissions, and remaining work

No approximation, forced epsilon, narrower ratio/cost/quantum/source-count domain, fallback payment, new daily/world hook, event enablement, or native-cost universality claim was introduced.
The exact quotation implementation is present and source-tested rather than another report-only scalar proposal.

Required MCP helper inspection/comparison artifacts, native arithmetic execution, duplicate-preserving token iteration, nested temporary lifetime, and decision-frame performance remain unresolved.
The interpreter assumes the documented operation semantics and cannot establish those engine facts.
The parent retains owner confirmation/payment integration and must require quote validity for owner-specific providers, including mathematical outputs that cannot fit in one engine scalar.
Existing native and inaccessible cost-surface dispositions remain unchanged.

The parent updated the comment immediately above the assigned `black_friday_quote_custom_cost` block to describe the exact producer and live registry.
That parent edit is preserved in the central-file hash captured by the lifetime follow-up tests.

No skill was modified outside the assigned write scope.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
This handoff does not request or authorize HOI4 launch, owner redesign, asset/catalog work, or a shared MCP router.

## Caller-lifetime follow-up

Disposition: implemented and source-tested under the explicitly requested conservative helper-return model.
Acceptance basis: the parent/user follow-up requires auditing all exact-helper outputs, including temporary arrays, and giving caller-owned storage before invocation.
This section supersedes the preceding temporary-lifetime uncertainty for SOURCE-model validation, while native duplicate-preserving iteration and performance remain pending.
Native confirmation of that model remains distinct evidence.

The prior interpreter retained helper-created temporaries in one shared context, so its earlier passing arithmetic results did not prove return-boundary safety.
With cleanup on every scripted return, the pre-patch actual source failed `single-0.00001-5000-1`: its final amount was one tick (`1`) instead of one quantum (`100000` ticks).
This failure was reproduced before changing the runtime helpers.

The patched caller boundaries initialize factor limb arrays at all five extraction calls; comparison and trial-product output storage at both division-trial calls; decoded scalar result/validity before both decoder calls; and scalar/unit/unit-token output storage before both product-quantizer calls.
The exact quote also initializes the family-match result before invoking the matcher.
Existing product arrays are inherited in-out buffers through multiplication, trimming and decoding, so they are preserved rather than globally reset.
Black Friday registration/clear wrappers now initialize the generic API result in their caller before invoking it.
The effect quantizer initializes its unit-limb output and optional quantum before its nested producer, and the effect quote initializes optional quantum storage before `if.limit`.
Zero/reward standalone quantization explicitly publishes zero unit limbs, preventing stale positive limbs from a preceding call.
The assigned central bridge block documents the OUTER caller's output-storage obligation; nested shared quote outputs were already initialized correctly in that block.

The VM now applies lexical cleanup to ALL scripted invocations, including effect/trigger public APIs, not merely local arithmetic helpers.
Temporary scalar and array stores are separate from regular stores.
New temporaries disappear on helper return; inherited temporaries retain modifications; regular writes persist; temporary shadowing does not erase underlying regular state.
Declared helper-output contracts are asserted at entry without automatically creating any internal scratch.
Outer test-call fixtures explicitly initialize public outputs as a conforming owner caller would.
Three negative controls invoke actual quotation APIs without outer declarations and confirm that their newly created public output names disappear, despite a successful predicate result.
These controls make the API lifetime requirement visible rather than hiding it with VM-wide preinitialization.

All 434 independent rational-oracle quotation scenarios and all 56 standalone quantizer scenarios pass under conservative cleanup.
The run checks all 19 declared exact/quote/registry-output contracts across 78,289 scripted returns, and discards 423,706 helper-created temporary names.
Additional checks cover eight lexical-model assertions, three bare-API output-loss controls, two source-wrapper result returns, four effect-family-matcher result returns, two warm zero/reward unit-array resets, arbitrary unit-limb returns, the 1,005-limb multiplication, 1,105 sources, and the unchanged registry/receipt expiry scenarios.
The [updated result artifact](exact_quote_source_results.json) contains the lifetime model, explicit outer caller declarations, every audited output contract, dynamic boundary coverage, scenarios and current runtime hashes.

Follow-up files changed: `common\scripted_triggers\chaosx_universal_cost_exact_triggers.txt`, its markdown, `common\scripted_effects\chaosx_universal_cost_effects.txt`, its markdown, only the assigned central bridge block in `026_black_friday_triggers.txt`, the actual-source VM, result/route artifacts and this handoff.
No constant, price formula, ratio domain, family domain, source-count policy, tuning, owner file, daily hook, enablement or native resource behavior changed.
Public owners must predefine every output they read after an API returns; that outer-caller integration remains with the parent.
The parent reports RSA validation under its own conservative frame model, including its repaired `black_friday_quote_final_cost` caller declaration; that report is not re-executed or substituted for these actual-source checks.

Live reference context, a narrow wiki temporary-variable search, 20-line no-reference exact-producer lookup, and narrow Event 026 inspect were retried in this follow-up.
They returned no results within measured 15,000 ms observation windows, not an absent-service finding.
Offline Data structures line 440 and 1073-1076, installed temporary-array resize documentation at 7414-7432, and the existing vanilla arithmetic-in-trigger precedent were read directly.
No reference IDs/revisions or inspection artifacts returned.
The local reference hashes remain the recorded hashes above.

Two attempts to add the lifetime paragraph to `docs\systems\universal_cost_modifier.md` failed with `Failed to write file` for that exact Windows path.
The file is readable, 17,491 bytes at inspection, `Archive`, and not read-only; no cause for the write failure is inferred.
Its existing exact-helper documentation link points to the updated lifetime contract, and the matching effect/trigger markdown examples are repaired.
The parent subsequently applied the explicit public-output caller-lifetime paragraph after the system document's public helper map.
That documentation blocker is closed by the parent; the failed write observations above are historical only.

No native game launch or commit was performed.

## Shared receipt lifetime tranche

Disposition: implemented and source-tested; native execution and engine performance remain pending.
Acceptance basis: the parent/user explicitly extended the bounded reusable-framework write authority to the shared receipt/debit/credit helpers and matching contracts/tests, while retaining ownership of Event 026 external callers and RSA replay guards.

All transaction/debit/credit definitions actually present in the assigned effect file were audited.
The file contains eleven such effect definitions; the thirteen formerly untouched definitions also included the two Black Friday source wrappers, whose return fields were repaired in the exact-lifetime tranche.
The receipt suite exercises thirteen real shared API contracts: all eleven effect definitions plus the native-affordability and native-kind scripted triggers.
No shared receipt API is mocked and no declared effect definition was omitted because of the count difference.

The pre-patch actual-source test failed at its first record: `caller lacks temporary output universal_cost_transaction_found_index before universal_cost_find_transaction_row`.
That defect occurs inside the real record API, independently of owner adapter mocks.
The component finder had the same missing nested transaction-lookup storage; settlement, acknowledgement and refund likewise relied on new lookup temporaries escaping helper return.
Record additionally relies on the returned transaction pointer, so all four caller-visible transaction lookup fields are covered.

Six effect bodies receive caller-local declarations: `universal_cost_find_component_row`, `universal_cost_record_transaction`, `universal_cost_settle_transaction`, `universal_cost_mark_component_refunded`, `universal_cost_refund_component_at_cursor`, and `universal_cost_refund_transaction`.
The five nested transaction lookups initialize found index, indexed flag, result and pointer before the call.
The two nested component lookups initialize component index/result before the call.
Refund initializes chain validity before validation, and its component callback initializes credit result before credit dispatch.
The change adds 26 temporary-output declarations and five explanatory comments only.
Existing refund cursors, cumulative totals and incomplete flags remain inherited state rather than being globally reset.
Regular receipt arrays, targeted row pointers, resource dispatch, lifecycle conditions, component/legacy bounds, amounts and tuning are unchanged.

The actual-source VM is now importable without running its arithmetic suite.
The uniquely named [receipt test artifact](universal_cost_receipt_lifetime_source_tests.js) imports that same interpreter, executes real receipt helper definitions, and loads the real `universal_cost_component_is_affordable` / `universal_cost_resource_kind_is_native` predicates.
Native resource reads/writes alone are modeled.
Targeted numeric keys follow offline Data structures line 551, and effect-loop iteration follows the documented existing 1,000-iteration default.
The normal allocator proof is seeded as persisted fixture data, then validated and consumed by the actual record API; no allocator runtime completion is claimed.

44 receipt/native-dispatch scenarios pass across 2,411 real scripted returns, with 13,162 helper-local temporary names discarded.
The suite validates all 29 native debit/credit dispatch branches, using .07 payments and .5 starting balances for Stability/War Support rather than an invalid whole-number resource range.
It covers cold record/append/lookup, valid component-chain return, settlement/repeat/no-refund behavior, duplicate components, consumed/missing allocator proofs, mismatched actual paid amounts, owner-credited partial refunds, repeated acknowledgement, zero-paid components, warm outer cursors, corrupt row pointers/next links/cycles/tails/counts, payer isolation, interleaved chains, mapless legacy behavior, and indexed rows beyond 1,000.
The integration case executes actual quote, debit, record, source expiry and refund APIs: ordinary 125 becomes quoted/paid 63, expiry restores ordinary quote 125, and refund still credits only stored actual-paid 63.
The [receipt result artifact](universal_cost_receipt_lifetime_source_results.json) records named scenarios, all API output contracts, dynamic boundary counts and complete tested source hashes.

The full 434 quotation and 56 quantizer scenarios were rerun on the final receipt-patched effect source and still pass under conservative cleanup.
Both result artifacts now identify effect source `a0fe5277e7251fc5ee8164f71128f0b836ce6be39dc93d06562620d27b0a633c` and the parent-header-preserving central source `6ffc13f17e09feebf68c35aec7ec4424ed6540f9771d4f1d10eaff05afb5f716`.

Receipt-tranche files changed: the six effect bodies in `common\scripted_effects\chaosx_universal_cost_effects.txt`, matching effect markdown, the shared actual-source VM, new uniquely named receipt test/result artifacts, updated quotation results, and this existing handoff.
No owner/Event 026 external-caller file, RSA event or regional-request guard, native resource effect body, script constant, daily hook, enablement, AI, asset, catalog or gameplay tuning is changed by this tranche.
The parent is separately initializing owner-visible outputs around external find calls and reports RSA adapter tests with mocked core APIs; those observations are neither re-executed here nor substituted for the real shared-source tests.

The matching [framework contract](../../../../common/scripted_effects/chaosx_universal_cost_effects.md#receipt-api-temporary-return-contract) lists every caller-visible field and supplies an explicit lookup example.
An outer caller must predefine the public receipt outputs it reads after return; private scratch from record/settle/refund does not become an exported API merely because a nested helper computed it.
Native resource arithmetic, real consumer execution, persistence through save/reload, duplicate-preserving scope-token iteration and performance remain separate pending engine evidence.
No simplification, approximation, balance change, fallback, commit or HOI4 launch was introduced.

## Read-only BF receipt-scanner closure

Acceptance basis: the parent/user explicitly requested actual-source coverage of `black_friday_scan_receipt_non_political_payment` and `black_friday_scan_receipt_political_power_only`, while reserving all `026_black_friday_effects.txt` writes to the parent and outer-caller worker.
Neither scanner nor any other owning BF effect was edited by this worker.
The receipt suite loads those two actual bodies and the required actual Black Friday constants, then invokes them after real core record, settlement and refund operations.
Both public outputs, `black_friday_purchase_receipt_proof_valid` and `black_friday_purchase_has_non_political_paid_component`, are explicitly initialized in the fixture caller before every scanner invocation.
No scanner or core receipt API is mocked.

The final suite passes 45 named scenarios, including 17 scanner checks, across fifteen actual shared/scanner API contracts.
Recorded PP, settled PP, recorded/settled mixed, fully refunded mixed, absent warm-caller, wrong component source and wrong family inputs are covered.
The native dispatch/lifecycle scenarios remain covered, and the independent 434 quote / 56 quantizer scenarios still pass after the final shared-source and VM changes.

| Receipt/input | Non-political scanner `(proof, nonPP)` | PP-only scanner `(proof, nonPP)` |
| --- | --- | --- |
| recorded PP, expected paid 5 | `(1,0)` | `(0,0)` |
| settled PP, expected paid 5 | `(1,0)` | `(1,0)` |
| recorded mixed PP5+CP3, expected aggregate 8 | `(1,1)` | `(0,0)` |
| settled mixed PP5+CP3, expected aggregate 8 | `(1,1)` | `(0,0)` |
| settled mixed PP5+CP3, expected PP component 5 | `(1,1)` | `(1,0)` |
| fully refunded mixed | `(1,0)` | `(0,0)` |
| absent receipt in a warm caller | `(0,0)` | `(0,0)` |

Meaningful source limit: the PP-only scanner proves the designated positive unrefunded PP component when its source, family, state and amount match; it does not independently reject other positive paid components in the same settled receipt.
A matching component-cost input of 5 therefore succeeds for the settled mixed fixture, while an aggregate input of 8 fails.
The non-political scanner's proof-valid field means an indexed receipt was found; a refunded indexed receipt can still have proof-valid one while its positive unrefunded non-political count is zero.
These are observed source semantics, not a design change, whole-achievement proof or native claim.
The parent controls the mode/input selection and outer achievement caller integration.

The [frozen receipt evidence](universal_cost_receipt_lifetime_source_results.json) stores the exact parsed scanner bodies, their semantic AST hashes, captured BF/constant-file SHA-256 identities, and the before/end concurrency comparison.
The earlier scanner run captured BF file `f6732fd015b6fefdc0dd7172c8e7bfa392ab9b5488879e17961eab3aa2e58362`.
The final rerun captured `62398cd3d6bd431b54d36190f497913a3ebe44c8be02d0abc06f2e3806fd727b`, reflecting concurrent outer-worker file edits between runs; that final file and both selected scanner bodies were unchanged throughout the completed final run.
The arithmetic rerun captured central trigger file `53783b7a3d8b125eb1c24bef6f59cdfd6b5265b89a0f6cfc67e45948afb43d5b` after outer-caller updates, superseding the earlier whole-file hash in this handoff.
Subsequent outer-caller edits can change whole-file hashes; archived snapshots must not be represented as newer source or native coverage.

Source preservation was checked for all eleven core transaction/debit/credit effect definitions against the pre-receipt source.
After removing only the 26 new caller-output declarations and five associated comments, each definition matches its prior body after newline normalization.
This establishes preservation of normal-variable/array writes, native effect statements, guards, loop bounds, resource values and tuning.
The result artifact records every checked helper name and result.
Both evidence files were verified as single parseable JSON objects containing the final result set and source hashes.

The parent owns and is separately repairing the three BF external transaction-finder callers, three component-finder callers, achievement scanner callers, and remaining outer outputs in `026` effects/triggers/localisation.
Those edits are read-only inputs here and are not replaced with adapter mocks.
RSA counts supplied by the parent remain external reports; these actual shared-source tests do not infer native coverage from them.
