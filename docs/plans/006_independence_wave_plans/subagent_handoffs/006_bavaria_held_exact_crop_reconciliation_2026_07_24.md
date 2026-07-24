# Event 006 IW-009 Heinrich Held exact-crop reconciliation

Date: `2026-07-24`

## Scope

This parent reconciliation closes the current explicit archival-crop evidence requirement for Heinrich Held without changing his identity master, crop rectangle, ImageGen result, processed `156x210` candidate, or deferred runtime consumer.

## Evidence

- Unchanged archival master: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/source_masters/BAY_heinrich_held_keystone_1933.jpg`
- Master SHA-256: `35d1ee399c8c86efd024e8226a8effe97afc5fc0114c4a1186ad9cd4d6c3560d`
- Exact half-open crop rectangle: `(400,160)-(2070,2409)`
- Retained crop: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/crops/BAY_heinrich_held_crop_400_160_2070_2409.png`
- Crop SHA-256 before and after reconciliation: `11841151745e97e7398bef3c60481c0bfeefaba2b2d8225f3e3466d78f75cf3a`
- New exact-pixel record: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/crops/BAY_heinrich_held_crop_400_160_2070_2409.json`
- Crop utility: `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`
- Utility verdict: `exact_source_crop_verified`
- Decoded comparison: `decoded_pixels_equal = true`
- Decoded master-rectangle and output RGBA SHA-256: `e4dd893e32b68865c4f3a2e1e5b0930ab97f7cbda199d7201521956f45dce16d`

The byte-identical crop proves that the exact pixels independently reviewed in the Held visual/provenance audit are the explicit decoded rectangle from the unchanged archival master.
The audit already passes likeness, HOI4 country-leader style, grounded male identity, period role, and rights provenance.
No new ImageGen output or subjective portrait judgment was introduced by this mechanical reconciliation.

## Runtime boundary

After the reconciliation closed the final mechanical crop-proof gap, the parent copied the independently approved evidence DDS byte-for-byte to `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds`.
The runtime DDS SHA-256 is `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95`, matching the approved evidence DDS exactly.
The existing stable GFX and generated-character consumer already point to that runtime path, so no GFX, gameplay, localisation, character, protected Rupprecht portrait, advisor asset, dossier, or `_small` source was changed.
The Bavaria commander remains separately blocked and the package remains fail-closed until a fully cleared sourced commander portrait passes the complete workflow and a fresh country-package audit.
