# Event 006 Sicily trial-01 portrait visual and provenance audit

Audit date: 2026-07-22  
Auditor: independent read-only portrait/provenance reviewer  
Producer package: commit `d6ae414b01e8b3281b0ffed6b1f642b530571d32`  
Scope: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_trial_01/`  
Subjects: real male Luigi Sturzo, Pietro Lanza di Scalea, and Luigi Rizzo.

No runtime DDS, GFX, gameplay, localisation, stable manifest, producer asset, or
source file was edited, copied, converted, or wired by this audit. This handoff
is the only new file owned by this audit.

## Controlling rules and disposition

Sicily is a grounded historical/regional polity. The three rows therefore remain
`grounded_source_only`: each must use an unchanged attributed real-person source,
an explicit source-pixel crop, and an identity-preserving ImageGen edit. ImageGen
may change medium, background, contrast, and restrained brush texture, but may not
reconstruct a face, beautify or genericise the person, change the pose or age, or
invent identity-changing uniform details. All final leader/commander textures must
remain full `156x210` portraits; this package contains no advisor, dossier,
`_small`, or other miniature asset.

The current package passes independent source, likeness, native-canvas/style, and
male-only visual review for all three subjects. The current package status can be
promoted from `needs_user_review` for visual/provenance purposes. Runtime admission
still requires the parent to copy/rename the approved DDS bytes into the existing
runtime paths, retain source attribution, and reconcile the Rizzo role note below.
No generic or fallback face is authorized.

| Subject / result | Source validity | Exact identity likeness | Native 156x210 / HOI4 style | Wiring authorization | Overall |
|---|---|---|---|---|---|
| Luigi Sturzo / `ASX_luigi_sturzo.png` | **PASS** — direct Albert Kahn master, CC-BY-4.0 record, hash-identical local copy | **PASS** — long narrow face, high forehead, side-parted dark hair, ears, eyes, nose, mouth, jaw, neutral expression, age, straight pose, cassock and white collar remain attributable | **PASS** — modeled face, visible but restrained brushwork, quiet warm-gray painted background, controlled values, clean silhouette; clearly painted rather than a photo or simple oil filter | **PASS, conditional on parent path copy** — existing male civilian large sprite is the intended consumer; preserve attribution/change note | **PASS** |
| Pietro Lanza di Scalea / `ASX_pietro_lanza_di_scalea.png` | **PASS** — Commons/ICCD original, pre-1932, PD-old/PD-US/PDM record, hash-identical local copy | **PASS** — long oval face, combed hair, narrow moustache, side gaze, age, three-quarter pose, court/military dress, sash, epaulette, medals and stars remain source-anchored; color/decoration painting is a small simplification, not an observed identity-changing substitution | **PASS** — modeled face and regalia, deliberate brush marks, subdued charcoal background, readable at native canvas, unmistakably HOI4-painted | **PASS, conditional on parent path copy** — existing male civilian large sprite is the intended consumer; no new insignia, advisor, or `_small` slot authorized | **PASS** |
| Luigi Rizzo / `ASX_luigi_rizzo.png` | **PASS** — Commons 1935 source, Italian Navy corroboration, PD-Italy/PD-1996/US record, hash-identical local copy | **PASS** — broad square face, swept dark hair, heavy brows, thick moustache, direct gaze, stern expression, age, straight pose, Regia Marina uniform, cords, sash, medals and crosses remain identifiable; medal colour/detail is restrained source-shape colorization, with no observed added badge or changed uniform silhouette | **PASS** — controlled blue-gray painted background, face modeling and brush texture remain visible at full master and native 156x210; commander-style finish is not photographic or over-smoothed | **PASS for the existing full `army`/corps-command large consumer only**; the source is a naval admiral, while `common/characters/006_independence_wave_mediterranean_characters.txt:174-188` currently declares `corps_commander` with `army = large`. No separate navy-leader slot or new role is authorized by this visual audit | **PASS visual/provenance; wiring role caveat** |

If a later parent inspection finds material face drift, invented insignia, or a
photographic/generic finish at a larger display size, fail closed and return that
row to `NEEDS_REVISION`; do not substitute a generated person.

## Package and transformation-chain checks

Inspected the complete package: `manifest.md`, `metadata.json`, `gfx_handoff.md`,
`hashes.sha256`, all three unchanged source masters, exact crop previews, prompts,
raw ImageGen masters, processed PNGs, DDS files, and the source/crop/raw/processed/
canonical comparison sheet.

The package hash ledger was verified line by line: all 19 entries match the current
bytes, with zero missing or changed files. Source masters and direct-source
downloads independently agree as follows:

| Subject | Source master / direct master | Native source | SHA-256 |
|---|---|---:|---|
| Sturzo | `source_masters/asx_luigi_sturzo_albert_kahn_big.jpeg`; Albert Kahn direct image | `1519x2048`, JPEG, 554,180 bytes | `4c18893744627c83761ee2b838a18f2f4798026811b888ecfb96d1f1d7a168ec` |
| Lanza di Scalea | `source_masters/asx_pietro_lanza_di_scalea_commons_original.jpg`; Commons original | `602x800`, JPEG, 77,019 bytes | `5cbf419d7f33539e726f0ef4089b1c9995e1bfdbcd8b581f8eaa996659d02f0b` |
| Rizzo | `source_masters/asx_luigi_rizzo_rear_admiral_1935.jpg`; Commons original | `402x582`, JPEG, 125,508 bytes | `aa113393b9b51ed481bfa485aaf729e867c20c6a364b41d3f8999b0dc2c8663e` |

The exact crop boxes were independently applied to the unchanged masters and
matched each retained crop preview byte-for-byte after decode:

| Subject | Crop box `(left, top, right, bottom)` | Crop canvas | Preview |
|---|---:|---:|---|
| Sturzo | `(520, 330, 1170, 1205)` | `650x875` RGB | `source_masters/ASX_luigi_sturzo_source_crop_preview.png` |
| Lanza di Scalea | `(155, 15, 495, 473)` | `340x458` grayscale source crop | `source_masters/ASX_pietro_lanza_di_scalea_source_crop_preview.png` |
| Rizzo | `(70, 0, 333, 354)` | `263x354` RGB | `source_masters/ASX_luigi_rizzo_source_crop_preview.png` |

Raw ImageGen masters are retained separately and are RGB, not source overwrites:

| Subject | Raw ImageGen master | Canvas |
|---|---|---:|
| Sturzo | `imagegen_masters/ASX_luigi_sturzo_imagegen_master.png` | `1080x1456` |
| Lanza di Scalea | `imagegen_masters/ASX_pietro_lanza_di_scalea_imagegen_master.png` | `1065x1477` |
| Rizzo | `imagegen_masters/ASX_luigi_rizzo_imagegen_master.png` | `1080x1456` |

Each processed candidate is RGBA `156x210` with alpha min/max `255/255`. DDS
validation independently found the legacy one-level BGRA header, dimensions,
`DDSCAPS_TEXTURE`, exact length `131168` bytes, and a lossless Pillow RGBA
round-trip for every row:

| Subject | Processed PNG SHA-256 | Package DDS SHA-256 |
|---|---|---|
| Sturzo | `cef2e7ac3c7548a012bea3f6f009aff6c892774cc70126262b1d190e2cb41ff4` | `4768e69316d2a03754be052143c68a157902c6953d99ce9389472ed1ada52e57` |
| Lanza di Scalea | `0e1b84ac901ac5c14ee029a7d4222e0f5eebe396c801a5604c684bb00d5ff650` | `7d1201f05a7189001b88a9d7aa9b5e2ed565379cbd30f2fe170ef6aaa245475a` |
| Rizzo | `a950f3737ba12dca1dd21372347e0999e0a80166be5076024a1f41ee9a6ebafd` | `659c819547559f50025fb3007cd5c60947a150ca4673238cc179dc2f0867d714` |

The retained prompts explicitly declare Image 1 as the sole identity source and
the canonical reference as style-only. The visual sheet was reviewed at full
master and native output size against the selected canonical male family refs.

## Subject-by-subject visual review

### Luigi Sturzo

The unchanged Albert Kahn autochrome crop shows a very narrow, elongated face,
high forehead, dark side-parted hair, prominent ears, deep-set eyes, long nose,
thin mouth, tapering jaw, neutral expression, and black clerical cassock with a
small white collar. The raw ImageGen master and native processed PNG retain those
same landmarks and the straight-on pose. The result does not add facial hair,
clerical ornament, medals, a hat, a flag, text, a modern object, or another
person. The result remains visibly male and reads as a country-leader portrait.

The raw and native images use modeled planes and deliberate brush marks over a
quiet olive/warm-gray painted backdrop. The texture is stronger and the backdrop
darker than `den_thorvald_stauning.png`, but the result remains a controlled
HOI4-style painted portrait rather than a photograph, sharpened archival scan,
over-smoothed render, or generic face. No identity drift was found at native
size or in the full raw master.

### Pietro Lanza di Scalea

The source is a formal three-quarter portrait with long oval face, neatly combed
dark hair, narrow moustache, side gaze, calm formal expression, ornate dark court
uniform, diagonal sash, shoulder epaulette, stars, medals, and glove/hand details.
The raw and native results preserve the same face geometry, gaze, moustache, pose,
uniform silhouette, sash, epaulette, and source decoration layout. The source is
grayscale, so the muted red/ivory sash and metal colour are necessarily painted
interpretations; this is a documented small simplification and not, on visual
inspection, an invented insignia or identity-changing uniform replacement.

The output has a quiet charcoal painted background, modeled skin and uniform, and
deliberate brush marks visible at both full and native resolution. It is clearly
HOI4-painted and role-appropriate for a formal crown/council leader. If a later
review identifies an extra order, star, or changed sash geometry, fail closed and
reject the row rather than treating colorization as permission to invent regalia.

### Luigi Rizzo

The source is a 1935 Regia Marina rear-admiral portrait: broad square face,
swept-back dark hair, heavy brows, thick moustache, direct gaze, stern calm
expression, black dress uniform, white shoulder cords, diagonal sash, medals, and
crosses. The raw and native results preserve all of those identity and role cues.
Medal and cross colors are restrained interpretations of the source-backed shapes;
no extra badge, modern prop, replacement uniform, or changed silhouette is visible.

The blue-gray background and controlled brushwork match the intended full
commander treatment and the native texture remains legibly painted beside
`generic_africa_navy_2.png`. This is a visual/provenance pass. The parent must
decide whether the existing `corps_commander`/`army = large` consumer is the
intended Event 006 role; this audit does not authorize a new navy-leader or
advisor/miniature consumer.

## Source provenance, rights, and identity evidence

### Sturzo

- Source page: [Wikimedia Commons, `1925 Luigi Sturzo`](https://commons.wikimedia.org/wiki/File:1925_Luigi_Sturzo.jpg).
- Direct master: [Albert Kahn image](https://collections.albert-kahn.hauts-de-seine.fr/media/cache/big/61/64/6164609751e082079310c926.jpeg).
- Collection record: [Don Luigi Sturzo](https://collections.albert-kahn.hauts-de-seine.fr/document/proprit-d-albert-kahn-boulogne-france-don-luigi-sturzo/617a7a45cf8b8968b338626f?filtrerParThme%5B0%5D=Personnalit%C3%A9&filtrerParDomaine%5B0%5D=Images%20fixes&s=dateDePriseDeVue&so=desc&pos=3482&pgn=231).
- Independent fetch on 2026-07-22 matched the local direct master hash,
  `1519x2048`, 554,180 bytes. The collection page identifies Don Luigi Sturzo,
  Georges Chevalier as operator, 4 April 1925, autochrome process, and states
  `Librement réutilisable (CC-BY-4.0)`. Commons describes the same source as a
  1925 autochrome and repeats CC BY 4.0.
- Release condition: retain attribution to Georges Chevalier/Albert Kahn, link
  the CC BY 4.0 license and source record, and state that the portrait was
  cropped and converted to a painted HOI4-style derivative.

### Pietro Lanza di Scalea

- Source page: [Wikimedia Commons, `Pietro Lanza di Scalea by Mario Nunes Vais`](https://commons.wikimedia.org/wiki/File:Pietro_Lanza_di_Scalea_by_Mario_Nunes_Vais.jpg).
- Direct master: [Commons original](https://upload.wikimedia.org/wikipedia/commons/4/43/Pietro_Lanza_di_Scalea_by_Mario_Nunes_Vais.jpg).
- Commons identifies the ICCD Fondo Nunes Vais collection, Mario Nunes Vais
  (1856–1932), and a date before 1932. The page carries PD-old/PD-US/PDM marks.
- Independent fetch matched the local master hash, `602x800`, 77,019 bytes. The
  portrait is a face-visible formal court-uniform source and fits the role/era.
  Preserve source credit and the Commons public-domain caveat in durable docs.

### Luigi Rizzo

- Source page: [Wikimedia Commons, `Rear Admiral Luigi Rizzo in 1935`](https://commons.wikimedia.org/wiki/File:Rear_Admiral_Luigi_Rizzo_in_1935.jpg).
- Direct master: [Commons original](https://upload.wikimedia.org/wikipedia/commons/b/b0/Rear_Admiral_Luigi_Rizzo_in_1935.jpg).
- Role corroboration: [Italian Navy biography](https://www.marina.difesa.it/cosa-facciamo/storia/la-nostra-storia/medaglie/Pagine/RizzoLuigi.aspx).
- Commons identifies Luigi Rizzo (1887–1951) in Regia Marina rear-admiral
  uniform, sourced from *Medaglie d'oro della Grande Guerra* (Rome, 1935), with
  photographer unknown. The page states PD-Italy and PD-1996/US bases. An
  independent fetch matched the local master hash, `402x582`, 125,508 bytes.
  The Italian Navy page independently identifies Rizzo as born in Milazzo on
  8 October 1887 and a decorated naval officer, supporting Sicilian role fit.

## Subject-ownership search

The exact and variant terms searched were `Sturzo`, `luigi_sturzo`, `Don Luigi
Sturzo`, `Lanza di Scalea`, `Lanza_di_Scalea`, `Scalea`, `Luigi Rizzo`, and
`luigi_rizzo`. The searched ownership roots were character definitions, country
histories/recruitment, leader/commander portrait files, `.gfx`/interface
consumers, and localisation.

### Installed vanilla

- No exact Sturzo, Lanza di Scalea, or Rizzo character, country-history
  recruitment, leader/commander portrait, or `.gfx`/interface consumer was
  found in `common/characters/`, `history/countries/`, `gfx/leaders/`,
  `interface/`, or `localisation/`.
- The only vanilla Rizzo hits are incidental ship production names at
  `common/national_focus/italy.txt:7862` and `:7938` (`name = "Luigi Rizzo"`).
  These are not character or portrait ownership.

### Current Chaos Redux

The only active runtime owner is the intended ASX package:

- `common/characters/006_independence_wave_mediterranean_characters.txt:157-184`
  defines the three ASX character tokens and male metadata.
- `history/countries/ASX - Sicily.txt:17-21` recruits the three tokens.
- `interface/006_independence_wave_mediterranean_portraits.gfx:33-43`
  consumes the three stable full-portrait sprite names.
- No duplicate Chaos Redux character/portrait owner or opposite-gender metadata
  was found. The current runtime DDS files are older treatment bytes and are not
  the trial package: runtime hashes are Sturzo `bdd4fe08090a8dd3a2ac464add432dc3a4c60d1f7fa0dcd5d834bfea511e67c0`,
  Scalea `a067f230ef233e5c6314959f9f0904e6d5c036f2d284bef9a44d6eb2a5a3be01`,
  and Rizzo `2348b811cc46f2ff8d7cbb0a7d0a66865205cd57d526903cbc159ae1aaa9dea5`.
  They must not be treated as this audit's accepted outputs.

### Approved reference mods

Reference-mod hits were checked but do not create a Chaos Redux runtime
collision; these mods are not dependencies of the current package and no image
was copied from them:

- Kaiserreich (`1521695605`) actively defines/recruits and portrait-owns
  `SIC_luigi_sturzo` at `common/characters/SIC characters.txt:322-332`,
  `history/countries/SIC - Two Sicilies.txt:146`, and
  `interface/kaiserreich/portraits/SIC_portraits.gfx:99-100`.
- Kaiserreich actively defines/recruits and portrait-owns `SRI_luigi_rizzo` at
  `common/characters/SRI characters.txt:1247-1267`,
  `history/countries/SRI - Socialist Republic of Italy.txt:308`, and
  `interface/kaiserreich/portraits/SRI_portraits.gfx:371-376`.
- No exact Sturzo, Scalea, or Rizzo character/portrait owner was found in Old
  World Blues (`2265420196`).
- Cold War Iron Curtain (`1458561226`) has only an incidental ship name
  `Luigi Rizzo (F-596)` at `history/units/ITA_1980_naval_mtg.txt:44`; no person
  character or portrait consumer was found.

These reference-mod uses are recorded as an identity/art caution only. They are
not a global exclusivity claim about historical people and do not block the ASX
package under the current vanilla/Chaos Redux ownership gate.

## Canonical HOI4 reference and offline-rule evidence

Read before review:

- `.agents/skills/chaos-redux-event-assets/SKILL.md` in full, including the
  grounded portrait source-mode gate, real-person edit sequence, subject
  ownership gate, canonical reference routing, and full `156x210` requirement.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
  and `CATALOG.md`.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/README.md`
  and `REFERENCE_MANIFEST.md`.
- `paradox_wiki/Portrait modding - Hearts of Iron 4 Wiki.md` (portraits are
  normally `156x210`; army/navy pools are role-specific).
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` (the
  `.gfx` `spriteType` binds a stable name to a texture path).

The matching role references were inspected at native canvas and through both
contact sheets:

- Country-leader style: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/den_thorvald_stauning.png`,
  SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`.
- Navy-commander style: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/generic_africa_navy_2.png`,
  SHA-256 `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f`.
- The complete canonical leader and commander contact sheets were also viewed;
  all references are full `156x210` painted textures. The Sicily results are
  somewhat darker and more impasto-textured than the pale reference backdrops,
  but retain the modeled face, restrained palette, readable silhouette, and
  unmistakably painted HOI4 treatment at both full and native resolution.

## Parent wiring handoff and remaining risks

After accepting this handoff, the parent may promote the three package DDS files
to the already registered runtime paths, preserving stable sprite names:

- `final_dds/ASX_luigi_sturzo.dds` ->
  `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_sturzo.dds`
- `final_dds/ASX_pietro_lanza_di_scalea.dds` ->
  `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds`
- `final_dds/ASX_luigi_rizzo.dds` ->
  `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds`

No new `.gfx` names, `_small` files, advisor cards, or gameplay/localisation
changes are authorized by this audit. Preserve the existing male metadata and
the source-attribution/change notes, and do not treat the current older runtime
DDS hashes as accepted outputs. For Rizzo, retain the explicit parent decision
whether the rear-admiral visual is intentionally used by the current ASX corps
commander/army portrait consumer; a separate navy-leader role would require a
gameplay/character audit outside this handoff.

No simplification, substitute, generated identity, invented person, or asset copy
from a reference mod was used. The only noted visual simplifications are the
normal painted rendering/colorization of source-backed uniform decorations for
Lanza di Scalea and Rizzo; neither showed an identity-changing insignia or
uniform replacement. Rights attribution remains a release obligation for
Sturzo's CC BY 4.0 source.

