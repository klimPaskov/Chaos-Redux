# IW-058 ASY roster sourced portrait research handoff

Date: 2026-08-02

Scope: source research for the two unresolved Event 6 ASY roster consumers `ASY_independence_wave_civic_national_assembly` and `ASY_independence_wave_levies_guardianship`.

Outcome: **HOLD / no production promotion**. Two collision-free Levies leads were sourced and cropped: Yacob Khoshaba Aboona has strong 1936 service evidence but an explicit all-rights-reserved gate; Daniel Ismail has a public-domain assertion but unresolved 1936 living/active-role and group-photo identity gates. The strongest Civic lead failed the exact-person ownership gate. No DDS, GFX, character, localisation, gameplay, admission, or attestation files were changed.

## Candidate matrix

### Civic National Assembly

Candidate: Yusuf Salman Yusuf (Comrade Fahd).

- Source: [Commons file page](https://commons.wikimedia.org/wiki/File:Youssif_Salman_Youssif.jpg), original `https://upload.wikimedia.org/wikipedia/commons/f/fb/Youssif_Salman_Youssif.jpg`.
- Source master: `docs/assets/006_independence_wave/iw058_asy_roster_source_research_2026_08_02/lead_fahd_youssif_salman_youssif_source.jpg`, 200x257 grayscale, SHA-256 `90cd4e4fe376d329c989812196dbfd7d92b64af1f4b894f99bc0fbab1a63c4fc`.
- Exact crop: `source_crops/ASY_civic_national_assembly_yusuf_salman_yusuf_head_shoulders.png`, crop `[10,8,190,257]`, SHA-256 `ea654e2b5c55b0826da8f341ff2e9f73800dfae1910099a96208a80f331fe7ce`; `crop_metadata/ASY_civic_national_assembly_yusuf_salman_yusuf_crop.json` records `decoded_pixels_equal: true`.
- Source metadata: `source_metadata/ASY_civic_national_assembly_yusuf_salman_yusuf_source.json`.
- Role/date: public biographies identify him as an Assyrian of Chaldean Catholic background and Iraqi civic/worker organizer; the 1930s photo is broadly era-compatible, but exact 1936 location is not established.
- Rights: Commons asserts PD-Iraq; photographer and original publication are uncredited.
- Ownership gate: **FAIL**. Vanilla defines `IRQ_yusuf_salman_yusuf` in `common/characters/IRQ.txt`; Kaiserreich 1521695605 defines the same exact person in `common/characters/IRQ characters.txt`.
- Disposition: **REJECTED SUBJECT COLLISION**. Do not silently reuse or transfer this identity to ASY.

### Levies Guardianship: Yacob Khoshaba Aboona

Candidate: Yacob Khoshaba Aboona (Rab Tremma Yacob Khoshaba Aboona).

- Source and role biography: [Assyrian RAF Levies page](https://assyrianlevies.info/rab-tremma-y-k-aboona.html), lead image `1974504_orig.jpg` at `https://assyrianlevies.info/uploads/3/4/5/4/34547999/1974504_orig.jpg`.
- Source master: `yacob_khoshaba_aboona_source/yacob_aboona_image_1.jpg`, 226x289 RGB, SHA-256 `d8ca68bc0864692696aaf1c8d12e4a6eb6b77994d2c8ef87dd432cb0a75bdd5d`.
- Exact crop: `source_crops/ASY_levies_guardianship_yacob_khoshaba_aboona_head_shoulders.png`, crop `[20,10,210,250]`, SHA-256 `d19d479eecfa0baa4a71b3490cc02a431ab4ac842a0de416007cec121dc6acc4`; `crop_metadata/ASY_levies_guardianship_yacob_khoshaba_aboona_crop.json` records `decoded_pixels_equal: true`.
- Role/date: the named biography gives birth 4 February 1900, enlistment in the Iraq Levies on 16 February 1922, and service until 2 May 1955. This is strong evidence for a living/active Levies role in 1936; the portrait capture date is not stated.
- Ownership gate: targeted no-match scan in Chaos Redux, vanilla HOI4, and approved Kaiserreich common paths for Yacob/Jacob Khoshaba Aboona variants. This is evidence of no collision found, not a global attestation.
- Rights gate: **FAIL/PENDING RIGHTS**. The source page explicitly says "All rights reserved" and offers the photographs on request at `gabykiwarkis@gmail.com`. No public license or transfer grant is published.
- Source metadata and rights evidence: `source_metadata/ASY_levies_guardianship_yacob_khoshaba_aboona_source.json` and `role_evidence/ASY_levies_guardianship_yacob_khoshaba_aboona_evidence.md`.
- Disposition: **NEEDS_USER_REVIEW / RIGHTS HOLD**. Written permission must cover derivative portrait repaint and mod distribution before any source-locked repaint or runtime work.

### Levies Guardianship: Daniel Ismail

Candidate: Daniel Ismail, son of Malik Ismail of Upper Tyari.

- Source: [Commons file page](https://commons.wikimedia.org/wiki/File:Malik_Ismail_II_of_Upper_Tyari,_surrounded_by_his_children_and_grandchildren._Standing_(left_to_right)_are_his_sons_Daniel,_Shlimon,_Yaqou_(later_Malik_Yaqou)_and_Dinkha.png), original URL is recorded in the source metadata. The 1912 caption orders the four standing sons left-to-right as Daniel, Shlimon, Yaqou (later Malik Yaqou), and Dinkha.
- Source master: `docs/assets/006_independence_wave/iw058_asy_roster_source_research_2026_08_02/lead_daniel_ismail_family_1912.png`, 2048x1343 palette PNG, SHA-256 `13b3cf9aa9972a35290e86f3484e872200b0804dcc16f9b31c2d4f7d5bf23235`.
- Exact tight crop: `source_crops/ASY_levies_guardianship_daniel_ismail_head_shoulders_tight.png`, crop `[90,140,445,600]`, SHA-256 `eecd7cc10ce1d56cf37e99a01c347cfb1fa592a5afeaa247d9797dce1acb7354`; `crop_metadata/ASY_levies_guardianship_daniel_ismail_tight_crop.json` records `decoded_pixels_equal: true`.
- Source metadata: `source_metadata/ASY_levies_guardianship_daniel_ismail_source.json`.
- Role evidence: Brigadier J. Gilbert Browne, *Iraq Levies 1915-1932* (1932), [Internet Archive item](https://archive.org/details/file1-iraqlevies), [OCR](https://archive.org/download/file1-iraqlevies/File2IraqLevies_djvu.txt). The local copy is `iraq_levies_1932_ocr.txt` (SHA-256 `cc70a18435bcfd541f377942be4010375294ce6b59536f668bf25758fb22edbe`). The OCR names Daniel as an Assyrian native officer/Rab-Tremma of the 2nd Assyrian Battalion, later "senior Assyrian Officer of the Levies," and still retained in the 1928 chapter.
- Ownership gate: targeted no-match scan in Chaos Redux, vanilla HOI4, and approved Kaiserreich common paths for `Daniel Ismail`, `Daniel Malik Ismail`, and `Malik Ismail`. This is evidence of no collision found, not a global attestation.
- Rights: Commons asserts public domain under PD-Iraq and PD-US-expired with an unknown photographer; the page credits the Tyareh gallery. The author and source chain are unresolved.
- Date gate: **OPEN**. The 1932 publication and 1928 chapter establish historical service but no post-1932 living, retirement, or 1936 active-role record was located.
- Identity gate: **OPEN**. The source caption identifies the leftmost standing son, but this is a group photograph and requires independent audit before repaint.
- Disposition: **NEEDS_USER_REVIEW / HOLD**. Do not promote to DDS or runtime until date proof, group-photo identity audit, source-locked repaint, and independent repaint audit are complete.

## Additional civic leads that did not clear source gate

Farid Nuzha (1894-1970) is a plausible living Assyrian journalist/activist and newspaper editor, but Commons search produced only 1939 newspaper-front-page scans, not an attributable portrait. Ishak Armale (1879-1954) is a plausible Assyrian historian/philologist, but no attributable archival portrait was located. Neither is production-ready without a named portrait source.

Existing package leads were not reused: Gallo Shabo is project-owned, Barsoum is reserved/promoted for Concordat, Werda/Warda remains low-resolution with unresolved 1936 status, Haydo has unresolved rights, Agha Petros is dead in 1932 and Kaiserreich-owned, Malik Khoshaba/Malik Yaqo/Yusuf Malek/Dawid Mar Shimun/Yosip Khoshaba/Malik Qambar Warda are Kaiserreich-owned, Naum Faiq and Freydun Atoraya fail the 1936 death gate, and unnamed recruits/Cecil Beaton/Toma Tomas fail exact-person or era gates.

## Handoff files

- Full evidence manifest: `docs/assets/006_independence_wave/iw058_asy_roster_source_research_2026_08_02/manifest.md`.
- Source metadata JSON: `source_metadata/ASY_levies_guardianship_daniel_ismail_source.json` and `source_metadata/ASY_civic_national_assembly_yusuf_salman_yusuf_source.json`.
- Daniel role evidence: `role_evidence/ASY_levies_guardianship_daniel_ismail_levies_evidence.md`.
- Review contact sheet: `review/asy_roster_contact_sheet_v02.png` (SHA-256 `9cd64dbd85c171ef2c95a87f7f1ed2b36e921a307dfb3bdbbdc477173698c865`).
- GFX handoff: `gfx_handoff.md` (blocked; no final DDS paths).

## Parent action required

Treat this as a precise HOLD. If Daniel Ismail is retained, commission a source-locked repaint only after confirming 1936 living/active status and assign an independent identity/rights audit. If those gates cannot be closed, keep the Levies consumer blocked. Find a different non-owned named Civic portrait; Yusuf Salman Yusuf must remain rejected despite its otherwise strong role/date fit.
