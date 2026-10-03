# Universal exact quotation predicates

These predicates provide the arithmetic used by both `universal_cost_quote_integer` and `black_friday_quote_custom_cost`.
They operate in an existing payer or owner-selected object scope and change temporary variables and arrays only.
They do not inspect countries, states, or other objects outside that selected scope.
The neutral framework contract is in [universal_cost_modifier.md](../../docs/systems/universal_cost_modifier.md).

## Public producer contract

`universal_cost_quote_exact = yes` accepts temporary `universal_cost_quote_ordinary_cost`, `universal_cost_quote_family_mask`, and `universal_cost_quote_rounding_quantum`.
The ordinary input must include the owner's ordinary current modifiers.
An absent or non-positive quantum uses the existing default one-unit quantum.
The same live aligned registry supplies source IDs, represented ratios, priorities, and eligibility masks to both frontends.
There is no finite canonical-family quotation table.
The source ratio domain and thirty-bit source-mask contract are the existing registration contract, without an added integer-ratio, small-cost, quantum, or source-count restriction.

Outputs are temporary `universal_cost_quote_final_cost`, `universal_cost_quote_displayed_cost`, `universal_cost_quote_saved_cost`, `universal_cost_quote_source_count`, `universal_cost_quote_primary_source_id`, and `universal_cost_quote_valid`.
The producer returns true so that arithmetic inside a loop cannot stop subsequent iterations; callers must check `universal_cost_quote_valid` before using the amount.
A malformed aligned registry or a mathematically nonrepresentable scalar price yields validity zero, preserving the initialized amount only as an invalid diagnostic value.
The shared quoted-affordability effect rejects invalid quotes, and the Black Friday bridge returns false for them.
Owner-specific payment providers must likewise honor validity before committing a quote.

`universal_cost_quote_composed_ratio` is a retired scalar field: basis with no participating source, and zero meaning unavailable with participating sources.
Its zero never means a zero price or a rejected source product.
No runtime consumer outside the replaced quote/cache/bridge blocks used this field in the inspected repository.
Read the source registry and source-proof outputs rather than introducing a truncated scalar product.

Positive prices with at least one eligible source are rounded upward exactly once to a whole number of the requested quanta.
Positive prices without an eligible source retain the ordinary amount without quantization.
Zero and negative/reward inputs are preserved.
Saved amount is the non-negative difference between ordinary and final price.
Priority selects the primary source; equal priorities select the earliest registry row, preserving the existing stable tie behavior.
Price multiplication is exact and commutative, so registration order cannot change the payable amount.

Example in a trigger:

```txt
set_temp_variable = { universal_cost_quote_ordinary_cost = owner_current_cost }
set_temp_variable = { universal_cost_quote_family_mask = constant:universal_cost_family.equipment }
set_temp_variable = { universal_cost_quote_rounding_quantum = owner_quantum }
set_temp_variable = { universal_cost_quote_final_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_displayed_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_saved_cost = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_valid = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_source_count = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_primary_source_id = constant:universal_cost_framework.zero }
set_temp_variable = { universal_cost_quote_composed_ratio = constant:universal_cost_framework.zero }
hidden_trigger = { universal_cost_quote_exact = yes }
check_variable = { universal_cost_quote_valid = constant:universal_cost_framework.one }
```

The effect frontend retains the same public input/output names and invokes this predicate in an effect `if.limit`.
Its public outputs are initialized in the enclosing effect chain before calling the producer, following the offline wiki's temporary-variable lifetime warning.
The central Black Friday bridge likewise initializes the shared outputs before calling the producer.
Its existing owners retain family-default quanta (one unit, or .01 for Stability/War Support).
A generic caller can supply positive `black_friday_quote_requested_quantum`; the bridge consumes and resets this optional input so a later owner quote cannot inherit it.
The bridge still requires the active Black Friday state, existing readiness marker, and positive family mask, and returns the actual quote-validity result.

## Caller-owned temporary lifetime

Offline Data structures line 440 warns that temporaries first created inside a scripted helper may disappear when it returns, while a caller-defined temporary retains the helper's modifications.
The array sections at lines 1073-1076 apply the same distinction to temporary arrays and treat array elements as variables.
The implementation and source VM conservatively apply that rule to every scripted call, including public APIs and nested calls inside `if.limit`.
Native conditional blocks, hidden triggers, and array iteration are not separate scripted helper frames.

Every caller must define each temporary output it reads AFTER a helper returns, before that helper invocation.
Assignments at the beginning of the called helper do not establish storage in its outer caller.
This applies to `black_friday_quote_final_cost`, validity, effective quantum, source-result fields, and exact unit limbs just as it does to local scalar/digit outputs.
Owner adapters outside the assigned exact-quote block must establish their own outer output storage; this package cannot export new temporaries into an undeclared caller frame.

Internally, each output-only limb array is created in the caller with `resize_temp_array` and one placeholder element before the helper clears and fills it.
Input/output product arrays are already constructed in their caller and retain mutations through multiplication, trimming, and scalar reconstruction.
The placeholder is storage initialization, not a price, precision, source-count, or digit-count limit.
Scalar result/validity and division comparison outputs are likewise initialized immediately before their calls.
Outputs used only inside a helper remain helper-local and are deliberately discarded after it returns.

| Helper boundary | Caller-owned temporary outputs / in-out storage |
| --- | --- |
| scalar extraction | `uc_exact_factor` |
| multiplication and trimming | existing `uc_exact_product` |
| family matching | `universal_cost_source_matches_quote` |
| source finder | `universal_cost_source_found_index` |
| division trial | `uc_exact_comparison`, `uc_exact_trial_product` |
| product quantizer | `uc_exact_scalar_result`, `uc_exact_scalar_valid`, existing product, `uc_exact_units`, `uc_exact_units_tokens` |
| ticks-to-scalar decoder | `uc_exact_scalar_result`, `uc_exact_scalar_valid`, existing product |
| standalone quantizer | quantize result/validity, scalar units/units-validity, effective quantum, `uc_exact_units` |
| Black Friday source wrappers | existing public register/clear result field before the generic API call |
| public quotation APIs | the final/displayed/saved/validity/source-proof outputs read by their outer owner caller; effective quantum when observed |

The standalone quantizer publishes zero unit limbs for zero/reward inputs, including a warm caller whose preceding quote had positive units.
Its effect frontend creates `uc_exact_units` in the effect caller before invoking the nested scalar producer.
An owner reading unit limbs after the public effect returns must also create that array before calling the effect.

The actual-source VM uses separate temporary and regular stores, deletes newly created temporary names on every scripted return, retains inherited temporary changes, and preserves regular writes and regular storage hidden by a temporary of the same name.
It asserts each declared output exists at helper entry; this audit does not initialize internal scratch or bypass cleanup.
Its outer test fixtures explicitly declare public outputs to model a conforming owner caller, and negative controls show that bare public API calls lose newly created outputs.

## Arithmetic and bound proof

All represented scalar inputs have five fractional digits.
Write `Cticks` and `Qticks` for their exact integer ticks and write each source fraction as `Rticks / 1000000000`.
The implementation splits whole and fractional input parts before building radix-1000 limbs; it never forms a scalar `C * 100000` or `C / Q`.
Five limbs represent every non-negative scalar tick value in the documented envelope.
Only the ordinary whole portion remains a large scalar during extraction and reconstruction.

The numerator starts as the cost tick limbs and multiplies every eligible non-identity source's ratio tick limbs.
An identity ratio contributes source proof but needs no multiplication or denominator shift.
Each non-identity source contributes three low denominator limbs because `1000000000 = 1000^3`.
Digit multiplication carries after each product; its accumulator is at most `999*999 + 999 + 999 = 999999`, independent of product length and source count.
Arrays grow with the input product; five and six are scalar/divisor representation widths, not product or source-count caps.

After all multiplications, separate the numerator at the denominator shift into an integer high part `H` and a fractional low part `f`, with `0 <= f < 1`.
Keep whether any removed low limb is positive as a sticky bit.
Divide `H` by the arbitrary positive integer `Qticks` using radix long division.
The remainder is always less than `Qticks`; the next-digit trial needs at most six limbs.
Ten binary-search iterations resolve one quotient digit in the complete range 0 through 999.
Comparison runs from high to low; subtraction propagates a one-digit borrow.

Because `Qticks` is an integer, the exact upward unit count is `H div Qticks + 1` precisely when `H mod Qticks > 0` or `f > 0`.
A positive fractional tail is retained through this test even when every scalar ratio composition would have become zero.
Multiply the exact upward unit limbs by the exact quantum limbs to obtain price ticks, then reconstruct the represented scalar price only after checking the positive envelope `2147483647.99999`.
There is no per-source rounding, nearest-integer ceiling approximation, forced epsilon, or saturated price.

## Trigger iteration capability

Installed `documentation/triggers_documentation.md` documents temporary arrays, `resize_temp_array`, temporary arithmetic, and `all_of_scopes`.
Offline Data structures explicitly permits temporary array mutation in triggers and documents that `all_` trigger scopes visit targets in order until a false body.
Installed `common/scripted_effects/00_scripted_effects.txt` lines 498-520 uses `all_of_scopes` with temporary arithmetic inside an effect limit.

Each loop here creates an array filled with the current `THIS` pointer and uses its entries only as iteration tokens.
The cursor is temporary, so these loops neither reinterpret numeric digits as scopes nor scan the world.
Nested loops use separate token arrays and never modify the array being traversed.
Loop bodies contain producer arithmetic and conditional assignments only, and remain true.
They do not use `while_loop_effect` or `for_loop_effect`, whose documented 1,000-iteration limit would otherwise truncate source or digit traversal.
No localisation-generated text, recursive meta trigger, meta effect, dynamic effect key, or undocumented trigger-loop command is required.

This documented route is implemented and source-tested, not native engine evidence.
Repeated scope entries, native confirmation of the conservative temporary-lifetime model, dynamic resize sizes, engine arithmetic internals, and consumer performance still need returned MCP/native acceptance evidence.
The local interpreter intentionally assumes ordered, duplicate-preserving array iteration and the documented fixed-point operations; it cannot establish those engine facts itself.

## Internal helper map

All helpers below use the selected valid object scope, default to explicit scratch initialization, and have temporary-only side effects.
Scratch variables and arrays start with `uc_exact_` to keep them separate from owner fields.

| Helper | Inputs | Outputs | Direct caller |
| --- | --- | --- | --- |
| `universal_cost_exact_scalar_to_ticks` | non-negative `uc_exact_scalar` | little-endian `uc_exact_factor` tick limbs | quote, product quantizer, standalone quantizer |
| `universal_cost_exact_multiply` | `uc_exact_product`, `uc_exact_factor` | replaces product with exact limb multiplication | quote composition, product quantizer, standalone quantizer |
| `universal_cost_exact_trim_product` | product limbs | removes high zero limbs, preserving one for zero | multiplication |
| `universal_cost_exact_match_family` | source mask, quote family mask | `universal_cost_source_matches_quote` | quote, existing effect family matcher |
| `universal_cost_exact_find_source` | source ID, live registry | first matching row index or invalid index | register and source-identified clear |
| `universal_cost_exact_division_trial` | quantum limbs, six-limb remainder, trial digit | six-limb trial product and comparison -1/0/1 | product quantizer |
| `universal_cost_exact_quantize_product` | exact numerator product, denominator shift, positive `uc_exact_quantum_scalar` | exact unit limbs in `uc_exact_units`, scalar result and validity | quote, standalone quantizer |
| `universal_cost_exact_ticks_to_scalar` | product tick limbs | `uc_exact_scalar_result`, `uc_exact_scalar_valid` | product quantizer, standalone unit-scalar publication |
| `universal_cost_exact_quantize_scalar` | quantize amount, optional quantum | quantize result/validity, exact unit limbs, scalar units/units-validity | existing `universal_cost_round_up_to_quantum` effect |
| `universal_cost_quote_exact` | ordinary price, family mask, optional quantum, live registry | public quote fields and source proof | existing effect quote, central Black Friday trigger |

Standalone `universal_cost_round_up_to_quantum` exposes `universal_cost_quantize_valid` and `universal_cost_quantize_units_valid`.
An exact price may fit when its integer number of very small quanta cannot fit as one scalar.
In that case scalar units are unavailable (`units_valid = 0`, scalar units zero), while the exact unit limbs remain in `uc_exact_units` and the payable price is still valid.
No production caller outside the quantizer used scalar units in the inspected repository.

## Lifecycle and validation

Quotation needs no event target, persistent per-payer cache, recurring hook, new flag, or world scan.
Scratch arrays are cleared before reuse and expire with the trigger/effect chain.
Register/clear uses the same read-only source finder, so rows beyond 1,000 are not silently skipped.
The existing cache entry points retain the Black Friday readiness marker and remove the twelve retired scalar variables.
They never clear the live registry or payer receipts.
Clearing a source removes only its aligned row; remaining sources still participate in the generic exact quote.
Historical actual-paid receipt values remain unchanged.

[Source tests](../../docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js) parse the actual helper bodies, assert every arithmetic operation fits the documented envelope and every division/multiplication retains full represented precision, and compare the results to an independent direct BigInt rational oracle.
[Implementation handoff](../../docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-03_exact_quote_implementation.md) records scenarios, source hashes, reference spans, route gaps, and remaining integration responsibilities.
No native-cost universality or live debit claim follows from this arithmetic evidence.
