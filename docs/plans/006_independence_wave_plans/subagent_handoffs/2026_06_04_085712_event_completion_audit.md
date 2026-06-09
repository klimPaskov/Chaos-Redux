# Event006 Independence Wave Current-State Completion Audit

Role: `chaosx_event_completion_auditor`  
Mode: read-only audit; no gameplay, localisation, asset, GFX, spec, spreadsheet, or source implementation files were edited.  
Worktree basis: current filesystem state in `/home/klim/projects/chaos_redux`; older plans are treated as stale when contradicted by current files.

Supersession note: the concrete Canal Register focus-localisation blocker from
this audit was resolved in
`2026_06_04_090019_parent_event006_completion_audit_focus_loc_fix.md`, and the
stale catalog focus-count wording was resolved in
`2026_06_04_090650_event006_catalog_spreadsheet_alignment_handoff.md`. The
broader Event006 completion blockers listed here remain current until separate
implementation and validation handoffs prove otherwise.

## Required References Consulted

- Offline Paradox wiki snapshot before implementation reads: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Country creation, Interface modding, Scripted GUI modding, Graphical asset modding, Sound modding, Achievement modding.
- Vanilla docs under `/home/klim/projects/Hearts of Iron IV/documentation` and system folders: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `common/on_actions/_documentation.md`, `common/decisions/_documentation.md`, `common/scripted_guis/_documentation.md`, `common/ai_strategy/_documentation.md`, `common/script_constants/documentation.md`, `common/characters/_documentation.md`.
- Repo skills used: `chaos-redux-events`, `hoi4-decisions-missions`, `chaos-redux-super-events`, `chaos-redux-event-assets`, `hoi4-focus-trees`.

## Bottom Line

Event006 is not complete. The current implementation is broad and substantially wired, but current evidence shows one concrete focus localisation blocker and the live Event006 documentation still lists completion-blocking future work. The strongest current runtime-facing gap is the missing focus name/description for `independence_wave_canal_register`; the strongest completion blocker is unfinished package/formable/overlay/asset depth explicitly retained in `docs/events/006_independence_wave.md:351-357` against spec completion gates in `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1111-1140`.

## Requirement Status Table

| Requirement | Status | Current evidence |
| --- | --- | --- |
| Entry root remains `chaosx.nr6.1` | Complete | `events/006_independence_wave.txt:1` sets namespace `chaosx.nr6`; `events/006_independence_wave.txt:24-25` defines `id = chaosx.nr6.1`. |
| Minor repeatable registration | Complete | `common/scripted_effects/chaosx_logic_effects.txt:187-188` adds Event 6 to `global.repeatable_events`; `common/on_actions/chaosx_on_actions_system.txt:158-164` selects and fires a random event id; `common/scripted_effects/chaosx_settings_effects.txt:6074-6082` dispatches `chaosx.nr[EVENT_ID].1`. |
| Event name and details integration | Complete | `localisation/english/chaosx_event_names_l_english.yml:7` maps `chaosx.event_name.6`; `docs/events/006_independence_wave.md:113` documents event-log/details wiring; `localisation/english/chaosx_gui_l_english.yml:482` defines the Event006 details body. |
| Release resolver and host-survival rule | Weak evidence | Resolver reserves host survival state and fires releases in `events/006_independence_wave.txt:75-113`; docs describe protected-state and reduced-release behavior in `docs/events/006_independence_wave.md:5-9`. This audit did not run an in-game scenario matrix, and `docs/events/006_independence_wave.md:353` still asks for additional reduced-territory audit scenarios. |
| Event005 separation/origin gating | Complete | `common/scripted_triggers/006_independence_wave_triggers.txt:8-13` requires Event006 origin and excludes Soviet Collapse flags; `common/scripted_effects/006_independence_wave_effects.txt:1260-1268` marks release origin; focus loading is origin-gated at `common/scripted_effects/006_independence_wave_effects.txt:1778-1783`. |
| Country package starter set | Incomplete | Current starter packages are documented at `docs/events/006_independence_wave.md:13-33`, but `docs/events/006_independence_wave.md:351-356` keeps dormant tags, protectorate variants, additional historical-return/local-polity packages, hidden formables, deeper strange packages, deeper overlays, and future formation decisions/missions open. |
| Decisions, missions, categories, and AI | Mostly complete, with future-work gaps | Seven categories exist in `common/decisions/categories/006_independence_wave_categories.txt:8-83`; decision localisation coverage check found 138 decision-like ids and 0 missing names/descs; current fixes resolved the municipal/oil audit items. Future package-specific formation decisions remain open at `docs/events/006_independence_wave.md:356`. |
| Scripted GUI | Weak evidence | Scripted GUI is mounted for major boards per `docs/events/006_independence_wave.md:44`, and files exist under `common/scripted_guis/006_independence_wave_scripted_guis.txt` and `interface/006_independence_wave_scripted_gui.gui`; richer GUI states and animated/category art remain open at `docs/events/006_independence_wave.md:355`. |
| Focus tree | Incomplete | Focus tree exists as `independence_wave_liberation_provisional_tree` at `common/national_focus/006_independence_wave_focus.txt:13-20`, with 79 focus blocks. `common/national_focus/006_independence_wave_focus.txt:1648-1668` defines `independence_wave_canal_register`, but validation found no `independence_wave_canal_register` or `_desc` keys in `localisation/english/006_independence_wave_l_english.yml`. Deeper overlays remain open at `docs/events/006_independence_wave.md:354`. |
| Ideas | Complete for current starter surface | Idea file exists and current icon texture references resolve; current package spirits are wired, e.g. municipal/oil ideas in `common/scripted_effects/006_independence_wave_effects.txt:1470` and `1489`. This does not cover future packages. |
| Report/news events and images | Complete for current visible set | `events/006_independence_wave.txt:137-138` fires report `chaosx.nr6.2` and news `chaosx.news.6` after successful release; report events through `.15` are present at `events/006_independence_wave.txt:144-335`; report/news sprites are registered in `interface/006_independence_wave_report_event_images.gfx:3-55` and `interface/006_independence_wave_news_event_images.gfx:3-7`. |
| Event log/evolutions | Complete for current package list | Release log recording is in `common/scripted_effects/006_independence_wave_effects.txt:3935-3970`; formation/package log helpers cover current packages through `common/scripted_effects/006_independence_wave_effects.txt:3972-4375`; municipal/oil selected details are now routed at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:3996-3998` and `4024-4026`. |
| Super-events/audio | Complete for the seven currently documented core super-events; weak for additional candidates | Seven gate triggers exist at `common/scripted_triggers/006_independence_wave_triggers.txt:900-1077`; seven show effects exist at `common/scripted_effects/006_independence_wave_effects.txt:3439-3499`; seven sprites are registered at `interface/chaosx_super_events.gfx:116-140`; docs list files/audio/gates at `docs/events/006_independence_wave.md:273-347`. Additional formable/scripted-GUI super-event candidates remain only candidates in `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md:511-526`. |
| Achievements | Complete for 19 current Event006 definitions/assets | `docs/systems/custom_achievements.md:38-57` lists 19 Event006 achievements; definitions are in `common/achievements/chaos_redux_achievements.txt:624-924` and `1023-1049`; validation found all 19 have definitions, `_NAME`/`_DESC`/tooltip localisation, and primary/grey/not-eligible sprites. |
| Assets, icons, flags, portraits | Complete for current reusable/vanilla-backed surface; incomplete for future bespoke/animated assets | Texture reference validation checked 147 Event006/super/achievement refs and found 0 missing files. `docs/events/006_independence_wave.md:261-271` keeps future package-specific flags, portraits, animated seals/widgets, and final animation packages open. |
| Catalog/spreadsheet/presentation alignment | Stale doc / incomplete | Catalog handoff says workbook row status remains `In progress` at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_event006_catalog_spreadsheet_handoff.md:55` and `71`. It also says the workbook details mention a `60-focus provisional tree` at line `40`, but current tree validation found 79 focus blocks and `docs/events/006_independence_wave.md:50-59` describes the current tree. |
| Completion claim | Incomplete | Spec says a first working implementation is not enough and lists completion gates at `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md:1111-1140`; current docs list active blockers at `docs/events/006_independence_wave.md:351-357`. |

## Current Real Gaps and Patch Candidates

1. High impact: Add missing focus localisation for `independence_wave_canal_register`.
   - Evidence: focus block at `common/national_focus/006_independence_wave_focus.txt:1648-1668`.
   - Validation: `independence_wave_canal_register False` and `independence_wave_canal_register_desc False` in `localisation/english/006_independence_wave_l_english.yml`.
   - Target: `localisation/english/006_independence_wave_l_english.yml`.

2. High impact: Do not claim Event006 complete until current future-work list is implemented or explicitly descoped by the parent.
   - Evidence: `docs/events/006_independence_wave.md:351-357` keeps package data, reduced-territory audit scenarios, deeper overlays, richer scripted GUI states, future formation decisions/missions, milestone rows, catalog rows, assets, and final validation open.
   - Target files depend on accepted scope: likely `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/decisions/006_independence_wave_decisions.txt`, `common/national_focus/006_independence_wave_focus.txt`, `interface/`, `localisation/english/006_independence_wave_l_english.yml`, `docs/events/006_independence_wave.md`, and catalog/spreadsheet docs.

3. Medium impact: Reconcile stale catalog prose with current focus count.
   - Evidence: catalog handoff says `60-focus provisional tree` at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_event006_catalog_spreadsheet_handoff.md:40`; validation counted 79 focus blocks; Event006 docs describe the current tree at `docs/events/006_independence_wave.md:50-59`.
   - Target: `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and any generated catalog handoff/docs that still quote 60 focuses.

4. Medium impact: Update or extend achievement icon registry prose if the long registry section is expected to enumerate current Event006 sprite aliases.
   - Evidence: `docs/systems/custom_achievements.md:38-57` lists Event006 achievements, and `docs/systems/custom_achievements.md:203-205` points to Event006 icon docs, but the “Registered primary sprite aliases” section starting at `docs/systems/custom_achievements.md:207` still begins with older non-Event006 entries. Runtime assets are present, so this is documentation completeness, not a missing asset.
   - Target: `docs/systems/custom_achievements.md`.

5. Medium/low impact: Future flag/art route should go through asset subagents if the parent adds bespoke country flags, portraits, animated route seals, or animated widgets.
   - Evidence: current docs explicitly leave future package-specific and animated assets open at `docs/events/006_independence_wave.md:261-271`; asset prompt requires `chaos-redux-frame-animation` for animated Independence Wave assets at `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md:342-348`.
   - Target: asset subagent route, then final main-agent `.gfx`/gameplay wiring.

## Stale Older-Audit Claims Versus Current Evidence

- Stale/resolved: The 2026-06-04 decision/mission audit said municipal event-log selected detail bodies omitted municipal formation/package types at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_083702_decision_mission_audit.md:17-26`. Current routing includes municipal formation and package checks at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:3998` and `4026`.
- Stale/resolved: The same audit said `independence_wave_integrate_municipal_authority` used the Free Port duration at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_083702_decision_mission_audit.md:37-40`. Current file defines `@independence_wave_municipal_authority_integration_days = 95` at `common/decisions/006_independence_wave_decisions.txt:25` and uses it at `common/decisions/006_independence_wave_decisions.txt:1488`.
- Stale/resolved: The same audit said non-proclamation package steps exposed raw scripted trigger gates at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_083702_decision_mission_audit.md:42-63`. Current requirement tooltip keys exist for municipal and oil package steps at `localisation/english/006_independence_wave_l_english.yml:529-563`, and decision references use those keys at `common/decisions/006_independence_wave_decisions.txt:1404-1457` and `1618-1671`.
- Stale/resolved: The same audit said generic protectorate AI also enabled for Oil Protectorates at `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_083702_decision_mission_audit.md:67-70`. Current generic protectorate AI excludes `independence_wave_package_oil_protectorate` at `common/ai_strategy/006_independence_wave.txt:465-475`; oil-specific AI exists at `common/ai_strategy/006_independence_wave.txt:538-548`.
- Stale/partially stale: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_event006_catalog_spreadsheet_handoff.md:40` reports workbook text containing a `60-focus provisional tree`; current validation counted 79 focus blocks. The same handoff correctly keeps workbook status `In progress` at lines `55` and `71`.
- Still current: Current Event006 documentation explicitly says queued follow-up items still block completion at `docs/events/006_independence_wave.md:351-357`; do not treat older completion-sounding implementation handoffs as final completion proof.

## Flags and Assets

- No current missing texture files were found among 147 Event006/super-event/achievement references parsed from Event006 `.gfx`, `chaosx_super_events.gfx`, and `chaosx_achievements.gfx`.
- Current package tags use vanilla or existing mod tags. OGB has mod flags in `gfx/flags/`, `gfx/flags/small/`, and `gfx/flags/medium/`. Vanilla direct or ideology-variant flags/history exist for the checked vanilla package carriers (`ASY`, `DNZ`, `UGA`, `SOK`, `BUK`, `KHI`, `BAR`, `DAH`, `MIS`, `ITZ`, `MAY`, `GAR`, `CHR`, `KUR`) in `/home/klim/projects/Hearts of Iron IV/`.
- Several vanilla tags use ideology-variant flags rather than direct `TAG.tga`; this is not current missing-flag evidence. If the main agent decides new bespoke Event006 flags are required, route them to an asset subagent; this audit did not create flags.
- Current future asset blockers are documented, not hidden: `docs/events/006_independence_wave.md:261-271` lists package-specific flag variants, council/portrait packages, animated seals/widgets, route-specific final assets, and final animation packages as future work.

## Validation Commands and Results

- Unsupported comparison-token scan over Event006 files: no matches; command exited 1 because no unsupported operator matches were found.
- Brace-balance Python check over Event006 event/on_action/constants/effects/triggers/decisions/categories/ideas/focus/AI/scripted GUI/localisation/GFX/GUI files: every checked file had equal `{` and `}` counts; examples include `events/006_independence_wave.txt opens=75 closes=75`, `common/scripted_effects/006_independence_wave_effects.txt opens=2014 closes=2014`, `common/decisions/006_independence_wave_decisions.txt opens=1206 closes=1206`.
- BOM check: `localisation/english/006_independence_wave_l_english.yml`, `chaosx_achievements_l_english.yml`, `chaosx_gui_l_english.yml`, and `chaosx_event_names_l_english.yml` all start with UTF-8 BOM.
- `rg -n ":0\\s*\\\"" localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_achievements_l_english.yml localisation/english/chaosx_gui_l_english.yml localisation/english/chaosx_event_names_l_english.yml`: no matches; command exited 1 because no old `:0` localisation style was found in the checked files.
- Focus coverage Python check: `focus_blocks 79`, `focus_ids 80`, `missing_focus_name 1 ['independence_wave_canal_register']`, `missing_focus_desc 1 ['independence_wave_canal_register']`.
- Decision localisation Python check: `decision_like_ids 138`, `missing_decision_name 0`, `missing_decision_desc 0`.
- Achievement coverage Python check over 19 Event006 ids: `missing_or_incomplete []`.
- Texture reference Python check: `checked_texture_refs 147`, `missing_texture_refs 0`.
- Decision/focus icon reference Python check: `decision_icon_refs 18 missing_local_sprites []`; `focus_icon_refs 25 missing_any_gfx []`.
- Current worktree status for sampled Event006 files shows uncommitted/untracked implementation state, e.g. `M events/006_independence_wave.txt`, `M localisation/english/006_independence_wave_l_english.yml`, and untracked `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `docs/events/006_independence_wave.md`, and the required recent handoffs. This audit used filesystem current state, not commit history.

## Completion Judgment

Do not claim Event006 complete. The current implementation has substantial evidence for the entry root, repeatable dispatch, resolver framework, Event005 separation, current decisions/missions/AI, current event-log/details, current achievements, current super-events/audio, and current assets. It remains incomplete because one current focus is missing player-facing localisation and the source/current docs still identify package/formable/overlay/GUI/asset/catalog/final-validation blockers.
