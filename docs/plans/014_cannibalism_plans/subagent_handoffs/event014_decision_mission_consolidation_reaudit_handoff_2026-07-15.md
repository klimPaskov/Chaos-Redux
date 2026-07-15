# Event 014 Decision and Mission Consolidation Reaudit Handoff

Date: 2026-07-15

## Assignment

Reaudit the consolidated Event 014 decisions, missions, scripted-GUI actions, achievements, SCN-010 launch types, balance/reset behavior, population and recruitment safety, secrecy, origins, terminal gates, AI, and post-consolidation wiring. Apply only small local fixes and report P0-P3 findings.

## Outcome

The assigned surface has no unresolved finding after one narrow P1 remediation.

- P0 open: 0
- P1 open: 0
- P2 open: 0
- P3 open: 0
- P1 closed during audit: 1

The full evidence report is:

- `docs/plans/014_cannibalism_plans/audits/event014_decision_mission_consolidation_reaudit_2026-07-15.md`

## Runtime Change

Changed:

- `common/scripted_triggers/014_cannibalism_triggers.txt`

Identifier changed:

- `cannibalism_can_consume_current_state`

Added:

```txt
NOT = { has_state_flag = cannibalism_recovery_active }
```

Reason: the previous predicate blocked liberated emergency and final stabilization but allowed identification, institutional, and long-trauma recovery stages after the initial stage flag was replaced. The persistent recovery flag now blocks all canonical consumption and recruitment until recovery finishes.

No localization or interface text changed because the existing player-facing recovery contract already states that liberated states stop continuing losses.

## Documentation Added

- `docs/plans/014_cannibalism_plans/audits/event014_decision_mission_consolidation_reaudit_2026-07-15.md`
- this handoff

## Meaningful Validation

- Parsed 127 unique decision IDs: 94 paid decisions, 14 timed missions, 18 read-only trackers, and one cost-free exploitation-exit decision.
- Matched all 14 timed mission IDs to the 14 guarded reset removals with no missing or extra ID.
- Confirmed every paid decision has both a custom affordability trigger and custom cost text; all 90 unique cost localization keys exist.
- Confirmed all 43 derived unified affordability gates are assigned, reduced by the correct step, and used by triggers.
- Confirmed exact consumption request identity, applied-loss accounting, and post-transaction equality gates on all operational recruitment paths.
- Confirmed 16 interface buttons match 16 scripted-GUI callbacks; callbacks are presentation-only and reveal-gated.
- Confirmed 18 registry achievements, 18 completion-trigger calls, 18 read-only tracker decisions, and 18 scripted-localization status selectors.
- Confirmed SCN-010 has exactly five launch types and the launch wrapper branches to exactly five setup effects after preflight.
- Confirmed only Island Host, Siege Commune, and March Host origins exist; `Prison Host` is absent.
- Confirmed both terminal routes use strict greater-than comparison against the shared 1000 Chaos threshold.
- Confirmed the ordinary and transformed static portraits use `hannibal.dds` and `hannibal_wendigo.dds`, and both files exist.
- Confirmed all 95 selectable non-mission decisions have AI blocks and all eight targeted country decisions consume the mirrored unified or Wendigo MTTH scorer weight.
- Confirmed the consolidated effects, triggers, MTTH, scorers, constants, and registered categories contain no duplicate top-level identifiers; repeated decision-category blocks contain unique child decision IDs.

## Remaining Risks

No known risk remains in the assigned source-audit surface. This handoff does not claim runtime play-session execution or completion of unrelated Event 014 focus, asset, audio, or country-package work.

## Simplifications, Omissions, and Blockers

None. No fallback was used. No commit was created.
