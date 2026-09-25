# Event 016 Mengele Singularity incident recovery AI audit

Date: 2026-09-25.

Role: read-only `chaosx_ai_probability_auditor`.

Disposition: `unresolved` for MCP-confirmed willingness results and historical comparison because the connected probability adapter did not evaluate this source; implementation existence and the declared base input are source-reviewed only.

No gameplay balance target is selected or proposed by this audit.

## Audited surface and source trace

The requested native decision is `mengele_event016_singularity_incident_recovery` in `common/decisions/016_mengele_singularity_incident_decisions.txt:8`.

Its only `ai_will_do` clause is `base = constant:brilliant_scientist_project_board.ai_urgent` at line 57; the referenced constant is `ai_urgent = 25` in `common/script_constants/016_brilliant_scientist_project_constants.txt:77`.

This is a source-traced raw base willingness input of 25 with no local AI modifiers; MCP did not confirm an evaluated score, so the effective willingness result remains unresolved.

An `ai_will_do` value is a willingness score, not a click probability, and this singleton audit does not include the other decisions an AI may choose among.

The decision is visible when `brilliant_scientist_mengele_singularity_incident_is_active` is true and is available only through `brilliant_scientist_mengele_singularity_incident_recovery_can_start` and the native cost gates in `common/scripted_triggers/016_mengele_singularity_incident_triggers.txt:50-67`.

Those gates require an active incident, a valid Mengele provider, no active or stale recovery receipt, at least 35 Political Power, 300 Support Equipment, 500 fuel, and 2 civilian factories available for projects; the provider helper also checks the directorate registry, live program route and idea, and terminal or invalidation flags in `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16-51`.

The native decision reserves 2 civilian factories, declares `ai_hint_pp_cost = 35`, and has a 60-day removal timer in the decision source; these are source context and were not interpreted as AI-score modifiers.

## Named MCP scenarios

Scenario set: `016-mengele-singularity-incident-recovery-ai-2026-09-25`; actor `GER`; the candidate pool contains only `mengele_event016_singularity_incident_recovery`.

| Scenario ID | Declared state | Declared flags |
| --- | --- | --- |
| `016-SING-RECOVERY-VALID-PROVIDER-ACTIVE-INCIDENT-PAYABLE` | Political Power 100; Support Equipment 500; fuel 1000; project-available civilian factories 3. | `mengele_clone_focus_directorate_project_registry`, `mengele_event016_singularity_incident_active`, `germany_mengele_faction`. |
| `016-SING-RECOVERY-VALID-PROVIDER-ACTIVE-INCIDENT-INSUFFICIENT-COST` | Political Power 34; Support Equipment 299; fuel 499; project-available civilian factories 1. | Same registry, incident, and faction flags as the payable scenario. |
| `016-SING-RECOVERY-INVALID-PROVIDER-ACTIVE-INCIDENT` | Political Power 100; Support Equipment 500; fuel 1000; project-available civilian factories 3. | Payable scenario flags plus `germany_mengele_program_closed`. |

The vectors straddle the source affordability thresholds: the payable case is at or above every threshold, while the insufficient case is below each. The invalid-provider case carries a source-defined closed-program flag that fails the provider helper.

The connected adapter accepts only flat primitive state, flags, and scopes; it cannot establish the provider's required idea and compound scripted-trigger state from these records. These are named scenario contexts, not engine-validated availability fixtures. The inspected AI block itself required zero inputs because its base contains no modifiers.

The singleton candidate is complete only for this requested row. The category-wide available-decision pool, external decision scores, and click-selection race are outside scope and were not analyzed.

## MCP evidence

The required first `hoi4.probability_inspect` attempt with `source` as a string was rejected with `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Invalid input: expected object, received string at source`.

The corrected source-specific inspect used adapter `decision_ai_will_do` and `{identifier: "mengele_event016_singularity_incident_recovery", path: "common/decisions/016_mengele_singularity_incident_decisions.txt"}`.

It returned `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, scanned `mod:common/decisions/016_mengele_singularity_incident_decisions.txt`, source revision `3d42628aee06ff7af863e39241fc10846f2f98b1607ed57de4ab2e01df2ecadf`, and MCP source hash `8b0d675864b8c97b881b3613982b090643beddd79027fd96b89e413fb18f990e`.

The exact inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e847fe843a82806978dbb9273a26728a70144bbce3049492e59201ed3b6c5f8/fd3959c37cbb7bed7806ef36126fff5807b5c571f94c0766e5071afc8d0219dd/probability-inspect-8b0d675864b8.json`.

Inspect reported `requestedAdapter=decision_ai_will_do`, `suggestedAdapter=mission_ai_will_do`, `discoveryReason=identifier_not_found`, zero candidates for the requested adapter, and exactly one candidate under `mission_ai_will_do`, where both `identifierMatches` and `candidatePoolMatches` were 1 and the candidate example was the requested decision ID; required inputs and unresolved count were both 0, with no diagnostics or blockers.

The adapter therefore did not expose this native decision under the requested decision surface. The inspect result is evidence of its classification, not of a score.

`hoi4.probability_evaluate` was attempted with the same three scenario IDs, current source, singleton candidate pool, and `raw_value` metric under both the suggested `mission_ai_will_do` adapter and requested `decision_ai_will_do` adapter.

Both calls returned status `error`, code `INTERNAL_ERROR`, blocker `Unexpected internal error`, empty `filesScanned`, and no artifact; neither produced numerical outcomes or a scenario hash.

`hoi4.probability_compare` was attempted with the same scenario set and candidate pool under both adapters, using the absent-before inline source `# absent at HEAD 653ca61aec846e202c52f462c1ba4785fbbdd098` and the current source object as `after`.

Both calls returned status `error`, code `PROBABILITY_SURFACE_EMPTY`, message `No weighted blocks matched this request`, and no artifact; details named the corresponding requested adapter, the absent inline source, the singleton candidate pool, and `availableAdapters=[]`.

No comparison result, scenario hash, or historical score delta was produced. The empty-before source could not be compared through this route; do not infer a zero-to-25 historical delta.

## Frozen before state, revisions, and validation boundary

Repository `HEAD` at audit time was `653ca61aec846e202c52f462c1ba4785fbbdd098`.

`git cat-file -e HEAD:common/decisions/016_mengele_singularity_incident_decisions.txt` returned `fatal: path 'common/decisions/016_mengele_singularity_incident_decisions.txt' exists on disk, but not in 'HEAD'`; the current decision file is added in the shared checkout and its local SHA-256 is `FDD1B158E7E1C98FEAE17EC1082BFED2902120D69765E767521AC0063B753F39`.

Related source hashes reviewed were `C6D286D429C6C5270256D78F64ACD992776137CDD336D9535EEF8E2B79459CDD` for the incident triggers, `86217F4A10AE1F84FBC7E73ADD2029F092F00AD72A250F6E868AD3B7B38FAA7E` for the Mengele provider triggers, and `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131` for the project constants.

The decision-mod and AI-mod pages in the offline `paradox_wiki/` snapshot and the relevant vanilla trigger/effect documentation were consulted; the eleven core offline wiki pages and vanilla documentation were also consulted earlier in this same Event 016 audit thread.

No sweep or render was run because the inspected expression has one constant base, the required evaluator returned no analysis, and the user requested no optional long analysis. No probability, rank, dominance, starvation, or threshold conclusion is available from MCP.

No gameplay files were edited. This handoff is the only file created by this audit; shared checkout changes were left in place, with no staging or commit.

## Parent follow-up

Keep the decision's effective AI willingness unresolved until the MCP route can inspect and evaluate this source as a decision or mission candidate without the internal error.

If the parent needs a historical comparison, the MCP compare route must first support a zero-candidate absent-before source or an equivalent explicit empty manifest; the current attempted empty-source compare is blocked as recorded above.
