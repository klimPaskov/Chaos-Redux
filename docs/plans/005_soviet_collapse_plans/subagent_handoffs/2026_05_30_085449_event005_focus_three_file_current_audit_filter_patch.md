# Event 005 Soviet Collapse Focus Three-File Audit And Filter Patch

Date: 2026-05-30 08:54 UTC
Role: Chaos Redux focus tree subagent

Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Related files inspected for narrow integration context:
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- Event 005 English localisation files.

Constraints honored:
- No `gfx/flags` files, flag sprite assets, or flag artwork were inspected or edited.
- No commit was made.
- Existing dirty worktree edits were preserved. The `git diff` for `005_soviet_collapse_republics.txt` includes pre-existing changes outside this subagent patch.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.
- Vanilla focus precedent: `~/projects/Hearts of Iron IV/common/national_focus/generic.txt` for prerequisites, mutual exclusions, filters, completion rewards, and AI blocks.

## Audit Coverage

All `focus = { id = ... }` blocks in the three scoped files were parsed from the current worktree: 1,634 focuses across 37 focus trees. Exact patched focus ids are listed under "Small Patch Applied". The audited focus id set is every focus id in the route coverage table's trees.

Coverage checks:
- Missing `ai_will_do`: 0.
- Missing `icon =`: 0.
- Missing focus title localisation key: 0.
- Missing focus description localisation key: 0.
- Empty/missing `search_filters`: 0.
- Duplicate same direct `add_ideas` or same direct equipment stockpile tuple inside one focus: 0.
- Direct `create_unit` and direct `division_template` calls in these focus rewards: 0.

## Route Coverage Table

| Required route or tree | Implemented tree | Focuses | Hooks | Claims/war/core | Status | Notes |
|---|---|---:|---:|---:|---|---|
| Ukraine major republic politics, industry, military, diplomacy, expansion | `soviet_collapse_ukraine_focus_tree` | 83 | 7 | 0 | Partial | Broad branches exist; major endpoints still lean on helpers/stat rewards. Black Sea and League branches have hooks but need stronger postwar/territorial results. |
| Generic breakaway republics | `soviet_collapse_breakaway_focus_tree` | 36 | 0 | 0 | Simplified | Shared survival shell, not enough for any long-lived major breakaway. |
| Internal republics | `soviet_collapse_internal_republic_focus_tree` | 62 | 0 | 1 | Partial | Large enough, but mostly helper/building rewards; Crimea settlement claim filter was patched. |
| Baltic republics | `soviet_collapse_baltic_focus_tree` | 42 | 0 | 0 | Simplified | Restoration/ports/foreign protection names exist, but no direct decisions or expansion hooks by scan. |
| Caucasus republics | `soviet_collapse_caucasus_focus_tree` | 40 | 2 | 0 | Partial | Oil/mountain identity exists; needs neighbor conflict, postwar, and integration depth. |
| Central Asian republics | `soviet_collapse_central_asia_focus_tree` | 45 | 3 | 1 | Partial | Steppe/federation surface exists; Khwarazm claim focus filter was patched. |
| Moldova | `soviet_collapse_moldova_focus_tree` | 48 | 0 | 0 | Simplified | Bridge, river, union, and Ukrainian corridor themes lack direct decision/war/core hooks. |
| Belarus | `soviet_collapse_belarus_focus_tree` | 53 | 3 | 0 | Partial | Rail/forest/corridor identity exists; needs unit/template, forest-war, and League logistics mechanics. |
| Kazakhstan | `soviet_collapse_kazakhstan_focus_tree` | 92 | 4 | 0 | Partial | Broadest republic route set; resource/federation/Alash routes need more state-targeted mechanics and route AI. |
| Free Territory | `FTH_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Full-size but disconnected from decision and expansion surfaces. |
| Pale Railway Authority | `PRA_soviet_collapse_focus_tree` | 22 | 12 | 1 | Shallow but improved | Strong rail decision hooks exist; still too short for an OP chaos-country standard. |
| Tunguska Star Committee | `TSC_soviet_collapse_focus_tree` | 18 | 0 | 1 | Shallow | Needs a full identity mechanic, not only a compact crisis ladder. |
| Red Martyrs Cult | `RMC_soviet_collapse_focus_tree` | 18 | 0 | 3 | Shallow | Aggression exists but lacks decision loop, units, and route depth. |
| Dead Soldiers' Congress | `DSC_soviet_collapse_focus_tree` | 18 | 5 | 6 | Shallow but dangerous | Best compact chaos package for direct war/core hooks, but still too small and equipment-heavy. |
| Northern Revenant Fleet | `NRF_soviet_collapse_focus_tree` | 18 | 5 | 3 | Shallow but dangerous | Needs naval war, port control, fleets, and sea-lane mechanics. |
| Iron Commissariat of the Dead | `ICD_soviet_collapse_focus_tree` | 18 | 0 | 3 | Shallow | Death-state idea exists; no decision loop or direct unit system. |
| Basmachi Confederation | `BSC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Full-size template tree with no direct decision/war/core hooks. |
| Turkestan National Council | `TNC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Full-size template tree with no direct decision/war/core hooks. |
| Alash Restoration Authority | `ALA_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Identity exists; route payoffs remain generic. |
| Black Banner Host | `BBH_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Stronger lore tone, but no direct decision/war/core hooks. |
| Kronstadt Council | `KRS_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Naval/port titles need port-control and fleet mechanics. |
| Union Defense Committee | `UDC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Military theme exists but lacks expansion and decision integration. |
| Security Directorate Zone | `SDZ_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Security-state route lacks decision, repression, intelligence, or war hooks in focuses. |
| Green Army Congress | `GAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Peasant/partisan identity needs village, supply, and territorial mechanics. |
| Don Host Circle | `DHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Host route needs cavalry, river, grain, and expansion payoffs. |
| Kuban Host Council | `KHC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Host route needs cavalry, mountain, and corridor payoffs. |
| Far Eastern Republic Revival | `FEV_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Port, Amur, and foreign route labels lack direct mechanics. |
| Siberian Zemstvo Authority | `SZA_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Siberian rail/governance themes need regional missions and expansion hooks. |
| Ural Workers Directorate | `UWD_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Industrial theme is reward-heavy: 18 building focuses and 11 equipment focuses. |
| Mountain Republic of the Caucasus | `MRC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Pass/confederation identity exists; lacks territorial and decision hooks. |
| Idel-Ural League | `IUL_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Volga/Ural identity lacks direct formable/war/core/decision integration. |
| Birobidzhan Autonomous Commune | `BAC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Amur/relief identity lacks direct route mechanics. |
| Arctic Naval Directorate | `ARD_soviet_collapse_focus_tree` | 47 | 3 | 0 | Partial | Has naval identity and some decisions, but no direct claim/war/core hooks. |
| Northern Lights Commune | `NLC_soviet_collapse_focus_tree` | 47 | 0 | 0 | Simplified | Polar/science identity lacks decision, expansion, or OP mechanics. |
| Construction Factory Republic | `CFR_soviet_collapse_focus_tree` | 47 | 5 | 2 | Partial | Stronger governance/industry structure; still has convergence risk and repeated construction rewards. |
| Old Great Bulgaria | `OGB_soviet_collapse_focus_tree` | 23 | 2 | 4 | Shallow but dangerous | Has Volga claims/cores/war hooks, but too short and not enough restoration-state politics. |
| Munitions Factory Republic | `MFR_soviet_collapse_focus_tree` | 58 | 3 | 1 | Partial | Best factory successor surface; still needs more route-specialized end states. |

## Repeated Rewards And Shallow Content

Direct reward counts by file:

| File | Focuses | Equipment stockpile calls | Building calls | Decision hooks | War/claim/core calls | Direct AI strategy calls |
|---|---:|---:|---:|---:|---:|---:|
| `005_soviet_collapse_republics.txt` | 501 | 31 | 170 | 35 | 8 | 2 |
| `005_soviet_collapse_custom_splinters.txt` | 1005 | 207 | 391 | 25 | 17 | 24 |
| `005_soviet_collapse_factory_successors.txt` | 128 | 3 | 24 plus 6 offsite | 11 | 11 | 22 |

Missing or simplified content:
- Direct duplicate idea spam is gone: 0 direct `add_ideas`, 0 direct `swap_ideas`, 0 direct `add_timed_idea` in the three focus files. There are 8 direct `remove_ideas` cleanup calls, all route cleanup rather than spam.
- The custom splinter file remains the main shallow-reward risk: 1,005 focuses, 207 equipment stockpile calls, and 391 building calls.
- The common 47-focus splinter family often has branches named for industry, diplomacy, war plans, hidden doctrine, and endgame, but 17 of those trees have no direct decision hooks and no direct claim/war/core calls.
- No focus reward directly creates units or defines templates in these three files. Existing helper calls may spawn units, but the focus surface still under-delivers the requested "strong unit spawns" standard for many chaos countries.
- Ukraine, Belarus, Kazakhstan, CFR, and MFR are structurally large enough to preserve, but need focused route payoff work rather than more generic reward insertion.
- PRA, TSC, RMC, DSC, NRF, ICD, and OGB require broad route-family expansion if they are meant to be full playable chaos-country trees. A safe local patch cannot make 18 to 23-focus crisis ladders meet the requested standard.

## Pathline And Mutual-Exclusion Risks

The main pathline risk is OR prerequisites that join mutually exclusive parents. This is valid syntax, but it can draw visible pathlines through incompatible choices or make route convergence look accidental.

High-priority examples:

| Focus | File line | Mutually exclusive parents joined | Risk |
|---|---:|---|---|
| `ukr_soviet_collapse_free_soil_compromise` | `005_soviet_collapse_republics.txt:802` | `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire` | Democratic/Black Banner convergence is visually and mechanically ambiguous. |
| `ukr_soviet_collapse_last_harvest_plan` | `005_soviet_collapse_republics.txt:2243` | `ukr_soviet_collapse_the_commune_war`, `ukr_soviet_collapse_the_double_republic` | Late incompatible bread-state outcomes converge. |
| `central_asia_soviet_collapse_the_south_survives_together` | `005_soviet_collapse_republics.txt:7435` | `central_asia_soviet_collapse_loose_southern_pact`, `central_asia_soviet_collapse_federation_state` | Pact/federation distinction blurs. |
| `central_asia_soviet_collapse_the_basmachi_amnesty_ledger` | `005_soviet_collapse_republics.txt:7485` | `central_asia_soviet_collapse_negotiate_with_the_mountain_bands`, `central_asia_soviet_collapse_clear_the_mountain_bands` | Negotiation/clearance choice rejoins too quickly. |
| `PRA_passport_of_the_moving_state` | `005_soviet_collapse_custom_splinters.txt:1563` | `PRA_the_board_overrules_ministers`, `PRA_armored_train_directorate` | Board/directorate route line convergence remains readable risk. |
| `DSC_field_hospital_memorials`, `DSC_maps_of_lost_armies` | `005_soviet_collapse_custom_splinters.txt:2996`, `3083` | `DSC_revenant_staff_line`, `DSC_witness_officers` | Incompatible identity fork converges immediately. |
| `NRF_icebound_marine_guard`, `NRF_maps_of_sunken_routes` | `005_soviet_collapse_custom_splinters.txt:3569`, `3656` | `NRF_revenant_admiralty`, `NRF_living_harbor_committees` | Living/revenant naval identities converge immediately. |
| Repeated `*_industry_plan` pattern | Custom splinter file | `*_radical_turn`, `*_settlement` | Template convergence repeats across many 47-focus trees. |
| `CFR_apartment_blocks_for_loyalty` | `005_soviet_collapse_factory_successors.txt:517` | `CFR_cities_first`, `CFR_rails_first` | Strategy choices are mutually exclusive but rejoin through one visible child. |

Recommended fix pattern: split route-specific children where gameplay differs, move neutral children before the fork, or keep convergence but reflow the layout so pathlines do not cross incompatible route space.

## Icon Coverage Table

This audit checked focus icon assignment strings only. It did not inspect `.gfx` definitions or any flag assets.

| File | Focuses missing icon assignment | Repeated icon groups | Top repeated icon ids |
|---|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 0 | 22 | `GFX_focus_soviet_collapse_guard_the_radio_stations` x4, `GFX_ukr_soviet_collapse_democratic` x4, `GFX_focus_soviet_collapse_no_masters_in_kyiv_or_moscow` x4, `GFX_focus_soviet_collapse_steppe_supply_congress` x4 |
| `005_soviet_collapse_custom_splinters.txt` | 0 | 99 | `GFX_focus_FEV_diplomatic_plan` x4, `GFX_focus_SZA_diplomatic_plan` x4, `GFX_focus_MRC_civil_rule` x4, `GFX_focus_MRC_foreign` x4, `GFX_focus_IUL_supply` x4, `GFX_focus_IUL_war_plan` x4 |
| `005_soviet_collapse_factory_successors.txt` | 0 | 11 | `GFX_focus_CFR_municipal_board_elections` x3, `GFX_focus_CFR_concrete_republic` x3, `GFX_focus_CFR_the_builder_state` x3, `GFX_focus_CFR_civilian_hegemony_project` x3 |

Icon conclusion: there are no missing icon assignments, but repeated icon families reinforce the generic-template feel. Icon asset work should wait until route roles are stable and must not touch flags without explicit scope.

## Localisation And Reward Mismatch List

Localisation coverage:
- Missing focus title keys: 0.
- Missing focus description keys: 0.

Content-level mismatch risks:
- `internal_soviet_collapse_ukraine_settlement_commission` at `005_soviet_collapse_republics.txt:3983` has a real claim reward. Search filter now matches this.
- `central_asia_soviet_collapse_khwarazm_restoration_debate` at `005_soviet_collapse_republics.txt:7534` has real conditional claim rewards. Search filter now matches this.
- `soviet_collapse_baltic_focus_tree` and `soviet_collapse_moldova_focus_tree` titles imply restoration, ports, river routes, union questions, and corridors, but the scan found 0 direct decision hooks and 0 direct war/claim/core hooks.
- `KRS`, `ARD`, and `NRF` use port/naval language; only `NRF` has direct war/claim hooks, while `KRS` and `ARD` still need direct port-control, fleet, sea-lane, or postwar mechanics.
- `UWD` uses worker/industrial state language but remains heavy on direct construction/equipment rewards rather than a production or arsenal decision loop.
- `NLC` uses polar/science route language but has 0 direct decision hooks and 0 direct expansion hooks.

## AI Behavior Gaps

- Every audited focus has `ai_will_do`, so there are no missing AI blocks.
- Route-aware behavior is still thin in effect terms. Direct `add_ai_strategy` calls appear in only 1 republic focus, 12 custom splinter focuses, and 8 factory successor focuses.
- Chaos-country aggression is uneven. `DSC`, `NRF`, and `OGB` have direct aggressive hooks; most 47-focus custom splinters have no direct `add_ai_strategy`, no direct wargoal/claim/core, and no direct decision hooks.
- Ukraine, Belarus, and Kazakhstan route selectors have focus weights, but the follow-through after route selection should drive expansion, defense, League behavior, and foreign alignment through persistent strategies or route-specific decisions.
- Naval actors need AI strategies for dockyards, convoy/fleet behavior, coastal defense, and port targets.

## Small Patch Applied

Changed gameplay file:
- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus ids:
- `internal_soviet_collapse_ukraine_settlement_commission`
- `central_asia_soviet_collapse_khwarazm_restoration_debate`

Before:
- Both focuses directly granted claims but only had political/stability search filters.

After:
- Added `FOCUS_FILTER_ANNEXATION` to both focus `search_filters`.
- No prerequisites, rewards, AI weights, icons, localisation, route locks, or layout coordinates changed by this subagent patch.

Localisation keys changed:
- None.

Icon ids changed:
- None.

Route behavior before and after:
- Gameplay behavior is unchanged. This is a UI search/filter alignment patch only.

Why this was safe and bounded:
- Both focuses already had direct `add_claim_by` or `add_state_claim` effects. The patch only makes the focus search menu reflect existing expansion rewards.

## High-Priority Fixes First

1. Expand shallow chaos successors before polishing generic rewards: `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, and `OGB`.
2. Give every 47-focus custom splinter at least one real expansion or postwar loop: claims/war goals, integration, units/templates, AI target strategy, and decision hooks.
3. Rework zero-hook regional republic trees: `soviet_collapse_baltic_focus_tree`, `soviet_collapse_moldova_focus_tree`, and `soviet_collapse_breakaway_focus_tree`.
4. Convert repeated equipment/building ladders in `005_soviet_collapse_custom_splinters.txt` into route-specific decision loops and OP chaos mechanics.
5. Resolve OR-joins through mutually exclusive parents before visual completion claims.
6. Deepen Ukraine, Belarus, Kazakhstan, CFR, and MFR route endpoints with leader/advisor/law/cosmetic hooks where available, plus stronger route AI and postwar handling.

## Validation Run

Commands run and results:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Result: passed; no whitespace errors.
- `rg -n '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Result: no matches; exit code 1 from no results.
- Brace balance script over the three focus files:
  - `005_soviet_collapse_republics.txt`: final depth 0, minimum depth 0.
  - `005_soviet_collapse_custom_splinters.txt`: final depth 0, minimum depth 0.
  - `005_soviet_collapse_factory_successors.txt`: final depth 0, minimum depth 0.
- Post-patch expansion-filter scan:
  - Result: 0 focus rewards with direct claim/war/core effects missing `FOCUS_FILTER_ANNEXATION`.

Skipped validation:
- No in-game validation was run.
- No `.gfx` definition validation was run because the user constrained the task away from flag/gfx work and primary scope was focus/localisation/script integration.
- No broad decision-system validation was run because the only gameplay patch was focus search filters.

## Remaining Route Risks

The focus-tree rework is not complete. The main remaining risks are broad route-design gaps, not local syntax errors:

- High-chaos trees are not consistently OP or expansionist enough.
- Most 47-focus custom splinters still read as generated route templates with repeated reward cadence.
- Direct unit/template creation is absent in the three focus files.
- Many branches remain disconnected from the existing decision categories.
- Route-aware AI exists at focus-pick level, but not enough persistent campaign strategy follows from route endpoints.
- Icon assignments exist, but repeated icon families are too common for final distinct identity.
- Several OR joins through mutually exclusive parents need layout or route-logic decisions from the parent rework.

Plan handoff path:
- This file: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_30_085449_event005_focus_three_file_current_audit_filter_patch.md`
