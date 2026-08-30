# Event 006 non-portrait asset source and rights research

Date: 2026-08-30.

Scope: read-only source, provenance, era-fit, basename, and release-blocker research for Event 006 Independence Wave non-portrait assets requested by the parent agent.

This handoff covers ASSET-046 formable emblems, BWX, the 17-row chunk-3 flag package, the AEX basename collision, Northern/Western Europe ideology aliases, and broad flag-package source metadata gaps.

Character portraits and portrait-source files are outside this handoff and remain owned by `chaosx_portrait_creator`.

## Disposition at a glance

| Surface | Current disposition | What is safe to do now | Required next decision |
| --- | --- | --- | --- |
| ASSET-046 formable flags and emblems | `blocked` for the unresolved rows; two emblem files are technically complete | Preserve the two admitted emblem files and the existing researched flag packages; do not invent generic emblems | Fix each unresolved formable's final tag, public identity, motif/ownership, palette, route variant, and stable UI consumer before producing more emblems |
| BWX Erzya-Moksha Federal Republic | `blocked` as a historically sourced neutral 1936 flag | Retain the existing ladder as evidence-only; use the cited 1934 Soviet material and Erzya/Moksha motif research as references | Choose a Soviet successor route or explicitly approve a generated alternate-history civic synthesis after map and identity gates close |
| Chunk-3 flags | `handed_off` technically for GTX, GYX, and HCX; `needs_user_review` for the other fourteen | Keep all source masters and ladders in their package; do not describe generated output as rights-cleared or historically attested where it is not | Record provider provenance and reference-file licence details, then obtain the required scope, era, community, institutional, and small-size approvals |
| AEX basename | `hold` pending cross-event ownership resolution | Leave Event 5's global AEX files untouched and do not create an Event 006 AEX file | Choose a scope-aware NWE validator or separately review a cross-event tag migration |
| NWE ideology aliases | `hold` / unapproved alias quarantine | Keep the four unsuffixed ACX, AFX, AGX, and AJX ladders; do not wire the 48 aliases as Event 006 route art | Remove the aliases or document an accepted route-to-filename contract after the AEX policy is resolved |
| Broad generated flag metadata | `needs_user_review` | Treat absent row-level licence, author, archive, and source-date fields as unknown, never as public domain | Add per-row source/rights/date records before calling historically grounded packages release-ready |

## Authority and method

The parent asset prompt is `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md`.

The family-level request is `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`.

The current package authority is `docs/assets/006_independence_wave/manifest.md` and the package manifests named in the sections below.

The latest technical audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_assets_audit_current_2026-08-29.md`.

The current source-repair note is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asset_source_repairs_2026-08-29.md`.

The canonical HOI4 reference library used for the asset-class comparison is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`, especially its `flags/normal`, `flags/medium`, `flags/small`, and event-art catalogues.

No source image was downloaded, copied, generated, cropped, processed, converted, or promoted during this tranche.

No GFX, gameplay, country, event, localisation, or runtime asset file was edited.

The existing source files, processed previews, final TGAs, and DDS files listed here are cited for auditability only; their presence does not by itself clear source rights, historical adoption, identity fit, or package admission.

## ASSET-046 formable flags and emblem coverage

The fixed naming contract remains `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_01.dds` through `independence_wave_formable_form_48.dds`, with sprites `GFX_independence_wave_formable_form_01` through `GFX_independence_wave_formable_form_48`.

The league contract remains `gfx/interface/006_independence_wave/emblems/independence_wave_league_emblem.dds` with sprite `GFX_independence_wave_league_emblem`.

The current consolidated registry is `interface/006_independence_wave_small_assets.gfx`.

Only these two formable emblem textures currently exist in the runtime registry:

| Formable | Source and processed preview | Runtime texture | Sprite | Size | SHA-256 | Package authority |
| --- | --- | --- | --- | --- | --- | --- |
| FORM-05 Mediterranean Island League | `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/source_png/emblems/independence_wave_formable_form_05_alpha_master.png`; `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/processed_png/emblems/independence_wave_formable_form_05.png` | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds` | `GFX_independence_wave_formable_form_05` | 128x128 | `08DDDF415C532570848D022B6E2391E634FD08539BA129E26DB518289A594DB4` | `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md` |
| FORM-48 Pacific Regional Federation | `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/source_png/emblems/independence_wave_formable_form_48_alpha_master.png`; `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/processed_png/emblems/independence_wave_formable_form_48.png` | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds` | `GFX_independence_wave_formable_form_48` | 128x128 | `6CFA1B3A342F588F17B42802D189C72E6AAB6F7C0E12CB3349AEDDE8E2ECD222` | `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/manifest.md` |

FORM-01 KCX, FORM-02 NUX, FORM-03 LCX, and FORM-04 RLX have researched/generated flag packages, but they do not have dedicated ASSET-046 formable-emblem DDS files in the current runtime registry.

FORM-05 has ARX, ASX, and MIX route flags and one admitted `form_05` emblem.

FORM-48 has PFX as its federation flag and one admitted `form_48` emblem; HBX is its California carrier flag and is not a second formable emblem.

FORM-06 through FORM-47 and the league emblem row remain absent by authority, not as orphaned textures.

The FORM-48 package manifest still says sprite registration is pending, but the current consolidated registry contains `GFX_independence_wave_formable_form_48`; treat the consolidated registry as the live path and the package wording as documentation drift.

The unresolved rows still require a final gameplay tag, final public identity, verified historical or explicitly alternate-history motif, source or ownership record for historical/community symbols, approved palette, route variants, and the exact UI consumer before asset production.

Do not fill missing rows with a generic seal, a copied vanilla emblem, a modern regional flag, or an unreviewed league symbol.

### Existing source and rights evidence for the two admitted emblems

The FORM-05 package describes ARX and ASX historical research using link-only institutional evidence and Commons design aids, while MIX and the emblem are original generated designs.

The FORM-05 package records the [Regione Autonoma della Sardegna Four Moors history](https://www.regione.sardegna.it/regione/identita-visiva/emblemi-istituzionali/storia-dello-stemma) as official link-only evidence and the [Traditional flag of Sardinia](https://commons.wikimedia.org/wiki/File:Traditional_flag_of_Sardinia.png) as a CC0 geometry aid.

The FORM-05 package records the [Italian Ministry of Culture catalog object 0100215963 / S.015](https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/0100215963) as CC BY 4.0 metadata with no catalog image copied, the [Archivio di Stato di Palermo 1848 decrees](https://digitalibrary-saassipa.cultura.gov.it/entities/archivalmaterial/20749410-4367-4365-9f75-33392164d6ae) as all-rights-reserved link-only evidence with no scan copied, and the [1848 Sicilian flag Commons file](https://commons.wikimedia.org/wiki/File:Flag_of_Sicilian_Kingdom_1848.svg) as a CC BY-SA 4.0 layout aid.

The FORM-48 package records [California Government Code section 420](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?article=&chapter=2.&division=2.&lawCode=GOV&part=&title=1.), the [California State Capitol Museum flag chronology](https://capitolmuseum.ca.gov/state-symbols/flag/), and [California State Parks flag history](https://www.parks.ca.gov/?page_id=24644) as link-only factual references.

The FORM-48 package records the [California Commons reference](https://commons.wikimedia.org/wiki/File:Flag_of_California.svg) as a public-domain visual reference with an official-insignia caveat, and records [Hawaii Revised Statutes section 5-19](https://data.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/HRS0005/HRS_0005-0019.htm), the [Federated States of Micronesia Code flag description](https://www.fsmlaw.org/fsm/code/title01/t1ch5_2014.html), and the [Pacific Community media page](https://www.spc.int/media) as link-only conceptual/legal research.

Those package records are sufficient to preserve the two existing emblem deliveries as documented generated art, but they do not authorize inventing the absent formable rows or silently treating all 48 rows as complete.

### ASSET-046 handoff

No new ASSET-046 basename is proposed in this tranche.

The parent may wire only the two stable existing sprites after checking their consumer ownership and the consolidated GFX registry.

The next asset owner needs an accepted formable identity/route matrix before creating any additional emblem source, preview, DDS, or contact sheet.

## BWX Erzya-Moksha Federal Republic

Disposition: `blocked` as a historically sourced neutral 1936 flag.

`metadata/flag_validation.json` marks the existing ladder `handed_off` as a technical package state, but the dated IW-049 symbol research retains a release block because no reviewed source attests a separate neutral Erzya-Moksha federal flag in 1936.

The authoritative research handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw049_bwx_symbol_research_2026_08_15.md`.

### Existing BWX files and checksums

The current package is `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/`.

| Surface | Path | SHA-256 | Evidence state |
| --- | --- | --- | --- |
| ImageGen source master | `source_png/BWX_erzya_moksha_federal_republic_imagegen_raw.png` | `1bc5d57fe761acbad7ca35f2a9f20c04f0b84babdac6c097d6b2c22ec52a94ac` | Provider/source date and licence are not recorded |
| Prompt | `prompts/BWX_flag_imagegen_prompt.txt` | `4cf3db65a086bf8491bf5e894f63df6674e13772406ff7b690b9a32c835f3b3f` | Requests red/white/black and sun/rosette motifs from Erzya/Moksha context pages |
| Processed master | `processed_png/BWX_flat_master_820x520.png` | `2c6694238a9497fdf4d2df765eb6b46b5d5d1a22323cd95e5d700030a14c7c13` | Flattened review master |
| Normal preview | `processed_png/normal/BWX.png` | `5fd0f1a0572c907d6fceeb249f9dc5eb3573c990ff4a7ad600b4147e9c1ec38c` | 82x52 review output |
| Medium preview | `processed_png/medium/BWX.png` | `1b3d504f497fb17a3624cd5fad74de466f016a4ab4553c66b876472e12f8ddee` | 41x26 review output |
| Small preview | `processed_png/small/BWX.png` | `e2d6c2f7f54d2fa41a4d18a57a946553355cdf8307dd0890dc004b0d5e4c3e23` | 10x7 review output |
| Runtime normal | `gfx/flags/BWX.tga` | `56e2ebf489a7685bf108f820b6d11503a90edb564d01e5b2bd83177de52803c5` | 82x52 type-2 32-bit bottom-left-origin TGA |
| Runtime medium | `gfx/flags/medium/BWX.tga` | `427054c8c1a699ade82815dd3f4eb22d084972483bf8b95568851e9f4494a4ae` | 41x26 type-2 32-bit bottom-left-origin TGA |
| Runtime small | `gfx/flags/small/BWX.tga` | `35fefa690435c5cee66667bc5e8c09489492489c523a7584208ee9148c6d81cf` | 10x7 type-2 32-bit bottom-left-origin TGA |

The package copies `final_tga/BWX_normal_82x52.tga`, `final_tga/BWX_medium_41x26.tga`, and `final_tga/BWX_small_10x7.tga` match the runtime hashes above.

The current basename remains `BWX` with `gfx/flags/BWX.tga`, `gfx/flags/medium/BWX.tga`, and `gfx/flags/small/BWX.tga` if and when an approved replacement is produced.

### Reviewed BWX source, rights, and era evidence

The [Russian Presidential Library item 1417941](https://www.prlib.ru/item/1417941) records a sketch of the Mordovian ASSR state flag approved at the First Congress of Soviets of the Mordovian ASSR on 27 December 1934, sourced to the Central State Archive of the Republic of Mordovia, fond R-175, inventory 1, file 4.

The [Russian Presidential Library item 1418019](https://www.prlib.ru/item/1418019) records the decree on the Mordovian ASSR state emblem and flag approved at the same congress, sourced to fond R-175, inventory 1, file 6, folios 236 and 236 verso.

The Presidential Library material is strong dated period evidence for a Soviet Mordovian ASSR flag, but the public item pages do not state a scan licence or redistribution permission.

The [Russian Centre of Vexillology and Heraldry Mordovia page](https://vexillographia.ru/russia/subjects/mordovia.htm) describes the 1934 flag as a scarlet/red flag with Soviet hammer-and-sickle, gold `МАССР`, and multilingual Soviet slogan elements, and separately dates the modern Mordovia flag to 1995/2008.

The 1934 ASSR flag therefore has period fit but fails identity fit for a neutral Erzya-Moksha Federal Republic unless the parent explicitly changes the route to a Soviet successor.

The [Commons Mordovian ASSR 1934–1937 reconstruction](https://commons.wikimedia.org/wiki/File:Flag_of_Mordovian_ASSR_(1934-1937).svg) is marked public domain with Sshu94 credited and Vexillographia cited, while the [Variant 2 file](https://commons.wikimedia.org/wiki/File:Flag_of_Mordovian_ASSR_(1934-1937)_(Variant_2).svg) is marked public domain with Helgo13 credited; their derivative/variant status does not clear a neutral BWX identity.

The [Commons 1934 Mordovian ASSR emblem](https://commons.wikimedia.org/wiki/File:Emblem_of_the_Mordovian_ASSR_(1934-1937).jpg) is marked public domain and cites the Central State Archive of the Republic of Mordovia, but it remains Soviet emblem evidence rather than a neutral federal source.

The [Fenno-Ugria Erzya page](https://fennougria.ee/en/peoples/mordvins/erzya/) and [Fenno-Ugria Moksha page](https://fennougria.ee/en/peoples/mordvins/moksha/) support the two peoples' geography and language context, including 1925 Erzya and 1933 Moksha standardisation, but neither attests a 1936 federal flag.

The [M.A. Castrén Society clothing-symbolism page](https://www.ugri.net/in-english/cultures/mordvins/symbolism-of-mordvin-clothing/) and [Rogachev and Karabanova, “Ethnic Symbols of the Finno-Ugrians and Its Functions”](https://journals.rcsi.science/2076-2577/article/view/267351) support period-valid embroidery, rosette, cross, rhombus, star, and family/protective motifs, but they describe textile and ritual symbolism rather than state ownership.

The existing red/white/black tricolour, central rosette, black ring, and outer geometry are not attested by those sources as a 1936 federal flag.

### BWX candidate dispositions

| Candidate | Era fit | Identity fit | Rights/provenance | Disposition |
| --- | --- | --- | --- | --- |
| 1934 Mordovian ASSR archival flag | Exact prewar date and official adoption | Soviet ASSR, not a neutral Erzya-Moksha Federal Republic | Archive scan terms unclear; Commons derivatives have public-domain metadata but reconstruction/variant uncertainty | `historical_reference_only`; blocked for current neutral BWX |
| Period civic synthesis from documented Erzya/Moksha textile motifs | Motifs are documented into the 1930s | Compatible only with an explicitly fictional federal route | Text sources can be cited; new generated art needs its own prompt, source, date, and rights record | `needs_user_review`; viable only after identity/map approval |
| Existing BWX ImageGen ladder | Broad motifs are period-plausible, exact flag geometry is not sourced | Fictional federal label fits, “historically grounded” does not | Source/prompt hashes exist, provider date/licence absent | `blocked`; evidence-only |
| Modern Republic of Mordovia 1995/2008 flag | Fails the 1936 era gate | Modern regional identity, not BWX route | Dates are clear but irrelevant to current route | `rejected`; do not backdate or reuse as proof |

The installed map/package gate is also open: the current reservation record has no authoritative Mordovia state split, anchor, capital, or protected former-host witness.

Do not silently bind BWX to Penza 255, Chuvashia 256, Udmurtia 399, Komi 397, Yakutia 574, or Buryatia 564.

### BWX handoff

No new BWX source or runtime basename is proposed.

The next owner must choose between an explicitly Soviet successor identity and a generated alternate-history civic synthesis.

If the civic synthesis route is accepted, the next generated package must describe itself as alternate-history, distinguish textile/family/ritual motifs from state emblems, record provider generation date and applicable rights, and reuse the unchanged `BWX` ladder basename only after the map and identity gates close.

## Chunk-3 flag package: 17 rows

The package authority is `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/`.

The source register is `references/source_manifest.md` and the machine-readable row manifest is `metadata/asset_manifest.csv`.

Reference PNGs in `references/` are visual-comparison material only and are not runtime inputs.

The package contact sheets are `contact_sheets/source_masters_contact_sheet.png` and `contact_sheets/final_size_ladder_enlarged_contact_sheet.png`.

All generated runtime ladders use the stable paths `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga`.

The package has three technically handed-off rows and fourteen `needs_user_review` rows.

“Handed off” below means the source, processed ladder, TGA files, and checksums exist; it does not mean that ImageGen provider terms or every reference-file licence is independently recorded.

### Source URLs, attribution, and era-fit dispositions

| Tag | Identity and source URL | Source master | Date/era fit | Attribution and rights state | Current disposition |
| --- | --- | --- | --- | --- | --- |
| GMX | East Turkestan; [Flag of East Turkestan](https://en.wikipedia.org/wiki/Flag_of_East_Turkestan) | `source_png/GMX_east_turkestan_imagegen_raw.png` | 1933–1934 Kokbayraq reference; not automatically a 1936 federal flag | Commons file licensing is controlled by its file page; generated runtime source is separate and provider metadata is absent | `needs_user_review`; scope/community review |
| GTX | Tonga; [Flag of Tonga](https://en.wikipedia.org/wiki/Flag_of_Tonga) | `source_png/GTX_tonga_imagegen_raw.png` | Attested 1875 design; period-compatible redraw | Commons file licence is controlled by its file page; generated runtime source is separate | `handed_off` technically; rights record incomplete |
| GYX | Acadia; [Flag of Acadia](https://en.wikipedia.org/wiki/Flag_of_Acadia) | `source_png/GYX_acadia_imagegen_raw.png` | Attested 1884 design; period-compatible redraw | Commons file licence is controlled by its file page; generated runtime source is separate | `handed_off` technically; rights record incomplete |
| GZX | Newfoundland; [Dominion of Newfoundland](https://en.wikipedia.org/wiki/Dominion_of_Newfoundland) | `source_png/GZX_newfoundland_imagegen_raw.png` | 1904–1949 red ensign is era-compatible | Great Seal-style roundel is a simplified generated emblem; reference-file licence and provider metadata are not separately recorded | `needs_user_review`; small-size and rights review |
| HAX | Cascadia; [Cascadia independence movement](https://en.wikipedia.org/wiki/Cascadia_(independence_movement)) | `source_png/HAX_cascadia_imagegen_raw.png` | Fictional 1936 alternate-history route; no historical state flag claim | Original generated civic synthesis; provider date/licence is absent; movement page is context only | `needs_user_review`; route/community review |
| HCX | Texas; [Flag of Texas](https://en.wikipedia.org/wiki/Flag_of_Texas) | `source_png/HCX_texas_imagegen_raw.png` | Lone Star design associated with the Republic of Texas period | Commons file licence is controlled by its file page; generated runtime source is separate | `handed_off` technically; rights record incomplete |
| HDX | Cherokee Nation; [Cherokee Nation official culture FAQ](https://www.cherokee.org/about-the-nation/frequently-asked-questions/culture/?page=2&pageSize=7&term=) | `source_png/HDX_cherokee_imagegen_raw.png` | Fictional 1936 route; modern institutional context is not a 1936 flag | Generated seven-point-star/seven-oak civic synthesis; institutional and community review required | `needs_user_review` |
| HEX | Haudenosaunee Confederacy; [Flag of the Iroquois Confederacy](https://en.wikipedia.org/wiki/Flag_of_the_Iroquois_Confederacy) | `source_png/HEX_haudenosaunee_imagegen_raw.png` | Modern/commemorative context; no universal 1936 flag claim | Generated wampum/eastern-white-pine synthesis; Commons reference is separate; community approval required | `needs_user_review` |
| IBX | Kachin State; [Kachin Independence Army](https://en.wikipedia.org/wiki/Kachin_Independence_Army) | `source_png/IBX_kachin_state_imagegen_raw.png` | No single defensible 1936 flag; alternate-history route | Generated highland/river/jade/sun synthesis; no attested source file or provider rights record | `needs_user_review` |
| GIX | Wa State; [Wa State](https://en.wikipedia.org/wiki/Wa_State) | `source_png/GIX_wa_state_imagegen_raw.png` | No single defensible 1936 flag; alternate-history route | Generated mountain/valley/tea/rubber/sun synthesis; modern flag explicitly not copied; provider rights record absent | `needs_user_review` |
| GRX | Iwi-led Maori Federation; [Tino Rangatiratanga](https://en.wikipedia.org/wiki/Tino_Rangatiratanga) | `source_png/GRX_maori_federation_imagegen_raw.png` | Modern context only; fictional 1936 negotiated route | Generated restrained koru/wave synthesis, not a modern flag copy; iwi/community review required | `needs_user_review` |
| HFX | Lakota State; [Lakota people](https://en.wikipedia.org/wiki/Lakota_people) | `source_png/HFX_lakota_state_imagegen_raw.png` | No single period flag; fictional treaty-state route | Generated Black Hills/directional-sun synthesis; community review required; provider rights record absent | `needs_user_review` |
| HGX | Dine State; [Navajo Nation](https://en.wikipedia.org/wiki/Navajo_Nation) | `source_png/HGX_dine_state_imagegen_raw.png` | Pre-1968 alternate-history synthesis; modern 1968 Navajo flag excluded | Generated four-direction mountain geometry; community and era review required | `needs_user_review` |
| HKX | Zapotec-Mixtec Federation; [Mixtec](https://en.wikipedia.org/wiki/Mixtec) and [Zapotec peoples](https://en.wikipedia.org/wiki/Zapotec_peoples) | `source_png/HKX_zapotec_mixtec_imagegen_raw.png` | No single 1936 flag; negotiated alternate-history route | Generated combined textile geometry with no generic Aztec/Mexican motif; community review required | `needs_user_review` |
| HPX | Aymara State; [Aymara people](https://en.wikipedia.org/wiki/Aymara_people) | `source_png/HPX_aymara_state_imagegen_raw.png` | No single defensible 1936 flag; alternate-history Altiplano route | Generated restrained chakana-inspired synthesis; Wiphala intentionally excluded; community/sensitivity review required | `needs_user_review` |
| HSX | Muisca Restoration; [Muisca](https://en.wikipedia.org/wiki/Muisca) | `source_png/HSX_muisca_restoration_imagegen_raw.png` | Archaeological cues do not establish a 1936 flag | Generated raft/sun/river/mountain synthesis; restoration-route review required | `needs_user_review` |
| HUX | Patagonian State; [Patagonia](https://en.wikipedia.org/wiki/Patagonia) | `source_png/HUX_patagonian_state_imagegen_raw.png` | Broad region with no single 1936 state standard; alternate-history route | Generated wind/steppe/wave/star/sun synthesis, explicitly not Welsh, Araucanian, or Argentine; regional identity review required | `needs_user_review` |

The package itself records that attempts to retrieve additional Commons image references were rate-limited, so the source register preserves context URLs and uncertainty instead of inventing licences or copying unclear media.

### Chunk-3 source and runtime checksums

The following table records the retained ImageGen source SHA-256 and normal runtime TGA SHA-256 from `metadata/flag_validation.json`.

Medium and small runtime checksums remain in that JSON and are reproduced here for all 17 rows to make this handoff self-contained.

| Tag | Source PNG SHA-256 | Normal runtime TGA SHA-256 | Medium runtime TGA SHA-256 | Small runtime TGA SHA-256 | Status |
| --- | --- | --- | --- | --- | --- |
| GMX | `4736a0d8bb65807a2e0af5d5c6bd7dd7ce6b9a5c4d05aea422f03518974aab58` | `9577a6487def960b0f9697939d221a9cc3afadc6f6df80d01ec50527b638753f` | `2ffc6fba1e040f56f7fe9396e4057ec63aeacee9423fc1b948144ed4cff3c293` | `1d38b7520b3ab5f8660d16cb0155df6363cd3c09a26c0cfb13e7cae3a45861ca` | `needs_user_review` |
| GTX | `27b251753a51831b15b344c407e25d5864721be920d9497c1cc8c3ed571df906` | `218aa32d2bef6bff13f8753a712365d4cdd199b8170e91ef6be8ac95382c4315` | `1c39755f9fee8b3ad61f41c82f5d0e70c71d96516029c595e45433e68589b311` | `cb2a2be752f08013f4913f122440903a347c0da1a2942896a6f025ef4ac47e74` | `handed_off` |
| GYX | `df238839b4e5669abd3a17aec30b2cc5860bd158d427b6933cf6e01df57c1f4b` | `a5667d9ff04ea2904773a4b06b381ac3fa137028577a620df4e72b82b87cb76b` | `20024258e4e8d3a6ec2b7029dc04ce840ad529654c3c5d8c060d18c4dace5c4f` | `7255493df9b8b220e1b51d87e245777f9a5fe26a697b4a5dd97252e1c22a0bcd` | `handed_off` |
| GZX | `a676d71462c18179afd309b44aab922f7fbf9ef3d590e6674c16c66afe521086` | `5be5df298878106ae92511daa04b822a627218cc1c91f224ca46fd1bf709810a` | `f3cc290d4749db18a46243f8caa53f98274ff63a7b450e1799530972ff4580ae` | `58985de0e5c77d1aa4b1bfe82dff0c4fe9c162386678dd9c2272479f19bdce4e` | `needs_user_review` |
| HAX | `e9444395cc00f3447c90020740b9642d56292c6934c86fb1e02a0742aca92666` | `0fe2f7d54e93b5daceb61d858863769e81009df87fbdf22f6ea179e77ce6914a` | `738caafdab15c48743914280b64490331fc3cf6ef4c5548895b4b55a3b218852` | `c98d7081446d9d1a2a9791cf51c02c5fdbcbb39116a88d628b87bc5e8744bf04` | `needs_user_review` |
| HCX | `8753a620620ac287f2f521fb36f42b7176b9c85f3040e612eb7b60427e23c52c` | `e6dd6054315baa9c2a9de155d5510289937b7395b19a33b030427d5e00eea67b` | `acf61693d18993b880a9bd4e2617bb96aeb6e058cff8ffa37b4c87e34aeeb09a` | `7c20540946ed62771f9211540a452d0772813caf6df38554d23732cd10b66a85` | `handed_off` |
| HDX | `3178435eec354b13242f8d01ff673138cbb74f1a1a39c5ca102bd2439e991eb7` | `f5f0c45be78eec004824d2d076bc7d80effc456a01b16237a5b0135167f1a0ad` | `d146ab58937e98fd3640819012bbd5c7bd8c75ece848c3a6a1d2eed30ea1a528` | `7c7f5798d145d91fe014919e0629f7413f4e1933a2c420d9aa40fc9870f609cb` | `needs_user_review` |
| HEX | `27beb9598f51410241f980b6de3710eaa9326977de6e15cf20ab55b5b36b1784` | `f63e6fd94690346475334f19bc18f4cbe2f8702ab3b3bdd06f6ccce92fffa857` | `2db53c5aa52c55d29f76ed0242b0786593c810cc8302cf37a246d6a958eb89ec` | `758ef617522c4078135b81d6a66094d38abc89245e14d272e7d19e0e52b7e785` | `needs_user_review` |
| IBX | `8c9a7047ff482f239149542a25a5957f7f1cf7850eeeaed7bc121c8d3824b998` | `4801e0545f92272696ae3c227ccc084606871c94dfb6058ec123a28d2193b815` | `3dda83aa3bc44f7a12a87557dad84b7697aa4e700421f7b3955569b783620b73` | `f1a5b21b128625ec0a5c126cfbf381fabe5d0d81ea8fbcf30656132316c16490` | `needs_user_review` |
| GIX | `699c0e796c634a53fc5623c8faaced5738995778bafa078d5569deb4130a92e9` | `6c3eae75c61b074d3098fd1d6c721d87576ed1dce1ee8b841dda4c7333403fe7` | `7e4d7b67013515299fd09a17008b00a8ff44e6821c5cecf7e18851eff0c13c2d` | `72005052012f06e0e8c7b4b1081202432baf5e62cb751e064e6404ac35651053` | `needs_user_review` |
| GRX | `fc6b12b0c3105b57c31f7bebcdff2be1ae34a54b7ee808bdfabf6a1f36fa2883` | `7155862d249d98cfbeebbfc735367fe620d2d76cbf6339cafcdaee60acbf4d4d` | `652bf3f002f98c25f80d21b799bf7e98d2746ee29d144d00b9d020b5ccc5ece4` | `e1fa204bdc4785f0ef525c9f45ae5307cd609a4f8721e37d16edd7f839c5ff2e` | `needs_user_review` |
| HFX | `30a7967e3ff28b465732f202daa43c0426164a0e6a92c01af74b64a6c9a71091` | `5c023fae3389846a6d5b46c882c1aa734b9bae0df64ab5683726649db37ed764` | `efa5c4411fb034435798b09ee57525642e0394462bf5a223f6572b7801d090dc` | `4f5f531701cad492939bd8b061a9c43b6d07ffa093b0ef832138c22355c709f6` | `needs_user_review` |
| HGX | `014f46147fb0af3988fe471a2b93a642de1a01524a063a25fa24629a3e932534` | `74beb677ff91e2876d59b19119fdee3f943a7db2a570b57a7d0208dd5cd410b1` | `4dbb1f1c766755cd1d81178c66fca55913ec894b70189671a8d8a7702832c870` | `853e5b619762d4e79580e8af59fadc8b4a88213e72c5c4c2626049625bba26bc` | `needs_user_review` |
| HKX | `1ea934bfca545e529f0fa1cfbfdb71d5a2273e6640cbdd830788ff332aec3be6` | `367a355fda0abda282db2131af240761582bdd637a629b5a357a2add38adad45` | `10331b1dce963e48c64a9c26dbad919d189d766227fce590e04f1c2d71f95069` | `94cf6123ff479e291c170d476f493d1e11e3cf7d34f568ae2a358e055ee9532c` | `needs_user_review` |
| HPX | `01f5ebfdd96989b6a093a690dd6f45428fcfa683192f97c7253d64be03265c95` | `f7d54dcf229af5400ccac2c34496cb69c405453bc66da2798b0f5c467f99d244` | `28f9992a59c7de0eb337d3bb28adaf7a87d3966435e0d696267f7c76e0185fda` | `0e6a679d5581312b359552cacd89a6f8bf7f1e7760988f7e48f5afb776855b21` | `needs_user_review` |
| HSX | `ed750a9c42c35718c65cfba3dcdd383a13c3dd78da75e453af9aaf03276ae11b` | `9975746125266022011410b6c9223dd8fddf2245aaecbd00ddbcc48e7b5561e3` | `df9204d42dca49578370c18264ad843ab893136866a669b05f9dbed629aa0de3` | `e519267af3a08bfa195bcbc38e9ae5df770329e31c8f8ecea6493aa9a8736cf8` | `needs_user_review` |
| HUX | `db9dbeb750040310983625ca7a275e0d8cca3027ab7f1259853a9911e9cc704d` | `f9aa690fefa9d0d0f94423b7b5f059236ca9f30f7ef46defce557e60da979b7b` | `424f7170eb2c1a9f315a14b4e704fbb7eddef18f73ddb20f62dd3987e8728a60` | `c479cac5b57151850e68a55a547c7d7af150714c8dc59e98a40097b80f99880d` | `needs_user_review` |

The normal, medium, and small TGAs validate as uncompressed 32-bit type-2 images with descriptor `8` and bottom-left origin at 82x52, 41x26, and 10x7 respectively.

### Chunk-3 next gates

GTX, GYX, and HCX can remain in technical handoff state because their period design references are clear enough for a clean redraw, but the package should add provider-generation date/terms and the exact Commons file-page licence before calling them rights-complete.

GMX needs East Turkestan scope/community review because the Kokbayraq reference is tied to 1933–1934 and modern identity overlap remains.

GZX needs small-size review of its simplified Great Seal-style roundel and a clearer reference/licence record.

HAX, IBX, GIX, HFX, HGX, HSX, and HUX are alternate-history or regional syntheses without a single defensible 1936 state flag, so they must remain explicitly synthetic and route-reviewed.

HDX, HEX, GRX, HKX, and HPX need institutional, iwi, community, or sensitivity review before promotion because the designs use living or contested identity motifs.

No chunk-3 source or runtime basename change is proposed.

## AEX basename collision

The Event 006 IW-005 candidate row lists provisional `AEX`, but its `resolved_tag` is blank and its policy is `reuse_vanilla_route_overlay` for the non-selectable `BEL_flanders` cosmetic overlay.

The Event 006 NWE package explicitly requires the standalone AEX source, processed, and runtime paths to remain absent.

The repository-wide runtime currently contains these AEX files:

| Runtime path | SHA-256 |
| --- | --- |
| `gfx/flags/AEX.tga` | `49D1205A64D792E2EA7BDD04049DA5C89E88BF024F1418F7B50DA27508FA4F5E` |
| `gfx/flags/medium/AEX.tga` | `AC656B8F8F86EEED03C7ACDC545980DA31DDC63B87E131DE3BA725E129D699B8` |
| `gfx/flags/small/AEX.tga` | `32059E03D495B36142C3CD2A67A1CE366E31CC947C5607D5620FC9F35D270A01` |

Those global AEX files belong to Event 005's Basmachi Confederation surface through `common/country_tags/chaosx_countries.txt:18` and are not an Event 006 Flanders source package.

Do not delete, rename, overwrite, or relabel the current AEX files in an Event 006 asset pass.

Do not create a new Event 006 `AEX.tga`, `AEX_medium`, `AEX_small`, or NWE source tree.

The safe owner decision is either to make NWE validation scope-aware or to run a separately reviewed cross-event tag migration with Event 005 ownership present.

No AEX basename is proposed for Event 006 in this handoff.

## Northern/Western Europe ideology aliases

The NWE package authorizes only the unsuffixed base ladders for ACX, AFX, AGX, and AJX.

It explicitly authorizes no `<TAG>_democratic`, `<TAG>_communism`, `<TAG>_fascism`, or `<TAG>_neutrality` files.

The current runtime nevertheless contains 48 suffix aliases: four suffixes for each of four tags at each of the three ladder sizes.

Within each tag and size, the four aliases are byte-identical to the unsuffixed base.

The following base hashes are the comparison anchors:

| Tag | Normal `82x52` | Medium `41x26` | Small `10x7` |
| --- | --- | --- | --- |
| ACX | `e44993e121278c5d5dd72d51cd78d47c66f34f256e12e3c80e4fc11af70cfaad` | `38aa26dad200038e0bb3db84d651227312ea9941e31505f49541cb100b2fe1fb` | `c47d991628fe98cc8b7c6c669521530319cc4b8f35b06c5aff23a93dd0bfa718` |
| AFX | `ab7979743621acd8c32b7665dd9b2f921bf32b5909817f89744d665469a7dd97` | `c290fd5dbd6209460ba1ed7542aad3739fdfaf429c93ec39d35725bc96d35d7a` | `654b62796678117e0ff38d849d63966dd37ce41a2cfe9ab02043558dfabcd95d` |
| AGX | `9097e4d1d83cf59db356913de459bd6e3e52f6d5fb495da8052b70e284fce2dc` | `1061319a167acf56c3a967f2e819ed279cccc37b57f61bf1e40cd0fb662bcccc` | `92546ec8d91417c03ce6056f5ce562da17020a6c2036fd9e766e174af5379683` |
| AJX | `be622a9d8cf12435cf055ae7d59278081975eecfc05a2787a056e1d096810a4c` | `ffb75c4a42b8d6255a2d8f365963ad3da675da91dc7baa15b3e40d967a967772` | `9ece1cfa8e6c3f5e61ba6e6e59920c2a843a10751055309b5b8bc9b12d868b6f` |

The source/provenance records for the four unsuffixed designs are:

| Tag | Attested design input | Source/rights record | Era/function note |
| --- | --- | --- | --- |
| ACX | St Piran's Cross; [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg) and [Flag Institute UK Flag Registry](https://www.flaginstitute.org/wp/flags/cornwall-flag/) | Commons public-domain reference; Flag Institute identity/proportion check | Cornish community flag; engine-fitted 82:52 ladder |
| AFX | Walloon coq hardi, 1913 reference; [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Flag_of_Wallonia.svg) and [Wallonia Public Service](https://connaitrelawallonie.wallonie.be/histoire-et-symboles/symboles/un-embleme-le-coq-hardi) | Commons CC0 reference; Wallonia Public Service historical check | Period Walloon symbol; generated flat redraw |
| AGX | Provincial Friesland/Fryslân flag; [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Frisian_flag.svg) and [Province of Fryslân](https://www.fryslan.frl/friese-vlag) | Commons public-domain reference; official provincial design check | Official provincial design; generated flat redraw |
| AJX | Saar territory 1920–1935 flag; [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Flag_of_Saar_1920-1935.svg) and [Saarland State Chancellery](https://artsandculture.google.com/story/saarhundert-das-saargebiet-ein-kind-der-internationalen-v%C3%B6lkergemeinschaft-staatskanzlei-saarland/kQWBBjUfmhpHJA?hl=en) | Commons public-domain reference; institutional check | Interwar territory design; generated flat redraw |

The four retained source inputs are `docs/assets/006_independence_wave/source_png/country_symbols/acx_st_pirans_cross_source.png`, `docs/assets/006_independence_wave/source_png/country_symbols/afx_walloon_rooster_source.png`, `docs/assets/006_independence_wave/source_png/country_symbols/agx_west_frisian_flag_source.png`, and `docs/assets/006_independence_wave/source_png/country_symbols/ajx_saar_territory_1920_1935_source.png`; generated raws and flat masters remain under `docs/assets/006_independence_wave/source_png/generated_nwe/flags/`.

These records support the four unsuffixed base designs, not the 48 unauthorized aliases.

The aliases have no separate route, ideology, source, or design contract, even though the bytes are identical.

No aliases were removed or promoted in this tranche.

The next owner must choose between deleting the 48 files after confirming no consumer expects them, or documenting a deliberate route-to-filename contract that keeps them outside the NWE source package.

## Broader source, rights, and era gaps

The AKX–CLX package and the COX–EBX package retain ImageGen sources, processed ladders, final TGAs, prompts, design-reference URLs, and hashes.

Their machine-readable validation records do not provide per-row `license`, `author`, `archive`, or `source_date` fields.

Package prose distinguishes generated, historical-reference, and alternate-history designs, but a technical `handed_off` state is not a blanket rights clearance.

Treat any unlisted reference-file licence, author, archive, or date as unknown rather than public domain.

The chunk-3 register similarly distinguishes generated runtime art from reference pages, and the reference pages do not themselves establish the licence of an individual Commons file unless the exact file page is cited.

No external reference pixels were copied in this tranche because several archive terms and generated-provider terms are unclear.

No source/rights gap found here justifies a fallback emblem, modern flag, borrowed vanilla flag, or invented public-domain claim.

## Runtime handoff boundary

No new processed PNG preview, DDS, TGA, contact sheet, sprite definition, or runtime basename was created in this research-only tranche.

The existing chunk-3 and BWX path pattern remains the normal/medium/small `<TAG>.tga` ladder.

The existing ASSET-046 path pattern remains the immutable `form_01` through `form_48` emblem IDs and the separate league emblem name.

AEX has no proposed Event 006 basename.

The parent agent can use this handoff to wire only assets already accepted by the relevant package authority, while carrying all `blocked`, `needs_user_review`, and rights-unknown dispositions forward.

## Simplifications, omissions, and blockers

This handoff intentionally performs research and documentation only.

No source file was selected for new runtime promotion.

No blocked BWX or chunk-3 design was regenerated, recoloured, cropped, or renamed.

No ASSET-046 emblem was invented for a missing formable row.

No AEX file or NWE ideology alias was deleted because ownership and consumer policy remain unresolved.

The remaining blockers are the formable identity/consumer matrix, BWX map and route decision, chunk-3 provider/licence and community review, AEX cross-event ownership, NWE alias policy, and row-level rights/date metadata for the broader generated flag packages.
