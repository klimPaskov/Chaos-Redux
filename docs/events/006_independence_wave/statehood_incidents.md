# Event 006 statehood incidents

## What it is

Every active Event 006 country draws recurring incidents from its own pulse for as long as its origin lives.
The incidents cover the six baseline categories of Part 2 (founding, recognition, security, government, League and formable) and add evolution incidents for each of the five evolutions.
They sit beside the package incidents (`package_incidents.md`), which tell each Level 2 package's own history, and the paid evolution incident decisions (`evolutions.md`).

## Event map

| Event | Category | Title | Eligible when |
| --- | --- | --- | --- |
| `chaosx.nr6.150` | pulse | hidden | queued by the country itself |
| `.151` | founding | Notes Without a Treasury | emergency or provisional phase, State Capacity below 45 |
| `.152` | founding | The Clerks Who Stayed Home | founding phases, living former host, State Capacity below 70 |
| `.153` | founding | Who Runs the Junction | founding phases, living former host, host relation not settled |
| `.154` | founding | Carts at the Border Posts | living former host under a severe threat or with Hostility of at least 40 |
| `.155` | recognition | A Legation Above the Pharmacy | Recognition from 15 to below 60 |
| `.156` | recognition | Recognition at a Price | provisional phase or later, Recognition below 60, Security of at least 20 |
| `.157` | recognition | Short by Three Votes | provisional phase or later, Recognition from 15 to below 35 |
| `.158` | security | The Militia Keeps Its Rifles | Security below 65 and Instability of at least 20 or disputed Legitimacy |
| `.159` | security | Guards Across the River | living former host, relation not settled, Security below 85 |
| `.160` | security | Captains Without Companies | Security below 40, or at war |
| `.161` | government | The Assembly in the School Hall | provisional phase or later, undecided, constitutional or popular council route |
| `.162` | government | Six More Months | provisional phase or later, emergency military route, or Security of at least 40 without established Legitimacy |
| `.163` | government | The Provincial Councils | provisional phase or later, controls at least two states |
| `.164` | government | Ministers Chosen Abroad | provisional phase or later, patron influence at the warning level but below control |
| `.165` | League | A Member Asks for Rifles | League member, another member at war |
| `.166` | League | A Motion for Collective War | League member, armed-liberation or revisionist League route or another radical member |
| `.167` | League | Rights Before Rifles | League member that has not ratified the Sovereign Congress rights charter |
| `.168` | formable | Whose Flag for the Union | formable discovered, not yet formed |
| `.169` | formable | Seats at the Founding Congress | formable method chosen or founding proposal open, not yet formed |
| `.170` | formable | The Army Wants One Command | formable formed, first integration stage not complete |
| `.171` | Replicable Independence | Clerks from Another New State | another Event 006 country active, State Capacity below 70 |
| `.172` | Replicable Independence | The Old Capitals Compare Files | living former host, relation not settled |
| `.173` | Dormant Nations | The Claimant at the Station | undecided or traditional route |
| `.174` | Dormant Nations | The Language of the Schoolroom | provisional phase or later |
| `.175` | Armed Birth | Colonels in the Ministry Corridors | Security of at least 40 and State Capacity below 45 |
| `.176` | Armed Birth | Rifles Without Cartridges | State Capacity below 70, at war or Security below 65 |
| `.177` | Sovereign Congress | The Common Defence Clause | League member |
| `.178` | Sovereign Congress | Envelopes at the Secretariat | League member, patron warning or League Patron Capture of at least 30 |
| `.179` | Sovereign Congress | When a Member Is Invaded | League member, another member at war with its own former host |
| `.180` | Open Sovereignty | A Constitution Written in the Streets | undecided, radical or popular council route, Instability of at least 20 |
| `.181` | Open Sovereignty | Plans Against the Old Capitals | living former host under a severe threat or with Hostility of at least 50, another Event 006 country active |

Every evolution incident also needs its evolution active and enabled in the Event Logs, so disabling an evolution removes its incidents from the pool.

## Runtime flow

1. When a released country resolves its founding posture (`chaosx.nr6.41`/`.42` resolution effects), `independence_wave_start_statehood_incidents` queues the first pulse `first_delay_days` (60) later.
2. Queuing stores the generation and a due date one margin day before the event, converted with `chaosx_convert_days_to_date_offset`.
3. The pulse runs only for the live generation, on or after its due date. It computes one weight per category from the country's state, gives every eligible incident its category weight and every ineligible incident zero, adds a quiet-season weight, and draws once with `random_list`.
4. The drawn incident is marked done for this generation, becomes the open incident, puts its category on a cooldown date (240 days, 150 for the evolution category) and fires at once.
5. The pulse queues the next pulse after a random 90 to 139 days.
6. The generation reset and origin end call `independence_wave_clear_statehood_incident_runtime`, which clears the queue flag, generation, due date, open incident, cooldown dates and done flags.

No effect iterates countries or runs from a periodic world hook. The only array walks are the bounded Event 006 active-country and League-member registries.

## Weights

| Category | Base | Doubled when |
| --- | --- | --- |
| founding | 10 | emergency founding phase |
| recognition | 10 | Recognition below de facto (35) |
| security | 10 | at war or under a severe host threat |
| government | 10 | government route undecided |
| League | 10 | League founder, or League in crisis |
| formable | 10 | founding proposal open |
| evolution | 10 | never |
| quiet season | 8 | doubled when Instability is below 20 with established Legitimacy, halved in severe Instability |

All values live in `common/script_constants/006_independence_wave_statehood_incident_constants.txt`.

## Options and AI

Every incident has a free answer. Costly answers spend 35 political power, the light diplomatic cost (command power and convoys or trains) or the light security cost (command power, infantry and support equipment). Arms sent to a League member in `.165` and `.179` arrive in that member's stockpile.
Options trade the five Statehood values against the former-host relation, League Cohesion, Common Cause, Patron Capture, Shared Reserve, Member Confidence and Network Standing. Three options add real resources: 1500 manpower from registered refugees, 600 manpower from defecting guards, and 10 army experience from recalled officers.
`ai_chance` uses the `independence_wave_decision_ai` bases and doubles the answer that fits the country's route, war or host threat.
The AI also reads the world milestones (`milestones.md`): after the first host annexation it doubles the security answers (`.156`, `.159`, `.160`, `.181`), after the first rescue the arms answers (`.165`, `.179`), after the first broad recognition the paid recognition answers (`.155`, `.157`), after the first peaceful treaty the conciliatory host answers (`.153`, `.156`, `.172`), after the first radical bloc the collective war motion (`.166`), and after the first union the shared union answers (`.168`, `.169`).

## Pacing safety

The delay window keeps `first_delay_days + interval_minimum_days` above `interval_maximum_days` and `interval_maximum_days` below twice `interval_minimum_days`. A pulse event left over from an earlier release of the same tag therefore always arrives before the current chain's due date, finds the date unreached, and does nothing.

## Pictures

All pictures are existing registered report pictures: vanilla `eventpictures.gfx` sprites and the Event 006 host-crisis, first-recognition and charter-convention sprites in `interface/006_independence_wave_small_assets.gfx`. No new art is required.

## Files

- `events/006_independence_wave_statehood_incident_events.txt`
- `common/scripted_effects/006_independence_wave_statehood_incident_effects.txt` and `.md`
- `common/scripted_triggers/006_independence_wave_statehood_incident_triggers.txt`
- `common/script_constants/006_independence_wave_statehood_incident_constants.txt`
- `localisation/english/006_independence_wave_statehood_incidents_l_english.yml`

## Limitations

- Each incident fires at most once per generation. A country that survives long enough exhausts the pool and then sees only quiet seasons until its next generation.
- The probability route (`hoi4.probability_inspect`, `event_option_ai_chance`) returned `INTERNAL_ERROR` for this file, so the option weights have no MCP evidence.

## Future expansion

- A second tier of incidents for the recognized and regional-power phases, such as embassy disputes, arms-purchase scandals and trade wars.
- Follow-up chains for the riskier answers, for example a coup attempt after the colonels are posted to the frontier.
- Package-specific overrides that replace a generic incident with a regional variant when a package registers one.
