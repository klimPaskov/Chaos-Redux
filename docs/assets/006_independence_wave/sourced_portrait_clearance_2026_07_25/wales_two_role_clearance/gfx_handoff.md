# Event 6 Wales portrait source handoff

This is a source-clearance handoff only. No DDS or final `156x210` PNG exists yet, and no `.gfx` file was edited.

| WLS role | Candidate source | Existing sprite | Reserved runtime texture | Status |
| --- | --- | --- | --- | --- |
| Civic or national council | W. J. Gruffydd, `source_crops/w_j_gruffydd_civic_crop.png` | `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `needs_user_review` — postwar 1946 source; CC BY-SA attribution required |
| Mountain or territorial commandant | Lewis Pugh Evans VC, `source_crops/lewis_pugh_evans_commander_crop.png` | `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `needs_user_review` — circa-1918 source; Public Domain under Commons PD-Old |

## Main-agent wiring boundary

Use `interface/006_independence_wave_region_01_portraits.gfx` if either candidate passes the parent-owned downstream identity/style/provenance review. Keep the existing sprite names and reserved texture paths stable. The parent must reconcile the current civic localisation (`WLS_independence_wave_national_council` currently names Saunders Lewis) before any accepted candidate is made a named runtime character. This subtask does not edit localisation, characters, history, GFX or gameplay.

## Required downstream sequence

1. Treat each JPEG master and exact crop as immutable identity evidence.
2. Feed only the exact crop to source-locked identity-preserving ImageGen; use canonical leader/commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` for style only.
3. Compare unchanged master, exact crop, raw ImageGen result and deterministic `156x210` candidate at native and enlarged scales. Obtain an independent likeness/style/provenance audit.
4. Convert only an independently approved `156x210` PNG to DDS with the repository converter and wire it to the reserved path.

The source files and equality JSON are in the sibling `source_masters/`, `source_master_png/` and `source_crops/` folders. The comparison sheet is `contact_sheets/wales_two_role_clearance_contact_sheet.png`; the authoritative data is `manifest.json`.

