# IW-009 Bavaria — Otto von Lossow sourced portrait retry

Date: 2026-07-24.

Scope: archival male source preservation, explicit identity crop, provenance and rights recording, ownership collision scan, historical role-fit assessment, and downstream processing handoff only.

No gameplay, character, history, GFX, interface, localisation, workbook, processed portrait, ImageGen output, or DDS file was created or edited.

## Candidate verdict

Otto Hermann von Lossow (15 January 1868 – 25 November 1938) is a grounded historical Bavarian/German general and a source-ready replacement candidate for the safety-blocked Friedrich Dollmann input in the Bavaria IW-009 package.

Status: `blocked_imagegen_safety_no_runtime_asset`.

Source mode: `grounded_source_only` / `sourced_real_person`.

The candidate remains suitable archival identity evidence, but the required ImageGen repaint is blocked by the safety system.

No generated image was returned, and no processed PNG, DDS, or runtime wiring may be created from this source package.

## Immutable archival source

Exact Commons title: `General Otto von Lossow 01.jpg`.

Wikimedia Commons file page: <https://commons.wikimedia.org/wiki/File:General_Otto_von_Lossow_01.jpg>.

Direct original file URL: <https://upload.wikimedia.org/wikipedia/commons/b/b6/General_Otto_von_Lossow_01.jpg>.

The immutable local master is [OTTO_von_lossow_bain_1923_original.jpg](source_masters/OTTO_von_lossow_bain_1923_original.jpg).

Commons records the source as `Bain News Service, 255 Canal St., New York, N. Y.`, the date as `1923`, and the author as `Unknown author`.

Original dimensions are `8980x13470` pixels, JPEG/RGB, `14,442,869` bytes.

Local master SHA-1 is `37230181C476AEB90217CF30701FE601E6C3E303`, matching the Commons API image hash.

Local master SHA-256 is `AD5B0F11C107EB58FBA5BD00975E7A64B046234CC16D61299D8EA6F49D28192F`.

The download was made unchanged from the direct original URL with a `?download=1` query only to request attachment delivery; the query does not identify a different image.

## Rights and provenance

Commons applies `{{PD-US}}` and describes the file as public domain in the United States because the work was published before 1 January 1931 or otherwise falls under the US public-domain rule. Commons metadata reports `Public domain`, no attribution required, and `Copyrighted=False`.

The rights basis is therefore defensible for US use, but Commons explicitly warns that the file may not be public domain outside the United States. Record this as `public_domain_US_needs_jurisdiction_review` rather than inventing a worldwide clearance.

The 1923 Commons description names Bain News Service as the source agency but does not provide a Library of Congress catalog number, LCCN, digital ID, or persistent LOC image URL. The local package must not claim that this exact scan is the separately cataloged LOC record `Gen. Lossow` (LCCN 2014716720), which is dated 1900. The institutional provenance for the 1923 scan is therefore `Bain News Service / Wikimedia Commons upload; archive institution not identified on the source page`, with an explicit LOC-link uncertainty.

Commons API metadata snapshot used for verification: <https://commons.wikimedia.org/w/api.php?action=query&titles=File%3AGeneral_Otto_von_Lossow_01.jpg&prop=imageinfo&iiprop=url%7Csize%7Cextmetadata%7Csha1&format=json>.

Library of Congress Bain collection background and rights page: <https://www.loc.gov/pictures/collection/ggbain/> and <https://www.loc.gov/rr/print/res/274_bain.html>. These establish the Bain collection context only; they do not establish an LOC accession for this exact 1923 scan.

## Rejected first identity crop

The unchanged source was cropped directly in source pixels with Pillow and no resampling, retouching, recolouring, denoising, or identity alteration.

Crop rectangle uses half-open `(left, top, right, bottom)` coordinates in the `8980x13470` master: `(2000, 400, 8000, 7000)`.

The resulting crop is [OTTO_von_lossow_bain_1923_head_shoulders_2000_400_8000_7000.png](source_crops/OTTO_von_lossow_bain_1923_head_shoulders_2000_400_8000_7000.png), `6000x6600` pixels, RGB PNG, `24,686,930` bytes.

Crop SHA-1 is `DF8F6D459F3C70B85D51FBD2307D99874C1ECA24`.

Crop SHA-256 is `A47246879AA1B7E51444C95B3E29F3A128203334F0CABF8966B01076CEF691EE`.

The crop keeps the full bald head, both eyes behind the source glasses, nose, moustache, jaw, and neck, but independent parent inspection rejected it because it does not show both shoulders.

It is retained as rejected evidence only and is not an authorized ImageGen or runtime input.

## Corrected explicit head-and-shoulders crop

The corrected source-pixel crop is [OTTO_von_lossow_bain_1923_head_shoulders_1300_0_7763_8700.png](source_crops/OTTO_von_lossow_bain_1923_head_shoulders_1300_0_7763_8700.png).

Its half-open rectangle is `(left=1300, top=0, right=7763, bottom=8700)` in the unchanged `8980x13470` master.

The corrected crop is `6463x8700` RGB PNG, `56,686,053` bytes.

Its SHA-1 is `A6FE96C9D0945D23692394D69A50AA555EF62DA7`.

Its SHA-256 is `0083F0F78CD1606A1FD87A2D42614F68A163C7D7DBFB544543DE1202A6A1D22A`.

It visibly retains the full head, face, neck, and both shoulders at the source aspect needed for a leader portrait.

It also necessarily retains parts of the source military collar and shoulder decoration.

The source has archival dust, scratches, sepia/grayscale toning, and uneven exposure; these are source artifacts, not a reason to alter the immutable master or crop.

## ImageGen safety disposition

The corrected head-and-shoulders crop was submitted as the sole identity source, with canonical male HOI4 commander portraits supplied as style-only references.

The prompt explicitly required preservation of Lossow's bald head, glasses, moustache, age, ears, facial asymmetry, three-quarter pose, and expression while replacing the visible uniform with a plain field-gray tunic without medals, badges, collar patches, epaulettes, political symbols, flags, text, or readable insignia.

ImageGen rejected the request through the safety system and returned no generated output.

The block is treated as final for this archival photograph.

The raw photograph will not be resized, filtered, directly converted, manually composited, or promoted as a runtime substitute.

## Historical fit for the Bavaria role

Lossow is a strong territorial-command fit, not a literal historical holder of a fictional `emergency passes-and-depots commandant` office.

Authoritative Bavarian and German biographical records identify him as Generalleutnant, commander of the 7th Division, Befehlshaber in Wehrkreis VII, and Bavarian Landeskommandant during the 1923 crisis. The sources differ on the formal start date of the appointment (`28 September 1921` in Deutsche Biographie versus `1 January 1923` in the Bavarian administrative biography), but agree that he exercised the relevant Bavaria-wide military authority in 1923.

His documented service supports a territorial logistics and emergency-command abstraction: Wehrkreis VII covered Bavaria, the 7th Division headquarters was in Munich, and the Landeskommandant role involved military assistance to the Bavarian government during public emergencies. The fictional passes-and-depots remit should therefore be written as an alternate assignment derived from his Bavaria-wide command scope, not as a claim that historical Lossow specifically administered mountain passes, depot networks, or a named wartime logistics office.

His 1923 record also includes refusing the Reich order to suppress the `Völkischer Beobachter`, the resulting dismissal dispute, participation in the Kahr–Lossow–Seißer triumvirate, and the suppression of the Beer Hall Putsch. Those are historical context, not evidence that he held the proposed 1936 office. He retired from the army in February 1924, so an active 1936 command is necessarily an alternate-history reuse of a living historical figure (age 68 in 1936), not a literal continuation of his documented career.

Sources for role fit:

- [Bavarikon administrative biography](https://verwaltungshandbuch.bavarikon.de/VWH/Lossow%2C_Otto_v.) — 1 January 1923 appointment as 7th Division commander, Wehrkreis VII commander, and Bavarian Landeskommandant; dismissal/reappointment note.
- [Deutsche Biographie / Neue Deutsche Biographie entry](https://www.deutsche-biographie.de/sfz54372.html) — 1921 Bavaria command, Wehrkreis VII and 7th Division scope, 1923 crisis chronology, and February 1924 retirement.
- [DHM LeMO 1923 chronology](https://www.dhm.de/lemo/jahreschronik/1923) — October 1923 refusal of the newspaper-ban order and description as commander of the 7th Bavarian Reichswehr Division.
- [7. Division der Reichswehr reference](https://www.lexikon-der-wehrmacht.de/Gliederungen/DivisionenRW/DivisionRW7-R.htm) — division headquarters in Munich and commander/Wehrkreis dual role (secondary reference).

## Ownership gate result

Search terms included exact and variant identity forms: `Otto von Lossow`, `Otto Hermann von Lossow`, `Otto Stephan Hermann von Lossow`, `General Lossow`, `von Lossow`, `Lossow Otto`, `Lossow, Otto`, `Otto_von_Lossow`, `Otto-Hermann-von-Lossow`, `otto_von_lossow`, `Lossov`, `Лоссов`, `洛索`, and `Loßow`.

Current Chaos Redux roots checked: `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`, plus event/decision/focus roots for named consumers. No exact or variant Lossow character, recruitment, leader/commander/operative, portrait, `.gfx`/interface owner, or localisation identity was found. No Lossow-named file exists outside this source package.

Installed vanilla roots checked: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`. No exact or variant owner or Lossow-named portrait file was found. Incidental `Otto Hermann` hits in generic German name lists are not character ownership.

Approved reference roots checked: Kaiserreich `1521695605`, `2265420196`, and `1458561226`, using the same character, history, leader, interface, localisation, and named-file checks. No exact or variant Lossow owner or portrait file was found. Unrelated false positives were `Дарьзавын Лосол` in a Mongolian localisation file, generic German `Otto Hermann` name-pool entries, and Polish `Jerzy Klossowski`; none resolves to Otto von Lossow.

Disposition: ownership gate passes with no origin character and no transfer guard required. No reference-mod source or art was copied.

Full search notes are in [ownership_scan.md](ownership_scan.md).

## Proposed consumer boundary

This blocked candidate was proposed as a replacement source for the existing Bavaria IW-009 commander token `BAY_independence_wave_mountain_commandant`, with sprite `GFX_portrait_BAY_independence_wave_mountain_commandant` and reserved runtime texture `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

The role is male and commander-family, but the source is not authorized for runtime use after the safety block.

No advisor/dossier, `_small`, operative, female, alternate-country, or fallback derivative is authorized by this package.

## Blockers and simplifications

No substitute, generated portrait, processed portrait, DDS, or gameplay fallback was used.

The runtime blocker is the ImageGen safety rejection.

The provenance caveat also remains: the exact 1923 image has a clear Commons `PD-US` record and high resolution, but no LOC catalog/LCCN is exposed on its source page and worldwide public-domain status is not established.
