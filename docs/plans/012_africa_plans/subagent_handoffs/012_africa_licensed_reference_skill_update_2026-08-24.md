# Africa Licensed-Reference 3D Workflow Update

Date: 2026-08-24

## Disposition

Promoted into the authoritative `chaos-redux-3d-model-pipeline` skill.

## File changed

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`

## Policy before and after

Previously, the normal sourced route required ImageGen to remain a pixel-faithful cleanup of one eligible artwork and treated a substantially original refinement as a separately approved fallback.

The active policy permits clearly licensed modern designed artwork and explicitly user-authorized copyrighted artwork to serve as the actual source for one faithful, model-ready ImageGen cleanup. ImageGen may remove or replace the background with genuine transparency, isolate the subject, enhance resolution, exposure, contrast, sharpness, compression quality, source-visible detail, and alpha edges, and remove scenery, display bases, irrelevant text, or extra figures. It must preserve the exact design, identity, silhouette, pose, anatomy, equipment, proportions, materials, palette, and distinctive details; it may not re-pose, restyle, complete, invent, redesign, or create a substantially original substitute. Only the approved faithful cleanup may be submitted to Meshy 7, and neither the source nor its cleaned reference may become a shipped runtime asset.

The workflow still records the source URL or page, title, creator or publisher, stated license or terms, retrieval date, provenance and AI-use decision, source checksum or identifying fingerprint, user authorization where applicable, exact ImageGen cleanup prompt, source-to-cleanup comparison, cleaned checksum, and parent approval. Source bytes are archived only when the stated terms permit local evidence retention.

Explicit `NoAI`, no-derivatives, or equivalent incompatible restrictions remain disqualifying. A license label or user authorization does not override those stated restrictions. Ambiguous or incompatible terms and material changes to the accepted unit identity still require review.

## Validation

`python C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/chaos-redux-3d-model-pipeline` returned `Skill is valid!`.

An independent read-only skill review passed every requested policy and non-regression gate before the later cleanup-only clarification. Its two wording observations remain incorporated: broad authorization applies to named source candidates only, final cleaned-image approval remains mandatory, and non-archived sources use a transient checksum or identifying fingerprint when permitted. The user's later correction superseded the earlier substantially-original-refinement wording and restored faithful cleanup as the only normal Internet-derived route.

## Scope and unresolved consistency follow-up

No gameplay, localisation, runtime asset, provider job, generated Qoder definition, or generated Cursor definition was changed.

The related `chaos-redux-event-assets`, `chaos-redux-subagents`, and canonical Codex 3D-agent TOML surfaces already contain unrelated working-tree edits. Their duplicated routing prose was deliberately left unchanged to avoid mixing this policy update with unrelated work. A later isolated consistency pass should align those duplicates from the authoritative 3D skill and then regenerate runtime-specific agent definitions through the approved sync workflow.
