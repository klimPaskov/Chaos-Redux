# Probability snapshot skill maintenance handoff

Disposition: `implemented` for the bounded skill correction; current fixture identity is reproduced by the captured exact-fixture replay, while the cause of the historical receipt discrepancy remains `unresolved`.
Acceptance basis: the parent assigned a concise, generic correction to the existing probability guidance and this handoff, with no gameplay, index, or commit scope.

## Owned changes

Updated `.agents/skills/chaos-redux-subagents/SKILL.md` with five added lines beside its existing immutable probability-baseline guidance.
The existing skill already covered canonical logical paths, supported `snapshotPath` fields, immutable bytes, identical scenarios, and partial evidence classification, so no new skill was created and those rules were retained.
The addition explains that archive-path `no_weighted_surfaces` can be a discovery-routing issue, distinguishes raw snapshot-byte `expectedSourceHash` from analysis `sourceHash`, requires verbatim fixture metadata and reconciled scenario hashes, and limits zero-score-delta conclusions when native research factors remain unbound.
No event IDs, audit dates, source-specific technology IDs, or prompt history were added to the skill.
No routing boundary changed; AGENTS.md and subagent definitions need no update.
Other skills were left unchanged.

## Evidence and meaningful validation

Read `docs/testing/2026-10-08_cbrn_research_cost_probability/mcp_baseline.json`, `scenario_plan.json`, and `mcp_after_compare.json`, plus `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-08_cbrn_research_cost_probability.md`.
The baseline records zero candidates from the archived paths and 25 plus 2 candidates from the canonical technology paths with the same before bytes.
Both final comparison receipts use canonical `path`, archived `snapshotPath`, and `expectedSourceHash`; recomputing SHA-256 from all four physical before/after snapshot files exactly matches those expected hash values.
Those raw snapshot hashes differ from the returned analysis `sourceHash` values; the skill does not guess the algorithm behind the latter.
Both comparison calls completed as `PROBABILITY_ANALYZED_PARTIAL` with zero exposed changes, while native external factors remain unresolved.
Official `skill-creator/scripts/quick_validate.py` accepts the edited skill.
The owned diff was reviewed against a byte-preserved copy of the already-dirty skill, confirming only the five intended additions.
No new MCP calls or live-game validation were needed for this documentation-only scope.

## Preservation and parent integration

Original working-file bytes: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.git\chaosx_skill_scratch\probability_snapshot_skill_note_20261008_173738\SKILL.before.md`.
Original SHA-256: `0447c92781ff53befe897284dca64ee4b3edfebf8e4879bdd92a1e00f5eb5976`.
Owned diff: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.git\chaosx_skill_scratch\probability_snapshot_skill_note_20261008_173738\owned.patch`.
Post-edit SHA-256 at handoff: `8900245486b1f0c536de615a557ec13cc835b26b93af5b41025b9e0caf9dac2f`.
Scratch manifest: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\.git\chaosx_skill_scratch\probability_snapshot_skill_note_20261008_173738\manifest.json`.
The anchor beginning `For an immutable baseline` was verified unchanged in HEAD before editing.
Prior documentation-curation and scenario-schema dirty hunks were preserved.
The parent owns isolation and any commit; no index or commit mutation was performed.

## Unresolved evidence discrepancy

At inspection, baseline JSON, scenario-plan JSON, and the auditor handoff record scenario hash `6af9cf175c3e31a2977acb6971aa71414d2ca9bff98567194e20dad5633fd467`.
The final comparison receipt claims baseline-identical fixtures but records `6af9cf175c3e31a2977acb6971aa71414d2ca9bff98567194f08a3e6c19cf61`.
The parent was notified; those auditor-owned files were not changed.
Those historical summaries do not establish matched fixture identity.
The current reconciliation in `docs/testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json` captures two frozen-before evaluations and two before/after comparisons with requests equal to the saved fixture and returned scenario hash `9014abc855784fcdc7f9cba67f0c7d33afff123b1402db73949c381209e7c004` in all four responses.
The historical artifact prefixes report the first `6af9` hash, but their complete bodies were not assembled and the original request body is absent, leaving the contradictory receipt unexplained.
Use the four captured exact-fixture replay packets for current partial comparison evidence; do not rewrite the historical discrepancy as a proven transcription error.
This discrepancy does not block the reusable source-routing and raw snapshot-hash correction.
No simplifications were made to the assigned skill-maintenance scope.
