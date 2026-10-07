# Council localisation review, 2026-10-07

Disposition: source review completed; the parent applied recommendations 1–5 in the Council localisation integration.
This is a bounded source review, not a Council implementation or native presentation completion claim.
Only this handoff was written.
No gameplay, localisation, spreadsheet, asset, Git, or game-launch operation was performed.

## Verdict

The Council getters, English key coverage, frozen quote selection, reserve requirement, partial balance, zero retry, and speech exclusion agree at the inspected source level.
Two definite wording defects remain in `gods_of_africa_council_pledge_cost_tooltip`: a forbidden sentence semicolon and an unsupported claim that sent supplies remain in Africa.
Its cost hover also omits the outgoing numeric amount, and the deferred category status leaves the blocking obligations vague.
These were recommended parent fixes, subsequently applied by the parent; this reviewer made no localisation edit.

## Scope and evidence

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Paths below are relative to that root unless an installed-game path is named.
Read `AGENTS.md` and pertinent sections of `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md`.
No skill was changed.

Inspected sources:

- `common\scripted_localisation\012_africa_gods_council_scripted_localisation.txt`, all three getters.
- `localisation\english\012_africa_gods_l_english.yml:204-227`, the outer participant description at line 255, and the existing base-description keys at lines 687-688.
- `common\scripted_localisation\012_africa_gods_scripted_localisation.txt:969-973`, outer category base selection.
- `localisation\english\012_africa_gods_recovery_l_english.yml:14`, existence of the recovery base-description dependency only.
- `common\decisions\012_africa_gods_decisions.txt:214-295`, Council choices, custom costs, requirements, and effect tooltip calls.
- `common\decisions\categories\012_africa_gods_categories.txt:10-29`, participant category consumer and lack of attached scripted GUI.
- `common\scripted_triggers\012_africa_gods_council_triggers.txt`, current terms, phase, accounting, retry, and speech replacement.
- `common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt:46-75`, Council opening and inclusive affordability.
- `common\scripted_effects\012_africa_gods_council_effects.txt`, freeze, native shipment, consumed receipt, bounded receiver reserve, retry, completion, and cleanup.
- `common\scripted_effects\012_africa_gods_focus_payoff_effects.txt:55-76`, public pledge delegation and 25 PP speech debit.
- `common\scripted_effects\012_africa_gods_contribution_effects.txt:354-395,473-475,522-552,749-815`, integral request proof, source floor, consumed donor payment, and independent receiver accounting.
- `common\scripted_effects\012_africa_gods_equipment_effects.txt:8-12`, existing whole-equipment flooring helper for reference.
- `common\script_constants\012_africa_gods_constants.txt:39,598-607`, seven-day retry and 1000/500/25 values.
- `common\scripted_effects\012_africa_gods_council_effects.md` and `common\scripted_effects\012_africa_gods_contribution_effects.md`, the actual Council and shared contribution API contracts.

The prompt's API reference resolves to those helper markdown files headed “API”, rather than a separate Council `API.md` file.
The Council API explicitly adopts L3 donor-loss credit and limits Africa's reserve to measured receiver gain.
Other Gods UI, events, focuses, technologies, maps, and AI balance were outside this review.

## Specific fixes and prose review

All recommendations in this section target `localisation\english\012_africa_gods_l_english.yml`.
Keep the existing inline row keys and their one-icon, one-amount display unchanged.

1. **Meaning and style, line 220, `gods_of_africa_council_pledge_cost_tooltip`.**
   Current ending: “A short shipment leaves a balance; an empty one earns no credit. Supplies already sent remain in Africa if the relationship ends.”
   The semicolon violates the event prose rules.
   “Remain in Africa” promises recipient possession despite credit being based on donor loss.
   The hover names the reserve numerically but calls the outgoing amount only “the unpaid part”.
   Recommended full wording: `Send £infantry_equipment_text_icon §Y[GetGodsOfAfricaCouncilPledgeAmount]§! toward our pledge and keep £infantry_equipment_text_icon §Y[GetGodsOfAfricaCouncilPledgeReserve]§! in reserve. Only rifles that leave our stocks reduce the balance, and an empty shipment earns no credit. Rifles sent are not refunded if the relationship ends.`
   This keeps payment and reserve explicit in the full hover, preserves both getters and existing formatting/icon tokens, and replaces an arrival claim with the actual no-refund rule.
   Two icon/amount pairs in the full hover do not change the one-pair inline row limit.

2. **Vagueness, line 215, `gods_of_africa_council_deferred_status`.**
   Current: `\n\nThe Council choices wait while we settle our outstanding obligations.`
   Recommended: `\n\nResolve our tribute response, negotiations, reconciliation or ultimatum before answering the Council.`
   The explicit list matches the four response-phase blockers without adding timers, amounts, or public metrics.

3. **Obvious explanation, line 226, `gods_of_africa_council_speech_cost_tooltip`.**
   Current: “Political capital spent on the speech.”
   This repeats the cost label without explaining the alternative choice.
   Recommended: `We may speak instead of sending rifles only if no part of the pledge has been paid and our earlier shipments are accounted for.`
   The existing row remains the sole numeric PP quote.
   This states the speech-switch rule without exposing native receipt internals.

4. **Bloat and repetition, line 206, `gods_of_africa_council_pledge_effect_tt`.**
   The existing three sentences correctly limit payment to stock loss and voice/history to full payment.
   Once the cost hover carries payment accounting, the effect tooltip can concentrate on the final consequence.
   Recommended optional reduction: `Only a fully paid pledge earns our voice at the Final Council and a place in the world order's record.`
   This retains the established world-order consequence and does not imply arrival.
   If applied, the amount getter remains in the inline row, stock requirement, and recommended full cost hover.

5. **Vagueness, line 222, `gods_of_africa_council_speech_desc`.**
   “Spend our standing” is an abstract description of spending political power.
   Optional clearer wording: `Argue for Africa and its partners at the Final Council before the continent's settlement.`
   The row and requirement continue to display the existing 25 PP price.

The pledge title and description, speech title and effect, stock requirements, retry requirement, open requirement, and speech obligation requirement communicate their bounded purpose without a necessary rewrite.
`gods_of_africa_council_pledge_obligation_tt` correctly states both no partial pledge and clear earlier shipment accounting.
No excessive subordinate clauses, noun stacks, staged contrasts, prompt fragments, hidden route revelations, implementation-history text, or staccato chains were found in these Council passages.
The one forbidden semicolon is the definite style-rule repair above.
No broad cleanup of the ordinary base category descriptions is proposed.

## Key, formatting, and encoding audit

- Missing key list: empty for all six Council getter outputs, all Council decision name/description/requirement/effect/cost references, and both native cost suffix families.
- Duplicate key list: empty for the inspected Council keys, outer category key, and shared accounted-shipment requirement when searched across English localisation files.
- Scripted localisation issue list: no broken literal key target, wrong getter name, recursive Council reference, or format-code leak found.
- Amount targets: `gods_of_africa_council_pledge_remaining_amount` and `gods_of_africa_council_pledge_new_amount`.
- Reserve targets: `gods_of_africa_council_pledge_frozen_reserve` and `gods_of_africa_council_pledge_new_reserve`.
- Status targets: `gods_of_africa_council_deferred_status` and `gods_of_africa_council_no_status`.
- The outer `gods_of_africa_participant_category_desc` concatenates `[GetGodsOfAfricaVictorCategoryDesc][GetGodsOfAfricaCouncilPhaseText]`.
  Its recovery, victor, and ordinary base-description dependencies exist, including the recovery key in the separate recovery English file.
- The amount and reserve leaf keys are plain `[?value|0]` strings.
  They contain no nested colour reset, so wrapping the amount getter in `§Y...§!` or `§R...§!` has no conflicting colour scope at source level.
- Each of the four inline cost variants contains exactly one existing texticon and one dynamic amount.
  The infantry token has whitespace before colour formatting.
  The speech token follows the closed amount colour span.
- The inspected English Council file has UTF-8 BOM bytes `EF BB BF` and decodes as UTF-8.
  The new scripted localisation file contains neither `§` nor `£`.
  No encoding concern was found for this owned surface.
- Dynamic text opportunities: include the existing amount getter in the full pledge cost hover as recommended above.
  Do not add a new price cache, receipt metric, recalculation, image, or status number.

Existing texticons were confirmed in installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\texticons.gfx:261-265,2014-2018`: `GFX_pol_power` and `GFX_infantry_equipment_text_icon`.
The decisions retain `GFX_decision_012_africa_gods_fulfill_demand` and `GFX_decision_012_africa_gods_public_pardon`.
Their native appearance was not rendered by this review.

## Bounded source cases

These are source deductions and arithmetic checks, not executed HOI4 scenarios.

| Case | Selected amount / reserve | Source result |
| --- | --- | --- |
| No current terms, accounting clear | 1000 / 500 | Fresh price requires at least 1500 rifles and freezes those terms before sending. |
| Current terms, 250 unpaid | 250 / frozen 500 | Stock gate and native request use the same 250, with an inclusive 750-rifle floor. No reprice to 1000. Speech is blocked. |
| Current terms, 1000 unpaid | 1000 / frozen 500 | An uncharged quote can switch to speech when accounting is clear and PP is at least 25. |
| Current terms, zero unpaid | 0 / frozen 500 | Getter selects zero, never the new-price fallback. Positive-balance preflight blocks another send. Completion clears terms and sets voice, hiding both choices. |
| Full measured donor loss of 1000 | Balance becomes zero | Full pledge publishes Council voice, one aid-history record, and world history. Receiver reserve increases only by bounded actual receiver gain. |
| Donor loss of 750 from a 1000 pledge | Balance becomes 250 | No final voice/history. The next quote retains 250 plus the frozen reserve. |
| Donor loss of 250 from a 1000 pledge | Balance becomes 750 | No final voice/history. Payment is credited once from the consumed measured receipt. |
| Zero measured donor loss | Balance stays 1000 | No material credit or final voice/history. Pledge retry is seven days. Clear accounting permits the speech alternative without waiting for that material retry. |
| Stale or absent terms, accounting clear | Fresh constants | Old frozen fields are rejected by the same current-context predicate used by display and affordability. A fresh pledge reinitializes terms, and speech may replace the uncharged quote. |
| Unknown accounting, current/stale/absent terms | Getter can still show the applicable quote | Both actions fail their accounting preflight. Displayed affordability colour is not a payment permission. |
| Demand, negotiations, reconciliation, or ultimatum active | Qualitative outer-category status | Both choices are deferred by the same phase predicate. The Council status appends to the selected base description. Existing clocks are not changed. |

After successful completion the cleared getters would fall back to 1000 if queried independently, but the Council voice closes both decision rows.
This is not a visible zero-to-1000 reprice in the inspected source.
Whether a native hover persists across that transition remains a parent presentation check.

Arithmetic checks covered 1499/1500/1501 rifles for the fresh quote, 749/750/751 for a 250 balance, and 24/25/26 PP for speech.
The predicates are inclusive at 1500, 750, and 25 respectively.
The numeric leaf formatter has no SI abbreviation and selects zero decimal places, so 0, 250, and 1000 preserve their integer quantity in the source model.
Thousands punctuation is a native formatting detail, not verified here.
The Council adds no flooring/repricing pass between getter and debit.
Integral Council constants and the shared non-fractional request proof align with whole rifle amounts.
The exact native stock readers and native integer deltas remain runtime evidence gaps.

## Cross-surface and quotation notes

The Council API says that supplies remain sent without an inferred refund or successor delivery.
The current cost hover's “remain in Africa” is stronger and contradicts that accounting distinction.
The rest of the inspected Council price, reserve, retry, replacement, and full-payment consequence text agrees with the source/API contract.
No event catalog workbook or export-only CSV was read or edited, so catalog parity is unverified rather than reported as matching.
If the spreadsheet owner mirrors these Council passages, pass the recommended key-level wording above after parent acceptance, especially `gods_of_africa_council_pledge_cost_tooltip`, `gods_of_africa_council_deferred_status`, and `gods_of_africa_council_speech_cost_tooltip`.
There is no newly accepted final localisation wording from this read-only review.

No sourced or attributed quotation occurs on the inspected Council choice/status surface.
No quotation or dynamic token was changed.
Recommended replacements preserve gameplay meaning and use the existing getters, formatting codes, icon names, price, reserve, and retry contract.

## MCP references and validation limits

Live `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` were exposed and returned successful read-only results for workspace `mod_chaos_redux_ea3b2d67c2c0`.
This establishes the success of these calls only, not general service health or native consumer behavior.
No omitted required source kind was reported by the localisation context.
Search-result limits were followed with the relevant targeted section reads.

Read reference citations:

- Offline `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:184-215,656-705`, variable formatting and first-matching scripted localisation branches, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:284-336`, native custom cost base/blocked/tooltip keys and manual debit, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md:216-222`, scoped-variable `constant:` support, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- Installed `documentation\loc_formatter_documentation.md`, revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`: MCP read returned only heading lines 1-2, which did not establish numeric or nested-getter behavior. The local formatter file was also read and its named formatter examples were not treated as numeric-getter proof.
- Installed vanilla precedent `common\decisions\CHL.txt:3163-3177` was read directly for infantry-equipment custom cost, stock gate, and hidden/manual payment structure. It is a cost-pattern precedent, not a Council measurement precedent.
- Live source lookup read `gods_of_africa_council_pledge_is_affordable`, `mod:common/scripted_triggers/012_africa_gods_focus_payoff_triggers.txt:56-71`, index revision `cd102f9f86ec3abd026d444d2b7cfa83b0e8b0239c229188c4557204a287fb47`, one unshadowed definition.

No artifact URI was returned by these calls.
A separate tool-catalog check found technology inspect/render/compare routes but no standalone Technology Tree Viewer entry.
Standalone viewer availability is therefore unverified, with a package/exposure gap in this session, not a claim that technology routes are absent or healthy.
No technology surface was audited.

Meaningful validation performed: Council getter/decision reference coverage, English duplicate search restricted to owned keys, nested-category dependency recovery across English files, colour/token composition review, exact quote/debit/floor tracing, and full/partial/zero/stale/accounting-hold source-case review.
The initial single-file category-dependency check did not find the recovery base key, which was then located in the separate recovery English file.
It is not a missing-key defect.

Skipped: MCP GUI window inspection/rendering, native cost-row and hover appearance, clipping/wrapping evidence, native stock-delta execution, and game launch.
The parent explicitly excluded the Gods GUI audit and owns MCP/native validation gaps.
The ordinary participant category has no standalone attached scripted-GUI definition, so no substitute GUI or invented clipping evidence was produced.
No visual-fit verdict is made.

## Inspected source identities

SHA-256 identities bind this review to the inspected shared-tree bytes and do not assert that other agents will leave them unchanged.

| Source | SHA-256 |
| --- | --- |
| `localisation\english\012_africa_gods_l_english.yml` | `bee48661e4b9d40c8fc436571ccce7cb19fdc5b697cfb2dbb5c8c7ab8e40cc5a` |
| `common\scripted_localisation\012_africa_gods_council_scripted_localisation.txt` | `6b5d53f731a15e77a9fd89d0c2cc4fb98dd9483309a37a6826c6024050d2ce0b` |
| `common\scripted_triggers\012_africa_gods_council_triggers.txt` | `1c9266025c6f7b92e728ed35d9663256a020ac99ebae0a076c210e2aa82e0218` |
| `common\scripted_effects\012_africa_gods_council_effects.txt` | `0b7db3b048c92bdf5fef8b482a6963558d0ca925db7f80bf4eba49e0558b1e05` |
| `common\scripted_effects\012_africa_gods_council_effects.md` | `bbc0ddec9317af29eeaf5f2cdee87b0c61446390d6daf84b804466efb6a53bf2` |
| `common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt` | `23d5bfdf4e762b9dd390e5029d5168c7c7714f4922882aea0310d0c4aee31f23` |
| `common\scripted_effects\012_africa_gods_focus_payoff_effects.txt` | `26fa6867fb7a75a14e58f10660653fe5fd73cc8c7650ae8ffb0b64a935213e2f` |
| `common\decisions\012_africa_gods_decisions.txt` | `b39073b4370a8f7508ddc7902a6d9f4e5907942375313257fd063268a60fc6e8` |
| `common\script_constants\012_africa_gods_constants.txt` | `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e` |

## Parent follow-up

Apply the two definite tooltip wording repairs and review the concrete hover/status recommendations.
Keep the accounting distinction intact: donor loss pays the pledge, measured receiver gain funds Africa's reserve.
Parent MCP/native evidence must settle actual cost-row formatting, tooltip fit, and stock changes.
No gameplay design change or additional expansion plan is requested.
