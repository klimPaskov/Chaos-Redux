# Event005 Focus Tree Fresh Full Audit - CFR Mutual-Exclusion Patch

Date: 2026-06-04

Role: `chaosx_focus_tree_auditor`

Scope:
- Audited current Event005 Soviet Collapse focus trees in:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Used repo skills: `hoi4-focus-trees`, `chaos-redux-events`, `chaos-redux-subagents`.
- Consulted required offline Paradox wiki pages plus vanilla HOI4 documentation and vanilla focus examples before opening/editing Chaos Redux files.
- Parent constraint honored: no flag files, flag assets, `.dds`, `.tga`, sprite files, or flag-related paths were edited.
- No commit made.

## Changed Files

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Added missing visual `mutually_exclusive` links to two CFR four-way choice groups so the tree display matches the already-existing hidden `available` route locks.
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_fresh_full_audit_cfr_mutex_patch.md`
  - This handoff.

The focus file already contained unrelated uncommitted parent changes before this audit. This patch only added `mutually_exclusive` references for the IDs listed below.

## Audit Counts

- Focus trees audited: 41
- Focus count: 1,698
  - `005_soviet_collapse_republics.txt`: 501
  - `005_soviet_collapse_custom_splinters.txt`: 1,005
  - `005_soviet_collapse_factory_successors.txt`: 128
  - `005_soviet_collapse_ancient_restorations.txt`: 64
- Duplicate focus IDs: 0
- Direct `add_ideas` rewards: 0
- Direct `add_ideas` duplicate names: 0
- Repeated idea/update helper rewards: 8 call sites using 1 helper name, `soviet_collapse_update_pra_authority_idea`
- Reward-thin focuses: 0 by strict scan: no empty `completion_reward`, and no reward reduced only to flags/tooltips/variables.
- Hard pathline/prerequisite/mutual-exclusion problems after patch: 0
  - Missing prerequisites: 0
  - Missing mutual-exclusion targets: 0
  - Non-reciprocal direct mutual exclusions: 0
- Visible route-lock mismatch candidates after patch: 31
  - These are not hard syntax problems. They are focuses where `available` hides completion based on other focuses that are not fully represented by visible `mutually_exclusive` lines. Some are probably intentional dependency/anti-duplicate guards and need parent-level design judgement before broad patching.
- Filter mismatch candidates: 220 strict direct-effect candidates
  - `republics`: 51
  - `custom_splinters`: 143
  - `factory_successors`: 3
  - `ancient_restorations`: 23
  - This count is intentionally conservative and direct-effect based. It flags focuses whose direct rewards include buildings/resources/manpower/XP/research/territorial effects without the matching filter. Many are mixed primary/secondary rewards, not automatically defects.
- Shallow/no-depth branches: 0 hard no-depth trees
  - Minimum current tree size is 16 focuses for each ancient-restoration tree, with max depth 10.
  - The compact TSC/RMC/DSC/NRF/ICD trees are 18 focuses each with max depth 8.
  - Broad depth improvement remains possible, but there is no current one- or two-focus placeholder tree in the audited files.

## Exact Focus IDs Patched

Patched CFR governance choice group:
- `CFR_elect_the_site_committees`
- `CFR_publish_the_planners_charter`
- `CFR_invite_the_foreign_contract_board`
- `CFR_the_concrete_committee`

Patched CFR construction strategy choice group:
- `CFR_cities_first`
- `CFR_rails_first`
- `CFR_factories_first`
- `CFR_contracts_first`

Before behavior:
- Each group was mechanically locked as a four-way choice through hidden `available` checks.
- The focus tree only showed one pair of mutual-exclusion links in each group, making the visible route geometry misleading.

After behavior:
- Every focus in each group now mutually excludes the other three visible alternatives.
- No rewards, flags, AI weights, prerequisites, localisation, assets, or helper calls changed.

## Exact Focus IDs Flagged

Repeated idea/update helper call sites, for parent review only:
- `PRA_the_timetable_declares_authority`
- `PRA_the_board_overrules_ministers`
- `PRA_armored_train_directorate`
- `PRA_passport_of_the_moving_state`
- `PRA_league_transit_bargain`
- `PRA_rails_over_capitals`
- `PRA_flags_on_every_station`
- `PRA_the_pale_line_endures`

Assessment: these are not direct duplicate `add_ideas` rewards. They follow authority-variable changes or route endpoints and appear to be intended staged updater calls. Parent should still verify the helper is idempotent and tier-safe.

Remaining visible route-lock mismatch candidates:
- `central_asia_soviet_collapse_local_republic_council`
- `central_asia_soviet_collapse_negotiate_with_the_mountain_bands`
- `central_asia_soviet_collapse_clear_the_mountain_bands`
- `moldova_soviet_collapse_alliance_not_union`
- `moldova_soviet_collapse_conditional_union`
- `kaz_soviet_collapse_domestic_resource_state`
- `kaz_soviet_collapse_league_resource_pool`
- `kaz_soviet_collapse_foreign_technical_missions`
- `kaz_soviet_collapse_steppe_federation_charter`
- `PRA_armored_train_directorate`
- `TSC_observatory_state`
- `RMC_republic_of_witnesses`
- `DSC_republic_of_roll_calls`
- `NRF_port_republic_of_the_living`
- `ICD_citizens_after_death`
- `BSC_settlement`
- `TNC_settlement`
- `ALA_settlement`
- `BBH_settlement`
- `UDC_settlement`
- `SDZ_settlement`
- `GAC_settlement`
- `DHC_settlement`
- `KHC_settlement`
- `FEV_settlement`
- `SZA_settlement`
- `UWD_settlement`
- `MRC_settlement`
- `IUL_settlement`
- `OGB_treat_with_idel_ural`
- `OGB_the_volga_cannot_have_two_seals`

Assessment: do not bulk-patch these without parent review. Several hidden locks refer to upstream gate focuses rather than sibling route alternatives, so adding visible mutual exclusions mechanically may be correct in some places and visually misleading in others.

## Remaining Parent-Level Gaps

- Filter normalization: 220 direct-effect filter candidates remain. This should be a deliberate parent pass, not a blind append-all-filters patch, because many focuses intentionally expose their primary role while carrying secondary reward effects.
- Generic helper reuse is still heavy across republic/custom-splinter trees. That is mostly intentional, but deeper country-specific mechanics could improve some 47-focus template families by adding more route-specific decisions, postwar handling, and AI strategy consequences.
- PRA authority idea progression should be verified from the helper implementation side. The focus surface has 8 updater call sites but no direct idea spam.
- Some visible route-lock candidates need design classification: draw them if they are true sibling choices; leave them hidden if they are dependency, endpoint, or anti-duplicate guards.

## Validation Run

Passed:
- Brace balance on all four scoped focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`: balance 0, min depth 0
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`: balance 0, min depth 0
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`: balance 0, min depth 0
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: balance 0, min depth 0
- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_fresh_full_audit_cfr_mutex_patch.md`
- Unsupported operator scan on all four scoped focus files: no `<=` or `>=` matches.
- No flag-related diff check: no matches for `gfx/flags`, flag `.gfx`, `.tga`, or flag `.dds` paths in `git diff --name-only`.

Skipped:
- No game launch or live in-game verification; this is a subagent audit handoff and parent owns final integration validation.
