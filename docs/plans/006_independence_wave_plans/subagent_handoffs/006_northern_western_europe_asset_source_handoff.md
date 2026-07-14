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
flags in place, retains sourced motifs as evidence for Group B generated civic
flags, and produces real-person portraits only where identity, route context,
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

No flag TGA was created. The accepted package resolution requires generated
period civic baselines for all five Group B packages, and no ideology/cosmetic
mapping is approved for the Saar historical flag.

### Real-person portrait packages

- BRI François Debeauvais: public-domain 1928 party-congress source, 156x210
  processed PNG, and uncompressed BGRA DDS. Nationalist route only. The crop is
  low fidelity and has a parent visual-review gate.
- RHI Josef Friedrich Matthes: 1923 Library of Congress Bain source, 156x210
  processed PNG, and uncompressed BGRA DDS. Rhenish separatist/republic route
  only.
- BAY Rupprecht of Bavaria: circa-1916 Franz Grainer public-domain source,
  156x210 processed PNG, and uncompressed BGRA DDS. Traditional
  crown/restoration route only.

The sharper 1932 Debeauvais image was not used because its Commons page does not
establish United States public-domain status. The 1928 source is lower quality
but has explicit dual-jurisdiction public-domain status and identifies
Debeauvais by annotation.

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
- three 156x210 processed portrait PNGs under
  `docs/assets/006_independence_wave/processed_png/portraits/`
- `docs/assets/006_independence_wave/contact_sheets/006_northern_western_europe_sourced_assets.png`
- `docs/assets/006_independence_wave/contact_sheets/006_northern_western_europe_final_dds_decoded.png`
- `gfx/leaders/006_independence_wave/portrait_BRI_francois_debeauvais.dds`
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
| ACX | Route the sourced St Piran motif to generated civic flag production. Do not wire the processed review PNG. |
| BRI | Reuse installed Gwenn-ha-du family. The main agent accepted the archival low-fidelity Debeauvais portrait for the nationalist route only. |
| AEX | Route the historical lion-arms motif to generated civic flag production; do not backdate the current official Flemish flag. |
| AFX | Route the CC0 rooster vector to generated civic flag production; do not copy the restricted original Paulus watercolor. |
| AGX | Route the West Frisian motif to a bounded Friesland civic design; do not present it as a universal pan-Frisian flag. |
| RHI | Reuse installed flags with the green-white-red separatist distinction. Register Matthes only for the Rhenish-republic route. |
| BAY | Reuse installed flags with republican/royal distinctions. Register Rupprecht only for the restoration route. |
| AJX | Route the 1920-35 Saar flag to generated civic production as commission-legacy evidence. Do not guess an `AJX_neutrality` mapping. |
| ICE | Reuse installed flags. Decide separately whether an AAT portrait dependency is allowed; no mod-owned Hermann portrait was cleared. |

## Main-agent integration checklist

- Both contact sheets were reviewed. The main agent accepted the Brittany crop
  for its nationalist route only and registered the three proposed sprites in
  `interface/006_independence_wave.gfx` on 2026-07-14.
- Wire each portrait to its exact historical person and allowed route; do not
  make any of the three a universal institutional portrait.
- Route ACX, AEX, AFX, AGX, and AJX to the generated-flag worker with the source
  manifest attached. Require separate generated labeling and full TGA triplets.
- Keep installed SCO, WLS, BRI, RHI, BAY, and ICE flag families in place; do not
  copy vanilla binaries into the mod.
- Carry the SCO, WLS, and ICE real-portrait blockers and the BRI quality gate into
  the Event 006 completion report.

## Meaningful validation

- The five motif pairs were visually reviewed from the retained source SVG/PNG
  files and again in the combined contact sheet.
- All three processed portraits are exactly 156x210 and were visually reviewed.
- All three DDS files reopen as 156x210 RGBA images, have one-mip uncompressed
  BGRA layout, and have the exact expected length of 131,168 bytes.
- The final DDS contact sheet was generated from decoded runtime DDS files.
- SHA-256 hashes for every source, processed image, contact sheet, and DDS are in
  `northern_western_europe_source_manifest.md`.
- The installed SCO, WLS, BRI, RHI, BAY, and ICE normal/medium/small flag
  families were checked for complete triplets; no vanilla art was copied.

## Simplifications, omissions, and blockers

The bounded source-research task and its permitted source assets are complete,
but the full country-package art is not complete:

- five generated civic flag families remain outside this source worker's role;
- five generated institutional council portrait packages remain outside this
  source worker's role;
- SCO, WLS, and ICE have no new rights-cleared real-person portrait;
- BRI's delivered real portrait is legally cleared and accepted at archival
  low fidelity for the nationalist route only;
- no unapproved ideology mapping, modern-symbol backdating, or unlicensed
  substitute was used.

These omissions are explicit blockers or owner-bound work, not silent fallbacks.
