# Event 037 Mysterious People localisation audit

Scope patched: `localisation/english/037_mysterious_population_l_english.yml` (UTF-8 with BOM, LF) and `common/scripted_localisation/037_mysterious_population_scripted_localisation.txt` (no BOM, CRLF, original line endings kept). No script logic, other events, or shared files were touched.

Status: disposition `implemented` for the patched keys. Nothing was checked in a running game, so every scope claim below is from source reading.

## Patched keys

### yml

| Key | Before | After | Reason |
| --- | --- | --- | --- |
| `chaosx.nr37.2.d.baseline` | `... [ROOT.GetNameDef] woke to ...` | `... [ROOT.GetNameDefCap] woke to ...` | Sentence-initial country name printed "the United States" in lower case. |
| `chaosx.nr37.2.d.evolution_i` | `[ROOT.GetNameDef] counts` and `bricklayers are hired at the station before they step off the train` | `[ROOT.GetNameDefCap] counts` and `contractors hire bricklayers on the station platform` | Same capitalisation fix. Removed the banned "X before Y" frame. |
| `chaosx.nr37.2.d.evolution_ii` | `[ROOT.GetNameDef] has` | `[ROOT.GetNameDefCap] has` | Sentence-initial capitalisation. |
| `chaosx.nr37.2.crowded_tt` | `Thousands still have no home or work. Housing, roads and a registration drive will settle them faster through the §YMysterious People§! decisions.` | `[ROOT.GetMysteriousPeopleUnsettled] newcomers still have no home or work. Housing, roads and a registration drive in the §YMysterious People§! decisions will settle them faster.` | "Thousands" was static and wrong for any country with hundreds or millions unsettled. Now reads the real figure. |
| `mysterious_people_report_crowding` | `... The worst crowding is in [mysterious_people_top_hotspot.GetName], where the government can house and register them through the Mysterious People decisions.` | `... The worst crowding is in [ROOT.mysterious_people_top_hotspot.GetName].` | Parchment report pointed at a decision menu. The variable now has the `ROOT.` prefix, matching the repo's precedent for variable-held scopes (`[ROOT.industrial_boom_opening_region.GetName]`). |
| `mysterious_people_top_hotspot_line` | `Most crowded: [mysterious_people_top_hotspot.GetName]` | `Most crowded: [ROOT.mysterious_people_top_hotspot.GetName]` | Same scope prefix. The variable is a country variable that holds a state, set in `mysterious_people_refresh_national_pressure`. |
| `chaosx.nr37.13.a.tt` | `The next Roads and Water project in X costs half.` | `... needs half the usual political power and civilian factories.` | The discount halves both `mysterious_people_quote_roads` and `mysterious_people_quote_roads_pp`, so "costs half" hid which costs. |
| `chaosx.nr37.16.a.tt` | `The next Emergency Housing in X costs half.` | `... needs half the usual political power and civilian factories.` | Same, for the housing quotes. |
| `chaosx.nr37.14.b` | `Send them home until housing is found.` | `Turn the shift away until housing is found.` | The description says the workers have nowhere to sleep, so "home" contradicted it. |
| `chaosx.nr37.15.b.tt` | `Stability §R-2%§! for 90 days. The examinations find nothing that anyone can use.` | `Stability §R-2%§! for 90 days.\nThe examinations explain nothing.` | Vague second clause, and the two facts now sit on separate lines like the other tooltips. |
| `chaosx.nr37.21.d` | `... Many of them hold tickets dated before they arrived.` | `... Many of them hold tickets stamped with dates from years ago.` | The old line hinted at time displacement. The new one keeps the false-history detail without implying an origin. |
| `chaosx.nr37.21.b.tt` | `For 60 days nobody leaves X because of the crowding, and the crowding stays.` | `For 60 days nobody leaves X to escape the crowding, so the backlog stays.` | Unclear causation. Matches `mysterious_people_station_closed` suppressing flight requests. |
| `mysterious_people_cause_flight` | `Many people have fled the crowding here, which is why the backlog fell.` | `Many people have fled the crowding here, so fewer remain without homes.` | "Backlog" is not a term the player sees anywhere else. |
| `mysterious_people_cause_hunger_deaths` | `Hunger has killed people here, which is why the backlog fell.` | `Hunger has killed people here, so fewer remain without homes.` | Same. |
| `mysterious_people_history_stage_0` | `A quiet wave` | `Quiet Wave` | The other three stage names are title case. |
| `mysterious_people.evolution.stage_3.body` | `Manifestations large enough to swamp whole countries, and governments that begin counting origins.` | `Manifestations grow large enough to swamp whole countries, and governments begin counting origins.` | The old text had no main verb. |
| `037_a_billion_more_desc` | `Stay calm while the world is transformed.` | `Keep your country steady as the world's newcomers reach one billion.` | Vague and filler. Now states the actual target. |

### Keys added and removed

- Added `mysterious_people_fmt_billion: "[?mysterious_people_fmt|2] billion"`. Without it, a world newcomer count of 1,000,000 thousand or more (the A Billion More threshold, `mysterious_people_achievement.billion_world_k`) printed as "1000.0 million".
- Removed `mysterious_people_stage_plain_absorbing`, `_strained`, `_overcrowded`, `_emergency`, `_breakdown`. They had no caller.

### Scripted localisation

- All seven live count formatters (`GetMysteriousPeopleNewcomers`, `Unsettled`, `Created`, `WorldCreated`, `WorldNewcomers`, `HistoryCreated`, `HistoryWorld`) now have a fourth tier. The million block adds `check_variable = { mysterious_people_fmt < constant:mysterious_people_value.people_per_k }`, and a new block divides by `people_per_k` twice and returns `mysterious_people_fmt_billion`. The formatter tiers are people below 1, thousand below 1000 thousand, million below 1000 million, billion above.
- Removed `GetMysteriousPeopleStateGrant` and `GetMysteriousPeopleStagePlain`. Neither selector is called from any localisation, interface, decision or event file.
- Header comment now lists billions.

## Findings not patched

- Option effect tooltips for 11.b and 12.b read "Under Open Integration, ..." and "Under Restricted Registration, ...". They are accurate (the stability effect is stance-gated in script) and readable, so they stay.
- 17.a has no custom tooltip. Its opinion modifier produces the native tooltip line, and the modifier name `mysterious_people_shared_families` is localised. No change needed.
- 24.b says newcomers settle 25% slower for a year. The register factor (0.75) multiplies with the Restricted Registration factor (0.75) that the option also sets, so the true combined slowdown is about 44%. The tooltip states the factor the option itself adds. Changing the figure needs a design call, so it is left for the parent.
- The wave comparison key resolves to an empty string on the first firing, leaving a trailing space before the paragraph break in the baseline and evolution report descriptions. Harmless on parchment.
- `mysterious_people_drive_cost_blocked`, `_cost_tooltip` and the other `_cost_*` keys, all `*_desc` keys, and the dynamic modifier `_desc` keys have no script reference by design. The engine selects them from `custom_cost_text`, decision names and modifier ids (`chaos-redux-decisions-missions` cost-payment reference).
- `chaosx.nr37.1.t`, `.6.t`, `.7.t`, `.8.t` are titles of hidden events and are never shown. They stay as event-log and debugging labels.
- 21.d, 10.d and the other flavour descriptions imply a false shared history but never an origin. No text names aliens, time travel, clones, the dead, another world or a government project. The two Event Details lines "Nobody knows where they come from" assert ignorance only.
- Hotspot decision rows use `[FROM.GetMysteriousPeople...]` selectors that read state variables (`mysterious_people_pressure`, `_newcomers_k`, `_unsettled_k`, `_loss_cause`, `_cause`). All exist on states in the effects file. Scopes are valid: FROM is the state in the decision rows, ROOT or This is the country in the category description and the reports, and `mysterious_people_flavour_state` and `mysterious_people_flavour_country` are saved as event targets in `mysterious_people_bind_flavour_target` before each flavour event fires.

## Cross-surface handoff for the spreadsheet owner

Changed player-facing wording that may be mirrored in the event catalog workbook:

- `mysterious_people.evolution.stage_3.body`: "Manifestations grow large enough to swamp whole countries, and governments begin counting origins."
- `mysterious_people_history_stage_0`: "Quiet Wave"
- `037_a_billion_more_desc`: "Keep your country steady as the world's newcomers reach one billion."
- `chaosx.nr37.21.d` last sentence: "Many of them hold tickets stamped with dates from years ago."

## Checks run

- Key coverage: every localisation key referenced from the 037 event, decision, category, dynamic modifier, opinion modifier, achievement, event-log and Chaos Meter files exists. No duplicate keys. Every `localization_key` in the scripted localisation file exists in the yml. Every `[...GetMysteriousPeople...]` selector used in the yml is defined.
- Orphans: the two selectors and five plain-stage keys above were the only unreferenced scripted-localisation entries. Every other unreferenced yml key is an engine-selected `_desc`, `_blocked` or `_tooltip` companion.
- Number match against script constants: settlement shares 10/15/20/25/30/50%, factors 1.25/0.75/0.5/1.5, durations 30/60/90/150/180/300/365 days, stability 1/2/3/5%, output +3% and -2%, stage thresholds 20/40/60/80, project slots 3, billion and ten million thresholds. All tooltips agree with `common/script_constants/037_mysterious_population_constants.txt` and the event options. The one exception is the 24.b compounding noted above.
- `python .tools/report_colour_audit.py`: 0 keys with colour. A separate scan of every `.d`, `report`, `wave`, `fmt`, `cause`, `history` and `event_details` key found no `§`.
- Style scan of every value for em dashes, semicolons, "while", "before", "but", "yet", "not" frames and origin words. Remaining "before" and "while" hits are literal timing or tooltip wording, not staged contrast.
- Encoding after the patch: yml still UTF-8 with BOM and LF, scripted localisation still CRLF with balanced braces.

## Not checked

- Nothing was rendered or run in game. Whether `[ROOT.mysterious_people_top_hotspot.GetName]` and `[ROOT.GetMysteriousPeopleUnsettled]` resolve inside the report description and the option tooltip is inferred from the wiki's namespace rules and repo precedent.
