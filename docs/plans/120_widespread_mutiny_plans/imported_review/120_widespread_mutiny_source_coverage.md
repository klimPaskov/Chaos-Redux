# Event 120 source coverage

The full supplied-source gate passed at **2026-10-23 17:22:48.090548 UTC**, before substantive design and repository research. The completed pass covered **152 unique text bodies, 3,212,060 original bytes and 36,169 lines**. Root and reviewers A, B and C each read their assigned complete bodies in model-visible output. Root reviewed the specialist findings and recorded the global completion.

This is a team reading claim. Root personally covered 29 unique bodies. The inventory stage made no content-reading claim and predates the final team assignment. The completed reader ledgers and parent completion record govern the final coverage status.

The companion `120_widespread_mutiny_source_coverage.json` contains every full SHA-256, all original provenance instances, original assignments, credited readers and complete recorded reading ranges. Both coverage files contain evidence metadata. Supplied source bodies, source archives, internal planning scratch files and review plans are excluded.

## Verified corpus totals

| Measure | Verified result |
|---|---:|
| Original top-level sources | 27 |
| Top-level text sources | 24 |
| Top-level ZIP sources | 3 |
| Top-level source bytes | 2,286,113 |
| All provenance records | 199 |
| Text provenance instances | 194 |
| Archive provenance instances | 5 |
| Unique archive bodies | 4 |
| Archive member occurrences, including nested ZIP entries | 172 |
| Unique text bodies | 152 |
| Unique text bytes | 3,212,060 |
| Unique text lines | 36,169 |
| Exact duplicate text groups | 42 |
| Additional duplicate text instances | 42 |
| Text provenance bytes, before deduplication | 4,414,742 |
| Text provenance lines, before deduplication | 50,241 |
| Other non-text bodies | 0 |
| Uncovered bodies or verification discrepancies | 0 |

All 199 original provenance records were rehashed. Every archive member was opened recursively from the original ZIP bytes and compared byte for byte with its extraction copy. Every same-hash group was also compared byte for byte. The final counts exactly match the completed gate. Compressed archive sizes and expanded text sizes describe different inventories and should be read separately.

There are 110 text bodies with one provenance instance and 42 with two exact-byte instances. The repeated legacy documents and repeated legacy subagent members share a reading credit only after equality verification. Older and newer versions with different hashes remain separate bodies and were each read completely. The standalone legacy subagents ZIP is also byte-identical to the nested legacy copy. The dated upload contains a distinct subagents ZIP.

## Four-reader coverage

| Reader | Original assigned bodies | Credited complete bodies | Original bytes | Lines |
|---|---:|---:|---:|---:|
| root | 23 | 29 | 785,704 | 9,798 |
| A | 42 | 42 | 939,057 | 10,174 |
| B | 43 | 40 | 724,329 | 7,941 |
| C | 44 | 41 | 762,970 | 8,256 |
| **Total** | **152** | **152** | **3,212,060** | **36,169** |

Each unique body has exactly one credited reader in this partition. Reviewer A additionally read the complete source protocol and user brief, queues 23 and 152, for orientation. Root holds their assigned coverage. These two supplementary reads are preserved in JSON and add no bodies, bytes or lines to the partition totals.

## Recovered output truncations and assignment transfers

| Evidence | Final accounting |
|---|---|
| Root, queue 4 | The initial truncated AGENTS output was superseded by a complete reread covering characters `[0, 44418)` and lines 1 through 431. The recovery note was repeated across the original root ledger entries. It describes this AGENTS recovery. |
| A, batch 18, queues 100, 101 and 105 | The first attempt exceeded available model context and received no reading credit. The whole batch was reread after compaction without truncation. The recovered spans are queue 100 `[4635, 8680)`, queue 101 `[0, 11844)` and queue 105 `[0, 24107)`. Queue 100's earlier span and queue 105's later span were read in adjacent batches. |
| B to root, queues 68 and 112 | B recorded no reading credit. Root completed both bodies and owns their final coverage. |
| C to root, queues 93, 97 and 109 | C explicitly marked the bodies unread by C. Root completed all three. |
| A to root, queue 115 | A deliberately omitted this body from batch 20 and recorded empty read ranges. Root completed it. |
| B to root to A, queue 124 | No prior reading credit was claimed. A completed both extra chunks, `[0, 37386)` and `[37386, 70328)`, covering lines 1 through 143 and 144 through 296. The persisted ledger entry completed the global union before the gate passed. |
| A retained, queues 88, 89 and 90 | A had fully read these bodies before root proposed taking ownership. The completed gate retains A as the actual reader and credits no root reread. |

B and C report complete retained reads without content truncation. No unrecovered source-reading truncation remains in the completed gate. Failed display attempts receive no coverage credit. The final metadata audit does not add new source-reading claims.

## Byte identity and reading coordinates

SHA-256 and byte counts always refer to the unmodified original bytes, including any UTF-8 BOM and original newline representation. Lines are recounted with `splitlines()` after UTF-8 decoding with an optional BOM removed. Character positions describe the reading display convention and are distinct from byte offsets.

| Reader | Character coordinates | Line evidence |
|---|---|---|
| Root | Zero based, end exclusive, UTF-8 decoded source with any BOM and original newline characters retained | Whole-body inclusive line range, with separately recorded character chunk boundaries |
| A | Zero based, end exclusive, optional BOM removed and CRLF or CR normalized to LF | Inclusive line range for every recorded read chunk |
| B | One based, inclusive, BOM retained and CRLF or CR normalized to LF for display | Inclusive range for each display chunk. Adjacent chunks can share a line when a character boundary falls inside it |
| C | Zero based, end exclusive, UTF-8 decoded source with any BOM and original newline characters retained | Whole-body inclusive line range, with separately recorded character chunk boundaries. The queue 10 note also records newline normalization during that full-file display |

B records raw decoded source character counts alongside normalized display ranges. Their difference is explained by newline normalization. JSON preserves both and provides an additional zero-based, end-exclusive form of the recorded character intervals. Every recorded range set reaches its verified full extent without gaps. Root and C aggregate line ranges are labelled as whole-body evidence, so they are not presented as independently recorded per-chunk line positions.

The reading claim comes from the contemporaneous reader attestations and completed gate. The final administrative audit checks those records against the actual source bytes and verifies arithmetic, provenance and interval completeness.

## Original top-level source inventory

These 27 paths describe the original supplied sources. The SHA-256 column is a 12-character prefix for navigation. JSON carries the complete hashes.

| Source path | Kind | Bytes | Lines | SHA-256 prefix |
|---|---|---:|---:|---|
| `project_sources/01-subagents.zip` | archive | 62,071 | n/a | `376a16781713` |
| `project_sources/02-chaos-redux-improvement-loop.md` | text | 28,515 | 289 | `ca2b6a001f69` |
| `project_sources/03-chaos-redux-comfyui.md` | text | 2,456 | 21 | `125daa4e6695` |
| `project_sources/04-chaos-redux-decisions-missions.md` | text | 64,394 | 1,022 | `bd92b691ec78` |
| `project_sources/05-AGENTS.md` | text | 44,442 | 431 | `ba5f6799c692` |
| `project_sources/06-chaos-redux-subagents.md` | text | 41,493 | 366 | `68e6b1d4878e` |
| `project_sources/07-chaos-redux-3d-model-pipeline.md` | text | 96,728 | 477 | `45ffc273c4df` |
| `project_sources/08-chaos-redux-event-planning.md` | text | 197,109 | 2,297 | `4a1a0a46ffe4` |
| `project_sources/09-chaos-redux-event-assets.md` | text | 109,712 | 1,004 | `6766e846130e` |
| `project_sources/10-chaos-redux-events.md` | text | 80,791 | 833 | `42b1c53c5996` |
| `project_sources/11-chaosx_dynamic_effects.md` | text | 19,635 | 328 | `73b2740ebfb8` |
| `project_sources/12-chaos-redux-scripted-gui.md` | text | 23,695 | 130 | `f85f0a0888b2` |
| `project_sources/13-chaos-redux-frame-animation.md` | text | 28,266 | 501 | `86469ff50f33` |
| `project_sources/14-chaos-redux-focus-trees.md` | text | 98,951 | 1,505 | `74805c1f8522` |
| `project_sources/15-chaos-redux-debug-playtest.md` | text | 34,086 | 698 | `9c6e27b8a86f` |
| `project_sources/16-chaos-redux-super-events.md` | text | 33,489 | 787 | `001a899b4b19` |
| `project_sources/17-chaos_redux_clusters_catalog-5-.csv` | text | 5,362 | 20 | `689fe07883da` |
| `project_sources/18-chaos_redux_scenarios_catalog-5-.csv` | text | 16,848 | 120 | `8b944de19817` |
| `project_sources/19-chaos_redux_events_catalog-5-.csv` | text | 65,053 | 294 | `e2e457ba96ae` |
| `project_sources/20-config.toml` | text | 11,714 | 192 | `24bcac71960d` |
| `project_sources/21-README.md` | text | 2,857 | 42 | `9f713e2dcaf1` |
| `project_sources/22-chaosx_dynamic_triggers.md` | text | 3,991 | 61 | `6792ee030cb6` |
| `project_sources/23-CHAOS_REDUX_MECHANICS.md` | text | 41,848 | 855 | `e3f21aca358f` |
| `project_sources/24-all-project-sources.zip` | archive | 418,567 | n/a | `658006c9a1fd` |
| `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | text | 12,728 | 373 | `e7d9ac3d70b8` |
| `upload/120 - Widespread Mutiny.md` | text | 2,317 | 34 | `7a9f98784faa` |
| `upload/all-project-sources(20261023-170917).zip` | archive | 738,995 | n/a | `82fd1eb220e9` |

## ZIP provenance instances

The notation `!/` identifies an archive member in its supplied container. It is a provenance notation and does not identify a file included in the delivered specification ZIP. Each nested container is listed independently. Immediate uncompressed bytes include a nested ZIP as a member where present.

| Original archive location | Direct members | Immediate uncompressed bytes | SHA-256 prefix |
|---|---:|---:|---|
| `project_sources/01-subagents.zip` | 20 | 151,247 | `376a16781713` |
| `project_sources/24-all-project-sources.zip` | 23 | 1,113,506 | `658006c9a1fd` |
| `project_sources/24-all-project-sources.zip!/subagents.zip` | 20 | 151,247 | `376a16781713` |
| `upload/all-project-sources(20261023-170917).zip` | 86 | 1,922,367 | `82fd1eb220e9` |
| `upload/all-project-sources(20261023-170917).zip!/subagents.zip` | 23 | 128,239 | `b7b2f3d44b90` |

JSON preserves the complete member inventories and all 194 text provenance instances. Extraction workspace paths are omitted. A body found in multiple supplied locations retains every location in its provenance array.

## Complete 152-body index

The source path is one canonical original provenance location for the body. All exact duplicate locations and full hashes remain in JSON. Queue IDs preserve the original reading queue order. Every row has complete reading coverage.

| Queue | Reader | Bytes / lines | Source path | SHA-256 prefix |
|---:|---|---:|---|---|
| 1 | A | 28,515 / 289 | `project_sources/02-chaos-redux-improvement-loop.md` | `ca2b6a001f69` |
| 2 | A | 2,456 / 21 | `project_sources/03-chaos-redux-comfyui.md` | `125daa4e6695` |
| 3 | A | 64,394 / 1,022 | `project_sources/04-chaos-redux-decisions-missions.md` | `bd92b691ec78` |
| 4 | root | 44,442 / 431 | `project_sources/05-AGENTS.md` | `ba5f6799c692` |
| 5 | A | 41,493 / 366 | `project_sources/06-chaos-redux-subagents.md` | `68e6b1d4878e` |
| 6 | C | 96,728 / 477 | `project_sources/07-chaos-redux-3d-model-pipeline.md` | `45ffc273c4df` |
| 7 | A | 197,109 / 2,297 | `project_sources/08-chaos-redux-event-planning.md` | `4a1a0a46ffe4` |
| 8 | B | 109,712 / 1,004 | `project_sources/09-chaos-redux-event-assets.md` | `6766e846130e` |
| 9 | B | 80,791 / 833 | `project_sources/10-chaos-redux-events.md` | `42b1c53c5996` |
| 10 | C | 19,635 / 328 | `project_sources/11-chaosx_dynamic_effects.md` | `73b2740ebfb8` |
| 11 | A | 23,695 / 130 | `project_sources/12-chaos-redux-scripted-gui.md` | `f85f0a0888b2` |
| 12 | B | 28,266 / 501 | `project_sources/13-chaos-redux-frame-animation.md` | `86469ff50f33` |
| 13 | C | 98,951 / 1,505 | `project_sources/14-chaos-redux-focus-trees.md` | `74805c1f8522` |
| 14 | C | 34,086 / 698 | `project_sources/15-chaos-redux-debug-playtest.md` | `9c6e27b8a86f` |
| 15 | C | 33,489 / 787 | `project_sources/16-chaos-redux-super-events.md` | `001a899b4b19` |
| 16 | A | 5,362 / 20 | `project_sources/17-chaos_redux_clusters_catalog-5-.csv` | `689fe07883da` |
| 17 | B | 16,848 / 120 | `project_sources/18-chaos_redux_scenarios_catalog-5-.csv` | `8b944de19817` |
| 18 | C | 65,053 / 294 | `project_sources/19-chaos_redux_events_catalog-5-.csv` | `e2e457ba96ae` |
| 19 | root | 11,714 / 192 | `project_sources/20-config.toml` | `24bcac71960d` |
| 20 | root | 2,857 / 42 | `project_sources/21-README.md` | `9f713e2dcaf1` |
| 21 | root | 3,991 / 61 | `project_sources/22-chaosx_dynamic_triggers.md` | `6792ee030cb6` |
| 22 | root | 41,848 / 855 | `project_sources/23-CHAOS_REDUX_MECHANICS.md` | `e3f21aca358f` |
| 23 | root | 12,728 / 373 | `project_sources/25-CHAOS_REDUX_PROJECT_SOURCE_PROTOCOL.md` | `e7d9ac3d70b8` |
| 24 | C | 27,552 / 197 | `project_sources/01-subagents.zip!/chaosx_3d_model_pipeline.toml` | `f0036ce6d12b` |
| 25 | C | 6,414 / 66 | `project_sources/01-subagents.zip!/chaosx_ai_probability_auditor.toml` | `1c3c202e7f15` |
| 26 | A | 3,024 / 58 | `project_sources/01-subagents.zip!/chaosx_asset_source_researcher.toml` | `f652dfac61f3` |
| 27 | C | 8,099 / 87 | `project_sources/01-subagents.zip!/chaosx_country_package_auditor.toml` | `d1c6e1940823` |
| 28 | C | 8,994 / 100 | `project_sources/01-subagents.zip!/chaosx_decision_mission_auditor.toml` | `1b1f9e50909d` |
| 29 | B | 11,319 / 134 | `project_sources/01-subagents.zip!/chaosx_documentation_curator.toml` | `e881bcc4303d` |
| 30 | C | 4,141 / 66 | `project_sources/01-subagents.zip!/chaosx_event_completion_auditor.toml` | `38180484672c` |
| 31 | A | 10,136 / 90 | `project_sources/01-subagents.zip!/chaosx_event_ui_worker.toml` | `56a254896faf` |
| 32 | B | 4,480 / 80 | `project_sources/01-subagents.zip!/chaosx_focus_tree_auditor.toml` | `88149cedcf2d` |
| 33 | A | 3,930 / 72 | `project_sources/01-subagents.zip!/chaosx_generated_event_art.toml` | `d056a89535a8` |
| 34 | A | 10,096 / 117 | `project_sources/01-subagents.zip!/chaosx_icon_artist.toml` | `df0345a30665` |
| 35 | B | 7,229 / 61 | `project_sources/01-subagents.zip!/chaosx_improvement_loop_planner.toml` | `c8bcb04ac81e` |
| 36 | A | 9,782 / 111 | `project_sources/01-subagents.zip!/chaosx_localisation_auditor.toml` | `8d588111bb27` |
| 37 | C | 2,049 / 20 | `project_sources/01-subagents.zip!/chaosx_portrait_creator.toml` | `ea2ae603081f` |
| 38 | B | 13,488 / 235 | `project_sources/01-subagents.zip!/chaosx_repo_explorer.toml` | `276acf0305e8` |
| 39 | B | 5,388 / 74 | `project_sources/01-subagents.zip!/chaosx_scripted_system_architect.toml` | `7c845c07d54d` |
| 40 | C | 3,258 / 45 | `project_sources/01-subagents.zip!/chaosx_skill_maintainer.toml` | `232a9a008c07` |
| 41 | B | 4,605 / 59 | `project_sources/01-subagents.zip!/chaosx_spreadsheet_doc_worker.toml` | `896cb6322248` |
| 42 | A | 3,342 / 65 | `project_sources/01-subagents.zip!/chaosx_super_event_audio_researcher.toml` | `c0e7e0c422f1` |
| 43 | B | 3,921 / 62 | `project_sources/01-subagents.zip!/chaosx_super_event_text_researcher.toml` | `c918dae02f2b` |
| 44 | B | 50,063 / 319 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/SKILL.md` | `f5efeb6e0ecc` |
| 45 | C | 40,856 / 194 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/references/blender-processing-and-export.md` | `d2a4ed570ff3` |
| 46 | A | 12,047 / 37 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/references/reference-images.md` | `badc6d76d959` |
| 47 | A | 18,912 / 88 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/references/start-gates-and-adapter.md` | `2f38a7675eb0` |
| 48 | C | 10,707 / 65 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/references/unit-audio-and-counters.md` | `e6edb855a160` |
| 49 | B | 23,142 / 226 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-3d-model-pipeline/references/unit_rebuild_workflow.md` | `ae01f5d9f7e5` |
| 50 | B | 35,398 / 390 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-ai-strategies/SKILL.md` | `d27d6c1102e3` |
| 51 | B | 12,347 / 206 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-ai-strategies/references/other-ai-systems.md` | `afe9a0a22d55` |
| 52 | A | 17,493 / 154 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-ai-strategies/references/strategy-token-catalog.md` | `8c9b640fae7c` |
| 53 | B | 36,499 / 349 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-characters-leaders/SKILL.md` | `5340d015b0b0` |
| 54 | C | 9,706 / 109 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-characters-leaders/references/effects-triggers.md` | `868406c71a94` |
| 55 | B | 9,766 / 141 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-characters-leaders/references/unit-leader-traits.md` | `8100802fba7c` |
| 56 | A | 6,469 / 78 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-codebase-cleanup/SKILL.md` | `17d5cd60387a` |
| 57 | A | 52,677 / 794 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-debug-playtest/SKILL.md` | `b735c59cb056` |
| 58 | B | 53,438 / 849 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/SKILL.md` | `04ccd1520e1d` |
| 59 | C | 10,066 / 87 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/references/cost-payment-and-localisation.md` | `edaf2de4b6cf` |
| 60 | B | 17,510 / 182 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/references/formables-and-category-presentation.md` | `a6b358b5ecb7` |
| 61 | C | 4,777 / 45 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/references/mechanic-values-and-faction-goals.md` | `fa01621561ce` |
| 62 | B | 5,439 / 34 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/references/validation-addenda-and-handoffs.md` | `89b7a8015c08` |
| 63 | B | 22,750 / 139 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/README.md` | `7160cb17894c` |
| 64 | C | 4,987 / 33 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/category_attachment_audit.md` | `7a6f781e941d` |
| 65 | C | 2,931 / 72 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/static_category_picture_option.md` | `e42dbf180b09` |
| 66 | C | 13,637 / 114 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md` | `53e88cb78065` |
| 67 | A | 8,269 / 72 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/validation_checklist.md` | `360c0836c9b7` |
| 68 | root | 39,782 / 383 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-diplomacy-war/SKILL.md` | `c7ee80a0be46` |
| 69 | C | 12,457 / 150 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-diplomacy-war/references/syntax-reference.md` | `3f488d21d805` |
| 70 | C | 25,156 / 346 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-equipment/SKILL.md` | `fc9a8d2f01a6` |
| 71 | B | 10,978 / 154 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-equipment/references/modular-equipment-and-designer.md` | `5c6006d957a7` |
| 72 | C | 11,293 / 131 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-equipment/references/production-and-stockpile.md` | `98ea5e8948f7` |
| 73 | C | 58,224 / 557 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/SKILL.md` | `eae8e08271c2` |
| 74 | B | 9,084 / 82 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/event-images-and-flags.md` | `28b59a9f86fb` |
| 75 | B | 32,393 / 315 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/icon-and-ui-families.md` | `d786e5fb2b88` |
| 76 | B | 7,104 / 62 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/manifest-and-lineage.md` | `9a006df84775` |
| 77 | A | 21,024 / 135 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/portrait-production.md` | `8d2690da31e8` |
| 78 | C | 11,249 / 110 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/reference-library.md` | `0ddebefc8f44` |
| 79 | B | 4,863 / 30 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-assets/references/unit-visuals.md` | `9ab6970e3015` |
| 80 | root | 52,550 / 702 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/SKILL.md` | `5aa8bd4013ba` |
| 81 | root | 13,911 / 140 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/advanced-chaos-generation-design.md` | `9e5217ac8fa6` |
| 82 | root | 34,057 / 318 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/advanced-country-and-forces-design.md` | `5d0fa02b3f4d` |
| 83 | root | 31,696 / 369 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/advanced-focus-tree-design.md` | `de01708724dd` |
| 84 | root | 1,267 / 9 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/advanced-system-design.md` | `fef80d851d2e` |
| 85 | root | 11,088 / 139 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/player-facing-text-direction.md` | `3cdf7b3946a5` |
| 86 | root | 22,549 / 284 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/presentation-and-assets.md` | `8cc27195ee4b` |
| 87 | root | 40,195 / 434 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-event-planning/references/specification-delivery.md` | `5dc6797ddfea` |
| 88 | A | 50,632 / 549 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-events/SKILL.md` | `95a994715c78` |
| 89 | A | 13,182 / 150 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-events/references/event-log-evolutions-and-clusters.md` | `7dcb982ca162` |
| 90 | A | 4,858 / 31 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-events/references/event-text-formatting-and-details.md` | `64d9ca7a1d15` |
| 91 | A | 37,078 / 316 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-events/references/scripted-systems-and-country-integration.md` | `ee6096a78b07` |
| 92 | C | 8,588 / 103 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-events/references/world-end-triggerable-scenarios-and-aftermath.md` | `428753a0046a` |
| 93 | root | 49,108 / 766 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-focus-trees/SKILL.md` | `7519e58332b5` |
| 94 | C | 16,369 / 146 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-focus-trees/references/layout-and-navigation.md` | `2c70954a0c00` |
| 95 | C | 37,641 / 609 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-focus-trees/references/major-country-design.md` | `cb4ed32d3a6c` |
| 96 | A | 29,729 / 501 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-frame-animation/SKILL.md` | `07a0d6b7e032` |
| 97 | root | 36,171 / 301 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-ideas-modifiers/SKILL.md` | `7c136d082883` |
| 98 | B | 29,088 / 291 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-improvement-loop/SKILL.md` | `1a4d14996738` |
| 99 | A | 39,271 / 360 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-map-states/SKILL.md` | `c0b916d62bbb` |
| 100 | A | 8,680 / 109 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-map-states/references/map-geometry.md` | `06dfae7bb38c` |
| 101 | A | 11,844 / 82 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-map-states/references/state-ledgers.md` | `28e5ce71ebde` |
| 102 | B | 2,637 / 70 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-mtth/SKILL.md` | `3d148f8c8592` |
| 103 | B | 5,176 / 37 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-native-raids/SKILL.md` | `3d146b94582b` |
| 104 | B | 8,279 / 93 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-save-inspection/SKILL.md` | `ef46a62be887` |
| 105 | A | 31,082 / 157 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-scripted-gui/SKILL.md` | `958a7671c4ee` |
| 106 | B | 7,747 / 39 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-shared-git-commit/SKILL.md` | `93f4bc424192` |
| 107 | root | 51,180 / 452 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-subagents/SKILL.md` | `a8ae53cad112` |
| 108 | A | 35,075 / 776 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-super-events/SKILL.md` | `29910f20e0b5` |
| 109 | root | 28,884 / 357 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-technology-doctrines/SKILL.md` | `dd64a493b7a7` |
| 110 | B | 10,092 / 193 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-technology-doctrines/references/doctrine-authoring.md` | `2f3134cb7a58` |
| 111 | A | 8,597 / 119 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-technology-doctrines/references/technology-tree-gui.md` | `c172e78ec882` |
| 112 | root | 41,582 / 412 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-units-divisions/SKILL.md` | `401e66ab9374` |
| 113 | C | 4,566 / 57 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-units-divisions/references/names-stats-visuals.md` | `eb78ab82a652` |
| 114 | C | 8,826 / 131 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-units-divisions/references/naval-air-oob.md` | `5e37a5b38ec1` |
| 115 | root | 7,420 / 74 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-units-divisions/references/runtime-effects-triggers.md` | `947047f15978` |
| 116 | B | 3,131 / 35 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-xlsx/SKILL.md` | `f7fd5443a985` |
| 117 | B | 3,349 / 40 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-xlsx/references/catalog.md` | `4adb7bac59c5` |
| 118 | C | 1,337 / 15 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-xlsx/references/doctrines.md` | `e5bd431395a3` |
| 119 | B | 10,713 / 165 | `upload/all-project-sources(20261023-170917).zip!/.claude/skills/chaos-redux-xlsx/references/preservation.md` | `f673aabdc0fc` |
| 120 | root | 59,777 / 522 | `upload/all-project-sources(20261023-170917).zip!/AGENTS.md` | `7999e656e215` |
| 121 | root | 55,586 / 1,023 | `upload/all-project-sources(20261023-170917).zip!/CHAOS_REDUX_MECHANICS.md` | `21f21df8bf62` |
| 122 | root | 3,421 / 44 | `upload/all-project-sources(20261023-170917).zip!/README.md` | `1b820bf81c43` |
| 123 | C | 5,358 / 20 | `upload/all-project-sources(20261023-170917).zip!/chaos_redux_clusters_catalog.csv` | `e9a728efedba` |
| 124 | A | 70,351 / 296 | `upload/all-project-sources(20261023-170917).zip!/chaos_redux_events_catalog.csv` | `66f6d682b2b3` |
| 125 | C | 19,470 / 137 | `upload/all-project-sources(20261023-170917).zip!/chaos_redux_scenarios_catalog.csv` | `c2c421b12193` |
| 126 | root | 59,641 / 688 | `upload/all-project-sources(20261023-170917).zip!/chaosx_dynamic_effects.md` | `b3ac82d2c2ff` |
| 127 | root | 5,522 / 75 | `upload/all-project-sources(20261023-170917).zip!/chaosx_dynamic_triggers.md` | `a2fb5e8d52d3` |
| 128 | root | 14,250 / 255 | `upload/all-project-sources(20261023-170917).zip!/config.toml` | `b39e25b135e6` |
| 129 | A | 9,501 / 50 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-3d-model-pipeline.md` | `11c5e073780b` |
| 130 | A | 6,787 / 64 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-ai-probability-auditor.md` | `b4b792f78dfe` |
| 131 | A | 2,832 / 56 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-asset-source-researcher.md` | `b1568542d99d` |
| 132 | A | 7,503 / 89 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-country-package-auditor.md` | `ca019b8e81c6` |
| 133 | B | 8,376 / 102 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-decision-mission-auditor.md` | `0a9863762d22` |
| 134 | C | 7,048 / 44 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-documentation-curator.md` | `1b9b52bb0915` |
| 135 | A | 3,844 / 46 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-equipment-units-worker.md` | `56eae9f23b81` |
| 136 | B | 4,014 / 61 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-event-completion-auditor.md` | `5acbac98f307` |
| 137 | C | 7,661 / 44 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-event-ui-worker.md` | `135e3ea565e1` |
| 138 | A | 4,204 / 83 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-focus-tree-auditor.md` | `baacc543ec12` |
| 139 | C | 3,931 / 70 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-generated-event-art.md` | `0f06189f2b36` |
| 140 | A | 10,788 / 127 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-icon-artist.md` | `461c4a2070b1` |
| 141 | root | 6,170 / 63 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-improvement-loop-planner.md` | `3b21f6cff025` |
| 142 | B | 8,934 / 110 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-localisation-auditor.md` | `6fcb3a08221a` |
| 143 | B | 3,405 / 44 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-map-states-worker.md` | `1929ed110dc9` |
| 144 | B | 2,567 / 20 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-portrait-creator.md` | `89c929137cb8` |
| 145 | C | 7,323 / 50 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-repo-explorer.md` | `468b74735033` |
| 146 | A | 5,104 / 76 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-scripted-system-architect.md` | `fd494290f59e` |
| 147 | C | 3,083 / 43 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-skill-maintainer.md` | `fe25fff0c275` |
| 148 | A | 4,523 / 58 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-spreadsheet-doc-worker.md` | `cc29e3177696` |
| 149 | A | 3,367 / 63 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-super-event-audio-researcher.md` | `b3397deb63a9` |
| 150 | C | 3,878 / 60 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-super-event-text-researcher.md` | `cc46361b9558` |
| 151 | C | 3,396 / 44 | `upload/all-project-sources(20261023-170917).zip!/subagents.zip!/chaosx-technology-tree-worker.md` | `e6dd48b4a76b` |
| 152 | root | 2,317 / 34 | `upload/120 - Widespread Mutiny.md` | `7a9f98784faa` |

## Boundary of the reading claim

This record covers the full supplied source corpus represented by these 152 unique hashes. Later technical work used bounded repository excerpts and external historical passages, documented elsewhere in the package. Those later reads are separate evidence with their own scope. This record makes no claim that the complete repository or every external source was read.

The portable JSON retains the names and hashes of the administrative inputs used to assemble this report. Those names identify audit inputs. Internal ledgers, assignment queues, review plans, source bodies and source archives are excluded as separate deliverable files.
