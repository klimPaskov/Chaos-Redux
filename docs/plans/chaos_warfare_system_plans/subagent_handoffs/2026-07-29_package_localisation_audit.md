# Chaos Warfare package localisation audit handoff

Date: 2026-07-29

This is a bounded Chaos Warfare and CBRN package localisation audit and handoff, not an overall Chaos Warfare completion claim.

## Authority and scope

The audit used `AGENTS.md`, the required Chaos Redux event, decision, and subagent guidance, the offline Paradox wiki pages, the installed vanilla documentation, all twelve numbered Chaos Warfare specifications, the applicable matrices and prompts, and the 2026-07-29 closure and scenario-evidence plans.

The audit treated the twelve specifications as authority, then matrices, then prompts, with the later explicit decisions for doctrine scope, biological potency order, agent-neutral native raid success, fail-closed exact-state operations, delivery routes, wording, and preserved military raid icons.

Only small localisation corrections directly required by the audit and the accepted achievement conformance changes were made.

## Changed files and exact keys

### `localisation/english/cbrn_achievements_l_english.yml`

- `chaos_warfare_quarantine_without_collapse_tooltip` now requires retaining the required stability, medical capacity, and supply-vehicle readiness after containing the outbreak and clearing ordinary episodes.
- `chaos_warfare_arsenal_dismantled_DESC` now states that the country must avoid changing regime after the campaign begins or capitulating.
- `chaos_warfare_arsenal_dismantled_tooltip` now states the same post-start regime-change and capitulation disqualifiers alongside inspection, stockpile destruction, condemnation history, and the empty offensive stockpile.
- `chaos_warfare_terminal_contagion_DESC` now requires the 90-day survival record to end with the country still at war, an active-sanctions history, and either serious Chemical Contamination or a catastrophic biological episode.
- `chaos_warfare_terminal_contagion_tooltip` now states that the country must survive ninety days and still be at war, have the sanctions history, and also have serious Chemical Contamination or a catastrophic biological episode.

The Terminal Contagion wording uses “still be at war” rather than implying uninterrupted war throughout the ninety-day interval, matching the accepted completion trigger.

### `localisation/english/cbrn_battlefield_operations_l_english.yml`

- `cbrn_battlefield_resolution_rejected_tt` no longer uses fallback or estimator wording and now explains that an exact target, policy, protection, payload, or condition receipt was invalid and that the release was not redirected to another state.

### `localisation/english/chaosx_gui_l_english.yml`

No change was made to this concurrently modified file.

The stale `chaosx.events_log.window.event_details.cbrn_action` value was inspected and a narrow display correction was attempted, but the file was write-locked by concurrent work and `apply_patch` could not safely update it without risking unrelated edits.

## Required coverage findings

### Missing keys

- The bounded source-localisation audit found 521 CBRN and biological source references, with 402 unique package keys represented and no missing package keys.
- The package scripted-localisation audit found 148 package references and no missing package keys.
- All 15 `chaos_warfare_*` achievements have `_NAME`, `_DESC`, and `_tooltip` localisation, with zero missing achievement keys.
- All 27 hidden aerosol/rack grant technologies have name and `_desc` localisation, with zero missing technology keys.
- CBRN Event Log type 991 has an event-name key, debug/event-name mapping, history mapping, and active detail mapping.

### Duplicate keys

- The 31 bounded package YAML files contain 5,090 parsed localisation keys and zero duplicate keys.
- Unrelated duplicate keys exist elsewhere in the repository, including non-CBRN Fallout and generic content, and were not changed.

### Scripted localisation

- The seven package-relevant scripted-localisation files have complete package-key coverage for the 148 references audited.
- Type 991 resolves to `cbrn.event_log.details` through the action-record event-log mapping and resolves to `chaosx.event_name.991` for the event name and history display.
- `GetCBRNActionLogRepeatUsePressure` selects the four named repeat-use categories `none`, `single`, `campaign`, and `sustained` from the action-record thresholds.
- The stale GUI detail key remains an issue because it contains raw numeric attribution, retaliation, first-use, and repeat-use fields and omits the named actor and victim display.
- No source under `interface` or `common` references the stale GUI key; the active event-details placeholder routes through `cbrn.event_log.details`.

### Dynamic text opportunities

- `localisation/english/biological_facility_recovery_raids_l_english.yml` still presents several facility-recovery resource thresholds and outcome percentages as static text.
- `localisation/english/biological_sabotage_l_english.yml` still presents agent-specific preparation and resource costs as static text.
- `localisation/english/japan_biological_campaign_l_english.yml` still presents bounded Japan-China decision costs, payloads, support, and command-power values as static text.
- `localisation/english/cbrn_hq_l_english.yml` still presents force bands, timing bands, and manpower values in static slash-list text.
- `localisation/english/cbrn_occupation_l_english.yml` still presents expected Sarin and Soman effect envelopes as static ranges.
- `localisation/english/cbrn_designers_l_english.yml` still presents several designer trait percentages statically.

These are dynamic-localisation opportunities rather than proven current mismatches, so no broad rewrite was made in this bounded audit.

## Cross-surface and wording findings

- The active type-991 detail displays named actor, victim nation, target state, weapon class, agent, delivery route, outcome, attribution, first-use status, diplomatic context, repeat-use pressure, deaths, contamination or outbreak changes, evidence quality, and the recorded date.
- Repeat-use category text is present and uses player-facing names rather than raw threshold values.
- Biological raid, sabotage, bounded Japan-China, and doomsday decision surfaces are localised, including agent-specific text and the Tularemia < Anthrax < Plague < Smallpox potency order with only Smallpox described as severe.
- Native raid-success wording is agent-neutral where the source uses the native raid success path.
- Doctrine wording describes CBRN potency and Condemnation mitigation only and does not claim that doctrine creates, authorizes, or conceals camps.
- Existing military raid icon names and files remain preserved for the biological and Sarin/Soman raid surfaces.
- The bounded CBRN and biological player-facing files contain no `fallback`, `estimator`, or ordinary continuous-air claim after the battlefield tooltip correction.
- A repository-wide search still finds unrelated `continuous` wording in non-CBRN content, which was outside this package audit and was not changed.
- No hidden incubation duration, hidden incubation value, attribution band, or secret attacker identity is exposed by the audited package text.
- Lifecycle text refers to uncertainty, concealment, detection, or visible outbreaks without announcing hidden incubation values.
- Ground, weather, terrain, and nerve route wording is conditional on valid exact-state releases where applicable; the current fail-closed source hooks prevent the text from authorising an invalid release.

## Encoding findings

- All 31 bounded package YAML files have a UTF-8 BOM.
- The package scripted-localisation `.txt` files decode as UTF-8 without a BOM, matching their existing script-file convention.
- No invalid encoding was found in the audited package files.

## Validation coverage

- Parsed 31 bounded package YAML files for key coverage, obtaining 5,090 keys and zero duplicates.
- Checked BOM presence for all 31 bounded package YAML files, obtaining zero missing BOMs.
- Checked all 15 Chaos Warfare achievement IDs and all three localisation surfaces per achievement, obtaining zero missing keys.
- Checked all 27 hidden aerosol/rack technology IDs and both localisation surfaces per technology, obtaining zero missing keys.
- Checked package source and scripted-localisation references, obtaining zero missing package references in the bounded audits.
- Searched bounded CBRN and biological player-facing text for fallback, estimator, and continuous-air wording, obtaining no such matches after the scoped correction.
- Checked source references for the stale GUI detail key and found none.
- Inspected type 991 mappings, active actor/victim display, repeat-use selectors, biological delivery-route text, and existing raid icon references.
- Hearts of Iron IV was not launched, and live game or GUI verification remains user-owned as required by repository guidance.

## Remaining limitations and blockers

- Ground chemical exact-state decisions remain fail-closed because `cbrn_battlefield_current_version_condition_hook_verified = always = no`.
- Nerve occupation exact-state decisions remain fail-closed because `cbrn_occupation_current_version_condition_hook_verified = always = no`, and no target-loss receipt exists.
- Ordinary-air continuous contamination remains disabled and fail-closed because the required mission hook is not verified.
- `chaos_warfare_no_wind_is_friendly` and `chaos_warfare_unbroken_supply_corridor` still depend on unsupported achievement receipts identified by the closure plan.
- `chaos_warfare_antidote_arrived` still describes an accepted nerve-suppression attack, but its occupation receipt is unreachable while the exact-state hook remains fail-closed.
- The Hardened Mobile Plant transaction remains unsupported.
- The stale `chaosx.events_log.window.event_details.cbrn_action` key remains unpatched because the concurrently modified GUI file was write-locked; the active type-991 detail path is already correct.
- The static numeric strings listed under dynamic text opportunities remain unchanged because converting them requires a broader source-constant and dynamic-localisation pass.
- The Technology Tree Viewer is not installed, so hidden technology coverage was source/localisation based rather than viewer-rendered.
- No in-game overflow, live localisation reload, or runtime event-log GUI validation was performed.
- No commit was created because the shared worktree contains unrelated concurrent edits and the parent agent owns final integration.

The package audit and the scoped localisation corrections are handed off for parent review, with the limitations above still open.
