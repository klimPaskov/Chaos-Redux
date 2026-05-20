# Event 005 Soviet Collapse Validation Report

Audit date: 2026-05-20

## Validation Type

This report records current source inspection and non-Python validation scenarios. It does not claim a live in-game playthrough. The repository instruction says the user verifies live sessions, so this report avoids log requests and records only evidence available in the worktree.

## Commands Run

```text
git diff --check
rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt
rg -n "country_event = \\{ id = chaosx\\.nr5\\.(30|31|32)" common events
rg -n "soviet_collapse_show_(baltic_restoration_pact|caucasus_defense_compact|eastern_buffer_coalition)_super_event" common events interface
rg -n "soviet_collapse_show_(league_equal_republics|steppe_federation)_super_event|GFX_super_event_(league_equal_republics|steppe_federation)|super_event\\.(23|24|25|26|27)\\." common interface localisation events
```

Static checks for the current correction pass passed: no whitespace errors, no forbidden comparison operators in the edited script/trigger files, no local-league formation calls still using `country_event`, no active local-league super-event helper calls, and no remaining Free Republics' League, Steppe Federation, Baltic League, Caucasus League, or Eastern Buffer Coalition super-event localisation/sprite mappings.

## Scenario Matrix

| Scenario | Evidence | Result |
| --- | --- | --- |
| Calm World, strong USSR, event fired manually | `crisis_balance_surface` | Authority 62, Threat 7.25 |
| Calm World, strong USSR, Soviet missions succeed for six months | `mission_success_pressure_surface`, `crisis_monthly_guard_surface` | Success helpers are non-increasing; ordinary months are guarded |
| Calm World, strong USSR, Soviet missions fail for six months | `mission_failure_pressure_surface`, `union_unmade_first_month_guard_surface` | Largest single failure delta is 4.25; a 10-mission maximum-pressure first wave reaches 49.75 and cannot fire Union Unmade during the 31-day lock |
| USSR at war with Germany | war-pressure factors in crisis and MTTH surfaces | Higher pressure requires visible war-state causes |
| USSR at war with Japan | Far Eastern mission and release surfaces | Far Eastern pressure exists without automatic terminal collapse |
| High chaos opening | `crisis_balance_surface` | Higher pressure than calm baseline, still below terminal |
| Totalen Chaos opening | `crisis_balance_surface` | Severe case Threat 50.25, still not first-month terminal by itself |
| One Caucasus republic free | `local_league_surface` plus quorum triggers | League cannot form from one member |
| Two Caucasus republics free | `has_soviet_collapse_caucasus_league_quorum` | League can form under pressure |
| One Central Asian republic free | `local_league_surface` plus quorum triggers | League cannot form from one member |
| Two Central Asian republics free | `has_soviet_collapse_central_asian_league_quorum` | League can form under pressure |
| Union Unmade terminal collapse | `union_unmade_pacing`, `terminal_ordinary_republic_release_surface`, `terminal_mission_cleanup` | First-month guard, release path, and cleanup pass |
| Soviet puppet republics at Union Unmade | terminal release subject path | Soviet subjects are freed with `autonomy_free` before setup |
| New internal republic MTTH release | `mtth_release_surface` | MTTH weights, eight cause events, constants, docs pass |
| Ukraine focus tree full route review | `focus_integrity`, `focus_reward_variety_surface`, `focus_ai_surface` | 81-focus tree passes parser, reward, AI, localisation, and icon checks |
| Belarus focus tree full route review | same focus surfaces | 38-focus tree passes parser, reward, AI, localisation, and icon checks |
| Kazakhstan focus tree full route review | same focus surfaces | 57-focus tree passes parser, reward, AI, localisation, and icon checks |
| Regional republic focus tree review | same focus surfaces | regional/shared/custom trees pass parser, layout, reward, AI, localisation, and icon checks |
| Internal republic focus tree review | `internal_republic_focus_loader`, `internal_republic_focus_tree`, `internal_republic_focus_localisation` | vanilla-supported internal republic tags route to a 62-focus shared tree with northern, Volga-Ural, expanded Crimea, expanded eastern/inner-Asian, tag-specific regional, high-chaos, and common-front branches |

## Latest Correction Validated

The current audit records source-level checks that fail if:

- local league founding triggers do not call explicit quorum triggers, or
- ordinary local league and normal League-route content calls local super-event helpers instead of news events.

The current direct source checks cover these surfaces:

```text
Calm World opening threat is 7.25, and the severe scripted opening scenario is 50.25.
Mission success pressure helpers are net non-increasing; the least stabilizing helper changes threat by -1.50.
Mission failure pressure helpers are bounded; the largest single failure changes threat by 4.25, and the active-cap first wave remains under the Union Unmade high-threat gate.
Union Unmade first-month lock is set for 31 days and the maybe-show helper requires the lock to be absent.
Union Unmade threat-ceiling calls route through the guarded maybe-show helper.
Union Unmade pacing constants require five breakaways, high threat 60, critical authority 25, and contested authority 45.
Kazakhstan is included in terminal ordinary release and subject-freeing lists.
Vanilla-supported internal republic tags are included in terminal release and subject-freeing lists.
Vanilla-supported internal republic tags route to `soviet_collapse_internal_republic_focus_tree` instead of the generic fallback tree.
Terminal ordinary republic release covers release, subject-freeing, breakaway setup, and runtime focus loading paths.
Terminal collapse calls the high-chaos successor spawn helper and anti-Soviet war pass.
Terminal collapse calls local-league and Free Republics' League formation between release/spawn and war entry.
Local league founding triggers require regional quorum triggers instead of one-member readiness checks.
MTTH release checks cover release/miss weights, eight cause events, and cooldown wiring.
Mission objective blocks have timed non-selectable shape, hidden scripted requirements, localized requirement/success/failure text, and distinct success/failure effects.
Terminal mission cleanup removes every Soviet objective mission.
Event 005 focus IDs are unique across republic, custom splinter, and factory successor trees, and all focus IDs have localisation with UTF-8 BOM Event 005 localisation files.
Event 005 focus integrity covers 947 focus blocks with icons, coordinates, completion rewards, AI weights, and resolved focus prerequisite/mutual-exclusion references.
Event 005 focus reward variety covers 650 material reward focuses, 436 shared focus-helper reward focuses, and only 37 idea-only focuses.
Event 005 focus AI checks cover 361 focuses with contextual `ai_will_do` modifiers.
The internal republic tree has 62 focus IDs, 62 completion rewards, 62 AI blocks, no duplicate internal focus IDs, no unresolved internal prerequisites, and current Crimea and eastern/inner-Asian localisation coverage for the newly added settlement, mediation, fortress, compact observer, Yakut, Far Eastern, Buryat, and Tuvan focuses.
The Kronstadt Free Soviet tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate KRS focus IDs, no unresolved KRS prerequisites, and current localisation coverage for campaign planning, port-council diplomacy, permanent arsenal, fortress signal rooms, Gulf battery posts, free-port conferences, and endgame focuses.
The Free Territory of Huliaipole tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate FTH focus IDs, no unresolved FTH prerequisites, and current localisation coverage for campaign planning, anti-capital diplomacy, free rail communes, tachanka front, roaming embassies, and endgame focuses.
The Siberian Zemstvo Authority tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate SZA focus IDs, no unresolved SZA prerequisites, and current localisation coverage for the depth defense, rail diplomacy, Tomsk-Omsk, Irkutsk, Yenisei, and endgame focuses.
The Far Eastern Republic Revival tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate FEV focus IDs, no unresolved FEV prerequisites, and current localisation coverage for port-rail war planning, rail diplomacy, Vladivostok harbor board, Amur buffer posts, Pacific observer missions, and endgame focuses.
The Idel-Ural League tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate IUL focus IDs, no unresolved IUL prerequisites, and current localisation coverage for Volga-line war planning, corridor diplomacy, Kazan-Ufa workshop cordons, Orenburg approach posts, federal congress missions, and endgame focuses.
The Birobidzhan Autonomous Commune tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate BAC focus IDs, no unresolved BAC prerequisites, and current localisation coverage for river-settlement defense planning, relief diplomacy, archive workshops, Amur relief posts, observer relief conferences, and endgame focuses.
The Arctic Naval Directorate tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate ARD focus IDs, no unresolved ARD prerequisites, and current localisation coverage for northern sea denial, convoy recognition, Murmansk dockyard sheds, Kola denial posts, White Sea observer boards, and endgame focuses.
```

## Blockers

The direct source checks cover deterministic script surfaces, not live-session feel or the full final design claim. Live-session behavior remains the final practical check for pacing, league joining, terminal war entry, and whether shared regional trees feel sufficiently distinct in play.
