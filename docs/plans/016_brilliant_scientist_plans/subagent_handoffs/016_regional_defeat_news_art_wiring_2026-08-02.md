# Event 016 regional-defeat news-art handoff

Date: 2026-08-02

## Scope

The mapped regional-defeat news event `chaosx.nr16.302` now has an Event 016-owned black-and-white scene instead of the generic research-lab picture. The underlying defeat qualification, custodian selection, and settlement decisions are unchanged.

## Asset and wiring

- Generated source master: `docs/assets/016_brilliant_scientist/report_news_expansion/source_masters/news/news_event_016_brilliant_scientist_regional_defeat_source.png`.
- Processed preview: `docs/assets/016_brilliant_scientist/report_news_expansion/processed/news/news_event_016_brilliant_scientist_regional_defeat.png`.
- Runtime DDS: `gfx/event_pictures/016_brilliant_scientist/news_event_016_brilliant_scientist_regional_defeat.dds`.
- Sprite: `GFX_news_event_016_brilliant_scientist_regional_defeat` in `interface/016_brilliant_scientist.gfx`.
- The event now uses `minor_flavor = yes` and `major = no` and retains its existing localisation.

## Guard and validation

The regional branch sets `brilliant_scientist_news_regional_defeat_fired` before dispatching the event with the shared two-day news delay. The guard prevents a repeated capitulation callback from replaying the headline. The parent checked the generated scene visually, the DDS header (`397x153`, 32-bit BGRA, exact uncompressed size), sprite path existence, and Event Inspector status for `chaosx.nr16.302`. No 3D model or unit reference is involved.
