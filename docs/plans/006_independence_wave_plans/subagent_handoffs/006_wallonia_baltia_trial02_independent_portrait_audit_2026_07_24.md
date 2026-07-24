# IW-006 Wallonia Herman Baltia trial 02 independent portrait audit

Audit date: 2026-07-24.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_02/` against the immutable source, exact crop record, raw ImageGen repaint, native `156x210` candidate, prompt, processor metadata, commander references, and the current Event 6 consumer.

Final disposition: `FAIL`; export-only and not authorized for localisation rename or DDS promotion.

The independent review compared the master, exact crop, raw repaint, candidate, and commander references at native size and a disposable `4x` nearest-neighbour inspection. Identity is a separate gate and style quality cannot compensate for the likeness failure.

## Verdicts

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance and rights | `PASS` | The unchanged Commons upload is identified as `General_Baltia_Herman.jpg`, Public Domain Mark 1.0/`PD-old`, with the recorded master SHA-256 `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66`; the raw repaint and candidate file hashes match the package record. The processor's decoded-RGBA digest is domain-separated, using `b"chaos-redux-decoded-rgba-v1\\0" + width + height + RGBA bytes`; recomputation gives candidate `eab689a10a5b42c5aaf4e0fefb99f301b95615c55d11437a7ccdeeaba2aef435`, exactly matching the retained artifact metadata. The retained determinism source digest `fcb8b259c0e7d0d7fa988e92152c3b8b05303d598a0f5366f76aa50bcea33c9a` likewise matches the raw repaint under the same scheme. The plain unprefixed RGBA digest `411a2a3ec2b4c5cbea94250087fc284cb4dc51f32da92a9fe03e80abfaa84753` is only a diagnostic and is not the processor's integrity value. |
| Exact crop equality | `PASS` | Master rectangle `(20,12,373,473)` decodes to `353x461` and independently equals the retained crop pixel-for-pixel in RGBA. Both decoded payloads hash `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326`; the crop utility and metadata hashes also match. |
| Historical role | `PASS` | The package identifies the subject as Herman Baltia and explicitly limits the historical claim to his Belgian/Arlon and Chasseurs Ardennais lineage. It correctly states that the Event 6 senior territorial/reserve-command role is an alternate-history abstraction and does not claim that he commanded an independent Walloon state in real history. |
| Likeness and identity | `FAIL` | The archival face is recognisable in the repaint, but the source-locked requirements are not preserved strongly enough for a real-person portrait. At native and 4x, the repaint materially widens/shortens the long narrow nose, regularises the unequal deep-set eyes, thickens and symmetrises the moustache curls, and broadens the long narrow jaw/chin. The receding hairline is fuller and the source asymmetries are softened. These are identity drift findings, not style preferences. |
| HOI4 commander style | `PASS` | The candidate is a full `156x210` restrained painted commander portrait with subdued background, readable head-and-shoulders silhouette, matte painted treatment, and the correct commander reference family. The selected canonical references are Montgomery and Witzleben, both `156x210` commander PNGs. |
| Native framing | `PASS` | Candidate is exactly `156x210`, with the head and both shoulders inside the canvas and no frame, card, text, watermark, or UI decoration. |
| Male-only scope | `PASS` | The subject is male-presenting, the current character definition has `gender = male`, and the package contains no female asset or female metadata. |
| Ownership and stable-consumer transfer | `PASS` | Current ownership is singular and stable: `AFX_walloon_reserve_commander` is defined in `common/characters/006_independence_wave_wallonia_frisia_characters.txt` with `civilian.large` and `army.large` both using `GFX_portrait_AFX_walloon_reserve_commander`; it is recruited by `history/countries/AFX - Wallonia.txt` and registered by `interface/006_independence_wave_region_01_portraits.gfx`. Vanilla and approved workshop searches found no Herman Baltia/Baltia owner or portrait consumer. Current-project exact searches found only this AFX character/consumer and the old Marcel Delcourt localisation; the sole approved-mod `Delcourt` hits were disabled generic surname-list entries, not character ownership. No origin owner or simultaneous owner was found, so a localisation-only name transfer would preserve the stable token if the identity gate passed. |
| No advisor/dossier/operative/`_small` derivatives | `PASS` | The character has only `civilian.large` and `army.large`; no `advisor`, `dossier`, `operative`, or `_small` slot or file exists in this package. The retained package contains only the source master/crop, raw repaint, full candidate, style sheet, prompt, and metadata. |

## Exact retained hashes and dimensions

| Artifact | Dimensions/mode | Independent SHA-256 |
|---|---|---|
| `source_masters/AFX_herman_baltia_1909_master.jpg` | `389x473` RGB | `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` | `353x461` RGB | `4980ac2a82fae576809adc1b10141ca711118bbbc58548c63942e4650a7a25a1` |
| Crop decoded RGBA payload | `162733` pixels | `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` | JSON | `b60815e5abd161b2e58858bf44a12b63f824a95cdb615735b85857b3230190e5` |
| `imagegen_results/AFX_herman_baltia_identity_preserve_trial_02.png` | `1097x1434` RGB | `fcfe0ebb08adb38fe974bd3b14e5957765e60b8156a0ff2a2df93c19a18e2f6f` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png` | `156x210` RGBA | `d06cfdbb56f1348cd61218c86b53a0d7c5be85220ecd83f99732e4bc51362047` |
| Candidate plain unprefixed RGBA payload (diagnostic only) | `131040` bytes | `411a2a3ec2b4c5cbea94250087fc284cb4dc51f32da92a9fe03e80abfaa84753` |
| Candidate processor-domain decoded RGBA payload | `156x210`, domain-separated | `eab689a10a5b42c5aaf4e0fefb99f301b95615c55d11437a7ccdeeaba2aef435` |
| Raw repaint processor-domain decoded RGBA payload | `1097x1434`, domain-separated | `fcb8b259c0e7d0d7fa988e92152c3b8b05303d598a0f5366f76aa50bcea33c9a` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png.json` | JSON | `963edabb634879a804afc4333a89adf6fc37c98534a31b6b10759e402db2c7a5` |
| `review/AFX_herman_baltia_commander_style_sheet.png` | `1344x464` RGBA | `5aa51dc2a58080920421512a3acc4547292321e3da107e53f519f2d6f35d110f` |
| Canonical `eng_bernard_montgomery.png` | `156x210` RGBA | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |

The crop tool hash recorded in the crop JSON and present in the repository is `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`. The processor hash recorded in the candidate metadata and present in the repository is `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`.

## Consumer and ownership evidence

The current stable consumer is `AFX_walloon_reserve_commander` with sprite `GFX_portrait_AFX_walloon_reserve_commander` and intended runtime path `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`.

The current runtime DDS already exists at that path with SHA-256 `c75e081b57eac880a55772b96ac0d0a77e4b5fa2ba2cce74a4d46a46f17ede9a`, valid legacy dimensions `156x210`, pixel-format size `32`, flags `65`, and `DDSCAPS_TEXTURE`; it was not modified or replaced by this audit.

The current localisation still names the character `Marcel Delcourt` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and the emergency-command description repeats that name at line 91. Because likeness and provenance gates fail, the parent must not update these strings from this candidate.

## Remaining risks and required disposition

1. Regenerate or recrop from the unchanged archival crop until the nose, unequal eye geometry, moustache asymmetry, jaw/chin proportions, and receding hairline remain source-faithful at native and 4x inspection.
2. Preserve the processor-domain hash method in any regenerated metadata; the retained candidate output digest `eab689a10a5b42c5aaf4e0fefb99f301b95615c55d11437a7ccdeeaba2aef435` and raw-source seed digest `fcb8b259c0e7d0d7fa988e92152c3b8b05303d598a0f5366f76aa50bcea33c9a` independently match the package metadata.
3. Keep the stable character key, sprite, `civilian.large`/`army.large` ownership, male gate, and no-advisor/no-`_small` scope unchanged.
4. Do not convert or wire a DDS and do not rename the current localisation until a fresh independent audit returns `PASS` for every gate.

No files other than this audit handoff were created or modified by this audit.
