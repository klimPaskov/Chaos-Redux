# IW-050/KOM Komi flag and symbol source research — fail-closed handoff

Audit date: 2026-08-14.

Owner scope: source-only historical flag and symbol research. No runtime TGA/PNG/DDS files, ImageGen output, `.gfx` entry, country/cosmetic-tag edit, event edit, localisation edit, or gameplay wiring was created.

## Verdict

**BLOCKED / fail closed for a new neutral or route-specific Komi flag.** The accepted IW-050 specification permits reuse of the registered KOM base only when the released identity and origin match, permits sourced historical route variants, and permits generated clearly alternate, civic, or high-chaos variants. It does not name any Komi route identifiers, route-tag filenames, route ownership rules, or requirement-to-runtime crosswalk for a new flag family. No generated route mark is therefore authorized by the currently accepted evidence.

The installed game has a KOM ideology ladder, but the source path changed during this audit. The official game path was first observed as a complete type-2 32-bit ladder and later observed with the democratic/fascist/neutrality members replaced by byte-identical type-10 RLE files dated 2026-08-13. That non-stationary state is recorded below and prevents treating the current path as a clean immutable vanilla reference. The parent must resolve the concurrent file mutation before any runtime reuse or final asset QA.

No defensible neutral 1936 Komi state flag was located. The only period-adjacent source with a clear constitutional attribution is a 1937 Komi ASSR institutional flag reconstruction; it is one year after the 1936 opening, carries RSFSR/ASSR state identity and text, and cannot be presented as a neutral Komi national flag. Modern Republic, Komi Voityr, and Nordic-cross designs are post-1936 and route/institution-specific.

## Accepted IW-050 design boundary

The candidate registry row identifies `IW-050` as Komi, registered tag `KOM`, anchor state `397`/Syktyvkar, and `reuse_registered_tag` (`docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:51`).

The package research resolution says: “Reuse the registered base flag only when it matches the released identity and origin. Source historical route variants. Generate only clearly alternate, civic, or high-chaos variants” (`docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51`).

The Event 006 asset ledger places IW-050 in Group A, existing registered base reuse, and says the installed normal/medium/small ladder may be retained only when it matches the package identity and opening route; historical or route-specific variants still need separate provenance (`docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:75-82`).

The country-package specification explicitly keeps Komi distinct from Tatar, Chuvash, Bashkir, Mari, Udmurt, Mordvin, Buryat, Sakha, Altai, Khakass, Nenets, and other identities (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:591-593`). A generic Volga-Finnic, pan-Ural, Soviet, or Nordic symbol must not be relabelled as a neutral Komi flag.

## Installed KOM ladder evidence

Authoritative source root requested by the repository is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/`, with `medium/` and `small/` subfolders. The canonical review library was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`; it contains the flag family contact sheet and flag references but no KOM-specific review PNG.

### First complete snapshot observed during this audit

At the first read, all four ideology members existed as uncompressed type-2 32-bit TGA files at the expected 82x52, 41x26, and 10x7 sizes. The following hashes are retained as evidence of that snapshot, not as new runtime assets:

| Path | Size | Header observation | SHA-256 |
| --- | ---: | --- | --- |
| `gfx/flags/KOM_communism.tga` | 82x52 | type 2, depth 32, descriptor `0x08`, 17,100 bytes | `30ff8121e5099723e0cd3411a9a2c44fc4192549038a1b42f059d91358724aee` |
| `gfx/flags/KOM_democratic.tga` | 82x52 | type 2, depth 32, descriptor `0x08`, 17,100 bytes | `9a76f666e2545601a8b2ea657a1a9dd7b311c35b7076645d7d07d438709ea8d9` |
| `gfx/flags/KOM_fascism.tga` | 82x52 | type 2, depth 32, descriptor `0x08`, 17,100 bytes | `b4ed90cdd4d03f7cb74eb3be9edabd7d30d8929ec92c2b99cfa62e50503a193d` |
| `gfx/flags/KOM_neutrality.tga` | 82x52 | type 2, depth 32, descriptor `0x08`, 17,100 bytes | `2e9a464de6cfc0bf10b053361096b06dfd72ab3a2a12819805d9277e0e8b15c9` |
| `gfx/flags/medium/KOM_communism.tga` | 41x26 | type 2, depth 32, descriptor `0x08`, 4,803 bytes | `af1828d2c31ad7bfdfcafa1833a5425a0a159b09e55395a0f5d8fe19ab6f8f9c` |
| `gfx/flags/medium/KOM_democratic.tga` | 41x26 | type 2, depth 32, descriptor `0x08`, 4,803 bytes | `a5bd8f59e132cf08d69ccc92da2f3c781540bece3f47cdc886ac0cdc6f383fc6` |
| `gfx/flags/medium/KOM_fascism.tga` | 41x26 | type 2, depth 32, descriptor `0x08`, 4,803 bytes | `f19f2d660d0a2bda87282e649071622c3cb9e78b67af58dba9f340cf30bbb29c` |
| `gfx/flags/medium/KOM_neutrality.tga` | 41x26 | type 2, depth 32, descriptor `0x08`, 4,803 bytes | `8783e8e3927ba0f5ef12ab455e5a5788866cea34315102edd71fdab4b61df37f` |
| `gfx/flags/small/KOM_communism.tga` | 10x7 | type 2, depth 32, descriptor `0x00`, 298 bytes | `0e644d5734c4160f9805fec653e88c4f8d62055a185952bac388bc85c711658c` |
| `gfx/flags/small/KOM_democratic.tga` | 10x7 | type 2, depth 32, descriptor `0x00`, 298 bytes | `96a36c8939a96934abf69fb9286dd72bc11744d31b89ccf71fa6e96ef38e09b3` |
| `gfx/flags/small/KOM_fascism.tga` | 10x7 | type 2, depth 32, descriptor `0x00`, 298 bytes | `c43bf5e259f15e88942a34783c41527ce7159285c496fe670fd105ace4ce14cd` |
| `gfx/flags/small/KOM_neutrality.tga` | 10x7 | type 2, depth 32, descriptor `0x00`, 298 bytes | `4945c8d5eefa414aaf5b3326b4f49de09879c34d007599fc7520b11c528cc785` |

No file was copied or edited by this audit. Because the source path changed during the same session, re-hash the file after the path is stabilized before any reuse claim.

### Later conflicting snapshot observed in the same session

The same official path subsequently reported the following for democratic, fascist, and neutrality files: normal 82x52 / 3,588 bytes / type 10 / descriptor `0x28` / SHA-256 `f550493e3ca57bab7337088291f5ade36937729c0f1f234b44276dba5187fb24`; medium 41x26 / 1,528 bytes / type 10 / descriptor `0x28` / SHA-256 `bb75c7a96eb014a2b06718f3a1ce12d03b03ec38dad41958005a3395e6f0b65e`; small 10x7 / 279 bytes / type 10 / descriptor `0x28` / SHA-256 `414a3624def506bc11f06349f18f15fa0667d94fad14432a54f83b8ff0af3e1a`. All three ideology files were byte-identical at each size. `KOM_communism` remained at the 2024 type-2 snapshot. This is not a valid clean vanilla ladder for acceptance and requires parent investigation.

## Historical and culturally grounded symbol candidates

### 1937 Komi ASSR constitutional flag — period-adjacent institutional reference only

- Wikimedia Commons file: [Flag of the Komi ASSR (1937)](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_ASSR_(1937).svg).
- Direct source URL: `https://upload.wikimedia.org/wikipedia/commons/1/12/Flag_of_the_Komi_ASSR_%281937%29.svg`.
- Commons metadata: artist Helgo13; date of reconstruction 2019-05-17; credit `Constitution of Komi ASSR`; SHA-1 `856333903cd513bd5852cb00becabbee5b6bcb55`; stated license `Public domain`, category `PD-RU-exempt (flags)`.
- Historical design claim: the 1937 Komi ASSR constitution describes an RSFSR red field with gold `RSFSR` and `Komi ASSR` inscriptions in Russian and Komi. The 1938–1954 reconstruction changes the Komi script to Cyrillic and is later than the 1936 opening.
- Primary bibliographic lead: [Nauka Prava catalog entry](https://naukaprava.ru/catalog/3561/3564/43687?view=1), 1937 Syktyvkar Executive Committee edition, 48 pages, “Constitution (Basic Law) of the Komi ASSR” project.
- Rights/identity verdict: rights are stated as public domain for the reconstructed flag, but the design is an institutional ASSR/RSFSR standard and is not a neutral Komi national flag. Do not ship or generate from it as the default KOM baseline. It can inform a separately approved socialist/ASSR historical route only if the parent names that route and accepts the 1937/1938 date boundary.

### 1938–1954 Komi ASSR constitutional flag — later institutional route reference only

- Wikimedia Commons file: [Flag of the Komi ASSR (1938–1954)](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_ASSR_(1938-1954).svg).
- Commons metadata: artist Jeromi Mikhael; date 2018-10-31; credit constitution description; stated license `Public domain`; SHA-1 `26eeb11f57006423acc860de5dac72c4461422e3`.
- Rejected for 1936 baseline because it is a later constitutional version and retains Soviet institutional identity.

### Modern Komi Republic tricolour — not 1936-compatible

- Wikimedia Commons file: [Flag of Komi](https://commons.wikimedia.org/wiki/File:Flag_of_Komi.svg).
- Commons metadata: design dated 1997-12-17; artist V. Ya. Serditov; stated license `Public domain`; SHA-1 `4d0669da39450a7bc282452002d54e1ba9485d92`.
- The blue/green/white tricolour is a modern Komi Republic state flag. It is useful as identity context but cannot be backdated to 1936 or treated as a period-accurate neutral route mark.

### Komi Voityr organizational flag — exact institution only, not neutral state identity

- Wikimedia Commons file: [Flag of the Komi Voityr](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_Voityr.svg).
- Commons metadata: ProjectHorizons, 2022-11-15; stated license `CC BY-SA 4.0`; SHA-1 `e281f47b704bdb5688e0b1d7874555b4d7d35974`.
- This is explicitly an organizational flag used alongside the official Republic flag. It cannot be relabelled as a neutral Komi state flag. CC BY-SA terms also require an approved attribution/share-alike treatment if reused.

### Nordic-cross proposal — modern activist alternative, no accepted route

- Wikimedia Commons file: [Komi Nordic cross flag](https://commons.wikimedia.org/wiki/File:Komi_Nordic_cross_flag.svg).
- Commons metadata: ProjectHorizons, 2019-10-09; stated license `CC BY-SA 4.0`; SHA-1 `df9651b27b94bcf6ddf1d204d8d24e083de54ae1`.
- This is a 2010s activist proposal and is not a 1936 flag. It cannot be used for a default or neutral Komi route without an explicit high-chaos/alternate-history amendment that names the route, owner, and rights treatment.

## Source and rights conclusion

No source establishes a distributable, neutral Komi national flag valid for 1936. The constitutional flag sources establish Soviet ASSR institutions, not an independent neutral Komi identity. Modern tricolour, Voityr, and Nordic-cross sources are temporally or institutionally wrong for a 1936 baseline. Therefore no source asset, processed preview, DDS, contact sheet, or `gfx_handoff.md` is being produced for IW-050.

## Parent handoff / required next decision

1. Stabilize and re-audit the official vanilla `gfx/flags/KOM*` ladder before any reuse claim; the current source path showed concurrent mutation and must not be treated as authoritative until re-hashed.
2. If the opening route is ordinary registered KOM, reuse only the stabilized installed ladder with no new asset and preserve the existing no-suffix/ideology naming contract.
3. If a historical route is desired, parent must name the route and accept the exact institution/date boundary. The 1937 ASSR flag can be a sourced design reference for a Soviet institutional route, not a neutral baseline.
4. If a generated route mark is desired, parent must amend the accepted spec with exact route identifiers, route ownership, source motifs, and the alternate/civic/high-chaos classification. Only after that approval may `chaosx_generated_event_art` produce separate flat ImageGen masters and ladders.
5. Do not copy Commons SVGs, generated designs, workshop files, or current mutable game files into runtime paths from this handoff. No `.gfx` or gameplay wiring is implied.
