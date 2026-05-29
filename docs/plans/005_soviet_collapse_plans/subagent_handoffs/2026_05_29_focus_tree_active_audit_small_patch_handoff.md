# Soviet Collapse Focus Tree Active Audit Small Patch Handoff

Date: 2026-05-29
Subagent: Chaos Redux focus tree subagent
Scope: bounded audit and small patch for Soviet Collapse focus trees.

## Required References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs and precedents: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`, vanilla `common/national_focus/soviet.txt`, and vanilla `common/national_focus/baltic_shared.txt`.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_active_audit_small_patch_handoff.md`

No localisation files, decision files, release/scenario mechanics, or flag assets were edited.

## Route Coverage Table

| File | Trees | Focuses | Audit result |
|---|---:|---:|---|
| `005_soviet_collapse_republics.txt` | 9 | 501 | Ukraine, Belarus, Kazakhstan and shared republic trees exist. Ukraine and Belarus still need route-depth/reward-identity redesign. |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 | Full splinters mostly have 47 focuses; crisis splinters have 18-22. Identity exists but repeated small equipment rewards remain. |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 | CFR/MFR route forks now have visible mutual exclusions. OGB remains shallow. |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 | Audited only. All four ancient trees are shallow 16-focus packages and need later route design. |

## High-Priority Fixes Patched

1. Visible route locks for Ukraine.
   - File: `common/national_focus/005_soviet_collapse_republics.txt`
   - Focus ids: `ukr_soviet_collapse_socialist_republic_without_moscow`, `ukr_soviet_collapse_black_banner_compact`, `ukr_soviet_collapse_elections_under_shellfire`, `ukr_soviet_collapse_officers_above_parties`, `ukr_soviet_collapse_protectorate_debate`
   - Before: hidden `available = { hidden_trigger = { NOT = { has_completed_focus = ... } } }` route locks blocked siblings without visible pathline semantics.
   - After: each route selector has reciprocal visible `mutually_exclusive` entries matching the hidden locks.

2. Visible route locks for CFR and MFR.
   - File: `common/national_focus/005_soviet_collapse_factory_successors.txt`
   - CFR governance ids: `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, `CFR_the_concrete_committee`
   - CFR strategy ids: `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, `CFR_contracts_first`
   - MFR route ids: `MFR_officers_chair_the_board`, `MFR_armorers_elect_delegates`, `MFR_merchants_of_ammunition`, `MFR_eternal_arsenal`
   - Before: hidden route locks made mutually exclusive branch behavior non-obvious.
   - After: route selectors have reciprocal visible mutual exclusions.

3. Layout cleanup.
   - File: `common/national_focus/005_soviet_collapse_republics.txt`
   - Tree-level continuous panel: `soviet_collapse_central_asia_focus_tree` continuous panel moved away from `central_asia_soviet_collapse_ashgabat_desert_authority`.
   - Kazakhstan coordinates changed: `kaz_soviet_collapse_aul_councils_and_red_teachers`, `kaz_soviet_collapse_teachers_of_the_new_steppe`, `kaz_soviet_collapse_no_steppe_without_the_south`, `kaz_soviet_collapse_kyrgyz_mountain_liaisons`, `kaz_soviet_collapse_tajik_pass_agreements`.
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - Custom splinter coordinates changed: `FTH_settlement`, `ARD_hidden_doctrine`, `ARD_extreme_gate`, `ARD_extreme_path`.
   - Before: parser found same-row boxes at distance 0 or 1 and continuous panel obstruction.
   - After: parser finds 0 same-row close focus boxes and 0 continuous panel risks.

4. Reward cleanup.
   - File: `common/national_focus/005_soviet_collapse_republics.txt`
   - Focus ids: `ukr_soviet_collapse_grain_loan`, `blr_soviet_collapse_prepare_league_freight_tables`
   - Before: both had direct `small_convoy_reward` stockpile grants in addition to existing helper/mechanic rewards.
   - After: direct tiny convoy grants removed. Existing flags and helper rewards remain.

5. Missing icon references.
   - File: `common/national_focus/005_soviet_collapse_custom_splinters.txt`
   - `BBH_column_schools`: `GFX_focus_generic_military_academy` -> `GFX_focus_BBH_borderless_column_schools`
   - `BBH_commune_mediation`: `GFX_focus_generic_self_management` -> `GFX_focus_BBH_temporary_free_city_pacts`
   - `BBH_non_domination_pacts`: `GFX_focus_generic_diplomatic_treaty` -> `GFX_focus_BBH_no_masters_clause`
   - Before: 3 focus icon ids had no `.gfx` definition.
   - After: missing focus icon definitions check returns 0.

## Localisation Keys and Icon IDs Changed

- Localisation keys changed: none.
- Icon ids changed in focus references only:
  - `BBH_column_schools`
  - `BBH_commune_mediation`
  - `BBH_non_domination_pacts`
- No `.gfx` files were edited. The new icon ids already exist in `interface/005_soviet_collapse_custom_icons.gfx`.

## Missing or Simplified Content List

- Full redesign is not complete. A follow-up plan was written at `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
- Ukraine remains route-heavy and needs route-specific identity, AI, and existing-decision/mechanic hooks beyond visible mutual exclusions.
- Belarus remains route-crowded and needs a corridor/rail/forest identity pass beyond the single tiny reward cleanup.
- Custom splinters still contain repeated direct tiny equipment rewards and need stronger OP expansion/specialization routes.
- OGB has only 23 focuses and remains shallow compared with CFR/MFR.
- Ancient restorations have 16 focuses each and remain shallow.
- 47 direct tiny generic equipment rewards remain. They are listed in the follow-up plan.
- 26 hidden route-lock style focus blocks remain without visible mutual exclusions. They need manual semantics review before broad patching.

## Icon Coverage Table

| Check | Result |
|---|---:|
| Focus icon assignments parsed | 1698 |
| Missing icon definitions before BBH patch | 3 |
| Missing icon definitions after BBH patch | 0 |
| Localisation names missing | 0 |
| Localisation descs missing | 0 |

## Localisation and Reward Mismatch List

- Localisation audit found no missing focus names or descriptions.
- No text was changed, so no BOM-sensitive localisation edit was made.
- Reward mismatch/high-noise backlog remains where focus names imply diplomacy, ports, rail, or patrol identity but still include direct tiny `small_convoy_reward`, `small_train_reward`, `small_truck_reward`, or `small_aa_reward` stockpile grants. Exact ids are listed in the follow-up plan under Reward Cleanup Backlog.

## AI Behavior Gaps

- Many route selectors still use flat `ai_will_do = { base = ... }` or only shallow variable modifiers.
- Ukraine, Belarus, ancient restorations, OGB, and several custom splinter routes need route-aware AI behavior tied to Soviet Collapse variables such as Moscow authority, military obedience, depot vulnerability, foreign appetite, League pressure, old movement pressure, local authority pressure, and chaos tier.
- Decision integration remains mostly helper-effect based. Direct decision unlock count in focus blocks remains effectively absent, though helpers such as League preparation do connect to existing Soviet Collapse mechanics.

## Validation Run

Commands/checks run:

- Focus parser over the four scoped files:
  - `trees=41`
  - `focuses=1698`
  - `duplicate_focus_ids=0`
  - `SPACING_ISSUES 0`
  - `CONTINUOUS_PANEL_RISK 0`
  - `missing_names=0`
  - `missing_descs=0`
  - `missing_icon_defs=0`
- Bracket depth:
  - `common/national_focus/005_soviet_collapse_republics.txt: final_depth=0 min_depth=0`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt: final_depth=0 min_depth=0`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt: final_depth=0 min_depth=0`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt: final_depth=0 min_depth=0`
- Unsupported operator grep:
  - `rg -n "<=|>=" ...` returned no matches.
- Wrong focus filter grep:
  - `rg -n "FOCUS_FILTER_ARMY\\b|FOCUS_FILTER_AIR\\b|FOCUS_FILTER_NAVY\\b" ...` returned no matches.
- Whitespace check:
  - `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt` returned no output.
- Grep audit run for every changed focus id group.

## Skipped Validation

- No in-game load was run from this subagent pass.
- No screenshot/pathline visual validation was run; validation was parser and grep based.
- No commit was created because the worktree already contains extensive concurrent parent/user edits, including edits in the same focus files. Committing from this subagent would risk bundling unrelated work.

## Remaining Route Risks

- This is not a full completion claim for Soviet Collapse focus trees.
- The parser confirms layout and reference safety for the scoped files, but it cannot prove that every pathline is visually pleasing in the game client.
- Some hidden locks may be valid endpoint gates and should not be bulk-mutual-excluded without route review.
- Reward cleanup should be handled route by route so helper calls and decision unlocks stay aligned with the parent release/scenario/decision work.
