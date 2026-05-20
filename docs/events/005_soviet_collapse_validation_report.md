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
rg -n "Steppe Federation super-event|fires the Steppe Federation super-event" localisation/english/005_soviet_collapse_custom_countries_l_english.yml
rg -n "This is the|players who want|generic republic|Taking this focus|[Tt]he tag|tag\\x27s identity|implementation|newly added|reworked|dynamic reward|scales with|scaled reward|focus for" localisation/english/005_soviet_collapse_custom_countries_l_english.yml
rg -n "rather than repeating a generic checklist|generic checklist|is a .* focus for the republic crisis path|objective preparation|scaled reward|Dynamic .* reward|scales with|implementation|newly added|reworked" localisation/english/005_soviet_collapse_focus_expansion_l_english.yml
rg -n "The effect scales|The backlash scales|Cost scales|Scales with|scale with|scales with|generic emergency battalion|required states|border states|nearby states|key states|some divisions|sufficient troops|enough equipment|capital-adjacent states|signal hub states|southern capitals|southern approach states|border routes" localisation/english/005_soviet_collapse_l_english.yml
rg -n "^.*:0 " localisation/english/005_soviet_collapse_l_english.yml
xxd -p -l 3 localisation/english/005_soviet_collapse_l_english.yml
xxd -p -l 3 localisation/english/005_soviet_collapse_focus_expansion_l_english.yml
rg -n "^.*:0 " localisation/english/005_soviet_collapse_focus_expansion_l_english.yml
awk '/focus = \{/ { count++ } END { print "focus_blocks", count }' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt
awk '/id = soviet_collapse_kazakhstan_focus_tree/ { in_tree=1 } /id = soviet_collapse_baltic_focus_tree/ { in_tree=0 } in_tree && /focus = \{/ { focuses++ } in_tree && /completion_reward = \{/ { rewards++ } in_tree && /ai_will_do = \{/ { ai++ } END { print "kazakhstan", focuses, rewards, ai }' common/national_focus/005_soviet_collapse_republics.txt
awk 'NR==FNR { sub(/:.*/, "", $1); loc[$1]=1; next } /id = soviet_collapse_kazakhstan_focus_tree/ { in_tree=1; next } /id = soviet_collapse_baltic_focus_tree/ { in_tree=0 } in_tree && /^\t\tid = / { id=$3; if (!(id in loc) || !((id "_desc") in loc)) print id }' localisation/english/005_soviet_collapse_kaz_focus_l_english.yml common/national_focus/005_soviet_collapse_republics.txt
awk 'NR==FNR { if ($0 ~ /name = "GFX_kaz_soviet_collapse_/) { gsub(/.*name = "/, ""); gsub(/".*/, ""); icons[$0]=1 } next } /id = soviet_collapse_kazakhstan_focus_tree/ { in_tree=1; next } /id = soviet_collapse_baltic_focus_tree/ { in_tree=0 } in_tree && /^\t\ticon = / { if (!($3 in icons)) print $3 }' interface/005_soviet_collapse_kaz_icons.gfx common/national_focus/005_soviet_collapse_republics.txt
```

Static checks for the current correction pass passed: no whitespace errors, no forbidden comparison operators in the edited script/trigger files, no local-league formation calls still using `country_event`, no active local-league super-event helper calls, and no remaining Free Republics' League, Steppe Federation, Baltic League, Caucasus League, or Eastern Buffer Coalition super-event localisation/sprite mappings.
The custom-country tooltip audit also has zero hits for the retired `Steppe Federation super-event` phrasing; the Basmachi, Turkestan, and Alash route pushes now describe the in-world announcement that matches `chaosx.nr5.36`.
The custom-country localisation phrase audit also has zero hits for out-of-world focus text such as `players who want`, `generic republic`, `Taking this focus`, `the tag`, `tag's identity`, implementation-update wording, and visible dynamic-reward wording; the remaining special-arm and radical-route descriptions use in-world institutional language.
The focus-expansion localisation phrase audit also has zero hits for the former generated placeholder sentence, generic-checklist wording, implementation-update wording, and visible `Dynamic reward: scales...` tooltip phrasing; the file keeps the UTF-8 BOM (`efbbbf`) and has no `:0` keys.
The main Soviet Collapse localisation phrase audit also has zero hits for the former mission outcome `scales with` wording, cost `Scales with` wording, generic emergency battalion wording, and vague mission-place phrases such as `required states`, `border states`, `nearby states`, `key states`, `some divisions`, `sufficient troops`, `enough equipment`, `capital-adjacent states`, `signal hub states`, `southern capitals`, `southern approach states`, and `border routes`; the file keeps the UTF-8 BOM (`efbbbf`) and has no `:0` keys.

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
| Belarus focus tree full route review | same focus surfaces | 53-focus tree passes parser, reward, AI, localisation, icon, and route-reference checks |
| Kazakhstan focus tree full route review | same focus surfaces | 92-focus tree passes parser, reward, AI, localisation, icon, and route-reference checks |
| Regional republic focus tree review | same focus surfaces | regional/shared/custom trees pass parser, layout, reward, AI, localisation, and icon checks. The Baltic shared tree includes tag-gated Estonia, Latvia, and Lithuania branch pairs. |
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
Mission outcome, cost, and selected route requirement localisation now describes visible pressure, named corridors, named capitals, and named route chains instead of exposing `scales with` tuning language or anonymous route/state wording.
Terminal mission cleanup removes every Soviet objective mission.
Event 005 focus IDs are unique across republic, custom splinter, and factory successor trees, and all focus IDs have localisation with UTF-8 BOM Event 005 localisation files.
The generated focus-expansion description layer now uses in-world crisis prose for Ukraine, Belarus, Kazakhstan, regional, and fallback breakaway focus descriptions instead of the former placeholder "focus for the republic crisis path" construction.
Event 005 focus integrity covers 1455 focus blocks with icons, coordinates, completion rewards, AI weights, and resolved focus prerequisite/mutual-exclusion references.

The Mountain Republic of the Caucasus custom tree now passes direct source checks for 47 focuses, 47 completion rewards, 47 icon assignments, 47 `ai_will_do` blocks, matching focus name/description localisation, resolved focus references, and unique coordinates.
The Military Factory of Russia tree now passes direct source checks for 58 focuses, 58 completion rewards, 58 icon assignments, 58 `ai_will_do` blocks, matching focus name/description localisation, resolved focus references, and unique coordinates.
The Belarus tree has 53 focus IDs, 53 completion rewards, 53 AI blocks, no unresolved Belarus focus references, no missing Belarus focus localisation, and icon assignments resolved through `interface/005_soviet_collapse_blr_icons.gfx`.
The Kazakhstan tree has 92 focus IDs, 92 completion rewards, 92 AI blocks, no unresolved Kazakhstan focus references, no missing Kazakhstan focus localisation, and icon assignments resolved through `interface/005_soviet_collapse_kaz_icons.gfx`.
The Moldova tree has 48 focus IDs, 48 completion rewards, 48 AI blocks, no unresolved Moldova focus references, no missing Moldova focus localisation, no duplicate Moldova coordinates, and icon assignments resolved through `interface/005_soviet_collapse_regional_icons.gfx`.
Event 005 focus reward variety covers 817 material reward focuses in the conservative direct shell scan, 546 shared focus-helper reward focuses, and 19 focuses in the conservative add-ideas-without-material scan.
Event 005 focus AI checks cover at least 353 focuses with contextual `ai_will_do` modifiers in the conservative direct shell scan.
The internal republic tree has 62 focus IDs, 62 completion rewards, 62 AI blocks, no duplicate internal focus IDs, no unresolved internal prerequisites, and current Crimea and eastern/inner-Asian localisation coverage for the newly added settlement, mediation, fortress, compact observer, Yakut, Far Eastern, Buryat, and Tuvan focuses.
The Kronstadt Free Soviet tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate KRS focus IDs, no unresolved KRS prerequisites, no layout coordinate collisions, and current localisation coverage for sailor assembly registers, Baltic worker letters, free Soviet couriers, Petrograd signal watch, Baltic observer missions, anti-party soviet clauses, free-port liaison rooms, sailor-worker defense councils, free Soviet congresses, dockyard repair crews, icebound supply ledgers, radio-room workshops, convoy escort ledgers, fortress hospitals, naval infantry oaths, Red Fleet signal posts, gulf mine watch, coastal air patrols, port guard schools, Every Harbor a Soviet, and endgame focuses.
The Free Territory of Huliaipole tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate FTH focus IDs, no unresolved FTH prerequisites, no layout coordinate collisions, and current localisation coverage for free-soviet registers, village delegate roads, commune supply ledgers, hidden workshop cells, grain-and-rifle stores, field hospital routes, Ukrainian border letters, Dnieper commune watch, Don steppe contacts, Crimean port whispers, Free Territory Defense Council, commune court registers, tachanka column oaths, black-flag signal posts, steppe airstrips, anti-puppet commune clauses, free school compacts, bread-and-rifle ledgers, foreign mediation, communes without capitals, and endgame focuses.
The Black Banner Host tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate BBH focus IDs, no unresolved BBH prerequisites, no layout coordinate collisions, and current localisation coverage for anti-protectorate letters, temporary free-city pacts, no-hostage committees, Black Banner war councils, mobile court posts, armored-car raids, prison-break networks, roving artillery crews, scorched prison roads, captured rail stores, column supply ledgers, workshop cells, red-and-black depots, field hospital columns, black column registers, railway-state sabotage, borderless column schools, no-masters clauses, foreign-fear mediation, banner without borders, and endgame focuses.
The Basmachi Confederation tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate BSC focus IDs, no unresolved BSC prerequisites, no layout coordinate collisions, and current localisation coverage for recognition by road, caravan officer schools, caravan war planning, oasis mediation, road-and-water guarantees, oasis council registers, road-and-well ledgers, caravan supply hubs, hidden road depots, Central Asian defense council, tribal court registers, raiding column oaths, desert airstrips, anti-puppet caravan clause, water-and-rifle ledger, foreign route mediation, and endgame focuses.
The Turkestan National Council tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate TNC focus IDs, no unresolved TNC prerequisites, no layout coordinate collisions, and current localisation coverage for Tashkent emergency ministries, Samarkand-Bukhara legitimacy, cotton-rail republic, irrigation boards, canal guard posts, oasis supply hubs, southern pass offices, Kyrgyz contact posts, Tajik relief corridors, Turkmen-Caspian letters, the Central Asian Defense Council, station court registers, city militia charter, signal bureaus, council airfields, anti-puppet charter law, school compacts, water-and-bread ledgers, foreign mediation, the New Turkestan Statute, and endgame focuses.
The Alash Restoration Authority tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate ALA focus IDs, no unresolved ALA prerequisites, no layout coordinate collisions, and current localisation coverage for steppe communications, district registers, southern rail, Karaganda letters, Caspian oil survey, resource-town councils, southern republic contacts, pass guards, route bargains, Central Asian League drafting, aul committees, cavalry columns, mobile airstrips, steppe supply hubs, officer oath boards, anti-puppet statutes, the Steppe Republic Charter, and endgame focuses.
The Union Defense Committee tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate UDC focus IDs, no unresolved UDC prerequisites, no layout coordinate collisions, and current localisation coverage for staff recognition channels, emergency staff college, operational war planning, command mediation, loyalist statute guarantees, and endgame focuses.
The Security Directorate Zone tree has 27 focus IDs, 27 completion rewards, 27 AI blocks, no duplicate SDZ focus IDs, no unresolved SDZ prerequisites, no layout coordinate collisions, and current localisation coverage for recognition through custody, internal troop school, archive war planning, custody review, chain-of-custody statutes, and endgame focuses.
The Green Army Congress tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate GAC focus IDs, no unresolved GAC prerequisites, no layout coordinate collisions, and current localisation coverage for village delegate registers, grain passage papers, free republic market days, harvest observer missions, food-for-autonomy clauses, rural congress charters, village federation congresses, rail-siding ambushes, green column oaths, captured artillery caches, forest radio runners, partisan airstrip meadows, no-requisition borders, every-village-a-front routes, hidden mill ledgers, blacksmith carts, forest depot clearings, seed-and-rifle stores, field hospital barns, winter hay roads, harvest truce guarantees, and endgame focuses.
The Don Host Emergency Circle tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate DHC focus IDs, no unresolved DHC prerequisites, no layout coordinate collisions, and current localisation coverage for Novocherkassk field staff, host-court registers, river customs, cavalry yards, convoy escorts, crossing batteries, Rostov workshops, watch posts, rear-area logistics, League passage bargaining, autonomy statutes, river-steppe compact, and Don endurance focuses.
The Kuban Host Provisional Council tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate KHC focus IDs, no unresolved KHC prerequisites, no layout coordinate collisions, and current localisation coverage for Ekaterinodar field staff, crossing-court registers, Kuban river customs, cavalry yards, grain-corridor escorts, mountain crossing batteries, Krasnodar workshops, watch posts, Laba rear-area logistics, League corridor bargaining, autonomy statutes, steppe-mountain compact, and Kuban endurance focuses.
The Siberian Zemstvo Authority tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate SZA focus IDs, no unresolved SZA prerequisites, no layout coordinate collisions, and current localisation coverage for the city-duma records, rail courts, militia charter, workshop contracts, river ports, distant-city League, railhead authority, and endgame focuses.
The Far Eastern Republic Revival tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate FEV focus IDs, no unresolved FEV prerequisites, no layout coordinate collisions, and current localisation coverage for the Khabarovsk assembly, Ussuri rail court, customs ledger, harbor fortress, Nikolsk workshops, Amur river ports, Pacific compact, harbor authority, and endgame focuses.
The Ural Workers Directorate tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate UWD focus IDs, no unresolved UWD prerequisites, no layout coordinate collisions, and current localisation coverage for factory records, machine-tool ledgers, steel quotas, rail-yard repairs, airwatch yards, League arsenal bargaining, shipment-control hardliners, industrial neutrality, and endgame focuses.
The Idel-Ural League tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate IUL focus IDs, no unresolved IUL prerequisites, no layout coordinate collisions, and current localisation coverage for Kazan registers, Ufa field commissars, Volga crossings, Bashkir cavalry roads, oilfield security, League corridor bargaining, the Bolghar question, federal corridor compact, and Volga-Ural endurance focuses.
The Birobidzhan Autonomous Commune tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate BAC focus IDs, no unresolved BAC prerequisites, no layout coordinate collisions, and current localisation coverage for Birobidzhan council records, Amur field staff, court registers, Yiddish school boards, river customs, relief escorts, border batteries, workshop contracts, watch posts, Obluchye rear areas, Far Eastern letters, League relief bargaining, autonomy statutes, Amur commune endurance, and endgame focuses.
The Arctic Naval Directorate tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, no duplicate ARD focus IDs, no unresolved ARD prerequisites, no layout coordinate collisions, and current localisation coverage for Murmansk port records, Kola field staff, convoy court registers, Ice Watch boards, White Sea customs, naval infantry yards, Kola batteries, dockyard contracts, tundra watch posts, winter convoy columns, Kandalaksha rear areas, League convoy bargaining, port neutrality statutes, Arctic port endurance, and endgame focuses.
The Northern Lights Commune tree has 47 focus IDs, 47 completion rewards, 47 AI blocks, 47 icon assignments, no duplicate NLC focus IDs, no unresolved NLC prerequisites, no layout coordinate collisions, and current localisation coverage for Aurora council records, weather-station staff, station courts, greenhouse boards, Ice Watch training, ice-road customs, ration-and-signal escorts, station batteries, heated workshops, tundra watch posts, winter road columns, Apatity rear area, foreign science letters, League weather bargaining, polar neutrality, polar endurance, and endgame focuses.
```

## Blockers

The direct source checks cover deterministic script surfaces, not live-session feel or the full final design claim. Live-session behavior remains the final practical check for pacing, league joining, terminal war entry, and whether shared regional trees feel sufficiently distinct in play.
