# Event 006 Mediterranean / Volga / Assyria sourced-portrait research handoff

Date: 2026-07-22
Owner: sourced visual-asset subagent
Scope: replace the current large-only fictional Event 006 COR/ARX/ASX/CHU/ASY
country-leader/commander portrait roles with defensible real male historical
people or documented archival material. No gameplay, GFX, advisor assets,
cropping, processing, contact sheet, PNG, or DDS work was performed.

## Deliverables

- Complete 16-role ledger, source URLs, archive/author/date, rights notes,
  dimensions, consumer mapping, local paths, and uncertainty: [manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md).
- Twelve nonzero original source masters under
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/source_masters/`.
- SHA-256 inventory: [source_hashes.sha256](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/source_hashes.sha256).

## Status summary

| Status | Roles |
|---|---|
| `source_ready` | Current COR resolution: `COR_corsican_municipal_congress` → Adolphe Landry (stable institutional token with personal visible identity) and `COR_jean_chiappe` → Jean Chiappe (Gallica; replaces archived fictional `COR_pasquale_venturi`). The earlier COR role pairing in this research handoff is superseded by the implemented and independently audited package mapping. Other rows: `ARX_sardinian_provisional_assembly` → Emilio Lussu (Commons/Archivio Brigata Sassari); `ASX_sicilian_provisional_assembly` → Luigi Sturzo (Albert Kahn); `ASX_sicilian_crown_council` → Pietro Lanza di Scalea (Commons/ICCD); `CHU_independence_wave_middle_volga_congress` → Mirsaid Sultan-Galiev; `ASY_independence_wave_provisional_national_council` → Gallo Shabo (Aramean Archive) |
| `needs_user_review` | `ARX_sardinian_crown_consultative_council` → Giovanni Battista Melis (1963 post-era/low resolution); `CHU_independence_wave_river_security_directorate` → Musa Dzhalil (museum rights/late-1930s); `ASY_independence_wave_civic_national_assembly` → Naum Faiq (page scan requires crop); `ASY_independence_wave_levies_guardianship` → Agha Petros (source page gives no explicit license) |
| `blocked` | Luigi Efisio Marras, Carlo Geloso, Shamil Usmanov, Galimzhan Ibrahimov, Malik Ismail II (5 roles: four retry rows still lack a verified local bitstream or explicit source-rights chain; Malik Ismail II is separately disqualified by watermark and rights uncertainty) |

`ASY_shimun_eshai` is an additional blocked research lead: the Foundation image
archive has no stated reuse license and no file was copied. No generated or
generic replacement was used for any grounded identity.

## Source-master hashes

- `source_masters/mediterranean/cor_adolphe_landry.jpg` —
  `f1afc654cfeb655313cb943aaab54e438df8c483abe54a96dbf229ad6fa7c9a8`
- `source_masters/mediterranean/cor_jean_chiappe_gallica_f1_highres.jpg` —
  `2dd15d292a7caa8081b099e7234b41960ede3f2e46318d9b7e752b4570b9d378`
- `source_masters/mediterranean/asx_luigi_sturzo_albert_kahn_big.jpeg` —
  `4c18893744627c83761ee2b838a18f2f4798026811b888ecfb96d1f1d7a168ec`
- `source_masters/mediterranean/asx_pietro_lanza_di_scalea_commons_original.jpg` —
  `5cbf419d7f33539e726f0ef4089b1c9995e1bfdbcd8b581f8eaa996659d02f0b`
- `source_masters/volga/chu_mirsaid_sultan_galiev.jpg` —
  `4eb3707a50bb6d7ccf193773172b415dd4b1c4f83e09669dd9f2850972e46319`
- `source_masters/volga/chu_musa_dzhalil_tatmuseum_original.jpg` —
  `0bdef46f14a209b1dc749ff9063af7323006e34668c037f9367b96e609605489`
- `source_masters/assyria/asy_naum_faiq_archive_org_page_n10.jpg` —
  `f8c6852056eadc30e61e1baa311185265d8fff2d7849f4c2d894fd5bf41d50bd`
- `source_masters/assyria/asy_gallo_shabo_aramean_archive_original.webp` —
  `65601e55c8a07cfce7dd547253065cae0930ec6e6382995bc04313338d7d22db`
- `source_masters/sardinia/arx_emilio_lussu_commons_original.jpg` —
  `b91efc1de64c98ec591a97e41fc79d1823d35ee8be0797ce5525920736ba633a`
- `source_masters/sardinia/arx_giovanni_battista_melis_commons_original.jpg` —
  `2c27b2e5cbfa4a5b72924a344f23cae0c136bcde52e4eb1f0df25a28a710e970`
- `source_masters/assyria/asy_agha_petros_atour_original.jpg` —
  `e1deec1794568a765ab26a6c7611c15255748641b827e33d147f47e8826f5990`
- `source_masters/assyria/asy_malik_ismail_ii_tyari_family_original.jpg` —
  `0e40fcdffc983266da7d486f339d5b962f172dfb9c361c3e8d3248a264e90ad7`

## Parent integration notes

1. Treat the manifest as a research ledger, not runtime approval. Do not wire a
   `needs_user_review` or `blocked` row.
2. Do not use the Malik Ismail file: it is visibly watermarked and the family
   page provides no reuse grant.
3. Do not copy Mar Eshai Shimun imagery from the Foundation without separate
   written permission.
4. The second bounded retry retrieved Jean Chiappe from Gallica, Luigi Sturzo
   from the Albert Kahn collection, Gallo Shabo from the Aramean Archive,
   Pietro Lanza di Scalea via the verified Commons original redirect, and
   Emilio Lussu via the verified Commons original redirect. Giovanni Battista
   Melis was recovered but remains `needs_user_review` because the source is a
   1963 post-era, 214x263 portrait. The remaining four retry rows are blocked;
   do not substitute a generated face.
5. After a separate rights/visual review, process only approved masters with the
   repository portrait pipeline; this handoff intentionally contains no DDS/GFX
   path.

## Simplifications / blockers

- Wikimedia Commons returned HTTP 429 during the paced source download window;
  four otherwise well-documented retry candidates remain ledgered but have no
  local bitstream or independently usable source-rights chain in this pass.
- Four downloaded sources need review for explicit reuse rights or framing;
  one is a watermarked/rights-blocked candidate retained only as evidence.
- No fallback, generated, generic, modern, female, or invented identity was
  introduced.
