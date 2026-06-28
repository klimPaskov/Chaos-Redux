# Achievement Prompt - Event 010 Death

Implement and asset-wire the Event 010 Death achievements according to the spec. Follow existing Chaos Redux achievement patterns, localisation conventions, asset manifest rules, and tracking practices. Achievements must not be automatic event-fire rewards.

## Achievement table

| ID | Title | Visibility | Eligible player | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `death_no_one_heard_the_first_boat` | No One Heard the First Boat | Hidden | Any report recipient | Find Death and declare war before a mainland coast names it. | Death is named from a mainland coast first. | Hard | Survey boat at empty pier. |
| `death_not_on_my_continent` | Not on My Continent | Visible | Continental neighbor/nearby country | Defeat Death after it is named, before it consumes three mainland states on your continent. | Black Oath. | Medium-hard | Barricaded coastline. |
| `death_the_names_do_not_come_back` | The Names Do Not Come Back | Visible | Any country | Defeat Death after 10M+ consumed population, then complete three dead-zone outpost projects. | Herald path restoration or Black Oath. | Hard | Blank census book and candle. |
| `death_last_ferry` | The Last Ferry | Visible | Island/coastal country | Evacuate at least five threatened island/coastal states before Death consumes them, then survive until the black country is named. | Become Herald. | Hard | Ferry leaving black shore. |
| `death_counted_every_name` | Counted Every Name | Hidden | Compact leader/major | Use census and compact work to defeat Death before the Hollow Hosts gather. | High black-method exposure. | Very hard | Empty ledger. |
| `death_black_tide_reversed` | Black Tide Reversed | Visible | World-end participant | After Last Shores fires, recapture every Death foothold outside the first consumed continent and defeat Death. | Any Herald survives as Herald. | Extreme | Black tide retreating from coasts. |
| `death_friend_of_zol` | Friend of Zol | Hidden | Black Oath country | Become Herald of Zol, survive until Death world-end, keep capital unconsumed one year. | Break the Oath. | Very hard | Black oath seal with living crown. |
| `death_no_witnesses` | No Witnesses | Hidden/rare | Death scenario player or supported Herald path | Death consumes all eligible world states. | Death defeated. | Extreme | Empty radio room / black globe. |
| `death_before_the_name` | Before the Name | Hidden | Any country | Defeat Death before a mainland coast gives it a public name. | Trigger naming or maximum manual scenario. | Very hard | Covered map label with black stain. |
| `death_the_living_conference` | The Living Conference | Visible | Major/threatened leader | Form containment compact with five or more members, keep cohesion above threshold, defeat Death. | Black Oath or compact abandonment. | Hard | Conference table with black empty chair. |
| `death_book_burner` | Book Burner | Hidden | Necromancy user | Open Black Book, use at least one bound-name decision, burn the book before exposure reaches high, defeat Death. | Become Herald or max exposure. | Hard | Burning black book, no readable letters. |
| `death_six_continents_one_color` | Six Continents, One Color | Hidden | Death/observer route if supported | Witness or cause Last Shores footholds on every continent. | Death defeated before world-end. | Extreme | Six black coast shapes around dark center. |

## Tracking notes

Track at least:

- Death discovered before reveal.
- Country declared war before reveal.
- Reveal fired.
- Death consumed mainland-state count by continent.
- Total consumed population bands.
- Ghost tiers unlocked.
- World-end started.
- Footholds created and recaptured.
- Compact created, member count, cohesion maintained.
- Black Oath taken/broken.
- Black-method exposure maximum reached or avoided.
- Dead-zone outpost projects completed by country.
- Death defeated before/after reveal.
- Death consumed all eligible world states.

## Asset notes

Every achievement needs a 64x64 completed icon direction. Use the asset prompt for icon production. Do not use placeholders as final icons unless the completion report clearly marks the achievement icons pending.
