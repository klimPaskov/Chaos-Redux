# Event 006 Completion Gap Audit - Independence Wave

Date: 2026-05-30 09:16 UTC
Agent: chaos-redux event completion audit subagent
Scope: read-only audit against the Event 006 source-spec pack, current docs, accepted plan addendum, and current implementation.

## Bottom Line

Event 006 has a working first-pass resolver, origin-gated release setup, a provisional focus tree, several decision ledgers, starter package/formable content for OGB/ASY/DNZ/UGA/SOK plus railway/compact content, event-log rows, localisation, ideas, constants, triggers, and AI scaffolding.

The full Event 006 source-spec pack cannot honestly be claimed complete. The largest blockers are reduced-territory release handling, package depth and coverage, achievements, super-events, final assets/GUI, and unresolved Event 005 visual/tag separation for shared-package material.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Entry event and resolver | Partial | `events/006_independence_wave.txt:23` defines `chaosx.nr6.1`; release loop uses `release = PREV` at `events/006_independence_wave.txt:93`, with host-state reservation before release. |
| Release count scaling | Partial | Constants include min/max ranges, but `independence_wave_prepare_release_count` only selects the tier minimum at `common/scripted_effects/006_independence_wave_effects.txt:8`. |
| Host survival | Partial | Safety trigger requires a non-candidate owned state and prevents reserved-state reuse at `common/scripted_triggers/006_independence_wave_triggers.txt:186`, but there is no reduced-territory shrink/fallback path. |
| Event 005 separation | Partial | Core origin guard exists in `is_independence_wave_release` and setup flags, but OGB still carries Event 005-branded portrait/source surfaces per the earlier country-package audit and `history/countries/OGB - Old Great Bulgaria.txt:29`. |
| Focus tree | Partial | `common/national_focus/006_independence_wave_focus.txt` has 46 focuses, 46 `ai_will_do`, and origin-gated tree loading, but it is still a modular starter tree rather than the full source-spec route family. |
| Decisions and missions | Partial | Host, committee, congress, patron, formation, and border categories exist, but host/major/old-archive/sealed-dossier/scripted-GUI decision families are thin or absent. |
| Country packages | Partial | Verified starter packages exist for OGB, ASY, DNZ, UGA, SOK and generic railway, but the source-spec minimum of six historical/local packages from three continents plus strange/containment packages is not met. |
| Event log/details | Partial | Dossier/package/formation log types and localisation exist for current packages; future package, super-event, and achievement rows are missing. |
| Localisation | Mostly current for implemented gameplay | `localisation/english/006_independence_wave_l_english.yml` is UTF-8 BOM and has no `:0` key format hits in the checked file. Missing localisation follows missing systems. |
| Assets | Blocked for completion | No Event 006-specific report/news/super-event/focus/decision/idea/achievement asset pack was found. The news event uses `GFX_news_event_dutch_soldiers_indonesia` at `events/_chaosx_news.txt:148`. |
| Scripted GUI | Missing | Source specs call for Dossier Board, New States Congress, Patron Ledger, and Formation Ledger GUI windows; no Event 006 GUI or scripted GUI surface was found. |
| Achievements | Missing | `common/achievements/chaos_redux_achievements.txt` has no Event 006 `cr_*`, `independence_wave`, or `chaosx_iw` achievement definitions. Current similarly named achievements are Event 005/Soviet Collapse content. |
| Super-events/audio | Missing | No Event 006 super-event effects, sprites, localisation, audio, or catalog entries were found. |
| Documentation | Partial/stale | `docs/events/006_independence_wave.md` accurately admits many gaps, but some future-work language is stale after later package/ledger tranches. The accepted improvement addendum remains open and only partly implemented. |

## Source-Spec Gap Table

| Surface | Spec expectation | Current state | Severity | Recommended next tranche |
| --- | --- | --- | --- | --- |
| Reduced-territory release | Release valid reduced starts when full `release = TAG` would erase the host or break survival requirements. | Resolver uses full `release = PREV`; safety is skip-only with one protected host state. Docs also state no reduced-territory candidate starts. | Blocker | Implement reduced-territory package/release variants with explicit state proof and host survival validation. |
| Release count ranges | Baseline 3-5 through Evo V 10-16, with chaos-tier range behavior. | The count target always uses the tier minimum despite max constants existing. | High | Add range/randomization or documented deterministic tier target that matches the spec. |
| Dossier capture | Dossiers should record the wave after release and scale to high-tier release counts. | Releases are stored in an array, but named globals are only captured for countries 1-5 while Evo targets exceed five. | High | Extend details/reporting to use arrays or store all high-tier releases. |
| Package ladder | Ordinary, dormant, city, protectorate, historical, local, strange packages with bespoke data and validation. | Generic tier scoring exists; only OGB/ASY/DNZ/UGA/SOK plus railway have starter package content. Strange pool is any ordinary candidate at chaos tier 5. | Blocker | Add package tranche for missing historical/local packages and separate strange/containment packages. |
| Minimum package set | At least six historical/local packages from three continents, at least two strange packages, and one containment path. | Current bespoke set is short of required count/depth and has no true strange/containment package. | Blocker | Build the remaining package minimum before any completion claim. |
| Focus tree depth | Modular tree with opening, civic, military, revolutionary, national directorate, patron/anti-patron, historical/local, coalition, border, crisis, and strange modules. | Provisional 46-focus tree covers trunk, mandates, package overlays, compact, and railway, but lacks full anti-patron, crisis, strange, and broader package route families. | High | Expand focus modules after package data is finalized. |
| Decisions/AI | Host, breakaway, major, congress, patron, border, old archive, land, sealed dossier, cleanup, dynamic costs, AI. | Several categories exist; host/committee/congress are narrow, major-power category absent, old archive/land/sealed dossier are only partially represented through package/formation content. | High | Add role-specific decision tranche and AI plans for host, major, previous breakaway, package actors, and strange-state containment. |
| Scripted GUI | Dossier Board, Congress, Patron Ledger, and Formation Ledger GUI windows with tooltips/effects/AI/log hooks. | Decision categories stand in for these systems; no Event 006 GUI or scripted GUI files found. | Blocker for full spec | Implement GUI only after decisions stabilize, or formally downgrade the GUI requirement in the source spec. |
| Assets | Full Event 006 asset pack with report/news/super-event images, decision/focus/idea/category/achievement icons, manifests, contact sheets, animation handoff. | No Event 006-specific asset pack found; placeholders/generic vanilla pictures/icons are in use. Flag assets were not touched or audited. | Blocker | Route an asset tranche and wire stable `.gfx` names before claiming completion. |
| Achievements | Implement the `cr_*` Event 006 achievement catalog with origin guards, debug disqualifiers, icons, localisation. | Gameplay tracking flags exist, but there are no Event 006 achievement definitions/icons/localisation. | Blocker | Add achievement definitions, localisation, sprites, and validation hooks. |
| Super-events | Implement candidate super-events such as First League, Great Partition Week, Old Name Returns, Impossible State, League War, Human Renunciation, and Rump That Endures. | No Event 006 super-event wiring found. | Blocker | Implement a first super-event tranche with catalog/audio/image documentation. |
| Event 005 separation | Event 006 must stand apart from Event 005 even when sharing tags. | Origin flags and content gates are present, but OGB asset/leader-source paths remain Event 005-branded; older Event 005-style names also appear in nearby achievements/assets. | High | Audit shared tags and add Event 006-specific aliases or explicit accepted reuse notes. |
| Documentation alignment | Docs/specs/plans should match what is implemented and what remains queued. | Main event doc is mostly honest but still has stale future-work phrasing; accepted improvement addendum remains open and partly superseded. | Medium | Update disposition: implemented, queued, rejected, or promoted into source specs. |

## True Blockers

- Reduced-territory release/fallback is not implemented. Current release handling is a full `release = PREV` guarded by skip-only safety.
- The source-spec package minimum is unmet. Current starter packages do not satisfy six historical/local packages across three continents, and no true strange/containment packages exist.
- Achievements are absent as actual achievements. Event 006 only seeds tracking flags.
- Super-events/audio/catalog surfaces are absent.
- Event 006-specific final assets and GUI surfaces are absent. Current visuals are generic/vanilla or borrowed from other surfaces.
- The accepted post-focus formation improvement addendum remains open and only partly implemented; completion should not be claimed until it is closed, promoted, queued with reasons, or rejected with reasons.

## Ordinary Follow-Up

- Balance review for current decision costs, compact integration, border commission cooldowns, and package formation rewards.
- Expand package-level AI strategies beyond local `ai_will_do` blocks.
- Extend event-log/detail copy for future packages once those packages exist.
- Decide whether OGB Event 005-branded visual paths are accepted temporary reuse or require Event 006-specific aliases before the next package expansion.
- Clean up stale wording in `docs/events/006_independence_wave.md` after the next implementation tranche.

## Stale Or Mismatched Docs/Plan Statements

- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md` is still an open accepted addendum. Some items are now implemented or partially implemented, including Border Commission safety, Patron Ledger hardening, regional compact work, railway overlay work, and UGA/SOK package content. The addendum needs disposition updates, but the super-event/audio/achievement/catalog expansion remains substantially unimplemented.
- `docs/events/006_independence_wave.md` correctly states reduced-territory starts, achievements, assets, GUI, and package depth remain future work. Its "future work" phrasing around package-specific formation decisions is partly stale because OGB/ASY/DNZ/UGA/SOK and railway formation decisions now exist.
- Older starter package handoffs that reported missing OGB trigger/idea are superseded by later implementation and the 2026-05-30 country-package audit.
- The achievement prompt expects `cr_*` Event 006 achievements, but current implementation has only older `chaosx_ach_*` achievements from other events/surfaces. Similar names must not be treated as Event 006 completion.

## Validation Performed

- Consulted required offline Paradox wiki core pages: data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focus, achievements, scripted GUI, interface, and graphical assets.
- Consulted relevant vanilla documentation for effects/triggers/script concepts/dynamic variables/modifiers/localisation formatting and script constants.
- Read the required Event 006 source specs, current event doc, and accepted improvement addendum.
- Inspected current Event 006 files under `events/`, `common/decisions`, `common/national_focus`, `common/scripted_effects`, `common/scripted_triggers`, `common/script_constants`, `common/ideas`, `common/ai_strategy`, localisation, achievements, and GFX/interface surfaces.
- Ran brace-balance checks on the main Event 006 script files; all checked files returned balance `0`.
- Searched the checked Event 006 gameplay/localisation files for unsupported `<=`/`>=`; no hits.
- Confirmed `localisation/english/006_independence_wave_l_english.yml` is UTF-8 with BOM and did not show `:0` key format hits in the checked file.
- Counted the focus tree surface: 46 focus blocks, 46 `ai_will_do` blocks, and 46 `completion_reward` blocks.
- Searched achievements, super-event, asset, and Event 006-specific GFX surfaces; missing surfaces are based on negative `rg`/`find` evidence.

## Validation Skipped

- No HOI4 executable load, in-game scenario run, parser log review, or save-game validation was performed.
- No flag or flag-asset validation was performed, per instruction not to touch flags or flag assets.
- No balance simulation was run for release count distribution, host survival after many releases, compact integration, border claims, or package AI.
- No visual inspection of final DDS assets was possible because no Event 006-specific asset pack/manifests were found.

## Recommendation On Improvement Loop Planner

Do not spawn `chaosx_improvement_loop_planner` again for Event 006 yet. The accepted post-focus formation improvement addendum is still unresolved and already covers the depth gap. Close, promote, queue, or reject that addendum's remaining items before requesting another improvement-loop plan for the same event.

## Highest-Impact Next Tranches

1. Reduced-territory resolver tranche: implement shrink/fallback packages and validate host survival beyond skip-only release.
2. Package minimum tranche: add enough historical/local packages to satisfy the source-spec count and continent coverage, then add two true strange packages plus one containment path.
3. Achievements and super-event tranche: implement actual `cr_*` achievements and the first Event 006 super-event/audio/catalog surfaces.
4. Asset/GUI tranche: register and wire Event 006-specific report/news/decision/focus/idea/category/achievement/super-event assets and build the required scripted GUI surfaces or formally revise the source spec.
5. Documentation/disposition tranche: update the open improvement addendum and current docs so implemented, queued, rejected, and promoted items are explicit before any completion claim.
