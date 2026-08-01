# IW-058 ASY portrait-source retry v92

Research date: 2026-08-01. This bounded retry sought a period concordat or levies/guardianship identity with a clearer archival publication and public-domain chain than the Haydo and Dolabani leads. It does not overwrite the v91 evidence package and does not edit characters, gameplay, localisation, GFX, DDS files, advisor icons, or central portrait attestation.

## Result

Ignatius Aphrem I Barsoum is the stronger concordat source. This is the same historically grounded church identity already used by the existing IW-058 concordat consumer, but the retry preserves a higher-resolution 1920/1921 archival delegation image whose publication and `PD-1923` status are explicit. It is a source-ready alternate master and exact crop for parent review, not a new runtime admission.

No new collision-free levies identity with an equally clear pre-1936 rights chain was found. Agha Petros remains a direct military fit but is deceased before the 1936 window and Kaiserreich-owned; Malik Ismail II remains date-gated; Haydo remains rights-uncertain. No alternate levies source was copied in this retry.

## Source package

| Consumer | Identity and role/date evidence | Source and rights | Local source and crop | Disposition |
|---|---|---|---|---|
| `ASY_independence_wave_concordat_council` | Ignatius Aphrem I Barsoum (Ayoub Barsoum, 1887–1957) was Archbishop of Syria and Lebanon from 1918 and Patriarch of the Syriac Orthodox Church from 30 January 1933 through 1957. The 1920 image caption identifies “Metran Afrem Barsoom” in the Assyro-Chaldean delegation to the Paris Peace Conference, establishing a role-correct church representative before the 1936 baseline. | [Commons file](https://commons.wikimedia.org/wiki/File:Assyro-Chaldean_delegation_to_the_Paris_Peace_Conference.png) and [original PNG](https://upload.wikimedia.org/wikipedia/commons/4/40/Assyro-Chaldean_delegation_to_the_Paris_Peace_Conference.png). Commons records `Babylon`, vol. 2, no. 14, 3 February 1921 as the source, reprinted in Racho Donef's [Macquarie University paper](https://researchers.mq.edu.au/en/publications/the-assyrian-delegation-at-the-paris-peace-conference), unknown photographer, and `PD-1923`/public-domain status. The publication date and rights tag are materially clearer than the unknown-author source-country assertions attached to Haydo and Dolabani. | Master: `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_masters/ASY_ignatius_afram_barsoum_paris_1921.png` (1728x1314 RGBA, SHA-256 `ED5473DAB88A27D4DD5736AB5B6136A95E1E9FEF1622EFF7005DD0E17ED7D9D9`). Exact crop: `docs/assets/006_independence_wave/asy_portrait_source_retry_v92_2026_08_01/source_crops/ASY_concordat_council_ignatius_afram_barsoum_paris_head_shoulders.png` (crop `650,85,970,470`, 320x385 RGBA, SHA-256 `C91D7E97DC8FA06ED9DC3F7FA70B01B09BE71EF53A60E07C29737728999D1555`). Equality evidence: `crop_metadata/ASY_concordat_council_ignatius_afram_barsoum_paris_crop.json`. | `source_ready_for_parent_review`: identity, role/date, publication, and public-domain chain are strong. The source is a ten-person group, so the parent should retain the caption evidence and run the normal identity-preservation audit before repaint or DDS promotion. |

## Crop notes

The crop contains Barsoum's hat, face, beard, and upper ecclesiastical shoulders without another person's face. A narrow adjacent shoulder edge remains at the far right because the delegation members overlap in the original composition; no pixels were reconstructed or painted out. The crop was produced with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` and reports `status: exact_source_crop_verified` with `decoded_pixels_equal: true`.

## Parent handoff

The stable consumer and sprite remain `ASY_independence_wave_concordat_council` and `GFX_portrait_ASY_independence_wave_concordat_council`; no `.gfx` or gameplay changes are authorized by this handoff. If accepted, pass the exact crop to the source-locked real-person repaint workflow, then run the independent identity/style audit before replacing the existing DDS. Keep the v37 Barsoum source and v91 Haydo/Dolabani evidence unchanged for provenance comparison.
