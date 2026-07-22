# Event 006 Mediterranean / Volga / Assyria gap-retry handoff

Research mode: sourced real male portraits only. Research/download date:
2026-07-22. Parent scope was limited to unchanged archival masters; no crop,
resize, processing, DDS, `.gfx`, gameplay, localization, advisor, or dossier
files were produced.

## Source-ready tranche

Four candidates cleared the source, identity, rights, and role/era screen and
are recorded in the package manifest:

| Role | Real identity | Master | Dimensions / bytes | SHA-256 | Why it fits |
|---|---|---|---:|---|---|
| `ASX_salvatore_licata` | Luigi Rizzo | `source_masters/sicily/asx_luigi_rizzo_rear_admiral_1935.jpg` | 402x582 / 125,508 | `aa113393b9b51ed481bfa485aaf729e867c20c6a364b41d3f8999b0dc2c8663e` | Milazzo-born Sicilian Regia Marina rear admiral; source book is dated 1935 and the face is a direct period portrait. Commons records PD-Italy/PD-1996. |
| `CHU_independence_wave_federal_presidium` | Galimzhan Ibrahimov | `source_masters/volga/chu_galimzhan_ibrahimov.jpg` | 863x1272 / 344,829 | `931a6dd35f70e2fd4fbd58aafd030d60a2755dc6a7dc68704b8267aefb864532` | Tatar writer, politician, and Constituent Assembly member; 1920s source from Kazan State University library with a Commons public-domain mark. |
| `ASY_independence_wave_civic_national_assembly` | Naum Faiq | `source_masters/assyria/asy_naum_faiq_1920s.jpg` | 466x618 / 151,906 | `3c69fe811703407a76dd2ac4508ae4b54d5fc6693a0150e0a26ebeadfc059444` | Standalone 1920s face portrait from the 1936 Damascus memorial volume; Assyrian nationalist civic legacy identity; Commons PD-Syria/PD-US rationale. |
| `ASY_independence_wave_levies_guardianship` | Agha Petros | `source_masters/assyria/asy_agha_petros_1920.jpg` | 794x1130 / 295,869 | `ad63874811c26570d9b624dc1c693036c8b1584faf0fe35ce5a6905ae00bccc1` | Assyrian military leader shown in uniform in 1920; H. G. Donatossian source with Commons public-domain mark. |

These are source-ready masters, not final portraits. The parent must still
perform the separate visual review and approved portrait processing before any
runtime asset is created.

## Fail-closed gaps and rejected evidence

- `ARX_gavino_piras`: Luigi Efisio Marras is Sardinian and alive in 1936, but
  the only located image is explicitly from the 1950s and only 255x346; blocked.
- `ARX_sardinian_crown_consultative_council`: Pietro Mastino is a strong
  Sardinian civic source (1920s, 367x600, CC BY-SA 4.0) but is not a documented
  dynastic/crown officeholder; blocked as role-mismatched.
- `CHU_independence_wave_bolgar_civic_presidium`: Shamil Usmanov is a direct
  Tatar identity, but 187x250 is below the quality gate; blocked.
- `CHU_independence_wave_river_security_directorate`: the Bashkir Zeki Velidi
  Togan master is retained as `needs_review` because its institution/unknown
  photographer/date chain needs a rights review. The downloaded Musa Murtazin
  file is a group image, not a one-person portrait, and is blocked.
- `ASY_independence_wave_concordat_council`: the Library of Congress Mar
  Benyamin Shimun XXI master is rights-clear but the subject died in 1918, so it
  cannot fill a living 1936 concordat office without an explicit design choice;
  blocked. Malik Ismail II remains blocked due a visible watermark and no
  reusable family license. Mar Eshai Shimun XXIII Foundation photos were not
  copied because the Foundation states they are copyright protected.

No generated, generic, female, modern, watermarked, group, cropped, or
re-encoded substitute was handed off.

## Files and documentation

- Source package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/`
- Full source/rights/era ledger and hashes: package `manifest.md`.
- Deferred runtime-name notes: package `gfx_handoff.md`.
- Only unchanged masters are present under `source_masters/`; there are no
  processed PNGs, DDS files, contact sheets, or `.gfx` edits.

## Meaningful validation

All ten downloaded files were opened and verified as valid JPEGs with Pillow;
their dimensions, byte counts, and SHA-256 hashes are recorded in the package
manifest. The group Murtazin image was visually rejected as non-individual;
the four source-ready files were visually inspected for a clear face and
period/role plausibility.
