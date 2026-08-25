# 3D source-style and firearm-readiness skill update

## Disposition

The reusable `chaos-redux-3d-model-pipeline` workflow now rejects anime-derived references and prevents firearm-bearing units from reaching Meshy when the source pose cannot support ordinary combat firing.

## Changed file

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`

## Rules added

- Anime, manga, manhwa, chibi, anime-derived cel shading, exaggerated anime proportions, and similar anime-game-character presentation are hard source and final-input rejections.
- Grounded professional fantasy, horror, tabletop, promotional, and game concept illustration remains eligible when it is not anime-derived.
- Every firearm-bearing unit declares `fires_in_combat` or `non_firing`.
- A combat-firing firearm must be complete and unobstructed in both the selected Internet artwork and final Meshy input, with trigger-hand, support-hand, stock/shoulder where applicable, and clear muzzle continuity already present.
- Faithful ImageGen cleanup cannot re-pose the subject or repair a failed weapon relationship.
- Firing actions require provider-authored aim, discharge, recoil, and recovery with retained contact; Meshy remains first, with another professional source allowed only through the existing documented fallback gate.
- `attack`, `defend`, `support_attack`, and every additional firing state require discharge timing, muzzle locator, appropriate particle/effect and light records, legally usable weapon-identity-matched sourced audio, provenance/checksums, and synchronization evidence.
- A `non_firing` unit requires a zero firing-state/effect/sound audit.

The gates are mirrored in intake, Internet source selection, exact-one-image preflight, action QA, evidence and manifest requirements, and the bounded `chaosx_3d_model_pipeline` prompt contract.

## Review and validation

The official `skill-creator` validator reports `Skill is valid!`.

An independent `chaosx_skill_maintainer` audit found initial gaps around energy-weapon preservation, explicit evidence fields, named firing states, non-firing sound roles, and professional-animation fallback wording. Those findings were incorporated. The existing Meshy 7, rights and NoAI, faithful-cleanup, period, color, sourced-audio, bespoke-counter, and no-manual-Blender-animation gates remain in force.

The independent audit also noted that the shared routing skill and canonical worker TOML do not restate these new rules. This task intentionally changes only the user-requested 3D skill; current Africa worker prompts explicitly require reading the updated skill and repeat the new gates. A separate routing-definition change should be made only if the project wants these clauses duplicated outside the 3D skill.
