# Decision startup parser repair handoff

Status: checkpoint partial. The first atomic source edit is complete; the remaining bounded parser fixes are held for the next fresh-log review at the parent agent's request.

## Changed source

- `common/decisions/021_random_civil_war_decisions.txt`
  - Replaced invalid resource trigger keys `army_experience` and `political_power` with the documented `has_army_experience` and `has_political_power` forms at the existing gates.
  - Replaced invalid `add_army_experience` effect keys with the documented `army_experience` effect key at the loyalty, integration, and disarmament decisions.
  - Comparisons and constant-backed values are unchanged.

The file remains untracked in the shared worktree, so its source-to-backup comparison is recorded against `pre_patch_decisions/common/decisions/021_random_civil_war_decisions.txt`. The backup SHA-256 is `9DE76FF9027EA2A4F01DAEDB0AEFA02BEA671AC49215B6905EEBA7312038886C`; the edited source SHA-256 is `A26F67E5CEEB80EB5BF26B431C0A51D86A26A0C93B82C77B52044B2D09A19E14`.

## Backup inventory

Originals were copied before inspection or editing under `pre_patch_decisions/` for the following planned decision files: `common/decisions/021_random_civil_war_decisions.txt`, `common/decisions/028_asteroid_incoming_decisions.txt`, `common/decisions/031_random_terror_decisions.txt`, `common/decisions/032_missiles_decisions.txt`, `common/decisions/035_great_depression_decisions.txt`, `common/decisions/categories/035_great_depression_categories.txt`, and `common/decisions/039_murder_mystery_decisions.txt`. The backups for files other than `021_random_civil_war_decisions.txt` are unchanged references; no source edits were made to those files in this checkpoint.

## Deferred bounded fixes

- `common/decisions/028_asteroid_incoming_decisions.txt`: replace the unsupported modifier-field constant with a file-local `@` value retaining `1`, change two invalid `has_command_power` keys to `command_power`, and change three invalid `state_target = any_state` values to documented `any`.
- `common/decisions/031_random_terror_decisions.txt`: replace three invalid `set_timed_country_flag` blocks with `set_country_flag` blocks retaining the existing flag names and durations, change invalid army-experience effect keys, change invalid `is_same_country` checks to `tag = ROOT`, and change three invalid political-power checks to `has_political_power`.
- `common/decisions/032_missiles_decisions.txt`: change the invalid `has_command_power` and `add_air_experience` keys while preserving the concurrent icon edits and all values.
- `common/decisions/035_great_depression_decisions.txt`: replace the unsupported `ai_hint_pp_cost` constant token with a file-local value retaining `25`.
- `common/decisions/categories/035_great_depression_categories.txt`: remove the invalid category `desc` field.
- `common/decisions/039_murder_mystery_decisions.txt`: replace the unsupported divisions threshold constant token with a file-local value retaining `2`.
- Event 025 category registration is held. Its missing category IDs and existing scripted-GUI linkage need the parent review because the read-only GUI inspection found unresolved button references, missing fonts, and missing localisation, while the baseline GUI render timed out after 180 seconds.

Event 029 remains a follow-up because its repeated constant and trigger issues exceed the current tranche checkpoint. Event 026 has no decision source file in `common/decisions`; its reported issue is in ideas and is outside this decision-only ownership.

## Evidence and limits

The focused read-only `hoi4.event_inspect` query for `chaosx.nr21.1` returned `EVENT_INSPECTED_PARTIAL` with artifact SHA-256 `71bd20d65bab4892b622ac5726033d86c51e12f82ca44a01d111c11dd626cf91`. The MCP response reported `MCP_INLINE_FILES_TRUNCATED` and deferred workspace-wide helper and lifecycle projections, so it is evidence of event linkage only and not a replacement for decision parser validation.

Offline decision and trigger documentation, vanilla decision examples, and the archived launch log were consulted before the alias choices. A targeted source scan confirms that the edited `021` file no longer contains the reported raw `army_experience`, `political_power`, or `add_army_experience` parser forms. No game process or live-game validation was run.

No weights, thresholds, timers, effects values, mission nesting, protected event files, or parent-owned scripted effects were changed in this checkpoint. No plan document was written because this handoff is the requested root QA handoff and the remaining work is explicitly queued for parent routing.

Parent relocated the handoff and backup directory into the actual run folder after verifying both resolved destinations stay within the workspace.
