# Event 026 universal-cost quantization audit

Disposition: audit and accepted positive-minimum invariant repair implemented, unrestricted exact arithmetic repair blocked and queued for parent follow-up.
Acceptance basis: the parent explicitly requested this continuation within the original Part 3 semantics, with exact upward rounding, positive minimum quantum, zero preservation, all-source composition, and displayed trigger quote equal to confirmation payment after ordinary current modifiers.
The parent's reviewed follow-up explicitly authorized one guard after `universal_cost_round_up_to_quantum` and the final-cost assignment, comparing final cost with the actual effective `universal_cost_quantize_quantum` and assigning that quantum when final cost is smaller.
This accepts the positive-minimum invariant repair independently of the still-blocked exact ceiling and composition repair.
This handoff does not establish Event 026 completion, availability, native consumer behavior, or approval of a restricted pricing domain.
No commit was created.

## Result and changed files

The accepted minimum guard establishes the effect-side positive minimum for the registered positive quanta, while the existing scalar composed-ratio cache still cannot establish the full requested contract.
The source also loses a payable remainder before its final quantizer and can overflow before division.
Only the explicitly accepted final-cost minimum guard was applied to gameplay.
No helper scaffolding, source restriction, constant change, ratio epsilon, or approximate-ceiling replacement was applied.

Files changed:

- `common/scripted_effects/chaosx_universal_cost_effects.txt` adds the final-cost minimum guard inside the existing positive-ordinary and eligible-source branch of `universal_cost_quote_integer`.
- `common/scripted_effects/chaosx_universal_cost_effects.md` distinguishes required semantics from the current implementation's arithmetic limits.
- `docs/systems/universal_cost_modifier.md` describes the actual distinct effect and trigger arithmetic and links this audit.
- This handoff preserves reference identities, source identities, counterexamples, and the proposed architecture.

Call sites changed: none.
Helper documentation added or updated: the existing `universal_cost_round_up_to_quantum` validation limits and the accepted `universal_cost_quote_integer` positive minimum.
Constants added or updated: none.
Cleanup logic added: none.
The parent-owned central Event 026 triggers/effects, owner adapters, AI, catalog, and event enablement were not edited.

## Source evidence before documentation edits

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Observed HEAD: `4991fd7de71e40ca78b5ccfe31749dd42e9029d8`.
The authorized framework files and the observed trigger were hashed before editing documentation.
Their relevant pre-edit executable statements are recorded below.
The effect file had no task or unrelated working-tree diff at the observed HEAD before this additive guard, and its prior source content remains recoverable from that immutable commit and the recorded pre-edit hash.
No probability-bearing source was patched and no probability comparison was performed.
These hashes identify this audit's observed versions and must be checked against concurrent parent edits before using the proposed bridge.

| File relative to workspace | SHA-256 before edits |
| --- | --- |
| `common/scripted_effects/chaosx_universal_cost_effects.txt` | `097e7acbe42b6d2ef67f6b3dffd0f7faba6f90e96e5ed4a4d7cb431ecbdfb7ba` |
| `common/scripted_effects/chaosx_universal_cost_effects.md` | `399b4277bc1601dd3ea2957e5dab772331cb0d1b508440ba4d44351255e47fdd` |
| `common/script_constants/chaosx_universal_cost_constants.txt` | `11f9e8a42a65999c21161771aeb640670bce36fed753dc7c16fa5b39f697090b` |
| `common/scripted_triggers/026_black_friday_triggers.txt` | `fbf4289e5fa2dd3e82514279ec92eb7ac0c6aeafb99366145245349522d0335d` |
| `docs/systems/universal_cost_modifier.md` | `2d00f27e458ab0f6e2f642dce3342582a06028be10eff1666f42a96a4dce9313` |
| `docs/specs/026_black_friday_specs/026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md` | `a852ddae45a49c835b98d0a34998e098f816089bf87fdf64cd5c2f53e94eeb58` |

The observed effect quote at lines 555 through 563 multiplies `universal_cost_quote_ordinary_cost` by `universal_cost_quote_composed_ratio`, divides by `constant:universal_cost_framework.basis`, then calls `universal_cost_round_up_to_quantum`.
The observed quantizer at lines 393 through 412 divides amount by quantum, rounds to the nearest integer, adds one when the rounded units are less than the stored raw units, and multiplies units by quantum.
The source composition at lines 520 through 525 multiplies the composed ratio by a source ratio and divides by the basis after every source.
The observed trigger at lines 256 through 280 divides ordinary cost by quantum, multiplies by its cached ratio, computes modulo basis, subtracts that remainder before division, adds one when the remainder is positive, and multiplies the resulting units by quantum.
The cache rebuild at lines 600 through 651 persists only twelve scalar composed ratios, without the discarded source-product digits.

The accepted follow-up adds twelve lines immediately after the final-cost assignment at pre-edit line 564.
Its post-edit effect-file SHA-256 is `622ff8dc8e720c38efe4f9fe5047f9771e9759f582729ec74d136be050dda9fe`.
The parent-owned trigger hash remained `fbf4289e5fa2dd3e82514279ec92eb7ac0c6aeafb99366145245349522d0335d` after the patch.
Recovery, if required, removes only this additive guard and its two comment lines while preserving any later parent edits.

```txt
if = {
	limit = {
		check_variable = {
			var = universal_cost_quote_final_cost
			value = universal_cost_quantize_quantum
			compare = less_than
		}
	}
	set_temp_variable = { universal_cost_quote_final_cost = universal_cost_quantize_quantum }
}
```

The guard runs only after a positive ordinary cost has matched at least one source.
It executes before displayed and saved quote fields are calculated, and it does not change the quantizer's scratch result, source ratio, payment providers, or receipts.
The effective quantum must be positive and representable, as required by the registered quantum contract.
This patch does not extend that contract to invalid caller quanta or recover an ordinary input that overflowed before quotation.
An existing default-handling limitation remains: the quantizer replaces a supplied nonpositive quantum only inside its positive-amount branch.
If an explicitly zero quantum accompanies an amount already truncated to zero, that branch does not run and this guard compares zero with zero.
That case does not receive the default one-unit minimum from this patch, and no quantum-default normalization change was authorized or applied.
The corrected scenarios below supply the registered positive quanta 1 and 0.01.

## Exact local references and MCP route gaps

The connected tool catalog exposed `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and `hoi4.event_inspect` with their live schemas.
Exposure did not establish service health.
The call to `hoi4.reference_context` used surface `general`, limit 8, and question `fixed-point variable precision range overflow multiply divide modulo ceil_variable script_constants scripted effects`.
It returned the exact error `timed out awaiting tools/call after 600s`.
Parallel searches for `variable` in wiki/game documentation and `round_temp_variable` in game/script documentation each returned `timed out awaiting tools/call after 600s`.
The source lookup for `universal_cost_quote_integer`, kind `scripted_effect`, one definition, 25 lines, and no references also returned `timed out awaiting tools/call after 600s`.
The initial event selector omitted `kind` and returned input validation error `Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`.
An intermediate selector with `kind = event` and `id` returned `expected string, received undefined at selector.eventId` and `Unrecognized key: "id" at selector`.
The corrected narrow request used `mode = trace`, `selector = { kind: "event", eventId: "chaosx.nr26.1" }`, depth 1, nodes 10, and edges 15, and returned no result during an explicitly measured 30,000 ms observation window.
The selector errors were corrected and are not described as a server capability gap.
The corrected request's missing result leaves current event evidence unresolved.
During the accepted invariant follow-up, the corrected event trace and a `check_variable` reference search were each retried and returned no result within measured 20,000 ms observation windows.
The connected catalog did not expose `hoi4.script_validate`, so that newer validation route was unavailable in this client.
A separate search for `2147483647` returned no result during an explicitly measured 30,000 ms observation window.
No returned citation IDs or revisions were available for a valid `hoi4.reference_read` request.
No artifact URI, continuation URI, completed event coverage, server health result, or source revision was fabricated.
Direct local reads below are reference evidence only and do not replace the unavailable MCP event evidence.
No helper-expansion, job, native-task, focus, GUI, map, owner, or AI analysis was attempted.
Cost ratios are deterministic payment fractions, not probability weights, so this bounded arithmetic audit introduces no probability-bearing helper and requires no AI probability patch or comparison.

| Reference | Read lines and finding | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 425-447: script variables have five decimal places, excess precision truncates, and the documented numeric range is approximately signed 32-bit whole numbers plus a five-digit fractional part. 558-575: temporary variable operations, Euclidean modulo, and nearest-integer rounding. 1485, 1591, 1596: deprecated manpower readers retain a separate roughly 2.147-million overflow warning. | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 3587-3611: variable division and zero-divisor handling. 4986-5028: temporary modulo and multiplication syntax. 6476-6495: variable rounding. | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 184-214: math expressions use fixed-point arithmetic, sequential operations, and parse-failure zero. 215-245: shared script constants and explicit `constant:` access. | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-84: constant schemas, fixed-point and integer data, and scoped variable access. | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_math_functions.md` | 1-325: enumerated arithmetic functions contain `mod`, `divide`, `multiply`, and nearest-integer `round`, but no documented ceiling or arbitrary-precision rational primitive. | `3c7116906f0bc7590cdd014f5a8b3cf8ef9f0685044fc10e29fabd19afaf832b` |

The installed arithmetic documentation does not independently state the script-variable range, low-level multiplication intermediate width, or overflow wrapping algorithm.
The analysis therefore uses the new offline wiki's numeric envelope as a documented model and identifies out-of-range products without predicting their wrapped values.
The positive upper envelope quoted in the wiki is `2147483647.99999`.
Its negative-end wording and separate manpower warnings are not used to infer additional engine behavior.
The approximately 214k ordinary-cost boundary applies when multiplying by the full 10000 basis.
At ratio 5000 the documented product boundary is approximately 429496.73, and at ratio 2500 it is approximately 858993.46.
An ordinary 200000 is therefore within this multiplication envelope at both sale ratios, while 1000000 exceeds it at both.
The source-composition products for the two ordinary sale sources reach at most 100000000, which fits this documented envelope.

Additional directly read precedent: vanilla `common\scripted_effects\zz_debug_effects.txt` lines 74-82 multiplies, rounds, and clamps `num_to_create`.
That proves an installed structure example, not a precedent for exact upward rational quantization.
For the accepted minimum guard, the installed `documentation\triggers_documentation.md` lines 2110-2140 directly document variable-to-variable `check_variable` comparisons and `compare = less_than`.
That file's SHA-256 is `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The installed `documentation\effects_documentation.md` lines 4677-4684 document conditional `if` effects and lines 7820-7840 document assigning one temporary variable from another, using the previously recorded file hash.
The offline Data structures temporary-variable/scoping sections, Scopes country/trigger examples, Localisation variable formatting lines 184-203, Effects scripted effects lines 4683-4697, and Triggers scripted-trigger section and temporary-variable note at line 2545 were consulted.
The existing `chaosx_dynamic_effects.txt` and matching markdown were inspected and provide no exact rational quantizer that can replace this pipeline.
The events, decisions-missions, and subagents skills were used without modification.
No skill update was made outside the explicit write scope.

## Meaningful arithmetic scenarios

Executed 28 BigInt rational-oracle scenarios in memory.
The oracle keeps five-decimal input values as integer ticks, multiplies exact rational source fractions, and computes the final ceiling once.
The existing-path model truncates each positive fixed-point multiply/divide result to five decimals and applies the source's documented nearest-integer correction or trigger remainder calculation.
Overflow cases are labeled unresolved after the out-of-envelope operation and are not assigned invented engine results.
These are arithmetic checks under the documented model, not game execution, MCP evaluator results, or live affordability/debit observations.

| Ordinary current cost | Quantum | 5000 expected | 2500 expected | Observed source arithmetic under the model |
| ---: | ---: | ---: | ---: | --- |
| 0 | 1 | 0 | 0 | both paths preserve zero |
| 1 | 1 | 1 | 1 | both match |
| 2 | 1 | 1 | 1 | both match |
| 3 | 1 | 2 | 1 | both match |
| 5 | 1 | 3 | 2 | both match |
| 101 | 1 | 51 | 26 | both match |
| 125 | 1 | 63 | 32 | both match after the ordinary surcharge is included |
| 200000 | 1 | 100000 | 50000 | both match within the documented envelope |
| 1000000 | 1 | 500000 | 250000 | effect and trigger numerator exceed the documented envelope |

| Additional case | Exact expected | Effect before guard | Effect after guard | Unchanged trigger model |
| --- | ---: | ---: | ---: | ---: |
| Ordinary 0.05, quantum 0.01, ratio 5000 | 0.03 | 0.03 | 0.03 | 0.03 |
| Ordinary 0.04001, quantum 0.01, ratio 2500 | 0.02 | 0.01 | 0.01 | 0.02 |
| Ordinary 0.00001, quantum 1, ratio 5000 | 1 | 0 | 1 | 1 |
| Ordinary 0.00001, quantum 0.01, ratio 5000 | 0.01 | 0 | 0.01 | 0.01 |
| Ordinary 2.00001, quantum 1, ratio 5000 | 2 | 1 | 1 | 2 |
| Ordinary 5, quantum 1, ratios 5000 then 5000 | 2 | 2 | 2 | 2 |
| Ordinary 6, quantum 1, ratios 5000 then 3333.33335 | 2 | 1 | 1 | 2 |
| Ordinary 1000000, quantum 1, ratios 5000 then 0.001 then 0.001 | 1 | 0 | 1 | ratio zero rejects the quote |
| Ordinary 1000000, quantum 0.01, ratios 5000 then 0.001 then 0.001 | 0.01 | 0 | 0.01 | ratio zero rejects the quote |
| Ordinary 1000000, quantum 0.01, ratio 5000 | 500000 | numerator 5000000000 exceeds envelope | overflow remains unresolved | numerator 500000000000 exceeds envelope |

The initial 28 checks contained seven effect-path precision/minimum mismatches and three distinct scenarios with out-of-envelope products.
The accepted guard corrects the four zero-price scenarios, leaving three non-overflow ceiling mismatches and the three overflow scenarios unresolved.
The zero-ratio composition scenarios now produce the effect-side minimum, but the unchanged central trigger still rejects that invalid scalar ratio, so their display/payment consistency remains blocked.
Eight additional bypass checks preserve zero with both quanta, negative -5 and -0.00001 with eligible sources, and no-source ordinary values 0.00001, 0.5, 125, and 200000.
Source-linked validation confirms that the exact accepted guard uses `universal_cost_quantize_quantum`, follows the quantizer and final-cost assignment inside the existing positive/source-count branches, and precedes displayed-cost assignment.
An initial verification model omitted the enclosing positive-ordinary condition and therefore incorrectly clamped its zero fixtures.
That model was corrected to reflect the actual unchanged source guard before the reported verification results were accepted.
The ordinary 125 fixture represents a cost provider that has already applied the normal 25-percent surcharge to 100.
No ordinary modifier calculation or owner behavior was changed.

One further exact-composition counterexample was checked separately: ordinary 2, quantum 1, source ratios 9999.99999 and 5000.00001.
Their exact composed basis ratio is `5000.00000499999999`, while the scalar cache stores `5000` under the documented truncation model.
The exact final cost is 2, but both current paths return 1.
This mismatch survives replacing the final quote multiply/divide with an otherwise exact bounded scalar algorithm.
It proves that a cached scalar ratio alone cannot reproduce all-source exact upward rounding for the currently accepted fractional source inputs.
Raising a zero ratio to an epsilon cannot recover those discarded digits and remains rejected as an arithmetic approximation.
The accepted one-quantum minimum implements its separate invariant and does not recover exact composition or ceiling information.

## Bounded quotient/remainder decomposition

For a represented ordinary cost C, basis B = 10000, an integer composed basis ratio R in (0, B], and registered quantum Q = 1 or 0.01, decompose `C = B*a + r` using `r = C mod B` and `a = (C-r)/B`.
The exact unrounded amount is `a*R + r*R/B`.
The first term is an integer, so it is a multiple of both registered quanta.
Compute `p = r*R`, `m = p mod (B*Q)`, and return `a*R + (p-m)/B + (Q when m > 0)`.
Every division of the retained payable component is exact at the registered quantum.
The remainder branch retains positive subquantum information before division.
The product `r*R` is less than 100000000 and `a*R` is at most the ordinary cost, so this avoids the original large numerator within the documented envelope.
The final sum must still be representable, and no output can repair an ordinary input that overflowed before entering the helper.

This identity passed 48 separate BigInt checks over ordinary values 0, 0.00001, 0.04001, 1, 2, 2.00001, 3, 5, 101, 125, 200000, and 1000000, both ratios 2500/5000, and both registered quanta.
It is an exact mathematical candidate for that input subset.
It is not an unrestricted repair because source registration currently accepts fractional ratios, composition can truncate to zero, and other owner quanta have not been constrained to this subset.
No subset restriction was inferred from the requested semantics.

### Exact proposed parent trigger bridge for that subset

The following replacement for the observed trigger's positive-cost arithmetic is exact only after an exact composition provider has proven an integer R and a registered Q of 1 or 0.01.
It uses the existing parent trigger names and shared constants.
Do not apply it unguarded to the current unrestricted scalar cache.
It is a reviewable bounded bridge candidate, not a ready unrestricted implementation or an accepted exclusion of fractional ratios.

```txt
set_temp_variable = { black_friday_quote_remainder = black_friday_quote_ordinary_cost }
modulo_temp_variable = {
	var = black_friday_quote_remainder
	value = constant:universal_cost_framework.basis
}
set_temp_variable = { black_friday_quote_final_cost = black_friday_quote_ordinary_cost }
subtract_from_temp_variable = { black_friday_quote_final_cost = black_friday_quote_remainder }
divide_temp_variable = { black_friday_quote_final_cost = constant:universal_cost_framework.basis }
multiply_temp_variable = { black_friday_quote_final_cost = black_friday_quote_composed_ratio }
set_temp_variable = { black_friday_quote_numerator = black_friday_quote_remainder }
multiply_temp_variable = { black_friday_quote_numerator = black_friday_quote_composed_ratio }
set_temp_variable = { black_friday_quote_denominator = black_friday_quote_rounding_quantum }
multiply_temp_variable = { black_friday_quote_denominator = constant:universal_cost_framework.basis }
set_temp_variable = { black_friday_quote_remainder = black_friday_quote_numerator }
modulo_temp_variable = {
	var = black_friday_quote_remainder
	value = black_friday_quote_denominator
}
subtract_from_temp_variable = { black_friday_quote_numerator = black_friday_quote_remainder }
divide_temp_variable = { black_friday_quote_numerator = constant:universal_cost_framework.basis }
add_to_temp_variable = { black_friday_quote_final_cost = black_friday_quote_numerator }
if = {
	limit = { check_variable = { black_friday_quote_remainder > constant:universal_cost_framework.zero } }
	add_to_temp_variable = { black_friday_quote_final_cost = black_friday_quote_rounding_quantum }
}
```

An effect-side implementation must use this same identity with the corresponding `universal_cost_quote_*` inputs and outputs and preserve the existing zero/negative/no-source behavior.
The accepted effect-side minimum guard needs no central trigger edit for positive quotes with a nonzero cached ratio because that trigger already preserves the positive minimum.
The proposed bounded decomposition above remains unimplemented and was not selected as a substitute ceiling algorithm.
The current effect/trigger mismatch remains a consistency blocker for the parent.
An unrestricted exact trigger patch remains blocked on the exact source representation and a verified trigger-readable evaluation route.

## Proposed helper map and exact architecture

The following helpers are proposals for parent review and are not unused declarations in the repository.
Prefer extending the existing quote and cache entry points rather than moving transaction or owner systems.

| Responsibility and proposed name | Scope | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- | --- |
| Extend `universal_cost_quote_integer` | payer-selected scope | ordinary current cost, family, positive quantum, exact source representation | same displayed/final/saved fields plus explicit arithmetic validity | temporary arithmetic, existing owner confirmation call sites retained |
| Internal `universal_cost_compose_exact_ratio` | effect chain | eligible source ratios in the current deterministic order | exact rational numerator/denominator digits, source count and identity proof | temporary digit storage, called by existing quote/cache rebuild only |
| Internal `universal_cost_quote_exact_product` | effect chain | represented C and Q, exact rational source product | exact payable quantum ceiling without an oversized scalar unit count | temporary bounded arithmetic, called by existing quote only |
| Extend `universal_cost_rebuild_custom_quote_ratio_cache` | existing registry-mutating effect scope | same exact family composition | exact family representation and generation validity beside legacy scalar display data | current successful register/clear call sites, global family representation publication only |
| Parent-owned exact trigger evaluator | read-only payer trigger | ordinary current cost, Q, exact family representation and generation | fresh exact final cost and validity | temporary arithmetic only, `black_friday_quote_custom_cost` bridge, no global quote scratch |
| Extend `universal_cost_clear_custom_quote_ratio_cache` | existing source-expiry effect scope | none | invalidated exact family representation | same existing expiry calls, no receipt mutation |

Represent five-decimal source ratios as integer ticks and exact source fractions as `ratio_ticks / 1000000000`.
Represent the ordinary cost and quantum as integer ticks as well, without forming an oversized scalar `C*100000`.
Extract whole and fractional limbs by Euclidean modulo and exact division before multiplication.
Use bounded small limbs for exact numerator/denominator products and carry propagation, followed by exact comparison/division to determine the payable quantum ceiling once.
Keep all discarded digits or an exact rational representation, because a mere positive-remainder bit cannot determine how many quanta a large ordinary cost owes.
Do not introduce per-source cost rounding, a forced epsilon ratio, floating-point calculations, or a substitute quote table.

A candidate radix is 1000, with each digit product below 1000000, but a full carry bound, scalar extraction proof, rational division implementation, source-count capacity, and loop batching proof must be established before it becomes an engine helper.
The source registry has no accepted small source-count cap, while the repository documents the 1000-iteration effect-loop limit.
An arbitrary-precision effect implementation also does not prove a matching trigger implementation, because the existing bridge avoids source-array traversal and effect calls.
The installed math-expression/collection and trigger routes must be checked for an exact read-only evaluator or a complete bounded representation before choosing that bridge architecture.
This is broader representation work than the requested narrow patch and remains a parent plan, not permission to cap registered sources or weaken exact semantics.

### Constants and tuning plan

Retain basis 10000, sale ratios 5000/2500, ordinary current modifiers, and registered quanta unchanged.
The native eligibility-mask contract remains frozen at thirty bits, and this audit proposes no enum, mask, or matcher changes.
Any later digit implementation should centralize the proven tick scale, radix, carry bounds, batching limits, and representable output checks in the dedicated framework constants file.
These are representation constants, not new balance targets.
The current `gate_epsilon` is an affordability comparison value and must never be added to a payable amount to imitate a ceiling.
No arithmetic or tuning constant was added here.

### Event targets and cleanup plan

No event target is required by quotation arithmetic.
Temporary quote work remains in the current payer effect/trigger chain.
If exact family cache digits are introduced, registry mutation must build them deterministically and publish validity only after all family rows are complete.
The existing clear-cache call must invalidate those digits at expiry, and a fresh confirmation must resolve the current generation.
Receipt amounts remain actual-paid amounts and must never be recomputed during this migration or cleanup.
No recurring world scan or owner lifecycle change is proposed.

### Migration plan

First recover required MCP reference and event evidence, verify the installed representation limits, and select an exact effect/trigger representation that covers every currently accepted source and quantum.
Preserve exact pre-edit source copies and scenario fixtures when a gameplay patch is ready.
Implement the representation and quantizer inside the existing framework quote/cache entry points.
Have the parent apply the matching central trigger bridge in the same tranche.
Keep ordinary cost providers, eligibility, payments, receipts, refunds, owner AI, and call sites intact.
Compare exact display, affordability, and payment results for the scenarios above, both source orders, identity/no-source state, expiry, and payer isolation.
The accepted minimum guard retains the existing consistency blocker for ceiling failures and zero composed ratios until an exact trigger bridge matches.
The unrestricted rational architecture requires parent review because it exceeds a small scalar helper extraction.

## Simplifications, omissions, and blockers

No rounding approximation, gameplay simplification, fallback, or source-domain restriction was applied.
The explicitly accepted positive-minimum repair is implemented.
Unrestricted exact ceiling, overflow repair, and all-source composition remain incomplete and queued for parent follow-up.
Required MCP context, reference searches, and source lookup timed out after 600 seconds, the corrected event inspection returned no evidence within the measured observation window, and installed documentation alone does not specify the complete numeric storage and multiplication behavior.
The current scalar cache cannot preserve all-source exact composition, and an unrestricted trigger bridge has not been proven.
The bounded candidate covers integer R and Q = 1/0.01 only and must not be described as a universal repair.
Task-specific native quote/display/debit validation was not run because it is user-owned.
No HOI4 process was launched, event enabled, owner or AI changed, or catalog written.
Parent follow-up is required for the exact representation, trigger integration, recovered MCP evidence, and native acceptance evidence.
