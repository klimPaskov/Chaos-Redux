# IW-012 formal route AI closure implementation handoff

Date: 2026-07-28

Status: **IMPLEMENTED / STATIC REVIEW PENDING**

## Scope

The bounded improvement-loop design in `006_iw012_formal_route_ai_closure_addendum_2026_07_28.md` is implemented without adding a country, tag, history file, leader, portrait, advisor icon, flag, decision, focus, formable, GUI, or reward family.

## Gameplay changes

- `common/decisions/006_independence_wave_ice_decisions.txt` now gives all six paid projects state-aware AI willingness from the ICE ledgers, war, severe host threat, Compact readiness, former-host pressure, and League membership.
- Armed Neutrality no longer calls `independence_wave_select_government_route`; it remains a paid, one-time security commitment that supplies the Emergency Military route with a visible signal.
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt` adds ICE-local Compact-posture and former-host-charter-pressure predicates.
- `common/national_focus/006_independence_wave_focus.txt` now gives the four mutually exclusive formal route focuses distinct ledger, host, war, instability, Coastwatch, Compact, and League weights.

Existing project costs, durations, caps, route prerequisites, focus costs, mutual exclusions, completion rewards, and cleanup are unchanged. The four route focuses remain the only formal government-route writers.

## Localisation and documentation

The Armed Neutrality tooltip now describes a security commitment and leaves the formal route choice to the route focuses. The IW-012 event package, Part 5 package contract, Part 7 AI matrix, source-of-truth map, and resume packet record the two-stage arbitration rule.

## Static acceptance targets

- No `independence_wave_select_government_route` call remains in the ICE decision file.
- No literal `DEN` is introduced by the closure.
- The exact source weights reproduce the five design scenarios in the addendum before engine normalization.
- The vanilla `iceland_tree` carrier and all Event 006 imports remain untouched.
- BOM, duplicate-localisation, brace/depth, allocator, and installed-tag collision checks remain required before tranche commit.

## Remaining evidence

Read-only probability inspection, live shared-focus visibility, AI project timing, route selection, allocator/save-load, host-survival, scenario transaction, GUI, achievement, super-event, and whole-event completion evidence remain open. Event 006 stays **HOLD / PARTIAL**.
