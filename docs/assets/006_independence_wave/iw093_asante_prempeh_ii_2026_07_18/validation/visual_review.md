# Prempeh II country-leader portrait — superseded visual review

**Review date:** 2026-07-19
**Reviewer:** parent/main agent
**Historical PNG:** `processed_png/portrait_DOX_prempeh_ii_hoi4.png`
**SHA-256:** `4f3ac8ecba82b41679a499bc56551440f5dad2772abaef8db0bd9570300f38a6`
**Verdict:** visual approval withdrawn on 2026-07-22

The archival identity and TNA/OGL source remain accepted. The installed PNG
was produced through an ImageGen restyling of a real person, which conflicts
with the current deterministic real-person portrait pipeline. It must be
rebuilt from the unchanged archival master before IW-093 can receive visual
readiness. The findings below describe the historical review only.

## Findings

- The portrait is male and preserves the archival subject's recognizable face,
  direct gaze, age, skin tone, beaded head ornament, and Asante cloth.
- The crop is a readable head-and-shoulders/bust composition at `156x210`.
- The finish is painted and colorized with the restrained contrast, crisp
  facial planes, quiet period background, and readable silhouette of the
  canonical vanilla HOI4 male leader references.
- It contains no text, flag, frame, modern UI, advisor-card construction, or
  invented facial hair.
- At native size, the face remains distinct rather than reading as the generic
  Africa reference. The reference controls the style family only.

The superseded comparison sheet is
`contact_sheets/portrait_DOX_prempeh_ii_hoi4_review.png`. The earlier grayscale
candidate remains rejected and is not an alternative runtime asset.

## Retry-2 independent audit (2026-08-02)

**Verdict:** conditional near-pass for visual gates; package/runtime HOLD.

Retry-2 is recognizably Prempeh II and preserves the beaded headband, Asante
striped cloth, bird-finial chair, and pale fly-whisk. The master is 1081x1455
RGB and the deterministic candidate is 156x210 RGBA with a fully opaque alpha
channel. It has the centered readable bust, parchment-gray painted treatment,
and restrained warm/cool contrast expected of a vanilla HOI4 leader card.

The audit still records minor eye enlargement/brightening, a somewhat modeled
and narrower nose, a slightly longer jaw, and more ornate chair/cloth framing
than the canonical reference cards. These are source-fidelity risks rather
than a face substitution. Source crop equality, 1935 TNA/OGL provenance, and
the explicit head-and-shoulders consumer role pass. The retry therefore stays
evidence-only until the parent accepts the residual likeness/style caveat.

Retry-2 master SHA-256:
`1F4DE5280DC4F5050E11159D48FC672A2A0E65CFAF1F10C3A13579ECAE32D01F`.

Retry-2 deterministic candidate SHA-256:
`E55BC4D3D79502E6AA5049CF554616C263FDAA00336433A4E1179119FEBDA833`.

The source/master/candidate comparison sheet is
`contact_sheets/portrait_DOX_prempeh_ii_retry2_review.png`, SHA-256
`5A5AE59A56F3A431F5A141D774E35BF0C47B3290B706F7152EA52FBA43CBECC5`.
