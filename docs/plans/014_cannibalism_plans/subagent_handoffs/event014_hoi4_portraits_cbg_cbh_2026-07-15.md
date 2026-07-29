# Event 014 AMX/CBH HOI4 Portrait Repaint Handoff

Date: 2026-07-15
Owner: `event014_portraits_cbg_cbh_hoi4`
Scope: the 14 static AMX and CBH warlord leader portraits only. No gameplay, interface, localisation, Hannibal asset, shared manifest, aggregate hash, validation summary, or prompt-matrix file was edited.

## Delivered package

All fourteen portraits were regenerated as original fictional bald or severely shorn adult male warlords. Each requested prop action remains readable in the final 156x210 leader crop. The accepted masters follow the requested classic HOI4 country-leader visual language: opaque matte oil/gouache handling, simplified facial planes, firm painted edges, low photographic microdetail, a muted 1930s-1940s palette, and quiet brushed backgrounds.

ImageGen was called separately for every portrait. Every call used these three vanilla portraits as style, crop-language, value-range, and paint-finish references only:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

No referenced identity, face, clothing, pose, or insignia was copied. The set contains no modern equipment or materials, prison or restraint imagery, living Indigenous sacred motifs, or graphic injury.

## Portrait matrix

| Stem | Required action preserved in source and leader crop |
| --- | --- |
| `leader_AMX_warlord` | Clenches the knot of a cord looped through a cracked jaw relic between his teeth. |
| `leader_AMX_warlord_africa` | Holds a mud-dark boot heel directly beneath his nose with ecstatic disgust. |
| `leader_AMX_warlord_asia` | Smears rust-red sealing wax across a blank ledger and his cheek. |
| `leader_AMX_warlord_middle_east` | Chews the corner of a captured field map while grinning at the viewer. |
| `leader_AMX_warlord_north_america` | Displays a molar on his tongue beside a small secular skull token. |
| `leader_AMX_warlord_south_america` | Bites and counts a necklace of mismatched teeth. |
| `leader_AMX_warlord_oceania` | Sews a plain human-shaped leather mask with the thread held between his teeth. |
| `leader_CBH_warlord` | Pulls his filed grin wider while studying it in a cracked mirror. |
| `leader_CBH_warlord_africa` | In three-quarter side profile, polishes one oversized ivory-colored tooth charm pinned against the black wool sleeve beside his cheek while his other arm remains folded across his chest. |
| `leader_CBH_warlord_asia` | Holds a glossy black leech-shaped wax charm at his lip. |
| `leader_CBH_warlord_middle_east` | Grinds a tooth charm on a whetstone and tastes the dust. |
| `leader_CBH_warlord_north_america` | Rolls a spent brass casing across his tongue. |
| `leader_CBH_warlord_south_america` | Holds a jawbone-shaped nutcracker beside his cheek and mimics its bite. |
| `leader_CBH_warlord_oceania` | Stitches a pale leather patch onto his high collar with a curved needle held between his teeth. |

Each face, skull silhouette, expression, garment arrangement, and prop interaction is distinct. The two initial AMX default and Africa generations were rejected after processed comparison because their finish was too glossy. Both were regenerated with a stricter matte-gouache prompt, reprocessed, re-exported, and visually approved; only those accepted second versions are present in the package and final DDS files.

An independent uniqueness audit then identified the earlier `leader_CBH_warlord_africa` as borderline similar to `leader_AMX_warlord_south_america`: both used a near-frontal, two-handed tooth-row presentation. That CBH Africa result was rejected. The accepted audit-driven third version uses a strong three-quarter side profile, one single vertical sleeve-pinned charm, one rag-rubbing hand, and a folded-arm diagonal silhouette. It contains no necklace, cord, tooth row, or two-handed horizontal display. The rebuilt combined contact sheet confirms that it is unmistakably different from the frontal AMX South America tooth-necklace action.

### Audit-driven CBH Africa v3 provenance

- Built-in ImageGen output: `C:/Users/klimp/.codex/generated_images/019f6710-c26b-76b3-9731-9ce2c0e46179/exec-d5089134-8221-425a-811f-d7c81da6d6f7.png`
- Image inputs: the three style-only vanilla leader references listed above, supplied together in the single dedicated generation call
- Exact accepted prompt: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/prompts/generated/leader_CBH_warlord_africa.txt`
- Accepted workspace master: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/source_png/leader_CBH_warlord_africa_source.png`
- Accepted source SHA-256: `144de6dcbc9d3c7f76efaaf59d353c61d013b0924ecb4416dc06a073b8026f26`
- Deterministic crop: source 1080x1456, crop `0 1 1080 1455`
- Processed PNG SHA-256: `ccd7e274e20ab0b137a83582aaa9e939a2f04b38bcfe1157cd6cf874378a1345`
- Review-sheet SHA-256: `4bbec06f80d424e18202a47fb99843e6b9ee0a5c14bd9ec7e2560e43d0d093d6`
- Final DDS SHA-256: `0b947b723e90be0f1eaa3f7cb8ed6a3cf05031010b21ee3e8a89289b7b2668bd`
- Rebuilt combined contact-sheet SHA-256: `4070c346e0747c3158d71ad24e18d0a7bd4d8c2024a1537eb21473a0d2b4b3c1`

## Files and locations

- Accepted ImageGen masters: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/source_png/leader_AMX_warlord*_source.png` and `leader_CBH_warlord*_source.png`
- Exact accepted prompts: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/prompts/generated/leader_AMX_warlord*.txt` and `leader_CBH_warlord*.txt`
- Finished leader PNGs: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/processed_png/leader_AMX_warlord*.png` and `leader_CBH_warlord*.png`
- Processor metadata: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/metadata/leader_AMX_warlord*.json` and `leader_CBH_warlord*.json`
- Per-portrait review sheets: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/reviews/leader_AMX_warlord*_review.png` and `leader_CBH_warlord*_review.png`
- Combined visual review: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/cbg_cbh_hoi4_repaint_contact_sheet.png`
- Final game DDS files: `gfx/leaders/014_cannibalism/leader_AMX_warlord*.dds` and `leader_CBH_warlord*.dds`

## Deterministic finishing

Every portrait was processed with `the retired portrait-processing utility leader`, `--source-kind fictional`, the leader reference directory above, an explicit crop, a metadata JSON, and an individual comparison sheet. Every processed PNG is 156x210. Every DDS was created with `.tools/convert_to_dds.py --width 156 --height 210`.

The crop geometry recorded in metadata is:

| Stem | Source size | Crop |
| --- | --- | --- |
| `leader_AMX_warlord` | 1081x1455 | `0 0 1081 1455` |
| `leader_AMX_warlord_africa` | 1085x1450 | `4 0 1081 1450` |
| `leader_AMX_warlord_asia` | 1080x1457 | `0 1 1080 1455` |
| `leader_AMX_warlord_middle_east` | 1080x1456 | `0 1 1080 1455` |
| `leader_AMX_warlord_north_america` | 1082x1454 | `1 0 1081 1454` |
| `leader_AMX_warlord_south_america` | 1081x1455 | `0 0 1081 1455` |
| `leader_AMX_warlord_oceania` | 1080x1456 | `0 1 1080 1455` |
| `leader_CBH_warlord` | 1080x1456 | `0 1 1080 1455` |
| `leader_CBH_warlord_africa` | 1080x1456 | `0 1 1080 1455` |
| `leader_CBH_warlord_asia` | 1080x1456 | `0 1 1080 1455` |
| `leader_CBH_warlord_middle_east` | 1080x1456 | `0 1 1080 1455` |
| `leader_CBH_warlord_north_america` | 1082x1453 | `1 0 1080 1453` |
| `leader_CBH_warlord_south_america` | 1082x1453 | `1 0 1080 1453` |
| `leader_CBH_warlord_oceania` | 1080x1456 | `0 1 1080 1455` |

The processor metadata retains its machine status `candidate_requires_visual_approval`. Manual approval is recorded here: every generated master was inspected at generation time, every final crop was reviewed against the vanilla references in its individual comparison sheet, and the complete set was reviewed together in the combined contact sheet. The gestures remain legible, the figures remain unique, and the final set is coherent with the three style references.

## Wiring and validation evidence

Existing sprite definitions in `interface/014_cannibalism.gfx` lines 215-230 already point to the exact fourteen DDS filenames, including each default portrait reused for its European sprite. No interface edit was required or made.

- 14/14 source masters, accepted prompt files, processed PNGs, metadata files, review sheets, and DDS files are present.
- Metadata source SHA-256 values match the current accepted masters, and all metadata output sizes are 156x210.
- Source SHA-256 hashes are unique across all fourteen masters; processed PNG SHA-256 hashes are also unique across all fourteen finals.
- All DDS headers validate as uncompressed 32-bit BGRA, 156x210, with opaque alpha; each file is 131,168 bytes.
- The accepted prompt text files match the prompts used in their individual ImageGen calls.
- The 1228x905 combined contact sheet was inspected at original resolution after final processing and includes all fourteen finals with the three vanilla style references.
- The audit comparison specifically confirms that `leader_CBH_warlord_africa` uses one vertical sleeve-pinned charm in side profile and no longer duplicates `leader_AMX_warlord_south_america`'s frontal two-handed tooth-necklace silhouette.

Shared `manifest.md`, `hashes.sha256`, `source_generation_metadata.md`, `validation.md`, and `prompts/prompt_matrix.md` were intentionally left untouched under the parent-granted ownership boundary. Aggregate records can be refreshed after all portrait batches are assembled.

## Simplifications, omissions, and blockers

None within the assigned fourteen-portrait scope. No fallback art, transform-only substitute, placeholder, missing action, missing regional variant, or unwired filename was accepted. No commit was created, as requested.

## Skills used

- `imagegen`
- `chaos-redux-event-assets`

No skill was created or updated.
