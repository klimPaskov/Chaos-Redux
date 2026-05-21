# Event 005 Sponsor Influence Audit

Audit date: 2026-05-21

## Scope

This audit checks the Part 3 influence-war and sponsor-dependency requirements against the current source. It covers sponsor eligibility, per-sponsor tracking, influence categories, foreign aid decisions, Moscow reintegration, balanced sponsorship, dominant sponsor pressure, and the foreign puppet chain. It is source-level evidence and does not claim a live in-game playthrough.

## Sponsor Coverage

Foreign patron eligibility is explicit in `is_soviet_collapse_foreign_patron_candidate`. The trigger accepts only the tracked sponsor tags below, while still requiring an active war with Moscow or negative opinion of Moscow. This prevents untracked majors from adding only generic total influence.

| Sponsor | Tag | Sponsor-specific variable | Coverage |
| --- | --- | --- | --- |
| Germany | `GER` | `soviet_collapse_influence_germany` | candidate, influence delta, balance pressure, dominance comparison |
| United Kingdom | `ENG` | `soviet_collapse_influence_britain` | candidate, influence delta, balance pressure, dominance comparison |
| Japan | `JAP` | `soviet_collapse_influence_japan` | candidate, influence delta, balance pressure, dominance comparison |
| France | `FRA` | `soviet_collapse_influence_france` | candidate, influence delta, balance pressure, dominance comparison |
| United States | `USA` | `soviet_collapse_influence_usa` | candidate, influence delta, balance pressure, dominance comparison |
| Turkey | `TUR` | `soviet_collapse_influence_turkey` | candidate, influence delta, balance pressure, dominance comparison |
| Iran | `PER` | `soviet_collapse_influence_iran` | candidate, influence delta, balance pressure, dominance comparison |
| Poland | `POL` | `soviet_collapse_influence_poland` | candidate, influence delta, balance pressure, dominance comparison |
| Romania | `ROM` | `soviet_collapse_influence_romania` | candidate, influence delta, balance pressure, dominance comparison |
| Finland | `FIN` | `soviet_collapse_influence_finland` | candidate, influence delta, balance pressure, dominance comparison |
| Sweden | `SWE` | `soviet_collapse_influence_sweden` | candidate, influence delta, balance pressure, dominance comparison |
| Italy | `ITA` | `soviet_collapse_influence_italy` | candidate, influence delta, balance pressure, dominance comparison |
| Moscow | `SOV` | `soviet_collapse_influence_moscow` | reintegration treaty, federal compact, Moscow dominance comparison |
| Free Republics' League | faction/channel | League cohesion, League logistics channel, League member flags | channel and balancing path rather than a normal country sponsor variable |

## Influence Categories

| Required category | Source variable or mechanic | Main source actions |
| --- | --- | --- |
| Recognition | `soviet_collapse_influence_recognition_total` | recognition, conference, press network, protection treaty |
| Arms | `soviet_collapse_influence_arms_total` | armaments, military construction, aid corridor, League logistics |
| Volunteers | `soviet_collapse_influence_volunteers_total` | advisers, volunteer corps, adviser privileges |
| Industrial investment | `soviet_collapse_influence_industry_total` | trade mission, civilian construction, military construction |
| Intelligence | `soviet_collapse_influence_intelligence_total` | republican intelligence channel |
| Ideology | `soviet_collapse_influence_ideology_total` | ideological liaison, press and radio network, client cabinet |
| Logistics | `soviet_collapse_influence_logistics_total` | armaments, intelligence, trade, construction, aid corridor, League logistics |
| Patronage risk | `soviet_collapse_influence_patronage_risk` | liaison, advisers, intelligence, volunteers, trade, construction, press network, aid corridor, League logistics, anti-puppet clause, reintegration, dependency chain |

Each foreign action that changes sponsor influence calls `soviet_collapse_apply_foreign_influence_delta`, which increments `soviet_collapse_influence_total`, updates the matching sponsor variable, and then calls `soviet_collapse_update_sponsor_balance_pressure`.

## Foreign Decision Coverage

The foreign patron category has 17 targeted decisions:

| Decision | Role |
| --- | --- |
| `soviet_collapse_recognize_breakaway_government` | recognition influence |
| `soviet_collapse_fund_ideological_liaison_offices` | ideology, recognition, patronage risk |
| `soviet_collapse_ship_border_armaments` | arms and logistics |
| `soviet_collapse_dispatch_military_advisers` | advisers, volunteers, patronage risk |
| `soviet_collapse_open_republican_intelligence_channel` | intelligence, logistics, patronage risk |
| `soviet_collapse_sponsor_volunteer_corps` | volunteers, patronage risk, field-force support |
| `soviet_collapse_negotiate_republican_trade_mission` | industry, logistics, patronage risk |
| `soviet_collapse_fund_civilian_construction_mission` | industry, logistics, patronage risk, construction burden |
| `soviet_collapse_fund_military_construction_mission` | arms, industry, logistics, patronage risk |
| `soviet_collapse_sponsor_press_and_radio_network` | ideology, recognition, patronage risk |
| `soviet_collapse_secure_republican_aid_corridor` | logistics, arms, patronage risk, route flag |
| `soviet_collapse_build_republics_league_conference` | recognition, resilience, League cohesion |
| `soviet_collapse_route_aid_through_league_logistics` | logistics, arms, resilience, League cohesion, lower dependency pressure |
| `soviet_collapse_demand_anti_puppet_clause` | resilience and patronage-risk resistance |
| `soviet_collapse_offer_protection_treaty` | dependency chain step 1 |
| `soviet_collapse_demand_adviser_privileges` | dependency chain step 2 |
| `soviet_collapse_install_client_cabinet` | dependency chain step 3 and puppet effect |

The Part 3 decision examples are covered directly or by equivalent current names. `Expose Foreign Patronage`, `Counter-Sponsor Radio Campaign`, and `Offer Better Guarantees` are represented by anti-puppet clauses, conference guarantees, League logistics, press/radio pressure, and Soviet objective missions that contest sponsor influence rather than by separate duplicate foreign buttons.

## Acceptance, Balance, And Dependency Guards

- `can_target_soviet_collapse_breakaway_for_aid` requires an existing breakaway target, a valid aid route, no war between sponsor and target, and target acceptance.
- `has_soviet_collapse_target_acceptance_for_foreign_aid_from_root` opens aid through wartime pressure, weak target state, equipment shortage, aid corridor, balanced sponsorship, recognition, low resilience, low patronage risk, relief style, or League conference style.
- The same acceptance trigger blocks client-style pressure when patronage is already high unless balanced sponsorship exists.
- `soviet_collapse_update_sponsor_balance_pressure` tracks active sponsor count, top sponsor, second sponsor, and sponsor gap. Two or three meaningful sponsors add independence resilience and reduce patronage risk. One dominant lead adds patronage risk and lowers resilience.
- `can_target_soviet_collapse_breakaway_for_foreign_protection_treaty`, `can_target_soviet_collapse_breakaway_for_foreign_adviser_privileges`, and `can_target_soviet_collapse_breakaway_for_foreign_client_cabinet` require weak targets, low resilience, no subject status, no active war with Moscow, no strong dependency protection, a valid route, and dominant ROOT sponsor influence.
- Moscow reintegration uses separate union treaty and federal compact triggers, records `soviet_collapse_influence_moscow`, and requires low threat, sufficient Moscow Authority, weak target conditions, and Moscow dominance for the compact step.

## Validation Commands

```text
python3 - <<'PY'
from pathlib import Path
tr = Path('common/scripted_triggers/005_soviet_collapse_triggers.txt').read_text()
eff = Path('common/scripted_effects/005_soviet_collapse_effects.txt').read_text()
sponsors = {
    'Germany':'GER:germany', 'United Kingdom':'ENG:britain', 'Japan':'JAP:japan',
    'France':'FRA:france', 'United States':'USA:usa', 'Turkey':'TUR:turkey',
    'Iran':'PER:iran', 'Poland':'POL:poland', 'Romania':'ROM:romania',
    'Finland':'FIN:finland', 'Sweden':'SWE:sweden', 'Italy':'ITA:italy',
    'Moscow':'SOV:moscow',
}
for name, spec in sponsors.items():
    tag, var = spec.split(':')
    print(name, tag, eff.count('soviet_collapse_influence_' + var) + tr.count('soviet_collapse_influence_' + var))
PY
rg -n "is_soviet_collapse_foreign_patron_candidate|soviet_collapse_apply_foreign_influence_delta|soviet_collapse_update_sponsor_balance_pressure|can_target_soviet_collapse_breakaway_for_foreign_(protection_treaty|adviser_privileges|client_cabinet)" common/scripted_triggers/005_soviet_collapse_triggers.txt common/scripted_effects/005_soviet_collapse_effects.txt
```

## Result

The source now covers the listed sponsors, influence categories, balanced-sponsorship safeguards, Moscow reintegration, and foreign dependency chain. Remaining broader Event 005 work is tracked elsewhere in the full implementation ledger.
