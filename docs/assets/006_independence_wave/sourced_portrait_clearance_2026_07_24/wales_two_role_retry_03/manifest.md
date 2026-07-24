# IW-002 Wales sourced portrait clearance - retry 03

This package records two rights-cleared archival male source candidates for the existing WLS independence-wave portrait consumers. The package is source-ready for the parent-owned downstream identity-preserving portrait pipeline, but both requested roles remain `needs_user_review` because this bounded subtask intentionally stops before ImageGen, independent likeness/style review, `156x210` processing, and DDS conversion.

No `.gfx`, character, history, localisation, gameplay, or spreadsheet file was edited. No fallback portrait was created.

## Stable consumers

| Role | Existing sprite | Reserved runtime texture | Source-clearance result |
| --- | --- | --- | --- |
| WLS national council / civic-national leader | `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | David Grenfell is the preferred source candidate; downstream review remains required. |
| WLS mountain commandant | `GFX_portrait_WLS_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | George Cornwallis-West is the preferred source candidate; downstream review remains required. |

## Selected source entries

### WLS civic-national leader: David Rhys Grenfell

| Field | Value |
| --- | --- |
| Status | `needs_user_review` for downstream identity-preserving processing; source-clearance pass |
| Identity | David Rhys Grenfell (16 June 1881 to 21 November 1968), Welsh Labour MP for Gower from 1922 to 1959 and Welsh Parliamentary Labour Party chair; alive at age 54 in the 1936 setting |
| Role fit | A real Welsh civic and national political figure with a pre-war public portrait and a plausible 1936 national-council role |
| Source page | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:David_Grenfell.jpg) |
| Institutional record | [National Portrait Gallery record MW64853](https://www.npg.org.uk/collections/search/portrait/mw64853/David-Rhys-Grenfell) |
| Direct source URL | `https://upload.wikimedia.org/wikipedia/commons/9/9a/David_Grenfell.jpg` |
| Source attribution | Bassano Ltd; National Portrait Gallery record credits the 1922 portrait |
| Photograph date | 1922 |
| Era fit | Strong pre-war fit for a 1936 identity reference; the subject is 41 in the source image and 54 in the target setting |
| Rights | Public domain according to the Commons record; retain the Bassano Ltd and National Portrait Gallery credit in downstream provenance notes |
| Original source file | `source_png/david_grenfell_civic_candidate.jpg` |
| Original source dimensions and mode | `620x800`, grayscale JPEG (`L`) |
| Original source SHA-256 | `5bf5bfe500c724961acd4f56e3057f5a53981fcb779060bf9a79e901a7515749` |
| Decoded master | `source_master_png/david_grenfell_civic_master.png` |
| Master dimensions and mode | `620x800`, RGB PNG; lossless decode-to-PNG conversion only |
| Master SHA-256 | `7b613faad429e155133b60fb9e4c403639281e7054df47f07d5cdd6ea3e10e70` |
| Exact source crop | `exact_crops/david_grenfell_civic_crop.png` |
| Crop metadata | `exact_crops/david_grenfell_civic_crop.json` |
| Crop rectangle | `(left=70, top=65, right=600, bottom=790)` in decoded master pixels |
| Crop dimensions and mode | `530x725`, RGB PNG |
| Crop SHA-256 | `55f5cd025f7bfc070f3b821e90bcfabba0ba6daafffcb6d4a161a1a7db73392f` |
| Equality evidence | `decoded_pixels_equal: true`; master-crop and output RGBA SHA-256 both `05abcfec333dfe203df00e6f4c4755a55276c9d0339d5dc5234880433572fa19` |
| Crop method | `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, direct Pillow crop with no resampling or retouching |
| Future final size | `156x210` only after parent-owned source-locked ImageGen and independent review |
| Future final path | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| Uncertainty | Commons marks the image public domain, while the institutional record should remain attached for provenance. The source is a three-quarter portrait, so the downstream repaint must preserve facial geometry and not turn it into a generic moustached official. |

### WLS military or mountain commandant: Major George Frederick Myddleton Cornwallis-West

| Field | Value |
| --- | --- |
| Status | `needs_user_review` for downstream identity-preserving processing; source-clearance pass |
| Identity | Major George Frederick Myddleton Cornwallis-West (1874 to 1951), Welsh-born in Ruthin and an officer of the Scots Guards who also served with the Royal Marines and Royal Naval Division in the First World War; alive at age 62 in 1936 |
| Role fit | A real Welsh-born Army officer with a clear single-person uniform portrait and a defensible military-commandant fit for the existing WLS mountain-commandant token |
| Source page | [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Georgecornwalliswest.jpg) |
| Direct source URL | `https://upload.wikimedia.org/wikipedia/commons/0/0c/Georgecornwalliswest.jpg` |
| Source attribution | Henry Walter Barnett; Commons identifies the sitter as George Cornwallis-West and dates the portrait between 1900 and 1910 |
| Photograph date | Between 1900 and 1910 |
| Era fit | Strong early-century military fit; the subject is visibly younger than the 1936 target and the downstream repaint must age him without changing identity geometry |
| Rights | Public domain according to the Commons record; retain the photographer credit. Commons also displays a PD-Art jurisdiction caution, so the final provenance reviewer must preserve that uncertainty rather than claim unrestricted worldwide rights without review |
| Original source file | `source_png/george_cornwallis_west_original.jpg` |
| Original source dimensions and mode | `1080x1371`, RGB JPEG |
| Original source SHA-256 | `95068427782c799d86644133e1654b995569aebd51267da10f1d1e1baf16e3e8` |
| Decoded master | `source_master_png/george_cornwallis_west_commander_master.png` |
| Master dimensions and mode | `1080x1371`, RGB PNG; lossless decode-to-PNG conversion only |
| Master SHA-256 | `dba6c6bc4b5a261c4e761323944bc2d504b0f3de992f0d8301f2d28535e5ed2c` |
| Exact source crop | `exact_crops/george_cornwallis_west_commander_crop.png` |
| Crop metadata | `exact_crops/george_cornwallis_west_commander_crop.json` |
| Crop rectangle | `(left=40, top=40, right=1040, bottom=1320)` in decoded master pixels |
| Crop dimensions and mode | `1000x1280`, RGB PNG |
| Crop SHA-256 | `3483095e908cd993d46469d4033aaba4ad8cf7009e3bd7d8ba69f890cea066c4` |
| Equality evidence | `decoded_pixels_equal: true`; master-crop and output RGBA SHA-256 both `3b41102af8cc896b2afd2620160dadb7304c9fd2c371da30eaf0200fd57422ec` |
| Crop method | `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`, direct Pillow crop with no resampling or retouching |
| Future final size | `156x210` only after parent-owned source-locked ImageGen and independent review |
| Future final path | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| Uncertainty | The Commons date is a range and the PD record carries a jurisdiction caution. The sitter is Welsh-born and a real Army officer, but the source does not prove a specialist mountain command; the identity is offered as a plausible military-commandant fit, not as a claim that he commanded Welsh mountain units. |

## Held and rejected comparisons

| Candidate | Source and fit | Status | Reason |
| --- | --- | --- | --- |
| W. J. Gruffydd | Cardiff University archival portrait, 1946, CC BY-SA 4.0; exact source crop retained | `needs_user_review` / HOLD | Visually clear and culturally Welsh, but the only located image is postwar and the event targets a 1936-era setting. |
| William Ambrose Bebb | National Library of Wales portrait archive, circa 1930, Public Domain; candidate retained at `source_png/william_ambrose_bebb_candidate.jpg` | `blocked` | Kaiserreich `1521695605` actively owns the WLS character, portrait consumers, and localisation identity. |
| David Lloyd George | Clear archival candidate retained at `source_png/david_lloyd_george_civic_candidate.jpg` | `blocked` | Installed vanilla owns the English identity and localisation surfaces. |
| Gwilym Ivor Thomas | 1930s-era self-uploaded CC BY 4.0 photograph retained at `source_png/ivor_thomas_commander_source.jpg` | `needs_user_review` / alternate only | Clear face, but Welsh identity is indirect and uploader provenance is weaker than the selected archival sources. |
| James Henry Thomas | 1920 Illustrated London News scan retained at `source_png/j_h_thomas_civic_candidate.jpg` | `rejected` | Public domain and Welsh-born, but the available image is only `252x377` and cannot support the requested source-locked portrait workflow without inventing detail. |
| Hugh Evan-Thomas | 1917 paired photograph and public-domain illustration retained under `source_png/` | `rejected` | The usable photograph is a two-person scene and the other located images are illustrations, not a single-person archival identity master. |

## Downstream boundary

The exact crops are immutable identity references, not raw runtime portraits. A later parent-owned pass must use each exact crop as the sole identity input, use canonical vanilla commander or leader portraits for style only, produce a source-locked identity-preserving repaint, obtain an independent likeness/style/provenance review, and then create the deterministic `156x210` final PNG and repository-standard DDS. This package contains no final `156x210` PNG and no DDS by design.

