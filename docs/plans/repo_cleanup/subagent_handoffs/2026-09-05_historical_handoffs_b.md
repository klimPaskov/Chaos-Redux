# Historical handoffs cleanup B

Date: 2026-09-05

Status: bounded documentation-only cleanup handoff for eleven historical handoffs. Parent review and final integration remain outstanding. No gameplay files, localisation source, workbook, CSV, MCP, or generated-agent source was changed by this pass.

## Ownership and scope

This subagent owned writes to the eleven existing files named below and to this handoff. No other files were edited.

- `focus_cleanup_baseline_2026-08-22.md`
- `focus_cleanup_events_1_20_2026-07-29.md`
- `localisation_cleanup_2026-07-29.md`
- `localisation_cleanup_baseline_2026-08-22.md`
- `localisation_cleanup_patch_2026-08-22.md`
- `remaining_safe_cleanup_2026-08-24.md`
- `repo_map_2026-08-22.md`
- `shared_helper_architecture_baseline_2026-08-22.md`
- `shared_helpers_audit_2026-07-29.md`
- `spreadsheet_cleanup_alignment_2026-08-22.md`
- `spreadsheet_cleanup_alignment_followup_2026-08-22.md`

No file was deleted. Concurrent changes in other handoffs were preserved, including the pre-existing changes in `shared_helpers_audit_2026-07-29.md`. The root documentation curator owns the root documentation set and `documentation_state.md`, so this handoff does not duplicate that source map or resume packet.

## Required reading and full-read count

The repository `AGENTS.md` and `.agents/skills/chaos-redux-subagents/SKILL.md` were read before editing. The offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding were read. The installed vanilla documentation Markdown files were read in full for the required source-reference context.

All eleven assigned handoffs were read in full before editing. Exact full-read count: 11 of 11. Unread assigned files: 0.

The supplied batch baseline under `C:\Users\klimp\.codex\visualizations\2026\09\04\01a06e33-dc56-78e3-a787-850360234143\documentation_review\batch01_baseline\files` was used for comparison. The eleven assigned baseline copies matched the repository versions before this cleanup began.

This pass used no new MCP call because the parent authorized structural prose and reference cleanup without engine-behavior reconciliation. Existing MCP artifact references and their dated limitations remain in the handoffs. No MCP health, viewer availability, route completion, or gameplay status is claimed here.

## Exact edits

| File | Exact cleanup |
| --- | --- |
| `focus_cleanup_baseline_2026-08-22.md` | Added a dated-evidence notice, retained the report's `common/events` scan claim with a current correction that `common/events` is absent and `events` exists, recorded that historical traversal of `events` is unverified, marked the scope wording as historical, and required a recorded acceptance basis before route reflow or loader changes. Removed authored semicolons while preserving artifact references and structural facts. |
| `focus_cleanup_events_1_20_2026-07-29.md` | Added a dated-evidence notice, changed snapshot findings that were labelled current or latest to audited-snapshot wording, removed acceptance language that lacked a recorded basis, and kept the Event 003, Event 005, Event 012, Event 019, and Event 020 risks distinct. Removed authored semicolons. |
| `localisation_cleanup_2026-07-29.md` | Added the missing date and dated-evidence notice, retained the old Event 006 and Fallout paths as historical facts with named consolidated replacements, updated the Fallout selector evidence to the later consolidated anchor, and required an explicit acceptance basis for future design changes. |
| `localisation_cleanup_baseline_2026-08-22.md` | Added a dated-evidence notice, recorded the Event 5 duplicate-file retirement as implemented by `remaining_safe_cleanup_2026-08-24.md` and commit `0587e680c3`, recorded the Event 011 fallback replacement by `localisation_cleanup_patch_2026-08-22.md` and commit `9cfec72b3`, and converted the remaining wording instruction into an owner-decision item. The sourced semicolon in the General Rules attribution was preserved verbatim. |
| `localisation_cleanup_patch_2026-08-22.md` | Added a dated-evidence notice and changed current-sounding selector and scan descriptions to post-patch or audited-tree wording. |
| `remaining_safe_cleanup_2026-08-24.md` | Replaced the em dash in the title, added a dated-evidence notice, and changed current-sounding wording to the comparison tree or named canonical source. The Event 5 deletion and Event 14 comment evidence remain intact. |
| `repo_map_2026-08-22.md` | Converted the top note into a dated snapshot note, retained the 2026-08-24 workbook and README findings as dated facts, changed old current-state labels to snapshot wording, and preserved the map as a dated source map rather than treating it as globally superseded. |
| `shared_helper_architecture_baseline_2026-08-22.md` | Added a dated-evidence notice, recorded ownership clarification by commit `775099cbfa`, recorded removal of `modify_value_based_on_chaos_tier` by commit `2f529cc54c`, removed that retired helper from the remaining proof instruction, and retained the dated world-threat path recommendation alongside the targeted current check that confirms its correction. Broader wrapper wording remains unresolved. |
| `shared_helpers_audit_2026-07-29.md` | Preserved the concurrent Event 026 retirement changes, added a dated-evidence notice, and changed current-sounding call-site and definition wording to inspected-tree wording. |
| `spreadsheet_cleanup_alignment_2026-08-22.md` | Added a dated-evidence notice, replaced em dash field separators with colons, and described the premise text and exporter results as evidence from that workbook pass. |
| `spreadsheet_cleanup_alignment_followup_2026-08-22.md` | Added a dated-evidence notice, replaced em dash field separators with colons, changed the key column to audited-tree wording, and removed current-status language from the Event 012 and Event 019 result descriptions. |

## Source-of-truth map

| Surface | Evidence and disposition |
| --- | --- |
| Focus audits | `focus_cleanup_baseline_2026-08-22.md` and `focus_cleanup_events_1_20_2026-07-29.md` remain dated static and MCP evidence. Their route gaps, geometry warnings, AI observations, and timeout limits are retained. No current gameplay status or design approval follows from those reports. |
| Localisation cleanup | `localisation_cleanup_2026-07-29.md`, `localisation_cleanup_baseline_2026-08-22.md`, and `localisation_cleanup_patch_2026-08-22.md` retain their dated key scans and wording decisions. Later Event 5, Event 6, Fallout, and Event 11 changes are named where the old paths or instructions would otherwise be replayed. |
| Event 5 duplicate localisation | The candidate in the baseline was implemented by `remaining_safe_cleanup_2026-08-24.md` and commit `0587e680c3`. The named surviving source is `localisation/english/005_soviet_collapse_l_english.yml`. |
| Event 6 localisation | The old decisions, country-core, events, and focus files were later consolidated into `localisation/english/006_independence_wave_iw043_iw058_l_english.yml` by commit `fe064fd57a`. The old path in the 2026-07-29 report is retained only as historical evidence. |
| Fallout Ashline localisation | The old Ashline file was later consolidated into `localisation/english/fallout_consolidated_l_english.yml` by commit `8cea20fda6`. The shared key is recorded at line 958 in the inspected tree and the selector anchor is recorded around line 5937. |
| Shared helper ownership | `shared_helper_architecture_baseline_2026-08-22.md` retains the ownership-drift finding. Commit `775099cbfa` later clarified the owner index and preamble in `common/scripted_effects/chaosx_dynamic_effects.md`. |
| Retired dynamic helper | `modify_value_based_on_chaos_tier` was a dated orphan candidate and was later removed by commit `2f529cc54c`, as recorded by `events_1_20_catalog_dead_localisation_cleanup.md`. |
| Remaining helper candidates | `damage_buildings_in_random_states` and `clear_special_chaos_country_civilian_effects` remain unresolved proof targets in the dated helper baseline. This cleanup did not perform their dynamic, meta-effect, save, or generated-reference proof. |
| Shared helper audit | `shared_helpers_audit_2026-07-29.md` records the duplicate state alternatives and the later Event 026 consumer retirement. Its concurrent changes were preserved. |
| Repo map | `repo_map_2026-08-22.md` remains a dated repository source map. Its 2026-08-24 status note and recommendations are historical evidence and are not a global replacement for the root curator's source map. |
| Spreadsheet handoffs | The two spreadsheet handoffs document dated workbook edits and exporter results. The workbook and export files were outside this subagent's write scope, so no new workbook status is claimed. |
| World-threat documentation path and wrapper wording | The dated audit named `014_cannibalism_core_effects.txt` at `docs/systems/world_threat_mechanic.md:81,154`, but a targeted current path check confirms both lines now use `common/scripted_effects/014_cannibalism_effects.txt`. The narrow path correction is present. Broader Black Plague wrapper wording and runtime behavior reconciliation remain unresolved. |

## Plan and handoff disposition

| Item | Disposition | Basis or blocker |
| --- | --- | --- |
| Focus static and MCP baselines | Unresolved | The reports retain dated source and artifact evidence, but no explicit acceptance basis for route redesign, loader normalization, geometry changes, or AI changes is present in this scope. Required engine and probability checks remain parent-owned. |
| Event 5 duplicate-file candidate | Implemented | `remaining_safe_cleanup_2026-08-24.md` and commit `0587e680c3` record the deletion and the named canonical file. No replay is needed. |
| Event 011 unavailable fallback | Implemented in the named patch | `localisation_cleanup_patch_2026-08-22.md` and commit `9cfec72b3` record the replacement and exact-reference scan. Early participant-disclosure concerns remain historical review context. |
| Event 6 old localisation paths | Superseded by named replacement | Commit `fe064fd57a` names `006_independence_wave_iw043_iw058_l_english.yml` as the consolidated replacement. |
| Fallout Ashline old localisation path | Superseded by named replacement | Commit `8cea20fda6` names `fallout_consolidated_l_english.yml` as the consolidated replacement. |
| Shared helper ownership drift | Implemented in the named documentation repair | Commit `775099cbfa` clarified the owner index and preamble. The dated finding remains for chronology. |
| Retired chaos-tier helper candidate | Superseded by named removal evidence | Commit `2f529cc54c` and `events_1_20_catalog_dead_localisation_cleanup.md` record the removal. |
| Remaining helper and world-threat wrapper candidates | Unresolved | Full dynamic or owner-source proof was outside the bounded structural prose pass. The narrow world-threat path correction is confirmed at lines 81 and 154, but broader wrapper wording and runtime behavior reconciliation still need owner and MCP review. |
| Repo map recommendations | Unresolved | They are dated next actions without a new acceptance basis. Retain them as evidence and re-evaluate against the root curator's source map. |
| Spreadsheet alignment handoffs | Implemented in their dated workbook passes | Their own validation sections record workbook and export evidence. No workbook or CSV edit was made here. |

No new design claim was promoted to accepted status in this cleanup. Claims that lacked an explicit acceptance basis remain unresolved or are linked to later implementation evidence without treating implementation evidence as approval.

## Contradictions and resolutions

1. The helper baseline listed `modify_value_based_on_chaos_tier` as a proof-gated orphan, while later source history records its removal. The contradiction is resolved by retaining the dated candidate and naming commit `2f529cc54c` as the later removal evidence.
2. The helper baseline described ownership drift as open, while commit `775099cbfa` later repaired the dynamic-effects documentation owner index. The dated finding is retained and no replay instruction remains.
3. The 2026-07-29 localisation handoff names deleted Event 6 and Fallout files. The later consolidated replacement files and commits are now named beside those historical paths.
4. The 2026-08-22 localisation baseline lists the Event 5 duplicate file as a future retirement candidate, while the 2026-08-24 handoff records the deletion. The baseline now records the implemented disposition.
5. The focus baseline's dated consumer-scan claim listed `common/events`. The current path check found `common/events` absent and `events` present, but this cleanup does not claim that the dated scanner traversed `events`.
6. The helper baseline retained a dated recommendation for stale Event 014 paths in `docs/systems/world_threat_mechanic.md`. A targeted current check confirms lines 81 and 154 already use `014_cannibalism_effects.txt`. The narrow path contradiction is resolved. Broader wrapper wording and runtime behavior remain open.
7. Several dated reports used current or accepted labels for snapshot findings. Those labels were changed to audited-tree or recorded-target wording without changing counts, scenario evidence, artifact URIs, or route distinctions.

## Duplicate and superseded documents

No documentation file was merged, deleted, or archived by this pass. The following historical candidates or paths are superseded by named evidence:

- The Event 5 duplicate-file candidate is superseded by `remaining_safe_cleanup_2026-08-24.md`.
- The retired chaos-tier helper candidate is superseded by `events_1_20_catalog_dead_localisation_cleanup.md` and commit `2f529cc54c`.
- The old Event 6 localisation paths are superseded by `localisation/english/006_independence_wave_iw043_iw058_l_english.yml` and commit `fe064fd57a`.
- The old Fallout Ashline path is superseded by `localisation/english/fallout_consolidated_l_english.yml` and commit `8cea20fda6`.
- The helper ownership-drift recommendation is superseded by the owner-index repair in commit `775099cbfa`.

## Stale prompts and replay instructions

- The old Event 5 retirement instruction now points to its completed handoff and named canonical file.
- The old Event 011 fallback replacement instruction now points to the completed localisation patch and keeps the disclosure caveat.
- The old Event 6 and Fallout file references now include named consolidated replacements.
- The old helper proof list no longer asks the parent to delete the already-removed chaos-tier helper.
- The repo map's documentation repair recommendation remains a dated recommendation. The targeted path check confirms the world-threat filename correction is already present. Broader wrapper wording still needs owner and MCP review, and no acceptance is inferred from the old recommendation.
- Focus and spreadsheet reports retain their scenario evidence, counts, and edge cases while removing snapshot labels that could be mistaken for present status.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wraps were found in the eleven assigned files. The physical-line audit excluded headings, list markers, tables, block quotes, and code blocks. No intentional Markdown structure was flattened.

## Link-fix and reference evidence

The dated focus scan listed `common/events`. The current path check found `common/events` absent and `events` present without asserting historical traversal of `events`. The old Event 5 duplicate localisation file is absent and `localisation/english/005_soviet_collapse_l_english.yml` is present. The old Event 6 decisions file and the other component files are absent, while `localisation/english/006_independence_wave_iw043_iw058_l_english.yml` is present. The old Fallout Ashline file is absent, while `localisation/english/fallout_consolidated_l_english.yml` is present. The old `common/scripted_effects/014_cannibalism_core_effects.txt` path is absent, while `common/scripted_effects/014_cannibalism_effects.txt` is present. A targeted check of `docs/systems/world_threat_mechanic.md` confirms lines 81 and 154 already use the corrected source filename.

The named focus plan links used by the handoffs were checked where they are complete repository paths. Vanilla reference paths and generic placeholder paths were retained as explicitly labelled references. The narrow world-threat path correction is present, while broader wrapper wording and runtime behavior remain unresolved and need owner and MCP checks.

## Retained facts and unresolved checks

The exact focus counts, route identifiers, scenario-specific MCP artifacts, timeout results, GUI artifact limits, localisation key counts, sourced quotation attribution, workbook dimensions, export row counts, Event 026 retirement note, helper call-site evidence, and spreadsheet cell mappings remain in their original handoffs. Punctuation cleanup did not change those facts.

The parent still needs full source and MCP checks for any focus behavior, event behavior, weighted logic, GUI, map, technology, or lifecycle claim. The parent also needs owner and MCP review for the world-threat wrapper wording and runtime behavior, any remaining helper deletion, the unresolved event-name registry, and any design target described as accepted in older material without a recorded basis.

## Validation and limits

- Read count was verified as 11 of 11 assigned handoffs in full before editing.
- Scoped `rg` checks were used for stale paths, current-status wording, old helper names, semicolon and em dash punctuation, and the named replacement files.
- Repository path checks confirmed the old paths and their named replacements listed above.
- The hard-wrap audit found no accidental prose wraps.
- The final diff review is limited to the eleven assigned files and this handoff. Other worktree changes were left untouched.
- No MCP route was called because the parent authorized structural prose cleanup only. No new engine evidence was generated.
- No workbook, CSV, gameplay, localisation source, asset, GUI, generated role, or provider validation was run because those surfaces were outside the named ownership scope.
- No game executable or live save was opened.
- No commit was created. The parent reviews and commits the combined work.

## Remaining risks for the parent

The dated audit documents still contain historical claims that require parent interpretation against the latest source tree. The world-threat filename correction is present, while the broader wrapper wording and runtime behavior still need owner and MCP review. The remaining helper candidates need full generated-reference and lifecycle proof. Older plan and handoff language may still require explicit acceptance records before it can become an active plan. Existing MCP artifacts remain partial and revision-bound, and no gameplay completion claim is made by this handoff.

Simplifications and omissions: no gameplay, engine, MCP, workbook, CSV, asset, localisation source, GUI, or generated-agent changes were made. No hard-wrap correction was needed because none was found. No historical document was deleted.
