# Event 006 Residual Localisation Cleanup Handoff

Date: 2026-08-30

Owner: `chaosx_localisation_auditor`

Scope: Residual player-facing localisation for Event 006, with no gameplay, category, pre-event pressure, or shared UI redesign.

## Outcome

The residual audit found one overloaded five-resource decision cost, five Statehood Ledger panel strings that overflowed their production-render bounds, two implementation-facing GUI tooltips, and a cluster of SCN-008 transaction and rejection messages written in source-facing terms. The patch keeps all mechanics, costs, dynamic values, event identifiers, and route conditions unchanged.

The source workbook and generated CSV exports were not edited. The Event Details text, Liberations cluster text, and SCN-008 catalog description already match their current runtime counterparts, and none of the patched keys is a catalog-mirrored description.

## Changed files and keys

### `localisation/english/006_independence_wave_decisions_l_english.yml`

- `independence_wave_cost_security_standard_factory`
- `independence_wave_cost_security_standard_factory_blocked`

The old cost presented five commitments in one uninterrupted row. The new display separates four immediate expenditures under `Spend:` from the civilian factory commitment under `Commit:`. Both normal and blocked forms preserve the same five constant references and five icon tokens. The existing `_tooltip` alias remains unchanged.

### `localisation/english/006_independence_wave_gui_l_english.yml`

- `independence_wave_status_gui_refresh_tt`
- `independence_wave_status_gui_toggle_animation_tt`
- `independence_wave_status_gui_government_panel`
- `independence_wave_status_gui_recognition_panel`
- `independence_wave_status_gui_security_panel`
- `independence_wave_status_gui_league_panel`
- `independence_wave_status_gui_ambitions_panel`

The refresh and animation tooltips now describe player-visible results instead of authored ledgers, panels, states, and frames. The five panel summaries retain their distinct route and institution meaning in shorter sentences that fit the production render.

### `localisation/english/006_independence_wave_scenario_l_english.yml`

- `chaosx.scenarios.launch_status.independence_wave.presentation_pending`
- `chaosx.scenarios.launch_status.independence_wave.transaction_busy`
- `chaosx.scenarios.launch_status.independence_wave.ready`
- `chaosx.triggerable_scenarios.80.b`
- `independence_wave_scenario_summary_outcome_committed`
- `independence_wave_scenario_summary_outcome_failed`
- `independence_wave_scenario_transaction_committed`
- `independence_wave_scenario_ledger_category_desc`
- `independence_wave_scenario_reject_state_reserved`
- `independence_wave_scenario_reject_reservation_group_taken`
- `independence_wave_scenario_reject_unsafe_instantiation`
- `independence_wave_scenario_reject_invalid_scope`
- `independence_wave_scenario_reject_stale_plan`
- `independence_wave_scenario_reject_aligned_array_failure`
- `independence_wave_scenario_reject_insufficient_pool`
- `independence_wave_scenario_reject_protected_state_mismatch`
- `independence_wave_scenario_reject_unknown`

The old strings exposed implementation concepts such as synchronized setup, transaction preparation, final safety review, scope verification, stale plans, and aligned arrays. The replacements explain declarations, changing borders, competing regional claims, viable governments, safe homelands, and protected host remnants in world-state terms. Every dynamic counter, country name call, and scripted-localisation call in the ledger remains intact.

## Audit results

### Missing keys

None in the bounded surfaces. All 192 Event 006 `custom_cost_text` consumers resolve base, `_tooltip`, and `_blocked` keys. All 871 checked Event 006 decision and category identifiers resolve base and description keys. All 393 Event 006 text-producing scripted-localisation references resolve against repository localisation. A further 100 `GFX_independence_wave_*` `localization_key` values are sprite identifiers and were correctly excluded from the text-key result.

### Duplicate keys

None among the 8,813 keys parsed from the 37 dedicated Event 006 English localisation files. No duplicate `defined_text` names were found in the Event 006 scripted-localisation surface.

### Scripted-localisation issues

None found. The audit found no unresolved Event 006 text key, broken scripted selector call, or inconsistent selector name. Engine-provided `GetNameDef` and `GetNameDefCap` calls were treated as engine methods rather than repository keys.

### Dynamic text opportunities

No safe missing dynamic value was identified. Existing constants, counters, country-name calls, state-derived entries, costs, route labels, and scripted selectors already cover the relevant values. The patch preserves them rather than replacing them with static prose.

### Cross-surface alignment

- The Event Details Independence Wave text matches the Event 006 catalog Details field.
- The Liberations cluster runtime text matches the exported cluster catalog text.
- The SCN-008 runtime description matches the scenario catalog row.
- No patched key changes a catalog-mirrored description, evolution detail, cluster detail, or event-detail paragraph, so a workbook update and CSV export were unnecessary.

### Encoding

All 37 dedicated Event 006 English localisation files retain UTF-8 BOM encoding. The three changed files begin with `EF-BB-BF`. No `:0` localisation key form was introduced.

## Prose-quality repairs

### Vagueness

The scenario failure strings now name the concrete obstacle: changed borders, an unavailable homeland, an unidentifiable government or host, a competing claim, or the loss of a protected remnant.

### Bloat

The five Statehood Ledger panel summaries were reduced to the information needed to distinguish government, recognition, security, league, and ambition surfaces. The cost display is split by resource behavior instead of stretching five items across one line.

### Obvious explanation

The animation tooltip no longer explains that an animation was authored frame by frame. The refresh tooltip now states what information is updated and when that is useful.

### Repetition

Repeated formulations about a coordinated or synchronized release were replaced with concise references to declarations and the independence wave.

### Overcomplication

Long source-facing phrases about release preparation, scope validation, and aligned records were replaced with direct statements about governments, homelands, borders, and hosts.

### Style-rule repair

No em dash, sentence semicolon, prompt fragment, implementation history, or tuning note remains in the changed strings. Route identity and consequence language remain specific rather than generic.

## Sourced quotations and dynamic tokens

The approved Woodrow Wilson Point XIV and Hosea 8:7 KJV quotation surfaces were inspected but not edited. Their wording, omission marks, attribution, and formatting remain verbatim. No sourced quotation was normalized or repunctuated.

All dynamic tokens in edited strings were preserved. The normal and blocked five-resource cost strings have exact constant and icon token parity after the formatting change.

## Validation evidence

- `python -B .tools/audit_event6_scenario_matrix.py` passed every SCN-008 matrix cell and listed edge case after the wording changes.
- `python -B .tools/audit_event6_gui_matrix.py` passed the five mutually exclusive tabs, all recognition, dependency, league, and formable animation frames, cleanup paths, and static/animated siblings.
- A focused localisation audit parsed 37 files and 8,813 keys with no missing BOM, duplicate key, missing cost family, or missing text-producing scripted-localisation reference.
- The HOI4 MCP event inspection for `chaosx.nr6.1` completed without a blocker. It returned `EVENT_INSPECTED_PARTIAL` only because the large-workspace helper and lifecycle projection was deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25768bc2765a9952454061243a07ee08498c7761184fdc25ce4163f8e7423c98/b2ff35a3115d5fd3d984d08018aa0aa2a9b2007c3bc23c001f6ab075d0477c3e/event-lint-55c38793c7fb.json`.
- The pre-change Statehood Ledger production render found five `GUI_TEXT_OVERFLOW` defects in the five panel strings. Pre-change validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1169d64cd39cb5c24692ab02e250d724bcb1d89c1a45dc366df2a91188718913/569ab508dbe5ce8253f283f3ead103157a027fe926c94b7be5aad041c44a2c84/independence_wave_status_window-validation.json`.
- The post-change production render reports no text overflow or missing localisation. Post-change validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f245c63a9af7aaa0e4e26653f2973337040ffaf7bc1dc086b7726c4ef2aa8a53/d072f5088d91f9a5fd4e642e13d25b1b8cbe3e0a98ca9036dcef7999629d9106/independence_wave_status_window-validation.json`.

## Skipped meaningful validation and residual uncertainty

The ordinary decision-list cost label has no available HOI4 MCP rendering route, so the revised five-resource cost is source- and token-verified but not visually rendered in its final decision consumer. The underlying design still commits five distinct resource types. Changing or removing one would be a gameplay decision outside this localisation scope, so the display was clarified without concealing a requirement.

The post-change Statehood Ledger render still reports tiny subpixel icon clipping and an animated-static-fallback diagnostic. Both concern existing icon assets or GUI state wiring, not the patched text, and remain outside this bounded localisation tranche.

No unresolved wording choice remains. No fallback, mechanic simplification, new route lore, or hidden mechanic was introduced. This handoff is the only plan document created by the tranche.
