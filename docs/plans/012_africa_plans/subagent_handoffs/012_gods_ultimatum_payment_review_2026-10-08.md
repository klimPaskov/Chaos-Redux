# Event 012 extraordinary ultimatum payment review

Disposition: completed bounded read-only source review; native transaction semantics remain `unresolved`.
Only this handoff was written.
No gameplay, Git, game launch, probability audit, repricing, fallback, or separate helper specification was performed.
The assignment explicitly excludes AI balance and the parent's separate response-phase implementation.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.

## Conclusion and recommendation

**No concrete payment defect is proved by the inspected source and available references.**
The actual decision ID is `gods_of_africa_ultimatum_pay_settlement`, in `gods_of_africa_participant_category`; there is no inspected `gods_of_africa_ultimatum_pay` decision.
The owner uses a real native `send_equipment`, checks affordability again at execution, charges political power once, and rejects an expired or stale-authority participant.
The absence of measured receipt handling does not prove simulated transfer or establish that an affordable native shipment actually fails.

The proved source fact is **unconditional post-send success**: after the guarded PP effects and native send, the owner always calls `gods_of_africa_resolve_final_ultimatum`.
If a valid invocation's native send delivered zero or less than 3,000, the current code would still clear the ultimatum and record `ultimatum_met`.
That is conditional source-path reasoning, not a demonstrated failing transaction.
This review has no native observation or documented stock-pool mismatch proving that such an outcome occurs after the actual affordability check passes.
The stock check includes a 500-rifle reserve and is intended to exclude ordinary insufficient-stock partial sending.
Do not promote missing instrumentation or the conditional case to a proved accepted-contract defect.

**Recommended choice: preserve the existing transaction and keep the specific native semantics unresolved.**
Retain the 150 PP plus 3,000 rifle prices, 500-rifle reserve, 60-day deadline, punishment owner and history kind 21.
No receipt redesign, new helper specification, repricing, equipment-family restriction, contribution credit or broader audit is justified by the collected evidence alone.
If actual native transaction evidence later contradicts this contract, a narrow corrective owner review can follow that demonstrated result.
No alternative implementation is proposed here.

## Accepted contract and actual path

The accepted full spec is `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md`, not the separate generic `012_africa_specs` package.
Its Tier V sequence at lines 851-876, especially 874, provides the extraordinary-settlement opportunity.
Its balance invariants at lines 1582-1588 require real material payments and capacity with a protected reserve.
The concrete acceptance basis is L26 in `docs\plans\012_africa_plans\agent_decisions_2026-10-04.md:343-357`, especially line 354: 60 days, 150 PP plus 3,000 infantry equipment, 25 Wrath relief and history kind 21; the lead chose to implement the promised ultimatum rather than remove it.
Current documentation at `docs\events\012_africa\gods_of_africa.md:184` matches those terms.
The October 7 repair handoff at line 20 explicitly leaves transaction internals unresolved and rejects the inference that native shipment is simulated.

The code path is:

- Decision `common\decisions\012_africa_gods_decisions.txt:166-201` in the final observed shared source calls the settlement effect at line 188; the initial MCP-indexed version was lines 147-181, call at 168.
- `common\scripted_triggers\012_africa_gods_punishment_triggers.txt:88-93` checks a current participant, pending ultimatum, stored due day and `global.num_days < due_day`.
- The same trigger file at lines 104-109 checks PP at least 150 and archetype infantry stock at least 3,000 + 500.
The temporary requirement is created and consumed within this trigger, so no returned temporary output is required.
- `common\scripted_effects\012_africa_gods_punishment_effects.txt:568-581` repeats both gates, subtracts 150 PP from the participant, adds 150 to the host, requests the 3,000-rifle native transfer and resolves.
- The resolver at lines 520-529 clears pending/due-day state, removes the mission, requests 25 Wrath reduction through the existing floor-aware owner, and records `ultimatum_met`.
It does not award Council voice, ordinary compliance, voluntary aid or a contribution quantity.
- The `.618` event at `events\012_africa_gods_of_africa.txt:480-494` is an acknowledgement notice with one cosmetic option; it is not a second payment caller.

The decision's `custom_cost_trigger` and `custom_cost_text` display the two prices and gate selection; `cost = 0` provides no additional native PP charge.
The current row also has `ai_hint_pp_cost = @GODS_OF_AFRICA_ULTIMATUM_PP_COST` at line 181, added by another writer during this review.
The cited wiki defines this as an AI budgeting hint, not an additional debit.
No AI weight or hint correctness claim is made here.
The final row was reread after that shared edit; its transaction gates, zero cost and effect call retain the inspected behavior.

## Scenario reasoning

These are source-path deductions under the documented trigger meanings, not executed native scenarios or a simulated transfer test.

| Scenario | Source result and limit |
| --- | --- |
| Current authority, before deadline, exactly 150 PP and 3,500 eligible rifles | Preflight admits; participant is charged 150 PP once and the native effect requests 3,000 rifles. A full send leaves 500. Exact native movement and receiver gain are unobserved. |
| 149 PP, or fewer than 3,500 rifles | Affordability rejects before either debit. The effect repeats this check, so a stale visible row alone does not authorize spending. |
| No pending flag, missing due day, or current day equals/exceeds due day | Current-ultimatum gate rejects; no payment effects run. Existing refusal/expiry remains with its original owner. |
| Replayed call after successful resolution | Pending flag and due day have been cleared; second call rejects, so no demonstrated double PP charge or repeated history entry. |
| Host pointer, host generation, origin or authority epoch changes | The participant binding chain rejects stale identities before payment; no demonstrated transfer to a replacement authority. Permission also checks host physical return and transfer/terminal flags. |
| Only captured, licensed, foreign-produced, mixed-tier or mod-defined descendants of `infantry_equipment` supply the required stock | Gate and send use the same archetype. Neither source adds an own-producer filter. Whether both native operations include exactly the same variants/producers is not specified by the retrieved references and is unobserved. |
| Equipment belongs to a different archetype | It is outside the existing rifle price; lack of support is not a defect or authorization to broaden compatible payment families. |
| Affordable invocation but native donor loss/host gain are zero | Conditional risk: current PP effects and ultimatum resolution still execute. This review does not establish a reachable affordable zero-send case. |
| Affordable invocation but send is partial or donor loss differs from host gain | Conditional risk: full settlement success still follows the attempted send; no remainder, retry or native mismatch proof is stored. Documentation permits partial delivery when insufficient stock, but current preflight is designed to exclude that condition. |

Authority proof is in `012_africa_gods_triggers.txt:12-19,160-184`, `012_africa_gods_epoch_binding_triggers.txt:4-18`, and `012_africa_gods_recovery_triggers.txt:5-50`.
The normal participant binding validates the live registry/generation before writing host/origin/epoch identities in `012_africa_gods_epoch_binding_effects.txt:5-21`.
Existing participant cleanup and authority cancellation call `gods_of_africa_clear_final_ultimatum` in `012_africa_gods_effects.txt:4243,4529`; the local clear at punishment effects lines 607-612 removes the live flag/day/mission.
The payment invocation contains no delayed callback or wait between debit, send and resolution.
That is source ordering, not a guarantee of native atomicity or callback timing.

## Precedents and their limits

Vanilla `common\scripted_effects\USA_scripted_effects.txt:403-416`, `USA_foreign_support_pilots_effect`, checks archetype stock with `has_equipment` and sends it using `equipment = small_plane_airframe`, `amount`, and `target = ROOT`.
This supports the existing `equipment =` syntax and stock-check/send structure; its enclosing country iterator is not proposed for reuse.
The older SAF precedent uses `type =` at `SAF_german_coup_effects.txt:83-87`; it does not invalidate the installed USA `equipment =` precedent.
The wiki has a `type =` table entry but an `equipment =` example at lines 2285-2292; that inconsistency is not a demonstrated syntax defect in this settlement.

Council precedent: `012_africa_gods_council_effects.txt:59-103` freezes its separate pledge terms, performs native sending, uses fresh completion evidence, reduces the balance by measured donor loss, and bounds host reserve credit by measured receiver gain.
Council is voluntary aid and intentionally writes contribution records.
Ordinary tribute precedent: `012_africa_gods_effects.txt:2607-2620` and contribution effects lines 1259-1265,1283-1292 surround their native send with measured receipts.
The native reader at contribution effects lines 10-15 reads `num_equipment@infantry_equipment` with caller-initialized temporary output.
However, `gods_of_africa_complete_material_transfer` at lines 720-836 automatically calls `gods_of_africa_record_paid_contribution` at line 820.
Passing voluntary=false does not make that recorder neutral punitive-payment accounting; begin also selects ordinary-demand identities at lines 403-408.
These are potential precedents only, not evidence that the ultimatum transaction ran, a requirement to retrofit it, or authorization to grant punitive settlement voluntary-aid credit.
No helper map, migration, constants, cleanup or receipt design is introduced by this review.

## Reference evidence

Live `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read` and `hoi4.source_lookup` routes were verified from exposed schemas and called successfully.
Decision context had both required source kinds, `omittedSources=[]`, `missing=[]`; generic context entries were not treated as read rules.
Targeted sections below were read through revision-bound MCP references, except the explicitly marked direct supplementary reads.
`script_doc` is unavailable in the configured reference index; installed `game_doc` and offline `wiki` evidence are available.

| Citation | Revision SHA-256 | Bearing on conclusion |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md:6550-6558`, send_equipment | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Country scope; sends specified amount to target. No full argument schema, producer rules, return status or atomicity guarantee. |
| Same installed file, add_political_power, 1854-1862 | Same revision | Native country PP mutation; sparse prose does not prove exact host gain at native caps. |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:2254`; direct example supplement 2285-2292 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Removes donor equipment, may deliver less when stock insufficient; amount supports variables and equipment may be archetype. |
| Installed `documentation\triggers_documentation.md:3835-3843`, has_equipment | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | Checks stored equipment in country; producer/variant pool not described. |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md:1516`, has_equipment | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` | Equipment threshold supports variable and comparison operator. |
| Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:268-277,284-336` | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` | Selection runs complete_effect; custom costs do not debit; ai_hint_pp_cost only informs AI saving. |
| Installed `common\decisions\_documentation.md:1-22`, direct supplementary read | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` | Decision visible/available country scope and frame-refresh behavior. Exact custom-cost search in installed docs returned no section; wiki supplies that rule. |
| Installed `documentation\dynamic_variables_documentation.md:557-559` and offline Data structures:1615 | Installed `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`; wiki `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Typed num_equipment reader; wiki identifies stockpile. Same-tick visibility and foreign-origin coverage remain unproved. |
| Offline Data structures:263-269, direct global-target supplement 270-275 | Same wiki revision | Scope pointers and global reassignment/lifetime; no new global target is proposed. |
| Installed `documentation\script_concept_documentation.md:216-222`; `common\script_constants\documentation.md:1-34` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`; `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Constants are globally reusable; individual field support must be explicit. No send_equipment amount constant acceptance is proved by its sparse installed prose. |
| Installed USA_scripted_effects:403-416, MCP location plus direct source | `9da33cb6e469906d7c8353b88d3957945f35ae12d81e1134d294b78b14f76f75` | Native archetype capacity/send precedent with equipment key. Source-location index revision `2a3c080a629399d79a344a72d771a43495a6e91c3638ed0aa7e689cee4d4907d`. |

All installed paths above resolve beneath `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
All mod and offline-wiki paths resolve beneath the assigned `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\` root.
No Paradox web wiki was used.

## Source identities and validation limits

Exact-definition lookup initially returned decision and effect identities without overrides under workspace-index revision `c9d4ad9495d68317b0f9623ef38bb230dc83897a1c953269b8eec09446aa57bc`.
Definitions were complete; reference discovery was not complete (`referencesComplete=false`, global unresolved-reference count 20105), so it is not proof of every possible consumer.
The inspected direct decision/effect and `.618` callers were read separately.
Shared file edits shifted the decision row and added the AI hint; whole-file identity is therefore explicitly time-bound.

| Source | Observed SHA-256 |
| --- | --- |
| punishment effects | `1205d872a6a9ff6e911ff71e6431e413a33cd1a74174ef45cf9f38194259c261` |
| punishment triggers | `061487f76b4fc0581fc5acf2e36d6944d64d179405be3e38b68488a26856ff10` |
| decisions, first hash observation | `e808262b60c0ff34cfd6c0eac146fcb53f6ced3bb6d58bcc157799fe48720f93` |
| decisions, final row recheck | `ae732079d66e081b0b6a13fbbe411b42936722009652639106d42d2b2144bfb9` |
| gods triggers | `9db29e9384743ee26e476b69fb46e83ebe076e3475023917866de6f6dba2e2b2` |
| epoch binding triggers | `63ba5fa62d2ca8c2bd5562abde0cdf1c1cc53fd599f64efb8d36df4181e553e7` |
| recovery triggers | `c9f9073f3969b3c18a9a1d17048512a332723722ec5e509fbee85b583b01ecd1` |
| epoch binding effects | `00132b89309640cf9bfa0f4a86605eeb0b910b78b61cabf18c5c3c4a217a2908` |
| gods effects, observation before final decision recheck | `a8345ffd8135137f90e0e87da15067f16607a43578fe4e9f69d3a3abb7511092` |
| contribution effects | `bc06a98c1a2582e7fc2d54c6db73958273141e816de17ae13f1872a95fc749e6` |
| Council effects | `0b7db3b048c92bdf5fef8b482a6963558d0ca925db7f80bf4eba49e0558b1e05` |
| Gods constants | `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e` |
| Gods English localisation | `3efe9abb5a29c62cae79699857f21411240840f3e59749c1896ffc14963e2b65` |
| Gods event doc | `aab3798c634e596772fb844259ce1e761cf22d481095e0ba6ea4654dcbee4992` |
| Accepted Gods full spec | `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798` |
| October 4 acceptance record | `9ac6bfbf44a53ed81b2fab3b1bfd8b7da944c98805f134c2f182ae26268948b2` |

Meaningful checks performed: exact decision/effect/trigger reads; final payment-row recheck after shared edits; gate/debit/replay/authority scenario reasoning; accepted-price and localisation comparison; neutral-reader versus contribution-recorder separation; revision-bound wiki and installed documentation; native vanilla precedent; bounded MCP event inspect/render; one country-scope settlement-body script validation.

`hoi4.script_validate` returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, `parametersChecked=false` with checks only for syntax, command kind and declared scope.
It recognized native sending and PP mutation but left the send argument block unchecked, custom helpers unresolved and even `event_target:africa_host` unresolved despite the supplied country binding.
Documentation aggregate revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
This is not native argument or transaction proof.

The focused `.618` trace and options render used graph revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5` and returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`.
The render-data resource was retrieved and parsed: three nodes (notice, acknowledgement option, terminal), `complete=false`, selected unresolved list empty.
The focused analysis has zero indexed helpers and explicitly defers whole-workspace helper/lifecycle projections; it does not cover native settlement execution.
No graph comparison was required for this read-only review, and no PNG visual or engine execution claim is made.

Artifact references:

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea0ace33e65013a4316ef94a1913a3233bd795f840deb3450ca67038a6df51b2/04d47bee3939a5e775c05ab5191e3d63d42d1b51c03f921f7f06579bc6292b10/event-trace-db07bcddfa36.json`.
- Parsed render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/528596aea331a9860a000e0aeea2be10cb7824aa4de01e9ea66b3cdf4132e84d/a91546cb9c6b9898517a65e067a502f3ae6e76f3304efcd279b72fbc7e050fe4/event-options-db07bcddfa36.json`.
- Render manifest, not independently inspected: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e6216e93946bc3a0140730e7f1b691aa008b2f95182541af3985b6bce606d65/2593b28600f109ac284ea45fa370e8bd34969c678105ec0ea5f1e7e160929068/event-options-db07bcddfa36-manifest.json`.

Exact decision-inspector limitation: the exposed route first rejected `{mode:"inspect",id:"gods_of_africa_ultimatum_pay_settlement"}` because declared `scenarios` are required.
A corrected read-only request supplied one deliberately unbound scenario `{id:"ultimatum_native_context_unbound",actor:"ENG",state:{},closedFlags:false}`.
It produced no final observed result during repeated bounded waits; the observer execution was terminated while pending.
Its server-side outcome remains unknown, not proved failed; no scenario artifact or valid transaction result is claimed.
No broad probability job, helper-expansion job, whole-world source search, service modification or tool generator was used.

Missing native evidence remains explicit: exact 150-PP donor mutation and any native host cap behavior; 3,000-rifle donor loss and receiver gain at the reserve boundary; stock-pool agreement for captured/licensed/foreign-produced/mixed/custom infantry variants; acceptance of the `constant:` amount token; synchronous visibility of both stock readings; and a real zero/partial/mismatch case, if any, that passes the actual affordability predicate.
No save or native transaction observations were supplied, and game launch is prohibited by the assignment.
No executable transaction model was introduced because mocking the native result would not resolve that uncertainty.
No existing Council audit or measured receipt is treated as proof that this ultimatum path ran in game.

Only this report changed; helpers, call sites, constants, cleanup, prices, punishment, history and contribution accounting were not patched.
No simplification or fallback was adopted.
The parent receives the completed bounded review with no proved payment defect and the exact native uncertainties retained.
