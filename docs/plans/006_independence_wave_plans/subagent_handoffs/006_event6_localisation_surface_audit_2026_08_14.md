# Event 006 localisation surface audit handoff

Date: 2026-08-14

Scope: one bounded, already admitted Event 006 popup-localisation correction. No gameplay, central attestation, Join, asset, scripted-localisation, GUI, spreadsheet, or design files were changed.

## Finding and patch

- Changed file: `localisation/english/006_independence_wave_l_english.yml`
- Changed key: `chaosx.nr6.2.a`
- Exact surface: the sole player option on the synchronized-wave summary event `chaosx.nr6.2`.
- Before: `The map has learned new names.`
- After: `Let each government defend its declaration.`
- Reason: the old line made the changed map the emotional center. Part 1 of the accepted Event 006 spec requires the visible moment to center newly appearing governments and explicitly says that it should not be framed mainly as a changed map. The replacement names the governments and the immediate political consequence without promising a mechanic or changing the option effect.
- Safety: `chaosx.nr6.2` still has one effect-free acknowledgement option. Only its displayed sentence changed. Existing dynamic tokens in the event description were untouched.

## Required audit lists

- Missing keys: none found in the inspected `chaosx.nr6.2` surface. The event title, description, and option keys are present.
- Duplicate keys: none found for `chaosx.nr6.2.t`, `chaosx.nr6.2.d`, or `chaosx.nr6.2.a` in Event 006 English localisation.
- Scripted localisation issues: none found in the inspected description calls `GetIndependenceWavePresentationRegionText`, `GetIndependenceWavePresentationArmedText`, `GetIndependenceWavePresentationHostText`, and `GetIndependenceWavePresentationNetworkText`. Their selectors and fallback keys are source-present. Runtime output was not available from the read-only event viewer.
- Dynamic text opportunities: none required for the corrected option. The description already reports country count, region spread, armed releases, host concentration, and prior-network state dynamically.
- Cross-surface mismatch: corrected. The old map-centered option contradicted `006_independence_wave_spec_part_1_core.md`, section `The visible moment`.
- File encoding concerns: none for the changed file. Its UTF-8 BOM was present before the patch and preserved after it.
- Prose-quality issue: the old option was a vague personification and an obvious map summary. The replacement gives a direct subject, a concrete political action, and the consequence that follows the declarations. No bloat, repetition, overcomplication, em dash, semicolon, staged contrast, or staccato chain was introduced.
- Sourced quotation preservation: no sourced or attributed quotation exists on the inspected `chaosx.nr6.2` surface.

## MCP evidence

- `hoi4.event_inspect`, focused selector `chaosx.nr6.2`, returned revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b` and graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`.
- Scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67e636754849b8e10cbcdca49d68c3bf892d63423664fd6444dc39b03543ed17/6d8b9d04821986385420bbc32ce6847a2c9be3e06f4afd79d2f9a0a639a34c15/event-scan-741883f50501.json`
- `hoi4.event_render`, options view for `chaosx.nr6.2`, returned layout hash `642304747a6f09986be77c2b7543bfc6337755f5249f1238b2d31e14b362deaa`.
- Options render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63607b89d25e6600ae6fba6cb5d448f541803d6acb83aa8d35e203a63662ac74/be2f1f3b62c341e00d624435e45c367accb97ec5d8e4139eb3756fc6c6cf443f/event-options-741883f50501.svg`
- Viewer limitation: both MCP calls returned `EVENT_*_PARTIAL`. The large-workspace analysis deferred workspace-wide helper projections and lifecycle passes, so the artifacts prove the event and option surface linkage but not runtime-rendered localisation expansion or overflow.

## Validation

- Confirmed from `events/006_independence_wave.txt` that `chaosx.nr6.2` references `chaosx.nr6.2.a` as its sole option and that the option has no scripted effect to alter.
- Confirmed the four dynamic description selectors resolve to definitions in `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`, with every referenced fallback/localisation key present in `localisation/english/006_independence_wave_l_english.yml`.
- Confirmed the three `chaosx.nr6.2` localisation keys are unique within Event 006 English localisation and that the corrected option line contains no broken bracket, formatting, or dynamic token.
- Confirmed the changed localisation file retains the UTF-8 BOM.
- Compared the corrected sentence against the accepted Event 006 spec and the Chaos Redux event-writing rules.

## Skipped meaningful validation

- No live in-game localisation expansion or popup-width check was performed. Agents do not launch Hearts of Iron IV, and the installed event MCP returned structural source-linked renders rather than a runtime popup text-layout render.
- No workbook or Event Details comparison was needed because this option sentence is not a mirrored Event Details or catalog field.

## Before-and-after prose summary

- Vagueness: replaced the personified map with the concrete governments created by the event.
- Bloat: no added explanation; the option remains one short sentence.
- Obvious explanation: removed the redundant observation that the map has more names.
- Repetition: the option no longer repeats the description's map-level summary.
- Overcomplication: no issue before or after.
- Style-rule repair: shifted the emotional center from the map to governments defending their declarations, matching the accepted spec.

## Preservation and unresolved decisions

- Preserved all dynamic localisation tokens and formatting codes in `chaosx.nr6.2.d`.
- No sourced quotations were changed.
- No unresolved wording decision remains for this bounded correction.
- No broader design gap was found, so no separate plan handoff was written.
