# Wales alternative portrait source clearance research

## Research decision

The failed David Rhys Grenfell and George Cornwallis-West source photographs were not retried. Lewis Valentine was initially considered for the civic role but was rejected after the ownership scan found an active Kaiserreich WLS identity. Thomas Wynford Rees was considered for the commander role but was rejected because the SE3459 image is a wide scene with a small face and Kaiserreich owns the subject. J. H. Thomas remains source-ready for the civic role. The IWM HU 126780 image is retained only as blocked namesake evidence: it depicts Second Lieutenant Gervase Thorpe Spendlove, who died in 1914, not the requested Major-General Gervase Thorpe who was alive in 1936. Robert Ross remains blocked research evidence because his exact crop is too small for reliable facial geometry.

## James Henry Thomas (J. H. Thomas) source evidence

- Commons file page: https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg
- Unchanged master URL: https://upload.wikimedia.org/wikipedia/commons/4/42/James_Henry_Thomas_%281874-1949%29_portrait.jpg
- Commons metadata snapshot: `source_page_snapshots/j_h_thomas_commons_file_page.html`.
- Commons identifies the source as the Library of Congress George Grantham Bain Collection digital ID `ggbain.29625`, authored by Bain and dated circa 1920.
- Commons records `PD-Bain` and Library of Congress no-known-copyright-restrictions notices. Preserve the Commons/LOC provenance and do not infer a separate personal photographer or estate clearance.
- The source is `3674x4977` grayscale and shows a single person with clear eyes, ears, brow, nose, moustache, mouth, jaw, bow tie and shoulders. The exact crop `source_crops/j_h_thomas_civic_crop.png` is `(350,200)-(3350,4200)` and is `3000x4000`.
- The crop proof `source_crops/j_h_thomas_civic_crop.json` reports `decoded_pixels_equal: true` with matching RGBA SHA-256 `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`.
- Thomas was Welsh-born in Newport, a trade-union leader and Labour politician, and served as Secretary of State for the Colonies from 1935 to 1936. This gives the existing WLS civic role a direct Welsh institutional and interwar political connection.
- The source is circa 1920 rather than 1936. Preserve the source-visible age and identity exactly; downstream treatment must not invent age progression or describe the image as a 1936 photograph.

## IWM HU 126780 namesake source evidence (blocked for requested commander)

- IWM object page: https://www.iwm.org.uk/collections/item/object/205388980
- Unchanged master URL: https://media.iwm.org.uk/ciim5/439/54/large_000000.jpg
- IWM metadata snapshot: `source_page_snapshots/gervase_thorpe_iwm_hu126780_page.md`.
- The source is IWM Bond of Sacrifice - First World War Portraits Collection object `205388980`, collection number `HU 126780`. The page title is **Second Lieutenant Gervase Thorpe Spendlove**; the object description names his unit as the 2nd Battalion, The Prince of Wales' Volunteers (South Lancashire Regiment) and records death on 17 November 1914. The exact photographer and photograph date are not stated; IWM classifies the record as First World War production/content.
- IWM permits low-resolution downloads and embeds for accepted non-commercial uses under https://www.iwm.org.uk/corporate/policies/non-commercial-licence and requires the attribution `Image: IWM (HU 126780)`. The listed uses include private research/study, information-led non-paywalled websites, personal non-commercial social media, non-commercial education, offline viewing/listening and free exhibitions. Commercial use, high-resolution copies or other uses require an IWM licence. Do not infer a public-domain status.
- The unchanged master is `612x800` RGB. It is a single-person archival portrait with clear eyes, ears, brow, nose, mouth, jaw, hairline, cap, collar and both shoulder tops. The exact crop `source_crops/gervase_thorpe_commander_crop.png` is `(10,80)-(602,720)` and is `592x640`.
- The crop proof `source_crops/gervase_thorpe_commander_crop.json` reports `decoded_pixels_equal: true` with matching RGBA SHA-256 `3f4666b6918993d3d2b2634cd24c9f6a3cad575f5f18301c7ec1134c45370fbf`.
- The requested subject is Major-General Gervase Thorpe (1877-1962), GOC of the 53rd (Welsh) Infantry Division from 1935 to 1939 and alive in 1936. The IWM subject is a different namesake who died in 1914; there is no evidence in the IWM record linking the two identities. The apparent Welsh-formation role fit was a conflation and is rejected.
- The crop is visually usable as an adult male head-and-shoulders source only in the generic sense: clear eyes, ears, brow, nose, mouth, jaw, hairline, cap, collar and both shoulder tops. It is not usable as the requested 1936 WLS mountain-commandant identity master. Preserve the source-visible age and identity exactly and do not pass it to ImageGen, processing or runtime wiring. The halftone pattern is inherent source detail and should be disclosed.

## Robert Ross blocked research evidence

- Commons file page: https://commons.wikimedia.org/wiki/File:Negative_H24742.jpg
- Unchanged master URL: https://upload.wikimedia.org/wikipedia/commons/6/6b/Negative_H24742.jpg
- Commons metadata snapshot: `source_page_snapshots/robert_ross_commons_file_page.html`.
- Commons identifies Imperial War Museums object `205497134`, Negative H24742, from the War Office Second World War Official Collection, dated 20 October 1942.
- Commons marks the IWM/War Office source `PD-UKGov`. The page does not name a separate photographer, so no personal author is inferred.
- The source is `800x582` RGB and shows Ross in period service dress with cap, eyes, ears, nose, jaw, tunic, medal bars and both shoulders. The tightened exact crop `source_crops/robert_ross_commander_crop.png` is `(220,85)-(530,385)` and is `310x300`; it removes the frame, hands and waist.
- The crop proof `source_crops/robert_ross_commander_crop.json` reports `decoded_pixels_equal: true` with matching RGBA SHA-256 `6db001ff152d9bd894b8d6e6d8d83ed0e08b954e0f4dae03f7b66245b69b1a87`.
- Ross commanded the 160th Infantry Brigade and the 53rd (Welsh) Infantry Division during the Second World War. He was not Welsh-born, so the WLS role fit is based on documented Welsh-formation command rather than birthplace.
- Ross is blocked because this exact crop leaves only roughly 60-80 px of usable facial geometry. Retain the master, crop and equality proof for provenance evidence only; do not send it to the downstream identity-preserving pipeline.
- The official source is directly within the WWII period. The parent still owns the alternate-history appointment decision and must not present the 1942 image as a 1936 photograph.

## Rejected comparison evidence

- Lewis Valentine source `source_masters/lewis_valentine_yn_ifanc_1920.jpg` is complete and exact-cropped but is `rejected_subject_owned` because Kaiserreich `1521695605` owns `WLS_lewis_valentine`, recruitment, portraits and localisation.
- Thomas Wynford Rees SE3459 ([Commons source page](https://commons.wikimedia.org/wiki/File:Major_General_T_W_Rees,_commanding_19th_Indian_Division,_enters_Fort_Dufferin_in_Mandalay,_Burma,_19_March_1945._SE3459.jpg)) was downloaded for comparison but not admitted to the package as a candidate. The image is an 800x798 wide arrival scene with a small face, and Kaiserreich `1521695605` owns `RAJ_thomas_wynford_rees` and its portrait/localisation consumers.
- W. J. Gruffydd source `source_masters/w_j_gruffydd_original.jpg` is `blocked_postwar_source` because Commons dates it 1946, after the 1936 start date. It remains in the package only as documented blocked evidence.
- Lewis Pugh Evans HU 93411 is `rejected_duplicate_failed_source` because it is the same source already used by the two failed Evans repaint trials in the 2026-07-24 replacement package.
- The January 1924 Underwood & Underwood J. H. Thomas alternative is retained as `source_masters/j_h_thomas_underwood_1924_rejected.jpg` only for comparison. Its circular halftone/newspaper reproduction has softer facial geometry than the selected Bain photograph.
- Field Marshal Sir Archibald Montgomery-Massingberd was not admitted despite a clear 14 December 1927 Bassano/National Portrait Gallery portrait and a documented 53rd (Welsh) Division command connection. The Commons page combines a public-domain tag with an NPG copyright claim and unauthorised-reproduction notice, so the source is rights-uncertain rather than source-ready.

## Processing evidence

The decoded PNG masters are lossless decodes of the downloaded JPEG masters. The source crops in the package were made exclusively with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`. The J. H. Thomas and IWM HU 126780 namesake crop JSON files prove exact decoded-pixel equality between each decoded master rectangle and its crop output. The v7 contact sheet compares the source-ready Thomas master and the blocked HU 126780 namesake master/crop; Ross remains listed only as blocked evidence in the manifest.

No ImageGen, resizing, enhancement, recolouring, DDS conversion, advisor/dossier processing, or runtime wiring was performed in this package.
