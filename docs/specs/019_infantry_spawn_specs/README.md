# Event 19 Infantry Spawn Planning Package

> **Current-state routing (2026-07-18):** This source specification is paired with the implemented and resolved near-completion addendum at `docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`. Older references below to a closure without an addendum or to two pending owner decisions are historical. Exactly two engine-constrained substitutes were approved: exact recorded-formation recreate/prove/delete and controlled one-formation combat trials. The addendum findings were implemented. The 27 fixed technical identity slots are 20 claimant army/muster scenes, 6 fantastical massed-host scenes, and 1 neutral unassigned muster scene, never an individual focal person. Their stable `GFX_portrait_*` names remain engine and UI terminology, not a description of the depicted content.

> **Current implementation extension (2026-08-09):** The accepted design remains the source specification, while the implemented provider bridge now covers 18 static Event 19 provider IDs (`501-514`, `518`, `520-522`). Event 016 adds the separate Germany/Mengele-gated Aryan clone provider 522 beside providers 504-510; it never aliases provider 504. The shared manifest profiles 130-148 carry exact custom equipment obligations, provider 521 remains combat-only on the CBRN side, and provider 513 remains dormant until Event 012 sets its package-ready flag. Event 19 MCP inspection is partial and normalized dynamic provider-pool odds remain unresolved, so the older `Fully Functional` and no-closure language below is historical for the 2026-07-18 tranche and must not be used as current provider-lifecycle proof.

> The provider bridge also exposes a presentation-only `event19_get_management_cost_display` profile-cache callback alongside each provider's ten gameplay callbacks. Ledger-backed zero-debit adapters must identify that boundary in the player-facing tooltip, and the single Event 19 registry rule remains unchanged.

This folder is the source planning package for Chaos Redux Event ID `19`, **Infantry Spawn**.

The request label `017# Infantry Spawn` is preserved in the package history, but the catalog and current repository identify the canonical event as ID `19`. All event, file, registry, achievement, scenario, and documentation identifiers in this package therefore use `019` or event ID `19`.

## Package purpose

The current event is a small repeatable global spawn loop. This package redesigns it as a scalable military disruption system whose identity changes through four evolutions:

1. uneven local musters
2. organized and increasingly advanced formations
3. deliberately requested armies with completely random composition and claimant generals
4. registered Chaos unit families whose reckless use can produce independent nonhuman revolt countries

The design keeps the event repeatable, prevents free equipment farming, separates ordinary lifecycle stages from true evolutions, provides AI behavior, maps the decision-category surface, defines derivative country packages, and includes the requested immediate-mutiny triggerable scenario.

## Folder map

- `specs/` contains the sequential source specification.
- `matrices/` contains implementation-facing design maps for templates, decisions, generals, AI, countries, assets, and cleanup.
- `focus_graphs/` contains the route architecture for derivative nonhuman countries.
- `prompts/` contains bounded handoffs for asset production, achievements, decisions and missions, implementation, and the final implementation goal.
- `research/` records repository findings and historical design anchors.
- `review/` records full source reading, anti-bloat review, manual role-equivalent subagent reviews, uncertainty, and completion auditing.

## Live source-of-truth map

- This folder owns the accepted Event 19 design. Event 19 is ID `19`, `Minor
  Repeatable`, unclustered, nonterminal, and has no fixed derivative tag.
- `docs/events/019_infantry_spawn/overview.md` owns the canonical implemented-system
  explanation.
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md` owns the direct
  scenario contract. The live identity is `SCN-013`; proposed `SCN-008`
  collided with Independence Wave.
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` owns registry contract version 4.
  Event 19 has exactly one dedicated registry code file:
  `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
- `common/scripted_triggers/chaosx_dynamic_triggers.md` owns the shared special
  and nonhuman classifier documentation, and
  `docs/achievements/019_infantry_spawn/achievements.md` owns the eleven
  achievement proof contracts.
- The accepted near-completion addendum named above owns the disposition of its
  three findings. Dated implementation and audit evidence lives under
  `docs/plans/019_infantry_spawn_plans/subagent_handoffs/`.
- `docs/assets/019_infantry_spawn/manifest.md` and `gfx_handoff.md` are the asset
  worker's live evidence surfaces. The 27 fixed identity scenes are separate
  from the 7/18 regional flag candidate. The current approved candidate chain
  is 91 unmodified full-flag ImageGen raws, 91 deterministic 820 by 520 spot
  masters, 273 native PNGs, and 273 runtime TGAs. The independent remediation
  re-audit is PASS and clears the regional asset gate for parent-owned package
  promotion. See
  `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`.
  The machine JSON retains its immutable literal
  `candidate_requires_independent_visual_review` processor-state value. Parent
  workbook/catalog export and reconciliation are complete, Event 19 and SCN-013
  now read `Fully Functional`, and package inventory is complete at 33/33
  current files. The final completion audit is PASS with P0/P1/P2 = 0, so no
  closure gate remains.
- `review/decision_only_surface_addendum_2026-08-05.md` is the accepted current
  UI-surface decision. It supersedes the earlier scripted-GUI implementation
  handoffs while preserving their source-art provenance as archival evidence.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable
  catalog source. Event 19 and SCN-013 are `Fully Functional`; the exported CSVs
  match those promoted workbook rows and remain generated outputs rather than
  source documents.

The live focus-tree, decision/mission, country-package, localisation,
registry/scenario, evolution-counter, and AI, balance, performance, isolation,
scenario-safety, and exploit specialist audits are clean. The live-final AI
reaudit reports zero P0, P1, or P2 findings. All gameplay specialist gates are
therefore closed. Its evidence is
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_ai_balance_performance_live_final_reaudit_2026_07_16.md`.

The owner-approved Event 19-only deterministic spot-colour flattening exception
is now the current regional source route. The 7/18 raws, spot masters, native
PNG/TGA ladders, validation JSON, and checksum file are the current evidence.
The independent remediation re-audit handoff
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
is PASS and clears the regional asset gate for parent-owned package promotion.
The machine JSON's literal `candidate_requires_independent_visual_review` value
remains an immutable processor-state record and is superseded for approval by
that PASS handoff. The seven retained GHOST_BASE prompt records were recovered
exactly from the original archive and independently matched by the parent. The
7/16 `regional_variants/` composites, motif/composite notes, validation/checksum
pair, and contact sheets remain archival superseded evidence. Workbook/catalog
export and reconciliation, the 33/33 package inventory, and the final
completion audit are complete. Event 19 and SCN-013 now read `Fully Functional`.
The three accepted exceptions and no-other-fallback rule remain explicit.

## Reading order

1. `specs/019_infantry_spawn_spec_part_1_core.md`
2. `specs/019_infantry_spawn_spec_part_2_spawn_engine_and_baseline.md`
3. `specs/019_infantry_spawn_spec_part_3_evolutions_i_and_ii.md`
4. `specs/019_infantry_spawn_spec_part_4_evolution_iii.md`
5. `specs/019_infantry_spawn_spec_part_5_evolution_iv.md`
6. `specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
7. `specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md`
8. `specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`

The matrices and prompts should be read after the sequential specification.

## Deliberate boundaries

The event has no terminal world-end outcome. The derivative countries are dangerous regional actors, not substitutes for the Zombie Outbreak, Death, golem, or future parent event endgames. No super-event is planned because the normal event, its evolutions, and its requested triggerable scenario do not meet the project threshold for a campaign-defining presentation moment. A later globally dominant derivative revolt could justify a separate improvement proposal, but it is outside this source design.

The planning text distinguishes working labels from stable script identifiers.
Final in-world English wording is owned by
`localisation/english/019_infrantry_spawn_l_english.yml` and its aligned Event
19 documentation and catalog fields.

## Process disclosure

All 30 supplied project files were read in full before this package was drafted.
Their hashes and line counts are recorded in `review/source_reading_manifest.md`.

The planning environment initially lacked the custom project-agent runtime, so
its early role-equivalent reviews are preserved as historical design evidence.
Implementation subsequently used project agents with no inherited parent
context. A later required near-completion planner pass produced the routed
addendum named above; its findings were implemented. Dated specialist handoffs
live under `docs/plans/019_infantry_spawn_plans/`.

Implementation also inspected the full local repository, required offline
Paradox wiki snapshot, installed vanilla documentation and source precedents,
and approved reference mods where needed. Current engine limitations,
transaction invariants, and remaining audit gates are recorded in
`review/blockers_and_uncertainty.md`.
