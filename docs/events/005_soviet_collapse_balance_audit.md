# Event 005 Soviet Collapse Balance Audit

Audit date: 2026-05-23

## Threat Model Evidence

Verifier evidence from `crisis_balance_surface`, `crisis_monthly_guard_surface`, `mission_success_pressure_surface`, `mission_failure_pressure_surface`, and `union_unmade_first_month_guard_surface`:

| Scenario | Expected threat behavior | Scripted result after implementation |
| --- | --- | --- |
| Calm World, strong USSR, event fired manually | low opening threat, no first-month runaway | Moscow Authority 62, Command Obedience 56, Union Crisis Threat 7.25 before first-wave setup; a normal three-republic opening remains about 10.25 before posture selection. |
| Calm World, strong USSR, first missions succeed | threat falls or stabilizes | 11 success helpers net non-increasing; highest success delta is -1.50 threat |
| Calm World, first missions fail | modest rise, not terminal | Strong-center dynamic caps hold early Republic Momentum, Foreign Penetration, depot, League, and old-movement components below runaway ranges; calm failed-month deltas are capped at 8 while the center is still strong and below five breakaways. Component month-over-month growth caps also prevent separate mission, focus, and foreign-action writes from rebuilding a runaway total before the next monthly guard tick. |
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
- Dynamic component caps now run inside `soviet_collapse_recalculate_total_threat`. In calm strong-center conditions with no war, fewer than five breakaways, and chaos below Rising Chaos, Republic Momentum is capped at 38, depot vulnerability at 38, Foreign Penetration at 22, League Cohesion at 24, and old-movement pressure at 18. That keeps repeated early pressure writes below the calm ceiling while Moscow Authority and Command Obedience remain strong.
- Contested-center caps remain looser: while Moscow Authority is at least 45, fewer than five breakaways exist, and chaos is below Totalen Chaos, the same components can rise into severe ranges but not instantly hard-cap at 100. Once authority breaks, war pressure escalates, high chaos arrives, or the breakaway count reaches the Union Unmade ingredient gate, the caps no longer suppress terminal collapse.
- Component growth caps now also run inside total-threat recalculation. In calm strong-center months, Republic Momentum and depot vulnerability can rise at most 5 points from their last monthly checkpoint, Foreign Penetration at most 3, League Cohesion at most 4, and old-movement pressure at most 3. In moderate non-terminal months, those caps loosen to 10/9/7/8/6 for Republic Momentum, depot vulnerability, Foreign Penetration, League Cohesion, and old-movement pressure. This catches direct pressure writes that are not naturally routed through the foreign-pressure helper and stops Republic Momentum or Foreign Penetration from reaching 100 in a few days while the center is still strong.
- Terminal ordinary release includes Kazakhstan and vanilla-supported internal republic tags: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN`.
- Event-created internal republic tags use `soviet_collapse_internal_republic_focus_tree` with legal, security, liaison, and tag-specific regional branch content instead of the generic fallback tree.
- Terminal collapse now runs league formation before anti-Soviet war entry. Local leagues auto-form only where two-member regional quorum exists, while Free Republics' League expansion skips countries already committed to a local compact.
- Monthly guard constants cap ordinary successful, calm failed, and moderate failed months at low deltas when the center is not yet genuinely broken.
- Foreign-pressure writes from Soviet objectives, foreign patron actions, regional faction failures, and the focus foreign-channel helper now route through `soviet_collapse_apply_foreign_pressure_delta`, which tracks `soviet_collapse_monthly_foreign_pressure`, accepts both positive and negative deltas, and applies calm, moderate, and severe monthly caps before recalculating threat. Opening-pressure and some one-shot setup/focus effects still write directly by design and remain covered by component caps during recalculation.
- The 2026-05-23 focus-reward follow-up also expands direct custom-splinter and ancient-restoration `SOV = { add_to_variable = { soviet_collapse_* = ... } }` focus rewards into scoped blocks that immediately call `soviet_collapse_recalculate_total_threat`. This keeps route rewards that raise foreign appetite, old-movement pressure, depot vulnerability, military obedience, or related crisis components inside the same clamp/recompute surface instead of waiting for the next monthly or event-side recalculation.
- Monthly threat guard overflow is stored in `soviet_collapse_monthly_threat_dampening` and subtracted during later threat recalculations until a later guard pass no longer needs a cap. This closes the stale recalculation surface where the guard could cap `soviet_collapse_total_collapse_threat`, only for unchanged component values to rebuild the same threat total later in the month.
- Soviet emergency mobilisation is limited to three reserve call-ups, uses a 63-day re-enable delay, spends command power, and repeated call-ups add authority, depot, and foreign-pressure strain instead of remaining a pure manpower/equipment faucet.
- Foreign patron eligibility now requires SOV to exist and the Soviet Collapse crisis to be active. Foreign aid routing no longer treats war with SOV or a bare coastal route as a completed physical aid route. Sponsors need a faction channel, opened aid corridor, controlled shared border, or League channel for follow-on aid and dependency actions; mutual coastal access remains only a potential route for opening the corridor, with the corridor decision's own cost trigger handling fuel, train, and convoy affordability.
- Foreign client dependency escalation is limited to client-style patrons. Protection treaties and adviser privileges stamp the sponsoring patron onto the target, so later adviser and client-cabinet steps require the same sponsor rather than whichever patron later becomes dominant.
- Moscow federal compact reintegration now removes the target from the breakaway array, decrements local/global breakaway counts, clears external-dependency flags, and leaves the target as a federated subject instead of a stale breakaway target.
- Manual Soviet objective activation has phase-band gates in the activation effect itself. This closes the source-level stale-queue surface where `activate_mission` could ignore normal mission activation and queue legal-settlement, late recovery, foreign, old-movement, regional, League, high-chaos, or cleanup objectives before the matching crisis phase exists. The activation helper prunes invalid active late objectives before counting the active-objective cap, stamps each pruned late mission's existing done flag before removal so it cannot return with a fresh timer, and resolved-breakaway/league-formation effects call the same prune when the crisis phase changes outside a mission tick.
- Mission success helpers do not raise the main threat total.
- Mission failure helpers are bounded by a verified maximum single-failure delta of 4.25 threat. With the active mission cap at 10, even a full first wave of maximum-pressure failures from the calm baseline reaches 49.75.
- Progressive release MTTH weighs threat, authority, command obedience, depot vulnerability, foreign penetration, League pressure, old movements, failed missions, war state, regional cascades, and chaos tier. The 2026-05-23 tuning raises the low/moderate/high/severe/critical thresholds to 30/45/60/75/90, sets `release_base = 0`, raises `miss_base = 240`, and uses `can_soviet_collapse_roll_progressive_release` so calm strong-center games do not roll extra republic releases merely because the first-wave breakaways exist. Regional cascade modifiers now require moderate threat, five breakaways, weak center signals, war pressure, or capital-loss pressure. The latest follow-up adds dedicated release-gate thresholds, sustained unresolved-pressure weighting at 4 per eligible monthly pass capped at 24, severe-threat tapering for strong-center suppression, a direct Republic Momentum release factor, and a selected-candidate guard so empty candidate pools cannot start the release cooldown.
- The progressive release roll now belongs to the hidden 30-day SOV scheduler, not to every objective-board refresh or regional-league defensive-war effect. Those paths still apply pressure and recalculate threat, but they leave actual release rolls to `chaosx.nr5.129`. This preserves MTTH releases while preventing clustered mission completions, timeouts, or league war declarations from producing extra release rolls in the same month.
- Progressive release selection now uses `global.soviet_collapse_progressive_release_selection` as a scratch array instead of clearing the persistent first-wave memory array. Resolved Moscow-federated subjects are excluded from `is_soviet_collapse_progressive_release_candidate`, so MTTH pressure cannot spend a release on a republic already settled through the Moscow federal compact.

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
| Free-unit farming | Unit creation is limited to setup, terminal, MTTH, and costed decision paths. Soviet emergency mobilisation is capped at three reserve call-ups, spends command power, has a longer cooldown, and repeated call-ups strain authority, depots, and foreign pressure. | Live-session unit-count tuning. |
| Equipment farming | Equipment aid and mobilisation are behind cost triggers, visible cost text, command-power spending, cooldowns, and use caps; foreign aid adds sponsor influence or patronage risk and now requires a real aid route rather than war status alone. | Country-size scaling review. |
| Factory loops | Construction rewards are mostly one-shot focus or setup effects; foreign construction aid spends resources, adds influence, and applies timed patron burden. | Map-state placement review. |
| Influence farming | Target acceptance, protected-republic checks, dominant-sponsor comparisons, balanced sponsorship, patronage-risk pressure, active-SOV patron eligibility, controlled-route foreign aid checks, and sponsor-specific dependency-chain flags prevent silent sponsor stacking. | Sponsor-by-sponsor final audit. |
| Puppet abuse | Client-cabinet and dependency chains require weak targets, high influence, client-patron style, matching sponsor-chain flags, dominant sponsor checks, and fail against protected republics. | Live diplomacy edge cases. |
| War-goal, claim, and core spam | Source scan finds no `create_wargoal`; war entry is terminal-scripted, claims are one-shot focus rewards, and cores are release/setup effects. | Live diplomatic edge cases. |
| Mission pressure farming | Active mission cap is 10; success helpers are non-increasing for main threat and failure deltas stay below terminal bypass levels. | In-game category density review. |
| Release farming | Progressive releases use global cooldown, terminal-state gates, `can_soviet_collapse_roll_progressive_release`, candidate counting, selected-candidate confirmation, sustained-pressure reset on empty pools, and cascade-gated MTTH modifiers; Union Unmade uses first-month lock, severe-condition gates, and terminal cleanup. Strong-center MTTH miss weights suppress calm release chains, while weak-authority, component pressure, failed missions, and cascade factors still raise release odds. | Live pacing. |

## Non-Python Validation Commands

```text
rg -n "soviet_collapse_total_collapse_threat|soviet_collapse_monthly_successful_objectives|soviet_collapse_monthly_failed_objectives|soviet_collapse_union_unmade_first_month_lock|soviet_collapse_maybe_show_union_unmade_super_event" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt
rg -n '<''=|>''=' common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt
rg -n "soviet_collapse_apply_dynamic_pressure_caps|soviet_collapse_apply_monthly_component_growth_caps|soviet_collapse_apply_foreign_pressure_delta|can_soviet_collapse_roll_progressive_release|calm_failed_month_cap|moderate_failed_month_cap|release_base = 0|miss_base = 240" common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt
rg -n "python3[ ].tools/verify_event005_completion_gate.py" docs/events/005_soviet_collapse_balance_audit.md
```

Current checkout validation is based on the listed static source surfaces and scenario evidence above. The Python completion gate is deliberately not used as proof for this audit.
