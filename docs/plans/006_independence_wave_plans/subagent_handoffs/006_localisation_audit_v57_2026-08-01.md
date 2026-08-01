# Event 006 localisation audit handoff — 2026-08-01

## Scope and disposition

This is a read-only, source-level localisation audit of Event 006, with the Catalonia package (CAT) checked after the latest indentation and duplicate-key repairs. No gameplay, asset, or localisation source file was changed by this audit.

CAT localisation coverage is source-complete for the currently installed package. Event 006 has no missing or duplicate localisation keys in the audited surfaces and all audited files retain UTF-8 BOM encoding. The remaining hold is wording-policy related: the shared Event Details string currently exposes mechanical thresholds, rewards, timing, and raw constant tokens, and one crisis cost tooltip uses a semicolon where the event writing standard prefers a sentence break.

## Audited surfaces

- `localisation/english/006_*.yml` (all 44 Event 006 localisation files), including CAT, crisis, GUI, scenario, super-event, evolution, and report text.
- `common/decisions/006_*.txt`, `common/decisions/categories/006_*.txt`, `common/national_focus/006_independence_wave_focus.txt`, `events/006_*.txt`, and Event 006 scripted localisation/effect/trigger files.
- `common/decisions/006_independence_wave_catalonia_decisions.txt`, `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`, `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt`, `common/script_constants/006_independence_wave_catalonia_constants.txt`, and CAT AI strategy.
- `localisation/english/chaosx_gui_l_english.yml`, `localisation/english/chaosx_event_names_l_english.yml`, the Event 006 event-log/detail scripted localisation, and the exported Event 006 spreadsheet row in `docs/spreadsheets/chaos_redux_events_catalog.csv`.

## Required audit lists

### Missing keys

- None in the audited Event 006 surfaces.
- Decision references: 1,534 total, zero missing.
- Decision custom-cost base/tooltip/blocked coverage: 410 references, zero missing.
- Event references: 415 total, zero missing.
- National focus IDs: 208; all titles and descriptions resolve except the top-level `independence_wave_focus_tree_desc`, which is intentionally not defined for the tree root.
- Scripted-localisation `localisation_key` references: 237 total, zero missing.
- Event 006 custom getter references: 76, all defined.
- Selected Event 006 custom-effect tooltip references: 949, zero missing.

### Duplicate keys

- Current duplicate-key scan across all 44 Event 006 localisation files: zero duplicate groups.
- The six generic cost-key collisions seen in an earlier CAT snapshot are gone after the latest parent repair. Do not reintroduce CAT-specific copies of the shared cost keys.

### Scripted localisation issues

- No undefined Event 006 scripted-localisation getter or localisation-key reference was found.
- The Event Details mechanics are not a resolver failure; they are a display-policy issue because the string exposes implementation values that belong on crisis, decision, or scenario surfaces.
- `localisation/english/006_independence_wave_decisions_l_english.yml:236` (`independence_wave_cost_pre_wave_crisis_tooltip`) contains a semicolon between the equipment commitment and stability result. Replace it with a period if the event punctuation pass is accepted.

### Dynamic-text opportunities

- CAT effect tooltips remain valid static summaries, but `independence_wave_cat_project_failure_effect_tt`, `independence_wave_cat_depots_effect_tt`, `independence_wave_cat_guards_effect_tt`, `independence_wave_cat_assembly_effect_tt`, `independence_wave_cat_host_ledgers_effect_tt`, `independence_wave_cat_route_effect_tt`, `independence_wave_cat_patron_route_effect_tt`, `independence_wave_cat_sovereignty_effect_tt`, and `independence_wave_cat_network_effect_tt` could optionally expose the relevant CAT/shared constant magnitudes.
- Adding exact dynamic values is an optional UX improvement, not a coverage blocker. Keep the values on decision or effect surfaces and out of the premise-only Event Details field.
- No generic CAT route-name getter is currently required; other Event 006 packages use the same static route-summary convention.

## Cross-surface mismatch notes

- `localisation/english/chaosx_gui_l_english.yml:957` (`chaosx.events_log.window.event_details.independence_wave`) and spreadsheet row ID 6 `Details` are internally identical, but both violate the Event Details contract by listing automatic release counts, World Collapse pressure changes, crisis thresholds, the 120-day timing, exact cancellation/failure deltas, cooldown, bounded retry behavior, and raw `?constant:` tokens. Event Details should remain a premise and consequence summary; mechanics should remain on the crisis decision, mission, scenario, or report surfaces.
- CAT localisation is installed and route-specific, while CAT remains fail-closed and outside the compile-time attestation set. Its category is not exposed until CAT setup is complete, so the current text does not prematurely reveal a playable route.
- Event 006 evolution titles and bodies I–V match the spreadsheet export exactly. The main report (`chaosx.nr6.2.d`) uses dynamic presentation count and scripted actor/region/host/network text correctly.
- Earlier concerns about stale scenario counts, raw numeric GUI league phases, hidden route lists in evolution V, and network fallback punctuation are closed in the current tree.
- The CAT package documentation says “ten project decisions” while the source exposes eleven serialized project decisions including the protected-customs patron route. This is a gameplay/documentation audit item, not a localisation key failure, and remains with the owning agent.

## Encoding and syntax concerns

- All 44 Event 006 localisation files begin with the UTF-8 BOM (`EF BB BF`). Shared GUI and event-name localisation files also retain BOM encoding.
- No Event 006 localisation key uses the forbidden `:0` suffix.
- CAT keys currently have repaired indentation with no leading spaces; no current duplicate or indentation defect remains in the CAT file.

## Recommended fixes

1. Rewrite `localisation/english/chaosx_gui_l_english.yml:957` (`chaosx.events_log.window.event_details.independence_wave`) as a premise-only, in-world description that keeps the synchronized regional-rise, former-host remnant, unsettled borders, recognition struggle, governance choice, and rival-bloc context, while removing automatic counts, thresholds, exact deltas, cooldown/timing, bounded-retry text, and raw `?constant:` tokens.
2. Apply the same premise-only wording to the workbook source row ID 6 `Details` in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`; do not edit the export CSV directly.
3. Replace the semicolon in `localisation/english/006_independence_wave_decisions_l_english.yml:236` with a period or separate sentence.
4. If exact CAT outcome magnitudes are desired, add narrow dynamic values only to the listed CAT effect tooltips and validate the linked constants; do not broaden the CAT localisation surface or expose gated route names.

## Patch and validation record

- Changed files: none.
- Changed localisation keys: none.
- Dynamic localisation added or fixed: none.
- Behaviour/display before and after this audit: unchanged; this handoff records bounded recommendations for the owning agent.
- Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_v57_2026-08-01.md`.
- Static checks run: BOM scan for all 44 Event 006 YML files, aggregate duplicate-key scan, `:0` key scan, decision/event/focus/category/key-coverage scans, custom-cost pair scan, scripted-localisation/getter resolution scan, selected custom-effect tooltip scan, and evolution/spreadsheet text comparison.
- Skipped meaningful validation: no GUI render, event playback, save/load observation, or Hearts of Iron IV process launch. The parent requested a static localisation handoff, and live consumer validation belongs to the user.

## Unresolved wording decisions

- The owning agent must choose the final premise-only Event Details wording and whether the automatic ladder belongs on a separate scenario/report surface.
- The owning agent or spreadsheet worker must update the XLSX source and regenerate CSV if the Details rewrite is accepted.
- The owning agent must decide whether to expose exact CAT effect magnitudes dynamically and whether to include the one-semicolon punctuation cleanup in the next bounded patch.

## Simplifications, omissions, and blockers

- No localisation implementation was omitted inside the currently installed Event 006/CAT surface; all audited references resolve.
- The Event Details rewrite, workbook update, punctuation cleanup, and optional CAT dynamic magnitudes remain unpatched because this parent turn requested a read-only handoff and no broad edits.
- Runtime/save-load/player-owned decision observation and CAT admission are outside this localisation audit and remain with the owning implementation and QA passes.
