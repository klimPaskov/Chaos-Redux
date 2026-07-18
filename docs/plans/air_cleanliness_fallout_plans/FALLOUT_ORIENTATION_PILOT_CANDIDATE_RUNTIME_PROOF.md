# Fallout Orientation Pilot Candidate Runtime Proof

Date: 2026-07-18

Status: dormant identity mapping implemented, installation blocked

## Engine references

The implementation was checked against the offline Data Structures, Scopes, Triggers, Effects, and Event Modding wiki pages. Vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and the script-constants documentation were also reviewed. Vanilla event arrays and existing Chaos Redux fixed-slot transaction rows were used as precedents.

The final design uses country-owned fixed slots rather than a global array. Every pilot defines exactly three candidate identities, while the installed package may authenticate two or three. This matches the existing orientation transaction and avoids a new world iterator.

## Typed identity

`fallout_orientation_candidate_id` reserves ids 1 through 36 in the manually reviewed source order. The ids map to twenty-four fictional characters and twelve fictional institutions. Script constants carry every tuning-independent identity.

The mapping row stores:

- schema version
- transition generation
- exact country-memory id
- exact live region
- exact government archetype
- candidate count
- three candidate ids
- three candidate types
- each candidate's region and archetype

The validator compares every field with the current successor assignment row. It also checks one of twelve exact memory, region, archetype, and candidate-id combinations.

## Idempotence and failure

`fallout_orientation_prepare_candidate_mapping` accepts an already current row without rewriting it. A stale or partial row is cleared before one deterministic rebuild. Unsupported memory, identity mismatch, invalid payload, and missing allocation have separate diagnostics.

The mapper has no world iterator and no caller. A stale mapping cannot become usable because generation and successor-assignment proof are required on every access.

## Package separation

The identity mapping does not prove that portraits, icons, localisation, or install effects exist. A separate package receipt must authenticate:

- current schema and generation
- exact country memory
- two or three installed candidates
- exact ids and candidate types

A two-candidate package writes an explicit empty third slot. A three-candidate package must match the mapped institution. The request loader idempotently prepares the identity mapping, clears all temporary slots, then copies only the authenticated installed package. The character-component entry point always uses this loader. This prevents stale temporary candidate data from entering a transaction.

No gameplay file sets `fallout_orientation_candidate_package_installed`. No gameplay file approves `fallout_orientation_character_install_surface_status`. The candidate request therefore remains unreachable.

## Transaction authentication

The begin trigger now compares requested candidate ids, types, regions, and archetypes with the current mapped row and package receipt. The transaction freezes explicit zero values for non-character components. A character transaction freezes two or three candidates, and result eligibility rejects an invalid frozen registry. The regional-institution branch is unavailable when the third slot is empty.

## Inspection boundary

The narrow helper-expanded event inspection for `chaosx.fallout.62` reached the tool's fixed 200000-node projection ceiling and returned `EVENT_HELPER_PROJECTION_LIMIT`. Hearts of Iron IV was not run, as requested. Static inspection confirms that no caller, package setter, installation approval setter, event id, or scheduler activation was added in this tranche.
