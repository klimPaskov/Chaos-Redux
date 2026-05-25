# Event 005 - Central Asia League Decisions

## Overview

The Central Asia endgame route has a live decision surface once a southern runtime republic reaches the Southern Shield, pact choice, loose pact, federation, or final survival focus flags. The decisions sit in the breakaway category and use the existing focus flags rather than changing the focus tree layout.

## Player Surface

- Register a Water-Sharing Council: converts water and canal administration into institutions, League support, stability, and infrastructure.
- Levy the Cotton-Rail Quota: turns cotton, rail repair, and fuel accounting into depot control, League support, war support, equipment, and a supply node.
- Convene the Pass and Caravan Board: spends command capacity and stores to secure passes, caravan routes, depots, and frontier fortifications.
- Submit the Member Vote Protocol: raises recognition, resilience, stability, and Central Asian League program progress.
- Request a Foreign Mediation Desk: channels outside patrons through a visible mediation desk, improving liaison reach and reducing patronage risk while still raising Soviet foreign-pressure awareness.
- Ratify the Southern Survival Settlement: requires enough program progress and the final survival focus flag, then consolidates institutions, resilience, League support, recognition, stability, war support, and limited industrial repair.

## Wiring

The decisions are in `common/decisions/005_soviet_collapse_central_asia_league_decisions.txt`.

Reusable gates live in `common/scripted_triggers/005_soviet_collapse_triggers.txt`, including the Central Asia decision-surface trigger, individual cost triggers, and the final settlement progress gate.

Costs and tuning live under `soviet_collapse_central_asia_league` in `common/script_constants/005_soviet_collapse_constants.txt`.

Effects live in `common/scripted_effects/005_soviet_collapse_effects.txt`. They update republic variables, consolidated republic spirits, and Moscow-facing League, depot, and foreign pressure.

Localisation lives in `localisation/english/005_soviet_collapse_l_english.yml`.

## Icons

This slice requires no additional sprites. The decisions reuse existing Event 005 decision icons:

- `GFX_decision_soviet_collapse_authority_goal`
- `GFX_decision_soviet_collapse_rail_goal`
- `GFX_decision_soviet_collapse_depot_goal`
- `GFX_decision_soviet_collapse_foreign_goal`

## Future Plans

- Add targetable member aid once Central Asian League membership quality is audited across Uzbekistan, Kyrgyzstan, Tajikistan, Turkmenistan, and Kazakhstan.
- Give Basmachi, Turkestan National Council, and Alash variants tailored versions of the same water, caravan, and mediation surface rather than sharing only the ordinary republic route.
