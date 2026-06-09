# Event005 Soviet Collapse Focus-Tree Auditor Handoff

Role: `chaosx_focus_tree_auditor` style bounded audit, using `hoi4-focus-trees`.

Scope audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No `gfx/flags`, `.tga`, `.dds`, flag sprites, or flag assets were touched.

## Reference pass

Required local references consulted before focus-file edits:

- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla precedent: `~/projects/Hearts of Iron IV/common/national_focus/soviet.txt`.
- Repo rules: `AGENTS.md`.
- Skill: `/home/klim/projects/chaos_redux/.agents/skills/hoi4-focus-trees/SKILL.md`.

Key engine points used: prerequisite blocks are OR inside one block and AND across blocks; focus pathlines are safest when prerequisites are above children; `ai_will_do` uses MTTH-style scoring; search filters are per-focus UI filter tags.

## Patches applied

Changed files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- this handoff file

Bounded layout-only focus coordinate patches:

| File | Focus id | Change |
| --- | --- | --- |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_army_of_the_republic` | `x = 26` to `x = 27` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_black_sea_port_ledgers` | `x = 31` to `x = 33` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_british_caution` | `x = 30` to `x = 31` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_romanian_port_route` | `x = 23` to `x = 24` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_advisers_without_flags` | `x = 28` to `x = 29` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_direct_national_claims` | `x = 21` to `x = 20` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_black_soil_oath` | `x = 21` to `x = 22` |
| `005_soviet_collapse_republics.txt` | `ukr_soviet_collapse_black_banner_takes_the_villages` | `x = 22` to `x = 21` |
| `005_soviet_collapse_republics.txt` | `baltic_soviet_collapse_baltic_shield_doctrine` | `y = 7` to `y = 8` |
| `005_soviet_collapse_republics.txt` | `baltic_soviet_collapse_singing_barricades_early` | `x = 22` to `x = 18` |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_depot_cars_without_labels` | `x = 8` to `x = 9` |
| `005_soviet_collapse_republics.txt` | `blr_soviet_collapse_join_the_league_when_war_comes` | `x = 15` to `x = 17` |
| `005_soviet_collapse_custom_splinters.txt` | `FTH_enemy_front` | `x = 10` to `x = 12` |
| `005_soviet_collapse_custom_splinters.txt` | `DHC_convoy_autonomy_guarantees` | `x = 9` to `x = 11` |
| `005_soviet_collapse_custom_splinters.txt` | `KHC_grain_passage_guarantees` | `x = 9` to `x = 11` |

No reward logic, AI weights, prerequisites, localisation, scripted effects, sprites, or assets were changed.

## Audit evidence

Full current focus-tree totals across all four Event005 focus files:

- Focus trees: 40
- Focuses: 1698
- Duplicate focus ids: 0
- Direct focus-file `add_ideas`: 0
- Direct focus-file `remove_ideas`: 0
- Direct focus-file `swap_ideas`: 0
- Focuses missing `ai_will_do`: 0
- Focuses missing `search_filters`: 0
- Duplicate coordinate pairs: 0
- Parent-below-child pathline risks found by coordinate scan: 0
- Same-row parent/child pathline risks: 0
- Remaining one-unit same-row spacing risks: 4

Remaining one-unit spacing risks:

| Tree | Count | Examples |
| --- | ---: | --- |
| `soviet_collapse_moldova_focus_tree` | 2 | `moldova_soviet_collapse_tiraspol_depot_belt`/`reject_the_union_question`; `reject_the_union_question`/`southern_rail_timetables` |
| `soviet_collapse_kazakhstan_focus_tree` | 2 | `kaz_soviet_collapse_no_concession_without_a_republic`/`the_steppe_arsenal`; `the_steppe_arsenal`/`the_resource_towns_demand_seats` |

Ukraine and Belarus evidence after patch:

- `soviet_collapse_ukraine_focus_tree`: 83 focuses, 0 direct idea ops, 0 duplicate coordinates, 0 one-unit same-row spacing risks, 0 parent-below-child risks, 0 same-row parent/child risks.
- `soviet_collapse_belarus_focus_tree`: 53 focuses, 0 direct idea ops, 0 duplicate coordinates, 0 one-unit same-row spacing risks, 0 parent-below-child risks, 0 same-row parent/child risks.

Direct idea spam evidence:

- Direct idea operations in Event005 focus files: 0.
- Direct idea operations remain in `common/scripted_effects/005_soviet_collapse_effects.txt`: 51. These are helper/lifecycle-level operations, not direct focus reward lines. I did not replace them in this bounded focus-tree audit because that requires helper-by-helper lifecycle review.

## Remaining depth gaps

Shallow focus-tree families still below the large-country branch-depth standard:

| Tree family | Focus count | Gap |
| --- | ---: | --- |
| `PRA_soviet_collapse_focus_tree` | 22 | Railway identity exists, but route families are still compressed for a major chaos-country successor. |
| `TSC_soviet_collapse_focus_tree` | 18 | High-chaos/special successor is too short for politics, industry, military, diplomacy, expansion, and endgame depth. |
| `RMC_soviet_collapse_focus_tree` | 18 | Cult route needs deeper mechanics, failure pressure, and map-facing consequences. |
| `DSC_soviet_collapse_focus_tree` | 18 | Death-state route remains too compact for the requested powerful lore-mechanical profile. |
| `NRF_soviet_collapse_focus_tree` | 18 | Naval revenant route needs stronger fleet, port, raid, and settlement mechanics. |
| `ICD_soviet_collapse_focus_tree` | 18 | Dead/iron commissariat route needs more playable systems and route consequence. |
| `OGB_soviet_collapse_focus_tree` | 23 | Restored-name successor remains small compared with requested chaos-country power. |
| `KZR_soviet_collapse_ancient_focus_tree` | 16 | Ancient restoration needs a full branch expansion beyond symbolic restoration/claims. |
| `SOG_soviet_collapse_ancient_focus_tree` | 16 | Ancient restoration needs stronger city-state, trade, war, and endgame mechanics. |
| `KHW_soviet_collapse_ancient_focus_tree` | 16 | Ancient restoration needs deeper water/canal authority, patron, and expansion consequences. |
| `ALN_soviet_collapse_ancient_focus_tree` | 16 | Ancient restoration needs deeper steppe/host identity, military, and settlement payoffs. |

Other remaining design risks:

- Several 47-focus custom splinter trees are structurally adequate by count, but still read as repeated route templates in places. They need route-by-route payoff review, not another coordinate pass.
- `005_soviet_collapse_custom_splinters.txt` still relies heavily on helper packages. That is cleaner than direct idea spam, but helper payloads should be reviewed against the visible focus tooltip and route identity.
- Moldova and Kazakhstan retain four total one-unit same-row layout risks. I left them because the user concern emphasized Ukraine/Belarus/custom chaos-country trees, and changing those rows safely requires a more local branch read.

## Implementation plan

1. Run a focused route-depth tranche for the 11 shallow trees listed above. Start with `DSC`, `NRF`, `ICD`, `TSC`, and `RMC` because they most directly match the "chaos-country trees are not powerful or lore-mechanical enough" concern.
2. For each shallow chaos tree, add at least five branch families where conceptually valid: political authority, economy/industry, military doctrine, diplomacy/patron or League interaction, expansion/map consequence, and late endgame.
3. Replace helper-only route payoffs with visible mechanics where possible: decisions, missions, special units, claims/cores/war goals, postwar settlement, leader/cosmetic changes, route locks, and AI strategy.
4. Review `common/scripted_effects/005_soviet_collapse_effects.txt` helper idea operations. Keep real lifecycle helpers, but remove any helper that applies the same static idea repeatedly without gating or upgrade intent.
5. Take a local Moldova/Kazakhstan layout pass for the remaining four one-unit row risks after reading those branches in full.

## Validation

Passed:

- Brace-depth check on all four Event005 focus files: final depth 0, minimum depth 0.
- `rg -n '<=|>='` on all four Event005 focus files: no matches.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed with no output.

Not run:

- In-game validation. Per repo instructions, the user verifies live sessions.
- Full helper lifecycle rewrite validation, because helper payload changes were out of bounded audit scope.

No commit was made.
