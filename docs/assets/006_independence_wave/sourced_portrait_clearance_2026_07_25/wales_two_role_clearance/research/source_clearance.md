# Wales alternative portrait source clearance research

## Research decision

The failed David Rhys Grenfell and George Cornwallis-West source photographs were not retried. Lewis Valentine was initially considered for the civic role but was rejected after the ownership scan found an active Kaiserreich WLS identity. Thomas Wynford Rees was considered for the commander role but was rejected because the SE3459 image is a wide scene with a small face and Kaiserreich owns the subject. The selected review pair is J. H. Thomas and Major-General Robert Knox Ross.

## James Henry Thomas (J. H. Thomas) source evidence

- Commons file page: https://commons.wikimedia.org/wiki/File:James_Henry_Thomas_(1874-1949)_portrait.jpg
- Unchanged master URL: https://upload.wikimedia.org/wikipedia/commons/4/42/James_Henry_Thomas_%281874-1949%29_portrait.jpg
- Commons metadata snapshot: `source_page_snapshots/j_h_thomas_commons_file_page.html`.
- Commons identifies the source as the Library of Congress George Grantham Bain Collection digital ID `ggbain.29625`, authored by Bain and dated circa 1920.
- Commons records `PD-Bain` and Library of Congress no-known-copyright-restrictions notices. Preserve the Commons/LOC provenance and do not infer a separate personal photographer or estate clearance.
- The source is `3674x4977` grayscale and shows a single person with clear eyes, ears, brow, nose, moustache, mouth, jaw, bow tie and shoulders. The exact crop `source_crops/j_h_thomas_civic_crop.png` is `(350,200)-(3350,4200)` and is `3000x4000`.
- The crop proof `source_crops/j_h_thomas_civic_crop.json` reports `decoded_pixels_equal: true` with matching RGBA SHA-256 `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`.
- Thomas was Welsh-born in Newport, a trade-union leader and Labour politician, and served as Secretary of State for the Colonies from 1935 to 1936. This gives the existing WLS civic role a direct Welsh institutional and interwar political connection.
- The source is circa 1920 rather than 1936. Any downstream treatment must age the subject without altering the source facial geometry and must not describe the image as a 1936 photograph.

## Robert Ross source evidence

- Commons file page: https://commons.wikimedia.org/wiki/File:Negative_H24742.jpg
- Unchanged master URL: https://upload.wikimedia.org/wikipedia/commons/6/6b/Negative_H24742.jpg
- Commons metadata snapshot: `source_page_snapshots/robert_ross_commons_file_page.html`.
- Commons identifies Imperial War Museums object `205497134`, Negative H24742, from the War Office Second World War Official Collection, dated 20 October 1942.
- Commons marks the IWM/War Office source `PD-UKGov`. The page does not name a separate photographer, so no personal author is inferred.
- The source is `800x582` RGB and shows Ross in period service dress with cap, eyes, ears, nose, jaw, tunic, medal bars and both shoulders. The tightened exact crop `source_crops/robert_ross_commander_crop.png` is `(220,85)-(530,385)` and is `310x300`; it removes the frame, hands and waist.
- The crop proof `source_crops/robert_ross_commander_crop.json` reports `decoded_pixels_equal: true` with matching RGBA SHA-256 `6db001ff152d9bd894b8d6e6d8d83ed0e08b954e0f4dae03f7b66245b69b1a87`.
- Ross commanded the 160th Infantry Brigade and the 53rd (Welsh) Infantry Division during the Second World War. He was not Welsh-born, so the WLS role fit is based on documented Welsh-formation command rather than birthplace.
- The official source is directly within the WWII period. The parent still owns the alternate-history appointment decision and must not present the 1942 image as a 1936 photograph.

## Rejected comparison evidence

- Lewis Valentine source `source_masters/lewis_valentine_yn_ifanc_1920.jpg` is complete and exact-cropped but is `rejected_subject_owned` because Kaiserreich `1521695605` owns `WLS_lewis_valentine`, recruitment, portraits and localisation.
- Thomas Wynford Rees SE3459 ([Commons source page](https://commons.wikimedia.org/wiki/File:Major_General_T_W_Rees,_commanding_19th_Indian_Division,_enters_Fort_Dufferin_in_Mandalay,_Burma,_19_March_1945._SE3459.jpg)) was downloaded for comparison but not admitted to the package as a candidate. The image is an 800x798 wide arrival scene with a small face, and Kaiserreich `1521695605` owns `RAJ_thomas_wynford_rees` and its portrait/localisation consumers.
- W. J. Gruffydd source `source_masters/w_j_gruffydd_original.jpg` is `blocked_postwar_source` because Commons dates it 1946, after the 1936 start date. It remains in the package only as documented blocked evidence.
- Lewis Pugh Evans HU 93411 is `rejected_duplicate_failed_source` because it is the same source already used by the two failed Evans repaint trials in the 2026-07-24 replacement package.
- The January 1924 Underwood & Underwood J. H. Thomas alternative is retained as `source_masters/j_h_thomas_underwood_1924_rejected.jpg` only for comparison. Its circular halftone/newspaper reproduction has softer facial geometry than the selected Bain photograph.

## Processing evidence

The decoded PNG masters are lossless decodes of the downloaded JPEG masters. The four review crops in the package were made exclusively with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py`. The J. H. Thomas and Robert Ross crop JSON files prove exact decoded-pixel equality between each decoded master rectangle and its crop output. The v5 contact sheet compares each selected source master and exact crop for review.

No ImageGen, resizing, enhancement, recolouring, DDS conversion, advisor/dossier processing, or runtime wiring was performed in this package.
