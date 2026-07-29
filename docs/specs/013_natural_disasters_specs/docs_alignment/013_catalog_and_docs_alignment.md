# Event 013 Natural Disasters, catalog and documentation alignment handoff

This file gives player-facing direction for documentation, catalog rows, Event Details, scenario details, cluster details, and spreadsheet fields. It does not write final localisation. Implementation must write final text later from the accepted design and then use `chaosx_spreadsheet_doc_worker` to align the workbook with final in-game wording.

## Source alignment

| Surface | Direction |
| --- | --- |
| Event source spec folder | `docs/specs/013_natural_disasters_specs/` remains the source design area after this package is imported. |
| Working plan folder | Any implementation addendum, audit, or subagent handoff belongs in `docs/plans/013_natural_disasters_plans/`. |
| Event doc | `docs/events/013_natural_disasters/overview.md` should explain the live system after implementation, not the planning process. |
| Catalog workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` should be updated only after final in-game wording exists. |
| Scenario docs | Disaster Barrage should be documented with type and intensity controls after it is wired. |
| Related placeholders | Event 046 and Event 099 docs should be updated only to reflect their placeholder or bridge status. Event 051 stays separate. |

## Event Details direction

The Event Details entry should describe what the player sees in play. It should not list formulas, hidden weights, death percentages, building damage constants, or implementation history.

| Detail field | Direction |
| --- | --- |
| Main premise | Natural disasters can now arrive as delayed local, regional, and abnormal sequences. The player should understand that affected places receive reports and aftermath decisions. |
| Visible behavior | Mention specific disasters hitting specific states, delayed reports, recovery categories, and later chains. |
| Deaths and damage | State that disasters can cause serious deaths and infrastructure damage in broad player-facing terms. Do not list calculation details. |
| Reusable calls | Do not explain caller API in player-facing Event Details. Keep that in implementation docs. |
| Evolutions | Describe broader variety, regional scale, chained aftermath, and abnormal disaster systems by direction. Do not spoil hidden rare chains beyond visible evolution detail. |
| Tone | Grounded, physical, place-specific. Avoid a generic announcer frame. |

## Spreadsheet row direction

| Column | Direction for Event 013 row |
| --- | --- |
| `ID` | Keep `13`. |
| `Event Name` | Keep Natural Disasters unless final localisation changes the public name. |
| `Details` | Describe the player-facing premise, delayed disaster sequences, affected-country reports, aftermath categories, serious deaths, and damage. Do not write formulas or debug API fields. |
| `Evo I` | Describe widened disaster variety and more active delayed sequences. Keep it player-facing. |
| `Evo II` | Describe regional and global disaster pressure, neighboring-state damage, hard death scaling, and chained aftermath. Avoid spam detail. |
| `Evo III` | Describe abnormal high-chaos disasters such as meteor showers, rupture waves, massive eruptions, delayed tsunami chains, and moving storm corridors. |
| `World-End Scenario` | Leave blank in the workbook unless final implementation creates a scenario, which this spec does not ask for. |
| `Type` | Minor Repeatable. |
| `Cluster ID` | Use final cluster id only after cluster registry is implemented. |
| `Member Severity` | Low for baseline member entries, higher severity only through cluster member rows or final cluster detail if implementation supports it. |
| `Status` | Should move from To Be Reworked only after implementation and audit are complete. |

## Scenario details direction

Disaster Barrage should read as a manual challenge setup that launches the Event 013 controller directly. It should not sound terminal. It should not imply that every disaster creates its own event log row.

| Field | Direction |
| --- | --- |
| Scenario name | Disaster Barrage unless final scenario localisation chooses another researched and accepted name. |
| Details | Explain that it launches a disaster season using the same controller as live Event 013. Mention delayed impacts, warning logic, reports, aftermath, and throttled news. |
| Type options | Random Barrage, Geological Crisis, Weather Crisis, Skyfall Crisis, and Full Catalogue remain working route labels until final localisation. |
| Intensity scaling | Low, Medium, High, and Maximum should communicate sequence size, delay compression, and abnormal access. |
| Warning | Maximum intensity can be devastating but should not be described as a terminal scenario. |
| History logging | One scenario launch should produce one Event 013 firing row unless implementation gives the scenario its own separate scenario log. |

## Cluster detail direction

The Natural Disasters cluster is unusual because the same repeatable event can occupy several logical member slots at different chaos tiers.

| Cluster field | Direction |
| --- | --- |
| Cluster name | Natural Disasters. If there are several internal cluster entries, keep public naming clear and avoid numbered names unless the UI requires them. |
| Details | Describe a period of repeated or stronger disasters rather than a collection of unrelated event ids. |
| Members | Event 013 appears as multiple logical member entries by tier or evolution access. Do not add Event 046, 051, or 099 as normal cluster members. |
| Severity | Baseline entries are Low. Evolution II and III logical entries can display higher danger if the cluster UI supports per-member danger. |
| Cooldown | Bigger abnormal disasters should not repeat too frequently through clusters. |
| News behavior | Cluster details should note that news is throttled for smaller hits in later stages. |

## Documentation structure for `docs/events/013_natural_disasters/overview.md`

| Section | Direction |
| --- | --- |
| What the event is | Explain Event 013 as a repeatable disaster season system. Avoid implementation history. |
| Runtime flow | Explain one firing, delayed subevents, reports, aftermath cards, and chain checks. |
| Disaster families | Summarize family groups and point to the source spec for implementation depth. |
| Recovery system | Explain rescue, stabilization, reconstruction, foreign relief, active caps, and partial success. |
| Evolutions | Explain Baseline, Evolution I, Evolution II, and Evolution III behavior. |
| Abnormal GUI | Explain when the abnormal map appears and what it shows. |
| Disaster Barrage | Explain scenario controls and intensity. |
| Related event handling | Document Event 046 placeholder, Event 099 bridge or placeholder, and Event 051 non-stacking rule after implementation. |
| AI behavior | Summarize AI priorities for warning, recovery, chain prevention, and abnormal path selection. |
| Assets and super-events | List final wired assets and super-events only after they exist. |
| Limitations | Only list actual implementation limitations or unresolved blockers, not planned features. |

## Player-facing wording guardrails

- Use direction-only wording in specs and prompts until implementation writes final localisation.
- Do not write final super-event titles, quotes, button text, slogans, lyric fragments, or cultural remarks before research.
- Do not frame disasters as messages from a global institution.
- Do not use generic bad-weather wording for every family.
- Do not expose hidden formulas in Event Details or spreadsheet fields.
- Do not describe absent systems as features. Keep absent surfaces blank or omitted unless the UI requires a field.
- Do not present Event 046, Event 099, or Event 051 as active Event 013 families in the catalog. Use placeholder or bridge wording only after implementation.
