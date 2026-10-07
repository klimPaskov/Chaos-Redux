# Event 095 package-integrity report

Date: 5 October 2026.

**Historical result, 5 October 2026: all 21 artifact-structure checks passed.**
The source ZIP was removed at the user's request in commit `6a2ebc838`, and the package was subsequently edited.
These results and their JSON counterpart are original-run receipts, not current integrity evidence.
The validation script checks file counts, links, manifest hashes, preserved source bytes and truthful unexecuted-status fields.
It does not validate HOI4 syntax, engine capabilities, balance, visual quality or independent review.

| Artifact check | Result | Detail |
|---|---|---|
| Fourteen consecutive specification parts | PASS | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] |
| Six required prompts | PASS | asset, achievement, decision_mission, super_event, coding, goal |
| Goal character limit | PASS | 3998 characters, including heading and trailing newline |
| 36 original gameplay coverage rows | PASS | 36 |
| Coverage references resolve | PASS | [] |
| No implementation claim in coverage | PASS | Design coverage remains separate |
| 97 planned unique scenarios | PASS | 97 |
| Runtime tests remain NOT_RUN | PASS | No engine or live-test execution claimed |
| 20 unique role assignments | PASS | 20 |
| Assignments exist and are unexecuted | PASS | Prepared prompts are not runs |
| 49 distinct asset-family rows | PASS | 49 |
| Six achievement triplet families | PASS | 18 required final icons, none produced |
| Original archive unchanged | PASS | 0f13352a0bbf4c657fcb82ac6ec549a1ac208f2624b23489c25dc9bd85105d3e |
| 46 supplied source entries | PASS | 46 inventory / 46 archive |
| Every source byte count and hash matches | PASS | [] |
| Recorded source total | PASS | 15,017 recorded physical lines / 1,337,172 bytes |
| Assignments match supplied roles exactly | PASS | chaosx_3d_model_pipeline, chaosx_ai_probability_auditor, chaosx_asset_source_researcher, chaosx_country_package_auditor, chaosx_decision_mission_auditor, chaosx_documentation_curator, chaosx_event_completion_auditor, chaosx_event_ui_worker, chaosx_focus_tree_auditor, chaosx_generated_event_art, chaosx_icon_artist, chaosx_improvement_loop_planner, chaosx_localisation_auditor, chaosx_portrait_creator, chaosx_repo_explorer, chaosx_scripted_system_architect, chaosx_skill_maintainer, chaosx_spreadsheet_doc_worker, chaosx_super_event_audio_researcher, chaosx_super_event_text_researcher |
| 17 supplied skills | PASS | 17 |
| All local Markdown links resolve | PASS | [] |
| No loose runtime, font or catalog files | PASS | [] |
| Manifest hashes and membership match | PASS | [] |

## Reading-log corroboration

The local reading log contains all 115 chunk identifiers from 0 through 114.
Repeated entries correspond to recovered displays, including chunks 43 and 76–78.
Chunk logs and source hashes corroborate an existing reading record, but do not independently prove reading or understanding.
The full reading report remains the authority for actual scope and external gaps.

## What remains unvalidated

All 97 runtime scenarios remain NOT_RUN.
All 20 specialist assignments remain NOT_EXECUTED.
The full external/native source gate is incomplete.
No actual game launch, native simulation, MCP render/inspect/probability call, final asset production or gameplay implementation occurred.
No authoritative catalog workbook or CSV was changed.

## Reproducing the artifact check

The retained `validate_package.py` requires the removed source ZIP and is blocked for reproducing the original archive checks.
Do not restore the archive to satisfy it or reuse the historical PASS results for the current package.
The current package manifest is maintained separately through local file membership, size and hash checks.
A passing artifact check never changes the event status from To Be Reworked.
