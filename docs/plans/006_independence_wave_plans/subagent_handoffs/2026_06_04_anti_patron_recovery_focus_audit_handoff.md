# Event 006 Anti-Patron Recovery Focus Audit Handoff

## Scope

Audited the just-added Event 006 anti-patron recovery focus tranche:

- `independence_wave_expose_broker_files`
- `independence_wave_audit_dependency_clauses`
- `independence_wave_charter_without_masters`
- `independence_wave_route_anti_patron_recovery`

This was a bounded focus, AI, localisation, constants, documentation, and catalog wording pass. No Event 005 files, flags, flag assets, or art files were edited.

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_anti_patron_recovery_focus_audit_handoff.md`

## Patch summary

- Added `independence_wave_charter_without_masters` as an alternate prerequisite for `independence_wave_send_permanent_delegation`.
  - Before: the anti-patron recovery endpoint set `independence_wave_route_anti_patron_recovery` but did not reconnect to the congress delegation route unless the country also completed `independence_wave_write_the_cabinet_contract`.
  - After: the anti-patron endpoint can progress into the existing congress support path without creating a new sponsor system.
- Moved the adjacent `independence_wave_balance_the_sponsors` AI patron-leverage gate from literal `15` to `constant:independence_wave_focus.patron_balance_ai_patron_gate`.
- Normalized local indentation in the patron branch focus blocks and the `independence_wave_anti_puppet_balancing` AI strategy `OR` block.

## Validation

- Brace balance:
  - `common/national_focus/006_independence_wave_focus.txt`: `brace_balance=0`
  - `common/script_constants/006_independence_wave_constants.txt`: `brace_balance=0`
  - `common/ai_strategy/006_independence_wave.txt`: `brace_balance=0`
- Unsupported operators:
  - `rg -n '<=|>='` over touched script files returned no matches.
- Focus count and coverage:
  - `common/national_focus/006_independence_wave_focus.txt`: 90 `focus = {` blocks.
  - Same file: 90 `ai_will_do = {` blocks.
  - Same file: 90 `completion_reward = {` blocks.
  - Focus name/description localisation coverage: 0 missing keys for focus ids/descriptions.
- Localisation encoding and style:
  - `localisation/english/006_independence_wave_l_english.yml` starts with UTF-8 BOM `efbbbf`.
  - `rg -n ':0\s*"' localisation/english/006_independence_wave_l_english.yml` returned no matches.
- Catalog/doc count:
  - `docs/events/006_independence_wave.md` says the tree has 90 focuses.
  - `docs/spreadsheets/chaos_redux_events_catalog.xlsx` row 7 cells `C7` and `O7` also reference the shared 90-focus Liberation Provisional tree.

## Remaining risks and gaps

- The anti-patron recovery branch is still a compact three-focus spine. That matches the bounded tranche request, but it is not a broad redesign of the Patron Ledger or a full sponsor politics route.
- `independence_wave_expose_broker_files` and `independence_wave_audit_dependency_clauses` intentionally keep their focus-specific proof flags separate from the Patron Ledger decision completion flags. I did not merge those state flags because that would change achievement and decision availability semantics beyond this local focus-gate audit.
