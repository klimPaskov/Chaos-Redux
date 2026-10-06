# Event 097 Collaboration: Achievement Prompt

Implement the six Event 097 achievements defined in `docs/specs/097_collaboration_specs/specs/097_collaboration_spec_part_6_ai_presentation_achievements.md`. Inspect the existing Chaos Redux achievement registry, its event sections, its forced-setup disqualifiers, its localisation file, and its `.gfx` registration before writing anything. Keep Event 097 achievements in their own section of the single root achievement registry. The keys below follow the repository convention `<id>_<slug>_<name>` used by other event-owned achievements, such as the Event 008 section, and are the proposed final ids. Confirm that no id collides with an existing entry before writing.

Titles and descriptions are direction only. Write final localisation in the Chaos Redux voice. Descriptions state the requirement clearly in the achievement UI. Event text, decision text, and reports must never mention achievements or achievement routes.

## Shared rules

- Every achievement is visible, with the requirement stated in its description.
- Every achievement uses the forced-setup set other Chaos Redux achievement triggers combine, because no single shared trigger exists: human player, debug mode off, force-trigger mode off, test country not initialized, no Event 097 manual-trigger disqualifier, and no triggerable-scenario launch. Write the Event 097 manual-trigger disqualifier when Event 097 is fired from Event Details or the forced trigger path. Put these checks in one Event 097 achievement trigger file.
- Tracking uses flags and variables written at the moment the relevant outcome happens. No achievement may rely on a periodic whole-world scan.
- Record every tracking flag and variable in `docs/events/097_collaboration/` together with its writer and reader.
- Each achievement needs the completed, grey, and not-eligible icon states through the repository achievement workflow, using the motifs in the asset prompt.

## Achievements

### `097_collaboration_open_doors`

- Title direction: three doors that were already open when the armies arrived.
- Description direction: make three countries capitulate to you in one campaign while each was collapsing from within with your network as the strongest inside it, without ever screening your own state.
- Eligible: any participant.
- Unlock: three distinct capitulations credited to the player in one campaign, each with the loser's recorded highest Fifth Column band equal to Collapsing and the player recorded as the strongest network at capitulation.
- Disqualifier: the player chose Screen in any Event 097 firing.
- Tracking: a per-country count of qualifying capitulations, written in the capitulation hook. A per-country marker for any Screen choice, written when the stance is chosen.
- Difficulty: hard.
- Why it is hard: three separate wars must each reach the deepest internal collapse, and the player must have built the strongest network through Cultivate choices.

### `097_collaboration_clean_ministries`

- Title direction: no one left inside to open the gates.
- Description direction: screen your state in at least three firings, then survive a war against a major power in which your ministries began defecting, without capitulating and without losing your capital.
- Eligible: any participant.
- Unlock: at least three Screen choices recorded, then a war against a major power in which the player's recorded highest band reached Defecting or Collapsing, ending in peace with the player never capitulating and never losing control of the capital during that war.
- Disqualifier: losing control of the capital at any point in that war.
- Tracking: Screen count, highest band per war, a capital-lost marker per war cleared at war start, checked when the player leaves the war.
- Difficulty: hard.

### `097_collaboration_three_continents`

- Title direction: administrations on three continents.
- Description direction: hold governments installed through prepared networks on three different continents at the same time.
- Eligible: any participant.
- Unlock: the registry shows at least three living governments installed through Event 097 with the player as installer, whose capitals lie on three different continents, at the same moment.
- Tracking: the registry records capital continent at installation and updates it when a government turns or ends. Checked on installation and on turning.
- Difficulty: very hard.

### `097_collaboration_turned_regime`

- Title direction: a government with two masters.
- Description direction: win a government away from its installer during a war, then make that former installer surrender.
- Eligible: any participant.
- Unlock: the player received a government through Turned Regime and later the former installer capitulates to the player while that government is still the player's subject.
- Tracking: the registry row records the route and the former installer. Checked in the capitulation hook.
- Difficulty: very hard and rare.

### `097_collaboration_return_from_exile`

- Title direction: the cabinet comes home.
- Description direction: charter a government in exile, lose your country to a prepared government, and return to your capital within three years after that government is gone.
- Eligible: the original country of a government installed through Event 097.
- Unlock: the player took Charter a Government in Exile in the war in which it capitulated, a government was installed over its cores through Event 097, and the player owns its capital again within three years of installation while that government no longer exists.
- Disqualifier: a separate peace with the installer before the return.
- Tracking: a charter marker on the original country, the registry history row with installation date, and a check when the original country regains its capital or returns from exile.
- Difficulty: hard.

### `097_collaboration_quiet_capitulation`

- Title direction: a major power taken by telephone.
- Description direction: make a major power surrender to you while you hold less than half of its core territory, its state apparatus is turning against it, and your network runs through all of it.
- Eligible: any participant.
- Unlock: a major power capitulates to the player with an active Fifth Column, the player's network inside it in the Total band, and the player controlling fewer than half of its core states.
- Tracking: core states are counted once in the capitulation hook over the loser's core states.
- Difficulty: very hard.

## Completion

The achievement task is complete only when every achievement has registry entries, unlock and disqualifier logic, tracking flags documented, localisation, three icon states wired, and a documented test scenario per achievement. Simplified or automatic unlocks are not acceptable.
