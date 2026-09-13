# Event 58: Achievement design

Achievement names below are working labels. Final player-facing titles and descriptions must be written during implementation after localisation review. The IDs are stable planning IDs unless a collision audit requires a controlled rename.

All achievements use Event 58 placement provenance. A building that existed before the event or was built normally does not count.

Normal achievement validity rules apply. Force Trigger Mode, direct hidden-event calls, debug setup, observer play, and unsupported tag switching do not grant credit.

## Achievement 1: Every Plot Accounted For

- Planned ID: `058_random_buildings_every_plot_accounted_for`
- Visibility: visible
- Difficulty: medium
- Eligible country: the current player-controlled country

### Unlock condition

During one natural or cluster-driven Event 58 firing:

- the player country owns and controls at least `10` land states at transaction start
- every one of those states receives a successful baseline state-building result
- no player-owned and controlled state is baseline-exhausted
- the player remains on the same country through result finalization

The denominator includes all player-owned and controlled land states, including states whose buildings were already near capacity. This makes free capacity and valid candidate coverage matter.

### Why it is not trivial

The player must preserve enough building capacity across a sizeable country. Repeated Event 58 firings, normal construction, conquest, and high development can make the condition harder.

### Tracking

The transaction stores:

- player country at transaction start
- player-owned and controlled land-state count
- baseline success count across that exact set
- baseline exhaustion count across that exact set
- normal or cluster launch proof
- force and debug disqualifier state

The achievement checks once after the baseline layer and all callback failures have resolved.

### Icon direction

A dense period city and industrial landscape divided into orderly construction plots, with every plot marked by a simple completed symbol. The icon should read as total coverage at the verified final achievement size without text.

## Achievement 2: Mixed-Use Empire

- Planned ID: `058_random_buildings_mixed_use_empire`
- Visibility: visible
- Difficulty: hard
- Eligible country: the current player-controlled country

### Unlock condition

Across one campaign, the same player country must receive and still possess Event 58 results from at least `8` distinct display families.

The collected set must include all of these broad roles:

- industry
- transport or infrastructure
- air, detection, or state defense
- fuel, energy, or synthetic industry
- provincial fortification, rail, port, or supply
- one advanced, rare, restricted, or exceptional family

The remaining families can come from any registered Event 58 provider.

At unlock, the country must still own and control at least one state containing a surviving Event 58 result for every counted family.

### Display-family examples

Possible families include:

- infrastructure
- civilian industry
- military industry
- naval industry
- air base
- anti-air
- radar
- fuel storage
- synthetic industry
- advanced energy
- research or rocket site
- repression site
- land fortification
- coastal fortification
- railway
- naval base
- supply hub
- exceptional landmark or facility

Provider owners choose one stable family for each entry. Closely related levels of the same building do not count as separate families.

### Why it is not trivial

The achievement requires several Event 58 firings or a large and geographically varied country at higher Chaos. The player must retain the states and structures. Temporary credit does not qualify.

### Tracking

Each successful provider callback can publish one country-scoped Event 58 family marker when the current player country controls the recipient state.

Before unlock, the check confirms that every mandatory role remains represented by a surviving structure in current player territory. A stale marker alone is insufficient.

Country switching resets or disqualifies the current run unless the project's achievement framework already has a stricter standard.

### Icon direction

A compact patchwork of a factory, railway, radar mast, fuel or energy structure, and fort or port assembled into one coherent period construction emblem. Avoid a grid of tiny unreadable icons.

## Achievement 3: The Exceptional Case

- Planned ID: `058_random_buildings_the_exceptional_case`
- Visibility: hidden
- Difficulty: very hard
- Eligible country: the current player-controlled country

### Initial trigger

During a natural or cluster-driven Event 58 firing at `600+` Chaos:

- Evolution III is enabled
- an exceptional structure is placed in a core state owned and controlled by the player country
- the provider reports a persistent structure identity that can be checked later
- the player remains on the same country

### Completion condition

After the initial trigger, the player must:

- retain uninterrupted ownership and control of the recipient state for `365` days
- keep the exceptional structure present and valid under its owner system
- avoid force-trigger, debug, or tag-switch disqualification

Temporary loss of ownership, temporary loss of control, structure destruction, owner-system invalidation, or state removal resets the retention progress.

### Why it is not trivial

Exceptional placement is globally limited and depends on a valid provider location. The player then has to protect the state and structure for a full year.

### Tracking

The provider returns a persistent location proof and structure-exists check. Event 58 stores the recipient state, player country, provider identity, and retention start date through the normal achievement framework.

The retention check should use a bounded country or state hook. It must not create a new whole-world daily scan. A state or country timed mission, scheduled check, or existing achievement pulse can own the countdown.

### Icon direction

One monumental dam, facility, or rare engineered structure rising over a small landscape, framed as a protected prize. The design must stay generic enough to represent several exceptional provider families.

## Achievement implementation rules

The achievement implementation must:

- inspect the existing Chaos Redux achievement registry and tracking patterns
- keep all achievement definitions in the single root achievement registry used by the project
- create completed, grey, and not-eligible icon variants under the root achievement asset convention
- add title, description, requirement, and debug localisation
- use Event 58 transaction proofs and reject inferred building totals
- reject direct hidden-resolver or force-trigger credit
- handle multiplayer and player-country identity consistently
- preserve save and reload progress
- document every persistent flag, variable, target, or provider proof
- clear temporary transaction values after checks
- audit ID, localisation, and asset collisions

The final implementation can tighten disqualifiers to match the existing project achievement standard. It must not weaken the core conditions or convert the achievements into automatic rewards for merely seeing the event.
