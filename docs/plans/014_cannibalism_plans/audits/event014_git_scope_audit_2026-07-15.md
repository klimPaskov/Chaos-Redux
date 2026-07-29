# Event 014 Git Scope Audit — 2026-07-15

## Verdict

Against branch master at HEAD 4f634045877c970b8472b123210ec0486ff8ad0c, the pre-report Event 014 working-tree tranche contains exactly 977 paths:

| State | Count |
| --- | ---: |
| Modified | 846 |
| Deleted | 76 |
| Untracked | 55 |
| Total | 977 |

All 977 paths are Event 014-only whole-file paths. No modified shared file contains an Event 014 hunk. Therefore:

- whole-file Event 014 paths: 977;
- mixed shared files requiring hunk staging: 0;
- shared-file Event 014 hunks: 0;
- unrelated shared files inspected: exclude all of them.

This audit and its handoff add two untracked Event 014 documentation paths after the snapshot above. With those report artifacts present, the expected Event 014 total is 979 paths: 846 modified, 76 deleted, and 57 untracked.

The repository had 2,919 changed or untracked paths before these report artifacts and no staged paths. The audit is deliberately a scope classification, not an assertion that the other worktree changes are related.

## Method and boundary

The classification used these Event 014 boundaries:

1. Any path segment or basename beginning 014_cannibalism.
2. Any basename beginning zz_014_cannibalism.
3. The exact Event 014 flag ladder:
   - CBA, AHX, CBC, AIX, CBE, CBF, AMX, CBH;
   - CBL, CBL_CENTRAL_COMMAND, CBL_HOST_CONFEDERATION, CBL_RITUAL_STATE;
   - ZZZ_CANNIBALISM_HANNIBAL;
   - each root plus the empty, _communism, _democratic, _fascism, and _neutrality suffixes;
   - each resulting stem at root, medium, and small flag tiers.

The audit then:

- scanned every tracked diff for Event 014 names, chaosx.nr14, Cannibalism, CBA-CBH/CBL identifiers, SCN-010, and removed-origin identifiers;
- manually inspected every matching shared-file diff plus the known achievement, Event Log/evolution/Event Details, scenario, localisation, audio, GFX, dynamic-effect, and chaos-meter integration surfaces;
- compared the working workbook with the HEAD workbook cell-by-cell in memory;
- tested the staging pathspec below against the independently classified set.

The pathspec test selected exactly 977 of 977 pre-report Event 014 paths, with zero missing and zero extra paths.

## Event 014-only path inventory

These counts describe the pre-report 977-path snapshot.

| Path family | Modified | Deleted | Untracked | Classification |
| --- | ---: | ---: | ---: | --- |
| common/country_leader | 1 | 1 | 0 | Event 014-only |
| common/decisions and categories | 2 | 8 | 0 | Event 014-only |
| common/dynamic_modifiers | 1 | 3 | 0 | Event 014-only |
| common/ideas | 1 | 1 | 0 | Event 014-only |
| common/national_focus | 0 | 3 | 1 | Event 014-only |
| common/script_constants | 0 | 14 | 1 | Event 014-only |
| common/scripted_effects | 0 | 20 | 1 | Event 014-only |
| common/scripted_localisation | 1 | 1 | 0 | Event 014-only |
| common/scripted_triggers | 1 | 13 | 0 | Event 014-only |
| docs/assets/014_cannibalism | 560 | 0 | 35 | Event 014-only |
| docs/events | 1 | 0 | 0 | Event 014-only |
| docs/plans/014_cannibalism_plans | 12 | 0 | 17 | Event 014-only |
| docs/specs/014_cannibalism_specs | 10 | 0 | 0 | Event 014-only |
| events | 1 | 1 | 0 | Event 014-only |
| Event 014 flag ladder | 195 | 0 | 0 | Event 014-only |
| gfx/leaders/014_cannibalism | 58 | 2 | 0 | Event 014-only |
| interface | 1 | 6 | 0 | Event 014-only |
| localisation | 1 | 3 | 0 | Event 014-only |
| **Total** | **846** | **76** | **55** | **Event 014-only** |

The 76 deletions are part of the consolidation and asset-correction tranche: 74 superseded Event 014 runtime loader files and two superseded static portrait DDS files. They must be staged as deletions with the rest of the Event 014 set.

The 55 pre-report untracked paths are:

- three consolidated runtime loaders:
  - common/national_focus/014_cannibalism_focus.txt;
  - common/script_constants/014_cannibalism_constants.txt;
  - common/scripted_effects/014_cannibalism_effects.txt;
- 35 paths under docs/assets/014_cannibalism, comprising generation evidence, validation, source-generation notes/prompts, and canonical comparison images;
- 17 paths under docs/plans/014_cannibalism_plans, comprising consolidation re-audits, workbook screenshot evidence, and subagent handoffs.

The two files produced by this scope audit increase the last group from 17 to 19 untracked paths.

## Shared-file classification

There are no mixed files. Every shared candidate below is unrelated to Event 014 and must be excluded in full.

| Shared surface | Current diff and hunk anchors | Classification and action |
| --- | --- | --- |
| common/achievements/chaos_redux_achievements.txt | @@ -3115,0 +3116,120 | Event 019 achievements only; unrelated; exclude |
| localisation/english/chaosx_achievements_l_english.yml | @@ -622,0 +623,37 | Event 019 achievement text only; unrelated; exclude |
| common/scripted_effects/chaosx_events_log_effects.txt | New-side anchors 102-121, 419-423, 451-455, 457-461, 472-478, 481, 486, 530-532, 1332, 1897-1922, 2233, 2697-2700, 2748, and 2986 | Event 019 payload/evolution plumbing only; unrelated; exclude |
| common/scripted_guis/chaosx_scripted_gui_events_log.txt | @@ -321,0 +322 | Event 019 payload selection only; unrelated; exclude |
| common/scripted_localisation/chaosx_scripted_localisation_events_log.txt | New-side anchors 622-625, 1823-1826, 2699-2702, 2908-2911, 3772-3775, 4498-4599, 4763-4766, 5503-5506, 6243-6246, 6726-6729, and 7294-7391 | Event 019 history/title/description mappings only; unrelated; exclude |
| localisation/english/chaosx_event_names_l_english.yml | @@ -21 +21 | Event 019 spelling correction only; unrelated; exclude |
| localisation/english/chaosx_gui_l_english.yml | @@ -78,0 +79; @@ -146,0 +148,13; @@ -185,0 +200,4 | Event 019 SCN-013 UI text only; unrelated; exclude |
| common/script_constants/chaosx_triggerable_scenarios_constants.txt | @@ -25,0 +26; @@ -64,0 +66 | Event 019/SCN-013 registry additions only; unrelated; exclude |
| common/scripted_effects/chaosx_triggerable_scenarios_effects.txt | New-side anchors 54-57, 158-165, 249-256, 296-303, 382-389, 568-575, 806-813, 890-897, and 1022-1037 | Event 019/SCN-013 only; unrelated; exclude |
| common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt | @@ -239,0 +240,7 | Event 019/SCN-013 only; unrelated; exclude |
| common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt | New-side anchors 59-62, 126-129, 193-196, 457-484, 814-841, 1138-1162, and 1244-1271 | Event 019/SCN-013 only; unrelated; exclude |
| docs/systems/triggerable_scenarios.md | @@ -47,0 +48; @@ -137,0 +139,8 | Event 019/SCN-013 documentation only; unrelated; exclude |
| common/scripted_effects/chaosx_dynamic_effects.txt | @@ -502,65 +501,0 | CBRN helper removal only; unrelated; exclude |
| common/scripted_effects/chaosx_dynamic_effects.md | Hunk starts at old/new lines 3, 7, 29, 36, 39, 767/744, 934/925, and 1010/973 | CBRN documentation relocation and general registry-policy edits only; unrelated; exclude |
| common/scripted_effects/chaosx_logic_effects.txt | @@ -37,2 +37,3; @@ -219 +220; @@ -513,0 +515,13; @@ -564 +578,4; @@ -573,0 +591,6 | Event 006 and Event 019 pool/plumbing changes only; unrelated; exclude |
| common/script_constants/chaos_meter_constants.txt | @@ -369,0 +370; @@ -403,0 +405 | Event 019 ghost-decline reason only; unrelated; exclude |
| common/scripted_effects/chaos_meter_effects.txt | New-side anchors 167, 780, 1066-1075, 1511, 1650-1653, 1713, 1856, 2343, 2375, and 2440-2452 | Event 019 ghost-decline accounting only; unrelated; exclude |
| common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt | @@ -3424,0 +3425,17; @@ -3967,0 +3985,10; @@ -4181,0 +4209,10 | Event 019 ghost-decline display only; unrelated; exclude |
| localisation/english/chaosx_chaos_meter_l_english.yml | @@ -302,2 +302,2; @@ -323,0 +324 | Event 019 ghost-decline text only. Existing Cannibalism selector text is unchanged; unrelated; exclude |
| docs/systems/chaos_meter_popup_window.md | @@ -171,0 +172; @@ -190,0 +192,6; @@ -199,0 +207 | Event 019 ghost-decline documentation only; unrelated; exclude |
| docs/systems/chaos_meter_deaths_mechanic.md | @@ -29,0 +30; @@ -95,0 +97,5 | Event 019 ghost-decline documentation only; unrelated; exclude |
| localisation/english/chaosx_raids_l_english.yml | Hunk starts at 9, 12/13, 15/17, 18/21, and 19/24 | Biological/CBRN raid wording only; unrelated; exclude |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | Binary workbook; cell comparison found changes only in Events row 16 (Event 015), Events row 20 (Event 019), and new Scenarios row 11 (SCN-013) | No Event 014 cell, formatting-table, or scenario-row delta; unrelated; exclude the whole workbook |

The all-diff marker scan also encountered .agents/skills/chaos-redux-event-assets/SKILL.md because it contains generic portrait-policy language. It has no Event 014 tranche hunk and is excluded.

Other nearby modified systems, including common/on_actions/002_zombie_outbreak_on_actions.txt and the Fallout successor-allocation effects/triggers, contain Event 006/Fallout work only and are unrelated.

### Mixed-file hunk instructions

None. Do not stage any hunk from any shared file for Event 014.

## Relevant clean integration surfaces

The following Event 014-adjacent shared registries and files are clean against HEAD and therefore are not part of the current tranche:

- interface/chaosx_achievements.gfx;
- interface/chaosx_pictures.gfx;
- interface/chaosx_super_events.gfx;
- interface/chaosx_events_log_popup.gui;
- common/script_constants/world_end_scenario_registry_constants.txt;
- sound/chaosx_sound.asset;
- sound/chaosx_sound.asset;
- music/chaosx_music_track_list.html;
- sound/chaosx_sound.asset;
- all current music/014_cannibalism and sound/014_cannibalism audio files.

The CBA-CBH and CBL country-history files are also clean. Other clean Event 014 singleton files, such as the AI strategy, characters, country tags, MTTH, on-actions, opinion modifiers, scorer, scripted GUI, dormant unit history, and interface/014_cannibalism.gui, must not be added merely because they belong to the feature.

## Exact validated staging pathspec

The following pathspec selected all 977 pre-report Event 014 paths and no others. Once the two report files exist, the same pathspec should select 979 paths.

~~~powershell
git add -A -- ':(glob)**/014_cannibalism*' ':(glob)**/014_cannibalism*/**' ':(glob)**/zz_014_cannibalism*' ':(glob)gfx/flags/**/CB[A-H]*.tga' ':(glob)gfx/flags/**/CBL*.tga' ':(glob)gfx/flags/**/ZZZ_CANNIBALISM_HANNIBAL*.tga'
~~~

Use git add -A because the tranche includes 76 intentional deletions.

After staging, the parent should verify that the staged set contains only the expected Event 014 paths and that its count is 979:

~~~powershell
git -c core.quotepath=false diff --cached --name-status
git -c core.quotepath=false diff --cached --name-only | Measure-Object
~~~

Do not broaden the flag pathspec to all gfx/flags. Specifically exclude:

- all UTOPIA_MANIFESTO and utopia flag paths;
- all ZZZ_weaponized_wendigo flag paths;
- Event 019 files whose names contain prototype_cannibalization;
- all Event 006, Event 015, Event 019, Fallout, and CBRN shared/system changes;
- the workbook and every shared file classified above.

## Simplifications, omissions, and blockers

None for the requested Git-scope audit. Every current Event 014 M/D/?? path was classified, every known modified shared integration surface was inspected, and the proposed pathspec was checked by exact set comparison. The result is tied to HEAD 4f634045877c970b8472b123210ec0486ff8ad0c and must be refreshed if HEAD or the worktree changes before staging.

## Skills used

- chaos-redux-subagents for ownership boundaries and handoff structure;
- xlsx for read-only workbook comparison.

No skill was created or updated.
