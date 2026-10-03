# Event 012 Gods Post-Mobile AI Eligibility and Named-Scenario Probability Audit

Audit date: 2026-10-03. Disposition: **incomplete; source eligibility review completed, mandatory current MCP probability analysis blocked**.

This is a read-only continuation for the Gods participant decision response surface after typed truck and artillery integration. The user owns Gods completion and the parent owns integration, implementation, and every balance target. Per the parent status supplied for this task, full mobile integration remains pending parent review and commit.

No gameplay source, indexes, spreadsheets, Git state, or HOI4 process were touched. This handoff is the only file written by this audit. No numeric AI balance target was selected.

## MCP route and retained evidence

The initial tool declaration snapshot listed the probability inspect, evaluate, sweep, compare, and render schemas, including the decision_ai_will_do adapter. The inspect source selector was declared as unknown. I started with the required source-bound read-only request:

    hoi4.probability_inspect({
      source: { path: "common/decisions/012_africa_gods_decisions.txt" },
      refresh: true
    })

The call returned the exact error: “MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model”.

I retried the narrower decision adapter request with adapter = decision_ai_will_do and the same source. The wrapper returned: “TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function”. A follow-up tool inventory showed the probability and reference functions absent from the callable list. This establishes a model-route availability blocker, not a diagnosis of MCP server health.

The initial inspect declaration exposed a generic candidatePool field, but no actual participant-specific decision or phase-pool selector could be verified. The narrower retry failed before route-level schema validation, so I did not guess a selector or submit an incomplete pool.

The live service version, health, and client task negotiation were not verified. No job, helper expansion, native task, undocumented route, or alternate probability engine was used. No current inspect artifact, MCP source revision, candidate-pool hash, scenario hash, analysis ID, comparison ID, render URI, or continuation URI exists.

The prior 2026-10-03 probability handoff contains two older file-wide inspect artifacts. They are retained here as historical inventory evidence only; neither contains the current participant response analysis or a usable saved scenario result.

| Prior artifact | Revision | Source hash | Artifact URI | Current use |
| --- | --- | --- | --- | --- |
| 2026-09-25 file-wide decision inventory | cb808894b33a51fb05d6cf7d5d6cf37359ebd45403586b7a505779e7a14dae25 | 94b21c86205c16af5243748d08e52bdf9584a0069fab23c4ad2bb02e3746f74b | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b3ff62526399ee9d929a528ec02adf8a880f6ffcd4d0dc9e4e1049e00847d89/249f9333cf6cc219fdfe1290f6d4351b7043cf71fd880a1870ca91b1b3404d26/probability-inspect-94b21c86205c.json | Stale 36-candidate inventory; not a response analysis |
| 2026-09-26 refreshed file-wide decision inventory | 8b8752b7c0dcc5128addc5410f28ebde4e84b45bb2d36bd62a75ba45de0bf497 | 713a8151187b0c43bd119a69a7cb36f20524e39932d0815c4059a9f9202ab364 | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/561edaa3efd8861da97f5c03f8644efc5f76cef4fbccff1e13430b937b1aba3d/75ed9786078df7957ccde1d74274dfa389a0e7253a9e5c1515459fb084afbe83/probability-inspect-713a8151187b.json | Stale 36-candidate inventory; not a response analysis |

The prior response evaluations returned INTERNAL_ERROR and produced no analysis ID. The older six-scenario label RESP-COOPERATIVE-HARDSHIP is not silently reused; this handoff preserves the current requested ID RESP-HARDSHIP. No old scenario hash or analysis ID was returned.

Because the current inspect could not execute, probability_evaluate, probability_sweep, probability_compare, and probability_render were not callable for a valid evidence pass. No comparison was fabricated from the unchanged decision file, no current file was compared with itself, and no prior inspect artifact was treated as a before-analysis result. Simulation was not run because no uncertain-input distribution was declared. Sequence analysis was not run because this is not a declared custom weighted pool with a complete manifest, cadence, and transitions.

This task concerns the participant decision score surface only. I did not duplicate the parent’s pending .606 event trace or render calls.

## Current source snapshot

Hashes below are local SHA-256 values, not MCP source revisions. The current decisions file hash matches the prior 2026-10-03 baseline exactly. The eligibility helpers changed after that baseline.

| Exact source | Audited identifiers or role | Current local SHA-256 |
| --- | --- | --- |
| common\decisions\012_africa_gods_decisions.txt, lines 120-426 | Ten participant response decisions; visibility, availability, and ai_will_do | 230F9F22136CDA7A6625641EF45E4D14666B846457E2C466656824D2B0D3F8B6 |
| common\scripted_triggers\012_africa_gods_triggers.txt, lines 25-35, 214-233, 282-290, 312-377, 381-497, 504-515, 965-1019 | Active host, current demand, family/type validity, full, partial, substitute, and defiance gates | 7250742B4BC2392203A24F819B16F2646FD7D086766D4E15FF9CBAB5B074AF26 |
| common\scripted_triggers\012_africa_gods_equipment_triggers.txt, lines 79-145 | Mobile subtype validator and matching native stock/reserve capacity | CD464C44BC7687BE7C2DECDC131B3819FEE539E129E20507D7FB77826187ED7D |
| common\scripted_effects\012_africa_gods_equipment_effects.txt, lines 93-219 | Separate host need profiles, typed quote selection, and native sender | 4D0E522BB32E20C1A0E5708C4B2813C7A7D50B87F86938275A25C9D7ADD2414C |
| common\scripted_effects\012_africa_gods_mobile_contract_effects.txt, lines 6-23 | Preparation quote cleanup and payment subtype binder | 249BAE4063918989934B30EDA61AD06C50CC5659B38BA3C1D24B29FCCBD00BD2 |
| common\scripted_effects\012_africa_gods_effects.txt, lines 1145-1168, 1428-1438, 1762-1774, 2064-2070, 2233-2285, 3617-3659 | Selected type, immutable demand type, substitute type, cleanup, and generic first-valid-slot dispatch | 7DEF8A688E56DD54571CBCA0356F3D5AD487D9BBF4A95E9F07BE465B59BB26F8 |
| common\script_constants\012_africa_gods_constants.txt, lines 149 and 514-531 | Family 2; trucks subtype 1; artillery subtype 2; shared reserve and shipment tuning | 53E01EE0705A641ED2D66410AE7FE42A9F1C1A5D70DC85DF6FB14193F687FE11 |

The decision file’s unchanged hash confirms that its base and modifier clauses did not change since the prior source snapshot. It does not establish unchanged effective scores: existing modifiers ask whether the current demand can be paid, and that gate now reaches the typed mobile capacity checks. A truck or artillery subtype and its matching stock/reserve state can therefore change which unchanged score modifier applies.

## Typed mobile eligibility source trace

The existing mobile/artillery family is family 2. Its immutable subtype is either trucks = 1 or artillery = 2. Missing, zero, and invalid subtype values have no truck default.

The host’s truck and artillery needs are stored and refreshed separately. The quote helper selects artillery first when there is positive artillery need and matching artillery capacity; it falls back to trucks only when there is positive truck need and matching truck capacity. The subtype branches read motorized_equipment or artillery_equipment independently and do not pool the inventories.

Each host need is calculated independently as floor(max(0, max(matching army reinforcement shortfall, matching unlocked route-stock floor) minus matching host stock)).

For the participant, gods_of_africa_mobile_capacity_is_sufficient reads the selected subtype’s native stock, army target, and fielded army equipment. It converts the thousand-unit army measures with the shared units_per_thousand constant, computes the reinforcement deficit, retains the greater of the subtype reserve floor and the operating reserve plus deficit, clamps spare stock at zero, floors whole equipment, and passes only when typed spare is at least the required amount. The requirement must be nonnegative and integral. This is the source formula, not an evaluated result for a named participant.

The current full-payment path uses gods_of_africa_current_demand_can_be_paid and gods_of_africa_participant_has_capacity_for_family. The current-contract gate checks the active host, generation, participant demand, host-war exclusion, a valid immutable family/type, and deadline. The family-2 capacity branch requires the payment subtype and passes it into the mobile capacity trigger. Demand selection and contract creation copy the selected subtype into the participant’s payment fields and immutable demand_mobile_type before the response decisions are exposed.

The partial path, gods_of_africa_partial_payment_is_affordable, requires a current contract, present positive partial amount, partial amount strictly below remaining balance, satisfied cooldown, and matching family-specific capacity. For family 2 it copies the frozen demand subtype and partial capacity requirement into the same typed capacity helper.

The substitute path, gods_of_africa_substitute_offer_is_affordable, requires the typed family and subtype, positive offer amount, and matching capacity. When the original demand is also family 2, the offered subtype must equal the original frozen subtype. Negotiation slot validity is separate, and the shared submission path rechecks live affordability before debit.

The source therefore preserves subtype identity through full, partial, and substitute eligibility, subject to the source inputs being populated as intended. No current MCP run confirmed engine evaluation, candidate presence, or participant-level eligibility.

The completed helper handoff’s deterministic source model reported the following cases: artillery-only need with a truck-only sender yields no selected subtype, amount 0, and ceiling 0; healthy host stock covering need yields no quote; a source quote of 11 permits the described partial payment of 5 and leaves 6. The current equipment-effects source hash matches that helper handoff. These are bounded source-model results, not HOI4 MCP results and not decision AI results. They do not bind or prove any named probability scenario.

The parent’s mobile integration audit records its earlier need-scaling and cleanup findings as resolved in the follow-up. The mobile tribute handoff records the parent-owned typed contract and native transfer design. Those handoffs do not constitute the pending final parent integration review or commit.

## Candidate pools and phase boundaries

The ten named response IDs do not form one normalized ten-way race.

| Source phase | Named participant decisions | Pool status |
| --- | --- | --- |
| Active demand, negotiation closed | gods_of_africa_comply_demand; gods_of_africa_partial_compliance; gods_of_africa_negotiate_demand; gods_of_africa_refuse_demand; gods_of_africa_permanent_defiance | Source-phase list only; current active entries depend on their visibility and availability gates |
| Negotiation open | gods_of_africa_substitute_demand; gods_of_africa_substitute_demand_slot_1; gods_of_africa_substitute_demand_slot_2; gods_of_africa_substitute_demand_slot_3; gods_of_africa_return_to_demand | Source-phase list only; generic and slot entries depend on current frozen slot validity |
| No active demand, defiance available | gods_of_africa_permanent_defiance | Kept as its own state; not normalized with the active-demand or negotiation pool |

These are source-derived pools for the ten named participant response decisions, not MCP-certified complete decision-category pools. Other decisions in the active category, the participant’s actual country scope, host binding, current flags and variables, and any external selection factors were not resolved by the unavailable adapter. No ten-ID normalization or click probability is reported.

## Requested named scenarios

The scenario IDs are preserved exactly as supplied. A name alone does not define a country, host, phase, type, variable state, or external factor.

| Scenario ID | Source pool mapping | Candidate-pool completeness | External factors and typed state | Classification |
| --- | --- | --- | --- | --- |
| RESP-COOPERATIVE-AFFORDABLE | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No participant or africa_host binding, current demand phase, family/subtype, stock, target, fielded amount, flags, Wrath, or AI factor was bound | Unresolved |
| RESP-HARDSHIP | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No participant or africa_host binding, current demand phase, family/subtype, stock, target, fielded amount, remaining balance, cooldown, flags, Wrath, or AI factor was bound | Unresolved |
| RESP-GAMBLER-WEAK-AFRICA | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No participant strength, host identity/state, current demand, family/subtype, stocks, flags, Wrath, or AI factor was bound | Unresolved |
| RESP-OCCUPIER | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No occupier actor, host binding, war state, demand phase, family/subtype, stocks, flags, Wrath, or AI factor was bound | Unresolved |
| RESP-LOYAL-ALLY-EMERGENCY | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No alliance/ally state, participant, host, emergency demand, family/subtype, stocks, flags, Wrath, or AI factor was bound | Unresolved |
| RESP-ABUSIVE-AFRICA | Direct, negotiation, and no-demand defiance phases remain separately available for binding | Incomplete for analyzer use; no current category pool hash | No offender flag, Wrath, actor/host, current demand phase, family/subtype, stock, or AI factor was bound | Unresolved |

The common unbound inputs also include active host generation, current day and deadline, demand amount and remaining balance, payment and capacity requirements, substitute slot state, host validity, participant war status, and other simultaneously available decisions. The adapter did not return an accepted requirement schema, so no hypothetical typed participant/host fixtures or candidate overrides were invented. No scenarioSet or scenario hash was submitted.

## Source score traces and AI risks

These are source-only ai_will_do traces. They are classified as score-only. They are not probability shares, click chances, or analyzer rankings. The offline AI reference distinguishes ai_will_do score races from ai_chance probability-proportional sampling.

| Decision | Base and modifiers in the unchanged decision source | Classification |
| --- | --- | --- |
| gods_of_africa_comply_demand | Base 100; factor 0 when gods_of_africa_current_demand_can_be_paid is false; availability separately requires current full capacity | Score-only |
| gods_of_africa_partial_compliance | Base 15; factor 0.25 when the full demand is payable; factor 1.5 otherwise; availability separately requires partial amount, remaining-balance, cooldown, and typed capacity checks | Score-only |
| gods_of_africa_negotiate_demand | Base 20; factor 2 when full demand cannot be paid; factor 0.5 when Wrath exceeds the vengeful threshold | Score-only |
| gods_of_africa_substitute_demand | Base 10; factor 2 when full demand cannot be paid; factor 0.5 when Wrath exceeds the vengeful threshold | Score-only |
| gods_of_africa_substitute_demand_slot_1 | Base 10; factor 2 when full demand cannot be paid | Score-only |
| gods_of_africa_substitute_demand_slot_2 | Base 9; factor 2 when full demand cannot be paid | Score-only |
| gods_of_africa_substitute_demand_slot_3 | Base 8; factor 2 when full demand cannot be paid | Score-only |
| gods_of_africa_return_to_demand | Flat base 5 when the current contract is valid | Score-only |
| gods_of_africa_refuse_demand | Base 5; factor 3 when full demand cannot be paid; factor 0.5 when it can | Score-only |
| gods_of_africa_permanent_defiance | Base 5; factor 4 for an offender; factor 3 at or above hostile Wrath; factor 2 during an active demand; factor 0 while reconciliation is pending | Score-only |

A previously recorded conditional source comparison remains: with offender status, hostile-or-higher Wrath, and an active demand, permanent defiance’s raw source score reaches 120 while comply’s base is 100 when payable. The defiance decision’s comment says defiance remains rarer than ordinary responses. This is a possible source/comment inconsistency requiring owner intent, not evidence that defiance wins or a probability estimate.

A second source risk remains in negotiation. The generic substitute decision dispatches to the first valid slot, so it can produce the same slot-1 outcome while slot 1 is also a separately scored candidate. Their base scores are both 10; the generic route also has a Wrath modifier that the slot-specific route lacks. This can duplicate the route to the same outcome and may create pressure against later slots. No MCP ranking or sequence established the actual frequency, dominance, starvation, or exploitation.

The ten named decisions all have source ai_will_do blocks. No unbounded expression was found in those clauses. No positive score on an obviously impossible candidate was confirmed by this bounded source review, because each decision has separate visibility/availability or helper gates. These are source findings only; actual candidate eligibility and any external selection effects remain unresolved. All response declarations use fire_only_once = no, while current-contract status, negotiation phase, one-use extension, slot validity, cooldown, and cleanup alter future availability. Repetition, rank reversals under external factors, starvation, and snowball risk were not analyzed by a supported sequence or sweep. No MTTH timing distribution applies to this decision score pass.

## References read locally

The reference MCP tools were not callable in the current session, so these citations are direct local reads with SHA-256 revisions, not revision-bound MCP references.

| Local reference | Read span and use | Local SHA-256 |
| --- | --- | --- |
| paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md | Lines 26-36; ai_will_do score race, external modifiers, and distinction from ai_chance sampling | 917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818 |
| paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md | Lines 357-372; decision ai_will_do as a conditional MTTH-style score block | 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md | Lines 1-35; country scope and visible/available evaluation cadence; no decision-weight semantics | 5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\GER.txt | Lines 250-279; GER_seize_gold_reserves conditional base/factor precedent | 6E109AF4C268DCD4E67AEC2D70EF7ABD479D64B06EBB2FC439A9777591C5C3C8 |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md | Lines 557-565 and 687-692; stock and army target/fielded measurement semantics | 538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA |
| C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md | Lines 6550-6557; country-scope send_equipment | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | Lines 1614-1619; native equipment stock and army target/fielded quantity definitions | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A9403E790E7AF32D4 |

The installed documentation folder contained no decision ai_will_do weight section in the bounded search. The adjacent installed common/decisions documentation and vanilla conditional decision were read directly. Since no reference IDs or MCP revisions were returned, hoi4.reference_read could not be called revision-bound.

## Recommended owner follow-up

1. Restore the callable HOI4 MCP probability route and begin again with probability_inspect for common/decisions/012_africa_gods_decisions.txt. Ask the adapter for its actual participant decision or pool selector and supported typed country/host requirement schema before binding fixtures.
2. Keep the direct-response, negotiation, and no-active-demand defiance pools separate. Supply each complete concurrent candidate pool the adapter requires; the ten named IDs alone are not certified as the full decision category.
3. Re-evaluate all six preserved scenario IDs with explicit typed family/subtype, immutable contract, matching native stock/army target/fielded state, host validity, demand phase, deadline/day, Wrath/offender state, and other supported modifiers. Include the requested artillery-only-need/truck-only-stock, healthy-host, reserve-protection, and odd 11 / partial 5 / remaining 6 traces only if the adapter accepts those bindings.
4. Use a threshold/sensitivity sweep for supported stock/reserve and Wrath boundaries and ask the analyzer for rank reversals. Render ranking, matrix, or unresolved views only after a successful analysis ID exists.
5. Establish and retain a fresh post-mobile current baseline for future weighted edits. The decision file is unchanged, but its typed eligibility dependencies changed and can alter existing conditional score branches. Do not compare now: there is no successful exact before analysis paired with the same saved scenario set. For any later owner-applied weight change, run probability_compare on matching scenarios and sources.
6. Ask the owner to resolve the permanent-defiance comment versus conditional raw score and the generic substitute/slot-1 duplicate outcome after supported evidence is available. This audit proposes no numeric weight, threshold, or balance target.

## Completed work, blocked work, and uncertainty

Completed: read repository AGENTS.md; read chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-mtth guidance; read the previous Gods probability handoff and the completed mobile helper, mobile text, mobile tribute, and mobile integration audit handoffs; read the current decisions, typed triggers, effects, constants, offline wiki, and installed vanilla references; verified the unchanged decision-file hash against the previous baseline; reviewed source-only score and eligibility behavior.

Blocked: the required current probability inspect, scenario evaluation, sensitivity/rank-reversal sweep, fresh baseline, valid before/after comparison, and rendered probability evidence. The exact route errors are recorded above.

Uncertainty: adapter coverage, full category candidate pools, hypothetical typed scope support, all six scenario fixtures, external decision-selection factors, engine candidate validity, ranking, exact selection chance, dominance, actual starvation/repetition, and exploit or snowball risk remain unresolved. No current result can support numeric AI balance acceptance.

No implementation simplification was made. The mandatory MCP analyses were blocked and are not replaced by the source review. The overall Gods AI/probability audit and numeric balance acceptance remain incomplete.

Skills used: chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-mtth. No skill was created or updated.
