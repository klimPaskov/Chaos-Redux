# Soviet Collapse Focus Tree Audit and Duplicate Updater Cleanup

Date: 2026-05-29

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- Read-only context from `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/decisions/categories/005_soviet_collapse_categories.txt`, and `localisation/english/005_soviet_collapse_l_english.yml`

This is not a complete Soviet Collapse focus-tree rework. The tree set still needs a parent-owned redesign pass against the accepted focus-tree spec.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus precedents for `ai_will_do`, `search_filters`, mutual exclusions, construction rewards, war goals, and AI strategies.

## Patch Summary

Changed files:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_audit_duplicate_updater_cleanup.md`

Changed focus ids:
- `ukr_soviet_collapse_factories_under_local_guard`
- `soviet_collapse_factory_defense_committees`
- `blr_soviet_collapse_join_the_league_when_war_comes`
- `kaz_soviet_collapse_basmachi_roads_reopen`
- `kaz_soviet_collapse_karaganda_coal_accounting`
- `PRA_omsk_station_guard`
- `PRA_the_board_overrules_ministers`
- `TSC_observatory_guard`
- `RMC_count_the_returning_names`
- `RMC_reliquary_guard`
- `RMC_republic_of_witnesses`
- `DSC_vote_by_regimental_dead`
- `DSC_field_hospital_memorials`
- `DSC_republic_of_roll_calls`
- `NRF_count_the_drowned_crews`
- `NRF_icebound_marine_guard`
- `NRF_port_republic_of_the_living`
- `ICD_census_of_absent_citizens`
- `ICD_funeral_guard`
- `ICD_citizens_after_death`
- `KHC_crossing_court_registers`
- `IUL_kazan_emergency_registers`

Behavior before:
- 21 focus rewards ran `hidden_effect = { soviet_collapse_update_consolidated_republic_ideas = yes }` and then called a helper that also refreshes consolidated republic ideas. These were stale pre-helper refreshes, so they could remove/add the staged ideas before the real helper payload changed route variables.
- Kazakhstan had `kaz_soviet_collapse_karaganda_coal_accounting` at `x = 21, y = 6`, exactly between mutually exclusive `kaz_soviet_collapse_domestic_resource_state` and `kaz_soviet_collapse_league_resource_pool`.

Behavior after:
- Removed only the stale direct updater calls that appeared before updater-owning helpers. The helper-side update remains, so the final idea refresh still happens after the helper payload.
- Kept 34 direct updater calls that appear after updater-owning helpers, because those may be intentional final refreshes after later variable changes. Removing them safely requires a helper-level deferred-update design.
- Moved `kaz_soviet_collapse_karaganda_coal_accounting` to `x = 21, y = 7` to clear the mutual-exclusion midpoint.

Localisation keys changed: none.

Icon ids changed: none.

## Idea Spam Findings

Direct focus-file idea spam:
- `add_ideas = 0` in the three scoped focus files.
- `swap_ideas = 0` in the three scoped focus files.
- Direct idea maintenance is mostly hidden behind helper calls now.

Remaining helper-driven spam risk:
- `soviet_collapse_update_consolidated_republic_ideas` removes all staged republic ideas via `soviet_collapse_clear_republic_staged_ideas` and then re-adds matching staged ideas. This is hidden, but repeated calls in one focus still create redundant refresh work.
- `soviet_collapse_form_free_republics_league_from_ukraine` contains many updater calls. This may be valid if each call scopes into a different League member, but it needs a scripted-system review before patching.
- 34 focus rewards still call an updater after one or more updater-owning helpers. These were not patched because the final direct call may be the only refresh after variables added later in the focus reward.

Recommended implementation direction:
- Add no-update variants or a deferred consolidated-republic-idea refresh wrapper for focus rewards.
- Refactor focus rewards so variable mutations happen first, helper payloads do not update mid-reward, and one final hidden updater runs at the end.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Ukraine emergency, democratic, socialist, military, grain/industry, logistics, Black Sea, foreign, League, expansion, Black Banner, Bread State | `soviet_collapse_ukraine_focus_tree` has 83 focuses and visible route labels. | Partial | Large but still helper-heavy. 43 simple rewards, only 11 direct mechanic/route hooks by scan. Needs route-specific decision evolution and more payoff variety. |
| Belarus rail, forest, corridor, logistics, League, high-chaos | `soviet_collapse_belarus_focus_tree` has 53 focuses. | Partial | Rail/forest naming exists. 30 simple rewards and only 1 direct mechanic hook by scan. Needs a stronger rail/corridor mechanic and postwar settlement. |
| Kazakhstan steppe, Alash, socialist, military district, resources, southern cascade, Central Asian League, foreign mediation, Basmachi pressure | `soviet_collapse_kazakhstan_focus_tree` has 92 focuses. | Partial | Broadest republic tree, but scan found 54 simple rewards and 0 direct mechanic/route hooks using the audited term set. Needs resource/rail economy and League leadership to drive decisions, cores, settlement, and AI. |
| Baltic legal restoration, coast/forest defense, recognition, Baltic League, exile/underground, anti-puppet, anti-Moscow pressure | `soviet_collapse_baltic_focus_tree` has 42 focuses. | Partial | Country-adapted flavor is present, but there are no direct expansion hooks and 19 simple rewards. Needs intervention pressure and postwar handling. |
| Caucasus national council, mountain/border defense, oil/infrastructure, Turkish/Iranian mediation, Caucasus League, loyalist garrisons, high-chaos/restoration pressure | `soviet_collapse_caucasus_focus_tree` has 40 focuses. | Partial | Oil/pass naming exists. No direct route hooks by scan and 19 simple rewards. Needs oilfield security decisions and mediation consequences. |
| Central Asian council, southern defense, Basmachi, foreign mediation, cotton/water/rail/pass economy, Central Asian League, ancient pressure | `soviet_collapse_central_asia_focus_tree` has 45 focuses. | Partial | Required labels exist, but 26 simple rewards and 1 direct hook. Needs country-adapted subroutes for UZB/TMS/TAJ/KYR rather than shared generic payloads. |
| Moldova Chisinau council, Dniester defense, Romanian diplomacy, Ukraine settlement, agrarian/river economy, League observer, high-chaos Dniester | `soviet_collapse_moldova_focus_tree` has 48 focuses. | Partial | Route names are present, but 28 simple rewards and 1 direct hook. Needs Dniester/Romanian/Ukraine settlement decisions and clearer route locks. |
| Internal republic compact trees | `soviet_collapse_internal_republic_focus_tree` has 62 focuses. | Partial | Many internal identities are present, but 41 simple rewards and only 1 direct hook. Needs local compact mechanics and differentiated outcomes. |
| Custom splinters | 25 custom splinter trees. Most long-form trees have 47 focuses; crisis splinters have 18-22. | Partial to shallow | Long-form trees remain templated. Short crisis trees are very shallow despite prior endpoint war-goal patches. |
| Factory successors | `CFR`, `OGB`, `MFR` trees. | Partial | CFR and MFR have stronger industrial identity than most trees. CFR has only 3 expansion-filter focuses and still needs larger visible civilian-factory escalation. OGB is compact but still mostly legitimacy/simple rewards. |

## Missing or Simplified Content

High priority:
- Add real focus-to-decision integration. The three focus files still have effectively no direct `activate_decision`, `activate_mission`, or `unlock_decision_tooltip` usage; route effects are mostly hidden helper calls.
- Add expansion branches that do more than claims or one war goal. Required postwar handling should include cores, occupation/integration missions, puppet/protectorate choices, settlement events, or resistance consequences.
- Give chaos countries stronger overpowered behavior:
  - `CFR_*`: more civilian factories and construction decision escalation, not only mandate variables and a few factory rewards.
  - `DSC_*`, `RMC_*`, `ICD_*`, `NRF_*`: more immediate neighbor aggression, coring of occupied states, relentless war AI, and zombie/dead-state route consequences.
  - `PRA_*`, `TSC_*`: stronger map consequences and mechanical identity beyond one endpoint SOV war goal.
- Replace repeated simple rewards with route mechanics. Many trees have 40-60% simple rewards by scan.
- Create route-specific AI strategy plans. Existing `ai_will_do` blocks are present on all focuses, but most are flat local weights.

Reward monotony by branch/tree:
- Republic trees: many focuses still give small factories, equipment, XP, stability, war support, or variables via common helpers. Ukraine, Belarus, Kazakhstan, Central Asia, Caucasus, and Moldova all need route-specific mechanics and decision unlocks.
- Custom splinters: long-form 47-focus trees share repeated branch skeletons and generic helper rewards. The 18-focus crisis trees are especially shallow.
- Factory successors: CFR/MFR are stronger than average, but several focuses still resolve to mandate/industry numbers instead of new construction systems, forced labor/worksite missions, protectorate decisions, or coring/wargoal packages.

## Icon Coverage Table

| Tree group | Focus icons | Missing icon assignments | Repeated icon IDs | Notes |
| --- | ---: | ---: | ---: | --- |
| Republic focus file | 501 / 501 | 0 | Repeats in most trees except Kazakhstan | Assignments exist, but repeated icon families remain. Asset definition existence was not fully validated. |
| Custom splinter focus file | 1005 / 1005 | 0 | Repeats in many templated 47-focus trees | The repeated icon pattern reinforces the templated feel. Needs asset-led icon differentiation. |
| Factory successor focus file | 128 / 128 | 0 | CFR repeats 11 icon IDs; OGB/MFR no repeated IDs by scan | CFR uses repeated construction/civilian motifs; this may be intentional but needs unique variants per spec. |

## Localisation and Reward Mismatch List

- Focus localisation lookup across `localisation/`: all audited focus ids and `_desc` pairs were found by scan.
- No localisation keys were changed in this patch.
- Reward mismatch risks remain where focus names promise large political or expansion outcomes but rewards are helper/stat payloads:
  - Kazakhstan resource and League branches need visible resource/rail/League mechanics.
  - Belarus rail and forest branches need rail/corridor missions, not only generic helper rewards.
  - Caucasus oil and mediation branches need oilfield/infrastructure and foreign mediation decisions.
  - Dead/revenant splinters need immediate coring, war, and aggression behavior matching their names.

## AI Behavior Gaps

- All 1634 scoped focus blocks have `ai_will_do`, but most are flat `base` weights with small state checks.
- Few focus rewards add direct persistent AI strategies; prior dirty work added some endpoint aggression, but it is not a complete route-aware AI plan.
- Missing route-aware AI:
  - Ukraine should choose between legal, socialist, military, League, expansionist, Bread State, and Black Banner paths based on war state, stability, sponsor pressure, and League readiness.
  - Belarus should prioritize rail/logistics and corridor defense when threatened.
  - Kazakhstan should prefer resource/state, League, foreign mediation, or Basmachi paths based on southern cascade, foreign pressure, and resource authority.
  - Chaos states should prefer war, coring, and nearby expansion far more aggressively than normal republics.

## Pathline and Mutual Exclusion Findings

- Duplicate coordinate audit after patch: 0 duplicate focus coordinates in touched focus files.
- Mutual-exclusion midpoint audit after patch: 0 midpoint hits in touched focus files.
- Patched pathline risk:
  - `kaz_soviet_collapse_karaganda_coal_accounting` no longer sits between `kaz_soviet_collapse_domestic_resource_state` and `kaz_soviet_collapse_league_resource_pool`.
- Meaningless mutual exclusions were not broadly removed. Remaining mutual exclusions should be reviewed during the rewrite to ensure they represent real incompatible institutions, not layout or branch labels.

## Concrete Rework Plan

1. Build shared focus reward architecture first:
   - Create deferred consolidated-idea update wrappers.
   - Split helper payloads into variable/reward mutation and final idea refresh.
   - Add focus-level route flags that decisions and AI can read.

2. Republic tree rewrite pass:
   - Ukraine: make League leadership, Bread State, Black Banner, Black Sea expansion, and grain/industry routes alter decisions, war goals, cores, leaders, flags/cosmetic names, and AI.
   - Belarus: build rail sovereignty/corridor defense missions and forest logistics mechanics.
   - Kazakhstan: build resource authority, rail corridor, southern cascade, Alash/socialist/foreign mediation, and Central Asian League mechanics.
   - Central Asia/Caucasus/Moldova/Baltics: country-adapt shared trees with distinct state targets, foreign reactions, and regional leagues.

3. Custom splinter rewrite pass:
   - Convert repeated 47-focus skeletons into families with distinct political, industrial/logistics, military, diplomacy, expansion, and high-chaos endgame payoffs.
   - Expand short crisis splinters (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) beyond 18-22 focus endpoint ladders.

4. Chaos overpowered pass:
   - CFR gets major civilian construction surge, rapid worksite decisions, client city/protectorate mechanics, and SOV/neighbor rebuilding-or-conquest branches.
   - Dead/revenant states get immediate coring of controlled states, aggressive neighbor war goals, direct AI conquest plans, and death-state recruitment/economy loops.
   - MFR gets arsenal quotas tied to arms factories, production lines, forced procurement, and war escalation.

5. AI and validation pass:
   - Add route-aware AI strategies and invalid-route zero weights.
   - Re-run focus count, icon, localisation, duplicate coordinate, mutual exclusion, reward monotony, and route coverage audits.

## Validation Run

Passed:
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt`
- Brace balance on touched focus files: final depth 0, early closes 0.
- Unsupported operator scan on touched focus files: no `<=` or `>=`.
- Duplicate coordinate/pathline audit on touched focus files: duplicate coordinates 0, mutual-exclusion midpoint hits 0.
- Direct-before-helper duplicate updater scan: 0 remaining.

Skipped:
- Full mod validation was skipped because the worktree is already dirty with ongoing Soviet Collapse changes outside this subagent scope.
- No Git commit was created because this is a subagent handoff in a dirty parent worktree.

## Remaining Route Risks

- This patch does not solve the broad complaint. It only removes high-confidence duplicate updater calls and one pathline risk.
- Many route rewards remain helper-heavy and simple.
- Focus decision/mission integration is still thin.
- Icon assignment coverage is complete, but unique icon identity is not.
- AI behavior exists as `ai_will_do`, but not as complete route-aware behavior.
- Broad rewrite should be parent-owned or split into planned subagents by tree family.
