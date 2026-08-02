# IW-093 Prempeh II portrait — GFX handoff

**Disposition:** historical consumer wiring only; visual approval withdrawn.

- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds`
- Sprite: `GFX_portrait_DOX_prempeh_ii`
- Character: `DOX_prempeh_ii`
- Texture size: `156x210`
- Consumer class: civilian country leader only

The sprite belongs in
`interface/006_independence_wave_iw093_iw098_portraits.gfx`. The installed DDS
was produced from an ImageGen restyling of a real person and does not satisfy
the current deterministic real-person portrait pipeline. Keep the source and
consumer contract for the compliant rebuild; registration does not attest the
IW-093 package or permit release before its portrait, history, force, flag,
formable, localisation, and audit gates pass.

No advisor, dossier, commander-small, or other-person fallback is authorized.

## Retry-2 disposition (2026-08-02)

Retry-2 is a source-locked ImageGen repaint from
`source_crops/DOX_prempeh_ii_head_shoulders.png` and has a conditional
near-pass from the independent identity/style audit. Documentation now records
its master and deterministic candidate, but the runtime consumer remains on
HOLD because minor facial drift and ornate framing still require final
native-size acceptance. Do not convert or wire the retry-2 candidate until a
final visual disposition is recorded.
