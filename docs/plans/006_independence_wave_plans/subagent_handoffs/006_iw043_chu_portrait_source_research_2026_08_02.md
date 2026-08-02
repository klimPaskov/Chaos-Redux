# IW-043 CHU portrait source-research handoff — 2026-08-02

Scope: bounded archival source research for one real male CHU leader candidate. No gameplay, country, character, localisation, `.gfx`, DDS, admission, or attestation file was edited. The parent remains responsible for final role selection, source-locked repaint, independent audit, DDS conversion, and runtime wiring.

## Candidate

**Muhammed Ayaz İshaki / Gayaz Ishaki (1878–1954)** is a Tatar journalist, publisher, politician, and leading figure of the Tatar national movement born near Kazan. The retained biography records his 1918 Idel-Ural State secretary-of-state role and 1931 chairmanship of the Independence Committee of the Muslims in Idel-Ural. He was alive in the 1936 baseline. This is a plausible `CHU_independence_wave_federal_presidium` candidate; the exact fictional office transfer is `PASS with parent review`, not a historical claim of a literal 1936 appointment.

## Evidence package

All files are under [`docs/assets/006_independence_wave/iw043_chu_portrait_source_research_2026_08_02/`](../../../assets/006_independence_wave/iw043_chu_portrait_source_research_2026_08_02/).

- Primary solo source master: `source_masters/gayaz_ishaki_book_plate.jpg`, 2361×3393 RGB JPEG, SHA-256 `e2cc555c9a6fb63f0707b77038195d41aafa1d01e6a9be584116f2582245803e`.
- Primary source page: [Commons `Muhammad Ayaz Ishaqi`](https://commons.wikimedia.org/wiki/File:Muhammad_Ayaz_Ishaqi.jpg); direct original: [upload.wikimedia.org original](https://upload.wikimedia.org/wikipedia/commons/0/09/Muhammad_Ayaz_Ishaqi.jpg).
- Primary rights basis: Commons `{{PD-old-70-1923}}`; metadata reports public domain, `Copyrighted=False`, and `AttributionRequired=False`. The file credits Ahmet Kanlidere, *Reform within Islam: The Tajdid and Jadid Movement among the Kazan Tatars (1809–1917). Conciliation or Conflict?* (Istanbul, 1997). Photographer and first-publication chain remain unknown, so status is `needs_user_review` rather than cleared.
- Exact primary crop: `source_crops/gayaz_ishaki_book_plate_head_shoulders.png`, crop `(80,0,2250,3050)`, 2170×3050 RGB PNG, SHA-256 `a276710b8816b218941040329ea34c8ca57b55f47b65c18998836f8f25fdef11`; `source_metadata/gayaz_ishaki_book_plate_crop.json` proves decoded-pixel equality.
- Corroborating solo source: `source_masters/gayaz_ishaki_1911.jpg`, 1790×1956 RGB JPEG, SHA-256 `1db02884643a83b61ff35afdbf4e913408aa2bf27d2145bcf7e1abc1aa1b2c32`; [Commons page](https://commons.wikimedia.org/wiki/File:%C4%9Eayaz_Ishaqi,_1911.jpg); rights tag `{{PD-old}}`; crop `(300,0,1510,1650)` at `source_crops/gayaz_ishaki_head_shoulders.png`, SHA-256 `16c22b97b3f67d51d95036f01f97d72f2b41deb02180585e9b0bf6c043705b21`; equality JSON retained.
- Raw Commons API snapshots and crop JSON are retained under `source_metadata/`; `hashes.sha256` records the immutable source/crop hashes.
- Ownership preflight in `ownership_audit.md`: no exact or variant character, leader, commander, operative, advisor, portrait, sprite, recruitment, or localisation owner found in Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`. Parent must repeat immediately before creating a runtime token.

## Parent action

1. Decide whether a Volga-Tatar Idel-Ural émigré politician is acceptable for the fictional CHU federal-presidium role.
2. Resolve unknown photographer/first-publication uncertainty and approve or reject the Commons `PD-old` basis.
3. If approved, run the repository real-person sequence from the exact primary crop: source-locked country-leader repaint, independent likeness/style/provenance audit, then deterministic 156×210 candidate and DDS conversion. Do not wire the raw photograph or a mere resize.
4. Keep the candidate `needs_user_review` and do not alter CHU admission or stable sprite paths in this tranche.

An exploratory `sadri_maksudi_finland_1920.jpg` group photograph is retained in the evidence folder but is explicitly unselected in `manifest.md`; do not use it without a new review.
