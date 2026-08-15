# IW-033 / IW-041 focus-depth queue

Status: superseded as an implementation blocker; retained as historical breadth-risk evidence.  
Parent decision: the shared generic tree is accepted and the Level 2 country-specific-focus expectation is waived.  
Owner: main Event 006 implementation agent.  
Reason: the package candidate registry/spec marks KAR and CRI as Level 2 and expects one country-specific focus group per package, but the accepted implementation currently exposes only the shared `independence_wave_focus_tree` and package-specific non-focus content.

## Guardrails

Preserve the accepted one-tree architecture. Do not create a second KAR or CRI focus tree, do not load a focus tree over a meaningful vanilla tree, and do not weaken `has_independence_wave_generic_focus_contract`. Any implementation must be a gated module inside `independence_wave_focus_tree` and must use the existing package assignment, regional ambition, power-struggle, route-lock, and cleanup helpers.

## Evidence of the gap

- `docs/specs/006_independence_wave/spec_part_5_country_packages_and_regional_overlays.md` classifies IW-033 and IW-041 as Level 2 and calls for one country-specific focus group.
- `common/national_focus/006_independence_wave_focus.txt` and the imported `006_independence_wave*_focus.txt` files contain no KAR/CRI/IW-033/IW-041 focus identifiers or package-specific focus blocks.
- `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:448-538` assigns the full shared tree and publishes package effects, force profiles, power struggles, ambition/signature/league registration, and package AI flags.
- `docs/plans/006_independence_wave_plans/006_generic_focus_contract_closure_handoff_2026_08_02.md` closes broad generic-tree expansion and rejects bespoke trees without a new accepted design.

## Narrow implementation options

Option A, if the Level 2 requirement remains authoritative: add one small gated shared module for each package, with distinct KAR forest-frontier and CRI peninsula/return institutions, route-aware prerequisites, package-local rewards, and a meaningful end state. Keep the module inside `independence_wave_focus_tree`, gate it on the existing package identity and `independence_wave_ambition_family_registered`, provide unique icons/localisation/AI, and wire cleanup through `independence_wave_clear_focus_runtime`. The module must not duplicate the four government or four host lanes.

Option B, if the generic-tree closure is authoritative: update the candidate registry/spec to explicitly waive the Level 2 country-specific-focus requirement for IW-033 and IW-041, documenting that package decisions, ideas, force mapping, power struggles, regional ambition, and AI provide the accepted differentiation. Do not silently leave the mismatch undocumented.

## Acceptance checks before implementation or waiver

- Parent accepts one option and updates the source-of-truth spec/candidate registry.
- Any new focus IDs have unique prerequisites, mutual exclusions, icons plus `_shine`, localisation title/description/custom tooltip, varied rewards, and route-aware `ai_will_do`.
- `hoi4.focus_inspect` and `hoi4.focus_render` show no new crossings or overlaps and preserve the shared layout contract.
- Package attestation remains fail-closed until decision, localisation, AI, and asset audits promote the rows.
- `chaosx_ai_probability_auditor` receives named KAR/CRI focus-selection scenarios for any new or changed weighted focus logic.

No gameplay edits were made while recording this queue.

## Parent decision (2026-08-05)

The parent accepts the shared generic Event 006 tree for IW-033/KAR and IW-041/CRI and waives the Level 2 country-specific-focus expectation for these packages. This queue is superseded as an implementation blocker and is retained only as historical breadth-risk evidence. No country-specific focus tree or focus group should be added without a new accepted design; any future breadth work must remain inside the shared tree and use the existing assignment, route-lock, cleanup, localisation, icon, and AI evidence contract.
