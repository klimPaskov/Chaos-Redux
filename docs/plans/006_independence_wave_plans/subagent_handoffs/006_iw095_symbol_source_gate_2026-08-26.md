# IW-095 Dahomey — symbol and flag source gate (2026-08-26)

Audit date: 2026-08-26 (Europe/Kyiv).

Scope: bounded non-portrait source audit for Event 006 IW-095 Dahomey (`DAH`), covering the opening-1936 identity, installed vanilla flags, historically defensible Dahomey/Abomey symbol leads, and redistribution rights.

Status: **BLOCKED for a historically sourced 1936 baseline / NEEDS_USER_REVIEW for any alternate-history route flag**.

No gameplay, country, history, localisation, `.gfx`, runtime flag, source PNG, processed preview, DDS/TGA output, or contact sheet was created or changed by this audit.

## Decision

The installed vanilla `DAH` family is technically complete but is not appropriate as the historical 1936 Event 006 opening flag family.

The green-hoist/yellow-over-red design is the flag adopted by the Republic of Dahomey on 16 November 1959, not a documented colonial-era 1936 Dahomey flag.

The other installed ideology files are later or generic ideological variants and do not establish a 1936 Dahomey identity.

No reviewed source establishes one package-wide, independently documented 1936 Dahomey national flag that is both historically attributable and safe to redistribute as runtime art.

The current carrier may remain technically available for parent-owned testing, but the IW-095 symbol gate must remain closed until the parent accepts either a primary-source-backed route-specific banner or an explicitly alternate-history civic flag brief.

## Authority and registry evidence

The accepted first-footprint addendum is `docs/plans/006_independence_wave_plans/006_event6_first_footprint_admission_improvement_addendum_2026_08_26.md`.

Its IW-095 row requires carrier `DAH`, current-map state 776 Dahomey, reservation group `RG-NIGERIA-COARSE`, and a specific check that the vanilla flags describe Dahomey rather than post-1960 Benin.

The candidate registry row at `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:96` records IW-095 as `Dahomey`, `DAH`, `reuse_registered_tag`, `sourced historical flags and leaders`, and `automatic_pool_ready_if_unique_state_exists`.

The asset-family row at `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv:45` defines ASSET-044 as the normal/medium/small country-flag family at 82x52, 41x26, and 10x7.

The asset ledger at `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:19-25,74-85` places IW-095 in existing-base reuse, but explicitly limits reuse to a base flag that matches the package identity and opening route.

The accepted sensitive-identity rules are `docs/specs/006_independence_wave_specs/research/006_sensitive_identity_research_rules.md`.

The canonical review library is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`.

Its flags shelf contains a 21-reference review contact sheet and no DAH-specific reference; it is review-only and does not grant a runtime redistribution licence.

## Installed vanilla identity and flag audit

Vanilla binds `DAH` to `countries/Dahomey.txt` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:160`.

Vanilla state 776 is named `STATE_776` with the comment `Benin/Dahomey`, is owned by `FRA`, and has `DAH` as a core at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/776-Dahomey.txt:2-10`.

Vanilla country localisation is ideology-dependent rather than a single clean 1936 identity: `DAH_neutrality` is “Dahomey”, the bare `DAH` key is “Benin”, democratic is “Benin”, fascist is “Benin Unitary Federation”, and communist is “Socialist Republic of Dahomey” at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_l_english.yml:2619-2633`.

No DAH flag files are present in the mod `gfx/flags/`, and no DAH reference files are present in the canonical flags shelf.

The current runtime therefore falls back to the installed vanilla files below when the parent uses the `DAH` carrier.

| Installed source | Native format | SHA-256 | Visual observation and historical status |
|---|---|---|---|
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/DAH_neutrality.tga` | 82x52, TGA type 2, 32-bit, descriptor 8 | `bfa74629618da992c30b95c7e775b2e5cb8b5d45577810e5f5b8f33a15362c15` | Green hoist with yellow-over-red fly; matches the 1959 Republic of Dahomey design, not a documented 1936 colonial flag. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/DAH_democratic.tga` | 82x52, TGA type 2, 32-bit, descriptor 8 | `40bbbbf7ce00d167ab96965850fe00adcf9a11a8d09a08b8a6f9f8807d2c6a10` | Same yellow/red/green layout with a white star; ideological variant, not 1936 evidence. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/DAH_communism.tga` | 82x52, TGA type 2, 32-bit, descriptor 8 | `8f18c34624d85dd4d5b48c7d0bea4d8c83ebf1fb79989f15fcaa76888b91712d` | Green field with a red star; post-1975-style ideological symbolism, not 1936 evidence. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/DAH_fascism.tga` | 82x52, TGA type 2, 32-bit, descriptor 8 | `f3c18ee3f5e04de13ad96086fd39c474361b0499e31c4b4aee810308504c0daa` | Red-bordered white panel with an elephant motif; vanilla ideological art, not a sourced 1936 Dahomey flag. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/medium/DAH_neutrality.tga` | 41x26, TGA type 2, 32-bit, descriptor 32 | `3355ff209bf8658bc4abcf36a5bebe100e9f21e55983951a8994ded2274b699c` | Reduced neutral version of the 1959 design; descriptor uses top-left origin. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/medium/DAH_democratic.tga` | 41x26, TGA type 2, 32-bit, descriptor 32 | `a95290563028b056e3e1aad929c37e0460a4cd07dfbe0ba22653b64d5bd4c724` | Reduced white-star ideological version; descriptor uses top-left origin. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/medium/DAH_communism.tga` | 41x26, TGA type 2, 32-bit, descriptor 32 | `98b3c119e1d4459d2d6cd06bd9d88aa228589a78b4789f029e0e632700c2fa99` | Reduced red-star ideological version; descriptor uses top-left origin. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/medium/DAH_fascism.tga` | 41x26, TGA type 2, 32-bit, descriptor 8 | `1708cb6903d5dd7a893a958607b72f644e61916717f551dc5ed73d46f1b23925` | Reduced elephant-panel ideological version. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/DAH_neutrality.tga` | 10x7, TGA type 2, 32-bit, descriptor 0 | `a0929469ed6678955bc9b8a7664cb3b23e7a962ad82ddb6ad7cdecedad2b855c` | Small neutral version of the 1959 design. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/DAH_democratic.tga` | 10x7, TGA type 2, 32-bit, descriptor 0 | `18fa1986423834256571793ca26103f09894c8d50e84c7905c22a6bbf4856d8c` | Small white-star ideological version. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/DAH_communism.tga` | 10x7, TGA type 2, 32-bit, descriptor 0 | `a7d3d82326b2b41feca0caa49347b5a98d29a961a07874b81ceb136d979ea2ff` | Small red-star ideological version. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/DAH_fascism.tga` | 10x7, TGA type 2, 32-bit, descriptor 0 | `7de5132da791612edaeab3de9dd947236bd560246fa27805da9d1b0a50698e04` | Small elephant-panel ideological version. |

The neutral master uses dominant RGB values `0,153,0`, `255,255,0`, and `255,0,0`, confirming a clean modern flat tricolour rather than an archival texture.

The installed files are valid technical vanilla inputs for inspection only; no redistribution permission for game-owned art is inferred, and they were not copied into the mod.

## Historical source review

The accessible flag chronology at <https://en.wikipedia.org/wiki/Flag_of_Benin> records that the green-hoist/yellow-over-red flag was adopted on 16 November 1959, served the Republic of Dahomey from 1959 to 1975, and was restored in 1990.

The same page records that French colonial Dahomey used the French tricolour as its official flag and that the colony was not permitted a separate regional flag; this is secondary evidence with cited Britannica and historical-dictionary references, so the exact colonial regulation remains a source uncertainty rather than a claim of primary archival proof.

The French-colony chronology at <https://en.wikipedia.org/wiki/French_Dahomey> places French Dahomey in French West Africa from 1894 to 1958 and places the Republic of Dahomey after the 1958 transition, which is consistent with rejecting the 1959 flag as a 1936 baseline.

The accepted regional context source is the Library of Congress Federal Research Division Nigeria study at <https://tile.loc.gov/storage-services/master/frd/frdcstdy/ni/nigeriacountryst00metz_0/nigeriacountryst00metz_0_djvu.txt>.

That study is useful for regional Dahomey/Benin distinctions, but it is not an asset licence and does not establish a single 1936 Dahomey flag.

The independent heraldic research at <http://www.hubert-herald.nl/BeninDahomey.htm> describes a Béhanzin banner captured in the Abomey palace on 18 November 1892, notes that the museum colour interpretation is disputed, and suggests that different kings may have used different banners.

The following public or Creative Commons files are historical leads only and do not clear a package-wide 1936 flag.

| Candidate source | Rights metadata | Historical function and fit | Disposition |
|---|---|---|---|
| <https://commons.wikimedia.org/wiki/File:Dahomey_flag_1889.svg> | Commons marks the modern vector public domain; author metadata is Jaume Ollé, SVG by ArnoldPlaton, dated 2012. | The page describes a Kingdom of Dahomey flag associated with King Ghezo and “perhaps” 1889; a page addendum notes that the evidence may instead point to 1818–1859 and asks for a citation for 1889. | Research only; do not label as a verified 1936 national flag. |
| <https://commons.wikimedia.org/wiki/File:Flag_of_Ghezo_of_Dahomey.svg> | CC BY-SA 4.0; modern reconstruction by Di, dated 2020, based on Hubert-Herald and an attributed badge. | King Ghezo’s route-specific royal design, not an opening-1936 state flag; the source is a reconstruction rather than a period scan. | Research only; any later use requires attribution/share-alike compliance and a dynastic-route label. |
| <https://commons.wikimedia.org/wiki/File:Royal_banner_of_B%C3%A9hanzin_of_Dahomey.svg> | Commons marks the modern vector public domain; Samhanin, dated 2019. | Reconstructed Béhanzin royal banner for 1889–1892; ownership, colours, and function do not establish a universal 1936 national flag. | Research only; primary museum/archive confirmation is required before any route asset. |
| <https://commons.wikimedia.org/wiki/File:King_Adandozan_banner_of_war.jpg> | CC BY-SA 4.0; `N.N./Museu Nacional UFRJ`; museum source; object dated circa 1800. | Photograph of an actual Adandozan war banner, not a national flag and far earlier than the 1936 opening. | Research only; useful object evidence, not a runtime country flag. |
| <https://commons.wikimedia.org/wiki/File:FOOT(1854)_p098_DAHOMEY,_SKULL_ORNAMENTS_AND_BANNERS.jpg> | Public-domain 1854 scan; British Library Mechanical Curator/Commons record. | Period book plate showing Dahomey banners and regalia, but not one attributable state flag or a 1936 design. | Research only; source motif context, not a final flag. |
| <https://commons.wikimedia.org/wiki/File:Flag_of_Benin.svg> | Commons marks the vector public domain. | The depicted design is the 1959 Republic of Dahomey/Benin flag and is therefore anachronistic for the 1936 opening. | Reject for the IW-095 1936 baseline. |

The source review found no defensible basis for treating an elephant, shark, egg, palm, royal throne, war banner, or modern Beninese tricolour as an undifferentiated Dahomey national symbol.

## Manifest-style blocked record

| Asset id | Source and provenance | License | Date and era fit | Source/processed/runtime paths | Runtime basename and sprite | Status and uncertainty |
|---|---|---|---|---|---|---|
| `IW-095-DAH-flag-family` / ASSET-044 | Installed vanilla `DAH_*` TGA family listed above; no package-local source master selected. | Vanilla game files; no redistribution licence inferred. | Technical 1936-compatible dimensions, but neutral design dates to 1959 and ideology variants are later/generic. | Source: installed vanilla paths only; processed PNG: none; final TGA/DDS: none; mod `gfx/flags/DAH*`: absent. | Parent-proposed basename: none; current engine lookup is `DAH`, `DAH_neutrality`, `DAH_democratic`, `DAH_communism`, and `DAH_fascism`; sprite: none. | **blocked** for historical baseline; **needs_user_review** for an explicit alternate-history or route-specific design. |

Because no candidate cleared the source gate, no source file, processed PNG preview, final TGA/DDS, manifest file, or `gfx_handoff.md` was created for IW-095.

## Safe paths and owner handoff

The canonical review-only flag sheet is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png`.

The installed vanilla DAH files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/` and its `medium/` and `small/` subfolders are safe audit inputs only, not safe runtime copies.

No safe IW-095 runtime flag path or sprite basename is available from this audit.

If the parent accepts a generated alternate-history civic baseline, the parent must first record the exact route identity and proposed `X`-suffixed basename, then send an asset brief to the flag-production owner with period motif sources, explicit alternate-history wording, and the normal/medium/small ladder requirement.

If the parent wants a traditional route, it must first obtain primary museum or archival confirmation for the exact banner owner, date, function, colour geometry, and redistribution rights; a Commons reconstruction alone is not enough.

Do not copy the vanilla DAH tricolour, the public-domain Benin vector, or any reconstructed royal banner into the runtime and call it a historical 1936 Dahomey flag.

Do not use the French tricolour as an independent DAH identity; it represents the colonial host and would erase the package’s post-report independence distinction.

Portrait sourcing and portrait files are outside this audit and remain routed to `chaosx_portrait_creator`; the existing separate IW-095 asset handoff records that gate.

## Validation and remaining blockers

The installed 12-file family was checked for dimensions, TGA type, bit depth, descriptor, visual content, and SHA-256 values.

The canonical flags contact sheet was inspected and contains no DAH reference.

The installed neutral, democratic, communist, and fascist DAH normal variants were visually inspected; the neutral medium and small ladders were also inspected.

No live game, MCP render, or gameplay admission claim is made.

Remaining blockers are the lack of a primary-source-backed 1936 Dahomey flag, uncertain ownership/function and disputed colours for reconstructed Abomey royal banners, and the absence of a parent-approved alternate-history route identity and runtime basename.

This handoff does not alter the addendum’s authority boundary or admit IW-095 to the central Event 006 pool.
