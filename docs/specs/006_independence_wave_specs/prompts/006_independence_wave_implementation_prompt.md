# 006 Independence Wave Implementation Prompt

This file gives the implementation agent a single source prompt for building Event 6 from the canonical spec files.

## Implementation prompt

Implement Event 6, Independence Wave, as a Minor Repeatable Liberations event.

Use these source files as acceptance criteria:

- `006_independence_wave_overview.md`
- `006_independence_wave_mechanics.md`
- `006_independence_wave_decisions_missions_gui.md`
- `006_independence_wave_focus_trees.md`
- `006_independence_wave_country_packages.md`
- `006_independence_wave_formables.md`
- `006_independence_wave_super_events_assets_achievements.md`
- `006_independence_wave_research_notes.md`

Build the event as an instant release wave with the automatic count ladder 3, 4, 5, 7, and 10. Keep manual release-all scenario behavior separate. Hosts must never be fully deleted. Prefer to keep host capitals. If a release, formable, or scenario transfer would violate host survival, shrink, delay, convert to claims, or choose another target.

Event 6 origin must remain separate from Soviet Collapse and every other release system. A reused tag receives Event 6 mechanics only when Event 6 created it or explicitly marked it as participating. New Event 6 country tags, formable tags, cosmetic tags, and route split tags must end with `X`.

Create real content for released countries. Do not spawn empty tags. Each Event 6 country needs origin memory, state setup, politics, leader setup, starting forces, economy assumptions, ideas, decision categories, focus overlay or additive crisis package, AI behavior, reinforcement path, and cleanup. Ordinary small releases use the shared Independence Wave overlay with regional inserts. Selected stronger releases use ambition inserts, formable access, and deeper asset needs.

Implement the living mechanics from the mechanics file. Values should use the documented 0 to 100 bands and be visible through decision headers, scripted localisation, idea tooltips, focus tooltips, and the scripted GUI ledger when built. Include Legitimacy, Recognition, Foreign Support, Patron Influence, Sponsor Rivalry, Coalition Trust, Border Heat, Post-Release Instability, Local Control, Former Host Anger, Host Exhaustion, Reclamation Capacity, Negotiation Willingness, League Cohesion, League Authority, and Aggressive Bloc Pressure where applicable.

Implement decisions and missions as concrete actions. Avoid political power stores and passive reward trays. Use costs and requirements such as equipment, manpower, XP, convoys, trains, fuel, supply, held states, local control, legitimacy, foreign access, stability, war support, tied-down divisions, sponsor debt, and time pressure. Include success, partial success, failure, cooldowns, AI use, cleanup, and clutter control.

Implement the scripted GUI only as a readable management surface. It must not bypass decision costs or mechanics. It should show current actor mode, values, key targets, current missions, route status, league or compact status, host pressure, and scenario state when relevant.

Implement the shared focus overlay with survival, political, administration, economy, army, recognition, patron, host dispute, league, aggressive, regional, and ambition lanes. Focuses should unlock or modify decisions, missions, mechanics, leaders, ideas, claims, cores, units, buildings, diplomacy, and formable routes. Avoid filler rewards. Wire idea lifecycles.

Implement country packages through a registry. Reuse vanilla or Chaos Redux tags only when safe. Create X-ending tags for new Event 6 countries and formables. Use readable public country names. Do not use office, board, compact, or committee names as country names.

Implement the formable web with reveal conditions, state-control groups, integration requirements, focus and decision hooks, former host safeguards, league outcomes, compact outcomes, AI behavior, and cleanup. Cores should require integration. Claims should not become free conquest loops.

Implement super-events only for global thresholds, such as a meaningful Independence League, federal league proclamation, coercive compact, great partition shock, major hidden restoration, host counterstroke, or release-all scenario crisis. Do not create a super-event for every wave. Research final quotes, remarks, images, and audio before wiring. Keep final localisation direction-aware and do not paste working labels.

Produce required assets through the proper asset workflow. Historical flags, historical symbols, real leader portraits, and real regalia must be sourced and documented. Fictional, symbolic, alternate-history, and high-chaos assets can be generated. Process assets into final game-ready formats and document them. Achievement icons need completed, grey, and not-eligible variants.

Implement achievements with tracking flags or variables, unlock triggers, disqualifiers, localisation, icons, docs, and route or scenario hooks. Do not convert hard achievements into automatic unlocks.

Update event log, event details, evolutions, docs, and spreadsheet only after player-facing wording exists. Keep direction-only spec labels out of localisation.

Run meaningful validation:

- automatic wave counts 3, 4, 5, 7, 10
- host survival and capital retention
- Event 6 origin separation from Soviet Collapse
- X-ending rule for new Event 6 tags
- release target validity and cleanup
- mechanics visible and changing through actions
- decisions and missions with costs, outcomes, AI, cooldowns, and cleanup
- focus overlay loading and route locks
- country packages with forces, leaders, politics, economy, and reinforcement
- formables with state groups, integration, host safeguards, and cleanup
- league and compact thresholds
- super-event triggers and settings-aware playback
- asset references and source-mode compliance
- achievement disqualifiers and tracking
- release-all scenario variants

Report any simplification, blocker, missing asset, missing repository precedent, or unimplemented accepted requirement honestly.

## Compact `/goal` prompt

```text
/goal Implement Event 6, Independence Wave, from docs/specs/006_independence_wave_specs. It is a Minor Repeatable Liberations event that instantly releases countries in waves of 3, 4, 5, 7, and 10. Preserve host survival and preferably host capitals. Keep Event 6 origin separate from Soviet Collapse and other release systems. Reused tags only get Event 6 content if Event 6 created or marked them. New Event 6 country, formable, cosmetic, and route split tags must end with X.

Released countries must not be empty tags. Give them origin memory, politics, leaders, starting forces, economy, ideas, shared Independence Wave focus overlay, regional inserts, decisions, missions, mechanics, AI, reinforcement, and cleanup. Implement visible values for legitimacy, recognition, foreign support, patron influence, sponsor rivalry, coalition trust, border heat, instability, local control, host anger, host exhaustion, host reclamation readiness, negotiation willingness, league cohesion, league authority, and aggressive bloc pressure where applicable.

Build decision and mission categories for releases, hosts, sponsors, league, compact, formables, and release-all scenario variants. Use concrete costs such as equipment, manpower, XP, convoys, trains, fuel, supply, local control, legitimacy, stability, war support, tied-down divisions, sponsor debt, and time. Include success, partial success, failure, cooldowns, AI use, cleanup, clutter control, and exploit prevention. GUI is a readable ledger, not a bypass.

Build the focus overlay with survival, politics, administration, economy, army, recognition, patron, host dispute, league, aggressive, regional, and ambition lanes. Wire focuses to mechanics, decisions, missions, ideas, units, leaders, claims, cores, buildings, diplomacy, formables, and AI. Use varied rewards and idea lifecycles.

Build country packages through a registry. Reuse existing tags only if safe. Create X-ending tags when new. Use readable map names. Historical flags, symbols, real leaders, and real regalia require sourced assets. Fictional or high-chaos assets may be generated.

Build regional and hidden formables with reveal logic, state groups, integration, focus and decision hooks, host safeguards, league and compact outcomes, AI, cleanup, and no free core spam. Super-events only for major league, federal league, coercive compact, great partition shock, major hidden restoration, host counterstroke, or scenario crises. Add achievements with tracking, disqualifiers, icons, docs, and route hooks. Validate wave counts, host survival, origin separation, tag rules, mechanics, decisions, focus loading, country packages, formables, assets, achievements, scenario variants, and cleanup. Report blockers and simplifications honestly.
```

## Final acceptance criteria

Event 6 is implementation-complete only when all of these are true:

1. The random event can fire as Minor Repeatable and follows the 3, 4, 5, 7, 10 automatic ladder.
2. Manual release-all scenario variants work separately from automatic waves.
3. Every host survives Event 6 transfers and capital retention is preferred.
4. Event 6 origin is tracked and separates overlapping tags from Soviet Collapse content.
5. New Event 6 custom tags, formable tags, cosmetic tags, and route split tags end with `X`.
6. Release target selection blocks dead tags, invalid countries, unsafe capitals, missing packages, and host deletion.
7. Released countries have real content, not empty tags.
8. Shared focus overlay and regional inserts load correctly.
9. Strong candidates receive ambition inserts without requiring unique content for every possible release.
10. Mechanics are visible and values change through decisions, missions, focuses, events, wars, state control, AI actions, and foreign influence.
11. Decisions and missions use meaningful costs, outcomes, AI, cooldowns, clutter control, and cleanup.
12. Scripted GUI surfaces show values and actions without bypassing mechanics.
13. Former hosts receive response tools, settlement paths, reclamation logic, exhaustion, and safeguards.
14. Sponsors can support releases while creating patron influence and rivalry risks.
15. Independence League and coercive compact systems have thresholds, decisions, missions, AI, super-event hooks, and failure states.
16. Formables have origin checks, state groups, integration missions, reveal logic, host safeguards, post-formation play, and cleanup.
17. Super-events fire only for documented major thresholds and have researched quote, text, image, and audio packages before final wiring.
18. Assets exist or are clearly marked blocked, with correct source mode and final game-ready paths.
19. Achievements have tracking, disqualifiers, icons, localisation, docs, and route hooks.
20. Event logs, Event Details, evolutions, docs, and spreadsheet fields align with final in-game wording.
21. AI behavior exists for releases, hosts, sponsors, league, compact, formables, scenario variants, and route choices.
22. Cleanup handles annexation, tag switch, invalid targets, origin conflicts, dead hosts, closed routes, obsolete missions, and stale variables.
23. Exploit checks block free cores, host deletion, tag farming, puppet bypass, war-goal spam, free-unit loops, and sponsor abuse.
24. Validation covers all major surfaces and any missing or simplified requirement is reported.
