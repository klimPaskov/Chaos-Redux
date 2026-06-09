# Event006 Wiring Audit and Plan Alignment Handoff

Parent pass: 2026-06-04

Supersession note: later Event006 package/focus work expanded the shared focus
tree to 79 focus blocks. Use
`2026_06_04_090650_event006_catalog_spreadsheet_alignment_handoff.md` and the
current focus file for current count evidence. This handoff remains useful only
for the wiring fixes it recorded at the time.

## Scope

Audited the current Event006 focus, decision, idea, event, scripted helper, localisation, and icon wiring after the report-event call-site tranche. This pass did not touch country flags, country history, country files, or Event005 files.

## Evidence

- Focus coverage at the time of this handoff: `common/national_focus/006_independence_wave_focus.txt` contained the then-current shared focus tree under `independence_wave_liberation_provisional_tree`.
- Localisation coverage at the time of this handoff: all then-current focus IDs had name and `_desc` keys in `localisation/english/006_independence_wave_l_english.yml`.
- Decision/category/idea coverage: 90 Event006 decision-like IDs, 8 decision categories, and 16 ideas have name and `_desc` localisation.
- Event coverage: visible report events `chaosx.nr6.2` through `chaosx.nr6.15` have title, description, and option localisation. `chaosx.nr6.1` is intentionally hidden and has no visible option body.
- Icon coverage: all 65 Event006 script-side `GFX_*` references found in the focus, decision, category, and event files are registered in Event006 interface files.
- Idea picture coverage: all 16 Event006 idea picture keys have matching `GFX_idea_*` registrations.
- Helper coverage: every `independence_wave_* = yes`, `can_independence_wave_* = yes`, `has_independence_wave_* = yes`, and `is_independence_wave_* = yes` call across the Event006 script surface has a matching scripted effect or scripted trigger definition.
- Localisation reference coverage: no missing referenced localisation keys and no duplicate keys were found in `006_independence_wave_l_english.yml`.

## Changes Made

- Updated `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md` so it no longer treats already-wired scripted GUI value panels, report-event call sites, first playable route layers, current achievement definitions, or the shared provisional tree as absent.
- Reframed the remaining blockers around final package depth, package-specific non-flag assets and animation manifests, spreadsheet/catalog/event-detail alignment, and final audit scenarios.

## Remaining Risks

- Event006 is still incomplete. Dormant tags, additional city/protectorate/historical-return/local-polity packages, hidden formables, and deeper strange packages still need verified tags, state groups, leaders or councils, package proof, AI behavior, localisation, package-specific non-flag assets, and validation.
- Current GUI value panels are functional first layers; richer route-state displays and animated presentation should wait for accepted package mechanics and asset handoffs.
- The broad worktree remains dirty and includes unrelated Event005 and Event006 files, so no scoped commit was made in this parent pass.
