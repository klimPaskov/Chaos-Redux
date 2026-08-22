# Event 014 Documentation Reaudit - 2026-07-15

> Superseded for current authority by `event014_documentation_consolidation_reaudit_2026-07-15.md`. This same-day checkpoint remains historical evidence only.

## Scope

This was a documentation-only reconciliation of the current Event 014 source specifications, matrices, canonical event document, scenario catalog document, accepted addenda, current asset authority, and status plans. Gameplay, localisation, runtime assets, spreadsheets, and `docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md` were not edited.

The audit used the 2026-07-15 country-package, decision/mission, focus-tree, improvement-loop, visual, flag, portrait, and icon evidence as implementation authority. The 2026-07-13 final completion audit is retained only as a historical pre-origin-removal checkpoint.

## Verdict

| Severity | Findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

The current documentation authority is internally aligned. No current source specification, matrix, canonical status surface, scenario document, accepted-addendum disposition, or root Event 014 asset authority presents the retired fourth origin as live.

## Current authority facts

- Exactly three origins are live: Island Host, Siege Commune, and March Host.
- The focus trees contain 68 local warlord focuses, 108 unified focuses, and 28 Wendigo focuses, for 204 total.
- All 204 focus surfaces have current focus icons.
- The nine Event 014 GFX files contain 812 texture references, 598 unique runtime paths, and 0 missing paths.
- The unified decision package contains 38 distinct live decisions and 38 distinct icons under `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/`.
- The unified decision evidence is divided across three row-range manifests and three row-range handoffs: rows 01-09, rows 10-24 with 14 retained live rows, and rows 25-39.
- The flag package contains 195 flat image-generated runtime TGA files.
- The regional warlord package contains 56 distinct no-prison HOI4-style portraits.
- The ordinary leader animation has 12 independently generated frames. The transformed leader animation has 16 independently generated frames.
- Four action super-events are live.
- Super-event audio contains 8 runtime files at 44.1 kHz: 4 WAV.
- Exactly 18 achievements and an 18-entry read-only staged tracker are live.
- `SCN-010` has five types and is cataloged as `Fully Functional`.
- Manual `SCN-010` launch uses a mutation-free exact preflight for actors, opening-state capacity, external Island/Siege/March state arrays, origin distribution, and reusable slots. Commit starts only after exact equality. Failure changes only the launcher marker and temporary plan state.
- Incarnation reset begins with one idempotent cleanup covering exactly 14 timed missions. Terminal-hunt global-target cleanup is owner-scoped.
- The pre-lock AI package deliberately assigns one first score band per valid target. The post-lock profile is a separate one-time package. This is resolved intentional design, not an open finding.
- Event 014 adds no custom subunit or equipment identifiers. Existing battalion and equipment surfaces remain in use, so no bespoke unit-counter or equipment art is required. This is a verified scope disposition, not a fallback.

## P2-01 closure

Every correction required by `event014_improvement_loop_reaudit_2026-07-15.md` is reflected in current authority:

- Current completion references point to the 2026-07-15 audit set. The 2026-07-13 audit has a prominent historical and superseded banner, and its checkpoint body is preserved.
- The current country-package audit reports P0/P1/P2/P3 all zero after atomic manual-scenario remediation.
- Removed-origin cleanup and regional portrait repair now record closed status with current audit, manifest, and handoff evidence.
- The focus-closure addendum no longer invents inherited prison-origin knowledge and records the live prison/camp route as an independent score factor.
- Both accepted addenda use the live 38-icon count.
- The post-implementation addendum points to the real `static_icons_imagegen/unified_decisions` source, processed, contact-sheet, manifest, and three row-range handoff paths.
- `docs/systems/event_system/triggerable_scenarios.md` records `SCN-010` as `Fully Functional` and documents the exact atomic preflight boundary.

## Secrecy and retired-origin disposition

Current player-facing authority keeps Hannibal Lecter behind `cannibalism_reveal_complete`. Pre-reveal event, focus, decision, GUI, Event Details, achievement-tracker, scenario, portrait, and audio surfaces remain neutral. Documentation may name the character when describing the reveal gate or post-reveal behavior; this does not create a player-facing pre-reveal lookup.

Current mentions of the retired Prison Host are limited to explicit removal, exclusion, or historical-checkpoint context. No current gameplay or asset authority presents it as a live origin.

## Files changed by this reconciliation

- `docs/specs/014_cannibalism_specs/README.md`
- `docs/specs/014_cannibalism_specs/quality/package_status.md`
- `docs/specs/014_cannibalism_specs/quality/package_validation.md`
- `docs/specs/014_cannibalism_specs/quality/manual_improvement_loop_review.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_11_achievements_scenarios_and_aftermath.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`
- `docs/specs/014_cannibalism_specs/matrices/ai_strategy_matrix.md`
- `docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md`
- `docs/specs/014_cannibalism_specs/matrices/decision_mission_matrix.md`
- `docs/events/014_cannibalism/overview.md`
- `docs/systems/event_system/triggerable_scenarios.md`
- `docs/assets/014_cannibalism/manifest.md`
- `docs/assets/014_cannibalism/gfx_handoff.md`
- `docs/plans/014_cannibalism_plans/014_removed_origin_cleanup_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/014_warlord_regional_portrait_repair.md`
- `docs/plans/014_cannibalism_plans/improvement_loop/2026-07-12_event014_focus_closure_addendum.md`
- `docs/plans/014_cannibalism_plans/improvement_loop/2026-07-12_event014_post_implementation_closure_addendum.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_final_completion_audit_2026-07-13.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localisation_final_reaudit_2026-07-12.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_unified_decision_icons_rows_01_09_2026-07-12.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_unified_decision_icons_rows_10_24_2026-07-12.md`
- `docs/plans/014_cannibalism_plans/audits/event014_documentation_reaudit_2026-07-15.md`

## Meaningful validation

- Rechecked all 12 source spec parts, all 10 current matrices, both accepted addenda, the canonical event document, current status and validation pages, the scenario document, current asset authority, and the current 2026-07-15 audit set.
- Re-ran current-authority searches for `four origins`, `Prison Republic`, `72 focuses`, `208 focuses`, `816`, `39-icon`, `39 decisions`, `unified_decision_icons_imagegen`, the nonexistent consolidated unified-icon handoff, `Needs Testing`, and open-P3 wording. Current authority returned no stale live-scope matches.
- Verified that the old final audit banner precedes the preserved checkpoint body.
- Verified that the accepted addendum points to three existing manifests and three existing row-range handoffs.
- Verified that the scenario, canonical event document, Part 6, Part 11, decision matrix, and package validation agree on atomic preflight and the exact 14-mission reset.
- Verified that current asset and specification surfaces agree on 204 focus icons, 62 idea/modifier textures, 135 decision/category textures, 195 flags, 56 portraits, 12/16 leader frames, 4 super-events, and 8 runtime audio files.

## Simplifications, omissions, and blockers

None. No fallback, historical-count substitution, missing current citation, omitted documentation surface, or unresolved audit finding remains in this documentation scope.
