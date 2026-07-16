# Event 006 rejected portrait evidence cleanup execution

Date: 2026-07-16

Status: completed exact-scope cleanup transaction. This record covers superseded portrait evidence only; it is not an Event 006 completion claim.

## Accepted replacement authority

The deletion gate in `006_rejected_portrait_evidence_cleanup_plan_2026_07_16.md` was opened only after the replacement package and its provenance were independently accepted:

- `docs/assets/006_independence_wave/portrait_regeneration_male_hoi4_2026_07_16/`
- `006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md`
- `006_event6_portrait_frozen_v43_provenance_reaudit_2026_07_16.md`
- `006_event6_portrait_documentation_promotion_2026_07_16.md`
- `006_nwe_flag_only_asset_workflow_cleanup_2026_07_16.md`

The accepted replacement covers all 20 non-exempt large portraits and all 10 matching commander-small portraits. The Rupprecht of Bavaria and Josef Friedrich Matthes DDS files remain protected and unchanged.

## Exact deletion transaction

Before deletion, every target was resolved to an absolute path and verified to be inside `docs/assets/006_independence_wave/`. The complete pre-authorized set contained:

- five rejected portrait-only evidence packages;
- ten rejected portrait subdirectories inside the mixed `generated_nwe` evidence tree; and
- four rejected top-level NWE portrait contact sheets.

The transaction removed exactly 19 targets, 331 files, and 155,622,295 bytes. No wildcard or parent-directory deletion was used. The deleted paths were exactly those listed in the cleanup plan.

## Preservation evidence

Post-delete checks confirmed that none of the 19 paths exists. The following protected surfaces remain present:

- the accepted 2026-07-16 male-HOI4 portrait package;
- NWE source and processed flag directories and both flag contact sheets;
- the Rupprecht and Matthes source, edit, metadata, and review evidence;
- the Debeauvais negative-rights/source record;
- AFX, AJX, RHI/BAY, formable, Low Countries, Mediterranean/Danube, super-event, and other independent non-portrait packages; and
- all 32 runtime DDS portraits in `gfx/leaders/006_independence_wave/`.

Protected runtime SHA-256 values remain:

- `portrait_BAY_rupprecht_of_bavaria.dds`: `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`
- `portrait_RHI_josef_friedrich_matthes.dds`: `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`

## Non-recreation and authority checks

The corrected NWE builder was run with `--scope flags` after deletion. It rebuilt and validated only the ACX, AFX, AGX, and AJX historical ImageGen flag triplets and did not recreate any deleted portrait directory or contact sheet. Its ledger contains 47 existing, hash-matching flag rows and zero portrait or `gfx/leaders` rows. AEX remains deliberately outside the standalone flag scope.

The old-authority reference scan found no active manifest, source-of-truth document, builder, ledger, or current package document that depends on a deleted path. Surviving references are bounded historical handoffs with portrait-specific supersession notices, the cleanup records, the flag-only migration handoff, or the unrelated Event 015 tooling-migration history.

The Event 006 custom advisor-icon directory remains absent and no Event 006 custom advisor texture or sprite reference was reintroduced.

## Result

The rejected 2026-07-15 portrait evidence has been removed without changing runtime portrait names, sprite consumers, flags, protected historical portraits, gameplay, localisation, spreadsheets, or unrelated asset packages. Current portrait documentation routes to the accepted 2026-07-16 package and independent audits.

## Simplifications, omissions, and blockers

No cleanup simplification or fallback was used. No blocker remains within this cleanup transaction. ACX and AEX remain readiness-controlled portrait assets and are not promoted to country admission by this cleanup.

## Skills used

- `chaos-redux-event-assets` for evidence classification, preservation boundaries, runtime validation, and flag/portrait workflow separation.
- `chaos-redux-subagents` for bounded audit handoffs and independent review routing.
