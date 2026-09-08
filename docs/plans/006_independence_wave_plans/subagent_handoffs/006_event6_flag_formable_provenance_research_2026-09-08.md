# Event 006 flag and formable-emblem provenance research handoff

Date: 2026-09-08

Owner: `/root/flag_emblem_research`

Scope: read-only provenance, rights, identity, era-fit, and runtime comparison for the unresolved non-portrait source rows ASSET-044 (historical/attested flag families) and ASSET-046 (formable and league flags/emblems).

Status: ASSET-044 is technically present for the audited families but remains mixed between handed-off, needs-user-review, and blocked source states. ASSET-046 remains blocked as a family because only two family-specific emblem packages exist and the shared league emblem has no accepted identity, source, or consumer. No unresolved identity is promoted by this handoff.

## Boundary and change record

This was a documentation-only audit. No runtime GFX, TGA, DDS, interface, event, country, localisation, spreadsheet, source package, or gameplay file was edited.

No external image, PDF, vector, or generated master was copied into the repository. Temporary downloads were used only for inspection and are not source handoff assets.

No flag or emblem was generated, substituted, cropped, relabelled, aliased, or promoted. No unapproved fallback was used. No commit was created by this subagent.

The exact runtime basenames remain the parent-owned names recorded below; this handoff proposes no new runtime basename.

## Evidence reviewed

The audit used the Event 006 asset prompt, the ASSET-044 and ASSET-046 registries, the formable-family registry, the prior flag and emblem provenance handoffs, the existing source manifests and contact sheets, and the canonical vanilla reference root at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`.

The relevant prior evidence is retained in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_flag_provenance_research_2026-09-05.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_formable_emblem_research_2026-09-05.md`.

The current flag source package evidence is retained in `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/`, `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk3/`, `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md`, and `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/`.

The existing formable emblem package evidence is retained in `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/`, `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/`, and `docs/assets/006_independence_wave/manifest.md`.

## Runtime and vanilla-reference comparison

### ASSET-044 targeted runtime census

The targeted unresolved-family census covered BWX, ACX, AFX, AGX, AJX, GMX, GZX, HAX, HDX, HEX, IBX, GIX, GRX, HFX, HGX, HKX, HPX, HSX, and HUX.

Each of the 19 families has the five expected names (base, `_communism`, `_democratic`, `_fascism`, and `_neutrality`) at all three target sizes, for 15 files per family and 285 files total.

Every audited file is a type-2, 32-bit TGA with the expected bottom-left descriptor and dimensions: normal 82x52, medium 41x26, and small 10x7.

All 15 files in each audited family are byte-identical to that family’s unsuffixed base at the corresponding size. This is technically complete ladder coverage, but it does not demonstrate the accepted prompt requirement for distinct ideology and route designs. The result is an audit finding only; no variant art is proposed here.

The ladders are flat and opaque in the inspected contact sheets and match the presentation and dimensions of the canonical vanilla flag family. Fine detail loss at 10x7 is expected for this consumer. No clipping or malformed ladder dimensions were observed.

The current runtime basename contract remains `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga`.

For reference, the previously recorded BWX runtime hashes are normal `56e2ebf489a7685bf108f820b6d11503a90edb564d01e5b2bd83177de52803c5`, medium `427054c8c1a699ade82815dd3f4eb22d084972483bf8b95568851e9f4494a4ae`, and small `35fefa690435c5cee66667bc5e8c09489492489c523a7584208ee9148c6d81cf`.

### ASSET-046 targeted runtime census

The current `gfx/interface/006_independence_wave/emblems/` directory contains only `independence_wave_formable_form_05.dds` and `independence_wave_formable_form_48.dds`. Both are 128x128, 32-bit uncompressed DDS files with the expected texture payload size and transparent emblem treatment.

The existing FORM-05 runtime DDS hash is `08dddf415c532570848d022b6e2391e634fd08539ba129e26db518289a594db4` and its sprite is `GFX_independence_wave_formable_form_05` in `interface/006_independence_wave_small_assets.gfx`.

The existing FORM-48 runtime DDS hash is `6cfa1b3a342f588f17b42802d189c72e6aab6f7c0e12cb3349aedde8e2ecd222` and its sprite is `GFX_independence_wave_formable_form_48` in `interface/006_independence_wave_small_assets.gfx`.

The corresponding source/raw, alpha-master, and processed-PNG hashes are recorded in the 2026-09-05 formable-emblem handoff. FORM-05 has no confirmed live consumer in the inspected source, while FORM-48 is tied to the Pacific maritime congress preparation route. Neither is a universal league mark.

The reserved shared names `gfx/interface/006_independence_wave/emblems/independence_wave_league_emblem.dds` and `GFX_independence_wave_league_emblem` are absent from the runtime and GFX registration. There is therefore no current shared league asset to compare or repair.

The vanilla faction reference family is visually and structurally separate: the canonical extracted references include 200x100 faction-logo textures and a 32x32 miniature, whereas the Event 006 family-specific emblems are 128x128 transparent UI symbols. A vanilla faction reference, League of Nations image, FORM-05 emblem, or FORM-48 emblem must not be cropped or relabelled as the missing universal league emblem.

## ASSET-044 per-row provenance, rights, and identity status

The status values below are fail-closed. `handed_off` means the previous handoff found an attributable source and usable rights note for the named base identity, not that every route alias or ideology variant is independently sourced. `needs_user_review` means the design lead is useful but rights, identity, community review, provider terms, or route ownership remain open. `blocked` means no defensible source/identity combination is available for the requested row.

| Row | Current identity and runtime state | Source and era evidence | Rights and identity disposition | Status |
|---|---|---|---|---|
| BWX | Erzya-Moksha Federal Republic; technical base and all size/variant files exist under the BWX basename contract. | The prior Soviet Mordovian ASSR 1934 flag lead is an archival lead for a different Soviet administrative identity, not a neutral Erzya-Moksha federal republic. The current generated source is `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/source_png/BWX_erzya_moksha_federal_republic_imagegen_raw.png`. | No provider/output licence or redistribution receipt is recorded for the generated master, and the map anchor remains unbound. Reusing the ASSR flag would backdate or misidentify the requested country. | blocked |
| ACX | Celtic/St Piran’s Cross base; 48 NWE suffix aliases are also present as byte-identical copies of base ladders. | St Piran’s Cross is an attributable historical design lead; the prior handoff records Commons public-domain treatment and a Flag Institute UK check. | The unsuffixed base has a documented source/rights record in the prior handoff. No independent source, route owner, or rights record exists for the 48 suffix aliases, so no suffix promotion or deletion is authorized. | base handed_off; suffixes needs_user_review |
| AFX | Walloon coq hardi base; NWE suffix aliases are byte-identical. | The prior handoff records the 1913 Walloon coq hardi design, Commons CC0 treatment, and a Wallonia Public Service check. | The unsuffixed base has an attributable source/rights record. The suffix aliases have no independent route/source/owner record and remain review-only. | base handed_off; suffixes needs_user_review |
| AGX | West Frisian provincial flag base; NWE suffix aliases are byte-identical. | The prior handoff records the provincial design and Commons public-domain treatment with a Province of Fryslân check. | The unsuffixed base has an attributable source/rights record. The suffix aliases have no independent route/source/owner record and remain review-only. | base handed_off; suffixes needs_user_review |
| AJX | Saar Territory 1920–1935 tricolour base; NWE suffix aliases are byte-identical. | The prior handoff records the period Saar Territory design, Commons public-domain treatment, and a Saarland State Chancellery check. | The unsuffixed base has an attributable source/rights record. The suffix aliases have no independent route/source/owner record and remain review-only. | base handed_off; suffixes needs_user_review |
| GMX | East Turkestan / First East Turkestan Republic candidate; current generated ladder is present and technically valid. | The Kök Bayraq is associated with the First East Turkestan Republic of 1933–1934 and the East Turkestan independence movement. Public-domain vector leads are listed below, but they are later reconstructions rather than an archival flag scan. | The Commons design references help identify the intended symbol, but they do not clear the current generated master. No ImageGen provider/output terms or redistribution receipt are recorded, and exact route/community acceptance is open. | needs_user_review |
| GZX | Dominion of Newfoundland 1904–1949 red ensign candidate; current generated ladder is present and technically valid. | The 1904–1949 Newfoundland design is period-compatible with a 1936 route. The public-domain vector lead below records the historical interval, but it is a later reconstruction and the tiny seal is necessarily simplified at 10x7. | The design reference carries a Commons public-domain treatment, but that does not license the current generated master. No provider/output terms or redistribution receipt are recorded. | needs_user_review |
| HAX | Cascadia; fictional regional identity and current generated ladder. | No single historical 1936 Cascadian state flag exists for this alternate-history identity. | This requires an accepted fictional/alternate-history route decision, final X identity ownership, palette/variant policy, and provider/output rights receipt. | needs_user_review |
| HDX | Cherokee; current generated ladder and official-context references exist. | The Cherokee Nation flag is a modern 1978/1989 design. The Cherokee Nation seal has a 1869 historical-use lead, but it is a seal identity and not a 1936 flag. | Modern official identity cannot be silently backdated into a 1936 flag. A seal or flag treatment would require a Cherokee-specific consumer and institutional/community review. The current generated master has no recorded provider/output redistribution receipt. | needs_user_review |
| HEX | Haudenosaunee / Iroquois Confederacy candidate; current generated ladder. | The Hiawatha Belt flag representation is modern, dated 2005 in the public-domain Commons record, and is not a 1936 archival flag. | It is a cultural design lead only. Community/consent review, exact identity scope, and generated-source rights remain open. | needs_user_review |
| IBX | Kachin; current generated ladder. | Public-domain Commons leads attest Kachin State or Kachin Independence Army designs from the post-war or modern period, including a 1945–1974 Kachin State interval. None supplies a 1936 Kachin flag. | The later historical lead is wrong-era for the requested route and cannot be used as a silent repair. Community identity and generated-source rights remain open. | needs_user_review |
| GIX | Wa; current generated ladder. | Available public-domain vectors are modern Wa State, United Wa State Party, or Wa National Army reconstructions from 2007–2022. They are not a 1936 flag source, and the army/state identities are distinct. | No period-matching source or provider/output redistribution receipt is recorded. The current synthesis remains review-only. | needs_user_review |
| GRX | Māori; current generated ladder. | No single period-matching flag was found that can stand for the requested broad Māori identity without choosing among iwi or later national-symbol contexts. | Iwi/community review, exact identity scope, route ownership, and generated-source rights are unresolved. | needs_user_review |
| HFX | Lakota; current generated ladder. | No single 1936 Lakota flag or federation emblem was found that would safely identify the requested route without selecting a community-specific symbol. | Community/identity review and generated-source rights are unresolved. | needs_user_review |
| HGX | Diné; current generated ladder. | The 1968 Navajo Nation flag is a modern official design and was explicitly excluded from the 1936 source requirement. | No defensible period source was found. Community review and generated-source rights remain open. | needs_user_review |
| HKX | Zapotec–Mixtec; current generated ladder. | A 2021 public-domain Zapotec vector is a modern own-work design, not a historical Zapotec–Mixtec federation flag. | It cannot establish the combined identity. Community review, exact route identity, and generated-source rights are unresolved. | needs_user_review |
| HPX | Aymara; current generated ladder. | The Wiphala is a modern 1979 design and the inspected 2022 photograph is CC BY-SA 2.0; the current package explicitly excludes it as a 1936 flag source. | No defensible 1936 flag source was found. Do not substitute the Wiphala. Community review and generated-source rights remain open. | needs_user_review |
| HSX | Muisca; current generated ladder. | The available 2016 CC0 Muisca flag is a modern own-work reconstruction without a historical attestation. | CC0 on that modern file does not establish historical identity for the requested route. Exact identity and generated-source rights remain unresolved. | needs_user_review |
| HUX | Patagonia; fictional regional identity and current generated ladder. | No single historical 1936 Patagonia-wide flag was found for this alternate-history identity. | Collision review, final X identity, route/palette policy, and provider/output redistribution receipt are unresolved. | needs_user_review |
| IW-015 GLC | Vanilla carrier used by the opening route; exact base and democratic runtime ladders exist. | The identity is technically vanilla-correct, but the opening selects `GLC_democratic`, whose shielded model is dated to later 1972/1984 context rather than a standalone clear 1936 source. | Installed vanilla binary provenance does not provide a mod redistribution grant. Preserve only conditionally under the existing vanilla-carrier policy; do not treat it as a new sourced package. | needs_user_review / conditional preserve |
| IW-043 CHU | CHU opening and later route-generated family. | Current route ladders are generated fictional/alternate-history designs, not a single attested 1936 flag. | No ImageGen provider/output terms or redistribution receipt are recorded. Route identity and final tag ownership remain open. | needs_user_review |
| IW-058 ASY | ASY opening route-generated family. | Current route ladders are generated fictional/alternate-history designs, not a single attested 1936 flag. | No ImageGen provider/output terms or redistribution receipt are recorded. Route identity and final tag ownership remain open. | needs_user_review |

The NWE base rows remain technically handoff-ready only for their unsuffixed identities under the earlier source records. The 48 suffix aliases are not independently source-backed and must not be silently promoted because byte equality is not provenance.

## ASSET-046 per-formable emblem status

The formable registry contains 48 rows. The table records the current emblem state, not a proposal to invent missing motifs. Every row other than FORM-05 and FORM-48 is absent from the current emblem runtime directory.

| Form | Formable identity | Current emblem/source status | Disposition and blocker |
|---|---|---|---|
| FORM-01 | Celtic Congress | No separate emblem package; flag work does not establish an emblem. | blocked on accepted motif, rights, consumer, and route policy. |
| FORM-02 | North Atlantic Union | No separate emblem package. | blocked on exact public identity, motif, rights, and consumer. |
| FORM-03 | Confederation of the Low Countries | No separate emblem package. | blocked on exact public identity, motif, rights, and consumer. |
| FORM-04 | Rhenish League | No separate emblem package. | blocked on exact public identity, motif, rights, and consumer. |
| FORM-05 | Mediterranean Island League | Package exists as a project-owned 128x128 transparent emblem. Raw, alpha-master, processed PNG, DDS, and sprite evidence are recorded in the prior handoff. No confirmed live consumer was found. | needs_user_review; family-specific package only. It is not a universal league substitute, and current generated-source/provider terms still require review. |
| FORM-06 | Adriatic Federation | No separate emblem package. | blocked on final X identity, motif, rights, and consumer. |
| FORM-07 | Iberian Federation | No separate emblem package. | blocked on final X identity, motif, rights, and consumer. |
| FORM-08 | Danubian Confederation | No new emblem is authorized by the present evidence; the route reuses a vanilla identity. | blocked pending parent decision on vanilla reuse and rights/consumer scope. Do not crop or relabel a vanilla faction reference. |
| FORM-09 | Balkan Federation | No separate emblem package. | blocked on final identity, motif, rights, and consumer. |
| FORM-10 | Baltic Federation | No separate emblem package. | blocked on final identity, motif, rights, and consumer. |
| FORM-11 | Cossack Host Federation | No separate emblem package. | blocked on final identity, historically attested motif, rights, and consumer. |
| FORM-12 | Volga-Ural Federation | No separate emblem package. | blocked on exact X identity, motif, rights, and consumer. Do not merge its identity with the Idel-Ural lead without parent acceptance. |
| FORM-13 | Idel-Ural | No separate emblem package. A 1918 proclamation supplies a concrete historical logo lead, but not a documented flag or cleared redistribution package. | blocked pending parent acceptance of the logo as the exact route identity, source/rights chain, and a named UI consumer. |
| FORM-14 | Siberian Federation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-15 | Northern Indigenous Confederation | No separate emblem package. | blocked on broad identity scope, community review, motif, rights, and consumer. |
| FORM-16 | Transcaucasian Federation | No new emblem is authorized by the present evidence; the route reuses a vanilla identity. | blocked pending parent decision on vanilla reuse and rights/consumer scope. |
| FORM-17 | North Caucasian Federation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-18 | Mesopotamian Federation | No separate emblem package. | blocked on exact identity, historically attested motif, rights, and consumer. |
| FORM-19 | Fertile Crescent Union | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-20 | Arabian Federation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-21 | Levantine Federation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-22 | Maghreb Union | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-23 | Saharan Confederation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-24 | West African Federation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-25 | Sahel Confederation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-26 | Kongo Basin Federation | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-27 | Great Lakes Federation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-28 | East African Federation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-29 | Horn League State | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-30 | Southern African Confederation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-31 | Indian Ocean League State | No separate emblem package. | blocked on exact identity, motif, route policy, rights, and consumer. |
| FORM-32 | Indus Federation | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-33 | Dravidian Federation | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-34 | Northeast Federation | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-35 | Himalayan Confederation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-36 | Maritime Federation (Southeast Asia) | No separate emblem package. | blocked on exact identity, motif, route policy, rights, and consumer. |
| FORM-37 | Mainland Southeast Asian Federation | No separate emblem package. | blocked on exact identity, motif, community review, rights, and consumer. |
| FORM-38 | Polynesian League State | No separate emblem package. | blocked on broad identity scope, community review, rights, and consumer. |
| FORM-39 | Melanesian Federation | Flag package evidence exists, but no separate emblem package or confirmed emblem consumer. | needs_user_review pending exact identity, motif, community review, rights, and consumer. |
| FORM-40 | Caribbean Federation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-41 | Andean Confederation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-42 | Qullasuyu-Inspired Highland Union | No separate emblem package. Modern Wiphala material is not a safe historical substitute. | blocked on exact identity/community acceptance, motif, rights, and consumer. |
| FORM-43 | Gran Colombian Federation | No separate emblem package. A primary 1821 national-arms law is a historical motif lead, not a cleared emblem asset. | blocked pending parent acceptance of the historic-inspired identity, rights chain, and a named UI consumer. Do not convert a modern flag vector into an emblem. |
| FORM-44 | Rio de la Plata Confederation | No separate emblem package. | blocked on exact identity, motif, rights, and consumer. |
| FORM-45 | Mesoamerican Federation | No separate emblem package. | blocked on broad identity scope, motif, community review, rights, and consumer. |
| FORM-46 | Northeastern Indigenous Confederation | No separate emblem package. Modern Haudenosaunee/Hiawatha Belt material is a cultural lead only and cannot establish the broad route identity. | blocked on member identity, community acceptance, motif, rights, and consumer. |
| FORM-47 | Southwestern Indigenous Compact | No separate emblem package. The Cherokee seal/flag leads do not establish the requested multi-member compact. | blocked on exact member identity, community acceptance, motif, rights, and consumer. |
| FORM-48 | Pacific Regional Federation | Package exists as a project-owned 128x128 transparent emblem and is tied to the Pacific maritime congress preparation consumer. Raw, alpha-master, processed PNG, DDS, and sprite evidence are recorded in the prior handoff. | needs_user_review; family-specific package only. It is not a universal league substitute, and current generated-source/provider terms still require review. |

## Source-safe repair and archive evidence

### FORM-13 Idel-Ural proclamation logo

The strongest new historical identity lead is the 1918 `Proclamation of Idel-Ural Republic` scan at [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Proclamation_of_Idel-Ural_Republic.png). Commons records the author as unknown, date as 1918, and the file as public-domain/ineligible, while the underlying source page is [Bulgars.ru](http://www.bulgars.ru/idur.htm).

The scan visibly contains a distinctive logo or mark above the proclamation text. The historical-symbol research at [FOTW’s Idel-Ural page](https://www.crwflags.com/fotw/flags/ru-idurh.html) identifies that mark on the 1918 proclamation as the only authentic Idel-Ural symbol found by its editor and separately states that the later blue/gold tamga flag has no record before a 1933 book.

This is useful archive evidence for a possible FORM-13 motif, not a ready-to-ship emblem. The source chain has an unknown author and no explicit archival redistribution grant beyond the Commons metadata, FOTW has a restrictive site disclaimer, and no exact UI consumer or parent acceptance is recorded. Keep FORM-13 blocked/needs-user-review. Do not crop, trace, or promote the scan in this handoff, and do not share the motif with FORM-12 without a parent identity decision.

### FORM-43 Gran Colombian arms law

The strongest new primary historical motif lead for FORM-43 is the 1821 law [El Congreso General de Colombia considerando...](https://commons.wikimedia.org/wiki/File:El_Congreso_General_de_Colombia_considerando-_Que_por_el_art%C3%ADculo_11_de_la_ley_fundamental_de_la_Rep%C3%BAblica_le_corresponde_designar_las_armas_que_deban_distinguirla_en_lo_v_(IA_elcongresogenera00colo_0).pdf), with the library item at [Internet Archive](https://archive.org/details/elcongresogenera00colo_0).

The law is a primary design record dated Rosario de Cúcuta 4 October 1821 and approved 6 October 1821. It describes the national arms using cornucopias, Colombian fasces, crossed bows and arrows, a tricolour tie, and a circumferential República de Colombia inscription.

The Commons file is marked public domain, but the Internet Archive metadata inspected for the library scan does not supply an explicit licence or rights field. This is therefore a historical motif lead with incomplete redistribution evidence, not a cleared source package. Keep FORM-43 blocked until the parent accepts the Gran Colombian historic-inspired identity, rights treatment, and exact consumer. Do not convert a modern Gran Colombia flag or CC BY-SA vector into a new emblem.

### GMX East Turkestan design references

The [Kokbayraq flag vector](https://commons.wikimedia.org/wiki/File:Kokbayraq_flag.svg) is recorded on Commons as a public-domain simple-geometry work and describes the symbol used by the East Turkestan independence movement. The [First East Turkestan Republic vector](https://commons.wikimedia.org/wiki/File:Flag_of_the_First_East_Turkestan_Republic.svg) is also marked public domain and describes the 1933–1934 republic.

These links support the intended blue field with white crescent and star identity, but both are later vector reconstructions rather than a period archive scan. They do not clear the current generated GMX source, which lacks a provider/output redistribution receipt. Keep GMX `needs_user_review`.

### GZX Newfoundland design reference

The [1904–1949 Newfoundland flag vector](https://commons.wikimedia.org/wiki/File:Flag_of_Newfoundland_(1904%E2%80%931949).svg) is marked with Commons public-domain Canada/old-assumed treatment and gives the correct historical interval. The [Dominion of Newfoundland context](https://en.wikipedia.org/wiki/Dominion_of_Newfoundland) supports the 1936 period fit.

This is a defensible design and era lead, not an archival source for the current generated raster. The seal detail is simplified at the small ladder size, and the current generated master still lacks a provider/output redistribution receipt. Keep GZX `needs_user_review`.

### Negative or wrong-era evidence that must not become repairs

The [Kachin State 1945–1974 vector](https://commons.wikimedia.org/wiki/File:Flag_of_Kachin_State_(1945%E2%80%931974).svg), modern Wa State and Wa Party vectors, 1978/1989 Cherokee flag material, the 2005 Hiawatha Belt representation, the 1979 Wiphala, and the 2016 Muisca reconstruction are useful context only. Their dates or identity scopes do not satisfy the requested 1936 historical-source gate, and their public-domain or CC labels do not license unrelated generated masters.

The [Gran Colombia 1821 coat-of-arms vector](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Gran_Colombia_(1821).svg) and related flag vectors are modern CC BY-SA reconstructions. They may corroborate a historical design discussion but must not be treated as an exact ASSET-046 emblem source.

The [1939 League of Nations emblem](https://commons.wikimedia.org/wiki/File:Emblem_of_the_League_of_Nations_(1939).svg) is not a safe universal league repair. The prior source audit records that the League of Nations never adopted an official flag/logo/emblem and that this 1939 design was a World’s Fair communication illustration. It has the wrong institutional identity for Event 006’s League of New States.

## Explicit blockers and parent decisions needed

1. Current ImageGen masters for BWX, chunk-3 families, CHU, and ASY lack provider date/output terms and a redistribution receipt. A generated raster cannot be promoted on a historical link alone.

2. BWX has no neutral 1936 identity source and its map anchor is still unbound. The Soviet Mordovian ASSR flag is a different identity and is not an approved repair.

3. The 48 NWE suffix aliases have no independent route owner, source, or rights record. Byte-identical copies do not establish route provenance, and no suffix deletion or promotion is authorized here.

4. Community and institutional identities remain unresolved for HDX, HEX, IBX, GIX, GRX, HFX, HGX, HKX, HPX, HSX, FORM-15, FORM-24 through FORM-30, FORM-32 through FORM-42, FORM-45, FORM-46, and FORM-47. Modern public-domain/CC material is not a substitute for community acceptance or period fit.

5. ASSET-046 has no accepted final X tag, public identity, motif, palette, route-variant policy, or named UI consumer for most rows. A flag package alone does not satisfy the emblem row.

6. FORM-05 and FORM-48 are family-specific packages with unresolved consumer or source-rights review; neither can serve as a universal emblem.

7. The shared league basename and sprite are reserved but absent, and no safe universal League of New States symbol was found. Vanilla faction references and League of Nations material are not authorized substitutes.

8. GLC can only be conditionally preserved as a vanilla carrier. The installed vanilla binary has no mod redistribution grant in the reviewed evidence, and its democratic shield model is later than a standalone 1936 reference.

9. The technical flag ladders currently duplicate each family’s base across ideology suffixes. The dimensions and file format are accepted, but the prompt’s distinct ideology/route-design requirement is not evidenced. Repairing that visual gap requires parent-owned identity and art decisions and is outside this provenance-only handoff.

## Exact basename and source handoff boundary

No new basename is proposed.

For ASSET-044, the existing parent-owned contract is `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga` for each final accepted X tag.

For ASSET-046, the only existing family-specific basenames are `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` and `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`, with sprites `GFX_independence_wave_formable_form_05` and `GFX_independence_wave_formable_form_48`.

The reserved but absent shared names remain `gfx/interface/006_independence_wave/emblems/independence_wave_league_emblem.dds` and `GFX_independence_wave_league_emblem`.

Because no new candidate passed the source, identity, rights, and consumer gates, this handoff intentionally contains no new source PNG, processed PNG, DDS, manifest row, contact sheet, or GFX edit.

## Final disposition

ASSET-044: the targeted runtime ladders are structurally valid and visually consistent with the vanilla flag reference family, but unresolved source/rights/identity gates remain for BWX, all generated chunk-3 families, NWE suffix aliases, CHU, ASY, and the supplemental GLC carrier. ACX, AFX, AGX, and AJX unsuffixed bases retain their prior attributable source handoff; no new promotion is made.

ASSET-046: blocked overall. FORM-05 and FORM-48 remain existing family-specific packages requiring parent review, FORM-13 and FORM-43 now have concrete historical motif leads but incomplete rights/consumer acceptance, and every other missing emblem remains blocked or needs-user-review. The universal league emblem remains explicitly blocked.

The safe next step is parent resolution of the named identities, route ownership, community/institutional review, provider redistribution evidence, GLC policy, and per-family/league consumers. Until those decisions are recorded, no source-safe repair or runtime promotion is authorized.
