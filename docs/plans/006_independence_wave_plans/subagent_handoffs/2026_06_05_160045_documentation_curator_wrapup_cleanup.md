# Event 006 Documentation Curator Handoff: Wrap-up Cleanup

Role: `chaosx_documentation_curator`

Scope: docs-only Event 006 Independence Wave cleanup for playable wrap-up and stale-claim correction.

## Files changed

- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_foundation_tranche_handoff.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`
- `docs/assets/006_independence_wave/report_event_images/manifest.md`
- `docs/assets/006_independence_wave/news_event_images/manifest.md`
- `docs/assets/006_independence_wave/flags/manifest.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_160045_documentation_curator_wrapup_cleanup.md`

## Stale claims removed or corrected

- Corrected the active completion boundary: playable technical wrap-up is the current target; optional package overlays, portraits, animations, richer GUI states, and spreadsheet/catalog polish remain future work unless specifically requested.
- Reaffirmed that KUB/ALT expansion notes are superseded historical handoff material, not current Event 006 package, focus, or asset scope.
- Marked the report/news asset blocker as stale. `interface/006_independence_wave_report_event_images.gfx` and `interface/006_independence_wave_news_event_images.gfx` exist, and current report/news DDS references resolve.
- Corrected stale report-image prompt sprite names from `GFX_report_event_independence_wave_old_state` and `GFX_report_event_independence_wave_land_congress` to the implemented `GFX_report_event_independence_wave_old_name` and `GFX_report_event_independence_wave_local_polity`.
- Corrected older plan wording that implied per-release evolution-log progressions. Actual Event 006 evolution rows are release-scale tiers, beginning no earlier than Gathering Storm, not per-country release rows or package-route progression rows.

## Remaining documentation risks

- Many older subagent handoffs remain historical records and still contain obsolete implementation plans. They were not rewritten wholesale; current docs now mark the relevant KUB/ALT, report/news, and evolution-log claims as superseded.
- The worktree contains many uncommitted gameplay, localisation, asset, and spreadsheet changes outside this docs-only task. I did not verify or alter those beyond read-only checks needed to align docs with current filenames and GFX refs.
- Some source specs are still aspirational by design. They now distinguish playable wrap-up from future polish, but they should be re-audited after the parent finishes release-scale evolution log fixes and final decision tooltip cleanup.

## Intentionally not touched

- Gameplay script, localisation, assets, spreadsheets, binaries, and flags.
- Historical per-tranche subagent handoffs except the foundation/improvement plan files that currently summarize completion status.
- Event 005 docs and any non-Event 006 documentation.

## References consulted

- Offline Paradox wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`.
- Repo skills: `chaos-redux-events`, `chaos-redux-subagents`.
