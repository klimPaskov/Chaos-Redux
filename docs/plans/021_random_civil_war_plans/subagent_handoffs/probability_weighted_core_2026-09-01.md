# Event 021 independent probability audit, weighted core

Audit date: 2026-09-01.

Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

Scope: TGT-01 through TGT-10, ARC-01 through ARC-08, SEV-01 through SEV-06, and STR-01 through STR-05.

This is an independent read-only audit.

No gameplay, localisation, asset, workbook, configuration, source, or existing report file was edited.

The only file written by this audit is this handoff.

## Certification

This slice does not pass certification.

The independent TGT-02 and TGT-03 pair baseline completed with exact MCP results for the declared two-candidate source-local weight model.

Those results are not whole-campaign target probabilities because the live global country pool was not returned and the parent ticket-expansion helper is not defined in the current workspace search.

The remaining weighted families remain unresolved or score-only because their source-backed MCP inspections did not return within the bounded waits.

## Priority finding: major-country Evolution I gate defect

The current source has no major-country exclusion or reduced-weight branch in random_civil_war_country_can_be_target at common/scripted_triggers/021_random_civil_war_triggers.txt:215-240.

The automatic wrapper at common/scripted_triggers/021_random_civil_war_triggers.txt:243-247 only excludes scenario-bypass flags.

The major-severity predicate at common/scripted_triggers/021_random_civil_war_triggers.txt:300-307 becomes true when the global Evolution I, Evolution II, Evolution III, or scenario-bypass flag is active.

The target effect at common/scripted_effects/021_random_civil_war_effects.txt:389-478 adds constant:random_civil_war_target_weight.major_stage at lines 432-433 whenever that global predicate is true.

That addition is applied to every candidate passing the target gate, not only to major countries.

The current target formula therefore does not implement the specification statement that Evolution I admits majors at reduced weight.

In the baseline manifest, b_is_major is true and b_eligible is also true because every current automatic target predicate was declared satisfied and no major-country predicate exists to set it false.

The b_is_major state is descriptive scenario input and is not used by the weight expression, which makes the missing major-specific branch observable rather than baking an expected result into the manifest.

### TGT-02 baseline result

Scenario TGT-02 is unstable minor versus stable major after Evolution I.

The complete declared pair pool contains minor and major, with both eligible.

The MCP returned minor raw weight 352 and major raw weight 277.

The MCP returned exact conditional probabilities of 352/629, or 0.559618441971383147, for minor and 277/629, or 0.440381558028616852, for major.

Minor ranks first in this declared pair, so the expected local ordering holds for these explicit inputs.

This does not prove that the major receives a reduced weight in the implementation.

It proves only that the selected unstable-minor versus stable-major state values produce a minor-first raw-formula ordering in the declared pair.

Classification: exact for the declared pair source-local formula model, unresolved for the live global automatic target pool.

### TGT-03 baseline result

Scenario TGT-03 is stable minor versus unstable major after Evolution I.

The complete declared pair pool contains minor and major, with both eligible.

The MCP returned minor raw weight 232 and major raw weight 397.

The MCP returned exact conditional probabilities of 232/629, or 0.368839427662957074, for minor and 397/629, or 0.631160572337042925, for major.

Major ranks first in this declared pair.

This is not an automatic-dominance claim for the whole live pool.

It is direct evidence that the current source-local score can let an Evolution I major outrank a stable minor when the major has unstable pressure and the multi-state fragmentation contribution.

Classification: exact for the declared pair source-local formula model, unresolved for the live global automatic target pool.

### Why the finding is actionable before a patch

The source has no independent major-country state in the automatic target predicate.

The source does have a global Evolution I major-stage contribution of +50.

The source has no explicit negative or multiplicative major-country adjustment.

Consequently, a major country that satisfies the ordinary human, liveness, route, capacity, grace, and reservation checks enters automatic selection on the same eligibility basis as a minor.

A high-pressure major can then receive the same global major-stage contribution plus pressure, route, evidence, and fragmentation contributions.

The owner should decide whether the intended repair belongs in the automatic wrapper, in the target score, or in both manual and automatic policy paths.

No source patch was applied.

## Source and documentation evidence

The required repository guidance was read completely before the audit, including AGENTS.md and .agents/skills/chaos-redux-subagents/SKILL.md.

The event-specific, MTTH, and event-planning guidance used for this audit was also read, including .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-mtth/SKILL.md, and .agents/skills/chaos-redux-event-planning/SKILL.md.

The complete scenario matrix was read from docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md.

The installed probability documentation was read from C:\Users\klimp\AppData\Roaming\npm\node_modules\hoi4-agent-tools\docs\probability.md.

The installed probability examples and the probability-inspect, probability-evaluate, probability-sweep, probability-compare, probability-render, probability-scenario-set, probability-sequence, probability-simulate, and probability-analysis-result schemas were consulted.

The required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding.

The required vanilla documentation was consulted, including effects_documentation.md, triggers_documentation.md, script_concept_documentation.md, and common/script_constants/documentation.md.

The relevant vanilla random_list documentation describes weighted effect selection, while the probability adapter documentation distinguishes normalized categorical selection, score races, direct random percentages, and timing distributions.

The parent-supplied formula probe was treated only as a syntax template and was not used as audit evidence.

## Audited source families and direct helpers

The primary source families were:

- common/scripted_effects/021_random_civil_war_effects.txt
- common/scripted_effects/021_random_civil_war_parent_effects.txt
- common/scripted_triggers/021_random_civil_war_triggers.txt
- common/script_constants/021_random_civil_war_constants.txt

The direct helper references inspected were common/scripted_effects/chaosx_dynamic_effects.txt, common/scripted_effects/chaosx_crisis_pressure_effects.txt, common/script_constants/individual_crisis_targeting_constants.txt, and docs/systems/event_system/individual_crisis_targeting.md.

The current workspace search found calls to adjust_individual_crisis_candidate_ticket_weight at common/scripted_effects/021_random_civil_war_parent_effects.txt:4203 and :4226, but no definition of that scripted effect, its adjusted-weight output, or the associated load-derivation effect in the current workspace or the searched vanilla common directory.

The documentation describes a load-zero multiplier of 4, load-one multiplier of 2, load-two multiplier of 1, and zero tickets at load three, but source evidence for the called helper is absent in this checkout.

This helper absence is recorded as a current-workspace structural blocker rather than treated as proof of a runtime load error, because another agent may be editing the shared repository.

### Local source hashes captured at audit time

common/scripted_effects/021_random_civil_war_effects.txt: 7F78C38901B068BC7C2913C11F4E3C3CA6D237AA462ACD37AB2465D01C2D1950.

common/scripted_effects/021_random_civil_war_parent_effects.txt: B0820BA0F007A1AC4F8D2FA326A5D5CCC70821B41D718DCB559EC5625F10E91B.

common/scripted_triggers/021_random_civil_war_triggers.txt: F9F494D0D83F8D12E10507E9BC88F9999438D1795166A4954F2144F8A6B3F7116.

common/script_constants/021_random_civil_war_constants.txt: 8506E12120C0E81F69A2DEBAE69B6CC9B7A47EB2E7E87CE778DC6971FB1A9515.

The source hash for scripted triggers above is preserved exactly as returned by the read-only local hash command.

## Source-local weight traces

### Target selection

event021_random_civil_war_prepare_target initializes the target weight at 10.

It adds pressure multiplied by 4.

It adds 90 for failing authority and 160 for collapsed authority.

It adds 80 for a valid actor route.

It adds route evidence count multiplied by 12.

It adds 45 for more than two controlled states.

It adds 70 for occupation at opening.

It adds 35 below the weak-manpower gate.

It adds 45 for a valid Event 006 route.

It adds 50 whenever major severity is allowed.

It adds 60 for nearby conflict exposure.

It adds -120 for recent civil-war memory.

It adds 20 for subject status.

It sets the score to the minimum for a failed target predicate or a reserved target, clamps to 0 through 1000, rounds, and persists the result.

The parent then divides the persisted score by event021_parent_tuning.target_pool_weight_scale, rounds and clamps it to the target ticket cap, invokes the missing helper, and expands the candidate into a temporary array before random_scope_in_array.

Therefore the exact global selection probability is not the raw score ratio.

The TGT-02 and TGT-03 MCP baseline intentionally reports the source-local formula layer and marks the parent ticket layer unresolved.

### Archetype selection

event021_prepare_archetype_weights initializes six route weights at zero and gives valid routes their route-specific bases.

The current bases are political 70, legal 55, regional 60, command 50, Event 006 80, and same-tag 35.

Evidence strength multiplies the route base and adds the strength step.

Political receives a recent-grievance bonus when pressure is exposed.

Legal receives a weak-target bonus when authority is failing.

Regional receives a divided-target bonus above two controlled states.

Event 006 receives its package bonus.

Command receives an authority-failing bonus.

Same-tag receives its safety bonus.

Each route is clamped to the route maximum before the parent random_list.

The source-local result is a score race over six outcomes, but no completed MCP evaluation established exact normalized route probabilities.

### Severity

event021_prepare_opening_severity initializes limited at 100, serious at 35, and severe and critical at zero.

Exposed pressure adds 80 to serious.

Fractured pressure adds 65 to serious.

Critical pressure adds 100 to serious.

Failing authority adds 25 to serious.

Capitulation with opening occupation adds 35 to serious.

More than two controlled states adds 25 to serious.

When major severity is allowed, the country has more than one controlled state, a non-island owned state exists, and pressure is fractured or critical, severe and critical become eligible.

Fractured pressure adds 65 to severe.

Critical pressure sets critical to 170 and adds the critical bonus.

Failing authority, occupation, and division add their corresponding bonuses to severe and critical.

Stable pressure subtracts 20 from serious.

The parent invokes random_list over limited, serious, severe, and critical.

No completed MCP evaluation established exact severity probabilities.

### Strange incidents

event021_parent_roll_strange_incident has a weighted 0.08 incident branch and a weighted 0.92 no-incident branch.

The entire random_list is gated by global Evolution II activity, the evolution-log-disabled flag, country activity, and the absence of random_civil_war_strange_incident_recent.

The incident branch sets the recent flag, reduces authority by 3, adds pressure 4, and writes an until variable using the 30-day exposure cooldown.

The current source search found no clear of the recent flag and no trigger read of the until variable in the inspected Event 021 family.

A successful incident can therefore suppress later incidents permanently through the flag even though an until variable is written.

This is a source lifecycle risk separate from the major-country gate finding.

## Exact independent MCP baseline manifest

The following complete manifest was sent to hoi4.probability_inspect as event021_tgt_02_03_prechange_baseline_20260901.

    {
      "schemaVersion": "1.0",
      "id": "event021_tgt_02_03_prechange_baseline_20260901",
      "description": "Pre-change independent baseline for TGT-02 and TGT-03. Complete scoped pair pool derived from event021_random_civil_war_prepare_target and random_civil_war_country_can_be_target. The major candidate is intentionally eligible during Evolution I because the current automatic target trigger has no major-country exclusion or reduced-weight branch.",
      "selection": {
        "mode": "categorical_weighted",
        "cadence": "daily",
        "rounding": "nearest"
      },
      "state": {
        "a_eligible": true,
        "b_eligible": true,
        "a_is_major": false,
        "b_is_major": true,
        "evolution_i_active": true,
        "major_severity_allowed": true,
        "a_pressure": 50,
        "a_authority_failing": 0,
        "a_authority_collapsed": 0,
        "a_valid_actor_route": 80,
        "a_route_evidence_count": 1,
        "a_state_fragmentation": 0,
        "a_occupied": 0,
        "a_weak_manpower": 0,
        "a_event006_package": 0,
        "a_major_stage": 50,
        "a_nearby_exposure": 0,
        "a_recent_memory": 0,
        "a_subject": 0,
        "b_pressure": 20,
        "b_authority_failing": 0,
        "b_authority_collapsed": 0,
        "b_valid_actor_route": 80,
        "b_route_evidence_count": 1,
        "b_state_fragmentation": 45,
        "b_occupied": 0,
        "b_weak_manpower": 0,
        "b_event006_package": 0,
        "b_major_stage": 50,
        "b_nearby_exposure": 0,
        "b_recent_memory": 0,
        "b_subject": 0
      },
      "candidates": [
        {
          "id": "minor",
          "category": "target",
          "weight": "10 + state.a_pressure * 4 + state.a_authority_failing + state.a_authority_collapsed + state.a_valid_actor_route + state.a_route_evidence_count * 12 + state.a_state_fragmentation + state.a_occupied + state.a_weak_manpower + state.a_event006_package + state.a_major_stage + state.a_nearby_exposure + state.a_recent_memory + state.a_subject",
          "cap": 1000,
          "eligibleWhen": "state.a_eligible == true"
        },
        {
          "id": "major",
          "category": "target",
          "weight": "10 + state.b_pressure * 4 + state.b_authority_failing + state.b_authority_collapsed + state.b_valid_actor_route + state.b_route_evidence_count * 12 + state.b_state_fragmentation + state.b_occupied + state.b_weak_manpower + state.b_event006_package + state.b_major_stage + state.b_nearby_exposure + state.b_recent_memory + state.b_subject",
          "cap": 1000,
          "eligibleWhen": "state.b_eligible == true"
        }
      ],
      "transitions": []
    }

Every referenced state key is declared.

The manifest contains no min or max function and uses cap 1000 with plain arithmetic only.

The two candidates form a complete declared pair pool for the two matrix scenarios.

The complete declared pair pool is not a claim that it is the complete live global country pool.

The target score is intentionally represented before the parent ticket transform because the called ticket helper is not defined in the current source search.

## Exact MCP calls and results

### Source-backed weighted inspection attempt

The first bounded source-backed inspection batch submitted these four calls concurrently.

    hoi4.probability_inspect({
      "adapter": "custom_weighted_pool",
      "source": {
        "identifier": "event021_parent_add_target_to_selection_pool",
        "path": "common/scripted_effects/021_random_civil_war_parent_effects.txt"
      },
      "refresh": true
    })

    hoi4.probability_inspect({
      "adapter": "random_list",
      "source": {
        "identifier": "event021_parent_select_archetype",
        "path": "common/scripted_effects/021_random_civil_war_parent_effects.txt"
      },
      "refresh": true
    })

    hoi4.probability_inspect({
      "adapter": "random_list",
      "source": {
        "identifier": "event021_prepare_opening_severity",
        "path": "common/scripted_effects/021_random_civil_war_effects.txt"
      },
      "refresh": true
    })

    hoi4.probability_inspect({
      "adapter": "random_list",
      "source": {
        "identifier": "event021_parent_roll_strange_incident",
        "path": "common/scripted_effects/021_random_civil_war_parent_effects.txt"
      },
      "refresh": true
    })

No structured MCP response was returned after the bounded approximately 62-second wait.

The batch was terminated after the bounded wait.

No source-backed revision, source hash, candidate inventory, artifact URI, or analysis ID was returned for that batch.

This is the blocker for treating the other source-family results as engine-confirmed probability evidence.

### TGT-02 and TGT-03 custom-pool inspection

The exact custom-pool manifest above was sent with adapter custom_weighted_pool, refresh true, and workspaceId mod_chaos_redux_ea3b2d67c2c0.

The MCP result was status ok with code PROBABILITY_SOURCE_INSPECTED.

The returned data was sourceRevision 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945, sourceHash d5b12a60ef9eeb157642209e2d06c7032881caf9542d006d5d4aa68957b794e9, poolComplete true, candidates 2, requiredInputs 0, and unresolved 0.

The inspection artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3513df76f0f9ac952be20bfbf13aacd11cb06ab65ea346e4c72d2d572e1f1937/785da1e9c5fda285261e37cc5beef6c28fbc3454aec8a3954a974deb0f664492/probability-inspect-d5b12a60ef9e.json.

The artifact SHA-256 is 3513df76f0f9ac952be20bfbf13aacd11cb06ab65ea346e4c72d2d572e1f1937.

### Initial evaluation request rejected by schema

The first evaluation used the same manifest and scenario states but included a description property on each scenario.

The exact result was MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_evaluate: Unrecognized key: "description" at scenarioSet.scenarios[0]; Unrecognized key: "description" at scenarioSet.scenarios[1].

No analysis was created by that request.

### Corrected TGT-02 and TGT-03 evaluation

The corrected evaluation used adapter custom_weighted_pool, the same manifest ID and all the same state, candidate, expression, cap, eligibility, selection, and transition fields as the inspection manifest.

The only manifest scalar changed in the corrected request was description, which was exactly: Pre-change independent baseline for TGT-02 and TGT-03 using the complete two-candidate scoped pair pool derived from the current target formula and automatic target gate.

The exact corrected scenario set was:

    {
      "schemaVersion": "1.0",
      "id": "event021_tgt_02_03_prechange_scenarios_20260901",
      "scenarios": [
        {
          "id": "TGT-02",
          "state": {
            "a_eligible": true,
            "b_eligible": true,
            "a_is_major": false,
            "b_is_major": true,
            "evolution_i_active": true,
            "major_severity_allowed": true,
            "a_pressure": 50,
            "a_authority_failing": 0,
            "a_authority_collapsed": 0,
            "a_valid_actor_route": 80,
            "a_route_evidence_count": 1,
            "a_state_fragmentation": 0,
            "a_occupied": 0,
            "a_weak_manpower": 0,
            "a_event006_package": 0,
            "a_major_stage": 50,
            "a_nearby_exposure": 0,
            "a_recent_memory": 0,
            "a_subject": 0,
            "b_pressure": 20,
            "b_authority_failing": 0,
            "b_authority_collapsed": 0,
            "b_valid_actor_route": 80,
            "b_route_evidence_count": 1,
            "b_state_fragmentation": 45,
            "b_occupied": 0,
            "b_weak_manpower": 0,
            "b_event006_package": 0,
            "b_major_stage": 50,
            "b_nearby_exposure": 0,
            "b_recent_memory": 0,
            "b_subject": 0
          }
        },
        {
          "id": "TGT-03",
          "state": {
            "a_eligible": true,
            "b_eligible": true,
            "a_is_major": false,
            "b_is_major": true,
            "evolution_i_active": true,
            "major_severity_allowed": true,
            "a_pressure": 20,
            "a_authority_failing": 0,
            "a_authority_collapsed": 0,
            "a_valid_actor_route": 80,
            "a_route_evidence_count": 1,
            "a_state_fragmentation": 0,
            "a_occupied": 0,
            "a_weak_manpower": 0,
            "a_event006_package": 0,
            "a_major_stage": 50,
            "a_nearby_exposure": 0,
            "a_recent_memory": 0,
            "a_subject": 0,
            "b_pressure": 50,
            "b_authority_failing": 0,
            "b_authority_collapsed": 0,
            "b_valid_actor_route": 80,
            "b_route_evidence_count": 1,
            "b_state_fragmentation": 45,
            "b_occupied": 0,
            "b_weak_manpower": 0,
            "b_event006_package": 0,
            "b_major_stage": 50,
            "b_nearby_exposure": 0,
            "b_recent_memory": 0,
            "b_subject": 0
          }
        }
      ]
    }

The corrected call requested metrics raw_value and conditional_probability, outputs json, ranking, and unresolved, refresh true, and workspaceId mod_chaos_redux_ea3b2d67c2c0.

The exact MCP result was status ok with code PROBABILITY_ANALYZED.

The returned analysis ID is probability-a218d22f84d6a1f32e09755c.

The returned sourceRevision is 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945.

The returned sourceHash is e5db118f7f03f5f18b5c64f2dc604aa871204687b31268e6fcf4963cb9b18181.

The returned scenarioHash is 82e4acdb9d02cfd8edd52c6936a97cb5a5e5507b4559440fb163b4d40b9aa9f9.

The returned cache key is a218d22f84d6a1f32e09755cc31ee9d5da8a577877042adfc4090741cd737ff5.

The returned analysis status is complete with scenarios 2, candidates 4, unresolved 0, diagnostics 0, and visualResources 4.

The analysis JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/977c71cba879d9c5c8da960cacbbbd96f30df58aa5572f445c374f530cf3c2e4/374d1823d4648afd20b3c18eb2d37d4b9c8a2307faad9836bb525a976257ded8/probability-a218d22f84d6a1f32e09755c.json.

The JSON artifact SHA-256 is 977c71cba879d9c5c8da960cacbbbd96f30df58aa5572f445c374f530cf3c2e4.

The ranking SVG artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de5f8bf014b1f2853480674f4a23b619d679f074185ac2e4471b1dd7435622f1/f5b10626c0b0d3fc86f44c8f5170f4be12740770fcb5ef112aa8e80b78fc17fe/probability-probability-a218d22f84d6a1f32e09755c-ranking.svg.

The ranking SVG SHA-256 is de5f8bf014b1f2853480674f4a23b619d679f074185ac2e4471b1dd7435622f1.

The ranking PNG artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b84e3f02720d35287c0da5b81ad2d451d9693579ad180b3824bcbffe396554cd/4f4cdd3ede5b9cb31d97dac761cf218d624866ad6babfe32fbe86db2ccb1af4b/probability-probability-a218d22f84d6a1f32e09755c-ranking.png.

The ranking PNG SHA-256 is b84e3f02720d35287c0da5b81ad2d451d9693579ad180b3824bcbffe396554cd.

The unresolved SVG artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/c124d14c144cf4dae9b2b4bf22cee9edec3447073eca5fcc187fb29acc3d1169/probability-probability-a218d22f84d6a1f32e09755c-unresolved.svg.

The unresolved PNG artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/006a775ec602f90a4de30f3cfaad2fd4387e9c0234e1b6151f0cea612ec38864/probability-probability-a218d22f84d6a1f32e09755c-unresolved.png.

The analysis validation passed and explicitly reported zero unresolved or bounded analysis items inside the declared manifest.

### Artifact readback

The analysis JSON was read with read_mcp_resource using server hoi4_agent_tools and the exact analysis artifact URI above.

The artifact readback confirmed TGT-02 minor rawValue 352, major rawValue 277, poolTotal 629, exact fractions 352/629 and 277/629, both eligible, poolComplete true, supportLevel exact, and unresolved empty.

The artifact readback confirmed TGT-03 minor rawValue 232, major rawValue 397, poolTotal 629, exact fractions 232/629 and 397/629, both eligible, poolComplete true, supportLevel exact, and unresolved empty.

The artifact adapter metadata reports adapter custom_weighted_pool version hoi4-1.19.2.v1, numerical precision exact bigint rationals for finite source arithmetic, sourceScope none, and workspace mod_chaos_redux_ea3b2d67c2c0.

### Cached render attempt

The exact cached render request was:

    hoi4.probability_render({
      "analysisId": "probability-a218d22f84d6a1f32e09755c",
      "expectedScenarioHash": "82e4acdb9d02cfd8edd52c6936a97cb5a5e5507b4559440fb163b4d40b9aa9f9",
      "outputs": ["json", "ranking", "unresolved"],
      "includeHtml": false,
      "workspaceId": "mod_chaos_redux_ea3b2d67c2c0"
    })

The exact result was status error with code PROBABILITY_ANALYSIS_NOT_CACHED.

The blocker message was Render requires an analysis ID produced by this server process, with analysisId probability-a218d22f84d6a1f32e09755c.

The evaluate call itself emitted the ranking and unresolved artifacts listed above, so those artifacts remain the rendered evidence for this baseline.

## Scenario ledger

The following ledger lists every requested scenario ID.

The exact label applies only where the MCP result supports that level of evidence.

An unresolved label means that no complete engine-backed result was obtained for the requested live source surface.

### Target selection

| Scenario | Current result | Evidence classification |
| --- | --- | --- |
| TGT-01 | Unstable minor has the source-level direction advantage from pressure, valid opposition, route evidence, and related contributions, but the full pool was not returned. | score-only / unresolved |
| TGT-02 | Unstable minor 352 versus stable major 277 in the complete declared pair, with exact 352/629 versus 277/629. | exact for declared pair / unresolved globally |
| TGT-03 | Unstable major 397 versus stable minor 232 in the complete declared pair, with exact 397/629 versus 232/629. | exact for declared pair / unresolved globally |
| TGT-04 | Recent civil-war memory contributes -120 to the raw target score, while the recent-target cooldown is a separate eligibility gate. | score-only / unresolved |
| TGT-05 | No is_ai-specific target weight or target eligibility branch was found in the inspected Event 021 target path. | score-only / unresolved |
| TGT-06 | Multiple actors affect route evidence and can add evidence and fragmentation contributions, but no direct actor-count term was found in the target formula. | score-only / unresolved |
| TGT-07 | Nearby conflict exposure contributes +60 to the raw target score when its flag is present. | score-only / unresolved |
| TGT-08 | random_civil_war_is_normal_human_country is required, so an actual nonhuman candidate is source-gated out before positive target scoring. | deterministic source gate / unresolved MCP |
| TGT-09 | Event 006 route validity contributes +45 and the ordinary target gate has no Event 006 exclusion after the grace conditions are satisfied. | score-only / unresolved |
| TGT-10 | random_civil_war_has_incompatible_bespoke_route is negated by the target gate, so an incompatible country is source-gated out. | deterministic source gate / unresolved MCP |

### Archetype selection

| Scenario | Current result | Evidence classification |
| --- | --- | --- |
| ARC-01 | Ideological route receives its political base and relevant evidence and pressure contributions when its route predicate is valid. | score-only / unresolved |
| ARC-02 | Legal route receives its legal base and authority-failing contribution when the legal route predicate is valid. | score-only / unresolved |
| ARC-03 | Command route receives its command base and authority-failing contribution when command evidence is valid. | score-only / unresolved |
| ARC-04 | Complete Event 006 validity gives the Event 006 route its base and package bonus, but no MCP ranking was returned. | score-only / unresolved |
| ARC-05 | Regional validity gives the regional route its base and divided-target contribution above two controlled states. | score-only / unresolved |
| ARC-06 | Same-tag takeover is represented as one of six random_list outcomes and is route-gated for the one-state context. | score-only / unresolved |
| ARC-07 | All six route candidates are present in source logic, but equal-strength multi-front balance was not evaluated by MCP. | unresolved |
| ARC-08 | Incomplete Event 006 package fails the Event 006 route predicate and contributes zero for that route in source logic. | deterministic source gate / unresolved MCP |

### Severity

| Scenario | Current result | Evidence classification |
| --- | --- | --- |
| SEV-01 | Stable pressure leaves limited positive and applies the stable serious penalty; severe and critical remain zero without the major-evolution branch. | score-only / unresolved |
| SEV-02 | Exposed pressure adds 80 to serious, with valid opposition remaining a route prerequisite upstream. | score-only / unresolved |
| SEV-03 | Low stability, external war, and occupation supply serious and possibly major-branch inputs, but exact severe normalization was not evaluated. | score-only / unresolved |
| SEV-04 | Evolution I can make severe and critical eligible under fractured or critical pressure, non-island, and multi-state conditions, but exact critical probability was not evaluated. | score-only / unresolved |
| SEV-05 | A stable one-state country still has a positive limited branch and may retain positive serious after the stable penalty; the source does not make limited exclusive. | score-only / unresolved |
| SEV-06 | Major-stage permission enables severe and critical only under the multi-state, non-island, fractured-or-critical conditions, so source logic does not directly force destruction. | score-only / unresolved |

### Strange incidents

| Scenario | Current result | Evidence classification |
| --- | --- | --- |
| STR-01 | If Evolution II is not active, the outer gate makes the incident draw deterministic zero; the requested very-low Rising Chaos behavior was not MCP-evaluated. | deterministic source gate / unresolved MCP |
| STR-02 | When the outer gate passes and the recent flag is absent, source weights are 0.08 incident and 0.92 no incident, with no completed MCP evaluation. | score-only / unresolved |
| STR-03 | The recent-incident flag is a deterministic outer exclusion. | deterministic source gate / unresolved MCP |
| STR-04 | The until variable is written, but the recent flag has no observed clear in the inspected family, so successful incidents can remain suppressed beyond the intended cooldown. | deterministic lifecycle risk / unresolved MCP |
| STR-05 | The evolution-log-disabled flag is a deterministic outer exclusion. | deterministic source gate / unresolved MCP |

## Candidate-pool and external-factor completeness

The TGT-02 and TGT-03 declared pair pool is complete for the two named candidates and returned unresolved zero.

The pair model declares Evolution I active, major severity allowed, one valid actor-route contribution, one route-evidence count, explicit pressure, explicit fragmentation, no occupation, no weak-manpower contribution, no Event 006 package contribution, no nearby exposure, no recent memory, no subject contribution, and both ordinary target predicates true.

The pair model does not declare the live global registry, scheduler cursor, review-due dates, bounded scan window, cluster reservations, active crisis load, country identities, or the missing ticket-helper implementation.

The actual automatic scheduler scans a bounded number of registered countries from a cursor and filters review timing and parent capacity before expanding tickets.

The actual scheduler therefore has a larger and stateful candidate pool than the declared two-country pair.

The ARC, SEV, and STR source pools are structurally identifiable as six, four, and two outcomes respectively, but their live eligibility state and source-backed MCP traces were not returned.

No uncertain input simulation was declared.

No sequence analysis was run because no complete lifecycle manifest with verified transitions, cooldown clearing, recovery, and terminal states was available.

No before revision exists.

## Skipped analyses and exact reasons

Source-backed probability_inspect for target, archetype, severity, and strange-incident source selectors returned no structured response within the bounded approximately 62-second wait and was terminated.

An individual archetype source retry with adapter random_list, source identifier event021_parent_select_archetype, source path common/scripted_effects/021_random_civil_war_parent_effects.txt, and refresh false remained live for the bounded approximately 31-second wait and was terminated.

An individual severity source retry with adapter random_list, source path common/scripted_effects/021_random_civil_war_effects.txt, line 590, workspaceId mod_chaos_redux_ea3b2d67c2c0, and refresh false remained live for the bounded approximately 31-second wait and was terminated.

The full six-route custom archetype manifest inspection event021_arc_audit_20260901 remained live for the bounded approximately 31-second wait and was terminated before returning a source revision, artifact, or analysis.

probability_sweep was skipped for the remaining families because no source-backed inspect completed and the user requested bounded completion.

probability_compare was skipped because no owner-applied source change or declared before/after relationship exists.

probability_simulate was skipped because no uncertain inputs were declared.

probability_sequence was skipped because the live candidate pool, helper implementation, cadence transitions, cooldown clearing, and terminal states were not complete.

The cached probability_render call was attempted after the completed TGT evaluation and returned PROBABILITY_ANALYSIS_NOT_CACHED because the analysis ID was not available to that server process.

The matching structural event inspection was also blocked by selector validation.

The first exact structural request used selector kind omitted and returned MCP error -32602: Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind.

The corrected structural request used selector kind namespace and id chaosx.nr21 and returned MCP error -32602: expected string, received undefined at selector.namespace; Unrecognized key: "id" at selector.

event_render was not called after those schema blockers and the user’s bounded-completion instruction.

## Non-evidence capability probes

The independent syntax probe event021_tgt_formula_probe_independent_20260901 used a two-candidate custom manifest with plain arithmetic and cap 1000.

It returned status ok, code PROBABILITY_SOURCE_INSPECTED, poolComplete true, candidates 2, requiredInputs 0, unresolved 0, sourceRevision 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945, and sourceHash 5b40e2b53ba192d2b75b0b0c1f4e9d87ed2ebfb88a70d163217775956f139422.

Its artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd311ceb62e2ba3e18e2faad6dd5de618e51e6b587bb8365e63b170c2d87ac0d/26e3bfe76f924f140f544628fd10bc075089fee6c8acc2ff2dad4e63c8509285/probability-inspect-5b40e2b53ba1.json.

That probe was a syntax and manifest-contract check only and is not evidence for any requested scenario.

The minimal custom-pool inspection event021_arc_audit_mininspect_20260901 returned status ok, code PROBABILITY_SOURCE_INSPECTED, poolComplete true, candidates 2, requiredInputs 0, unresolved 0, sourceRevision 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945, and sourceHash 6cc888b042216ab6aaff68a54ad639dfc40211a7aaf25b284038997697984d99.

Its artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa9b2b8420e9421d2bc84c967f2eeef240ea68b9ec79df3f5a606b3ceec4ed79/b7ff74082599a2ca3523335976553a5d890d049170c852b2a3df0181a0e68a86/probability-inspect-6cc888b04221.json.

The minimal custom-pool evaluation event021_arc_probe_eval_20260901 returned status ok, code PROBABILITY_ANALYZED, analysisId probability-a652cabf6ff01a29208c11c2, sourceRevision 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945, sourceHash ce23e14854c8c1a2b33db0c75fdb7f84caf406e70a0ba8c3a2cf13908c5452ff, scenarioHash 78fc813274d71baa4e68157bee3b2dd96ddf09fbdffed1f35733c6989ba33a39, scenarios 1, candidates 2, unresolved 0, diagnostics 0, and visualResources 4.

Its JSON artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad4f99b042770e970b32c3b3ba7133f21b8d67026e3d74997bdd14602ff8622b/eec2f901af4d23165d9b8512efde3a3073e794363449012259862259416afc87/probability-a652cabf6ff01a29208c11c2.json.

Its ranking SVG was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6428af2fc5f0e681ff8fd4e3eadc52834f75db74f729300f7e82e16344d3ace8/a0a9eaf1f3cecc49cffb4b6c25c9d73e9fe688d2f71a62b123b9ece9ef27629d/probability-probability-a652cabf6ff01a29208c11c2-ranking.svg.

Its ranking PNG was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6dc743d5992dec905d7382da2ef5a6375f31064775fcadbd0705d2d99803718/e76cca3053b0cb39a2c065412b4c68ace8999bc79d89dd3556ff08889f29efd0/probability-probability-a652cabf6ff01a29208c11c2-ranking.png.

Its unresolved SVG was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/e4593882955a8936cf852ec389c0f87d3d6b63ea8964eb1caa8762d81dce3537/probability-probability-a652cabf6ff01a29208c11c2-unresolved.svg.

Its unresolved PNG was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/c730ec2eedaa686f631a988f1e9f6d134227be178d0f3f59522d69d46e2e0231/probability-probability-a652cabf6ff01a29208c11c2-unresolved.png.

These capability-probe artifacts are excluded from all scenario conclusions.

## Recommended owner follow-up, without applying changes

Add an explicit major-country policy to the automatic target path that matches the specification’s Evolution I reduced-weight rule.

Keep manual scenario bypass semantics separate from automatic eligibility if the intended design allows manual major selection before Evolution I.

Centralize any new reduced-weight tuning in common/script_constants/021_random_civil_war_constants.txt.

Re-run the exact TGT-02 and TGT-03 manifest and scenario IDs after the owner patch.

Use probability_compare only after a real before and after source revision exists, with the same candidate pool and scenario states.

Resolve or document the missing adjust_individual_crisis_candidate_ticket_weight definition before claiming final target-selection probabilities.

Add a lifecycle clear or an until-based eligibility test for random_civil_war_strange_incident_recent if the intended incident cooldown is repeatable.

Re-run the full live candidate-pool inspections for TGT, ARC, SEV, and STR after those source-level blockers are resolved.

## Handoff conclusion

The highest-priority owner action is the missing major-country Evolution I gate or reduced-weight branch.

The current source allows an Evolution I major into automatic selection whenever the ordinary target predicate passes and applies the global +50 major-stage contribution without a major-specific reduction.

The exact independent pre-change pair baseline is preserved above and in the MCP artifacts.

The TGT-02 and TGT-03 conclusions are durable as declared-pair source-local evidence, while whole-pool and parent-ticket conclusions remain explicitly unresolved.

No patch, revert, commit, or claim of full certification was made.

## Post-change re-audit, TGT-02 and TGT-03

Re-audit date: 2026-09-01.

The owner patch was observed in the shared workspace before this re-audit.

Only TGT-02 and TGT-03 were re-audited.

The exact pre-change pair candidate IDs remain minor and major.

The exact pre-change scenario states were reused for the mandatory comparison.

No gameplay file was edited.

### Post-change source proof

The current automatic target path at common/scripted_triggers/021_random_civil_war_triggers.txt:137-163 calls random_civil_war_major_targeting_allowed before the ordinary target gates complete.

The current helper at common/scripted_triggers/021_random_civil_war_triggers.txt:212-217 is:

    random_civil_war_major_targeting_allowed = {
        OR = {
            is_major = no
            random_civil_war_major_severity_allowed = yes
        }
    }

random_civil_war_major_severity_allowed at lines 200-210 is true for global Evolution I, Evolution II, Evolution III, or scenario-bypass activity.

Before Evolution I, with no later evolution or bypass flag, a major fails the deterministic OR and is not a weighted candidate.

This is a deterministic eligibility result, not a probability, so no fabricated pre-Evolution probability is reported.

At Evolution I and later, a major passes the deterministic gate when the remaining ordinary target predicates pass.

The current target effect at common/scripted_effects/021_random_civil_war_effects.txt:407-478 adds major_stage only inside an is_major = yes and random_civil_war_major_severity_allowed = yes condition at lines 428-432.

The current effect then multiplies the completed major score by constant:random_civil_war_target_weight.major_target_factor at lines 450-452 inside an is_major = yes condition.

The current constant is major_target_factor = 0.35 at common/script_constants/021_random_civil_war_constants.txt:246.

The minor path does not receive major_stage and does not receive the major factor because both operations are guarded by is_major = yes.

The source now also contains a player-target +25 contribution at lines 446-448.

The current source-local target formula no longer contains the pre-change route-evidence, state-fragmentation, weak-manpower, or Event 006 package additions that were present in the pre-change declared manifest.

That formula difference is preserved as a comparison caveat below and was not silently attributed to the major factor alone.

### Post-change manifest

The following complete manifest was sent to hoi4.probability_inspect and hoi4.probability_evaluate as event021_tgt_02_03_postchange_20260901.

    {
      "schemaVersion": "1.0",
      "id": "event021_tgt_02_03_postchange_20260901",
      "description": "Post-change independent audit manifest for TGT-02 and TGT-03 using the exact pre-change pair states. Current source gates majors through random_civil_war_major_targeting_allowed, applies major_stage only to majors, and applies major_target_factor after the source-local score.",
      "selection": {
        "mode": "categorical_weighted",
        "cadence": "daily",
        "rounding": "nearest"
      },
      "state": {
        "a_eligible": true,
        "b_eligible": true,
        "a_is_major": false,
        "b_is_major": true,
        "evolution_i_active": true,
        "major_severity_allowed": true,
        "a_pressure": 50,
        "a_authority_failing": 0,
        "a_authority_collapsed": 0,
        "a_valid_actor_route": 80,
        "a_route_evidence_count": 1,
        "a_state_fragmentation": 0,
        "a_occupied": 0,
        "a_weak_manpower": 0,
        "a_event006_package": 0,
        "a_major_stage": 0,
        "a_nearby_exposure": 0,
        "a_recent_memory": 0,
        "a_subject": 0,
        "a_player": 0,
        "a_major_target_factor": 1,
        "b_pressure": 20,
        "b_authority_failing": 0,
        "b_authority_collapsed": 0,
        "b_valid_actor_route": 80,
        "b_route_evidence_count": 1,
        "b_state_fragmentation": 45,
        "b_occupied": 0,
        "b_weak_manpower": 0,
        "b_event006_package": 0,
        "b_major_stage": 50,
        "b_nearby_exposure": 0,
        "b_recent_memory": 0,
        "b_subject": 0,
        "b_player": 0,
        "b_major_target_factor": 0.35
      },
      "candidates": [
        {
          "id": "minor",
          "category": "target",
          "weight": "(10 + state.a_pressure * 4 + state.a_authority_failing + state.a_authority_collapsed + state.a_valid_actor_route + state.a_major_stage + state.a_nearby_exposure + state.a_recent_memory + state.a_subject + state.a_player) * state.a_major_target_factor",
          "cap": 1000,
          "eligibleWhen": "state.a_eligible == true"
        },
        {
          "id": "major",
          "category": "target",
          "weight": "(10 + state.b_pressure * 4 + state.b_authority_failing + state.b_authority_collapsed + state.b_valid_actor_route + state.b_major_stage + state.b_nearby_exposure + state.b_recent_memory + state.b_subject + state.b_player) * state.b_major_target_factor",
          "cap": 1000,
          "eligibleWhen": "state.b_eligible == true"
        }
      ],
      "transitions": []
    }

All referenced state keys are declared.

The candidate pool is complete for the same two declared pair candidates as the pre-change manifest.

The major factor is declared as 0.35 only for the major expression.

The minor expression contains no major_stage term in the post-change source-local model.

### Post-change inspect call and result

The exact inspect call used adapter custom_weighted_pool, the complete manifest above, refresh true, and workspaceId mod_chaos_redux_ea3b2d67c2c0.

The MCP returned status ok with code PROBABILITY_SOURCE_INSPECTED.

The inspect result returned sourceRevision 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945.

The inspect result returned sourceHash b71da4d367d27bb6ba1b9866da7c580f98a4efc1845d743f913d86c1ab38856b.

The inspect result returned poolComplete true, candidates 2, requiredInputs 0, unresolved 0, and diagnostics empty.

The inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13e8d1eb2cc41e587bca3fad488f0f3a182d9f164636bc624d0d69986c17fee1/dcdc5ca946aeb6602711bc24007640e73199921b10a8a2deb885b4fe80034901/probability-inspect-b71da4d367d2.json.

The inspect artifact SHA-256 is 13e8d1eb2cc41e587bca3fad488f0f3a182d9f164636bc624d0d69986c17fee1.

### Post-change evaluation call and result

The exact evaluation call used adapter custom_weighted_pool, the manifest above, scenario set event021_tgt_02_03_postchange_scenarios_20260901, metrics raw_value and conditional_probability, outputs json, ranking, and unresolved, refresh true, and workspaceId mod_chaos_redux_ea3b2d67c2c0.

The exact post-change scenario set was:

    {
      "schemaVersion": "1.0",
      "id": "event021_tgt_02_03_postchange_scenarios_20260901",
      "scenarios": [
        {
          "id": "TGT-02",
          "state": {
            "a_eligible": true,
            "b_eligible": true,
            "a_is_major": false,
            "b_is_major": true,
            "evolution_i_active": true,
            "major_severity_allowed": true,
            "a_pressure": 50,
            "a_authority_failing": 0,
            "a_authority_collapsed": 0,
            "a_valid_actor_route": 80,
            "a_route_evidence_count": 1,
            "a_state_fragmentation": 0,
            "a_occupied": 0,
            "a_weak_manpower": 0,
            "a_event006_package": 0,
            "a_major_stage": 0,
            "a_nearby_exposure": 0,
            "a_recent_memory": 0,
            "a_subject": 0,
            "a_player": 0,
            "a_major_target_factor": 1,
            "b_pressure": 20,
            "b_authority_failing": 0,
            "b_authority_collapsed": 0,
            "b_valid_actor_route": 80,
            "b_route_evidence_count": 1,
            "b_state_fragmentation": 45,
            "b_occupied": 0,
            "b_weak_manpower": 0,
            "b_event006_package": 0,
            "b_major_stage": 50,
            "b_nearby_exposure": 0,
            "b_recent_memory": 0,
            "b_subject": 0,
            "b_player": 0,
            "b_major_target_factor": 0.35
          }
        },
        {
          "id": "TGT-03",
          "state": {
            "a_eligible": true,
            "b_eligible": true,
            "a_is_major": false,
            "b_is_major": true,
            "evolution_i_active": true,
            "major_severity_allowed": true,
            "a_pressure": 20,
            "a_authority_failing": 0,
            "a_authority_collapsed": 0,
            "a_valid_actor_route": 80,
            "a_route_evidence_count": 1,
            "a_state_fragmentation": 0,
            "a_occupied": 0,
            "a_weak_manpower": 0,
            "a_event006_package": 0,
            "a_major_stage": 0,
            "a_nearby_exposure": 0,
            "a_recent_memory": 0,
            "a_subject": 0,
            "a_player": 0,
            "a_major_target_factor": 1,
            "b_pressure": 50,
            "b_authority_failing": 0,
            "b_authority_collapsed": 0,
            "b_valid_actor_route": 80,
            "b_route_evidence_count": 1,
            "b_state_fragmentation": 45,
            "b_occupied": 0,
            "b_weak_manpower": 0,
            "b_event006_package": 0,
            "b_major_stage": 50,
            "b_nearby_exposure": 0,
            "b_recent_memory": 0,
            "b_subject": 0,
            "b_player": 0,
            "b_major_target_factor": 0.35
          }
        }
      ]
    }

The MCP returned status ok with code PROBABILITY_ANALYZED.

The post-change evaluation analysis ID is probability-fef09b6786ba8c1594243bea.

The post-change evaluation sourceRevision is 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945.

The post-change evaluation sourceHash is b71da4d367d27bb6ba1b9866da7c580f98a4efc1845d743f913d86c1ab38856b.

The post-change evaluation scenarioHash is aecbd718dfc317a9466165bc408ca6964dc34a4a6552ba22ea1e1e4d993e7a6f.

The post-change evaluation returned scenarios 2, candidates 4, unresolved 0, diagnostics 0, and analysisStatus complete.

The post-change JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d92ee65dec1f6bced51e4d20d42578ae6e3bef3eedaf48344d1e3828f9e674eb/1f896e567138026405e74448a44f66696a457604d50818595323ae6daab7f58d/probability-fef09b6786ba8c1594243bea.json.

The post-change JSON artifact SHA-256 is d92ee65dec1f6bced51e4d20d42578ae6e3bef3eedaf48344d1e3828f9e674eb.

The post-change ranking SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209fd366c3a67f25d68ed18652f3cfe6a2bfc18e25ef092c4994ea0de85b8342/7970502dd6ef833032a222b1d8f5306c95fff0c8b71b3784441cc821009c6814/probability-probability-fef09b6786ba8c1594243bea-ranking.svg.

The post-change ranking PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70ca14675d3c0d67d453825ffbe025becb6009ec89e8e7c35fec2d7bcc5e24dd/fe7e2a3c1857b2f7d0034ddc5b0332e0b61ae6c2f819dffc1468478d19e4ee6b/probability-probability-fef09b6786ba8c1594243bea-ranking.png.

The post-change unresolved SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/0899a5c8c7600d8d67869c1f21921dabaf4f0d6ab5f0ae8cdbf8e528f2ba0733/probability-probability-fef09b6786ba8c1594243bea-unresolved.svg.

The post-change unresolved PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/a0fa5cc7b943a4e190daf0354e6e9f1f82c9bd2a2347a787425eacf49ad1aeb9/probability-probability-fef09b6786ba8c1594243bea-unresolved.png.

The evaluation artifact readback confirmed TGT-02 minor raw value 290 and major raw value 77, with exact conditional probabilities 290/367 = 0.790190735694822888 and 77/367 = 0.209809264305177111.

The evaluation artifact readback confirmed TGT-03 minor raw value 170 and major raw value 119, with exact conditional probabilities 170/289 = 0.588235294117647058 and 119/289 = 0.411764705882352941.

Both candidates are eligible in both post-change Evolution I scenarios.

### Mandatory compare call and result

The exact compare call used adapter custom_weighted_pool, beforeManifest event021_tgt_02_03_prechange_baseline_20260901 exactly as preserved earlier in this report, afterManifest event021_tgt_02_03_postchange_20260901 exactly as preserved above, and the exact pre-change scenario set event021_tgt_02_03_prechange_scenarios_20260901 exactly as preserved earlier in this report.

The compare requested outputs json, ranking, comparison, and unresolved, refresh true, and workspaceId mod_chaos_redux_ea3b2d67c2c0.

The MCP returned status ok with code PROBABILITY_ANALYZED.

The compare analysis ID is probability-e1dc6dc56a110c9cbdeed4b3.

The compare sourceRevision is 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945.

The compare sourceHash is 0aa87d86daa080eec8ae1b89ef4726f592246f735e128af4afff2ec900dd531b.

The compare scenarioHash is 82e4acdb9d02cfd8edd52c6936a97cb5a5e5507b4559440fb163b4d40b9aa9f9, which is the exact pre-change scenario hash.

The compare returned scenarios 2, candidates 4, unresolved 0, diagnostics 0, comparisonChanges 4, and visualResources 6.

The compare artifact reports beforeAnalysisId probability-4d19541d06ae2dc45feb0fa2 and afterAnalysisId probability-8fd051c28022c729bb21b3a2.

The compare JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50ed658d909e7fbf3b43fc1e7a152556f9a70bb9f3af517179f58c95f731aded/8458d1bc1a51ac90865ddd80392820b9badcb6c0f2bcb83c2b04b888167ea662/probability-e1dc6dc56a110c9cbdeed4b3.json.

The compare JSON artifact SHA-256 is 50ed658d909e7fbf3b43fc1e7a152556f9a70bb9f3af517179f58c95f731aded.

The compare ranking SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b4893cd593686b15610c9cfe5f529ae0192d723db3f325ac3c6a1da00d59e01/9d45ea7073ad85bdf1485f3fb0af5423d20b3b42defa3e7de126e3973f888503/probability-probability-e1dc6dc56a110c9cbdeed4b3-ranking.svg.

The compare ranking PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5a9ebb3492af1f90f5fdb2ce4ebb1f6c694baee6eb50b9dbecae7b2d6f5d591/da2ef8d7b16905b00b562b485a88fb6111d2852135ed625bbd4016ca7ca1cda1/probability-probability-e1dc6dc56a110c9cbdeed4b3-ranking.png.

The compare visualization SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84d7af4ec5a30ee740aa916ca8e4170d48fbe7f0a5e478a8bc2591a3f6db1898/f9871b334b863e274674f305bcf8a057087d16831b90fdf42d3c559877107264/probability-probability-e1dc6dc56a110c9cbdeed4b3-comparison.svg.

The compare visualization PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/980073bb41c5bdb8ba2f642446eb69dea8733db7e7c4f5a6a80cddf4aa485851/099874ceb9c50fc6918b2a4b7d7d4fd3ced610f5c1731288c7adab8e3a86b7a5/probability-probability-e1dc6dc56a110c9cbdeed4b3-comparison.png.

The compare unresolved SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/870742cdd0cf0fe01173227444841d1fd0b711b74de2d9e923c3a03c3db66a7e/probability-probability-e1dc6dc56a110c9cbdeed4b3-unresolved.svg.

The compare unresolved PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/c1d034fa9ce14ac96022c895e53c410bbf518e3823293da0b153f311957510aa/probability-probability-e1dc6dc56a110c9cbdeed4b3-unresolved.png.

The compare JSON readback reported adapterChanged false, assumptionsChanged false, regressions empty, and changedAstPaths empty for all four candidate changes.

The compare raw and probability deltas were:

| Scenario | Candidate | Pre raw | Post raw | Raw delta | Pre probability | Post probability | Probability delta | Rank change |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TGT-02 | minor | 352 | 290 | -62 | 352/629 | 290/367 | +0.2305722937234398 | rank 1 to rank 1 |
| TGT-02 | major | 277 | 77 | -200 | 277/629 | 77/367 | -0.23057229372343974 | rank 2 to rank 2 |
| TGT-03 | minor | 232 | 170 | -62 | 232/629 | 170/289 | +0.21939586645469 | rank 2 to rank 1 |
| TGT-03 | major | 397 | 119 | -278 | 397/629 | 119/289 | -0.21939586645469 | rank 1 to rank 2 |

The compare artifact’s generic attribution is source or scenario metadata changed because the declared before and after manifests are fixture manifests and changedAstPaths are empty.

The compare therefore proves the exact declared-pair before/after result but does not attribute every raw delta solely to the 0.35 factor.

### Post-change verdict

The post-change source satisfies the requested deterministic gate: majors are invalid before Evolution I unless a later evolution or scenario-bypass condition is active.

The post-change source satisfies the requested Evolution I eligibility: majors are valid once Evolution I is active and all ordinary target predicates pass.

The post-change source satisfies the requested weighting order: major_stage is added before major_target_factor is multiplied.

The post-change source satisfies the requested minor behavior: minors do not receive major_stage and do not receive the major factor.

TGT-02 remains minor-first in the exact declared pair, changing from 352/629 before to 290/367 after.

TGT-03 changes from major-first at 397/629 before to minor-first at 170/289 after.

The TGT-03 rank reversal is the intended reduced-major-weight behavior for the declared pair.

Classification: exact for the declared pair source-local before/after comparison, deterministic for the pre-Evolution major gate, and unresolved for the live global campaign pool and parent ticket-expansion layer.

The full Event 021 certification verdict remains FAIL because this re-audit covers only TGT-02 and TGT-03 and does not resolve the previously recorded live-pool, helper-definition, or other-family MCP blockers.

### Post-change local hashes

common/scripted_effects/021_random_civil_war_effects.txt: A6C6BF571B87CBC934ABEC5F51FA6CB733EC177AA1605D166E469CB831355516.

common/scripted_effects/021_random_civil_war_parent_effects.txt: 901D13DDB820C04AE48A3862623815CE15F61758B188917A7C6C920C0478C7C1.

common/scripted_triggers/021_random_civil_war_triggers.txt: C8AF1AE4514D1DA200AB79AF7FFDAE021358A874E578513A6BDF75B3764E25D5.

common/script_constants/021_random_civil_war_constants.txt: BDF3BBCA70B2B7650EA1D117DAD9642AC3AA5179767F20F47210EEF1ABE8F1A6.

The MCP sourceRevision remained 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 across the post-change inspect, evaluate, and compare calls.

The local source hashes changed from the pre-change hashes recorded earlier in this report, confirming that the shared workspace was not at the prior source state.

### Remaining blocker and owner note

The parent still calls adjust_individual_crisis_candidate_ticket_weight in common/scripted_effects/021_random_civil_war_parent_effects.txt, while the current workspace search did not find its definition.

The exact pair results above are therefore source-local target-score evidence, not final automatic campaign selection probabilities after ticket expansion.

The owner should review the observed removal of the pre-change evidence, fragmentation, weak-manpower, and Event 006 score components before treating the compare deltas as a narrowly isolated major-target patch effect.

No additional retry was made after the successful compare.

No gameplay source, localisation, asset, workbook, configuration, or existing report was edited, and no commit was created.
