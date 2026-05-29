# Soviet Collapse Focus Tree Reward and Route Patch Handoff

## Scope
- Audited and patched the four Soviet Collapse focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- This pass targeted shallow flag/variable rewards, weak route payoffs, route-lock clarity, and compact layout issues that could be fixed locally.

## Changed Focus IDs
- Shared/republic tree:
  - `soviet_collapse_rail_hub_or_mountain_pass`
  - `central_asia_soviet_collapse_local_republic_council`
  - `central_asia_soviet_collapse_military_border_authority`
  - `central_asia_soviet_collapse_foreign_border_patronage`
  - `central_asia_soviet_collapse_turkestan_federation_road`
- Custom splinters:
  - `PRA_novosibirsk_dispatcher_court`
  - `PRA_ticket_courts_for_every_platform`
  - `DSC_stalingrad_roll_call`
  - `DSC_revenant_staff_line`
  - `DSC_maps_of_lost_armies`
  - `NRF_murmansk_dead_muster`
  - `NRF_revenant_admiralty`
  - `NRF_maps_of_sunken_routes`
- Factory successors:
  - `CFR_the_trust_office_takes_the_seal`
  - `CFR_the_first_new_district`
  - `CFR_the_builder_state_marches_east`
  - `MFR_shop_floor_committees`
  - `MFR_the_arsenal_state`
- Ancient restorations:
  - `KZR_symbolic_crossing_state`
  - `KZR_expansionist_steppe_levy`
  - `SOG_symbolic_city_league`
  - `SOG_expansionist_merchant_claims`
  - `KHW_symbolic_oasis_authority`
  - `KHW_expansionist_water_claims`
  - `ALN_symbolic_pass_principality`
  - `ALN_expansionist_mountain_claims`

## Route Behavior Before and After
- `soviet_collapse_rail_hub_or_mountain_pass`
  - Before: opened a logistics choice flag and command power only.
  - After: also applies depot control, rail authority rewards, and actual infrastructure/rail construction.
- Central Asia route fork
  - Before: route exclusivity partly relied on hidden `available` checks, and the three visible route choices sat close together.
  - After: local council, military authority, foreign patronage, and Turkestan federation routes have explicit mutual exclusions; local and military choices were spaced apart; military/foreign/federation routes gained clearer manpower, depot, recognition, league, or diplomacy payoffs.
- PRA rail authority
  - Before: early political focuses mostly added authority variables.
  - After: early focuses surface existing rail decisions and apply rail authority/legal-recognition rewards.
- DSC and NRF chaos routes
  - Before: several early and mid-route focuses only added PP/XP/variables.
  - After: they unlock/surface existing dead-army or revenant-fleet decisions, add manpower/equipment/naval resources, and set aggressive SOV AI strategies on revenant payoffs.
- CFR/MFR factory successors
  - Before: several factory identity focuses only called a helper effect.
  - After: CFR surfaces reconstruction decisions; MFR worker and arsenal focuses add institution/equipment/AI specialization around arms factories and anti-SOV aggression.
- Ancient restorations
  - Before: symbolic branches were largely recognition/stability and expansion branches had claims but little AI aggression.
  - After: symbolic routes gained small real construction where missing; expansion routes gained SOV conquer/antagonize AI strategies; branch pairs were spaced to reduce line crowding.

## Localisation and Icon Changes
- No localisation keys were added or renamed.
- No icon IDs were changed.
- Added `unlock_decision_tooltip` references only to existing decision IDs:
  - `pra_consolidate_timetable_courts`
  - `dsc_verify_the_roll_call`
  - `dsc_convene_the_dead_army`
  - `nrf_recover_drowned_ship_logs`
  - `nrf_call_the_revenant_fleet`
  - `cfr_survey_unfinished_sites`
  - `cfr_issue_reconstruction_contracts`
  - `mfr_convert_depots_to_arms_lines`

## Validation Run
- Brace/count sanity on all four focus files:
  - `005_soviet_collapse_republics.txt`: `4245/4245`, balance `0`
  - `005_soviet_collapse_custom_splinters.txt`: `10866/10866`, balance `0`
  - `005_soviet_collapse_factory_successors.txt`: `1340/1340`, balance `0`
  - `005_soviet_collapse_ancient_restorations.txt`: `618/618`, balance `0`
- Repeated same-idea additions:
  - Republics: `0` idea reward refs, duplicates `none`
  - Custom splinters: `7` idea reward refs, duplicates `none`
  - Factory successors: `1` idea reward ref, duplicates `none`
  - Ancient restorations: `0` idea reward refs, duplicates `none`
- Unsupported operator scan on edited focus files:
  - `rg -n "<=|>=|type = naval_avoid_region" ...` returned no matches.
- Decision tooltip hook scan confirmed every added `unlock_decision_tooltip` target appears in the focus files with the intended IDs.

## Remaining Risks and Broad Gaps
- This was not a full redesign of all 1,698 focuses. Many template-derived custom splinter and ancient trees still share repeated icon families and parallel layouts.
- Duplicate coordinates remain across different focus trees in the same file because multiple independent trees reuse the same compact template coordinates. The quick scan reports those as duplicates even when they are not in the same visible tree.
- Several Soviet Collapse trees still rely heavily on helper effects; a future deeper pass should audit helper-effect variety and final route endpoint strength tree by tree.
- No new localisation was required for changed rewards, but existing descriptions were not exhaustively checked for every reward-helper nuance across all four large files.
- No commit was made because the working tree already contained unrelated dirty and untracked work in the same target area; staging whole files would risk committing other agents' changes.
