# IW-017 Corsica sourced portrait trial-01 fresh provenance re-audit

Audit date: 2026-07-22  
Auditor: generated-event-art subagent (independent of the producer)  
Revision audited: post-`347d25216` (`Reconcile Corsica portrait provenance`)  
Package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/corsica_trial_01/`

## Decision

**Both exact processed PNGs PASS and are authorized for repository-standard DDS
conversion.** The fresh review clears the previous provenance blockers:

- the source-authority ledger now maps `COR_corsican_municipal_congress` to
  Adolphe Landry and `COR_jean_chiappe` (replacing archived fictional
  `COR_pasquale_venturi`) to Jean Chiappe;
- the Landry source-derived crop is retained and hash-pinned, with the prior
  treatment ledger's crop coordinates;
- the manifest records the exact ownership searches and guarded IW-017
  recruitment/retirement boundary; and
- the documented quick-reference sheets are explicitly permitted style-only
  inputs and are byte-identical copies of the canonical role families.

This audit authorizes conversion only. It does not run the converter, modify a
DDS, edit `.gfx`, or make the post-wiring country-package attestation. The
existing runtime DDS files are stale relative to these trial PNGs and must be
replaced by the parent using the exact approved PNG hashes below.
The authorization is hash-scoped: no alternate, renamed, or stale DDS source is
implicitly approved.

## Current runtime and wiring state

The live character, localisation, scripted-effect, trigger, and GFX surfaces
were checked directly:

- `common/characters/006_independence_wave_mediterranean_characters.txt`
  defines `COR_corsican_municipal_congress` with visible name
  `COR_adolphe_landry`, male gender, and only the large civilian sprite
  `GFX_portrait_COR_independence_wave_adolphe_landry`.
- The same file defines `COR_jean_chiappe` with visible name
  `COR_jean_chiappe`, male gender, large civilian and large army sprites, and
  a corps-commander record.
- `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`
  recruits, promotes, and retires those two current COR ids through the IW-017
  package adapter; no live `COR_pasquale_venturi` effect remains.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`
  requires the two current COR records and checks Chiappe's corps-commander
  status.
- `localisation/english/006_independence_wave_mediterranean_l_english.yml`
  identifies Landry as the civic leader and Chiappe as the emergency/security
  authority.
- `interface/006_independence_wave_mediterranean_portraits.gfx` points the two
  stable sprites to the handoff paths and intentionally declares no small or
  advisor sprite.

An exact search for `COR_pasquale_venturi`, `pasquale_venturi`, and `Pasquale
Venturi` returned no matches in live `common/`, `history/`, `interface/`,
`localisation/`, `gfx/`, or `events/`. Remaining matches are archived source,
review, or documentation records only. Vanilla and approved workshop roots
(`1521695605`, `2265420196`, and `1458561226`) also returned no matching
character, recruitment, portrait, or officeholder ownership.

## Reference-route recheck

Per the current `chaos-redux-event-assets` section 4, I inspected both required
reference families and the matching quick-reference sheets:

- canonical leaders: `assets/vanilla_reference/portraits/leaders/` and its
  `contact_sheet.png`;
- canonical commanders: `assets/vanilla_reference/portraits/commanders/` and
  its `contact_sheet.png`;
- permitted leader quick-reference: `assets/leader_portraits/leaders/` and
  `contact_sheet.png`;
- permitted commander quick-reference: `assets/leader_portraits/commanders/`
  and `contact_sheet.png`.

The quick-reference README and manifest state that the eight copied PNGs are
reference-only, male-presenting, native `156x210`, and byte-identical to the
canonical PNGs. Independent SHA checks confirmed all eight pack/canonical pairs
match. The package's style-only references are therefore permitted and do not
constitute runtime substitutes, copied identities, advisor art, dossier cards,
or `_small` derivatives.

## Package hash and dimension audit

All retained package hashes below were recomputed. The existing trial portrait
hashes are unchanged from the prior visual audit; only the retained Landry crop
is new in this revision.

| Item | Dimensions / mode | SHA-256 | Result |
| --- | --- | --- | --- |
| `source_masters/COR_adolphe_landry.jpg` | 512x724, grayscale JPEG | `f1afc654cfeb655313cb943aaab54e438df8c483abe54a96dbf229ad6fa7c9a8` | unchanged source |
| `source_masters/COR_adolphe_landry_source_crop_preview.png` | 156x210, opaque RGBA | `cc96ee5e74165c6713e4df052816064f546197530a5cbc700858f13e11ee54c3` | new explicit source crop |
| `raw_masters/COR_adolphe_landry_hoi4_trial_01.png` | 1081x1455, RGB | `07e28ddd0a4fb0e0db40b87407322320fa15b95fa0576a29db16c9cba1a7ff99` | unchanged raw master |
| `processed_png/COR_adolphe_landry.png` | 156x210, opaque RGBA | `a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505` | **DDS authorized** |
| `source_masters/COR_jean_chiappe_gallica_f1_highres.jpg` | 1374x1054, grayscale JPEG | `2dd15d292a7caa8081b099e7234b41960ede3f2e46318d9b7e752b4570b9d378` | unchanged source |
| `source_masters/COR_jean_chiappe_source_crop_preview.png` | 156x210, opaque RGBA | `4c517f0e6f5a7db45f5f5ad6190dd5d95b5d86698c1ac6ff83d34bd03be04da2` | retained source crop |
| `raw_masters/COR_jean_chiappe_hoi4_trial_01.png` | 1081x1455, RGB | `703250cc5fff915991110aadf69549860a7f97ce3a1c220a185df7b4e4205614` | unchanged raw master |
| `processed_png/COR_jean_chiappe.png` | 156x210, opaque RGBA | `ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45` | **DDS authorized** |
| `contact_sheets/source_result_style_comparison.png` | 2301x3082, RGB | `a02b122b1bf2d07a89be49d5a434ffd6726e7b76f03d1db19505d65365508ef1` | unchanged comparison |

Both processed PNGs are pixel-identical to a Lanczos resize of their retained
raw masters to `156x210`. Both source crop previews are opaque `156x210` files.
The package contains no DDS; the authorized runtime targets remain the two
paths in the GFX handoff.

## Landry — PASS / DDS authorized

The source authority ledger now records Adolphe Landry for the stable
`COR_corsican_municipal_congress` civic token, with the 1917 Agence Meurisse /
BnF-Gallica source and public-domain France/US basis. The source-treatment
ledger records the explicit crop `(36,0,476,592)` from the unchanged `512x724`
master. The retained crop preview hash is
`cc96ee5e74165c6713e4df052816064f546197530a5cbc700858f13e11ee54c3`; it shows
the same source face and adds no generated detail.

At raw and native size, the ImageGen edit remains recognisably the same man:
narrow oval face, high forehead, side-parted dark hair, heavy moustache,
distinctive brows and eyes, long straight nose, tapered jaw, visible ear,
three-quarter angle, and sober alert expression all hold. The centered
head-and-shoulders/bust crop retains source-backed dark lapels, white collar,
tie/upper chest, and no hands. The muted warm-grey/brown background and subtle
full-colour brush treatment read as restrained vanilla HOI4 leader art rather
than a raw photograph, sepia filter, generic face, or reconstructed identity.

The exact ownership searches listed in the current manifest cover `Adolphe
Landry`, `Adolphe_Landry`, both `COR_` forms, all relevant Chaos Redux roots,
vanilla roots, and the three approved workshop roots. Only the intended COR
definition/consumer and its documentation matched; no competing owner or
transfer contract is needed because the IW-017 adapter recruits and retires the
character within the guarded package.

**Authorization:** convert exactly
`processed_png/COR_adolphe_landry.png`
(`a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505`) to
`gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds`
at `156x210`, then retain sprite
`GFX_portrait_COR_independence_wave_adolphe_landry`.

## Chiappe — PASS / DDS authorized

The source authority ledger now records Jean Chiappe for dedicated
`COR_jean_chiappe`, explicitly replacing archived fictional
`COR_pasquale_venturi`. The 1927 Agence Meurisse / BnF-Gallica source is listed
with Commons worldwide public-domain dedication. The retained source crop hash
is `4c517f0e6f5a7db45f5f5ad6190dd5d95b5d86698c1ac6ff83d34bd03be04da2`, and the
source-treatment ledger records crop `(560,120,860,524)`.

At raw and native size, the edit preserves Chiappe's high balding forehead,
receding side hair, long rounded face, sparse brows, small deep-set eyes and
off-centre gaze, broad rounded-tip nose, clean-shaven upper lip, thin mouth,
soft jowls, rounded chin, ears, apparent middle age, and controlled formal
expression. The centered bust retains the source-backed civilian three-piece
suit, patterned tie, pocket square, and small lapel pin without invented
uniform or enlarged insignia. The full-colour muted painterly finish fits the
commander family while remaining an administrative-security portrait; it does
not drift into a generic commander face, advisor/dossier card, `_small` texture,
female portrait, or fictional substitute.

The exact ownership searches listed in the current manifest cover `Jean
Chiappe`, `Jean_Chiappe`, both `COR_` forms, all relevant Chaos Redux roots,
vanilla roots, and the three approved workshop roots. Only the intended COR
definition/consumer and its documentation matched; no competing owner or
transfer contract is needed because the IW-017 adapter recruits and retires the
character within the guarded package.

**Authorization:** convert exactly
`processed_png/COR_jean_chiappe.png`
(`ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45`) to
`gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds`
at `156x210`, then retain sprite
`GFX_portrait_COR_independence_wave_jean_chiappe`.

## Existing runtime DDS warning

The two runtime DDS files already present at the handoff paths are valid
one-level uncompressed BGRA `156x210` files (`131168` bytes, correct legacy
header), but they do **not** decode pixel-identically to the approved trial
PNGs. Their hashes are:

- `portrait_COR_independence_wave_adolphe_landry.dds` —
  `c76b8f66aad39b90288bf216f388d642c7297f4a4e4701b223c378bda7d9b523`;
- `portrait_COR_independence_wave_jean_chiappe.dds` —
  `83014381e587873b461d8cd71c0d6ba958364a54085d17a157c6ee40c4e6de79`.

Decoded runtime RGB means are approximately `[89.3, 89.1, 89.0]` (Landry)
and `[70.5, 70.5, 70.5]` (Chiappe), while the approved full-colour PNGs are
approximately `[88.7, 80.3, 70.2]` and `[84.8, 75.2, 63.4]`, respectively.
These are stale prior-treatment textures, not the current approved trial
renders. The parent may overwrite them only by running the repository-standard
converter on the exact approved PNGs above, then performing the required
post-wiring country-package audit.

## Final handoff state

| Candidate | Visual likeness | Source/rights | Crop/provenance | Ownership | DDS conversion |
|---|---|---|---|---|---|
| Adolphe Landry | PASS | PASS | PASS; crop `(36,0,476,592)`, hash pinned | PASS; exact roots/searches recorded, no competing owner | **AUTHORIZED** |
| Jean Chiappe | PASS | PASS | PASS; crop `(560,120,860,524)`, hash pinned | PASS; exact roots/searches recorded, no competing owner | **AUTHORIZED** |

No advisor, dossier, `_small`, female, flag, focus, decision, or gameplay asset
was created by this re-audit. Runtime/GFX files were not edited. IW-017 still
requires the fresh post-wiring country-package audit named in the GFX handoff;
that remaining requirement does not block conversion of these two exact PNGs.
