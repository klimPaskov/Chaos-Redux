# Stage 7 Biological Food/Water/Medical-Chain Sabotage Icons

## Package scope

This package contains the four ordinary-agent decision icons for the separate
covert food, water, and medical-chain sabotage route from Spec 06. It is not
the battlefield-dissemination route and does not reuse any military-raid icon.

The four parent-provided runtime sprite ids and DDS paths are preserved
exactly. No existing Chaos Redux icon was modified, overwritten, resized,
recolored, or repurposed.

Source mode is the official built-in `$imagegen` workflow. Each source was
generated as an original fictional HOI4-style symbolic icon on a flat green
chroma-key canvas, then processed locally into real RGBA transparency. No
internet or archival source was used. The final normalized prompt ledger is in
[`prompt_ledger.md`](prompt_ledger.md).

## Accepted-design coverage crosswalk

| Accepted requirement | Visual emphasis | Runtime asset package | Status |
|---|---|---|---|
| Spec 06, “Sabotage of food, water, or medical systems”: covert low-dose seed with uncertain initial attribution and severe later discovery consequences | Anthrax icon emphasizes a compromised food chain; the decision affects the combined public food, water, and medical network | `decision_bio_sabotage_anthrax` source, processed PNG, and exact DDS below | wired |
| Spec 06, same route | Plague icon emphasizes a compromised water chain; the decision affects the combined public food, water, and medical network | `decision_bio_sabotage_plague` source, processed PNG, and exact DDS below | wired |
| Spec 06, same route | Tularemia icon emphasizes a compromised medical chain; the decision affects the combined public food, water, and medical network | `decision_bio_sabotage_tularemia` source, processed PNG, and exact DDS below | wired |
| Spec 06, same route | Smallpox icon emphasizes a compromised medical chain; the decision affects the combined public food, water, and medical network | `decision_bio_sabotage_smallpox` source, processed PNG, and exact DDS below | wired |

The live consumers are the twelve internal doctrine-timing variants under
`common/decisions/biological_sabotage_decisions.txt`, presented as one action
per agent. Sprite registration is complete in `interface/biological_warfare.gfx`.

## Processing and validation contract

1. Original ImageGen RGB source PNGs were retained in `source/` at their
   generated `1254x1254` canvas.
2. The installed ImageGen chroma-key helper was run with `--auto-key border`,
   `--soft-matte`, `--transparent-threshold 12`, `--opaque-threshold 220`, and
   `--despill`; its RGBA outputs are retained in `intermediate/`.
3. Each alpha result was cropped to its visible subject plus a small
   proportional margin, fitted inside a transparent `32x32` RGBA canvas, and
   downsampled with Lanczos into `processed/`.
4. Each processed PNG was converted from the mod root with
   `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`
   to a standard one-level uncompressed BGRA DDS.
5. Every processed PNG and DDS is exactly `32x32`. Every processed PNG has
   alpha minimum `0`, alpha maximum `255`, and transparent corners. DDS
   decoding produced exact RGBA pixel equality with its processed PNG.
6. The four final DDS hashes are distinct. The contact sheet shows each final
   icon enlarged over a checkerboard review background; it is not a runtime
   asset.

## Asset records

### Anthrax

- Asset type: covert sabotage decision icon; food-chain visual emphasis
- Visual identity: grain sack and wheat sheaf with a sealed dark vial and
  heavy charcoal spore-like flecks
- Source PNG: `source/decision_bio_sabotage_anthrax_imagegen.png`
- Source dimensions / SHA-256: `1254x1254` / `4498f2bf965f6002708bb42815e94e1d5a80ba079dbf0c5b1e7ea8441e8dd5ef`
- Chroma-key intermediate: `intermediate/decision_bio_sabotage_anthrax_alpha.png`
- Intermediate SHA-256: `dbe80d6608bd82cc5e7b17b30aa7d006bec1aff23139d4ef7fe0b3dfb376a559`
- Processed PNG: `processed/decision_bio_sabotage_anthrax.png`
- Processed dimensions / SHA-256: `32x32` / `02d85c536e2f8e049ccd7fc3d0b9e2757040519ee6a1a31d630a82025bf6afda`
- Final DDS: `gfx/interface/decisions/biowarfare/decision_bio_sabotage_anthrax.dds`
- DDS dimensions / byte length / SHA-256: `32x32` / `4224` / `694b1aafb23db0ed56da760e0dc606c3a948a3bda367c208659b148e56a061e1`
- Sprite: `GFX_decision_bio_sabotage_anthrax`
- Suggested `.gfx` file: `interface/biological_warfare.gfx`
- Status: `wired`

### Plague

- Asset type: covert sabotage decision icon; water-chain visual emphasis
- Visual identity: dark rat on a cracked iron water pipe above a metal canteen,
  with a hanging droplet and clustered neck swelling
- Source PNG: `source/decision_bio_sabotage_plague_imagegen.png`
- Source dimensions / SHA-256: `1254x1254` / `6e818996b9aae079f8640049cb05ddaab76827c070a523be2367a1ce35e4b143`
- Chroma-key intermediate: `intermediate/decision_bio_sabotage_plague_alpha.png`
- Intermediate SHA-256: `7d2d584e03af34433ae8b89a446ba793aa1585b1fcfdc254ea4ff5806fd7ed71`
- Processed PNG: `processed/decision_bio_sabotage_plague.png`
- Processed dimensions / SHA-256: `32x32` / `1fa627c00008306f3945771cf8eacfb3036480949df9a048b6a3a1c5f8b3ec5f`
- Final DDS: `gfx/interface/decisions/biowarfare/decision_bio_sabotage_plague.dds`
- DDS dimensions / byte length / SHA-256: `32x32` / `4224` / `512092522e8e402d63c5cf7712d26cba5e60ade8552e6d38eeb15c3b3c332f7f`
- Sprite: `GFX_decision_bio_sabotage_plague`
- Suggested `.gfx` file: `interface/biological_warfare.gfx`
- Status: `wired`

### Tularemia

- Asset type: covert sabotage decision icon; medical-chain visual emphasis
- Visual identity: open canvas medical crate, folded bandage, sealed ampoule,
  rabbit silhouette, and small tick cue
- Source PNG: `source/decision_bio_sabotage_tularemia_imagegen.png`
- Source dimensions / SHA-256: `1254x1254` / `2ab82f3fb96846b6ce10c4f7b80c2f8a690e6603abb2fa77c2c225856532302e`
- Chroma-key intermediate: `intermediate/decision_bio_sabotage_tularemia_alpha.png`
- Intermediate SHA-256: `ee7cb8fc947f47c9018704a5a1e2dbd3446f1e303a4aeeb7f7bed43952135f1c`
- Processed PNG: `processed/decision_bio_sabotage_tularemia.png`
- Processed dimensions / SHA-256: `32x32` / `16fb4afd1df0c8f90f1b85af9d8450cac5076d121e20ca461a9c3f8c30222855`
- Final DDS: `gfx/interface/decisions/biowarfare/decision_bio_sabotage_tularemia.dds`
- DDS dimensions / byte length / SHA-256: `32x32` / `4224` / `7c1fdecedd679231225c0f68dc2d44508adc5264ea498e67fe11e5cf378d0ca0`
- Sprite: `GFX_decision_bio_sabotage_tularemia`
- Suggested `.gfx` file: `interface/biological_warfare.gfx`
- Status: `wired`

### Smallpox

- Asset type: covert sabotage decision icon; medical-chain visual emphasis
- Visual identity: medical shipment crate, folded dressings, cracked vial, and
  a strong cluster of dark red-brown pockmarks
- Source PNG: `source/decision_bio_sabotage_smallpox_imagegen.png`
- Source dimensions / SHA-256: `1254x1254` / `749126e5c0abf3cbfa01750fde09273a5d0285895d630fbc2e1250458b32a165`
- Chroma-key intermediate: `intermediate/decision_bio_sabotage_smallpox_alpha.png`
- Intermediate SHA-256: `560fd1a6ed658f6fd1e6f476effffff5fdcf6724b4efa348ffa0213de913fcb2`
- Processed PNG: `processed/decision_bio_sabotage_smallpox.png`
- Processed dimensions / SHA-256: `32x32` / `b75fbda0f2cc324159228d66ac506170f569968e5b76b2b29fe7e867cfb3fd61`
- Final DDS: `gfx/interface/decisions/biowarfare/decision_bio_sabotage_smallpox.dds`
- DDS dimensions / byte length / SHA-256: `32x32` / `4224` / `58a72fd3cac0caf013d5580857a0f7655923e6b9e5c2b65975ce5f90ea705659`
- Sprite: `GFX_decision_bio_sabotage_smallpox`
- Suggested `.gfx` file: `interface/biological_warfare.gfx`
- Status: `wired`

## Review artifact

- Contact sheet: `contact_sheet.png`
- Contact sheet dimensions / SHA-256: `760x600` /
  `30523168d18d64dafd9dd090a13e33a6f7a9f7621ef457cc14c0b78046827b7f`

## Asset-production exclusions

- No files under `gfx/interface/military_raids/` or `gfx/interface/raids/`
  were touched.
- No `decision_bio_battlefield_*.dds` file was touched.
- The asset-production subagent did not edit `.gfx`, `.gui`, localisation,
  gameplay, decision, spec, or spreadsheet files. Main-agent integration later
  registered the sprites, decisions, and localisation recorded above.
- No icon from another UI surface was resized or used as a substitute.
