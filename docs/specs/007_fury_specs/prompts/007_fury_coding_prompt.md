# Coding prompt for Event 007 Fury

Event 007 Fury is implemented: actor selection, package, finite reserve, target loop, opening and territorial-gain news, the 52-focus tree, both decision categories, the triggerable scenario, both super-events, the world-end branch, and ten achievements.
Do not rebuild any of it from the older planning text.
Read the [README](../README.md), the [accepted release corrections](../specs/007_fury_release_corrections_2026-10-05.md), and `docs/plans/007_fury_plans/agent_decisions_2026-10-05.md` before changing source.

Follow `CLAUDE.md` and the `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-focus-trees` skills for any change.

## Remaining source work

These items repair consistency with accepted design and need no new design decision:

- `fury_form_war_table_tt` and `fury_assign_terminal_fronts_tt` in `localisation/english/007_random_expansion_l_english.yml` still promise pact cohesion, which is retired; describe the real pact membership, idea, preparation, momentum, and overextension effects instead.
- `fury_terminal.reserve_cohesion_gain` and `fury_terminal.fronts_cohesion_gain` have no reader and can be removed.
- Literal tuning values remain in source: momentum additions of `1` and `3` in `common/decisions/007_fury_decisions.txt` and `common/scripted_effects/007_fury_effects.txt`, and overextension gates of `5` and `4` in the target and settlement decisions; move them into the `fury_balance` or `fury_decision_cost` constant blocks.

## Work that needs a decision first

Implement these only after the README's open questions record an accepted disposition:

- the Internal Fury branch (War Directorate, Civil Mobilization, Compliance Administration) and its institutional portrait.
- ordinary per-country defeat news.
- the audit proposals for momentum, a single strain value, spent target preparation, anti-Fury mission map checks, harsh-coring migration pressure, Random War overlap, internal fracture, and actor-milestone evolution application.

Any accepted change to AI weights, target scores, or reserve values needs a before-and-after comparison through `chaosx_ai_probability_auditor`.

## Validation still owed

Release sign-off still lacks full event, focus, and probability coverage, the post-change focus render, a populated Event Details review, overlay composition, and legacy asset provenance; see `docs/plans/007_fury_plans/release_review_2026-10-05.md`.
Catalog wording is queued in `docs/plans/007_fury_plans/catalog_changes_pending.md` for the spreadsheet owner.
Report every remaining blocker or simplification; do not claim completion while any of the above stays open.
