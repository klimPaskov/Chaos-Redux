# Event006 Wrapup Status And Next Steps

Date: 2026-06-05
Owner: parent agent

## Scope

Status pass after urgent Event006 Independence Wave fixes, focused on release functionality, event-log behavior, released-country playability, reduced-start expansion, and the current next steps.

## Current Functional State

- The Independence Wave release event builds a candidate pool, validates a live host, reserves a host survival state, prepares a reduced release footprint, calls `release = event_target:independence_wave_current_candidate`, sets the new country free, registers successful releases, and stores release slots for the news event.
- Released countries receive Event006 origin, an ordinary/package identity, startup manpower, infantry equipment, support equipment, a recruitable Provisional Guard template, two starting divisions in the capital, one arms factory, and the shared `independence_wave_liberation_provisional_tree`.
- Reduced releases mask extra candidate cores before release, restore them afterward, mark `independence_wave_reduced_territory_start`, file a border survey, and add claim ambition. This gives one-state starts a generic recovery route through the Border Commission.
- The Border Commission is generic for independent Event006 releases and can claim, arbitrate, transfer, recover, or ultimatum valid non-capital, non-protected target states while checking that the owner can survive the transfer.
- KUB and ALT are not active Event006 candidates. They remain only as explicit exclusions in `can_independence_wave_use_candidate_tag`.
- The news event displays all stored successful releases from one through sixteen slots.
- True evolution log writes are limited to four chaos-tier stages: Gathering Storm, Rising Cascade, Old Names Return, and Impossible Statehood. Package and formation helpers prepare detail labels but do not call the global evolution-entry recorder.
- The first-impossible-state super-event sound token and the referenced `.wav` and `.ogg` payloads are present.

## Validation

- Required HOI4 wiki pages and vanilla documentation were consulted before the pass.
- Brace-balance checks returned zero balance and no early-negative close braces for Event006 event, effects, triggers, decisions, categories, focus tree, constants, ideas, and AI strategy files.
- `git diff --check` passed for the active Event006 runtime, localisation, event-log, sound, and music files checked in this pass.
- Localisation BOM check passed for `006_independence_wave_l_english.yml`, `chaosx_gui_l_english.yml`, and `chaosx_countries_l_english.yml`.
- No `error.log` file is currently present under `tmp/hoi4-error-logs` or elsewhere in the repo; only `tmp/hoi4-error-logs/watchdog.log` was found.
- `KUB`, `ALT`, `Kuban`, `Altai`, and `Oyrot` active-surface scan found only the intended KUB/ALT candidate exclusions.

## Next Steps

1. Run one final event-completion audit from the current worktree and compare it against the source spec, not older superseded handoffs.
2. If live testing reports an Event006 runtime error, patch from the concrete error line; no current `error.log` is available locally.
3. Reconcile stale docs that still describe package/formable/event-detail work as future or incomplete, separating full-spec ambitions from the urgent playable tranche.
4. Review package/formation event-log display labels as event details, not evolution-stage spam, and rename wording if the UI still reads like true evolutions.
5. Commit only a scoped, coherent Event006 tranche after reviewing the large dirty worktree and excluding unrelated Event005 or documentation-maintenance changes.

## Remaining Risks

- Full Event006 spec completion is not proven by this pass. The current state supports a playable urgent tranche, but final completion still needs a source-spec audit, catalog/spreadsheet alignment review, and package/formable reachability checks.
- Final animated assets are still documented as not complete unless real frame sheets, DDS output, static fallbacks, manifests, and `.gfx` handoffs are added.
