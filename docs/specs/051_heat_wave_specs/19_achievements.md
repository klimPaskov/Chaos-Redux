# Achievements

## Achievement design rules

Event 51 achievements should reward mastery of the crisis, difficult protection choices, and rare evolved outcomes. They should not unlock from merely seeing the event.

Every achievement needs:

- stable ID
- visible requirement direction
- exact hidden trigger
- disqualifiers
- one-time unlock guard
- normal achievement registry wiring
- localisation
- base, grey, and not-eligible icon files
- documentation
- save and reload persistence

Proposed IDs are planning identifiers and require collision checks.

# Achievement set

## `051_heat_wave_cooler_heads`

**Working name:** Cooler Heads

**Challenge:** Complete one severe Heat Wave without any owned state remaining in Extreme or Scorched heat long enough to enter lethal exposure.

**Required conditions:**

- Episode peak reaches at least the Extreme global band.
- Country owns at least five populated valid states at episode onset.
- Country remains independent through cleanup.
- No owned state records confirmed lethal exposure.
- Episode cleanup completes.

**Disqualifiers:**

- Country loses most exposed states through transfer before cleanup.
- Force-trigger or debug bypass used when the achievement framework tracks it.
- Country switches to an excluded nonhuman identity.

**Anti-cheese:** Snapshot qualifying owned states at onset. Losing or releasing them does not erase their exposure record for this achievement.

**Icon direction:** A shaded command table with a cool water flask beneath a severe sun, designed as an achievement icon rather than a decision icon.

## `051_heat_wave_every_drop`

**Working name:** Every Drop Accounted For

**Challenge:** Keep the capital's water service from reaching System Failure through an Evolution I episode.

**Required conditions:**

- Evolution I active.
- Capital reaches at least Extreme Heat Stress.
- Capital remains the country's capital or a tracked original-capital target through the lethal phase.
- Water service never reaches System Failure.
- Episode cleanup completes.

**Disqualifiers:**

- Capital moved solely after the episode began to avoid the target, unless forced by occupation.
- Tracked capital is lost without being recovered before cleanup.

**Anti-cheese:** Save the capital target at the first Extreme threshold. A voluntary capital move does not change the tracked state.

**Icon direction:** A guarded reservoir gate below a city skyline and sun.

## `051_heat_wave_the_harvest_holds`

**Working name:** The Harvest Holds

**Challenge:** Protect every qualifying major agricultural state during a severe episode and avoid a heat-triggered Famine request.

**Required conditions:**

- At least two qualifying agricultural states at onset.
- Episode reaches a severe agricultural pressure threshold.
- All tracked harvest missions succeed or partially succeed above the accepted protection floor.
- Famine accepts no new Event 51 incident for the country.

**Disqualifiers:**

- Tracked state is released or transferred voluntarily.
- Agriculture qualification falls only because buildings or population were deliberately removed.

**Anti-cheese:** Freeze the agricultural target set at onset and update only for forced territorial loss.

**Icon direction:** A grain sheaf surviving under a white sun with a visible irrigation channel.

## `051_heat_wave_hold_the_line_not_the_sun`

**Working name:** Hold the Line, Not the Sun

**Challenge:** Win or hold a major hot front while rotating every Critical division before it suffers heat casualties.

**Required conditions:**

- At least twelve divisions operate in Extreme or Scorched states.
- At least one rotation mission completes.
- No tracked Critical division receives a heat casualty transaction.
- Country retains the defined strategic front objective through the episode.

**Disqualifiers:**

- Divisions disbanded to erase exposure.
- Front requirement removed by voluntary territorial transfer.

**Anti-cheese:** Track division identity or supported formation ledger through rotation. Disbanding an exposed formation fails the achievement.

**Icon direction:** Two infantry columns exchanging positions beneath a severe sun.

## `051_heat_wave_night_country`

**Working name:** The Country Works at Night

**Challenge:** Maintain a major industrial economy through an Extreme episode using night shifts without suffering direct heat damage to tracked factories.

**Required conditions:**

- Country begins with a minimum industrial threshold.
- At least three industrial hotspot states enter Dangerous or higher.
- Night-shift conversion is active through the main surge.
- No tracked industrial state receives heat-caused factory damage.
- Production remains above a defined fraction of pre-episode output.

**Disqualifiers:**

- Factories intentionally transferred or removed.
- Country uses controlled shutdown for every tracked state, since the challenge concerns continued operation.

**Icon direction:** Factory windows glowing under a moon while the sun remains beyond the horizon.

## `051_heat_wave_the_rails_remain`

**Working name:** The Rails Remain

**Challenge:** Keep every selected critical corridor operational through a multi-surge episode.

**Required conditions:**

- At least two critical corridors selected by the event.
- Episode contains at least two major surges.
- All corridor missions succeed.
- No tracked corridor becomes fully disconnected.

**Disqualifiers:**

- Critical destinations abandoned voluntarily.
- Track requirement removed by deleting supply consumers or moving the capital solely to evade it.

**Anti-cheese:** Corridor endpoints and purposes are frozen when the mission starts.

**Icon direction:** Straight rail line crossing cracked ground with repair crews and a distant train.

## `051_heat_wave_no_city_abandoned`

**Working name:** No City Abandoned

**Challenge:** Survive Evolution III without an owned major city entering the abandoned or near-uninhabitable condition.

**Required conditions:**

- Evolution III active.
- Global super-event milestone occurs during the episode.
- Country owns at least two major urban states at onset.
- No tracked city enters confirmed near-uninhabitable condition.
- Episode cleanup completes.

**Disqualifiers:**

- Voluntary release or transfer of tracked cities.
- Country ceases to use normal civilian systems.

**Icon direction:** Lit water tower and occupied city under a pale sun.

## `051_heat_wave_green_belt`

**Working name:** The Green Belt

**Challenge:** Preserve a major fertile or forested region from permanent degradation during Evolution II or III.

**Required conditions:**

- At least three connected qualifying states are tracked.
- Every tracked state reaches environmental warning.
- No tracked state advances a permanent degradation stage.
- At least one environmental mitigation or recovery mission succeeds.

**Disqualifiers:**

- Tracked states transferred voluntarily.
- Region already desertified before the episode.

**Anti-cheese:** Region selected from the highest valid connected exposure set, not by player cherry-picking one easy state.

**Icon direction:** Green strip of fields or forest beneath a cracked outer landscape.

## `051_heat_wave_open_road_north`

**Working name:** The Open Road North

**Challenge:** Complete a large heat evacuation and reception chain with no forced-displacement deaths.

**Required conditions:**

- Migration accepts an Event 51 organized movement request above a minimum cohort size.
- A safe destination is reached.
- Reception capacity remains above the failure floor.
- No movement death is recorded under forced displacement for the tracked cohort.
- Settlement, transit, or safe return completes.

**Disqualifiers:**

- Violent pushback, unsafe return, or closed-border action against the tracked cohort.

**Anti-cheese:** Achievement reads the Migration cohort and route result. Event 51 cannot infer success from population change alone.

**Icon direction:** Civilian train or road column moving toward mountains with organized reception visible.

## `051_heat_wave_firebreak`

**Working name:** Firebreak

**Challenge:** Prevent every eligible Event 51 wildfire request from becoming a damaging wildfire during one high-risk episode.

**Required conditions:**

- Evolution I or higher.
- Country has at least three wildfire-suitable states at high heat risk.
- Event 51 submits at least one valid wildfire-risk request or warning.
- Prevention or Event 013 outcome causes no damaging wildfire in tracked states.

**Disqualifiers:**

- States removed from control to avoid risk.
- Natural Disasters system disabled after the risk is established, if the achievement framework treats that as invalid.

**Anti-cheese:** Track eligible states and accepted owner results rather than simply checking that no wildfire event fired globally.

**Icon direction:** A maintained firebreak separating dry forest from settlement.

## `051_heat_wave_after_the_peak`

**Working name:** After the Peak

**Challenge:** Complete every major recovery obligation before Event 51 cleanup.

**Required conditions:**

- Episode creates at least one water, rail, industrial, agricultural, or military recovery obligation.
- Country completes all generated obligations.
- No obligation times out or remains unresolved at cleanup.

**Disqualifiers:**

- Target state intentionally transferred.
- Recovery action bypassed through debug or direct console completion when tracked.

**Anti-cheese:** Only obligations created by real damage or severe failure count. A mild episode cannot grant the achievement.

**Icon direction:** Repair crews restarting pumps and rail beneath a cooling sky.

## `051_heat_wave_again`

**Working name:** We Remember This Heat

**Challenge:** Survive three separate Heat Wave episodes while preserving the same capital and avoiding permanent degradation in the capital state.

**Required conditions:**

- Three completed episode generations.
- Same tracked capital state remains owned at each onset and cleanup.
- Capital reaches at least Dangerous in every episode.
- No permanent degradation in the capital.

**Disqualifiers:**

- Voluntary capital move.
- Tag change that loses achievement continuity under existing rules.

**Anti-cheese:** Count completed generations, not repeated entry-event calls during one episode.

**Icon direction:** Three sun marks above the same intact city and reservoir.

# Achievement implementation notes

## Trigger ownership

Use event-owned persistent flags or variables only for facts that cannot be reconstructed safely from shared owner systems. Read Deaths, Famine, Migration, and Event 013 through their public achievement facts or stable outcomes.

## Difficulty and availability

Achievements tied to Evolution II or III should remain hidden or clearly marked unavailable until the evolution exists, according to the established achievement UI convention.

## Multiplayer

Country achievements should unlock for the country that satisfied the conditions. Global milestones should not grant every player an achievement unless each country met its own tracked requirements.

## Asset count

Twelve achievements require thirty-six final DDS files if the established triplet pattern applies.

## Audit cases

- voluntary state release does not erase failure
- annexation fails or suspends country achievement correctly
- capital move exploit blocked
- division disband exploit blocked
- debug firing does not create false generation count
- save and reload preserves progress
- repeated episode achievements count cleanup, not onset
- owner-system outcomes are read once
