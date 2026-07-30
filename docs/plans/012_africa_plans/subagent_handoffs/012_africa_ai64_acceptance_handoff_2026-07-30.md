# Event 012 Africa AI 64-profile acceptance handoff — 2026-07-30

## Scope and status

This handoff covers the bounded acceptance repair for the exact 64-row Africa AI profile registry, with ownership limited to profile activation guards and the 64 AI acceptance-ledger rows.

The source defect was stale profile layering after world_end: the common validity guard intentionally permits world_end_africa_the_world, but preterminal host, relationship, foreign, high-chaos, and external-world profile families were inheriting that allowance.

The repair is source-only and does not change the terminal late-action path, the RSA branch, focus-plan payoff factors, profile constants, profile loaders, action dispatch, world-order lifecycle, or readiness flags.

No fallback, substitute model, or gameplay simplification was introduced.

No commit was created because the parent agent owns the final Event 012 integration commit.

## Helper map

| Helper or surface | Scope | Inputs | Output | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| africa_ai_preterminal_host_profile_base_is_active | Country scope on the current host | Existing africa_ai_host_profile_base_is_active result and world_end global flag | Boolean activation result | None | Nine regional overlays, seven constitutional routes, and 22 full-host playbooks in 012_africa_ai_profile_triggers.txt |
| africa_ai_member_profile_base_is_active | Country scope on relationship targets | Existing relationship target, africa_host event target, and world_end global flag | Boolean activation result | None | Seven member relationship predicates |
| africa_ai_foreign_profile_base_is_active | Country scope on external action targets | Existing external target, host event target, chaos exclusions, and world_end global flag | Boolean activation result | None | Five outside-power predicates |
| africa_ai_chaos_profile_base_is_active | Country scope on Evolution III actors or ecological sites | Existing actor/site flags, Evolution III flag, and world_end global flag | Boolean activation result | None | Six high-chaos predicates |
| africa_ai_world_profile_base_is_active | Country scope on external world-order actors | Existing world-order-open flag, external target, and world_end global flag | Boolean activation result | None | Six external-continent predicates |
| africa_ai_profile_world_africa_world_is_active | Country scope on the current African host | Existing host base, world-order/terminal flag, Africa-one flag, authority, burden, and viability-review guard | Boolean activation result | None | Profile 42 only; deliberately retains the terminal world_end_africa_the_world exception |

The base helper is intentionally separate from the terminal exception so Actions 90–92 can retain their existing late-action behavior without reactivating stale preterminal layers.

## Constants and tuning plan

No new constants were required.

The existing africa_ai_profile registry, 64 africa_ai_policy_profile vectors, risk ceilings, partial tolerances, retry stances, controller factors, and 14 MTTH context factors remain the single tuning surface.

No weights were changed, so the accepted nine overlay-capstone factors in 012_africa_focus_plans.txt remain intact.

## Event-target and cleanup plan

No event target was added or removed.

The existing africa_host target and bounded policy snapshots remain the source of host persistence.

The terminal guard prevents new registry layers from being merged after world_end; existing lifecycle cleanup and late-action terminal handling remain parent-owned surfaces.

## Migration from duplicated logic

Profile refresh and merge code in 012_africa_ai_profile_effects.txt continues to call the same 64 activation predicates, so no dispatcher migration was needed.

All nine overlay, seven route, and 22 host-specific predicates now share the preterminal helper instead of repeating a direct host-base call.

Member, foreign, chaos, and external-world families retain their existing family-specific predicates while inheriting the direct terminal guard at their base.

The Africa-world terminal contender remains on the original host base and is not migrated to the preterminal helper.

## Coverage and bounded validation

The matrix contains exactly 64 profile rows, with family counts of 9 regional overlays, 7 constitutional routes, 8 member relationships, 5 foreign powers, 6 high-chaos profiles, 7 world profiles, and 22 full-host playbooks.

Source checks report 64 policy blocks, 64 apply/loaders, 64 activation predicates, 38 preterminal host call sites, and the previously audited 102 prepared action profiles across early and late dispatch.

Static state checks cover a nonterminal-valid branch and a world_end-invalid branch for every preterminal family, while profile 42 retains its explicit terminal branch.

The RSA-integrated Profile 63 South Africa path remains guarded by the RSA eligibility helpers and maps to the existing south_africa host playbook and southern overlay.

The W0–W4 world-order package surfaces remain unchanged; only stale external-world profile activation is blocked after terminal world end.

## Read-only probability evidence

Decision-surface inspection after the patch found one complete decision candidate and four required runtime inputs, with no source diagnostics: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d20a4464b431e31de31553b2e9c632d7be166265020ab978e91cd699a475ee0/a50cd843bab22d2e0bf52e43ff718b92f7171a7bae3c2eca9d0252868c7a1a64/probability-inspect-a580282405cc.json

Focus-surface inspection found 276 candidates and eight required scenario inputs, with the complete-pool requirement visible: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23b48b861b5dd313d8b01753d4f50180fc657e8687c69e8ce191bf9dc4314e72/97e80ca03b68179e9be95ba280726a99186e38e863e11fc4be925eec1113d27d/probability-inspect-707bc0290c2b.json

The bounded focus evaluation used normal-host, terminal-host, and non-AI scenarios and four representative focus candidates, returning partial analysis with raw score ordering, 12 candidate traces, and four unresolved external-factor items: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0040a641549e46ed376338ebba919a7c6c6b11570cc5985707988dfd85174de5/36567dd85676844845b6340f5d3d0857da7c6717f486d6f81b9ce20cc01f2feb/probability-aa2c499175371ac0cd74a3e9.json

The bounded decision evaluation used the same three state classes and returned partial analysis with no eligible controller outcome because helper inputs such as event_target:africa_host, has_variable, check_variable, and is_ai were unresolved in the adapter scenario: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9230d2758e93dd518a65b43c4796d83361ce227df729f28cf94396ae251318c7/daa9d900191f401615d40f002e2769091d480984e2cf5e09c05aa8b66cee021e/probability-3d429e3a0495de6b00a75e5a.json

A declared six-family custom-pool sequence was run with seed 64 and 1,000 samples for rank and starvation sensitivity only; it is not a gameplay probability claim because the manifest is synthetic and no transition semantics were declared: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b366da21099accd4293b28b4e0dc4ac1864b7d4b1a2504a04315180f5f5c17cc/af4aac8cfa1419d0f1bb54ae130f57f4e80844c27d4a97096aab0bc2fc54118a/probability-2a9440271902f32585d5fc75.json

The MCP focus and decision adapters do not prove live campaign behavior or normalize decision scores, and the sequence adapter reported bounded-beam omitted probability for the six-family manifest.

## Skipped validation and limitations

No Hearts of Iron IV executable or live campaign was launched because live consumer validation belongs to the user.

No exact per-profile action probability or campaign balance claim is made; the adapter cannot resolve the complete focus strategy/prerequisite factors or the decision helper state from these bounded scenarios.

No new model consumer was introduced, and profiles 16 and 30–35 retain their existing explicit gate requirements.

The 64 ledger rows remain blocked pending campaign simulation, independent scenario audit, and balance review even though the terminal-layer source repair is complete.

## Changed files

- common/scripted_triggers/012_africa_ai_profile_triggers.txt — added the preterminal helper and terminal guards.
- docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv — updated exactly 64 ai_profile rows with family-specific bounded-state evidence and MCP artifact limits.
- docs/plans/012_africa_plans/subagent_handoffs/012_africa_ai64_acceptance_handoff_2026-07-30.md — this handoff.

The constants, scripted effects, MTTH profiles, and focus plans were inspected but not changed in this bounded repair.
