# Event 006 Scripted System Audit Handoff

## Scope

Audited the Event 006 package/ledger hardening tranche after parent edits, limited to the allowed Event 006 event, constants, effects, triggers, docs, and this handoff.

References consulted:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding
- Vanilla documentation for script constants, effects, and triggers
- Existing dynamic helper docs in `common/scripted_effects/chaosx_dynamic_effects.md`

## Files Changed

- `events/006_independence_wave.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_independence_wave_scripted_system_audit_handoff.md`

`common/scripted_triggers/006_independence_wave_triggers.txt` was audited but not changed.

## Identifiers Changed

- Added script constant category `independence_wave_resolver`.
- Added constants:
  - `independence_wave_resolver.release_truce_days`
  - `independence_wave_resolver.host_survival_state_floor`
  - `independence_wave_resolver.host_stability_weakness_gate`
  - `independence_wave_resolver.host_war_support_weakness_gate`
  - `independence_wave_resolver.host_surrender_weakness_gate`
- Updated `independence_wave_prepare_release_count`.
- Updated `independence_wave_mark_host_aftermath`.
- Updated `independence_wave_setup_released_country`.
- Updated `chaosx.nr6.1` immediate resolver.

## Behavior Before

- `independence_wave_prepare_release_count` cleared `global.independence_wave_candidate_pool`, `global.independence_wave_released_countries`, and `global.independence_wave_compact_members` every time repeatable Event 006 fired.
- Host/breakaway recent timed flags used file-local `@` constants despite matching script constants existing under `independence_wave_decision`.
- Resolver host weakness and truce tuning used file-local `@` constants in `events/006_independence_wave.txt`.
- Event docs did not spell out which ledgers are per-run and which are persistent.

## Behavior After

- `independence_wave_prepare_release_count` clears only `global.independence_wave_candidate_pool` and resets `global.independence_wave_actual_release_count`.
- `global.independence_wave_released_countries` persists as the compact delegate target ledger for Event 006 releases.
- `global.independence_wave_compact_members` persists as the member arbitration target ledger.
- Host and breakaway timed flags now load script constants into temp variables before passing them to `days =`.
- Resolver truce duration now loads `constant:independence_wave_resolver.release_truce_days` into `independence_wave_release_truce_days` before `set_truce`.
- Host survival and weakness gates now read from `independence_wave_resolver`.
- Event docs now state the candidate pool is per-run, while released-country and compact-member arrays are persistent ledgers.
- Event docs now state the package-family system is still a framework; `game_rule` and `railway` constants are reserved and are not completed country-package paths.

## Audit Findings

1. Script constant and duration fields:
   - No `days = constant:` remains in the audited allowed files.
   - No `days = @...` remains in the audited allowed files.
   - Timed country flags use temp variables fed from script constants.
   - `random_select_amount` still uses `@independence_wave_candidate_scan_cap`; vanilla docs show this field as a literal integer and do not document script-constant support, so I did not inject a script constant there.

2. Candidate pools and Event 005 separation:
   - Candidate pool triggers exclude Soviet Collapse origin/republic flags.
   - Event 006 release setup sets `chaosx_release_origin_independence_wave` and does not set Soviet Collapse release flags.
   - Candidate pool dedupe uses `NOT = { is_in_array = { array = global.independence_wave_candidate_pool value = THIS } }` before each pool add.

3. Scope safety:
   - Candidate scan scope flow is consistent: `for_each_scope_loop` sets candidate scope, `random_country` scopes to the host, and `PREV.PREV` inside host-owned state checks points back to the candidate.
   - Compact delegate helpers are consistent with targeted decisions: ROOT is founder, FROM is target release.
   - Border commission helpers are consistent with state-targeted decisions: ROOT is claimant country, FROM is target state.

4. Unsupported operators and magic numbers:
   - No `<=` or `>=` found in the audited allowed files.
   - Remaining direct numeric literals are structural IDs, enum values in script constants, event IDs, or engine-required literal fields.
   - Resolver tuning values moved into `independence_wave_resolver`.

5. Arrays:
   - `global.independence_wave_candidate_pool` is per-run and cleared by `independence_wave_prepare_release_count`.
   - `global.independence_wave_released_countries` is appended by `independence_wave_register_successful_release` and used by `independence_wave_invite_compact_delegate`.
   - `global.independence_wave_compact_members` is appended by `independence_wave_prepare_compact_petition` and `independence_wave_accept_compact_delegate`, then used by `independence_wave_arbitrate_member_dispute`.
   - Persistent arrays may retain dead or annexed countries; target triggers check existence where used, so this is acceptable for the current tranche.

6. Package-family honesty:
   - Current scoring is a framework. It can mark several family candidates and set package variables, but it is not a completed country-package implementation.
   - `game_rule` and `railway` package constants still need package-specific scoring, overlays, tags/state groups, focus/decision behavior, and assets before they should be treated as implemented package paths.

## Why The Patch Is Bounded

- No new event chain, decision family, focus route, country package, scripted GUI, or on-action polling was added.
- No release solver redesign was attempted.
- Host survival remains based on the existing ordinary `release = PREV` resolver with host capital/non-capital checks.
- The patch only preserves ledgers across repeatable waves and centralizes existing resolver tuning.

## Validation Run

- `rg -n "\\bdays\\s*=\\s*(constant:|@)|<=|>="` on the audited allowed script/doc files: no forbidden operator or forbidden timed duration usage found.
- `rg` array lifecycle check confirmed only `global.independence_wave_candidate_pool` is cleared by Event 006 setup; `released_countries` and `compact_members` are append-only ledgers in the audited files.
- Brace-balance `awk` check passed for:
  - `events/006_independence_wave.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
- Leading-space indentation check found no leading spaces in the audited script files.
- Searched for local validation/lint scripts; no project HOI4 parser or validator script was found.

## Skipped Validation

- Did not run the game or an in-engine script reload.
- Did not run a full HOI4 parser because no project parser/validator was available in the repo search.
- Did not audit or patch `common/decisions/006_independence_wave_decisions.txt` beyond reading call sites, because it was outside the allowed patch list.

## Remaining Risks And Follow-Up

- `random_select_amount = @independence_wave_candidate_scan_cap` remains file-local because script-constant support for that scope field is not documented. If the parent confirms `constant:` works there, replace the macro with `constant:independence_wave_release_count.candidate_scan_cap`.
- `global.independence_wave_released_countries` and `global.independence_wave_compact_members` do not have stale-entry cleanup for annexed countries. Existing target triggers gate `exists = yes`, but a later cleanup helper would keep ledgers smaller.
- Package-family scoring does not yet fully represent `game_rule` or `railway` packages. This is documented as framework-only, not completed package behavior.
- The release resolver still uses ordinary `release = PREV`; it does not shrink candidate state sets. This matches the parent constraint and remains future work if a full host-survival state solver is later requested.
- `save_event_target_as = independence_wave_current_host` is set but not consumed in the audited files. It is harmless as a regular event target, but can be removed later if no follow-up chain uses it.

## Commit Status

No commit was made, per instruction.
