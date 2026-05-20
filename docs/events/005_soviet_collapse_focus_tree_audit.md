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
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 20 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 34 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 17 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_internal_republic_focus_tree` | 20 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 27 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 19 custom successor trees | 20-21 each |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 45 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 37 |

The current shell recount counts 810 total focuses across 30 trees.

## Route Coverage

Ukraine covers survival, Rada/democratic, socialist sovereignty, military directory, grain/industry, foreign influence, League leadership, Black Sea ambition, Black Banner, and Bread State route families.

Belarus covers Minsk authority, legal restoration, rail sovereignty, forest defense, socialist autonomy, corridor diplomacy, League logistics, and high-chaos rail/forest routes.

Kazakhstan covers steppe emergency authority, Alash restoration, socialist steppe republic, military district state, resource/rail economy, southern cascade, foreign mediation, Central Asian League, and high-chaos steppe pressure.

Baltic, Caucasus, Moldova, internal republic, fallback, and custom successor trees are implemented as shared or compact path-level trees with local route identities, focus icons, AI, localisation, and rewards. The Baltic shared tree is now a 36-focus path-level tree with legal continuity, archive protection, border government, Baltic League, port/customs sovereignty, coastal and forest defense, foreign-protector, and recognition settlement routes. The Central Asian shared tree has been expanded from its compact placeholder into a 34-focus path-level tree with local council, military border authority, foreign patronage, Turkestan federation, cotton/water logistics, Basmachi pressure, Khwarazm high-chaos, and southern pact/federation routes.

The internal republic tree covers the vanilla-supported internal Union Unmade tags `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`. It gives them a 20-focus shared route set with legal, security, and liaison choices plus regional branches for northern forest republics, Volga-Ural republics, Crimea, and Siberian/Far Eastern/inner Asian republics.

## Duplicate And Reward Audit

Current non-Python evidence:

- Event 005 focus recount: 810 focuses across the Event 005 focus files after the Baltic expansion.
- Baltic tree recount: 36 focuses, 36 completion rewards, and 36 `ai_will_do` blocks.
- Baltic focus references resolve to focus IDs defined inside the same tree.
- Baltic focus IDs have matching name and description localisation.
- Baltic icon assignments resolve through the existing regional icon GFX files.
- Central Asian tree recount: 34 focuses, 34 completion rewards, and 34 `ai_will_do` blocks.
- Central Asian focus references resolve to focus IDs defined inside the same tree.
- Central Asian focus IDs have matching name and description localisation.
- Central Asian icon assignments resolve through the existing regional icon GFX files.

## Changes From This Audit Pass

The ordinary local league reward focuses no longer fire super-events:

- `ukr_soviet_collapse_league_of_equals`
- `baltic_soviet_collapse_baltic_defense_compact`
- `caucasus_soviet_collapse_caucasus_defense_compact`
- `kaz_soviet_collapse_steppe_federation_charter`

These focuses still apply league preparation rewards and flags, but local/faction formation presentation remains normal event/report/news flow.

The vanilla-supported internal republics no longer use only the generic fallback tree. Event-created internal republic tags route to `soviet_collapse_internal_republic_focus_tree`, with localisation and verifier coverage for the loader, focus IDs, and focus text.

## Remaining Audit Notes

The existing focus-tree implementation passes parser-level and layout-level checks. Live route feel still depends on in-game play, especially compact shared regional trees where several republics share one tree with tag-specific localisation and rewards.
