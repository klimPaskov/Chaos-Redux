# Holy Realm Achievement Specification

Achievements should be difficult and should reward mastery of the route. Do not add achievements that unlock only because the event fired.

## Achievement list

### `HOLY_REALM_NO_EMPIRE_OF_THE_WHEEL`

Title: No Empire of the Wheel.

Eligible country: Holy Realm.

Requirement:

- Become the Buddha.
- Complete `No Empire of the Wheel` or equivalent clean-route focus.
- Do not declare an offensive war against any normal non-chaos country.
- Defeat or help defeat at least one chaos country.

Disqualifiers:

- Ordinary conquest abuse flag.
- False Mandala route.

Icon: wheel above a closed sword.

Difficulty: hard.

Why it matters: rewards using the Holy Realm as a spiritual and anti-chaos actor, not a conquest tag.

### `HOLY_REALM_FOUR_DHYANAS_UNDER_FIRE`

Title: Four Dhyānas Under Fire.

Requirement:

- Reach Dhyana Depth 4 while at war with a chaos country or while a compact member capital is threatened.
- Capital sanctuary remains controlled.

Disqualifiers:

- None, but failure if capital falls before reaching Dhyana 4.

Icon: seated figure with shells falling in the distance.

Difficulty: hard.

### `HOLY_REALM_ONE_BECOMES_MANY`

Title: One Becomes Many.

Requirement:

- After Buddhahood, activate One Becomes Many.
- Complete at least three teaching or relief missions while the power is active.
- At least one target must be at war with a chaos country.

Icon: repeated silhouettes around one lamp.

Difficulty: medium hard.

### `HOLY_REALM_WALL_RIVER_SKY`

Title: Wall, River, Sky.

Requirement:

- In one war against a chaos country, activate Passing Through Walls, Walking on Water, and Seated in the Sky.
- Win the war or force the chaos country to lose its capital.

Disqualifiers:

- Any power used against a normal country in the same campaign.

Icon: mountain wall, river, and sky lotus.

Difficulty: hard.

### `HOLY_REALM_EMPTY_SEAT`

Title: The Empty Seat.

Requirement:

- Complete the non-terminal Final Silence route.
- Leader changes to Empty Seat.
- At least three compact members survive.

Disqualifiers:

- World-end branch.
- False Buddha route.

Icon: empty throne with lotus and bell.

Difficulty: very hard.

### `HOLY_REALM_FINAL_SILENCE_WORLD_END`

Title: The Final Silence.

Requirement:

- Complete terminal Final Silence with chaos value above 1000.
- World-end flag is `world_end_final_silence`.
- Capital sanctuary has not fallen in the last 180 days.

Icon: extinguished world map with a single lotus.

Difficulty: extreme.

### `HOLY_REALM_NO_FALSE_BUDDHA`

Title: No False Buddha.

Requirement:

- Become the Buddha with no active False Buddha Schism.
- Defilements never exceed 50 after Bodhi Progress reaches 75.

Icon: clean mandala with unbroken mirror.

Difficulty: medium hard.

### `HOLY_REALM_DEBATE_THE_PRETENDER`

Title: Debate the Pretender.

Requirement:

- Trigger the False Buddha Schism.
- Resolve it through debate or reconciliation.
- Do not use military suppression.

Icon: two seated figures divided by a cracked wheel.

Difficulty: hard.

Hidden: yes.

### `HOLY_REALM_SANGHA_OF_NATIONS`

Title: Sangha of Nations.

Requirement:

- Form the Sangha Compact.
- Have at least eight non-chaos members.
- Keep Sangha Cohesion above 70 for 180 days.
- No member may be a puppet of the Holy Realm.

Icon: ring of lamps around a mountain.

Difficulty: hard.

### `HOLY_REALM_MERCY_IN_THE_ASHES`

Title: Mercy in the Ashes.

Requirement:

- Complete at least five relief or refugee missions in countries damaged by chaos.
- Keep Defilements below 20.
- At least one mission must occur while the target capital is threatened or occupied.

Icon: hands lifting a lamp from ruins.

Difficulty: medium hard.

### `HOLY_REALM_SUN_AND_MOON`

Title: The Sun and Moon Were Within Reach.

Requirement:

- Activate Touching the Sun and Moon during a global chaos crisis.
- At least two different chaos-country sources must be active or one chaos source must control a major capital.
- Win a major anti-chaos war within 365 days after activation.

Icon: hand reaching toward sun and moon over a mandala.

Difficulty: very hard.

### `HOLY_REALM_LOTUS_BRIDGE`

Title: Lotus Bridge.

Requirement:

- Use Walking on Water to open a relief route to a compact member or friendly country.
- Prevent that country's capital from falling for 180 days.

Icon: lotus path across water.

Difficulty: hard.

## Tracking notes

The implementation needs flags for:

- Offensive war against normal country after Holy Realm reveal.
- Any Buddha power used against a normal country.
- False Buddha Schism triggered, resolved by debate, resolved by suppression, or absorbed.
- Capital sanctuary fallen within the last 180 days.
- Compact member count and cohesion history.
- Final Silence terminal versus non-terminal completion.
- Dhyana Depth reached while under chaos war or capital threat.
- Missions completed while One Becomes Many active.

Achievement icons should follow the asset prompt and use 64x64 completed icons first.
