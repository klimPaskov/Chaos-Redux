# Event016 Native Selection AI Baseline ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â 2026-10-03

Status: **The source baseline and one-state retry are documented; MCP probability validation and the full eight-scenario audit remain unresolved. No balance certification is made.**

## Authority and scope

The accepted owner policy is explicit in the parent instruction and correction in this task: the three native selection decisions copy the corresponding existing Prototype `ai_will_do` block verbatim; the cloning reference is `ai_high` at line 124, not the cloning Theory block's `ai_medium` at line 56; the two rocketry choices copy the rocketry Prototype block at line 93; releases use the shared zero value and must not cause autonomous AI churn. No tuning values or random list are authorized. The parent owns source and balance policy and reports source integration audits complete. The verbatim-reference score policy remains unchanged, and no baseline weight values changed; this does not resolve the MCP probability gap.

This is a read-only audit. I changed no gameplay, AI, decision, trigger, effect, localisation, or other source file; launched no game; used no model tooling; ran no tests; and created no commit. The only repository write is this handoff.

## Audited surfaces and source snapshots

| Surface | Source path and identifiers | Source evidence |
|---|---|---|
| Existing cloning Prototype reference | `common/decisions/016_mengele_cloning_stage_decisions.txt`: `mengele_event016_cloning_prototype`, `ai_will_do` line 124 | Local SHA-256 `D67CFEF2A063DC1258FC0C6CC0858133CC30D009EB9CDC751DB80D1245EDF2C7` |
| Existing rocketry Prototype reference | `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt`: `mengele_event016_rocketry_prototype`, `ai_will_do` line 93 | Local SHA-256 `80B52209C7267F27DB004B2F9CCC63023C14BE76ECB9D4F2B317A0B4FB13C98F` |
| New selections and releases | `common/decisions/016_mengele_native_prototype_selection_decisions.txt`: `mengele_event016_native_select_cloning`, `mengele_event016_native_select_flying_bomb`, `mengele_event016_native_select_jet_engine`, `mengele_event016_native_release_cloning`, `mengele_event016_native_release_flying_bomb`, `mengele_event016_native_release_jet_engine` | Local SHA-256 `9C49FFEA996DFE5FAA06E03E34B2676BF1BD314AD2EB5510A498936498384669` |
| Selection gate and effect helpers | `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt`; `common/scripted_triggers/016_mengele_native_prototype_triggers.txt`; `common/scripted_effects/016_mengele_native_selection_decision_effects.txt` | The user reports that core and UI helpers are fully defined and corrected. Read-only source review covered the cloning visibility/selection/release gates and the decision adapters. Their engine availability remains unvalidated by MCP. |

The three new selection `ai_will_do` expressions match their intended reference expressions after trimming leading and trailing whitespace: cloning line 15 equals cloning Prototype line 124; flying-bomb line 41 and jet-engine line 53 each equal rocketry Prototype line 93. The release expressions at lines 27, 65, and 77 each use `base = constant:brilliant_scientist_value.zero`.

The source-declared tuning inputs are `brilliant_scientist_project_board.ai_high = 10` at `common/script_constants/016_brilliant_scientist_project_constants.txt:76`, `brilliant_scientist_project_ai.preferred_factor = 2` at line 288, `brilliant_scientist_project_ai.cautious_factor = 0.50` at line 290, and `brilliant_scientist_value.zero = 0` at `common/script_constants/016_brilliant_scientist_constants.txt:45`. Their local SHA-256 values are respectively `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131` and `ADFEE7FE6093933C394C34C8A6A162795D4BDB4575512C476B417C1173B6E4A6`.

The declared selection score trace is therefore base `ai_high`, a `preferred_factor` modifier under `has_war = yes`, and a `cautious_factor` modifier under the existing family predicate. Cloning uses `brilliant_scientist_mengele_cloning_prototype_decision_no_spare_factories`; flying bomb and jet engine both use `brilliant_scientist_mengele_rocketry_prototype_low_factory_margin`. I did not combine these values into an effective score because the required MCP trace did not return. The decision blocks declare zero cost and no decision timer fields. The completed decision adapters delegate to the native selection/release core and clear the temporary selector state; these effects are separate from the willingness score.

## Scenario contract submitted

The scenario-set id submitted for comparison was `E016_NATIVE_SELECTION_AI_2026_10_03`, with exactly these scenario ids: `quiet_ready`, `war_ready`, `low_factory_margin`, `both_rocketry_native_sources_ready`, `only_flying_bomb_ready`, `only_jet_engine_ready`, `matching_selected_completed`, and `invalid_provider`.

Each scenario used `tag = MEN`, `is_ai = true`, and the declared assumptions `provider_valid = true`, `private_theory = true`, `prototype_incomplete = true`, `no_paid_receipt = true`, and `opposite_source_selected = false`, except `invalid_provider`, which set `provider_valid = false`. Scenario-specific inputs were: `quiet_ready` set peace and `low_factory_margin = false`; `war_ready` set `has_war = true`; `low_factory_margin` set peace and `low_factory_margin = true`; `both_rocketry_native_sources_ready` set both native rocketry gate labels true; `only_flying_bomb_ready` set the flying-bomb gate label true and jet-engine gate label false; `only_jet_engine_ready` set those labels false and true respectively; `matching_selected_completed` set `matching_selected_completed = true`; and `invalid_provider` set `provider_valid = false`.

The submitted `candidateOverrides` forced all eight old/new decision ids into the scoring fixture in every scenario. The cloning comparison's `candidatePool` was exactly `mengele_event016_cloning_prototype` plus `mengele_event016_native_select_cloning`; it did not assume that the before and after identifiers matched. This is a bounded score-comparison pool for those two source identities, not the full game decision scheduler or a normalized selection pool.

The top-level live tool schema exposed `scenarioSet` as unknown. The nested scenario shape followed the repository's existing E016 fixture pattern (`id`, `scenarios`, per-scenario `state`, and `candidateOverrides`), but the MCP call returned no validation result or scenario hash. The custom state keys above are symbolic analytical assumptions, not confirmed HOI4 scopes or helper-trigger outputs. In particular, the generic low-factory and native-gate labels do not prove the actual family predicates or native technology gates. Candidate overrides isolate score evaluation and cannot prove provider, Theory, incomplete-prototype, receipt, exclusivity, or adoption availability.

| Scenario id | Candidate pool / external-factor completeness | Classification |
|---|---|---|
| `quiet_ready` | Submitted cloning pair only; complete for that bounded expression pair, incomplete for the full game AI choice set. War is explicitly false; provider, private Theory, prototype, receipt, opposite-source, and low-margin inputs are assumptions. | Unresolved MCP result; no probability claim. |
| `war_ready` | Same bounded cloning pair; `has_war = true` is supplied, while other gates remain assumptions. | Unresolved MCP result; no probability claim. |
| `low_factory_margin` | Same bounded cloning pair; the generic margin label is supplied but is not mapped to the cloning helper predicate. | Unresolved MCP result; no probability claim. |
| `both_rocketry_native_sources_ready` | No rocketry comparison completed. Both native-gate labels were supplied as assumptions; the cloning compare pool does not establish rocketry availability. | Unresolved. |
| `only_flying_bomb_ready` | No rocketry comparison completed. Native-gate labels are assumptions and candidate overrides force scoring candidates. | Unresolved. |
| `only_jet_engine_ready` | No rocketry comparison completed. Native-gate labels are assumptions and candidate overrides force scoring candidates. | Unresolved. |
| `matching_selected_completed` | No completed-adoption or release-gate proof; candidate overrides force scoring candidates despite the state label. | Unresolved. |
| `invalid_provider` | The state label marks an invalid provider, but candidate overrides still force candidates for score isolation; this scenario cannot validate hidden availability. | Unresolved. |

The analyzer did not establish external AI strategy factors, decision-specific strategy adjustments, hidden campaign state, full candidate competition, or any engine availability result. No exact selection probability is claimed. These controls are `decision_ai_will_do` scores, not event `ai_chance` sampling and not an MTTH timing distribution.

## MCP evidence and blocker

The installed service was verified as `hoi4-agent-tools` version `3.6.0`; stdio initialization, `ping`, and `listTools` succeeded on the first local-client session. The live list exposed `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, and `hoi4.probability_render`. The live `probability_inspect` schema accepts `adapter`, `source`, `candidatePool`, `refresh`, and `workspaceId`; source objects were passed as `{ path: <mod-relative path> }`. Both comparison requests used real nonempty `before.path` and `after.path` values and did not add source hashes or revisions to those objects.

`hoi4.probability_inspect` was started first for adapter `decision_ai_will_do` and the existing cloning Prototype source. Connected-route calls remained pending beyond 120 seconds. Narrow local-stdio retries against the explicit one-workspace registration returned the SDK error `McpError: MCP error -32001: Request timed out`. A further narrow inspect request targeted the current selection source and `mengele_event016_native_select_cloning` with `refresh = false`; it remained pending for about 180 seconds and was cancelled without an artifact, source revision, or schema diagnostics.

`hoi4.probability_compare` was submitted through the connected route for the exact cloning before/after source paths, the bounded two-id candidate pool, and the eight named scenarios above. The call returned the MCP error `timed out awaiting tools/call after 600s`; no comparison id, artifact URI, source revision, scenario hash, or rendered output was issued. The rocketry pair was not submitted after that route failure.

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were not run because inspect did not return candidate/input diagnostics, and no supported sweep paths or trace schema were available to validate. This leaves base-score evaluation, modifier traces, rankings, rank reversals, dominance, starvation, and thresholds unresolved. `hoi4.probability_render` was skipped because no analysis id exists. Simulation was not warranted because the declared scenarios are deterministic assumptions; sequence analysis was not applicable because this is not a declared custom weighted pool with cadence and state transitions.

`hoi4.reference_context` was exposed but remained pending beyond 120 seconds and was terminated. I read the pertinent offline local references directly. The installed documentation directory contains no AI-specific or decision-weight document, and an exact-term search for `ai_will_do` in its script-concept, modifier, and trigger Markdown files returned no matches.

## Reference evidence

| Local reference | Relevant lines | Local SHA-256 | Use in this audit |
|---|---:|---|---|
| `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` | 26ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“36 | `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` | Describes `ai_will_do` as a randomized score race in which the highest score wins, notes additional AI strategy/define modifiers, and distinguishes event `ai_chance` probability-proportional sampling. |
| `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` | 357ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“371 | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` | Describes decision AI willingness and its MTTH-block structure. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` | 216ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å“221 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` | Confirms shared script constants and the `constant:` fixed-point form where supported. |

## Narrow quiet-ready retry after helper correction

The user requested one narrow current/reference comparison before closing the gap. I first submitted `hoi4.probability_inspect` for adapter `decision_ai_will_do`, source `common/decisions/016_mengele_native_prototype_selection_decisions.txt`, candidate pool `mengele_event016_native_select_cloning`, and `refresh = false`. It remained pending for about 180 seconds and was cancelled without a tool result.

I then submitted one `hoi4.probability_compare` request with the cloning Prototype source at `common/decisions/016_mengele_cloning_stage_decisions.txt`, the current selection source at `common/decisions/016_mengele_native_prototype_selection_decisions.txt`, and the explicit id union `mengele_event016_cloning_prototype` plus `mengele_event016_native_select_cloning`. The request used `refresh = false`, outputs `json`, `comparison`, and `unresolved`, and one scenario:

```json
{
  "id": "E016_NATIVE_SELECTION_AI_QUIET_READY_RETRY_2026_10_03",
  "scenarios": [
    {
      "id": "quiet_ready",
      "state": {
        "tag": "MEN",
        "is_ai": true,
        "has_war": false,
        "num_of_civilian_factories_available_for_projects": 3
      },
      "candidateOverrides": {
        "mengele_event016_cloning_prototype": true,
        "mengele_event016_native_select_cloning": true
      }
    }
  ]
}
```

The factory input is the actual dynamic variable consumed by `brilliant_scientist_mengele_cloning_prototype_decision_no_spare_factories` in `common/scripted_triggers/016_mengele_cloning_stage_decision_triggers.txt:116-118`; its threshold is `brilliant_scientist_project_fallback_prototype.cloning_civilian_factories = 2` in `common/script_constants/016_brilliant_scientist_project_constants.txt:126`. The scenario supplies that state input alongside `has_war = false`; `tag = MEN` and `is_ai = true` were actor context, while the only score-modifier inputs were `has_war` and the actual factory variable. It does not claim an evaluated modifier trace or calculate an effective willingness score. The request supplied `candidateOverrides` for the two comparison ids as score-isolation inputs; the timed-out call did not validate how the adapter handled them, and they do not represent native selection eligibility.

The connected live declaration exposes `before` and `after` as unknown objects and `scenarioSet` as unknown. It does not advertise an `inlineClausewitz` or `virtualSource` shape, so I used the documented nonempty `path` sources and did not invent a source kind. The tool returned no schema acceptance or rejection for the nested scenario fields because the call ended with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; timed out awaiting tools/call after 600s`. No comparison id, analysis id, scenario hash, source revision, artifact URI, or render was returned. The score result and nested-field validation are unresolved.

This one-state retry is separate from and does not replace the outstanding full scenario set `E016_NATIVE_SELECTION_AI_2026_10_03` with `quiet_ready`, `war_ready`, `low_factory_margin`, `both_rocketry_native_sources_ready`, `only_flying_bomb_ready`, `only_jet_engine_ready`, `matching_selected_completed`, and `invalid_provider`. The previous candidate-pool, external-factor, and eligibility limitations for those scenarios remain outstanding. Their provider, Theory, receipt, source, and completion fields remain symbolic scenario assumptions, not engine facts; the completed source integration review does not promote them to runtime validation.

The corrected helper snapshots read during this retry were `common/scripted_triggers/016_mengele_cloning_stage_decision_triggers.txt` (local SHA-256 `7318FF6926BBE23321DF66658355E19E88998954C0918861A33B994A45369A8D`), `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt` (`F3AA2D778F847166E36F39A245A04799FE1E31C7818CEAB91825F0D9932989D1`), `common/scripted_triggers/016_mengele_native_prototype_triggers.txt` (`6316A57859BDBF65914D8D11EC935D908D5A3E7B43B7C7A7A350A66441C19982`), and `common/scripted_effects/016_mengele_native_selection_decision_effects.txt` (`AC950026A27264A2617D84EEDD6E65F9956DA4D1D6B66347CC274EE78AFF1FA4`). These are local content hashes, not MCP source revisions.
## Findings and recommended follow-up

The source expressions follow the explicit owner policy: all three selectors copy the correct `ai_high` Prototype expressions, and all three release controls declare the shared zero score. No score tuning change is recommended from this source-only review. The MCP evidence is insufficient to conclude that effective scores, ranking, dominance, starvation, AI validity, or no-autonomous-release behavior are balanced in engine context.

The completed gates were source-reviewed after the user correction. `brilliant_scientist_mengele_native_cloning_selection_is_visible` requires a valid provider, Gotterdammerung, an empty cloning receipt, completed cloning Theory, an incomplete cloning Prototype, and either no existing native selection or a completed native project. `brilliant_scientist_mengele_can_select_native_cloning` adds the private cloning gate, one-source selection guard, and either exact native-project completion or `brilliant_scientist_can_research_mengele_cloning_prototype`. Release requires the matching selected flag, an empty receipt, and no active matching special project. These are source findings, not engine availability results. The zero-cost controls still merit a repetition review for duplicate receipts or contradictory source state; no exploit is confirmed.

When the MCP probability route responds, rerun inspect first, then evaluate the six actions under the same eight scenario ids, sweep the supported war and family-margin inputs, and compare both source pairs with explicit id unions: cloning Prototype to native cloning selection, and rocketry Prototype to both flying-bomb and jet-engine selections. Keep releases as a separate zero-score check. Render the comparison, ranking, or unresolved view when an analysis artifact is available. Preserve returned source revisions, scenario hashes, comparison ids, and artifact URIs in the parent handoff.

No MCP analysis artifacts, revisions, comparison ids, scenario hashes, or rendered evidence paths were returned in this audit. The numeric probability and balance conclusions remain **unresolved**. The full goal remains incomplete and will not be reported as balanced.