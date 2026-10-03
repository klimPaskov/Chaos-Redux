# Event 012 armoured tribute architecture audit — 2026-10-03

## Result and ownership

Disposition: source audit completed; required MCP evidence remains unresolved.
No outstanding source-level must-fix finding remains in the final re-read described below.
Two must-fix findings were identified during the audit and corrected by the parent concurrently; both corrections were re-read rather than assuming the earlier snapshot remained current.
This is a narrow architecture assessment, not final Event 012 completion or observed engine validation.
The only file written by this auditor is this handoff.
Gameplay, localisation, parent documentation, and Git were not modified.
Skills read and applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`; no skills were created or updated.
The task instruction supplies the acceptance basis for the parent design and the full spec's armour passage at `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md:442-446`.

## Findings resolved by the parent

1. **Undocumented floor commands — resolved in source.**
The first snapshot used `floor_temp_variable` at equipment triggers line 21 and `floor_variable` at equipment effects lines 17/24 and main effects line 1281.
Neither command was present in the installed effect/trigger documentation or defined as a mod/vanilla scripted helper in the searched helper directories.
Installed documentation instead defines rounding and modulo, and the offline Data structures table defines modulo as a remainder.
The final source uses documented modulo subtraction: equipment triggers `:21-23` subtract the fractional spare remainder, equipment effects `:6-10` define `gods_of_africa_floor_equipment_amount`, and quote/final demand call sites use that helper.
The helper is safe for this nonnegative amount domain and does not rely on tie-breaking or an undocumented floor command.

2. **Fractional partial tank payments — resolved in source.**
The first snapshot divided an integral contract by two without integer normalization, giving 2.5 for a 5-tank contract.
That value was passed to native shipment and subtracted from the remaining balance, so the source did not establish equality between whole equipment delivered and tribute credited.
The exact native treatment of fractional amounts was not asserted or observed.
Final main effects `:1642-1653` normalize armour partial amounts with the modulo helper before building their capacity requirement.
A 5-tank demand consequently quotes a 2-tank partial and leaves 3 due; an 11-tank demand quotes 5 and leaves 6 due.
The existing partial resolver uses the same payment amount for transfer and balance reduction at `:1886` onward.

## Helper map and lifetime review

| Helper | Scope and required input | Output and side effects | Direct consumers |
| --- | --- | --- | --- |
| `gods_of_africa_measure_armor_archetype` | COUNTRY; literal `EQUIPMENT` chassis | Temporary per-type stock, target, fielded, deficit, reserve, integer spare; adds to existing aggregate temps; returns true; no economic mutation | Capacity trigger and per-chassis sender |
| `gods_of_africa_armor_capacity_is_sufficient` | COUNTRY; `AMOUNT`, no default | Resets and measures three aggregate temps; inclusive spare comparison with capacity tooltip | Host need, family selection, quote, full/partial/substitute affordability |
| `gods_of_africa_floor_equipment_amount` | COUNTRY variable owner; literal normal variable name `AMOUNT` | Replaces that normal amount with its nonnegative integer part; private temporary remainder | Quote, ceiling, final demand, armour partial amount |
| `gods_of_africa_quote_armored_tribute` | Participant COUNTRY; current stock/army/production inputs | Normal amount and ceiling initialized to zero and then quoted; aggregate temps; no payment | Main family selection |
| `gods_of_africa_send_armored_archetype` | Sender COUNTRY; literal `EQUIPMENT`; caller-owned remaining/type/slice temps; authoritative host target | Native equipment transfer; reduces temporary remaining by the slice | Six calls in tribute sender |
| `gods_of_africa_send_armored_tribute` | Sender COUNTRY; positive normal payment amount and valid host supplied by transaction preflight | Initializes shipment/type/slice temps; sends at most six integer slices | Armour branch of `gods_of_africa_transfer_payment` |

The quote initializes aggregate temps before calling the capacity trigger (`equipment_effects:15-19`), so the trigger's aggregate modifications have existing caller storage to update.
Host need does the same in main effects `:846-850`.
The capacity trigger initializes its accumulators before all six measure calls (`equipment_triggers:33-41`), and each measurement updates those existing accumulators.
Per-type scratch variables created inside measurement do not have to survive for capacity's final aggregate comparison.
The tribute sender explicitly initializes remaining, all six type outputs, and slice before its nested send/measure calls (`equipment_effects:57-70`).
This supplies the pre-existing storage needed for `gods_of_africa_armor_type_spare` to survive the trigger-to-effect boundary in each send slice.
Fractional-remainder scratch variables are consumed inside the helper that creates them and need no external lifetime.
No temporary value is referenced through ROOT, PREV, or another scoped namespace in the new helpers.
The sender's remaining temp is not a public receipt for its caller unless that caller preinitializes it; the present transaction does not attempt to read it afterward.

## Formula, constants, and integration

For each of six installed chassis, reserve is `max(25, 0.10 * army_target + max(0, army_target - fielded))`, and spare is the nonnegative integer part of stock minus reserve.
Army target and fielded reads use their `_k` forms and multiply by the centralized units-per-thousand constant.
Aggregate spare must be at least 5 before quoting.
The base amount is the integer part of `clamp(0.10 * spare + 0.01 * cumulative_actual_armor_production, 5, ceiling)`.
The integer ceiling is `min(300, max(5, 0.25 * spare))`.
Existing main-demand scaling starts from the armour quote (`main effects:1160-1165`) and applies its final armour ceiling and integer normalization at `:1275-1281` in the recorded audit snapshot.
The main capacity special case uses payment amount directly for armour (`:755-760`), because per-chassis reserves have already been excluded from spare; it does not add the old generic truck/equipment floor again.
The `gods_of_africa_armor` constants category at `common\script_constants\012_africa_gods_constants.txt:113-127` centralizes conversion, reserves, quote fractions, shipment bounds, and the Evolution II host stock floor.
No new tuning table or migration is recommended beyond the implemented narrow family-specific helpers.
The old combined mobile-artillery/armour branch has been split: armour calls native chassis transfers rather than removing motorized equipment and manufacturing a replacement credit.
The new armour branch is exclusive within the transaction's `else_if` ladder.
There is no additional armour `add_equipment_to_stockpile` credit in that branch.

Full, partial, and substitute affordability use the same live armour capacity trigger in main triggers `:325`, `:957`, and `:429` respectively.
The actual debit path rechecks current contract, positive amount, live capacity, and host existence at main effects `:1702` onward, so a stale UI quote cannot alone authorize a shipment.
Full compliance closes the demand after success; repeat invocation then fails the active-contract guard.
Partial compliance requires the frozen partial amount to be strictly less than the current remaining balance and uses its existing cooldown, preventing a repeated half-payment from overdrawing the residual balance.
Substitute acceptance passes through full compliance and restores the original family/balance if transfer fails; see main effects `:1932` onward.
The currently constructed substitute set offers infantry, fuel, manpower, or support equipment; its generic armour affordability branch is guarded correctly but no new armour substitute slot is created by this patch.

`event_target:africa_host` remains the authoritative receiver, independent of ROOT or nested PREV.
The existing current-contract chain checks the participant generation, demand generation, host validity, and war status, and the host validity helper explicitly checks `exists = yes`.
No new global event target is created, so no armour-specific global-target cleanup is needed.
Quote variables are cleared in preparation `:1618-1619` and demand cleanup `:2083-2084`; the host armour-needed flag is refreshed by need calculation and cleared on unifier loss `:3087`.
The final re-read also confirms armour in the need/scale OR gates, the expanded visible capacity text, and the parent-written matching helper documentation.
Those known concurrent edits are not reported as omissions.

The six chassis are installed archetypes: light, medium, heavy, modern, super-heavy, and amphibious.
Installed `tank_chassis.txt` defines them without a No Step Back availability gate; its visible AAT conditional in the first chassis block selects Bulgarian restriction checks rather than excluding the chassis.
The legacy light-tank archetype block in installed `tank_light.txt:5-55` is commented out.
No new DLC check, designer variant assumption, technology grant, or replacement equipment is introduced by the helpers.
This establishes installed-source compatibility, not observed execution with every DLC combination.

## Meaningful boundary scenarios

These are a small arithmetic model of the inspected formulas, not executed HOI4 script or stock observations.
Seven cases checked quote bounds and exact sum of modeled per-chassis slices.

| Scenario | Input stock / target / fielded; cumulative production | Spare; ceiling; base quote | Result |
| --- | --- | --- | --- |
| Below minimum | 29 / 0 / 0; 0 | 4; 0; 0 | No tank quote |
| Exact minimum | 30 / 0 / 0; 0 | 5; 5; 5 | Valid minimum shipment, reserve remains 25 |
| Mixed chassis | Light 28 / 0 / 0, medium 40 / 0 / 0; 0 | 3 + 15; 5; 5 | Slices 3 light + 2 medium, no duplicate credit |
| Reinforcement need | 200 / 100 / 50; 1000 | 140; 35; 24 | Reserve 60 includes 50 shortfall plus 10 operating |
| Fractional operating reserve | 500 / 257 / 257; 0 | 474; 118; 47 | Reserve 25.7 causes conservative integer spare/ceiling |
| Production without spare | 25 / 0 / 0; 100000 | 0; 0; 0 | Historical production cannot manufacture current capacity |
| Maximum ceiling | 5025 / 0 / 0; 100000 | 5000; 300; 300 | Quote never exceeds 300 |

Additional source-path checks covered odd partials 5, 11, and 47; exact-capacity inclusive comparisons; stock lost after quote but before payment; repeated full resolution; repeated partial after cooldown; substitute stock lost before acceptance; and stale/dead/replaced host generation.
Their control-flow conclusions are source-derived only.
No probability adapter or probability auditor was required for the deterministic arithmetic and fixed six-type transfer sequence in this bounded audit.
Existing AI weights, event option probabilities, focus selection, and random non-armour branches were not audited or changed.

## Reference evidence and MCP coverage

Connected metadata exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and event inspect/render/compare.
`hoi4.script_validate` and a HOI4 health/version route were not exposed in the discovered tool list.
No helper-expansion or native task route was used because the required health/version/client negotiation could not be verified.

The live event context request, installed-doc-only `send_equipment` search with limit 1, and source lookup for `gods_of_africa_send_armored_tribute` returned no result in this audit's bounded wait window.
A narrower installed-doc-only `num_equipment` search with limit 1 and an exact `floor_variable` search with limit 1 also returned no result before cancellation.
An initial event selector omitted `kind` and used the padded namespace; it supplies no evidence.
Corrected requests used `selector: { kind: "event", eventId: "chaosx.nr12.603" }` with a four-node, depth-one trace and options render, but neither returned a result in the bounded wait window.
All pending orchestration cells were terminated at the audit boundary rather than spending the entire review waiting on transport.
This is an unresolved response/transport gap, not a confirmed server-health diagnosis or a reported 600-second server timeout.
No artifact URI, source revision, graph coverage, or render diagnostic was returned by those calls.
Revision-bound `reference_read` could not be populated from a returned reference ID, so the relevant exact local sections were read directly instead.
Event comparison was skipped because no valid baseline graph/artifact was returned; comparing current source to itself would not establish change evidence.
The focused trace, even if returned, would not establish helper lifecycle coverage.
The parent must retain or obtain its owning MCP evidence separately; this report does not substitute source inspection for that requirement.

Local references read, with file SHA-256 revisions:

| Reference | Relevant lines | Revision |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md` | 6550-6557 native send; 4986-5011 modulo; 6476-6493 round; 6496-6511 event targets; 7820-7839 temp arithmetic | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | 6442-6452 modulo; 7440-7448 round; 7482-7500 temp arithmetic; 3844-3850 event target predicate | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\dynamic_variables_documentation.md` | 557-565 stock/fielded; 687-691 army targets; 870-871 actual armour production | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Installed `documentation\script_concept_documentation.md` | 216-244 script constants | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1-32 schema and fixed-point access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-305 event targets; 435-442 temp lifetime; 570-574 arithmetic | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 2254 transfer removes stock; 2285-2293 example uses `equipment` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Vanilla `events\AAT_Finland.txt` | 3722-3735 direct native equipment transfers | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |
| Vanilla `common\units\equipment\tank_chassis.txt` | Archetypes and first production gate at 7-30; remaining chassis definition blocks | `5f77546f91c66d99df005314c3c4e2a2f7474753e4a01f6ad9253835dafca4f8` |

Installed paths above are rooted at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
The wiki revision supplied in the prompt for dynamic docs agrees with the local hash; the current local Data structures hash is recorded independently rather than attributing another file's revision to it.
Existing mod `common\scripted_effects\077_send_eq_effects.txt:50-80` provides chassis transfer precedent; its duplicated heavy-tank call was not copied and is outside this audit's edit scope.
Existing `chaosx_dynamic_effects.txt` and matching markdown were searched/read for stockpile helpers and integer patterns; the present armour helper remains feature-local and does not require a central router or wrapper.

## Final source identities and remaining limits

The complete source review and resolved-finding re-read used these SHA-256 identities:

| File | SHA-256 |
| --- | --- |
| `common\scripted_triggers\012_africa_gods_equipment_triggers.txt` | `8113c7f41e3fe55be1bf191de7108fa6698cb7cecee8bd737f4d5691f85eb3ae` |
| `common\scripted_effects\012_africa_gods_equipment_effects.txt` | `61c7189bdee1ec84f5c5315b4d5d18f0f97c978cd6f53387d3016e1c1b06b1ba` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `6c80dce3c2a9d896ff866b2c1c8d95e714b67e04b58d2169fe2fb627fba30589` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `1e4e99a517bef1dd546ae0223142010b9e54e942972642073c6024a28d3e8297` |
| `common\script_constants\012_africa_gods_constants.txt` | `dea075a53455cbcb894e33a8e5e8bf15dd1a5c2969edcec63ea70a96d18dbeea` |
| Parent helper docs `common\scripted_effects\012_africa_gods_equipment_effects.md` | `940eb5fb762aae52125427bcec56bcfeda2010070a47040f1fb9647c7a9378b2` |

At the final existence/hash check, the parent-owned main effects file had advanced to `949dd25f64e48de3ad5a602147dbff3d59f3ea445c40704e544afea95b82b6aa`, while the two equipment helper source hashes remained unchanged.
The final amount-base block was checked again and still takes the armour quote at current line 1164.
The whole newer main-effects revision was not independently re-audited; line references outside that final check belong to the recorded `6c80dce3...` snapshot and may shift during concurrent parent work.
This boundary is explicit rather than treating a moving shared workspace as a frozen final implementation.

The installed stock dynamic variable description says “number of equipment in country” and does not itself fully specify variant aggregation or stockpile/accounting edge cases.
The native transfer evidence and existing chassis precedent support the parent implementation, but actual stock deltas, variant choice, every DLC execution mode, and helper temp persistence are not observed engine results in this audit.
The transaction marks success after its source-preflight and native calls without an independently observed delivery receipt; source arithmetic establishes requested slice totals, not runtime transfer success.
GUI layout, focuses, maps, whole-event AI/balance, spreadsheets, and overall completion were outside this narrow review.
No gameplay simplification or replacement was introduced by this auditor.
Required MCP evidence is the remaining coverage blocker; final wiring and broader completion remain with the parent.
