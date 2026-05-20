# Event 005 Soviet Collapse Validation Report

Audit date: 2026-05-20

## Validation Type

This report records current script/parser validation and deterministic verifier scenarios. It does not claim a live in-game playthrough. The repository instruction says the user verifies live sessions, so this report avoids log requests and records only evidence available in the worktree.

## Commands Run

```text
python3 -m py_compile .tools/verify_event005_completion_gate.py
python3 .tools/verify_event005_completion_gate.py
git diff --check
rg -n "<=|>=" common/scripted_effects/005_soviet_collapse_effects.txt
```

The verifier compiled and exited 0. Static checks for the current correction pass passed: no whitespace errors and no forbidden comparison operators in the edited script file.

## Scenario Matrix

| Scenario | Evidence | Result |
| --- | --- | --- |
| Calm World, strong USSR, event fired manually | `crisis_balance_surface` | Authority 62, Threat 7.25 |
| Calm World, strong USSR, Soviet missions succeed for six months | `mission_success_pressure_surface`, `crisis_monthly_guard_surface` | Success helpers are non-increasing; ordinary months are guarded |
| Calm World, strong USSR, Soviet missions fail for six months | `crisis_monthly_guard_surface` | Ordinary failure max delta 2.75; not terminal in first month |
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
| Internal republic focus tree review | `internal_republic_focus_loader`, `internal_republic_focus_tree`, `internal_republic_focus_localisation` | vanilla-supported internal republic tags route to a 20-focus shared tree with regional branches |

## Latest Correction Validated

The previous audit recorded a verifier that fails if:

- local league founding triggers do not call explicit quorum triggers, or
- ordinary local league and normal League-route content calls local super-event helpers.

The restored verifier checks these current surfaces:

```text
Union Unmade threat-ceiling calls now route through the guarded maybe-show helper.
Kazakhstan is included in terminal ordinary release and subject-freeing lists.
Vanilla-supported internal republic tags are included in terminal release and subject-freeing lists.
Vanilla-supported internal republic tags route to `soviet_collapse_internal_republic_focus_tree` instead of the generic fallback tree.
Terminal collapse calls the high-chaos successor spawn helper and anti-Soviet war pass.
Terminal collapse calls local-league and Free Republics' League formation between release/spawn and war entry.
Mission objective blocks have timed non-selectable shape, hidden scripted requirements, localized requirement/success/failure text, and distinct success/failure effects.
Event 005 focus IDs are unique across republic, custom splinter, and factory successor trees, and all focus IDs have localisation with UTF-8 BOM Event 005 localisation files.
Event 005 focus integrity covers 775 focus blocks with icons, coordinates, completion rewards, AI weights, and resolved focus prerequisite/mutual-exclusion references.
```

## Blockers

The restored verifier covers deterministic script surfaces, not live-session feel or the full final design claim. Live-session behavior remains the final practical check for pacing, league joining, terminal war entry, and whether shared regional trees feel sufficiently distinct in play.
