# Event 006 portrait source-mode and compile-attestation audit

**Audit date:** 2026-07-22  
**Scope:** all 45 non-`_small` DDS files in `gfx/leaders/006_independence_wave/`, their registered interface sprites and consumers, current portrait manifests/source modes, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.  
**Mode:** read-only audit; this handoff is the only file written. No asset, gameplay, GFX, localisation, or manifest content was changed. This is an inventory and remediation map, not a completion claim.

> **Parent correction after vanilla precedent inspection:** the 45-file Event 6
> inventory is complete, but its recommendation to retain IW-173 was rejected.
> Vanilla `_leader_portraits.gfx` maps
> `GFX_portrait_David_Kalakaua_Kawananakoa` to
> `gfx/leaders/Asia/Portrait_Asia_Generic_land_5.dds`, not to a sourced portrait
> of the real man. IW-173 therefore fails the same grounded source gate. The
> parent implemented an empty compile-time content-attestation set. This note
> supersedes every later statement in this handoff that says IW-173 may remain.

## Gate applied

Event 006 now applies the portrait source-mode gate from
`.agents/skills/chaos-redux-event-assets/SKILL.md`: a real, historical, restored,
regional, indigenous, dynastic, separatist, or otherwise plausibly historical
polity/community is **grounded** and must use a defensible sourced real person or
sourced archival material for the actual institution. A generated face or generated
institution is not allowed. A generated one-person portrait is allowed only for a
truly fictional high-chaos or impossible/supernatural identity.

All 45 rows below are grounded. None is `fictional_high_chaos`; the current manifests'
`fictional`/`ImageGen` labels describe production history, not an identity-class
exception. BAY Rupprecht and RHI Matthes are the two protected compliant files.

## Complete 45-file inventory

`small` sprites are included in the sprite/consumer column where they exist; they
are not additional table rows. “Replace” means the runtime file is live or wired
but its source mode fails the grounded gate. “Orphan” means the file is retained
readiness-pool art with no live sprite/consumer; it must not be promoted as-is.

| Runtime DDS | Interface sprite(s); consumer / role | Package execution ID | Identity class | Current source mode / evidence | Disposition | Candidate person or source direction |
|---|---|---|---|---|---|---|
| `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds` | **No sprite or consumer.** Intended Cornish coastal commander; readiness-pool only. | `iw_003` (IW-003 ACX Cornwall; no current adapter/attestation) | grounded — historical Cornish community | Generated ImageGen fictional male; `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/manifest.md`; unregistered readiness pool | **orphan** (replace before any future admission) | No defensible person in local evidence; source a period Cornish nationalist/coastal commander or archive the actual institution. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` | **No sprite or consumer.** Intended Cornish port/mines civic authority; readiness-pool only. | `iw_003` | grounded — historical Cornish community | Generated ImageGen fictional institutional male; same portrait-refresh manifest; unregistered | **orphan** (replace before any future admission) | No local candidate; source a period Cornish port/mines committee or real officeholder. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds` | **No sprite or consumer.** Intended Flanders/BEL-flemish overlay commander; readiness-pool only. | `iw_005` (IW-005 Flanders living-`BEL_flanders` overlay; no standalone adapter) | grounded — historical Flemish regional identity | Generated ImageGen fictional male; portrait-refresh manifest; no standalone AEX registration | **orphan** (not a standalone Event 006 asset) | No local standalone candidate; source a real period Flemish industrial/security officeholder only if the overlay ever receives an admitted portrait surface. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AEX_flemish_civil_industrial_board.dds` | **No sprite or consumer.** Intended Flemish civil/industrial board; readiness-pool only. | `iw_005` | grounded — historical Flemish regional identity | Generated ImageGen fictional institutional male; portrait-refresh manifest; no standalone registration | **orphan** (not a standalone Event 006 asset) | No local candidate; source the actual `BEL_flanders` institutional archive or a defensible period officeholder if a real portrait is later authorized. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` | `GFX_portrait_AFX_walloon_provisional_assembly`; `AFX_walloon_provisional_assembly`, civilian country leader (centrism/socialism/oligarchism). | `iw_006` (IW-006 AFX Wallonia) | grounded — historical/regional Walloon polity | Generated ImageGen fictional institutional male; portrait-refresh manifest, `institutional_raw_outputs/`; status `approved_for_runtime` | **replace** | Source a documented 1930s Walloon provisional assembly/real presiding officeholder; no person/image license is present locally. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` | `GFX_portrait_AFX_walloon_reserve_commander` + `_small`; `AFX_walloon_reserve_commander`, civilian/army corps commander. | `iw_006` | grounded — historical/regional Walloon polity | Generated ImageGen fictional male; portrait-refresh `raw_outputs/`; matching 65x67 derivative | **replace** | Source a period Walloon reserve/industrial commander with a defensible archive/license. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` | `GFX_portrait_AGX_friesland_coastal_commander` + `_small`; `AGX_friesland_coastal_commander`, army corps commander. | `iw_007` (IW-007 AGX Frisia) | grounded — historical/regional West Frisian polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Source a period West Frisian coastal commander or actual coastal-security archive. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | `GFX_portrait_AGX_friesland_coastal_council`; `AGX_friesland_coastal_council`, civilian country leader (centrism/socialism/oligarchism). | `iw_007` | grounded — historical/regional West Frisian polity | Generated ImageGen fictional institutional male; portrait-refresh `institutional_raw_outputs/` | **replace** | Source a period West Frisian coastal council/real chair or archival institutional material. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds` | `GFX_portrait_AJX_karl_becker` + `_small`; `AJX_karl_becker`, civilian/army corps commander. | `iw_010` (IW-010 AJX Saar) | grounded — historical League-governed Saar territory | Generated ImageGen fictional male; portrait-refresh manifest; sprite name differs from texture stem; matching 65x67 derivative | **replace** | Source a documented 1920–35 Saar industrial/security official or commander. unresolved |
| `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | `GFX_portrait_AJX_friedrich_hoffmann`; `AJX_friedrich_hoffmann`, civilian neutral-commission leader. | `iw_010` | grounded — historical League-governed Saar territory | Generated ImageGen fictional institutional male; portrait-refresh manifest | **replace** | Source the actual Saar municipal neutral commission or a period chair with archive rights. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_antioco_melis.dds` | `GFX_portrait_ARX_independence_wave_antioco_melis`; `ARX_sardinian_provisional_assembly`, civilian leader. | `iw_018` (IW-018 ARX Sardinia) | grounded — historical/regional Sardinian polity | Generated ImageGen fictional adult male; `mediterranean_portraits_2026_07_16/manifest.md`, per-file `source_kind: fictional` | **replace** | Antioco Melis is only onomastically attested in local package research; source a real period Sardinian assembly officeholder/portrait. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds` | `GFX_portrait_ARX_independence_wave_gavino_piras`; `ARX_gavino_piras`, civilian/army corps commander. | `iw_018` | grounded — historical/regional Sardinian polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Gavino Piras is a name-only local identity; source a period Sardinian field commander. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds` | `GFX_portrait_ARX_independence_wave_vittorio_pala`; `ARX_sardinian_crown_consultative_council`, civilian dynastic/crown leader. | `iw_018` | grounded — historical/regional/dynastic Sardinian polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Vittorio Pala components are onomastically attested locally; source a real Sardinian crown/council officeholder or archival council material. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_salvatore_licata.dds` | `GFX_portrait_ASX_independence_wave_salvatore_licata`; `ASX_salvatore_licata`, civilian/army corps commander. | `iw_019` (IW-019 ASX Sicily) | grounded — historical/regional Sicilian polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Source a documented 1930s Sicilian territorial commander; no local portrait candidate. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_sebastiano_restivo.dds` | `GFX_portrait_ASX_independence_wave_sebastiano_restivo`; `ASX_sicilian_provisional_assembly`, civilian country leader. | `iw_019` | grounded — historical/regional Sicilian polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Source a period Sicilian provisional assembly/real civic officeholder. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_vincenzo_lanza.dds` | `GFX_portrait_ASX_independence_wave_vincenzo_lanza`; `ASX_sicilian_crown_council`, civilian dynastic/crown leader. | `iw_019` | grounded — historical/regional/dynastic Sicilian polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Source a documented Sicilian crown/council officeholder or archival council material. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly.dds` | `GFX_portrait_ASY_independence_wave_civic_national_assembly`; `ASY_independence_wave_civic_national_assembly`, civilian country leader. | `iw_058` (IW-058 ASY Assyria) | grounded — historical/indigenous Assyrian polity | Generated ImageGen fictional collective institutional group; `iw043_iw058_generated_visuals_2026_07_18/manifest.md`, `manifests/asset_manifest.json` | **replace** | Source a real 1930s Assyrian civic national assembly or a defensible officeholder; local research is institutional only. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds` | `GFX_portrait_ASY_independence_wave_concordat_council`; `ASY_independence_wave_concordat_council`, civilian concordat/council leader. | `iw_058` | grounded — historical/indigenous Assyrian polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source the real concordat/cross-community council archive or a documented 1930s chair. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.dds` | `GFX_portrait_ASY_independence_wave_levies_guardianship`; `ASY_independence_wave_levies_guardianship`, emergency/Levies civilian leader. | `iw_058` | grounded — historical/indigenous Assyrian polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source an actual Assyrian Levies guardianship/officeholder archive; local Hansard/British Library research establishes the institution but no reusable portrait. unresolved |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_provisional_national_council.dds` | `GFX_portrait_ASY_independence_wave_provisional_national_council`; `ASY_independence_wave_provisional_national_council`, provisional civilian leader. | `iw_058` | grounded — historical/indigenous Assyrian polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source a period Assyrian provisional council/real officeholder or archival council material. unresolved |
| `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` | `GFX_portrait_BAY_independence_wave_mountain_commandant` + `_small`; `BAY_independence_wave_mountain_commandant`, civilian/army corps commander. | `iw_009` (IW-009 BAY Bavaria) | grounded — historical/regional/dynastic Bavarian polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Source a real period Bavarian mountain/territorial commander; protected Rupprecht does not cover this role. unresolved |
| `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` | `GFX_portrait_BAY_independence_wave_state_council`; `BAY_independence_wave_state_council`, civilian country leader. | `iw_009` | grounded — historical/regional/dynastic Bavarian polity | Generated ImageGen fictional institutional male; portrait-refresh manifest | **replace** | Source a real Bavarian state-council officeholder or archival council material; Rupprecht is route-specific only. unresolved |
| `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria`; `BAY_rupprecht_of_bavaria` restoration route (the restore helper also uses vanilla `GFX_portrait_BAY_rupprecht_of_bavaria`). | `iw_009` | grounded — historical/dynastic Bavarian polity | Sourced Franz Grainer portrait, c.1916, PD-Art/public-domain rationale; identity-preserving ImageGen edit; protected hash `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`; northern/western Europe source manifest | **compliant / protected** | Preserve Rupprecht and the traditional-crown/restoration route lock; do not generalize to republican, labor, military, or neutral openings. |
| `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | `GFX_portrait_BRI_independence_wave_civic_commission`; runtime-generated `BRI_independence_wave_civic_delegate`, civilian country leader. | `iw_004` (IW-004 BRI Brittany) | grounded — historical/regional/separatist Breton polity | Generated ImageGen fictional institutional male; portrait-refresh manifest; live BRI sprite | **replace** | François Debeauvais is the repository's reserved historical direction, but 1928 face detail is too weak and sharper 1932/1933 sources fail the US-rights review; source a stronger rights-cleared period Debeauvais/BRI delegate or actual civic archive. unresolved/blocked |
| `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | `GFX_portrait_BRI_independence_wave_coastal_commandant` + `_small`; runtime-generated `BRI_independence_wave_coastal_commandant`, civilian/army corps commander. | `iw_004` | grounded — historical/regional/separatist Breton polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Source a documented period Breton coastal/territorial commander; Debeauvais research does not clear this command role. unresolved |
| `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium`; `CHU_independence_wave_bolgar_civic_presidium`, civilian restoration/civic leader. | `iw_043` (IW-043 CHU Middle Volga/Bolgar) | grounded — historical/restored/regional Volga-Bolgar polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source a real Bolgar/Middle-Volga civic presidium or archival officeholder; UNESCO evidence is architecture/heritage only, not a portrait. unresolved |
| `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.dds` | `GFX_portrait_CHU_independence_wave_federal_presidium`; `CHU_independence_wave_federal_presidium`, civilian federal leader. | `iw_043` | grounded — historical/restored/regional Volga-Bolgar polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source a real Middle-Volga federal/presidium officeholder or archival institution. unresolved |
| `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_middle_volga_congress.dds` | `GFX_portrait_CHU_independence_wave_middle_volga_congress`; `CHU_independence_wave_middle_volga_congress`, civilian congress leader. | `iw_043` | grounded — historical/restored/regional Volga-Bolgar polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source a period Middle-Volga congress/convention archive or defensible real delegate. unresolved |
| `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds` | `GFX_portrait_CHU_independence_wave_river_security_directorate`; `CHU_independence_wave_river_security_directorate`, emergency/security civilian leader. | `iw_043` | grounded — historical/restored/regional Volga-Bolgar polity | Generated ImageGen fictional collective institutional group; IW-043/IW-058 generated-visual manifest | **replace** | Source an actual river-security directorate/period officer archive; no local portrait source. unresolved |
| `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_pasquale_venturi.dds` | `GFX_portrait_COR_independence_wave_pasquale_venturi`; `COR_pasquale_venturi`, civilian/army corps commander. | `iw_017` (IW-017 COR Corsica) | grounded — historical/regional Corsican polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Pasquale Venturi is a fictional/local onomastic role; source a period Corsican commander with rights-cleared archive. unresolved |
| `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_petru_santucci.dds` | `GFX_portrait_COR_independence_wave_petru_santucci`; `COR_corsican_municipal_congress`, civilian country leader. | `iw_017` | grounded — historical/regional Corsican polity | Generated ImageGen fictional adult male; Mediterranean portrait manifest; `source_kind: fictional` | **replace** | Petru/Santucci is locally onomastically attested; source a real Corsican municipal-congress officeholder or archival congress material. unresolved |
| `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong.dds` | `GFX_portrait_DOX_kwame_frimpong` + `_small`; `DOX_kwame_frimpong`, civilian/army corps commander. | `iw_093` (IW-093 DOX Asante; adapter-only, not content-attested) | grounded — restored/dynastic Asante polity | `generated_imagegen`, `fictional_male_army_commander_portraits`; `iw093_iw098_commanders_2026_07_19/manifest.json` explicitly sets `all_portraits_fictional: true`; matching 65x67 derivative | **replace before admission** | Source a real Asante/Gold Coast colonial veteran or Forest Guard commander; local package research supplies the role/name only, no image rights. unresolved |
| `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim.dds` | `GFX_portrait_DOX_kwaku_ntim` + `_small`; `DOX_kwaku_ntim`, civilian/army corps commander. | `iw_093` (adapter-only) | grounded — restored/dynastic Asante polity | Generated ImageGen fictional commander; IW-093/IW-098 commanders manifest; matching 65x67 derivative | **replace before admission** | Source a real Asante Forest Guard organizer/field commander with defensible archive/licence. unresolved |
| `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds` | `GFX_portrait_DOX_prempeh_ii`; `DOX_prempeh_ii`, male civilian country leader (despotism/centrism). | `iw_093` (adapter-only) | grounded — restored/dynastic Asante polity | Sourced 31 Jan 1935 National Archives UK CO 1069-44-12, OGL v1.0 attribution; identity-preserving ImageGen edit; `iw093_asante_prempeh_ii_2026_07_18/manifest.md`; runtime hash `5fcab91f052810e66f3795734c55219488a592e513ab06f737dcbfb5cabbb26e` | **compliant** | Preserve Nana Otumfuo Agyeman Prempeh II and the 1935 restoration-day source/attribution. |
| `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds` | `GFX_portrait_FSM_independence_wave_inter_island_congress_chair`; `FSM_independence_wave_inter_island_congress_chair`, civilian country leader. | `iw_179` (IW-179 FSM Micronesia) | grounded — historical/regional Micronesian polity | Generated ImageGen fictional adult male Elias Kihleng; `form48_pacific_leader_portraits_2026_07_17/manifest.md`; live sprite/character | **replace** | Source a real 1930s Micronesian inter-island congress/chair or archival island-government record. unresolved |
| `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds` | `GFX_portrait_HBX_independence_wave_civic_convention`; `HBX_independence_wave_civic_convention_chair`, civilian country leader. | `iw_184` (IW-184 HBX California) | grounded — real/regional California polity | Generated ImageGen fictional adult male Daniel Mercer; FORM-48 Pacific leader-portrait manifest; live sprite/character | **replace** | Source a real 1930s California civic-convention/state officeholder or period convention archive. unresolved |
| `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` | `GFX_portrait_RHI_independence_wave_provisional_directorate`; runtime `RHI_independence_wave_provisional_directorate`, civilian country leader. | `iw_008` (IW-008 RHI Rhineland) | grounded — historical/separatist/regional Rhineland polity | Generated ImageGen fictional institutional male; portrait-refresh manifest; live sprite/effect consumer | **replace** | Source a real 1923 Rhenish provisional-directorate officeholder or archival directorate material; protected Matthes is not universal. unresolved |
| `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` | `GFX_portrait_RHI_independence_wave_river_commandant` + `_small`; runtime `RHI_independence_wave_river_commandant`, civilian/army corps commander. | `iw_008` | grounded — historical/separatist/regional Rhineland polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Source a documented period Rhine-region river/territorial commander. unresolved |
| `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | `GFX_portrait_RHI_josef_friedrich_matthes`; `RHI_josef_friedrich_matthes` separatist/republic civilian route (restore helper's vanilla alias is separate). | `iw_008` | grounded — historical/separatist Rhineland polity | Bain News Service photograph, 22 Nov 1923, Library of Congress “no known restrictions,” identity-preserving ImageGen edit; protected hash `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`; northern/western Europe source manifest | **compliant / protected** | Preserve Matthes and the 1923 separatist/republic route lock; do not generalize to neutral corridor, military cabinet, or labor/constitutional openings. |
| `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` | `GFX_portrait_SCO_independence_wave_civic_convention`; runtime `SCO_independence_wave_civic_convention`, civilian country leader. | `iw_001` (IW-001 SCO Scotland) | grounded — historical/regional Scottish polity | Generated ImageGen fictional institutional male; portrait-refresh manifest; live sprite/effect consumer | **replace** | Local source research found no rights-cleared period Scottish nationalist leader; Roland Muirhead material is restricted. Source a rights-cleared 1930s Scottish civic/nationalist officeholder or archive. unresolved |
| `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` | `GFX_portrait_SCO_independence_wave_territorial_commandant` + `_small`; runtime `SCO_independence_wave_territorial_commandant`, civilian/army corps commander. | `iw_001` | grounded — historical/regional Scottish polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Source a rights-cleared 1930s Scottish territorial/mountain commander; no local candidate. unresolved |
| `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah.dds` | `GFX_portrait_SOK_bello_rabah` + `_small`; `SOK_bello_rabah`, civilian/army corps commander. | `iw_098` (IW-098 SOK Sokoto; adapter-only, not content-attested) | grounded — historical successor-sultanate/regional Sokoto polity | `generated_imagegen`, fictional male commander; IW-093/IW-098 commanders manifest; matching 65x67 derivative | **replace before admission** | Source a real Sokoto caravan/security officer with rights-cleared archival material. The local Hasan source is veiled/restricted and cannot substitute. unresolved |
| `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa.dds` | `GFX_portrait_SOK_umaru_gwadabawa` + `_small`; `SOK_umaru_gwadabawa`, civilian/army mounted frontier commander. | `iw_098` (adapter-only) | grounded — historical successor-sultanate/regional Sokoto polity | `generated_imagegen`, fictional male commander; IW-093/IW-098 commanders manifest; matching 65x67 derivative | **replace before admission** | Source a real Sokoto emirate/frontier commander; repository provides role direction only, no image rights. unresolved |
| `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `GFX_portrait_WLS_independence_wave_mountain_commandant` + `_small`; runtime `WLS_independence_wave_mountain_commandant`, civilian/army corps commander. | `iw_002` (IW-002 WLS Wales) | grounded — historical/regional Welsh polity | Generated ImageGen fictional male; portrait-refresh manifest; matching 65x67 derivative | **replace** | Saunders Lewis source is postwar (1973) and excluded; source a rights-cleared period Welsh territorial/mountain commander. unresolved |
| `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `GFX_portrait_WLS_independence_wave_national_council`; runtime `WLS_independence_wave_national_council`, civilian country leader. | `iw_002` | grounded — historical/regional Welsh polity | Generated ImageGen fictional institutional male; portrait-refresh manifest; live sprite/effect consumer | **replace** | Source a rights-cleared 1930s Welsh nationalist/civic officeholder or actual national-council archive; Saunders Lewis 1973 cannot be used. unresolved |

### Inventory totals

- 45 non-`_small` DDS rows: **3 compliant** (BAY Rupprecht, RHI Matthes, DOX Prempeh II), **38 live/wired generated rows requiring replacement**, and **4 orphan readiness-pool rows** (ACX/AEX; replacement required before any admission).
- Fourteen `_small` DDS files were also inspected. All fourteen are generated commander derivatives and therefore require the same grounded-source replacement/withdrawal decision as their large master; none is protected or compliant.
- Zero Event 006 custom advisor portraits, advisor sprites, or advisor DDS files are present; the ten `advisor`-mode records in older processor ledgers are commander-small dossier renders, not advisor assets.

## Compile-time content attestation

At audit time,
`has_independence_wave_runtime_package_content_attestation_for_execution_id`
contained these 16 IDs:

```text
iw_001 iw_002 iw_004 iw_006 iw_007 iw_008 iw_009 iw_010
iw_017 iw_018 iw_019 iw_043 iw_058 iw_173 iw_179 iw_184
```

Until every grounded portrait consumer is replaced with a sourced real person
or sourced archival institution, remove all 16 IDs from compile-time content
attestation:

```text
iw_001 iw_002 iw_004 iw_006 iw_007 iw_008 iw_009 iw_010
iw_017 iw_018 iw_019 iw_043 iw_058 iw_173 iw_179 iw_184
```

IW-173 defines no custom Event 6 DDS, but its preserved vanilla roster still
uses a generic portrait for David Kalakaua Kawananakoa. It therefore requires a
sourced replacement before re-admission. `iw_003`/`iw_005` are not in the
compile-time attestation set and have no live adapter; `iw_093` and `iw_098` are
adapter-only and must remain so until their remaining portrait/source blockers
are closed. Do not add any package merely because a DDS exists.

## Readiness, manifest, and documentation surfaces that must change

1. **Attestation authority:** remove all 16 IDs listed above from the gate in
   `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`;
   leave adapter and scenario-preflight rows separate until sourced replacement
   evidence and fresh package audits authorize individual re-admission.
2. **Runtime and sprite surfaces:** withdraw or replace the 38 live generated large
   DDS files and their 14 generated `_small` derivatives; keep the four ACX/AEX
   files unregistered/readiness-only or remove them only under a separately approved
   asset-cleanup change. Update the owning registrations in
   `interface/006_independence_wave_region_01_portraits.gfx`,
   `interface/006_independence_wave_brittany_portraits.gfx`,
   `interface/006_independence_wave_mediterranean_portraits.gfx`,
   `interface/006_independence_wave_iw043_iw058_portraits.gfx`,
   `interface/006_independence_wave_iw093_iw098_portraits.gfx`, and
   `interface/006_independence_wave_pacific_portraits.gfx` only when a replacement
   or explicit withdrawal is ready. Protected BAY/RHI sprite registrations remain.
3. **Character/effect consumers:** replace the generated `set_portraits` and static
   portrait blocks in the owning `common/characters/006_independence_wave_*.txt`
   and `common/scripted_effects/006_independence_wave_*package_effects.txt` files
   with the sourced person/institution identifiers and route locks. Preserve
   male metadata, role scope, commander-small pairing, and cleanup behavior; no
   generated or generic person may be retained as a fallback.
4. **Current portrait manifests:** supersede the “approved fictional” claims in
   `docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/` and
   its `portrait_provenance_manifest.json`, `institutional_provenance_manifest.json`,
   metadata, and package handoff; mark ACX/AEX as orphan readiness art and every
   other generated grounded row as replacement-required. Keep the protected BAY/RHI
   evidence separate.
5. **Regional generated package:** mark the eight Mediterranean rows in
   `docs/assets/006_independence_wave/mediterranean_portraits_2026_07_16/` as
   generated-grounded replacements; retain its source/processing evidence only as
   superseded audit history until sourced candidates exist.
6. **IW-043/IW-058 package:** update
   `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifest.md`,
   `manifests/asset_manifest.json`, and `manifests/portrait_visual_review.md` so
   the eight generated institutional portraits are not treated as valid grounded
   leader assets; the flag/report portions are unaffected by this portrait gate.
7. **Pacific package:** update
   `docs/assets/006_independence_wave/form48_pacific_leader_portraits_2026_07_17/`
   and `006_form48_pacific_individual_leader_portraits_2026_07_17.md` to mark HBX
   and FSM generated leaders replacement-required; HAW flag/focus/vanilla roster
   evidence is unaffected.
8. **IW-093/IW-098 commander package:** update
   `docs/assets/006_independence_wave/iw093_iw098_commanders_2026_07_19/manifest.json`
   and `iw093_iw098_commanders_2026_07_19_handoff.md` to mark its four generated
   grounded commander portraits and smalls replacement-required. Keep
   `iw093_asante_prempeh_ii_2026_07_18/manifest.md` as the compliant sourced
   Prempeh II authority; keep Hasan/Siddiq/Sokoto source blockers fail-closed.
9. **Root/source-of-truth docs:** reconcile the portrait section of
   `docs/assets/006_independence_wave/manifest.md`,
   `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md`,
   `docs/plans/006_independence_wave_plans/asset_research/006_real_portrait_and_symbol_sources.md`,
   and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` so they
   no longer call generated grounded portraits accepted runtime authority.
10. **Historical handoffs:** add a supersession note to
    `006_event6_male_commander_portrait_refresh_2026_07_18.md` and the related
    Mediterranean, NWE, Pacific, and IW-093/IW-098 portrait handoffs. Preserve the
    two protected BAY/RHI records and the sourced Prempeh II record; do not rewrite
    historical audit bodies.

## Remaining blockers

No grounded replacement candidate with both identity fit and reusable image evidence
was found locally for the 38 live generated rows or the 14 generated smalls. The
repository has strong source leads for BAY Rupprecht, RHI Matthes, and DOX Prempeh II,
but those are route-specific and cannot be generalized to neighboring roles. BRI
Debeauvais, SCO Muirhead, WLS Saunders Lewis, SOK Hasan/Siddiq, and the Mediterranean,
Pacific, NWE, CHU, and ASY role surfaces remain unresolved or rights-blocked. No
generated or generic fallback is authorized by this audit.
