# Prompt for `chaosx_ai_probability_auditor`

Spawn with `fork_context=false`.

Perform a read-only Event 53 probability audit. Do not patch source.

Read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, the complete specification under `docs/specs/053_mysterious_man_specs/`, the final implementation files, and the scripted-system handoff.

Audit every scenario in:

`docs/specs/053_mysterious_man_specs/quality/probability_scenarios.md`

Mandatory surfaces:

- uniform initial player-country target selection
- uniform valid demand-type selection
- demand applicability threshold changes
- fresh uniform consequence-package selection
- exact one-entry registration for every valid package
- exclusion of invalid packages
- no anti-repeat or recent-history weighting
- one-ballot compound packages
- no variant inflation from disasters, independence candidates, characters, or targets
- adapter-rejection redraw behavior
- interval distributions and 45-day floor
- payment progression and stockpile-dumping sensitivity
- affordability samples by country size and tier

Start each surface with `hoi4.probability_inspect`. Use `hoi4.probability_evaluate`, `hoi4.probability_sweep`, and `hoi4.probability_compare` as required. Use `hoi4.probability_render` for pool matrices, threshold sweeps, and before-and-after evidence. Use simulation only for declared uncertain inputs. Do not claim exact probabilities from incomplete pools.

For every scenario, record the complete candidate pool, external factors, scenario hash, artifact references, normalized result, and classification as exact, bounded, sampled, score-only, or unresolved.

Write the audit to:

`docs/plans/053_mysterious_man_plans/subagent_handoffs/ai_probability_audit.md`

Flag any duplicated entry, hidden weight, missing candidate, incomplete owner adapter, dominance, invalid timing, or unsupported exact claim. Recommend file and identifier fixes without applying them.
