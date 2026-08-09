# Event 012 Africa achievement closure audit

Date: 2026-08-09.

## Verdict before closure patches

The registry, trigger, visibility, English localisation, and icon surfaces are complete for all 44 achievements. The icon package contains 132 unique 64x64 DDS files: normal, grey, and not-eligible variants for every row. The canonical acceptance ledger nevertheless classifies all 44 achievement rows as `blocked` because negative outcomes, readiness owners, lifecycle resets, or source acceptance remained incomplete.

Rows 2, 3, 19, 28, 32, 33, and 38 already appeared source-owned in the audited snapshot but had not been promoted in the acceptance ledger. The other rows retained at least one concrete source gap. The user explicitly assigns live in-game validation to himself, so the parent may close a row after its exact source owners, cleanup, invalid path, and MCP/static evidence are present. A generic success/failure proxy is not acceptable.

## Row findings

| Row | Achievement | Pre-patch gap |
| ---: | --- | --- |
| 1 | `africa_guardians_without_borders` | Forced-scenario recorder has no caller; protection-war cleanup evidence is incomplete. |
| 2 | `africa_last_convoy_home` | Source owners appear complete; ledger remains blocked. |
| 3 | `africa_no_empty_promises` | Source owners appear complete; ledger remains blocked. |
| 4 | `africa_the_interveners_left` | No partition-accepted writer; forced-scenario recorder has no caller. |
| 5 | `africa_archive_of_the_living_state` | No archive-destroyed or archive-suppressed writers. |
| 6 | `africa_twelve_empty_chairs_filled` | Generic regional-charter success proxies all-agenda completion; member-loss reset is incomplete. |
| 7 | `africa_the_clause_is_the_country` | No protected-clause-cancelled writer or stable clause/member cleanup. |
| 8 | `africa_exit_without_war` | No exit-war/coup or coerced-return writers. |
| 9 | `africa_no_second_capital` | No rival-leader-annexed or terminal-rival-coercion writers. |
| 10 | `africa_every_region_speaks` | Stale represented/overlap region entries survive later loss. |
| 11 | `africa_confidence_is_contagious` | The 720-day clock is not proven to reset on every relationship/member loss. |
| 12 | `africa_federation_by_consent` | No military-takeover writer. |
| 13 | `africa_republic_of_many_capitals` | No republic-suspension, one-region-centralisation, or military-transition writers. |
| 14 | `africa_crowns_at_one_table` | No counted-court-deposition or monarchy-abolition writers. |
| 15 | `africa_union_of_work_and_land` | No military-takeover, private-concession-restoration, or preventable-famine writers. |
| 16 | `africa_order_without_partition` | No permanent-maximum-emergency, member-genocide, or region-partition writers. |
| 17 | `africa_confederation_that_endured` | No confederal-to-federal-annexation writer; duration reset on sovereign-member loss is incomplete. |
| 18 | `africa_covenant_with_the_impossible` | Nonhuman actor lifecycle lacks exact rampage and terminal-disease negative owners. |
| 19 | `africa_kings_of_the_savanna` | Luba/Lunda/Kuba source owners appear complete; ledger remains blocked. |
| 20 | `africa_nile_has_many_memories` | Nile readiness, corridor-failure, and capital-dispute writers are absent. |
| 21 | `africa_ports_of_the_monsoon` | Monsoon readiness, two-port-loss, and inland-shortcut writers are absent. |
| 22 | `africa_walls_courts_and_caravans` | Horn readiness, corridor-loss, and package-abolition writers are absent. |
| 23 | `africa_the_old_gold_roads` | Gold-roads readiness, Mutapa/Rozwi closure, foreign-majority, and corridor-failure owners are absent. |
| 24 | `africa_member_who_said_no` | Colonial-puppet, League-destruction, and terminal-high-chaos writers are absent. |
| 25 | `africa_return_without_compulsion` | Forced-relocation helper has no caller. |
| 26 | `africa_tools_books_and_ballots` | No military-labour-only writer. |
| 27 | `africa_four_oceans_homeward` | Forced-relocation and forced-scenario helpers have no callers. |
| 28 | `africa_capital_without_capture` | Source owners appear complete; ledger remains blocked. |
| 29 | `africa_rails_rivers_roads_and_ports` | No connected-region-lost writer; stale region proof is not removed. |
| 30 | `africa_ore_leaves_as_machines` | No forced-resource-seizure writer. |
| 31 | `africa_bread_before_banners` | No preventable-famine or maximum civilian ecological-wrath writers. |
| 32 | `africa_development_without_overstretch` | Source owners appear complete; ledger remains blocked. |
| 33 | `africa_common_reserve_answers` | Source owners appear complete; ledger remains blocked. |
| 34 | `africa_no_foreign_boot_remains` | No African-core-cession or unreversed-member-capitulation writers. |
| 35 | `africa_beasts_but_not_caricatures` | Formation-family witnesses and caricature-use/extermination writers are incomplete. |
| 36 | `africa_elephants_crossed_the_desert` | Formation, terrain, supply, and victory helpers have no gameplay callers; all three negative outcomes lack writers. |
| 37 | `africa_the_forest_kept_its_word` | No ecological-covenant readiness or forest-rampage writer. |
| 38 | `africa_rain_on_command` | Source owners appear complete; ledger remains blocked. |
| 39 | `africa_disease_made_and_unmade` | No deliberate-uncontrolled-release, irreversible-outcome, or terminal-disease writers. |
| 40 | `africa_stone_walks_into_parliament` | Stoneborn positive helper has no package owner; rights, human-member-war, and erasure writers are absent. |
| 41 | `africa_another_continent_stood_up` | Sponsored collapse, puppeting, and betrayal writers are absent. |
| 42 | `africa_two_continents_one_name` | Two-continent confidence-collapse and union-civil-war writers are absent. |
| 43 | `africa_war_between_worlds` | Debug-surrender and global-revolt-threshold writers are absent. |
| 44 | `africa_the_world_is_one` | Forced-scenario helper has no caller; terminal source owners otherwise exist behind exact package state. |

## Required owner routing

- Call `africa_achievement_record_forced_scenario` immediately before an actual Event 12 scenario launch, never from an inert selector.
- Extend `africa_achievement_record_action_outcome` only where the resolved action's exact terminal fact proves archive loss, clause cancellation, exit coercion/war, rival coercion, private concession, famine, forced relocation, military-only labour, connected-region loss, forced seizure, or maximum civilian ecological wrath.
- Remove all-agenda achievement meaning from generic `create_regional_charter` success. Call the congress agenda helper only from the actual completed-agenda owner, and reset the retention window on qualifying member loss.
- Write constitutional negative outcomes from the actual route transition/result barriers. Reset confidence/confederation duration windows and regional arrays from real relationship/member/state loss owners.
- Open Nile, Monsoon, Horn, and Gold Roads readiness only after all positive and negative owners required by their trigger exist. Use existing tags, states, and priority packages; do not create a new tag or substitute a coarse state.
- Write Scramble partition, region-partition, African-core-cession, and unreversed-capitulation facts only from their exact settlement/final-peace dispositions.
- Wire elephant helpers to real Event 12 formation creation and bounded movement/supply/protection-war owners. Record formation destruction, supply failure, and use against an unthreatened African state from exact lifecycle outcomes.
- Write disease and high-chaos negative outcomes at deliberate release, irreversible/terminal disease, actor rampage, rights violation, human-member war, erasure, caricature-use, and extermination owners.
- Write world-order negative outcomes at sponsorship default/breakup/puppeting, union confidence collapse/civil war, and continental-war debug surrender/global revolt threshold owners. Preserve candidate-scoped W5 certification.

## MCP evidence

`hoi4.event_inspect` on `chaosx.nr12.1` returned `EVENT_INSPECTED_PARTIAL` with source-linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b66e074e369ce483a30b4b253c2fd6c2cd37a7cc2a729f4ff5a47658905ade4/03dcbb62bc0aa4d8ac25c1170b825ee8e791c247af23ea62b24cca99d71189f6/event-trace-73e269b481e4.json`. The reachability render also returned `EVENT_RENDERED_PARTIAL`. Namespace-wide, bounded file-root, and event-compare attempts timed out after 180 seconds. These limits do not substitute for the exact source-owner audit.

No achievement-specific probability surface exists. Human and AI action resolutions share the same achievement owner hooks.

## Acceptance rule

After the combined owner patches land, rerun the 44-row writer/callsite/cleanup diff. Promote an acceptance-ledger row only when every positive condition, negative condition, duration reset, readiness gate, and referenced helper has an exact runtime writer/caller. Do not use live validation as a completion prerequisite because the user owns it, but do not infer a condition from a generic outcome or package-presence proxy.
