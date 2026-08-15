# Event 006 IW-013 / IW-015 Historical Flag-Source Audit

## Scope and disposition

This is a bounded source and vanilla-family audit for the IW-013 NAV Basque carrier and IW-015 GLC Galicia carrier.

The audit verifies the installed vanilla flag ladders, compares their motifs with the requested circa-1940 identity, records direct historical and rights sources, and identifies the route decision needed before any replacement flag work.

No flag, GFX, gameplay, localisation, portrait, advisor, PNG, TGA, DDS, or cosmetic-tag file was created or edited in this pass.

The current disposition is **IW-013 needs_user_review / blocked for current base reuse** and **IW-015 conditional baseline accepted for review / package admission still HOLD**.

`SAFE_FLAG_ATTESTATION = NO` for the combined package because the installed NAV base family is a Navarra flag rather than a defensible compact Basque Country baseline, and the GLC baseline still carries period and rights caveats.

## Current package wiring

`docs/events/006_independence_wave/iberian_registered_packages.md` states that IW-013 reuses vanilla `NAV` with state 792 País Vasco as the compact anchor and optional states 172 Navarra and 806 Pyrénées-Atlantiques, while IW-015 reuses vanilla `GLC` with state 171 Galicia.

`common/scripted_effects/006_independence_wave_iberian_package_effects.txt` explicitly preserves the registered carriers' vanilla history, tag, flag, and leader roster.

The mod has no `NAV.tga`, `NAV_*`, `GLC.tga`, or `GLC_*` override under `gfx/flags/`, and no IW-013/IW-015 cosmetic tag or route-specific flag wiring was found.

Therefore the following are audits of the currently installed vanilla family, not approval to copy or replace any file.

## Installed vanilla evidence

The vanilla country registry maps `NAV` to `history/countries/NAV - Navarra.txt` and `GLC` to `history/countries/GLC - Galicia.txt` in `common/country_tags/00_countries.txt`.

The vanilla NAV history uses capital/state 792 but is semantically Navarra, and its base flag is a Navarrese red field with gold chain and arms motifs.

The vanilla GLC history uses capital/state 171 Galicia, and its base flag is a plain white field with a blue diagonal from the upper-left to the lower-right.

Each family has complete normal, medium, and small ladders at `82x52`, `41x26`, and `10x7` pixels under the vanilla `gfx/flags/` tree.

The normal and medium files use uncompressed 32-bit TGA with `y_origin=0` and descriptor `8` (bottom-left origin with eight alpha bits); the small files use the same vanilla family convention with descriptor `0`.

All inspected ladders are dimensionally valid, non-empty, and distinct across normal, medium, and small sizes.

Canonical normal-file hashes recorded during this audit are:

| Family | File | SHA-256 | Audit reading |
| --- | --- | --- | --- |
| NAV | `NAV.tga` | `7810f746f8ed587eac8a531a1a17137cb0ae50e5b00312f668c82768942942d9` | Navarrese red/gold chains and arms; authentic for the Navarra carrier, not the compact Basque identity. |
| NAV | `NAV_democratic.tga` | `b5e59482b7ca2a589caaae3f437698d4ed473b1c6b464bb65d2559633f594f68` | Ikurriña geometry; historically defensible for an explicitly Basque democratic/civic route. |
| NAV | `NAV_communism.tga` | `a8d8ab193a30b88ea835ffb08a5518b4e8e674db8eee70a14740f22af7c14ce0` | Ideological red/black/gold emblem; no bounded source attestation for a neutral Basque baseline. |
| NAV | `NAV_fascism.tga` | `59d65d7bd0cea6916de3b835cbfeda095347e182101dac4ce3355e496e7814e4` | Ikurriña-derived regime emblem with black swastika medallion; not a neutral Basque flag. |
| GLC | `GLC.tga` | `17d9e5f67a441bea6a77135da4cf2118535e12f4b461b1eec03ab958fff0e599` | Plain civil white/blue diagonal; strongest installed circa-1940 baseline, subject to the official date caveat below. |
| GLC | `GLC_democratic.tga` | `f0e651c2bf253588b52ee11f5625529865209491a1c9093c937a0ff458cfde3d` | Shielded institutional form; not safe as the neutral 1936 baseline because the definitive shield model is later. |
| GLC | `GLC_communism.tga` | `d73d10851afaef93df9279f62c08cc1d19517f1995aa0c1f2e79aa7534d9042a` | Red-star Estreleira-style route symbol; exclude from the default civil package. |
| GLC | `GLC_fascism.tga` | `9aca7124df1ec44ce34a53a5ef5384f63f3b94fa261e8fd7b3a3bab15ac7ab6a` | Route-specific ideological emblem; no bounded historical baseline attestation. |

The complete medium and small ladders were also hashed and visually checked; no malformed ladder or missing vanilla file was found.

## Historical and rights evidence

### IW-013 Basque Country / NAV

The [Flag of the Basque Country historical summary](https://en.wikipedia.org/wiki/Flag_of_the_Basque_Country) records the red field, green saltire, and white cross as the Ikurriña designed by Sabino and Luis Arana in 1894, adopted by EAJ-PNV in 1895, proposed for the whole Basque Country in 1933, and adopted by the Basque Government in 1936.

The [Commons geometry page](https://commons.wikimedia.org/wiki/File:Flag_of_the_Basque_Country.svg) identifies the modern vector author as Daniele Schirmo (Frankie688), with the original file dated 28 December 2006 and licensed CC BY-SA 2.5 Generic.

The direct [Basque SVG source](https://upload.wikimedia.org/wikipedia/commons/2/2d/Flag_of_the_Basque_Country.svg) is archived locally as `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_basque_country_reference.svg` with SHA-256 `f282e4ea7981c707c5db8a10094e5cd3094c3e9689b384d6882cdda89c91b255`.

The modern SVG is geometry/reference evidence only, not a period photograph and not a final runtime flag.

Any derivative that uses this exact CC BY-SA 2.5 geometry needs attribution and ShareAlike handling; that rights obligation has not been transferred into a runtime asset in this audit.

The existing vanilla `NAV_democratic.tga` visually matches the historically attested Ikurriña geometry, but the current package reuses `NAV.tga` as the default family and has no explicit route-specific cosmetic tag.

The existing vanilla `NAV.tga` is therefore not defensible as the compact state-792 Basque baseline merely because the vanilla carrier uses capital 792; it remains defensible only as a Navarra-carrier flag or an explicitly selected Navarra extension surface.

### IW-015 Galicia / GLC

The official Xunta [A bandeira](https://www.xunta.gal/a-bandeira) page documents the civil Galician flag as a 3:2 white field with a blue diagonal band from the upper-left to the lower-right, with the institutional form adding the shield at the centre.

The same official page states that there is no evidence proving the current flag existed before the twentieth century, and that the white-and-blue design derives from the flag of the Coruña Naval Command before being adopted by emigrants and later by peninsular Galicia.

This makes the installed plain `GLC.tga` a plausible interwar/circa-1940 civil baseline, but not an ancient or unqualified pre-1900 baseline; the caveat must remain in the parent package documentation.

The official Xunta [O escudo](https://www.xunta.gal/o-escudo) page records the blue field, gold chalice, silver host, and seven silver crosses and dates the definitive shield model to 1972, with regulation by the 1984 symbols law.

The shielded `GLC_democratic.tga` is consequently not safe as the neutral 1936 baseline unless the parent explicitly selects a later institutional route.

The [Flag of Galicia historical summary](https://en.wikipedia.org/wiki/Flag_of_Galicia) records public white-and-blue use by 1891 and treats the 1936 red-star `Estreleira` as a route-specific left-nationalist variant, not the default civil flag.

The [Commons geometry page](https://commons.wikimedia.org/wiki/File:Flag_of_Galicia.svg) identifies Pedro A. Gracia Fajardo as the uploader/creator of the 25 November 2005 flat SVG and marks it public domain in the United States, while warning that public-domain status may not hold outside the United States.

The direct [Galicia SVG source](https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_Galicia.svg) is archived locally as `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_galicia_reference.svg` with SHA-256 `fbdaf8a27bd279ba167a8956ce94bccee4a06257bfa4bafedf2d1560c8ec8db5`.

The archived SVG is an old flat geometry reference and is flagged as an invalid Inkscape SVG, so it is not a final runtime file; rights outside the stated public-domain jurisdiction remain unresolved.

The official Xunta pages are historical and geometric evidence, not a license grant for downloaded website artwork.

## Route and identity decision required

For IW-013, the parent must choose one of these explicit outcomes before flag attestation:

- **Basque compact route (recommended):** treat state 792 as the Basque identity and commission a later route-specific Ikurriña normal/medium/small triplet, using the sourced geometry with attribution/ShareAlike handling or a separately generated derivative whose provenance is recorded. The existing `NAV_democratic.tga` is a visual reference only and must not silently become the neutral base.
- **Navarra carrier route:** retain vanilla `NAV.tga` and revise the package identity/route contract so the compact carrier is Navarra rather than Basque Country. That would be a gameplay/design decision outside this audit and is not assumed here.

For IW-015, retaining vanilla `GLC.tga` is defensible as the plain civil interwar baseline if the parent accepts the official Xunta caveat that the current design is not proven before the twentieth century.

Do not promote `GLC_democratic.tga`, `GLC_communism.tga`, or `GLC_fascism.tga` to the default package without an explicit route decision and separate historical/rights review.

## Blockers and simplifications

1. NAV current-base identity is unresolved: `NAV.tga` is a Navarra motif, while the compact state-792 package is documented as Basque Country.
2. No route-specific cosmetic tag or flag family exists in the mod, so changing NAV without parent-owned wiring would be an unsafe silent override.
3. The Basque geometry reference is CC BY-SA 2.5; attribution and ShareAlike handling must be decided before any derivative is shipped.
4. Galicia's plain civil design has an official twentieth-century provenance caveat, and the Commons geometry reference has jurisdiction-limited public-domain language; neither is a blanket runtime license.
5. Shielded, red-star, and fascist variants are route-specific or modern/uncorroborated and remain excluded from the neutral baseline.
6. No final processed PNG preview, TGA, DDS, GFX handoff, generated replacement, contact sheet, or gameplay wiring was produced because the parent explicitly requested source audit only.
7. The current portrait-placeholder policy and absence of advisor-icon requests do not resolve the flag decisions; no portrait or advisor asset was touched.

## Validation and acceptance state

The vanilla NAV/GLC normal, medium, and small ladders were inspected for dimensions, TGA headers, alpha/origin conventions, and non-empty content.

The current mod was searched for NAV/GLC flag overrides and cosmetic tags; none were found.

The installed package documentation and scripted-effect comments were checked to confirm that vanilla flags remain intentionally preserved.

No gameplay or runtime files were modified, so final in-game validation and any future flag-generation acceptance remain parent-owned.

**Acceptance recommendation:** keep IW-013 at `needs_user_review` until the compact Basque-vs-Navarra route is explicitly chosen and a route-specific flag plan is approved; keep IW-015 at conditional base reuse with the plain civil `GLC.tga` while recording the Xunta era and rights caveats; keep combined central package attestation blocked.

## Source and handoff paths

- Historical/source manifest: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/manifest.md`.
- Basque source master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_basque_country_reference.svg`.
- Galicia source master: `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/source_masters/flag_galicia_reference.svg`.
- Current package registration: `docs/events/006_independence_wave/iberian_registered_packages.md`.
- Previous package audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_iberian_package_current_audit_2026-08-05.md`.

## Skills used

`chaos-redux-event-assets` guided the flag-source, vanilla-ladder, provenance, and fail-closed handoff boundary.
