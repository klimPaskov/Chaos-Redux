# Event 006 decision route audit — IW-093/IW-098 — 2026-09-19

Status: NO-CHANGE / DESIGN BLOCKER. This is a read-only audit of the six Event 006 route conference decisions and their active-origin/pre-event gates. No gameplay, AI, localisation, GUI, or cost source was changed.

## Scope and references

Audited ids: independence_wave_iw093_royal_confederacy_conference, independence_wave_iw093_constitutional_cabinet_conference, independence_wave_iw093_veterans_emergency_conference, independence_wave_iw098_sultanic_federal_compact, independence_wave_iw098_northern_constitution_compact, and independence_wave_iw098_frontier_command_compact.

Primary source: common/decisions/006_independence_wave_iw093_iw098_decisions.txt (IW-093 route conferences at lines 100–310; IW-098 compacts at lines 697–880 in the audited checkout).

Gate source: common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt (is_independence_wave_iw093_country and is_independence_wave_iw098_country at lines 180–188, route locks at lines 216–266) plus common/scripted_triggers/006_independence_wave_triggers.txt (is_independence_wave_event6_local_content_active at lines 20–23).

Category source: common/decisions/categories/006_independence_wave_categories.txt (IW-093/IW-098 category visibility at lines 395–410).

Lifecycle source: common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt (setup-complete flags after package attestation/proofs and cleanup at lines 574–715 and 784 onward).

Accepted design sources: docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md, docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026-07-18.md, docs/events/006_independence_wave/systems/iw093_iw098_signature_packages.md, docs/plans/006_independence_wave_plans/006_source_of_truth_map.md, and the latest cost blocker docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw093_iw098_route_cost_contract_blocker_2026-09-13.md.

Syntax and behavior references: the required offline Paradox wiki decision/effect/trigger/localisation/scope/data-structure pages, vanilla HOI4 documentation under C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/, and vanilla timed decision precedent C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/BOL.txt.

## Severity-sorted findings

### P1 — unresolved accepted-design conflict: flat PP route cost

006_independence_wave_spec_part_3_mechanics_and_decisions.md has a generic rule that major families should not use one flat political-power cost, while the accepted IW-093/IW-098 route contract explicitly defines a 70-day conference/compact with 100 political power. The current source uses cost = constant:independence_wave_iw093.conference_political_power_cost or cost = constant:independence_wave_iw098.conference_political_power_cost, with both constants equal to 100 in common/script_constants/006_independence_wave_constants_registry.txt at lines 5403 and 5453.

The veterans route additionally has the accepted 50 command-power custom row and paid ledger, but the other five routes have no accepted replacement material/resource family or amount. Removing native PP, guessing a replacement, or changing payer/payment timing would change the accepted contract and could create a free-action or double-payment defect. This remains the exact blocker recorded by the 2026-09-13 cost handoff; no source-safe gameplay patch is authorized.

### P2 — probability evidence is structurally incomplete

The required named route chaosx_ai_probability_auditor is not callable in this runtime. Direct hoi4_probability_inspect was used only for structural evidence and is not a substitute for the named auditor.

For common/decisions/006_independence_wave_iw093_iw098_decisions.txt, adapter decision_ai_will_do discovered zero decision candidates and reported the source as exposing 18 mission_ai_will_do candidates; the mission adapter inspected 18 candidates but had poolComplete=false, zero available candidates, and 12 required inputs. Therefore no numeric AI balance claim or probability compare is made, and no AI weight is changed.

Direct evidence artifacts: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35ed3dc9d04f6e65594bd769cac2b83f92071bac480e61e46db4a36542e1070a/6fbe829b2f02e772065ba0bc8bc1db6bd212894ddbf920aea8645843d4903af7/probability-inspect-2fbba302b4edbb6f28af31c7ef3640368389ffa03230f3ad3b03cd300ae2b75c.json and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18e1ca2657729c76a4e8553b61a1390403fa36025e39583620e51e5d220a7625/b854819261230faf86741c4b9d3df3f699d98f9f46941094646bfd46b6acc16b/probability-inspect-2fbba302b4edbb6f28af31c7ef3640368389ffa03230f3ad3b03cd300ae2b75c.json.

### P3 — no active-origin or pre-event gate defect found

Each category requires is_independence_wave_event6_local_content_active, the package-specific country predicate, and the package setup-complete flag. Each decision repeats the package-country predicate in visible, available, completion, cancellation, and cleanup paths. The package-country predicates require active Event 006 origin, the correct package id, and setup completion; prepared-only origins cannot satisfy them.

The six route helpers also require the active package predicate, mutually exclusive route flags, and a compatible government-route value. IW-093 veterans and IW-098 frontier additionally require severe host threat. No pre-event setter for the six unlock flags was found; focus effects set them only after the active package surface exists, and package cleanup clears them.

The setup effect uses prepared-scope checks internally, but it sets *_setup_complete only after active-package identity, runtime attestation, capital/host proofs, and content initialization succeed. Adding a second attestation check to every decision would duplicate the lifecycle boundary without fixing a demonstrated defect.

## Decision category lifecycle notes

The six entries are ordinary timed decisions rather than separate mission objects. Starting one consumes native PP immediately, starts the 70-day timer, sets the package conference/compact active flag, and records the start tooltip. Completion locks the selected route and records success when the route basis still holds; failed completion records failure when the route basis is lost. Cancellation closes the active state and records a terminal cancellation without refunding the committed payment.

Each package allows at most one conference/compact at a time through its active flag. Opposing route flags are excluded in availability and route helpers, so a completed route cannot be reopened by another route decision. Package cleanup clears active, terminal, route, setup, attestation, and package variables.

## Cognitive-load notes

Each IW-093/IW-098 category exposes three primary route actions, below the six-action ceiling; the surrounding package category contains other preparation actions but does not create a duplicate conference tab or passive PP store.

There is at most one active route timer per package, and the active flag prevents concurrent route sessions. The visible package values are named balance/authority/compact/threat values with route thresholds explained by the decision descriptions and custom tooltips.

The route descriptions are concise and the start/success/failure/cancel tooltips explain duration, commitment timing, route consequence, and refund behavior. There is no raw wall of dynamic numbers in these six entries, and the only custom spendable row uses a texticon.

## Mission-quality notes

These are timed decisions, so the mission fields below describe the equivalent lifecycle contract.

| Id | Owner/category/region | Requirement and duration | Success/failure/cancel | Duplicate risk |
| --- | --- | --- | --- | --- |
| independence_wave_iw093_royal_confederacy_conference | IW-093 Asante package; West/Central Africa; DOX state 274 | Active IW-093 origin, setup complete, focus unlock, traditional/undecided government route, no other conference; 70 days | Locks royal route and records success if route basis remains; otherwise terminal failure; route loss/country loss cancels without refund | Active flag and route locks prevent parallel/reopened conferences |
| independence_wave_iw093_constitutional_cabinet_conference | IW-093 Asante package; West/Central Africa; DOX state 274 | Active IW-093 origin, setup complete, focus unlock, constitutional/undecided route, no other conference; 70 days | Locks constitutional route and records success if route basis remains; otherwise terminal failure; route loss/country loss cancels without refund | Active flag and route locks prevent parallel/reopened conferences |
| independence_wave_iw093_veterans_emergency_conference | IW-093 Asante package; West/Central Africa; DOX state 274 | Active IW-093 origin, setup complete, focus unlock, emergency route, severe host threat, 50 command power, no other conference; 70 days | Spends native PP plus command commitment, then records veterans success only while severe threat remains; otherwise terminal failure/cancel without refund | Active flag plus paid ledger prevents duplicate command payment |
| independence_wave_iw098_sultanic_federal_compact | IW-098 Sokoto package; West/Central Africa; SOK state 902 | Active IW-098 origin, setup complete, focus unlock, traditional/undecided route, no other compact; 70 days | Locks sultanic route and records success if route basis remains; otherwise terminal failure; route loss/country loss cancels without refund | Active flag and route locks prevent parallel/reopened compacts |
| independence_wave_iw098_northern_constitution_compact | IW-098 Sokoto package; West/Central Africa; SOK state 902 | Active IW-098 origin, setup complete, focus unlock, constitutional/undecided route, no other compact; 70 days | Locks northern constitutional route and records success if route basis remains; otherwise terminal failure; route loss/country loss cancels without refund | Active flag and route locks prevent parallel/reopened compacts |
| independence_wave_iw098_frontier_command_compact | IW-098 Sokoto package; West/Central Africa; SOK state 902 | Active IW-098 origin, setup complete, focus unlock, emergency route, severe host threat, no other compact; 70 days | Records frontier success only while severe threat remains; otherwise terminal failure/cancel without refund | Active flag and route locks prevent parallel/reopened compacts |

## Cost and requirement clarity

The five non-veterans routes have one native spendable type, political power, shown by the engine’s native cost row. The veterans route has two spendable types, native political power plus custom command power, and its custom row is £command_power [?constant:independence_wave_iw093.veterans_command_power_cost|0] in localisation/english/006_independence_wave_iw093_iw098_l_english.yml.

All six routes are within the four-spendable-type cap, have no hidden fifth cost, and keep non-consumed requirements separate in available and custom cost triggers. The current localisation covers title, description, start, success, failure, cancel, and the veterans custom-cost triplet; no icon-first cost gap was found.

## AI validity and route-lock notes

The six ai_will_do blocks use low default values plus route-specific factors tied to balance, host settlement, or severe threat. The route triggers require a live package country and compatible government route, so no dead-country target or closed route is selected by the source logic.

The named AI/probability auditor and typed scenario evidence are unavailable, so AI weight validity is not certified beyond static source review. No AI patch or probability compare was run.

## Localisation and tooltip gaps

No source-safe localisation gap was found. The five native-PP entries explain the 70-day duration and native political commitment timing; veterans additionally explains command authority. Failure and cancellation text explicitly states that commitments are not returned.

## Cleanup and exploit-risk notes

The route timers set their active state only after payment initialization, clear it on completion, cancellation, or failure, and use terminal route flags to prevent repeat route execution. Veterans closes its paid command ledger on every terminal path. Package cleanup clears decision content and route/setup state. I found no free unit loop, equipment farming, war-goal spam, refund loop, or cooldown bypass in the audited six entries.

## Recommended fixes

1. The parent/design owner should resolve the generic no-flat-PP rule against the accepted IW-093/IW-098 100-PP conference contract by either recording a narrow accepted exception or supplying an exact replacement spendable family, amount, payer, and payment timing. No agent should guess this target.
2. If a replacement cost is accepted, update all six available/cost/complete_effect paths and matching localisation while preserving the 70-day route lifecycle, veterans ledger semantics, and no-refund terminal behavior.
3. Once the weighted source is complete and a named chaosx_ai_probability_auditor route is available, run baseline and same-scenario probability comparison for the six route weights before changing AI factors.
4. No GUI worker or GUI inspect/render is required for this ordinary decision category; these entries do not introduce a dedicated scripted GUI.

## Validation and handoff

Static review covered the six decision blocks, constants, route predicates, event6 active-origin triggers, category visibility, package setup/cleanup, focus unlock setters, localisation, accepted specs, source-of-truth map, and latest cost blocker. The offline wiki and vanilla documentation were consulted, and BOL.txt provided a vanilla timed-decision precedent for native PP plus a 70-day timer.

The read-only HOI4 probability inspection produced the two artifacts listed under P2, but no evaluation, sweep, simulation, or compare was meaningful because the package pool had no available candidates and 12 required inputs were unresolved by the adapter contract. Live gameplay validation was not run by the agent.

Changed files: this handoff only, docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_route_audit_2026-09-19.md.

Changed gameplay ids: none. Before and after behavior: unchanged.

Remaining blockers: the accepted PP-versus-no-flat-PP design conflict, unavailable named probability auditor, and incomplete weighted-source scenario inputs. No simplification or unapproved fallback was used, and no plan handoff beyond this audit was written.
