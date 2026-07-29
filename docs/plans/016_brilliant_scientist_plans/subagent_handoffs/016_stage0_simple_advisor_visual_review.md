# Event 016 stage-0 simple advisor visual review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_frame.png` and `advisor_paper.png` sources.

The bottom-to-top layer order is the untouched native frame, the proportionally fitted and rotated portrait, and the untouched native paper. The portrait receives a slight sepia blend and is clipped to the frame opening with a narrow exclusion beneath the paper footprint.

## Independent verdict

Reviewer: `/root/kruger_uniform_advisor_review`

Verdict: `PASS`

- Natural face proportions pass with no stretching or warping.
- The `-3` degree portrait rotation aligns with the frame.
- The portrait covers all four opening corners without a visible gap.
- All 1,350 visible nontransparent frame pixels outside the paper overlap match the untouched canonical frame exactly.
- All 701 fully opaque paper pixels match the untouched canonical paper exactly.
- The paper edge has no white fringe, new mask gap, or halo.
- Outer corners remain clean and transparent.
- Kruger's identity remains readable at native size and the card fits the vanilla advisor family.
- A `4x` nearest-neighbour checkerboard inspection also found clean borders, mask transitions, paper shadow, and transparency.

No further correction was recommended.

## Alignment and layer contract

The final placement uses the full `156x210` portrait, one uniform scale of `0.245299926`, a fitted size of approximately `38.267x51.513`, stable center `25 32.5`, rotation `-3`, proportional cover margin `1.02`, and sepia strength `0.18`.

The affine sampler maps the portrait into the `65x67` card with a single scale for both axes, so it cannot stretch, squash, skew, or perspective-warp the face. The four opening corners inverse-map to valid source coordinates, proving the proportional portrait covers the opening corner to corner.

The canonical frame and paper remain their original `65x67` pixels and are neither resized nor rotated. The paper exclusion affects only portrait visibility beneath the supplied paper alpha footprint; it does not rewrite the frame or paper and prevents light clothing from producing a white fringe.

## Runtime evidence

- Script SHA-256: `8B6F625C13B75AFD45B29FAFF2F00FAB0013342594C93ACDF7B7E5C0333D4183`
- Canonical frame SHA-256: `09EA6F96C9423A601EADF69CEC910EB8D9B2C17C9C4BC5CCD482EC469675C711`
- Canonical paper SHA-256: `39426397FD23CCB06DD0216537C3A6934DB65DC3CBD142A8119E0EBA4422B980`
- Processed PNG SHA-256: `7421829B05F4B0D0471C08B748246B77F308DC48D1FCEEDEA6F968D5AA54524F`
- Runtime DDS SHA-256: `CD0042AA5F63BD0A0CB3F3693828FB61B1E804C75D3189C94999426E29DDD737`
- PNG and decoded DDS RGBA pixels are identical.
- The runtime DDS is a `65x67` one-level BGRA surface of `17,548` bytes.
- All four outer corner pixels are transparent.
- The entire 2,697-pixel protected frame-and-paper region is byte-identical to the supplied layers composited without a portrait.
