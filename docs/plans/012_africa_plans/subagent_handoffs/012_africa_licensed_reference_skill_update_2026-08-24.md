# Africa Licensed-Reference 3D Workflow Update

Date: 2026-08-24

## Disposition

Promoted into the authoritative `chaos-redux-3d-model-pipeline` skill.

## File changed

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`

## Policy before and after

Previously, the normal sourced route required ImageGen to remain a pixel-faithful cleanup of one eligible artwork and treated a substantially original refinement as a separately approved fallback.

The active policy permits clearly licensed modern designed artwork and explicitly user-authorized copyrighted artwork to serve as visual reference for one substantially original, model-ready ImageGen refinement. The refinement may adapt pose, composition, silhouette, background, anatomy or equipment readability, and other production-facing presentation while preserving the selected concept traits and intended unit identity. Only the approved refinement may be submitted to Meshy 7, and the source artwork must never become a shipped runtime asset.

The workflow still records the source URL or page, title, creator or publisher, stated license or terms, retrieval date, provenance and AI-use decision, source checksum, user authorization where applicable, exact ImageGen prompt, source-to-refinement comparison, refined checksum, and parent approval. Source bytes are archived only when the stated terms permit local evidence retention.

Explicit `NoAI`, no-derivatives, or equivalent incompatible restrictions remain disqualifying. A license label or user authorization does not override those stated restrictions. Ambiguous or incompatible terms and material changes to the accepted unit identity still require review.

## Validation

`python C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/chaos-redux-3d-model-pipeline` returned `Skill is valid!`.

An independent read-only skill review passed every requested policy and non-regression gate. Its two wording observations were incorporated: broad authorization applies to named source candidates only, final refinement approval remains mandatory, and non-archived sources use a transient checksum or identifying fingerprint when permitted.

## Scope and unresolved consistency follow-up

No gameplay, localisation, runtime asset, provider job, generated Qoder definition, or generated Cursor definition was changed.

The related `chaos-redux-event-assets`, `chaos-redux-subagents`, and canonical Codex 3D-agent TOML surfaces already contain unrelated working-tree edits. Their duplicated routing prose was deliberately left unchanged to avoid mixing this policy update with unrelated work. A later isolated consistency pass should align those duplicates from the authoritative 3D skill and then regenerate runtime-specific agent definitions through the approved sync workflow.
