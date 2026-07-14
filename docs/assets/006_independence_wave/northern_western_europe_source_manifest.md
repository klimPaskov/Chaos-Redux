# Event 006 northern and western Europe source manifest

## Scope and source-mode boundary

This package covers the bounded Event 006 source tranche for IW-001 through
IW-010, excluding IW-011 Faroe Islands, plus IW-012 Icelandic emergency
republic:

- SCO Scotland;
- WLS Wales;
- ACX Cornwall;
- BRI Brittany;
- AEX Flanders;
- AFX Wallonia;
- AGX Frisia;
- RHI Rhineland;
- BAY Bavaria;
- AJX Saar;
- ICE Icelandic emergency republic.

Every new tag in this tranche ends in `X`: ACX, AEX, AFX, AGX, and AJX.

The files in this source package are historical or community-source evidence.
No generated route flag, fictional council portrait, or generated leader is
included. The five Group B packages still require generated period civic
baseline flags and, where the accepted design calls for them, generated
institutional council portraits. The source and processed symbol PNGs in this
manifest are inputs for that separate generated-art pass; they are not runtime
flags and must not be presented as authentic 1936 state flags.

Registered vanilla flags are inspected in place and are not copied into the mod.
This avoids duplicating proprietary game art and preserves the accepted
registered-tag reuse rule.

## Review artifacts

- `contact_sheets/006_northern_western_europe_sourced_assets.png` shows all five
  sourced motifs and all three route-owned portrait candidates.
- `contact_sheets/006_northern_western_europe_final_dds_decoded.png` was built by
  reopening the actual runtime DDS files, not by reusing the processed PNGs.
- `_tooling/build_northern_western_europe_sources.py` records the fixed portrait
  crops, non-generative tonal processing, symbol preview normalisation, and
  contact-sheet layout.

## Package disposition

| Package | Flag or symbol disposition | Portrait disposition | Binding distinction or blocker |
|---|---|---|---|
| IW-001 Scotland / SCO | Reuse the installed SCO ideology triplets. The Saltire is the civic/national identity. The Lion Rampant is a royal banner and is route-owned, not a neutral substitute. | No mod-owned real portrait delivered. | No rights-cleared, period-appropriate portrait for a supported 1936 Scottish nationalist leader was found. Roland Muirhead material at the National Library of Scotland is subject to copyright restrictions. |
| IW-002 Wales / WLS | Reuse the installed WLS family only under the accepted registered-tag rule. | No mod-owned real portrait delivered. | The familiar red-dragon-on-green-and-white layout was officially adopted in 1959. Its dragon is historical, but the installed flag must not be described as an authentic 1936 Welsh state flag. The only cleared Saunders Lewis portrait found is from 1973 and is excluded by the period rule. |
| IW-003 Cornwall / ACX | St Piran's Cross source and processed motif delivered. No TGA produced. | Institutional council remains the accepted opening mode. | This is a historical Cornish community flag, not evidence of a 1936 Cornish state flag. Final civic baseline art remains generated-art work. |
| IW-004 Brittany / BRI | Reuse the installed BRI base family. The Gwenn-ha-du is a period regional identity, adopted as a Breton symbol in 1923. | François Debeauvais portrait DDS delivered for a nationalist route only. | Debeauvais must not be assigned to a constitutional, neutral, or universal opening government. The crop is from an identified 1928 party-congress photograph and is low fidelity. A sharper 1932 portrait was rejected because its page does not establish United States public-domain status. |
| IW-005 Flanders / AEX | Historical Lion of Flanders arms source and processed motif delivered. No TGA produced. | Institutional council remains the accepted opening mode. | The current official Flemish flag is postwar. The delivered arms are a historical motif for generated civic design, not a backdated modern state flag. |
| IW-006 Wallonia / AFX | CC0 rooster vector source and processed motif delivered. No TGA produced. | Institutional council remains the accepted opening mode. | The rooster was selected and validated by the Walloon Assembly in 1913. The delivered vector follows the 1998 legal form; Pierre Paulus's original watercolor was not copied because the museum/province rights notice is restrictive. |
| IW-007 Frisia / AGX | West Frisian provincial flag source and processed motif delivered. No TGA produced. | Institutional council remains the accepted opening mode. | The seven stripes and seven pompeblêden are attested for Friesland and recognized provincially in 1897. They are not proof of one pan-Frisian state flag and cannot be universalized across every Frisian coast. |
| IW-008 Rhineland / RHI | Reuse installed RHI triplets. The green-white-red democratic variant belongs to the 1923 separatist-republic direction, not every Rhineland route. | Josef Friedrich Matthes portrait DDS delivered for the separatist/republic route. | Matthes was the leading figure and minister-president of the short-lived 1923 Rhenish Republic. Do not use him for a generic neutral corridor, military cabinet, or universal constitutional opening. |
| IW-009 Bavaria / BAY | Reuse installed BAY triplets. White-blue civic state colors and royal/crowned variants must remain route-distinct. | Rupprecht portrait DDS delivered for a traditional restoration route. | Rupprecht was the last Bavarian crown prince. Do not use this portrait for a republican or labor opening. |
| IW-010 Saar / AJX | Exact 1920-1935 Territory of the Saar Basin flag source and processed motif delivered. No TGA produced. | Institutional neutral commission remains the accepted opening mode. | The blue-white-black tricolor ended with the territory on 1 March 1935. It is strong source material for a neutral-commission route, but no ideology/cosmetic mapping is approved, so creating `AJX_neutrality.tga` would be an unsupported design decision. Final civic baseline art remains generated-art work. |
| IW-012 Iceland / ICE | Reuse the installed ICE family. The cross design was specified by royal decree in 1915 and became the national maritime flag in 1918. | No new mod-owned portrait delivered. | Hermann Jónasson's AAT portrait is an installed-DLC option only if the implementation permits that dependency. The exact-period 1937 Swedish-calendar photograph lacks a United States public-domain tag, so it was not copied. |

## Sourced symbol provenance

| Package | Delivered source | Creator or institution | Date and rights | Historical function and allowed use |
|---|---|---|---|---|
| ACX Cornwall | [Flag of Cornwall SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg); [Flag Institute history](https://www.flaginstitute.org/wp/flags/cornwall-flag/) | Jon Harald Søby; Flag Institute for history | Commons public-domain dedication | St Piran's Cross, a Cornish community flag with nineteenth-century/traditional use. Motif input only. |
| AEX Flanders | [Arms of Flanders SVG](https://commons.wikimedia.org/wiki/File:Arms_of_Flanders.svg); [Flemish Parliament symbol history](https://www.vlaamsparlement.be/nl/parlementair-werk/dossiers/dossiers/vlaamse-symbolen) | Tom Lemmens; Flemish Parliament for history | CC0 1.0, vector dated 2010 | Generic historical arms of Flanders. Use the lion motif; do not backdate the postwar official flag as a 1936 state flag. |
| AFX Wallonia | [Flag of Wallonia SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Wallonia.svg); [1913 Walloon Assembly history](https://connaitrelawallonie.wallonie.be/histoire/timeline/3-juillet-1913-officialisation-du-coq-wallon-de-pierre-paulus-suivie-de-sa) | Tom Lemmens; Walloon history portal | CC0 1.0, vector follows the 23 July 1998 decree | Modern rights-cleared vector of the rooster motif selected in 1913. It is not a copy of Paulus's restricted original watercolor. |
| AGX Frisia | [Frisian flag SVG](https://commons.wikimedia.org/wiki/File:Frisian_flag.svg); [Province of Fryslân history](https://www.fryslan.frl/fy/fryske-flagge) | P. H. Wagemakers and Joh. Koopmans; Province of Fryslân for history | Public domain; current vector revision dated 2026 | West Frisian provincial flag; the design was recognized by the provincial executive in 1897. Motif input only for the bounded Friesland package. |
| AJX Saar | [Territory of Saar Basin flag SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Saar_1920-1935.svg); [historical source summary](https://www.crwflags.com/fotw/flags/de-sl920.html) | Thommy / Thommy9; historical summary cites Saar Governing Commission reporting | Public-domain dedication | Exact flag of the League-governed Saar territory, 28 July 1920 to 1 March 1935. Candidate only for a route explicitly owning that commission legacy. |

The source SVG and source PNG render are retained for each motif. Processed PNGs
are neutral 600x400 review cards, not flag masters.

## Sourced portrait provenance and route ownership

| Runtime stem | Source and identity evidence | Creator, date, rights | Processing | Route lock |
|---|---|---|---|---|
| `portrait_BRI_francois_debeauvais` | [Breiz Atao party-congress photograph](https://commons.wikimedia.org/wiki/File:Breiz_Atao_-_2_septembre_1928_-_le_comit%C3%A9_directeur_et_les_d%C3%A9l%C3%A9gu%C3%A9s_alsaciens_et_corses.jpg); [CRBC authority record](https://crbc.huma-num.fr/prelib/personne/378/) | Anonymous `Breiz Atao`, 2 September 1928; PD anonymous-expired in the United States and source-country terms | Fixed crop around the Commons-identified Debeauvais annotation, grayscale autocontrast, mild sharpening, 156x210 resize | Breton nationalist route only; archival low fidelity accepted by the main agent on 2026-07-14 |
| `portrait_RHI_josef_friedrich_matthes` | [Library of Congress item](https://www.loc.gov/pictures/item/2014695969/); [Deutsche Biographie identity record](https://www.deutsche-biographie.de/dbo100308-7.html?language=de) | Bain News Service, 22 November 1923; Library of Congress rights advisory: no known restrictions on publication | Fixed head-and-torso crop, grayscale autocontrast, mild sharpening, 156x210 resize | 1923 Rhenish separatist/republic route only |
| `portrait_BAY_rupprecht_of_bavaria` | [Franz Grainer portrait](https://commons.wikimedia.org/wiki/File:Rupprecht_von_Bayern_01.jpg); [Munich NS Documentation Center biography](https://www.nsdoku.de/lexikon/artikel/rupprecht-von-bayern-723) | Franz Grainer, circa 1916; PD-Art / PD-old-auto-1923, author died 1948, United States term expired | Fixed head-and-torso crop, grayscale autocontrast, mild sharpening, 156x210 resize | Bavarian traditional crown/restoration route only |

No face was generated, reconstructed, colorized with invented detail, or replaced.
The processing script performs conventional crop, tonal normalization, resize,
and mild sharpening only.

## Rejected and blocked sources

| Package | Candidate | Decision |
|---|---|---|
| SCO | [Roland Muirhead papers and related portrait research at the National Library of Scotland](https://manuscripts.nls.uk/repositories/2/resources/9259) | Rejected for asset production: the archive record warns that access and reuse are subject to copyright restrictions; no cleared period portrait was identified. |
| WLS | [Saunders Lewis, 4 October 1973](https://commons.wikimedia.org/wiki/File:Saunders_Lewis_(1520394).jpg) | Rejected for this 1936 package despite CC BY-SA 4.0: it is a postwar 1973 portrait and no approval exists to use later imagery. |
| BRI | [François Debeauvais in Ouest-Eclair, 10 August 1932](https://commons.wikimedia.org/wiki/File:Debeauvais.png) | Rejected for final production: the page supplies a France public-domain rationale but no United States public-domain rationale. The lower-quality 1928 dual-jurisdiction source is used instead and disclosed. |
| AEX | [Current official Flemish flag](https://commons.wikimedia.org/wiki/File:Flag_of_Flanders.svg) | Not used as a 1936 state flag. The source is CC0, but official adoption is postwar; only the historical lion-arms motif is retained. |
| AFX | [Original Pierre Paulus rooster history and watercolor](https://connaitrelawallonie.wallonie.be/histoire-et-symboles/symboles/le-drapeau-wallon) | Original watercolor not copied. The official history page identifies museum/province rights; the CC0 modern vector is used only to evidence the 1913 motif. |
| ICE | [Hermann Jónasson in Nordens kalender, 1937](https://commons.wikimedia.org/wiki/File:Herman_Jonass%C3%B3n.jpg) | Rejected for final production: exact-period identity is strong, but the Commons page lacks a United States public-domain tag. |

Blocked means no substitute file was created. Generated fictional/institutional
art remains a separately labeled generated-art responsibility and may not be
passed off as a sourced portrait.

## Registered vanilla reuse audit

The following installed flag families were inspected at normal, medium, and
small sizes. Every listed family has a complete triplet for each installed
variant. No vanilla binary was copied into Chaos Redux.

| Tag | Installed family | Reuse boundary |
|---|---|---|
| SCO | ideology-specific SCO triplets | Saltire for civic/national identity; Royal Banner only for an explicitly royal route |
| WLS | ideology-specific WLS triplets | accepted registered-tag reuse, with the 1959 design-date caveat stated above |
| BRI | base plus communism, fascism, and neutrality triplets | Gwenn-ha-du base is a period regional identity; variants remain route-owned |
| RHI | ideology-specific RHI triplets | green-white-red belongs to the Rhenish-republic direction, not every route |
| BAY | ideology-specific BAY triplets | white-blue civic and crowned/royal variants remain politically distinct |
| ICE | base plus communism, fascism, and neutrality triplets | existing cross identity is period-valid; generated alternate routes stay separate |

Historical distinction sources for the registered identities:

| Tag | Source | Distinction supported |
|---|---|---|
| SCO | [Scottish Government flag guidance](https://www.gov.scot/publications/flag-flying-on-government-buildings/pages/guidance/); [Royal Banner history](https://www.royal.uk/royal-banner-royal-arms-scotland?page=1) | The Saltire is the general Scottish flag; the Lion Rampant is the sovereign's royal banner in Scotland. |
| WLS | [Flag Institute Wales registry](https://www.flaginstitute.org/wp/flags/wales-flag/) | The current green-white field with red dragon was officially adopted in 1959, while the dragon emblem is much older. |
| BRI | [Région Bretagne symbol history](https://www.bretagne.bzh/actualites/triskell-hermine-gwenn-ha-du-les-symboles-de-la-bretagne-pour-les-nuls/) | The Gwenn-ha-du was adopted as a Breton symbol at a 1923 regionalist congress and is therefore a period regional identity. |
| RHI | [Regional history of the 1923 proclamation](https://www.1914-1930-rlp.de/bibliothek/aufsaetze/ausrufung-der-rheinischen-republik-1923-in-mainz.html); [Bad Kreuznach archive flag study](https://www.bad-kreuznach.de/buergerservice/politik-und-verwaltung/haus-der-stadtgeschichte-und-stadtarchiv/projekte/publikationen/demnaechst-im-haus-der-stadtgeschichte/die-ebernburger-separatistenfahne-von-1923/) | Separatists raised green-white-red Rheinland flags in 1923; this does not make the tricolor universal to every Rhineland route. |
| BAY | [Bavarian State Portal](https://www.bayern.de/der-freistaat/); [Bavarian Palaces historical note](https://schloesserblog.bayern.de/tipps-aktuelles/jetzt-wieder-mit-weiss-blauer-raute-die-instandsetzung-des-wittelsbacherturms-auf-der-burg-trausnitz) | White-blue is the civic state-color family; the striped state flag dates to 1878, while royal arms and crowns remain dynastic route material. |
| ICE | [Government of Iceland flag history](https://www.mfa.is/topics/governance-and-national-symbols/icelandic-national-flag/history/) | The cross design was specified in 1915 and became the sovereign maritime/national flag in 1918. |

Installed portrait precedents were also inspected:

- vanilla RHI provides `gfx/leaders/RHI/portrait_RHI_josef_matthes.dds`;
- vanilla BAY provides `gfx/leaders/BAY/portrait_BAY_rupprecht_of_bavaria.dds`;
- base ICE provides `gfx/leaders/ICE/portrait_ice_sveinn_bjornsson.dds`;
- Arms Against Tyranny provides ICE portraits for Hermann Jónasson and Sveinn
  Björnsson.

The new RHI and BAY DDS files are mod-owned derivatives of public-domain source
images and therefore do not require a DLC portrait dependency. They still retain
the route locks above.

## Runtime portrait files and proposed sprites

| Proposed sprite | Texture file | Status |
|---|---|---|
| `GFX_portrait_BRI_francois_debeauvais` | `gfx/leaders/006_independence_wave/portrait_BRI_francois_debeauvais.dds` | registered; nationalist route only; archival low fidelity accepted with the route lock retained |
| `GFX_portrait_RHI_josef_friedrich_matthes` | `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | registered; separatist/republic route only |
| `GFX_portrait_BAY_rupprecht_of_bavaria` | `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | registered; restoration route only |

All three runtime files are 156x210, one-mip, uncompressed BGRA DDS. The main
agent owns `.gfx` registration and character wiring.

## Delivered-file hashes

SHA-256 hashes below cover every source, processed review file, contact sheet,
and runtime DDS in this package.

| File | SHA-256 |
|---|---|
| `source_svg/country_symbols/acx_st_pirans_cross_source.svg` | `3d257c4f792664b3215e7e46c8ac625cb9949dd53e932cfea0f2517f1d036a3c` |
| `source_svg/country_symbols/aex_flemish_lion_arms_source.svg` | `9e7c0efcef911a4fbcab37f7c8097b5ab591b7a92a9e44a9105878fbccf7b13f` |
| `source_svg/country_symbols/afx_walloon_rooster_source.svg` | `0d8dd085216df49082c3bb1d54df043f916ebbe8d155dd1774206d6c73e2c076` |
| `source_svg/country_symbols/agx_west_frisian_flag_source.svg` | `5225c8b1b18882a51a76a1cc7e52cc7e369e353ee48c3c82a0a0a00d64f2abf5` |
| `source_svg/country_symbols/ajx_saar_territory_1920_1935_source.svg` | `f09df675c2223a6514f999bfe01f47750f219bad9b10d8fbba1b0d368d883f00` |
| `source_png/country_symbols/acx_st_pirans_cross_source.png` | `72c2db524f5b7c30e1aa71e0b034bd28c29c1d52469c9404ebbbe97636a7bf7d` |
| `source_png/country_symbols/aex_flemish_lion_arms_source.png` | `96a6355500dedd16825a0d6047e4bf9382b1b789c12cdf4e12ab5526c7aa5384` |
| `source_png/country_symbols/afx_walloon_rooster_source.png` | `a359ae5972731fc4f10f59167a250b3c7f0003a702f9cd977282a0d6af527671` |
| `source_png/country_symbols/agx_west_frisian_flag_source.png` | `1c78257755e0ea6d8f225cb228f376cf63105e328ce4227807b3bf96a52b0697` |
| `source_png/country_symbols/ajx_saar_territory_1920_1935_source.png` | `b70a11b417b6422a85a769c1d8add4d4fbee88cfc55d012183bb3c29d6e269e0` |
| `source_png/portraits/bay_rupprecht_of_bavaria_source.jpg` | `143a06bc3703fb6bf7da61d1e1f04a99a4f4afdcf11f940ba7b2c30cae9b9148` |
| `source_png/portraits/bri_francois_debeauvais_group_source.jpg` | `47d35fa91749eeda405105c4df7c2a90f87c29d691b6efdbccc916a3df96ec11` |
| `source_png/portraits/rhi_josef_friedrich_matthes_source.jpg` | `230c415ea7d94cc4725c2435a52376c1724475b3f6cfabdfcda6562240b19dcd` |
| `processed_png/country_symbols/acx_st_pirans_cross.png` | `489bf36c1296e9cd0a4b1e81426f6c7e85d7cbf47b9b56c0c3a5323d63122af8` |
| `processed_png/country_symbols/aex_flemish_lion_arms.png` | `78116c68ad77dc84e1d7040e194fe35e4a6073c21a68eb91bc15e2174d76fae0` |
| `processed_png/country_symbols/afx_walloon_rooster.png` | `421817b5aa3cc9401385ba78a7794bc2a17d6fea7afc1167381a5075244c858a` |
| `processed_png/country_symbols/agx_west_frisian_flag.png` | `71b1e1b433a2acbceb5d0515ea78bbc1211068e2c2980477bf41bc60c514d7cf` |
| `processed_png/country_symbols/ajx_saar_territory_1920_1935.png` | `ea6cf5e133a6255df14ecbbbd59f680992225434cfaee3d133c47d6ac7aee08f` |
| `processed_png/portraits/portrait_bay_rupprecht_of_bavaria.png` | `c54415e0c45a450b18271cb41b08db10112573e141ad219338b2d579d8d160b0` |
| `processed_png/portraits/portrait_bri_francois_debeauvais.png` | `d9dc4e8456deef9828ee1cb3d58cf6577d0c74ca348f28ad67ec6f5cbc888540` |
| `processed_png/portraits/portrait_rhi_josef_friedrich_matthes.png` | `ea3ea5e94e72753d01de93a7b350e582145a4dff217bfe820022ecefa4f5a154` |
| `contact_sheets/006_northern_western_europe_sourced_assets.png` | `17986da7fbc8873197bb09beae5af75e88b4d90447226e9efc227d19ce8c1d6f` |
| `contact_sheets/006_northern_western_europe_final_dds_decoded.png` | `f3eda364195e534e02a3aed53ec77309fd5133c396ee33168a32fa876a8db370` |
| `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | `103ca2bc1e9290c712ae8548050a2a5cc9cd61c0e9eec4acdc213b24eeece423` |
| `gfx/leaders/006_independence_wave/portrait_BRI_francois_debeauvais.dds` | `2d480b6b240c4a31da7a66f70e69042de8a8ddfaed954107eccda4efcb76ef4e` |
| `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | `ad724ee9adb2f7be5daedf6654a41fbb52f0e1ce16f24ca6f9fbef0f45b523f2` |

## Remaining blockers and omissions

This source tranche does not complete the package art:

- ACX, AEX, AFX, AGX, and AJX still require separately labeled generated civic
  baseline flag triplets after the generated artist consumes the motif and route
  distinctions above.
- Institutional council portraits for those five packages remain generated-art
  work.
- SCO, WLS, and ICE have no new rights-cleared real portrait in this package.
- BRI has a legally cleared, route-locked archival portrait whose low fidelity
  was accepted by the main agent; the sharper 1932 image remains rejected.
- No ideology-specific or cosmetic flag filename was guessed for any Group B
  package.

No fallback, invented historical symbol, or unlicensed substitute was produced.
