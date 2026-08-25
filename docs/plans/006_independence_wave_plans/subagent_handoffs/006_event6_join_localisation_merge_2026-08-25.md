# Event 006 Join localisation merge

## Scope

This source-layout pass folds the twelve shared Join localisation keys into `localisation/english/006_independence_wave_l_english.yml`, the existing Event 006 shared localisation registry. The former `006_independence_wave_join_l_english.yml` file is removed.

The four history payloads, report title/description/options, and cooldown tooltip retain their original keys and player-facing wording. No event id, scripted effect, trigger, callback, category, decision, or gameplay condition changes.

## Preservation evidence

The Join source contained 12 unique keys; the central registry had no colliding keys. A source comparison found all 12 key/value pairs unchanged in the receiver, with no duplicate keys. The receiver remains UTF-8 with BOM.

## Boundary

This is a source-layout consolidation only. It does not change Join reachability, retry timing, event-log history, pre-event visibility, or the package-admission boundary. Historical Join handoffs may retain the removed path for provenance; current Join documentation points to the shared registry.
