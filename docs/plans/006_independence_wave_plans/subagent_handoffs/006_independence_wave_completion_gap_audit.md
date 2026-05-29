# Event 006 Independence Wave Completion-Gap Audit

Read-only audit for Event 006. Gameplay and localisation files were not edited.

## Severe Blockers

1. **Host deletion is still possible.** The current resolver releases each selected tag from a random country that controls any core state for that tag, with no protected host state, no capital reservation, no batch-level state-count check, and no candidate shrink/skip path. Evidence: `events/006_independence_wave.txt:31-50` selects possible countries and runs `release = PREV`; the spec requires capital-preferred host survival validation and skipping/reducing candidates before release (`docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:46-59`, `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md:55-69`).
2. **Event 006 origin is not set anywhere.** Released countries do not receive `chaosx_release_origin_independence_wave`, any origin variable, package type, batch index, host target, or release-count variable. Evidence: `events/006_independence_wave.txt:36-55` only releases tags, adds cores back, sets global display variables, and fires news. This violates the Event 005 separation rule and leaves Soviet republic style/shared tags unprotected from wrong-system routing (`006_independence_wave_spec.md:26-43`, `006_independence_wave_focus_trees.md:15-36`, `006_independence_wave_event005_separation_handoff.md:7-24`).
3. **Release count is fixed and not validated.** The implementation always tries to select 3 candidates (`events/006_independence_wave.txt:31-34`) and displays exactly three global variables (`:52-55`). It does not scale by evolution/chaos tier, valid candidates, host weakness, prior waves, performance, or host survival as required (`006_independence_wave_spec.md:104-117`, `006_independence_wave_decisions_ai.md:39-69`).
4. **The event is still a bare random release button, not the specified system.** Required aftermath decisions, breakaway state-building, focus trees, package overlays, formation routes, scripted GUI, AI equivalents, event logs/details, assets, super-events, achievements, docs, and catalog alignment are absent from implementation surfaces.

## Current Implemented Evidence

- `events/006_independence_wave.txt:22-57`: one hidden triggered event, clears `global.indp_countries`, samples three inactive possible countries with cores, releases them immediately from random controllers, sets three global variables, fires `chaosx.news.6`.
- `events/_chaosx_news.txt:140-156`: one triggered major news event using `GFX_news_event_dutch_soldiers_indonesia`.
- `localisation/english/006_independence_wave_l_english.yml:1-6`: title and one news text, encoded UTF-8 BOM.
- Cluster membership exists only at a high level: Event 6 is in Liberations (`common/scripted_effects/chaosx_event_cluster_effects.txt:247-263`, `:287-305`; `common/script_constants/event_cluster_constants.txt:116-120`; `docs/systems/event_clusters.md:50-56`).
- Event name/debug mapping exists: `localisation/english/chaosx_event_names_l_english.yml:7`, `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:45-46`.

## Surface Status

| Surface | Status |
| --- | --- |
| Event resolver | Partial and unsafe. Immediate release exists, but no scoring, host selection, origin, survival validation, candidate ladder, evolution scaling, package assignment, dossiers, or cleanup. |
| Event 005 separation | Not implemented. No origin flags or blockers; Soviet republic/shared tag handling is absent. |
| Host survival | Not implemented. No protected capital/state logic. |
| Candidate ladder/packages | Not implemented. Only generic existing/core-based possible countries are sampled. High-chaos packages are absent. |
| Decisions/missions | Missing. `common/decisions/chaosx_independence_wave_decisions.txt` does not exist. |
| Focus trees | Missing. `common/national_focus/chaosx_independence_wave_focus.txt` does not exist. |
| Ideas/startup setup | Missing. `common/ideas/chaosx_independence_wave_ideas.txt` does not exist. |
| Scripted effects/triggers/values | Missing. Expected Event 006 helper files do not exist. |
| AI | Missing. No Event 006 AI strategy plan, AI decision behavior, or route AI. |
| Formables/routes | Missing. No formation decisions, origin checks, staged integration, or route reveal logic. |
| Scripted GUI | Missing. No dossier board, congress, patron ledger, or formation ledger. |
| Assets/animation | Missing. No Event 006 asset definitions, DDS outputs, manifests, frame sheets, static fallbacks, or handoffs found. |
| Super-events | Missing. Candidate moments are specified but no Event 006 super-event trigger/text/image/audio package is wired. |
| Achievements | Missing. No Event 006 achievement tracking or icons found. |
| Event log/details/evolutions | Missing. No Event 006 log keys, actor mapping, event-details text, or evolution entries found. |
| Docs/catalog | Stale/incomplete. `docs/events/006_independence_wave.md` is missing; spreadsheet row still says `to be reworked`, `To Be Reworked`, and cluster `Aliens`. |

## Accepted Plans And Disposition

- `006_independence_wave_event005_separation_handoff.md`: accepted correction, not implemented. No origin flag/variable or Event 005 blocker is present.
- `006_independence_wave_instant_release_correction_handoff.md`: partially implemented only in the narrow sense that releases happen immediately. Required hidden scoring, protected host state, origin-before-content, dossiers-after-release, and GUI-after-release are not implemented.
- `006_independence_wave_subagent_deployment_plan.md`: routing plan exists. No subagent handoffs were present before this audit, and no patch handoffs exist for Event 006 implementation.
- `006_independence_wave_improvement_loop_gate.md`: closure criteria are not met. The event is below the first working-system threshold, so this should not be treated as closure.

## Validation Performed

- Read required Event 006 specs and plans listed by the parent.
- Consulted local Paradox wiki snapshot pages and vanilla documentation for events, effects, triggers, decisions, focuses, AI, localisation, scopes, GUI/scripted GUI, graphical assets, and country creation.
- Repository searches for `nr6`, `indp_`, `independence_wave`, `chaosx_event_006`, and origin/package asset keys.
- Checked expected implementation files from `006_independence_wave_spec.md:762-780`; all Event 006-specific decisions/focus/ideas/scripted helper/AI/docs/asset handoff files are missing.
- Read workbook XML for `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; row 7 for Event 6 is stale (`to be reworked`, `To Be Reworked`, cluster `Aliens`).

## Validation Missing

- No game load or error-log validation was run.
- No scenario validation exists for host survival, capital protection, Soviet republic/shared tag origin separation, release count scaling, candidate shrink/skip, or low/high chaos pool gates.
- No decision/focus/country/localisation/asset/super-event/achievement subaudits can pass because those surfaces are absent.

## Asset And Documentation Gaps

- Required report/news images, decision icons, idea icons, focus icon families, achievement icons, flags/cosmetic variants, leader/council portraits, animated GUI sprites, manifests, source notes, and DDS placements are absent.
- No frame-animation package exists for protected-capital seal, warning pulse, congress seal, patron shimmer, formation seal, or other specified animated assets.
- No `docs/events/006_independence_wave.md`, package table, focus route table, decision lifecycle table, validation note, asset manifest summary, or super-event summary exists.
- The event news uses a generic existing image instead of any specified `GFX_*_independence_wave_*` asset.

## Remaining Blockers

- Implement a real Event 006 framework before further completion claims: origin-gated release helper, host scoring, candidate scoring, protected host state, batch validation, release-count target/actual count, and Event 005 separation checks.
- Add a safe baseline ordinary releasable pool first; high-chaos historical/local/strange packages should remain blocked until tags, state mapping, assets, leaders, localisation, and AI are present.
- Add player-facing aftermath decisions and active missions with dynamic costs and cleanup before scripted GUI; GUI should not precede working script ownership.
- Add provisional country setup: startup ideas, emergency armies, focus access, AI strategy, event log/detail entries, and docs.

## Recommended Next Implementation Tranche

1. Build `common/scripted_effects/chaosx_independence_wave_effects.txt`, `common/scripted_triggers/chaosx_independence_wave_triggers.txt`, and `common/script_values/chaosx_independence_wave_values.txt` around origin setting, host survival, candidate scoring, and release count.
2. Replace the 57-line event resolver with a hidden batch pipeline that reserves a capital-preferred host state, validates all candidates together, releases fewer countries when needed, and records actual release count.
3. Implement minimal but complete baseline aftermath: host response category, breakaway survival category, provisional idea set, event details/log entry, and Event 006 origin-gated focus tree access.
4. Add the first small audited country-package tranche only for ordinary releasables and one safe researched package; explicitly queue unsupported historical-return/local-polity/strange packages.
5. Only after the baseline works, route focus/decision/country/localisation audits and asset production subagents, then update docs and spreadsheet.

## Improvement Loop Recommendation

Do **not** request a closure handoff. The event does not technically meet the intended depth and also lacks the baseline framework. After the next working implementation tranche creates resolver, decisions, provisional tree, and at least one package overlay, use `chaosx_improvement_loop_planner` for a concrete expansion addendum if route/package/GUI depth is still shallow and no unresolved addendum already covers it.
