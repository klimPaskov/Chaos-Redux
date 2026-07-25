# Event 6 Wales portrait source handoff

This is a source-clearance handoff only. No DDS or final `156x210` PNG exists yet, and no `.gfx` file was edited.

| WLS role | New candidate source | Exact crop | Existing sprite | Reserved runtime texture | Status |
| --- | --- | --- | --- | --- | --- |
| Civic or national council | James Henry Thomas (J. H. Thomas), `source_masters/j_h_thomas_bain_ggbain_29625_circa_1920.jpg` | `source_crops/j_h_thomas_civic_crop.png` (`3000x4000`) | `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `source_ready_for_parent_pipeline` - circa-1920 Library of Congress Bain source, Commons PD-Bain, clear head-and-shoulders geometry; preserve source-visible age exactly |
| Mountain or territorial commandant | Requested Major-General Gervase Thorpe (1877-1962); IWM HU 126780 depicts a different Second Lieutenant Gervase Thorpe Spendlove, killed 17 November 1914 | `source_crops/gervase_thorpe_commander_crop.png` (`592x640`) | `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `blocked_identity_mismatch` - retain source/crop only as provenance evidence; do not use for the 1936 commander, despite clear adult head-and-shoulders geometry |

## Main-agent wiring boundary

Use `interface/006_independence_wave_region_01_portraits.gfx` only if a candidate passes the parent-owned downstream identity, style and provenance review. Keep the existing sprite names and reserved texture paths stable. The parent must reconcile the current civic localisation, which names Saunders Lewis, before any accepted civic candidate becomes a named runtime character. The commandant localisation is currently a role label; HU 126780 cannot satisfy it because the image is a different 1914 namesake. A correctly identified Major-General Gervase Thorpe source is still required.

## Required downstream sequence

1. Treat each JPEG master, decoded PNG master and exact crop as immutable identity evidence.
2. Feed only an approved, correctly identified source crop to source-locked identity-preserving ImageGen; do not feed the HU 126780 crop because it is an identity mismatch. Use canonical leader and commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` for style only. If a later correctly identified IWM source is found, retain its exact IWM attribution and licence terms in downstream documentation and any distribution notice.
3. Compare unchanged master, exact crop, raw ImageGen result and deterministic `156x210` candidate at native and enlarged scales. Obtain an independent likeness, style and provenance audit.
4. Convert only an independently approved `156x210` PNG to DDS with the repository converter and wire it to the reserved path.

The authoritative comparison sheet is `contact_sheets/wales_two_role_clearance_contact_sheet_v7.png`; its SHA-256 is recorded in `manifest.json` after the final sheet build. Candidate metadata and dispositions are in `manifest.json`. HU 126780 is not a handoff candidate because its identity is the 1914 namesake; Robert Ross is also not a handoff candidate because its `310x300` crop leaves roughly 60-80 px of facial geometry.

## Explicitly rejected routes

Lewis Valentine is rejected because Kaiserreich owns the identity and its portrait consumers. Thomas Wynford Rees SE3459 is rejected because the source is a wide scene with a small face and Kaiserreich owns the subject. W. J. Gruffydd is blocked as postwar (1946). Lewis Pugh Evans HU 93411 is a duplicate of the failed Evans trials. HU 126780 is blocked because the IWM record identifies a distinct namesake who died in 1914, not the requested Major-General Gervase Thorpe. Robert Ross is blocked because its exact crop is too small for reliable face geometry. Saunders Lewis remains governed by the existing age-gate and Kaiserreich ownership evidence. David Rhys Grenfell and George Cornwallis-West remain excluded after failed likeness audits. No fallback or generic commander portrait is authorized by this package.
