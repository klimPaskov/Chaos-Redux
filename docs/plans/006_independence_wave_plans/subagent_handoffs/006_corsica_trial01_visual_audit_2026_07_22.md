# IW-017 Corsica sourced portrait trial-01 independent visual audit

Audit date: 2026-07-22  
Auditor: generated-event-art subagent (independent review; not the producer)  
Package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/corsica_trial_01/`

## Decision

**Package admission: FAIL-CLOSED for both candidates.** The rendered images pass
the direct visual identity review below, but neither candidate is authorized for
DDS conversion or runtime wiring until the source-authority role mapping is
reconciled and the required subject-ownership evidence is recorded. Landry also
lacks a retained explicit source-crop record. This handoff does not create or
authorize a DDS, overwrite a runtime texture, or change `.gfx`.

The fail-closed decision is an admission/provenance decision, not a claim that
either face is a generated substitute. Both images are visibly grounded,
identity-preserving edits of the named male source photograph.

## Evidence and hash audit

All hashes below were recomputed from the files in the package and match
`hashes.sha256` and `manifest.md`.

| Item | Dimensions / mode | SHA-256 |
| --- | --- | --- |
| `source_masters/COR_adolphe_landry.jpg` | 512x724, grayscale JPEG | `f1afc654cfeb655313cb943aaab54e438df8c483abe54a96dbf229ad6fa7c9a8` |
| `raw_masters/COR_adolphe_landry_hoi4_trial_01.png` | 1081x1455, RGB | `07e28ddd0a4fb0e0db40b87407322320fa15b95fa0576a29db16c9cba1a7ff99` |
| `processed_png/COR_adolphe_landry.png` | 156x210, opaque RGBA | `a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505` |
| `source_masters/COR_jean_chiappe_gallica_f1_highres.jpg` | 1374x1054, grayscale JPEG | `2dd15d292a7caa8081b099e7234b41960ede3f2e46318d9b7e752b4570b9d378` |
| `source_masters/COR_jean_chiappe_source_crop_preview.png` | 156x210, opaque RGBA | `4c517f0e6f5a7db45f5f5ad6190dd5d95b5d86698c1ac6ff83d34bd03be04da2` |
| `raw_masters/COR_jean_chiappe_hoi4_trial_01.png` | 1081x1455, RGB | `703250cc5fff915991110aadf69549860a7f97ce3a1c220a185df7b4e4205614` |
| `processed_png/COR_jean_chiappe.png` | 156x210, opaque RGBA | `ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45` |
| `contact_sheets/source_result_style_comparison.png` | 2301x3082, RGB | `a02b122b1bf2d07a89be49d5a434ffd6726e7b76f03d1db19505d65365508ef1` |

The processed PNG for each subject is pixel-identical to a Lanczos resize of
its retained raw master (`1081x1455` to `156x210`); no hidden native-size edit
or post-generation face filter was found. No `.dds` exists in this trial
package, as expected from its review-only status.

I also read both identity-preserve prompt records, `hashes.sha256`, the review-
only `gfx_handoff.md`, and the complete trial manifest. The package's prompt
constraints agree with the grounded male, identity-preserving policy. The
canonical style families inspected were the only permitted references:
`assets/vanilla_reference/portraits/leaders/` and
`assets/vanilla_reference/portraits/commanders/`, including each family's
`contact_sheet.png` and cataloged native `156x210` examples.

## Source authority and rights

The required authority ledger is
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md`.
It records:

- Adolphe Landry: Agence Meurisse/BnF-Gallica portrait, 1917; Commons public
  domain (France/US), source hash matching the retained JPEG above.
- Jean Chiappe: Agence de presse Meurisse/BnF-Gallica portrait, 1927; Commons
  worldwide public-domain dedication, source hash matching the retained JPEG
  above.

Both subjects are real male people in a grounded Corsica package, so the
grounded-source-only gate is satisfied. The source authority itself is not
ambiguous about either identity or rights.

## Candidate 1 — Adolphe Landry

### Direct visual review: PASS

Reviewed the unchanged source, raw ImageGen master, 156x210 native PNG, and the
comparison sheet at native scale. The result preserves the source's narrow oval
face, high forehead, dark side-parted hair, strong brows, large dark eyes,
long straight nose, dense broad moustache, closed mouth, tapered jaw/chin,
visible ear, three-quarter head angle, and sober alert expression. It remains
recognisably the same man at both the raw and native sizes; there is no generic
face drift or imported face from the style references.

The native image is a centered male head-and-shoulders/bust portrait with full
hair, shoulders, lapels, white collar, tie/upper chest, and no hands. Dark suit
and collar construction remain source-backed for Landry's civilian civic role.
The finish is full-colour, quiet, controlled, and painterly in the vanilla HOI4
leader family: muted warm-grey/brown background, matte brush texture, restrained
contrast, no modern props, text, flag, watermark, frame, dossier card, or icon
artifacts. The source and result contain no extra people, female subject, or
fictional/generated substitute.

### Admission blockers

1. **Source-authority role mismatch.** The authority ledger maps Adolphe Landry
   to current consumer `COR_pasquale_venturi`, while this package maps him to
   `COR_corsican_municipal_congress`. The ledger maps that latter consumer to
   Jean Chiappe. This is a role/ownership conflict, not a visual question.
2. **Explicit crop evidence is incomplete.** The package has no retained
   Landry source-derived crop or crop coordinates; `manifest.md` explicitly
   says the raw master was resized as a full canvas with “no ... crop.” The
   rendered result visually has the required head-and-shoulders framing, but the
   fixed grounded-real-person source -> explicit crop -> ImageGen sequence is
   not evidenced for this candidate.
3. **Subject-ownership evidence is absent.** The package manifest does not list
   the required exact/variant name searches, roots/ids checked, no-match result,
   or guarded transfer contract. I therefore cannot attest non-duplication from
   this package alone.
4. **Reference-route provenance is not compliant.** The manifest names
   `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png`
   as the style-only reference. This audit route permits only the canonical
   `assets/vanilla_reference/` family; no skill-local quick-reference pack may
   serve as a generation/reference input. Replace or formally reconcile that
   provenance before admission.

**Candidate verdict: FAIL-CLOSED.** Do not convert
`a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505` to
`gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds`
or wire `GFX_portrait_COR_independence_wave_adolphe_landry` until all three
blockers are resolved. The exact PNG hash remains eligible for re-review after
the evidence and role mapping are corrected; no visual regeneration is required
by this audit.

## Candidate 2 — Jean Chiappe

### Direct visual review: PASS

Reviewed the unchanged Gallica source, the deterministic source crop, raw
ImageGen master, 156x210 native PNG, and the comparison sheet at native scale.
The result preserves Chiappe's high balding forehead and receding dark side
hair, long rounded face, sparse brows, small deep-set eyes with the same slight
off-centre gaze, long broad rounded-tip nose, clean-shaven cheeks/upper lip,
thin closed mouth, soft jowls, rounded chin, ears, apparent middle age, upright
stance, and controlled formal expression. The same person remains clear at both
raw and native sizes; there is no generic commander-face drift.

The native image is a centered male head-and-shoulders/bust portrait with full
head, shoulders, lapels, white collar, patterned tie, pocket square, and upper
chest. The civilian three-piece suit and small lapel pin are source-backed and
fit the stated administrative-security role; no invented uniform or enlarged
badge was introduced. The finish is full-colour, restrained HOI4 commander
family painting with quiet warm-grey/brown background, controlled values, and
visible but subdued brush texture. No modern props, text, flag, watermark,
advisor/dossier card, `_small` texture, icon treatment, extra people, female
subject, or fictional/generated substitute is present.

### Admission blockers

1. **Source-authority role mismatch.** The authority ledger maps Jean Chiappe to
   current consumer `COR_corsican_municipal_congress`, while this package maps
   that consumer to Adolphe Landry and assigns Chiappe to `COR_jean_chiappe`.
   The latter consumer has no corresponding authority-ledger row. This is a
   role/ownership conflict, not a visual question.
2. **Subject-ownership evidence is absent.** The package manifest does not list
   the required exact/variant name searches, roots/ids checked, no-match result,
   or guarded transfer contract. I therefore cannot attest non-duplication from
   this package alone.
3. **Reference-route provenance is not compliant.** The manifest names
   `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png`
   as the style-only reference. This audit route permits only the canonical
   `assets/vanilla_reference/` family; no skill-local quick-reference pack may
   serve as a generation/reference input. Replace or formally reconcile that
   provenance before admission.

**Candidate verdict: FAIL-CLOSED.** Do not convert
`ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45` to
`gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds`
or wire `GFX_portrait_COR_independence_wave_jean_chiappe` until the role mapping
and ownership evidence are corrected. The exact PNG hash remains eligible for
re-review after those corrections; no visual regeneration is required by this
audit.

## Required parent follow-up

1. Reconcile the authority ledger and package consumer mapping. Either update
   the authoritative source ledger with an accepted role change or restore the
   stable consumers to the ledger's assignments; do not silently swap the two
   real identities.
2. Add the required subject-ownership search evidence and any guarded transfer
   contract to the portrait manifest/handoff for both names.
3. Replace the disallowed skill-local quick-reference provenance with the
   canonical `assets/vanilla_reference/portraits/` family and retain the exact
   permitted reference paths in the manifest/prompts.
4. For Landry, retain and hash an explicit source-derived head-and-shoulders
   crop (or provide equivalent immutable crop coordinates and provenance) and
   rerun this independent review.
5. Only after a fresh independent PASS should the parent run the repository
   converter at `156x210`, inspect the complete legacy BGRA DDS header, and wire
   the two stable sprites. This audit authorizes no DDS or runtime mutation.
