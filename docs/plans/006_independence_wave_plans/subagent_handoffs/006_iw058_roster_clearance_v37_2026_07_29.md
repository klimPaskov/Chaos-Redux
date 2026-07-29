# IW-058 ASY roster source-clearance handoff

Date: 2026-07-29. Scope: source-only research for three grounded Assyrian male portrait candidates. No gameplay, event, character, localisation, GFX, DDS, or source-image repaint files were edited outside this bounded package. No commit was created.

## Package outputs

- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/source_files/asy_concordat_ignatius_afram_barsoum_pd_syria.jpg` — 500x656 RGB JPEG, SHA-256 `07ecd3da89959083eda76823025352f6970e620bbfdf338de0f127cfb7777f09`.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/source_files/asy_civic_rev_joel_e_werda_paris_1920.png` — 283x378 L PNG, SHA-256 `b2243d791bff5c61e9b6b157c69859885dda35cd17b09415012a83de06d8f0db`.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/source_files/asy_levies_malik_ismail_ii_baquba_1918_1919.jpg` — 1042x1669 RGB JPEG, SHA-256 `5ecae410a2bc8e6b69497a2a1ee18c06dc19e78360fcc0bb3bb9fe4833e3228b`.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/review/asy_roster_clearance_contact_sheet.png` — 1500x1030 RGB comparison sheet, SHA-256 `c8cf6545d3356e0adb63109bede6367bd540849890bcb33905ddc1ae254ee66`.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/manifest.md` — provenance, license, date, era-fit, role-fit, crop, collision, and blocker ledger.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/gfx_handoff.md` — parent-owned sprite suggestions and processing boundary.
- `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/hashes.sha256` — source and review-sheet hashes.

## Candidate decisions

1. `ASY_independence_wave_concordat_council`: Ignatius Afram I Barsoum is a strong active-period ecclesiastical portrait, but the subject is Syriac Orthodox rather than unambiguously Assyrian Church of the East. Commons marks the source public domain under PD-Syria, yet the parent must explicitly accept both the denominational identity and rights rationale. Status: `needs_user_review`.
2. `ASY_independence_wave_civic_national_assembly`: Rev. Joel E. Werda, also spelled Warda, is identified in the circa-1920 Paris Peace Conference delegation crop and in the Assyrian National Association delegation record. Living status in 1936 is unverified and the source is low-resolution. Status: `needs_user_review`.
3. `ASY_independence_wave_levies_guardianship`: Malik Ismail II is identified by the PCUSA Digital History record as an Assyrian Tyari chieftain; the identity record also documents his Assyrian volunteer command role. His death occurred in 1936, so confirm the IW-058 event date. Status: `source_ready` pending that date check.

## Ownership gate

The collision scan covered current Chaos Redux `common`, `history`, `gfx`, `interface`, and `localisation`, installed vanilla HOI4, and approved mods `1521695605`, `2265420196`, and `1458561226`. No exact owner was found for Afram, Werda, or Malik Ismail II. Mar Eshai, Dawid Mar Shimun, Yusuf Malek, Malik Yaqo, Yosip Khoshaba, Malik Qambar Warda, and Benjamin Arsanis were rejected or blocked because of exact vanilla/Kaiserreich owners, current rights/identity problems, group-only crops, AI-retouched imagery, or wrong-era sources. The existing Naum Faiq and Agha Petros rows remain legacy-continuity options and are not silently promoted.

## Parent next steps

- Resolve whether a Syriac Orthodox patriarch is acceptable for the concordat-council consumer or request a living-1936 Assyrian Church of the East source.
- Resolve Werda/Warda identity spelling, 1936 living status, and low-resolution acceptability before any crop or repaint.
- Verify the IW-058 event date against Malik Ismail II's 1936 death and then run the repository portrait-processing and independent audit pipeline if approved.
- Keep the source masters immutable and do not wire any candidate directly from this package.
