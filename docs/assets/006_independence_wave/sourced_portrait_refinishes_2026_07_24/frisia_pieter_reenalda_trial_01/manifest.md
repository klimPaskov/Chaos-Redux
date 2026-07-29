# AGX Pieter Reenalda identity-preserving portrait trial 01

Status: `rejected_identity_runtime_hold`.

This package applies the mandatory sourced-person portrait chain to Pieter Reenalda for the existing Event 006 Frisia coastal-commander consumer.

No DDS was created or wired.

The 2026-07-24 independent audit rejected this trial on the non-compensable identity gate and retained it only as failed comparison evidence. The candidate must not be converted to DDS or wired to the stable consumer; no fallback or generic substitute is authorized.

## Stable consumer

| Field | Value |
|---|---|
| Character | `AGX_friesland_coastal_commander` |
| Sprite | `GFX_portrait_AGX_friesland_coastal_commander` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` |
| Role family | Army commander with maritime/coastal package identity |
| Gender gate | Male |

This is a full-size commander portrait only.

It does not create an advisor portrait, advisor icon, dossier, or `_small` derivative.

## Historical role fit

Pieter Reenalda was a real KPM first officer born in 1887 and photographed in maritime uniform.

The Tresoar family-archive provenance supplies a direct Frisian source chain, while his documented KPM officer service gives the AGX coastal-command token a concrete maritime identity.

The alternate office is not a claim that Reenalda historically commanded an independent Frisian army.

## Mandatory source chain

### 1. Archival male photograph

| Field | Value |
|---|---|
| Master | `source_masters/AGX_pieter_reenalda_1919_uniform_master.jpg` |
| Dimensions | 1206 x 1765 |
| Byte count | 145,425 |
| SHA-256 | `8F93840B12ECDCB313279C6F0FD4027863F8C1C4C9232E699AA7A0A9D46668CE` |
| Archive record | [Tresoar collection record](https://tresoar.nl/zoeken/collectie/4fddaece-1058-470b-be2a-29e4e9e236ac) |
| Archive description | Pieter Reenalda in uniform |
| Date / maker | 1919; unknown maker |
| Rights | Tresoar records public domain; Wikimedia Commons records the same |

The master is the unchanged selected 1919 uniform original retained from the vetted Frisia source package.

The 1915 garden photograph and 1911 uniform photograph remain comparison evidence in that source package and were not used as ImageGen inputs.

### 2. Explicit head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/AGX_pieter_reenalda_1919_head_shoulders_crop.png` |
| Master rectangle | `left=203, top=130, right=1003, bottom=1207` |
| Dimensions | 800 x 1077 |
| SHA-256 | `653437B6CBA46027CE630AB8EBC70D7355C1B86A7F3D64631BAFDC2E82D3AF71` |
| Method | Direct source-pixel crop exported to PNG without identity retouching, repainting, synthesis, or colourisation |

The crop preserves the complete head, neck, both shoulders, high maritime collar, and Reenalda's exceptionally long waxed moustache.

Independent crop review confirms the declared geometry and source identity. A decoded Pillow comparison against `master.crop((203, 130, 1003, 1207))` found only +/-1 grayscale-level decoder deltas in 16,430 of 861,600 pixels, with no offset, rescale, or visible identity retouching; a literal zero-delta re-export is still recommended if the source-pixel gate is enforced byte-for-byte.

### 3. Identity-preserving ImageGen repaint

| Field | Value |
|---|---|
| Input | Archival crop only |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `353C12A05A1187572C305B66DD3B9C42C44BACA200766604148315FE0A08293B` |
| Raw repaint | `imagegen_results/AGX_pieter_reenalda_identity_preserve_trial_01.png` |
| Raw dimensions | 1081 x 1455 |
| Raw SHA-256 | `4EBE0BDFF3AC39D89387E887BF22499975D520A6D1B409F06989C44C5B4BFFA2` |

The prompt makes the archival crop the sole identity and composition authority.

It explicitly preserves Reenalda's high forehead, side-parted hair, unequal eyes and ears, long narrow nose, tapering face, small chin, and the exact mass, length, height, and asymmetry of the moustache.

It permits only source-supported uniform shapes and forbids invented medals, badges, rank details, text, or hidden insignia.

### 4. Deterministic 156 x 210 processing

| Field | Value |
|---|---|
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | 5.0 |
| Processor SHA-256 | `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC` |
| Positional mode | `leader` |
| Role family | `commander` |
| Repaint crop | `left=0, top=0, right=1081, bottom=1455` |
| Output | `processed_png/portrait_AGX_friesland_coastal_commander.png` |
| Output dimensions | 156 x 210 |
| Output SHA-256 | `C683EEB6E71FE5EF118843F3748DB9C66136ACBC5C120C8B82F35FC55CE3789C` |
| Metadata | `processing_metadata.json` |
| Metadata SHA-256 | `841E4DECAEF783D988F9FEC9DB836FAED63399CD444E05B521AC21EB7C7C665D` |
| Review sheet | `review/AGX_pieter_reenalda_commander_style_sheet.png` |
| Review SHA-256 | `AC44475681DE159973EEADD8A7140AE3848D3EDE74B5DD1444A914B93EE8A167` |

The processor recorded the commander reference family explicitly.

The canonical reference images are `eng_bernard_montgomery.png` with SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` and `ger_erwin_von_witzleben.png` with SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

The processor performs crop, grade, and export only.

It does not synthesize or redraw the subject.

## Independent audit gate

An independent reviewer must compare the archival master, explicit source crop, raw ImageGen repaint, 156 x 210 processed PNG, prompt, processing metadata, review sheet, and commander references.

The reviewer must return separate verdicts for source provenance and rights, male-subject compliance, Frisian and maritime role fit, crop correctness, identity and likeness preservation, HOI4 commander style, 156 x 210 framing, ownership and stable-consumer fit, and absence of advisor, dossier, and `_small` assets.

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
