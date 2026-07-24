# IW-006 Wallonia Herman Baltia trial 03 independent portrait audit

Audit date: 2026-07-24.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_03/` against its immutable archival master, exact crop and equality record, source-only ImageGen repaint, native `156x210` candidate, prompt, processor metadata, canonical commander references, and the current Event 6 consumer.

Final disposition: `FAIL`; trial 03 remains export-only and is not authorized for localisation rename or DDS promotion.

The independent review compared the master, exact crop, raw repaint, candidate, and commander references at native size and a disposable `4x` nearest-neighbour inspection. Identity is a separate gate and commander style cannot compensate for likeness drift.

## Verdicts

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Provenance and rights | `PASS` | The unchanged Commons upload is identified as `General_Baltia_Herman.jpg`, Public Domain Mark 1.0/`PD-old`, with master SHA-256 `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66`; the raw repaint and candidate file hashes match the package. The processor's decoded-RGBA digest uses `b"chaos-redux-decoded-rgba-v1\\0" + width + height + RGBA bytes`; recomputation gives raw source `4c91ea8d390d9358449255ed97914b1b4ecb4d43de4a6e3095a685ae81ae713c` and candidate `477c7c86b4ac15ae4630fceae2d1c809d6069a342d2af1cc53463eccea54e720`, exactly matching metadata. The metadata canonical payload hash also matches. |
| Exact crop equality | `PASS` | Master rectangle `(20,12,373,473)` decodes to `353x461` and independently equals the retained crop pixel-for-pixel in RGBA. Both decoded payloads hash `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326`; the crop utility and equality JSON agree. |
| Historical role | `PASS` | The package identifies Herman Baltia as a Belgian lieutenant-general tied to the Arlon-based 10th Line Regiment and its Chasseurs Ardennais lineage, and explicitly describes the Event 6 position as an alternate-history territorial/reserve-command abstraction. It does not claim that Baltia historically commanded an independent Walloon state or that the source's 1909 uniform is a 1936 uniform. |
| Likeness and identity | `FAIL` | Trial 03 is closer than trial 02, but the source-locked real-person gate still fails at native and 4x. The repaint broadens the long lean face and jaw, rounds the pointed chin, thickens and regularises the unequal moustache curls, reduces the source eye-size/height asymmetry, and fills/regularises the sparse receding hairline. The nose is closer than trial 02 but remains broader and shorter through the bridge/tip relationship. These are visible identity-geometry changes, not style preferences. The source's face asymmetries and narrow proportions are not preserved strongly enough for promotion. |
| HOI4 commander style | `PASS` | The candidate is a full `156x210` restrained painted commander portrait with subdued background, readable head-and-shoulders silhouette, matte painted treatment, and the correct canonical commander family. The selected references are Montgomery and Witzleben, both full `156x210` commander textures. |
| Native framing | `PASS` | Candidate is exactly `156x210`, with the head and both shoulders safely inside the canvas and no frame, card, text, watermark, or UI decoration. |
| Male-only scope | `PASS` | The subject is male-presenting, the current character definition has `gender = male`, and the package contains no female asset or female metadata. |
| Ownership and guarded transfer | `PASS` | Current ownership is singular and stable: `AFX_walloon_reserve_commander` is defined in `common/characters/006_independence_wave_wallonia_frisia_characters.txt` with `civilian.large` and `army.large` both using `GFX_portrait_AFX_walloon_reserve_commander`; it is recruited by `history/countries/AFX - Wallonia.txt` and registered by `interface/006_independence_wave_region_01_portraits.gfx`. Exact vanilla and approved-mod character-root searches found no Herman Baltia/Baltia owner, portrait consumer, or `AFX_walloon_reserve_commander` clone. Current-project searches found only this AFX consumer and the old Marcel Delcourt localisation. No origin owner or simultaneous owner was found, so a player-facing localisation transfer on the same stable token is structurally safe if the identity gate passes. |
| No advisor/dossier/operative/`_small` derivatives | `PASS` | The character has only `civilian.large` and `army.large`; no advisor, dossier, operative, or `_small` slot or file exists in this package. The processor metadata's advisor fields are null and no derivative asset is retained. |

## Exact retained hashes and dimensions

| Artifact | Dimensions/mode | Independent SHA-256 |
|---|---|---|
| `source_masters/AFX_herman_baltia_1909_master.jpg` | `389x473` RGB | `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` | `353x461` RGB | `4980ac2a82fae576809adc1b10141ca711118bbbc58548c63942e4650a7a25a1` |
| Crop decoded RGBA payload | `162733` pixels | `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` | JSON | `4eef10b5531c8c1660d684af5f35826204bce36f7d2ce4435a0c5871e48ac3ad` |
| `imagegen_results/AFX_herman_baltia_identity_preserve_trial_03.png` | `1097x1434` RGB | `b4ea2c284226385fd30646c59d5af9c3623289042703809e41f34bbd7e9e86eb` |
| Raw repaint processor-domain decoded RGBA payload | `1097x1434`, domain-separated | `4c91ea8d390d9358449255ed97914b1b4ecb4d43de4a6e3095a685ae81ae713c` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png` | `156x210` RGBA | `f9095a351a709b859264c61647ef9dcfcc35a9ad9244c2207e2c7474fe6d8143` |
| Candidate processor-domain decoded RGBA payload | `156x210`, domain-separated | `477c7c86b4ac15ae4630fceae2d1c809d6069a342d2af1cc53463eccea54e720` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png.json` | JSON | `c97398a5f1e5bf69e2503d3b106750a2f812ed910833251a82b36732e3df6a36` |
| `review/AFX_herman_baltia_commander_style_sheet.png` | `1344x464` RGBA | `ba861497873379eba642a5d60d1e25067436a93c2a2990603f6d6b9bfc751f79` |
| Review-sheet processor-domain decoded RGBA payload | `1344x464`, domain-separated | `8bf5e6c5a8d37ded188c9ff4a884a407ba6a2fc17c6551a3346342fc1a8ef861` |
| Canonical `eng_bernard_montgomery.png` | `156x210` RGBA | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |

The crop utility hash recorded in the crop JSON and present in the repository is `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`. The processor hash recorded in the candidate metadata and present in the repository is `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`.

## Consumer and ownership evidence

The current stable consumer is `AFX_walloon_reserve_commander` with sprite `GFX_portrait_AFX_walloon_reserve_commander` and intended runtime path `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`.

The current runtime DDS already exists at that path with SHA-256 `c75e081b57eac880a55772b96ac0d0a77e4b5fa2ba2cce74a4d46a46f17ede9a`, valid legacy dimensions `156x210`, pixel-format size `32`, flags `65`, and `DDSCAPS_TEXTURE`; it was not modified or replaced by this audit.

The current localisation still names the character `Marcel Delcourt` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and the emergency-command description repeats that name at line 91. Because likeness fails, the parent must not update these strings from this candidate.

## Remaining risks and required disposition

1. Regenerate the source-locked repaint until the forehead/hairline, unequal eyes, narrow nose, moustache asymmetry, narrow jaw/chin, and source facial proportions survive native and 4x inspection without identity drift.
2. Keep the stable character key, sprite, `civilian.large`/`army.large` ownership, male gate, and no-advisor/no-`_small` scope unchanged.
3. Do not convert or wire a DDS and do not rename the current localisation until a fresh independent audit returns `PASS` for every gate.

No files other than this audit handoff were created or modified by this audit.
