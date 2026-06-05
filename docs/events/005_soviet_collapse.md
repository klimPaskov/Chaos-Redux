# Event 005 Soviet Collapse Clean Overview

This is the compact entry point for the Soviet Collapse implementation state. It merges the scattered Event 005 notes into a small readable set and replaces older audits, package notes, asset sidecars, and subagent handoffs as the current documentation source.

## Current Gameplay Surface

Event 005 is a major Soviet crisis started through `chaosx.nr5.1` and visible event `chaosx.nr5.2`. The implementation spans:

- event chain: `events/005_soviet_collapse.txt`
- crisis constants: `common/script_constants/005_soviet_collapse_constants.txt`
- MTTH values: `common/mtth/005_soviet_collapse_mtth.txt`
- shared logic: `common/scripted_effects/005_soviet_collapse_effects.txt`
- shared gates: `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- decisions and missions: `common/decisions/005_soviet_collapse_decisions.txt`
- focus trees: `common/national_focus/005_soviet_collapse_*.txt`
- localisation: `localisation/english/005_soviet_collapse*.yml`
- country setup: `history/countries/*`
- assets: `gfx/`, `interface/`, `music/`, `sound/`, and `docs/assets/005_soviet_union_collapse/`

The main active systems are:

- a dynamic Union Collapse Threat model
- Moscow Authority, Armed Breakaway Momentum, Command Obedience, Foreign Penetration, League Cohesion, Depot Vulnerability, and Old Movement pressure
- opening breakaway selection
- progressive MTTH republic releases
- Soviet crisis missions and response decisions
- breakaway emergency decisions
- foreign patron decisions and dependency pressure
- local league and Free Republics' League logic
- Union Unmade terminal collapse
- triggerable scenario launch: the Scenarios window can force standalone Soviet Collapse starts without inheriting unrelated live-crisis settings, release ordinary republics or ordinary plus high-chaos splinters by type, form local factions, start the anti-Soviet wars, and grant extra opening forces scaled by intensity, controlled states, civilian factories, and military factories; large and industrial republics receive stronger opening armies through state and factory multipliers
- reconquest resolution: Moscow marks the crisis resolved after regaining control of every state held when the crisis began, which clears the crisis/terminal flags, removes active Soviet missions, hides breakaway and foreign intervention boards, and resets the crisis meters
- runtime focus trees for ordinary republics and fixed focus trees for custom/high-chaos actors
- super-event and report/news presentation surfaces

Progressive general releases are selected from a dynamic `every_possible_country` pool once Gathering Storm or higher chaos is active. Eligible countries must have core territory still owned and controlled by Moscow, core territory already inside the Soviet-collapse breakaway ecosystem, or be Soviet subjects with core territory, so late ordinary breakaways such as northern, Siberian, Arctic, and regional republic tags can join the same release flow as the better-known republics instead of depending on a hardcoded country list. Regional cascade pressure and every chaos tier release additional dynamic follow-on candidates in the same cycle, with each higher tier releasing a larger burst. Terminal collapse uses the same dynamic core rule across repeated release passes, so overlapping-core releasables can be freed from Moscow, Soviet subjects, ordinary breakaways, event-created republics, or high-chaos successors before the anti-Soviet war is formed.

Breakaway setup grants starting forces dynamically. The release package scales field brigades, manpower, infantry equipment, support equipment, and artillery from controlled states, civilian factories, and military factories before applying chaos, war-pressure, depot, foreign-access, and terminal-collapse bonuses. Stronger republics therefore start with substantially larger armies without relying only on a short fixed major-tag list. The triggerable Union Unmade scenario uses the same strength model with higher intensity caps, so high-intensity starts can give Ukraine, Belarus, Kazakhstan, large Siberian republics, and industrial successors far larger opening forces than small isolated tags. Large republics and industrial successors receive especially large field-brigade bursts at high intensity, while small northern or regional tags still get enough guards to survive the first month.

Foreign patron target expansion is compact for players and broad for AI. Human patrons choose one visible republic desk at a time; selecting a target normalizes that target into the breakaway array and marks it as the active patron target so recognition, liaison, armament, adviser, aid-corridor, construction, press, treaty, and client decisions can evaluate it even when the republic was added by a dynamic release path. The selected desk remains available after Union Unmade, and the selected target bypasses ordinary route/cooldown display gates so the player does not open an empty republic panel. AI patrons keep the full target list visible by default.

Selected patron desks must be robust to targeted-decision scope direction. Intervention decisions check both the target scope and `FROM` for the active selected-target flag, so dynamically released republics such as Central Asian breakaways still expose their aid decisions after the player opens their desk.

Focus rewards avoid direct idea stacking as a normal payoff. New focus rewards should prefer variable progression, state work, units, decisions, recognition, depot control, League coordination, or one of the consolidated staged idea helpers rather than adding a fresh visible spirit from each focus. Tiny repeated train, truck, or isolated state-building rewards should be routed through shared rail authority, field-defense, and mobile-column helpers, so the visible result is supply nodes, defended capitals, deployed field columns, depot readiness, command capacity, or route progress rather than clutter. The External Support consolidated idea is reserved for republics that have actually received foreign aid or accepted dependency patronage; self-directed liaison or diplomacy focuses can raise liaison, recognition, resilience, or patronage risk, but they must not mark the republic as externally supported by themselves.

High-chaos/custom splinter military routes are deliberately more dangerous than ordinary republic routes. Their war-plan and hidden-doctrine payoffs create assault and raider templates, spawn equipped formations, core controlled ground, and issue dynamic war goals against the Soviet remnant and non-allied neighbors. This keeps chaos actors expansion-driven instead of defensive focus trees that only collect small stockpile or building rewards.

Country identity rewards should live on existing consolidated spirits where possible. The Pale Railway Authority uses its Railway Guard spirit and railway decisions to build railways, infrastructure, and supply hubs, while the Dead Soldiers' Congress uses its Congress spirit for mass recruitable-population pressure rather than a separate new idea.

Union Unmade terminal collapse gives high-chaos successors the first release pass when they are enabled, then releases ordinary republics from whatever Soviet, subject, breakaway, event-created, or high-chaos-controlled territory remains. This prevents ordinary republic releases from consuming the state ownership needed by special successors. Terminal high-chaos and triggerable chaos collapses also push breakaway neighbors into immediate wars when they are not allied, turning maximum chaos into a multi-front rupture instead of a passive anti-Soviet-only war.

The League branches are wired into the decision system instead of ending as flat reward rows. Early League focus depth unlocks League rifle and motor-column deployment decisions; deeper League focus depth unlocks a generic regional security-zone mandate for regional-faction leaders. The mandate is a targeted decision against eligible neighboring non-collapse countries and costs political power, command power, and fuel before issuing a League-backed war goal. The Ukrainian League branch keeps its bespoke council surface: League focuses open the League Council, arms quotas, grain relief, anti-client protection, `External Border Arbitration`, and `League Security Zone Mandates`. `External Border Arbitration` lets Ukraine spend League arbitration capacity to create a war goal against eligible neighboring non-collapse countries. `League Security Zone Mandates` spends the Black Sea security mission package to create a stronger League-backed war goal against eligible external neighbors that are coastal, major, or regionally industrial. These decisions reuse existing regional decision icons and do not require new sprites.

## Event Log Evolutions

Event 005 registers two event-log evolution families:

- Republic Secession Progression, type `constant:soviet_collapse_event_log.secession_evolution_type`: records first republic declarations, regional cascade, Union Unmade, and terminal republic/splinter rupture milestones.
- High-Chaos Successor Mutation, type `constant:soviet_collapse_high_chaos_event_log.evolution_type`: records the first qualifying high-chaos or extreme successor authority while keeping later high-chaos reports out of the evolution log.

The event-details preview list for event ID `5` is registered in `events_log_rebuild_open_event_details_view`. Player-facing evolution body text must match the Event 005 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` exactly after implementation facts are finalized. The current documentation should not be treated as proof that event-detail and spreadsheet wording are already aligned.

## Legacy Doc Routing

Older Event 005 markdown now redirects into the clean set:

- top-level `docs/events/*005*soviet*.md` and `docs/events/*005*Soviet*.md`
- `docs/plans/005_soviet_union_collapse_plans/**/*.md`
- old `docs/plans/005_soviet_collapse_plans/**/*.md`
- markdown sidecars under `docs/assets/005_soviet_union_collapse/`, `docs/assets/005_soviet_collapse/`, and `docs/assets/005_soviet_collapse_generated_handoff/`
- `docs/super_events/005_soviet_union_collapse_super_event_research.md`

Generated/source/final binary assets and text prompt files remain in place. The removed Markdown bodies should not be used for implementation decisions; update this clean doc set instead.

## Current Priority

Implementation should continue in this order:

1. Release pacing: preserve gradual active-crisis releases. Calm worlds release only the base Soviet republics; higher release pressure and chaos tiers unlock vanilla regional republics; chaos tier and above can unlock custom chaos/special splinters; terminal and maximum-intensity paths can run all-possible release passes.
2. Dynamic release gates: keep extra non-base releases tied to live Union Collapse Threat, release pressure, failed objectives, cascade pressure, war pressure, severe component pressure, urgency, or chaos-tier pressure. Do not reintroduce static one-shot release behavior.
3. Focus quality: continue cleanup around political, industry, and expansion branches; compact layouts; no overlapping lines; fewer pointless mutexes; no idea spam; and visible mechanics such as decisions, war goals, cores, units, templates, factions, and regional interaction rewards.
4. Scenario and decision visibility: keep triggerable scenarios standalone, and fix selected-breakaway intervention visibility dynamically so tags such as Tajikistan do not expose an empty intervention panel. Do not solve this with hardcoded tag lists.
5. Evolution details: update event-detail and evolution-detail wording only after implementation facts are finalized, then mirror the spreadsheet descriptions exactly.
6. Flags and flag assets: no active work. Do not edit flags, route flags, ideology flags, `gfx/flags`, flag GFX, or flag assets unless the parent explicitly reopens that scope.
