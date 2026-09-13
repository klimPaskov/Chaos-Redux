# Event 39 constant declaration repair

Disposition: implemented narrowly; native parser confirmation remains pending with the parent.
The parent accepted the two declarations after reviewing the full consumer inventory and the distinction between explicit specification ranges and the existing shared-bound contract.

## Changed files and backup

- `common/script_constants/039_murder_mystery_constants.txt`: added `murder_mystery_value.minimum = 0` and `murder_mystery_value.maximum = 100`, plus an explanatory comment.
- `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event39_constant_repair/common/script_constants/039_murder_mystery_constants.txt`: exact pre-patch bytes.
- `docs/testing/live_qa/2026-09-04_catalog_01/event39_constant_parser_repair.md`: this handoff.

Before SHA-256: `9faad248e38e88de9fa2b55dfd74b2f02c412a0efd38a1f512a23b1c6202c4ee`.
After SHA-256: `d6e7316f59402e81d151c151f7a7ab343a7e121ea3d208744f77d0fcd0d653fe`.
Removing the inserted comment and declarations reproduces the exact backup bytes.
The source was untracked before this patch, so the backup, rather than Git HEAD, is the reliable baseline.

No existing constant values, consumer expressions, AI weights, phases, helpers, lifecycle state, event targets, cleanup behavior, localisation, assets, or other gameplay files changed.
No helper extraction or migration was required.
No game launch or commit was performed.

## Diagnosis and value evidence

The parent-provided `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_09/logs/error.log` contains 55 missing-value errors for each bound.
Both keys were absent from the category; this was not a duplicate-category collision or an invalid schema declaration.
All 48 category names in the owned file occur once across the current mod constant registry.
The declaration parser found no duplicate member keys, every category starts with its schema, and the repaired file contains 636 data entries.

The explicit range evidence is `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_1_core.md:43`, `:58`, and `:76`: Case Progress, Network Reach, and Brotherhood Cohesion each use 0 to 100.
`docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_5_international_network.md:82` explicitly assigns Local Case Progress the same range.
Existing `common/scripted_effects/039_murder_mystery_focus_effects.txt:76` and `:77` already clamp Network Reach and Case Progress with the declared `zero` and `hundred` entries.
Those existing entries are 0 and 100 and remain unchanged.

The hidden support and cell scores are not individually assigned numerical ranges in the inspected specification paragraphs.
Their range follows from the existing source contract: they already share the exact same minimum/maximum keys as the explicitly bounded public scores in paired validation and clamping helpers.
They initialize at zero and use integer point deltas; the shared keys do not serve counts, ratios, durations, stages, roles, identifiers, or registry indices.
This inference was explicitly reported to and accepted by the parent before applying the patch.

Vanilla `documentation/script_concept_documentation.md:216` and `common/script_constants/documentation.md` document category schemas and scoped `constant:` consumption.
The former explicitly excludes use of script constants inside other script constant files, so numeric declarations were used rather than unsupported references to `zero` and `hundred`.
Vanilla `documentation/effects_documentation.md:2695` documents the variable-valued clamp bounds; `documentation/triggers_documentation.md:2110` documents variable comparisons.
Installed vanilla `common/script_constants/special_project_constants.txt` and `propaganda_campaigns.txt` were consulted as schema precedents.

## Complete exact-token consumer inventory

There are 34 minimum references and 34 maximum references in two files.
Suffixes such as `maximum_action`, `maximum_target_role`, and `maximum_cell_role` are different keys and were excluded by an exact-token search.

Each country score below has one clamp in `common/scripted_effects/039_murder_mystery_runtime_effects.txt` and one paired lower/upper validation in `common/scripted_triggers/039_murder_mystery_runtime_triggers.txt`.
All variable names in this table carry the `murder_mystery_` prefix.

| Meaning and variable suffix | Effect clamp line | Trigger lower / upper lines |
| --- | --- | --- |
| Public case progress: `case_progress` | 211 | 57 / 58 |
| Public network reach: `network_reach` | 212 | 59 / 60 |
| Public cohesion: `brotherhood_cohesion` | 213 | 61 / 62 |
| Evidence quality: `evidence_integrity` | 214 | 67 / 68 |
| Witness protection: `witness_safety` | 215 | 69 / 70 |
| Investigator exposure: `investigator_exposure` | 216 | 71 / 72 |
| Killer adaptation: `killer_adaptation` | 217 | 73 / 74 |
| Cell maturity: `cell_maturity` | 218 | 75 / 76 |
| Route security: `route_security` | 219 | 77 / 78 |
| False evidence: `counterfeit_evidence` | 220 | 79 / 80 |
| Succession strain: `succession_strain` | 221 | 81 / 82 |
| Government weakness: `local_government_weakness` | 222 | 83 / 84 |
| Target vulnerability: `target_vulnerability` | 223 | 85 / 86 |

The remaining eight reference pairs are in the same runtime effects file.

| Cell score | Registration lower / upper lines | Row-update clamp line and array |
| --- | --- | --- |
| `murder_mystery_cell_registration_maturity` | 977 / 978 | 1117: `global.murder_mystery_cell_maturity_entries` |
| `murder_mystery_cell_registration_local_case` | 979 / 980 | 1129: `global.murder_mystery_cell_local_case_entries` |
| `murder_mystery_cell_registration_exposure` | 981 / 982 | 1133: `global.murder_mystery_cell_exposure_entries` |
| `murder_mystery_cell_registration_inherited_evidence` | 985 / 986 | 1137: `global.murder_mystery_cell_inherited_evidence_entries` |

The row-update clamps use `murder_mystery_cell_row_value`, loaded from and returned to the listed array around each clamp.
Adjacent stage, role, revolt-readiness, generation, and array-count fields use other keys; they do not share the repaired bounds.

## Meaningful validation and limits

Source validation resolved every one of the 68 exact bound references against the repaired registry.
A recursive declaration parse checked category nesting, schema placement, member uniqueness, and existing-member preservation.
This is source evidence and does not prove the native game parser loaded the repaired declarations.
Native parser confirmation remains the parent's task.

The mandatory narrow event inspection used `chaosx.nr39.1`, depth 1, three nodes, and three edges.
It returned `EVENT_INSPECTED_PARTIAL`, revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`.
The event render returned `EVENT_RENDERED_PARTIAL` with the same revision.
Both explicitly reported deferred workspace-wide helper projections and lifecycle passes, with `validation.passed = false`.
They are limited event-chain evidence, not a constants-parser certification.
The post-change `hoi4.event_compare` request used the captured inspection revision as its baseline and returned `EVENT_REVISION_NOT_CACHED` with `validation.passed = false`.
The exact blocker is "Requested event graph revision is not cached".
No graph-equivalence claim is made from that failed comparison.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd6149587794662fddf1ac35c56822c77faca9efbf219a0bfd66c85d4da1caa2/ab5ce0f1257bb632d88a6dbdff5cc62ed5eba42bcf86ae8349c946e1a9124d59/event-scan-1102e50fad94.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bad839a4f52e6aa8e8d26e7097e0308c2c977fc72cbe9684726f544a36f50139/6f4d78c770a569fb8b6b2d02235e958e7181eede9509bcb5ea7059e5909168d0/event-neighborhood-1102e50fad94-manifest.json`.

## Simplifications, omissions, and blockers

No simplification was introduced in this declaration repair.
The Event 39 parser-error family is not fully resolved: five shared Chaos history-reason keys remain absent.
Each appears twice in the provided launch archive:

- `chaos_meter_history_reason.special.murder_mystery_entry`, consumer `039_murder_mystery_integration_effects.txt:387`.
- `chaos_meter_history_reason.special.murder_mystery_reversal`, consumer line 1036.
- `chaos_meter_history_reason.special.murder_mystery_network`, consumer line 1675.
- `chaos_meter_history_reason.special.murder_mystery_world_end`, consumer line 1924.
- `chaos_meter_history_reason.special.murder_mystery_defeat`, consumer line 1941.

The canonical shared category is in `common/script_constants/chaos_meter_constants.txt:43`.
It has no corresponding Event 39 definitions; no proven existing numeric IDs or declaration typos were found within this repair's ownership.
That registry is outside the owned `039*` constants surface, so assigning IDs or editing the consumers would exceed this repair and risk changing history meaning.
No missing IDs were invented.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or changed.
