# IW-045 Bashkiria identity, flag, and symbol research handoff

Date: 2026-08-14

Scope: non-portrait source research for Event 006 `IW-045` (`Bashkiria`, registered carrier `BSK`). No gameplay, country, localisation, GFX, spreadsheet, runtime flag, TGA, DDS, or tag files were edited. Research evidence is retained under [`docs/assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/`](../../../assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/).

## Disposition

**FAIL-CLOSED for a universal 1936 IW-045 flag.** Keep the installed vanilla BSK ideology ladder unchanged while the Event 006 country package remains unattested. The only defensible period flag found is the blue-green-white Bashkurdistan national-government flag associated with the 1918-1919 route. It cannot be silently presented as a neutral 1936 Bashkiria flag, and it must remain route-owned if used.

The Soviet Bashkir ASSR flag sequence is useful for chronology and rejection evidence, not for an independent Event 006 opening. A Soviet continuity interpretation would be an explicit Soviet/ASSR route and must not cross the Event 005 origin boundary.

## Installed vanilla BSK ladder

The installed HOI4 build contains `BSK_communism.tga`, `BSK_democratic.tga`, `BSK_fascism.tga`, and `BSK_neutrality.tga` in `gfx/flags/`, with complete 41x26 and 10x7 counterparts in `medium/` and `small/`. It has no no-suffix `BSK.tga` in any size root. All 12 files decode as opaque bottom-left-origin TGA at the standard 82x52 / 41x26 / 10x7 sizes.

The vanilla identity binding is `common/country_tags/00_countries.txt:237` (`BSK = "countries/Bashkortostan.txt"`) and `history/countries/BSK - Bashkortostan.txt:1` (capital 651/Ufa), with a 1936 democratic setup and `BSK_yakov_bykin` recruitment. This establishes the installed carrier and start-state baseline, not an independent 1936 flag provenance.

The review sheet is [`vanilla_previews/vanilla_bsk_contact_sheet.png`](../../../assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/vanilla_previews/vanilla_bsk_contact_sheet.png), and the decoded normal previews are in the same folder. The normal-file hashes are:

| Variant | Vanilla normal SHA-256 | Identity finding |
| --- | --- | --- |
| `BSK_communism` | `61924312347de9d27b8bd034c4c98505bead2d118b294ebe9680aafef503a481` | Red Soviet-style field with Bashkortostan/ASSR crest and lower blue-green-white bands; not the documented 1926-1937 ASSR reconstruction and not a neutral 1936 source. |
| `BSK_democratic` | `ea51fa0379d13920d6452f8c85009be146aa7c03b9bf900f6fede0b00fa9e000` | Blue/green/white bands plus a gold circular device; game art, not an exact 1918 plain tricolour or post-1992 blue/white/green kurai flag. |
| `BSK_fascism` | `b7392f07cdc2f99d6077036747bbf93eeb56f7e9aa79637e020a09852979a3d6` | Black/white geometric emblem; no period Bashkir state or movement attribution found. |
| `BSK_neutrality` | `c13ac4e7f5b22f515ce73d898b36c507b33e31a2cc5b7871762c69d4661b50ef` | White/red horse motif over a green patterned field; no period Bashkir state attribution found. |

These built-in ideology variants are not to be repainted, relabelled, or used as historical source evidence. In particular, the absence of a no-suffix file is not permission to create `BSK.tga`; Event 006 must use an explicit route/cosmetic family if it ever changes identity.

## Historical identity findings

### 1917-1919 Bashkurdistan / Bashkir national-government route

The [FOTW pre-Soviet Bashkirian flag page](https://www.fotw.info/flags/ru-02_h.html) identifies a green/yellow-crescent 1917 candidate and separately dates a sky-blue/green/white flag to 20 August 1918-23 March 1919, with use described across 1917-1919. It credits Jaume Ollé's 1996 research image and later vexillological redrawings. FOTW is a secondary source with an image-rights disclaimer, so its geometry is evidence rather than a runtime art licence.

The [Commons `Flag of Bashkortostan (1918).svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Bashkortostan_(1918).svg) is a 2017 CC BY-SA 4.0 flat reconstruction by GTRus. Its page description attributes the design to Bashkortostan Government Farman No. 4547. The retained source is not a period textile and must not be described as one.

The [Commons `Flag of Bashkurdistan with crescent and star.svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Bashkurdistan_with_crescent_and_star.svg) is a CC0 reconstruction by Sebirkhan described as a flag by Akhmed-Zaki Walidi Tughan. Its 1918-08-20 upload metadata is not independent period evidence. Treat the crescent/star as a conditional Bashkir Muslim or military-route reconstruction only, never as the neutral Event 006 identity.

The institutional [E-history Kazakhstan account of the Bashkir and Kazakh national movements](https://e-history.kz/en/projects/show/23366) records the 1917 Bashkir regional bureau, Central Shuro, 15 November 1917 territorial-autonomy declaration, and the Bashkir Government's political and armed institutions. It supports the national-government context but does not license any image.

**Route result:** The 1918 blue-green-white tricolour is admissible only for a deliberate Bashkurdistan restoration or national-government route. It should be labelled `historical_route_reconstruction`, not `1936 neutral flag`. The green/yellow crescent candidate is held as uncertain and is not recommended without an explicit route owner.

### Soviet Bashkir ASSR continuity

The [FOTW Bashkiria-in-the-Soviet-Union page](https://www.crwflags.com/FOTW/flags/su-ruba.html) records Bashkiria as an RSFSR autonomy from 1919 and lists flag sequences for 1926-1937, 1937-1940, and 1940-1954. It notes that the 1937 flag used Latin-script Bashkir text and that the orthography switched to Cyrillic in 1940.

The retained `research/fotw_su_bssr1925.gif` shows the red 1926-1937 Soviet design with a bordered canton, while `fotw_su_ruba2_1937.gif` and `fotw_su_ruba3_1940.gif` show later bilingual/Cyrillic inscription changes. The Commons 1937-1938 and 1938-1947 vectors are public-domain reconstructions based on Vexillographia.ru, not period source scans.

These designs are chronological context only. They do not support an independent 1936 Event 006 flag, and an ASSR/Soviet continuity route would have to carry a Soviet identity owner and reject Event 005/006 origin conflation.

### Modern Bashkortostan identity is not a 1936 baseline

The [FOTW Bashkortostan page](https://www.crwflags.com/FOTW/flags/ru-02.html) dates the current blue/white/green flag with a gold kurai flower to the 25 February 1992 adoption and discusses the 2003 proportion change. The seven-petal kurai is therefore a modern regional-state device, not a documented 1936 independent flag. Do not use the modern kurai flag as an unqualified historical baseline.

## Recommended parent contract

1. Keep `gfx/flags/BSK_*` exactly as installed and leave the carrier dormant until the existing IW-045 adapter, attestation, and origin gates pass.
2. If the parent explicitly selects a 1918 Bashkurdistan restoration route, ask the generated-art worker for a new flat orthographic master constrained to equal sky-blue/green/white horizontal stripes, with no kurai, crescent/star, lettering, modern coat of arms, fabric, folds, pole, shadows, or scene. Produce route-specific normal/medium/small ladders from that master and label the manifest `historical_route_reconstruction`.
3. If the parent selects a post-1936 Provisional Bashkir Congress or civic directorate, a generated route flag is permissible only as `alternate_history_synthesis`. It may use the 1918 palette as a documented motif and a clearly fictional civic device, but must never be described as an attested 1936 flag. ImageGen should create one clean flat master; no local primitive-shape substitute is acceptable.
4. If a Soviet/ASSR continuity route is chosen, treat the 1926-1937 flag as an explicit Soviet institutional symbol and keep it outside independent Event 006 opening semantics. Do not use it to bypass Event 005 origin separation.
5. Any future generated route package must contain the ImageGen source master, processed PNG, 82x52 / 41x26 / 10x7 bottom-left-origin TGA outputs, source/provenance manifest, native-size contact sheet, and handoff. No final asset was produced in this pass.

## Origin-separation guardrail

The parent should preserve the existing Event 006 fail-closed requirement: a future IW-045 flag route must not activate when BSK is living under Event 005/Soviet-collapse provenance (`soviet_collapse_active_origin`, `liberation_origin = liberation_origin.soviet_collapse`, or Event 005 BSK breakaway markers). The Event 005 BSK council portrait and flags remain Event 005-owned evidence and are not Event 006 assets.

## Asset outputs and blockers

- Research-only snapshots, decoded vanilla previews, and contact sheets: [`docs/assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/`](../../../assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/).
- Proposed runtime family: none while the universal route is blocked. Conditional future basenames are documented in [`gfx_handoff.md`](../../../assets/006_independence_wave/iw045_bashkiria_flags_2026_08_14/gfx_handoff.md), but no sprite or tag is registered.
- No processed runtime PNG, TGA, DDS, `.gfx` snippet, or gameplay wiring was created.
- The package remains blocked for automatic admission by the separate viability handoff because the exact Event 006 adapter/content attestation and runtime proof are absent. This symbol pass does not alter that decision.

## Validation evidence

The copied vanilla previews decode at 82x52, 41x26, and 10x7 for every ideology, and the source TGA headers use bottom-left origin descriptors (`0x08` for normal/medium with alpha bits and `0x00` for small). The research snapshots and contact sheets are retained under the workspace; no DDS conversion was attempted because no runtime asset was selected.

No commit or staging was performed.
