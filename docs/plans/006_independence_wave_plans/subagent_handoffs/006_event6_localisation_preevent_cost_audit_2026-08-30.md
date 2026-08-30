# Event 006 pre-event leakage and cost-localisation audit

Date: 2026-08-30

Mode: bounded localisation audit and patch

## Outcome

The retired pre-event Independence Wave surface remains absent. The current Event 006 allocator exposes no pre-event crisis category, mission, cost, queue, or early-request string, and package and overlay presentation remains gated behind committed Event 006 setup. The surviving uses of `crisis` and `pressure` in dedicated Event 006 localisation describe post-release founding problems, league conflict, former-host relations, route pressure, or explicitly launched scenarios. They are not pre-event warnings.

One redundant cost family was simplified. `independence_wave_cost_strategic_instant` displayed the same four charges as `independence_wave_cost_strategic` but added `Spend:` and `Capacity:` labels and a forced line break. Its normal and blocked rows now nest the authoritative compact strategic rows. No amount, icon, transport selector, affordability trigger, payment effect, decision identifier, or visibility rule changed.

## Changed files

- `localisation/english/006_independence_wave_decisions_l_english.yml`
- this handoff

## Changed keys

- `independence_wave_cost_strategic_instant`
- `independence_wave_cost_strategic_instant_blocked`

`independence_wave_cost_strategic_instant_tooltip` already nested the base row and remains unchanged.

## Before and after

- Before, the normal row prefixed the four authoritative charges with `Spend:` and `Capacity:` and split them across two lines. After, it resolves through `$independence_wave_cost_strategic$`.
- Before, the blocked row repeated the same structure and labels in red. After, it resolves through `$independence_wave_cost_strategic_blocked$`.
- The displayed stability, command power, convoy-or-train transport, and civilian-factory commitments remain identical.

## Audit lists

### Missing keys

None in the inspected Event 006 surfaces.

- 336 event title, description, and option references resolve.
- All 88 parsed Event 006 decision and category identifiers have name and description keys.
- All 227 actual Event 006 focus identifiers have name and description keys. The focus-tree container has its name key and does not require a description key.
- All 192 `custom_cost_text` consumers have base, `_blocked`, and `_tooltip` keys.
- All 230 Event 006 scripted-localisation result keys resolve.
- All 32 text and tooltip keys bound by `interface/006_independence_wave.gui` resolve.

### Duplicate keys

None. The 37 dedicated Event 006 English files contain 8,813 unique keys, with no duplicate Event 006 key elsewhere under `localisation/english`.

### Scripted-localisation issues

No missing result key or broken reference was found. The strategic-instant aliases use existing normal and blocked localisation keys and preserve the dynamic convoy-or-train selector.

### Dynamic text opportunities and blockers

- `independence_wave_cost_selected_formable_commit_blocked` cannot display the selected formation's exact blocked charge. Its only existing selector returns the normal-colour cost, while the fallback sentence uses implementation-facing `family` and `carrier` terms. Fixing this correctly requires a blocked scripted-localisation selector outside this localisation-only ownership.
- `Replicable Opening Confidence` is visible in `independence_wave_league_category_desc`. Source intentionally exposes the cross-generation value, but the accepted specification calls the evolution `Replicable Independence` and does not authorize a final player-facing name for this value. No invented replacement was applied.

### Cross-surface mismatch notes

No identifier mismatch was found between current Event 006 events, decisions, categories, focuses, scripted localisation, GUI bindings, and dedicated English localisation.

Three cost families remain mechanically incompatible with the four-cost localisation contract and cannot be made compliant by hiding charges in text:

- `independence_wave_cost_security_standard_factory`: five spendable types.
- `independence_wave_formable_commit_cost_revolutionary`: seven spendable types.
- `independence_wave_formable_commit_cost_military`: seven spendable types.

The owning decision implementation must simplify those payments before their localisation can meet the hard cost budget. `independence_wave_cost_patron_balance` also shows separate starting and later payments. Its two short labels are necessary under the current staged payment design, so they were not removed as cosmetic filler.

### Encoding concerns

None. All 37 dedicated Event 006 English files have UTF-8 BOM and an `l_english:` header. No indented or versioned Event 006 key remains.

## Prose-quality findings

- Vagueness: `Replicable Opening Confidence` remains an unresolved working-style value label because the accepted spec provides no final replacement.
- Bloat: the duplicated strategic-instant `Spend:` and `Capacity:` wrappers were removed. The staged patron-balance text remains because collapsing the stages would obscure when payment occurs.
- Obvious explanation: the strategic-instant labels repeated information already communicated by the icons and amounts and were removed.
- Repetition: the strategic-instant normal and blocked rows now reuse the authoritative strategic rows instead of maintaining duplicated charge lists.
- Overcomplication: no additional safe localisation-only reduction was found. The five- and seven-cost families require gameplay simplification rather than concealed charges.
- Style-rule repair: the 37-file scan found no em dash, sentence semicolon, placeholder, TODO, TBD, working-label marker, debug-only marker, or test-only marker. No sourced quotation was normalized.

## Sourced quotation preservation

The following quote-bearing strings were inspected and left unchanged:

- `chaosx_super_event.23.q`, the Woodrow Wilson Point XIV quotation.
- `chaosx_super_event.24.q`, the Hosea 8:7 King James Version quotation.
- `chaosx_super_event.24.a`, `They have sown the wind.`

All dynamic tokens and formatting codes in the changed cost family were preserved through nested authoritative keys.

## Meaningful validation

- `.tools/audit_event6_allocator.py` passed and reported the pre-event crisis surface retired with no category, mission, cost, or queue.
- `.tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix.
- `.tools/audit_event6_scenario_matrix.py`, `.tools/audit_event6_form16.py`, `.tools/audit_event6_flags.py`, and `.tools/audit_event6_country_api.py` passed their Event 006 source contracts.
- The post-patch cost scan found 192 consumers, zero missing triplet keys, zero static displayed numeric amounts without constants, and zero unapproved copied tooltip rows.
- HOI4 Event Chain Viewer inspect/render completed partially for `chaosx.nr6.1`. Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c5e729e83171409d5dd8f555d162a0acf8a9180f496160a8fbcc3047ce9500b/ad5e22eec79d99e6321698b8e31398312213007140db7093f592e2a16349ac08/event-trace-ac2516cf55a8.json`. Options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5568e20d856eed5d1b0bf8fb7cd003e8b083562e898eadb8327688d82931944/51d05811a1a28d4519a4b997d17c890502abdfa921b221b2987096f447683365/event-options-ac2516cf55a8-manifest.json`.
- HOI4 GUI inspect/render completed for `independence_wave_status_window` at 1920x1080 and 1366x768 in normal, long-text, and missing-localisation states. The renderer reported no text overflow, missing localisation, button-label centering problem, background-edge crossing, or resolution drift. Validation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45ca7eeec3e63b6301feebec8ffd8a618d71f4bbd61997844514c835d6a9c72e/b544a87960f01ab16cf26de8dc8a23988bce705d0ed43a2c4abe30bdeb805493/independence_wave_status_window-validation.json`. Production render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/783f12be501c602a718675258db328437b818ea3e4b4b771206634b95a9641a3/bec52931f310d6ae719c8de77cc52cf2664e37bbad57d5360e524d1b5f7cc456/independence_wave_status_window-cropped.png`.

The GUI validator also reported non-localisation layout and animation-fallback warnings. They are outside this localisation-only patch and do not indicate text overflow.

## Skipped meaningful validation

No production decision-list renderer is exposed by the installed MCP package, so the 192 custom-cost rows could not be visually rendered in their decision consumers. Source alignment and dynamic-token checks are not treated as equivalent visual evidence.

Live in-game display is user-owned and was not attempted.

## Unresolved wording and ownership decisions

- The owner must choose a final source-backed label for `global.independence_wave_replicable_opening_confidence` if the value remains visible.
- The decision owner must simplify the five- and seven-cost families rather than asking localisation to conceal extra charges.
- A blocked selected-formable cost selector is needed if exact red costs should replace the current implementation-facing fallback sentence.

## Simplifications, omissions, and blockers

No pre-event indication, gameplay cost, transport alternative, route, event, dynamic token, sourced quotation, or hidden outcome was simplified. The unresolved cost-budget defects and missing blocked selected-formable selector remain explicit blockers outside this localisation-only ownership. No fallback was used.

## Plan handoff

None. No new mechanic was designed or inferred.
