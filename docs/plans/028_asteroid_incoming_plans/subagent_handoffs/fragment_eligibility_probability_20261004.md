# Event028 F03 fragment owner/controller probability audit — 2026-10-04

Disposition: unresolved native acceptance and artifact-payload verification; live declared-pool inspection, evaluation, and mandatory same-scenario comparison returned complete model summaries.
This is a separate F03 tranche and does not replace or modify the frozen [availability probability handoff](availability_probability_20261003.md).
The parent authorized the owner/controller exclusion and declared finite-world fixture construction, not new balance targets.
The auditor changed only this handoff and files under `fragment_eligibility_20261004/auditor/`.
No gameplay source, shared classifier, weights, costs, parent reentry document, mineral appendix, or parent-owned `.gitattributes` was edited.
HOI4 was not launched.

## Source identity and scope

Hashes are raw file SHA-256 values, distinct from MCP canonical source and scenario hashes.

| Source | SHA-256 |
| --- | --- |
| `docs/plans/028_asteroid_incoming_plans/fragment_eligibility_20261004/before/028_asteroid_incoming_triggers.txt` | `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B` |
| `docs/plans/028_asteroid_incoming_plans/fragment_eligibility_20261004/before/chaosx_dynamic_triggers.txt` | `4BC09B54327C90AE73C6ED90446093658BD1E941071AD97ECF7499EC66389FDE` |
| `common/scripted_triggers/028_asteroid_incoming_triggers.txt` | `3B3694273B1A7F6041FBD012A698F6E285359A8EFF9707FF9B9E9BDBA48AFEE8` |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` | `4BC09B54327C90AE73C6ED90446093658BD1E941071AD97ECF7499EC66389FDE` |
| `common/scripted_effects/028_asteroid_incoming_runtime_effects.txt` | `276CBAF89FFCB4071A077DAA6948E787D6BA723FD08D2342332E023F14EB2564` |
| `common/script_constants/028_asteroid_incoming_constants.txt` | `E81036C0CFFA3D9830B220AA4BA7E311F14165D40599B990D316F77E470FE157` |

The exact pre-edit trigger file has SHA-256 `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B`.
The current trigger file has SHA-256 `3B3694273B1A7F6041FBD012A698F6E285359A8EFF9707FF9B9E9BDBA48AFEE8`.
The source-contract audit found exactly one added helper, `asteroid_incoming_country_can_host_fragment_center`, and exactly one changed helper, `asteroid_incoming_state_is_valid_fragment_site`.
Removing the two added OWNER/CONTROLLER calls immediately after generic state validity reproduces the exact baseline fragment-site AST.
The new country helper is exactly `exists = yes`, `uses_normal_civilian_systems = yes`, and `NOT = { tag = CXT }` within a hidden trigger.
The shared civilian classifier is byte-identical to its before capture and expands to actual-nonhuman exclusion, not broad Special Chaos exclusion.
All 65 other trigger definitions are AST-identical.
Generic state validity, selection, neighbor validity, ring validity, the current-Chaos fragmentation helper, and the exact mineral AI predicate retain their baseline AST hashes in [source_receipts_boolean.json](../fragment_eligibility_20261004/auditor/source_receipts_boolean.json).
The runtime and constants hashes match the retained 2026-10-04 baseline identities.

Fresh live lookup evidence:

- Host helper: `common/scripted_triggers/028_asteroid_incoming_triggers.txt:263-269`, indexed revision `72d4ed71fdce75d6b4373927337357fb35e7176839e1501324c8481c63fb8853`.
- Fragment-site helper: the same file at lines 271-301, indexed revision `313beaba1e612cd30fbc1a82762850405d9213467a609039874510eaf0bc495b`.
- Neutral civilian classifier: `common/scripted_triggers/chaosx_dynamic_triggers.txt:62-66`, indexed revision `313beaba1e612cd30fbc1a82762850405d9213467a609039874510eaf0bc495b`.

Concurrent agents change the global index revision; these are per-call evidence, not one frozen workspace revision.
Custom-manifest inspection reports revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` with no scanned source files; it does not independently bind the gameplay revision.
The separate raw hashes and exact AST/source-contract checks establish the declared projection's source identity.

## Declared scenario contract

[finite_worlds.json](../fragment_eligibility_20261004/auditor/finite_worlds.json) contains exactly 23 closed, declared worlds with the same five state-scope IDs: `f03_anchor`, `f03_probe`, `f03_probe_neighbor`, `f03_anchor_neighbor`, and `f03_previous_center`.
These are abstract fixture scopes, not real map IDs or an observed native world.
Country scopes, owner/controller bindings, country/state flags, classifier inputs, adjacency, global arrays, registry count, event targets, and relevant constants are explicit.
The complete candidate universe includes all five states, even when footprint or registry guards exclude a state from center selection.
Country bindings use GER/FRA/ENG and the source's REV human-Special-Chaos, ZIN actual-nonhuman, and CXT system tag branches.
Other external classifier branches are explicitly false.
Dead-owner/controller cases declare invalid country scopes for negative existence tests; they do not claim an observed campaign can contain those ownership bindings.
The source evaluator checks the actual shared classifiers, all site/neighbor/ring predicates, and the unchanged preferential random-state routing limits against every candidate in every supplied world.
It verifies that the actual routing branch pool equals the projected selection pool in all supplied cases; this does not generalize to untested country/continent preference worlds or multi-draw chains.

Both custom manifests use candidate weight 1 and cap 1, exact categorical selection, and no transitions.
Equal-choice weights are a declared model assumption for unchanged implicit `random_state`, not a gameplay tuning change or proof of native RNG behavior.
The identical one-day timer is required API encoding only, with no native timing, cadence, or sequence conclusion.
No seeded simulation, sequence analysis, or timing sweep is warranted by this one-draw, deterministic eligibility contract.

The connected expression evaluator silently rejects parenthesized expressions and does not correctly evaluate the quoted-string equality probes.
The final serialization therefore uses flat boolean/numeric conjunctions and explicit `source_meaningful_settlement`, `source_neighbor_gate`, and `source_is_wasteland` fixture values.
Each derived value is independently checked against the complete current and before source predicates for every state in every world.
They are audit-only inputs, not new source fields, flags, candidate overrides, or unexplained eligibility assertions.
The original and intermediate serialization files are preserved, along with their failed or unsuitable MCP results.
They have the same 23 IDs and underlying finite worlds.
Only serialization-derived metadata changes between these attempts.

Final input files:

- [manifest_before_boolean.json](../fragment_eligibility_20261004/auditor/manifest_before_boolean.json)
- [manifest_after_boolean.json](../fragment_eligibility_20261004/auditor/manifest_after_boolean.json)
- [mcp_scenarios_boolean.json](../fragment_eligibility_20261004/auditor/mcp_scenarios_boolean.json), scenario-set ID `AST_F03_OWNER_CONTROLLER_20261004`
- [audit_fixture.py](../fragment_eligibility_20261004/auditor/audit_fixture.py), read-only source-subset/contract evaluator

Run `python docs/plans/028_asteroid_incoming_plans/fragment_eligibility_20261004/auditor/audit_fixture.py --boolean-category`.
It passes all 23 cases, confirms exact owner-only source changes, and validates the projection inputs and complete selection universes.
This local check is source evidence, not native or MCP probability evidence.

| Fixture | Raw SHA-256 |
| --- | --- |
| `finite_worlds.json` | `228A1701C4B6EA7A275DB6D1E818745B6855A8FC084C67741466D18EE6A2E2E8` |
| `mcp_scenarios_boolean.json` | `EE028848D50D1C3EE457E23356EA784C7795CFAA0DAD163CD16F3BCD892346B0` |
| `manifest_before_boolean.json` | `39CF41117E1E6E6AD474A1B2B2F400F101C6EC84FF68456CC1B2DD3A781373CD` |
| `manifest_after_boolean.json` | `B9C9CC5714CB3C88B5304385F6B7E6F00B41C4B8387710B2ED61B68644824C7D` |

## Scenario-specific findings

A means `f03_anchor`; P means `f03_probe`.
The three other states are retained in the declared universe but are center-ineligible in all supplied cases.
The pool columns below are verified actual-source-subset results for the declared worlds, not observed native outcomes.
Each changed case was also compared individually through live MCP; the other 19 were compared together under their unchanged names and state fixtures.
The MCP change counts below are returned summaries; detailed numeric rows could not be read because of the artifact-provenance blocker.
No native conditional probability is claimed.

| Scenario ID | Before source pool | Current source pool | Live model comparison changes |
| --- | --- | --- | --- |
| `AST_F03_BOTH_HUMAN` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_HUMAN_SPECIAL_OWNER` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_HUMAN_SPECIAL_CONTROLLER` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_HUMAN_SPECIAL_BOTH` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_ACTUAL_NONHUMAN_OWNER` | A+P | A | 2, individual comparison |
| `AST_F03_ACTUAL_NONHUMAN_CONTROLLER` | A+P | A | 2, individual comparison |
| `AST_F03_CXT_OWNER` | A+P | A | 2, individual comparison |
| `AST_F03_CXT_CONTROLLER` | A+P | A | 2, individual comparison |
| `AST_F03_DEAD_OWNER` | A | A | 0, unchanged-19 comparison |
| `AST_F03_DEAD_CONTROLLER` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_IMPASSABLE` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_WASTELAND` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_EMPTY_POPULATION` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_NO_SETTLEMENT` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_MAIN_CRATER` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_EXISTING_FRAGMENT_FLAG` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_MAIN_FOOTPRINT` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_REGISTERED_FRAGMENT_CENTER` | A | A | 0, unchanged-19 comparison |
| `AST_F03_GEO_RESERVED_FIRST_RING` | A | A | 0, unchanged-19 comparison |
| `AST_F03_NEIGHBOR_MODE_ON_ISOLATED` | A | A | 0, unchanged-19 comparison |
| `AST_F03_NEIGHBOR_MODE_OFF_ISOLATED` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_NONHUMAN_NEIGHBOR_AND_RING` | A+P | A+P | 0, unchanged-19 comparison |
| `AST_F03_CXT_NEIGHBOR_AND_RING` | A+P | A+P | 0, unchanged-19 comparison |

The four eligibility changes are actual-nonhuman OWNER, actual-nonhuman CONTROLLER, CXT OWNER, and CXT CONTROLLER.
Human Special Chaos remains eligible as owner, controller, and both.
Dead scopes, impassable/wasteland/empty/unsettled/crater/registered/reserved/footprint exclusions, and isolated-center neighbor modes retain their before behavior.
Actual-nonhuman and CXT neighbor/ring carriers are not narrowed by the center guard.
Source neighbor and ring results are identical across all 23 before/current pairs.
No balance target was selected.

## Live probability evidence

Both final `hoi4.probability_inspect` calls returned `PROBABILITY_SOURCE_INSPECTED`, five candidates, `poolComplete = true`, and zero unresolved inputs.
Before canonical manifest source hash: `8a3ca272d30a4a41051012c583b092947cfa0da595b3255045ea194e63f5fb4b`.
After canonical manifest source hash: `e92a199d8c6d641ccb5e65ac2a5ca809ea3cb31c6f812a0eabc7afaf4ec62634`.
Both evaluations and the required comparison used the identical saved final scenario set and the complete five-candidate universe.

| Operation | Analysis ID | Scenarios / candidate rows | Eligible / excluded rows | Changes | Unresolved |
| --- | --- | --- | --- | --- | --- |
| Before evaluate | `probability-6c57f058672d59ddfb1e0e1a` | 23 / 115 | 34 / 81 | n/a | 0 |
| Current evaluate | `probability-9c75d0e525f0f8a8951b625a` | 23 / 115 | 30 / 85 | n/a | 0 |
| Mandatory compare | `probability-f574512c962eb99e81277895` | 23 / 115 | 30 / 85 | 8 | 0 |

All three returned `PROBABILITY_ANALYZED` with `analysisStatus = complete` for the declared model.
Matching scenario hash: `25124f51b82bc41842fe00077c751b662f839f02bcb414514093ce4d7003d6b1`.
The 34-before/30-current eligible-row totals match the independent source-contract counts.
The four individual comparisons each returned two changes and zero unresolved.
The unchanged-19 comparison returned zero changes and zero unresolved.
These are live analyzer summary facts, not inference from a source-only test.
The final custom manifests retain identical raw candidate weights and caps; raw-value and conditional-probability row payload verification remains blocked.

| Bounded comparison | Analysis ID | Scenario hash |
| --- | --- | --- |
| `AST_F03_ACTUAL_NONHUMAN_OWNER` | `probability-dfaa03dd97376231e817ea6f` | `e15f4fc2cdf9dc76a1cfad00702de2b696983feed54aa8c49017392871fc36c7` |
| `AST_F03_ACTUAL_NONHUMAN_CONTROLLER` | `probability-5c3e7c3d82da1b8e5cfd1370` | `d19653e37ca9ec369a3b2bc88b893eb8532c7686d23dfbca9c3ae8efab09e9f1` |
| `AST_F03_CXT_OWNER` | `probability-7db96582884008e2e593cd0d` | `c8c0826518cd832bdab3d7289f2ed77b4946fcc198198c53ec4e0e52bfcc2029` |
| `AST_F03_CXT_CONTROLLER` | `probability-3aa6f6908d0b36cda7dbadb4` | `aac956d051fd9ddfeaef0a511eeeab7c642678b3afb5ed0c1f571d2a6d1b5321` |
| Other 19 named cases | `probability-4574303c2909e551e4f40fe6` | `7d8f42d62ec8dc0111ac1639404f6ce5a7efaa7597880d52f19ef7dc8d5c3b9b` |

The dominance warnings are the expected single-survivor cases in these intentionally small worlds, not a tuning recommendation.
The three never-eligible candidate warnings reflect explicitly included footprint/previous-center distractors, not an omitted universe.
The parent should not treat these diagnostics or `analysisStatus = complete` as native balance acceptance.

Primary compare artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/034067ced825b3c34ebfa26f751e8debb7013b71621db0641b1374fc59a8afd1/cb097a490798cffb9859ac67b143ed4d8cf7ab4507eaf44a24f37498490ab74c/probability-f574512c962eb99e81277895.json`

All returned summary objects, diagnostics, source revisions, artifact URIs, SHA-256 values, and retrieval errors are retained in [mcp_receipts.json](../fragment_eligibility_20261004/auditor/mcp_receipts.json).
[request_receipts.json](../fragment_eligibility_20261004/auditor/request_receipts.json) records exact route options, referenced input files, unchanged subset IDs, diagnostic probe inputs, and requested retrieval/render bounds.
It references actual before/current source files; no current-current source comparison was used.

## Exact blockers and rejected evidence

The native-source `direct_random` inspect on the runtime file returned `no_weighted_surfaces`, zero candidates, and no available adapters.
Before/current trigger-file inspections also returned zero discovered weighted surfaces.
The live before-path/current-path `probability_compare` returned `PROBABILITY_SURFACE_EMPTY`: “No weighted blocks matched this request.”
This is a current selector-coverage gap, not route absence or a historical timeout.
It provides no numeric native fragment-selection evidence.

The first custom requests were rejected for missing cadence and the 4,096-character predicate limit.
After that schema correction, parenthesized expressions produced all 115 rows excluded and zero changes, with partial status.
Those zero changes are rejected, not accepted baseline equivalence.
A narrow grouping probe confirmed the parenthesis failure against otherwise true explicit state inputs.
The first flat-conjunction serialization reported complete status and eight changes but incorrectly admitted the wasteland probe, producing 35-before/31-current eligible rows.
That result is also rejected as acceptance evidence.
A narrow quoted-string probe confirmed that the equality/inequality expressions did not match the declared string values.
The final boolean-category serialization fixes the model encoding only and matches all source-contract checks.
No external tool code or dependencies were changed.

A fresh 4,096-byte read of the final JSON compare artifact failed:
`Mcp error: -32603: Artifact provenance manifest is unavailable`.
A fresh `probability_render` call with the exact returned final analysis ID and scenario hash failed:
`PROBABILITY_ANALYSIS_NOT_CACHED` — “Render requires a retained analysis ID from this authorized workspace.”
The server emitted JSON/SVG/PNG artifact metadata, but their payloads and images were not successfully retrieved or visually reviewed.
The handoff therefore does not assert verified per-row numeric deltas, raw-score deltas, rendered acceptance, or durable artifact retention.
The bounded per-case comparisons supply scenario-specific summary evidence despite that gap.

A narrow `chaosx.nr28.4` downstream event trace returned `EVENT_INSPECTED_PARTIAL` with whole-workspace graph counts and an inline inventory truncation notice.
It is retained but is not accepted as full Event028 helper-expansion or lifecycle proof.
No broad timeout retries, helper jobs, native tasks, or source writes were used.

## Local reference evidence and remaining coverage

Read through the live reference route:

- Installed `documentation/effects_documentation.md:5574-5585`, `random_state`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:245-289`, including OWNER and CONTROLLER dual scopes, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`.

Installed documentation describes selecting a state satisfying `limit` and optional `prioritize`; it does not establish the model's uniform-choice assumption.
The context bundle omitted four sources at limit two and is not claimed as complete detailed reference coverage.
Targeted searches and reads cover the relevant scope and selector rules above.
No web Paradox Wiki was used.

Native country/classifier scope execution, actual world ownership/control/adjacency, RNG and tie behavior, greedy multi-fragment routing and reservations, effects, chronology, and success/achievement outcomes remain unresolved.
F04 current I/II toggles at impact and F14 read-only near-miss geographic feasibility were not changed or accepted by this F03 audit.
Other Event028 weighted surfaces retain the status and limits in the frozen availability probability handoff; no new result for .1/.8, target-country sampling, preparedness, crater/recovery decisions, sweeps, or capital continuity is claimed here.
The parent's reported 42-case mineral validation is not this auditor's validation and was not re-audited.

Skills used: `chaos-redux-subagents` for read-only ownership/evidence boundaries and `chaos-redux-events` for Event028 integration and review requirements.
No skills were created or modified.
No gameplay simplification or unapproved source fallback was made; the explicit, authorized declared-pool projection remains bounded and is not a substitute for native acceptance.
The event is not claimed complete and this handoff does not choose tuning.
