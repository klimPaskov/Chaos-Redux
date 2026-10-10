# Asteroid Incoming, Part 8: Events, Logs and Text Direction

Status: implemented; native delivery order of the news queue (L1) is a live check.
Final text is in `localisation/english/028_asteroid_impact_l_english.yml` and `028_asteroid_incoming_news_plain_l_english.yml`.

## Event chain

| Role | Identifier | Notes |
| --- | --- | --- |
| Opening board | `chaosx.nr28.1` | Three strike options, the near miss, or the `N/A` option |
| Confirmation | `chaosx.nr28.2` | Repeats the target; no new roll |
| Target preparedness | `chaosx.nr28.3` | One stance; says whether the locked state is the capital |
| Hidden resolver | `chaosx.nr28.4` | The whole impact transaction |
| Main-footprint country report | `chaosx.nr28.5` | One per affected country |
| National recovery closeout | `chaosx.nr28.6` | One per country when local recovery ends |
| Fragment-only country report | `chaosx.nr28.7` | One per affected country |
| Reopened board | `chaosx.nr28.8` | Same pairs after cancelling |
| Fragment visual callback | `chaosx.nr28.9` | Hidden, one fragment every four hours |
| News queue callback | `chaosx.nr28.10` | Hidden |
| Impact presentation start | `chaosx.nr28.11` | Hidden, waits for the forecast to close |
| Price re-quote after surcharge | `chaosx.nr28.12` | Hidden; retired if Open question 2 is accepted |
| Opening warning | `chaosx.news.29` | "Asteroid Incoming" |
| Locked course | `chaosx.news.30` | Names state, country, continent and date |
| Close passage | `chaosx.news.96` | Near-miss outcome |
| Failed course | `chaosx.news.97` | Fail-closed outcome |
| Impact bulletin | `chaosx.news.32` | Fragment count and struck continents |
| Dust milestones | `chaosx.news.92`, `93`, `94` | Below Impact Winter, Residual Haze, clear sky |
| Impact super-event | Shared slot 116 | Names the target and region |

Presentation order: open asteroid news and pending human reports come before the super-event, and queued asteroid news waits while any super-event is visible.
Each bulletin is accepted once and each recipient consumes its own receipt, so a bulletin cannot repeat; an unprinted opening warning is replaced by the locked course or the outcome, and the latest dust bulletin replaces older unprinted ones.
A quick-confirmed strike gives an unaffected player two bulletins and one super-event.

## Writing direction

Player-facing text follows the `chaos-redux-events` writing rules: concrete, short, period-appropriate, and free of implementation or update-history wording.

- **Board.** Scientists and a government holding a short-lived power to steer the object. Controlled, technical and morally severe; no heroic planetary-defence framing, no invented equations, no jokes about mass death. Options are cold and brief and never celebrate destruction.
- **Preparedness.** The targeted government with forty-eight hours to save what lies outside the centre. Urgent and practical: command, transport, hospitals, shelters, water. No false hope for the centre.
- **Country reports.** The first consolidated assessment: worst-hit state, deaths, damaged states, lost transport and industry, the capital outcome when relevant, and the next useful order. Specific and restrained; never a stat sheet, one line per state, or raw variables.
- **Impact bulletin.** Global factual coverage that does not compete with the super-event.
- **Dust bulletins.** Weather services, rail networks, factories and civilians under a changed sky; a different concrete observation at each stage, never the formula.
- **Close passage.** Relief mixed with scientific interest; observatories keep tracking; no hint that the object will return.

Target sample for the locked-course bulletin opening: "Observatories have locked the asteroid's course on Silesia in Germany, in Europe. Impact is expected on 9 March 1938."
The current `chaosx.news.30.d` and `chaosx.nr28.2.d` strings read "on [continent]", which should become "in [continent]".

## Event history

Event 028 writes one Major history row when it fires, later updated in place with the outcome; preparedness, reports, fragments, dust bulletins and the super-event never add rows.
Rows use the shared two-line form (header plus one summary line, 41 pixels high).
The flags show the chooser and, after a strike, the target country.
The summary line gives the outcome: the offered board, "Impact on [state]: [deaths] dead, [n] fragments", the near-miss date, or the closed trajectory.
Every other record field lives in Event Details.

## Event Details

Before firing, Event Details describes the premise without target scores or formulas, and shows `N/A` with the reason when no valid board exists.

After a near miss it shows the outcome and the date of closest passage.
After a fail-closed course it shows that outcome.

After a strike it shows:

- who chose the trajectory;
- the original target state, its continent and capital status;
- the impact date, deaths, affected states and countries;
- whether the government could move, when the capital was struck;
- the fragment-site count;
- the opening and current dust stage, with the current Dust Load as a record value;
- the current main-crater and fragment-site controllers under Extraordinary Minerals.

Current controllers update live; historical target information never changes.

## Evolution views

The Global Fragmentation preview describes worldwide fragment strikes with smaller rings and more dust, without locations.
The Extraordinary Minerals preview states the plus 100 and plus 20 percent armour values, because they are visible mechanics.
Each applied evolution writes one global row with no actor; the Evolutions tab and the related-evolution view show source event, tier, stage and date.

## Target names

Accepted decision F06 (Part 2): text names the target through the persistent pointers saved at the lock.
An annexed target still shows its former name and flag; region text uses the locked state's continent; current reports use the country that holds the damaged territory.
No text may show a missing scope or raw key.

## Super-event

The super-event is the first global reveal of a completed strike.
It names where the main body struck, says the surrounding regions were damaged, mentions fragments by count and continent when they applied, and notes the developing atmospheric effects.
The quote, button remark and music were chosen through sourced research in `docs/super_events/028_asteroid_incoming_super_event_research.md`; the music is a public-domain Brahms recording played through the shared settings-aware audio path.

## Availability and default queue

Event 028 is in the default event queue under the user's instruction that every event from 1 to 40 is playable.
It shows `N/A` instead of a misleading zero weight when no valid board can be built.

## Spreadsheet

The catalog row (Events row 29) is Major with status Needs Testing.
Its Details, Evo I and Evo II cells match `asteroid_incoming.event_details.description` and the two evolution bodies in meaning, with colour codes removed and constants rendered.
Any later wording change edits the authoritative workbook first and regenerates the CSV exports with `python .tools/export_event_catalog_csv.py`; the catalog never lists target scores, AI weights, formulas or implementation history.
