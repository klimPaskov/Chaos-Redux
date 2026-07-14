# Event 015 Non-Icon Asset Wiring Handoff

Date: `2026-07-14`  
Owner: `chaosx_non_icon_asset_wiring`  
Status: complete for the bounded report and news asset wiring scope  
Commit: not created, as requested

## Outcome

The complete Event 015 report and news package is registered and referenced by the event script. The existing `GFX_report_event_utopia_manifesto_found` registration was retained. The other `13` report sprites and all `3` news sprites were added without aliases or duplicate registrations.

The previously stale military picture identity was removed from all five military and auxiliary incidents. The event-family mappings were also completed for the three report identities that had no script references at asset handoff time.

## Changed Files

- `interface/015_utopia_manifesto.gfx`
  - Added `13` missing report sprite definitions.
  - Added `3` missing news sprite definitions.
  - Retained the existing `GFX_report_event_utopia_manifesto_found` block.
- `events/015_utopia_manifesto.txt`
  - Updated the five defense-family references.
  - Assigned the island, foreign commonwealth, and formation pictures to their confirmed event surfaces.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/non_icon_asset_wiring_handoff.md`
  - Records this bounded implementation and its validation evidence.

No decisions, focuses, scripted effects, scripted triggers, localisation, spreadsheets, asset manifests, or unrelated files were edited.

## Registered Report Sprites

- `GFX_report_event_utopia_manifesto_found` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_found.dds`
- `GFX_report_event_utopia_manifesto_ledger` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_ledger.dds`
- `GFX_report_event_utopia_manifesto_calling` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_calling.dds`
- `GFX_report_event_utopia_manifesto_store` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_store.dds`
- `GFX_report_event_utopia_manifesto_settlement` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_settlement.dds`
- `GFX_report_event_utopia_manifesto_island` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_island.dds`
- `GFX_report_event_utopia_manifesto_defense` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_defense.dds`
- `GFX_report_event_utopia_manifesto_foreign_commonwealth` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_foreign_commonwealth.dds`
- `GFX_report_event_utopia_manifesto_necessary_ground` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_necessary_ground.dds`
- `GFX_report_event_utopia_manifesto_stewardship` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_stewardship.dds`
- `GFX_report_event_utopia_manifesto_league` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_league.dds`
- `GFX_report_event_utopia_manifesto_formation` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_formation.dds`
- `GFX_report_event_utopia_manifesto_contradiction` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_contradiction.dds`
- `GFX_report_event_utopia_manifesto_evolution` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_evolution.dds`

## Registered News Sprites

- `GFX_news_event_utopia_manifesto_league` -> `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_league.dds`
- `GFX_news_event_utopia_manifesto_necessary_ground_war` -> `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_necessary_ground_war.dds`
- `GFX_news_event_utopia_manifesto_colony_revolt` -> `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_manifesto_colony_revolt.dds`

## Event Picture Assignments

- `chaosx.nr15.10` and `chaosx.nr15.130` use `GFX_report_event_utopia_manifesto_formation`.
- `chaosx.nr15.44` uses `GFX_report_event_utopia_manifesto_island`.
- `chaosx.nr15.80`, `chaosx.nr15.81`, `chaosx.nr15.82`, `chaosx.nr15.83`, and `chaosx.nr15.84` use `GFX_report_event_utopia_manifesto_defense`.
- `chaosx.nr15.110`, `chaosx.nr15.111`, `chaosx.nr15.112`, `chaosx.nr15.113`, `chaosx.nr15.114`, and `chaosx.nr15.115` use `GFX_report_event_utopia_manifesto_foreign_commonwealth`.
- `chaosx.nr15.160` uses `GFX_news_event_utopia_manifesto_league`.
- `chaosx.nr15.161` uses `GFX_news_event_utopia_manifesto_necessary_ground_war`.
- `chaosx.nr15.162` uses `GFX_news_event_utopia_manifesto_colony_revolt`.

The existing settlement, Necessary Ground, stewardship, league, contradiction, and evolution families retain their dedicated report sprites outside the explicitly mapped events above.

## Validation

- Checked all `17` expected report and news identities against `interface/015_utopia_manifesto.gfx`. Every sprite name and texture path appears exactly once.
- Checked all Event 015 report and news picture references. The script uses all `17` package identities, every reference resolves, and no registered package identity is unused.
- Checked the runtime files against `final_non_icon_2026_07_14/asset_records.json`. All `17` SHA-256 values match the recorded final checksums.
- Checked each DDS legacy header, pixel format, channel masks, texture caps, exact byte length, dimensions, and alpha range. All `14` reports are `210x176` with transparent report-card pixels. All `3` news images are `397x153` with opaque alpha.
- Confirmed that no gameplay or interface reference to `GFX_report_event_utopia_manifesto_military` remains.

## Simplifications, Omissions, and Remaining Risks

No fallback, alias, placeholder, simplification, or ambiguous mapping was used. There are no remaining risks inside this bounded registration and event-picture assignment scope. Broader Event 015 implementation and completion review remain parent-owned.

## Skills Used

- `chaos-redux-event-assets`
- `chaos-redux-events`

No skill was created or updated.
