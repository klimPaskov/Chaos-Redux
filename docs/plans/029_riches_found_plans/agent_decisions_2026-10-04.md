# Event 029 agent decisions, 2026-10-04

Disposition: accepted and recorded by the implementing agent under the owner's full-authority grant for this round.
Acceptance basis: the lead's round-one owner decisions (relayed in the orchestration task) and the accepted Event 029 specification in `docs/specs/029_riches_found_specs/`.
Each entry names the decision, the reason, and the files it governs.
Implementation evidence is source review only unless an entry says otherwise; live-game behaviour remains with the orchestrator.

## D1. Adopt the stopped thread's uncommitted tranche

The stopped thread's 15 modified and 8 new Event 029 files were reviewed for load hazards before adoption: brace balance with comments stripped, unsupported `<=`/`>=` operators, `$PARAM$` tokens, timed flags with `days = constant:`, country-only effects inside state scopes (heuristic scope walk over every scripted effect and decision), undefined `riches_found_*` helpers, undefined script constants and missing localisation keys.
No hazard was found.
The routed date-unit defects 3 (account, late outcome, exposure and maintenance dates) and 5 (discovery receipt, controller pulse and terminal verification dates) are fixed inside this tranche, so it is committed as a whole.

Two corrections were made during adoption.
The event file header and the direct-invocation comment still described a load-weighted recipient; the dispatcher draws uniformly from the eligible pool, so both comments now say so, and the misindented state selection block was re-indented.
The terminal verification callback `chaosx.nr29.907` read its mine through a regular event target saved before a delay of up to a year; the callback is a state event whose scope is already the sealed mine, so it now reads `THIS` directly and no longer depends on the target surviving the delay.

The unrelated re-indent in `common/scripted_effects/chaosx_settings_effects.txt` belongs to another owner and is left untouched.

## D2. Catalog clusters 7 and 15 stay

The authoritative cluster workbook was written after the 2026-08-19 specification and keeps Event 029 in clusters 7 and 15.
No Event 029 cluster has a runtime consumer, so the specification's "no cluster" line is superseded rather than enforced in script.

## D3. Native 2,000 political power cap

The one-time 1,000 political power discovery grant uses the native cap.
No global define change, deferred credit or workaround is added; behaviour at the cap is a live-game check.

## D4. Constant-driven event delays

`days = constant:` inside `country_event` and `state_event`, and timed flags fed through a temporary variable, follow the repository convention used by more than one hundred other call sites.
They remain live-game checks and are not rewritten.
