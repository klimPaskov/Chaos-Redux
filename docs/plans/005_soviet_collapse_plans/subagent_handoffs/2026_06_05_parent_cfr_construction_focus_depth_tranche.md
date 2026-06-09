# Event005 Parent Handoff: CFR Construction Focus Depth Tranche

## Scope

Parent implementation tranche for the Construction Directorate/CFR focus tree inside Event005 Soviet Collapse.

This is not a completion claim for Event005. It records a bounded patch to reduce shallow focus rewards and make the CFR opening/early strategy path connect to the existing construction mandate, reconstruction contract, and map-building mechanics.

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Changed Identifiers

New scripted effects:

- `soviet_collapse_apply_cfr_focus_opening_crane_census`
- `soviet_collapse_apply_cfr_focus_housing_city_program`
- `soviet_collapse_apply_cfr_focus_contracting_office`

Adjusted scripted effect:

- `soviet_collapse_apply_cfr_focus_contracts_first`

Adjusted CFR focuses:

- `CFR_count_the_cranes`
- `CFR_the_trust_office_takes_the_seal`
- `CFR_ration_cards_for_workers`
- `CFR_emergency_cement_accounts`
- `CFR_the_unfinished_city_speaks`
- `CFR_contracts_first`
- `CFR_apartment_blocks_for_loyalty`
- `CFR_the_first_new_district`

Adjusted decisions:

- `cfr_issue_reconstruction_contracts`
- `cfr_seize_idle_construction_queues`

New localisation keys:

- `CFR_count_the_cranes_mechanics_tt`
- `CFR_the_trust_office_takes_the_seal_mechanics_tt`
- `CFR_ration_cards_for_workers_mechanics_tt`
- `CFR_emergency_cement_accounts_mechanics_tt`
- `CFR_the_unfinished_city_speaks_mechanics_tt`
- `CFR_contracts_first_tt`
- `CFR_apartment_blocks_for_loyalty_mechanics_tt`
- `CFR_the_first_new_district_mechanics_tt`

## Behavior Before

- Several CFR focuses only called small helper rewards or showed long raw construction effects.
- `CFR_emergency_cement_accounts` displayed a reconstruction-contract unlock, but the decision visibility did not accept that focus flag.
- `CFR_contracts_first` did not immediately unlock the decision pair that makes contract-first gameplay feel different.
- Early CFR rewards did not consistently create map-visible construction outcomes.

## Behavior After

- Early CFR focuses now use compact custom tooltips and hidden construction payloads.
- The opening crane census creates construction mandates, offsite civilian capacity, site registry progress, controlled-core infrastructure, and a rail reconnection.
- Housing-oriented focuses improve stability, site registry depth, controlled-core slots, and infrastructure without adding new idea spam.
- Emergency Cement Accounts now builds the contracting office mechanically and unlocks both survey and reconstruction contract decisions.
- Contract-first now unlocks reconstruction contracts and idle-queue seizure, deepens the contract network, improves recognition, and adds a client factory site.
- The reconstruction-contract decision is visible from `cfr_focus_emergency_cement_accounts`.
- The idle-queue seizure decision is visible from `cfr_strategy_contracts_first`.

## Validation

Run by parent:

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Unsupported operator scan for `<=` and `>=` on touched script/focus/decision/trigger files: no matches.
- Brace balance check on:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- CFR focus coordinate duplicate check: 47 CFR focuses, no duplicate coordinate output.
- Localisation BOM check for `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: BOM present.

## Remaining Gaps

- This tranche only deepens CFR. Other Event005 focus trees still need systematic reward-depth review.
- Event005 is still not complete: staged release pacing, evolution detail parity, dynamic decision expansion behavior, and broad focus-tree route depth remain active parent work.
- No flags were touched in this tranche.
