# Event 012 Africa Foundation Gap Improvement Handoff

Date: 2026-06-16

Subagent role: Chaos Redux improvement-loop planning. Planning only; no gameplay, localisation, asset, or spreadsheet files were edited.

## Design Problem

The first Event 012 foundation tranche has strong scaffolding but thin playable consequences:

- 32 historical dossier IDs and 11 high-chaos package IDs exist in constants/localisation.
- The scripted effects can register catalogs and mark generic opened/unlocked entries.
- The focus tree has an Authority Atlas, Archive of Old Seats, three aggregate dossier focuses, and two high-chaos branch focuses.
- The decision layer still relies on one generic historical dossier decision and one generic Bestiary decision.

The remaining gap is turning the catalog into macro-region dossier missions, settlement forks, subject/tag surfaces, route-specific AI, source-aware assets, and safe nonhuman/supernatural high-chaos gameplay.

## Files Written

- `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_foundation_gap_improvement_handoff.md`

## Prior Addendum Status

No previous Event 012 improvement-loop addendum was found under `docs/plans/012_africa_plans/`. Existing handoffs are source, text, and audio research handoffs, not unresolved implementation addenda.

## Proposed Expansion

The addendum recommends a focused next tranche:

- Add Authority Register focus/decision depth after `AFR_archive_of_old_seats`.
- Replace three aggregate dossier focuses with macro-regional lanes and mission unlocks.
- Implement 24 historical dossier gameplay packages first, mapped across North/Nile/Horn, West/Sahel, Central, East/Indian Ocean, Great Lakes, Southern/Zambezi, and Madagascar.
- Implement at least 8 high-chaos packages from the existing 11-ID catalog, with explicit nonhuman/supernatural handling and no human-caricature framing.
- Replace thin generic decisions with selected-dossier, survey, local office, guard, monument/regalia, settlement, forgery crisis, and package-specific Bestiary decisions/missions.
- Treat most historical dossiers as no-tag offices in the first playable pass; spawn subject tags only after country, flag, leader, AI, and source blockers are cleared.

## Research Basis

Local sources read:

- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/prompts/012_africa_coding_prompt.md`
- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`
- `docs/specs/012_africa_specs/specs/012_africa_niche_country_expansion.md`
- `docs/specs/012_africa_specs/specs/012_africa_high_chaos_absurd_paths.md`
- `docs/specs/012_africa_specs/matrices/012_africa_acceptance_criteria.md`
- `docs/specs/012_africa_specs/matrices/012_africa_decision_map.md`
- `docs/specs/012_africa_specs/matrices/012_africa_ai_strategy_matrix.md`
- `docs/specs/012_africa_specs/matrices/012_africa_expanded_subject_matrix.md`
- `docs/specs/012_africa_specs/matrices/012_africa_absurd_high_chaos_routes_matrix.md`
- `docs/specs/012_africa_specs/matrices/012_africa_asset_matrix.md`
- `docs/assets/012_africa/source_research/manifest.md`
- Existing source/audio/text handoffs under `docs/plans/012_africa_plans/subagent_handoffs/`

Implementation files inspected:

- `events/012_african_union.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/ideas/012_africa_ideas.txt`
- `localisation/english/012_african_union_l_english.yml`

External historical cross-checks included UNESCO pages for Aksum, Meroe, Great Zimbabwe, and Kilwa; Britannica pages for Kanem-Bornu, Songhai, Asante, Oyo, Buganda, Bunyoro/Buganda, and Merina; and the Metropolitan Museum of Art Benin chronology page.

## Implementation Surfaces Affected

If accepted, the main agent will likely touch:

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/ideas/012_africa_ideas.txt`
- `events/012_african_union.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `interface/`, `common/scripted_guis/`, and `interface/*.gfx` if the selected-target UI is implemented now
- `common/country_tags/`, `common/countries/`, `history/countries/`, `gfx/flags/`, and `common/characters/` only for accepted spawned tags
- AI strategy files or existing AI surfaces
- Event docs/specs/matrices after implementation

## Open Questions and Blockers

- Which existing untracked country/tag/flag files in the worktree are accepted parent work and which are provisional?
- Should the first playable tranche spawn any historical subject tags, or should all historical dossiers start as no-tag offices until assets and country packages are audited?
- Are neutral Archive placeholder emblems acceptable for Low-confidence historical asset rows, or must those rows wait for rights-clean sources?
- Should the selected-target Authority Register be implemented through scripted GUI in this tranche, or should it remain decision-category driven until the dossier missions are stable?
- Final super-event titles, quotes, images, and audio remain research-gated and should not be inferred from role labels.

## Promotion Recommendation

Keep the addendum in `docs/plans/012_africa_plans/` until accepted. If accepted, promote the implemented parts into the focus-tree, decisions/UI, country-package, evolutions/world-end, acceptance, decision-map, AI, and asset specs listed in the addendum. Do not promote unimplemented package details as if they are source-of-truth gameplay.
