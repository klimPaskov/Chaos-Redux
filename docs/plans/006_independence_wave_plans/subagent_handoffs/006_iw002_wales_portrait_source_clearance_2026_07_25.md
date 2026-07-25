# IW-002 Wales alternative portrait source-clearance handoff - 2026-07-25

## Result

Source-clearance is complete for two materially different, historically defensible male candidates with crop-grade face geometry. The civic candidate is James Henry Thomas (J. H. Thomas) from a Library of Congress Bain photograph circa 1920. The commander candidate is Major-General Robert Knox Ross from an Imperial War Museums War Office photograph dated 20 October 1942.

| Role | Candidate | Source disposition | Why it is useful |
| --- | --- | --- | --- |
| Civic or national council | James Henry Thomas (J. H. Thomas) (1874-1949) | `needs_user_review` | Welsh-born Newport trade-union leader and Labour politician with a high-resolution Bain portrait showing clear eyes, ears, brow, nose, moustache, jaw, bow tie and shoulders. |
| Mountain or territorial commandant | Major-General Robert Knox Ross CB DSO MC (1893-1951) | `needs_user_review` | Directly documented commander of the 160th Infantry Brigade and 53rd (Welsh) Infantry Division with a period 1942 uniform portrait and a tight head-and-shoulders crop. |

Both selected candidates passed the subject-ownership scan with no meaningful owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605` or approved mods `2265420196` and `1458561226`. No transfer guard was found for either candidate. The parent must still make the identity and role decision before downstream treatment.

## Files and evidence

- Asset package: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/`.
- J. H. Thomas unchanged master: `source_masters/j_h_thomas_bain_ggbain_29625_circa_1920.jpg`, `3674x4977`, SHA-256 `4f70ef8f6f2f970f5cd9216e15f65348dd92330be390389f2e2e717d0cec8cf5`.
- J. H. Thomas decoded master: `source_master_png/j_h_thomas_civic_master.png`, `3674x4977`, SHA-256 `14e085120d40257ce06f8f0abe4c8c9bbf4f20d0a1092636e3d9958d5e5581bc`.
- J. H. Thomas exact crop: `source_crops/j_h_thomas_civic_crop.png`, rectangle `(350,200)-(3350,4200)`, `3000x4000`, SHA-256 `0b0b8e8ca7807939391a29c64a04f241c56e47e84ba649060f418fe71ef087be`.
- J. H. Thomas equality proof: `source_crops/j_h_thomas_civic_crop.json` reports `decoded_pixels_equal: true` with RGBA SHA-256 `58acbfea5a056c43490682a10cca063828dfa0268a092092a346c307c67368f6`.
- Robert Ross unchanged master: `source_masters/robert_ross_iwm_negative_h24742_1942.jpg`, `800x582`, SHA-256 `1d05da1867e3b31e431f9a3d7e512d44eab1d5ea14d6c10c3ea00de109161621`.
- Robert Ross decoded master: `source_master_png/robert_ross_commander_master.png`, `800x582`, SHA-256 `941efc477dfe904ee93bd1f2950a1aa1757536b10ad717edd6108b84e78b4ae2`.
- Robert Ross exact crop: `source_crops/robert_ross_commander_crop.png`, rectangle `(220,85)-(530,385)`, `310x300`, SHA-256 `de218e083de97c54fa0b250a22d2c62fe8810fab000c5b7dfca602bf5d10273e`.
- Robert Ross equality proof: `source_crops/robert_ross_commander_crop.json` reports `decoded_pixels_equal: true` with RGBA SHA-256 `6db001ff152d9bd894b8d6e6d8d83ed0e08b954e0f4dae03f7b66245b69b1a87`.
- Source-page snapshots: `source_page_snapshots/j_h_thomas_commons_file_page.html` and `source_page_snapshots/robert_ross_commons_file_page.html`.
- Comparison sheet: `contact_sheets/wales_two_role_clearance_contact_sheet_v5.png`, SHA-256 `d25308ecd1f20696b423f0770b436b4fdcef920d2c39d228912b12108dfb87f8`.
- Package manifest and notes: `manifest.json`, `manifest.md`, `ownership_scan.md`, `research/source_clearance.md`, `gfx_handoff.md`.

## Rejected and blocked leads

- Lewis Valentine is retained as complete source evidence but is `rejected_subject_owned` because Kaiserreich actively owns `WLS_lewis_valentine`, recruitment, portraits and localisation.
- Thomas Wynford Rees [SE3459](https://commons.wikimedia.org/wiki/File:Major_General_T_W_Rees,_commanding_19th_Indian_Division,_enters_Fort_Dufferin_in_Mandalay,_Burma,_19_March_1945._SE3459.jpg) is rejected because the source is a wide scene with a small face rather than a crop-grade portrait, and Kaiserreich actively owns `RAJ_thomas_wynford_rees` and its consumers.
- W. J. Gruffydd is `blocked_postwar_source` because the attributed photograph is dated 1946, after the 1936 scenario start date.
- Lewis Pugh Evans HU 93411 is `rejected_duplicate_failed_source` because it is the same source already used by the two failed Evans repaint trials in the 2026-07-24 replacement package.
- The January 1924 Underwood & Underwood J. H. Thomas image is retained only as a softer halftone comparison; the Bain photograph is the selected civic source.
- David Rhys Grenfell and George Cornwallis-West remain excluded after the parent reported repeated likeness failures.
- Saunders Lewis, Aneurin Bevan and William Ambrose Bebb remain excluded under the existing age-gate or Kaiserreich ownership evidence.

## Parent-owned next step

This package is not runtime-ready. The parent must choose whether the circa-1920 J. H. Thomas source is acceptable for the 1936 civic identity and whether the 1942 Ross source is acceptable for the alternate-history WLS commandant role. If accepted, use each exact crop as the sole identity input for source-locked identity-preserving ImageGen, perform independent likeness/style/provenance review, process to deterministic `156x210`, convert to DDS with the repository converter, and reconcile the current Saunders Lewis civic localisation before named wiring. Do not create advisor, dossier, `_small` or fallback assets from these sources.

## Scope confirmation

No ImageGen, DDS conversion, runtime/GFX/localisation/gameplay edits, advisor or dossier assets, or unrelated repository changes were made by this handoff.
