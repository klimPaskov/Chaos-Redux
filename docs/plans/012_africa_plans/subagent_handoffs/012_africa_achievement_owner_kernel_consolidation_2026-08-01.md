# Event 012 Africa achievement-owner kernel consolidation — 2026-08-01

## Scope

This tranche consolidates existing Event 012 full-action outcome branches onto the declared achievement owner helpers. It changes no achievement threshold, tag, model, asset, AI weight, recurring scan, or readiness gate.

## Exact callers

`africa_achievement_record_full_action` in `common/scripted_effects/012_africa_achievement_effects.txt` now calls:

- `africa_achievement_record_development_project` for each counted rail, river, port, processing, food-reserve, development-fund, and industrial-plan project.
- `africa_achievement_record_socialised_resource_project` for a full processing project under the People's Union constitution.
- `africa_achievement_record_diaspora_owned_project` for a full diaspora investment-bond project.
- `africa_achievement_record_disease_outbreak_contained` for the full disease-containment action.

The preceding state or country guards remain unchanged, so project families and counted-state flags still prevent duplicate credit. The disease helper's existing active-outbreak guard is now authoritative; a containment action cannot manufacture a containment count when no outbreak is active.

## Acceptance boundary

These are owner-callsite closures only. They do not award an achievement by themselves. Development stability, region coverage, confidence, exploitation-scandal disqualification, voluntary-return conditions, and the remaining disease severity/end-state gates remain open exactly as recorded by the matrix and achievement triggers.

## Validation

The touched script remains balanced by the repository brace/quote scan. A targeted symbol audit finds the four declared helpers in their intended full-action branches and removes their previous inline duplicate counter writes. Focused HOI4 event inspection remains the required parser evidence; no live game was launched.

## Remaining blockers

Civilian disaster damage, model-dependent elephant proofs, forced relocation/scenario proof, other-world-end proof, and terminal super-event proof still have no exact caller. W5, unique continent packages, audio/rights, native-language review, model production, live scenario acceptance, and the existing Event 006 binding gates remain unchanged.
