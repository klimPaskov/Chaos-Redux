# Event 006 ASSET-046 formable-emblem source research

Date: 2026-08-30

Scope: source, provenance, rights, era-fit, consumer, and release-gate review for two unresolved ASSET-046 formable emblem rows, FORM-03 and FORM-04.

Disposition: `blocked` / no-change handoff.

No image was downloaded, copied, generated, cropped, processed, converted, or promoted during this tranche. No source candidate, processed PNG, DDS, contact sheet, GFX registration, or gameplay consumer was added. Because no file was downloaded, there is no new source SHA-256 to report. No public-domain or licence status is inferred from a link alone.

## Rows reviewed

| Row | Public identity | Cosmetic identity | Why selected | Status |
| --- | --- | --- | --- | --- |
| FORM-03 | Confederation of the Low Countries | `LCX` | The identity package has an exact constitutional name, member/territory rules, and a retained flag-design package. | `blocked`: no common emblem is attested for this exact alternate-history confederation and the only strong historic unity motif is explicitly excluded. |
| FORM-04 | Rhenish League | `RLX` | The identity package has the strongest league precedent in the reviewed set, with a documented 1254 Rhenish Cities League and an exact two-founder adapter. | `blocked`: the reviewed sources attest leagues, a proclamation, and founder symbols, but no shared Rhenish League emblem that can be legally and historically reused. |

## Exact consumer contract checked

The current Event 006 asset authority reserves one immutable UI texture and sprite per family ID. The two proposed runtime basenames are recorded here for a future owner, but neither is currently registered or consumed.

| Row | Proposed source master | Proposed processed preview | Exact runtime texture | Exact sprite | Expected format and size | Current consumer evidence |
| --- | --- | --- | --- | --- | --- | --- |
| FORM-03 / `LCX` | Not created; package path is intentionally unassigned while blocked. | Not created; package path is intentionally unassigned while blocked. | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_03.dds` | `GFX_independence_wave_formable_form_03` | Transparent 128x128 PNG master/preview; repository-standard one-level uncompressed BGRA DDS after admission. No secondary size is authorized until the parent names the actual UI consumer. | Reserved in `docs/assets/006_independence_wave/manifest.md` and the dated rights handoff only. No matching DDS or sprite exists in `interface/006_independence_wave_small_assets.gfx`, and no exact family emblem consumer was found in the current Event 006 GUI/decision search. |
| FORM-04 / `RLX` | Not created; package path is intentionally unassigned while blocked. | Not created; package path is intentionally unassigned while blocked. | `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_04.dds` | `GFX_independence_wave_formable_form_04` | Transparent 128x128 PNG master/preview; repository-standard one-level uncompressed BGRA DDS after admission. No secondary size is authorized until the parent names the actual UI consumer. | Reserved in `docs/assets/006_independence_wave/manifest.md` and the dated rights handoff only. No matching DDS or sprite exists in `interface/006_independence_wave_small_assets.gfx`, and no exact family emblem consumer was found in the current Event 006 GUI/decision search. |

The two admitted exceptions establish the technical size only: `independence_wave_formable_form_05.dds` and `independence_wave_formable_form_48.dds` are both 128x128 and have package source, processed, final, contact-sheet, and handoff evidence. They do not supply a motif or a consumer for FORM-03 or FORM-04.

The canonical vanilla reference root was checked for the distinction between a flag family and a faction-emblem family. Its faction references use transparent emblem canvases and separate miniature consumers, while the current Event 006 contract reserves 128x128 family emblems. A vanilla flag, flag crop, or generic faction mark is therefore not a valid substitute.

## FORM-03 evidence and rights disposition

| Source | Attribution and licence state | Era and identity fit | Disposition |
| --- | --- | --- | --- |
| [Rijksmuseum, Map of the Seventeen Netherlandish Provinces in the Shape of the Belgic Lion](https://www.rijksmuseum.nl/en/collection/object/Map%2Bof%2Bthe%2BSeventeen%2BNetherlandish%2BProvinces%2Bin%2Bthe%2BShape%2Bof%2Bthe%2BBelgic%2BLion--901991b1f47334fff1a8f1f9e69a1a4a) | Rijksmuseum collection page used as link-only historical evidence. Image author, source-file terms, and redistribution licence were not independently cleared here; no pixels were copied. | It documents a long-standing Netherlandish unity motif, but not the exact decentralized `LCX` confederation. The identity handoff explicitly says Leo Belgicus must not become the principal LCX emblem because vanilla already uses that unified-Netherlands identity. | `rejected`; wrong identity contract even before unresolved image rights. |
| [Benelux official history](https://www.benelux.int/en/information-for-citizens/benelux-union/about-us/history/) and [2019 Benelux prime-ministers declaration](https://www.benelux.int/files/9415/5427/7383/20190402_Decl_Benelux_Summit_EN_Final.pdf) | Official factual sources used link-only. No visual asset was selected and no redistribution claim was made. | The convention is dated 5 September 1944, after the Event 006 baseline, and vanilla already owns the Benelux identity. | `rejected`; post-baseline and duplicate identity. |
| [Belgian official flags and regional symbols](https://www.belgium.be/en/about_belgium/country/belgium_in_nutshell/symbols/flags) | Official factual source used link-only; no regional symbol file was copied and no reuse licence was inferred. | Flemish, Walloon, German-speaking, and Brussels symbols are member identities. Collapsing one into the confederation would violate the LCX member-preservation rule. | `rejected`; member-only symbol, not a common LCX emblem. |
| [Friesland flag history](https://www.friesland.nl/nl/blog/historie/de-vrijheidsgeest-van-de-friezen) | Institutional factual source used link-only; no image was copied and no reuse licence was inferred. | The seven pompeblêden and blue/white waters are tied to historic Frisian regions and cannot stand for Wallonia, Flanders, and the wider confederation. | `rejected`; member-only symbol, not a common LCX emblem. |

The accepted LCX source package is a generated alternate-history river-fork flag, not a historical emblem source. Its retained raw file is `docs/assets/006_independence_wave/low_countries_form03_2026_07_15/source_png/LCX_low_countries_river_fork_imagegen_raw.png`, 1575x998, SHA-256 `472be5afd8e061a99e4e5a4669b42618b9dd649b0814e1943828530a3e43fe16`. This hash is recorded only as existing evidence; the file was not downloaded or changed in this tranche, and the flag cannot be cropped or relabelled into an ASSET-046 emblem.

FORM-03 result: no defensible sourced or redistributable common emblem was found. The row remains blocked until the parent either supplies a directly attested, rights-cleared LCX emblem source or explicitly authorizes a separate generated alternate-history emblem pass with a fixed consumer.

## FORM-04 evidence and rights disposition

| Source | Attribution and licence state | Era and identity fit | Disposition |
| --- | --- | --- | --- |
| [Landschaftsverband Rheinland, 1254 Rheinischer Städtebund](https://rheinische-geschichte.lvr.de/chronicle/1254) | Institutional history portal used as link-only factual evidence. No seal or image file was selected, and the page does not establish a redistributable emblem asset for the revived league. | It records Mainz, Worms, Oppenheim, and Bingen forming a public-peace league and is strong precedent for a river league. It does not attest one common emblem for the exact Event 006 two-state `RLX` adapter. | `blocked`; league precedent without an emblem source. |
| [German Historical Museum, Rhenish separatist movement](https://www.dhm.de/lemo/kapitel/weimarer-republik/innenpolitik/separatistenbewegung) | Institutional history page used link-only. Image/scan reuse terms were not independently cleared; no pixels were copied. | It documents the 1923 Rhenish Republic proclamation, French support, and local opposition. It does not attest a neutral 1936 Rhenish League emblem or a universally accepted symbol. | `blocked`; context only, not an emblem source. |
| [Rhineland-Palatinate State Archive exhibition PDF](https://www.landeshauptarchiv.de/fileadmin/user_upload/Gemeinsame_Dateien/Download/Ausstellungen/Banner_9.pdf) | Archive exhibition link used as factual context. PDF image rights and redistribution terms were not established; no page image was copied. | It supports the 23 October 1923 Koblenz proclamation context but not a shared league seal. | `blocked`; context only, not an emblem source. |
| [Bad Kreuznach city archive, 1923 separatist flag](https://www.bad-kreuznach.de/buergerservice/politik-und-verwaltung/haus-der-stadtgeschichte-und-stadtarchiv/projekte/publikationen/demnaechst-im-haus-der-stadtgeschichte/die-ebernburger-separatistenfahne-von-1923/) | City-archive page used link-only. The page's image reuse licence was not independently cleared; no pixels were copied. | The green-white-red horizontal arrangement is associated with the 1923 separatist episode and is also the basis of vanilla `RHI_democratic.tga`. The identity handoff explicitly forbids copying that arrangement for RLX. | `rejected`; vanilla collision, contested context, and unresolved image rights. |

The accepted RLX source package is a generated alternate-history green/white/red river flag, not a historical emblem source. Its retained raw file is `docs/assets/006_independence_wave/form01_02_04_flags_2026_07_15/source_png/RLX_rhenish_league_river_tricolor_imagegen_raw.png`, 1576x998, SHA-256 `2ffeb4d04c4810c6adb5baf23f466b57c816a318a43a90cc353ec1f77c0fcfb8`. This hash is recorded only as existing evidence; the file was not downloaded or changed in this tranche, and the flag cannot be cropped or relabelled into an ASSET-046 emblem.

FORM-04 result: no defensible sourced or redistributable common emblem was found. A city seal would represent one founder rather than the league, while a 1923 flag would collide with vanilla and misstate the historical continuity. The row remains blocked until the parent supplies a directly attested, rights-cleared Rhenish League emblem source or explicitly authorizes a separate generated alternate-history emblem pass with a fixed consumer.

## References consulted

- Parent asset brief: `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md`.
- ASSET-046 registry row: `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`.
- Formable identity rows: `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`.
- Identity authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form01_04_identity_research_2026_07_15.md`.
- Current rights authority: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asset_rights_research_2026-08-30.md`.
- Current asset audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_assets_audit_current_2026-08-29.md`.
- Existing FORM-03 package: `docs/assets/006_independence_wave/low_countries_form03_2026_07_15/`.
- Existing FORM-04 flag package: `docs/assets/006_independence_wave/form01_02_04_flags_2026_07_15/`.
- Runtime registry and handoff: `interface/006_independence_wave_small_assets.gfx` and `docs/assets/006_independence_wave/gfx_handoff.md`.
- Relevant offline references: `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, vanilla documentation directory, and the canonical `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` flag/faction-emblem references.

## Handoff and blockers

- No source file is selected for either row, so there is no processed PNG, DDS, contact sheet, or source-file SHA-256 to hand off.
- No `gfx_handoff.md` package file was created because there is no runtime candidate to wire. The parent-owned `docs/assets/006_independence_wave/gfx_handoff.md` and `interface/006_independence_wave_small_assets.gfx` were not edited.
- Do not use Leo Belgicus, Benelux, Belgian, Frisian, Dutch, or vanilla RHI symbols as LCX/RLX fallback emblems.
- Do not crop either retained generated flag into a square emblem, and do not treat ImageGen provider output as a historical or public-domain source.
- Before any future production pass, the parent must lock the final family identity, emblem motif, route/ideology policy, and actual UI consumer. The current reserved 128x128 basenames are not proof of runtime reachability.

Files changed by this tranche: this dated handoff only.
