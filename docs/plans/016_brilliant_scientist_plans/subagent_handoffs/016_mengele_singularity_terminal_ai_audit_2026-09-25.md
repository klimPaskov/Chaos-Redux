# Event 016 Mengele singularity terminal AI probability audit

**Disposition:** Partial audit completed. The corrected probability inspection and scenario evaluation succeeded; eligibility and historical comparison remain unresolved. No gameplay source was edited, staged, or committed.

## Scope and source revisions

The only weighted surface audited is decision mengele_event016_authorize_singularity_detonation in common/decisions/016_mengele_singularity_terminal_decisions.txt.

Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux  
Git HEAD: 278ecf1a4939b7d473a7ce35a770a0efd3fe884d

| Source | Identifier | Revision |
| --- | --- | --- |
| common/decisions/016_mengele_singularity_terminal_decisions.txt | mengele_event016_authorize_singularity_detonation | MCP source hash f676ea276f035cda6f9706ed91648f212bd3e0b3ba17b552ca2d69f772404855; source revision 87e499a89c643f577479f0c000567a017a674963ab5dfbda88f783fde4301593; local SHA-256 7C3A3B27861C321F0B986D81BCF82E1CEA0943E18921950AA4B0C857C8B86FC8. Untracked and absent from HEAD. |
| common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt | brilliant_scientist_krg_authorize_deliberate_singularity_detonation | Local SHA-256 E5D24548DF4CBE01F25A63A4528B65EBC2935274409FF4A098C3B78488BB65F3. |
| common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt | brilliant_scientist_krg_ai.never | Local SHA-256 D849A2C345E90D652A951109A8A3BF01E72AC4BA005F706796A4119A8E85C46D. |
| common/scripted_triggers/016_mengele_singularity_terminal_triggers.txt | Mengele terminal readiness chain | Local SHA-256 2B505433DE06B27302A76179AB486BA793E584398CE7DB1DA33563C4508C02D0; untracked. |
| common/scripted_triggers/016_mengele_project_stage_triggers.txt | brilliant_scientist_mengele_project_stage_provider_is_valid | Local SHA-256 86217F4A10AE1F84FBC7E73ADD2029F092F00AD72A250F6E868AD3B7B38FAA7E. |
| common/scripted_triggers/016_brilliant_scientist_triggers.txt | brilliant_scientist_singularity_scenario_is_enabled | Local SHA-256 93359531ED2BA2020258747A7AAB26FFB63315672D9F098FACE8DBB8B5D24444. |
| common/scripted_triggers/chaosx_world_end_scenario_triggers.txt | world_end_brilliant_scientist_strategic_singularity_scenario_enabled | Local SHA-256 5B925970287AA61051897D26EF459CB77E543B736E6900ED092C12CB1DB59485. |

The decision file is absent from the before image: git cat-file -e HEAD:common/decisions/016_mengele_singularity_terminal_decisions.txt returned exit 128 and reported that the path exists on disk but not in HEAD.

## MCP routes, diagnostics, and artifacts

Adapter: decision_ai_will_do. Connected game version was verified by MCP as Operation Postern v1.19.2.0.a729 (d245), matching adapter target Operation Postern 1.19.2.0 (d245).

| Route | Attempt | Result |
| --- | --- | --- |
| hoi4.probability_inspect | Earlier malformed source string. | MCP error -32602: expected object, received string at source. |
| hoi4.probability_inspect | Earlier correction using source.relativePath. | MCP error -32602: Unrecognized key relativePath at source. |
| hoi4.probability_inspect | Corrected schema source = { path: "common/decisions/016_mengele_singularity_terminal_decisions.txt" }. | Succeeded, status PROBABILITY_SOURCE_INSPECTED; workspace mod_chaos_redux_ea3b2d67c2c0. Candidate count 1, default available candidates 0, poolComplete false, required input custom_trigger_tooltip, no inspect-level unresolved item. |
| hoi4.probability_evaluate | Same named scenarios below, source = { path: target }, candidatePool containing only the target, raw_value requested. | Succeeded with PROBABILITY_ANALYZED_PARTIAL; analysis ID probability-14c9082a62073f8b5d65016c; two scenarios, two scenario-candidate records, one unresolved item, zero diagnostics. |
| hoi4.probability_compare | Same scenarios; after points to the target path and before uses an empty path to represent the absent HEAD source. | MCP error -32602: Too small: expected string to have >=1 characters at before.path. No comparison response or comparison ID exists. |
| hoi4.probability_compare | Earlier attempt with absent/revision and relativePath/revision keys. | MCP error -32602: unrecognized keys absent and revision at before; unrecognized keys relativePath and revision at after. |

Inspect artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/01ecea3df4c4591fe6f3ee0d5daf3bef0b6f76983e77babab9c0ade1bf343e3a/cc0f10f730fd3f993486567c507a5f866de55f84661b717acf9a5b725f766a53/probability-inspect-f676ea276f03.json

Evaluation JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc1dfc86fb2842c1659f0770d912570f33ae9a5562cd151a62fa027b41ac47c7/72a3598357a185a251bfed37e282ff70d1914e259ef5cf1161132a215d0275b9/probability-14c9082a62073f8b5d65016c.json

Evaluation ranking SVG and PNG:
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56c005969985e7e8d4ea47bae22ec3e5281b0296302ac0715342570c05f82815/04b0b5e1cdae4bfdff4faf07ae1a779f229ce94d43f068cb0ea4b5eeb161cf42/probability-probability-14c9082a62073f8b5d65016c-ranking.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b4ddd47295c3a940eece40808f20ad6487832bc84ce9b627e990ed63ce742e7/bd3c104f0ffc2e01ad901c30a1436262703980379f421211e8077ccaee0af8a5/probability-probability-14c9082a62073f8b5d65016c-ranking.png

Evaluation unresolved SVG and PNG:
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48692d5a1b9a3220206984e7bbbf14433e03c0b1d1ddd32b4b69fc3348b1a74d/d34b3f70ac19417c808880062588ef0e366bffac78bd3171899b0212217178b4/probability-probability-14c9082a62073f8b5d65016c-unresolved.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95964db399c2a424a8e3482e798090ab0d7bfc04a6d2f4ed80c3b9f7965a8afe/3232e4cb5956183277f40d81f5e0cbb11c9487b0aac87dfe9caf836821750a34/probability-probability-14c9082a62073f8b5d65016c-unresolved.png

No successful comparison was returned; no historical delta is claimed. The adapter declares selectionRule score_only, normalizedProbability false, rawScore true, timeDistribution false, and completePoolRequired false. It warns that decision scores are not normalized without a documented complete selection rule.

## Exact score trace and limits

The adapter resolved the source-local base expression exactly as constant:brilliant_scientist_krg_ai.never = 0/1. The trace begins at 1/1, applies the base operation, and ends at rawValue 0/1. No local modifier operations follow. The result is classified score_only, not a selection probability.

For both named scenarios, the target has rawValue 0/1 and is assigned rank 1 only within the one-member candidate list submitted for this bounded evaluation. conditionalProbability is null. The source inspection reported poolComplete=false; therefore the declared one-item pool does not prove the complete live decision pool and the rank is not a campaign-level rank.

Both scenario records mark eligibility unresolved. Exact adapter diagnostic: TRIGGER_UNRESOLVED, “Scoped or compound trigger custom_trigger_tooltip is not declared by the scenario.” The tool therefore did not establish whether the target is selectable in either state. The raw score is exact; selection and eligibility are unresolved. No external AI factors were declared, so the result is the source-local score trace only.

## Scenario records

Scenario set ID: event016_mengele_terminal_ai_2026_09_25  
Scenario hash: f43aa59a69419ad596af423f9123b3577b41fb3114b42f526806ef880ec3c0b3  
Submitted candidate-pool hash: 49cbb246258a1c55b118203923bbe9d9bfc7910ee945dde3875f761410660ebc

| Scenario ID | Declared state | MCP result |
| --- | --- | --- |
| EVENT016_MENGELE_PRELOCK_READY_2026_09_25 | Actor label MENGELE_CLONE_DIRECTORATE; flags for scenario-country identity, project registry, completed weaponization; global world_end=false, fallout_request_locked=false, settings_chaos_meter_disabled=false. | Exact raw source score 0/1; eligibility unresolved at custom_trigger_tooltip. Fixture also omits facility, site network, components, incident state, scenario-disable collection, complete provider lifecycle, and other ledger locks. Actor label is descriptive, not a verified game tag. |
| EVENT016_MENGELE_UNAVAILABLE_WORLD_END_2026_09_25 | Same country flags; global world_end=true and fallout_request_locked=true. | Exact raw source score 0/1; eligibility still unresolved at custom_trigger_tooltip, so the adapter did not confirm unavailability. Other provider/global state is incomplete. |

The source trigger review shows that world_end blocks visibility and terminal readiness, but the MCP scenario adapter did not bind the compound custom tooltip and did not prove the result from these fixtures.

## Comparison to Kruger

The Mengele decision uses ai_will_do base = constant:brilliant_scientist_krg_ai.never, with no local modifiers. The current constant file defines never = 0. The existing Kruger decision brilliant_scientist_krg_authorize_deliberate_singularity_detonation uses the same constant as its base. This is a direct source-level match, and the MCP evaluation independently resolved the Mengele base to zero.

The MCP adapter did not inspect or evaluate the Kruger decision as a second candidate, so no paired MCP comparison was made. The before/after compare against the absent-before Mengele file could not run because the supported path field rejects an empty before.path. The earlier guessed absent/revision object was also rejected. The source is absent from HEAD, so comparing two current path references would not establish a historical delta; no such comparison is claimed.

## Decision gates and AI findings

The decision is visible only when the Mengele provider is valid, the strategic singularity scenario is enabled, weaponization is complete, the terminal-fired flag is absent, and global world_end is absent. Its available gate calls brilliant_scientist_mengele_singularity_terminal_is_ready through a hidden tooltip. Completion immediately invokes brilliant_scientist_mengele_execute_singularity_terminal; no cost or timer is defined.

The readiness chain requires a free Fallout request ledger and commit-state readiness, including valid provider state, enabled scenario, required facilities, minimum live site network, ready terminal components, completed weaponization, no active incident or prior terminal/request submission, and no world-end/disabled settings. Component readiness depends on Gotterdammerung DLC presence.

- AI weight validity: source-local base is finite and resolves exactly to zero; no local modifiers or unbounded terms were found.
- Dominance, starvation, and rank reversal: unresolved at the full choice level because eligibility and the live pool are incomplete. The one-item rank is not comparative evidence.
- Repetition/exploit risk: the visible gate excludes a country after its terminal-fired flag is set; executor cleanup and broader gameplay exploit behavior were outside this weighted-surface audit.
- Timing: this immediate decision has no timer or MTTH timing distribution.
- Probability: none computed; decision AI raw scores are not normalized probabilities.

No weight change is recommended. Retain the shared never base if the intended behavior remains player-authorized terminal detonation.

## References and skills

Offline wiki snapshot pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding. Decision modding documents the default never behavior without ai_will_do; AI modding distinguishes score races from event-option ai_chance sampling.

Vanilla documentation consulted: documentation/script_concept_documentation.md (Script Constants), common/script_constants/documentation.md, documentation/effects_documentation.md, and documentation/triggers_documentation.md. Vanilla precedents inspected: common/decisions/_generic_decisions.txt and common/decisions/AFG.txt.

Skills applied: chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-mtth.