# Event 016 stage-0 simple advisor visual review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_frame.png` and `advisor_paper.png` sources.

The bottom-to-top layer order is frame, resized/rotated portrait, and paper. The portrait is clipped to the frame opening and receives a slight sepia blend.

## Independent verdict

Reviewer: `/root/kruger_advisor_alignment_review`

Verdict: `PASS`

- Face scale is close to the canonical `generic_europe_1` and `generic_europe_6` cards without appearing oversized.
- Hair has a tight but valid upper margin, while eyes, chin, collar, and visible shoulder sit naturally inside the opening.
- Horizontal centering remains correct in the exposed portrait area despite the paper overlap.
- The `-1.5` degree rotation follows the irregular frame without making Kruger look tilted.
- The paper covers the lower-right torso without materially obscuring identity.
- No portrait pixels spill beyond the frame opening, and the outer corners remain transparent.
- Kruger's white hair, facial structure, expression, and scientist styling remain distinct at `65x67`.
- The canonical frame and paper geometry plus the civilian advisor composition fit the vanilla family.
- No further alignment adjustment is required. The selected `c03` placement should remain unchanged.

## Alignment study

The final was selected after a twelve-candidate coarse grid, a twelve-candidate fine grid, and a six-candidate finalist grid against canonical vanilla cards.

The chosen placement uses the full `156x210` portrait, resized to `34x57`, centered at `24.5 35.5`, rotated `-1.5` degrees around that stable center, and blended with sepia strength `0.18`.

The finalist comparison sheet is retained at `docs/assets/016_brilliant_scientist/contact_sheets/kruger_stage0_advisor_alignment_grid.png`.

## Runtime evidence

- Script SHA-256: `8B7F9F69820207A9191D634E578CDDC8519C4BB6E5D426CD84742544120F4967`
- Processed PNG SHA-256: `0F9B4A0EE0BAE500E9F6F8F65EBA47A1B35A86E828E1E65AA3E8CD8642C823C1`
- Runtime DDS SHA-256: `182B7D4947AC0649FA8D01601C2466B837733D391EE61DC79A1814E9606CB84B`
- PNG and decoded DDS RGBA pixels are identical.
- Both files are `65x67` RGBA with alpha extrema `0..255`.
