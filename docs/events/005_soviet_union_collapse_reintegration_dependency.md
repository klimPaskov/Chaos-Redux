# Event 005 - Reintegration And Dependency Pressure

## Overview

This mechanic adds the negotiated side of the Soviet Collapse influence war. Moscow can use credible low-threat influence to pull weak breakaway republics into a federated compact, while foreign patrons can only puppet a republic through a staged dependency chain. Both routes read the same republic-side influence variables used by the wider intervention system.

## Moscow Path

`Offer a New Union Treaty` targets a breakaway republic from the Soviet crisis category. It is available when Union Crisis Threat is low or moderate, Moscow Authority is credible, the republic is not at war with Moscow, the republic is not already a subject, and a strong League or faction is not protecting it. The decision spends political power, command power, fuel, and trains. It raises `soviet_collapse_influence_moscow`, lowers target patronage pressure, lowers independence resistance, and applies New Union Negotiations.

`Offer a Federal Reintegration Compact` is the follow-up. It requires the treaty flag, dominant Moscow influence over every foreign sponsor variable, lower Union Crisis Threat, stronger Moscow Authority, weak target stability or war support, and low foreign patronage lock-in. It sets the republic as a Soviet autonomous subject with `set_autonomy` and marks the republic as peacefully federated.

## Foreign Sponsor Path

Foreign dependency is a three-step chain:

1. `Offer Protection Treaty`
2. `Demand Adviser Privileges`
3. `Install Client Cabinet`

The protection treaty requires the sponsor to be the dominant influence holder, the target to be weak, low target independence resilience, no active war with Moscow, no subject status, and no strong League or faction protection. Adviser privileges require the protection treaty. Client cabinet installation requires adviser privileges and then sets the target as the sponsor's puppet. All three dependency steps use the same ordinary, regional, and major target-tier cost model as direct foreign aid, so stronger republics demand larger political, command, fuel, army experience, and manpower commitments before they can be pulled into client status.

The chain uses `soviet_collapse_influence_total`, sponsor-specific influence variables, `soviet_collapse_influence_patronage_risk`, and `soviet_collapse_independence_resilience`. Balanced sponsorship and League protection block or delay dependency, while one dominant sponsor can convert influence into puppet pressure.

## Tuning

Tuning lives in `common/script_constants/005_soviet_collapse_constants.txt`:

- `soviet_collapse_moscow_reintegration`: Soviet treaty and compact costs, threat ceilings, authority floors, target weakness thresholds, and pressure effects.
- `soviet_collapse_puppet_pressure`: sponsor dominance thresholds, total influence floor, target weakness thresholds, resilience limits, and local side effects.
- `soviet_collapse_influence_war`: Moscow influence gains, protection treaty influence, adviser privilege influence, client cabinet influence, and patronage-risk deltas.

Dependency-chain cost text is dynamic. `common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt` selects ordinary, regional, or major values for protection treaty, adviser privileges, and client cabinet costs, and the matching `_cost_text` localisation shows only icon-value groups.

## Script Surfaces

- Decisions: `common/decisions/005_soviet_collapse_decisions.txt`
- Triggers: `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- Effects: `common/scripted_effects/005_soviet_collapse_effects.txt`
- Localisation: `localisation/english/005_soviet_collapse_l_english.yml`
- Verification: `.tools/verify_event005_completion_gate.py`, check `reintegration_puppet_surface`

## Icons

No new icons are required for this mechanic. The decisions reuse existing Event 005 decision sprites:

- `GFX_decision_soviet_collapse_regional_goal_recognition`
- `GFX_decision_soviet_collapse_free_soviet_congress`
- `GFX_decision_soviet_collapse_foreign_recognition`
- `GFX_decision_soviet_collapse_foreign_advisers`
- `GFX_decision_soviet_collapse_foreign_ideology`

These sprite names are already registered in `interface/005_soviet_collapse_icons.gfx`.

## Future Extensions

The next pass can add refusal events, sponsor anger, counter-influence decisions, and League neutrality resolutions. A later event pass can also split federal reintegration into softer autonomy and direct reintegration outcomes if the republic's focus route explicitly accepts Moscow's settlement.
