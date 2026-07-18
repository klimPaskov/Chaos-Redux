# Event 006 FORM-48 Pacific visual-asset manifest

Date: 2026-07-18
Package status: final asset production and runtime installation; parent-owned
gameplay and `.gfx` consumption remain pending

## Delivered inventory

| Requirement | Delivered source | Processed review assets | Runtime final | State |
|---|---|---|---|---|
| `ASSET-044` / `HBX` California carrier flag | official ImageGen historical Bear Flag source plus public-domain California reference | exact seven-colour 1536x1024 master and 82x52, 41x26, 10x7 PNGs, retaining the `CALIFORNIA REPUBLIC` legend at normal/medium sizes | 15 uncompressed 32-bit bottom-left-origin TGAs | handed off |
| `ASSET-046` / `PFX` Pacific Federation flag | original official ImageGen federal flag source | exact four-colour 1536x1024 master and 82x52, 41x26, 10x7 PNGs | 15 uncompressed 32-bit bottom-left-origin TGAs | handed off |
| `ASSET-046` / `FORM-48` emblem | original official ImageGen chroma source | transparent alpha master and 128x128 PNG | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds` | handed off; sprite registration pending |

Exact prompts and generation paths are recorded in
`prompts/imagegen_prompts.md`. `notes/validation.json` records the full
30-TGA/one-DDS validation, and `hashes.sha256` covers sources, processed files,
runtime finals, review artifacts, and handoff documents.

## `HBX` California civic carrier

The controlling California statute describes a 3:2 white flag with a red
five-point star in the upper hoist, a brown grizzly walking left on green
grass, a red lower stripe one-sixth of the hoist, and the words “California
Republic.” The State Capitol Museum records the Bear Flag's 1846 origin, 1911
adoption, and 1953 design standardization. California State Parks separately
documents the long-running variation before the 1953 standard.

`HBX` uses the historically grounded 1911 California Bear Flag arrangement for
IW-184's real California civic identity. ImageGen was used against the retained
public-domain geometry reference to produce a clean flat source with the
documented red star, left-facing grizzly, green ground, red lower stripe, and
the exact `CALIFORNIA REPUBLIC` legend. The deterministic post-process maps the
selected ImageGen geometry to seven solid colours; it does not redraw the bear
or add a new emblem. The legend is retained in the master and normal/medium
runtime PNG/TGA ladders; at 10x7 it necessarily collapses into a dark text band
and is not expected to remain individually legible.

The 1911-era visual is treated as a historical civic reconstruction, not a
claim that every pre-1953 California flag used one invariant bear drawing or
letterform. State sources document design variation before the 1953 standard;
the retained public-domain reference supplies the concrete bear and lettering
geometry used for this package.

Geometry and colour comparison:

| Element | Controlling reference | Runtime disposition |
|---|---|---|
| field | white, 3:2 | warm white `#f7f5ec`, 3:2 source master |
| star | red five-point star at upper hoist | retained at upper hoist in California red `#ba0c2f` |
| bear | brown grizzly walking left | retained left-facing generated silhouette with four discrete brown/detail tones |
| ground | green grass | retained as solid `#00843d` |
| lower stripe | red, one-sixth of hoist | retained as a solid lower stripe in `#ba0c2f` |
| wording | `CALIFORNIA REPUBLIC` | retained verbatim in the source/master and normal/medium runtime; necessarily compressed at 10x7 |

Sources and rights:

- [California Government Code §420](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?article=&chapter=2.&division=2.&lawCode=GOV&part=&title=1.) — official legal design description; factual and legal reference, link-only.
- [California State Capitol Museum, State Flag](https://capitolmuseum.ca.gov/state-symbols/flag/) — official historical chronology; link-only.
- [California State Parks, California State Flag](https://www.parks.ca.gov/?page_id=24644) — official history of early design variation; link-only.
- [Wikimedia Commons, Flag of California.svg](https://commons.wikimedia.org/wiki/File:Flag_of_California.svg) — distributable visual reference. The file page identifies the California public record as public domain in the United States and separately warns that official-insignia restrictions may apply. The downloaded 960px PNG is retained at `reference_inputs/california_flag_public_domain_960px.png`; no claim is made that public-domain copyright status removes non-copyright insignia rules.

## `PFX` Pacific Federation

`PFX` is an original alternate-history federal identity for the California,
Hawaii, and Micronesian Pacific route. Its deep navy field represents the open
ocean; the broad turquoise band represents a shared maritime corridor; the
gold rope ring represents negotiated federal obligations; exactly three ivory
currents represent the three founding Pacific constituencies; and the gold
eight-point compass represents common navigation and ports.

The design deliberately does not reproduce California's bear or star,
Hawaii's Union Jack canton and eight stripes, the Federated States of
Micronesia's four-star circle, or the Pacific Community's protected sail,
two-wave, and member-star logo. The Pacific Community source informed only the
general research conclusion that navigation and waves are regionally legible
symbols of connection. Its logo was not downloaded, supplied to ImageGen,
traced, or copied.

Palette: deep navy `#0b2d4d`, turquoise `#159a9c`, gold `#e4b33b`, ivory
`#f5f1de`. The flat master and every runtime size use only these four solid
colours, with no gradients, texture, lighting, fabric, lettering, or partial
alpha.

Research sources and rights:

- [Hawaii Revised Statutes §5-19](https://data.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/HRS0005/HRS_0005-0019.htm) — official statutory description of Hawaii's eight-stripe flag; factual/legal context only, with no media copied.
- [Federated States of Micronesia Code, Title 1 chapter 5](https://www.fsmlaw.org/fsm/code/title01/t1ch5_2014.html) — official description of the four-star federal flag; factual/legal context only, with no media copied.
- [Pacific Community media page](https://www.spc.int/media) — official explanation of its sail, waves, stars, and colours and its logo-use restrictions. Link-only conceptual research; no SPC artwork was downloaded or used as an image input.

## Complete ideology ladders

For each tag and each of `gfx/flags/`, `gfx/flags/medium/`, and
`gfx/flags/small/`, this package supplies the base filename plus
`_democratic`, `_communism`, `_fascism`, and `_neutrality`. The corresponding
five files are byte-identical by design. They represent a constitutional/civic
identity that persists across governments, not an omitted ideology pass; the
accepted FORM-48 plan authorizes no ideology-specific overlay.

| Tag | 82x52 shared SHA-256 | 41x26 shared SHA-256 | 10x7 shared SHA-256 |
|---|---|---|---|
| `HBX` | `4dcf34960d51ae627eb8b992ac1598be685f1f8dd5b4ae4d499048de9d913c38` | `0e1002184dab749f8d4fe7f9c221be20affbb2c6df4ad1b7ef1ecef57171d81d` | `d605431d0970a75143fd4a84cd3b2c5dd5bb1f2995d4df12b74b9b1fec231e5a` |
| `PFX` | `a2be355a7e236a48124b0c2b6935ce3d7d77014f7c30c0badd9c7ffae3ba021a` | `74bc570441e216883565104cc5e9e6001fa3dcf9b16b8e320bced5d6c2d7e19b` | `cfc91e988248574bdcf13d7fe47619d6e15901789bb91dc0306c3a1635d90d73` |

All 30 TGAs decode pixel-for-pixel to their processed PNGs. They are
uncompressed 32-bit true-colour files with eight alpha bits and bottom-left
origin, matching the offline country-creation documentation and vanilla flag
ladders.

## FORM-48 emblem

The separate FORM-48 UI emblem combines an open ivory charter, one gold
eight-point compass, a rising sun, exactly three linked turquoise wave
medallions, and a navy rope arc. It communicates negotiated federation,
navigation, and three founding Pacific constituencies without copying either
flag charge verbatim. Painterly internal material detail is intentional for a
HOI4 UI emblem; the no-gradient vexillology constraint applies to the flat flag
masters and runtime flags.

- Processed PNG: `processed_png/emblems/independence_wave_formable_form_48.png`
- Runtime DDS: `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`
- Proposed sprite: `GFX_independence_wave_formable_form_48`
- Runtime SHA-256: `6cfa1b3a342f588f17b42802d189c72e6aab6f7c0e12cb3349aedde8e2ecd222`
- Format: 128x128 legacy uncompressed BGRA8888 with real transparency
- State: final texture installed; parent-owned `.gfx` registration and live consumer pending

## Requirement-to-runtime crosswalk

| Registry row | Requirement | Runtime path(s) | Resolution mechanism | Current state |
|---|---|---|---|---|
| `ASSET-044` | `HBX` historical/civic California flag | `gfx/flags/HBX*.tga`, `gfx/flags/medium/HBX*.tga`, `gfx/flags/small/HBX*.tga` | HOI4 country-tag and ideology filename lookup | handed off; parent must ensure `HBX` country package consumes the tag |
| `ASSET-046` | distinct `PFX` Pacific federation identity | `gfx/flags/PFX*.tga`, `gfx/flags/medium/PFX*.tga`, `gfx/flags/small/PFX*.tga` | HOI4 cosmetic-country tag and ideology filename lookup | handed off; parent must wire `PFX` to FORM-48 formation/cosmetic logic |
| `ASSET-046` | FORM-48 UI emblem | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds` | proposed `GFX_independence_wave_formable_form_48` sprite | handed off; parent registration and consumer pending |

## Review and protected boundaries

- `contact_sheets/006_form48_flag_sources_and_ladders.png` compares the
  California reference, selected ImageGen sources, exact spot-colour masters,
  and all three target sizes.
- `contact_sheets/006_form48_emblem_source_and_runtime.png` compares the raw
  ImageGen chroma source, alpha master, final PNG, and decoded runtime DDS.
- `notes/visual_review.md` records the native-size manual review.
- No BAY or RHI portrait, historical-person portrait, fictional portrait,
  commander portrait, advisor icon, gameplay script, localisation, registry,
  `.gfx`, or `.gui` file was opened for editing or changed by this package.
