# Event 006 Completion Audit Continuation - Read-only Handoff

## Current Status Note

Historical read-only audit. Its KUB/ALT route evidence is superseded by the 2026-06-05 user correction and by `docs/plans/006_independence_wave_plans/source_of_truth_map.md`. Do not use this audit as proof that Kuban (`KUB`) or Altai (`ALT`) are current Event 006 package scope. Event006 still requires a final completion audit before any completion claim.

Date: 2026-06-04  
Role: `chaosx_event_completion_auditor`  
Scope: read-only audit of current Event 006 Independence Wave implementation against the listed specs/plans and user corrections.  
Status: incomplete. This handoff is not a completion claim.

## Reference Baseline

Required offline references were consulted before auditing Chaos Redux files:

- Paradox wiki snapshot pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Additional wiki pages for touched systems: Interface modding, Scripted GUI modding, National focus modding, Country creation, Cosmetic tag modding, Achievement modding, State modding.
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`.

Audited source specs/plans:

- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_research_notes.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_subagent_deployment_plan.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md`

## Proven Implemented Areas

### Event entry, immediate release, and host survival shell

- Entry event `chaosx.nr6.1` exists, is hidden, and is triggered-only in `events/006_independence_wave.txt:23`.
- The entry event prepares release count, seeds candidate pools, and releases countries in the same immediate chain after candidate and host-safety checks. Evidence: `events/006_independence_wave.txt:30`, `events/006_independence_wave.txt:75`, `events/006_independence_wave.txt:80`, `events/006_independence_wave.txt:94`.
- After release, the candidate is set up, cores are restored, release is registered, Congress is opened if ready, and report/news events are fired. Evidence: `events/006_independence_wave.txt:99`, `events/006_independence_wave.txt:100`, `events/006_independence_wave.txt:130`, `events/006_independence_wave.txt:136`.
- Host survival is implemented through reserved survival-state selection and reduced-footprint release masking. The survival state prefers the capital when the capital is host-owned and not a candidate core. Evidence: `common/scripted_effects/006_independence_wave_effects.txt:74`, `common/scripted_effects/006_independence_wave_effects.txt:79`, `common/scripted_effects/006_independence_wave_effects.txt:84`, `common/scripted_effects/006_independence_wave_effects.txt:140`.
- Host-safety trigger requires controlled state count above the floor, at least one candidate-cored non-capital state, and at least one host-owned state not cored by the candidate. Evidence: `common/scripted_triggers/006_independence_wave_triggers.txt:852`, `common/scripted_triggers/006_independence_wave_triggers.txt:855`, `common/scripted_triggers/006_independence_wave_triggers.txt:864`, `common/scripted_triggers/006_independence_wave_triggers.txt:869`.

### Release count scaling

- Release count constants match the requested baseline/evolution scale: baseline 3-5, Evo I 4-6, Evo II 5-7, Evo III 6-9, Evo IV 8-12, Evo V 10-16. Evidence: `common/script_constants/006_independence_wave_constants.txt:14`, `common/script_constants/006_independence_wave_constants.txt:17`, `common/script_constants/006_independence_wave_constants.txt:20`, `common/script_constants/006_independence_wave_constants.txt:23`, `common/script_constants/006_independence_wave_constants.txt:26`, `common/script_constants/006_independence_wave_constants.txt:29`.
- `independence_wave_prepare_release_count` applies those constants by `chaos_tier`, randomizes the target, and clears per-wave arrays/display variables. Evidence: `common/scripted_effects/006_independence_wave_effects.txt:15`, `common/scripted_effects/006_independence_wave_effects.txt:20`, `common/scripted_effects/006_independence_wave_effects.txt:44`, `common/scripted_effects/006_independence_wave_effects.txt:50`, `common/scripted_effects/006_independence_wave_effects.txt:70`.

### Event 006 origin, focus tree, decisions, and AI surfaces

- Event 006 has a dedicated origin trigger and origin setup flag/variable. Evidence: `common/scripted_triggers/006_independence_wave_triggers.txt:10`, `common/scripted_effects/006_independence_wave_effects.txt:2047`, `common/scripted_effects/006_independence_wave_effects.txt:2054`.
- The focus loader loads only `independence_wave_liberation_provisional_tree`. Evidence: `common/scripted_effects/006_independence_wave_effects.txt:2867`, `common/scripted_effects/006_independence_wave_effects.txt:2873`.
- The Event 006 focus tree exists with 125 `focus = {` blocks. Each counted focus has `completion_reward` and `ai_will_do` based on command counts. The tree includes opening, route, crisis, anti-patron, railway, formation, historical-return, local-polity, and strange branches. Evidence starts at `common/national_focus/006_independence_wave_focus.txt:14`, with representative focus IDs at `common/national_focus/006_independence_wave_focus.txt:28`, `common/national_focus/006_independence_wave_focus.txt:219`, `common/national_focus/006_independence_wave_focus.txt:244`, `common/national_focus/006_independence_wave_focus.txt:879`, `common/national_focus/006_independence_wave_focus.txt:1031`.
- Decision categories and action surfaces exist for host aftermath, committee survival, New States Congress, Patron Ledger, patronage recognition, Formation Ledger, Border Commission, and sealed dossiers. Representative evidence: `common/decisions/006_independence_wave_decisions.txt:67`, `common/decisions/006_independence_wave_decisions.txt:288`, `common/decisions/006_independence_wave_decisions.txt:377`, `common/decisions/006_independence_wave_decisions.txt:534`, `common/decisions/006_independence_wave_decisions.txt:689`, `common/decisions/006_independence_wave_decisions.txt:944`.
- Decisions use constants for costs and include AI weights broadly. Command count found 148 `ai_will_do` blocks in `common/decisions/006_independence_wave_decisions.txt`.
- Formation Ledger has numerous package route decisions with costs, requirement tooltips, trigger checks, effects, and AI weights. Representative evidence: Volga at `common/decisions/006_independence_wave_decisions.txt:997`, Assyria at `common/decisions/006_independence_wave_decisions.txt:1065`, Free Port at `common/decisions/006_independence_wave_decisions.txt:1250`, Canal at `common/decisions/006_independence_wave_decisions.txt:1357`, Municipal at `common/decisions/006_independence_wave_decisions.txt:1464`, Protectorate at `common/decisions/006_independence_wave_decisions.txt:1571`, Oil Protectorate at `common/decisions/006_independence_wave_decisions.txt:1678`, Buganda at `common/decisions/006_independence_wave_decisions.txt:1777`, Sokoto at `common/decisions/006_independence_wave_decisions.txt:1876`, Bukhara at `common/decisions/006_independence_wave_decisions.txt:1975`, Khiva at `common/decisions/006_independence_wave_decisions.txt:2074`, Mesopotamia at `common/decisions/006_independence_wave_decisions.txt:2173`, Don at `common/decisions/006_independence_wave_decisions.txt:2272`, Kuban at `common/decisions/006_independence_wave_decisions.txt:2371`, Altai at `common/decisions/006_independence_wave_decisions.txt:2470`.
- Event 006 has a dedicated AI strategy file present: `common/ai_strategy/006_independence_wave.txt`.

### Static scripted GUI value panels

- Scripted GUI entries exist for Dossier Board, Congress, Patron Ledger, Formation Ledger, and Border Commission. Evidence: `common/scripted_guis/006_independence_wave_scripted_guis.txt:2`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:13`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:25`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:36`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:48`.
- GUI layout containers exist with icons and value text boxes. Evidence: `interface/006_independence_wave_scripted_gui.gui:2`, `interface/006_independence_wave_scripted_gui.gui:35`, `interface/006_independence_wave_scripted_gui.gui:68`, `interface/006_independence_wave_scripted_gui.gui:101`, `interface/006_independence_wave_scripted_gui.gui:134`.

### Super-events, achievements, assets, and country tags

- Seven Event 006 super-event packages are present as static image/audio packages under `gfx/super_events/`, `music/`, `sound/`, and `docs/assets/006_independence_wave/super_events/`: First League, Human Renunciation, League War, First Old Name, Great Partition Week, First Impossible State, and Rump That Endures.
- Super-event effect callsites/gates exist for those packages. Evidence: `common/scripted_effects/006_independence_wave_effects.txt:5268`, `common/scripted_effects/006_independence_wave_effects.txt:5277`, `common/scripted_effects/006_independence_wave_effects.txt:5286`, `common/scripted_effects/006_independence_wave_effects.txt:5296`, `common/scripted_effects/006_independence_wave_effects.txt:5306`, `common/scripted_effects/006_independence_wave_effects.txt:5315`, `common/scripted_effects/006_independence_wave_effects.txt:5324`.
- Nineteen Event 006 achievements are implemented in `common/achievements/chaos_redux_achievements.txt`, with matching localisation and achievement sprites. Representative definition evidence: `common/achievements/chaos_redux_achievements.txt:624`, `common/achievements/chaos_redux_achievements.txt:637`, `common/achievements/chaos_redux_achievements.txt:709`, `common/achievements/chaos_redux_achievements.txt:788`, `common/achievements/chaos_redux_achievements.txt:873`, `common/achievements/chaos_redux_achievements.txt:890`, `common/achievements/chaos_redux_achievements.txt:907`, `common/achievements/chaos_redux_achievements.txt:1023`, `common/achievements/chaos_redux_achievements.txt:1040`. Localisation evidence starts at `localisation/english/chaosx_achievements_l_english.yml:239`. Sprite evidence starts at `interface/chaosx_achievements.gfx:806`.
- Package carrier tags checked against mod and vanilla country tags. Vanilla has ASY, DNZ, UGA, SOK, BUK, KHI, IRQ, DON, KUB, ALT, BAR, DAH, GHA, NMB, KUR, PAL, BOT, ERI, MIS, MAY, CHR, ITZ, GAR. Mod adds OGB, DFR, ZUL in `common/country_tags/chaosx_countries.txt:9`, `common/country_tags/chaosx_countries.txt:41`, `common/country_tags/chaosx_countries.txt:42`.

## Incomplete or Missing Areas

### 1. Event 005/Soviet Collapse exclusion is not proven in gameplay candidate gates

The docs claim candidate gates reject Soviet Collapse origin, breakaway, event-created republic, and high-chaos successor flags. Evidence: `docs/events/006_independence_wave.md:9`, `docs/events/006_independence_wave.md:157`.

However, targeted search of Event 006 gameplay files found Soviet Collapse flag checks only in Event 006 achievements, not in candidate entry, host safety, decisions, focus, or event release code. The candidate gate `can_independence_wave_use_candidate_tag` starts at `common/scripted_triggers/006_independence_wave_triggers.txt:44` and checks tag/package availability, but no Event 005 origin flags in the searched block. Candidate pool gates start at `common/scripted_triggers/006_independence_wave_triggers.txt:774` and similarly do not show Event 005 exclusion. The only direct Event 006 gameplay anti-repeat host check found is `NOT = { has_country_flag = chaosx_release_origin_independence_wave }` at `common/scripted_triggers/006_independence_wave_triggers.txt:856`.

This is a high-priority suspected gap because the user correction explicitly requires no Event 6 releases to enter or be sourced from Event 5/Soviet Collapse systems.

### 2. Scripted GUI is display-only, not the specified interactive button surface

The requested surfaces include Dossier Board, New States Congress, Patron Ledger, and Formation Ledger where useful, with every button having costs/tooltips/AI equivalent/cleanup/helpers.

Current scripted GUI entries all set `ai_enabled = { always = no }` and contain only visibility/window bindings. Evidence: `common/scripted_guis/006_independence_wave_scripted_guis.txt:6`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:17`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:29`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:40`, `common/scripted_guis/006_independence_wave_scripted_guis.txt:52`.

The GUI layout contains icons and value text boxes, not clickable scripted GUI buttons. Evidence: `interface/006_independence_wave_scripted_gui.gui:7`, `interface/006_independence_wave_scripted_gui.gui:15`, `interface/006_independence_wave_scripted_gui.gui:24`, repeated through `interface/006_independence_wave_scripted_gui.gui:156`.

Gameplay actions are implemented as decisions with costs and AI weights, which is useful, but the current scripted GUI does not satisfy the stronger "every button" requirement.

### 3. Major route-state animations are not implemented

The asset/spec requirement says major route-state animations require real frames, frame sheet, DDS, static fallback, manifest, and `.gfx` handoff.

No Event 006 `frameAnimatedSpriteType` or Event 006 animation frame-sheet wiring was found. The only `frameAnimatedSpriteType` hits are unrelated interface/tech files. Current Event 006 docs explicitly say final animated assets still need real source frames, frame sheets, DDS output, static fallbacks, manifest entries, and `.gfx` handoffs. Evidence: `docs/events/006_independence_wave.md:308`, `docs/events/006_independence_wave.md:312`, `docs/events/006_independence_wave.md:316`, `docs/events/006_independence_wave.md:400`.

This is a hard completion blocker under the user correction.

### 4. Candidate pool priority may not match "early waves prioritize ordinary releasables"

The event seeds candidate pools in this order: strange, historical/local polity, city/railway/protectorate/game-rule/dormant, then ordinary. Evidence: `events/006_independence_wave.txt:34`, `events/006_independence_wave.txt:42`, `events/006_independence_wave.txt:53`, `events/006_independence_wave.txt:67`.

Some special pools are gated by higher `chaos_tier`, so baseline waves likely remain ordinary-only. But dormant can enter at `chaos_tier` value 1 before ordinary (`common/scripted_triggers/006_independence_wave_triggers.txt:782`), city/railway at tier 2 (`common/scripted_triggers/006_independence_wave_triggers.txt:800`, `common/scripted_triggers/006_independence_wave_triggers.txt:816`), historical/local at tier 4, and strange at tier 5. This means once special pools unlock, the resolver prioritizes them before ordinary rather than trying ordinary first and escalating. That may violate the stated prioritization model.

### 5. Package/formable coverage is broad but still documented as incomplete

The implementation has many package formation decisions and carrier tags, but `docs/events/006_independence_wave.md` still records queued package work:

- Remaining package data for dormant tags, border protectorate variants, additional historical-return packages, additional local-polity packages, hidden formables, deeper strange packages, Mapuche, Idel-Ural, and PRA separation. Evidence: `docs/events/006_independence_wave.md:397`.
- Future audit scenarios and additional package state maps for reduced-territory starts. Evidence: `docs/events/006_independence_wave.md:398`.
- Deeper package overlays and package-specific variants beyond current family finishers. Evidence: `docs/events/006_independence_wave.md:399`.
- Future package formation decisions and post-formation integration missions beyond the verified starter set. Evidence: `docs/events/006_independence_wave.md:401`.

Under the no-fallback/no-shallow-package requirement, this cannot be called complete. Current generic route families may be acceptable as designed families, but they are not enough to close the full spec as written.

### 6. Country/flag asset coverage has at least one visible gap

Custom Event 006 tags OGB, DFR, and ZUL exist. OGB and ZUL have base and ideology flag variants in base/medium/small folders. DFR currently has only `DFR.tga` in base/medium/small, with no ideology-specific DFR variants found by file search.

If DFR is intended to use a neutral/base flag for all ideologies, this should be documented as intentional. If ideology variants are required by the asset spec for package country flags, DFR is incomplete.

### 7. Event 006 documentation has stale internal counts and open completion notes

The focus tree count command found 125 focuses and 125 focus `ai_will_do` blocks. The Event 006 doc still says the tree references 25 focus sprites across 121 focuses. Evidence: `docs/events/006_independence_wave.md:165`.

The same doc has open future-work completion blockers at `docs/events/006_independence_wave.md:394` through `docs/events/006_independence_wave.md:402`. These should be reconciled with actual implementation state before a final parent completion claim.

## Suspected Errors and Risks

1. Event 5 exclusion is likely weaker than the docs say. Event 006 uses its own origin flag and focus tree, but I did not find candidate/host gates that reject Soviet Collapse-origin or Soviet Collapse breakaway/high-chaos successor countries. This is the biggest correctness risk against the user's non-negotiables.
2. Current scripted GUI surfaces are not interactive scripted GUI systems. They are value panels backed by decisions. If the parent intends decisions to be the only action layer, the spec must be amended; otherwise the GUI work is incomplete.
3. The high-chaos pool order could overweight special packages once they unlock, rather than ordinary-first release waves with later escalation.
4. The implementation has many generic/family package routes while the user explicitly forbids generic packages/fallbacks. Each family route needs a design decision: either prove it is a bespoke intended package family, or replace it with package-specific content.
5. `cr_volga_without_collapse` from the achievement prompt appears to have been implemented as `cr_not_the_collapse`. The implemented achievement matches the idea and has localisation/assets, but the ID rename should be cross-checked against catalog/spec expectations.
6. I did not run live game validation, syntax parser validation, or asset rendering validation. This report is a static audit.

## Validation Commands Run

Representative commands run during this audit:

```bash
rg --files paradox_wiki | rg 'Data structures|Triggers|Effect|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|Interface modding|Scripted GUI|National focus|Country creation|Cosmetic tag|Achievement|State modding'
rg --files '/home/klim/projects/Hearts of Iron IV/documentation'
wc -l docs/specs/006_independence_wave_specs/*.md docs/plans/006_independence_wave_plans/006_independence_wave_subagent_deployment_plan.md docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md
sha256sum docs/specs/006_independence_wave_specs/*.md docs/plans/006_independence_wave_plans/006_independence_wave_subagent_deployment_plan.md docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md
wc -l events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/script_constants/006_independence_wave_constants.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt common/scripted_guis/006_independence_wave_scripted_guis.txt interface/006_independence_wave_scripted_gui.gui
rg -n 'load_focus_tree|005|soviet|SOV|soviet_collapse|chaosx_release_origin_soviet|release_origin' events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/national_focus/006_independence_wave_focus.txt common/decisions/006_independence_wave_decisions.txt docs/events/006_independence_wave.md
rg -n 'soviet_collapse|chaosx_release_origin_soviet_collapse|event_created_republic|high_chaos_successor|breakaway' common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt events/006_independence_wave.txt
rg -n 'super_event_independence_wave|independence_wave_show_|great_partition|first_old_name|first_impossible|rump_that_endures|league_war|human_renunciation' common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt events/006_independence_wave.txt interface/*.gfx localisation/english/*.yml docs/events/006_independence_wave.md
rg -n 'frameAnimatedSpriteType|animation|frame sheet|static fallback|animated' docs/events/006_independence_wave.md interface common docs/assets/006_independence_wave -g '*.txt' -g '*.gfx' -g '*.gui' -g '*.md'
rg -n '^(ASY|DNZ|UGA|SOK|BUK|KHI|IRQ|DON|KUB|ALT|BAR|DAH|MIS|ITZ|MAY|GAR|CHR|KUR|KBK|NMB|BOT|PAL|GHA|ERI|DFR|ZUL|OGB)\\s*=' common/country_tags '/home/klim/projects/Hearts of Iron IV/common/country_tags' -g '*.txt'
printf 'focus_count='; rg -c '^\\s*focus = \\{' common/national_focus/006_independence_wave_focus.txt
printf 'focus_ai_will_do_count='; rg -c '^\\s*ai_will_do = \\{' common/national_focus/006_independence_wave_focus.txt
printf 'focus_completion_reward_count='; rg -c '^\\s*completion_reward = \\{' common/national_focus/006_independence_wave_focus.txt
printf 'decision_ai_will_do_count='; rg -c '^\\s*ai_will_do = \\{' common/decisions/006_independence_wave_decisions.txt
rg -n '<=|>=' events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt common/scripted_guis/006_independence_wave_scripted_guis.txt
find gfx/super_events music sound docs/assets/006_independence_wave/super_events -maxdepth 4 \( -iname '*independence_wave*' -o -iname 'manifest.md' \) | sort
find docs/assets/006_independence_wave gfx interface -maxdepth 5 \( -iname '*anim*' -o -iname '*frame*' -o -iname '*sheet*' \) | sort
git status --short
```

Notable command results:

- No `<=` or `>=` operators found in the searched Event 006 script files.
- Focus count: 125.
- Focus `ai_will_do` count: 125.
- Focus `completion_reward` count: 125.
- Decision `ai_will_do` count: 148.
- Event 006 static super-event image/audio packages were present for all seven listed super-events.
- Event 006 animation/frame-sheet search found contact sheets and unrelated interface animations, but no Event 006 route-state frame animation wiring.
- Worktree was already dirty with many Event 005/Event 006 changes before this handoff; this subagent did not edit gameplay files.

## Prioritized Next Implementation Tasks

1. Add explicit Event 005/Soviet Collapse exclusion to Event 006 candidate/host gates, then re-audit `can_independence_wave_use_candidate_tag`, pool gates, package seed gates, and any formation/focus eligibility that could admit Event 005-origin tags. Confirm OGB and other overlapping carriers cannot enter Soviet Collapse trees/formables from Event 006 origin.
2. Decide whether the action layer is decision-only or true scripted GUI. If true scripted GUI is still required, convert the value panels into real scripted GUI button surfaces with costs/tooltips/effects/AI equivalents/cleanup helpers. If decisions remain the action layer, update specs to remove the button requirement.
3. Implement major route-state animation assets using the frame-animation workflow: real source frames, contact sheet, frame sheet DDS, static fallback DDS, manifest, `frameAnimatedSpriteType`/`.gfx` handoff, and GUI/category wiring.
4. Reconcile ordinary-first release priority with the current pool order. If the spec means ordinary first at every tier, seed ordinary candidates before special pools or add weighted/dynamic ordering that proves ordinary precedence while still allowing higher-chaos unlocks.
5. Close package/formable completion gaps listed in `docs/events/006_independence_wave.md:397` through `docs/events/006_independence_wave.md:401`, especially dormant tags, border protectorate variants, hidden formables, Mapuche/Idel-Ural/PRA blockers, package-specific post-formation missions, and deeper strange packages.
6. Audit DFR flag policy and any other package country asset gaps. Either add ideology variants where required or document intentional base-flag reuse in the Event 006 asset manifest/spec.
7. Reconcile docs/catalog with implementation facts: 125 focuses, current achievement IDs, current package list, current open blockers, and animation/GUI status.
8. After implementation changes, run focused follow-up audits: Event 006 decision/mission auditor, focus tree auditor, country package auditor, localisation auditor, and asset/frame-animation audit. Do not make a final completion claim until these blockers are closed.
