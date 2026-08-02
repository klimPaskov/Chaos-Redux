# Event 020 readiness board and Crown Strike AI handoff

## Scope

This tranche closes two current runtime-surface gaps without adding a disease category, country tag, model, or separate UI window.

## Gameplay changes

- `common/scripted_effects/020_black_plague_evolution_effects.txt` refreshes target-continent capital and refuge totals, human-established state count, and aggregate human response strength from the existing response-country registry during the existing Rat King progress refresh.
- `common/scripted_effects/020_black_plague_effects.txt` initializes the new readiness snapshot variables with the existing Event 020 runtime generation.
- `common/scripted_localisation/020_black_plague_terminal_scripted_localisation.txt` adds `GetBlackPlagueTerminalFocusReadiness` and keeps the readiness summary dynamic rather than duplicating a second GUI surface.
- `localisation/english/biowarfare_disease_containment_l_english.yml` exposes target control, surviving capitals/refuge nodes, focus readiness, royal registers, deaths, human state counts, and response strength in the shared-board readiness rows.
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt` removes the player-only Crown Strike gate while preserving every route, war, target, contribution, payment, and terminal-safety condition.
- `common/decisions/020_black_plague_shared_response_decisions.txt` gives Crown Strike urgency-aware AI weighting keyed to terminal pressure, Dominion, and war.

## Validation

Focused `hoi4_event_inspect` lint on `chaosx.nr20.90` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and zero blocking diagnostics. The six changed script/localisation files have balanced braces and no unsupported comparison operators; the edited localisation file retains its UTF-8 BOM with no duplicate keys.

## Boundary

This is static source validation only. Hearts of Iron IV was not launched, and live consumer/UI rendering remains user-owned validation. No bespoke Rat Nation or Rat King model package is required or planned.
