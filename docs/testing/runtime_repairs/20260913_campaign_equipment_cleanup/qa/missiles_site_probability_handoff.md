# Missile site probability handoff

Status: baseline preserved and mandatory post-owner-patch compare complete. This handoff is read-only evidence; no gameplay source was edited, staged, or committed by the auditor.

Surface: `missiles_score_site_candidate` in `common/scripted_effects/032_missiles_effects.txt`, downstream strict-`>` selector `missiles_select_best_site`, and region helper `missiles_assign_site_strategic_region`.

Source identity: baseline SHA-256 `35d8c85e0c6fd7b7e1826135968ad5b2a2e1982d41ce6fb1d8d7ca7b52650903`; owner postpatch SHA-256 `457e2e8fb8aed64bafc585fa74b0b324ae8db226d89edd6b0615fbed85f51111`. Owner receipt: [root_source_edits.json](../root_source_edits.json).

MCP compare: `custom_weighted_pool`, workspace `mod_chaos_redux_ea3b2d67c2c0`, comparison id `probability-70e5f22e3d72a5f285fe6135`, scenario set `event032_missiles_site_factory_gate_scenarios_20260913`, scenario hash `9773f5a64705c398e3d385d62e24dd4f0de85a8b00af867eb535e60abb353925`, 5 scenarios, 25 rows, 15 changed rows, zero unresolved diagnostics, zero regressions, and unchanged adapter/assumptions.

Result: under the exact five-state projection, the military-only, civilian-only, and dockyard-only State candidates each gain raw score +8 after the owner patch; no-factory and existing/core/infrastructure scenarios are unchanged. The representative existing/core/infrastructure site remains the highest projected score. This is raw score evidence for the named scenarios and a deterministic maximum race; it is not a native selection probability.

Native MCP status: both source inspections discovered zero candidates because the adapter does not bind or execute this scripted-effect helper and cannot infer the full `every_owned_state` pool. The five-state manifests are complete only within their declared projection. Their +100000 offset preserves differences and is adapter-only. The after manifest's sum of local factory fields matches the source OR for the named mutually exclusive one-building cases and overcounts a multi-type State, which remains outside the projection.

Paired24 cause: the former `any_state_in` at `missiles_assign_site_strategic_region` supplied both `array` and `strategic_region`, while the offline trigger documentation allows exactly one selector category. The owner repair uses only `strategic_region` plus State-scope `is_in_array` membership. Parent validation found effective region IDs 1..304 complete and unique.

Evidence files: [missiles_site_manifest_before.json](missiles_site_manifest_before.json), [missiles_site_manifest_after.json](missiles_site_manifest_after.json), [missiles_site_scenarios.json](missiles_site_scenarios.json), [missiles_site_probability_baseline_evaluate.json](missiles_site_probability_baseline_evaluate.json), [missiles_site_probability_after_evaluate.json](missiles_site_probability_after_evaluate.json), [missiles_site_probability_compare.json](missiles_site_probability_compare.json), and [missiles_site_probability_native_inspect.json](missiles_site_probability_native_inspect.json).

Remaining uncertainty: native candidate-pool binding, full-world ranking, combined factory-type State semantics, and live engine behavior remain unresolved by the available MCP adapter. No tuning target was selected. A prepatch sweep returned `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`; no postpatch sweep was needed because constants and ranking dimensions were unchanged.
