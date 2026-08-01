# Event 006 leader/commander reference-library audit

## Scope

Audited only the user-requested skill-local reference pack and its routing surfaces:

- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/`
- `.agents/skills/chaos-redux-event-assets/assets/README.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md` reference-library routing

No gameplay, `.gfx`, localisation, advisor-card, or runtime asset files were changed.

## Findings

- The pack contains 6 country-leader PNGs and 9 army/navy-commander PNGs, all visually male-presenting and all native `156x210` RGBA portraits.
- Every pack portrait is byte-identical to its mapped canonical file under `assets/vanilla_reference/portraits/`; the manifest SHA-256 values match the actual pack and canonical bytes for all 15 rows.
- The CATALOG-mapped Vanilla HOI4 DDS sources exist in the installed game for every pack row, and each catalog row is marked `Vanilla HOI4`; Pillow decoded all 15 DDS files to `156x210` pixels identical to the canonical PNGs.
- `leaders/contact_sheet.png` is `660x560` RGB with SHA-256 `19320E58B96B1A5C2766392D5F332C1F56E8A3720AA0A47FA5970971B6B6A79E`; it displays the six manifest leader files and its manifest evidence matches.
- `commanders/contact_sheet.png` is `660x840` RGB with SHA-256 `86C9A2D6C66CC6A7274D41327C424CB733BBCDAF31F38F155DAB9BD30A209D90`; it displays the nine manifest commander files and its manifest evidence matches.
- The pack has no advisor/high-command/officer-corps/army-small/operative files, no DDS files, and no runtime or `.gfx` references. Its README and manifest explicitly keep those families in their separate canonical folders.
- `assets/README.md` and the event-assets skill routing agree on the nested `leader_portraits/leaders/` and `leader_portraits/commanders/` paths, two contact sheets, reference-only status, and canonical-library ownership. All referenced files exist.

## Changes

No semantic documentation or skill patch was necessary: the scoped README, manifest, contact-sheet evidence, and routing text are internally consistent with the audited files. The touched README lines were only reflowed to keep each sentence on one physical line; the existing working-tree change to `assets/README.md` is preserved, and unrelated worktree changes were not touched.

## Validation evidence

The audit used Pillow to verify image dimensions/modes, SHA-256 and byte equality checks against the canonical library, a CATALOG-to-installed-vanilla source existence check, and visual inspection of both labeled contact sheets. The pack remains review-only and must not be wired as runtime art.

## Handoff

Parent agent may include the 15 untracked pack files and the existing `assets/README.md` edit in the Event 006 change. No simplifications or blockers were introduced by this audit.
