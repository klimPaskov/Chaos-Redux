# IW-002 Wales portrait ownership scan — 2026-07-25

This scan covers the two alternative grounded male identities in this package before any downstream portrait treatment. It is source-clearance evidence only and does not edit character definitions, country histories, interface/GFX, localisation, or gameplay.

## Roots checked

- Current Chaos Redux repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`
- Installed vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- Approved Kaiserreich reference: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605`
- Approved reference mod: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196`
- Approved reference mod: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1458561226`

Within each root, the search covered `common/characters/`, `history/countries/`, `interface/`, `localisation/`, and `gfx/leaders/`. Text matching used case-insensitive exact and variant forms and excluded binary textures and unrelated build artefacts.

## Terms checked

| Candidate | Exact and variant forms |
| --- | --- |
| W. J. Gruffydd | `Gruffydd`; `William John Gruffydd`; `W. J. Gruffydd`; `WJ Gruffydd` |
| Lewis Pugh Evans | `Lewis Pugh Evans`; `Pugh Evans` |

## Results for selected candidates

| Candidate | Current Chaos Redux | Vanilla | Kaiserreich 1521695605 | 2265420196 | 1458561226 | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| W. J. Gruffydd | No matching character, recruitment, portrait, GFX, or localisation owner found | No match | No match | No match | No match | Clear for additive source treatment; no transfer guard required |
| Lewis Pugh Evans | No matching character, recruitment, portrait, GFX, or localisation owner found | No match | No match | No match | No match | Clear for additive source treatment; no transfer guard required |

No match means no text owner was found in the checked role-bearing roots. It does not imply that a generic incidental surname or an unrelated historical person is an ownership collision. Literal prose, ship names, equipment, streets, and unrelated credits were not treated as character ownership.

## Existing WLS consumer evidence

The current project already reserves the following parent-owned consumers:

- `interface/006_independence_wave_region_01_portraits.gfx:63-64`: `GFX_portrait_WLS_independence_wave_national_council` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.
- `interface/006_independence_wave_region_01_portraits.gfx:67-68`: `GFX_portrait_WLS_independence_wave_mountain_commandant` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`.
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-7`: the current civic label names Saunders Lewis and the commandant remains a role label. This package does not alter either surface.

## Collision examples excluded from this package

- Aneurin Bevan was considered because the 1943 National Portrait Gallery photograph has strong face geometry. Kaiserreich `1521695605` actively defines `ENG_aneurin_bevan` in `common/characters/ENG characters.txt`, recruits him in `history/countries/ENG - Union of Britain.txt`, defines `GFX_portrait_ENG_aneurin_bevan_army_small` in `interface/kaiserreich/portraits/ENG_portraits.gfx`, and localises `ENG_aneurin_bevan`. This is a meaningful live owner; no clone is allowed without a guarded transfer contract.
- William Ambrose Bebb remains excluded under the earlier Event 6 scan because Kaiserreich `1521695605` owns `WLS_ambrose_bebb`, its WLS portrait consumers and localisation.
- David Rhys Grenfell and George Cornwallis-West are not ownership collisions in the checked roots, but their earlier source photographs were not retried because the parent reported failed likeness passes.

## Interpretation

Both selected candidates pass the subject-ownership gate as additive source candidates. They still require parent-owned identity reconciliation, source-locked ImageGen, independent likeness/style/provenance review, deterministic `156x210` processing, and DDS conversion. The ownership result does not authorize generated portraits or simultaneous reuse of any already-owned identity.

