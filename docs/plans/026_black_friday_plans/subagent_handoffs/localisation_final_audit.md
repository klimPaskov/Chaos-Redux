# Event 026 Black Friday Localisation Final Audit

## Scope and references

This audit covered only Event 026 Black Friday localisation and its shared Event Log and Event Details scripted-localisation consumers. I read the complete `docs/specs/026_black_friday_specs/` package, the Event 026 event/effect/scripted-localisation/localisation sources, the shared Event Log effect and scripted-localisation files, the shared GUI localisation, achievement definition, debug/settings mappings, and the Event Log scripted GUI/interface consumers. I also consulted the required offline Paradox wiki pages, relevant installed HOI4 documentation, and vanilla scripted-localisation precedents.

The `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skills governed the audit. No design-depth gap required an improvement-loop plan.

## Changed files

- `localisation/english/026_black_friday_l_english.yml`
- `common/scripted_localisation/026_black_friday_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `docs/plans/026_black_friday_plans/subagent_handoffs/localisation_final_audit.md`

No gameplay logic, spreadsheet content, assets, achievement script, shared GUI layout, shared GUI localisation, debug/settings mappings, or shared Event Log effects were edited.

## Exact findings and fixes

### Missing and duplicate keys

- Missing Event 026 keys: none. Thirty-one scoped Event 026 references resolve to localisation keys.
- Duplicate keys across `026_black_friday_l_english.yml`, `chaosx_gui_l_english.yml`, and `chaosx_event_names_l_english.yml`: none.
- Wrong namespace findings: none. `chaosx.event_name.26` consistently resolves to `Black Friday` in the Event list, debug selector, settings selector, and last-fired-event selector.

### Scripted-localisation issues

- Fixed a semantic inversion in `chaosx.nr26.2.d`, `black_friday.event_detail.status.active`, and `black_friday.cost_source.line`. `global.black_friday_discount_percent` stores the percentage taken off, but the old copy described it as the percentage still payable. A 75 percent discount therefore appeared as a 75 percent payable cost. The revised copy consistently says `75% off` or `reduced by 75%`.
- Added payload-specific Event History detail branches to `GetEventsLogEventDetailDescription`. A payload equal to `constant:black_friday_event.baseline_payment_ratio` now selects `black_friday.history.50`; the evolution payment ratio selects `black_friday.history.75`. Catalogue/Event Details records with payload zero continue to select `black_friday.event_detail.premise`.
- Corrected `GetBlackFridayEventListStatus` from the nonexistent/stale `global.events_log_view_event_id_entries` array to `global.events_log_events_view_event_id_entries`. Added explicit disabled and fired branches.
- Reordered Event Details status priority so a fired event that is currently disabled displays `Disabled` rather than the stale `Fired` state. Active and reserved states remain higher priority.
- Added a leading line break to each nonempty Event 26 status value. The shared tertiary label concatenates `[GetEventsLogDetailContextLine][GetBlackFridayEventDetailStatusLine]`; the old values could run directly into the fired-date/log-number context.

### Dynamic localisation

- Preserved `[?global.black_friday_discount_percent|0]` in the report, active idea, Event Details active state, and cost-source line.
- Added no new gameplay variable. The history description now dynamically follows the already-recorded payment-ratio payload.
- `black_friday.cost_source.line`, `.rounding`, and `.requirements` are defined, mechanically sound, and consumed by the active sale idea description. `black_friday.cost_source.name` remains a standalone label, while the Event Details premise states the source scope, baseline rate, expiry, ordinary-requirement rule, modifier rule, and positive-cost rounding rule directly.

### Cross-surface consistency

- Event title, event-name mapping, debug/settings mappings, Event list status names, Event Details status, idea names, evolution title/body/summary, history payload descriptions, and achievement text now consistently use `Black Friday`, a 50 percent baseline discount, and a 75 percent Chaos Tier evolution discount.
- The event catalogue workbook and CSV exports were deliberately not changed. The revised in-game prose is therefore no longer a verbatim mirror of older spreadsheet wording in any row that copied the former report, detail, evolution, or achievement prose. This is an expected cross-surface mismatch under the assigned prohibition on spreadsheet edits and needs a later spreadsheet-owner pass.
- No active Event 26 source contains stale desert, sandstorm, or unrelated disaster wording. Historical baseline handoffs under this plan directory still mention the earlier desert-content audit as dated evidence; those records were not rewritten.

### Actorless history and evolution rows

- Activation history explicitly records `events_log_system_actor = 0`, `events_log_system_has_actor = 0`, `events_log_system_secondary_actor = 0`, and `events_log_system_has_secondary_actor = 0` before calling the shared recorder.
- Evolution recording explicitly sets `events_log_evolution_has_actor = 0`; the shared effect also defaults absent evolution actors to zero.
- The shared default-actor effect explicitly exempts Event 026 and Event 027 as global system records.
- Event 26 history prose itself says `A global Friday sale`, so the global context remains visible even though the shared history-details GUI hides its actor line when `has_actor = 0`.
- `black_friday.scope.global` has a scripted-localisation branch, but the current GUI actor-line visibility condition prevents that branch from being displayed for an actorless record. Correcting that would require a shared scripted-GUI behavior change and was outside this localisation-only scope.

### File encoding

- `localisation/english/026_black_friday_l_english.yml`: UTF-8 BOM present after patch.
- `localisation/english/chaosx_gui_l_english.yml`: UTF-8 BOM present and unchanged.
- `localisation/english/chaosx_event_names_l_english.yml`: UTF-8 BOM present and unchanged.
- No `:0` localisation version suffixes were introduced.

## Changed keys

- Event report: `chaosx.nr26.2.t`, `chaosx.nr26.2.d`, `chaosx.nr26.2.a`.
- Active ideas: `black_friday_sale_desc`, `black_friday_sale_evolution_i`, `black_friday_sale_evolution_i_desc`.
- Event Details: `black_friday.event_detail.premise`, all six nonempty `black_friday.event_detail.status.*` keys, and `black_friday.event_detail.evolution`.
- Evolution: `black_friday.evolution.1.title`, `.body`, `.summary`.
- Cost display: `black_friday.cost_source.line`, `black_friday.cost_source.rounding`, `black_friday.cost_source.requirements`.
- Achievement: `026_black_friday_five_departments_DESC`, `026_black_friday_five_departments_tooltip`.
- Scripted selectors: `GetBlackFridayEventDetailStatusLine`, `GetBlackFridayEventListStatus`, and the Event 026 branches in `GetEventsLogEventDetailDescription`.

## Display behavior before and after

- Before: a 75 percent discount could display as `75% of the ordinary payable cost`. After: every dynamic percentage is explicitly the amount off.
- Before: History details always showed the generic 50 percent premise. After: recorded 50 percent and 75 percent activations select their matching history sentence.
- Before: the Event 26 list helper read the wrong backing array and could only return active, reserved, or unavailable. After: it reads the Events-tab array and can return active, reserved, disabled, fired, or unavailable.
- Before: Event Details could concatenate the context and state without separation. After: the Event 26 state starts on its own line.
- Before: report, evolution, rounding, and achievement text used internal language such as `registered`, `snapshot`, `minimum nonzero rounding`, `registered quantum`, and `final-registry primary cost families`. After: the text names the concrete sale, the percentage off, the daily expiry, the smallest payable unit, and the five required cost categories in player-facing language.

## Prose-quality repair summary

- Vagueness: replaced `The Price Sheet Turns`, `The Deep Cut`, and abstract market-tightening language with concrete ministry price sheets, the Friday rush, and `Seventy-Five Percent Off`.
- Bloat: condensed repeated registry and framework qualifications while retaining the requirements, expiry, modifier, cooldown, and rounding rules that affect player decisions.
- Obvious explanation: removed labels that merely announced `Evolution I` and made the idea/evolution names state the actual stronger discount.
- Repetition: consolidated repeated lists where a shorter statement preserved the same constraint; retained the full exception list only in the achievement tooltip where it changes eligibility.
- Overcomplication: replaced `minimum nonzero rounding`, `registered quantum`, and `final-registry primary cost families` with `smallest payable unit` and `cost categories`.
- Style-rule repair: removed the Event 26 em dash and avoided semicolons, implementation history, tuning notes, staccato fragments, staged contrast formulas, and raw trigger language.

## Sourced quotations

No inspected Event 026 surface contains a sourced or attributed quotation. No quotation text was changed.

## MCP inspection and rendering evidence

- Narrow Event 026 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e4facf48c0bcfdb0332f5bd4e16ac5b37317f038f4675f033b5f4020a68cd5a/86e56b1c4571d3ba7e8413b824987683c3ea5eac6f81f69edf160999ddddd97e/event-trace-92dcbf81468a.json`.
- File-targeted Event 026 scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1930141e98832968c12bec2cfb67c66b89adf55b715e10e34766854e5da2f035/db37b9eea69174095bd3547f973e42e380363e23c47da598750771fb944c9eb9/event-scan-7a11a434d50b.json`. The server returned `EVENT_INSPECTED_PARTIAL` because large-workspace helper and lifecycle passes were deferred; the complete artifact retains the blocking diagnostics.
- Event Details production render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82b2973928e0ea5c302bfb4d31422ebb687d6315cb2b1f2ec8d80c59c7d1e5f2/b1b42561af1e3f30445af571791e68d0901831f0781c35eefb38825553bb6728/events_log_event_details_window-full.svg`.
- Event-list production render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329f59d19feda3e8c5a3245fc23a018a4112c756142aa356257b4edddb14ade0/150e136419c28684a7b2a0599d2a4e06af7a006ee61cb322a316c27b2153d41a/events_log_events_content_window-full.svg`.
- The Event-list render returned `GUI_RENDERED` with no blocker, but the wire response was truncated and its validation object contained no checks. The linked SVG is the retained evidence; it is not sufficient to claim Event-26-specific state substitution because the renderer accepted only a synthetic scenario identifier, not explicit Event 26 variable bindings.
- Event source rendering timed out after 180 seconds. GUI inspection of `events_log_event_details_window` also timed out after 180 seconds.
- Actorless History and Evolution detail renders were requested for normal, long-text, and missing-localisation states. The calls completed but returned no structured artifact metadata through the wrapper (`{}` for both results). A follow-up History render remained running without output and was terminated. These are exact MCP-route blockers; source-only checks are not treated as equivalent visual acceptance.

## Meaningful validation

- Confirmed all thirty-one scoped Event 26 localisation references resolve.
- Confirmed no scoped duplicate keys, stale desert terms, raw old percentage phrasing, or internal phrases targeted by this pass remain in active Event 26/event-log surfaces.
- Confirmed Event 26 debug, settings, and last-fired mappings all resolve to `chaosx.event_name.26: "Black Friday"`.
- Confirmed the Event 26 and shared scripted-localisation files remain structurally balanced after selector insertion.
- Confirmed the 50 percent and 75 percent payload constants match the recorded payment ratios used by the new History selector branches.

## Remaining risks and skipped validation

- Event-26-bound post-change visual acceptance remains unresolved because the installed MCP GUI route did not expose explicit variable binding, the inspect/render calls timed out or returned empty metadata, and the successful synthetic renders reported no validation checks. Overflow, clipping, and wrapping therefore cannot be certified for the exact dynamic 50/75 percent states.
- The `black_friday.scope.global` line remains hidden by shared GUI actor visibility for actorless records. The visible history sentence still establishes global scope.
- The active sale idea description consumes the dynamic line, rounding, and requirements strings. Owner-specific purchase-tool-tip display still depends on each owner adapter, so the generic source text is not evidence of universal coverage.
- Spreadsheet mirrors require a later owner pass because spreadsheet edits were explicitly prohibited.
- No Git commit was created. The repository has extensive unrelated concurrent changes, including pre-existing edits in the shared scripted-localisation file; committing that file would also commit work not owned by this audit.

## Simplifications and omissions

No requested localisation surface was omitted from source review, and no fallback text or gameplay simplification was introduced. Exact Event-26-bound visual acceptance and the actor-line GUI behavior remain blocked as described above.
