# Event 006 Sicily sourced-real-male portrait refinish trial 01

Status: `independently_approved_and_wired` for Luigi Sturzo, Pietro Lanza di Scalea, and Luigi Rizzo under the independent visual/provenance audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sicily_trial01_portrait_visual_provenance_audit_2026_07_22.md` and the separate current-consumer audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_luigi_rizzo_political_consumer_independent_audit_2026_07_24.md`.

## Scope and method

- Event: `006_independence_wave` (`IW-019` Sicily)
- Source mode: `grounded_source_only` with identity-preserving ImageGen edit
- Subjects: three real male Sicilian identities, no invented or substitute face
- Workflow: unchanged source master -> exact requested crop -> official
  ImageGen edit using the exact crop as Image 1 and one matching canonical male
  HOI4 portrait as style-only Image 2 -> 156x210 opaque RGBA PNG -> repository
  `convert_to_dds.py` -> final one-level uncompressed BGRA DDS
- ImageGen outputs remain separate under `imagegen_masters/`; source masters are
  copied unchanged under `source_masters/` and are never overwritten.
- No advisor art, advisor portrait, `_small` miniature, female portrait, alternate portrait, or generated identity is included.
- The approved large portraits are copied to the runtime paths and registered by the parent-owned GFX and character files.

## Asset ledger

| Result | Grounded role / gender | Exact source and crop | Source provenance | Output files | Status |
|---|---|---|---|---|---|
| `ASX_luigi_sturzo.png` | Country leader / Sicilian provisional assembly; male | `asx_luigi_sturzo_albert_kahn_big.jpeg`, `(520,330,1170,1205)`, source `1519x2048`, crop `650x875` | Albert Kahn collection record and Commons `1925_Luigi_Sturzo.jpg`; Georges Chevalier; 1925; Albert Kahn record/Commons attribution state `CC BY 4.0`; source SHA-256 `4c18893744627c83761ee2b838a18f2f4798026811b888ecfb96d1f1d7a168ec` | `imagegen_masters/ASX_luigi_sturzo_imagegen_master.png`; `processed_png/ASX_luigi_sturzo.png`; `final_dds/ASX_luigi_sturzo.dds`; prompt and crop preview | `independently_approved_and_wired` |
| `ASX_pietro_lanza_di_scalea.png` | Country leader / Sicilian crown council; male | `asx_pietro_lanza_di_scalea_commons_original.jpg`, `(155,15,495,473)`, source `602x800`, crop `340x458` | Commons file “Pietro Lanza di Scalea by Mario Nunes Vais”; ICCD Fondo Nunes Vais; before 1932; Mario Nunes Vais (1856–1932); Commons PD-old/PD-US/PDM tags; source SHA-256 `5cbf419d7f33539e726f0ef4089b1c9995e1bfdbcd8b581f8eaa996659d02f0b` | `imagegen_masters/ASX_pietro_lanza_di_scalea_imagegen_master.png`; `processed_png/ASX_pietro_lanza_di_scalea.png`; `final_dds/ASX_pietro_lanza_di_scalea.dds`; prompt and crop preview | `independently_approved_and_wired` |
| `ASX_luigi_rizzo.png` | Country leader / Sicilian straits-security government; male | `asx_luigi_rizzo_rear_admiral_1935.jpg`, `(70,0,333,354)`, source `402x582`, crop `263x354` | Commons “Rear Admiral Luigi Rizzo in 1935”; *Medaglie d'oro della Grande Guerra*, Rome, 1935; Italian Navy biography; photographer unnamed; Commons PD-Italy and PD-1996/US tags; source SHA-256 `aa113393b9b51ed481bfa485aaf729e867c20c6a364b41d3f8999b0dc2c8663e` | `imagegen_masters/ASX_luigi_rizzo_imagegen_master.png`; `processed_png/ASX_luigi_rizzo.png`; `final_dds/ASX_luigi_rizzo.dds`; prompt and crop preview | `independently_approved_and_wired`; separate audit passes the current civilian-large political consumer with the fictional-office disclosure; no corps-command consumer |

## Source links and rights notes

- Luigi Sturzo: [Commons `1925 Luigi Sturzo`](https://commons.wikimedia.org/wiki/File:1925_Luigi_Sturzo.jpg), [Albert Kahn collection record](https://collections.albert-kahn.hauts-de-seine.fr/document/proprit-d-albert-kahn-boulogne-france-don-luigi-sturzo/617a7a45cf8b8968b338626f?filtrerParThme%5B0%5D=Personnalit%C3%A9&filtrerParDomaine%5B0%5D=Images%20fixes&s=dateDePriseDeVue&so=desc&pos=3482&pgn=231), and [Albert Kahn original image](https://collections.albert-kahn.hauts-de-seine.fr/media/cache/big/61/64/6164609751e082079310c926.jpeg). The source ledger records Georges Chevalier, 1925, and CC BY 4.0 attribution; the parent must re-check the exact derivative-use terms before release.
- Pietro Lanza di Scalea: [Commons `Pietro Lanza di Scalea by Mario Nunes Vais`](https://commons.wikimedia.org/wiki/File:Pietro_Lanza_di_Scalea_by_Mario_Nunes_Vais.jpg), [Commons original via Special:FilePath](https://commons.wikimedia.org/wiki/Special:FilePath/Pietro_Lanza_di_Scalea_by_Mario_Nunes_Vais.jpg), and ICCD Fondo Nunes Vais context. The source ledger records Mario Nunes Vais (1856–1932), before 1932, with Commons PD-old/PD-US/PDM tags; the parent must re-check the rights chain.
- Luigi Rizzo: [Commons `Rear Admiral Luigi Rizzo in 1935`](https://commons.wikimedia.org/wiki/File:Rear_Admiral_Luigi_Rizzo_in_1935.jpg), [Commons original](https://upload.wikimedia.org/wikipedia/commons/b/b0/Rear_Admiral_Luigi_Rizzo_in_1935.jpg), and [Italian Navy biography](https://www.marina.difesa.it/cosa-facciamo/storia/la-nostra-storia/medaglie/Pagine/RizzoLuigi.aspx). The source ledger records *Medaglie d'oro della Grande Guerra*, Rome, 1935, an unnamed photographer, and Commons PD-Italy/PD-1996/US tags; the parent must re-check the rights chain.

## Visual review record (not an approval)

The contact sheet at `contact_sheets/source_crop_result_style_comparison.png`
places each unchanged source, exact crop, raw ImageGen result, processed
156x210 result, and the matching male-only canonical reference family side by
side. The results visibly use modeled brushwork, controlled wartime palettes,
subdued painted backgrounds, and head-and-shoulders framing rather than a
lightly filtered photograph. The face, age, hair, facial hair, expression,
pose, clothing/regalia, and distinctive structure remain source-anchored on
visual inspection; this statement is evidence for the independent auditor, not
producer approval.

Known audit risks:

1. ImageGen necessarily paints hidden/low-resolution detail; compare each result
   directly to the exact crop and reject if the auditor sees identity drift,
   beautification, changed age, changed pose, or substituted clothing.
2. Pietro Lanza di Scalea’s decorations are painted rather than pixel-identical;
   verify that no invented insignia materially changes the source-backed regalia.
3. Luigi Rizzo’s medals and shoulder cords are retained as source-backed visual
   features but are simplified at 156x210; verify that the result still reads as
   the same rear admiral.
4. Rights notes above are inherited from the source ledgers and still require
   the parent’s independent provenance check before distribution.

## Validation evidence

- All processed previews are exactly `156x210`, `RGBA`, and have alpha min/max
  `255/255` (opaque).
- All DDS files are generated by
  `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and have a
  valid legacy one-level BGRA header, `156x210` dimensions, `DDSCAPS_TEXTURE`,
  and exact length `131168` bytes (`128 + 156*210*4`).
- Pillow DDS decode round-trips each final DDS to its processed RGBA PNG
  exactly (`diff.getbbox() is None` for all three files).
- `hashes.sha256` records every source copy, crop preview, prompt, raw
  ImageGen master, processed PNG, DDS, and contact sheet.

## Explicit non-authorization

The visual/provenance audit authorized the three exact processed identities, and the separate current-consumer audit authorizes Luigi Rizzo only for the male civilian-large Straits Security Directorate political role with the recorded fictional-office disclosure.
Their approved DDS files are wired to the current runtime paths.
No fallback or generic face was used.
No advisor, dossier, `_small`, female, alternate, or newly generated identity is authorized.
