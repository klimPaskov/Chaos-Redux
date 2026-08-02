# IW-177 Fiji Vishnu Deo repaint evidence v109

Date: 2026-08-03.

Scope: source-linked visual evidence only. No gameplay, character, GFX, DDS, localisation, flag, allocator, dispatch, or attestation files were changed.

## Candidate and source chain

The candidate is Pt. Vishnu Deo, a named adult male Fiji-born Indo-Fijian civic and communal leader. The preserved source chain is the October 1929 *Modern Review* page scan and its exact head-and-shoulders crop:

- Source page: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/n474_w4000.jpg`.
- Exact crop: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/vishnu_deo_modern_review_crop.png`.
- Crop proof: `vishnu_deo_modern_review_crop.json` with source equality verification.
- Archival context: *The Modern Review*, October 1929, printed page 459, captioned “Mr. Vishnu Deo.” The earlier source handoff records the Internet Archive scan, Wikimedia Commons identity corroboration, and anonymous-author/public-domain caveat.

## HOI4 repaint evidence

The source crop was passed through an identity-preserving HOI4 painted-gouache/oil ImageGen prompt. The generated result is retained in the ignored evidence workspace:

- Prompt: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/prompts/vishnu_deo_identity_preserve_hoi4.md`.
- Repaint: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/imagegen_results/vishnu_deo_identity_preserve_hoi4.png`.
- Repaint SHA-256: `376883c89bab545d86e854d0b9d098b272401d5aa185c101fdf4f211b32901be`.
- Repaint dimensions: `1254x1254`.
- Metadata: `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/metadata/vishnu_deo_identity_preserve_hoi4.json`.

The repaint is visually a restrained dark-background HOI4-style portrait with a male head-and-shoulders framing and no emblem, text, second person, or modern prop. It is evidence-only; it has not been resized to a runtime consumer or converted to DDS.

## Fail-closed gates

This evidence does not clear IW-177. The current package gate remains closed because:

1. Vishnu Deo's 1929 civic source is period-valid for a 1936-centered visual, but the exact Event 006 country-leader role is not yet resolved. The existing package role is a Fiji founding-congress chair; the source handoff records that Deo returned to Fiji's Legislative Council in 1937, so a 1936 office continuity decision is still required.
2. The source is an anonymous halftone reproduction. The Commons `PD-India` claim and Internet Archive chain are documented, but the likeness quality and rights basis still require independent asset review before runtime promotion.
3. FIJ is still outside the exact content-attestation OR block. FORM-39 remains separately fail-closed for PNG/WPG named-community research, MFX identity/flag review, member consent, and collision checks.

No generic portrait, invented grounded identity, circa-1940s Sukuna substitution, advisor icon, fallback flag, or attestation shortcut was introduced.

## Required next review

An independent asset/identity audit must compare the source crop and repaint for likeness, HOI4 framing/style, and source-chain fidelity. A parent design decision must then choose whether a 1929 civic-candidate portrait is acceptable for the 1936 founding-congress-chair role. Only after those gates, a final runtime-size conversion, DDS hash check, character consumer wiring, full FIJ package audit, and FORM-39 dependency review may FIJ be reconsidered for admission.
