# Event 016 stage-0 simple advisor visual review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_frame.png` and `advisor_paper.png` sources.

The bottom-to-top layer order is a generated soft frame shadow, the untouched native frame, the proportionally fitted and rotated portrait, a generated soft paper shadow, and the untouched native paper. The portrait receives a slight sepia blend and is clipped only against the frame opening and visible frame footprint.

## Independent verdict

Reviewer: `/root/kruger_shadow_smoothing_review`

Verdict: `PASS`

- Natural face proportions pass with no stretching or warping.
- The portrait is visibly larger while remaining readable at native size.
- The `+4` degree counter-clockwise rotation gives the requested left tilt.
- The portrait covers the opening without a visible or transparent gap across 934 sampled exposed-opening pixels.
- The canonical frame and paper source hashes remain unchanged, their geometry is retained, and the portrait does not overpaint the frame.
- All 701 fully opaque paper pixels match the untouched canonical paper exactly.
- The generated shadows are smoother without appearing hard or over-dark.
- The paper edge has no white, light, or transparent fringe on dark, warm-light, and checkerboard backgrounds.
- All four outer corners remain fully transparent.
- Kruger's identity remains readable at native size and the card fits the vanilla advisor family.
- A `4x` nearest-neighbour inspection confirmed clean borders, shadow transitions, paper edges, and transparency.

No further correction was recommended.

## Alignment and layer contract

The final placement uses the full `156x210` portrait, one uniform scale of `0.257293965`, a fitted size of approximately `40.138x54.032`, stable center `25 32.5`, rotation `+4`, proportional cover margin `1.06`, and sepia strength `0.18`.

The affine sampler maps the portrait into the `65x67` card with a single scale for both axes, so it cannot stretch, squash, skew, or perspective-warp the face. The four opening corners inverse-map to valid source coordinates, proving the proportional portrait covers the opening corner to corner.

The canonical frame and paper remain their original `65x67` pixels and are neither resized nor rotated. Separate shadows derived from their alpha use Gaussian radius `1.05`, opacity `0.36`, dark neutral RGB `7 6 5`, and a one-pixel downward offset. Removing the hard paper exclusion eliminates the transparent strip beneath the paper, while the feathered shadow prevents Kruger's light clothing from reading as a white outline.

## Runtime evidence

- Script SHA-256: `0E479752C8CDE5F8F98578BBE463D066FE9C8CBB19E4DBD748811AC40073A139`
- Canonical frame SHA-256: `09EA6F96C9423A601EADF69CEC910EB8D9B2C17C9C4BC5CCD482EC469675C711`
- Canonical paper SHA-256: `39426397FD23CCB06DD0216537C3A6934DB65DC3CBD142A8119E0EBA4422B980`
- Processed PNG SHA-256: `F5ABD69FB0DA67E7133CE061D19F841E50FD6BF47A602606CD1D1017043F85CA`
- Runtime DDS SHA-256: `B6F34889DFDE4E893C749976AB8B532FA15FDD133C31EDFE7146224AB588FC05`
- PNG and decoded DDS RGBA pixels are identical.
- The runtime DDS is a `65x67` one-level BGRA surface of `17,548` bytes.
- All four outer corner pixels are transparent.
- No semi-transparent final pixel has near-white RGB contamination.
