# Documentation cleanup state and resume record

Date: 2026-09-06.
Overall status: incomplete beyond the reviewed coverage below.
The completed documentation repairs are parent-reviewed, across the navigation, instruction, and historical-documentation batches.
Their commits and supporting handoffs are identified below.
This file owns current cleanup routing and status, while dated source maps and reports retain their distinct evidence.

## Authorization and authority

The attached user request authorizes documentation and instruction cleanup, excluding gameplay, localisation, binary assets, catalog workbooks, configuration policy, model selection, permissions, and provider-policy changes.
The parent asked, “May I apply the full-reading requirement separately to each bounded cleanup batch?”
The user answered, “okay, i approve, continue.”
That answer changes the reading workflow only and does not approve an embedded design, deletion, fallback, or protected policy change.
The user-supplied AGENTS.md on 2026-09-06 explicitly makes `gui_rewrite` optional and permits direct application of authorized reviewed GUI edits.
A rewrite failure or rollback alone is no longer a current completion gate or a reason for further fallback approval.
Mandatory inspect, render, and matching before-and-after evidence remain required, and visible defects must be resolved.
This documentation task does not authorize implementing the pending Death dashboard extension.

| Source | What it establishes |
| --- | --- |
| Explicit user decisions and parent acceptance within that scope | Authorization and accepted design, with the decision basis recorded separately from implementation. |
| [AGENTS.md](../../../AGENTS.md), [owning skills](../../../.agents/skills/), and [canonical roles](../../../.codex/agents/) | Repository policy, reusable workflows, specialist boundaries, and required handoffs. Protected conflicts remain explicit below. |
| [Specification index](../../specs/README.md) and package decision evidence | Design sources. A location, date, catalog status, or detailed specification alone does not prove acceptance. |
| [Event overviews](../../events/README.md), [shared systems](../../systems/README.md), and actual source files | Recorded implementation facts for the named source revision. They do not establish approval or live behavior. |
| [Catalog workbook](../../spreadsheets/chaos_redux_events_catalog.xlsx) | Editable catalog source. The CSVs are exports and were not edited here. |
| Named calculations, MCP artifacts, and user live-game evidence | Separate evidence categories. MCP source analysis and previews are not engine execution. Tool exposure, service health, specialist registration, and standalone viewers require separate checks. |
| [Plans index](../README.md) and dated handoffs | Working proposals, dispositions, historical findings, and validation limits. Old execution prompts do not grant current authorization. |

## Completed work and proof

| Batch | Result | Evidence |
| --- | --- | --- |
| Main navigation | Repaired the missing Time Traveler target and added 37 omitted specification-package entry points. All 76 direct specification directories and 65 direct plan directories are linked. Root README, CONTRIBUTING, documentation indexes, and synchronizer guidance distinguish their ownership. | Commit `d156e8ee121e9c3ea9ea91acce221610567b4cb2` and [navigation handoff](subagent_handoffs/2026-09-05_navigation_review.md). Directory coverage is not full reading of interiors. |
| Instructions | Updated AGENTS.md, 14 existing skills, and 10 canonical role instruction bodies. Corrected context isolation, approval evidence, specialist ownership, probability routing, helper paths, and tool/viewer distinctions. MTTH was reviewed without edits. | Commit `7cff54ad5522b2d9a4af6cde063a8028bbf4b8ac`. The ten TOML diffs change instruction text only, preserving model, reasoning, permission, and other fields. |
| Area navigation | Added six event entries, two expanded event-document links, five shared-system documents, and four super-event research links. Kept distinct Event 026/032 root details alongside their folder overviews. Formables/testing received sentence punctuation corrections. | The area continuation in the [navigation handoff](subagent_handoffs/2026-09-05_navigation_review.md) records all 21 curator reads. All six area indexes were fully read by the parent. The achievements index needed no change. |
| Cleanup history | Commit `d21d8fb5c7847929ed9644a33563ad4294125a7f` reconciled 13 root documents and 23 historical handoffs. Preserved dated findings and original missing paths, added current-path annotations, and linked already-applied recommendations to their recorded outcomes. No old map was globally superseded by this narrower ledger. | [Root review](subagent_handoffs/2026-09-05_documentation_batch01.md), [historical A](subagent_handoffs/2026-09-05_historical_handoffs_a.md), and [historical B](subagent_handoffs/2026-09-05_historical_handoffs_b.md). Parent verified the cited helper, ownership, and localisation commits. |
| Catalog review | Fully read all five populated sheets without saving the workbook or running the exporter. Recorded schema, membership, name, severity, and status contradictions for the workbook owner. | [Catalog review](subagent_handoffs/2026-09-05_catalog_review.md). Reviewed SHA-256: `b6de395b4a77fb0f7cb9eaee274195a182b67626cbf5fcc4481ebe2db991acaa`. |
| Runtime documentation | Fixed the two missing generator paths in `.cursor/README.md` and linked the existing destination-write rules. Added a direct cleanup-record link from `docs/README.md`. | Correct paths are `.tools/sync/sync_cursor_agents.py` and `.tools/sync/sync_qoder_agents.py`. Both exist. No synchronizer ran and no generated agent was edited. The fully reviewed Cursor README was pre-existing and untracked, and is included as documentation in this batch. |
| Audio and runtime continuation | Recorded the two missing Event 031 original OGGs, verified both WAV derivatives, and identified protected runtime wording conflicts. | Commit `ee8996e16d0fc4d4d4156e199cceb337ebc837e4` and the existing navigation and instruction handoffs. |
| Settings and Chaos Meter | Commit `729100275be89cf813bc93ed5d38fbacd285c0f0` fully read thirteen documents, repaired seven, and retained an unresolved Deaths overlay contradiction. | [Settings and Chaos review](subagent_handoffs/2026-09-05_settings_chaos_documentation.md). |
| Shared plans | Commit `284f1f77c3ef6c17b16efff6553ee0754ce1f158` fully read twelve historical records and added individual current dispositions without changing their original bodies. Recorded schema, hidden-world-end visibility, and source-gap versus later-runtime claims. | [Shared-plan handoff](subagent_handoffs/2026-09-05_shared_plan_dispositions.md). No design promotion or current engine validation. |
| Shared event-system docs | Commit `86fb03440fea45cec2471e2513fa2476ec1f1182` includes the reviewed eleven-file documentation batch. Full curator and parent reads. Corrected the 82-row claim to the retained 75-row matrix, separated historical MCP results, and exposed specific contract conflicts. | [Shared-event review](subagent_handoffs/2026-09-05_shared_events_documentation.md). No formula, gameplay value, or scenario identity was changed. |
| Events 001 to 005 | Commit `f1e06718ff9268b2fb577ea3525725177bb7815b` contains repairs to seven of eight fully read documents, preserving historical timing, licensing, animation, and release-cause evidence. Marked the Soviet focus-rewrite recommendation and Holy Realm terminal-audio proposal unresolved. | [Early-event review](subagent_handoffs/2026-09-05_events_001_005_documentation.md). Event 004 is unchanged by this task. |
| Events 007 to 010 | Review-branch commit `f38c2e99d68861669965f8e60fc188f7ce0bc73d`. Four full curator and parent reads. Corrected White Peace option-settlement ownership, distinguished existing Atlas source from the historically blocked shared extension, recorded missing archives, and removed exact duplicate Fury asset entries. | [Four-event review](subagent_handoffs/2026-09-05_events_007_010_documentation.md). Current Atlas inspection is source evidence with visible and dynamic-value findings, not visual acceptance. |
| Events 011, 013, and 014 | Review-branch commit `f38c2e99d68861669965f8e60fc188f7ce0bc73d`. Three full curator and parent reads. Attributed frozen completion claims, exposed missing source archives, corrected the March Predation modifier wording, and preserved historical GUI recovery evidence. | [Three-event review](subagent_handoffs/2026-09-05_events_011_013_014_documentation.md). No gameplay value, workbook, or asset changed. |
| Events 015 through 018 | Four full curator and parent overview reads. Parent corrected the Event 015 display range cited by Event 016, annotated three absent source workspaces, attributed frozen completion claims, and preserved mandatory GUI evidence requirements. | [Four-event continuation04 review](subagent_handoffs/2026-09-06_events_015_018_documentation.md). All four current root traces are partial, and package-interior reading limits remain explicit. |
| Inherited asset reference rule | Review-branch commit `4d069dfb3db3e54f5f9b749f694e564e85e25da5`. Added one reusable paragraph to the existing asset skill after matching vanilla GFX and shader evidence. Parent proved every baseline byte outside the 563-byte insertion is preserved. | [Asset-reference skill handoff](subagent_handoffs/2026-09-05_asset_reference_skill_check.md). Literal Lua paths and inherited DDS files require owner lookup before a missing-resource claim. |
| GUI prose and workflow | Parent-reviewed installed-contract audit and punctuation repairs in the GUI skill and event UI worker instruction body. | [GUI workflow handoff](subagent_handoffs/2026-09-05_gui_workflow_review.md). No instruction behavior or protected TOML field changed. |
| Nested Event 046/047 tree | Fully read 51 nested Markdown files and 51 counterparts. Every pair was text and SHA-256 identical, with no nested-only requirements or evidence. | The navigation handoff records all 51 pair hashes. Added a retained-mirror notice, canonical links, six plan dispositions, and supported Codex transport and explorer routing. All 51 mirror sources remain unchanged. No design approval was inferred. |

The `d21d8fb` documentation batch contained 60 Markdown files, including 16 additions to Git.
Eleven additions preserve fully reviewed pre-existing untracked documents, and five are the new source map, three cleanup handoffs, and retained-mirror README.
Unrelated staged event-index entries and Event 026 retirement edits remain outside this commit.
All 298 relative link targets in the final candidate resolved against the working tree, including retained untracked package dependencies.
The commit does not track every referenced package file.

The historical evidence checks preserved all 23 handoffs' fenced code blocks, complete `hoi4-agent` artifact URI multisets, and named probability scenarios against the captured baseline.
The old Event 006 incidents filename remains historical text beside a related current path, without an inferred rename.
The world-threat documentation already uses `014_cannibalism_effects.txt` at the two cited locations, so its old path-fix recommendation is resolved independently of broader behavior questions.

## Reading coverage

These are full reads by the named worker or parent, not inventory or search results.
Overlapping files between batches are not additive unique-file counts.

| Read set | Coverage and limit |
| --- | --- |
| Original instruction baseline | AGENTS.md, 15 original skill entrypoints, and 20 canonical role TOMLs were fully read. Parent reviewed final task-specific changes. The concurrent sixteenth scripted-GUI skill and later migration lines were preserved but excluded from this review. |
| Cleanup records | All 13 existing root documents and 23 historical handoffs were fully read before editing. Parent reviewed the three new handoffs and their changes. |
| Main package navigation | 37 omitted specification entry documents were fully read, plus the existing Time Traveler README and main indexes. Package interiors outside the nested comparison were not reconciled. |
| Area navigation | Parent read six area indexes. Curator read 21 files, comprising three of those indexes and 18 supporting entries. Exact paths are in the navigation handoff. |
| Nested comparison | All 51 files beneath `docs/specs/docs/` and their 51 exact counterparts were fully read. That includes six plans and 45 specification-package files per tree. |
| Shared-event continuation | All eleven event-system documents were fully read by the curator and then parent. The handoff distinguishes original hashes, source descriptions, reported MCP artifacts, and unresolved acceptance. |
| Shared-plan continuation | All twelve records listed in the shared-plan handoff were fully read by the parent. Original bodies and named MCP evidence were retained. |
| Settings and Chaos continuation | All six settings and seven Chaos Meter documents were fully read directly by the parent. Seven received prose, navigation, or evidence-boundary repairs. |
| GUI workflow continuation | Fully read the sixteenth GUI skill, event-UI worker, shared subagents, decisions and events skills, and the GUI visual-review reference. Inspected package contracts are separately identified as full or partial reads in the GUI handoff. |
| Early-event continuation | All eight original documents were fully read by the curator. Parent reviewed and corrected the source deltas. Together with the settings, shared-plan, and shared-event sets, continuation02 covers 44 source documents. This does not count package interiors as read. |
| Event-entry continuation03 | All seven original overviews were fully read by curator and parent, bringing the two continuation source sets to 51 documents. Curator-reported authority-tree reads are listed in their handoffs and are not blanket reconciliation of those interiors. Parent fully read the existing Atlas GUI, scripted GUI, and historical shared-dashboard blocker. |
| Event-entry continuation04 | All four original overviews were fully read by curator and parent, bringing continuation02 through continuation04 to 55 source documents. Curator fully read the named Event 015 authority documents and recorded Event 016 through 018 dependency excerpts and inventories. Parent fully read two super-event constant files and identified all other source checks as narrow excerpts. |
| Runtime configuration continuation | Fully read `.codex/config.toml`, `.qoder/mcp.json`, `.cursor/mcp.json`, and `.cursor/rules/chaos-redux-cursor-runtime.mdc` without edits. The instruction handoff records their hashes, 20 resolved role paths, and protected stale instructions. |
| Event 031 audio continuation | Fully read the audio note and owning super-event skill. Verified two derivative hashes and WAV headers. Original recording files were absent and could not be read. |
| Catalog | All populated cells in Events, Clusters, Cluster Memberships, Scenarios, and Legend were fully read in the reviewed workbook revision. No workbook edit or export was performed. |
| Earlier broad discovery | About 8,477 files and 90 MB were inventoried in an earlier pass. This is a lower-bound inventory, not a complete source read or an immutable snapshot. Most remaining project documentation, reference libraries, and configuration remain outside the verified reading sets. |

At integration of `d21d8fb`, the workbook SHA-256 was `ac7d7d9848d2fb1ea51e1541d61939d395362a82948f618844c5cb9cfc669aa5`, different from the catalog review revision.
This cleanup did not write the workbook.
The recorded catalog findings apply to the earlier hash and were not re-audited after concurrent workbook changes.

The implementation-facing docs reached through navigation were read for their role and evidence limits, without a current gameplay, asset, balance, or live-engine audit.
The empty `docs/events/028_asteroid_incoming/` directory had no entry to read.
The Event 031 audio continuation fully read `docs/super_events/031_random_terror/audio_research.md`.
The expected original recordings are absent from its empty `audio_sources/` directory.
Both runtime WAVs match the recorded hashes and 110-second stereo PCM16 format, but source-to-derivative reproduction remains blocked by the missing originals.
The [navigation handoff](subagent_handoffs/2026-09-05_navigation_review.md) records the exact search and validation limits.

The shared-event commit isolates task edits from inherited uncommitted cluster and scenario changes.
A few count and punctuation corrections inside those inherited sections remain in the working tree, as recorded in the shared-event handoff.
The early-event commit likewise excludes the inherited Event 023 custody-bridge section in the Event 005 overview, including one punctuation repair that remains with its owning work.
The continuation03 review commit also excludes inherited Fury, Diplomacy, and Natural Disasters cluster-contract changes. A punctuation repair in the inherited Diplomacy paragraph remains with that work.
Continuation04 likewise excludes the inherited Event 017 cluster-contract replacement. Its older tracked wording is not promoted as current accepted design by this isolation.
Their presence does not mean those larger sections were committed or accepted by this cleanup.

## Root-plan dispositions

These dispositions apply to the 13 root documents, preserving their dated facts.
Historical implementation evidence does not supply an acceptance decision.

| Document | Type | Disposition | Basis, evidence, or blocker |
| --- | --- | --- | --- |
| `chaos_redux_multi_system_fix_spec.md` | Historical design proposal | Unresolved | No explicit acceptance basis for the proposed mechanics is recorded in the current scope, and current source and MCP evidence does not promote the proposal. |
| `chaos_redux_repo_cleanup_goal_prompt.md` | Historical goal prompt | Superseded by `documentation_state.md` for current task routing | The prompt records an earlier broad goal. Its text remains for provenance and does not grant new authorization. |
| `chaos_redux_repo_cleanup_master_prompt.md` | Historical cleanup prompt | Superseded by `documentation_state.md` for current task routing | The prompt preserves the earlier broad contract and safety rules. Current work is parent-assigned and batch bounded. |
| `decision_category_presentation_audit.md` | Dated presentation audit | Unresolved | The 2026-08-09 table and `Complete` labels are historical observations. Current source, asset, and GUI MCP evidence was not re-established in this batch. |
| `event_003_006_bounded_cleanup_2026-08-22.md` | Dated implementation report | Historical implementation record with current status unresolved | The report preserves its partial Event 003 MCP artifact and dated source findings. Current implementation and runtime behavior require current evidence. |
| `event_013_020_bounded_cleanup_2026-08-22.md` | Dated implementation report | Historical implementation record with current status unresolved | The report preserves its bounded source findings and timed-out Event 020 MCP attempt. Current implementation and runtime behavior require current evidence. |
| `gfx_icon_flag_mapmode_cleanup.md` | Historical asset registry | Unresolved current asset status | Asset paths and wiring statements are retained as historical evidence. Current asset availability, consumer resolution, and visual acceptance were not revalidated. |
| `git_storage_cleanup_2026-08-22.md` | Dated storage report | Historical implementation record with current status unresolved | Counts, deletions, and checks apply to the 2026-08-22 and 2026-08-24 runs. Current Git and LFS state was not rechecked. |
| `interface_audit_2026-07-22.md` | Dated GUI audit | Blocked | A fresh `hoi4.gui_inspect`, render, and comparison pass is required before current GUI layout or consumer claims can be made. |
| `README.md` | Documentation index | Implemented for current navigation | It now points to this ledger and the current handoff and labels the root prompts and completion report as historical records. |
| `repo_cleanup_completion_report_2026-08-22.md` | Dated completion report | Historical completion record with current status unresolved | Its bounded tranche and dated validation facts are preserved. Later concurrent changes and missing current evidence prevent a present completion claim. |
| `shared_system_migration_plan_2026-08-22.md` | Active deferred migration plan | Blocked | The dated queue requires current parent acceptance, usable Event 006, Event 019, and shared Event Log MCP evidence, plus a scenario-specific probability auditor inspect and compare pass before migration status can be promoted. |
| `systems_documentation_reorganization_2026-08-22.md` | Dated documentation report | Superseded for current navigation by `2026-09-05_navigation_review.md` | The 2026-08-22 move and link facts remain historical evidence. Current index coverage is governed by the parent navigation commit and handoff. |

The 23 historical handoffs have individual dispositions in the A/B reviews linked above.
Their recorded implementations remain historical, while current source, acceptance, and validation questions remain unresolved where no new evidence exists.
The six Event 046/047 plan dispositions are recorded in their owning canonical files, with acceptance claims unresolved and implementation evidence gates retained.
No proposal was promoted into an accepted specification by this cleanup.
No document or asset was deleted, and no distinct source requirement was discarded to simplify a design.

## Protected conflicts and remaining checks

| Issue | Exact decision or evidence still required |
| --- | --- |
| Generated-role synchronization | AGENTS.md requires propagation from canonical TOMLs and also protects Qoder and generated Cursor files from this runtime. An explicit destination-write decision is needed before synchronization. Generated consistency is not claimed. |
| Source and production policies | Portrait-placeholder finality, grounded final ownership, 3D reference/refinement and rigging routes, animation approval, flags, advisor review, and source-reading exceptions differ across some roles and skills. Preserve the exact conflicts in the [instruction review](subagent_handoffs/2026-09-05_instruction_batch01.md), [remaining roles](subagent_handoffs/2026-09-05_remaining_roles.md), and [asset skills review](subagent_handoffs/2026-09-05_skills_assets.md). No more-permissive version was selected. |
| Paid work and live QA | Provider recovery confirmation, the live-QA skill versus user-only game testing, and related invocation or audit rules need their recorded owner decisions. No paid operation, game launch, log search, or autonomous test occurred. See the instruction and [other-skills review](subagent_handoffs/2026-09-05_skills_other.md). |
| Engine and workflow interpretation | Duration constants/variables, event-target usage, focus reward exceptions, and planning cadence or source-mode differences remain at the limits recorded by [gameplay skills](subagent_handoffs/2026-09-05_skills_gameplay_docs.md) and [planning skills](subagent_handoffs/2026-09-05_skills_planning.md). They were not resolved through source-only assumptions. |
| MCP capabilities | GUI and technology route metadata and the installed 3.0.8 package were reviewed. No dedicated standalone Technology Tree Viewer launcher was found within that package. This is a package gap, not machine-wide absence. The GUI workflow audit itself made no execution call. Later curator closeouts returned diagnostic GUI inspections, partial event evidence, and an incomplete zero-candidate probability pool, recorded in the settings, shared-plan, and shared-event handoffs. No clean render, evaluated probability comparison, or live-game acceptance follows. |
| Workbook contradictions | In the reviewed workbook revision, Events had 13 visible columns versus 14 table/export columns. Clusters had 8 columns but the exporter emitted 7 and omitted Status. Exact status-validation, identity, membership, slot, and Event 39 detail issues are in the catalog review. Workbook/exporter changes require their own authorized scope and accepted wording. |
| Package acceptance and identities | Detailed specs and old status labels do not approve Event 043 identity changes, proposed SCN-015 uses, Event 046/047 cluster IDs or membership severity, or conflicting supplied scenario-row counts. Retain explicit unresolved dispositions. |
| GUI workflow review | The owner skill, event-UI role, required cross-skill inputs, and visual-review reference were fully read and parent-reviewed. No behavior repair was justified. The [GUI workflow handoff](subagent_handoffs/2026-09-05_gui_workflow_review.md) records installed-contract evidence and a separately parent-reviewed punctuation cleanup with preserved literals and protected TOML fields. This closes the named excluded-read boundary without accepting GUI layout or live behavior. |
| Runtime configuration wording | The Cursor runtime rule names the missing old generator path. The Codex UI-worker registration describes the older decision-layout owner, and its 3D registration/approval language differs from AGENTS.md. Exact protected follow-ups are in the instruction handoff. No configuration or paid-work policy was changed. |
| Audio archive recovery | Two Event 031 original OGGs are absent. Recover the exact bytes matching the recorded source hashes, or review a replacement source and conversion lineage. Existing derivative identity does not supply missing source provenance. |
| Newly reviewed archive and presentation gaps | Events 007, 008, 009, 010, and 011 have missing named source archives. Event 013's restored-source claim conflicts with current absence. The two continuation03 handoffs preserve deletion history and current source limits. Atlas inspection reports footer overflow, unresolved text and fallback linkage, and other findings. Its source-graph success does not close these issues or the historical shared-dashboard extension. |
| Continuation04 source and evidence gaps | The Event 015 manifest, Event 017 archive, and Event 018 temporary workspace are absent. Missing source workspaces do not prove runtime asset loss or completed source promotion. Four new event-root traces returned partial evidence at revision `d845f43c97099a029173014ead16d7eef197a0351971daad8dc5c946aec7fb38`, with deferred workspace-wide helper and lifecycle analysis. No current event-wide, GUI, technology, focus, probability, or asset acceptance follows. |
| Broader coverage | Unreviewed event/system packages, active addenda, manifests, asset archives, skill-local references, and configuration still need bounded full reads and evidence-backed dispositions. The whole documentation cleanup remains incomplete. |

## Resume without repeating completed work

1. Preserve the completed instruction, navigation, historical, catalog-read, and nested-comparison batches recorded above. Keep all retained mirror files intact.
2. The eight Events 001 to 005 entries and companions are reviewed at the documentation boundary in their handoff. All four continuation02 curators have closed. Their exact read ledgers and available diagnostic evidence are retained in the owning handoffs. Do not repeat their repairs or interpret retained package completion claims as fresh validation.
3. Events 007 to 018 are reviewed at the specific overview boundaries in the continuation03 and continuation04 handoffs, excluding Event 012. Their curators have closed. The next overview entries are `docs/events/019_infantry_spawn/overview.md`, `docs/events/020_black_plague/overview.md`, and `docs/events/021_random_civil_war/overview.md`. These three paths are inventory-only. Event 016 companions `evolutions.md` and the systems named in the continuation04 handoff, Event 017 authority interiors, and Event 018 `assets.md`, `cave_country.md`, `helper_contracts.md`, super-event overview, and achievement guide still require their recorded full reads. Event 006 and Africa retain concurrent implementation work and remain outside these entry batches.
4. Resolve the Event 031 missing-original archive gap through the audio owner. The note and derivative file evidence are already reviewed, so do not repeat those reads as an unexplored navigation task.
5. Use `docs/specs/046_the_great_shuffle_specs/matrices/046_source_conflict_ledger.md`, `docs/specs/047_boom_specs/047_boom_source_reading_ledger.md`, and the catalog review for the unresolved identity/schema decisions. Their recorded snapshot counts are not current workbook facts.
6. Resolve protected role/skill and cross-runtime conflicts through explicit decisions recorded in the existing handoffs. Do not change settings or source restrictions to unblock cleanup.

Skills used across the cleanup: chaos-redux-subagents, skill-creator through the skill maintainers, and xlsx for the read-only catalog review.
This continuation also used chaos-redux-super-events for the audio note, plus the GUI, events, and decisions skills through their documentation reviewers.
The asset-reference follow-up used the existing event-assets skill and official skill-creator guidance through the skill maintainer.
Fifteen existing skills were updated across the cleanup, MTTH was reviewed unchanged, and this cleanup created no new skill.
No design or production simplification was introduced within the completed edits.
The unread coverage, unperformed current engine checks, unresolved acceptance, protected-policy decisions, and blocked synchronization above are material omissions from any repository-wide completion claim.

## Pending Git integration at this checkpoint

The continuation03 seven-overview batch and inherited-asset skill paragraph are parent-reviewed and preserved as separate commits on `codex/documentation-cleanup-review-20260906`.
The review branch was created through private-index commit trees and a new branch reference, without writing the shared Git index or moving the working branch.
Their selective candidates are prepared separately from unrelated staged work and inherited cluster-contract changes.
The shared `.git/index.lock` appeared outside this task with modification time `2026-09-05 07:56:30 UTC` and prevented the commit transaction.
A read-only Windows Restart Manager query returned no open owner handles, but that does not establish whether another task still owns the coordination lock.
This task did not remove or overwrite it.
A 2026-09-06 recheck observed a zero-byte lock with creation and modification time `2026-09-05 09:55:11 UTC`, differing from the earlier recorded timestamp.
Two `git.exe` processes running `add --sparse --pathspec-from-file=- --pathspec-file-nul` were also present, without proof that either owned this lock.
HEAD was `302e73478b6ca51b425360267329099248072196`, with no committed changes to the pending batches' owned paths since their recorded baseline.
The authority annotations for Events 010 and 011 and both related handoffs were refreshed under the current user instruction.

Prepared manifests are `C:/Users/klimp/.codex/visualizations/2026/09/04/01a06e33-dc56-78e3-a787-850360234143/documentation_review/continuation03/event_entries_commit/manifest.json` and the sibling `skill_commit/manifest.json`.
The review branch records event-entry commit `f38c2e99d68861669965f8e60fc188f7ce0bc73d` first and asset-skill commit `4d069dfb3db3e54f5f9b749f694e564e85e25da5` second.
Before integration into the shared working branch, compare current HEAD and staged entries with the recorded baselines and preserve every unrelated change.
Re-review overlapping changes if the owned source blobs advanced.
The review commits do not establish integration into the working branch.
Post-commit review found concurrent asset-skill changes to animated-unit and armed-unit motion-source policy and completion item 31.
They remain outside this cleanup and outside its asset-reference commit.
The asset-reference handoff records this additional selective-integration boundary.
Continue documentation review from the next-file list while shared integration remains pending.

The continuation04 overview repairs use the same review branch and preserve their original snapshot at `documentation_review/continuation04/baseline/manifest.json` in the external review workspace.
A later 2026-09-06 check found the shared index lock absent.
Shared integration still requires a current-HEAD merge and preservation of unrelated staged entries before it can be claimed.
