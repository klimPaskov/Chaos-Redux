# Final decision-category and formable state-puzzle audit

Audit date: 2026-08-09.

Scope covered the nine selected static category pictures, 21 live fixed-state formable category attachments, the reusable state-puzzle template, generated GUI/GFX/scripted-localisation runtime, 21 manifests, runtime DDS assets, and the requested documentation and handoffs.

## Findings by severity

### High

No remaining high-severity defect was found in the reviewed task surfaces after the bounded subject-scope patch below. All 21 selected category attachments have matching scripted-GUI declarations and GUI windows; the generated runtime contains 784 state-piece sprites and 784 runtime DDS files.

### Medium

- The reviewed manifests contain 392 selected formable-state entries and 392 wrapper definitions, while the same installed state id can legitimately occur in more than one formable (the cross-form distinct-id count is 309). The mechanic documentation now uses the entry-based terminology.
- Five manifests use the reviewed legacy geometry shape and are normalized by `.tools/generate_formable_state_puzzle_runtime.mjs`; the remaining 16 use `chaos-redux-formable-state-puzzle/v1`. The generator fail-closed checks and pair validation cover both shapes. This mixed-schema compatibility should remain documented until all manifests are intentionally migrated.
- The installed MCP evidence is GUI evidence rather than a dedicated decision-category route. The existing post-fix inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2eb170613915717fe7e0e9c11bd08511f9859eb45e69e157dc6fc4364bd225e/2cb04c228656f2c3b8bebac39201168bb719516de179c7f4c48d2bbe20188ebe/gui-inspect.d60311b14e0ced7d.json`; compact render status was `GUI_RENDERED`. No fresh long MCP call was made during this final audit.

### Low

- Static category-picture wiring is complete for all nine selected sprites and their DDS paths. Dimension inspection remains an asset-pipeline concern because this audit did not regenerate or reprocess those images.
- The 27 static formable exceptions remain on inherited Vanilla category presentation by design; they are not puzzle displays and must not be inferred from the 21 selected metadata blocks.

## Bounded patch applied

Changed `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt` for the 22 Greater Italy/Sweden-Hungary state wrappers (`chaosx_formable_proclaim_greater_italy_state_{1,846,735,163,103,853,116,182,164}_qualifies` and `chaosx_formable_proclaim_sweden_hungary_state_{138,139,140,915,124,913,919,141,916,38,917,918,666}_qualifies`).

Before: each wrapper used a world-wide `any_country` scan filtered by `is_subject_of = ITA` or `is_subject_of = HUN`.

After: each wrapper enters the explicit `ITA` or `HUN` country scope and uses `any_subject_country` for the same `controls_state` check. Vanilla trigger documentation and the installed Vanilla focus precedent confirm that `any_subject_country` is a country-scope trigger. Because these decisions/categories are explicitly carrier-tagged to ITA or HUN, the subject-control semantics are equivalent while removing the forbidden global country scan from repeated GUI/scripted-localisation evaluation. Greater Italy and Sweden-Hungary transfer-state behavior in `common/decisions/formable_nation_decisions.txt` is unchanged.

No generated runtime file was hand-edited and no AI weights, buttons, event targets, on-actions, caches, animation, or balance values were changed.

## Task-specific validation

- `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt`: 392 state-wrapper definitions, 21 territory helpers, 0 `any_country` scans, and 22 `any_subject_country` clauses after the patch.
- `common/decisions/categories/zzz_chaosx_formable_state_puzzle_categories.txt`: 21 category attachments.
- `common/scripted_guis/chaosx_formable_state_puzzles.txt`: 21 scripted-GUI blocks.
- `interface/chaosx_formable_state_puzzle_*.gui`: 21 GUI windows.
- `interface/chaosx_formable_state_puzzles.gfx`: 784 unresolved/qualifying sprite registrations.
- `gfx/interface/formables/state_puzzles`: 784 runtime DDS files.
- `docs/formables/state_puzzles`: 21 manifest directories; normalized manifest state-entry total is 392.
- `.tools/generate_formable_state_puzzle_runtime.mjs` has the selected-category set of 21, fail-closed manifest discovery, legacy normalization, 440x180 projection checks, and unresolved/qualifying runtime-DDS checks. The generator was not rerun because the only source change in this audit was the non-generated trigger scope patch.
- `interface/chaosx_decision_category_pictures.gfx` contains nine sprite registrations, and all nine referenced DDS paths exist in the workspace.

## Remaining risks and blockers

The MCP decision-inspection route is not exposed in the installed tool inventory, so direct decision-surface evidence remains unavailable. The cited GUI artifact and compact render status are retained as the closest supported presentation evidence. Live in-game consumer validation remains parent/user-owned. No simplifications or unapproved fallbacks were introduced by this audit.
