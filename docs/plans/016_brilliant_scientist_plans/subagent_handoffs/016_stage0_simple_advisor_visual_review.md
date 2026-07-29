# Event 016 stage-0 simple advisor visual review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_frame.png` and `advisor_paper.png` sources.

The compositor first removes the baked shadow alpha from working copies of the canonical frame and paper. The bottom-to-top layer order is a generated clean frame shadow, the cleaned native frame, the proportionally fitted and rotated portrait, a generated clean paper shadow, and the cleaned native paper. The portrait receives a slight sepia blend and is clipped only against the frame opening and visible frame footprint.

## Independent verdict

Reviewer: `/root/kruger_clean_shadow_review`

Verdict: `PASS`

- Natural face proportions pass with no stretching or warping.
- The portrait is clearly larger while remaining readable at native size.
- The `+10` degree counter-clockwise rotation gives an unmistakable left tilt.
- The portrait covers the frame opening without a visible or transparent gap, frame overpaint, or clipped face.
- The canonical frame and paper source hashes remain unchanged, while their cleaned working copies retain the original geometry, patina, and recognizability.
- Each cleaned element has one consistent soft shadow without retaining or doubling its baked shadow.
- The paper edge has no white, light, or transparent fringe on dark, light, and checkerboard backgrounds.
- All four outer corners remain fully transparent.
- Kruger's identity remains readable at native size and the card fits the vanilla advisor family.
- A `4x` nearest-neighbour inspection confirmed clean borders, shadow transitions, paper edges, and transparency.

No further correction was recommended.

## Alignment and layer contract

The final placement uses the full `156x210` portrait, one uniform scale of `0.295330616`, a fitted size of approximately `46.072x62.019`, stable center `25 32.5`, rotation `+10`, proportional cover margin `1.16`, and sepia strength `0.18`.

The affine sampler maps the portrait into the `65x67` card with a single scale for both axes, so it cannot stretch, squash, skew, or perspective-warp the face. The four opening corners inverse-map to valid source coordinates, proving the proportional portrait covers the opening corner to corner.

The canonical source files remain unchanged. Working copies remove baked shadow alpha with core thresholds `96` for the frame and `176` for the paper, then reconstruct a narrow antialiased edge with Gaussian radius `0.45`. Separate shadows derived from those cleaned alpha cores use Gaussian radius `1.05`, opacity `0.36`, dark neutral RGB `7 6 5`, and a one-pixel downward offset. This produces one clean shadow per layer without a hard portrait exclusion or pale paper fringe.

## Runtime evidence

- Script SHA-256: `B98F59DD38F44E72016EE7A9754C320CF473253B5C8705E77020E420EBEC8185`
- Canonical frame SHA-256: `09EA6F96C9423A601EADF69CEC910EB8D9B2C17C9C4BC5CCD482EC469675C711`
- Canonical paper SHA-256: `39426397FD23CCB06DD0216537C3A6934DB65DC3CBD142A8119E0EBA4422B980`
- Processed PNG SHA-256: `A8F7EEA39E4999168AD0147CEA619DF8D7F9FB101283D016CF4297F8CFDE166C`
- Runtime DDS SHA-256: `6C23015F3CB13D4C09797D13AB688E771BDDDEE8C1B2771B8DD41FEED3BC4E15`
- PNG and decoded DDS RGBA pixels are identical.
- The runtime DDS is a `65x67` one-level BGRA surface of `17,548` bytes.
- All four outer corner pixels are transparent.
- No semi-transparent final pixel has near-white RGB contamination.
