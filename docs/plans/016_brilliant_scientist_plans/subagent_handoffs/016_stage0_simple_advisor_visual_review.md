# Event 016 stage-0 simple advisor visual review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_frame.png` and `advisor_paper.png` sources.

The bottom-to-top layer order is frame, resized/rotated portrait, and paper. The portrait is clipped to the frame opening and receives a slight sepia blend.

## Independent verdict

Reviewer: `/root/kruger_advisor_simple_review`

Verdict: `PASS`

- Kruger remains recognizable at native size and at enlarged nearest-neighbour review scale.
- Face and hair remain inside the dark portrait frame with no visible spill.
- The paper correctly appears above the portrait and frame.
- Outer corners remain transparent.
- Sepia is restrained and preserves facial contrast.
- Silhouette, scale, layering, and palette fit the vanilla advisor-card family.

## Runtime evidence

- Processed PNG SHA-256: `0F4142E72E5C062335BE90FF41BFCF5F48923AAF2E3573E07AC0AD8175C9EC08`
- Runtime DDS SHA-256: `CADB9BDCEA3FE57A5FBC5F27EFEE737EE023D04DD0D4F94C1F7FFBDA4A03B9CB`
- PNG and decoded DDS RGBA pixels are identical.
- Both files are `65x67` RGBA with alpha extrema `0..255`.
