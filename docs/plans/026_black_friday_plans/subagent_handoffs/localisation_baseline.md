# Event 26 Black Friday localisation baseline

## Scope and evidence boundary

This is a read-only source audit of the current desert Event 26 and the shared event-name, settings/debug, event-history, Event Details, evolution, actor, status, cost-text, and catalog surfaces that the Black Friday implementation must change. No gameplay, localisation, GUI, scripted-localisation, asset, or workbook source was patched.

The installed runtime did not expose any `hoi4-agent-tools` event or GUI callable. Searches of the available tool inventory found no `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.gui_inspect`, or `hoi4.gui_render` route. Therefore Event 26 chain rendering, production Event Log/Event Details rendering, overflow, wrapping, clipping, alignment, and artifact URIs remain blocked. Source-only review below is not equivalent to MCP engine or visual evidence.

## Current Event 26 identity and stale desert ownership

| Surface | Exact source | Current stale ownership | Required disposition |
| --- | --- | --- | --- |
| Entry and report chain | `events/026_industry_to_desert.txt:1`, `:23-24`, `:32`, `:36`, `:45-54`, `:106` | `chaosx.nr26.1` leads to desert report `chaosx.nr26.2`; the report uses `GFX_report_event_desert` | Preserve only canonical entry `chaosx.nr26.1`; replace the `.2` report role and all desert behavior |
| Event localisation | `localisation/english/026_industry_to_desert_l_english.yml:2`, `:4-7` | `chaosx.nr26.1.t`, `.2.t`, `.2.d`, `.2.a`, `.2.b` describe Desert Industry and Operation Desert Forge | Replace in the new Event 26 localisation file; retaining `.2` as the player report is the least disruptive namespace choice |
| Desert news event | `events/_chaosx_news.txt:339-347`; `localisation/english/026_industry_to_desert_l_english.yml:9-11` | `chaosx.news.27` is explicitly owned by Industry to Desert and uses `GFX_news_desert` | Remove Event 26 ownership and the three news keys unless another owner is deliberately assigned; Black Friday specs require a report broadcast, not a news event |
| Desert sprites | `interface/chaosx_pictures.gfx:137`, `:156-157` | Desert news/report textures live below `gfx/event_pictures/026_industry_to_desert/`; report sprite is `GFX_report_event_desert` | Remove or reassign only after confirming no other consumer; Black Friday proposes `GFX_report_event_026_black_friday` |
| Fire-once registry comment | `common/scripted_effects/chaosx_logic_effects.txt:249` | ID 26 is labeled `MOVE INDUSTRY TO DESERT` | Keep the fire-once row and relabel it Black Friday |
| Shared event name | `localisation/english/chaosx_event_names_l_english.yml:28` | `chaosx.event_name.26: "Industry to Desert"` | Change value to `Black Friday` |
| Debug/settings selectors | `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:124-127`; `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:1728-1731`, `:5729-5732` | ID 26 already resolves through `chaosx.event_name.26` | No selector key rename is needed; changing the shared key value updates debug selection, settings selection, and last-fired display |
| Evolution/history/cluster member name selectors | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:1348-1357`, `:10277-10286`, `:11989-11998` | ID 26 already resolves through `chaosx.event_name.26` | No selector key rename is needed |
| Catalog | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events!A27:N27`; export at `docs/spreadsheets/chaos_redux_events_catalog.csv:113` | `26 / Desert question / To Be Reworked`, with desert premise | Replace row 27 from the workbook and regenerate exports |

Repository-wide stale phrase search also found the Event 26 comments and assets above. No active no-ID `Black Friday` backlog row exists in the current workbook or exported Events CSV, despite the specification package recording one in its earlier source snapshot. The spreadsheet worker must reconcile against the current workbook and must not delete a row that is no longer present.

## Existing shared patterns to reuse

- Event names use one stable key, `chaosx.event_name.<id>`, across debug, settings, last-fired, history, evolution, and cluster-member selectors. Event 26 already has complete selector coverage.
- Event Details descriptions are selected by `GetEventsLogEventDetailDescription` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`. Existing event branches return event-specific premise keys, for example `resources_found.event_details.description` at lines 6200-6209. There is no Event 26 description branch, so Event 26 currently falls through to `chaosx.events_log.window.event_details.entry_placeholder.generic` at lines 6615-6618.
- Event Detail evolution previews use `GetEventsLogEventDetailEvolutionTitle` at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6671-6673` and shared row keys at `localisation/english/chaosx_gui_l_english.yml:618-621`. A Black Friday evolution branch is absent.
- Full evolution detail uses the existing `GetEventsLogSelectedEvolutionTitle`, `GetEventsLogSelectedEvolutionBody`, and `GetEventsLogSelectedEvolutionSummary` selectors at lines 7429, 8186, and 8663 of the scripted-localisation file. Event 26 needs branches in all three if the evolution detail window is intended to be complete.
- The event logger defaults to actorless state with `events_log_default_has_actor = 0` at `common/scripted_effects/chaosx_events_log_effects.txt:198-200`. Event 26 has no actor override, which is mechanically correct. However, `GetEventsLogHistoryDetailsActorLine` falls through to `chaosx.events_log.window.history_details.actor_missing` at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:801-804`, whose current text is `Actor: Unattributed` at `localisation/english/chaosx_gui_l_english.yml:596`. Deliberately global Black Friday should not look like missing data.
- Generic locked weight text already exists as `chaosx.events_log.events.weight.locked: "§RN/A§!"` at `localisation/english/chaosx_gui_l_english.yml:537`. No existing event-list keys or selector states express `Reserved` or `Active Today`; these require new state data and localisation branches rather than reusing zero or generic lock text.
- Existing cost text is owner-specific. The audit found static normal/discounted pairs such as `japan_chemical_campaign.cost.discounted` and `_blocked` in `localisation/english/chaosx_decisions_l_english.yml:344-346`, and dynamic multi-resource text such as `cannibalism_unified_air_operation_cost_text` in `localisation/english/014_cannibalism_l_english.yml:1682`. No shared universal cost-source label, quote line, ordinary-versus-final line, saved amount line, or minimum-quantum explanation currently exists.

## Missing key contract for Black Friday

The exact helper and subevent identifiers are still owner decisions, but the following stable localisation keys are recommended so all required surfaces have one named contract. If the parent selects different identifiers, it should provide a one-to-one replacement list rather than omitting a surface.

### Event-owned popup and temporary status

- `chaosx.nr26.1.t`: hidden entry title, `Black Friday`.
- `chaosx.nr26.2.t`: human report title.
- `chaosx.nr26.2.d`: human report description with dynamic active percentage and next-daily-tick expiry.
- `chaosx.nr26.2.a`: one short dry purchasing-office acknowledgment.
- `black_friday_sale`: temporary idea/status title.
- `black_friday_sale_desc`: dynamic active percentage, next-tick expiry, positive minimum unit, and unchanged requirements/cooldowns.

The old `chaosx.nr26.2.b` is not required by the accepted one-option report design. The old `chaosx.news.27.t`, `.d`, and `.a` are stale and should not be carried into Black Friday.

### Shared name, premise, actorless context, and live status

- `chaosx.event_name.26`: `Black Friday`.
- `chaosx.events_log.window.event_details.black_friday`: premise-only Event Details copy aligned with the catalog `Details` mirror.
- `chaosx.events_log.window.history_details.actor_global`: deliberate actorless label such as `Scope: Global`; add an Event 26-specific branch before the generic `actor_missing` fallback.
- `black_friday.event_list.status.reserved`: `Reserved`.
- `black_friday.event_list.status.active`: `Active Today`.
- `black_friday.event_details.status.unavailable`, `.eligible`, `.reserved`, `.active`, `.expired`, `.disabled`: concise dynamic detail status states.

The shared Event Details metadata already supplies type, chaos level, fired state, and enabled state. Do not repeat those values in the premise paragraph.

### Evolution and history payload

- `black_friday.evolution.1.title`: `Seventy-Five Percent Off`.
- `black_friday.evolution.1.body`: concrete 75-percent activation behavior, fixed snapshot, and one-day duration.
- `black_friday.evolution.1.summary`: short evolution-list summary.
- `black_friday.history.50.description`: actorless Friday activation at 50 percent.
- `black_friday.history.75.description`: actorless Friday activation at 75 percent.

The implementation must add corresponding branches to Event Detail preview, selected evolution title/body/summary, and history payload description selectors. A title key alone would leave the evolution detail body generic or raw.

### Universal cost-source display

- `black_friday.cost_source.name`: short source label, `Black Friday`.
- `black_friday.cost_source.line`: dynamic final price first, followed by the ordinary current price when the consumer has room.
- `black_friday.cost_source.minimum_rounding`: explains only when upward minimum-unit rounding changed the arithmetic result.
- `black_friday.cost_source.requirements_unchanged`: short reminder that non-cost requirements and cooldowns still apply.
- `universal_cost.quote.final`: shared final-payable label for adapters that use generic quote UI.
- `universal_cost.quote.ordinary`: shared ordinary-current-cost label.
- `universal_cost.quote.blocked`: generic blocked affordability state that preserves the exact amount and matching texticon.

The shared API should expose dynamic values to these keys with integer `|0` formatting where the resource quantum is integral. It must not print basis points, helper names, variable names, or formula fragments. Owner-specific cost strings still need their own active and blocked variants or scripted-localisation branches when their UI cannot consume the generic quote keys.

### Achievement

- `026_black_friday_five_departments_NAME`: final reviewed achievement name.
- `026_black_friday_five_departments_DESC`: five distinct purchase types during one natural Black Friday, including institutional, material/commitment, and non-political-power requirements.
- `026_black_friday_five_departments_tooltip`: optional only if the existing achievement registry requires a separate progress/eligibility explanation.

The working phrase `Five Departments` is not accepted final copy by the spec and should not be promoted without localisation review.

## Mechanical localisation findings

### Missing keys

- All Black Friday keys listed above are absent.
- Event 26 has no Event Details description branch and therefore displays the generic no-detail placeholder.
- Event 26 has no evolution preview or selected evolution title/body/summary branches.
- The shared event list has no reserved or active-today display state.
- The shared framework has no universal cost-source or quote keys.
- There is no deliberate global actor label for Event 26 history.

### Duplicate keys

No duplicate definitions were found for the current Event 26 key family. Each of `chaosx.nr26.*`, `chaosx.news.27.*`, and `chaosx.event_name.26` occurs once in localisation. No `black_friday*` or `026_black_friday*` localisation key currently exists.

### Scripted localisation issues

- Event 26 name selectors are present and correctly converge on `chaosx.event_name.26`; only that key value is stale.
- Event Details lacks an Event 26 branch and falls through to the generic placeholder.
- Actorless history is mechanically represented by `has_actor = 0`, but the generic text calls it `Unattributed`, which falsely suggests missing provenance.
- Evolution selectors have no Event 26 branches.
- Reserved and active statuses cannot currently be distinguished by the standard weight text. Using zero would contradict the specification.
- No current dynamic text joins displayed ordinary cost, discounted cost, source name, and rounding state. Every cost owner must bind display and payment to the same quote result.

### Dynamic text opportunities

- Resolve active `50` or `75` percentage from the activation snapshot in the popup, idea description, Event Details active status, history detail, and cost-source line.
- Resolve expiry as `next daily tick` unless a verified date formatter can show the exact synchronized expiry date without stale quotation risk.
- Print ordinary and final cost from the same per-payer quote scope, with the resource's registered formatter and texticon.
- Show minimum rounding only when it actually changes the unrounded result.
- Keep blocked non-cost requirements separate from the discounted price and reuse the owning action's existing requirement tooltip.

## Cross-surface and catalog alignment risks

- The specification's catalog brief supplies a long `Details` paragraph. Event Details must use the same premise wording, but the current brief mixes premise with mechanical guarantees such as modifier preservation and minimum rounding. The event skill says Event Details and spreadsheet `Details` should describe the situation and premise rather than list effects. Recommended mirror: one concise sentence about a global Friday sale lowering government, military, intelligence, equipment, and project purchase costs for that day. Put percentages, expiry, and minimum rounding in status/evolution/cost tooltips and dedicated columns.
- The catalog brief's Evolution I wording is suitable as a mechanic summary but should match `black_friday.evolution.1.summary` exactly after final prose review.
- The workbook currently has only the ID 26 desert row. The older spec claim about a duplicate no-ID Black Friday row is stale against the current authoritative workbook.
- The workbook row's `Chaos level` is currently `1`, while the accepted design requires Gathering Storm at 200 chaos. The catalog update brief does not explicitly state the replacement value for this column. The parent/spreadsheet worker must resolve the workbook's tier encoding before saving.
- Status must remain `Needs Testing` after implementation. Do not infer `Playable`.
- `chaosx.news.27` is globally numbered and adjacent to Event 25's `chaosx.news.26`. Removing Event 26's news entry must not renumber or damage Event 25 or later news events.
- Cost-source wording must not promise universal coverage for strategy-D engine-inaccessible surfaces. Prefer `registered purchase costs` until the final coverage registry proves the supported boundary.

## Prose-quality findings

- Vagueness: `Desert Industry`, `Move Industry to desert?`, and `Secure our industry!` do not identify who acts or what precise player choice changes. These keys are obsolete rather than reusable.
- Bloat: the old desert event prose is short and not bloated, but its two-sentence news description repeats the relocation result. The news surface is outside the accepted Black Friday chain and should be removed rather than rewritten.
- Obvious explanation: `The relocation is complete.` adds no useful consequence beyond its title and description.
- Repetition: `Desert Industry` is repeated as both event and news title, and `Operation Desert Forge` repeats the same move in popup and news copy.
- Overcomplication: no severe syntactic overcomplication was found in the old Event 26 localisation. The new implementation is at greater risk of overcomplication if it enumerates adapter classes, cost families, rounding formulas, and preserved conditions in the report description.
- Style-rule repair: the old copy uses no em dash, semicolon, staged contrast formula, or sourced quotation. New prose should keep the dry period retail tone, avoid modern e-commerce language, and put final price before explanation in cost tooltips.

## Encoding and sourced quotations

- `localisation/english/026_industry_to_desert_l_english.yml`, `chaosx_event_names_l_english.yml`, and `chaosx_gui_l_english.yml` are UTF-8 with BOM.
- The current Event 26 localisation uses repository key syntax without `:0`.
- A replacement `localisation/english/026_black_friday_l_english.yml` must retain UTF-8 BOM. Deleting the old file and creating a new one is an encoding-risk point that needs explicit verification by the parent.
- No sourced or attributed quotation appears in the current Event 26, shared Event 26 selectors, or accepted Black Friday spec. No quotation text needs preservation.

## Recommended parent edit map

- Replace `events/026_industry_to_desert.txt` and `localisation/english/026_industry_to_desert_l_english.yml` while preserving entry `chaosx.nr26.1`.
- Update `localisation/english/chaosx_event_names_l_english.yml:28` key `chaosx.event_name.26`.
- Add Event 26 premise, actorless-global, active-status, history-payload, and evolution branches to `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and their keys to `localisation/english/chaosx_gui_l_english.yml` or the event-owned Black Friday localisation file according to current ownership conventions.
- Keep debug/settings selector branches unchanged unless the implementation replaces numeric ID 26 with a documented constant in the same behavior-preserving change.
- Remove Event 26 ownership of `chaosx.news.27` from `events/_chaosx_news.txt` and its old localisation, without renumbering neighboring news events.
- Remove or reassign desert GFX entries in `interface/chaosx_pictures.gfx` only after a consumer search; wire the proposed Black Friday report and idea sprites in the event-owned GFX file.
- Add the temporary idea keys, cost-source keys, owner-specific dynamic/blocked cost variants, and achievement keys listed above.
- Update only the authoritative workbook row `Events!A27:N27`, verify the `Chaos level` encoding, set status `Needs Testing`, then regenerate all catalog CSV exports.

## Validation completed and unresolved blockers

Completed: repository-wide stale-identity search, Event 26 key occurrence and duplicate scan, shared selector tracing, actorless fallback tracing, authoritative workbook row inspection, exported CSV comparison, and BOM inspection of the three directly affected shared/current localisation files.

Blocked: HOI4 MCP event inspection/rendering and GUI inspection/rendering are unavailable in this runtime, so there is no event-chain diagnostic, no production visual evidence, no overflow or clipping conclusion, and no artifact URI. Final localisation acceptance still requires those routes after implementation. The full universal cost-owner audit also belongs to the implementing cost-framework and decision owners; this baseline only establishes the shared key contract and current Event 26 text debt.
