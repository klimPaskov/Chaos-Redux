# Event 023 first-use boundary audit: High Chaos, Evolution IV absent

Audit date: 2026-09-26.

Mode: read-only; no gameplay, specification, workbook, asset, or existing handoff file was edited, and no commit was created.

Disposition: the source-level gate is present and aligned with the accepted scenario, but scenario-level MCP validation remains unresolved because the live analyzer cannot bind the required campaign variables and target scopes.

## Scope and acceptance basis

Audited scenario: P23_FIRST_USE_HIGH_CHAOS_EVO4_ABSENT.

Acceptance basis: the user's explicit Event 23 goal says AI major first use is impossible below Evolution IV and High Chaos alone never permits it; the named case was added to the probability scenario specification and Part 10 acceptance scenario G.

Scenario expectation: Chaos 1100, Evolution III active, Evolution IV absent or disabled, a nuclear-major target at war, and all other severe first-use conditions hypothetically satisfied; authorization eligibility remains false.

Weighted candidate: sov_nuclear_bombs_give_final_authorization in C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\023_sov_nuclear_bombs_decisions.txt.

Related identifiers: sov_nuclear_bombs_authorize_selected_strike; sov_nuclear_bombs_event_severe_first_use_gate; sov_nuclear_bombs_event_can_authorize_first_use; sov_nuclear_bombs_event_has_valid_prepared_strike; sov_nuclear_bombs_event_prepared_strike_chain_is_valid; sov_nuclear_bombs_action_major_first_use_gate_is_valid; sov_nuclear_bombs_event_has_evolution_iv.

## Probability MCP evidence

Workspace: mod_chaos_redux_ea3b2d67c2c0.

### Required first call and source discovery

The first probability_inspect call used adapter decision_ai_will_do without a source and was rejected with: MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters.

The accepted source form, confirmed in the live route guidance, was source { path: "common/decisions/023_sov_nuclear_bombs_decisions.txt" }.

The first successful source discovery scanned mod:common/decisions/023_sov_nuclear_bombs_decisions.txt and returned sourceRevision 9169079c355195c82f3ea07f3e43364e18d183d1f1a176199a9af8113cdc563b with MCP sourceHash f86565ae8b81a493d5c84a814610137f5f3e12d56b06ab74bbdff904ebfa3cde.

The source inspection requested decision_ai_will_do and returned status ok, code PROBABILITY_SOURCE_DISCOVERED, requestedAdapter decision_ai_will_do, suggestedAdapter mission_ai_will_do, discoveryReason requested_adapter_empty, candidates 0, availableCandidates 81, requiredInputs 0, and unresolved 0.

Targeted decision-adapter inspection returned sourceRevision 410e89280a39cac8fa9682e212cf4b1b22453bae36d465613d9e92f250befdbc and MCP sourceHash f86565ae8b81a493d5c84a814610137f5f3e12d56b06ab74bbdff904ebfa3cde.

The requested candidate matched one entry under the suggested mission adapter, but the decision adapter still indexed zero candidates.

Inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bca6add60607d28a305157090f3b544b8ab6edfaa2e6b96c0a1e2aadb8342439/c0af70aaee6aedccdcadb151de3179ac98cc284706ec5412c5656dcce32406ff/probability-inspect-f86565ae8b81.json

The follow-up mission_ai_will_do inspection found the exact requested candidate as one candidate, poolComplete true for that one-item probe, availableCandidates 0, requiredInputs 8, unresolved 0, with no blockers.

Targeted mission-adapter inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2becc5ada5a3033c2de59dab29044e179ecedc7892782df3a1fb47689ee42d7/271e903e83ccc7b2ac43b2d15ef4c5e1627ec1ff04c14bb1c04572cdedecfa79/probability-inspect-f86565ae8b81.json

An earlier source discovery and the targeted inspections reported the same MCP sourceHash, while sourceRevision changed after refresh; the final evaluation revision is recorded below.

Initial source-discovery artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f49320bb14fc8c405677e5d8cb87bbdf50d73c42cfa097122c524cb939377295/3f5b3968970b9eb657fdd0a1c4097e7ae612f1e9829019c9ab46a9ac9b49f9cd/probability-inspect-f86565ae8b81.json

### Accepted scenarioSet and evaluation

The final request used only the live-accepted fields id, scenarios, actor, state, flags, and scopes.

The flags below are source-defined identifiers; no synthetic flags, variable declarations, fixture records, or scope ids were added.

~~~json
{
  "id": "P23_FIRST_USE_HIGH_CHAOS_EVO4_ABSENT",
  "scenarios": [{
    "id": "P23_FIRST_USE_HIGH_CHAOS_EVO4_ABSENT",
    "actor": "SOV",
    "state": {},
    "flags": [
      "sov_nuclear_bombs_event_active",
      "sov_nuclear_bombs_evolution_iii_active",
      "sov_nuclear_bombs_capital_threat_active",
      "sov_nuclear_bombs_front_collapsed",
      "sov_nuclear_bombs_reserve_exhausted",
      "sov_nuclear_bombs_enemy_launch_preparation_verified",
      "sov_nuclear_bombs_actor_registered",
      "sov_nuclear_bombs_authority_centralized",
      "sov_nuclear_bombs_limited_strike_prepared",
      "sov_nuclear_bombs_strike_preparation_complete",
      "sov_nuclear_bombs_action_reservation_active",
      "sov_nuclear_bombs_technical_certified"
    ],
    "scopes": {}
  }]
}
~~~

Evolution IV active is deliberately absent from the flags list, matching the scenario; the source also uses the separate global disable flag events_log_disabled_evolution_23_23_4.

The request asked for adapter decision_ai_will_do, candidatePool [sov_nuclear_bombs_give_final_authorization], metric raw_value, outputs json and unresolved, refresh true, and the decision source path above.

Evaluation status was ok with code PROBABILITY_ANALYZED_PARTIAL, but the returned adapterId was mission_ai_will_do, not decision_ai_will_do.

Analysis id: probability-1364f25270fc044f03ebfcab.

Scenario hash: 03958c7654bf51f78938fe65e3ef9301587442d77ef0e7a1540c6b3136fab6cb.

Evaluation sourceRevision: 52936ec518d6561bcd257b24f9a2fd99d2fff20981b2a68dedb4fad7a077e003.

Evaluation MCP sourceHash: f86565ae8b81a493d5c84a814610137f5f3e12d56b06ab74bbdff904ebfa3cde.

Evaluation result counts: one scenario, one candidate, 12 unresolved items, two diagnostics, and two visual resources.

The diagnostics say that modifier factor constant:sov_nuclear_bombs_ai.severe_loss_factor and modifier factor 0.00 were not active in any supplied scenario.

The inactive 0.00 modifier is consistent with the supplied Evolution III flag because that modifier applies only when Evolution III is absent.

The severe-loss modifier's inactive diagnostic is not uniquely attributable to Evolution IV absence by MCP because the campaign variables and target scope remain unresolved.

The inline result did not expose a numeric raw_value; the authoritative per-candidate JSON is linked below, and no arithmetic was substituted for that evidence.

Evaluation JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2eaf090b5a7253bfaa38325d5e864d8497ba63c9e8f8bbd8120f21ab6fd40b3c/d1a9f9e65987f52726ac01dc7031af71af451316e191982158ceaa62ac31402d/probability-1364f25270fc044f03ebfcab.json

### Rendered probability evidence

hoi4.probability_render was called for analysis probability-1364f25270fc044f03ebfcab with expectedScenarioHash 03958c7654bf51f78938fe65e3ef9301587442d77ef0e7a1540c6b3136fab6cb and outputs json and unresolved.

The render returned status ok, analysisStatus partial, the same sourceRevision, MCP sourceHash, and scenarioHash, with 12 unresolved items.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93b91d865e6d8bf7c998e1139803dd82a995bd14a88ebbd5d64fda233daafa6a/bb4911c24c3094d98e840e866bb1893ee0887b3945172902746217015abf8996/probability-probability-1364f25270fc044f03ebfcab-unresolved.svg

Rendered unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/416850b0ae064071c986488a4603340e895430667e066300f7cc05e782061381/ca6d4119bd4cbf8851c77d32376e4ea51230f93ee6c00b042863014dba67eb19/probability-probability-1364f25270fc044f03ebfcab-unresolved.png

Rendered unresolved HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e00f3c13d89a7f1b0277a0cf16e2ebdfdaca1a8f593712361863dd8d139e77e/205e0b558fb62ba767fffa37a85eb7bf7f6543cca1c0160182a0c8842eb37b6b/probability-probability-1364f25270fc044f03ebfcab-unresolved.html

### Superseded empty-fixture probe

Before adding the source-defined positive flags above, a schema-only request used the same scenario id with empty state, flags, and scopes.

That preliminary run returned analysis probability-db5dfff8194bcae71c6e4398, scenarioHash 725b9501baf585bac8b9edc8224eeaa61fe8d98bfaa1ee35675e7a0d24ee07e3, and 12 unresolved items.

It is retained only as an input-discovery record and is not the final scenario evidence.

Preliminary JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/820bcf93bbd76a0a6f3449df82e7a8ebdec960ebca02d3c9cf24ff4d7aafe181/d9446becc3fcc6d72f643e612f1740c2de461ee824f9006ffb92613ab9d350df/probability-db5dfff8194bcae71c6e4398.json

## Source trace

The final authorization decision is visible only after the actor, limited-strike preparation, preparation completion, and technical-certification flags are present.

Its available block calls sov_nuclear_bombs_event_prepared_strike_chain_is_valid and rechecks technical certification; the complete_effect then calls sov_nuclear_bombs_authorize_selected_strike.

The AI weight at common/decisions/023_sov_nuclear_bombs_decisions.txt:640 is base 0.10, multiplied by constant:sov_nuclear_bombs_ai.severe_loss_factor when sov_nuclear_bombs_event_can_authorize_first_use is yes, plus a factor 0.00 only when Evolution III is absent.

The constant severe_loss_factor is 1.50, so it is a score multiplier and not a 50 percent selection chance.

The source base term is 0.10 as a willingness score; the effective scenario score remains unresolved because the MCP did not return a numeric raw_value and external factors are incomplete.

sov_nuclear_bombs_event_has_evolution_iv checks the country flag sov_nuclear_bombs_evolution_iv_active.

sov_nuclear_bombs_event_severe_first_use_gate has Evolution IV as its first required condition, followed by Chaos at least 1000, war, strategic losses at least 3, capital threat, collapsed front, exhausted reserve, confirmed enemy use or verified enemy launch preparation, no moratorium, no prior recorded Soviet major first use, valid delivery and crew certification, Readiness at least 75, Integrity at least 20, and a nuclear-major target satisfying the lower-consequence rule or the prior-populated-use exception.

sov_nuclear_bombs_event_can_authorize_first_use requires that severe gate and additionally checks that the selected state's owner or controller is at war with the Soviet root.

sov_nuclear_bombs_event_has_valid_prepared_strike permits a major target only when the major-exchange world gate or sov_nuclear_bombs_event_can_authorize_first_use passes.

sov_nuclear_bombs_event_prepared_strike_chain_is_valid includes the prepared combat-strike state, active reservation, actor validity, no active project, no moratorium or suspended release orders, selected-state validity, action context, and centralized or delegated authority.

The runtime predicate sov_nuclear_bombs_action_major_first_use_gate_is_valid routes AI combat use without confirmed enemy nuclear use through sov_nuclear_bombs_event_severe_first_use_gate.

The runtime predicate has a separate confirmed-enemy-use plus major-exchange branch for retaliation; that is not the named first-use scenario.

sov_nuclear_bombs_authorize_selected_strike checks the prepared-strike chain again before staging an action and calling the shared action executor; accepted actions record a receipt and clear the prepared action context.

Evolution IV activation also checks the disabled-evolution global flag before activation, and the active Evolution IV flag is set only through the Evolution IV enable path inspected in the Event 23 effects file.

The source therefore has a deterministic conditional implication: when the Evolution IV active flag is absent, the severe first-use gate is false regardless of Chaos or the other severe conditions.

## Values, completeness, and classifications

| Question | Finding | Classification |
| --- | --- | --- |
| Is Evolution IV required by the source authorization gate? | Yes; it is the first condition of the severe gate used for AI first use. | Exact source implication |
| Does Chaos 1100 replace Evolution IV? | No; the source checks both the Evolution IV active flag and the separate 1000 Chaos threshold. | Exact source implication |
| Is the named scenario's engine eligibility confirmed by MCP? | No; the final evaluator returned 12 unresolved items and could not bind all required campaign state. | Unresolved |
| What is the decision's base AI weight? | The source base term is 0.10, with a 1.50 severity multiplier guarded by can_authorize_first_use; the Evolution III absence modifier is inactive in this scenario. | Score-only source trace |
| Can a positive willingness score bypass decision availability or action authorization? | No bypass appears in the source path: availability rechecks the prepared-strike chain, and the runtime AI first-use branch rechecks the severe gate. The engine scenario is not MCP-proven. | Exact source implication; runtime scenario unresolved |
| What is the numeric effective AI score in the named campaign state? | Not returned inline and not recoverable from the unresolved bindings without interpreting uninspected artifact contents. | Unresolved |
| Is there a normalized probability that the AI clicks or selects this decision? | No such probability was established; the inspected candidate is a willingness score and the decision adapter was remapped to mission_ai_will_do. | Unresolved; no probability claim |
| Is the candidate pool complete for a selection race? | The singleton candidate is complete only for the requested score probe; no full decision race or rank pool was evaluated. | Incomplete for ranking |
| Are external scenario factors complete? | No; the accepted prose's numeric Chaos, strategic-loss, Readiness, and Integrity values, target owner/controller war, target-major status, delivery route, and global flags/scopes were not bound. | Incomplete |
| Are rank reversal, dominance, or starvation findings available? | No; there is no complete comparison pool or sweep result. | Unresolved |
| Are repetition and terminal-state risks quantified? | No sequence or campaign horizon was declared; source flags prevent a repeated first-use route, but cadence was not MCP-tested. | Unresolved |
| Is there a source-level bypass or exploit path around Evolution IV? | None was found in the audited eligibility and runtime authorization chain; execution remains unverified by MCP for this campaign state. | Bounded source review |

The scenarioSet uses the documented shape, but state is empty and scopes is empty because the live guidance does not document typed bindings for the Clausewitz variables or the action-state and target scopes required by this chain.

The flags array contains only source-defined identifiers; it cannot supply numeric global chaos, strategic-loss, Readiness, or Integrity values or the nested target relationship.

The scenario represents Evolution IV as absent by omitting its active country flag; the alternate disabled-global-flag branch was not separately represented because the live fixture schema documents no typed country-versus-global flag binding.

The candidatePool is a singleton scalar-score probe, not a normalization pool.

No exact or bounded selection probability, campaign timing, rank reversal, dominance, starvation, repeated-action rate, or exploit rate is claimed.

## Structural Event MCP evidence

The read-only trace used event root chaosx.nr23.1, downstream direction, maxDepth 8, maxNodes 100, and maxEdges 100.

The first event_inspect route probes returned these exact errors before the accepted selector form was found:

- MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Invalid input: expected object, received string at from.
- MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at from.kind.
- MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Invalid input: expected string, received undefined at from.eventId.
- MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Trace requires selector at selector.

The successful selector was { kind: "event", eventId: "chaosx.nr23.1" }.

The trace returned EVENT_INSPECTED_PARTIAL, revision b19c7598ecdee0b5f2ff38e73c6ccc0a959a8bc274b1366669f03c6254ff33cd, graphHash b21ab27433e29831a0b1957754e4affceed5b7a87b28f0b2e7242417bc0007cf, 9,836 events, 38,554 edges, 8,908 unresolved nodes, 2,194 diagnostics, zero blocking diagnostics, zero expanded helpers, and a nine-node selected view with 42,853 nodes omitted.

The inline source inventory was truncated to 64 of 384 paths; the linked trace is the complete evidence.

Trace artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebd31681645930d5842527dc06e900fc3f4d1aa3c32a6828bf962f1e26c15f02/0e86168ebd07f020682c94062b2d1344fc6e4f0ed4340d66084aab6ceb9c55a5/event-trace-b19c7598ecde.json

The trace validation check said: Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked.

hoi4.event_render used view unresolved with the same event selector and returned EVENT_RENDERED_PARTIAL.

The final render revision was f95e58711c7ffdcda2bae4e59e7e030aa20b045e86c1e5e9d35a647536d55fa0, graphHash 06fc0bb73dcf1f3e4c47694633ac804b9d812ab3372152192f305b3b10a289e3, and layoutHash e22194d8435f7595e72907e160795561e14e93ad83da65c10fe677f52b97d084.

Its coverage remained nine selected nodes, 42,853 omitted nodes, 8,908 unresolved nodes, 2,194 diagnostics, zero blocking diagnostics, and zero expanded helpers.

Rendered Event 23 unresolved manifest: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc59f9175cca3ed18bd0cf6b8d7daf11f45982f60e0e6d0c56f130a37be997e1/417969ef2937df86b603499a7f84c8c9b3f11aba4ecd74a67f1e90786e1ce83f/event-unresolved-f95e58711c7f-manifest.json

Rendered Event 23 unresolved JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8157a3639208d559a61d31a4ce0d2a161e5865eeb9eed15c18c0296a4d6ce5eb/259d4f08f3ead3bfb620b3e3f0eb5d19055be66059614bac08610a6faf9ce35e/event-unresolved-f95e58711c7f.json

Rendered Event 23 unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/001d626ed46c4f85f1675a78d5de419cc24b8521ca81a69cc472a00ede868d9b/b19bce606865a9e9a3cb6c2bf01c41144d3e58e0ed3a690729c5248c8820eb44/event-unresolved-f95e58711c7f.svg

Rendered Event 23 unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fc1b68971fcb90a25d4dcf05574dfd211acc502f7f0922e305685bd73cdc162/580b6492801aff4f54f707c947edd555988af3129ed48eef52036a8803cfa63a/event-unresolved-f95e58711c7f.png

Rendered Event 23 unresolved HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2878071f443d0a6245a4533a86f951a41aa354531124a3f0fb3316337e28eda/1b816596cb584802e3c91211582b443f26e25be6c8a196211c41706d4d53ede3/event-unresolved-f95e58711c7f.html

The rendered graph is broad workspace evidence, not a complete Event 23 helper expansion, and it does not replace the probability result or the direct authorization-source trace.

## Skipped analyses, blockers, and recommendations

hoi4.probability_sweep was not run because no documented fixture path can vary the global Chaos variable or the Evolution IV active state without inventing a sweep key; the single accepted case also supplies no typed numeric binding.

hoi4.probability_compare was not run because this audit made no source change and the user supplied no before-source artifact; comparing the current file to itself is prohibited by the route guidance.

hoi4.probability_simulate was not run because the accepted scenario declares no uncertain-input distribution or seed.

hoi4.probability_sequence was not run because this is not a complete custom weighted pool with declared cadence, transitions, and terminal states.

The exact remaining probability blocker is support for typed campaign values and nested actor, selected-state, target-owner/controller, war, delivery, and global-flag bindings under the documented scenarioSet schema, together with correct indexing by decision_ai_will_do for this decision file.

No AI-weight tuning or AI-weight change is recommended.

No gameplay patch is recommended from this bounded audit; the source-level Evolution IV gate is present and aligns with the accepted scenario, while the scenario-level MCP result remains unresolved.

The parent should not report the scenario as MCP-proven until the adapter can evaluate the required typed campaign context under the same scenario id.

## Source identities and references

The MCP sourceHash f86565ae8b81a493d5c84a814610137f5f3e12d56b06ab74bbdff904ebfa3cde differs from the local decision-file byte SHA-256 326D63D2239A2F827240DE5FEE35A0FC0F2BC93B9441E9DC56A31C1736DC2C66.

The live route exposes no mapping that reconciles those digests, so both are recorded separately and source-byte identity between the MCP snapshot and local file remains uncertain.

Local source SHA-256 values:

- common\decisions\023_sov_nuclear_bombs_decisions.txt: 326D63D2239A2F827240DE5FEE35A0FC0F2BC93B9441E9DC56A31C1736DC2C66
- common\scripted_effects\023_sov_nuclear_bombs_event_effects.txt: C3F3BA0ACA7C5FEFE0B5BE84704ACE1C292BB146E32BADDA896FC2FA35D3FEB5
- common\scripted_triggers\023_sov_nuclear_bombs_event_triggers.txt: D9D451369F89FEB97F85D7628DB62B33830BA79F47667021AD2EE3CB53D07093
- common\scripted_triggers\023_sov_nuclear_bombs_runtime_triggers.txt: BDF6DD93EA83B1CF484F1E23F9E0DBB373735AD8DA1401C468DB249BFE99FDCF
- common\script_constants\023_sov_nuclear_bombs_constants.txt: 073BC77FB14B4FC6D2CCF0CE8EC46939E96EE62DC9EE201B12C1A04F50F097CE

Accepted design reviewed: docs\specs\023_sov_nuclear_bombs_specs\023_sov_nuclear_bombs_probability_scenarios.md, the complete named scenario P23_FIRST_USE_HIGH_CHAOS_EVO4_ABSENT, spec Parts 4, 5, and 9, Part 10 acceptance scenario G, and the complete Event 023 decision map.

Offline Paradox wiki pages consulted: Data structures; Triggers; Effects; Modifiers; Localisation; Scopes; On actions; Event modding; Decision modding; Idea modding; and AI modding.

Vanilla documentation consulted: C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md for flags, variable comparisons, war, and AI scope; C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md for decision-related effects, country flags, and event effects; C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md for modifier context.

Skills applied: chaos-redux-subagents for MCP/handoff evidence and chaos-redux-decisions-missions because the audited surface is a decision with AI willingness and a distinct availability gate.

chaos-redux-mtth was not used because this surface has no mtth: entry or MTTH-backed AI weight; it is a decision ai_will_do base and modifier block.

Only this handoff file is intended to be written; no commit is requested.
