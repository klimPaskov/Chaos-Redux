# Event 005 - Kazakhstan Route Decisions

## Overview

Kazakhstan's route-defining focuses unlock a live decision surface in the breakaway category instead of ending as generic focus rewards. The surface uses existing focus-set flags for the Alash, socialist steppe, resource directorate, and foreign concession paths.

## Player Surface

- Convene Alash Court Commissions: spends political staff and command liaison capacity to build Alash legal authority, institutions, recognition, democratic organization, and stability.
- Issue the Steppe Soviet Supply Plan: spends political staff, trains, and fuel to build socialist planning, depot control, communist organization, war support, and infrastructure.
- Secure Minehead Guard Contracts: spends command capacity and stores to protect mines, improve resource authority, strengthen depot control, add equipment, improve steel output, and harden resilience.
- Audit Foreign Concession Ledgers: spends political staff, convoy paperwork, and fuel to improve concession control, liaison reach, recognition, and support stores while reducing patronage risk.

## Wiring

The decisions are in `common/decisions/005_soviet_collapse_kazakhstan_route_decisions.txt`.

Costs and tuning live under `soviet_collapse_kazakhstan_route` in `common/script_constants/005_soviet_collapse_constants.txt`.

Visibility and cost gates live in `common/scripted_triggers/005_soviet_collapse_triggers.txt`.

Effects live in `common/scripted_effects/005_soviet_collapse_effects.txt`. They update Kazakhstan route variables, consolidated republic spirits, and measured Moscow-facing republic, depot, or foreign pressure.

Localisation lives in `localisation/english/005_soviet_collapse_kazakhstan_route_decisions_l_english.yml`.

## Icons

This slice requires no additional sprites. The decisions reuse existing Event 005 decision icons:

- `GFX_decision_soviet_collapse_authority_goal`
- `GFX_decision_soviet_collapse_rail_goal`
- `GFX_decision_soviet_collapse_depot_goal`
- `GFX_decision_soviet_collapse_foreign_goal`

## Future Plans

- Connect later Kazakhstan focus-end states to route-score thresholds so Alash, socialist, federation, and resource-state endings can demand different institutional proof.
- Add targeted neighbor decisions for southern federation diplomacy once the Central Asian route audit is complete.
