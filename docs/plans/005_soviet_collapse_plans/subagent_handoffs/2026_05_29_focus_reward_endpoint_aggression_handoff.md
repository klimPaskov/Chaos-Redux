# Soviet Collapse Focus Reward Endpoint Aggression Handoff

Date: 2026-05-29

Subagent: Chaos Redux focus-tree subagent

## Scope

- Audited:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Soviet Collapse focus localisation in `localisation/`
- Patched only:
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
- Did not edit coordinates.
- Did not edit scripted effects, triggers, decisions, or localisation.

## References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline Paradox wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla precedent scan: national focus `create_wargoal`, `add_ai_strategy`, focus filters, and division/template/equipment reward patterns.

## Files Changed

| File | Change |
| --- | --- |
| `common/national_focus/005_soviet_collapse_custom_splinters.txt` | Added SOV war-goal and hidden SOV aggression AI packages to six shallow high-chaos crisis endpoints; added annexation search filters to those endpoints. |
| `common/national_focus/005_soviet_collapse_factory_successors.txt` | Made the OGB Idel-Ural mutual exclusion mechanically divergent: compact route now adds hidden alliance/support AI toward IUL; rival route now grants an IUL war goal and hidden IUL aggression AI. Added SOV war-goal and hidden SOV aggression AI to the OGB endgame. |
| `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_reward_endpoint_aggression_handoff.md` | This handoff. |

## Changed Focus IDs

| Focus id | File | Before | After |
| --- | --- | --- | --- |
| `PRA_rails_over_capitals` | `custom_splinters` | Extreme rail endpoint called identity/military/endgame helpers only. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `annex_everything` war goal against `SOV`, and hidden conquer/antagonize AI against `SOV`. |
| `TSC_starfall_mandate` | `custom_splinters` | Extreme mandate endpoint gave air XP plus endgame helper. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |
| `RMC_resurrection_without_state` | `custom_splinters` | Death-state endpoint had identity/military/endgame helpers only. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |
| `DSC_congress_of_the_dead_army` | `custom_splinters` | Dead-army endpoint had identity/military/endgame helpers only. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |
| `NRF_northern_revenant_fleet` | `custom_splinters` | Fleet endpoint gave navy XP, convoys, and endgame helper. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |
| `ICD_commissariat_without_end` | `custom_splinters` | Endless commissariat endpoint gave command power and endgame helper. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |
| `OGB_treat_with_idel_ural` | `factory_successors` | Compact route gave PP and opinion only. | Adds hidden alliance/support AI toward `IUL` when it exists. |
| `OGB_the_volga_cannot_have_two_seals` | `factory_successors` | Rival route gave war support, opinion, and legitimacy only. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `annex_everything` war goal against `IUL`, and hidden conquer/antagonize AI against `IUL`. |
| `OGB_the_old_name_survives_modern_war` | `factory_successors` | Endgame helper and Soviet pressure only. | Adds `FOCUS_FILTER_ANNEXATION`, valid-gated `SOV` war goal, and hidden `SOV` aggression AI. |

## Route Coverage Table

| Required route/content area | Implemented coverage | Status | Notes |
| --- | --- | --- | --- |
| Republic political, industry, military, diplomacy, expansion branches | `005_soviet_collapse_republics.txt` has large republic trees with branches and helpers. | Partial | Not patched in this pass. Rewards remain helper-heavy; direct decision unlocks and expansion/postwar hooks remain thin. |
| Custom splinter political/industry/military branches | Most 47-focus custom splinters have visible branch families. | Partial | Templated branch structure remains. This pass only strengthened the weakest short crisis endpoints. |
| Shallow crisis splinter threat behavior | `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD` endpoints now gain direct SOV war-goal and AI aggression hooks. | Improved | This does not replace a full route redesign, but the endpoint reward now matches dangerous high-chaos identity better. |
| Factory successor construction and arsenal threat | Prior dirty worktree already strengthened CFR/MFR. | Improved before this pass | I did not change CFR/MFR. |
| Old Great Bulgaria Volga fork | `OGB_treat_with_idel_ural` vs `OGB_the_volga_cannot_have_two_seals`. | Improved | Compact route now biases AI toward IUL cooperation; rival route grants a direct IUL war goal and aggression AI. |
| Focus-decision integration | No direct `unlock_decision_tooltip`, `activate_decision`, or `activate_mission` found in the three focus files. | Gap | Broader decision integration should be parent-owned because it needs decision/category lifecycle work. |
| Expansion/postwar handling | Some direct claims/war goals now exist, but postwar integration remains sparse. | Partial | War goals are a narrow endpoint payoff, not a full postwar system. |

## Missing or Simplified Content

1. The three audited focus files still contain no direct focus-level decision or mission unlocks.
2. Direct idea spam is not the current main issue: audited focus files have `add_ideas = 0` and `swap_ideas = 0`, but they still rely heavily on shared helpers and flat construction/equipment/stat rewards.
3. The short crisis trees (`PRA`, `TSC`, `RMC`, `DSC`, `NRF`, `ICD`) remain shallow. This pass gives their extreme endpoints a real military consequence but does not add branch families.
4. The custom splinter family remains templated. Many 47-focus trees need bespoke regional goals, decision loops, claims, postwar settlement, and distinct AI behavior.
5. Republic trees still need route-specific decision evolution, postwar integration, and clearer route payoff variety.
6. War goals added here are valid-gated against existing `SOV` or `IUL`; no fallback target selection was added.

## Icon Coverage Table

| Surface | Status | Notes |
| --- | --- | --- |
| Patched focus icon IDs | Unchanged | Existing icons remain assigned for all 9 patched focus IDs. |
| New icon IDs | None | No `.gfx` or sprite references were added. |
| Filter/icon match | Improved | War-goal endpoints now carry `FOCUS_FILTER_ANNEXATION`; cooperative `OGB_treat_with_idel_ural` remains political-only. |
| Broader repeated icon risk | Still present | Previous handoffs reported repeated icon groups across Soviet Collapse trees. This pass did not do an icon differentiation pass. |

## Localisation and Reward Mismatch List

| Focus id | Localisation status | Reward/text alignment after patch |
| --- | --- | --- |
| `PRA_rails_over_capitals` | Existing keys in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: capitals are now subordinated through a visible war aim, not only helper output. |
| `TSC_starfall_mandate` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: mandate now has military expansion consequence. |
| `RMC_resurrection_without_state` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: death-state endpoint now pressures war. |
| `DSC_congress_of_the_dead_army` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: dead army sovereignty now creates an offensive claim. |
| `NRF_northern_revenant_fleet` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: fleet sovereignty now escalates beyond convoys/naval XP. |
| `ICD_commissariat_without_end` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: endless commissariat now has a war payoff. |
| `OGB_treat_with_idel_ural` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: compact route now nudges AI cooperation. |
| `OGB_the_volga_cannot_have_two_seals` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: rival seal route now directly contests IUL. |
| `OGB_the_old_name_survives_modern_war` | Existing keys in `005_soviet_collapse_custom_countries_l_english.yml`. | Better aligned: modern war endpoint now grants a war goal. |

No localisation keys or player-facing IDs were changed.

## AI Behavior Gaps

1. Improved: six crisis endpoints now add hidden `conquer` and `antagonize` AI strategies against `SOV`.
2. Improved: OGB compact/rival route now changes AI diplomacy/aggression toward `IUL`.
3. Remaining: many focus `ai_will_do` blocks are still flat local weights without route strategy.
4. Remaining: focus-granted AI strategies added here are persistent; cleanup/removal hooks were not added because that would require broader scripted system ownership.
5. Remaining: AI needs broader target selection and postwar behavior. This pass intentionally uses only clear `SOV`/`IUL` targets.

## High-Priority Fixes

Completed in this pass:

1. Added direct dangerous endpoint payoffs to `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD`.
2. Added annexation filters to the patched high-chaos endpoints and OGB rival/endgame focuses.
3. Made OGB's Idel-Ural mutual exclusion mechanically meaningful.
4. Avoided coordinate churn while the parent layout pass is active.

Remaining parent-level fixes:

1. Redesign the shallow crisis trees into real fixed-purpose branches with hierarchy, industry, military, expansion, endgame, and postwar handling.
2. Add focus-unlocked decisions/missions for expansion, integration, League conflict, recognition, industrial programs, and military mobilization.
3. Build postwar settlement and integration around the new war-goal endpoints.
4. Continue replacing helper-heavy flat rewards with route-specific mechanics, units, state projects, decisions, and AI route plans.
5. Re-run layout after the parent compactness pass; this subagent made no coordinate edits.

## Validation Run

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`: passed.
- Brace-depth check on both edited focus files: final depth 0, early closes 0.
- Unsupported operator check on both edited focus files: no `<=` or `>=`.
- Mechanical focus scan across the three scoped focus files:
  - 1634 focus blocks.
  - 1634 focus icon assignments.
  - `add_ideas = 0`, `swap_ideas = 0`.
  - `create_wargoal = 10` after this pass.
  - `add_ai_strategy = 31` after this pass.
- Changed focus localisation lookup across `localisation/`: all 9 changed focus IDs and descriptions exist.
- Localisation BOM check for `localisation/english/005_soviet_collapse_l_english.yml`: UTF-8 BOM present. File was not edited.

## Skipped Validation

- No in-game HOI4 load test was run.
- No full mod-wide validator was run because the worktree is dirty with parent/user changes outside this subagent scope.
- No localisation encoding rewrite was performed because no localisation files were edited.
- No Git commit was created because this is a subagent handoff in an actively dirty parent worktree.

## Remaining Route Risks

- This is not a complete Soviet Collapse focus-tree cleanup.
- The new war goals make endpoints more meaningful but do not add claims, cores, occupation decisions, or postwar integration.
- The added AI strategy values follow existing local focus-file precedent and are not centralized in new constants because scripted/system edits were out of scope.
- Broad reward repetition remains in shared helper usage and flat construction/equipment rewards.
- The parent should review this alongside other 2026-05-29 Soviet Collapse handoffs before final completion claims.
