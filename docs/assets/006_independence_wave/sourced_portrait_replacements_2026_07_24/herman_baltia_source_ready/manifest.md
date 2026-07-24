# IW-006 AFX Wallonia commander source package: Herman Baltia

Status: `source_ready_needs_role_review`.

This is a grounded-source package for the Event 006 AFX Wallonia reserve/industrial commander surface. It contains one unchanged archival master and one direct pixel crop only. No ImageGen output, processed portrait, DDS, GFX edit, gameplay edit, or localisation edit was made.

## Candidate and role fit

The candidate is Baron Herman Baltia, born 1 September 1863 at Saint-Josse-ten-Noode, Belgium, and deceased 16 September 1938 at Saint-Gilles. He was alive in 1936 and held the Belgian rank of lieutenant-general.

Baltia commanded the Belgian 10th Line Regiment from 14 April 1916. That regiment was traditionally based at Arlon and was transformed into the 1st Regiment of Chasseurs Ardennais on 10 March 1933, making his command record directly Walloon-linked through the Arlon/Luxembourg province formation lineage. He later served as High Commissioner and Governor of Eupen-Malmedy from 1920 to 1925.

The candidate is a credible senior military analogue for an alternate-history Walloon reserve or industrial-security command surface, but he was a retired seventy-two-year-old general by the 1936 start rather than an active field commander. The AFX title is therefore a territorial alternate-history abstraction and must not be presented as a claim that Baltia commanded an independent Walloon state in 1936.

## Source master

| Field | Value |
|---|---|
| File | `herman_baltia_1909_master.jpg` |
| Dimensions | 389 x 473 pixels |
| Format / mode | JPEG / RGB |
| Byte count | 72,828 |
| SHA-256 | `73597E416240754B2F5A9C78AAC4798287B58642F1ABD93C920F3020D95A1B66` |
| Local path | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/herman_baltia_source_ready/herman_baltia_1909_master.jpg` |
| Source page | [Wikimedia Commons: File:General Baltia Herman.jpg](https://commons.wikimedia.org/wiki/File:General_Baltia_Herman.jpg) |
| Direct upload | [Original upload](https://upload.wikimedia.org/wikipedia/commons/e/eb/General_Baltia_Herman.jpg) |
| Depicted date | 1909, as stated in the Commons caption (`Major Baltia 1909`) |
| Author / source | Not identified on the Commons file record |
| Rights | Commons records the work as public domain / Public Domain Mark 1.0 and free of known restrictions under copyright law; the file is also tagged `PD-old` |
| Attribution note | Retain the Commons source page, the `Major Baltia 1909` caption, and the public-domain designation with any later derivative |

The master is the direct original upload, not a thumbnail, screenshot, proxy, or re-encoded derivative. It is a clear grayscale military portrait with face, shoulders, and upper torso visible.

## Head-and-shoulders crop

| Field | Value |
|---|---|
| File | `herman_baltia_1909_head_shoulders_crop.png` |
| Dimensions | 353 x 461 pixels |
| Crop rectangle | `left=20, top=12, right=373, bottom=473` in the 389 x 473 master |
| SHA-256 | `442658EC257566827290B77D7D3B8E7AF208CF9A999FFC1086DD61BC059BCB59` |
| Byte count | 191,109 |
| Local path | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/herman_baltia_source_ready/herman_baltia_1909_head_shoulders_crop.png` |
| Method | Direct source-pixel crop with Pillow; no resampling, retouching, repainting, face synthesis, or colourisation |

The crop isolates Baltia from the top of his head through the upper torso and preserves a face-visible, neutral expression. The portrait contains only Belgian military dress and medals; no Nazi or collaborationist symbol is visible.

The source is from 1909 and shows a pre-World War I uniform. It is identity evidence for a person alive in 1936, not a claim that this exact uniform should be used unchanged as a 1936 portrait.

## Historical references

- [Royal Museum of the Armed Forces and Military History, Baltia personalia inventory](https://museedelarmee.be/sites/default/files/2024-03/inv-15-personalia_0.pdf) records Baltia's Belgian military career, including command of the 10th Line on 14 April 1916.
- [Zentrum für Ostbelgische Geschichte, Herman Baltia](https://www.geschichte.be/herman-baltia/) records his 1863-1938 dates, lieutenant-general career, and 1920-1925 Eupen-Malmedy governorship.
- [Belgium WWII / CegeSoma, Chasseurs Ardennais](https://www.belgiumwwii.be/belgique-en-guerre/articles/chasseurs-ardennais.html) records that the Arlon-based 10th Line Regiment became the 1st Regiment of Chasseurs Ardennais on 10 March 1933 and identifies the province of Luxembourg defensive role.
- [Belgian State Archives, Eupen-Malmedy and Governor Baltia](https://www.arch.be/index.php?a=2015-12-19-eupen-malmedy-en-gouverneur-baltia-inventaris-van-het-archief-van-de-regering-van-eupen-malmedy-1873-1925&l=nl&m=nieuws&r=alle-nieuwsberichten) confirms Baltia's High Commissioner and Governor function after the Versailles transfer.

## Ownership gate

The exact and variant searches were `Herman Baltia`, `Baltia Herman`, `Herman_Baltia`, `BEL_herman_baltia`, `General Baltia`, and `general_baltia`.

Current Chaos Redux has no exact or variant Herman Baltia character, portrait, history, interface/GFX, or English-localisation owner. Event 006's current stable AFX consumer remains `AFX_walloon_reserve_commander` with sprite `GFX_portrait_AFX_walloon_reserve_commander` and runtime texture path `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`; this package does not alter that path.

The installed vanilla game has no exact or variant Herman Baltia owner in the searched `common`, `history`, `interface`, `gfx`, or `localisation` roots. Approved reference Kaiserreich `1521695605` has no exact or variant owner in its corresponding roots. Approved references `2265420196` and `1458561226` likewise have no exact or variant owner in their corresponding roots.

No source bytes were copied from vanilla or any reference mod, and no guarded transfer is required for this candidate. The remaining review question is role/timing fit: the source is a 1909 portrait and Baltia was retired by the 1936 start.

## Parent handoff

If the parent accepts the senior-retired-general interpretation, the source and crop may enter the normal identity-preserving portrait pipeline under the existing AFX sprite name. Preserve the source attribution, crop rectangle, hashes, and 1909/pre-World War I uniform caveat through the independent visual audit.

Do not create or wire a DDS from this package until the parent accepts that historical timing and role abstraction. If the parent declines it, retain this source package as a documented candidate and continue the search rather than substituting a generic or invented identity.

No fallback or invented likeness was used. The only review gate is the candidate's retired status and the age of the available portrait, not source rights or identity ownership.
