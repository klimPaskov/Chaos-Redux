# Event 065 Trait Registry Schema

## Registry purpose

The registry is the authoritative bridge between the current loaded country-leader trait sources and Event 65 runtime selection.

It prevents manual omissions, accidental duplicate weights, stale DLC coverage, and raw-key report output.

## Required source files

Recommended tool files:

- `.tools/generate_random_trait_registry.py`
- `.tools/data/065_random_trait_featured_overrides.csv`
- `.tools/data/065_random_trait_registry_index_history.csv`

Recommended generated runtime files:

- `common/scripted_effects/065_random_trait_pool_generated.txt`
- `common/scripted_localisation/065_random_trait_names_generated.txt`
- `common/script_constants/065_random_trait_generated_constants.txt`

Recommended permanent documentation outputs:

- `docs/events/065_random_trait/trait_registry.csv`
- `docs/events/065_random_trait/trait_registry_summary.md`
- `docs/events/065_random_trait/trait_registry_exclusions.md`
- `docs/events/065_random_trait/trait_registry_overrides.md`

The implementation agent may adjust paths to match existing repository generator conventions.

The same ownership and validation contract must remain.

## Canonical registry columns

| Column | Type | Required | Meaning |
| --- | --- | --- | --- |
| `registry_index` | integer | yes | Stable append-only Event 65 index |
| `source_trait_id` | token | yes | Final source trait ID passed to the native effect |
| `source_family` | enum | yes | Country leader, advisor, theorist, high command, manufacturer, or other database role |
| `source_origin` | enum | yes | Vanilla or Chaos Redux |
| `source_file` | path | yes | Final definition file |
| `source_root` | path label | yes | Inspected source root |
| `definition_hash` | SHA-256 | yes | Hash of normalized final trait definition |
| `load_order_winner` | text | yes | Final owner after override resolution |
| `overridden_sources` | list | no | Earlier definitions with the same ID |
| `content_gate` | token | no | Verified DLC or content condition |
| `loaded_in_profile` | map | yes | Availability across declared test profiles |
| `name_loc_key` | token | no | Source display-name key |
| `name_loc_status` | enum | yes | Present, fallback required, or blocked |
| `description_loc_key` | token | no | Source description key |
| `description_loc_status` | enum | yes | Present, missing, or not used |
| `presentation_status` | enum | yes | Normal, hidden, empty, or unusual |
| `featured` | boolean | yes | Final non-stacking featured classification |
| `featured_reasons` | list | no | Powerful, unusual, severe, beneficial, harmful, bizarre, extreme, rare, narrow route, unique character, or Chaos Redux |
| `classification_source` | enum | yes | Default, source-origin rule, reviewed override, or accepted heuristic |
| `weight_baseline` | integer | yes | `100` |
| `weight_evolution_1` | integer | yes | `100` |
| `weight_evolution_2` | integer | yes | `100` or `125` |
| `weight_evolution_3` | integer | yes | `100` or `150` |
| `runtime_included` | boolean | yes | Final runtime inclusion |
| `technical_exclusion_reason` | text | no | Evidence-backed reason when excluded |
| `technical_exclusion_evidence` | path or artifact | no | Inspection, log, or test proof |
| `generated_group` | integer | no | Dispatcher group when hierarchical selection is used |
| `legacy_index` | integer | no | Prior index used during migration |
| `notes` | text | no | Review notes |

## Stable index rules

1. A source trait keeps its registry index across ordinary regenerations.
2. New traits append new indexes.
3. Removed traits keep a retired index record.
4. A retired index is never assigned to a different source trait inside the same registry major version.
5. Renaming a source trait requires an explicit migration entry.
6. An override that keeps the same trait ID keeps the same registry index and updates the definition hash.
7. The runtime name selector and report data use the stable index.
8. The source trait ID remains the real gameplay identity.

## Featured override columns

| Column | Meaning |
| --- | --- |
| `source_trait_id` | Trait to classify |
| `featured` | `yes` or `no` |
| `reason_tags` | One or more accepted reason tags |
| `review_note` | Short evidence for the classification |
| `reviewed_by` | Reviewer or process |
| `review_date` | Date |
| `source_version` | Game or mod version reviewed |

An override row for a missing trait is a validation error.

Several reason tags do not stack weight.

## Generator inputs

The generator accepts:

- vanilla install root
- Chaos Redux repository root
- declared content profile
- prior index history
- featured override file
- optional output root
- check-only mode
- verbose discovery mode

The generator should support Windows paths used by the repository workflow.

It should normalize line endings and comments before computing definition hashes.

## Generator outputs

### Runtime pool

The runtime output provides:

- one selectable entry per included source trait
- stage-specific weights
- exact source effect
- collision test hook
- grant ledger hook
- registry index storage
- origin and featured counters
- group totals when a hierarchy is used

### Name selector

The generated scripted localisation maps each registry index to:

- source localized name when valid
- Event 65 fallback key when the source name is missing

A missing selector branch is a validation error.

### Generated constants

Generated constants may include:

- active pool count
- ordinary count
- featured count
- vanilla count
- Chaos Redux count
- registry major version
- registry minor version
- registry checksum fragments
- group totals for each stage

No hand-edited gameplay tuning belongs in a generated constants file.

The `100`, `125`, and `150` tuning anchors should remain in an event-owned manual constants file.

## Check mode

The command returns nonzero when:

- source discovery differs from committed registry
- generated runtime output differs
- a source ID is duplicated
- an included source has no runtime branch
- a runtime branch has no manifest row
- a registry index maps to several source IDs
- a source ID maps to several active indexes
- a retired index was reused
- a featured override is stale
- a source definition hash changed without regeneration
- a content profile has an unexplained missing entry
- a technical exclusion lacks evidence
- weight totals are incorrect
- generated name selectors are incomplete
- output files contain unstable ordering

## Summary report

The summary should include:

- source roots
- game version
- mod commit
- generation date
- active content profile
- total discovered IDs
- total final loaded IDs
- total runtime-included IDs
- total technical exclusions
- ordinary and featured counts
- vanilla and Chaos Redux counts
- content-gated counts
- override count
- missing localisation count
- generated group count
- runtime output hash
- registry hash

## Validation standard

A registry is acceptable only when every final loaded source trait is either runtime included or appears in the explicit technical exclusion report with evidence.

The existence of an exclusion report does not make a broad exclusion acceptable.

A large exclusion set requires user review.
