# Event006 Completion Audit After Generic Playability

Date: 2026-06-05
Auditor: `chaosx_event_completion_auditor`
Scope: Read-only completion audit for Event006 Independence Wave after the generic-playability cleanup.

## Scope And References

This audit used the current source-of-truth map in `docs/plans/006_independence_wave_plans/source_of_truth_map.md`, the Event006 specs under `docs/specs/006_independence_wave_specs/`, the compact event doc `docs/events/006_independence_wave.md`, and current implementation files under `events/`, `common/`, `interface/`, `gfx/`, `sound/`, `music/`, and `localisation/english/`.

Required repo guidance used:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/xlsx/SKILL.md` for read-only workbook inspection

Required HOI4 references were consulted from the offline `paradox_wiki/` snapshot and vanilla documentation before opening Chaos Redux implementation files. No gameplay, localisation, asset, or spreadsheet files were edited.

## Executive Status

Event006 is technically much closer to a playable state than the earlier handoffs describe, but it is not ready for a true completion claim.

The strongest current positives are:

- The main hidden event now builds a candidate pool, checks a live host, reserves a host survival state, prepares a reduced release footprint, calls `release = event_target:independence_wave_current_candidate`, applies autonomy/truce, and registers successful releases in one flow: `events/006_independence_wave.txt:73`.
- Released countries receive Event006 origin, variables, startup manpower/equipment, a provisional guard template, starting divisions, an arms factory, and the shared provisional focus tree: `common/scripted_effects/006_independence_wave_effects.txt:2266`.
- The shared focus tree is generic and Event006-origin-gated: `common/national_focus/006_independence_wave_focus.txt:13`, `common/scripted_effects/006_independence_wave_effects.txt:3128`.
- KUB/ALT are no longer active Event006 candidates; the only Event006 script references found are explicit candidate exclusions: `common/scripted_triggers/006_independence_wave_triggers.txt:44`.
- News display now has 1-16 release slots and uses the current-wave country list: `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:224`, `localisation/english/006_independence_wave_l_english.yml:47`.
- Evolution recording is limited to four chaos-tier stage entries, not per release/package/formable: `common/scripted_effects/006_independence_wave_effects.txt:5981`.

## Blocking Findings

### 1. Persistent host-state protection is documented but not actually persistent

The resolver sets `independence_wave_host_survival_reserved` on the protected host state immediately before release: `events/006_independence_wave.txt:83`. That flag is then cleared in the generic pending-candidate cleanup after the release attempt: `common/scripted_effects/006_independence_wave_effects.txt:1943`.

This means the immediate release guard still prevents direct host erasure for the current candidate, but the current docs overstate the protection. `docs/events/006_independence_wave.md:17` says successful releases mark the protected state so later Event006 releases or Border Commission claims cannot consume it. In current code, later release passes and Border Commission checks cannot rely on that flag because cleanup clears it.

Why it matters:

- The host-survival trigger does require a non-candidate host state for the current candidate: `common/scripted_triggers/006_independence_wave_triggers.txt:640`.
- The Border Commission target trigger explicitly blocks `independence_wave_host_survival_reserved`: `common/scripted_triggers/006_independence_wave_triggers.txt:2716`.
- Because the flag is cleared after each release attempt, that Border Commission protection only works while the temporary release target is still live, not as durable aftermath protection.

Completion impact: blocker for the host-survival contract and docs alignment. It is not evidence that the resolver never releases countries; it is evidence that the persistent safety layer described by the docs is not present.

### 2. Package/formable depth remains intentionally incomplete

The implementation has a large starter set of package identities, generic authority finishers, formation ledger flows, and niche generic releases. The current event doc still lists full completion blockers for remaining package data, hidden formables, additional package state maps, deeper strange packages, richer GUI states, and catalog/event-detail alignment: `docs/events/006_independence_wave.md:402`.

This audit excludes KUB/ALT from required scope, per current user correction. Excluding KUB/ALT, the remaining gap is still real: broad spec matrices include more candidates and formation ambitions than the current verified starter set. The event can be treated as a playable tranche, not as full package/formable completion.

Completion impact: blocker for "Event006 complete" if the completion standard means the full spec, not just generic playability.

### 3. Event-log/detail surfaces still carry stale package/formation evolution vocabulary

The active recorder only calls `record_events_log_evolution_entry` for four tier stages: Gathering Storm, Rising Cascade, Old Names Return, and Impossible Statehood. Dossier/package/formation helper effects prepare variables but do not call the global evolution recorder.

However, GUI/scripted-localisation surfaces still contain many package and formation "evolution type" labels and detail branches. These are stale with the current source-of-truth rule that package steps and formations should not behave like evolution entries.

Completion impact: not an active spam bug based on direct grep, but still a catalog/detail alignment blocker before a final completion claim.

### 4. Full achievement reachability depends on still-queued route depth

Achievement definitions, icons, and localisation exist for the Event006 set. Definitions are origin-gated, and shared-tag achievements such as `cr_not_the_collapse` explicitly reject Event005/Soviet Collapse origin flags. GFX and localisation references are present in `interface/chaosx_achievements.gfx` and `localisation/english/chaosx_achievements_l_english.yml`.

The remaining issue is reachability breadth: several achievements depend on deep package/formation/League/strange-state routes that are only as complete as those route systems. This is acceptable for a playable tranche, but not enough for final achievement/catalog parity.

Completion impact: blocker for final achievement completion, not for basic event firing.

## Non-Blocking Verification Notes

- No unsupported `<=` or `>=` operators were found in the audited Event006 gameplay/localisation files.
- Simple brace-balance checks returned zero balance and no early-negative close braces for the main Event006 event, scripted effects, scripted triggers, decisions, focus tree, and achievement file.
- `openpyxl` is not installed, so workbook inspection used direct `.xlsx` XML reads. The Event006 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` describes immediate releases, startup divisions, the shared 50-focus tree, generic aftermath systems, current starter packages, generic niche releases, and no active KUB/ALT scope.
- Super-event GFX, sound-channel WAV files, and music OGG files for IDs 52-58 exist. The super-event emit helpers are gated by gameplay thresholds such as League formation, strange doctrine, first old name, mass special wave, rump survival, and League war triggers.
- The repo worktree was already heavily dirty before this report. This audit added only this markdown report.

## Event005 Separation

Event006 setup writes `chaosx_release_origin_independence_wave` and the numeric release-origin variable: `common/scripted_effects/006_independence_wave_effects.txt:2266`.

The Event006 focus loader checks `is_independence_wave_release` before loading the generic Event006 tree: `common/scripted_effects/006_independence_wave_effects.txt:3128`.

Event005 setup helpers have explicit Event006-origin guards:

- `soviet_collapse_setup_breakaway_country` skips countries with `chaosx_release_origin_independence_wave`: `common/scripted_effects/005_soviet_collapse_effects.txt:3899`.
- `soviet_collapse_load_event_created_focus_tree` also skips that origin: `common/scripted_effects/005_soviet_collapse_effects.txt:8037`.

This is good separation evidence. Shared tags can still appear in Event005 candidate lists, but existing Event006-origin countries should not receive Soviet Collapse setup/focus effects through those guarded helpers.

## Current Completion Verdict

Do not claim Event006 complete yet.

The current implementation appears suitable for a "generic playability / urgent functional closure" handoff if the protected-state persistence issue is either fixed or explicitly re-documented as temporary-only. A true completion claim still needs durable host-protection behavior, package/formable scope closure, achievement reachability review, event-log/detail cleanup, and final catalog/spreadsheet parity.

## Skills Used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `xlsx`
