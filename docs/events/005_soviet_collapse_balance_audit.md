# Event 005 Soviet Collapse Balance Audit

Audit date: 2026-05-20

## Threat Model Evidence

Verifier evidence from `crisis_balance_surface`, `crisis_monthly_guard_surface`, and `mission_success_pressure_surface`:

| Scenario | Expected threat behavior | Scripted result after implementation |
| --- | --- | --- |
| Calm World, strong USSR, event fired manually | low opening threat, no first-month runaway | Moscow Authority 62, Union Crisis Threat 7.25 |
| Calm World, strong USSR, first missions succeed | threat falls or stabilizes | 11 success helpers net non-increasing; highest success delta is -1.50 threat |
| Calm World, first missions fail | modest rise, not terminal | ordinary failure max delta 2.75; estimated 26.45 ordinary failed months to reach 80 |
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
| Belarus focus tree full route review | rail and forest identity works | 38 focuses, route families present, focus integrity/reward/AI pass |
| Kazakhstan focus tree full route review | southern and steppe identity works | 57 focuses, southern cascade and Central Asian League route present |
| Regional republic focus tree review | non-generic regional content works | shared regional and custom successor trees pass parser, reward, localisation, icon, and AI checks |

## Guards And Dampening

- Union Unmade first-month lock: `soviet_collapse_union_unmade_first_month_lock`.
- Union Unmade regular trigger ingredients: minimum breakaway count 5, high threat 60, critical authority 25, and sustained severe pressure alternatives.
- Threat-ceiling recalculation and progressive-release checks route through `soviet_collapse_maybe_show_union_unmade_super_event`, so they use the same first-month and severe-failure gates instead of calling Union Unmade directly.
- Terminal ordinary release includes Kazakhstan and vanilla-supported internal republic tags: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.
- Terminal collapse now runs league formation before anti-Soviet war entry. Local leagues auto-form only where two-member regional quorum exists, while Free Republics' League expansion skips countries already committed to a local compact.
- Monthly guard constants cap ordinary successful or moderate months at low deltas.
- Mission success helpers do not raise the main threat total.
- Progressive release MTTH weighs threat, authority, command obedience, depot vulnerability, foreign penetration, League pressure, old movements, failed missions, war state, regional cascades, and chaos tier.

## Local League Correction

This pass corrected local league balance by replacing one-member readiness checks with explicit quorum triggers:

- `has_soviet_collapse_baltic_league_quorum`
- `has_soviet_collapse_caucasus_league_quorum`
- `has_soviet_collapse_central_asian_league_quorum`

Ordinary local league formation no longer emits super-events. Formation still uses normal country events and global announcement flags.

## Validation Command

```text
python3 .tools/verify_event005_completion_gate.py --allow-missing-continuation-spec
```

Current checkout result: exit 0. Static checks also found no whitespace errors and no forbidden `<=`/`>=` operators in `common/scripted_effects/005_soviet_collapse_effects.txt`.
