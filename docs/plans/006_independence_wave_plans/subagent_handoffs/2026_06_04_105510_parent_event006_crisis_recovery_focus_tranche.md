# Parent handoff: Event 006 crisis recovery focus tranche

## Scope

Implemented a bounded crisis recovery spine in the shared Event 006 Liberation Provisional focus tree. The branch gives releases a recovery path when war, low stability, compact failure, regional compact integration failure, patron cabinet-seat demands, or dangerous patron leverage make normal state-building too fragile.

New focuses:

- `independence_wave_summon_emergency_session`
- `independence_wave_form_street_defense_committees`
- `independence_wave_reopen_cabinet_authority`

New route/proof flags:

- `independence_wave_route_crisis_recovery`
- `independence_wave_focus_emergency_session`
- `independence_wave_focus_street_defense_committees`
- `independence_wave_focus_cabinet_authority_reopened`

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_105347_crisis_recovery_focus_audit_handoff.md`

No Event 005 files were touched. No flags or assets were touched.

## Implementation notes

- The branch root is gated behind existing crisis signals instead of being a normal stable-country route.
- `independence_wave_reopen_cabinet_authority` is an alternate OR prerequisite for `independence_wave_send_permanent_delegation`, so recovered crisis states can rejoin the Congress path.
- Rewards use `constant:independence_wave_focus.*` tuning for stability, militia, legitimacy, cohesion, and patron relief.
- Patron leverage relief calls `independence_wave_clamp_patron_leverage` only when dangerous patron leverage exists.
- The AI overlay `independence_wave_crisis_recovery_posture` steers crisis states toward defense, restraint, infantry/support production, and division-template XP spending.

## Subagent audit

Spawned `chaosx_focus_tree_auditor` with `fork_context=false`.

The auditor patched one narrow mismatch: `independence_wave_crisis_recovery_posture` now also activates from `has_war = yes` and `has_independence_wave_dangerous_patron_leverage = yes`, matching the crisis focus entry gate.

Audit handoff:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_105347_crisis_recovery_focus_audit_handoff.md`

## Validation

- Focus tree count: 93 `focus = {` blocks.
- Focus tree coverage: 93 `ai_will_do = {` blocks and 93 `completion_reward = {` blocks.
- Focus localisation: 0 missing name keys and 0 missing `_desc` keys.
- Brace balance clean for the touched script and localisation files.
- Unsupported operator scan found no `<=` or `>=` in touched script files.
- Localisation file remains UTF-8 BOM and has no `:0` entries.
- Workbook XML contains `93-focus` and no `90-focus`.
- LibreOffice headless converted `docs/spreadsheets/chaos_redux_events_catalog.xlsx` successfully.
- Workbook XML scan found no `#REF!`, `#VALUE!`, `#NAME?`, or `#DIV/0!` tokens.

## Remaining gaps

No remaining gaps were found inside this bounded crisis recovery focus tranche.

The broader Event 006 source-spec goal is still incomplete; this tranche closes only the documented shared-tree crisis branch gap.
