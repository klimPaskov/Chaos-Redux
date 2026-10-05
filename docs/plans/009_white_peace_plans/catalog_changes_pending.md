# Event 009 Catalog Changes Pending

Disposition: accepted and queued. The parent finalized shared Event Details, evolution, availability, and achievement wording on 2026-10-06. Workbook alignment remains queued because the Event 009 owner task explicitly excluded workbook and CSV edits.

The only editable event-catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Do not edit the exported CSV files directly. After the workbook update, run `python .tools/export_event_catalog_csv.py` from the mod root.

The workbook's Event 009 row should be reconciled against the accepted runtime wording in `localisation/english/chaosx_gui_l_english.yml` for `chaosx.events_log.window.event_details.white_peace`, `chaosx.events_log.window.evolution_details.white_peace.body.event_detail`, and the three stage body keys. It should describe the armistice premise and separate isolated wars, without listing mechanics or implying several pairs can be taken from one multi-country war. Achievement descriptions and tooltips must mirror the current five achievement conditions.

The `docs/plans/009_white_peace_plans/subagent_handoffs/white_peace_event_catalog_workbook_handoff.md` document predates this release audit and does not certify current catalog alignment. The workbook source remains unverified in this pass.

## Exact accepted runtime wording

Only applicable existing catalog fields should be mirrored; this table is not approval to add speculative workbook rows.

| Key | Current English value |
| --- | --- |
| `chaosx.events_log.window.event_details.white_peace` | `Exhausted belligerents agree to an armistice without conquest or indemnity. Their armies withdraw to the borders held before the war, and neither government claims victory.` |
| `chaosx.events_log.window.evolution_details.white_peace.title.stage_1` | `Repeated Minor Settlements` |
| `chaosx.events_log.window.evolution_details.white_peace.title.stage_2` | `Major-Country Settlement` |
| `chaosx.events_log.window.evolution_details.white_peace.title.stage_3` | `Broad Diplomatic Settlement` |
| `chaosx.events_log.window.evolution_details.white_peace.body.event_detail` | `Negotiations bring exhausted armies back to their own territory. Other governments watch the ceasefire for signs that peace can hold.` |
| `chaosx.events_log.window.evolution_details.white_peace.body.stage_1` | `Armies withdraw to the old frontier as minor governments accept an armistice. Soldiers return to their own towns without a victory parade.` |
| `chaosx.events_log.window.evolution_details.white_peace.body.stage_2` | `A major power agrees to stop fighting without gaining land or tribute. Its soldiers withdraw across the old frontier.` |
| `chaosx.events_log.window.evolution_details.white_peace.body.stage_3` | `Separate armies receive orders to stop fighting and return to their own territory. The armistices leave neither side with conquered land or tribute.` |
| `achievement_white_peace_status_quo_ante_tooltip` | `As an independent minor outside factions, be included in a prolonged §YWhite Peace§! settlement.` |
| `achievement_white_peace_no_winner_tooltip` | `Both countries must remain alive, independent, and uncapitulated for 180 days after White Peace.` |
| `achievement_white_peace_chain_of_tables_tooltip` | `Have White Peace settle six separate minor wars before it settles a war involving a major country.` |
| `achievement_white_peace_silence_of_giants_tooltip` | `As a major country, be included in a prolonged §YWhite Peace§! settlement.` |
| `achievement_white_peace_the_circular_tooltip` | `Have one broad White Peace settlement end at least three separate minor wars.` |
| `chaosx.nr9.2.t` | `No Gains from the War` |
| `chaosx.nr9.2.d` | `[white_peace_report_primary.GetName] and [white_peace_report_partner.GetName] have accepted the same armistice. Their armies return behind the lines they held before the war, and neither country gains land or demands payment.` |
| `chaosx.nr9.3.t` | `Several Minor Wars End` |
| `chaosx.nr9.3.d` | `Across several frontiers, soldiers leave their posts and return behind the old borders. These wars have ended without a transfer of land or an indemnity.` |
| `chaosx.nr9.4.t` | `A Major Front Falls Silent` |
| `chaosx.nr9.4.d` | `A major government has ordered its armies to stand down after an armistice restores the old borders. Neither country receives payment.` |
| `chaosx.nr9.5.t` | `Armistices Across Several Fronts` |
| `chaosx.nr9.5.d` | `A series of separate minor wars has ended under the same terms. The armies return behind their former lines, and no country gains territory or an indemnity.` |
| `chaosx.nr9.2.a` | `The guns are quiet now.` |
| `chaosx.nr9.3.a` | `The front lines grow still.` |
| `chaosx.nr9.4.a` | `The armies return to their lines.` |
| `chaosx.nr9.5.a` | `The fighting has ended on these fronts.` |
| `chaosx.nr9.6.t` | `No Terms Can Be Sent` |
| `chaosx.nr9.6.d` | `[GetWhitePeaceInvalidEntryReason] No peace has been imposed and no border has changed.` |
| `chaosx.nr9.6.a` | `Understood.` |
| `chaosx.nr9.7.t` | `A War Ends Without a Victor` |
| `chaosx.nr9.7.d` | `[white_peace_report_primary.GetName] and [white_peace_report_partner.GetName] have returned to their prewar borders. Their armies have stopped fighting, and neither country gains land or pays an indemnity.` |
| `chaosx.nr9.7.a` | `The guns have fallen silent.` |
| `chaosx.nr9.8.t` | `Several Minor Wars End` |
| `chaosx.nr9.8.d` | `Across several frontiers, soldiers leave their posts and return behind the old borders. These wars have ended without a transfer of land or an indemnity.` |
| `chaosx.nr9.8.a` | `The front lines grow still.` |
| `chaosx.nr9.9.t` | `A Major Front Falls Silent` |
| `chaosx.nr9.9.d` | `[white_peace_report_primary.GetName] and [white_peace_report_partner.GetName] have ended their war on the borders they held before the fighting. The major army is returning to its own territory, and neither side receives payment.` |
| `chaosx.nr9.9.a` | `The war is over.` |
| `chaosx.nr9.10.t` | `Armistices Across Several Fronts` |
| `chaosx.nr9.10.d` | `Several separate minor wars have ended at once. The armies return behind their former lines, and no country gains territory or an indemnity.` |
| `chaosx.nr9.10.a` | `The fighting has ended on these fronts.` |
