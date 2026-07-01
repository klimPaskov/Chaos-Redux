# Achievement Prompt for Event 013 Natural Disasters

Use the existing Chaos Redux achievement implementation patterns. Titles below are working labels, not final localisation. Final achievement names and descriptions should be written during implementation from these directions.

## Planned achievements

| Working id | Working label | Visibility | Eligible play | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `013_natural_disasters_against_the_season` | Against the Season | Visible | Any country | During one Event 013 season, recover every active disaster aftermath in owned core states before delayed deaths or famine pressure worsens | Losing capital during season, disabling deaths system if achievements require it | Medium | Relief crews reopening a broken road under storm clouds |
| `013_natural_disasters_faultline_accountant` | Faultline Accountant | Visible | Country hit by earthquake chain | Survive an earthquake with aftershock and tsunami follow-up while restoring supply and port access before all recovery missions expire | Letting port or hub remain disabled at mission end | Hard | Ledger, cracked ground, rail bridge symbol |
| `013_natural_disasters_eye_of_the_road` | Eye of the Road | Hidden | Any country threatened by storm corridor | Use the storm corridor GUI response actions to protect three predicted path states before the corridor arrives | Failing any protected state or not using prediction actions | Hard | Tornado path marker over a map card, no text |
| `013_natural_disasters_ash_winter_bureau` | Ash Winter Bureau | Visible | Country affected by massive eruption ash | Clear ash, keep food distribution stable, and prevent famine pressure after a massive eruption | Famine pressure escalates or capital supply is lost | Hard | Ash-covered railway and relief mask symbol |
| `013_natural_disasters_skyfall_drill` | Skyfall Drill | Hidden | Any country directly hit by meteor shower | Survive a meteor shower impact in a core state and restore local infrastructure before the next Event 013 season | Losing the affected state before recovery completes | Very hard | Meteor fragment above emergency shelter |
| `013_natural_disasters_ring_of_firebreaks` | Ring of Firebreaks | Visible | Country with wildfire aftermath | Stop three wildfire follow-up chains by completing firebreak or evacuation responses before they spread | Any wildfire follow-up reaches a high severity state | Medium | Firebreak line, forest silhouette, shovel symbol |
| `013_natural_disasters_dust_has_no_master` | Dust Has No Master | Visible | Desert or arid-region country | Recover from a sand or dust storm while at war without losing supply in the affected front state | Losing the state or failing supply mission | Medium | Dust wall and covered railway symbol |
| `013_natural_disasters_barrage_survivor` | Barrage Survivor | Hidden | Any country, manual scenario allowed only if achievements permit manual scenario unlocks | Complete a maximum Disaster Barrage with at least one abnormal disaster active and recover all owned-state aftermath | Manual scenario achievements disabled by project policy, if applicable | Very hard | Composite disaster emblem with meteor, wave, and storm marker |

## Tracking notes

- Achievements should track meaningful recovery and survival, not merely Event 013 firing.
- If manual scenario launches are not allowed to unlock achievements by project policy, `013_natural_disasters_barrage_survivor` should be disabled or converted into a non-achievement challenge note.
- Hidden achievements should reveal only the public conditions and avoid exposing secret hidden rolls.
- Each achievement needs a 64x64 completed icon direction and grey or not-eligible variants if the achievement system requires them.
- Disqualifiers should prevent exploit unlocks from disabling systems, tag-switching out of danger, or letting puppets absorb all damage.
