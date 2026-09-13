# Chaos Redux main-menu startup repair

Status: complete for the requested main-menu startup scope.
Cycles 03 and 04 both reached the responsive Chaos Redux main menu with zero-byte fresh error and text logs, remained clean for more than 60 seconds after the recorded menu observation, and loaded an unchanged final source batch.
The final HOI4 process, PID 21172, remains open at the menu.
The final cycle records supersede earlier handoff sections that still describe parent startup acceptance as pending.

## Requested scope and evidence

The user authorized autonomous debug launch, crash repair, removal of every error emitted while loading the main menu, and as many relaunches as necessary.
The user excluded computer control and prohibited Astra subagents during the run.
The parent stopped all then-running Astra workers and completed the remaining script/model work directly; the other bounded specialists used their non-Astra configurations.
No mouse input, keyboard input, in-game console command, campaign, or save was used.
Only the verified existing HOI4 shortcut and the recorded game PIDs were operated.
See `coverage.md` and `setup_commands.md` for the exact scope and launch boundary.

| Cycle | PID | Startup error log | Main-menu evidence | Result |
| --- | --- | --- | --- | --- |
| 01 | 18396 | 2,288 lines / 394,673 bytes after stop | None; stopped for source repairs | Parser/material/model repair baseline |
| 02 | 14720 | 651 lines / 115,264 bytes after full startup validation | `screenshots/cycle_02_window.png` | Responsive menu; stopped for remaining repairs |
| 03 | 2652 | 0 bytes, including after close | `screenshots/cycle_03_window.png` | Clean for another 99 seconds at menu; closed for confirmation |
| 04 | 21172 | 0 bytes; text log also 0 bytes | `screenshots/cycle_04_window.png` | Clean for another 95 seconds at menu; left open |

The early cycle 02 snapshot contained 446 lines; the final archived 651-line log includes later database validation and is the authoritative record.
The reported original crash was not independently reproduced before cycle 01 was stopped for the first repair tranche.
Completion is based on observed fresh, responsive, error-free loads rather than a claim that a single crash cause was isolated.
No newly produced crash is treated as an old crash folder, and old crash artifacts do not count as failures of the current cycles.

## Repairs and preserved behavior

| Surface | Repair and useful validation |
| --- | --- |
| Camp administration and CBRN payloads | Replaced rejected parameterized static payloads with exact explicit helper contracts; corrected documented political-power and dynamic-modifier syntax. Expanded-body comparisons preserve the original effects and caller inputs. See `camp_repair_handoff.md` and its contract proofs. |
| Script effects, scopes, and lifecycles | Corrected invalid comparisons, missing helper calls, unsupported local-target clears, temporary-variable scope mistakes, resource/building static-field injection, and selected-target readiness protocols. Transactions retain cost, attribution, cleanup order, and existing branches. See the script handoffs and byte backups. |
| Constants, synchronized tokens, and equipment enums | Registered missing exact consumer keys and synchronized runtime IDs; corrected wrong constant categories and installed equipment identifiers. No unrelated tuning value was redesigned. |
| Decisions and Antarctic missions | Preserved the original cost/gate/spend/factory contracts using same-value parser-supported aliases, corrected equipment tokens, and registered all seven existing Antarctic categories with their actual scripted-GUI entry point. Existing mission consumers remain wired. See `decision_repair_handoff.md`. |
| Focus icons | Registered 91 genuine vanilla-style animated shine sprites covering all 107 reported focus consumers; removed five unsupported description fields while retaining their standard localization. Routes, rewards, positions, and AI remain unchanged. Focus MCP inspection/render and cycle 02 show the targeted shine/description faults gone. |
| Localization | Corrected selector syntax and variable predicates, supplied the missing meter/category labels, and resolved eight duplicate portal keys to the actual canonical strings. See `localisation_repair_handoff.md`. |
| Country references | Corrected ideology subtype tokens, active-leader existence checks, and exact installed technology IDs. Runtime commander assignment uses the two existing characters' documented nationality transfer, preserving their portraits and corps roles. See `country_repair_handoff.md`. |
| DLC-gated game rules | Registered five native default rule objects and retained the native DLC gate on all 42 non-default options. The parent independently compared each native payload, all options, and original comment bytes. See `startup_game_rules_preservation_check.json` and the handoff. |
| Doctrine geography | Replaced five invalid STATE-scoped terrain checks with native controlled-state membership checks over exact current-map arrays. The independent join covers 1,081 states / 13,414 provinces; its source hashes match the researcher's values. Country control and all score additions are preserved. See `startup_terrain_research.md`. |
| Model palette, shaders, and textures | Installed a matching 50-bone alien mesh and all seven genuine skeletal actions; 703 motion samples and actual runtime mesh comparisons preserve geometry, materials, and retained attachment matrices. Corrected the robot double-skinned shader lookup and embedded texture references in 17 registered meshes, plus nine byte-identical texture renames. See `model_repair_handoff.md` and its receipts. |

The source file ledger is `source_repair_inventory.json`.
It compares the task-owned backups with the final files and records binary hashes and identical-byte renames.
Its 150 path records cover 125 modified existing files, seven task-created source/documentation files, and nine byte-identical texture renames with their nine removed old names.
`repair_ledger.json` retains every observed baseline diagnostic message group, including log summaries, against the two empty final fresh error logs.
`source_repairs.patch` is a readable logical text diff with newline/BOM representation normalized; the backups and SHA-256 values remain the byte-level evidence.
The Event 039 focus-effect baseline is reconstructed by reversing three unique substitutions rather than being a captured original; the country handoff explicitly records this evidence limit.
The pre-existing tracked workspace patch and status are preserved under `baseline/`; unrelated user drafts were not reset or removed.

## Weighted logic and MCP limits

No balance redesign, new numeric chance, score addition, or threshold was introduced.
The Random Terror incident pool retains 158 tickets, and the scenario/raid pools retain their exact original 100-ticket distributions.
The probability auditor captured the complete incident baseline and bounded same-scenario comparisons; its final handoff records exact artifacts, declared fixtures, and unresolved direct dynamic-variable binding limitations.
Incident, scenario-pattern, and high-raid declared-pool comparisons report zero changes; low/mid comparisons returned without an exposed retained `comparisonChanges` field, so that field is not treated as a pass.
The inline declared-pool projections are narrower audit evidence than the full live-source call graph and are explicitly reported as an audit simplification.
Source scenario contracts also cover the corrected leader, opinion, technology, controlled-terrain, target-readiness, and current zero-VP predicates.
They do not establish campaign behavior that was not exercised.

Focused Event MCP inspection and rendering returned partial graphs because helper/lifecycle projections were deferred.
Several post-edit Event/technology comparisons failed with `Transport closed`, `EVENT_REVISION_NOT_CACHED`, or `EVENT_GRAPH_ARTIFACT_INVALID`; these are recorded as tool limitations, not successful engine validation.
The technology viewer package was not assumed to exist from exposed inspector routes.
The verified Blender adapter CLI reported 1.10.49 while cached exposed MCP health still reported 1.10.48; the parent used the verified CLI for the retained repaired checkpoint and export/reimport operations.
The required project skill's referenced generic playtest skill is absent and recorded in `coverage.md`.

Read-only inspection of the existing Antarctic GUI also reports missing font/element/localization references, and the broader map inspector reports floating-harbor position errors.
Those inspectors cover dormant/campaign surfaces outside the requested main-menu run; no full GUI or map-position completion is claimed.
The fixed current-zero-VP predicate remains exact for its existing zero threshold; arbitrary future VP thresholds require separate implementation review.

## Simplifications, omissions, and blockers

No gameplay, model, action, material, cost, route, mission, or AI weight was deliberately removed or simplified to clear the startup log.
Campaign execution and in-campaign visual/audio checks are outside the requested scope.
The partial/unavailable MCP evidence, reconstructed three-substitution focus backup, and map-derived arrays' regeneration requirement remain explicit validation limits.
They do not substitute for or invalidate the final recorded fresh main-menu engine result.

## Documentation, skills, and Git

The parent reviewed the camp, script lifecycle, decision, focus, localization, country, game-rule, model, terrain, and probability handoffs against their preserved source evidence.
This report and final cycle observations supersede earlier parent-relaunch pending statements without promoting unrelated design proposals.
The Holy Realm recovery retains the recorded Tibet-first behavior; the shared load-aware fixed-host proposal remains unresolved in its recovery handoff.

Skills used: `chaos-redux-debug-playtest`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-scripted-gui`, `chaos-redux-event-assets`, and `chaos-redux-3d-model-pipeline`.
No skill was created or updated for this startup-specific run.
Existing affected source files contain substantial pre-existing uncommitted user work.
Their task-only deltas are recorded in `source_repairs.patch`, and the installed runtime fixes remain in the shared working tree.
The task's Git commit records only newly created repair evidence, logical deltas, handoffs, and cycle observations so it does not absorb those existing source drafts.
Its receipt is `git_commit_receipt.json`.
