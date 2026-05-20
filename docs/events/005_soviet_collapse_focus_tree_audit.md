# Event 005 Soviet Collapse Focus Tree Audit

Audit date: 2026-05-20

## Current Counts

Current parser count across Event 005 focus files:

| File | Tree | Focuses |
| --- | --- | ---: |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 81 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 38 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 57 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 36 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 40 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 45 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 23 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 50 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 36 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 19 custom successor trees | 20-27 each |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 45 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 37 |

The current shell recount counts 892 total focuses across 30 trees.

## Route Coverage

Ukraine covers survival, Rada/democratic, socialist sovereignty, military directory, grain/industry, foreign influence, League leadership, Black Sea ambition, Black Banner, and Bread State route families.

Belarus covers Minsk authority, legal restoration, rail sovereignty, forest defense, socialist autonomy, corridor diplomacy, League logistics, and high-chaos rail/forest routes.

Kazakhstan covers steppe emergency authority, Alash restoration, socialist steppe republic, military district state, resource/rail economy, southern cascade, foreign mediation, Central Asian League, and high-chaos steppe pressure.

Baltic, Caucasus, Moldova, internal republic, fallback, and custom successor trees are implemented as shared or compact path-level trees with local route identities, focus icons, AI, localisation, and rewards. The Baltic shared tree is a 36-focus path-level tree with legal continuity, archive protection, border government, Baltic League, port/customs sovereignty, coastal and forest defense, foreign-protector, and recognition settlement routes. The Caucasus shared tree is a 40-focus path-level tree with mountain federal, national restoration, oil directorate, pass defense, Georgian Tbilisi/Black Sea observer route, Armenian Yerevan relief and border-fortress route, Azerbaijani Baku oilfield and Caspian oil diplomacy route, sponsor-consulate, border treaty, compact, and high-chaos crown routes. The Central Asian shared tree has been expanded from its compact placeholder into a 45-focus path-level tree with local council, military border authority, Uzbek Tashkent emergency ministries, Samarkand-Bukhara legitimacy, cotton-rail republic, Turkestan city congress, Tajik Dushanbe/Pamir mountain sovereignty, Kyrgyz Bishkek/Tian Shan pass authority, foreign patronage, Turkmen Ashgabat/desert/Caspian authority, Turkestan federation, cotton/water logistics, Basmachi pressure, Khwarazm high-chaos, and southern pact/federation routes. The Moldova tree is a 23-focus path-level tree with Chisinau legitimacy, Dniester defense, Romanian alignment and union-debate routes, Ukrainian grain-road logistics, river-state consolidation, and the Eastern Buffer Coalition news-event hook. The fallback breakaway tree is now a 36-focus modular emergency tree with legal records, local court and militia rolls, depot repair, home industry, engineer rosters, border militia, many-patron ledgers, League observer access, and road-and-rail repair routes on top of the existing political, military, foreign-liaison, League, and high-chaos lanes. The internal republic tree is now a 50-focus tree with tag-specific Karelian border, deeper Komi Syktyvkar/Pechora/mine-and-timber/exile-camp/northern-accord content, Bashkir Ufa/oilfield/mobile-defense/Volga-Ural compact content, Tatar Idel-Ural, Crimean peninsula-statute, Far Eastern port, Yakut resource, Buryat Baikal, and Tuvan steppe branches. The Mountain Republic of the Caucasus custom tree is now a 27-focus tree with dedicated pass-closure, elder-council, lowland-depot raid, Caucasus negotiation, village-autonomy, and anti-border-troop branches on top of the high-chaos successor core.

The internal republic tree covers the vanilla-supported internal Union Unmade tags `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`. It gives them a 50-focus shared route set with legal, security, and liaison choices plus deeper tag-specific northern forest, Komi, Volga-Ural, Bashkir, Crimea, Siberian/Far Eastern, inner Asian, high-chaos old-name, and common-front branches.

## Duplicate And Reward Audit

Current non-Python evidence:

- Event 005 focus recount: 892 focuses across the Event 005 focus files after the Bashkir internal-route expansion.
- Baltic tree recount: 36 focuses, 36 completion rewards, and 36 `ai_will_do` blocks.
- Baltic focus references resolve to focus IDs defined inside the same tree.
- Baltic focus IDs have matching name and description localisation.
- Baltic icon assignments resolve through the existing regional icon GFX files.
- Caucasus tree recount: 40 focuses, 40 completion rewards, and 40 `ai_will_do` blocks.
- Caucasus focus references resolve to focus IDs defined inside the same tree.
- Caucasus focus IDs have matching name and description localisation.
- Caucasus icon assignments resolve through the existing regional icon GFX files.
- Central Asian tree recount: 45 focuses, 45 completion rewards, and 45 `ai_will_do` blocks.
- Central Asian focus references resolve to focus IDs defined inside the same tree.
- Central Asian focus IDs have matching name and description localisation.
- Central Asian icon assignments resolve through the existing regional icon GFX files.
- Moldova tree recount: 23 focuses, 23 completion rewards, and 23 `ai_will_do` blocks.
- Moldova focus references resolve to focus IDs defined inside the same tree.
- Moldova focus IDs have matching name and description localisation.
- Moldova icon assignments resolve through the existing regional icon GFX files.
- Moldova route gates no longer require mutually exclusive routes at the same time; the river guard and river-state finishers use the existing OR-style prerequisite block pattern.
- Internal republic tree recount: 50 focuses, 50 completion rewards, and 50 `ai_will_do` blocks.
- Internal republic focus references resolve to focus IDs defined inside the same tree.
- Internal republic focus IDs have matching name and description localisation.
- Internal republic icon assignments resolve through existing Event 005 focus icon GFX files.
- Fallback breakaway tree recount: 36 focuses, 36 completion rewards, and 36 `ai_will_do` blocks.
- Fallback breakaway route locks no longer force the stabilization and armed-neutrality finishers through mutually incompatible political, foreign, League, military, and high-chaos routes at the same time.
- Fallback breakaway focus IDs have matching name and description localisation, using existing Event 005 focus sprites.
- Mountain Republic tree recount: 27 focuses, 27 completion rewards, 27 icon assignments, and 27 `ai_will_do` blocks.
- Mountain Republic focus IDs have matching name and description localisation, using existing MRC focus sprites and previously wired MRC decision/focus asset files.

## Changes From This Audit Pass

The ordinary local league reward focuses no longer fire super-events:

- `ukr_soviet_collapse_league_of_equals`
- `baltic_soviet_collapse_baltic_defense_compact`
- `caucasus_soviet_collapse_caucasus_defense_compact`
- `kaz_soviet_collapse_steppe_federation_charter`

These focuses still apply league preparation rewards and flags, but local/faction formation presentation remains normal event/report/news flow.

The vanilla-supported internal republics no longer use only the generic fallback tree. Event-created internal republic tags route to `soviet_collapse_internal_republic_focus_tree`, with localisation and verifier coverage for the loader, focus IDs, and focus text.

The Central Asian shared tree now gives Uzbekistan its own route after the shared local council and cotton setup. `UZB` can build Tashkent emergency ministries, join Samarkand and Bukhara legitimacy work to the written-republic route, turn cotton and rail into material state capacity, and finish with a Turkestan city congress that prepares League leadership without replacing the other southern republics.

The Caucasus shared tree now has tag-gated country routes for each core republic. `GEO` can build Tbilisi's Black Sea authority and register observer desks, `ARM` can organize Yerevan relief networks and Ararat border fortresses, and `AZR` can secure Baku oilfields before turning Caspian oil access into diplomacy under local command.

The internal republic tree now gives `KOM` a deeper route after the shared forest branch. Komi can consolidate Syktyvkar's emergency council, keep Pechora rail survival open, convert mine and timber contracts into guarded industrial capacity, reckon with exile-camp authority, and finish with a Northern Republic Accord tied to League contact.

The internal republic tree also gives `BSK` a deeper route after the shared Volga-Ural branch. Bashkiria can consolidate Ufa's emergency authority, secure oilfields, build a mobile Ural defense, and enter a Volga-Ural Compact with League and neighboring-republic contact.

## Remaining Audit Notes

The existing focus-tree implementation passes parser-level and layout-level checks. Live route feel still depends on in-game play, especially compact shared regional trees where several republics share one tree with tag-specific localisation and rewards.
