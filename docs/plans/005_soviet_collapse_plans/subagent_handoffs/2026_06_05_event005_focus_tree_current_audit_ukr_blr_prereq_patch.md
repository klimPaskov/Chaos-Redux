# Event005 Focus Tree Current-State Audit - Ukraine/Belarus Prereq Patch

Date: 2026-06-05
Role: chaosx_focus_tree_auditor

## Scope

Audited current worktree state for:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Related Event005 localisation/scripted effects were not edited. Flags, `gfx/flags`, graphical assets, binaries, Event006 files, and flag-interface code were not touched.

Required references consulted before opening/editing Chaos Redux files:

- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`.
- Vanilla focus precedents: `common/national_focus/soviet.txt` and `common/national_focus/baltic_shared.txt`, mainly for prerequisite, mutex, `ai_will_do`, and layout patterns.

## Current Audit Metrics

Parser coverage:

- Focus files parsed: 4
- Focus trees parsed: 41
- Focus blocks parsed: 1,698
- Duplicate focus IDs: 0
- Duplicate resolved coordinate groups inside each tree: 0
- Missing prerequisite references in audited files: 0
- Parent-y prerequisite inversions inside same tree: 0
- Direct `add_ideas` or `remove_ideas` effects inside focus completion rewards: 0
- Mutually exclusive asymmetry inside same tree: 0

No direct idea-spam reward remains in the audited focus completion rewards. The current reward-spam issue is now mostly helper-density and repeated helper texture rather than direct `add_ideas`/`remove_ideas`.

## Helper Density By Tree

| Tree | File | Focuses | Helper calls | Calls/focus | Most repeated helpers |
| --- | --- | ---: | ---: | ---: | --- |
| `soviet_collapse_ukraine_focus_tree` | `005_soviet_collapse_republics.txt` | 83 | 65 | 0.78 | `soviet_collapse_apply_focus_foreign_channel` x9, `soviet_collapse_apply_focus_socialist_sovereignty` x8, `soviet_collapse_apply_focus_military_consolidation` x7 |
| `soviet_collapse_breakaway_focus_tree` | `005_soviet_collapse_republics.txt` | 36 | 33 | 0.92 | `soviet_collapse_apply_focus_military_consolidation` x7, `soviet_collapse_apply_focus_depot_and_supply_control` x6, `soviet_collapse_apply_focus_legal_recognition` x3 |
| `soviet_collapse_internal_republic_focus_tree` | `005_soviet_collapse_republics.txt` | 62 | 70 | 1.13 | `soviet_collapse_apply_focus_depot_and_supply_control` x11, `soviet_collapse_apply_focus_security_supply_plan` x6, `soviet_collapse_apply_focus_legal_recognition` x5 |
| `soviet_collapse_baltic_focus_tree` | `005_soviet_collapse_republics.txt` | 42 | 37 | 0.88 | `soviet_collapse_apply_focus_military_consolidation` x8, `soviet_collapse_apply_focus_lawful_supply_plan` x4, `soviet_collapse_apply_focus_depot_and_supply_control` x4 |
| `soviet_collapse_caucasus_focus_tree` | `005_soviet_collapse_republics.txt` | 40 | 39 | 0.97 | `soviet_collapse_apply_focus_legal_recognition` x7, `soviet_collapse_apply_focus_lawful_supply_plan` x5, `soviet_collapse_apply_focus_security_supply_plan` x5 |
| `soviet_collapse_central_asia_focus_tree` | `005_soviet_collapse_republics.txt` | 45 | 47 | 1.04 | `soviet_collapse_apply_focus_republican_compact_plan` x6, `soviet_collapse_apply_focus_legal_recognition` x5, `soviet_collapse_apply_focus_military_consolidation` x5 |
| `soviet_collapse_moldova_focus_tree` | `005_soviet_collapse_republics.txt` | 48 | 49 | 1.02 | `soviet_collapse_apply_focus_depot_and_supply_control` x8, `soviet_collapse_apply_focus_legal_recognition` x7, `soviet_collapse_apply_focus_military_consolidation` x7 |
| `soviet_collapse_belarus_focus_tree` | `005_soviet_collapse_republics.txt` | 53 | 51 | 0.96 | `soviet_collapse_apply_focus_depot_and_supply_control` x8, `soviet_collapse_apply_focus_legal_recognition` x6, `soviet_collapse_apply_focus_security_supply_plan` x6 |
| `soviet_collapse_kazakhstan_focus_tree` | `005_soviet_collapse_republics.txt` | 92 | 90 | 0.98 | `soviet_collapse_apply_focus_depot_and_supply_control` x12, `soviet_collapse_apply_focus_military_consolidation` x12, `soviet_collapse_apply_focus_league_preparation` x10 |
| `FTH_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt` | 47 | 55 | 1.17 | `soviet_collapse_apply_focus_chaos_assault_plan` x6, `soviet_collapse_apply_focus_military_consolidation` x5, `soviet_collapse_apply_focus_chaos_supply_plan` x4 |
| `PRA_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt` | 22 | 22 | 1.00 | `soviet_collapse_apply_focus_legal_recognition` x4, `soviet_collapse_apply_focus_depot_and_supply_control` x4, `soviet_collapse_apply_focus_military_consolidation` x3 |
| `UDC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt` | 47 | 50 | 1.06 | `soviet_collapse_apply_focus_chaos_assault_plan` x7, `soviet_collapse_apply_focus_republican_compact_plan` x5, `soviet_collapse_apply_focus_chaos_legitimacy_plan` x4 |
| `SDZ_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt` | 47 | 47 | 1.00 | `soviet_collapse_apply_focus_republican_compact_plan` x5, `soviet_collapse_apply_focus_chaos_supply_plan` x4, `soviet_collapse_apply_focus_chaos_legitimacy_plan` x4 |
| `NLC_soviet_collapse_focus_tree` | `005_soviet_collapse_custom_splinters.txt` | 47 | 51 | 1.09 | `soviet_collapse_apply_focus_republican_compact_plan` x7, `soviet_collapse_apply_focus_chaos_assault_plan` x5, `soviet_collapse_apply_focus_chaos_supply_plan` x4 |
| `CFR_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt` | 47 | 45 | 0.96 | `soviet_collapse_apply_cfr_focus_public_works` x4, `soviet_collapse_apply_cfr_focus_housing_city_program` x2, `soviet_collapse_apply_cfr_focus_contracting_office` x2 |
| `MFR_soviet_collapse_focus_tree` | `005_soviet_collapse_factory_successors.txt` | 58 | 57 | 0.98 | `soviet_collapse_apply_mfr_focus_security_state` x4, `soviet_collapse_apply_mfr_focus_client_arms_network` x4, `soviet_collapse_apply_mfr_focus_unsafe_output` x4 |

Lower-density trees not expanded above: `TSC`, `RMC`, `DSC`, `NRF`, `ICD`, `BSC`, `TNC`, `ALA`, `BBH`, `KRS`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `ARD`, `OGB`, `KZR`, `SOG`, `KHW`, and `ALN` are between 0.36 and 0.91 helper calls per focus except ancient restorations at 0.62. Their worst repeated helpers are mostly route-specific or low-count generic helpers.

## Layout And Pathline Findings

The parser found no duplicate coordinates or parent-below-child prerequisite inversions, so the remaining layout issue is long prerequisite lines passing through dense clusters.

Worst post-patch clusters:

- Belarus: `blr_soviet_collapse_armored_train_workshops` at `(10,12)` to `blr_soviet_collapse_the_league_depot_at_minsk` at `(24,15)` remains the worst Belarus pathline risk. It crosses the league/freight/ammunition cluster. Fixing this cleanly likely needs moving several nodes or changing branch architecture, not another one-line prerequisite patch.
- Belarus: `blr_soviet_collapse_forest_ammunition_hides` at `(17,15)` to `blr_soviet_collapse_the_forest_state_rumor` at `(30,18)` remains a long high-chaos line across the late forest branch.
- Ukraine: `ukr_soviet_collapse_open_the_liaison_offices` at `(25,5)` to `ukr_soviet_collapse_ports_need_soldiers` at `(32,10)` remains the worst Ukraine edge after patch. A safe fix likely requires a wider foreign-supply lane cleanup.
- Ukraine: `ukr_soviet_collapse_open_the_liaison_offices` at `(25,5)` to `ukr_soviet_collapse_foreign_advisers_in_plain_coats` at `(37,7)` remains long, but it is now the explicit bridge into the foreign-adviser/protectorate lane.
- Other high-risk clusters still visible by heuristic: breakaway `soviet_collapse_a_small_state_with_teeth` to `soviet_collapse_rail_hub_or_mountain_pass`, Baltic `baltic_soviet_collapse_the_baltic_question_resolved`, Moldova `moldova_soviet_collapse_black_soil_recovery_boards`, and BAC `BAC_militia_training_yards` to `BAC_taiga_watch_posts`.

No mutex asymmetry was found inside the audited current-state trees.

## Patch Made

Changed file:

- `common/national_focus/005_soviet_collapse_republics.txt`

Changed focus IDs:

- `ukr_soviet_collapse_protectorate_debate`
- `blr_soviet_collapse_baltic_wire_rooms`

Before and after:

- `ukr_soviet_collapse_protectorate_debate`
  - Before: prerequisite was `ukr_soviet_collapse_open_the_liaison_offices`, producing a long line from `(25,5)` to `(36,9)` through the foreign/military cluster.
  - After: prerequisite is `ukr_soviet_collapse_foreign_advisers_in_plain_coats`, keeping the route inside the existing foreign-adviser lane. This also makes the protectorate debate require the obvious foreign-adviser setup step.
- `blr_soviet_collapse_baltic_wire_rooms`
  - Before: prerequisite was `blr_soviet_collapse_state_between_armies`, producing a long line from `(16,7)` to `(31,12)` across the Belarus political, rail, and forest clusters.
  - After: prerequisite is `blr_soviet_collapse_the_green_border`, keeping the Baltic contact node inside the existing eastern/green-border lane. The original statehood chain is preserved because `the_green_border` still descends from `belarusian_question_answered`, which descends from `state_between_armies`.

Why bounded:

- No new focuses, helpers, localisation, assets, flags, decisions, events, or constants were added.
- No rewards, AI weights, coordinates, mutex groups, or route flags were changed.
- The patch only replaces two existing prerequisite targets with already-existing same-tree focuses in the same route families.

## Validation

Run against final worktree state:

- Structural parser over the four scoped focus files:
  - `focus_trees 41`
  - `focuses 1698`
  - `duplicate_ids 0`
  - `coordinate_duplicate_groups 0`
  - `direct_idea_effects 0`
  - `missing_prereqs 0`
  - `parent_y_inversions 0`
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt`: passed with no output.
- `git diff --no-index --check /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_event005_focus_tree_current_audit_ukr_blr_prereq_patch.md`: no whitespace output; command returned the expected nonzero no-index diff status because the file is new.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt`: no matches.
- `git status --short gfx/flags`: no output.
- `git status --short interface | rg -i "flag|flags"`: no output.
- Required combined check `git status --short gfx/flags interface | head` showed existing non-flag interface changes (`interface/chaosx_achievements.gfx`, `interface/chaosx_super_events.gfx`, and Event006 interface files). This audit did not touch them.

## Remaining Gaps For Parent

- Do not treat this audit as Event005 focus-tree completion. It is a current-state bounded audit with a small pathline patch only.
- Several trees still feel helper-heavy by density. The worst are `FTH`, internal republic, `NLC`, `UDC`, central Asia, Moldova, `PRA`, `MFR`, Kazakhstan, Belarus, and `CFR`. Most have no direct idea spam, but repeated helper categories can still feel samey in play.
- Ukraine and Belarus still have visible layout cleanup opportunities after the two patch lines. The remaining clusters need coordinated branch movement or route architecture changes, not isolated prerequisite edits.
- Chaos/factory successor purpose is better than direct reward spam, but broader balance and route payoff proof still needs parent-level audit against decisions, scripted effects, AI, and in-game behavior.

No commit was made, per instruction.
