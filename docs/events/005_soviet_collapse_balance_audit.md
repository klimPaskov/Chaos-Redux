# Event 005 Soviet Collapse Balance Audit

Audit date: 2026-05-20

## Threat Model Evidence

Verifier evidence from `crisis_balance_surface`, `crisis_monthly_guard_surface`, `mission_success_pressure_surface`, `mission_failure_pressure_surface`, and `union_unmade_first_month_guard_surface`:

| Scenario | Expected threat behavior | Scripted result after implementation |
| --- | --- | --- |
| Calm World, strong USSR, event fired manually | low opening threat, no first-month runaway | Moscow Authority 62, Union Crisis Threat 7.25 |
| Calm World, strong USSR, first missions succeed | threat falls or stabilizes | 11 success helpers net non-increasing; highest success delta is -1.50 threat |
| Calm World, first missions fail | modest rise, not terminal | largest single failure delta is 4.25; 10 simultaneous max-pressure failures reach 49.75, below the Union Unmade high-threat gate and far below terminal |
| USSR at war with Germany | higher visible war pressure | war pressure contributes through opening and MTTH factors, still behind first-month Union Unmade lock |
| USSR at war with Japan | eastern pressure without instant terminal collapse | Far Eastern missions and MTTH factors exist; no ordinary early terminal path without sustained severe ingredients |
| High chaos opening | higher threat and more weirdness | tier 1 example threat 9.25; higher tiers add controlled pressure bands |
| Totalen Chaos opening | severe but bounded | severe scripted scenario Authority 38, Threat 50.25, below automatic terminal unless compounded |
| One Caucasus republic free | preparation, no league | quorum trigger requires two named Caucasus republics |
| Two Caucasus republics free | league can form under pressure | `has_soviet_collapse_caucasus_league_quorum` contains GEO/ARM, GEO/AZR, ARM/AZR pairs |
| One Central Asian republic free | preparation, no league | quorum trigger requires two southern republics or Kazakhstan after three smaller republics are free |
| Two Central Asian republics free | league can form under pressure | `has_soviet_collapse_central_asian_league_quorum` contains all ordinary two-member pairs |
| Union Unmade terminal collapse | all supported republics release and war begins | terminal release, dynamic force package, and war-entry surfaces pass verifier |
| Soviet puppet republics at Union Unmade | puppets become free | subject paths use `set_autonomy = { autonomy_state = autonomy_free }` before setup |
| New internal republic MTTH release | release follows pressure and region logic | MTTH release surface passes: 8 cause events, release/miss weights, constants, docs |
| Ukraine focus tree full route review | real path content, not filler | 81 focuses, route families present, focus integrity/reward/AI pass |
| Belarus focus tree full route review | rail and forest identity works | 53 focuses, with added military-transit, rail-neutrality, rail-war, forest-command, and League freight branches; focus integrity/reward/AI pass |
| Kazakhstan focus tree full route review | southern and steppe identity works | 92 focuses, with deeper Alash, socialist, resource-sovereignty, mobile-defense, southern cascade, Central Asian League, and multi-vector foreign routes |
| Regional republic focus tree review | non-generic regional content works | shared regional and custom successor trees pass parser, reward, localisation, icon, and AI checks |
| Internal republic focus tree review | internal republics get regional path content | `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN` route to a 62-focus shared tree with tag-specific regional branches, including Crimea's settlement, mediation, fortress, and Black Sea compact route plus Yakut, Far Eastern, Buryat, and Tuvan eastern-survival routes |

## Guards And Dampening

- Union Unmade first-month lock: `soviet_collapse_union_unmade_first_month_lock`.
- Union Unmade regular trigger ingredients: minimum breakaway count 5, high threat 60, critical authority 25, and sustained severe pressure alternatives.
- Threat-ceiling recalculation and progressive-release checks route through `soviet_collapse_maybe_show_union_unmade_super_event`, so they use the same first-month and severe-failure gates instead of calling Union Unmade directly.
- Terminal ordinary release includes Kazakhstan and vanilla-supported internal republic tags: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.
- Event-created internal republic tags use `soviet_collapse_internal_republic_focus_tree` with legal, security, liaison, and tag-specific regional branch content instead of the generic fallback tree.
- Terminal collapse now runs league formation before anti-Soviet war entry. Local leagues auto-form only where two-member regional quorum exists, while Free Republics' League expansion skips countries already committed to a local compact.
- Monthly guard constants cap ordinary successful or moderate months at low deltas.
- Mission success helpers do not raise the main threat total.
- Mission failure helpers are bounded by a verified maximum single-failure delta of 4.25 threat. With the active mission cap at 10, even a full first wave of maximum-pressure failures from the calm baseline reaches 49.75.
- Progressive release MTTH weighs threat, authority, command obedience, depot vulnerability, foreign penetration, League pressure, old movements, failed missions, war state, regional cascades, and chaos tier.

## Local League Correction

This pass corrected local league balance by replacing one-member readiness checks with explicit quorum triggers:

- `has_soviet_collapse_baltic_league_quorum`
- `has_soviet_collapse_caucasus_league_quorum`
- `has_soviet_collapse_central_asian_league_quorum`

Ordinary local league formation no longer emits super-events. Formation still uses normal country events and global announcement flags.

## Exploit Checklist

Detailed evidence is recorded in `docs/events/005_soviet_collapse_exploit_audit.md`.

| Exploit surface | Source-level result | Remaining risk |
| --- | --- | --- |
| Free-unit farming | Unit creation is limited to setup, terminal, MTTH, and costed decision paths; repeatable mobilisation spends command, political, army, manpower, or equipment resources and uses cooldowns. | Live-session unit-count tuning. |
| Equipment farming | Equipment aid and mobilisation are behind cost triggers, visible cost text, and cooldowns; foreign aid adds sponsor influence or patronage risk. | Country-size scaling review. |
| Factory loops | Construction rewards are mostly one-shot focus or setup effects; foreign construction aid spends resources, adds influence, and applies timed patron burden. | Map-state placement review. |
| Influence farming | Target acceptance, protected-republic checks, dominant-sponsor comparisons, balanced sponsorship, and patronage-risk pressure prevent silent sponsor stacking. | Sponsor-by-sponsor final audit. |
| Puppet abuse | Client-cabinet and dependency chains require weak targets, high influence, dominant sponsor checks, and fail against protected republics. | Live diplomacy edge cases. |
| War-goal, claim, and core spam | Source scan finds no `create_wargoal`; war entry is terminal-scripted, claims are one-shot focus rewards, and cores are release/setup effects. | Live diplomatic edge cases. |
| Mission pressure farming | Active mission cap is 10; success helpers are non-increasing for main threat and failure deltas stay below terminal bypass levels. | In-game category density review. |
| Release farming | Progressive releases use global cooldown and terminal-state gates; Union Unmade uses first-month lock, severe-condition gates, and terminal cleanup. | Final family-by-family MTTH audit. |

## Non-Python Validation Commands

```text
rg -n "soviet_collapse_total_collapse_threat|soviet_collapse_monthly_successful_objectives|soviet_collapse_monthly_failed_objectives|soviet_collapse_union_unmade_first_month_lock|soviet_collapse_maybe_show_union_unmade_super_event" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt
rg -n '<''=|>''=' common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt
rg -n "python3[ ].tools/verify_event005_completion_gate.py" docs/events/005_soviet_collapse_balance_audit.md
```

Current checkout validation is based on the listed static source surfaces and scenario evidence above. The Python completion gate is deliberately not used as proof for this audit.
