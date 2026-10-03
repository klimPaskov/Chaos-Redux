# Event 012 truck and artillery helper implementation, 2026-10-03

## Disposition and authority

Disposition: **implemented for the bounded helper lane, with source acceptance only**.
Acceptance basis: the parent assignment explicitly authorized exactly these four files, the two subtype IDs, reserve/need/quote formulas, artillery-first selection, caller-owned temporary inputs, static native transfer branches, and parent ownership of constants/core lifecycle/receipts/localisation/commit.
The accepted queued design is `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_mobile_artillery_design_2026-10-03.md`.
Its parameter-shaped proposals and examples are superseded for this lane by the assignment's `= yes` and caller-temp contract.
No Git command or index operation was performed.
No HOI4 process was launched.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, with AGENTS and existing dynamic-helper documentation read before implementation.
No skill was created or changed because the write boundary permits only this helper lane and its handoff.

The helper implementation is delivered, while final owner integration, audit and gameplay completion remain parent-owned.
No simplification of either truck or artillery helper coverage was made.
The parent's subsequent source review explicitly required outer-frame measurement initialization, absent failed-quote identity and matching subtype tooltips.
Those changes are included and the source acceptance scenarios were rerun against their final definitions.
Parent core wiring and its `012_africa_gods_mobile_contract_effects.txt` payment-type binder are parent-owned.
The parent subsequently reported core completion after cleanup/rollback wiring.
That is parent-reported integration status and was not duplicated or independently audited by this documentation lane.

## Files and helper map

| Changed file | Delivered surface |
| --- | --- |
| `common\scripted_effects\012_africa_gods_equipment_effects.txt` | Added host need profile at line 93, participant typed quote at line 136, and participant native sender at line 199, plus one overview comment |
| `common\scripted_triggers\012_africa_gods_equipment_triggers.txt` | Added subtype validator at line 79 and matching capacity at line 89, plus one overview comment |
| `common\scripted_effects\012_africa_gods_equipment_effects.md` | Added the mobile API, caller initialization, formulas, examples, constants contract, lifecycle ownership and source references from line 84 |
| This handoff | Source acceptance, snapshots, validation limits and owner follow-up |

| Helper | Scope and inputs | Outputs/defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `gods_of_africa_mobile_type_is_valid` | COUNTRY, temporary `gods_of_africa_mobile_type` | Boolean, only trucks 1 or artillery 2 accepted, no type default | No mutation, called by mobile capacity and parent typed contract/payment/offer validators |
| `gods_of_africa_mobile_capacity_is_sufficient` | COUNTRY, temporary type and `gods_of_africa_mobile_required_amount` | Boolean, optional temporary stock/target/fielded/deficit/reserve/spare, no required-amount default | Recomputes matching archetype only, rejects negative/fractional requirements, accepts zero measurement request, called by quote and parent full/partial/substitute/transfer capacity gates |
| `gods_of_africa_build_mobile_need_profile` | Authoritative host COUNTRY, native stock/army reads and existing logistics/arsenal flags | Normal host `gods_of_africa_truck_need_amount`, `gods_of_africa_artillery_need_amount`, both refreshed including zero | Scratch arithmetic and normal output overwrite, two nested calls to preserved `gods_of_africa_floor_equipment_amount`, parent call site `gods_of_africa_build_need_profile` |
| `gods_of_africa_quote_mobile_tribute` | Participant COUNTRY, living explicit `africa_host`, refreshed integral host need quantities | Normal participant `gods_of_africa_mobile_quote_type`, `gods_of_africa_mobile_quote_amount`, `gods_of_africa_mobile_quote_ceiling`, type cleared and amount/ceiling zeroed at entry | Artillery first, independent truck fallback, matching spare and subtype maximum, no equipment or success accounting, parent call site demand selector |
| `gods_of_africa_send_mobile_tribute` | Participant COUNTRY, normal payment subtype/amount and explicit `africa_host`, parent preflight | Exactly one native matching-archetype transfer, no receipt output or inferred type/amount | Exclusive `send_equipment` branches, no replacement grant, counters, history, success write or remaining-balance mutation, parent family-2 transfer branch |

Before this lane, these files supplied the six-chassis armour API and shared modulo-one integer helper.
After this lane they additionally supply separate literal `motorized_equipment` and `artillery_equipment` stock/reserve/need/quote/native-transfer paths.
All seven pre-existing effect/trigger definitions were compared against the captured pre-edit text and are identical.
Only their overview comments changed.
Mobile capacity initializes stock, target, fielded and reserve-floor temps in its outer trigger frame before either conditional branch, then overwrites matching measurements rather than adding one subtype to another.
Host need uses `max(reinforcement_shortfall, matching_unlocked_route_floor) - stock`, clamped nonnegative and floored.
Native stock, target and fielded reads are literal in both capacity branches and both host need paths.
No mobile meta block, shared production total, random branch or AI weight was added.

## Exact Boolean caller contract

Initialize these two temporary inputs in the enclosing caller block, then invoke the helper with `= yes`:

```text
set_temp_variable = { gods_of_africa_mobile_type = gods_of_africa_payment_mobile_type }
set_temp_variable = { gods_of_africa_mobile_required_amount = gods_of_africa_payment_amount }
gods_of_africa_mobile_capacity_is_sufficient = yes
```

Boolean callers need no measurement output initialization.
For a standalone type validator, initialize only temporary `gods_of_africa_mobile_type` before `gods_of_africa_mobile_type_is_valid = yes`.
Full, partial and substitute wrappers must copy their own frozen subtype and corresponding requirement into these two temporary inputs rather than passing named argument blocks.
The trigger accepts integral zero for measurement and requires nonnegative integral input.
Parent payment callbacks still enforce positive payment, present and matching subtype, integral payment no greater than remaining, and all existing contract/host/generation/deadline/war guards.
The native sender deliberately does not repeat those parent checks or success accounting.

If a caller needs measurement values after the nested capacity call, initialize temporary `gods_of_africa_mobile_stock`, `_target`, `_fielded`, `_deficit`, `_reserve`, and `_spare` to the existing zero constant before that call.
The quote helper already owns those six temps before either nested measurement and owns `gods_of_africa_equipment_amount` before nested integer flooring.
The host need helper also owns its integer amount temp before flooring.
Measurement outputs are not guaranteed on rejected input.
The capacity helper's reserve-floor, fractional-spare and requirement-remainder temps are private scratch and do not need caller initialization.
Its subtype comparison uses `gods_of_africa_mobile_truck_capacity_tt` or `gods_of_africa_mobile_artillery_capacity_tt`, confirmed in parent-owned `localisation\english\012_africa_gods_l_english.yml:424-425`.
The quote helper overwrites mobile scratch inputs, so later payment gates must bind them again from frozen normal contract/payment fields.
Temporary variables are unscoped and must never be read through ROOT/PREV prefixes.

## Constants, event targets, cleanup and migration

No constant was added or edited by this subagent.
Required parent categories and accepted values are:

| Category | Keys/values |
| --- | --- |
| `gods_of_africa_mobile_type` | trucks 1, artillery 2 |
| `gods_of_africa_mobile` | units_per_thousand 1000, operating_reserve_fraction 0.10, truck_reserve_floor 100, artillery_reserve_floor 25, truck_route_stock_floor 100, artillery_route_stock_floor 25, minimum_shipment 1, spare_quote_fraction 0.10, maximum_spare_fraction 0.25, maximum_truck_shipment 500, maximum_artillery_shipment 300 |
| Existing `gods_of_africa_value` | zero and one |

A final read-only snapshot found both parent mobile constant categories present at lines 514-531 of `common\script_constants\012_africa_gods_constants.txt`, matching the delegated numeric values.
The source model used these supplied values and did not claim acceptance of the parent's entire constants file.
During the final read-only snapshot, parent core calls were present at main effects lines 835, 980 and 1819 and main triggers lines 287, 328, 450, 573 and 1006.
Those are concurrent parent edits, not subagent changes or a full integration review.
Follow function identifiers if line numbers move.

Migration belongs to the parent: refresh host needs during existing preparation, replace the flat family-2 quote with the typed quote, freeze selected subtype, bind capacity inputs for full/partial/substitute/transfer gates, replace the truck debit/replacement grant with the native sender, and apply the typed ceiling after existing demand scaling/flooring.
No existing armour behavior changes during this migration.
One-unit payments are supported and a one-unit demand has no legal smaller partial payment.
Parent partials continue using the shared integer helper and exact remaining-balance accounting.

No event target is created or cleared.
`event_target:africa_host` remains Charter-owned and is read explicitly for corresponding host need and native receiver.
The parent clears host need quantities on unifier loss/system cleanup and quote outputs after preparation on all exits and ordinary demand cleanup.
Contract/payment/offer/slot/rollback subtype cleanup and receipt persistence are parent-owned.
Ordinary demand cleanup must not clear the latest-response subtype receipt before its queued report consumes it.
No persistent cleanup logic or new recurring hook was added by this lane.
Parent presentation owns subtype names/capacity tooltip localisation and reuses motorized/artillery icons.
This lane wires those two existing parent-written tooltip keys and adds no localisation definition, sprite, texture or asset manifest.

## Meaningful source acceptance checks

A read-only Python Decimal model parsed the actual five added helper definitions and the preserved integer helper.
It evaluated their ordered conditionals, short-circuit gates, variable reads and arithmetic against an independently computed formula using the delegated constants.
It recorded native branch arguments without simulating stock movement.
The model was passed to Python through stdin and created no additional file.
These results cover source arithmetic and branch selection, not the installed engine's native stock movement or nested temporary lifetime.

All 19 need/quote cases passed:

| Scenario | Quote type/amount/ceiling |
| --- | --- |
| Zero sender stock | no type / 0 / 0 |
| Artillery-only need with truck-only sender | no type / 0 / 0 |
| Artillery sender stock/target/fielded 275/100/50, host 40/200/100 | artillery / 21 / 53 |
| Truck sender 1000/100/100, host 30/200/100 | trucks / 70 / 70 |
| Both host needs and compatible sender stocks | artillery / 21 / 53 |
| Artillery cannot spare one, independent truck need/capacity available | trucks / 70 / 70 |
| Healthy host stock covers both shortfalls | no type / 0 / 0 |
| No army shortfall and routes locked | no type / 0 / 0 |
| Logistics route only, host trucks 30 and no army need | trucks / 70 / 70 |
| Arsenal route only, host artillery 5 and no army need | artillery / 20 / 20 |
| Arsenal unlocked, host target 80, fielded 0, stock 30 | artillery / 50 / 50, proving route max rather than addition |
| Odd quote, artillery sender 135/0/0, host need 40 | artillery / 11 / 27 |
| Fractional reserve, artillery sender 500/257/257, host need 500 | artillery / 47 / 118, spare 474 |
| Exactly one spare gun and one-unit host need | artillery / 1 / 1 |
| Exactly one spare truck and one-unit host need | trucks / 1 / 1 |
| Large artillery spare and need | artillery / 300 / 300 |
| Large truck spare and need | trucks / 500 / 500 |
| Host target 100, fielded 0, fractional stock 0.75 | artillery / 97 / 99, integral host need 99 |
| Fielded sender equipment exceeds army target | artillery / 7 / 18, reinforcement deficit remains zero |

Ten capacity boundary cases passed: zero-requirement measurement for both reserve-floor stocks, exact artillery spare 215 accepted, 216 rejected, fractional 0.5 rejected, negative -1 rejected, type zero/unknown rejected, below-minimum spare rejected, and exactly one spare truck accepted.
Four reset cases passed: absent host, dead host, healthy host, and loss of sender stock after a successful quote all clear previous quote identity and overwrite amount/ceiling to zero.
Four native branch-record cases passed: truck/artillery each emit one matching `send_equipment` with the normal payment amount and explicit `africa_host`, invalid/missing types emit neither branch, and normal payment fields remain unchanged.
The final source pass additionally asserted that all four private branch measurement inputs are declared before the first conditional, failed quotes contain no normal type field, and both custom subtype tooltip branches retain the inclusive capacity test.
Definition preservation was separately checked for all seven pre-existing armour/floor definitions.
The source floor helper is reused at every normal need/quote integer boundary and no unsupported helper parameter API is used.

## MCP and reference evidence

Connected schemas expose reference_context/search/read/source_lookup and event inspection, but do not expose `hoi4.script_validate`.
No native tasks, jobs or helper-expansion route was used or claimed.
Workspace ID returned by successful reference/source calls: `mod_chaos_redux_ea3b2d67c2c0`.

The first context request was rejected because its question exceeded 160 characters.
A corrected bounded request returned the installed Effects and offline Event modding headings with no missing sources, plus `omittedSources` listing Data structures, Effects, Triggers, Scopes, On actions, Localisation, installed triggers documentation and on-action documentation.
The context bundle is not claimed as detailed rule coverage.
Task-bearing Data structures, Effects, Triggers and Scopes sections were read directly at the exact local spans cited below.
On actions and localisation are outside this helper lane and were not implemented here.

Installed-doc-only search and revision-bound `reference_read` returned the native send section:

- ID `a16f0a6f150fc33be67f9532f77a4b83b3cfc654c747eae15b90c59ad8988131`, path `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 6550-6558, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, `nextLine = null`.
- Narrow installed-doc-only army-target search and revision-bound read returned ID `85767e7c956e8f3654eeb2be8db65653dfd4a37e8d0d7f6ce6ebdb8833f75df7`, path `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md`, lines 690-692, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, `nextLine = null`.
- Focused `source_lookup` for `gods_of_africa_floor_equipment_amount`, `includeReferences = false`, returned one unshadowed mod definition at lines 8-12, index revision `5d30364ba4cea0860225be21805f5f6c968c0a81479a65887479b9bbdcc91653`, complete definition read and no artifact URI.

The initial bounded event trace for `chaosx.nr12.603` was rejected because `maxDepth = 0` is below the route's minimum of one.
A corrected `maxDepth = 1`, `maxNodes = 1`, `maxEdges = 1`, `expandHelpers = false` trace was submitted.
The corrected trace returned no result before its orchestration cell was terminated at the bounded delivery boundary.
This is an unresolved delivery and event-coverage blocker, not a confirmed server timeout or a claim about service health.
No event artifact, graph revision or helper coverage was returned by that attempt.
Focused trace would not establish helper/lifecycle coverage even if successful.
No event render/compare claim is made for this helper lane because event sources and owner lifecycle remain parent-owned and a complete post-integration comparison is still required there.

All installed relative paths below are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline paths are mod-relative.

| Local sections actually read | SHA-256 source revision |
| --- | --- |
| Installed `documentation\effects_documentation.md:6550-6557,4986-5011` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md:2110-2134,2145-2152,2708-2715,3844-3851,5166-5174,6442-6452,7482-7500` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\dynamic_variables_documentation.md:557-565,687-691` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Installed `documentation\script_concept_documentation.md:216-243` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md:1-32` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:285-305,435-442,449,557-575` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:339-346,386-403` | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:2254-2255,2285-2293` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:260-270` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Vanilla precedent `events\AAT_Finland.txt:3722-3735` | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |

The offline transfer table labels the argument `type`, while its actual example and installed vanilla use `equipment`.
The implementation follows that exact vanilla example structure.
Existing `chaosx_dynamic_effects` debit helpers were inspected and were not substituted for native transfer because they do not supply the required native debit/delivery identity.

## Source snapshots and remaining limits

| Owned implementation file | Pre-edit SHA-256 | Delivered SHA-256 |
| --- | --- | --- |
| Equipment effects | `2b065d4d9930e83cac1976ccebde8ab2466048d20679b60e147743a2bf9b65f0` | `4d0e522bb32e20c1a0e5708c4b2813c7a7d50b87f86938275a25c9d7add2414c` |
| Equipment triggers | `a999713db442472ce7bff50d858f9318844b8e8d0c8d63a80dc460d2aca397f1` | `d3e14269419ac25901e7001129cee55d408d44eaca6498c72520455fa24fbee6` |
| Matching helper documentation | `db856120456e578c4cdfda43e370c6da7845418e10dfa7a7345b1c978f5f1ca4` | `0f4120c3daa6775833957980f294cfc2a4fadaef6a6c5f9914d455c6ebb1438c` |

Skipped meaningful validation: no engine launch or observed transfer/lifetime/variant-order test was authorized, and `hoi4.script_validate` is absent from the connected tool list.
No probability-bearing helper or AI weight was changed, so no new weighted target or probability audit was introduced by this lane.
Parent final AI eligibility review remains necessary before AI behavior claims.
Unsupported analysis remains exact native variant aggregation/order, engine temporary lifetime and native delivery execution, native supply-network truck shortage, and campaign balance beyond source arithmetic.
The parent must review this handoff, finish/confirm frozen subtype binding and cleanup/receipts/tooltips, retain final owner event/decision evidence, and commit only the completed parent tranche.

## Parent-owned contract documentation follow-up

Disposition: **implemented documentation for parent-owned source**, authorized by the parent's explicit follow-up to document binding and quote cleanup in the matching equipment helper markdown.
Only the matching helper documentation and this handoff were changed in this follow-up.
`common\scripted_effects\012_africa_gods_mobile_contract_effects.txt` was read without modification, SHA-256 `249bae4063918989934b30eda61ad06c50cc5659b38ba3c1d24b29fccbd00bd2`.
Its `gods_of_africa_bind_payment_mobile_type` clears payment subtype and copies the frozen demand subtype only when both normal family fields are family 2 and the normal demand subtype exists.
Its `gods_of_africa_clear_mobile_quote` clears only the three normal preparation quote outputs.
Documentation records COUNTRY scope, normal inputs and output lifetimes, absence/default behavior, no charging or receipt/authority changes, caller obligations, cleanup ownership and `= yes` examples.
The accepted numeric sanity results are included: artillery reserve 60/spare 215/need 60/quote 21/ceiling 53, trucks reserve 100/spare 900/need 70/quote 70/ceiling 70, and odd artillery quote 11/ceiling 27 with accepted half-payment arithmetic 5 paid and 6 remaining.
Those are source-model and arithmetic results, with no invented live delivery evidence.
The shared `chaosx_dynamic_effects.md` owner index was not touched.
No extra UI action, AI weight, source implementation change or Git operation was added.
Meaningful verification was direct comparison of the two documented contracts with their parent-owned source and read-only confirmation of existing parent invocation sites.
The earlier engine and event-coverage limits remain unchanged.
