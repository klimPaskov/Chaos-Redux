# Event 006 AGX Frisia Douwe Kalma trial 01 independent portrait audit

Audit date: 2026-07-24.

Auditor: `chaosx_country_package_auditor`.

Scope: independent source-only audit of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/frisia_douwe_kalma_trial_01/`.

No source image, raw repaint, processed PNG, DDS, `.gfx`, gameplay, localisation, or fallback asset was created, edited, converted, or wired by this audit.

## Disposition

`REJECTED / UNWIRED`.

The provenance, male-subject, historical/Frisian role, crop, HOI4 style, 156 x 210 framing, stable-consumer, and no-advisor/dossier/`_small` gates pass independently.

The mandatory identity/likeness gate fails because the raw ImageGen repaint and processed candidate materially change immutable facial geometry and pose.

Style quality does not compensate for identity drift.

The trial must not be converted to DDS, used to replace the existing runtime texture, or wired to `GFX_portrait_AGX_friesland_coastal_council`.

## Evidence reviewed

| Artifact | Path | SHA-256 / facts |
|---|---|---|
| Archival master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/frisia_douwe_kalma_trial_01/source_masters/AGX_douwe_kalma_1917_master.jpg` | `38DAFCBFF7C3A67B6B29B9B637E69FF4C2F9D8CAAE076361200919A6BB36DBDF`; JPEG RGB; 691 x 1013; 87,040 bytes. |
| Explicit crop | `source_crops/AGX_douwe_kalma_1917_head_shoulders_crop.png` | `C247B52B5F1E0C5528F086C3FC374F8E4F5815E9172E1737C07BD4432DAFD59B`; PNG RGB; 590 x 796; master rectangle `(50,80,640,876)`. |
| Prompt | `identity_repaint_prompt.md` | `0F897249867052D1ACF9024C37488926FB20B51B133A3A239695FD38DF617D2E`. |
| Raw repaint | `imagegen_results/AGX_douwe_kalma_identity_preserve_trial_01.png` | `DDC58B9B096034F786837D26D23C2C8F6FD0FF6308D069267407863A19E18998`; PNG RGB; 1076 x 1461. |
| Processed candidate | `processed_png/portrait_AGX_friesland_coastal_council.png` | `1097704208FCA9758B2B7546805BA91C3E9D440E7ABB8342B68D4938ABDCDEF9`; PNG RGBA; 156 x 210; alpha fully opaque. |
| Processor metadata | `processing_metadata.json` | `8CC3362C1676BFF971560A720ACEFD9F6A149178ABE1C2D7AD46FDB2D1FF9993`; processor v5.0; mode/role `leader`; raw crop `(0,6,1076,1455)`. |
| Review sheet | `review/AGX_douwe_kalma_leader_style_sheet.png` | `0B3574693E0062C6C0AA5376468AA7875231497ED2B301B6514EC65AA2D17B91`; PNG RGBA; 1344 x 464. |
| Hash ledger | `hashes.sha256` | Every listed file was recomputed and matched after the manifest status update. |

Canonical country-leader references were verified at `156 x 210` and against their recorded metadata hashes.

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png` — `08732002182BDCB2BFF3D78B142CC2B3D75ADBDB29D4115F9E89CA5BDC6A21B6`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png` — `7E78E33E0B691B96B584393F2D363C07A302320F7E6300BDA0FFF261AA98D49E`.

The processor hash recorded in metadata matches the current `the retired portrait-processing utility` SHA-256 `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`.

## Separate gate verdicts

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance / rights | **PASS** | The unchanged male archival master, direct upload, crop, prompt, raw result, metadata, candidate, and review sheet are retained in distinct paths. `manifest.md` records the [Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Portret_fan_Douwe_Kalma,_1917_ca._archiefnr_1990.jpg), [original upload](https://upload.wikimedia.org/wikipedia/commons/d/d6/Portret_fan_Douwe_Kalma%2C_1917_ca._archiefnr_1990.jpg), and [Tresoar collection record](https://tresoar.nl/zoeken/collectie/cf64b17f-5d0c-46f9-9209-a7f60c185068), with circa-1917 date, F. O. Strüppert attribution, and public-domain/no-copyright record. The immutable master hash matches the source package. |
| Male-subject compliance | **PASS** | The source, repaint, and candidate depict one male subject. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-103` declares `gender = male`; no `female = yes`, female name pool, or opposite-gender portrait/name pairing exists. The prompt requires one male subject only. |
| Historical / Frisian role fit | **PASS** | Douwe Kalma was a real Frisian writer, poet, translator, and nationalist born in 1896 and alive in 1936. His regional civic and cultural work supports the AGX Frisia civic-leader consumer. The manifest correctly states that this alternate office is not a claim that Kalma historically headed an independent Frisian state. |
| Explicit crop correctness | **PASS** | The crop rectangle is within the 691 x 1013 master, yields 590 x 796, and preserves the complete head, neck, both shoulders, suit, collar, and tie. The archival viewer-left forehead pinhole remains in the immutable crop. Minor JPEG-to-PNG decode rounding is not a geometry edit; no crop retouch, repaint, or synthesis is visible. |
| Identity / likeness preservation | **FAIL — mandatory gate** | Native and 4x nearest-neighbour comparison of master → crop → raw repaint → candidate shows material drift. The source’s very long narrow oval face becomes shorter, broader, and rounder. Narrow unequal heavy-lidded eyes become more open and regularized. Unequal prominent ears are reduced and normalized. The long narrow straight nose becomes shorter, wider, and more bulbous. Thin asymmetrical lips become thicker and more regular. The small pointed chin and long jaw become broader and rounded. The quiet direct gaze and source head angle are frontalized, with normalized age/expression. Center-parted hair remains broadly present but the uneven source hairline and volume are regularized. These are facial-geometry and pose changes, not removable emulsion damage. The isolated forehead pinhole is correctly treated as a removable surface defect and is not the rejection reason. |
| HOI4 country-leader style | **PASS, independent of identity** | The raw repaint and candidate have subdued oil-brush texture, muted brown/charcoal/olive values, a dark quiet vignette, period civilian suit, controlled contrast, readable face, and full country-leader treatment consistent with the selected Stauning and Mannerheim references. No text, watermark, UI border, modern prop, unsupported insignia, cartoon treatment, or raw-photo-only finish is present. |
| 156 x 210 framing | **PASS** | The processed candidate is exactly 156 x 210, fully opaque, and retains head, neck, both shoulders, collar, tie, and upper jacket within the full country-leader frame. It is not a 65 x 67 dossier crop or a plain small resize. |
| Ownership / stable-consumer fit | **PASS for the consumer contract; candidate remains unwired** | Exact and variant searches for `Douwe Kalma`, `Kalma, Douwe`, `Douwe_Kalma`, and `DouweKalma` found no competing vanilla character/history/localisation/GFX owner. The intended project owner is `AGX_friesland_coastal_council` in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-103`, recruited by `history/countries/AGX - Frisia.txt:17`, localized as `Douwe Kalma` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:5`, and bound only to `GFX_portrait_AGX_friesland_coastal_council` at `interface/006_independence_wave_region_01_portraits.gfx:19-20`. |
| Absence of advisor / dossier / `_small` assets | **PASS** | The trial workspace contains no advisor, high-command, dossier, operative, commander, or `_small` asset. The character defines only a civilian `large` portrait. No `portraits = { army = { small = ... } }` consumer or AGX `_small` runtime texture exists. |

## Existing runtime texture warning

The documented runtime path already contains a pre-existing DDS at `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` with SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2` and a valid 156 x 210 legacy BGRA header.

That file predates this trial and was not created, replaced, or approved by this audit.

The rejected trial candidate must not be copied over it, and the existing texture must not be treated as evidence that trial 01 passed.

## Source-only retry contract

The mutable manifest status is now `rejected_unwired_identity_gate`.

A retry must start from the unchanged master and exact crop and must preserve these immutable traits: the very long narrow face; pointed chin and long tapering jaw; narrow unequal heavy-lidded eyes; quiet direct gaze; unequal prominent ears; long narrow straight nose and small tip; thin asymmetrical lips; exact young-adult age, expression, head angle, neck length, and shoulder slope; center-parted hair with the uneven source hairline; and source-visible suit, high white collar, tie silhouette, and both-shoulder framing.

Only the isolated viewer-left forehead emulsion pinhole may be removed.

Do not brighten or open the eyes, shorten or widen the nose, thicken lips or brows, hide or regularize the ears, broaden or soften the jaw, enlarge the chin, beautify, age, rejuvenate, frontalize, symmetrize, smooth, genericize, substitute another man, add hidden detail, or add unsupported uniform, medals, badges, political symbols, flags, text, frame, or UI border.

No generated/generic person, advisor portrait, dossier card, `_small` derivative, fallback, DDS conversion, or runtime wiring is authorized by this failure result.

## Validation and omissions

- Recomputed every entry in `hashes.sha256` after editing the manifest; all entries match.
- Verified source, crop, raw, candidate, review, metadata, and reference dimensions and decodes with Pillow.
- Verified the candidate alpha is fully opaque and the candidate dimensions are exactly 156 x 210.
- Verified the recorded processor hash and both selected-reference hashes against the current files.
- Rechecked exact/variant identity ownership terms in project and installed vanilla character/history/GFX/interface/localisation roots.
- Inspected the retained source, crop, raw repaint, candidate, review sheet, selected references, and role quick-reference at native size and a separate 4x nearest-neighbour scale.
- Verified the candidate was not converted or wired by this audit and no source/runtime asset was modified.
- Skipped DDS conversion, `.gfx` edits, gameplay edits, localisation edits, live HOI4 loading, and any fallback because the identity gate failed and the task explicitly forbids those actions.

## Files changed by this audit

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/frisia_douwe_kalma_trial_01/manifest.md` — status changed to `rejected_unwired_identity_gate`; independent gate results, evidence, and immutable retry traits added.
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/frisia_douwe_kalma_trial_01/hashes.sha256` — manifest hash refreshed; all other artifact hashes unchanged.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_frisia_douwe_kalma_trial01_independent_audit_2026_07_24.md` — this audit handoff.

No simplification or fallback was used.
