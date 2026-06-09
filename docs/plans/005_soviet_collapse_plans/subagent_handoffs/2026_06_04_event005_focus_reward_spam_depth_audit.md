# Event005 Focus Reward Spam and Depth Audit Handoff

## Scope

Audited these focus files for Soviet Collapse reward spam and route depth:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Related helper files inspected:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/ideas/005_soviet_collapse_ideas.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`

Used the `hoi4-focus-trees` and `chaos-redux-events` skills. Consulted the required offline Paradox wiki pages and vanilla documentation before editing.

## Findings

- A read-only recursive reward trace found no current same-focus duplicate same-idea additions reachable from the inspected `completion_reward` blocks. Earlier dirty-worktree changes appear to have removed the most obvious consolidated-idea spam pattern.
- Raw/direct idea operations in focus rewards are currently limited to cleanup/removal cases:
  - `PRA_the_board_overrules_ministers` removes `pra_dispatcher_court_tensions`.
  - `TSC_the_committee_of_instruments` removes `tsc_field_station_rivalries`.
  - `RMC_communes_of_witnesses` removes `rmc_credal_cell_rivalries`.
  - `DSC_witness_officers` removes `dsc_grave_regiment_rivalries`.
  - `NRF_living_harbor_committees` removes `nrf_drowned_crew_disputes`.
  - `ICD_commissars_of_last_addresses` removes `icd_grave_commissar_rivalries`.
  - `OGB_the_council_takes_the_seal` removes `ogb_disputed_restored_name`.
- `soviet_collapse_update_pra_authority_idea` still has many internal add/remove paths for the PRA staged authority idea, but this is a staged lifecycle helper rather than multiple focus helpers applying the same idea in one reward.
- Remaining route-depth gaps are mainly shallow local rewards in high-chaos branches, especially OGB river legitimacy nodes and FEV Far Eastern economic/logistics nodes. Some NRF and DSC nodes should still receive a focused follow-up pass, but broad rewrites were outside this small-patch audit.

## Patches

Changed `common/national_focus/005_soviet_collapse_custom_splinters.txt`:

- `FEV_customs_house_ledger`: added `soviet_collapse_apply_focus_foreign_channel = yes` so the customs/liaison node contributes to recognition, foreign-channel depth, recovery progress, and existing high-chaos pressure payloads.
- `FEV_nikolsk_workshop_contracts`: added `soviet_collapse_apply_focus_depot_and_supply_control = yes` so the workshop node is not only one arms factory plus political power.
- `FEV_amur_river_ports`: added `soviet_collapse_apply_focus_depot_and_supply_control = yes` so the river-port node connects to depot depth and supply mechanics.

Changed `common/national_focus/005_soviet_collapse_factory_successors.txt`:

- `OGB_kazan_ferry_offices`: added `soviet_collapse_apply_focus_depot_and_supply_control = yes` to connect the ferry office economy node to depot/supply depth.
- `OGB_steppe_caravan_letters`: added `soviet_collapse_apply_focus_foreign_channel = yes` to make the caravan diplomacy node advance existing foreign-channel mechanics.

No idea additions, idea swaps, timed ideas, new flags, flag asset paths, `.tga` files, flag `.gfx` files, or flag sprite wiring were edited.

## Validation

- Brace balance on the four inspected focus files plus Event005 effect, idea, decision, and constant files: passed.
- `git diff --check` on the patched focus files: passed.
- `rg -n "<=|>="` on the inspected Event005 focus/effect/idea/decision/constant files: no matches.
- Flag asset diff/status check for `gfx/flags`, `flags/`, `.tga`, flag `.gfx`, or flag sprite wiring paths: no matches.

## Remaining Work

- Do a follow-up high-chaos depth pass for NRF and DSC. Current audit saw NRF nodes such as `NRF_arkhangelsk_ice_registers`, `NRF_ghost_convoy_escorts`, and `NRF_maps_of_sunken_routes` still leaning on local naval/building rewards.
- OGB still has route identity nodes (`OGB_scholars_guard_the_charter`, `OGB_clerics_guard_the_charter`, `OGB_society_of_the_restored_name`) that could use more distinct branch payoffs in a larger parent-approved pass.
- Keep monitoring PRA authority idea updates, but do not remove its staged cleanup helper unless a live duplicate application is proven from a specific focus reward.
