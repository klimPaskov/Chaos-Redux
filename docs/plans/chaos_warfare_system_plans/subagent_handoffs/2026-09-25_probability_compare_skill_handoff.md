# Probability comparison skill handoff

Disposition: implemented under the parent's bounded skill-maintenance request.

Changed `.agents/skills/chaos-redux-subagents/SKILL.md` only. The audit-patch-compare rule now requires the parent or patch owner to save the exact pre-edit source as an immutable file, its SHA-256 hash, and the scenario fixture before editing. The compare guidance now uses real before/after source paths under the live schema, keeps source hashes and revisions in evidence rather than rejected source fields, and reserves manifests for declared custom pools. A saved analysis artifact does not stand in for a before source. Missing historical source or a deleted candidate that prevents comparison leaves the numeric delta unresolved; the auditor retains inspect evidence for absence.

Basis: the current `hoi4.probability_compare` tool declaration exposes `before`, `after`, `beforeManifest`, `afterManifest`, and `scenarioSet`. The existing post-edit handoffs recorded input-validation rejection of `sourceRevision` and `sourceHash` under both source objects, and rejection of analysis-artifact fields under `beforeManifest` in favor of custom-pool fields `id`, `selection`, `candidates`, and `transitions`.

Validation: reviewed the skill diff against the live tool declaration and the two recorded validation failures. No gameplay source or probability analysis was changed or run by this skill patch.

Remaining limit: a historical comparison already lacking an exact pre-edit file cannot be reconstructed from its analysis URI or hash alone. The parent must arrange the source snapshot before a future weighted edit; source-path acceptance and the comparison result still require the connected tool's response for that specific case.
