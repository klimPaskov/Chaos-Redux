# Event 006 Northwestern Europe sourced-portrait research handoff

Date: 2026-07-22
Owner: `/root/event6_nwe_sourced_portraits`
Scope: source-mode research and original master acquisition only. No gameplay,
GFX/interface, advisor, localisation, crop, resize, PNG, DDS, or runtime edits.

## Deliverables

- [Northwestern Europe portrait ledger](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md)
- [SHA-256 inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/source_hashes.sha256)
- Fourteen verified, non-empty original JPEG/TIFF masters under
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/source_masters/`.

The manifest is the role-complete ledger for the twenty non-protected Event 006
Northwestern Europe leader/commander rows. Every commander row lists both its
large and `_small` runtime consumer. The two protected existing portraits (RHI
Josef Friedrich Matthes and BAY Rupprecht) are explicitly recorded as
`protected_not_touched` and were not copied.

## Package status

- `source_ready`: 12 rows with a downloaded original and a recorded source/rights
  basis (the original six plus AEX Staf De Clercq, AEX Joris Van Severen, AFX
  Jules Destrée, SCO Robert Bontine Cunninghame Graham, SCO William Edmund
  Ironside, and WLS David Lloyd George).
- `needs_rights_review`: 2 rows with a downloaded original but unresolved
  archive/license or role-fit questions (AJX Max Braun, RHI Wilhelm Sollmann).
- `blocked`: 6 rows with a defensible candidate/source page but no verified local
  original after the bounded retry: AJX Johannes Hoffmann, BRI Morvan Marchal,
  BRI Célestin Lainé, BAY Heinrich Held, BAY Franz Ritter von Epp, and WLS
  Saunders Lewis. Wikimedia upload requests returned HTTP 429; no HTML,
  zero-byte, paid-rights, proxy, or generated substitute was retained.

The fourteen retained files have dimensions, byte counts, and SHA-256 values in
`manifest.md` and `source_hashes.sha256`. The masters are deliberately not
game-ready; a later pass must perform the separate identity-preserving portrait
processing/visual approval workflow before any DDS conversion.

## Second bounded retry record

The six newly retained masters are:

- `source_masters/AEX/AEX_staf_de_clercq.jpg` (335x480; Commons direct original;
  PD-anon-70-EU/PDM basis with territorial review caveat).
- `source_masters/AEX/AEX_joris_van_severen.jpg` (590x960; Commons direct
  original; PD-anon-70-EU/PDM basis with territorial review caveat).
- `source_masters/AFX/AFX_jules_destree.jpg` (891x1216; *Le Patriote Illustré*,
  12 Jan 1936; public-domain historical press image).
- `source_masters/SCO/SCO_cunninghame_graham_rijksmuseum.jpg` (3846x4852;
  Rijksmuseum IIIF/CC0 institutional original; full page/object scan).
- `source_masters/SCO/SCO_edmund_ironside_loc_1920.tif` (1199x1536; Library of
  Congress TIFF; “No known restrictions on publication”).
- `source_masters/WLS/WLS_david_lloyd_george_bystander_page_n363.jpg`
  (2500x3953; Internet Archive *The Bystander* page scan, Haines, 13 Nov 1907;
  public-domain publication basis).

All six are face-visible, attributable, and retained as untouched originals.
The 12-row retry therefore leaves six roles blocked: AJX Johannes Hoffmann,
BRI Morvan Marchal, BRI Célestin Lainé, BAY Heinrich Held, BAY Franz Ritter
von Epp, and WLS Saunders Lewis. A Bundesarchiv alternate for Held (and a
separate Bundesarchiv alternate for von Epp) was rejected because the catalogue
did not provide free reuse; neither paid-rights file remains in the package.

## Follow-up queue and cautions

1. The six `blocked` candidates remain queued for a future source pass. Retry
   them from their listed source/archive pages when access is available; verify
   each downloaded file is the named original bitstream, not an HTML/error page,
   paid-rights image, or proxy re-encode.
2. Obtain rights/role approval for Max Braun and Wilhelm Sollmann before using
   their local masters. Both are civilian political organizers rather than
   unambiguous military commanders; do not silently promote them to commanders.
3. Pieter Reenalda is a strong uniformed maritime portrait from the Frisian
   Tresoar family archive, but the ledger marks the Friesland connection as
   low/medium confidence. Parent review is required before processing.
4. Preserve the historical-risk notes for Staf De Clercq, Joris Van Severen,
   Célestin Lainé, and Franz von Epp if any of those candidates are later used.
5. Do not alter the protected RHI Matthes or BAY Rupprecht assets, and do not
   place unreviewed masters in runtime folders.
