# Custom Splinter Focus Layout Cleanup Handoff

Date: 2026-05-29

Scope: `common/national_focus/005_soviet_collapse_custom_splinters.txt` only.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/custom_splinter_focus_layout_cleanup_handoff.md`

No localisation files were changed.

## Changed Focus IDs

| Focus id | Before | After | Reason |
| --- | --- | --- | --- |
| `PRA_passport_of_the_moving_state` | `x = 0`, `y = 6` | `x = 6`, `y = 6` | Moved OR continuation away from directly under a mutual-exclusive endpoint. |
| `BSC_cleric_elder_compact` | `x = 10`, `y = 8` | `x = 15`, `y = 8` | Moved settlement-side focus out of the `BSC_radical_turn` / `BSC_settlement` fork lane. |
| `BSC_water_and_rifle_ledger` | `x = 12`, `y = 9` | `x = 15`, `y = 9` | Kept the child line aligned after moving `BSC_cleric_elder_compact`. |
| `TNC_madrasah_school_compact` | `x = 10`, `y = 8` | `x = 15`, `y = 8` | Moved settlement-side focus out of the `TNC_radical_turn` / `TNC_settlement` fork lane. |
| `TNC_water_and_bread_ledger` | `x = 12`, `y = 9` | `x = 15`, `y = 9` | Kept the child line aligned after moving `TNC_madrasah_school_compact`. |
| `ALA_anti_puppet_steppe_statute` | `x = 10`, `y = 8` | `x = 15`, `y = 8` | Moved settlement-side focus out of the `ALA_radical_turn` / `ALA_settlement` fork lane. |
| `BSC_kyrgyz_raid_watch` | `x = 22`, `y = 8` | `x = 18`, `y = 8` | Resolved duplicate coordinates in the BSC side branch. |
| `BSC_tajik_pass_bargains` | `x = 22`, `y = 8` | `x = 16`, `y = 8` | Resolved duplicate coordinates in the BSC side branch. |
| `TNC_tajik_relief_corridors` | `x = 18`, `y = 8` | `x = 16`, `y = 8` | Resolved duplicate coordinates in the TNC side branch. |
| `DHC_stanitsa_mediation` | `x = 4`, `y = 6` | `x = 6`, `y = 6` | Resolved duplicate coordinates with `DHC_propaganda`. |
| `KHC_stanitsa_mediation` | `x = 4`, `y = 6` | `x = 6`, `y = 6` | Resolved duplicate coordinates with `KHC_propaganda`. |
| `BAC_militia_training_yards` | `x = 4`, `y = 9` | `x = 2`, `y = 9` | Resolved duplicate coordinates with `BAC_hidden_doctrine`. |
| `ARD_hidden_doctrine` | `x = 6`, `y = 9` | `x = 5`, `y = 9` | Resolved duplicate coordinates with `ARD_murmansk_dockyard_sheds`. |

## Route Coverage

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| PRA board/directorate fork | `PRA_the_board_overrules_ministers` / `PRA_armored_train_directorate` into `PRA_passport_of_the_moving_state` | Layout adjusted | Gameplay prerequisites unchanged. |
| BSC settlement lane | `BSC_settlement` support focuses | Layout adjusted | `BSC_cleric_elder_compact` chain moved out of the fork lane. |
| TNC settlement lane | `TNC_settlement` support focuses | Layout adjusted | `TNC_madrasah_school_compact` chain moved out of the fork lane. |
| ALA settlement lane | `ALA_settlement` support focuses | Layout adjusted | `ALA_anti_puppet_steppe_statute` moved out of the fork lane. |
| DHC/KHC civil-propaganda area | Stanitsa mediation and propaganda support branches | Layout adjusted | Duplicate coordinates removed. |
| BAC/ARD late generic lanes | Military / hidden doctrine branch | Layout adjusted | Duplicate coordinates removed. |

## Before And After Behavior

Before:

- Several settlement-side or OR continuation focuses sat between or directly under mutual-exclusive endpoints.
- Four custom splinter trees had duplicate focus coordinates in the current file.

After:

- The patched focuses use open adjacent lanes and preserve all prerequisites, mutual exclusions, rewards, icons, AI weights, and localisation keys.
- The custom splinter file validates with no duplicate focus coordinates and no `continuous_focus_position` x values under 1000.

## Icons, Localisation, Rewards, And AI

| Surface | Status | Notes |
| --- | --- | --- |
| Icons | Unchanged | No icon ids or sprite references changed. |
| Localisation | Unchanged | No text or localisation keys changed. |
| Rewards | Unchanged | No completion rewards changed. |
| AI behavior | Unchanged | No `ai_will_do` blocks changed. |

## Missing Or Simplified Content

- No route content was added or removed.
- No prerequisite semantics were changed.
- Broader generic `*_industry_plan` merge-lane cleanup was not attempted because several trees would require cascading branch relocation beyond this narrow layout patch.

## Validation Run

Read required references before editing:

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Required core wiki pages from `paradox_wiki/`
- Vanilla focus examples from `~/projects/Hearts of Iron IV/common/national_focus/`
- Vanilla docs in `~/projects/Hearts of Iron IV/documentation/effects_documentation.md` and `triggers_documentation.md`

Validation command:

```bash
python3 - <<'PY'
# Parsed focus trees in common/national_focus/005_soviet_collapse_custom_splinters.txt,
# checked every focus for x/y, duplicate coordinates per tree, and continuous_focus_position x < 1000.
PY
```

Result:

```text
focus_trees=25 validation_errors=0
```

Skipped validation:

- No full game launch or external HOI4 parser was run in this subagent pass.

## Remaining Risks

- Some generic `*_industry_plan` and `*_hidden_doctrine` merge lanes still sit close to `*_radical_turn` / `*_settlement` forks. Moving those cleanly would require broader branch-lane relocation across dense downstream industry and extreme-route chains.
- The file had pre-existing unrelated edits in the worktree before this pass, including other reward and coordinate changes. This handoff only claims the focus IDs listed above.
