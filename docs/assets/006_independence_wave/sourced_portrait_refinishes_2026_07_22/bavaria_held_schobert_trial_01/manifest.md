# IW-009 Bavaria sourced portrait refinishes — trial 01

Date: `2026-07-22`  
Scope: exactly two grounded, real male identities for Event 006 IW-009 Bavaria.  
Status: both candidates are `needs_independent_review`; no runtime DDS, GFX, gameplay, localisation, character, or protected-file wiring was changed.

This temporary evidence package keeps the two unchanged source masters, exact
head-and-shoulders crops, raw built-in ImageGen edit masters, prompts, native
`156x210` processed PNGs, docs-only DDS conversions, metadata, hashes, and
source/crop/result/canonical contact sheets. The docs-only DDS files are not
engine-facing assets and must not be copied into `gfx/leaders/` until an
independent reviewer approves both identity and visual finish.

## Current gate reconciliation

On `2026-07-24`, the current exact-pixel crop utility re-extracted Heinrich Held's documented rectangle `(400,160)-(2070,2409)` from the unchanged archival master into the already retained crop path.
The re-extracted PNG is byte-identical to the reviewed crop at SHA-256 `11841151745e97e7398bef3c60481C0BFEEFABA2B2D8225F3E3466D78F75CF3A`.
The new `crops/BAY_heinrich_held_crop_400_160_2070_2409.json` records `decoded_pixels_equal = true`, matching RGBA hashes for the decoded master rectangle and output, the normalized utility invocation, Pillow version, master hash, crop coordinates, and output hash.
This closes the current explicit-crop evidence requirement without changing the ImageGen identity input or reviewed result.
The independent audit passes Heinrich Held's likeness, HOI4 leader style, male grounded identity, period role, and provenance; only parent runtime promotion remains.
Eugen Ritter von Schobert remains blocked on source rights and must not be promoted from this package.

## Source-mode and identity gate

Bavaria is a grounded historical polity. Both rows therefore use attributed
real-person source material and the only permitted generative step: an
identity-preserving edit of the unchanged exact source crop. The canonical
male leader/commander PNGs are style-only references; no canonical person,
face, clothing, or prop was copied or used as an identity substitute. No
generated person, generic face, female subject, second person, advisor card,
commander `_small`, flag, or fallback was created.

## Candidate ledger

| Asset / role | Source and rights | Exact crop | ImageGen edit / finish | Processed + docs DDS | Sprite / runtime target | Status / uncertainty |
|---|---|---|---|---|---|---|
| Heinrich Held — civic country leader | NAC/Agencja Keystone View Company; Commons file [Heinrich Held, 1933](https://commons.wikimedia.org/wiki/File:Heinrich_Held,_1933.jpg), direct archive record [NAC object 473188](https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6270998/obiekty/473188), direct upload [original JPG](https://upload.wikimedia.org/wikipedia/commons/0/03/Heinrich_Held%2C_1933.jpg); circa 1 Jan 1933; Commons records CC0 1.0. Unchanged local copy: `source_masters/BAY_heinrich_held_keystone_1933.jpg`, `2471x3623`, SHA-256 `35d1ee399c8c86efd024e8226a8effe97afc5fc0114c4a1186ad9cd4d6c3560d`. | Exact source pixels `(400,160)-(2070,2409)`; `1670x2249`; `crops/BAY_heinrich_held_crop_400_160_2070_2409.png`; SHA-256 `11841151745e97e7398bef3c60481c0bfeefaba2b2d8225f3e3466d78f75cf3a`. NAC band is below crop and absent from identity input. | Built-in ImageGen identity-preserving edit; exact crop was Image 1/sole identity input; Stauning and de Valera were style-only references; prompt `prompts/BAY_heinrich_held_prompt.md`; raw `raw_imagegen_masters/BAY_heinrich_held_refinish_raw.png` (`1082x1454`, SHA-256 `2ea1a1b30d0734d30d5306343eb8fee0648c103558f621f1f4119865e790de48`). | `processed_png/BAY_heinrich_held_refinish_156x210.png`, SHA-256 `b2b5854d393020a3db5b7a0767f73244581f6f8a54b99149f33ce47b7321164d`; docs-only `docs_dds/BAY_heinrich_held_refinish_156x210.dds`, SHA-256 `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95`. | `GFX_portrait_BAY_independence_wave_state_council`; deferred runtime target `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds`; target `.gfx`: `interface/006_independence_wave_region_01_portraits.gfx`. | `needs_independent_review`. Held was Bavaria's Minister-President 1924–1933, alive in 1936; source is period-close and role-exact. Independent reviewer must verify likeness, painted finish, and archive-side reuse terms despite Commons CC0 record. |
| Eugen Ritter von Schobert — army/corps commander | NAC catalogue/info `2-12702`; Commons file [Eugen von Schobert](https://commons.wikimedia.org/wiki/File:Eugen_von_Schobert.jpg), [NAC record](https://www.audiovis.nac.gov.pl/obraz/2-12702/), [direct original JPG](https://upload.wikimedia.org/wikipedia/commons/d/d3/Eugen_von_Schobert.jpg); July 1940; author unknown; Commons records NAC free-use statement and Poland/US public-domain rationale. Unchanged local copy: `source_masters/BAY_eugen_von_schobert_nac_1940.jpg`, `2315x3520`, SHA-256 `0512bb979b5bac234eac4c0c61f397664ba97e64cf1626ec95aa05d6d99e7f83`. | Explicit source crop `(170,100)-(2145,2760)`; `1975x2660`; `crops/BAY_eugen_von_schobert_crop_170_100_2145_2760.png`; SHA-256 `9189ea5b8971b74f795d40e665025945e530197532286ec3f0b187a461d461a9`. Crop retains swept hair, moustache, collar embroidery, visible decorations, and upper tunic silhouette. | Built-in ImageGen identity-preserving edit; exact crop was Image 1/sole identity input; generic Africa land commander references were style-only; prompt `prompts/BAY_eugen_von_schobert_prompt.md`; raw `raw_imagegen_masters/BAY_eugen_von_schobert_refinish_raw.png` (`1080x1456`, SHA-256 `d941289dba8eebb34419484d0483351e6d2a1066d835ace294ca2d21a1f8818c`). | `processed_png/BAY_eugen_von_schobert_refinish_156x210.png`, SHA-256 `67ea312d6dccdb1a1dbdf2d94035f73816da179eb942ff34d76bbdca65f3063f`; docs-only `docs_dds/BAY_eugen_von_schobert_refinish_156x210.dds`, SHA-256 `d2c9432e7918fca4f43d51c11b108ffeb65f5dd1aaad440123a49a0e22f66381`. | `GFX_portrait_BAY_independence_wave_mountain_commandant`; deferred runtime target `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`; target `.gfx`: `interface/006_independence_wave_region_01_portraits.gfx`. | `needs_independent_review`. Schobert was born in Würzburg, entered the Royal Bavarian Army, commanded Bavarian infantry formations, and was alive in 1936. The source is later (1940) but period-matching. Commons requests first-publication evidence for its US public-domain analysis; the role is infantry rather than specialist mountain command, recorded as an abstraction caveat. |

Detailed machine-readable records are in `metadata/BAY_heinrich_held_refinish.json`
and `metadata/BAY_eugen_von_schobert_refinish.json`. Binary hashes are in
`hashes/asset_sha256.txt`.

## Ownership gate evidence

On `2026-07-22`, exact, title, underscore, transliteration, and name-order
variants were searched case-insensitively in both installed vanilla and the
current Chaos Redux roots:

```text
common/characters
history/countries
common/country_leader
interface
gfx/leaders
localisation/english
```

Held terms: `Heinrich Held`, `Heinrich_Held`, `heinrich_held`, `Held, Heinrich`.  
Schobert terms: `Eugen von Schobert`, `Eugen Ritter von Schobert`,
`Eugen_Schobert`, `Eugen_von_Schobert`, `eugen_ritter_von_schobert`,
`eugen_von_schobert`, `Eugen Siegfried Erich`.

Installed vanilla returned no identity, character, recruitment, portrait, or
localisation hits for either person. Current Chaos Redux returned no source
identity character/portrait owner; the only matches are the intended Event 006
generated-character tokens, their stable GFX sprites, and their display-name
localisation rows. No existing-character transfer guard is applicable because
no origin character exists. This scan is bounded evidence, not a runtime claim.

## Visual review evidence

`contact_sheets/BAY_held_schobert_source_crop_result_canonical_contact_sheet.png`
shows source-master fit preview, exact source crop, raw ImageGen master,
processed native portrait, and two canonical style references for each role.
The matching `..._4x.png` sheet provides nearest-neighbour enlargement for
face, edge, brush, clothing, and silhouette inspection. The final PNGs are
native `156x210` RGB portraits; DDS conversion is legacy uncompressed BGRA32,
one level, with exact byte/pixel equality to each processed PNG (see handoff).

Both candidates remain `needs_independent_review`: the producing agent may not
approve its own likeness or HOI4-style finish. A reviewer should explicitly
check source-to-result identity, apparent age, face geometry, pose, clothing
and source-visible details, canonical family fit, non-photographic painted
finish, and the rights/role caveats above.

## Protected file check

The package did not copy or edit the protected Rupprecht runtime portrait.
At generation time:

```text
gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds
SHA-256 7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B
```

## No wiring / no fallback

No runtime DDS or `.gfx` file was edited. No localisation or gameplay file was
edited. No fallback, generated substitute, generic identity, advisor/dossier
art, `_small` texture, or flag was added. The main agent may wire only an
independently approved processed PNG/DDS, preserving the existing stable sprite
names and runtime target paths in `gfx_handoff.md`.
