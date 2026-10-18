# Event 039 unit-model repair decisions

Acceptance basis: the user assigned every WP4 ticket in the unit-fix plan and authorized repairs to weak unit presentation.
This record covers model presentation and sound, without changing event gameplay.

## Burst particles

Retain each existing first discharge time and emit one finite vanilla MG flash and one smoke emission per infantry burst.
Remove the two additional flashes at +0.1 and +0.2 seconds and remove `keep_particle` from impulse emitters.
The installed vanilla infantry MG weapon entity emits its flash, smoke and cartridge systems once for a burst; its particle systems contain their own emission cadence.
Repeating that entire system for every round produced the oversized fireball recorded in the showcase.
Shadow Company and Master Assassin inherit the Cadre correction through their existing entity clones.
Cartridge wiring remains dependent on a measured, exported and reimported ejection locator; a muzzle locator cannot stand in for it.

## Mechanized fire

Select the ticket's explicit one-burst-per-cycle option for attack, support attack and defend.
Retain the first existing discharge at 0.7667, 0.9667 and 0.2333 seconds respectively, and remove the second sound event.
Bind each remaining sound and finite flash to the measured `barrel` node.
Use the five installed vanilla mechanized MG recordings through a package-owned soundeffect at vanilla volume 0.45.
Omit the vanilla soundeffect's random 0–0.3 second onset delay so that its event shares the flash time.
Omit playback-rate randomness so that recorded cadence and tail length remain predictable.
The defend cycle is 50 frames at 30 FPS, or 1.6667 seconds; its separate wrapper uses vanilla takes 02–05, whose durations are 1.3680–1.6254 seconds.
Take 01 lasts 1.7908 seconds and stays in the longer attack/support-attack pool, where it fits the cycle.
This is a local soundeffect definition; installed vanilla files are unchanged.

## Evidence and acceptance

The user-authorized existing-assets repair task takes precedence over the skill's normal paid regeneration route.
No paid provider tasks or audio downloads are authorized for this tranche.
The compressed textures and removal of obsolete DDS maps were already delivered by the section 3 owner and are baseline facts, not WP4 production claims.
Current changes, source hashes, particle counts and remaining model/audio gates belong to `docs/plans/unit_fix_2026-10/wp4_gun_troopers_report.md` and its linked evidence.
Visible flash size, grip, recoil, topology, texture separation and live playback acceptance remain independent checks.
