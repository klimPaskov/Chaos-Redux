# Distinct Probability Recovery Review — 2026-08-26

## Scope and disposition

This is a read-only recovery review of the two supplied cached `hoi4.probability_compare` artifacts. No probability analysis was rerun, no new MCP artifact was created, no gameplay source was edited, and the temporary before-source copies are not present in the workspace after comparison.

The recovery comparison is valid as a distinct before/current provenance check: the artifact provenance keeps the temporary before-side source identity separate from the final frozen famine and migration decision sources. The deleted temporary copies must not be reconstructed or treated as current source files. The current source boundary is the final frozen decision implementation recorded by `ai_probability_current.md`.

## Exact MCP evidence

| Surface | Adapter | Analysis id | Scenario hash | Artifact | Comparison result |
| --- | --- | --- | --- | --- | --- |
| Famine decision AI / mission `ai_will_do` | `mission_ai_will_do` (`hoi4-1.19.2.v1`) | `probability-4afd69e0e79bd79eefce0d1a` | `90ebda36ce4ae460b3dd64cbefdb6ae5d5ae4f8deadf0da15828cfec35a13739` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ee35ac8f350bc2e820ac4e71ba492777a718644d576f6d84ad48eec3e1a1746/d989f58eebde25a1a880569a5c8bb072ad9a291ec76bef52f6f6f25b107a856c/probability-4afd69e0e79bd79eefce0d1a.json` | `comparisonChanges=0`; 46 unresolved |
| Migration decision AI / mission `ai_will_do` and corridor modifiers | `mission_ai_will_do` (`hoi4-1.19.2.v1`) | `probability-35fd3b50d64d8a2cbbed5af4` | `d0e5281c91db132e22ea8cfa0c4d9373bbe197d251859451641995bc87b43b26` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e18aeed48d51f13834da02e62224082ea671580383a588d501179eb5c3f7b1a/7a2916fce9cb62258856d61c7e7ff5517c423a9ea95ef08259521beb05219349/probability-35fd3b50d64d8a2cbbed5af4.json` | `comparisonChanges=6`; 134 unresolved; 4 info diagnostics |

Both artifacts use the same documented score-only mission adapter boundary. They do not provide normalized click probabilities, timing distributions, or an exact balance certification. The scenario hashes above are the hashes to preserve for any later same-scenario comparison.

## Famine result

The famine artifact is a distinct before/current comparison with `comparisonChanges=0`. Its 46 unresolved entries are retained as unresolved engine-state evidence, not interpreted as proof that the source sides were identical. The zero delta means no modeled famine willingness-score change was observed under the supplied scenarios; it does not certify eligibility, ranking, starvation absence, dominance absence, or exact selection odds.

Classification: score-only, partial, unresolved for live trigger and scope state. The famine comparison is not a numeric balance certification.

## Migration result

The migration artifact is a distinct before/current comparison with `comparisonChanges=6`, 134 unresolved entries, and four informational diagnostics. The six changes are exactly two corridor modifier changes repeated across three analyzed scenarios (`2 modifiers × 3 scenarios = 6 comparison rows`). They therefore represent the same two corridor-weight edits observed in each scenario, rather than six independent migration logic changes or a broad candidate-pool rewrite.

The six deltas are limited to the migration corridor modifier surface. They must not be described as six new candidates, six rank reversals, six exact probabilities, or proof that all migration actions are eligible. The 134 unresolved entries remain the dominant limitation, and the four info diagnostics do not close that limitation.

Classification: score-only, partial, unresolved for live trigger and target state. The migration comparison demonstrates a bounded corridor-score delta only; it does not certify normalized selection odds, timing, dominance, starvation, repetition, or exploit safety.

## Blocker disposition

Closed blocker: provenance ambiguity is closed for this recovery review. The cached before/current sides are materially distinct in the artifacts, so the prior concern that a zero-change comparison might have resolved the same intermediate source on both sides does not apply to these two supplied recovery artifacts. The temporary before copies were intentionally deleted after comparison and remain historical provenance only.

Retained blocker: exact named-scenario probability certification remains blocked by the adapter/runtime boundary. The artifacts retain unresolved typed scopes, compound eligibility triggers, and other live state required by the scenarios; the migration artifact additionally retains 134 unresolved entries and four informational diagnostics. Dynamic destination, opposition, and relief-donor registries remain outside a complete normalized candidate pool as recorded in `docs/plans/famine_and_migration_system_plans/ai_probability_current.md`.

## Recommended disposition

Accept these artifacts as the authoritative recovery provenance for the famine/migration before/current comparison, record famine as no modeled score delta and migration as the six-row corridor-modifier delta, and retain the live-state/complete-pool probability blocker. Do not claim exact probabilities or full balance closure from either artifact. A future audit may rerun the same scenarios only after the adapter can bind the unresolved typed scopes and complete the dynamic candidate pools; it must preserve the two scenario hashes above and use a fresh comparison against the final frozen sources.

## Sources reviewed

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-mtth/SKILL.md`
- `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_probability_scenarios.csv`
- `docs/plans/famine_and_migration_system_plans/ai_probability_current.md`
- The two exact MCP artifact resources listed above.

No other files were changed.
