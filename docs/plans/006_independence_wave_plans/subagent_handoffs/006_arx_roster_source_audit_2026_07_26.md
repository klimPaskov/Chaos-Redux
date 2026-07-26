# IW-018 ARX grounded male-portrait roster source audit

Date: 2026-07-26  
Owner: sourced visual-asset research subagent  
Scope: source and rights research only for the two unresolved male ARX portrait roles. No gameplay, localisation, GFX, DDS, generated portrait, crop file, or existing asset package was edited.

## Fail-closed result

There is no rights-valid pair ready for runtime admission. Vittorio Vernè is a source-ready commander candidate pending the normal independent visual audit, while the strongest crown identity, Eugenio di Savoia-Genova, is blocked because the available Commons records establish Italian public-domain status but do not establish the United States publication/URAA condition required for safe redistribution.

| ARX role | Identity | Disposition | Reason |
|---|---|---|---|
| `ARX_sardinian_crown_consultative_council` | Eugenio Alfonso Carlo Maria Giuseppe di Savoia-Genova, Duke of Ancona and fifth Duke of Genoa | `blocked_needs_rights_review` | Strong dynastic and 1936-era fit, no active vanilla or Chaos Redux character/portrait owner, but every usable source is tagged `PD-Italy` without `PD-1996` or verifiable United States publication/registration evidence. |
| `ARX_gavino_piras` | Vittorio Vernè | `source_ready_for_parent_review` | Historically active Italian major-general in 1936, explicit Commons `PD-Italy` plus `PD-1996`, no active vanilla or Chaos Redux owner, and a documented Sardinia-linked formation; source quality is low-resolution and must go through the independent portrait audit before any repaint or DDS. |

## Crown candidate: Eugenio di Savoia-Genova

Eugenio Alfonso Carlo Maria Giuseppe di Savoia-Genova (1906-1996) was Duke of Ancona from 1906, the fifth Duke of Genoa, a member of the Savoy-Genova branch, and an Italian naval officer who entered the Navy in 1927 and served in the Ethiopian campaign. He is alive and historically active in the 1936 start window, making him the closest defensible crown-route officeholder found in the requested roster.

The primary Commons source is [File:Prince Eugenio di Savoia-Genova.png](https://commons.wikimedia.org/wiki/File:Prince_Eugenio_di_Savoia-Genova.png), an 870x1252 image credited to M. Ranzani and dated circa 1920, with the source credit [Getty Images record 929528940](https://www.gettyimages.it/detail/fotografie-di-cronaca/portrait-of-eugenio-di-savoia-genova-italian-fotografie-di-cronaca/929528940). Commons applies `PD-Italy` and its permission text expressly says United States status depends on pre-1978 publication and the absence of a United States registration; no `PD-1996` tag or publication record is present.

A second archival candidate is [File:S.A.R. Eugenio di Savoia.png](https://commons.wikimedia.org/wiki/File:S.A.R._Eugenio_di_Savoia.png), 669x916, dated 1935, with the Piemonte cultural archive record [Memora Piemonte item 515241](https://www.memora.piemonte.it/beni/regpie_cabe/515241). Its Commons record is also only `PD-Italy`, with an unknown photographer and no United States publication proof.

The lower-resolution [File:Eugenio di savoia, quinto duca di genova.jpg](https://commons.wikimedia.org/wiki/File:Eugenio_di_savoia,_quinto_duca_di_genova.jpg) is 287x368, dated between 1920 and 1930, by an unknown author, and likewise only `PD-Italy`. It is useful as identity corroboration but is not a rights-cleared runtime source.

The exact blocker is rights, not identity or ownership. A `PD-Italy` label cannot be silently promoted to United States public domain, and no source page found here proves pre-1978 publication, non-registration, or a `PD-1996` condition. Keep the crown role fail-closed until the parent obtains that evidence or an explicitly redistributable source.

If rights are cleared, the 669x916 1935 Memora source is the preferred crop master because it is period-matched and nearly portrait-shaped. Suggested head-and-shoulders crop is `left=0, top=0, right=669, bottom=900` followed by the repository's deterministic 156x210 finish; retain the face, collar, and upper chest and do not synthesize uniform details. This is a plan only and was not executed.

Ownership audit: exact and title variants (`Eugenio di Savoia-Genova`, `Eugenio di Savoia`, `Prince Eugenio`, and `Duke of Genoa`) were scanned in vanilla `common/characters`, country history, and portrait GFX plus the current Chaos Redux equivalents. No character, leader, commander, or portrait owner was found; vanilla hits are unrelated Cuban/Uruguayan names and ship/division names.

## Commander candidate: Vittorio Vernè

Vittorio Vernè (Rome, 8 May 1883 - Godofelassi, 7 January 1937) is a historically attested Italian major-general. The [Generals.dk record](https://generals.dk/general/Vern%C3%A8/Vittorio/Italy.html) records him as deputy general officer commanding the 6th Blackshirt Division “Tevere” in East Africa from 15 March to 30 June 1936, at disposal of the 5th Division from 30 June to 12 August, and general officer commanding the 5th Blackshirt Division “I Febbraio” from 12 August 1936 until his death. The Italian-language biographical record is [Vittorio Vernè](https://it.wikipedia.org/wiki/Vittorio_Vern%C3%A8).

The source binary is [File:Vittorio Vernè.jpg](https://commons.wikimedia.org/wiki/File:Vittorio_Vern%C3%A8.jpg) and the unchanged direct file is [Vittorio_Vernè.jpg](https://upload.wikimedia.org/wikipedia/commons/d/df/Vittorio_Vern%C3%A8.jpg). Commons records 200x250 pixels, an anonymous photograph dated “anni 30”, source credit to Generals.dk, and both `{{PD-Italy}}` and `{{PD-1996}}`. The downloaded binary used for the audit was 31,645 bytes with SHA-256 `DE94DF14318398914A51AA0FB6601F9C31F916CC98D3803B313FE33BE15F1417`.

Vernè is not Sardinian-born, but his documented 1936 career includes the 176th Legion “Cacciatori Guide di Sardegna” and active command in the 1936 East African war. This gives the ARX commander role a concrete Sardinian institutional link without inventing a Sardinian identity. If the parent requires Sardinian birth rather than a Sardinia-linked formation, keep this role blocked and do not substitute a generic Italian general.

Suggested exact source crop for the 200x250 master is `left=7, top=0, right=193, bottom=250` (186x250), then the repository's deterministic 156x210 finish. This retains the complete cap, face, collar, shoulder insignia, and medal area while trimming the gray side border. The image is photographic and low-resolution; it must remain evidence only until the source-locked HOI4-style repaint and independent identity audit are completed by the downstream asset workflow.

Ownership audit: exact and normalized variants (`Vittorio Vernè`, `Vittorio Verne`, `Vittorio Vernè`, and `ITA_vittorio_verne`) were scanned in vanilla `common/characters`, country history, portrait GFX, and the current Chaos Redux equivalents. No owner was found. Do not reuse the existing generated `ARX_gavino_piras` face; the sourced identity would require a new reviewed source package and parent-owned runtime wiring.

## Rejected nearby leads

Giuseppe Tellera and Carlo Favagrossa are active vanilla character owners and cannot be transferred into ARX. Prince Adalberto di Savoia-Genova is also an active vanilla character (`ITA_prince_adalberto`) and is blocked despite earlier ARX notes claiming otherwise. Alberto De Marinis has an official Italian Senate image with a clear CC BY 3.0 IT record, but the available biography documents a 1920 Upper Silesia command and later political service rather than a clear 1936 field-command role; keep him as a research fallback only, not as a roster decision. No generated or name-only substitute is admissible for the crown role.

## Parent handoff

1. Keep the crown route fail-closed until Eugenio's United States publication/registration status is independently documented or an explicitly redistributable period source is found.
2. If a Sardinia-linked but non-Sardinian-born commander is acceptable, route the Vernè source through the grounded portrait pipeline, preserving the source binary and the crop coordinates above and requiring the independent visual audit before any DDS or `.gfx` work.
3. If Sardinian birth is mandatory, reject Vernè and continue source research rather than assigning a generic, generated, vanilla-owned, or copyright-unclear face.
4. This handoff intentionally contains no processed PNG, final DDS, `.gfx` change, gameplay edit, localisation, or generated portrait.
