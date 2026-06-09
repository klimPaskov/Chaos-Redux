# Event005 Soviet Collapse Focus Tree Audit Handoff

Subagent role: `chaosx_focus_tree_auditor`

Skills used:

- `hoi4-focus-trees`
- `chaos-redux-events`

References consulted before reading or patching Chaos Redux files:

- Offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus precedent for focus rewards, `swap_ideas`, `add_timed_idea`, `mutually_exclusive`, `prerequisite`, `relative_position_id`, and `ai_will_do`.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`

No gfx, flags, or interface flag files were touched.

## Narrow Patches Applied

### Ukraine pathline cleanup

- `ukr_soviet_collapse_re_register_the_party`
  - Changed `y = 10` to `y = 11`.
  - Reason: this aligns the mutually exclusive socialist route pair with `ukr_soviet_collapse_purge_moscow_loyalists` at `y = 11`, reducing a diagonal mutex/pathline hazard.

- `ukr_soviet_collapse_rural_deputy_bloc`
  - Changed `x = 14` to `x = 10`.
  - Reason: this focus was sitting between the mutually exclusive military-route siblings `ukr_soviet_collapse_mixed_emergency_cabinet` at `(12,8)` and `ukr_soviet_collapse_army_supremacy` at `(15,8)`.

### Belarus pathline cleanup

- `blr_soviet_collapse_prepare_league_freight_tables`
  - Changed coordinates from `(22,11)` to `(18,12)`.
  - Reason: this focus was sitting between mutually exclusive siblings `blr_soviet_collapse_regular_forest_brigades` at `(21,11)` and `blr_soviet_collapse_decentralized_detachments` at `(27,11)`.

## Idea Spam Audit

Direct focus-file scan of the four requested files found no direct focus reward calls to:

- `add_ideas`
- `add_timed_idea`
- `swap_ideas`

Transitive helper scan found five focus-visible helper paths that can reach `add_ideas`:

- `PRA_the_timetable_declares_authority` -> `soviet_collapse_update_pra_authority_idea`
- `PRA_armored_train_directorate` -> `soviet_collapse_update_pra_authority_idea`
- `PRA_passport_of_the_moving_state` -> `soviet_collapse_update_pra_authority_idea`
- `PRA_league_transit_bargain` -> `soviet_collapse_update_pra_authority_idea`
- `CFR_pour_the_final_foundation` -> `soviet_collapse_apply_cfr_raise_factory_city_belt`

These were not patched:

- `soviet_collapse_update_pra_authority_idea` clears alternate PRA authority spirits and guards each `add_ideas` with `NOT = { has_idea = ... }`, so it behaves as an authority-state replacement/update, not unconditional idea spam.
- `soviet_collapse_apply_cfr_raise_factory_city_belt` only adds `cfr_construction_mandates` behind `NOT = { has_idea = cfr_construction_mandates }`.

## Focus Count Snapshot

Requested files contain 1,269 focus blocks across 41 trees:

- Republics: Ukraine 83, generic breakaway 36, internal republic 62, Baltic 42, Caucasus 40, Central Asia 45, Moldova 48, Belarus 53, Kazakhstan 92.
- Custom splinters: FTH 47, PRA 22, TSC/RMC/DSC/NRF/ICD 18 each, and BSC/TNC/ALA/BBH/KRS/UDC/SDZ/GAC/DHC/KHC/FEV/SZA/UWD/MRC/IUL/BAC/ARD/NLC 47 each.
- Factory successors: CFR 47, OGB 23, MFR 58.
- Ancient restorations: KZR/SOG/KHW/ALN 16 each.

## Remaining High-Priority Findings

### Layout and pathlines

- `CFR_soviet_collapse_focus_tree` still has the worst remaining mutex layout risk:
  - Governance fork around `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, and `CFR_the_concrete_committee` is staggered and has route choices between other mutually exclusive choice lines.
  - Build-priority fork around `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first` is staggered with several nodes between route choices.
- `soviet_collapse_moldova_focus_tree` has route choices and support nodes interleaved around `moldova_soviet_collapse_moldova_route_fork` and `moldova_soviet_collapse_union_with_romania_question`.
- `soviet_collapse_central_asia_focus_tree` has multi-route choices around `central_asia_soviet_collapse_southern_route_fork` with federation and Basmachi nodes sitting inside the route-choice span.
- `soviet_collapse_kazakhstan_focus_tree` has route-choice rows with mismatched parents and interleaved industrial nodes around the Alash/socialist/resource fork, resource concessions, and steppe federation/lone-state fork.
- `soviet_collapse_baltic_focus_tree` has four route choices around `baltic_soviet_collapse_the_legal_state_or_the_front_state` split across y-levels with other route choices between line spans.

### Reward depth

- The four focus files no longer show direct idea-spam rewards, but many focus rewards are still flat stat packages without a clear mechanic unlock. Highest-priority examples for rewrite tranches:
  - Ukraine opening/military nodes: `ukr_soviet_collapse_emergency_rada`, `ukr_soviet_collapse_first_republican_line`, `ukr_soviet_collapse_moscows_officers_in_our_barracks`, `ukr_soviet_collapse_black_sea_defense_staff`, `ukr_soviet_collapse_ports_need_soldiers`.
  - Belarus rail/forest nodes: `blr_soviet_collapse_seal_the_minsk_junction`, `blr_soviet_collapse_railway_guard_regiments`, `blr_soviet_collapse_village_warning_bells`.
  - Kazakhstan nodes: `kaz_soviet_collapse_alma_ata_emergency_congress`, `kaz_soviet_collapse_oil_field_protection_orders`, `kaz_soviet_collapse_the_steppe_arsenal`, `kaz_soviet_collapse_aul_horse_registers`, `kaz_soviet_collapse_army_of_the_open_horizon`.
  - OGB remains shallow relative to other chaos successors at 23 focuses, with many flat stability/political power route rewards.
  - Ancient restoration trees are compact at 16 focuses each and still need stronger OP identity mechanics, especially for symbolic/endgame routes.

### Branch depth and identity

- Ukraine and Belarus are much deeper than a generic placeholder, but their layouts still feel ugly because route choices, support nodes, and follow-up branch nodes overlap visually. They need a layout tranche, not a broad content rewrite in a subagent patch.
- OGB, PRA, and the 18-focus extreme chaos trees are the weakest compared to the 47-focus custom splinter standard. They should receive bespoke OP identity mechanics before final completion claims.
- Ancient restoration trees need a second pass for political/industry/expansion separation. They currently have a compact historic-restoration pattern but not enough late-game identity compared to larger high-chaos countries.

## Recommended Rewrite Plan

1. Run a dedicated CFR layout tranche:
   - Put governance choices on a shared y-row with no child/support nodes between them.
   - Put build-priority choices on a shared y-row and move `machine_tools`, `client_city_charters`, and follow-ups below their selected route.
2. Run a Moldova/Central Asia/Kazakhstan layout tranche:
   - Split route-choice rows from support/mechanic rows.
   - Keep mutual-exclusion siblings horizontally clean and same-y where possible.
3. Run an OGB/PRA/extreme-chaos depth tranche:
   - Add 3-6 country-specific mechanic focuses per weak tree rather than repeating flat stats.
   - Prefer decisions, state targeting, AI strategies, claims/cores, timed missions, or special units over another national spirit.
4. Run an ancient-restoration OP identity tranche:
   - Give KZR/SOG/KHW/ALN unique late-game identity mechanics and expansion consequences.
   - Keep symbolic and expansionist branches mechanically distinct.
5. Re-run the focus-tree auditor after those tranches and then use a localisation audit for all new or changed player-facing text.

## Validation

- Direct focus reward scan found no `add_ideas`, `add_timed_idea`, or `swap_ideas` in:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Transitive helper scan reviewed focus-visible idea grants and found them guarded/replacement-style.
- Coordinate verification after patch:
  - `ukr_soviet_collapse_re_register_the_party` is now `(20,11)`.
  - `ukr_soviet_collapse_purge_moscow_loyalists` remains `(19,11)`.
  - `ukr_soviet_collapse_rural_deputy_bloc` is now `(10,8)`.
  - `blr_soviet_collapse_prepare_league_freight_tables` is now `(18,12)`.
  - `blr_soviet_collapse_regular_forest_brigades` remains `(21,11)`.
  - `blr_soviet_collapse_decentralized_detachments` remains `(27,11)`.

Skipped validation:

- No in-game render test was run.
- No broad syntax validator was run beyond `git diff --check`, because the worktree already contains many unrelated Event005/Event006 modifications.

