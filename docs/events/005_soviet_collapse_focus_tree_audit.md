# Event 005 Soviet Collapse Focus Tree Audit

Audit date: 2026-05-20

## Current Counts

Current parser count across Event 005 focus files:

| File | Tree | Focuses |
| --- | --- | ---: |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_ukraine_focus_tree` | 81 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_belarus_focus_tree` | 38 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_kazakhstan_focus_tree` | 57 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_baltic_focus_tree` | 21 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_caucasus_focus_tree` | 20 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_central_asia_focus_tree` | 14 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_moldova_focus_tree` | 17 |
| `common/national_focus/005_soviet_collapse_republics.txt` | `soviet_collapse_breakaway_focus_tree` | 27 |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | 19 custom successor trees | 20-21 each |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 45 |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 37 |

The verifier counts 755 total focuses across 29 trees.

## Route Coverage

Ukraine covers survival, Rada/democratic, socialist sovereignty, military directory, grain/industry, foreign influence, League leadership, Black Sea ambition, Black Banner, and Bread State route families.

Belarus covers Minsk authority, legal restoration, rail sovereignty, forest defense, socialist autonomy, corridor diplomacy, League logistics, and high-chaos rail/forest routes.

Kazakhstan covers steppe emergency authority, Alash restoration, socialist steppe republic, military district state, resource/rail economy, southern cascade, foreign mediation, Central Asian League, and high-chaos steppe pressure.

Baltic, Caucasus, Central Asian, Moldova, Karelia/fallback, and custom successor trees are implemented as shared or compact path-level trees with local route identities, focus icons, AI, localisation, and rewards.

## Duplicate And Reward Audit

Verifier evidence:

- `focus_integrity`: 755 focuses, zero duplicate IDs, zero missing references, zero self-references, zero nonreciprocal mutual exclusions, zero repeated mutual blocks, zero missing rewards, zero missing icons, zero missing coordinates.
- `focus_reward_variety_surface`: zero duplicate reward groups, zero duplicate reward focuses, nine reward categories, 76 add-idea rewards across 755 focuses.
- `focus_ai_surface`: every focus has `ai_will_do`; mutually exclusive route choices use dynamic AI rather than flat weights.
- `focus_layout_surface`: no duplicate coordinates, no isolated focuses, no shallow dead-end leaves, no edge crossings, and all continuous focus positions are in right-side panels.

## Changes From This Audit Pass

The ordinary local league reward focuses no longer fire super-events:

- `ukr_soviet_collapse_league_of_equals`
- `baltic_soviet_collapse_baltic_defense_compact`
- `caucasus_soviet_collapse_caucasus_defense_compact`
- `kaz_soviet_collapse_steppe_federation_charter`

These focuses still apply league preparation rewards and flags, but local/faction formation presentation remains normal event/report/news flow.

## Remaining Audit Notes

The existing focus-tree implementation passes parser-level and layout-level checks. Live route feel still depends on in-game play, especially compact shared regional trees where several republics share one tree with tag-specific localisation and rewards.
