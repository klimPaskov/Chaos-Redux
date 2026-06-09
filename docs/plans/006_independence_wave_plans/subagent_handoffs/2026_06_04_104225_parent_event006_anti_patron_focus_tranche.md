# Parent handoff: Event 006 anti-patron recovery focus tranche

Date: 2026-06-04 10:42 UTC

## Scope

Added a compact anti-patron recovery spine to the shared Event 006 Liberation Provisional focus tree. The branch deepens the existing Patron Ledger layer without creating a second sponsor system.

New focuses:

- `independence_wave_expose_broker_files`
- `independence_wave_audit_dependency_clauses`
- `independence_wave_charter_without_masters`

New route flag:

- `independence_wave_route_anti_patron_recovery`

The branch starts from `independence_wave_balance_the_sponsors`, uses high patron leverage as the opening pressure, unlocks existing Patron Ledger decisions, lowers patron leverage through constants, and reconnects to `independence_wave_send_permanent_delegation` after `independence_wave_charter_without_masters`.

## Files changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_anti_patron_recovery_focus_audit_handoff.md`

## Subagent handoff

- `chaosx_focus_tree_auditor` ran with `fork_context=false`.
- Handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_anti_patron_recovery_focus_audit_handoff.md`
- Subagent patch:
  - added `independence_wave_charter_without_masters` as an alternate prerequisite for `independence_wave_send_permanent_delegation`
  - moved the `Balance the Sponsors` patron AI gate into `constant:independence_wave_focus.patron_balance_ai_patron_gate`
  - cleaned local indentation in the patron focus/AI blocks

## Asset and flag handling

No flags, flag assets, portraits, or new art were created or edited. The branch reuses the existing registered focus sprite `GFX_focus_independence_wave_patron_balance`.

## Validation

- Offline Paradox wiki and vanilla documentation references were refreshed before this tranche.
- Script brace balance:
  - `common/script_constants/006_independence_wave_constants.txt`: clean
  - `common/national_focus/006_independence_wave_focus.txt`: clean
  - `common/ai_strategy/006_independence_wave.txt`: clean
  - `localisation/english/006_independence_wave_l_english.yml`: clean
- Unsupported operators:
  - no `<=` or `>=` in touched Event 006 script files.
- Localisation:
  - `localisation/english/006_independence_wave_l_english.yml` remains UTF-8 with BOM.
  - no `:0` keys found.
  - all 90 focus ids have name and description keys.
- Focus tree:
  - 90 `focus = {` blocks.
  - 90 `ai_will_do = {` blocks.
  - 90 `completion_reward = {` blocks.
  - `GFX_focus_independence_wave_patron_balance` is registered in `interface/006_independence_wave_icons.gfx`.
- Workbook:
  - `docs/spreadsheets/chaos_redux_events_catalog.xlsx` opens/converts through LibreOffice headless.
  - no `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, or `#NAME?` tokens found.
  - row 7 now says `90-focus Liberation Provisional tree`.
  - row 7 now says `New States Congress`, matching the implemented category name.

## Remaining risks and gaps

- This is a bounded focus-route hardening tranche, not a complete Patron Ledger redesign.
- The anti-patron focus proof flags remain separate from Patron Ledger decision completion flags to avoid changing decision and achievement semantics outside this tranche.
- Event 006 is still incomplete as a full source-spec pack. Remaining blockers include final package depth, package-specific presentation assets and animation manifests, final catalog/event-detail alignment, balance scenarios, and completion audits.
