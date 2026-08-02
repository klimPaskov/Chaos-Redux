# Fallout 712 asset manifest

## Identity

- Candidate: 712, The Returning Disease
- Asset class: fictional Fallout report-event illustration
- Source workflow: approved ImageGen generation followed by the Chaos Redux report-event processor
- No real person, flag, or attested symbol is represented

## Files

| Role | Path | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| Generated source | `docs/assets/712_returning_disease/source_returning_disease.png` | 1536x1024 | `F7AC81523CA5E3E0F23B75C775F7D8EB95F127FE3CE8B12E51EA561FBAEEB285` |
| Processed review PNG | `docs/assets/712_returning_disease/processed_returning_disease.png` | 210x176 | `834ECF2C79E35D875398A47DF365BC38B93A338722A9CD9EF2D0C69711B9AD7C` |
| Runtime DDS source | `docs/assets/712_returning_disease/report_event_fallout_returning_disease.dds` | 210x176 | `ECB715C86B471B31912A47660F80497ACFAB5CE5A28F61D813A93314150C12B2` |
| Runtime DDS copy | `gfx/event_pictures/fallout/report_event_fallout_returning_disease.dds` | 210x176 | `ECB715C86B471B31912A47660F80497ACFAB5CE5A28F61D813A93314150C12B2` |

## Prompt record

The source depicts a fictional winter quarantine clinic at Ash Ward Hospital with a masked public health officer, a red-seal ward ledger, medicine crates, a frozen checkpoint, and an aid convoy under cold rain and ash. The palette is muted blue, green, charcoal, and restrained amber. It contains no readable text, logos, or real people.

## Runtime consumer

`interface/fallout_world_end.gfx` registers `GFX_report_event_fallout_returning_disease`. The Fallout 712 event chain consumes that sprite in events 712, 714, and 716. The chain remains dormant until the reviewed scheduler activates candidate 712.
