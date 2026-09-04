# Event 016 Mengele Computation special-project probability baseline

Status: prepatch source and scenario baseline secured, MCP result unresolved because no installed probability adapter recognizes native special projects. No gameplay, weight, or balance file was changed. This handoff is not an acceptance claim.

## Audited surface

The bounded surface is `sp_brilliant_scientist_computational_engine` and its unique reward block `sp_brilliant_scientist_computational_engine_reward_unreadable_notation` in `common/special_projects/projects/016_brilliant_scientist_projects.txt`. The two reward option tokens are `sp_brilliant_scientist_computational_engine_reward_unreadable_notation_cautious` (default) and `sp_brilliant_scientist_computational_engine_reward_unreadable_notation_risky`.

The provider gate is `brilliant_scientist_mengele_project_provider_is_valid` in `common/scripted_triggers/016_mengele_project_bridge_triggers.txt`. The computation gate `brilliant_scientist_can_research_mengele_computation_prototype` currently requires that provider gate, no completed computation flag, and either the all-projects or computation-available flag. It does not currently require a provider Theory receipt or an actual active Mengele program.

The provider selector is `brilliant_scientist_record_new_project_prototype` in `common/scripted_effects/016_brilliant_scientist_project_effects.txt`. It routes a valid Mengele provider to `brilliant_scientist_record_mengele_project_prototype`; otherwise it enters the existing Kruger stage path. The bridge computation branch sets `directorate_special_project_computation_completed`, clears its availability flag, and adds `mengele_directorate_computation_prototype`. The bridge source explicitly avoids Kruger stage arrays, capacity, facilities, event targets, evolution, containment, and Singularity state.

The native special project has an empty `allowed` block, an OR of the Kruger and Mengele visibility/availability helpers, a base AI score with a wartime preferred factor and low-capacity cautious factor, and a computation prototype output that sets the family selector before calling the provider selector. The unique reward block has `fire_only_once = yes` and one shared reward weight; its cautious option is `default = yes`, while the risky option dispatches the computation prototype accident after setting the family and prototype-stage selectors. There is no option-local `ai_will_do` or `ai_chance` block from which to infer AI option probabilities.

The parent-planned change is provider-owned Theory prerequisite, independent prototype receipt, no Kruger writes, and provider-specific risky-option incident handling. Those changes remain outside this read-only audit.

## Source provenance retained before owner edits

The captured repository HEAD was `5f31c83ce66f1c00fbf21f7a120f7ba2d1f25d55`.

| Source | Current worktree raw SHA-256 | Git blob at capture | Notes |
| --- | --- | --- | --- |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `e24d19fd70cf52c3374bac1553b83444147f86546db981601c42ae6e3dfbf0dc` | `ab03af00ae2d595d37c64a3ad622c9be1e9443ea` | clean against HEAD |
| `common/scripted_triggers/016_mengele_project_bridge_triggers.txt` | `02649be801e1bdcd9a5054caa4a9cf1299f541c4ad4a7c754287fa711ccc778b` | `d86d64907eceecc79824dffb4b5b4a4ca430ecb9` | clean against HEAD |
| `common/scripted_effects/016_mengele_project_bridge_effects.txt` | `700bf3a191f61a395103b6fb29541de6a1828d55c035dd05d5a2ccd9d874df19` | `e6ab2341181996822fe7fbc3191ee76bc29c81d4` | clean against HEAD |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | `6406e3e8087cd475193a6ca470a81f2976e889a6831098897b9ad334cba349d1` | `388af9db2d1d250e622e74000b1166d52559b461` | provider selector bytes retained; unrelated staged project-stage work has index blob `d15329425736e06f9eb4a3610914005cea8985d6` |

The worktree provider-selector bytes were used for source review and the special-project source evaluation. The staged project-stage changes in the shared project-effects index were not incorporated into this baseline and were not edited.

## Exact durable fixture

The fixture is [E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json](E016_MENGELE_COMPUTATION_BASELINE_2026_09_02.scenarios.json), SHA-256 `3c197628aa74eb4dba902f771ec0eba18e2dcf66cf0b1f886858a5632d5bb99e`. It retains eight named scenario bodies:

- `E016_MENGELE_KRUGER_VALID`
- `E016_MENGELE_ACTUAL_PROGRAM_VALID`
- `E016_MENGELE_NO_THEORY`
- `E016_MENGELE_INACTIVE_PROGRAM_OWNER`
- `E016_MENGELE_LOST_PROJECT_OWNER`
- `E016_MENGELE_BOTH_IDENTITIES_SINGLE_OWNER`
- `E016_MENGELE_SAFE_PROTOTYPE_OPTION`
- `E016_MENGELE_RISKY_PROTOTYPE_OPTION`

The rows declare country identity, current-host and Kruger flags, Mengele program flags, Theory receipt, computation availability/completion, incident and terminal state, project owner existence/activity, resource/capacity inputs, native project identity, and cautious/risky option declarations in state fields. `MCL` and `GER_josef_mengele` are used for the Mengele provider cases; the dual-identity row also declares `brilliant_scientist_current_host` and the Kruger identity to exercise the provider precedence boundary.

The scenario metadata uses the installed schema's `technology_ai_will_do` enum solely because `special_project` is not a valid scenario-set hint. The state fields remain the exact special-project/provider fixture. This metadata accommodation is not evidence that a technology adapter applies to native special projects.

## Mandatory MCP inspect and bounded evaluate

The mandatory source-only `hoi4.probability_inspect` on the special-project source returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, 11 adapters, zero candidates, zero unresolved items, and no available adapters. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb629317338c6d1b1ea76f7feaee8cc07410fa0354f2dbefbb6ab2fc44744b3a/b29b9b28dc20f2fc2af330d53251e7ef576507bc0bb451784a1b8f5e2a539c23/probability-inspect-c5f2cac56da7.json`. It reports source revision `3f2ce2bf5d774617a8d9d158fa294d346f59f9d1673938b7c74e2a20c70e4133` and source hash `c5f2cac56da709f03d31ab07a930341ede188c140555d55ec9bd4453e10ac5cb`.

A second narrow inspect requested `technology_ai_will_do` for the special-project and two option tokens. It returned the same `no_weighted_surfaces` result with zero candidates and zero available adapters. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e012f896d7b6a90d11fbc84f3abd7afc88a2014d81c7ba86a88a5faa32a328b8/8e601847a412a5a5eb38a73bcd0652644c4ca2ac5140f899d5be992791ba233f/probability-inspect-c5f2cac56da7.json`.

One bounded evaluate attempt using the valid `technology_ai_will_do` adapter, the three declared candidate IDs, the fixture, and the asserted special-project source hash returned `PROBABILITY_SURFACE_EMPTY` before analysis. The exact blocker was `No weighted blocks matched this request`; `availableAdapters` was empty for the requested source and the candidate pool was not bound. No artifact, ranking, matrix, normalized probability, or unresolved analysis was produced. A prior schema-only attempt was rejected because `special_project` is not an allowed `surfaceHint` and the fixture's presentation-only `selection` keys are not accepted by the strict scenario schema; those keys were removed and the valid enum retained without changing scenario state bodies.

No special-project research-selection adapter, prototype-option AI adapter, or helper predicate evaluator is installed for this source. `probability_evaluate`, `probability_sweep`, `probability_simulate`, `probability_sequence`, `probability_render`, and `probability_compare` cannot provide valid weighted evidence here. No replacement adapter or hand simulator was invented.

## Source-level boundary findings

The current source conditionally exposes the computation project to either Kruger or Mengele, but the evaluator cannot prove the engine's native project ownership or visibility behavior. The source-level expectations for the retained cases are:

| Scenario family | Current source boundary | Audit classification |
| --- | --- | --- |
| Kruger valid | Native Kruger helper path; Mengele bridge gate is false for the ordinary host | source-bounded, engine unresolved |
| Mengele actual program valid | Current bridge gate can pass from Mengele identity plus availability, even without a Theory check | source-bounded finding, no probability |
| No Theory | Current Mengele helper does not inspect a Theory receipt, so this is a planned prerequisite gap | exact source finding, engine unresolved |
| Inactive program owner | Current provider gate does not inspect active program state, so identity/availability alone can remain sufficient | exact source finding, engine unresolved |
| Lost project owner | No bridge helper checks native owner existence; native special-project ownership semantics are unsupported | unresolved |
| Both identities, one actual owner | `NOT current_host` rejects the provider bridge when the same country is the live Kruger host; the native else path needs separate native gates | source-bounded, engine unresolved |
| Cautious option | Cautious is the default option and applies low progress loss | source-only; no AI option probability |
| Risky option | Risky dispatches the computation accident after setting computation/prototype selectors | source-only; incident outcome probability unresolved |

The shared prototype reward weight is a source-local reward selection weight, not a declared AI candidate pool. The two option blocks have no AI scores, so no safe/risky ranking, normalized chance, repetition rate, or accident incidence can be inferred. The project AI block itself is outside a recognized probability adapter on this source; its base, wartime factor, and low-capacity factor are retained unchanged.

## Recommendations and remaining uncertainty

The owner should add the accepted provider-owned Theory prerequisite and actual-program/owner validity at the shared Mengele gate, preserve an independent prototype receipt, and keep the native provider selector from writing Kruger stage state. Risky prototype incident dispatch should remain provider-specific and should be compared against this exact fixture after the patch. No AI weights or reward weights need adjustment based on this baseline.

The decisive unresolved inputs are native special-project research selection, native project owner identity/loss, `is_mengele_clone_directorate_country`, Theory receipt semantics, and prototype-option selection cadence. The fixture records those inputs for later structural/source review, but it does not convert them into engine truth. No overall Event 016 or Mengele Computation acceptance claim is made.

Skills used: `chaos-redux-events` for native Event 016 project/effect integration, `chaos-redux-subagents` for bounded handoff ownership, and the required weighted-probability MCP workflow. Relevant offline wiki and vanilla documentation were consulted. No gameplay or configuration files were edited and no commit was created.
