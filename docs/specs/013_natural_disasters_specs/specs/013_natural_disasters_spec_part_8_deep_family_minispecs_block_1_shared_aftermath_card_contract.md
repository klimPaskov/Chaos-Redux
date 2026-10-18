# Shared aftermath card contract (block 1)

Verbatim part of [013_natural_disasters_spec_part_8_deep_family_minispecs.md](013_natural_disasters_spec_part_8_deep_family_minispecs.md), which indexes this specification.

## Shared aftermath card contract

Every active disaster card should use the same player-readable field set so the UI remains predictable. The field values differ by family.

The fields below are the accepted, implemented card data.
Showing all of them at once is the value-dump pattern the 10 October brief rejects; a four-line display budget that keeps every field in the data and in abnormal history is proposed (spec audit 2026-10-10) as open question 1 in the package README.
The working decision keys in the family sections below map to live decisions by replacing the `013_` prefix with `natural_disaster_` (for example `013_warn_earthquake_rail_crews` is `natural_disaster_warn_earthquake_rail_crews`).

| Card field | Purpose |
| --- | --- |
| `family_key` | Internal family key used by scripted localisation, icons, reports, and chain logic. |
| `family_group` | Broad hazard group for filters and visual grouping. |
| `primary_state` | Main affected state, with optional linked states displayed below it. |
| `impact_signature` | Short direction for the visual damage identity. This is not final text. |
| `severity_band` | Local, severe, regional, abnormal, or barrage. |
| `primary_damage_profile` | What the player should understand was damaged. |
| `death_driver_summary` | Visible reasons deaths rose, without exposing hidden formulas. |
| `visible_disruption` | The main disruption the player must manage now. |
| `primary_recovery_need` | The first recovery need that should guide decisions. |
| `risk_badges` | Follow-up risks that can appear as compact icons or text tags. |
| `cleanup_state` | Warning pending, impact pending, rescue active, stabilization active, reconstruction active, or closed. |
| `next_reassessment` | Dynamic date or countdown for the next impact, chain check, or recovery pulse. |
| `foreign_relief_state` | Current relief state when a foreign variant is active. |
