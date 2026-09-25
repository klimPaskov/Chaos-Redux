# Event 016 country-settlement AI probability audit

Date: 2026-09-25

Disposition: **incomplete; probability conclusions unresolved**. This is a read-only audit handoff. The only authorized write was this file. No gameplay, localisation, unit, model, 3D asset, or other source was changed or touched, and nothing was staged or committed.

## Scope and design authority

Audited surfaces: `chaosx.nr16.5` and its 13 event options in `events/016_brilliant_scientist_context_events.txt`; the six `.7` and `.8` options in `events/016_brilliant_scientist_host_reaction_events.txt`; the country settlement constants, resolver, and unresolved-receipt trigger listed below.

The accepted vector authority is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_broader_country_settlement_content_implementation_2026-08-03.md`. The accepted design says the ten named country options reuse the existing `.5` resolver and add one bounded vector and receipt; `.7` and `.8` keep their existing three choices and receive only settlement-specific description and AI factors. Current status and pending transfer, cleanup, balance, and probability validation are summarized in `docs/events/016_brilliant_scientist/overview.md` and `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_7_world_reactions_and_ai.md`.

Accepted total vectors, ordered `(Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, Grievance)`, are ENG `(+5,-10,+15,+5,+20,-15)`, USA `(+10,+5,+10,+15,+5,-5)`, SOV `(+5,+20,-5,+15,-5,+20)`, JAP `(+15,+5,+5,+10,+5,+5)`, GER `(+10,+20,-10,+20,-15,+20)`, FRA `(+10,-10,+15,+5,+25,-20)`, ITA `(+20,+10,+15,+15,+5,-5)`, CHI `(+5,+25,-10,+20,-20,+15)`, POL `(+15,0,+10,+5,+15,0)`, and CZE `(+5,-15,+15,+15,+20,-15)`. These are accepted design/source figures; this audit did not replay the effects or validate their downstream balance.

## Source files and identities

The local SHA-256 hashes below were read during this audit. The MCP source hash is included separately where available.

| Source | Local SHA-256 |
| --- | --- |
| `events/016_brilliant_scientist_context_events.txt` | `9C2A9B9E2567A26093670CA27B0B60F09EC03EF3352EAAC788F769EA7802481B` |
| `events/016_brilliant_scientist_host_reaction_events.txt` | `304F414DDE65F73DE59788157FB5902B600D30900BD880795ADF8E24F499F550` |
| `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt` | `BCC719DDD9599794F92BFB0A77809A54B5A9FD1B7AA007387219EE7E89558CBE` |
| `common/scripted_effects/016_brilliant_scientist_context_effects.txt` | `C76E351AA366BE60E69472E007B56312C2C18642AAB4B96F8F9AC63819C2B80A` |
| `common/scripted_triggers/016_brilliant_scientist_context_triggers.txt` | `A43A8881A85BEB14F922D94537652676640C3920A66F6B39565E47F43C718621` |

Related external weight inputs named in those sources include `brilliant_scientist_evolution_ai.*`, `brilliant_scientist_host_flavor_ai.*`, `brilliant_scientist_host_reaction_delta.ai_*`, `brilliant_scientist_opening_ai.industrial_factory_gate`, and the scripted host, archetype, and high-value triggers in `common/scripted_triggers/016_brilliant_scientist_triggers.txt`. Their runtime values and scenario bindings were not resolved by the probability adapter in this pass.

## HOI4 MCP evidence

All tool calls used the connected workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Probability inspection

- Started with read-only `hoi4.probability_inspect` for `event_option_ai_chance` on `events/016_brilliant_scientist_context_events.txt`. Source discovery returned `PROBABILITY_SOURCE_DISCOVERED`, `sourceRevision=d5b8c7a16c616b0ce8f5bb9f32d9f103e6d232b7b428c26791f6cf8b6258681d`, `sourceHash=b5ae25990c04b9d0ba2e14b4abc9ee793bbed6dcfb48ede345c316514c514c54`, and 21 available candidates in the file. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86bc4dfb0cf9b9f63b684011da967300dc9c39f16ac517f344e62cac9b145f75/7c228250d99a1746b265ad3c4fa4cb5a7a80326b07af99175727c4c0e6d530db/probability-inspect-b5ae25990c04.json`.
- A focused adapter inspection of the same source returned `PROBABILITY_SOURCE_INSPECTED`, `sourceRevision=6a1a194654f8c567ca6b9fcf36a1b064239a53ab5928b56e48a9c821f8b44f5f` and the same `sourceHash=b5ae25990c04b9d0ba2e14b4abc9ee793bbed6dcfb48ede345c316514c514c54`, but reported `poolComplete=false`, 21 candidates, zero available candidates, six required inputs, and one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39416bc68779cb8bb157b2e5db065f0945d263336c9fd44af1225475526406b9/fb55d7373f6870dacb0a50785ce1bd954a68e27523ee6cf29c01ddbf8a958ed7/probability-inspect-b5ae25990c04.json`. The source hash stayed stable while the reported source revision changed between these inspections.
- The declared `.5` pool was the 13 visible option names `.5.a` through `.5.m_cze`. Inspecting with that pool returned `INTERNAL_ERROR` / `Unexpected internal error`, with no artifact or diagnostic detail. The adapter therefore did not attest that the scenario pool was complete.
- Inspection of `events/016_brilliant_scientist_host_reaction_events.txt` returned `sourceRevision=fadb37e707f6918a9f9fec5c496ee49ad58cee9f2519f39895122660d88008c5`, `sourceHash=c839cdd6824339ec6fc966b339565053ea38fa37fdac128fca8bd5941e8931d2`, nine file-level candidates, `poolComplete=false`, zero available candidates, five required inputs, and one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2155cd178cf2553de1df055c97147185fa9abfb5105612c78a867e35a7398f58/2bcf57a1dcdc053876abcb3f17a2b8c87a9385f5a754a81a7474025521952add/probability-inspect-c839cdd68243.json`.
- A second inspection declared the six `.7.a`–`.7.c` and `.8.a`–`.8.c` names. It returned six requested candidates but still zero available candidates, `poolComplete=false`, four required inputs, and one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30de1aa7bcdaca6bf0960965a6de977ea64a2737e246d139e3c8477f01556476/c4ea40fa110af9945d7390af9dfe4946239ffc4bb71573ba6617542b02e51c99/probability-inspect-c839cdd68243.json`. The file-level count of nine includes the separate `.9` surface, which is outside this audit.

### Event structure inspection and render

- `hoi4.event_inspect` lint for `chaosx.nr16.5` returned `EVENT_INSPECTED_PARTIAL`, revision `811e61df0f66e2986e5ba3d637f8f755945d0c067de0b312c964852355901694`, graph hash `4d1c6fc2b78e2871312bd7c3170c33e645624c4434b6a148075f9cce323839a3`, and zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b61f7ff70271104f4590cbb6f6aea250005812373943cd21a16fe8a02ba44980/b321134d5410715c833fc478f112cc2bc9cbe9a9e6db03e47459560272b32cea/event-lint-811e61df0f66.json`. The workspace analysis deferred helper projections and lifecycle passes. Its large workspace counts are not event-specific diagnostics.
- `hoi4.event_render` options view for `chaosx.nr16.5` returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `c557885de33491cacc30d8a6804316e88aaf66f0fe0f55c4424007dca1ee30b9`, zero blocking diagnostics, 40 selected nodes, and 42,813 omitted nodes. Render artifacts: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1c73ae71cf0cabf28ca1bdd5670d8cb978107f7f8e0c7402395522a28a5736f/b9eb408dd6f5427e48684c09db3a87fc210af2dde9c195397e220d2e2409328c/event-options-811e61df0f66-manifest.json`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96645c2eaca5acca42a37a39fc1f99b396df0fbaf89204e0b2ad961b4fd0aaf3/a1098ecfc0236d1bf761e3b708c592612dda4ab641246d90e9110a7f2ed79b2a/event-options-811e61df0f66.json`; SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9e4cdb13389dd08195b516fd836f45f865f856b765914a6737237687e4d1903/39667687072504f89845757925855368755f6f4fd2948389df860566bedf5ea9/event-options-811e61df0f66.svg`; PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c4ad57b80fa1ce3e12c8ddea09a04acbcf57bbe9d6689ba505ffed0d847e776/9c4a8138e076784cd3c91f96884670a1279669f2e5b30d679b889ac1539198a3/event-options-811e61df0f66.png`; HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f57d1934015aab369bd1923b9db05f1ed0e5cc467217aa6bdc7edb467e933d3b/b812ba085e1c69c8c9d6dee177048804e26de6ab79b7a56bd7d5a363b09227a5/event-options-811e61df0f66.html`.

### Scenario and probability-analysis status

No `hoi4.probability_evaluate`, `hoi4.probability_sweep`, or `hoi4.probability_render` result was obtained. No scenario IDs or scenario hashes exist for this audit. User direction at the end of the turn was to stop further long MCP calls and finish with existing evidence; therefore the required numeric evaluation and sweep remain **unresolved**. No `hoi4.probability_compare` was warranted because no source weights changed. `hoi4.probability_simulate` was not warranted because no uncertain inputs were explicitly declared for sampling. `hoi4.probability_sequence` was not applicable because these are ordinary event option races, not a declared custom pool with cadence and transitions.

The next probability pass should use named scenarios for each of the ten actors with an eligible `.5` context, a context or tag mismatch, and relevant peace/war, public/secret, and high-meter states. It should use the complete `.5.a`–`.5.m_cze` source pool and record which options are gated out per actor. For `.7` and `.8`, evaluate each of the ten settlement receipts against all three event options, plus the government, context, war, exposure, grievance, and accident-pressure variants that the source factors reference. Suggested, not submitted, scenario IDs are `e016_nr16_5_<tag>_eligible_base`, `e016_nr16_5_<tag>_mismatch`, `e016_nr16_5_<tag>_war_secret_high_risk`, `e016_nr16_7_<tag>_receipt_base`, and `e016_nr16_8_<tag>_receipt_base`. No exact, bounded, or sampled selection probabilities are claimed.

## Source-backed scores and eligibility

The settlement constants define `.5` national option base `10`, preferred factor `2.25`, and cautious factor `0.50`; `.7`/`.8` settlement receipt factors are preferred `1.50` and cautious `0.70`. These are score inputs, not normalized probabilities. The generic `.5.a`–`.5.c` weights reference `brilliant_scientist_evolution_ai.base`, `.preferred`, and `.cautious`, and several context-flavor constants and scripted triggers. Their evaluated values are not present in the successful MCP evidence.

The ten named `.5` options have explicit country-tag and context gates: ENG public/distributed; USA industrial/distributed; SOV and JAP strategic-security/industrial; GER strategic-security/industrial; FRA public/distributed; ITA and CHI strategic-security/industrial; POL public/distributed/strategic-security; CZE industrial/distributed. The three generic options remain in the race where their own triggers pass, including the unconditional mediation option `.5.c`. Each named option has positive base weight `10` in source. ENG, USA, SOV, and JAP repeat their complete eligibility-context OR condition as the preferred-factor condition, so that `2.25` modifier is always active whenever that named choice is eligible. This is a source-level score observation; its normalized effect is unresolved. Other named choices apply the preferred factor only to one of their eligible contexts and apply the `0.50` caution factor to their listed war or high-meter conditions.

In `.7` and `.8`, the settlement receipt flags apply named `1.50` preferences or `0.70` cautions to the existing choices. The `.7` source maps ENG/FRA/POL toward `.7.a`, SOV toward `.7.b`, and USA/JAP/GER/ITA/CHI/CZE toward `.7.c`, with additional cautions for specified receipts. The `.8` source maps ENG toward `.8.a`, SOV/JAP/GER/CHI toward `.8.b`, and USA/JAP/ITA/CZE toward `.8.c`, again with specified cautions. These factors can interact multiplicatively with government, context, archetype, war, and high-value modifiers; no final ranks or rates were proven.

## Findings and recommendations

1. **The weighted analysis is not complete.** The adapter could not establish a usable complete candidate pool, and no scenario evaluation or sensitivity sweep was run. Do not use the static weights or accepted vectors as balance evidence. Parent follow-up: rerun the probability pass with an adapter-supported candidate identity and explicit tag/context/receipt states, or retain the conclusion as unresolved if the adapter still cannot bind those inputs.
2. **The four `.5` preferred conditions are redundant with option eligibility.** For ENG, USA, SOV, and JAP the preferred multiplier does not discriminate between eligible contexts. Parent should decide whether that always-on national-choice premium is intended. If not, replace the redundant condition with an actually distinguishing accepted context or remove the multiplier, then compare the same named scenarios after an owner patch.
3. **Relative `.5` weights and reaction ranks remain unknown.** Generic base constants, archetype factors, and high-meter trigger results are external inputs. No dominance, starvation, rank reversal, probability floor, or threshold conclusion is supported until those inputs resolve in the analyzer.
4. **Check `.8` option coverage under government changes.** The source contains government-gated reaction choices. Confirm every eligible host, including CHI and hosts whose government changes before `.8`, has at least one valid option and a safe fallback. The structural render was only for `.5`, and the probability adapter did not prove these gates.
5. **One-time guards reduce local replay risk in source.** `.5` requires a pending unresolved assistant conflict; each country resolver checks the shared mutually exclusive settlement-receipt guard before applying a vector. The accepted overview says `.7`/`.8` are career-once and transfer/cleanup behavior remains pending. No transfer, cleanup, or repeat-resolution scenario was evaluated here.

Selection semantics: `ai_chance` is a weighted option race, not a displayed score or an `ai_will_do` willingness score. The offline wiki pages `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:31` and `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:159` describe proportional option weighting and the engine's d100 granularity. Thus raw source factors cannot be reported as click probabilities, and even a complete mathematical normalization must account for the engine roll. The vanilla documentation files were located and relevant effect/trigger references searched, but a direct vanilla `ai_chance` precedent and the remaining core wiki pages were not fully reviewed before the user requested immediate handoff; this reference review remains a limitation.

## Coverage matrix

| Surface | Candidate pool and external factors | Result classification |
| --- | --- | --- |
| `chaosx.nr16.5` | 13 source options identified. Per-actor option eligibility depends on country tag, one of the context flags, current-host and pending/unresolved gates, plus war, secret-directorate, archetype, and high-value states. The adapter pool call errored; runtime trigger binding and external factors are incomplete. | Source factors: **score-only**. Eligibility and normalized race: **unresolved**. |
| `chaosx.nr16.7` | Three options in the event; per-actor receipt, government/context, archetype, war, and high-value factors are not all bound by the adapter. File-level inspect also saw `.9`, outside scope. | Source factors: **score-only**. Pool completeness and normalized race: **unresolved**. |
| `chaosx.nr16.8` | Three source options; settlement receipts interact with government/context, archetype, war, high exposure/grievance, and accident-pressure factors. Option-gate coverage is not scenario-verified. | Source factors: **score-only**. Pool completeness and normalized race: **unresolved**. |

## Skipped work, blockers, and remaining uncertainty

- Exact blocker for `.5`: the adapter call with the complete 13-name pool returned `INTERNAL_ERROR: Unexpected internal error`; focused inspection then reported zero available candidates, six required inputs, and one unresolved input.
- Exact blocker for `.7`/`.8`: the six-name declared pool inspection reported zero available candidates, incomplete pool coverage, and one unresolved input. No evaluation route result was obtained.
- Parent handoff instruction: no further long MCP calls were to be started after the last probability inspection. This prevented evaluation, sweep, and probability rendering. Because there is no analysis ID, probability rendering could not be attached to this handoff. The user's separate instruction prohibited model work.
- No MCP scenario IDs, scenario hashes, ranks, modifier traces, normalized rates, timing results, sensitivity thresholds, or rank reversals are claimed. All are unresolved.
- No weights changed, so probability comparison was skipped. No uncertain input distribution or custom sequence manifest was in scope.
- The focused Event Inspector and options render were partial and did not establish helper expansion, lifecycle, transfer, cleanup, or `.7`/`.8` structural coverage.
- The relevant offline Event Modding and AI Modding wiki sections were consulted. AGENTS.md, `chaos-redux-events`, and `chaos-redux-subagents` were read. Remaining core wiki and direct vanilla precedent review is incomplete as noted above.

No model, 3D asset, Portal Raider, Alien Infantry, or Autonomous Robot unit file was opened or changed.
