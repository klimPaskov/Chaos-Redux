# IW-043 CHU Musa Dzhalil source-clearance handoff

Date: 2026-08-02 (Europe/Kyiv).

Scope: bounded source-authority, reuse-rights, identity/date, role-fit, and evidence-ledger review for the existing `CHU_independence_wave_bolgar_civic_presidium` Musa Dzhalil portrait chain. No gameplay, character, localisation, `.gfx`, DDS, tag, advisor, small/dossier, or source-image file was edited or created. The existing crop and HOI4-style repaint remain preserved.

## Executive disposition

**Status: `needs_user_review` / no-wire.** Identity and baseline-era fit are supported by official museum evidence, but the source is not rights-cleared for mod redistribution. Commons provides an uploader `PD-old` declaration for an unknown-author file; the credited museum catalog identifies the displayed object as a 2021 reproduction and its current terms require permission for reproduction. No explicit museum reuse grant or identified photographer-rights basis was found.

## Authority and rights evidence

- [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Musa_Dzhalil,_1930s.jpg) was checked live on 2026-08-02. Its API reports 594x931, `DateTimeOriginal=1930s`, `Artist=Unknown author`, `Credit=collections.museum.tatar.ru`, `LicenseShortName=Public domain`, and the direct original `https://upload.wikimedia.org/wikipedia/commons/6/60/Musa_Dzhalil%2C_1930s.jpg`. The file wikitext contains `{{PD-old}}` and an empty `permission=` field. This is a Commons uploader assertion, not an explicit permission from the museum or an identified photographer.
- [National Museum of Tatarstan object 332016](https://collections.museum.tatar.ru/entity/OBJECT/332016) was checked through its live API. The catalog title is `Репродукция с фотографии. Муса Джалиль. 1930-е гг. ... 2021 г.`; the item is a 2021 paper reproduction from a photograph, created in Kazan, record `НМРТ В-24959/4`. The catalog confirms the museum as collection authority but contains no item-level license or reuse grant.
- The museum's [terms of use](https://collections.museum.tatar.ru/terms-of-use) state that site images/text are for personal noncommercial, educational, or media use; reprint is allowed only by agreement with the museum; and whole or partial reproduction requires prior written permission. The footer states all rights reserved. A mod portrait distributed with Chaos Redux therefore remains permission-gated; the terms cannot be treated as a blanket public-domain or redistribution license.

The unresolved gate is exact: obtain written permission covering reproduction/adaptation and redistribution of this image or replace the source with an explicitly reusable archival original whose rights chain is independent of the 2021 museum reproduction. Because the credited museum object is a 2021 reproduction rather than the original negative or a contemporaneous archive scan, the strict real-person portrait gate should also treat the current master as provenance-uncertain until an archival original or permission record is supplied. Do not infer legal acceptance from the Commons `PD-old` template.

## Identity, date, and role fit

The official [Musa Dzhalil apartment museum](https://m-jalil.tatmuseum.ru/) identifies Musa Mustafovich Zalilov (Musa Dzhalil) as a Tatar poet and literary/public figure and gives his lifespan as 1906–1944. This supports the grounded male identity classification, survival through the Event 006 1936 baseline, and broad Volga/Tatar civic role fit. The 1930s date is broad but era-appropriate. It does **not** establish that Dzhalil historically held the fictional `Bolgar civic presidium` office; that label is a route-level thematic assignment and should not be documented as a historical office.

The existing subject-ownership search remains valid: no current Chaos Redux or installed vanilla character, recruitment, portrait, leader, commander, operative, or officeholder consumer owns Musa Dzhalil, and no transfer contract is needed. This finding does not authorize wiring while the source-rights gate is open.

## Preserved evidence and hash reconciliation

The following existing files were not changed and their ledger values remain current:

| Evidence | Path | SHA-256 |
| --- | --- | --- |
| Immutable source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/source_masters/volga/chu_musa_dzhalil_commons_1930s.jpg` | `c7e92f3b1e939cfcfcc67a06ab455ab101b8f04509aab75a245d7da97a74869f` |
| Exact head-and-shoulders crop | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/source_crops/CHU_bolgar_civic_presidium_musa_dzhalil_head_shoulders.png` | `9a50cda37b2be6754c1722c4379eb9272adf36a8dd0f12cb11f2108922d64eb0` |
| Raw HOI4-style repaint master | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_raw/CHU_bolgar_civic_presidium_musa_dzhalil_hoi4_repaint_v1.png` | `491726ea93d4507d8327a4505fa0aaa14dfb13fb62b5b1be53490fa86d1a2b13` |
| Deterministic 156x210 candidate | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/repaints_processed/CHU_bolgar_civic_presidium_musa_dzhalil_156x210_candidate.png` | `669ccdc9d345659f260b5f4f03c8786f0b06eac2d5c9ce84c4bf8ae13b272015` |
| Processing review sheet | `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/review/CHU_bolgar_civic_presidium_musa_dzhalil_processing_review.png` | `9ce81849f48ec386fd7db2a5d79a3d313c386c7c8aceefcd3587777a74069d69` |

`docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/hashes.sha256` already contains these values; no hash or crop reconciliation is required. The package manifest now records the live authority and terms-of-use blocker.

## No-wire boundary

Keep the existing source master, exact crop, raw repaint, processed candidate, review sheet, and flat-shelf copy as evidence only. Do not create or convert a DDS, edit the existing `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` sprite, alter the character consumer, add an advisor/small/dossier derivative, or admit IW-043 on this row until written reuse permission (or an explicitly reusable replacement source) is documented and the parent reruns the independent identity/style/provenance audit and package admission checks.
