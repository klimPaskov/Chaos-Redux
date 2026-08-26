# Event 012 Oracle Recon counter refresh handoff

Date: 2026-08-26.

Scope: replace the identity-stale Oracle Recon counter package only. No gameplay, localisation, entity, animation, sound-definition, or shared GFX design changes were introduced by the counter artist.

## Accepted source and visual review

The replacement source is `docs/assets/012_africa/models_3d/oracle_recon/counters/source/oracle_recon_imagegen.png`. It depicts the accepted adult African male bone-clad oracle with an upright skull-and-rib ritual staff, ram-skull and bone regalia, dark fur and bindings, and an earth-and-bone palette. It is period-appropriate, unarmed, electronics-free, and not anime. The parent reviewed the source and `docs/assets/012_africa/models_3d/oracle_recon/counters/contact_sheet.png`; the former modern female scout/telescope identity remains quarantined under `rejected_stale/`.

The full-body alpha uses the documented rembg u2net alpha-only fallback, while the schematic source is native-alpha ImageGen. No checkerboard or matte pixels are present in the processed or final strips.

## Runtime package

The large strip is `152x42` with two `76x42` frames. The on-map strip is `60x12` with two `30x12` frames. The large frame 0 uses the sampled vanilla-green palette with dominant RGB `(73,106,73)`, and frame 1 carries the pale schematic selected state. The on-map frames use the inspected neutral grayscale family.

| Runtime destination | SHA-256 | Size |
| --- | --- | ---: |
| `gfx/interface/counters/divisions_large/unit_oracle_recon_icon.dds` | `96A6F7753B48E381A4FEFC3F145968FBE02491B4F3CF468EEED543586A410CDD` | 25,664 bytes |
| `gfx/interface/counters/divisions_small/onmap_unit_oracle_recon_icon.dds` | `023D841CEA7E26CE94A29EB6B3A144A3CA14962A130EB9F336B368908A77D837` | 3,008 bytes |

Both DDS files passed the legacy 32-bit BGRA header, exact-dimension, two-frame, alpha, and decoded roundtrip checks recorded in `docs/assets/012_africa/models_3d/oracle_recon/counters/manifest.json`. The stable sprite rows in `interface/012_africa_strange_force_counters.gfx` were retained unchanged.

## Completion boundary

Counter production and parent visual review are complete. The Oracle model package still has a 117 welded diagnostic boundary-edge warning, and the parent-owned live visual/audio consumer validation remains open. This handoff does not set the shared eight-family readiness flag and does not claim in-game completion.
