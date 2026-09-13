# Event 016 private native custom-project access probability baseline — 2026-09-08

Status: `baseline_frozen_route_blocked`. This is a read-only source and eligibility-binding audit of the seven custom native special projects before any source wiring. No gameplay, AI, scripted trigger, special-project, or runtime file was edited, and no commit was created.

## Audited surface and exact candidates

The audited source is `common/special_projects/projects/016_brilliant_scientist_projects.txt`. The exact candidate pool is:

- `sp_brilliant_scientist_quantum_transit` (portal, source line 315, `ai_will_do` line 332)
- `sp_brilliant_scientist_cloning` (cloning, source line 385, `ai_will_do` line 401)
- `sp_brilliant_scientist_autonomous_cognition` (robotics, source line 454, `ai_will_do` line 471)
- `sp_brilliant_scientist_paleogenetics` (paleogenetics, source line 524, `ai_will_do` line 541)
- `sp_brilliant_scientist_xenobiological_synthesis` (xenobiological, source line 594, `ai_will_do` line 611)
- `sp_brilliant_scientist_alien_arms` (alien, source line 664, `ai_will_do` line 681)
- `sp_brilliant_scientist_temporal_mechanics` (temporal, source line 734, `ai_will_do` line 751)

The complete source and scenario fixture is [016_private_native_custom_access_probability_2026-09-08.json](../testing/016_private_native_custom_access_probability_2026-09-08.json).

The MCP source snapshot returned revision `761ad93a36af7fc09f908341d540f7b23afc4637206205b091800ea03fc0951d` and canonical source hash `91632464523c7dc7feba73de542fc95814c701a8385cb711a57c50eb936f7420` for the special-project file.

## Shared AI expression

All seven projects use `base = constant:brilliant_scientist_project_ai.base`, a war modifier `factor = constant:brilliant_scientist_project_ai.preferred_factor` when `FROM = { has_war = yes }`, and a low-capacity modifier `factor = constant:brilliant_scientist_project_ai.cautious_factor` when `FROM = { brilliant_scientist_has_low_project_capacity = yes }`.

The current constants are base `1`, war preference factor `2`, and low-capacity caution factor `0.5` in `common/script_constants/016_brilliant_scientist_project_constants.txt:282-293`.

These are native special-project willingness scores. They are not normalized click probabilities, and no exact score result was claimed because the required native adapter is unavailable.

## Separate eligibility bindings

Each project’s `visible` and `available` block is an OR of the current-host research trigger and the matching private Mengele research trigger. The private bridge bindings are in `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:88-195`.

Each private family trigger requires the strict provider gate, the matching `mengele_event016_<family>_theory_completed` flag, the absence of the private and Directorate completion flags, the absence of the matching native special-project completion ID, and either the global or family-specific availability flag.

The strict provider gate is `brilliant_scientist_mengele_project_stage_provider_is_valid` in `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16-54`. It rejects current-host state, active incident state, defeated/rejected/closed/expired provider states, terminal/world-end state, and any provider without one of the accepted Mengele program-and-idea branches.

The current-host bindings are the family-specific `brilliant_scientist_can_research_<family>_prototype` helpers in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:1897-2060`. They require current-host identity, a valid primary facility, no project incident, the theory stage, and prototype capacity.

The scenario fixture keeps these source bindings separate from score overrides. All seven candidate IDs are overridden true only to make a future supported score adapter’s expression boundary explicit; those overrides do not prove that the source gates are eligible.

## Required scenario matrix

Scenario set `E016_PRIVATE_NATIVE_CUSTOM_ACCESS_2026_09_08` contains named rows for KRG host-valid peace, private provider plus theory-valid peace, private provider without theory, inactive provider, private/native already completed, owner-both-invalid, and private provider plus theory-valid war.

The source truth matrix records the host branch, private branch, strict provider, theory, native-completion, owner, and war inputs separately. War changes only the AI modifier; it is not part of the private eligibility trigger.

## Mandatory MCP evidence and route blocker

The required first weighted call was `hoi4.probability_inspect` against the exact special-project source and the seven-candidate pool. It returned `PROBABILITY_SOURCE_DISCOVERED`, discovery reason `no_weighted_surfaces`, zero candidates, zero available candidates, zero required inputs, and zero unresolved constructs.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21653a5b2ee22d419acd30c4139075a8bdc4666c47637f7336386a898cca5e3d/d938771e535ede89478fe223f31ba14af442a7d59f4398abb20cbd3a9a78688e/probability-inspect-91632464523c.json`.

The installed probability schema exposes event MTTH, event option AI chance, decision AI willingness, mission AI willingness, national-focus AI willingness, technology AI willingness, doctrine AI willingness, direct random, random list, AI strategy factor, and custom weighted pool adapters. It has no native special-project `ai_will_do` adapter.

This is an exact route gap, not an empty or zero-valued special-project score. Technology, decision, mission, and custom-pool adapters were not substituted, so no `probability_evaluate`, `probability_sweep`, `probability_simulate`, `probability_render`, or `probability_compare` result is claimed.

## Findings and handoff

The seven custom projects share the same base/war-preference/low-capacity-caution score expression. Their native presentation gates correctly expose a distinct current-host path and a strict private-provider theory path in source, but MCP cannot evaluate that special-project surface.

The evidence-compatible next step is an MCP adapter that understands native special-project AI willingness and its `FROM` country scope, or an explicitly declared owner-provided adapter contract. Until then, keep source eligibility truth and AI score evidence separate and do not infer that a technology or decision result applies.

No balance, dominance, starvation, rank-reversal, repetition, or exploit conclusion is supported by this baseline. No source wiring or weight change was recommended or applied.

No gameplay files were changed, no unrelated Event 016 surface was audited, and no commit was created.
