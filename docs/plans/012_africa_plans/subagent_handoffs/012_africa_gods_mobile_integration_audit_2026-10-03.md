# Event 012 mobile/artillery integration audit, 2026-10-03

## Concrete outstanding findings

**M1: the accepted mobile need integration is missing from the demand-scaling gate.**
`common\scripted_effects\012_africa_gods_effects.txt:1252–1271` applies the existing `gods_of_africa_demand_scale.need_delta` when another maintained need is positive, but its OR has neither `gods_of_africa_truck_need_amount` nor `gods_of_africa_artillery_need_amount`.
The accepted design handoff explicitly requires both preparation and demand-scale need OR coverage at `012_africa_gods_mobile_artillery_design_2026-10-03.md:161–164`.
Preparation has the new conditions at effects `1671–1672`, while scaling does not.
With a compatible mobile shipment as the only real need, selection works but that existing need delta is omitted.
If an unrelated maintained need is also positive, the delta is applied.
This is a concrete accepted-design integration gap, not authority for the auditor to choose a replacement scale or balance target.
The typed ceiling still bounds the shipment, so this finding does not establish an overdraw or subtype conversion.

**M2: declared mobile cleanup is incomplete and its helper documentation overstates coverage.**
The complete host-loss body at effects `3302–3339` does not clear the two new host need quantities or `gods_of_africa_selected_mobile_type`.
The complete system-cleanup body at `3458–3484` clears selected subtype at `3479` but leaves both new host need quantities.
The accepted design at `215–220` requires host need and selected-type cleanup on both exits.
`common\scripted_effects\012_africa_gods_equipment_effects.md:236` describes host-need cleanup as already provided, which disagrees with the source.

`gods_of_africa_clear_demand`, effects `2233–2284`, also does not clear the three mobile quote outputs or call `gods_of_africa_clear_mobile_quote`.
That omission disagrees with the accepted quote/cleanup contract at design `72,147,215–219` and helper documentation `236,264–269`.
Register, archive, clean-participant, finalize-participant, and cancel-participant do call the quote cleaner, and normal preparation explicitly discards its quote before returning.
Thus the ordinary prepared-demand trace normally has no surviving quote to consume, and no unauthorized live transfer from this omission is proved.
It remains missing required cleanup for a retained preparation quote, including an authorized future typed offer producer, and stale dormant host state after loss/system closure.
Existing active-host guards close live transfer after loss, so this finding does not assert that stale need values confer authority by themselves.

Parent follow-up is to complete these exact accepted scaling/cleanup requirements and reconcile the documentary claims against the final source.
No gameplay correction, documentation correction outside this handoff, or balance target was applied by this auditor.

## Scope, disposition, and status

This is a separate bounded read-only mobile/artillery integration review.
The lifecycle tranche `61cca7` is the comparison baseline and L1–L3 were not re-audited.
Acceptance comes from the explicit parent assignment and its accepted `012_africa_gods_mobile_artillery_design_2026-10-03.md`, including the instruction to choose the recommended bounded implementation and introduce no simplifications.
The full spec's compatible equipment, protected reserves, and corresponding host deficit/route reason were read at `012_gods_of_africa_full_spec.md:424–438`.
The helper and text worker handoffs were read, along with the parent integration handoff `012_africa_gods_mobile_tribute_2026-10-03.md` and current helper/report documentation.
The assignment's caller-temp and `= yes` API supersedes parameter-shaped examples in the older design.

| Surface | Status | Evidence or limit |
| --- | --- | --- |
| Two literal equipment measures, reserve, need, base quote, ceiling | Confirmed in source and independent arithmetic | Helpers and accepted constants match the prescribed formulas |
| Deterministic subtype selection and ordinary ladder | Confirmed in source | Artillery first, truck fallback requires its own need, family 2 after armour and before manpower |
| Existing scaled demand integration | Partial | M1, with typed cap and integer flooring present |
| Immutable contract, full/partial debit, matching native transfer | Confirmed in source | Normal type binding, presence/value checks, live capacity, positive integral amount and residual bound |
| Typed future substitute wrappers, submission, preflight, rollback | Confirmed in source | No new family-2 slot producer, untyped or opposite subtype fails closed |
| Rejection and return to ordinary payment fields | Confirmed in source | Restores original family, subtype, balance-derived work amount, and capacity requirement |
| Response subtype lifetime and concrete names/icons | Confirmed in final source | Parent's artillery icon correction verified separately from worker's original output |
| Host/ordinary-demand cleanup | Partial | M2 |
| Meaningful native/MCP/AI eligibility evidence | Unconfirmed | Pending receipts and separately owned probability pass |

Disposition of the accepted mobile design: substantially implemented in source, with M1–M2 outstanding and required native/MCP acceptance unconfirmed.
The parent integration handoff's implemented status is not evidence that those missing requirements have been completed.
The text and helper workers supplied handoffs, and their ownership boundaries match the assignment.
No additional design expansion is recommended for these two bounded omissions.
No accepted requirement was rejected, promoted, silently queued, or replaced by a fallback here.
Only this new audit handoff was written, with no gameplay, other docs, skills, assets, workbook, Git index, commit, or HOI4 launch.

## Manual source paths and requested scenarios

The mobile helper effects at `common\scripted_effects\012_africa_gods_equipment_effects.txt:93–195` reset both host needs, measure each literal archetype separately, apply a matching unlocked route floor through a maximum, and require positive matching sender spare and host need.
Capacity at `common\scripted_triggers\012_africa_gods_equipment_triggers.txt:79–142` initializes its branch measurements in the outer trigger frame and uses subtype-specific reserve tooltips.
The quote owns every measurement output it reads after the nested trigger and its shared integer-floor output before calling that helper.

| Requested scenario | Manual result |
| --- | --- |
| Zero sender spare | No successful subtype quote, amount/ceiling zero, no native payment capacity |
| Healthy host | Each matching need is zero when stock covers reinforcement shortfall and any unlocked route objective. With every other maintained need and route demand gate false, preparation creates no arbitrary demand |
| Artillery need and truck-only sender | Artillery attempt fails matching capacity. With truck need zero, the truck branch cannot quote, regardless of truck stock |
| Artillery sender 275 stock, target 100, fielded 50 | Reserve 60, spare 215. Host target 200, fielded 100, stock 40 gives need 60, base quote 21 and ceiling 53 |
| Truck sender 1000 stock, target/fielded 100 | Reserve 100, spare 900. Host need 70 gives base quote and ceiling 70 |
| Both matching needs and capacity | Artillery succeeds first and suppresses truck fallback, producing one type |
| Odd 11-unit artillery contract | Shared half ratio and floor give partial 5. Successful resolution subtracts 5 once, leaves 6, captures amount 5/balance 6/type artillery, and restores ordinary payment work for the residual |
| One-unit residual | Precomputed minimum partial is one, while the strict smaller-than-residual gate rejects it |
| Stock lost before host acceptance | The refreshed offer-capacity preflight rejects before the temporary contract swap, leaving original family/type/balance unchanged and writing no success/history/response credit |
| Failure after temporary swap | The demand-active rollback branch restores original family, optional type presence, remaining balance, and ordinary payment amount/type/requirement. It clears the acceptance flag and backups |
| Untyped/zero/unknown normal family-2 type | Demand/payment validators and full/partial/substitute wrappers reject missing or invalid type. No default truck value or inference from current inventory occurs |
| Typed truck offer against artillery demand, or reverse | Affordability compatibility requires matching types when both original and offered families are 2, so it rejects the cross-type offer |
| Return or rejection | Canonical and slot offer state is cleared, then ordinary family/type/remaining-derived amount/requirement are restored |
| Response survives demand cleanup | Receipt reads frozen demand type before cleanup. Ordinary demand cleanup leaves the response subtype, later non-family-2 capture clears it, and archive uses the shared receipt reset |
| Existing family validators | Current family-ID sets match `61cca7`: six equipment classifier entries and 14 demand/payment validator families. Only family 2 gains its required type checks |

An independent Decimal calculation using the current constant values checked the artillery, truck, zero-spare, healthy-host, odd-quote, and one-unit cases.
That arithmetic check computes the accepted formula, rather than executing Clausewitz or the native transfer.
The helper worker's source model reports additional cases, but those are attributed worker evidence and not a claim that this auditor executed them again.
The base quote examples above do not assert that every existing doctrine/conduct/Strength/Chaos scaling scenario produces the same final contract amount.
Current scaled amount is clamped and floored against the typed ceiling at core effects `1331–1340`.
The existing affordability fallback returns to the already integral, bounded base quote at `1438–1442`, so no oversize fallback was found in the ordinary quote path.

## Binding, substitution, and receipt evidence

Selection copies the quote type into normal participant payment work and then host selected type at core effects `1142–1169`.
Contract creation at `1734–1805` rechecks live eligibility, matching selected family/amount/type and protected capacity, and freezes the normal demand type.
`common\scripted_effects\012_africa_gods_mobile_contract_effects.txt:13–23` binds payment type from the normal demand only when both work and demand family are 2.
Its callers set family and amount separately, use `= yes`, and do not supply named parameters or dollar macros.

The shared transfer at core effects `1834–1847` requires current contract, present family/amount, positive amount, payment-family validity, the mobile contract match, and matching capacity.
Core triggers `592–606` enforce payment/demand type equality, integral payment, and payment no greater than remaining.
The native mobile sender at equipment effects `199–216` has mutually exclusive static `motorized_equipment` and `artillery_equipment` branches addressed to explicit `event_target:africa_host`.
It does not remove stock through a helper and synthesize replacement receiver equipment, pool archetypes, credit the infantry ledger, or choose another stock type at payment.
Native completion and exact variant aggregation/order remain unobserved.

Full, partial, and substitute wrappers materialize their own normal type and amount into temporary inputs before capacity.
Family 2 is exempted from the generic extra equipment-floor requirement because its typed reserve measurement already deducts the protected reserve.
The partial resolver at core effects `2017–2052` binds frozen demand type, debits through the shared transfer, and changes balance/receipt/history only after success.

Current substitute producers remain infantry/fuel/manpower/support paths at core effects `1495–1558`.
Freeze at `1565–1644` and all three wrappers at `3636–3692` carry each slot's own optional type, clearing canonical type first.
Submission rechecks typed affordability before marking the offer at `2054–2072`.
Acceptance recalculates the offer requirement and capacity before the temporary swap at `2074–2083`.
Original type presence and remaining balance are backed up at `2089–2095`, restored on failed resolution at `2105–2120`, and backups discarded at `2126–2128`.
Rejection at `2158–2187` and return at `3694–3713` restore the ordinary demand-derived payment fields.

`common\scripted_effects\012_africa_gods_report_effects.txt:5–21` clears the previous optional response subtype within its existing family-present guard and snapshots demand type before live cleanup.
No-family capture leaves the previous complete receipt intact.
The shared reset at `23–31` clears response subtype alongside the other receipt fields.
The response resolver at `common\scripted_localisation\012_africa_gods_scripted_localisation.txt:110–115` uses response family/type only, with a family-2 unavailable fallback.
The remaining ten targeted name/icon resolvers branch on their own demand, work, offer, or slot type fields.

## Localisation, assets, and documentation

The final YML at `localisation\english\012_africa_gods_l_english.yml:422` contains U+00A3 followed by `artillery_texticon`, and direct byte inspection confirmed UTF-8 bytes `c2a3` for that character.
The parent corrected the text worker's original literal `?artillery_texticon`.
This audit accepts the corrected current leaf and does not claim the worker's original icon literal passed native-token validation.
The truck leaf reuses its existing motorized texticon, and capacity keys at `424–425` are wired by the final matching trigger branches.
No new image, DDS, portrait, model, animation, GUI, currency, or player action is part of this lane.
The existing installed artillery sprite was inspected at `interface\texticons.gfx:2131–2135`.

The current Gods guide at `docs\events\012_africa\gods_of_africa.md:118–127` describes the typed selection, native transfer, reserves, ceiling, and response lifetime.
Report-helper documentation at `012_africa_gods_report_effects.md:7–17` matches the optional subtype receipt contract.
Helper cleanup statements at `012_africa_gods_equipment_effects.md:236,269` require reconciliation under M2.
Broader Event 012 docs, catalog, lifecycle, focus trees, country packages, achievements, and asset completion were not re-audited.

## Required evidence still unconfirmed

The parent owns its pending `.606` reference/inspect/render receipts and collection/retry workflow.
This audit also dispatched narrow read-only `.603` trace, options render, and event comparison requests, plus event reference context limit 2 and installed-only `send_equipment` search limit 1.
Trace/render bounds were depth 1 and one node, with one trace edge, no helper expansion, and no HTML.
Comparison selected the same event with one chain/render node and rendering disabled, without asserting an invented cached baseline.
No final result, source revision, artifact URI, valid before/after comparison, or helper/lifecycle coverage from those requests was observed before this prompt-delivery handoff.
Pending or unobserved receipts are not proof that a route is absent or the server failed.
Source review is not substituted for required MCP event evidence, and a successful focused trace would still not establish full scripted-helper lifecycle coverage.
No helper expansion, native task, job inspection/cancellation, or health/version claim was used without negotiation.

No AI weight or random choice was changed or audited in this deterministic lane review.
Changed eligibility still belongs in the parent's separately routed `chaosx_ai_probability_auditor` scenarios before AI behavior or full Gods completion claims.
No probability target was selected by this auditor.
Native inventory execution, nested temporary lifetime, variant aggregation/choice, live tooltip/render presentation, and campaign balance remain unconfirmed.
This report does not authorize or request an engine launch and makes no full-goal completion claim.

## Exact references read

Installed relative paths below are rooted at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline paths are mod-relative, and SHA-256 is the local file revision actually read.

| Reference | Read span | SHA-256 |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md` | 6550–6558 native equipment transfer | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\dynamic_variables_documentation.md` | 557–565 stock/fielded measures, 687–691 target measures and thousand-unit conversion | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Installed `events\AAT_Finland.txt` | 3722–3735 literal archetype/amount/target precedent including artillery | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |
| Installed `interface\texticons.gfx` | 2131–2135 artillery texticon definition | `e0349b22f05affe550e755fc2e1f3a2ad3749fb016b5c9031b3672d9656304b5` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 435–442 caller-owned temporary lifetime and unscoped temps | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 2285–2293 native transfer example | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |

## Source snapshot and next action

| Reviewed mod-relative source | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `68abe0c32f03b239dc6fa5f4a2cdb4f7ffc86eb6fc30bc13a6ed042fd071b6e3` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `7250742b4bc2392203a24f819b16f2646fd7d086766d4e15ff9cbab5b074af26` |
| `common\script_constants\012_africa_gods_constants.txt` | `53e01ee0705a641ed2d66410ae7fe42a9f1c1a5d70dc85df6fb14193f687fe11` |
| `common\scripted_effects\012_africa_gods_mobile_contract_effects.txt` | `249bae4063918989934b30eda61ad06c50cc5659b38ba3c1d24b29fccbd00bd2` |
| `common\scripted_effects\012_africa_gods_equipment_effects.txt` | `4d0e522bb32e20c1a0e5708c4b2813c7a7d50b87f86938275a25c9d7add2414c` |
| `common\scripted_triggers\012_africa_gods_equipment_triggers.txt` | `d3e14269419ac25901e7001129cee55d408d44eaca6498c72520455fa24fbee6` |
| `common\scripted_effects\012_africa_gods_equipment_effects.md` | `0f4120c3daa6775833957980f294cfc2a4fadaef6a6c5f9914d455c6ebb1438c` |
| `common\scripted_effects\012_africa_gods_report_effects.txt` | `fbbef7c6f960626f8ea9a92358a92863b1648d63ce54fb0e7c6403f1f6957dc9` |
| `common\scripted_effects\012_africa_gods_report_effects.md` | `dc1d15dc4b36520e8dbdb7d377106be50a855aa0527d7c5babfb2946d6e4ead4` |
| `common\scripted_localisation\012_africa_gods_scripted_localisation.txt` | `4dc1a974842bb76e58bb3fe830ae11ad1459816c4d2486922a3bfef61ddfcdd9` |
| `localisation\english\012_africa_gods_l_english.yml` | `8f65adf9e0b412b34dd938a734a43a39facc50ac8891aee2e993e9f2ecd9d6f2` |
| `docs\events\012_africa\gods_of_africa.md` | `f77eabfc0b8ae1995b627314a56d4017bde43da1ec650b4da355138765c78241` |

The parent should resolve M1–M2 within the existing accepted design, then recheck those exact affected source blocks and retain the corrected icon evidence before its own tranche decision.
Pending MCP receipts and required narrower retries stay with the parent and do not hold this manual findings delivery open.
No simplification was made by the audit, and the two missing accepted requirements are reported explicitly rather than presented as complete.

Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-decisions-missions`, and the authorization-bounded native-icon guidance in `chaos-redux-event-assets`.
No skill was created or updated.

## Narrow resolution review after parent fixes, 2026-10-03

**M1 and M2 are resolved in the current source.**
This appended disposition supersedes their outstanding status, the two partial source-status rows, and the corresponding next-action wording above.
The earlier findings and hashes remain the record of the original reviewed snapshot.
This follow-up reread only the named scaling/cleanup changes and the subtype tooltip wrapper, without repeating the integration audit or L1–L3.

| Finding or change | Current source evidence | Resolution |
| --- | --- | --- |
| M1 mobile need scaling | `common\scripted_effects\012_africa_gods_effects.txt:1252–1272` now includes positive truck need at 1258 and artillery need at 1259 in the existing need-delta OR | A mobile-only need now satisfies the same existing need-delta gate. No replacement scale or balance target was introduced |
| M2 host-loss fields | `gods_of_africa_cancel_on_unifier_loss:3303–3343` clears selected mobile subtype at 3320 and both host need quantities at 3321–3322 after its array cleanup | The exact three declared fields are removed from cancelled host state |
| M2 system cleanup | `gods_of_africa_clean_system:3462–3490` clears both host needs at 3465–3466 and retains selected subtype cleanup at 3485 | Both system-exit requirements are source-present |
| M2 ordinary quote cleanup | `gods_of_africa_clear_demand:2233–2285` invokes `gods_of_africa_clear_mobile_quote = yes` at 2234 | The existing cleaner removes the three preparation quote fields and leaves latest-response subtype untouched |
| Subtype requirement tooltip | `common\scripted_triggers\012_africa_gods_equipment_triggers.txt:79–87` wraps the same trucks/artillery enum OR in `custom_trigger_tooltip`, using `gods_of_africa_mobile_type_invalid_tt` | The existing player-facing key is consumed and the accepted two-value predicate is unchanged |

The helper documentation's host-need and ordinary-quote cleanup statements now agree with these source changes, so the M2 documentation contradiction is resolved by implementation.
The core trigger, constants, binding helper, equipment effects, equipment documentation, report helper/documentation, scripted localisation, corrected YML, and Gods guide hashes were rechecked and still match the original snapshot table.
The corrected artillery literal remains the parent-fixed YML reviewed above, and the original text-worker literal is not retrospectively treated as passing.

| Changed source with current SHA-256 | Revision |
| --- | --- |
| `common\scripted_effects\012_africa_gods_effects.txt` | `7def8a688e56dd54571cbca0356f3d5ad487d9bbf4a95e9f07be465b59bb26f8` |
| `common\scripted_triggers\012_africa_gods_equipment_triggers.txt` | `cd464c44bc7687be7c2decdc131b3819fee539e129e20507d7fb77826187ed7d` |

Final bounded disposition: the reported source integration gaps are resolved, with no remaining source defect identified by this audit and no simplification introduced.
The mobile tranche is source-reviewed for the parent's commit decision.
Required MCP receipts, valid event comparison/helper coverage, native inventory execution, live presentation, and separately owned AI eligibility/probability evidence remain unconfirmed as previously recorded.
This append makes no engine acceptance, campaign balance, full Gods, or Event 012 completion claim.
Only this audit handoff was appended, with no gameplay, other documentation, skill, index, commit, or HOI4 launch by the auditor.
