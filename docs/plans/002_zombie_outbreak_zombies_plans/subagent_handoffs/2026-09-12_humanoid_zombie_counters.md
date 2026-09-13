# Humanoid zombie counter companion handoff

Date: 2026-09-12.

Status: `needs_user_review` for the four standard packages and the two shared-model variant audits. The standard frame-1 plate and ink corrections are complete, and both variant repairs are complete as package evidence. No runtime or shared GFX files were edited; the parent owns promotion and wiring.

This handoff covers the four existing `002_zombie_outbreak` humanoid subunits `zombies`, `infected_zombies`, `rabid_zombies`, and `undead_zombies`, plus the parent-authorized `armored_undead_zombies` and `wendigo_zombies` counter audits.

## Review sheets

These are the exact native-size DDS-decoded neutral-matte contact sheets for parent visual review:

- `docs/assets/002_zombie_outbreak/models_3d/zombies/counters/contact_sheet.png`
- `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/counters/contact_sheet.png`
- `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/counters/contact_sheet.png`
- `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/counters/contact_sheet.png`
- `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/counters/armored_variant/contact_sheet.png`
- `docs/assets/002_zombie_outbreak/models_3d/zombies/counters/wendigo_variant/contact_sheet.png`

The standard sheets show source, processed, and exact DDS round-trip rows. The variant sheets compare the copied current runtime DDS decode against the package candidate DDS decode. The installed-vanilla frame-1 comparison at native and enlarged scales is `docs/assets/002_zombie_outbreak/models_3d/zombies/counters/frame1_vanilla_comparison.png`.

## Standard four packages

Each standard package is under `docs/assets/002_zombie_outbreak/models_3d/<slug>/counters/` and retains its native ImageGen source, processed PNGs, final candidate DDS files, decoded round trips, manifest, prompt, validation, plate and ink repair proof, and SHA-256 ledger.

| Unit | Large source -> processed -> candidate DDS | Small source -> processed -> candidate DDS |
| --- | --- | --- |
| `zombies` | `large/source/zombies_icon_source.png` -> `large/processed/zombies_icon.png` -> `large/zombies_icon.dds` | `small/source/onmap_unit_zombies_icon_source.png` -> `small/processed/onmap_unit_zombies_icon.png` -> `small/onmap_unit_zombies_icon.dds` |
| `infected_zombies` | `large/source/unit_infected_zombies_icon_source.png` -> `large/processed/unit_infected_zombies_icon.png` -> `large/unit_infected_zombies_icon.dds` | `small/source/onmap_unit_infected_zombies_icon_source.png` -> `small/processed/onmap_unit_infected_zombies_icon.png` -> `small/onmap_unit_infected_zombies_icon.dds` |
| `rabid_zombies` | `large/source/unit_rabid_zombies_icon_source.png` -> `large/processed/unit_rabid_zombies_icon.png` -> `large/unit_rabid_zombies_icon.dds` | `small/source/onmap_unit_rabid_zombies_icon_source.png` -> `small/processed/onmap_unit_rabid_zombies_icon.png` -> `small/onmap_unit_rabid_zombies_icon.dds` |
| `undead_zombies` | `large/source/unit_undead_zombies_icon_source.png` -> `large/processed/unit_undead_zombies_icon.png` -> `large/unit_undead_zombies_icon.dds` | `small/source/onmap_unit_undead_zombies_icon_source.png` -> `small/processed/onmap_unit_undead_zombies_icon.png` -> `small/onmap_unit_undead_zombies_icon.dds` |

The existing consumers are `GFX_unit_<slug>_icon_medium` for the large strip and `GFX_unit_<slug>_icon_medium_white` for the small strip, as defined by the parent-owned `interface/chaosx_subuniticons.gfx` entries. The proposed runtime destinations are `gfx/interface/counters/divisions_large/` and `gfx/interface/counters/divisions_small/` with the basenames shown above.

Large candidate DDS files are 152x42 canvases containing two adjacent 76x42 frames in `normal`, `alternate_schematic` order. Small candidate DDS files are 60x12 canvases containing two adjacent 30x12 frames in the same order. Frame 0 remains the unit-specific normal identity: a compact muted vanilla-green large silhouette or pale grayscale small silhouette. Frame 1 is the separate unit-specific schematic on the inspected opaque pale inactive vanilla plate, with subject ink quantized to three near-black sampled inactive-palette colors for native-size readability.

The parent-requested frame-1 correction first removed the rejected transparent outline/checkerboard presentation and reconstructed the canonical inactive plate from the inspected vanilla reference family. The follow-up correction retained each unit-specific role pose and identity while strengthening only its subject ink to the sampled near-black palette. The native-alpha source PNGs remain byte-identical and were not regenerated for either correction.

### Frame-0 preservation and frame-1 ink proof

Each package `frame1_repair.json` records both the plate repair and the follow-up `ink_strengthening` before/after hashes. The following pairs are equal, proving that the accepted normal frame 0 stayed byte-identical while the final frame 1 changed:

| Unit | Large frame 0 before = after | Small frame 0 before = after | Large final frame 1 | Small final frame 1 | Final role ink luma |
| --- | --- | --- | --- | --- | --- |
| `zombies` | `42853c7b2062497ac42cbb205a8b0e9b33fbf208bdb9c89afc12c480eb40db73` | `cf9d494e492cf3533b3d1534dbcd82de09537b90f96b757c71359bdd5cdf30d8` | `dae6c2e25063488c57c3f2ef188bd8c6ac536145ec2c07c07a47203fd0370a9d` | `043e3ce56906c078cb5edc5d7e74bd93cbe85af9bc2f55ab72a5d224a319eaa6` | large `0-63`; small `64` |
| `infected_zombies` | `617a98868808669ef8d092d8a2f1df950b5581e54294bf7e59794da4089ba000` | `43f85e8eac2c0b021ced9327e5d7e617ee55fe91912dc4d981fa8b9eb69d6bd9` | `7fd09f36953548b83be5991cd7ef9af29704fdb56a255823372db5d2786bd378` | `77b7f454eb871a00b0603d93443767ebe15b693f0ec84b1701cc2f507261638a` | large `0-63`; small `33-64` |
| `rabid_zombies` | `dfa4af57dd818277f3cadaa658a99cf3354eeea3628e7ca399e6a4aba316a0e2` | `2ed0904d6f455913d765143d91a063828f9e5141fc17db3691a6813ba7abc0c3` | `0bb04f20386d0cf536bdf348cf31fb5476f604c8d7a8cd2df1d97106eadfca64` | `d5958d28ee359f07acd4c6731ba766b210018f850bb68407cb26ed0509836749` | large `0-63`; small `0-64` |
| `undead_zombies` | `da5f622dcdf8277f14e7e6454ad0713fc6fb8cba7223e3b4c70b7992105a0605` | `c69b20dfd9540f9d97472fff1b3443d73cfa56b91b24c5c9c0554b2d9280b0bc` | `94891933f6bf1bc0b0abef9d5812a0b10ee36b548651efdb68fd11a71d2a9469` | `fb7f27eb6dca6f551e6bea9bba939ed664935bed5b2b279a173bc0deb03745cf` | large `0-63`; small `33-64` |

The four validators confirmed exact processed-to-DDS pixel equality, strict 152x42 and 60x12 dimensions, one-mip uncompressed BGRA headers, alpha extrema `[0, 255]`, and visible colors inside the corresponding inspected reference palette. The final frame-1 role metrics report no more than 64 luma and three or fewer role colors per size, while the canonical plate remains intact.

The four identity motifs follow the viewed model references: shambling decayed civilian for `zombies`, wet diseased formal civilian for `infected_zombies`, snarling clawing feral for `rabid_zombies`, and gaunt skull-faced tattered formal civilian for `undead_zombies`. All selected ImageGen sources were requested with genuine transparent backgrounds and validated as RGBA PNGs with transparent corners; no background-removal fallback or checkerboard/chroma candidate was processed.

The canonical reference family is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`. The installed reference DDS hashes are large `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23` and small `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`. The sampled large normal anchors are `#496A49`, `#4A6B4A`, `#537253`, and `#648064`.

The repeatable processor is `process_humanoid_counters.py`, the plate correction is `repair_frame1_plate.py`, the near-black correction is `strengthen_frame1_ink.py`, and the validator is `validate_humanoid_counters.py` in the `zombies/counters/` package. The per-package `gfx_handoff.md` files describe the exact source, processed, DDS, round-trip, prompt, manifest, repair, and validation paths.

### Current standard source and candidate DDS hashes

| Unit | Large source | Large candidate DDS | Small source | Small candidate DDS |
| --- | --- | --- | --- | --- |
| `zombies` | `7d17e5cf75bb0dc36390e0f66e4d3887071c06ad00e26fd4f6dd0d99e9acbee8` | `907852de18bb57b16da1ae9b6a48ea67eef64946ebab9aa36fc592ff30a006a0` | `0f656ec6c0e32dc0ba69914a9220b115d55fec443a9ecb6a41a8691d08fe0880` | `5713fa9fb6e415a2a10d490d362b50528103dd242e00fa4cc258f00cb21d6346` |
| `infected_zombies` | `b5cbaa15d56de1912e9e9cfc5d45f88bc5a9a024877404dcad583c4770a3a099` | `f726c876fdfed95b0f9f26ba2ae1ae3e2c15489b059e11c36ee394db84acb675` | `43c28db44e8aefed651da323754be272f080664986af81659894666a08a7b156` | `e022fadfef246853815c20a1d66db72a44649e1583fb55e28b1116eb68a92fa9` |
| `rabid_zombies` | `5e8f126700ea7ac99e2d6355d01e405672b4bce8b5ca1fb47942af0a807db370` | `720aea7ba20a481e9ff0fbb740fbbb13e3f89b44c632bd575da9a14c39530bb4` | `32cf80c338bd86d7e7c2dd003dc202d0e1dc491fafa65c0f5b294c14e250accc` | `0a2f3646b17597a166d808d882da7fbf59fa8bd46ae42e20368a100b0e07d0b1` |
| `undead_zombies` | `6f452f79f45bf9569bd260e030e2110dd4f7cb761464020ed1324e060312ad15` | `02f0a5b6333200c97162ed0442a7cd0c965ef5fd8b639e1f8c97fe5b55e4a1c4` | `72332125bef4af04595bc524f30ad831790d56404a813e39940056d19305982d` | `8562300c6289ff738ae6e64963ffe1ce9dbc9f19c980bb92fadebe32a241dc0d` |

## Armored undead shared-model audit

The parent-authorized audit covers subunit `armored_undead_zombies` in `common/units/zombies.txt`, sprite `chaosx_undead_zombies`, and existing aliases `GFX_unit_armored_undead_zombies_icon_medium` and `GFX_unit_armored_undead_zombies_icon_medium_white`. All evidence is kept under `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/counters/armored_variant/` and no runtime file was written.

The copied current runtime sources are `source/runtime_large_original.dds` for `gfx/interface/counters/divisions_large/unit_armored_undead_zombies_icon.dds`, SHA-256 `6409846e58734fa198ff1d1d6b37863c65fb058fafe16e6f47e66cd0fd1ac291`, and `source/runtime_small_original.dds` for `gfx/interface/counters/divisions_small/onmap_unit_armored_undead_zombies_icon.dds`, SHA-256 `8eafd2bf7b2fb65ea48e0be01e5d5741b4f5db2bcad0302c409da7130e5d3623`. Their decoded source PNGs are retained beside them.

Inspection found the existing frame 0 skull/helmet identity usable, so the final candidate preserves its decoded pixels exactly. Existing frame 1 contained diagonal-stroke debris and jagged edge artifacts. The source containers were DXT1 with mip metadata, unlike the inspected one-mip uncompressed BGRA vanilla family. The package candidate repairs only frame 1 with the original dark skull/formal/steel-helmet/compact-armor role schematic on the canonical opaque pale inactive plate.

| Size | Candidate processed PNG and SHA-256 | Candidate DDS and SHA-256 | Final decoded frame 0 | Final decoded frame 1 |
| --- | --- | --- | --- | --- |
| Large | `large/processed/unit_armored_undead_zombies_icon.png` — `30f8fffed38a564f0e52b008662ba29e4313593a3de53810a562d440db918306` | `large/unit_armored_undead_zombies_icon.dds` — `9c31285d291c9b9d85c328895be063ebe5aef24cf7dacfa917eb3671579d0e1f` | `e83958e7046da612b45a76ab5daa4e9028ce284e2bfb9fcf1f9bc0eed001c7c0` | `4ae477262dbcc95e91bf4312972fd70ba73ce454ce1ad9ae6bd4ff15f8523cd0` |
| Small | `small/processed/onmap_unit_armored_undead_zombies_icon.png` — `2b9505f92cf196c8341943a90582a0f41315f9e42af1d4d1737bc1964e2a52e3` | `small/onmap_unit_armored_undead_zombies_icon.dds` — `e90a559c9ee83968f0e0c61f6f10e458a9289252e3e6daecd5a0ba5fc64bae78` | `61b70b540db444228c9ae66f3e79cfd16388d1d977625799bf41dcb35d8b63dc` | `016a62a2b1b5bf048b62ff8f079f919975933f9fd9b6c7c191a20e0d66519147` |

`armored_repair.json` records the original and final frame hashes and `frame0_pixel_unchanged=true`; `validation.json` records exact PNG-to-DDS round trips, strict dimensions and headers, canonical inactive plate alpha, palette checks, and `runtime_write=false`. The native-alpha generated source is `source/armored_undead_schematic_generated.png`, SHA-256 `0b100954a54fa6388fdb3236e757947d55d214b5861a506266ac96656999bef1`.

## Wendigo shared-consumer audit

The parent-authorized audit covers subunit `wendigo_zombies` in `common/units/zombies.txt`. Its current consumer is `sprite = zombies` with `map_icon_category = armored`, and its existing aliases are `GFX_unit_wendigo_zombies_icon_medium` and `GFX_unit_wendigo_zombies_icon_medium_white`. All evidence is kept under `docs/assets/002_zombie_outbreak/models_3d/zombies/counters/wendigo_variant/` and no runtime file was written.

The copied current runtime sources are `source/runtime_large_original.dds` for `gfx/interface/counters/divisions_large/unit_wendigo_zombies_icon.dds`, SHA-256 `6409846e58734fa198ff1d1d6b37863c65fb058fafe16e6f47e66cd0fd1ac291`, and `source/runtime_small_original.dds` for `gfx/interface/counters/divisions_small/onmap_unit_wendigo_zombies_icon.dds`, SHA-256 `8eafd2bf7b2fb65ea48e0be01e5d5741b4f5db2bcad0302c409da7130e5d3623`. The copied decoded source PNGs and the original runtime hashes are retained under `source/`.

The inspected current frame 0 is the armored-human skull/helmet glyph used by the other consumer, and frame 1 is diagonal-stroke debris with jagged edges. The identity defect is concrete because the existing weaponized Wendigo portrait at `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_wendigo.dds` depicts a gaunt antlered winter beast with a wolf-like skull and animal forequarters. The package candidate therefore repairs both states from one original native-alpha Wendigo source, using the sampled vanilla normal palette for frame 0 and the sampled near-black role palette over the opaque pale inactive plate for frame 1.

| Size | Candidate processed PNG and SHA-256 | Candidate DDS and SHA-256 | Original runtime frame 0 | Original runtime frame 1 | Final decoded frame 0 | Final decoded frame 1 |
| --- | --- | --- | --- | --- | --- | --- |
| Large | `large/processed/unit_wendigo_zombies_icon.png` — `48a0a3e8de28d7a095e0d0695df366bd655ef6aeeeedbdbd087626b2f8f19741` | `large/unit_wendigo_zombies_icon.dds` — `f8eb957ea5aeda148a7bbf589c24699c7c845978de766e451fa5c180933747c5` | `e83958e7046da612b45a76ab5daa4e9028ce284e2bfb9fcf1f9bc0eed001c7c0` | `8c747ce9877fcb8c2e31e68ab106d1d6fda89efcde3cd5ccb51d63400baa0303` | `681184e22f291dc7f51eca856b72e3b4d5defca9aac25e752615d8e790a5b744` | `2af642d9c7faef7c7d618e9874f57442e6647ae3777ea80151a676fddeef6c17` |
| Small | `small/processed/onmap_unit_wendigo_zombies_icon.png` — `3a09b70ff53f8525b771708044b1bdc1752cc317052463a94dcf9a1e01a5389b` | `small/onmap_unit_wendigo_zombies_icon.dds` — `ee16f8a25b5b436c613d52ca0dddae28666da7171587793490dc6dc142ba9ee8` | `61b70b540db444228c9ae66f3e79cfd16388d1d977625799bf41dcb35d8b63dc` | `f972092d1f9f57ab9c5306e859b3a25fbe1b9368d36f144da188a62af07aa958` | `b2cff5b4137ea0a811892ac314abfb8e5c469466cffee38376ca853e325bc539` | `42f14ed08f926046737d2c7dd87834cc0105fc6970e326844c01d11bf5af5dcb` |

The native-alpha generated source is `source/wendigo_schematic_generated.png`, SHA-256 `baaedf006e8c7b24f29eb21d270514601969bb60fa33d77f89de6de2409e0746`. The identity evidence copy is `source/identity_reference_portrait_original.dds`, SHA-256 `1468c7998f98cca7cf79d916a5db177aaf2bf93b6568a977ea901a22b9fd4fdc`, with decoded review PNG `source/identity_reference_portrait_decoded.png`, SHA-256 `6e4c8fb40595bf744d1c5fb59eb5cf7c3d885b22c0e7a0b0c52becee773a2d83`.

`wendigo_repair.json` records both concrete defects and the original/final frame hashes. `validation.json` records exact PNG-to-DDS round trips, strict dimensions and headers, canonical palette/plate checks, native alpha, `runtime_write=false`, and the `sprite=zombies` shared-consumer limitation. No dedicated Wendigo mesh, entity, animation, GFX wiring change, or live-game validation is claimed here; the quadruped model route remains outside the active runtime until the parent changes that consumer.

## Boundaries and review state

The parent owns promotion into `gfx/interface/counters/divisions_large/` and `gfx/interface/counters/divisions_small/`, any final `.gfx` or gameplay edits, and live-game validation. This work made no shared GFX, gameplay, definitions, runtime, model, localisation, or other job-folder changes.

The stale `specialized_zombie_counter_art_handoff.md` was not treated as evidence because its claimed counter bytes were absent. All paths and hashes in this handoff come from files currently present in the package folders and their validators.

No simplification was made within the authorized counter scope. The only route limitation is recorded explicitly: `wendigo_zombies` still shares `sprite = zombies`, so its package provides reviewable counter evidence without asserting a dedicated model route or wiring change.

No commit was created, as requested.
