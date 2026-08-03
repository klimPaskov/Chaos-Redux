# Event 012 disease-action gate disposition

## Scope

This handoff closes an unreachable-action defect for `contain_emergent_disease` (71) and `research_disease_countermeasure` (72) without inventing a disease source, country tag, or Event 013 API.

## Finding

Both action profiles and shared quote, mission, result, and cleanup kernels were present, but the target validator required `africa_disease_crisis_active` or `africa_disease_research_site`. Neither receipt had a positive Event 012 writer. The selectors were visible after Evolution III, so the player could open an action that could never validate. The AI picker could also sample those concepts even though their target gate was unwritten.

## Changes

- `common/decisions/012_africa_decisions.txt` now requires `africa_fictional_pathogen_review_authorized` before Actions 71 and 72 appear.
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt` requires the same package gate for AI Actions 71 and 72; Action 73 keeps its separate authorisation check.
- `common/scripted_effects/012_africa_ai_profile_effects.txt` samples disease actions only when that package gate is present; the default high-chaos picker excludes 71–73 while the package is absent.
- `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` reclassifies rows 71 and 72 as `blocked_with_gate`.

## Required future owner

An accepted fictional-disease package must write the authorisation receipt, create a target-owned crisis or secure research-site receipt, implement Action 72 laboratory-accident outbreak creation, and close all target/site/quarantine flags through the existing shared cleanup. A host-only flag is not sufficient because the country-target execution path excludes the host.

## Validation

Focused source assertions should confirm the two selectors, AI gate, and picker all reference the same package authorisation flag; the action profiles and target validator remain present. No new tag, model, disease API, or real-world pathogen procedure is introduced.
