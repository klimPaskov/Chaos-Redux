# Event 006 Targeted Decision Tooltip Tranche

Parent tranche: 2026-06-05 08:44 UTC

## Changed files

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`

## Scope

Hardened a bounded set of targeted patronage and New States Congress decisions so their root and target requirements show concise custom tooltips instead of only hidden scripted gates.

## Changed decision ids

- `independence_wave_major_recognize_committee`
- `independence_wave_major_supply_rifles`
- `independence_wave_major_offer_military_mission`
- `independence_wave_major_demand_cabinet_seats`
- `independence_wave_major_sabotage_rival_patron`
- `independence_wave_sign_mutual_guarantee`
- `independence_wave_recognize_impossible_delegate`
- `independence_wave_bind_strange_cooperation`
- `independence_wave_send_congress_volunteer_cadre`

## Localisation keys added

- `independence_wave_major_patronage_root_requirements_tt`
- `independence_wave_major_recognize_committee_target_requirements_tt`
- `independence_wave_major_supply_rifles_target_requirements_tt`
- `independence_wave_major_offer_military_mission_target_requirements_tt`
- `independence_wave_major_demand_cabinet_seats_target_requirements_tt`
- `independence_wave_major_sabotage_rival_patron_target_requirements_tt`
- `independence_wave_congress_target_root_requirements_tt`
- `independence_wave_sign_mutual_guarantee_target_requirements_tt`
- `independence_wave_recognize_impossible_delegate_target_requirements_tt`
- `independence_wave_bind_strange_cooperation_root_requirements_tt`
- `independence_wave_bind_strange_cooperation_target_requirements_tt`
- `independence_wave_send_congress_volunteer_cadre_target_requirements_tt`

## Before and after behavior

Before, these decisions had costs, effects, and AI weights, but target/root eligibility was displayed through hidden or raw trigger structure.

After, the same scripted triggers remain authoritative, but each root or target gate has a player-facing `custom_trigger_tooltip` summary. Costs, AI weights, cooldowns, effects, and target arrays were not changed.

## Validation

Run follow-up static checks for brace balance, localisation BOM, `:0` style, missing localisation keys, and unsupported comparison operators on the touched files.

## Remaining gaps

- Later Border Commission, compact, and Formation Ledger targeted decisions still need the same tooltip treatment.
- This tranche does not add true scripted GUI buttons or animation assets.
- This tranche does not claim Event 006 completion.
