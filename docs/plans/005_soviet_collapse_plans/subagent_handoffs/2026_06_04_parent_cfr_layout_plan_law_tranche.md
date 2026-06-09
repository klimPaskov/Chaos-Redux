# Parent Handoff: CFR Layout and Plan-Law Focus Tranche

Date: 2026-06-04
Owner: parent Codex agent
Scope: Event005 Soviet Collapse focus-tree cleanup and reward-depth work

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `docs/events/005_soviet_collapse.md`

No flag files or flag sprite folders were touched.

## Focus IDs Changed

- `CFR_elect_the_site_committees`
- `CFR_publish_the_planners_charter`
- `CFR_invite_the_foreign_contract_board`
- `CFR_the_concrete_committee`
- `CFR_minutes_from_every_workshop`
- `CFR_the_engineers_overrule_the_party`
- `CFR_contracts_before_ideology`
- `CFR_housing_as_discipline`
- `CFR_cities_first`
- `CFR_rails_first`
- `CFR_factories_first`
- `CFR_contracts_first`
- `CFR_apartment_blocks_for_loyalty`
- `CFR_machine_tools_from_empty_ministries`
- `CFR_no_ruins_without_receipts`
- `CFR_client_city_charters`
- `CFR_the_first_new_district`
- `CFR_a_civilian_factory_in_every_capital`
- `CFR_the_debt_map`
- `CFR_the_state_that_builds`
- `CFR_buy_peace_with_concrete`
- `CFR_the_builder_state_marches_east`
- `CFR_build_the_border_bend_the_border`
- `CFR_factories_as_embassies`
- `CFR_reconstruction_protectorates`
- `CFR_the_workers_keep_the_keys`
- `CFR_the_plan_is_the_law`
- `CFR_pour_the_final_foundation`
- `CFR_nothing_but_foundations`
- `CFR_rebuild_russia_without_moscow`

## Behavior

The CFR tree geometry was compressed into cleaner lanes. The governance fork now sits at `x = 11/15/19/23`, the strategy fork mirrors it at `x = 11/15/19/23`, and the late planner route now runs down a compact lane around `x = 21`. This shortens several long parent-child lines and keeps mutually exclusive rows readable without spreading the tree too far.

`CFR_the_plan_is_the_law` no longer gives only a small mandate bump and popularity. It now calls `soviet_collapse_apply_cfr_focus_plan_is_law`, which:

- raises construction mandates
- advances site registry, contract network, and rebuild network depth
- keeps the consolidated Construction Mandates idea available without adding a new spirit
- rebuilds every controlled core with civilian industry and infrastructure
- adds a supply hub
- increases Soviet foreign-pressure response if the collapse system is active
- adds construction-focused AI strategy pressure

## Localisation

Added:

- `soviet_collapse_apply_cfr_focus_plan_is_law_tt`

## Remaining Risks

This is one CFR tranche, not a full Soviet Collapse focus-tree completion. Remaining broad issues include OGB/MFR/custom-splinter layout, Ukraine and Belarus polish, shallow helper-only rewards in many trees, and wider route-aware AI work.

## Validation

Validation is parent-owned after this handoff.
