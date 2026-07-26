# FORM-39 Melanesian Federation flag handoff

Status: `needs_user_review` for runtime admission; visual generation, processing, DDS conversion, and TGA placement are complete.

## Proposed runtime identity

- Proposed/reserved route tag: `MFX` (not an approved gameplay identity yet).
- Flag family: base flag only. No ideology variants were requested or generated; do not invent variants until the FORM-39 adapter specifies them.
- Normal runtime TGA: `gfx/flags/MFX.tga` (82x52).
- Medium runtime TGA: `gfx/flags/medium/MFX.tga` (41x26).
- Small runtime TGA: `gfx/flags/small/MFX.tga` (10x7).
- DDS evidence: `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/dds/MFX.dds`, `MFX_medium.dds`, and `MFX_small.dds`. These are evidence/conversion outputs; HOI4 country flags use TGA files.

## Wiring guidance

Country flags are engine-convention TGA assets and normally do not require a `.gfx` sprite definition. If the accepted FORM-39 adapter chooses a different X-tag, rename or copy the three TGAs to that exact tag before admission and update the manifest. Do not wire `MFX` merely because it is available in the reserved-tag audit.

If a project-specific `.gfx` consumer is later approved, the parent agent owns the `.gfx` edit and must point it to the final runtime DDS or TGA path required by that consumer. This package intentionally does not edit `.gfx`, gameplay, localisation, or country files.

## Visual rationale

The generated flat flag uses deep ocean blue for shared maritime space, a narrow gold route band for the negotiated civic compact and maritime logistics, and an invented ivory three-lobed emblem with dark-teal outline and three internal divisions for the named Fiji/Papua/West Papua member packages. The emblem is non-sacred and makes no historical or cultural attribution.

## Acceptance gate

The package remains `needs_user_review` until the parent accepts the named FIJ/PNG/WPG consent-led adapter, final X-tag identity, member-package research/consent gates, and collision tests. If the small 10x7 mark is judged too collapsed at runtime, regenerate a new ImageGen flag design; do not replace the emblem with locally drawn primitive geometry.
