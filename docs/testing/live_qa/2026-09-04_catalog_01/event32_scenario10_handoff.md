# Event 32 scenario parser repair handoff

Date: 2026-09-05.
Disposition: implemented source corrections, with engine parser acceptance unresolved.
Acceptance basis: the parent delegated the eleven enumerated parser corrections under the user's safe bug-fix authorization and retained operations-file and broader gameplay ownership.

## Changed files and exact scope

- `common/scripted_effects/032_missiles_scenario_effects.txt`: nine token or syntax corrections at unchanged source lines 283, 287, 316, 483, 496, 501, 526, 629, and 682.
- `common/scripted_effects/032_missiles_effects.txt`: two `limit` wrappers at unchanged source lines 944 and 948.
- `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event32_scenario10/`: exact immediate pre-edit bytes for both files.
- `event32_scenario10_source_checks.json`: exact replacement manifest, occurrence counts, byte sizes, before/after SHA-256 hashes, and inverse verification result.
- `event32_scenario10_mcp.json`: read-only before/after trace, neighborhood render, and compare responses.

No source outside the two assigned files was changed by this subtask.
No launch, staging, or commit was performed.

## Repair map and preserved contracts

| Existing helper | Scope and existing inputs | Correction and resulting behavior | Existing outputs and side effects |
| --- | --- | --- | --- |
| `missiles_scenario_freeze_candidate_arrays` | Orchestrator with nested country iteration, scenario profile | `is_at_war` becomes documented `has_war`, and two `has_global_event_target` checks become `has_event_target` | Preserves the priority arrays, war-anchor target name, war-pair flag, and deterministic selection structure |
| `missiles_scenario_seed_command_breakdown` | Country, nested selected site state, global intensity and incident cap | Adds `var =` to two malformed long-form checks and reads `global.missiles_scenario_command_damage` directly | Preserves all damage values, incident thresholds, compromise flags, helper calls, and existing command-seeded guard |
| `missiles_scenario_seed_retaliation_warning` | Country, global warning seed count | Adds `var =` to the malformed positive-count gate | Preserves the warning receipt and root lifecycle |
| `missiles_scenario_apply_country_package` | Country, global intensity | Adds `var =` to the malformed intensity gate | Preserves the existing warning-pressure assignment |
| `missiles_scenario_finish_transaction` | Orchestrator with global warning root | Replaces the unsupported global-target check with `has_event_target` | Preserves root closure conditions, targets, flags, and cleanup statements |
| `missiles_reinforce_one_site` | State, existing site hardening/security | Places each existing less-than-maximum check inside its own `else_if.limit` | Preserves the recovery, capacity, hardening, security order and both existing gains |

All helper identifiers and direct callers are unchanged.
The core helper's existing caller remains `missiles_reinforce_network_from_firing` at line 975.
No helper extraction, new helper, defaults, tuning constants, lifecycle cleanup, event target, event option, localisation, asset, or probability-bearing logic was authored.
The helper contract documentation for this parser correction is the map above.
No migration or new tuning table is needed because every existing constant token remains byte-identical and in the same order.

## Evidence for the corrections

The parent-supplied `event32_helper_parser_analysis.md` identifies each exact defect and was reviewed before editing.
The supplied launch 09 log confirms `is_at_war` and `has_global_event_target` failures, malformed long-form checks, and the invalid `ROOT.global.missiles_scenario_command_damage` reference at log lines 1671–1691.
The same log reports the two invalid effect-position `check_variable` clauses at lines 1387 and 1389, and the warning-root target check later in the scenario error block.

Installed vanilla `documentation/triggers_documentation.md:3844` explicitly says that `has_event_target` checks the current or global scope for the saved target.
The same file documents `has_war` at line 5024 and the required `var`, `value`, and `compare` long form at line 2110.
Installed vanilla `documentation/effects_documentation.md` documents conditional `if` and global target storage.
Vanilla `common/scripted_effects/00_scripted_effects.txt:653` supplies a direct `else_if = { limit = { ... } effects... }` precedent.
Vanilla `AUS_scripted_effects.txt:123` uses a directly prefixed `global` variable reference, and `INS_scripted_effects.txt:1482` uses `has_event_target`.

Offline `Data structures - Hearts of Iron 4 Wiki.md` describes global target lookup and the `global.var_name` variable namespace.
Offline `Scopes - Hearts of Iron 4 Wiki.md` documents the `else_if` trigger limit and effect body.
The source initializes `global.missiles_scenario_command_damage` for every intensity branch at scenario lines 20, 34, 49, and 63, proving the intended read target at line 496.
The comment above `missiles_reinforce_one_site` explicitly states recovery, capacity, hardening, then security, matching the repaired branch guards.
The required core offline pages, vanilla script constants documentation, existing shared dynamic helper source/docs, and the events/subagents skills were consulted.

## Validation and limits

Reconstructing both post-edit files from the immediate backups using only the approved replacement list produced exact byte matches.
An independent diff-opcode inverse reconstructed each complete pre-edit byte stream.
All constant references retained their original sequence, and every `clear_temp_variable` and `clear_event_target` line remained byte-identical.
Review of the immediate-backup diff confirmed nine scenario changes and two single-line wrappers, with no added or removed lines.

The before and after `hoi4.event_inspect` calls used event `chaosx.nr32.1`, depth 2, node limit 25, edge limit 40, helper expansion enabled, and refresh enabled.
Both returned `EVENT_INSPECTED_PARTIAL` at revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8` and graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e`.
Their validation explicitly failed because large-workspace analysis deferred helper projections and lifecycle passes, with `helpers = 0` despite expansion being requested.
The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fd56917a2afb387be1747dadd32bf37eaf283cbe77f0fbb50b9b718161c555c/f9fc73a0b36a67a84e14c1493768f6fa6d414074d21ae9c227ac679050136718/event-trace-1102e50fad94.json`.
The neighborhood render also returned `EVENT_RENDERED_PARTIAL`, with its exact JSON, SVG, PNG, and manifest artifact references retained in the MCP evidence file.
The unchanged MCP revision cannot establish successful parsing or helper registration for these changed scripted-effects files.
The `hoi4.event_compare` request against the recorded before/after revision failed with `EVENT_REVISION_NOT_CACHED` and produced no comparison artifact.
No in-game test or fresh engine parser run was performed in this subtask, as the parent explicitly prohibited launching.

## Simplifications, omissions, and blockers

No simplifications were made to the eleven requested corrections.
The known unsupported `clear_temp_variable` family and `clear_event_target = missiles_scenario_warning_recipient` remain unchanged by explicit parent instruction, pending separate lifetime review.
The operations-file missing brace and helper-registration cascade remain parent-owned, and this subtask adds no replacement helpers for them.
The source correction is complete, but helper-aware MCP acceptance and fresh engine parser acceptance remain unresolved.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or updated.
