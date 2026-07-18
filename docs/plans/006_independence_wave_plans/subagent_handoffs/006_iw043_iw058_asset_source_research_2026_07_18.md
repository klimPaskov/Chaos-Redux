# IW-043 / IW-058 sourced visual research handoff — 2026-07-18

## Scope and outcome

Completed source-only research for the accepted Event 006 IW-043 Middle Volga / Volga Bulgaria and IW-058 Assyria / Mosul signature packages. The work covers the ten requested cosmetic identifiers and the optional real-person portrait review. No gameplay, localisation, spreadsheet, `.gfx`, final flag, portrait, DDS, TGA, advisor asset, or report image was created.

The self-contained package is:

`docs/assets/006_independence_wave/iw043_iw058_source_research_2026_07_18/`

Files delivered:

- `README.md`
- `source_ledger.csv`
- `flag_design_dispositions.md`
- `portrait_eligibility.md`
- `gfx_handoff.md` (no runtime art produced; future identifiers only)
- `references/reference_notes.md`
- `references/urls.txt`

No source image was retained from a rights-unclear archive. The package keeps URLs and paraphrased research notes so a later producer can re-check item-level permission without mistaking a research reference for cleared art.

## Flag source conclusions

### IW-043

- `CHU_independence_wave_middle_volga_congressX`: no authentic flag found; use a modern Kazan/Volga civic congress seal and equal river geometry. Do not add medieval or ethnic shorthand.
- `CHU_independence_wave_volga_bulgariaX`: UNESCO Bolgar is a strong official heritage anchor for river, limestone, mosque/minaret, Islam, continuity, and diversity. It is not evidence of an ancient flag. Use a restrained archaeological arch/masonry motif only as a later restoration-route reference.
- `CHU_independence_wave_volga_federationX`: Tatarica’s Idel-Ural institutional history supports equal-member federal geometry, shared competencies, and religious/language equality. No copied flag.
- `VOLGA_URAL_FEDERATIONX`: later FORM12 federation; use a broader interlocking river/federal knot so it remains distinct from the CHU opening route.
- `IDEL_URAL_COMPACTX`: 1918 institutional concept is sourced, but the blue/tamga flag reconstruction in FOTW/Wikimedia is contested. If the artist mentions it, label it `reference_only_not_authentic` and do not copy the tamga.

### IW-058

- `ASY_independence_wave_national_councilX`: modern civic council with four equal guarantees; no current AUA flag, cross, winged disk, Levies badge, or ancient imperial claim.
- `ASY_independence_wave_church_compactX`: route-specific church symbols require attribution. Church of the East cross practice, Chaldean institutional identity, and Syriac Orthodox heraldry are not interchangeable. Recommended all-community version uses neutral arches/book/bridge geometry and no exclusive cross.
- `ASY_independence_wave_civic_federationX`: secular Mosul civic bridge/river geometry; no church, Levies, current national, or imperial emblem.
- `ASY_independence_wave_security_guardianshipX`: Hansard, British Library, and Newcastle sources establish a distinct 1919–1932 Levies security institution. Use abstract watchtower/river-gate geometry only; no British RAF roundel, crown, generic eagle, or un-cleared Levies badge.
- `MESOPOTAMIAN_FEDERATIONX`: UNESCO Mosul/Tigris/Nineveh and urban heritage support a modern bridge/twin-river federation. Historic Iraqi/Hashemite colors and two stars are context only; do not copy the 1921–1958 flag or turn the route into Arab monarchy or neo-Assyrian conquest.

## Real portrait conclusion

`ASY_shimun_eshai` (Mar Eshai Shimun XXIII) is identity- and period-plausible: born 1908, Church of the East patriarch from 1920, politically active and exiled in 1933. The Foundation’s circa-1920 formal photo is a possible crop reference, but the reviewed page gives no clear reuse license or stable image provenance. It remains `needs_user_review`; no image was downloaded, cropped, processed, or approved. Prefer a clearly licensed 1930–1936 archive photo if one is later found. The 1945 QDL record is too late for a baseline portrait and the LOC “Ishai d’Mar Shimun” image is the wrong person.

Do not auto-use `CHU_gerasim_ivanov`, do not use Benjamin Arsanis without the separate provenance review, and do not add any Event 006 advisor art. The eight institutional IW043/IW058 portraits can remain separately authored fictional, all-male institutional groups in canonical HOI4 style.

## Next producer handoff

1. Flag artist should read `flag_design_dispositions.md` and create flat, clean, non-fabric ImageGen flags. The artist should preserve each item’s distinction and include the attribution caveats in the generation manifest.
2. For the Idel-Ural compact, include an explicit note that the tamga reconstruction is contested and was not copied.
3. For church and security routes, record the chosen institution and symbol disposition before generation. No generic cross, British/Levies badge, or modern national flag is acceptable without an item-level review.
4. If a real Mar Eshai image is proposed, producer must supply the exact source file, permission/license, native crop box, source hash, and a separate reviewer approval before the native portrait pipeline or DDS conversion.

## Remaining blockers

- No clear redistribution license was located for the Mar Eshai 1920 Foundation image or the Newcastle Levies photograph.
- No historically attested 1918 Idel-Ural flag geometry was located; the common blue/tamga SVG is a modern contested reconstruction.
- Modern Assyrian movement/flag archive material is attribution-sensitive and must not be copied directly; the 1973 AUA design is anachronistic for the Event 006 baseline.
- No direct source supports a universal Assyrian/Chaldean/Syriac/Aramean church emblem; the inclusive council/civic designs should stay abstract and modern.
