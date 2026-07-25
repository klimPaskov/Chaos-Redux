# Event 6 Wallonia alternative portrait source-clearance handoff

## Outcome

The bounded source search produced two historically defensible, non-owned alternatives: Fernand Jacquet for an AFX commander role and Charles de Broqueville for an AFX civic role. Albert Devèze has an excellent source but is blocked by the vanilla `BEL_albert_deveze` owner. Gérard Leman was rejected because he died in 1920, and Jules Destrée remains the current Chaos Redux AFX civic owner.

## Files delivered

- Source package: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_role_source_clearance/`.
- Manifest: `manifest.md`.
- Ownership evidence: `ownership_audit.md`.
- Parent wiring notes: `gfx_handoff.md`.
- SHA-256 inventory: `source_hashes.sha256`.
- Contact sheet: `contact_sheets/walloon_role_source_clearance_contact_sheet.png`.
- Jacquet unchanged master and exact crop: `source_masters/fernand_jacquet_1915_memorix_heu_139408cf.jpg`, `source_crops/fernand_jacquet_1915_head_shoulders_crop.png`, and the matching JSON equality proof.
- de Broqueville unchanged master and exact crop: `source_masters/charles_de_broqueville_1909_1920_commons.jpg`, `source_crops/charles_de_broqueville_commons_head_shoulders_crop.png`, and the matching JSON equality proof.
- Devèze comparison master and exact clean crop are retained only to document the vanilla-owner blocker.

## Review decisions needed from parent

- Accept or reject the unknown-photographer rights uncertainty for Jacquet.
- Confirm whether de Broqueville's partially occluded left ear satisfies the project's strict portrait identity gate. If it does not, use Jacquet only and request another civic source rather than reconstructing the feature.
- If either identity is accepted, run the parent-owned portrait processor, standard DDS converter, `.gfx` registration, localisation, and character wiring. Those steps were intentionally not performed here.

## Simplifications and blockers

No source image was generated, retouched, restored, or transformed beyond exact-pixel head-and-shoulders cropping. No final DDS, GFX, gameplay, localisation, or runtime changes were made. Jacquet has an unknown photographer and therefore remains `needs_user_review`; de Broqueville is source-cleared on LOC no-known-restrictions evidence but still needs the parent identity gate decision.
