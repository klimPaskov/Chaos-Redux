# IW-007 Frisia retry-02 independent portrait audit

Date: 2026-07-22  
Scope: visual/source audit only; no DDS, `.gfx`, gameplay, localisation, or
producer-package edits.

## Evidence reviewed

Reviewed every file in
`docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia_retry_02/`:
the two unchanged source masters, all raw ImageGen masters, the three retained
156x210 processed candidates plus the unchanged Reenalda crop preview, all
prompts, `manifest.md`, `gfx_handoff.md`, `hashes.sha256`, and
`contact_sheets/native_source_result_style_comparison.png`. I also inspected the
canonical role families and contact sheets at
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`
and `.../portraits/commanders/`.

The package contains only sourced real male subjects and portrait evidence. No
female, advisor, `_small`, invented-face, flag, or runtime asset is accepted.

## Independent verdicts

### Douwe Kalma — AGX civic leader

**PASS (visual/source gate).** The result remains identifiable as the supplied
1917 Douwe Kalma source: the direct gaze, narrow facial structure, eye/nose/mouth
placement, swept dark hair, jaw and ears, small dark forehead mark, broad white
collar, patterned tie, dark jacket, shoulder silhouette, and centered pose all
survive the edit. I found no generic-face substitution or demographic drift.
The source-to-result crop is head-and-shoulders and the processed output is
opaque RGBA `156x210`, the leader-family native size. The muted full-color result
has a quiet pale painted background, restrained texture/contrast, and remains
legible at native size; it is not sepia, monochrome, a raw photograph, or UI art.
Civilian 1917 clothing is appropriate to Kalma's civic-leader role.

Source/rights traceability is sufficient for this audit: the manifest preserves
the F.O. Strüppert/Tresoar attribution, Commons file and original-upload links,
and public-domain claim. Keep that provenance with any promotion.

Evidence hashes (SHA-256):

- source master `source_masters/AGX_douwe_kalma_1917.jpg` —
  `38dafcbff7c3a67b6b29b9b637e69ff4c2f9d8caae076361200919a6bb36dbdf`
- raw edit `raw_masters/leader_douwe_kalma_imagegen_2026-07-22.png` —
  `222c7f75bbf24a4167151bb96aa3f256b4f50938f14dc4739de7df6fa2f53238`
- selected processed `processed_png/AGX_friesland_coastal_council.png` —
  `644e37c3ffbcfa871af22bcb6cf9e575cbfa16bdd2cc30b253e2f65c440277a8`
- identity-preserve prompt `prompts/leader_douwe_kalma_identity_preserve.txt` —
  `12c9dde6a4e662d1a0676764ba4f77a024b4b542fd6e12f606b520b2e36d5e0c`

### Pieter Reenalda — AGX coastal commander, candidate02

**PASS (visual/source gate).** Candidate02 preserves the supplied 1919 Pieter
Reenalda identity: broad oval face, deep-set small eyes and gaze, straight nose,
very wide horizontal handlebar moustache, mouth/chin, ears, side-parted hairline,
apparent age, centered head pose, and shoulder placement remain coherent against
the unchanged source. The white high-collared maritime uniform, buttons, shoulder
boards, pocket chain, and visible torso silhouette are retained, with no invented
modern props or role mismatch. At `156x210` the face and moustache still read
clearly; the full-color muted finish, pale quiet background, controlled contrast,
and restrained brush texture match the canonical commander family. There is no
generic/generated-face drift visible in the direct source/raw/native comparison.

Source/rights traceability is sufficient for this audit: the manifest preserves
the Tresoar attribution, unknown-maker note, archive/public-domain basis, exact
source master, and crop evidence. Preserve this rights note before distribution.

Evidence hashes (SHA-256):

- source master `source_masters/AGX_pieter_reenalda_1919_uniform.jpg` —
  `8f93840b12ecdcb313279c6f0fd4027863f8c1c4c9232e699aa7a0a9d46668ce`
- unchanged source crop preview
  `processed_png/AGX_friesland_coastal_commander_source_crop_preview.png` —
  `b1894163b1e94b2ed1b50460fc6e1d840ed5aa0c0616826ddc83a45fdee20bdf`
- selected raw edit (candidate02)
  `raw_masters/commander_pieter_reenalda_imagegen_candidate_02_2026-07-22.png` —
  `eb5d9e6ee35ba6a44ddf9b2e307c42da1b0f5bdaf7df273487350e5c6ad5a8b3`
- selected processed `processed_png/AGX_friesland_coastal_commander.png` —
  `25a3c29b6b9deeda87d0e96699beb44d2d2d7051a5335af61f630cb5d918c968`
- identity-preserve prompt (candidate02)
  `prompts/commander_pieter_reenalda_identity_preserve_candidate_02.txt` —
  `8d70f07674138d46ec2930ca74c2abf76b16a3da15ee51151efe12eaec13ddaa`

### Pieter Reenalda — candidate01

**FAIL-CLOSED / BLOCKED.** Retain only as rejected comparison evidence. Its
eye/cheek proportions and shoulder-board treatment visibly drift from the
unchanged source; it is not an acceptable identity-preserving portrait and must
never be selected or wired.

- raw candidate01 —
  `cdc0c7fb893ee980ec5be0e94cfb8df0aabcf455252c90aee4c62e2cd58ef2d1`
- processed candidate01 —
  `e6e2e20791823f4f21edf5cf295fbfbbde68382619111c2431ab91e093df9647`

## Handoff and metadata boundary

The comparison sheet hash is
`51fc799896d858095da7e0470c188156466bebdf17ad4138b48e062c9d760a33`.
`hashes.sha256` verifies the listed files (its first hash line is UTF-8-BOM;
strip the BOM before comparing the 64 hex characters).

The visual PASSes authorize parent-side conversion review only; this package has
no DDS. Before wiring, correct the producer's stale intended paths in
`manifest.md`/`gfx_handoff.md`: they currently name
`gfx/leaders/AGX_friesland_coastal_...dds`. The authoritative existing texture
paths are
`gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`
and
`gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`.
Do not wire the bare producer paths and do not wire candidate01.
