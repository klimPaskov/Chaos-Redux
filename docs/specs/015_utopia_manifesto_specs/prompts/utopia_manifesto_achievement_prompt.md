# Achievement prompt for Event 015, `utopia_manifesto`

Implement achievements only after the core event, focus tree, decisions, mechanics, and assets are present. Do not unlock any achievement just for accepting the manifesto.

Every achievement needs localisation, tracking, disqualifiers, icon, grey variant, not-eligible variant if the achievement system requires it, docs, and validation.

## Planned achievements

| Working id | Title direction, not final text | Eligible country | Unlock conditions | Disqualifiers | Visibility | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `015_utopia_new_utopia` | peaceful proclamation of a durable New Utopia | any eligible accepting player country | proclaim New Utopia with high Consent, high Surplus, stable Vocation Balance, low Overreach, and completed geography branch | ever completed Marked Bounds final focus, Overreach above safe threshold | visible | hard | bright civic seal, island, open storehouse |
| `015_utopia_need_not_greed` | gain land by proven need without conquest | accepting player country | gain at least three states through arbitration, settlement charter, or consent integration without offensive war goals | offensive war for claims, forced settlement | hidden | hard | scale with bread and boundary map |
| `015_utopia_friends_without_treaties` | build a network of Friends before a formal League | accepting player country | create at least five Friend statuses and send aid to each before creating the League | Marked Bounds active, Friend country annexed by player | visible | medium-hard | clasped hands around common store |
| `015_utopia_six_hour_country` | complete the six-hour ambition without shortage collapse | accepting player country | finish Six-Hour branch, keep all vocation tracks viable for a sustained period, keep Consent high | urgent service spam, Vocation Balance below threshold for long period | visible | hard | clock, tools, open book |
| `015_utopia_inland_island` | create an island without a coast | landlocked accepting player country | complete Inland Island route, build rail or supply ring, secure a port by charter, federation, or justified claim | starting with a port, Marked Bounds forced port seizure | hidden | hard | rail ring shaped like island |
| `015_utopia_no_bloody_glory` | win through defense and restraint | accepting player country | win or survive a defensive war using Household Guards, keep own casualties or manpower loss below tuned limit, avoid unjust offensive war | use Marked Bounds war goal during achievement window | visible | hard | shield over open manuscript |
| `015_utopia_storehouses_abroad` | aid others without emptying home stores | accepting player country | send major aid to at least ten eligible minors or Friends while keeping domestic Surplus and Need stable | domestic Need crisis caused by aid, bankruptcy-style store failure | visible | medium-hard | convoy and storehouse |
| `015_utopia_marked_bounds_survivor` | complete hardline route and survive backlash | accepting player country on Marked Bounds | complete Marked Bounds State route, survive foreign reaction or coalition for a tuned duration, integrate at least two marked states | reform out before route finish | hidden | very hard | red boundary stake and compass |
| `015_utopia_renounced_bounds` | open the dangerous route, then reform it | accepting player country | unlock Marked Bounds, cause backlash, complete renunciation and reparations, lower Overreach below threshold | continue forced settlement after renunciation begins | hidden | very hard | broken boundary stake with green sprout |
| `015_utopia_all_useful_arts` | keep every vocation useful | accepting player country | maintain all five vocation shares within viable bands for a long duration while at peace and then at war or crisis | urgent service overuse or sustained shortage | visible | medium-hard | five tools in a balanced ring |
| `015_utopia_league_of_need` | found a stable Utopian League | accepting player country | create League with at least five members, high cohesion, shared stores, and no member under forced dependency | Marked Bounds League variant, member puppeting by player | visible | hard | ring of small flags around storehouse |
| `015_utopia_paper_no_more` | recover from institutional failure | accepting player country | trigger Paper Utopia crisis, recover through reforms, restore Consent and Surplus, and complete a late route | civil collapse or tag loss during recovery | hidden | very hard | torn manuscript repaired with seal |

## Implementation notes

- Use flags and variables to track disqualifiers from the moment acceptance occurs.
- Track offensive wars created by Utopian claim decisions separately from defensive wars.
- Track forced settlement and urgent service spam with counters.
- Track Friend statuses and League membership through robust cleanup, so dead countries do not count.
- Achievement icons belong directly in `gfx/achievements/` using achievement ids for final filenames.
- Do not expose hidden route names in ordinary event, focus, or decision text.
- Achievement localisation can reveal challenge conditions in the achievement UI, but not in ordinary event details.

