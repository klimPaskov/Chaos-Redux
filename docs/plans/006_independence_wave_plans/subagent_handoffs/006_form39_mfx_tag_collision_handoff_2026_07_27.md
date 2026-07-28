# Event 006 FORM-39 MFX tag and identity handoff

Date: 2026-07-27

Status: **candidate reserved; runtime admission remains fail-closed**

## Decision

FORM-39 Melanesian Federation uses cosmetic/formable identity `MFX`. The
identifier ends in `X`, is not a vanilla country tag, and was selected from the
unused Event 006 candidate pool after the installed-mod collision audit.
Vanilla `FIJ`, `PNG`, and `WPG` remain the researched member carriers; no new
country history shell is created for those existing countries.

## Collision evidence

The superseding installed-mod audit in
`tag_audit/006_installed_tag_collision_audit_2026_07_28.md` scanned 122
Workshop directories, eight embedded archives, four sibling local mods,
vanilla/external definitions, and Chaos Redux definitions. It reports zero
reserved/custom-tag collisions, zero custom-cosmetic collisions, and 444
unused `??X` candidates at the current snapshot. `MFX` is covered by the
curated identity map and has no scanned collision. The candidate must still be
rechecked if the installed mod set or registry changes.

## Asset evidence

The flat ImageGen flag package is in
`docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/`.
It contains the source PNG, normal/medium/small processed PNGs, DDS files,
runtime TGA candidates, prompt, review sheet, and manifests. The package is
marked `needs_user_review`; the runtime TGAs in `gfx/flags/` are not a readiness
fallback and must not be treated as final admission without the independent
flag review.

## Gameplay binding

`common/scripted_triggers/006_independence_wave_form39_triggers.txt` owns the
exact FIJ/PNG/WPG member and anchor map, research flags, MFX reservation gate,
three-member founding ledger, consent checks, staged integration, and cleanup
proofs. `common/scripted_effects/006_independence_wave_form39_effects.txt`
owns identity setup, autonomous member relations, project ledgers, integration,
rollback, and dissolution cleanup. The readiness flags
`independence_wave_form39_x_tag_reserved`,
`independence_wave_form39_flag_package_ready`, and
`independence_wave_form39_identity_review_complete` intentionally remain
unset until the research and review decisions are accepted.

## Remaining acceptance

1. Re-run the collision audit if external mods or the accepted tag registry
   change.
2. Complete the sensitive IW-157 West Papuan and IW-178 Papuan source and
   identity packages, including their named-community distinctions.
3. Accept the circa-1940s FIJ Sukuna portrait against the 1936 baseline, or
   record a source/date disposition that preserves the package gate.
4. Independently review the MFX flat flag and then set the three explicit
   FORM-39 attestation flags through a researched, review-owned setup path.
5. Run the country-package, decision/mission, localisation, allocator, and
   whole-event completion audits before any readiness promotion.

No advisor icon or advisor portrait asset is part of this handoff.
