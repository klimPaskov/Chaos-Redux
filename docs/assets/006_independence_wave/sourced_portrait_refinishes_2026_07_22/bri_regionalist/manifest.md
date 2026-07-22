# Event 006 BRI regionalist portrait refinish

Date: 2026-07-22  
Asset: `leader_bri_regionalist_regis_de_l_estourbeillon`  
Role: existing `BRI_independence_wave_civic_delegate` country-leader token; male civic/regionalist leader  
Identity classification: `grounded_identity`  
Source treatment: attributed real-person source plus ImageGen edit restricted to identity-preserving repaint/recomposition  
Package status: `approved_and_wired` (revision 3 passed independent visual/provenance review and parent runtime conversion)

## Source authority

The only identity source used is the source-ready John Wickens 1904 photograph
retained by the source-research package:

- source master: `../../sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`
- source dimensions: `1145x1707`, JPEG, RGB
- source SHA-256: `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`
- source link: [Commons File:Estourbeillon.jpg](https://commons.wikimedia.org/wiki/File:Estourbeillon.jpg)
- direct original: [upload.wikimedia.org original](https://upload.wikimedia.org/wikipedia/commons/b/b5/Estourbeillon.jpg)
- provenance: John Wickens, *A Book of Mad Celts* (1904); subject described as the Marquis de Estourbeillon in Breton national costume at the Pan-Celtic Congress
- rights basis: Wikimedia Commons records Public domain/PD. The retained source package also records Wickens's 1864-1936 dates, the UK life-plus-70 analysis, pre-1929 publication, and the missing structured copyright-status caveat. Preserve attribution and do not treat the Commons tag as the sole rights evidence.

The Maurice Dulac 1898 illustration was not used as an identity source and was
not included in this package.

The unchanged source master is also retained byte-for-byte inside this package
for direct v2/v3 comparison:

- `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_john_wickens_1904_source_master.jpg`
- dimensions: `1145x1707`, JPEG RGB
- SHA-256: `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`

## Ownership and role evidence

The source package's bounded ownership scan searched exact and variant forms of
`Régis de l'Estourbeillon`, `L'Estourbeillon`, and related spellings across the
current project and vanilla character, leader, commander, operative,
officeholder, portrait, `.gfx`, and localisation roots. It found no active
owner or consumer. The same package records institutional role evidence from
BnF, Assemblée nationale Sycomore, and CRBC/PRELIB: founder/president of the
Union régionaliste bretonne, a Morbihan deputy, and a conservative Breton
regionalist civic figure alive at the 1936 start. See the source package's
`search_notes/ownership_and_candidate_log.md` for the complete search terms,
roots, and evidence chain.

## Selected source-preserving edit

- ImageGen selected raw master: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png`
- raw dimensions: `1024x1536`, PNG RGB, opaque; SHA-256 `CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7`
- retained alternative for comparison: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`
- alternative dimensions: `1080x1456`, PNG RGB, opaque; SHA-256 `8BE51C6A25E14BB93CE1996483F0E76CAB76B708118723091C998B49E454418B`
- generated-image intent: edit the sourced person, not generate or substitute an identity
- invariants checked visually: same male face, moustache, apparent age, expression/gaze, head angle, hat, and visible period Breton costume; no invented medals, insignia, tartan, pseudo-Celtic motif, sacred/cultural symbol, flag, text, modern prop, stereotype, or generic face
- style references inspected: canonical vanilla leader family contact sheet and `portraits/leaders/den_thorvald_stauning.png`, `portraits/leaders/fin_carl_mannerheim.png`; references supplied only for quiet pale background, head-and-shoulders framing, restrained brush texture, and controlled contrast
- review sheet: `contact_sheets/bri_regionalist_identity_review.png` (source crop, both ImageGen candidates, selected processed output, and canonical style references; review only)

## Revision 3 current candidate

- ImageGen v3 raw master: `source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master_v3.png`
- raw dimensions: `1082x1454`, PNG RGB, opaque; SHA-256 `660E954102CC6DF902792E84D0B0F97F178351476485A008362E64A1610E8120`
- processed preview: `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`
- processed dimensions: `156x210`, PNG RGB, opaque; SHA-256 `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80`
- generation intent: strict edit of the John Wickens source photograph, not a new identity
- style references: skill-local male vanilla HOI4 country-leader portraits `leader_portraits/leaders/den_thorvald_stauning.png`, `leader_portraits/leaders/ire_eamon_de_valera.png`, and `leader_portraits/leaders/afg_mohammed_zahir_shah.png`; references were used only for full-color restrained HOI4 paint, pale quiet backdrop, controlled values, and head-and-shoulders composition
- visual direction: muted charcoal/black, slate, subdued tan/gray and restrained dull-metal highlights; quiet painted neutral background; no sepia or black-and-white treatment
- identity invariants checked: same male face, gaze, facial geometry, apparent source age, moustache, hat, costume, pose, and silhouette; no hidden detail reconstructed and no symbols, flags, text, invented insignia, medals, tartan, pseudo-Celtic motif, sacred/cultural symbol, stereotype, or generic face
- crop: source v3 master `(1,0,1081,1454)` -> `1080x1454` -> Lanczos `156x210`
- current comparison sheet: `contact_sheets/bri_regionalist_v3_comparison.png` (unchanged source crop, v2 processed, v3 processed, v3 master, and three male vanilla references; review only)

## Crop and processing

The prior v2 raw master is `1024x1536`. To preserve the complete head, hat,
shoulders, and visible upper-torso costume while matching the HOI4 portrait
ratio, a deterministic top/bottom crop was applied:

```text
crop box (x0, y0, x1, y1): (0, 79, 1024, 1457)
crop size: 1024x1378
resize: Lanczos -> 156x210
output mode: RGB, opaque (no alpha)
```

Processed preview: `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png`  
Dimensions: `156x210`, PNG RGB, opaque  
SHA-256: `BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8`

The prior v2 processed PNG remains review evidence only. The current v3
processed PNG is the sole approved DDS input.

## Exact ImageGen prompts

The selected v3 prompt, prior v2 prompt, and retained v1 prompt are preserved
verbatim in [`prompt.md`](prompt.md). The v3 edit used the unchanged source
photograph as the identity-bearing edit target and only male vanilla
country-leader portraits as style references. The comparison sheets are review
evidence, not runtime textures.

## Runtime integration

- existing sprite: `GFX_portrait_BRI_independence_wave_civic_commission`
- existing `.gfx`: `interface/006_independence_wave_brittany_portraits.gfx`
- approved runtime texture: `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`
- preserved package DDS: `final_dds/BRI/portrait_BRI_independence_wave_civic_commission.dds`
- sole approved conversion input: `processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`
- final texture: `156x210`, one-level uncompressed BGRA DDS, SHA-256 `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0`
- package and runtime DDS files are byte-identical
- no new sprite declaration is requested; preserve the existing mapping

## Fail-closed review verdict

Revision 3 is the accepted source-preserving portrait. It is visibly full-color
and painted in the restrained vanilla HOI4 direction while retaining the same
source-supported face, moustache, gaze, age appearance, hat, pose, silhouette,
and costume. The independent visual/provenance audit passed every identity,
crop, source, style, and native-readability gate; the parent then accepted the
direct comparison and converted only v3. Any later replacement must pass the
same gate and must not use the Dulac illustration or a generated, generic,
female, advisor, or operative substitute.
