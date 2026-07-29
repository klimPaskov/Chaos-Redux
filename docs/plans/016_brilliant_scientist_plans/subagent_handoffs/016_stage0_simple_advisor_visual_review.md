# Event 016 stage-0 advisor template review

## Scope

This review covers `docs/assets/016_brilliant_scientist/processed_png/portraits/idea_doctor_warren_kruger_stage_0.png`, produced with `.tools/create_advisor_icon.py` from the approved stage-0 Kruger portrait and the canonical `advisor_template.png`.

The runtime composition has exactly two layers: the processed portrait first and the untouched template on top. No separate frame, paper, shadow, threshold, blur, edge, or component reconstruction remains.

## Exact transform contract

- Source portrait: full `156x210` stage-0 Kruger portrait.
- Proportional center crop: `0, 7.211745905, 156, 202.788254095`.
- Pre-rotation portrait size: exactly `25.03x31.38` pixels.
- Uniform affine scale: `0.16044871794871796`.
- Template opening center: `25 32.5`.
- Portrait offset: `7` right and `2` up.
- Final portrait center: `32 30.5`.
- Rotation: exactly `-3.75` degrees.
- Portrait-only sepia strength: `0.18`.
- Top layer: untouched native `65x67` `advisor_template.png`.

The fractional center crop changes the source aspect ratio without stretching it. The compositor asserts that the X and Y scales are equal before sampling.

## Independent verdict

Reviewer: `/root/kruger_exact_template_review`

Verdict: `PASS`

- The final PNG reproduces pixel-for-pixel from the source portrait using the compositor defaults.
- The portrait is created first and the template is alpha-composited exactly once as the top layer.
- The requested size, rotation, opening center, and offset are preserved without integer rounding.
- No portrait spill beyond the intended template coverage, broken alpha, fringe, or opaque-corner defect was found at native size or `4x` nearest-neighbour size.
- No contract deviation remains.

## Runtime evidence

- Script SHA-256: `A0445F3C2F2875076AC64ABED48B6A79AE2C828411A1E631E9E2066A2126D8B5`
- Canonical template SHA-256: `8F594EF62AFBA6FDEC58DE66A80609350DCFE884320B11E6CB6220F1A0E19F58`
- Processed PNG SHA-256: `780E4A87260F91921295C982A8D2A71706A02276097EE869FF031A17291C0E09`
- Runtime DDS SHA-256: `B8E9CBD8AAE61424504FCFF76C60CFAC1DB01EE94A189C2E3A68A1899446F423`
- All 897 fully opaque template pixels are byte-identical in the final composite.
- PNG and decoded DDS RGBA pixels are identical.
- The runtime DDS is a `65x67` one-level BGRA surface of `17,548` bytes.
