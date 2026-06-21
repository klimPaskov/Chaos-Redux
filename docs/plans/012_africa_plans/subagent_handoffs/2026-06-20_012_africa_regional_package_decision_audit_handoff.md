# Event 012 Africa Regional Package Decision Audit Handoff

Date: 2026-06-20
Role: Chaos Redux decision and mission subagent
Scope: bounded Event 012 Africa follow-up audit for regional authority decision/effect surfaces and the WAC/SAH/IOC tag-specific package-action patch shape.

Parent follow-up, 2026-06-21: the package-action presentation finding is closed. `africa_charter_league_diplomacy_category_desc` exposes `africa_regional_package_action_count` against `global.africa_mission_required_regional_package_actions`, and the Continental Congress regional seats card now exposes the same package-action counter beside authority mandates and rail regions. Remaining findings in this handoff should be read against later localisation and cost-gate patches.

## Instructions Applied

- Read `AGENTS.md`.
- Read and applied `chaos-redux-subagents`, `chaos-redux-events`, and `hoi4-decisions-missions`.
- Consulted the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding before inspecting Chaos Redux files.
- Consulted vanilla documentation under `/home/klim/projects/Hearts of Iron IV/documentation/` for effects, triggers, script concepts, and script constants.
- Checked vanilla decision precedent for targeted decisions, custom costs, `ai_will_do`, and equipment gates.

## Changed Files

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_regional_package_decision_audit_handoff.md`

No gameplay, localisation, events, scripted effects, scripted triggers, constants, GUI, GFX, focus, country, history, AI, asset, spreadsheet, Event 010, or Event 070 files were edited. No commit was made.

## Audited Files And Surfaces

- `common/decisions/012_africa_decisions.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/script_constants/012_africa_constants.txt`
- `events/012_african_union.txt`
- `localisation/english/012_african_union_l_english.yml`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md`
- `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_country_package_depth_audit_handoff.md`

## Changed Identifiers

Documentation-only handoff. No gameplay identifiers were changed.

Audited identifiers:

- Decisions: `africa_commission_regional_authority_mandate`, `africa_convene_wac_port_congress`, `africa_open_sah_caravan_columns`, `africa_secure_ioc_sea_lanes`, `africa_regional_authority_mandate_mission`.
- Effects: `africa_start_regional_authority_mandate_for_from`, `africa_apply_regional_authority_mandate_success`, `africa_apply_regional_authority_mandate_failure`, `africa_convene_wac_port_congress_from`, `africa_open_sah_caravan_columns_from`, `africa_secure_ioc_sea_lanes_from`.
- Triggers: `can_africa_target_regional_authority_mandate_for_root`, `can_africa_target_regional_package_action_for_root`, `can_africa_start_regional_authority_mandate`, `can_africa_complete_regional_authority_mandate`.
- Events: `chaosx.nr12.55`, `chaosx.nr12.56`, `chaosx.nr12.57`.
- Flags/counters: `africa_regional_authority_mandate_success`, `africa_wac_port_congress_convened`, `africa_sah_caravan_columns_opened`, `africa_ioc_sea_lanes_secured`, `africa_has_regional_package_action`, `africa_regional_package_action_count`.

## Issue List Sorted By Severity

1. High: WAC/IOC convoy cost gates use `has_equipment = { convoy > ... }`, while the effects spend and transfer `convoy_1`. Existing Event 012 and vanilla precedent commonly gate convoy stockpiles with `convoy_1` when spending `convoy_1`. Fix `africa_convene_wac_port_congress` and `africa_secure_ioc_sea_lanes` to use `convoy_1` so availability matches the actual stockpile spend.

2. High: the new WAC/SAH/IOC decision and report localisation keys appear missing from `localisation/english/012_african_union_l_english.yml`. Static `rg` found no localisation for `africa_convene_wac_port_congress`, `africa_open_sah_caravan_columns`, `africa_secure_ioc_sea_lanes`, `africa_regional_package_wac_cost_tt`, `africa_regional_package_sah_cost_tt`, `africa_regional_package_ioc_cost_tt`, or `chaosx.nr12.55/.56/.57`. The event blocks exist, but without these keys the decisions and reports will show raw ids.

3. Medium: package-action counter visibility is incomplete. `africa_regional_package_action_count` is initialized, incremented, and has a global requirement mirror, but the Charter League and Continental Congress authority card currently show authority mandates, Bestiary actions, and other counters, not regional package actions. Add the package action count to the Charter diplomacy category or authority card if the World Is One gate reads it.

4. Medium: route-locking is safe at the target level but the root triggers for the three package actions only require `africa_regional_authorities_open`; they rely on target triggers for mandate success. This is acceptable mechanically, but player-facing root tooltips should say these are post-success authority actions so empty target lists are not confusing when WAC/SAH/IOC exist but have not completed mandates.

5. Medium: the three report events use a regular event target `africa_regional_package_target` saved inside the helper and fire immediately. This should work for the immediate report chain, but do not make these reports delayed without converting the target to a global target and adding cleanup. If the parent wants delayed reports, add explicit global-target cleanup in each option.

6. Low: `ai_hint_pp_cost` for all three package actions reuses `@africa_regional_authority_mandate_ai_pp_cost` even though the package action PP cost is lower. This does not block function, but the AI hint should be a package-specific file constant, e.g. `@africa_regional_package_action_ai_pp_cost = 25`, to avoid overstating the cost.

7. Low: the effects set both target-specific completion flags and a root-wide `africa_has_regional_package_action` flag. That is fine for a broad "any package action completed" gate, but do not use the root flag to suppress the remaining WAC/SAH/IOC actions. The target-specific flags are the correct one-time blockers.

## Decision Category Lifecycle Notes

`africa_charter_league_diplomacy_category` is the right category for these actions because it already owns Charter member and regional authority target work. The lifecycle is mostly solid:

- Regional authority mandate commissioning is one-active-at-a-time through `africa_regional_authority_mandate_active`.
- A mandate target is stored as `africa_regional_authority_mandate_target` and cleared by `africa_clear_regional_authority_mandate_context`.
- The WAC/SAH/IOC actions are post-mandate one-time target decisions, gated by target flags and by `can_africa_target_regional_package_action_for_root`.
- Runtime cleanup clears WAC/SAH/IOC package flags and the active mandate target.

The main lifecycle gap is presentation: the category description records authority mandate progress but not regional package action progress, even though `global.africa_mission_required_regional_package_actions` exists.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_regional_authority_mandate_mission` | Active Africa unifier | Charter League Diplomacy | Selected regional authority subject | Target exists, loyal, not capitulated, not at war with ROOT, controls capital, and has tag capstone flag | 150 days | Sets target mandate success, increments `africa_regional_authority_mandate_success_count`, applies role-bucket outcome | Lowers Regional Trust, raises Colonial Alarm and Paper-Core Burden, marks retryable failure | Low |

The WAC/SAH/IOC package actions are clickable one-time consequences, not missions. That is acceptable for this bounded follow-up because the prerequisite mission already proves the authority. Do not add a second timer unless the action itself needs a map objective.

## Cost And Requirement Clarity Notes

- Mandate costs are concrete and varied: PP, command power, rifles, support equipment, manpower.
- WAC cost shape is good: PP, support equipment, convoys.
- SAH cost shape is good: PP, command power, infantry equipment, motorized equipment, manpower.
- IOC cost shape is good: PP, command power, support equipment, convoys.
- Fix the WAC/IOC convoy gate token mismatch to `convoy_1`.
- Add missing localisation with icon-first cost text and blocked variants for all three package actions.
- The report/effect tooltips should mention the visible value movement and target-side package without exposing implementation history.

## AI Validity And Route-Lock Notes

- Target validity is good: all three actions require a live regional authority target with mandate success, no capitulation, no Charter former/resistant flags, no war with ROOT, and controlled capital.
- The decisions are tag-specific (`WAC`, `SAH`, `IOC`) and one-time through target flags.
- AI weights are plausible but should also weight to zero indirectly through target triggers; no separate AI-only target bypass is needed.
- Consider package-specific AI hints for PP cost. Current AI hints reuse the regional mandate cost constant, which is higher than the actual package action cost.
- The WAC AI modifier for low League Cohesion, SAH for high Paper-Core Burden, and IOC for Indian Ocean/sponsor readiness all fit the action identity.

## Localisation And Tooltip Gaps

Missing or likely missing localisation keys:

- `africa_convene_wac_port_congress`
- `africa_convene_wac_port_congress_desc`
- `africa_convene_wac_port_congress_root_req_tt`
- `africa_convene_wac_port_congress_target_req_tt`
- `africa_regional_package_wac_cost_tt`
- `africa_regional_package_wac_cost_tt_blocked`
- `africa_convene_wac_port_congress_effect_tt`
- `africa_open_sah_caravan_columns`
- `africa_open_sah_caravan_columns_desc`
- `africa_open_sah_caravan_columns_root_req_tt`
- `africa_open_sah_caravan_columns_target_req_tt`
- `africa_regional_package_sah_cost_tt`
- `africa_regional_package_sah_cost_tt_blocked`
- `africa_open_sah_caravan_columns_effect_tt`
- `africa_secure_ioc_sea_lanes`
- `africa_secure_ioc_sea_lanes_desc`
- `africa_secure_ioc_sea_lanes_root_req_tt`
- `africa_secure_ioc_sea_lanes_target_req_tt`
- `africa_regional_package_ioc_cost_tt`
- `africa_regional_package_ioc_cost_tt_blocked`
- `africa_secure_ioc_sea_lanes_effect_tt`
- `chaosx.nr12.55.t`, `.d`, `.a`
- `chaosx.nr12.56.t`, `.d`, `.a`
- `chaosx.nr12.57.t`, `.d`, `.a`

The category and GUI currently expose mandate counts and Bestiary action counts, but not regional package action counts. Add a short counter line where the player already tracks authority seats.

## Cleanup And Exploit-Risk Notes

- Target one-time flags prevent repeat clicks per authority: `africa_wac_port_congress_convened`, `africa_sah_caravan_columns_opened`, and `africa_ioc_sea_lanes_secured`.
- The target trigger requires mandate success, so package actions cannot be farmed before the authority proves its capstone.
- The root counter can only reach three in this bounded design because only WAC/SAH/IOC actions exist and each has a target one-time flag.
- The effects transfer exactly the spent equipment/manpower to the target, except infrastructure/dockyard/guard reinforcement rewards. These rewards are one-time and bounded by target flags, so no repeat equipment or factory loop was found.
- Runtime cleanup already includes the WAC/SAH/IOC action flags. Keep those cleanup entries if the parent refactors package action names.
- Do not clear package action flags during ordinary target invalidation; they should represent completed historical actions unless the whole Event 012 runtime is being reset.

## Concrete Recommended Fixes

1. In `common/decisions/012_africa_decisions.txt`, change WAC/IOC convoy custom cost gates from `convoy` to `convoy_1`.

2. In `localisation/english/012_african_union_l_english.yml`, add the missing decision, cost, effect, and report-event keys listed above. Keep cost text icon-first and include blocked variants.

3. In `localisation/english/012_african_union_l_english.yml` and, if needed, `common/scripted_localisation/012_africa_scripted_localisation.txt`, expose `africa_regional_package_action_count` against `global.africa_mission_required_regional_package_actions` in the Charter diplomacy description or Continental Congress authority card.

4. In `common/decisions/012_africa_decisions.txt`, add a file-scoped `@africa_regional_package_action_ai_pp_cost = 25` and use it for the three package-action `ai_hint_pp_cost` fields, or remove the hints if parent wants the custom-cost trigger alone to guide AI.

5. If report events are meant to show the selected authority name, write their descriptions using `[africa_regional_package_target.GetName]` and keep the event fired in the same effect chain. If delayed reports are added later, convert `africa_regional_package_target` to a global event target and clear it from every report option.

## Before And After Behavior

Before this handoff: the repo already contains WAC/SAH/IOC targeted package decisions and effects, but the visible localisation/counter surface and convoy-gate consistency still need parent attention.

After this handoff: no gameplay behavior changed. The parent has a bounded checklist for making the patch reviewable without rediscovering the decision, trigger, effect, event, counter, localisation, AI, cleanup, and exploit surfaces.

## Meaningful Validation Run

- Static search confirmed WAC/SAH/IOC decisions call matching helper effects.
- Static search confirmed helper effects call report events `chaosx.nr12.55`, `.56`, and `.57`, and those event blocks exist.
- Static search found no matching localisation entries for the three decisions, three cost keys, three effect tooltip keys, or three report event ids in `localisation/english/012_african_union_l_english.yml`.
- Static search confirmed `africa_regional_package_action_count` is initialized/incremented and has a global requirement mirror, but is not exposed in current localisation or scripted localisation.
- Static search compared convoy requirements against Event 012 and vanilla precedent and found WAC/IOC use `convoy` while their spend/transfer effects use `convoy_1`.

## Skipped Meaningful Validation

- No live HOI4 launch, in-game scenario run, GUI screenshot, or mission completion simulation was run.
- No broad Event 012 completion audit was run; Event 012 remains active and incomplete.
- No localisation parser was run because this was a bounded audit and the missing keys were already visible through static search.

## Remaining Issues

- Parent should patch the convoy gate mismatch and localisation/counter gaps before treating the WAC/SAH/IOC package-action tranche as complete.
- Parent should verify the three actions in a targeted scenario after patching: WAC mandate success then port congress, SAH mandate success then caravan columns, IOC mandate success then sea lanes.
- Event 012 still has broader open country-package depth and live validation blockers outside this handoff.
