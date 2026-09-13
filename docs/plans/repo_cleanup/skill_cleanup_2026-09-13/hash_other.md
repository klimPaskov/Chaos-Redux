# Hash prose cleanup handoff — other skills

Disposition: `implemented`, pending parent review.
Acceptance basis: the user explicitly requested removal of skill bloat about hashes; the parent assigned these seven current entrypoints only.
This request supersedes earlier blanket preservation only for hash bookkeeping, while unrelated requirements remain intact.

## Reading and scope

All seven current skills were fully read before editing in three bounded, untruncated outputs: comfyui, MTTH, state ledgers, and GUI completely; debug in lines 1–350 and 351–698; frame animation in lines 1–175, 176–350, and 351–501; XLSX completely.
Pre-edit copies are saved at `C:/Users/klimp/.codex/tmp/chaos-redux-category-pictures-20260913/original/.agents/skills/<name>/SKILL.md`.
`AGENTS.md`, the official skill-creator, and the subagent skill were read fully in the preceding cleanup and remain applicable.
The current `.codex/agents/chaosx_skill_maintainer.toml` was read fully for this pass; its Sol/high fields were not edited.
Previously consulted offline wiki and installed vanilla references remain the instruction-meaning sources; this pass changes no engine-facing surface.
Only comfyui and debug-playtest were edited; five assigned entrypoints were reviewed and left byte-for-byte unchanged.
No agents were spawned, no game/provider/production/paid/runtime operation was performed, no spreadsheet/helper/other documentation file was edited, and no commit was made.

## Exact removed mandates

- `chaos-redux-comfyui/SKILL.md`, grounded `styled_final` subitem, line 15: removed `output hashes` from the branch evidence list.
The list retains locked workflow revision, provider/job evidence, and independent identity/framing/provenance review.
Portrait source/rights/identity, explicit crop/resize, wiring, pending-state, optional request, user-operated RunPod, queued-job exclusion, and worker-validation requirements remain unchanged.
The removed demand had no specific corruption, equality, concurrent-output, or synchronization check attached to it.
- `chaos-redux-debug-playtest/SKILL.md`, startup step 2, line 121: changed `Record hashes and timestamps for` to `Record timestamps for` for the same five named log paths.
Timestamps, fresh-directory verification, current-run delta, copied fresh logs, before-patch evidence, triage, relaunch/retest, and explicit opt-in desktop scope remain unchanged.
Hashes added bookkeeping to this freshness/delta workflow without a separate integrity purpose.
Neither removal was replaced with generic boilerplate.

## Purposeful retained check and unchanged files

`chaos-redux-scripted-gui/SKILL.md`, apply/compare step 4, line 55 retains `expectedSourceHash` and its patches-mode-only restriction.
It is an actual tool-contract field guarding the source a patch applies to, with an explicit source-mode exclusion; removing it would change the concurrency/schema contract rather than remove prose bookkeeping.
GUI reference creation, iterative MCP preview, before/after scenario identity, layout, click-region and visible-defect gates remain byte-exact.
No exact artifact-retrieval or hash-dependent runtime-synchronization requirement occurs in these seven entrypoints, so none was removed or invented.
MTTH, state ledgers, XLSX, and frame animation contain no hash/checksum/SHA/digest mandate and remain byte-exact.
Real source frames, animation/static-fallback/DDS proof, ledger conservation/privacy/scope, probability analysis, workbook/formula preservation, recalculation limits, and catalog source/export boundaries remain untouched.

## Validation and limits

Saved pre-edit copies were compared with current bytes for every file.
The entire delta equals only the two exact substring replacements above; the other five files match their copies exactly.
Frontmatter bytes, every fenced block's exact bytes, and the full multiset of inline technical literals match in all seven files.
No heading, anchor, code, command, schema, path, id, numeric value, or unrelated prose changed.
All seven passed the official `skill-creator/scripts/quick_validate.py` under Python UTF-8 mode.
An initial validator invocation incorrectly supplied the SKILL.md file instead of its containing folder; rerunning with the required folder argument passed without changing the skills or validator.
This is instruction-text validation, not provider/MCP/engine/game validation; those operations were outside scope.
No unrelated workflow simplification or omission was introduced.
The generic debug dependency gap reported in `other.md` is untouched.
Parent review owns cross-group integration and the final commit.

## Final file identities for parent review

These one-time digests identify handoff-time files for parent review; they are not added skill mandates.

| Skill | Disposition | Lines | SHA-256 |
| --- | --- | --- | --- |
| chaos-redux-comfyui | updated | 21 | `125daa4e66957fcf02f5cd91e3a0a17f4a99395ad0f40c7ae376b4b59393b303` |
| chaos-redux-debug-playtest | updated | 698 | `9c6e27b8a86fd27422d8b2ec5302ac6fa7c64d89a564dbbda71db238190e3549` |
| chaos-redux-mtth | unchanged | 69 | `28be8b89fc0c8f6a86112411c62724a8c3e356339b5f1f3e1019b1d7292617e1` |
| chaos-redux-state-ledgers | unchanged | 97 | `efa2b14e8313dc427f452ef93705b8e149b91ce68006a2a7fc48580811cc2530` |
| xlsx | unchanged | 330 | `aead3ab9e26e4f951f212604481fd9267c8ccb52698311a0d8f07c2d30f6cce5` |
| chaos-redux-scripted-gui | unchanged | 130 | `f85f0a0888b25d14ca6d6b6535ea8b578542e19dac1f5fbd3d9113e51a525b93` |
| chaos-redux-frame-animation | unchanged | 501 | `86469ff50f33ead0690d3709b0523de1992f01a29713b801a6dd08c27b1be870` |
