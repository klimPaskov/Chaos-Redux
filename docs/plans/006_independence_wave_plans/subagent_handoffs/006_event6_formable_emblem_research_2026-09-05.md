# Event 006 ASSET-046 formable emblem research handoff

Date: 2026-09-05

Scope: bounded provenance, historical identity, rights, era-fit, and identity-closure research for unresolved ASSET-046 formable and shared league/faction emblems. This handoff does not select, download, generate, process, convert, wire, or promote any visual asset.

Disposition: `blocked` overall. No new ASSET-046 source file, processed PNG, DDS, contact sheet, manifest entry, GFX registration, runtime flag, gameplay file, or admission gate was changed.

## Executive finding

No unresolved ASSET-046 row acquired a defensible emblem candidate in this tranche. The repository's existing 2026-09-02 source audit remains authoritative: only FORM-05 (`MIX`) and FORM-48 (`PFX`) have separate project-owned emblem packages, and neither may be promoted to the shared league mark.

The strongest historical lead, FORM-13 Idel-Ural, is not safe to close from the available evidence. A historical flag description exists, but the source itself says the blue-and-gold tamga flag has no records before a 1933 book and that the only authentic symbol lead is a logo on a 1918 proclamation. The available Commons vectors are later reconstructions, and one is explicitly marked fictitious. The source trail therefore does not establish a rights-cleared, historically attested ASSET-046 emblem.

The shared league mark is also not source-closable by reusing the League of Nations material. The League of Nations 1939 file explicitly states that the League never had an official flag, logo, or emblem and that the displayed design was a World's Fair communication illustration. It is the wrong institutional identity for Event 006's working League of New States and cannot serve as an inherited historical emblem.

## Repository evidence inspected

- `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md` — requires historical-source review before flag/emblem generation, three-size flag ladders, provenance and rights notes, no waving-fabric art, and no runtime fallback.
- `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv` — ASSET-046 is the formable flag/faction-emblem family with flag triplets, UI sizes, and separate `gfx/flags` and `gfx/interface/006_independence_wave/` contracts.
- `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv` — FORM-13 is the `Idel-Ural` family with the current keyed adapter `IDEL_URAL_COMPACTX`; FORM-43 is `Gran Colombian Federation`; the working names do not by themselves authorize an emblem.
- `docs/assets/006_independence_wave/manifest.md` — only the FORM-05 and FORM-48 emblem packages are accepted; FORM-06 through FORM-47 and the shared league emblem remain gated on final identity, motif, source/ownership, palette, route policy, and stable consumer.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_formable_emblem_source_audit_2026-09-02.md` — current full-row disposition, reserved basenames, existing hashes, consumer audit, and the prohibition on cropping flags, faction references, or generic seals into emblems.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_formable_emblem_source_research_2026-08-30.md` — prior FORM-03 and FORM-04 identity/source research; both remain blocked with no common rights-cleared emblem.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_visual_asset_audit_2026-09-03.md` — visual audit confirms ASSET-046 is blocked and that FORM-05/FORM-48 are the only present family-emblem packages.
- `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md`, `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/manifest.md`, and `docs/assets/006_independence_wave/form48_pacific_assets_2026_07_17/manifest.md` — existing FORM-05/39/48 source modes and review states.
- `interface/006_independence_wave_small_assets.gfx` and `interface/006_independence_wave.gfx` — only `GFX_independence_wave_formable_form_05` and `GFX_independence_wave_formable_form_48` are registered; no `GFX_independence_wave_league_emblem` exists.
- Canonical review material `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`, `CATALOG.md`, `flags/contact_sheet.png`, and `icons/factions/contact_sheet.png` — vanilla flag ladders and faction-logo surfaces are reference material only, not ASSET-046 sources.

## External source and rights checks

### FORM-13 — Idel-Ural

1. The [Flags of the World Idel-Ural State page](https://www.crwflags.com/fotw/flags/ru-idurh.html) identifies the 1918 Idel-Ural State and describes a light-blue flag with a gold tamga associated with Golden Horde/Tatar heraldic tradition.
2. The same page expressly cautions that there are no records of the blue flag before Gayaz Iskhaki's 1933 book, calls the 1918 proclamation the only authentic source of an Idel-Ural logo found by its editors, and says that the proclamation does not establish a flag design. This is a historical-identity warning, not sufficient design evidence for a final emblem.
3. [Commons `Flag of Idel-Ural State.svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Idel-Ural_State.svg) is a 2006 uploader-created vector marked public domain by its uploader and sourced to FOTW. The public-domain statement covers that vector rendition, while FOTW's uncertainty remains unresolved for the underlying 1918 design.
4. [Commons `Idel-Ural flag.svg`](https://commons.wikimedia.org/wiki/File:Idel-Ural_flag.svg) is a 2021 CC BY-SA 4.0 reconstruction attributed to an account that is currently a redlink user page. Its own description says the flag was “probably” created in early 1918 and taken from Iskhaki's book; the page is additionally tagged `Fictitious flag`. It cannot be used as a historically attested ASSET-046 emblem.
5. [Commons `Idel-ural ver1.svg`](https://commons.wikimedia.org/wiki/File:Idel-ural_ver1.svg) is CC0, but it depicts an Idel-Ural Legion patch and dates from 2018. It is a WWII collaborationist military patch, not the 1918 Idel-Ural State identity, so it is wrong-era and wrong-identity for FORM-13.
6. [FOTW's copyright and reuse disclaimer](https://www.crwflags.com/fotw/flags/disclaim.html) limits contributor material to a maximum of five percent of the site's content, requires attribution, forbids alteration, and restricts use to non-commercial and non-political purposes. Even apart from the historical uncertainty, that is not a clean redistribution grant for a modified HOI4 mod asset.

Conclusion for FORM-13: `blocked`. Do not download or promote any of the above vectors, do not crop the existing `IDEL_URAL_COMPACTX` flag ladder into an emblem, and do not let the related Volga-Ural Federation (FORM-12) inherit this mark. The exact 1918 proclamation logo would need a stable archival scan, attributable ownership/public-domain or explicit redistribution terms, and parent acceptance of the identity/consumer before any emblem production.

### FORM-43 — Gran Colombian Federation

1. [Commons `Flag of Gran Colombia.svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Gran_Colombia.svg) is a CC BY-SA 3.0 vector by Milenioscuro depicting the 1821–1831 Gran Colombia flag and listing historical reference links, including an ICOM museum object and Señal Memoria material.
2. [Commons `Flag of Gran Colombia (1819–1820).svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Gran_Colombia_(1819%E2%80%931820).svg) is a CC BY-SA 4.0 vector by HansenBCN depicting an earlier flag period. These are modern vector renditions of historical flag designs, not separately sourced ASSET-046 faction emblems.

Conclusion for FORM-43: the flag references are useful leads only; no exact, rights-cleared formable emblem and no stable FORM-43 X-tag/UI consumer are established. Keep FORM-43 `blocked` and do not convert either flag vector into an emblem.

### Shared league/faction emblem

1. [Commons `Flag of the League of Nations (1939).svg`](https://commons.wikimedia.org/wiki/File:Flag_of_the_League_of_Nations_(1939).svg) is a CC BY-SA 4.0 vector based on a flag held by the League of Nations Archives, United Nations Geneva.
2. The file's own historical note states that the League of Nations never had an official flag, logo, or emblem and that the 1939 design was created for the New York World's Fair as a communication illustration rather than by inter-state consultation.
3. [Commons `Emblem of the League of Nations (1939).svg`](https://commons.wikimedia.org/wiki/File:Emblem_of_the_League_of_Nations_(1939).svg) is extracted from that nonofficial flag. Its file license does not change the wrong-identity and nonofficial-status problem.

Conclusion for the shared league mark: `blocked`. The reserved `independence_wave_league_emblem.dds` and `GFX_independence_wave_league_emblem` remain unproduced and unwired. Parent must first decide whether Event 006 needs one universal alternate-history charter mark or family/route-specific marks; only then may the generated-emblem route or a new rights-cleared historical source be commissioned.

## Disposition and next owner

| Area | Disposition | Exact next owner/action |
| --- | --- | --- |
| FORM-01 through FORM-04 and FORM-09 | Preserve prior blocked dispositions; prior flag packages are not emblem sources. | Parent locks identity, motif, palette, route policy, and consumer; then route each family to source-research or generated-emblem production. |
| FORM-05 | Preserve existing complete `MIX` package; it is family-specific and not a universal league substitute. | Parent selects and wires the intended live consumer if desired. |
| FORM-06 through FORM-12 and FORM-14 through FORM-38 | Preserve prior blocked or vanilla-reuse dispositions; no new source was found or selected here. | Parent owns final X/reused identity and consumer gates. |
| FORM-13 | `blocked` after Idel-Ural provenance/rights review. | Parent requests an archival 1918 proclamation/logo source with explicit redistribution terms or keeps the family fail-closed. |
| FORM-39 | Preserve `needs_user_review`; MFX flag package has no emblem. | Parent owns FIJ/PNG/WPG identity, consent, and admission review. |
| FORM-40 through FORM-47 | Preserve prior blocked dispositions; FORM-43 flag vectors are flag-only leads. | Parent locks exact identity and consumer before emblem research. |
| FORM-48 | Preserve existing complete `PFX` package; it is family-specific and not a universal league substitute. | Parent owns PFX wiring and FORM-48 admission proof. |
| Shared league/faction emblem | `blocked`; League of Nations material is nonofficial and wrong identity. | Parent decides universal versus family/route-specific Event 006 mark; then route to the appropriate asset worker. |

## Asset and runtime handoff

No source master, processed PNG, final DDS, contact sheet, source hash, or `gfx_handoff.md` was created because no candidate passed identity and rights review. No exact runtime basename is proposed beyond the already reserved contracts `independence_wave_formable_form_<NN>.dds` and `independence_wave_league_emblem.dds`; do not create or wire those names from the rejected candidates above.

No files outside this handoff were changed. No GFX, GUI, gameplay, country, flag, localisation, manifest, or admission file was changed. No commit or staging was performed.
