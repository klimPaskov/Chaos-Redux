# Event 006 northern and western Europe asset-source handoff

## Scope completed

Completed the bounded source-research and allowed source-production tranche for:

- IW-001 Scotland / SCO;
- IW-002 Wales / WLS;
- IW-003 Cornwall / ACX;
- IW-004 Brittany / BRI;
- IW-005 Flanders / AEX;
- IW-006 Wallonia / AFX;
- IW-007 Frisia / AGX;
- IW-008 Rhineland / RHI;
- IW-009 Bavaria / BAY;
- IW-010 Saar / AJX;
- IW-012 Icelandic emergency republic / ICE.

The work follows the accepted source-mode split. It reuses installed registered
flags in place, retains sourced designs as inputs for the four live historical
ImageGen flag families and the AEX lion solely as vanilla-overlay evidence, and
produces real-person portraits only where identity, route context,
date, and rights support them. No invented or generated substitute was used.

No gameplay, localisation, `.gfx`, `.gui`, spreadsheet, specification, or event
file was edited. No commit was created.

## Delivered assets

### Historical or community motif source packages

- ACX: St Piran's Cross source SVG, source PNG render, and processed review PNG.
- AEX: historical Lion of Flanders arms source SVG, source PNG render, and
  processed review PNG.
- AFX: CC0 Walloon rooster vector source SVG, source PNG render, and processed
  review PNG, explicitly distinguished from Pierre Paulus's restricted original
  watercolor.
- AGX: West Frisian provincial flag source SVG, source PNG render, and processed
  review PNG, explicitly not universalized as a pan-Frisian flag.
- AJX: exact 1920-1935 Saar Territory flag source SVG, source PNG render, and
  processed review PNG, retained as neutral-commission route evidence only.

No flag TGA was created by this source tranche. The downstream live-flag repair
uses the ACX, AFX, AGX, and AJX sources as exact historical design references.
AEX is excluded because it is a vanilla `BEL_flanders` cosmetic overlay.

### Real-person portrait packages

- BRI François Debeauvais: the rights-cleared 1928 party-congress source is
  retained as identity research only. Its face is too weak for an
  identity-preserving final. Sharper 1932 and 1933 candidates fail the United
  States rights review. No processed final, runtime DDS, or sprite registration
  is retained, and BRI content-readiness remains unset.
- RHI Josef Friedrich Matthes: 1923 Library of Congress Bain source,
  identity-preserving HOI4 painted master, explicit head-and-shoulders crop,
  156x210 processed PNG, comparison evidence, and uncompressed BGRA DDS.
  Rhenish separatist/republic route only.
- BAY Rupprecht of Bavaria: circa-1916 Franz Grainer public-domain source,
  corrected identity-preserving HOI4 painted master, explicit
  head-and-shoulders crop, 156x210 processed PNG, comparison evidence, and
  uncompressed BGRA DDS. Traditional crown/restoration route only.

## Files added

- `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md`
- `docs/assets/006_independence_wave/northern_western_europe_gfx_handoff.md`
- `docs/assets/006_independence_wave/_tooling/build_northern_western_europe_sources.py`
- five SVG files under
  `docs/assets/006_independence_wave/source_svg/country_symbols/`
- five source PNG renders under
  `docs/assets/006_independence_wave/source_png/country_symbols/`
- three portrait source images under
  `docs/assets/006_independence_wave/source_png/portraits/`
- five processed symbol review PNGs under
  `docs/assets/006_independence_wave/processed_png/country_symbols/`
- two 156x210 processed portrait PNGs under
  `docs/assets/006_independence_wave/processed_png/portraits/`
- real-person crop metadata, prompt provenance, source/candidate comparison
  sheets, and the explicit BRI blocker record under
  `docs/assets/006_independence_wave/`
- `docs/assets/006_independence_wave/contact_sheets/006_northern_western_europe_sourced_assets.png`
- `docs/assets/006_independence_wave/contact_sheets/006_northern_western_europe_final_dds_decoded.png`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`
- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`

## Files updated

- `docs/assets/006_independence_wave/manifest.md`
  - links the bounded country-package source manifest and states its generated
    versus sourced boundary.
- `docs/assets/006_independence_wave/gfx_handoff.md`
  - links the dedicated portrait registration and route-lock handoff.

## Package conclusions for the parent

| Package | Parent action |
|---|---|
| SCO | Reuse installed flags. Keep Lion Rampant royal-route-only. Retain a sourced-real portrait blocker unless a new cleared prewar source is found. |
| WLS | Reuse installed flags only under the accepted registered-tag rule and preserve the explicit 1959-layout caveat. Do not use the 1973 Saunders Lewis image. |
| ACX | Use the sourced St Piran design as the exact historical input to the official ImageGen flag production pass. |
| BRI | Reuse the installed Gwenn-ha-du family. Keep the Debeauvais portrait and content-readiness blocked until a stronger attributable source with a defensible reuse basis is approved. |
| AEX | Retain the historical lion arms only as evidence for vanilla `BEL_flanders`; do not create or restore an AEX flag family. |
| AFX | Use the CC0 rooster vector as the distributable flat reference for the 1913 Walloon coq hardi identity; do not copy the restricted original Paulus watercolor. |
| AGX | Use the West Frisian provincial flag as the exact bounded Friesland design; do not present it as a universal pan-Frisian flag. |
| RHI | Reuse installed flags with the green-white-red separatist distinction. Register Matthes only for the Rhenish-republic route. |
| BAY | Reuse installed flags with republican/royal distinctions. Register Rupprecht only for the restoration route. |
| AJX | Use the 1920–1935 Saar Territory flag as the exact unsuffixed historical design. Do not guess an ideology variant mapping. |
| ICE | Reuse installed flags. Decide separately whether an AAT portrait dependency is allowed; no mod-owned Hermann portrait was cleared. |

## Main-agent integration checklist

- The real-person source/candidate/canonical sheets were reviewed. Matthes and
  the corrected Rupprecht portrait were approved. Debeauvais was rejected, and
  his processed/runtime files and sprite registration were removed.
- Wire Matthes and Rupprecht to their exact existing vanilla characters and
  allowed Event 6 routes with `set_portraits`. Do not globally replace vanilla
  sprite ids. Keep the BRI sprite id reserved and unwired.
- Route ACX, AFX, AGX, and AJX to the official ImageGen flag worker with the
  source manifest attached and require full historical TGA triplets. Keep AEX
  out of standalone flag production.
- Keep installed SCO, WLS, BRI, RHI, BAY, and ICE flag families in place; do not
  copy vanilla binaries into the mod.
- Carry the SCO, WLS, ICE, and BRI real-portrait blockers into the Event 006
  completion report.

## Meaningful validation

- The five motif pairs were visually reviewed from the retained source SVG/PNG
  files and again in the combined contact sheet.
- Both approved processed portraits are exactly 156x210 and were visually
  reviewed against their archival identities and canonical vanilla leaders.
- Both approved DDS files reopen as 156x210 RGBA images, have one-mip uncompressed
  BGRA layout, and have the exact expected length of 131,168 bytes.
- The final DDS contact sheet was generated from decoded runtime DDS files.
- SHA-256 hashes for every source, processed image, contact sheet, and DDS are in
  `northern_western_europe_source_manifest.md`.
- The installed SCO, WLS, BRI, RHI, BAY, and ICE normal/medium/small flag
  families were checked for complete triplets; no vanilla art was copied.

## Simplifications, omissions, and blockers

The bounded source-research task and its permitted source assets are complete,
but the full country-package art is not complete:

- four official-ImageGen-derived historical flag families were completed by the
  downstream live-flag repair; AEX has no standalone flag family;
- the five generated institutional council portrait packages are owned by the
  downstream generated-art package;
- SCO, WLS, and ICE have no new rights-cleared real-person portrait;
- BRI remains blocked because no candidate satisfies identity fidelity and a
  defensible reuse basis together;
- no unapproved ideology mapping, modern-symbol backdating, or unlicensed
  substitute was used.

These omissions are explicit blockers or owner-bound work, not silent fallbacks.
