# AGX Douwe Kalma identity-preserving portrait trial 01

Status: `rejected_unwired_identity_gate`.

This package applies the mandatory sourced-person portrait chain to Douwe Kalma for the existing Event 006 Frisia civic-leader consumer.

No DDS was created or wired.

## Stable consumer

| Field | Value |
|---|---|
| Character | `AGX_friesland_coastal_council` |
| Sprite | `GFX_portrait_AGX_friesland_coastal_council` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` |
| Role family | Country leader |
| Gender gate | Male |

This is a full-size country-leader portrait only.

It does not create an advisor portrait, advisor icon, dossier, or `_small` derivative.

## Historical role fit

Douwe Kalma was a real Frisian writer, poet, translator, and nationalist born in 1896 and alive in 1936.

His Frisian cultural and political work gives the grounded AGX civic and municipal leadership token a direct regional identity.

The alternate office is not a claim that Kalma historically headed an independent Frisian state.

## Mandatory source chain

### 1. Archival male photograph

| Field | Value |
|---|---|
| Master | `source_masters/AGX_douwe_kalma_1917_master.jpg` |
| Dimensions | 691 x 1013 |
| Byte count | 87,040 |
| SHA-256 | `38DAFCBFF7C3A67B6B29B9B637E69FF4C2F9D8CAAE076361200919A6BB36DBDF` |
| Source page | [Wikimedia Commons: Portret fan Douwe Kalma, 1917 ca.](https://commons.wikimedia.org/wiki/File:Portret_fan_Douwe_Kalma,_1917_ca._archiefnr_1990.jpg) |
| Direct upload | [Original upload](https://upload.wikimedia.org/wikipedia/commons/d/d6/Portret_fan_Douwe_Kalma%2C_1917_ca._archiefnr_1990.jpg) |
| Archive record | [Tresoar collection record](https://tresoar.nl/zoeken/collectie/cf64b17f-5d0c-46f9-9209-a7f60c185068) |
| Date / maker | Circa 1917; F. O. Strüppert, Leeuwarden |
| Rights | Tresoar records no copyright / public domain; Commons records public domain |

The master is the unchanged original retained from the vetted Frisia source package.

### 2. Explicit head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/AGX_douwe_kalma_1917_head_shoulders_crop.png` |
| Master rectangle | `left=50, top=80, right=640, bottom=876` |
| Dimensions | 590 x 796 |
| Byte count | 427,511 |
| SHA-256 | `C247B52B5F1E0C5528F086C3FC374F8E4F5815E9172E1737C07BD4432DAFD59B` |
| Method | Direct source-pixel crop exported to PNG without identity retouching, repainting, synthesis, or colourisation |

The crop preserves the complete head, neck, and both shoulders.

The dark pinhole on the viewer-left forehead is archival surface damage and remains visible in this immutable identity crop.

### 3. Identity-preserving ImageGen repaint

| Field | Value |
|---|---|
| Input | Archival crop only |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `0F897249867052D1ACF9024C37488926FB20B51B133A3A239695FD38DF617D2E` |
| Raw repaint | `imagegen_results/AGX_douwe_kalma_identity_preserve_trial_01.png` |
| Raw dimensions | 1076 x 1461 |
| Raw SHA-256 | `DDC58B9B096034F786837D26D23C2C8F6FD0FF6308D069267407863A19E18998` |

The prompt makes the archival crop the sole identity and composition authority.

It explicitly preserves Kalma's long narrow face, center-parted hair, unequal exposed ears, narrow eyes and lids, long narrow nose, thin lips, pointed chin, expression, gaze, head angle, neck length, and shoulder slope.

It permits removal of the isolated emulsion pinhole as surface restoration but forbids changing the underlying forehead geometry or inventing hidden detail.

### 4. Deterministic 156 x 210 processing

| Field | Value |
|---|---|
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | 5.0 |
| Processor SHA-256 | `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC` |
| Positional mode | `leader` |
| Role family | `leader` |
| Repaint crop | `left=0, top=6, right=1076, bottom=1455` |
| Output | `processed_png/portrait_AGX_friesland_coastal_council.png` |
| Output dimensions | 156 x 210 |
| Output SHA-256 | `1097704208FCA9758B2B7546805BA91C3E9D440E7ABB8342B68D4938ABDCDEF9` |
| Metadata | `processing_metadata.json` |
| Metadata SHA-256 | `8CC3362C1676BFF971560A720ACEFD9F6A149178ABE1C2D7AD46FDB2D1FF9993` |
| Review sheet | `review/AGX_douwe_kalma_leader_style_sheet.png` |
| Review SHA-256 | `0B3574693E0062C6C0AA5376468AA7875231497ED2B301B6514EC65AA2D17B91` |

The processor recorded the country-leader reference family explicitly.

The canonical reference images are `den_thorvald_stauning.png` with SHA-256 `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6` and `fin_carl_mannerheim.png` with SHA-256 `7E78E33E0B691B96B584393F2D363C07A302320F7E6300BDA0FFF261AA98D49E`.

The processor performs crop, grade, and export only.

It does not synthesize or redraw the subject.

## Independent audit gate

An independent reviewer must compare the archival master, explicit source crop, raw ImageGen repaint, 156 x 210 processed PNG, prompt, processing metadata, review sheet, and country-leader references.

The reviewer must return separate verdicts for source provenance and rights, male-subject compliance, role fit, crop correctness, identity and likeness preservation, HOI4 country-leader style, 156 x 210 framing, ownership and stable-consumer fit, and absence of advisor, dossier, and `_small` assets.

Identity and style are separate non-compensable gates.

Any failed identity or style verdict keeps the candidate rejected and unwired.

Only a complete independent pass permits deterministic DDS conversion and sprite wiring.

## Independent audit result — 2026-07-24

Reviewer: `chaosx_country_package_auditor` (independent of the producing asset worker).

The retained source master, explicit crop, raw repaint, processed 156 x 210 PNG, prompt, processing metadata, review sheet, and both selected country-leader references were inspected at native size and at a 4x nearest-neighbour inspection scale. The package hash ledger was recomputed; every listed hash matches its file. No DDS was created, replaced, or wired by this trial.

| Gate | Verdict | Evidence and disposition |
|---|---|---|
| Provenance / rights | **PASS** | `source_masters/AGX_douwe_kalma_1917_master.jpg` is retained unchanged with SHA-256 `38DAFCBFF7C3A67B6B29B9B637E69FF4C2F9D8CAAE076361200919A6BB36DBDF`; the Commons file, original upload, and Tresoar collection links, circa-1917 date, F. O. Strüppert attribution, and public-domain/no-copyright record are retained above. The crop, prompt, raw result, processor metadata, candidate, and review sheet remain in distinct paths. |
| Male-subject compliance | **PASS** | The source, repaint, and candidate show one male subject. The live character declares `gender = male`; no `female = yes`, female name pool, or opposite-gender pairing is present. The prompt explicitly requires one male subject only. |
| Historical / Frisian role fit | **PASS** | Douwe Kalma is a real Frisian writer, poet, translator, and nationalist (1896–1953), alive in 1936. His regional civic and cultural work supports the AGX Frisia civic-leader token; the manifest correctly avoids claiming that he historically headed an independent Frisian state. |
| Explicit head-and-shoulders crop | **PASS** | `source_crops/AGX_douwe_kalma_1917_head_shoulders_crop.png` is 590 x 796 from master rectangle `left=50, top=80, right=640, bottom=876`, with the complete head, neck, both shoulders, suit, collar, and tie. The archival forehead pinhole remains in this immutable crop. Minor JPEG-to-PNG decode rounding does not change the source geometry or add a retouch. |
| Identity / likeness preservation | **FAIL — mandatory gate** | At 4x, the raw repaint and native candidate broaden and shorten the source’s very long narrow oval face; open and regularize the narrow unequal heavy-lidded eyes; reduce the unequal prominent ear shapes; shorten and widen the long narrow straight nose; thicken and regularize the thin asymmetrical lips; broaden and round the pointed chin/long jaw; and frontalize the source’s age, expression, and quiet direct gaze. Center-parted hair remains broadly recognizable but the hairline/volume is normalized. These are facial-geometry and pose changes, not removable emulsion damage. The isolated viewer-left forehead pinhole is correctly treated as removable surface damage and is not the rejection reason. |
| HOI4 country-leader style | **PASS (independent of identity)** | The raw result and 156 x 210 candidate use a restrained painted finish, muted brown/charcoal/olive palette, dark quiet vignette, period civilian suit, readable face, and controlled contrast consistent with `den_thorvald_stauning.png` and `fin_carl_mannerheim.png`. There is no text, watermark, UI frame, modern prop, unsupported insignia, or photographic-only finish. Style cannot compensate for the identity failure. |
| 156 x 210 framing | **PASS** | `processed_png/portrait_AGX_friesland_coastal_council.png` is an opaque RGBA PNG at exactly 156 x 210. It keeps the full head, neck, both shoulders, collar, tie, and upper jacket within a country-leader portrait frame. |
| Ownership / stable-consumer fit | **PASS (consumer contract; candidate still unwired)** | Exact and variant searches for `Douwe Kalma`, `Kalma, Douwe`, `Douwe_Kalma`, and `DouweKalma` found no competing vanilla character/history/localisation/GFX consumer. The intended project owner is `AGX_friesland_coastal_council` in `common/characters/006_independence_wave_wallonia_frisia_characters.txt`, recruited by `history/countries/AGX - Frisia.txt`, localized as `Douwe Kalma`, and bound only to civilian large sprite `GFX_portrait_AGX_friesland_coastal_council` in `interface/006_independence_wave_region_01_portraits.gfx`. A pre-existing DDS already occupies the documented runtime path, but this rejected trial did not create, replace, or authorize it. |
| Advisor / dossier / `_small` absence | **PASS** | The trial folder contains no advisor, high-command, dossier, operative, commander, or `_small` asset. The AGX character defines only a civilian `large` portrait; no `portraits = { army = { small = ... } }` consumer or AGX `_small` runtime texture exists. |

### Rejected/unwired status and source-only retry invariants

Because the identity gate fails, this candidate remains `rejected_unwired_identity_gate`. Do not convert it to DDS, replace the existing runtime texture, wire the sprite, or approve a fallback. A source-only retry must use the unchanged archival master and preserve these immutable traits exactly: very long narrow face and pointed chin; narrow unequal heavy-lidded eyes and quiet direct gaze; unequal prominent ears; long narrow straight nose with small tip; thin asymmetrical lips; exact young-adult age, expression, head angle, neck length, and shoulder slope; center-parted hair with the uneven source hairline; and source-visible suit, high white collar, tie silhouette, and both-shoulder framing. Remove only the isolated viewer-left forehead emulsion pinhole; do not alter forehead geometry or invent hidden facial detail.

## Current runtime state

- DDS created by this trial: no.
- Candidate DDS/GFX wiring authorized: no; candidate rejected and unwired.
- Pre-existing runtime DDS: present at `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`; not created or replaced by this trial.
- GFX edited: no.
- Gameplay edited: no.
- Localisation edited: no.
- Advisor asset created: no.
- Fallback used or approved: no.
