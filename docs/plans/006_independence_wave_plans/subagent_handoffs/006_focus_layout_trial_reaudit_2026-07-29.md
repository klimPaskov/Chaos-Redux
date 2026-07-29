# Event 006 professional-defense layout trial re-audit

Status: retain provisionally; layout remains **HOLD**. This is a coordinate-only visual improvement, not a clean focus-tree validation, because the MCP result still contains 14 blocking diagnostics.

## Scope and changed source

The only gameplay file in the trial is `common/national_focus/006_independence_wave_focus.txt`. The diff changes only `x` and `y` fields for the professional-defense cluster:

| Focus ID | Baseline | Trial |
| --- | --- | --- |
| `independence_wave_adopt_military_archetype_program` | x=38, y=6 | x=36, y=7 |
| `independence_wave_confirm_civilian_control` | x=33, y=7 | x=31, y=8 |
| `independence_wave_grant_military_autonomy` | x=35, y=7 | x=33, y=8 |
| `independence_wave_raise_mass_reserve` | x=37, y=8 | x=35, y=8 |
| `independence_wave_build_professional_core` | x=39, y=8 | x=37, y=8 |
| `independence_wave_fund_domestic_arsenals` | x=41, y=9 | x=39, y=8 |
| `independence_wave_accept_foreign_arms` | x=43, y=9 | x=41, y=8 |
| `independence_wave_adopt_border_defense` | x=33, y=10 | x=43, y=8 |
| `independence_wave_adopt_reclamation_doctrine` | x=35, y=10 | x=45, y=8 |
| `independence_wave_standardize_with_league` | x=37, y=11 | x=47, y=8 |
| `independence_wave_preserve_independent_command` | x=39, y=11 | x=49, y=8 |
| `independence_wave_found_professional_defense_institution` | x=38, y=12 | x=40, y=9 |

No IDs, prerequisites, mutual exclusions, route locks, rewards, icons, localisation, AI, decisions, missions, ideas, advisors, leaders, flags, claims, cores, war goals, events, or formable hooks changed.

## MCP metrics

| Metric | Restored baseline (`a7bd7fe6...`) | Current trial (`58cc490c...`) | Delta |
| --- | ---: | ---: | ---: |
| Focuses / connectors | 184 / 223 | 184 / 223 | 0 / 0 |
| Connector crossings | 49 | 45 | -4 |
| Node intersections | 18 | 7 | -11 |
| Long connectors | 27 | 28 | +1 |
| Diagnostics | 143 | 125 | -18 |
| Blocking diagnostics | 14 | 14 | 0 |
| Bounds | x=1..101, y=0..19 | x=1..101, y=0..19 | unchanged |

The trial layout hash is `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`; the restored baseline hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`. Validation remains false because the same 14-blocker set is unresolved.

## Visual and route assessment

The baseline staggers the five mutually-exclusive pairs across y=7..11 and routes a dense fan into the y=12 capstone. The trial places the five pairs adjacently on y=8 at x=31/33, 35/37, 39/41, 43/45, and 47/49, with the archetype root at x=36/y=7 and the capstone at x=40/y=9. The paired red exclusion links are now visually grouped, and the professional-cluster through-node findings disappear; the remaining seven through-node warnings are on the pre-existing founding-to-regional path.

The crossing and node-intersection reductions are therefore a real visual improvement. The one added long connector and higher total Manhattan span are acceptable for this provisional layout because the tree bounds are unchanged and no route semantics were traded away. Keep the trial as a layout HOLD, not as completion evidence.

Route coverage is unchanged for state construction, economy/administration, army/security, diplomacy/recognition, package settlements, independence network, formable, signature, and high-chaos branches. No content is missing or simplified; only the four previously coupled geometry clusters remain unresolved: opening oath/economy, founding fan/economy, founding fan/depot, and the remaining professional-defense crossings.

## Artifact evidence

Parent MCP render artifacts for the current trial:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14a0e2f70f466c6de94ee908efd0e4ef42b03bd55b4ff1e26c55dd548b37753c/313a6ea7059a8b11ebc49d1d5fa335ab9011c15d37f98a403e0163bb02423f7a/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2feed19716a2aa8011645b7c55f38f75b13a2cd5c1520e276c0d59fb9ea1848/b66bb7805fb7fd4581b38acc996b3cd8237a412a1de5a6263a2d6dbe3c23d6e8/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b208934082ce3e3579bac351a6a978e29f6261ceef4dbb577131c71414f9cb8f/0a70300c96a980cd6c4a011b88d6bd8b9901b4a3bea32a99d3958b276a33b919/independence_wave_focus_tree.focus.json`

Local read-only importer/layout/lint/render reproduction matched the trial hash and aggregate metrics. The subagent MCP endpoint itself remained unavailable during this turn, so the parent-produced MCP artifacts above are the current revision evidence.

## Recommendation and remaining risk

Retain the uncommitted coordinate trial provisionally. Do not claim layout completion while the 14 blockers remain. Any next change must preserve this cluster's five pair groupings and re-run inspect/render against the full tree; reject candidates that reduce one local crossing while increasing crossings, node intersections, long connectors, or route ambiguity elsewhere.

No files were changed by this re-audit. The parent-owned trial file remains the only source diff; this handoff is documentation-only and intentionally uncommitted.
