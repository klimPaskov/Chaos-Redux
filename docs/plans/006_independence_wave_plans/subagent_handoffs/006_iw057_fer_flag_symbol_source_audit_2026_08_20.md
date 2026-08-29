# IW-057 Far Eastern Republic flag and symbol source audit

Date: 2026-08-20.

Scope: bounded, read-only refresh of the Event 006 IW-057 Far Eastern Republic (FER) flag and institutional-symbol source gate.

Mode: historical and archival source research only.

## Executive disposition

`status`: `HOLD / FAIL-CLOSED`.

`approved_runtime_candidate`: none.

`FER_INDEPENDENCE_WAVE_PROVISIONALX`: remains blocked and must not be created, installed, or used to publish a package receipt.

The strongest historical-continuity candidate remains `FER-H0-1920-FLAG`, but it is a 1920 design used in a 1936 Event 006 package only as an explicitly documented revival or continuity identity after parent review and rights clearance.

The public-domain `FER-H1-1921-CONST-FLAG` is a constitutional-text reconstruction fallback, not evidence of a distinct attested 1936 flag.

`FER-SYN-CIVIC-1936` and `FER-SYN-RAIL-PORT-1936` remain alternate-history design briefs only and require a separate parent authorization before any generated art task.

No processed PNG, TGA, DDS, GFX definition, cosmetic tag, manifest row, runtime flag, portrait, gameplay file, localisation file, spreadsheet, central admission, or Join surface was changed.

## Inputs and authority checked

The repository guidance and asset workflow consulted were `AGENTS.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md` sections 2.1, 2.2, 3, 6, 7, 8, 8.1, 12, 20, 25, 26, 27, 28, and 29, `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`, and the required core offline wiki pages listed by `AGENTS.md`.

The vanilla documentation consulted for the flag and cosmetic-tag surface was the installed country/flag guidance represented by `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md`; the installed documentation set was also opened for the required core references, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The accepted Event 006 sources checked were `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, the `IW-057` row in `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, the `IW-057` row in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, and the country-flag family row in `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`.

The current package and source handoffs checked were `006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md`, `006_iw057_fer_flag_symbol_research_current_2026_08_15.md`, `006_iw057_fer_symbol_flag_research_handoff_2026_08_15.md`, `006_iw057_fer_next_tranche_planner_handoff_2026_08_15.md`, `006_iw057_far_eastern_republic_package_core_2026_08_15.md`, `006_iw057_far_eastern_republic_package_audit_2026_08_15.md`, `006_iw057_far_eastern_authority_docs_reconciliation_2026_08_15.md`, and `006_iw057_fer_symbol_sources_2026_08_15/fer_symbol_gate_status.md`.

The canonical reference root checked was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, `REFERENCE_MANIFEST.md`, and `flags/` with its normal, medium, small, and contact-sheet shelves.

The canonical reference root contains 21 generic flag references and no FER-specific reference; its README marks every extracted reference as review-only and forbids wiring or copying it into runtime.

## Exact proposed runtime identity

The accepted IW-057 addendum proposes the package-only cosmetic basename `FER_INDEPENDENCE_WAVE_PROVISIONALX` if and only if the parent accepts a source-backed identity.

| Runtime surface | Proposed path | Current status |
| --- | --- | --- |
| Normal flag | `gfx/flags/FER_INDEPENDENCE_WAVE_PROVISIONALX.tga` | Not created; blocked. |
| Medium flag | `gfx/flags/medium/FER_INDEPENDENCE_WAVE_PROVISIONALX.tga` | Not created; blocked. |
| Small flag | `gfx/flags/small/FER_INDEPENDENCE_WAVE_PROVISIONALX.tga` | Not created; blocked. |
| GFX sprite | None; flag filenames are engine lookups. | No GFX handoff because no runtime asset was selected. |

The flag workflow requires uncompressed 32-bit TGA files at `82x52`, `41x26`, and `10x7` with the vanilla bottom-left origin/header convention.

No DDS is proposed for this flag surface because the accepted flag and cosmetic-tag references use TGA lookup files rather than a custom sprite texture.

## Installed vanilla FER ladder audit

Installed source root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

The installed ladder was re-read on 2026-08-20.

All twelve installed files are uncompressed TGA type 2 and 32-bit.

Normal files are `82x52` with descriptor `0x08`, medium files are `41x26` with descriptor `0x08`, and small files are `10x7` with descriptor `0x00`.

All twelve files have origin code `0` and no top-origin bit.

No no-suffix `FER.tga`, `medium/FER.tga`, or `small/FER.tga` exists in the installed ladder.

| Variant | Native design evidence | Event 006 disposition |
| --- | --- | --- |
| `FER_communism` | Red field `#CC0000`, dark-blue upper-hoist canton `#071B54`, canton approximately `35x26` in the displayed `82x52` normal canvas, and red D.V.R. letters arranged in a triangle. | Strong historical-continuity comparison for H0 only; never a neutral/base substitute. |
| `FER_democratic` | Red upper field `#D81E05`, blue lower field `#0359BA`, white hoist triangle, and no documented D.V.R. or constitutional emblem. | Reject as Event 006 identity or historical source. |
| `FER_neutrality` | Green upper field `#00923F`, red lower field `#D81E05`, yellow hoist triangle `#FFD700`, and a detailed emblem with no documented 1920/1921 FER geometry. | Reject as neutral/base source; installed ideology art has no accepted historical provenance. |
| `FER_fascism` | Black, green, and white horizontal bands with no documented FER constitutional emblem. | Reject as Event 006 identity or historical source. |

The H0 colour and canton comparison is not a claim that the vanilla communist file is licensed or historically current for 1936; it only records that the installed file visibly matches the documented 1920 design family.

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

## Historical candidates

The Far Eastern Republic existed from April 1920 until its merger into the RSFSR on 15 November 1922.

No FER flag or emblem is therefore an uninterrupted historically current 1936 state symbol.

Any Event 006 1936 use must be described as a revival, restoration, continuity claim, successor institution, or explicit alternate-history synthesis.

| Candidate | Identity, date, and geometry | Source and rights | Era and disposition |
| --- | --- | --- | --- |
| `FER-H0-1920-FLAG` | FER government design dated 11 November 1920: red field, dark-blue upper-hoist canton, and red D.V.R. letters arranged in a triangle. The archived SVG is `900x600`, with canton width `383.4025` and height `300`. | [Commons reconstruction](https://commons.wikimedia.org/wiki/File:Flag_of_Far_Eastern_Republic.svg) by NuclearVacuum, based on [SHPL scan page 67](http://elib.shpl.ru/ru/nodes/8743#mode/inspect/page/67/zoom/4), marked CC BY-SA 3.0. The reconstruction licence is clear, but the underlying SHPL scan rights are not independently stated. | Strongest route-neutral historical-continuity candidate, not a non-socialist neutral flag. `needs_user_review`; no runtime asset. |
| `FER-H1-1921-CONST-FLAG` | Constitutional wording reconstruction of the red field, dark-blue canton, and red D/V/R triangle. Commons metadata date is 1920-04-06, which is treated as a founding-date marker rather than proof of design adoption. | [Commons constitutional option](https://commons.wikimedia.org/wiki/File:Flag_of_the_Far_Eastern_Republic_(Constitutional_option).svg) credits the FER Constitution/government and marks the reconstruction public domain. It is a text-based reconstruction, not a primary period scan. | Acceptable only as an explicitly named constitutional reconstruction if H0 rights cannot be cleared. `needs_user_review`; no runtime asset. |
| `FER-H2-CONST-EMBLEM` | Article 180 institutional-arms family: red shield, conifer wreath, sunrise, five-pointed silver star, wheat sheaf crossed by an anchor and pointed pickaxe, and D.V.R. letters on wreath ribbons. | [Commons constitutional arms](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_the_Far_Eastern_Republic.svg) and its [second reconstruction](https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_the_Far_Eastern_Republic_2.svg) are marked public domain and credit the Constitution. [Heraldicum](https://www.heraldicum.ru/russia/civilwar.htm#dvr) corroborates the design family. | Institutional seal/banner research reference only; no standalone runtime emblem is accepted or requested. |
| `FER-H3-BANKNOTE-EMBLEM` | Simplified wheat, anchor, and pickaxe motif reported on FER banknotes in 1920. | [Heraldicum banknote image](https://www.heraldicum.ru/russia/images/dvr1.gif); image reuse rights are not stated. | Historical motif evidence only; low-resolution and rights-uncertain; blocked for runtime. |
| `FER-H4-MUSEUM-BANNER` | Photographic evidence of FER banners and variant emblem renderings; exact photograph date is not stated. | [Heraldicum banner photograph](https://www.heraldicum.ru/russia/images/dwr.jpg), credited to the Khabarovsk Regional Museum named N. I. Grodekov; image reuse rights are not stated. | Archive-only context; blocked for runtime. |
| `FER-H5-PRE-1920-PROVISIONAL-EMBLEM` | Earlier provisional-government emblem before the 11 November 1920 approval. | [Heraldicum civil-war reference](https://www.heraldicum.ru/russia/civilwar.htm#dvr) provides text but no dated primary scan or defensible reuse licence in this tranche. | Blocked pending a dated primary scan and rights evidence. |
| `FER-R0-2006-PD-REDRAW` | 2006 redraw of the FER flag, not a historical design date. | [Commons redraw](https://commons.wikimedia.org/wiki/File:Flag_Far_Eastern_Republic.svg) by Szczepan1990, marked public domain, with no historical source for its geometry recorded on the page. | Comparison aid only; reject as sole 1936 identity proof. |
| `FER-SYN-CIVIC-1936` | Proposed non-socialist civic synthesis for a 1936 revival or successor institution using traceable maritime, wheat, conifer, anchor, or administrative motifs. | No artwork, source licence, or historical attestation exists because this is only a design brief. Motifs must remain traceable to H2, H3, and H4 evidence if authorized. | Alternate history only; blocked pending explicit parent authorization and a separate generated-art task. |
| `FER-SYN-RAIL-PORT-1936` | Proposed route-specific railway-port synthesis for the IW-057 force identity. | No artwork, source licence, or historical attestation exists. Railway, port, customs, or coastal additions would be design additions, not attested FER heraldry. | Alternate history only; blocked pending explicit parent authorization and must not replace the historical continuity baseline. |

## Source files, hashes, and hydration state

The durable archive folder is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_symbol_sources_2026_08_15/`.

The three SVG flag sources were re-read locally on 2026-08-20 and their bytes match the current Commons downloads.

| Local source file | Provenance and rights | Local or payload SHA-256 |
| --- | --- | --- |
| `flag_of_far_eastern_republic_cc_by_sa_3.svg` | Commons H0 reconstruction; NuclearVacuum; CC BY-SA 3.0; SHPL underlying scan rights unclear. | `8e40e542c381cab99b27222f690a77d77a112c18976fd3cd99135b8b5235ff10` |
| `flag_constitutional_option_public_domain.svg` | Commons H1 constitutional reconstruction; FER Constitution/government credit; public domain as marked by Commons. | `2c37b2bec02b66bde60be76e886421091660bb4c02a4ef0ace393a3c26421881` |
| `flag_far_eastern_republic_pd_2006.svg` | Commons 2006 redraw; Szczepan1990; public domain as marked by Commons; no historical-source proof. | `20b08fb6bc102fd3b85f97b2f895e30e7aadbdb6007fee0b02980079d6b9422c` |
| `coat_of_arms_constitutional_public_domain.svg` | Commons H2 constitutional-arms reconstruction; public domain as marked by Commons. | `d706595472ee4ced1de180e321895c825010d6c3bdb69d4a756b3668dc6dbecd` |
| `coat_of_arms_constitutional_variant_2_public_domain.svg` | Commons alternative H2 reconstruction; public domain as marked by Commons; not a verified primary scan. | `076e97c30f5a45b96c89c09b49efe54da172d2ed5543710c65e2f4f81cd246c1` |
| `far_eastern_constitution_1921_worldstatesmen.pdf` | [World Statesmen English translation](https://www.worldstatesmen.org/Far-eastern-constitution1921.pdf), title *Constitution of the Far Eastern Republic (1921)*, author Assembly of the Far Eastern Republic; archive/site reuse rights not stated. | Payload OID `7a62e44e5da3b1886ae88f17ec6ce636b0b42b112561bbc503a2fb66a056b361`; remote payload recheck matched, but the local file is a Git-LFS pointer rather than hydrated PDF bytes. |
| `heraldicum_dvr_constitutional_reconstruction.gif` | [Heraldicum constitutional reconstruction](https://www.heraldicum.ru/russia/images/dvr.gif); reuse rights not stated. | Payload OID `6527f7bc66e765db6dbb805c8d168df4714d736471654339ae416316eda8b4c8`; remote payload recheck matched, but the local file is a Git-LFS pointer rather than hydrated GIF bytes. |
| `heraldicum_dvr_banknote_emblem.gif` | [Heraldicum banknote emblem](https://www.heraldicum.ru/russia/images/dvr1.gif); reuse rights not stated. | Payload OID `404541aaf00a592bff82f24b5f7671d89c59ae62fe892bbe3ab6d4ac570d06aa`; remote payload recheck matched, but the local file is a Git-LFS pointer rather than hydrated GIF bytes. |
| `heraldicum_dwr_museum_banner_photo.jpg` | [Heraldicum museum banner photograph](https://www.heraldicum.ru/russia/images/dwr.jpg), museum credit present; exact date and reuse rights not stated. | Payload OID `51f3328e37d73a19fdd9b0494ff2eded689e445aafe36d1ba83187918a3e143b`; remote payload recheck matched, but the local file is a Git-LFS pointer rather than hydrated JPEG bytes. |

The LFS pointer state is an archive limitation, not permission to promote the remote payloads into runtime.

The Article 180 and Article 181 numbering and wording are retained from the prior source handoff and the Commons/Heraldicum reconstruction chain; direct text extraction of the remote scanned PDF did not independently reproduce those article headings, so the exact article citation remains a review item pending page-image inspection.

The existing `fer_symbol_candidates_contact_sheet.svg` remains review-only and has SHA-256 `1ed2a3cdf13059351276f0dd5097bc5925f963ca426c8ed8178148f8c5810e16`.

## Parent decision gate

If `neutral/base` means route-neutral historical continuity, the parent must explicitly accept `FER-H0-1920-FLAG` as a 1920–1922 revival or continuity identity, resolve the CC BY-SA attribution/share-alike obligations, and resolve or expressly accept the unresolved SHPL scan-rights chain.

If H0 rights cannot be cleared, the parent may explicitly choose `FER-H1-1921-CONST-FLAG` as a public-domain constitutional-text reconstruction and must document that it is a reconstruction rather than a distinct attested 1936 flag.

If genuinely non-socialist neutral visual language is required, the parent must explicitly authorize `FER-SYN-CIVIC-1936` as alternate history and commission a separate generated-art task with motif traceability.

If the railway-port route needs a distinct symbol, the parent must separately authorize `FER-SYN-RAIL-PORT-1936`; it must remain route-specific and cannot replace the historical baseline.

Until one of those choices is recorded, do not create the proposed normal, medium, or small `FER_INDEPENDENCE_WAVE_PROVISIONALX` TGA files and do not set `independence_wave_iw_057_identity_rights_cleared` or any roster receipt.

Do not use `FER_democratic`, `FER_neutrality`, `FER_fascism`, or `FER_communism` as a neutral/base substitute.

Do not substitute Priamur, White-movement, Japanese-backed, RSFSR/Soviet, generic Siberian, or generic railway symbols.

## Completion and blockers

Completed: current package/spec gate review, canonical reference-root review, installed twelve-file FER ladder audit, TGA header/dimension/origin checks, installed ladder hashes, Commons metadata refresh, local SVG hash comparison, remote payload/OID verification for the archived PDF/GIF/JPEG sources, historical-era assessment, and durable documentation.

Blocked: no candidate is runtime-admissible without the parent identity decision and rights/reconstruction disposition.

Uncertainty: the FER state existed only through 1922, so any 1936 use is interpretive; H0 depends on a CC BY-SA reconstruction whose SHPL source rights are not stated; H1 and H2 are reconstructions rather than primary scans; Heraldicum image rights and exact banner date are unstated; four archived binary source files are local LFS pointers rather than hydrated bytes.

No asset production was authorized by the current source contract, so no source PNG, processed preview, final TGA/DDS, manifest row, contact sheet refresh, or `gfx_handoff.md` was created in this audit.

No gameplay, central admission, Join, event, focus, idea, decision, GUI, GFX, localisation, history, country, or spreadsheet file was changed.
