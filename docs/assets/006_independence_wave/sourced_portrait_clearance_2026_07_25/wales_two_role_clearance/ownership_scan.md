# IW-002 Wales portrait ownership scan - 2026-07-25

This scan covers the alternative grounded male identities considered for the WLS civic and mountain-commandant portrait consumers before any downstream portrait treatment. It is source-clearance evidence only and does not edit character definitions, country histories, interface/GFX, localisation or gameplay.

## Roots checked

- Current Chaos Redux repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`
- Installed vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- Approved Kaiserreich reference: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605`
- Approved reference mod: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196`
- Approved reference mod: `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1458561226`

Within each root, the search covered `common/characters/`, `history/countries/`, `interface/`, `localisation/` and `gfx/leaders/`. Text matching used case-insensitive exact and variant forms and excluded binary textures and unrelated build artefacts.

## Terms checked

| Candidate | Exact and variant forms |
| --- | --- |
| James Henry Thomas (J. H. Thomas) | `James Henry Thomas`; `J. H. Thomas`; `James_Henry_Thomas`; `JH Thomas` |
| Requested Major-General Gervase Thorpe / IWM namesake Gervase Thorpe Spendlove | `Gervase Thorpe`; `Gervase Thorpe Spendlove`; `Major-General Gervase Thorpe`; `Thorpe Spendlove`; `Gervase_Thorpe`; `gervase_thorpe`; `Spendlove`; `53rd Welsh Division` |
| Major-General Robert Knox Ross | `Robert Ross`; `Robert Knox Ross`; `Major-General Robert Ross`; `R. L. Ross`; `53rd Welsh Division` |
| Lewis Edward Valentine | `Lewis Valentine`; `Lewis Edward Valentine`; `Parch Lewis Valentine`; `Valentine` |
| Thomas Wynford Rees | `Thomas Wynford Rees`; `T. W. Rees`; `RAJ_thomas_wynford_rees`; `SE3459` |
| W. J. Gruffydd | `Gruffydd`; `William John Gruffydd`; `W. J. Gruffydd`; `WJ Gruffydd` |
| Lewis Pugh Evans | `Lewis Pugh Evans`; `Pugh Evans` |
| Saunders Lewis | `Saunders Lewis`; `WLS_saunders_lewis` |

## Results

| Candidate | Current Chaos Redux | Vanilla | Kaiserreich 1521695605 | 2265420196 | 1458561226 | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| James Henry Thomas (J. H. Thomas) | No match | No match | No match | No match | No match | Clear additive source candidate; no transfer guard found. |
| Requested Major-General Gervase Thorpe / IWM namesake Gervase Thorpe Spendlove | No match for requested identity | No match | No match | No match | No match | Ownership scan is not a clearance: IWM HU 126780 identifies a distinct Second Lieutenant Gervase Thorpe Spendlove killed in 1914, so the source is blocked for identity mismatch. |
| Major-General Robert Knox Ross | No match | No match | No match | No match | No match | Ownership clear, but blocked because the exact crop leaves insufficient facial resolution. |
| Lewis Edward Valentine | No meaningful current owner | No match | Active WLS identity, recruitment, portraits and localisation | No match | No match | Rejected active Kaiserreich owner. |
| Thomas Wynford Rees | No match | No match | Active `RAJ_thomas_wynford_rees` identity and portrait/localisation consumers | No match | No match | Rejected active Kaiserreich owner; source also fails crop scale. |
| W. J. Gruffydd | No match | No match | No match | No match | No match | Ownership clear, but source is `blocked_postwar_source` because it is dated 1946. |
| Lewis Pugh Evans | No match | No match | No match | No match | No match | Ownership clear, but source is `rejected_duplicate_failed_source` because HU 93411 was used by two failed trials. |
| Saunders Lewis | Current WLS localisation/consumer exists | No match | Active WLS identity and portrait/localisation consumers | No match | No match | Excluded by the existing age gate and active Kaiserreich ownership. |

## Active ownership evidence

- Lewis Valentine: Kaiserreich `common/characters/WLS characters.txt:62-71`, `history/countries/WLS - Wales.txt:35`, `interface/kaiserreich/portraits/WLS_portraits.gfx:15-20` and `localisation/english/KR_country_specific/WLS - Wales l_english.yml:201-202`.
- Thomas Wynford Rees: Kaiserreich `common/characters/RAJ characters.txt:183-192`, `history/countries/RAJ - Dominion of India.txt:166,242`, `interface/kaiserreich/portraits/RAJ_portraits.gfx:95-100` and the corresponding localisation entries at lines 878-879.
- Saunders Lewis: the existing age-gate package records Kaiserreich WLS character, portrait and localisation ownership; this clearance package does not reuse that identity.

## Existing WLS consumer evidence

- `interface/006_independence_wave_region_01_portraits.gfx:63-64`: `GFX_portrait_WLS_independence_wave_national_council` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.
- `interface/006_independence_wave_region_01_portraits.gfx:67-68`: `GFX_portrait_WLS_independence_wave_mountain_commandant` -> `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`.
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml:5-7`: the current civic label names Saunders Lewis and the commandant remains a role label. This package does not alter either surface.

## Collision examples excluded from this package

- Aneurin Bevan was excluded because Kaiserreich `1521695605` actively defines `ENG_aneurin_bevan`, recruits him in `history/countries/ENG - Union of Britain.txt`, defines an army-small portrait consumer and localises the identity.
- William Ambrose Bebb was excluded under the earlier Event 6 scan because Kaiserreich `1521695605` owns `WLS_ambrose_bebb`, its WLS portrait consumers and localisation.
- David Rhys Grenfell and George Cornwallis-West are not ownership collisions in the checked roots, but their earlier source photographs were not retried because the parent reported failed likeness passes.

## Interpretation

J. H. Thomas passes the subject-ownership gate as an additive source candidate. The HU 126780 namesake source does not pass identity clearance: the IWM page identifies a different person who died in 1914, and no ownership no-match can bridge that identity mismatch to the requested Major-General Gervase Thorpe. The source, decoded master and crop remain blocked provenance evidence only; they must not enter ImageGen or runtime reuse. The parent still owns identity reconciliation, source-locked treatment, independent likeness/style/provenance review, deterministic `156x210` processing and DDS conversion for any correctly identified replacement. Robert Ross is retained only as blocked research evidence because the exact crop is too small for reliable downstream likeness work. Valentine, Rees and Saunders must not be cloned without an explicit guarded transfer decision, while Gruffydd and Evans remain blocked or rejected for their separate source reasons.
