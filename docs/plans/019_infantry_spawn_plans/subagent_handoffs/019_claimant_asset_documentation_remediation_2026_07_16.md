# Event 019 Claimant Asset Documentation Remediation Handoff

Date: 2026-07-16

> Visual supersession notice: every portrait-binary, output-id, hash, hard-link, contact-sheet, facial/presentation, and human-roster statement below describes rejected pre-army-scene art. The fixed Event 019 slots now show twenty regional claimant armies/musters, six derivative massed hosts, and one neutral unassigned muster with no individual focal human/person. Current visual authority is `019_full_portrait_regeneration_handoff_2026_07_16.md`, `019_neutral_unassigned_muster_asset_handoff_2026_07_16.md`, the current 27-row crosswalk, and the current 27-row reproduction/provenance record. Historical fail-closed claimant-selection, regional-contract, gameplay-name, and male-metadata reasoning remains applicable where it does not describe pixels.

Mode: patch-capable, documentation-only remediation

## Scope and ownership

This tranche remediates the documentation portion of claimant identity specialist findings P2-02, P2-03, and P2-04. It does not edit gameplay script, localisation, GUI, GFX, portrait binaries, the parent audit packet, or the blockers review. It does not create an Event 019 registry file; `interface/019_infantry_spawn.gfx` remains the sole inspected sprite-definition consumer for these portraits.

Skills used: `chaos-redux-event-assets` for generated-asset provenance, source-to-runtime crosswalk, validation, and handoff requirements; `chaos-redux-events` for Event 019 integration boundaries; `chaos-redux-subagents` for bounded ownership and residual-finding reporting.

## Changed files

- `docs/assets/019_infantry_spawn/manifest.md`
- `docs/assets/019_infantry_spawn/gfx_handoff.md`
- `docs/assets/019_infantry_spawn/notes/claimant_identity_metadata.md`
- `docs/assets/019_infantry_spawn/notes/claimant_portrait_asset_crosswalk_2026_07_16.md`
- `docs/assets/019_infantry_spawn/prompts/claimant_portrait_reproduction_specs_2026_07_16.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_possessed_general_matrix.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_claimant_asset_documentation_remediation_2026_07_16.md`

## Remediation delivered

### P2-02 documentation portion

- Removed the matrix instruction requesting a portrait-compatible fallback.
- Replaced it with the actual fail-closed contract: claimant creation stops when no unused region-compatible profile exists, without a global, catch-all, or mismatched portrait.
- Repeated the no-fallback invariant in the identity metadata, manifest, GFX handoff, crosswalk, and reproduction record so profile 20 cannot be reinterpreted as a recovery profile.

Disposition: documentation portion closed. The specialist's separate invalid-context defaults in scripted localisation and the GUI remain outside this documentation-only tranche.

### P2-03

- Added an exact 20-row claimant submanifest crosswalk. Every row records working identity, name pool, runtime region gate, built-in ImageGen source mode, linked prompt/provenance row, source PNG and source dimensions/hash, processed PNG and dimensions/hash, DDS and dimensions/byte length/hash, sprite id, and status.
- Added a linked 20-row reproduction/provenance record with a shared production contract, row-specific prompt direction, exact built-in ImageGen output id, repository source path, and source hash.
- Stated honestly that the reproduction directions are normalized reconstructions from recoverable generation-side descriptions, design records, and the images, not verbatim original prompt submissions.
- Linked both records from the main manifest, GFX handoff, and claimant identity metadata.

Disposition: closed.

### P2-04

- Documented profiles 04 and 12 as Asia/Australasia diaspora-compatible in the source-of-truth matrix, identity metadata, crosswalk, prompt record, manifest, and GFX handoff.
- Documented profile 20 as Australia-only and explicitly prohibited global or cross-region use.
- Recorded the exact live region gates for all 20 profiles in the crosswalk.

Disposition: documentation evidence closed. The current unique profile descriptions are not consumed according to P2-01; if a later P2-01 implementation exposes them, that implementation must align the profile 04 and 12 localisation descriptions with this source-of-truth wording.

## Evidence and validation

- Visually inspected the original-detail source and processed claimant contact sheets. They show 20 distinct one-person portraits, the ten-male/ten-female split, readable retained framing, Asia/Australasia-compatible presentation for profiles 04 and 12, and a distinct Australia-only profile 20.
- Verified all 20 repository source PNGs are hard links to the exact built-in ImageGen output ids recorded in the prompt/provenance table.
- Parsed the new crosswalk and verified 20 rows, 60 existing source/processed/DDS paths, all 60 documented SHA-256 values, stage-local hash uniqueness, all documented source/processed dimensions, and each DDS byte length.
- Reran the retained Event 019 validator against all 20 claimant pairs: every processed PNG and DDS is `156x210`, the DDS is uncompressed 32-bit BGRA, and decoded pixels match exactly.
- Verified exactly one sprite and one numbered texture registration for each of `GFX_portrait_infantry_spawn_claimant_01` through `GFX_portrait_infantry_spawn_claimant_20` in `interface/019_infantry_spawn.gfx`.
- Verified 20 prompt/provenance rows, 20 unique ImageGen output ids, and removal of the obsolete fallback sentence.

## Residual specialist findings

Current residual severity after this documentation tranche, using the claimant identity specialist report's numbering:

| Severity | Count | Residual |
| --- | ---: | --- |
| P0 | 0 | none |
| P1 | 0 | none |
| P2 | 2 | P2-01 runtime consumption of the 20 authored titles/descriptions; non-documentation portion of P2-02 covering invalid-context profile-01/Quartermaster defaults and GUI presentation |

P2-03 is closed. P2-04's documentation proof is closed; its localisation wording becomes a required coordination item only if the currently unconsumed profile descriptions are exposed while closing P2-01.

## Simplifications, omissions, and blockers

No fallback or asset substitution was introduced, and no requested documentation row was omitted. This tranche intentionally does not claim closure of P2-01 or the defensive-selector/GUI portion of P2-02 because those require runtime/localisation/UI ownership outside the granted scope.
