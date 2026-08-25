# 3D model pipeline skill source-artwork update handoff

## Scope and result

Parent amendment: this handoff’s source rule is superseded for Event 014 by the final 2026-08-22 gate. Actual Internet-sourced or user-supplied modern artwork is required, and ImageGen is limited to faithful resolution, alpha, background, padding, or edge cleanup; from-scratch generation and redesign are not acceptable model-input routes.

Updated `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` with the reusable modern-artwork source-first policy requested for Chaos Redux model references.

The source gate now requires a unit-specific modern visual artwork search before from-scratch generation, prefers official or explicitly reusable sources, excludes archival, museum, historical, antiquities, archaeological, and documentary material as model-reference sources, and records `reference_only` for copyrighted visual research that cannot be passed directly to generation.

The ImageGen gate now requires a substantially original single-subject model sheet informed only by broad silhouette, pose, material/function cues, and unit role, with direct copying of distinctive protected designs, logos, symbols, exact costumes, and proprietary details prohibited. The existing exact-one approved Meshy 7 input rule, native transparency checks, provenance/checksum evidence, manifest fields, and parent/user approval gate for from-scratch fallback remain aligned.

## Files changed

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` — source mode/rights fields, modern artwork source-first gate, reference-only handling, ImageGen adaptation boundary, manifest/evidence requirements, and bounded worker prompt requirements.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/chaosx_3d_model_pipeline_skill_update_2026-08-22.md` — this handoff.

## Validation and ownership

The official validator passed:

```powershell
python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-3d-model-pipeline
```

Output: `Skill is valid!`

No gameplay, model, runtime, `.qoder`, or unrelated skill files were edited. No web artwork was selected and no provider or paid operation was called because this task only updated reusable instructions.

No simplification or unresolved blocker remains within this skill-maintenance scope. Parent review is still required before committing the combined working tree and before relying on any source-specific rights decision in a model job.

## Superseding clarification

Later committed skill revisions replaced the “substantially original model sheet” wording described above with the current faithful-cleanup contract. The live `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md` is authoritative: it requires an actual modern designed-artwork or user-supplied source, forbids archival and documentary model references, and limits ImageGen to faithful cleanup, alpha, resolution, background, padding, exposure, and approved colorization. A source-free reference remains a separate fallback requiring explicit approval after documented search failure.
