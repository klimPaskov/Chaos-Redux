# Event 007 Fury Localisation Audit

Date: 2026-10-05.

Agent role: `chaosx_localisation_auditor`.

Disposition: `implemented` for the assigned localisation patch, pending parent review.

Acceptance basis: The parent's 2026-10-05 instructions authorized concise plain-language rewrites, meaningful requirement labels, the first-entry and invalid-start report keys, first-conquest wording, and inline cost rows with complete cost tooltips.

## Files changed

- `localisation/english/007_random_expansion_l_english.yml` contains the Event 007 reports, decisions, ideas, focus descriptions, and dynamic cost labels.
- `localisation/english/007_fury_requirement_flags_l_english.yml` contains visible Fury flag and scripted-trigger requirement labels.
- `docs/plans/007_fury_plans/catalog_changes_pending.md` records the spreadsheet mirror work queued for the parent.

## Localisation changes

The new `chaosx.nr7.3` report explains that Fury can start only in an independent minor country with at least one valid neighboring country, while player countries, their allies, and their subjects remain protected.

The new `chaosx.news.7008` article covers Fury’s opening mobilization and uses `[fury_opening_news_actor.GetName]` in its title and body.

The `chaosx.news.7007` title now identifies the first conquest: `Fury Takes Its First Neighbor`.

World reports, decision descriptions and tooltips, idea descriptions, and focus descriptions use shorter concrete sentences and omit the scoped process terms, update-history wording, achievement references, and branching spoilers reviewed in this pass.

`fury_world_in_fury_candidate_tt` now states the visible focus effect without describing hidden seed counts or the escalation route.

The depot action text says that it deploys one fully equipped column and consumes one reserve; the inline cost row shows command power, infantry equipment, and manpower, and its full cost tooltip adds support equipment.

The depot requirement strings identify the available reserve and the required owned and controlled deployable state; its dynamic cost row and full cost tooltip display the support-equipment and manpower amounts.

The admin-core, emergency-aid, terminal-reserve, and March coring inline variants each show no more than three iconized values; their full tooltip strings append the fourth amount through parent-owned dynamic getters.

March coring retains the stability icon and value and no longer displays support equipment, matching the parent-approved four-cost action.

Reserve sharing is titled `Share Reserve Supplies` and describes supplies going to another eligible Fury Pact member without claiming native faction membership.

The visible and activation requirement labels cover every audited Event 007 flag and scripted trigger exposed in player-facing requirements, including the depot and War Office unlocks and the reserve-share recipient gate.


No gameplay, event, shared GUI, or shared-framework localisation files were edited.

## Localisation coverage

The focused source sweep covered `events/007_fury.txt`, the Event 007 decisions and category, focus tree, ideas, scripted effects and triggers, scripted localisation, scripted GUI, and the shared `026_black_friday_scripted_localisation.txt` selectors used by Event 007 cost rows.

The repo-wide `.tools/audit_localisation_static.py` token pass did not finish after roughly 60 seconds, so its full-tree run was stopped. The focused key-binding and visible-requirement checks below completed against the Event 007 sources.

All visible Event 007 event fields and bare or quoted player-facing localisation bindings resolved to English keys. The focused requirement audit found no unlocalised Fury or Anti-Fury flag/tooltips in visible decision, mission, or focus requirements. The two owned YAML files contain no duplicate keys.

The Event 007 GUI and GFX files had no direct localisation-key or custom-tooltip references.

Dynamic scope references were checked against their source setup: `fury_opening_news_actor` is saved before the opening news event; `fury_news_actor` before first-conquest news; `fury_terminal_player_target` before the player warning and is cleared at shutdown; and `fury_monroe_response_actor` before its report event.

The title, description, action-tooltip, and unused wrapper keys for `fury_survey_beyond_the_border` were removed after root accepted retiring that decision. Its six ordinary and sale cost-adapter target keys remain because the shared 026 selectors still reference them.

The no-op `anti_fury_recognition_denial` decision was retired. Its visible strings and unreferenced cost wrappers were removed, while its six ordinary and sale cost-adapter values and matching cost-display pair remain for the shared 026 selectors.

The old `fury_core_cost_text*` values remain as literal compatibility strings because the shared 026 selectors reference them and no live Event 007 decision uses that family. The active administration and March decisions use per-resource dynamic getters. Root accepted retaining the legacy family without changing shared selectors in this tranche.

The parent removed the obsolete `common/scripted_localisation/007_fury_costs.txt` scalar-cost file. Its seven scalar `_value` outputs no longer appear as missing Event 007 localisation bindings.

## Cost and encoding evidence

Every active inline cost variant shows no more than three resource icons. Depot, administration, emergency aid, terminal reserves, and March coring show all four paid components in their full tooltip; the fourth component uses its own per-resource getter.

The component display localisations pair the correct resource icon and dynamic amount. The same getter appears in normal and blocked rows, so only the resource the payer lacks turns red. Integer resource values use the `.0` formatter; March stability uses `%0`.

The unconsumed generic `fury_core_cost_text*` compatibility family remains the one legacy cached-colour exception. Its 026 selectors have no live Event 007 decision consumer; the active administration and March decision rows use component-level affordability colours.

`python .tools/report_colour_audit.py --event 007` returned `total keys with colour: 0` for report and news titles, descriptions, and reachable scripted localisation.

Both owned YAML files retain their UTF-8 BOM. Their icon bytes are valid UTF-8 for `£` and `§`, and neither contains replacement characters. The primary localisation file's pre-existing mixed line endings were preserved during key cleanup.

## Reference evidence and route gap

`hoi4.reference_context` returned status `ok` for the localisation surface in workspace `mod_chaos_redux_ea3b2d67c2c0`; it identified the local Paradox Wiki Localisation section at lines 73–105 with revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, Event Modding localisation at lines 49–75 with revision `0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d`, and installed `loc_formatter_documentation.md` with revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`.

The bounded `hoi4.reference_search` and `hoi4.reference_read` calls did not return; the local source files were read directly as required by `AGENTS.md`.

The offline Localisation page was read at lines 73–105 for UTF-8-BOM and one-line value requirements and lines 184–214 for dynamic variable digit formatting; its SHA-256 is `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.

The offline Event Modding page was read at lines 49–75 for English event localisation and UTF-8-BOM requirements; its SHA-256 is `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.

The offline Data Structures page was read at lines 263–307 for event targets and localisation namespaces; its SHA-256 is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

The installed `loc_formatter_documentation.md` was read at lines 1–22; its SHA-256 is `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`.

The installed `effects_documentation.md` entry for `save_event_target_as` was read at lines 6496–6509; its SHA-256 is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.

The installed `triggers_documentation.md` entry for `has_event_target` was read at lines 3844–3854; its SHA-256 is `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

## Remaining parent review

The source reference image `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/evt007_sheet.jpg` contains observer-run popups but no Fury popup, so it cannot establish Fury text wrapping or layout.

Shared-framework localisation remains outside this subagent’s edit scope, so these accepted `premise only, no mechanics spoiler` text updates are queued for the parent:

- `chaosx.events_log.window.event_details.fury`: `A sudden rage seizes a minor country and drives its army into neighboring states. As the violence spreads, nearby countries must decide how to respond.`
- `chaosx.events_log.world_end.world_in_fury.details`: `Fury has reached countries around the world. Governments mobilize against their neighbors, and the scale of the fighting threatens every border.`
- `chaosx.events_log.window.evolution_details.fury.body.event_detail`: `The crisis grows as Fury spreads. New conflicts draw countries into the violence.`
- `chaosx.events_log.window.evolution_details.fury.body.stage_1`: `Fury's first country has become a lasting threat. Its neighbors now face a force that continues after its first campaign.`
- `chaosx.events_log.window.evolution_details.fury.body.stage_2`: `Fury has reached a second country. Its arrival deepens the danger across the region.`
- `chaosx.events_log.window.evolution_details.fury.body.stage_3`: `Fury has spread across several countries. The fighting now reaches every frontier.`

The event catalog workbook and CSV exports were not edited; the exact mirror candidates are in `catalog_changes_pending.md` for the parent’s spreadsheet handoff.

No in-game or desktop verification was performed.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and the cost-localisation section of `chaos-redux-decisions-missions`; no skill files were changed.
