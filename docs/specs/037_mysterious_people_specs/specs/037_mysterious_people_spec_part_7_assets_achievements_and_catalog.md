# Event 037: Mysterious People

## Part 7: Assets, achievements, and catalog alignment

## Visual identity

Event 037 looks ordinary enough to make the anomaly credible: documentary, domestic, and crowded.
People and settlements are the subject, and records appear only as props.
No portals, alien silhouettes, laboratories, beams, science-fiction machinery, readable generated text, modern clothing, maps as the main image, disease symbolism, or hostile caricature.

## Asset inventory

All assets are implemented.
Production follows `.claude/skills/chaos-redux-event-assets/SKILL.md` and the [asset prompt](../prompts/037_mysterious_people_asset_prompt.md), which owns sizes, paths, and the handoff format.

| Asset | Consumer | Subject |
| --- | --- | --- |
| Manifestation report image | `chaosx.nr37.2` and the evolution reports | A settlement full of families, complete homes, and ordinary work that looks years old |
| News picture | `chaosx.news.42` | Review the existing `GFX_news_mysterious_population` against the firewall, and replace it only if it suggests an origin |
| Decision category picture | Event 037 category | A crowded new district or settlement street, with no painted controls or values |
| Category icon | Event 037 category | A small family group beside a house |
| Stance icons (2) | Open Integration, Restricted Registration | Open doorway with a family, a barrier with papers |
| Action icons (5) | Registration Drive, Requisition, Emergency Housing, Roads and Water, New City | Registration table, opened vacant building, scaffolded houses, road and water main, new city blocks |
| Mission icon | Absorb the Newcomers | Families carrying belongings into finished homes |
| Modifier icon | Newcomers | Workers entering a factory and a farm |
| Achievement triplets (3) | The three achievements below | See each achievement |

Each icon has its own source art.
Event 037 adds no art for Famine, Migration, or camp actions.

## Achievements

All three are implemented and live in `common/achievements/chaos_redux_achievements.txt` with the existing shared rules for game mode, country continuation, and persistence.
Their IDs follow the repository pattern for event achievements.

### `037_room_for_everyone`

Make the newcomers part of ordinary life without hunger.

- Newcomers are at least `25%` of the country's population at the latest count.
- National pressure stays below `40` for `365` consecutive days.
- No owned state reaches the famine or catastrophic famine stage during that time.
- The timer resets when either condition fails.

Icon direction: a dense, orderly town around an open civic building.

### `037_a_billion_more`

Stay calm while the world transforms.

- Evolution III is active.
- A manifestation brings living newcomers in the world to at least `1,000,000,000`.
- At that firing's count the country holds at least `10,000,000` newcomers and its national pressure is below `40`.

Icon direction: an immense crowd spread across city, farm, and industry, without a globe as the whole composition.

### `037_three_censuses`

Settle three waves in a row.

- Complete Absorb the Newcomers successfully after three different manifestations.
- National pressure never reaches Emergency between the first counted manifestation and the third success.
- A mission success counts once, keyed to the manifestation that started it, so reports, reloads, and multiplayer cannot count it twice.

Icon direction: three household rolls stacked beside a growing settlement, with no readable text.

## Catalog alignment

The current workbook row still holds the legacy premise ("A major country receives millions of unexplained new recruits.").
The replacement wording, the cluster record, and the workbook procedure are in [the catalog handoff](../handoffs/037_mysterious_people_catalog_and_cluster_alignment.md).

## Event Details

Event Details explain the worldwide appearance of people with homes and histories, that it repeats, that settling them can become a burden, and that nobody knows where they come from.
It never shows formulas, variable names, AI weights, or an explanation.
Evolution previews describe the next manifestation and the situation it creates, not modifier lists.

## Event-log detail

One history row per firing shows the people created worldwide, the people created in the player's country when relevant, the number of states affected, the manifestation stage, and the living newcomers in the world.
Evolution rows record the three evolutions.
Pressure stages never become log rows.

## Documentation set

Implementation writes `docs/events/037_mysterious_people/overview.md` with the ledger, pressure, evolutions, decisions, adapters, assets, achievements, and validation, documents the new neutral gain helper in `common/scripted_effects/chaosx_dynamic_effects.md`, and updates the workbook through the catalog handoff.
