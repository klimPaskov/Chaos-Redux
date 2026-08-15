# IW-057 FER flag and symbol provenance review — current 2026-08-15

Date: 2026-08-15.

Scope: independent source and identity review for the Far Eastern Republic (FER) neutral/base flag and route-symbol question in the 1936 Event 006 opening.

This is a research-only handoff. It does not select a runtime asset, invoke ImageGen, create a processed PNG, create TGA/DDS/GFX files, edit gameplay or localisation, alter central admission or Join, or replace the existing dated symbol-source handoff.

## Executive disposition

`FER` is a valid installed vanilla carrier tag, but its vanilla flag ladder is not a safe Event 006 neutral/base identity by filename or carrier presence alone.

The installed ladder contains only four ideology-specific files in each size family and has no no-suffix `FER.tga` base flag in normal, medium, or small size.

The vanilla `FER_communism` ladder is a strong historical-continuity reference: its normal flag uses the same `#CC0000` red field, `#071B54` upper-hoist canton, 42.7%-by-50% canton geometry, and triangular red `D.V.R.` letter arrangement documented for the 11 November 1920 FER design and Article 181 of the 1921 Constitution.

That match does not make `FER_communism` a neutral/base runtime asset. It is an ideology-suffixed vanilla file, its small letters collapse at 10x7, and the historical design is a 1920–1922 continuity symbol rather than an attested 1936 flag.

The vanilla democratic, neutrality, and fascist ladders are visually different ideology designs with no source or date provenance in the installed FER country package, so they must not be treated as Event 006 historical or neutral symbols.

No directly attested neutral, non-socialist FER flag current in 1936 was found. The source gate remains `needs_user_review` for a historical continuity reconstruction and `blocked` for an unapproved non-socialist synthesis.

## Accepted IW-057 context

The binding research row is `IW-057, Far Eastern Republic, FER` in [006_package_research_resolution.csv](../../../specs/006_independence_wave_specs/research/006_package_research_resolution.csv).

That row requires the registered base flag to match released identity and origin, historical route variants to be sourced, and clearly alternate civic or high-chaos variants to be generated only as explicit alternate-history designs.

The package-local implementation and audit remain HOLD / FAIL-CLOSED in [package core](006_iw057_far_eastern_republic_package_core_2026_08_15.md) and [package audit](006_iw057_far_eastern_republic_package_audit_2026_08_15.md).

The current capital-preflight repair permits dormant vanilla capital state 563 only before shared execution reanchors the runtime package to ordered Event 006 anchor state 408 or 409; it does not change the flag conclusion. See [capital preflight repair](006_iw057_fer_capital_preflight_repair_2026_08_15.md).

The current next-tranche plan names `FER-H0-1920-FLAG` as the preferred historical-continuity candidate, `FER-H1-1921-CONST-FLAG` as a public-domain constitutional reconstruction fallback, and explicitly forbids silent use of the vanilla democratic flag. See [next-tranche planner handoff](006_iw057_fer_next_tranche_planner_handoff_2026_08_15.md).

Vanilla carrier evidence is identity context, not Event 006 origin proof.

`history/countries/FER - Far Eastern Republic.txt` sets `capital = 563`, starts the dormant carrier as democratic with 1936 elections, and sets democratic popularity to 60 and communist popularity to 40.

`history/states/408-Vladivostok.txt` and `history/states/409-Khabarovsk.txt` are SOV-owned states with FER cores, while dormant FER history retains capital state 563 in `history/states/563-TS 5.txt`.

`common/countries/Fareastern Republic.txt` contains only eastern-European graphical cultures and the vanilla country colour, and `common/country_tags/00_countries.txt` maps `FER` to that country definition.

None of those files states that the vanilla democratic, neutrality, or fascist flag is the historical FER institutional flag or an Event 006 provisional-origin symbol.

## Installed vanilla FER ladder

Installed source root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

The canonical reference library records the inspected vanilla extraction as Operation Postern `v1.19.2.0.a729 (d245)`, extracted 2026-07-16. The installed files were re-read on 2026-08-15.

All twelve files were inspected at their native dimensions and TGA headers. Normal files are 82x52, medium files are 41x26, and small files are 10x7. Normal and medium files use 32-bit TGA descriptor `0x08`; small files use descriptor `0x00`; all have origin code `0` and no upside-down origin signal.

| Variant | Installed geometry | Visible design | Provenance and Event 006 disposition |
| --- | --- | --- | --- |
| `FER_communism` | Red field with dark-blue upper-hoist canton; normal dominant colours `#CC0000` and `#071B54`; canton bbox in the 82x52 normal is x=0..34 and y=0..25. | Triangular red `D.V.R.`/`В.Д.Р.` letters in the canton. The colours and canton ratio match the archived H0 historical reconstruction. | Historical-continuity reference only. It is not a neutral/base replacement and must not be copied into the package cosmetic tag without an explicit parent decision and a separate production pass. |
| `FER_democratic` | Red upper field, blue lower field, white hoist triangle; normal dominant colours `#D81E05`, `#0359BA`, and white. | No D.V.R. letters or documented FER constitutional emblem. | Not identity/origin-compatible for the Event 006 provisional identity; reject as the base or historical route symbol. |
| `FER_neutrality` | Green upper field, red lower field, yellow hoist triangle with a detailed brown/red emblem; normal dominant colours `#00923F`, `#D81E05`, and `#FFD700`. | No documented 1920/1921 FER flag geometry. | No installed source/date provenance establishes this as a historical neutral FER design; reject as a neutral/base source. |
| `FER_fascism` | Black, green, and white horizontal bands; normal dominant colours `#000000`, `#009900`, and white. | No documented FER emblem or constitutional geometry. | Ideology-specific game art with no accepted Event 006 historical provenance; reject as a base or route symbol. |

There is no `gfx/flags/FER.tga`, `gfx/flags/medium/FER.tga`, or `gfx/flags/small/FER.tga` in the installed ladder.

The vanilla ladder therefore proves that the carrier has ideology variants, not that any variant is an Event 006 neutral/base identity. The only strong historical match is the communist-suffixed ladder, which is unsuitable as a neutral/base handoff without a parent identity decision.

### Vanilla ladder checksums

The following SHA-256 values identify the installed source files reviewed in this tranche.

| Installed source file | SHA-256 |
| --- | --- |
| `gfx/flags/FER_communism.tga` | `67bfd2aea68817fbb65a7c3ba699eadd8ab28017cf1ab8429d3f652d55b7d074` |
| `gfx/flags/FER_democratic.tga` | `925dfc3213469da0ecec01c18c3ae8c45f71915759d97da5efb25cc329ed0516` |
| `gfx/flags/FER_fascism.tga` | `eba3cfb00aeaf9efa9e8fdd989ced585cfca72983562cc9da1fc07f9d2efc0af` |
| `gfx/flags/FER_neutrality.tga` | `1194e88f15fd61e64645d2602e262689f89974b13ad9e019d5beedce72c744f1` |
| `gfx/flags/medium/FER_communism.tga` | `192a80a8daa2af0bce27fc072e33ac9fcabb119ec8fd4b7713de6452847d587f` |
| `gfx/flags/medium/FER_democratic.tga` | `4549aa43a471d559a37dd69974726d0170498f8977c7f91b4ff5852a3e533108` |
| `gfx/flags/medium/FER_fascism.tga` | `e94c9554e58aaf753376f5455f8160d9ed439b384e76491afc6d8e71697d4a7f` |
| `gfx/flags/medium/FER_neutrality.tga` | `9e6d1c0e563cde6386e9d5f1d41ae65d47b0e0bb988bfbe656ed09a51ab36502` |
| `gfx/flags/small/FER_communism.tga` | `675bee57b892c30b006d123fefb183c8a15f921f2314dea2ba49c571327513cf` |
| `gfx/flags/small/FER_democratic.tga` | `b76e2da4103c83c5f0373074bc6df003f2525d7e91b912d9cede786a7341565` |
| `gfx/flags/small/FER_fascism.tga` | `9459d9d56a39ba4e051c1421cad5ae9a6c4b334db68703051ad7b0db3a15e0fe` |
| `gfx/flags/small/FER_neutrality.tga` | `9652fd5b79d8e7997bba1f4508707913b0b67a9a6c1b818a0511afbf4d26659d` |

## Historical source chain

The existing archived source package is [006_iw057_fer_symbol_sources_2026_08_15](006_iw057_fer_symbol_sources_2026_08_15/). Its comparison sheet is [fer_symbol_candidates_contact_sheet.svg](006_iw057_fer_symbol_sources_2026_08_15/fer_symbol_candidates_contact_sheet.svg), which is review-only and must not be wired.

The Far Eastern Republic existed from April 1920 through its merger into the RSFSR on 15 November 1922. Therefore a 1936 FER use must be described as a revival, restoration, continuity claim, or explicit alternate-history successor rather than an uninterrupted historical government.

| Candidate | Source URL or archive | Historical date and geometry | Rights and uncertainty | Current disposition |
| --- | --- | --- | --- | --- |
| `FER-H0-1920-FLAG` | [Commons historical reconstruction](https://commons.wikimedia.org/wiki/File:Flag_of_Far_Eastern_Republic.svg), based on the [SHPL scan, page 67](http://elib.shpl.ru/ru/nodes/8743#mode/inspect/page/67/zoom/4). | Commons metadata gives 11 November 1920. The archived SVG is nominally 900x600, with a red `#CC0000` field, dark-blue `#071B54` upper-hoist canton approximately 383.4x300, and red D.V.R. letters in a triangle. | Commons identifies NuclearVacuum as author and states CC BY-SA 3.0 plus GFDL. The reconstruction licence is visible, but the underlying SHPL scan's reuse rights are not independently stated. Commons also warns that official insignia restrictions are separate from copyright. | Strongest historical continuity candidate, but `needs_user_review` for rights and for an explicit 1936 revival framing. No runtime asset selected. |
| `FER-H1-1921-CONST-FLAG` | [Commons constitutional-option reconstruction](https://commons.wikimedia.org/wiki/File:Flag_of_the_Far_Eastern_Republic_(Constitutional_option).svg), sourced to the 1921 Constitution text. | Commons metadata shows 6 April 1920, likely a founding-date marker rather than a proof of design adoption. The archived SVG is 1500x1000 (3:2), with red field, dark-blue upper-hoist canton, and red D/V/R paths. | Commons marks the reconstruction public domain and credits the FER Constitution/government. It is a text-based reconstruction, not a primary period scan and not proof of a distinct 1936 flag. | `needs_user_review` as an explicit constitutional reconstruction fallback only if the parent rejects or cannot clear H0. |
| `FER-H2-CONST-EMBLEM` | [Commons constitutional coat-of-arms reconstruction](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_the_Far_Eastern_Republic.svg) and [Heraldicum civil-war reference](https://www.heraldicum.ru/russia/civilwar.htm#dvr). | Article 180 family: red shield, conifer wreath, sunrise, five-pointed silver star, wheat sheaf crossed by an anchor and pointed pickaxe, and D.V.R. letters on the wreath ribbons. | Commons marks its reconstruction public domain and credits the Constitution. It is an emblem reference, not a directly scanned period runtime asset. | Research reference for H0/H1 identity; no standalone runtime emblem requested or produced. |
| `FER-H3-BANKNOTE-EMBLEM` | [Heraldicum banknote image](https://www.heraldicum.ru/russia/images/dvr1.gif). | Heraldicum places the wheat, anchor, and pickaxe motif on FER banknotes in 1920. The local GIF is low-resolution and not a clean flag master. | Image reuse rights are not stated. | Archive-only; blocked for runtime. |
| `FER-H4-MUSEUM-BANNER` | [Heraldicum banner photograph](https://www.heraldicum.ru/russia/images/dwr.jpg), credited to the Khabarovsk Regional Museum named N. I. Grodekov. | Historical banner context is relevant, but the page does not state the photograph's exact date or clean flag geometry. | Museum credit is present; image rights are not stated. | Archive-only; blocked for runtime. |
| `FER-H5-PRE-1920-PROVISIONAL-EMBLEM` | [Heraldicum civil-war reference](https://www.heraldicum.ru/russia/civilwar.htm#dvr). | Text describes an earlier provisional-government emblem before the 11 November 1920 approval. | No dated primary scan and no defensible reuse licence were found in this tranche. | Blocked pending a primary scan and rights evidence; do not reconstruct from prose alone. |
| `FER-R0-2006-PD-REDRAW` | [Commons 2006 redraw](https://commons.wikimedia.org/wiki/File:Flag_Far_Eastern_Republic.svg). | Commons metadata gives 24 July 2006; the file is 1200x800 and is not a historical design date. | Commons marks it public domain and credits Szczepan1990, but the page records no historical source for its geometry. | Comparison aid only; reject as sole 1936 identity evidence. |
| `FER-SYN-CIVIC-1936` | No source URL because no art exists. Motif inputs would be H2, H3, and H4 only. | Explicit non-socialist alternate-history civic synthesis for a 1936 revival or successor institution. | No artwork or licence exists until the parent approves a separate generated-art task. | Blocked pending explicit parent approval; never label historical. |
| `FER-SYN-RAIL-PORT-1936` | No source URL because no art exists. Rail, port, customs, and coastal additions would be design additions, not attested heraldry. | Explicit route-specific alternate-history railway-port synthesis. | No artwork or licence exists until the parent approves a separate generated-art task. | Blocked pending explicit parent approval; do not replace the historical continuity baseline. |

The archived 1921 constitutional evidence copy is [far_eastern_constitution_1921_worldstatesmen.pdf](006_iw057_fer_symbol_sources_2026_08_15/far_eastern_constitution_1921_worldstatesmen.pdf), SHA-256 `7a62e44e5da3b1886ae88f17ec6ce636b0b42b112561bbc503a2fb66a056b361`. Its PDF metadata identifies the title as *Constitution of the Far Eastern Republic (1921)* and the author as Assembly of the Far Eastern Republic; the archive/site reuse rights are not stated.

The local archived source hashes are retained in the prior [symbol research handoff](006_iw057_fer_symbol_flag_research_handoff_2026_08_15.md). The key flag and emblem hashes are repeated here for parent selection:

| Archived source file | SHA-256 | Rights status |
| --- | --- | --- |
| `flag_of_far_eastern_republic_cc_by_sa_3.svg` | `8e40e542c381cab99b27222f690a77d77a112c18976fd3cd99135b8b5235ff10` | Commons CC BY-SA 3.0 reconstruction; SHPL underlying rights unclear. |
| `flag_constitutional_option_public_domain.svg` | `2c37b2bec02b66bde60be76e886421091660bb4c2ca4ef0ace393a3c26421881` | Commons public-domain reconstruction from constitutional text. |
| `coat_of_arms_constitutional_public_domain.svg` | `d706595472ee4ced1de180e321895c825010d6c3bdb69d4a756b3668dc6dbecd` | Commons public-domain reconstruction from constitutional text. |
| `heraldicum_dvr_constitutional_reconstruction.gif` | `6527f7bc66e765db6dbb805c8d168df4714d736471654339ae416316eda8b4c8` | Rights not stated; archive-only. |
| `heraldicum_dvr_banknote_emblem.gif` | `404541aaf00a592bff82f24b5f7671d89c59ae62fe892bbe3ab6d4ac570d06aa` | Rights not stated; archive-only. |
| `heraldicum_dwr_museum_banner_photo.jpg` | `51f3328e37d73a19fdd9b0494ff2eded689e445aafe36d1ba83187918a3e143b` | Museum credit present, date and rights unclear; archive-only. |
| `flag_far_eastern_republic_pd_2006.svg` | `20b08fb6bc102fd3b85f97b2f895e30e7aadbdb6007fee0b02980079d6b9422c` | Commons public-domain 2006 redraw; no historical-source proof. |

## Parent decision gate

The parent must first state whether “neutral/base” means route-neutral historical continuity or a genuinely non-socialist neutral visual language.

If route-neutral historical continuity is intended, explicitly accept `FER-H0-1920-FLAG` as a 1920–1922 revival/continuity identity, resolve the CC BY-SA 3.0 attribution/share-alike and SHPL-source uncertainty, and route the accepted design to the non-portrait flat-flag production owner under the Event 006 prompt's ImageGen reconstruction rule.

If H0 rights cannot be cleared, explicitly choose `FER-H1-1921-CONST-FLAG` as a public-domain constitutional-text reconstruction and document that it is a reconstruction, not a distinct attested 1936 flag.

If non-socialist neutral language is required, explicitly authorize `FER-SYN-CIVIC-1936` as alternate history and commission a separate generated-art task with motif traceability to the documented FER sources. Do not call the result historical.

If the railway-port route needs a distinct symbol, authorize `FER-SYN-RAIL-PORT-1936` separately and keep it route-specific; it must not replace the historical continuity baseline.

Until one of those choices is recorded, leave `FER_INDEPENDENCE_WAVE_PROVISIONALX` and all identity/roster receipts fail-closed and do not create a runtime flag package.

Do not use the vanilla democratic, neutrality, or fascist FER ladders as a substitute. Do not use `FER_communism` as a neutral/base substitute even though its geometry matches H0. Do not substitute Priamur, White-movement, Japanese-backed, RSFSR/Soviet, generic Siberian, or generic railway symbols.

The exact next parent decision is: “Choose H0 historical continuity with rights clearance, H1 public-domain constitutional reconstruction with explicit reconstruction framing, or authorize the alternate-history civic synthesis; otherwise keep the FER symbol gate blocked.”

## Handoff status and boundary

Status by candidate: `FER-H0-1920-FLAG` = `needs_user_review`; `FER-H1-1921-CONST-FLAG` = `needs_user_review`; `FER-H2-CONST-EMBLEM` = research reference only; `FER-H3`, `FER-H4`, and `FER-H5` = blocked archive-only evidence; `FER-R0-2006-PD-REDRAW` = rejected as sole historical proof; `FER-SYN-CIVIC-1936` and `FER-SYN-RAIL-PORT-1936` = blocked pending parent approval.

No selected runtime asset exists, so no processed PNG, final TGA/DDS, manifest entry, or `gfx_handoff.md` is produced by this research-only tranche. The parent must not wire the archived source files or canonical vanilla reference PNGs into runtime.

Work completed: installed vanilla ladder inspection, TGA dimension/header/hash capture, comparison against the accepted IW-057 source rows and package handoffs, independent local review of the archived Commons/SHPL/Constitution/Heraldicum source chain, and this durable handoff.

No gameplay, localisation, central admission, Join, event, GFX, runtime flag, portrait, or spreadsheet file was changed.
