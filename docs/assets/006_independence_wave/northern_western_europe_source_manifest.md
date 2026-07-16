# Event 006 northern and western Europe source manifest

## Scope and source-mode boundary

This package covers the bounded Event 006 source tranche for IW-001 through
IW-010, excluding IW-011 Faroe Islands, plus IW-012 Icelandic emergency
republic:

- SCO Scotland;
- WLS Wales;
- ACX Cornwall;
- BRI Brittany;
- Flanders (`BEL_flanders` vanilla cosmetic overlay; legacy AEX source label);
- AFX Wallonia;
- AGX Frisia;
- RHI Rhineland;
- BAY Bavaria;
- AJX Saar;
- ICE Icelandic emergency republic.

The live standalone tags in this source tranche are ACX, AFX, AGX, and AJX.
The legacy AEX label survives only on retained overlay evidence and portrait
staging; it does not define a standalone Flanders flag family.

The files in this source package are historical or community-source evidence.
No generated route flag, fictional council portrait, or generated leader is
included here. The four generated historical-design flag families remain in
the flag-only `northern_western_europe_generated_art_manifest.md`. Current
fictional portrait evidence instead lives in
`portrait_regeneration_male_hoi4_2026_07_16/manifest.md` and is accepted by
`../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md`.
ACX and AEX portrait files are unregistered readiness-pool art only; they do not
authorize standalone release packages. ACX, AFX, AGX, and AJX source PNGs are
exact historical flag-design inputs; the AEX lion remains evidence for vanilla
`BEL_flanders` only. These source-package review PNGs are not runtime flags and
must not be registered as final sprites.

Registered vanilla flags are inspected in place and are not copied into the mod.
This avoids duplicating proprietary game art and preserves the accepted
registered-tag reuse rule.

## Review artifacts

- `contact_sheets/portraits/portrait_rhi_josef_friedrich_matthes_source_candidate_canonical.png`
  shows the attributed archival frame and identity crop, retained ImageGen
  master, processed final, decoded runtime DDS, and canonical vanilla leaders.
- `contact_sheets/portraits/portrait_bay_rupprecht_of_bavaria_source_candidate_canonical.png`
  shows the attributed source, rejected first pass, corrected master, processed
  final, decoded runtime DDS, and canonical vanilla leaders.
- `contact_sheets/portraits/portrait_bri_francois_debeauvais_source_candidate_canonical_blocked.png`
  records the weak but rights-cleared 1928 identity crop and the sharper 1932
  and 1933 candidates rejected on United States rights evidence.
- `contact_sheets/portraits/process_review/` and
  `processed_png/portraits/metadata/` retain the required deterministic
  processor review sheets and exact `(5, 0, 1075, 1440)` edit-master crops.
- `prompts/006_real_portrait_imagegen_provenance_2026_07_15.md` retains the
  complete prompts, input roles, correction history, and no-fallback record.
- `_tooling/build_real_portrait_comparisons.py` assembles evidence only.
  `_tooling/build_northern_western_europe_sources.py` consumes the two approved
  processor outputs and cannot recreate the rejected BRI fallback.

The current combined sourced-assets and DDS sheets show only the two approved
runtime portraits. The rejected earlier BRI approval is retained solely through
the blocker comparison and research record, never as a runtime asset. Those
sheets remain the protected Rupprecht and Matthes exemption evidence; they are
not the acceptance record for the twenty regenerated fictional large portraits
or ten commander-small dossiers.

## Package disposition

| Package | Flag or symbol disposition | Portrait disposition | Binding distinction or blocker |
|---|---|---|---|
| IW-001 Scotland / SCO | Reuse the installed SCO ideology triplets. The Saltire is the civic/national identity. The Lion Rampant is a royal banner and is route-owned, not a neutral substitute. | No mod-owned real portrait delivered. | No rights-cleared, period-appropriate portrait for a supported 1936 Scottish nationalist leader was found. Roland Muirhead material at the National Library of Scotland is subject to copyright restrictions. |
| IW-002 Wales / WLS | Reuse the installed WLS family only under the accepted registered-tag rule. | No mod-owned real portrait delivered. | The familiar red-dragon-on-green-and-white layout was officially adopted in 1959. Its dragon is historical, but the installed flag must not be described as an authentic 1936 Welsh state flag. The only cleared Saunders Lewis portrait found is from 1973 and is excluded by the period rule. |
| IW-003 Cornwall / ACX | St Piran's Cross source delivered; the downstream package uses it as the exact design input for the live ACX historical triplet. | Accepted male fictional institutional and commander art exists only in the unregistered readiness pool. | This is a historical Cornish community flag, not evidence of a sovereign 1936 Cornish state; portrait presence does not resolve the map blocker. |
| IW-004 Brittany / BRI | Reuse the installed BRI base family. The Gwenn-ha-du is a period regional identity, adopted as a Breton symbol in 1923. | Accepted male fictional civic and commander art is governed by the 2026-07-16 package. The historical Francois Debeauvais portrait remains blocked. | The rights-cleared 1928 group source is too weak for identity-preserving editing. Sharper 1932/1933 candidates do not establish defensible United States public-domain status; do not invent a Debeauvais likeness. |
| IW-005 Flanders / AEX | Historical Lion of Flanders arms source retained as overlay evidence. No standalone AEX TGA exists. | Accepted male fictional art exists only in the unregistered readiness pool. | Flanders remains the vanilla `BEL_flanders` cosmetic overlay. Neither the lion source nor readiness-pool portraits create a standalone AEX package. |
| IW-006 Wallonia / AFX | CC0 rooster vector delivered; the downstream package uses it as the distributable flat reference for the 1913 coq hardi identity. | Institutional council remains the accepted opening mode. | Pierre Paulus's restricted original watercolor was not copied; the live triplet preserves the cited red-on-yellow single-charge design. |
| IW-007 Frisia / AGX | West Frisian provincial flag source delivered; the downstream package uses its seven bands and seven pompeblêden as the exact live design. | Institutional council remains the accepted opening mode. | The flag is bounded to Friesland and is not universalized across every Frisian coast. |
| IW-008 Rhineland / RHI | Reuse installed RHI triplets. The green-white-red democratic variant belongs to the 1923 separatist-republic direction, not every Rhineland route. | Josef Friedrich Matthes identity-preserving painted portrait DDS delivered for the separatist/republic route. | The edit preserves the attributed 1923 Bain photograph's face, beret, bow tie, tweed suit, pose, and breast card. Do not use him for a generic neutral corridor, military cabinet, or universal constitutional opening. |
| IW-009 Bavaria / BAY | Reuse installed BAY triplets. White-blue civic state colors and royal/crowned variants must remain route-distinct. | Rupprecht identity-preserving painted portrait DDS delivered for a traditional restoration route. | The corrected edit preserves the attributed c.1916 Grainer face, thin moustache, hairline, expression, uniform, and source-visible orders. Do not use this portrait for a republican or labor opening. |
| IW-010 Saar / AJX | Exact 1920–1935 Territory of the Saar Basin source delivered; the downstream package uses it as the exact unsuffixed live design. | Institutional neutral commission remains the accepted opening mode. | The blue-white-black tricolour ended with the territory on 1 March 1935. No ideology/cosmetic variant is inferred. |
| IW-012 Iceland / ICE | Reuse the installed ICE family. The cross design was specified by royal decree in 1915 and became the national maritime flag in 1918. | No new mod-owned portrait delivered. | Hermann Jónasson's AAT portrait is an installed-DLC option only if the implementation permits that dependency. The exact-period 1937 Swedish-calendar photograph lacks a United States public-domain tag, so it was not copied. |

## Sourced symbol provenance

| Package | Delivered source | Creator or institution | Date and rights | Historical function and allowed use |
|---|---|---|---|---|
| ACX Cornwall | [Flag of Cornwall SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg); [Flag Institute history](https://www.flaginstitute.org/wp/flags/cornwall-flag/) | Jon Harald Søby; Flag Institute for history | Commons public-domain dedication | St Piran's Cross, a Cornish community flag with nineteenth-century/traditional use; exact design input for the live ACX triplet. |
| AEX Flanders | [Arms of Flanders SVG](https://commons.wikimedia.org/wiki/File:Arms_of_Flanders.svg); [Flemish Parliament symbol history](https://www.vlaamsparlement.be/nl/parlementair-werk/dossiers/dossiers/vlaamse-symbolen) | Tom Lemmens; Flemish Parliament for history | CC0 1.0, vector dated 2010 | Historical arms retained only as `BEL_flanders` overlay evidence. It is not an AEX flag input. |
| AFX Wallonia | [Flag of Wallonia SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Wallonia.svg); [1913 Walloon Assembly history](https://connaitrelawallonie.wallonie.be/histoire/timeline/3-juillet-1913-officialisation-du-coq-wallon-de-pierre-paulus-suivie-de-sa) | Tom Lemmens; Walloon history portal | CC0 1.0, vector follows the 23 July 1998 decree | Rights-cleared flat representation of the coq hardi identity selected in 1913; exact distributable design input for the live AFX triplet. It is not a copy of Paulus's restricted original watercolor. |
| AGX Frisia | [Frisian flag SVG](https://commons.wikimedia.org/wiki/File:Frisian_flag.svg); [Province of Fryslân history](https://www.fryslan.frl/fy/fryske-flagge) | P. H. Wagemakers and Joh. Koopmans; Province of Fryslân for history | Public domain; current vector revision dated 2026 | West Frisian provincial flag recognized in 1897; exact design input for the bounded live AGX triplet. |
| AJX Saar | [Territory of Saar Basin flag SVG](https://commons.wikimedia.org/wiki/File:Flag_of_Saar_1920-1935.svg); [Saarland State Chancellery history](https://artsandculture.google.com/story/saarhundert-das-saargebiet-ein-kind-der-internationalen-v%C3%B6lkergemeinschaft-staatskanzlei-saarland/kQWBBjUfmhpHJA?hl=en) | Thommy / Thommy9; Saarland State Chancellery for institutional corroboration | Public-domain dedication | Exact flag of the League-governed Saar territory, 28 July 1920 to 1 March 1935; exact design input for the live unsuffixed AJX triplet. |

The source SVG and source PNG render are retained for each motif. Processed PNGs
are neutral 600x400 review cards, not flag masters.

## Sourced portrait provenance and route ownership

| Runtime stem | Source and identity evidence | Creator, date, rights | Processing | Route lock |
|---|---|---|---|---|
| `portrait_BRI_francois_debeauvais` (reserved; no runtime file) | [Breiz Atao party-congress photograph](https://commons.wikimedia.org/wiki/File:Breiz_Atao_-_2_septembre_1928_-_le_comit%C3%A9_directeur_et_les_d%C3%A9l%C3%A9gu%C3%A9s_alsaciens_et_corses.jpg); [CRBC authority record](https://crbc.huma-num.fr/prelib/personne/378/) | Anonymous *Breiz Atao*, 2 September 1928; dual-jurisdiction public-domain rationale is defensible | Face detail is too weak for identity-preserving editing; no ImageGen operation, processed final, DDS, or sprite registration | Blocked; content-readiness unset pending a stronger attributable dual-jurisdiction source |
| `portrait_RHI_josef_friedrich_matthes` | [Library of Congress item](https://www.loc.gov/pictures/item/2014695969/); [Deutsche Biographie identity record](https://www.deutsche-biographie.de/dbo100308-7.html?language=de) | Bain News Service, 22 November 1923; Library of Congress rights advisory: no known restrictions on publication | Built-in ImageGen identity-preserving edit with canonical vanilla finish references; official leader processor crop `(5, 0, 1075, 1440)`; 156x210 final | 1923 Rhenish separatist/republic route only |
| `portrait_BAY_rupprecht_of_bavaria` | [Franz Grainer portrait](https://commons.wikimedia.org/wiki/File:Rupprecht_von_Bayern_01.jpg); [Munich NS Documentation Center biography](https://www.nsdoku.de/lexikon/artikel/rupprecht-von-bayern-723) | Franz Grainer, circa 1916; PD-Art / author died 1948; source-country and pre-1929 United States terms expired | Built-in ImageGen identity-preserving edit; first pass rejected, thin-moustache correction retained; official leader processor crop `(5, 0, 1075, 1440)`; 156x210 final | Bavarian traditional crown/restoration route only |

No person was generated without a real source. Matthes and Rupprecht were
edited from their attributed archival photographs with explicit identity,
clothing, pose, and route-detail invariants; canonical vanilla portraits were
finish/framing references only. Debeauvais was not edited because the cleared
source could not support identity preservation. Prompt provenance, exact crops,
processor metadata, and visual approval are retained in this package.

## Rejected and blocked sources

| Package | Candidate | Decision |
|---|---|---|
| SCO | [Roland Muirhead papers and related portrait research at the National Library of Scotland](https://manuscripts.nls.uk/repositories/2/resources/9259) | Rejected for asset production: the archive record warns that access and reuse are subject to copyright restrictions; no cleared period portrait was identified. |
| WLS | [Saunders Lewis, 4 October 1973](https://commons.wikimedia.org/wiki/File:Saunders_Lewis_(1520394).jpg) | Rejected for this 1936 package despite CC BY-SA 4.0: it is a postwar 1973 portrait and no approval exists to use later imagery. |
| BRI | [François Debeauvais in Ouest-Eclair, 10 August 1932](https://commons.wikimedia.org/wiki/File:Debeauvais.png) | Rejected: the face is stronger, but the page supplies a France public-domain rationale without a defensible United States public-domain basis. A 1932 foreign publication can remain in the 95-year US term through 2027. |
| BRI | [François Debeauvais in Breiz Atao, 17 September 1933](https://commons.wikimedia.org/wiki/File:19330917_Fran%C3%A7ois_Debeauvais_bless%C3%A9_par_les_Camelots_du_Roi_lors_du_rassemblement_de_Saint-Goazec_dans_Breiz_Atao.png) | Rejected: the record dates the work to 1933 but uses a US rationale asserting publication before 1 January 1931. That contradiction is not defensible. |
| BRI | [Olier Mordrel and François Debeauvais, 30 July 1939](https://commons.wikimedia.org/wiki/File:Breiz_Atao_-_30_juillet_1939_-_Olier_Mordrel_%26_Fran%C3%A7ois_Debeauvais.jpg) | Rejected: the Commons record lacks a sufficient United States public-domain tag. |
| AEX | [Current official Flemish flag](https://commons.wikimedia.org/wiki/File:Flag_of_Flanders.svg) | Not used as an Event 006 standalone flag. AEX is retired from flag production; only the historical lion arms remain as evidence for vanilla `BEL_flanders`. |
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

This table covers only the two protected sourced exemptions and the blocked
Debeauvais identifier. The current fictional runtime inventory, stable
registrations, readiness-pool boundary, hashes, and visual acceptance are owned
by `portrait_regeneration_male_hoi4_2026_07_16/manifest.md` and its final
independent audit.

| Proposed sprite | Texture file | Status |
|---|---|---|
| `GFX_portrait_BRI_francois_debeauvais` | none | reserved identifier only; not registered; content-readiness blocked/unset |
| `GFX_portrait_RHI_josef_friedrich_matthes` | `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | registered; separatist/republic route only |
| `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` | `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | registered; assigned to the existing vanilla Rupprecht character only on the Event 6 restoration route with `set_portraits` |

The two approved runtime files are 156x210, one-mip, uncompressed BGRA DDS.
Their sprite names remain registered. The BRI texture and registration were
removed with the rejected fallback. Character and route wiring remains outside
this asset tranche.

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
| `source_png/portraits/candidates/bri_francois_debeauvais_1932_ouest_eclair_rejected_us_rights.png` | `fec7e2f8ae7d38d714776a40d8eac98c3e1758c5e04c7b7c0750ed9e688a8de4` |
| `source_png/portraits/candidates/bri_francois_debeauvais_1933_breiz_atao_rejected_rights_record.png` | `974acbb5607efc711c871ecf3406d85782398bef059bf77dec6d8036369c3d92` |
| `source_png/portraits/imagegen_edits/portrait_rhi_josef_friedrich_matthes_imagegen_master.png` | `a1ba1a9a6138d9053ed76a408a3ac54b80e7fdd22f06db9b4b6a41edb7bea6f5` |
| `source_png/portraits/imagegen_edits/portrait_bay_rupprecht_of_bavaria_imagegen_candidate_01.png` | `51a2eab19554c68e6dcfbdcaa96c86b06ba729fca06573b1e45904959056a437` |
| `source_png/portraits/imagegen_edits/portrait_bay_rupprecht_of_bavaria_imagegen_master.png` | `321c5d6101d1fb5c2d13748d76aea00b2ffc0f485ec8e3e2c4ff76b50b5dc98b` |
| `processed_png/country_symbols/acx_st_pirans_cross.png` | `489bf36c1296e9cd0a4b1e81426f6c7e85d7cbf47b9b56c0c3a5323d63122af8` |
| `processed_png/country_symbols/aex_flemish_lion_arms.png` | `78116c68ad77dc84e1d7040e194fe35e4a6073c21a68eb91bc15e2174d76fae0` |
| `processed_png/country_symbols/afx_walloon_rooster.png` | `421817b5aa3cc9401385ba78a7794bc2a17d6fea7afc1167381a5075244c858a` |
| `processed_png/country_symbols/agx_west_frisian_flag.png` | `71b1e1b433a2acbceb5d0515ea78bbc1211068e2c2980477bf41bc60c514d7cf` |
| `processed_png/country_symbols/ajx_saar_territory_1920_1935.png` | `ea6cf5e133a6255df14ecbbbd59f680992225434cfaee3d133c47d6ac7aee08f` |
| `processed_png/portraits/portrait_bay_rupprecht_of_bavaria.png` | `739a16b27abd20b5a9515cf7988557aed5d0ab31591a3c20fa3cf33974dc882e` |
| `processed_png/portraits/portrait_rhi_josef_friedrich_matthes.png` | `700dad9e2cf5eb50837eed0f338ac82944d94a5470b9a8cd8cfe666b7d1dd450` |
| `processed_png/portraits/metadata/portrait_bay_rupprecht_of_bavaria.json` | `c8e5dea77c6fbfb3f0143fbb19659162552e4c2df55695d5ac25fcf3082a8f58` |
| `processed_png/portraits/metadata/portrait_rhi_josef_friedrich_matthes.json` | `c1fd555ddc4f22d07e5ff79e9a2fbc1cf977753568bfaf188f5d61d7078c6353` |
| `contact_sheets/portraits/process_review/portrait_bay_rupprecht_of_bavaria_process_review.png` | `21c25103f8b07265174dcfaf22415ca91bf7a5c5a4c38324ac630b8c18bd1e92` |
| `contact_sheets/portraits/process_review/portrait_rhi_josef_friedrich_matthes_process_review.png` | `f7969a6de625809af149701b4012966afa0223fd0a2bd3e77c9d75e067195470` |
| `contact_sheets/portraits/portrait_bay_rupprecht_of_bavaria_source_candidate_canonical.png` | `e8db7046e6df6c1824bc7d3fb81871f3296b530130b0fd5bfb0327052008d92d` |
| `contact_sheets/portraits/portrait_bri_francois_debeauvais_source_candidate_canonical_blocked.png` | `5a69ab6820790338e692c1ea7e0830852020d96f2ed4fdc6bcafb278981f085d` |
| `contact_sheets/portraits/portrait_rhi_josef_friedrich_matthes_source_candidate_canonical.png` | `7b0c83973d58480311ef6a102d173c7d3465d9e25064d6d41547a7d8330c4676` |
| `contact_sheets/006_northern_western_europe_sourced_assets.png` | `d5988197861e7f0dd1d6a3152624387008c82f1a44746962f54b899a843e3110` |
| `contact_sheets/006_northern_western_europe_final_dds_decoded.png` | `8b809e18e3794bcb5d452842b86f1873fe98191f61125a563166c61402b8069f` |
| `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b` |
| `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` |

## Remaining blockers and omissions

This source tranche alone does not complete the package art:

- the downstream generated-art package completes the ACX, AFX, AGX, and AJX
  live historical triplets; AEX is deliberately absent as a standalone flag;
- the accepted 2026-07-16 portrait package completes the twenty fictional large
  portraits and ten commander-small dossiers. ACX and AEX remain unregistered
  readiness-pool art only;
- SCO, WLS, and ICE have no new rights-cleared real portrait in this source
  package. SCO and WLS use the accepted fictional male portrait package;
- the historical Debeauvais route remains blocked: the legally cleared 1928
  face is too weak for identity-preserving editing, while sharper 1932/1933
  candidates fail the United States rights review. The accepted fictional BRI
  civic portrait does not substitute for Debeauvais; and
- custom Event 006 advisor icons remain withdrawn and are not part of either
  portrait authority.
- No ideology-specific or cosmetic flag filename was guessed for any live flag
  package.

No fallback, invented historical symbol, or unlicensed substitute was produced.
