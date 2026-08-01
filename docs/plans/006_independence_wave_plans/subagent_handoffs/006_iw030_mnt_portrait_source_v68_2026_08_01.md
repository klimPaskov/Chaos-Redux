# Event 006 IW-030 MNT sourced male portrait roster handoff v68

Date: 2026-08-01.
Subagent: `/root/event6_mnt_portraits_research_v68`.
Scope: sourced archival male portrait evidence for the vanilla Montenegro `MNT` roster.

## Outcome

The v68 package proves two named male candidates through unchanged attributed archival masters, exact Pillow crops with decoded-pixel equality evidence, source-locked HOI4-style ImageGen repaints, deterministic 156x210 candidates, and a separate likeness/style/provenance audit.
`MNT_blazo_jovanovic` and `MNT_blazo_dukanovic` are visually accepted evidence candidates but remain `needs_user_review` because their public-domain claims involve unknown photographers and need a final rights decision.
`MNT_kristo_popovic` remains `blocked`; no defensible archival author/source/date chain was found for the generic consumer replacement.
No DDS, `.gfx` wiring, character edit, history edit, localisation edit, advisor icon, or runtime promotion was made.

## Package

All generated/source PNG evidence for this tranche is in one workspace: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v68_2026_08_01/`.
The package manifest is `manifest.md`.
The source/crop equality records are under `crop_metadata/`.
The raw source-locked repaint record is `imagegen_source_lock_v68.md`.
The independent visual audit is `audit_v68.md` with native and 4x sheets at `review/mnt_v68_audit_native.png` and `review/mnt_v68_audit_4x.png`.
The multi-candidate contact sheet is `review/mnt_v68_roster_contact_sheet.png`.
The parent-facing sprite boundary is `gfx_handoff.md`.
The row-level requirement crosswalk is `coverage.md`.

## Candidate matrix

| Consumer | Candidate/source | Source/date/role fit | Rights/provenance | Visual audit | Disposition |
| --- | --- | --- | --- | --- | --- |
| `MNT_blazo_jovanovic` | Blažo Jovanović, Commons Livno group, 1942, central subject identified by caption. Master `source_masters/mnt_blazo_jovanovic_livno_1942.jpg` SHA-256 `a66cf887c8b28f86c92dedd763b3cb6bd046c01f6dff0f63825c07f30c64c120`; crop `[300,80,720,850]` SHA-256 `fd5834027ece9dce94c7dd0f5a7f9b0b74559a85c2653619bc890b3fe117b880`; raw repaint SHA-256 `4022dee805b4be1364d51f7fa481b66e706e93b7a1239c39931ca697e358e989`; candidate SHA-256 `769ae8ccd0fc3bd4ddd2ced1918b21ae37c1c281bd644c8c6df231d20c684b72`. | Real male Montenegrin partisan leader and corps commander; 1942 is later than 1936 but period-authentic active life. | Commons `PD-because` claim and znaci.net credit; photographer unknown, so legal/public-domain clearance remains open. | `PASS` likeness, male/framing/artifacts, HOI4 style, source/crop linkage; `NEEDS_USER_REVIEW` rights. | Evidence-only candidate; do not convert or wire. |
| `MNT_blazo_dukanovic` | Blažo Đukanović, Commons military portrait estimated 1938–1940. Master `source_masters/mnt_blazo_dukanovic_1938_1940.jpg` SHA-256 `b099dff0ad5b45d8dd33a10c9a0ccc113d4e08afa8ca1fa7c2d5fe68b76a8be8`; crop `[30,20,420,475]` SHA-256 `b626fe6089e3483f89a7fc0d553b69b16fa52ce8116b696d2f6e3362ec318cd9`; raw repaint SHA-256 `af610f67ae7001d1348b6fda966f2c9e2e570dd670c25a992d0df3dfcf271874`; candidate SHA-256 `b5535b51c6cca13ad5dba381ad032e690c1ae3100a360e5b0c6fad646f3d73ae`. | Real male Montenegrin/Yugoslav officer, fascist-route country leader, and corps commander; the estimated date brackets the 1936-era setting. | Commons credits Bjelajac’s 2004 military-biography volume and asserts `PD-old`/PDM; photographer/book-reproduction chain is still unknown and needs legal review. | `PASS` likeness, male/framing/artifacts, HOI4 style, source/crop linkage; `NEEDS_USER_REVIEW` rights. | Evidence-only candidate; do not convert or wire. |
| `MNT_kristo_popovic` | Commons `Krsto_Zrnov_Popovic.jpg` and Montenegrina article image retained under `rejected_candidates/`. | Identity and 1881–1947 life dates are historically fit, but neither image provides a defensible capture date or archival author/source chain. | Commons CC BY-SA 3.0/VRTS lacks machine-readable author/source/date; Montenegrina has no image license and prohibits further distribution or unauthorized exploitation. | No crop, repaint, or candidate made; source gate fails before visual pipeline. | `blocked`; do not relabel Jovanović/Đukanović or generate a substitute. |

## Source URLs and rights notes

Jovanović source: <https://commons.wikimedia.org/wiki/File:Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>; original <https://upload.wikimedia.org/wikipedia/commons/a/ab/Grupa_vojnih_rukovodilaca_u_oslobo%C4%91enom_Livnu.jpg>; source collection <http://www.znaci.net/fotogalerija/fotogalerija06.html>.
Đukanović source: <https://commons.wikimedia.org/wiki/File:Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>; original <https://upload.wikimedia.org/wikipedia/commons/7/77/Bla%C5%BEo_%C4%90ukanovi%C4%87.jpg>; credited source is Mile S. Bjelajac, *Generali i admirali Kraljevine Jugoslavije: 1918–1941* (2004).
Popović Commons lead: <https://commons.wikimedia.org/wiki/File:Krsto_Zrnov_Popovic.jpg>; original <https://upload.wikimedia.org/wikipedia/commons/2/25/Krsto_Zrnov_Popovic.jpg>; license CC BY-SA 3.0 with VRTS permission but author/source/date absent.
Popović Montenegrina lead: <https://montenegrina.net/pages/pages1/istorija/cg_izmedju_1_i_2_svj_rata/general_krsto_zrnov_popovic.htm>; image <https://montenegrina.net/images/istorija/krsto_zrnov_popovic.jpg>; article by Novak Adžić, but image credit/date/license absent and the site terms prohibit further distribution or unauthorized exploitation.

## Identity ownership and roster fit

Vanilla `common/characters/MNT.txt` owns all three ids and assigns each country-leader plus corps-commander roles; the Event 006 MNT branch recruits the same ids synchronously.
Search terms covered exact and transliterated forms `Blažo Jovanović`, `Blazo Jovanovic`, `MNT_blazo_jovanovic`, `Blažo Đukanović`, `Blazo Dukanovic`, `MNT_blazo_dukanovic`, `Krsto Popović`, `Krsto Zrnov Popović`, and `MNT_kristo_popovic` across the current Chaos Redux tree and installed vanilla character/history/GFX/interface/localisation roots.
No cross-country owner or transfer contract was found, so same-owner source replacement would not need a transfer guard once a candidate is legally admitted.
All three subjects are male; no female metadata or female source entered the package.

## Parent wiring boundary

The existing vanilla sprite contracts remain `GFX_portrait_Blazo_Jovanovic`, `GFX_portrait_MNT_blazo_dukanovic`, and blocked generic `GFX_portrait_europe_generic_land_19` for Popović.
No final DDS path is assigned because the user explicitly bounded this tranche to source/evidence and prohibited runtime promotion.
Parent must not wire a raw source, merely resized photograph, candidate PNG, rejected Popović lead, or any file under `docs/assets/`.
If rights and full-roster admission later pass, the parent may convert the approved 156x210 candidate through the repository converter and choose a stable engine-facing path under `gfx/leaders/006_independence_wave/` while preserving sprite names.

## Remaining blockers

1. `MNT_kristo_popovic` still has no defensible archival source with author/source/date/rights evidence, so the generic consumer cannot be replaced in this tranche.
2. Jovanović’s Commons public-domain rationale has an unknown photographer and needs a final rights decision.
3. Đukanović’s Commons public-domain assertion covers an unknown-photographer book reproduction and needs a final rights decision.
4. The broader IW-030 package remains outside runtime admission until the parent resolves its independent country-package and shared-focus gates.

No simplification was hidden: the Popović gap is reported as blocked, and the two visual candidates remain evidence-only rather than being promoted without rights clearance.
