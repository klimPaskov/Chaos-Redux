# Event 021 AI Probability Audit Handoff — 2026-09-06

Status: bounded read-only audit, MCP partial, no gameplay files edited, no live HOI4 evidence claimed.

This handoff records the current checkout and the MCP evidence obtained on 2026-09-06 for Event 021 Random Civil War and its weighted integrations.

The audit is intentionally closed with unresolved results where the installed MCP adapter did not expose a complete pool, required dynamic state, supported helper trace, or stable structural route.

## Audited surfaces

The primary event surface is `events/021_random_civil_war.txt::chaosx.nr21.1`, which dispatches to `event021_parent_dispatch_opening` in `common/scripted_effects/021_random_civil_war_parent_effects.txt`.

The weighted and probability-bearing identifiers reviewed were `event021_parent_prepare_target`, `event021_prepare_archetype_weights`, `event021_parent_select_archetype`, `event021_prepare_opening_severity`, `event021_parent_roll_strange_incident`, `event021_prepare_recurrence`, `event021_parent_global_scheduler_pulse`, `event021_global_review_current_country`, `event021_parent_prepare_scenario_country`, `event021_parent_commit_scenario_country`, and the shared `individual_crisis_apply_candidate_ticket_curve`.

The integration surfaces reviewed were the Event 006 adapter registry and admission triggers, the Event 004 Random War sources, the Event 007 Fury sources, the Wars cluster member registry, the triggerable-scenario registry, and the shared individual-crisis load contract.

The matrix scenario IDs covered by this handoff are `TGT-01` through `TGT-10`, `ARC-01` through `ARC-08`, `SEV-01` through `SEV-06`, `EVO1-01` through `EVO3-02`, `FRT-01` through `FRT-05`, `SPN-01` through `SPN-05`, `STR-01` through `STR-05`, `SET-01` through `SET-06`, `REC-01` through `REC-06`, `GLB-01` through `GLB-07`, `CLU-01` through `CLU-05`, and `SCN-01` through `SCN-07`.

## Required references read

The repository instructions were read from `AGENTS.md`.

The applied repository skills were `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-event-planning/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.

The Event 021 specification and matrix references were `docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md`, `021_random_civil_war_spec_part_1_core.md`, `021_random_civil_war_spec_part_2_targeting_and_baseline.md`, `021_random_civil_war_spec_part_8_cluster_scenario_ai_balance.md`, and `021_random_civil_war_spec_part_10_acceptance_and_implementation_handoff.md`.

The shared targeting references were `docs/systems/event_system/individual_crisis_targeting.md` and `docs/systems/event_system/triggerable_scenarios.md`.

The required offline wiki pages read were `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

The installed vanilla references read were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, and `script_math_functions.md`, plus `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`.

The references establish that `ai_will_do` and `ai_chance` are scores or proportional option weights over a valid competition, MTTH is a timing distribution, `random_list` is proportional only over the positive entries in the evaluated list, and a generic event selector requires the complete active candidate pool before an event-level probability can be stated.

## Current source hashes

These are local checkout SHA-256 values captured before writing this handoff.

| Source | Local SHA-256 |
|---|---|
| `events/021_random_civil_war.txt` | `127d20f82d9893bd912a4b68484487433cbd6ef384c5375c1ed52e4cfe9aad26` |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `be9e51f4923f6d5be3bbffb548fb3e73fcba2e859c6e6040c80bfc8a745b4787` |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` | `86b514f200242fafe2ff096b9a5bb239c4c2574db2dfb434be1d2b76a0ef2635` |
| `common/scripted_effects/021_random_civil_war_effects.txt` | `fee5eea47a8c9597125bd9d4e0e257163ca72874cb10968127c22a21f10448b8` |
| `common/scripted_triggers/021_random_civil_war_triggers.txt` | `2587a21b168069e6ded0511e878531139e997582a0277bef8046d2058d78e139` |
| `common/mtth/021_random_civil_war_mtth.txt` | `6a8c516e1a2625f3534995f6744ed373e5803ac981fd139ea95787f07b9ea71f` |
| `common/decisions/021_random_civil_war_decisions.txt` | `a26f67e5ceeb80eb5bf26b431c0a51d86a26a0c93b82c77b52044b2d09a19e14` |
| `common/ai_strategy/021_random_civil_war_ai_strategy.txt` | `6adbb93b2cd17665c4bd967368f08bc953738d81db7a2069171241f45c309dca` |
| `common/script_constants/021_random_civil_war_constants.txt` | `b02ae147ce8ce700792c2b9110d0bf34d5c65d1403ba15f685a968d8c1d09ec1` |
| `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` | `56031881c70b613843e8a87e45ecabb51901555e4a039b14707a96dfcf25794b` |
| `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt` | `3dde81d9845c74fef57d8d089256a69d682d4a937ce410d19600b34dfadcefc7` |
| `events/004_random_war.txt` | `3238cd32dee9df983e063331ccd33d458b7c46cdb0745e7c33dac8bdb7e9ce29` |
| `common/scripted_effects/004_random_war_effects.txt` | `1527c5e02297fdc6f115fc4b70fdbc9a9e1443fabeda8fd6590e1c6439c62bbd` |
| `common/scripted_triggers/004_random_war_triggers.txt` | `536f47bc1bff39aaf73fcd0752847e4d44111a5911e6580f4ab787c623ac966c` |
| `events/007_fury.txt` | `ce958b29b1505147c52cee1dd0711ea630a5ea6e1a2cf8e818f994dd67831ec9` |
| `common/scripted_effects/007_fury_effects.txt` | `73b18883e67b12564f30360a7bc0599bc5e9bc7c6718d2b4417cc12fcb3802c1` |
| `common/scripted_triggers/007_fury_triggers.txt` | `0ab3cd76d9cff7613694a31caa27a6f744cb7ca88c08e6cbe5df6dd3d88f3550` |
| `common/decisions/007_fury_decisions.txt` | `3dc14d6c408880f561bcd5c552b98e980e2c63233610fce80f7077fc9e20b679` |
| `common/script_constants/007_fury_constants.txt` | `1af7b847a5ab05ee1df56d938974347774305c149ecf52b5a6ae7d314500d740` |
| `common/on_actions/007_fury_on_actions.txt` | `bc61168f55e43cd4976b2d9b01d1254c9b532eb0a75a47a110fe2139e8bbca7f` |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562c1dc27bf9367e5a8ab8a807047a798fb16de0bd8e1df2841b6a2c40b16` |
| `common/scripted_triggers/individual_crisis_targeting_triggers.txt` | `af537f93e969948ca5cb35e1d06c504f6797ccbaaf659a13c9a661db8e510b70` |
| `common/script_constants/individual_crisis_targeting_constants.txt` | `8b4471a8412e3a883570743e0ee17037129dceaa889d63781ac8fc2c3529e002` |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | `cb8b1d2039b947a37185e7fc04da6aa84bd13ef3d647306fdf2a40bc4494fbfe` |
| `common/script_constants/event_cluster_constants.txt` | `f21f0091643b127856ae936ec65c90a5f698fd4ca724b6ad6611dc36134545c5` |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | `b3aad10569c3d47e40163dfa64a0106859cfb35fc20b32c908df41a042fd3a0f` |
| `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt` | `ab0ef42e20929468be35c270f9872d818432e275e05457c6d218ea6eb8b91392` |
| `common/script_constants/chaosx_triggerable_scenarios_constants.txt` | `87d4716be8d675167b8cf57ee316df718b91181513090d10b9b49a10fd31ce66` |

MCP `sourceRevision` and `sourceHash` values below are preserved exactly as returned by the service and are not assumed to be raw local SHA-256 values.

## MCP workspace and inspect receipts

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The required first live probability call was:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "custom_weighted_pool",
  source: { path: "common/scripted_effects/021_random_civil_war_parent_effects.txt" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=false`, `candidates=0`, `availableCandidates=0`, `requiredInputs=0`, and `unresolved=0`.

The MCP source revision was `2b07f5480cce52f51b0b2c4816568c3e5738bb8e2fd6bad2c148435d0e5536af`, the MCP source hash was `f38a5c004f3505025f7d8368f33906565b1ed3773e2350396525d11b082ef748`, and the artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81be86fef0b59521ddbcabe8a7e13e8c393a8b3da0a8bacc8d1f4727bf0a1e00/7f2db01ed67f854f3f64922ee9e828796c6b2cf87e14f9ac9bc22a8024387ad6/probability-inspect-f38a5c004f35.json`.

The result means that the custom adapter did not discover a complete target pool in the current parent-effects source; it does not prove that the runtime country pool is empty.

The remaining successful inspect calls were:

| Surface | Exact inspect result | MCP source revision | MCP source hash | Artifact | Pool result |
|---|---|---|---|---|---|
| Event 021 decisions, `decision_ai_will_do`, `common/decisions/021_random_civil_war_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED` | `f2993b1eb4a0f56a2755a847d9dce091acfa1f5f0c07e04f415fa1840ccb5a5a` | `f737e27647ca83d358f7878de14c5df11f9dae729264b141706b069051609385` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c803e36c71647dc0c0e123e8eb4f36b021303a63bf23cbf02b48129a9bb68681/1bce8b162e24e52f883de189db3b1bc72322356700b41133c6b389a59934a709/probability-inspect-f737e27647ca.json` | 18 source candidates, `poolComplete=false`, 11 required input families, 0 inspect-time unresolved. |
| Event 021 missions, `mission_ai_will_do`, `common/decisions/021_random_civil_war_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED` | `db6f65264cbc9283de8dd0a87b421e7adb3c5f303bf58929f19012600c767d21` | `f737e27647ca83d358f7878de14c5df11f9dae729264b141706b069051609385` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72f36a3062204c275fccbc48bc248c967690d89fe8c7f7fe48bd6b904704fe78/7480e1a5574f6cc4edbaba1a4cc0fb007c850f5d5f310f4401f4bb5441d44acf/probability-inspect-f737e27647ca.json` | 3 source candidates, `poolComplete=false`, 2 required input families, 0 inspect-time unresolved. |
| Event 021 parent `random_list`, whole source | `PROBABILITY_SOURCE_INSPECTED` | `345d01517d145dd9c7eb4e69c23e9c73444186846b3dfe9966217703725e99cc` | `f38a5c004f3505025f7d8368f33906565b1ed3773e2350396525d11b082ef748` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2e17e090686661ddaecc6f7d7cfce76fa2513e411a5bb58a99434ed406b5b0c/ed022d3115c7cb7f59b2a25311e30b869ca9183b85f05deb641df54d57a19b5c/probability-inspect-f38a5c004f35.json` | 8 aggregate candidates, `poolComplete=false`, 8 required input families, 1 unresolved. |
| Event 021 MTTH, `event_mean_time_to_happen`, `common/mtth/021_random_civil_war_mtth.txt` | `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` | `345d01517d145dd9c7eb4e69c23e9c73444186846b3dfe9966217703725e99cc` | `c55a108bcbf249ce1d76875506cd0fe4b8c8db79646c426b503ba036d72405b8` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4d1957b897a6ffe6598635cb29ebdee5c72906aafbbbe47669bae14cdae5daf/a3d4866634f01fd424bb36be55c3c0b6bb295112a4f508a6223bf9acbf40aafd/probability-inspect-c55a108bcbf2.json` | 0 candidates. This does not prove the source has no MTTH; the adapter did not expose the dynamic entries. |
| Event 021 AI strategy, `ai_strategy_factor`, `common/ai_strategy/021_random_civil_war_ai_strategy.txt` | `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` | `59b51a3aa99361012332e54a444c58bf2c8f18db1d82087d80b41123e28aa128` | `74d73084d977d42abe822021d859cb7b7a075aa89565a9c9dd861c9261b37db9` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/980f0616d293e85b9e5e39da83f41cd1c559d3b047798d880e150ffb05d861c3/d0a23b19d98df9dfade909b5b4c8a3daac407b0f26a299f33974d0e40abee14b/probability-inspect-74d73084d977.json` | 0 candidates. Strategy plan values were reviewed as strategy state, not Event 021 selection probabilities. |
| Event 021 event options, `event_option_ai_chance`, `events/021_random_civil_war.txt` | `PROBABILITY_SOURCE_INSPECTED` | `0e1bcb1f7c44de5660aebacefd130b0ba72e776b746defe09f71c56f12441c14` | `c60040e772dcb4eac72edf27219d495c59299193c5c6f8d3106a3e8a3b463f04` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74b410dc424f01b07826a47e979d2366f57def4b5bcc24f7a5db2648b6462284/c8bcdad18acc77c24adb38e13a303eca6b672f6cd043c480ea12106fda0fb8a2/probability-inspect-c60040e772dc.json` | 11 source options, `poolComplete=false`, 1 unresolved. Each current presentation callback has a single `base=100` option, so this aggregate is not a meaningful multi-option race. |
| Manual scenario registry, `custom_weighted_pool`, `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | `PROBABILITY_SOURCE_INSPECTED` | `345d01517d145dd9c7eb4e69c23e9c73444186846b3dfe9966217703725e99cc` | `572023816aeb91956310786bf8a101c01ff517c5f13537948b437b7018aa6214` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/46400a14222cc157580eddeaaa74c423f3129547df128c83cb3ccb70ce9622b6/7dd08563b414a8b01d77e7cebed659564cee5abcab37739684f781eb43ce8241/probability-inspect-572023816aeb.json` | 0 candidates, `poolComplete=false`. |

An additional `custom_weighted_pool` inspect was attempted against `common/scripted_effects/individual_crisis_targeting_effects.txt` and timed out after 180 seconds with the exact tool error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 180s`.

The narrowed current strange-incident pool at `common/scripted_effects/021_random_civil_war_parent_effects.txt:5203` was also inspected with candidates `5203.entry.1` and `5203.entry.2`, and timed out after 180 seconds with the same exact error.

## Source-level traces and classifications

The following are source facts or score traces only, not live selection probabilities.

### Target score and validity

`event021_parent_prepare_target` calls the core target preparation and then requires `event021_country_can_be_target`, a positive candidate weight, a valid archetype route, and available capacity before marking the target ready.

The current target score starts at `constant:event021_target_weight.base = 10` and adds pressure multiplied by `constant:event021_target_weight.pressure_per_point = 4`, authority-failing `90`, authority-collapse `160`, valid-actor-route `80`, major-stage `50` when the major gate is valid, nearby exposure `60`, subject `20`, and player `25`.

The current target score subtracts recent-target memory `120` and multiplies major-country candidates by `constant:event021_target_weight.major_target_factor = 0.35`, then clamps to the configured `0..1000` range.

The target trigger requires a normal human country, positive controlled territory, no terminal lock, no incompatible bespoke civil-war lock, no active or reserved Event 021 state, no unresolved recent-target cooldown, a below-cap shared individual-crisis load, major eligibility when applicable, and a valid opposition route.

Classification: score-only source evidence for the numeric target trace and unresolved probability evidence for `TGT-01` through `TGT-10`.

The MCP custom-pool inspect did not discover a normalized target candidate pool, so no exact target probability, dominance, starvation, or rank-reversal claim is made.

### Archetype selection

`event021_prepare_archetype_weights` initializes six route weights to zero and assigns the same `valid_actor_route` contribution of `80` to each valid ideological, legal, regional, Event 006, command, and same-tag route.

`event021_parent_select_archetype` uses the six temporary weights in the `random_list` at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070`.

The source therefore exposes a flat valid-route score layer rather than route-specific pressure, scenario, exposure, sponsor, or variety modifiers.

Classification: score-only source evidence for `ARC-01` through `ARC-08`, with unresolved conditional selection probability because the whole-source random-list inspect reported multiple aggregate categorical surfaces and one unresolved input.

Potential tuning risk: if multiple routes are valid, the current source gives them equal positive weights, so route identity may be determined by eligibility and the random draw rather than by route-specific strength.

### Severity

`event021_prepare_opening_severity` defaults to Limited, raises to Serious for exposed pressure or a serious opening, raises to Severe when major severity is allowed and pressure is fractured, and raises to Critical when major severity is allowed and pressure is critical.

The same helper forces Limited for the one-state route.

Manual scenario intensity maps Low to Limited, Medium to Serious, High to Severe, and Maximum to Critical in `event021_parent_prepare_scenario_country`.

Classification: exact deterministic source branch evidence for the severity mapping, not a probability result, and unresolved for `SEV-01` through `SEV-06` because the dynamic pressure, authority, major-stage, and route fixtures were not evaluated by MCP.

### Evolution timing, exposure, and sponsor

The MTTH file contains `random_civil_war_evolution_i_days`, `random_civil_war_evolution_ii_days`, and `random_civil_war_evolution_iii_days`.

Evolution I uses an authority-failure factor, large-country factor, extra-actor factor, near-defeat factor, settlement-progress factor, and no-extra-actor factor.

Evolution II uses border-route, sponsor-route, Event 006 independence-front, multi-front, settlement-progress, strong-neighbor, and no-exposure factors.

Evolution III uses a severe-war factor when opening severity is Severe or Critical.

The bounded parent scheduler samples a stage date once, clamps it to the configured 60–180 day window, stores an absolute due date, and processes the date through `event021_parent_process_evolution_schedule`.

`event021_parent_propagate_exposure` and the target score's nearby-exposure contribution connect active fronts to later target pressure, while sponsor and mediator state are represented by route flags and commitment variables.

Classification: bounded source design only for evolution scheduling and exposure propagation, unresolved MTTH timing for `EVO1-01` through `EVO3-02`, `TGT-07`, and `SPN-01` through `SPN-05`.

The MTTH adapter returned no weighted surfaces, so no effective MTTH days, timing distribution, sponsor sensitivity, or exposure rank reversal is claimed.

### Recurrence and settlement

`event021_prepare_recurrence` starts from current pressure, adds memory pressure `10`, failed-settlement pressure `20`, and authority-collapse pressure `10`, and subtracts `20` for government victory or coalition settlement before clamping the recurrence score to `0..100`.

The recurrence trigger uses the configured recurrence threshold `45`, stores a minimum review date of 60 days when valid, and keeps the recurrence window bounded by earliest and latest dates.

Settlement and reconstruction remain prerequisites before cleanup and recurrence review, and successor grace suppresses recurrence eligibility.

Classification: score-only source evidence for `REC-01` through `REC-06` and `SET-01` through `SET-06`, with unresolved recurrence timing and post-settlement competition because no complete state/date fixture or MTTH result exists.

### Global review queue

The bounded scheduler registers four random country samples per pulse through `event021_parent_global_scheduler_pulse` and reviews a configured batch of six registered countries.

Critical countries are queued once through `event021_queue_critical_country`, with a configured critical queue batch of three and capacity, launch-in-progress, terminal, and validity gates.

The queue uses persistent arrays, a cursor, due dates, and a launch lock, but the inspected sources do not provide a complete MCP custom-pool or sequence manifest for the live registry state.

Classification: bounded source structure only for `GLB-01` through `GLB-07`, unresolved queue ordering, cumulative launch chance, starvation, and timing drift.

`probability_sequence` was not run because the required complete registry pool, cadence, cooldown, recovery, cap, removal, reset, timer changes, and terminal states were not supplied.

### Manual scenario and SCN-018 identity

The current constants define `triggerable_scenario_id.random_civil_war = 18` and the current triggerable-scenario documentation names the public row `SCN-018: The Fracture Cascade`.

The current scenario exposes Political Fracture, Independence Cascade, Command Collapse, and Universal Fragmentation, each with Low, Medium, High, and Maximum intensity.

Low, Medium, and High use source shares `0.10`, `0.25`, and `0.50`, respectively, after the eligible normal-human pool is built, while Maximum requests every eligible country.

The manual target path uses `event021_parent_add_scenario_target_to_weighted_pool`, ticket removal, type-specific route preflight, and the same actor, capital, force, reservation, and cleanup proof as ordinary Event 021 setup.

The current implementation source and shared documentation use `SCN-018`, while older Event 021 planning material contains a provisional `SCN-014` identity.

Classification: exact source identity and share constants, unresolved scenario selection and completion for `SCN-01` through `SCN-07` because the custom-scenario inspect returned zero candidates and no live eligible-country pool.

### Wars cluster

The current Wars cluster has cluster id `constant:event_cluster_id.wars = 1` and a member registry row for Event 004 `wars_random_war` as Required/Low, Event 007 `wars_fury` as Optional/Medium, and Event 021 `wars_random_civil_war` as Optional/Medium with row id `constant:event_cluster_member_row_id.wars_random_civil_war = 1003`.

The cluster layer records member eligibility, danger, participation, reservation, collision, cooldown, skip status, and pending queue metadata.

Event 004 has no direct Event 021 weighted reference beyond cluster actor context storage, and Event 007 has no direct Event 021 source reference in the reviewed event, effect, trigger, decision, constant, or on-action files.

Event 004's local option weights are `80/20` for its aggressor response and `70/30` for its target response, but its pair selector is a priority/fallback process over nested country selectors rather than a single normalized pair pool.

Event 007 owns its own weighted actor and target-score system, while the shared targeting trigger counts `is_fury_actor` as one individual-crisis load unit.

Classification: exact source registry facts and comparison-only Event 004/Event 007 score evidence for `CLU-01` through `CLU-05`, with unresolved cluster overlap probability, optional-member participation, collision rerolls, and pacing timing.

No cluster-specific probability inspect was run after the user requested closure because the current cluster registry is not exposed as a complete probability candidate pool and the Event 021 parent inspect had already returned an empty custom surface.

### Shared individual-crisis targeting

The shared load contract sets an active cap of three packages.

The source ticket curve is load zero factor `1.00` and four tickets, load one factor `0.50` and two tickets, load two factor `0.25` and one ticket, and load three ineligible.

The shared trigger counts Event 021 through `random_civil_war_active` and counts Fury through `is_fury_actor` alongside other individual crisis providers.

The Event 021 scenario eligibility trigger also requires `individual_crisis_load_is_below_cap` before adding a country to its manual scenario pool.

The custom-pool inspect against `individual_crisis_targeting_effects.txt` timed out after 180 seconds, so the live candidate pool, external provider flags, ticket allocation, and cross-provider normalization remain unresolved.

Classification: exact source constants and bounded gating structure, unresolved shared-targeting probability for all target, scenario, exposure, and recurrence cases that depend on the shared load.

## Candidate-pool and external-factor completeness

| Scenario group | Candidate pool | External factors | MCP result and classification |
|---|---|---|---|
| `TGT-01`–`TGT-10` | Incomplete; custom Event 021 target inspect returned 0 discoverable candidates and `poolComplete=false`. | Pressure, authority, actor completeness, controlled states, recent-target dates, active wars, incompatible locks, player/AI state, major stage, and shared provider load are not supplied as a complete runtime fixture. | No evaluate, sweep, compare, or exact target probability; unresolved. |
| `ARC-01`–`ARC-08` | Six route weights exist in source, but whole `random_list` inspection found eight aggregate surfaces, `poolComplete=false`, and one unresolved item. | Route flags, Event 006 package identity, same-tag validity, state count, leaders, divisions, and collision state are incomplete. | Score-only source trace; conditional selection unresolved. |
| `SEV-01`–`SEV-06` | No separate weighted severity pool; source branch is deterministic. | Pressure band, authority band, major gate, one-state route, external war, and actor/front count are incomplete. | Deterministic source mapping only; scenario result unresolved. |
| `EVO1-01`–`EVO3-02` | No MCP MTTH candidates were exposed from the MTTH file. | All MTTH flags, thresholds, theatre state, settlement phase, exposure routes, sponsors, neighbors, and severity are incomplete. | No timing evaluation; unresolved. |
| `TGT-07`, `SPN-01`–`SPN-05` | No complete exposure or sponsor pool. | Active-front geometry, neighbor validity, sponsor resources, commitments, recognition, mediation, and caps are incomplete. | No ranking or probability; unresolved. |
| `SET-01`–`SET-06`, `REC-01`–`REC-06` | No complete postwar candidate pool. | Settlement outcome, reconstruction phase, memory, grace period, earliest/latest dates, and target cooldown are incomplete. | Score-only source trace; timing and repetition unresolved. |
| `GLB-01`–`GLB-07` | No complete persistent registry/critical queue pool. | Registration cadence, cursor, queue date, queue budget, capacity, launch lock, removal, reset, and terminal state are incomplete. | Sequence skipped; bounded source structure only. |
| `CLU-01`–`CLU-05` | Wars rows are source-visible, but complete live member availability and cluster candidate weights are not exposed. | Cluster tier, optional participation, cooldown, reservations, collisions, and member skip states are incomplete. | No cluster probability or rank result; unresolved. |
| `SCN-01`–`SCN-07` | Manual-scenario custom inspect returned 0 candidates and `poolComplete=false`. | Eligible normal-human count, route-specific preflight, shared load, reservations, type, intensity, and commit outcomes are incomplete. | Exact source shares only; completion and realized share unresolved. |
| Shared individual-crisis contract | Inspect timed out; no candidate pool artifact. | All provider flags and current load are missing. | Unresolved. |

The auxiliary strange-incident pool is also unresolved in the current snapshot because the whole-source random-list inspect was incomplete and the narrowed current `:5203.entry.1/.2` inspect timed out.

## Probability evaluations, sweeps, compares, and renders

No `hoi4.probability_evaluate` call was issued in this closed audit because every candidate surface that could have supported a meaningful named scenario was either incomplete, empty at the adapter layer, or missing typed dynamic inputs.

Consequently, there are no current `analysisId` values, scenario hashes, exact or bounded traces, normalized probabilities, ranking artifacts, timing artifacts, or result classifications of `exact`, `bounded`, or `sampled` for the Event 021 matrix.

No `hoi4.probability_sweep` call was issued because no complete target, route, MTTH, queue, cluster, or shared-provider pool was available, and the user requested closure rather than waiting for additional runtime evidence.

No `hoi4.probability_compare` call was issued because no owner-applied before/after source state, candidate manifest, or immutable same-scenario baseline was supplied.

No `hoi4.probability_simulate` call was issued because no uncertain input distribution and seed contract was declared.

No `hoi4.probability_sequence` call was issued because the global queue and custom scenario paths lack a complete pool, cadence, cooldown, recovery, cap, removal, reset, and terminal-state manifest.

No probability render artifact exists for this current audit because no current probability analysis completed.

## Structural MCP status

The required structural call was attempted as:

```text
mcp__hoi4_agent_tools__hoi4_event_inspect({
  mode: "trace",
  direction: "both",
  expandHelpers: true,
  maxDepth: 3,
  maxNodes: 200,
  maxEdges: 400,
  selector: { kind: "event", eventId: "chaosx.nr21.1" },
  refresh: true,
  workspaceId: "mod_chaos_redux_ea3b2d67c2c0"
})
```

It failed with the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_inspect; Caused by: timed out awaiting tools/call after 180s`.

No structural artifact, graph revision, or event render was produced.

`hoi4.event_render` was not retried after the inspector timeout because the user explicitly requested finalization without waiting for more runtime evidence.

The structural conclusions in this handoff are therefore source findings only and are not presented as current MCP event-graph proof.

## Findings and risks

The Event 021 target score is bounded in source and includes explicit validity gates, cooldown, major, exposure, subject, player, and route contributions, but MCP did not expose the complete candidate competition.

The six archetype routes have a flat positive contribution when valid, which may create route starvation or arbitrary route dominance when several receipts coexist; this is a source tuning risk, not a measured live result.

Severity is deterministic from pressure and route state rather than a probability race, so claims about severity frequency require campaign timing and state-transition evidence that is absent here.

The Event 006 adapter has an explicit static package allowlist and anchor/package checks, and the Event 021 source has a dedicated Event 006 route, but incomplete package and anchor fixtures prevent proof of exact-zero invalid-package behavior or baseline Event 006 participation.

The manual scenario identity is currently `SCN-018`/raw id `18`, while older planning material contains a provisional `SCN-014` reference; this identity mismatch must remain visible until the owner accepts the current registry as authoritative.

The bounded queue has explicit batch and cursor controls, but its random registration samples, critical queue order, capacity gates, and reset behavior could still produce starvation or timing drift without a complete sequence analysis.

The shared load curve prevents unrestricted stacking in source, but its actual effect on Event 021 target and scenario shares is unresolved because the shared inspect timed out and no provider-state fixture exists.

No exploit is proven by this audit.

Unresolved exploit risks are positive route weight on stale or incomplete Event 006 receipts, target validity at the reservation boundary, repeated queue reviews, scenario target-ticket removal, recurrence re-entry after settlement, and cross-provider load interactions.

## Recommended owner follow-up, not applied

1. Provide a supported MCP custom-pool manifest or adapter mapping for `event021_parent_prepare_target` and `event021_parent_add_scenario_target_to_weighted_pool` that enumerates every candidate and exposes the target score trace, validity gates, reservations, cooldowns, and shared-load adjustment.

2. Provide typed country, state, target, resource, flag, scope, route, package, date, and external-war fixtures for `TGT-01` through `TGT-10`, `ARC-01` through `ARC-08`, and `SEV-01` through `SEV-06`.

3. Re-run the same named matrix scenarios after the owner supplies complete pools, retaining the distinction between score-only `ai_will_do` evidence and probability-proportional selection evidence.

4. Decide whether equal valid-route contributions in `event021_prepare_archetype_weights` are intended, then test route rank reversals with the same complete fixtures before changing any tuning value.

5. Expose the three Event 021 MTTH entries to the MCP MTTH adapter or record a supported helper manifest, then evaluate evolution timing with explicit state transitions and no inferred flags.

6. Provide a complete global registry and queue sequence manifest covering four-country registration samples, review batch six, critical queue batch three, cursor wrap, capacity, launch lock, cooldown, removal, reset, and terminal states before using sequence analysis.

7. Provide a complete Wars cluster member manifest for Event 004, Event 007, and Event 021 at each relevant chaos tier, with optional participation, cooldown, reservation, collision, skip, and pacing inputs before claiming cluster overlap or member shares.

8. Reconcile the current `SCN-018` registry identity with the older provisional `SCN-014` planning reference through an accepted documentation decision before scenario acceptance is reported.

9. Keep all gameplay, AI, event, weight, prerequisite, and tuning changes with the owning implementation agent; this auditor applied none.

## Skipped analyses and exact blockers

The Event 021 target custom pool was not evaluated because `probability_inspect` returned `poolComplete=false` and zero discoverable candidates.

The shared individual-crisis pool was not evaluated because `probability_inspect` timed out after 180 seconds with no artifact.

The current narrowed strange-incident list was not evaluated because its `probability_inspect` timed out after 180 seconds with no artifact.

The decision and mission score pools were not evaluated because their source candidate counts were discoverable but `poolComplete=false`, `availableCandidates=0`, and required dynamic input families were absent.

The MTTH entries were not evaluated because the adapter returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` and zero candidates despite the source containing dynamic MTTH definitions.

The AI strategy factor surface was not evaluated because the adapter returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` and zero candidates.

The event-option surface was not evaluated because the adapter returned an aggregate 11-option view with `poolComplete=false` and one unresolved item, while each current callback event has one base-100 option.

The manual scenario pool was not evaluated because its custom inspect returned zero candidates and `poolComplete=false`.

The cluster probability surface was not evaluated because no complete cluster candidate adapter or member manifest was available at closure.

Structural `hoi4.event_inspect` timed out after 180 seconds, so structural `hoi4.event_render` was skipped under the user's closure instruction and has no artifact.

No live HOI4 launch, save-state acceptance, campaign timing, or runtime log evidence was used.

## Disposition

This handoff is `MCP partial / score-only source findings / unresolved runtime probability / not gameplay complete`.

The only new repository artifact from this audit is this dated handoff file.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, localisation, asset, country, runtime, or tuning file was edited.
