# Event005 Bounded Focus Reward Spam Audit Handoff

Timestamp: 2026-06-04 13:30:54 UTC

Subagent role: Chaos Redux focus-tree auditor

## Scope

Audited the bounded Event005 focus reward cleanup requested by the parent. No gameplay, localisation, gfx, flag, or interface files were patched.

Files audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `localisation/english/005_soviet_collapse*_l_english.yml`

Affected focus ids checked:

- `PRA_armored_train_directorate`
- `PRA_seize_the_junction_cities`
- `KZR_returned_names_endgame`
- `KZR_road_beyond_the_caspian`
- `SOG_returned_names_endgame`
- `SOG_cities_beyond_the_desert`
- `KHW_returned_names_endgame`
- `KHW_delta_without_a_center`
- `ALN_returned_names_endgame`
- `ALN_every_pass_a_border`
- `blr_soviet_collapse_military_transit_directorate`
- `kaz_soviet_collapse_the_southern_republics_do_not_kneel`
- `DSC_grave_ordnance_claims`
- `DSC_claim_the_soldiers_road`

## References Read

Repo guidance:

- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`

Required offline wiki snapshot pages:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`

Vanilla references:

- `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/generic.txt`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/china_nationalist.txt`
- `/home/klim/projects/Hearts of Iron IV/common/national_focus/uruguay.txt`

Relevant reference conclusions:

- `custom_effect_tooltip` and `hidden_effect` are documented effects supported in any scope.
- Focus prerequisites are OR within one `prerequisite = { ... }` block and AND across multiple `prerequisite` blocks.
- Focus pathline risk is detectable from duplicate focus ids, prerequisites not visually above dependents, invalid relative positioning, and mutually exclusive lines crossing nodes, but this audit did not render the tree in game.

## Commands And Checks Run

- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`
- `sed -n '1,220p' /home/klim/projects/chaos_redux/.agents/skills/chaos-redux-subagents/SKILL.md`
- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `rg --files '/home/klim/projects/Hearts of Iron IV/documentation' | rg -i 'focus|national|trigger|effect|localisation|ai|script'`
- `find '/home/klim/projects/Hearts of Iron IV' -iname '*focus*documentation*' -o -iname '*national*focus*' | head -80`
- `sed -n '3290,3325p' '/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md' && sed -n '4620,4645p' '/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md'`
- `sed -n '120,260p' 'paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md'`
- One-off Python parser over the four bounded focus files and matching Event005 localisation files. Checks performed:
  - parsed `focus_tree` and `focus` blocks
  - counted duplicate focus ids
  - verified all affected focus ids are present
  - counted visible `soviet_collapse_* = yes` and `nlc_soviet_collapse_* = yes` calls inside `completion_reward` but outside `hidden_effect`
  - flagged duplicate visible helper calls in one reward
  - flagged any focus with 4 or more visible helpers outside `hidden_effect`
  - extracted affected focus tooltips and checked focus title, focus description, and tooltip localisation keys
  - checked UTF-8 BOM on matching Event005 localisation files
  - extracted coordinates, prerequisites, mutual exclusions, relative position ids, and unsupported `<=` or `>=` operators
  - computed same-tree absolute coordinates and checked affected prerequisite geometry and same-tree mutual-exclusion line/node crossings
- `nl -ba common/national_focus/005_soviet_collapse_custom_splinters.txt | sed -n '1378,1425p;1665,1720p;2938,2990p;3138,3198p'`
- `nl -ba common/national_focus/005_soviet_collapse_ancient_restorations.txt | sed -n '345,421p;740,816p;1139,1215p;1532,1614p'`
- `rg -n "id = blr_soviet_collapse_military_transit_directorate|id = kaz_soviet_collapse_the_southern_republics_do_not_kneel" common/national_focus/005_soviet_collapse_republics.txt`
- `nl -ba common/national_focus/005_soviet_collapse_republics.txt | sed -n '8922,8970p;10920,10972p'`
- `rg -n "blr_soviet_collapse_military_transit_directorate|kaz_soviet_collapse_the_southern_republics_do_not_kneel" localisation/english/005_soviet_collapse*_l_english.yml`
- `rg -n "PRA_armored_train_directorate_tt|PRA_seize_the_junction_cities_tt|dsc_grave_ordnance_claims_tt|dsc_claim_the_soldiers_road_focus_tt|KZR_returned_names_endgame_tt|KZR_road_beyond_the_caspian_tt|SOG_returned_names_endgame_tt|SOG_cities_beyond_the_desert_tt|KHW_returned_names_endgame_tt|KHW_delta_without_a_center_tt|ALN_returned_names_endgame_tt|ALN_every_pass_a_border_tt" localisation/english/005_soviet_collapse*_l_english.yml`
- `git status --short`
- `date -u +%Y_%m_%d_%H%M%S`

## Results

Reward spam:

- Parsed 1698 focus blocks across the four bounded files.
- Duplicate focus ids found: 0.
- Missing affected focus ids: 0.
- Focuses with duplicate visible `soviet_collapse_* = yes` helpers in one `completion_reward`: 0.
- Focuses with 4 or more visible helper calls outside `hidden_effect`: 0.

Affected focus tooltip pattern:

- Every affected focus inspected uses a visible `custom_effect_tooltip` for the summarized reward and puts the stacked helper effects inside `hidden_effect`.
- Visible helpers outside `hidden_effect` for the affected ids: 0.
- Unsupported `<=` or `>=` operators in affected focus blocks: 0.

Localisation:

- Checked 42 relevant keys: affected focus title keys, affected `_desc` keys, and affected `custom_effect_tooltip` keys.
- Missing localisation keys: 0.
- Matching Event005 localisation files checked for UTF-8 BOM: all checked files returned true.
- Tooltip key locations include:
  - `PRA_armored_train_directorate_tt`: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3227`
  - `PRA_seize_the_junction_cities_tt`: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3250`
  - `dsc_grave_ordnance_claims_tt`: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3498`
  - `dsc_claim_the_soldiers_road_focus_tt`: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3468`
  - ancient route tooltips: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml:3687`, `3690`, `3721`, `3724`, `3755`, `3758`, `3789`, `3792`
  - `blr_soviet_collapse_military_transit_directorate_tt`: `localisation/english/005_soviet_collapse_blr_focus_l_english.yml:26`
  - `kaz_soviet_collapse_the_southern_republics_do_not_kneel_tt`: `localisation/english/005_soviet_collapse_kaz_focus_l_english.yml:123`

Layout and pathline risk:

- No affected prerequisite was found at the same y level or below its dependent focus within its own focus tree.
- `PRA_armored_train_directorate` mutual exclusion with `PRA_the_board_overrules_ministers` was checked inside `PRA_soviet_collapse_focus_tree`; the line from `(4, 5)` to `(0, 5)` did not cross another PRA focus node under the parser's same-tree coordinate check.
- No affected focus uses a `relative_position_id`, so there is no affected relative-position recursion risk.
- No in-game rendered verification was performed, and no claim is made that the tree was rendered in the client.

## Files Changed

Gameplay/localisation/gfx/interface files changed by this audit: none.

Report file created:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_133054_event005_bounded_focus_reward_spam_audit_handoff.md`

## Remaining Risks

- This was a static parser plus line-level audit, not an in-game focus tree render.
- The mutual-exclusion line crossing check approximates focus node positions from script coordinates and only treats same-tree nodes as relevant. It is suitable for obvious layout risk, not pixel-perfect UI proof.
- Broader branch depth, reward balance, and route design were outside this bounded audit.
