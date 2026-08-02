# Event 016 recognition-basis news handoff

## Scope

This bounded continuation enriches the existing `chaosx.nr16.305` international-recognition headline without adding a fire path, reward, event-log row, super-event, project, unit, provider, entity, or model dependency.

The headline reads the active host's existing recognition receipts and explains the first recorded public cause of international visibility.

## Changed files

- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` adds `GetBrilliantScientistNewsRecognitionClause`.
- `localisation/english/016_brilliant_scientist_l_english.yml` adds five recognition-basis clauses and appends the helper to `chaosx.nr16.305.d`.
- `docs/events/016_brilliant_scientist/systems/news_events.md` documents the selector and its presentation-only contract.
- `docs/events/016_brilliant_scientist/overview.md` records the recognition headline continuation and its unchanged runtime boundary.
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md` records the accepted continuation and handoff.
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md` records the current bounded status and handoff list.

## Runtime contract

The selector is evaluated against `event_target:brilliant_scientist_current_host` and safely falls back when terminal cleanup has cleared the target.

The stable precedence is joint laboratory, public reputation or exposed research advantage, foreign protection framework, failed-assassination exposure, and neutral.

All selected text is presentation-only and does not change the recognition score, threshold, one-time receipt, super-event dispatch, research bonus, transfer state, containment state, or model boundary.

## Validation

Focused Event Inspector lint for `chaosx.nr16.305` must report `status: ok` with zero blockers and zero blocking diagnostics after the parent refreshes the workspace.

Static checks must confirm five recognition keys resolve exactly once, the helper definition occurs once, the `.305` call occurs once, the localisation file remains UTF-8 with BOM, the frozen package checksum ledger remains at 55 entries with zero mismatches, and `git diff --check` is clean.

## Deferred boundary

Broader country-context flavour, quantitative route-balance evidence, user-owned live acceptance, and all seven reusable Event 016 3D unit packages remain deferred.
