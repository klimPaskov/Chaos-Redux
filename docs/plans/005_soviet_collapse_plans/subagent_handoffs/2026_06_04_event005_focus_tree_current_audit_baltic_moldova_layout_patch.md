# Event005 Focus Tree Current Audit - Baltic/Moldova Layout Patch

Role: `chaosx_focus_tree_auditor`
Date: 2026-06-04

## Scope

Audited the current worktree state of the four requested focus files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

No flag assets, flag sprites, `gfx/flags`, `.tga`, `.dds`, or flag-related interface definitions were touched.

## Required References Consulted

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- Offline wiki pages: National focus, Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, Decision modding, Event modding, Idea modding, AI modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`
- Vanilla focus examples for focus reward, filter, layout, and AI syntax

## Current-State Audit Counts

Parsed the current four files after the patch:

| File | Focus trees | Focuses |
| --- | ---: | ---: |
| `005_soviet_collapse_republics.txt` | 9 | 501 |
| `005_soviet_collapse_custom_splinters.txt` | 25 | 1005 |
| `005_soviet_collapse_factory_successors.txt` | 3 | 128 |
| `005_soviet_collapse_ancient_restorations.txt` | 4 | 64 |
| Total | 41 | 1698 |

Mechanical audit results:

- Direct `add_ideas =`: 0
- Direct `swap_ideas =`: 0
- Duplicate direct `add_ideas` inside one focus: 0
- Focus rewards chaining three-or-more direct idea/identity/update helpers in one reward: 0
- Parent-not-above-child coordinate heuristic findings: 0 after patch
- Clear search-filter/reward mismatches: 0 after patch
- Strict small-only rewards still detected by heuristic: 7

## Patched IDs

### Layout/pathline cleanup

- `baltic_soviet_collapse_military_border_government`
  - Moved from `y = 4` to `y = 3`.
  - Reason: parent route choice now sits directly below `baltic_soviet_collapse_the_legal_state_or_the_front_state`, and its child `baltic_soviet_collapse_the_border_front_at_home` no longer draws from a same-row parent.

- `baltic_soviet_collapse_baltic_league_first`
  - Moved from `y = 6` to `y = 3`.
  - Reason: route choice now sits above `baltic_soviet_collapse_baltic_defense_compact` instead of below it.

- `baltic_soviet_collapse_foreign_protection_council`
  - Moved from `y = 5` to `y = 3`.
  - Reason: foreign-protection children now sit below their visible parent rather than above/same-row.

- `moldova_soviet_collapse_western_training_mission`
  - Moved from `y = 7` to `y = 9`.
  - Normalized indentation of the focus block.
  - Reason: the OR prerequisite line includes `moldova_soviet_collapse_conditional_union` at `y = 8`; the child now sits below all visible OR parents.

- `moldova_soviet_collapse_vote_on_the_prut_statute`
  - Normalized indentation only.

### Reward and filter cleanup

- `NLC_weather_station_staff`
  - Changed search filters from `FOCUS_FILTER_POLITICAL FOCUS_FILTER_RESEARCH` to `FOCUS_FILTER_POLITICAL FOCUS_FILTER_STABILITY`.
  - Reason: reward grants command/foreign-channel stabilization effects, not a research bonus, decryption, doctrine reduction, or technology.

- `baltic_soviet_collapse_university_volunteer_lists`
  - Added existing helper `soviet_collapse_apply_focus_military_consolidation = yes`.
  - Reason: reward now does more than a small manpower/army XP bundle and matches the volunteer military branch.

- `CFR_construction_battalions`
  - Added existing helper `soviet_collapse_apply_cfr_focus_defense_build = yes`.
  - Reason: construction battalions now create a practical defense/building payoff through the existing CFR helper instead of remaining a manpower/XP bundle.

## Findings

- Direct idea spam is not present in the current focus files. The active cleanup problem is mostly helper cadence, reward depth, route payoff quality, and layout, not duplicate direct `add_ideas`.
- Most suspected Annexation filter mismatches were false positives from the parser because the focus rewards used scoped `add_claim_by = ROOT` or existing expansion helpers.
- The Baltic and Moldova branches had clear visible pathline issues where children were above or same-row with visible prerequisites. Those are fixed in this patch.
- Custom splinter trees remain broad and templated. Many 47-focus tags now have helper-backed rewards, but their regional mechanics, postwar settlement, AI route identity, and distinct late-game payoff still need parent-level design rather than small auditor edits.
- Factory successors are stronger than earlier handoffs describe, but CFR/MFR route selectors still deserve visual review for mutually exclusive convergence lines that a coordinate-only parser cannot prove clean.

## Remaining Gaps

Strict small-only reward heuristic still flags these focuses:

- `ukr_soviet_collapse_question_of_statehood`
- `ukr_soviet_collapse_village_granary_guards`
- `soviet_collapse_assemble_emergency_government`
- `soviet_collapse_route_consolidation_congress`
- `internal_soviet_collapse_bashkir_cavalry_oath`
- `baltic_soviet_collapse_the_legal_state_or_the_front_state`
- `kaz_soviet_collapse_border_cavalry_schools`

I did not patch these because each is either an early route/fork marker, a fallback-tree opener, or needs a more intentional parent decision about which route mechanic/helper should own the payoff.

## Validation

Validation run after handoff creation:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_event005_focus_tree_current_audit_baltic_moldova_layout_patch.md`
  - Passed with no output.
- `rg '<=|>=' common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - Passed: no unsupported `<=` or `>=` operators in scoped focus files.
- Brace balance on all four scoped `.txt` focus files
  - Passed for all four scoped focus files.
- No flag diff check
  - Passed: no flag-related diff in scoped touched paths.

## Skills Used

- `hoi4-focus-trees`
- `chaos-redux-events`
- `hoi4-decisions-missions`
