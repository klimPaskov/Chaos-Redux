# IW-049 BWX Erzya–Moksha symbol research handoff

Date: 2026-08-15.

Scope: read-only identity, map-binding, flag-provenance, rights, and period-fit research for Event 006 IW-049 BWX.

This handoff does not create or modify runtime TGA, DDS, PNG, GFX, gameplay, central-admission, Join, localisation, or map files.

## Disposition

Status: `blocked` for acceptance as a historically sourced neutral 1936 BWX flag.

The existing BWX ladder is technically present and marked `handed_off` by the earlier asset package, but it is not defensible as an attested 1936 Erzya–Moksha federal flag.

The current package cites only Erzya and Moksha Wikipedia pages as motif references and labels the output a “historically grounded federal synthesis.”

No primary or official source reviewed here attests a separate Erzya–Moksha federal state flag in 1936.

The only directly dated 1934 flag source found is the Mordovian ASSR state flag, which is Soviet and therefore does not match a neutral Erzya–Moksha Federal Republic without an explicit identity-route decision.

The safest non-Soviet direction is a clearly labelled period civic synthesis from documented Erzya/Moksha textile and embroidery motifs, but that remains a generated alternate-history design and needs parent acceptance after the identity and map gates close.

## Current BWX identity and runtime surfaces

The authoritative current project identity is `BWX = Erzya-Moksha Federal Republic`, with the same name and adjective for the neutral, democratic, communist, and fascist localisation variants.

The identity is a Chaos Redux Event 006 federal synthesis, not evidence that a historical independent federal government existed in 1936.

Repository identity and shell evidence:

- `common/country_tags/006_independence_wave_countries.txt:32` registers `BWX = "countries/006_independence_wave_BWX.txt"` for IW-049.
- `common/countries/006_independence_wave_BWX.txt` contains only eastern-European graphical cultures and the map colour `rgb { 154 84 76 }`.
- `history/countries/BWX - Erzya-Moksha Federal Republic.txt` is a neutral start shell with `neutrality = 100`; its comments defer territory, capital, politics, leaders, forces, ideas, focus, and AI to formation-time logic.
- `localisation/english/006_independence_wave_countries_l_english.yml:275-290` names the country “Erzya-Moksha Federal Republic” and the adjective “Erzya-Moksha”.
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_08_06.json:260-262` confirms the installed BWX identity and history-file binding.

The current gap-map authority explicitly says that the shell and flag ladder do not prove package admission, sourced identity, or a complete runtime adapter.

`common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:4-5` also keeps IW-049 unbound at the planner level.

The current central adapter, attestation, preflight, and deterministic Join surfaces intentionally exclude IW-049.

## Current map binding and host gate

The installed-map audit is dated 2026-07-14 and records 1,081 vanilla state files with IDs 1 through 1,081, no Chaos Redux state overrides, and no map replacement path.

The binding authority row is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`:

```text
IW-049 | Mordovia | BWX | automatic_pool_ready_if_unique_state_exists | disabled_no_unique_current_state | unbound | ... | RG-MORDOVIA | ... | unbound_current_map | ... | Not selectable: no authoritative current-map binding. | Mordovia or Penza map group, current-map split required
```

`docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:96` defines `RG-MORDOVIA` with no current state claim and requires a unique anchor plus a protected host remnant.

The installed vanilla localisation has `STATE_255: "Penza"` and no `Mordovia` state name.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/255-Penza.txt` defines state 255 as Penza, owned and cored by `SOV` in 1936, with a broad province list.

Neighbouring current localisation names include Kazan (249), Ulyanovsky (250), Ryazan (254), Chuvashia (256), Tambov (257), and Voronezh (260); none is an accepted BWX anchor.

Do not silently bind BWX to state 255 Penza, state 256 Chuvashia, state 399 Udmurtia, state 397 Komi, state 574 Yakutia, or state 564 Buryatia.

The accepted specification explicitly requires a Mordovia or Penza current-map split and a host-survival witness before any state transfer or country admission.

Map disposition: `blocked` until an exact installed-state split, capital choice, protected former-host state, and runtime reservation witness exist.

## Existing BWX flag ladder audit

The existing package is `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/`.

Its manifest, validation JSON, and hashes describe a complete normal/medium/small ladder, but they do not establish historical adoption or source rights for the design.

| Surface | Path | SHA-256 | Evidence |
| --- | --- | --- | --- |
| ImageGen source master | `source_png/BWX_erzya_moksha_federal_republic_imagegen_raw.png` | `1bc5d57fe761acbad7ca35f2a9f20c04f0b84babdac6c097d6b2c22ec52a94ac` | 1586x992 source PNG; provider/source date and licence are not recorded. |
| Prompt | `prompts/BWX_flag_imagegen_prompt.txt` | `4cf3db65a086bf8491bf5e894f63df6674e13772406ff7b690b9a32c835f3b3f` | Calls for a red/white/black flag and sun/rosette motifs and cites only Erzya/Moksha Wikipedia pages. |
| Processed master | `processed_png/BWX_flat_master_820x520.png` | `2c6694238a9497fdf4d2df765eb6b46b5d5d1a22323cd95e5d700030a14c7c13` | 820x520 flattened source. |
| Normal preview | `processed_png/normal/BWX.png` | `5fd0f1a0572c907d6fceeb249f9dc5eb3573c990ff4a7ad600b4147e9c1ec38c` | 82x52. |
| Medium preview | `processed_png/medium/BWX.png` | `1b3d504f497fb17a3624cd5fad74de466f016a4ab4553c66b876472e12f8ddee` | 41x26. |
| Small preview | `processed_png/small/BWX.png` | `e2d6c2f7f54d2fa41a4d18a57a946553355cdf8307dd0890dc004b0d5e4c3e23` | 10x7. |
| Runtime normal | `gfx/flags/BWX.tga` | `56e2ebf489a7685bf108f820b6d11503a90edb564d01e5b2bd83177de52803c5` | 82x52, type-2 32-bit, bottom-left origin, 17,074 bytes. |
| Runtime medium | `gfx/flags/medium/BWX.tga` | `427054c8c1a699ade82815dd3f4eb22d084972483bf8b95568851e9f4494a4ae` | 41x26, type-2 32-bit, bottom-left origin, 4,282 bytes. |
| Runtime small | `gfx/flags/small/BWX.tga` | `35fefa690435c5cee66667bc5e8c09489492489c523a7584208ee9148c6d81cf` | 10x7, type-2 32-bit, bottom-left origin, 298 bytes. |

The package copies under `final_tga/BWX_normal_82x52.tga`, `final_tga/BWX_medium_41x26.tga`, and `final_tga/BWX_small_10x7.tga` match the runtime hashes.

The current flag is a red/white/black horizontal tricolour with a large central red-and-white rosette or sun-like device enclosed by a black ring and additional geometric motifs.

The package calls this geometry “historically grounded Erzya-Moksha synthesis,” but it supplies no dated flag, archive, heraldic standard, or institutional adoption record for the red/white/black field, central device, black ring, or detailed outer motifs.

The black lower field is not supported by the cited Wikipedia links as a documented 1936 flag field.

The package has broad source and ladder contact sheets, but there is no BWX-specific historical source contact sheet or period source file in the package.

The engine-facing basename remains `BWX` with the ordinary lookup paths `gfx/flags/BWX.tga`, `gfx/flags/medium/BWX.tga`, and `gfx/flags/small/BWX.tga` if and when the parent accepts a replacement.

No new `.gfx` definition is needed for flags, and this research tranche proposes no filename change.

## Period and symbol evidence

### Primary dated institutional evidence

The Russian Presidential Library records an official archival flag sketch:

- [PRLib item 1417941](https://www.prlib.ru/item/1417941) — “Sketch of the State Flag of the Mordovian ASSR, approved at the First Congress of Soviets of the Mordovian ASSR on 27 December 1934,” sourced to the Central State Archive of the Republic of Mordovia, fond R-175, inventory 1, file 4.
- [PRLib item 1418019](https://www.prlib.ru/item/1418019) — “Resolution on the state emblem and flag of the Mordovian ASSR, approved at the First Congress of Soviets of the Mordovian ASSR,” dated 27 December 1934, sourced to the Central State Archive of the Republic of Mordovia, fond R-175, inventory 1, file 6, folios 236 and 236 verso.

The Presidential Library page says the electronic copy comes from the Central State Archive of the Republic of Mordovia and that the item is available only in electronic reading rooms.

The archive scan licence or redistribution terms are not stated on the public item page, so these pages are design-reference citations, not cleared source pixels.

### Period flag description and uncertainty

[Russian Centre of Vexillology and Heraldry, Mordovia flags](https://vexillographia.ru/russia/subjects/mordovia.htm) quotes the 27 December 1934 resolution as a scarlet/red 1:2 flag with gold crossed hammer and sickle in the upper hoist, gold `МАССР` above it, and the slogan “Workers of all countries, unite!” in Russian, Moksha, and Erzya in the upper fly.

The same page says the surviving Saransk archive drawing uses Cyrillic lettering and notes that some sources show a simpler 1930s version; it presents the simplification as an unresolved possibility rather than a settled second standard.

This is strong period evidence for the Soviet Mordovian ASSR flag, but it is not neutral and it is not evidence for an independent Erzya–Moksha Federal Republic.

The page is a secondary research source and no pixel-redistribution licence was established.

### Public-domain derivatives and rights limits

Wikimedia Commons provides public-domain metadata for period references, but these are derivatives or reconstructions and should not replace the archive record:

- [Flag of Mordovian ASSR (1934–1937)](https://commons.wikimedia.org/wiki/File:Flag_of_Mordovian_ASSR_(1934-1937).svg) — Commons metadata says Public domain, artist Sshu94, with Vexillographia as credit; the description contains a “Moldavian” typo and should not be treated as the primary identity authority.
- [Flag of Mordovian ASSR (1934–1937), Variant 2](https://commons.wikimedia.org/wiki/File:Flag_of_Mordovian_ASSR_(1934-1937)_(Variant_2).svg) — Commons metadata says Public domain, artist Helgo13, credit “Constitution of Mordovian ASSR”; variant status and exact historical usage remain uncertain.
- [Emblem of the Mordovian ASSR (1934–1937)](https://commons.wikimedia.org/wiki/File:Emblem_of_the_Mordovian_ASSR_(1934-1937).jpg) — Commons metadata says Public domain, dated 1934, with artist/source “ЦГА Республики Мордовия. Ф. Р-175. Оп. 1. Д. 4.” and a credit link to the former e-mordovia archive exhibition.

The Commons metadata is a rights lead for the derivative files, not proof that a new BWX design may copy Soviet insignia or that the archive scan itself is cleared.

### Erzya and Moksha identity and period-fit evidence

- [Fenno-Ugria: Erzya](https://fennougria.ee/en/peoples/mordvins/erzya/) records Erzya territory across eastern Mordovia and neighbouring oblasts, a standardised Erzya written language completed in 1925, the Mordovian region in 1928, autonomous oblast in 1930, and ASSR in 1934.
- [Fenno-Ugria: Moksha](https://fennougria.ee/en/peoples/mordvins/moksha/) records Moksha territory in southern and western Mordovia plus Penza and Saratov oblasts, and a standardised Moksha written language completed in 1933.
- [M.A. Castrén Society: Symbolism of Mordvin clothing](https://www.ugri.net/in-english/cultures/mordvins/symbolism-of-mordvin-clothing/) dates detailed descriptions of Mordvin clothing to the 1770s and discusses Erzya/Moksha white tunics, embroidery, family or ownership signs, star and cross motifs, animal motifs, and continuity into the 1930s.
- [Rogachev and Karabanova, “Ethnic Symbols of the Finno-Ugrians and Its Functions,” Finno-Ugric World, vol. 16 no. 4 (2024)](https://journals.rcsi.science/2076-2577/article/view/267351) cites A. O. Heikel’s 1899 recording of Mordvin ornament terms and describes eight-point rosettes, crosses, rhombi, stars, black dots on red embroidery, and protective/family-sign functions.

These sources support period-valid textile and ornament motifs, not a pre-1936 national flag.

They also show that a rosette, cross, rhombus, or geometric sign may have ritual, family, ownership, or garment-protection meanings rather than federal-state ownership.

Do not call a traditional embroidery motif a historical state emblem without an additional institutional source.

### Modern flag excluded from 1936

[Russian Centre of Vexillology and Heraldry](https://vexillographia.ru/russia/subjects/mordovia.htm) dates the modern Mordovia flag to a 30 March 1995 law, with maroon, white, and dark-blue bands and a maroon eight-point solar rosette, and records a 20 May 2008 proportion amendment.

The modern 1995/2008 flag is postwar and must not be backdated to 1936.

It may explain why a modern rosette appears in contemporary regional references, but it cannot serve as the BWX 1936 neutral flag source.

## Candidate comparison

| Candidate | Period fit | Identity fit | Rights/provenance | Disposition |
| --- | --- | --- | --- | --- |
| 1934 Mordovian ASSR archival flag | Exact prewar date and official institutional adoption; valid at the 1936 start date. | Soviet ASSR, not a neutral Erzya–Moksha Federal Republic; contains hammer/sickle and multilingual Soviet slogan. | PRLib archive record is authoritative for date and source, but public scan rights are unclear; Commons derivatives are marked Public domain but have variant/reconstruction uncertainty. | `historical_reference_only`; blocked as the neutral BWX runtime flag unless the parent explicitly changes the route identity to a Soviet successor. |
| Period civic synthesis from documented Erzya/Moksha textile motifs | Motifs are documented from 1770s descriptions, 1899 field recording, and continuity into the 1930s. | Compatible with a fictional federal civic route if explicitly framed as a synthesis shared by Erzya and Moksha; not an attested flag. | Source text and citations are usable as research references; no source pixels should be copied. New generated art would need a separate prompt, source PNG, manifest, and rights/provenance entry. | `needs_user_review`; only viable next design direction after parent identity/map acceptance and separate generated-art approval. |
| Existing BWX ImageGen red/white/black rosette ladder | The motifs are broadly period-plausible but the exact field, ring, and composite rosette geometry are not sourced to 1936. | Federal synthesis label fits the fictional route, but “historically grounded” is too strong without a documented design reference. | Source PNG and prompt hashes exist; provider rights, generation date, and source licence are not recorded. | `blocked` as a historically sourced neutral flag; retain as evidence only and do not describe it as attested history. |
| Modern Republic of Mordovia 1995/2008 flag | Fails 1936 era fit. | Modern Mordovia identity, not the Event 006 federal route. | Modern official design dates are clear, but this is irrelevant to period acceptance. | `rejected` for the 1936 flag; do not backdate or reuse its solar rosette as proof of a 1936 state emblem. |

## Acceptance gates for any future BWX flag package

1. Resolve the exact installed current-map split, anchor, capital, and former-host survival witness for `RG-MORDOVIA`.
2. Confirm that the parent wants a fictional federal civic synthesis rather than a Soviet Mordovian ASSR successor route.
3. If the civic synthesis route is accepted, describe it as generated alternate-history art grounded in documented Erzya/Moksha motifs, never as an attested historical flag.
4. Record the exact symbol ownership distinction: textile/family/ritual motif versus federal state emblem.
5. Preserve the 1934 ASSR flag and decree as cited historical references only; do not copy Soviet lettering or insignia without an explicit route decision.
6. Establish generated-art provenance and applicable rights terms before accepting the existing ImageGen source or commissioning a replacement.
7. After and only after these gates close, the asset owner may produce a new source master and complete the normal/medium/small ladder under the unchanged runtime basename `BWX`.

## Handoff and simplifications

No ImageGen call, TGA/DDS/GFX creation, runtime wiring, gameplay edit, map edit, central-admission edit, or Join edit was performed.

No new source image was copied into the repository because the archive scan licence is unclear and the parent explicitly requested read-only research.

The existing runtime ladder remains untouched and should not be promoted from “handed off” to “historically sourced neutral flag” on the basis of this tranche.

The final disposition is intentionally fail-closed pending the map anchor, identity-route decision, and source/rights gate.
