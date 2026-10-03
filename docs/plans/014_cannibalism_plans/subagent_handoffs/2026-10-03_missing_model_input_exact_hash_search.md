# Repo Explorer Handoff

## Scope read
- Parent task: Perform a bounded, read-only local search for exact SHA-256 matches to five missing Event 014 model source or approved-input files.
- Explicit constraints: Seven-model production is closed; do not generate assets, use providers, run Blender or RunPod, write runtime files, reinterpret approved inputs, or copy recovered bytes. The parent owns any exact-byte copy, manifest audit, and commit. This handoff is the only write made for this task.
- Files or ids requested: Feast Guard `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`; Feast Cohort raw JPEG `80D34425CCC5F21E63FA378F6129DE4ED502020F2E59F8A09C7D69883D37AC9C`; Bone Guard raw source `DB4164F9435588C85672B51CE0F81AF4B47A950CE43686755FB6406D8F1D7F41`; Siege Eaters recorded provider input `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`; March Predation Column accepted reference `9523DBF13601E7AE8ACB3B58013700209D19BCA6C3866B8932FB6E8D18C91289`.
- Skills or docs read: Repository `AGENTS.md` instructions; `.agents/skills/chaos-redux-subagents/SKILL.md`; `docs/plans/014_cannibalism_plans/014_cannibal_model_source_direction_2026-08-22.md`; the five current package manifests listed below.

## Primary findings
- No exact SHA-256 match was found for any of the five targets in the eligible files under Downloads, `.codex/generated_images`, or OneDrive/Pictures.
- The scan hashed 2,936 files with `.png`, `.jpg`, `.jpeg`, or `.webp` extensions and sizes up to 25 MiB: Downloads 279, Codex generated images 2,577, and OneDrive/Pictures 80. No oversized candidate, enumeration error, or symlink was encountered.
- The repository-root `scratch`, `assets`, and `archives` directories do not exist. All five manifest-recorded source/input paths are also absent in the current working tree.
- `git log --all` found no history pointer at any of the five exact approved package paths. No general `.git` or Git LFS object-store scan was performed.
- The parent-provided prior result remains: a separate bounded 200-model-image search found no matches. The parent also records the F4 export recovery as complete in commit `911149f`; that recovered export was outside this search and was not rechecked or changed.
- Search snapshot revision: `16664b3a47988a099ca23e7b7d6779dad454d1ec`.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/plans/014_cannibalism_plans/014_cannibal_model_source_direction_2026-08-22.md` | Current Event 014 source and faithful-enhancement gate. | Line 19 records Feast Guard's user-supplied source path and exact `C67AF852...` hash; it says superseded generated descendants cannot be promoted. |
| `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/manifest.json` | Current Feast Guard provenance status and missing selected-source bytes. | `source_provenance.selected_source_sha256_as_documented` records `C67AF852...`; `selected_source_bytes_present` is false. |
| `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/manifest.json` | Current raw-source identity, authorization mode, and separate model-ready input record. | Lines 40–59 record raw JPEG `80D344...` as absent, reference-only authorization, a separate present `F2E2...` input, and an earlier no-match search. |
| `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/manifest.json` | Distinguishes the missing raw source from the separately approved prepared body and poleaxe images. | Lines 42–65 record raw `DB4164...` as absent and the distinct prepared-image hashes and approval roles. |
| `docs/assets/014_cannibalism/models_3d/cannibal_siege_eaters/manifest.json` | Records the missing provider-input hash and unresolved source-gate conflict. | Lines 56–73 record `1AC18B...`, state the NoAI candidate is not proven to be the provider input, and preserve the 2026-08-22 versus 2026-08-25 conflict. |
| `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/manifest.json` | Records the missing accepted reference hash and conflicting underlying-source records. | Lines 21–47 record `9523DB...`, missing bytes, null underlying-source identity/terms, and conflicting or superseded source records. |
| `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_missing_model_input_exact_hash_search.md` | This bounded search handoff. | Created by this read-only exploration task. |

## Existing patterns
The current manifests separate source bytes and provenance from accepted prepared/provider inputs, so a matching file hash can establish byte identity while leaving source creator, rights, task linkage, and approval questions unresolved. Feast Cohort explicitly records distinct raw and model-ready hashes; Bone Guard explicitly records a missing raw source alongside two different prepared inputs. Neither set of prepared files is a substitute for its missing raw source.

For Siege Eaters, the current manifest calls the retained NoAI artwork research-only and says its connection to `1AC18B...` is unproven; its source-gate override conflicts with the later accepted runtime handoff. For March, `9523DB...` identifies the accepted `meshy_input.png`, while underlying source identity, terms, exact prompt, and source comparison remain absent or conflicting. Exact-byte recovery would not resolve these questions.

## Vanilla or reference precedents
No vanilla or approved-mod precedent applies to local file-byte recovery. This task does not inspect or change an engine-facing surface, so no HOI4 MCP, wiki, or installed-game documentation route was used.

## Likely edit order for the parent
1. Keep the seven-model production closure and current source-direction gate in force.
2. Do not copy or promote an input from this search because it produced no matching paths.
3. If a future authorized local location yields a matching file, review its exact hash and recorded role first; then have the parent assess source eligibility and provenance independently before deciding whether a destination copy and manifest reconciliation are authorized.
4. Keep the Feast Guard F4 export recovery separate; the parent records that as complete in commit `911149f`.

## Validation checks
- Read the five manifests and confirmed the full recorded target hashes and source/input roles before searching.
- Confirmed each of the five current manifest-recorded source/input paths is absent in the working tree.
- Hashed only PNG/JPG/JPEG/WebP files of at most 25 MiB in Downloads, `.codex/generated_images`, and OneDrive/Pictures; excluded `.git` directories, did not follow symlinks, and printed no nonmatching file paths or contents.
- Checked Git history only for the five exact manifest-recorded paths; no approved-path commit pointer existed, so Git objects and LFS storage were not searched.
- Recorded the search revision above. No HOI4 process, logs, network source search, production tool, or runtime consumer was used.

## Risks and blockers
### Confirmed blockers
- All five exact target hashes remain unrecovered in the searched roots, and their current package paths are absent.
- Feast Guard's recorded user-supplied source still lacks its bytes and source-rights details; the exact model-ready input hash is also unset in its manifest.
- Feast Cohort and Bone Guard raw source bytes remain missing. Their separately recorded prepared inputs do not recover those raw sources or establish further rights.
- Siege Eaters retains the unresolved source-gate override conflict and an unlinked, ineligible NoAI research candidate. No hash result in this search resolves either issue.
- March Predation Column retains the missing accepted image and unresolved underlying source identity/rights, plus conflicting source records. A match to the accepted-image hash alone would not fill those provenance fields.

### Ordinary risks
- A byte-for-byte match in a future search would identify bytes only. It would not establish creator, license, usage permission, authorization scope, or provider-task linkage.
- The search was bounded to the named roots, raster extensions, a 25 MiB maximum, and the current local files. It made no claim about other disks, archives, online sources, or files above that size.

## Proposed writes and recovery requirements
No source-file write is proposed from this no-match result. If a later exact match is found, the parent owns any copy and manifest change: dry-run by reporting the candidate path, expected and actual SHA-256, byte size, and recorded semantic role; review source eligibility and provenance separately; apply only an explicitly authorized exact-byte copy; post-validate destination bytes against the expected SHA and audit the manifest's source/input role without filling unsupported provenance fields; if the copy or validation fails, remove only the newly created destination copy and restore any parent-owned manifest edit from its pre-change version while preserving the discovered original. No write, rewrite, copy, or rollback was performed by this explorer.

## Recommended next action
Keep these five source/input records unresolved and production closed. The parent should continue only if a newly authorized local source location is identified or the user supplies one of the exact expected files; any recovered bytes require a separate parent review of the package's existing provenance gate.
