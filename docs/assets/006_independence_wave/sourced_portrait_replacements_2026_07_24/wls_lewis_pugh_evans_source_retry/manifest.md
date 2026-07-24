# IW-002 Wales commander sourced portrait replacement

This package is a source-only replacement candidate for the grounded male `WLS_independence_wave_mountain_commandant` commander token in Event 6, IW-002 Wales.

Status is `source_ready_needs_user_review`: the immutable archival source, explicit identity crop, provenance record, ownership scan, and candidate comparison are complete, while the downstream identity-preserving repaint, independent visual audit, DDS conversion, and runtime wiring remain outside this package.

No ImageGen result, processed `156x210` portrait, DDS, `.gfx` edit, gameplay edit, localisation edit, workbook edit, advisor portrait, dossier portrait, `_small` portrait, or fallback was created.

## Selected identity and role fit

The selected identity is Lewis Pugh Evans (3 January 1881 to 30 November 1962), a Welsh-born British Army officer born at Abermad near Aberystwyth.

The Dictionary of Welsh Biography records that Evans's final appointment was commander of the 159th Welsh Border Infantry Brigade from 1933 until his retirement in January 1938, which places him alive and in an active Welsh formation command on 1 January 1936.

The source therefore satisfies the Welsh connection, male identity, alive-in-1936, and period-command gates without reusing a vanilla-owned commander.

WLS's `mountain_frontier` force profile is an alternate-history territorial and mountain-defense abstraction. Evans commanded a Welsh Border infantry brigade, not a specialist Gebirgstruppe or historically named mountain formation; the game role must not imply otherwise.

Recommended role wording: `Lewis Pugh Evans is used here as Wales's Welsh Border territorial commandant; the mountain-frontier label describes the package's defensive terrain and communications, not a claim of specialist mountain-branch service.`

## Immutable source master

| Field | Value |
| --- | --- |
| Path | `source_masters/WLS/WLS_lewis_pugh_evans_iwm_hu93411_c1918.jpg` |
| Source page | <https://commons.wikimedia.org/wiki/File:Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg> |
| Exact original URL | <https://upload.wikimedia.org/wikipedia/commons/c/c1/Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg> |
| Download route used | <https://commons.wikimedia.org/wiki/Special:FilePath/Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg?width=605> |
| Official archive record | <https://www.iwm.org.uk/collections/search?query=HU+93411> |
| Archive/provider | Imperial War Museums, collection no. `2500-02`, image `HU 93411` |
| Archive description | `Photograph of Lt Col Lewis Pugh Evans VC` |
| Photographer | Henry Walter Barnett (1862–1934) |
| Source date | circa 1918 |
| Original dimensions | `605x800` |
| Decoded mode/format | 24-bit RGB JPEG |
| File size | `46,537` bytes |
| SHA-256 | `FDFDE87660F50EB9A2112186878FB8EE93B7C1F0E2CB9F533CA9B2C41C26012C` |
| Rights record | Wikimedia Commons records the file as `Public domain` with `Public domain` usage terms and a Public Domain Mark record. |
| Rights basis | The source is a pre-1931 archival photograph by Barnett, whose 1934 death supports the UK life-plus-70 public-domain basis; Commons also preserves the IWM Crown-copyright/Non-Commercial-Licence note. |
| Recommended credit | `Imperial War Museums, HU 93411; photograph by Henry Walter Barnett` |

The retained JPEG is the unchanged 605x800 download and is not a screenshot, web thumbnail, modern reenactment, film still, or generated likeness.

Rights uncertainty is limited to the exact capture/publication date and territorial treatment not stated by the IWM record. Preserve the IWM/Barnett credit and re-check the target distribution territory before final runtime promotion if the parent project requires a jurisdiction-specific legal opinion.

## Explicit face-visible head-and-shoulders crop

| Field | Value |
| --- | --- |
| Path | `source_crops/WLS/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png` |
| Source master | `source_masters/WLS/WLS_lewis_pugh_evans_iwm_hu93411_c1918.jpg` |
| Crop coordinates | `(left=95, top=25, right=540, bottom=505)` in source-master pixels |
| Crop dimensions | `445x480` |
| Decoded mode/format | 24-bit RGB PNG |
| File size | `107,585` bytes |
| SHA-256 | `B16812C1B58AF568EAC7E74EC64E592CC34DD793CC2DB3A8D261D85168A2C064` |
| Crop method | Direct source-pixel `Pillow.Image.crop`; no resampling, retouching, recolouring, sharpening, or face alteration |
| Framing | Evans's cap, unobstructed face, neck, both shoulders, collar, upper tunic, and ribbons are visible; hands, lower body, captioning, and unrelated people are excluded. |
| Intended use | Immutable identity evidence for a future source-locked HOI4 commander-family repaint and likeness audit; not a runtime portrait. |

The source crop is an evidence PNG only. It must not be promoted directly to the game as a raw photograph or merely resized portrait.

## Candidate comparison evidence

The contact sheet `candidate_review/WLS_lewis_pugh_evans_candidate_comparison.png` is a review-only comparison of the selected Evans source, the selected crop, and two rejected Thomas Wynford Rees IWM candidates.

| Evidence | Dimensions | SHA-256 |
| --- | ---: | --- |
| `candidate_review/WLS_lewis_pugh_evans_candidate_comparison.png` | `740x740` | `9E94FF65C47F68A680AFBC95136CBB6551573D0785AB6FC54F992B82998591BD` |

Rees's `SE3459` and `SE3465` files are retained only as rejected comparison evidence. Both Commons records describe 1945 Burma field scenes and mark the images public domain under the IWM Crown-copyright expiry note, but neither provides a clean single-person head-and-shoulders source at useful facial scale. Rees was also already owned by the approved Kaiserreich reference mod and was serving in India/Waziristan rather than a Welsh formation in 1936.

## Canonical visual references

The canonical vanilla reference root was read before packaging: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`, `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`, and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/REFERENCE_MANIFEST.md`.

Those references are style and framing references only. They are not source material and no vanilla or reference-mod art was copied.

## Stable consumer and processing boundary

The stable character token remains `WLS_independence_wave_mountain_commandant` and is checked as a corps commander by `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`.

The stable full sprite is `GFX_portrait_WLS_independence_wave_mountain_commandant` in `interface/006_independence_wave_region_01_portraits.gfx`.

The reserved runtime texture remains `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`.

The downstream processor must use the unchanged source master and exact crop as identity inputs, use the canonical commander references for style only, produce an identity-preserving commander-family repaint at `156x210`, and stop for an independent likeness/style/provenance audit before any DDS conversion or runtime wiring.

No advisor, dossier, `_small`, alternate, female, navy, generic, or fallback derivative is authorized by this source package.

## Status and uncertainty

The source candidate is complete for the requested sourced-input scope and is not runtime-ready until the parent-owned downstream repaint, audit, DDS, and `.gfx` wiring stages are separately completed.

No simplification or fallback was used in the source selection, rights review, crop, or ownership gate.
