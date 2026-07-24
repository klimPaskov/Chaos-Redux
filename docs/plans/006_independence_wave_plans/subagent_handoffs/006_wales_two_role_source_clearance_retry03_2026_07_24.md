# IW-002 Wales two-role sourced portrait clearance handoff - retry 03

This handoff covers only archival source research, source rights notes, ownership checks, exact source crops, and the GFX handoff for the two existing WLS independence-wave portrait roles. It does not edit gameplay, characters, history, localisation, interface, GFX, or spreadsheets.

## Outcome

The source-clearance pass found a clean pre-war Welsh civic candidate and a clean archival Welsh-born military candidate:

- David Rhys Grenfell for `GFX_portrait_WLS_independence_wave_national_council`.
- Major George Frederick Myddleton Cornwallis-West for `GFX_portrait_WLS_independence_wave_mountain_commandant`.

Both are source-ready for the parent-owned downstream identity-preserving portrait pipeline, but both remain `needs_user_review` until the required source-locked ImageGen, independent likeness/style/provenance audit, deterministic `156x210` processing, and DDS conversion are completed. No fallback was created.

## Role-by-role status

### Civic or national leader: David Rhys Grenfell

**Source clearance: PASS.** Grenfell was a Welsh Labour MP for Gower from 1922 to 1959 and a Welsh Parliamentary Labour Party chair, so he is a defensible Welsh civic-national figure alive in the 1936 setting.

The selected archival source is the 1922 Bassano Ltd portrait recorded by the National Portrait Gallery and distributed on Wikimedia Commons as Public Domain. The unchanged downloaded JPEG is `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_png/david_grenfell_civic_candidate.jpg` with SHA-256 `5bf5bfe500c724961acd4f56e3057f5a53981fcb779060bf9a79e901a7515749`.

The decoded lossless master is `source_master_png/david_grenfell_civic_master.png` with SHA-256 `7b613faad429e155133b60fb9e4c403639281e7054df47f07d5cdd6ea3e10e70`. The exact head-and-shoulders crop is `exact_crops/david_grenfell_civic_crop.png` with SHA-256 `55f5cd025f7bfc070f3b821e90bcfabba0ba6daafffcb6d4a161a1a7db73392f` and crop rectangle `(70,65)-(600,790)`. Its JSON evidence reports `decoded_pixels_equal: true` and matching master/output RGBA hash `05abcfec333dfe203df00e6f4c4755a55276c9d0339d5dc5234880433572fa19`.

The institutional source record is <https://www.npg.org.uk/collections/search/portrait/mw64853/David-Rhys-Grenfell>. The Commons page is <https://commons.wikimedia.org/wiki/File:David_Grenfell.jpg>. Preserve the Bassano Ltd and National Portrait Gallery credit in downstream provenance notes.

### Military, territorial, or mountain commander: Major George Frederick Myddleton Cornwallis-West

**Source clearance: PASS with rights-review note.** Cornwallis-West was born in Ruthin, Wales, and was an officer of the Scots Guards who also served with the Royal Marines and Royal Naval Division in the First World War. He is a defensible military-commandant identity for the existing WLS token, although the source does not establish a specialist Welsh mountain command.

The selected archival source is a single-person Henry Walter Barnett portrait dated by Commons between 1900 and 1910 and marked Public Domain. The unchanged downloaded JPEG is `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/source_png/george_cornwallis_west_original.jpg` with SHA-256 `95068427782c799d86644133e1654b995569aebd51267da10f1d1e1baf16e3e8`.

The decoded lossless master is `source_master_png/george_cornwallis_west_commander_master.png` with SHA-256 `dba6c6bc4b5a261c4e761323944bc2d504b0f3de992f0d8301f2d28535e5ed2c`. The exact head-and-shoulders crop is `exact_crops/george_cornwallis_west_commander_crop.png` with SHA-256 `3483095e908cd993d46469d4033aaba4ad8cf7009e3bd7d8ba69f890cea066c4` and crop rectangle `(40,40)-(1040,1320)`. Its JSON evidence reports `decoded_pixels_equal: true` and matching master/output RGBA hash `3b41102af8cc896b2afd2620160dadb7304c9fd2c371da30eaf0200fd57422ec`.

The Commons page is <https://commons.wikimedia.org/wiki/File:Georgecornwalliswest.jpg>. Preserve the Henry Walter Barnett credit. Commons presents a Public Domain record with a PD-Art jurisdiction caution, so the final provenance reviewer must retain that caution instead of asserting unrestricted worldwide rights without review.

### Held civic alternate: W. J. Gruffydd

**Status: HOLD.** The Cardiff University portrait is clear, attributed, and CC BY-SA 4.0, but the available image is dated 1946. That is postwar for the 1936 setting, so it remains an alternate only unless the parent explicitly approves the era exception.

### Blocked civic alternate: William Ambrose Bebb

**Status: BLOCKED.** The circa-1930 National Library of Wales portrait is an excellent period fit and Public Domain, but approved reference mod `1521695605` actively owns `WLS_ambrose_bebb`, its portrait consumers, and its localisation identity. It cannot be reused.

### Blocked civic alternate: David Lloyd George

**Status: BLOCKED.** The source is clear, but installed vanilla owns the English identity and localisation surfaces. It cannot be reused for this WLS role.

## Ownership and source evidence

The ownership roots, exact search terms, match summary, and existing WLS consumer note are recorded in `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_24/wales_two_role_retry_03/ownership_scan.md`.

Commons API snapshots for the retained and comparison sources are in `source_page_snapshots/`. The source comparison contact sheet is `contact_sheets/wales_two_role_retry03_portrait_candidates.png`.

## Parent-owned next step

Use the two exact crops as immutable identity references for separate source-locked identity-preserving ImageGen passes. Use canonical vanilla portraits only for style. Obtain independent likeness/style/provenance review, then create the deterministic `156x210` PNGs and repository-standard DDS files. Wire only after those downstream gates pass; this subtask performed no ImageGen, final PNG, DDS, GFX, or gameplay work.

