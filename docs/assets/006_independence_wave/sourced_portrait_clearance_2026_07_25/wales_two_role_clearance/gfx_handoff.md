# Event 6 Wales portrait source handoff

This is a source-clearance handoff only. No DDS or final `156x210` PNG exists yet, and no `.gfx` file was edited.

| WLS role | New candidate source | Exact crop | Existing sprite | Reserved runtime texture | Status |
| --- | --- | --- | --- | --- | --- |
| Civic or national council | James Henry Thomas (J. H. Thomas), `source_masters/j_h_thomas_bain_ggbain_29625_circa_1920.jpg` | `source_crops/j_h_thomas_civic_crop.png` (`3000x4000`) | `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `needs_user_review` - circa-1920 Library of Congress Bain source, Commons PD-Bain, clear head-and-shoulders geometry |
| Mountain or territorial commandant | Major-General Robert Knox Ross, `source_masters/robert_ross_iwm_negative_h24742_1942.jpg` | `source_crops/robert_ross_commander_crop.png` (`310x300`) | `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `needs_user_review` - 20 October 1942 IWM/War Office source, Commons PD-UKGov, tight head-and-shoulders crop |

## Main-agent wiring boundary

Use `interface/006_independence_wave_region_01_portraits.gfx` only if a candidate passes the parent-owned downstream identity, style and provenance review. Keep the existing sprite names and reserved texture paths stable. The parent must reconcile the current civic localisation, which names Saunders Lewis, before any accepted civic candidate becomes a named runtime character. The commandant localisation is currently a role label and requires the parent-owned identity decision for Robert Ross.

## Required downstream sequence

1. Treat each JPEG master, decoded PNG master and exact crop as immutable identity evidence.
2. Feed only the exact crop to source-locked identity-preserving ImageGen; use canonical leader and commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` for style only.
3. Compare unchanged master, exact crop, raw ImageGen result and deterministic `156x210` candidate at native and enlarged scales. Obtain an independent likeness, style and provenance audit.
4. Convert only an independently approved `156x210` PNG to DDS with the repository converter and wire it to the reserved path.

The authoritative comparison sheet is `contact_sheets/wales_two_role_clearance_contact_sheet_v5.png`, SHA-256 `d25308ecd1f20696b423f0770b436b4fdcef920d2c39d228912b12108dfb87f8`. Candidate metadata and dispositions are in `manifest.json`.

## Explicitly rejected routes

Lewis Valentine is rejected because Kaiserreich owns the identity and its portrait consumers. Thomas Wynford Rees SE3459 is rejected because the source is a wide scene with a small face and Kaiserreich owns the subject. W. J. Gruffydd is blocked as postwar (1946). Lewis Pugh Evans HU 93411 is a duplicate of the failed Evans trials. Saunders Lewis remains governed by the existing age-gate and Kaiserreich ownership evidence. David Rhys Grenfell and George Cornwallis-West remain excluded after failed likeness audits.
