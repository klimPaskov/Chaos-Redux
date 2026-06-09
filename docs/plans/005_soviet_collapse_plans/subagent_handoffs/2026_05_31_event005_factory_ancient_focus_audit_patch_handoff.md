# Event005 Factory/Ancient Focus Audit Patch Handoff

Date: 2026-05-31
Subagent scope: `common/national_focus/005_soviet_collapse_factory_successors.txt` and `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Changed Files

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_31_event005_factory_ancient_focus_audit_patch_handoff.md`

No flags or `gfx/flags` files were touched.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| CFR construction/factory identity | `CFR_*` opening spine, governance selector, construction strategy selector, coercive/foreign/worker branches, eastern expansion endgame | Partially improved | Selector mutual exclusions are now visible/currently complete, and one repeated mandate helper stack was removed. CFR still needs an icon pass and deeper distinction among repeated construction icon families. |
| MFR military factory identity | `MFR_*` opening spine, four-way rifle ownership selector, arms production routes, foreign arms market, arsenal endgame | Partially improved | Selector mutual exclusions are now visible/currently complete, and one duplicate rail-authority reward stack was removed. Several MFR helpers still share arms/equipment rhythm by design. |
| OGB ancient/factory successor restoration | `OGB_*` Volga legitimacy, trade, guard, Idel-Ural diplomacy/rivalry, restoration state endgame | Audit only | Current 23-focus shape is playable but still shallow versus the spec's OP chaos-country branch-depth target. No bounded safe patch found without broader route design. |
| KZR ancient restoration | `KZR_*` toll authority, trade/guard, symbolic vs expansionist, charter, endgame | Patched | `KZR_expansionist_steppe_levy` now grants a guarded SOV annexation war goal when legal, matching existing conquest AI. |
| SOG ancient restoration | `SOG_*` city authority, oasis trade/guard, symbolic vs expansionist, charter, endgame | Patched | `SOG_expansionist_merchant_claims` now grants a guarded SOV annexation war goal when legal, matching existing conquest AI. |
| KHW ancient restoration | `KHW_*` water authority, caravan/canal guard, symbolic vs expansionist, charter, endgame | Patched | `KHW_expansionist_water_claims` now grants a guarded SOV annexation war goal when legal, matching existing conquest AI. |
| ALN ancient restoration | `ALN_*` pass authority, Darial road/guard, symbolic vs expansionist, charter, endgame | Patched | `ALN_expansionist_mountain_claims` now grants a guarded SOV annexation war goal when legal, matching existing conquest AI. |

## High-Priority Fixes Made

| Priority | File | Focus ids | Before | After |
| --- | --- | --- | --- | --- |
| High | `005_soviet_collapse_factory_successors.txt` | `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee` | Hidden `available` locks made the four governance routes exclusive, but visible `mutually_exclusive` entries were incomplete. | The current file has visible pairwise mutual exclusions across the four governance choices. |
| High | `005_soviet_collapse_factory_successors.txt` | `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first` | Hidden locks made the four construction strategy choices exclusive, but visible `mutually_exclusive` entries were incomplete. | The current file has visible pairwise mutual exclusions across the four strategy choices. |
| High | `005_soviet_collapse_factory_successors.txt` | `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, `MFR_eternal_arsenal` | Hidden `available` locks made the four MFR route choices exclusive, but visible `mutually_exclusive` entries were incomplete. | The current file has visible pairwise mutual exclusions across the four route choices. |
| High | `005_soviet_collapse_ancient_restorations.txt` | `KZR_expansionist_steppe_levy`, `SOG_expansionist_merchant_claims`, `KHW_expansionist_water_claims`, `ALN_expansionist_mountain_claims` | Expansionist branches granted claims, war support, units/equipment, and hidden conquest AI against SOV, but no direct war goal. | Each expansionist branch now grants a guarded `annex_everything` war goal against SOV if SOV exists, the country is not already at war, has no SOV war goal, and can declare. |
| Medium | `005_soviet_collapse_factory_successors.txt` | `CFR_emergency_cement_accounts` | Called both `soviet_collapse_apply_cfr_focus_mandate_gain` and `soviet_collapse_apply_cfr_focus_public_works`; `public_works` already grants construction mandates and map construction. | Removed the separate mandate helper call to reduce repeated reward spam while keeping the concrete/public-works payoff. |
| Medium | `005_soviet_collapse_factory_successors.txt` | `MFR_armored_train_workshops` | Called `soviet_collapse_apply_mfr_focus_armored_train_workshops` and then `soviet_collapse_apply_focus_rail_authority_reward`; the MFR helper already calls the rail-authority reward. | Removed the duplicate direct rail-authority helper call. |

## Icon Coverage Table

| File | Tree | Focuses | Unique icons | Repeated icon ids |
| --- | --- | ---: | ---: | --- |
| `005_soviet_collapse_factory_successors.txt` | `CFR_soviet_collapse_focus_tree` | 43 | 30 | `GFX_focus_CFR_cement_allocation_boards` (2), `GFX_focus_CFR_reconstruction_contract_state` (2), `GFX_focus_CFR_municipal_board_elections` (3), `GFX_focus_CFR_contract_dependency_web` (2), `GFX_focus_CFR_the_builder_state` (3), `GFX_focus_CFR_housing_before_flags` (2), `GFX_focus_CFR_civilian_hegemony_project` (3), `GFX_focus_CFR_forced_labor_barracks` (2), `GFX_focus_CFR_silent_site_guards` (2), `GFX_focus_CFR_concrete_republic` (2) |
| `005_soviet_collapse_factory_successors.txt` | `OGB_soviet_collapse_focus_tree` | 23 | 23 | None |
| `005_soviet_collapse_factory_successors.txt` | `MFR_soviet_collapse_focus_tree` | 55 | 55 | None |
| `005_soviet_collapse_ancient_restorations.txt` | `KZR_soviet_collapse_ancient_focus_tree` | 16 | 16 | None |
| `005_soviet_collapse_ancient_restorations.txt` | `SOG_soviet_collapse_ancient_focus_tree` | 16 | 16 | None |
| `005_soviet_collapse_ancient_restorations.txt` | `KHW_soviet_collapse_ancient_focus_tree` | 16 | 16 | None |
| `005_soviet_collapse_ancient_restorations.txt` | `ALN_soviet_collapse_ancient_focus_tree` | 16 | 16 | None |

No icon ids were changed because the parent forbade asset/flag work and this subtask did not own `.gfx` edits.

## Missing or Simplified Content

- `OGB_soviet_collapse_focus_tree` remains shallow at 23 focuses. It has real Volga restoration hooks, but not the full political/industry/military/diplomacy/expansion/special OP route depth requested by the user.
- `KZR`, `SOG`, `KHW`, and `ALN` remain compact 16-focus ancient trees. The expansionist selectors now have direct SOV war goals, but broader identity-specific route depth still needs parent-level design.
- `CFR_soviet_collapse_focus_tree` still has repeated icon ids and several focuses with similar construction/factory reward rhythm. Fixing that cleanly needs either new registered icon ids or broader route reward design outside this bounded patch.
- `MFR_soviet_collapse_focus_tree` is deeper and icon-complete, but several helper rewards still revolve around quotas, stockpile equipment, war support, and arms-factory construction. A larger pass should add more distinct production decisions, client-state consequences, or arsenal route mechanics.

## Localisation and Reward Mismatch List

- Missing focus localisation: none found for the two owned focus files in current Event005 localisation.
- Localisation keys changed: none.
- `CFR_emergency_cement_accounts`: reward spam reduced by removing the duplicate mandate helper; the focus still matches cement/public-works construction rewards.
- `MFR_armored_train_workshops`: duplicate rail-authority helper removed; the focus still grants rail authority through `soviet_collapse_apply_mfr_focus_armored_train_workshops`.
- Ancient expansionist focus descriptions should be reviewed by the parent after localisation scope opens, because the rewards now include direct SOV war goals in addition to claims/equipment/AI.

## AI Behavior Gaps

- Ancient expansionist branches already had hidden `conquer` and `antagonize` AI strategies against SOV; this patch aligned their visible reward with that behavior by adding guarded SOV war goals.
- OGB route AI remains relatively compact and should get stronger distinction between compact diplomacy, rival-seal aggression, trade-city restoration, and full restoration-state ambitions.
- CFR and MFR selector AI exists but could still be more route-aware around construction mandate levels, arsenal quotas, foreign appetite, and actual neighbor war state.

## Validation Run

- Brace-depth validation for both owned focus files: passed (`final_depth=0`, no negative depth events).
- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: passed.
- `git diff --name-only -- gfx/flags`: empty output, confirming no flag files under `gfx/flags` are touched.
- Unsupported operator grep for `<=` / `>=` in the two owned focus files: no matches.
- Vanilla/documentation consulted: offline Paradox National focus, core syntax pages, and vanilla `effects_documentation.md` / `triggers_documentation.md` entries for focus loading, construction, claims, cores, war goals, units, and focus tree behavior.

## Skipped Validation

- No HOI4 runtime launch or in-game focus-tree screenshot validation was run in this subagent pass.
- No localisation edits were made, so BOM/localisation write validation was not applicable.
- No `.gfx`, asset, or flag validation was performed beyond confirming `gfx/flags` diff is empty.

## Remaining Route Risks

- This does not complete the user's broad objective by itself. The owned trees still need parent-level route depth work, especially OGB and the four ancient restorations.
- The worktree already contained concurrent parent changes in the two owned files before this patch. This handoff records the current file behavior and the bounded changes made here, but parent review should compare against the active branch state carefully.
- No full route redesign plan was written here because an existing broader follow-up plan already exists at `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
