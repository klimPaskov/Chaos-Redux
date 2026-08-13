# Advisor Cover-Fit Skill Update Handoff

Status: complete reusable workflow correction; parent commit pending.

## Scope

This pass records the user-corrected reusable advisor-dossier fit rule and the follow-up alpha-seam correction in the existing Chaos Redux event-assets workflow.

The parent owns the corresponding `create_advisor_icon.py` and `test_create_advisor_icon.py` implementation and regression coverage. This handoff records the reusable contract; it changed no gameplay files, runtime assets, `AGENTS.md`, or unrelated skills.

## Exact sections changed

- `.agents/skills/chaos-redux-event-assets/SKILL.md`, `## 21.1 Advisor and high-command portrait icons`, advisor-template composition paragraph at current line 1109.
- `.agents/skills/chaos-redux-event-assets/tools/README.md`, `## Advisor and high-command dossier portraits`, fit contract at current line 91, overlay contract at current line 110, and metadata/QA contract at current line 118.

## Reusable rule captured

- Load the complete approved source canvas without pre-crop or pre-warp, measure the actual opening center, rotated width and height, and angle, and use one shared uniform scale factor to cover the opening while preserving aspect ratio exactly.
- Never clip the portrait to the exact visible opening. The canonical frame uses translucent antialiased inner-edge pixels, so an exact opening mask leaves those pixels without underlying portrait coverage and reveals an alpha seam.
- Center the covering portrait behind the opening, reject anisotropic stretch and matte or padded strips, extend it beneath the frame with the processor's centralized `2` px safe bleed and `1` px resampling guard, and keep the untouched template as the final top layer.
- Fail closed if the expanded bleed mask reaches a fully transparent exterior template pixel. The portrait may occupy the verified bleed region beneath the frame but must never spill into the transparent card exterior.
- Explain `source_pre_crop=false` as no pre-scale source crop, not as an assertion that post-scale frame clipping is absent.
- Record `source_pre_crop=false`, `frame_clip=true`, `stretch=false`, `frame_clip_pixels`, `opening_fill_size`, `under_frame_fill_size`, `covering_content_size`, `covering_content_center`, bleed and guard values, measured opening geometry, transform evidence, and output hashes.
- Require `opening_alpha_gap_pixels=0`, `inner_edge_alpha_gap_pixels=0`, and `exterior_alpha_leak_pixels=0`, then inspect native and nearest-neighbour enlargement against contrasting and checker backgrounds.
- Define the alignment overlay as red measured opening, green opening-fill plane, and yellow uniformly scaled covering portrait, with yellow showing the safe bleed/guard extension and recorded symmetric cover excess.

## Validation and search evidence

- Frame analysis proved that the old exact-opening mask left all `140` translucent pixels in the first inner-edge ring without portrait coverage. A `2` px expansion remains wholly beneath nontransparent frame pixels.
- `python -B .agents/skills/chaos-redux-event-assets/tools/tests/test_create_advisor_icon.py` completed with `Ran 17 tests` and `OK` after adding seam and exterior-spill regression cases.
- `python -B -m unittest discover -s .agents/skills/chaos-redux-event-assets/tools/tests -p 'test_*.py'` completed with `Ran 25 tests` and `OK`.
- `git diff --check -- .agents/skills/chaos-redux-event-assets/SKILL.md .agents/skills/chaos-redux-event-assets/tools/README.md` reported no whitespace errors.

## Boundary and remaining review

Runtime-card regeneration and independent visual acceptance remain documented in `2026-08-13_cbrn_advisor_card_reprocessing.md`; the producer may not self-approve that visual gate.
