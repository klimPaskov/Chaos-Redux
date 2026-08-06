# Event 020 Localisation and Scripted Localisation Audit Handoff

Date: 2026-08-06

## Scope

Audited Event 020 event, report, news, evolution, triggerable-scenario, decision, focus, country, unit, achievement, world-end, shared disease-board UI, and scripted-localisation text against the current runtime source and accepted specification package.

## Audit result

- Missing key list: none among explicit Event 020 event references, 110 decision and category ids, 122 focus nodes, the two focus-tree names, six Rat sub-units and descriptions, country identities, or disease-board GUI text and tooltip references.
- Duplicate key list: none among 1,302 Event 020-related localisation keys across English localisation.
- Scripted localisation issue list: none. All 15 `GetBlackPlague*` calls found in the Event 020 and linked shared GUI text resolve to a `defined_text` declaration, and every inspected `localization_key` target exists.
- Dynamic text opportunities: four terminal-readiness rows displayed a literal maximum of `100` even though runtime clamps use `constant:black_plague_value.maximum`. Those rows now display the shared constant. Existing state, target-continent, actor, route-readiness, cost, timer, and meter tokens remain dynamic.
- Cross-surface mismatch notes: scenario text exposed `RTA`, `RTX`, forced setup, reconciliation, and temporary-reservation language that belonged to implementation rather than the world. Rat decisions, a focus, one report, one achievement, and one unit description also exposed `capped`, `scripted`, or carrier-tag language. These mismatches are patched. The entry title `Black Plague` and the historical news title `Black Death` remain deliberately distinct.
- File encoding concerns: all ten dedicated Event 020 English localisation files and the three edited shared English localisation files are valid UTF-8 with BOM. Mixed repository line-ending normalization remains present but did not alter encoding.
- Overflow concerns: the shared disease-board inspection could not render because the MCP scanner returned `SCAN_BYTE_LIMIT`. The four terminal-readiness strings and the longest resource cost rows therefore remain visually unverified. They preserve required values and are not shortened in a way that would conceal costs.

## Files changed

- `localisation/english/020_black_death_l_english.yml`
- `localisation/english/020_black_plague_rat_countries_l_english.yml`
- `localisation/english/020_black_plague_rat_decisions_l_english.yml`
- `localisation/english/020_black_plague_rat_focus_l_english.yml`
- `localisation/english/020_black_plague_reports_l_english.yml`
- `localisation/english/020_black_plague_response_l_english.yml`
- `localisation/english/biowarfare_disease_containment_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

## Changed keys

- Event and report: `chaosx.news.21.d`, `chaosx.nr20.43.d`.
- Country and unit: `rat_dock_stowaways_desc`.
- Rat decision and category text: `black_plague_rat_brood_category_desc_rta`, `black_plague_rat_brood_category_desc_king`, `black_plague_rat_call_a_brood_pulse_desc`, `black_plague_rat_call_a_brood_pulse_cost_blocked`, `black_plague_rat_concentrate_brood_desc`, `black_plague_rat_scatter_brood_cost_blocked`, `black_plague_rat_devour_rival_desc`, `black_plague_rat_distribute_the_nests_desc`, `black_plague_rat_seat_the_alpha_desc`.
- Focus text: `black_plague_rat_capped_pulses`, `black_plague_rat_mass_swarm_desc`.
- Human response text: `black_plague_produce_medical_reserve_desc`, `black_plague_produce_medical_reserve_cost_tooltip`, `black_plague_shared_population_recovery_program_desc`, `black_plague_shared_start_last_response_hold_effect_tt`.
- Achievement text: `black_plague_achievement_eligible_tooltip`, `020_black_plague_no_census_required_DESC`.
- Triggerable scenario and world-end text: `chaosx.scenarios.black_plague.impact.low`, `chaosx.scenarios.black_plague.impact.medium`, `chaosx.scenarios.black_plague.impact.high`, `chaosx.scenarios.black_plague.impact.maximum`, `chaosx.scenarios.launch_status.black_plague.repeat_ready`, `chaosx.scenarios.launch_status.black_plague.already_launched`, `chaosx.scenarios.launch_status.black_plague.setup_failed`, `chaosx.events_log.world_end.black_plague.details`.
- Shared disease-board dynamic text: `black_plague_terminal_readiness_king_active`, `black_plague_terminal_readiness_route_open`, `black_plague_terminal_readiness_target_selected`, `black_plague_terminal_readiness_crowned`.

## Display before and after

- Rat force limits previously appeared as `capped force`, `capped host`, and `capped pulse` implementation language. The text now uses `force ceiling`, `finite reserve`, and `Measured Pulses`, while retaining every cost, cooldown, and gain.
- Scenario rows previously named internal tags and setup operations. They now name lesser brood basins, the Rat Nation, the Rat King, infected states, active evolutions, and locked terminal outcomes.
- The Black Death news report previously called the origin `weighted`. It now identifies the first known basin.
- The world-end log previously called the takeover deterministic. It now describes the Rat King's final order and its consequences directly.
- The Rat dock unit previously referred to scripted overseas seeding. It now explains that the unit hides in cargo and reaches overseas ports.
- Terminal-readiness rows previously displayed `/ 100`. They now display `/ [?constant:black_plague_value.maximum|0]`.

## Prose-quality repairs

- Vagueness: replaced `weighted origin`, setup state, and reconciliation language with the concrete basin, crisis, and launch result.
- Bloat: shortened the brood absorption report and blocked-cost requirements without removing conditions.
- Obvious explanation: removed setup-reservation and deterministic-process commentary that did not help the player act.
- Repetition: removed repeated `capped` wording from adjacent Rat command surfaces.
- Overcomplication: changed carrier-tag phrasing into direct Rat Nation and Rat King language.
- Style-rule repair: removed implementation terms including `capped`, `scripted`, `deterministic`, `forced setup`, and internal country tags from visible prose. No new em dash, semicolon, staged contrast formula, or implementation-history wording was introduced.

## Sourced quotation preservation

The quote-bearing super-event file was inspected and left unchanged. `chaosx_super_event.85.q` retains the Robert Browning excerpt, `chaosx_super_event.86.q` retains Revelation 6:8, and `chaosx_super_event.87.q` retains the Aeschylus excerpt in E. D. A. Morshead's translation without added terminal punctuation. The existing Event 087 research handoff records that the source line ends at `pain`; this audit preserved that exact choice. No quotation token, attribution, or cultural-remark button was edited.

## Validation

- Parsed 1,302 relevant keys across English localisation with zero duplicates.
- Resolved every explicit Event 020 `title`, `desc`, `name`, custom-cost, tooltip, and scripted-localisation target found in the bounded source set.
- Checked 110 decision and category ids with zero missing name or description keys.
- Checked 122 focus nodes with zero missing name or description keys. The two tree ids have names and do not require node-style `_desc` rows.
- Checked six Rat sub-units with zero missing name or description keys.
- Checked every explicit disease-board GUI `text`, `buttonText`, and `pdx_tooltip` key with zero missing keys.
- Parsed the edited localisation rows with zero malformed entries and zero `:0` keys.
- Compared all originally changed rows and found no lost dynamic tokens, formatting markers, icons, costs, requirements, names, or timers. The four later terminal maximum edits intentionally add `constant:black_plague_value.maximum`.

## MCP evidence and blockers

- `hoi4.event_inspect` was invoked for the `chaosx.nr20` namespace in lint mode. It did not return after repeated waits and was terminated without an artifact, so event graph and popup rendering remain unavailable.
- `hoi4.focus_inspect` was invoked for both Event 020 focus files. Neither call returned after repeated waits and they were terminated without artifacts, so focus-tree visual localisation and overflow evidence remain unavailable.
- `hoi4.gui_inspect` reached the Event 020 shared disease board with scenario id `event020_black_plague` but returned `SCAN_BYTE_LIMIT`, status `error`, workspace id `mod_chaos_redux_ea3b2d67c2c0`, and no artifacts.
- No Technology Tree Viewer is installed, and Event 020 has no in-scope technology tree in this localisation patch.

## Skipped meaningful validation

No event, focus, or GUI MCP render could be completed because the prerequisite inspections returned no usable graph or the byte-limit error above. No live game session was run because runtime consumer validation belongs to the parent and user.

## Remaining gaps and unresolved wording decisions

- Visual overflow remains unresolved for the shared disease-board terminal summaries and the longest custom-cost strings because the GUI MCP could not produce a render.
- The implementation still uses the internal focus id `black_plague_rat_capped_pulses`; only its player-facing title changed to `Measured Pulses`, so no script rename is required.
- No missing mechanic or design-depth gap was identified that requires a separate plan handoff.

## Simplifications and omissions

No localisation fallback or gameplay simplification was introduced. The only omitted evidence is MCP visual output blocked as documented above.
