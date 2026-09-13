# Event 23 fresh final localisation audit

Date: 2026-09-05

Disposition: `implemented`, with two visual-validation limits and one spreadsheet wording handoff.

The Event 23 player-facing text set is mechanically complete after a narrow correction to the three verification reports and the public demonstration news description. The audit found no missing Event 23 source-referenced key, no duplicate Event 23 key, no broken return key in the Event 23 scripted localisation, and no encoding defect. No gameplay, GFX, workbook, export CSV, or unrelated localisation was changed.

## Scope and evidence reviewed

- All files under `docs/specs/023_sov_nuclear_bombs_specs/`.
- `events/023_soviet_nukes.txt`.
- `common/decisions/023_sov_nuclear_bombs_decisions.txt` and `common/decisions/categories/023_sov_nuclear_bombs_categories.txt`.
- The Event 23 achievement family in `common/achievements/chaos_redux_achievements.txt`.
- `common/scripted_localisation/023_sov_nuclear_bombs_scripted_localisation.txt`.
- Event 23 branches in the shared event-log, Event Details, settings, and debug scripted-localisation selectors.
- `localisation/english/023_soviet_nukes_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`, and the linked shared GUI localisation.
- `docs/events/023_sov_nuclear_bombs.md`.
- Current localisation, decision, completion, and spreadsheet handoffs under this plan folder.
- Required offline Paradox localisation and event/decision references and the relevant vanilla documentation and precedents.

## Audit result

### Missing keys

None.

- 210 distinct title, description, option, tooltip, achievement-tooltip, and custom-cost references extracted directly from the Event 23 event, decision, category, and achievement sources all resolve in English localisation.
- All 78 distinct decision or mission name references and all 78 description references resolve.
- Seven registered achievements have all 28 conventional `_NAME`, `_DESC`, `_tooltip`, and `_locked` keys. The shared eligibility tooltip also resolves.
- All Event 23 event-log, Event Details, evolution title/body/summary, super-event, settings, and debug selector return keys resolve.

### Duplicate keys

None across the English localisation set for the Event 23 event, news, decision, achievement, event-log, evolution, Event Details, and super-event key families.

The historical collision between `chaosx.nr23.120.d` and the refusal option is closed. The current refusal option uses `chaosx.nr23.120.refuse`.

### Scripted localisation

No current broken Event 23 scripted-localisation reference remains.

- The Event 23 file contains seven `defined_text` selectors and 45 static return keys. Every static return key resolves.
- Phase, posture, knowledge, site, target, deadline, and Event Details status selectors retain explicit fallback branches.
- Site and target event targets use the documented localisation namespace form without an `event_target:` prefix.
- The shared `GetEventsLogEventDetailDescription` selector now routes Event ID 23 to `sov_nuclear_bombs.event_details.description`.
- Shared evolution list, history, title, body, summary, and type selectors now contain Event 23 branches. The missing-selector limitation in the previous localisation handoff is therefore superseded.

### Dynamic text coverage and opportunities

Current dynamic coverage is complete for the accepted surface:

- The command category displays phase, selected site, selected target, configured active-family duration, usable-device count, readiness, integrity, posture, and public knowledge.
- Site and target selectors return actual event-target names when their targets exist.
- Deadline branches distinguish production, delivery training, command exercise, test, ultimatum, strike, retaliation, rail security, three breakaway stages, joint custody, dismantlement, and no active deadline.
- Five cost families use existing script constants in normal and blocked displays.

Remaining opportunity: the category deadline line reports the configured duration for the active mission family, while the ordinary decision mission supplies the live remaining-day countdown. A second countdown in the category header would require a reliable existing remaining-time value and was not invented in this localisation-only patch.

Remaining uncertainty: `sov_nuclear_bombs_selected_state` is a fallback in both site and target selectors. Current phase logic determines whether that duplication is meaningful. No selector change was made without a phase-to-field ownership contract.

### Cross-surface consistency

- The canonical event name remains `SOV Nuclear Bombs` in `chaosx.event_name.23` and the root event title.
- Event, option, report, decision, mission, achievement, super-event, event-log, Event Details, and evolution wording agree on a physical custody ledger, operational readiness, constrained release authority, coercion, verification, and nonterminal exchange.
- Public text does not reveal exact hidden authorization gates, AI weights, depot locations, or future thresholds before their public surfaces.
- Events 160, 161, and 162 now describe their actual script checks: moratorium accounting, reciprocal hotline stand-down verification, and settlement verification.
- Event 23 adds no localisation-owned technology or doctrine tree surface. The read-only technology inspect, render, and compare routes are exposed, but no standalone Technology Tree Viewer is present in the installed package. This is a package gap, not evidence of service failure.

### Spreadsheet wording handoff

The workbook was not edited. Its Event 23 Details and evolution prose are conceptually aligned but do not exactly mirror the current in-game Event Details and evolution body wording. The spreadsheet owner should use these final localisation keys and values if exact catalog parity is required:

- `chaosx.event_name.23`: `SOV Nuclear Bombs`
- `sov_nuclear_bombs.event_log.evolution_type`: `Nuclear Escalation`
- `sov_nuclear_bombs.event_log.detail`: `A Soviet atomic arsenal is governed through a reconciled custody ledger, staged command authority, verified delivery, coercive decisions, and limited exchange responses.`
- `sov_nuclear_bombs.event_details.description`: `The Soviet atomic arsenal is governed through production, testing, coercion, and disputed custody. Every weapon remains tied to a physical depot, a command authority, trained delivery crews, and a release order. A Soviet collapse may scatter the stockpile among successor authorities, but possession alone does not provide the knowledge or command structure needed to launch it. Any confirmed detonation can bring fallout, condemnation, and retaliation far beyond its target.`
- `sov_nuclear_bombs.evolution.i.title`: `The Wider Nuclear Race`
- `sov_nuclear_bombs.evolution.i.body`: `The Soviet breakthrough has become an international race. Reactor compounds, production batches, observers, and bomber patrols turn the hidden arsenal into a repeatable state program.`
- `sov_nuclear_bombs.evolution.ii.title`: `Coercive Doctrine`
- `sov_nuclear_bombs.evolution.ii.body`: `The arsenal becomes an instrument of political pressure. Selected demands can reach independent minor governments and eligible breakaways, but credibility, foreign backing, target behavior, and delivery evidence still shape the result.`
- `sov_nuclear_bombs.evolution.iii.title`: `Nuclear War Becomes Possible`
- `sov_nuclear_bombs.evolution.iii.body`: `A real exchange opponent exists. Retaliation windows, survivable command, hotlines, limited profiles, reserve preservation, and the first warning of a wider exchange now surround every major-power authorization.`
- `sov_nuclear_bombs.evolution.iv.title`: `Unrestrained Release`
- `sov_nuclear_bombs.evolution.iv.body`: `The Soviet command can prepare its widest response profiles. Even under unrestrained doctrine, a major first strike remains confined to an extreme strategic emergency, and a verified stand-down can still halt the order.`
- `sov_nuclear_bombs.evolution.summary`: `The Soviet nuclear escalation begins with one hundred guarded devices. As the crisis deepens, the arsenal and reactor network can expand, but custody, command authority, and verified delivery govern every physical action.`

### Encoding

`localisation/english/023_soviet_nukes_l_english.yml` remains valid UTF-8 with BOM after the patch. It contains no `:0` key declarations. The two linked English localisation files inspected for the canonical name and shared GUI also have UTF-8 BOM. No encoding concern remains.

## Prose-quality audit

### Vagueness

Before: events 161 and 162 described the wrong verification subjects, so the player could not tell which agreement was being reviewed.

After: event 161 names the hotline agreement and its reciprocal release-order pause. Event 162 names the target government's settlement and states the independence, capitulation, and continued-compliance checks.

### Bloat

No remaining Event 23 passage contains removable throat-clearing or a repeated summary that obscures its action. The replacement verification descriptions each lead with the review date and then state the conditions being checked.

### Obvious explanation

No remaining tooltip merely repeats its title or narrates an obvious click. Cost tooltips identify the resource families being consumed, while requirement tooltips state the blocked condition.

### Repetition

Before: event 160 used `stand-down` for moratorium verification, duplicating the distinct reciprocal stand-down terminology used by event 161.

After: event 160 says `Verify the moratorium.` and event 161 retains the reciprocal stand-down identity.

### Overcomplication

Before: the mismatched 161 and 162 descriptions mixed moratorium, custody, and discrepancy concepts that did not belong to their script checks.

After: each report uses one concrete subject and one bounded set of conditions.

### Style-rule repair

Before: `chaosx.news.230.d` used a staged `not ... but ...` contrast and the abstract phrase `report of capability`.

After: it states that the remote blast proves a working Soviet delivery capability and that governments are reassessing air defenses and war plans.

No em dash, sentence semicolon, or remaining `not ... but ...` construction was found in the Event 23 localisation file after the patch. No actual sourced quotation was normalized.

## Sourced quotation preservation

`chaosx_super_event.108.q` remains exactly `The first blow or series of first blows may be the last.`

The Event 23 research handoff attributes this quotation to General Leslie R. Groves's 2 January 1946 memorandum reproduced in FRUS document 600. Its words, punctuation, and capitalization were not changed.

## Changed files and keys

### `localisation/english/023_soviet_nukes_l_english.yml`

- `chaosx.nr23.160.a`
- `chaosx.nr23.161.t`
- `chaosx.nr23.161.d`
- `chaosx.nr23.161.a`
- `chaosx.nr23.162.t`
- `chaosx.nr23.162.d`
- `chaosx.nr23.162.a`
- `chaosx.news.230.d`

### Handoff

- `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_localisation_auditor_fresh_final_2026-09-05.md`

No scripted localisation was changed. No dynamic token, formatting code, cost, condition, target name, state name, duration, or consequence was removed.

## Behaviour and display before and after

- Event 160 option before: `Verify the stand-down.` After: `Verify the moratorium.`
- Event 161 before: claimed the moratorium was already verified and the arsenal sealed. After: presents a reciprocal stand-down review whose option evaluates the scripted success or failure conditions.
- Event 162 before: described an incomplete stand-down and a device-ledger discrepancy. After: presents the settlement review actually evaluated by the event option.
- News 230 before: described the demonstration through an abstract contrast. After: identifies the demonstrated delivery capability and concrete foreign response.

## Meaningful validation

- Automated direct-reference audit: 210 distinct Event 23 source references, zero missing.
- Decision and mission localisation audit: 78 name references and 78 description references, zero missing.
- Achievement audit: seven registrations and 28 conventional keys, zero missing.
- Scripted-localisation audit: seven selectors and 45 static return keys, zero missing; dynamic event-target return strings were inspected separately.
- Duplicate audit across English localisation: zero duplicate Event 23 keys.
- Encoding and key syntax: Event 23 YML retains UTF-8 BOM and contains no `:0` declarations.
- Targeted semantic comparison: events 160, 161, and 162 descriptions and options were checked against their current trigger and option-effect blocks.
- Read-only event inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics for the focused graph. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69eb2dd3a47e3a8b96e31c6b69f9f89a276ddf33054d366500a6988fdb3ee619/591ff5aa3750d254be1a2bfaf19bc822c7452d694fbbfabbcf27f89926bacda1/event-lint-a755267db440.json`.
- Read-only Event 23 options render completed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49a89fd6deddb50f63c4c95e64f1340a71ae4b3970febb946bb226d7e1c0ea41/671a239e2ea92a00daeed6be61b2611640a2ad38345258f668d54330a96752f4/event-options-a755267db440.json`.
- Shared Event Details inspection completed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/978f63285644b825b019f9bf7c9615fe68de9db73b919eec0df93d97174f5e98/2f4471aa5ce7c00665df1dd061455629366ac041eb4ee5d55f6c850dd4082524/gui-inspect.cad299f8340c96a1.json`.
- A populated Event 23 Event Details fixture rendered at 1920x1080 and 1366x768 with normal and long-text states. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/867ba134523f9466588bb092dd8d57065355d1df883ecf0217339d52422e92ca/54caf4925c20e281bec62c1e2bd24b3ba6013c0e4034cd52f92093ab584769d6/events_log_event_details_window-full.svg`.

## Remaining limits and skipped validation

- The Event Chain Viewer supplies source-linked graph and option diagrams, not the native event popup typography surface. Event-popup wrapping and clipping therefore remain outside this MCP route.
- `sov_nuclear_bombs_command_category` is an ordinary decision category, not a scripted-GUI window. A direct `hoi4.gui_inspect` request returned no inspected element for that name and reported the missing window inside globally truncated diagnostics. There is no exposed ordinary decision-category production renderer, so one-to-one category description wrapping and overflow remain unproven.
- The shared Event Details render succeeded, but scripted GUI visibility remains scenario-mocked and the renderer returned no standalone pass/fail layout checklist for the Event 23 text fixture. The artifact is retained as the available visual evidence rather than overstated as live-engine proof.
- HOI4 was not launched, as required.
- The workbook and export CSVs were not edited. Their exact-text mismatch is handed to the spreadsheet owner above.
- No commit was created because the Event 23 localisation file already contains substantial concurrent or pre-existing uncommitted work. Committing the whole file would capture changes outside this audit's ownership.

## Unresolved wording decisions

None for the patched event, news, decision, mission, achievement, event-log, Event Details, evolution, or super-event text.

The remaining deadline-countdown and dual-use selected-state questions are data-ownership questions, not unresolved English wording.

## Simplifications, omissions, and blockers

No player-facing key family was omitted from the audit. No gameplay or visual fallback was introduced. The only blockers are the absent ordinary decision-category renderer and the lack of a native event-popup typography route described above.

No design-depth plan was written because the findings were bounded localisation defects rather than a missing mechanic.
