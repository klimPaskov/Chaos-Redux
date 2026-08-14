# Event 006 IW-038 Ruthenia portrait source-placeholder handoff

Date: 2026-08-10.

Owner: `chaosx_portrait_creator`.

## Handoff result

Four grounded male full-size portrait consumers are prepared for parent review: the existing vanilla `RUT_augustin_voloshyn` with a parent-owned Event 006 scoped override, plus `RUT_independence_wave_andriy_brodiy`, `RUT_independence_wave_ivan_mondok`, and `RUT_independence_wave_dmytro_klympush`. No duplicate Augustin character token was created.

All four packages contain an unchanged attributed source master, an immutable source crop with exact-pixel JSON evidence, a deterministic RGB `156x210` candidate, a `624x840` nearest-neighbour review, a `131168`-byte one-level BGRA DDS, and portrait-specific GFX registration. Runtime consumers must use `gfx/leaders/006_independence_wave/*.dds` and the sprites in `interface/006_independence_wave_iw038_ruthenia_portraits.gfx`; they must never point into `docs/assets/portraits/`.

The portrait worker did not edit character identity, traits, ideology, localisation, country setup, route logic, decisions, focuses, parties, AI, events, advisors, dossier portraits, small portraits, or gameplay files. The country-core owner must apply the three new character definitions, portrait assignments, and localisation using the exact stable tokens below.

## Stable consumers and source gates

| Consumer | Role fit in 1936 | Source package | Runtime sprite | Rights / admission |
| --- | --- | --- | --- | --- |
| Existing `RUT_augustin_voloshyn` | Civic, constitutional, clerical-traditional anchor; Voloshyn was alive in 1936 | `docs/assets/portraits/006_independence_wave/iw038_rut_augustin_voloshyn_source_placeholder_2026_08_10/` | `GFX_portrait_RUT_independence_wave_augustin_voloshyn` | `PASS_WITH_CAVEAT`; Commons PD mark but unknown photographer/first publication and no US-specific tag |
| `RUT_independence_wave_andriy_brodiy` | Agrarian/autonomist traditional route; Brodiy led the Autonomous Agricultural Union and represented Subcarpathian Rus | `docs/assets/portraits/006_independence_wave/iw038_rut_andriy_brodiy_source_placeholder_2026_08_10/` | `GFX_portrait_RUT_independence_wave_andriy_brodiy` | `PASS_WITH_CAVEAT`; Commons PD mark and circa-1930–40 source but unknown photographer/first publication and no US-specific tag |
| `RUT_independence_wave_ivan_mondok` | Socialist route; Mondok was a Carpatho-Ruthenian communist organizer and Czechoslovak deputy, alive in 1936 | `docs/assets/portraits/006_independence_wave/iw038_rut_ivan_mondok_source_placeholder_2026_08_10/` | `GFX_portrait_RUT_independence_wave_ivan_mondok` | `PASS`; anonymous 1926 National Assembly source, `PD-anon-70-EU`, pre-1929 US publication basis, National Library Kramerius credit |
| `RUT_independence_wave_dmytro_klympush` | Emergency mountain-border route and full corps command; Klympush later commanded Carpathian Sich, with pre-command background in 1936 | `docs/assets/portraits/006_independence_wave/iw038_rut_dmytro_klympush_source_placeholder_2026_08_10/` | `GFX_portrait_RUT_independence_wave_dmytro_klympush` | `PASS_WITH_CAVEAT`; Commons `PD-Ukraine (1930s works)` and named biographical credit, but unknown photographer/first publication and no US-specific tag; native source is only `157x211` |

The exact rights dispositions are explicit: Mondok is `PASS`; Voloshyn, Brodiy, and Klympush are `PASS_WITH_CAVEAT` because the source pages preserve public-domain records but omit photographer/first-publication or US-specific detail. If the parent review rejects a caveat, keep that consumer blocked and do not substitute a different person or generated image.

## Source evidence

### Augustin Voloshyn

Source page: [Wikimedia Commons — Волошин Августин.jpg](https://commons.wikimedia.org/wiki/File:%D0%92%D0%BE%D0%BB%D0%BE%D1%88%D0%B8%D0%BD_%D0%90%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B8%D0%BD.jpg).

Original binary: `https://upload.wikimedia.org/wikipedia/commons/8/8c/%D0%92%D0%BB%D0%BE%D1%88%D0%B8%D0%BD_%D0%90%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B8%D0%BD.jpg`.

Credit: [Cegolnya parish biography](http://cegolnya.uz.ua/?page_id=1687); the [2014 Wayback snapshot](https://web.archive.org/web/20140113235228id_/http://cegolnya.uz.ua/?page_id=1687) identifies Voloshyn and reproduces the same photograph. Commons records `PD Old`, `CC-PD-Mark`, and public-domain usage, but no named photographer, first publication, or US-specific tag.

Identity and role reference: the archived biography identifies Voloshyn as a priest, educator, Czechoslovak parliamentarian, and later head of Carpathian Ukraine; he was alive throughout 1936.

Master: RGB `3152x4016`, 1,578,614 bytes, SHA-256 `aa697c70054f791d91a3fb07c576c52dffeaecc6d4739b69a2a0bada58137ca8`.

Crop: `[83,0,3068,4016]`, RGB `2985x4016`, SHA-256 `353c4219949bf47bf3bcff8a87b485e93abf34c0de116813b0d67157752fb764`, RGBA equality SHA-256 `86981548b622983291df0c94f41bc2c46ebc6300ab51f444fae7234d89259635`.

Candidate: `portrait_RUT_augustin_voloshyn.png`, `156x210`, SHA-256 `c673dc85f05f7e564c7631900489159935e9f437066aef3dec00cc0872caeb23`.

DDS: `gfx/leaders/006_independence_wave/portrait_RUT_augustin_voloshyn.dds`, 131,168 bytes, SHA-256 `d3c1aced2343465b679deacfae1692ab721803f8e63b5468ac3cb7bf92530ec6`; DDS decode is pixel-identical to the candidate.

### Andriy Brodiy

Source page: [Wikimedia Commons — Brodij A.jpg](https://commons.wikimedia.org/wiki/File:Brodij_A.jpg).

Original binary: `https://upload.wikimedia.org/wikipedia/commons/8/86/Brodij_A.jpg`.

Credit: [Institute of History of Ukraine encyclopedia entry](http://www.history.org.ua/?l=EHU&verbvar=Brodij_A&abcvar=2&bbcvar=20). Commons dates the image circa 1930–1940, identifies the photographer only as `Фотограф`, and applies `PD Old` and `CC-PD-Mark`. The [Ukrainian biography](https://uk.wikipedia.org/wiki/%D0%91%D1%80%D0%BE%D0%B4%D1%96%D0%B9_%D0%90%D0%BD%D0%B4%D1%80%D1%96%D0%B9_%D0%86%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87) identifies Brodiy as an agrarian-union leader, autonomist, journalist, and Czechoslovak parliamentarian; he was alive in 1936.

Master: grayscale `760x1061`, 141,412 bytes, SHA-256 `cef5bf6d305d3393240392fb672eae59ab28b29b0d34b4f265947643d2bbb2d2`.

Crop: `[0,0,760,1023]`, grayscale `760x1023`, SHA-256 `1b8609ccb7633ecd55e69448f093307f4614d274d210043afe538273d1fc6583`, RGBA equality SHA-256 `357d1faf640c77fa4c64f3265a13c3ab76b3f2ab94d67168e83f5aa150b99e9a`.

Candidate: `portrait_RUT_independence_wave_andriy_brodiy.png`, `156x210`, SHA-256 `fc7393aceb37fa8215d81180a9673abb3aff2209dee2ce85646fcc17766b63d4`.

DDS: `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_andriy_brodiy.dds`, 131,168 bytes, SHA-256 `b0aaf6c848d48435ecde5ae568a825e5b736a89225d912c7e08d25595ef2f664`; DDS decode is pixel-identical to the candidate.

### Ivan Mondok

Source page: [Wikimedia Commons — Mondok Ivan, Poslanecká sněmovna v II. volebním období 1926.jpg](https://commons.wikimedia.org/wiki/File:Mondok_Ivan,_Poslaneck%C3%A1_sn%C4%9Bmovna_v_II._volebním_období_1926.jpg).

Original binary: `https://upload.wikimedia.org/wikipedia/commons/a/a1/Mondok_Ivan%2C_Poslaneck%C3%A1_sněmovna_v_II._volebním_období_1926.jpg`.

Credit: *Československo. Poslanecká sněmovna v II. volebním období 1926*, p. 137, with a [National Library of the Czech Republic Kramerius copy](https://kramerius5.nkp.cz/uuid/uuid:c3a44520-db1f-11e5-9f76-5ef3fc9bb22f). The anonymous 1926 publication is tagged `PD-anon-70-EU`; 1926 is before the United States 1929 publication cutoff. The [Ivan Mondok biography](https://en.wikipedia.org/wiki/Ivan_Mondok) identifies him as a Carpatho-Ukrainian communist organiser and Czechoslovak deputy; the Commons caption gives 1893–1937 while the English biography gives 1893–1941, both after the 1936 start.

Master: RGB `346x436`, 122,320 bytes, SHA-256 `1aa8dc1514a63ce285196e84bcfa700521e48762c707bc8424b039ab1d4efd6a`.

Crop: `[13,0,334,432]`, RGB `321x432`, SHA-256 `767fab8dd497d80c52b1bfa6a919dcc9dfa0e0da8fbac33575856e617e4e4eeb`, RGBA equality SHA-256 `984cf3c3c778e3d0834924d0b9ccacbc43abc3c40a2987325f57cda90bb35ae9`.

Candidate: `portrait_RUT_independence_wave_ivan_mondok.png`, `156x210`, SHA-256 `772c146e5db1b24f59ee7076019bb0d17bb74747f13487d8047de54423afb2b3`.

DDS: `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_ivan_mondok.dds`, 131,168 bytes, SHA-256 `7157e1df41bcefe1318c0b93080b6a7967abf93d69e28d82c3f146c29f1a2ce9`; DDS decode is pixel-identical to the candidate.

### Dmytro Klympush

Source page: [Wikimedia Commons — Klympush Dmytro.jpg](https://commons.wikimedia.org/wiki/File:Klympush_Dmytro.jpg).

Original binary: `https://upload.wikimedia.org/wikipedia/commons/b/b4/Klympush_Dmytro.jpg`.

Credit: [Transcarpathia Tour biographical page](http://www.transcarpathiatour.com.ua/library/persons/persons_klimpush_ua.html). Commons describes Klympush as commander of the Carpathian Sich (1938–1939), applies `PD-Ukraine (1930s works)`, and records no named photographer. The [Ukrainian biography](https://uk.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D0%BC%D0%BF%D1%83%D1%88_%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%BE_%D0%86%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87) records his pre-1938 military, Sich, and regional-organising background and confirms he was alive in 1936.

Master: RGB `157x211`, 11,991 bytes, SHA-256 `d9cd50424efa105918c5118db7fe886994734d073c40d078336bbe837dfc71be`.

Crop: `[0,0,157,211]`, RGB `157x211`, SHA-256 `86f668096af1099abf9685d62c73a46f57dda9e2f75544f90611397641894308`, RGBA equality SHA-256 `f85a084fb44223b65fb446fb52386c847c91c9100f1c9f08e117791f2c62eaeb`.

Candidate: `portrait_RUT_independence_wave_dmytro_klympush.png`, `156x210`, SHA-256 `b1ce6d618c073e0f84d77afaa0585088a243ac3ee3014680e4a33a7132f2d854`.

DDS: `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_dmytro_klympush.dds`, 131,168 bytes, SHA-256 `07c24f7f0ee26740ca17b99137e9e1ce654148e13f95e9e9b287e81ae0476b5a`; DDS decode is pixel-identical to the candidate.

## Parent-owned wiring requirements

Use `GFX_portrait_RUT_independence_wave_augustin_voloshyn` only for the existing vanilla `RUT_augustin_voloshyn` character and apply it through the Event 006 scoped override. Define the other three consumers with exactly `RUT_independence_wave_andriy_brodiy`, `RUT_independence_wave_ivan_mondok`, and `RUT_independence_wave_dmytro_klympush`, pointing their full country-leader/corps-commander portrait field at the corresponding sprites. Keep all portrait surfaces at `156x210`; do not add advisor, high-command, dossier, commander-small, mini, female, or alternate portraits.

## Changed files and checks

Changed portrait-specific files:

- `interface/006_independence_wave_iw038_ruthenia_portraits.gfx`.
- `gfx/leaders/006_independence_wave/portrait_RUT_augustin_voloshyn.dds`.
- `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_andriy_brodiy.dds`.
- `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_ivan_mondok.dds`.
- `gfx/leaders/006_independence_wave/portrait_RUT_independence_wave_dmytro_klympush.dds`.
- Four durable source packages under `docs/assets/portraits/006_independence_wave/iw038_rut_*_source_placeholder_2026_08_10/`, each with source master, crop PNG/JSON, processed candidate, 4x review, processing JSON, DDS copy, `manifest.md`, `gfx_handoff.md`, and `source_provenance.json`.

Checks completed:

- All four masters were visually inspected before crop; all subjects are real men and role/date fit was reviewed against cited biographical sources.
- All four crop JSON records report `status: exact_source_crop_verified` and matching decoded master/crop RGBA hashes.
- All four candidates are RGB `156x210`; all four DDS files are `131168` bytes with valid `DDS ` headers, one BGRA mip level, opaque alpha, and pixel-identical decoded payloads.
- The installed-vanilla leader and commander contact sheets were inspected as canonical `156x210` framing/style references.
- Source provenance JSON files parse successfully.

Skipped by scope: no RunPod, no ImageGen, no fictional person, no gameplay or localisation edits, no character-definition edits, no advisors, no small portraits, no live-game launch or validation.

## Remaining blockers and simplifications

Voloshyn, Brodiy, and Klympush are `PASS_WITH_CAVEAT`, not unconditional passes, because Commons does not state a named photographer, first publication, or United States-specific tag. The source pixels and exact archive credits are preserved; if parent review cannot accept a caveat, block that consumer rather than substituting a different person. Klympush is also a native `157x211` source and therefore has limited detail, although it converts cleanly to the required `156x210` canvas.

No fictional or generic fallback was used. Mondok is the recommended socialist route candidate because the previously considered Ivan Lokota had no attributable portrait source; no monument, postwar artwork, or generic face was substituted.
