# Localisation cleanup handoff

Scope: shared Chaos Redux English and scripted localisation plus Event 001 through Event 020 surfaces. Event 021 and later content was only inspected where a shared selector or registry referenced it. Parent-owned Event 010 Death and Event 011 Secret Alliance evolution-type mappings and the main-menu version tooltip were preserved.

## Required references and audit method

Read `AGENTS.md`, the Chaos Redux events and subagents skills, the required offline Paradox wiki pages, and the relevant vanilla localisation and dynamic-variable documentation before editing.

Scanned English key coverage, exact-case duplicate keys, scripted-localisation method references, shared event-log selectors, event detail and evolution detail mappings, placeholder/process wording, dynamic variable formatting, and UTF-8 BOM bytes.

## Changed files and keys

- `localisation/english/001_communism_spread_l_english.yml`: replaced the legacy Event 001 option text `chaosx.nr1.1.a` and `chaosx.nr1.1.b` with `Contain the agitation.` and `The revolution has already arrived.`.
- `localisation/english/002_zombie_outbreak_l_english.yml`: formatted `total_zombie_divisions` as an integer in `chaosx.nr2.7.d` with `[?total_zombie_divisions|0]`.
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`: removed four duplicate title and description definitions for `independence_wave_iw043_repair_cheboksary_workshops` and `independence_wave_iw058_fortify_mountain_river_corridor`. The focus localisation file remains the canonical source for those shared keys, while the decision-specific start, success, timeout, cancel, and cost text remains in the decisions file.
- `localisation/english/chaosx_gui_l_english.yml`: replaced process-style scenario, event-detail, evolution-detail, and cluster placeholder wording with current-state wording. The changed keys are `chaosx.scenarios.africa.desc.placeholder`, `chaosx.scenarios.type.placeholder`, `chaosx.scenarios.placeholder.impact`, `chaosx.triggerable_scenarios.11.d`, `chaosx.events_log.window.cluster_details.description.formables`, `chaosx.events_log.window.event_details.entry_placeholder.generic`, and `chaosx.events_log.window.evolution_details.placeholder.generic`.
- `localisation/english/fallout_world_end_ashline_firebreak_l_english.yml`: added the missing shared event-log base key `fallout.event_log.ashline_firebreak.detail` pointing to the existing `GetFalloutEvent554EventLogDetail` selector. This is the only Event 021 and later localisation file touched, and it was touched solely because the shared `GetEventsLogEventDetailDescription` selector directly requests that key for history id 554.

## Display changes before and after

- Event 001 no longer presents the player with the legacy Custerdome and class wording. The options now describe containment or acceptance of the revolution.
- The Anti-Zombie League report now displays the division count as a whole number instead of an unformatted variable value.
- Event 006 decisions no longer compete with focus-tree strings for the same four keys. The focus wording is used consistently, and decision outcome tooltips still provide the functional details.
- Scenario and event-log fallback text no longer promises future rework or future detail. It reports that no playable incident, outcome, escalation, or additional detail is currently available.
- Ashline Firebreak history entries now resolve the shared base detail selector before choosing one of the existing cut, seal, cordon, or callback branch descriptions.

## Missing key list

- Fixed: `fallout.event_log.ashline_firebreak.detail` was requested by `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5650` but only branch-suffix keys existed.
- Deferred shared registry gap: `chaosx_scripted_localisation_debug.txt` and `chaosx_scripted_localisation_settings.txt` contain selector branches for `chaosx.event_name.100` through `chaosx.event_name.1000`, while the English event-name registry defines only selected ids such as 1 through 99, 163, 635 through 641, and 991. Generating hundreds of speculative names or redirecting the selector would change shared registry behavior and requires parent design input.
- After the Ashline addition, the shared event-log selector scan found zero missing non-GFX localisation keys outside the known future event-name family.

## Duplicate key list

- Fixed: four exact duplicate Event 006 title and description keys were removed from the decisions file.
- The case-sensitive scan of Event 001 through Event 020 and shared GUI/event-name English files now reports zero duplicate non-header keys.
- Retained intentional case variants in Event 005 and related country or focus surfaces, such as lowercase idea ids versus uppercase route or cosmetic-tag ids. These are distinct Clausewitz keys and were not collapsed.
- Deferred out-of-scope duplicate candidates: standalone Fallout files contain repeated option keys in some Event 021 and later files, and `FalloutThawWaterEventLogPayload` is declared in both `fallout_world_end_bridge_that_moved_event_log_scripted_localisation.txt:6` and `fallout_world_end_thaw_water_event_log_scripted_localisation.txt:6`. No live custom-localisation reference to the duplicate method name was found, so renaming it without the owning Fallout wiring is unsafe.

## Scripted-localisation issue list

- The shared Ashline history selector had a missing base localisation key. It is fixed with the existing `GetFalloutEvent554EventLogDetail` method.
- The five `chaosx.events_log.window.evolution_details.placeholder.generic` fallbacks at lines 8116, 8277, 8303, 8367, and 8393 are defensive `always = yes` branches. Valid Event 001 Communism stages 1 through 3, Event 002 Zombie stages 1 through 3, Event 003 Holy Realm stages 1 through 4, and the remaining Event 004 through Event 020 evolution types all resolve to authored detail keys before those branches. No valid Event 001 through Event 020 path reaches them. Scripted mappings were left unchanged, including the parent Event 010 and Event 011 mappings.
- The generic evolution fallback localisation was rewritten to `No additional evolution detail is recorded for this milestone.` so an invalid or uninitialised state does not expose process notes.
- Custom scripted-localisation method reference checks for the allowed event and shared prefixes found no missing methods.

## Dynamic text opportunities

- Fixed the only clearly unformatted numeric variable found in Event 001 through Event 020 English localisation, `total_zombie_divisions` in Event 002.
- Event-log actor names, state names, route names, costs, timers, evolution stages, and CBRN values already use dynamic localisation or scoped variables in the inspected surfaces. No new dynamic method was added.
- The future event-name registry gap remains a shared selector design problem rather than a safe localisation-only expansion.

## Cross-surface mismatch notes

- Event 006 focus and decision files had the same four key ids with different text. The focus strings remain canonical after duplicate removal, and the decision file still owns all functional project tooltips.
- Event 012 and the Africa Is One scenario are intentionally registered as a reserved member with no playable formable escalation. The cluster description now states that player-facing state without mentioning implementation history.
- Parent changes to `chaosx.events_log.evolution.type.death`, `chaosx.events_log.evolution.type.secret_alliance`, and `chaosx_main_menu_version_tt` were reviewed and preserved.
- Event 020 response and weaponization cost keys already present in the working tree were preserved.
- Scripted GUI event-target scope patterns were not flagged or migrated.

## File encoding concerns

All touched English YAML files retain UTF-8 with BOM bytes `EF BB BF`. Scripted-localisation `.txt` files remain in their existing no-BOM format. No encoding repair was needed.

## Recommended deferred fixes

- Decide whether the shared future event-name selector should gain a bounded registry fallback or a deliberate expansion plan. Do not synthesize hundreds of event-name strings in a localisation-only pass.
- Have the Fallout owner resolve the duplicate `FalloutThawWaterEventLogPayload` declaration and audit repeated option keys in standalone Fallout event files when that scope is opened.
- Keep the neutral scenario and event-log fallback wording unless a future accepted design adds a playable Event 012 formable escalation or new evolution detail branches.

## Validation

- Re-scanned shared event-log `localization_key` references against the mod English key set after the patch. The result was zero missing non-GFX keys outside the known future event-name family, and `fallout.event_log.ashline_firebreak.detail` is present.
- Re-ran the case-sensitive duplicate-key scan over Event 001 through Event 020 and shared GUI/event-name files. The result was zero duplicate non-header keys.
- Rechecked UTF-8 BOM bytes for every touched YAML file.
- In-game launch and live UI validation were skipped because repository policy assigns those checks to the parent and user.

Unresolved wording decision: the canonical Event 006 focus descriptions are less operational than the removed decision descriptions, but decision-specific requirements and outcomes remain visible through existing custom tooltip keys. No gameplay meaning was changed.

Handoff path: `docs/plans/repo_cleanup/subagent_handoffs/localisation_cleanup_2026-07-29.md`.
