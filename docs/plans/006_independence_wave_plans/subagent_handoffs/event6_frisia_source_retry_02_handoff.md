# Event 006 Frisia source retry 02 handoff

Date: 2026-07-22  
Owner: `chaosx_asset_source_researcher` (source-only retry)  
Scope: stronger archival source masters for the exact grounded male AGX
identities Douwe Kalma and Pieter Reenalda.

## Delivered source package

Manifest: [frisia retry 02 manifest](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/frisia_retry_02/manifest.md)

Source package root:
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/frisia_retry_02/`

- `source_masters/AGX_douwe_kalma_1917.jpg` — unchanged Tresoar/Commons
  original, 691x1013 RGB, 87,040 bytes, SHA-256
  `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`.
  Recommended identity base for `AGX_friesland_coastal_council` because the
  face is centered, frontal, and much clearer than the previous 1922 passport
  master. The archive credits F.O. Strüppert, circa 1917, and declares the item
  public domain.
- `source_masters/AGX_pieter_reenalda_1915_garden.jpg` — unchanged
  Tresoar/Commons original, 1023x1619 grayscale, 91,591 bytes, SHA-256
  `d97dc109f6d9e172b63004a0655fb8995c9bd7d7e3935dd6a85858083414aee2`.
  Recommended identity-clarity base for `AGX_friesland_coastal_commander`;
  the archive identifies Pieter Reenalda, 1915, by F.O. Strüppert and declares
  the item public domain.
- `source_masters/AGX_pieter_reenalda_1911_uniform_prior.jpg` — unchanged
  copy of the prior package's 1911 KPM-uniform master, 1243x1787 grayscale,
  183,898 bytes, SHA-256
  `2830fdc7d56040c2a3fa6a6f686bfd73126612786cc6eba80d428863190c488f`.
  Keep as the role-context comparison: it proves the maritime first-officer
  appearance more directly, but its native face is less clear than the 1915
  garden source.
- `candidate_contact_sheet.png` — review-only comparison of the selected
  masters and exact-person alternates; never wire this sheet into the game.
- `source_hashes.sha256` — hash inventory for the three source masters.

Exact source URLs, archive GUIDs, estimated dates, license/public-domain basis,
crop estimates, candidate dispositions, and all ownership-search evidence are
in the manifest. Candidate originals retained for comparison include Kalma's
1924 office photograph and Reenalda's 1911 square/Buyskes and 1903 costume
photographs; none is a generated substitute.

## Ownership and role checks

The exact/variant terms `Douwe Kalma`, `Kalma, Douwe`, `Douwe_Kalma`, `Pieter
Reenalda`, `Reenalda, Pieter`, `Pieter_Reenalda`, and `Reenalda` were searched in
the installed vanilla and project `common/characters/`, `history/countries/`,
`gfx/leaders/`, `interface/`, and `localisation/` roots on 2026-07-22.

- Vanilla had no exact person or variant hit and no character/portrait owner.
- Project had no competing character/history/GFX/interface owner. The only
  literal full names are the intended AGX localisation labels. The live AGX
  character tokens are `AGX_friesland_coastal_council` and
  `AGX_friesland_coastal_commander` in
  `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-125`,
  recruited by `history/countries/AGX - Frisia.txt:17-18`; both are male.
- The leader uses only a large civilian portrait. The commander uses only a
  full large army portrait and is checked as a corps commander. No advisor,
  dossier, `_small`, or alternate-country consumer was found; no transfer guard
  is needed.

## Parent handoff / next action

1. Treat Kalma 1917 as the first downstream identity-preserving processing input.
2. Review Reenalda 1915 garden versus the retained 1911 KPM-uniform master. The
   1915 source has stronger face geometry; the 1911 source has stronger explicit
   maritime-command context. Do not merge faces or invent a uniform.
3. If processing is attempted, use only the unchanged source master as the
   identity image reference and require a direct before/after likeness review
   against the source. No generated or generic face may replace either person.
4. If identity drift or role evidence remains unacceptable, mark that portrait
   `blocked`/`needs_user_review` and keep the source-only package; do not use an
   advisor, `_small`, female, generic, or fictional fallback.
5. The main agent still owns any processed PNG, DDS conversion, `.gfx` wiring,
   runtime references, and final admission audit. This handoff performed none of
   those actions.

## Explicit boundary / blockers

No portrait treatment, crop, resize, processed PNG, DDS, `.gfx`, character,
history, event, focus, decision, GUI, localisation, spreadsheet, flag, or
runtime edit was made. The source gates clear for both exact identities; the
downstream HOI4 painted-finish gate remains open and requires parent review.
The Reenalda 1915 source is civilian dress, so role-context approval is still
required even though the companion 1911 record documents his KPM first-officer
role. If that caveat is not accepted, the exact role should be blocked rather
than replaced with another person's face.

