# Gods response and punishment report audit

Disposition: unresolved pending parent fixes and MCP evidence.
This is the requested narrow read-only review of the working `.604`/`.605` report changes and integral equipment receipts on 2026-10-03.
Only this handoff was written, with no gameplay, localisation, spreadsheet, weight, or Git writes.
The parent continues mobile/artillery implementation, so the source identities below describe the inspected snapshot rather than a locked final change set.
Skills applied: `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-decisions-missions`.

## Must-fix findings

1. **High: population receipt and Deaths attribution use the wrong country on owner-driven punishment paths.**
   In `common/scripted_effects/012_africa_gods_effects.txt:2509`, the loss target is `ROOT`, and `:2513-2516` writes the applied flag, historical amount, and new report receipt through `ROOT`.
   The host event `events/012_africa_gods_of_africa.txt:118-123` calls the owner tick, whose participant loop at effects `:116-134` calls expiry and whose defiance review at `:140-153` calls punishment without rebinding ROOT.
   Thus the selected state belongs to the participant, but ROOT is the African host.
   The participant receipt initialized to zero at `:2285` can remain zero even after a positive state loss, and the host receives the receipt and wave flag instead.
   The shared helper passes the supplied country into Deaths accounting at `common/scripted_effects/chaosx_dynamic_effects.txt:693-699`, so this also misattributes the country ledger.
   Use the calling participant pointer consistently, preferably a captured event target, or verified `PREV` at state entry, for both the supplied loss country and the receipt/flag destination.
   Do not repair only the new copy line while leaving the target-country and idempotence flag on ROOT.
   Review owner-driven expiry and repeated defiance separately from participant-triggered refusal, where ROOT happens to be the participant.
   This is a source-demonstrated call-chain defect, not an observed engine result.

2. **Medium: integral equipment reports still show fractional-looking counts, and non-equipment receipts hide their payment unit.**
   `localisation/english/012_africa_gods_l_english.yml:29,31`, keys `gods_of_africa_response_partial_report` and `gods_of_africa_response_expired_report`, use unconditional `|1` and generic “units of” for every family.
   The corrected 55-aircraft payment therefore reads as 27.0 sent and 28.0 due, contrary to the integer-display rule in the events skill.
   For recognition, industrial repair, security access, emergency relief, and territory, the payment fallback at effects `:1817-1821` spends political power, so “units of recognition” or “units of the return of African soil” conceals what remains payable.
   Add family-aware amount/unit rendering using the existing snapshot family and values.
   Equipment uses `|0`, while genuinely fractional fuel or political-power values retain sufficient precision.
   Preserve all receipt values and do not globally round every family to integers.

3. **Medium: punishment leaves omit concrete consequences and expose helper terminology.**
   YML `:34-36`, keys `gods_of_africa_punishment_disruption_report`, `gods_of_africa_punishment_crisis_report`, and `gods_of_africa_punishment_ultimatum_report`, say only “limited disruption”, “a crisis”, and “an ultimatum”.
   The stat footer does not explain the possible resistance increase (`:2342-2346`), infrastructure damage (`:2360-2367`), or infrastructure and factory damage (`:2382-2393`).
   Give concise source-supported consequences and respect the `gods_of_africa_transport_secured` exemption and absence of an eligible state.
   A report must not assert that a building was damaged solely from the tier if no state was selected.
   YML `:38-39`, keys `gods_of_africa_punishment_catastrophe_report` and `gods_of_africa_punishment_catastrophe_no_wave_report`, use “call ... was accepted”, “population wave”, and “loss was applied”, which narrate the gateway/helper rather than the country's experience.
   A bounded proposed replacement for the positive leaf is “Africa has brought disaster upon us. Its attack killed [?gods_of_africa_punishment_report_population_loss|0] civilians.”
   For the zero-wave leaf, retain that the accepted disaster and the additional Gods civilian loss are different outcomes, without claiming the entire disaster caused no deaths.
   Proposed wording is not implemented or accepted final catalogue text.

4. **Low: report-helper documentation cites the wrong sprite-definition file.**
   `common/scripted_effects/012_africa_gods_report_effects.md` names `interface/012_africa.gfx` for the report sprites.
   The actual definitions are `interface/012_africa_event_pictures.gfx:15-16`, with `gfx/event_pictures/012_africa/report_event_012_africa_gods_response.dds` and `report_event_012_africa_gods_punishment.dds`.
   Correct the source-location claim.

## Branch and receipt agreement

| Surface | Source result |
| --- | --- |
| Full compliance | `:1858-1899` snapshots only after successful transfer, preserves the original family, records zero balance, then clears demand and fires `.604`. |
| Accepted substitute | `:1968-1989` temporarily replaces demand family/balance before the canonical full resolver snapshots the actual paid substitute. Failed transfer restores the original family/balance and publishes no new response. |
| Partial compliance | `:1904-1935` copies the paid amount before transfer cleanup, subtracts it, snapshots the residual, and leaves the contract/deadline running. |
| Refusal / expiry | `:2630-2655` / `:2682-2706` evaluate punishment, capture zero paid and outstanding balance, clear the demand, then fire `.604`. The closed-contract wording agrees with these branches. |
| Negotiation / defiance | No `.604` call in these handlers. They are not incorrectly selected as response leaves. `.605` can also result from repeated defiance, so its “Broken Demand” title is narrower than its actual dispatcher. |
| Punishment | `:2282-2285` captures the starting native stats and initializes this punishment's extra civilian loss to zero. `:2416` records the actual capability-limited tier, and `:2440-2445` stores after-minus-before deltas after defensive relief. |
| Catastrophe | Getter checks gateway rejection/missing result before positive-wave and no-wave alternatives. Gateway result is reset at `:2468`. Historic `last_population_wave` is not used to fabricate the current loss. The owner-path scope defect above remains blocking. |
| Cleanup | The new eight-field clear helper is called at enrollment `:314`, archive `:397`, and cancellation `:3152`. Ordinary demand cleanup `:2103-2129` preserves report receipts. |

The six-family equipment classifier contains land equipment, support equipment, mobile/artillery, armour, aircraft, and transport.
Full quote normalization at `:1278-1280` and partial normalization at `:1652-1654` use the existing modulo-one helper, so the source arithmetic gives 55 -> 27 paid + 28 remaining and 5 -> 2 paid + 3 remaining.
These are arithmetic/source checks, not measured stockpile transfers.
The report helper adds no population debit, disaster request, or Deaths registration.
It duplicates only the existing helper's numeric receipt.

These fields hold the latest response and latest punishment, not a separate historical record for every popup instance.
No frozen-old-popup claim is supported.
The helper documentation correctly states this limit.
Historical punishment tier/result fields survive the new eight-field clear helper.
Consequently the punishment getter alone can still select an old tier after cleanup, even though delta fields are absent.
Existing pending-flag/current-participant gates reduce ordinary popup exposure, so this is a bounded getter-hardening opportunity, not proof that a stale popup is delivered.
Use a dedicated report-valid predicate or field-presence guard if unknown-report rendering must be reliable after lifecycle reset, without deleting historical relationship data.

## Localisation and prose checklist

- Missing keys: none among all 29 selected getter leaves, comprising 15 family leaves and 14 response/punishment leaves, or the `.604`/`.605` title/description/options/tooltips.
- Duplicate keys: none in the assigned YML or for the inspected report/family keys across English localisation. The three getter names each have one source definition.
- Scripted localisation issues: no missing nested family getter, cyclic report reference, or incorrect spelling of `localization_key` found. Receipt-country scope and stale-tier fallback limits are detailed above.
- Numeric formatting: `|=+1` correctly combines sign, good/bad colouring, and one decimal. `|%=+1` also converts the 0-1 stability/war-support delta to percent. Installed documentation confirms `has_war_support`, not plain `war_support`, as the dynamic read.
- Encoding concerns: none identified in the inspected English file. Its bytes carry UTF-8 BOM. Console code-page failures during reference display were not source-encoding defects.
- Vagueness: the three normal punishment leaves and “Africa has judged its response” (`:30-31`) need concrete wording. “Judged its response” is an unclear subject/object phrase.
- Bloat and repetition: compliance/substitute leaves repeat acceptance and settlement after already stating fulfilment or delivery. This is small and suitable for a bounded parent edit.
- Obvious explanation: the response option tooltip `:20` repeats recording, and punishment option tooltip `:25` merely narrates acknowledgement. Neither changes contract state.
- Overcomplication: no overloaded sentence structure or long noun stack found in the assigned leaves. Family-neutral “units of” is the meaningful clarity problem.
- Style-rule repair: catastrophe leaves expose helper vocabulary. No em dash, semicolon, staged contrast, or sourced quotation was found in this bounded text set.
- Unknown leaves: short and neutral, with no invented outcome. `.605.d` nevertheless appends numeric fields even when its getter selects unknown, so blank-receipt rendering remains unverified.
- Dynamic opportunities: family-aware numeric units/precision, actual optional resistance/building-damage results, and a report-valid fallback. Do not publish hidden history, intent tiers, or future routes.
- Cross-surface mismatch: the sprite source citation is wrong. Workbook content was not reviewed or edited in this bounded task. Spreadsheet owner should receive final parent-approved wording for changed report keys if those passages are catalogued. No proposed wording here should be treated as final synchronisation input.
- Quotations and tokens: no attributed quotation inspected. All source tokens and formatting were left untouched.

## Evidence and coverage limits

This child has no callable `mcp__hoi4_agent_tools__hoi4_event_inspect`, `hoi4_event_render`, `hoi4_event_compare`, `hoi4_reference_context`, `hoi4_reference_search`, `hoi4_reference_read`, or `hoi4_source_lookup` in its tool inventory, and no tool-search route to load them.
The resource-template inventory exposes the `hoi4_agent_tools` artifact URI template, which does not establish domain-route availability or service health.
No event inspection/render request or timeout retry was possible here.
Parent metadata exposure, parent `.603` retries, and the supplied older menu error context are not this child's executed engine proof.
Correct follow-up event selectors are `{ kind: event, eventId: chaosx.nr12.604 }` and the equivalent `.605` selector, encoded according to the parent's live schema.
No helper-expansion, jobs, native tasks, game launch, log requests, or save speculation occurred.
There are no new artifact URIs from this child.
Standalone Technology Tree Viewer was checked separately against available tools/resources: none is exposed to this child, recorded as a viewer package/access gap, with installation and service health unresolved.
There is no in-scope technology tree, focus tree, map, or new scripted GUI ownership.
Popup wrapping, overflow, clipping, image fit, repeated-instance delivery, and native stock movement remain unverified.
Source-only review is not equivalent to MCP or live consumer evidence, and this handoff makes no full Gods completion claim.

Offline references read directly because reference routes were unavailable:

- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:184-214,656-689`, SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, variable formatting and recursive scripted localisation/first matching leaf.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:484-516,557-570`, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, variables, default scope, and receipt operations.
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:260`, SHA-256 `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, ROOT retains the original event recipient.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:439-441,743-747,785-787`, SHA-256 `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, actual native stat inputs.
- Installed `documentation\effects_documentation.md:4986-5007`, modulo operation, and vanilla `localisation\english\effects_l_english.yml:263` / `career_profile_more_customization_l_english.yml:25`, signed coloured formatter precedents.
- Read `common/scripted_effects/012_africa_gods_equipment_effects.md` and `012_africa_gods_report_effects.md` for the parent helper contracts and their full reference revisions. Their references are documentation claims where underlying native transfer sections were outside this report-focused review.

Inspected SHA-256 source identities:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_effects.txt` | `ed5855eafccb6655a54b8acecb56049a6182ec1ed1e824a75d6c62599c1b97a5` |
| `common/scripted_effects/012_africa_gods_report_effects.txt` | `0f3a23e4ae4e9fd8f2ef5dabcb6d02c0eea158695054eb21a52f30347a87dcb5` |
| `common/scripted_effects/012_africa_gods_report_effects.md` | `398c6292055043c4db2dc19f45de2840b30b7b056481bf396e3c27b1aae416bd` |
| `common/scripted_triggers/012_africa_gods_triggers.txt` | `b70b438cf6ad01e34690ad67f97ad3630940bee650d5962a1f84244796e747ed` |
| `common/scripted_localisation/012_africa_gods_scripted_localisation.txt` | `a4e7172cb1b0cc87c62dbb3f2ef3d9c234f5c416a9de3853bdaebc8f2cc8d4b7` |
| `localisation/english/012_africa_gods_l_english.yml` | `ac970b1205bf70cbaf971b077413214b1fdc67b6bece5bdb16a6bb36ca6b35a3` |

No gameplay simplification was made by this reviewer.
The review is deliberately bounded, with MCP/runtime/visual coverage blocked and parent fixes still required.

## Bounded parent-fix resolution, 2026-10-03

This section supersedes the four must-fix dispositions above for the re-read source snapshot.
All four previous findings are resolved in source, with no new must-fix identified in this bounded re-review.
Only this section was appended by the reviewer, with no gameplay, localisation, or Git writes.

| Previous finding | Resolution evidence |
| --- | --- |
| Population country/receipt scope | `012_africa_gods_effects.txt:2535` captures `gods_of_africa_population_wave_participant` before random-state entry. `:2541` supplies that target to the exact helper, and `:2545-2548` writes wave flag, historical amount, and new report loss to that same participant. There is no ROOT reference in this helper body. The shared Deaths-input contract therefore receives the participant even when the outer event ROOT is the host. |
| Receipt units and precision | Scripted localisation `:152-167` selects equipment/manpower whole counts, fuel/political power with three decimals, and steel-rights concession text. YML `:41-50` contains the corresponding real keys. Partial and expiry reports use these getters rather than generic fractional “units of”. |
| Missing local consequences and implementation wording | Punishment captures its participant at effects `:2286`. Resistance at `:2356-2365` stores only a positive measured after-minus-before change, with state `PREV.id` saved after entering the participant target. Infrastructure/factory receipts at `:2390-2392,2421-2424` are published only inside selected-state invocations. YML `:52-54` says “targeted”, without claiming measured building damage. Transport protection is copied at `:2293-2295` before preparation cleanup and selects its own consequence only for the relevant tiers. Catastrophe leaves `:38-39` remove gateway and population-helper terminology while preserving the distinction between disaster and additional civilian attack. |
| Incorrect sprite source citation | Report-helper documentation `:63` now names `interface/012_africa_event_pictures.gfx:15-16` and both actual DDS paths. |

The new local state receipts use an explicit participant target, and `PREV` at each setter is the selected state.
The population helper receives the participant for Deaths attribution and returns its existing actual-loss output to that participant's report field, without adding a second death registration or civilian debit.
Actual output propagation and native accounting remain runtime evidence limits rather than observed results.
The source state-name namespace follows existing `localisation/english/migration_l_english.yml:43` and Charter variable-name conventions.
Installed dynamic-variable documentation `:1145-1147`, SHA-256 `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, supports the state resistance read and points display.

`GetGodsOfAfricaPunishmentReportBody` at scripted localisation `:189-199` requires all three native delta fields before selecting the receipt body.
Lifecycle cleanup therefore selects only the unknown leaf rather than appending invented zero deltas to a historical tier.
`012_africa_gods_report_effects.txt:15-29` clears ten normal fields and four local-consequence flags, matching its updated documentation.
The title “Africa Answers” covers repeated defiance.
Refusal/expiry leaves now report remembered conduct rather than claiming Wrath increased even at its cap.
Full/substitute prose removes repeated acceptance wording, and the accepted substitute continues to describe the family captured during the successful transaction.
The latest-snapshot contract remains unchanged, with no per-popup historical archive claim.

Validation was limited to the fixes: manual country/state-scope trace, receipt publication/guard order, 45 distinct selected localisation leaves with no missing keys, no duplicate keys in the assigned English file, and exact ten-field/four-flag clear inventory.
No sourced quotation occurs in these changed leaves, and dynamic amounts, family getters, state names, and signed native delta formatters are retained.
Family 2 mobile/artillery implementation remains parent-owned and pending, outside this resolution claim.
Catalogue synchronisation, visual wrapping/clipping, native receipt output survival, stock movement, and repeated-popup delivery were not established by this source re-review.
No claim about the parent's current MCP availability is made.
Child inspect/render routes became exposed during this follow-up, which does not establish service health or completed inspection.
A narrow `.604` trace with the exact event selector, `maxNodes = 1`, `maxDepth = 1`, and `expandHelpers = false` returned no result during the bounded review window.
The waiting orchestration cell was stopped, with no server result, artifact URI, health/version finding, or confirmed server-side cancellation.
This was not a returned timeout diagnostic, so no timeout-retry result is claimed.
Rendering and `.605` MCP inspection remain unverified in this child review.

Re-read SHA-256 identities:

- Effects: `b3f52f8c6689dccacdc18ede8f43c7d292266c2d0bcf0e199449dcaa6d56453a`.
- Scripted localisation: `437584dfd24204bb4ab1c97d4580a963cbc0da4859cb5112d7a0db03eda06a57`.
- English localisation: `c80b00f0e2ebbdb1cd87230728b266c62dc40f16202724d05bfec22eed03ba8c`.
- Report effects: `01269095dc901feed089c42fd933e14d2480eb6d6c5c683d56b0a2934a84948c`.
- Report-helper documentation: `34e8c1ecca64ce340cc4938cc8b2bd3147ba42272ca46b546aea31de4b4c8107`.
