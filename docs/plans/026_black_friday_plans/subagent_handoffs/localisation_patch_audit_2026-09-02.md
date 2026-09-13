# Event 26 localisation patch and bounded audit — 2026-09-02

## Outcome and ownership

Patched three localisation/scripted-localisation files only.
No gameplay, GUI layout, GFX, workbook, or generated CSV was edited.
Other agents' changes were retained.
This is not universal cost-coverage acceptance or live validation, and Event 26 is not declared complete.

Read AGENTS.md, all files in `docs/specs/026_black_friday_specs/`, the events, decisions-missions, and subagents skills, the required offline wiki core pages plus interface/scripted-GUI references, and relevant installed vanilla documentation/precedents.
No new design mechanic or improvement plan was introduced.
This handoff supersedes the scoped completion claims in `subagent_handoffs/localisation_final_audit_current.md`, whose key inventory, normal Fury resolution claim, and claim that GUI SVGs omit text are stale.
The SVGs contain rendered glyph paths and were rasterized and visually inspected.

## Changed files and exact keys

### `localisation/english/026_black_friday_l_english.yml`

- `chaosx.nr26.2.d`
- `black_friday_sale_desc`
- `black_friday_sale_evolution_i`
- `black_friday_sale_evolution_i_desc`
- `black_friday.event_detail.premise`
- `black_friday.event_detail.status.reserved`
- `black_friday.event_detail.status.active`
- `black_friday.event_detail.status.expired`
- `black_friday.event_detail.status.disabled`
- `black_friday.event_detail.status.eligible`
- `black_friday.event_detail.evolution`
- `black_friday.evolution.1.body`
- `black_friday.evolution.1.summary`
- `black_friday.history.50`
- `black_friday.history.75`
- `black_friday.cost_source.line`
- `black_friday.cost_source.rounding`
- `black_friday.cost_source.requirements`
- `universal_cost.quote.ordinary`
- `universal_cost.quote.final`
- `universal_cost.quote.blocked`
- `chaosx.events_log.events.na_reason.black_friday_active`
- `026_black_friday_five_departments_DESC`
- `026_black_friday_five_departments_tooltip`

### `localisation/english/007_random_expansion_l_english.yml`

Added four normal-price leaf keys:

- `fury_terminal_reserves_cost_text_normal`
- `fury_terminal_reserves_cost_text_normal_blocked`
- `fury_terminal_fronts_cost_text_normal`
- `fury_terminal_fronts_cost_text_normal_blocked`

### `common/scripted_localisation/026_black_friday_scripted_localisation.txt`

Changed `GetFuryTerminalReservesCostText`, `GetFuryTerminalReservesCostTextBlocked`, `GetFuryTerminalFrontsCostText`, and `GetFuryTerminalFrontsCostTextBlocked`.
Their ordinary-price branches previously selected the wrapper key that called the same selector again.
They now calculate positive display-only temporary values from existing negative spend constants and select the four new leaf keys.
Sale branches and actual payments are unchanged except that the terminal sale leaves were aligned to the ordinary terminal display order, with each amount preceding its icon.
The ordinary values resolve to reserves: 30 command power, 1,000 manpower, 600 infantry equipment, 40 support equipment; fronts: 25 command power, 15 army experience.

## Prose and dynamic-text changes

- Vagueness: replaced “every positive cost keeps its smallest payable unit” with explicit rounding and non-free purchase wording; replaced “material or capacity commitment” with supplies or factory capacity.
- Bloat: shortened status strings and the cost-source label; the report separates its concrete scene from the purchase rules.
- Obvious explanation: removed “Disabled: excluded from event selection” and repeated label explanations from the narrow metadata/history rows.
- Repetition: the evolution idea description shares the ordinary sale description; the achievement tooltip reuses its description; the spare evolution detail key aliases the canonical evolution body.
- Overcomplication: the premise no longer recites selection thresholds and an implementation “snapshot”; it describes shops, government orders, and the people making purchases.
- Style repair: replaced abstract “intelligence desks” with intelligence officers and removed technical “ordinary payable cost” phrasing from the generic quote labels.
- Dynamic text: the evolution idea title reads the active percentage; evolution requirements/rate and achievement category count read existing constants.
- Historical rows remain explicitly 50%/75%, selected from stored history payload, rather than showing today's global rate.
- The three-line history copy became two lines without dropping sequence, date, event ID, type, event name, percentage, global scope, or duration.

Existing dynamic tokens and formatting were retained or deliberately replaced by equivalent aliases/dynamic constant lookups.
New calculation-only terminal display tokens were added.
No sourced or attributed quotation occurs on the inspected Event 26 surfaces, and none was changed.
“Quote” in the cost helpers means a price quotation, not attributed prose.

## Audit results and source consumers

- Missing localisation keys: none among the 44 Event 26 keys and 157 localisation-key references in its scripted-localisation file.
- Duplicate keys: none for that bounded key set across English localisation.
- Scripted localisation: four recursive terminal normal/blocked branches fixed; the scoped selector/alias graph is now acyclic.
- Encoding concerns: none in the two changed YAML files; strict UTF-8 decoding succeeds and their BOMs were retained.
- Stale desert identity: no matches in runtime localisation, scripted localisation, or events for `026_industry_to_desert`, `Desert Industry`, `Move Industry to desert`, `Operation Desert Forge`, `GFX_report_event_desert`, or `desert question`.
- Report consumption: `events/026_black_friday.txt` keeps hidden dispatcher `chaosx.nr26.1` and consumes `.2.t`, `.2.d`, and `.2.a` in the human report.
- Event/debug/settings names resolve ID 26 to `chaosx.event_name.26` (“Black Friday”).
- Shared event-log selectors consume the premise, global scope, status, evolution title/body/summary, and payload-specific history rows.
- The status is appended to `chaosx.events_log.window.event_details.entry_meta_cluster`, not the tertiary metadata line described by the stale audit.
- The shared list weight selector directly handles active, reserved, disabled, fired, and unavailable states; `GetBlackFridayEventListStatus` itself has no caller.
- Idea `_desc` keys and achievement `_NAME` keys have implicit engine consumers and were not treated as dead keys.

## Remaining gaps and recommendations

1. **Resolved Fury command-power quote constants.**
   The terminal-reserve and terminal-front quote paths now use the defined positive gate constants `fury_decision_cost.terminal_reserves_cp_gate` and `fury_decision_cost.terminal_fronts_cp_gate`, while payment continues to use the matching negative spend constants.
   The remaining sale-price risk is owner-level display/payment and live validation, not an undefined constant.

2. **Generic quote and blocked presentation remains owner-limited.**
   The active sale idea now consumes `black_friday.cost_source.line`, `.rounding`, and `.requirements`; `black_friday.cost_source.name` and the generic `universal_cost.quote.*` keys remain available for future owner panels.
   The generic quote values still use integer formatting without resource-specific units/icons, and `Requirements not met.` cannot identify the failed requirement without an owner-supplied reason.
   Wire resource-aware quotes and specific blocked reasons in the remaining owning consumers, then verify displayed cost against payment.
   The shorter generic label “Payable” intentionally does not attribute every possible cost source to Black Friday.

3. **Other orphan presentation hooks.**
   No caller was found for `black_friday.event_detail.evolution`, `chaosx.events_log.events.na_reason.black_friday_reserved`, `chaosx.events_log.events.na_reason.black_friday_active`, or `chaosx.events_log.detail.status.global`.
   Retained them because parent work is ongoing; either wire them intentionally or remove them with that integration.
   The live shared status/weight branches already consume their separate keys.

4. **Sale display context still needs verification.**
   Existing Fury sale leaves use `black_friday_fury_display_*` temporary values prepared by affordability helpers.
   This pass did not prove availability of every temporary value in every tooltip evaluation path, per-resource red colouring, or quote/debit agreement for every adapter. Terminal blocked leaves still colour the whole bundle because the shared blocked-text entry does not expose whether the failure is a resource shortage or an unrelated route/target requirement.
   No universal/native cost coverage claim is made.

5. **Mirrored documentation/catalogue wording is synchronized for the current source snapshot.**
   The in-world premise, evolution body/summary, and achievement wording are mirrored in the authoritative workbook and refreshed export CSVs.
   The workbook row remains `Needs Testing` until live validation, and the current custom-cost inventory has since been reconciled to 2,224 trigger and 2,225 text references across 81 Chaos Redux files.

6. **Visual and runtime acceptance remains bounded.**
   Production renders prove the inspected text areas below, not the full event-log interaction, every state, every resolution, or the native human-report popup.
   The isolated detail render also showed overlapping unrelated bottom map/member controls because their visibility was not supplied in that isolated scenario.
   Do not accept the whole panel from that artifact; validate the containing shared scripted-GUI state before any layout change.
   The earlier automatically generated detail scenario selected Event 51, so it was rejected as Event 26 evidence.
   The GUI calls returned `validation.passed = false` and wire-budget warnings; no overall renderer validation pass is claimed.
   No ordinary decision-tooltip render route was exposed by the installed MCP tool inventory.
   The event-chain view is not a native report-popup overflow check.
   No live game was launched.

## Meaningful validation and evidence

The task-specific source audit checked actual selector targets, aliases, wrapper recursion, consuming references, stored-history payload selection, and normal terminal arithmetic against spend constants.
The following read-only production MCP evidence was obtained.
Explicit GUI scenarios substituted resolved Event 26 strings for geometry review; they do not prove runtime localisation evaluation.

- History row: `events_log_history_entry_generic`, 1920×1080, 1× UI scale, normal state, sequence 999/date 1936.12.31/type Minor Fire-Once/75% sale.
  The new two-line copy fits the 435×38 text area and its background.
  The old three-line copy was supplied as the comparison scenario.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40a862bbd0b75a57d72cf17b198bacdd0b5e6f3053e36caa6c5a66beb13b2115/17d8e6de75f253b14681d8c88768c7987c0a4876475315516a05b61cd557d5c1/events_log_history_entry_generic-full.svg`

- Event detail entry: explicit active 75% copy, with reserved copy as a related scenario; requested 1920×1080 and 1366×768 at 1× UI scale.
  The returned active artifact was inspected: the premise and active scope/status line fit their text areas.
  The wire-limited response exposed one artifact, so separate reserved/resolution coverage is not claimed.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/616bbb4cdad1c604902964bfb3ee049db6e842858e3882c21908c6e18d3f2354/a6aa3b66ece6f645347934017a9e344cdf3820c5c02ea42868cfaf97ad05d8f7/events_log_event_detail_entry-full.svg`

- Evolution detail: explicit actorless, portraitless `events_log_evolution_details_window_wide`, 1920×1080 at 1× UI scale.
  Title, summary, and complete body fit their backgrounds without visible text clipping.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6553bcdfb74a6c24278caa5aa2e2a9909db17826c4723499184a7db413ef4aa9/b884246c569eabea9d9135ffc4651b36a5d292baa704accc284b2d8e68007381/events_log_evolution_details_window_wide-full.svg`

- Event inspection: narrow trace of `chaosx.nr26.1`; helper expansion was bounded, so it does not prove the lifecycle.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13a1766dc4718d16260686022fc4d4d680621f5b3e6e88ddfd1fbc4d6002e010/3f6b39b013e2d820163a1387917bd217b74c8c24b74d27e2f611ddfb0114f83f/event-trace-65f53c2f4a09.json`
- Human-report event options render selected `chaosx.nr26.2` and its option; the hidden refresh helper was unresolved in this bounded graph.
  Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7475c3261c19404920518bec54b47fe42304d8b82154a60d8b6fef374b35fd81/f95a18eb5d4a6ed142286054301f7e55e9620b55580749eece5a19522777dacd/event-options-65f53c2f4a09.json`
- Event comparison attempted against revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`; exact blocker: `EVENT_REVISION_NOT_CACHED: Requested event graph revision is not cached`.
  No comparison success is claimed.

## Handoff status

Localisation fixes above are implemented; parent gameplay, quote-consumer, catalogue, and acceptance follow-ups remain open.
No feature was simplified to claim completion.
No commit was made: these files overlap the parent's unfinished, dirty implementation, and the remaining acceptance blockers must not be represented as a completed Event 26 plan.
