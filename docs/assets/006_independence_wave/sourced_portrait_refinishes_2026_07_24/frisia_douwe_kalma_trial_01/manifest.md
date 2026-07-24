# AGX Douwe Kalma identity-preserving portrait trial 01

Status: `candidate_pending_independent_audit`.

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
| Processor | `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` |
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

## Current runtime state

- DDS created: no.
- GFX edited: no.
- Gameplay edited: no.
- Localisation edited: no.
- Advisor asset created: no.
- Fallback used: no.
