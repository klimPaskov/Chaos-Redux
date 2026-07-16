# Event 006 FORM-05 Mediterranean visual-asset manifest

Date: 2026-07-16
Package status: final and runtime-wired for this bounded asset tranche

## Delivered inventory

| Family | Count | Source | Processed/final format | Runtime format |
|---|---:|---|---|---|
| `ARX`, `ASX`, `MIX` flags | 3 generated designs, 45 runtime files | 1536x1024 official ImageGen PNG | fixed-palette PNG at 82x52, 41x26, 10x7 | uncompressed 32-bit bottom-left-origin TGA |
| FORM-05 decisions | 7 | 1254x1254 official ImageGen PNG | keyed RGBA PNG, 32x32 | legacy uncompressed BGRA8888 DDS |
| FORM-05 lifecycle ideas | 3 | 1254x1254 official ImageGen PNG | keyed RGBA PNG, 64x64 | legacy uncompressed BGRA8888 DDS |
| FORM-05 emblem | 1 | 1254x1254 official ImageGen PNG | keyed RGBA PNG, 128x128 | legacy uncompressed BGRA8888 DDS |
| Charter-congress report | 1 | 1400x1123 official ImageGen PNG | tilted transparent report-card PNG, 210x176 | legacy uncompressed BGRA8888 DDS |

Exact prompts and original ImageGen paths are in
`prompts/imagegen_prompts.md`. `hashes.sha256` records every retained source,
processed file, contact sheet, runtime final, and package document.
`notes/validation.json` records dimensions, codecs, palettes, hashes, alpha,
origin, decode comparisons, and the exact 45-TGA/12-DDS counts.

## Historical flag disposition

### `ARX` Sardinia

The selected exact arrangement is supported by the Italian Ministry of
Culture catalog record for object `2000050479`, a 1766-1815 Sardinian royal
standard: red St George cross on white; four quartered Moor heads; all four
turned left; bands wrapped around the forehead. The Ministry's 1809 Arborea
cavalry-standard record `0100216743` independently confirms the Sardinian arms
as a red cross on white with four black heads bandaged white on the forehead.
The civic flat field retains only that attested Sardinian arrangement and
omits royal, Savoy, crown, eagle, border, and regimental devices.

The retained CC0 geometry aid establishes no authority by itself; it was used
only to constrain motif geometry during ImageGen. The cataloged physical
object controls orientation and band placement. The result is not described
as an attested sovereign 1936 Sardinian state flag.

Sources:

- [Regione Autonoma della Sardegna, history of the Four Moors](https://www.regione.sardegna.it/regione/identita-visiva/emblemi-istituzionali/storia-dello-stemma) — official institutional history; link-only evidence.
- [Italian Ministry of Culture catalog object 2000050479](https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/2000050479) — controlling exact arrangement; catalog metadata CC BY 4.0; no catalog image copied.
- [Italian Ministry of Culture catalog object 0100216743](https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/0100216743) — corroborating 1809 standard; catalog metadata CC BY 4.0; no catalog image copied.
- `mediterranean_danube_flag_sources_2026_07_15/source_images/sardinia_traditional_four_moors_reference.png` — “Traditional flag of Sardinia,” Betelgeuse2003, [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Traditional_flag_of_Sardinia.png), CC0 1.0; geometry aid only.

Palette: off-white `#f7f5ec`, civic red `#c8102e`, near-black `#111111`.

### `ASX` Sicily

The selected design reconstructs the flat field of the surviving 1848 S.015
national colour described by the Italian Ministry of Culture: three vertical
bands with green at the hoist, ecru in the center, red at the fly, and one gold
Trinacria centered on the middle band; recto and verso are identical. The
3:2 field ratio and reviewed Trinacria rotation are disclosed normalizations
because the accessible catalog metadata does not specify exact digital
geometry. Fringe, tassels, pole, cravat, inscription, and embroidery texture
are intentionally omitted from the runtime flat field.

Sources:

- [Italian Ministry of Culture catalog object 0100215963 / S.015](https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/0100215963) — controlling dated physical object; catalog metadata CC BY 4.0; no catalog image copied.
- [Archivio di Stato di Palermo, General Parliament of Sicily decrees](https://digitalibrary-saassipa.cultura.gov.it/entities/archivalmaterial/20749410-4367-4365-9f75-33392164d6ae) — link-only, all-rights-reserved archive evidence; no scan copied. The collection records the March-April 1848 adoption sequence.
- `mediterranean_danube_flag_sources_2026_07_15/source_images/sicily_1848_national_flag_reference.svg` — “Flag of Sicilian Kingdom 1848,” Manny Mannheimer and later Wikimedia Commons contributors, [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Sicilian_Kingdom_1848.svg), CC BY-SA 4.0. Attribution and share-alike obligations are retained because the modern layout aid informed the ImageGen call.

Palette: green `#009246`, ecru `#f5f1e6`, civic red `#ce2b37`, gold `#d8a328`.

### `MIX` Mediterranean Island League

`MIX` is a fictional project-generated civic flag: deep navy field, sea-green
central band with gold edges, and a gold rope ring enclosing three white
lateen sails around a gold four-point compass. The distinct league emblem uses
an anchor, open charter, three harbor seals, and a rope wreath; it does not copy
the flag charge. There is no external historical-design claim or third-party
source image.

Palette: navy `#0c2340`, sea green `#147774`, gold `#dea92f`, ivory `#f5f3e8`.

## Complete flag ladders

For each tag and each of `gfx/flags/`, `gfx/flags/medium/`, and
`gfx/flags/small/`, the package supplies the base filename plus `_democratic`,
`_communism`, `_fascism`, and `_neutrality`. The corresponding five files are
byte-identical by design. This is intentional civic identity continuity, not
a missing ideology pass; no ideology overlay is authorized or present.

| Tag | 82x52 SHA-256 shared by five names | 41x26 | 10x7 |
|---|---|---|---|
| `ARX` | `0677ba67d24fa5a8acd180aa5ac511f998d17ab9747dec64072da06252aa7803` | recorded in `notes/validation.json` | recorded in `notes/validation.json` |
| `ASX` | recorded in `notes/validation.json` | recorded in `notes/validation.json` | recorded in `notes/validation.json` |
| `MIX` | recorded in `notes/validation.json` | recorded in `notes/validation.json` | recorded in `notes/validation.json` |

All 45 files decode exactly to their fixed-palette processed PNG. No flag at
any size contains gradients, texture, illustrative shading, or partial alpha.

## Sprite and runtime crosswalk

| Sprite | Runtime path | Target | Live consumer/state |
|---|---|---:|---|
| `GFX_decision_independence_wave_form05_charter` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_charter.dds` | 32x32 | category and formation/lifecycle decisions |
| `GFX_decision_independence_wave_form05_delegation` | `.../decision_independence_wave_form05_delegation.dds` | 32x32 | delegation decisions |
| `GFX_decision_independence_wave_form05_shipping` | `.../decision_independence_wave_form05_shipping.dds` | 32x32 | shipping decisions; reused post-formation |
| `GFX_decision_independence_wave_form05_defense` | `.../decision_independence_wave_form05_defense.dds` | 32x32 | defense decisions; reused post-formation |
| `GFX_decision_independence_wave_form05_customs` | `.../decision_independence_wave_form05_customs.dds` | 32x32 | customs decisions; reused post-formation |
| `GFX_decision_independence_wave_form05_capital` | `.../decision_independence_wave_form05_capital.dds` | 32x32 | capital decision |
| `GFX_decision_independence_wave_form05_proclamation` | `.../decision_independence_wave_form05_proclamation.dds` | 32x32 | proclamation decisions; reused post-formation |
| `GFX_idea_independence_wave_form05_provisional_charter` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_provisional_charter.dds` | 64x64 | `picture = independence_wave_form05_provisional_charter` |
| `GFX_idea_independence_wave_form05_ratified_union` | `.../idea_independence_wave_form05_ratified_union.dds` | 64x64 | `picture = independence_wave_form05_ratified_union` |
| `GFX_idea_independence_wave_form05_charter_breakdown` | `.../idea_independence_wave_form05_charter_breakdown.dds` | 64x64 | `picture = independence_wave_form05_charter_breakdown` |
| `GFX_report_event_independence_wave_form05_charter_congress` | `gfx/event_pictures/006_independence_wave/mediterranean/report_event_independence_wave_form05_charter_congress.dds` | 210x176 | all FORM-05 event pictures |
| `GFX_independence_wave_formable_form_05` | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` | 128x128 | registered FORM-05 identity emblem |

Every full texture path is registered in
`interface/006_independence_wave_form05.gfx`. That file deliberately registers
only the seven requested decision sprites. New post-formation actions reuse
those sprites; this tranche creates no extra post-formation decision sprite.

## Review and protected boundaries

- `contact_sheets/006_form05_flag_sources_and_ladders.png` reviews each raw
  ImageGen flag against its flat master and all three target sizes.
- `contact_sheets/006_form05_ui_icons_contact_sheet.png` reviews all seven
  decisions, three ideas, and the distinct emblem at integer target scaling.
- `contact_sheets/006_form05_report_event_contact_sheet.png` reviews the
  fictional press-photo source and final report card.
- No advisor icon, leader portrait, character portrait, army-small portrait,
  BAY/RHI protected portrait, or Event 14 asset was opened, copied, generated,
  edited, registered, referenced as an art input, or retained by this package.
