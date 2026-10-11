# Event 026 bounded CBRN coverup localisation audit

## Current bounded recheck, 2026-10-07

Disposition: implemented source fixes verified by current reads and actual source-model cases, with native consumer evidence unresolved.
This section supersedes the initial findings and initial validation status retained below.
Parent acceptance basis is the explicit resumed assignment to review the updated recovery preflight, malformed-pointer fallback, shared affordability predicate, and two wording repairs.
Only the named handoff was edited by this auditor.

### Closed source findings

1. **Pending pointer validation: closed for the inspected source contract.** All four price/detail getters initialize `cbrn_occupation_coverup_target = FROM` and receipt ID zero before `cbrn_occupation_coverup_can_retry_refund`.
The current helper in `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt:4-20` requires a positive open ID, existing target/paid/phase fields, exact target correspondence, positive paid amount, and refund phase 1 or 2.
Detail getters read the saved paid amount using the validated exported receipt ID.
Each fresh branch also rejects any existing open-pointer variable, including a zero-valued pointer.
Malformed pointers therefore reach `Price unavailable`, rather than recovery or a fresh purchase.

2. **Shared affordability: closed for the inspected source contract.** The two fresh-purchase branches now set kind Political Power and amount to the authoritative quote, then invoke `universal_cost_component_is_affordable`, matching the nested hover selector.
Both native `available` and `custom_cost_trigger` continue through their shared owning `can_pay` helper.
The same validated recovery helper supplies the zero-PP recovery branch in both payment gates and all four display getters.

3. **Concrete prose: closed.** Current English keys `cbrn_occupation_seal_state_cost_details` and `cbrn_occupation_destroy_records_cost_details` contain the exact recommended wording below.
The parent applied these changes.
Existing getter calls, source clause, formatting, and refund meaning are retained.
The former vague resource wording and awkward rejection wording are absent from these two current keys.

### Executed source-model validation

Executed the existing `2026-10-07_cbrn_coverup_cost_source_tests.js` production-source harness using Node v24.15.0, with an in-memory loader extension and 54 additional bounded localisation scenarios.
The complete run passed **133 scenarios: 79 existing scenarios and 54 additional cases**.
No test file, result JSON, implementation source, or other documentation was written or patched.

The first unchanged runner failed with `unsupported tested command cbrn_occupation_coverup_can_retry_refund` because its load list did not yet include the new trigger file.
The in-memory extension loaded the actual `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt` through the runner's existing parser, and declared its target/receipt-ID caller-output contract for conservative helper-lifetime checks.
It did not mock the new preflight or substitute its result.
An initial additional fixture failed its own caller-output declaration assertion, then the outer fixture was corrected to initialize the existing four quote outputs before invoking payment gates.
Neither failure is counted as a passing production case.

Added cases use payer GER, target state 64, receipt ID 1, score `500.12345`, source 26 at 50% discount, and zero current PP unless otherwise specified.
Valid saved receipt fields are target 64, paid `40.00008`, and phase 1 or 2.

| Additional cases | Count | Observed source-model result |
| --- | --- | --- |
| Four getters × zero ID, negative ID, missing target, wrong target 65, missing paid, zero paid, negative paid, missing phase, phase 3, phase 0 | 40 | Exact `§RPrice unavailable§!`, both payment gates false, normal payer storage unchanged, no native writes |
| Four getters × valid phase 1 or 2, then remove open pointer and remove all source-registry rows | 8 | Recovery permitted at zero PP, numeric getters return `Payment recovery`, detail getters show saved `40.00008` and no-new-purchase text, no Black Friday clause; afterwards fresh ordinary `80.00987` or `120.01481` returns with no recovery or sale clause |
| Two action costs × PP one represented tick below, exactly equal, one tick above | 6 | Shared gate false/red below and true/yellow at or above; both gate and hover execute `universal_cost_component_is_affordable` |

The existing 79 cases also passed against the new source, including ordinary/sale/invalid rendering of all four parent getters, pending-refund retry and clearing, receipt-paid refund behaviour, score clamping, fresh click-time score/source changes, and caller-output-loss negative control.
The nested price/detail tests render the actual YAML and scripted-localisation definitions through the existing harness, rather than asserting an independently rewritten selector.
The model conservatively discards helper-created temps on return and retains caller-preinitialized modifications.
Five-decimal fixed-point arithmetic, scope resolution, native resources, timers, flags, and modifiers are modeled.
Downstream sanctions publication is captured as an explicitly out-of-scope native boundary.
This proves the bounded source-model cases, not engine execution, timer expiry, serialization, multiplayer, or visual layout.

### Current localisation conclusions

Missing-key list: empty for the thirteen output keys and six native consumer keys.
Duplicate-key list: empty for the assigned outputs/getters.
Scripted-localisation issue list: no remaining issue demonstrated in these inspected and tested cases.
Dynamic opportunities: all requested price, source, saved-payment, and precision bindings are present, with no additional cache or parallel formula needed.
Cross-surface source mismatch: the former recovery/affordability mismatch is closed by the shared predicates and tested cases.
Workbook comparison remains outside scope, with no workbook mismatch or catalog readiness claim.
Encoding concerns: none observed in the assigned English file.
Prose vagueness and overcomplication: repaired in the two keys by the parent.
Bloat, obvious explanation, repetition, and other writing-style violations: no remaining material issue found in the assigned outputs.
No unresolved wording choice remains in the bounded set.
No attributed quotation occurs in these values, and this auditor changed no dynamic tokens or quoted text.

Final wording for any parent-authorized spreadsheet mirror:

```yaml
cbrn_occupation_seal_state_cost_details: "[This.GetCbrnOccupationCoverupQuotedPpCost][This.GetCbrnOccupationCoverupCostSource]\nThe Political Power cost rises with Condemnation. If sealing cannot proceed, any Political Power paid is refunded."
cbrn_occupation_destroy_records_cost_details: "[This.GetCbrnOccupationCoverupQuotedPpCost][This.GetCbrnOccupationCoverupCostSource]\nThe Political Power cost rises with Condemnation. If evidence destruction cannot proceed, any Political Power paid is refunded."
```

### Current source identities and retained uncertainty

Source SHA-256 values were returned by the successful test run and independently re-read immediately afterwards:

- `common/scripted_localisation/cbrn_occupation_value_localisation.txt`: `2a5495aea10e11216341142a372bdd5abc951103732809433fba8cc5c6b0bb96`.
- `localisation/english/cbrn_occupation_l_english.yml`: `23a74c0e952e417b73daa04f748543be4f268ccd61cc7ea30d8a29221aa217a2`.
- `common/scripted_triggers/cbrn_occupation_triggers.txt`: `55d9f4ce79911d202f42072f4cc01b59feaa1315299be6d0c5a42adafbcc5d3f`.
- `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt`: `a6c1beb547ef0cdd721141f95faa75422f6083cd523ec411e29334bf3bdeb615`.
- `common/scripted_effects/cbrn_occupation_coverup_cost_effects.txt`: `02ec95de08ec1058298c3c014e2b36cbd8e691a182fcf447909161dbd5cff9b7`.

Native decision cost/hover rendering remains unresolved.
No new MCP render or artifact URI was obtained during this recheck, and the initial MCP limitations below remain in force.
Source-model string rendering is not a production GUI raster and does not establish absence of overflow, clipping, poor wrapping, misalignment, or native colour defects.
The separately recorded standalone Technology Tree Viewer capability gap is unchanged.
No native/game launch, game inspection, or log search occurred.
No implementation simplification was made by this auditor, and no Event 026 or whole-framework completion claim is made.

## Historical initial audit, superseded by the current recheck above

Initial disposition: unresolved pending parent review, architect integration, and consumer evidence.
Authority: the parent requested read-only review of seven new getters and their English keys, then explicitly added the pending-payment branches.
Only this handoff was written.
No gameplay, localisation, other documentation, workbook, export, or Git index changes were made by this auditor.
Coordination remains through the parent.
The parent-provided default-26 restored/excluded gate at `b9e4e7540` and catalog status `Needs Testing` are excluded from this audit and were not independently verified.

## Findings requiring parent action

1. **Pending display accepts an unvalidated pointer.** In `common/scripted_localisation/cbrn_occupation_value_localisation.txt:90-95,113-118,137-144,162-169`, each first branch tests only `has_variable = cbrn_occupation_coverup_open_receipt_@var:cbrn_occupation_coverup_target`.
The detail branches then read the pointed-to paid field without checking its existence, the receipt phase, or its target correspondence.
An orphaned, zero, or malformed open pointer therefore selects the refund promise rather than the fresh-price branch, and its amount is not established by that branch.
At the final source recheck the gameplay gates require an open pointer greater than zero, while localisation still tests existence only, so a present zero pointer demonstrably chooses different branches in the two source contracts.
This is a source-level missing-validation finding, not evidence that a malformed pointer occurs in normal play.
Use the architect's authoritative read-only recovery preflight for all four selectors, initializing any forwarded outputs in the caller before invoking it.
Distinguish a valid outstanding refund from other unresolved payment phases.
An absent pointer already falls through correctly.
The parent must decide malformed-pointer disposition together with the owning recovery contract so presentation does not offer a new purchase while gameplay still rejects it as unresolved.

2. **Affordability predicate identity is unfinished in the reviewed snapshot.** `GetCbrnOccupationCoverupQuotedPpCost` at lines 186-195 sets resource kind Political Power and amount to the fresh quote, then calls `universal_cost_component_is_affordable`.
The two `cbrn_occupation_can_pay_*_pp` gates in `common/scripted_triggers/cbrn_occupation_triggers.txt:465` onward still repeat `NOT = { has_political_power < cbrn_occupation_coverup_pp_quote }` directly in their fresh-purchase branches.
For a valid positive quote these currently have the same inclusive mathematical boundary, but do not satisfy the parent-required shared component contract.
Have the owner call the shared kind-PP component after quote validity and align the recovery-only preflight with the display predicate.
The final source recheck adds an OR recovery branch for a positive open pointer, which does permit that recovery path at zero PP without producing a new quote.
Both native `custom_cost_trigger` and `available` already call their respective `can_pay` helper, so their gate is shared with each other.
Pending-row colour must follow that completed recovery gate, without testing affordability against the historical refund amount.
The architect was concurrently finishing this work, so re-read the final source before treating this finding as outstanding.

3. **Two fresh-price explanations need concrete wording.** `localisation/english/cbrn_occupation_l_english.yml:78-79` says “Political effort rises with Condemnation” and describes a “rejected seal” or “Rejected evidence destruction”.
“Political effort” hides the named resource and the rejection wording does not explain the condition that produces a refund.
Recommended replacements retain the exact getter tokens and source clause:

```yaml
cbrn_occupation_seal_state_cost_details: "[This.GetCbrnOccupationCoverupQuotedPpCost][This.GetCbrnOccupationCoverupCostSource]\nThe Political Power cost rises with Condemnation. If sealing cannot proceed, any Political Power paid is refunded."
cbrn_occupation_destroy_records_cost_details: "[This.GetCbrnOccupationCoverupQuotedPpCost][This.GetCbrnOccupationCoverupCostSource]\nThe Political Power cost rises with Condemnation. If evidence destruction cannot proceed, any Political Power paid is refunded."
```

These are recommendations only and remain unpatched.
The existing recovery wording “Retry the outstanding refund. This attempt makes no new purchase.” is clear and should remain, conditional on the validated recovery branch.

## Bounded coverage and source findings

Reviewed `GetCbrnOccupationSealStatePpQuote`, `GetCbrnOccupationDestroyRecordsPpQuote`, `GetCbrnOccupationSealStateCostDetails`, `GetCbrnOccupationDestroyRecordsCostDetails`, `GetCbrnOccupationCoverupQuotedPpCost`, `GetCbrnOccupationCoverupPpAmount`, and `GetCbrnOccupationCoverupCostSource`.
The latest reviewed definitions occupy lines 88-222 of `common/scripted_localisation/cbrn_occupation_value_localisation.txt`.
Price/detail English outputs occupy lines 71-83, with native consumer keys at lines 28-30 and 36-38 of `localisation/english/cbrn_occupation_l_english.yml`.

- Missing keys: none found among the thirteen literal output keys or the six native base/blocked/tooltip keys.
- Duplicate keys: none found for those keys across English localisation, and none found for the seven getter definitions across scripted localisation.
- Namespace issues: none found in the assigned chain.
- Scripted localisation issues: the pending-pointer validation gap above, plus unresolved native consumer evaluation.
- Encoding concerns: none observed in the assigned English file, whose byte prefix is UTF-8 BOM.
- Dynamic text opportunities: the fresh quote, fractional amount, source clause, and receipt-paid recovery amount already cover the requested values.
Keep these bindings instead of introducing display caches or another pricing formula.
- Raw requirements: the two linked native decision affordability blocks are hidden, and their state requirements use custom tooltips.
No new raw requirement text was found in the bounded price chain.
- Cross-surface mismatch: predicate identity and pending recovery gate remain owner follow-ups, rather than a mismatch in numeric YAML formatting.
The workbook was not inspected because it is outside this assigned price-key audit.
No catalog mismatch or catalog readiness is claimed.
If the spreadsheet owner mirrors these cost explanations, use the two final key/value recommendations above after parent acceptance.
- Sourced quotations: no attributed quotation appears in these outputs.
No quote wording or attribution was changed.

The four fresh-price/detail branches initialize `cbrn_occupation_coverup_pp_quote`, `cbrn_occupation_coverup_pp_ordinary`, `cbrn_occupation_coverup_pp_quote_valid`, and `cbrn_occupation_coverup_pp_source_id` before their authoritative prepare helper.
Each requires validity equal to one before selecting the fresh key and otherwise returns `cbrn_occupation_coverup_price_unavailable`.
This avoids consuming the nested amount/source getters after invalid quote production.

The nested amount getter copies the quote into independent remainder scratch storage, applies modulo one, and returns a literal YAML key.
Whole values use `|0`, fractional values use `|5`.
It does not round or mutate the quote and does not use an inline numeric expression as `localization_key`.
The quote-value keys are plain numeric substitutions for the native inline cost wrapper, while hover keys own their texticon and affordability colour.
The current consumers are decision costs and tooltips, with no discovered parchment consumer of these seven getters.
No separate plain report variant is required by the discovered bounded consumers.

The source selector tests the quote's primary source ID against constant 26.
It does not infer discount eligibility from global sale activity.
The selected source key delegates to `black_friday.cost_source.line`, which exists at `localisation/english/026_black_friday_l_english.yml:34`.
The valid pending detail key bypasses both fresh-price getters and the source clause and directly renders the normal saved paid field through a caller-local display temp with `|5`.
The `Payment recovery` inline status remains wrapped by the native base/blocked cost keys and their native colour selection.
The `£pol_power` texticon resolves to installed `interface/texticons.gfx:262-263` (`GFX_pol_power`).
No new icon is necessary.

## Price, branch, and boundary review

The two original prepare helpers remain authoritative and call `condemnation_prepare_scaled_fraction_cost` before `universal_cost_quote_exact`.
Their bases are 40 and 60 in `common/script_constants/cbrn_occupation_constants.txt:66-67`.
The shared Condemnation helper clamps score to 0..1000 and computes `base * (500 + score) / 500`, preserving its existing operation order and represented precision.
The exact quote frontend retains the ordinary fraction without a matching source and quantizes only when a source matches.
The caller quantum is one.
These are inspected source contracts, not executed engine-price proof.

| Case | Source-derived display expectation | Confidence limit |
| --- | --- | --- |
| No open receipt, valid no-source quote | Fresh amount, whole `|0` or fractional `|5`, no sale clause | Nested consumer execution unobserved |
| No open receipt, valid primary source 26 | Fresh integer quote and Black Friday clause | Exact quantization execution owned by parent/architect |
| Sale active but actor/source ineligible | Ordinary fraction and no sale clause | Requires final actor fixture |
| No open receipt, invalid quote | Price unavailable, no numeric/source detail expansion | Source branch selection inspected |
| Valid open refund receipt | Payment recovery, saved paid amount at five decimals, no fresh purchase/source text | Positive-pointer recovery bypass now exists, receipt validity remains unchecked |
| Open pointer with absent paid field or invalid receipt | Currently selects recovery anyway | Requires shared validity and agreed malformed-pointer disposition |
| Prior recovery display followed by no open receipt | Four outputs reset, fresh helper recomputes amount and source | No stale receipt temp is used by the fresh YAML keys |

For a represented fractional quote such as 40.00008, the selector must show `40.00008` rather than `40.00` or `40`.
For a quote of 40, it must show `40`.
At PP equal to a valid positive quote, the reviewed comparison permits payment and hover selects yellow.
Just below the quote both reject and hover selects red, and just above both permit.
These are logical consequences of the inspected comparisons, not executed scenarios.
Do not claim a universal fixed-point precision or engine agreement from this review.
The receipt path records `cbrn_occupation_coverup_receipt_paid_@var:receipt_id` before refund handling, and recovery reads that saved amount rather than recomputing the ordinary/current discounted price.
Refund execution, repeat recovery, and native timing were not tested here.

## Prose-quality review

Vagueness: the two fresh-price explanations need the concrete resource and refund condition specified above.
Bloat: no material bloat found in the assigned short outputs.
Obvious explanation: the cost-scaling sentence adds a useful cause, and the refund sentence adds a material consequence, so neither should simply be deleted.
Repetition: the parallel explanations belong to two separately hovered actions, with no repeated explanation inside one tooltip.
Overcomplication: replace “rejected evidence destruction” with the direct conditional recommended above.
Style-rule repair: no em dash, semicolon, staged contrast, prompt fragment, implementation-history note, hidden route reveal, or attributed-quote violation found in these assigned values.
No prose was changed by the auditor, and no broader writing pass was performed.

## Documentation and MCP evidence

Used `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
The role-specific read-only instruction overrides their default patch capability.
No skill was modified.

`hoi4.reference_context` succeeded for localisation in workspace `mod_chaos_redux_ea3b2d67c2c0`, with both installed documentation and offline wiki coverage included and no `omittedSources`.
It returned no artifacts.
It identified the following pertinent sections, which were then read directly from their local files:

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:729-792` and the scripted-localisation/formatting rules at 656-705 and 188-214.
SHA-256/revision: `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
Temps remain available down the selected text/localisation chain, which supports these nested selectors.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443`.
SHA-256/revision: `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Caller-created temps retain nested helper updates and are unscoped.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:12-53,125-181`.
SHA-256: `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
Read bindable, contextual, and formatted localisation distinctions.
These sections do not independently prove legacy nested temporary-variable lifetime.
- Installed `documentation/loc_formatter_documentation.md:1-135`, revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`, and the opening localisation-object definitions in `documentation/loc_objects_documentation.md` were read.
- Installed `documentation/triggers_documentation.md:6442-6454` documents modulo temporary-variable use.
- Installed `common/scripted_localisation/00_scripted_localisation.txt:1-70` supplies the literal-key/default-branch precedent.
- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:311-329` supplies native base/blocked/tooltip selection semantics.

The connected catalog exposes reference context/search/read, source lookup, decision inspect, GUI inspect/render, and technology inspect/render/compare.
Exposure is not treated as service health.
This auditor's detailed reference read/search calls and source-lookup call did not return before observation was stopped, so their outcomes remain unresolved rather than failed.
No detailed MCP read or source lookup success is claimed for this auditor, despite the parent's separately reported successful reference use.
An initial decision inspection without scenarios returned exact argument error `MCP -32602: Decision inspection requires declared scenarios at scenarios`.
A corrected read-only inspection for `cbrn_seal_state`, scenario `cbrn_seal_no_source_exact_pp` (GER, closed flags, PP 40, Condemnation 0), also returned no result before observation was stopped.
This incomplete actor fixture was intended to inspect the route, and supplies no eligibility or boundary proof.

Useful artifact URIs: none returned by successful calls in this audit.
No decision cost-row raster, hover raster, overflow, clipping, wrapping, or visual alignment evidence was obtained.
The exposed decision inspection route is source/scenario evidence and is not a native visual render route.
The exposed GUI renderer requires a named GUI window, while this bounded assignment provides ordinary native decision consumers and no event-owned scripted GUI window.
No substitute GUI or render capability was invented.
Consumer visual review remains blocked/unresolved for the parent, and source review is not equivalent visual evidence.
No focus, event-popup, map, technology, doctrine, or weighted-AI surface was included in this seven-getter audit.
Separately, no standalone Technology Tree Viewer route was found in the connected catalog.
Record this as a session/package capability gap, with standalone installation/launch availability unverified, independently of the exposed technology tools.

## Review identities and remaining work

Latest inspected SHA-256 identities:

- Scripted localisation: `dcc7cfdc68a5c6ce4642c65431687997dd3313a864409acd09114bbaef6179e4`.
- English localisation: `8ab70017c6b7abe6b285c904ca513b860c0da09c8188dbe9df3cfd9508f16c99`.
- Occupation triggers at final recheck: `0870948142a6fce77236eed3c79775553c8fb8e01d0f4415026a34ea2cdadbcf`.
The prior inspected revision was `3b3e6248f31454a68aa3d06a6daf336023dd15dd6cc5ee5c791329930befd0da`, before the positive-pointer recovery OR branches were added.
- Occupation effects: `1012cd4de8c883a1e20e7ee8f62cf64290890592329d4c86c00808d7350ce943`.
- Coverup recovery effects: `28b585ec4e28d2c96c7cc6299aa7982b82d775f842c7e7c5a7333153c819877e`.

Completed: bounded source/localisation linkage, nested storage review, quote-source review, receipt amount review, and manual prose review with key-level recommendations.
Changed files: this handoff only.
Changed gameplay keys/getters: none.
Dynamic localisation added or fixed by this auditor: none.
Dynamic tokens and all existing wording were preserved because implementation files were read-only.
Meaningful checks were limited to exact English output coverage, getter consumer search, authoritative helper call tracing, and pending/fresh branch inspection.
No engine execution, local emulation, boundary test suite, or native visual validation ran.
Those checks remain unresolved, alongside the final architect predicate/recovery contract and malformed-pointer wording disposition.
No implementation simplifications were made by this auditor.
This is an actionable bounded audit, not a completion claim for Event 026 or the integrated purchase/refund system.
