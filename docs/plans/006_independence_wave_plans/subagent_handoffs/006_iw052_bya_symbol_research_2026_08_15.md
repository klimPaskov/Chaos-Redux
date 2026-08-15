# IW-052 Buryatia (`BYA`) symbol and flag provenance handoff

## Status

`BLOCKED / FAIL-CLOSED` as of 2026-08-15.

This is a bounded, read-only source and installed-carrier audit for the IW-052 Buryatia symbol request. No runtime PNG, TGA, DDS, or GFX asset was created. No ImageGen call was made. No vanilla file, gameplay file, country file, localisation file, map file, workbook, central-admission surface, or Join surface was changed.

The installed vanilla carrier is usable as an existing carrier only. The exact provenance of its neutral ideology flag is not defensible as a 1936 Buryat flag from the sources reviewed, so this audit does not approve a historical replacement or a new route variant.

This handoff was re-audited against the current package-local implementation on 2026-08-15. The package-local audit still reports `BLOCKED / FAIL-CLOSED`, and no new source, rights receipt, or approved design route clears the symbol gate.

## Decision

Do not generate, repaint, copy, replace, or wire a BYA neutral flag from the current evidence.

The documented pre-1937 material is uncertain, the documented 1937 and 1939 Buryat-Mongol ASSR flags are red text-bearing Soviet constitutional flags, and the modern blue-white-yellow Soyombo flag dates from 1992. None is a source-backed match for the installed vanilla `BYA_neutrality.tga` design. A modern provincial flag is identity evidence, not permission to backdate a symbol to 1936.

The vanilla triplets must remain untouched until one of the following gates is explicitly cleared:

1. An authoritative archival, museum, official heraldic, or public-domain source proves the installed neutral design or another approved symbol was used by the relevant Buryat institution in or before 1936 and supplies usable rights evidence.
2. The parent explicitly approves the installed vanilla neutral triplet as a reused baseline without claiming that its artwork is a historically attested 1936 flag.
3. The parent approves a separate alternate-history, civic, or high-chaos route with its own basename, documented design brief, and ImageGen/source-design authorization.

## Installed vanilla carrier

The installed tag mapping is `BYA = "countries/Buryatia.txt"` in `common/country_tags/00_countries.txt:222`. The installed country definition is `common/countries/Buryatia.txt`; it uses `asian_gfx`, `asian_2d`, and country color `rgb { 0 64 255 }`. The installed history is `history/countries/BYA - Buryatia.txt`.

The installed history has capital state `564` (Ulan Ude), two research slots, and a 1936 democratic/neutrality opening with `democratic = 50`, `neutrality = 50`, `fascism = 0`, and `communism = 0`. These files are vanilla carrier evidence only; they do not constitute Event 006 package admission or symbol provenance.

Vanilla provides four ideology variants at every required flag size and no no-suffix `BYA.tga` base. All checksums below are SHA-256 hashes of the installed vanilla bytes, collected read-only. No external source file was downloaded, so there are no external hashes to report.

| Installed surface | File | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| normal / neutrality | `gfx/flags/BYA_neutrality.tga` | 82x52 RGBA | `e607a634676ad35da60985420189bf673979d3c894403c4debc457a23fe4b4d1` |
| normal / communism | `gfx/flags/BYA_communism.tga` | 82x52 RGBA | `c5baf46ad5510d06696964b834ed0c2b6e4196eb3cce8857924731e88fdb590d` |
| normal / democratic | `gfx/flags/BYA_democratic.tga` | 82x52 RGBA | `26cb64158da6ac65821a15dbcd14ef519dccee9aa7b79a891677f12d6a54f506` |
| normal / fascism | `gfx/flags/BYA_fascism.tga` | 82x52 RGBA | `0c0b1dde4a934e07fd03b0ba579482a8f5bffe2fbe398a127274cd2e734bcb03` |
| medium / neutrality | `gfx/flags/medium/BYA_neutrality.tga` | 41x26 RGBA | `3b960c0c27e6f3da70a3a91570d33ace0231693bc42d67a519263f24253ad69d` |
| medium / communism | `gfx/flags/medium/BYA_communism.tga` | 41x26 RGBA | `8e5238df4a63f74c0396d74090d85eb61a740276e12ff1469235aae1050119ba` |
| medium / democratic | `gfx/flags/medium/BYA_democratic.tga` | 41x26 RGBA | `db4bfc65d24699f065d058c62525303374640c521dd2c4d8842c5e53cb9a28c5` |
| medium / fascism | `gfx/flags/medium/BYA_fascism.tga` | 41x26 RGBA | `4004929c6bb245dbc5e2c3254c6336a89c5bae9c6da753ef690b210d60926e90` |
| small / neutrality | `gfx/flags/small/BYA_neutrality.tga` | 10x7 RGBA | `93a57636ddc7e78a88f5f11bb1c6379c29bbb782cd5d6f59078de6a8ce338832` |
| small / communism | `gfx/flags/small/BYA_communism.tga` | 10x7 RGBA | `b386bbfabd9eb660ec3d10b9080088e68c4a66649e8e47a6972bc2a2d56af57c` |
| small / democratic | `gfx/flags/small/BYA_democratic.tga` | 10x7 RGBA | `0204ddb898a0b984720538baec4460e8e06ec25fa97a3ee089c35b57fa07d5f7` |
| small / fascism | `gfx/flags/small/BYA_fascism.tga` | 10x7 RGBA | `25bd02f3b53accb50b5ba8b3d09a79ed8f06e70133e1e718a08351ecfaa3c984` |

The vanilla TGA headers identify 32-bit uncompressed images at the three ladder sizes. Their inspected source headers use the installed vanilla descriptor orientation; this is evidence about the carrier only and is not a new final-asset conversion recommendation. The repository asset policy still requires any newly delivered flag triplet to be 32-bit uncompressed TGA at 82x52, 41x26, and 10x7 with bottom-left origin.

## Visual and era assessment

The neutral normal flag is a flat red, white, blue, white, red band composition with a white central emblem on blue. Pixel inspection can describe that layout, but no reviewed source attributes that exact emblem or composition to a Buryat 1936 institution. It must not be relabelled as an attested historical flag.

The democratic variant visually resembles a blue-white-yellow tricolor with a yellow Soyombo-like device near the hoist. The modern Republic of Buryatia flag uses that family, but its adoption date is 1992-10-29. It is therefore not a neutral 1936 source without a separately approved alternate-history route.

The communism and fascism variants are ideology-specific vanilla graphics. Their visual motifs were not assigned a historical source in the installed files or the reviewed archival references. They are not evidence that the neutral variant existed in 1936.

## Source, rights, and era evidence

The following sources were reviewed only for provenance research. None was selected as a runtime asset source.

| Source | Evidence | Rights/date/era result | Runtime decision |
| --- | --- | --- | --- |
| [Flags of Buriatia in the Soviet Union](https://www.crwflags.com/fotw/flags/su-rubu.html) | FOTW reports that the Buryat-Mongol republic was created in 1923, gives a possible ca. 1927 flag with no firm information, and documents red text-bearing 1937 and 1939 constitutional variants. | Page last modified 2021-07-24. FOTW carries its own copyright notice and does not provide a permissive runtime-art license in the reviewed page. The pre-1937 candidate is explicitly uncertain, and the documented 1937/1939 designs do not match installed BYA neutrality. | Historical research only; rejected as a direct runtime source and rejected as proof of installed neutral provenance. |
| [Modern Buryatia flag, FOTW](https://www.crwflags.com/fotw/flags/ru-03.html) | Describes the current blue-white-yellow flag and the Soyombo device. | Page last modified 2020-02-24. FOTW rights remain research-only for this task. The flag was adopted 1992-10-29, outside the 1936 opening era. | Modern identity context only; cannot be backdated to 1936. |
| [Flag of Buryatia](https://en.wikipedia.org/wiki/Flag_of_Buryatia) | Provides a timeline that places the current flag in the post-Soviet period and identifies the 1937-1954 Buryat-Mongol ASSR interval. | The article is marked unsourced in the reviewed revision and is therefore a lead rather than sole historical proof. Wikipedia prose is CC BY-SA 4.0, but that does not license copying an unverified flag design into the mod. | Lead/timeline only; no direct runtime artwork selected. |
| [Buryat-Mongol ASSR 1937-1954 SVG](https://commons.wikimedia.org/wiki/File:Flag_of_the_Buryat-Mongol_ASSR_(1937-1954).svg) | Commons metadata describes the 1937 constitution and Article 112 red cloth with RSFSR/BMASSR inscriptions, initially in Latin and later in Russian. | Commons metadata records `1937-02-15`, artist unknown, and `CC0`/Public Domain Dedication, with a proher.ru credit. The vector is a historical reconstruction/representation of the documented text-bearing flag, not a match for installed BYA neutrality. | Rights may support separate historical reference use, but era/design mismatch blocks this request. |
| [Buryat-Mongol ASSR 1925-1937 PNG](https://commons.wikimedia.org/wiki/File:Flag_of_the_Buryat-Mongol_ASSR_(1925-1937).png) | Commons describes a FOTW-based depiction of the earlier Soviet republic period. | Metadata records artist Jaume Ollé, date 1996-11-13, and CC BY-SA 4.0. It is a later depiction based on FOTW, while FOTW itself marks pre-1937 information as uncertain. | Historical lead only; not a direct attested source for installed neutral or a source-cleared runtime file. |
| [Buryat-Mongol ASSR 1937-1954 PNG](https://commons.wikimedia.org/wiki/File:Flag_of_the_Buryat-Mongol_ASSR_(1937-1954).png) | Commons provides a later FOTW-based depiction of the documented 1937-1954 red/text flag. | Metadata records artist Jaume Ollé, date 1996-11-13, and CC BY-SA 4.0. The file is not the period artifact and does not match installed neutral. | Research only; no runtime use. |

The source set therefore establishes a historical mismatch rather than a cleared candidate. The reviewed evidence does not prove that the vanilla neutral design was a 1936 Buryat state, municipal, customary, Buddhist, or frontier-institution standard.

## Re-audit against current package-local implementation

The current package-local receipt is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw052_buryatia_package_core_implementation_2026_08_15.md`. It confirms that IW-052 remains unadmitted because the parent-owned identity/rights receipt, leader or institutional identity evidence, symbol provenance, and weighted package evidence are absent.

The current implementation adds package-local constants, triggers, effects, ideas, decisions, AI, localisation, and five shared-focus callbacks, but no asset or identity approval. `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:72-80` checks package-slot, `RG-564`, `BYA`, and state-564 availability. `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:96-106` loads `iw_052`, `BYA`, and state 564, while `:195` reserves only state 564. These surfaces establish a planning anchor and reservation boundary; they do not prove that a flag matches the released identity and origin.

The current force mapping at `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:53` is planning metadata for a mounted-mobile Buryat frontier force. The package-local audit records that no BYA setup caller, package-local route flag, source/rights manifest, or parent-owned clearance flag such as `independence_wave_iw_052_identity_rights_cleared` exists. The vanilla BYA carrier files remain outside the mod and were not copied or altered.

The package-local audit also confirms that the Event 005 `Baikal Relay Council` portrait is origin-bound and cannot be reused as Event 006 identity evidence. The separate Erbanov source-placeholder candidate is still framing/rights HOLD, and no package-local flag file appeared in the implementation, so no runtime portrait or flag approval is warranted.

The exact next asset gate is therefore unchanged: the parent must publish the identity/rights decision and source receipts first. If the parent approves the installed vanilla triplet as an unclaimed baseline, preserve it without a historical provenance claim. If the parent approves an alternate, civic, or high-chaos route, provide a separate basename and explicit design brief before any ImageGen or sourced-art work. Neither path is currently cleared.

## Event 006 identity and origin gates

The exact Event 006 registry and research surfaces were inspected without changing them.

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:53` resolves IW-052 to `BYA`, registered-tag reuse, state `564`, Ulan Ude, and `RG-564`. It says to reuse the registered base flag only when it matches the released identity and origin, source historical route variants separately, and generate only clearly alternate, civic, or high-chaos variants.
- The same row blocks the package until a defensible sourced period leader or institution is assigned. This symbol handoff does not clear that separate identity/leadership gate.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:53` records the Buryat anchor, compact Transbaikal package, sourced historical symbols and leaders, and the registered `BYA` reuse path.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:45` says `RG-564` may reserve state 564 only when the state is unique, the tag is not living, and the host remnant test succeeds.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:53` records the current accepted binding as `IW-052` / `BYA` / state 564 / Ulan Ude with `564=SOV` and a surviving Soviet host state. This is a map binding, not symbol or package admission.
- `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:25,74-104` places IW-052 in Group A existing registered-base reuse, requires the full three-size ladder, and explicitly says a modern provincial flag is present-identity evidence rather than automatic permission to backdate it to 1936.
- `docs/events/006_independence_wave/country_api.md:28-61` requires exact package ID, origin, tag, reservation group, unique anchor, surviving host, symbols, leaders, and cleanup proof. A tag or existing vanilla carrier alone does not grant admission, focus loading, or a new identity.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_registry_gap_map_2026_08_15.md:73,110-123` keeps IW-052 on HOLD: vanilla history and flags exist, but sourced Buryat institution/leader, identity-matched symbols, package-local mechanics, host cleanup, weighted evidence, and central promotion remain unresolved.

The safe asset conclusion is to preserve the installed vanilla ladder and leave the IW-052 symbol gate unresolved. Do not infer a source-backed historical flag from carrier existence.

## Event 005 collision boundary

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event5_collision_handoff.md` records that Event 005 currently has no Event 006 reservation, tag, anchor, state, or origin guards. The shared-tag list explicitly includes `BYA` among `KAR`, `DON`, `KUB`, `CRI`, `TAT`, `BSK`, `CHU`, `MEL`, `UDM`, `KOM`, `YAK`, `ALT`, `NEN`, `FER`, `CIN`, `DAG`, `ARM`, `GEO`, and `AZR`.

The same handoff identifies Buryatia state 564 against Far Eastern packages as a high-risk different-tag geographic collision. Event 005 must publish its exact provisional tag and state footprint before Event 006 draws, Event 006 must rerun tag/state/reservation-group collisions after Event 005 reservations freeze, and Event 005 terminal adoption must exclude active Event 006-origin countries. Required regression coverage includes both event orders, living BYA before either release path, same-tag and same-anchor collisions, and host survival.

This asset audit does not alter or repair those gameplay boundaries. Parent-owned integration work must keep the origin and reservation gates separate from any later flag decision.

## Blockers and requested parent decision

1. No reviewed source proves the installed `BYA_neutrality.tga` composition is a 1936 Buryat flag or symbol.
2. The modern Soyombo tricolor is a 1992 identity source and cannot be backdated to the neutral 1936 opening without explicit route approval.
3. FOTW marks pre-1937 flag information as possible/uncertain, while the documented 1937/1939 flags are red text-bearing designs that do not match the installed neutral graphic.
4. The CC0 Commons 1937 vector has useful rights metadata but represents the documented red/text constitutional flag, not the installed neutral design; rights clearance alone does not clear identity or era fit.
5. Event 006 still has separate institution/leader, package mechanics, host cleanup, weighted evidence, central promotion, and origin gates.
6. Event 005 and Event 006 collision guards remain a parent-owned integration boundary, including state 564 and shared tag `BYA`.
7. No source PNG, processed PNG, DDS, GFX sprite, or runtime basename was produced. No manifest entry was created because no candidate was selected; this handoff is the blocked record.

To reopen the asset lane, the parent must either approve the installed vanilla triplet as an unclaimed vanilla baseline, provide a rights-cleared pre-1936 source matching the identity, or approve a separately named alternate/civic/high-chaos route with an explicit design brief and ImageGen authorization. Until then, keep all vanilla BYA files and the flat portrait archive layout unchanged.

## Validation and handoff inventory

- Read-only carrier checks covered the installed country tag, country definition, history, country color, normal/medium/small ideology ladders, dimensions, and byte hashes listed above.
- The canonical reference root was checked at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`; it contains no BYA reference that could establish provenance or authorize a replacement.
- The installed vanilla documentation directory contains no dedicated flag-art provenance document; the installed TGA files and country/tag/history files are the authoritative carrier surfaces reviewed here.
- No external source file was downloaded, so no external hash, processed preview, or conversion output exists.
- No `.gfx` handoff is appropriate because no new runtime asset exists and vanilla ideology flags use the existing engine naming convention.
- The only file produced by this task is this fail-closed documentation handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw052_bya_symbol_research_2026_08_15.md`.
