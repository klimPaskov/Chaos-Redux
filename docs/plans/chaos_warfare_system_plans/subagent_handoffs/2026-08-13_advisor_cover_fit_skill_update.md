# Advisor Cover-Fit Skill Update Handoff

Status: complete documentation-only maintenance pass; no commit was created.

## Scope

This pass records the user-corrected reusable advisor-dossier fit rule in the existing Chaos Redux event-assets workflow.

The parent-owned `create_advisor_icon.py` and `test_create_advisor_icon.py` changes were not edited.

This pass changed no gameplay files, runtime assets, `AGENTS.md`, unrelated skills, Python code, or tests.

## Exact sections changed

- `.agents/skills/chaos-redux-event-assets/SKILL.md`, `## 21.1 Advisor and high-command portrait icons`, advisor-template composition paragraph at current line 1109.
- `.agents/skills/chaos-redux-event-assets/tools/README.md`, `## Advisor and high-command dossier portraits`, fit contract at current line 91, overlay contract at current line 110, and metadata/QA contract at current line 118.

## Reusable rule captured

- Load the complete approved source canvas without pre-crop or pre-warp, measure the actual opening center, rotated width and height, and angle, and use one shared uniform scale factor to cover the opening while preserving aspect ratio exactly.
- Center the covering portrait behind the opening, reject anisotropic stretch and matte or padded strips, allow only the narrow symmetric post-scale excess to be clipped by the unchanged opening safety mask, and keep the untouched template as the final top layer.
- Explain `source_pre_crop=false` as no pre-scale source crop, not as an assertion that post-scale frame clipping is absent.
- Record `source_pre_crop=false`, `frame_clip=true`, `stretch=false`, `frame_clip_pixels`, `opening_fill_size`, `covering_content_size`, `covering_content_center`, measured opening geometry, transform evidence, and output hashes.
- Require proof that every opening-mask pixel has source coverage, no transparent, black, matte, or padded gap remains, and subject scale is comparable with vanilla references at native and `4x` review sizes.
- Define the alignment overlay as red measured opening, green opening-fill plane, and yellow uniformly scaled covering portrait, with yellow extending beyond green only by the recorded symmetric frame clip.

## Validation and search evidence

- Before editing, a targeted `rg` search found the superseded contain/matte wording in the two active workflow documents at `SKILL.md:1109` and `tools/README.md:91,110,118`.
- After editing, the targeted stale-wording search for uniform contain, contained portrait/content, source-derived padding/fill plane, residual strip, matte sampling, and `source_derived_padding` returned no matches in those two active workflow documents.
- A follow-up key search confirmed the active docs expose `source_pre_crop`, `frame_clip_pixels`, `frame_clip`, `stretch`, covering-content geometry, post-scale frame clipping, opening-mask QA, and red/green/yellow overlay semantics.
- `python -B .agents/skills/chaos-redux-event-assets/tools/tests/test_create_advisor_icon.py` completed with `Ran 15 tests in 0.765s` and `OK`; this execution did not write bytecode.
- `python -B C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents/skills/chaos-redux-event-assets` returned `Skill is valid!`.
- `git diff --check -- .agents/skills/chaos-redux-event-assets/SKILL.md .agents/skills/chaos-redux-event-assets/tools/README.md` reported no whitespace errors.
- The required offline Paradox wiki core pages and the installed vanilla documentation inventory were consulted before the documentation edit, as required by `AGENTS.md`.

## Boundary and remaining review

The pre-existing `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-08-13_cbrn_advisor_card_reprocessing.md` was not edited because it is outside the allowed write set; treat it as historical handoff material, not current reusable fit guidance.

This pass does not claim new runtime-card reprocessing or live HOI4 visual acceptance; the parent owns those follow-up decisions.
