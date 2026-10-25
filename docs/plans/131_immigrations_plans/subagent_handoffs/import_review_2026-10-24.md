# Import review: Event 131 Immigrations

Date: 2026-10-25, reviewing the planning package extracted from `C:\Users\klimp\Downloads\131_immigrations_planning_package.zip`.

## Scope and authority

This subtask imports and reviews the package in documentation folders only, with no gameplay, localisation, GFX, workbook, CSV, or asset edits.
The workbook, shared identifier registry, and CSV export were read only to verify the identity state.
The user's brief restores Event 131 as Immigrations, and the brief is preserved verbatim as `131_immigrations_original_brief.md`.
The shared identifier registry records the parent's 25 October 2026 adoption of Event 131 with former ID 149, Unavailable, and no runtime root.
Gameplay design, classification, numerical tuning, achievements, and report art remain unresolved proposals and are not accepted by this import.

## Archive member count

The archive contains 14 members under `131_immigrations_specs/`, not the 18 stated in the review request.
The archive has no directory entries or other members, and every member's SHA-256 matches the extracted copy used here.
No member was omitted.

## Member disposition

Hashes are the SHA-256 of the original extracted member.

| Archive member | SHA-256 (original) | Destination | Disposition and change |
| --- | --- | --- | --- |
| `README.md` | `c5579c37cab06094fed2f15bdb4e44a33bcf0134e1fca7c517d210320912ca20` | `docs/specs/131_immigrations_specs/README.md` | Edited. Install path, renamed brief link, historical coverage link, identity and disposition table, where-things-went section, evidence status rewritten as original pass plus import review. |
| `131_immigrations_source_brief.md` | `34f56635dabbb05c20842048924a2e2006075c5346bf245043122dfe196c112e` | `docs/specs/131_immigrations_specs/131_immigrations_original_brief.md` | Renamed to follow the Gandhi precedent. Content unchanged, and the destination hash matches the original. |
| `131_immigrations_spec_part_1_core.md` | `02cc3ea2bc2786f46d9cae883dd8445bfa1355acf35d4c2f3659e73c7a952a67` | `docs/specs/131_immigrations_specs/131_immigrations_spec_part_1_core.md` | Edited. Identity rows now show the user-directed brief as accepted identity and 149 as superseded. |
| `131_immigrations_spec_part_2_responses_and_outcomes.md` | `fbd4b467c2b13b709187e60a1ed0156a6550256ab418ea669acae50b3e6a856e` | `docs/specs/131_immigrations_specs/131_immigrations_spec_part_2_responses_and_outcomes.md` | Unchanged. The panel inventory and aid-gap statements were re-checked against docs/systems/migration_system.md and remain consistent. |
| `131_immigrations_spec_part_3_balance_and_presentation.md` | `9bb47b4ba73fc1ab19c7e5c28ff4183a00f8165f239873b7fbf2b57edb77b280` | `docs/specs/131_immigrations_specs/131_immigrations_spec_part_3_balance_and_presentation.md` | Edited. Report-art inventory corrected: seven declared images, four wired by interface/migration_report_pictures.gfx, three famine-owned. |
| `131_immigrations_validation_matrix.md` | `a5f5cd739464174a390eba6fc157f9318e4cfc4b13a344c01ba141e5941fde1d` | `docs/specs/131_immigrations_specs/131_immigrations_validation_matrix.md` | Edited. V34 Mutiny wording now reflects the migration of Widespread Mutiny to catalog 120. No case was added or removed. |
| `131_immigrations_implementation_routes.md` | `dc073a51933ac915e0b3c6e618ce51734946f3ffb4a01ab160deb523c43134ab` | `docs/specs/131_immigrations_specs/131_immigrations_implementation_routes.md` | Edited. Snapshot statement now records the original pass and the 2eabe59360 re-verification. R1 replaces the external protocol reference. The Event 149 conflict is assigned to its documentation owner, and the aid-inventory claim is re-verified. |
| `131_immigrations_research_and_reconciliation.md` | `a9d39fc5cf220f34a19307cd640a9340fc9a9539b402d45efdcb85be378b7f96` | `docs/specs/131_immigrations_specs/131_immigrations_research_and_reconciliation.md` | Edited. Brief and ledger links updated, supplied-source coverage labelled historical, new re-verification section at 2eabe59360, numbering state updated to the 25 October registry adoption and CSV export, and current AGENTS.md wording. |
| `131_immigrations_coding_prompt.md` | `4b812e7fd178755eff7000cc2125d3bc8581c77a00983517605d46998785f16d` | `docs/specs/131_immigrations_specs/131_immigrations_coding_prompt.md` | Edited. Removed the external Project Source protocol instruction, updated the brief reference, catalog state, and workbook gate. The iterate-until-complete and no-claim-before-spec requirements are kept. |
| `131_immigrations_decision_mission_prompt.md` | `2ac84a4a68b601b67ef62f11b474ad9a2eff3d7ee813f1bd0fdae965c63e7343` | `docs/specs/131_immigrations_specs/131_immigrations_decision_mission_prompt.md` | Edited. Corridor and closure action names aligned to docs/systems/migration_system.md (Negotiate a Corridor, Accept a Corridor Offer, Reject a Corridor Offer, Enforce the Closure). |
| `131_immigrations_asset_prompt.md` | `2c7844cfacee604afeda95a6b8d1780d1d17b86f779026ab4a46160212874a63` | `docs/specs/131_immigrations_specs/131_immigrations_asset_prompt.md` | Edited. Report-image inventory corrected to match the four-wired and seven-file reality. Image route now names the gptimage MCP tool for Claude Code and native ImageGen for Codex. |
| `131_immigrations_achievement_prompt.md` | `7f9312bf443ccf5314a750a72203d11cc8e1a7954fd1b99508dbd4c9f86274ad` | `docs/specs/131_immigrations_specs/131_immigrations_achievement_prompt.md` | Edited. Snapshot statement updated. Achievement IDs, trigger names, and file paths were re-verified at 2eabe59360, and a recheck before implementation is still required. |
| `131_immigrations_goal_prompt.md` | `207ca76182ff5140270678b1073460b9aae6a735aa83c7e63fc69d9ac4f2e661` | `docs/specs/131_immigrations_specs/131_immigrations_goal_prompt.md` | Edited. Removed the external source-protocol and Project Sources reads, and updated identity wording. Length is 3,906 characters, inside the 3,500 to 4,000 band and under the 4,000 limit in the event-planning delivery reference. |
| `131_immigrations_source_coverage.json` | `41e4b08805f6b7acf04a95d294b6a1a22cba9f6893292666b1c5b08432734032` | `docs/plans/131_immigrations_plans/imported_review/131_immigrations_source_coverage.json` | Moved to historical evidence. Content unchanged, and the destination hash matches the original. Its paths refer to the external bundle and are not valid repository paths. |

## What was fixed

Stale repository assumptions were corrected.
Event 149 is now described as the superseded former identity, and Event 131 as the registry-adopted Immigrations entry.
Widespread Mutiny is described at catalog 120.
The brief file name and install path were updated.
The report-art inventory was corrected because `interface/migration_report_pictures.gfx` wires four migration sprites while `gfx/event_pictures/famine_and_migration_system/` holds seven report DDS files.
Corridor and closure action names were aligned to `docs/systems/migration_system.md`.
The image-generation route was corrected to the gptimage MCP tool for Claude Code.

Stale instructions were removed.
The external Project Source protocol and Project Sources reads were removed from the coding and goal prompts, and the research note's "supplied" statements were labelled historical.
Snapshot wording in the routes, achievement prompt, and research note now separates the original pass at `41bc4e50` from the 2eabe59360 re-verification.

Internal consistency was restored.
The validation matrix V34 Mutiny cell matches the migration to catalog 120, and the README now has a disposition table and where-things-went section.
Every relative Markdown link in the 13 spec files resolves.

Markdown and style were checked.
No mid-sentence hard wraps were found in the 13 spec Markdown files, and the only multi-line non-prose block is the intentional Mermaid diagram in Part 1.
No update-history wording was added, and no player-facing text was written in this review.

## Re-verified repository claims

The following were checked by path and identifier at `2eabe59360` plus the working tree at review time.
Shared owner files exist: `common/scripted_effects/migration_core_effects.txt`, `migration_spontaneous_movement_effects.txt`, `civilian_transfer_effects.txt`, `migration_integration_effects.txt`, `migration_report_effects.txt`, and `common/scripted_triggers/humanitarian_validation_triggers.txt`.
`migration_request_cross_border_flight` still submits through `migration_spontaneous_movement_submit_request`, and the spontaneous owner still prefers internal displacement with foreign fallback.
The safe spontaneous transfer still requests zero route deaths, and the residual restoration path remains.
The Migration panel documentation still lists four canonical values and seventeen operational actions, with no donor aid action.
The five migration achievement IDs, their `humanitarian_achievement_*_is_complete` triggers, and the possible and natural campaign predicates exist.
The Holy Realm refuge adapter `holy_realm_open_refuge_reception` exists in `common/scripted_effects/003_holy_realm_effects.txt`.
`events/` contains 185 files with no 131 or 149 Immigrations root, and `common/` and `localisation/` contain no `nr131` or `nr149` identifier.
Domestic Unrest is cluster 16 with members 1, 6, 22, 31, and 63, status Needs Testing, and no Event 131 member.
The `.claude/agents/` definitions named in the routes all exist, and `.tools/export_event_catalog_csv.py` exists.

## Unresolved items for the parent

1. Gameplay design acceptance is unresolved for every mechanic, response family, achievement, and art direction in the package.
2. Numerical tuning remains unresolved: the 0.5%, 1%, and 2% request ceilings, the 180-day origin interval, the 30-day observation window, the Chaos bands with the proposed +5 cap, and the Minor Repeatable, Chaos 1, and Domestic Unrest Medium classification. The catalog row records no Type, Chaos level, or cluster facts, which follows the registry rule that proposals are not promoted into catalog facts.
3. International aid has no direct donor action in the migration panel inventory, so the implementation must find the shared humanitarian donor path or justify a minimal shared extension. This is an implementation question for the parent, not a design decision made here.
4. The narrow Event 131 exception to the Event 149 retirement rule is not yet recorded in `docs/systems/migration_system.md`, section "Event 149 retirement", which still forbids a replacement event ID.
5. The ordinary report image has not been decided between reuse and new production. The asset route in the prompt owns that decision.
6. Cluster 16 membership for Event 131 is not registered, and the package treats that as queued runtime work.

## Cross-package issues for the parent

- `docs/systems/migration_system.md` line 185 says "seven report images", while only four are wired by the migration GFX. The owner should state which are migration-wired.
- The Event 149 retirement text in `docs/systems/migration_system.md` needs the narrow Event 131 exception recorded by its owner.
- These active famine and migration specs still describe Event 149 retirement without the Event 131 restoration: `docs/specs/famine_and_migration_system_specs/README.md` (line 85), `famine_and_migration_system_spec_part_3_displacement_migration_return.md` (section "Event 149 absorption"), `famine_and_migration_system_spec_part_7_cross_system_connections.md` (lines 23 and 170), `famine_and_migration_system_spec_part_8_balance_acceptance.md` (line 534), `famine_and_migration_system_coding_prompt.md` (lines 316 to 318), `famine_and_migration_system_goal_prompt.md` (line 28), `famine_and_migration_system_integration_matrix.csv` (line 27), and `subagent_prompts/01_repo_explorer.md`, `11_event_completion_auditor.md`, and `12_spreadsheet_doc_worker.md`. These were not edited because they are outside this package.
- Historical plans under `docs/plans/famine_and_migration_system_plans/` and several other folders mention Event 149. They are historical records and were not edited.
- The workbook's first sheet contains one Immigrations and one Widespread Mutiny entry. Row-level field verification belongs to the spreadsheet worker, and this review did not edit the workbook or the CSV exports.

## Checks performed and limits

- SHA-256 was computed for every copied member. The brief, Part 2, and the coverage ledger are byte-identical to their originals. The other 11 members were edited by exact-match replacement, and the script failed closed unless each old string occurred exactly once.
- Relative Markdown links in the 13 spec-folder Markdown files were resolved on disk, with zero broken links.
- A line-level check for mid-sentence hard wraps found none in the spec-folder Markdown files.
- A stale-term search across the spec folder found only historical "supplied" labels in the README and research note.
- Repository claims listed above were checked by file existence and grep, not by reading whole implementation files.
- No HOI4 MCP tool was invoked, no live game was run, and the deferred tool names were not called.
- The package was not edited beyond the listed destinations, and no commit, stage, or stash was performed.

## Remaining risks

- The re-verification is source and grep evidence, and it does not prove runtime behaviour.
- The working tree contains the parent's uncommitted catalog, registry, and workbook changes, so the 131 and 149 statements can change before commit.
- The goal and coding prompts still require the implementer to re-read the actual owner contracts before editing, and this review does not replace that work.
