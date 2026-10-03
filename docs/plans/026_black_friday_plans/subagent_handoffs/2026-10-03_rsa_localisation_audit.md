# Event 026 RSA purchase localisation audit

Date: 2026-10-03.
Disposition: RSA-L01, RSA-L02, and the four bounded prose findings are implemented by the parent and verified in the source recheck below.
The original audit sections retain the baseline findings and proposals as historical evidence, not descriptions of the corrected source.
Native display evidence remains unresolved.
Authority: the parent's bounded read-only assignment and follow-up identifying invalid-quote and pending-order explanations.
Only this report was written.
No gameplay, localisation, scripted localisation, spreadsheet, export, or Git-index changes were made, and no game was launched.

## Scope and evidence identity

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Reviewed only the five assigned purchase actions in these source files, plus required skills and pertinent offline and installed references.
Source hashes were unchanged when checked again before writing this handoff.

| Relative source path | SHA-256 |
| --- | --- |
| `common\scripted_localisation\012_africa_rsa_purchase_localisation.txt` | `5CD0600E623396635C26F0E597E8D5767A6FFCCC5C26EC423EBF49F4C7404C23` |
| `localisation\english\012_africa_rsa_l_english.yml` | `955266AA98733D960F91DC3B8E32CB1EC2C864A734EAD095D416E6D63377CD42` |
| `common\decisions\012_africa_rsa_decisions.txt` | `5DD77C415A5E68E4353D82A5418B0AD8D0644C36A5AC01514656C6A81D96E740` |
| `common\scripted_triggers\012_africa_rsa_purchase_triggers.txt` | `EC3C1ADF78C811F6729B63CE4B0544D1DB00D04FE90F59E34F1F80A001431653` |

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions`.
No skill was created or updated.
Parent ownership and the explicit read-only assignment override default patch capability.

## Finding RSA-L01: invalid quotations still select ordinary-looking costs

Current disposition: implemented by the parent, verified in all 15 getters at the post-fix hashes below.
The following description records the pre-fix defect.

Priority: required display fix for all 15 action getters.
In `common\scripted_triggers\012_africa_rsa_purchase_triggers.txt:45-65`, failed active-source quotation marks `africa_rsa_purchase_quote_valid` zero, while `africa_rsa_component_quote` initially retains the ordinary amount.
`africa_rsa_quote_selected_purchase` ends with `always = yes`, so successful trigger evaluation is not proof of a valid quotation.
The action getters invoke that helper and select their cost keys without checking the validity output.
`africa_rsa_can_pay_selected_purchase` correctly rejects invalid quotation at line 120, but that rejection is hidden in both decision availability and custom-cost gates.
Each resource getter checks only whether the amount is affordable, so an unavailable purchase can show yellow ordinary amounts.
`GetAfricaRsaPurchaseSource` independently checks active Black Friday and the registered source, so an invalid quotation can also display a clause that appears to explain a valid discount.
This last case depends on the external quote helper failing while the source is active, which is a supported failure branch in the adapter, not a witnessed native UI result.

Affected getter families in `common\scripted_localisation\012_africa_rsa_purchase_localisation.txt`:

| Family | Normal / blocked / details definition starts | Selected key stem |
| --- | --- | --- |
| `GetAfricaRsaReliefCost` | 84 / 106 / 128 | `africa_rsa_relief_cost` |
| `GetAfricaRsaRegionalRequestCost` | 150 / 172 / 194 | `africa_rsa_regional_request_cost` |
| `GetAfricaRsaCitizenshipCost` | 216 / 238 / 260 | `africa_rsa_citizenship_cost` |
| `GetAfricaRsaSovereigntyCost` | 282 / 304 / 326 | `africa_rsa_sovereignty_guarantee_cost` |
| `GetAfricaRsaExileRecoveryCost` | 348 / 370 / 392 | `africa_rsa_exile_recovery_cost` |

Each family includes its base getter, `Blocked` getter, and `Details` getter.
Recommended parent change: preserve the existing caller initialization and fresh five-field quotation, then require `africa_rsa_purchase_quote_valid = constant:universal_cost_framework.one` before selecting any numeric cost key.
Use real literal fallback localisation keys, never an inline numeric string as `localization_key`.
An invalid quotation should select a concise unavailable status instead of numbers or `GetAfricaRsaPurchaseSource`.
Suggested new keys in `localisation\english\012_africa_rsa_l_english.yml`:

```yaml
africa_rsa_purchase_price_unavailable: "§RPrice unavailable§!"
africa_rsa_purchase_price_unavailable_tooltip: "This purchase is unavailable until its price is confirmed."
```

These are proposals, not installed wording.
No change to affordability, payment, rounding, or resource colours is requested.

## Finding RSA-L02: pending order blocks payment without an explanation

Current disposition: implemented by the parent, verified in all 15 getters at the post-fix hashes below.
The following description records the pre-fix defect.

Priority: required blocked-state explanation for the same 15 getters.
`common\scripted_triggers\012_africa_rsa_purchase_triggers.txt:119` rejects a caller with `africa_rsa_purchase_pending_receipt`.
None of the assigned action or resource getters checks that state, and none of the assigned cost keys explains it.
When all resources are affordable, the disabled decision can therefore retain yellow costs with no cost-related reason for its rejection.
Recommended parent change: numeric branches must also require no pending receipt, with a separate pending-order branch using real keys.
Give pending-order explanation precedence over the generic unavailable fallback when both conditions occur.
Do not expose the variable name, receipt identifier, helper names, or settlement internals.
Suggested new keys:

```yaml
africa_rsa_purchase_order_pending: "§ROrder pending§!"
africa_rsa_purchase_order_pending_tooltip: "Wait for your previous order to finish before placing another order."
```

For each getter, a bounded branch pattern is: existing initialization and quotation followed by valid-quote and no-pending requirements for the numeric key, then a pending-state text block, then the unavailable fallback.
Use the short keys in normal and blocked getters and the explanatory keys in details getters.
The first branch must still initialize outputs before helper calls, even when its selection fails.
Preserve resource-specific red colouring for valid quotes with an unaffordable component.
Neither fallback should append a Black Friday source clause or imply a confirmed discounted price.

## Price and formatting coverage

These are the exact normal, baseline, and evolved price expectations supplied by the parent.
The assigned trigger source selects the correct owner constant tokens and resource families, but constant definitions and the external discount helper are outside this audit's source scope.
The table is an acceptance matrix, not a claim that native values were observed or that external rounding code was independently audited.

| Action | Normal | Baseline | Evolved | Inline / full tooltip |
| --- | --- | --- | --- | --- |
| Relief | 35 PP, 20 CP, 5 trains, 150 support equipment | 18 PP, 10 CP, 3 trains, 75 support equipment | 9 PP, 5 CP, 2 trains, 38 support equipment | PP, CP, trains inline, all four in tooltip |
| Regional request | 15 PP | 8 PP | 4 PP | PP |
| Citizenship | 75 PP, 5% stability | 38 PP, 3% stability | 19 PP, 2% stability | PP and stability |
| Sovereignty | 40 PP, 10 CP | 20 PP, 5 CP | 10 PP, 3 CP | PP and CP |
| Exile recovery | 60 PP, 25 CP | 30 PP, 13 CP | 15 PP, 7 CP | PP and CP |

The parent's fixed stability quantum is 0.01.
YML lines 12-13 use `[?africa_rsa_purchase_stability_cost|%0]`, which converts fractional stability to percent with no decimals.
For the stated 0.05, 0.03, and 0.02 costs, the documented formatter yields 5%, 3%, and 2%.
Do not replace `%0` with `0`, `%%0`, or add a second percent sign.
The other four resource pairs use `|0`.
Normal and blocked action keys intentionally call the same per-resource getters, so a valid quote colours only the unaffordable amount red and leaves satisfied amounts yellow.
The icon is outside the red amount span, consistent with the parent's per-field colour requirement.
Icon registration and native icon expansion were not inspected in this bounded task.

## Temporary-variable and cross-call review

All 15 normal, blocked, and details getters initialize quote validity, all five ordinary fields, all five payable fields, and `africa_rsa_component_quote` before their action helper.
The selected-action helper initializes those fields again and quotes PP, CP, trains, support equipment, and stability on every call, including zero-valued unused resources.
It initializes ordinary outputs before calling `africa_rsa_prepare_purchase_costs` and initializes the component output before calling `africa_rsa_quote_purchase_component`.
The component helper initializes `black_friday_quote_final_cost` before invoking the external Black Friday quote helper.
Action wrappers set the action input before invoking the selected helper.
Resource getters set their resource-kind and amount inputs before invoking affordability.
No bounded-source output lifetime omission or cross-action stale-field path was found.
Nested resource getters consume the action quotation rather than selecting another action.
Do not remove the caller initialization merely because the callee also initializes fields.

Offline Localisation lines 729-791 explicitly permit temporary values computed in a text trigger to be used by its selected real localisation key and downstream keys.
Data structures line 440 separately warns that values first defined inside a scripted helper may not survive its return, while caller-defined values can be modified safely inside it.
These are distinct rules and the adapter observes both.

The parent reports that its independent source interpreter passed 214 checks, including conservative temporary-variable lifetime across all APIs and 45 actual normal/blocked/details text-trigger contexts.
That is parent-provided source-model evidence, not a test run by this subagent or native engine proof.
The reported pass does not remove RSA-L01 or RSA-L02, because valid output lifetime and truthful blocked-state explanation are separate checks.

## Key and source-clause audit

- Missing local purchase keys: none found in the assigned English file.
- Duplicate localisation keys: none found within that file.
- Duplicate `defined_text` names: none found in the assigned purchase file.
- Unresolved RSA purchase getters: none found among the purchase getter calls in the assigned YML.
- Inline numeric `localization_key` defect: absent in the assigned purchase getter file, whose selected outputs are literal real keys.
- External key: `black_friday.cost_source.line` is selected literally at scripted-localisation line 79 and lies outside the assigned YML.
  The parent explicitly states that it exists, so it is not classified as a missing key.
  Its definition and the recently fixed Black Friday constant getters were not independently read under this scope.
- Source selection: `GetAfricaRsaPurchaseSource` requires Black Friday active and the registered source query active, then returns `black_friday.cost_source.line`, otherwise the existing empty `africa_rsa_purchase_source_none` key.
  The numeric source-ID definition is external and the parent supplies ID 26.
- Encoding concerns: none in the assigned English file, which has a UTF-8 BOM and decodes strictly as UTF-8.
- Repository-wide duplicate and override checks were not performed because the parent restricted source inspection to four files.

## Prose findings inside current cost wording

Current disposition: the four recommended sentence removals are implemented by the parent and verified at the post-fix English-file hash below.
The following findings and proposal block record the baseline wording.

No prose was changed.
These findings concern only the current prices and their explanations at YML lines 125, 131, 137, 143, and 149.
Decision descriptions and other narrative wording are outside the requested prose pass.

| Category | Exact keys and finding | Recommended parent action |
| --- | --- | --- |
| Vagueness | `africa_rsa_citizenship_cost_tooltip_value`: “These resources enact” gives resources agency instead of stating the player's action. | Remove the redundant explanatory sentence while retaining all tokens. |
| Bloat | `africa_rsa_relief_cost_tooltip_value`: “These resources are consumed when the corridor opens” explains expenditure already represented by the costs. | Keep all four resource entries and source clause, remove this sentence unless the parent needs to distinguish payment timing. |
| Obvious explanation | `africa_rsa_sovereignty_guarantee_cost_tooltip_value` says payment issues the guarantee already named by the action. | Remove that sentence. |
| Repetition | `africa_rsa_exile_recovery_cost_tooltip_value` repeats reconstitution and the oversight clause from the action description. | Remove that sentence. |
| Overcomplication | No additional multi-clause or inflated-language defect found in the five bounded cost explanations. | No wording expansion needed. |
| Style-rule repair | No em dash, sentence semicolon, quotation, staged contrast formula, or implementation-history claim found in these five price explanations. | Keep the two new blocked-state explanations plain and concise. |

`africa_rsa_regional_request_cost_tooltip_value` usefully distinguishes paying for a request from receiving support.
Its sentence is acceptable within this narrow task.
Optional dynamic-text opportunity: replace “the selected government” with `[FROM.GetNameDef]` only after confirming the targeted decision tooltip context retains FROM.
That context exists in the installed decision documentation, but native expansion remains unproven here.
Do not add acceptance, rejection, refund, or timing promises without the parent's payment-source evidence.

Proposed final simplifications for parent review, preserving every existing cost getter and the source getter:

```yaml
africa_rsa_relief_cost_tooltip_value: "[GetAfricaRsaPurchasePpValue]  [GetAfricaRsaPurchaseCpValue]  [GetAfricaRsaPurchaseTrainsValue]\n[GetAfricaRsaPurchaseSupportValue]\n[GetAfricaRsaPurchaseSource]"
africa_rsa_citizenship_cost_tooltip_value: "[GetAfricaRsaPurchasePpValue]  [GetAfricaRsaPurchaseStabilityValue]\n[GetAfricaRsaPurchaseSource]"
africa_rsa_sovereignty_guarantee_cost_tooltip_value: "[GetAfricaRsaPurchasePpValue]  [GetAfricaRsaPurchaseCpValue]\n[GetAfricaRsaPurchaseSource]"
africa_rsa_exile_recovery_cost_tooltip_value: "[GetAfricaRsaPurchasePpValue]  [GetAfricaRsaPurchaseCpValue]\n[GetAfricaRsaPurchaseSource]"
```

These remain proposals and may produce a trailing blank line when the source is absent.
If the parent adopts them, preserve all four relief costs and do not allow the source clause in invalid or pending fallbacks.
No sourced or attributed quotation occurs in the reviewed purchase wording.
All existing dynamic tokens, colour spans, and source names were left untouched.

## Cross-surface and spreadsheet notes

The five decision `custom_cost_text` keys match the five action families and their English entry points.
The same affordability helpers are used in both `available` and `custom_cost_trigger`, with hidden cost gates.
The ordinary PP AI saving hints in the decision file match the parent's stated ordinary PP prices, but AI scoring and balance were not audited.
The main mismatch is valid-looking cost text versus invalid/pending payment rejection, described in RSA-L01 and RSA-L02.
No spreadsheet or export was read, so catalog agreement is unresolved, not confirmed.
There are no changed final localisation keys to hand to `chaosx_spreadsheet_doc_worker`.
The four proposed explanation removals and four proposed status keys above are not catalog source wording until the parent accepts and installs them.

## References actually read

Offline paths below are relative to the Windows workspace above.
Hashes identify the local source revisions, since MCP did not return revision-bound citations.

| Reference | Lines read relevant to this audit | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 184-215 and 729-791 | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 424-449, especially 440-442 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 7482-7512, temporary-variable assignment | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 125-159, localisation scope context and legacy-context limits | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | 1-35, availability and actor/target contexts | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation_SPR_loc.txt` | 1-28, vanilla real-key selection precedent | `0997CE02F60303F6D23278DA44AA3C6F52E420458A11B3F6FA566099A2F742F9` |

The installed decision documentation section read does not document custom-cost suffix expansion.
No claim about native `_blocked` or `_tooltip` consumption is based on that section.

## MCP and native evidence limits

Connected tool metadata exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and `hoi4.decision_inspect`.
Live `hoi4.reference_context` was called for localisation with a limit of four and a temporary-variable/percent-formatting question, but did not return within the audit window.
Its orchestration cell was terminated after the read-only source review.
No returned source revisions, missing/omitted-source inventory, or artifact URIs were available.
Reference search/read/source lookup were not represented as successful retrievals, and pertinent local references were read directly.

The first decision-inspect attempt returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.decision_inspect: Decision inspection requires declared scenarios at scenarios`.
A second attempt supplied `id = africa_rsa_protect_civilian_corridor`, actor SAF, scenario `rsa_relief_normal_display_audit`, and PP/CP state 35/20.
It did not return within the audit window and its orchestration cell was terminated.
That minimal scenario was not complete relief eligibility or equipment evidence, and no successful scenario result is claimed.
Service health and server version were not established by tool exposure or prevalidation.
No helper-expansion, job, task-negotiation, or rewrite route was used.

Standalone Technology Tree Viewer: no such callable viewer was present in the connected tool-name inventory, separately from the exposed `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` routes.
Record this as a connected-package viewer gap, not proof that an unrelated desktop package is absent.
No technology source was in scope and no technology route was invoked.

No new dedicated GUI was introduced, and the parent explicitly excluded MCP GUI work.
No GUI, focus, event-chain, map, or technology surface was broadened into this purchase audit.
Native value expansion, nested getter expansion, suffix-key consumption, actual icon display, clipping, wrapping, overflow, and hovered source placement remain unproven.
Source-only review and the parent's interpreter checks do not substitute for those missing native observations.

## Validation and handoff status

Completed task-specific checks: traced each of the five price entry points through normal/blocked/details getters, verified all 15 caller initialization contexts, inspected selected-helper zeroing of unused resources and nested output lifetimes, checked real local key/getter resolution, reviewed percent formatting and per-resource colour selection, compared inline relief costs with the four-resource full tooltip, and examined invalid/pending gate-to-display consistency.
The parent independently reports 214 passing interpreter checks and 45 real text-trigger contexts.
No additional source interpreter was written or run by this subagent.

Skipped or blocked validation: MCP reference retrieval and declared decision inspection did not return, native text/UI expansion was not observed, external constant/discount/affordability/payment source was outside the assigned four files, repository-wide key overrides and workbook alignment were outside scope, and GUI rendering was explicitly excluded.
The report is a completed bounded source audit with two actionable display findings, not completion proof for the adapter or Event 026.
No source simplification or fallback was implemented.
The parent owns the 15-getter patch, proposed-key approval, post-patch validation, and any catalog alignment.
No separate design-depth plan was needed.

## Parent-fix recheck, 2026-10-03

Authority: the parent's explicit bounded recheck of the same four owned sources, with only this report writable and no game launch.
The parent accepted and applied the invalid-quote and pending-order changes, corrected caller initialization indentation, and removed the four recommended redundant sentences.
Only this audit report was modified by the subagent during the recheck.
No additional MCP was requested or used, as directed for this localisation-only pass.

| Relative source path | Post-fix SHA-256 |
| --- | --- |
| `common\scripted_localisation\012_africa_rsa_purchase_localisation.txt` | `4245FE74CF31A6442B536C03BA821C6E4AA95F73A7AA575D816EBEAF57FF3F20` |
| `localisation\english\012_africa_rsa_l_english.yml` | `F65FE6330D1BBC0B5AAA4EE6511B21E2926B91EA0B56516C9D0A8D2188F7B133` |
| `common\decisions\012_africa_rsa_decisions.txt` | `5DD77C415A5E68E4353D82A5418B0AD8D0644C36A5AC01514656C6A81D96E740` |
| `common\scripted_triggers\012_africa_rsa_purchase_triggers.txt` | `EC3C1ADF78C811F6729B63CE4B0544D1DB00D04FE90F59E34F1F80A001431653` |

Decision and purchase-trigger hashes are unchanged from the baseline, so the five-field quotation and payment gates reviewed above retain their source identity.

| Finding | Disposition and post-fix evidence |
| --- | --- |
| RSA-L01 | Implemented. Every normal, blocked, and details getter initializes caller outputs, invokes its fresh quote, then checks quote validity equals one before selecting a numeric key. The last text block selects the real unavailable key. |
| RSA-L02 | Implemented. Every numeric branch also requires no pending receipt. The second text block tests pending receipt and selects the real pending key, taking precedence over unavailable when both conditions occur. Details getters select the explanatory `_details` key. |
| Vagueness | Implemented. `africa_rsa_citizenship_cost_tooltip_value` at YML line 141 no longer says “These resources enact”. |
| Bloat | Implemented. `africa_rsa_relief_cost_tooltip_value` at line 129 no longer explains that resources are consumed, and retains all four resource getters. |
| Obvious explanation | Implemented. `africa_rsa_sovereignty_guarantee_cost_tooltip_value` at line 147 no longer narrates issuing the guarantee. |
| Repetition | Implemented. `africa_rsa_exile_recovery_cost_tooltip_value` at line 153 no longer repeats reconstitution and oversight. |

Post-fix getter-name lines for normal / blocked / details are relief 85 / 114 / 143, regional request 172 / 201 / 230, citizenship 259 / 288 / 317, sovereignty 346 / 375 / 404, and exile recovery 433 / 462 / 491.
All 15 retain their existing quote-valid, five ordinary, five payable, and component-output initialization before the helper, now indented with three tabs inside `text.trigger`.
The resource-specific affordability getters remain the numeric display path for valid, nonpending quotes.
Invalid and pending branches select no cost amount and no source clause.

The four installed English keys at lines 4-7 are:

```yaml
africa_rsa_purchase_quote_unavailable: "§RPrice unavailable§!"
africa_rsa_purchase_quote_unavailable_details: "§RPrice unavailable§!"
africa_rsa_purchase_order_pending: "§ROrder pending§!"
africa_rsa_purchase_order_pending_details: "§ROrder pending§!\nWait for your previous order to finish before placing another order."
```

The generic unavailable hover is acceptable for the parent's requested generic fallback.
The pending hover gives the exact requested instruction without leaking receipt, helper, source-ID, or variable identifiers.
All four are real local keys and contain no numeric getter or cost-source call.
No local selected-key or duplicate-key defect was found in the corrected files.
The only selected key external to the assigned YML remains the parent-confirmed `black_friday.cost_source.line`.

The four simplified tooltips match the proposed dynamic-token sequences retained in the baseline report.
`africa_rsa_regional_request_cost_tooltip_value` at line 135 retains “The fee submits the request to the selected government.”
No costs, dynamic resource tokens, percent formatter, or source getter were removed from valid cost text.
No sourced quotation was present or changed in this bounded wording set.
No new prose issue was found in the changed price/status wording.

Validation performed by this subagent: inspected the corrected getter branch pattern and English values, then checked all 15 getter bodies for complete caller initialization before quotation, validity and no-pending gates after quotation, correctly ordered pending/unavailable branches, and the short versus details key selection.
All 15 matched that source contract.
Local key resolution and duplicate checks also covered the new fallback keys.
No native API implementation or source interpreter was introduced or executed by this subagent.

Parent test status: the earlier 214 passing checks used native API mocks.
The parent states that 75 fallback contexts are being added, giving an expected total of 289.
No completed 289-check passing result was supplied for this recheck, so that total is recorded as expected rather than passed.
Mocked API/source-model checks do not establish native engine execution or actual UI expansion.

Remaining limits: native getter and suffix-key expansion, temporary-value behavior in the live engine, displayed icons, hovered fallback selection, clipping, wrapping, overflow, and source placement remain unproven.
External constant, discount, affordability, and payment definitions remain outside the four-source scope.
Workbook agreement and repository-wide overrides remain unaudited.
The earlier MCP and viewer-package limits remain historical evidence and were not retested.
An empty source getter may leave a trailing line break in a valid full tooltip, whose native layout was not observed.
No further source fix or unresolved wording decision was identified in this recheck.
The bounded source findings are closed as implemented, while adapter runtime completion and the expected 289-check result remain with the parent.

## Final bounded requirement-key addition, 2026-10-03

Authority: the parent's final request to include three real requirement keys, their named consumers, refreshed decision/English hashes, and supplied validation results.
Only this report was updated.
The event read was restricted to the named `chaosx.nr12.1202` option-A requirement wrapper at `events\012_africa_rsa.txt:42-68`, without broadening into event-chain, AI, or gameplay review.
No additional MCP, source writes, Git writes, or game launch occurred.

| Key | English definition and exact wording | Verified consumer |
| --- | --- | --- |
| `africa_rsa_support_response_available_tt` | Line 4: “The Coalition must still be fighting and seeking a distinct regional supporter.” | `events\012_africa_rsa.txt:53-55`, option `chaosx.nr12.1202.a`, custom tooltip wrapping `africa_rsa_pending_support_response_is_valid = yes`. |
| `africa_rsa_current_host_required_tt` | Line 5: “This country must lead the African unification campaign.” | `common\decisions\012_africa_rsa_decisions.txt:118-120`, citizenship availability, custom tooltip wrapping `africa_is_current_host = yes`. |
| `africa_rsa_exile_custodian_required_tt` | Line 6: “The exiled Continental Court must be held by an independent, uncapitulated country that controls its capital and has inherited the Coalition's defeated mandate.” | `common\decisions\012_africa_rsa_decisions.txt:208-210`, exile recovery availability, custom tooltip wrapping `africa_rsa_exile_recovery_can_be_completed = yes`. |

All three keys are used and resolved, each with exactly one definition in the assigned English file.
Their wording provides concrete requirements without exposing the predicate identifiers.
The host and exile wrappers retain the exact availability predicate calls inspected in the original decision source, with the separate purchase affordability gates still present.
The support-response predicate's implementation is outside this narrow localisation addition, so its complete state semantics remain parent-owned.
No new wording defect was identified in these three bounded requirement strings.

| Source | Final-addition SHA-256 |
| --- | --- |
| `localisation\english\012_africa_rsa_l_english.yml` | `DBE357D5F22B510FF80C8E4ACDAE7FC604B0E3874D70DFD33616898F167EC95E` |
| `common\decisions\012_africa_rsa_decisions.txt` | `0F5CFC6369BE6A42C5C0705C318352B9C70951DFDC7C6244BE9172DD1D15F884` |
| `common\scripted_localisation\012_africa_rsa_purchase_localisation.txt` | `4245FE74CF31A6442B536C03BA821C6E4AA95F73A7AA575D816EBEAF57FF3F20` |
| `common\scripted_triggers\012_africa_rsa_purchase_triggers.txt` | `EC3C1ADF78C811F6729B63CE4B0544D1DB00D04FE90F59E34F1F80A001431653` |
| `events\012_africa_rsa.txt`, narrow consumer evidence | `89D5165760C2B0505D50265BE01720FBA546BD6F62C45D7082323CAF58CE325E` |

The purchase-localisation and purchase-trigger hashes remain identical to the prior source recheck, preserving all 15 corrected action getters and their quoted-cost lifetime evidence.
The parent states that the separate pending P1 repair changes source effects unrelated to cost text, which were not inspected by this subagent.

Updated parent-provided validation: 295 owner tests plus 30 further tests passed, superseding the earlier expected 289-check count.
The parent also reports raw baseline byte identity verified between commit `f9f057` and `402837`.
These results were supplied by the parent, not independently executed or compared by this subagent.
The known native API mocks establish source-model behavior only, and none of these results establish native UI or engine execution.
RSA-L01, RSA-L02, and the four prose findings remain implemented with no further bounded localisation fix identified.
Native display, external predicate semantics, external helper/payment behavior, and catalog/override limits remain as recorded above.
