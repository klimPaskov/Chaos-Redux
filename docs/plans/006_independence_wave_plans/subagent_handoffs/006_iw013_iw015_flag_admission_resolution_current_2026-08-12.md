# Event 006 IW-013 / IW-015 flag-admission resolution

> Superseded for the NAV asset-production state by `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/gfx_handoff.md` and its companion manifest. The historical `SAFE_FLAG_ATTESTATION=NO` disposition remains authoritative for central admission because the generated route flags are alternate-history synthesis with a documented rights/provenance caveat. GLC remains governed by this handoff.

Date: `2026-08-12`.

Scope: bounded source, rights, installed-vanilla-ladder, and current-map contract review for IW-013 Basque Country on the `NAV` carrier and IW-015 Galicia on the `GLC` carrier. This handoff does not edit gameplay, country history, country tags, cosmetic tags, `.gfx`, localisation, or any runtime asset. No flag PNG, TGA, DDS, ImageGen output, contact sheet, or sprite handoff was produced because neither flag passed the current admission gate.

## Executive disposition

| Package | Current-map identity contract | Existing carrier ladder | Flag disposition | Admission result |
| --- | --- | --- | --- | --- |
| IW-013 Basque Country / `NAV` | Compact anchor is installed state `792` País Vasco; optional extensions are `172` Navarra and `806` Pyrénées-Atlantiques; reservation group remains `RG-172` | Vanilla `NAV.tga` is a Navarrese red field with gold chains and arms. The `NAV_democratic` variant is Ikurriña-like but is a route/ideology file, not the neutral base. | **BLOCKED / `needs_user_review`.** The base carrier flag does not identify the current Basque compact anchor. | **FAIL-CLOSED.** Do not attest, copy, override, or silently promote any NAV ladder. |
| IW-015 Galicia / `GLC` | Compact anchor is installed state `171` Galicia; reservation group `RG-171` | Vanilla `GLC.tga` is a plain white field with a blue diagonal and is the strongest installed civil baseline. The shielded, red-star, and fascist variants are route-specific or later/uncorroborated. | **CONDITIONAL CARRIER REUSE / `needs_user_review`.** The plain ladder may remain untouched on the vanilla carrier only after the parent explicitly accepts its twentieth-century provenance caveat and rights review. | **FAIL-CLOSED independently.** Conditional compatibility is not a standalone content attestation. |

Combined result: `SAFE_FLAG_ATTESTATION = NO`. Keep IW-013 and IW-015 outside central Event 006 content attestation. Package-local setup predicates and the complete vanilla ladders are not evidence that the grounded identities or rights have been accepted.

## Current contract and authority precedence

- `docs/events/006_independence_wave/iberian_registered_packages.md` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` are the current installed-map authority: NAV uses `792` País Vasco as the compact anchor, with `172` and `806` only as optional extensions; GLC uses `171` Galicia.
- Older baseline prose in `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, `006_package_research_resolution.csv`, and the candidate registry calls `172` the Basque anchor. That wording is stale relative to the installed-map package binding and must not drive the flag decision.
- Both packages intentionally preserve the vanilla carrier tag, history, ruling-leader roster, flag family, and non-Event-006 identity surfaces. There is no mod `NAV.tga`, `NAV_*`, `GLC.tga`, or `GLC_*` override, no route-specific cosmetic tag, and no accepted replacement ladder.
- The current package-admission audit is `006_iw013_iw015_package_admission_audit_current_2026-08-12.md`; it independently records both packages as HOLD / FAIL-CLOSED and records the current MCP artifact-manifest blocker. This handoff resolves only the flag-source/admission surface and does not weaken those other gates.

## Installed vanilla ladder evidence

The installed vanilla source is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/`. The ladders are complete, dimensionally valid, non-empty, and use the vanilla TGA convention. Normal and medium files are uncompressed 32-bit type-2 TGA, `82x52` and `41x26`, descriptor `8` (bottom-left origin, eight alpha bits). Small files are `10x7`, descriptor `0`, also bottom-left. These are installed-game references/runtime files, not files to copy into the mod.

### NAV base ladder (runtime-valid for Navarra only)

| Installed source | Dimensions | SHA-256 |
| --- | ---: | --- |
| `gfx/flags/NAV.tga` | 82x52 | `7810f746f8ed587eac8a531a1a17137cb0ae50e5b00312f668c82768942942d9` |
| `gfx/flags/medium/NAV.tga` | 41x26 | `cc83d275496a5ff04f5ad8ab8cd8d6825803e7156979c2d54f229e344e3e6ff9` |
| `gfx/flags/small/NAV.tga` | 10x7 | `4a8b700f5240a24c3bae4509cdd005657ad6b55f805900a37d6a44774e26ec0d` |

Reading: these files are engine-ready for the vanilla Navarra carrier, but their red/gold-chain motif is not a defensible neutral Basque flag for current state `792`. Keeping them on a deliberately Navarra-identified carrier would be a gameplay/design decision outside this source handoff.

### GLC base ladder (runtime-valid for the vanilla Galicia carrier; not yet independently attested for Event 006)

| Installed source | Dimensions | SHA-256 |
| --- | ---: | --- |
| `gfx/flags/GLC.tga` | 82x52 | `17d9e5f67a441bea6a77135da4cf2118535e12f4b461b1eec03ab958fff0e599` |
| `gfx/flags/medium/GLC.tga` | 41x26 | `233ac8bce579300c46b579fe35c100b9eb158ed1a2449b9a64f91e54f08ff7a9` |
| `gfx/flags/small/GLC.tga` | 10x7 | `b61e46b73aa478acc1f117815db6f782dd0334b6398535cfb8f11486724d1951` |

Reading: these are exact installed-file hashes recorded for reference. They are not an admission receipt and do not promote any vanilla binary into mod provenance. The ladder is complete and can remain untouched as a carrier-preservation asset; it is not a newly sourced Event 006 flag.

### Existing ideology variants are not neutral substitutes

- `NAV_democratic.tga` visually follows Ikurriña geometry but is an existing ideology/route file. It cannot silently replace the no-suffix NAV base, and the asset skill requires a separate ImageGen flat reconstruction for every newly produced flag.
- `NAV_communism.tga` and `NAV_fascism.tga` are route-specific ideological designs and are excluded from the neutral compact baseline.
- `GLC_democratic.tga` contains the shielded institutional form. The official Xunta source dates the definitive shield model to 1972 and its regulation to the 1984 symbols law, so it is not safe as a neutral 1936 baseline.
- `GLC_communism.tga` is a red-star/Estreleira-style route symbol; `GLC_fascism.tga` has no bounded historical baseline attestation. Neither may become the default carrier flag.

## IW-013 Basque source and rights record

### Design and period evidence

- Official Government of the Basque Country identity manual: <https://www.euskadi.eus/contenidos/informacion/v2_simbolos/es_simboide/adjuntos/manual_id_corporativa.pdf>. The downloaded manual is a later corporate-identity publication (the PDF records the 1993/1999 identity-manual decrees), but it reproduces the historical legal basis: the provisional Government of Euskadi decree of `19 October 1936` (published `21 October 1936`, amended `24 October 1936`) and the later 1979 Statute wording. It specifies the red field, green saltire, white cross, proportions, and official Pantone references. It is historical/design evidence, not a runtime redistribution licence.
- Historical summary: <https://en.wikipedia.org/wiki/Flag_of_the_Basque_Country>. It records the Arana design in `1894`, EAJ-PNV adoption in `1895`, the whole-Basque proposal in `1933`, and adoption by the Basque Government in `1936`. Use this as corroborating chronology, not as a licence source.
- Geometry reference: <https://commons.wikimedia.org/wiki/File:Flag_of_the_Basque_Country.svg>; direct SVG <https://upload.wikimedia.org/wikipedia/commons/2/2d/Flag_of_the_Basque_Country.svg>. Commons identifies Daniele Schirmo (Frankie688) as author, the work date as `28 December 2006`, and the geometry as CC BY-SA 2.5 Generic. Local reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_basque_country_reference.svg`, SHA-256 `f282e4ea7981c707c5db8a10094e5cd3094c3e9689b384d6882cdda89c91b255`.

### Rights and runtime reading

The Commons SVG is a modern self-published reconstruction, not a period flag photograph or an original 1936 government file. A derivative that uses its exact geometry needs attribution, a link to CC BY-SA 2.5, indication of changes, and compatible ShareAlike treatment. No attribution/ShareAlike decision has been accepted for a runtime mod file. The official manual has no blanket runtime licence statement. Therefore the reference is **source/reference only**, not runtime-ready.

### Required parent decision

The recommended route is the current Basque compact contract: keep state `792` as Basque and commission a later clean, flat Ikurriña triplet from the cited design evidence, with rights/attribution recorded and a distinct ImageGen source master. The later flag worker must produce normal `82x52`, medium `41x26`, and small `10x7` TGA files, preserve the vanilla bottom-left origin/header convention, retain a master-plus-ladder comparison sheet, and provide manifest and GFX handoff evidence. Do not copy `NAV_democratic.tga` or create a local rectangle/colour-only substitute.

The only alternative is a deliberate package/design revision that identifies the compact carrier as Navarra and accepts the existing NAV ladder unchanged. This is not assumed, and it would require parent-owned package, localisation, and gameplay review; this handoff does not authorize it.

## IW-015 Galicia source and rights record

### Design and period evidence

- Official Xunta de Galicia: <https://www.xunta.gal/a-bandeira>. Accessed `2026-08-12`; the cached page states that the civil flag is three modules by two (3:2), a white field with a light/cobalt-blue diagonal from upper-left to lower-right. It expressly says there are no testimonies proving the current flag before the twentieth century, and explains the design's origin in the A Coruña Naval Command flag, later adopted by emigrants and then peninsular Galicia. This makes the plain GLC carrier ladder a plausible interwar civil baseline, but not an unqualified pre-1900 or ancient design.
- Official Xunta shield page: <https://www.xunta.gal/o-escudo>. It states that the definitive shield model was adopted by the Real Academia Galega in `1972` and regulated by the `5 May 1984` symbols law. The shielded GLC democratic variant is therefore excluded from the neutral 1936 baseline unless a later institutional route is explicitly selected.
- Historical summary: <https://en.wikipedia.org/wiki/Flag_of_Galicia>. It corroborates public white-and-blue use by `1891` and distinguishes the 1936 red-star Estreleira as a left-nationalist route symbol rather than the default civil flag.
- Geometry reference: <https://commons.wikimedia.org/wiki/File:Flag_of_Galicia.svg>; direct SVG <https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Galicia.svg>. Commons identifies Pedro A. Gracia Fajardo as author, records the first upload as `25 November 2005` (current revision `26 February 2006`), leaves the source date blank, marks the SVG as W3C-invalid, and declares Public Domain in the United States only. Local reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_galicia_reference.svg`, SHA-256 `fbdaf8a27bd279ba167a8956ce94bccee4a06257bfa4bafedf2d1560c8ec8db5`.

### Rights and runtime reading

The installed plain `GLC.tga` is a complete engine-ready vanilla carrier ladder and may remain untouched under the existing `GLC` tag. It is not a new Event 006 asset, and the vanilla game files are not a mod redistribution licence. The Commons geometry page's PD statement is jurisdiction-limited and the SVG is invalid; the official Xunta page is evidence, not a licence grant. Treat the plain ladder as **conditionally compatible carrier reuse**, not a cleared standalone Event 006 flag asset, until the parent records an explicit rights/period acceptance or commissions a separately sourced/generated flat triplet.

Do not promote `GLC_democratic`, `GLC_communism`, or `GLC_fascism` to the no-suffix carrier. If the parent elects a generated replacement rather than preserving the carrier, the later asset worker must use the plain civil geometry, not the shielded or red-star forms, and must produce a separate ImageGen source master plus complete ladder and provenance package.

## Parent-owned work still required

1. Keep central content attestation closed for both `iw_013` and `iw_015`; do not treat adapter/setup predicates, complete vanilla ladders, or this handoff as admission proof.
2. For NAV, choose explicitly between the current Basque compact route (recommended; commission a rights-aware Ikurriña triplet) and a package redesign that identifies the carrier as Navarra. Until then, NAV is blocked and no base or ideology variant may be copied or wired.
3. For GLC, explicitly accept or reject plain vanilla `GLC.tga` carrier preservation after recording the Xunta twentieth-century provenance caveat and the Commons jurisdiction/invalid-SVG caveat. Even if accepted as a carrier-preservation decision, keep standalone package admission closed until the independent country-package, portrait/source, MCP, and probability gates pass.
4. If either package receives a new flag, route the actual production through the flat-flag ImageGen workflow: source/design reference first, clean orthographic flag only, no fabric/folds/scene, full normal/medium/small ladder, TGA header/orientation validation, visible source master, comparison sheet, manifest, and parent-owned `.gfx`/gameplay wiring.
5. Re-run the independent country-package audit after the flag decision, portrait/source-rights review, and current MCP artifact-manifest repair. Do not use older 2026-08-06 source audits as current engine evidence.

## Completion and blockers

- Source/reference work: **complete for bounded review**. Official and Commons links, dates, geometry, period fit, rights caveats, installed-map anchors, and vanilla ladder hashes are recorded above.
- Runtime-ready asset production: **not performed and not claimed**. No new source PNG, processed preview, TGA, DDS, contact sheet, ImageGen output, GFX handoff, or runtime override exists for either package.
- IW-013: **blocked / needs user review** because `NAV.tga` is Navarrese while the accepted current-map identity is Basque state `792`; the Ikurriña reference has CC BY-SA 2.5 obligations and no accepted runtime triplet.
- IW-015: **conditional carrier reuse / needs user review; fail-closed for admission** because plain `GLC.tga` matches the civil geometry but the official date caveat, jurisdiction-limited Commons PD statement, and invalid SVG prevent an automatic independent flag attestation.
- Combined: **`SAFE_FLAG_ATTESTATION = NO`; no central admission or silent fallback is authorized.**

## Source and reference paths

- Current package authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_package_admission_audit_current_2026-08-12.md`.
- Prior flag source audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_flag_source_audit_2026-08-06.md`.
- Current installed-map binding: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.
- Basque reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_basque_country_reference.svg`.
- Galicia reference master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_galicia_reference.svg`.
- Canonical flag family used for visual comparison: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/contact_sheet.png`.

## Required references read

The repository `AGENTS.md`, the relevant `chaos-redux-event-assets` flag/reference/blocked-asset sections, the canonical `assets/vanilla_reference` README/CATALOG and flags family, the offline Paradox wiki pages (Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, State modding), and the installed vanilla documentation (`effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `script_collection_input.md`) were consulted before this handoff.
