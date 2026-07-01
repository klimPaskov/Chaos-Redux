# Event 015 Utopia Manifesto Focus Tree Audit Patch Handoff

Subagent: Chaos Redux focus tree subagent
Date: 2026-07-01
Scope: Event 015 `utopia_manifesto` focus-tree audit with narrow patch authority.

## Summary

Audited the Event 015 focus tree and related focus helpers against the current spec, final depth addendum, decision hooks, icon wiring, localisation, and route behavior. I patched one narrow focus-helper bug: the hidden Marked Bounds branch used `allow_branch`, but Event 015 did not refresh the tree layout after ledger/mission state changed. The branch could stay invisible if its opening condition became true after the tree was loaded.

I did not patch localisation, assets, docs, decisions, achievements, or unrelated files.

## Changed Files

| File | Change |
| --- | --- |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | Added `utopia_manifesto_refresh_marked_bounds_branch` and called it from `utopia_manifesto_refresh_ledger`. |

No focus IDs were edited. No localisation keys or icon IDs were changed.

## Changed Identifiers

| Identifier | Type | Before | After |
| --- | --- | --- | --- |
| `utopia_manifesto_refresh_ledger` | scripted effect | Refreshed ledger display, threshold flags, route AI weights, and achievements. | Also checks whether Marked Bounds should become visible and dirties the focus-tree layout once. |
| `utopia_manifesto_refresh_marked_bounds_branch` | scripted effect | Missing. | If `utopia_manifesto_focus_tree_loaded` is set, `utopia_manifesto_can_open_marked_bounds = yes`, and `utopia_manifesto_marked_bounds_layout_revealed` is not set, sets that flag and runs `mark_focus_tree_layout_dirty = yes`. |
| `utopia_manifesto_marked_bounds_layout_revealed` | country flag | Missing. | New internal guard flag preventing repeated layout dirty calls. |

## Route Behavior Before And After

| Route surface | Before | After |
| --- | --- | --- |
| Hidden Marked Bounds entry: `utopia_marked_bounds_clause` | The focus uses `allow_branch = { utopia_manifesto_can_open_marked_bounds = yes }`. Per the offline wiki, `allow_branch` is checked when the tree first loads unless `mark_focus_tree_layout_dirty` is run. If Need/Overreach/Suspicion/arbitration failure happened later, the route could remain hidden. | Ledger-changing focus rewards and decision/mission helpers now flow through `utopia_manifesto_refresh_ledger`, which refreshes the layout once Marked Bounds becomes valid after the tree is loaded. |
| Normal Marked Bounds reward behavior | No direct change. Completing `utopia_marked_bounds_clause` still sets the Marked Bounds route and adds surveyors. | Same. |
| Other routes | No direct change. | Same. |

Remaining limitation: if the only opener is a later global Chaos Meter rise and Event 015 does not run any ledger refresh afterward, the branch may not refresh until the next Event 015 ledger-changing action. This is a residual cross-system/on-action risk outside the permitted patch surface.

## Route Coverage Table

| Required route/branch | Status | Key focus IDs / files | Notes |
| --- | --- | --- | --- |
| Opening trunk | Implemented | `utopia_open_the_manifesto` through `utopia_four_readings` in `common/national_focus/015_utopia_manifesto_focus_tree.txt` | Non-linear setup with ledger, stores, useful arts, Need, boundaries, route choice. |
| Living Humanism | Implemented | `utopia_living_humanism`, `utopia_councils_before_ministers`, `utopia_six_hour_country`, `utopia_free_sick_tables`, `utopia_consent_assemblies`, `utopia_mercy_in_the_registers`, `utopia_renounce_the_idle_clause`, `utopia_living_commonwealth` | Route anchor is mutually exclusive with the other three normal interpretations and uses route-aware AI. |
| Common Store State | Implemented | `utopia_common_store_state`, `utopia_grain_without_owners`, `utopia_standard_measures`, `utopia_train_of_stores`, `utopia_surplus_without_gold`, `utopia_central_auditors`, `utopia_crisis_rations`, `utopia_store_state` | Surplus/store route with bureaucracy/auditor tradeoffs. |
| Guild Commonwealth | Implemented | `utopia_guild_commonwealth`, `utopia_congress_of_masters`, `utopia_apprentice_lots`, `utopia_second_trade_law`, `utopia_workshop_councils`, `utopia_engineer_guilds`, `utopia_common_patents`, `utopia_guild_charter` | Vocation route with craft militia/engineer rewards. |
| Island Discipline | Implemented | `utopia_island_discipline`, `utopia_count_the_harbors`, `utopia_convoy_store`, `utopia_watch_the_sea_roads`, `utopia_ring_councils`, `utopia_shore_engineers`, `utopia_lighthouse_couriers`, `utopia_island_compact` | Coastal/island-gated route with harbor/watch rewards. Landlocked countries are supported through the geography adaptation branch instead. |
| Economy/storehouse | Implemented | `utopia_storehouse_spine` through `utopia_common_store_network` | Has industry, supply, reserve, audit, and foreign-aid hooks. |
| Vocation/learning | Implemented | `utopia_vocation_balance` through `utopia_all_useful_arts` | Uses vocation balance, useful arts shares, education/research, and engineer/healer rewards. |
| Military/just war | Implemented | `utopia_just_war_review` through `utopia_guard_the_ledger` | Uses Household Guard, Storehouse Engineers, defensive drill, no-glory, reinforcement paths, and ledger defense. |
| Diplomacy/League | Implemented | `utopia_need_not_conquest` through `utopia_no_secret_empire`; decisions under `common/decisions/015_utopia_manifesto_decisions.txt` | League identity is applied through `utopia_manifesto_maybe_apply_league_identity` after member/confidence thresholds, not directly by the focus. |
| Needful Land/integration | Implemented | `utopia_needful_land_question` through `utopia_needful_land_commission`; decisions/missions `decision_utopia_boundary_arbitration`, `mission_utopia_boundary_arbitration`, `decision_utopia_common_administration` | Claims are mission/decision-gated; cores require integration conditions. No focus grants instant free cores. |
| Geography adaptation | Implemented | `utopia_coastal_store_routes`, `utopia_landlocked_caravan_stores`, `utopia_subject_ledger`, `utopia_tiny_country_deep_ledger`, `utopia_adapt_the_commonwealth` | Separate adaptations exist for coast, landlocked, subject, and tiny country contexts. |
| Hidden Marked Bounds | Implemented with patch | `utopia_marked_bounds_clause` through `utopia_no_idle_acre`; trigger `utopia_manifesto_can_open_marked_bounds`; patched helper in effects | Hidden route now refreshes after Event 015 ledger changes open it. Residual risk remains for global chaos-only changes without a later ledger refresh. |
| Late proclamations | Implemented | `utopia_paper_utopia`, `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_marked_bounds_state`, `utopia_proclaim_the_common_store`, `utopia_the_manifesto_survives` | Late outcomes are mutually exclusive and then converge into the final proclamation. |
| Cosmetic identities | Implemented | `utopia_manifesto_apply_new_utopia_identity`, `utopia_manifesto_apply_necessary_commonwealth_identity`, `utopia_manifesto_apply_marked_bounds_state_identity`, `utopia_manifesto_maybe_apply_league_identity` | New Utopia, Necessary Commonwealth, and Marked Bounds State are focus-driven. League identity is threshold-driven after League success. |
| Super-event trigger focuses | Implemented | `utopia_new_utopia`, `utopia_marked_bounds_state` | These call `utopia_manifesto_emit_new_utopia_super_event` and `utopia_manifesto_emit_marked_bounds_super_event`. |

## Missing Or Simplified Content

1. Missing focus shine sprites: `interface/015_utopia_manifesto.gfx` defines base `GFX_goal_utopia_*` sprites but no `_shine` variants. The offline focus wiki says available/current focus display expects `GFX_focus_icon_shine`. This is outside the permitted patch scope because it requires `.gfx` asset wiring.
2. Six focus icon IDs are reused. This is not a blocker, but it is repeated icon coverage in a tree that otherwise has strong asset coverage:
   - `GFX_goal_utopia_councils`: `utopia_councils_before_ministers`, `utopia_household_councils`
   - `GFX_goal_utopia_store_state`: `utopia_common_store_state`, `utopia_store_state`
   - `GFX_goal_utopia_surplus`: `utopia_surplus_without_gold`, `utopia_account_surplus`
   - `GFX_goal_utopia_auditors`: `utopia_central_auditors`, `utopia_audit_the_auditors`
   - `GFX_goal_utopia_engineers`: `utopia_engineer_guilds`, `utopia_storehouse_engineers`
   - `GFX_goal_utopia_arbitration_tables`: `utopia_arbitration_tables`, `utopia_boundary_arbitration`
3. `utopia_open_the_manifesto_tt` says the ledger opens and the tree is received, but that behavior happens on event acceptance via `utopia_manifesto_accept_manifesto`, before this focus can be taken. This is a localisation/effect wording mismatch outside the patch scope.
4. `utopia_mark_needed_districts_tt` says marked districts create claims, but the focus itself sets a flag, adds surveyor columns, and raises suspicion; actual claims happen through `decision_utopia_mark_needed_district` and `mission_utopia_marked_district_survey`. This is mostly true at the branch level but may overstate the immediate focus reward.

## Icon Coverage Table

| Check | Result | Notes |
| --- | --- | --- |
| Focus count | 105 | `common/national_focus/015_utopia_manifesto_focus_tree.txt` |
| Unique focus IDs | 105 | No duplicate focus IDs found. |
| Base focus icons | 105/105 referenced | All focus icon references have base sprite definitions in `interface/015_utopia_manifesto.gfx`. |
| Unique base icon IDs | 99 | Six icon IDs are reused, listed above. |
| Shine sprite definitions | 0/99 unique focus icons | Missing `_shine` variants for all unique Event 015 focus icons. |
| Runtime DDS handoff | Present | Existing handoff reports 109 runtime focus DDS files, all 94x86 with transparent corners. I did not reprocess or patch assets. |

## Localisation And Reward Mismatch List

| Identifier | Status | Evidence / issue |
| --- | --- | --- |
| All focus names/descriptions | Covered | Mechanical check found no missing `focus_id` or `focus_id_desc` keys for the 105 focus IDs. |
| `utopia_open_the_manifesto_tt` | Mismatch | Tooltip claims ledger/tree opening, but event acceptance already handles `set_country_flag = utopia_manifesto_ledger_visible` and `load_focus_tree`. |
| `utopia_mark_needed_districts_tt` | Mild mismatch | Text says districts create claims; focus only unlocks/flags the route and adds risk. Claims are decision/mission outcomes. |
| `utopia_necessary_commonwealth_desc`, `utopia_marked_bounds_state_desc` | Weak differentiation | Both descriptions use the same hard-reading wording. Not broken, but the late identities read less distinct than their rewards/cosmetic outcomes. |

## AI Behavior Gaps

| Area | Status | Notes |
| --- | --- | --- |
| Route anchors | Good | The four normal interpretation focuses use route-weight variables and government/ledger modifiers. |
| Hidden Marked Bounds | Improved | `utopia_marked_bounds_clause` uses route weight, Need crisis, and authoritarian modifiers; layout visibility is now refreshed after ledger changes. |
| Leaf/support focuses | Simplified | Many support focuses use flat `ai_will_do = { base = N }`. Every focus has AI, but not every focus is route-/ledger-aware. This is acceptable for low-risk leaf nodes but not fully route-aware. |
| Late outcomes | Partial | `utopia_new_utopia` has meaningful ledger gates and AI modifiers; `utopia_necessary_commonwealth` and `utopia_marked_bounds_state` are gated but have flat base AI weights. |
| Decisions | Present | Decision AI blocks exist for the inspected Needful Land, Marked District, League, and integration decisions. |

## High-Priority Fixes First

1. Fixed: Marked Bounds `allow_branch` could fail to reveal after tree load. Patched `utopia_manifesto_refresh_ledger` to dirty the layout once the Marked Bounds trigger is true.
2. Unfixed, outside scope: add `_shine` sprite definitions for every `GFX_goal_utopia_*` focus icon in `interface/015_utopia_manifesto.gfx` or a matching goals shine `.gfx` file.
3. Unfixed, outside scope: adjust `utopia_open_the_manifesto_tt` and possibly `utopia_mark_needed_districts_tt` to distinguish event acceptance/tree loading from focus rewards and decision/mission outcomes.
4. Unfixed, design/balance follow-up: add route-/ledger-aware modifiers to the flat-AI late outcome focuses and selected shared leaf focuses if the parent wants stricter AI route shaping.

## Validation

Ran focused checks after the patch:

| Check | Result |
| --- | --- |
| Focus block count / unique IDs | 105 focus blocks, 105 unique IDs. |
| Missing focus AI blocks | None. |
| Missing focus localisation keys | None. |
| Missing focus description keys | None. |
| Missing base focus icon sprite definitions | None. |
| Missing focus shine sprite definitions | 99 unique missing `_shine` sprites. |
| Helper wiring | `utopia_manifesto_refresh_marked_bounds_branch` has one definition, one call from `utopia_manifesto_refresh_ledger`, and one `mark_focus_tree_layout_dirty = yes`. |
| Brace balance on touched focus/effect scripts | Balanced. |
| Unsupported `<=` / `>=` in touched focus/effect scripts | None found. |

Skipped live in-game validation; this subagent has no game runtime execution path here, and the user asked for a repo audit/patch handoff.

## Remaining Route Risks

1. Global chaos-only Marked Bounds opening may still wait until the next Event 015 ledger refresh because the patch hooks Event 015 ledger updates, not a global on-action.
2. Missing `_shine` sprites can cause available/current focus icons to fall back to missing focus art even though base DDS assets exist.
3. Some AI weights are present but flat, especially late outcomes and low-risk support focuses.
4. Tooltip wording around tree/ledger opening and marked claims should be cleaned in localisation by the parent/main agent.
5. Event 015 gameplay files are currently untracked in git in this workspace; this handoff reports my targeted patch but cannot provide a tracked diff baseline for the full Event 015 implementation.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
