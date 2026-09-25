# Theater decontamination assignment probability baseline

Status: baseline captured before the parent’s theater-cost patch; read-only audit. This report does not validate or compare the later edit.

## Audited surface and source

- Weighted surface: decision cbrn_assign_decontamination_corridor, adapter decision_ai_will_do.
- Source: common/decisions/cbrn_doctrine_decisions.txt. Related baseline sources reviewed: common/scripted_triggers/cbrn_doctrine_triggers.txt, common/scripted_effects/cbrn_doctrine_effects.txt, common/scripted_effects/chaosx_dynamic_effects.txt, common/scripted_triggers/cbrn_triggers.txt, and common/script_constants/cbrn_doctrine_constants.txt.
- Baseline repository HEAD during source review: cbb163549744d72de4147413bb7a7c04dc0993ed. The parent later reported an unrelated commit (99dfa5402) and started the doctrine patch after baseline capture; neither is represented by the baseline source hash.
- MCP inspect source revision: 94498ccf2043b0d87cd115780cb7e7c512835952941226bbc81b341fb06d1561.
- MCP evaluate source revision: 1514bcc804339e063e5ec5ea4541a2f8ce25e35c68a8ad71a019c5a57fcc3c86.
- Both MCP operations reported the same complete source hash: 10792628365baec1d0963795cb81bfe638bf15273e3ec8ff6ef60ece4ab65768.
- Inspected decision block segment hash: 3838862aa3a89474d18f3264a256a7b7040a63886f7abe801f700b8a0dd384e7.
- Adapter: decision_ai_will_do, adapter version hoi4-1.19.2.v1; observed game version v1.19.2.0.a729 (Operation Postern 1.19.2.0, d245). Workspace: mod_chaos_redux_ea3b2d67c2c0.

## MCP evidence

The required first call, hoi4.probability_inspect, succeeded for the source path. It found four decisions in the file, but reported poolComplete=false, no candidates available from the unbound state, and eight required inputs: FROM, any_enemy_country, custom_trigger_tooltip, has_idea, has_war, has_war_with, hidden_trigger, and original_tag.

Inspect artifact:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9baed68d39841e5a9850d250774bf45112f30202c4cd26fd4501c9eed478540a/283e5d8abe6811993665307d153be2083a6215cc18ce7ab024a389a528d12b8a/probability-inspect-10792628365b.json

hoi4.probability_evaluate succeeded with PROBABILITY_ANALYZED_PARTIAL for scenario corridor_gate_unbound_baseline. Analysis ID: probability-3fd4871d9c6dfd72d5ce1f96. Scenario hash: 35ee95deb1b003f1c237d14b60aff7765d4015a5aa5173ba1031e79939bafd61. Candidate-pool hash: 926a0f8ce963f3ad54fa615450f586272ed59b3cdb478da451a56878c9a392c6. The request used metric raw_value, outputs json, ranking, and unresolved, and refresh=true.

Evaluation JSON:
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea95ab732c75dad80fdd9c999a9c550d1ed5113f0d2ffbdf698225ea4e6b0577/13aa4a696f306909fda611860d251b3b1197d91160c76a819705852843767f42/probability-3fd4871d9c6dfd72d5ce1f96.json

The exact ranking and unresolved render artifacts returned with evaluation are:
- Ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e015badb3fac9de8f3b4a029bfabb6a31de9f919e21cb9bb86a4bd6f126d8e9/aa1c34f4854287c4cb6212cf0e8349c7f186d391e02be1c54db8084903cd15bc/probability-probability-3fd4871d9c6dfd72d5ce1f96-ranking.svg
- Ranking PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53e608c122eb678ad738e228cf76262295977fae2a92ca96ca1bc706e917ce89/4ce5b2ef13c9814218a236d02cc3778776b6df6f274282c1aba1445e17aab5e7/probability-probability-3fd4871d9c6dfd72d5ce1f96-ranking.png
- Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9970c22dfa83cf49c1b8c80cd06fa4c40e291561bcec77d7c89f24718c040429/fab92dcdff4a1cc1296924a2b5209f6cb21f5c817bf6ba3617eca87455a899e5/probability-probability-3fd4871d9c6dfd72d5ce1f96-unresolved.svg
- Unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be1de0c42b293e356e2853e08b29e723c684d707e405bf4ffe49cf1d0c27e24e/d6fce2ee65d7e9a96decb091476ed0187aae5d0a74c4987ea55c3cf230f8b782/probability-probability-3fd4871d9c6dfd72d5ce1f96-unresolved.png

A separate explicit hoi4.probability_render attempt failed with PROBABILITY_ANALYSIS_NOT_CACHED: “Render requires an analysis ID produced by this server process.” The evaluation-generated ranking and unresolved render artifacts remain available as listed above.

## Exact saved request fixture

Reusable fixture file: docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_theater_four_cost_probability_fixture.json.

SHA-256: 441F449349ABAC7CC0AE084D3E52CE34B34A0DB9292796A4E82370CD552FED6D.

This is the exact scenarioSet sent to the successful evaluate call:

    {
      "id": "cbrn_theater_cleanup_baseline_inputs",
      "scenarios": [
        {
          "id": "corridor_gate_unbound_baseline",
          "actor": "CXT",
          "state": {},
          "flags": ["cbrn_milestone_theater_exploitation"],
          "scopes": {
            "FROM": {
              "id": "target_state",
              "state": {}
            }
          }
        }
      ]
    }

The complete candidate pool supplied to evaluate, in order, was cbrn_assign_decontamination_corridor, cbrn_choose_retaliation_only, cbrn_choose_battlefield_authorization, and cbrn_choose_unrestricted_authorization. These are all four decisions discovered in this source file, but the adapter did not establish that this is the complete in-game selection pool. Do not infer an exhaustive cross-category competition.

## Results and classification

The adapter declares selectionRule=score_only, normalizedProbability=false, timingDistribution=false, and supports raw scores and eligibility. All four candidate eligibility results remained unresolved; ranking and conditional selection probabilities were null. The source-file candidate pool is explicit but global pool completeness remains unresolved.

For the target decision, the trace applied constant:cbrn_doctrine_ai.theater_cleanup_assignment_base exactly at 40. It found constant:cbrn_doctrine_ai.theater_cleanup_serious_factor at 2 and constant:cbrn_doctrine_ai.theater_cleanup_severe_factor at 1.5, but the respective contamination conditions were unresolved. The source permits those factors to apply based on contamination severity; no final multiplied score is claimed. The custom_trigger_tooltip eligibility wrapper was unresolved. The evaluator reported unresolved trigger inputs including undeclared has_variable, undeclared numeric variable cbrn_chemical_contamination (twice), and the compound custom_trigger_tooltip.

Other file candidates had base scores of 4 for cbrn_choose_retaliation_only, 0 for cbrn_choose_battlefield_authorization, and 0 for cbrn_choose_unrestricted_authorization; their conditions/modifiers were not fully evaluated. These are score traces only, not click or selection probabilities.

Source review found the pre-patch assignment trigger required Political Power 5, Command Power 4, decontamination equipment 40, masks 100, support equipment 20, motorized equipment 2, and fuel 300. The completion effect debited all seven. AI weight itself is score logic; stockpile values act through eligibility, not as a continuous AI score modifier. Thus inventory-threshold changes cannot be judged from the returned score trace.

The scripted motorized debit helper consumes motorized_equipment_0 before motorized_equipment_1; the availability trigger checks the motorized_equipment archetype. The analyzer does not model variant-level inventory, so a model-0-only gate or payment is not established.

## Requested inventory boundary scenarios and limits

The exact fixture intentionally does not invent state bindings or custom trigger inputs. The connected adapter/skill contract supports the declared scenarioSet schema with primitive state and scope data, but provides no typed country stockpile/equipment-inventory bindings for these Clausewitz gates, and it left compound custom_trigger_tooltip and the contamination variable unresolved.

Accordingly, the following requested boundary values were not executed as engine-bound scenarios and remain unresolved: decon equipment 39/40/41; fuel 299/300/301; masks 99/100/101; support equipment 19/20/21; motorized 1/2/3; model-0-only motorized stock. The only evaluated scenario is the explicitly named unbound baseline above. This handoff does not claim those thresholds pass, fail, or change rankings. The parent asked to stop further baseline sweeps after this partial fixture; a later post-change same-scenario compare is a separate task.

## Decision structure and risk notes

The pre-patch decision is visible after cbrn_milestone_theater_exploitation, targets a state, requires the country’s active decontamination corridor and no existing assignment lock, and uses state and country custom triggers for eligibility. On completion it sets the 28-day assignment flag and invokes a state-scoped pay/apply effect. Resource availability gates, state eligibility, actor/target scopes, and contamination severity are external conditions that were not fully supplied to the analyzer.

No dominance, starvation, rank reversal, repetition, or exploit conclusion can be made from this partial score-only evaluation. The evaluator did not normalize the scores, model a complete live decision pool, or evaluate whether any candidate was eligible. Static bases 40, 4, 0, 0 alone do not prove that the target is selected more often.

## Parent design note (not a reviewed post-change result)

The parent’s later refinement is to drop the 5 PP payment, retain only three consumed payments (4 CP, 40 decontamination equipment, 300 fuel), and retain 100 masks, 20 support equipment, and 2 motorized as non-consumed availability requirements. This is a pending parent implementation decision, not represented in the baseline fixture or evidence, and was not compared here. It also addresses the native decision cost budget noted in the offline wiki/vanilla docs: seven native cost entries exceed the four-entry native budget. Offline Decision modding review also noted that custom_cost_text may replace native cost presentation, so the parent plans three custom payments rather than native costs. Do not treat that implementation choice as validated by this baseline.

## References read

- Repository AGENTS.md; .agents/skills/chaos-redux-subagents/SKILL.md; .agents/skills/chaos-redux-decisions-missions/SKILL.md.
- Offline wiki core pages in paradox_wiki/: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding; plus Decision modding cost/AI material.
- Vanilla documentation: documentation/triggers_documentation.md, documentation/effects_documentation.md, documentation/modifiers_documentation.md, and common/decisions/_documentation.md (installed game root: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/).
- No game launch was performed.

## Skipped analyses and remaining blockers

- hoi4.probability_sweep: skipped because no faithful typed inventory or compound-trigger scenario binding is available; threshold results would be invented. Parent explicitly requested no more baseline sweeps.
- hoi4.probability_compare: not part of this baseline; parent will request a separate post-change comparison with the same named scenario fixture.
- hoi4.probability_simulate and hoi4.probability_sequence: not appropriate without declared uncertain inputs or a complete pool/cadence/state-transition model.
- Standalone render retry: attempted and blocked by server-process cache mismatch as documented above; evaluation returned ranking and unresolved render artifacts.
- Unresolved: complete live candidate pool, country and target eligibility, external country/war/idea scopes, contamination variable values and severity, all requested resource boundaries, motorized model-level stock, and any ranking/selection probability.

