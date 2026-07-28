# Event 006 installed-tag collision audit handoff — 2026-07-28

## Scope

This bounded audit checks Event 006 country, formable, cosmetic, history,
localisation, and flag identifiers against the installed vanilla game,
Workshop directories, embedded archives, sibling local mods, and non-Event
006 Chaos Redux surfaces. It is an evidence pass only; it does not promote a
country package, set a readiness flag, or rename a tag.

## Result

The full report is
`tag_audit/006_installed_tag_collision_audit_2026_07_28.md` with machine-readable
JSON and CSV companions. It scanned 206 registry rows, 102 Event 006 country
tags, seven three-character formable/cosmetic tags, 17 all-length custom
cosmetic identifiers, 122 Workshop directories, eight embedded archives, four
sibling local mods, 7,981 external/vanilla country definitions, and 69,521
external/vanilla extended tag surfaces.

- Reserved-tag collisions: **0**.
- Event 006 custom-cosmetic collisions: **0**.
- Exact or state-word-normalized vanilla identity blockers: **0**.
- Fuzzy identity leads requiring manual review: **16 packages**, recorded in the
  report and existing manual-disposition ledger.
- Collision-free unused `??X` candidates: **444** at the audit snapshot.

The report covers the documented FORM-39 `MFX` identity. The audit script's
curated identity map was missing `MFX`, so the audit previously stopped before
collision results could be produced. Adding `MFX` as `FORM-39 / Melanesian
Federation` fixes audit coverage; it does not change the gameplay registry or
set the MFX reservation, flag-readiness, or identity-review inputs.

## Boundaries

MFX remains `needs_user_review` and FORM-39 remains fail-closed behind the six
writer-dependent research/identity inputs. The zero-collision result therefore
does not admit FORM-39. The 16 fuzzy identity matches remain discovery leads,
not automatic remaps; the four already-blocked distinct-identity packages
remain blocked by their existing manual disposition. Shared `BIA` and `CHU`
carriers remain protected by one reservation group each and are not admitted by
this audit.

## Changed surfaces

- `.tools/audit_hoi4_country_tags.py` — added the documented `MFX` / FORM-39
  identity to the curated three-character formable/cosmetic registry.
- `tag_audit/006_installed_tag_collision_audit_2026_07_28.{md,json}` — full
  audit evidence and input fingerprints.
- `tag_audit/006_installed_tag_collisions_2026_07_28.csv` — empty collision
  table with the report schema.
- `tag_audit/006_installed_custom_cosmetic_collisions_2026_07_28.csv` — empty
  custom-cosmetic collision table.
- `tag_audit/006_vanilla_identity_review_2026_07_28.csv` — current fuzzy identity
  review leads.
- `006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` —
  current audit authority and MFX boundary reconciled.

## Validation

The command used was:

`python -B .tools/audit_hoi4_country_tags.py --write-reports`

It completed against the configured vanilla, Workshop, archive, sibling-mod,
and repository roots with `collisions=0`,
`custom_cosmetic_collisions=0`, `identity_matches=50`, and
`safe_x_tags=444`. No HOI4 process or live runtime was launched.

## Follow-up

Re-run this audit whenever the installed mod set, Event 006 tag registry,
formable/cosmetic registry, or identity manual-disposition ledger changes.
Keep the report and source fingerprints with the corresponding completion
snapshot; do not treat the clean collision tables as proof of package
readiness.
