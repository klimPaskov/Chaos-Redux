# Achievement implementation prompt for Event 028: Asteroid Incoming

Read the complete Event 028 specification pack, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the project achievement precedents. Implement the five achievement routes from Part 10 without reducing them to event-fired checks.

## Accepted achievement routes

1. Preserve the Near Miss
   - Miss selected at 800 Chaos or above while both evolutions are enabled and eligible
   - Verify that no impact, fragment, dust, or crater transaction occurred

2. Government Beyond the Crater
   - Player is the original intended target
   - The locked center was its capital
   - Government relocates and the same country completes national network and outer-ring recovery inside the accepted deadline

3. Collector of Fallen Stars
   - Extraordinary Minerals active
   - Player directly controls the main crater and at least three fragment sites for the continuous hold period
   - Subject control does not count

4. Piercing the Impossible
   - Enemy controls the main crater and has the active plus 100 percent armour modifier
   - Player takes the main crater through war and holds it for the accepted period

5. A World Reconnected
   - Player was not the original target
   - Opening dust reached Impact Winter or Severe Impact Winter
   - Player completed the highest national protection, observation, and transport actions
   - Global dust later reached zero

Working labels are structural. Write final names and descriptions under the project localisation rules.

## Tracking requirements

- Use persistent flags or variables that survive save and reload.
- Preserve intended target identity separately from current crater controller.
- Reset continuous control timers when any required site is lost.
- Prevent one site from counting several times.
- Apply direct-control and subject-control rules exactly.
- Follow current debug, manual-trigger, difficulty, and achievement disqualification policy.
- Do not depend on temporary event targets after the event chain ends.
- Tie recovery achievements to real state and mission completion, not a button click alone.
- Tie conquest achievement to hostile control transfer, not peaceful state exchange.

## Localisation and icons

- Add final title, description, completion condition, and blocked condition text.
- Create one unique 64x64 completed, grey, and not-eligible icon triplet for each full achievement ID.
- Route icon production through `chaosx_icon_artist` with the Event 028 asset prompt.
- Use the canonical overlay for not-eligible variants.
- Keep all achievement DDS files directly under the root achievement asset folder.

## Documentation and audit

Update the Event 028 docs and achievement coverage table. List every tracking identifier, disqualifier, reset path, and icon path in the handoff.

Validate:

- Save and reload in the middle of every multi-stage achievement
- Loss and recapture of crater sites
- Subject versus direct control
- Capital relocation before and after lock
- Miss at the wrong Chaos tier
- Evolution disabled
- Peaceful transfer versus conquest
- Global dust reaches zero before the player's required actions finish

Do not claim completion with missing icon states, raw working labels, automatic unlocks, or untested continuous-control resets.
