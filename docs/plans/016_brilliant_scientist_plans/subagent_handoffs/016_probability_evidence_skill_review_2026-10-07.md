# Probability evidence skill review

Disposition: reviewed and applied by the parent as two owned skill hunks, pending the shared-tree commit.
The bounded review is complete; only this handoff was created.
The existing `chaos-redux-subagents` skill covers the workflow, so no new skill or router is recommended.

## Exact proposed patch

Target: `.agents\skills\chaos-redux-subagents\SKILL.md`, within `MCP evidence in handoffs`.
Apply only these two replacements after reviewing the latest working copy; line numbers below describe the reviewed copy, not stable patch coordinates.

Replace the paragraph beginning `Discover the server's artifact resource template` (reviewed line 312) with this single paragraph:

```markdown
Discover the server's artifact resource template and use bounded byte-range reads when full output may be truncated.
For base64 blob payloads, decode each response to bytes, check its reported range against the requested offset and decoded length, and concatenate bytes in offset order without gaps or overlaps before decoding UTF-8 or parsing JSON.
Follow the returned continuation URI unchanged; `returnedRange.endExclusive == totalSize` marks the final range even when `complete` is false for a partial read.
Reject invalid payloads or embedded truncation text, and verify the assembled byte count, artifact SHA-256, and expected format before use.
Recover a truncated full read with bounded reads or report retrieval unresolved; retain the original artifact URI.
```

Replace the two consecutive paragraphs beginning `For hoi4.probability_inspect and hoi4.probability_evaluate` and `Probability scenario schemas vary` (reviewed lines 320 and 322, with inline backticks in the original) with this single paragraph:

```markdown
Use source objects and scenario fields accepted by each live probability route schema; correct argument rejection before declaring a route unhealthy.
Where supported, analyze frozen source bytes with `path` identifying the logical gameplay file, `snapshotPath` identifying the preserved workspace-relative file, and `expectedSourceHash` containing its exact SHA-256; compare distinct before and after sources under the identical saved `scenarioSet` without replacing gameplay files.
Shared helpers and constants remain current, so a frozen source comparison does not establish a historical whole-workspace comparison.
Analysis artifacts cannot replace pre-edit source, and manifests describe declared custom pools; report missing baseline or comparison coverage unresolved.
An empty `requiredInputPaths` discovery result does not prove complete scenario inputs: check evaluation requirements and unresolved findings.
Follow the live schema and installed evaluator for numeric and token predicate shapes; never invent overrides, fixture keys, or gameplay flags to satisfy the adapter.
Record source and scenario identities, validation errors, artifact URIs, and eligibility assumptions; do not present assumptions or partial scores as campaign-state or balance proof.
```

## Evidence and limits

- Disk and HEAD collision checks found no existing handoff at the requested path before creation; an exclusive create also guards against a concurrent disk write.
- Reviewed repository HEAD: `4f4b26e81ee199df45211540a6eeeefae76ece93`.
The skill had other working changes (`7` added lines, `1` removed line in the read-only diff summary); its reviewed SHA-256 was `CC0C5514559EBFD61F7C7855066A00055622E34E2E286C952CD053170B2EAC68`.
- Read `AGENTS.md`, official `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`, and the current skill's relevant MCP/probability paragraphs.
The recommendation follows existing ownership, immutable-baseline, and evidence limits rather than adding routing rules.
- Named installed package checked: `C:\Users\klimp\AppData\Local\npm-cache\_npx\e5002410e5b7105a\node_modules\hoi4-agent-tools`, package version `3.10.0`.
Its `docs\probability.md` lines 17–30 describe read-only tools and discovery/evaluation limits; lines 123–127 document frozen selectors, logical-path recognition, exact byte hashing, and current shared helpers/constants.
Its `dist\hoi4_agent_tools\schemas\probability.js` lines 263–288 accept `snapshotPath` and `expectedSourceHash`, require logical `path` plus hash for frozen input, and reject combining snapshots with inline source or virtual patches.
Document SHA-256: `A392933E376396FE135E25711F513FE3B0F5F09D03847455C1A95948FED030C8`; schema SHA-256: `DE7AEB8FCFEBFDFC7DF6CE48E01808C64D371D590932916DC456CB8D7C73DF20`.
- Parent-supplied verified experience: the connected package accepted the frozen selector, a Git prepatch file was preserved exactly under `docs\testing`, and the after snapshot evaluated without gameplay writes.
This review does not independently rerun the tools or claim that the full comparison is complete.
- Parent-supplied verified artifact recovery: eleven reads with a 4096-byte range length reconstructed a 44080-byte JSON artifact from decoded blobs, following `continuationUri` and stopping at `returnedRange.endExclusive == totalSize` despite a false last-range `complete` value.
The replacement removes the unnecessary preference for byte lengths divisible by three: each returned range is decoded independently before byte concatenation, and text/JSON decoding waits for the complete byte stream.
- Parent-supplied verified scenario gap: inspect returned empty `requiredInputPaths` although evaluation needed input fields.
The recommendation preserves this distinction and requires actual evaluator predicate shapes rather than guessed overrides.

## Parent follow-up

Review and apply only the owned replacement paragraphs against the latest skill bytes, preserving other agents' changes, then commit through the parent-owned safe workflow.
No AGENTS.md or subagent-routing update is needed.
Skills created: none; skills updated: none; `chaos-redux-subagents` remains unchanged and needs parent review of this proposal.
No gameplay identifiers, source files, assets, models, MCP configuration, package files, Git state, or index entries were changed by this review.
There are no simplifications to the requested recommendation; applying the skill patch is intentionally deferred to the parent, and live observations above are attributed to the parent rather than independently verified here.

## Parent application

The parent replaced the existing artifact-read paragraph with the reviewed byte-concatenation and final-range rule, retaining its concrete resource-template example.
The parent added the frozen-source and empty-discovery guidance before the existing live-schema paragraph, preserving the existing source-object examples, rejected-field warning and the other agent's uncommitted schema update.
No event-specific details were added to the skill.
The owned patch and before-working bytes are retained in C:/Users/klimp/AppData/Local/Temp/chaosx_probability_skill_patch_bfa6d4cb587b4e2cb75abbfc032e2a98.
The parent verified the recovered pilot artifact at 15,373 bytes with SHA-256 692d5efe0ea258e549f2906246c3e2a9036694908be90ba41629632456b9b1f4, and verified the initial decision artifact at 217,816 bytes with its returned SHA-256 before retaining its gate projection.
Skill updated: chaos-redux-subagents.
No new skill, router or gameplay rule was introduced.
