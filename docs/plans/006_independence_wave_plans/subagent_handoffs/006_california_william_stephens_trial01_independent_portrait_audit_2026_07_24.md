# IW-184 California William D. Stephens trial 01 independent portrait audit

Audit date: 2026-07-24.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/california_william_stephens_trial_01/` against the unchanged Library of Congress master, exact crop and equality record, source-locked ImageGen repaint, native `156x210` candidate, processor metadata, leader references, and the current HBX Event 6 consumer.

Final disposition: `PASS`; the exact candidate is runtime-authorized for the guarded `Daniel Mercer` to William D. Stephens identity promotion and subsequent DDS conversion.

The independent review compared the master, exact crop, raw repaint, candidate, and leader references at native size and a disposable `4x` nearest-neighbour inspection. The updated manifest's provider-side versus processor-side reference distinction resolves the only prior evidence concern; all gates below pass independently.

## Verdicts

| Gate | Verdict | Evidence and finding |
|---|---|---|
| Identity, provenance, and rights | `PASS` | The unchanged LOC source and rights evidence pass: the retained grayscale master is the Library of Congress George Grantham Bain object, with advisory `no known restrictions on publication`, and master SHA-256 `5ba60d2fd0fab9a0dcf6a47b08a89bed486e35e5c14fc200c7fc6204b8652b5d`; the Commons derivative is documented as cross-check evidence only. The exact crop, raw repaint, candidate file, processor-domain hashes, metadata canonical payload, and source chain are internally verified. The updated manifest explicitly separates provider-side ImageGen style inputs (`den_thorvald_stauning.png` and `ire_eamon_de_valera.png`) from the deterministic processor review-sheet pair (`den_thorvald_stauning.png` and `fin_carl_mannerheim.png`); neither reference supplies identity, so the prior apparent discrepancy is resolved. |
| Exact crop equality | `PASS` | Master rectangle `(75,130,685,940)` decodes to `610x810` and independently equals the retained crop pixel-for-pixel in RGBA. Both decoded payloads hash `3d3d617eefff51f0fc629625a41a36c167d35f26c98239ccd81e3ee36a82f883`; the crop utility and equality JSON agree. |
| Historical and alternate-history role | `PASS` | William D. Stephens served as California governor from 1917 to 1923, as a United States congressman and lieutenant governor, and as Los Angeles Chamber of Commerce director. He was alive in 1936. Those civic/state roles make the emergency California constitutional-convention chair an explicit alternate-history abstraction, and the package does not claim that he chaired a real 1936 convention. |
| Likeness and identity | `PASS` | At native and 4x, the raw repaint and processed candidate preserve the high broad forehead, bald crown, sparse side hair, unequal heavy-lidded eyes, eyebrow geometry, broad-to-narrow nose, thin upper/full lower lips, cheek and under-eye lines, compact ears, broad lower cheeks, softly squared jaw, rounded chin, older age, reserved expression, three-quarter head angle, and stout shoulder relationship. The face remains recognisably Stephens rather than a generic politician. Minor painterly simplification does not materially substitute or beautify the identity. |
| HOI4 leader style | `PASS` | The candidate is a full `156x210` restrained painted country-leader portrait with subdued neutral background, readable head-and-shoulders framing, matte oil/gouache treatment, and the correct leader family. The retained review sheet uses canonical `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` style references, both full `156x210` leader textures. |
| Native framing | `PASS` | Candidate is exactly `156x210`, with the head and both shoulders inside the canvas and no frame, card, text, watermark, UI, or extra person. The current consumer is civilian-only large portrait usage. |
| Male-only scope | `PASS` | The subject is male-presenting, the current HBX character has `gender = male`, and the package contains no female asset or female metadata. |
| Guarded stable-consumer transfer | `PASS` | The stable consumer is singular: `HBX_independence_wave_civic_convention_chair` uses `GFX_portrait_HBX_independence_wave_civic_convention` in `civilian.large`, is recruited by `history/countries/HBX - California.txt`, and is registered by `interface/006_independence_wave_pacific_portraits.gfx`. Exact current-project, vanilla, Kaiserreich, and approved-mod character-root searches found no William D. Stephens/William Stephens owner or HBX clone. Nonmatching surname hits (`Percy Stephensen`, `William Samuel Stephenson`, and `Donald Stephens`) are distinct people and not ownership conflicts. The same stable token is authorized for the guarded rename from `Daniel Mercer`. |
| No advisor/dossier/operative/commander/`_small` derivatives | `PASS` | The HBX character defines only `civilian.large`; no advisor, dossier, operative, commander, or `_small` slot or file exists in this package or its GFX handoff. Processor advisor fields are null. |

## Exact retained hashes and dimensions

| Artifact | Dimensions/mode | Independent SHA-256 |
|---|---|---|
| `source_masters/HBX_william_stephens_loc_master.jpg` | `743x1024` L | `5ba60d2fd0fab9a0dcf6a47b08a89bed486e35e5c14fc200c7fc6204b8652b5d` |
| `source_crops/HBX_william_stephens_head_shoulders.png` | `610x810` L | `d87f5fe6773844b597a4a1175dd26a6016a5a9df87a6295ce074f92d33ea2085` |
| Crop decoded RGBA payload | `494100` pixels | `3d3d617eefff51f0fc629625a41a36c167d35f26c98239ccd81e3ee36a82f883` |
| `source_crops/HBX_william_stephens_head_shoulders.json` | JSON | `103998c275bacfba65d8598ce01ee027ee797f2d3f99228c101855715cb57bfb` |
| `imagegen_results/HBX_william_stephens_identity_preserve_trial_01.png` | `1080x1456` RGB | `9e52bfebc1dfca49ffb08aad3cb4742242685770ad6f443f07a8c05f67b84ccc` |
| Raw repaint processor-domain decoded RGBA payload | `1080x1456`, domain-separated | `19c5ebbaab76cf706632f20018dcfe837fb3033b1bbc63b0be4df9f0806e0325` |
| `processed_png/portrait_HBX_independence_wave_civic_convention.png` | `156x210` RGBA | `6bac5f87d3df3aeb4fd9b92bae2c51a204739ece11ba820c28e49a2de3362154` |
| Candidate processor-domain decoded RGBA payload | `156x210`, domain-separated | `c51843bd453cd9c08764ac2bf23ec475b4a1667b9250adb9854280c1a620fae9` |
| `processed_png/portrait_HBX_independence_wave_civic_convention.png.json` | JSON | `4bbe5bf4556edeee102c03477a8325b36b24d14ee2beac242e4999bad2fa750c` |
| `review/HBX_william_stephens_leader_style_sheet.png` | `1344x464` RGBA | `df014fc2965d688a4e3281cb5d1aea1afe3562bcb3c6e21d4d1ffa9c70b436cf` |
| Review-sheet processor-domain decoded RGBA payload | `1344x464`, domain-separated | `d4f2f7e91a001a6bf27997883d767dc97154b70ae76548a3478c4d8573274cd7` |
| Canonical `den_thorvald_stauning.png` | `156x210` RGBA | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| Canonical `fin_carl_mannerheim.png` | `156x210` RGBA | `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e` |
| Canonical `ire_eamon_de_valera.png` named by manifest | `156x210` RGBA | `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0` |

The crop utility hash recorded in the crop JSON and present in the repository is `14fa178d6df999346874a7033e84f9b3ae988e7d845f3a4b2f8a44755e30641c`. The processor hash recorded in the candidate metadata and present in the repository is `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`.

The processor's decoded-RGBA scheme is `SHA256(b"chaos-redux-decoded-rgba-v1\\0" + width.to_bytes(4,"little") + height.to_bytes(4,"little") + RGBA bytes)`. Independently recomputed raw, candidate, and review-sheet digests match the retained metadata values above. The metadata canonical JSON payload hash recomputes to `82ef895c4ab97afd3318886a6e9a4881836379ea5078f734642a431383ab3899`, matching its integrity record.

## Consumer and ownership evidence

The current stable consumer is `HBX_independence_wave_civic_convention_chair` with sprite `GFX_portrait_HBX_independence_wave_civic_convention` and intended runtime path `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds`.

The current runtime DDS already exists at that path with SHA-256 `7cd86794c10c9621f90340490e2d57b72edd01b6c785240db943fe9253af145e`, valid legacy dimensions `156x210`, pixel-format size `32`, flags `65`, and `DDSCAPS_TEXTURE`; it was not modified or replaced by this audit.

The current localisation still names the character `Daniel Mercer` at `localisation/english/006_independence_wave_pacific_l_english.yml:11`, and the description at line 12 describes Mercer. The parent is authorized to update these strings to William D. Stephens in the same guarded promotion as the exact candidate DDS.

## Remaining risks and required disposition

1. Keep the stable character key, sprite, civilian-large-only ownership, male gate, and no-advisor/no-commander/no-`_small` scope unchanged.
2. Convert this exact approved candidate to the stable `156x210` DDS, prove its decoded-pixel equality, and update the player-facing name and description from `Daniel Mercer` to William D. Stephens in the same guarded promotion.
3. Request a fresh IW-184 country-package audit after the runtime promotion; no portrait gate remains blocked.

No files other than this audit handoff were created or modified by this audit.
